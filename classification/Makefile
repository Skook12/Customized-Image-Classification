ifneq ("$(wildcard .env)","")
	include .env
	export
endif

.PHONY: install
install: ## Install Python requirements.
	python -m pip install --upgrade pip setuptools wheel poetry
	poetry add ultralytics
	poetry lock
	poetry install --no-root
	poetry run pre-commit install

.PHONY: run
run: ## Run the project.
	poetry run python src/app/main.py