"""
Django Rework App managements
"""

import os
import re

from .. import utils


def add(params):
    """Add apps to project"""

    app = params[0]

    print('Start adding app:', app)

    # Add app name to base settings
    settings_file = os.path.join(
        utils.get_settings_path(), 'base', '__init__.py',
    )
    with open(settings_file, 'r+') as file:
        # check where app in INSTALLED_APPS
        content = file.read()
        print('settings content is', content)

        app_full_name = f'rework.contrib.{app}'
        installed_apps_pattern = r'INSTALLED_APPS\s*\=\s*\[[\s\S]*?\]'

        installed_apps_match = re.search(installed_apps_pattern, content)
        if not installed_apps_match:
            print('There is no `INSTALLED_APPS` block in your settings')
            return False

        installed_apps_block = installed_apps_match.group()

        for exist_app in re.findall(r"(?<=').*(?=')", installed_apps_block):
            if exist_app == app_full_name:
                print(f'[ERROR] App {app_full_name} is already exists')
                return False

        installed_apps_block = re.sub(
            r'\n]', f"\n    '{app_full_name}',\n]",
            installed_apps_block,
        )

        print('installed_apps_block', installed_apps_block)

        content = re.sub(installed_apps_pattern, installed_apps_block, content)
        print('content', content)
        file.seek(0)
        file.truncate()
        file.write(content)

    print('Added completely!')
