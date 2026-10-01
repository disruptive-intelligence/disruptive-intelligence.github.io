---
title: Chapitre 37 — Registres corporate et sources internationales
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VI — Corporate, infrastructure et données exposées
  - index.md
---

## 37.1 Tour d'horizon

Ce chapitre détaille les **registres officiels** et **sources internationales** par juridiction, en se concentrant sur ceux qui sont accessibles en source ouverte gratuite ou semi-gratuite.

## 37.2 France — l'écosystème complet

**Pappers** (pappers.fr). Interface publique gratuite (limitée) et payante. Combine RNE, RBE, BODACC, INPI, ARCEP. C'est le standard pour la France.

**Infogreffe** (infogreffe.fr). Registre officiel des greffes. Accès gratuit aux KBIS partiel, payant pour comptes détaillés.

**RNE — Registre National des Entreprises.** Depuis 2023, registre unifié remplaçant RCS, RM, registre des actifs agricoles. Accessible via Pappers, INPI.

**RBE — Registre des Bénéficiaires Effectifs.** Géré par INPI. Accessible avec authentification.

**BODACC** (bodacc.fr). Bulletin Officiel des Annonces Civiles et Commerciales. Création, modifications, ventes, procédures collectives. Recherchable en ligne.

**INPI**. Marques, brevets, dessins.

**societe.com**, **manageo.fr**, **verif.com**. Agrégateurs gratuits, données partielles.

## 37.3 Royaume-Uni — Companies House

**Companies House** (gov.uk/government/organisations/companies-house). Registre officiel UK, **entièrement gratuit** et très bien documenté. Standard mondial de transparence.

**Données accessibles.**

- Identité légale complète.
- Dirigeants et anciens dirigeants.
- UBO (depuis 2016, registre PSC — People with Significant Control).
- Comptes annuels publiés.
- Filings (statuts, modifications).

**API gratuite** disponible.

## 37.4 États-Unis — fragmentation par état

L'enregistrement des sociétés est **étatique** aux US, pas fédéral.

**Delaware** : juridiction préférée. Search via Delaware Department of State.

**Californie, Nevada, Texas, New York, Floride** : portails dédiés par état.

**Pour les sociétés cotées.** **SEC EDGAR** (sec.gov/edgar) : référence pour filings boursiers (10-K, 10-Q, 8-K, proxy statements). Mine d'information sur dirigeants, rémunérations, transactions internes.

**Limites US.**

- Registres étatiques souvent peu transparents (Delaware notamment).
- Pas de registre UBO fédéral (Corporate Transparency Act 2024 ralenti par contentieux).
- Coût d'accès aux comptes détaillés.

## 37.5 Union Européenne — registres nationaux

**Belgique** : Banque-Carrefour des Entreprises (BCE / CBE), gratuit.

**Allemagne** : Handelsregister, gratuit base, payant pour comptes.

**Pays-Bas** : KvK (Kamer van Koophandel), payant la plupart des données.

**Italie** : Registro Imprese, accès payant pour la plupart des fonctions.

**Espagne** : Registro Mercantil, payant.

**Irlande** : Companies Registration Office (CRO), gratuit.

**Luxembourg** : RCS (Registre de Commerce et des Sociétés), gratuit base.

**Malte** : Companies Registry, gratuit (recherche), payant (extracts).

**Chypre** : Department of Registrar of Companies, gratuit base.

## 37.6 Paradis fiscaux et juridictions opaques

Les juridictions opaques varient en transparence.

**Plus accessibles.** Malte (UE, donc registre UBO récent), Chypre (UE), Luxembourg.

**Difficiles.** BVI, Cayman Islands, Bermuda, Liechtenstein. Registres existants mais accès très restreint.

**Très difficiles.** Panama (avant Panama Papers), Belize, Seychelles, certaines juridictions Pacifique.

**Pour ces juridictions opaques :**

- **ICIJ leaks** sont la principale source (Panama, Paradise, Pandora, Cyprus Confidential).
- **OCCRP Aleph** agrège.
- Documents internes leakés sur dark web (à manier avec déontologie).

## 37.7 OpenCorporates : méta-agrégateur

**OpenCorporates** (opencorporates.com) agrège les registres officiels de **140+ juridictions**.

**Forces.**

- Recherche cross-juridiction.
- Graph d'officiers (dirigeants partagés).
- API.
- Données mises à jour.

**Limites.**

- Couverture variable selon registres (parfois superficielle).
- API payante au-delà du freemium.
- Pas tous les UBO (dépend des registres sources).

## 37.8 ICIJ Offshore Leaks Database

L'**ICIJ Offshore Leaks Database** (offshoreleaks.icij.org) est un agrégateur public des grands leaks.

**Inclus.**

- Panama Papers (2016).
- Paradise Papers (2017).
- Pandora Papers (2021).
- FinCEN Files (2020) — partiel.
- Cyprus Confidential (2023).
- Other leaks plus anciens (Offshore Leaks 2013).

**Forces.**

- Recherche par nom, juridiction.
- Visualisation des liens.
- Sources documentaires partielles consultables.

**Limites.**

- Ce qui est leaké ≠ exhaustif.
- Recoupements nécessaires.
- Données d'années diverses.

## 37.9 OCCRP Aleph

**Aleph** (aleph.occrp.org) est la plateforme journalistique OCCRP.

**Contenu.**

- Registres corporate (sélection).
- Leaks (sélection des ICIJ et autres).
- Documents publics (filings, contrats publics).
- Listes sanctions, PEP.
- Documents OCCRP propres.

**Accès.**

- Une partie public (gratuit).
- Accès journaliste pour fonctions avancées (sur demande motivée).

## 37.10 Bureau van Dijk Orbis et alternatives payantes

Pour les usages corporate intensifs :

- **Orbis** (Bureau van Dijk / Moody's) : 400+ M de sociétés mondiales, données financières profondes. ~50-200 k€/an.
- **Sayari** : alternative orientée OSINT, fortes capacités sur Chine, Russie, Iran.
- **Dun & Bradstreet** : standard credit reporting.
- **Bisnode** : européen.

Réservés aux cabinets professionnels avec budget.

## 37.11 Synthèse — quelle source pour quel besoin

| Besoin | Source prioritaire |
|---|---|
| Société française | Pappers + Infogreffe + BODACC |
| Société UK | Companies House (gratuit, complet) |
| Société UE | OpenCorporates + registre national |
| Société US cotée | SEC EDGAR |
| Société US non cotée | Registre étatique (Delaware, etc.) |
| Paradis fiscal | OpenCorporates + ICIJ leaks + Aleph |
| UBO multi-juridictions | Aleph + Orbis (si dispo) + Pappers + ICIJ |
| Cross-juridiction rapide | OpenCorporates |
| Investigation journalistique | OCCRP Aleph + ICIJ |

-----
