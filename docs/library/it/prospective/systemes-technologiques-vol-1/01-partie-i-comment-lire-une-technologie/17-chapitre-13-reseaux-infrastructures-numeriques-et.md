---
title: Chapitre 13 — Réseaux, infrastructures numériques et datacenters
source: IT/09 Technologies & prospective/Systèmes technologiques (vol. 1).md
note: Systèmes technologiques (vol. 1)
up:
- - Systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

> **🎯 Pour lire ce chapitre**
>
> **À retenir :**
> * un centre de données est un bâtiment défini par une puissance électrique, et il la transforme en chaleur ;
> * seule la part de la latence due à la distance est incompressible.
>
> **À reconnaître :** gigue · densité par baie · dépendance invisible · cloud comme modèle de déploiement
>
> **Le reste se consulte.** Les mécanismes de détail, les chiffres et les variantes ne sont pas à mémoriser : ils sont là pour que vous puissiez y revenir.

Ce chapitre a un objectif précis pour un lecteur venant de l'informatique : vous faire voir votre infrastructure comme **un objet physique**. Vous en connaissez le fonctionnement logique ; ce chapitre traite de ce qui la contraint réellement, et qui relève de l'électricité, de la thermique, du foncier et du génie civil.

## 13.1 Pourquoi cette famille existe : déplacer l'information

Le problème : transporter de l'information d'un endroit à un autre, de façon fiable, à un débit suffisant, sur une distance donnée, à un coût acceptable.

**Le principe est toujours le même.** On module une grandeur physique — une onde électromagnétique, dans presque tous les cas — et on la fait varier au rythme de l'information à transmettre. Le récepteur observe ces variations et reconstitue le message.

**La bande passante disponible détermine le débit possible.** Plus la plage de fréquences utilisable est large, plus on peut faire varier le signal rapidement, donc plus on transmet d'information par seconde. C'est pourquoi les supports offrant de larges plages de fréquences — les fibres optiques, qui travaillent à des fréquences très élevées — permettent des débits sans commune mesure avec ceux des supports radio classiques.

**Le rapport signal sur bruit fixe la limite.** Le chapitre 8 l'a établi : il existe un plancher de détection. Pour un rapport signal sur bruit donné et une bande passante donnée, il existe un débit maximal au-delà duquel l'information ne passe plus de façon fiable. Ce n'est pas une limite d'équipement mais une limite théorique, et les systèmes modernes en sont proches. **Les gains futurs viendront donc de l'élargissement de la bande ou du nombre de canaux, non d'un meilleur décodage.**

## 13.2 Quatre supports, quatre compromis

| Support | Débit | Portée | Contrainte principale | Coût dominant |
|---|---|---|---|---|
| **Fibre optique** | très élevé | grande, avec amplification | il faut la poser | génie civil |
| **Cuivre** | modéré | courte, atténuation forte | atténuation, diaphonie | existant, déjà posé |
| **Radio terrestre** | variable | limitée par la puissance et les obstacles | spectre partagé, obstacles | licences, sites, densité |
| **Satellite** | variable | très grande | latence selon l'orbite, bilan de liaison | segment spatial |

**Ce que le chapitre 8 permet maintenant de comprendre.** Le choix entre ces supports découle directement du compromis longueur d'onde : plus la fréquence est élevée, plus le débit potentiel est grand, et plus la propagation est difficile — obstacles, pluie, portée réduite. Les fréquences basses traversent mieux et portent plus loin, avec des débits plus faibles. Toutes les architectures de réseau sont des arbitrages sur cet axe.

**Le spectre est une ressource attribuée.** Les fréquences utilisables ne s'achètent pas librement : elles sont réparties par des autorités, nationalement et internationalement, et leur attribution est un processus long. C'est un exemple net de ce que le chapitre 31 appelle une rareté institutionnelle plutôt que physique — la ressource existe, l'accès est régulé.

## 13.3 Protocoles et interopérabilité

Un réseau fonctionne parce que des équipements conçus indépendamment respectent des conventions communes, organisées en couches : chacune rend un service à celle du dessus sans que celle-ci connaisse son fonctionnement.

**Ce que cette organisation permet.** Remplacer une couche sans toucher aux autres — changer de support physique sans réécrire les applications.

**Ce qu'elle coûte.** Le chapitre 9 l'a nommé : les abstractions fuient. Une application indifférente au support découvre que la latence, la perte ou la variabilité du support remontent et affectent son comportement.

**Pourquoi les protocoles sont durables.** Un protocole largement déployé est une base installée au sens du chapitre 27, avec des effets de réseau maximaux : sa valeur vient précisément du fait que tout le monde l'utilise. C'est ce qui explique la longévité remarquable de certains protocoles techniquement imparfaits, et la difficulté à faire adopter leurs successeurs même supérieurs.

## 13.4 Latence, débit, gigue

Trois grandeurs distinctes, régulièrement confondues, et le chapitre 8 a montré qu'une seule est bornée par la physique.

**Le débit** — quantité par unité de temps. S'achète en ajoutant de la capacité.

**La latence** — délai avant l'arrivée du premier élément. Elle a quatre composantes : le temps de propagation, borné par la vitesse de la lumière ; le temps de mise sur le support, qui dépend du débit ; les temps de traitement dans les équipements traversés ; et les temps d'attente dans les files. **Seule la première est incompressible**, et elle vaut environ 200 km par milliseconde dans une fibre.

**La gigue** — la variabilité de la latence. Souvent plus gênante que la latence elle-même : un système peut s'adapter à un délai constant, beaucoup plus difficilement à un délai imprévisible.

**Ce que cela impose.** Le chapitre 8 l'a établi : la simultanéité n'existe pas gratuitement, et toute coordination entre systèmes distants suppose du délai, donc une incertitude sur l'état de l'autre. C'est une contrainte physique et non un défaut d'ingénierie logicielle — elle réapparaîtra au chapitre 16 pour les systèmes autonomes, et au Volume 2 pour la coordination distribuée.

## 13.5 Le datacenter comme objet physique

Voici le cœur du chapitre.

Un centre de données est généralement décrit par sa capacité de calcul ou de stockage. Physiquement, c'est **un bâtiment défini par une puissance électrique** — et le chapitre 8 a établi qu'il transforme la quasi-totalité de cette puissance en chaleur.

**Les grandeurs qui le caractérisent réellement :**

| Grandeur | Ce qu'elle détermine |
|---|---|
| Puissance raccordée | la taille réelle de l'installation |
| Densité de puissance par baie | ce qu'on peut y installer, et comment refroidir |
| Efficacité d'usage de l'énergie | la part consommée par autre chose que les équipements |
| Consommation d'eau | selon le mode de refroidissement retenu |
| Surface et foncier | contrainte croissante en zone dense |
| Délai de raccordement | le chapitre 26 l'a chiffré : plusieurs années |

**Le refroidissement est la contrainte structurante.** Le chapitre 8 l'a établi en général : évacuer la chaleur exige un écart de température, une surface d'échange et un fluide. À mesure que la densité de puissance par baie augmente — poussée notamment par les équipements de calcul intensif — l'air atteint ses limites, et le refroidissement liquide devient nécessaire. Ce n'est pas un raffinement : c'est un changement de nature de l'installation, avec des conséquences sur la conception du bâtiment, la maintenance et l'exploitation.

> **Résout / coûte.** Le refroidissement liquide : *résout* la densité de puissance évacuable · *coûte* une complexité de plomberie, un risque de fuite au contact d'équipements électriques, une maintenance différente, et une incompatibilité avec le parc existant — donc un problème de base installée.

**La chaleur récupérée est de basse valeur.** Le chapitre 12 l'a expliqué : une chaleur à quelques dizaines de degrés n'est valorisable que s'il existe un besoin à proximité immédiate acceptant ce niveau de température. La récupération est donc possible et géographiquement contrainte — elle ne se décide pas après coup.

**Cette section boucle la chaîne du chapitre 32.** Vous tenez maintenant les six maillons avec leurs chiffres : capacité de calcul, accès mémoire (chapitre 9), énergie et densité de puissance (chapitre 10), évacuation thermique (ici), raccordement électrique et délais d'équipement (chapitre 26).

## 13.6 Le cloud n'est pas une brique

Application directe du chapitre 2, et elle mérite d'être faite explicitement.

Le cloud n'est pas une technologie. C'est un **modèle de déploiement** : mutualisation de ressources physiques, facturation à l'usage, provisionnement à la demande. Les briques sous-jacentes sont des serveurs, des réseaux, du stockage et des bâtiments — objets parfaitement classiques.

**Ce que le modèle change réellement :** la structure de coûts, en transformant du capital en dépense d'exploitation ; l'élasticité, qui est une capacité et non une technologie ; et la localisation de la compétence, qui se déplace vers le fournisseur.

**Ce qu'il ne change pas :** aucune des contraintes physiques de ce chapitre. Le raccordement, le refroidissement, la latence, le foncier existent identiquement — ils sont simplement supportés par quelqu'un d'autre.

**Pourquoi ce point compte pour vous.** Le raisonnement « le cloud est infiniment élastique » est une abstraction qui fuit. L'élasticité perçue par un client repose sur une capacité physique préexistante, construite des années plus tôt, avec les délais de raccordement du chapitre 26. Quand la demande globale croît plus vite que cette capacité, l'abstraction cesse de tenir — et le client découvre que la ressource qu'il croyait illimitée est allouée.

## 13.7 Les dépendances invisibles

Le chapitre 25 a généralisé cette notion aux chaînes physiques ; voici sa forme d'origine.

Un système numérique dépend d'éléments minuscules, peu coûteux, rarement inventoriés, dont la défaillance l'arrête entièrement :

* **la résolution de noms**, sans laquelle les adresses ne se retrouvent plus ;
* **les certificats**, dont l'expiration interrompt des services parfaitement fonctionnels ;
* **la référence de temps**, dont dépendent les journaux, les protocoles de sécurité et la corrélation d'événements — et qui vient elle-même, dans beaucoup de cas, du système satellitaire du chapitre 18 ;
* **le routage**, dont une annonce erronée peut détourner un trafic à grande échelle ;
* **les câbles sous-marins**, qui portent l'essentiel du trafic intercontinental et dont le nombre sur certaines routes est faible.

**Le point commun.** Aucun de ces éléments n'est cher, et aucun n'apparaît dans les schémas d'architecture. C'est exactement le paradoxe de la criticité du chapitre 25 : **l'élément critique n'est pas l'élément coûteux, c'est celui dont l'absence arrête tout**.

**Cas de panne.** Un certificat expire sur un composant interne. Le service ne tombe pas immédiatement : il commence à refuser certaines connexions, de façon partielle et intermittente. Les symptômes apparaissent loin de la cause, à plusieurs couches d'abstraction de distance. Le diagnostic prend plus de temps que la correction — c'est la signature du chapitre 9 : la panne est deux couches plus bas que le symptôme.

## 13.8 Ce que cela implique

**Le passage à l'échelle.** D'un serveur à un bâtiment, les contraintes changent de nature : l'électricité devient un problème de raccordement au réseau national, le refroidissement un problème d'eau ou d'air, l'implantation une décision d'aménagement. Le chapitre 5 le disait sur cet exemple précis ; vous en tenez maintenant le détail.

**Dépendances.** Cette famille dépend de l'énergie, du foncier, des semi-conducteurs, du spectre, du spatial pour le temps et le positionnement, et de décisions d'attribution publiques. Presque toutes les autres familles dépendent d'elle pour leur exploitation.

**Implication cyber.** Trois points : les **frontières de confiance** se déplacent avec le modèle de déploiement, et une frontière déplacée est rarement redocumentée ; la **dépendance à des tiers non contractuels** — vous dépendez d'infrastructures avec lesquelles vous n'avez aucune relation ; et la **concentration géographique**, qui transforme une redondance apparente en risque commun au sens du chapitre 21.

## 🧪 Lab 5 — La chaîne calcul, énergie, chaleur
**Objectif.** Suivre une contrainte unique à travers trois familles et constater qu'elle change de nom sans changer de nature.
**Durée.** 60 minutes. **Difficulté.** 2/3. **Prérequis.** Chapitres 8, 9, 10, 13.
**Contexte.** Une installation de calcul vous est décrite par sa puissance électrique appelée, sa densité par baie, son mode de refroidissement et sa localisation.

**Travail demandé.**
(a) Établir, en une phrase et sans calcul, ce que devient l'électricité consommée par cette installation.
(b) Calculer la puissance thermique à évacuer, et la comparer à l'ordre de grandeur d'un système de chauffage domestique.
(c) Identifier, parmi les trois maillons — accès mémoire, densité de puissance, évacuation thermique — celui qui limite cette installation précise, et justifier.
(d) Estimer ce que deviendrait chacun des trois si la densité par baie était multipliée par quatre.
(e) Dire quelle amélioration technique serait sans effet sur le calendrier de ce projet, et pourquoi.

**Livrable.** Une page, calculs apparents.

**Éléments attendus.** En (a), la réponse est que la quasi-totalité devient de la chaleur — chapitre 8.2. En (c), il n'y a pas de réponse unique : elle dépend des données fournies, et une copie qui justifie son choix vaut mieux qu'une copie qui devine juste. En (e), la réponse recherchée est qu'une amélioration de performance par puce ne change rien si le raccordement électrique est attendu pour dans plusieurs années — c'est le déplacement de goulet du chapitre 26.4, et le repérer sans qu'on l'ait nommé est le vrai test de ce lab.

---

🎓 **À ce stade, vous savez…** relier le choix d'un support de transmission au compromis du chapitre 8 ; décomposer une latence et identifier sa seule composante incompressible ; décrire un datacenter par sa puissance et sa capacité d'évacuation thermique ; expliquer pourquoi le cloud est un modèle de déploiement et où son abstraction fuit ; inventorier les dépendances invisibles d'un système numérique.

---
