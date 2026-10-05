---
title: 'Chapitre 59 — Cas 5 : Asset tracing d’un dirigeant sous enquête'
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie IX — Cas pratiques déroulés
  - index.md
---

## Contexte

Un magistrat instructeur français saisit, par réquisition, une cellule spécialisée pour l’**asset tracing** d’un dirigeant français, **M. RIVIÈRE**, mis en examen pour escroquerie aggravée à hauteur de 15 M€. Le magistrat soupçonne une dissipation patrimoniale en cours et souhaite **identifier les actifs susceptibles d’une mesure conservatoire** (gel, saisie).

L’enquête a déjà identifié les flux frauduleux principaux et certains comptes bancaires français. Mais le patrimoine étranger et les structures offshore éventuelles restent à identifier.

**Demande** : asset tracing complet pour mesure conservatoire urgente.

## Indices initiaux

- M. RIVIÈRE, 55 ans, ancien dirigeant d’une PME en redressement.
- Mises en cause : ventes fictives via faux clients, fraude TVA et abus de biens sociaux. Préjudice estimé 15 M€.
- Comptes français : 6 comptes identifiés, soldes cumulés actuels ~280 K€. *Insuffisant* pour mesure conservatoire significative.
- Patrimoine français déclaré (déclarations fiscales) : 2 résidences, 1 SCI, ~2 M€ valeur.
- Signaux : voyages réguliers à Dubaï et Genève depuis 18 mois, train de vie présomé supérieur au patrimoine déclaré.

## Cadrage

**Questions de renseignement** :

- QR1 — Quels actifs cachés ou indirects ? Immobilier étranger ? Comptes étrangers ? Structures offshore ?
- QR2 — Y a-t-il des prête-noms ou des structures interposées ?
- QR3 — Quelle est la trajectoire récente du patrimoine (dissipation ? consolidation ?) ?
- QR4 — Quels actifs sont juridiquement susceptibles de mesure conservatoire ?

**Délai** : 4 semaines (mesure conservatoire à décider rapidement).

## Collecte

**Sources ouvertes** :

- DVF + cadastre : identification des biens français.
- Pappers : sociétés détenues par M. RIVIÈRE et ses proches.
- LinkedIn + presse + réseaux sociaux : profilage, identification de relations et de localisations.
- Patrim (accessible CRF) : revenus et patrimoine déclarés.
- Reverse image search : identification du yacht visible sur Instagram.

**Sources fermées (en cadre judiciaire)** :

- FICOBA : tous les comptes bancaires en France au nom de M. RIVIÈRE et de ses proches identifiés.
- FICOVIE : assurances-vie.
- EAR/CRS (via demande administrative en coopération avec DGFiP) : comptes étrangers déclarés.
- Réquisitions auprès de banques françaises : relevés détaillés.

**Coopérations internationales** :

- Egmont avec MROS (Suisse) : confirmation d’1 compte privé à Genève, soldes et historiques.
- Egmont avec CRF émiratie : identification de 2 sociétés free zone (Dubaï) liées à un proche collaborateur — *probable* UBO M. RIVIÈRE via prête-nom.
- Recherche presse mondaine : photos de M. RIVIÈRE devant un appartement à Dubaï (identifiable au quartier).

## Analyse

**Cartographie patrimoniale consolidée** :

```
France
├─ 2 résidences (déclarées) — 2 M€
├─ SCI (déclarée) — 1 M€
├─ 6 comptes bancaires — 280 K€
└─ 2 contrats assurance-vie — 850 K€

Suisse
└─ 1 compte banque privée Genève — 3,2 M€ (EAR/CRS + coop MROS)

Émirats
├─ 1 LLC Dubaï détentrice apparente d'un appartement à Dubaï Marina — valeur estimée ~1,8 M€
├─ 1 autre LLC sans actifs clairs — possible société écran
└─ Pas d'autres comptes identifiés à ce stade

Yacht
└─ Pavillon Malte, valeur estimée 1,2 M€, propriété via société écran maltaise

Total identifié : ~10,4 M€ (vs préjudice 15 M€).
```


**Dissipation observable** : sur les 6 derniers mois (post-mise en examen), virements totaux de 1,8 M€ depuis comptes français vers Suisse et Dubaï. *Probable* dissipation active.

## Hypothèses calibrées

- M. RIVIÈRE détient une fraction significative des fonds frauduleux dans des structures étrangères : quasi-certain.
- Une partie du patrimoine identifié (Suisse, Dubaï, yacht) est saisissable sous procédure judiciaire et coopérations internationales : probable.
- Dissipation active en cours : quasi-certain.

## Livrable

Rapport au magistrat instructeur :

- Cartographie patrimoniale consolidée : ~10,4 M€ identifiés.
- Actifs prioritaires pour mesures conservatoires :
    - France : saisine AGRASC pour gel et saisie des biens immobiliers et comptes.
    - Suisse : demande d’entraide pour gel via MROS et coopération judiciaire.
    - Émirats : demande d’entraide judiciaire (plus complexe et plus longue).
    - Yacht : possible saisie sous pavillon Malte (coopération MLA).
- Recommandation d’urgence : geler immédiatement les comptes français pour stopper la dissipation, puis enchaîner les coopérations internationales en parallèle.

## Bilan honnête

L’asset tracing a permis d’identifier ~10,4 M€ d’actifs (vs 15 M€ de préjudice). Le recouvrement réel dépend de :

- Réactivité des autorités (gel français immédiat).
- Vitesse des coopérations internationales (Suisse rapide, Émirats lent, Malte intermédiaire).
- Qualité juridique du dossier d’enquête (la mesure conservatoire repose sur la solidité de l’enquête pénale).

Récupération espérée : une **fraction significative** du patrimoine identifié si action rapide et coopération satisfaisante, sur le préjudice global, le recouvrement est **structurellement partiel**, sur 18 à 36 mois ou plus. Les ordres de grandeur donnés dans le cours sont **pédagogiques** ; la réalité varie fortement selon les juridictions, la qualité du dossier judiciaire, la coopération et les stratégies de protection adverses.

## Leçons FININT

- L’**asset tracing** combine OSINT (signaux visibles), sources fermées (FICOBA, EAR/CRS), et coopération internationale.
- La **rapidité** d’action conditionne le résultat (dissipation possible en parallèle).
- La **coopération avec AGRASC** en France et équivalents étrangers est indispensable.
- Les juridictions varient en réactivité : Suisse, UK, Allemagne sont relativement coopératifs ; Émirats, Asie, Liban beaucoup moins.

-----
