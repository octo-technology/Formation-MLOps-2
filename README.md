# Formation Industrialisation d'un projet de data science avancée

## Introduction
On retrouve dans ce dépôt de code, tout le code relatif aux TPs de la formation DSIN2. Ces TPs sont à réaliser sur l'environnement de TP nommé dslab.

## Avant la formation  
 - [ ] Récupérer les slides de la formation
 - [ ] Déployer et installer l'environnement de TP sur AWS
 
### Récupérer les slides de la formation
Les dernières slides de la formation DSIN2 sont disponibles sur le [Drive d'OCAC](https://drive.google.com/drive/folders/1yeeUWUCE1QPrsFcvEKmdHeq_hxnewpql). 

Cette version des slides est utilisée par tous les formateurs, il est donc préférable de ne pas la modifier directement.

Tu veux changer certaines slides ou améliorer le contenu global de la présentation ?
1. Duplique la dernière version des slides
2. Renomme le nouveau document en incrémentant la version (1.0.0 -> 2.0.0 pour une édition majeure, 1.0.0 -> 1.1.0 pour de l'ajout de contenu, 1.0.0 -> 1.0.1 pour des petits correctifs)
3. Apporte ta proposition au nouveau document et indique le contenu de ta proposition dans le changelog des slides
4. Partage à tes pairs qui donnent cette formation via un issue sur gitlab

### Déployer et installer l'environnement de TP sur AWS
Pour le setup de dans l'environnement de TP, ça se passe sur le dépôt de code [dslab](https://gitlab.com/octo-technology/les-bg-de-la-data/s-s-all/formation/dslab).

## Les TPs
Pour suivre ces TPs, nous allons utiliser les pages gitlab suivantes :

[TP 0 Installation de l'environnement](https://octo-technology.github.io/Formation-MLOps-2/tp0#0)

[TP 1 Mise en place de la CI](https://octo-technology.github.io/Formation-MLOps-2/tp1#0)

[TP 2 Test behave](https://octo-technology.github.io/Formation-MLOps-2/tp2#0)

[TP 3 Infra as code](https://octo-technology.github.io/Formation-MLOps-2/tp3#0)

[TP 4 Orchestration](https://octo-technology.github.io/Formation-MLOps-2/tp4#0)

[TP 5 Artefacts](https://octo-technology.github.io/Formation-MLOps-2/tp5#0)

[TP 6 Model registry](https://octo-technology.github.io/Formation-MLOps-2/tp6#0)

[TP 7 Exposition](https://octo-technology.github.io/Formation-MLOps-2/tp7#0)

[TP 8 Monitoring](https://octo-technology.github.io/Formation-MLOps-2/tp8#0)

## Modifier les TPs, 

### Modifier les instructions
Si tu souhaites modifier les instructions, il faut modifier les `.md` dans la branche de dev puis push. La CI s'occupera 
propager les modifications sur master et de publier les pages.

### Modifier le code
La branche de dev est la branche principale qui contient toutes les solutions, les autre branches contiennent une version 
partielle du code pour faire un TP.

Si vous souhaitez apporter des modifications, il convient de la faire sur dev puis de la propager sur toutes les branches 
pertinentes en faisant `git log --oneline` sur dev pour récupérer le hash de commit, puis sur chaque branche

```shell
git checkout branch
git cherry-pick <commihash>
git push
```

Or to run it on many branches at once, here on branch 0 to 7
```shell
 git branch -a  | grep remotes/origin/[0-7] | cut  -c18- | xargs -I b git checkout b; git cherry-pick >>commit-hash<<; git push
```
