---
title: ◆◆◆ Détection de sortie de domaine
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

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


### ◆◆ Vérification formelle

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


### ◆◆ Dossiers de sûreté

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


### ◆◆ Dégradation maîtrisée

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


## Clôture de la couche H — Vérifier


### Ce que les quinze entrées font apparaître

**Un. Toute vérification suppose un ancrage, et l'ancrage est toujours un déplacement de confiance.** Racine matérielle, enclave, attestation : dans les trois cas, on ne supprime pas la confiance, on la déplace vers un point jugé acceptable. **La question utile n'est jamais « ce système est-il sûr ? » mais « à qui ce système me demande-t-il de faire confiance ? »**

**Deux. Le déplacement conceptuel majeur de la couche est de renoncer à prouver le système pour prouver son enveloppe.** C'est ce que fait l'architecture de sûreté, et c'est ce qui rend déployable un système dont on ne peut démontrer le comportement. **La garantie ne porte pas sur ce que le système fera, mais sur ce qu'il ne pourra pas faire.**

**Trois. Le verrou est institutionnel dans cinq entrées sur quinze.** Architecture de sûreté, dossiers de sûreté, dégradation maîtrisée, sûreté mémoire, crypto-agilité : dans chaque cas, les dispositifs techniques existent et **leur reconnaissance par un référentiel est le facteur limitant**.

**Quatre. Une signature n'atteste jamais la véracité.** Cette limite apparaît dans trois entrées — provenance, attestation, identité machine — et elle avait été posée à la couche *percevoir*. **C'est probablement la formulation la plus utile de tout l'atlas pour un lecteur venant de la sécurité des systèmes d'information.**


### Ce que la couche livre aux convergences

| Dossier | Entrées mobilisées |
|---|---|
| **38 — Intelligence distribuée** | racine de confiance, attestation, identité machine |
| **39 — Autonomie mobile** | architecture de sûreté, détection de sortie de domaine, vérification formelle, dossiers de sûreté, dégradation maîtrisée |
| **41 — Biologie programmable** | *voir biosécurité, ch. 20* |

**Le dossier 39 mobilise cinq entrées de cette couche — et son maillon en retard est ici.** C'est la vérification la plus nette de la thèse du volume : la convergence la plus dépendante des couches *percevoir* et *agir* a son verrou dans *vérifier*.

---

---

---


### Couche I — Interagir

---
