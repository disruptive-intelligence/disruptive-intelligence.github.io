---
title: ◆◆◆ Photonique intégrée
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — composant · **Couche** — calculer, relier

**En une phrase.** Réaliser sur une puce des fonctions optiques — guider, moduler, détecter la lumière — en utilisant les procédés de la microélectronique.

**Pourquoi on en parle.** Parce qu'elle attaque le coût du déplacement des données à courte distance, et parce qu'elle est passée récemment du laboratoire à la production en volume.

**Comment ça fonctionne.** On grave dans le silicium des guides d'onde qui conduisent la lumière comme des pistes conduisent le courant. On y ajoute des modulateurs, des multiplexeurs et des détecteurs. Le silicium n'émettant pas efficacement de lumière, la source laser est généralement rapportée — c'est l'une des difficultés d'intégration du domaine.

**L'intérêt vient de trois propriétés.** La lumière ne dissipe pas dans le guide comme un courant dans un conducteur. Plusieurs longueurs d'onde peuvent coexister dans le même guide, multipliant la capacité. Et la consommation d'une liaison optique dépend peu de la distance, contrairement à une liaison électrique.

**Où vous rencontrerez le terme.** Centres de calcul · liaisons entre puces · capteurs · télécommunications · instrumentation.

**Ce que ça permet.** Remplacer des liaisons électriques par des liaisons optiques **à l'intérieur des équipements**, là où la densité et la consommation deviennent limitantes — ce qui est un déplacement récent, l'optique ayant longtemps été réservée aux longues distances.

**Ce qui bloque.** **Le seuil de conversion.** Passer de l'électronique à l'optique et revenir coûte de l'énergie et du temps. En dessous d'une certaine distance et d'un certain débit, ce coût dépasse le gain du transport optique. **C'est ce seuil qui détermine où la photonique gagne**, et il se déplace à mesure que les composants s'améliorent — c'est la grandeur à surveiller.

S'y ajoutent l'intégration de la source laser, la sensibilité en température, et l'alignement optique, qui exige des précisions submicrométriques en assemblage.

**Ce que cela implique.** La photonique **n'est pas une alternative au calcul électronique** : c'est une technologie d'interconnexion qui repousse un mur. Elle gagne progressivement du terrain vers l'intérieur des systèmes, et sa progression se mesure par une distance décroissante — celle en dessous de laquelle l'électrique reste préférable.

**À ne pas confondre avec.** **Le calcul photonique**, traité séparément : effectuer l'opération dans le domaine optique est un problème entièrement différent de transporter l'information optiquement.

**Termes voisins.** *Silicon photonics* · *optique co-packagée* désigne l'intégration au plus près du processeur.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour les liaisons de centre de calcul, 🔬 émergent pour l'intégration au plus près du processeur, en industrialisation rapide.
> 🔄 **À revoir si** l'optique co-packagée devient l'architecture par défaut des accélérateurs de grande taille.

**Renvois** — Couche : calculer, relier · Convergence : énergie et calcul (40).

---


## ◆◆ Calcul photonique

**Niveau** — capacité · **Couche** — calculer

**En une phrase.** Effectuer l'opération elle-même dans le domaine optique, plutôt que de convertir en électronique pour calculer.

**Comment ça fonctionne.** Certaines opérations se prêtent naturellement à une réalisation optique. Faire passer un faisceau à travers un réseau d'éléments qui l'atténuent et le recombinent réalise, physiquement, une multiplication matricielle — à la vitesse de la lumière et sans consommation liée à l'opération elle-même.

**Ce que ça permet.** Un débit d'opérations très élevé sur des calculs réguliers, avec une consommation potentiellement très inférieure.

**Ce qui bloque.** **Les mêmes trois obstacles que le calcul analogique**, dont il est une variante physique : la **précision** est limitée et sensible aux conditions ; la **conversion** aux entrées et sorties consomme et peut annuler le gain ; et il n'existe **aucune mémoire optique** pratique, ce qui oblige à revenir dans le domaine électronique entre les étapes.

Ce dernier point est décisif : le calcul photonique excelle sur une opération isolée et perd son avantage dès qu'il faut chaîner.

**Ce que cela implique.** L'approche vise des niches où le motif de calcul est fixe, régulier et tolérant à l'imprécision. Elle ne vise pas le remplacement d'un processeur.

**À ne pas confondre avec.** **La photonique intégrée**, qui transporte. La confusion est fréquente et coûteuse : la première est déployée, le second est prospectif.

> ⏱ **État au 23/08/2026** — 🔭 prospectif, avec des démonstrateurs et quelques produits de niche.
> 🔄 **À revoir si** un système photonique démontre un avantage net sur une charge complète — et non sur une opération isolée — conversions comprises.

**Renvois** — Couche : calculer · Convergence : énergie et calcul (40).

---
