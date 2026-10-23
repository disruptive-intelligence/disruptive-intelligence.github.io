/* Outils de lecture de la veille (pages générées par hooks/portal.py) :
   - Explorer : sujets lus dans assets/veille-sujets.json, filtrés, affichés 50 par page ;
   - Recherche de la Bibliothèque et des cheat sheets (search/bibliotheque.json), regroupée par page ;
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
  function pager(nav, page, pages, go, labels) {
    labels = labels || ["‹ Plus récents", "Plus anciens ›"];
    nav.innerHTML = "";
    if (pages <= 1) return;
    function button(label, target, disabled) {
      var b = document.createElement("button");
      b.type = "button"; b.textContent = label; b.disabled = disabled;
      b.addEventListener("click", function () { go(target); nav.parentNode.scrollIntoView({ behavior: "smooth" }); });
      nav.appendChild(b);
    }
    button(labels[0], page - 1, page === 0);
    var info = document.createElement("span");
    info.textContent = "Page " + (page + 1) + " / " + pages;
    nav.appendChild(info);
    button(labels[1], page + 1, page >= pages - 1);
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

  /* Recherche de la Bibliothèque et des cheat sheets : texte intégral lu dans search/bibliotheque.json (retiré de
     l'index global, qui ne garde que les titres), chargé seulement sur cette page. Les sections sont regroupées par
     page ; la page dont le titre contient les mots, les fiches et les cheat sheets passent devant. Un nombre seul
     (« 7 », « 4624 ») compte comme un mot entier. La recherche et le filtre restent dans l'adresse (?mots=, ?type=). */
  var KINDS = { fiche: "Fiche détection", cs: "Cheat sheet", cours: "Cours", lab: "Lab", notion: "Fiche notion" };
  var BONUS = { fiche: 6, cs: 5, notion: 3, lab: 2, cours: 0 };
  var GROUPS = { "": null, pratique: ["fiche", "cs"], cours: ["cours", "notion"], lab: ["lab"] };
  var PER_PAGE = 20;
  function librarySearch() {
    var root = document.getElementById("kw-libsearch");
    if (!root) return;
    var q = root.querySelector(".kw-explorer__q"), count = root.querySelector(".kw-explorer__count"),
        list = root.querySelector(".kw-libsearch__hits"), nav = root.querySelector(".kw-pager"),
        kinds = Array.prototype.slice.call(root.querySelectorAll(".kw-libsearch__kinds button")),
        site = base(), rows = [], page = 0, kind = "", timer;
    function matcher(w) {
      if (/^\d+$/.test(w)) { var re = new RegExp("(^|[^0-9])" + w + "([^0-9]|$)"); return function (s) { return re.test(s); }; }
      return function (s) { return s.indexOf(w) >= 0; };
    }
    function snippet(r, words) {
      var at = -1;
      words.forEach(function (w) { var k = r._body.indexOf(w); if (at < 0 && k >= 0) at = k; });
      var start = Math.max(0, at - 90), text = r.x.slice(start, start + 240);
      text = esc((start ? "…" : "") + text + (start + 240 < r.x.length ? "…" : ""));
      words.forEach(function (w) {
        if (!/^[a-z0-9]+$/.test(w)) return;
        var re = new RegExp(/^\d+$/.test(w) ? "(?<![0-9])(" + w + ")(?![0-9])" : "(" + w + ")", "gi");
        text = text.replace(re, "<mark>$1</mark>");
      });
      return text;
    }
    function remember() {
      try {
        var u = new URL(location.href);
        if (q.value.trim()) u.searchParams.set("mots", q.value.trim()); else u.searchParams.delete("mots");
        if (kind) u.searchParams.set("type", kind); else u.searchParams.delete("type");
        history.replaceState(history.state, "", u.toString());
      } catch (e) { /* adresse inchangée */ }
    }
    function apply(keepPage) {
      remember();
      kinds.forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.kind === kind ? "true" : "false"); });
      var words = fold(q.value).split(/\s+/).filter(function (w) { return w.length > 1 || /^\d$/.test(w); });
      if (!words.length) {
        list.innerHTML = ""; nav.innerHTML = "";
        count.textContent = rows.length + " sections indexées";
        return;
      }
      var tests = words.map(matcher), allowed = GROUPS[kind], byPage = {}, order = [];
      rows.forEach(function (r) {
        if (allowed && allowed.indexOf(r.k) < 0) return;
        var score = 0;
        for (var i = 0; i < tests.length; i++) {
          var inTitle = tests[i](r._title), inBody = tests[i](r._body);
          if (!inTitle && !inBody) return;
          score += (inTitle ? 10 : 0) + (inBody ? 1 : 0);
        }
        var p = byPage[r.p];
        if (!p) {
          p = byPage[r.p] = { page: r.p, title: r.pt || r.t, note: r.n, k: r.k, hits: [], score: 0 };
          var pt = fold(p.title);
          p.titled = tests.every(function (t) { return t(pt); });
          order.push(p);
        }
        p.hits.push([score, r]);
      });
      order.forEach(function (p) {
        p.hits.sort(function (a, b) { return b[0] - a[0]; });
        p.score = p.hits[0][0] + (p.titled ? 20 : 0) + (BONUS[p.k] || 0) + Math.min(p.hits.length, 5);
      });
      order.sort(function (a, b) { return b.score - a.score; });
      var pages = Math.max(1, Math.ceil(order.length / PER_PAGE));
      if (!keepPage) page = 0;
      page = Math.min(page, pages - 1);
      list.innerHTML = order.slice(page * PER_PAGE, (page + 1) * PER_PAGE).map(function (p) {
        var sections = p.hits.filter(function (h) { return h[1].l.indexOf("#") >= 0; });
        var first = p.hits[0][1];
        var line = function (h) {
          return '<li><a href="' + esc(new URL(h[1].l, site).href) + '">' + esc(h[1].t) + "</a></li>";
        };
        var shown = sections.slice(0, 3).map(line).join(""), more = sections.slice(3);
        return '<li class="kw-hit kw-hit--' + p.k + '"><span class="kw-hit__kind">' + esc(KINDS[p.k] || "") + "</span>" +
          '<a class="kw-hit__title" href="' + esc(new URL(p.page, site).href) + '">' + esc(p.title) + "</a>" +
          (p.note !== p.title ? '<span class="kw-libsearch__note">' + esc(p.note) + "</span>" : "") +
          (first.x ? '<span class="kw-ex__fact">' + snippet(first, words) + "</span>" : "") +
          (shown ? '<ul class="kw-hit__sections">' + shown + "</ul>" : "") +
          (more.length ? '<details class="kw-hit__more"><summary>' + more.length + " autre" + (more.length > 1 ? "s" : "") +
            " passage" + (more.length > 1 ? "s" : "") + '</summary><ul class="kw-hit__sections">' + more.map(line).join("") +
            "</ul></details>" : "") + "</li>";
      }).join("") || '<li class="kw-muted">Rien ne correspond. Essayer un seul mot, ou un autre filtre.</li>';
      count.textContent = order.length + " page" + (order.length > 1 ? "s" : "");
      pager(nav, page, pages, function (n) { page = n; apply(true); }, ["‹ Précédentes", "Suivantes ›"]);
    }
    count.textContent = "Chargement…";
    fetch(new URL(root.dataset.src, site)).then(function (r) { return r.json(); }).then(function (data) {
      rows = data.map(function (d) {
        return { l: d[0], t: d[1], n: d[2], x: d[3], k: d[4] || "cours", pt: d[5] || "", p: d[0].split("#")[0],
                 _title: fold(d[1] + " " + (d[5] || "")), _body: fold(d[3]) };
      });
      var params = new URLSearchParams(location.search);   // « q » ouvrirait la recherche de Material
      if (params.get("mots")) q.value = params.get("mots");
      if (params.get("type") in GROUPS) kind = params.get("type");
      q.addEventListener("input", function () { clearTimeout(timer); timer = setTimeout(function () { apply(false); }, 150); });
      kinds.forEach(function (b) { b.addEventListener("click", function () { kind = b.dataset.kind; apply(false); }); });
      apply(false);
    }).catch(function () { count.textContent = "Chargement impossible."; });
  }

  function init() { explorer(); librarySearch(); readings(); calendars(); progress(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
