"""
Deploy to server 
"""
from ..hosts import get_host_value, connect
from ... import devops
from ...utils import say


class Deploy:
    def __init__(self, c):
        self.c = connect(c)
        self.host_value = get_host_value(c)[1]

        self.project = devops.PROJECT
        self.env = devops.ENV

        self.host = self.host_value.get('host')
        self.port = self.host_value.get('port', 22)
        self.password = self.host_value.get('password')

    def __call__(self, *args, **kwargs):
        if self.env == 'prod':
            root = f'/opt/projects/{self.project}-server/'
            service = f'{self.project}_server'
            branch = 'master'
        elif self.env == 'test':
            root = f'/opt/test-projects/{self.project}-server/'
            service = f'{self.project}_server_test'
            branch = 'test'
        elif self.env == 'dev':
            root = f'/opt/dev-projects/{self.project}-server/'
            service = f'{self.project}_server_dev'
            branch = 'dev'
        else:
            raise Exception('Un-supported Environment to deploy.')

        say(f'Project root is: {root}')

        self.pull(branch, root)
        if kwargs.get('requirements_update'):
            self.update_requirement(root)
        self.migrate(root)
        self.collect_static(root)
        self.copy_uwsgi(root)
        self.restart(service)

    def pull(self, branch, root):
        # Pull latest code
        say('Pull latest code from remote git')
        self.c.run(f'cd {root} && git checkout {branch} && git pull')

    def update_requirement(self, root):
        # Update requirements
        say('install requirements')
        self.c.run(f'cd {root} && python3 -m pip install -r requirements.txt')

    def migrate(self, root):
        # Models migrate
        say('Migrate database')
        self.c.run(
            f'cd {root} && python3 manage.py migrate --settings={self.project}.settings.{self.env}'
        )

    def collect_static(self, root):
        # Collect static
        say('Collect static')
        settings_suffix = f'--settings={self.project}.settings.{self.env}'
        self.c.run(f'cd {root} && python3 manage.py collectstatic {settings_suffix} --no-input')

    def copy_uwsgi(self, root):
        # Copy uwsgi files
        origin = f'{root}.deploy/supervisor/{self.project}_supervisor_{self.env}.conf'
        destination = f'/etc/supervisor/conf.d/'
        self.c.run(f'cp {origin} {destination}')

    def restart(self, service):
        # Restart uwsgi service
        say('Restart the uwsgi service')
        self.c.run(f'supervisorctl restart {service}')
