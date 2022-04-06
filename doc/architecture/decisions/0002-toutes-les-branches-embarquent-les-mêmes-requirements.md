# 2. Toutes les branches embarquent les mêmes requirements.

Date: 2022-04-06

## Statut

Accepté

## Contexte

Vu qu'on gère plein de branches, ce n'est pas facile de gérer des requirements différents dans requirements.txt.  
Mais notre intention étant de faire en sorte que l'utilisateur fasse un seul `pip install` qui fonctionne à travers toutes les branches, ce n'est pas grave de ne pas gérer "finement" les dépendances.

## Décision

Toutes les branches embarquent les mêmes requirements.txt.

## Conséquences

Lorsqu'un contributeur édite le fichier requirements.txt d'une branche, il doit reporter cette modification sur toutes les branches ouvertes sur le repo.
Test de recette : il ne doit pas y avoir de différences lorsque j'exécute :
`git branch --merged | grep -v \* | xargs -I {} git diff {} master -- requirements.txt`
