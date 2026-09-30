---
title: Chapitre 45 — Synthèse MIXSHADOW
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VIII — Cas historiques emblématiques
  - index.md
---

Bilan complet du fil rouge déployé tout au long du cours.

## 45.1 Récapitulatif factuel

**Victime** : Aurélien Médical, équipementier français de matériel hospitalier (700 collaborateurs, OIV santé, Lyon).

**Incident** : ransomware Akira, mars 2026. Vecteur : compromission VPN admin via stealer log. 3 hôpitaux clients impactés (patients en attente, dont cas vitaux).

**Paiement** : 35 BTC (~2 M EUR) le 14 mars 2026. Clé déchiffrement reçue. Reprise progressive sur 3 semaines.

**Mandat** : Aurélien Médical + DGSI mandatent Athéna Group. Sarah Marin, analyste senior. 8 semaines, 80 k EUR.

**Objectifs** : tracer, cartographier, identifier off-ramps, contribuer à attribution, coopérer avec autorités.

## 45.2 Méthodes appliquées

**Outils** :

- Chainalysis Reactor (principal).
- TRM Labs (validation croisée).
- Mempool.space, Etherscan, Tronscan, BscScan (publics).
- Maltego, Excalidraw (visualisation).
- Hunchly (capture).
- OpenTimestamps (anchoring preuves).

**Méthodes** :

- Cadrage initial structuré (Ch.24).
- Fiches d’adresses pour 250+ adresses (Ch.12).
- Suivi peeling chain (Ch.7).
- Tracking cross-chain (Ch.33).
- Analyse Tornado Cash statistique (Ch.31).
- Caractérisation hubs TRON (Ch.10).
- Calibration WEP systématique (Ch.18).
- Chain of custody rigoureuse (Ch.23).

**Coordination** :

- Briefings DGSI bi-hebdomadaires.
- Coordination Tether pour gel USDT-TRON.
- Coordination FBI / Europol via DGSI.
- Réquisitions via DGSI vers Binance, Kraken, Coinbase.

## 45.3 Résultats

**Cartographie** :

- **250 adresses identifiées** au total (Bitcoin, Ethereum, TRON, Solana mineur).
- **4 chaînes principales** couvertes.
- **~75% des flux** Akira post-paiement Aurélien Médical tracés.

**Caractérisation Akira** :

- Patterns de blanchiment documentés (peeling Bitcoin → swap FixedFloat → Tornado Cash sur ETH → conversion USDT-TRON via exchange non-KYC → dispersion TRON via hubs).
- Pattern temporel suggérant fuseau horaire UTC+9 / Asie de l’Est (possible, non-conclusif).
- Choix Bitcoin (vs Monero) suggérant compromis traçabilité / facilité opérationnelle.
- **Insight transversal** : 2 hubs TRON identifiés comme **services de blanchiment partagés** entre Akira et Black Basta (insight cross-incident, alimente dossier multi-victimes).

**Coopération** :

- **3 mules identifiées** sur Binance / Kraken.
- **~45 000 USDT gelés** sur exchanges régulés.
- **~30 000 USDT gelés** via Tether (sur 6 adresses TRON).
- **6 adresses Akira principales** transmises pour évaluation sanctions OFAC.
- **2 adresses « possibles retraits Tornado »** alimentent suivi complémentaire.

**Threat Intel** :

- Fiche acteur Akira enrichie (base Athéna).
- Pattern blanchiment Akira documenté pour réutilisation.
- Insight hubs partagés pour coordination CTI plus large.

## 45.4 Bilan financier

**Récupération nominale** :

- 45 000 USDT (Binance/Kraken) + 30 000 USDT (Tether) = **75 000 USDT gelés**.
- ~ **3,75 % du paiement initial** (75k / 2 M EUR).

**Bilan en valeur de renseignement** :

- 3 mules identifiées (utiles pour enquête judiciaire ultérieure).
- 2 hubs blanchiment identifiés (alimentent base Chainalysis / TRM).
- Pattern Akira documenté (réutilisable pour autres victimes).
- Coopération multi-juridictionnelle activée.

**Bilan en valeur stratégique** :

- Aurélien Médical bénéficie d’un dossier complet pour procédure judiciaire et déclaration assurance.
- DGSI bénéficie d’un dossier alimentant ses suivis Akira / RaaS.
- Athéna renforce sa base CTI et sa crédibilité opérationnelle.

## 45.5 Limites assumées

**Pas de récupération massive**. Le bilan financier est **modeste**. C’est la réalité de l’enquête ransomware, sauf cas exceptionnels (Bitfinex, Colonial).

**Pas d’attribution civile**. Akira reste un cluster sans identités civiles attribuées par OSINT seul. Relevait des autorités via voies classifiées.

**Tornado Cash** : rupture analytique sur ~12 ETH (~36 000 USD à l’époque). Hypothèses calibrées, pas certitudes.

**Exchange non-KYC X** : ~150 000 USDT sans angle KYC direct.

**Solana** : couverture moindre des outils, sous-flux peu caractérisés.

## 45.6 Apprentissages

**Pour Sarah** :

- L’enquête « modeste en récupération » peut être **substantielle en valeur de renseignement**.
- La calibration honnête préserve la crédibilité et permet la coopération.
- Le travail de cartographie complète prend des semaines mais paie sur le long terme.

**Pour Athéna** :

- Combiner outils pro (Chainalysis + TRM) augmente la couverture et la confiance.
- La coordination DGSI active les leviers que l’OSINT pure ne peut activer.
- Les insights cross-incident (hubs partagés) construisent une vue stratégique.

**Pour Aurélien Médical** :

- Le paiement en pression vitale, choix difficile, contextualisé.
- L’enquête post-paiement maximize la valeur extraite des fonds payés.
- Renforcement des défenses pour incidents futurs.

**Pour l’écosystème** :

- L’industrie ransomware est résiliente mais pressurée.
- La coopération internationale finit par produire des résultats.
- Chaque enquête contribue à la capacité collective.

## 45.7 Devenir post-MIXSHADOW

**Aurélien Médical** :

- Reprise complète de l’activité.
- Investissement majeur dans cybersécurité (EDR, MFA universel, segmentation, surveillance 24/7).
- Plan IR durci.
- Communication transparente avec clients hospitaliers.

**Sarah Marin** :

- Continue chez Athéna, monte en seniorité.
- MIXSHADOW comme étude de cas en formations internes.
- Contribue à publication CTI sectorielle (TLP AMBER) sur Akira.

**DGSI** :

- Dossier Akira enrichi.
- Coordination Europol / FBI continue.
- Démantèlement éventuel d’Akira : à plus long terme, comme tous les groupes RaaS — cycle continue.

**Akira (groupe)** :

- Continue à opérer en 2026.
- Pression croissante des autorités.
- Possible rebranding ultérieur.
- Patterns documentés alimentent la défense collective.

## 45.8 Le message final de MIXSHADOW

> **L’enquête crypto-forensique professionnelle ne promet pas miracles. Elle produit du renseignement actionnable, contribue à la justice, et alimente la défense sectorielle. Sa valeur tient à sa rigueur méthodologique, sa calibration honnête, et son intégration dans des écosystèmes coopératifs.**

C’est ce que le cours OSINT Crypto a tenté de transmettre, à travers méthodes, outils, cas, et fil rouge.

La Partie IX va aborder la **production professionnelle** : rapport, calibration formelle, coopération, éthique, et programme durable.

-----
