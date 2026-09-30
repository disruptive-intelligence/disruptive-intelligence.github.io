---
title: Partie V — Crypto, finance, CTI ET analyse
source: Cyber/02_OSINT/OSINT_Synthese.md
note: OSINT — synthèse
up:
- - OSINT — synthèse
  - index.md
---

*Cinq chapitres avec chacun un angle précis : Ch.16 = blockchain OSINT (tracer les fonds), Ch.17 = finance et compliance (évaluer une structure), Ch.18 = CTI (l'OSINT au service de la cybersécurité), Ch.19 = techniques d'adaptation (contourner les restrictions, automatiser), Ch.20 = analyse et vérification finale (produire le renseignement).*

---


## Chapitre 16 — Crypto-actifs et blockchain OSINT

*Angle : tracer les fonds sur la blockchain et faire le lien avec l'identité. Le cours OSINT Expert & Crypto-Actifs approfondit le traçage avec les outils professionnels et les schémas de blanchiment crypto avancés.*

### 16.1 Concepts pour l'investigateur

**Bitcoin** : pseudo-anonyme (adresses publiques, transactions publiques, identité derrière l'adresse = investigation OSINT). Explorateurs : Blockchain.com, Blockchair, OXT. **Ethereum** : comptes + tokens + smart contracts ; Etherscan. **Stablecoins** (USDT/USDC — la majorité des flux illicites en 2025 passe par les stablecoins, principalement USDT sur TRON — Tronscan). Les **exchanges** (Binance, Coinbase, Kraken — les exchanges KYC sont le point de dé-anonymisation : la réquisition judiciaire révèle l'identité).

### 16.2 Les pivots OSINT → crypto

Un email lié à un exchange via Holehe (signal fort), un ENS (.eth → adresse Ethereum), une adresse publiée sur un profil (forum, Telegram, site web, QR code), un wallet hardware via un leak (dump Ledger 2020), un paiement crypto visible sur la blockchain.

### 16.3 Investigation blockchain de base

Explorer une adresse : volume total, nombre de transactions, dates, adresses en relation. Le **clustering** (heuristiques de co-spending — si deux adresses sont inputs dans la même transaction, elles appartiennent probablement au même wallet). Le suivi des flux : adresse → adresse → exchange KYC → réquisition = identité. Outils : explorateurs gratuits (Blockchain.com, Etherscan, Tronscan), OXT (analyse graphique Bitcoin), outils professionnels (Chainalysis Reactor, TRM Labs, Elliptic — cours OSINT Crypto pour la profondeur).

### 16.4 Limites et schémas d'opacification

Les **mixers/tumblers** (mélangent les fonds → cassent la traçabilité — le traçage au-delà nécessite des outils pro et des heuristiques probabilistes). Les **bridges cross-chain** (Bitcoin → Ethereum → TRON — complique le suivi). Le **DeFi** (exchanges décentralisés sans KYC → traçage possible mais complexe). Les **privacy coins** (Monero — traçage extrêmement difficile). L'analyste OSINT doit connaître ces limites et savoir quand le traçage nécessite une expertise spécialisée.

**Ce qui constitue une piste vs un élément corroboré :** une adresse Bitcoin trouvée sur un profil Telegram = piste. La même adresse avec des flux vers un exchange KYC dont le compte est au nom du suspect (via Holehe + corroboration) = élément fortement corroboré.

> **🎯 MIRAGE — Épisode 8 :** L'adresse Bitcoin du groupe Telegram (bc1q...xyz) → Blockchain.com → 12,4 BTC sur 18 mois, flux vers Binance. Le compte Binance de Delaunay (identifié via Holehe) correspond. Lien OSINT → blockchain → exchange KYC établi.

---


## Chapitre 17 — OSINT financier, corporate avancé et compliance

*Angle : évaluer une structure et un individu par les sources financières ouvertes. Le cours FININT approfondit le renseignement financier institutionnel (CRF, analyse de flux, typologies de blanchiment).*

### 17.1 Analyse financière par sources ouvertes

Les comptes publiés (Infogreffe, Companies House, SEC EDGAR). Red flags comptables pour l'analyste OSINT : CA en forte croissance sans explication, charges de « conseil » à des sociétés liées, résultat très faible malgré un CA élevé, absence de commissaire aux comptes au-delà des seuils. **Limite :** les comptes publiés sont une déclaration — ils montrent ce que la société veut montrer. L'analyste cherche les incohérences entre les comptes, les flux visibles et la réalité opérationnelle.

### 17.2 Due diligence et KYC/AML

Le KYC utilise l'OSINT pour vérifier l'identité au-delà des documents (profil LinkedIn cohérent ? présence en ligne plausible ? sanctions ?). Screening sanctions (OFAC, listes UE, ONU). Identification PEP (dirigeants politiques, hauts fonctionnaires, proches). Due diligence approfondie M&A (le cours IE traite l'IE stratégique — ici c'est la composante OSINT).

### 17.3 Investigation patrimoniale

L'immobilier (cadastre, publicité foncière, SCI), les véhicules, les biens de luxe (bateaux, avions — registres d'immatriculation publics), le train de vie visible (Instagram, Facebook — voyages, hôtels, marques). L'incohérence patrimoine/revenus est un signal fort.

**Faux positifs :** un patrimoine élevé peut être hérité, pas nécessairement frauduleux. Un dirigeant qui possède une société au Luxembourg peut faire de l'optimisation fiscale légale. **Distinguer signal et corroboration :** patrimoine incohérent avec les revenus = signal à investiguer. Patrimoine incohérent + sociétés offshore + flux crypto + train de vie excessif = faisceau convergent.

---


## Chapitre 18 — OSINT et cybersécurité : Threat Intelligence

*Angle : comment l'OSINT alimente la CTI. Le cours CTI approfondit le cycle de renseignement de menace, les frameworks (ATT&CK, Diamond Model), et la production CTI.*

### 18.1 L'OSINT comme source de CTI

Les APT et cybercriminels laissent des traces en sources ouvertes : infrastructure C2 dans DNS/certificats (domaines C2 enregistrés avec des patterns détectables — DGA, typosquatting, domaines récents), malware sur VirusTotal (relations entre fichiers, domaines, IPs), communications sur forums dark web et Telegram (acteurs qui recrutent, vendent, discutent), et code sur GitHub (malwares, exploits, outils offensifs publiés).

### 18.2 Reconnaissance offensive passive

Ce que le pentester collecte en OSINT avant de tester : DNS/sous-domaines (Amass, Sublist3r → surface d'attaque), services exposés (Shodan, Censys → versions vulnérables), technologies web (Wappalyzer → CMS, frameworks), emails d'employés (Hunter.io → phishing ciblé), credentials dans les leaks (DeHashed → password spraying).

### 18.3 Monitoring de surface d'attaque

Surveiller en continu : domaines, sous-domaines, services exposés (SecurityTrails, Censys), fuites de credentials (Intelligence X, paste sites), mentions sur forums dark web et Telegram.

**Limites :** le monitoring de surface d'attaque ne couvre que ce qui est exposé et indexé. Un C2 sur une infrastructure cloud éphémère (serverless) peut être invisible pour Shodan/Censys. Les IOCs trouvés en OSINT doivent être vérifiés — un domaine similaire peut être un typosquatting légitime (une entreprise qui enregistre des variantes défensives de son propre domaine).

---


## Chapitre 19 — Restrictions de plateformes, techniques avancées et automatisation

*Angle : comment continuer à collecter quand les plateformes ferment leurs portes, et comment automatiser la collecte à l'échelle.*

### 19.1 Les restrictions 2025

X/Twitter quasi inaccessible sans API payante, LinkedIn bloque les profils OSINT, Facebook restreint les recherches, Instagram limite l'accès sans compte, Google réduit les résultats des dorks avancés. Ces restrictions transforment l'OSINT : ce qui était simple en 2020 est devenu complexe en 2025.

### 19.2 Stratégies d'adaptation

L'archivage anticipé (capturer AVANT que les données ne deviennent inaccessibles), les APIs alternatives (Nitter pour X — instances en déclin mais encore utiles à date, unddit pour Reddit supprimé), les moteurs alternatifs (Yandex, Baidu), le Google Cache, la recherche multi-langues (translitération, moteurs locaux). Chaque stratégie a une durée de vie — l'adaptabilité est la compétence, pas la connaissance d'un outil spécifique.

### 19.3 Automatisation Python

requests (APIs), BeautifulSoup (parsing HTML), Selenium (sites dynamiques), Scrapy (crawling à grande échelle), pandas (traitement de données), networkx (graphes), rapidfuzz (entity resolution). La gestion des anti-scraping (rotation user-agents, délais, proxies, CAPTCHAs). Les APIs (Shodan, VirusTotal, Reddit/PRAW — pagination, rate limiting, authentification). Les LLMs comme assistant (résumé, extraction d'entités — avec précaution : les LLMs hallucinent → vérifier chaque fait).

---


## Chapitre 20 — Analyse, vérification et production de renseignement

*Angle : transformer les données collectées en renseignement fiable — c'est la compétence qui distingue l'analyste du chercheur amateur.*

L'**ACH** (Analysis of Competing Hypotheses) : H1 Delaunay détourne des fonds, H2 optimisation fiscale agressive mais légale, H3 innocent. Tester chaque hypothèse contre les évidences : quel fait est compatible avec H1 mais pas H2 ? Quel fait pourrait invalider H1 ? L'ACH force l'analyste à considérer les alternatives et à documenter son raisonnement.

La **cotation de fiabilité** (grille A-F/1-6 — chaque fait porte une cotation explicite). La **corroboration multi-sources** (un fait n'est établi que s'il est confirmé par 2+ sources indépendantes). Les **biais cognitifs** : biais de confirmation (on cherche ce qui confirme notre hypothèse), biais d'ancrage (la première info pèse trop), biais de disponibilité (on surestime ce qui est facilement trouvable), effet de halo (un suspect qui ment sur un point est suspecté de tout — ce n'est pas nécessairement vrai). La **timeline** (chronologie annotée — ordonne les éléments dans le temps et révèle les corrélations temporelles).

**La distinction fondamentale** — ce qui constitue une piste vs un élément corroboré : une piste = un indice unique, issu d'une source, non vérifié par une source indépendante (ex : un username commun entre deux plateformes). Un élément corroboré = un indice confirmé par 2+ sources indépendantes (ex : le même username + même avatar + même fuseau horaire + même style d'écriture sur deux plateformes). Le rapport doit distinguer les deux explicitement.

---
