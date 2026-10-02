---
title: Chapitre 19 — Outils gratuits et explorateurs avancés
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie IV — Outils et workflow
  - index.md
---

Avant de souscrire à Chainalysis ou TRM Labs (50-500 k USD/an), beaucoup d’enquêtes peuvent être menées avec des **outils gratuits**. Ce chapitre cartographie l’arsenal gratuit du crypto-forensique.

## 19.1 Les explorateurs blockchain (rappel et approfondissement)

Déjà couverts Ch.11. En usage avancé :

**Mempool.space** :

- API gratuite généreuse pour scripts.
- Fonctionnalités avancées : visualisation des UTXO, estimateur de frais, vue mempool en temps réel.
- Parfait pour Bitcoin.

**Etherscan.io** :

- API gratuite (5 calls/sec gratuit, plus en payant).
- Recherche avancée : filtrage transactions par range de blocs, par méthode appelée.
- Watch list pour monitoring d’adresses.

**Tronscan, Solscan, BscScan, etc.** : équivalents par chaîne.

**Blockchair.com** : multi-chain, recherche cross-chain pratique.

## 19.2 OXT.me — l’outil Bitcoin avancé gratuit

**OXT** (OpenX Tools) est un outil communautaire dédié à l’analyse Bitcoin avancée. Maintenu par Samourai Wallet historiquement, accessible via oxt.me.

**Capacités** :

- Analyse de peeling chains.
- Reconstitution de clusters par heuristiques.
- Visualisation de graphes Bitcoin.
- Statistiques transactionnelles avancées.
- Détection de patterns (CoinJoin, consolidation, etc.).

**Cas d’usage** : analyse fine d’une chaîne de transactions, validation de clustering, exploration d’historique.

**Limites** : Bitcoin uniquement, interface technique, pas de support client.

## 19.3 Breadcrumbs.app

**Breadcrumbs** propose une interface graphique pour exploration de flux. Tier gratuit limité (en transactions explorées par jour) ; tier payant pour usage intensif.

**Capacités** :

- Visualisation interactive de flux blockchain.
- Multi-chain (BTC, ETH, principales).
- Suivi simple de chemins (« où vont ces fonds ? »).
- Export pour rapports.

**Cas d’usage** : visualisation rapide d’un flux pour rapport ou démo.

**Limites** : moins puissant que Chainalysis Reactor mais plus accessible.

## 19.4 Arkham Intelligence (accès public)

**Arkham Intelligence** est une plateforme de blockchain intelligence. Une partie est en accès **public gratuit** (recherche d’adresses, vue de wallets attribués) ; les fonctionnalités avancées sont en abonnement.

**Capacités gratuites** :

- Recherche d’adresses avec attributions publiques (« Vitalik Buterin », « Justin Sun », et milliers d’entités).
- Vue d’ensemble des holdings d’une adresse multi-chain.
- Information sur transactions notables.

**Pour l’enquêteur** : excellent pour vérifier rapidement si une adresse est connue publiquement. Complémentaire d’Etherscan.

## 19.5 DeBank

**DeBank** : portfolio explorer multi-chain pour adresses Ethereum/EVM. Gratuit en consultation.

**Capacités** :

- Vue portfolio d’une adresse (tokens détenus, valeurs USD).
- Activité DeFi (positions sur protocoles).
- Historique de transactions DeFi décodé.

**Cas d’usage** : pour adresse Ethereum identifiée, comprendre rapidement « combien vaut ce wallet et où est l’argent ».

## 19.6 Dune Analytics

**Dune Analytics** : plateforme de dashboards SQL sur données blockchain. Tier gratuit pour consultation, payant pour création/édition avancée.

**Capacités** :

- Dashboards créés par communauté pour des sujets spécifiques (volumes ransomware, flux Tornado Cash, exchanges activity, etc.).
- Recherche libre via SQL pour analystes techniques.
- Visualisations préconfigurées.

**Cas d’usage** : recherche de patterns macro (« qui sont les plus gros utilisateurs de tel mixer ? »), benchmarks sectoriels.

## 19.7 Token Sniffer / GoPlus

Outils d’**analyse de tokens** pour détection de honeypots, rug pulls, tokens malveillants.

**Capacités** :

- Vérification automatique du code d’un token (présence de blacklist, fonctions cachées, taxes anormales).
- Score de risque.
- Détection de patterns connus de fraude.

**Cas d’usage** : pour enquête sur un token suspect (rug pull, scam), valider rapidement la malveillance.

## 19.8 Revoke.cash

**Revoke.cash** : outil pour utilisateurs (révoquer approvals abusifs), mais aussi pour enquêteurs (consulter approvals d’une adresse).

**Capacités** :

- Liste des approvals actifs d’une adresse Ethereum (ou EVM).
- Identifie les approvals « illimités » (potentiellement dangereux).
- Permet la révocation pour les utilisateurs (transaction signée).

**Cas d’usage enquêteur** : pour adresse drainée, comprendre **quel contrat** la victime a approuvé. Identifier le drainer.

## 19.9 Chainabuse

**Chainabuse** : plateforme communautaire de signalement d’arnaques crypto.

**Capacités** :

- Recherche d’adresses signalées comme frauduleuses.
- Détails des arnaques (catégorie, date, victimes).
- Contribution communautaire.

**Cas d’usage** : pour adresse potentiellement liée à fraude, vérifier si déjà signalée. Économise du travail (« cette adresse est déjà documentée comme scam, voici les détails »).

## 19.10 Outils de sécurité et leak research

**Etherscan / Tronscan watch lists** : créer des alertes sur adresses (notifications par email).

**Whale Alert** : suivi public des grosses transactions on-chain (Twitter/X, alertes API). Utile pour macro-trends mais pas pour enquête fine.

**ZachXBT et chercheurs publics** : suivre Twitter/X pour annonces de nouvelles attributions, hacks, scams.

**OnChainScores** : scoring de risque communautaire pour adresses Ethereum.

## 19.11 Scripts custom Python

Pour usages avancés, **scripts Python** sont incontournables.

**Bibliothèques** :

- **`web3.py`** : interactions Ethereum (lecture transactions, smart contracts).
- **`tronpy`** : équivalent TRON.
- **`python-bitcoinlib`** : Bitcoin.
- **`requests`** + APIs explorateurs : pour analyses sur mesure.
- **`pandas`** : manipulation de données.
- **`networkx`** : graphes d’analyse.

**Cas d’usage** :

- Pull massif de transactions pour une adresse / cluster.
- Analyse statistique sur des milliers de transactions.
- Automatisation de monitoring (scripts cron).
- Intégration de données blockchain dans pipelines analytiques internes.

**Pour l’analyste pro** : minimum un peu de Python est utile. Permet d’automatiser des tâches répétitives et de produire des analyses sur mesure.

## 19.12 Limites des outils gratuits

Honnêtement :

**Pas de clustering automatique sophistiqué**. Reconstituer manuellement avec heuristiques fonctionne pour petits cas. Pour cas complexes, outils pro nettement supérieurs.

**Labels limités**. Etherscan et autres ont des labels mais bien moins riches que Chainalysis/TRM (qui ont bases propriétaires acquises sur années).

**Pas de scoring de risque automatisé**. Outils gratuits affichent les données ; ils n’évaluent pas le risque (« cette adresse est à 80% risque élevé »).

**Performance sur grosses adresses**. Pour wallet exchange à 100 000 transactions, outils gratuits sont lents.

**Pas de visualisation graphe automatique** (sauf Breadcrumbs limité).

**Pas d’API entreprise**. Pour intégration dans pipelines, outils gratuits sont limités.

**Pour cas complexes** : outils pro indispensables. Pour cas plus simples : outils gratuits suffisent souvent.

## 19.13 Stratégie de mix gratuit / payant

Recommandation pour cabinet en démarrage ou analyste indépendant :

**100% gratuit** (budget zéro) :

- Mempool, Etherscan, Tronscan + autres explorateurs.
- OXT pour Bitcoin avancé.
- DeBank pour Ethereum portfolios.
- Arkham public.
- Chainabuse pour fraude.
- Maltego Community Edition (limité).
- Scripts Python.

**Premier investissement** (~5-30 k USD/an) :

- Breadcrumbs ou tier payant Arkham.
- Maltego Pro avec quelques connecteurs.
- API payantes Etherscan/équivalents.

**Investissement professionnel** (50-200 k USD/an) :

- Une licence Chainalysis Reactor ou TRM Labs.
- Maltego Pro complet.
- Outils d’automatisation (Splunk, Elastic).

**Investissement enterprise** (200-500 k+ USD/an) :

- Chainalysis Reactor + Chainalysis KYT.
- TRM Labs Investigations + Know Your VASP.
- Elliptic Investigator.
- Plateforme CTI complète intégrée.

L’analyste expérimenté **utilise les bons outils pour les bons cas**. Pas besoin de licence Chainalysis pour suivre une simple transaction Bitcoin. Pas judicieux d’utiliser Etherscan seul pour un dossier multi-chaînes complexe à enjeux M USD.

-----
