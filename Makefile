APP:=

run:
	python3 manage.py runserver

create_app:
	python3 manage.py startapp $(APP)