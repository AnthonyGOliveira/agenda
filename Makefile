APP:=
USERNAME:=

run:
	python3 manage.py runserver

create_app:
	python3 manage.py startapp $(APP)

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

createsuperuser:
	python3 manage.py createsuperuser

changepassword:
	python3 manage.py changepassword $(USERNAME)

collectstatic:
	python3 manage.py collectstatic
