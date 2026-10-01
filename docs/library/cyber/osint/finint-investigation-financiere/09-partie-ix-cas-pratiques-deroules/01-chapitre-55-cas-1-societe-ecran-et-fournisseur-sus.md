---
title: 'Chapitre 55 — Cas 1 : Société écran et fournisseur suspect'
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie IX — Cas pratiques déroulés
  - index.md
---

## Contexte

Une grande entreprise française du secteur BTP, **CONSTRUCT FRANCE SA**, fait appel à un cabinet de compliance externe à la suite d’une alerte du contrôle interne : un fournisseur récent, **BTP SERVICES INTERNATIONAL SARL**, basé en France, présente des caractéristiques inhabituelles. La compliance a déjà identifié plusieurs signaux mais sollicite une analyse FININT externe pour qualifier.

**Demande** : qualifier la nature et le risque associés à BTP SERVICES INTERNATIONAL.

## Indices initiaux fournis

- Société française créée 11 mois avant le premier marché avec CONSTRUCT.
- Capital social 1 000 €.
- Dirigeant unique, ancien retraité du secteur agro-alimentaire.
- Domiciliation à un cabinet de domiciliation parisien.
- Aucun site web.
- Volume de prestations facturé sur 6 mois : 1,4 M€.
- Facturations très techniques (sous-traitance gros œuvre, ferraillage, étanchéité).
- Bénéficiaire effectif déclaré au RBE : le dirigeant unique.

## Cadrage initial

**Questions de renseignement** :

- QR1 — La société a-t-elle une activité économique réelle ?
- QR2 — Quel est l’UBO réel ?
- QR3 — Quel est le réseau de relations de cette société ?
- QR4 — Quel est le profil de risque (fraude fiscale, ABS, blanchiment, fronting) ?

**Budget temps estimé** : 2 semaines.

**Limites prévisibles** : sans réquisition, accès limité aux relevés bancaires et à la comptabilité détaillée.

## Collecte

**OSINT registres** :

- Pappers + INPI + Companies House (rien à l’étranger). SIREN, K-bis, statuts, comptes (1er exercice non clos).
- Recherche par dirigeant : la personne est gérante d’une seule société. Pas multi-mandats. Mais profil incohérent (retraité agro vs gros œuvre).
- BODACC : pas de procédure.

**OSINT divers** :

- LinkedIn du dirigeant : profil très minimal, aucune photo, aucune mention BTP.
- Adresse de domiciliation : 32 autres entités à la même adresse. Variées, peu de cohérence sectorielle.

**Sources adjacentes** :

- Le dirigeant a un fils. Recherche par nom : le fils, M. R, dirige une autre société de BTP en région parisienne, **R-CONSTRUCT SARL**, qui a connu une procédure collective il y a 3 ans (liquidation pour passifs URSSAF et fiscaux).
- Croisement : l’adresse personnelle déclarée par M. R correspond à celle du père (domiciliation familiale plausible).
- Recherche presse : un article local de 2021 mentionne un dossier de fraude TVA en BTP impliquant plusieurs sociétés en lien avec M. R (instruction en cours à l’époque ; pas d’information sur la suite).

**Compliance interne CONSTRUCT (partagé)** :

- Sur 6 mois, BTP SERVICES INTERNATIONAL a facturé 1,4 M€ à CONSTRUCT pour des prestations dont la traçabilité physique (présence de personnel sur chantier, signatures pointage) est faible voire absente.
- Les factures ont été acquittées par virements vers un compte de la société à la Banque XX (France).

## Analyse

**Substance économique** : faible. Pas de personnel déclaré (URSSAF non accessible à l’externe), pas de matériel, pas de présence opérationnelle visible. Le dirigeant officiel n’a aucune compétence visible en BTP.

**UBO réel probable** : *probable* que M. R (le fils) soit l’UBO réel, via prête-nom paternel. Indices convergents : profil incohérent du dirigeant officiel, historique BTP de M. R, contentieux antérieur de M. R, adresse partagée, période de création (un an après la liquidation de R-CONSTRUCT — délai typique de reconstruction sous nouveau nom).

**Typologie probable** : compatible avec **fronting** (M. R, ayant des contentieux et difficultés antérieures, utilise une société au nom du père pour continuer ses activités) **et/ou** avec un schéma de **facturation fictive** au profit de CONSTRUCT (rétrocommissions, mise à disposition de travail au noir, fraude URSSAF). Sans accès aux relevés et au pointage de chantier, distinction *indéterminable* à ce stade.

## Hypothèses calibrées

- **H1 — Fronting + activité réelle (M. R reprend une activité légale via prête-nom paternel)** : probable.
- **H2 — Facturation fictive et travail dissimulé** : possible à probable.
- **H3 — Schéma de blanchiment** : peu probable au vu des éléments (les flux sont entrants depuis CONSTRUCT, pas d’origine externe suspecte).
- **H4 — Société écran à finalité de carrousel TVA** : peu probable (pas de cycle observable, profil mono-client).

## Limites

- Sans réquisition des relevés bancaires et des pointages de chantier, impossible de distinguer H1 de H2.
- Sans accès aux déclarations URSSAF, impossible de qualifier le travail dissimulé.
- L’UBO réel = M. R reste *probable*, pas *quasi-certain*.

## Livrable

Rapport au client (CONSTRUCT) :

- Société présentant *probable* fronting.
- Risque de facturation fictive ou de travail dissimulé : *possible à probable*.
- Recommandations :
  - **Rupture progressive** de la relation commerciale, avec mention explicite du risque dans le dossier compliance.
  - **Plainte au procureur de la République** (article 40 CPP ne s’applique pas à une entreprise privée, mais une plainte est ouverte à toute personne morale victime ou témoin d’infractions) si éléments suffisants de facturation fictive ou d’escroquerie au préjudice de CONSTRUCT.
  - **Signalement à l’inspection du travail** pour le volet travail dissimulé.
  - **Signalement à l’URSSAF** et à la **DGFiP** selon les indices.
  - **Important** : une entreprise du BTP comme CONSTRUCT n’est **pas, en principe, assujettie LCB-FT** au sens du Code monétaire et financier. La déclaration de soupçon à TRACFIN concerne les **assujettis** (banques, PSP, notaires, certaines professions). CONSTRUCT ne peut donc pas faire de DS TRACFIN ; ses signalements passent par les voies évoquées ci-dessus (plainte, inspection, URSSAF, DGFiP). C’est sa **banque** qui, le cas échéant, sera assujettie et susceptible de produire une DS sur les flux observés.
  - **Audit interne** sur les processus de KYB fournisseurs.

## Bilan honnête

L’enquête a permis de qualifier rapidement (2 semaines) un fournisseur à risque, sans coût ni outils professionnels lourds (gratuits : Pappers, Companies House, BODACC, LinkedIn, presse locale, recherches d’état civil partielles). La qualification reste à un niveau *probable* — la confirmation *quasi-certaine* exigerait des éléments accessibles seulement en cadre judiciaire ou inspection. C’est une qualification utile à CONSTRUCT : suffit à motiver des décisions internes (rupture commerciale, signalement) sans engager judiciairement CONSTRUCT au-delà de ses obligations.

## Leçons FININT

- **Le profil du dirigeant** est souvent un signal de premier ordre. Un retraité agro à la tête d’une société de gros œuvre = signal fort.
- **L’antériorité familiale ou relationnelle** : un fronting via parent est un classique.
- **La cohérence sectorielle** : 32 entités domiciliées au même cabinet sans cohérence sectorielle = signal de cluster suspect.
- **Limites d’OSINT** : sans réquisition, on s’arrête à *probable*. C’est suffisant pour motiver une rupture commerciale ; insuffisant pour qualifier judiciairement.

-----
