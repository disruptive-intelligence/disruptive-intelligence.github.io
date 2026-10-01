---
title: 'Chapitre 21 — La fiabilité : le mur invisible'
source: IT/09 Technologies & prospective/Systèmes technologiques (vol. 1).md
note: Systèmes technologiques (vol. 1)
up:
- - Systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

## 21.1 Pourquoi les derniers gains coûtent le plus cher

Un système qui réussit neuf fois sur dix impressionne. Un système qui réussit 999 999 fois sur un million est un produit. Entre les deux, il n'y a pas une amélioration : il y a un changement de métier.

La manière la plus parlante de le voir est de traduire un taux de disponibilité en temps d'indisponibilité annuel.

| Disponibilité | Indisponibilité par an |
|---|---|
| 90 % | environ 36 jours |
| 99 % | environ 3,7 jours |
| 99,9 % | environ 8,8 heures |
| 99,99 % | environ 53 minutes |
| 99,999 % | environ 5,3 minutes |
| 99,9999 % | environ 32 secondes |

Chaque ligne divise l'indisponibilité par dix. Aucune ne se franchit par le même moyen que la précédente.

Passer de 90 % à 99 % relève généralement de la correction des défauts fréquents : on les observe, on les répare. Passer de 99 % à 99,9 % demande de traiter des défauts qu'on n'observe qu'occasionnellement, donc de les instrumenter pour les voir. Passer de 99,9 % à 99,99 % oblige à traiter des combinaisons de circonstances qui ne se produisent jamais pendant les essais. Au-delà, on ne corrige plus des défauts : on conçoit un système qui reste acceptable quand ses composants échouent.

Le lecteur venant de l'exploitation informatique connaît cette progression et son coût. Le point de ce chapitre est qu'elle est **universelle** : elle vaut pour un moteur, un capteur, une chaîne de production, un réseau électrique et un système autonome. Et surtout, elle est **invisible dans une démonstration**, puisqu'une démonstration ne dure pas assez longtemps pour rencontrer les événements rares.

> **P6 — La fiabilité n'est pas une performance : les derniers gains sont généralement disproportionnellement difficiles.**

**Précision importante.** Ce principe n'est pas une loi quantitative. Il n'existe pas de règle établissant qu'un neuf supplémentaire coûte exactement un ordre de grandeur. Ce qui est robuste, c'est la forme : les gains de fiabilité deviennent de plus en plus coûteux à mesure qu'on progresse, et le coût marginal croît plus vite que le gain. Traiter cela comme une équation serait exactement l'erreur du chapitre 7.

## 21.2 De quoi une défaillance est faite

Trois notions suffisent pour raisonner, et elles se confondent souvent.

**Le mode de défaillance** — *comment* ça casse. Un roulement s'use, un condensateur sèche, un logiciel accumule un état, un capteur dérive, une soudure se fissure sous les cycles thermiques. Deux systèmes de même fiabilité globale peuvent avoir des modes de défaillance radicalement différents, et c'est le mode, pas le taux, qui détermine ce qu'il faut faire.

**Le taux de défaillance dans le temps** — la fameuse courbe en baignoire. La plupart des populations d'objets manufacturés présentent trois régimes : une mortalité infantile élevée au début (défauts de fabrication), un plateau long à taux faible et à peu près constant, puis une remontée par usure. Cette forme explique deux pratiques industrielles qui paraissent absurdes vues de loin : le **déverminage** (faire fonctionner les objets en usine pour éliminer les défaillances précoces avant livraison) et le **remplacement préventif** de pièces encore fonctionnelles avant l'entrée en zone d'usure.

**La durée de vie** — combien de temps ou combien de cycles. Une batterie ne meurt pas : elle perd de la capacité, cycle après cycle. Un panneau photovoltaïque ne s'arrête pas : il se dégrade lentement. Pour ces objets, la question « est-ce que ça marche ? » n'a pas de sens sans « pendant combien de temps, et à quel niveau de performance résiduelle ? ».

**L'erreur d'analyse la plus fréquente** consiste à confondre une fiabilité de composant avec une fiabilité de système. Un système composé de composants très fiables peut être peu fiable, si les défaillances se combinent ou si l'assemblage introduit ses propres modes. L'inverse est vrai aussi : c'est tout l'objet de la section suivante.

## 21.3 Redondance

ce qu'elle règle, ce qu'elle coûte, ce qu'elle ne règle pas

La redondance consiste à dupliquer une fonction pour qu'une défaillance unique n'arrête pas le système. C'est le mécanisme central de la haute fiabilité, et il est plus fragile qu'il n'y paraît.

**Ce qu'elle règle.** Les défaillances indépendantes. Si deux composants ont chacun une probabilité de panne de 1 %, et que leurs pannes sont réellement indépendantes, la probabilité qu'ils tombent tous les deux est de 0,01 % — deux ordres de grandeur gagnés pour un composant ajouté. C'est un excellent rendement, et c'est pourquoi la redondance est partout.

**Ce qu'elle coûte.** Masse, volume, énergie, prix, complexité, et surtout **un mécanisme de bascule** — un dispositif qui détecte la défaillance et commute. Ce mécanisme devient lui-même un composant critique, et l'expérience industrielle montre qu'il est souvent le point faible de l'ensemble.

**Ce qu'elle ne règle pas.** Les **défaillances de mode commun** : une cause unique qui atteint simultanément tous les exemplaires redondants. Un défaut de conception présent dans les deux unités. Une erreur logicielle identique dans les deux calculateurs. Une alimentation partagée. Un lot de fabrication défectueux. Un incendie dans le local qui contient les deux serveurs. Une inondation qui atteint les deux groupes électrogènes.

L'hypothèse d'indépendance est **toujours** l'hypothèse porteuse d'un raisonnement de redondance, au sens du chapitre 4. C'est donc elle qu'il faut attaquer en premier.

> **Une redondance non testée est une croyance.**

Cette formule mérite d'être prise au pied de la lettre. Un dispositif de secours qui n'a jamais basculé en conditions réelles n'a pas démontré qu'il basculerait. C'est un cas particulier du chapitre 6 : la redondance est une affirmation, et le test de bascule est son protocole.

**La question à poser :** *quand la bascule a-t-elle été exercée pour la dernière fois, en conditions réelles, sans prévenir ?*

## 21.4 Échouer proprement

Pour beaucoup de systèmes, l'objectif n'est pas de ne jamais échouer — c'est inatteignable — mais d'échouer d'une manière acceptable. Le chapitre 16 a introduit deux réponses distinctes ; il faut maintenant voir ce qu'elles coûtent.

**Fail-safe** : en cas de défaillance, le système se met dans un état sûr et cesse de fonctionner. Un ascenseur bloque ses freins. Un robot industriel s'immobilise. C'est la réponse la moins coûteuse et elle convient quand l'arrêt est sûr.

**Fail-operational** : le système doit continuer à assurer sa fonction malgré la défaillance, parce que s'arrêter n'est pas sûr. Un avion en vol ne peut pas s'arrêter. Un véhicule autonome sur une voie rapide non plus : s'immobiliser au milieu de la circulation est un mode de défaillance dangereux.

**Le saut de coût entre les deux est considérable**, et il est régulièrement sous-estimé dans les analyses. Le fail-operational impose de la redondance sur la chaîne complète — perception, calcul, alimentation, actionneurs — et pas seulement sur le composant qu'on juge le plus fragile. C'est l'une des raisons pour lesquelles l'autonomie de niveau élevé coûte structurellement plus cher que l'assistance à la conduite, indépendamment de la qualité de la perception.

**Un troisième cas, souvent oublié : la défaillance silencieuse.** Le chapitre 14 l'a rencontrée avec le capteur dérivé, le chapitre 15 avec le modèle produisant une sortie plausible hors distribution. Ni fail-safe ni fail-operational ne s'appliquent, parce que **rien ne signale la défaillance**. C'est le mode le plus dangereux, et il est spécifiquement difficile à traiter pour les systèmes apprenants — nous y revenons en 21.6 et au chapitre 28.

## 21.5 Ce que la fiabilité coûte en temps

le cas de l'aviation commerciale

L'aviation commerciale est le meilleur exemple documenté de fiabilité de très haut niveau atteinte sur un système complexe. Elle est aussi un excellent antidote à l'idée que la fiabilité s'obtiendrait par la technologie seule.

**Les faits.** Selon le rapport annuel de sécurité de l'IATA publié en mars 2026, l'année 2025 a vu 51 accidents pour 38,7 millions de vols, soit un taux de 1,32 accident par million de vols — environ un accident pour 760 000 vols. La tendance longue est plus significative que l'année isolée : le taux est passé de 3,72 accidents par million de secteurs en 2005 à 1,32 en 2025. Sur les accidents mortels, la moyenne mobile sur cinq ans est passée d'un accident mortel pour 3,5 millions de vols sur 2012-2016 à un pour 5,6 millions de vols sur 2021-2025.

**Trois enseignements, et le troisième est le plus important.**

**Premier enseignement : c'est lent.** Diviser le taux d'accidents par près de trois a demandé vingt ans, sur une industrie déjà très sûre au départ. Il n'existe aucun exemple de gain d'un ordre de grandeur en fiabilité obtenu rapidement sur un système complexe déployé.

**Deuxième enseignement : les gains sont ciblés.** Le rapport 2025 relève l'absence d'accidents de type perte de contrôle en vol, catégorie historiquement responsable d'une grande part des décès. Ce n'est pas un progrès diffus : c'est le résultat d'un travail spécifique sur une famille de causes identifiée. La fiabilité se gagne mode de défaillance par mode de défaillance, pas globalement.

**Troisième enseignement : la fiabilité est une construction institutionnelle.** Ce que l'aviation a bâti, ce n'est pas seulement une technologie : c'est un système de retour d'expérience obligatoire, une classification indépendante des accidents, des recommandations opposables, des audits d'exploitation, une formation normalisée et une culture du signalement sans sanction. Le rapport le montre indirectement : les compagnies inscrites au registre d'audit d'exploitation présentent un taux d'accidents nettement inférieur à celles qui ne le sont pas. **La même technologie exploitée dans deux cadres institutionnels différents ne produit pas la même fiabilité.**

**Ce que ce cas ne permet pas de conclure.** Que tout système atteindra ce niveau. L'aviation bénéficie d'un environnement relativement contrôlé, d'opérateurs professionnels formés, d'une flotte homogène et d'une économie qui permet d'amortir des coûts de sécurité élevés. Peu de domaines réunissent ces quatre conditions.

⏱ *Données IATA 2025, publiées en mars 2026. Voir Annexe I.*

## 21.6 Fiabilité et apprentissage statistique

Un système appris pose un problème de fiabilité d'une nature particulière, et c'est l'un des points où le lecteur doit être le plus précis.

**Le problème des queues de distribution.** Un système appris à partir de données est bon là où les données sont denses. Les situations rares sont, par définition, rares dans les données d'entraînement. Or ce sont précisément elles qui déterminent la fiabilité au-delà de quelques neuf. Il existe donc une asymétrie structurelle : le système progresse vite jusqu'à un certain niveau, puis chaque incrément supplémentaire exige un volume de données ou de situations difficiles qui croît beaucoup plus vite que le gain obtenu.

**Trois conséquences pratiques.**

D'abord, **une démonstration ne renseigne presque pas** sur ce régime. Elle échantillonne le centre de la distribution, jamais les queues.

Ensuite, **le kilométrage ou le volume d'usage devient la seule mesure crédible**, et il en faut énormément. Établir statistiquement qu'un système est plus sûr qu'une référence humaine sur des événements rares exige un nombre d'expositions considérable — c'est une contrainte mathématique, pas une exigence bureaucratique.

Enfin, **la vérification exhaustive est impossible**. On ne peut pas énumérer les situations d'entrée d'un système ouvert sur le monde. C'est ce qui rend la certification des systèmes apprenants structurellement différente de la certification classique, et c'est l'objet du chapitre 28.

**Un exemple d'affirmation à lire correctement.** Un exploitant de véhicules autonomes a publié des analyses portant sur plus d'une centaine de millions de kilomètres parcourus, faisant état d'une réduction importante des accidents avec blessures graves par rapport à une référence humaine comparable. ⏱

Que peut-on en conclure, avec les instruments du chapitre 6 ? Que sur **cette flotte**, dans **ces villes**, sur **ces types de voies**, avec **cette référence de comparaison**, le résultat est favorable et repose sur un volume d'exposition sérieux. Que ne peut-on pas en conclure ? Que le résultat se transporte à d'autres environnements, à d'autres conditions météorologiques, ou à d'autres types de voies non incluses dans le domaine d'exploitation. La question à poser n'est donc jamais « est-ce fiable ? » mais **« fiable dans quel domaine d'exploitation, et que se passe-t-il aux frontières de ce domaine ? »**.

C'est exactement la notion d'enveloppe de fonctionnement introduite au chapitre 16.

🗣 **Vocabulaire de réunion**

| Ce que vous entendez | Ce que cela signifie probablement | La question à poser |
|---|---|---|
| « On est à 99 % » | un taux mesuré sur une période et un périmètre non précisés | 99 % de quoi, mesuré comment, sur quelle durée ? |
| « C'est redondant » | il existe un second exemplaire | la bascule a-t-elle été testée, et qu'est-ce qui est commun aux deux ? |
| « Le système est robuste » | affirmation qualitative | robuste à quoi ? quel mode de défaillance a été traité ? |
| « Ça n'est jamais arrivé » | la période d'observation est peut-être plus courte que la période de retour | depuis combien de temps observe-t-on, et avec quelle instrumentation ? |
| « On corrigera en production » | vrai pour le logiciel, faux pour le matériel | quel est le coût d'un rappel physique ? |

🧪 **Lab 10 — Diagnostic de fiabilité**

**Objectif.** Distinguer taux, mode et durée de vie ; attaquer une hypothèse d'indépendance.
**Durée.** 60 minutes. **Difficulté.** 2/3. **Prérequis.** Chapitres 14, 16, 21.
**Contexte.** Une architecture système vous est fournie, comportant deux chaînes redondantes, un mécanisme de bascule, une alimentation et un jeu de capteurs.
**Travail demandé.** (a) Lister les modes de défaillance par composant. (b) Identifier tout ce qui est commun aux deux chaînes — c'est le cœur de l'exercice. (c) Dire si le système est fail-safe ou fail-operational, et si ce choix est cohérent avec sa fonction. (d) Identifier au moins un mode de défaillance silencieuse. (e) Proposer un test de bascule réaliste, en précisant ce qu'il ne prouverait pas.
**Livrable.** Une page, dont un tableau des éléments communs.
**Éléments attendus.** L'architecture fournie contient au moins trois éléments de mode commun, dont un non évident (l'horloge, le lot de fabrication, ou l'équipe qui a écrit les deux logiciels). Une copie qui n'en trouve qu'un a fait l'exercice attendu ; une copie qui en trouve trois a compris le mécanisme. En (e), l'erreur fréquente est de proposer un test qui vérifie que la bascule fonctionne quand on la déclenche volontairement — ce qui ne prouve rien sur son déclenchement automatique en conditions non anticipées.

🎓 **À ce stade, vous savez…**

* traduire un taux de disponibilité en indisponibilité annuelle et sentir le coût de chaque neuf ;
* distinguer mode de défaillance, taux dans le temps et durée de vie ;
* attaquer une hypothèse d'indépendance et repérer les défaillances de mode commun ;
* distinguer fail-safe, fail-operational et défaillance silencieuse, et connaître leur écart de coût ;
* expliquer pourquoi la fiabilité est une construction institutionnelle autant que technique ;
* dire pourquoi les systèmes appris ont un problème de fiabilité spécifique dans les queues de distribution.

---
