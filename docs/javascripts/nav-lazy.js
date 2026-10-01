// Menu latéral : la flèche « » » d'une entrée repliée la déroule sur place, sans changer de page.
// Le thème n'écrit dans chaque page que la partie du menu qui mène à la page lue (navigation.prune : la
// Bibliothèque compte plus de 2 000 pages) ; une entrée repliée n'y est qu'un lien vers sa page. Au clic
// sur la flèche, ce script charge cette page en arrière-plan, y prend le sous-menu de l'entrée et l'insère.
// Un clic sur le nom ouvre toujours la page. Sur mobile (menu en panneaux), comportement du thème inchangé.
(function () {
  var cache = {};
  var desktop = window.matchMedia("(min-width: 76.25em)");

  function sameUrl(a, b) {
    return a.replace(/index\.html$/, "") === b.replace(/index\.html$/, "");
  }

  function subtree(html, pageUrl) {
    var doc = new DOMParser().parseFromString(html, "text/html");
    var target = new URL(pageUrl, location.href).pathname;
    var items = doc.querySelectorAll(".md-nav--primary li.md-nav__item--nested");
    for (var i = 0; i < items.length; i++) {
      var own = items[i].querySelector(":scope > .md-nav__container > a.md-nav__link, :scope > a.md-nav__link");
      var nav = items[i].querySelector(":scope > nav.md-nav");
      if (!own || !nav || !sameUrl(new URL(own.getAttribute("href"), pageUrl).pathname, target)) continue;
      nav = nav.cloneNode(true);
      nav.querySelectorAll("label.md-nav__title").forEach(function (l) { l.remove(); });
      nav.querySelectorAll("[href]").forEach(function (a) {          // liens relatifs à la page chargée
        var u = new URL(a.getAttribute("href"), pageUrl);
        a.setAttribute("href", u.pathname + u.hash);
      });
      nav.querySelectorAll(".md-nav__link--active").forEach(function (a) { a.classList.remove("md-nav__link--active"); });
      nav.removeAttribute("aria-labelledby");
      return nav;
    }
    return null;
  }

  function toggle(li, link) {
    var open = !li.classList.contains("kw-open");
    var nav = li.querySelector(":scope > nav.md-nav");
    if (nav || !open) {
      li.classList.toggle("kw-open", open);
      link.setAttribute("aria-expanded", open ? "true" : "false");
      return;
    }
    var url = new URL(link.getAttribute("href"), location.href).href;
    li.classList.add("kw-loading");
    (cache[url] || (cache[url] = fetch(url).then(function (r) { return r.text(); })))
      .then(function (html) {
        var tree = subtree(html, url);
        li.classList.remove("kw-loading");
        if (!tree) { location.href = url; return; }                  // sous-menu introuvable : ouvrir la page
        li.appendChild(tree);
        li.classList.add("kw-lazy", "kw-open");
        link.setAttribute("aria-expanded", "true");
      })
      .catch(function () { location.href = url; });
  }

  document.addEventListener("click", function (e) {
    if (!desktop.matches || e.button !== 0 || e.ctrlKey || e.metaKey || e.shiftKey) return;
    var icon = e.target.closest(".md-nav--primary .md-nav__item--pruned > a.md-nav__link .md-nav__icon");
    if (!icon) return;
    e.preventDefault();
    e.stopPropagation();
    var link = icon.closest("a.md-nav__link");
    toggle(link.parentElement, link);
  }, true);
})();
