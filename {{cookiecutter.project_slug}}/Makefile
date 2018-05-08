migrate:
	python3 manage.py migrate

makemigrations:
	python3 manage.py makemigrations

run:
	python3 manage.py runserver 0.0.0.0:8000

create-superuser:
	python3 manage.py createsuperuser

d-migrate:
	docker-compose exec {{cookiecutter.project_slug}} python3 manage.py migrate

d-makemigrations:
	docker-compose exec {{cookiecutter.project_slug}} python3 manage.py makemigrations

d-create-superuser:
	docker-compose exec {{cookiecutter.project_slug}} python3 manage.py createsuperuser

gentelella:
	tar -xzvf gentelella.tar.gz -C {{cookiecutter.project_slug}}/static/ && rm {{cookiecutter.project_slug}}/static/gentelella/*

d-collectstatic:
	docker-compose exec {{cookiecutter.project_slug}} python3 manage.py collectstatic --noinput