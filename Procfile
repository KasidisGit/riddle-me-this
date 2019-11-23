release: python manage.py makemigrations user --noinput
release: python manage.py migrate --noinput
release: python manage.py loaddata game.json --noinput
web: gunicorn riddle-me-this.wsgi