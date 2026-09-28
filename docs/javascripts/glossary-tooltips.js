/* Glossaire au survol.
   Charge assets/glossary.json (généré par hooks/portal.py), souligne la PREMIÈRE
   occurrence de chaque terme dans le texte de la page (pas dans les titres, liens
   ni blocs de code) et affiche sa définition au survol, au focus clavier ou au toucher. */
(function () {
  var SKIP = "a, code, pre, h1, h2, h3, h4, h5, h6, script, style, button, label, summary, .kw-term, .kw-tip, .headerlink";
  var MAX_TERMS = 60;

  function base() {
    if (window.__md_scope) return window.__md_scope;
    var s = document.querySelector('script[src*="glossary-tooltips.js"]');
    return new URL(s ? s.src.replace(/javascripts\/glossary-tooltips\.js.*$/, "") : ".", location);
  }

  function escapeRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }

  function annotate(root, entries) {
    var byTerm = {};
    entries.forEach(function (e, i) { byTerm[e.t] = i; });
    var terms = entries.map(function (e) { return e.t; }).sort(function (a, b) { return b.length - a.length; });
    var re = new RegExp("(?<![\\p{L}\\p{N}])(" + terms.map(escapeRe).join("|") + ")(?![\\p{L}\\p{N}])", "gu");
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
      var text = node.nodeValue, last = 0, frag = null, m;
      re.lastIndex = 0;
      while ((m = re.exec(text))) {
        if (used[m[1]] || count >= MAX_TERMS) continue;
        used[m[1]] = true; count++;
        frag = frag || document.createDocumentFragment();
        frag.appendChild(document.createTextNode(text.slice(last, m.index)));
        var span = document.createElement("span");
        span.className = "kw-term";
        span.tabIndex = 0;
        span.setAttribute("role", "button");
        span.dataset.i = byTerm[m[1]];
        span.textContent = m[1];
        frag.appendChild(span);
        last = m.index + m[1].length;
      }
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
      link.textContent = "Glossaire →";
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
