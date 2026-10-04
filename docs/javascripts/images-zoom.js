// Images des notes : un clic ouvre l'image en grand (taille réelle, dans la limite de l'écran) ; clic ou Échap
// pour fermer. Les images sont affichées en taille réduite dans le texte (stylesheets/extra.css).
(function () {
  function close(box) {
    box.remove();
    document.removeEventListener("keydown", box._onKey);
  }

  function open(img) {
    var box = document.createElement("figure");
    box.className = "kw-zoom";
    var big = document.createElement("img");
    big.src = img.currentSrc || img.src;
    big.alt = img.alt;
    box.appendChild(big);
    if (img.alt) {
      var cap = document.createElement("figcaption");
      cap.textContent = img.alt;
      box.appendChild(cap);
    }
    box._onKey = function (e) { if (e.key === "Escape") close(box); };
    box.addEventListener("click", function () { close(box); });
    document.addEventListener("keydown", box._onKey);
    document.body.appendChild(box);
  }

  function init() {
    document.addEventListener("click", function (e) {
      var img = e.target.closest && e.target.closest(".md-typeset p > img");
      if (!img || img.closest("a")) return;
      e.preventDefault();
      open(img);
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
