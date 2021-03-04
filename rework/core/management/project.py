"""project managements

Using the commands to initialize new project or management existing project
"""

import os
import shutil
import subprocess
from ... import core


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

    print(f'- Initialing project: ``{project}`` using `django-admin` command')
    result = subprocess.run(["django-admin", "startproject", *params])

    if result.returncode != 0:
        print(f'{os.linesep} 🌶 Initialized failed!')
        return False

    # Changed the settings files to satisfy multi environments
    print(f'- Changed the settings files to satisfy multi environments')

    settings_folder = os.path.join(project_dir, project)

    #  1. Make a package named `settings`
    settings_package_path = os.path.join(settings_folder, 'settings')
    base_settings_path = os.path.join(settings_package_path, 'base')
    os.makedirs(base_settings_path)

    #  2. Move origin settings.py to settings/__.init.py
    origin_settings_file = os.path.join(settings_folder, 'settings.py')
    shutil.move(
        origin_settings_file,
        os.path.join(base_settings_path, '__init__.py'),
    )

    #  3. Added multi env setting files
    with open(os.path.join(settings_package_path, 'production.py'), 'w') as f:
        f.write('from .base import *\n')
        f.write('\n')
        f.write('DEBUG = False')

    with open(os.path.join(settings_package_path, 'test.py'), 'w') as f:
        f.write('from .base import *\n')

    with open(os.path.join(settings_package_path, 'development.py'), 'w') as f:
        f.write('from .base import *\n')

    with open(os.path.join(settings_package_path, 'local.py'), 'w') as f:
        f.write('from .base import *\n')

    # Update settings

    # Others

    with open(os.path.join(base_dir, '.editorconfig'), 'w') as f:
        f.write("""# EditorConfig is awesome

# top-most EditorConfig file
root = true

# Unix-style newlines with a newline ending every file
[*]
end_of_line = lf
insert_final_newline = true

# Matches multiple files with brace expansion notation
[*.{js,html,css}]
charset = utf-8
indent_style = space
tab_width = 2

[*.py]
max_line_length = 100

""")

    with open(os.path.join(base_dir, '.gitignore'), 'w') as f:
        f.write("""### Django ###
*.log
*.pot
*.pyc
__pycache__/

# ide
.idea/

# hidden files
.*
!.gitignore
!.editorconfig

# celery
celerybeat.pid

# static generated
static_root/

# virtual env
venv

.doc

settings/local.py
""")
        with open(os.path.join(base_dir, 'requirements.txt'), 'w') as f:
            f.write(f'django-rework=={core.__version__}{os.linesep}')

    print(f'{os.linesep} 🎨 Initialized completely!')
