---
title: Chapitre 23 — Réseaux et gestion de l'énergie
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - ../index.md
- - Partie I — Lire une frontière technologique
  - index.md
---

> **Ce que ce chapitre ajoute.** Les chapitres 21 et 22 traitaient de produire et de stocker. Celui-ci traite de **transporter, équilibrer et raccorder** — et c'est là que se situe, aujourd'hui, le verrou le plus visible du domaine.
>
> **Cinq entrées**, dont deux majeures. La dernière n'est pas une technologie mais une contrainte, et c'est probablement la plus importante du chapitre.

---

## ◆◆◆ Réseaux électriques pilotés

**Niveau** — système · **Couche** — alimenter, décider, relier

**En une phrase.** Un réseau électrique instrumenté et commandé finement, capable d'ajuster production, consommation et stockage à des échelles de temps courtes.

**Pourquoi cette entrée est majeure.** Parce que **le réseau électrique ne stocke rien** : à chaque instant, production et consommation doivent s'équilibrer, aux pertes près. Toute la difficulté de l'électrification découle de cette contrainte.

**Comment ça fonctionne — et pourquoi la fréquence est la variable de survie.** Si la production dépasse la consommation, la fréquence du réseau monte ; si elle est inférieure, elle baisse. Un écart trop important déclenche des protections, qui déconnectent des équipements — ce qui aggrave le déséquilibre. **C'est un mécanisme d'effondrement en cascade**, et il se propage en quelques secondes, bien plus vite qu'aucune intervention humaine.

**L'inertie amortit les écarts.** Les grandes masses tournantes des alternateurs classiques stockent de l'énergie cinétique et ralentissent la variation de fréquence, laissant le temps aux régulations d'agir. **Les sources connectées par électronique de puissance ne fournissent pas naturellement cette inertie** — elles peuvent l'émuler, mais c'est une fonction à concevoir, non une propriété physique offerte.

C'est un cas net du mécanisme du volume 1 : **résoudre un problème en révèle un autre qui n'existait pas.**

**Ce que le pilotage apporte.** De la **flexibilité** : déplacer une consommation dans le temps, moduler un stockage, agréger de petits moyens dispersés pour qu'ils se comportent comme un moyen unique. C'est ce qui permet d'accueillir des sources variables sans multiplier les moyens de secours.

**Ce qui bloque.** **La congestion.** Le pilotage ne crée aucune capacité de transport : une production que le réseau ne peut pas évacuer reste inutilisable, quelle que soit l'intelligence de la conduite. **Confondre flexibilité et capacité est la confusion la plus coûteuse du domaine.**

S'y ajoutent l'**observabilité** des réseaux de distribution, historiquement peu instrumentés ; la **coordination** entre acteurs multiples ; et les **modèles de marché**, qui doivent rémunérer la flexibilité pour qu'elle existe.

**Sûreté et sécurité.** Le pilotage d'un réseau est un système numérique dont une défaillance produit des conséquences physiques immédiates et étendues. **C'est le cas le plus net du volume où le logiciel agit directement sur le monde**, et où les modèles de menace du système d'information ne suffisent pas : l'intégrité des commandes et la disponibilité du contrôle priment sur la confidentialité.

**À ne pas confondre avec.** **Le comptage communicant**, qui est une brique d'observabilité et non un système de conduite.

> ⏱ **État au 23/08/2026** — 🏭 déployé au niveau du transport, 🔬 émergent au niveau de la distribution. Développement rapide de l'agrégation de moyens décentralisés ; travaux actifs sur l'inertie synthétique.
> 🔄 **À revoir si** un grand réseau fonctionne durablement avec une part majoritaire de sources sans inertie mécanique.

**Renvois** — Couche : alimenter, décider · Courant : smart grid (ch. 34) · Convergence : énergie et calcul (40).

---

## ◆◆ Électronique de puissance avancée

**Niveau** — composant · **Couche** — alimenter

**En une phrase.** Les convertisseurs qui adaptent la forme de l'électricité — tension, fréquence, continu ou alternatif — entre la source et l'usage.

**Pourquoi c'est stratégique.** Parce que **ces composants sont présents dans presque toutes les chaînes énergétiques**, et que le volume 1 l'a établi : dans une chaîne, les rendements se multiplient. Un point gagné ici se répercute partout.

**Ce que ça permet.** Raccorder des sources qui ne produisent pas nativement du courant alternatif à la bonne fréquence · piloter finement des moteurs · transporter en courant continu sur longue distance, avec des pertes inférieures à l'alternatif au-delà d'une certaine distance · créer des réseaux à courant continu.

**Ce qui bloque.** **La dissipation thermique**, qui borne la puissance réellement commutable dans un volume donné. **Les perturbations électromagnétiques** engendrées par la commutation rapide, qui exigent une conception soignée — le gain ne s'obtient pas en remplaçant un composant. Et **le coût** des semi-conducteurs à grand gap, qui conditionnent les meilleures performances.

**Ce que cela implique.** C'est **une technologie habilitante au sens strict** : invisible pour l'utilisateur, présente partout, et dont le progrès conditionne celui de nombreuses autres couches — véhicules, réseaux, alimentations d'installations de calcul, actionneurs.

> ⏱ **État au 23/08/2026** — 🏭 déployé, en évolution rapide sous l'effet des semi-conducteurs à grand gap.
> 🔄 **À revoir si** les architectures à courant continu se généralisent dans les bâtiments ou les installations de calcul.

**Renvois** — Couche : alimenter · Voir aussi : semi-conducteurs à grand gap (ch. 19), actionneurs (ch. 15).

---

## ◆◆ Microgrids et centrales virtuelles

**Niveau** — système · **Couche** — alimenter, décider

**En une phrase.** Des ensembles locaux capables de fonctionner de façon autonome — ou des agrégations de moyens dispersés pilotés comme une unité unique.

**Comment ça fonctionne.** Un **microgrid** rassemble production, stockage et consommation sur un périmètre restreint, et peut se séparer du réseau principal pour continuer à fonctionner. Une **centrale virtuelle** agrège des moyens dispersés — panneaux, batteries, véhicules, consommations pilotables — pour qu'ils se présentent au marché comme un moyen unique.

**Ce que ça permet.** Une continuité de service en cas de défaillance du réseau · une valorisation de moyens individuellement trop petits pour participer au marché · une réduction des besoins de renforcement local.

**Ce qui bloque.** **La complexité de la conduite**, notamment le passage entre mode connecté et mode isolé. **Les modèles économiques**, qui dépendent entièrement des règles de marché et de tarification — ce sont des dispositifs dont la viabilité est déterminée par la réglementation. Et **la disponibilité effective** des moyens agrégés, qui appartiennent à des tiers dont l'engagement est variable.

**À ne pas confondre avec.** L'**autoconsommation**, qui ne suppose ni pilotage ni capacité d'îlotage.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour l'agrégation dans plusieurs marchés, 🔬 émergent pour les microgrids en dehors des sites isolés.
> 🔄 **À revoir si** les règles de marché ouvrent la participation des moyens agrégés à l'ensemble des services système dans une zone majeure.

**Renvois** — Couche : alimenter, décider.

---

## ◆◆◆ Raccordement et files d'attente

**Niveau** — contrainte · **Couche** — alimenter

**En une phrase.** Le délai et la capacité disponibles pour connecter une nouvelle installation — production ou consommation — au réseau électrique.

**Pourquoi cette entrée est majeure alors qu'elle ne décrit aucune technologie.** Parce que **c'est le verrou dominant de la couche aujourd'hui**, et parce qu'il est invisible dans toute analyse technique.

**Le mécanisme.** Raccorder une installation suppose d'étudier son effet sur le réseau, de dimensionner et parfois de construire les ouvrages nécessaires — postes, lignes, transformateurs. Les demandes sont traitées dans un ordre défini, et une demande peut dépendre d'ouvrages qui dépendent eux-mêmes d'autres demandes.

**Les grandeurs à connaître.** Le volume 1 les a chiffrées : les délais de raccordement pour les installations de forte puissance se comptent en années — couramment sept à dix dans plusieurs marchés d'Europe occidentale, et jusqu'à une décennie dans certains pôles. Et **une file d'attente n'est pas une capacité** : sur l'ensemble des demandes déposées aux États-Unis entre 2000 et 2019, une petite minorité avait atteint l'exploitation commerciale, l'essentiel ayant été retiré. ⏱

**Ce qui bloque, en aval de la procédure.** Une réforme des files d'attente ne suffit pas, car le goulet s'est déplacé : **construction de lignes de transport**, soumise à des procédures d'autorisation et à une acceptation locale ; **capacité des postes** ; et **délais de fabrication des transformateurs de puissance**, dont les carnets de commandes se comptent en années.

**Ce que cela implique — et c'est le résultat le plus important du chapitre.** Une amélioration d'efficacité, une baisse de coût de production ou une percée technologique **ne changent rien au calendrier d'un projet dont le raccordement est attendu pour dans plusieurs années**. Le verrou n'est ni dans la production, ni dans le calcul, ni dans le stockage : il est dans le génie électrique et dans les procédures.

**C'est la démonstration la plus nette du volume que le verrou n'est pas dans la couche où l'attention se porte.**

**À ne pas confondre avec.** **La capacité de production**, qui est une autre question. Un pays peut disposer d'une production abondante et être incapable de raccorder de nouveaux consommateurs.

> ⏱ **État au 23/08/2026** — contrainte active et aggravée. Délais élevés dans la plupart des marchés développés ; réformes de procédure engagées ; goulet industriel sur les équipements de réseau. **Domaine à évolution rapide, vérification obligatoire avant réédition.**
> 🔄 **À revoir si** les délais moyens de raccordement pour les installations de forte puissance baissent significativement dans un marché majeur.

**Renvois** — Couche : alimenter · Convergence : énergie et calcul (40) · Voir aussi : volume 1, chapitre 26.

---

## ◆ Récupération d'énergie

**Niveau** — capacité · **Couche** — alimenter

**En une phrase.** Alimenter un dispositif à faible consommation en captant l'énergie de son environnement — lumière, vibration, chaleur, ondes radio.

**Ce que ça permet.** Supprimer la pile d'un capteur, donc son remplacement — ce qui change entièrement l'économie d'un déploiement massif, où la maintenance domine le coût.

**Ce qui bloque.** **La puissance disponible**, très faible et intermittente, ce qui limite les usages à des dispositifs conçus pour consommer extrêmement peu et fonctionner par intermittence. Et **la variabilité de la source**, qui impose un stockage tampon et une conception tolérante aux interruptions.

**Ce que cela implique.** C'est une technologie qui ne rend service que si **le dispositif alimenté a été conçu pour elle** — on ne récupère pas de l'énergie pour un capteur existant, on conçoit un capteur autour de la récupération.

**À ne pas confondre avec.** Le **rechargement sans fil**, qui transfère une puissance importante sur une courte distance.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des usages établis dans le bâtiment et l'industrie.
> 🔄 **À revoir si** un dispositif de récupération alimente durablement un capteur communicant à débit utile sans batterie tampon significative.

**Renvois** — Convergence : intelligence distribuée (38).

---
