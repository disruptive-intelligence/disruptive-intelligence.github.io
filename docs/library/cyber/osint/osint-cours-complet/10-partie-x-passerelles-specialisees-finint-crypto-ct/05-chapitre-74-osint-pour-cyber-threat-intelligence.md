---
title: Chapitre 74 — OSINT pour Cyber Threat Intelligence
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - 'PARTIE X — Passerelles spécialisées : FININT, Crypto, CTI, Influence'
  - index.md
---

## 74.1 OSINT au service de la CTI

La **Cyber Threat Intelligence** (CTI) est la discipline qui produit du renseignement sur les menaces cyber : acteurs, infrastructures adverses, TTP, IOCs.

L'OSINT est l'une des sources majeures de la CTI, avec les feeds commerciaux, l'analyse interne, le partage communauté.

Le présent chapitre fournit la **vue maître**. Pour la profondeur (attribution étatique, threat hunting, analyse intrusion, framework MITRE complet), renvoi vers **cours CTI dédié**.

## 74.2 IOCs : Indicators of Compromise

**Types d'IOCs.**

- Hashs (MD5, SHA-1, SHA-256) de malware.
- Domaines malveillants.
- IPs malveillantes.
- URLs (phishing, C2).
- Emails (phishing).
- Wallets (rançonneurs).

**Sources publiques OSINT.**

- **VirusTotal** : analyse multi-AV.
- **AbuseIPDB** : IPs malveillantes.
- **URLhaus** (abuse.ch) : URLs.
- **MalwareBazaar** (abuse.ch) : samples.
- **ThreatFox** (abuse.ch) : IOCs.
- **AlienVault OTX** : community-driven.
- **MISP** instances publiques.

## 74.3 TTPs : Tactics, Techniques, Procedures

**MITRE ATT&CK Framework.** Référence mondiale. Catalogue des comportements adverses.

**Pour OSINT.**

- Identification de TTPs dans rapports publics.
- Cross-référence cas observés vs ATT&CK.
- Cartographie de groupes par TTP signature.

## 74.4 Modèles d'analyse

**Diamond Model.** 4 features : adversary, capability, infrastructure, victim.

**Cyber Kill Chain (Lockheed Martin).** 7 phases.

**MITRE ATT&CK.** Le plus utilisé en 2026.

## 74.5 Acteurs et groupes

**Catalogues publics de groupes.**

- **MITRE ATT&CK Groups**.
- **MISP Galaxy**.
- **ThaiCERT APT groups**.
- **CrowdStrike adversary list**.
- **Mandiant APT reports**.

**Précaution attribution.** Attribution à un groupe nommé suppose éléments solides. OSINT permet hypothèse, pas attribution définitive sans corroboration.

## 74.6 Plateformes CTI

**Open source.**

- **MISP** : Malware Information Sharing Platform. Standard de partage CTI.
- **OpenCTI** : plateforme moderne.
- **YARA** rules.

**Commercial.**

- Recorded Future, Mandiant Advantage, CrowdStrike Falcon X, Flashpoint.
- Coûts élevés (50 k€-500 k€/an).

## 74.7 Sources publiques CTI

- **abuse.ch** : malware tracker (URLhaus, MalwareBazaar, ThreatFox, FeodoTracker, SSLBL).
- **AlienVault OTX**.
- **MISP communities**.
- **CISA alerts** (US).
- **ANSSI bulletins** (France).
- **NCSC alerts** (UK).
- **CERT-FR** (France).
- **Twitter/X CTI community** (suivi de chercheurs).

## 74.8 Workflow CTI OSINT

1. **Veille** : monitoring sources publiques.
2. **Collecte IOCs**.
3. **Enrichissement** (VirusTotal, etc.).
4. **Corrélation** (avec autres IOCs, groupes connus).
5. **Diffusion** (interne, MISP communauté).
6. **Action** (blocking, alerting).

## 74.9 Limites et renvoi

L'OSINT pour CTI couvre la **collecte et corrélation** publique. La profondeur (analyse intrusion, reverse engineering, attribution étatique forensique) est dans le cours CTI dédié.

## 74.10 Synthèse

L'OSINT contribue substantiellement à la CTI. Pour les analystes CTI, l'OSINT est une discipline de référence. Pour les analystes OSINT, la CTI est un domaine d'application majeur.

## 74.11 Threat hunting via OSINT

Le **threat hunting** est la recherche proactive de menaces. L'OSINT y contribue par :

**Identification d'IOCs précurseurs.** Monitoring des forums et canaux Telegram cybercriminels pour repérer dès leur émergence : nouveaux domaines de phishing, nouveaux samples malware, nouveaux services offerts (RaaS, accès initial).

**Surveillance d'acteurs.** Suivi des profils, alias, et infrastructures d'acteurs identifiés. Détection des changements de patterns.

**Anticipation de campagnes.** Identification de TTPs émergents avant qu'ils ne se généralisent. Cross-référence avec rapports vendeurs (CrowdStrike, Mandiant, Microsoft, Group-IB).

**Recherches dans les leaks.** Identification précoce de credentials compromis de l'organisation cible avant exploitation par adversaire.

## 74.12 Méthodologie d'analyse de campagne

Pour caractériser une campagne d'attaque observée :

1. **Collecte initiale.** IOCs depuis logs SOC, EDR, sandboxes.
2. **Enrichissement OSINT.** VirusTotal, abuse.ch, AlienVault OTX pour contexte.
3. **Pivots infrastructure.** Tous domaines / IPs liées via passive DNS, certificats, registrar.
4. **Pivots TTPs.** Comparaison à campagnes connues (MITRE ATT&CK, rapports publics).
5. **Hypothèses acteurs.** Attribution probable avec ACH (Ch.79).
6. **Cotation et publication.** Partage MISP communauté si TLP permet.

## 74.13 Acteurs majeurs CTI 2026 à connaître

**Groupes étatiques principaux documentés.**

**Russie.**

- **APT28 (Fancy Bear, GRU)** : opérations politiques et défense.
- **APT29 (Cozy Bear, SVR)** : espionnage long terme.
- **Sandworm (GRU)** : opérations destructives, infrastructures critiques.
- **Turla** : espionnage diplomatique.

**Chine.**

- **APT41 (Winnti, Barium)** : double activité espionnage et cybercrime.
- **APT10 (MenuPass)** : MSP supply chain attacks.
- **Volt Typhoon** : infrastructures critiques US.
- **Salt Typhoon** : télécoms (révélé 2024-2025).

**Iran.**

- **APT35 (Charming Kitten)** : journalistes, dissidents.
- **APT34 (OilRig)** : industrie pétrolière.
- **MuddyWater** : opérations diversifiées.

**Corée du Nord.**

- **Lazarus Group** : monétaire, ransomware, hacks crypto.
- **APT38** : finance.
- **Kimsuky** : espionnage.

**Cybercriminels.**

- **LockBit** (ransomware, opération en cours après tentative démantèlement 2024).
- **BlackCat / ALPHV** (ransomware).
- **Conti** (dissous 2022, mais successeurs : Royal, Akira, etc.).
- **FIN groups** : cybercrime financier.

**Sources de référence.** MITRE ATT&CK Groups, MISP Galaxy, ThaiCERT APT, CrowdStrike adversary list, Mandiant APT reports, Microsoft Threat Intelligence reports.

## 74.14 Frameworks d'analyse

**Diamond Model (Caltagirone, Pendergast, Betz, 2013).** Quatre features : adversary, capability, infrastructure, victim. Permet structurer analyse intrusion.

**Cyber Kill Chain (Lockheed Martin, 2011).** Sept phases : reconnaissance, weaponization, delivery, exploitation, installation, command & control, actions on objectives. Plus orienté détection.

**MITRE ATT&CK.** Le plus utilisé en 2026. Catalogue exhaustif TTPs adverses, par technique, par groupe, par plateforme. Mises à jour régulières.

**Unified Kill Chain (Pols, 2017).** Synthèse Diamond + Kill Chain + MITRE.

**Pyramid of Pain (Bianco, 2013).** Hiérarchie des IOCs par difficulté pour l'adversaire (hashs faciles à changer, TTPs très difficiles).

## 74.15 Workflow CTI complet

**Cycle de renseignement CTI.**

1. **Direction.** Quelles questions stratégiques ? Quels actifs à protéger ?
2. **Collecte.** OSINT + feeds payants + interne (logs, sandboxes).
3. **Traitement.** Normalisation, déduplication, enrichissement.
4. **Analyse.** Caractérisation, attribution, prédictions.
5. **Diffusion.** Bulletins, alertes, briefings.
6. **Feedback.** Boucle vers direction.

**Maturité CTI.**

- **Tactical.** IOCs, signatures, alertes opérationnelles.
- **Operational.** Campagnes, modes opératoires.
- **Strategic.** Tendances long terme, attribution étatique, contexte géopolitique.

## 74.16 Limites et renvoi

L'OSINT pour CTI couvre la **collecte et corrélation** publique. La profondeur (analyse intrusion, reverse engineering, attribution étatique forensique, threat hunting on-prem) est dans le **cours CTI dédié** (à venir dans la bibliothèque).

-----
