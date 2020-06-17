SHELL := /bin/bash
.SHELLFLAGS = -ec
.ONESHELL:
.SILENT:

.PHONY: help
help:
	echo "❓ Utiliser \`make <target>' où <target> peut être"
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: conda-env  ## 🐍 créé l'environnement conda python_indus_avancee, et le récréé s'il existe déjà
conda-env:
	conda create -yqf python=3.8 --name embedded_model

.PHONY: dependencies  ## ⏬ installe les dépendances pour embedded_model et formation_indus_avancee
dependences:
	pip install -r requirements.txt && pip install -r ../../requirements.txt

.PHONY: tests  ## ✅ lance tous les tests
tests:
	$(MAKE) tests-unitaires

.PHONY: tests-unitaires  ## ✅ lance les tests unitaires
tests-unitaires:
	python -m pytest . \
		--junitxml=junit/test-results.xml \
		--cov -vv -p no:warnings --cov-report=xml --cov-report=html -v
