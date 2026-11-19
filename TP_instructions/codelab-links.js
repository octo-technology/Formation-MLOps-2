// Dans les codelabs générés par claat, le bouton « Done » de la dernière étape et la croix
// en haut à gauche pointent vers la racine du domaine (https://octo-technology.github.io/),
// qui n'existe pas pour ce repo. Ce script les redirige :
// - « Done » vers le TP suivant, donné par l'attribut data-next de la balise <script> qui le
//   charge, ou vers le repo GitHub de la formation pour le dernier TP ;
// - la croix vers le repo GitHub de la formation.
// Le workflow .github/workflows/static.yml ajoute cette balise à chaque page.
(function () {
  var REPO_URL = 'https://github.com/octo-technology/Formation-MLOps-2';
  var next = (document.currentScript && document.currentScript.dataset.next) || REPO_URL;

  function updateLinks() {
    var done = document.querySelector('google-codelab #done');
    var close = document.querySelector('google-codelab #arrow-back');
    if (!done || !close) return false;
    done.setAttribute('href', next);
    close.setAttribute('href', REPO_URL);
    return true;
  }

  // Les boutons n'existent qu'une fois l'élément <google-codelab> affiché : on attend qu'ils apparaissent.
  if (updateLinks()) return;
  var observer = new MutationObserver(function () {
    if (updateLinks()) observer.disconnect();
  });
  observer.observe(document.documentElement, { childList: true, subtree: true });
})();
