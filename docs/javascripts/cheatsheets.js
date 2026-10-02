// Cheat sheets : un filtre en haut de chaque fiche (masque les besoins qui ne correspondent pas) et sur la
// page « Que veux-tu faire ? ». Chaque besoin (titre ###) et ce qui le suit forment une entrée.
(function () {
  function norm(s) {
    return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
  }

  function cmdName(card) {
    return norm((card.querySelector("code") || card).textContent);
  }

  function liCmds(li, withExamples) {                // commandes d'un besoin : forme neutre (+ exemples)
    var out = [];
    li.querySelectorAll(withExamples ? ".kw-cs-cmds code, .kw-cs-hidden" : ".kw-cs-cmds code").forEach(function (c) {
      out = out.concat(norm(c.textContent).split(/\s+/));
    });
    return out;
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
    if (search) {                                       // pages « Que veux-tu faire ? » et « Par commande »
      var groups = article.querySelectorAll(search.dataset.scope);
      search.addEventListener("input", function () {
        var q = norm(search.value.trim());
        var byName = q && Array.prototype.some.call(groups, function (g) {     // « ss » : la commande ss,
          return !g.querySelector("h2") && cmdName(g).indexOf(q) === 0;         // pas tout ce qui contient « ss »
        });
        var items = article.querySelectorAll(search.dataset.scope + " li");
        var uses = function (withExamples) {               // « tail » : les besoins dont la forme neutre
          return Array.prototype.some.call(items, function (li) {   // l'utilise ; à défaut, ses exemples (awk)
            return liCmds(li, withExamples).indexOf(q) >= 0;
          });
        };
        var byCmd = q && (uses(false) ? "neutre" : uses(true) ? "exemples" : "");
        groups.forEach(function (g) {
          var title = g.querySelector("h2");
          if (!title) {                                 // une commande : par son nom, sinon par tout son texte
            g.hidden = q && (byName ? cmdName(g).indexOf(q) !== 0 : norm(g.textContent).indexOf(q) < 0);
            return;
          }
          var shown = 0;
          g.querySelectorAll("li").forEach(function (li) {
            li.hidden = q && (byCmd ? liCmds(li, byCmd === "exemples").indexOf(q) < 0
                                    : norm(li.textContent + " " + title.textContent).indexOf(q) < 0);
            if (!li.hidden) shown++;
          });
          g.hidden = shown === 0;
        });
        article.querySelectorAll(":scope > h2").forEach(function (h2) {     // lettre sans commande visible
          var node = h2.nextElementSibling, any = false;
          while (node && node.tagName !== "H2") { if (node.matches(search.dataset.scope) && !node.hidden) any = true; node = node.nextElementSibling; }
          h2.hidden = !any;
        });
        var letters = article.querySelector(".kw-cs-letters");
        if (letters) letters.hidden = !!q;
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
