include .env

PROJECT_NAME := task_manager
PORT := ${PORT}
HOST := ${HOST}
# PORT := 8000
# HOST := 0.0.0.0

dev:
	poetry run python manage.py runserver


shell:
	poetry run python manage.py shell

superuser:
	poetry run python manage.py createsuperuser

deploy:
	railway up

dev-up: freeze
	docker-compose up

up:
	docker-compose up

show: up migrate

start:
	poetry run uvicorn $(PROJECT_NAME):app --port $(HOST) --reload

start-server:
	gunicorn $(PROJECT_NAME).wsgi --bind $(HOST):$(PORT)

migrate:
	poetry run python manage.py makemigrations && poetry run python manage.py migrate

db:
	docker-compose -f docker-compose.db.yml up

lint:
	poetry run flake8 $(PROJECT_NAME)

freeze:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

install:
	poetry install

rm:
	docker-compose stop && \
	docker-compose rm && \
	sudo rm -rf pgdata/

rm-venv:
	rm -rf `poetry env info -p`
