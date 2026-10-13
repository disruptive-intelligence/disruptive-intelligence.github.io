// Cartes mentales des cheat sheets : une liste Markdown dans <div class="kw-mindmap"> devient une carte
// repliable (markmap). Sans JavaScript, la liste reste lisible telle quelle. Les bibliothèques ne sont
// chargées que sur les pages qui ont une carte.
(function () {
  var D3 = "https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js";
  var VIEW = "https://cdn.jsdelivr.net/npm/markmap-view@0.18.12/dist/browser/index.js";
  var BRANCHES = ["#8f9bff", "#ff4d5a", "#e0b12a", "#3fbf9f", "#e879b9", "#5bb8e6", "#f08a5d", "#a98bff"];

  function load(src) {
    return new Promise(function (ok, ko) {
      var s = document.createElement("script");
      s.src = src; s.onload = ok; s.onerror = ko;
      document.head.appendChild(s);
    });
  }

  function toNode(li) {                              // <li> → nœud markmap { content, children }
    var parts = [], children = [];
    li.childNodes.forEach(function (c) {
      if (c.nodeType === 1 && c.tagName === "UL") {
        c.querySelectorAll(":scope > li").forEach(function (sub) { children.push(toNode(sub)); });
      } else if (c.nodeType === 1 && c.tagName === "P") {
        parts.push(c.innerHTML);
      } else {
        parts.push(c.nodeType === 1 ? c.outerHTML : (c.textContent || "").replace(/</g, "&lt;"));
      }
    });
    return { content: parts.join("").trim(), children: children };
  }

  function markBranches(data) {                    // une couleur par branche principale, héritée par ses nœuds
    data.children.forEach(function (child, i) {
      (function walk(n) {
        n.payload = Object.assign({}, n.payload, { branch: i });
        n.children.forEach(walk);
      })(child);
    });
  }

  function branchColor(node) {
    var b = node.payload && node.payload.branch;
    return b === undefined ? "var(--kw-link)" : BRANCHES[b % BRANCHES.length];
  }

  function setFold(mm, fold) {                       // fold : fonction(profondeur) → 0 ouvert, 1 replié
    (function walk(n) {
      n.payload = Object.assign({}, n.payload, { fold: (n.children || []).length ? fold(n.state.depth) : 0 });
      (n.children || []).forEach(walk);
    })(mm.state.data);
    return mm.renderData();
  }

  function visibleBounds(root) {                     // étendue des nœuds affichés, en unités de la carte
    var b = { x1: Infinity, y1: Infinity, x2: -Infinity, y2: -Infinity };
    (function walk(n) {
      var r = n.state.rect;
      b.x1 = Math.min(b.x1, r.x); b.y1 = Math.min(b.y1, r.y);
      b.x2 = Math.max(b.x2, r.x + r.width); b.y2 = Math.max(b.y2, r.y + r.height);
      if (!(n.payload && n.payload.fold)) (n.children || []).forEach(walk);
    })(root);
    return b;
  }

  // Le cadre grandit avec ce qui est déplié : le texte garde une taille lisible au lieu de rétrécir.
  function autoHeight(mm, stage, box) {
    var render = mm.renderData.bind(mm);
    mm.renderData = function (d) {
      return render(d).then(function () {
        if (document.fullscreenElement !== box) {
          var b = visibleBounds(mm.state.data);
          var scale = Math.min(1, (stage.clientWidth - 40) / (b.x2 - b.x1));
          var h = Math.round((b.y2 - b.y1) * scale + 60);
          stage.style.height = Math.max(MIN_H(), Math.min(h, 2600)) + "px";
        }
        return mm.fit();
      });
    };
  }

  function MIN_H() { return window.innerWidth <= 600 ? 320 : 560; }

  function button(label, title, onClick) {
    var b = document.createElement("button");
    b.type = "button"; b.className = "kw-mindmap__btn"; b.textContent = label; b.title = title;
    b.addEventListener("click", onClick);
    return b;
  }

  function build(box) {
    var ul = box.querySelector(":scope > ul");
    if (!ul) return;
    var roots = ul.querySelectorAll(":scope > li");
    var data = roots.length === 1 ? toNode(roots[0]) : { content: "", children: [].map.call(roots, toNode) };

    markBranches(data);

    var stage = document.createElement("div");
    stage.className = "kw-mindmap__stage";
    var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    stage.appendChild(svg);

    box.appendChild(stage);                          // mesuré avant le premier rendu
    var mm = new window.markmap.Markmap(svg, {
      autoFit: false, maxInitialScale: 1, duration: 350, initialExpandLevel: 2, maxWidth: 300,
      paddingX: 10, spacingVertical: 8, spacingHorizontal: 70, color: branchColor
    });
    autoHeight(mm, stage, box);
    mm.setData(data);

    var bar = document.createElement("div");
    bar.className = "kw-mindmap__bar";
    bar.appendChild(button("Tout déplier", "Ouvrir toutes les branches", function () { setFold(mm, function () { return 0; }); }));
    bar.appendChild(button("Replier", "Revenir aux grandes branches", function () { setFold(mm, function (d) { return d >= 2 ? 1 : 0; }); }));
    bar.appendChild(button("Recentrer", "Recadrer la carte", function () { mm.fit(); }));
    bar.appendChild(button("⛶ Plein écran", "Afficher la carte en plein écran", function () {
      if (document.fullscreenElement) document.exitFullscreen();
      else if (box.requestFullscreen) box.requestFullscreen();
    }));
    var hint = document.createElement("span");
    hint.className = "kw-mindmap__hint";
    hint.textContent = "Clic sur un nœud : déplier · Ctrl + molette : zoom · glisser : déplacer";
    bar.appendChild(hint);

    // La molette fait défiler la page ; Ctrl + molette (ou le plein écran) zoome sur la carte.
    stage.addEventListener("wheel", function (e) {
      if (!e.ctrlKey && document.fullscreenElement !== box) e.stopPropagation();
    }, true);
    document.addEventListener("fullscreenchange", function () {
      setTimeout(function () { mm.renderData(); }, 120);
    });

    ul.hidden = true;                                // la liste reste dans la page (recherche, sans JS)
    box.classList.add("kw-mindmap--ready");
    box.insertBefore(bar, stage);
  }

  function init() {
    var boxes = document.querySelectorAll(".kw-mindmap");
    if (!boxes.length) return;
    load(D3).then(function () { return load(VIEW); }).then(function () {
      boxes.forEach(build);
    }).catch(function () { /* bibliothèque injoignable : la liste reste affichée */ });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
