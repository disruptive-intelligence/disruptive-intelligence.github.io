---
title: Chapitre 35 — Menaces dark web par secteur d'activité
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie VI — ANALYSE, renseignement et production
  - index.md
---

Les menaces dark web ne sont pas homogènes — chaque secteur a ses profils de risque. Ce chapitre cartographie les patterns sectoriels observés 2024-2026 pour orienter les postures défensives.

## 35.1 Services financiers

**Profil** : cible historique de premier rang. Concentre valeur monétaire directe et données sensibles.

**Menaces dominantes** :

- **Carding** et fraude à la carte bancaire. Marchés spécialisés (BriansClub, successeurs), prix 5-150 USD/carte selon qualité.
- **Comptes bancaires compromis** (access credentials + cookies session). Prix 100-1 000 USD selon balance.
- **Fraude à l'identité** : fullz pour ouverture de comptes frauduleux, crédit fraud.
- **Ransomware ciblé banks, assets management, fintech** : rançons élevées, sensibilité régulatoire.
- **Targeted phishing** sur employés clés (trading, IT, SWIFT). Industrialisation via PhaaS.
- **SIM swapping** pour contourner SMS 2FA sur comptes crypto et bancaires.
- **Insiders recrutés sur forums** : le recrutement d'employés de banques pour faciliter fraudes est documenté.

**Acteurs typiques** : groupes RaaS (LockBit, ALPHV, Black Basta ciblent finance régulièrement), carders spécialisés, IAB banking-focused, fraudeurs opportunistes.

**Impacts** : pertes financières directes, impact régulatoire (amendes CNIL/ACPR, sanctions réglementaires), réputationnel, opérationnel (ransomware).

**Priorités défensives** :

- MFA FIDO2 obligatoire (pas SMS).
- Monitoring approfondi des marchés de cartes et logs bancaires.
- Détection de SIM swapping par monitoring téléphonique.
- Veille insiders (anormalités comportement, patterns communications).
- Segmentation forte des systèmes critiques (trading, SWIFT).

## 35.2 Santé

**Profil** : cible en forte croissance. Combinaison de données sensibles + systèmes critiques + budgets souvent plus faibles en cyber = cible privilégiée.

**Menaces dominantes** :

- **Ransomware** : impact vital (hôpitaux, urgences, PACS), urgence → taux de paiement historiquement élevé (bien que déclinant).
- **Vol de dossiers médicaux** : prix 50-250 USD/dossier US (marché développé), moins en Europe. Usages : fraude assurance, chantage, fraude à l'identité enrichie.
- **PHI (Protected Health Information)** et HIPAA breaches US — obligations de notification publique qui génèrent publicité négative.
- **Ciblage des labos et R&D pharma** : propriété intellectuelle (formules, essais cliniques, brevets).
- **Access to provider networks** : vente d'accès à hôpitaux, cabinets médicaux, cliniques sur forums.

**Cas emblématiques** :

- **Change Healthcare (2024)** : ransomware ALPHV, paiement ~22 M USD, impact massif sur chaîne de remboursements US.
- **Hôpitaux français** : multiples cas 2023-2025 (Corbeil-Essonnes, Versailles, André-Mignot).
- **Synnovis (UK, 2024)** : Qilin, impact sur analyses sanguines NHS Londres.

**Priorités défensives** :

- Backup offline testé et fiable.
- Segmentation IT/OT médicale (PACS, imaging, bloc opératoire).
- Plan de continuité avec procédures dégradées.
- MFA renforcé malgré les contraintes UX des soignants.
- Coopération sectorielle (H-ISAC).

## 35.3 Industrie / manufacturing

**Profil** : montée en ciblage 2020-2026. Combine OT vulnérable + propriété intellectuelle + supply chain critique.

**Menaces dominantes** :

- **Ransomware** : impact opérationnel direct (arrêt production), pression au paiement.
- **Vol de propriété intellectuelle** : specs, plans, formules. Acheteurs : concurrents, États.
- **Targeted IAB sur OT** : accès aux systèmes SCADA revendus, usage potentiel sabotage ou espionnage.
- **Supply chain attacks** : compromission fournisseur pour atteindre cible en aval.

**Cas emblématiques** :

- **Colonial Pipeline (2021)** : DarkSide, impact infrastructurel US.
- **JBS (2021)** : REvil, impact chaîne alimentaire mondiale.
- **Saint-Gobain, Norsk Hydro, Picoty** : exemples européens de ransomware manufacturing.

**Ciblage aerospace/defense** : particulièrement sensible. DARKSTREAM s'inscrit dans ce segment. Intérêt étatique parfois, intérêt cybercriminel toujours.

**Priorités défensives** :

- Segmentation IT/OT stricte (modèle Purdue).
- Inventaire et patching des OT assets.
- Air-gap ou DMZ pour systèmes critiques.
- Backups offline pour automates et configurations industrielles.
- Partenariats avec CERT sectoriel (ex : France : CERT-IST).

## 35.4 Énergie et utilities

**Profil** : cible stratégique, souvent OIV. Intérêt étatique potentiel (prépositionnement), cybercriminel (ransomware), hacktiviste (ciblage géopolitique).

**Menaces dominantes** :

- **Pré-positionnement étatique** (Volt Typhoon contre US, patterns similaires contre UE).
- **Ransomware ciblant opérateurs électriques, gaziers, eau** : impact potentiel sur population.
- **Sabotage par hacktivistes** : tentatives contre infrastructure eau (Cyber Av3ngers iraniens contre opérateurs US).
- **Exfiltration de données techniques** : topologie réseau, procédures, fournisseurs.

**Cas emblématiques** :

- **Colonial Pipeline** (cité).
- **Cyber Av3ngers contre Unitronics (2023-2024)** : compromissions opérateurs eau US par défaut-password sur PLC.
- **Multiples incidents ukrainien** (cours APT détaille).

**Priorités défensives** :

- Défense en profondeur IT/OT.
- Monitoring OT spécialisé (Dragos, Claroty, Nozomi).
- Plan de continuité incluant dégradés analogiques.
- Coopération ANSSI / FranceNum / ENTSO-E / E-ISAC.

## 35.5 Retail et e-commerce

**Profil** : cible de masse pour fraude et credentials volumineux.

**Menaces dominantes** :

- **Credential stuffing** : comptes clients volés revendus.
- **Skimming / Magecart** : injection de JS malveillant dans sites e-commerce pour voler données de paiement.
- **Ransomware** : grandes chaînes ciblées (Marks & Spencer 2025, Co-op 2025, autres).
- **Fraude à l'identité** sur comptes clients.

**Priorités défensives** :

- Monitoring crédentiels sur stealer markets.
- Sécurité applicative web (OWASP, CSP, SRI pour scripts tiers).
- Détection fraude (ML sur comportements).
- Plan de continuité e-commerce.

## 35.6 Télécoms

**Profil** : infrastructure critique + accès aux communications clients. Cible d'acteurs étatiques (Salt Typhoon contre télécoms US) et cybercriminels.

**Menaces dominantes** :

- **Accès au cœur réseau pour interception** : Salt Typhoon contre opérateurs US (2024).
- **SIM swapping** par insiders corrompus.
- **Ransomware** contre opérateurs.
- **Vol de données d'abonnés** (milliards de lignes potentielles).

**Priorités défensives** :

- Durcissement accès privilégiés réseau.
- Monitoring insiders (insider threat programs).
- Chiffrement des métadonnées et communications où possible.
- Coopération ANSSI et homologues internationaux.

## 35.7 Secteur public et gouvernement

**Profil** : cible prioritaire d'APT étatiques. Données sensibles, fonctionnaires à haute valeur, services critiques.

**Menaces dominantes** :

- **Espionnage étatique** : APT29, APT40, APT31 ciblent régulièrement administrations.
- **Ransomware** : multiples collectivités locales victimes (mairies, départements).
- **Vol de données citoyens** : identités, fiscales, sociales.
- **Influence et désinformation** via compromission de comptes officiels.

**Cas emblématiques** :

- **France Travail (2024)** : breach massif de données chercheurs d'emploi.
- **Multiples collectivités françaises** victimes ransomware.
- **APT31 contre parlementaires britanniques et américains** (documenté 2024).

**Priorités défensives** :

- Alignement ANSSI (OIV, NIS 2).
- Segmentation et zero trust.
- Protection dirigeants et élus (monitoring VIP sur dark web).
- Sensibilisation face aux opérations d'influence.

## 35.8 Éducation et recherche

**Profil** : cible régulière, budgets cyber limités, posture défensive souvent faible.

**Menaces dominantes** :

- **Ransomware** contre universités (multiples cas France 2024-2025).
- **Vol de propriété intellectuelle** : recherche, brevets, données d'essais cliniques.
- **Targeted espionnage** sur chercheurs dans domaines sensibles (quantique, IA, biotech).
- **Compromission d'infrastructures partagées** : sites universitaires hébergeant de multiples services.

**Priorités défensives** :

- Renforcement posture malgré contraintes budgétaires.
- Coopération Renater / CSIRT académique.
- Segmentation entre recherche sensible et usage général.

## 35.9 Cryptomonnaies et fintech crypto

**Profil** : cible de très forte valeur (vols de millions USD possibles en une opération).

**Menaces dominantes** :

- **Vol de wallets** (exchanges, cold wallets). Cas Ronin Network, Bybit, FTX (mais pour FTX : hack post-faillite).
- **Phishing ciblé** des utilisateurs particuliers.
- **Compromission de smart contracts** (bridges DeFi notamment).
- **Stealers ciblant extensions crypto** (MetaMask, Phantom).

**Priorités défensives** :

- Cold storage pour majorité des fonds.
- Multi-sig hardware wallets.
- Sécurité opérationnelle des validateurs (Ronin a été compromis par vol de clés validateurs).
- Veille active sur marchés de phishing kits crypto.

## 35.10 Fil rouge — DARKSTREAM : le secteur aerospace/defense

> **🌐 DARKSTREAM — Épisode 19 : contextualisation sectorielle**
>
> Lucas inclut dans son rapport final une section sur le **contexte sectoriel aerospace/defense 2024-2026**.
>
> **Observations générales sur le secteur** :
> - Menace étatique croissante (Chine, Russie particulièrement intéressées par technologies sensibles).
> - Menace cybercriminelle opportuniste en hausse : le secteur est perçu comme « cible de valeur » avec revenus potentiels élevés via ransomware ou revente de données techniques.
> - Multiple cas 2024-2025 : plusieurs équipementiers aerospace européens et US victimes de ransomware ou exfiltrations.
> - IndustrialLeaks et forums similaires listent régulièrement des « aerospace sellers » — marché structuré pour ces données.
> - Acheteurs potentiels : services de renseignement (étatiques), concurrents industriels (via proxies), groupes cybercriminels cherchant à revendre ou exploiter levier chantage.
>
> **Spécificités défense** :
> - Données contrôlées export (ITAR aux US, équivalents européens) — exposition juridique accrue si fuite.
> - Partenariats multi-pays (programmes OTAN, européens) — ripple effects si un partenaire est compromis.
> - Sensibilité gouvernementale : remontée obligatoire aux autorités (en France : ANSSI, DGSI, autorités militaires selon classification des données).
>
> **Recommandations spécifiques** pour Vectris au-delà des actions DARKSTREAM :
> - Coopération accrue avec CERT-DEF (CERT défense).
> - Participation ISAC sectoriel aerospace (ASD-EUROSPACE, AIAC).
> - Revue des contrôles ITAR/export.
> - Sensibilisation collaborateurs R&D sur menace stealer et hygiène poste de travail.
> - Prépar communication gouvernementale (client défense) en cas d'escalade.
>
> Cette contextualisation donne à la direction Vectris la dimension **stratégique** — l'incident DARKSTREAM n'est pas isolé, il s'inscrit dans un pattern sectoriel qui appelle réponse durable, pas seulement réaction ponctuelle.

---
