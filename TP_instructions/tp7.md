summary: TP7 - Exposition de modèles
id: tp7
categories: tp, api
tags: api, flask
status: Published
authors: OCTO Technology
Feedback Link: https://gitlab.com/octo-technology/octo-bda/cercle-formation/dsin2/-/issues/new

# TP7 - Exposition de modèles

## Overview
Duration: 1

### A l'issue de cette section, vous aurez découvert

- Comment fonctionne une simple API Flask,
- Le pattern d'exposition `modèle embarqué`,
- Le pattern d'exposition `model as a service`,
- Le pattern d'exposition `model published as data`,

## Développement d'API avec Flask

Flask est un microserveur d'application. Il est souvent utilisé en Python pour développer des APIs et exposer des ressources.

### Exposition "model as a service"

- Se rendre dans `dsin2/exposition/model_as_a_service/`
- Démarrer le serveur Flask d'exposition avec `FLASK_APP=inference.py python -m flask run`

Le serveur d'exposition est désormais disponible sur le port 5000, avec:

- la route de healthcheck `/health` pour vérifier que le service est fonctionnel,
- la route `/predict` pour demander une prédiction
  - Il est possible de demander une prédiction en spécifiant une valeur pour la feature explicative `Ws1_avg`

![requete-healthcheck](./docs/tp7/ping-healthcheck.png)

Requêter une prédiction pour une `Wind Speed` de 50.