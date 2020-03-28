import os
import shutil
import subprocess


def init(params):
    """Initialize django rework project"""

    project = params[0]
    base_dir = os.getcwd()
    project_dir = os.path.join(base_dir, project)

    print('Start initialing project:', project)

    # Start a django project using `django-admin` command
    print('Start a django project using `django-admin` command')
    result = subprocess.run(["django-admin", "startproject", project])

    if result.returncode != 0:
        print('Initialized failed!')
        return False

    # Changed the settings files to satisfy multi environments
    print('Changed the settings files to satisfy multi environments')

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
# Set default charset
[*.{js,html,css}]
charset = utf-8

# Tab indentation (no size specified)
[*.{js,html,css}]
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
            f.write("django-rework==0.1.1\n")

    print('Initialized completely!')
