#!/bin/sh

python3 manage.py migrate
python3 manage.py collectstatic --noinput

exec gunicorn main.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 4