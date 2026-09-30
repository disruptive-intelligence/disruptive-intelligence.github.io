---
title: 'Chapitre 39 — Cas 4 : flux multi-chaînes avec bridge et stablecoins'
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VII — Cas pratiques déroulés
  - index.md
---

**Profil de l’enquête** : enquête sur une fraude internationale (intermédiaire commercial frauduleux) impliquant flux multi-chaînes complexes. Cas qui montre la complexité de l’enquête moderne.

## 39.1 Le contexte

**Société victime** : « ImportExport SAS » (nom fictif), ETI française d’import-export de matériels électroniques, ~50 employés, CA ~25 M EUR/an.

**L’incident** :

ImportExport est cliente d’un fournisseur asiatique (Vietnam). Pour un contrat de 800 000 USD, négociation avec interlocuteur habituel (M. Tran, directeur achat, ImportExport est en relation depuis 3 ans).

Mi-février 2026, M. Tran annonce changement de procédure de paiement : fournisseur a souffert de problèmes bancaires (sanctions banques vietnamiennes liées à un autre dossier), nouvelle procédure : paiement en **USDT-Tron** vers une adresse fournie. Justification crédible. Email de confirmation reçu sur l’adresse habituelle de M. Tran.

Mi-février 2026 : ImportExport convertit 800 000 USD en USDT (via partenaire crypto OTC français régulé) et transfère vers l’adresse fournie.

Une semaine plus tard, contact direct au téléphone avec M. Tran (pas à Tran officiel mais à son standard) : Tran n’a **jamais demandé de paiement crypto**. Compromission de son email professionnel découverte. ImportExport est **victime de BEC (Business Email Compromise)** sophistiquée — avec demande de paiement détournée vers crypto.

**Mandat** : ImportExport mandate un cabinet pour cartographier les flux et soutenir plainte. Coopération avec autorités françaises ET vietnamiennes (M. Tran réel coopère également pour son côté). 6 semaines, 50 000 EUR.

## 39.2 Phase 1 — Lecture initiale

**Inputs** :

- TXID du transfert USDT-TRON.
- Adresse destinataire : `TR[fraud-receive]...`.
- Email frauduleux et son origine technique.

**Étape 1 — Vérification on-chain**.

Tronscan : 800 000 USDT transférés à 2026-02-18 09:43 UTC vers `TR[fraud-receive]...`.

Adresse fraîche, première activité = ce transfert. Suggère adresse dédiée à cette fraude.

**Étape 2 — Suite immédiate**.

À 2026-02-18 11:15 UTC (90 minutes après réception), `TR[fraud-receive]` envoie l’intégralité (800 000 USDT) vers `TR[fraud-ops1]`.

Délai bref : opérateur supervise le compte ou bot automatique.

## 39.3 Phase 2 — Cascade multi-chaîne

**Étape 1 — Mouvement TR[fraud-ops1]**.

À 2026-02-18 12:30 UTC, `TR[fraud-ops1]` :

- Conserve 200 000 USDT-TRON.
- Convertit 600 000 USDT-TRON via SunSwap DEX en TRX puis re-swap en USDT-Ethereum via service de swap cross-chain (FixedFloat ou équivalent).

Le swap cross-chain est **traçable** mais demande matching manuel : USDT-TRON sortie sur TRON, USDT-Ethereum entrée sur Ethereum quelques minutes plus tard.

**Étape 2 — Sur Ethereum**.

À 2026-02-18 13:45 UTC, 600 000 USDT-Ethereum reçus sur `0x[fraud-eth1]...`.

Quelques minutes plus tard :

- 300 000 USDT-Ethereum → bridge **Stargate** vers BNB Chain.
- 300 000 USDT-Ethereum → swap via Uniswap en ETH (~85 ETH au cours du moment).

**Étape 3 — Sur BNB Chain**.

USDT-BNB reçus. Quelques minutes plus tard, swap en BUSD via PancakeSwap.

BUSD transférés en 5 sub-adresses (60 000 BUSD chaque). Patterns de dispersion.

**Étape 4 — Sur Ethereum (suite swap ETH)**.

85 ETH dans `0x[fraud-eth1]`. Sur les 24h suivantes :

- 50 ETH déposés en 5 dépôts vers Tornado Cash (10 ETH × 5).
- 25 ETH transférés vers `0x[fraud-eth2]`.
- 10 ETH consolidés vers wallet opérationnel.

## 39.4 Phase 3 — Cartographie complète

**À 1 semaine** : l’analyste a reconstitué la cascade :

```
ImportExport (800k USDT-TRON)
    ↓
TR[fraud-receive] (90 min)
    ↓
TR[fraud-ops1]
    ↓ split:
    ├── 200k USDT-TRON (reste sur TRON, dispersion vers hubs)
    └── 600k → cross-chain
              ↓
         0x[fraud-eth1] sur Ethereum
              ↓ split:
              ├── 300k → Stargate → BNB Chain → BUSD → 5 sub-addresses
              └── 300k → Uniswap swap → 85 ETH
                        ↓ split:
                        ├── 50 ETH → Tornado Cash
                        ├── 25 ETH → 0x[fraud-eth2]
                        └── 10 ETH → consolidation
```


**Outils utilisés** : Reactor pour suivi automatique, validation manuelle sur Etherscan / Tronscan / BscScan, Stargate Finance pour matching cross-chain.

**Étape — Caractérisation des destinations finales** (à 4 semaines) :

**Sur TRON** (200k USDT) :

- Layering via 6 hops jusqu’à dépôts vers exchange asiatique non-KYC.
- ~150k USDT cumulés identifiés sur exchange Y.

**Sur BNB Chain** (300k USDT puis BUSD) :

- 5 sub-adresses → consolidation puis dépôts Binance (KYC).
- 5 dépôts Binance identifiés totalisant ~280k BUSD.

**Sur Ethereum** :

- Tornado Cash (~50 ETH = ~150k USD équivalent) : rupture de visibilité.
- `0x[fraud-eth2]` → bridge vers Polygon → swap → consolidation. ~75k USD équivalent suivi jusqu’à dépôts Coinbase Pro.
- Consolidation 10 ETH : reste dormant, pas de mouvement à 4 semaines.

## 39.5 Phase 4 — Coopération et identification

**Étape 1 — Binance (BNB Chain dépôts)**.

DGSI envoie réquisition à Binance pour les 5 dépôts BNB Chain.

Retour Binance (3 semaines plus tard) :

- 5 comptes identifiés, KYC complets.
- 4 mules : individus en Asie du Sud-Est avec patterns de mules (comptes ouverts récemment, multiple flux de dépôts crypto, retraits rapides).
- 1 compte semble-t-il du « cerveau » : individu en Russie (KYC valide), ~80k BUSD récupérés (gel) avant retrait.
- Total gelé Binance : ~80k EUR équivalent.

**Étape 2 — Coinbase Pro (75k USD via Polygon)**.

Réquisition Coinbase. Retour : 1 compte, mule en Roumanie. Fonds déjà retirés. Pas de gel.

**Étape 3 — Exchange non-KYC asiatique**.

Pas de coopération directe. Sanctions évaluées par DGSI mais procédures internationales lentes.

**Étape 4 — Email frauduleux**.

Forensics email coordonnée avec FAI vietnamien : compromission révèle malware infostealer sur poste de M. Tran ayant volé credentials email il y a 3 mois. **Pas un acteur étatique** — fraude opportuniste par groupe BEC.

Patterns techniques cohérents avec **groupe BEC russophone** (même infrastructure / même style de messages que d’autres incidents BEC documentés). Attribution **probable** russophone, mais pas plus précis.

## 39.6 Phase 5 — Bilan

**Total tracé** : ~625k USD sur 800k initial (78%).

**Total gelé / récupéré** : ~80k EUR (Binance, ~10% du total).

**Tornado Cash** : ~150k USD perdus dans rupture analytique.

**Exchange non-KYC asiatique** : ~150k USDT, possible récupération via coopération internationale ultérieure.

**Identification** :

- 4 mules identifiées (utiles pour enquête judiciaire).
- 1 acteur principal en Russie (KYC fourni).
- Profil acteur principal : russophone, BEC professionnel.

## 39.7 Rapport et action

**Rapport de 42 pages** :

- Executive summary.
- Méthodologie.
- Reconstitution timeline complète.
- Cartographie multi-chaînes (graphes Reactor + Maltego).
- Identifications et coopérations.
- Recommandations.
- Limites.

**Recommandations à ImportExport** :

- Sécurisation des emails (MFA, monitoring).
- Procédure de validation pour changements de paiement (téléphone direct + canal indépendant).
- Formation des équipes finance.
- Cyber-insurance évaluation.

**Recommandations autorités** :

- Soutenir procédure judiciaire avec pièces fournies.
- Coopération DGSI / Vietnam / Russie selon accords bilatéraux.
- Sanctions OFAC évaluation pour exchange non-KYC asiatique.

## 39.8 Bilan honnête

✅ **Réussites** :

- Cartographie multi-chaînes complète (BTC → ETH → BNB → Polygon).
- Identification de 5 KYC (4 mules + 1 acteur principal).
- 80k EUR gelés.
- Profil acteur établi.

⚠️ **Limites** :

- 22% des flux non tracés (Tornado Cash, exchange non-KYC).
- Récupération limitée à ~10%.
- Acteur principal en Russie : peu coopération attendue.

**Apprentissage clé** : pour fraude multi-chaîne sophistiquée, l’enquête est **fastidieuse mais payante**. Les outils pro permettent le tracking cross-chain. La coopération exchanges régulés finit par produire des KYC. Le bilan financier est modeste mais le bilan **renseignement** est solide.

-----
