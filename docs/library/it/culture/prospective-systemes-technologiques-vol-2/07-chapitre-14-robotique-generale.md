---
title: Chapitre 14 — Robotique générale
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
chapter: 7
chapters: 14
---

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé deux contraintes : la boucle masse-énergie, qui borne toute machine emportant son énergie, et le fait que manipuler est structurellement plus difficile que se déplacer. Ce chapitre traite des **familles de machines** et de ce qui les sépare.
>
> **Un principe de classement.** Les entrées ne sont pas ordonnées par degré d'avancement mais par **environnement d'opération** — du plus structuré au moins structuré. C'est la variable qui décide de la difficulté, bien avant la sophistication de la machine.
>
> **Huit entrées.**

---

### ◆◆ Robotique industrielle et cobots

**Niveau** — plateforme · **Couche** — agir

**En une phrase.** Des machines à trajectoire programmée opérant dans un environnement conçu autour d'elles — et, pour les cobots, dans un espace partagé avec des humains.

**Pourquoi on en parle.** Parce que c'est **la base installée de référence**, celle à laquelle toute nouvelle promesse robotique se compare — et parce que ses limites expliquent ce que les autres familles tentent de dépasser.

**Comment ça fonctionne.** Un bras articulé répète une trajectoire avec une précision élevée et une répétabilité remarquable. La perception, quand elle existe, sert à confirmer une position attendue plutôt qu'à découvrir une scène. **L'environnement est adapté à la machine**, pas l'inverse : pièces présentées en position connue, éclairage maîtrisé, zone délimitée.

Le **cobot** modifie un paramètre : il est conçu pour opérer sans barrière, avec une limitation de vitesse et de force et une détection de contact. Il échange de la performance contre de la coexistence.

**Où vous rencontrerez le terme.** Automobile · électronique · agroalimentaire · logistique · laboratoires · machines-outils.

**Ce que ça permet.** Une cadence et une répétabilité que l'humain n'atteint pas · un fonctionnement continu · une qualité constante sur des séries longues.

**Ce qui bloque.** **Le coût d'intégration**, qui dépasse souvent celui de la machine : préhenseurs spécifiques, adaptation du poste, programmation, sécurité, formation. C'est pourquoi la robotisation reste économiquement liée à la longueur des séries. S'y ajoute **l'inflexibilité** : changer de produit suppose de reprogrammer et souvent de réoutiller.

Pour le cobot, la limitation de vitesse réduit la cadence, ce qui restreint son domaine de rentabilité.

**Ce que cela implique.** La question pertinente n'est jamais « robot ou humain » mais **à partir de quelle taille de série l'intégration s'amortit**. C'est cette frontière que les familles suivantes cherchent à déplacer.

**À ne pas confondre avec.** **La robotique collaborative** au sens d'une machine qui coopère : un cobot partage un espace, il ne collabore pas à une tâche. **L'automatisation** au sens large, qui n'implique pas de machine mobile.

> ⏱ **État au 23/08/2026** — 🏭 déployé, filière mature. Croissance tirée par les cobots et par les séries plus courtes ; densité de robots très inégale selon les pays et les secteurs.
> 🔄 **À revoir si** le coût d'intégration par poste baisse d'un facteur significatif — ce qui déplacerait le seuil de série rentable.

**Renvois** — Couche : agir · Convergence : robotique généraliste (36).

---

### ◆◆ Robots mobiles autonomes

**Niveau** — plateforme · **Couche** — agir, percevoir

**En une phrase.** Des machines qui se déplacent seules dans un environnement partiellement structuré — entrepôt, atelier, hôpital — pour transporter, inspecter ou nettoyer.

**Comment ça fonctionne.** Deux générations coexistent, et leur confusion est fréquente. Les **véhicules à guidage automatique** suivent une infrastructure physique — bande magnétique, rail, marquage au sol — et s'arrêtent devant un obstacle. Les **robots mobiles autonomes** construisent et utilisent une carte, se localisent dedans et **contournent** un obstacle plutôt que de s'arrêter.

La différence est économique autant que technique : le premier exige d'équiper le bâtiment, le second de cartographier.

**Ce que ça permet.** Automatiser le transport interne sans modifier l'infrastructure · s'adapter à des flux variables · cohabiter avec des humains et des chariots.

**Ce qui bloque.** **La gestion de flotte** plus que la machine : coordonner des dizaines d'unités, éviter les blocages mutuels, gérer la recharge et les priorités. **Les environnements encombrés et changeants**, où la carte se périme. Et **la manipulation** : un robot mobile transporte, il ne charge ni ne décharge — le maillon final reste humain dans la plupart des déploiements.

**Ce que cela implique.** C'est la famille robotique dont le déploiement est le plus large et le moins visible. **Elle démontre que l'autonomie de déplacement est un problème résolu en environnement semi-structuré** — ce qui isole précisément ce qui ne l'est pas : saisir et poser.

**À ne pas confondre avec.** **Les véhicules autonomes routiers** (ch. 17), dont l'environnement n'est pas structuré et dont les conséquences d'erreur sont sans commune mesure.

> ⏱ **État au 23/08/2026** — 🏭 déployé, en croissance. Standardisation progressive de l'interopérabilité entre flottes de fournisseurs différents.
> 🔄 **À revoir si** une plateforme mobile intègre une capacité de manipulation fiable en environnement d'entrepôt non préparé.

**Renvois** — Couche : agir · Convergence : robotique généraliste (36).

---

### ◆◆◆ Manipulation et préhension

**Niveau** — capacité · **Couche** — agir

**En une phrase.** Saisir, déplacer, orienter et poser un objet dont on ne connaît pas exactement les propriétés — et c'est le verrou central de toute la couche.

**Pourquoi on en parle.** Parce que **c'est ce qui sépare une machine qui se déplace d'une machine qui travaille**, et parce que la difficulté est constamment sous-estimée par ceux qui observent des démonstrations.

**Comment ça fonctionne — et pourquoi c'est difficile.** Quatre raisons, qui n'existent pas dans le déplacement.

**Le contact change brutalement la dynamique.** Tant qu'il n'y a pas contact, la machine bouge librement ; à l'instant du contact, les forces changent discontinûment. Un régulateur réglé pour le mouvement libre est inadapté au contact, et réciproquement — il faut donc détecter la transition et changer de régime, ce qui est un problème de commande difficile.

**Il faut contrôler des forces, pas seulement des positions.** Serrer trop fort abîme, pas assez fait glisser. Cela suppose de mesurer des efforts, ce qui est plus bruité et plus lent que mesurer une position.

**Les objets diffèrent alors qu'ils se ressemblent.** Deux objets d'apparence identique peuvent avoir des masses, des rigidités et des coefficients de frottement différents. **La perception visuelle ne renseigne pas sur la masse ni sur le frottement** — il faut le découvrir en touchant.

**Certaines erreurs sont irréversibles.** Un objet lâché tombe, un objet cassé est cassé. Contrairement au déplacement, où l'on corrige en continu, la manipulation comporte des instants sans rattrapage.

**Ce qui bloque, en pratique.** Le taux de succès. Une démonstration montre une saisie réussie ; une exploitation exige un taux d'échec assez faible pour que le traitement des échecs ne coûte pas plus que le gain. **L'écart entre les deux se compte en ordres de grandeur**, et il n'est pas visible dans une vidéo.

**Ce que cela implique pour votre lecture des démonstrations.** Une démonstration de déplacement et une démonstration de manipulation ne prouvent pas des choses de même difficulté. Devant une manipulation, les questions utiles sont : **combien de prises, quelle variété d'objets, quelle préparation de la scène, et que se passe-t-il quand ça rate**.

**À ne pas confondre avec.** **La préhension seule**, qui est le geste de saisie ; la manipulation inclut l'insertion, l'assemblage, la réorientation en main — dont la difficulté est supérieure d'un cran.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Progrès nets sur la saisie d'objets variés en environnement maîtrisé ; les tâches d'assemblage et d'insertion restent très en deçà d'une exploitation sans surveillance.
> 🔄 **À revoir si** un système démontre un taux de succès en manipulation d'objets variés compatible avec une exploitation continue, publié sur plusieurs mois d'exploitation réelle.

**Renvois** — Couche : agir · Courants : Physical AI, general-purpose robotics (ch. 33) · Convergence : robotique généraliste (36) · Voir aussi : peau électronique (ch. 7), VLA (ch. 13).

---

### ◆◆ Locomotion

**Niveau** — capacité · **Couche** — agir

**En une phrase.** Se déplacer en terrain non aménagé, par roues, chenilles ou pattes.

**Comment ça fonctionne.** Le choix du mode de locomotion est un arbitrage entre efficacité énergétique et franchissement. **Les roues sont largement plus efficaces** sur sol praticable — un ordre de grandeur en énergie par distance parcourue. Les pattes permettent de franchir des obstacles discontinus — marches, gravats, terrain accidenté — au prix d'une consommation supérieure, d'une complexité de commande et d'une usure accrue.

Le progrès des machines à pattes vient moins de la mécanique que du **contrôle** : maintenir l'équilibre d'un système intrinsèquement instable suppose une boucle rapide et une bonne estimation de l'état, ce que la puissance de calcul embarquée a rendu possible.

**Ce que ça permet.** Accéder à des environnements conçus pour l'humain — escaliers, échelles, encombrement — sans les modifier · inspecter des sites non aménagés · opérer après un sinistre.

**Ce qui bloque.** **L'énergie.** Une machine à pattes consomme davantage pour la même distance, ce qui aggrave la boucle masse-énergie de la couche. **L'usure** : les articulations sollicitées en permanence limitent la durée entre maintenances. Et **la valeur d'usage** : le franchissement n'est utile que là où le terrain l'exige, ce qui restreint le domaine économique.

**Ce que cela implique.** La question n'est pas quelle locomotion est supérieure, mais **quelle fraction des environnements visés exige réellement le franchissement**. Dans la plupart des sites industriels, la réponse est faible — ce qui explique la domination des plateformes à roues malgré la visibilité des machines à pattes.

**À ne pas confondre avec.** **La navigation**, qui est le choix du chemin ; la locomotion est la manière de le parcourir.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour les plateformes à roues, 🔬 émergent en exploitation pour les quadrupèdes, principalement en inspection.
> 🔄 **À revoir si** l'autonomie énergétique d'une plateforme à pattes atteint celle d'une plateforme à roues de mission comparable.

**Renvois** — Couche : agir · Convergence : robotique généraliste (36).

---

### ◆◆ Robotique souple

**Niveau** — famille · **Couche** — agir

**En une phrase.** Des machines dont les éléments se déforment, plutôt que d'être rigides et articulées.

**Comment ça fonctionne.** Au lieu d'un squelette rigide avec des articulations, la structure elle-même se déforme — par actionnement pneumatique, par matériaux à mémoire de forme, ou par câbles internes. **La conformité remplace la précision** : au lieu de calculer la position exacte à atteindre, on laisse la structure épouser l'objet.

**Ce que ça permet.** Saisir des objets fragiles, irréguliers ou dont la position est mal connue · opérer près d'humains avec un risque intrinsèquement réduit · s'insérer dans des espaces contraints.

**Ce qui bloque.** **La commande.** Un système déformable a une infinité de configurations possibles ; le modéliser et le piloter précisément est difficile — la conformité qui fait sa force fait aussi sa difficulté. **La force disponible**, limitée par les matériaux. **La durabilité**, les éléments souples se fatiguant. Et **l'alimentation** pneumatique, qui impose un compresseur et des conduites.

**Ce que cela implique.** C'est une famille qui gagne là où **la variabilité de l'objet est le problème**, et perd là où la force et la précision comptent — typiquement dans l'agroalimentaire et la manipulation de produits frais.

**À ne pas confondre avec.** **Les cobots**, dont la sécurité vient d'une limitation de puissance et non d'une propriété mécanique.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des déploiements industriels établis en préhension de produits variables.
> 🔄 **À revoir si** un actionnement souple électrique — sans pneumatique — atteint des forces et une durabilité comparables.

**Renvois** — Couche : agir.

---

### ◆ Microrobotique

**Niveau** — famille · **Couche** — agir

**En une phrase.** Des machines de très petite taille, dont le comportement physique diffère radicalement de celui de leurs équivalents à grande échelle.

**Ce qu'il faut en savoir.** **Ce n'est pas de la robotique miniaturisée.** À cette échelle, les forces de surface — adhérence, tension superficielle, frottement — dominent le poids et l'inertie. Un objet microscopique colle plutôt qu'il ne tombe. Les principes de conception et d'actionnement sont donc entièrement différents, et l'actionnement est souvent externe — champ magnétique, lumière, écoulement — plutôt qu'embarqué.

**Ce qui bloque.** **L'énergie et le contrôle.** Embarquer une source d'énergie et un calculateur à cette échelle reste largement hors de portée, ce qui limite l'autonomie réelle.

**Où vous rencontrerez le terme.** Recherche médicale · microfabrication · inspection de canalisations fines.

**À ne pas confondre avec.** **Les MEMS** (ch. 7), qui sont des composants et non des machines mobiles.

> ⏱ **État au 23/08/2026** — 🔭 prospectif hors laboratoire.
> 🔄 **À revoir si** un dispositif microrobotique atteint un usage clinique ou industriel établi.

**Renvois** — Couche : agir.

---

### ◆◆ Robotique médicale

**Niveau** — famille · **Couche** — agir

**En une phrase.** Des systèmes qui assistent ou exécutent un geste médical, sous contrôle d'un praticien.

**Pourquoi on en parle.** Parce que c'est **le domaine robotique le plus régulé et le mieux documenté**, et donc celui qui montre le mieux ce que coûte une démonstration de sûreté.

**Comment ça fonctionne.** La majorité des systèmes déployés sont **téléopérés** : le praticien commande, la machine reproduit avec une précision et une stabilité supérieures, filtre les tremblements et démultiplie ou réduit les mouvements. L'autonomie réelle est très limitée et confinée à des gestes bien définis.

**Ce que ça permet.** Des gestes plus précis et moins invasifs · une meilleure ergonomie pour le praticien · une reproductibilité accrue.

**Ce qui bloque.** **Le coût d'acquisition et de consommables**, qui restreint la diffusion. **La démonstration de bénéfice clinique**, qui exige des études longues et dont les résultats sont inégaux selon les interventions. Et **le cadre** : chaque évolution logicielle significative peut relever d'une procédure d'autorisation.

**Ce que cela implique.** C'est le domaine qui illustre le mieux **l'écart entre capacité technique et déploiement** : la technologie n'est pas le facteur limitant. Le sont le coût, la preuve clinique et la formation des praticiens.

**À ne pas confondre avec.** **Une chirurgie autonome**, qui n'existe pas en pratique clinique.

> ⏱ **État au 23/08/2026** — 🏭 déployé, en croissance, avec une diversification des acteurs après l'expiration de brevets fondateurs.
> 🔄 **À revoir si** un geste chirurgical est autorisé en exécution autonome sous supervision, dans une juridiction majeure.

**Renvois** — Couche : agir.

---

### ◆ Robotique agricole

**Niveau** — famille · **Couche** — agir

**En une phrase.** Des machines autonomes pour le désherbage, la récolte, le semis ou la surveillance de cultures.

**Ce qui bloque.** **La saisonnalité.** Une machine utilisable trois semaines par an doit amortir son coût sur ces trois semaines — c'est la contrainte économique dominante, et elle explique la préférence pour des machines polyvalentes ou louées. S'y ajoutent **la variabilité du végétal**, qui est un cas extrême du problème de manipulation, et **les conditions** — boue, poussière, pluie, luminosité changeante.

**Ce que cela implique.** Les usages qui réussissent sont ceux où le travail humain est cher, rare ou pénible, et où la tâche est répétitive : désherbage mécanique, surveillance, traite. La récolte de fruits fragiles reste un problème ouvert, et c'est précisément un problème de manipulation.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des segments 🏭 déployés — traite, désherbage sur certaines cultures.
> 🔄 **À revoir si** un récolteur robotisé de fruits atteint un coût par kilogramme compétitif avec la main-d'œuvre dans une région à coût du travail élevé.

**Renvois** — Couche : agir.

---


## Chapitre 15 — Humanoïdes et robots généralistes

> **Ce que ce chapitre ajoute — et ce qu'il ne fait pas.** Ce chapitre traite **la plateforme humanoïde comme objet** : comment elle est faite, ce qu'elle coûte, ce qui s'use, ce qui la borne.
>
> **Il ne traite pas de la capacité de généralité robotique**, qui fait l'objet du dossier de convergence 36 — lequel considère toutes les morphologies, y compris non humanoïdes. La question « quelle forme gagnera » n'appartient pas à ce chapitre.
>
> **Format exceptionnel.** L'entrée principale est une monographie plus longue que le format standard, parce que l'objet est le plus médiatisé de l'atlas et le plus mal évalué. Trois entrées de composants la complètent.

---

### ◆◆◆ Robot humanoïde — *monographie*

**Niveau** — plateforme · **Couche** — agir

**En une phrase.** Une machine à morphologie humaine — bipède, à deux bras, à hauteur d'homme — conçue pour opérer dans des environnements aménagés pour l'humain.

**Pourquoi on en parle.** Parce que c'est l'objet technologique le plus visible de la période, celui qui concentre le plus d'investissement et de démonstrations — et celui où l'écart entre ce qui est montré et ce qui est exploitable est le plus grand.

#### Pourquoi une morphologie humaine

L'argument est précis et mérite d'être compris avant d'être discuté : **le monde bâti est conçu pour des humains**. Escaliers, poignées, interrupteurs, hauteurs de plan de travail, largeurs de passage, outils à main. Une machine de forme humaine peut, en principe, opérer dans cet environnement sans le modifier — ce qui supprime le coût d'aménagement qui domine l'économie de la robotique industrielle.

**Le contre-argument est tout aussi précis.** La forme humaine résulte d'une évolution biologique sous des contraintes qui ne sont pas celles d'une machine. Elle est instable par construction, énergétiquement coûteuse, et impose de porter une masse en hauteur. Une machine libre de sa forme choisirait rarement celle-là.

**Le vrai critère est donc économique** : la fraction des tâches visées qui exige réellement la forme humaine, comparée au coût qu'elle impose. Cette fraction n'est pas nulle et n'est pas la majorité — c'est ce que le dossier 36 instruira.

#### Ce qui compose la machine

**Les actionneurs** dominent le coût, la masse et la performance. Un humanoïde en compte plusieurs dizaines, chacun devant produire un couple élevé dans un volume réduit, avec une réponse rapide et une capacité à absorber les chocs. Ils font l'objet d'une entrée dédiée.

**Les mains** concentrent la difficulté : c'est là que se joue la généralité, et c'est le sous-système le moins mature.

**L'énergie embarquée** est soumise à la boucle de la couche : ajouter de la batterie ajoute de la masse, qu'il faut déplacer, ce qui consomme davantage. L'autonomie utile des plateformes actuelles se compte en heures, et le gain d'autonomie est moins que proportionnel à l'énergie ajoutée.

**Le calcul embarqué** doit exécuter la perception et la commande dans une enveloppe thermique et énergétique contrainte — ce qui renvoie aux modèles compacts du chapitre 11.

**La structure** doit être légère et rigide, et supporter des cycles de sollicitation qui produisent du jeu et de l'usure.

#### Ce qui bloque

**La fiabilité, très loin devant tout le reste.** Une démonstration montre une tâche réussie ; une exploitation exige un taux d'échec compatible avec une supervision légère. Sur des tâches de manipulation variées, l'écart entre les deux se compte en ordres de grandeur.

**Le coût.** Il est dominé par les actionneurs et l'intégration, et sa baisse dépend de la série — donc de la demande, donc de la fiabilité. **C'est une boucle** : sans fiabilité, pas de série ; sans série, pas de baisse de coût ; sans baisse de coût, pas de demande.

**La maintenance.** Une machine à plusieurs dizaines d'articulations sollicitées produit du jeu, de l'usure et des pannes. Le nombre de techniciens formés borne le déploiement bien avant la capacité de production.

**Les données.** L'apprentissage de tâches variées dépend de démonstrations acquises une à une, généralement par téléopération.

#### Pourquoi la démonstration est particulièrement trompeuse ici

Cinq raisons, toutes vérifiables :

**La téléopération n'est pas toujours déclarée.** Une machine pilotée à distance et une machine autonome produisent des images identiques.

**Le nombre de prises n'est pas indiqué.** Une réussite sur cinquante donne la même vidéo qu'une réussite sur deux.

**La scène est préparée.** Objets connus, positions favorables, éclairage maîtrisé, sol plan.

**Le montage masque les durées.** Une accélération, une coupure, un changement de plan suffisent à effacer une reprise.

**Et l'échec n'est jamais montré**, alors que c'est l'information la plus utile — un système qui échoue proprement est très différent d'un système qui échoue dangereusement.

**Ce qu'il faut demander devant toute démonstration :** combien de prises · quelle part de téléopération · quelle variété d'objets et de positions · quelle durée continue sans intervention · et que se passe-t-il quand ça rate.

#### Ce que cela implique

L'humanoïde est **une plateforme, pas une capacité**. Sa présence dans une démonstration ne dit rien sur la généralité du système qui la pilote, laquelle relève des architectures du chapitre 13.

Et les premiers déploiements crédibles se situent là où **l'environnement est humain mais la tâche répétitive** — manutention en entrepôt, chargement, transfert entre postes. C'est-à-dire précisément là où une machine spécialisée serait souvent moins chère, ce qui explique que le débat économique reste ouvert.

**À ne pas confondre avec.** **La robotique généraliste** (dossier 36), qui est une capacité et non une forme. **L'embodied AI** (ch. 13), qui est une thèse sur l'apprentissage. **Physical AI** (ch. 33), qui est un cadrage.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Nombreux acteurs, plateformes disponibles, premiers programmes pilotes en environnement industriel avec supervision. Aucune exploitation autonome documentée à l'échelle. Les annonces de production en série sont des objectifs, non des capacités installées.
> 🔄 **À revoir si** un exploitant tiers publie des données d'exploitation sur plusieurs mois — taux d'intervention humaine, disponibilité, coût de maintenance — sur une flotte en production.

**Renvois** — Couche : agir · Courants : humanoid robotics, Physical AI (ch. 33) · Convergence : robotique généraliste (36).

---

### ◆◆◆ Actionneurs robotiques

**Niveau** — composant · **Couche** — agir

**En une phrase.** Les dispositifs qui convertissent l'énergie en mouvement — et qui déterminent, plus que toute autre pièce, ce qu'une machine peut faire et ce qu'elle coûte.

**Pourquoi on en parle.** Parce que c'est **la brique déterminante de toute la couche et la moins discutée**. Les débats portent sur les modèles et la perception ; les limites viennent le plus souvent d'ici.

**Comment ça fonctionne — trois familles.**

**Électrique.** Un moteur associé à un réducteur. Précis, propre, facile à commander, rendement élevé. Mais un moteur tourne vite avec peu de couple, alors que l'application demande l'inverse : il faut donc un **réducteur**, qui introduit du jeu, du frottement, de l'inertie et de l'usure. **Le réducteur devient souvent le composant qui limite la précision et la durée de vie de l'ensemble** — cas net du mécanisme du volume 1 : résoudre le problème du couple crée le problème du jeu.

**Hydraulique.** Densité de puissance très supérieure, capacité à encaisser les chocs. Mais une centrale, des conduites, des fuites, un rendement moindre et un entretien lourd.

**Quasi-direct.** Un moteur à couple élevé avec une réduction faible ou nulle. On perd en couple maximal, on gagne en absence de jeu, en réversibilité — la machine peut être poussée à la main — et en capacité à mesurer les efforts sans capteur dédié. **C'est l'approche qui a rendu praticables les machines à pattes et une partie des humanoïdes.**

**Les grandeurs qui comptent.** Couple maximal · densité de puissance par kilogramme · précision et jeu · rendement · durée de vie en cycles · et **capacité à encaisser un choc**, souvent oubliée alors qu'elle décide de la survie de la machine en usage réel.

**Ce qui bloque.** **La dissipation.** Un actionneur perd son énergie en chaleur, dans un volume restreint, souvent sans circulation d'air. **La densité de puissance réellement utilisable est bornée par l'évacuation thermique**, non par les caractéristiques électriques — c'est pourquoi un actionneur peut délivrer un couple élevé brièvement et pas en continu.

S'y ajoutent le **coût**, qui domine celui d'une machine multi-articulée, et **l'usure**, qui produit du jeu et donc une imprécision que les capteurs articulaires ne voient pas.

**Ce que cela implique.** Une machine peut être précise selon ses capteurs et imprécise en réalité, parce que le jeu se situe en aval de la mesure. **C'est une défaillance silencieuse d'origine mécanique**, et elle croît avec l'usage.

**À ne pas confondre avec.** **Le moteur seul**, qui n'est qu'un élément de l'actionneur — lequel comprend aussi la réduction, l'électronique de commande, les capteurs et souvent le refroidissement.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Progrès continus sur la densité de puissance et sur les architectures quasi-directes ; le coût unitaire reste le facteur dominant du prix des machines multi-articulées.
> 🔄 **À revoir si** un actionneur combine densité de puissance hydraulique et propreté électrique à un coût de série.

**Renvois** — Couche : agir · Convergence : robotique généraliste (36) · Voir aussi : électronique de puissance (ch. 23).

---

### ◆◆ Mains et préhenseurs

**Niveau** — composant · **Couche** — agir

**En une phrase.** L'interface entre la machine et l'objet — et le sous-système où se joue la généralité.

**Comment ça fonctionne.** Un continuum, du plus spécialisé au plus général. La **ventouse** saisit rapidement des surfaces planes et lisses, à faible coût. La **pince à deux doigts** couvre une large variété d'objets rigides. La **main multi-doigts** permet en principe la réorientation en main et la manipulation fine, au prix d'une complexité considérable.

**L'arbitrage est net** : plus le préhenseur est général, plus il est cher, fragile et difficile à commander. En pratique, la plupart des déploiements industriels utilisent le préhenseur le plus spécialisé que la tâche autorise.

**Ce qui bloque.** **La perception du contact.** Sans retour tactile, la machine ne sait pas si elle tient, si elle serre trop, si l'objet glisse. C'est le lien direct avec la peau électronique du chapitre 7, et c'est le verrou. **La durabilité** : le préhenseur est la pièce qui frotte et qui reçoit les chocs. Et **le nombre d'actionneurs** d'une main multi-doigts, qui multiplie coût, masse et modes de panne.

**Ce que cela implique.** La généralité d'une machine se mesure moins à sa morphologie qu'à **la variété d'objets que son préhenseur peut saisir sans changement d'outil**. C'est une grandeur observable, rarement publiée.

**À ne pas confondre avec.** **La main humaine**, dont la densité de capteurs et la capacité de réorientation restent hors de portée — la comparaison est trompeuse et alimente des attentes non fondées.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour les préhenseurs simples, 🔬 émergent pour les mains multi-doigts en exploitation.
> 🔄 **À revoir si** une main multi-doigts démontre plusieurs milliers d'heures d'exploitation avec un taux de panne compatible avec un usage industriel.

**Renvois** — Couche : agir.

---

### ◆◆ Téléopération

**Niveau** — capacité et doctrine · **Couche** — agir, relier

**En une phrase.** Commander une machine à distance, l'humain fournissant la perception, la décision ou les deux.

**Pourquoi on en parle.** Pour deux raisons de nature opposée, et il faut les tenir ensemble. **C'est la principale source de données** pour l'apprentissage de la manipulation. Et **c'est ce que masquent la plupart des démonstrations spectaculaires**.

**Comment ça fonctionne.** Un opérateur pilote via une interface — manettes, exosquelette, capture de mouvement — et reçoit un retour visuel, parfois haptique. Trois régimes coexistent : **pilotage direct**, l'humain fait tout ; **assistance**, la machine corrige et sécurise ; **supervision**, la machine agit seule et l'humain intervient sur demande — un opérateur pouvant alors superviser plusieurs machines.

**Ce que ça permet.** Opérer en environnement inaccessible ou dangereux · déployer une capacité avant qu'elle soit autonome · **collecter des démonstrations**, ce qui en fait l'infrastructure de collecte du chapitre 13 · et amortir le coût humain sur plusieurs machines en régime de supervision.

**Ce qui bloque.** **La latence.** Au-delà de quelques centaines de millisecondes, le pilotage direct devient difficile et le retour de force instable. Cela borne la distance et impose une liaison de qualité. **Le retour haptique**, dont la fidélité reste limitée. Et **le ratio opérateurs par machine**, qui détermine l'économie : une machine supervisée à un opérateur pour une machine ne réduit pas le coût du travail, elle le déplace.

**Ce que cela implique.** Le **ratio de supervision** est la grandeur économique décisive de toute la couche, et elle est rarement publiée. Une flotte de machines supervisées à un pour un est une solution de mobilité du travail, pas d'automatisation.

**Sûreté et sécurité.** Une liaison de commande est une surface d'attaque dont la compromission produit un effet physique. Traitement au niveau du principe.

**À ne pas confondre avec.** **L'autonomie supervisée** (ch. 16), où la machine décide et l'humain surveille — ici, l'humain décide.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Usage établi en milieu dangereux et en médecine ; usage massif et souvent non déclaré dans les démonstrations et la collecte de données.
> 🔄 **À revoir si** des exploitants publient couramment leur ratio d'opérateurs par machine — ce qui rendrait comparable l'économie réelle des déploiements.

**Renvois** — Couche : agir, relier · Convergence : robotique généraliste (36) · Voir aussi : apprentissage par imitation (ch. 13), haptique (ch. 31).

---

---


## Chapitre 16 — Systèmes sans équipage

> **Périmètre de ce chapitre.** Il traite les plateformes sans équipage sous l'angle **technologique, industriel, économique et de gouvernance**. Il ne fournit aucun paramètre d'emploi, aucune méthode de mise en œuvre offensive, aucune technique de perturbation ou de contre-mesure — y compris lorsque ces informations sont publiquement accessibles. Cette règle s'applique phrase par phrase.
>
> **Ce que le chapitre ajoute.** Les chapitres 14 et 15 traitaient de machines opérant dans des espaces bornés. Celui-ci traite de machines qui opèrent **loin de leur opérateur**, ce qui introduit une contrainte nouvelle : la liaison.
>
> **Cinq entrées.**

---

### ◆◆◆ Drones aériens

**Niveau** — plateforme · **Couche** — agir, percevoir, relier

**En une phrase.** Des aéronefs sans équipage à bord, allant de quelques centaines de grammes à plusieurs tonnes, dont le point commun est d'être pilotés à distance ou de suivre un plan de vol automatique.

**Pourquoi on en parle.** Parce que **le mot désigne une vingtaine d'objets sans commune mesure** — et parce que dans la plupart des applications civiles, le verrou n'est pas technique.

**Comment ça fonctionne — et pourquoi les classes comptent.** La masse et le mode de sustentation déterminent presque tout : l'autonomie, la charge utile, le domaine de vol, et surtout le régime réglementaire applicable.

Un **multirotor** décolle verticalement, tient en vol stationnaire, et paie cette capacité par une autonomie qui se compte en dizaines de minutes — la sustentation consomme en permanence. Une **voilure fixe** est bien plus efficace en croisière, avec des autonomies d'un ordre de grandeur supérieures, mais exige une zone de décollage et ne peut pas stationner. Les architectures **hybrides** combinent les deux au prix d'une masse et d'une complexité accrues.

**La contrainte de la couche s'applique intégralement** : la boucle masse-énergie est ici la plus sévère de tout l'atlas, puisque toute masse ajoutée doit être sustentée en permanence.

**Où vous rencontrerez le terme.** Inspection d'infrastructures · cartographie et topographie · agriculture · cinéma · sécurité civile et secours · logistique · surveillance environnementale · applications de défense.

**Ce que ça permet.** Accéder à un point de vue aérien à un coût sans commune mesure avec celui d'un aéronef habité · inspecter sans échafaudage ni arrêt d'exploitation · couvrir rapidement une zone étendue.

**Ce qui bloque — et c'est le point principal.** Dans la majorité des applications civiles à valeur, **le verrou dominant est le cadre d'autorisation du vol hors vue directe de l'opérateur**. Tant qu'un opérateur doit garder la machine en vue, l'économie reste celle d'un travail humain déplacé ; l'automatisation ne devient intéressante qu'au-delà.

S'y ajoutent **l'assurabilité**, qui suit la maturité du cadre plus que celle de la technique ; **l'autonomie énergétique**, qui borne les missions ; **la détection et l'évitement** d'autres aéronefs, condition technique de l'autorisation ; et **l'intégration à l'espace aérien**, qui est un problème de coordination et non de plateforme.

**Ce que cela implique.** C'est un cas d'école du volume 1 : une technologie mûre, peu coûteuse, dont la diffusion est bornée par une condition institutionnelle. **La grandeur à surveiller n'est pas la performance des machines mais le nombre d'autorisations de vol hors vue délivrées** et les conditions qui les accompagnent.

**Sûreté et sécurité.** Un aéronef sans équipage est un objet volant dont la chute a des conséquences · la liaison de commande est une dépendance critique · la navigation repose souvent sur une référence satellitaire dont le chapitre 6 a établi la fragilité. Ces points sont traités au niveau du principe et de leurs conséquences systémiques.

**À ne pas confondre avec.** **Un aéronef autonome**, qui décide ; la plupart des drones exécutent un plan de vol et ne décident de rien. **Un modèle réduit**, dont le régime réglementaire et l'usage diffèrent.

**Termes voisins.** *UAV*, *UAS* — ce dernier désignant le système complet, plateforme, station sol et liaison, ce qui est plus juste.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Filière mature en inspection et cartographie ; cadres d'autorisation du vol hors vue en construction progressive selon les juridictions, avec des rythmes très inégaux.
> 🔄 **À revoir si** une juridiction majeure ouvre le vol hors vue à un régime déclaratif plutôt qu'à autorisation individuelle.

**Renvois** — Couche : agir · Courant : drone economy (ch. 33) · Convergence : autonomie mobile (39).

---

### ◆ Systèmes terrestres sans équipage

**Niveau** — plateforme · **Couche** — agir

**En une phrase.** Des véhicules terrestres opérant sans conducteur à bord, hors du réseau routier ouvert.

**Où vous rencontrerez le terme.** Mines et carrières · agriculture · logistique de site · inspection · agriculture · applications de défense.

**Ce qui bloque.** **La mobilité en terrain non préparé** reste difficile et coûteuse en énergie. Et le domaine souffre d'une comparaison défavorable : là où l'environnement est structuré, un robot mobile d'entrepôt suffit ; là où il ne l'est pas, la difficulté croît fortement. **La zone où ces plateformes sont économiquement pertinentes est donc étroite** — sites industriels étendus, agriculture, environnements dangereux.

**Ce que cela implique.** Le déploiement le plus avancé se situe dans les mines à ciel ouvert : environnement clos, trajets répétitifs, conducteurs coûteux et exposés. C'est la configuration qui réunit toutes les conditions favorables.

**À ne pas confondre avec.** **Les véhicules autonomes routiers** (ch. 17), dont la contrainte principale est la cohabitation avec des humains non prévenus.

> ⏱ **État au 23/08/2026** — 🏭 déployé en site clos, 🔬 émergent ailleurs.
> 🔄 **À revoir si** une plateforme terrestre autonome atteint un coût d'exploitation compétitif en terrain agricole ouvert.

**Renvois** — Couche : agir.

---

### ◆◆ Systèmes maritimes et sous-marins

**Niveau** — plateforme · **Couche** — agir, relier

**En une phrase.** Des navires et engins submersibles opérant sans équipage, en surface ou en immersion.

**Pourquoi on en parle.** Parce que le milieu impose une contrainte que ne connaît aucune autre plateforme : **sous l'eau, les ondes électromagnétiques ne se propagent pratiquement pas**.

**Comment ça fonctionne.** En surface, un navire sans équipage relève d'une problématique proche de celle des autres plateformes : navigation, perception, liaison satellitaire, avec des temps de réaction longs et un environnement peu encombré — ce qui rend la tâche plus facile que sur route.

**En immersion, tout change.** Pas de positionnement satellitaire, pas de liaison radio, pas de retour vidéo à distance. La navigation repose sur l'inertiel recalé par des méthodes acoustiques ou par appariement de terrain, et la communication passe par l'acoustique, dont le chapitre 7 a rappelé qu'elle est lente et à très faible débit. **Un engin submersible est donc autonome par nécessité**, non par choix.

**Ce que ça permet.** Inspecter des ouvrages sous-marins sans plongeur ni navire support · cartographier les fonds · surveiller des installations · effectuer des transits longs à faible coût.

**Ce qui bloque.** **L'énergie**, avec des missions bornées par la batterie et une recharge difficile. **La récupération** : une plateforme perdue est perdue, ce qui impose une fiabilité élevée. **La communication**, qui interdit toute supervision continue et impose de faire confiance à la machine pendant toute la mission. Et **le cadre juridique** de la navigation sans équipage, encore en construction.

**Ce que cela implique.** C'est le domaine où **l'autonomie n'est pas une ambition mais une contrainte** — et c'est ce qui en fait un observatoire utile : les questions de mode dégradé, de décision hors supervision et de comportement en cas de perte de contact y sont traitées depuis longtemps.

**À ne pas confondre avec.** Les engins **filoguidés**, reliés à un navire par un câble qui fournit énergie et liaison — ils ne sont pas autonomes et couvrent la majorité des interventions actuelles.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour l'inspection et l'hydrographie, 🔬 émergent pour les transits longs et la navigation de surface sans équipage.
> 🔄 **À revoir si** un cadre juridique international pour la navigation commerciale sans équipage entre en vigueur.

**Renvois** — Couche : agir · Voir aussi : acoustique sous-marine (ch. 7), navigation sans référence satellitaire (ch. 6).

---

### ◆◆◆ Essaims et coordination distribuée

**Niveau** — système et doctrine · **Couche** — agir, décider, relier

**En une phrase.** Faire opérer ensemble un grand nombre de plateformes dont le comportement collectif émerge de règles locales, sans coordination centrale.

**Pourquoi on en parle.** Parce que le terme est employé pour désigner tout regroupement nombreux — alors que **ce qui définit un essaim est l'absence de centre**, avec les propriétés et les difficultés que cela implique.

**Comment ça fonctionne.** Chaque unité observe son voisinage immédiat, applique des règles simples — maintenir une distance, suivre une direction moyenne, éviter une collision — et n'a de connaissance ni du plan d'ensemble, ni de l'état global. Le comportement collectif n'est programmé nulle part : il résulte des interactions locales.

**Ce que cela donne.** Une **robustesse remarquable** : la perte d'unités ne détruit pas le collectif, puisqu'aucune n'est indispensable. Une **scalabilité** : ajouter des unités ne complexifie pas la coordination, chacune ne dialoguant qu'avec ses voisines. Et une **absence de point unique de défaillance**.

**Ce que cela coûte, et c'est le point mal compris.** **La prévisibilité.** Un comportement émergent n'est pas spécifié : on peut le constater, difficilement le garantir. Vérifier qu'un collectif ne produira jamais un comportement indésirable est un problème ouvert, et c'est ce qui bloque l'emploi dans des contextes à conséquence.

S'y ajoute **la communication**, qui est le vrai verrou technique : une coordination locale suppose des échanges, donc de la bande passante, de l'énergie et une tolérance à la latence. Le cadrage biologique masque ce coût en suggérant que la coordination est gratuite — elle ne l'est pas.

**Ce que ça permet.** Couvrir une zone étendue avec des plateformes individuellement peu capables · maintenir une mission malgré des pertes · adapter la formation sans replanification centrale.

**Ce qui bloque.** La **vérification** du comportement collectif · la **communication** en environnement contraint · le **coût unitaire**, puisque l'approche suppose le nombre · et la **gouvernance**, un système sans centre étant difficile à interrompre proprement.

**Ce que cela implique.** L'essaim est un compromis explicite : **on échange de la prévisibilité contre de la robustesse**. Ce compromis convient à des missions tolérantes à l'incertitude du résultat — couverture, recherche, mesure distribuée — et convient mal là où le comportement doit être garanti.

**Traitement dual.** Les applications de défense de la coordination distribuée sont réelles et documentées. Ce volume les traite au niveau industriel, économique, doctrinal et de gouvernance — notamment la question de l'économie de l'attrition, abordée au chapitre 44 — et ne fournit aucun élément d'emploi.

**À ne pas confondre avec.** **Une flotte coordonnée depuis un centre**, qui est le cas le plus fréquent et n'est pas un essaim. **Les systèmes multi-agents** logiciels (ch. 12), dont l'architecture est généralement dirigée.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Démonstrations nombreuses, applications civiles limitées — spectacle, mesure distribuée — et développements soutenus en défense. La vérification du comportement collectif reste le verrou.
> 🔄 **À revoir si** une méthode de vérification permet de garantir des propriétés de sûreté sur un collectif à comportement émergent.

**Renvois** — Couche : agir, décider, relier · Courant : swarm intelligence (ch. 33) · Voir aussi : perception distribuée (ch. 7).

---

### ◆◆ Autonomie supervisée

**Niveau** — doctrine · **Couche** — décider

**En une phrase.** Une machine décide et agit ; un humain surveille et peut intervenir.

**Pourquoi on en parle.** Parce que **c'est le régime réel de la quasi-totalité des systèmes déployés**, et parce que son économie dépend d'un paramètre rarement publié.

**Comment ça fonctionne — trois configurations à distinguer.**

**Humain dans la boucle** : la machine propose, l'humain valide avant exécution. Sûr, mais le débit est borné par l'humain.

**Humain sur la boucle** : la machine agit, l'humain observe et peut interrompre. C'est le régime le plus courant, et le plus délicat.

**Humain en réserve** : la machine agit seule et sollicite l'humain uniquement en cas de blocage. C'est le régime qui permet à un opérateur de superviser plusieurs machines — et donc le seul qui produise un gain économique net.

**Ce qui bloque — et c'est un problème humain, pas technique.** **La vigilance.** Un opérateur qui surveille un système fiable pendant des heures n'est pas dans un état permettant de reprendre le contrôle en quelques secondes. Plus le système est fiable, moins l'humain est prêt — **la fiabilité dégrade la supervision qu'elle rend nécessaire**.

**Ce paradoxe n'est pas une intuition : il est établi dans la littérature des facteurs humains depuis les années 1980**, sous le nom d'*ironies de l'automatisation* — l'article fondateur de Lisanne Bainbridge, publié en 1983 dans *Automatica*, reste l'une des références les plus citées du domaine. Il décrit trois effets que quarante ans de travaux ont confirmés plutôt qu'infirmés : **la vigilance décroît** lors d'une surveillance prolongée d'un système qui ne défaille pas ; **les compétences s'atrophient** faute d'être exercées, précisément celles qu'exige la reprise ; et **la confiance excessive** conduit à suivre le système quand il se trompe et à ne pas voir qu'il a échoué — un mécanisme attentionnel que l'expérience et la formation ne suppriment pas.

**Ce que la littérature ne dit pas**, et qu'il faut se garder de lui faire dire : elle n'a pas produit de loi quantitative transposable. **Les durées au-delà desquelles la vigilance se dégrade dépendent de la tâche, du taux d'événements et de l'organisation** ; elles se mesurent sur un déploiement, elles ne se lisent pas dans un tableau. La conséquence pratique est en revanche stable : **on conçoit contre ce paradoxe** — par la rotation, la charge de travail maintenue, la conception des alertes — plutôt qu'on ne le résout par un supplément de fiabilité.

S'y ajoute **le délai de reprise** : entre l'alerte et l'action correcte, il faut comprendre la situation, ce qui prend du temps même pour un opérateur attentif.

**Ce que cela implique.** **Le ratio d'opérateurs par machine est la grandeur économique décisive** de tout déploiement autonome. Un ratio de un pour un ne réduit pas le coût du travail : il le déplace, éventuellement vers un lieu moins cher, ce qui est une décision différente de l'automatisation.

**À ne pas confondre avec.** **La téléopération** (ch. 15), où l'humain décide. Ici, la machine décide.

> ⏱ **État au 23/08/2026** — 🏭 déployé, régime dominant de tous les systèmes autonomes en exploitation.
> 🔄 **À revoir si** des exploitants publient couramment leur ratio de supervision, ce qui rendrait comparables les économies annoncées.

**Renvois** — Couche : décider · Convergence : autonomie mobile (39) · Voir aussi : automatisation, agentivité, autonomie (ch. 12).

---


## Chapitre 17 — Mobilité autonome

> **Ce que ce chapitre ajoute.** Le chapitre 16 traitait de plateformes opérant loin de leur opérateur, mais dans des espaces généralement réservés. Celui-ci traite du cas le plus difficile : **opérer dans un espace partagé avec des humains non prévenus**.
>
> **Quatre entrées**, dont deux majeures. La seconde — le domaine de conception opérationnelle — est la notion la plus utile et la moins connue de tout le chapitre.

---

### ◆◆◆ Véhicules autonomes

**Niveau** — plateforme · **Couche** — agir, percevoir, décider

**En une phrase.** Des véhicules routiers capables d'assurer la conduite sans intervention humaine, dans des conditions définies.

**Pourquoi on en parle.** Parce que c'est **le cas d'école de l'écart entre annonce et déploiement** — le volume 1 l'a instruit — et parce que la capacité est désormais démontrée en exploitation commerciale, ce qui déplace la question.

**Comment ça fonctionne.** Une chaîne en quatre étages : **perception** — combiner caméras, radars et souvent lidars pour construire une représentation de l'environnement ; **localisation** — se situer précisément, généralement par rapport à une carte préétablie ; **prédiction et planification** — anticiper le comportement des autres usagers et choisir une trajectoire ; **contrôle** — exécuter cette trajectoire.

**Les niveaux d'automatisation.** Une échelle normalisée à six niveaux structure le vocabulaire du secteur. Le point qui compte : **la frontière décisive se situe entre le niveau où l'humain doit rester prêt à reprendre et celui où il ne le doit plus**. En dessous, la responsabilité reste au conducteur ; au-dessus, elle bascule vers le système et son exploitant — ce qui change entièrement l'économie, l'assurance et les exigences de preuve.

**Où vous rencontrerez le terme.** Automobile · transport de personnes · logistique et camionnage · navettes · assistance à la conduite.

**Ce que ça permet.** Un service de transport dont le coût marginal ne comprend pas de conducteur · une réduction potentielle des accidents liés à l'inattention · une mobilité pour des personnes qui ne conduisent pas.

**Ce qui bloque.** **La démonstration de sûreté, très loin devant la perception.** Le volume 1 l'a établi : on ne peut pas énumérer les situations d'un système ouvert sur le monde, donc on ne peut pas démontrer exhaustivement, donc l'assureur ne peut pas tarifer facilement le risque. **L'assurabilité est un meilleur indicateur avancé de déploiement que n'importe quelle annonce technique.**

S'y ajoutent l'**extension du domaine d'exploitation**, qui se fait ville par ville et condition par condition ; le **coût de la supervision à distance**, dont le ratio détermine l'économie réelle ; et le **renouvellement du parc** pour les véhicules particuliers, qui borne toute transformation à l'échelle du parc quel que soit le succès sur le flux.

**Ce que cela implique.** La question n'est plus « est-ce que ça marche » mais **« dans quel domaine, à quel ratio de supervision, et sous quel régime de responsabilité »**. Ces trois grandeurs sont observables et rarement publiées ensemble.

**Sûreté et sécurité.** Le logiciel agit sur le monde physique ; l'intégrité des commandes et la disponibilité du contrôle priment sur la confidentialité · dépendance à une cartographie et à une référence de positionnement · comportement en cas de perte de liaison de supervision.

**À ne pas confondre avec.** **L'assistance à la conduite**, où le conducteur reste responsable et doit rester prêt — la confusion entre les deux est la plus dangereuse du domaine, et elle a des conséquences documentées.

> ⏱ **État au 23/08/2026** — 🔬 émergent en exploitation. Services commerciaux sans conducteur opérationnels dans un nombre limité de villes, avec extension progressive du domaine d'exploitation. Le camionnage sur axes dédiés progresse. Aucune généralisation au véhicule particulier.
> 🔄 **À revoir si** un référentiel de démonstration de sûreté applicable aux systèmes apprenants devient opposable dans une juridiction majeure — ce qui rendrait l'assurabilité traitable et permettrait une extension par cadre plutôt que par négociation locale.

**Renvois** — Couche : agir · Courant : autonomous mobility (ch. 33) · Convergence : autonomie mobile (39).

---

### ◆◆◆ Domaine de conception opérationnelle

**Niveau** — capacité et notion de conception · **Couche** — décider, vérifier

**En une phrase.** L'ensemble des conditions dans lesquelles un système automatisé a été conçu, testé et validé — et hors desquelles son comportement n'est pas caractérisé.

**Pourquoi cette entrée existe.** Parce que **c'est la notion la plus utile et la moins connue de toute la couche**, et parce qu'elle transforme une question sans réponse — « ce système est-il sûr ? » — en trois questions qui en ont.

**Ce qu'un domaine d'emploi spécifie.** Types de voies · plages de vitesse · conditions météorologiques · luminosité · densité de trafic · zones géographiques · état de l'infrastructure · présence ou non de piétons. Un système peut être parfaitement validé sur autoroute par temps clair et n'avoir aucun comportement caractérisé en ville sous la pluie.

**Les trois questions qui définissent une conception sûre.**

**Un — le système sait-il quand il sort de son domaine ?** C'est le problème le plus difficile, et c'est exactement la détection de sortie de distribution du chapitre 13. Un système qui ne sait pas qu'il est hors domaine continue d'agir avec la même assurance apparente.

**Deux — que fait-il alors ?** Quatre réponses possibles, aux coûts très différents : s'arrêter en sécurité, si l'arrêt est sûr ; continuer malgré la défaillance, ce qui exige de la redondance sur toute la chaîne et coûte considérablement plus ; rendre la main, ce qui suppose un humain disponible et attentif — voir l'entrée précédente ; ou réduire ses capacités, souvent la meilleure réponse et la plus difficile à concevoir, puisqu'il faut avoir prévu à l'avance ce qui peut être abandonné.

**Trois — qui en est informé, et dans quel délai ?**

**Ce que cela implique — et c'est généralisable bien au-delà des véhicules.** La question utile devant tout système automatisé n'est jamais « est-il autonome ? » ni « est-il fiable ? », mais : **dans quelles conditions son comportement a-t-il été validé, sait-il quand il en sort, et que fait-il alors ?** Cette formulation s'applique à un robot, à un agent logiciel, à un système d'exploitation autonome, à un dispositif médical.

**Ce qui bloque.** **La spécification du domaine elle-même.** Décrire exhaustivement des conditions d'usage est difficile, et un domaine trop étroit limite l'usage tandis qu'un domaine trop large ne peut pas être validé. La normalisation de ces descriptions progresse et reste incomplète.

**À ne pas confondre avec.** **Les niveaux d'automatisation**, qui décrivent le partage de tâches entre humain et machine. Un système de niveau élevé sur un domaine étroit et un système de niveau modeste sur un domaine large sont deux propositions différentes, et le seul niveau ne permet pas de les comparer.

> ⏱ **État au 23/08/2026** — 🔬 émergent comme pratique formalisée. Notion adoptée dans les référentiels du secteur automobile, en cours d'extension à d'autres domaines d'autonomie.
> 🔄 **À revoir si** la description du domaine d'emploi devient une exigence normalisée dans un secteur hors automobile.

**Renvois** — Couche : décider, vérifier · Convergence : autonomie mobile (39) · Voir aussi : architecture de sûreté (ch. 30), détection de sortie de domaine (ch. 30).

---

### ◆◆ Autonomie maritime, aérienne et ferroviaire civiles

**Niveau** — plateforme · **Couche** — agir, décider

**En une phrase.** L'automatisation de la conduite dans des modes de transport autres que routier, dont les difficultés et les cadres n'ont rien de commun.

**Pourquoi les traiter ensemble.** Parce que la catégorie *autonomous mobility* les réunit alors que **leurs contraintes sont opposées**, et que la comparaison est instructive.

**Le ferroviaire** est le mode le plus avancé et le moins commenté : voie dédiée, absence d'obstacles imprévus, signalisation coopérative. Des lignes fonctionnent sans conducteur depuis des décennies. **La difficulté n'y est pas la conduite mais l'infrastructure** : équiper une ligne existante coûte cher, et la coexistence avec des trains non équipés complique tout.

**L'aérien** dispose d'un pilotage automatique très ancien pour les phases de croisière. La difficulté se concentre sur les phases critiques, la gestion des situations non nominales, et surtout **le cadre de certification**, qui est le plus exigeant de tous les modes.

**Le maritime** de surface bénéficie de temps de réaction longs et d'un environnement peu encombré, mais souffre d'un **vide juridique international** : les conventions supposent un équipage à bord.

**Ce que cela implique.** Sur les trois modes, **la difficulté dominante est institutionnelle et non technique** — infrastructure pour le rail, certification pour l'aérien, droit international pour le maritime. C'est l'inverse du routier, où la difficulté technique de l'environnement ouvert reste réelle.

**À ne pas confondre avec.** **Le pilotage automatique**, présent depuis longtemps dans l'aérien et le maritime, qui exécute une consigne sans gérer les situations imprévues.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour le ferroviaire sur lignes dédiées, 🔬 émergent pour le maritime de surface, cadre en construction pour l'aérien civil sans pilote.
> 🔄 **À revoir si** une convention internationale sur la navigation commerciale sans équipage aboutit.

**Renvois** — Couche : agir, décider.

---

### ◆◆ Localisation et cartographie

**Niveau** — capacité · **Couche** — percevoir, décider

**En une phrase.** Se situer précisément dans un environnement, et construire ou maintenir la représentation qui permet de le faire.

**Comment ça fonctionne — deux approches complémentaires.**

**La cartographie préétablie.** On relève au préalable l'environnement avec une précision élevée, et le véhicule s'y localise en comparant ce qu'il perçoit à cette carte. Précision excellente, mais **la carte doit être maintenue** : travaux, marquages effacés, signalisation modifiée. C'est un coût d'exploitation continu, et c'est ce qui limite l'extension géographique.

**La cartographie et localisation simultanées.** Le système construit sa carte en se déplaçant, tout en s'y localisant. Aucune préparation nécessaire, mais la position obtenue est relative et dérive — sauf recalage sur une référence externe.

**Ce qui bloque.** **Le coût de maintien de la carte**, qui croît avec la surface couverte et qui est le facteur limitant réel de l'extension. **La dérive** pour l'approche sans carte. **Les environnements peu texturés ou répétitifs**, où la localisation visuelle échoue — couloirs identiques, tunnels, champs.

**Ce que cela implique.** Le choix entre les deux approches est un arbitrage entre **coût de préparation** et **précision garantie**. C'est un cas où le verrou est logistique — qui relève la carte, à quelle fréquence, et qui paie — plutôt que technique.

**À ne pas confondre avec.** **Le positionnement par satellite** (ch. 6), qui donne une position absolue mais insuffisamment précise et indisponible en intérieur, en tunnel ou en environnement urbain dense.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Le maintien de cartographies fines à grande échelle reste un coût significatif et un frein à l'extension géographique.
> 🔄 **À revoir si** un système atteint des performances de localisation suffisantes sans cartographie préétablie dans un environnement urbain dense.

**Renvois** — Couche : percevoir, décider · Convergence : autonomie mobile (39).

---


## Clôture de la couche D — Agir

### Ce que les vingt et une entrées font apparaître

**Un. La difficulté suit l'environnement, pas la machine.** Le classement du chapitre 14 le rendait visible ; les chapitres 16 et 17 le confirment. Une même capacité — se déplacer, saisir, décider — change de difficulté d'un ordre de grandeur selon que l'environnement est préparé, semi-structuré, ouvert mais réservé, ou partagé avec des humains non prévenus. **C'est la variable dominante de toute la couche, et elle n'apparaît dans aucune fiche technique.**

**Deux. Le verrou est institutionnel dans huit entrées sur vingt et une.** Drones — autorisation du vol hors vue. Véhicules autonomes — démonstration de sûreté et assurabilité. Maritime — droit international. Aérien — certification. Ferroviaire — infrastructure et financement. Robotique médicale — preuve clinique et autorisation. Essaims — vérifiabilité du comportement. Autonomie supervisée — responsabilité. **Dans aucun de ces cas la capacité technique n'est le facteur limitant.**

**Trois. Le ratio d'opérateurs par machine est la grandeur économique cachée de la couche.** Elle apparaît en téléopération, en autonomie supervisée, en véhicules autonomes et en systèmes maritimes. Elle décide de la rentabilité de tout déploiement, et elle est presque jamais publiée. **Si une seule grandeur devait être surveillée dans ce domaine, ce serait celle-là.**

**Quatre. La défaillance silencieuse d'origine mécanique complète le relevé du volume.** Jeu de réducteur, usure de préhenseur, dérive de structure : trois formes d'une même chose — une machine précise selon ses capteurs et imprécise en réalité, parce que la déformation se situe en aval de la mesure.

### Ce que la couche livre aux convergences

| Dossier | Entrées mobilisées |
|---|---|
| **36 — Robotique généraliste** | robotique industrielle, robots mobiles, manipulation, locomotion, souple, humanoïde, actionneurs, mains, téléopération |
| **39 — Autonomie mobile** | drones, terrestres, maritimes, essaims, autonomie supervisée, véhicules autonomes, domaine d'emploi, autres modes, localisation |

**Neuf entrées pour chacun des deux dossiers.** La couche D est la plus directement mobilisée de l'atlas — et c'est la seule dont les entrées se répartissent presque exclusivement entre deux dossiers, sans dispersion.

### Vérification de la thèse du volume

Le dossier 39 mobilise neuf entrées de cette couche et dix de la couche *percevoir*, soit dix-neuf sur les trente-six entrées attendues par l'ensemble des dossiers. **Et son maillon en retard est ailleurs** : dans la démonstration de sûreté, qui relève de la couche *vérifier*.

Le dossier 36 mobilise neuf entrées de cette couche et huit de la couche *apprendre*. **Son maillon en retard est partagé** entre la fiabilité de la manipulation — couche *agir* — et les données physiques — couche *apprendre*. C'est la contradiction partielle relevée au squelette, et elle se confirme.

**Bilan intermédiaire : deux vérifications, une contradiction partielle.** La formulation affaiblie proposée au squelette tient.

---

---

---

### Couche E — Fabriquer

---


## Chapitre 18 — Fabrication avancée

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé deux contraintes : on ne choisit jamais un matériau seul mais un couple matériau-procédé, et le rendement de production gouverne le coût sans apparaître dans aucune fiche technique. Ce chapitre traite des **procédés** et de leur instrumentation.
>
> **Une observation qui vaut pour les cinq entrées.** Dans cette couche, la nouveauté ne vient presque jamais d'une capacité inédite mais d'un **déplacement du seuil de rentabilité** : ce qui était possible en petite série devient possible en grande, ou l'inverse.
>
> **Cinq entrées.**

---

### ◆◆◆ Fabrication additive

**Niveau** — procédé · **Couche** — fabriquer

**En une phrase.** Construire une pièce en ajoutant de la matière couche par couche, plutôt qu'en retirant de la matière d'un bloc ou en la déformant dans un moule.

**Pourquoi on en parle.** Parce que c'est la technologie dont la trajectoire a été **la plus mal anticipée** de la période récente — annoncée comme remplaçant l'usine, elle a réussi ailleurs — et parce que comprendre pourquoi éclaire toute la couche.

**Comment ça fonctionne.** Une source d'énergie ou un dispositif de dépôt construit la pièce par strates successives, à partir d'un modèle numérique. Les procédés diffèrent par le matériau — polymère, métal, céramique — et par le mécanisme : fusion sur lit de poudre, dépôt de matière fondue, projection, photopolymérisation.

**L'économie du procédé est ce qui compte, et elle est particulière.** Le coût unitaire dépend peu de la complexité de la pièce — une géométrie compliquée ne coûte pas plus qu'une simple — et **il ne baisse presque pas avec le volume**, puisqu'il n'y a pas d'outillage à amortir. C'est exactement l'inverse d'un procédé de moulage, dont l'outillage coûte cher et dont le coût unitaire s'effondre en série.

**D'où le croisement.** Additif et formatif se croisent à un volume donné : en dessous, l'additif gagne ; au-dessus, il perd. **La question n'est donc jamais « quel procédé est le meilleur » mais « à quel volume le croisement se produit-il »** — et ce volume dépend de la complexité de la pièce, du matériau et du coût de l'outillage évité.

**Où vous rencontrerez le terme.** Aéronautique · médical et implants sur mesure · outillage · prototypage · pièces de rechange · énergie.

**Ce que ça permet.** Des géométries impossibles autrement — canaux internes, structures allégées, échangeurs intégrés · la pièce unique sans surcoût de complexité · la consolidation, une pièce imprimée remplaçant un assemblage de plusieurs · la production sans stock.

**Ce qui bloque.** **La cadence**, qui reste faible : une pièce se construit en heures. **La qualification**, dominante dans les secteurs réglementés : démontrer qu'une pièce imprimée est conforme suppose de qualifier le procédé, la machine, le lot de poudre et souvent chaque pièce — ce qui coûte davantage que la production. **L'état de surface et les tolérances**, souvent insuffisants sans reprise par usinage. Et **la reproductibilité entre machines**, y compris identiques.

**Ce que cela implique — et cela referme un cas ouvert au volume 1.** La fabrication additive n'a pas échoué : **elle occupe une zone du plan volume-complexité où le procédé traditionnel n'a jamais été bon**. L'erreur de prédiction ne portait pas sur la technologie mais sur le domaine d'application annoncé.

**À ne pas confondre avec.** **Le prototypage rapide**, qui fut son premier usage et reste le plus répandu — produire une pièce d'essai n'exige aucune qualification. **La fabrication distribuée**, qui est une doctrine d'organisation et non un procédé.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Production de série établie en aéronautique et en médical sur des pièces à forte valeur ; croissance continue de la taille des machines et du nombre de matériaux qualifiés.
> 🔄 **À revoir si** la cadence d'une machine de production atteint un ordre de grandeur au-dessus de la génération courante à qualité constante — ce qui déplacerait le volume de croisement.

**Renvois** — Couche : fabriquer · Courant : Advanced Manufacturing (ch. 35) · Convergence : découverte scientifique (37).

---

### ◆◆ Usines autonomes

**Niveau** — système · **Couche** — fabriquer, décider

**En une phrase.** Des installations de production capables d'ajuster leurs paramètres, de détecter leurs dérives et de traiter certaines anomalies sans intervention humaine.

**Comment ça fonctionne.** Trois étages, souvent confondus. La **collecte** — instrumenter les équipements et remonter les données. L'**analyse** — détecter dérives et anomalies. L'**action** — ajuster automatiquement un paramètre de procédé. Le premier étage est répandu, le deuxième courant, **le troisième est rare** : il suppose de confier une commande à un système dans un contexte où une erreur détruit de la matière et peut blesser.

**Ce que ça permet.** Réduire les rebuts par correction précoce · anticiper une panne · maintenir la qualité malgré des variations de matière première · réduire le temps de réglage lors d'un changement de série.

**Ce qui bloque.** **L'instrumentation d'un existant.** Équiper une ligne neuve est une décision de conception ; équiper une ligne en service suppose des arrêts, des reprises et une intégration à des automates parfois anciens — **c'est là que les projets échouent**, et non sur l'analyse. S'y ajoutent l'hétérogénéité des équipements, dont l'âge s'étale sur plusieurs décennies, et la difficulté de distinguer une anomalie d'un changement légitime.

**Ce que cela implique.** Le facteur limitant est **l'âge du parc machine**, pas la sophistication de l'analyse. Un site moyen fait cohabiter des équipements de quatre générations, et le rythme de transformation suit celui des investissements — pas celui des logiciels.

**À ne pas confondre avec.** **L'automatisation** au sens classique, qui exécute une séquence sans ajuster. **La supervision**, qui observe sans agir.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour la collecte et l'analyse, 🔬 émergent pour l'action automatique sur procédé critique.
> 🔄 **À revoir si** l'ajustement automatique de paramètres devient pratique courante sur des procédés à forte valeur ajoutée.

**Renvois** — Couche : fabriquer, décider · Courants : Industrie 4.0, smart factory (ch. 34).

---

### ◆◆ Métrologie avancée

**Niveau** — capacité · **Couche** — fabriquer, percevoir

**En une phrase.** Mesurer ce qui a été produit, avec une précision et une rapidité permettant de corriger le procédé plutôt que de trier après coup.

**Pourquoi on en parle.** Parce que **c'est la condition de tout le reste de la couche**, et parce qu'elle est invisible : personne n'annonce un progrès de métrologie, alors qu'aucun progrès de procédé ne se qualifie sans elle.

**Comment ça fonctionne.** Le déplacement décisif est le passage de la mesure **hors ligne** — prélever un échantillon, l'emporter au laboratoire — à la mesure **en ligne**, intégrée au flux de production. Cela change la nature de l'information : au lieu de constater un défaut après coup, on observe une dérive avant qu'elle produise des rebuts.

Les moyens vont de la vision industrielle à la tomographie, qui permet d'inspecter l'intérieur d'une pièce sans la détruire — capacité décisive pour les pièces imprimées, dont les défauts sont internes.

**Ce qui bloque.** **Le temps de mesure.** Une mesure fine est lente ; une mesure rapide est grossière. C'est le triangle d'arbitrage de la couche *percevoir*, appliqué à la production, et il détermine ce qu'on peut contrôler à cent pour cent et ce qu'on doit échantillonner. S'y ajoutent le **coût des moyens** et la **traçabilité des étalons**, sans laquelle une mesure n'est pas opposable.

**Ce que cela implique.** **On ne peut pas maîtriser ce qu'on ne mesure pas.** Un procédé nouveau ne devient industriel que lorsque sa métrologie existe — et le délai de développement de cette métrologie est souvent supérieur à celui du procédé lui-même. C'est une cause fréquente et rarement citée du retard entre démonstration et production.

**À ne pas confondre avec.** **Le contrôle qualité** au sens du tri, qui écarte les pièces non conformes sans corriger la cause.

> ⏱ **État au 23/08/2026** — 🏭 déployé, en extension vers la mesure en ligne et l'inspection non destructive.
> 🔄 **À revoir si** l'inspection interne non destructive devient assez rapide pour être appliquée à cent pour cent d'une production de série.

**Renvois** — Couche : fabriquer, percevoir.

---

### ◆◆◆ Jumeaux numériques industriels

**Niveau** — ambigu, et c'est le sujet · **Couche** — fabriquer, calculer, décider

**En une phrase.** Un modèle numérique d'un système réel, alimenté par les données de ce système, utilisé pour observer, simuler ou décider.

**Pourquoi cette entrée est en ◆◆◆.** Non pour sa difficulté technique, mais parce que **le terme désigne cinq objets différents** dont les exigences n'ont rien de commun — et que cette confusion produit des attentes désalignées dans presque tous les projets qui l'emploient.

**Les cinq objets, du plus simple au plus exigeant.**

**Une maquette tridimensionnelle** — une représentation géométrique, sans données en temps réel. Utile en conception et en formation.

**Un modèle de simulation** — reproduisant le comportement physique, alimenté par des paramètres et non par des mesures. Utile en dimensionnement.

**Un tableau de bord synchronisé** — affichant l'état courant à partir de capteurs. C'est le cas le plus fréquent de ce qui est vendu sous ce nom, et le moins exigeant.

**Un modèle prédictif** — capable d'anticiper l'évolution du système et donc de détecter une dérive avant qu'elle soit visible.

**Un modèle de commande** — dont les prédictions alimentent directement des décisions d'exploitation. C'est le seul qui exige une fidélité démontrée, et il est rare.

**Ce qui bloque.** **L'écart au réel et sa dérive.** Un modèle calé sur un système neuf s'écarte progressivement à mesure que le système s'use, se salit, se répare. **Sans procédure de recalage, le jumeau devient faux sans le signaler** — c'est une défaillance silencieuse, et c'est le mode de défaillance dominant de ces dispositifs.

S'y ajoutent le **coût d'instrumentation**, la **qualité des données** entrantes, et l'**effort de modélisation**, qui est souvent sous-estimé d'un facteur important.

**Ce que cela implique.** **La question n'est jamais « le jumeau est-il exact ? »** — il ne l'est pas — **mais « qu'a-t-il été construit pour ignorer, et cet aspect est-il négligeable dans mon usage ? »**. Un modèle qui ignore la thermique convient pour la logistique et pas pour la maintenance.

**À ne pas confondre avec.** **Une simulation**, qui n'est pas synchronisée sur un système réel. **Un modèle du monde** (ch. 13), qui est appris et vise la généralisation plutôt que la fidélité à un exemplaire.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour les trois premiers niveaux, 🔬 émergent pour le modèle de commande.
> 🔄 **À revoir si** une pratique de recalage périodique devient une exigence normalisée, ce qui rendrait la dérive traitable.

**Renvois** — Couche : fabriquer, calculer · Courants : digital twin, industrial metaverse (ch. 34).

---

### ◆ Fabrication distribuée

**Niveau** — doctrine · **Couche** — fabriquer

**En une phrase.** Produire près du lieu d'usage, dans de petites unités, plutôt que dans de grandes usines centralisées.

**Ce qui bloque.** **L'économie d'échelle joue contre.** Une petite unité produit à un coût unitaire supérieur, dispose de moins de compétences et amortit moins bien ses équipements. **La qualification** devient un problème multiplié : chaque site doit être qualifié pour chaque produit dans les secteurs réglementés.

**Ce que cela implique.** La doctrine est pertinente là où **le transport domine le coût** — pièces volumineuses, produits urgents, sites isolés — et là où la petite série est la règle. Elle ne l'est pas ailleurs, ce qui explique l'écart entre son attractivité conceptuelle et son déploiement réel.

**À ne pas confondre avec.** **La relocalisation**, qui déplace la production sans la fragmenter.

> ⏱ **État au 23/08/2026** — 🔬 émergent, sur des niches établies — pièces de rechange, dispositifs médicaux sur mesure.
> 🔄 **À revoir si** un secteur réglementé adopte une qualification de procédé transférable entre sites.

**Renvois** — Couche : fabriquer.

---
