---
title: Chapitre 26 — Ransomware et extorsion
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie V — Typologies d’abus crypto
  - index.md
---

Le ransomware est l’un des plus gros postes médiatisés de cybercriminalité. Pour l’enquêteur crypto, c’est aussi un **flux structuré et reconnaissable**, particulièrement adapté à l’analyse on-chain.

## 26.1 Le modèle économique

**Acteurs** :

- **Opérateurs / développeurs** : fournissent malware + infrastructure (leak site, portail négociation).
- **Affiliés** : exécutent les attaques, prennent typiquement 70-80% des rançons.
- **Initial Access Brokers (IAB)** : vendent les accès initiaux aux affiliés.
- **Négociateurs** : négocient avec les victimes côté criminel.
- **Services de blanchiment** : prennent en charge les flux post-paiement.

**Flux financier typique** :

1. Victime paie en crypto (BTC dominant, parfois XMR pour Monero-only).
1. Adresse de réception dédiée à la victime.
1. Mouvement post-paiement : peeling chain ou consolidation rapide.
1. Conversion potentielle (vers stablecoins, autres chaînes).
1. Anonymisation : mixers, bridges, swaps.
1. Cashout : exchanges non-KYC, P2P, OTC.

## 26.2 Le paiement

**Formats** :

- **Adresse fournie via portail Tor** : opérateurs maintiennent portails de négociation .onion, victime y accède pour négocier et obtenir l’adresse.
- **Adresse dans note de rançon** : moins courant pour gros opérateurs (préfèrent négociation), plus fréquent pour ransomware moins ciblé.
- **Email avec adresse** : sextortion et ransomware basique.

**Délai de paiement** : typiquement 7-14 jours négociés. Au-delà, leak site publication ou augmentation de la demande.

**Adresses fraîches dédiées**. La pratique standard est : **une adresse par victime**, fraîche, jamais utilisée. Évite que d’autres victimes (ou des observateurs) voient les paiements totaux.

## 26.3 Reconnaître un cluster ransomware

**Signaux d’une adresse ransomware** :

**Réception unique de gros montant**. Adresse fraîche reçoit un montant rond ou semi-rond (35 BTC, 50 BTC, 100 BTC…) en une seule transaction.

**Mouvement rapide post-paiement**. Le délai entre réception et premier mouvement est souvent court (heures à 1-2 jours).

**Pattern de blanchiment standardisé**. Peeling chain, consolidation, conversions. Les opérateurs établis ont des patterns reconnaissables.

**Multiple paiements pour le même opérateur**. Sur les outils pro, les clusters ransomware sont identifiés (« cluster Akira », « cluster LockBit », « cluster Black Basta »). Les nouvelles adresses sont assignées au cluster sur la base d’heuristiques + labels propriétaires.

## 26.4 Cluster opérateur vs cluster affilié

Distinction importante.

**Cluster opérateur** : infrastructure de l’opérateur (développeurs du ransomware). Reçoit la part de l’opérateur (~20-30% des rançons). Stable dans le temps.

**Cluster affilié** : infrastructure des affiliés. Reçoit la part de l’affilié (~70-80%). Multiple affiliés par opérateur, chacun avec ses patterns.

**Pour l’enquêteur** : identifier si l’enquête remonte vers opérateur ou affilié change la lecture. Affilié = un acteur parmi N. Opérateur = peut révéler infrastructure plus large.

## 26.5 Méthode d’enquête

**Étape 1 — Indices initiaux**. Adresse de paiement (du portail négociation, de la note ransomware, ou de la victime).

**Étape 2 — Validation**. TXID confirmant le paiement. Lecture sur Mempool.

**Étape 3 — Identification du cluster**. Outils pro identifient le cluster. Parfois directement attribué à un groupe ransomware.

**Étape 4 — Suivi des flux**. Comme MIXSHADOW : peeling chain, conversions, etc.

**Étape 5 — Identification des points de coopération**. Exchanges traversés, mixers, bridges.

**Étape 6 — Caractérisation du groupe**. Patterns, infrastructure, leak site, victimologie.

**Étape 7 — Rapport et coopération**.

## 26.6 Coopération avec les autorités

**FBI Cyber Division** (US) : référence pour ransomware. Multiple opérations (saisie Bitfinex, opération Cronos contre LockBit, etc.).

**NCA (UK)** : équivalent.

**Europol EC3** : coordination EU.

**ANSSI / DGSI / TRACFIN** (France) : pour victimes françaises.

**BKA (Allemagne)**.

**Coopération exchanges** : nombreux exchanges réguliers gèlent fonds tracés à ransomware sur réquisition.

**Coopération émetteurs stablecoins** : Tether et Circle ont gelé à plusieurs reprises des fonds de groupes ransomware.

## 26.7 Le débat « payer ou pas »

**Position officielle (US, France, UK)** : **déconseiller le paiement**. Arguments :

- Finance la criminalité.
- Ne garantit pas le déchiffrement.
- Crée incitation pour autres attaques.
- Peut violer sanctions OFAC (si groupe sanctionné).

**Réalité** : la décision relève de la victime, sous pression vitale (cf MIXSHADOW). Pas de critère universel.

**Pour l’enquêteur** : pas de jugement moral. Si paiement, l’enquête maximize la valeur (récupération potentielle, attribution, contribution sectorielle).

## 26.8 Tendances 2024-2026

**Multi-extorsion** : chiffrement + exfiltration + chantage clients + DDoS. Rançons plus élevées.

**Dual ransomware** : double chiffrement par deux groupes différents (rare mais documenté).

**Ciblage de la santé et OIV** : croissance.

**Sanctions et démantèlements** : LockBit (Operation Cronos février 2024), AlphaV/BlackCat, Hive (saisie 2023). Écosystème en mutation continue.

**Akira, Black Basta, Play, LockBit (relaunch), Medusa** : groupes actifs 2025-2026.

**Pour l’enquêteur** : la **typologie ransomware est pleine d’enjeux** mais aussi de **success stories** (Bitfinex saisie 3,6 Mrd, Colonial Pipeline récupération 2,3 M, opérations Cronos). L’enquête contribue.

-----
