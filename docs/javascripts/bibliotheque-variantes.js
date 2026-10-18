/* Bibliothèque — variantes de navigation (aperçu) : sélecteur Actuelle / A Explorateur / B Sommaire / C Filtres.
   Données : assets/bibliotheque-arbre.json (hooks/portal.py, library_tree). Sans JS, la page actuelle reste. */
(function () {
  "use strict";

  var KEY = "kw-bv-variante";
  var LABELS = [["actuelle", "Actuelle"], ["a", "A · Explorateur"], ["b", "B · Sommaire détaillé"], ["c", "C · Filtres"]];
  var FORMATS = { cours: "Cours", synthese: "Synthèse", fiche: "Fiche notion", "aide-memoire": "Aide-mémoire",
                  atelier: "Atelier", ressources: "Ressources", revision: "Révision" };

  function remember(value) {
    try {
      if (value === undefined) return localStorage.getItem(KEY);
      localStorage.setItem(KEY, value);
    } catch (e) { /* stockage indisponible : on garde le choix pour la page */ }
    return null;
  }

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text !== undefined) n.textContent = text;
    return n;
  }

  function link(root, item, cls) {
    var a = el("a", cls, item.t);
    a.href = root + item.u;
    return a;
  }

  function fold(s) {
    return (s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
  }

  function meta(note) {
    var bits = [];
    if (note.f) bits.push(FORMATS[note.f] || note.f);
    if (note.p) bits.push(note.p);
    if (note.m) bits.push(note.m >= 60 ? Math.round(note.m / 60 * 10) / 10 + " h" : note.m + " min");
    return bits.join(" · ");
  }

  function isLab(t) { return /^labs?\b/i.test(t || ""); }

  // ---------------------------------------------------------------- A · Explorateur
  function explorer(root, doms) {
    var wrap = el("div", "kw-bv-a");
    var bar = el("div", "kw-bv-bar");
    var input = el("input", "kw-bv-input");
    input.type = "search";
    input.placeholder = "Filtrer : un cours, un chapitre, un outil (kerberos, Sysmon 7, logman…)";
    input.setAttribute("aria-label", "Filtrer l'arborescence");
    var count = el("span", "kw-bv-count");
    bar.appendChild(input); bar.appendChild(count);
    wrap.appendChild(bar);
    var tree = el("ul", "kw-bv-tree");
    wrap.appendChild(tree);

    function node(item, level) {
      var li = el("li", "kw-bv-node kw-bv-l" + level);
      li.dataset.text = fold(item.t);
      var kids = item.c || item.g || item.n;
      if (item.g) {                                            // rubrique : sous-rubriques puis notes
        var det = el("details");
        var sum = el("summary"); sum.appendChild(link(root, item, "kw-bv-cat")); det.appendChild(sum);
        var ul = el("ul");
        item.g.forEach(function (g) {
          if (g.t) {
            var gl = el("li", "kw-bv-node kw-bv-group"); gl.dataset.text = fold(g.t);
            var gd = el("details"); gd.appendChild(el("summary", "kw-bv-glabel", g.t));
            var gu = el("ul"); g.n.forEach(function (n) { gu.appendChild(node(n, level + 1)); });
            gd.appendChild(gu); gl.appendChild(gd); ul.appendChild(gl);
          } else {
            g.n.forEach(function (n) { ul.appendChild(node(n, level + 1)); });
          }
        });
        det.appendChild(ul); li.appendChild(det);
        return li;
      }
      if (kids && kids.length) {
        var d = el("details");
        var s = el("summary"); s.appendChild(link(root, item, isLab(item.t) ? "kw-bv-lab" : ""));
        if (item.f || item.p) s.appendChild(el("span", "kw-bv-meta", meta(item)));
        d.appendChild(s);
        var u = el("ul"); kids.forEach(function (k) { u.appendChild(node(k, level + 1)); });
        d.appendChild(u); li.appendChild(d);
      } else {
        li.appendChild(link(root, item, isLab(item.t) ? "kw-bv-lab" : ""));
        if (item.f || item.p) li.appendChild(el("span", "kw-bv-meta", meta(item)));
      }
      return li;
    }

    doms.forEach(function (d) {
      var li = el("li", "kw-bv-node kw-bv-dom");
      li.dataset.text = fold(d.t);
      var det = el("details"); det.open = true;
      var sum = el("summary"); sum.appendChild(link(root, d, "kw-bv-domlink")); det.appendChild(sum);
      var ul = el("ul"); d.c.forEach(function (c) { ul.appendChild(node(c, 1)); });
      det.appendChild(ul); li.appendChild(det); tree.appendChild(li);
    });

    function apply() {
      var q = fold(input.value.trim());
      var hits = 0;
      function visit(li) {
        var own = q && li.dataset.text.indexOf(q) !== -1;
        var kids = li.querySelectorAll(":scope > details > ul > li, :scope > ul > li");
        var below = false;
        kids.forEach(function (k) { if (visit(k)) below = true; });
        var show = !q || own || below;
        li.hidden = !show;
        li.classList.toggle("kw-bv-hit", !!own);
        if (own) hits++;
        var det = li.querySelector(":scope > details");
        if (det) det.open = q ? below : li.classList.contains("kw-bv-dom");
        return own || below;
      }
      tree.querySelectorAll(":scope > li").forEach(visit);
      count.textContent = q ? hits + " résultat" + (hits > 1 ? "s" : "") : "";
    }
    input.addEventListener("input", apply);
    return wrap;
  }

  // ---------------------------------------------------------------- B · Sommaire détaillé
  function summary(root, doms) {
    var wrap = el("div", "kw-bv-b");
    doms.forEach(function (d) {
      d.c.forEach(function (c) {
        var h = el("h2", "kw-bv-btitle"); h.appendChild(link(root, c)); wrap.appendChild(h);
        c.g.forEach(function (g) {
          if (g.t) wrap.appendChild(el("h3", "kw-bv-bgroup", g.t));
          var grid = el("div", "kw-bv-grid");
          g.n.forEach(function (n) {
            var card = el("article", "kw-bv-card");
            var head = el("div", "kw-bv-cardhead");
            head.appendChild(link(root, n, "kw-bv-cardtitle"));
            var m = meta(n); if (m) head.appendChild(el("span", "kw-bv-meta", m));
            card.appendChild(head);
            if (n.c && n.c.length) {
              var list = el("ol", "kw-bv-toc");
              n.c.forEach(function (p) {
                var li = el("li");
                li.appendChild(link(root, p, (p.c && p.c.length ? "kw-bv-part" : "") + (isLab(p.t) ? " kw-bv-lab" : "")));
                if (p.c && p.c.length) {
                  var sub = el("ul");
                  p.c.forEach(function (ch) { var s = el("li"); s.appendChild(link(root, ch, isLab(ch.t) ? "kw-bv-lab" : "")); sub.appendChild(s); });
                  li.appendChild(sub);
                }
                list.appendChild(li);
              });
              if (n.c.length > 8) {
                var det = el("details", "kw-bv-more");
                det.appendChild(el("summary", "", n.c.length + " pages — afficher le sommaire"));
                det.appendChild(list); card.appendChild(det);
              } else {
                card.appendChild(list);
              }
            } else {
              card.appendChild(el("p", "kw-bv-one", "Une seule page."));
            }
            grid.appendChild(card);
          });
          wrap.appendChild(grid);
        });
      });
    });
    return wrap;
  }

  // ---------------------------------------------------------------- C · Filtres
  function facets(root, doms, scoped) {
    var rows = [];
    doms.forEach(function (d) {
      d.c.forEach(function (c) {
        c.g.forEach(function (g) {
          g.n.forEach(function (n) {
            rows.push({ t: n.t, u: n.u, dom: d.t, cat: c.t, grp: g.t, course: "", where: [c.t, g.t].filter(Boolean).join(" › "),
                        f: n.f, p: n.p, kind: "note" });
            (function walk(items, trail) {
              (items || []).forEach(function (it) {
                rows.push({ t: it.t, u: it.u, dom: d.t, cat: c.t, grp: g.t, course: n.t, where: [n.t].concat(trail).join(" › "),
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
      bar.appendChild(s);
      return s;
    }
    function uniq(key) {
      var seen = {}; var out = [];
      rows.forEach(function (r) { if (r[key] && !seen[r[key]]) { seen[r[key]] = 1; out.push([r[key], r[key]]); } });
      return out;
    }
    var sDom = scoped ? null : select("Domaine", uniq("dom"));
    var sCat = scoped ? select("Sous-rubrique", uniq("grp")) : select("Rubrique", uniq("cat"));
    var sKind = select("Type", [["note", "Cours et fiches (entrée)"], ["chapitre", "Chapitres"], ["lab", "Labs"]]);
    var sFmt = select("Format", Object.keys(FORMATS).filter(function (k) {
      return rows.some(function (r) { return r.kind === "note" && r.f === k; });
    }).map(function (k) { return [k, FORMATS[k]]; }));
    var sProv = select("Provenance", uniq("p"));
    var count = el("span", "kw-bv-count"); bar.appendChild(count);
    wrap.appendChild(bar);
    var list = el("ul", "kw-bv-results"); wrap.appendChild(list);

    function apply() {
      var q = fold(input.value.trim());
      var shown = 0, total = 0;
      list.textContent = "";
      rows.forEach(function (r) {
        if (sDom && sDom.value && r.dom !== sDom.value) return;
        if (sCat.value && (scoped ? r.grp : r.cat) !== sCat.value) return;
        if (sKind.value === "note" && r.kind !== "note") return;
        if (sKind.value === "chapitre" && r.f !== "chapitre") return;
        if (sKind.value === "lab" && r.f !== "lab") return;
        if (sFmt.value && !(r.kind === "note" ? r.f === sFmt.value : false)) return;
        if (sProv.value && r.p !== sProv.value) return;
        if (q && fold(r.t + " " + r.where).indexOf(q) === -1) return;
        total++;
        if (shown >= 250) return;
        shown++;
        var li = el("li", "kw-bv-row" + (r.kind === "note" ? " kw-bv-row--note" : ""));
        li.appendChild(link(root, r, r.f === "lab" ? "kw-bv-lab" : ""));
        var info = r.kind === "note" ? [r.where, FORMATS[r.f] || r.f, r.p] : [r.where, r.f === "lab" ? "Lab" : ""];
        li.appendChild(el("span", "kw-bv-meta", info.filter(Boolean).join(" · ")));
        list.appendChild(li);
      });
      count.textContent = total + " page" + (total > 1 ? "s" : "") + (total > shown ? " (250 affichées)" : "");
    }
    [input, sDom, sCat, sKind, sFmt, sProv].forEach(function (x) { if (x) x.addEventListener(x === input ? "input" : "change", apply); });
    apply();
    return wrap;
  }

  // ---------------------------------------------------------------- sélecteur
  function build(box, data) {
    var root = box.dataset.root || "";
    var scope = box.dataset.scope || "";
    var doms = data;
    if (scope) {
      doms = [];
      data.forEach(function (d) {
        d.c.forEach(function (c) { if (c.id === scope) doms.push({ t: d.t, u: d.u, c: [c] }); });
      });
    }
    var tabs = el("div", "kw-bv-tabs");
    tabs.setAttribute("role", "tablist");
    tabs.appendChild(el("span", "kw-bv-tabslabel", "Aperçu · affichage :"));
    var panel = el("div", "kw-bv-panel");
    var buttons = {};
    function choose(v) {
      Object.keys(buttons).forEach(function (k) { buttons[k].setAttribute("aria-selected", k === v ? "true" : "false"); });
      document.body.classList.toggle("kw-bv-on", v !== "actuelle");
      panel.textContent = "";
      if (v === "a") panel.appendChild(explorer(root, doms));
      if (v === "b") panel.appendChild(summary(root, doms));
      if (v === "c") panel.appendChild(facets(root, doms, !!scope));
      remember(v);
    }
    LABELS.forEach(function (l) {
      var b = el("button", "kw-bv-tab", l[1]);
      b.type = "button"; b.setAttribute("role", "tab");
      b.addEventListener("click", function () { choose(l[0]); });
      buttons[l[0]] = b; tabs.appendChild(b);
    });
    box.appendChild(tabs);
    box.appendChild(panel);
    var saved = remember();
    choose(buttons[saved] ? saved : "actuelle");
  }

  function init() {
    document.querySelectorAll(".kw-bv").forEach(function (box) {
      if (box.dataset.ready) return;
      box.dataset.ready = "1";
      fetch(box.dataset.json).then(function (r) { return r.json(); }).then(function (data) { build(box, data); })
        .catch(function () { box.remove(); });
    });
  }

  if (window.document$ && window.document$.subscribe) window.document$.subscribe(init);
  else document.addEventListener("DOMContentLoaded", init);
})();
