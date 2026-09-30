---
title: Chapitre 29 — Acteurs étatiques
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie V — Typologies d’abus crypto
  - index.md
---

Lazarus et contournement de sanctions

Les acteurs étatiques sophistiqués utilisent le crypto à grande échelle. **Lazarus** (DPRK / Corée du Nord) est l’archétype documenté. Les opérations de contournement de sanctions (Russie post-2022, Iran) sont également structurantes.

## 29.1 Le profil Lazarus

**Lazarus Group** (alias APT38, alias Hidden Cobra). Cluster d’acteurs DPRK opérant sous direction du Bureau 121 / Reconnaissance General Bureau (RGB).

**Évolution** :

- 2014-2016 : ciblage banques traditionnelles (SWIFT). Heist Bangladesh Bank 2016 : 81 M USD.
- 2017+ : pivot massif vers crypto. Cible exchanges, particuliers, DeFi.
- 2022+ : domination des plus gros vols crypto annuels.

**Cas marquants attribués** :

- **Ronin Network** (mars 2022, 625 M USD).
- **Harmony Bridge** (juin 2022, 100 M USD).
- **Atomic Wallet** (juin 2023, 100 M USD).
- **CoinEx** (septembre 2023, 54 M USD).
- **Stake.com** (septembre 2023, 41 M USD).
- **Multiple incidents** 2024-2025.

Estimations cumulées : **plusieurs milliards USD** volés depuis 2017. Selon TRM Labs et Chainalysis, Lazarus est l’acteur étatique le plus prolifique en crypto.

**Usage des fonds** : finance les programmes étatiques DPRK, contourne les sanctions internationales.

## 29.2 TTP Lazarus crypto

**Vecteurs d’accès** :

- Phishing sophistiqué (fake recruiters, fake job offers — « Operation Dream Job »).
- Compromission d’employés clés d’exchanges et protocoles.
- Vulnérabilités de smart contracts.
- Compromission d’infrastructure (nodes, relayers).

**Patterns de blanchiment** :

- **Tornado Cash** historiquement (avant sanctions août 2022, après aussi).
- **Bridges cross-chain** intensifs.
- **CoinJoin** Bitcoin.
- **Conversion en privacy coins** (Monero) parfois.
- **Off-ramp via OTC asiatiques** (Russie, Asie centrale).
- **Réseau de mules** pour cashout.

**Sophistication opérationnelle** : OPSEC souvent élevée. Wallets fraîs, infrastructure rotative, blanchiment méticuleusement structuré.

## 29.3 Reconnaître un cluster Lazarus

**Indicators** (selon TRM, Chainalysis, FBI) :

- Adresses précédemment attribuées à Lazarus dans les bases vendor.
- Patterns de blanchiment cohérents avec doctrine Lazarus.
- TTP de compromise compatibles.
- Liens infrastructure (mêmes serveurs, même malware family).

**Important** : Lazarus n’est **pas** la seule explanation pour des patterns sophistiqués. Sur-attribution est piège. Validation requise.

## 29.4 Sanctions et coopération

**OFAC** :

- A sanctionné de multiples wallets Lazarus.
- Sanction Tornado Cash (août 2022) cite Lazarus comme une des raisons.
- Mises à jour régulières.

**FBI** : très actif sur ransomware DPRK et Lazarus. Multiple advisory et identifications publiques.

**Coopération internationale** : tendue (DPRK n’est pas coopératif), mais pression des US/UE/Japon/Corée du Sud sur exchanges et points de cashout.

## 29.5 Russie et contournement de sanctions

Depuis 2022, contournement de sanctions Russie via crypto est documenté.

**Acteurs** :

- Particuliers russes contournant restrictions financières.
- Exchanges russes / liés (Garantex, sanctionné OFAC).
- Acteurs étatiques utilisant crypto pour transactions internationales.

**Outils** :

- Stablecoins (USDT-TRON dominant).
- P2P trading (LocalBitcoins historiquement, Binance P2P, autres).
- OTC desks dans juridictions permissives.

**Pour l’enquêteur** : flux Russie-related identifiables par patterns. Coopération avec exchanges pour gel possible (USDT-Tether a gelé multiples adresses Russie sur réquisition).

## 29.6 Iran et autres

**Iran** : usage crypto pour contourner sanctions, financer programmes étatiques. Cluster acteurs étatiques iraniens (« Pioneer Kitten », « APT34 », autres) avec activité crypto.

**Autres acteurs étatiques** : Chine (moins dans crypto direct, plus dans surveillance et minage), pays émergents avec capacité cyber moindre.

## 29.7 Méthode d’enquête : acteurs étatiques

**Étape 1 — Hypothèse étatique**. Patterns sophistiqués + indicateurs ne signifient **pas automatiquement** acteur étatique. Validation requise.

**Étape 2 — Recoupement avec bases vendor**. Chainalysis, TRM, Elliptic ont des labels « Lazarus », « Iran-related », etc. avec des niveaux de confiance.

**Étape 3 — Recoupement avec sources publiques**. OFAC SDN, FBI advisory, Mandiant / CrowdStrike threat reports.

**Étape 4 — Analyse TTP**. Patterns techniques (vecteurs, infrastructure, malware) si applicables.

**Étape 5 — Coopération**. Impossible directement (les acteurs sont étatiques). Coopération via FBI / Europol / autorités équivalentes pour suivre les flux et identifier points d’action (exchanges traversés, cashout).

**Étape 6 — Rapport et calibration**. Attribution étatique nécessite calibration prudente (cf Ch.18). Rarement « certain » sans accès renseignement classifié.

## 29.8 Limites

**Attribution civile impossible**. L’identification des opérateurs individuels au sein de Lazarus est réservée aux services de renseignement. OSINT identifie les **clusters** et **patterns**, pas les **individus**.

**Coopération minimale avec juridictions sanctuaires**. DPRK, Russie, Iran ne coopèrent pas. Action via points externes (exchanges, services, transit).

**Récupération limitée**. Quelques cas (Bitfinex saisie 3,6 Mrd, autres opérations FBI), mais dans l’ensemble, fonds Lazarus difficiles à récupérer.

## 29.9 Tendances 2024-2026

**Lazarus en croissance**. Vols cumulés en milliards USD/an.

**Sophistication croissante**. Usage de tous les outils d’obfuscation (mixers post-Tornado, bridges, privacy coins, réseaux de mules complexes).

**Coopération internationale renforcée**. Mais lente et fragmentée.

**Sanctions ciblées** : OFAC continue d’ajouter wallets et entités. UE suit progressivement.

**Pour l’analyste** : les acteurs étatiques sont **angle stratégique** pour les services de renseignement et CTI privé senior. Pour l’analyste défensif d’organisation, les détecter dans son périmètre = **alerte rouge** justifiant escalade immédiate (ANSSI, DGSI selon contexte).

-----
