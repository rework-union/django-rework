[program:${project}_test]
command=gunicorn ${project}.wsgi -b unix:/run/${project}_test.sock
directory=/opt/test-projects/${project}-server
stdout_logfile = /var/log/gunicorn/${project}_test.log
stderr_logfile = /var/log/gunicorn/${project}_test_error.log

[program:${project}_celery_test]
command=celery -A ${project} worker -l info
directory=/opt/test-projects/${project}-server/
stdout_logfile = /var/log/celery/${project}_test.log
stderr_logfile = /var/log/celery/${project}_test_error.log

[program:${project}_celery_beat_test]
command=celery -A ${project} beat -l info
directory=/opt/test-projects/${project}-server/
stdout_logfile = /var/log/celery/${project}_beat_test.log
stderr_logfile = /var/log/celery/${project}_beat_test_error.log
