---
title: Chapitre 9 — Calculer autrement
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - ../index.md
- - Partie I — Lire une frontière technologique
  - index.md
---

> **Ce que ce chapitre ajoute.** Le chapitre 8 optimisait à l'intérieur du paradigme électronique numérique. Celui-ci en sort — par le support, par la représentation, ou par le mode de communication.
>
> **Une observation commune aux six entrées.** Aucune ne bute principalement sur la physique. **Toutes butent sur l'écosystème** : outils de conception, compilateurs, bibliothèques, méthodes de test, personnes formées, base installée. C'est le mécanisme le plus important de ce chapitre, et il commande la lecture de chaque fiche.

---

## ◆◆◆ Photonique intégrée

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

## ◆◆◆ Neuromorphique

**Niveau** — famille · **Couche** — calculer

**En une phrase.** Des architectures inspirées de l'organisation du système nerveux : calcul et mémoire colocalisés, communication par impulsions brèves, activité déclenchée par l'événement plutôt que par une horloge.

**Pourquoi on en parle.** Parce que le terme est employé pour des objets très différents, et parce que l'approche attaque simultanément les deux contraintes de la couche : le déplacement des données et l'énergie.

**Comment ça fonctionne.** Trois principes, qui peuvent être adoptés séparément — d'où la confusion.

**La colocalisation** : chaque unité de calcul possède sa propre mémoire locale, supprimant les transferts longue distance.

**La communication par impulsions** : les unités n'échangent pas des valeurs continues mais des impulsions brèves, dont l'information réside dans l'instant d'émission. Une unité qui n'a rien à dire ne consomme rien.

**Le fonctionnement événementiel** : il n'y a pas d'horloge globale ; l'activité se déclenche à l'arrivée d'un événement. Sur des données naturellement éparses, la consommation chute d'un ou deux ordres de grandeur.

**Ce que ça permet.** Un traitement continu à très faible consommation, particulièrement adapté aux flux d'événements — reconnaissance de motifs sur signaux, traitement de sorties de caméras événementielles, surveillance permanente sur alimentation contrainte.

**Ce qui bloque.** **L'entraînement.** Les méthodes qui ont fait le succès de l'apprentissage profond supposent des grandeurs continues et différentiables ; les impulsions ne le sont pas. On contourne par conversion depuis un réseau classique, au prix d'une partie du gain, ou par des méthodes spécifiques encore moins matures.

S'y ajoute **l'absence complète d'écosystème** : outils, formats, jeux de données, métriques et compétences ont tous été construits pour le paradigme dominant.

**Ce que cela implique.** C'est l'entrée qui illustre le mieux l'observation d'ouverture du chapitre : **le verrou n'est pas physique, il est écosystémique.** Les composants existent et fonctionnent ; ce qui manque est tout ce qui permettrait de les utiliser sans être spécialiste.

**À ne pas confondre avec.** **Les réseaux de neurones artificiels courants**, qui s'exécutent sur du matériel conventionnel et n'ont d'inspiration biologique que le nom. **Le calcul analogique**, avec lequel le neuromorphique se combine souvent sans se confondre.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Puces disponibles auprès de plusieurs acteurs, applications de niche établies en traitement de signal à très faible consommation, adoption générale absente.
> 🔄 **À revoir si** une méthode d'entraînement native atteint des performances comparables au paradigme dominant sur une tâche de référence reconnue.

**Renvois** — Couche : calculer · Convergence : intelligence distribuée (38) · Voir aussi : caméras événementielles (ch. 6).

---

## ◆◆ Calcul analogique

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
