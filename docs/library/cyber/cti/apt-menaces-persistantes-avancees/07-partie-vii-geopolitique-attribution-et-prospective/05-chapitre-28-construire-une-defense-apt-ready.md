---
title: Chapitre 28 — Construire une défense APT-ready
source: Cyber/01 CTI & renseignement/Menace cyber/APT — menaces persistantes avancées.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie VII — Géopolitique, attribution et prospective
  - index.md
---

> **Note sur ce chapitre.** Ce chapitre synthétise les principes de défense spécifiques aux APT. Il ne reproduit pas un cours de SOC ou d’Incident Response — il se concentre sur ce qui distingue la défense contre les APT étatiques de la défense générale.

## 28.1 Principes : assume breach, defense in depth, Zero Trust

La défense APT-ready repose sur trois principes structurants.

**Assume breach** : partir du principe que **l’adversaire est probablement déjà à l’intérieur**. Cette posture change tout — les efforts ne se limitent pas à empêcher l’entrée (prévention), mais s’étendent à la détection précoce, au containment rapide, à l’éradication efficace, et à la résilience.

La justification de l’« assume breach » : face à des acteurs comme Volt Typhoon (LotL exclusif, zéro malware), APT29 (abus cloud/identity sophistiqué), Turla (piggybacking, rootkits kernel), la prévention seule ne suffit pas. Les défenseurs doivent supposer que tôt ou tard, un acteur suffisamment motivé et ressourcé **entrera**. L’objectif devient alors de **limiter l’impact** et d’**écourter le dwell time**.

**Defense in depth** : multiples couches de défense indépendantes, de manière à ce qu’une défaillance à une couche soit compensée par les suivantes. Couches typiques : sécurité périmétrique, endpoint, identity, cloud/SaaS, réseau interne, applicatif, données, détection/réponse. Un attaquant qui franchit une couche doit en franchir d’autres avant d’atteindre les données critiques.

**Zero Trust** : ne pas faire confiance par défaut aux utilisateurs, appareils, ou applications, même à l’intérieur du périmètre. Chaque accès est authentifié, autorisé, et validé. Le concept a été formalisé par Forrester (John Kindervag, 2010) et adopté largement — **NIST SP 800-207** (Zero Trust Architecture, 2020) en donne un cadre de référence.

Application Zero Trust : MFA résistant au phishing pour tous les accès, conditional access basé sur le contexte, micro-segmentation réseau, verification continue plutôt que session persistante, principle of least privilege strict.

## 28.2 Contrôles minimum viables

La défense APT-ready repose sur un ensemble de **contrôles minimum viables** — pratiques sans lesquelles tout le reste est compromis. Priorisation proposée.

**Priorité 0 — Prérequis absolus** :

- **MFA résistant au phishing** sur tous les comptes (FIDO2 / WebAuthn). Exclure TOTP SMS/appel (contournables par AitM).
- **Privileged Access Management (PAM)** : rotation des credentials privilégiés, sessions auditées, just-in-time pour les accès critiques.
- **EDR déployé partout** : endpoints et serveurs (incluant les serveurs de production). Les serveurs sans EDR sont les pivots préférés des attaquants.
- **Patching des edge devices en moins de 48h** sur les CVE exploitées activement (référence CISA KEV).

**Priorité 1 — Base solide** :

- **Segmentation réseau** : IT/OT, zones sensibles isolées, segmentation micro-services si possible.
- **Durcissement Active Directory** : tiering strict des comptes, limitation des privilèges, monitoring des changements critiques (groupes admin, GPO, trusts), protection KRBTGT.
- **Monitoring cloud / identity** : visibilité sur Azure AD/Entra, applications OAuth, sign-ins anormaux, changements de configuration.
- **Backup hors ligne testé** : backup offline (non joignable depuis le réseau), testé régulièrement par restore réel, couvrant systèmes et données critiques.
- **Plan IR formalisé et exercé** : playbooks documentés, équipe identifiée, retainer IR externe si besoin, exercices réguliers.

**Priorité 2 — Maturité** :

- **Threat hunting proactif** : équipe ou prestataire dédié, cycles réguliers, guidé par la CTI des acteurs pertinents.
- **Purple team** : exercices réguliers combinant red team (simulation TTP APT) et blue team (détection).
- **Intégration CTI** : ingestion de renseignement actionnable, corrélation avec la télémétrie.
- **Visibilité OT** (si applicable) : passive monitoring sur les segments industriels.
- **Gestion de la supply chain** : évaluation des prestataires, SBOM, monitoring des intégrations.

## 28.3 Visibilité minimum viable

Sans visibilité, la détection est impossible. Les **sources de télémétrie** essentielles :

**Endpoints** :

- **Sysmon** : logs détaillés des process, connexions réseau, modifications de fichiers, chargements de DLL. Configuration de référence : Olaf Hartong Sysmon config (GitHub, open source, largement adopté).
- **PowerShell ScriptBlock logging** : tous les scripts PowerShell exécutés sont loggés.
- **EDR** : détections comportementales, télémétrie détaillée.
- **Windows Security events** : authentifications, changements de comptes, privilèges.

**Réseau** :

- **DNS** : résolutions sortantes, détection des domaines malveillants connus, détection des patterns (beaconing).
- **Firewall et proxy** : flux sortants, tentatives d’exfiltration, connexions vers infrastructure suspecte.
- **Flow data (NetFlow/IPFIX)** : vue agrégée des communications, détection d’anomalies volumétriques.
- **IDS/NDR** : détection d’intrusion réseau, analyse comportementale.

**Identity / Cloud** :

- **Azure AD / Entra sign-in logs** : qui se connecte, depuis où, avec quel contexte.
- **Audit logs** : changements de configuration, consents OAuth, rôles modifiés.
- **Application logs** : pour les SaaS critiques (M365, Google Workspace, Salesforce, etc.).

**Email** :

- **Email gateway logs** : messages reçus/envoyés, détections phishing, blocages.
- **Messagerie interne** : monitoring des messages à haut risque (pièces jointes, liens externes, thèmes sensibles).

**Sources OT** (si applicable) :

- **Passive monitoring OT** (Claroty, Dragos, Nozomi, Microsoft Defender for IoT).
- **Logs des engineering workstations**.
- **Logs des HMI, historian, SCADA applications**.

**Centralisation** : tout remonte vers un **SIEM** centralisé (Splunk, QRadar, Sentinel, Elastic, Chronicle, Exabeam) qui permet corrélation cross-sources. Sans SIEM, chaque source est un silo et les corrélations (signe d’une APT) sont invisibles.

## 28.4 Détection TTP-driven vs IoC-driven

La détection moderne doit être **TTP-driven**, pas seulement IoC-driven.

**Détection IoC-driven (limitée)** : liste de hashes, IP, domaines connus comme malveillants. Facile à implémenter, efficace contre les malwares connus, **inefficace contre les APT** qui adaptent leurs IoC.

**Détection TTP-driven (recommandée)** : règles qui détectent les **comportements** plutôt que les signatures statiques. Exemples :

- « Un processus PowerShell exécuté par MS Word est suspect » (détecte les macros malveillantes).
- « Une connexion RDP sortante depuis un serveur vers une IP externe est suspecte ».
- « Un compte admin qui se connecte à un système où il ne s’est jamais connecté avant est suspect ».
- « Une connexion Azure AD depuis un pays où l’utilisateur ne travaille pas est suspecte ».

**Outils** :

- **Sigma rules** : format ouvert pour les règles de détection SIEM. Bibliothèque open source disponible.
- **Elastic detections, Splunk ES, Microsoft Sentinel analytics** : règles natives des SIEM.
- **ATT&CK mapping** : mapper les détections aux techniques MITRE ATT&CK pour visualiser la couverture.

**Detection engineering** : discipline de construction et maintenance des règles de détection. Cycle : hypothèse de TTP, développement de règle, test, déploiement, tuning par feedback terrain. Les équipes SOC matures ont des detection engineers dédiés.

## 28.5 Le containment APT : scope avant contenir

Face à une APT détectée, la règle critique est : **scope avant de contenir**.

**Pourquoi** : une APT sophistiquée a des **accès redondants** (plusieurs mécanismes de persistence, comptes backdoor, plusieurs hosts compromis). Si on contient un seul accès (isoler une machine, désactiver un compte), l’attaquant **active immédiatement ses accès redondants** et disparaît — tout en étant alerté que la détection a eu lieu. Résultat : perte de visibilité, réinfection via TTP modifiées, dwell time rallongé.

**Méthode recommandée** :

1. **Détecter** une présence APT (un signe).
1. **Ne pas agir visiblement** — préserver l’invisibilité pour l’attaquant.
1. **Scope** : identifier tous les systèmes, comptes, et mécanismes compromis. Threat hunting actif guidé par les premières observations. Cette phase peut durer des jours à des semaines.
1. **Planifier le containment coordonné** : qui fait quoi, quand, dans quel ordre.
1. **Containment simultané** : désactivation de **tous** les accès en une fenêtre courte (idéalement quelques heures), **de manière coordonnée**. L’attaquant ne peut plus pivoter vers des accès redondants parce qu’ils sont tous coupés simultanément.
1. **Éradication** : nettoyage des mécanismes de persistence, reset des credentials, reconstruction des systèmes compromis.
1. **Monitoring renforcé post-éradication** : l’attaquant tentera probablement de revenir — détection des tentatives de réentrée.

**Outils** : EDR modernes permettent la réponse coordonnée (isolation réseau de multiple endpoints en une action, désactivation de comptes en masse). SOAR (Security Orchestration, Automation and Response) pour orchestrer les playbooks complexes.

**Retainer IR** : avoir un prestataire IR contractualisé en amont permet une réponse rapide sans négocier les termes pendant la crise. Retainers Mandiant, CrowdStrike, Kroll, Unit 42, Sophos, et équivalents européens sont la norme pour les grandes organisations.

## 28.6 Purple team orienté APT

Le **purple team** combine red team (simulation d’attaque) et blue team (détection/réponse) en exercices collaboratifs. Appliqué aux APT, il vise à **valider** les détections face aux TTP des acteurs pertinents.

**Approche** :

- Identifier les acteurs pertinents pour l’organisation (sectoriels, géographiques).
- Cataloguer leurs TTP documentées (ATT&CK Groups, rapports CTI).
- Reproduire ces TTP dans un environnement contrôlé.
- Vérifier si le SOC détecte chaque TTP avec quelle latence.
- Identifier les gaps et les corriger (nouvelles règles de détection, nouvelles sources de télémétrie).

**Frameworks d’émulation** :

- **Atomic Red Team** (Red Canary, open source) : bibliothèque de tests atomiques mappés sur ATT&CK.
- **CALDERA** (MITRE) : plateforme d’émulation adversaire automatisée.
- **Red Canary AtomicTestHarnesses** : tests paramétrés.
- **Vectr** : plateforme de gestion des exercices purple team.
- **APT Emulation Plans** (MITRE CTID) : plans d’émulation d’acteurs spécifiques (APT29, FIN6, menuPass/APT10, Sandworm, Carbanak, Turla).

**Cadence recommandée** : exercices réguliers (trimestriels pour les grandes organisations), chaque exercice ciblant un acteur ou un ensemble de TTP spécifique.

**Bénéfices** :

- Validation empirique des détections (vs théorique).
- Formation des équipes blue sur les TTP réelles.
- Priorisation des investissements de détection sur les gaps identifiés.
- Documentation des capacités de détection pour la direction et les auditeurs.

## 28.7 Exercices de simulation (tabletop et au-delà)

Les exercices testent la **réponse organisationnelle**, pas seulement les capacités techniques.

**Niveaux** :

- **Tabletop** : discussion autour d’un scénario. Durée 2-4h. Participants : CISO, SOC, IR, juridique, communication, direction. Teste la coordination, les décisions, les procédures.
- **Fonctionnel** : simulation plus approfondie avec actions techniques sur environnement de test.
- **Full-scale / live** : exercice sur systèmes réels (en environnement contrôlé) avec injection de scenarios réels.

**Scénarios APT recommandés** :

**Tabletop 1 — « APT29 a compromis votre Azure AD via phishing OAuth »**

- J0 : alerte sign-in suspect depuis un pays inhabituel sur un compte admin.
- J+1 : règle de forwarding inbox créée par le compte, redirigeant des emails vers externe.
- J+3 : exfiltration détectée de SharePoint via Graph API, ~500 Go de données.
- J+5 : découverte d’une application OAuth avec permissions admin et tokens SAML forgés via ADFS compromis.
- Questions clés : Quand escaladez-vous à la direction ? Qui informez-vous (clients, autorités, ANSSI) ? Contenez-vous immédiatement (risque perdre visibilité) ou scopez-vous d’abord ?

**Tabletop 2 — « Ransomware BlackBasta avec précurseur APT »**

- J0 : déploiement ransomware massif, des centaines d’endpoints chiffrés, note de rançon sur plusieurs serveurs.
- Investigation révèle que l’accès initial a été vendu par un Initial Access Broker qui l’avait obtenu 6 mois plus tôt via une compromission Citrix.
- L’IAB avait probablement aussi vendu l’accès à un acteur étatique qui l’a utilisé pour d’autres opérations (exfiltration de propriété intellectuelle) avant le déploiement ransomware.
- Questions clés : comment discriminer cybercrime vs APT dans la réponse ? Qui notifier (ANSSI pour les OIV, CNIL pour les données personnelles, parquet pour les infractions pénales) ? Comment gérer la communication externe ?

**Tabletop 3 — « Pré-positionnement OT détecté sans action destructive »**

- Le SOC détecte des TTP compatibles avec Volt Typhoon/Sandworm dans l’environnement OT.
- L’attaquant est présent depuis probablement 3+ mois, pas d’exfiltration visible, pas d’action destructive.
- Questions clés : éradiquez-vous immédiatement (risque de perdre le renseignement sur l’adversaire) ou surveillez-vous (risque de laisser une menace active) ? Qui prend cette décision ? Comment se coordonne-t-on avec l’ANSSI ? Comment communique-t-on (ou pas) publiquement ?

Ces tabletops révèlent régulièrement des gaps organisationnels : procédures d’escalade floues, absence de contacts établis avec les autorités, mauvais partage d’information interne, gaps de communication avec la direction.

## 28.8 Le partage d’information : ISAC, CSIRT, coordination européenne

Le **partage d’information** est un pilier de la défense collective contre les APT.

**Niveaux de partage** :

- **Intra-organisation** : entre équipes (SOC, IR, threat intel, IT, métiers).
- **Sectoriel** : ISAC (Ch.23) — partage des IoC, TTP, tendances avec les pairs du même secteur.
- **National** : CERT national (CERT-FR, CERT-DE, NCSC, etc.), autorités (ANSSI, BSI).
- **International** : FIRST (Forum of Incident Response and Security Teams), coordination Five Eyes, UE.

**Règles de partage — TLP (Traffic Light Protocol)** :

- **TLP:RED** : strictement limité aux destinataires nommés.
- **TLP:AMBER** : limité à l’organisation et partenaires directs.
- **TLP:GREEN** : partage dans la communauté pertinente.
- **TLP:CLEAR** : public sans restriction.

**Outils de partage** :

- **MISP** (Malware Information Sharing Platform) : plateforme open source de partage d’indicateurs structurés.
- **STIX / TAXII** : formats standards pour le partage de threat intelligence.
- **ISAC portals** : chaque ISAC a ses mécanismes de partage.

**Bénéfice collectif** : un IoC partagé par un membre protège potentiellement tous les autres. L’inverse : ne pas partager par crainte d’exposer l’incident laisse les pairs vulnérables.

**Obligations légales** : NIS 2 impose des notifications aux autorités sous 24h (early warning) et 72h (détaillée) pour les incidents significatifs. RGPD impose la notification CNIL sous 72h pour les violations de données personnelles.

## 28.9 Former les équipes : CTI-driven defense

La défense APT-ready n’existe pas sans équipes **formées et motivées**. Quelques principes.

**Recrutement et rétention** : les profils cyber sont rares et chers. La rétention dépend de facteurs non-salariaux (défis intéressants, formation continue, reconnaissance, culture d’équipe, flexibilité). Les RSSI qui traitent leurs équipes cyber comme un investissement stratégique retiennent mieux.

**Formation continue** : certifications (SANS, Offensive Security, ISC2, ISACA), conférences (Black Hat, DEF CON, SSTIC, FIC, Botconf, RSA), labs d’entraînement (Hack The Box, TryHackMe, RangeForce), lectures (rapports Mandiant, CrowdStrike, Microsoft, Dragos, blogs spécialisés).

**CTI-driven mindset** : comprendre les acteurs avant de défendre contre les acteurs. Les équipes qui lisent régulièrement la CTI (rapports publics, threat intel d’abonnement, partages ISAC) savent ce contre quoi elles défendent. Les équipes qui ne lisent que leur SIEM ne savent pas.

**Exercices et apprentissage continu** : les tabletops, purple teams, CTF internes entretiennent les compétences. Une équipe qui ne s’entraîne pas perd ses capacités.

**Culture d’apprentissage des incidents** : après chaque incident (réel ou simulé), **post-mortem blameless** — analyse des faits, identification des causes systémiques, actions correctives documentées. Les équipes qui cachent les erreurs apprennent moins que celles qui les exposent et corrigent.

**Relation avec la direction** : le CISO doit pouvoir parler métier, budget, et risque, pas seulement technique. La défense APT-ready exige des investissements que la direction doit comprendre et soutenir — d’où l’importance de traduire les menaces APT en langage d’impact business compréhensible par le non-technique.

-----
