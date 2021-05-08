import os
from string import Template
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


def copy_template_to_file(file_path, target_path, **kwargs):
    """
    copy from template to create project file

    template path is `${file_path}+.tpl`

    :params file_path: human readable file path
    :params full_file_path:
    """
    template_base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
    template_path = os.path.join(template_base_path, f'{file_path}.tpl')

    with open(template_path) as f:
        content = f.read()

    t = Template(content)

    target = os.path.join(target_path, file_path)
    with open(target, 'w') as f:
        f.write(t.substitute(**kwargs))
