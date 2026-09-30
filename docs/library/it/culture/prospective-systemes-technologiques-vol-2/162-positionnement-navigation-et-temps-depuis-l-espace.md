---
title: ◆◆ Positionnement, navigation et temps depuis l'espace
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — infrastructure · **Couche** — infrastructure spatiale, percevoir

**En une phrase.** L'infrastructure spatiale qui fournit position et référence temporelle à une grande partie du monde technologique.

**Pourquoi cette entrée figure ici alors que le récepteur est traité au chapitre 6.** Parce que ce sont deux objets différents : le chapitre 6 traite du **capteur** et de son usage ; celui-ci traite de **l'infrastructure** et de ce qui la conditionne.

**Ce que le segment spatial exige.** Des **horloges d'une stabilité extrême** à bord — la précision de position découle directement de la précision de temps. Une **maîtrise fine des orbites**, puisque la position des satellites est le référentiel. Un **segment sol** qui surveille et corrige en permanence. Et un **renouvellement continu**, la durée de vie des satellites étant limitée.

**Ce qui bloque.** **Le coût de maintien**, qui est permanent et supporté par des États. **La puissance émise**, limitée, d'où un signal reçu très faible. Et **l'authentification** : les signaux civils historiques ne comportent pas de mécanisme permettant de vérifier leur origine — des services authentifiés existent désormais, mais **le parc de récepteurs déployés ne les exploite pas**.

**Ce que cela implique — et c'est le point du volume.** Une dépendance mondiale s'est constituée sans qu'aucun acteur ne la décide : chaque système a adopté la source de temps la moins coûteuse disponible, et l'agrégation de ces choix individuellement rationnels a produit une infrastructure critique. **C'est le cas d'école du chapitre 45**, et le volume 1 l'avait identifié comme un angle mort de sa propre méthode.

**À ne pas confondre avec.** Les systèmes d'**augmentation**, qui améliorent la précision par des corrections transmises séparément et ne changent rien à la dépendance de fond.

> ⏱ **État au 23/08/2026** — 🏭 déployé, infrastructure critique. Plusieurs constellations opérationnelles ; services authentifiés disponibles ; adoption par le parc de récepteurs très partielle.
> 🔄 **À revoir si** une part significative des récepteurs d'infrastructures critiques bascule sur des signaux authentifiés.

**Renvois** — Couche : infrastructure spatiale · Voir aussi : GNSS et positionnement par satellite (ch. 6), navigation sans référence satellitaire (ch. 6), chapitre 45.

---


## Clôture des couches G et G-bis


### Ce que les vingt-deux entrées font apparaître

**Un. Le spatial est devenu une industrie de série, et c'est le fait majeur de ces deux couches.** Lanceurs réutilisés, satellites produits en série, constellations renouvelées en permanence : **le régime de production a changé**, et c'est ce que le volume 1 avait identifié comme la condition manquante de cette filière. C'est le seul cas de l'atlas où l'on observe un changement de régime en cours, et non achevé ou hypothétique.

**Deux. La contrainte de descente de données déplace le calcul vers l'orbite.** Segment sol saturé, volumes croissants, fenêtres de visibilité courtes : la réponse est de traiter à bord. **La couche *relier* pousse ainsi la couche *calculer* dans un environnement où ses contraintes sont extrêmes** — énergie limitée, évacuation thermique par rayonnement seul, rayonnement ionisant.

**Trois. Deux entrées de ces couches décrivent des contraintes de ressource commune** — congestion orbitale et attribution du spectre. Aucune n'a d'autorité de gestion contraignante, et les deux se dégradent par agrégation de décisions individuellement rationnelles. **C'est le mécanisme du chapitre 45, observé sur des biens physiques.**

**Quatre. Trois entrées alimentent directement le chapitre 45** : positionnement et temps, congestion orbitale, et le GNSS du chapitre 6. **Le spatial fournit à lui seul la majorité des cas de dépendances non décidées de tout l'atlas** — ce qui justifie rétrospectivement de lui avoir donné sa propre couche.


### Ce que les couches livrent aux convergences

| Dossier | Entrées mobilisées |
|---|---|
| **38 — Intelligence distribuée** | edge/on-device/embarqué, continuum, réseaux non terrestres, calcul en orbite |
| **39 — Autonomie mobile** | edge/on-device/embarqué, réseaux non terrestres, communications dégradées, PNT |
| **40 — Énergie et calcul** | edge/on-device/embarqué, continuum |

---

---

---


### Couche H — Vérifier

---
