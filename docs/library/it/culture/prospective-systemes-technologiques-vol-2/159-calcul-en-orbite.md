---
title: ◆◆ Calcul en orbite
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — infrastructure spatiale, calculer

**En une phrase.** Traiter les données à bord d'un satellite plutôt que de les descendre au sol.

**Pourquoi on en parle.** Parce que c'est la réponse directe au goulet du segment sol : **descendre un résultat coûte infiniment moins que descendre une donnée brute**.

**Ce que ça permet.** Réduire le volume transmis d'un ou deux ordres de grandeur · réduire le délai entre l'observation et l'information — une détection faite à bord peut être signalée immédiatement · filtrer, ne descendre que ce qui est pertinent — par exemple ignorer les images entièrement nuageuses.

**Ce qui bloque.** **L'énergie et la dissipation.** Un satellite dispose d'une puissance limitée par sa surface de panneaux, et **il ne peut évacuer sa chaleur que par rayonnement** — la convection n'existe pas dans le vide. La contrainte thermique est donc bien plus sévère qu'au sol pour une même puissance de calcul.

**Le rayonnement**, qui perturbe l'électronique et impose soit des composants durcis — moins performants et d'une génération plus ancienne — soit des architectures tolérantes aux erreurs.

**La mise à jour** : modifier un traitement à bord suppose une liaison de commande et une procédure sûre, sur un objet qu'on ne peut pas récupérer en cas d'échec.

**Ce que cela implique.** C'est un cas où **les contraintes de la couche *calculer* deviennent extrêmes** : l'énergie, la dissipation et la fiabilité y priment sur la performance. Les traitements embarqués sont donc simples et spécialisés — ce qui rejoint la logique des modèles compacts.

**À ne pas confondre avec.** L'idée d'installer des centres de données en orbite pour bénéficier du froid spatial — proposition qui ignore que **le vide est un excellent isolant**, et que l'évacuation thermique y est plus difficile qu'au sol, pas plus facile.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Traitements embarqués opérationnels sur des missions d'observation, généralisation progressive.
> 🔄 **À revoir si** un satellite d'observation descend majoritairement des informations traitées plutôt que des images brutes.

**Renvois** — Couche : infrastructure spatiale, calculer.

---
