all: var/env/bin/django-admin var/db.sqlite3

help:
	@echo 'make ubuntu     install the necessary system packages (requires sudo)'
	@echo 'make            set up the development environment'
	@echo 'make run        start the web server'

ubuntu:
	sudo apt-get update
	sudo apt-get -y build-dep python-lxml python-imaging python-psycopg2
	sudo apt-get -y install python-virtualenv

fedora:
	sudo dnf update
	sudo dnf -y install 'dnf-command(builddep)'
	sudo dnf -y builddep python-lxml python-imaging python-psycopg2
	sudo dnf -y install python-virtualenv

var/env/bin/python:
	virtualenv -p $(shell which python3.4) var/env

var/env/bin/django-admin: var/env/bin/python requirements.txt
	var/env/bin/pip install -r requirements.txt -e .
	touch -c var/env/bin/django-admin

var/db.sqlite3:
	var/env/bin/python manage.py spiritinstall
	var/env/bin/python manage.py createsuperuser --username admin --email admin@example.com

run: all
	var/env/bin/python manage.py runserver

.PHONY: all run
