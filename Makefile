env:
	python3 -m venv env
act-env:	
	source env/bin/activate
i:
	pip install -r requirements.txt
mig:
	python manage.py makemigrations && python manage.py migrate
cru:
	python manage.py createsuperuser --username superuser --email superuser@example.com
run:
	python3 manage.py runserver 8000

freeze:
	pip freeze > requirements.txt
re-ignore:
	git rm -r --cached .idea/

up:
	make env & make act-env & make i & make mig & make cru & make run