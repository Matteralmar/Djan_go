MANAGE = python blog/manage.py
PROJECT_DIR=$(shell pwd)
WSGI_PORT=8081




fill_posts:
	python blog/manage.py fill_posts
run:
	$(MANAGE) runserver 0.0.0.0:8000
gunicorn-run:
	gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir $(PROJECT_DIR)/blog blog.wsgi --timeout 30 --log-level debug --max-requests 10000
collect-static:
	$(MANAGE) collectstatic
gunicorn-sock:
	gunicorn -w 4 -b unix:/tmp/gunicorn.sock --chdir /mnt/c/Users/user/PycharmProjects/Djan_go/blog blog.wsgi --timeout 30 --log-level debug --max-requests 10000