---
title: Chapitre 34 — DEX, swaps et obfuscation DeFi
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VI — Obfuscation, laundering et cashout
  - index.md
---

Les **DEX** (decentralized exchanges) et plus largement les **protocoles DeFi** offrent des outils additionnels d’obfuscation. Plus subtils que mixers ou bridges, ils permettent transformations d’actifs et brouillage des origines.

## 34.1 Les principaux DEX

**Uniswap** (Ethereum) : référence. Multi-version (V2, V3, V4). Pools de liquidité automated market maker (AMM).

**SushiSwap** : fork Uniswap, multi-chain.

**Curve Finance** : spécialisé stablecoins et actifs corrélés. Faible slippage sur paires similaires.

**PancakeSwap** : leader sur BNB Chain. Équivalent Uniswap.

**Balancer** : pools customisables, multi-actifs.

**1inch, Matcha, Paraswap** : aggregators (routent à travers multiple DEX pour meilleur prix).

**dYdX, GMX** : DEX dérivés (perpétuels, options).

**Trader Joe** : DEX Avalanche.

**Raydium, Orca, Jupiter** : DEX Solana.

**SunSwap, JustLend** : écosystème TRON.

## 34.2 Pourquoi les DEX permettent obfuscation

**Pas de KYC**. Smart contracts non-custodial. Pas d’identité requise.

**Conversion d’actifs**. ETH → USDT en quelques secondes. Brouille l’origine.

**Liquidité massive**. Volumes énormes. Fonds illicites se fondent dans le bruit.

**Multi-pool / multi-route**. Aggregators routent via plusieurs pools. Trace plus complexe.

**Multi-chain**. Combinaison DEX + bridge donne transformations multi-chaînes.

## 34.3 Patterns d’obfuscation via DEX

**Conversion simple**. Adresse reçoit ETH suspect, swap en USDT, USDT déposé sur exchange → KYC trace plus difficile.

**Multi-hop**. ETH → USDT → DAI → USDC → ETH. Multiple swaps redondants avant l’objectif. Brouille analyse simple.

**Yield farming intermédiaire**. Dépôt en pools de liquidité, claim de fees, retrait. Crée de l’historique « DeFi natural » qui peut tromper analyse superficielle.

**Flash loan layering**. Plus avancé : utilisation de flash loans pour manipulation de pools / arbitrage. Les fonds passent par multiple protocoles en une seule transaction.

## 34.4 Tracker un swap DEX

**Étape 1 — Identifier la transaction de swap**. Sur Etherscan, transaction qui appelle un DEX router.

**Étape 2 — Lire les logs**. Events `Swap` indiquent montants et tokens d’entrée/sortie.

**Étape 3 — Comprendre la route**. Aggregators peuvent passer par 2-5 pools en une transaction. Analyser tous les hops.

**Étape 4 — Continuer le tracking sur les fonds reçus**. Adresse user reçoit le token de sortie.

**Outils pro** : Reactor / TRM / Elliptic suivent automatiquement à travers DEX. Excellente couverture pour DEX mainstream.

**Outils gratuits** : Etherscan affiche transactions DEX bien décodées si contrats vérifiés (presque toujours le cas pour DEX majeurs).

## 34.5 Limites

**Multi-hop complexe**. Un aggregator routant via 5 pools est plus difficile à parser visuellement (mais bien décodé par les outils).

**MEV (Maximal Extractable Value)**. Les bots MEV peuvent intervenir dans les transactions, complexifiant l’analyse.

**Liquidity provider activity**. Si le criminel agit comme LP (provide liquidity), ses fonds sont mélangés avec la liquidité globale du pool. Tracking devient probabiliste.

**Pool extractables**. Certains LPs custodial peuvent retirer (par exemple, récupération fonds d’une pool LP), brouillant les traces.

## 34.6 Cas typiques

**Hack DeFi → swap rapide**. Attaquant draine un protocole DeFi, swap rapidement les tokens volés en stablecoin ou ETH (plus liquide), puis suit chemin classique d’obfuscation. Vu dans nombreux hacks 2022-2026.

**Pig butchering → swap pré-cashout**. Fonds USDT-TRON consolidés peuvent être swappés en autres stablecoins ou BTC pour faciliter cashout sur certaines plateformes.

**Ransomware → swap pour anonymisation**. Cf MIXSHADOW : Akira a swappé partiellement BTC en ETH via FixedFloat avant Tornado Cash.

## 34.7 Différence DEX vs CEX vs swap services

**DEX** (Uniswap, etc.) : smart contract pur. Pas de KYC. Pas d’opérateur central pour coopération.

**CEX** (Binance, etc.) : entreprise centralisée. KYC. Possible coopération.

**Swap services** (FixedFloat, ChangeNOW, SimpleSwap) : services qui permettent swap sans KYC mais avec opérateur central. Hybrides — pas vraiment décentralisés (l’opérateur peut blacklister, refuser), pas vraiment KYC. Souvent utilisés pour cross-chain rapide. Coopération variable selon service.

## 34.8 Tendances 2024-2026

**Volume DEX en croissance**. DeFi mature, plus d’utilisateurs.

**Cross-chain DEX** : 1inch Cross-chain, autres aggregators cross-chain.

**Régulation** : MiCA cible exchange centralisés, mais DEX est zone grise. Débat actif.

**Réseaux MEV-dominants** : MEV-Boost et auctions deviennent partie intégrale de l’écosystème, complexifiant l’analyse.

**Pour l’enquêteur** : DEX est **moins une rupture de visibilité qu’un détour traçable**. Ne pas avoir peur, mais ajouter au temps d’analyse.

-----
