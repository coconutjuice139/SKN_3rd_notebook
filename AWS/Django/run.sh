#!/bin/sh

# nginx로 static 주기
python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input

#gunicorn으로 django를 띄움
gunicorn config.wsgi:application --bind 0.0.0.0:8000 &


unlink /etc/nginx/sites-enabled/default
nginx -g 'daemon off;'