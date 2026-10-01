---
title: Annexes
source: Cyber/01 CTI & renseignement/Menace cyber/APT — synthèse.md
note: APT — synthèse
up:
- - APT — synthèse
  - index.md
---

---


## Annexe A — Glossaire APT/CTI

| Terme | Définition |
|-------|-----------|
| **ACH** | Analysis of Competing Hypotheses — technique analytique structurée |
| **APT** | Advanced Persistent Threat — acteur étatique sophistiqué et persistant |
| **ATT&CK** | Framework MITRE des tactiques, techniques et procédures adverses |
| **Attribution** | Processus de liaison d'une activité malveillante à un acteur/État |
| **Beaconing** | Communication périodique entre un implant et son C2 |
| **C2** | Command and Control — infrastructure de commande d'un implant |
| **Campaign** | Série d'intrusions liées par un objectif/période/infrastructure |
| **Cluster** | Regroupement d'activités non attribué à un acteur connu |
| **COMCYBER** | Commandement de la cyberdéfense français |
| **Defend forward** | Doctrine US de contestation permanente dans les réseaux adverses |
| **DIMEFIL** | Diplomatic, Information, Military, Economic, Financial, Intelligence, Law Enforcement |
| **DLL sideloading** | Chargement d'une DLL malveillante via un exécutable légitime |
| **Domain fronting** | Masquage du C2 réel via un CDN légitime |
| **Dwell time** | Temps entre compromission et détection |
| **Edge device** | Appliance réseau exposée (VPN, firewall, passerelle) |
| **False flag** | Indices plantés pour brouiller l'attribution |
| **Five Eyes** | Alliance de renseignement US/UK/Canada/Australie/Nouvelle-Zélande |
| **Foothold** | Point d'ancrage initial dans le réseau victime |
| **FSB** | Service fédéral de sécurité russe (sécurité intérieure) |
| **GoldenSAML** | Forgeage de tokens SAML pour accéder à Azure AD sans credentials |
| **GRU** | Direction du renseignement militaire russe |
| **Hacktiviste** | Acteur motivé par l'idéologie, pas par l'État ou le profit |
| **Hunt forward** | Déploiement d'équipes cyber dans les réseaux de pays alliés |
| **ICS** | Industrial Control Systems — systèmes de contrôle industriel |
| **Indictment** | Mise en accusation formelle (DOJ US) d'opérateurs APT |
| **Intrusion set** | Ensemble d'activités regroupées par TTP/infrastructure/victimologie |
| **IoA** | Indicator of Attack — signal comportemental d'attaque en cours |
| **IoC** | Indicator of Compromise — artefact technique d'une compromission |
| **Kill Chain** | Modèle Lockheed Martin des phases d'une intrusion |
| **LID** | Lutte informatique défensive (doctrine française) |
| **LIO** | Lutte informatique offensive (doctrine française) |
| **L2I** | Lutte informatique d'influence (doctrine française) |
| **LOLBin** | Living Off the Land Binary — outil système légitime détourné |
| **LotL** | Living off the Land — utilisation d'outils légitimes pour éviter la détection |
| **MSS** | Ministry of State Security — renseignement chinois |
| **OT** | Operational Technology — systèmes industriels |
| **PLA** | People's Liberation Army — armée chinoise |
| **Pré-positionnement** | Accès dormant dans une infra critique pour usage futur |
| **PSO** | Private Sector Offensive — entreprise de surveillance cyber commerciale |
| **Pyramid of Pain** | Hiérarchie des indicateurs par coût pour l'attaquant |
| **RGB** | Reconnaissance General Bureau — renseignement nord-coréen |
| **SCADA** | Supervisory Control and Data Acquisition — supervision industrielle |
| **SIS** | Safety Instrumented Systems — systèmes de sécurité industrielle |
| **Supply chain** | Compromission via un fournisseur de confiance |
| **SVR** | Service de renseignement extérieur russe |
| **Tabletop** | Exercice de simulation sur table d'un scénario d'incident |
| **Tradecraft** | Savoir-faire opérationnel global de l'attaquant |
| **TTP** | Tactics, Techniques, and Procedures |
| **USCYBERCOM** | United States Cyber Command |
| **Wiper** | Malware destructeur qui efface les données |
| **Zero Trust** | Architecture qui ne fait confiance à aucun flux par défaut |

---


## Annexe B — Groupes APT majeurs par pays

*La colonne « Statut d'attribution » indique le niveau de publicité et de confiance de l'attribution — un rappel que tout n'a pas le même statut probatoire.*

| Pays | Groupe (Mandiant) | CrowdStrike | Microsoft | Service | Cibles | Statut d'attribution |
|------|-------------------|-------------|-----------|---------|--------|---------------------|
| Russie | APT28 | Fancy Bear | Forest Blizzard | GRU Unit 26165 | OTAN, gouvernements, défense, médias | **Publiquement attribué** (indictment DOJ 2018, Five Eyes) |
| Russie | APT29 | Cozy Bear | Midnight Blizzard | SVR | Gouvernements, tech, think tanks | **Publiquement attribué** (Five Eyes, advisory SolarWinds 2021) |
| Russie | Sandworm | Voodoo Bear | Seashell Blizzard | GRU Unit 74455 | Ukraine, énergie, OT/ICS | **Publiquement attribué** (indictment DOJ 2020, Five Eyes) |
| Russie | Turla | Venomous Bear | Secret Blizzard | FSB Centre 16 | Gouvernements, diplomatie | **Publiquement attribué** (DOJ opération Medusa 2023) |
| Russie | Gamaredon | — | Aqua Blizzard | FSB Centre 18 | Ukraine (volume) | **Largement suspecté** (pas d'indictment formel) |
| Chine | APT41 | Wicked Panda | Brass Typhoon | MSS | Tech, santé, gaming + cybercrime | **Publiquement attribué** (indictment DOJ 2020) |
| Chine | APT40 | — | Gingham Typhoon | MSS Hainan | Maritime, défense, Asie-Pacifique | **Publiquement attribué** (advisory Five Eyes 2024) |
| Chine | APT10 | — | — | MSS | MSP (Cloud Hopper), tech | **Publiquement attribué** (indictment DOJ 2018) |
| Chine | Volt Typhoon | — | Volt Typhoon | PRC (évalué PLA) | Infras critiques US, prépositionnement | **Publiquement attribué** (advisory NSA/CISA/FBI + Five Eyes 2023) |
| Chine | Salt Typhoon | — | Salt Typhoon | PRC | Télécoms mondiales | **Attribué par gouvernements alliés** (advisory 2024) |
| Chine | APT31 | — | Violet Typhoon | MSS | Gouvernements, think tanks | **Publiquement attribué** (indictment DOJ 2024) |
| DPRK | Lazarus | Labyrinth Chollima | Diamond Sleet | RGB | Finance, crypto, défense, tech | **Publiquement attribué** (FBI, DOJ, Treasury — multiple) |
| DPRK | APT38 | — | Sapphire Sleet | RGB | Finance (SWIFT, crypto) | **Publiquement attribué** (FBI 2018) |
| DPRK | Kimsuky | Velvet Chollima | Emerald Sleet | RGB | Think tanks, diplomatique, nucléaire | **Largement suspecté** (advisory NSA/FBI 2023) |
| Iran | APT33 | Elfin | Peach Sandstorm | IRGC | Énergie, aérospatial, défense | **Largement suspecté** (attributions vendors, pas d'indictment) |
| Iran | APT34 | Helix Kitten | Hazel Sandstorm | MOIS | Gouvernement, finance MO | **Largement suspecté** (attributions vendors) |
| Iran | APT35 | Charming Kitten | Mint Sandstorm | IRGC | Chercheurs, dissidents, journalistes | **Publiquement attribué** (indictment DOJ 2022) |
| Iran | APT42 | — | Calanque | IRGC-IO | Surveillance ciblée | **Attribué par vendors** (Mandiant 2022) |
| Iran | MuddyWater | — | Mango Sandstorm | MOIS | Gouvernements MO, télécom | **Publiquement attribué** (advisory USCYBERCOM 2022) |

**Légende des statuts d'attribution :**

- **Publiquement attribué** : indictment DOJ, advisory gouvernemental signé (NSA/CISA/FBI, Five Eyes), ou attribution officielle par un État
- **Attribué par gouvernements alliés** : advisory ou déclaration publique de gouvernements sans indictment formel
- **Attribué par vendors** : attribution par un ou plusieurs éditeurs CTI (Mandiant, CrowdStrike, Microsoft) sans confirmation gouvernementale
- **Largement suspecté** : consensus de la communauté CTI sans attribution publique formelle
- **Cluster non attribué** : activité observée regroupée analytiquement sans attribution à un acteur connu

---


## Annexe C — Conventions de nommage comparées

| Vendor | Convention | Exemples |
|--------|-----------|----------|
| **Mandiant** | APT + numéro (attribué), UNC + numéro (non attribué) | APT28, APT41, UNC2452 |
| **CrowdStrike** | Animal par pays : Bear (Russie), Panda (Chine), Chollima (DPRK), Kitten (Iran), Spider (cybercrime), Jackal (hacktivisme) | Fancy Bear, Wicked Panda, Labyrinth Chollima |
| **Microsoft** | Météo : Blizzard (Russie), Typhoon (Chine), Sleet (DPRK), Sandstorm (Iran), Tempest (cybecrime), Storm (non attribué) | Forest Blizzard, Volt Typhoon, Diamond Sleet |
| **Kaspersky** | Noms descriptifs ou de projets | Equation Group, DarkHotel, Turla |
| **ESET** | Noms propres ou code | Sednit (APT28), Turla, Winnti |
| **Secureworks** | Couleur + animal par motivation : Iron (state), Gold (financial), Cobalt (threat) | Iron Twilight, Gold Melody |

---


## Annexe D — Timeline des cyberattaques étatiques majeures (2007-2026)

| Année | Opération | Attaquant | Type | Impact |
|-------|-----------|-----------|------|--------|
| 2007 | Cyberattaques Estonie | Russie (présumé) | DDoS massif | Premier cas massif et médiatisé |
| 2010 | Stuxnet | USA/Israël | Sabotage OT | Destruction centrifugeuses nucléaires Iran |
| 2012 | Shamoon v1 | Iran (APT33) | Wiper | 30 000 postes Saudi Aramco détruits |
| 2013 | Rapport APT1 | Chine (PLA) | Espionnage | Première attribution publique à une unité militaire |
| 2014 | Sony Pictures | DPRK (Lazarus) | Destructif + leak | Représailles pour un film |
| 2015 | BlackEnergy (Ukraine) | Russie (Sandworm) | Sabotage OT | Premier blackout par cyberattaque (230k foyers) |
| 2016 | Industroyer (Ukraine) | Russie (Sandworm) | Sabotage OT | Blackout Kiev (1h) |
| 2016 | Ingérence US 2016 | Russie (GRU + IRA) | Hack-and-leak + influence | Impact électoral |
| 2016 | Bangladesh Bank | DPRK (APT38) | Vol SWIFT | $81M volés |
| 2017 | WannaCry | DPRK (Lazarus) | Ransomware worm | 200 000+ systèmes, 150 pays |
| 2017 | NotPetya | Russie (Sandworm) | Wiper (false flag ransomware) | $10+ Mrd dégâts mondiaux |
| 2017 | Triton/TRISIS | Russie (TsNIIKhM) | Ciblage SIS industriel | Usine pétrochimique Arabie Saoudite |
| 2020 | SolarWinds/SUNBURST | Russie (APT29/SVR) | Supply chain | ~18 000 orgs touchées, ~100 exploitées |
| 2021 | Exchange/Hafnium | Chine | Espionnage | 250 000 serveurs vulnérables |
| 2021 | Colonial Pipeline | Cybecrime (DarkSide) | Ransomware → impact OT | Perturbation approvisionnement fuel US |
| 2022 | Industroyer2 (Ukraine) | Russie (Sandworm) | Tentative sabotage OT | Déjouée par CERT-UA/ESET |
| 2022 | Attaque Albanie | Iran | Wiper | Rupture diplomatique Iran-Albanie |
| 2023 | Volt Typhoon révélé | Chine (PRC) | Pré-positionnement | Infras critiques US |
| 2023 | 3CX supply chain | DPRK (Lazarus) | Supply chain | 600 000+ clients affectés |
| 2024 | Salt Typhoon | Chine (PRC) | Espionnage télécoms | Systèmes d'interception légale compromis |
| 2025 | Bybit crypto vol | DPRK (Lazarus) | Vol crypto | ~$1,5 Mrd (record historique) |

---


## Annexe E — Mapping ATT&CK par acteur

*Techniques ATT&CK les plus caractéristiques des 10 groupes les plus actifs — simplifié. Statut d'attribution entre parenthèses.*

| Acteur | Initial Access | Execution | Persistence | Cred Access | Lateral Move | C2 | Signature |
|--------|---------------|-----------|-------------|-------------|-------------|-----|-----------|
| **APT29** (publiquement attribué) | Supply chain, OAuth phishing | Signed binary proxy | Tokens/certificats SAML | Credential spray | GoldenSAML | HTTPS, services légitimes | Furtivité extrême, cloud |
| **APT28** (publiquement attribué) | Spear-phishing, exploit vuln | PowerShell, scripts | Service, registre | Mimikatz, credential harvest | RDP, SMB | HTTPS, custom | Exploitation 0-day |
| **Sandworm** (publiquement attribué) | Supply chain, exploit edge | Custom malware | Service, tâche planifiée | Mimikatz | PsExec, WMI | HTTPS, custom | Wipers, OT/ICS |
| **APT41** (publiquement attribué) | Supply chain, exploit web | Rootkits | Bootkits, registre | Credential dump | RDP, SMB | HTTPS, custom | Double mission |
| **Volt Typhoon** (publiquement attribué) | Exploit edge devices | LOLBins exclusif | Credentials légitimes | ntdsutil, mimikatz | LOLBins | Routeurs SOHO compromis | Pas de malware custom |
| **APT40** (publiquement attribué) | Exploit appliances réseau | Scripts, web shells | Web shells | Credential dump | SMB, RDP | HTTPS | Exploitation rapide CVE |
| **Lazarus** (publiquement attribué) | Social engineering, supply chain | Custom malware multi-OS | Service, tâche planifiée | Keylogger | RDP | HTTPS, custom | Crypto, LinkedIn |
| **APT35** (publiquement attribué) | Social engineering avancé | Scripts, backdoors | Registre, service | Credential phishing | Minimal | HTTPS | Impersonation individuelle |
| **APT33** (largement suspecté) | Password spraying | PowerShell | Service | Password spray | RDP | HTTPS | Volume, énergie |
| **Turla** (publiquement attribué) | Watering hole, supply chain | Ultra-custom malware | Rootkit, firmware | Custom tools | Réseaux satellite | Satellite, proxys | Sophistication extrême |

---


## Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Cours complémentaires |
|-----------|----------------|----------------------|
| Acteurs APT (profils, campagnes, géopolitique) | **Ce cours (APT)** | — |
| Processus analytique CTI (cycle, ACH, attribution, production) | **Cours CTI** | APT (Ch.23 attribution, Annexe B/E données acteurs) |
| Détection SOC (SIEM, investigation, detection engineering) | **Cours SOC** | APT (Ch.27 défense APT-ready, Ch.3 TTP) |
| Incident Response | **Cours IR** | APT (Ch.27 containment APT, Ch.28 tabletop) |
| Forensic numérique | **Cours Forensic** | APT (Ch.3 artefacts TTP) |
| Intelligence économique | **Cours IE** | APT (Ch.4 cyber comme instrument de puissance, Ch.16-19 doctrines étatiques) |
| Écosystèmes cybercriminels | **Cours Écosystèmes** | APT (Ch.15 zones grises crime-État) |
| Dark Web | **Cours Dark Web** | APT (Ch.15 mercenaires, Ch.11 DPRK) |
| OSINT | **Cours OSINT Mastery** | APT (Ch.1 OSINT sur les acteurs) |
| Windows / AD | **Cours Windows / AD** | APT (Ch.3 TTP mouvement latéral, credential access) |

---


## Annexe G — Ressources et formation

### Rapports annuels de référence

| Rapport | Éditeur | Contenu |
|---------|---------|---------|
| M-Trends | Mandiant/Google | Tendances IR/CTI, TTP observées, métriques dwell time |
| Global Threat Report | CrowdStrike | Panorama menace par pays et par acteur |
| Digital Defense Report | Microsoft | Tendances globales, telemetry massive |
| DBIR | Verizon | Statistiques breaches, vecteurs d'accès |
| IOCTA | Europol | Menaces cyber organisées en Europe |
| Panorama de la cybermenace | ANSSI | Menaces sur la France, OIV, secteurs critiques |
| Threat Landscape | ENISA | Panorama menace européen |

### Formations SANS

| Code | Titre | Focus |
|------|-------|-------|
| FOR578 | Cyber Threat Intelligence | CTI de référence — processus, acteurs, analyse |
| FOR508 | Advanced IR, Threat Hunting, Digital Forensics | IR + hunting guidé par CTI |
| FOR572 | Advanced Network Forensics | Détection réseau, C2, exfiltration |
| ICS515 | ICS Visibility, Detection, and Response | CTI et détection pour environnements OT |

### Bases de données et références

| Ressource | Type | Usage |
|-----------|------|-------|
| MITRE ATT&CK Groups | Base de données | Profils d'acteurs avec alias et TTP |
| Malpedia (Fraunhofer) | Base de données | Mappings croisés acteurs/malware |
| MITRE CTI (GitHub) | Dataset | Données STIX des acteurs ATT&CK |
| The DFIR Report | Blog | Intrusions complètes analysées pas à pas |
| Mandiant Blog | Blog | Analyses de campagnes APT |
| Microsoft Threat Intelligence Blog | Blog | Campagnes, TTP, telemetry |
| CISA Advisories | Advisories | CVE exploitées, alertes APT, IoC |
| CERT-FR Bulletins | Advisories | Alertes France, recommandations |

### Conférences

| Conférence | Focus |
|-----------|-------|
| Black Hat (US/EU/Asia) | Recherche offensive/défensive |
| SSTIC (France) | Recherche technique en sécurité |
| Botconf (France) | Analyse de malware, CTI |
| FIRST Conference | Communauté CERT/CSIRT mondiale |
| CyCon (Tallinn) | Géopolitique cyber, droit international |
| FIC / InCyber (Lille) | Cybersécurité et IE |

---

> **Note de clôture**
>
> Ce cours a été conçu comme l'encyclopédie des acteurs de la menace étatique — les profils, les campagnes, la géopolitique, et le tradecraft qui donnent sens aux alertes du SOC, aux artefacts du forensicien, et aux analyses du CTI.
>
> L'opération BLACKOUT illustre la leçon centrale : face à une intrusion sophistiquée, comprendre les acteurs est indispensable pour répondre. Un SOC sans connaissance des APT détecte un beaconing et isole un poste. Un SOC informé par le cours APT comprend que ce beaconing est compatible avec un pré-positionnement étatique dans une infrastructure critique européenne, calibre l'urgence de la réponse en conséquence, et déclenche les bons processus (signalement ANSSI, partage ISAC, monitoring OT renforcé).
>
> Le cours assume trois convictions. Première : les cyberopérations sont un instrument de puissance utilisé par tous les États dotés — les documenter sans angle mort (adversaires ET alliés) est une exigence de rigueur analytique. Deuxième : le pré-positionnement dans les infrastructures critiques est la menace structurelle de la prochaine décennie — et elle est la plus difficile à détecter. Troisième : l'attribution est un spectre, pas un binaire — et l'honnêteté sur les incertitudes est un signe de maturité, pas de faiblesse.
>
> *Comprendre qui menace • Pourquoi • Avec quels moyens • Dans quel contexte — pour mieux se défendre.*
