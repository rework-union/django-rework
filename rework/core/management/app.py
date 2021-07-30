"""
Django Rework App managements
"""

import os
import re
import subprocess

from .handlers.urls import UrlsHandle
from .. import utils
from ..utils import say


def setup_auth_user_model(content):
    # Setup `AUTH_USER_MODEL` to `basic.User` if adding app is `users`,
    # and generate `basic` App
    result = subprocess.run(["django-admin", "startapp", "basic"])
    if result.returncode != 0:
        say(f'Generate `basic` App failed!', icon='🌶 ', wrap='C')
        return content

    pattern = '# {!AUTH_USER_MODEL}'
    block = """AUTH_USER_MODEL = 'basic.User'"""
    content = content.replace(pattern, block)

    return content


def add(params):
    """Add apps to project"""
    app = params[0].lower()
    say(f'Start adding app: {app}')

    # Add app name to base settings
    settings_file = os.path.join(utils.get_settings_path(), 'base', '__init__.py')
    with open(settings_file, 'r+') as file:
        # check where app in INSTALLED_APPS
        content = file.read()

        app_full_name = f'rework.contrib.{app}'
        installed_apps_pattern = r'INSTALLED_APPS\s*\=\s*\[[\s\S]*?\]'

        installed_apps_match = re.search(installed_apps_pattern, content)
        if not installed_apps_match:
            print('There is no `INSTALLED_APPS` block in your settings')
            return False

        installed_apps_block = installed_apps_match.group()

        for exist_app in re.findall(r"(?<=').*(?=')", installed_apps_block):
            if exist_app == app_full_name:
                say(f'[ERROR] App {app_full_name} is already exists')
                return False

        installed_apps_block = re.sub(
            r'\n]',
            f"\n    '{app_full_name}',\n]",
            installed_apps_block,
        )

        if app == 'users':
            installed_apps_block = re.sub(
                r'\n]',
                f"\n    'basic',\n]",
                installed_apps_block,
            )

        say(f'installed_apps_block {installed_apps_block}')

        content = re.sub(installed_apps_pattern, installed_apps_block, content)

        if app == 'users':
            content = setup_auth_user_model(content)

        say(f'content {content}')
        file.seek(0)
        file.truncate()
        file.write(content)

    # Added include url to root urls
    urls_handler = UrlsHandle()
    urls_handler.add_include_urls(app)

    say('Added completely!')
