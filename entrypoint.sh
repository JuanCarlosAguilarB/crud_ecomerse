#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=crud_ecomerse.settings.production

echo 'Applying migrations...'
python manage.py wait_for_db --settings=crud_ecomerse.settings.production
python manage.py migrate --settings=crud_ecomerse.settings.production

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=gunicorn --env DJANGO_SETTINGS_MODULE=crud_ecomerse.settings.production crud_ecomerse.wsgi:application --bind 0.0.0.0:8000