---
title: Chapitre 47 — Échelle de confiance et formulation analytique
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie IX — Production, cadre et professionnalisation
  - index.md
---

Approfondissement du chapitre 18. La **calibration de la confiance** est la signature de l’analyste sérieux. Ce chapitre formalise.

## 47.1 Les Words of Estimative Probability

Les WEP sont une **échelle standardisée** de calibration. Origine : communauté du renseignement US (Sherman Kent, années 1960). Adoptés mondialement.

**Échelle CIA / NATO / DGSE** (variantes mineures) :

|WEP                                |Probabilité|Usage                  |
|-----------------------------------|-----------|-----------------------|
|Quasi-certain / Almost certain     |95-100%    |Preuve directe forte   |
|Très probable / Highly likely      |80-95%     |Multiple convergence   |
|Probable / Likely                  |60-80%     |Convergence majoritaire|
|Possible / Even chance             |40-60%     |Hypothèse plausible    |
|Peu probable / Unlikely            |15-40%     |Alternative dominante  |
|Très peu probable / Highly unlikely|<15%       |Possibilité résiduelle |

**Adaptation pour OSINT crypto** : même échelle, applicabilité à toute hypothèse.

## 47.2 Pourquoi cette discipline

**Plusieurs raisons** :

**Communication précise** : « probable » et « possible » ont des sens distincts. Sans calibration, le lecteur interprète différemment.

**Auto-discipline** : forcer à choisir un WEP oblige à examiner les preuves. Décourage les sur-affirmations.

**Comparabilité** : même échelle entre rapports permet de comparer hypothèses.

**Crédibilité** : analyste calibré est plus crédible que analyste qui prétend tout savoir.

**Gestion d’incertitude** : reconnaît que l’enquête OSINT est intrinsèquement probabiliste.

## 47.3 Application en pratique

**Pour chaque hypothèse non-évidente** :

1. Lister les preuves en faveur.
1. Lister les preuves contre / alternatives.
1. Évaluer le poids relatif.
1. Choisir un WEP.
1. Documenter justification.

**Exemples MIXSHADOW** :

- « L’adresse `bc1q[Akira-receive]` est l’adresse de réception du paiement Aurélien Médical » → **Quasi-certain** (preuve : transaction confirmée + correspondance avec récit victime + portail négociation Akira).
- « Le cluster Bitcoin opérationnel est contrôlé par opérateur(s) Akira » → **Très probable** (heuristique cluster + continuité peeling + label Chainalysis).
- « Les hubs TRON identifiés sont services de blanchiment partagés Akira / Black Basta » → **Probable** (patterns de service + corroboration cross-incident).
- « Le pattern temporel suggère acteur en fuseau Asie de l’Est » → **Possible** (signal cohérent mais alternatives plausibles).
- « Akira a des liens DPRK » → **Spéculatif / non déterminé** (pas de preuve OSINT directe, base sectorielle suggère possible).

## 47.4 Pièges à éviter

**Le piège du « possible »**. « Possible » signifie 40-60%, pas « peut-être ». Un événement « possible » a près d’une chance sur deux. Utilisé proprement, c’est fort. Utilisé comme « peut-être faible », c’est trompeur.

**Le piège du « peu probable »**. « Peu probable » signifie 15-40%. C’est une fourchette **assez large**. Un événement à 35% peut quand même se produire. Pas « impossible ».

**L’inflation lexicale**. « Très probable » devient automatique pour tout ce qui n’est pas certain. Discipline requise pour conserver le sens.

**Mélanger preuves et confiance**. Confiance = niveau de croyance. Preuves = ce qui supporte. Confiance basée sur preuves, mais distincte.

**Confiance sur la précision vs confiance sur l’attribution**. « 75% confiance que cluster X » vs « 75% confiance que cluster X est attribué à acteur Y ». Distinguer.

## 47.5 La calibration cumulative

Quand l’analyse aggregue plusieurs hypothèses, la **confiance se compose**.

**Exemple** :

- A : 80% confiance.
- B (dépend de A) : 70% confiance si A est vrai.
- A et B simultanément : 80% × 70% = **56% confiance**.

Beaucoup de raisonnements crypto sont **chaînés** : adresse → cluster → service → entité → individu. Chaque maillon a une incertitude. Cumulée, l’incertitude finale peut être substantielle même si chaque maillon paraît fort.

L’analyste honnête **reconnaît cette propagation**. Ne pas affirmer « certain que individu X est responsable » quand chaque maillon de la chaîne est à 70-80%, donc cumulé à 30-40%.

## 47.6 Rédaction calibrée

**Bonnes formulations** :

- « Sur la base de [preuves], il est très probable (85%) que [hypothèse]. »
- « L’analyse suggère, avec une confiance modérée (~65%), que [hypothèse]. Une explication alternative est [autre], qui reste possible (~25%). »
- « L’identification de [propriété] est probable (~70%) ; cependant, sans accès à [preuve manquante], une certitude n’est pas atteignable. »

**Mauvaises formulations** :

- « Cette adresse est X. » (Sans calibration.)
- « Il est clair que Y. » (« Clair » est subjectif.)
- « Tous les éléments convergent vers Z. » (Hyperbole, perd nuance.)

## 47.7 Quand exprimer son désaccord interne

Si plusieurs analystes désaccordent sur calibration :

- **Documenter** le désaccord.
- **Présenter** les deux positions dans le rapport.
- **Proposer** un WEP médian si possible, ou les deux explicitement.
- **Attribuer** chaque position aux analystes concernés.

Le désaccord sain renforce la qualité.

-----
