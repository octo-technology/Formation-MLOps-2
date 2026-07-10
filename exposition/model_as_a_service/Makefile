SHELL := /bin/bash
.SHELLFLAGS = -ec
.ONESHELL:
.SILENT:

.PHONY: help
help:
	echo "❓ Utiliser \`make <target>' où <target> peut être"
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: inference-service  ## 🐍 lancer le service d'inférence
inference-service:
	uv run uvicorn inference:app --host 0.0.0.0 --port 5000

.PHONY: docker-build-inference-service  ## 🐳 pour builder l'image docker du service d'inférence (FastAPI)
docker-build-inference-service:
	docker build -f dockerfile-inference-service -t inference-service:v1 .

.PHONY: docker-inference-service  ## 🐳 pour lancer le service d'inférence dans docker
docker-inference-service:
	docker run --rm -p 5000:5000 --name inference-service -it inference-service:v1

.PHONY: app  ## 🐍 lancer l'application de dashboarding (app streamlit)
app:
	uv run streamlit run app.py --server.port 8092

.PHONY: docker-build-app  ## 🐳 pour builder l'image docker de l'application de dashboarding (app streamlit)
docker-build-app:
	docker build -f dockerfile-app -t app:v1 .

.PHONY: docker-app  ## 🐳 pour lancer l'application de dashboard (app streamlit)
docker-app:
	docker run --rm -p 8092:8092 --name app -it app:v1
