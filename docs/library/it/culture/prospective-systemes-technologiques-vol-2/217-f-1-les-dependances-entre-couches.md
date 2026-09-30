---
title: F.1 Les dépendances entre couches
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Deux couches sont les plus transversales.** *Calculer* et *alimenter* conditionnent la grande majorité des capacités de l'atlas — quelques procédés et matériaux n'ont pas le calcul pour prérequis — et un verrou qui s'y installe se propage largement. C'est la raison pour laquelle le raccordement électrique — une entrée qui ne décrit aucune technologie — est l'un des objets les plus structurants du volume.

**Une couche est en aval de tout.** *Vérifier* ne produit aucune capacité nouvelle mais conditionne le déploiement de celles que les autres produisent. **Elle est donc fréquemment bloquante dans les déploiements critiques ou réglementés, et presque toujours traitée en dernier**, dans le volume comme dans les projets réels — ce qui est précisément le problème.

| Couche | Dépend principalement de | Conditionne |
|---|---|---|
| A — percevoir | calculer, alimenter | agir, apprendre, vérifier |
| B — calculer | alimenter, fabriquer | toutes |
| C — apprendre et décider | calculer, percevoir | agir, interagir |
| D — agir | percevoir, apprendre, alimenter, vérifier | usages physiques |
| E — fabriquer | calculer, alimenter, matériaux | toutes les couches matérielles |
| F — alimenter | fabriquer, réseaux, raccordement | toutes |
| G — relier | calculer, alimenter, spatial | perception distribuée, autonomie |
| G-bis — plan spatial | fabriquer, alimenter, relier | percevoir, positionner, relier |
| H — vérifier | calculer, percevoir | **le déploiement de tout le reste** |
| I — interagir | percevoir, calculer, alimenter | adoption |

**Lecture.** Ce tableau ne dit pas ce qui est important, il dit **par où un blocage se propage**. Une contrainte dans *alimenter* atteint toutes les couches ; une contrainte dans *interagir* n'atteint que l'adoption.
