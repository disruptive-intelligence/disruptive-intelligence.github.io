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

  if (window.document$) window.document$.subscribe(init);   // navigation instantanée de Material
  else document.addEventListener("DOMContentLoaded", init);
})();
