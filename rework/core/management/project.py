"""project managements

Using the commands to initialize new project or management existing project
"""

import os
import shutil
import subprocess

from ..utils import say, copy_template_to_file
from ... import core


def add_tags_to_base_settings(file_path):
    with open(file_path, 'r+') as f:
        content = f.read()

        # AUTH_USER_MODEL tag
        content = content.replace(
            '# Password validation', '\n'.join([
                '# {!AUTH_USER_MODEL}',
                '',
                '# Password validation',
            ])
        )

        f.seek(0)
        f.truncate()
        f.write(content)


def init(params):
    """Initialize django rework project"""

    project = params[0]
    try:
        path = params[1]
    except IndexError:
        path = None

    base_dir = os.getcwd()

    # when path is current dir, project dir is base dir
    if path == '.':
        project_dir = base_dir
    else:
        project_dir = os.path.join(base_dir, project)

    say(f'Initialing project: ``{project}`` using `django-admin` command')
    result = subprocess.run(["django-admin", "startproject", *params])

    if result.returncode != 0:
        say(f'Initialized failed!', icon='🌶 ', wrap='C')
        return False

    # Changed the settings files to satisfy multi environments
    say(f'Changed the settings files to satisfy multi environments')

    settings_folder = os.path.join(project_dir, project)

    # template variables
    kwargs = {
        'django_rework_version': core.__version__,
        'project': project,
    }

    #  1. Make a package named `settings`
    settings_package_path = os.path.join(settings_folder, 'settings')
    base_settings_path = os.path.join(settings_package_path, 'base')
    os.makedirs(base_settings_path)

    #  2. Move origin settings.py to settings/base/__init__.py
    origin_settings_file = os.path.join(settings_folder, 'settings.py')
    target_settings_file = os.path.join(base_settings_path, '__init__.py')
    shutil.move(origin_settings_file, target_settings_file)

    # Added template tag to base/__init__.py
    add_tags_to_base_settings(target_settings_file)

    #  3. Added multi env setting files
    settings_tpl_path = 'project/settings/'
    envs = ['prod', 'test', 'dev', 'dev.local']
    for env in envs:
        copy_template_to_file(f'{settings_tpl_path}{env}.py', base_dir, **kwargs)

    # Update settings

    # fabric DevOps
    copy_template_to_file('fabfile.py', base_dir, **kwargs)

    # Others
    copy_template_to_file('.editorconfig', base_dir, **kwargs)
    copy_template_to_file('.gitignore', base_dir, **kwargs)
    copy_template_to_file('requirements.txt', base_dir, **kwargs)

    print(f'{os.linesep} 🎨 Initialized completely!')
