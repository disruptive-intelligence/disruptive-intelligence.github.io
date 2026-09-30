/* Glossaire au survol.
   Charge assets/glossary.json (généré par hooks/portal.py), souligne la PREMIÈRE
   occurrence de chaque terme dans la page (texte et titres des sujets ; pas le titre
   de page, les rubriques, les liens, le code ni le Lexique lui-même) et affiche sa
   définition au survol, au focus clavier ou au toucher.
   Sigles (TPU, CVE…) : casse exacte. Autres termes : casse libre, pluriel en -s/-x accepté. */
(function () {
  var SKIP = "a, code, pre, h1, h2, script, style, button, label, summary, .kw-term, .kw-tip, .headerlink, .kw-toc-m, .kw-thread, .kw-no-gloss";
  var MAX_TERMS = 80;

  function isAcronym(t) { return t === t.toUpperCase(); }

  function markLexicon(root) {           // les définitions du Lexique ne sont pas re-soulignées
    var h = Array.prototype.find.call(root.querySelectorAll("h2"), function (e) { return /Lexique|Repères pour comprendre/.test(e.textContent); });
    for (var n = h && h.nextElementSibling; n && n.tagName !== "H2"; n = n.nextElementSibling) n.classList.add("kw-no-gloss");
  }

  function base() {
    if (window.__md_scope) return window.__md_scope;
    var s = document.querySelector('script[src*="glossary-tooltips.js"]');
    return new URL(s ? s.src.replace(/javascripts\/glossary-tooltips\.js.*$/, "") : ".", location);
  }

  function escapeRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }

  function annotate(root, entries) {
    markLexicon(root);
    var byTerm = {};
    entries.forEach(function (e, i) { byTerm[isAcronym(e.t) ? e.t : e.t.toLowerCase()] = i; });
    function pattern(list, flags) {
      if (!list.length) return null;
      list.sort(function (a, b) { return b.length - a.length; });
      return new RegExp("(?<![\\p{L}\\p{N}])(" + list.map(escapeRe).join("|") + ")(?:s|x)?(?![\\p{L}\\p{N}])", flags);
    }
    var terms = entries.map(function (e) { return e.t; });
    var patterns = [pattern(terms.filter(isAcronym), "gu"), pattern(terms.filter(function (t) { return !isAcronym(t); }), "giu")]
      .filter(Boolean);
    function keyOf(found) { return byTerm[found] !== undefined ? found : found.toLowerCase(); }
    var used = {}, count = 0, nodes = [];
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!n.nodeValue.trim() || (n.parentElement && n.parentElement.closest(SKIP))) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (node) {
      if (count >= MAX_TERMS) return;
      var text = node.nodeValue, last = 0, frag = null, found = [];
      patterns.forEach(function (re) {
        var m;
        re.lastIndex = 0;
        while ((m = re.exec(text))) found.push({ at: m.index, text: m[0], key: keyOf(m[1]) });
      });
      found.sort(function (a, b) { return a.at - b.at || b.text.length - a.text.length; });
      found.forEach(function (f) {
        if (f.at < last || used[f.key] || count >= MAX_TERMS) return;
        used[f.key] = true; count++;
        frag = frag || document.createDocumentFragment();
        frag.appendChild(document.createTextNode(text.slice(last, f.at)));
        var span = document.createElement("span");
        span.className = "kw-term";
        span.tabIndex = 0;
        span.setAttribute("role", "button");
        span.dataset.i = byTerm[f.key];
        span.textContent = f.text;
        frag.appendChild(span);
        last = f.at + f.text.length;
      });
      if (frag) {
        frag.appendChild(document.createTextNode(text.slice(last)));
        node.parentNode.replaceChild(frag, node);
      }
    });
  }

  function setup(entries, scope) {
    var tip = document.createElement("div");
    tip.className = "kw-tip";
    tip.setAttribute("role", "tooltip");
    document.body.appendChild(tip);
    var current = null, hideTimer = null;

    function show(term) {
      clearTimeout(hideTimer);
      var e = entries[term.dataset.i];
      tip.textContent = "";
      var title = document.createElement("strong");
      title.textContent = e.t;
      var link = document.createElement("a");
      link.href = new URL(e.u, scope).href;
      link.textContent = /^library\/(?!glossaire\/)/.test(e.u) ? "Voir la fiche →" : "Glossaire →";   // fiche notion
      tip.append(title, document.createTextNode(e.d + " "), link);
      tip.classList.add("is-open");
      var r = term.getBoundingClientRect(), w = tip.offsetWidth, h = tip.offsetHeight;
      var left = Math.min(Math.max(8, r.left + r.width / 2 - w / 2), document.documentElement.clientWidth - w - 8);
      var below = r.bottom + h + 12 < window.innerHeight;
      tip.style.left = left + window.scrollX + "px";
      tip.style.top = (below ? r.bottom + 8 : r.top - h - 8) + window.scrollY + "px";
      current = term;
    }
    function hide(delay) {
      clearTimeout(hideTimer);
      hideTimer = setTimeout(function () { tip.classList.remove("is-open"); current = null; }, delay || 0);
    }

    document.addEventListener("mouseover", function (ev) {
      var t = ev.target.closest && ev.target.closest(".kw-term");
      if (t) show(t);
      else if (ev.target.closest && ev.target.closest(".kw-tip")) clearTimeout(hideTimer);
    });
    document.addEventListener("mouseout", function (ev) {
      if (ev.target.closest && (ev.target.closest(".kw-term") || ev.target.closest(".kw-tip"))) hide(250);
    });
    document.addEventListener("focusin", function (ev) {
      if (ev.target.classList && ev.target.classList.contains("kw-term")) show(ev.target);
    });
    document.addEventListener("focusout", function (ev) {
      if (ev.target.classList && ev.target.classList.contains("kw-term")) hide(250);
    });
    document.addEventListener("click", function (ev) {        // toucher sur téléphone
      var t = ev.target.closest && ev.target.closest(".kw-term");
      if (t) { if (current === t && tip.classList.contains("is-open")) hide(); else show(t); }
      else if (!(ev.target.closest && ev.target.closest(".kw-tip"))) hide();
    });
    document.addEventListener("keydown", function (ev) { if (ev.key === "Escape") hide(); });
    window.addEventListener("scroll", function () { if (current && matchMedia("(hover: none)").matches) hide(); }, { passive: true });
  }

  function init() {
    var root = document.querySelector(".md-content article");
    if (!root || /\/library\/glossaire\/?$/.test(location.pathname)) return;
    var scope = base();
    fetch(new URL("assets/glossary.json", scope))
      .then(function (r) { return r.ok ? r.json() : []; })
      .then(function (entries) {
        if (!entries.length) return;
        annotate(root, entries);
        if (root.querySelector(".kw-term")) setup(entries, scope);
      })
      .catch(function () { /* pas de glossaire : la page reste normale */ });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
