---
title: Annexe A — Glossaire opérationnel crypto
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Annexes
  - index.md
---

**Adresse**. Identifiant cryptographique (chaîne de caractères) d’un point de réception sur une blockchain. Bitcoin : 26-62 caractères selon format. Ethereum : 42 caractères commençant par `0x`. TRON : 34 caractères commençant par `T`.

**ABI (Application Binary Interface)**. Spécification d’interaction avec un smart contract (signatures de fonctions, types). Etherscan affiche l’ABI des contrats vérifiés.

**Affilié RaaS**. Acteur qui exécute des attaques utilisant le malware d’un opérateur RaaS. Garde typiquement 70-80% des rançons.

**AMM (Automated Market Maker)**. Mécanisme DEX basé sur pools de liquidité avec formule mathématique de prix. Uniswap, Curve, etc.

**AML (Anti-Money Laundering)**. Cadre réglementaire de lutte contre le blanchiment.

**Anonymity set**. Nombre d’utilisateurs « indistinguables » dans un mécanisme d’anonymisation. Plus l’anonymity set est grand, plus l’anonymat est fort.

**Approve / Allowance**. Permission accordée à un smart contract de dépenser des tokens de l’utilisateur. Mécanisme central des DEX et lending protocols. Détourné par drainers (cf Ch.9).

**Bitcoin Core**. Implémentation de référence du protocole Bitcoin.

**BIP (Bitcoin Improvement Proposal)**. Standard d’évolution Bitcoin. BIP-21 (URI), BIP-32 (HD wallets), BIP-39 (mnemonic seed phrases), BIP-141 (SegWit), etc.

**Block**. Groupe de transactions agrégées et validées ensemble. Identifié par numéro (block height) et hash.

**Block height**. Numéro séquentiel d’un bloc dans la blockchain.

**Bootstrap**. Démarrage d’un wallet par téléchargement et synchronisation de la blockchain.

**Bridge**. Protocole permettant transferts d’actifs entre blockchains. Wormhole, Stargate, etc.

**BSC / BNB Chain**. Chaîne de Binance, EVM-compatible.

**Burn**. Destruction de tokens en les envoyant à une adresse non-récupérable (souvent `0x0`).

**CEX (Centralized Exchange)**. Exchange centralisé. Binance, Coinbase, Kraken, etc.

**Chain of custody**. Documentation traçant la possession et l’intégrité de preuves.

**Chainalysis**. Vendor de blockchain intelligence (Reactor, KYT). Référence industrie.

**Cluster**. Ensemble d’adresses regroupées comme contrôlées probablement par une même entité.

**Cold storage**. Wallet hors ligne (matériel, paper). Plus sécurisé. Réserves.

**CoinJoin**. Technique de mélange Bitcoin coopérative non-custodial. Wasabi, Samourai.

**Confirmations**. Nombre de blocs ajoutés depuis qu’une transaction a été incluse.

**Custodial / Non-custodial**. Custodial = un tiers détient les clés privées (exchange). Non-custodial = utilisateur les contrôle.

**dApp (decentralized application)**. Application décentralisée sur blockchain.

**DEX (Decentralized Exchange)**. Exchange décentralisé. Uniswap, PancakeSwap, etc.

**DeFi (Decentralized Finance)**. Écosystème d’applications financières sur blockchain.

**Drainer**. Smart contract / script malveillant vidant un wallet via approval phishing.

**ECDSA (Elliptic Curve Digital Signature Algorithm)**. Algorithme cryptographique de Bitcoin et Ethereum.

**EOA (Externally Owned Account)**. Compte Ethereum contrôlé par clé privée (wallet utilisateur). Vs smart contract.

**ERC-20**. Standard tokens fongibles Ethereum.

**ERC-721**. Standard NFT Ethereum.

**ERC-1155**. Standard hybride fongible/non-fongible Ethereum.

**EVM (Ethereum Virtual Machine)**. Machine virtuelle Ethereum. Compatibles : BNB, Polygon, Avalanche, etc.

**Exchange**. Plateforme d’échange crypto. Centralized (CEX) ou Decentralized (DEX).

**Fee / Frais**. Coût de transaction. Bitcoin : satoshis/byte. Ethereum : gas × gas price.

**Fork**. Divergence d’une blockchain. Bitcoin Cash est fork de Bitcoin.

**Gas**. Unité de compute Ethereum. Coût d’une transaction = gas used × gas price.

**Gwei**. Unité de gas price. 1 gwei = 10^-9 ETH.

**Hash**. Empreinte cryptographique. SHA-256 pour Bitcoin, Keccak-256 pour Ethereum.

**HD Wallet (Hierarchical Deterministic)**. Wallet générant adresses depuis seed unique (BIP-32).

**Hot wallet**. Wallet en ligne. Pratique pour usage. Moins sécurisé que cold.

**Honeypot**. Token codé pour empêcher acheteurs de revendre. Scam.

**IBC (Inter-Blockchain Communication)**. Protocole cross-chain Cosmos.

**KYC (Know Your Customer)**. Procédure d’identification client par VASP.

**KYT (Know Your Transaction)**. Solution Chainalysis de monitoring AML temps réel.

**Layer-1**. Blockchain de base. Bitcoin, Ethereum.

**Layer-2**. Blockchain déployée sur Layer-1 pour scaling. Lightning Network, Arbitrum, Optimism, Base.

**Lightning Network**. Layer-2 Bitcoin pour micro-paiements.

**Liquidity pool**. Pool de tokens dans un DEX permettant swaps.

**Mempool**. File d’attente des transactions pending non encore incluses dans un bloc.

**Mining / Stacking**. Mécanismes de validation. Bitcoin = PoW (mining). Ethereum post-Merge = PoS (staking).

**Mixer / Tumbler**. Service mélangeant fonds de multiples utilisateurs pour casser traçabilité.

**Mnemonic**. Suite de mots permettant reconstitution d’un wallet. BIP-39.

**Multi-sig**. Adresse nécessitant signatures multiples (M-of-N).

**NFT**. Non-Fungible Token. Token unique non-divisible.

**Nonce**. Compteur séquentiel des transactions d’une adresse Ethereum.

**OFAC**. Office of Foreign Assets Control, US Treasury. Sanctions list.

**Off-chain**. Tout ce qui se passe hors blockchain (KYC, communications, etc.).

**On-chain**. Transactions et états enregistrés sur blockchain.

**Off-ramp**. Conversion crypto → fiat (sortie).

**On-ramp**. Conversion fiat → crypto (entrée).

**OP_RETURN**. Output Bitcoin permettant inclusion de données arbitraires (limités).

**OPSEC (Operational Security)**. Discipline de protection des opérations.

**Oracle**. Service fournissant données externes à un smart contract (prix, événements).

**OTC (Over-The-Counter)**. Trading hors orderbook public.

**P2P (Peer-to-Peer)**. Échange direct entre particuliers.

**P2PKH, P2SH, P2WPKH (SegWit), P2TR (Taproot)**. Types d’adresses Bitcoin.

**Peeling chain**. Pattern de blanchiment Bitcoin où une grosse somme est progressivement épluchée.

**Pig butchering**. Type de fraude combinant manipulation sentimentale et faux investissement crypto.

**PoS / PoW (Proof of Stake / Work)**. Mécanismes de consensus.

**Privacy coin**. Cryptomonnaie conçue pour anonymat. Monero, Zcash.

**Private key**. Clé privée. Permet de signer transactions. Connaissance = contrôle des fonds.

**Public key**. Clé publique. Dérivée de la privée. Adresse dérivée de la publique.

**RaaS (Ransomware-as-a-Service)**. Modèle où opérateurs vendent malware à affiliés.

**Ring signature**. Mécanisme cryptographique Monero pour anonymiser émetteurs.

**Rug pull**. Scam où créateurs de token vident la liquidité.

**Saisie**. Action légale de prise de contrôle d’actifs par autorité.

**Satoshi (sat)**. Plus petite unité Bitcoin. 1 BTC = 100 000 000 sats.

**SDN (Specially Designated Nationals)**. Liste OFAC de personnes/entités sanctionnées.

**Seed phrase**. Mnemonic. Suite de 12-24 mots reconstituant wallet.

**SegWit**. Segregated Witness. Évolution Bitcoin permettant plus de transactions par bloc.

**Smart contract**. Programme déployé sur blockchain, exécuté quand conditions remplies.

**SPL (Solana Program Library)**. Tokens standard Solana.

**Stablecoin**. Crypto stable adossée à valeur de référence. USDT, USDC.

**Stealth address**. Adresse one-time Monero pour masquer destinataire.

**SWIFT**. Système international de paiement bancaire (mention pour comparaison).

**Taint**. Concept de « contamination » d’un fonds par origine illicite. Variable selon juridiction.

**Token**. Actif déployé sur blockchain via smart contract.

**Tor**. Réseau d’anonymisation web (cf cours Dark Web).

**Tornado Cash**. Mixer décentralisé Ethereum sanctionné OFAC août 2022.

**TRACFIN**. Cellule française de renseignement financier.

**Travel Rule**. Recommandation FATF étendue aux VASP.

**TRM Labs**. Vendor blockchain intelligence (concurrent Chainalysis).

**TXID**. Transaction Hash. Identifiant unique d’une transaction.

**UTXO (Unspent Transaction Output)**. Modèle Bitcoin de comptabilité par « pièces » non dépensées.

**VASP (Virtual Asset Service Provider)**. Terme FATF pour services manipulant actifs virtuels.

**Wallet**. Logiciel/matériel stockant clés et signant transactions.

**Watchlist**. Liste d’adresses surveillées pour alertes.

**WEP (Words of Estimative Probability)**. Vocabulaire calibré de niveau de confiance.

**WORM (Write Once Read Many)**. Stockage immutable.

**Zero-knowledge proof / zk-SNARK**. Preuve cryptographique sans révélation. Tornado Cash, Zcash shielded.

-----
