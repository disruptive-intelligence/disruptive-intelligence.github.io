// Analyses : filtre des listes (titre, thèse, auteur, sujets) et pastilles de sujets qui le remplissent.
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

    function apply() {
      var q = norm(input.value.trim());
      items.forEach(function (it) { it.hidden = q && norm(it.dataset.search).indexOf(q) < 0; });
      article.querySelectorAll(".kw-an-list .kw-chapter").forEach(function (ch) {   // thème sans résultat
        ch.hidden = q && !ch.querySelector(".kw-tuto[data-search]:not([hidden])");
      });
      chips.forEach(function (c) { c.classList.toggle("is-active", q && norm(c.dataset.filter) === q); });
    }

    input.addEventListener("input", apply);
    chips.forEach(function (c) {
      c.addEventListener("click", function () {
        input.value = norm(input.value.trim()) === norm(c.dataset.filter) ? "" : c.dataset.filter;
        apply();
        var list = article.querySelector(".kw-an-list");
        if (input.value && list) list.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
