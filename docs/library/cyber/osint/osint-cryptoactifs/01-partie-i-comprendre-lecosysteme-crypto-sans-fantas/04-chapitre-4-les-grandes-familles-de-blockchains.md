---
title: Chapitre 4 — Les grandes familles de blockchains
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie I — Comprendre l’écosystème crypto sans fantasme
  - index.md
---

Toutes les blockchains ne sont pas équivalentes. Pour l’analyste, comprendre les différences structurelles entre familles est essentiel — elles déterminent les méthodes d’enquête applicables, les outils utilisables, et les patterns à observer.

## 4.1 Bitcoin et le modèle UTXO

**Bitcoin** (lancé 2009). Première blockchain. Modèle **UTXO** (Unspent Transaction Output). Pas de smart contracts (au sens Ethereum) — Bitcoin est volontairement minimaliste.

**Caractéristiques pour l’enquête** :

- **Très grande lisibilité** : chaque transaction est un graphe d’inputs et outputs.
- **Heuristiques de clustering matures** (co-spend, change detection, peeling).
- **Outils nombreux** : Mempool.space, Blockstream.info, OXT, Breadcrumbs, Chainalysis, etc.
- **Communauté de recherche active** depuis 15+ ans.

**Usages illicites observés** : ransomware (BTC reste dominant pour les rançons selon Chainalysis 2024-2025), darknet markets (BTC + Monero), saisies historiques (Silk Road, AlphaBay, Bitfinex, Colonial Pipeline). En **baisse relative** vs stablecoins pour les autres typologies.

**Forks et clones notables** : Bitcoin Cash (BCH), Bitcoin SV (BSV), Litecoin (LTC), Dogecoin (DOGE). Mêmes principes d’analyse. Volumes illicites significativement moindres.

## 4.2 Ethereum et chaînes EVM

**Ethereum** (lancé 2015). Modèle **account-based** (pas UTXO). Introduction des **smart contracts** programmables. Dominance dans DeFi, NFT, DAO, et multiples couches d’application.

**Caractéristiques pour l’enquête** :

- **Lisibilité bonne mais différente** : transactions plus simples (un emetteur, un destinataire, un montant), mais complexité dans les **internal transactions** (appels entre smart contracts) et **logs d’événements**.
- **Outil dominant** : Etherscan.
- **Tokens omniprésents** : transferts ETH directs souvent moins importants que les transferts de tokens (USDT, USDC, autres).

**EVM (Ethereum Virtual Machine) compatibles** : BNB Chain, Polygon, Avalanche, Arbitrum, Optimism, Fantom, Base. **Mêmes principes d’enquête**, mêmes adresses (compatibles 0x…), mêmes outils dérivés (BscScan, PolygonScan, etc.). L’analyste qui maîtrise Ethereum peut travailler sur ces chaînes avec courbe d’apprentissage faible.

**Usages illicites** : DeFi exploits, rug pulls, NFT scams, drainers de wallets, certains flux ransomware (en hausse). Moins dominante que Bitcoin pour ransomware, mais centrale pour fraudes retail et acteurs étatiques (Lazarus utilise massivement Ethereum + Tornado Cash).

## 4.3 TRON

**TRON** (lancé 2018, fondateur Justin Sun). Blockchain à modèle compte, transactions très bon marché (~quelques centimes USD), confirmation rapide (~3 secondes).

**Caractéristiques structurantes pour l’enquête** :

- **USDT-TRON est dominant** : la blockchain TRON est devenue **la plate-forme principale** pour les flux USDT, légitimes et illicites. Source : observations Chainalysis, TRM Labs, Elliptic 2024-2026.
- **Frais minimes** : un transfert USDT-TRON coûte ~1 centime, contre ~5-30 USD sur Ethereum (selon congestion). Cette économie attire les flux à haute fréquence, dont le pig butchering et certaines opérations de blanchiment.
- **Confirmation rapide** : en 3 secondes, une transaction est finalisée. Pratique pour les criminels qui veulent disperser rapidement.
- **Outil principal** : Tronscan.

**Usages illicites observés** : pig butchering massif (volumes en milliards USD selon estimations), certaines fraudes ransomware (en hausse), opérations Lazarus, blanchiment et placement.

**Critique** : l’écosystème TRON est moins coopératif sur la régulation que d’autres. La fondation TRON est controversée. Plusieurs procédures aux US visent Justin Sun et entités liées.

**Pour l’analyste** : TRON ne peut **pas être ignoré**. Une part majeure des flux illicites stablecoin y transite. Maîtriser Tronscan et les heuristiques TRON est aussi important que maîtriser Etherscan.

## 4.4 Solana

**Solana** (lancé 2020). Architecture différente, très haute performance (théorique 65 000 TPS), confirmation quasi-instantanée, frais infimes.

**Caractéristiques pour l’enquête** :

- **Modèle compte** différent d’Ethereum (account model spécifique Solana).
- **Tokens SPL** (Solana Program Library) — équivalent ERC-20.
- **Outil** : Solscan, Solana Explorer.
- **Volumes croissants** : DeFi Solana, NFT Solana, memecoins (pump.fun et écosystème associé 2024-2025).

**Usages illicites observés** : memecoin scams massifs (rug pulls quasi-industriels via pump.fun), certaines fraudes retail. En forte croissance.

**Pour l’analyste** : Solana est **moins mature** dans l’outillage forensique que Bitcoin/Ethereum. Les outils commerciaux (Chainalysis, TRM, Elliptic) couvrent Solana mais avec moins de profondeur historique. Les heuristiques de clustering sont moins éprouvées.

## 4.5 Autres chaînes pertinentes

**BNB Chain (ex-Binance Smart Chain)**. EVM-compatible. Volumes massifs, particulièrement DeFi et memecoins. Outil : BscScan.

**Polygon**. Layer-2 Ethereum. EVM-compatible. Croissance.

**Avalanche**. EVM-compatible. Subnets. Croissance modérée.

**Arbitrum, Optimism, Base**. Layer-2 Ethereum (rollups). EVM-compatibles. Forte croissance 2023-2026.

**Cosmos écosystème** (Cosmos Hub, Osmosis, etc.). Différent d’Ethereum, IBC pour cross-chain. Outils moins matures.

**XRP Ledger (Ripple)**. Modèle différent. Usage majoritaire institutionnel.

**Stellar**. Similaire dans la philosophie à XRP.

## 4.6 Privacy coins

**Monero (XMR)** (lancé 2014). Anonymat par construction. Ring signatures, RingCT, stealth addresses. Détaillé Ch.35.

**Zcash (ZEC)** (lancé 2016). Optionnellement anonymisable (transparent par défaut, shielded en option). Une fraction des transactions est shielded.

**Dash** (lancé 2014). Anonymisation via PrivateSend (CoinJoin amélioré). Moins efficace que Monero, plus simple à analyser.

**Pour l’analyste** : Monero est **largement opaque**. Zcash transparent est lisible. Zcash shielded est opaque (mais peu utilisé en pratique). Dash est analysable avec effort.

## 4.7 Implications opérationnelles

**Pour Bitcoin**, l’analyste a besoin :

- Maîtrise du modèle UTXO.
- Heuristiques de clustering (co-spend, change).
- Outils : Mempool.space, OXT, Chainalysis.

**Pour Ethereum et EVM-chains**, l’analyste a besoin :

- Compréhension du model account.
- Lecture de smart contracts et events.
- Outils : Etherscan + équivalents par chaîne.

**Pour TRON**, l’analyste a besoin :

- Maîtrise de Tronscan.
- Spécificités USDT-TRON.
- Patterns pig butchering et blanchiment.

**Pour Solana**, l’analyste a besoin :

- Solscan.
- Spécificités SPL tokens.
- Conscience des limites d’outillage forensique.

**Pour Monero**, l’analyste se prépare à :

- Utiliser les **points off-chain** (exchanges, KYC, OPSEC errors).
- Documenter la rupture de visibilité.

Une enquête moderne touche **fréquemment plusieurs chaînes**. L’analyste polyvalent est l’analyste utile.

-----
