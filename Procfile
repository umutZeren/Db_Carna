release: python django/manage.py makemigrations --no-input
release: python django/manage.py migrate --no-input

web: gunicorn postgres_api.wsgi