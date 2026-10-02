---
title: Chapitre 28 — Fraudes NFT, tokens frauduleux et rug pulls
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie V — Typologies d’abus crypto
  - index.md
---

L’écosystème NFT et tokens connaît une **forte sinistralité fraude**. Différentes typologies, chacune avec ses patterns.

## 28.1 Rug pulls

**Schéma** :

1. Création d’un token (ERC-20, BEP-20, SPL, etc.).
1. Marketing intense (Twitter, Discord, Telegram, parfois influenceurs).
1. Liquidité ajoutée sur DEX (paire token/ETH ou token/USDT).
1. Investisseurs achètent.
1. Au pic, **les créateurs vident la liquidité** (« pull the rug »).
1. Token à zéro, investisseurs perdent tout.

**Variantes** :

- **Soft rug** : créateurs disparaissent silencieusement, abandon du projet.
- **Hard rug** : drain explicite de la liquidité.
- **Honeypot** : token codé pour empêcher acheteurs de revendre (techniquement plus subtil).

**Reconnaissance** :

- Tokens nouveaux sans audit.
- Concentration de l’offre dans quelques wallets (owner garde 50%+).
- Liquidité non « locked ».
- Communauté artificielle (bots).

## 28.2 Honeypot tokens

**Mécanisme** : le smart contract du token contient une fonction cachée qui empêche les acheteurs (sauf le créateur) de revendre. Investisseurs achètent, **ne peuvent jamais sortir**.

**Détection** : analyse du code Solidity. Fonctions avec conditions cachées sur `transfer`. Outils comme Token Sniffer, GoPlus automatisent.

## 28.3 Pump-and-dump

**Schéma** :

1. Création / sélection d’un token de faible capitalisation.
1. Coordination dans groupes Telegram / Discord (« pump signal »).
1. Achats coordonnés synchronisés.
1. Cours du token explose (multiplication 5-50x).
1. Insiders / leaders **dumpent** au pic.
1. Cours s’effondre, late-comers perdent.

Sur Solana 2024-2026, l’écosystème **memecoin** (pump.fun et associés) industrialise ce schéma à échelle massive.

## 28.4 Fraude NFT

**Faux mint**. Site phishing imitant un drop NFT légitime. Demande approval qui draine wallet.

**Faux marketplace**. Plateforme imitant OpenSea/Blur, avec listings frauduleux ou drainer.

**Wash trading**. Achats / ventes d’NFT entre wallets contrôlés par même entité, pour gonfler artificiellement le « volume » et tromper acheteurs.

**Fake collections**. Collections imitant collections célèbres (CryptoPunks, BAYC) avec léger changement de nom ou logo.

**Fake floor**. Listings à très bas prix (faux) pour attirer attention sur une collection.

**Phishing Discord**. Hack de Discord officiel d’un projet NFT, annonce de mint frauduleux qui draine wallets.

## 28.5 Méthode d’enquête : rug pull

**Étape 1 — Indices**. Token contracté, plainte d’investisseurs.

**Étape 2 — Analyse du contrat**. Lecture Solidity (si vérifié) ou bytecode. Identification de fonctions backdoor.

**Étape 3 — Identification des wallets créateurs**. Adresse de déploiement du contrat. Premiers holders. Adresses ayant ajouté la liquidité initiale.

**Étape 4 — Analyse des mouvements**. Quand les créateurs ont-ils dump ? Vers où ?

**Étape 5 — Suivi des fonds**. Standard.

**Étape 6 — Identification des créateurs**. Si OPSEC faible (réutilisation d’adresses, déposit sur exchange KYC), attribution possible.

## 28.6 Méthode d’enquête : phishing NFT

**Étape 1 — Indices**. Victime fournit transaction de drain.

**Étape 2 — Identification du drainer**. Smart contract appelé. Souvent service connu (drainer-as-a-service).

**Étape 3 — Suivi des fonds**. Standard.

## 28.7 Limites

**Volume massif**. Trop de rug pulls / scams pour tous les enquêter individuellement. Triage obligatoire (impact, victimes notables).

**Anonymat des créateurs**. Souvent OPSEC stricte (création depuis wallets fonds Tornado Cash, etc.).

**Aspects civils vs pénaux**. Beaucoup de rug pulls relèvent de **fraude civile** plus que pénale (selon juridiction, intentionnalité difficile à prouver).

## 28.8 Tendances 2024-2026

**Memecoin scams** : explosion via pump.fun et écosystème Solana.

**AI-generated NFT scams** : NFT générés en masse pour rug pull.

**Cross-chain rug pulls** : exploitation de bridges et confusion multi-chaîne.

-----
