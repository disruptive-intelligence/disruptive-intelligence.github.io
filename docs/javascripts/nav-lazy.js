// Menu latéral : la flèche « » » d'une entrée repliée la déroule sur place, sans changer de page.
// Le thème n'écrit dans chaque page que la partie du menu qui mène à la page lue (navigation.prune : la
// Bibliothèque compte plus de 2 000 pages) ; une entrée repliée n'y est qu'un lien vers sa page. Au clic
// sur la flèche, ce script charge cette page en arrière-plan, y prend le sous-menu de l'entrée et l'insère.
// Un clic sur le nom ouvre toujours la page. Même chose sur mobile, où le menu est un accordéon (extra.css) :
// à l'ouverture du tiroir, la page lue est centrée dans le menu.
(function () {
  var cache = {};

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
    if (e.button !== 0 || e.ctrlKey || e.metaKey || e.shiftKey) return;
    var icon = e.target.closest(".md-nav--primary .md-nav__item--pruned > a.md-nav__link .md-nav__icon");
    if (!icon) return;
    e.preventDefault();
    e.stopPropagation();
    var link = icon.closest("a.md-nav__link");
    toggle(link.parentElement, link);
  }, true);

  var drawer = document.getElementById("__drawer");
  if (drawer) drawer.addEventListener("change", function () {
    var list = document.querySelector(".md-nav--primary > .md-nav__list");
    var here = Array.prototype.filter.call(document.querySelectorAll(".md-nav--primary .md-nav__link--active"),
      function (el) { return el.offsetParent && !el.closest(".md-nav--secondary"); }).pop();
    if (!drawer.checked || !list || !here) return;
    var a = here.getBoundingClientRect(), b = list.getBoundingClientRect();
    list.scrollTop += a.top - b.top - (b.height - a.height) / 2;
  });

  // Plan de la page (≡) dans le menu mobile : chaque section se replie, » déplie ses sous-sections.
  document.querySelectorAll(".md-nav--primary .md-nav--secondary li.md-nav__item").forEach(function (li) {
    var link = li.querySelector(":scope > a.md-nav__link");
    if (!link || !li.querySelector(":scope > nav.md-nav")) return;
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "kw-toc-fold";
    btn.setAttribute("aria-label", "Sous-sections");
    btn.setAttribute("aria-expanded", "false");
    li.classList.add("kw-toc-branch");
    link.after(btn);
    btn.addEventListener("click", function () {
      var open = li.classList.toggle("kw-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });
  if (drawer) drawer.addEventListener("change", function () {          // section lue : sa branche dépliée
    if (!drawer.checked) return;
    document.querySelectorAll(".md-nav--primary .md-nav--secondary .md-nav__link--active").forEach(function (a) {
      for (var li = a.closest("li.kw-toc-branch"); li; li = li.parentElement.closest("li.kw-toc-branch")) {
        li.classList.add("kw-open");
        li.querySelector(":scope > .kw-toc-fold").setAttribute("aria-expanded", "true");
      }
    });
  });
})();
