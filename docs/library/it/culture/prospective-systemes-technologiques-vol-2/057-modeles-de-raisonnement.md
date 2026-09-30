---
title: ◆◆◆ Modèles de raisonnement
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

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
