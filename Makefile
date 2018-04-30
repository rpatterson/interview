# Makefile for the Verkada coding assignment 

SHELL=/usr/bin/env bash -o pipefail

## Top level targets

build:
	$(MAKE) -C api build
	$(MAKE) -C camera build

# Run the camera and the API server
run:
	$(MAKE) -j 2 run-camera run-api
run-camera:
	$(MAKE) -C camera run
run-api:
	$(MAKE) -C api run

# Run all tests
test:
	$(MAKE) -C api test
	$(MAKE) -C camera test

clean:
# Clean the docker containers as much as docker-compose supports
	docker-compose down --rmi all -v

	$(MAKE) -C api clean
	$(MAKE) -C camera clean


## Makefile administrivia
.PHONY: build run run-camera run-api test clean
