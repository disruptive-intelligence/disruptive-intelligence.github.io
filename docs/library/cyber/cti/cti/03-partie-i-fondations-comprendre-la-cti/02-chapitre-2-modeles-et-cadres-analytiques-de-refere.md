---
title: Chapitre 2 — Modèles et cadres analytiques de référence
source: Cyber/01_CTI/CTI.md
note: CTI
up:
- - CTI
  - ../index.md
- - 'Partie I — Fondations : comprendre la CTI'
  - index.md
---

## 2.1 Cyber Kill Chain (Lockheed Martin)

Le modèle linéaire en 7 étapes qui décrit le déroulement d'une intrusion, publié par Lockheed Martin en 2011. En CTI, la Kill Chain est utilisée pour positionner les actions d'un acteur dans la séquence d'attaque et identifier les opportunités de détection et de disruption à chaque étape.

**Reconnaissance :** l'attaquant collecte des informations sur la cible (OSINT, scan). L'analyste CTI surveille les signaux de ciblage (scans inhabituels, requêtes OSINT détectées sur l'infrastructure de l'organisation). **Weaponization :** l'attaquant crée le payload (document piégé, exploit). L'analyste CTI documente les outils et les capacités de l'acteur. **Delivery :** l'attaquant envoie le payload (email, watering hole, USB). L'analyste CTI identifie les vecteurs préférés de l'acteur — l'information la plus prédictive pour la défense. **Exploitation :** l'attaquant exploite une vulnérabilité. L'analyste CTI corrèle avec les CVE exploitées in the wild et évalue l'exposition de l'organisation. **Installation :** l'attaquant installe sa persistence (backdoor, service, scheduled task). L'analyste CTI documente les mécanismes de persistance caractéristiques. **Command & Control (C2) :** l'attaquant établit la communication avec son infrastructure. L'analyste CTI cartographie l'infrastructure C2 (domaines, IP, patterns de beaconing, JA3/JA4). **Actions on Objectives :** l'attaquant réalise son objectif final (exfiltration, sabotage, pré-positionnement). L'analyste CTI anticipe les objectifs finaux en fonction du profil de l'acteur.

**Limites de la Kill Chain :** le modèle est linéaire alors que la réalité est itérative (l'attaquant revient en arrière, pivote, répète des étapes). Il ne traite pas bien le mouvement latéral ni la persistence. MITRE ATT&CK comble ces lacunes.

## 2.2 Diamond Model of Intrusion Analysis

Le Diamond Model (Caltagirone, Pendergast, Betz, 2013) structure chaque événement d'intrusion autour de quatre sommets reliés par des arêtes.

**Adversary (acteur) :** qui est derrière l'attaque — groupe, individu, organisation, État. **Capability (capacité) :** quel outil ou technique l'acteur utilise — malware, exploit, framework C2, outil légitime détourné. **Infrastructure :** quelle infrastructure l'acteur emploie — domaines C2, serveurs de staging, VPS, services cloud, infrastructure de phishing. **Victim (victime) :** qui est ciblé — organisation, secteur, individu, système spécifique.

La puissance du Diamond Model réside dans le **pivot analytique** entre sommets. À partir d'une infrastructure C2 connue (un domaine identifié dans un incident), l'analyste pivote vers les victimes (quelles autres organisations contactent ce domaine — via passive DNS, telemetry EDR), vers les capacités (quel malware utilise ce domaine — via sandbox, VirusTotal), et vers l'adversaire (qui opère ce domaine — via WHOIS, patterns d'enregistrement, renseignement communautaire). Chaque pivot ouvre de nouvelles pistes d'investigation. Les trous dans le diamant (sommets sans information) indiquent explicitement ce qu'il reste à découvrir.

Les **méta-features** enrichissent le modèle : timestamp (quand), phase (quelle étape de la Kill Chain), result (succès ou échec), direction (adversary-to-victim ou victim-to-adversary). Ces méta-features permettent de relier plusieurs événements Diamond en une séquence chronologique — une campagne.

## 2.3 MITRE ATT&CK

MITRE ATT&CK est le référentiel central de la CTI moderne. Il organise les comportements adverses en **tactiques** (14, représentant les objectifs stratégiques de l'attaquant à chaque phase — Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact, Resource Development, Reconnaissance), **techniques** (~200, les méthodes pour atteindre chaque objectif), et **sous-techniques** (~400, les variantes spécifiques d'une technique).

L'usage CTI d'ATT&CK est multiple. Le **profiling** : décrire le tradecraft d'un acteur par ses techniques préférées — « UNC-VOLT utilise T1566.001 (Spearphishing Attachment) pour l'accès initial, T1059.001 (PowerShell) pour l'exécution, T1574.001 (DLL Search Order Hijacking) pour la persistence, et T1021.002 (SMB/Windows Admin Shares) pour le mouvement latéral ». La **comparaison** : croiser les TTP de deux clusters pour évaluer s'ils sont liés — si UNC-VOLT et Sandworm partagent 80 % de leurs techniques et procédures, c'est un indice de possible lien (mais pas une preuve — les techniques ATT&CK sont partagées par de nombreux acteurs). Le **gap analysis** : croiser les TTP des acteurs pertinents pour l'organisation avec la couverture de détection actuelle — identifier les techniques non détectées et prioriser les développements. La **communication** : ATT&CK fournit un langage universel entre CTI, SOC, IR, red team, et management.

**ATT&CK Navigator** est l'outil web de visualisation qui permet de colorier les techniques sur la matrice, de superposer les profils de plusieurs acteurs, et de visualiser les gaps de couverture. C'est l'outil de travail quotidien de l'analyste CTI.

**Limites d'ATT&CK :** la granularité est variable (certaines techniques sont très spécifiques, d'autres très larges), le biais de reporting (les techniques les plus documentées dans les rapports publics sont surreprésentées — les techniques utilisées par des acteurs furtifs qui ne sont jamais détectés sont sous-représentées), et la confusion technique/procédure (deux acteurs peuvent utiliser la même technique ATT&CK avec des procédures radicalement différentes — c'est la procédure qui distingue les acteurs, pas la technique générique).

## 2.4 STIX/TAXII — le standard d'échange

**STIX** (Structured Threat Information eXpression) est le format standard de structuration du renseignement cyber. Les objets STIX incluent : Indicator (IoC), Threat Actor, Malware, Attack Pattern (technique ATT&CK), Campaign, Intrusion Set, Vulnerability, Observed Data, et Report. Les relations STIX relient les objets (« Threat Actor uses Malware », « Campaign targets Identity », « Indicator indicates Malware »). Un bundle STIX est un ensemble cohérent d'objets et de relations — c'est le format d'échange standard entre TIP, SIEM, et EDR.

**TAXII** (Trusted Automated eXchange of Indicator Information) est le protocole de transport qui permet la transmission automatisée des bundles STIX entre systèmes. Les feeds STIX/TAXII sont le mécanisme standard d'injection d'IoC et de renseignement dans les systèmes de détection.

## 2.5 Le vocabulaire d'attribution

Le vocabulaire de la CTI est un terrain miné. Les termes ont des significations précises que les médias et parfois les praticiens utilisent de manière interchangeable.

Un **intrusion set** (terminologie MITRE) est un ensemble d'activités malveillantes liées, attribuées à un acteur ou un groupe. Un **cluster** ou **activity group** (terminologie variable) est un regroupement d'activités similaires sans attribution formelle à un acteur — c'est le statut de UNC-VOLT dans notre fil rouge. Une **campaign** est une série d'attaques liées par un objectif commun, une période, ou une infrastructure partagée. Un **threat actor** ou **APT** est un groupe identifié avec un sponsor présumé (souvent étatique).

Le **naming chaos** est le cauchemar de la CTI : chaque éditeur utilise sa propre nomenclature. CrowdStrike nomme par animaux (Bear = Russie, Panda = Chine, Kitten = Iran, Chollima = DPRK, Spider = cybercriminalité). Microsoft nomme par phénomènes météo (Blizzard = Russie, Typhoon = Chine, Sandstorm = Iran, Sleet = DPRK). Mandiant utilise APT/UNC/FIN. Résultat : APT28 = Fancy Bear = Forest Blizzard = Sofacy = Sednit = Pawn Storm — c'est le même acteur. La navigation dans ce chaos utilise **Malpedia** (base de données de référence avec les mappings croisés) et **MITRE ATT&CK Groups** (profils d'acteurs avec tous les alias connus).

## 2.6 Fil rouge — MERIDIAN : les cadres de l'investigation

> **🔎 MERIDIAN — Épisode 2**
>
> Élise commence par structurer les artefacts de l'incident EDE dans un Diamond Model. Adversary : UNC-VOLT (inconnu). Capability : DLL sideloading, PsExec, Kerberoasting, exploitation Ivanti — tradecraft sophistiqué. Infrastructure : 3 domaines C2, 2 IP VPS, certificats Let's Encrypt. Victim : EDE, opérateur d'énergie OIV. Les trous du diamant sont clairs : l'adversaire est inconnu (c'est l'objectif 1-2 de la mission), et la victimologie est limitée à un seul cas (EDE) — il faut déterminer si d'autres opérateurs sont ciblés (objectif 3).
>
> Elle mappe les TTP observées dans l'incident sur ATT&CK Navigator : T1566.001 (Spearphishing Attachment), T1059.001 (PowerShell), T1574.001 (DLL Search Order Hijacking), T1558.003 (Kerberoasting), T1003.006 (DCSync), T1021.002 (SMB/Admin Shares), T1053.005 (Scheduled Task), et T1190 (Exploit Public-Facing Application — Ivanti). Ce mapping sera comparé avec les profils d'acteurs connus pour identifier les correspondances (Ch.16-17).

---
