/* Outils de lecture de la veille (pages générées par hooks/portal.py) :
   - Explorer : sujets lus dans assets/veille-sujets.json, filtrés, affichés 50 par page ;
   - Pile de lecture : lectures cochées « lues » (mémorisées dans ce navigateur), pagination par éditions ;
   - calendriers feuilletables (‹ ›) de la page Veille et de l'Agenda ;
   - barre de progression de lecture sur les pages longues. */
(function () {
  var PAGE = 50;
  var LANES = { tech: "Tech", ia: "IA & rupture", cyber: "Cyber", "geo-ie": "Géopolitique" };
  var FRESH = { updated: "Mise à jour", carryover: "Suivi" };
  var MONTHS = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."];

  function fold(text) { return (text || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase(); }
  function esc(text) {
    return String(text).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; });
  }
  function base() {
    if (window.__md_scope) return window.__md_scope;
    var s = document.querySelector('script[src*="veille-tools.js"]');
    return new URL(s ? s.src.replace(/javascripts\/veille-tools\.js.*$/, "") : ".", location);
  }

  /* Pagination commune : « ‹ Précédent · Page n / N · Suivant › » */
  function pager(nav, page, pages, go) {
    nav.innerHTML = "";
    if (pages <= 1) return;
    function button(label, target, disabled) {
      var b = document.createElement("button");
      b.type = "button"; b.textContent = label; b.disabled = disabled;
      b.addEventListener("click", function () { go(target); nav.parentNode.scrollIntoView({ behavior: "smooth" }); });
      nav.appendChild(b);
    }
    button("‹ Plus récents", page - 1, page === 0);
    var info = document.createElement("span");
    info.textContent = "Page " + (page + 1) + " / " + pages;
    nav.appendChild(info);
    button("Plus anciens ›", page + 1, page >= pages - 1);
  }

  function explorer() {
    var root = document.getElementById("kw-explorer");
    if (!root) return;
    var q = root.querySelector(".kw-explorer__q"), period = root.querySelector(".kw-explorer__period"),
        lane = root.querySelector(".kw-explorer__lane"), fresh = root.querySelector(".kw-explorer__fresh"),
        count = root.querySelector(".kw-explorer__count"), body = root.querySelector("tbody"),
        nav = root.querySelector(".kw-pager"), site = base(), rows = [], page = 0;
    function row(r) {
      var d = new Date(r.d + "T12:00:00");
      return '<tr><td class="kw-ex__date">' + d.getDate() + " " + MONTHS[d.getMonth()] + "</td>" +
        "<td>" + (LANES[r.l] ? '<span class="kw-lanetag kw-lane--' + r.l + '">' + LANES[r.l] + "</span>" : "") + "</td>" +
        '<td><a href="' + esc(new URL(r.u, site).href) + '">' + esc(r.t) + "</a>" +
        (FRESH[r.f] ? ' <span class="kw-fresh kw-fresh--' + r.f + '">' + FRESH[r.f] + "</span>" : "") +
        '<span class="kw-ex__fact">' + esc(r.x) + "</span></td>" +
        '<td class="kw-ex__src">' + esc(r.s) + "</td></tr>";
    }
    function apply(keepPage) {
      var words = fold(q.value).split(/\s+/).filter(Boolean);
      var since = period.value ? new Date(Date.now() - period.value * 864e5).toISOString().slice(0, 10) : "";
      var hits = rows.filter(function (r) {
        return (!lane.value || r.l === lane.value) && (!fresh.value || r.f === fresh.value) && (!since || r.d >= since)
          && words.every(function (w) { return r._text.indexOf(w) >= 0; });
      });
      var pages = Math.max(1, Math.ceil(hits.length / PAGE));
      if (!keepPage) page = 0;
      page = Math.min(page, pages - 1);
      body.innerHTML = hits.slice(page * PAGE, (page + 1) * PAGE).map(row).join("") ||
        '<tr><td colspan="4" class="kw-muted">Aucun sujet ne correspond.</td></tr>';
      count.textContent = hits.length + " sujet" + (hits.length > 1 ? "s" : "") + " sur " + rows.length;
      pager(nav, page, pages, function (p) { page = p; apply(true); });
    }
    fetch(new URL(root.dataset.src, site)).then(function (r) { return r.json(); }).then(function (data) {
      rows = data;
      rows.forEach(function (r) { r._text = fold([r.t, r.x, r.s, LANES[r.l]].join(" ")); });
      var initial = new URLSearchParams(location.search).get("q");
      if (initial) q.value = initial;
      [q, period, lane, fresh].forEach(function (el) { el.addEventListener("input", function () { apply(false); }); });
      apply(false);
    }).catch(function () { count.textContent = "Chargement des sujets impossible."; });
  }

  function readings() {
    var root = document.getElementById("kw-readings");
    if (!root) return;
    var KEY = "kw-read", done = {}, perPage = +root.dataset.perPage || 5, page = 0;
    var hide = root.querySelector(".kw-read__hide"), nav = root.querySelector(".kw-pager"),
        count = root.querySelector(".kw-readings__count");
    var groups = Array.prototype.slice.call(root.querySelectorAll(".kw-read__group"));
    try { done = JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (e) { done = {}; }
    function save() { try { localStorage.setItem(KEY, JSON.stringify(done)); } catch (e) { /* stockage indisponible */ } }
    function render(keepPage) {
      var visible = groups.filter(function (g) {
        return !hide.checked || g.querySelector(".kw-read:not(.is-read)");
      });
      var pages = Math.max(1, Math.ceil(visible.length / perPage));
      if (!keepPage) page = 0;
      page = Math.min(page, pages - 1);
      groups.forEach(function (g) { g.hidden = true; });
      visible.slice(page * perPage, (page + 1) * perPage).forEach(function (g) { g.hidden = false; });
      root.classList.toggle("kw-hide-read", hide.checked);
      var all = root.querySelectorAll(".kw-read").length, read = root.querySelectorAll(".kw-read.is-read").length;
      count.textContent = "· " + read + " lue" + (read > 1 ? "s" : "") + " sur " + all;
      pager(nav, page, pages, function (p) { page = p; render(true); });
    }
    root.querySelectorAll(".kw-read").forEach(function (li) {
      var box = li.querySelector(".kw-read__box"), url = li.dataset.url;
      box.checked = !!done[url];
      li.classList.toggle("is-read", box.checked);
      box.addEventListener("change", function () {
        if (box.checked) done[url] = 1; else delete done[url];
        li.classList.toggle("is-read", box.checked);
        save();
        render(true);
      });
    });
    try { hide.checked = localStorage.getItem("kw-read-hide") === "1"; } catch (e) { /* idem */ }
    hide.addEventListener("change", function () {
      try { localStorage.setItem("kw-read-hide", hide.checked ? "1" : "0"); } catch (e) { /* idem */ }
      render(false);
    });
    render(false);
  }

  function calendars() {
    document.querySelectorAll(".kw-cal").forEach(function (cal) {
      var months = Array.prototype.slice.call(cal.querySelectorAll(".kw-cal__month"));
      if (!months.length) return;
      var i = Math.max(0, months.findIndex(function (m) { return m.hasAttribute("data-default"); }));
      var prev = cal.querySelector(".kw-cal__prev"), next = cal.querySelector(".kw-cal__next");
      function show() {
        months.forEach(function (m, k) { m.hidden = k !== i; });
        prev.disabled = i === 0; next.disabled = i === months.length - 1;
      }
      prev.addEventListener("click", function () { if (i > 0) { i--; show(); } });
      next.addEventListener("click", function () { if (i < months.length - 1) { i++; show(); } });
      cal.classList.add("is-paged");
      show();
    });
  }

  function progress() {
    var article = document.querySelector(".md-content article");
    if (!article || article.scrollHeight < window.innerHeight * 2.5) return;
    var bar = document.createElement("div");
    bar.className = "kw-progress";
    document.body.appendChild(bar);
    function update() {
      var top = article.getBoundingClientRect().top + window.scrollY;
      var span = article.scrollHeight - window.innerHeight;
      var ratio = span > 0 ? (window.scrollY - top + 80) / span : 0;
      bar.style.transform = "scaleX(" + Math.max(0, Math.min(1, ratio)) + ")";
    }
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    update();
  }

  function init() { explorer(); readings(); calendars(); progress(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
