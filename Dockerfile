FROM python:3.9

RUN uname -a
RUN apt update && apt install -y --no-install-recommends python-dev python-setuptools

WORKDIR /srv/project
COPY ../requirements.txt /tmp/requirements.txt
RUN pip install -r requirements.txt

COPY ../blog blog/
COPY commands/ commands/
RUN cmod +rx -R commands
COPY ../Makefile Makefile
#CMD ["python", "./blog/manage.py", "runserver", "0.0.0.0:8111"]

# CMD bash -C "./commands/wsgi_dev.sh"

