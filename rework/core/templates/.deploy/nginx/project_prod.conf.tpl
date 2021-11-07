server {
    listen       80;
    server_name  {project}.com;

    access_log  /var/log/nginx/${project}_prod.access.log  main;
    error_log /var/log/nginx/${project}_prod.error.log;

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        # we don't want nginx trying to do something clever with
        # redirects, we set the Host: header above already.
        proxy_redirect off;
        proxy_pass http://unix:/run/${project}_prod.sock;
    }

    location /static {
        alias /opt/projects/${project}-server/static_root/;
    }

    location /media {
        alias /opt/projects/${project}-server/media/;
    }

    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
