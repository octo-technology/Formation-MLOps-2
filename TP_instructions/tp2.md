summary: TP2
id: tp2
categories: tp, api
tags: api, flask
status: Published
authors: OCTO Technology
Feedback Link: https://gitlab.com/octo-technology/octo-bda/cercle-formation/dsin2/-/issues/new

# TP2 - Pyramide de tests

## Overview
Duration: 1

### A l'issue de cette section, vous aurez découvert

- Comment écrire un test fonctionnel,
- Comment se servir de `behave`,
- Mesurer des indicateurs de qualité: code coverage et pyramide de tests,

## Tests fonctionnels avec Behave

Dans cette partie, nous allons rédiger un test fonctionnel avec l'outil `Behave`.

Pour cela, il y a un squelette de test fonctionnel à compléter dans `dsin2/tests/test_functional/features/training_workflow.feature`.

Le test correspondant se trouve dans `dsin2/tests/test_functional/features/steps/training_workflow.py`.

## Tests fonctionnels avec Behave dans la CI

Compléter le squelette de test fonctionnel:

- ✅ Il doit passer **en local** avec la commande `behave tests/test_functional/features`.
- ✅ Compléter la chaîne d'intégration continue en exécutant les tests fonctionnels dans le stage `test`.

## Mesure de la qualité du code

Compléter la chaîne d'intégration continue avec une step `qualite` afin de

- mesurer la couverture de tests avec `pytest --cov`,
- mesurer la pyramide de tests avec le script `dsin2/tests/tests_pyramide.sh`.

![test+qualite](./docs/tp2/pipeline-test-qualite-vert.png)