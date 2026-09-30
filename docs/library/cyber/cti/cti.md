---
title: CTI
source: Cyber/01_CTI/CTI.md
---

*Du renseignement brut à l'intelligence actionnable*

**Cours complet — 36 chapitres • 8 parties • 7 annexes**

*Cycle intel • Analyse structurée • Profilage • Attribution • Production • Détection*

---

## Table des matières

- [Fil rouge : Opération MERIDIAN](#fil-rouge-operation-meridian)
- **PARTIE I — FONDATIONS : COMPRENDRE LA CTI (Ch.1-4)**
  - [Ch.1 — Qu'est-ce que la Cyber Threat Intelligence](#chapitre-1-quest-ce-que-la-cyber-threat-intelligence)
  - [Ch.2 — Modèles et cadres analytiques de référence](#chapitre-2-modeles-et-cadres-analytiques-de-reference)
  - [Ch.3 — Le paysage de la menace : grille de lecture de l'analyste CTI](#chapitre-3-le-paysage-de-la-menace-grille-de-lecture-de-lanalyste-cti)
  - [Ch.4 — Le métier d'analyste CTI](#chapitre-4-le-metier-danalyste-cti)
- **PARTIE II — LE CYCLE DU RENSEIGNEMENT APPLIQUÉ (Ch.5-8)**
  - [Ch.5 — Direction et planification : définir ce qu'on cherche](#chapitre-5-direction-et-planification-definir-ce-quon-cherche)
  - [Ch.6 — Collecte : sources, méthodes et gestion](#chapitre-6-collecte-sources-methodes-et-gestion)
  - [Ch.7 — Traitement et structuration](#chapitre-7-traitement-et-structuration)
  - [Ch.8 — Dissémination et feedback](#chapitre-8-dissemination-et-feedback)
- **PARTIE III — L'ANALYSE : LE CŒUR DU MÉTIER (Ch.9-14)**
  - [Ch.9 — Principes de l'analyse de renseignement](#chapitre-9-principes-de-lanalyse-de-renseignement)
  - [Ch.10 — Techniques analytiques structurées (TAS)](#chapitre-10-techniques-analytiques-structurees-tas)
  - [Ch.11 — Gestion des biais cognitifs en analyse CTI](#chapitre-11-gestion-des-biais-cognitifs-en-analyse-cti)
  - [Ch.12 — Évaluer la fiabilité des sources et la crédibilité de l'information](#chapitre-12-evaluer-la-fiabilite-des-sources-et-la-credibilite-de-linformation)
  - [Ch.13 — Niveaux de confiance et formulation analytique](#chapitre-13-niveaux-de-confiance-et-formulation-analytique)
  - [Ch.14 — Corrélation, recoupement et analyse multi-sources](#chapitre-14-correlation-recoupement-et-analyse-multi-sources)
- **PARTIE IV — PROFILAGE D'ACTEUR ET ATTRIBUTION (Ch.15-19)**
  - [Ch.15 — Construire un Threat Actor Profile](#chapitre-15-construire-un-threat-actor-profile)
  - [Ch.16 — Analyse des TTP et du tradecraft](#chapitre-16-analyse-des-ttp-et-du-tradecraft)
  - [Ch.17 — Attribution : méthode, rigueur et limites](#chapitre-17-attribution-methode-rigueur-et-limites)
  - [Ch.18 — Le naming problem et la gestion des clusters](#chapitre-18-le-naming-problem-et-la-gestion-des-clusters)
  - [Ch.19 — Cas de profilage et d'attribution documentés](#chapitre-19-cas-de-profilage-et-dattribution-documentes)
- **PARTIE V — CTI OPÉRATIONNELLE (Ch.20-25)**
  - [Ch.20 — CTI-to-Detection : transformer le renseignement en règles](#chapitre-20-cti-to-detection-transformer-le-renseignement-en-regles)
  - [Ch.21 — Vulnerability Intelligence](#chapitre-21-vulnerability-intelligence)
  - [Ch.22 — CTI et Threat Hunting](#chapitre-22-cti-et-threat-hunting)
  - [Ch.23 — CTI et Incident Response](#chapitre-23-cti-et-incident-response)
  - [Ch.24 — CTI pour le RSSI et la direction](#chapitre-24-cti-pour-le-rssi-et-la-direction)
  - [Ch.25 — Partage de renseignement et communautés](#chapitre-25-partage-de-renseignement-et-communautes)
- **PARTIE VI — PRODUCTION DE RENSEIGNEMENT (Ch.26-29)**
  - [Ch.26 — Les produits CTI : formats, audiences, temporalités](#chapitre-26-les-produits-cti-formats-audiences-temporalites)
  - [Ch.27 — Rédiger une note analytique CTI](#chapitre-27-rediger-une-note-analytique-cti)
  - [Ch.28 — Rédiger un profil d'acteur et cartographier une campagne](#chapitre-28-rediger-un-profil-dacteur-et-cartographier-une-campagne)
  - [Ch.29 — Étude critique de livrables CTI](#chapitre-29-etude-critique-de-livrables-cti)
- **PARTIE VII — PROGRAMME CTI ET MATURITÉ (Ch.30-33)**
  - [Ch.30 — Construire un programme CTI en entreprise](#chapitre-30-construire-un-programme-cti-en-entreprise)
  - [Ch.31 — Métriques et évaluation de la performance CTI](#chapitre-31-metriques-et-evaluation-de-la-performance-cti)
  - [Ch.32 — Veille et intelligence continue](#chapitre-32-veille-et-intelligence-continue)
  - [Ch.33 — Automatisation, outillage et place réaliste de l'IA](#chapitre-33-automatisation-outillage-et-place-realiste-de-lia)
- **PARTIE VIII — ÉTUDES DE CAS ET SYNTHÈSE (Ch.34-36)**
  - [Ch.34 — Cas complet : profilage et attribution d'un cluster inconnu](#chapitre-34-cas-complet-profilage-et-attribution-dun-cluster-inconnu-synthese-meridian)
  - [Ch.35 — Cas complet : réponse CTI à une campagne de ransomware active](#chapitre-35-cas-complet-reponse-cti-a-une-campagne-de-ransomware-active)
  - [Ch.36 — Cas complet : évaluation de menace sectorielle pour un board](#chapitre-36-cas-complet-evaluation-de-menace-sectorielle-pour-un-board)
- **ANNEXES**
  - [Annexe A — Glossaire CTI](#annexe-a-glossaire-cti)
  - [Annexe B — Taxonomie des sources CTI](#annexe-b-taxonomie-des-sources-cti)
  - [Annexe C — Templates de livrables CTI](#annexe-c-templates-de-livrables-cti)
  - [Annexe D — Cheat sheets analytiques](#annexe-d-cheat-sheets-analytiques)
  - [Annexe E — Outils de référence CTI](#annexe-e-outils-de-reference-cti)
  - [Annexe F — Mapping de la bibliothèque](#annexe-f-mapping-de-la-bibliotheque)
  - [Annexe G — Ressources et formation](#annexe-g-ressources-et-formation)

---

## Fil rouge : Opération MERIDIAN

> **Contexte narratif — ce fil rouge traverse les 33 premiers chapitres du cours et se conclut au Ch.34.**
>
> **Élise Moreau**, analyste CTI senior chez **Sentinelle Cyber** — MSSP français de 120 collaborateurs, clientèle ETI et grands groupes, SOC 24/7, CERT qualifié PRIS — reçoit une mission d'intelligence pour un client critique : **Européenne de Distribution Énergétique (EDE)**, opérateur de réseaux de distribution électrique dans 4 pays européens (France, Belgique, Allemagne, Pays-Bas), 6 200 collaborateurs, classé OIV en France et entité essentielle NIS 2.
>
> EDE a subi un incident de sécurité il y a 6 mois. L'équipe IR de Sentinelle a détecté et éradiqué l'intrusion (cf. cours IR de la bibliothèque). Les constats post-incident : l'attaquant a pénétré le réseau IT via un phishing ciblé sur un sous-traitant de maintenance, s'est déplacé latéralement via PsExec et RDP, a compromis l'Active Directory (Kerberoasting → DCSync), puis a pivoté vers le réseau de supervision SCADA via un poste d'ingénierie à double connexion. Il a été éjecté avant d'atteindre les automates, mais le CERT a identifié des mécanismes de persistance sophistiqués (DLL sideloading, tâches planifiées déguisées, modifications d'ACL AD) qui suggèrent un acteur de haut niveau. Aucune donnée exfiltrée confirmée, pas de ransomware, pas de sabotage — le positionnement semblait stratégique, pas financier.
>
> L'équipe IR a catalogué l'activité sous un cluster temporaire : **UNC-VOLT** (« UNC » pour uncategorized, convention Sentinelle). La mission d'Élise couvre cinq objectifs.
>
> **Objectif 1 — Profilage :** qui est UNC-VOLT ? Acteur étatique, mercenaire, cybercriminel sophistiqué ?
> **Objectif 2 — Attribution :** quel sponsor, quel pays, quel service de renseignement — avec quel niveau de confiance ?
> **Objectif 3 — Menace résiduelle :** UNC-VOLT va-t-il revenir ? Cible-t-il d'autres opérateurs d'énergie européens ?
> **Objectif 4 — Renseignement actionnable :** quelles TTP anticiper, quelles détections déployer, quelle posture défensive recommander à EDE ?
> **Objectif 5 — Contribution communautaire :** partager les conclusions avec l'ISAC énergie européen et contribuer à la connaissance collective sur ce cluster.
>
> L'investigation va mobiliser chaque compétence enseignée dans le cours : formulation de PIR, plan de collecte multi-sources, traitement et structuration dans OpenCTI, analyse structurée avec ACH (4 hypothèses concurrentes), gestion des biais, évaluation des sources, profilage d'acteur, analyse du tradecraft, attribution avec ses incertitudes, vulnerability intelligence (l'attaquant a exploité une vulnérabilité Ivanti), corrélation avec des campagnes connues, production de la note analytique, production de détections Sigma, briefing stratégique au COMEX d'EDE, et partage ISAC.

---

## PARTIE I — FONDATIONS : COMPRENDRE LA CTI

*Avant de collecter ou d'analyser : comprendre ce qu'est la CTI, avec quels cadres elle raisonne, dans quel paysage de menace elle opère, et avec quelle posture professionnelle.*

---

### Chapitre 1 — Qu'est-ce que la Cyber Threat Intelligence

#### 1.1 Définition opérationnelle

La Cyber Threat Intelligence est la discipline qui transforme des informations brutes sur les menaces cyber en renseignement exploitable pour la prise de décision. Le mot clé est « discipline » : la CTI n'est pas un flux d'IoC injecté dans un SIEM, ni une revue de presse des dernières attaques, ni un dashboard de vulnérabilités. C'est un processus analytique structuré — collecte, traitement, analyse, production, dissémination — qui répond à des questions de renseignement définies, avec des niveaux de confiance explicites et des recommandations actionnables.

La distinction fondamentale est entre **information** et **renseignement**. Une information est un fait brut (« le hash X a été observé sur VirusTotal »). Un renseignement est une information analysée, contextualisée, et rendue exploitable (« le hash X est associé au loader BumbleBee, utilisé par le cluster UNC-VOLT qui cible les opérateurs d'énergie européens via exploitation de vulnérabilités Ivanti — notre infrastructure utilise Ivanti, nous recommandons une vérification immédiate et le déploiement des IoC joints dans le SIEM »). La différence est l'analyse : sans analyse, un IoC est un artefact mort. Avec analyse, il devient un renseignement qui oriente une décision.

#### 1.2 CTI et disciplines voisines — interfaces et frontières

La CTI s'inscrit dans un écosystème de disciplines interconnectées, et les confusions entre elles sont fréquentes.

L'**OSINT** (Open Source Intelligence) est une méthode de collecte — la CTI l'utilise comme l'une de ses sources parmi d'autres (sources internes, communautaires, commerciales, techniques, dark web). Dire « je fais de l'OSINT » et « je fais de la CTI » ne désigne pas la même activité : l'OSINT collecte, la CTI analyse et produit. Un analyste CTI utilise l'OSINT, mais il utilise aussi les logs internes du SOC, les rapports d'IR post-incident, les feeds commerciaux, et les échanges en cercles de confiance.

Le **SOC** (Security Operations Center) est le principal consommateur de la CTI technique et tactique. Le SOC reçoit les IoC (pour le SIEM/EDR), les TTP (pour orienter les détections et le hunting), et le contexte (pour qualifier les alertes — « cette alerte correspond-elle à un comportement d'acteur connu ? »). En retour, le SOC alimente la CTI : les alertes, les faux positifs, et les incidents détectés sont des données de première main sur ce que les attaquants tentent contre l'organisation. La boucle SOC → CTI → SOC est le mécanisme le plus productif de la sécurité opérationnelle.

Le **DFIR** (Digital Forensics and Incident Response) fournit des données de terrain à la CTI : les artefacts collectés pendant un incident (malware samples, IoC, TTP observés) sont la matière première que la CTI contextualise et attribue. En retour, la CTI fournit au DFIR le contexte de menace pendant l'incident : « les TTP observées correspondent au cluster X, qui utilise typiquement les mécanismes de persistance Y — cherchez-les ».

Le **Threat Hunting** utilise les hypothèses CTI comme point de départ : « le cluster UNC-VOLT utilise le DLL sideloading sur les postes d'ingénieurs OT — nos postes d'ingénieurs OT sont-ils compromis ? ». Le hunter traduit l'hypothèse CTI en requête technique. Sans CTI, le hunting est aveugle. Sans hunting, la CTI reste théorique.

#### 1.3 Les quatre niveaux de CTI

La CTI produit du renseignement à quatre niveaux distincts, chacun avec son audience, son format, sa temporalité, et son usage.

La **CTI stratégique** s'adresse à la direction, au RSSI, et au board. Elle traite des tendances de menace (quels acteurs ciblent notre secteur, quelle est l'évolution du paysage), de la géopolitique (quelles tensions internationales créent des risques cyber pour notre organisation), et des risques sectoriels (le secteur énergie est-il plus ciblé cette année ? par qui ?). Format : rapports semestriels ou annuels, briefings exécutifs, évaluations de risque. Temporalité : mois. La CTI stratégique informe les décisions de budget, de posture, et de stratégie.

La **CTI opérationnelle** s'adresse aux SOC managers, aux IR leads, et aux responsables sécurité. Elle traite des campagnes en cours (qui attaque, avec quoi, contre qui, depuis quand), des acteurs actifs (profils, TTP à haut niveau), et des alertes sur les menaces imminentes. Format : bulletins hebdomadaires, alertes flash, briefings opérationnels. Temporalité : semaines. La CTI opérationnelle oriente la préparation et la réponse.

La **CTI tactique** s'adresse aux analystes SOC, aux hunters, et aux ingénieurs de détection. Elle traite des TTP détaillés (techniques ATT&CK avec procédures spécifiques, patterns de comportement), des règles de détection associées, et des méthodologies de hunting. Format : mappings ATT&CK, règles Sigma, guides de hunting. Temporalité : jours. La CTI tactique transforme le renseignement en capacité de détection.

La **CTI technique** s'adresse directement aux outils (SIEM, EDR, pare-feu, proxy). Ce sont les IoC bruts : hash de malware, domaines C2, adresses IP, URLs, règles YARA. Format : feeds STIX/TAXII, listes d'IoC, règles de blocage. Temporalité : heures. La CTI technique est consommée automatiquement par les systèmes de détection.

#### 1.4 IoC, TTP, IoA et la Pyramid of Pain

La hiérarchie de valeur du renseignement est structurée par la **Pyramid of Pain** (David Bianco, 2013). En bas de la pyramide, les indicateurs que l'attaquant peut changer facilement : les **hash values** (recompiler le malware = nouveau hash — trivial), les **adresses IP** (changer de VPS — facile), les **noms de domaine** (enregistrer un nouveau domaine — simple). Au milieu, les indicateurs plus coûteux à changer : les **artefacts réseau et host** (user-agents, JA3/JA4, certificats, artefacts de registre — ennuyeux à modifier), les **outils** (changer d'outil de C2, de framework d'exploitation — challenging). Au sommet, les **TTP** (Tactics, Techniques, and Procedures) — le savoir-faire opérationnel de l'attaquant, qui représente des mois ou des années d'investissement et qui est le plus douloureux à modifier.

Le message pour l'analyste CTI : visez le plus haut possible dans la pyramide. Un IoC (hash, IP, domaine) a une durée de vie de quelques heures à quelques jours — l'attaquant le change dès qu'il est détecté. Un TTP a une durée de vie de mois à années — c'est le comportement profond de l'attaquant, et le changer coûte cher en temps, en compétences, et en risque opérationnel. Les détections basées sur les TTP sont les plus résilientes et les plus douloureuses pour l'adversaire.

Les **IoA** (Indicators of Attack) sont un concept intermédiaire : des signaux comportementaux qui indiquent une attaque en cours (un process tree anormal, un beaconing régulier, une rafale de commandes de discovery) — avant même la compromission complète. Les IoA détectent l'action, pas l'artefact — ils survivent au changement d'outillage.

#### 1.5 Ce que la CTI n'est PAS

La CTI n'est PAS un flux automatisé d'IoC injecté dans un SIEM sans contexte (c'est de la CTI technique brute — utile mais insuffisante). Elle n'est PAS une revue de presse des dernières attaques (c'est de la veille, pas du renseignement). Elle n'est PAS un dashboard de vulnérabilités (c'est du vulnerability management). Elle n'est PAS de l'attribution sensationnaliste (« c'est la Russie ! » sans niveau de confiance ni évidences). Et elle n'est PAS un service ponctuel activé uniquement pendant les incidents — c'est un processus continu qui alimente la posture de sécurité en permanence.

#### 1.6 Fil rouge — MERIDIAN : la mission

> **🔎 MERIDIAN — Épisode 1**
>
> Élise reçoit le brief d'EDE. Le RSSI d'EDE, Thomas Kessler, pose les questions en termes business : « Qui nous a attaqués ? Vont-ils revenir ? Que devons-nous faire différemment ? » Élise traduit ces questions en objectifs CTI structurés (les 5 objectifs du fil rouge). Elle note que la première étape n'est pas de chercher des réponses — c'est de formuler les bonnes questions. Le chapitre 5 détaillera cette formulation.

---

### Chapitre 2 — Modèles et cadres analytiques de référence

#### 2.1 Cyber Kill Chain (Lockheed Martin)

Le modèle linéaire en 7 étapes qui décrit le déroulement d'une intrusion, publié par Lockheed Martin en 2011. En CTI, la Kill Chain est utilisée pour positionner les actions d'un acteur dans la séquence d'attaque et identifier les opportunités de détection et de disruption à chaque étape.

**Reconnaissance :** l'attaquant collecte des informations sur la cible (OSINT, scan). L'analyste CTI surveille les signaux de ciblage (scans inhabituels, requêtes OSINT détectées sur l'infrastructure de l'organisation). **Weaponization :** l'attaquant crée le payload (document piégé, exploit). L'analyste CTI documente les outils et les capacités de l'acteur. **Delivery :** l'attaquant envoie le payload (email, watering hole, USB). L'analyste CTI identifie les vecteurs préférés de l'acteur — l'information la plus prédictive pour la défense. **Exploitation :** l'attaquant exploite une vulnérabilité. L'analyste CTI corrèle avec les CVE exploitées in the wild et évalue l'exposition de l'organisation. **Installation :** l'attaquant installe sa persistence (backdoor, service, scheduled task). L'analyste CTI documente les mécanismes de persistance caractéristiques. **Command & Control (C2) :** l'attaquant établit la communication avec son infrastructure. L'analyste CTI cartographie l'infrastructure C2 (domaines, IP, patterns de beaconing, JA3/JA4). **Actions on Objectives :** l'attaquant réalise son objectif final (exfiltration, sabotage, pré-positionnement). L'analyste CTI anticipe les objectifs finaux en fonction du profil de l'acteur.

**Limites de la Kill Chain :** le modèle est linéaire alors que la réalité est itérative (l'attaquant revient en arrière, pivote, répète des étapes). Il ne traite pas bien le mouvement latéral ni la persistence. MITRE ATT&CK comble ces lacunes.

#### 2.2 Diamond Model of Intrusion Analysis

Le Diamond Model (Caltagirone, Pendergast, Betz, 2013) structure chaque événement d'intrusion autour de quatre sommets reliés par des arêtes.

**Adversary (acteur) :** qui est derrière l'attaque — groupe, individu, organisation, État. **Capability (capacité) :** quel outil ou technique l'acteur utilise — malware, exploit, framework C2, outil légitime détourné. **Infrastructure :** quelle infrastructure l'acteur emploie — domaines C2, serveurs de staging, VPS, services cloud, infrastructure de phishing. **Victim (victime) :** qui est ciblé — organisation, secteur, individu, système spécifique.

La puissance du Diamond Model réside dans le **pivot analytique** entre sommets. À partir d'une infrastructure C2 connue (un domaine identifié dans un incident), l'analyste pivote vers les victimes (quelles autres organisations contactent ce domaine — via passive DNS, telemetry EDR), vers les capacités (quel malware utilise ce domaine — via sandbox, VirusTotal), et vers l'adversaire (qui opère ce domaine — via WHOIS, patterns d'enregistrement, renseignement communautaire). Chaque pivot ouvre de nouvelles pistes d'investigation. Les trous dans le diamant (sommets sans information) indiquent explicitement ce qu'il reste à découvrir.

Les **méta-features** enrichissent le modèle : timestamp (quand), phase (quelle étape de la Kill Chain), result (succès ou échec), direction (adversary-to-victim ou victim-to-adversary). Ces méta-features permettent de relier plusieurs événements Diamond en une séquence chronologique — une campagne.

#### 2.3 MITRE ATT&CK

MITRE ATT&CK est le référentiel central de la CTI moderne. Il organise les comportements adverses en **tactiques** (14, représentant les objectifs stratégiques de l'attaquant à chaque phase — Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact, Resource Development, Reconnaissance), **techniques** (~200, les méthodes pour atteindre chaque objectif), et **sous-techniques** (~400, les variantes spécifiques d'une technique).

L'usage CTI d'ATT&CK est multiple. Le **profiling** : décrire le tradecraft d'un acteur par ses techniques préférées — « UNC-VOLT utilise T1566.001 (Spearphishing Attachment) pour l'accès initial, T1059.001 (PowerShell) pour l'exécution, T1574.001 (DLL Search Order Hijacking) pour la persistence, et T1021.002 (SMB/Windows Admin Shares) pour le mouvement latéral ». La **comparaison** : croiser les TTP de deux clusters pour évaluer s'ils sont liés — si UNC-VOLT et Sandworm partagent 80 % de leurs techniques et procédures, c'est un indice de possible lien (mais pas une preuve — les techniques ATT&CK sont partagées par de nombreux acteurs). Le **gap analysis** : croiser les TTP des acteurs pertinents pour l'organisation avec la couverture de détection actuelle — identifier les techniques non détectées et prioriser les développements. La **communication** : ATT&CK fournit un langage universel entre CTI, SOC, IR, red team, et management.

**ATT&CK Navigator** est l'outil web de visualisation qui permet de colorier les techniques sur la matrice, de superposer les profils de plusieurs acteurs, et de visualiser les gaps de couverture. C'est l'outil de travail quotidien de l'analyste CTI.

**Limites d'ATT&CK :** la granularité est variable (certaines techniques sont très spécifiques, d'autres très larges), le biais de reporting (les techniques les plus documentées dans les rapports publics sont surreprésentées — les techniques utilisées par des acteurs furtifs qui ne sont jamais détectés sont sous-représentées), et la confusion technique/procédure (deux acteurs peuvent utiliser la même technique ATT&CK avec des procédures radicalement différentes — c'est la procédure qui distingue les acteurs, pas la technique générique).

#### 2.4 STIX/TAXII — le standard d'échange

**STIX** (Structured Threat Information eXpression) est le format standard de structuration du renseignement cyber. Les objets STIX incluent : Indicator (IoC), Threat Actor, Malware, Attack Pattern (technique ATT&CK), Campaign, Intrusion Set, Vulnerability, Observed Data, et Report. Les relations STIX relient les objets (« Threat Actor uses Malware », « Campaign targets Identity », « Indicator indicates Malware »). Un bundle STIX est un ensemble cohérent d'objets et de relations — c'est le format d'échange standard entre TIP, SIEM, et EDR.

**TAXII** (Trusted Automated eXchange of Indicator Information) est le protocole de transport qui permet la transmission automatisée des bundles STIX entre systèmes. Les feeds STIX/TAXII sont le mécanisme standard d'injection d'IoC et de renseignement dans les systèmes de détection.

#### 2.5 Le vocabulaire d'attribution

Le vocabulaire de la CTI est un terrain miné. Les termes ont des significations précises que les médias et parfois les praticiens utilisent de manière interchangeable.

Un **intrusion set** (terminologie MITRE) est un ensemble d'activités malveillantes liées, attribuées à un acteur ou un groupe. Un **cluster** ou **activity group** (terminologie variable) est un regroupement d'activités similaires sans attribution formelle à un acteur — c'est le statut de UNC-VOLT dans notre fil rouge. Une **campaign** est une série d'attaques liées par un objectif commun, une période, ou une infrastructure partagée. Un **threat actor** ou **APT** est un groupe identifié avec un sponsor présumé (souvent étatique).

Le **naming chaos** est le cauchemar de la CTI : chaque éditeur utilise sa propre nomenclature. CrowdStrike nomme par animaux (Bear = Russie, Panda = Chine, Kitten = Iran, Chollima = DPRK, Spider = cybercriminalité). Microsoft nomme par phénomènes météo (Blizzard = Russie, Typhoon = Chine, Sandstorm = Iran, Sleet = DPRK). Mandiant utilise APT/UNC/FIN. Résultat : APT28 = Fancy Bear = Forest Blizzard = Sofacy = Sednit = Pawn Storm — c'est le même acteur. La navigation dans ce chaos utilise **Malpedia** (base de données de référence avec les mappings croisés) et **MITRE ATT&CK Groups** (profils d'acteurs avec tous les alias connus).

#### 2.6 Fil rouge — MERIDIAN : les cadres de l'investigation

> **🔎 MERIDIAN — Épisode 2**
>
> Élise commence par structurer les artefacts de l'incident EDE dans un Diamond Model. Adversary : UNC-VOLT (inconnu). Capability : DLL sideloading, PsExec, Kerberoasting, exploitation Ivanti — tradecraft sophistiqué. Infrastructure : 3 domaines C2, 2 IP VPS, certificats Let's Encrypt. Victim : EDE, opérateur d'énergie OIV. Les trous du diamant sont clairs : l'adversaire est inconnu (c'est l'objectif 1-2 de la mission), et la victimologie est limitée à un seul cas (EDE) — il faut déterminer si d'autres opérateurs sont ciblés (objectif 3).
>
> Elle mappe les TTP observées dans l'incident sur ATT&CK Navigator : T1566.001 (Spearphishing Attachment), T1059.001 (PowerShell), T1574.001 (DLL Search Order Hijacking), T1558.003 (Kerberoasting), T1003.006 (DCSync), T1021.002 (SMB/Admin Shares), T1053.005 (Scheduled Task), et T1190 (Exploit Public-Facing Application — Ivanti). Ce mapping sera comparé avec les profils d'acteurs connus pour identifier les correspondances (Ch.16-17).

---

### Chapitre 3 — Le paysage de la menace : grille de lecture de l'analyste CTI

*Ce chapitre fournit un socle complet et autosuffisant sur le paysage de la menace. Il est conçu pour que le lecteur dispose de toutes les clés de compréhension nécessaires sans avoir lu les autres cours de la bibliothèque. Les renvois vers les cours APT, Écosystèmes cybercriminels, et Dark Web enrichissent la lecture mais ne la conditionnent pas.*

#### 3.1 Les catégories d'acteurs

Le paysage de la menace cyber est structuré par 5 catégories d'acteurs aux motivations, ressources, et modes opératoires distincts. L'analyste CTI doit savoir dans quelle catégorie se situe l'acteur qu'il étudie, car cette catégorisation oriente toute l'analyse : les objectifs attendus, les TTP probables, la persistance anticipée, et les contre-mesures appropriées.

**Les acteurs étatiques (APT)** sont sponsorisés par un État — service de renseignement, armée, ou contractor mandaté. Leurs motivations : espionnage (politique, militaire, industriel), sabotage (infrastructure critique), influence (opérations informationnelles), et pré-positionnement stratégique (accès maintenu sans action immédiate, pour une utilisation future en cas de conflit). Leurs ressources sont considérables : budget étatique, tradecraft mature, outils custom combinés avec des LOLBins (Living off the Land Binaries — utilisation d'outils légitimes du système d'exploitation pour éviter la détection), renseignement préalable sur la cible, et tolérance au risque faible (furtivité maximale). Le dwell time (temps entre la compromission et la détection) est typiquement de mois à années. L'OPSEC est élevée — l'attaquant cherche à rester indétecté le plus longtemps possible.

Les groupes de référence par pays (résumé structurant — pour les profils détaillés, voir le cours APT) :

**Russie** — services : SVR (APT29/Cozy Bear — espionnage furtif, supply chain, abus de services cloud ; campagne de référence : SolarWinds/SUNBURST 2020), GRU (APT28/Fancy Bear — espionnage + influence, exploitation de vulnérabilités ; Sandworm/Unit 74455 — sabotage d'infrastructures critiques, wipers, campagne de référence : NotPetya 2017, attaques réseau électrique ukrainien), FSB (Gamaredon — ciblage massif de l'Ukraine). Tendance : opérations hybrides combinant cyber, influence, et actions cinétiques, particulièrement depuis l'invasion de l'Ukraine en 2022.

**Chine** — services : MSS (APT41 — double casquette espionnage étatique + cybercriminalité ; APT40 — espionnage maritime et défense ; APT10 — ciblage des MSP via Cloud Hopper), PLA et affiliés (Volt Typhoon — pré-positionnement dans les infrastructures critiques américaines avec living-off-the-land quasi exclusif ; Salt Typhoon — compromission d'opérateurs télécom pour accéder aux systèmes d'interception légale). Tendance : exploitation massive de vulnérabilités d'appliances réseau edge (Ivanti, Fortinet, Citrix, Barracuda), pré-positionnement stratégique sans action immédiate.

**Corée du Nord** — service : RGB (Lazarus Group — vol de cryptomonnaies pour financer le régime — Bybit $1,5 Mrd en 2025, Ronin Network $620M en 2022 ; APT38/BlueNoroff — braquages SWIFT ; Kimsuky — espionnage diplomatique et nucléaire). Tendance : ingénierie sociale sophistiquée sur LinkedIn, ciblage de la supply chain (3CX 2023), vol massif de crypto.

**Iran** — services : MOIS/IRGC (APT33/Peach Sandstorm — énergie et aérospatial ; APT34/OilRig — gouvernements Moyen-Orient ; APT35/Charming Kitten — social engineering avancé ciblant chercheurs et dissidents ; MuddyWater — PowerShell obfusqué, outils open source). Tendance : opérations destructives ponctuelles (wipers), surveillance des dissidents, social engineering très ciblé.

**Les cybercriminels organisés** sont motivés par le profit financier. Le modèle dominant en 2024-2026 est le **Crime-as-a-Service** : chaque fonction est spécialisée et externalisable. Le Ransomware-as-a-Service (RaaS) — l'opérateur développe et maintient le ransomware, les affiliés le déploient contre des cibles, les deux partagent les revenus (typiquement 70/30 ou 80/20). Les IAB (Initial Access Brokers) vendent des accès réseau compromis (VPN, RDP, Citrix) aux affiliés RaaS. Les infostealers (Lumma, RedLine, Vidar) volent automatiquement les credentials, cookies, et données de navigateur des victimes — les logs sont vendus sur des marchés spécialisés (Russian Market) et alimentent le pipeline vers les compromissions d'entreprise. Les temporalités sont courtes (jours à semaines — smash and grab), l'OPSEC est variable (du script kiddie au groupe structuré comme LockBit).

Exemples structurants : LockBit (RaaS dominant 2022-2024, disruption partielle par Operation Cronos en février 2024, réapparition sous LockBit 4.0), Lumma Stealer (infostealer dominant 2024-2025, infrastructure disruptée en mai 2025 par une opération coordonnée Microsoft/Europol — mais le développeur reste actif). *Pour la cartographie complète de l'économie cybercriminelle : voir le cours Écosystèmes cybercriminels.*

**Les hacktivistes** sont motivés par l'idéologie, la réputation, et l'impact médiatique. Leurs outils sont publics (DDoS, défacement, leaks), leur OPSEC faible à moyen, et leur impact souvent limité techniquement mais significatif médiatiquement. Le paysage hacktiviste post-2022 est fortement polarisé par le conflit russo-ukrainien : groupes pro-russes (KillNet, NoName057(16) — DDoS, parfois des fuites de données), groupes pro-ukrainiens (IT Army of Ukraine — DDoS coordonné via Telegram), et groupes idéologiques divers (Anonymous Sudan — DDoS massif, démantelé en 2024).

**Les mercenaires cyber / PSO** (Private Sector Offensive) sont des entreprises commerciales qui vendent des capacités d'espionnage à des États. NSO Group (Pegasus — spyware mobile ciblant journalistes, dissidents, opposants politiques), Intellexa (Predator), Candiru. Leur pertinence pour la CTI : leurs outils apparaissent dans les campagnes d'espionnage — l'analyste qui identifie un spyware Pegasus sait que le commanditaire est un client étatique de NSO, pas un cybercriminel.

**Les insiders** (employés malveillants ou négligents) opèrent avec des accès légitimes (pas de mouvement latéral classique), des motivations variables (vengeance, profit, négligence, recrutement par un service étranger), et une détection qui relève autant du RH et du juridique que de la cybersécurité. La CTI intervient dans la corrélation comportementale et le croisement avec les indicateurs de recrutement par des services étrangers.

#### 3.2 Les vecteurs d'accès initial dominants (2024-2026)

Le **phishing/spearphishing** reste le vecteur n°1 en volume. L'évolution : les kits de phishing AitM (Adversary-in-the-Middle) interceptent les tokens MFA en temps réel, rendant le MFA classique (SMS, push) moins efficace contre les attaques ciblées.

L'**exploitation de vulnérabilités périmétriques** est le vecteur n°1 en impact pour les acteurs étatiques et les affiliés RaaS sophistiqués. Les appliances réseau edge (VPN Ivanti/Pulse Secure, firewalls Fortinet, passerelles Citrix, appliances Barracuda) sont des cibles systématiques — elles sont exposées sur Internet, rarement patchées rapidement, et donnent un accès direct au réseau interne.

Les **credentials volées via infostealers** constituent le pipeline le plus industrialisé : infostealer déployé sur des milliers de machines (via phishing, publicités malveillantes, logiciels piratés) → logs collectés automatiquement → vendus sur les marchés de logs (Russian Market) → exploités par des affiliés RaaS ou des IAB pour compromettre les réseaux d'entreprise. Ce pipeline est détaillé dans le cours Écosystèmes cybercriminels.

La **supply chain** (logicielle et prestataire) est le vecteur le plus difficile à défendre : l'attaquant compromet un fournisseur de confiance et utilise cette position pour atteindre ses clients (SolarWinds, 3CX, compromission de sous-traitants de maintenance — c'est exactement le cas MERIDIAN).

#### 3.3 Dynamiques structurelles et tendances

**La convergence crime-état :** des acteurs opèrent simultanément pour un État et pour leur propre profit (APT41 — espionnage MSS + cybercriminalité personnelle), ou des acteurs criminels sont tolérés ou instrumentalisés par des États (les groupes ransomware russophones opèrent en toute impunité tant qu'ils ne ciblent pas la CEI). Cette convergence rend l'attribution plus complexe.

**Living off the Land (LotL) :** l'utilisation systématique d'outils légitimes du système d'exploitation (PowerShell, WMI, certutil, bitsadmin, mshta) pour éviter la détection. Volt Typhoon est l'exemple extrême : quasi aucun outil custom, uniquement des LOLBins. La conséquence pour la CTI : la détection basée sur les outils ne fonctionne plus — il faut détecter les comportements.

**Le ciblage systématique des appliances edge :** les appliances réseau exposées sur Internet (VPN, firewalls, passerelles) sont devenues le vecteur d'accès privilégié des acteurs étatiques et des affiliés RaaS sophistiqués. La gestion de ces appliances (patching rapide, monitoring dédié) est devenue un enjeu critique.

**Le pré-positionnement stratégique :** certains acteurs étatiques (Volt Typhoon, certains groupes russes) compromettent des infrastructures critiques sans mener d'action immédiate — ils maintiennent un accès dormant, utilisable en cas de conflit. C'est une menace existentielle pour les opérateurs d'énergie, de télécom, et de transport — et c'est exactement le profil de l'incident EDE dans MERIDIAN.

#### 3.4 Fil rouge — MERIDIAN : positionner UNC-VOLT dans le paysage

> **🔎 MERIDIAN — Épisode 3**
>
> Élise utilise le panorama de menace pour formuler ses hypothèses initiales sur UNC-VOLT.
>
> Le profil de l'incident (ciblage d'un opérateur d'énergie OIV, pré-positionnement OT sans action immédiate, tradecraft sophistiqué avec DLL sideloading et exploitation Ivanti, pas de ransomware ni d'exfiltration financière) élimine d'emblée les catégories hacktiviste et cybercriminel classique. Il reste trois hypothèses :
>
> **H1 :** Acteur étatique russe (Sandworm/GRU) — ciblage des infras critiques européennes cohérent avec le contexte géopolitique post-2022, TTP compatibles (Sandworm cible les opérateurs d'énergie).
> **H2 :** Acteur étatique chinois (Volt Typhoon ou cluster similaire) — pré-positionnement sans action immédiate, exploitation d'appliance edge (Ivanti), LotL.
> **H3 :** Mercenaire cyber / groupe offensif privé vendant des accès à un État — tradecraft sophistiqué sans signature d'un groupe connu.
> **H4 :** Acteur criminel sophistiqué ayant pivoté vers l'OT — peu probable mais à ne pas exclure sans données.
>
> Ces hypothèses seront testées avec l'ACH au Ch.10.

---

### Chapitre 4 — Le métier d'analyste CTI

#### 4.1 Ce que fait concrètement un analyste CTI au quotidien

La journée type d'un analyste CTI senior combine : la **veille** (1-2h — consultation des sources prioritaires, lecture des rapports publiés dans les dernières 24h, vérification des feeds et des alertes de monitoring), l'**analyse** (3-4h — le cœur du métier : analyse approfondie des données collectées, rédaction des notes et des profils, corrélation multi-sources, application des TAS), la **production** (1-2h — rédaction des livrables : flash alerts, notes tactiques, mises à jour de profils d'acteurs, briefings), la **collaboration** (1h — échanges avec le SOC, l'IR, le hunting, le RSSI : briefings, réponses aux questions, orientation des détections), et le **développement** (temps variable — participation aux communautés, formation continue, développement d'outils et de processus).

La répartition varie selon le contexte : en période calme, la veille et l'analyse dominent ; pendant un incident, la collaboration et la production prennent le dessus ; et le développement des capacités est un investissement continu qui ne doit pas être sacrifié aux urgences.

#### 4.2 Compétences requises

Les **compétences techniques** incluent la capacité à lire et interpréter un rapport technique d'incident (comprendre les artefacts, les TTP, les IoC), une compréhension des systèmes d'exploitation (Windows, Linux — registre, Event Logs, processus, réseau), une compréhension des réseaux (TCP/IP, DNS, HTTP/HTTPS, proxy, pare-feu), une capacité d'analyse de malware de premier niveau (soumission sandbox, interprétation des résultats, extraction d'IoC — pas du reverse engineering complet), et une maîtrise des outils CTI (TIP, ATT&CK Navigator, STIX/TAXII, feeds).

Les **compétences analytiques** sont les plus distinctives : raisonnement structuré (formuler des hypothèses, les tester, gérer l'incertitude), évaluation de sources (fiabilité, biais, crédibilité), rédaction analytique (formuler des conclusions avec niveaux de confiance, distinguer fait/déduction/hypothèse), et pensée critique (résistance aux biais, devil's advocate, remise en question des certitudes).

Les **compétences relationnelles** sont souvent sous-estimées : capacité de vulgarisation (expliquer une menace technique à un CEO sans jargon), collaboration interéquipes (travailler avec le SOC, l'IR, le RSSI dans des temporalités et des langages différents), et communication orale (briefings, présentations, argumentation).

#### 4.3 Les rôles CTI

L'**analyste CTI junior** (0-2 ans) traite les feeds, enrichit les IoC, rédige les résumés de rapports, et assiste les analystes seniors. L'**analyste CTI senior** (2-5 ans) mène les analyses de fond (profilage, attribution, corrélation), produit les notes analytiques, et gère les missions d'intelligence. Le **CTI team lead** (5+ ans) définit les PIR avec le RSSI, gère l'équipe, arbitre les priorités, et porte la relation avec les communautés. Le **directeur CTI / Head of Intelligence** oriente la stratégie, gère le budget et les partenariats, et reporte au RSSI ou au board.

La CTI peut être organisée dans le SOC (intégrée à l'équipe de détection — avantage : boucle courte CTI→SOC ; inconvénient : risque de se faire absorber par l'opérationnel au détriment de l'analyse de fond), en équipe dédiée (séparée du SOC — avantage : profondeur d'analyse ; inconvénient : risque de déconnexion avec l'opérationnel), ou en modèle hybride (cellule CTI dédiée avec un « CTI liaison » intégré au SOC pour la boucle courte).

#### 4.4 Posture intellectuelle

La rigueur : chaque affirmation est sourcée, chaque conclusion est accompagnée d'un niveau de confiance, chaque raisonnement est documenté. Le doute méthodique : l'analyste ne prend rien pour acquis, teste les hypothèses alternatives, et cherche activement ce qui contredit sa conclusion préférée. L'honnêteté : dire « nous ne savons pas » quand c'est le cas est un signe de maturité, pas de faiblesse. La résistance au sensationnalisme : le paysage de la menace est suffisamment inquiétant sans avoir besoin de l'exagérer — un rapport alarmiste non étayé détruit la crédibilité de la CTI.

---

## PARTIE II — LE CYCLE DU RENSEIGNEMENT APPLIQUÉ

*Le processus structuré qui transforme un besoin de renseignement en intelligence exploitable. Chaque phase est traitée avec la profondeur opérationnelle nécessaire pour être appliquée immédiatement.*

---

### Chapitre 5 — Direction et planification : définir ce qu'on cherche

#### 5.1 Les PIR (Priority Intelligence Requirements)

Les PIR sont les questions stratégiques auxquelles la CTI doit répondre. Sans PIR, la CTI produit du bruit — des rapports intéressants mais non ciblés, des IoC par milliers sans priorisation, des analyses brillantes qui ne répondent à aucun besoin opérationnel. Les PIR sont la boussole qui oriente chaque étape du cycle.

Un bon PIR est spécifique (pas « que se passe-t-il dans la menace ? » mais « quels acteurs ciblent les opérateurs de distribution d'énergie en Europe, avec quelles TTP, et notre couverture de détection couvre-t-elle ces TTP ? »), mesurable (on peut évaluer si le PIR a reçu une réponse), orienté décision (la réponse au PIR doit conduire à une action — déployer des détections, ajuster la posture, informer la direction), et temporel (le PIR a une période de validité — il est réexaminé trimestriellement).

Les PIR sont co-construits avec le RSSI (qui apporte la vision stratégique et la connaissance des risques business), le SOC manager (qui apporte la connaissance des capacités de détection et des gaps), l'IR lead (qui apporte le retour d'expérience des incidents passés), et les métiers (qui apportent la connaissance des actifs critiques et des enjeux business). La CTI seule ne peut pas définir ses propres PIR — elle les définit avec ses consommateurs.

#### 5.2 Des PIR aux IR et au plan de collecte

Chaque PIR se décline en **IR** (Intelligence Requirements) plus granulaires, qui eux-mêmes orientent le plan de collecte. Exemple de décomposition pour la mission MERIDIAN :

**PIR 1 :** Qui est UNC-VOLT ? → IR 1.1 : Quelles TTP caractéristiques UNC-VOLT utilise-t-il ? → IR 1.2 : Ces TTP correspondent-elles à un acteur connu ? → IR 1.3 : Quel est le sponsor présumé ? → Plan de collecte : analyse des artefacts IR, corrélation avec les bases ATT&CK, recherche dans les rapports communautaires et commerciaux.

**PIR 2 :** UNC-VOLT cible-t-il d'autres opérateurs d'énergie ? → IR 2.1 : Les IoC de l'incident EDE apparaissent-ils dans les feeds communautaires ? → IR 2.2 : Des incidents similaires ont-ils été signalés par l'ISAC énergie ? → Plan de collecte : partage d'IoC via MISP (ISAC énergie), requêtes auprès des contacts communautaires, monitoring des rapports vendor sur le secteur énergie.

**PIR 3 :** Quelle est la menace résiduelle pour EDE ? → IR 3.1 : Les mécanismes de persistance ont-ils tous été éradiqués ? → IR 3.2 : L'attaquant a-t-il d'autres points d'entrée (vulnérabilités non patchées, credentials non resetés) ? → Plan de collecte : revue des conclusions IR, audit des vulnérabilités exposées, monitoring dark web pour les credentials EDE.

#### 5.3 Fil rouge — MERIDIAN : les PIR

> **🔎 MERIDIAN — Épisode 4**
>
> Élise formule 5 PIR validés avec Thomas Kessler (RSSI d'EDE) et l'équipe Sentinelle.
>
> PIR 1 : Identité et attribution de UNC-VOLT (qui, sponsor, niveau de confiance)
> PIR 2 : Victimologie élargie (d'autres opérateurs énergie sont-ils ciblés ?)
> PIR 3 : Menace résiduelle pour EDE (l'attaquant va-t-il revenir ? par quel vecteur ?)
> PIR 4 : TTP à anticiper (quelles techniques futures utiliserait UNC-VOLT s'il revient ?)
> PIR 5 : Couverture de détection (nos détections couvrent-elles les TTP de UNC-VOLT ?)

---

### Chapitre 6 — Collecte : sources, méthodes et gestion

#### 6.1 Taxonomie des sources CTI

Les sources CTI se répartissent en 6 catégories, chacune avec ses forces, ses biais, et son coût.

**Sources ouvertes (OSINT) :** les rapports publics d'éditeurs CTI (Mandiant, CrowdStrike, ESET, Kaspersky, Microsoft, Recorded Future — rapports de campagnes, profils d'acteurs, analyses de malware), les blogs de chercheurs en sécurité (souvent la première source de publication d'une nouvelle campagne ou d'une nouvelle vulnérabilité exploitée), les advisories des CERT (CERT-FR, CISA, NCSC — alertes officielles avec IoC et recommandations), les conférences et présentations (Black Hat, DEF CON, SSTIC, Botconf — présentations techniques avec des données exclusives), et les réseaux sociaux techniques (Twitter/X, LinkedIn — les chercheurs partagent des IoC et des analyses en temps réel, mais avec un bruit considérable). Forces : gratuites, abondantes, vérifiables. Limites : biais de publication (seules les campagnes détectées et analysées sont publiées — les opérations furtives restent invisibles), biais commercial (les éditeurs dramatisent parfois pour vendre), et volume (le bruit est massif — filtrer est un défi permanent).

**Sources commerciales :** les plateformes de threat intelligence (Recorded Future, Intel 471, Flashpoint, Mandiant Advantage, CrowdStrike Falcon Intelligence, Group-IB, Sekoia) offrent une couverture plus large (dark web, forums fermés, traductions, analystes humains) et des fonctionnalités d'enrichissement, de scoring, et d'alerting. Chaque plateforme a ses spécialités (Intel 471 et Flashpoint sont fortes sur le dark web et la cybercriminalité, Mandiant est forte sur les APT et l'IR, Recorded Future est forte sur la couverture large et l'automatisation). Forces : couverture élargie, analyse humaine, intégration API. Limites : coût élevé (50K-500K+ $/an), biais de couverture (chaque éditeur a ses angles morts), et risque de dépendance.

**Sources internes :** souvent les plus pertinentes car contextualisées pour l'organisation. Les logs SOC (alertes, incidents, patterns de faux positifs — qui révèlent ce que les attaquants tentent), les post-mortems d'IR (TTP observées dans les incidents passés = intelligence de première main sur les menaces qui ciblent réellement l'organisation), le vuln management (quelles vulnérabilités existent dans l'environnement = surface d'attaque réelle), l'email security (campagnes de phishing ciblant les utilisateurs), et l'IAM (tentatives de brute force, comptes compromis, anomalies d'authentification).

**Sources communautaires :** les ISACs sectoriels (EE-ISAC pour l'énergie, FS-ISAC pour la finance, H-ISAC pour la santé — échanges non publics entre pairs du même secteur), les cercles de confiance (FIRST, TF-CSIRT, InterCERT France, groupes de travail ANSSI), et les trusted groups (groupes Signal/Telegram entre analystes de confiance). Forces : contexte que les rapports publics ne donnent pas, réciprocité, confiance. Limites : accès restreint (il faut être membre et contribuer), couverture limitée au secteur/à la communauté.

**Sources dark web :** le monitoring des forums, marchés, leak sites, et canaux Telegram pour détecter les ventes de données, les ventes d'accès, les revendications de ransomware, et les discussions de ciblage qui concernent l'organisation ou son secteur. La collecte dark web est traitée en profondeur dans le cours Dark Web de la bibliothèque — ici on traite de comment intégrer le renseignement dark web dans le cycle CTI (le renseignement dark web est une source parmi d'autres, pas une fin en soi, et il doit être évalué avec la même rigueur que les autres sources — voir le chapitre pièges analytiques du cours Dark Web).

**Sources techniques :** les honeypots et honeynets (systèmes pièges qui capturent les activités des attaquants), les sinkholes (domaines de C2 saisis ou expirés dont le trafic est redirigé vers un serveur de collecte — révèlent les machines compromises qui tentent de contacter le C2), la telemetry de déploiement (les éditeurs d'EDR/antivirus ont une visibilité sur des millions de machines — leurs feeds de threat intelligence en découlent), le passive DNS (historique des résolutions DNS — révèle les changements d'infrastructure C2), et Certificate Transparency (logs publics des certificats TLS émis — permettent de détecter l'enregistrement de certificats pour des domaines de phishing ou de C2).

#### 6.2 Gestion de la collecte

Le piège principal est la surcharge informationnelle : des centaines de rapports par semaine, des millions d'IoC dans les feeds, des dizaines d'alertes de monitoring. L'analyste qui essaie de tout lire et tout traiter se noie. La gestion de collecte impose de prioriser (les sources sont classées par pertinence pour les PIR actifs — les sources qui ne répondent à aucun PIR sont dé-priorisées), de documenter (chaque information est traçable jusqu'à sa source — qui, quand, où, avec quelle fiabilité), d'automatiser le traitement des feeds (l'injection d'IoC dans le SIEM/EDR est automatisée — l'analyste n'intervient que pour le scoring et la contextualisation), et de maintenir l'OPSEC (les identités de veille dark web sont compartimentées, l'infrastructure de collecte est séparée de l'infrastructure de production — les détails opérationnels sont dans le cours Dark Web).

#### 6.3 Fil rouge — MERIDIAN : le plan de collecte

> **🔎 MERIDIAN — Épisode 5**
>
> Élise construit son plan de collecte pour les 5 PIR. Sources mobilisées : artefacts IR de l'incident EDE (source interne — haute fiabilité), rapports Mandiant et CrowdStrike sur les acteurs ciblant le secteur énergie (source commerciale — haute fiabilité, biais de couverture à considérer), ISAC énergie européen (source communautaire — fiabilité variable selon les contributeurs), passive DNS sur les 3 domaines C2 identifiés (source technique), Certificate Transparency sur les patterns d'enregistrement, monitoring dark web pour les credentials EDE (source dark web — fiabilité modérée, risque de scams), et CISA KEV pour les vulnérabilités Ivanti exploitées ITW (source technique — haute fiabilité).

---

### Chapitre 7 — Traitement et structuration

#### 7.1 De la donnée brute au matériau analysable

Le traitement est la phase souvent négligée entre la collecte et l'analyse. Elle est pourtant déterminante : si les données sont mal normalisées, mal dédoublonnées, ou mal enrichies, l'analyse en souffrira.

La **normalisation** résout le problème des formats hétérogènes : un même IoC (domaine C2) peut apparaître sous 5 formes différentes dans 5 sources (avec ou sans protocole, avec ou sans port, avec ou sans defanging `hxxps://`). La normalisation le ramène à une forme canonique unique. Les noms d'acteurs sont normalisés vers un identifiant de référence (l'ID MITRE ou Malpedia) avec les alias comme métadonnées.

Le **dédoublonnage** identifie les doublons (le même rapport repris par 10 sources, le même IoC dans 5 feeds). L'analyste identifie la source primaire (le rapport original de l'éditeur) et les sources secondaires (les reprises). La source primaire est fiable ; les reprises ne la « corroborent » pas — elles la propagent. C'est le piège de la circularité (Ch.14).

L'**enrichissement automatisé** ajoute du contexte aux données brutes : un hash → soumission VirusTotal → famille de malware, detection rate, sandbox reports. Un domaine → Whois + passive DNS → dates d'enregistrement, registrar, IP hébergement, certificats. Une IP → géolocalisation + ASN + réputation (AbuseIPDB, GreyNoise). Un CVE → CVSS score + EPSS score + statut CISA KEV + exploitation ITW confirmée.

#### 7.2 Les TIP (Threat Intelligence Platforms)

Les TIP sont l'outil central de structuration et de gestion du renseignement CTI. Ils stockent les IoC, les profils d'acteurs, les campagnes, et les relations entre eux, dans un format structuré (STIX) interrogeable et partageable.

**MISP** (Malware Information Sharing Platform, open source) : la référence communautaire, utilisée par de nombreux CERT et ISACs. Forces : gratuit, communauté massive, intégration riche (STIX/TAXII, SIEM, EDR). Limites : interface utilisateur datée, courbe d'apprentissage, nécessite de l'administration.

**OpenCTI** (open source, développé par Filigran) : la plateforme montante en 2024-2026, conçue spécifiquement pour la CTI analytique (pas seulement le partage d'IoC). Forces : modèle de données riche (STIX 2.1 natif), visualisation de graphes de relations, intégration ATT&CK, connecteurs multiples. Limites : nécessite une infrastructure (Elasticsearch, Redis, RabbitMQ), courbe d'apprentissage.

**ThreatConnect** et **Anomali** (commerciaux) : plateformes intégrées avec enrichissement, scoring, et orchestration. Forces : interface mature, support commercial, intégration SOAR. Limites : coût élevé.

#### 7.3 Le problème de la qualité des données

Garbage in, garbage out : un IoC mal formaté propagé dans le SIEM génère des faux positifs. Un hash tronqué ne matche avec rien. Une attribution erronée (« ce malware est attribué à APT28 ») propagée dans un feed et intégrée automatiquement dans les profils d'acteurs de dizaines d'organisations crée une fausse certitude collective. La qualité des données est un enjeu permanent de la CTI — chaque IoC doit être vérifié, chaque attribution doit être sourcée, et chaque information automatisée doit être revue.

---

### Chapitre 8 — Dissémination et feedback

#### 8.1 Atteindre le bon public au bon moment

Le produit CTI le plus brillant est inutile s'il n'atteint pas son audience. La dissémination est la phase qui connecte le renseignement à l'action.

Les formats par audience : **IoC feed automatisé** (→ SIEM, EDR, pare-feu — format STIX/TAXII, intégration API, scoring automatique), **note tactique avec règles Sigma** (→ analystes SOC, hunters — format document technique avec détections prêtes à déployer), **briefing opérationnel** (→ IR lead, SOC manager — format présentation orale ou note de 2-3 pages), **note stratégique** (→ RSSI, direction, board — format rapport de 5-10 pages sans jargon), **flash alert** (→ toute l'équipe sécurité — format 1 page, urgence, actions immédiates).

#### 8.2 Le TLP (Traffic Light Protocol)

Le TLP encadre la diffusion du renseignement partagé. **TLP:RED** (yeux seulement — ne pas diffuser au-delà des personnes présentes dans l'échange). **TLP:AMBER** (diffusion limitée à l'organisation et aux partenaires qui ont besoin de savoir — le niveau le plus courant pour les échanges communautaires). **TLP:AMBER+STRICT** (diffusion limitée à l'organisation uniquement). **TLP:GREEN** (diffusion au sein de la communauté — pas au grand public). **TLP:CLEAR** (diffusion libre).

L'erreur courante : sur-classifier en TLP:RED par excès de prudence. Résultat : l'information ne circule pas, et les organisations qui auraient pu se protéger ne sont pas informées. L'analyste doit appliquer le niveau TLP minimum nécessaire pour protéger la source sans bloquer l'utilité du renseignement.

#### 8.3 Le feedback — la boucle la plus importante

Le feedback est la phase qui ferme le cycle et qui est la plus systématiquement négligée. Le SOC signale que les IoC d'un feed génèrent 80 % de faux positifs → la CTI réévalue le scoring du feed. L'IR signale que les TTP d'un rapport ne correspondent pas à ce qu'il observe sur le terrain → la CTI réévalue l'attribution ou identifie un nouveau cluster. Le RSSI signale que les rapports stratégiques sont trop techniques pour le board → la CTI ajuste le format. Le hunting signale qu'une hypothèse CTI a produit un résultat positif (ou négatif) → la CTI met à jour le profil d'acteur.

Sans feedback, le cycle est cassé : la CTI produit dans le vide, les consommateurs reçoivent du renseignement non calibré, et la qualité se dégrade.

---

## PARTIE III — L'ANALYSE : LE CŒUR DU MÉTIER

*C'est la partie la plus importante du cours — celle qui enseigne ce qu'aucun autre cours de la bibliothèque ne couvre : le processus analytique structuré qui transforme un collecteur d'informations en analyste de renseignement.*

---

### Chapitre 9 — Principes de l'analyse de renseignement

#### 9.1 Ce que signifie « analyser »

Analyser, en CTI, ne signifie pas résumer un rapport (« Mandiant dit que APT29 cible le secteur énergie »). Analyser signifie contextualiser (cette information est-elle pertinente pour notre organisation ? dans quel contexte s'inscrit-elle ?), corréler (cette information est-elle cohérente avec ce que nous observons dans nos logs, dans les autres sources, dans nos incidents passés ?), évaluer (quelle confiance accorder à cette information ? la source est-elle fiable ? l'information est-elle corroborée ?), et conclure avec un niveau de confiance (« nous évaluons avec un niveau de confiance modéré que UNC-VOLT est lié au GRU, sur la base de la convergence de TTP, d'infrastructure partagée, et de victimologie cohérente, tout en notant que ces éléments pourraient être des faux drapeaux »).

#### 9.2 Fait, déduction, hypothèse, inconnue

Cette distinction — empruntée à la rigueur forensique — doit être explicite dans chaque produit CTI.

Un **fait** est un observable vérifiable : « l'attaquant a utilisé le domaine C2 `update-srv-infra[.]xyz`, enregistré le 15 janvier 2026 via le registrar NameCheap, résolvant vers l'IP 185.xx.xx.xx (ASN: Serverius, Pays-Bas) » — vérifiable par passive DNS, Whois, et les artefacts IR.

Une **déduction** est une conclusion logique tirée de faits vérifiés : « l'attaquant a exploité la vulnérabilité CVE-2024-21887 (Ivanti Connect Secure) comme vecteur d'accès initial, car les logs du VPN Ivanti montrent une requête d'exploitation correspondant à la signature publique de cette CVE, suivie immédiatement d'une session authentifiée avec un compte de service compromis » — déduction forte, basée sur la corrélation de deux sources indépendantes.

Une **hypothèse** est une interprétation plausible non confirmée : « UNC-VOLT est probablement lié au GRU car les TTP observées sont compatibles avec le tradecraft de Sandworm, l'infrastructure partage des patterns d'enregistrement avec des campagnes Sandworm précédentes, et la victimologie (opérateur d'énergie européen) est cohérente avec les objectifs stratégiques du GRU » — hypothèse étayée par un faisceau d'indices mais qui admet des alternatives (faux drapeaux, acteur imitant Sandworm, infrastructure partagée accidentellement).

Une **inconnue** est ce que l'investigation n'a pas pu déterminer : « l'investigation n'a pas pu confirmer si l'attaquant a exfiltré des données du réseau SCADA — les logs de supervision ne couvraient pas la période concernée ».

#### 9.3 Le raisonnement abductif

L'analyste CTI pratique le raisonnement abductif — l'inférence à la meilleure explication. Face à un ensemble d'observables, il cherche l'explication qui rend compte du plus grand nombre d'observations de la manière la plus simple et la plus cohérente. Ce n'est pas de la déduction (certitude logique) ni de l'induction (généralisation statistique) — c'est un raisonnement probabiliste qui accepte l'incertitude et qui doit être accompagné d'un niveau de confiance.

---

### Chapitre 10 — Techniques analytiques structurées (TAS)

#### 10.1 ACH — Analysis of Competing Hypotheses

L'ACH est la technique analytique structurée la plus importante pour l'analyste CTI. Développée par Richards Heuer (CIA, 1999), elle force l'analyste à formuler explicitement les hypothèses concurrentes et à évaluer chaque évidence contre chaque hypothèse — pas seulement contre l'hypothèse préférée.

**Le processus ACH en 7 étapes :**

**Étape 1 — Formuler les hypothèses :** lister toutes les hypothèses plausibles (minimum 3-4). Les hypothèses doivent être mutuellement exclusives (si H1 est vraie, les autres sont fausses) et collectivement exhaustives (l'une d'entre elles doit être vraie). Dans MERIDIAN : H1 (GRU/Sandworm), H2 (Chine/Volt Typhoon-like), H3 (mercenaire cyber), H4 (cybercriminel sophistiqué).

**Étape 2 — Lister les évidences :** toutes les données pertinentes, avec leur source et leur fiabilité. Les évidences incluent les faits observés (TTP, IoC, infrastructure, victimologie), les déductions, et les absences significatives (le fait que l'attaquant n'a PAS déployé de ransomware est une évidence — elle est incohérente avec H4).

**Étape 3 — Construire la matrice :** colonnes = hypothèses, lignes = évidences. Pour chaque cellule : l'évidence est-elle cohérente (C), incohérente (I), ou non applicable (N) avec l'hypothèse ?

**Étape 4 — Évaluer la matrice :** la clé de l'ACH n'est PAS de choisir l'hypothèse avec le plus de « C ». C'est d'éliminer les hypothèses avec le plus de « I ». La logique : une seule incohérence forte peut invalider une hypothèse, alors que la cohérence ne prouve rien (un acteur peut être cohérent avec une hypothèse sans que cette hypothèse soit correcte).

**Étape 5 — Identifier les évidences diagnostiques :** les évidences qui différencient le plus entre les hypothèses (cohérentes avec une hypothèse et incohérentes avec les autres) sont les plus précieuses. Les évidences cohérentes avec toutes les hypothèses ne sont pas diagnostiques — elles ne discriminent pas.

**Étape 6 — Conclure :** l'hypothèse la moins réfutée (avec le moins d'incohérences) est la conclusion, accompagnée d'un niveau de confiance. Si plusieurs hypothèses sont également non réfutées, la conclusion est « insuffisamment déterminé — données supplémentaires nécessaires ».

**Étape 7 — Identifier les milestones de révision :** quelles données nouvelles changeraient la conclusion ? Si un IoC de Sandworm est identifié dans l'infrastructure C2, H1 est renforcée. Si un tool custom chinois est trouvé dans les artefacts, H2 est renforcée. Ces milestones guident la collecte future.

#### 10.2 Fil rouge — MERIDIAN : la matrice ACH

> **🔎 MERIDIAN — Épisode 6**
>
> Élise construit la matrice ACH pour les 4 hypothèses sur l'identité de UNC-VOLT.
>
> | Évidence | H1 GRU/Sandworm | H2 Chine/VoltTyphoon | H3 Mercenaire | H4 Cybercriminel |
> |----------|:---:|:---:|:---:|:---:|
> | Ciblage OIV énergie européen | C | C | C | I |
> | Pré-positionnement OT sans action | C | C | C | I |
> | Exploitation Ivanti (CVE-2024-21887) | C | C | C | C |
> | DLL sideloading (technique spécifique observée) | C | C | C | N |
> | Pas de ransomware, pas d'exfiltration financière | C | C | C | I |
> | Infrastructure C2 dans ASN Serverius (NL) | C | N | C | C |
> | Patterns de beaconing similaires à Sandworm/CaddyWiper | C | I | N | N |
> | Horaires d'activité UTC+3 | C | I | C | N |
> | Aucun outil custom chinois dans les artefacts | N | I | N | N |
> | Victimologie cohérente avec les objectifs GRU post-2022 | C | N | N | I |
>
> **Résultat :** H4 (cybercriminel) est éliminée (3 incohérences fortes). H2 (Chine) est affaiblie (3 incohérences — patterns de beaconing non chinois, horaires non chinois, pas d'outil chinois). H3 (mercenaire) reste possible mais peu étayée. H1 (GRU/Sandworm) est l'hypothèse la moins réfutée — conclusion avec **confiance modérée** (les TTP et la victimologie convergent, mais pas de preuve technique directe comme un outil Sandworm identifié ou un IoC partagé confirmé).

#### 10.3 Autres TAS

**Key Assumptions Check :** identifier les hypothèses implicites qui sous-tendent l'analyse et les tester explicitement. Exemple dans MERIDIAN : « Nous supposons que l'attaquant est étatique parce que l'OT est ciblé et qu'il n'y a pas de rançon » — est-ce une hypothèse valide ? Les cybercriminels ne ciblent-ils jamais l'OT ? (réponse : ils le font parfois par erreur ou par opportunisme, mais l'absence de toute monétisation après 6 mois rend cette hypothèse faible).

**Red Hat Analysis :** se mettre dans la peau de l'adversaire. « Si j'étais UNC-VOLT (un acteur étatique cherchant à pré-positionner dans les infras critiques européennes), pourquoi aurais-je ciblé EDE ? Quelles seraient mes prochaines étapes ? » Cette perspective aide à anticiper les actions futures de l'acteur et à formuler les recommandations défensives.

**Méthode des cônes :** analyse prospective par scénarios. Le cône d'évolution (probable → plausible → possible → imaginable) appliqué à la question « UNC-VOLT va-t-il revenir cibler EDE dans les 12 prochains mois ? ». Scénario probable : oui, avec un vecteur d'accès différent (les vulnérabilités précédentes sont patchées). Scénario plausible : ciblage d'un sous-traitant d'EDE (supply chain). Scénario possible : passage à l'action destructive (sabotage OT). Scénario imaginable : utilisation des accès pour une opération d'influence (fuite de données internes pour déstabiliser).

---

### Chapitre 11 — Gestion des biais cognitifs en analyse CTI

#### 11.1 Le biais de confirmation

Le piège le plus dangereux et le plus universel. L'analyste qui suspecte APT28 cherche les IoC d'APT28, trouve des similitudes (forcément — les techniques ATT&CK sont partagées), et conclut « c'est APT28 » sans avoir testé les alternatives. Contremesure : l'ACH (qui force à tester toutes les hypothèses), le devil's advocate (un collègue est désigné pour argumenter contre la conclusion principale), et la question systématique « qu'est-ce qui pourrait contredire cette conclusion ? ».

#### 11.2 Le biais de disponibilité

L'analyste surévalue les événements récents ou médiatisés. Le dernier rapport Mandiant parle de Volt Typhoon — donc tout comportement LotL est attribué à Volt Typhoon, même si 50 autres acteurs utilisent les mêmes techniques. Contremesure : rechercher systématiquement les acteurs alternatifs qui utilisent les mêmes TTP (la matrice ATT&CK Navigator montre tous les acteurs associés à une technique).

#### 11.3 L'anchoring

L'analyste s'accroche à la première information reçue. Le premier rapport d'IR disait « ransomware » (parce qu'un fichier chiffré a été trouvé) — toute l'investigation CTI est cadrée comme un incident ransomware, même quand les indices pointent vers de l'espionnage avec un wiper déguisé en ransomware (exactement le modus operandi de NotPetya). Contremesure : réévaluer périodiquement les hypothèses à la lumière des données nouvelles, et accepter que la première impression soit fausse.

#### 11.4 Le mirror imaging

L'analyste prête à l'adversaire sa propre logique. « Aucun acteur rationnel ne ciblerait cette PME de 50 personnes » — faux : la PME est sous-traitante d'un OIV, et c'est le vecteur d'accès supply chain. L'analyste occidental qui pense « aucun État ne risquerait une escalade en sabotant une infrastructure civile » projette sa propre rationalité sur un adversaire qui peut avoir une grille de calcul radicalement différente. Contremesure : le Red Hat Analysis (se mettre dans la peau de l'adversaire avec sa logique, ses contraintes, et ses objectifs — pas les nôtres).

#### 11.5 Le groupthink

L'équipe converge vers un consensus sans examen critique. Le premier analyste dit « c'est Sandworm », les autres acquiescent parce que c'est plausible et que personne ne veut être le contradicteur. Contremesure : le devil's advocate institutionnalisé (dans chaque analyse d'attribution, un analyste est formellement désigné pour argumenter contre la conclusion du groupe), et le pré-mortem (« imaginons que notre conclusion est fausse — pourquoi aurait-elle échoué ? »).

#### 11.6 Le biais d'attribution

L'analyste attribue trop vite et avec trop de confiance. La pression est forte : le RSSI veut savoir « qui », les médias veulent un nom, et l'analyste veut montrer sa valeur. Résultat : une attribution hâtive basée sur un indice fragile (un IoC partagé, une technique commune) présentée avec une confiance excessive. Contremesure : la discipline du niveau de confiance (Ch.13 — jamais de conclusion sans qualification), et le rappel que « insuffisamment déterminé » est une conclusion valide et souvent la plus honnête.

---

### Chapitre 12 — Évaluer la fiabilité des sources et la crédibilité de l'information

#### 12.1 Le système Admiralty adapté à la CTI

Le système de cotation Admiralty (NATO standard) évalue indépendamment la fiabilité de la source et la crédibilité de l'information. La **fiabilité de la source** (A à F) : A = complètement fiable (source avec un historique de fiabilité parfait — CERT-FR, CISA), B = habituellement fiable (éditeur CTI réputé — Mandiant, CrowdStrike), C = assez fiable (source avec un historique mixte), D = habituellement non fiable, E = non fiable, F = fiabilité inévaluable (nouvelle source sans historique). La **crédibilité de l'information** (1 à 6) : 1 = confirmée (corroborée par au moins une source indépendante), 2 = probablement vraie (cohérente avec ce qu'on sait, source fiable), 3 = possiblement vraie (pas d'incohérence mais pas de corroboration), 4 = douteuse (incohérences mineures), 5 = improbable (incohérences majeures), 6 = crédibilité inévaluable.

La cotation systématique de chaque source et de chaque information dans le TIP (OpenCTI, MISP) est une discipline fondamentale. Pas de renseignement sans cotation.

#### 12.2 Les biais des sources

Les **rapports vendor** ont un biais commercial : l'éditeur a intérêt à dramatiser la menace (pour vendre ses produits et services de CTI), à nommer ses découvertes avec des noms accrocheurs (pour la couverture médiatique), et à attribuer à des acteurs étatiques (plus impressionnant que « cybercriminel inconnu »). Ce biais ne rend pas les rapports inutilisables — il rend nécessaire la lecture critique. L'analyste qui prend un rapport Mandiant comme vérité absolue fait une erreur ; l'analyste qui le lit en évaluant les évidences présentées, en identifiant les lacunes, et en formulant ses propres conclusions fait son travail.

Les **rapports gouvernementaux** ont un biais politique : l'attribution publique par un gouvernement (US, UK, EU) sert parfois un objectif diplomatique autant que sécuritaire. L'attribution de NotPetya à la Russie en 2018 était techniquement solide mais aussi politiquement motivée. L'analyste utilise ces attributions comme un indice (source généralement fiable, crédibilité élevée) mais ne les traite pas comme des preuves — il les évalue avec la même rigueur que les autres sources.

---

### Chapitre 13 — Niveaux de confiance et formulation analytique

#### 13.1 Les trois niveaux

**Confiance élevée :** la conclusion est basée sur des informations de haute qualité provenant de sources multiples et indépendantes. Les évidences sont convergentes et les hypothèses alternatives sont réfutées ou peu plausibles. L'analyste a un haut degré de certitude, mais la certitude absolue n'existe pas. Formulation : « Nous évaluons avec un niveau de confiance élevé que... »

**Confiance modérée :** la conclusion est basée sur des informations de qualité raisonnable, partiellement corroborées. Certaines hypothèses alternatives restent plausibles mais moins soutenues par les données. Formulation : « Nous évaluons avec un niveau de confiance modéré que... » — c'est le niveau le plus fréquent en CTI.

**Confiance faible :** la conclusion est basée sur des informations fragmentaires, non corroborées, ou provenant de sources à fiabilité limitée. Les hypothèses alternatives sont aussi plausibles que la conclusion principale. Formulation : « Il est possible que... » ou « Les données disponibles sont insuffisantes pour déterminer avec confiance... »

#### 13.2 Les formulations à utiliser et à éviter

**À utiliser :** « Nous évaluons que... » (conclusion analytique), « Les évidences suggèrent que... » (déduction), « Il est plausible que... » (hypothèse), « L'investigation n'a pas pu déterminer... » (inconnue reconnue), « Sous réserve de confirmation par... » (conditionnel).

**À éviter :** « Il est certain que... » (la certitude n'existe pas en renseignement), « Nous savons que... » (trop assertif — on évalue, on ne sait pas), « Il est prouvé que... » (le renseignement n'est pas une preuve judiciaire), « Indubitablement... » (non).

#### 13.3 Le « what if I'm wrong »

Pour chaque conclusion clé, l'analyste documente ce qui changerait si elle était fausse et quels indicateurs permettraient de le détecter. Exemple dans MERIDIAN : « Si UNC-VOLT n'est PAS lié au GRU (H1 fausse), les indicateurs de révision seraient : découverte d'un outil custom chinois dans les artefacts, identification d'une infrastructure C2 liée à un groupe chinois connu, ou victimologie incohérente avec les objectifs stratégiques russes (par exemple, ciblage d'un pays allié de la Russie). »

---

### Chapitre 14 — Corrélation, recoupement et analyse multi-sources

#### 14.1 Les types de corrélation

La **corrélation technique** est la plus directe : le même IoC (hash, domaine, IP) apparaît dans deux sources indépendantes. Si le domaine C2 de l'incident EDE apparaît dans un rapport Mandiant sur une campagne Sandworm, c'est une corrélation technique forte — mais il faut vérifier que les deux sources sont réellement indépendantes (Mandiant n'a-t-il pas simplement ingéré les IoC d'EDE via un feed ?).

La **corrélation TTP** est plus nuancée : les mêmes techniques ATT&CK sont observées dans deux incidents. C'est un indice de possible lien — mais les techniques ATT&CK sont partagées par de nombreux acteurs (T1059.001 PowerShell est utilisé par quasiment tout le monde). C'est la procédure (le « comment exactement ») qui discrimine, pas la technique générique.

La **corrélation victimologique** est sous-utilisée et pourtant puissante : le même type de victime (secteur énergie, même géographie, même profil d'organisation) est ciblé dans plusieurs incidents. Si 4 opérateurs d'énergie européens sont ciblés en 6 mois avec des TTP similaires, la probabilité d'un même acteur avec un programme de ciblage systématique est élevée.

#### 14.2 Le faisceau d'indices

Aucune corrélation isolée ne suffit pour une conclusion. C'est la convergence de multiples corrélations indépendantes qui construit la confiance. Un IoC partagé + des TTP similaires + une victimologie cohérente + un timing compatible + une infrastructure avec les mêmes patterns d'enregistrement = un faisceau d'indices qui soutient l'attribution. Un seul de ces éléments isolé ne suffit pas — les IoC sont réutilisables, les TTP sont partagées, et la victimologie peut être coïncidentielle.

#### 14.3 Le danger de la circularité

La circularité est le piège le plus insidieux de la corrélation. La source A publie un rapport attribuant une campagne à APT28. La source B reprend cette attribution dans son propre rapport, en citant A. La source C cite B. L'analyste voit « 3 sources indépendantes attribuent à APT28 » — mais en réalité, une seule source a fait l'analyse, les deux autres l'ont propagée. La « corroboration » est illusoire. Contremesure : toujours remonter à la source primaire. Si les 3 rapports citent les mêmes IoC et la même analyse, c'est une seule source, pas trois.

---

## PARTIE IV — PROFILAGE D'ACTEUR ET ATTRIBUTION

*Comment construire un profil d'acteur, analyser son tradecraft, et naviguer dans la discipline la plus sensible de la CTI : l'attribution.*

---

### Chapitre 15 — Construire un Threat Actor Profile

#### 15.1 Les composantes du profil

Un profil d'acteur complet comprend : **identité et alias** (pseudos, clusters, noms selon les vendors — avec les mappings croisés), **sponsor présumé** (avec niveau de confiance explicite — « attribution GRU avec confiance modérée basée sur... »), **objectifs** (espionnage, sabotage, gain financier, pré-positionnement — déduits de la victimologie et des actions on objectives), **victimologie** (secteurs, géographies, profils d'organisations ciblées — l'outil d'attribution le plus sous-estimé : un acteur qui cible systématiquement les opérateurs d'énergie européens a un profil très différent d'un acteur qui cible des entreprises de toutes tailles dans tous les secteurs), **TTP** (mapping ATT&CK avec les procédures spécifiques — pas juste les techniques génériques), **outils** (malware custom, frameworks C2, outils légitimes détournés — la proportion custom/commodity/LOL est un indicateur de sophistication), **infrastructure** (patterns d'enregistrement de domaines, hébergement préféré, ASN récurrents, certificats — le « fingerprint infrastructurel »), **campagnes** (historique des opérations connues avec timeline), et **évolution** (comment le tradecraft change dans le temps — un acteur qui change ses TTP est un acteur qui apprend de ses détections).

#### 15.2 La victimologie comme outil d'attribution

La victimologie est l'outil d'attribution le plus sous-estimé et le plus résistant aux faux drapeaux. Un attaquant peut imiter les TTP d'un autre acteur, utiliser la même infrastructure, et déployer un outil similaire — mais il ne peut pas facilement falsifier sa victimologie. Un acteur qui cible systématiquement les opérateurs d'énergie, les sous-traitants de défense, et les agences gouvernementales en Europe a un profil de victimologie qui pointe vers un nombre limité de sponsors possibles. La corrélation victimologique est donc un complément essentiel à la corrélation technique.

---

### Chapitre 16 — Analyse des TTP et du tradecraft

#### 16.1 Au-delà du mapping ATT&CK

Le mapping ATT&CK (« l'acteur utilise T1059.001 PowerShell ») est nécessaire mais insuffisant pour le profilage. Ce qui distingue les acteurs entre eux, c'est la **procédure** — le « comment exactement ». Deux acteurs peuvent utiliser PowerShell (même technique) avec des méthodes radicalement différentes : l'un utilise `-EncodedCommand` avec un payload en base64, l'autre utilise `Invoke-Expression` avec un téléchargement depuis un serveur compromis. Ces différences procédurales sont le « fingerprint comportemental » de l'acteur — plus durable que les IoC et plus distinctif que les techniques ATT&CK génériques.

#### 16.2 Le tradecraft comme signature

Le tradecraft est l'ensemble des choix opérationnels de l'attaquant : quel vecteur d'accès initial, quel outil pour le mouvement latéral, quel mécanisme de persistence, quel pattern de beaconing C2, quelle méthode d'exfiltration, et quel niveau d'OPSEC. Ces choix forment un « style » qui est relativement stable dans le temps (changer de tradecraft coûte cher en entraînement et en risque opérationnel). L'analyste CTI qui documente le tradecraft d'un acteur au niveau procédural — pas juste au niveau technique ATT&CK — construit un profil qui permet la détection et l'attribution même quand les IoC changent.

---

### Chapitre 17 — Attribution : méthode, rigueur et limites

#### 17.1 Les niveaux d'attribution

L'attribution opère à trois niveaux de profondeur croissante. L'**attribution technique** (quel outil a été utilisé, quelle infrastructure) est la plus facile — c'est le domaine du forensic et de l'analyse de malware. L'**attribution opérationnelle** (quel groupe a conduit l'opération) est plus difficile — elle repose sur la corrélation de TTP, d'infrastructure, et de victimologie. L'**attribution stratégique** (quel État ou organisation a commandité l'opération) est la plus difficile — elle intègre le contexte géopolitique, les capacités connues, les intérêts stratégiques, et parfois du renseignement humain ou technique non public. Chaque niveau a son propre seuil de preuve et son propre niveau de confiance.

#### 17.2 Les pièges de l'attribution

Les **false flags** sont la menace la plus sérieuse : un acteur imite délibérément les TTP, les outils, ou l'infrastructure d'un autre acteur pour brouiller l'attribution. Olympic Destroyer (2018) est le cas d'école : le malware contenait des fragments de code de Lazarus Group (DPRK), mais l'attaque a finalement été attribuée au GRU (Russie) qui avait planté ces faux indices. Les **outils partagés** compliquent l'attribution : Cobalt Strike est utilisé par des dizaines d'acteurs étatiques et criminels — sa présence ne discrimine aucun acteur. Les **biais géopolitiques** peuvent déformer l'analyse : attribuer à la Russie ou à la Chine « par défaut » parce que le contexte géopolitique le rend plausible, sans évidences techniques suffisantes.

#### 17.3 Le devoir de prudence

Une attribution erronée a des conséquences réelles : décisions de sécurité mal orientées (si on croit que c'est un cybercriminel alors que c'est un État, les contre-mesures sont inadaptées), tensions diplomatiques (si un gouvernement attribue publiquement une attaque à un État sur la base d'une analyse CTI insuffisante), et poursuites judiciaires erronées. L'analyste qui attribue porte une responsabilité — d'où la discipline du niveau de confiance et du « what if I'm wrong ».

---

### Chapitre 18 — Le naming problem et la gestion des clusters

Chaque éditeur CTI nomme les acteurs selon sa propre convention : CrowdStrike utilise des animaux (Bear = Russie, Panda = Chine), Microsoft utilise des phénomènes météo (Blizzard = Russie, Typhoon = Chine), Mandiant utilise APT/UNC/FIN, ESET utilise des noms de créatures. Résultat : APT28 = Fancy Bear = Forest Blizzard = Sofacy = Sednit = Pawn Storm — le même acteur avec 6+ noms.

Le problème du **split/merge** aggrave le chaos : deux vendors peuvent traquer le même acteur sous deux clusters différents (split), ou regrouper deux acteurs distincts sous un même nom (merge). Les fusions sont rétrospectives : quand un vendor détermine que UNC-2452 et NOBELIUM sont le même acteur, il les fusionne — mais pendant des mois, les deux noms ont coexisté dans les rapports.

La discipline du cluster : quand l'analyste observe une activité nouvelle qui ne matche aucun acteur connu, il crée un cluster temporaire avec un nom interne (UNC-VOLT dans MERIDIAN). Le cluster est documenté comme « non attribué » jusqu'à ce que suffisamment de données s'accumulent pour soit l'attribuer à un acteur connu (merge), soit le confirmer comme un nouvel acteur (promotion en APT/FIN/etc.), soit le déclasser (l'activité s'arrête sans suite).

---

### Chapitre 19 — Cas de profilage et d'attribution documentés

#### 19.1 SolarWinds / SUNBURST (2020) — attribution à APT29

La campagne supply chain la plus sophistiquée documentée publiquement. L'attaquant a compromis le processus de build de SolarWinds Orion, injecté une backdoor (SUNBURST) dans les mises à jour légitimes, et ciblé environ 18 000 organisations — dont le Trésor américain, le Département d'État, et Microsoft. L'attribution à APT29/SVR repose sur la convergence de multiples indices : TTP cohérentes (supply chain, abus de services cloud, furtivité extrême), infrastructure liée à des campagnes APT29 précédentes, et renseignement gouvernemental (l'attribution publique par les US, UK, et EU cite du renseignement classifié). Le niveau de confiance est élevé — c'est un cas d'école de faisceau d'indices convergents.

#### 19.2 NotPetya (2017) — false flag ransomware

Le wiper le plus destructeur de l'histoire ($10 Mrd de dégâts mondiaux). Distribué via une mise à jour piégée du logiciel de comptabilité ukrainien MeDoc, il se propageait via EternalBlue + Mimikatz. Il ressemblait à un ransomware (demande de rançon affichée) mais était en réalité un wiper (la clé de déchiffrement n'existait pas). L'attribution à Sandworm/GRU repose sur le vecteur (supply chain via un logiciel spécifiquement ukrainien — cohérent avec les campagnes Sandworm contre l'Ukraine), les TTP (EternalBlue + credential dumping — signature Sandworm), et le contexte géopolitique (escalade du conflit russo-ukrainien). Le déguisement en ransomware est un false flag classique : faire croire à du cybercrime pour masquer du sabotage étatique.

#### 19.3 Cloud Hopper (2016-2018) — attribution par victimologie

APT10 (MSS/Chine) a compromis des MSP (Managed Service Providers) pour accéder aux réseaux de leurs clients — des centaines d'entreprises dans des dizaines de pays. L'attribution repose fortement sur la victimologie : les données volées correspondaient aux priorités stratégiques de la Chine (propriété intellectuelle dans les secteurs technologique, industriel, et défense), et le ciblage systématique des MSP (qui donnent un accès à de multiples organisations) est cohérent avec les objectifs d'espionnage à grande échelle du MSS.

#### 19.4 Un cas de révision d'attribution

L'attribution n'est pas définitive — elle peut être révisée quand de nouvelles données apparaissent. L'analyste mature accepte la révision comme un signe de rigueur, pas d'échec. Le cas Olympic Destroyer (2018) illustre ce point : les premiers indices (fragments de code Lazarus) pointaient vers la DPRK. Des analyses approfondies ont révélé que ces fragments étaient des faux drapeaux plantés par le GRU (Russie). L'attribution a été révisée — un processus douloureux mais nécessaire qui a renforcé la crédibilité de la communauté CTI.

---

## PARTIE V — CTI OPÉRATIONNELLE : DE L'INTELLIGENCE À L'ACTION

*Comment le renseignement CTI se traduit concrètement en détections, en hunts, en réponse à incident, et en décisions — y compris le chapitre dédié à la vulnerability intelligence.*

---

### Chapitre 20 — CTI-to-Detection : transformer le renseignement en règles

#### 20.1 Le workflow complet

Le processus CTI-to-Detection est le mécanisme qui transforme le renseignement en capacité de détection opérationnelle. Il suit une séquence structurée.

**Étape 1 — Identification du TTP pertinent :** la CTI identifie un TTP utilisé par un acteur qui représente une menace pour l'organisation. Dans MERIDIAN : UNC-VOLT utilise T1574.001 (DLL Search Order Hijacking) avec une procédure spécifique — placement d'une DLL malveillante dans le répertoire d'installation de l'application de supervision SCADA.

**Étape 2 — Vérification de la couverture actuelle :** l'analyste CTI vérifie avec le SOC si une règle de détection existe déjà pour ce TTP et cette procédure spécifique. Si la réponse est « oui, nous avons une règle Sigma pour T1574.001 », la question suivante est : la règle couvre-t-elle la procédure spécifique de UNC-VOLT (DLL dans le répertoire de l'application SCADA, pas juste le DLL hijacking générique) ?

**Étape 3 — Rédaction de la règle :** si la couverture est insuffisante, l'analyste CTI rédige une règle de détection en **Sigma** (format pivot universel) qui cible la procédure spécifique. Sigma est ensuite converti en SPL (Splunk), KQL (Microsoft Sentinel), EQL (Elastic), ou le langage de requête du SIEM utilisé par l'organisation.

**Étape 4 — Test et tuning :** la règle est testée sur les logs historiques (rétro-hunt) pour vérifier les faux positifs et la couverture. Si le volume de FP est trop élevé, la règle est affinée (ajout de conditions d'exclusion, restriction à un périmètre de machines).

**Étape 5 — Déploiement et monitoring :** la règle est déployée en production, les alertes sont monitorées, et les FP résiduels sont documentés.

**Étape 6 — Feedback :** le SOC reporte à la CTI les résultats (vrais positifs détectés, FP, gaps de logs identifiés). Ce feedback alimente le cycle suivant.

#### 20.2 Le gap analysis

Le gap analysis est l'exercice le plus productif de la CTI-to-Detection. L'analyste CTI liste les TTP des acteurs pertinents pour l'organisation (à partir des profils d'acteurs et des PIR), les croise avec la couverture de détection actuelle (quelles techniques sont couvertes par des règles SIEM, EDR, ou des hunts réguliers), et identifie les gaps (techniques utilisées par les acteurs pertinents mais non détectées). Les gaps sont priorisés par risque (probabilité que l'acteur utilise cette technique contre l'organisation × impact si non détecté) et le SOC les comble progressivement. ATT&CK Navigator est l'outil qui visualise cette analyse : la matrice colorée en vert (couvert), orange (partiellement couvert), et rouge (non couvert) est un livrable immédiatement actionnable.

---

### Chapitre 21 — Vulnerability Intelligence

#### 21.1 Pourquoi la vuln intel est un pilier CTI

L'exploitation de vulnérabilités est le 2ème vecteur d'accès initial derrière le phishing — et le 1er pour les acteurs étatiques sophistiqués (Volt Typhoon, APT40, Sandworm). Savoir quelles vulnérabilités sont activement exploitées in the wild, par quels acteurs, contre quel profil de cible, et avec quelle urgence, est du renseignement critique qui oriente directement la priorisation du patching et la posture défensive.

Le problème du volume : des dizaines de milliers de CVE sont publiées chaque année (plus de 28 000 en 2023, plus de 30 000 en 2024). La grande majorité ne sont jamais exploitées. La CTI filtre le bruit pour concentrer l'attention sur les vulnérabilités qui comptent.

#### 21.2 Le flux de vulnerability intelligence

**Publication CVE :** une vulnérabilité est identifiée et publiée (NVD, éditeur, chercheur).

**Évaluation de criticité technique :** le CVSS (Common Vulnerability Scoring System) mesure la sévérité technique (vecteur d'attaque, complexité, impact). Mais le CVSS seul est insuffisant pour la priorisation : un CVSS de 9.8 sur une technologie que l'organisation n'utilise pas a un risque réel de zéro.

**Détection d'exploitation in the wild :** c'est la donnée la plus critique. Le **CISA KEV** (Known Exploited Vulnerabilities catalog) est le catalogue de référence des vulnérabilités confirmées exploitées activement — mis à jour en continu, avec des dates de correction obligatoires pour les agences fédérales US (référence de fait mondiale). L'**EPSS** (Exploit Prediction Scoring System) calcule la probabilité qu'une CVE soit exploitée dans les 30 prochains jours, basée sur des signaux multiples. Les **sources communautaires** complètent : tweets de chercheurs signalant une exploitation, GreyNoise (détection de mass scanning exploitant une CVE), Shadowserver (monitoring d'Internet à grande échelle).

**Corrélation avec les acteurs :** la donnée de plus haute valeur — quelle vulnérabilité est exploitée par quel groupe. « CVE-2024-21887 (Ivanti Connect Secure) est activement exploitée par au moins 3 clusters d'activité incluant Volt Typhoon et UNC-VOLT » → cette corrélation est du renseignement qui oriente directement le patching prioritaire ET les détections post-exploitation.

**Évaluation de l'exposition :** la CTI apporte le contexte de menace (qui exploite quoi), le vuln management apporte le contexte interne (quels systèmes sont affectés, quels patchs sont disponibles). L'intersection produit une priorisation basée sur le risque réel : vulnérabilité exploitée ITW par un acteur qui cible notre secteur + nous avons les systèmes affectés exposés sur Internet = priorité critique immédiate.

**Production :** flash alert « CVE-2024-21887 activement exploitée — nos appliances Ivanti sont exposées → patch immédiat ou mitigation (disable SAML) » — livré au SOC, au vuln management, et au RSSI dans les heures suivant la détection d'exploitation ITW.

#### 21.3 Fil rouge — MERIDIAN : la piste Ivanti

> **🔎 MERIDIAN — Épisode 7**
>
> L'analyse des artefacts IR confirme que UNC-VOLT a exploité CVE-2024-21887 (Ivanti Connect Secure, RCE via commande d'injection dans le composant SAML) comme vecteur d'accès initial chez EDE. Élise vérifie le CISA KEV : la CVE est listée depuis le 10 janvier 2024. L'EPSS au moment de l'incident indiquait une probabilité d'exploitation de 97 %. Mandiant a publié un rapport liant l'exploitation de cette CVE à des clusters étatiques chinois (UNC5221) — mais aussi à des acteurs indépendants opportunistes.
>
> La corrélation est riche mais ambiguë : l'exploitation d'Ivanti est un indice faible pour l'attribution (trop d'acteurs l'exploitent — c'est une technique « commodity »). En revanche, c'est un renseignement critique pour la défense d'EDE : toutes les appliances Ivanti doivent être patchées, et des détections post-exploitation spécifiques doivent être déployées (recherche de webshells LIGHTWIRE/WIREFIRE dans les répertoires Ivanti).

---

### Chapitre 22 — CTI et Threat Hunting

Le threat hunting est la traduction opérationnelle des hypothèses CTI. Le processus : la CTI formule une hypothèse basée sur le renseignement (« UNC-VOLT utilise le DLL sideloading sur les postes d'ingénieurs OT — si nos postes d'ingénieurs OT sont compromis, on devrait trouver des DLL non signées dans les répertoires d'applications de supervision »). Le hunter traduit l'hypothèse en requête technique (recherche via Velociraptor ou le SIEM de DLL non signées dans des chemins spécifiques, corrélation avec les processus chargés). Les résultats alimentent le cycle : si le hunt est positif (compromission découverte) → escalade IR + mise à jour du profil d'acteur + nouvelles hypothèses. Si le hunt est négatif → renforcement de la confiance dans l'éradication + enrichissement de la baseline (les « normaux » découverts pendant le hunt sont documentés pour réduire les futurs FP).

La boucle vertueuse **CTI → Hunt → IR → CTI** est le mécanisme le plus mature de la sécurité opérationnelle : la CTI oriente le hunting, le hunting découvre des compromissions, l'IR investigue, et les artefacts IR enrichissent la CTI — qui formule de nouvelles hypothèses de hunting. Renvoi vers le cours SOC pour les techniques de hunting détaillées.

---

### Chapitre 23 — CTI et Incident Response

Le flux bidirectionnel CTI ↔ IR est le mécanisme qui rend les deux disciplines plus efficaces ensemble qu'isolément.

**En amont de l'incident :** la CTI fournit le contexte de menace que l'IR utilise pour préparer ses playbooks. « Les acteurs qui ciblent les opérateurs d'énergie utilisent typiquement T1190 (exploitation d'appliances VPN), T1574 (DLL hijacking), et T1003.006 (DCSync) — les playbooks IR doivent couvrir ces scénarios. » La CTI identifie aussi les acteurs les plus probables et leurs motivations — ce qui aide l'IR lead à cadrer la réponse (un acteur de pré-positionnement étatique nécessite une réponse différente d'un affilié RaaS).

**Pendant l'incident :** la CTI contextualise les observations de l'IR en temps réel. « Les TTP observées correspondent au cluster UNC-VOLT / profil Sandworm — anticiper les mécanismes de persistance suivants : DLL sideloading dans les répertoires d'applications, modification des ACL AD, et potentiel wiper pré-positionné. » Cette anticipation oriente l'investigation et évite les mauvaises surprises.

**Après l'incident :** l'IR fournit à la CTI les artefacts, les TTP observées, et les IoC. La CTI les intègre dans le profil d'acteur, met à jour les IoC dans le TIP, produit un rapport de campagne, et enrichit la base de connaissances pour les futurs incidents. Renvoi vers le cours IR de la bibliothèque pour le processus IR complet.

---

### Chapitre 24 — CTI pour le RSSI et la direction

#### 24.1 Le briefing stratégique

Le RSSI et la direction ont besoin de renseignement formulé en termes de risque business, pas en termes de techniques ATT&CK. Le briefing stratégique répond aux questions : quelles menaces sont pertinentes pour notre secteur et notre géographie ? Quelle est l'évolution du risque par rapport au trimestre précédent ? Sommes-nous plus ou moins exposés que nos pairs ? Quels investissements sont prioritaires ? Le format est court (2-3 pages ou 15 minutes de présentation orale), visuel (graphiques de tendance, cartes de chaleur), et focalisé sur les implications business (perte financière potentielle, risque réglementaire, risque réputationnel).

#### 24.2 L'évaluation de risque basée sur la menace (threat-informed)

L'approche classique de l'évaluation de risque (menace × vulnérabilité × impact) est souvent déconnectée de la réalité de la menace : les menaces sont listées de manière générique (« ransomware », « espionnage ») sans corrélation avec les acteurs réels qui ciblent l'organisation. La CTI enrichit l'évaluation de risque avec des menaces concrètes et contextualisées : « le cluster UNC-VOLT cible activement les opérateurs d'énergie européens avec les TTP X, Y, Z — notre exposition à ces TTP est de X % (gap analysis) — le risque est élevé et les mesures prioritaires sont A, B, C ». Renvoi vers le cours GRC pour la méthodologie d'analyse de risques.

---

### Chapitre 25 — Partage de renseignement et communautés

Le partage est un multiplicateur de force : un renseignement partagé avec 10 pairs protège 11 organisations. Les ISACs sectoriels (EE-ISAC pour l'énergie, FS-ISAC pour la finance, H-ISAC pour la santé) sont les structures formelles de partage sectoriel. Les cercles de confiance (FIRST, TF-CSIRT, InterCERT France, groupes de travail ANSSI) permettent les échanges non publics entre pairs. Les plateformes techniques (instances MISP communautaires, feeds TAXII partagés) automatisent le partage d'IoC et de TTP.

Les **règles du partage** : le TLP encadre la diffusion, la Chatham House Rule protège les discussions orales (on peut rapporter le contenu mais pas identifier la source), et la réciprocité est le contrat social (qui prend sans donner finit par être exclu). Les **freins** au partage : la peur de révéler une compromission (paradoxe — partager protège les pairs, qui partageront à leur tour), les contraintes juridiques (RGPD sur les données personnelles dans les IoC, clauses de confidentialité des contrats clients), et la concurrence (entre entreprises du même secteur — les ISACs sont conçus pour surmonter ce frein via la confiance institutionnelle).

#### 25.1 Fil rouge — MERIDIAN : le partage ISAC

> **🔎 MERIDIAN — Épisode 8**
>
> Élise partage les IoC et les TTP de UNC-VOLT avec l'EE-ISAC (European Energy ISAC) via MISP, en TLP:AMBER. En retour, elle reçoit des informations de 3 autres opérateurs d'énergie européens qui ont observé des activités similaires (mêmes patterns de beaconing, mêmes techniques de persistence, ciblage d'appliances Ivanti) dans les 6 derniers mois. L'un d'entre eux a identifié un IoC supplémentaire (un domaine C2 non découvert dans l'incident EDE) qui, analysé via passive DNS, révèle un cluster d'infrastructure plus large. Ce partage est le tournant de l'investigation : la victimologie passe de 1 victime (EDE) à 4 opérateurs d'énergie européens — un programme de ciblage systématique, cohérent avec un acteur étatique.

---

## PARTIE VI — PRODUCTION DE RENSEIGNEMENT

*La partie la plus opérationnelle : comment écrire les livrables CTI — du flash alert au rapport stratégique annuel.*

---

### Chapitre 26 — Les produits CTI : formats, audiences, temporalités

Cartographie complète des livrables CTI. Le **flash alert** (urgence — 0-day exploitée, campagne active ciblant l'organisation, fuite de données confirmée) : 1 page maximum, faits + impact + actions immédiates, diffusion sous 1-2 heures, audience : toute l'équipe sécurité. Le **daily/weekly brief** (résumé des menaces pertinentes de la période) : 1-2 pages, tendances + incidents notables + CVE exploitées + IoC pertinents, audience : SOC manager, RSSI. La **note tactique** (analyse de TTP avec détections) : 3-5 pages, mapping ATT&CK + procédures spécifiques + règles Sigma + recommandations de hunting, audience : analystes SOC, hunters, ingénieurs de détection. Le **rapport de campagne** (analyse approfondie d'une campagne) : 10-20 pages, acteur + TTP + IoC + victimologie + timeline + attribution + recommandations, audience : équipe sécurité, pairs communautaires. Le **profil d'acteur** (dossier complet) : document vivant, 15-30 pages, toutes les composantes du Ch.15, audience : référence long terme, communauté. Le **rapport stratégique** (évaluation de menace sectorielle) : 5-10 pages, tendances + acteurs + risques + recommandations business, audience : RSSI, direction, board. L'**évaluation de risque basée sur la menace** : 5-10 pages, menaces concrètes × exposition × recommandations priorisées, audience : RSSI, risk managers.

---

### Chapitre 27 — Rédiger une note analytique CTI

#### 27.1 La structure

**Résumé exécutif** (5 lignes maximum) : conclusion principale + niveau de confiance + implication + action recommandée. C'est souvent le seul élément lu par le décideur — il doit être autonome. Exemple : « Nous évaluons avec un niveau de confiance modéré que UNC-VOLT est lié au GRU (Sandworm). L'acteur cible systématiquement les opérateurs d'énergie européens avec un objectif de pré-positionnement dans les réseaux SCADA. Nous recommandons le déploiement des détections jointes en annexe et un audit de segmentation IT/OT dans les 30 jours. »

**Contexte :** pourquoi cette note, quel événement déclencheur, quel PIR adressé, quelles sources consultées, et quelles limitations (qu'est-ce que l'analyste n'a PAS pu vérifier).

**Faits observés :** chaque fait avec sa source et son évaluation de fiabilité (cotation Admiralty). La distinction fait/déduction est explicite.

**Analyse :** hypothèses testées (ACH ou équivalent), corrélations multi-sources, raisonnement explicite (pas juste les conclusions — le chemin qui y mène). Le lecteur doit pouvoir évaluer la qualité du raisonnement, pas seulement la conclusion.

**Conclusions :** avec niveaux de confiance explicites pour chaque affirmation clé. Les inconnues sont documentées.

**Implications et recommandations :** actions priorisées — techniques (IoC, détections Sigma, hunts), organisationnelles (posture, audit, formation), et stratégiques (communication, notification, budget).

**Annexes :** IoC complets (format STIX si possible), mapping ATT&CK, captures d'écran horodatées, références des sources.

#### 27.2 La discipline rédactionnelle

Phrases courtes (une idée par phrase). Pas de jargon non défini (chaque acronyme est développé à sa première occurrence). Chaque affirmation est sourcée (entre parenthèses ou en note). Chaque conclusion est qualifiée par un niveau de confiance. Le test de la note : si le résumé exécutif est lu seul, donne-t-il au décideur ce dont il a besoin pour agir ? Si la réponse est non, le résumé doit être réécrit.

---

### Chapitre 28 — Rédiger un profil d'acteur et cartographier une campagne

#### 28.1 Le profil d'acteur comme document vivant

Un profil d'acteur n'est pas un rapport ponctuel — c'est un document vivant mis à jour à chaque nouvelle information. La structure est celle du Ch.15 (identité, sponsor, objectifs, victimologie, TTP, outils, infrastructure, campagnes, évolution). Chaque section est datée et sourcée. Les mises à jour sont versionnées (v1.0 lors de la création, v1.1 après enrichissement communautaire, v2.0 après attribution révisée). Le profil est stocké dans le TIP (OpenCTI) avec les relations vers les IoC, les campagnes, et les malwares associés.

#### 28.2 Le rapport de campagne

Le rapport de campagne reconstitue et documente une série d'incidents liés. La timeline (de la première activité observée à la dernière — avec les lacunes explicites), le mapping des victimes (qui a été touché, dans quel ordre, avec quel vecteur — la victimologie est le cœur du rapport), l'infrastructure (domaines, IP, certificats — et leur évolution dans le temps), les TTP (cohérence ou variations entre incidents), et l'attribution (avec son niveau de confiance et ses limitations). Le rapport de campagne est le livrable de référence pour la communauté — il est partagé via l'ISAC ou en TLP:GREEN/AMBER pour que d'autres organisations puissent se protéger.

---

### Chapitre 29 — Étude critique de livrables CTI

*Ce chapitre examine des exemples de livrables CTI — bons et mauvais — pour développer le sens critique rédactionnel de l'analyste.*

#### 29.1 Ce qui fait un bon rapport CTI

Un bon rapport CTI : pose une question de renseignement claire (pas « voici ce qu'on a trouvé » mais « voici la réponse à votre question »), distingue explicitement les faits, les déductions, et les hypothèses, qualifie chaque conclusion par un niveau de confiance, source chaque affirmation, présente les hypothèses alternatives testées (pas juste la conclusion retenue — le lecteur doit voir que les alternatives ont été considérées), documente les limitations et les inconnues, et formule des recommandations actionnables (pas « soyez vigilants » mais « déployez la règle Sigma suivante sur les postes d'ingénieurs OT »).

#### 29.2 Les erreurs rédactionnelles les plus fréquentes

**L'affirmation sans niveau de confiance :** « UNC-VOLT est un groupe du GRU. » → pas de qualification. Devrait être : « Nous évaluons avec un niveau de confiance modéré que UNC-VOLT est lié au GRU, basé sur... ». **La confusion IoC = renseignement :** un rapport qui liste 200 hash sans contexte n'est pas du renseignement — c'est un dump de données. **Le résumé qui ne résume pas :** un résumé exécutif de 2 pages avec du jargon technique n'est pas un résumé. **L'attribution sur un seul indice :** « un domaine C2 est hébergé sur le même ASN qu'une campagne Sandworm précédente → donc c'est Sandworm » — un ASN est partagé par des milliers de clients, ce n'est pas un indice d'attribution. **Le rapport alarmiste sans évidences :** « MENACE CRITIQUE — votre organisation est ciblée par un APT étatique » basé sur un post de forum non vérifié.

#### 29.3 Exercice d'analyse critique

Le chapitre présente 3 extraits de rapports CTI (anonymisés, inspirés de rapports réels) que l'analyste doit critiquer : identifier les forces (sources multiples, niveaux de confiance explicites, hypothèses alternatives), les faiblesses (affirmations non sourcées, sauts logiques, attribution excessive), et les améliorations possibles. Cet exercice développe le sens critique qui distingue l'analyste consommateur passif de rapports (il lit et transmet) de l'analyste producteur actif de renseignement (il évalue, critique, et produit mieux).

---

## PARTIE VII — PROGRAMME CTI ET MATURITÉ

---

### Chapitre 30 — Construire un programme CTI en entreprise

#### 30.1 Prérequis

Un programme CTI ne fonctionne pas dans le vide. Les prérequis : des logs exploitables (si le SOC n'a pas de SIEM avec des logs de qualité, la CTI ne peut pas alimenter des détections), un SOC opérationnel (la CTI tactique et technique n'a de sens que si un SOC les consomme), un RSSI qui comprend la valeur de la CTI (si la direction voit la CTI comme un « nice to have » et non comme un « must have », le budget sera le premier coupé), et une culture de la menace (les équipes IT et métier doivent accepter que l'organisation EST une cible, pas une éventualité).

#### 30.2 Modèles d'organisation

**CTI intégrée au SOC :** l'analyste CTI est membre de l'équipe SOC. Avantage : boucle courte CTI → détection, connaissance intime des capacités et des gaps du SOC. Inconvénient : risque d'absorption par l'opérationnel (l'analyste passe son temps à traiter des alertes au lieu de faire de l'analyse de fond).

**CTI dédiée :** équipe séparée du SOC, avec sa propre hiérarchie. Avantage : profondeur d'analyse, capacité de travailler sur des missions de moyen/long terme (profilage, attribution, évaluation stratégique). Inconvénient : risque de déconnexion avec l'opérationnel (la CTI produit des rapports que le SOC ne lit pas).

**Modèle hybride :** équipe CTI dédiée avec un « CTI liaison » intégré au SOC pour la boucle courte. C'est le modèle le plus efficace pour les organisations de taille suffisante (3+ analystes CTI).

#### 30.3 Outillage et budget

L'outillage minimal : un TIP (MISP ou OpenCTI — gratuits si auto-hébergés, ~5-20K$/an en SaaS), 1-2 feeds commerciaux prioritaires (Recorded Future ou Mandiant pour la couverture large, Intel 471 ou Flashpoint pour le dark web — 50-150K$/an chacun), et l'intégration SIEM/EDR (connecteurs STIX/TAXII). Le budget analyste est le poste principal : un analyste CTI senior coûte 50-80K€/an en France, un junior 35-50K€. Le ROI se mesure en incidents prévenus, en temps de détection réduit, et en gaps comblés — des métriques traitées au Ch.31.

---

### Chapitre 31 — Métriques et évaluation de la performance CTI

Les métriques de performance CTI sont le mécanisme qui justifie l'investissement et guide l'amélioration continue.

**Métriques de processus :** nombre de PIR adressés (sur le total des PIR actifs), temps moyen de traitement d'un rapport (de la réception à la dissémination), taux de FP des IoC injectés dans le SIEM (objectif : < 5 %), couverture des TTP pertinentes par des détections (% des techniques ATT&CK des acteurs surveillés couvertes par des règles).

**Métriques d'impact :** incidents détectés ou prévenus grâce à la CTI (le renseignement a-t-il conduit à une détection qui n'aurait pas eu lieu sans CTI ?), gaps de détection comblés (combien de nouvelles règles déployées grâce aux recommandations CTI), temps de réponse réduit (l'IR a-t-il été plus rapide grâce au contexte CTI ?), et qualité des attributions (les attributions ont-elles été confirmées ou révisées avec le temps ?).

**Métriques de maturité :** pourcentage des détections basées sur les TTP vs les IoC (plus le % TTP est élevé, plus la CTI est mature — un SOC qui ne détecte que les IoC est au bas de la Pyramid of Pain), diversité des sources (combien de catégories de sources sont couvertes — OSINT seul = immature, OSINT + commercial + interne + communautaire + dark web + technique = mature), et fréquence du feedback (le feedback loop est-il formalisé et régulier, ou inexistant ?).

---

### Chapitre 32 — Veille et intelligence continue

La veille CTI n'est pas un projet ponctuel — c'est un processus quotidien. L'organisation de la veille comprend la consultation des sources prioritaires (adaptée aux PIR — les sources qui répondent aux PIR actifs sont consultées quotidiennement, les autres hebdomadairement), le suivi des vulnérabilités exploitées ITW (CISA KEV mis à jour en continu, EPSS quotidien, alertes CERT-FR — si une CVE affectant une technologie de l'organisation est ajoutée au KEV, c'est un flash alert immédiat), la veille sectorielle (rapports qui concernent le secteur de l'organisation, les technologies utilisées, la géographie), et le suivi des acteurs surveillés (profils d'acteurs mis à jour quand de nouvelles campagnes, TTP, ou infrastructures sont identifiées). Renvoi vers le cours Dark Web pour la veille dark web.

---

### Chapitre 33 — Automatisation, outillage et place réaliste de l'IA

*Ce chapitre traite de l'automatisation et de l'IA avec pragmatisme — en distinguant ce qui est opérationnellement utile aujourd'hui, ce qui est en cours de maturation, et ce qui relève du fantasme.*

#### 33.1 Ce qui peut et doit être automatisé

Le **traitement des feeds** est le candidat idéal à l'automatisation : l'ingestion de feeds STIX/TAXII, la normalisation des IoC, l'enrichissement automatisé (hash → VirusTotal, domaine → Whois/passive DNS, IP → géolocalisation/ASN), le dédoublonnage, et le scoring sont des tâches répétitives à haut volume et à faible valeur analytique — elles doivent être automatisées pour libérer du temps analyste. Les orchestrateurs (SOAR : Cortex XSOAR, Shuffle, Tines) et les connecteurs TIP → SIEM (MISP → Splunk, OpenCTI → Sentinel) font ce travail.

L'**injection des IoC** dans les systèmes de détection est automatisable (et doit l'être — un analyste qui copie-colle des IoC dans le SIEM est un gaspillage de compétence). L'**alerting** sur les mentions de l'organisation dans les sources dark web et les feeds commerciaux est automatisable. Et le **reporting automatisé** sur les métriques de processus (dashboards de couverture, volume de feeds traités, taux de FP) est automatisable.

#### 33.2 Ce que les LLM apportent concrètement (et ce qu'ils n'apportent pas)

Les LLM (GPT-4, Claude, modèles open source) sont des outils utiles pour l'analyste CTI dans des cas d'usage précis et encadrés. Le **résumé de rapports** : un LLM peut résumer un rapport de 30 pages en 1 page — gain de temps significatif pour la veille quotidienne, à condition que l'analyste vérifie le résumé (les hallucinations existent). La **traduction** : les rapports en chinois, russe, farsi, ou coréen sont directement pertinents pour la CTI — un LLM traduit avec une qualité largement suffisante pour le triage (la traduction finale pour un livrable formel doit être vérifiée par un humain). L'**extraction structurée d'IoC** : extraire les hash, domaines, IP, et techniques ATT&CK d'un rapport narratif vers un format structuré (STIX) est un cas d'usage productif. L'**aide à la rédaction** : un LLM peut aider à structurer un premier jet de note analytique — que l'analyste revoit, corrige, et complète.

Ce que les LLM **n'apportent PAS** (et ne doivent pas être utilisés pour) : l'**analyse structurée** (l'ACH, le Key Assumptions Check, et les TAS sont des processus de raisonnement humain qui nécessitent le jugement, l'expérience, et la connaissance du contexte — un LLM qui remplit une matrice ACH produit un résultat plausible mais potentiellement faux, sans que l'erreur soit détectable), l'**attribution** (un LLM qui « attribue » une campagne à un acteur se base sur des corrélations statistiques dans ses données d'entraînement, pas sur une analyse d'évidences — c'est de la pseudo-analyse dangereusement convaincante), la **formulation de niveaux de confiance** (un LLM ne sait pas ce qu'il ne sait pas — il ne peut pas évaluer honnêtement l'incertitude de ses conclusions), et la **détection des biais** (un LLM n'a pas conscience de ses propres biais de données — il les reproduit silencieusement).

#### 33.3 Le risque de la « CTI industrialisée »

L'automatisation poussée à l'extrême crée un risque : la CTI qui produit en volume (des dizaines de rapports par semaine, des milliers d'IoC par jour) mais sans profondeur analytique. Les rapports sont « plausibles » (le LLM écrit bien, les mots sont les bons, les structures sont correctes) mais creux (pas d'analyse réelle, pas d'hypothèses testées, pas de niveaux de confiance calibrés, pas de valeur ajoutée au-delà de ce que le consommateur aurait pu lire lui-même dans les sources). La CTI industrialisée sans analyse est du bruit déguisé en renseignement — et elle est pire que l'absence de CTI, car elle crée une fausse confiance.

La règle : automatiser le traitement (volume, répétitif, faible valeur analytique), assister la production (résumés, traductions, extraction), mais ne jamais automatiser l'analyse (raisonnement, jugement, confiance).

---

## PARTIE VIII — ÉTUDES DE CAS ET SYNTHÈSE

*Trois cas complets qui appliquent l'intégralité du processus CTI. Chaque cas est traité comme une investigation transversale complète — de la formulation des PIR à la production du livrable final.*

---

### Chapitre 34 — Cas complet : profilage et attribution d'un cluster inconnu (synthèse MERIDIAN)

Ce chapitre est la synthèse du fil rouge sous forme de cas autonome. Il reconstitue l'investigation complète d'Élise en un récit continu qui applique chaque compétence enseignée dans le cours.

**Phase 1 — Direction (Ch.5) :** Formulation des 5 PIR avec le RSSI d'EDE. Le plan de collecte identifie 7 catégories de sources à mobiliser.

**Phase 2 — Collecte (Ch.6) :** Artefacts IR de l'incident EDE (source interne, fiabilité A/1). Rapports Mandiant et CrowdStrike sur les acteurs ciblant l'énergie (source B/2). ISAC énergie européen (source B-C/2-3). Passive DNS sur les 3 domaines C2 (source technique, B/1). CISA KEV pour CVE-2024-21887 (source A/1). Monitoring dark web : aucune mention d'EDE — mais 2 mentions du secteur énergie européen sur XSS avec des discussions de ciblage (source C/3).

**Phase 3 — Traitement (Ch.7) :** Structuration dans OpenCTI. Création de l'objet Intrusion Set « UNC-VOLT ». Liaison avec les IoC, les TTP (mapping ATT&CK), les victimes (EDE + 3 opérateurs ISAC). Enrichissement automatisé des IoC (passive DNS, VirusTotal, ASN lookup).

**Phase 4 — Analyse (Ch.9-14) :** Application de l'ACH avec 4 hypothèses (voir épisode 6). Corrélation multi-sources : les patterns de beaconing (intervalles de 32 minutes avec jitter de 10 %) sont identiques à ceux documentés dans un rapport ESET sur Sandworm/CaddyWiper (2022). L'infrastructure C2 partage un registrar (NameCheap) et un pattern de nommage (subdomaines de services cloud légitimes) avec des campagnes Sandworm documentées par Mandiant. La victimologie (4 opérateurs d'énergie européens en 6 mois) est cohérente avec le programme de ciblage des infrastructures critiques européennes attribué au GRU. Key Assumptions Check : « nous supposons que les patterns de beaconing sont distinctifs » — vérification : les intervalles de 32 min + 10 % jitter ne sont documentés que pour Sandworm, pas pour d'autres acteurs. Conclusion : **attribution à Sandworm/GRU (Unit 74455) avec confiance modérée.** Modérée (pas élevée) car : pas de malware Sandworm identifié positivement (les outils custom de Sandworm comme Industroyer ou CaddyWiper n'ont pas été trouvés — l'attaquant utilisait principalement des LOLBins), et les faux drapeaux restent théoriquement possibles.

**Phase 5 — Production (Ch.26-28) :** Élise produit 3 livrables. (1) Note analytique stratégique pour le COMEX d'EDE (5 pages — résumé exécutif + analyse + recommandations business : « un acteur probablement lié au renseignement militaire russe vous cible pour un pré-positionnement dans vos systèmes de contrôle industriel — les mesures prioritaires sont la segmentation IT/OT physique, le patching des appliances Ivanti, et le déploiement des détections jointes »). (2) Note tactique pour le SOC d'EDE (10 pages — TTP détaillées + 12 règles Sigma + plan de hunting sur 4 semaines). (3) Profil d'acteur UNC-VOLT (15 pages, format OpenCTI — le profil est proposé à l'ISAC énergie pour enrichissement communautaire).

**Phase 6 — Partage et feedback (Ch.8, Ch.25) :** Partage ISAC (TLP:AMBER) → 2 opérateurs confirment des activités supplémentaires → le profil est enrichi. L'ANSSI est informée (EDE est OIV). Le feedback du SOC d'EDE après 4 semaines : 3 des 12 règles Sigma ont généré des FP nécessitant un tuning, 1 règle a détecté une activité suspecte qui s'est révélée être un test d'intrusion autorisé (FP documenté), et les hunts n'ont pas révélé de compromission résiduelle (renforcement de la confiance dans l'éradication).

---

### Chapitre 35 — Cas complet : réponse CTI à une campagne de ransomware active

**Contexte :** Un mardi à 14h, le SOC de Sentinelle Cyber détecte un ransomware en cours de déploiement chez un client (ETI industrielle, 1 800 employés, secteur agroalimentaire). L'IR est activé (cours IR). L'analyste CTI, **Nathan Roux** (junior, 18 mois d'expérience), est mobilisé pour contextualiser la menace.

**Identification du groupe (15 min) :** La note de rançon mentionne « BlackBasta ». Nathan vérifie : le format de la note, l'extension des fichiers chiffrés (.basta), et le portail de négociation (.onion) correspondent au groupe BlackBasta connu. Confirmation : le leak site de BlackBasta (monitoring via Ransomwatch) ne liste pas encore le client — le compte à rebours n'a pas commencé.

**Contextualisation (2h) :** Nathan produit une fiche de contexte pour l'IR lead. Profil de BlackBasta : RaaS actif depuis avril 2022, soupçonné d'être composé d'anciens membres de Conti, double extorsion systématique, cible préférentiellement les entreprises industrielles européennes et nord-américaines avec un CA > 50M€. TTP typiques : accès initial via Qakbot (historiquement) ou via phishing direct (post-disruption Qakbot), mouvement latéral via Cobalt Strike, escalade via exploitation Zerologon ou PrintNightmare, exfiltration via rclone avant chiffrement. Cette contextualisation oriente l'IR : chercher les traces de Cobalt Strike, vérifier Zerologon/PrintNightmare, quantifier l'exfiltration.

**Flash alert (1h après détection) :** Nathan émet un flash alert interne (TLP:AMBER) : « Campagne BlackBasta active — client [nom] impacté — IoC joints — tous les clients du secteur agroalimentaire avec profil similaire doivent renforcer le monitoring sur les IoC suivants et vérifier l'exposition aux CVE exploitées par BlackBasta. »

**Alimentation de la cellule de crise (J+1 à J+7) :** Nathan fournit le contexte au RSSI du client pour la communication de crise (« BlackBasta est un groupe criminel connu, pas un acteur étatique — le risque est financier et réputationnel, pas géopolitique »), l'évaluation du risque de publication (« BlackBasta publie systématiquement les données des victimes qui ne paient pas — délai typique : 10-14 jours »), et le monitoring du leak site (surveillance quotidienne — le client apparaît à J+3 avec un compte à rebours de 10 jours).

**Rapport post-incident (J+30) :** Nathan produit le rapport CTI post-incident. TTP observées mappées sur ATT&CK. Corrélation avec les campagnes BlackBasta documentées : les TTP correspondent (Cobalt Strike, rclone, Zerologon). Recommandations : patching Zerologon/PrintNightmare, détection de Cobalt Strike beaconing, et monitoring dark web renforcé. Le rapport est partagé avec l'ISAC du secteur agroalimentaire.

---

### Chapitre 36 — Cas complet : évaluation de menace sectorielle pour un board

**Contexte :** Le RSSI d'un groupe hospitalier français (3 établissements, 5 000 employés, données de santé de 2 millions de patients) demande à Sentinelle Cyber un rapport stratégique sur la menace cyber pour le secteur santé, à présenter au conseil d'administration.

**L'analyste**, **Sofia Leclerc** (CTI senior, spécialisation sectorielle santé), dispose de 3 semaines pour produire un rapport de 10 pages maximum, sans jargon technique, lisible par des administrateurs non experts en cybersécurité.

**Phase collecte (semaine 1) :** Sofia compile les rapports sectoriels (ENISA Threat Landscape for Health, HHS Health Sector Cybersecurity report, rapports H-ISAC, CERT Santé français). Elle analyse les incidents du secteur santé sur les 18 derniers mois (ransomwares sur des hôpitaux français — CHU de Rennes 2023, CH de Cannes 2024, incidents européens documentés). Elle consulte les feeds commerciaux pour les ventes d'accès ciblant le secteur santé (3 annonces sur Exploit.in dans les 6 derniers mois ciblant des « healthcare EU organizations »). Elle analyse les vulnérabilités des technologies utilisées par le client (systèmes HIS, PACS, équipements biomédicaux connectés).

**Phase analyse (semaine 2) :** Sofia identifie 3 menaces prioritaires. (1) Ransomware (menace principale — 67 % des incidents santé en Europe sont des ransomwares ; les groupes LockBit, BlackBasta et Play ciblent activement les hôpitaux ; motivation : les hôpitaux paient parce qu'ils ne peuvent pas se permettre d'arrêter les soins). (2) Vol de données de santé (menace croissante — les dossiers médicaux valent 10-50× plus que les données bancaires sur le dark web, car ils permettent la fraude à l'assurance, l'usurpation d'identité, et le chantage). (3) Espionnage étatique sur la recherche pharmaceutique (menace ciblée — APT29 et APT41 ont ciblé la recherche vaccin COVID ; les groupes hospitaliers avec des programmes de recherche sont des cibles pour l'espionnage de propriété intellectuelle).

**Phase production (semaine 3) :** Le rapport est structuré pour le board. Page 1 : résumé exécutif (« le secteur santé est le 3ème secteur le plus ciblé par les ransomwares en Europe, avec un coût moyen de 4,5 M€ par incident ; notre groupe est exposé ; les mesures prioritaires sont A, B, C »). Pages 2-4 : les 3 menaces avec leur impact business (pas technique — « arrêt des soins pendant X jours », « notification de X millions de patients au titre du RGPD », « amende CNIL potentielle de X M€ »). Pages 5-7 : l'exposition du groupe (technologies vulnérables, surface d'attaque, comparaison avec les pairs du secteur). Pages 8-9 : les recommandations priorisées (avec coût estimé et calendrier). Page 10 : glossaire minimal (5 termes essentiels définis pour le board).

Le rapport est présenté au conseil d'administration par le RSSI, avec Sofia en support pour les questions. Le board approuve un budget de sécurité supplémentaire de 800 K€ sur 18 mois.

---

## ANNEXES

---

### Annexe A — Glossaire CTI

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

### Annexe B — Taxonomie des sources CTI

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

### Annexe C — Templates de livrables CTI

#### Template Flash Alert

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

#### Template Note Analytique CTI

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

#### Template Profil d'Acteur

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

### Annexe D — Cheat sheets analytiques

#### Matrice ACH vierge

| Évidence (source, fiabilité) | H1 : _____ | H2 : _____ | H3 : _____ | H4 : _____ |
|------------------------------|:---:|:---:|:---:|:---:|
| E1 : _____ | C / I / N | C / I / N | C / I / N | C / I / N |
| E2 : _____ | | | | |
| E3 : _____ | | | | |
| **Total incohérences** | | | | |
| **Conclusion** | L'hypothèse avec le MOINS d'incohérences est retenue |

C = Cohérent, I = Incohérent, N = Non applicable

#### Grille Admiralty (évaluation source × information)

**Fiabilité de la source :**
A = Complètement fiable (historique parfait) | B = Habituellement fiable | C = Assez fiable | D = Habituellement non fiable | E = Non fiable | F = Inévaluable

**Crédibilité de l'information :**
1 = Confirmée (corroborée) | 2 = Probablement vraie | 3 = Possiblement vraie | 4 = Douteuse | 5 = Improbable | 6 = Inévaluable

#### Checklist des biais cognitifs

- [ ] **Confirmation :** ai-je cherché ce qui contredit ma conclusion ?
- [ ] **Disponibilité :** suis-je influencé par le dernier rapport médiatisé ?
- [ ] **Anchoring :** suis-je accroché à la première hypothèse ?
- [ ] **Mirror imaging :** est-ce que je prête ma logique à l'adversaire ?
- [ ] **Groupthink :** l'équipe a-t-elle contesté la conclusion ?
- [ ] **Attribution hâtive :** ai-je testé les hypothèses alternatives ?
- [ ] **Circularité :** mes « sources multiples » sont-elles réellement indépendantes ?

#### Workflow CTI-to-Detection

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

### Annexe E — Outils de référence CTI

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

### Annexe F — Mapping de la bibliothèque

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

### Annexe G — Ressources et formation

#### Certifications CTI

| Certification | Organisme | Focus | Prérequis |
|--------------|-----------|-------|-----------|
| GCTI (GIAC Cyber Threat Intelligence) | SANS/GIAC | Processus CTI complet | FOR578 recommandé |
| CREST CTIA (Certified Threat Intelligence Analyst) | CREST | Analyse et production CTI | 2+ ans d'expérience |
| CTIA (Certified Threat Intelligence Analyst) | EC-Council | CTI généraliste | — |
| FOR578 (Cyber Threat Intelligence) | SANS | Formation de référence CTI | — |

#### Formations complémentaires

| Code | Titre | Focus |
|------|-------|-------|
| SANS FOR578 | Cyber Threat Intelligence | Formation CTI de référence |
| SANS FOR508 | Advanced IR, Threat Hunting, Digital Forensics | IR + Hunting guidé par CTI |
| SANS FOR572 | Advanced Network Forensics | Network intelligence |
| SANS ICS515 | ICS Visibility, Detection, and Response | CTI pour les environnements industriels |

#### Rapports annuels de référence

| Rapport | Éditeur | Contenu |
|---------|---------|---------|
| M-Trends | Mandiant/Google | Tendances IR/CTI, TTP observées, métriques |
| CrowdStrike Global Threat Report | CrowdStrike | Panorama menace par pays et par acteur |
| DBIR (Data Breach Investigations Report) | Verizon | Statistiques sur les breaches, vecteurs |
| IOCTA | Europol | Menaces cyber organisées en Europe |
| ENISA Threat Landscape | ENISA | Panorama menace européen |
| Microsoft Digital Defense Report | Microsoft | Tendances globales, telemetry massive |
| ANSSI Panorama de la cybermenace | ANSSI | Menaces sur la France, OIV, secteurs |

#### Blogs et sources quotidiennes

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

#### Communautés

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
