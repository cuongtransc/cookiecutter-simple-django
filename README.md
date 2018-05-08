# Cookiecutter Simple Django

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter). Cookiecutter Simple Django is a framework for jumpstarting projects quickly (to write some small web tool, ...).
It is a small version of [cookiecutter-django](https://github.com/pydanny/cookiecutter-django)

## Introduction
This cookie cutter is a very simple boilerplate for starting a website using Django, Celery, Nginx, Docker. It comes with basic project structure and configuration, celery task.

**Features:**
- For django 1.11.10
- Simple web application with bootstrap 4
- Docker support using docker-compose
- Use honcho
- Use MySQL for database, Nginx proxy


**Used packages:**

- [django](https://www.djangoproject.com/) 
- [mysqlclient](https://github.com/PyMySQL/mysqlclient-python)
- [Celery](http://www.celeryproject.org/)
- [gunicorn](http://gunicorn.org/) 

## Usage

Step 1: Init project

`cookiecutter https://github.com/cuongnb14/cookiecutter-simple-django.git`

Step 2: Install requirements

`pip3 install -r requirements.txt`

Step 3: Run

`docker-compose up -d`

Step 4: Migrate database

`make d-migrate`

Access: http://localhost:85. Account: admin/admin. You can remove nginx basic auth in nginx-config