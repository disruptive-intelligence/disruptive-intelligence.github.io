---
title: Chapitre 43 — Ronin / Lazarus 2022 — 625 M USD
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VIII — Cas historiques emblématiques
  - index.md
---

Le hack du **Ronin Network** est le plus gros vol crypto à ce jour. Attribué à **Lazarus** (DPRK) par FBI et Chainalysis. Cas emblématique de l’intersection entre vulnérabilité technique et acteur étatique sophistiqué.

## 43.1 Le hack — mars 2022

**Ronin Network** : sidechain Ethereum développée par Sky Mavis pour le jeu Axie Infinity. Bridge Ronin permet transferts entre Ronin et Ethereum.

**Architecture du bridge** : 9 validators, 5 signatures requises pour autoriser un retrait. 4 contrôlés par Sky Mavis directement, 1 par Axie DAO (qui avait délégué ses signatures à Sky Mavis temporairement).

**Vecteur d’attaque** :

- Compromission de **5 des 9 clés validator** par phishing (« Operation Dream Job », fake job offer LinkedIn).
- Une fois 5 clés compromis (4 Sky Mavis + 1 Axie DAO délégué), attaquant atteint le seuil de signatures.

**L’attaque — 23 mars 2022** :

- Signature de transactions de retrait massives.
- **173 600 ETH** (~600 M USD) + **25,5 M USDC** (~25 M USD) drainés.
- **Total : ~625 M USD** au cours du moment.

**Découverte** : 6 jours après (29 mars 2022) — délai signaling failures de monitoring.

## 43.2 L’attribution

**14 avril 2022** : OFAC sanctionne adresses Lazarus liées au hack.

**Attribution** :

- FBI confirme attribution Lazarus / DPRK.
- Chainalysis confirme dans ses rapports.
- Patterns d’attaque cohérents avec opérations Lazarus (vecteur LinkedIn, techniques utilisées, infrastructure).

**Pourquoi attribution forte** :

- Patterns infra (C2 servers liés à autres opérations Lazarus).
- Vecteurs sociaux (Operation Dream Job documenté pour multiple opérations Lazarus).
- Behavioral post-hack (utilisation Tornado Cash, bridges, patterns de blanchiment cohérents).

## 43.3 Le blanchiment

**Méthode Lazarus post-hack** :

**Étape 1 — Conversion**. ETH et USDC convertis. USDC partiellement gelé par Circle (Circle a gelé ~250k USDC sur réquisition).

**Étape 2 — Tornado Cash**. Massive utilisation. ~25-30k ETH déposés à Tornado Cash dans les semaines post-hack. Volume tel que ils représentaient une fraction substantielle des dépôts Tornado.

**Étape 3 — Bridges**. Une partie passe via bridges vers Bitcoin (Ren BTC ou autre).

**Étape 4 — Mixing Bitcoin**. Sur Bitcoin, CoinJoin (Wasabi, Samourai), peeling chains.

**Étape 5 — Off-ramp**. Exchanges régionaux (Asie), OTC desks, P2P. Beaucoup en juridictions peu coopératives.

## 43.4 Récupération

**Récupération partielle documentée** :

- **Circle gel** : ~250k USDC.
- **Saisies multiples** : autorités US et Sky Mavis ont récupéré plusieurs millions USD via différents incidents.
- Total récupéré : **estimé ~30-40 M USD** sur 625 (5-6%).

**Sky Mavis** : a remboursé les utilisateurs via levée de fonds (350 M USD, dirigée par Binance), pas par récupération hack.

## 43.5 Méthodes mobilisées

**Attribution rapide** :

- OFAC dans les semaines suivant.
- Chainalysis / TRM / FBI publications.

**Sanctions** :

- Adresses Lazarus sanctionnées.
- Tornado Cash sanctionné en partie pour cette opération (août 2022).

**Coopération exchanges** :

- Multiple exchanges gelent des fonds Lazarus identifiés.
- Difficulté : Lazarus utilise exchanges non-coopératifs.

**Pression politique** :

- US, Corée du Sud, Japon, UE coordonnent sanctions DPRK élargies post-Ronin.

## 43.6 Leçons

**Pour acteurs DeFi / bridges** :

- **Sécurité validators** = critique. 5/9 c’était insuffisant. Multi-sig schemes doivent assumer compromise.
- **Monitoring real-time** des bridges essentiel.
- **Audit de gouvernance** : la délégation de signatures Axie DAO à Sky Mavis (de fait centralisation) était une faille.

**Pour enquêteurs** :

- **Attribution étatique** rapide possible avec ressources adéquates.
- **Récupération massive impossible** quand acteur étatique : Lazarus utilise tout l’arsenal d’obfuscation, opère depuis juridiction non-coopérative.
- **Sanctions et pressions** sont les outils principaux.

**Pour CTI / OSINT** :

- **Documentation des wallets Lazarus** alimentation continue.
- **Tracking long terme** parfois fournit des opportunités (saisies opportunistes des années plus tard).

## 43.7 Suite

Lazarus continue à opérer. Hacks majeurs subséquents attribués (Atomic Wallet, CoinEx, Stake.com, autres). **Plusieurs milliards USD/an** estimés volés par Lazarus selon Chainalysis. L’écosystème reste vulnérable à des acteurs ressourcés.

-----
