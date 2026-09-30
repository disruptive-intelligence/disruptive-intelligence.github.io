---
title: Chapitre 14 — Robotique générale
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - ../index.md
- - Partie I — Lire une frontière technologique
  - index.md
---

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé deux contraintes : la boucle masse-énergie, qui borne toute machine emportant son énergie, et le fait que manipuler est structurellement plus difficile que se déplacer. Ce chapitre traite des **familles de machines** et de ce qui les sépare.
>
> **Un principe de classement.** Les entrées ne sont pas ordonnées par degré d'avancement mais par **environnement d'opération** — du plus structuré au moins structuré. C'est la variable qui décide de la difficulté, bien avant la sophistication de la machine.
>
> **Huit entrées.**

---

## ◆◆ Robotique industrielle et cobots

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

## ◆◆ Robots mobiles autonomes

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

## ◆◆◆ Manipulation et préhension

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

## ◆◆ Locomotion

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

## ◆◆ Robotique souple

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

## ◆ Microrobotique

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

## ◆◆ Robotique médicale

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

## ◆ Robotique agricole

**Niveau** — famille · **Couche** — agir

**En une phrase.** Des machines autonomes pour le désherbage, la récolte, le semis ou la surveillance de cultures.

**Ce qui bloque.** **La saisonnalité.** Une machine utilisable trois semaines par an doit amortir son coût sur ces trois semaines — c'est la contrainte économique dominante, et elle explique la préférence pour des machines polyvalentes ou louées. S'y ajoutent **la variabilité du végétal**, qui est un cas extrême du problème de manipulation, et **les conditions** — boue, poussière, pluie, luminosité changeante.

**Ce que cela implique.** Les usages qui réussissent sont ceux où le travail humain est cher, rare ou pénible, et où la tâche est répétitive : désherbage mécanique, surveillance, traite. La récolte de fruits fragiles reste un problème ouvert, et c'est précisément un problème de manipulation.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des segments 🏭 déployés — traite, désherbage sur certaines cultures.
> 🔄 **À revoir si** un récolteur robotisé de fruits atteint un coût par kilogramme compétitif avec la main-d'œuvre dans une région à coût du travail élevé.

**Renvois** — Couche : agir.

---
