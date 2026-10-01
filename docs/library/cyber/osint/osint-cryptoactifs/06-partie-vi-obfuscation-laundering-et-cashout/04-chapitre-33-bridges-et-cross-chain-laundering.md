---
title: Chapitre 33 — Bridges et cross-chain laundering
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VI — Obfuscation, laundering et cashout
  - index.md
---

Les **bridges** sont des protocoles permettant de transférer des actifs entre blockchains. Ils sont **infrastructure légitime** mais aussi vecteur majeur de blanchiment et de hacks. Comprendre leur fonctionnement et leurs limites pour l’enquête est central.

## 33.1 Pourquoi les bridges existent

**Problème** : un Bitcoin natif ne peut pas exister directement sur Ethereum. Une USDT ERC-20 (Ethereum) ne peut pas être directement transférée à une adresse TRC-20 (TRON). Les blockchains sont **isolées** par construction.

**Solution** : bridges permettent de « migrer » un actif d’une chaîne à une autre, par mécanismes variés.

**Mécanismes** :

**Wrapped tokens** : sur la chaîne destinataire, un token « wrapped » est créé représentant l’actif natif de la chaîne source. Exemple : WBTC (Wrapped Bitcoin) sur Ethereum est un ERC-20 dont la valeur correspond à du BTC réel détenu en custody.

- Étapes : utilisateur dépose BTC sur custody → mint WBTC sur Ethereum → utilise WBTC dans DeFi → burn WBTC + retrait BTC depuis custody.

**Lock-and-mint** : actif locké sur chaîne source, équivalent miné sur chaîne destinataire.

**Burn-and-mint** : actif burned sur chaîne source, miné sur chaîne destinataire.

**Liquidity pools cross-chain** : pools de liquidité présents sur multiples chaînes, swap effectif entre chaînes.

**Intermediate exchanges** : non un « bridge » technique, mais effet équivalent — passer par exchange centralisé pour switch entre chaînes.

## 33.2 Bridges majeurs

**Wormhole** : Ethereum, Solana, BNB, Avalanche, Polygon, etc. Hack majeur février 2022 (326 M USD).

**Multichain (anciennement Anyswap)** : multi-chain. Compromis 2023, ~130 M USD volés dans circumstances opaques.

**Stargate** : LayerZero-based, multi-chain.

**Synapse** : multi-chain.

**Hop Protocol** : Layer-2 Ethereum focus.

**Across** : multi-chain, optimistic.

**deBridge** : multi-chain.

**Rainbow Bridge** (Aurora / NEAR) : Ethereum-NEAR.

**WBTC** : centralisé, Bitcoin → Ethereum.

**RenBTC** : décentralisé, multi-chain BTC. RenVM stoppé en 2023, mais cf forks.

**THORChain** : decentralized cross-chain swaps. Multiple incidents et reprises.

**FixedFloat, ChangeNOW, SimpleSwap** : services de swap cross-chain non-KYC. Différents techniquement (intermediaires opérant des pools propres) mais effet bridge utilisateur.

**Pour l’enquêteur** : la liste évolue rapidement. Vérifier la couverture par les outils pro.

## 33.3 Pourquoi les bridges sont attractifs pour le blanchiment

**Casser la chaîne**. Un fonds passe d’Ethereum à BNB Chain via bridge. Suivre cross-chain demande capacité spécifique.

**Multi-juridictionnel**. Différentes blockchains ont différents écosystèmes (régulés / non-régulés, KYC / non-KYC). Bridge permet de glisser du « monitoré » au « moins monitoré ».

**Faible KYC**. Bridges typiques sont smart contracts non-custodial — pas de KYC.

**Vitesse**. Bridge typique : minutes à heures. Plus rapide que conversion via exchange centralisé.

**Volume liquide**. Multi-billion USD passent par bridges quotidiennement. Fonds illicites se fondent dans le bruit.

## 33.4 Hacks de bridges

Les bridges ont été ciblés massivement pour leurs vulnérabilités.

**Top hacks** :

- **Ronin** (mars 2022, 625 M USD) — Lazarus.
- **Wormhole** (février 2022, 326 M USD).
- **Nomad** (août 2022, 190 M USD).
- **Multichain** (juillet 2023, 130 M USD) — circumstances opaques.
- **Harmony Bridge** (juin 2022, 100 M USD) — Lazarus.
- **Orbit Chain** (janvier 2024, 80+ M USD).
- **Multiple autres** 2023-2026.

**Pourquoi cibles** :

- **Concentration de fonds** : bridges détiennent des centaines de millions USD en custody.
- **Code complexe** : surfaces d’attaque larges.
- **Validators externes** : si compromis, takeover possible.
- **Monitoring limité** : moins de regards techniques que sur protocoles DeFi mainstream.

**Pour l’enquêteur** : un hack de bridge nécessite **tracking cross-chain** intensif. Les attaquants utilisent les fonds pour disperser sur multiple chaînes immédiatement.

## 33.5 Suivre un fonds à travers un bridge

**Méthode** :

**Étape 1 — Identifier la transaction de dépôt sur chaîne source**. Adresse utilisateur → smart contract bridge.

**Étape 2 — Consulter les logs / events du bridge**. Le bridge émet un event décrivant la transaction destinataire (chaîne, adresse, montant).

**Étape 3 — Identifier la transaction correspondante sur chaîne destinataire**. Souvent quelques minutes à heures plus tard. Rechercher par adresse destinataire et montant.

**Étape 4 — Continuer le suivi sur la nouvelle chaîne**.

**Outils pro** : Reactor / TRM / Elliptic suivent automatiquement les bridges majeurs. Mais couverture variable selon bridge et selon outil.

**Outils gratuits** : pour bridges populaires (Stargate, Across), sites comme `socket.tech` ou `debridge.finance` ont des explorateurs cross-chain. Utile pour traçage manuel.

## 33.6 Limites du tracking cross-chain

**Pas tous les bridges sont supportés** par les outils pro. Bridges obscurs ou spécialisés peuvent passer sous le radar.

**Délai de résolution**. Sur certains bridges, le matching entre dépôt et retrait est différé. L’analyste peut perdre la trace si pas vigilant.

**Multiple hops cross-chain**. Fonds qui passent ETH → BSC → TRON → Polygon → ETH représentent une chaîne compliquée à suivre. Erreurs possibles à chaque saut.

**Liquidity pools** : les bridges via pools (Stargate, etc.) ne maintiennent pas un mapping 1-to-1 entre dépôts et retraits. Fonds entrent dans un pool, autres fonds sortent — l’utilisateur reçoit des fonds différents (en termes de UTXO).

**Wrapped tokens et redemption**. Un utilisateur peut wrap, déwrap, re-wrap — multiple cycles brouillent.

## 33.7 Tracking spécifique par bridge

**Wormhole** : explorateur Wormhole Scan permet de matcher transactions cross-chain. Émet events détaillés.

**Stargate** : Stargate Finance interface, transactions traçables via LayerZero events.

**Multichain** : historiquement traçable, mais post-compromis 2023, situation chaotique.

**WBTC / wrapped centralisés** : custody centralisée, mints et burns visibles. Mais pour suivre quel BTC correspond à quel WBTC, custody internal logs nécessaires.

**FixedFloat / ChangeNOW** : pas de matching public direct (services internalisent). Suivi par timing et montant possible mais probabiliste.

## 33.8 Coopération avec opérateurs de bridges

**Bridges decentralisés** : pas d’opérateur central à qui demander coopération. Smart contract immutable.

**Bridges semi-centralisés** (multisig validators, custodial) : peuvent coopérer sur réquisition. Cas variés.

**Wrapped tokens centralisés** (WBTC) : custody peut coopérer. WBTC custody (BitGo) coopère avec autorités sur cas légaux.

**FixedFloat / ChangeNOW / similaires** : politique de KYC / coopération variable. Souvent limitée.

## 33.9 Tendances 2024-2026

**Bridges restent vulnerables** : continuent à se faire hacker régulièrement.

**Sophistication de tracking** : Reactor / TRM / Elliptic améliorent couverture cross-chain. Mais lag sur nouveaux bridges.

**Régulation** : MiCA en EU pourrait éventuellement imposer KYC sur bridges, mais débat actif. Les bridges décentralisés posent question juridique (qui régule un smart contract ?).

**Layer-2 et bridges natifs** : Arbitrum, Optimism, Base bridges ont architectures différentes (rollups), tracking spécifique.

## 33.10 Fil rouge — MIXSHADOW : tracking cross-chain Akira

> **🔗 MIXSHADOW — Épisode 19 : la branche cross-chain**
> 
> Sarah a tracé une **branche secondaire** dans MIXSHADOW : ~5 BTC depuis le peeling chain ont été convertis via FixedFloat en USDT-Ethereum. Ces USDT ont ensuite été bridgés via **Stargate** vers BNB Chain.
> 
> **Tracking** :
> 
> - Transaction Ethereum : USDT-ETH → Stargate router contract.
> - Event Stargate : transfer to BNB Chain, destination address `0x[BNB-Akira]`.
> - Transaction BNB Chain : USDT-BNB reçus quelques minutes plus tard.
> 
> Reactor a suivi automatiquement. Validation manuelle via Stargate Finance interface confirme la correspondance.
> 
> Sur BNB Chain, suite : USDT-BNB swappés via DEX en BUSD (Binance USD), puis transférés vers adresses dépôt Binance. **3 dépôts Binance** identifiés sur cette branche.
> 
> **Coopération** : ces 3 adresses Binance (avec USDT cumulés ~30 000 USDT équivalent) sont transmises à la DGSI pour réquisition KYC. **2 mules identifiées** (cf Ch.30.9). Coopération Binance-DGSI productive.
> 
> Sarah note dans le rapport : la **branche cross-chain** Akira est plus modeste en volume (~5 BTC sur 35) que la branche TRON-USDT (~3 BTC qui sont devenus 290k USDT). Mais elle est **plus traçable** parce que Stargate est bien couvert par les outils et Binance KYC est solide. Paradoxe : le criminel qui choisit la « simplicité » (Stargate + Binance) est plus exposé que celui qui choisit le « non-KYC + dispersion » (FixedFloat + exchange non-KYC + hubs TRON). Akira a fait les deux choix sur des branches différentes — diversification des risques pour l’opérateur.
> 
> Cette observation (Akira diversifie les chemins de blanchiment) alimente la fiche acteur Akira pour la base Athéna et CTI sectoriel.

-----
