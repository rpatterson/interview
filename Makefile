# Makefile for Python interview excercises

SHELL=/usr/bin/env bash -o pipefail

## Top level targets

build: .venv/lib/python3.6/site-packages/interview.egg-link $HOME/nltk_data

# Run all tests
test: build
	.venv/bin/flake8
	.venv/bin/coverage run setup.py test
	.venv/bin/coverage report

clean:
	rm -rf .venv


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

# Download the NLTK corpa
# TODO Figure out how to make this repeatable.  IOW, subsequent runs
# should not download a newer version of the corpa.
$HOME/nltk_data:
	.venv/bin/python -m textblob.download_corpora


## Makefile administrivia
.PHONY: build test clean
