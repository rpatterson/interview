# Makefile for the camera simulation in the Verkada coding assignment

SHELL=/usr/bin/env bash -o pipefail

## Top level targets

build: .venv/lib/python3.6/site-packages/verkada-assignment-camera.egg-link
# Build the container
	docker-compose -f ../docker-compose.yml build camera

# Upgrade all requirements to the latest versions allowed by setup.py
upgrade: clean .venv/bin/python3.6
	.venv/bin/pip install -U .
	.venv/bin/pip freeze >requirements.txt

# Run all tests
test: build
	.venv/bin/flake8
	.venv/bin/coverage run setup.py test
	.venv/bin/coverage report
# Run the tests in the container
	docker-compose -f ../docker-compose.yml run camera setup.py test

clean:
	docker-compose down --rmi all -v
	rm -rf .venv


## Real targets

# Set up an isolated Python environment
.venv/bin/python3.6:
	virtualenv -p $$(which python3.6) .venv || (\
		failure=$$? && rm -f .venv/bin/python3.6 && exit $$failure)
# Install the camera code in develop mode
.venv/lib/python3.6/site-packages/verkada-assignment-camera.egg-link: \
		setup.py setup.cfg .venv/bin/python3.6
	.venv/bin/pip install -e .[test] || (\
		failure=$$? && \
		rm .venv/lib/python3.6/site-packages/verkada-assignment-camera.egg-link && \
		exit $$failure)


## Makefile administrivia
.PHONY: build upgrade test clean
