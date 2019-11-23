release: python manage.py makemigrations game --noinput
release: python manage.py makemigrations user --noinput
release: python manage.py migrate --noinput
web: gunicorn riddle-me-this.wsgi