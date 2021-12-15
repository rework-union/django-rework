import os
from string import Template
from .say import *


def get_project_name():
    """Determined the project path

    project settings folder contains `wsgi.py`
    """
    for path in os.listdir('.'):
        if os.path.exists(os.path.join(path, 'wsgi.py')):
            say(f'Determined the project path is: {path}')
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

    path = os.path.join(base_dir, project, project, 'settings')
    if os.path.exists(path):
        return path

    path = os.path.join(base_dir, project, 'settings')
    if os.path.exists(path):
        return path

    raise Exception('Determine project path failed!')


def get_root_urls_path(project=None):
    """Determined the root urls path"""
    base_dir = os.getcwd()
    project = project or get_project_name()
    return os.path.join(base_dir, project, 'urls.py')


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

    target = os.path.join(target_path, file_path.replace('project', kwargs.get('project')))
    # Make sure target dir is exists
    target_dir = os.path.dirname(target)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)

    with open(target, 'w') as f:
        f.write(t.substitute(**kwargs))
