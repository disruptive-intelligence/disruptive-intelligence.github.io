---
title: ◆◆◆ Actionneurs robotiques
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — composant · **Couche** — agir

**En une phrase.** Les dispositifs qui convertissent l'énergie en mouvement — et qui déterminent, plus que toute autre pièce, ce qu'une machine peut faire et ce qu'elle coûte.

**Pourquoi on en parle.** Parce que c'est **la brique déterminante de toute la couche et la moins discutée**. Les débats portent sur les modèles et la perception ; les limites viennent le plus souvent d'ici.

**Comment ça fonctionne — trois familles.**

**Électrique.** Un moteur associé à un réducteur. Précis, propre, facile à commander, rendement élevé. Mais un moteur tourne vite avec peu de couple, alors que l'application demande l'inverse : il faut donc un **réducteur**, qui introduit du jeu, du frottement, de l'inertie et de l'usure. **Le réducteur devient souvent le composant qui limite la précision et la durée de vie de l'ensemble** — cas net du mécanisme du volume 1 : résoudre le problème du couple crée le problème du jeu.

**Hydraulique.** Densité de puissance très supérieure, capacité à encaisser les chocs. Mais une centrale, des conduites, des fuites, un rendement moindre et un entretien lourd.

**Quasi-direct.** Un moteur à couple élevé avec une réduction faible ou nulle. On perd en couple maximal, on gagne en absence de jeu, en réversibilité — la machine peut être poussée à la main — et en capacité à mesurer les efforts sans capteur dédié. **C'est l'approche qui a rendu praticables les machines à pattes et une partie des humanoïdes.**

**Les grandeurs qui comptent.** Couple maximal · densité de puissance par kilogramme · précision et jeu · rendement · durée de vie en cycles · et **capacité à encaisser un choc**, souvent oubliée alors qu'elle décide de la survie de la machine en usage réel.

**Ce qui bloque.** **La dissipation.** Un actionneur perd son énergie en chaleur, dans un volume restreint, souvent sans circulation d'air. **La densité de puissance réellement utilisable est bornée par l'évacuation thermique**, non par les caractéristiques électriques — c'est pourquoi un actionneur peut délivrer un couple élevé brièvement et pas en continu.

S'y ajoutent le **coût**, qui domine celui d'une machine multi-articulée, et **l'usure**, qui produit du jeu et donc une imprécision que les capteurs articulaires ne voient pas.

**Ce que cela implique.** Une machine peut être précise selon ses capteurs et imprécise en réalité, parce que le jeu se situe en aval de la mesure. **C'est une défaillance silencieuse d'origine mécanique**, et elle croît avec l'usage.

**À ne pas confondre avec.** **Le moteur seul**, qui n'est qu'un élément de l'actionneur — lequel comprend aussi la réduction, l'électronique de commande, les capteurs et souvent le refroidissement.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Progrès continus sur la densité de puissance et sur les architectures quasi-directes ; le coût unitaire reste le facteur dominant du prix des machines multi-articulées.
> 🔄 **À revoir si** un actionneur combine densité de puissance hydraulique et propreté électrique à un coût de série.

**Renvois** — Couche : agir · Convergence : robotique généraliste (36) · Voir aussi : électronique de puissance (ch. 23).

---


## ◆◆ Mains et préhenseurs

**Niveau** — composant · **Couche** — agir

**En une phrase.** L'interface entre la machine et l'objet — et le sous-système où se joue la généralité.

**Comment ça fonctionne.** Un continuum, du plus spécialisé au plus général. La **ventouse** saisit rapidement des surfaces planes et lisses, à faible coût. La **pince à deux doigts** couvre une large variété d'objets rigides. La **main multi-doigts** permet en principe la réorientation en main et la manipulation fine, au prix d'une complexité considérable.

**L'arbitrage est net** : plus le préhenseur est général, plus il est cher, fragile et difficile à commander. En pratique, la plupart des déploiements industriels utilisent le préhenseur le plus spécialisé que la tâche autorise.

**Ce qui bloque.** **La perception du contact.** Sans retour tactile, la machine ne sait pas si elle tient, si elle serre trop, si l'objet glisse. C'est le lien direct avec la peau électronique du chapitre 7, et c'est le verrou. **La durabilité** : le préhenseur est la pièce qui frotte et qui reçoit les chocs. Et **le nombre d'actionneurs** d'une main multi-doigts, qui multiplie coût, masse et modes de panne.

**Ce que cela implique.** La généralité d'une machine se mesure moins à sa morphologie qu'à **la variété d'objets que son préhenseur peut saisir sans changement d'outil**. C'est une grandeur observable, rarement publiée.

**À ne pas confondre avec.** **La main humaine**, dont la densité de capteurs et la capacité de réorientation restent hors de portée — la comparaison est trompeuse et alimente des attentes non fondées.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour les préhenseurs simples, 🔬 émergent pour les mains multi-doigts en exploitation.
> 🔄 **À revoir si** une main multi-doigts démontre plusieurs milliers d'heures d'exploitation avec un taux de panne compatible avec un usage industriel.

**Renvois** — Couche : agir.

---
