migrate:
	python3 manage.py migrate

makemigrations:
	python3 manage.py makemigrations

run:
	python3 manage.py runserver 0.0.0.0:8000

create-superuser:
	python3 manage.py createsuperuser

d-migrate:
	dcompose exec {{cookiecutter.project_slug}} python3 manage.py migrate

d-makemigrations:
	dcompose exec {{cookiecutter.project_slug}} python3 manage.py makemigrations

d-create-superuser:
	dcompose exec {{cookiecutter.project_slug}} python3 manage.py createsuperuser