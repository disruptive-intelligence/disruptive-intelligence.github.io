---
title: Chapitre 85 — Niveaux de confiance WEP
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XI — Analyse structurée, cotation et raisonnement
  - index.md
---

## 85.1 Words of Estimative Probability

Les **WEP** (Words of Estimative Probability) sont les expressions standardisées pour communiquer **niveaux de confiance** dans les conclusions analytiques.

Inspirées de **Sherman Kent** (CIA, années 1960), formalisées dans **ICD-203** (Intelligence Community Directive 203, US IC, 2007 et révisions).

**Pour OSINT, c'est le vocabulaire référence.**

## 85.2 Échelle WEP standard

- **Quasi-certain** (almost certainly) : >95 %.
- **Très probable** (very likely) : 80-95 %.
- **Probable** (likely) : 55-80 %.
- **Possible / environ moitié-moitié** (about even chance) : 45-55 %.
- **Peu probable** (unlikely) : 20-45 %.
- **Très peu probable** (very unlikely) : 5-20 %.
- **Hautement improbable** (almost no chance) : <5 %.
- **Indéterminable** : insuffisance d'évidence.

## 85.3 Cotation à appliquer aux conclusions

**Différence avec Admiralty.** Admiralty cote **faits** (A-F / 1-6). WEP cote **conclusions probabilistes**.

**Exemple.**

- Fait : « Delaunay est administrateur de Delta Consulting » → A1.
- Conclusion : « Delaunay bénéficie économiquement de Delta Consulting » → **probable** (faisceau d'indices convergents, démonstration directe manquante).

## 85.4 Précision et risque

**Précision.** Plus on est précis, plus on s'engage.

**Risque.** Une conclusion « quasi-certain » qui s'avère fausse détruit la crédibilité de l'analyste.

**Discipline.** Ne pas sur-affirmer. Préférer « probable » à « quasi-certain » quand c'est juste.

## 85.5 Distribution des conclusions

Une enquête mature produit des conclusions à **divers niveaux**, pas toutes au même niveau.

**Pattern type.**

- Quelques conclusions « quasi-certain » (faits multi-corroborés).
- Plusieurs « probable » (faisceaux d'indices).
- Plusieurs « possible » (hypothèses non infirmées).
- Quelques « indéterminable » (questions ouvertes).

**Si tout est « quasi-certain », méfiance.** Probable sur-affirmation.

## 85.6 WEP dans le rapport

**Bonne pratique.**

```
Conclusion : Marc Delaunay contrôle effectivement Delta Consulting Ltd 
et Verde Holdings, dans le cadre d'une organisation offshore destinée 
à détourner des fonds de TechnoVert SAS.

Niveau de confiance : probable.

Faisceau soutenant :
- Administrateur déclaré (A1).
- UBO déclaré (A1).
- Flux documentés dans Cyprus Confidential (B2).
- Patrimoine incohérent avec revenus (A1).

Réserves :
- Possible structure nominee (résiduelle, H2 ACH).
- Démonstration directe « détournement » non disponible (limite OSINT, 
  procédure judiciaire requise).
```


## 85.7 Vocabulaire calibré complet

**Pour AFFIRMER avec niveau.**

- « Il est quasi-certain que... »
- « Il est très probable que... »
- « Il est probable que... »

**Pour FAITS établis multi-corroborés.**

- « Il est établi que... »
- « Sources convergentes documentent... »

**Pour HYPOTHÈSES.**

- « L'hypothèse [X] est compatible avec les éléments observés. »
- « Plusieurs indices suggèrent [Y]. »

**Pour LIMITES.**

- « Les éléments collectés ne permettent pas de conclure sur... »
- « Une vérification complémentaire serait nécessaire pour... »

**À ÉVITER.**

- « Sans aucun doute. »
- « Prouvé. »
- « Confirmé » (sans cotation).
- « Évident. »
- « Manifestement. »

## 85.8 ICD-203 et standards

**ICD-203** (US IC, 2007 révisé) impose vocabulaire calibré dans tous les produits IC US.

**NATO** : standards similaires.

**Doctrines françaises** : convergence progressive.

## 85.9 Adaptation au commanditaire

**Pour client non-expert.** Glossaire en début de rapport. WEP explicité.

**Pour magistrat.** Adapter au vocabulaire judiciaire (« éléments convergents ne permettent pas d'écarter... », etc.).

**Pour direction.** Synthèse plus brève, mais maintenir précision.

## 85.10 Synthèse — discipline WEP

> **Règle d'or.** Chaque conclusion porte son niveau de confiance WEP. Pas de verdict. Pas de surenchère. Pas de sous-affirmation. Calibrage à l'évidence disponible.

-----
