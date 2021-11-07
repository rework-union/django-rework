"""
Deploy to server 
"""
import os

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

        # Should reload nginx when it's configurations file changed
        self._should_reload_nginx = False

    def __call__(self, *args, **kwargs):
        # supervisor service name
        service = f'{self.project}_{self.env}'
        if self.env == 'prod':
            env_root = f'/opt/projects/'
            branch = 'master'
        elif self.env == 'test':
            env_root = f'/opt/test-projects/'
            branch = 'test'
        elif self.env == 'dev':
            env_root = f'/opt/dev-projects/'
            branch = 'dev'
        else:
            raise Exception('Un-supported Environment to deploy.')
        root = f'{env_root}{self.project}-server/'

        say(f'Project root is: {root}')

        self.pull(branch, root)

        if kwargs.get('infrastructure'):
            self.setup_infrastructure(root)

        if kwargs.get('requirements_update'):
            self.update_requirement(root)

        self.migrate(root)
        self.collect_static(root)
        self.restart(service)

    def _copy_nginx(self, root):
        """Copy nginx files"""
        nginx_path = f'{root}.deploy/nginx/'

        origin = f'{nginx_path}{self.project}_{self.env}.conf'

        destination = f'/etc/nginx/conf.d/'
        self.c.run(f'cp {origin} {destination}')
        self._should_reload_nginx = True
        say('Copied nginx configuration successfully')

    def _copy_supervisor(self, root):
        """Copy supervisor files

        Compatible with Django-Rework ~0.2:
            supervisor file in django-rework <= 0.2:
                .deploy/supervisor/{self.project}_supervisor_{self.env}.conf
            supervisor file in django-rework >= 0.3:
                .deploy/supervisor/{self.project}_{self.env}.conf
        """
        supervisor_path = f'.deploy/supervisor/'

        origin = f'{supervisor_path}{self.project}_{self.env}.conf'
        if not os.path.exists(origin):
            say(f'Supervisor file: {origin} not exists, try find another...')
            origin = f'{supervisor_path}{self.project}_supervisor_{self.env}.conf'

        origin = f'{root}{origin}'

        destination = f'/etc/supervisor/conf.d/'
        self.c.run(f'cp {origin} {destination}')
        say('Copied supervisor configuration successfully')

    def pull(self, branch, root):
        # Pull latest code
        say('Pull latest code from remote git')
        self.c.run(f'cd {root} && git checkout {branch} && git pull')

    def setup_infrastructure(self, root):
        say('Setup infrastructure')
        self._copy_supervisor(root)
        self._copy_nginx(root)

    def update_requirement(self, root):
        # Update requirements
        say('Install requirements')
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

    def restart(self, service):
        # Restart infrastructure
        say('Restart Supervisor and Nginx(if conf changed)')
        self.c.run(f'supervisorctl restart {service}')
        if self._should_reload_nginx:
            self.c.run(f'nginx -s reload')
