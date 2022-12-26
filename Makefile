.PHONY: poetry-install

APP := jargonai

APP_DIR := ./$(APP)
DEV_DEPS := test,dev,docs,sandbox

# Python
PYTHON_BIN := /opt/pysetup/.venv/bin/python3
PYTHON_PIP_BIN := /opt/pysetup/.venv/bin/pip3

# Container Specific Paths
POETRY_DIR := /opt/pysetup
PY_ENV_DIR := /opt/pysetup/.venv

POETRY_CMD := poetry

ifdef REMOTE_CONTAINERS
	POETRY_CMD := poetry --directory $(POETRY_DIR) 
endif

dev-container-start: poetry-install poetry-export-dev poetry-activate


build: 
	docker-compose build 

poetry-install:
	# echo 'Install poetry dependencies'
	$(POETRY_CMD)  install

poetry-export-dev: poetry-install
	# echo 'Export poetry development dependencies'
	$(POETRY_CMD) export --without-hashes --format=requirements.txt >  ./dev.requirements.txt

poetry-export-prod: poetry-install
	# echo 'Export poetry production dependencies'
	$(POETRY_CMD)  export --without-hashes $(DEV_DEPS) --format=requirements.txt > ./requirements.txt

poetry-activate:
	$(POETRY_CMD) shell
