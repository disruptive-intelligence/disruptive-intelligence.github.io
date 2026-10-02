---
title: 'Chapitre 37 — Cas 2 : paiement ransomware BTC à un affilié RaaS'
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VII — Cas pratiques déroulés
  - index.md
---

**Profil de l’enquête** : enquête sur paiement ransomware par une PME française. Cas similaire à MIXSHADOW dans son schéma général mais d’un autre opérateur, pour montrer la diversité.

## 37.1 Le contexte

**Société** : « TechIndustrie » (nom fictif), PME française de 180 employés, fournisseur de pièces industrielles pour automobile. Compromission ransomware début mars 2026.

**Récit** :

- Vecteur initial : email phishing ciblé sur compte VPN d’un commercial.
- Découverte : 2026-03-04 vers 06:00 UTC. Postes de production chiffrés.
- Note de rançon : groupe « Black Basta » (cluster bien documenté).
- Demande initiale : 60 BTC (~3,5 M EUR au cours).
- Négociation : descend à 22 BTC (~1,3 M EUR).
- Décision direction : payer (impossibilité de reprise rapide via backups, pression production).
- Paiement : 2026-03-10 14:32 UTC.
- Réception clé : 2026-03-10 18:45 UTC. Reprise progressive sur 2 semaines.

**Mandat** : la cyber-assurance de TechIndustrie mandate Athéna Group pour investigation post-paiement. Sarah Marin (déjà engagée sur MIXSHADOW) est trop chargée ; un collègue, **Thomas Lefèvre** (analyste senior Athéna, 4 ans expérience, certifié TRM Labs), prend en charge.

**Objectifs** :

1. Tracer les fonds.
1. Cartographier le blanchiment.
1. Contribuer à la threat intelligence Black Basta.
1. Coopérer avec autorités.

**Budget** : 6 semaines analyste, 65 000 EUR.

## 37.2 Phase 1 — Collecte initiale

**Inputs** :

- TXID du paiement.
- Adresse Black Basta de réception : `bc1q[BB-receive]...` (fictif).
- Note de rançon en pièce jointe (avec adresse mentionnée).
- Logs forensics (Mandiant) du vecteur d’entrée.

**Étape 1 — Vérification on-chain**.

Mempool.space confirme : 22 BTC reçus sur l’adresse `bc1q[BB-receive]` le 2026-03-10 14:32 UTC. Cohérent.

**Étape 2 — Caractérisation initiale**.

Adresse fraîche, jamais vue avant le paiement. Solde 22 BTC. Pas encore de mouvement sortant au moment de l’analyse initiale (J+1 du paiement).

**Étape 3 — Cluster Reactor**.

Reactor : adresse intégrée à un cluster de **180 adresses** déjà labellisé **« Black Basta operational wallet »** par Chainalysis. Confiance high.

**Bonne nouvelle** : Black Basta est un cluster bien suivi. Patterns documentés. Threat intel disponible.

## 37.3 Phase 2 — Suivi post-paiement

**Étape 1 — Premier mouvement (J+1)**.

2026-03-11 09:15 UTC : adresse de réception envoie ses 22 BTC vers une **autre adresse Black Basta** (cluster identifié) : `bc1q[BB-ops1]...`. Transaction simple (1 input, 1 output, plus frais).

Hypothèse : rotation OPSEC standard (déplacer fonds après réception pour limiter exposition).

**Étape 2 — Peeling chain (J+2 à J+7)**.

Sur 5 jours, peeling chain avec ~30 hops. Chaque hop : 0,3-1,5 BTC vers adresse externe + reste vers nouvelle adresse Black Basta.

Total éplutchés : ~14 BTC (sur 22).

Reste dans wallet principal : ~8 BTC en mouvement continu.

**Étape 3 — Analyse des branches**.

Chaque output externe est suivi. Catégorisation :

- **6 branches** vers exchanges non-KYC (4 exchanges différents).
- **8 branches** vers Tornado Cash (~5,5 BTC convertis ETH puis dépôts Tornado).
- **5 branches** vers wallets intermédiaires non-attribués (probable layering supplémentaire).
- **3 branches** vers des hubs USDT-TRON (similaire à MIXSHADOW — services de blanchiment partagés).
- **8 branches** vers adresses non encore caractérisées.

**Insight cross-incident** : **2 des 3 hubs TRON** identifiés sont les **MÊMES** que ceux observés dans MIXSHADOW (Akira). Service de blanchiment partagé entre Black Basta et Akira. Confirme l’insight de Sarah dans MIXSHADOW. Thomas alerte Sarah qui complète sa fiche.

## 37.4 Phase 3 — Caractérisation du cluster Black Basta

**Étape 1 — Examen du cluster Reactor élargi**.

Les 180 adresses du cluster Black Basta (avant le nouveau paiement) montrent :

- ~95 paiements de victimes identifiés sur 8 mois.
- Volumes individuels : 5-150 BTC par paiement.
- Total cumulé reçu : ~1 200 BTC (~70 M EUR équivalent moyen).

**TechIndustrie** est la victime n°96 du cluster (visible).

**Étape 2 — Patterns Black Basta**.

Patterns reconnus :

- Adresses fraîches dédiées par victime.
- Délai paiement → premier mouvement : 12-72h (variable).
- Peeling chain systématique.
- Tornado Cash usage.
- Bridges occasionnels vers BNB Chain.

Patterns cohérents avec opérations Black Basta documentées par Mandiant, CrowdStrike, Sophos en 2024-2025.

**Étape 3 — Threat intel sectoriel**.

Thomas alimente la base CTI Athéna :

- Nouvelles adresses identifiées dans cluster Black Basta.
- Pattern temporel du paiement (cohérent avec autres incidents Black Basta).
- Confirmation usage des hubs TRON partagés (avec Akira).

## 37.5 Phase 4 — Cashouts et coopération

**Étape 1 — Identification des cashouts**.

À 4 semaines :

- **5 dépôts identifiés sur exchanges régulés** : Binance (3), Kraken (1), Bitstamp (1). Total ~2,3 BTC équivalent USDT (~140 000 EUR au cours).
- **3 dépôts identifiés sur exchange non-KYC** spécifique : ~3,5 BTC. Pas d’angle KYC.
- **Tornado Cash** : ~5,5 BTC. Rupture analytique.
- **Hubs TRON** : ~6 BTC convertis. Layering en cours.
- **Non encore caractérisé** : ~5 BTC.

**Étape 2 — Coordination DGSI / Europol**.

Thomas transmet à la DGSI :

- Liste des 5 adresses sur exchanges régulés (KYC potentiel).
- Liste des adresses Black Basta nouvellement identifiées (alimente fichier Black Basta multi-victimes).
- Insight sur hubs partagés Akira / Black Basta.

DGSI valide. Réquisitions envoyées vers Binance, Kraken, Bitstamp.

**Étape 3 — Retours coopération (à 6 semaines)**.

- Binance : 2 comptes identifiés, ~85 000 EUR équivalent gelés. KYC fournis (deux mules différentes).
- Kraken : 1 compte identifié, ~45 000 EUR équivalent gelés. KYC fourni.
- Bitstamp : 1 compte identifié mais fonds déjà retirés avant gel. KYC fourni mais fonds dispersés.
- Total gelés : ~130 000 EUR équivalent.

**Étape 4 — Tentative gel Tether**.

Pour les flux USDT-TRON via hubs, Tether contacté via DGSI. **Réponse Tether** : étude en cours, gel partiel sur 2 adresses identifiées (~30 000 USDT). Plusieurs autres adresses pas gelées (volume opérationnel Tether limité).

## 37.6 Phase 5 — Rapport et restitution

**Rapport de 38 pages** :

- Executive summary.
- Cadrage et méthodologie.
- Faits TechIndustrie (timeline, paiement).
- Cartographie des flux (graphes Reactor + Maltego).
- Caractérisation du cluster Black Basta.
- Insight cross-incident (hubs partagés Akira / Black Basta).
- Cashouts identifiés et résultats coopération.
- Recommandations défensives.
- Limites.

**Restitution** :

- Briefing TechIndustrie + cyber-assurance + DGSI : 90 minutes + Q&A.
- Rapport diffusé en TLP RED initialement, puis TLP AMBER pour partage ISAC sectoriel.

## 37.7 Bilan

✅ **Réussites** :

- Tracking complet sur ~85% des flux.
- Coordination DGSI productive : ~130 000 EUR gelés (sur 1,3 M EUR initial = **~10% récupération nominale**).
- 3 mules identifiées pour enquête judiciaire.
- 30 000 USDT additionnels gelés via Tether.
- Insight cross-incident : confirmation hubs partagés, alimente base CTI.
- Threat intel Black Basta enrichie.

⚠️ **Limites** :

- Tornado Cash : rupture sur ~5,5 BTC.
- Exchange non-KYC : ~3,5 BTC sans angle direct.
- Attribution civile Black Basta : non possible (relevait du FBI / autorités US qui ont opérations en cours).

📊 **Métriques** :

- Durée : 6 semaines.
- Coût : 65 000 EUR.
- Récupération nominale : ~12% (130k EUR + 30k USDT sur 1,3 M EUR).
- ROI cyber-assurance : positif (rapport produit + récupération partielle dépasse coût mission).

**Apprentissage clé** : pour ransomware d’opérateur établi (Black Basta, Akira), la **threat intel cumulative** finit par produire des résultats. L’investissement Athéna sur la base de connaissance interne paie sur le long terme.

-----
