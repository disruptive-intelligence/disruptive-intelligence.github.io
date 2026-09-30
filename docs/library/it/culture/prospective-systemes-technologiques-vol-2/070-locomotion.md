---
title: ◆◆ Locomotion
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

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
