import os
import re


class SettingsHandle:
    """
    Handle django settings files
    """
    def __init__(self, project, path):
        self.base_dir = os.getcwd()
        self.project = project
        self.path = path  # settings root path, generally is project name
        self.base_settings_file = os.path.join(self.path, 'settings.py')

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

    def _add_logging_setting(self):
        with open(self.base_settings_file, 'r+') as f:
            content = f.read()
            content += """

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        "default": {
            "format": '[%(asctime)s: %(levelname)s/%(name)s %(filename)s:%(lineno)d] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
    },
}

"""
            self._save(f, content)

    def initialize(self):
        # Added template tag to settings.py
        self._add_tags()
        self._add_installed_apps()
        self._add_rest_framework_setting()
        self._add_logging_setting()
