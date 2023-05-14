# include .env

PROJECT_NAME := task_manager
# PORT := ${PORT}
# HOST := ${HOST}
PORT := 8000
HOST := 0.0.0.0


shell:
	poetry run python manage.py shell

superuser:
	poetry run python manage.py createsuperuser

deploy:
	railway up

dev: freeze
	docker-compose up

up:
	docker-compose up

show: up migrate

start:
	poetry run uvicorn $(PROJECT_NAME):app --port $(HOST) --reload

start-server:
	gunicorn $(PROJECT_NAME).wsgi --bind $(HOST):$(PORT)

start-db:
	docker-compose -f docker-compose.db.yml up

lint:
	poetry run flake8 $(PROJECT_NAME)

freeze:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

install:
	poetry install

migrate:
	poetry run python $(PROJECT_NAME)/migration.py

stop:
	docker-compose stop && \
	docker-compose rm && \
	sudo rm -rf pgdata/

rm-venv:
	rm -rf `poetry env info -p`
