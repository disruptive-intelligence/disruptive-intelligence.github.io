---
title: 'Chapitre 72 — Crypto-actifs et blockchain : panorama OSINT'
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - 'PARTIE X — Passerelles spécialisées : FININT, Crypto, CTI, Influence'
  - index.md
---

## 72.1 Vue maître crypto

L'**OSINT crypto** est devenu un pan structurant entre 2017 et 2026, avec l'explosion des actifs numériques, leur usage dans la fraude, le ransomware, le contournement de sanctions.

Le présent chapitre fournit la **vue maître**. Pour la profondeur (clustering, attribution, mixers, bridges, cashout, IA on-chain, NFTs forensique, DeFi), **renvoi systématique vers OSINT Crypto vFULL**.

## 72.2 Lecture basique d'une transaction

**Bitcoin transaction.**

- TXID : identifiant unique.
- Inputs : adresses émettrices.
- Outputs : adresses destinataires.
- Montant.
- Frais.
- Block timestamp.

**Ethereum / EVM transaction.**

- Hash de transaction.
- From / To.
- Value.
- Gas, fees.
- Contract interaction (DeFi).

**TRON, autres.** Logiques similaires.

## 72.3 Explorateurs publics

**Bitcoin.**

- **Blockstream.info** : standard.
- **Mempool.space** : moderne.
- **Blockchain.com** : populaire.

**Ethereum.**

- **Etherscan.io** : référence.
- **Phalcon, Tenderly** : alternatives techniques.

**TRON.**

- **Tronscan.org**.

**Multi-chain.**

- **DeBank** : portfolio multi-chain.
- **Zerion**.

## 72.4 Clustering : vue maître

Le **clustering** consiste à regrouper plusieurs adresses appartenant probablement au même propriétaire.

**Heuristiques classiques.**

- Co-spending : adresses utilisées comme inputs dans même transaction.
- Change address heuristic.
- Patterns de transactions.

**Outils commerciaux clustering.** Chainalysis, TRM Labs, Elliptic, Crystal Blockchain.

**Outils gratuits.** Limités.

**Pour vue maître :** identifier qu'une adresse semble liée à un exchange / mixer / acteur connu (via base de connaissances publique).

## 72.5 Attribution prudente

**Adresse ≠ personne.**

Une adresse n'est jamais directement liée à une personne physique en source ouverte pure. L'attribution suppose :

- Lien plateforme (KYC d'exchange).
- Lien public (adresse publiée par personne).
- Lien forensique (saisie, perquisition).

**Pour OSINT.**

- Identification de clusters d'adresses.
- Identification de relations avec entités connues (exchanges, mixers).
- **Attribution à une personne reste prudente** sans lien direct.

## 72.6 Sanctions et crypto

**OFAC** sanctionne des adresses crypto spécifiques (Tornado Cash 2022, ChipMixer 2023, etc.).

**Outils.**

- **OFAC SDN crypto addresses list**.
- **Chainalysis Sanctions Screening**.
- **TRM Labs**.

**Travel Rule** (FATF) : impose aux VASPs d'échanger info émetteur/destinataire au-dessus de seuils.

## 72.7 Wallets et exchanges labellisés

**Bases de données labellisation publiques (partielles).**

- **OXT.me** : Bitcoin clustering ouvert.
- **Bitquery, Dune** : data on-chain analytique.
- **Walletexplorer.com** : labellisation Bitcoin partielle.

**Exchanges identifiables.** Adresses Binance, Coinbase, Kraken, etc., souvent identifiées dans bases publiques.

## 72.8 NFTs et tokenisation

**NFTs** : Non-Fungible Tokens. Investigation possible via OpenSea, Etherscan.

**Cas d'usage OSINT.** Lavage d'argent via NFTs, identification de marchés illicites.

## 72.9 DeFi : nouveau terrain

**Decentralized Finance.** Protocoles ouverts (Uniswap, Aave, Compound, etc.).

**OSINT.** Smart contracts publics, transactions tracables, mais complexité technique.

**→ Cours OSINT Crypto vFULL.**

## 72.10 Pivots crypto ↔ OSINT classique

**Pivots possibles.**

- Adresse → ENS (Ethereum Name Service) → username public.
- Adresse → fuite (DeHashed avec wallet) → email lié.
- Adresse → mention publique sur réseaux sociaux → identité.
- Adresse → infrastructure (domain WHOIS d'un projet crypto associé).

## 72.11 Renvoi systématique

Toute investigation crypto au-delà du triage doit être conduite avec la profondeur du **cours OSINT Crypto vFULL**.

## 72.12 Typologie criminelle crypto observable en OSINT

**Catégories majeures (compréhension, pas exploitation).**

**Ransomware et extorsion.** Les rançonneurs (LockBit, BlackCat / ALPHV, Royal, Play, etc.) demandent paiement en Bitcoin ou Monero. Patterns observables : adresses publiées par groupes ransomware sur leur leak site, suivi flux sur Bitcoin (Monero non-traçable par design).

**Marchés darkweb.** Drogues (anciennement Silk Road, Hydra, AlphaBay, et successeurs en émergence-fermeture). Bitcoin et Monero principaux. Cashout via mixers et P2P.

**Fraude au président via crypto.** CEO fraud avec demande conversion paiement en USDT TRC-20 (rapide, peu de frais). Cibles : DAF d'ETI. Pattern : urgence + nouveauté + non-vérification.

**Investment scams (« rug pulls »).** Faux projets DeFi / NFT / memcoins lancés pour collecter ETH/USDT puis disparaître. Volume astronomique 2021-2026.

**Pig butchering.** Arnaque sentimentale longue (semaines/mois) qui mène à investissement crypto fictif. Réseau organisé majoritairement Sud-Est asiatique (Cambodge, Birmanie, Laos).

**Money laundering / mules crypto.** Conversion stealer logs / cartes volées en crypto, puis cashout via P2P, exchanges low-KYC, ou bridges.

**Sanctions evasion.** Russie, Iran, Corée du Nord utilisent crypto pour contourner sanctions occidentales. North Korea (Lazarus Group) particulièrement actif sur DeFi, hacks d'exchanges, ransomware.

**Terrorist financing.** Volume limité mais existant. FATF documente cas.

## 72.13 Mixers, bridges et techniques d'obfuscation

**Mixers (mélangeurs).** Services qui mélangent crypto de plusieurs utilisateurs pour casser le lien on-chain.

- **Tornado Cash** : ETH, sanctionné OFAC août 2022. Toujours utilisé après sanction (smart contracts publics).
- **ChipMixer** : sanctionné 2023.
- **Sinbad** (BTC) : sanctionné 2023, successeur de Blender.io.
- **Wasabi Wallet / Samourai Wallet** : wallets BTC avec CoinJoin.
- **Monero** : par design, anonymat natif.

**Bridges (passerelles cross-chain).** Permettent conversion entre blockchains. Utilisés pour obfuscation.

- **Wormhole, Ronin, Multichain, Across, Stargate, Synapse** : bridges majeurs.
- **Hacks de bridges** : massive perte crypto 2022-2023 (Ronin 600 M$, Wormhole 320 M$, etc.).

**P2P et OTC.** Conversion fiat-crypto sans KYC ou avec KYC faible. LocalBitcoins (fermé 2023), Bisq, plateformes émergentes. Marchés Telegram massifs.

**Privacy coins.** Monero (XMR), Zcash, Dash. Anonymat plus fort que Bitcoin.

**Pour OSINT.** Identifier dans les flux observables passage par mixer / bridge / privacy coin → signal fort de tentative d'obfuscation.

## 72.14 Méthodologie triage OSINT crypto

**Triage en 6 étapes (vue maître, profondeur en cours crypto).**

1. **Pivots vers crypto.** Identifier dans l'enquête classique (Sherlock, breaches, presse) toute mention crypto (adresses, exchanges, projets).
2. **Validation des adresses.** Format correct (Bitcoin commence par 1, 3, bc1 ; Ethereum 0x...). Lookup sur explorateur (Etherscan, Blockstream).
3. **Labellisation.** Recherche labels publics (Walletexplorer.com pour BTC, Etherscan « public tags »).
4. **Volumes et flux.** Quelle activité, vers quels acteurs labellisés ? Exchanges connus ? Mixers connus ?
5. **Sanctions.** Cross-check OFAC SDN crypto addresses list, Chainalysis Sanctions Screening.
6. **Décision escalade.** Si volume / pattern suspects → cours OSINT Crypto vFULL ou cabinet spécialisé (Chainalysis, TRM Labs, Elliptic).

## 72.15 Cas typique de cashout

**Pattern fraudeur typique.**

1. Détournement fonds vers crypto via exchange KYC modéré (Binance, Kraken).
2. Transfert vers wallet personnel.
3. Conversion en stablecoin (USDT TRC-20 souvent, ou USDC).
4. Mixer ou bridge cross-chain pour obfuscation.
5. Reconversion vers wallet « propre ».
6. Cashout via P2P (Binance P2P, Bisq, marketplaces Telegram).
7. Réception fiat sur compte bancaire d'une mule ou directement.

**Pour OSINT.** Les étapes 2-6 sont **partiellement observables** on-chain (avec expertise). Le cashout final (étape 7) demande réquisitions exchanges. L'OSINT identifie le pattern, l'expertise judiciaire conclut.

## 72.16 Lien crypto ↔ identité réelle

Le lien entre adresse crypto et personne physique se construit via :

**Pivots ouverts (OSINT).**

- Adresse publiée par la personne (réseaux sociaux, blog, donation publique).
- ENS (Ethereum Name Service) ou Solana names : `marc.eth` lié à compte X public.
- Mention dans leak (Cyprus Confidential mentionne wallet associé à entité).
- NFT publics liés à compte vérifié.
- Activité sur DeFi avec patterns reliés à activité publique.

**Pivots fermés (judiciaire / institutionnel).**

- KYC d'exchange (réquisition).
- IP loguée par exchange.
- Tracé fiat → crypto sur compte bancaire identifié.

**Pour OSINT.** Lien public requiert corroboration multi-sources, cotation prudente (rarement A1). Conclusion typique : « adresse probablement associée à... niveau de confiance modéré, à confirmer judiciairement ».

> **MIRAGE — Épisode 14 : Piste crypto, renvoi OSINT Crypto**
>
> L'investigation a identifié un compte Binance personnel utilisé par Delaunay (MIRAGE 10, via stealer logs). L'email Binance étant `marc.delaunay76@gmail.com`, plusieurs pivots OSINT crypto se présentent.
>
> **Triage en surface (master OSINT).**
> - Recherche d'adresses publiques liées à `marc.delaunay76@gmail.com` ou aux usernames associés : aucun lien direct identifié sur les bases publiques (Etherscan, Walletexplorer.com).
> - Vérification sanctions : email non lié à entité OFAC.
> - L'email est dans stealer logs avec compte Binance, mais sans adresse publique exposée.
>
> **Limite du triage.** L'analyse on-chain réelle (clustering, identification d'adresses Binance retrait, attribution probable) demande l'expertise du cours OSINT Crypto vFULL.
>
> **Recommandation rapport MIRAGE.** Mentionner :
> - Existence d'un compte Binance personnel de Delaunay (cotation B2 via stealer logs).
> - Hypothèse : retraits Binance vers wallet personnel → cashout en stablecoins TRC-20 ou via P2P (pattern courant).
> - **Recommandation expertise crypto forensique** dans le cadre judiciaire pour analyse on-chain approfondie. Le PNF peut mandater cabinet spécialisé pour clustering Chainalysis-grade.
>
> Ce niveau de triage est suffisant pour MIRAGE comme rapport OSINT orienteur. La profondeur attend la procédure judiciaire avec expertise dédiée.

-----
