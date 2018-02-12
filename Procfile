api: /usr/local/bin/gunicorn config.wsgi:application -w 4 -b :8000
task: celery -A {{cookiecutter.project_slug}}.taskapp worker -l info
