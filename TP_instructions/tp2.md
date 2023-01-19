summary: TP2
id: tp2
categories: tp, api
tags: api, flask
status: Published
authors: OCTO Technology
Feedback Link: https://github.com/octo-technology/Formation-MLOps-2/issues/new/choose

# TP2 - Pyramide de tests

## Vue d'ensemble
Durée : 30 min

### À l'issue de cette section, vous aurez découvert

- Comment écrire un test fonctionnel,
- Comment se servir de `behave`,
- Mesurer des indicateurs de qualité : code coverage et pyramide de tests,

### Présentation des nouveautés sur la branche de ce TP

Pour ce TP, utilisez la branch 2_starting_test_behave

`git checkout 2_starting_test_behave`

Sur cette branche, il y a maintenant : 
- Un Dossier `tests/test_functional/` qui contient le squelette d'un test fonctionnel.

## Tests fonctionnels avec Behave

Dans cette partie, nous allons rédiger un test fonctionnel avec l'outil `Behave`.

Pour cela, il y a un squelette de test fonctionnel à compléter dans `tests/test_functional/features/training_workflow.feature`.

Le test correspondant se trouve dans `tests/test_functional/features/steps/training_workflow.py`.

## Tests fonctionnels avec Behave dans la CI

Compléter le squelette de test fonctionnel :

- ✅ Il doit passer **en local** avec la commande `behave tests/test_functional/features`.
- ✅ Compléter la chaîne d'intégration continue en exécutant les tests fonctionnels dans le stage `test`.

## Mesure de la qualité du code

Compléter la chaîne d'intégration continue avec une step `qualite` afin de

- mesurer la couverture de tests avec `pytest` en rajoutant l'argument `--cov`,
  - `python -m pytest --cov=formation_indus_ds_avancee/ tests/test_unit/ -vv -p no:warnings`
- mesurer la pyramide de tests en exécutant le script
  - `./tests/tests_pyramid.sh`

![test+qualite](./docs/tp2/pipeline-test-qualite-vert.png)

## Lien vers le TP suivant

Les instructions du tp suivant sont [ici](https://octo-technology.github.io/Formation-MLOps-2/tp3#0)