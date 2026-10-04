// Analyses : filtre des listes (titre, thèse, auteur, sujets), pastilles de sujets qui le remplissent et
// pastilles de nature de document (rapport, essai…) qui se combinent avec lui.
(function () {
  function norm(s) {
    return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
  }

  function init() {
    var article = document.querySelector("article.md-content__inner");
    var input = article && article.querySelector("input.kw-an-filter");
    if (!input) return;
    var items = article.querySelectorAll(".kw-an-list .kw-tuto[data-search]");
    var chips = article.querySelectorAll(".kw-subjects [data-filter]");
    var types = article.querySelectorAll(".kw-types [data-type]");
    var type = "";

    function apply() {
      var q = norm(input.value.trim());
      items.forEach(function (it) {
        it.hidden = (q && norm(it.dataset.search).indexOf(q) < 0) || (type && it.dataset.type !== type);
      });
      article.querySelectorAll(".kw-an-list .kw-chapter").forEach(function (ch) {   // thème sans résultat
        ch.hidden = (q || type) && !ch.querySelector(".kw-tuto[data-search]:not([hidden])");
      });
      chips.forEach(function (c) { c.classList.toggle("is-active", !!q && norm(c.dataset.filter) === q); });
      types.forEach(function (c) { c.classList.toggle("is-active", c.dataset.type === type); });
    }

    function showList() {
      var list = article.querySelector(".kw-an-list");
      if (list) list.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    input.addEventListener("input", apply);
    chips.forEach(function (c) {
      c.addEventListener("click", function () {
        input.value = norm(input.value.trim()) === norm(c.dataset.filter) ? "" : c.dataset.filter;
        apply();
        if (input.value) showList();
      });
    });
    types.forEach(function (c) {
      c.addEventListener("click", function () {
        type = type === c.dataset.type ? "" : c.dataset.type;
        apply();
        if (type) showList();
      });
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
