# Makefile for Python interview excercises

SHELL=/usr/bin/env bash -o pipefail

## Top level targets

build: .venv/lib/python3.6/site-packages/interview.egg-link migrate

# Perform any necessary DB migrations
migrate: .venv/lib/python3.6/site-packages/interview.egg-link
	.venv/bin/python manage.py migrate --noinput

# Run development django server for the API
run: build migrate
	.venv/bin/python manage.py runserver

# Run all tests
test: build
	.venv/bin/flake8
	.venv/bin/coverage run manage.py test
	.venv/bin/coverage report

clean:
	rm -rf .venv db.sqlite3


## Real targets

# Set up an isolated Python environment
.venv/bin/python3.6:
	virtualenv -p $$(which python3.6) .venv || (\
		failure=$$? && rm -f .venv/bin/python3.6 && exit $$failure)
# Install the interview code in develop mode
.venv/lib/python3.6/site-packages/interview.egg-link: \
		setup.py setup.cfg .venv/bin/python3.6
	.venv/bin/pip install -e .[test] || (\
		failure=$$? && \
		rm .venv/lib/python3.6/site-packages/interview.egg-link && \
		exit $$failure)


## Makefile administrivia
.PHONY: build migrate run test clean
