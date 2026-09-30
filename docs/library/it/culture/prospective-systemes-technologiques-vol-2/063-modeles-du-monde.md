---
title: ◆◆◆ Modèles du monde
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Un modèle qui apprend à prédire l'évolution d'un environnement, de sorte qu'un système puisse anticiper les conséquences d'une action avant de l'exécuter.

**Pourquoi on en parle.** Parce que c'est la réponse proposée au problème de coût des données physiques : si un système peut simuler intérieurement les conséquences de ses actions, il peut apprendre sans agir.

**Comment ça fonctionne.** Le modèle est entraîné à prédire l'état suivant à partir de l'état courant et de l'action envisagée. Une fois cette prédiction assez fiable, le système peut **dérouler mentalement** plusieurs séquences d'actions et choisir celle dont le résultat prédit est le meilleur — sans les exécuter.

**Ce que ça permet.** Réduire le nombre d'interactions réelles nécessaires · anticiper au lieu de réagir · évaluer une action risquée sans la tenter.

**Ce qui bloque.** **L'accumulation d'erreur de prédiction.** Chaque pas prédit introduit une erreur, et prédire loin revient à composer ces erreurs : au-delà de quelques pas, la prédiction diverge. L'horizon utile est donc court, et l'étendre est le sujet actif.

**La physique du contact** est particulièrement difficile à prédire : au moment où deux objets se touchent, la dynamique change brutalement et de faibles écarts de position produisent des résultats très différents.

**Et une difficulté de fond** : le modèle prédit ce qu'il a observé. Face à une situation inhabituelle, il produit une prédiction plausible et fausse — sans le signaler.

**Ce que cela implique.** Un modèle du monde ne supprime pas le besoin de données réelles : **il l'exporte vers la validation**. Il faut vérifier que les prédictions correspondent au réel, ce qui exige d'agir dans le réel.

**À ne pas confondre avec.** **Un simulateur physique**, construit à partir d'équations connues et non appris. **Un jumeau numérique** (ch. 34), qui est synchronisé sur un système existant et n'a pas vocation à généraliser.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Résultats convaincants sur horizon court et environnements maîtrisés ; extension à des environnements ouverts non établie.
> 🔄 **À revoir si** un modèle du monde permet un apprentissage de manipulation en environnement varié avec un volume d'interactions réelles réduit d'un ordre de grandeur.

**Renvois** — Couche : apprendre et décider · Courants : Physical AI, embodied AI (ch. 33) · Convergences : robotique généraliste (36), autonomie mobile (39).

---
