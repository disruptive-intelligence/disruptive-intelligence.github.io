/* Outils de lecture de la veille (pages générées par hooks/portal.py) :
   - Explorer : filtre des sujets par mot, rubrique et fraîcheur ;
   - Pile de lecture : lectures cochées « lues », mémorisées dans ce navigateur ;
   - barre de progression de lecture sur les pages longues. */
(function () {
  function fold(text) {
    return text.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
  }

  function explorer() {
    var root = document.getElementById("kw-explorer");
    if (!root) return;
    var q = root.querySelector(".kw-explorer__q"), lane = root.querySelector(".kw-explorer__lane"),
        fresh = root.querySelector(".kw-explorer__fresh"), count = root.querySelector(".kw-explorer__count");
    var rows = Array.prototype.slice.call(root.querySelectorAll("tbody tr"));
    rows.forEach(function (r) { r._text = fold(r.textContent); });
    function apply() {
      var words = fold(q.value).split(/\s+/).filter(Boolean), shown = 0;
      rows.forEach(function (r) {
        var ok = (!lane.value || r.dataset.lane === lane.value) && (!fresh.value || r.dataset.fresh === fresh.value)
          && words.every(function (w) { return r._text.indexOf(w) >= 0; });
        r.hidden = !ok;
        if (ok) shown++;
      });
      count.textContent = shown + " / " + rows.length + " sujets";
    }
    [q, lane, fresh].forEach(function (el) { el.addEventListener("input", apply); });
    var hash = new URLSearchParams(location.search).get("q");
    if (hash) q.value = hash;
    apply();
  }

  function readings() {
    var root = document.getElementById("kw-readings");
    if (!root) return;
    var KEY = "kw-read", done = {};
    try { done = JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (e) { done = {}; }
    function save() { try { localStorage.setItem(KEY, JSON.stringify(done)); } catch (e) { /* stockage indisponible */ } }
    root.querySelectorAll(".kw-read").forEach(function (li) {
      var box = li.querySelector(".kw-read__box"), url = li.dataset.url;
      box.checked = !!done[url];
      li.classList.toggle("is-read", box.checked);
      box.addEventListener("change", function () {
        if (box.checked) done[url] = 1; else delete done[url];
        li.classList.toggle("is-read", box.checked);
        save();
      });
    });
    var toggle = document.querySelector(".kw-read__toggle");
    if (toggle) toggle.addEventListener("click", function (ev) {
      ev.preventDefault();
      var hide = !root.classList.contains("kw-hide-read");
      root.classList.toggle("kw-hide-read", hide);
      toggle.textContent = hide ? "Afficher les lectures faites" : "Masquer les lectures faites";
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

  function init() { explorer(); readings(); progress(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
