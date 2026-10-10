// Ressources : recherche dédiée (nom, type, pourquoi, site, thème, rubrique) et pastilles de type.
// Accueil : les ressources trouvées remplacent les blocs par thème. Page de thème : la liste se filtre sur place.
// Tous les mots saisis doivent figurer ; un nom qui les contient remonte en tête. ?cherche=… pré-remplit la recherche (?q= ouvrirait celle du site).
(function () {
  function norm(s) {
    return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
  }

  function init() {
    var article = document.querySelector("article.md-content__inner");
    var input = article && article.querySelector("input.kw-rs-filter");
    if (!input) return;
    var items = Array.prototype.slice.call(article.querySelectorAll(".kw-rs-list .kw-tuto[data-search]"));
    var results = article.querySelector(".kw-rs-results");
    var browse = article.querySelector(".kw-rs-browse");
    var count = article.querySelector(".kw-rs-count");
    var types = article.querySelectorAll(".kw-types [data-type]");
    var grid = results && results.querySelector(".kw-rs-list");
    var type = "";
    items.forEach(function (it, i) {
      it._search = norm(it.dataset.search);
      it._name = norm(it.dataset.name || "");
      it._rank = i;
    });

    function apply() {
      var words = norm(input.value.trim()).split(/\s+/).filter(Boolean);
      var active = words.length > 0 || !!type;
      var hits = [];
      items.forEach(function (it) {
        var ok = words.every(function (w) { return it._search.indexOf(w) >= 0; }) && (!type || it.dataset.type === type);
        it.hidden = !ok;
        if (ok) hits.push(it);
      });
      if (grid) {                                   // accueil : les noms trouvés d'abord, puis l'ordre des thèmes
        hits.sort(function (a, b) {
          var na = words.every(function (w) { return a._name.indexOf(w) >= 0; }) ? 0 : 1;
          var nb = words.every(function (w) { return b._name.indexOf(w) >= 0; }) ? 0 : 1;
          return na - nb || a._rank - b._rank;
        });
        hits.forEach(function (it) { grid.appendChild(it); });
        results.hidden = !active;
        if (browse) browse.hidden = active;
      }
      article.querySelectorAll(".kw-rs-list .kw-chapter").forEach(function (ch) {   // rubrique sans résultat
        ch.hidden = active && !ch.querySelector(".kw-tuto[data-search]:not([hidden])");
      });
      types.forEach(function (c) { c.classList.toggle("is-active", c.dataset.type === type); });
      if (count) {
        count.hidden = !active;
        count.textContent = hits.length === 0 ? "Aucune ressource ne correspond."
          : hits.length + (hits.length > 1 ? " ressources trouvées" : " ressource trouvée")
            + (type ? " · type « " + type + " »" : "");
      }
    }

    input.addEventListener("input", apply);
    input.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { input.value = ""; type = ""; apply(); }
    });
    types.forEach(function (c) {
      c.addEventListener("click", function () {
        type = type === c.dataset.type ? "" : c.dataset.type;
        apply();
      });
    });
    var q = new URLSearchParams(location.search).get("cherche");
    if (q) { input.value = q; apply(); }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
