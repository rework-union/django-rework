import os

from ..utils import say, copy_template_to_file, get_project_name
from ..utils.command import BaseCommand
from ... import core


class DeployCommand(BaseCommand):
    def handle(self, params):
        if params == ['--init']:
            # template variables
            project = get_project_name()
            kwargs = {
                'django_rework_version': core.__version__,
                'project': project,
            }
            deploy_path = os.path.join(self.base_dir, 'deploy')

            copy_queues = [
                ('.deploy/nginx/project_prod.conf', deploy_path),
                ('.deploy/nginx/project_test.conf', deploy_path),
                ('.deploy/supervisor/supervisord.conf', deploy_path),
                ('.deploy/supervisor/project_prod.conf', deploy_path),
                ('.deploy/supervisor/project_test.conf', deploy_path),
            ]
            for q in copy_queues:
                copy_template_to_file(q[0], self.base_dir, **kwargs)

            say('Deploy files copied successfully')

        else:
            say('Unknown command args!')

    def __call__(self, params):
        return self.handle(params)
