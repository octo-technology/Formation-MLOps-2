SHELL := /bin/bash
.SHELLFLAGS = -ec
.ONESHELL:
.SILENT:

.PHONY: help
help:
	echo "❓ Utiliser \`make <target>' où <target> peut être"
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: server  ## 🐍 lance l'application streamlit
server:
	streamlit run embedded_model.py

.PHONY: docker-build  ## 🐳 pour builder l'image docker
docker-build:
	docker build -t embedded-model-app:v1 .

.PHONY: docker-server  ## 🐳 pour lancer l'application streamlit dans docker
docker-server:
	docker run --rm -p 8091:8091 --name embedded-model-app -it embedded-model-app:v1
