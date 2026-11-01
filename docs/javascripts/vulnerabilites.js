// Veille vulnérabilités (accueil, page dédiée) : heure de lecture des flux en heure locale,
// et pastille « nouveau » sur ce qui a moins de 36 h, calculée au moment où l'on lit la page.
(function () {
  var DAY = 36 * 3600 * 1000;

  function ago(ms) {
    var min = Math.round(ms / 60000);
    if (min < 60) return "il y a " + Math.max(min, 1) + " min";
    var h = Math.round(min / 60);
    if (h < 48) return "il y a " + h + " h";
    return "il y a " + Math.round(h / 24) + " jours";
  }

  function init() {
    var now = Date.now();
    document.querySelectorAll(".kw-vuln-age[data-ts]").forEach(function (el) {
      var t = new Date(el.dataset.ts);
      if (isNaN(t)) return;
      var time = t.toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit" });
      var day = t.toLocaleDateString("fr-FR", { weekday: "long", day: "numeric", month: "long" });
      el.textContent = "Flux lus " + ago(now - t) + " (" + day + ", " + time.replace(":", " h ") + ")";
      el.classList.toggle("is-old", now - t > 18 * 3600 * 1000);
    });
    document.querySelectorAll(".kw-vl[data-ts]").forEach(function (li) {
      var t = new Date(li.dataset.ts);
      if (!isNaN(t) && now - t < DAY && !li.querySelector(".kw-vb--new")) {
        var badges = li.querySelector(".kw-vl__badges");
        if (!badges) return;
        var b = document.createElement("span");
        b.className = "kw-vb kw-vb--new";
        b.textContent = "Nouveau";
        badges.insertBefore(b, badges.firstChild);
      }
    });
  }

  // Bouton « 📋 Fiche » : copie la fiche de suivi (texte brut) dans le presse-papiers.
  // Copie classique d'abord : immédiate pendant le clic, sans permission à attendre ;
  // l'API Clipboard ne sert qu'en secours (elle peut rester en attente d'une autorisation).
  function copy(text) {
    var ok = false;
    var area = document.createElement("textarea");
    area.value = text;
    area.setAttribute("readonly", "");
    area.style.position = "fixed";
    area.style.top = "0";
    area.style.opacity = "0";
    document.body.appendChild(area);
    area.select();
    try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
    document.body.removeChild(area);
    if (ok) return Promise.resolve();
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    return Promise.reject();
  }

  document.addEventListener("click", function (ev) {
    var btn = ev.target.closest && ev.target.closest(".kw-vcopy");
    if (!btn) return;
    ev.preventDefault();
    var label = btn.dataset.label || (btn.dataset.label = btn.textContent);
    copy(btn.dataset.fiche).then(function () {
      btn.textContent = "✓ Copiée";
      btn.classList.add("is-done");
    }, function () {
      btn.textContent = "Copie impossible";
    }).then(function () {
      setTimeout(function () { btn.textContent = label; btn.classList.remove("is-done"); }, 1800);
    });
  });

  if (window.document$) window.document$.subscribe(init);   // navigation instantanée de Material
  else document.addEventListener("DOMContentLoaded", init);
})();
