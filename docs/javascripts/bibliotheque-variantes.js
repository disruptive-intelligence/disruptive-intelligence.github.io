/* Bibliothèque — navigation (aperçu).
   - Page « Filtrer par titre » (.kw-bv-find) : toutes les pages filtrables, pré-remplie par ?titre= et ?rubrique=.
   - Variantes de la page d'accueil et des rubriques (.kw-bv) : Actuelle / D Étagères / E Rubriques et détail / F Mosaïque.
   Données : assets/bibliotheque-arbre.json (hooks/portal.py, library_tree). Sans JS, la page actuelle reste. */
(function () {
  "use strict";

  var KEY = "kw-bv-variante2";
  var LABELS = [["actuelle", "Actuelle"], ["j", "J · Domaine puis E"], ["l", "L · E + bandeau (filtre)"],
                ["m", "M · J + bandeau de navigation"]];
  var FORMATS = { cours: "Cours", synthese: "Synthèse", fiche: "Fiche notion", "aide-memoire": "Aide-mémoire",
                  atelier: "Atelier", ressources: "Ressources", revision: "Révision" };

  function remember(value) {
    try {
      if (value === undefined) return localStorage.getItem(KEY);
      localStorage.setItem(KEY, value);
    } catch (e) { /* stockage indisponible */ }
    return null;
  }
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
  function fold(s) { return (s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase(); }
  function isLab(t) { return /^labs?\b/i.test(t || ""); }
  function duration(m) { return m ? (m >= 60 ? (Math.round(m / 6) / 10).toString().replace(".", ",") + " h" : m + " min") : ""; }
  function meta(n) { return [FORMATS[n.f] || n.f, n.p, duration(n.m)].filter(Boolean).join(" · "); }
  function notesOf(cat) { var out = []; cat.g.forEach(function (g) { out = out.concat(g.n); }); return out; }
  function pagesCount(items) {
    var k = 0; (items || []).forEach(function (i) { k += 1 + pagesCount(i.c); }); return k;
  }
  function catPages(cat) { var k = 0; notesOf(cat).forEach(function (n) { k += 1 + pagesCount(n.c); }); return k; }
  function plural(n, word) { return n + " " + word + (n > 1 ? "s" : ""); }

  /* Sommaire d'un cours : parties en gras, chapitres dessous ; replié au-delà de 8 entrées. */
  function toc(root, note, openLimit) {
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

  /* Bouton « Sommaire » qui déplie le sommaire sous un cours. */
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

  // ---------------------------------------------------------------- D · Étagères
  function shelves(root, doms) {
    var wrap = el("div", "kw-bv-d");
    doms.forEach(function (d) {
      if (doms.length > 1 || d.c.length > 1) {
        var h = el("h2", "kw-bv-domtitle"); h.appendChild(link(root, d, "", (d.e ? d.e + " " : "") + d.t)); wrap.appendChild(h);
      }
      var grid = el("div", "kw-bv-shelves");
      var units = d.c.length > 1 ? d.c.map(function (c) { return { head: c, groups: c.g }; })
                                 : d.c[0].g.map(function (g) { return { head: { t: g.t || d.c[0].t, e: g.e || d.c[0].e, d: g.d, u: d.c[0].u }, groups: [{ t: "", n: g.n }] }; });
      units.forEach(function (u) {
        var card = el("section", "kw-bv-shelf");
        var head = el("header", "kw-bv-shelfhead");
        if (u.head.e) head.appendChild(el("span", "kw-bv-shelficon", u.head.e));
        var ht = el("div");
        ht.appendChild(link(root, u.head, "kw-bv-shelftitle"));
        var nn = 0; u.groups.forEach(function (g) { nn += g.n.length; });
        ht.appendChild(el("span", "kw-bv-meta", plural(nn, "note")));
        head.appendChild(ht); card.appendChild(head);
        if (u.head.d) card.appendChild(el("p", "kw-bv-shelfdesc", u.head.d));
        u.groups.forEach(function (g) {
          if (g.t) card.appendChild(el("h4", "kw-bv-shelfgroup", g.t));
          var ul = el("ul", "kw-bv-shelflist");
          g.n.forEach(function (n) {
            var li = el("li");
            var row = el("div", "kw-bv-shelfrow");
            row.appendChild(link(root, n, "kw-bv-course"));
            row.appendChild(el("span", "kw-bv-meta", [FORMATS[n.f] || n.f, duration(n.m)].filter(Boolean).join(" · ")));
            li.appendChild(row);
            var t = tocToggle(root, n); if (t) li.appendChild(t);
            ul.appendChild(li);
          });
          card.appendChild(ul);
        });
        grid.appendChild(card);
      });
      wrap.appendChild(grid);
    });
    return wrap;
  }

  // ---------------------------------------------------------------- E · Rubriques et détail
  function masterDetail(root, doms) {
    var wrap = el("div", "kw-bv-e");
    var side = el("nav", "kw-bv-eside"); side.setAttribute("aria-label", "Rubriques");
    var pick = el("select", "kw-bv-epick"); pick.setAttribute("aria-label", "Choisir une rubrique");
    var main = el("div", "kw-bv-emain");
    var units = [];
    doms.forEach(function (d) {
      if (d.c.length > 1) {
        side.appendChild(el("p", "kw-bv-eside-dom", (d.e ? d.e + " " : "") + d.t));
        d.c.forEach(function (c) { units.push({ head: c, groups: c.g }); });
      } else {
        d.c[0].g.forEach(function (g) {
          units.push({ head: { t: g.t || d.c[0].t, e: g.e || d.c[0].e, d: g.d, u: d.c[0].u }, groups: [{ t: "", d: "", n: g.n }] });
        });
      }
      units.slice(side.querySelectorAll("button").length).forEach(function (u) {
        var i = units.indexOf(u);
        var b = el("button", "kw-bv-eitem");
        b.type = "button";
        b.appendChild(el("span", "kw-bv-eicon", u.head.e || "•"));
        b.appendChild(el("span", "kw-bv-elabel", u.head.t));
        var nn = 0; u.groups.forEach(function (g) { nn += g.n.length; });
        b.appendChild(el("span", "kw-bv-ecount", String(nn)));
        b.addEventListener("click", function () { show(i); });
        side.appendChild(b);
        var o = el("option", "", u.head.t); o.value = String(i); pick.appendChild(o);
      });
    });
    function show(i) {
      side.querySelectorAll("button").forEach(function (b, k) { b.setAttribute("aria-current", k === i ? "true" : "false"); });
      pick.value = String(i);
      var u = units[i];
      main.textContent = "";
      var head = el("header", "kw-bv-ehead");
      var h = el("h2", "kw-bv-etitle"); h.appendChild(link(root, u.head, "", (u.head.e ? u.head.e + " " : "") + u.head.t));
      head.appendChild(h);
      if (u.head.d) head.appendChild(el("p", "kw-bv-edesc", u.head.d));
      main.appendChild(head);
      u.groups.forEach(function (g) {
        if (g.t) {
          main.appendChild(el("h3", "kw-bv-egroup", (g.e ? g.e + " " : "") + g.t));
          if (g.d) main.appendChild(el("p", "kw-bv-egroupdesc", g.d));
        }
        var grid = el("div", "kw-bv-ecards");
        g.n.forEach(function (n) {
          var card = el("article", "kw-bv-ecard");
          card.appendChild(link(root, n, "kw-bv-ecardtitle"));
          var m = meta(n); if (m) card.appendChild(el("span", "kw-bv-meta", m));
          if (n.r) card.appendChild(el("p", "kw-bv-ecardtext", n.r));
          var t = tocToggle(root, n); if (t) card.appendChild(t);
          grid.appendChild(card);
        });
        main.appendChild(grid);
      });
    }
    pick.addEventListener("change", function () { show(parseInt(pick.value, 10)); });
    wrap.appendChild(pick); wrap.appendChild(side); wrap.appendChild(main);
    if (units.length) show(0);
    return wrap;
  }

  // ---------------------------------------------------------------- F · Mosaïque
  function mosaic(root, doms) {
    var wrap = el("div", "kw-bv-f");
    doms.forEach(function (d) {
      var units = d.c.length > 1 ? d.c.map(function (c) { return { head: c, groups: c.g, pages: catPages(c) }; })
                                 : d.c[0].g.map(function (g) {
                                     var pseudo = { g: [{ t: "", n: g.n }] };
                                     return { head: { t: g.t || d.c[0].t, e: g.e || d.c[0].e, d: g.d, u: d.c[0].u }, groups: [{ t: "", n: g.n }], pages: catPages(pseudo) };
                                   });
      if (doms.length > 1 || d.c.length > 1) {
        var h = el("h2", "kw-bv-domtitle"); h.appendChild(link(root, d, "", (d.e ? d.e + " " : "") + d.t)); wrap.appendChild(h);
      }
      var max = Math.max.apply(null, units.map(function (u) { return u.pages; }).concat([1]));
      var grid = el("div", "kw-bv-tiles");
      var panel = null, openTile = null;
      units.forEach(function (u) {
        var tile = el("button", "kw-bv-tile");
        tile.type = "button";
        if (u.pages >= max * 0.45 && units.length > 2) tile.classList.add("kw-bv-tile--wide");
        tile.appendChild(el("span", "kw-bv-tileicon", u.head.e || "•"));
        tile.appendChild(el("span", "kw-bv-tiletitle", u.head.t));
        var notes = []; u.groups.forEach(function (g) { notes = notes.concat(g.n); });
        tile.appendChild(el("span", "kw-bv-meta", plural(notes.length, "note") + " · " + plural(u.pages, "page")));
        var peek = el("span", "kw-bv-tilepeek", notes.slice(0, 3).map(function (n) { return n.t; }).join(" · "));
        tile.appendChild(peek);
        tile.setAttribute("aria-expanded", "false");
        tile.addEventListener("click", function () {
          if (panel) { panel.remove(); if (openTile) openTile.setAttribute("aria-expanded", "false"); }
          if (openTile === tile) { panel = null; openTile = null; return; }
          openTile = tile; tile.setAttribute("aria-expanded", "true");
          panel = el("div", "kw-bv-tilepanel");
          var ph = el("div", "kw-bv-tilepanelhead");
          ph.appendChild(link(root, u.head, "kw-bv-tilepaneltitle", (u.head.e ? u.head.e + " " : "") + u.head.t + " →"));
          if (u.head.d) ph.appendChild(el("p", "kw-bv-edesc", u.head.d));
          panel.appendChild(ph);
          u.groups.forEach(function (g) {
            if (g.t) panel.appendChild(el("h4", "kw-bv-shelfgroup", g.t));
            var cols = el("div", "kw-bv-ecards");
            g.n.forEach(function (n) {
              var card = el("article", "kw-bv-ecard");
              card.appendChild(link(root, n, "kw-bv-ecardtitle"));
              var m = meta(n); if (m) card.appendChild(el("span", "kw-bv-meta", m));
              var t = toc(root, n);
              if (t) { if (pagesCount(n.c) > 10) { var tg = tocToggle(root, n); card.appendChild(tg); } else card.appendChild(t); }
              cols.appendChild(card);
            });
            panel.appendChild(cols);
          });
          // le panneau s'insère après la dernière tuile de la rangée de la tuile ouverte
          var tiles = Array.prototype.slice.call(grid.querySelectorAll(".kw-bv-tile"));
          var top = tile.offsetTop, after = tile;
          tiles.forEach(function (t) { if (t.offsetTop === top) after = t; });
          after.insertAdjacentElement("afterend", panel);
        });
        grid.appendChild(tile);
      });
      wrap.appendChild(grid);
    });
    return wrap;
  }

  // ---------------------------------------------------------------- briques communes des mix (G, H, I)
  /* Unités affichées : les rubriques d'un domaine, ou les sous-rubriques sur une page de rubrique. */
  function unitsOf(dom) {
    if (dom.c.length > 1) return dom.c.filter(function (c) { return notesOf(c).length; })
                                  .map(function (c) { return { head: c, groups: c.g, pages: catPages(c), dom: dom }; });
    var c = dom.c[0];
    return c.g.map(function (g) {
      return { head: { t: g.t || c.t, e: g.e || c.e, d: g.d, u: c.u }, groups: [{ t: "", d: "", n: g.n }],
               pages: catPages({ g: [{ n: g.n }] }), dom: dom };
    });
  }
  function notesCount(u) { var k = 0; u.groups.forEach(function (g) { k += g.n.length; }); return k; }

  /* Panneau de détail façon E : en-tête, sous-rubriques, cartes de cours avec résumé et sommaire. */
  function detail(root, u) {
    var box = el("div", "kw-bv-detail");
    var head = el("header", "kw-bv-ehead");
    var h = el("h2", "kw-bv-etitle"); h.appendChild(link(root, u.head, "", (u.head.e ? u.head.e + " " : "") + u.head.t));
    head.appendChild(h);
    head.appendChild(el("span", "kw-bv-meta kw-bv-headmeta", plural(notesCount(u), "note") + " · " + plural(u.pages, "page")));
    if (u.head.d) head.appendChild(el("p", "kw-bv-edesc", u.head.d));
    box.appendChild(head);
    u.groups.forEach(function (g) {
      if (g.t) {
        box.appendChild(el("h3", "kw-bv-egroup", (g.e ? g.e + " " : "") + g.t));
        if (g.d) box.appendChild(el("p", "kw-bv-egroupdesc", g.d));
      }
      var grid = el("div", "kw-bv-ecards");
      g.n.forEach(function (n) {
        var card = el("article", "kw-bv-ecard");
        card.appendChild(link(root, n, "kw-bv-ecardtitle"));
        var m = meta(n); if (m) card.appendChild(el("span", "kw-bv-meta", m));
        if (n.r) card.appendChild(el("p", "kw-bv-ecardtext", n.r));
        var t = tocToggle(root, n); if (t) card.appendChild(t);
        grid.appendChild(card);
      });
      box.appendChild(grid);
    });
    return box;
  }

  /* Tuile façon F ; « mini » : version compacte (icône, nom, nombre). */
  function tile(u, onPick, mini, wide) {
    var b = el("button", "kw-bv-tile" + (mini ? " kw-bv-tile--mini" : "") + (wide ? " kw-bv-tile--wide" : ""));
    b.type = "button"; b.setAttribute("aria-pressed", "false");
    b.appendChild(el("span", "kw-bv-tileicon", u.head.e || "•"));
    b.appendChild(el("span", "kw-bv-tiletitle", u.head.t));
    b.appendChild(el("span", "kw-bv-meta", mini ? String(notesCount(u)) : plural(notesCount(u), "note") + " · " + plural(u.pages, "page")));
    if (!mini) {
      var notes = []; u.groups.forEach(function (g) { notes = notes.concat(g.n); });
      b.appendChild(el("span", "kw-bv-tilepeek", notes.slice(0, 3).map(function (n) { return n.t; }).join(" · ")));
    }
    b.addEventListener("click", onPick);
    return b;
  }
  function press(tiles, active) { tiles.forEach(function (t) { t.setAttribute("aria-pressed", t === active ? "true" : "false"); }); }

  // ---------------------------------------------------------------- G · Mosaïque puis détail
  function mosaicThenDetail(root, doms) {
    var wrap = el("div", "kw-bv-g");
    var all = [], tiles = [];
    var out = el("div", "kw-bv-gdetail");
    doms.forEach(function (d) {
      var units = unitsOf(d);
      if (doms.length > 1 || d.c.length > 1) wrap.appendChild(el("h2", "kw-bv-domtitle kw-bv-domtitle--small", (d.e ? d.e + " " : "") + d.t));
      var max = Math.max.apply(null, units.map(function (u) { return u.pages; }).concat([1]));
      var grid = el("div", "kw-bv-tiles kw-bv-tiles--compact");
      units.forEach(function (u) {
        var t = tile(u, function () { press(tiles, t); out.textContent = ""; out.appendChild(detail(root, u));
          out.scrollIntoView({ behavior: "smooth", block: "start" }); }, false, u.pages >= max * 0.45 && units.length > 2);
        tiles.push(t); all.push(u); grid.appendChild(t);
      });
      wrap.appendChild(grid);
    });
    wrap.appendChild(out);
    if (all.length) { press(tiles, tiles[0]); out.appendChild(detail(root, all[0])); }
    return wrap;
  }

  // ---------------------------------------------------------------- H · Détail, mosaïque latérale
  function sideMosaic(root, doms) {
    var wrap = el("div", "kw-bv-h");
    var side = el("nav", "kw-bv-hside"); side.setAttribute("aria-label", "Rubriques");
    var main = el("div", "kw-bv-hmain");
    var tiles = [], first = null;
    doms.forEach(function (d) {
      if (doms.length > 1 || d.c.length > 1) side.appendChild(el("p", "kw-bv-eside-dom", (d.e ? d.e + " " : "") + d.t));
      var grid = el("div", "kw-bv-minis");
      unitsOf(d).forEach(function (u) {
        var t = tile(u, function () { press(tiles, t); main.textContent = ""; main.appendChild(detail(root, u)); }, true);
        tiles.push(t); grid.appendChild(t);
        if (!first) first = { t: t, u: u };
      });
      side.appendChild(grid);
    });
    wrap.appendChild(side); wrap.appendChild(main);
    if (first) { press(tiles, first.t); main.appendChild(detail(root, first.u)); }
    return wrap;
  }

  // ---------------------------------------------------------------- I · Domaine, bandeau, détail
  function domainStrip(root, doms) {
    var wrap = el("div", "kw-bv-i");
    var domRow = el("div", "kw-bv-idoms");
    var strip = el("div", "kw-bv-istrip");
    var out = el("div", "kw-bv-idetail");
    var domTiles = [];
    function openDom(d, dt) {
      press(domTiles, dt);
      strip.textContent = ""; out.textContent = "";
      var tiles = [];
      unitsOf(d).forEach(function (u, k) {
        var t = tile(u, function () { press(tiles, t); out.textContent = ""; out.appendChild(detail(root, u)); }, true);
        tiles.push(t); strip.appendChild(t);
        if (k === 0) { press(tiles, t); out.appendChild(detail(root, u)); }
      });
    }
    if (doms.length > 1 || doms[0].c.length > 1) {
      doms.forEach(function (d) {
        var b = el("button", "kw-bv-idom");
        b.type = "button"; b.setAttribute("aria-pressed", "false");
        b.appendChild(el("span", "kw-bv-tileicon", d.e || "•"));
        var txt = el("span", "kw-bv-idomtext");
        txt.appendChild(el("span", "kw-bv-tiletitle", d.t));
        var nn = 0, pp = 0; d.c.forEach(function (c) { nn += notesOf(c).length; pp += catPages(c); });
        txt.appendChild(el("span", "kw-bv-meta", plural(d.c.length, "rubrique") + " · " + plural(nn, "note") + " · " + plural(pp, "page")));
        b.appendChild(txt);
        b.addEventListener("click", function () { openDom(d, b); });
        domTiles.push(b); domRow.appendChild(b);
      });
      wrap.appendChild(domRow);
    }
    wrap.appendChild(strip); wrap.appendChild(out);
    openDom(doms[0], domTiles[0]);
    return wrap;
  }

  // ---------------------------------------------------------------- mix E + I (J, K, L), palette neutre
  /* Liste verticale de rubriques façon E ; onPick(u) au clic ; renvoie {nav, items}. */
  function rubricList(units, onPick, domLabel) {
    var nav = el("nav", "kw-bv-nlist"); nav.setAttribute("aria-label", "Rubriques");
    if (domLabel) nav.appendChild(el("p", "kw-bv-eside-dom", domLabel));
    var items = [];
    units.forEach(function (u) {
      var b = el("button", "kw-bv-nitem"); b.type = "button";
      b.appendChild(el("span", "kw-bv-eicon", u.head.e || "•"));
      b.appendChild(el("span", "kw-bv-elabel", u.head.t));
      b.appendChild(el("span", "kw-bv-ecount", String(notesCount(u))));
      b.addEventListener("click", function () { items.forEach(function (x) { x.setAttribute("aria-current", x === b ? "true" : "false"); }); onPick(u); });
      items.push(b); nav.appendChild(b);
    });
    return { nav: nav, items: items };
  }
  /* Sélecteur mobile équivalent à la liste. */
  function rubricPick(units, onPick) {
    var s = el("select", "kw-bv-epick"); s.setAttribute("aria-label", "Choisir une rubrique");
    units.forEach(function (u, i) { var o = el("option", "", u.head.t); o.value = String(i); s.appendChild(o); });
    s.addEventListener("change", function () { onPick(units[parseInt(s.value, 10)], parseInt(s.value, 10)); });
    return s;
  }
  /* Disposition E (liste à gauche, détail à droite) pour une liste d'unités. */
  function eLayout(root, units, domLabel, detailFn) {
    var box = el("div", "kw-bv-e kw-bv-nlayout");
    var main = el("div", "kw-bv-emain");
    var list, pick;
    function show(u, i) {
      main.textContent = ""; main.appendChild((detailFn || detail)(root, u));
      if (i === undefined) i = units.indexOf(u);
      pick.value = String(i);
      list.items.forEach(function (x, k) { x.setAttribute("aria-current", k === i ? "true" : "false"); });
    }
    list = rubricList(units, function (u) { show(u); }, domLabel);
    pick = rubricPick(units, show);
    box.appendChild(pick); box.appendChild(list.nav); box.appendChild(main);
    if (units.length) show(units[0], 0);
    return box;
  }
  function domainHead(d) {
    var nn = 0, pp = 0, rr = 0;
    d.c.forEach(function (c) { var k = notesOf(c).length; if (k) { rr++; nn += k; pp += catPages(c); } });
    return plural(rr, "rubrique") + " · " + plural(nn, "note") + " · " + plural(pp, "page");
  }

  // M · détail avec bandeau de navigation : toutes les sous-rubriques restent affichées,
  // le bandeau (collant) fait défiler jusqu'à l'une d'elles et souligne celle en cours de lecture.
  var spy = null;
  function detailWithNav(root, u) {
    var named = u.groups.filter(function (g) { return g.t; });
    var box = detail(root, u);
    if (named.length < 2) return box;
    var heads = Array.prototype.slice.call(box.querySelectorAll(".kw-bv-egroup"));
    var strip = el("nav", "kw-bv-lstrip kw-bv-mstrip"); strip.setAttribute("aria-label", "Sous-rubriques");
    var chips = [];
    heads.forEach(function (h, k) {
      h.id = "kw-bv-sr-" + k;
      var g = named[k];
      var b = el("button", "kw-bv-lchip"); b.type = "button";
      b.textContent = (g.e ? g.e + " " : "") + g.t + " · " + g.n.length;
      b.addEventListener("click", function () {
        press(chips, b);
        h.scrollIntoView({ behavior: "smooth", block: "start" });
      });
      chips.push(b); strip.appendChild(b);
    });
    press(chips, chips[0]);
    box.querySelector(".kw-bv-ehead").insertAdjacentElement("afterend", strip);
    if (spy) spy.disconnect();
    if ("IntersectionObserver" in window) {
      spy = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            var k = heads.indexOf(e.target);
            if (k >= 0) { press(chips, chips[k]); chips[k].scrollIntoView({ block: "nearest", inline: "nearest" }); }
          }
        });
      }, { rootMargin: "-25% 0px -65% 0px" });
      heads.forEach(function (h) { spy.observe(h); });
    }
    return box;
  }

  // J · grandes tuiles de domaine (I), puis E ; M : la même chose avec le bandeau de navigation
  function domainThenE(root, doms, detailFn) {
    var wrap = el("div", "kw-bv-neutral kw-bv-j");
    var out = el("div");
    if (doms.length > 1) {
      var row = el("div", "kw-bv-idoms"); var tiles = [];
      doms.forEach(function (d) {
        var b = el("button", "kw-bv-idom"); b.type = "button"; b.setAttribute("aria-pressed", "false");
        b.appendChild(el("span", "kw-bv-tileicon", d.e || "•"));
        var txt = el("span", "kw-bv-idomtext");
        txt.appendChild(el("span", "kw-bv-tiletitle", d.t)); txt.appendChild(el("span", "kw-bv-meta", domainHead(d)));
        b.appendChild(txt);
        b.addEventListener("click", function () { press(tiles, b); out.textContent = ""; out.appendChild(eLayout(root, unitsOf(d), "", detailFn)); });
        tiles.push(b); row.appendChild(b);
      });
      wrap.appendChild(row);
      press(tiles, tiles[0]);
    }
    out.appendChild(eLayout(root, unitsOf(doms[0]), "", detailFn));
    wrap.appendChild(out);
    return wrap;
  }

  // K · onglets de domaine soulignés, puis E
  function domainTabsThenE(root, doms) {
    var wrap = el("div", "kw-bv-neutral kw-bv-k");
    var out = el("div");
    if (doms.length > 1) {
      var bar = el("div", "kw-bv-ktabs"); var tabs = [];
      doms.forEach(function (d) {
        var b = el("button", "kw-bv-ktab"); b.type = "button"; b.setAttribute("aria-pressed", "false");
        b.appendChild(el("span", "", (d.e ? d.e + " " : "") + d.t));
        b.appendChild(el("span", "kw-bv-meta", domainHead(d)));
        b.addEventListener("click", function () { press(tabs, b); out.textContent = ""; out.appendChild(eLayout(root, unitsOf(d))); });
        tabs.push(b); bar.appendChild(b);
      });
      wrap.appendChild(bar);
      press(tabs, tabs[0]);
    }
    out.appendChild(eLayout(root, unitsOf(doms[0])));
    wrap.appendChild(out);
    return wrap;
  }

  // L · E avec, dans le détail, un bandeau de sous-rubriques qui filtre les cours
  function detailWithStrip(root, u) {
    var named = u.groups.filter(function (g) { return g.t; });
    if (named.length < 2) return detail(root, u);
    var box = el("div", "kw-bv-detail");
    var head = el("header", "kw-bv-ehead");
    var h = el("h2", "kw-bv-etitle"); h.appendChild(link(root, u.head, "", (u.head.e ? u.head.e + " " : "") + u.head.t));
    head.appendChild(h);
    head.appendChild(el("span", "kw-bv-meta kw-bv-headmeta", plural(notesCount(u), "note") + " · " + plural(u.pages, "page")));
    if (u.head.d) head.appendChild(el("p", "kw-bv-edesc", u.head.d));
    box.appendChild(head);
    var strip = el("div", "kw-bv-lstrip"); var chips = [];
    var body = el("div");
    function render(sel) {
      body.textContent = "";
      u.groups.forEach(function (g) {
        if (sel && g !== sel) return;
        if (g.t) {
          body.appendChild(el("h3", "kw-bv-egroup", (g.e ? g.e + " " : "") + g.t));
          if (g.d) body.appendChild(el("p", "kw-bv-egroupdesc", g.d));
        }
        var grid = el("div", "kw-bv-ecards");
        g.n.forEach(function (n) {
          var card = el("article", "kw-bv-ecard");
          card.appendChild(link(root, n, "kw-bv-ecardtitle"));
          var m = meta(n); if (m) card.appendChild(el("span", "kw-bv-meta", m));
          if (n.r) card.appendChild(el("p", "kw-bv-ecardtext", n.r));
          var t = tocToggle(root, n); if (t) card.appendChild(t);
          grid.appendChild(card);
        });
        body.appendChild(grid);
      });
    }
    [null].concat(u.groups.filter(function (g) { return g.t; })).forEach(function (g) {
      var b = el("button", "kw-bv-lchip"); b.type = "button";
      b.textContent = g ? (g.e ? g.e + " " : "") + g.t + " · " + g.n.length : "Tout · " + notesCount(u);
      b.addEventListener("click", function () { press(chips, b); render(g); });
      chips.push(b); strip.appendChild(b);
    });
    press(chips, chips[0]);
    box.appendChild(strip); box.appendChild(body);
    render(null);
    return box;
  }
  function eWithStrip(root, doms) {
    var wrap = el("div", "kw-bv-neutral kw-bv-l");
    var units = [];
    doms.forEach(function (d) { units = units.concat(unitsOf(d)); });
    wrap.appendChild(eLayout(root, units, "", detailWithStrip));
    return wrap;
  }

  // ---------------------------------------------------------------- page « Filtrer par titre »
  function facets(root, doms, params) {
    var rows = [];
    doms.forEach(function (d) {
      d.c.forEach(function (c) {
        c.g.forEach(function (g) {
          g.n.forEach(function (n) {
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
    var wrap = el("div", "kw-bv-c");
    var bar = el("div", "kw-bv-bar kw-bv-facets");
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
        if (input.value.trim()) u.searchParams.set("titre", input.value.trim()); else u.searchParams.delete("titre");
        if (sCat.value) u.searchParams.set("rubrique", sCat.value); else u.searchParams.delete("rubrique");
        window.history.replaceState(null, "", u.toString());
      } catch (e) { /* adresse inchangée */ }
    }
    [input, sDom, sCat, sKind, sFmt, sProv].forEach(function (x) { x.addEventListener(x === input ? "input" : "change", apply); });
    input.value = params.get("titre") || "";
    if (params.get("rubrique")) sCat.value = params.get("rubrique");
    apply();
    setTimeout(function () { input.focus(); }, 0);
    return wrap;
  }

  // ---------------------------------------------------------------- montage
  function variants(box, data) {
    var root = box.dataset.root || "";
    var scope = box.dataset.scope || "";
    var doms = data;
    if (scope) {
      doms = [];
      data.forEach(function (d) { d.c.forEach(function (c) { if (c.id === scope) doms.push({ t: d.t, e: d.e, u: d.u, c: [c] }); }); });
    }
    var tabs = el("div", "kw-bv-tabs"); tabs.setAttribute("role", "tablist");
    tabs.appendChild(el("span", "kw-bv-tabslabel", "Aperçu · affichage :"));
    var panel = el("div", "kw-bv-panel");
    var buttons = {};
    function choose(v) {
      Object.keys(buttons).forEach(function (k) { buttons[k].setAttribute("aria-selected", k === v ? "true" : "false"); });
      document.body.classList.toggle("kw-bv-on", v !== "actuelle");
      panel.textContent = "";
      if (v === "e") panel.appendChild(masterDetail(root, doms));
      if (v === "i") panel.appendChild(domainStrip(root, doms));
      if (v === "j") panel.appendChild(domainThenE(root, doms));
      if (v === "k") panel.appendChild(domainTabsThenE(root, doms));
      if (v === "l") panel.appendChild(eWithStrip(root, doms));
      if (v === "m") panel.appendChild(domainThenE(root, doms, detailWithNav));
      remember(v);
    }
    LABELS.forEach(function (l) {
      var b = el("button", "kw-bv-tab", l[1]); b.type = "button"; b.setAttribute("role", "tab");
      b.addEventListener("click", function () { choose(l[0]); });
      buttons[l[0]] = b; tabs.appendChild(b);
    });
    box.appendChild(tabs); box.appendChild(panel);
    var saved = remember();
    choose(buttons[saved] ? saved : "actuelle");
  }

  function load(box, then) {
    if (box.dataset.ready) return;
    box.dataset.ready = "1";
    fetch(box.dataset.json).then(function (r) { return r.json(); }).then(then).catch(function () { box.remove(); });
  }

  function init() {
    document.querySelectorAll(".kw-bv").forEach(function (box) { load(box, function (data) { variants(box, data); }); });
    document.querySelectorAll(".kw-bv-find").forEach(function (box) {
      load(box, function (data) {
        box.appendChild(facets(box.dataset.root || "", data, new URLSearchParams(window.location.search)));
      });
    });
  }

  if (window.document$ && window.document$.subscribe) window.document$.subscribe(init);
  else document.addEventListener("DOMContentLoaded", init);
})();
