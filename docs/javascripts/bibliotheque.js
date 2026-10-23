/* Bibliothèque — navigation.
   - Accueil et pages de rubrique (.kw-bv) : tuiles de domaine (Cyber, IT), liste des rubriques à gauche, détail à droite ;
     dans le détail, un bandeau collant fait défiler jusqu'aux sous-rubriques, toutes affichées, et souligne celle en cours.
   - Page « Filtrer par titre » (.kw-bv-find) : toutes les pages filtrables, pré-remplie par ?titre= (ou ?mots=) et ?rubrique=.
   Données : assets/bibliotheque-arbre.json (hooks/portal.py, library_tree). Sans JS, la liste générée par le hook reste. */
(function () {
  "use strict";

  var FORMATS = { cours: "Cours", synthese: "Synthèse", fiche: "Fiche notion", detection: "Fiche détection", "aide-memoire": "Aide-mémoire",
                  atelier: "Atelier", ressources: "Ressources", revision: "Révision" };

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text !== undefined && text !== null) n.textContent = text;
    return n;
  }
  function link(root, item, cls, text) {
    var a = el("a", cls, text !== undefined ? text : item.t);
    a.href = root + item.u;
    return a;
  }
  function button(cls, pressed) {
    var b = el("button", cls); b.type = "button";
    if (pressed !== undefined) b.setAttribute("aria-pressed", pressed ? "true" : "false");
    return b;
  }
  function press(items, active) { items.forEach(function (t) { t.setAttribute("aria-pressed", t === active ? "true" : "false"); }); }
  function fold(s) { return (s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase(); }
  function isLab(t) { return /^labs?\b/i.test(t || ""); }
  function duration(m) { return m ? (m >= 60 ? (Math.round(m / 6) / 10).toString().replace(".", ",") + " h" : m + " min") : ""; }
  function meta(n) { return [FORMATS[n.f] || n.f, n.p, duration(n.m), n.h ? "rangée dans " + n.h : ""].filter(Boolean).join(" · "); }
  function plural(n, word) { return n + " " + word + (n > 1 ? "s" : ""); }
  function notesOf(cat) { var out = []; cat.g.forEach(function (g) { out = out.concat(g.n); }); return out; }
  function pagesCount(items) { var k = 0; (items || []).forEach(function (i) { k += 1 + pagesCount(i.c); }); return k; }
  function catPages(cat) { var k = 0; notesOf(cat).forEach(function (n) { k += 1 + pagesCount(n.c); }); return k; }

  // ---------------------------------------------------------------- sommaire d'un cours
  /* Parties en gras, chapitres dessous ; replié derrière un bouton « Sommaire · N pages ». */
  function toc(root, note) {
    if (!note.c || !note.c.length) return null;
    var ol = el("ol", "kw-bv-toc");
    note.c.forEach(function (p) {
      var li = el("li");
      li.appendChild(link(root, p, (p.c && p.c.length ? "kw-bv-part" : "") + (isLab(p.t) ? " kw-bv-lab" : "")));
      if (p.c && p.c.length) {
        var ul = el("ul");
        p.c.forEach(function (ch) { var s = el("li"); s.appendChild(link(root, ch, isLab(ch.t) ? "kw-bv-lab" : "")); ul.appendChild(s); });
        li.appendChild(ul);
      }
      ol.appendChild(li);
    });
    return ol;
  }
  function tocToggle(root, note) {
    var list = toc(root, note);
    if (!list) return null;
    var wrap = el("div", "kw-bv-toggle");
    var btn = el("button", "kw-bv-tocbtn", "Sommaire · " + plural(pagesCount(note.c), "page"));
    btn.type = "button"; btn.setAttribute("aria-expanded", "false");
    list.hidden = true;
    btn.addEventListener("click", function () {
      var open = list.hidden; list.hidden = !open; btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    wrap.appendChild(btn); wrap.appendChild(list);
    return wrap;
  }

  // ---------------------------------------------------------------- rubriques et détail
  /* Unités de la liste : les rubriques (non vides) d'un domaine, ou les sous-rubriques sur une page de rubrique. */
  function unitsOf(dom) {
    if (dom.c.length > 1) return dom.c.filter(function (c) { return notesOf(c).length; })
                                  .map(function (c) { return { head: c, groups: c.g, pages: catPages(c) }; });
    var c = dom.c[0];
    return c.g.map(function (g) {
      return { head: { t: g.t || c.t, e: g.e || c.e, d: g.d, u: c.u }, groups: [{ t: "", d: "", n: g.n }],
               pages: catPages({ g: [{ n: g.n }] }) };
    });
  }
  function notesCount(u) { var k = 0; u.groups.forEach(function (g) { k += g.n.length; }); return k; }

  /* Détail d'une rubrique : en-tête, bandeau de sous-rubriques, cartes de cours avec résumé et sommaire. */
  var spy = null;
  function detail(root, u) {
    var box = el("div", "kw-bv-detail");
    var head = el("header", "kw-bv-head");
    var h = el("h2", "kw-bv-title"); h.appendChild(link(root, u.head, "", (u.head.e ? u.head.e + " " : "") + u.head.t));
    head.appendChild(h);
    head.appendChild(el("span", "kw-bv-meta kw-bv-headmeta", plural(notesCount(u), "note") + " · " + plural(u.pages, "page")));
    if (u.head.d) head.appendChild(el("p", "kw-bv-desc", u.head.d));
    box.appendChild(head);
    var heads = [], named = [];
    u.groups.forEach(function (g) {
      if (g.t) {
        var gh = el("h3", "kw-bv-group", (g.e ? g.e + " " : "") + g.t);
        box.appendChild(gh); heads.push(gh); named.push(g);
        if (g.d) box.appendChild(el("p", "kw-bv-groupdesc", g.d));
      }
      var grid = el("div", "kw-bv-cards");
      g.n.forEach(function (n) {
        var card = el("article", "kw-bv-card");
        card.appendChild(link(root, n, "kw-bv-cardtitle"));
        var m = meta(n); if (m) card.appendChild(el("span", "kw-bv-meta", m));
        if (n.r) card.appendChild(el("p", "kw-bv-cardtext", n.r));
        var t = tocToggle(root, n); if (t) card.appendChild(t);
        grid.appendChild(card);
      });
      box.appendChild(grid);
    });
    if (spy) { spy.disconnect(); spy = null; }
    if (heads.length > 1) head.insertAdjacentElement("afterend", strip(heads, named));
    return box;
  }
  /* Bandeau collant : un bouton par sous-rubrique, qui fait défiler jusqu'à elle ; celle en cours est soulignée. */
  function strip(heads, named) {
    var nav = el("nav", "kw-bv-strip"); nav.setAttribute("aria-label", "Sous-rubriques");
    var chips = [];
    heads.forEach(function (h, k) {
      h.id = "kw-bv-sr-" + k;
      var g = named[k];
      var b = button("kw-bv-chip", k === 0);
      b.textContent = (g.e ? g.e + " " : "") + g.t + " · " + g.n.length;
      b.addEventListener("click", function () { press(chips, b); h.scrollIntoView({ behavior: "smooth", block: "start" }); });
      chips.push(b); nav.appendChild(b);
    });
    if ("IntersectionObserver" in window) {
      spy = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          var k = heads.indexOf(e.target);
          if (e.isIntersecting && k >= 0) { press(chips, chips[k]); chips[k].scrollIntoView({ block: "nearest", inline: "nearest" }); }
        });
      }, { rootMargin: "-25% 0px -65% 0px" });
      heads.forEach(function (h) { spy.observe(h); });
    }
    return nav;
  }

  /* Choix gardé dans l'adresse (?voir=…, ?domaine=…) : un retour ou un lien partagé rouvre la même vue. */
  function param(name) { try { return new URLSearchParams(window.location.search).get(name) || ""; } catch (e) { return ""; } }
  function remember(name, value) {
    try {
      var u = new URL(window.location.href);
      if (value) u.searchParams.set(name, value); else u.searchParams.delete(name);
      window.history.replaceState(window.history.state, "", u.toString());
    } catch (e) { /* adresse inchangée */ }
  }
  function key(t) { return fold(t).replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, ""); }

  /* Liste des rubriques à gauche (sélecteur sur téléphone), détail à droite. */
  function rubrics(root, units) {
    var box = el("div", "kw-bv-layout");
    var main = el("div", "kw-bv-main");
    var nav = el("nav", "kw-bv-rubs"); nav.setAttribute("aria-label", "Rubriques");
    var pick = el("select", "kw-bv-pick"); pick.setAttribute("aria-label", "Choisir une rubrique");
    var items = [];
    function show(i, keep) {
      main.textContent = ""; main.appendChild(detail(root, units[i]));
      if (!keep) remember("voir", i ? key(units[i].head.t) : "");
      pick.value = String(i);
      items.forEach(function (x, k) { x.setAttribute("aria-current", k === i ? "true" : "false"); });
    }
    units.forEach(function (u, i) {
      var b = button("kw-bv-rub");
      b.appendChild(el("span", "kw-bv-rubicon", u.head.e || "•"));
      b.appendChild(el("span", "kw-bv-rublabel", u.head.t));
      b.appendChild(el("span", "kw-bv-rubcount", String(notesCount(u))));
      b.addEventListener("click", function () { show(i); });
      items.push(b); nav.appendChild(b);
      var o = el("option", "", u.head.t); o.value = String(i); pick.appendChild(o);
    });
    pick.addEventListener("change", function () { show(parseInt(pick.value, 10)); });
    box.appendChild(pick); box.appendChild(nav); box.appendChild(main);
    if (units.length) {
      var wanted = param("voir"), start = 0;
      units.forEach(function (u, i) { if (wanted && key(u.head.t) === wanted) start = i; });
      show(start, true);
    }
    return box;
  }
  function domainStats(d) {
    var nn = 0, pp = 0, rr = 0;
    d.c.forEach(function (c) { var k = notesOf(c).length; if (k) { rr++; nn += k; pp += catPages(c); } });
    return plural(rr, "rubrique") + " · " + plural(nn, "note") + " · " + plural(pp, "page");
  }

  /* Tuiles de domaine (accueil seulement), puis rubriques et détail du domaine choisi. */
  function library(root, doms) {
    var wrap = el("div", "kw-bv-nav");
    var out = el("div");
    var first = 0;
    doms.forEach(function (d, i) { if (doms.length > 1 && param("domaine") === d.id) first = i; });
    if (doms.length > 1) {
      var row = el("div", "kw-bv-doms"); var tiles = [];
      doms.forEach(function (d, i) {
        var b = button("kw-bv-dom", i === first);
        b.appendChild(el("span", "kw-bv-domicon", d.e || "•"));
        var txt = el("span", "kw-bv-domtext");
        txt.appendChild(el("span", "kw-bv-domtitle", d.t)); txt.appendChild(el("span", "kw-bv-meta", domainStats(d)));
        b.appendChild(txt);
        b.addEventListener("click", function () {
          press(tiles, b); remember("voir", ""); remember("domaine", i ? d.id : "");
          out.textContent = ""; out.appendChild(rubrics(root, unitsOf(d)));
        });
        tiles.push(b); row.appendChild(b);
      });
      wrap.appendChild(row);
    }
    out.appendChild(rubrics(root, unitsOf(doms[first])));
    wrap.appendChild(out);
    return wrap;
  }

  // ---------------------------------------------------------------- page « Filtrer par titre »
  function facets(root, doms, params) {
    var rows = [];
    doms.forEach(function (d) {
      d.c.forEach(function (c) {
        c.g.forEach(function (g) {
          g.n.forEach(function (n) {
            if (n.h) return;   // note rappelée : déjà listée dans sa rubrique
            rows.push({ t: n.t, u: n.u, dom: d.t, cat: c.t, catId: c.id, grp: g.t, where: [d.t, c.t, g.t].filter(Boolean).join(" › "),
                        f: n.f, p: n.p, kind: "note" });
            (function walk(items, trail) {
              (items || []).forEach(function (it) {
                rows.push({ t: it.t, u: it.u, dom: d.t, cat: c.t, catId: c.id, grp: g.t, where: [n.t].concat(trail).join(" › "),
                            f: isLab(it.t) ? "lab" : "chapitre", p: n.p, kind: "page" });
                if (it.c) walk(it.c, trail.concat([it.t]));
              });
            })(n.c, []);
          });
        });
      });
    });
    var wrap = el("div", "kw-bv-filter");
    var bar = el("div", "kw-bv-bar");
    var input = el("input", "kw-bv-input");
    input.type = "search"; input.placeholder = "Mot dans le titre…"; input.setAttribute("aria-label", "Filtrer par mot");
    bar.appendChild(input);
    function select(label, values) {
      var s = el("select", "kw-bv-select"); s.setAttribute("aria-label", label);
      var o = el("option", "", label + " : tous"); o.value = ""; s.appendChild(o);
      values.forEach(function (v) { var x = el("option", "", v[1]); x.value = v[0]; s.appendChild(x); });
      bar.appendChild(s); return s;
    }
    function uniq(key, labelKey) {
      var seen = {}, out = [];
      rows.forEach(function (r) { if (r[key] && !seen[r[key]]) { seen[r[key]] = 1; out.push([r[key], r[labelKey || key]]); } });
      return out;
    }
    var sDom = select("Domaine", uniq("dom"));
    var sCat = select("Rubrique", uniq("catId", "cat"));
    var sKind = select("Type", [["note", "Cours et fiches (entrée)"], ["chapitre", "Chapitres"], ["lab", "Labs"]]);
    var sFmt = select("Format", Object.keys(FORMATS).filter(function (k) {
      return rows.some(function (r) { return r.kind === "note" && r.f === k; });
    }).map(function (k) { return [k, FORMATS[k]]; }));
    var sProv = select("Provenance", uniq("p"));
    var count = el("span", "kw-bv-count"); bar.appendChild(count);
    wrap.appendChild(bar);
    var list = el("ul", "kw-bv-results"); wrap.appendChild(list);
    function apply() {
      var q = fold(input.value.trim()), shown = 0, total = 0;
      list.textContent = "";
      rows.forEach(function (r) {
        if (sDom.value && r.dom !== sDom.value) return;
        if (sCat.value && r.catId !== sCat.value) return;
        if (sKind.value === "note" && r.kind !== "note") return;
        if (sKind.value === "chapitre" && r.f !== "chapitre") return;
        if (sKind.value === "lab" && r.f !== "lab") return;
        if (sFmt.value && !(r.kind === "note" && r.f === sFmt.value)) return;
        if (sProv.value && r.p !== sProv.value) return;
        if (q && fold(r.t + " " + r.where).indexOf(q) === -1) return;
        total++;
        if (shown >= 300) return;
        shown++;
        var li = el("li", "kw-bv-row" + (r.kind === "note" ? " kw-bv-row--note" : ""));
        li.appendChild(link(root, r, r.f === "lab" ? "kw-bv-lab" : ""));
        var info = r.kind === "note" ? [r.where, FORMATS[r.f] || r.f, r.p] : [r.where, r.f === "lab" ? "Lab" : ""];
        li.appendChild(el("span", "kw-bv-meta", info.filter(Boolean).join(" · ")));
        list.appendChild(li);
      });
      count.textContent = plural(total, "page") + (total > shown ? " (300 affichées)" : "");
      try {
        var u = new URL(window.location.href);
        u.searchParams.delete("mots");
        if (input.value.trim()) u.searchParams.set("titre", input.value.trim()); else u.searchParams.delete("titre");
        if (sCat.value) u.searchParams.set("rubrique", sCat.value); else u.searchParams.delete("rubrique");
        window.history.replaceState(null, "", u.toString());
      } catch (e) { /* adresse inchangée */ }
    }
    [input, sDom, sCat, sKind, sFmt, sProv].forEach(function (x) { x.addEventListener(x === input ? "input" : "change", apply); });
    input.value = params.get("titre") || params.get("mots") || "";
    if (params.get("rubrique")) sCat.value = params.get("rubrique");
    apply();
    setTimeout(function () { input.focus(); }, 0);
    return wrap;
  }

  // ---------------------------------------------------------------- montage
  function mount(box, data) {
    var scope = box.dataset.scope || "";
    var doms = data;
    if (scope) {
      doms = [];
      data.forEach(function (d) { d.c.forEach(function (c) { if (c.id === scope) doms.push({ t: d.t, e: d.e, u: d.u, c: [c] }); }); });
    }
    if (!doms.length) return;
    box.appendChild(library(box.dataset.root || "", doms));
    document.body.classList.add("kw-bv-on");
  }
  function load(box, then) {
    if (box.dataset.ready) return;
    box.dataset.ready = "1";
    fetch(box.dataset.json).then(function (r) { return r.json(); }).then(then).catch(function () { box.remove(); });
  }
  /* Page Labs : filtre sur le titre, le cours et les compétences (data-search). */
  function labsFilter(box) {
    var input = box.querySelector("input"), count = box.querySelector("span");
    var items = Array.prototype.slice.call(document.querySelectorAll(".kw-labs li[data-search]"));
    function apply() {
      var q = fold(input.value.trim()), shown = 0;
      items.forEach(function (li) { var ok = !q || fold(li.dataset.search).indexOf(q) >= 0; li.hidden = !ok; if (ok) shown++; });
      document.querySelectorAll(".kw-labs").forEach(function (ul) {
        var h = ul.previousElementSibling, any = ul.querySelector("li:not([hidden])");
        ul.hidden = !any; if (h && /^H2$/.test(h.tagName)) h.hidden = !any;
      });
      count.textContent = plural(shown, "lab");
      remember("filtre", input.value.trim());
    }
    input.value = param("filtre");
    input.addEventListener("input", apply);
    apply();
  }

  function init() {
    document.body.classList.remove("kw-bv-on");
    document.querySelectorAll(".kw-labs-filter").forEach(labsFilter);
    document.querySelectorAll(".kw-bv").forEach(function (box) { load(box, function (data) { mount(box, data); }); });
    document.querySelectorAll(".kw-bv-find").forEach(function (box) {
      load(box, function (data) { box.appendChild(facets(box.dataset.root || "", data, new URLSearchParams(window.location.search))); });
    });
  }

  if (window.document$ && window.document$.subscribe) window.document$.subscribe(init);
  else document.addEventListener("DOMContentLoaded", init);
})();
