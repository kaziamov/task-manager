
migrate:
	poetry run python manage.py makemigrations && poetry run python manage.py migrate

shell:
	poetry run python manage.py shell

superuser:
	poetry run python manage.py createsuperuser

deploy:
	railway up

dev:
	poetry run python manage.py runserver

start:
	poetry run gunicorn task_manager.wsgi