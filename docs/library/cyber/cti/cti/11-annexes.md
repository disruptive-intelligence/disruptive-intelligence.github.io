---
title: Annexes
source: Cyber/01_CTI/CTI.md
note: CTI
up:
- - CTI
  - index.md
---

---


## Annexe A — Glossaire CTI

| Terme | Définition |
|-------|-----------|
| **ACH** | Analysis of Competing Hypotheses — technique analytique structurée pour tester des hypothèses concurrentes |
| **APT** | Advanced Persistent Threat — acteur de menace généralement étatique, sophistiqué et persistant |
| **ATT&CK** | Framework MITRE décrivant les tactiques, techniques et procédures des attaquants |
| **Attribution** | Processus de liaison d'une activité malveillante à un acteur, groupe, ou État |
| **Beaconing** | Pattern de communication périodique entre un malware et son serveur C2 |
| **C2** | Command and Control — infrastructure de commande d'un malware |
| **Campaign** | Série d'attaques liées par un objectif, une période, ou une infrastructure commune |
| **CISA KEV** | Known Exploited Vulnerabilities catalog — référence des vulnérabilités exploitées ITW |
| **Cluster** | Regroupement d'activités malveillantes liées, sans attribution formelle à un acteur |
| **CTI** | Cyber Threat Intelligence — discipline de renseignement sur les menaces cyber |
| **CVSS** | Common Vulnerability Scoring System — score de sévérité technique des vulnérabilités |
| **Diamond Model** | Modèle d'analyse d'intrusion à 4 sommets (adversaire, capacité, infrastructure, victime) |
| **Dissémination** | Phase de diffusion du renseignement produit aux consommateurs |
| **DLL sideloading** | Technique de persistence par placement de DLL malveillante dans le répertoire d'un exécutable légitime |
| **EPSS** | Exploit Prediction Scoring System — probabilité d'exploitation d'une CVE dans les 30 jours |
| **False flag** | Indices délibérément plantés pour brouiller l'attribution (imiter un autre acteur) |
| **Feed** | Flux automatisé de données de renseignement (IoC, TTP, rapports) |
| **GAP analysis** | Croisement des TTP des acteurs pertinents avec la couverture de détection actuelle |
| **Hunting** | Recherche proactive de menaces non détectées, souvent guidée par des hypothèses CTI |
| **IAB** | Initial Access Broker — acteur vendant des accès réseau compromis |
| **Infostealer** | Malware volant automatiquement credentials, cookies, et données de navigateur |
| **Intrusion set** | Ensemble d'activités malveillantes liées attribuées à un acteur (terminologie MITRE) |
| **IoA** | Indicator of Attack — signal comportemental indiquant une attaque en cours |
| **IoC** | Indicator of Compromise — artefact technique observé après une compromission |
| **IR** | Intelligence Requirement — question de renseignement dérivée d'un PIR |
| **ISAC** | Information Sharing and Analysis Center — structure de partage sectoriel |
| **ITW** | In the Wild — exploitation active d'une vulnérabilité dans la nature |
| **Kill Chain** | Modèle Lockheed Martin des 7 phases d'une intrusion |
| **Living off the Land (LotL)** | Utilisation d'outils légitimes du système pour éviter la détection |
| **LOLBins** | Living Off the Land Binaries — binaires légitimes détournés (PowerShell, certutil, etc.) |
| **Malpedia** | Base de données de référence pour les mappings de noms d'acteurs et de malwares |
| **MISP** | Malware Information Sharing Platform — plateforme open source de partage CTI |
| **MITRE ATT&CK** | Matrice des comportements adverses (tactiques, techniques, sous-techniques) |
| **Navigator** | Outil web MITRE pour visualiser les TTP sur la matrice ATT&CK |
| **NIS 2** | Directive européenne sur la sécurité des réseaux et systèmes d'information (v2) |
| **OIV** | Opérateur d'Importance Vitale — organisation critique désignée par l'État français |
| **OpenCTI** | Plateforme open source de gestion de renseignement cyber (Filigran) |
| **Passive DNS** | Historique des résolutions DNS — révèle les changements d'infrastructure |
| **PIR** | Priority Intelligence Requirement — question stratégique guidant la CTI |
| **Procedure** | Implémentation spécifique d'une technique ATT&CK par un acteur (le « comment exactement ») |
| **PSO** | Private Sector Offensive — entreprise vendant des capacités d'espionnage cyber |
| **Pyramid of Pain** | Hiérarchie des indicateurs par le coût infligé à l'attaquant (David Bianco) |
| **RaaS** | Ransomware-as-a-Service — modèle franchisé de distribution de ransomware |
| **Red Hat Analysis** | TAS consistant à se mettre dans la peau de l'adversaire |
| **Sigma** | Format de règle de détection universel, convertible en SPL/KQL/EQL |
| **SOAR** | Security Orchestration, Automation and Response — plateforme d'automatisation |
| **STIX** | Structured Threat Information eXpression — format standard de structuration CTI |
| **Supply chain** | Compromission via un fournisseur de confiance (logiciel ou prestataire) |
| **TAS** | Techniques Analytiques Structurées — méthodes formelles de raisonnement analytique |
| **TAXII** | Trusted Automated eXchange of Indicator Information — protocole de transport STIX |
| **Threat Actor** | Groupe identifié avec un sponsor présumé |
| **TIP** | Threat Intelligence Platform — plateforme de gestion du renseignement |
| **TLP** | Traffic Light Protocol — protocole de classification de la diffusion (RED/AMBER/GREEN/CLEAR) |
| **Tradecraft** | Ensemble des choix opérationnels d'un acteur (TTP + OPSEC + habitudes) |
| **TTP** | Tactics, Techniques, and Procedures — comportements opérationnels d'un attaquant |
| **UNC** | Uncategorized — préfixe pour un cluster d'activité non attribué (convention Mandiant/interne) |
| **Victimologie** | Étude des profils de victimes d'un acteur (secteur, géographie, taille) |
| **Vuln intel** | Vulnerability Intelligence — renseignement sur les vulnérabilités exploitées |

---


## Annexe B — Taxonomie des sources CTI

| Source | Type | Fiabilité typique | Couverture | Coût | Biais principal |
|--------|------|-------------------|-----------|------|----------------|
| CERT-FR / CISA advisories | OSINT gouvernemental | A (très fiable) | Vulnérabilités, campagnes majeures | Gratuit | Biais de seuil (seules les menaces majeures sont publiées) |
| Rapports Mandiant / CrowdStrike | OSINT commercial | B (fiable) | APT, campagnes, TTP | Gratuit (rapports publics) | Biais commercial (dramatisation), biais de couverture (clients) |
| Blogs de chercheurs (Twitter/X) | OSINT individuel | C (variable) | Découvertes fraîches, IoC | Gratuit | Non vérifié, bruit élevé, égo |
| Recorded Future / Intel 471 | Commercial (plateforme) | B (fiable) | Large (dark web, OSINT, technique) | 50-200K$/an | Couverture inégale selon les régions |
| Flashpoint / Cybersixgill | Commercial (dark web) | B-C | Dark web, forums, Telegram | 50-150K$/an | Couverture des forums fermés limitée |
| Logs SOC / IR post-mortems | Interne | A (première main) | Organisation spécifique | Inclus | Biais de sélection (seuls les incidents détectés) |
| Vuln management scans | Interne | A-B | Surface d'attaque de l'organisation | Inclus | Couverture partielle (assets non scannés) |
| ISAC sectoriel | Communautaire | B-C (variable) | Secteur spécifique | Adhésion (~5-30K$/an) | Biais de contribution (certains membres partagent peu) |
| FIRST / TF-CSIRT | Communautaire | B | Cross-sectoriel | Adhésion | Réciprocité requise |
| Dark web (forums, marchés) | Dark web | D-E (non fiable par défaut) | Cybercriminalité, ventes de données/accès | Variable | Intoxication, scams, recyclage |
| Passive DNS / CT logs | Technique | B (objectif) | Infrastructure | Gratuit-50K$/an | Couverture partielle, données historiques |
| Honeypots / Sinkholes | Technique | B (première main) | Attaques automatisées, botnets | Infrastructure | Biais d'attraction (que ce qui attaque le honeypot) |

---


## Annexe C — Templates de livrables CTI

### Template Flash Alert

```
🔴 FLASH ALERT — [TITRE]
TLP: [RED/AMBER/GREEN]    Date: [date]    Analyste: [nom]    Ref: [code]

RÉSUMÉ (3 lignes max)
[Quoi] — [Impact] — [Action immédiate]

DÉTAIL
  Événement déclencheur : [description]
  Source : [source, fiabilité]
  Impact pour l'organisation : [évaluation]
  Niveau de confiance : [élevé/modéré/faible]

ACTIONS IMMÉDIATES
  1. [action technique — responsable — délai]
  2. [action technique — responsable — délai]

IoC (si applicable)
  [hash / domaine / IP — type — contexte]

SUIVI
  Prochaine mise à jour : [date/heure]
```


### Template Note Analytique CTI

```
NOTE ANALYTIQUE — [TITRE]
Classification : [TLP]    Date : [date]    Analyste : [nom]    Ref : [code]

1. RÉSUMÉ EXÉCUTIF (5 lignes max)
   Conclusion — Niveau de confiance — Implication — Action recommandée

2. CONTEXTE
   PIR adressé — Événement déclencheur — Sources consultées — Limitations

3. FAITS OBSERVÉS
   [Fait 1 — source (fiabilité) — date]
   [Fait 2 — source (fiabilité) — date]

4. ANALYSE
   Hypothèses testées :
     H1 : [description — évidences pour/contre — évaluation]
     H2 : [description — évidences pour/contre — évaluation]
   Corrélations : [multi-sources, convergences]
   Raisonnement : [explicite, traçable]

5. CONCLUSIONS
   [Conclusion 1 — niveau de confiance : [élevé/modéré/faible]]
   [Conclusion 2 — niveau de confiance]
   Ce qui n'a pas pu être déterminé : [inconnues explicites]

6. IMPLICATIONS ET RECOMMANDATIONS
   Technique : [détections, IoC, hunts]
   Organisationnel : [posture, audit, formation]
   Stratégique : [communication, notification, budget]

7. INDICATEURS DE RÉVISION
   [Ce qui changerait la conclusion si observé]

ANNEXES
   A. IoC complets (format STIX)
   B. Mapping ATT&CK
   C. Références sources
```


### Template Profil d'Acteur

```
PROFIL D'ACTEUR — [NOM / CLUSTER]
Version : [X.Y]    Dernière MàJ : [date]    Analyste : [nom]

IDENTITÉ
  Nom(s) : [nom principal + alias vendors]
  Statut : [APT confirmé / cluster non attribué / FIN / etc.]
  Première observation : [date]

ATTRIBUTION
  Sponsor présumé : [pays / service — niveau de confiance]
  Évidences d'attribution : [résumé]
  Hypothèses alternatives : [résumé]

OBJECTIFS
  [Espionnage / sabotage / financier / pré-positionnement — déduit de...]

VICTIMOLOGIE
  Secteurs : [liste]
  Géographies : [liste]
  Profil type : [taille, type d'organisation]

TTP (MITRE ATT&CK)
  [Tableau tactique | technique | sous-technique | procédure spécifique]

OUTILS
  Custom : [liste]
  Commodity : [liste]
  LOLBins : [liste]

INFRASTRUCTURE
  Patterns : [registrars, ASN, hébergement, certificats]
  IoC actifs : [domaines, IP — avec dates de validité]

CAMPAGNES CONNUES
  [Campagne 1 — date — victimes — résumé]
  [Campagne 2 — etc.]

ÉVOLUTION
  [Comment le tradecraft a changé dans le temps]

SOURCES
  [Liste des rapports et sources utilisés pour ce profil]
```


---


## Annexe D — Cheat sheets analytiques

### Matrice ACH vierge

| Évidence (source, fiabilité) | H1 : _____ | H2 : _____ | H3 : _____ | H4 : _____ |
|------------------------------|:---:|:---:|:---:|:---:|
| E1 : _____ | C / I / N | C / I / N | C / I / N | C / I / N |
| E2 : _____ | | | | |
| E3 : _____ | | | | |
| **Total incohérences** | | | | |
| **Conclusion** | L'hypothèse avec le MOINS d'incohérences est retenue |

C = Cohérent, I = Incohérent, N = Non applicable

### Grille Admiralty (évaluation source × information)

**Fiabilité de la source :**
A = Complètement fiable (historique parfait) | B = Habituellement fiable | C = Assez fiable | D = Habituellement non fiable | E = Non fiable | F = Inévaluable

**Crédibilité de l'information :**
1 = Confirmée (corroborée) | 2 = Probablement vraie | 3 = Possiblement vraie | 4 = Douteuse | 5 = Improbable | 6 = Inévaluable

### Checklist des biais cognitifs

- [ ] **Confirmation :** ai-je cherché ce qui contredit ma conclusion ?
- [ ] **Disponibilité :** suis-je influencé par le dernier rapport médiatisé ?
- [ ] **Anchoring :** suis-je accroché à la première hypothèse ?
- [ ] **Mirror imaging :** est-ce que je prête ma logique à l'adversaire ?
- [ ] **Groupthink :** l'équipe a-t-elle contesté la conclusion ?
- [ ] **Attribution hâtive :** ai-je testé les hypothèses alternatives ?
- [ ] **Circularité :** mes « sources multiples » sont-elles réellement indépendantes ?

### Workflow CTI-to-Detection

```
1. CTI identifie TTP pertinent (acteur × PIR)
      ↓
2. Vérification couverture actuelle (règle existante ?)
      ↓ (si non couvert)
3. Rédaction règle Sigma (procédure spécifique, pas technique générique)
      ↓
4. Test sur logs historiques (rétro-hunt)
      ↓
5. Déploiement en production
      ↓
6. Monitoring FP + tuning
      ↓
7. Feedback → CTI (résultats, gaps, nouveaux signaux)
```


---


## Annexe E — Outils de référence CTI

| Catégorie | Outil | Gratuit/Payant | Usage principal |
|-----------|-------|---------------|----------------|
| **TIP** | MISP | Gratuit (OSS) | Partage d'IoC, communauté, intégration SIEM |
| **TIP** | OpenCTI | Gratuit (OSS) / Payant (SaaS) | Gestion CTI analytique, graphe de relations, STIX natif |
| **TIP** | ThreatConnect | Payant | TIP intégré avec SOAR, enrichissement |
| **Feed commercial** | Recorded Future | Payant | Couverture large, scoring, alerting |
| **Feed commercial** | Mandiant Advantage | Payant | APT, campagnes, IR context |
| **Feed commercial** | Intel 471 | Payant | Dark web, cybercriminalité, adversary intelligence |
| **Feed commercial** | Flashpoint | Payant | Dark web, forums, Telegram |
| **Feed OSINT** | AlienVault OTX | Gratuit | Feeds communautaires d'IoC |
| **Feed OSINT** | Abuse.ch (URLhaus, MalwareBazaar) | Gratuit | Malware, URLs malveillantes |
| **Enrichissement** | VirusTotal | Freemium | Multi-scanner, relations, sandbox |
| **Enrichissement** | Shodan | Freemium | Recherche d'infrastructure exposée |
| **Enrichissement** | PassiveTotal (RiskIQ) | Payant | Passive DNS, WHOIS, certificats |
| **Enrichissement** | GreyNoise | Freemium | Mass scanning, exploitation de CVE |
| **Vuln intel** | CISA KEV | Gratuit | Vulnérabilités exploitées confirmées |
| **Vuln intel** | EPSS (FIRST) | Gratuit | Probabilité d'exploitation |
| **Visualisation** | ATT&CK Navigator | Gratuit | Visualisation TTP, gap analysis |
| **Visualisation** | Maltego | Payant | Graphe de relations, transforms |
| **Partage** | TAXII server | Gratuit (OSS) | Transport automatisé de STIX |
| **Détection** | Sigma (rules) | Gratuit (OSS) | Format universel de règles de détection |
| **Détection** | Chainsaw | Gratuit (OSS) | Détection Sigma sur Event Logs |
| **SOAR** | Cortex XSOAR | Payant | Orchestration, playbooks automatisés |
| **SOAR** | Shuffle | Gratuit (OSS) | Orchestration open source |

---


## Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Cours complémentaires |
|-----------|----------------|----------------------|
| Processus analytique CTI | **Ce cours (CTI)** | — |
| Acteurs étatiques / APT | **Cours APT** | CTI (Ch.3 panorama), Écosystèmes (Ch.21 zones grises) |
| Économie cybercriminelle | **Cours Écosystèmes** | CTI (Ch.3 cybercriminalité), Dark Web (marchés, forums) |
| Dark web (navigation, investigation) | **Cours Dark Web** | CTI (Ch.6 sources dark web), Écosystèmes (Ch.8-10 espaces) |
| Incident Response | **Cours IR** | CTI (Ch.23 CTI↔IR) |
| Forensic numérique | **Cours Forensic** | CTI (Ch.23 artefacts → CTI) |
| Détection SOC | **Cours SOC** | CTI (Ch.20 CTI-to-Detection, Ch.22 Hunting) |
| OSINT | **Cours OSINT Mastery** | CTI (Ch.6 sources OSINT) |
| Active Directory | **Cours AD** | CTI (Ch.16 TTP AD), IR (Ch.20 investigation AD) |
| GRC / risques | **Cours GRC** | CTI (Ch.24 threat-informed risk assessment) |
| AppSec | **Cours AppSec** | CTI (Ch.21 vuln intel) |

---


## Annexe G — Ressources et formation

### Certifications CTI

| Certification | Organisme | Focus | Prérequis |
|--------------|-----------|-------|-----------|
| GCTI (GIAC Cyber Threat Intelligence) | SANS/GIAC | Processus CTI complet | FOR578 recommandé |
| CREST CTIA (Certified Threat Intelligence Analyst) | CREST | Analyse et production CTI | 2+ ans d'expérience |
| CTIA (Certified Threat Intelligence Analyst) | EC-Council | CTI généraliste | — |
| FOR578 (Cyber Threat Intelligence) | SANS | Formation de référence CTI | — |

### Formations complémentaires

| Code | Titre | Focus |
|------|-------|-------|
| SANS FOR578 | Cyber Threat Intelligence | Formation CTI de référence |
| SANS FOR508 | Advanced IR, Threat Hunting, Digital Forensics | IR + Hunting guidé par CTI |
| SANS FOR572 | Advanced Network Forensics | Network intelligence |
| SANS ICS515 | ICS Visibility, Detection, and Response | CTI pour les environnements industriels |

### Rapports annuels de référence

| Rapport | Éditeur | Contenu |
|---------|---------|---------|
| M-Trends | Mandiant/Google | Tendances IR/CTI, TTP observées, métriques |
| CrowdStrike Global Threat Report | CrowdStrike | Panorama menace par pays et par acteur |
| DBIR (Data Breach Investigations Report) | Verizon | Statistiques sur les breaches, vecteurs |
| IOCTA | Europol | Menaces cyber organisées en Europe |
| ENISA Threat Landscape | ENISA | Panorama menace européen |
| Microsoft Digital Defense Report | Microsoft | Tendances globales, telemetry massive |
| ANSSI Panorama de la cybermenace | ANSSI | Menaces sur la France, OIV, secteurs |

### Blogs et sources quotidiennes

| Source | Type | Fréquence | Pertinence CTI |
|--------|------|-----------|---------------|
| The DFIR Report | Blog | Mensuel | Rapports d'intrusion détaillés, TTP pas à pas |
| Mandiant Blog | Blog | Hebdomadaire | Campagnes APT, analyses techniques |
| CrowdStrike Blog | Blog | Hebdomadaire | Acteurs, campagnes, tendances |
| Microsoft Threat Intelligence Blog | Blog | Hebdomadaire | Campagnes, TTP, telemetry |
| CISA Advisories | Advisories | Continu | CVE exploitées, alertes sectorielles |
| CERT-FR Bulletins | Advisories | Continu | Alertes France, recommandations |
| Recorded Future Insikt Group | Blog | Hebdomadaire | Analyses géopolitiques, dark web |
| Krebs on Security | Blog | Quasi quotidien | Cybercriminalité, breaches, acteurs |
| BleepingComputer | News | Quotidien | Actualité ransomware, vulnérabilités |

### Communautés

| Communauté | Accès | Focus |
|-----------|-------|-------|
| FIRST | Adhésion (CERT/CSIRT) | Forum international des équipes de réponse |
| TF-CSIRT (Trusted Introducer) | Adhésion (CERT européens) | Communauté CERT européenne |
| InterCERT France | Adhésion (CERT français) | Communauté CERT française |
| ISAC sectoriels (EE-ISAC, FS-ISAC, H-ISAC) | Adhésion sectorielle | Partage sectoriel |
| MISP community instances | Ouvert / par invitation | Partage technique d'IoC |
| ATT&CK community | Ouvert | Contribution au framework |

---

> **Note de clôture**
>
> Ce cours a été conçu pour former à la discipline analytique de la CTI — le processus rigoureux qui transforme de l'information brute en renseignement exploitable pour la décision.
>
> L'opération MERIDIAN qui traverse les 33 premiers chapitres illustre ce processus de bout en bout : Élise ne se contente pas de « trouver des IoC » — elle formule des questions de renseignement, construit un plan de collecte, mobilise des sources multiples, applique l'ACH pour tester 4 hypothèses concurrentes, évalue ses sources avec le système Admiralty, gère ses propres biais, attribue avec prudence (confiance modérée, pas haute — parce que les données ne permettent pas mieux), et produit des livrables calibrés pour chaque audience (COMEX, SOC, ISAC).
>
> La CTI n'est pas un flux d'IoC. Ce n'est pas un résumé de rapports. Ce n'est pas une attribution sensationnaliste. C'est une discipline de raisonnement — avec ses méthodes, sa rigueur, ses limites avouées, et son exigence d'honnêteté intellectuelle.
>
> *Collecter • Traiter • Analyser • Produire • Diffuser • Améliorer — avec rigueur et humilité.*
