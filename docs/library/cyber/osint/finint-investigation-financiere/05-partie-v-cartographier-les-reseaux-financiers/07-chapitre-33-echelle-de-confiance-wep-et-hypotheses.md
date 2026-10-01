---
title: Chapitre 33 — Échelle de confiance WEP et hypothèses calibrées
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie V — Cartographier les réseaux financiers
  - index.md
---

## Objectif du chapitre

Formaliser et appliquer l’**échelle de confiance** inspirée des **Words of Estimative Probability** (WEP) pour calibrer toutes les conclusions d’une note FININT. C’est la discipline qui distingue un livrable professionnel d’un texte affirmatif sans nuance.

## Le concept

Les WEP sont une convention sémantique pour exprimer la confiance d’une affirmation. Origine : Sherman Kent, CIA, années 1960 — repris dans le renseignement civil et militaire et adapté en FININT.

**Échelle utilisée dans ce cours** :

|Niveau               |Plage  |Quand l’utiliser                                                           |
|---------------------|-------|---------------------------------------------------------------------------|
|**Quasi-certain**    |> 95 % |Multi-sources indépendantes, documents probants, recoupements convergents. |
|**Très probable**    |80-95 %|Plusieurs sources concordantes, hypothèses alternatives faibles.           |
|**Probable**         |60-80 %|Indices convergents mais incomplets, hypothèses alternatives moins fortes. |
|**Possible**         |40-60 %|Compatibilité avec les éléments, mais hypothèses alternatives équivalentes.|
|**Peu probable**     |15-40 %|Compatibilité faible, hypothèses alternatives dominantes.                  |
|**Très peu probable**|< 15 % |Quasi-exclusion.                                                           |
|**Indéterminable**   |n/a    |Données insuffisantes pour calibrer.                                       |

Cette échelle est utilisée systématiquement dans le cours, les fiches, les cas pratiques, la note FININT et les annexes.

## L’utilité opérationnelle

Cinq usages :

1. **Discipline analytique** : forcer l’analyste à se demander, pour chaque conclusion, *« quelle est la solidité réelle de ce que j’écris ? »*.
1. **Communication précise** : le lecteur (magistrat, comité, partenaire) sait à quel point il peut s’appuyer sur chaque élément.
1. **Honnêteté épistémique** : ne pas faire semblant de savoir ce qu’on ne sait pas.
1. **Calibration des actions** : un gel d’avoirs sur la base d’un *quasi-certain* n’est pas la même décision qu’un signalement sur la base d’un *probable*.
1. **Comparabilité** : entre analystes, entre dossiers, entre périodes.

## Méthode — calibrer une conclusion

1. **Identifier les sources** qui soutiennent la conclusion.
1. **Identifier les sources qui la contredisent** ou la nuancent.
1. **Identifier les hypothèses alternatives** : que d’autres explications restent compatibles avec les éléments ?
1. **Évaluer la solidité** : robustesse des sources, recoupements indépendants, cohérence avec le reste du dossier.
1. **Choisir le niveau** dans l’échelle.

## Mini-walkthrough — calibration progressive

Hypothèse : *« Karim Haddad est l’UBO réel de NEXUS TRADING SAS (France) »*.

**Étape 1** : seul élément initial — chaîne de capital remonte à NEXUS HOLDINGS LTD (CY).
→ Calibration : *indéterminable* sur Haddad spécifiquement.

**Étape 2** : ajout du hit Pandora — settlor du trust OMEGA = Karim Haddad.
→ Calibration : *probable*. La chaîne est plausible mais formelle ; le contrôle effectif n’est pas démontré.

**Étape 3** : ajout des analyses de flux — Haddad reçoit personnellement des fonds en sortie du réseau et signe des opérations critiques.
→ Calibration : *très probable*.

**Étape 4** : coopération Mokas confirme la qualité de bénéficiaire principal de Haddad dans le trust, et témoignage du trustee si obtenu.
→ Calibration : *quasi-certain*.

À chaque étape, l’évolution de la calibration est documentée. La note finale présente la calibration *finale*, mais les annexes peuvent retracer l’évolution pour transparence.

## Erreurs fréquentes

- **Utiliser un vocabulaire affirmatif sans calibration** : « c’est l’UBO », « il blanchit » — sans support, c’est faux ou exposé à contestation.
- **Sur-calibrer** par excès de prudence : tout est *possible* — devient ininterprétable.
- **Sous-calibrer** par enthousiasme : tout est *quasi-certain* — fait perdre la crédibilité.
- **Confondre absence de preuve et preuve d’absence** : si on ne trouve pas un élément, ce n’est pas qu’il n’existe pas — peut-être qu’on n’a pas la bonne source.

## Limites

L’échelle WEP est une convention sémantique, pas une mesure objective. La calibration reste un **jugement informé**. Deux analystes peuvent diverger légèrement sur le niveau — c’est attendu et acceptable, à condition que chacun **justifie** son choix.

## Lien avec le fil rouge

> **CLEARFLOW — Calibration systématique**
> 
> La note finale du dossier Haddad utilise systématiquement l’échelle WEP. Exemple d’extrait : *« La qualification de NEXUS DELAWARE LLC comme société écran de transit à finalité d’opacification est probable. La qualification de la finalité illicite (blanchiment) est possible à ce stade et nécessiterait, pour être qualifiée probable, la confirmation par audition de bénéficiaires de fonds et expertise comptable. La qualification du rôle de M. X comme prête-nom est probable. La qualification de K. Haddad comme UBO réel du réseau est très probable. »*

## Points clés à retenir

- WEP : quasi-certain > très probable > probable > possible > peu probable > très peu probable > indéterminable.
- Utiliser systématiquement, dans fiches, notes, cas pratiques.
- Calibration = jugement informé, à justifier.
- Permet honnêteté, communication, discipline analytique.

-----
