// Bouton pour masquer / afficher la sidebar de gauche (style HackTricks).
// Le choix est mémorisé dans le navigateur (localStorage) d'une page à l'autre.
(function () {
  var KEY = "kw-sidebar-hidden";

  function read() {
    try { return localStorage.getItem(KEY) === "1"; } catch (e) { return false; }
  }
  function save(hidden) {
    try { localStorage.setItem(KEY, hidden ? "1" : "0"); } catch (e) { /* stockage indisponible */ }
  }
  function apply(hidden, btn) {
    document.body.classList.toggle("kw-sidebar-hidden", hidden);
    btn.textContent = hidden ? "»" : "«";
    btn.title = hidden ? "Afficher le menu" : "Masquer le menu";
    btn.setAttribute("aria-label", btn.title);
  }

  function init() {
    if (document.querySelector(".kw-sidebar-toggle")) return;
    var btn = document.createElement("button");
    btn.className = "kw-sidebar-toggle";
    btn.type = "button";
    document.body.appendChild(btn);
    apply(read(), btn);
    btn.addEventListener("click", function () {
      var hidden = !document.body.classList.contains("kw-sidebar-hidden");
      apply(hidden, btn);
      save(hidden);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
