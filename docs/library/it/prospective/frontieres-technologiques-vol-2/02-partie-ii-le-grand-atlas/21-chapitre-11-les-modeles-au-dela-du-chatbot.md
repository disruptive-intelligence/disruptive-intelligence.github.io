---
title: Chapitre 11 — Les modèles au-delà du chatbot
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie II — Le grand atlas
  - index.md
---

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé l'échange fondamental : l'apprentissage troque de la certitude contre de la capacité. Ce chapitre traite des **objets** qui réalisent cet échange — comment ils sont construits, ce qui borne leur performance, et ce qu'ils coûtent à l'usage.
>
> **Une discipline propre à cette couche.** Aucune fiche ne nomme de modèle, d'acteur ni de score. Ce n'est pas de la prudence : c'est la condition pour que ces fiches restent valides dans trois ans. Les états sont qualitatifs, et c'est ce qui les rend durables.
>
> **Six entrées**, dont deux majeures.

---

## ◆◆◆ Modèles de fondation

**Niveau** — plateforme · **Couche** — apprendre et décider

**En une phrase.** Un modèle entraîné à très grande échelle sur des données larges, destiné à être adapté à de nombreuses tâches plutôt qu'à une seule.

**Pourquoi on en parle.** Parce que c'est l'objet autour duquel s'est réorganisée toute une industrie — et parce que le terme désigne simultanément une manière d'entraîner et un rapport de dépendance.

**Comment ça fonctionne.** L'entraînement se fait en deux temps. Une phase de **pré-entraînement** expose le modèle à un très grand volume de données avec un objectif simple — prédire ce qui manque —, ce qui lui fait acquérir des régularités générales. Une phase d'**adaptation** l'oriente ensuite vers des usages, par apprentissage supervisé sur des exemples choisis puis par ajustement sur des préférences exprimées.

**Ce qui a rendu cette approche dominante** est une observation empirique : la performance s'améliore de façon régulière quand on augmente conjointement la taille du modèle, le volume de données et la quantité de calcul. **Cette régularité est empirique, pas une loi.** Elle décrit ce qui a été observé sur une plage donnée ; elle ne garantit ni sa poursuite, ni l'apparition d'une capacité donnée à un niveau donné, et elle porte sur des mesures agrégées qui masquent des comportements très variables tâche par tâche.

**Où vous rencontrerez le terme.** Partout — et c'est le problème : il désigne selon le contexte un objet technique, un produit, ou un fournisseur.

**Ce que ça permet.** Obtenir un comportement utile sur une tâche sans disposer d'un jeu de données propre à cette tâche — ce qui a supprimé la principale barrière d'entrée de l'apprentissage automatique.

**Ce qui bloque.** **La densité des données.** Un modèle est bon là où ses données sont denses ; l'adaptation en aval ne crée pas de compétence là où le socle n'en avait pas. **Le coût d'entraînement**, qui concentre l'activité chez un petit nombre d'acteurs capables de l'engager. Et **l'absence de garantie** : on mesure une performance sur un échantillon, on ne démontre pas un comportement.

**De quoi ça dépend.** Accélérateurs · énergie · données et droits associés · compétences rares · infrastructure d'entraînement.

**Ce que cela implique.** Construire sur un socle qu'on n'a pas entraîné, dont on ne connaît pas les données et qui peut changer de comportement à chaque version est **une dépendance au sens strict** — au même titre qu'une dépendance à un fournisseur unique de composant. Elle est rarement traitée comme telle.

**Sûreté et sécurité.** Intégrité des données d'entraînement · dépendance à un fournisseur tiers non auditable · reproductibilité d'un comportement entre deux versions.

**À ne pas confondre avec.** **Un produit**, qui inclut une interface, une politique d'usage et une infrastructure. **Un modèle spécialisé**, entraîné pour une tâche unique et qui la surpasse souvent.

**Termes voisins.** *LLM* désigne la sous-famille textuelle. *Frontier model* désigne une catégorie réglementaire, non technique.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Écart croissant entre les modèles les plus grands et les modèles compacts sur les tâches courantes ; concentration persistante de la capacité d'entraînement.
> 🔄 **À revoir si** l'augmentation conjointe de la taille, des données et du calcul cesse de produire des gains mesurables sur des tâches d'intérêt pratique.

**Renvois** — Couche : apprendre et décider · Courants : IA générative, Frontier AI (ch. 32) · Convergences : découverte scientifique (37), biologie programmable (41).

---

## ◆◆◆ Modèles de raisonnement

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Des modèles qui consacrent davantage de calcul à produire une réponse, en décomposant le problème avant de conclure.

**Pourquoi on en parle.** Parce que c'est le déplacement le plus significatif de la période : le calcul est passé de l'entraînement vers l'usage — et parce que le mot « raisonnement » induit en erreur.

**Comment ça fonctionne.** Plutôt que de produire directement une réponse, le modèle génère une suite d'étapes intermédiaires, explore plusieurs pistes, revient sur certaines, puis conclut. Il consomme donc davantage à chaque requête, et cette dépense supplémentaire améliore effectivement les résultats sur des tâches à structure logique ou mathématique.

**Ce qui compte pour bien comprendre.** Ce déplacement ouvre un **arbitrage nouveau** : à performance donnée, on peut soit entraîner un modèle plus grand une fois, soit dépenser davantage à chaque appel. Le second choix est réversible et se règle par usage ; le premier est un investissement.

**Ce que ça permet.** Des résultats nettement meilleurs sur des tâches où la réponse directe échouait · un réglage du compromis qualité-coût requête par requête.

**Ce qui bloque.** **Le coût par requête**, qui devient la variable dominante d'un service très utilisé. **La latence**, une réponse longue à produire étant incompatible avec certains usages interactifs. Et **la vérification** : les étapes produites ne constituent pas une démonstration vérifiable.

**Ce que cela implique.** Ce qui est produit **ressemble** à un raisonnement sans en avoir les propriétés : le modèle peut atteindre la bonne conclusion par un chemin faux, et inversement. Les étapes intermédiaires sont une aide à la performance, pas une justification opposable — distinction décisive dès qu'une décision doit être motivée.

**À ne pas confondre avec.** **Une démonstration formelle**, vérifiable mécaniquement. **L'explicabilité** : produire des étapes n'est pas expliquer une décision.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Devenu une modalité standard, avec un réglage explicite du budget de calcul par requête chez plusieurs fournisseurs.
> 🔄 **À revoir si** les gains obtenus par allocation de calcul à l'inférence cessent de croître avec le budget alloué.

**Renvois** — Couche : apprendre et décider · Courants : modèles de raisonnement (ch. 32) · Convergence : découverte scientifique (37).

---

## ◆◆ Multimodalité

**Niveau** — capacité · **Couche** — percevoir, apprendre et décider

**En une phrase.** Traiter conjointement plusieurs types d'entrées — texte, image, son, vidéo, signaux — dans une représentation commune.

**Comment ça fonctionne.** Chaque modalité est convertie en une suite de vecteurs, puis projetée dans un espace partagé où la proximité traduit une similarité d'usage. Le modèle apprend les correspondances entre modalités à partir de données appariées — une image et sa description, un son et sa transcription.

**Ce que ça permet.** Interroger une image par du texte · relier une observation à une instruction · produire une commande à partir d'une scène — ce dernier point étant le fondement des architectures traitées au chapitre 13.

**Ce qui bloque.** **L'appariement des données.** Il faut des exemples où plusieurs modalités décrivent la même chose, et ces jeux sont bien plus rares que les corpus mono-modaux. **L'alignement temporel et spatial** quand les entrées viennent de capteurs distincts — c'est le problème de recalage de la couche *percevoir*, et c'est là que la chaîne échoue en pratique. Et le **déséquilibre** : une modalité dominante peut masquer les autres.

**Ce que cela implique.** Un système multimodal n'est pas plus fiable qu'un système mono-modal : **il hérite des défaillances de chaque capteur** et y ajoute celles de la combinaison.

**À ne pas confondre avec.** **La fusion de capteurs** (ch. 7), qui combine des mesures physiques avec un modèle d'incertitude explicite. Ici, la combinaison est apprise et son incertitude n'est pas explicitée.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour texte et image, 🔬 émergent pour l'intégration de signaux physiques hétérogènes.
> 🔄 **À revoir si** l'ajout d'une modalité issue de capteurs physiques produit un gain mesuré sur une tâche de décision en conditions réelles.

**Renvois** — Couche : percevoir, apprendre et décider · Convergence : robotique généraliste (36).

---

## ◆◆ Mémoire et contexte long

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Permettre à un modèle de tenir compte d'une grande quantité d'information fournie au moment de l'usage, ou de conserver une trace entre les échanges.

**Pourquoi on en parle.** Parce que c'est la limite que rencontrent en premier tous les usages professionnels — et parce que deux mécanismes très différents sont désignés par le même mot.

**Comment ça fonctionne — deux mécanismes distincts.**

**Le contexte** est ce qu'on fournit au modèle à chaque appel. Il est volatil : rien n'en subsiste après l'échange. L'étendre coûte cher, parce que le mécanisme qui met chaque élément en relation avec les autres implique un nombre de comparaisons croissant **avec le carré** de la longueur. Doubler le contexte quadruple ce coût — contrainte structurelle, et non réglage.

**La mémoire externe** consiste à stocker de l'information à l'extérieur du modèle et à en réinjecter les fragments pertinents au moment utile. Ce n'est pas une propriété du modèle mais une **architecture**, et sa qualité dépend entièrement de la pertinence de la récupération.

**Ce qui bloque.** Pour le contexte : le coût, la latence, et le fait qu'**une information présente dans un très long contexte n'est pas nécessairement utilisée** — la performance dépend de sa position et de sa saillance. Pour la mémoire externe : la récupération, qui devient le maillon déterminant, et la gestion de l'obsolescence — que faire d'une information mémorisée devenue fausse.

**Ce que cela implique.** Un modèle **n'a pas de mémoire persistante par construction** ; ce qu'il a appris est figé à l'entraînement. Tout ce qui ressemble à de la mémoire est un dispositif extérieur, avec ses propres modes de défaillance.

**À ne pas confondre avec.** **L'apprentissage**, qui modifie les paramètres. Fournir une information en contexte ne l'apprend pas.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Contextes très étendus disponibles ; l'exploitation effective de leur totalité reste inégale selon les tâches.
> 🔄 **À revoir si** un mécanisme dont le coût croît linéairement avec la longueur atteint les performances du mécanisme quadratique sur les tâches courantes.

**Renvois** — Couche : apprendre et décider · Convergence : intelligence distribuée (38).

---

## ◆◆ Modèles compacts

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Obtenir un comportement utile avec un modèle assez petit pour tenir dans la mémoire d'un appareil ordinaire.

**Pourquoi on en parle.** Parce que c'est la condition de l'exécution locale — donc de la latence faible, du coût par appel nul et de l'indépendance vis-à-vis d'un réseau.

**Comment ça fonctionne — trois techniques, souvent combinées.** La **distillation** entraîne un petit modèle à reproduire le comportement d'un grand. La **quantification** réduit la précision des paramètres, ce qui divise l'empreinte mémoire. Le **mélange d'experts** n'active qu'une fraction des paramètres à chaque requête, ce qui réduit le calcul sans réduire la taille totale.

**Ce que ça permet.** Exécuter sur un téléphone, un véhicule, un équipement industriel · supprimer le coût par requête · traiter des données qui ne doivent pas quitter l'appareil.

**Ce qui bloque.** **La dégradation n'est pas uniforme.** Un modèle compact peut égaler un grand modèle sur les tâches courantes et s'effondrer sur les cas rares — sans que les tests usuels le révèlent. C'est une défaillance silencieuse. S'y ajoutent la **mémoire disponible**, qui est la contrainte dimensionnante bien avant la puissance de calcul, et la **mise à jour** d'un parc déployé.

**À ne pas confondre avec.** **Un modèle simplement plus petit**, entraîné directement à cette taille : les performances diffèrent nettement, la distillation transférant une partie du comportement du grand modèle.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Exécution locale disponible sur des appareils courants ; l'écart avec les modèles distants persiste sur les tâches complexes.
> 🔄 **À revoir si** un modèle exécutable localement atteint, sur une tâche professionnelle de référence, la performance d'un modèle distant de génération courante.

**Renvois** — Couche : apprendre et décider · Convergence : intelligence distribuée (38).

---

## ◆◆ Données synthétiques

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Entraîner un modèle sur des données produites par un autre modèle ou par simulation, plutôt que collectées.

**Ce que ça permet.** Compléter des cas rares mal représentés · produire des données là où la collecte est coûteuse, dangereuse ou juridiquement contrainte · générer des variations contrôlées pour éprouver la robustesse.

**Ce qui bloque.** **La dérive de distribution.** Un modèle entraîné majoritairement sur les productions d'un autre hérite de ses biais et de ses angles morts, et peut s'écarter progressivement du réel sans que rien ne le signale. La question ouverte est celle de la proportion acceptable, et elle n'est pas tranchée. S'y ajoute la **validation** : vérifier qu'une donnée synthétique est représentative suppose de disposer de données réelles — ce qui est précisément ce qui manquait.

**Ce que cela implique.** Les données synthétiques fonctionnent bien là où **un modèle physique fiable existe** — simulation d'un capteur, d'un mécanisme, d'un environnement. Elles fonctionnent mal là où la richesse du réel est précisément ce qu'on ne sait pas modéliser.

**À ne pas confondre avec.** **L'augmentation de données**, qui transforme des données réelles sans en créer de nouvelles.

> ⏱ **État au 23/08/2026** — 🏭 déployé, pratique courante, avec des proportions et des méthodes variables selon les domaines.
> 🔄 **À revoir si** une méthode de mesure de la dérive de distribution devient assez fiable pour être utilisée comme critère de qualité opposable.

**Renvois** — Couche : apprendre et décider · Convergences : robotique généraliste (36), découverte scientifique (37).

---
