scratch:
	django-admin startproject config .

noidea:
	git rm -r --cached .idea/
env:
	python3 -m venv env && . env/bin/activate
i:
	pip install -r requirements.txt
mig:
	python manage.py makemigrations && python manage.py migrate
cru:
	python manage.py createsuperuser
run:
	python manage.py runserver 0.0.0.0:8000
