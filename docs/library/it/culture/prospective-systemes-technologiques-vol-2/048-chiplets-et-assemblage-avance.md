---
title: ◆◆◆ Chiplets et assemblage avancé
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — procédé · **Couche** — calculer

**En une phrase.** Construire un composant en assemblant plusieurs petites puces plutôt qu'en fabriquant une seule grande.

**Pourquoi on en parle.** Parce que c'est devenu **le principal levier de performance** de la microélectronique, davantage que la réduction des dimensions — et parce que ce déplacement est mal connu hors du secteur.

**Comment ça fonctionne.** La raison est économique avant d'être technique. Des défauts microscopiques se répartissent au hasard sur une plaquette ; plus une puce est grande, plus elle a de chances d'en contenir un, et la proportion de puces conformes s'effondre. Doubler la surface ne double pas le coût : il peut le tripler.

**La solution consiste à découper la fonction.** On fabrique plusieurs puces plus petites — chacune avec un bon rendement, chacune éventuellement dans le procédé le mieux adapté à sa fonction — et on les assemble sur un support commun avec des liaisons très courtes et très nombreuses. On peut aussi les empiler, ce qui réduit encore les distances.

**Où vous rencontrerez le terme.** Processeurs et accélérateurs · mémoires · équipements réseau · progressivement dans l'embarqué.

**Ce que ça permet.** Contourner la limite de taille imposée par le rendement · combiner des procédés de générations différentes selon les besoins de chaque bloc · rapprocher la mémoire du calcul, ce qui attaque directement le mur de la couche.

**Ce qui bloque.** **Le test.** Il faut vérifier chaque puce avant assemblage, car une seule défectueuse ruine l'ensemble — et certains défauts n'apparaissent qu'après assemblage. **La thermique** : empiler des sources de chaleur réduit la surface d'évacuation par unité de puissance, ce qui est le carré-cube appliqué à la puce. **L'interopérabilité** : assembler des puces d'origines différentes suppose des interfaces normalisées, et cette normalisation est récente et incomplète.

**De quoi ça dépend.** Équipements d'assemblage de précision · substrats et interposeurs · matériaux d'interconnexion · métrologie · normes d'interface.

**Ce que cela implique.** Le goulet s'est **déplacé de la fabrication vers l'assemblage**, qui a sa propre concentration industrielle et ses propres délais. C'est un cas d'école du mécanisme du volume 1 : résoudre une contrainte ne la supprime pas, il la déplace — et le nouveau goulet n'est pas là où l'attention se portait.

**À ne pas confondre avec.** **Le multi-puce classique**, qui plaçait plusieurs composants indépendants dans un boîtier sans liaison à haute densité. Ici, l'assemblage fait partie de la conception du composant.

**Termes voisins.** *Packaging avancé*, *intégration 2.5D et 3D*, *collage hybride* désignent des techniques d'un même mouvement.

> ⏱ **État au 23/08/2026** — 🏭 déployé et en généralisation. Capacité d'assemblage avancé identifiée comme facteur limitant chez plusieurs acteurs ; normalisation des interfaces entre puces en cours.
> 🔄 **À revoir si** une norme d'interface entre puces d'origines différentes devient assez répandue pour qu'un marché de composants assemblables apparaisse.

**Renvois** — Couche : calculer · Convergence : énergie et calcul (40).

---
