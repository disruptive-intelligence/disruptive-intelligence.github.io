---
title: ◆◆ Mémoire et contexte long
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

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
