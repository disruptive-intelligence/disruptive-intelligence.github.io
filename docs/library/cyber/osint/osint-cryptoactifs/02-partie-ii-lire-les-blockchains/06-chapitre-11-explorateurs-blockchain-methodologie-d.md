---
title: 'Chapitre 11 — Explorateurs blockchain : méthodologie de lecture'
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie II — Lire les blockchains
  - index.md
---

L’analyste qui passe ses journées dans des explorateurs doit en maîtriser la lecture. Ce chapitre couvre les principaux explorateurs, leurs spécificités, et la méthodologie pour les utiliser efficacement.

## 11.1 Les explorateurs Bitcoin

**Mempool.space** :

- Open source, moderne, performant.
- Excellente UX pour navigation transaction/adresse/bloc.
- Visualisations mempool en temps réel.
- API gratuite généreuse.
- Communauté active.
- **Recommandé** pour usage quotidien et vérification.

**Blockstream.info (Esplora)** :

- Blockstream, open source aussi.
- Solide, classique.
- Bon pour intégration via API.

**Blockchain.com Explorer** :

- Historique, large utilisation.
- Interface vieillissante.
- Toujours fonctionnel.

**BTC.com Explorer** :

- Géré par Bitmain.
- Statistiques mining riches.

**OXT.me** :

- Spécialisé analyses Bitcoin avancées.
- Excellent pour peeling chains et clusters.

**Blockchair.com** :

- Multi-chain (BTC, ETH, autres).
- Recherche cross-chain pratique.

**Pour l’analyste** : Mempool.space en premier choix, OXT pour analyses avancées, autres en validation croisée.

## 11.2 Les explorateurs Ethereum

**Etherscan.io** :

- **Référence absolue**.
- UX éprouvée.
- Décodage automatique des smart contracts vérifiés.
- Labels riches (exchanges, contracts, sanctions OFAC).
- API gratuite (avec limites) + tier payant.
- Indispensable.

**Beaconcha.in** :

- Couvre la beacon chain (consensus) Ethereum post-Merge.
- Utile pour analyser staking, validators.

**Phalcon.xyz (BlockSec)** :

- Analyse forensique avancée.
- Excellent pour transactions complexes (DeFi, exploits).
- Visualisation des appels internes.

**Tenderly.co** :

- Plateforme dev, mais utile pour analyse.
- Simulation de transactions, debugging.

**Bloxy.info** :

- Analytics et reporting.
- Recherche avancée.

## 11.3 Les autres explorateurs

**Tronscan.org** : référence TRON. Couvre transactions, USDT-TRON, smart contracts TRON.

**Solscan.io** : référence Solana. Tokens SPL, NFT Solana.

**BscScan.com** : BNB Chain. Clone d’Etherscan (même équipe).

**PolygonScan.com** : Polygon. Clone Etherscan.

**Arbiscan.io, Optimistic.etherscan.io, Basescan.org** : Layer-2 Ethereum. Clones Etherscan.

**Snowtrace.io** : Avalanche.

**FtmScan.com** : Fantom.

**Multiversx Explorer (anciennement Elrond)** : MultiversX.

**Cosmos / Mintscan.io** : Cosmos écosystème.

**XRPSCAN, Bithomp** : XRP Ledger.

**Pour l’analyste polyvalent** : maîtriser au minimum Etherscan + Tronscan + Mempool. Étendre selon les chaînes rencontrées dans les enquêtes.

## 11.4 Méthodologie de lecture

**Phase 1 — Validation initiale**.

- Vérifier que le TXID/adresse existe bien (mauvaise saisie, typo, mauvaise chaîne).
- Vérifier la chaîne — beaucoup d’erreurs viennent de chercher un transaction ETH sur Etherscan alors qu’elle est sur BNB Chain.
- Status : Success ou Failed.
- Confirmations suffisantes (transaction finalisée).

**Phase 2 — Lecture structurée**.

- Header (block, timestamp).
- From / To.
- Value (native).
- Logs / Events (token transfers, autres).
- Internal transactions.
- Fee.

**Phase 3 — Documentation**.

- Capture de la page (Hunchly).
- Notation dans le journal d’enquête.
- Hash de la capture.
- Lien vers l’explorateur (stable, vérifiable plus tard).

**Phase 4 — Enrichissement**.

- Vérifier les labels associés (exchange, mixer, sanction).
- Pour les contrats, vérifier le code source si vérifié.
- Pour les adresses, regarder l’historique complet.

**Phase 5 — Croisement multi-explorateurs** (selon enjeu) :

- Pour les cas critiques, vérifier la même transaction sur 2 explorateurs indépendants.
- Confirme l’absence de bug d’affichage.
- Capture les enrichissements différents (labels, etc.).

## 11.5 Citer une page d’explorateur correctement

**Format de citation** :

- URL complète et stable.
- TXID ou adresse complète (pas tronquée).
- Date et heure de consultation (UTC).
- Hash de la capture (SHA-256).
- Pour pages dynamiques (qui peuvent évoluer), capture HTML + screenshot.

**Exemple journal** :

```
2026-03-19 14:23 UTC
Consulté Mempool.space pour TXID e3a5f9a8... 
URL: https://mempool.space/tx/e3a5f9a8c1b2d4e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0
Capture: tx_e3a5f9a8_20260319.html, hash SHA-256: abc123...
Observation: Transaction confirmée, 35 BTC transférés depuis 4 inputs Aurélien Médical vers bc1q[Akira]
Document de référence: MIXSHADOW_journal.md ligne 42
```


**Pourquoi ce niveau de rigueur ?** Les blockchains sont immutables, mais les explorateurs peuvent évoluer (UI change, labels updated, données enrichies). Une capture précise garantit reproductibilité d’analyse 6 mois ou 5 ans plus tard, voire devant juge.

## 11.6 Limites des explorateurs publics

**Manque de clustering**. Les explorateurs publics affichent transactions et adresses individuellement. Pour voir le cluster d’une adresse, il faut un outil professionnel (Chainalysis Reactor, TRM Labs).

**Labels limités**. Etherscan a beaucoup de labels mais pas tous. Tronscan en a moins. Les outils pro ont des bases label propriétaires bien plus riches.

**Pas de visualisation graphe**. Les explorateurs sont transactionnels, pas graphiques. Pour visualiser des flux complexes (peeling chains, dispersions), outil dédié (Maltego, Gephi, Chainalysis Reactor).

**Pas de scoring de risque**. Les explorateurs n’évaluent pas le risque d’une adresse. Outils pro le font.

**Performance sur grosses adresses**. Une adresse avec 100 000 transactions sera lente à charger. Outils pro paginent et indexent mieux.

**Conclusion** : explorateurs publics = base nécessaire et gratuite pour vérification. Outils pro = amplification de capacité pour investigations sérieuses. Combiner les deux. Voir Ch.19 (gratuits) et Ch.20 (pro).

## 11.7 Fil rouge — MIXSHADOW : navigation multi-explorateurs

> **🔗 MIXSHADOW — Épisode 8 : routine quotidienne**
> 
> Le travail de Sarah devient routine. Chaque jour, elle :
> 
> 1. Vérifie sur Mempool.space les nouveaux mouvements depuis les adresses Akira identifiées.
> 1. Cross-check sur Etherscan pour les flux Ethereum.
> 1. Tronscan pour les flux TRON.
> 1. Chainalysis Reactor pour la vue cluster et alertes.
> 1. TRM Labs en validation parallèle.
> 
> Au bout de 3 semaines :
> 
> - **62 adresses Bitcoin** identifiées dans les peeling chains et leurs branches.
> - **18 adresses Ethereum** identifiées dans la branche Tornado Cash et post-retraits.
> - **47 adresses TRON** identifiées dans les flux USDT.
> - **12 adresses dans 4 exchanges différents** (FixedFloat, ChangeNOW, exchange non-KYC X, autre exchange non-KYC Y).
> 
> Sarah maintient un **graphe maître** dans Chainalysis Reactor + un **journal Markdown détaillé** pour chaque mouvement. Pour chaque adresse, une **fiche d’adresse** (Ch.12) est constituée.
> 
> Elle remarque : **certaines adresses TRON** (3 d’entre elles) ont un comportement « hub » — elles reçoivent de multiples sources et redistribuent. Hypothèse : ces adresses pourraient appartenir à un **service de blanchiment** (mixer manuel, OTC desk) qu’Akira utilise comme intermédiaire, plutôt qu’à Akira directement.
> 
> Cette nuance est importante : si ces hubs sont des **services**, l’attribution ne peut pas remonter directement à Akira via ces hubs. Mais identifier le **service utilisé** par Akira est en soi une **valeur de renseignement** : d’autres groupes ransomware utilisent peut-être le même service, et le service lui-même peut être ciblé par les autorités.
> 
> Sarah documente cette hypothèse comme « probable » (confiance ~70%), avec actions de vérification : continuer à surveiller, vérifier si d’autres clusters ransomware connus ont historiquement utilisé ces hubs, croiser avec bases TRM/Chainalysis (dont les labels propriétaires sont plus riches que les labels Etherscan/Tronscan).
> 
> La méthodologie d’enquête (Partie III) va structurer cette analyse — comment passer de l’observation brute (« je vois des hops, des adresses, des flux ») à la production de renseignement (« voici la topologie du réseau de blanchiment Akira, avec niveaux de confiance et angles d’action »).

-----
