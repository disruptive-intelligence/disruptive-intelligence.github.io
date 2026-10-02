---
title: Chapitre 41 — Bitfinex 2016 → saisie 3,6 Mrd USD 2022
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VIII — Cas historiques emblématiques
  - index.md
---

Le hack Bitfinex de 2016 et la saisie de 2022 constituent le **plus gros cas de récupération crypto** documenté à ce jour. Six ans entre le vol et la saisie. Démonstration que la traçabilité on-chain, combinée à la persévérance et la coopération, peut aboutir.

## 41.1 Le hack — août 2016

**Faits** :

- 2 août 2016 : Bitfinex (exchange majeur, basé à Hong Kong) annonce avoir été piraté.
- **119 756 BTC** volés (~72 M USD au cours de l’époque, ~7,2 Mrd USD au cours record post).
- Vecteur précis : compromis multi-signature wallet via failles d’implémentation BitGo (debate technique sur la responsabilité, jamais entièrement clarifié publiquement).
- Bitfinex socialise les pertes : haircut de 36% sur tous les comptes utilisateurs, émission de tokens BFX comme dette.

**Adresses** :

- 119 756 BTC sont **disséminés** entre 2 000+ adresses fraîches dans les heures suivant le hack.
- Ces adresses restent ensuite **largement dormantes** pendant des années.

**Suivi** :

- Communauté Bitcoin et chercheurs (notamment **Sergej Kotliar**, Alec Ziupsnys, et plus tard Chainalysis, Elliptic) **monitor les wallets**.
- Quelques mouvements occasionnels (petites sommes) entre 2016 et 2022, surveillés.
- Bitfinex offre des récompenses pour informations.

## 41.2 La saisie — février 2022

**Annonce DOJ — 8 février 2022** :

- **Heather « Razzlekhan » Morgan** et **Ilya « Dutch » Lichtenstein**, couple à Manhattan, arrêtés.
- Chargés de **conspiracy to commit money laundering** et **conspiracy to defraud the United States**.
- DOJ saisit **94 636 BTC** (sur les 119 756 originaux), valorisés à **3,6 Mrd USD** au cours de l’époque.

**Méthode d’investigation reconstituée** (depuis l’indictment unsealed et investigations journalistiques) :

**Étape 1 — Long monitoring**. Les adresses du hack sont surveillées par autorités et chercheurs depuis 2016. Quelques mouvements occasionnels alimentent le dossier.

**Étape 2 — Patterns émergent**. À partir de 2020-2021, des **mouvements plus actifs** émergent. Lichtenstein utilise progressivement les fonds via :

- AlphaBay (darknet market, saisi en 2017 — son historique permet aux autorités d’extraire des liens).
- Multiple exchanges (avec KYC pour certains).
- Mixers (Bitcoin Fog notamment).

**Étape 3 — KYC sur exchanges**. Lichtenstein dépose une **partie** des fonds sur exchanges utilisant **identités réelles** (lui ou Morgan, ou liens identifiables). Erreur OPSEC critique.

**Étape 4 — Décrypter l’infrastructure**. Le DOJ exécute un mandat de perquisition sur le **cloud storage** de Lichtenstein (Cloud account). Le cloud contenait un fichier chiffré avec **les clés privées des wallets contenant ~94 636 BTC**.

Le fichier était sécurisé par mot de passe. Le DOJ accède au mot de passe (modalités précises peu détaillées publiquement — possible exploitation cloud, possible recovery via partner, possible cryptanalyse). Décryption permet **prise de contrôle** des wallets et saisie effective.

**Étape 5 — Saisie**. 94 636 BTC transférés depuis les wallets compromis vers wallet contrôlé par US gouvernement.

**Étape 6 — Inculpation**. Indictment publié, charges expliquées, fonds publiquement annoncés.

## 41.3 Le procès — 2023-2024

**Lichtenstein** : plaide coupable en août 2023 pour conspiracy to commit money laundering et fraud against the United States.

**Morgan** : plaide coupable au même moment pour conspiracy.

**Sentencing** :

- **Lichtenstein** : condamné en novembre 2024 à 5 ans de prison.
- **Morgan** : condamnée en novembre 2024 à 18 mois de prison.

**Restitution** : les BTC saisis vont en partie à la restitution des victimes (utilisateurs Bitfinex de 2016 ayant subi le haircut). Procédure complexe étant donné l’évolution de la valeur (BTC valait ~600 USD en 2016, ~40-70k en 2024).

## 41.4 Méthodes mobilisées

**Tracking on-chain de longue durée** :

- Surveillance des adresses pendant 6 ans.
- Identification des mouvements progressifs.
- Outils : Chainalysis Reactor, monitoring custom, communauté.

**Saisies antérieures comme inputs** :

- AlphaBay saisi en 2017 a fourni données utilisées pour le dossier Bitfinex.
- Bitcoin Fog saisi 2021, idem.

**KYC exchange** :

- Erreurs OPSEC de Lichtenstein/Morgan exposant identité.

**Cloud forensics** :

- Mandat de perquisition sur le cloud account.
- Décryption des fichiers stockés.

**Coopération internationale** :

- DOJ + FBI + IRS + autres agences US.
- Coopération avec exchanges concernés.

**Persévérance institutionnelle** :

- 6 ans de monitoring patient.

## 41.5 Leçons

**Pour les criminels (perspective des autorités)** :

- **Long terme = vulnérabilité**. Les adresses « tranquilles » pendant des années deviennent **incentive croissant** à mauvaise OPSEC quand l’opérateur tente de monétiser.
- **Erreurs OPSEC se cumulent**. Une seule erreur sur 6 ans suffit (KYC exchange, cloud non-sécurisé, etc.).
- **Cryptographie protège les fonds, pas les humains**. Lichtenstein avait techniquement les clés privées — mais ses **comptes utilisateur** étaient compromis par perquisition.

**Pour les enquêteurs** :

- **Patience institutionnelle** : LEA peuvent maintenir surveillance pendant des années.
- **Recoupement multi-source** : crypto + cloud + exchange KYC + saisies antérieures.
- **Volume justifie l’investissement** : 3,6 Mrd USD justifie ressources LEA significatives.

**Pour les analystes** :

- **Documentation longitudinale** des wallets criminels alimente les cas futurs.
- **Le « cold storage » pendant des années** ne signifie pas « impossible à saisir ».

**Pour les victimes** :

- **Récupération possible mais lente**. Bitfinex est exemple. Beaucoup d’incidents ne aboutissent pas comme cela.

## 41.6 Bitfinex aujourd’hui

À 2026 :

- Procédure de restitution toujours en cours pour utilisateurs originaux.
- Bitfinex a survécu à l’incident, reste exchange actif (et Tether y est lié).
- Cas étudié dans formations forensiques (Chainalysis utilise comme étude de cas).

-----
