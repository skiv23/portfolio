#!/usr/bin/env bash

apt-get update -y
apt-get install -y uwsgi-plugin-python3
cd /code
pip install -r requirements/production.txt
python manage.py migrate
python manage.py collectstatic --noinput
uwsgi --ini /code/docker/portfolio.ini
