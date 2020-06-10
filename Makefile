SHELL := /bin/bash
.SHELLFLAGS = -ec
.ONESHELL:
.SILENT:

.PHONY: help
help:
	echo "❓ Utiliser \`make <target>' où <target> peut être"
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: conda-env  ## créé l'environnement conda python_indus_avancee, et le récréé s'il existe déjà
conda-env:
	conda env create --file requirements.txt --name python_indus_avancee --force --quiet

.PHONY: test-tps  ## lance les tests
test-tps:
	pytest tests

.PHONY: distribution  ## crée le package 
distribution:
	python3 setup.py sdist bdist_wheel
