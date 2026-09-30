---
title: Chapitre 47 — Concevoir sous contrainte
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - PARTIE IX — Concevoir
  - index.md
---

## 47.1 Les arbitrages classiques, et ce qu'ils coûtent

| Arbitrage | Ce qu'on gagne | Ce qu'on perd | Quand il est juste |
|---|---|---|---|
| **Redonder ou non** | Continuité | Coût ×2, complexité, un composant de plus à exploiter | Quand l'interruption tolérable est inférieure au délai de remise en service |
| **Segmenter finement ou non** | Limitation de la propagation | Flux à maintenir, dépannage plus long | Quand les conséquences d'une propagation sont graves |
| **Centraliser ou distribuer** | Simplicité, économies | Dépendance au lien, latence | Quand le lien est fiable et la latence acceptable |
| **Internaliser ou externaliser** | Maîtrise, ou compétences | Compétences à tenir, ou dépendance | Selon ce que l'organisation sait exploiter |
| **Chiffrer partout ou aux frontières** | Confidentialité | Visibilité perdue, complexité de gestion des clés | Selon la sensibilité et la capacité de détection |
| **Authentifier une fois ou à chaque étape** | Confort, ou cloisonnement | Un jeton unique qui ouvre tout, ou de la friction | Selon la sensibilité des étapes |

## 47.2 L'architecture qui optimise tout n'existe pas

⚠️ **Le réflexe du débutant en conception** : produire une architecture qui coche toutes les cases. Elle est redondée, segmentée, chiffrée, journalisée, authentifiée à chaque étape.

**Ce qui se passe ensuite**, dans l'ordre :

```
Mois 1    L'architecture est validée. Elle est excellente sur le papier.
Mois 6    Le déploiement prend du retard : trop de composants à intégrer.
Mois 12   L'exploitation ne suit pas — deux personnes pour quinze composants.
Mois 18   Des contournements apparaissent pour tenir les délais.
Mois 24   La segmentation est partiellement désactivée « en attendant ».
Mois 36   L'architecture réelle ressemble à celle qu'on voulait éviter,
          avec le coût de celle qu'on a conçue.
```


> **Une architecture qu'une organisation ne sait pas exploiter se dégrade jusqu'à son niveau réel de compétence — en ayant coûté le prix de l'ambition.**

**Ce que ce principe explique, et qui vaut d'être énoncé explicitement** :

| Affirmation courante | Ce que le principe y oppose |
|---|---|
| « L'orchestration de conteneurs est plus moderne » | Elle introduit un système distribué complet à exploiter. **Plus moderne n'est pas plus adapté** |
| « Les microservices sont un signe de maturité » | Ils multiplient les composants et les flux. **La maturité est de savoir les exploiter** |
| « Plusieurs fournisseurs cloud, c'est plus résilient » | C'est deux plateformes à maîtriser au lieu d'une |
| « Plus de segmentation, c'est plus sûr » | Jusqu'au point où les flux deviennent ingérables et sont contournés — §24.2 |
| « Nous avons de la haute disponibilité » | **Une redondance non testée est une croyance** — *principe de preuve* |

> **Formulation générale, à rapprocher du principe du coût** : *un composant techniquement excellent que personne ne sait exploiter dégrade l'architecture au lieu de l'améliorer.*

**Le test à s'appliquer** : *combien de personnes faudra-t-il pour tenir cette architecture, et les avons-nous ?*

## 47.3 Concevoir pour ce qu'on sait exploiter

| Signe qu'une architecture est trop ambitieuse | Ce qu'on fait |
|---|---|
| Elle exige une compétence que personne n'a | La simplifier, ou acquérir la compétence **avant** |
| Elle comporte plus de composants que d'exploitants | Réduire, ou externaliser une partie |
| Elle suppose des procédures qui n'existent pas | Les écrire, ou choisir un modèle qui s'en passe |
| **Son basculement n'est testable que rarement** | Choisir un modèle testable — §20 |

**La quatrième ligne est celle qu'on découvre le plus tard.** Une redondance qui ne peut être testée qu'une fois par an, pendant une fenêtre difficile à obtenir, **ne sera pas testée** — et une redondance non testée est une croyance.

---
