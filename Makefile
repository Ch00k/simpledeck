SHELL := /usr/bin/env bash

lint:
	black --diff --check .
	flake8 .
	isort --diff --check-only .
	mypy .
