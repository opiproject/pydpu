# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.
.PHONY: clean clean-build clean-pyc clean-test clean-proto help lint build docker format test proto
.DEFAULT_GOAL := help
SHELL=/bin/bash

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test clean-proto ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

clean-proto: ## remove auto-generated protocol buffers
	rm -fr /tmp/opi-api

lint: ## lint the code
	poetry run black --check .
	poetry run isort --check .
	poetry run bandit -r pydpu
	poetry run flake8 pydpu tests

format: ## format the code
	poetry run isort .
	poetry run black .

test: ## run tests
	poetry run pytest -v --cov pydpu

coverage: test ## show coverage report
	poetry run coverage report -m
	poetry run coverage html
	$(BROWSER) htmlcov/index.html

build: clean ## builds source and wheel package
	poetry build
	ls -l dist

docker: clean ## build docker image
	docker build . -t pydpu:$(TAG)

proto: clean ## auto-generate protocol buffers
	git clone https://github.com/opiproject/opi-api.git "/tmp/opi-api"
	cd "/tmp/opi-api/security" && $(MAKE)
	cd "/tmp/opi-api/storage" && $(MAKE)
	cd "/tmp/opi-api/network/cloud" && $(MAKE)
	cd $(git rev-parse --show-toplevel)
	rsync --exclude=__*.py /tmp/opi-api/common/v1/gen/python/*.py ./pydpu/proto/v1/
	rsync --exclude=__*.py /tmp/opi-api/security/v1/gen/python/*.py ./pydpu/proto/v1/
	rsync --exclude=__*.py /tmp/opi-api/storage/v1alpha1/gen/python/*.py ./pydpu/proto/v1/
	rsync --exclude=__*.py /tmp/opi-api/network/cloud/v1alpha1/gen/python/*.py ./pydpu/proto/v1/
	rsync --exclude=__*.py /tmp/opi-api/network/evpn-gw/v1alpha1/gen/python/*.py ./pydpu/proto/v1/
