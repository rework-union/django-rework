import os
import re
import shutil

from rework import core
from rework.core.utils import copy_template_to_file


class SettingsHandle:
    """
    Handle django settings files
    """

    def __init__(self, project, path):
        self.base_dir = os.getcwd()
        self.project = project
        self.path = path  # settings root path, generally is project name
        self.base_settings_file = None

    def _create_settings_package(self):
        #  1. Make a package named `settings`
        package = os.path.join(self.path, 'settings')
        base_settings_path = os.path.join(package, 'base')
        os.makedirs(base_settings_path)

        #  2. Move origin settings.py to settings/base/__init__.py
        origin_settings_file = os.path.join(self.path, 'settings.py')
        target_settings_file = os.path.join(base_settings_path, '__init__.py')
        shutil.move(origin_settings_file, target_settings_file)

        self.base_settings_file = target_settings_file

    def create_multi_envs(self):
        kwargs = {
            'django_rework_version': core.__version__,
            'project': self.project,
        }
        settings_tpl_path = 'project/settings/'
        envs = ['prod', 'test', 'dev', 'local']
        for env in envs:
            copy_template_to_file(f'{settings_tpl_path}{env}.py', self.base_dir, **kwargs)

    @staticmethod
    def _save(f, content):
        f.seek(0)
        f.truncate()
        f.write(content)

    def _add_tags(self):
        with open(self.base_settings_file, 'r+') as f:
            content = f.read()

            # AUTH_USER_MODEL tag
            content = content.replace(
                '# Password validation', '\n'.join([
                    '# {!AUTH_USER_MODEL}',
                    '',
                    '# Password validation',
                ])
            )
            self._save(f, content)

    def _add_installed_apps(self):
        """Initialize apps pre-installed"""

        with open(self.base_settings_file, 'r+') as f:
            content = f.read()
            content = self._insert_app_to_content(content, 'rest_framework')
            content = self._insert_app_to_content(content, 'rest_framework_simplejwt')
            self._save(f, content)

    @staticmethod
    def _insert_app_to_content(content, app):
        installed_apps_pattern = r'INSTALLED_APPS\s*\=\s*\[[\s\S]*?\]'
        installed_apps_match = re.search(installed_apps_pattern, content)
        if not installed_apps_match:
            print('There is no `INSTALLED_APPS` block in your settings')
            return False

        installed_apps_block = installed_apps_match.group()

        for exist_app in re.findall(r"(?<=').*(?=')", installed_apps_block):
            if exist_app == app:
                return False

        installed_apps_block = re.sub(
            r'\n]',
            f"\n    '{app}',\n]",
            installed_apps_block,
        )

        content = re.sub(installed_apps_pattern, installed_apps_block, content)
        return content

    def _add_rest_framework_setting(self):
        with open(self.base_settings_file, 'r+') as f:
            content = f.read()
            content += """

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

"""
            self._save(f, content)

    def initialize(self):
        self._create_settings_package()
        # Added multi env setting files
        self.create_multi_envs()
        # Added template tag to base/__init__.py
        self._add_tags()
        self._add_installed_apps()
        self._add_rest_framework_setting()
