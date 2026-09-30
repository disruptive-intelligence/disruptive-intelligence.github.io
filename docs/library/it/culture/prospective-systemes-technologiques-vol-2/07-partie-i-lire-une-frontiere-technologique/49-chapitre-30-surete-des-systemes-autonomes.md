---
title: Chapitre 30 — Sûreté des systèmes autonomes
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - ../index.md
- - Partie I — Lire une frontière technologique
  - index.md
---

> **Ce que ce chapitre ajoute.** Les chapitres 28 et 29 traitaient de la confiance dans **ce qu'un système est**. Celui-ci traite de la confiance dans **ce qu'un système fait** — et particulièrement lorsqu'il décide.
>
> **La première entrée absorbe six termes du marché.** Runtime monitoring, runtime verification, runtime assurance, architecture Simplex, safety envelope, shield layer : ce ne sont pas six technologies mais **les couches d'une même architecture**. Les traiter séparément les rendrait incompréhensibles.
>
> **Cinq entrées.**

---

## ◆◆◆ Architecture de sûreté d'un système autonome — *entrée comparative*

**Niveau** — système · **Couche** — vérifier

**En une phrase.** L'ensemble des dispositifs qui permettent de faire confiance à un système qui décide — organisés en quatre couches complémentaires.

**Pourquoi cette entrée est comparative.** Parce que les termes du domaine circulent comme s'ils désignaient des technologies concurrentes, alors qu'ils désignent **des étages d'une même construction**. Comprendre l'ordre est plus utile que connaître les définitions.

**Le problème à résoudre.** Un système classique se vérifie avant déploiement : on démontre qu'il se comporte correctement sur toutes les entrées possibles. Un système apprenant ne le permet pas — **on ne peut pas énumérer les entrées d'un système ouvert sur le monde**. La vérification exhaustive étant impossible, il faut lui substituer autre chose.

### Les quatre couches, dans l'ordre

**① OBSERVER — la surveillance en exploitation.**
Un dispositif indépendant observe le système pendant qu'il fonctionne et enregistre son état, ses entrées, ses sorties. Il ne juge pas : il constate. C'est la base de tout le reste, et c'est aussi ce qui permet le retour d'expérience.
*Terme du domaine : runtime monitoring.*

**② VÉRIFIER — le contrôle de propriétés en temps réel.**
On exprime des propriétés qui doivent rester vraies — « la distance à l'obstacle ne descend jamais sous ce seuil », « la commande reste dans cette plage » — et un dispositif vérifie en continu qu'elles le sont. **Il détecte une violation, il ne l'empêche pas.**
*Terme du domaine : runtime verification.*

**③ CONTRAINDRE — l'intervention qui garantit.**
Un dispositif simple, vérifiable par les méthodes classiques, s'interpose entre le système apprenant et les actionneurs. Il laisse passer les commandes qui préservent la sûreté et **substitue une commande sûre à celles qui ne le font pas**. Le système apprenant propose ; le dispositif de contrainte dispose.

C'est le principe le plus important de cette entrée : **on ne cherche pas à prouver que le système apprenant est sûr, on l'entoure d'un dispositif dont on peut prouver qu'il l'est.** La garantie ne porte pas sur l'intelligence mais sur son enveloppe.

*Termes du domaine : shield layer, architecture Simplex, safety envelope, runtime assurance.*

**④ DÉMONTRER — l'argumentation opposable.**
Un dossier structuré qui expose la revendication de sûreté, les arguments qui la soutiennent et les preuves qui étayent chaque argument. C'est ce qu'on présente à un régulateur, à un assureur, à un tribunal.
*Termes du domaine : safety case, assurance case.*

### Ce que l'architecture permet

**Déployer un système dont on ne peut pas démontrer le comportement**, en garantissant non pas ce qu'il fera mais ce qu'il ne pourra pas faire. **C'est le déplacement conceptuel décisif** du domaine : de la preuve du système à la preuve de son enveloppe.

### Ce qui bloque

**La définition des propriétés à garantir.** Écrire ce qui ne doit jamais arriver est plus difficile qu'il n'y paraît, et une propriété mal formulée produit soit des interventions incessantes qui rendent le système inutilisable, soit une garantie vide.

**Le conservatisme du dispositif de contrainte.** Plus il est prudent, plus il intervient, plus le système perd de sa capacité. **L'arbitrage entre sûreté et performance se joue entièrement ici**, et il est explicite — ce qui est préférable à un arbitrage implicite.

**La détection de sortie de domaine**, qui conditionne le déclenchement et fait l'objet de l'entrée suivante.

**Et le cadre.** Ces architectures sont reconnues dans certains référentiels sectoriels et pas dans d'autres. **Leur acceptation par les autorités est le facteur limitant du déploiement**, non leur disponibilité technique.

**Ce que cela implique.** La question à poser devant tout système autonome n'est pas « son modèle est-il fiable ? » mais **« quelle est son architecture de sûreté, et sur quelles propriétés porte la garantie ? »**

**À ne pas confondre avec.** La **sécurité informatique**, qui protège contre un adversaire — la carte de couche a établi que les hypothèses des deux disciplines sont opposées. Et les **essais**, qui vérifient avant déploiement ce que ces dispositifs vérifient pendant.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Architectures établies dans l'aéronautique et l'industrie ; extension aux systèmes apprenants en cours d'intégration dans les référentiels.
> 🔄 **À revoir si** un référentiel de certification accepte explicitement une architecture de ce type comme démonstration de sûreté pour un système apprenant.

**Renvois** — Couche : vérifier · Convergence : autonomie mobile (39) · Voir aussi : domaine de conception opérationnelle (ch. 17), volume 1 chapitre 16.

---

## ◆◆◆ Détection de sortie de domaine

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Reconnaître qu'une situation s'écarte de celles pour lesquelles le système a été validé — avant qu'il ne produise une réponse erronée avec assurance.

**Pourquoi cette entrée est majeure.** Parce que **c'est le verrou de l'autonomie apprenante**, et parce que le problème est plus difficile qu'il n'y paraît : il s'agit de reconnaître ce qu'on n'a jamais vu.

**Le problème.** Un système appris est bon là où ses données sont denses. Confronté à une entrée éloignée, **il ne produit pas d'erreur : il produit une sortie plausible avec la même assurance apparente**. Rien dans la forme du résultat ne distingue une interpolation d'une extrapolation.

**Les approches, et leurs limites.** Estimer une **incertitude** et alerter quand elle est élevée — mais un modèle peut être confiant à tort, et l'est précisément là où il extrapole. Mesurer une **distance à la distribution d'entraînement** — mais cette distance est difficile à définir dans un espace de grande dimension. Comparer les sorties de **plusieurs modèles** entraînés différemment, en supposant qu'ils divergeront sur les cas inhabituels — hypothèse d'indépendance qui n'est pas garantie. Ou surveiller des **propriétés physiques** de la situation plutôt que la sortie du modèle, ce qui est souvent la voie la plus robuste.

**Ce qui bloque.** **La définition même du domaine.** Décrire exhaustivement les conditions de validité d'un système est difficile ; un domaine trop étroit rend le système inutilisable, un domaine trop large ne peut pas être validé.

**Le compromis fausses alertes contre détections manquées.** Un détecteur trop sensible déclenche constamment ; un détecteur trop permissif laisse passer les cas dangereux. **Il n'existe pas de réglage sans arbitrage.**

**Et le fait qu'on ne peut pas tester ce qu'on n'a pas.** Évaluer un détecteur de situations inconnues suppose de disposer de situations inconnues — contradiction pratique qui rend l'évaluation partielle par construction.

**Ce que cela implique.** C'est le même problème sous trois noms dans ce volume : **la panne silencieuse du capteur, l'échec silencieux du modèle, la sortie de domaine du système autonome**. Un système qui cesse de fonctionner correctement mais continue de produire quelque chose de crédible est plus dangereux qu'un système qui s'arrête.

**À ne pas confondre avec.** La **détection d'anomalie** dans les données, qui cherche un événement inhabituel dans un flux ; ici, on cherche à savoir si le système lui-même est hors de sa zone de compétence.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Méthodes nombreuses, aucune dominante, évaluation comparative difficile faute de références partagées.
> 🔄 **À revoir si** une méthode d'évaluation standardisée de la détection hors domaine est adoptée dans un secteur réglementé.

**Renvois** — Couche : vérifier · Convergences : autonomie mobile (39), robotique généraliste (36) · Voir aussi : modèles du monde (ch. 13), capteurs inertiels (ch. 6).

---

## ◆◆ Vérification formelle

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Démontrer mathématiquement qu'un système satisfait une propriété, pour toutes les entrées possibles.

**Ce que ça permet.** Une garantie d'une nature différente de celle des essais : **les essais montrent l'absence de défaut sur les cas testés, la vérification formelle montre l'absence de défaut sur tous les cas** — dans les limites de ce qui a été modélisé.

**Ce qui bloque — et il faut être précis sur la portée.** **La taille.** La complexité de la vérification croît rapidement avec celle du système ; au-delà d'une certaine taille, elle devient impraticable. On vérifie donc des composants, pas des systèmes entiers.

**La modélisation.** On vérifie un modèle du système, pas le système. **Si le modèle omet un aspect, la preuve ne dit rien de cet aspect** — c'est la limite la plus importante et la moins comprise.

**Les systèmes apprenants.** Vérifier formellement un réseau de neurones est possible sur des propriétés simples et des tailles modestes, et reste hors de portée pour les modèles de grande taille. **C'est pourquoi l'architecture de sûreté ne cherche pas à vérifier le modèle mais son enveloppe** — dispositif simple, donc vérifiable.

**Ce que cela implique.** La vérification formelle est **un outil de composant, pas de système** — et c'est précisément ce qui la rend utile dans l'architecture de la première entrée : elle prouve la couche de contrainte, qui est simple par conception.

**À ne pas confondre avec.** Les **essais exhaustifs**, qui ne le sont jamais. Et l'**analyse statique**, qui détecte des classes d'erreurs sans démontrer une propriété.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour des composants critiques dans l'aéronautique, le ferroviaire et le matériel ; 🔬 émergent pour les composants d'autonomie.
> 🔄 **À revoir si** la vérification de propriétés utiles devient praticable sur des modèles de taille industrielle.

**Renvois** — Couche : vérifier.

---

## ◆◆ Dossiers de sûreté

**Niveau** — doctrine · **Couche** — vérifier

**En une phrase.** Un document structuré qui argumente qu'un système est suffisamment sûr pour son usage, en reliant explicitement revendications, arguments et preuves.

**Pourquoi cette entrée existe.** Parce que **c'est la forme sous laquelle la sûreté devient opposable** — à un régulateur, à un assureur, à un tribunal. Sans elle, une architecture technique ne se traduit pas en autorisation.

**Comment ça fonctionne.** Le document part d'une revendication — « ce système est acceptablement sûr dans ce domaine d'emploi » — la décompose en sous-revendications, et rattache à chacune des éléments de preuve : essais, analyses, vérifications formelles, retours d'exploitation. **La structure de l'argumentation est explicite**, ce qui permet de la contester point par point.

**Ce que ça permet.** Rendre discutable un raisonnement de sûreté · identifier les points faibles de l'argumentation · faire évoluer le dossier quand le système évolue.

**Ce qui bloque.** **La subjectivité du seuil.** « Suffisamment sûr » suppose un référentiel d'acceptabilité, qui relève d'un choix de société et non d'une mesure technique. **La confiance dans les preuves**, dont la qualité varie. Et **la mise à jour** : un système qui évolue exige un dossier qui évolue, ce qui est lourd et constitue un frein direct à l'amélioration continue.

**Ce que cela implique.** Le dossier de sûreté est **le point de rencontre entre technique et institution**. C'est là que se manifeste le verrou identifié tout au long de ce volume : la capacité technique existe, la démonstration opposable manque.

> ⏱ **État au 23/08/2026** — 🏭 déployé dans les secteurs réglementés, 🔬 émergent pour les systèmes apprenants.
> 🔄 **À revoir si** une méthodologie de dossier de sûreté pour système apprenant est reconnue par une autorité sectorielle.

**Renvois** — Couche : vérifier.

---

## ◆◆ Dégradation maîtrisée

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Continuer à fonctionner de manière réduite mais sûre lorsqu'une partie du système est défaillante ou hors de son domaine.

**Les quatre réponses possibles**, avec leur coût, établies au volume 1 et reprises ici comme référence.

**S'arrêter en sécurité.** Le moins coûteux, valable seulement si l'arrêt est effectivement sûr — ce qui n'est pas le cas d'un véhicule sur voie rapide ni d'un aéronef en vol.

**Continuer malgré la défaillance.** Exige une redondance sur toute la chaîne — perception, calcul, alimentation, actionneurs — et non sur le seul composant jugé fragile. **Le saut de coût est considérable** et régulièrement sous-estimé.

**Rendre la main.** Suppose un humain disponible, attentif et capable de reprendre en quelques secondes — ce que la couche *agir* a montré être une hypothèse fragile.

**Réduire les capacités.** Souvent la meilleure réponse et la plus difficile à concevoir : il faut avoir prévu à l'avance **ce qui peut être abandonné** et dans quel ordre.

**Ce qui bloque.** **La conception a priori.** Un mode dégradé ne s'improvise pas : il se conçoit, se spécifie et se teste — et tester un mode dégradé suppose de provoquer la défaillance, ce qui est coûteux et parfois impossible.

**Et l'information.** Un système qui se dégrade doit le signaler — à l'opérateur, à l'exploitant, aux autres systèmes qui en dépendent. **Une dégradation silencieuse est le pire des cas**, et c'est le fil rouge de tout ce volume.

**À ne pas confondre avec.** La **redondance**, qui est un moyen ; la dégradation maîtrisée est une propriété du comportement d'ensemble.

> ⏱ **État au 23/08/2026** — 🏭 déployé dans les secteurs à sûreté ancienne, 🔬 émergent ailleurs.
> 🔄 **À revoir si** la spécification d'un mode dégradé devient une exigence explicite pour les systèmes autonomes dans un secteur civil.

**Renvois** — Couche : vérifier · Voir aussi : autonomie supervisée (ch. 16), volume 1 chapitre 21.

---
