---
title: 'Chapitre 93 — Cas complet : synthèse MIRAGE'
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 93.1 Présentation du cas

Ce chapitre clôt l'épopée MIRAGE en rassemblant les 21 épisodes vus au fil du cours et en produisant la synthèse finale du dossier, telle qu'elle serait remise au cabinet Legrand & Associés.

L'objectif pédagogique est triple : (1) montrer comment des épisodes apparemment disparates s'assemblent en une enquête cohérente, (2) illustrer la production d'un livrable mature dans toutes ses dimensions, (3) servir de modèle de référence pour les enquêtes complexes que l'analyste sera amené à conduire.

## 93.2 Rappel du mandat

**Cabinet** Legrand & Associés, mandaté par TechnoVert SAS (Pierre Dubois, DG), dans le cadre d'une procédure interne post-audit. Saisine également du PNF en parallèle (dénonciation art. 40 CPP).

**Périmètre.** Investigation OSINT sur Marc Delaunay (DAF de TechnoVert) et son entourage corporate proche, dans le cadre de 5 soupçons : détournement, blanchiment crypto, désinformation contre lanceur d'alerte Berthier, cluster faux comptes, vidéo deepfake.

**Bornes.** Sources ouvertes exclusivement, OPSEC stricte, déontologie défensive, escalade vers expertise forensique et procédure judiciaire pour profondeur.

**Durée.** 4 semaines.

## 93.3 Architecture de l'enquête conduite

L'enquête s'est articulée en **5 volets** correspondant aux 5 IR formulées au cadrage (Ch.12 / MIRAGE 0).

**Volet 1 — Structures offshore (IR1).** Investigation sur Delta Consulting Ltd (Malte) et Verde Holdings (Chypre) : existence, contrôle, UBO, liens organiques.

**Volet 2 — Flux financiers visibles (IR2).** Indicateurs ouverts de transferts TechnoVert vers offshore.

**Volet 3 — Patrimoine et cohérence (IR3).** Patrimoine visible de Delaunay et cohérence avec revenus déclarés.

**Volet 4 — Désinformation contre Berthier (IR4).** Cluster X, Telegram, faux médias, contenu IA.

**Volet 5 — Contenus IA et attribution (IR5).** Authenticité des fausses photos et vidéo deepfake, attribution au commanditaire.

## 93.4 Synthèse Volet 1 — Structures offshore

**Faits saillants cotés.**

| Fait | Source | Cot. |
|---|---|---|
| Delta Consulting Ltd immatriculée Malte 03/2020 | Companies Registry Malta | A1 |
| Director unique Marc Delaunay | Companies Registry Malta | A1 |
| Adresse domiciliation type registered agent | OpenCorporates | A1 |
| Verde Holdings Chypre 01/2022 | Companies Registry CY | A1 |
| UBO Marc Delaunay 100 % | Registre UBO CY (partiel) | A1 |
| Marina Constantinidou administratrice locale | Registre CY | A1 |
| Cyprus Confidential mémo flux Delta → Verde | ICIJ leak | B2 |
| Aucune sanction / PEP active | OpenSanctions | A1 |
| Aucune déclaration française publiquement visible | Recherches FR | D3 |

**Conclusion.** **Probable** : Marc Delaunay détient et opère, depuis 2020, un dispositif de structures offshore (Delta Consulting et Verde Holdings) bénéficiant de flux dont l'origine plausible est TechnoVert SAS. **ACH résiduellement ouverte** sur l'hypothèse alternative « nominee pour tiers ». Hypothèse « pas de lien réel » réfutée par convergence des éléments.

**Limites.** Registre UBO chypriote partiellement accessible. Comptes Verde non publiés. Flux financiers réels demandent expertise comptable judiciaire.

## 93.5 Synthèse Volet 2 — Flux financiers visibles

**Faits saillants.**

| Fait | Source | Cot. |
|---|---|---|
| Comptes TechnoVert publiés montrent ligne « prestations consulting externes » significative | Pappers / comptes consolidés | A1 |
| Croissance de cette ligne 2020-2024 | Comptes consolidés | A1 |
| Cohérence temporelle avec création Delta (03/2020) | Cross-référence | B2 |
| Cyprus Confidential mentionne flux Delta → Verde | ICIJ leak | B2 |
| Pas de bénéficiaire externe connu cohérent | Recherches | B2 |

**Conclusion.** **Probable** : des flux financiers de TechnoVert vers Delta Consulting (cohérents avec la ligne « prestations consulting externes » dans les comptes consolidés) alimentent Delta puis Verde, dans un schéma compatible avec un détournement par double-fausse-facturation. **Démonstration formelle** demande accès aux factures Delta émises à TechnoVert (hors OSINT, requérable judiciairement).

## 93.6 Synthèse Volet 3 — Patrimoine et cohérence

**Faits saillants.**

| Fait | Source | Cot. |
|---|---|---|
| SCI La Provence Familiale, mas Goult (Vaucluse) | Pappers / cadastre | A1 |
| Estimation mas : 1.5-2 M€ | Estimations locales | B2 |
| Villa Marrakech | Cyprus Confidential mention | B2 |
| Appartements parisiens (SCI nominee) | Indices Pappers | C3 |
| Compte Binance personnel | Stealer log Hudson Rock | B2 |
| Revenus DAF TechnoVert estimés 180-250 k€/an | Standards sectoriels | B2 |
| Cumul revenus 2019-2025 (avant fiscalité) ~1.3-1.8 M€ | Estimation | B3 |
| Patrimoine visible estimé 3-4 M€ | Cumul | B3 |

**Conclusion.** **Probable** : le patrimoine visible de Delaunay (estimation 3-4 M€) est en **incohérence apparente** avec son cumul de revenus déclarés (1.3-1.8 M€ brut sur 7 ans, ramené après fiscalité et charges courantes à ~600-900 k€ disponibles à l'épargne). L'écart suggère soit (a) revenus complémentaires non déclarés, soit (b) acquisitions partiellement financées par des moyens non identifiés. Une expertise patrimoniale judiciaire serait nécessaire pour conclure.

**Hypothèses concurrentes.** Héritage familial substantiel, mariage favorable, gains exceptionnels (gain crypto, héritage récent) — toutes plausibles, aucune documentée par sources ouvertes.

## 93.7 Synthèse Volet 4 — Désinformation contre Berthier

**Faits saillants.**

| Fait | Source | Cot. |
|---|---|---|
| Cluster X : 8 comptes coordonnés | Analyse graphe + temporelle | A1 |
| Cluster Telegram : 9 canaux amplifiant | Observation passive | A1 |
| Domaine `verites-technovert.com` créé 12/10/2025 | WHOIS historique | A1 |
| Domaine `info-finance-eu.com` créé 18/10/2025 | WHOIS historique | A1 |
| GA partagé entre les deux domaines | DNSlytics | A1 |
| Création concentrée après licenciement Berthier (15/09/2025) | Cross-références | A1 |
| Cohérence narrative entre les supports | Lecture humaine | B2 |
| Existence de prestataire potentiel (canal Telegram « social media boost ») | Observation passive | B2 |
| Lien direct avec Delaunay non démontré | (négatif) | — |

**Conclusion.** **Très probable** : une **campagne de désinformation coordonnée** vise Antoine Berthier, articulée sur 8 comptes X, 9 canaux Telegram, 2 faux médias, contenus IA, avec démarrage chronologiquement consécutif à son licenciement et pic d'amplification avant l'audience prud'homale. **Probable** : cohérence d'intérêt avec Delaunay (cible de l'alerte Berthier), suggérant attribution à Delaunay ou son entourage comme commanditaire le plus plausible. **Démonstration directe** non disponible en OSINT.

## 93.8 Synthèse Volet 5 — Contenus IA

**Faits saillants.**

| Fait | Source | Cot. |
|---|---|---|
| 3 fausses photographies « Berthier en soirée privée » | Captures + recherche inversée | A1 |
| Faces swappés sur backgrounds Unsplash / Pexels | Recherche inversée + ELA | A1 |
| Vidéo deepfake « Berthier confessant » | yt-dlp capture | A1 |
| Detection IA convergente Sensity 89 %, FakeCatcher 92 % | Outils techniques | A1 |
| Voice cloning detecté Resemble 76 % | Audio analysis | A1 |
| Incompatibilité avec déclarations publiques Berthier | Presse régionale | A1 |
| Pic publication avant audience prud'homale | Chronologie | A1 |

**Conclusion.** **Très probable** : les trois fausses photographies et la vidéo deepfake de Berthier sont des **contenus synthétiques fabriqués**, dans le cadre d'une campagne de discrédit. La cohérence avec le calendrier procédural (avant audience) renforce l'intentionnalité.

**Recommandation.** Expertise judiciaire complémentaire (expert numérique inscrit) pour validation officielle. Le rapport OSINT fournit le substrat technique.

## 93.9 Synthèse intégrée

Les **cinq volets convergent** :

- **Architecture économique** : montage offshore Delta-Verde sous contrôle Delaunay, vraisemblablement alimenté par TechnoVert via fausses factures de consulting.
- **Manifestation patrimoniale** : patrimoine visible de Delaunay en incohérence avec revenus déclarés, cohérent avec bénéfice du montage.
- **Réaction au signalement** : Berthier a déclenché audit interne en avril 2025, signalé en mai, licencié en septembre 2025.
- **Campagne défensive** : à partir d'octobre 2025, déploiement coordonné d'une campagne de désinformation et de discrédit contre Berthier, intensifiée avant l'audience prud'homale.
- **Sophistication** : usage d'IA générative (deepfakes, faces swap, voice cloning), infrastructure technique mature, possible prestataire externe.

**Cohérence d'ensemble : élevée.** Tous les éléments forment un **dispositif** cohérent ayant pour finalité (a) détournement, (b) protection du dispositif via discrédit du lanceur d'alerte.

**Niveau de confiance global : probable** sur l'architecture d'ensemble, **élevé** sur les éléments factuels individuels, **modéré** sur l'attribution explicite de la campagne de désinformation à Delaunay comme commanditaire direct.

## 93.10 Recommandations actionnables

**Immédiat (sous 7 jours).**

- Préservation des pièces (intégrité maintenue, archive 3-2-1 chiffrée).
- Transmission de la note courte au PNF pour suite procédure pénale.
- Transmission au conseil de Berthier pour soutien à la procédure prud'homale.

**Court terme (1 mois).**

- Mandater expertise comptable forensique sur les comptes consolidés TechnoVert (2020-2025).
- Mandater expertise numérique sur les contenus IA identifiés (vidéo deepfake, fausses photos).
- Sollicitation par le PNF d'entraide judiciaire avec autorités maltaises et chypriotes.

**Moyen terme (3 mois).**

- Investigation crypto forensique professionnelle (clustering, attribution wallet, cashout patterns) — renvoi cours OSINT Crypto vFULL.
- Approfondissement réseau d'amplification (réquisitions Telegram, X).

**Suivi.**

- Veille post-rapport sur acteurs (TechnoVert, Delaunay, Berthier procédures).
- Mises à jour mensuelles au cabinet.

## 93.11 Limites globales du rapport

**Périmètre OSINT.** Démonstration directe de détournement, qualification pénale, accès aux flux financiers réels demandent expertise judiciaire et procédure pénale.

**Attribution désinformation.** Lien direct Delaunay → service de désinformation non démontré en sources ouvertes. Réquisitions opérateurs permettraient confirmation.

**Crypto.** Triage limité, expertise dédiée requise.

**Sources opaques.** Stealer logs et leaks ICIJ utilisés comme orientations, non comme preuves directes pour usage judiciaire (l'expertise certifie).

**Temporalité.** Enquête conduite en 4 semaines. Approfondissement à 3-6 mois pourrait révéler éléments supplémentaires.

## 93.12 Le rapport délivré

Le **rapport MIRAGE** finalisé fait :

- 47 pages (corps + executive summary).
- 134 pages d'annexes (fiches, matrices ACH, timeline détaillée, graphe export, catalogue de pièces).
- 287 pièces archivées avec hash, captures Hunchly.
- Signature électronique PAdES-LT, horodatage qualifié.
- Classification TLP:AMBER+STRICT.

Transmis au cabinet Legrand & Associés et, en copie, au PNF dans le cadre de la dénonciation art. 40.

> **MIRAGE — Épisode 20 : Rapport final intégré**
>
> Le rapport MIRAGE clôt formellement l'enquête de 4 semaines. Il documente un dispositif probable de détournement via structures offshore, accompagné d'une campagne de désinformation sophistiquée contre le lanceur d'alerte. Il fournit le substrat factuel et méthodologique au cabinet et au PNF pour les actions ultérieures (audits forensiques, expertise numérique, entraide judiciaire internationale).
>
> Le rapport ne « prouve » pas un délit ; il **documente** un faisceau cohérent que la procédure judiciaire confirmera ou non. C'est exactement le rôle de l'OSINT : produire le matériau structuré sur lequel les autorités compétentes prennent des décisions qualifiantes.

## 93.13 Pédagogie du cas MIRAGE

À travers les 21 épisodes répartis sur le cours, MIRAGE a illustré :

- Le cadrage initial (Ch.12 / MIRAGE 0).
- La cartographie des sources et fiches initiales (Ch.13-14 / MIRAGE 1-2).
- La méthodologie d'enquête (Ch.18 / MIRAGE 3).
- L'identification de personne (Ch.26 / MIRAGE 4).
- Les pseudonymes et identités numériques (Ch.28 / MIRAGE 5).
- Le SOCMINT multi-plateformes (Ch.32 / MIRAGE 6).
- Telegram et forums (Ch.33 / MIRAGE 7).
- Sociétés, dirigeants, UBO (Ch.37 / MIRAGE 8).
- Infrastructure web (Ch.39 / MIRAGE 9).
- Breaches et stealer logs (Ch.43 / MIRAGE 10).
- Image suspecte et vérification (Ch.47 / MIRAGE 11).
- GEOINT et chronolocation (Ch.49 / MIRAGE 12).
- Signaux financiers ouverts (Ch.70 / MIRAGE 13).
- Piste crypto avec renvoi cours dédié (Ch.72 / MIRAGE 14).
- Piste dark web avec renvoi cours dédié (Ch.44 / MIRAGE 15).
- Deepfake et contenu synthétique (Ch.59 / MIRAGE 16).
- Campagne d'influence coordonnée (Ch.76 / MIRAGE 17).
- Graphe et timeline (Ch.83 / MIRAGE 18).
- Hypothèses concurrentes ACH (Ch.79 / MIRAGE 19).
- Rapport final intégré (Ch.93 / MIRAGE 20).

Chaque épisode illustre un aspect méthodologique. Le tout forme un parcours pédagogique complet.

-----
