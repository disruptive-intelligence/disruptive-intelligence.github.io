---
title: Chapitre 19 — Matériaux émergents
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
chapter: 8
chapters: 14
---

> **Ce que ce chapitre ajoute.** Le chapitre 18 traitait des procédés. Celui-ci traite de **ce qu'on met dedans** — et d'une contrainte qui structure tout : entre la découverte d'un matériau et sa disponibilité industrielle, il s'écoule couramment une à deux décennies.
>
> **Un avertissement de lecture.** C'est le chapitre de l'atlas où les promesses récurrentes sont les plus nombreuses. Plusieurs entrées décrivent des matériaux annoncés comme transformateurs depuis longtemps et dont la trajectoire réelle est plus étroite. Le traitement est le même pour tous : ce qui est établi, ce qui bloque, et à quelle condition cela changerait.
>
> **Huit entrées.**

---

### ◆◆◆ Semi-conducteurs à grand gap

**Niveau** — composant · **Couche** — fabriquer, alimenter

**En une phrase.** Des matériaux semi-conducteurs — principalement le carbure de silicium et le nitrure de gallium — qui supportent des tensions, des températures et des fréquences de commutation bien supérieures à celles du silicium.

**Pourquoi on en parle.** Parce que **ce sont les composants qui conditionnent l'électrification**, et parce que leur effet se multiplie : chaque point de rendement gagné sur une conversion se répercute sur toute la chaîne.

**Comment ça fonctionne.** Un convertisseur de puissance ne dissipe presque rien quand l'interrupteur est franchement passant ou franchement bloqué : **l'essentiel des pertes se produit pendant la transition**. Commuter plus vite réduit donc la perte par cycle. Ces matériaux commutent plus vite et supportent des tensions plus élevées, ce qui permet à la fois de réduire les pertes et de diminuer la taille des composants passifs associés — bobines et condensateurs, dont le volume décroît quand la fréquence augmente.

**Le carbure de silicium** domine les hautes tensions — traction ferroviaire, véhicules, réseau. **Le nitrure de gallium** domine les fréquences élevées à tension modérée — alimentations, chargeurs, télécommunications.

**Où vous rencontrerez le terme.** Véhicules électriques · chargeurs · alimentations · onduleurs solaires · traction ferroviaire · centres de calcul · télécommunications.

**Ce que ça permet.** Réduire les pertes de conversion de plusieurs points · réduire la masse et le volume des convertisseurs · augmenter la tension de fonctionnement, ce qui réduit les courants et donc les pertes en ligne.

**Ce qui bloque.** **Le coût du substrat**, plus élevé que le silicium, même s'il baisse avec le volume. **La qualité cristalline** : ces matériaux tolèrent moins bien les défauts, ce qui pèse sur le rendement de production. **La commutation rapide elle-même**, qui génère des perturbations électromagnétiques exigeant une conception soignée — le gain ne s'obtient pas en remplaçant simplement un composant. Et **la chaîne d'approvisionnement**, étroite en substrats.

**Ce que cela implique.** C'est une brique dont le progrès **se propage à toute la couche *alimenter*** sans jamais être visible pour l'utilisateur final. Le chapitre 23 y renverra ; c'est un exemple net de technologie habilitante au sens du volume 1.

**À ne pas confondre avec.** **Le silicium**, qui reste dominant en volume et parfaitement adapté à la majorité des applications de puissance modérée.

> ⏱ **État au 23/08/2026** — 🏭 déployé et en croissance rapide. Capacité de production de substrats en extension ; passage progressif à des diamètres de plaquette supérieurs, ce qui est le principal levier de baisse de coût.
> 🔄 **À revoir si** le coût par ampère commuté atteint la parité avec le silicium sur les gammes de tension intermédiaires.

**Renvois** — Couche : fabriquer, alimenter · Convergence : énergie et calcul (40) · Voir aussi : électronique de puissance (ch. 23), actionneurs (ch. 15).

---

### ◆◆ Métamatériaux

**Niveau** — famille · **Couche** — fabriquer

**En une phrase.** Des matériaux dont les propriétés ne viennent pas de leur composition mais de leur **structure interne**, organisée à une échelle plus fine que la longueur d'onde qu'ils manipulent.

**Comment ça fonctionne.** En disposant des motifs réguliers plus petits que la longueur d'onde d'une onde — électromagnétique, acoustique, mécanique —, on obtient un comportement d'ensemble que ne présente aucun matériau naturel : dévier une onde de façon inhabituelle, l'absorber sélectivement, ou concentrer une énergie.

**Ce que ça permet.** Des antennes plus compactes ou reconfigurables · des absorbants acoustiques minces · des lentilles plates · des structures mécaniques à propriétés inhabituelles — rigidité dans une direction et souplesse dans une autre.

**Ce qui bloque.** **La bande passante.** Une structure conçue pour une longueur d'onde fonctionne mal ailleurs, ce qui limite l'usage général. **La fabrication** : les motifs doivent être réguliers à une échelle fine, sur une surface étendue. Et **le coût**, qui reste élevé au regard de solutions conventionnelles souvent suffisantes.

**Ce que cela implique.** Les applications qui percent sont celles où **la contrainte d'encombrement domine le coût** — antennes de terminaux, surfaces reconfigurables pour les réseaux, absorbants dans des espaces contraints. C'est une famille qui gagne par la géométrie, non par la performance brute.

**À ne pas confondre avec.** **Les nanomatériaux**, définis par leur échelle et non par leur structuration périodique.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des applications établies en antennes et en acoustique.
> 🔄 **À revoir si** une surface reconfigurable atteint un déploiement significatif dans les réseaux de télécommunications.

**Renvois** — Couche : fabriquer.

---

### ◆◆ Matériaux bidimensionnels

**Niveau** — famille · **Couche** — fabriquer

**En une phrase.** Des matériaux constitués d'une ou de quelques couches atomiques, dont le graphène est le représentant le plus connu.

**Pourquoi on en parle — et pourquoi le cas est instructif.** Parce que **c'est le cas de sur-anticipation le mieux documenté de la période récente**. Des propriétés exceptionnelles mesurées en laboratoire — conductivité, résistance mécanique, transparence — ont produit deux décennies d'annonces d'applications qui, pour l'essentiel, ne se sont pas matérialisées à l'échelle industrielle.

**Ce qui explique l'écart.** Les propriétés exceptionnelles sont mesurées sur des échantillons **parfaits et minuscules**. Produire de grandes surfaces de qualité constante est un problème différent, et les propriétés se dégradent fortement avec les défauts. S'y ajoute une difficulté d'intégration : un matériau d'une couche atomique est difficile à manipuler, à transférer et à connecter.

**Ce que cela implique — et c'est la leçon du chapitre.** Un matériau se juge par **ses propriétés à l'échelle et à la qualité industriellement atteignables**, pas par ses propriétés maximales en laboratoire. Cet écart est structurel et il vaut pour toutes les entrées de ce chapitre.

**Les usages réels** se situent aujourd'hui dans des additifs — améliorer un composite, une batterie, un revêtement — plutôt que dans des dispositifs où le matériau serait l'élément principal.

**À ne pas confondre avec.** **Les nanomatériaux** en général, catégorie bien plus large.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des usages établis comme additif. Production de grandes surfaces de qualité électronique encore limitée.
> 🔄 **À revoir si** un dispositif électronique utilisant un matériau bidimensionnel comme élément actif atteint la production de série.

**Renvois** — Couche : fabriquer.

---

### ◆◆ Composites avancés

**Niveau** — famille · **Couche** — fabriquer

**En une phrase.** Des matériaux associant des fibres résistantes et une matrice qui les lie, offrant un rapport résistance sur masse très supérieur à celui des métaux.

**Ce que ça permet.** Réduire la masse à performance mécanique égale · orienter les propriétés selon les directions de sollicitation · intégrer des fonctions dans la structure.

**Ce qui bloque — et ce sont des contraintes d'exploitation, pas de conception.** **L'inspection.** Un composite se dégrade par délaminage interne, invisible en surface : détecter un dommage exige des moyens non destructifs coûteux. **La réparation**, difficile et souvent limitée à des zones restreintes. **Le recyclage**, la séparation fibre-matrice n'ayant pas de solution industrielle satisfaisante. Et **le mode de rupture** : un composite rompt brutalement, sans déformation préalable — il ne prévient pas, contrairement à un métal.

**Ce que cela implique.** L'arbitrage composite contre métal ne se joue pas sur la performance mais sur **le cycle de vie complet** : inspection, réparabilité, fin de vie. C'est pourquoi les secteurs qui les emploient massivement sont ceux où le gain de masse a une valeur exceptionnelle.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Progrès sur les procédés hors autoclave et sur les matrices thermoplastiques, qui améliorent la cadence et la recyclabilité.
> 🔄 **À revoir si** un procédé de recyclage préservant les propriétés des fibres atteint l'échelle industrielle.

**Renvois** — Couche : fabriquer.

---

### ◆◆ Matériaux programmables et intelligents

**Niveau** — famille · **Couche** — fabriquer

**En une phrase.** Des matériaux qui changent de forme, de rigidité ou de propriété en réponse à un stimulus — chaleur, champ, lumière, humidité.

**Pourquoi ces deux termes sont traités ensemble.** Parce qu'ils désignent la même chose avec deux accents : *intelligent* insiste sur la réponse au stimulus, *programmable* sur le fait que cette réponse est inscrite à la fabrication. **Les traiter séparément suggérerait deux familles distinctes qui n'existent pas.**

**Ce que ça permet.** Supprimer des actionneurs — la structure fait le travail · des dispositifs qui se déploient seuls · des surfaces qui s'adaptent aux conditions · des assemblages qui se démontent sur commande.

**Ce qui bloque.** **La cinétique et la force.** La réponse est souvent lente et le travail mécanique disponible faible. **La fatigue** : la répétition du cycle dégrade la propriété. **Le contrôle**, le stimulus étant souvent global alors que la réponse voulue est locale. Et **la fabrication**, qui exige de structurer le matériau à une échelle fine.

**Ce que cela implique.** Ces matériaux ne remplacent pas des actionneurs à performance égale : ils occupent des niches où **la simplicité mécanique vaut plus que la performance** — dispositifs à usage unique, déploiement spatial, biomédical, environnements où un moteur ne peut pas être placé.

**À ne pas confondre avec.** **Les composites**, dont les propriétés sont fixes. **La robotique souple** (ch. 14), qui emploie parfois ces matériaux mais désigne des machines.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des usages établis en médical et en spatial.
> 🔄 **À revoir si** un matériau actif atteint une densité de travail mécanique comparable à celle d'un actionneur électrique compact.

**Renvois** — Couche : fabriquer.

---

### ◆ Nanomatériaux

**Niveau** — famille · **Couche** — fabriquer

**En une phrase.** Des matériaux dont au moins une dimension se situe à l'échelle du nanomètre, ce qui modifie leurs propriétés par rapport au même matériau massif.

**Ce qu'il faut en savoir.** **C'est une catégorie définie par une échelle, pas par une fonction** — elle rassemble des objets sans propriété commune autre que leur taille. Les usages réels sont massivement des **additifs** : renforcer un composite, améliorer une électrode, modifier un revêtement, catalyser une réaction.

**Ce qui bloque.** La **dispersion** — obtenir une répartition homogène dans une matrice est le problème pratique dominant. Et la **toxicologie**, l'évaluation des effets sanitaires et environnementaux étant plus lente que le développement des applications, ce qui produit une incertitude réglementaire.

**À ne pas confondre avec.** **La nanotechnologie** au sens de machines à l'échelle nanométrique, qui relève d'un autre registre et n'a pas d'existence industrielle.

> ⏱ **État au 23/08/2026** — 🏭 déployé comme additif dans de nombreux secteurs.
> 🔄 **À revoir si** un cadre réglementaire harmonisé sur les nanomatériaux entre en vigueur dans une juridiction majeure.

**Renvois** — Couche : fabriquer.

---

### ◆◆ Supraconductivité

**Niveau** — famille · **Couche** — fabriquer, alimenter

**En une phrase.** La propriété de certains matériaux de conduire l'électricité sans aucune résistance en dessous d'une température critique.

**Pourquoi cette entrée mérite un traitement soigneux.** Parce que c'est **la promesse récurrente la plus ancienne du chapitre**, et parce que la distinction entre ce qui est déployé et ce qui est prospectif y est particulièrement mal faite dans le discours public.

**Ce qui est déployé depuis des décennies.** Les supraconducteurs à basse température, refroidis à l'hélium liquide, sont une technologie industrielle mature : imagerie médicale par résonance magnétique, aimants d'accélérateurs, instruments scientifiques. **Le marché existe, il est stable, et il n'a rien de prospectif.**

**Ce qui est émergent.** Les supraconducteurs à plus haute température critique — refroidis à l'azote liquide, bien moins coûteux — sous forme de rubans. Ils permettent des aimants plus compacts et plus intenses, ce qui intéresse directement les projets de fusion par confinement magnétique et certaines applications de réseau électrique.

**Ce qui est prospectif, voire spéculatif.** La supraconductivité à température ambiante et pression ordinaire. Des annonces périodiques suscitent une attention considérable et n'ont pas été confirmées par réplication indépendante. **C'est un domaine où l'échelon « réplication » de l'échelle des preuves doit être appliqué avec une rigueur particulière.**

**Ce qui bloque, dans tous les cas.** **Le refroidissement**, dont le coût et la complexité dominent l'économie de tout système supraconducteur. **La densité de courant critique**, qui chute en présence d'un champ magnétique intense — précisément la condition d'usage. Et **la fabrication des rubans**, procédé délicat et coûteux au mètre.

**Ce que cela implique.** Même une supraconductivité à température ambiante ne supprimerait pas toutes les difficultés : il resterait la densité de courant, le comportement sous champ, la mise en forme et la protection en cas de perte brutale de supraconductivité. **La température n'est qu'un des paramètres.**

**À ne pas confondre avec.** **La simple bonne conductivité**. La supraconductivité est une propriété qualitativement différente, et elle disparaît brutalement au-delà de seuils de température, de champ ou de courant.

> ⏱ **État au 23/08/2026** — 🏭 déployé à basse température, 🔬 émergent pour les rubans à haute température, 🔭 prospectif pour la température ambiante.
> 🔄 **À revoir si** une supraconductivité à température ambiante et pression ordinaire fait l'objet d'une réplication indépendante confirmée par plusieurs équipes.

**Renvois** — Couche : fabriquer, alimenter · Voir aussi : fusion (ch. 22), calcul supraconducteur (ch. 9).

---

### ◆◆◆ Matériaux critiques et substitution

**Niveau** — contrainte · **Couche** — fabriquer

**En une phrase.** Les matériaux dont l'approvisionnement est concentré, difficile à substituer et long à développer — et qui contraignent en amont une grande partie de cet atlas.

**Pourquoi cette entrée est en ◆◆◆.** Parce qu'elle ne décrit pas une technologie mais **une contrainte qui borne les autres**, et parce que le raisonnement qu'elle porte s'applique à presque toutes les couches.

**Ce qui rend un matériau critique — trois facteurs cumulatifs.**

**La dispersion.** Un élément peut être abondant dans la croûte terrestre et rarement concentré en gisements exploitables.

**La coproduction.** Certains éléments sont extraits comme sous-produits d'un autre métal : leur production dépend d'une demande qui n'est pas la leur, et augmenter l'offre suppose d'augmenter la production du métal principal.

**La concentration du raffinage.** **C'est le point décisif et le plus mal compris.** Extraire un minerai est une chose ; le transformer en matériau de qualité industrielle en est une autre, qui suppose des installations spécialisées, une acceptabilité environnementale et un savoir-faire accumulé. **Le goulet est presque toujours au raffinage, pas à la mine.**

**La contrainte temporelle, qui est la plus dure.** Le développement d'une grande mine, de la découverte à la première production, demande couramment plus de quinze ans. ⏱ **Aucune décision prise aujourd'hui ne peut modifier substantiellement l'offre minière avant le milieu de la décennie suivante.** Toute analyse supposant une réponse rapide de l'offre à une hausse de demande est fausse par construction.

**S'y ajoute la baisse des teneurs.** À mesure que les gisements les plus riches sont exploités, on traite des minerais moins concentrés : il faut extraire, broyer et traiter davantage de roche pour la même quantité de métal, ce qui augmente l'énergie, l'eau et les déchets par tonne produite. Cette dérive est structurelle.

**Les trois leviers, par ordre de rapidité.**

**Réduire la quantité par unité** — le plus rapide et le plus négligé. Une reconception qui divise par deux la teneur en matériau critique équivaut à doubler l'offre, immédiatement.

**Substituer** — suppose de reconcevoir, avec souvent une perte de performance, et un délai de qualification qui se compte en années dans les secteurs réglementés.

**Recycler** — dépend du gisement disponible, c'est-à-dire de ce qui a été déployé une à deux décennies plus tôt. **Une filière en croissance rapide ne peut pas être alimentée majoritairement par le recyclage** : le stock disponible correspond à un déploiement bien plus petit. C'est arithmétique, non une question de volonté.

**Ce que cela implique.** Devant toute technologie dépendant d'un matériau concentré, les questions utiles sont : **quelle quantité par unité, quelle capacité de raffinage existe, quel délai de substitution, et quel gisement recyclable dans quinze ans**.

**Traitement neutre.** Les politiques de sécurisation d'approvisionnement et les mesures de contrôle à l'exportation relèvent de choix souverains que ce volume n'arbitre pas. Il en analyse les mécanismes : un contrôle produit un effet réel à court terme, déclenche des efforts de substitution et de recyclage à moyen terme, et a un coût pour celui qui l'impose.

**À ne pas confondre avec.** **La rareté géologique**. Un matériau critique n'est pas nécessairement rare : il est difficilement disponible, ce qui est une propriété industrielle et politique autant que géologique.

> ⏱ **État au 23/08/2026** — contrainte active. Concentration du raffinage élevée pour plusieurs matériaux stratégiques ; mesures de contrôle à l'exportation en expansion depuis 2023 ; projections de déficit sur certains métaux à horizon de la décennie. **Domaine à évolution rapide : vérification obligatoire avant toute réédition.**
> 🔄 **À revoir si** une capacité de raffinage significative entre en service hors des zones actuellement dominantes, ou si une substitution majeure est qualifiée dans une application de masse.

**Renvois** — Couche : fabriquer · Courant : Deep Tech, Climate Tech (ch. 35) · Convergences : énergie et calcul (40), autonomie mobile (39) · Voir aussi : batteries (ch. 21), semi-conducteurs à grand gap (ch. 19).

---

---


## Chapitre 20 — La biologie comme technologie

> **Périmètre de ce chapitre.** Il traite la biologie **comme moyen de production et d'intervention**, sous l'angle des mécanismes, des verrous industriels, de l'économie et de la gouvernance. Il ne décrit **aucun protocole, aucune méthode expérimentale, aucun paramètre de mise en œuvre** — y compris lorsque cette information est publiquement accessible. Cette règle s'applique phrase par phrase et sans exception.
>
> **Ce que ce chapitre ajoute à la carte de couche.** *Fabriquer* a posé le couple matériau-procédé et le rendement de production. La biologie ajoute une contrainte qu'aucun autre domaine de la couche ne connaît : **la variabilité intrinsèque du vivant**. Deux cultures conduites de façon identique ne donnent pas exactement le même résultat, et cela change la nature du contrôle qualité.
>
> **Onze entrées** — dix du registre, plus l'entrée « reproductibilité » ajoutée après le squelette de convergence, qui l'attendait sans qu'elle existe.

---

### ◆◆◆ Édition génomique

**Niveau** — capacité · **Couche** — fabriquer

**En une phrase.** Modifier une séquence d'ADN à une position choisie, dans une cellule vivante.

**Pourquoi on en parle.** Parce que c'est la capacité qui a transformé la biologie d'une science d'observation en une discipline d'intervention — et parce que le vocabulaire du domaine mélange des techniques dont la précision et les risques diffèrent nettement.

**Comment ça fonctionne — le principe commun.** Toutes les techniques modernes reposent sur un mécanisme en deux temps : un **élément de reconnaissance** programmable guide une machinerie moléculaire vers une position précise du génome, où elle intervient. C'est ce ciblage programmable qui a tout changé — auparavant, modifier une position choisie était laborieux et peu fiable.

**Trois générations, de précision croissante.**

La **coupure et réparation** intervient en coupant les deux brins d'ADN. La cellule répare ensuite par ses propres mécanismes, dont le résultat n'est pas entièrement prévisible : on oriente, on ne dicte pas. Efficace pour désactiver un gène, imprécis pour en corriger un.

L'**édition de base** modifie chimiquement une unité de l'ADN sans couper les deux brins. Plus précis, mais limité à certains types de changements.

L'**édition amorcée** permet des modifications plus variées en apportant avec l'outil une matrice de ce qu'il faut écrire. Plus polyvalent, plus complexe, et d'efficacité variable selon les contextes.

**Où vous rencontrerez le terme.** Thérapeutique · agriculture et sélection végétale · recherche fondamentale · biologie industrielle · diagnostic.

**Ce que ça permet.** Corriger, désactiver ou introduire une séquence · construire des modèles d'étude · modifier des organismes producteurs · développer des thérapies pour des maladies d'origine génétique bien caractérisée.

**Ce qui bloque — quatre difficultés, et la première est mal comprise.**

**Les effets hors cible.** L'élément de reconnaissance peut s'apparier à des positions ressemblantes ailleurs dans le génome, produisant des modifications non voulues. **Les détecter suppose de chercher des événements rares dans un très grand génome** — c'est un problème de détection de signal faible, au sens de la couche *percevoir*, et les méthodes de détection progressent moins vite que les méthodes d'édition.

**L'efficacité partielle.** Toutes les cellules d'une population ne sont pas modifiées. On obtient un mélange, et la proportion suffisante dépend entièrement de l'application.

**L'acheminement.** Amener l'outil dans les bonnes cellules d'un organisme vivant est souvent plus difficile que l'édition elle-même. **C'est le verrou dominant du thérapeutique**, et il est traité à l'entrée « thérapies géniques ».

**Le cadre.** Les régimes juridiques diffèrent fortement selon les juridictions et selon qu'il s'agit de cellules somatiques ou de la lignée germinale — cette dernière faisant l'objet de restrictions ou d'interdictions très larges.

**Ce que cela implique.** **On ne modifie pas un génome comme on modifie un fichier.** On applique un procédé dont le résultat est statistique et doit être vérifié — ce qui déplace le coût vers la validation, thème récurrent de ce chapitre.

**Sûreté et sécurité.** Le chapitre traite la biosécurité comme condition de diffusion, à l'entrée dédiée. Aucune information de mise en œuvre ne figure ici.

**À ne pas confondre avec.** **La thérapie génique**, qui est une application clinique et dont la difficulté principale est l'acheminement. **La transgénèse** classique, qui insère une séquence sans ciblage précis. **Le séquençage**, qui lit sans modifier.

> ⏱ **État au 23/08/2026** — 🏭 déployé en recherche et en agriculture selon les juridictions ; 🔬 émergent en thérapeutique, avec des autorisations obtenues sur un petit nombre d'indications bien caractérisées.
> 🔄 **À revoir si** une méthode de détection exhaustive des effets hors cible devient assez rapide et fiable pour être appliquée en routine.

**Renvois** — Couche : fabriquer · Courant : BioTech (ch. 35) · Convergence : biologie programmable (41).

---

### ◆◆◆ Biologie synthétique

**Niveau** — famille · **Couche** — fabriquer

**En une phrase.** Concevoir et assembler des systèmes biologiques aux fonctions choisies, en appliquant au vivant une démarche d'ingénierie — modularité, standardisation, réutilisation.

**Pourquoi on en parle.** Parce que c'est **le programme intellectuel qui donne son nom à la convergence du dossier 41** : passer de la découverte de fonctions biologiques à leur conception.

**Comment ça fonctionne.** L'ambition est de traiter des séquences génétiques comme des composants : des éléments qui déclenchent l'expression d'un gène, des séquences codant une fonction, des circuits qui combinent ces éléments pour produire un comportement — par exemple qu'une cellule produise une molécule uniquement en présence d'un signal donné.

Le travail se fait sur un **châssis** : un organisme hôte, souvent simplifié, dans lequel on introduit le circuit conçu.

**Ce qui distingue cette approche.** Elle vise la **réutilisabilité** : un élément caractérisé une fois devrait fonctionner de la même manière dans un autre assemblage. C'est le pari de l'ingénierie appliqué au vivant.

**Ce que ça permet.** Produire des molécules complexes par voie biologique · construire des capteurs cellulaires · concevoir des organismes producteurs pour la chimie, l'alimentation ou les matériaux.

**Ce qui bloque — et c'est là que le pari rencontre le vivant.** **La composabilité n'est pas acquise.** Un élément caractérisé isolément se comporte différemment une fois assemblé, parce que les composants partagent les ressources de la cellule et interagissent avec son métabolisme. **Le tout n'est pas la somme des parties**, et c'est la difficulté structurelle du domaine.

S'y ajoutent **la charge métabolique** — un circuit ajouté détourne des ressources et ralentit l'hôte, qui tend à éliminer la modification par sélection naturelle sur les générations —, la **variabilité** entre cellules d'une même population, et le **délai** des cycles de conception-construction-test, qui se comptent en semaines.

**Ce que cela implique.** L'automatisation des cycles expérimentaux — entrée « laboratoires autonomes » — attaque directement le dernier point. **C'est ce qui relie ce domaine à la convergence 41 : le verrou est la vitesse de la boucle, pas la capacité de conception.**

**À ne pas confondre avec.** **L'édition génomique**, qui modifie un organisme existant ; ici, on construit une fonction. **La biologie de synthèse au sens de créer la vie**, qui n'est pas le sujet et détourne l'attention des enjeux réels.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des segments 🏭 déployés en production de molécules. La composabilité reste le sujet ouvert.
> 🔄 **À revoir si** un ensemble d'éléments génétiques démontre un comportement prévisible et reproductible dans des châssis différents.

**Renvois** — Couche : fabriquer · Convergence : biologie programmable (41).

---

### ◆◆◆ Conception de protéines

**Niveau** — capacité · **Couche** — apprendre et décider, fabriquer

**En une phrase.** Concevoir la séquence d'une protéine pour qu'elle adopte une forme voulue et remplisse une fonction choisie.

**Pourquoi on en parle.** Parce que c'est **la convergence entre apprentissage automatique et biologie la plus avancée**, et parce qu'elle illustre un déplacement de goulet particulièrement net.

**Comment ça fonctionne — trois problèmes distincts, souvent confondus.**

**Prédire la forme à partir de la séquence.** Étant donné une séquence d'acides aminés, quelle structure tridimensionnelle adopte-t-elle ? Ce problème, ouvert pendant des décennies, a connu des progrès considérables.

**Concevoir une séquence pour une forme voulue** — le problème inverse. Il s'est révélé plus abordable que prévu.

**Concevoir pour une fonction.** Le plus difficile, et celui qui compte. **Connaître la forme d'une protéine ne suffit pas à connaître sa fonction** : celle-ci dépend aussi de ses partenaires, de sa localisation, de sa concentration et de son environnement chimique.

**Ce que ça permet.** Concevoir des molécules de liaison ciblant une protéine donnée · des enzymes catalysant une réaction voulue · des protéines stabilisées pour un usage industriel · des vaccins fondés sur des structures conçues.

**Ce qui bloque — et c'est le point du chapitre.** **La validation expérimentale.** Générer des candidats est devenu rapide et peu coûteux ; les tester reste lent et cher. **Le goulet s'est déplacé de la conception vers la vérification** — et il s'est aggravé, puisqu'on produit désormais plus de candidats qu'on ne peut en tester.

S'y ajoutent la **fonction contre la forme**, déjà évoquée ; le fait que les données d'entraînement sont **biaisées vers les protéines faciles à cristalliser**, donc pas représentatives ; et la difficulté de prédire le comportement dans un organisme entier plutôt qu'en tube.

**Ce que cela implique.** Le résultat contre-intuitif du dossier 37 s'applique directement : **la valeur marginale d'un meilleur modèle de conception décroît, celle d'un moyen de validation plus rapide augmente.** C'est l'inverse de la répartition actuelle de l'attention.

**À ne pas confondre avec.** **La prédiction de structure**, qui est un problème résolu à un degré utile, alors que la conception fonctionnelle ne l'est pas. Les deux sont régulièrement présentés comme un seul succès.

> ⏱ **État au 23/08/2026** — 🔬 émergent, en diffusion rapide. Outils accessibles largement ; taux de validation expérimentale des conceptions variable selon les classes de protéines et rarement publié de façon comparable.
> 🔄 **À revoir si** le taux de validation expérimentale des protéines conçues devient publié de façon standardisée, ce qui permettrait de mesurer le progrès réel.

**Renvois** — Couche : apprendre, fabriquer · Convergences : biologie programmable (41), découverte scientifique (37).

---

### ◆◆ Thérapies géniques et cellulaires

**Niveau** — famille · **Couche** — fabriquer

**En une phrase.** Traiter une maladie en modifiant les gènes d'un patient, ou en lui administrant des cellules vivantes modifiées.

**Comment ça fonctionne — deux approches distinctes.** La **thérapie génique** apporte une séquence corrective aux cellules du patient, généralement à l'aide d'un vecteur viral modifié. La **thérapie cellulaire** prélève des cellules, les modifie hors du corps, les multiplie et les réinjecte.

**Ce que ça permet.** Traiter des maladies génétiques rares sans traitement antérieur · obtenir dans certains cas une rémission durable après une administration unique · agir sur des mécanismes inaccessibles aux molécules classiques.

**Ce qui bloque — trois verrous, dans cet ordre.**

**L'acheminement.** Amener la séquence dans les bonnes cellules, en quantité suffisante, sans toucher les autres, est le problème central. Les vecteurs ont des capacités limitées, une immunogénicité, et un ciblage tissulaire imparfait.

**La production.** Ce sont des produits vivants ou biologiques, fabriqués par lot, souvent personnalisés — **chaque patient peut correspondre à un lot**. L'économie n'a rien de commun avec celle d'un médicament de synthèse, et le coût unitaire ne baisse pas par la série de la même manière.

**Le remboursement.** Un traitement administré une fois, potentiellement curatif, avec un coût très élevé et un bénéfice étalé sur des décennies, ne s'insère pas dans les mécanismes de financement conçus pour des traitements chroniques. **C'est une difficulté institutionnelle, et elle conditionne l'accès autant que la technique.**

**Ce que cela implique.** C'est un domaine où **la capacité technique est démontrée et où la diffusion est bornée par la production et le financement** — configuration que le volume 1 a rencontrée à plusieurs reprises.

**À ne pas confondre avec.** **L'édition génomique**, qui est l'outil ; ici, il s'agit de son application clinique, avec ses propres verrous.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des produits autorisés sur un nombre restreint d'indications. Extension vers des indications plus fréquentes en cours d'évaluation.
> 🔄 **À revoir si** une thérapie de ce type est autorisée pour une maladie fréquente, ce qui imposerait un changement d'échelle de production et de modèle de financement.

**Renvois** — Couche : fabriquer.

---

### ◆◆ Organoïdes et organes sur puce

**Niveau** — famille · **Couche** — fabriquer, percevoir

**En une phrase.** Des systèmes cellulaires tridimensionnels reproduisant partiellement l'organisation et la fonction d'un organe, utilisés comme modèles d'étude.

**Comment ça fonctionne.** Un **organoïde** est un agrégat de cellules qui s'auto-organise en une structure ressemblant à un organe miniature. Un **organe sur puce** est un dispositif microfluidique où des cellules sont cultivées dans un environnement contrôlé reproduisant des contraintes physiologiques — écoulement, pression, interfaces entre tissus.

**Ce que ça permet.** Tester une molécule sur du tissu humain plutôt que sur un modèle animal · étudier une maladie sur les cellules du patient · réduire le recours à l'expérimentation animale, dont la valeur prédictive pour l'humain est imparfaite.

**Ce qui bloque.** **La reproductibilité.** Deux organoïdes issus du même protocole diffèrent : c'est la variabilité intrinsèque du vivant, amplifiée par l'auto-organisation. **La maturité** : les structures obtenues correspondent souvent à un stade de développement précoce. **L'absence de système** : un organe isolé ne reproduit ni la circulation, ni le système immunitaire, ni les interactions entre organes. Et **la standardisation**, sans laquelle les résultats ne sont pas comparables entre laboratoires.

**Ce que cela implique.** Ces modèles complètent l'expérimentation animale plutôt qu'ils ne la remplacent — et leur adoption réglementaire, qui progresse, est le facteur déterminant de leur diffusion.

**À ne pas confondre avec.** **La culture cellulaire classique**, en deux dimensions, dont le comportement diffère nettement.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Usage établi en recherche ; reconnaissance réglementaire progressive comme élément de dossier.
> 🔄 **À revoir si** un dossier d'autorisation de médicament est accepté avec des données issues majoritairement de ces modèles en substitution d'études animales.

**Renvois** — Couche : fabriquer, percevoir.

---

### ◆◆◆ Bioproduction

**Niveau** — procédé · **Couche** — fabriquer

**En une phrase.** Produire une molécule ou un matériau en utilisant des organismes vivants comme usines, puis l'extraire et le purifier.

**Pourquoi cette entrée est majeure.** Parce que **c'est là que se joue l'industrialisation** de tout ce chapitre. Concevoir une fonction biologique est une chose ; en produire des tonnes en est une autre, et c'est le verrou du dossier 41.

**Comment ça fonctionne.** Un organisme modifié produit la molécule voulue. On le cultive dans un bioréacteur en contrôlant température, oxygénation, nutriments et pH. Puis on **récolte et on purifie** — le produit se trouvant mêlé à l'ensemble du contenu cellulaire.

**Ce qui bloque — quatre difficultés, toutes d'échelle.**

**La montée en volume n'est pas linéaire.** Le rapport entre surface et volume change avec la taille : dans une grande cuve, l'oxygénation, le mélange et l'évacuation de la chaleur deviennent des problèmes qui n'existaient pas en fiole. **Un procédé qui fonctionne au laboratoire ne fonctionne pas mécaniquement en bioréacteur industriel** — c'est le cinquième écart de la couche, dans sa forme la plus marquée.

**La purification domine souvent le coût.** Extraire le produit au degré de pureté requis représente fréquemment la part principale de la dépense, et davantage encore pour un usage thérapeutique.

**La variabilité biologique.** Deux cultures conduites identiquement ne donnent pas exactement le même résultat, ce qui impose un contrôle par lot bien plus lourd que pour une pièce mécanique.

**La contamination.** Un lot contaminé est perdu. Cela impose des exigences d'asepsie qui structurent la conception des installations et leur coût.

**Ce que cela implique.** La capacité de bioproduction qualifiée est **une infrastructure rare** : capital lourd, délai de construction en années, qualification réglementaire par site et par produit. **Si la conception s'accélère sans que cette capacité croisse, on produira des candidats qu'on ne saura pas fabriquer** — c'est la chronologie conditionnelle du dossier 41.

**À ne pas confondre avec.** **La chimie de synthèse**, dont l'économie et les contraintes sont différentes — reproductibilité supérieure, montée en échelle mieux maîtrisée, mais accès limité aux molécules complexes.

> ⏱ **État au 23/08/2026** — 🏭 déployé, filière mature pour les produits établis. Capacité qualifiée identifiée comme facteur limitant pour les produits nouveaux ; fermentation de précision en croissance hors du thérapeutique.
> 🔄 **À revoir si** un procédé de purification générique réduit significativement le coût de cette étape sur une classe large de produits.

**Renvois** — Couche : fabriquer · Convergence : biologie programmable (41).

---

### ◆ Bio-impression

**Niveau** — procédé · **Couche** — fabriquer

**En une phrase.** Déposer des cellules vivantes couche par couche pour construire une structure tissulaire.

**Ce qui bloque.** **La vascularisation.** Un tissu épais a besoin d'un réseau qui apporte nutriments et oxygène ; sans lui, les cellules situées au-delà de quelques centaines de micromètres de la surface meurent. **C'est la limite structurelle du domaine**, et elle explique pourquoi les réalisations concernent des tissus fins ou des modèles d'étude plutôt que des organes.

S'y ajoutent la survie cellulaire pendant le dépôt, la maturation du tissu après impression, et un cadre réglementaire pour un produit qui n'est ni un dispositif ni un médicament classique.

**Ce que cela implique.** Les usages réels sont **les modèles de test** — tissus pour évaluer une molécule — plutôt que la greffe. L'écart entre les deux est considérable et souvent effacé dans la présentation.

> ⏱ **État au 23/08/2026** — 🔭 prospectif pour la greffe d'organes, 🔬 émergent pour les modèles de test et les tissus fins.
> 🔄 **À revoir si** un tissu vascularisé épais survit et fonctionne dans un organisme sur une durée significative.

**Renvois** — Couche : fabriquer.

---

### ◆◆◆ Laboratoires autonomes

**Niveau** — système · **Couche** — fabriquer, percevoir, décider

**En une phrase.** Des installations où la conception d'expériences, leur exécution, la mesure et l'analyse s'enchaînent automatiquement, en boucle fermée.

**Pourquoi cette entrée est majeure.** Parce qu'elle attaque le goulet identifié dans ce chapitre et dans tout le dossier 37 : **la vitesse de la boucle expérimentale**.

**Comment ça fonctionne.** Une plateforme robotisée exécute les manipulations, des instruments mesurent les résultats, et un système de décision choisit l'expérience suivante en fonction de ce qui a été observé. La boucle **hypothèse → expérience → mesure → hypothèse** tourne sans intervention, jour et nuit.

**Le point qui compte** n'est pas la robotique — les automates de laboratoire existent depuis longtemps — mais **la fermeture de la boucle** : c'est le système qui décide quoi tester ensuite, ce qui change la nature de l'exploration.

**Ce que ça permet.** Explorer des espaces de paramètres bien plus vastes que ne le permettrait le travail manuel · réduire le délai entre hypothèse et résultat · obtenir des données produites dans des conditions identiques, donc comparables — ce qui est en soi précieux.

**Ce qui bloque.** **La manipulation physique.** Pipeter, transférer, peser, ouvrir un flacon — ce sont des tâches de manipulation, avec la difficulté établie au chapitre 14. **La diversité des protocoles** : une plateforme est configurée pour une famille d'expériences et ne se reconfigure pas trivialement. **Le coût d'installation**, qui limite l'accès à quelques acteurs. Et **la mesure** : automatiser l'exécution ne sert à rien si la caractérisation reste lente et manuelle.

**Ce que cela implique.** L'automatisation déplace le goulet **vers ce qui n'est pas automatisé**. Si l'exécution s'accélère et que la caractérisation reste lente, le gain est faible. **La question à poser devant tout laboratoire autonome est : quelle étape reste manuelle ?**

**À ne pas confondre avec.** **L'automatisation de laboratoire** classique, qui exécute un protocole défini sans décider de la suite. La différence est la boucle fermée, et elle est décisive.

**Termes voisins.** *Self-driving labs* désigne exactement la même chose — deux noms pour un objet, et il n'y a pas lieu d'en distinguer deux familles.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Installations opérationnelles chez un petit nombre d'acteurs académiques et industriels, principalement en chimie et en matériaux ; extension à la biologie plus lente en raison de la variabilité et de la durée des expériences.
> 🔄 **À revoir si** une plateforme de ce type réduit d'un ordre de grandeur le coût d'un cycle expérimental complet dans un domaine à validation lente.

**Renvois** — Couche : fabriquer, décider · Convergences : découverte scientifique (37), biologie programmable (41).

---

### ◆◆ Découverte de médicaments assistée

**Niveau** — capacité · **Couche** — apprendre et décider, fabriquer

**En une phrase.** Utiliser des méthodes prédictives pour identifier, sélectionner et optimiser des candidats médicaments avant de les tester.

**Ce que ça permet.** Réduire le nombre de molécules à synthétiser et tester · explorer des espaces chimiques plus vastes · prédire certaines propriétés — toxicité, solubilité, stabilité — avant la synthèse · réutiliser des molécules existantes pour de nouvelles indications.

**Ce qui bloque — et c'est une leçon d'échelle.** **L'attrition clinique.** La majorité des candidats échoue en développement, et l'échec est concentré aux étapes les plus coûteuses — précisément celles où la prédiction est la moins fiable, parce qu'elles portent sur l'efficacité et la sécurité chez l'humain.

**Accélérer les premières étapes ne change donc pas grand-chose au coût total.** Les phases précliniques représentent une fraction modeste de la dépense et du temps ; le goulet est en clinique, et il est irréductible pour des raisons de recrutement de patients, de durée d'observation et de cadre réglementaire.

**Ce que cela implique.** C'est le cas le plus net du volume où **améliorer l'étape amont d'un processus ne déplace pas son goulet**. Une accélération de dix fois en amont produit un gain marginal si l'aval représente l'essentiel du coût — application directe du raisonnement du volume 1.

**À ne pas confondre avec.** **La conception de protéines**, qui est un problème de conception moléculaire ; ici, il s'agit d'un processus de développement complet, dont la partie moléculaire est minoritaire en coût.

> ⏱ **État au 23/08/2026** — 🏭 déployé en phase amont, avec des candidats issus de ces méthodes en évaluation clinique. Effet mesurable sur le taux de succès global non établi.
> 🔄 **À revoir si** des candidats issus de ces méthodes montrent un taux de succès clinique supérieur à la référence historique sur un nombre significatif de programmes.

**Renvois** — Couche : apprendre et décider, fabriquer.

---

### ◆◆ Reproductibilité et réplication

**Niveau** — contrainte méthodologique · **Couche** — fabriquer, vérifier

**En une phrase.** La capacité d'un résultat scientifique à être obtenu de nouveau — par la même équipe, ou par une autre.

**Pourquoi cette entrée existe.** Elle n'était pas au registre initial. Elle a été ajoutée parce que le dossier de convergence 37 l'attendait sans qu'elle existe : **on ne peut pas raisonner sur l'accélération de la découverte sans savoir ce que vaut un résultat.**

**Deux notions à distinguer.** La **reproductibilité** — obtenir le même résultat avec les mêmes données et le même protocole. La **réplication** — obtenir le même résultat par une expérience indépendante. La seconde est bien plus exigeante et bien plus rare.

**Ce que les données montrent.** Une enquête publiée en 2016 auprès d'un large échantillon de chercheurs indiquait que plus de sept sur dix avaient échoué à reproduire l'expérience d'un autre, et plus de la moitié la leur. Les programmes de réplication systématique conduits depuis donnent des ordres de grandeur convergents et médiocres : **environ un tiers à deux tiers de résultats répliqués selon les domaines et les critères** — le programme de réplication en psychologie publié en 2015 se situe au bas de cette fourchette, l'économie expérimentale et la science sociale expérimentale nettement plus haut, la biologie du cancer entre les deux. ⏱

**Trois nuances qui comptent, et elles pèsent plus que les taux.** Un échec de réplication **n'établit pas que le résultat initial était faux** — il peut résulter d'une différence de conditions non documentée, ou d'une puissance statistique insuffisante de la réplication elle-même, ce que plusieurs analyses postérieures ont montré. **Les taux ne sont pas comparables entre eux** : ils dépendent du critère retenu — significativité de même signe, taille d'effet dans l'intervalle de confiance, jugement d'ensemble — et changer de critère déplace un même corpus de plusieurs dizaines de points. Et **les disciplines les mieux classées ne sont pas nécessairement les plus rigoureuses** : elles étudient souvent des systèmes moins variables, ce qui est une propriété de l'objet avant d'être une propriété de la méthode.

**Ce qu'on peut affirmer sans excès.** Que le problème est réel, transversal et mesuré ; qu'il touche des domaines réputés durs autant que les sciences humaines ; et qu'**aucun classement fin des disciplines par taux de réplication n'est solide**, parce que les protocoles de mesure ne sont pas les mêmes.

**Ce qui explique la difficulté en biologie.** La variabilité intrinsèque du vivant · la sensibilité à des conditions non documentées — lignée cellulaire, lot de réactif, opérateur · l'absence de description exhaustive des protocoles · et des incitations qui favorisent la publication de résultats positifs et nouveaux plutôt que la vérification.

**Ce que cela implique — et c'est le point pour ce volume.** L'échelon « réplication indépendante » de l'échelle des preuves a ici **un poids particulier**. Un résultat unique, même publié, y a un statut plus faible qu'ailleurs. La question à poser est : **cela a-t-il été reproduit par une autre équipe, avec un autre lot ?**

Et pour la convergence 37 : **une accélération de la production de résultats qui ne s'accompagne pas d'une amélioration de la reproductibilité produit du volume, non de la connaissance.**

**À ne pas confondre avec.** **La fraude**, qui est marginale ; l'essentiel du problème relève de la variabilité, de la documentation incomplète et des incitations.

> ⏱ **État au 23/08/2026** — contrainte active. Pratiques d'amélioration en diffusion — préenregistrement, partage de données et de protocoles, revues de réplication — sans qu'un effet global soit établi.
> 🔄 **À revoir si** un taux de réplication mesuré progresse significativement dans une discipline majeure sur une période de plusieurs années.

**Renvois** — Couche : fabriquer, vérifier · Convergences : découverte scientifique (37), biologie programmable (41) · Voir aussi : chapitre 4.

---

### ◆◆ Biosécurité

**Niveau** — contrainte et gouvernance · **Couche** — vérifier

**En une phrase.** L'ensemble des dispositions visant à prévenir les usages dangereux, les accidents et les diffusions non maîtrisées liés aux technologies du vivant.

**Pourquoi cette entrée figure dans l'atlas.** Parce que **c'est une condition de diffusion au même titre que le coût ou la réglementation**, et non un supplément moral. Une capacité dont la gouvernance n'est pas établie ne se déploie pas — ou se déploie dans un contexte d'incertitude qui décourage l'investissement.

**Ce que le terme recouvre — trois registres distincts.** La **sécurité biologique en laboratoire** : niveaux de confinement, procédures, formation, protection des personnels et de l'environnement. La **sûreté biologique** au sens de la prévention des usages malveillants : contrôle d'accès aux agents et aux équipements, vérification des commandes de séquences, contrôles à l'exportation. Et la **gouvernance** : cadres nationaux et internationaux, normes professionnelles, mécanismes d'évaluation des recherches à risque.

**Ce qui rend le sujet difficile.** **La double nature de l'information.** Une même connaissance peut servir à protéger et à nuire, et elle se diffuse par publication scientifique — dont l'ouverture est par ailleurs un principe. Les mécanismes d'évaluation existent et sont diversement appliqués selon les pays et les institutions.

**La diffusion des capacités.** Les outils de synthèse et d'édition sont devenus accessibles et peu coûteux, ce qui déplace la question du contrôle des équipements vers celui des intrants et des services.

**Et l'asymétrie des rythmes.** Les capacités progressent plus vite que les cadres, ce qui est le mécanisme général du volume 1 appliqué ici.

**Ce que cela implique.** Toute analyse de trajectoire dans ce domaine doit inclure la gouvernance comme variable, au même titre que le coût ou la capacité de production. **Un durcissement du cadre est un facteur de trajectoire aussi déterminant qu'une percée technique** — le volume 1 l'a établi sur d'autres filières.

**Traitement dans ce volume.** Principes, enjeux industriels et gouvernance uniquement. **Aucune information de mise en œuvre, aucun agent, aucune méthode, aucun paramètre.** Cette règle n'admet aucune exception, y compris pour des informations publiquement accessibles.

**À ne pas confondre avec.** **La bioéthique**, qui traite de l'acceptabilité morale des usages — question légitime, distincte, et que ce volume n'arbitre pas.

> ⏱ **État au 23/08/2026** — contrainte active. Cadres nationaux hétérogènes ; travaux internationaux en cours sur la vérification des commandes de séquences et sur l'évaluation des recherches à risque.
> 🔄 **À revoir si** un mécanisme de vérification devient une pratique standard chez la majorité des fournisseurs de synthèse.

**Renvois** — Couche : vérifier · Convergence : biologie programmable (41).

---


## Clôture de la couche E — Fabriquer

### Ce que les vingt-quatre entrées font apparaître

**Un. Le temps est le verrou dominant de cette couche**, et à trois échelles emboîtées. Quinze à vingt ans pour développer une mine. Une à deux décennies entre la découverte d'un matériau et sa disponibilité industrielle. Des années pour qualifier un procédé dans un secteur réglementé. **Aucune contrainte technique de cette couche n'est aussi structurante que ces délais**, et aucun financement ne les raccourcit substantiellement.

**Deux. Le goulet s'est déplacé de la conception vers la validation dans tout le chapitre 20.** Conception de protéines, biologie synthétique, découverte de médicaments, laboratoires autonomes : quatre entrées portent le même constat. Générer des candidats est devenu rapide ; les vérifier reste lent. **C'est la thèse centrale du dossier 37, retrouvée dans quatre entrées rédigées séparément.**

**Trois. Trois entrées de cette couche décrivent une contrainte plutôt qu'un objet** — matériaux critiques, reproductibilité, biosécurité. C'est la proportion la plus élevée de l'atlas, et elle est cohérente : *fabriquer* est la couche où l'on rencontre le monde matériel, réglementaire et institutionnel dans toute son épaisseur.

**Quatre. La variabilité du vivant n'a pas d'équivalent ailleurs.** Elle apparaît dans six entrées et impose un contrôle par lot que ne connaît aucune autre production. **C'est ce qui rend la biologie industrielle structurellement différente de la chimie**, et non son ambition ou sa nouveauté.

### Ce que la couche livre aux convergences

| Dossier | Entrées mobilisées |
|---|---|
| **37 — Découverte scientifique** | laboratoires autonomes, conception de protéines, reproductibilité, métrologie, fabrication additive |
| **40 — Énergie et calcul** | semi-conducteurs à grand gap, matériaux critiques |
| **41 — Biologie programmable** | édition, biologie synthétique, conception de protéines, thérapies, bioproduction, laboratoires autonomes, biosécurité, reproductibilité |

**Le dossier 41 mobilise huit entrées de cette seule couche** — la dépendance la plus concentrée de tout l'atlas. Et son maillon en retard, la montée en échelle de production, appartient **à cette même couche**. **C'est la seconde contradiction partielle de la thèse du volume**, et elle se confirme comme prévu au squelette.

---

---

---

### Couche F — Alimenter

---


## Chapitre 21 — Stockage électrochimique

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé deux contraintes : densité d'énergie et densité de puissance s'opposent presque toujours, et les rendements se multiplient le long d'une chaîne. Ce chapitre traite du **stockage électrochimique**, c'est-à-dire de la manière la plus répandue de transporter de l'énergie électrique dans le temps.
>
> **Une grille de lecture commune aux six entrées.** Toute technologie de stockage se juge sur six grandeurs, et jamais sur une seule : **énergie massique · énergie volumique · puissance · durée de vie en cycles · coût par kilowattheure · sécurité**. Une technologie qui gagne sur l'une perd presque toujours sur une autre. **Comparer deux stockages par la seule densité énergétique est l'erreur la plus fréquente du domaine.**

---

### ◆◆◆ Lithium-ion et ses chimies

**Niveau** — composant · **Couche** — alimenter

**En une phrase.** La famille de batteries qui domine le stockage électrochimique, et qui recouvre plusieurs chimies aux propriétés nettement différentes.

**Pourquoi on en parle.** Parce que c'est **la référence de comparaison de tout le domaine** — toute nouvelle technologie de stockage se juge par rapport à elle — et parce que le terme désigne une famille et non un produit.

**Comment ça fonctionne.** Des ions lithium se déplacent d'une électrode à l'autre à travers un électrolyte, tandis que les électrons empruntent le circuit extérieur : c'est ce déplacement d'électrons qui constitue le courant utile. La charge inverse le processus.

**Les chimies diffèrent par le matériau d'électrode positive**, et cette différence commande tout le compromis. Certaines privilégient l'énergie massique, au prix d'une durée de vie moindre, d'un coût supérieur et de matériaux plus contraints. D'autres privilégient la durée de vie, la sécurité thermique et le coût, au prix d'une densité énergétique inférieure — ce qui les rend adaptées au stationnaire et aux usages où la masse importe peu.

**Ce qui limite une batterie — cinq facteurs, dans l'ordre d'importance pratique.**

**Les interfaces.** C'est aux frontières entre électrodes et électrolyte que se produit l'essentiel des dégradations. Ce n'est pas le matériau actif qui vieillit d'abord, c'est la surface.

**Le cyclage.** Chaque cycle dégrade légèrement ; la durée de vie se compte en cycles, pas en années — c'est la fatigue au sens du volume 1.

**La température.** Le froid réduit temporairement les performances ; la chaleur accélère durablement la dégradation.

**La puissance de charge.** Charger vite dégrade davantage : c'est un arbitrage direct entre confort d'usage et durée de vie, et il est rarement présenté comme tel.

**L'emballement thermique.** Une dégradation locale échauffe, l'échauffement accélère la dégradation, et la boucle peut devenir incontrôlable. **C'est pourquoi la sécurité d'un pack est un problème de conception système** — détecter, isoler, refroidir, empêcher la propagation d'une cellule à ses voisines — et non un problème de chimie seule.

**Ce que cela implique — une distinction de niveau essentielle.** Les caractéristiques annoncées portent généralement sur la **cellule**. Un module ajoute structure, connectique et refroidissement ; un pack complet ajoute électronique de surveillance et protections. **La densité énergétique effective d'un pack est significativement inférieure à celle de ses cellules.** Comparer une densité de cellule à un besoin de véhicule est une erreur de niveau au sens du chapitre 2.

**Où vous rencontrerez le terme.** Véhicules · électronique portable · stockage stationnaire · outillage · aéronautique légère · plateformes robotiques.

**Ce qui bloque.** **Les matériaux**, pour les chimies dépendant d'éléments à approvisionnement concentré. **Le coût**, qui a fortement baissé et dont la poursuite dépend de la chimie retenue. **La recharge rapide**, limitée par la dégradation et par la puissance disponible au point de charge — le calcul du volume 1 le rappelait : recharger vite est d'abord un problème de raccordement électrique. Et **la fin de vie**, dont l'organisation conditionne l'accès futur aux matériaux.

**À ne pas confondre avec.** **Les batteries solides**, traitées séparément, qui sont une évolution de cette famille et non une famille distincte. **Les supercondensateurs**, dont le compromis est opposé.

> ⏱ **État au 23/08/2026** — 🏭 déployé, technologie dominante. Baisse de coût continue, part croissante des chimies sans matériaux les plus contraints, capacité de production concentrée géographiquement.
> 🔄 **À revoir si** une chimie alternative atteint simultanément le coût, la durée de vie et la densité des meilleures chimies actuelles.

**Renvois** — Couche : alimenter · Convergences : robotique généraliste (36), autonomie mobile (39) · Voir aussi : matériaux critiques (ch. 19).

---

### ◆◆◆ Batteries solides

**Niveau** — composant · **Couche** — alimenter

**En une phrase.** Des batteries dont l'électrolyte liquide est remplacé par un matériau solide.

**Pourquoi on en parle.** Parce que c'est **la promesse la plus annoncée du secteur énergétique** depuis une dizaine d'années — et parce que l'écart entre les annonces et l'industrialisation en fait un cas d'école pour ce volume.

**Ce que cela apporterait.** Trois gains, souvent présentés ensemble alors qu'ils ne s'obtiennent pas simultanément. **La sécurité** : un électrolyte solide n'est pas inflammable, ce qui réduit le risque d'emballement thermique. **La densité énergétique** : le solide permettrait d'utiliser une électrode négative en lithium métallique, à forte capacité. **La recharge rapide** : certains électrolytes solides tolèrent des courants élevés.

**Ce qui bloque — et le verrou n'est pas celui qu'on croit.** Le problème n'est pas de trouver un électrolyte solide conducteur : plusieurs familles existent et fonctionnent. **Le problème est l'interface.**

Un liquide épouse spontanément la surface des électrodes ; un solide ne le fait pas. Il faut donc maintenir un contact intime entre deux solides, sur une grande surface, **pendant que les électrodes changent de volume à chaque cycle**. Le contact se dégrade, la résistance augmente, la capacité chute.

S'y ajoutent la **croissance de dendrites** — des filaments métalliques qui traversent l'électrolyte et court-circuitent la cellule, phénomène que le solide devait empêcher et qu'il n'empêche pas toujours —, la **pression mécanique** que certaines conceptions exigent en fonctionnement, et surtout **la fabrication** : produire de grandes surfaces d'électrolyte solide sans défaut, à cadence industrielle, est un problème de procédé non résolu.

**Ce que cela implique.** Le verrou est **industriel et interfacial**, non fondamental. C'est une configuration où le principe est démontré depuis longtemps et où la production ne suit pas — cas fréquent au volume 1, et qui se reconnaît à un signe : les annonces portent sur des cellules de démonstration et non sur des lignes de production qualifiées.

**Le signal à surveiller n'est donc pas une performance de cellule** mais l'entrée en service d'une ligne de production en série avec un rendement publié.

**À ne pas confondre avec.** Les batteries à électrolyte **semi-solide** ou gélifié, souvent présentées sous le même terme, qui conservent une phase liquide et n'ont ni les mêmes promesses ni les mêmes difficultés. **Cette confusion est fréquente et commode.**

> ⏱ **État au 23/08/2026** — 🔬 émergent. Cellules de démonstration à performances élevées ; premières applications de niche ; production de série pour l'automobile annoncée à plusieurs reprises et repoussée. Le rendement de fabrication reste le sujet.
> 🔄 **À revoir si** une ligne de production en série publie un rendement de fabrication stable sur plusieurs mois.

**Renvois** — Couche : alimenter · Convergence : autonomie mobile (39).

---

### ◆◆ Sodium-ion

**Niveau** — composant · **Couche** — alimenter

**En une phrase.** Des batteries fonctionnant sur le même principe que le lithium-ion, avec du sodium à la place du lithium.

**Pourquoi on en parle.** Parce que c'est **une réponse à une contrainte d'approvisionnement plutôt qu'à une contrainte de performance** — configuration rare et instructive.

**Ce que ça apporte.** Le sodium est abondant, largement distribué et peu coûteux. La chimie tolère mieux le froid, supporte des charges rapides, et présente un meilleur comportement en sécurité. **Elle peut aussi être déchargée complètement pour le transport**, ce qui simplifie la logistique.

**Ce qui bloque.** **La densité énergétique**, structurellement inférieure — le sodium est plus lourd et plus volumineux que le lithium, et cet écart est physique, non conjoncturel. **La maturité industrielle** : les chaînes sont récentes et les volumes faibles, donc le coût réel n'a pas encore bénéficié de l'apprentissage. Et **la comparaison mouvante** : la baisse continue du coût du lithium-ion déplace en permanence le seuil où le sodium devient avantageux.

**Ce que cela implique.** Cette technologie ne vise pas les applications où la masse domine. Elle vise **le stationnaire, les usages à faible autonomie et les marchés sensibles au coût et à l'approvisionnement** — et son avenir dépend autant du prix du lithium que de ses propres progrès.

**À ne pas confondre avec.** Une technologie de remplacement du lithium-ion. Les deux sont complémentaires par leurs compromis.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des premières productions en série et des déploiements en stationnaire et en mobilité légère.
> 🔄 **À revoir si** le coût par kilowattheure passe durablement sous celui des chimies lithium les moins chères à volume comparable.

**Renvois** — Couche : alimenter.

---

### ◆◆ Batteries à flux

**Niveau** — composant · **Couche** — alimenter

**En une phrase.** Un stockage où l'énergie est contenue dans des liquides stockés en réservoirs séparés, que l'on fait circuler à travers une cellule de conversion.

**Pourquoi cette architecture est intéressante.** Parce qu'elle **découple la puissance de l'énergie**. La puissance dépend de la taille de la cellule ; l'énergie dépend du volume des réservoirs. On peut donc dimensionner l'une sans toucher à l'autre — ce qu'aucune batterie conventionnelle ne permet, sa capacité et sa puissance étant liées par construction.

**Ce que ça permet.** Un stockage de longue durée à coût marginal faible — ajouter des heures de stockage revient à agrandir un réservoir · une durée de vie très élevée, les liquides ne se dégradant pas comme des électrodes solides · une sécurité intrinsèque.

**Ce qui bloque.** **La densité énergétique**, très faible : c'est une technologie encombrante, exclusivement stationnaire. **Le coût des matériaux actifs** pour certaines chimies. **La complexité mécanique** — pompes, membranes, circuits — qui introduit des modes de panne absents d'une batterie classique. Et **la concurrence du lithium-ion**, dont la baisse de coût a envahi une partie du marché stationnaire visé.

**Ce que cela implique.** La pertinence de cette famille se joue sur **la durée de stockage visée**. En dessous de quelques heures, le lithium-ion domine ; au-delà, le découplage devient un avantage décisif. **Le seuil se déplace avec les prix relatifs**, ce qui rend la comparaison instable.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des installations en service et une croissance liée aux besoins de stockage longue durée.
> 🔄 **À revoir si** un besoin réglementaire de stockage de plusieurs heures devient obligatoire dans un marché électrique majeur.

**Renvois** — Couche : alimenter.

---

### ◆ Supercondensateurs

**Niveau** — composant · **Couche** — alimenter

**En une phrase.** Un stockage qui accumule les charges électriques à la surface d'électrodes, sans réaction chimique — ce qui le rend très rapide et peu capacitif.

**Ce que ça permet.** Une densité de puissance très supérieure aux batteries · des centaines de milliers de cycles sans dégradation notable · un fonctionnement à basse température.

**Ce qui bloque.** **La densité énergétique**, inférieure d'un à deux ordres de grandeur à celle d'une batterie. Ce n'est pas un défaut à corriger : c'est la conséquence du principe physique.

**Ce que cela implique.** Ce n'est pas un concurrent des batteries mais un **complément** : les deux sont souvent associés, la batterie fournissant l'énergie et le supercondensateur les pointes de puissance. **C'est l'illustration la plus nette de l'opposition entre densité d'énergie et densité de puissance** posée par la carte de couche.

**À ne pas confondre avec.** Une batterie à charge rapide, qui reste une batterie.

> ⏱ **État au 23/08/2026** — 🏭 déployé, applications établies en récupération d'énergie, en transport et en industrie.
> 🔄 **À revoir si** une technologie hybride atteint simultanément la puissance d'un supercondensateur et une fraction significative de l'énergie d'une batterie.

**Renvois** — Couche : alimenter.

---

### ◆◆ Stockage longue durée non électrochimique

**Niveau** — famille · **Couche** — alimenter

**En une phrase.** Stocker de l'énergie pendant des heures, des jours ou des saisons par des moyens mécaniques, thermiques ou chimiques.

**Pourquoi cette entrée existe.** Parce que **le stockage électrochimique ne couvre pas les longues durées**, et que la question du stockage saisonnier est distincte de celle du stockage journalier — les deux étant régulièrement confondues.

**Les familles.** Le **stockage hydraulique par pompage**, de loin le plus déployé, dont la limite est la disponibilité de sites. Le **stockage thermique**, qui accumule de la chaleur — sensible ou latente — pour la restituer plus tard, avec un rendement élevé si l'usage final est thermique et médiocre s'il faut repasser par l'électricité. Le **stockage mécanique** — air comprimé, gravitaire, volants d'inertie. Et le **stockage chimique**, sous forme d'hydrogène ou de molécules de synthèse, seul candidat crédible pour le saisonnier mais au rendement aller-retour faible.

**La grandeur qui structure tout.** **Le coût par unité d'énergie stockée**, et non par unité de puissance. Pour un stockage de longue durée, ajouter des heures doit coûter peu — ce qui favorise les technologies où le réservoir est bon marché et pénalise celles où la capacité est liée au dispositif de conversion.

**Ce qui bloque.** Pour l'hydraulique, **les sites**. Pour le thermique, **la valeur de la chaleur restituée**, qui dépend entièrement de sa température. Pour le chimique, **le rendement cumulé** — le volume 1 l'a chiffré, une chaîne électricité-molécule-électricité perd l'essentiel en route. Et pour tous, **le modèle économique** : un stockage utilisé quelques fois par an amortit mal, ce qui est la difficulté centrale du saisonnier.

**Ce que cela implique.** **Il n'y a pas une question du stockage mais plusieurs**, selon la durée visée — minutes, heures, jours, saisons. Les technologies pertinentes diffèrent complètement d'une échelle à l'autre, et une affirmation sur « le stockage » sans précision de durée n'est pas exploitable.

**À ne pas confondre avec.** Le stockage de puissance, destiné à absorber des variations rapides.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour l'hydraulique et le thermique industriel, 🔬 émergent pour les autres familles à l'échelle réseau.
> 🔄 **À revoir si** une technologie de stockage de plusieurs jours atteint un coût par kilowattheure stocké compétitif avec les moyens pilotables.

**Renvois** — Couche : alimenter · Voir aussi : hydrogène (ch. 22), réseaux pilotés (ch. 23) · **Ce sujet est le domaine retenu pour le protocole final du chapitre 47.**

---
