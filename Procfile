api: /usr/local/bin/gunicorn config.wsgi:application -w 4 -b :8000
task: celery -A jokes.taskapp worker -l info
