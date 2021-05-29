# Описание по запуску gunicorn
MANAGE = python blog/manage.py
PROJECT_DIR=$(shell pwd)
WSGI_PORT=8081

run:
	$(MANAGE) runserver 0.0.0.0:8000
gunicorn-run:
	gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir $(PROJECT_DIR)/blog blog.wsgi --timeout 30 --log-level debug --max-requests 10000
gunicorn-sock:
	gunicorn -w 4 -b unix:/tmp/gunicorn.sock --chdir /mnt/c/Users/user/PycharmProjects/Djan_go/blog blog.wsgi --timeout 30 --log-level debug --max-requests 10000
# Конфиг Nginx Ubuntu
cd /etc/nginx/
touch sites-available/default
ln -s sites-available/default sites-enabled/default
vim default

upstream django {
    server unix:/tmp/gunicorn.sock fail_timeout=0;
}
server {
    listen 80;
    listen [::]:80;
    server_name 127.0.0.1 posts.com;
    
    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
    root /mnt/c/Users/user/PycharmProjects/Djan_go/static_content;
    }
    
    location / {
     proxy_pass http://django;
    }
  }
}    

    
sudo nginx -t
sudo service nginx restart







