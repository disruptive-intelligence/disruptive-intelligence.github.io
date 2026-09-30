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
