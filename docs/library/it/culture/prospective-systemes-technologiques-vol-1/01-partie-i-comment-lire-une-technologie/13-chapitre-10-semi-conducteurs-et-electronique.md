---
title: Chapitre 10 — Semi-conducteurs et électronique
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
up:
- - Prospective — systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

> **🎯 Pour lire ce chapitre**
>
> **À retenir :**
> * le rendement de fabrication gouverne brutalement le coût, et il dépend de la surface de la puce ;
> * l'industrie est capitalistique à l'extrême et dépend d'une chaîne très spécialisée.
>
> **À reconnaître :** transistor · plaquette · lithographie · assemblage avancé · rendement (*yield*)
>
> **Le reste se consulte.** Les mécanismes de détail, les chiffres et les variantes ne sont pas à mémoriser : ils sont là pour que vous puissiez y revenir.

Ce chapitre traite du substrat physique de tout ce qui précède. Il a une particularité : c'est celui où l'économie et la physique sont les plus étroitement liées, et où un paramètre invisible dans toute documentation technique décide de qui gagne.

## 10.1 Pourquoi cette famille existe : un interrupteur sans pièce mobile

Le problème est ancien : construire un interrupteur commandé électriquement, sans pièce mécanique, capable de commuter très vite, très souvent, en consommant très peu, et fabricable par millions au même endroit.

Un **semi-conducteur** est un matériau intermédiaire entre isolant et conducteur, dont la conductivité peut être modifiée. En introduisant volontairement des impuretés — le dopage — et en disposant plusieurs régions ainsi traitées, on obtient un dispositif où **une tension appliquée sur une électrode de commande contrôle le passage du courant entre deux autres**. C'est le transistor.

Trois propriétés font tout le reste :

* il n'a aucune pièce mobile, donc aucune usure mécanique ;
* il commute en une fraction de nanoseconde ;
* il peut être fabriqué collectivement, par milliards, sur une même plaque de matériau.

**La troisième est la véritable rupture.** Ce n'est pas le transistor qui a changé le monde : c'est le fait qu'on ait su en fabriquer des milliards d'un coup, à un coût qui décroît avec le volume. Le chapitre 22 vous a donné le nom de ce mécanisme.

## 10.2 De l'interrupteur à la logique et à la mémoire

En combinant quelques transistors, on obtient des fonctions logiques élémentaires — des dispositifs dont la sortie dépend des entrées selon une règle fixe. En combinant ces fonctions, on obtient des opérations arithmétiques ; en les combinant encore, un processeur.

**Le stockage suit la même logique.** Un circuit qui se maintient dans l'état où on l'a placé mémorise un bit. Selon la façon dont on le construit, on obtient des mémoires rapides et coûteuses en surface, ou lentes et denses, ou capables de conserver l'information sans alimentation. Aucune ne réunit ces qualités : c'est ce qui impose la hiérarchie du chapitre 9.

**Point à retenir.** Toute la complexité du calcul est construite à partir d'un unique dispositif répété. Cette uniformité est ce qui a permis l'échelle — et c'est aussi ce qui rend l'industrie si concentrée, comme la suite va le montrer.

## 10.3 Fabriquer : une accumulation d'étapes

La fabrication procède par **empilement de couches**. On part d'une plaque de silicium ultrapur — la *plaquette*, aujourd'hui de 300 mm de diamètre — et l'on répète un cycle : déposer un matériau, appliquer un produit photosensible, l'exposer à travers un masque qui projette un motif, développer, graver, nettoyer. Chaque cycle construit une couche du circuit.

**Les ordres de grandeur qui comptent :**

| Grandeur | Ordre de grandeur |
|---|---|
| Nombre d'étapes pour un nœud avancé | 1 000 à 2 000 |
| Durée de traversée d'une plaquette | environ 12 à 20 semaines |
| Coût d'une plaquette finie, nœud avancé | de l'ordre de 20 000 à 30 000 $ |
| Coût d'un jeu de masques, nœud avancé | de l'ordre de 10 à 15 M$ |
| Coût d'une usine de pointe | de l'ordre de 15 à 30 Md$ |
| Coût d'un équipement de lithographie extrême | de l'ordre de 200 à 400 M$ |

⏱ *Valeurs 2025-2026, à réactualiser. Voir Annexe I.*

**La lithographie est l'étape critique.** C'est elle qui fixe la finesse des motifs, elle qui coûte le plus cher, et elle qui constitue le point de concentration extrême de toute la chaîne : les équipements les plus avancés proviennent d'un fournisseur unique au monde. Le chapitre 25 vous a donné le cadre pour analyser cette situation ; vous en tenez ici l'exemple le plus net.

**Conséquence économique immédiate.** Une usine à 20 milliards de dollars, amortie sur quelques années, doit tourner en permanence et à pleine charge. Elle appartient à la catégorie décrite au chapitre 22 : économie entièrement dominée par le capital, où le volume n'est pas un avantage mais une condition de survie. Le nombre d'acteurs capables de financer une usine de pointe s'est réduit à un très petit nombre, et ce n'est pas un accident de marché : c'est la conséquence directe de cette structure de coûts.

## 10.4 Le rendement : le paramètre qui décide

🖼 **SCHÉMA — Rendement en fonction de la surface de puce.** Courbe décroissante, surface en abscisse de 0,25 à 4 cm², rendement en ordonnée. Marquer la zone d'effondrement au-delà de 1 cm². Légende : « modèle simple à un défaut par cm² — la réalité est adoucie par le regroupement des défauts et la redondance ».



Voici le point le plus important du chapitre.

Une plaquette produit un certain nombre de puces. Toutes ne fonctionnent pas : des défauts microscopiques — une poussière, une irrégularité, une variation de procédé — rendent certaines puces inutilisables. La proportion de puces conformes est le **rendement**, et il gouverne l'économie entière, comme le chapitre 24 l'a montré en général.

**Ce que le chapitre 24 n'a pas montré, et qui est spécifique ici : le rendement dépend violemment de la taille de la puce.**

Prenons un modèle simple — et rappelons qu'il s'agit d'un modèle pédagogique, la réalité industrielle comportant des regroupements de défauts et des mécanismes de redondance qui l'adoucissent. Supposons les défauts répartis au hasard sur la plaquette, à raison d'un défaut par centimètre carré en moyenne. Une puce est bonne si elle ne contient aucun défaut.

| Surface de la puce | Puces bonnes (modèle simple) |
|---|---|
| 0,25 cm² | environ 78 % |
| 0,5 cm² | environ 61 % |
| 1 cm² | environ 37 % |
| 2 cm² | environ 14 % |
| 4 cm² | environ 2 % |

Multiplier la surface par huit fait passer le rendement de 61 % à moins de 2 %. **La pénalité n'est pas proportionnelle : elle est brutale.**

**Trois conséquences majeures découlent de ce seul tableau.**

**Premièrement, la taille des puces est bornée par l'économie, pas par la conception.** On sait dessiner une très grande puce ; on ne sait pas la produire à un coût acceptable.

**Deuxièmement, cela explique le mouvement vers les architectures assemblées.** Plutôt qu'une grande puce unique, on en fabrique plusieurs petites — chacune avec un bon rendement — et on les assemble. C'est l'objet de la section suivante, et vous comprenez maintenant que ce n'est pas une élégance de conception : c'est une réponse à une contrainte de rendement.

**Troisièmement, cela relie ce chapitre au chapitre 22.** Le rendement s'améliore avec l'expérience de production, et cette amélioration est l'un des principaux moteurs de la baisse de coût. La courbe d'apprentissage des semi-conducteurs est, pour une bonne part, une courbe de rendement.

**La question à poser désormais, devant toute annonce sur une puce :** *quelle surface, et quel rendement en production ?* Elle est presque toujours sans réponse publique, et c'est en soi une information.

## 10.5 Ce que « nœud » veut dire, et ne veut pas dire

Les procédés de fabrication sont désignés par des noms qui ressemblent à des dimensions : « 7 nm », « 3 nm », « 2 nm ». Il faut savoir ce que ces désignations recouvrent réellement.

**Ce qu'elles ne sont pas.** Elles ne correspondent plus, depuis longtemps, à une dimension physique mesurable du transistor. Aucune longueur du dispositif ne mesure deux nanomètres dans un procédé dit « 2 nm ». Ce sont des **noms commerciaux de générations technologiques**, et deux fabricants employant la même désignation ne produisent pas nécessairement des transistors de dimensions comparables.

**Ce qu'elles indiquent réellement.** Une génération de procédé, censée offrir un gain combiné en densité, en performance et en consommation par rapport à la précédente.

**Pourquoi c'est important pour vous.** C'est un cas d'école de la vigilance du chapitre 6 : un chiffre précis, d'apparence physique, qui est en réalité une désignation commerciale. Comparer deux procédés par leur nom de nœud est une erreur de méthode. **Les grandeurs comparables sont la densité de transistors effective, la performance à consommation donnée, et le coût par fonction.**

🗣 *En réunion : « ils sont en 3 nm » n'est pas une information technique. La question utile est : quelle densité, à quelle consommation, à quel coût par puce fonctionnelle ?*

## 10.6 Packaging et assemblage : quand l'emballage redevient central

Pendant des décennies, l'assemblage du circuit dans son boîtier était une étape peu valorisée. Elle est redevenue stratégique, pour la raison exposée en 10.4.

**Le principe.** Plutôt qu'une puce unique de grande surface, on fabrique plusieurs puces plus petites, chacune éventuellement dans le procédé le mieux adapté à sa fonction, et on les assemble dans un même boîtier avec des liaisons très courtes et très nombreuses. On peut aussi les empiler, ce qui raccourcit encore les distances.

**Trois bénéfices, tous déjà rencontrés dans ce volume :**

* **le rendement**, puisque de petites puces ont un bien meilleur taux de réussite ;
* **le coût**, puisque seules les fonctions qui l'exigent utilisent le procédé le plus cher ;
* **la distance**, puisque rapprocher la mémoire du calcul attaque directement le mur du chapitre 9.

> **Résout / coûte.** L'assemblage avancé : *résout* le rendement, le coût et la distance mémoire · *coûte* une complexité d'assemblage nouvelle, un test plus difficile — une puce défectueuse peut ruiner un assemblage entier —, une contrainte thermique aggravée par l'empilement, et une nouvelle étape critique dans la chaîne d'approvisionnement.

Ce dernier point mérite attention : en déplaçant la difficulté de la fabrication vers l'assemblage, l'industrie a créé un nouveau goulet, avec sa propre concentration industrielle. C'est le mécanisme du chapitre 32, observé en direct.

## 10.7 Consommation et densité de puissance

Le chapitre 8 a établi que tout finit en chaleur et que l'évacuation est limitée par la surface. Voici ce que cela donne ici.

**Deux sources de consommation.** L'énergie dépensée à chaque commutation, proportionnelle au nombre de commutations et fortement dépendante de la tension d'alimentation ; et les fuites, consommées en permanence, y compris quand rien ne se passe. La part des fuites augmente à mesure que les dimensions diminuent.

**Le point de bascule historique.** Pendant longtemps, réduire les dimensions permettait de réduire la tension dans les mêmes proportions, si bien que la puissance par unité de surface restait à peu près constante. Cette réduction conjointe s'est arrêtée : les tensions ne pouvaient plus descendre autant, alors que la densité de transistors continuait d'augmenter. **La densité de puissance a donc commencé à croître**, et c'est ce qui a mis fin à l'augmentation des fréquences d'horloge.

**Conséquence toujours actuelle.** Une puce moderne ne peut pas faire fonctionner tous ses circuits à pleine vitesse simultanément : cela dépasserait sa capacité d'évacuation thermique. On répartit donc l'activité, on spécialise des blocs, on en éteint d'autres. **La contrainte de conception n'est plus le nombre de transistors disponibles, mais l'énergie qu'on peut dissiper.**

C'est la deuxième fois dans ce chapitre qu'une contrainte physique du chapitre 8 se traduit en choix d'architecture. Ce sera aussi le cas au chapitre 13, à l'échelle du bâtiment.

## 10.8 Les mémoires : trois familles, trois compromis

| Famille | Rapidité | Densité | Conserve sans alimentation | Usage typique |
|---|---|---|---|---|
| Mémoire intégrée rapide | très élevée | faible | non | caches, registres |
| Mémoire dynamique | moyenne | élevée | non | mémoire principale |
| Mémoire non volatile | plus lente en écriture | très élevée | oui | stockage |

Aucune famille ne domine les autres sur les trois critères, et c'est ce qui impose la hiérarchie. La recherche de mémoires combinant densité, rapidité et non-volatilité est ancienne et constitue l'un des sujets sérieux du Volume 2 — mais aucune n'a encore délogé les trois familles établies, pour des raisons qui relèvent autant du chapitre 27 que de la physique.

**Point de vigilance.** Une mémoire non volatile s'use : le nombre de cycles d'écriture qu'elle supporte est fini. C'est une durée de vie exprimée en cycles, exactement comme la fatigue du chapitre 8.

## 10.9 L'électronique de puissance

Souvent ignorée, elle conditionne l'électrification de tout ce qui bouge.

**Le problème.** Convertir de l'électricité d'une forme à une autre — changer la tension, passer du continu à l'alternatif, régler la vitesse d'un moteur — avec le moins de pertes possible.

**Le principe.** Plutôt que de dissiper l'excédent, on commute très rapidement entre deux états — passant et bloqué — et on lisse le résultat. Un interrupteur idéal ne dissipe rien : ni quand il est fermé, ni quand il est ouvert. Toute la perte se produit **pendant la commutation**, et pendant les phases où le composant n'est ni tout à fait passant ni tout à fait bloqué.

**D'où la course.** On cherche des composants qui commutent plus vite, supportent des tensions plus élevées et résistent à des températures plus hautes. Des matériaux semi-conducteurs autres que le silicium permettent d'aller plus loin sur ces trois axes ; le Volume 2 traitera de leur trajectoire industrielle.

**Pourquoi cela compte.** Chaque point de rendement gagné sur ces convertisseurs se répercute sur tout ce qui est électrifié : véhicules, réseaux, alimentations de centres de calcul, machines industrielles. Le chapitre 8 vous l'a montré — dans une chaîne, les rendements se multiplient. L'électronique de puissance est présente dans presque toutes ces chaînes.

## 10.10 Ce que cela implique

**Le passage à l'échelle.** L'industrie du semi-conducteur est celle où l'échelle a le plus radicalement changé la nature du problème. Le procédé initial était accessible à une équipe de laboratoire ; il exige aujourd'hui un investissement de plusieurs dizaines de milliards, une chaîne d'équipements dont certains n'ont qu'un fournisseur mondial, et une production continue à très haut volume pour être viable. **Le chapitre 31 dira que changer d'échelle peut changer la nature du problème ; ceci en est l'illustration la plus complète du volume.**

**Les dépendances.** Cette famille dépend de la chimie de haute pureté, de l'optique de précision, de la mécanique de très haute stabilité, de l'eau ultrapure en grande quantité et d'une alimentation électrique irréprochable. Et presque tout le reste du monde technologique dépend d'elle.

**Implication cyber.** Trois éléments, tous prolongés au Volume 2 : la confiance dans un composant qu'on n'a pas fabriqué et qu'on ne peut pas inspecter sans le détruire ; l'existence de fonctions de sécurité ancrées dans le matériel, dont la solidité repose sur l'intégrité du procédé de fabrication ; et la concentration géographique de la production, qui fait d'une chaîne technique un enjeu de dépendance au sens du chapitre 25.

**Cas de panne.** Une variation de procédé minime, non détectée, produit un lot de composants qui passent les tests initiaux et défaillent après plusieurs mois d'utilisation, sous contrainte thermique. Le défaut n'est pas dans la conception, il n'est pas reproductible en laboratoire, et il touche une population dispersée chez des clients finaux. C'est la conjonction du chapitre 8 — la matière n'est pas idéale — et du chapitre 24 — le coût de la non-qualité croît avec le moment de la détection.

🎓 **À ce stade, vous savez…**

* expliquer pourquoi un transistor commute et pourquoi la vraie rupture est la fabrication collective ;
* citer les ordres de grandeur d'une usine de pointe et en déduire la structure économique du secteur ;
* expliquer pourquoi le rendement dépend violemment de la surface de la puce, et ce que cela impose ;
* dire ce qu'une désignation de nœud recouvre et refuser de comparer deux procédés par leur nom ;
* expliquer pourquoi l'assemblage est redevenu central, et quel nouveau goulet il crée ;
* relier la fin de l'augmentation des fréquences à la densité de puissance ;
* nommer les trois familles de mémoires et le compromis qui impose leur hiérarchie ;
* dire pourquoi l'électronique de puissance conditionne l'électrification et où elle intervient.

---

---

---
