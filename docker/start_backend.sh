#!/bin/sh

cd /code

cp -n env.sample .env

pip install -r requirements/docker.txt

python manage.py migrate
python manage.py runserver 0.0.0.0:8000