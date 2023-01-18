summary: TP5
id: tp5
categories: tp, artifacts
tags: artifacts
status: Published
authors: OCTO Technology
Feedback Link: https://github.com/octo-technology/Formation-MLOps-2/issues/new/choose

# TP5 - Artefacts

## Vue d'ensemble
Durée : 15 min

### À l'issue de cette section, vous aurez découvert

- Une stratégie simple de versioning de modèles,
- Un timestamp est un bon moyen pour versionner les modèles,
- Mais il est difficile de retrouver quel code a produit quel modèle.

### Présentation des nouveautés sur la branche de ce TP

Pour ce TP, utilisez la branch 5_starting_artifacts

`git checkout 5_starting_artifacts`

## Versionner les modèles avec un timestamp

Pour l'instant, les modèles sont sauvegardés par la fonction `train_model`.

Ils possèdent le même nom de fichier, ce qui signifie que chaque entraînement produit un modèle, mais que le modèle ainsi produit écrase le précédent 😕.

Ceci est problématique pour des raisons

- de suivi et d'auditabilité : un modèle est déployé, mais je ne sais pas lequel précisément.
- de reproductibilité : comme je ne sais pas quel modèle est déployé, je ne peux pas facilement effectuer un roll-back vers un précédent modèle plus stable si le modèle que je viens de déployer est défectueux.

Un moyen de distinguer un modèle d'un autre à chaque entraînement est *d'intégrer un identifiant unique à son nom*.

Un moyen simple d'y parvenir est d'utiliser un horodatage.

**L'objectif de ce TP est de modifier le nom du modèle généré en intégrant un timestamp au format YYYYMMDD-HHMMSS (`'%Y%m%d-%H%M%S'`).**

Exécuter plusieurs entraînements devrait produire plusieurs modèles identifiables comme ceci dans votre *model registry* :

![model-registry](./docs/tp5/model-registry.png)

- A quoi ce timestamp sert-il ?
- Quelles limitations voyez-vous à cette technique ?
