summary: TP1 - Introduction à la CI/CD
id: tp1
categories: CI
tags: CI,CD,gitlab
status: Published
authors: OCTO Technology
Feedback Link: https://gitlab.com/octo-technology/octo-bda/cercle-formation/dsin2/-/issues/new

# TP1 - Introduction à la CI/CD

## Overview
Duration: 1

### A l'issue de cette section, vous aurez découvert:

- 📄Comment lire un fichier de pipeline `.gitlab-ci.yml`, totototot
- 🚀Comment exécuter un pipeline gitlab, manuellement ou via commit & push
- 🖊Comment éditer un pipeline gitlab,
- ✅Comment tester le fonctionnement d'une application Python dans une chaîne d'intégration continue,
- ✔ Comment mesurer la qualité d'une application Python dans une chaîne de CI,
- 📦Comment packager une application Python dans une chaîne de CI, au format `wheel` et `docker`,
- 🐳Comment manipuler les registres gitlab pour Python et Docker.

## Créer un compte sur Gitlab
Duration: 2

### Création du compte

Rendez-vous sur le site de gitlab afin de créer un compte si vous n'en possédez pas déjà un: <https://gitlab.com/users/sign_in>.

Puis, cliquer sur `Register now`:

![Page de connexion à gitlab.com](./docs/tp1/gitlab-sign-in-page.png)

### Fork du repo de TP dans votre espace personnel gitlab

Une fois votre compte créé, rendez-vous sur la page du repository de code de cette formation: <https://...>

Puis `forkez` le repo à l'aide du bouton en haut à droite pour récupérer une copie de ce dernier dans votre espace gitlab personnel:

![bouton fork](docs/tp1/gitlab-fork-button.png)

🏁 Vous possédez désormais une copie personnelle du repo de code pour les TPs ! Nous allons désormais la cloner dans votre environnement de développement.

## Préparer son environnement et cloner le repo
Duration: 3

Rendez-vous sur votre environnement de développement. L'url de ce dernier vous sera communiqué pendant la formation.

Dans VSCode, ouvrez un terminal afin d'y cloner le repository de code des TPs avec la commande `$> git clone <url>;`. Vous trouverez l'URL de clonage en HTTPS sur gitlab, dans le repo que vous avez cloné:

![bouton clonage](docs/tp1/gitlab-clone-button.png)

<!-- ------------------------ -->
## Exécuter le pipeline de CI
Duration: 1

Un pipeline de CI est déjà présent dans ce repo, nous allons l'exécuter.

Dans le panneau de gauche, rendez-vous dans: `CI/CD` > `Pipelines`.

Puis cliquez sur `Run pipeline`: ![run pipeline](./docs/tp1/gitlab-run-pipeline.png) et valider le formulaire de déclenchement sur la branche `master`.

❌Malheureusement, le pipeline a échoué ...

![pipeline tests rouge](./docs/tp1/gitlab-pipeline-tests-rouge.png)

Il va falloir le faire passer au vert !

## Un mot sur les pipelines Gitlab

`Gitlab CI/CD` est un outil mis à disposition de Gitlab pour construire des pipelines de traitements.

Ces pipelines peuvent être utilisés à des fins d'intégration continue.

Le pipeline est décrit au travers de code, dans un fichier [.gitlab-ci.yml](../../.gitlab-ci.yml), à la racine du repo en langage [`YAML`](https://learnxinyminutes.com/docs/fr-fr/yaml-fr/), une spec de configuration similaire au `JSON`.

La documentation de gitlab ainsi que les mot-clefs utilisables dans le `.gitlab-ci.yml` sont consultables sur <https://docs.gitlab.com/ee/ci/yaml/README.html>.

### Exemple décrit en Python

Un exemple officiel en Python est disponible sur le repository Gitlab de Gitlab: <https://gitlab.com/gitlab-org/gitlab/-/blob/master/lib/gitlab/ci/templates/Python.gitlab-ci.yml>, nous allons le décrire briévement ci-après:

```yaml
## Un exemple de fichier .gitlab-ci.yml

# Le pipeline va s'exécuter dans une image docker.
# En l'ocurrence, il s'agit de l'image python officielle
# la plus à jour dans le dockerhub: https://hub.docker.com/r/library/python/tags/
image: python:latest

# Il est possible de définir des variables d'environnement
# qui seront disponibles dans la suite du pipeline.
variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

# Une étape nommée "test" est ajoutée au pipeline
test:
  script:
    - python setup.py test
    - pip install tox flake8  # you can also use tox
    - tox -e py36,flake8

# Une étape nommé "run" est ajoutée au pipeline.
# Elle s'exécutera si l'étape "test" se termine avec succès.
run:
  script:
    - python setup.py bdist_wheel
  # La direction "artifacts" permet de sauvegarder
  # des objets construits lors de l'exécution du pipeline.
  artifacts:
    paths:
      - dist/*.whl

# Une étape nommé "pages" est ajoutée au pipeline.
# Elle s'exécutera si l'étape "run" se termine avec succès.
pages:
  script:
    - pip install sphinx sphinx-rtd-theme
    - cd doc ; make html
    - mv build/html/ ../public/
  artifacts:
    paths:
      - public
  # Cette étape "pages" ne s'exécutera que si l'étape précédente ("run") est réussie
  # ET si la branche d'exécution du pipeline est master.
  only:
    - master
```

## Exercice: faire passer les tests au vert dans la CI
Duration: 1

Votre mission si vous l'acceptez: éditez le fichier `.gitlab-ci.yml` à la racine du repository pour exéuter les tests avec succès et faire passer le pipeline au vert ✅.
