import os
from .say import *


def get_project_name():
    """Determined the project path

    # TODO: the function must be improved
    There will be only one folder in root directory,
    it's the project name
    """
    for path in os.listdir('.'):
        if os.path.isdir(path):
            print('Determined the project path is: ', path)
            return path


def get_project_path(project=None):
    """Determined the project path"""
    base_dir = os.getcwd()
    project = project or get_project_name()
    return os.path.join(base_dir, project)


def get_settings_path(project=None):
    """Determined the project path"""
    base_dir = os.getcwd()
    project = project or get_project_name()
    return os.path.join(base_dir, project, project, 'settings')
