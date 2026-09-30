---
title: ◆◆ Calcul analogique
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — calculer

**En une phrase.** Représenter une valeur par une grandeur physique continue — tension, courant, charge, conductance — et laisser la physique effectuer le calcul.

**Comment ça fonctionne.** Additionner deux courants réalise une addition, sans aucune opération logique. Le calcul devient une propriété du circuit plutôt qu'une séquence d'instructions. C'est l'approche historique, abandonnée au profit du numérique dans les années 1960 pour une raison précise.

**Cette raison est toujours valable.** Le numérique n'est pas plus fidèle que l'analogique : il est **plus stable**. En ne conservant que deux niveaux largement séparés, il recopie l'information à l'identique indéfiniment, tant que le bruit reste sous le seuil de décision. L'analogique renonce à cette protection : chaque étape ajoute du bruit, et les erreurs s'accumulent.

**Ce que ça permet.** Une efficacité énergétique très supérieure sur des opérations simples et massivement répétées.

**Ce qui bloque.** **La précision et sa non-reproductibilité.** Deux exemplaires du même circuit ne donnent pas exactement le même résultat — variations de fabrication, dérive en température, vieillissement. Cela impose un étalonnage par exemplaire, complique le test, et rend délicate toute qualification. C'est la contrainte que le volume 1 identifiait comme propre à cette famille.

**Ce que cela implique.** L'analogique revient là où **l'imprécision est tolérable et l'énergie critique** — c'est-à-dire dans une partie de l'inférence embarquée. Il ne revient pas dans le calcul exact, et cette frontière est stable.

**À ne pas confondre avec.** **La faible précision numérique**, qui est un choix reproductible et contrôlé.

> ⏱ **État au 23/08/2026** — 🔬 émergent, essentiellement sous la forme du calcul en mémoire.
> 🔄 **À revoir si** une technique d'étalonnage automatique rend les performances reproductibles à l'échelle d'une production de série.

**Renvois** — Couche : calculer.

---


## ◆ Calcul supraconducteur

**Niveau** — famille · **Couche** — calculer

**En une phrase.** Utiliser des circuits supraconducteurs, sans résistance électrique, pour commuter à très haute fréquence en dissipant très peu.

**Ce qui bloque.** **Le refroidissement.** Ces circuits fonctionnent à quelques kelvins ; l'énergie dépensée pour les maintenir à cette température dépasse largement celle qu'ils économisent, sauf à très grande échelle. S'y ajoutent l'absence de mémoire dense compatible et un écosystème inexistant.

**À ne pas confondre avec.** **Le calcul quantique à supraconducteurs**, qui utilise des circuits similaires mais pour un tout autre principe — il s'agit ici de logique classique très rapide, pas de qubits.

> ⏱ **État au 23/08/2026** — 🔭 prospectif. Domaine de recherche ancien, applications limitées à l'instrumentation.
> 🔄 **À revoir si** la cryogénie devient de toute façon nécessaire à grande échelle pour une autre raison — le coût du refroidissement serait alors déjà payé.

**Renvois** — Couche : calculer.

---


## ◆ Architectures non von Neumann

**Niveau** — cadrage · **Couche** — calculer

**En une phrase.** Terme générique désignant toute architecture qui s'écarte de la séparation classique entre une mémoire, une unité de calcul et un flux d'instructions.

**Ce qu'il faut en savoir.** **C'est un terme fourre-tout**, défini par ce qu'il n'est pas. Il recouvre le calcul en mémoire, le neuromorphique, les architectures à flot de données et plusieurs autres approches qui n'ont en commun ni leurs principes, ni leurs verrous, ni leurs applications.

**À ne pas confondre avec.** Une famille technologique. Employé dans une phrase du type « les architectures non von Neumann vont remplacer », le terme ne désigne rien de vérifiable.

**Ce qu'il vous fait manquer.** **Lequel des trois murs est attaqué.** Chaque approche vise une contrainte précise — le déplacement, l'énergie, ou la nature du problème. Le terme générique efface cette distinction, qui est la seule qui compte.

> ⏱ **État au 23/08/2026** — sans objet : cadrage et non technologie.

**Renvois** — Couche : calculer.

---
