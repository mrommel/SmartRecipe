# define the name of the virtual environment directory
VENV := venv

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/python3.12 -m pip install --upgrade pip
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

pylint: venv
	./$(VENV)/bin/pylint data

tests: venv
	./$(VENV)/bin/python3 -m unittest

run: venv
	./$(VENV)/bin/python3 manage.py runserver 8083

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

makemigrations: venv
	./$(VENV)/bin/python3.12 manage.py makemigrations
	./$(VENV)/bin/python3.12 manage.py sqlmigrate data 0027  # change this
	./$(VENV)/bin/python3.12 manage.py migrate

migrate: venv
	./$(VENV)/bin/python3 manage.py migrate


createsuperuser: venv
	./$(VENV)/bin/python3 manage.py createsuperuser
	# admin + forrecipe

# actions

check_media_assets: venv
	./$(VENV)/bin/python3 manage.py check_media_assets

# make sure that all targets are used/evaluated even if a file with same name exists
.PHONY: all venv run clean tests