---
title: ◆◆ Multimodalité
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

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
