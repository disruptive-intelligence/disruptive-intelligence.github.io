// Cheat sheets : un filtre en haut de chaque fiche (masque les besoins qui ne correspondent pas) et sur la
// page « Que veux-tu faire ? ». Chaque besoin (titre ###) et ce qui le suit forment une entrée.
(function () {
  function norm(s) {
    return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
  }

  function wrapEntries(article) {
    var entries = [];
    article.querySelectorAll(":scope > h3").forEach(function (h3) {
      var box = document.createElement("div");
      box.className = "kw-cs-entry";
      h3.parentNode.insertBefore(box, h3);
      var node = h3;
      while (node && !(node !== h3 && /^H[1-3]$/.test(node.tagName)) && !(node.tagName === "DIV" && node.classList.contains("kw-cs-entry"))) {
        var next = node.nextElementSibling;
        box.appendChild(node);
        node = next;
      }
      entries.push(box);
    });
    return entries;
  }

  function filterSheet(article, input, entries) {
    var q = norm(input.value.trim());
    entries.forEach(function (e) { e.hidden = q && norm(e.textContent).indexOf(q) < 0; });
    article.querySelectorAll(":scope > h2").forEach(function (h2) {           // groupe vide : titre masqué
      var node = h2.nextElementSibling, any = false, has = false;
      while (node && node.tagName !== "H2") {
        if (node.classList && node.classList.contains("kw-cs-entry")) { has = true; any = any || !node.hidden; }
        node = node.nextElementSibling;
      }
      if (has) h2.hidden = q && !any;
    });
  }

  function init() {
    var article = document.querySelector("article.md-content__inner");
    if (!article || location.pathname.indexOf("/cheatsheets/") < 0) return;
    var search = article.querySelector("input.kw-cs-search[data-scope]");
    if (search) {                                                         // page « Que veux-tu faire ? »
      var groups = article.querySelectorAll(search.dataset.scope);
      search.addEventListener("input", function () {
        var q = norm(search.value.trim());
        groups.forEach(function (g) {
          var shown = 0;
          g.querySelectorAll("li").forEach(function (li) {
            li.hidden = q && norm(li.textContent + " " + g.querySelector("h2").textContent).indexOf(q) < 0;
            if (!li.hidden) shown++;
          });
          g.hidden = shown === 0;
        });
      });
      search.focus();
      return;
    }
    if (article.querySelectorAll(":scope > h3").length < 4 || article.querySelector("a[download]")) return;   // pas sur un modèle
    var entries = wrapEntries(article);
    var input = document.createElement("input");
    input.type = "search";
    input.className = "kw-cs-search";
    input.placeholder = "Filtrer cette fiche… (pid, port, cron)";
    input.setAttribute("aria-label", "Filtrer les besoins de la fiche");
    var anchor = article.querySelector(":scope > .kw-cs-top") || article.querySelector(":scope > h2");
    article.insertBefore(input, anchor && anchor.classList.contains("kw-cs-top") ? anchor.nextSibling : anchor);
    input.addEventListener("input", function () { filterSheet(article, input, entries); });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
