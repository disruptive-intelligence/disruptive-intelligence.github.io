---
title: Chapitre 3 — Lexique opérationnel des crypto-actifs
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie I — Comprendre l’écosystème crypto sans fantasme
  - index.md
---

Maîtriser le vocabulaire est la condition pour comprendre le reste du cours, mais aussi pour **communiquer crédiblement** avec ses interlocuteurs (autres analystes, autorités, exchanges, journalistes). Ce chapitre n’est pas un glossaire encyclopédique mais un panorama opérationnel des termes que l’analyste manipule quotidiennement.

## 3.1 Termes fondamentaux

**Blockchain**. Registre distribué de transactions, validé cryptographiquement, partagé entre les nœuds d’un réseau. Bitcoin (depuis 2009), Ethereum (depuis 2015), TRON (depuis 2018), Solana (depuis 2020), des centaines d’autres. Chaque blockchain a ses règles propres (consensus, structure de transaction, capacités de smart contracts).

**Wallet**. Logiciel ou matériel qui stocke les clés privées et permet de signer des transactions. Distinction importante :

- **Wallet logiciel** : application sur ordinateur ou mobile (MetaMask, Phantom, Trust Wallet, Electrum).
- **Wallet matériel** : appareil dédié hors ligne (Ledger, Trezor) — plus sécurisé.
- **Wallet custodial** : géré par un tiers (exchange) qui détient les clés à votre place — Binance, Coinbase. **Vous ne contrôlez pas vraiment** les fonds.
- **Wallet non-custodial** : vous détenez les clés. « Not your keys, not your coins ».

**Adresse**. Identifiant public d’un point de réception sur une blockchain. Dérivée cryptographiquement d’une clé publique elle-même dérivée d’une clé privée. Voir Ch.3.4 pour les formats.

**Clé privée**. Secret cryptographique permettant de signer des transactions depuis une adresse. Connaissance de la clé privée = contrôle de l’adresse. Si une clé privée est compromise, les fonds peuvent être volés.

**Seed phrase / Mnemonic**. Suite de 12 ou 24 mots permettant de reconstituer une clé privée. Format standardisé (BIP-39). **Si quelqu’un obtient votre seed phrase, il prend le contrôle de tous les wallets qu’elle génère**. Utilisée pour récupération.

**Transaction (TX)**. Transfert d’actif entre adresses, signé cryptographiquement, propagé sur la blockchain.

**Transaction hash (TXID)**. Identifiant unique d’une transaction. Référence pour citer ou rechercher une transaction.

**Bloc**. Groupe de transactions agrégées et validées ensemble. Identifié par un numéro (block height) et un hash.

**Confirmations**. Nombre de blocs ajoutés depuis qu’une transaction a été incluse. Plus de confirmations = plus de finalité. Bitcoin : 6 confirmations standard (~1h). Ethereum post-Merge : finalité après ~12-15 minutes.

## 3.2 Termes économiques

**Coin natif**. L’actif intrinsèque d’une blockchain. BTC sur Bitcoin, ETH sur Ethereum, TRX sur TRON, SOL sur Solana, BNB sur BNB Chain.

**Token**. Actif déployé sur une blockchain via un smart contract (sans avoir sa propre blockchain). USDT, USDC, des dizaines de milliers d’autres. Distinction des standards :

- **ERC-20** sur Ethereum (et chaînes EVM-compatibles).
- **TRC-20** sur TRON.
- **BEP-20** sur BNB Chain.
- **SPL** sur Solana.

**Stablecoin**. Token dont la valeur est arrimée à une référence stable (généralement USD). USDT (Tether), USDC (Circle), DAI (MakerDAO). Détaillé Ch.10.

**NFT (Non-Fungible Token)**. Token unique non-divisible (contrairement aux fungibles type USDT). ERC-721 standard sur Ethereum. Représente collectibles, art numérique, droits, etc.

**Gas**. Frais de transaction sur Ethereum (et chaînes EVM). Mesuré en gwei (10^-9 ETH). Plus le réseau est congestionné, plus le gas coûte cher.

**Mining / Staking**. Mécanismes de validation des blocs. Bitcoin utilise Proof-of-Work (mining). Ethereum a basculé en Proof-of-Stake en septembre 2022 (The Merge). Implications pour l’analyste : peu directes, mais impact sur certaines heuristiques.

## 3.3 Termes d’enquête

**UTXO (Unspent Transaction Output)**. Modèle Bitcoin (et clones) où chaque transaction consomme des « pièces » (outputs précédents) et en génère de nouvelles. Détaillé Ch.7.

**Account model**. Modèle Ethereum (et chaînes EVM) où les adresses ont un solde directement (pas d’UTXO). Plus simple en surface, complexité différente en profondeur. Détaillé Ch.8.

**Clustering**. Regroupement d’adresses appartenant probablement à la même entité, basé sur des heuristiques (co-spending, change detection, etc.). Détaillé Ch.17.

**Attribution**. Association d’une adresse ou d’un cluster à une entité identifiable (exchange, mixer, individu, organisation). Niveaux de confiance variables. Détaillé Ch.18.

**Label**. Étiquette publique ou propriétaire associée à une adresse. Sources : annonces officielles, recherche communautaire, vendor commerciaux. Détaillé Ch.22.

**Heuristique**. Règle d’inférence non garantie, utilisée pour faire des hypothèses. Exemple : « si plusieurs inputs sont co-dépensés dans une même transaction, ils appartiennent probablement à la même entité ».

**Peeling chain**. Technique d’obfuscation Bitcoin où une grosse somme est progressivement « épluchée » en transferts successifs, chaque transaction laissant un petit montant à un destinataire et le reste à une nouvelle adresse de change. Détaillé Ch.7.

**Cluster**. Ensemble d’adresses regroupées comme appartenant probablement à la même entité.

**Cashout / Off-ramp**. Conversion de crypto en monnaie utilisable (fiat, biens, services). Le moment où l’on **quitte la blockchain**. Point critique d’enquête. Détaillé Ch.30.

## 3.4 Termes liés aux services

**CEX (Centralized Exchange)**. Plateforme d’échange centralisée. Binance, Coinbase, Kraken, OKX, Bybit, Bitstamp, Bitfinex. Détient les fonds des utilisateurs (custodial). Soumis à KYC dans les juridictions régulées.

**DEX (Decentralized Exchange)**. Plateforme d’échange décentralisée, sur smart contracts. Uniswap, PancakeSwap, Curve, dYdX. Pas de KYC (en principe), pas de custodian. L’utilisateur conserve ses clés.

**VASP (Virtual Asset Service Provider)**. Terme FATF désignant tout service qui manipule des actifs virtuels (exchanges, custodians, wallet providers, parfois DEX selon interprétation). Soumis à la Travel Rule.

**Bridge**. Pont permettant le transfert d’actifs entre blockchains. Wormhole, Multichain (compromis 2023), Stargate, etc. Souvent ciblé par hacks (cf Ronin, Ch.43). Détaillé Ch.33.

**Mixer / Tumbler**. Service mélangeant les fonds de plusieurs utilisateurs pour casser la traçabilité. Tornado Cash (sanctionné 2022), Helix (saisi 2020), Bitcoin Fog (saisi 2021), Chipmixer (saisi 2023), Samourai (saisi 2024). Détaillé Ch.31.

**CoinJoin**. Technique de mélange Bitcoin coopérative (sans custodian central). Wasabi, Samourai. Détaillé Ch.32.

**Privacy coin**. Cryptomonnaie conçue pour anonymat. Monero, Zcash, Dash. Détaillé Ch.35.

**Smart contract**. Programme déployé sur une blockchain, exécuté quand des conditions sont remplies. Ethereum est la blockchain pionnière. Détaillé Ch.9.

**DeFi (Decentralized Finance)**. Écosystème d’applications financières sur blockchain (DEX, lending, yield farming, dérivés). Détaillé Ch.34.

## 3.5 Termes liés à la conformité et la réglementation

**KYC (Know Your Customer)**. Procédure d’identification des clients par les VASP. Exigée par MiCA et la plupart des juridictions sérieuses.

**AML (Anti-Money Laundering) / CFT (Counter-Financing of Terrorism)**. Cadre réglementaire de lutte contre le blanchiment et le financement du terrorisme.

**Travel Rule**. Recommandation FATF étendue aux VASP : pour transferts au-delà d’un certain seuil (1 000 USD/EUR), l’expéditeur doit transmettre des informations sur l’expéditeur et le destinataire au VASP destinataire.

**MiCA (Markets in Crypto-Assets)**. Règlement UE 2023/1114, entré en vigueur progressivement à partir de 2024. Cadre réglementaire crypto unifié pour l’UE.

**Sanctions OFAC**. Sanctions américaines ciblant entités, individus, et désormais adresses crypto. Tornado Cash (août 2022), Garantex, Suex, Bitzlato, multiples wallets Lazarus.

**TRACFIN**. Cellule française de renseignement financier. Reçoit les déclarations de soupçon des assujettis (banques, VASP). Cadre français de lutte AML/CFT.

**SAR (Suspicious Activity Report)**. Déclaration de soupçon (équivalent international du signalement TRACFIN).

## 3.6 Termes spécifiques d’enquête

**Drainer**. Smart contract ou script malveillant qui vide automatiquement un wallet une fois que la victime signe une transaction d’approval. Vecteur de phishing crypto majeur 2022-2026.

**Approval**. Permission accordée à un smart contract de dépenser certains tokens. Mécanisme légitime (DEX, lending) mais détourné par phishing.

**Rug pull**. Arnaque où les créateurs d’un projet crypto disparaissent avec les fonds des investisseurs. Variante : honeypot token (impossible à revendre).

**Pig butchering** (« 杀猪盘 », shā zhū pán). Type de fraude combinant manipulation sentimentale (romance scam) et faux investissement crypto. Volumes massifs depuis 2022. Ch.25 détaillé.

**Pump-and-dump**. Manipulation coordonnée du cours d’un token : achats coordonnés (pump) suivis d’une revente massive (dump) qui plante le cours.

**Wash trading**. Fausses transactions entre wallets contrôlés par la même entité, pour simuler du volume.

**Dust attack**. Envoi de petits montants vers de nombreuses adresses pour tenter de les corréler par heuristiques de co-spending si elles « consolident » la poussière.

-----
