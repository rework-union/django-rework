"""project managements

Using the commands to initialize new project or management existing project
"""

import os
import subprocess

from .handlers.settings import SettingsHandle
from ..utils import say, copy_template_to_file
from ... import core


def init(params):
    """Initialize django rework project"""

    project = params[0]

    base_dir = os.getcwd()
    project_dir = base_dir

    say(f'Initialing project: ``{project}`` using `django-admin` command')
    result = subprocess.run(["django-admin", "startproject", *params])

    if result.returncode != 0:
        say(f'Initialized failed!', icon='🌶 ', wrap='C')
        return False

    # Changed the settings files to satisfy multi environments
    say(f'Changed the settings files to satisfy multi environments')
    settings_folder = os.path.join(project_dir, project)
    settings_handler = SettingsHandle(project=project, path=settings_folder)

    # template variables

    kwargs = {
        'django_rework_version': core.__version__,
        'project': project,
    }

    settings_handler.initialize()

    # fabric DevOps
    copy_template_to_file('fabfile.py', base_dir, **kwargs)

    # Others
    copy_template_to_file('.editorconfig', base_dir, **kwargs)
    copy_template_to_file('.gitignore', base_dir, **kwargs)
    copy_template_to_file('.style.yapf', base_dir, **kwargs)
    copy_template_to_file('requirements.txt', base_dir, **kwargs)

    say(f'Initialized completely!', icon='🎨', wrap='C')
