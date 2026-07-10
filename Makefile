SHELL := /bin/bash
.SHELLFLAGS = -ec
.ONESHELL:
.SILENT:

.EXPORT_ALL_VARIABLES:
REPO_DIRECTORY:=$(shell pwd)
AIRFLOW_HOME?=${REPO_DIRECTORY}/airflow
PYTHONPATH:=${PYTHONPATH}:${REPO_DIRECTORY}

.PHONY: help
help:
	echo "❓ Utiliser \`make <target>' où <target> peut être"
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: install  ## 🐍 créé l'environnement conda python_indus_avancee, et le récréé s'il existe déjà
install:
	uv sync --locked --all-groups

.PHONY: validation  ## ✅ lance tous les validation
validation:
	uv run ruff check .
	$(MAKE) tests-unitaires && $(MAKE) tests-fonctionnels

.PHONY: tests-unitaires  ## ✅ lance les tests unitaires
tests-unitaires:
	uv run pytest

.PHONY: tests-fonctionnels  ## ✅ lance les tests fonctionnels
tests-fonctionnels:
	uv run behave tests/test_functional/features/

.PHONY: distribution  ## 📦 crée le package au format wheel
distribution:
	uv build

.PHONY: instructions  ## 📄 Génère les instructions de TPs au format codelabs
instructions:
	$(MAKE) -C TP_instructions/ instructions

.PHONY: dataset  ## 🔽 télécharge les données et les dézippe dans le dossier data/
dataset:
	# le lien d'origine https://opendata-renewables.engie.com/media/datasets/01c55756-5cd6-4f60-9f63-2d771bb25a1a.zip est mort
	# solution de contournement en hébergeant le dataset directement sur github
	curl -L https://github.com/Loubout/la_haute_borne_data/raw/main/la-haute-borne-data-2017-2020.csv \
  		-o data/la-haute-borne-data-2017-2020.csv

.PHONY: airflow-setup  ## 💨  Initialize airflow backend: initdb > variables > connections
airflow-setup:
	echo "AIRFLOW_HOME is: ${AIRFLOW_HOME}"
	uv run airflow db

.PHONY: airflow-webserver  ## 🌐  Run airflow web server
airflow-webserver:
	echo "AIRFLOW_HOME is: ${AIRFLOW_HOME}"
	uv run airflow api-server

.PHONY: airflow-scheduler  ## 🌐  Run airflow scheduler
airflow-scheduler:
	echo "AIRFLOW_HOME is: ${AIRFLOW_HOME}"
	uv run airflow scheduler



.PHONY: airflow-pod-processor  ## 🌐  Run airflow pod-processor
airflow-pod-processor:
	echo "AIRFLOW_HOME is: ${AIRFLOW_HOME}"
	uv run airflow pod-processor

