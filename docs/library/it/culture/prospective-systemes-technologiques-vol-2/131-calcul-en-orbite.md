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


## ◆◆ Services en orbite

**Niveau** — capacité · **Couche** — infrastructure spatiale

**En une phrase.** Intervenir sur un objet en orbite — le ravitailler, le réparer, le déplacer, le désorbiter, ou l'assembler.

**Pourquoi on en parle.** Parce que cela remet en cause **la contrainte la plus structurante du spatial : on ne répare pas**.

**Ce que cela changerait.** Prolonger la vie d'un satellite dont les fonctions marchent mais dont l'ergol est épuisé · corriger une anomalie de déploiement · déplacer un objet vers une orbite plus utile · **désorbiter un débris**, ce qui relie directement cette entrée à la suivante · assembler en orbite des structures trop grandes pour être lancées d'un seul tenant.

**Ce qui bloque.** **Le rendez-vous et l'amarrage** avec un objet non coopératif — non conçu pour être saisi, éventuellement en rotation. C'est une difficulté de manipulation au sens de la couche *agir*, dans un environnement sans reprise possible.

**Le modèle économique** : le coût d'une mission de service doit rester inférieur à celui du remplacement du satellite, ce qui est difficile quand le coût de lancement baisse.

**Le cadre juridique** : approcher un objet appartenant à un tiers pose des questions de responsabilité et de sécurité que le droit spatial existant traite mal.

**Ce que cela implique.** Les services les plus crédibles à court terme sont ceux où **le client est le propriétaire de l'objet** — prolongation de vie, désorbitation en fin de mission. L'intervention sur objet tiers est bien plus contrainte, juridiquement autant que techniquement.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Démonstrations de prolongation de vie et de rendez-vous réalisées ; désorbitation active en développement ; assemblage en orbite au stade des démonstrations.
> 🔄 **À revoir si** une mission de désorbitation active d'un débris non coopératif est réalisée avec succès.

**Renvois** — Couche : infrastructure spatiale · Voir aussi : manipulation (ch. 14), débris (ch. 27).

---
