poetry install --only main
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
