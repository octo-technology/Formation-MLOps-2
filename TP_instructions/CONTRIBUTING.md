# CONTRIBUTING

## Getting started

- [ ] Installer [Go](https://golang.org/dl/) si vous l'avez pas déjà,
- [ ] Installer claat, l'outil de génération de fichiers codelabs de Google avec `$> go get -u -v -x github.com/googlecodelabs/tools/claat`

Des instructions détaillées sont disponibles ici: <https://github.com/googlecodelabs/tools/blob/master/sample/codelab.md>

## Génération des TPs au format Codelabs

Il n'est pas pérenne de modifier les fichiers HTML directement, ils seront écrasés à chaque génération de TP codelabs.

Il est préférable de les générer comme suit:

```bash
cd dsin2/TP_instructions;
claat export tp*.md;
```

ou de manière équivalente avec le makefile: `$> make instructions` pour générer les instructions de TP.

La commande `claat export` générera un dossier pour chaque fichier markdown contenant ses sources statiques au format HTML+CSS+JS.

Il est ensuite possible d'ouvrir le fichier `tp1/index.html` dans un navigateur pour consulter le rendu des instructions de TP au format codelabs.

## Créer un nouveau TP

- [ ] Dupliquer le fichier `tp1.md`, nommer la copie comme souhaité (ex: `tp14.md`)
- [ ] Editer le fichier `tp14.md` avec le contenu voulu
  - [ ] Si des pièces sont à joindre (comme des images), les placer dans `docs/tp14/`,
- [ ] Générer le TP au format codelabs avec `$> claat export tp14.md` ou `$> make instructions`.
