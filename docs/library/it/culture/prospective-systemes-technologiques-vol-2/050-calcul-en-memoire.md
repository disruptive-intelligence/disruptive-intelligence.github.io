---
title: ◆◆◆ Calcul en mémoire
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — calculer

**En une phrase.** Effectuer l'opération là où la donnée réside, au lieu de la déplacer vers une unité de calcul.

**Pourquoi on en parle.** Parce que c'est **la seule approche qui attaque frontalement la contrainte dominante de la couche** — si déplacer coûte des centaines de fois plus que traiter, la meilleure optimisation consiste à ne pas déplacer.

**Comment ça fonctionne.** Deux familles très différentes portent ce nom.

Le **calcul près de la mémoire** place des unités de calcul simples dans le composant mémoire lui-même. L'approche est modérée, compatible avec les procédés existants, et les gains sont réels sans être spectaculaires.

Le **calcul dans la mémoire** au sens strict utilise les propriétés physiques du réseau de cellules pour réaliser l'opération. Dans une matrice de cellules dont chacune stocke une valeur sous forme de conductance, appliquer des tensions en entrée produit, par simple addition de courants, le résultat d'une multiplication matricielle — **en une seule opération physique, sans qu'aucune donnée ne circule**. Le gain énergétique potentiel est d'un ou deux ordres de grandeur.

**Ce qui bloque.** **La précision.** L'approche stricte est analogique : la valeur stockée est une grandeur physique, donc bruitée, dérivant avec la température et variant d'une cellule à l'autre. **La précision atteignable est limitée et, surtout, elle n'est pas reproductible d'un exemplaire à l'autre** — ce qui pose des problèmes de conception, de test et de qualification que le numérique n'a pas.

S'y ajoutent la conversion entre analogique et numérique aux frontières du bloc, qui consomme et peut annuler le gain ; l'endurance en écriture des cellules ; et l'absence d'écosystème de conception.

**Ce que cela implique.** L'approche convient aux calculs **tolérants à une précision modeste** — ce qui inclut une partie des traitements d'apprentissage, où une précision réduite dégrade peu les résultats. Elle ne convient pas au calcul exact.

**À ne pas confondre avec.** **Le cache**, qui rapproche la donnée sans changer le lieu du calcul. **Le neuromorphique**, qui partage la colocalisation mais s'en distingue par le mode de communication.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Démonstrateurs et premiers composants commerciaux sur des niches ; adoption générale limitée par la précision et l'écosystème.
> 🔄 **À revoir si** un composant de calcul en mémoire atteint une précision suffisante pour une charge d'inférence courante, avec des performances reproductibles d'un exemplaire à l'autre.

**Renvois** — Couche : calculer · Convergences : énergie et calcul (40), intelligence distribuée (38) · Voir aussi : calcul analogique (ch. 9).

---
