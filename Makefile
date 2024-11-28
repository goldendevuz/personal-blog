gen-env:
	python3 -m venv env && . env/bin/activate
migration:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
mig:
	make migration & make migrate
i:
	pip install -r requirements.txt
cru:
	python manage.py createsuperuser --username superuser --email superuser@example.com
run:
	python3 manage.py runserver 8000
freeze:
	pip freeze > requirements.txt