; Testing environment and Production environment is in the same server,
; So the supervisord.conf include both environment's settings.

[unix_http_server]
file=/etc/tmp/supervisor.sock                       ; path to your socket file
 
[supervisord]
logfile=/var/log/supervisor/supervisord.log                     ; supervisord log file
logfile_maxbytes=50MB                           ; maximum size of logfile before rotation
logfile_backups=10                              ; number of backed up logfiles
loglevel=error                                  ; info, debug, warn, trace
pidfile=/etc/tmp/supervisor/supervisord.pid                     ; pidfile location
nodaemon=false                                  ; run supervisord as a daemon
minfds=1024                                     ; number of startup file descriptors
minprocs=200                                    ; number of process descriptors
user=root                                       ; default user

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
 
[supervisorctl]
serverurl=unix:///etc/tmp/supervisor.sock           ; use a unix:// URL  for a unix socket

[include]
files = /etc/supervisor/conf.d/*.conf
