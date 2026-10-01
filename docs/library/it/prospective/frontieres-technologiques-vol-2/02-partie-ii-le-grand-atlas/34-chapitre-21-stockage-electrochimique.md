---
title: Chapitre 21 — Stockage électrochimique
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie II — Le grand atlas
  - index.md
---

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé deux contraintes : densité d'énergie et densité de puissance s'opposent presque toujours, et les rendements se multiplient le long d'une chaîne. Ce chapitre traite du **stockage électrochimique**, c'est-à-dire de la manière la plus répandue de transporter de l'énergie électrique dans le temps.
>
> **Une grille de lecture commune aux six entrées.** Toute technologie de stockage se juge sur six grandeurs, et jamais sur une seule : **énergie massique · énergie volumique · puissance · durée de vie en cycles · coût par kilowattheure · sécurité**. Une technologie qui gagne sur l'une perd presque toujours sur une autre. **Comparer deux stockages par la seule densité énergétique est l'erreur la plus fréquente du domaine.**

---

## ◆◆◆ Lithium-ion et ses chimies

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

## ◆◆◆ Batteries solides

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

## ◆◆ Sodium-ion

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

## ◆◆ Batteries à flux

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

## ◆ Supercondensateurs

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

## ◆◆ Stockage longue durée non électrochimique

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
