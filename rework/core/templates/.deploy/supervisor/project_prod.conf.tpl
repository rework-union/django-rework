[program:${project}_prod]
command=gunicorn ${project}.wsgi -b unix:/run/${project}_prod.sock
directory=/opt/projects/${project}-server
environment=DJANGO_SETTINGS_MODULE=${project}.settings.prod
stdout_logfile = /var/log/gunicorn/${project}_prod.log
stderr_logfile = /var/log/gunicorn/${project}_prod_error.log

[program:${project}_celery_prod]
command=celery -A ${project} worker -l info
directory=/opt/projects/${project}-server/
environment=DJANGO_SETTINGS_MODULE=${project}.settings.prod
stdout_logfile = /var/log/celery/${project}_prod.log
stderr_logfile = /var/log/celery/${project}_prod_error.log

[program:${project}_celery_beat_prod]
command=celery -A ${project} beat -l info
directory=/opt/projects/${project}-server/
environment=DJANGO_SETTINGS_MODULE=${project}.settings.prod
stdout_logfile = /var/log/celery/${project}_beat_prod.log
stderr_logfile = /var/log/celery/${project}_beat_prod_error.log
