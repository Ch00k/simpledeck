SHELL := /usr/bin/env bash

lint:
	black --diff --check .
	flake8 .
	isort --diff --check-only .
	mypy .

install_devs_prod:
	pip install -r requirements.txt

install_deps_dev:
	pip install -r requirements-dev.txt

install_deps: install_devs_prod install_deps_dev
