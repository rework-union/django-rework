### Django ###
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
!.style.yapf
!.deploy

# celery
celerybeat.pid

# static generated
static_root/

# virtual env
venv

.doc

# Django local settings
**/settings/local.py
**/settings/dev.local.py

# Fabric deploy key files
.deploy/*.pem
