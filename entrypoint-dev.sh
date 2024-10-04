#!/bin/sh
poetry install
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py runscript load_fixtures
python manage.py runserver 127.0.0.1:8000
exec "$@"