---
title: ◆◆ Imagerie computationnelle
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — percevoir, calculer

**En une phrase.** Concevoir conjointement l'optique et l'algorithme, de sorte que l'image finale soit reconstruite plutôt que directement captée.

**Pourquoi on en parle.** Parce qu'elle déplace une partie du coût de l'optique vers le calcul — ce qui, dans un monde où le calcul est bon marché et l'optique chère, change les architectures possibles.

**Comment ça fonctionne.** Plutôt que de former une image nette sur le détecteur, on capte une mesure volontairement encodée — par une ouverture codée, un masque, plusieurs prises de vue légèrement différentes — puis on reconstruit l'image par calcul. Le capteur ne mesure plus l'image : il mesure de quoi la reconstruire.

**Où vous rencontrerez le terme.** Photographie mobile · microscopie · imagerie médicale · observation spatiale · capteurs compacts.

**Ce que ça permet.** Réduire l'encombrement optique · dépasser certaines limites de profondeur de champ ou de dynamique · reconstruire une information de distance à partir de plusieurs prises.

**Ce qui bloque.** **La reconstruction est une inférence.** Ce qui est produit dépend d'hypothèses sur la scène ; quand ces hypothèses ne tiennent pas, l'algorithme produit une image plausible et fausse, sans le signaler. S'y ajoute le coût en calcul, qui déplace la contrainte vers l'énergie du dispositif.

**Ce que cela implique.** **La distinction entre mesure et inférence devient opérationnelle.** Dans une chaîne computationnelle, une partie de ce que vous voyez a été acquise et une partie a été reconstruite. Pour un usage esthétique, la distinction importe peu ; pour une mesure, une preuve ou une décision automatique, elle est décisive.

**À ne pas confondre avec.** **Le post-traitement d'image**, qui améliore une image déjà formée. Ici, l'optique elle-même est conçue pour ne pas former d'image.

> ⏱ **État au 23/08/2026** — 🏭 déployé en photographie grand public, 🔬 émergent en instrumentation.
> 🔄 **À revoir si** une exigence réglementaire ou probatoire impose de distinguer, dans une image, ce qui est mesuré de ce qui est reconstruit.

**Renvois** — Couche : percevoir, calculer · Convergence : intelligence distribuée (38).

---


## ◆ Intensification d'image

**Niveau** — composant · **Couche** — percevoir

**En une phrase.** Amplifier la lumière résiduelle d'une scène nocturne pour la rendre visible.

**Où vous rencontrerez le terme.** Vision nocturne · sécurité · applications de défense · astronomie amateur.

**Ce qui bloque.** **Il faut qu'il reste de la lumière.** Un intensificateur ne crée rien : il amplifie des photons existants. Dans l'obscurité totale, il ne voit rien — contrairement à un imageur thermique.

**À ne pas confondre avec.** **L'imagerie thermique.** C'est la confusion la plus fréquente du chapitre : les deux sont appelés « vision nocturne » et reposent sur des principes opposés. L'un amplifie la lumière réfléchie, l'autre capte l'émission propre des objets. L'un est aveuglé par une source vive, l'autre non ; l'un ne voit rien sans lumière, l'autre voit un corps chaud dans le noir absolu.

> ⏱ **État au 23/08/2026** — 🏭 déployé, technologie mature. Progressivement concurrencée par les capteurs à très faible bruit en bandes visible et proche infrarouge.
> 🔄 **À revoir si** des capteurs numériques à faible bruit atteignent des performances équivalentes à un coût et une consommation comparables.

**Renvois** — Couche : percevoir.

---
