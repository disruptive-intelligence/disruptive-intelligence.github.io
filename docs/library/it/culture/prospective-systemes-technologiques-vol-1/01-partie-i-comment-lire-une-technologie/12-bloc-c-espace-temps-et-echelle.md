---
title: Bloc C — Espace, temps et échelle
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
up:
- - Prospective — systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

## 8.7 La vitesse finie de l'information

Rien ne transporte d'information plus vite que la lumière. Dans une fibre optique, le signal se propage à environ **200 000 km/s**, soit environ **200 km par milliseconde**.

**Ce que cela borne.** Le chapitre 5 l'a établi sur un exemple : un aller-retour transatlantique ne peut pas descendre sous quelques dizaines de millisecondes. Aucun équipement, aucun protocole, aucun investissement ne franchira cette limite. C'est une borne physique, et c'est ce qui la distingue de toutes les autres contraintes de ce chapitre.

**Trois conséquences qui traverseront le volume.**

**La latence ne s'achète pas comme le débit.** On peut multiplier le débit en ajoutant de la capacité. On ne peut pas raccourcir une distance. C'est pourquoi certaines architectures rapprochent le traitement de la donnée plutôt que l'inverse.

**La simultanéité n'existe pas gratuitement.** Deux systèmes distants ne peuvent pas savoir instantanément ce que fait l'autre. Toute coordination suppose des échanges, donc du délai, donc une incertitude sur l'état de l'autre pendant ce délai. Ce n'est pas un problème d'ingénierie logicielle : c'est une contrainte physique, et elle explique une bonne part de la difficulté des systèmes distribués et des systèmes autonomes coordonnés.

**Une boucle de contrôle est bornée par son délai.** Un système qui corrige sa trajectoire ne peut réagir plus vite que le temps nécessaire pour mesurer, décider et agir. Vouloir corriger plus vite que ce délai ne stabilise pas le système : cela le déstabilise. Le chapitre 16 y reviendra ; retenez que **le délai de boucle fixe un plafond de réactivité**, et que ce plafond n'est pas négociable.

## 8.8 Ondes et spectre : le cadre commun

Cette section est la plus dense du chapitre, et elle est celle qui vous servira le plus souvent. Elle établit une fois pour toutes un cadre qui servira à l'optique, au thermique, au radar, au lidar, aux télécommunications et à l'observation.

**Trois grandeurs liées.** Une onde électromagnétique se caractérise par sa **longueur d'onde** et sa **fréquence**, qui varient en sens inverse : longueur d'onde courte, fréquence élevée. L'énergie transportée par unité élémentaire croît avec la fréquence. Radio, micro-ondes, infrarouge, visible, ultraviolet, rayons X ne sont pas des phénomènes de nature différente : ce sont des régions d'un même continuum.

| Bande | Longueur d'onde | Usages typiques |
|---|---|---|
| Radio | mètres à kilomètres | radiodiffusion, communications longue portée |
| Micro-ondes | millimètres à centimètres | radar, réseaux mobiles, liaisons satellite |
| Infrarouge | micromètres à dizaines de micromètres | thermique, vision nocturne, télécoms optiques |
| Visible | environ 0,4 à 0,7 µm | vision humaine, imagerie courante |
| Ultraviolet et au-delà | plus court | stérilisation, lithographie, imagerie médicale |

**L'émission thermique — le point à retenir absolument.** Tout corps émet un rayonnement électromagnétique du seul fait de sa température, et **plus il est chaud, plus le rayonnement émis se déplace vers les courtes longueurs d'onde**.

Cela a une conséquence directe et très pratique :

| Objet | Température | Émet principalement dans |
|---|---|---|
| Corps humain, bâtiment, sol | environ 300 K | infrarouge lointain, autour de 10 µm |
| Moteur, échappement, foyer | quelques centaines de °C | infrarouge moyen |
| Filament, flamme vive | plus de 1 000 K | proche infrarouge et visible |
| Soleil | environ 5 800 K | visible, avec ses maxima au milieu de notre vision |

C'est pourquoi une caméra thermique voit dans le noir : elle ne capte pas de la lumière réfléchie, elle capte le rayonnement **émis** par les objets eux-mêmes. Et c'est pourquoi les capteurs infrarouges sont spécialisés par bande : détecter un corps humain et détecter une source très chaude ne se font pas dans la même région du spectre. Le Volume 2 en tirera tout son traitement de l'optronique ; vous avez ici le socle.

**Les fenêtres atmosphériques.** L'atmosphère n'est pas transparente partout. Certaines longueurs d'onde sont fortement absorbées par la vapeur d'eau ou le dioxyde de carbone, d'autres passent bien. Ces « fenêtres » ne sont pas un choix technique : elles dictent quelles bandes sont utilisables pour observer ou communiquer à travers l'atmosphère. Une bonne partie des choix de conception en observation et en télécommunications en découle directement.

**Le compromis universel.** Voici la règle qui, à elle seule, explique la plupart des architectures que vous rencontrerez.

| Longueur d'onde courte | Longueur d'onde longue |
|---|---|
| meilleure résolution pour une même taille d'antenne ou d'optique | résolution plus grossière |
| moins bonne pénétration : arrêtée par les nuages, la pluie, les murs | traverse mieux les obstacles et les conditions dégradées |
| antennes et optiques plus petites | antennes et optiques plus grandes |
| débit potentiel plus élevé | portée souvent meilleure |

**La finesse de détail accessible dépend du rapport entre la longueur d'onde et la taille de l'ouverture** — antenne, miroir, objectif. Pour un même détail à discerner, allonger la longueur d'onde impose d'agrandir l'ouverture. Cette relation explique la taille des antennes radar, celle des télescopes, la résolution des satellites d'observation, et pourquoi certaines mesures ne peuvent pas être miniaturisées.

> **Résout / coûte.** Passer à une longueur d'onde plus longue : *résout* la pénétration à travers nuages, pluie, poussière ou obstacles · *coûte* de la résolution à taille d'ouverture égale, donc de l'encombrement et de la masse.

## 8.9 Les lois d'échelle physiques

Quand on change la taille d'un objet, ses grandeurs ne suivent pas toutes le même rythme. C'est l'origine de nombreux échecs de mise à l'échelle, et le mécanisme est d'une simplicité désarmante.

**La règle du carré-cube.** Si l'on multiplie toutes les dimensions d'un objet par un facteur *k* :

* les longueurs sont multipliées par *k* ;
* les **surfaces** sont multipliées par *k²* ;
* les **volumes**, et donc les masses, par *k³*.

Un objet deux fois plus grand a quatre fois plus de surface et huit fois plus de masse.

**Première conséquence : la thermique.** La chaleur est produite en proportion du volume et évacuée en proportion de la surface. En grandissant, un objet produit donc de la chaleur plus vite qu'il ne peut l'évacuer. Un petit objet se refroidit tout seul ; un gros ne peut pas. C'est la raison profonde pour laquelle le refroidissement devient un problème dès que l'on agrandit — d'une cellule de batterie à un pack, d'une puce à une baie, d'une baie à un bâtiment.

**Deuxième conséquence : la structure.** La masse croît comme le cube, la section qui la supporte comme le carré. En grandissant, un objet devient proportionnellement plus lourd pour sa résistance. Il faut donc épaissir, ce qui alourdit encore. C'est pourquoi on ne peut pas simplement agrandir une structure qui fonctionne.

**Troisième conséquence, dans l'autre sens : le petit obéit à d'autres forces.** En réduisant la taille, les effets de surface — adhérence, tension superficielle, frottement — deviennent dominants devant le poids. Un très petit objet ne se comporte pas comme un grand objet miniaturisé : il vit dans un régime physique différent. C'est ce qui rend la microrobotique difficile pour des raisons qui n'ont rien à voir avec la miniaturisation de l'électronique.

**Ce que ce paragraphe vous permet de faire.** Le chapitre 31 vous demandera de dérouler un facteur mille. Vous savez maintenant que ce déroulé n'est pas une multiplication : **certaines grandeurs suivent, d'autres divergent**, et ce sont ces dernières qui décident.

---

## 8.10 Comment les trois blocs se recombinent

Les contraintes ne se rencontrent jamais isolément. Prenons un objet quelconque — disons un engin mobile autonome, sans préciser lequel — et voyons apparaître les trois blocs simultanément.

| Question de conception | Bloc | Contrainte à l'œuvre |
|---|---|---|
| Combien de temps peut-il fonctionner ? | A | énergie embarquée, densité, rendement de la chaîne |
| Pourquoi chauffe-t-il ? | A | pertes de conversion, toutes finissant en chaleur |
| Peut-on l'agrandir ? | C | carré-cube : masse et évacuation thermique divergent |
| Que voit-il dans le noir ? | C | émission thermique, choix de bande spectrale |
| Avec quelle finesse de détail ? | C | rapport longueur d'onde / ouverture |
| Sa perception est-elle fiable ? | B | bruit, plancher de détection, dynamique du capteur |
| Que fait-il quand un capteur dérive ? | B | la mesure fausse ne se signale pas |
| À quelle vitesse peut-il corriger sa trajectoire ? | C | délai de boucle |
| Peut-il coordonner son action avec un autre engin ? | C | vitesse finie, absence de simultanéité |

Aucune de ces contraintes n'est propre à cet objet. Vous rencontrerez les mêmes, sous d'autres noms, dans un centre de calcul, une chaîne de production, un satellite ou un bioréacteur.

🖼 **SCHÉMA — Les trois blocs et les familles qu'ils traversent.** Représenter les trois blocs A, B et C en colonnes, et les onze familles technologiques en lignes. À chaque intersection, faire figurer le nom que porte la contrainte dans ce domaine (par exemple : bloc A × calcul → « enveloppe thermique » ; bloc A × énergie → « pertes de conversion » ; bloc B × capteurs → « rapport signal sur bruit » ; bloc B × IA → « échec hors distribution »). Le schéma doit rendre visible que les colonnes sont peu nombreuses et les noms nombreux. Ce schéma est structurant pour le volume et sera repris au chapitre 20.

🖼 **SCHÉMA — Le spectre électromagnétique en pratique.** Axe horizontal en longueur d'onde, échelle logarithmique, du kilomètre au nanomètre. Trois bandeaux superposés : les régions nommées (radio, micro-ondes, infrarouge, visible, ultraviolet) ; les usages typiques ; les fenêtres atmosphériques, en indiquant les zones de forte absorption. Faire figurer, sous l'axe, les températures d'émission correspondantes (300 K, quelques centaines de °C, 5 800 K) alignées sur leur maximum d'émission. Schéma de référence, à rappeler aux chapitres 13, 14 et 18.

🗣 **Vocabulaire de terrain**

| Ce que vous entendez | Ce que cela signifie probablement | La question à poser |
|---|---|---|
| « Ça consomme X kWh » | une quantité, sans nature précisée | de l'électricité ou de la chaleur ? à quelle température ? |
| « On récupère la chaleur fatale » | valorisation possible mais limitée | à quelle température, et pour quel usage acceptant ce niveau ? |
| « Le capteur est très précis » | une des trois qualités a été privilégiée | et sa dynamique ? sa cadence ? |
| « L'algorithme améliore l'image » | inférence, pas mesure | qu'est-ce qui est mesuré et qu'est-ce qui est reconstruit ? |
| « On réduira la latence » | vrai jusqu'à une borne | quelle part est due à la distance ? celle-là ne bougera pas |
| « Il suffit de faire plus grand » | ignore le carré-cube | comment la chaleur sort-elle, et que devient la masse ? |

🎓 **À ce stade, vous savez…**

* distinguer une impossibilité physique d'une difficulté d'ingénierie, et savoir que la première catégorie est étroite ;
* refuser de comparer deux énergies sans en connaître la nature et la température ;
* multiplier les rendements d'une chaîne de conversion et en tirer une conclusion ;
* expliquer pourquoi tout finit en chaleur et pourquoi l'évacuer devient plus difficile en grandissant ;
* dire pourquoi la matière réelle se comporte autrement qu'une fiche technique, et pourquoi les durées de vie se comptent souvent en cycles ;
* poser la question du rapport signal sur bruit et identifier laquelle des trois qualités d'un capteur a été sacrifiée ;
* distinguer une mesure d'une inférence, et savoir qu'aucun traitement ne recrée l'information absente ;
* reconnaître qu'une mesure insuffisante ne se signale pas ;
* borner une latence par la distance, et un système de contrôle par son délai de boucle ;
* placer une longueur d'onde sur le spectre, en déduire ce qui émet quoi, et énoncer le compromis résolution / pénétration / ouverture ;
* dérouler la règle du carré-cube et prévoir ce qui diverge quand on agrandit.

**Ce que vous ne savez pas encore :** comment ces contraintes se manifestent concrètement dans chaque domaine. C'est l'objet des onze chapitres suivants, qui commencent par celui où vous êtes le plus à l'aise — et où les limites de vos modèles habituels apparaîtront le plus vite.

---

---

---
