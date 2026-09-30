---
title: 'Fil rouge : Opération BLACKOUT'
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
chapter: 1
chapters: 8
---

> **Contexte narratif — ce fil rouge traverse le cours et se conclut au Ch.32.**
> 
> Un **opérateur de distribution d’énergie européen** (4 pays, 6 200 collaborateurs, classé OIV en France, entité essentielle NIS 2) subit une compromission sophistiquée détectée par son CERT mandaté.
> 
> **L’intrusion** : l’attaquant a exploité une vulnérabilité sur un VPN Ivanti (CVE-2024-21887) pour pénétrer le réseau IT, établi la persistence via DLL sideloading dans le répertoire d’une application de supervision, s’est déplacé latéralement via PsExec et Kerberoasting, puis a pivoté vers le réseau de supervision SCADA via un poste d’ingénierie à double connexion. Il a été détecté et éjecté avant d’atteindre les automates — mais le positionnement était clairement orienté vers les systèmes de contrôle industriel.
> 
> **Le mystère** : aucune donnée exfiltrée, aucun ransomware, aucun sabotage. L’attaquant se pré-positionnait — mais pourquoi, et pour qui ? Les TTP observées sont compatibles avec plusieurs acteurs étatiques : Sandworm/GRU (patterns de beaconing similaires, ciblage énergie cohérent, contexte géopolitique russo-ukrainien), Volt Typhoon (exploitation d’appliance edge, LotL, pré-positionnement infra critique sans action), ou un cluster inconnu.
> 
> L’investigation traverse le cours à travers une dizaine d’épisodes — chacun placé là où il apporte une clé analytique réelle : identification des TTP, comparaison aux profils par pays, analyse du ciblage OT, processus d’attribution et calibration de la réponse, synthèse finale au Ch.32.

-----


## PARTIE I — FONDATIONS

> **Ce que cette partie apprend.** Comprendre ce qu’est une APT comme objet d’analyse (pas juste une attaque sophistiquée), maîtriser le vocabulaire de la discipline, reconnaître la structure d’une intrusion de bout en bout, connaître les techniques de tradecraft qui distinguent l’opérateur étatique, et saisir pourquoi les États utilisent le cyberespace comme instrument de puissance.
> 
> **Ce qu’elle ne couvre pas.** Les profils d’acteurs par pays (Parties II à V), les spécificités OT (Partie VI), les enjeux d’attribution et de droit international (Partie VII).
> 
> **Ce que vous saurez faire après cette partie.** Distinguer une APT d’autres classes de menaces, lire une matrice ATT&CK, comprendre un rapport CTI d’incident, et situer n’importe quelle cyberopération étatique dans le cadre doctrinal d’un État.

-----

### Chapitre 1 — Qu’est-ce qu’une APT : définition, frontières, typologies

#### 1.1 Définition opérationnelle : Advanced, Persistent, Threat

Le terme **APT** (Advanced Persistent Threat) désigne un adversaire généralement state-sponsored ou state-aligned qui mène des cyberopérations sophistiquées, durables et ciblées. Chaque mot compte, et chacun corrige une erreur d’interprétation fréquente.

**Advanced** ne signifie pas forcément « zero-day » ou « malware jamais vu ». Beaucoup d’APT réussissent avec des credentials volés, des vulnérabilités connues non patchées, ou du Living off the Land quasi exclusif (Volt Typhoon est l’exemple canonique). Ce qui est « advanced », c’est la combinaison de quatre éléments : **capacité d’adaptation** (l’attaquant change de TTP quand il est détecté), **tradecraft mature** (OPSEC, évasion, persistence multi-couches), **ressources conséquentes** (temps, budget, opérateurs formés, infrastructure renouvelable), et **renseignement préalable** sur la cible (reconnaissance, HUMINT, collection passive en amont).

**Persistent** signifie que l’objectif n’est pas un coup unique. L’adversaire investit dans la persistence — backdoors multiples, accès redondants, mécanismes de réinfection si éjecté. Le **dwell time** (temps écoulé entre la compromission initiale et la détection) se mesure typiquement en semaines à mois. Pour les opérations de pré-positionnement sophistiquées (Volt Typhoon dans les infrastructures US, Sandworm dans les réseaux énergétiques européens), il se mesure en **années**. La moyenne observée par Mandiant dans son rapport M-Trends est passée de 205 jours en 2014 à 10 jours en 2023 — mais cette baisse cache une bimodalité : les compromissions de ransomware sont détectées vite (impact visible), les compromissions APT silencieuses restent longtemps sous le radar.

**Threat** rappelle qu’on parle d’une menace intentionnelle, dirigée par des humains. Des opérateurs prennent des décisions en temps réel, adaptent leur approche aux contre-mesures de la victime, et ont des objectifs stratégiques définis par un commanditaire — un service de renseignement, un état-major militaire, ou un appareil gouvernemental. Cette dimension humaine distingue l’APT d’un malware automatisé ou d’un ransomware opportuniste.

La définition opérationnelle qui en résulte : une APT est un **intrusion set** suivi dans le temps, caractérisé par une victimologie cohérente, des TTP stables ou évoluant lentement, une infrastructure réutilisée, et dont les objectifs s’inscrivent dans l’agenda stratégique d’un État — directement (opérateur interne à un service) ou indirectement (contractor, proxy, hacktiviste instrumentalisé).

#### 1.2 APT vs cybercriminalité vs hacktivisme vs insider

Les différences structurantes entre les classes de menaces sont résumées dans le tableau suivant. Elles ne sont pas absolues — les frontières s’estompent, on y reviendra — mais elles fixent les repères de base.

|Critère                |APT (étatique)                                       |Cybercriminel              |Hacktiviste                  |Insider                      |
|-----------------------|:---------------------------------------------------:|:-------------------------:|:---------------------------:|:---------------------------:|
|Motivation             |Espionnage, sabotage, influence, pré-positionnement  |Profit financier           |Idéologie, réputation        |Vengeance, profit, négligence|
|Sponsor                |État, proxy, contractor                              |Autonome ou groupe organisé|Groupe idéologique           |Employé/contractant          |
|Temporalité            |Mois à années                                        |Jours à semaines           |Ponctuel                     |Variable                     |
|Sélection cibles       |Très ciblé (secteur, organisation)                   |Opportuniste ou semi-ciblé |Symboles politiques          |Leur propre organisation     |
|OPSEC                  |Très élevé (furtivité maximale)                      |Variable                   |Faible à moyen               |Variable                     |
|Tolérance au bruit     |Très faible                                          |Moyenne (smash & grab)     |Haute (cherche la visibilité)|Variable                     |
|Critère de succès      |Accès maintenu, données exfiltrées, effet stratégique|Monétisation rapide        |Impact médiatique            |Dommage ou gain personnel    |
|Adaptation aux défenses|Systématique                                         |Parfois                    |Rare                         |Aucune                       |

Les frontières sont floues, et c’est précisément ce qui rend l’analyse intéressante. **APT41** (Chine) mène simultanément des opérations d’espionnage étatique validées par le MSS et des opérations cybercriminelles personnelles pour le profit des opérateurs (les indictments DOJ de 2020 les documentent explicitement). Les **groupes ransomware russophones** (LockBit, Conti historique, BlackBasta) opèrent sous une tolérance tacite de l’État russe tant qu’ils ne ciblent pas la CEI — certains ont des liens documentés avec les services (le leak Conti en 2022 a révélé des correspondances évoquant le FSB). **Lazarus** (DPRK) utilise le cybervol de cryptomonnaies comme source de financement étatique — la méthode est du cybercrime, la finalité et l’opérateur sont étatiques. **KillNet** et **NoName057(16)** présentent une esthétique hacktiviste pro-russe mais leur coordination opérationnelle et leur protection relative suggèrent au minimum une connivence avec les services.

Ces zones grises sont traitées au Ch.15 et analysées au Ch.25. Pour l’analyste opérationnel, la règle est simple : **ne pas confondre méthode et finalité**. Un ransomware qui chiffre un hôpital peut être motivé par le profit, l’influence, ou la déstabilisation — la méthode ne détermine pas l’intention.

#### 1.3 Typologie d’objectifs APT

Les APT poursuivent cinq grands types d’objectifs, souvent combinés dans une même opération ou une même campagne.

Le **cyberespionnage** est l’objectif le plus courant en volume. Il vise la collecte de données stratégiques : propriété intellectuelle industrielle (semiconducteurs, aéronautique, pharmaceutique), plans militaires, communications diplomatiques, positions de négociation, secrets commerciaux, données personnelles de cibles d’intérêt (dissidents, journalistes, diplomates). L’espionnage cyber remplace ou complète les méthodes traditionnelles (HUMINT, SIGINT). APT29 (Russie/SVR) en est l’archétype sophistiqué ; APT10 (Chine/MSS) en est l’archétype massif.

Le **pré-positionnement** est l’objectif stratégique le plus inquiétant. Il consiste à maintenir un accès dormant dans des infrastructures critiques — énergie, eau, télécoms, transport — pour une activation future en cas de conflit. L’opération ne vise pas l’exfiltration ni le sabotage immédiat ; elle vise à disposer d’un levier. **Volt Typhoon** (Chine, traité au Ch.22 et Ch.31) en est le cas d’école moderne. Sandworm (GRU) a pratiqué le pré-positionnement sur les infrastructures européennes dans le contexte du conflit ukrainien.

Le **sabotage** vise à endommager ou détruire des systèmes. **NotPetya** (Sandworm, 2017) a causé plus de 10 milliards de dollars de dégâts mondiaux ; **Industroyer** (Sandworm, 2016) a provoqué un blackout à Kiev via la manipulation des protocoles industriels ; **Shamoon** (Iran, 2012) a détruit 30 000 postes de Saudi Aramco. Le sabotage cyber produit des effets physiques (blackouts) ou quasi physiques (destruction de capacité opérationnelle d’une organisation pendant des semaines).

L’**influence** et la **désinformation** manipulent l’opinion et déstabilisent politiquement. L’**ingérence électorale** de 2016 aux US (APT28 — DNC hack, puis publication coordonnée via WikiLeaks et DCLeaks) est le cas fondateur. Les campagnes russes contre les élections européennes, la campagne chinoise sur les réseaux sociaux occidentaux, les opérations iraniennes contre les diasporas sont la suite contemporaine. Le hack-and-leak (vol de données + publication orchestrée) est devenu un instrument standard de la guerre cognitive.

Le **financement** est l’objectif le plus caractéristique de la DPRK, mais d’autres acteurs l’emploient ponctuellement. **Lazarus** vole des crypto-actifs pour financer le programme nucléaire et balistique nord-coréen (Ch.30). Certaines opérations iraniennes ont inclus de la fraude financière pour contourner les sanctions. Ce mélange cybercrime/action étatique brouille les catégorisations classiques.

Ces objectifs ne sont pas exclusifs. Une opération APT29 classique combine espionnage (exfiltration de documents) et pré-positionnement (maintien d’accès). Une campagne Sandworm peut combiner espionnage (reconnaissance OT) et sabotage (wiper). L’analyste lit les TTP pour inférer les objectifs — et inversement, connaître les objectifs oriente l’investigation.

#### 1.4 Le vocabulaire terrain

Le vocabulaire APT a des nuances que les débutants confondent régulièrement. Les préciser évite des contresens d’analyse.

Un **intrusion set** est un ensemble d’activités malveillantes regroupées par TTP, infrastructure et victimologie communes. C’est ce que les vendors CTI appellent un « groupe APT » (APT29, Sandworm, etc.), mais c’est un **regroupement analytique**, pas forcément une seule équipe physique. L’intrusion set peut correspondre à une unité militaire précise (Sandworm = GRU Unit 74455), à un sous-ensemble d’opérateurs d’un service (APT29 regroupe plusieurs sous-groupes au sein du SVR), ou même à un consortium d’opérateurs partageant des outils (certains clusters chinois).

Un **cluster** est un regroupement préliminaire, pas encore attribué ou pas encore formellement promu au rang de groupe nommé. Mandiant utilise le préfixe **UNC** (Uncategorized) : UNC2452 était le cluster initial avant son identification comme APT29 dans l’affaire SolarWinds. Microsoft utilisait historiquement **DEV** (Developing) avant sa refonte en thèmes météo. Promouvoir un cluster en groupe nommé exige une convergence suffisante de TTP, d’infrastructure et d’objectifs dans le temps.

Une **campaign** (campagne) est une série d’intrusions liées par un objectif commun sur une période donnée. Une campagne peut être conduite par un seul groupe APT (campagne APT29 contre les ministères européens des affaires étrangères en 2023-2024) ou par plusieurs (campagne de ciblage des MSP — Managed Service Providers — impliquant APT10 et APT41 autour de 2016-2018).

Les **TTP** (Tactics, Techniques, Procedures) décrivent le « comment » de l’attaquant. Les **tactiques** sont les objectifs à haut niveau (gagner un foothold, établir la persistence). Les **techniques** sont les méthodes générales (phishing, DLL sideloading). Les **procédures** sont les implémentations spécifiques (utilisation d’un document Word avec une macro VBA spécifique, obfuscation par une méthode particulière). Les TTP sont plus durables que les IoC : un attaquant change facilement un hash de malware, rarement son tradecraft profond.

Le **tradecraft** est le savoir-faire opérationnel global : OPSEC, TTP, habitudes, réflexes, style. Un tradecraft mature est un marqueur d’acteur étatique professionnel. Reconnaître un tradecraft (la façon dont Turla compartimente son infrastructure, la manière dont APT29 abuse des services cloud légitimes) est l’un des exercices les plus sophistiqués de l’analyse CTI.

Les **IoC** (Indicators of Compromise) sont les artefacts techniques ponctuels : hash de fichier, adresse IP, domaine, clé de registre, chaîne de caractères. Les IoC vieillissent très vite (hash changé à chaque nouvelle compilation, IP brûlée dès qu’elle est signalée). Leur valeur tactique est immédiate, leur valeur stratégique est faible — d’où la **Pyramide de la Douleur** (David Bianco) qui hiérarchise les indicateurs par coût pour l’attaquant : les TTP sont tout en haut (coût élevé pour changer), les hashs sont tout en bas (coût nul). Cette pyramide structure toute la défense moderne (voir Ch.3).

#### 1.5 Le naming chaos : conventions par vendor

L’un des premiers obstacles de l’apprenant est le **naming chaos** : un même acteur peut avoir 5 à 10 noms différents selon le vendor CTI qui le désigne. Il n’existe pas d’autorité centrale de nommage — chaque éditeur utilise sa propre convention.

**Mandiant** (Google Cloud) utilise historiquement **APTxx** (pour les groupes étatiques attribués : APT28, APT29, APT41), **UNCxxx** (pour les clusters en attente), **FINxx** (pour les groupes financièrement motivés : FIN7, FIN8), et **TEMP.xxx** (préfixe temporaire).

**CrowdStrike** utilise des **animaux par pays** : Bear (Russie — Fancy Bear = APT28, Cozy Bear = APT29), Panda (Chine — Wicked Panda = APT41, Stone Panda = APT10), Chollima (DPRK — Stardust Chollima = APT38, Velvet Chollima = APT43), Kitten (Iran — Charming Kitten = APT35, Fox Kitten), Jackal (hacktivisme), Buffalo (Vietnam — OceanBuffalo = APT32), Crane (Corée du Sud), Spider (cybercrime — Scattered Spider, Wizard Spider).

**Microsoft** a refondu sa convention en 2023 autour de **thèmes météo par origine** : Blizzard (Russie — Midnight Blizzard = APT29, Forest Blizzard = APT28, Seashell Blizzard = Sandworm, Aqua Blizzard = Gamaredon, Secret Blizzard = Turla), Typhoon (Chine — Volt Typhoon, Salt Typhoon, Flax Typhoon, Brass Typhoon = APT41), Sleet (DPRK — Diamond Sleet = Lazarus, Sapphire Sleet = APT38, Emerald Sleet = Kimsuky), Sandstorm (Iran — Peach Sandstorm = APT33, Mint Sandstorm = APT35, Hazel Sandstorm = APT34, Mango Sandstorm = MuddyWater), Storm (cybercrime), Tempest (acteurs privés), Flood (DDoS).

**Kaspersky** utilise des noms variables et créatifs (Turla, Equation Group, BlueNoroff, ProjectSauron) sans convention systématique.

**Secureworks** utilise les **métaux par origine** : Bronze (Chine — Bronze Butler = Tick, Bronze President = Mustang Panda), Cobalt (Russie — Cobalt Mirage = Iran), Gold (cybercrime), Iron (Iran), Tin (DPRK).

**Palo Alto Networks / Unit 42** utilise des noms ciblés par nature (Stately Taurus, Fighting Ursa, Mushroom — plus descriptifs de TTP qu’organisés par pays).

L’**Annexe C** consolide les correspondances. Pour l’opérationnel : quand vous lisez un rapport, notez systématiquement le mapping vers APTxx (Mandiant) ou vers le nom Microsoft — ce sont les conventions les plus largement partagées.

#### 1.6 État des lieux quantitatif

Plusieurs centaines de groupes APT sont suivis publiquement par l’écosystème CTI mondial. L’ordre de grandeur :

- **MITRE ATT&CK Groups** répertorie environ 160 groupes documentés publiquement (février 2026).
- **Malpedia** (Fraunhofer FKIE) référence plusieurs centaines de familles de malware attribuées à des acteurs étatiques.
- **CrowdStrike** déclare suivre plus de 230 acteurs (adversaires nommés, 2024 Global Threat Report).
- **Mandiant** suit plus de 300 intrusion sets dans son périmètre interne (dont beaucoup restent en UNC, non promus en APTxx publics).
- **Microsoft Threat Intelligence** publie une liste de plus de 150 threat actors nommés.

Deux implications pour l’analyste. La première : même un expert ne peut pas connaître en profondeur tous les groupes. La discipline consiste à **maîtriser les 30-40 groupes les plus actifs** (couverts par ce cours), puis à savoir **rechercher efficacement** les autres sur Mandiant, Microsoft TI, MITRE ATT&CK, Malpedia. La seconde : le nombre croît chaque année. La prolifération des capacités offensives (Ch.25) produit une fragmentation des acteurs — plus de contractors, plus de clusters éphémères, plus de difficultés d’attribution.

#### 1.7 Fil rouge — BLACKOUT Épisode 1

> **⚡ BLACKOUT — Épisode 1 : la détection**
> 
> **J+42** depuis la compromission initiale (inconnue à ce stade).
> 
> Le SOC de l’opérateur énergie européen reçoit une alerte de l’EDR sur un **poste d’ingénierie OT** situé sur un site de supervision en France. L’alerte indique un comportement anormal : `rundll32.exe` exécute une DLL non signée située dans `C:\ProgramData\Supervision\plugins\`, et un beaconing HTTPS régulier (toutes les 27 minutes, avec un jitter de ±3 minutes) vers un domaine hébergé derrière Cloudflare.
> 
> Le poste en question est un **double-connecté** : interface 1 sur le réseau IT bureautique (pour les mises à jour, les sessions administrateur), interface 2 sur le réseau de supervision SCADA. C’est un jump host typique — le point le plus sensible de l’architecture, par construction.
> 
> L’ingénieur SOC monte l’incident au CERT mandaté (un CERT privé français, qualifié PDIS par l’ANSSI). Les premières observations du CERT en triage rapide :
> 
> - Persistence via DLL sideloading d’une application de supervision légitime (`SupervisionCenter.exe` charge `plugin_common.dll` à chaque démarrage — la DLL est normalement signée, celle-ci ne l’est pas).
> - Pas de malware custom identifié après un scan initial — le C2 passe par HTTPS vers un domaine d’apparence légitime.
> - Pas de ransomware, pas d’exfiltration massive visible dans les logs réseau, pas de modification détectée sur les automates eux-mêmes.
> 
> **Premier diagnostic du CERT** : « Ce n’est pas un cybercriminel, pas un hacktiviste, pas un incident opportuniste. Le ciblage d’un poste OT, la persistence discrète, l’absence d’action visible, la patience — tous les signaux évoquent une APT en phase de reconnaissance ou de pré-positionnement. La question est : lequel, et pour quoi faire ? »
> 
> Le dossier BLACKOUT commence. Il faudra traverser les six parties suivantes pour le comprendre.

-----

### Chapitre 2 — Cycle de vie d’une intrusion APT

#### 2.1 Modèles de cycle : Kill Chain, Unified Kill Chain, ATT&CK

Plusieurs modèles structurent l’analyse d’une intrusion APT de bout en bout. Ils ne se contredisent pas ; ils offrent des vues complémentaires.

La **Cyber Kill Chain** (Lockheed Martin, 2011) propose sept phases linéaires : Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command & Control, Actions on Objectives. Simple, pédagogique, elle reste la référence conceptuelle d’entrée de gamme. Sa limite : elle suggère une progression linéaire, alors qu’une APT réelle fait des allers-retours (nouvelle reconnaissance interne après chaque étape, re-compromission si éjectée).

La **Unified Kill Chain** (Paul Pols, 2017) enrichit le modèle avec 18 phases couvrant aussi le mouvement latéral, la reconnaissance interne, les pivots vers de nouveaux réseaux, et la persistence multi-couches. Plus complète pour les intrusions sophistiquées, elle est moins pédagogique pour l’introduction mais plus fidèle à la réalité des APT.

**MITRE ATT&CK** (2013, enrichi continuellement) est le framework dominant aujourd’hui. Il organise les TTP en **14 tactiques** (Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact, et — plus récentes — Reconnaissance et Resource Development). Chaque tactique contient de nombreuses **techniques** (200+ au total) et **sous-techniques** (400+). Pour chaque technique, ATT&CK documente les groupes qui l’utilisent, les malwares connus, les mitigations, et les détections. C’est à la fois un langage commun et une base de données. Dans la suite du cours, toutes les TTP sont référencées par leur identifiant ATT&CK (Txxxx).

ATT&CK couvre plusieurs matrices : **Enterprise** (Windows, Linux, macOS, cloud, containers — la plus complète), **Mobile** (iOS, Android), et **ICS** (systèmes industriels, voir Partie VI). Les matrices se complètent pour couvrir les attaques multi-environnements.

La suite du chapitre parcourt le cycle ATT&CK en l’enrichissant des spécificités APT.

#### 2.2 Reconnaissance et Resource Development

La **reconnaissance** (TA0043) est la phase où l’attaquant collecte de l’information sur la cible avant tout contact. Pour une APT étatique, cette phase dure des semaines à des mois et mobilise des sources variées : OSINT (LinkedIn pour identifier les employés et leur rôle, sites d’entreprise, conférences, presse), scan technique (Shodan, Censys pour l’infrastructure exposée), breach databases (credentials potentiellement réutilisables), et parfois HUMINT ou SIGINT quand l’acteur dispose de ces capacités.

Les APT les plus sophistiquées investissent lourdement dans la reconnaissance. APT29 est documenté pour avoir passé des mois à identifier les administrateurs SolarWinds avant la compromission initiale. APT35 (Iran) construit des profils d’ingénierie sociale extrêmement détaillés sur ses cibles (chercheurs, journalistes, dissidents) — jusqu’à des faux profils LinkedIn de « collègues » qui interagissent pendant des mois avant d’aborder l’objectif réel.

Le **Resource Development** (TA0042) est la phase où l’attaquant prépare son infrastructure et ses outils : acquisition de domaines (via des registrars permissifs, avec des identités fictives), mise en place des serveurs C2 (VPS chez des hébergeurs peu coopératifs, ou abus de services cloud légitimes), développement ou acquisition du malware, préparation des comptes d’opération (faux profils LinkedIn, faux comptes email pour le spear-phishing). Pour les APT matures, cette infrastructure est **compartimentée** : chaque opération a sa propre infrastructure, ce qui limite le risque de propagation d’une découverte.

#### 2.3 Accès initial : les vecteurs dominants 2024-2026

L’**Initial Access** (TA0001) est la phase où l’attaquant obtient son premier foothold. Cinq vecteurs dominent aujourd’hui.

**Phishing** (T1566) reste le vecteur statistiquement le plus fréquent. Le spear-phishing APT est très différent du phishing de masse : message personnalisé (fonction, projet en cours, relations), pretexte crédible (invitation à une conférence, message d’un faux collègue, notification d’un service légitime), leurre adapté (document Word avec macro, PDF avec exploit, lien vers un faux portail OAuth). APT29 a excellé dans le **phishing OAuth** — messages imitant des invitations Microsoft Teams ou des demandes d’autorisation d’application, qui, si acceptés, donnent à l’attaquant un accès persistant au compte sans avoir à voler de mot de passe.

**Exploitation d’appliances edge** (T1190) est devenue le vecteur n°1 des APT les plus sophistiquées depuis 2022-2023. Les VPN, firewalls, passerelles web et autres équipements exposés sur Internet sont des cibles privilégiées : ils ne supportent souvent pas d’EDR, leurs vulnérabilités sont exploitables massivement dès publication, et ils donnent un accès privilégié au réseau interne. Les vagues **Ivanti Connect Secure** (CVE-2023-46805, CVE-2024-21887, CVE-2024-21888 en 2024), **Fortinet FortiOS** (multiples CVE 2022-2024), **Citrix ADC / NetScaler** (CVE-2023-4966 — Citrix Bleed), **Barracuda Email Security Gateway** (CVE-2023-2868 exploité par UNC4841/Chine pendant 8 mois), **Palo Alto GlobalProtect** (CVE-2024-3400) ont toutes été exploitées en vagues massives par des acteurs étatiques dans les heures ou jours suivant la publication.

**Supply chain compromise** (T1195) est la catégorie la plus sophistiquée. Elle a plusieurs variantes : compromission d’un éditeur logiciel pour injecter une backdoor dans son produit (SolarWinds / SUNBURST par APT29 — Ch.29 ; 3CX par Lazarus en 2023), compromission d’un MSP pour atteindre ses clients (Opération Cloud Hopper — APT10 sur des MSP internationaux), compromission de dépôts de code (attaques sur des dépendances npm, PyPI), compromission du pipeline de build (modification de binaires signés).

**Credential abuse** (T1078) exploite des credentials volés ou réutilisés. Les sources : breaches publiques (un employé utilise le même mot de passe sur un site compromis et sur son compte professionnel), **infostealers** (Lumma, RedLine, Vidar — qui volent les credentials stockés dans les navigateurs), password spray (essais automatisés de mots de passe faibles sur des comptes M365/Azure AD), **AitM** (Adversary-in-the-Middle phishing, avec outils comme Evilginx, qui capture aussi les cookies de session — permettant de contourner la MFA).

**Exploitation de vulnérabilités publiques** (T1190 aussi) sur des services web exposés (Exchange, OWA, SharePoint, logiciels métier exposés) reste un vecteur massif. Les vagues Exchange **ProxyLogon** (CVE-2021-26855, exploitée massivement par Hafnium / Chine en 2021) et **ProxyShell** (2021) ont compromis des dizaines de milliers d’organisations mondialement.

Le choix du vecteur dépend du niveau de sophistication de l’acteur, de sa patience, et du profil de la cible. Une APT sophistiquée contre une cible de haute valeur privilégiera supply chain ou exploit 0-day. Une APT opportuniste contre des cibles multiples privilégiera l’exploitation massive d’edge devices non patchés.

#### 2.4 Execution, persistence, privilege escalation

Une fois le foothold obtenu, l’attaquant doit **exécuter** son code sur la machine compromise, **persister** à travers les redémarrages et les éjections, et **escalader ses privilèges** pour accéder à plus de ressources.

L’**Execution** (TA0002) se fait via des méthodes qui varient en discrétion. Les plus sophistiquées privilégient la **Living off the Land** : exécuter du code via des outils légitimes du système plutôt qu’en déposant un binaire dédié. PowerShell (T1059.001), wmic (T1047), rundll32 (T1218.011), regsvr32 (T1218.010), mshta (T1218.005), cmd.exe avec des techniques d’obfuscation, Python/Perl interpréteurs sont les LOLBins (Living Off the Land Binaries) de référence. L’exécution sans dépôt sur disque (fileless) via PowerShell en mémoire ou via WMI event consumers est le standard APT moderne.

La **Persistence** (TA0003) doit survivre aux redémarrages et aux tentatives d’éradication. Les mécanismes courants incluent les **tâches planifiées** (T1053, Windows Task Scheduler ou Linux cron), les **services Windows** (T1543.003), les **clés de registre Run/RunOnce** (T1547.001), le **DLL sideloading** (T1574.002 — placer une DLL malveillante dans le répertoire d’une application légitime qui la charge au démarrage ; très utilisée par les APT chinoises), le **COM hijacking** (T1546.015), le **WMI event subscription** (T1546.003 — déclenchement à chaque événement système), et les **bootkits** (T1542 — persistence au niveau UEFI/BIOS, techniquement complexe mais ultra-résiliente).

Les APT les plus sophistiquées déploient de la **persistence multi-couches** : plusieurs mécanismes indépendants, sur des systèmes différents, pour garantir qu’un nettoyage partiel laisse un point de réinfection. APT29 est documenté pour avoir maintenu quatre mécanismes de persistence simultanés sur certaines compromissions importantes.

La **Privilege Escalation** (TA0004) vise à passer d’un compte limité à un compte administrateur local, puis à un compte de domaine, puis à des credentials de service ou à des comptes hautement privilégiés. Les techniques classiques : exploitation de vulnérabilités locales (Windows local privilege escalation — CVE récentes kernel, print spooler), abus de mauvaises configurations (AlwaysInstallElevated, services mal configurés avec permissions faibles), vol de tokens (T1134), DLL search order hijacking (T1574.001). Les privilèges obtenus conditionnent la suite : sans privilèges admin, l’attaquant est limité ; avec des privilèges de domaine, il peut aller quasiment partout.

#### 2.5 Defense evasion et credential access

La **Defense Evasion** (TA0005) est le théâtre principal de l’évolution du tradecraft APT. Les techniques se multiplient avec le renforcement des défenses.

**Obfuscation** (T1027) : brouiller le code pour échapper à la détection signature-based. Scripts PowerShell en base64, binaires packés, strings chiffrées, noms de fonctions randomisés. **Signed binary proxy execution** (T1218) : détourner des binaires Windows signés légitimes (rundll32, regsvr32, mshta, installutil, msiexec) pour exécuter du code malveillant — l’exécution apparaît comme provenant d’un binaire de confiance. **Process injection** (T1055) : injecter du code dans le processus d’une application légitime (explorer.exe, svchost.exe) — le malware n’a pas de processus visible distinct. **Timestomping** (T1070.006) : modifier les timestamps des fichiers pour échapper aux analyses temporelles. **Indicator removal** (T1070) : nettoyage des logs, suppression des traces, désactivation de la télémétrie EDR.

La **Credential Access** (TA0006) est une phase critique car elle conditionne le mouvement latéral. Les outils de référence sont bien connus mais évoluent constamment pour échapper aux EDR.

**Mimikatz** reste l’outil emblématique — extraction de credentials depuis la mémoire LSASS. **DCSync** (T1003.006) : simule un contrôleur de domaine pour récupérer les hashs de tous les comptes AD — devient possible dès qu’on dispose d’un compte avec les bons droits (Domain Admin, ou droits de réplication accordés). **Kerberoasting** (T1558.003) : demander des tickets Kerberos pour des comptes de service avec SPN, puis cracker les hashs hors ligne. **AS-REP Roasting** (T1558.004) : cibler les comptes qui ne nécessitent pas de pré-authentification Kerberos. **Credential dumping** de LSASS (T1003.001) directement via procdump, comsvcs.dll, ou des techniques récentes anti-EDR (NanoDump, SafetyKatz). **Cloud credential access** : vol de tokens SAML (GoldenSAML — forgeage de tokens SAML via la compromission d’ADFS, technique pivot de SolarWinds), abus d’Azure AD (vol de Primary Refresh Tokens, pass-the-cookie, abus d’applications OAuth sur-permissives).

La sophistication de la phase credential access distingue les APT modernes. Les acteurs de pointe (APT29, Sandworm) combinent plusieurs techniques en chaîne, testent les détections, et adaptent leur approche si l’EDR alerte.

#### 2.6 Discovery et lateral movement

Le **Discovery** (TA0007) est la reconnaissance interne au réseau de la victime. L’attaquant cartographie : comptes (net user, net group, AD enumeration via BloodHound / SharpHound), systèmes (net view, DNS enumeration), partages (net share), groupes privilégiés, trusts de domaine, chemins vers les cibles de valeur. **BloodHound** (outil open source, aussi utilisé par les red teamers légitimes) est devenu central : il modélise l’AD en graphe et révèle les chemins d’escalade les plus courts. Les APT sophistiquées l’utilisent couramment.

Le **Lateral Movement** (TA0008) déplace l’attaquant de la machine de foothold vers les cibles de valeur. Plusieurs techniques standards.

**Remote Services** (T1021) : RDP (T1021.001 — le plus courant), SMB/Admin Shares (T1021.002 — `\\target\C$`), WinRM, SSH. Utilisent des credentials légitimes obtenus en phase Credential Access. **PsExec** et **WMI remoting** exécutent des commandes à distance sur des machines du domaine. **Pass-the-Hash** (T1550.002) : authentification avec un hash NTLM sans avoir le mot de passe en clair. **Pass-the-Ticket** (T1550.003) : réutilisation d’un ticket Kerberos volé. **Overpass-the-Hash** : utiliser un hash NTLM pour obtenir un ticket Kerberos (contourne certaines limitations).

Les mouvements latéraux modernes sont **orientés identité** : plutôt que de pivoter machine-à-machine avec des credentials locaux, les attaquants compromettent des comptes de domaine privilégiés et utilisent leurs droits pour accéder aux ressources cibles. La compromission de comptes administrateurs de domaine ou de comptes de service permet un mouvement quasi illimité — d’où l’importance de la segmentation des comptes privilégiés (tiering AD).

Dans le cloud, le mouvement latéral prend des formes différentes : pivoter entre tenants M365 en abusant de relations de partage, se déplacer entre abonnements Azure, exploiter des relations de confiance fédérées SAML.

#### 2.7 Collection, Command and Control, Exfiltration

La **Collection** (TA0009) rassemble les données d’intérêt. Pour une APT d’espionnage, ce sont des documents (Office, PDF), des emails (Exchange, O365), des bases de données, des dumps d’AD, des artefacts de messagerie, des fichiers de code source. Les données sont stagées localement (T1074) — rassemblées dans un répertoire de collecte avant l’exfiltration — et souvent compressées et chiffrées pour faciliter le transfert.

Le **Command and Control** (TA0011) est le canal par lequel l’attaquant contrôle ses implants et reçoit les données. Les C2 modernes ont évolué massivement depuis les années 2010.

**HTTPS mimicry** (T1071.001) : C2 transitant par HTTPS vers des domaines qui imitent des services légitimes (cdn-microsoft-updates.com, office365-patches.net). Catégorisation automatique des domaines côté défense, d’où l’innovation constante côté attaquant. **Domain fronting** (T1090.004) : faire transiter le C2 via un CDN légitime (Fastly, Akamai, Azure CDN) pour masquer la destination réelle — technique moins efficace aujourd’hui car les CDN ont restreint la pratique. **Abus de services cloud légitimes** (T1102) : utiliser Slack, Discord, Telegram, GitHub, Pastebin, Dropbox comme canaux C2. APT29 est documenté pour abuser de Microsoft OneDrive et Google Drive. **DNS tunneling** (T1071.004) : encoder les communications dans des requêtes DNS — lent mais très difficile à bloquer. **Routeurs SOHO compromis** : Volt Typhoon et APT28 (MooBot campaign) ont construit des botnets de routeurs résidentiels pour faire sortir le trafic C2 depuis des IP résidentielles légitimes — rendant la détection réseau extrêmement difficile.

Le **beaconing** est le pattern caractéristique du C2 APT : l’implant « appelle » à intervalles réguliers (chaque X minutes, avec un jitter pour éviter la détection par périodicité) pour recevoir des ordres. Les intervalles sont longs pour les opérations patientes (30 minutes à 24 heures), courts pour les actions en cours (quelques secondes à quelques minutes). La détection du beaconing repose sur l’analyse statistique des patterns temporels — un domaine consulté à intervalles réguliers est suspect, même si le domaine lui-même n’est pas sur liste noire.

L’**Exfiltration** (TA0010) extrait les données collectées. Elle peut utiliser le même canal que le C2 (T1041 — Exfiltration Over C2), un canal alternatif (T1048 — webshell séparé, upload vers un service cloud), ou des supports physiques si l’accès permet (T1052 — rare en pratique APT).

Les APT sophistiquées maîtrisent l’art du **low and slow** : exfiltration étalée dans le temps, à faible débit, pendant les heures de bureau (pour se fondre dans le trafic légitime), par petits volumes. Exfiltrer 10 Go en continu sur quelques heures est détectable ; exfiltrer 100 Mo chaque jour pendant 3 mois est beaucoup moins.

#### 2.8 Impact : espionnage silencieux, destruction, pré-positionnement

La phase **Impact** (TA0040) est l’objectif final. Pour une APT d’espionnage, l’impact est paradoxalement **invisible** : les données ont été collectées et exfiltrées, la cible continue ses activités normales sans le savoir. Pour une APT destructive, l’impact est brutal : wiper qui efface les disques (NotPetya, Shamoon), manipulation OT qui provoque un blackout (Industroyer), chiffrement ransomware déployé par un acteur étatique (Iran contre Albanie 2022 — wiper+ransomware combinés).

Pour une APT de pré-positionnement (Volt Typhoon, Sandworm sur les infras critiques européennes), la phase Impact n’est **pas encore activée**. L’attaquant maintient l’accès et attend un déclencheur (conflit, ordre politique, escalade). Cette configuration — intrusion complète sans impact visible — est la plus difficile à détecter et la plus lourde de conséquences stratégiques. C’est l’enjeu central de la Partie VI.

#### 2.9 Spécificités APT dans ce cycle

Comparé à un incident de cybercrime opportuniste, une intrusion APT se caractérise par quelques spécificités transversales au cycle.

**Durée** : l’APT investit dans le temps. Une intrusion ransomware typique passe de l’accès initial à l’impact en quelques jours à quelques semaines. Une intrusion APT d’espionnage dure des mois à des années, avec des phases d’activité et de dormance.

**OPSEC** : l’APT sophistiquée ne fait pas de bruit. Elle limite ses actions aux minimums nécessaires, évite les outils bruyants, efface ses traces, et adapte son comportement à ce qu’elle détecte de la défense.

**Adaptation** : quand l’APT est détectée ou éjectée d’une partie du réseau, elle revient via ses accès redondants, change de TTP, modifie son infrastructure. L’éradication complète nécessite une réponse coordonnée — d’où la règle « scope before contain » (Ch.28).

**Objectif stratégique** : l’APT ne monétise pas. Elle collecte du renseignement, prépare un levier, ou dégrade une capacité adverse. Cela implique que l’analyse ne peut pas s’arrêter à la technique — comprendre l’objectif stratégique est indispensable pour calibrer la réponse (Ch.32 BLACKOUT).

-----

### Chapitre 3 — Tradecraft et TTP : le comment opérationnel

#### 3.1 La Pyramide de la Douleur

La **Pyramide de la Douleur** (David Bianco, 2013) hiérarchise les indicateurs défensifs par leur coût pour l’attaquant quand ils sont brûlés.

|Niveau                  |Type d’indicateur   |Coût pour l’attaquant                                 |Durée de vie    |
|------------------------|--------------------|------------------------------------------------------|----------------|
|Base (peu douloureux)   |Hash de fichier     |Trivial (recompiler)                                  |Minutes à heures|
|                        |IP                  |Faible (changer de VPS)                               |Heures à jours  |
|                        |Nom de domaine      |Faible (acheter un nouveau)                           |Jours à semaines|
|                        |Artefact réseau/hôte|Modéré (adapter l’implant)                            |Semaines à mois |
|                        |Outils              |Fort (développer de nouveau)                          |Mois à années   |
|Sommet (très douloureux)|TTP / tradecraft    |Maximum (changer les pratiques, former les opérateurs)|Années          |

La leçon défensive fondamentale : **détecter des hashes et des IP, c’est imposer une gêne d’une journée à l’attaquant. Détecter des TTP, c’est imposer un coût qui peut lui prendre des mois à absorber.** La CTI moderne oriente l’effort vers le haut de la pyramide — c’est pour cela qu’ATT&CK est devenu le langage partagé.

Pour l’analyste APT, cela signifie : un IoC (hash, IP) est utile pour une détection immédiate, mais le renseignement qui produit une valeur durable est la description des TTP. Un rapport CTI qui liste 50 hashes a peu de valeur dans trois mois ; un rapport qui décrit précisément comment APT29 abuse des tokens SAML reste utile cinq ans.

#### 3.2 Living off the Land (LotL)

Le **Living off the Land** est la pratique qui consiste à atteindre ses objectifs en utilisant exclusivement les outils légitimes présents sur le système, sans déposer de malware custom. L’avantage est la discrétion — aucun binaire suspect à détecter par signature. L’inconvénient est la traçabilité : les commandes restent loguées, et la détection se fait par anomalie comportementale.

Les **LOLBins** sont les binaires Windows qui peuvent être détournés : rundll32, regsvr32, mshta, msiexec, installutil, wmic, PowerShell, cmd, certutil, bitsadmin, schtasks, sc.exe. Le projet **LOLBAS** (lolbas-project.github.io) maintient un catalogue exhaustif avec les techniques de détournement.

Le **LotL total** (zéro malware custom) est le standard des APT les plus sophistiquées. **Volt Typhoon** est l’exemple canonique : aucun binaire malveillant identifié sur les cibles, tout passe par LOLBins + credentials légitimes. **APT29** pratique un LotL partiel — malware custom en phase 2, mais LotL en mouvement latéral et en phase d’exploration. **Sandworm** utilise davantage de malware custom (wipers, outils OT dédiés) car ses objectifs destructifs imposent des capacités spécifiques.

Pour la défense, le LotL déplace l’effort vers la **détection comportementale** : surveiller les utilisations anormales des LOLBins (PowerShell exécuté depuis un processus inhabituel, rundll32 avec des paramètres suspects, certutil utilisé pour télécharger un fichier — un usage rare pour cet outil administratif).

#### 3.3 Credential access : l’arsenal moderne

Le credential access mérite un traitement détaillé car c’est la phase la plus sensible et la plus défendable.

**Mimikatz** (Benjamin Delpy, 2011) est l’outil emblématique — extraction de credentials depuis LSASS, génération de Golden Tickets et Silver Tickets, Pass-the-Hash, Pass-the-Ticket, DCSync. Détecté par les EDR modernes, il est souvent remplacé par des **réimplémentations furtives** : NanoDump (dump de LSASS en évitant les méthodes surveillées), SafetyKatz (Mimikatz refondu en C#), Rubeus (Kerberos-focused), Impacket (Python toolkit complet utilisé par quasi tous les opérateurs offensifs).

**DCSync** (T1003.006) : technique qui simule un contrôleur de domaine demandant une réplication, pour récupérer les hashs NTLM de tous les comptes du domaine. Nécessite les droits de réplication (Replicating Directory Changes / Replicating Directory Changes All). Une fois le DCSync réussi, l’attaquant a les hashs de tous les comptes, y compris le compte KRBTGT — qui permet les Golden Tickets.

**Golden Ticket** (T1558.001) : forgeage d’un ticket Kerberos TGT valide en utilisant le hash du compte KRBTGT. Résultat : l’attaquant peut s’authentifier comme n’importe quel utilisateur, avec une validité de 10 ans par défaut, sans jamais avoir à interagir avec le contrôleur de domaine pour s’authentifier. Contrer un Golden Ticket nécessite de changer le mot de passe KRBTGT deux fois — opération lourde, souvent retardée.

**Silver Ticket** (T1558.002) : forgeage d’un ticket Kerberos de service pour un service spécifique, en utilisant le hash du compte de service. Moins puissant qu’un Golden Ticket mais moins détectable (ne sollicite pas le DC).

**Kerberoasting** (T1558.003) : demander des tickets Kerberos (TGS) pour des comptes de service ayant un SPN, puis cracker les hashs hors ligne. Fonctionne si les comptes de service ont des mots de passe faibles — ce qui est fréquent historiquement. Défense : mots de passe forts pour les comptes de service (ou managed service accounts).

**AS-REP Roasting** (T1558.004) : cibler les comptes qui n’exigent pas de pré-authentification Kerberos (setting « Do not require Kerberos preauthentication »). Pour ces comptes, un attaquant peut demander directement un AS-REP chiffré avec le hash du compte, et le cracker hors ligne. Défense : éliminer le setting sauf usage documenté.

**Pass-the-Hash** (T1550.002) : s’authentifier avec un hash NTLM sans jamais avoir le mot de passe en clair. Fonctionne pour des services qui acceptent NTLM.

**Pass-the-Ticket** (T1550.003) : réutiliser un ticket Kerberos volé sur une autre machine.

**Overpass-the-Hash** : utiliser un hash NTLM pour demander un ticket Kerberos — permet de passer de NTLM à Kerberos quand seule la deuxième authentification est acceptée.

**Dans le cloud**, l’arsenal évolue : vol de **Primary Refresh Tokens** (Azure AD), **Golden SAML** (forgeage de tokens SAML via compromission d’ADFS — pivot de SolarWinds), vol de cookies de session (**pass-the-cookie** — contourne la MFA en réutilisant des sessions authentifiées), abus d’**applications OAuth** sur-permissives (technique APT29 récurrente).

#### 3.4 Persistence moderne

La persistence moderne va bien au-delà des clés Run/RunOnce classiques.

**DLL Sideloading** (T1574.002) : placer une DLL malveillante dans le même répertoire qu’une application légitime qui la charge par défaut au lancement. L’application légitime exécute la DLL, qui est donc exécutée dans le contexte du processus légitime. Les APT chinoises en font un usage massif — il est difficile à détecter car la DLL n’est pas exécutée directement, elle est chargée par un processus signé et de confiance.

**COM Hijacking** (T1546.015) : détourner une clé de registre COM pour pointer vers un CLSID malveillant, qui sera chargé quand un composant COM légitime est invoqué par une application Windows normale.

**WMI Event Subscription** (T1546.003) : créer un consommateur WMI qui se déclenche sur un événement système (démarrage, connexion utilisateur, à une heure précise). Exécute le code malveillant sans fichier persistant facilement identifiable.

**Scheduled Tasks** (T1053) : tâches planifiées Windows, avec des mécanismes récents de création sans écrire dans le registre visible (Task Scheduler 2.0 COM interfaces).

**Service Creation / Modification** (T1543.003) : créer un service Windows qui exécute le malware à chaque démarrage, ou modifier un service existant. Techniques avancées : modifier le ServiceDll d’un service svchost.exe existant.

**Scheduled Tasks avec déclencheurs inhabituels** : tâches déclenchées à la connexion d’un périphérique USB, à une heure précise, à un événement du journal système.

**Bootkits / Rootkits UEFI** (T1542) : persistence au niveau du firmware. Survit à la réinstallation complète de l’OS. Techniquement complexe mais démontré par Turla (MoonBounce), CosmicStrand (groupe chinois suspecté), LoJax (APT28). Extrêmement difficile à détecter et éliminer — la machine doit être physiquement reflashée.

**Cloud persistence** : création de comptes de service Azure AD avec permissions étendues, enregistrement d’applications OAuth avec consentement administrateur, ajout de comptes aux rôles privilégiés d’Entra ID. Une compromission cloud bien installée peut survivre à la réinstallation complète de tous les endpoints.

#### 3.5 Defense evasion

La defense evasion évolue en symbiose avec les EDR et les mécanismes de détection.

**Obfuscation** (T1027) à plusieurs niveaux : scripts PowerShell en base64 (détecté par beaucoup d’EDR aujourd’hui, donc combiné avec d’autres techniques), obfuscation XOR, chiffrement AES des payloads, strings chiffrées dans les binaires, noms de variables et fonctions randomisés, control-flow flattening.

**Signed Binary Proxy Execution** (T1218) : détourner des binaires Windows signés pour exécuter du code malveillant. Outil de référence : InstallUtil.exe, MSBuild.exe, RegAsm.exe, rundll32.exe, mshta.exe. L’exécution apparaît comme provenant d’un binaire légitime signé par Microsoft, ce qui contourne beaucoup de contrôles.

**Process Injection** (T1055) : injecter du code dans un processus légitime déjà en cours (explorer.exe, svchost.exe, un processus Office). Variantes techniques : classic DLL injection, reflective DLL injection, process hollowing, AtomBombing, Early Bird APC injection, Module Stomping. Chaque nouvelle technique cherche à échapper aux contrôles EDR de la génération précédente.

**EDR Bypass** : désactivation de l’EDR via des privilèges élevés, exploitation de vulnérabilités dans les drivers EDR eux-mêmes (technique « Bring Your Own Vulnerable Driver » — BYOVD, où l’attaquant déploie un driver signé mais vulnérable pour obtenir un contexte kernel et désactiver l’EDR). Cas célèbre : **RTCore64.sys** exploité par plusieurs acteurs, **PROCEXP.SYS** (un driver Sysinternals abusé), **Ryuk** et d’autres groupes ransomware ont utilisé BYOVD systématiquement.

**Timestomping** (T1070.006) : modifier les timestamps des fichiers malveillants pour qu’ils ressemblent à des fichiers système anciens, échappant aux analyses temporelles des investigateurs.

**Log Clearing** (T1070.001) : nettoyage des logs Windows (Security, System, Application, Sysmon). Détectable si les logs sont exfiltrés en temps réel vers un SIEM — d’où l’importance du log forwarding.

**Masquerading** (T1036) : nommer les fichiers malveillants avec des noms de binaires légitimes (svchost.exe placé dans un répertoire non standard, fichier malveillant nommé « Microsoft Update »), ou modifier les métadonnées (champ Description, CompanyName).

**Anti-forensics** : détection de sandbox / VM (l’implant refuse de s’exécuter si l’environnement ressemble à une sandbox analyste), effacement auto après un délai si pas de C2 reçu, mécanismes de kill switch.

#### 3.6 Command and Control moderne

Le C2 moderne a évolué pour rendre la détection réseau beaucoup plus difficile.

**HTTPS comme standard** : la quasi-totalité des C2 APT passent par HTTPS, avec des certificats Let’s Encrypt (gratuits, faciles à obtenir). Le contenu est chiffré, seul le domaine/SNI et les patterns de trafic sont visibles au défenseur sans déchiffrement.

**Catégorisation des domaines** : les attaquants enregistrent des domaines plausibles (lookalike des marques connues, domaines techniques type `cdn-updates-microsoft.net`, domaines dans des TLD peu surveillés). Les domaines récents sont suspects, d’où la mise en **aging** — l’acteur enregistre un domaine, le laisse « vieillir » plusieurs mois sans activité, puis l’active.

**Domain Fronting** (T1090.004) : faire transiter le C2 via un CDN légitime (Fastly, Akamai, Azure CDN, AWS CloudFront), en exploitant le fait que les CDN routent le trafic basé sur le header Host HTTPS après le déchiffrement SNI. L’attaquant voit le trafic partir vers `cdn-legitimate.com`, mais le backend reçoit et répond via le C2 réel. Technique massivement utilisée entre 2015 et 2018 ; largement restreinte depuis par les CDN majeurs qui bloquent le domain fronting.

**Abus de services légitimes** (T1102) : utiliser Slack, Discord, Telegram, GitHub, Pastebin, Google Drive, OneDrive, Dropbox comme canaux C2. Le trafic semble légitime, les domaines sont blanc-listés par défaut. APT29 excelle dans cette technique — leur malware FoggyWeb communiquait via des cookies Exchange bien calibrés. Des implants récents utilisent des canaux Discord pour recevoir leurs commandes.

**DNS Tunneling** (T1071.004) : encoder les données dans les requêtes DNS (particulièrement les requêtes TXT et CNAME). Lent (limité par la taille des enregistrements et le throughput DNS), mais très difficile à bloquer car le DNS doit rester fonctionnel pour le réseau. Souvent utilisé comme canal secondaire en cas de blocage du canal primaire.

**Routeurs SOHO compromis comme relais** : **Volt Typhoon** a construit un botnet de routeurs résidentiels compromis (Cisco RV, Fortinet, NetGear, ASUS). Le trafic C2 des implants transite via ces routeurs — apparaissant depuis des IP résidentielles aux États-Unis ou en Asie, fondant le trafic malveillant dans le trafic domestique. Détection très difficile. Démantèlement partiel par le FBI en janvier 2024, mais le modèle se reproduit. **APT28** a utilisé la même approche avec son botnet **MooBot** démantelé en février 2024.

**Beaconing** : le pattern temporel est caractéristique. Interval de 30 minutes à 24 heures pour les opérations patientes ; quelques secondes pour l’interactif. **Jitter** (variation aléatoire) ajouté pour éviter la détection par analyse de périodicité. La détection statistique du beaconing (RITA, machine learning sur les timeseries de connexions) est une parade efficace — d’où les attaquants expérimentent des patterns moins réguliers (beacon irrégulier, synchronisation avec les horaires de travail pour se fondre).

#### 3.7 OPSEC des attaquants sophistiqués

L’OPSEC distingue l’APT mature de l’amateur.

**Infrastructure compartimentée** : chaque opération a sa propre infrastructure C2, ses propres domaines, ses propres identités fictives. Une compromission découverte sur une cible ne propage pas le risque aux autres opérations. APT29 et Turla sont documentés pour cette pratique.

**Infrastructure renouvelable** : les domaines, IP, certificats sont prévus pour être jetables. Quand une infrastructure est brûlée publiquement, l’opérateur migre vers une infrastructure de remplacement déjà préparée.

**Opérateurs formés** : les APT matures ont des opérateurs entraînés, qui connaissent les techniques récentes, testent leurs actions avant de les déployer, et évitent les erreurs de débutant. Les services étatiques investissent dans la formation continue.

**Séparation des rôles** : développeurs de malware, opérateurs d’intrusion, analystes du renseignement collecté sont des rôles distincts. Le développeur ne sait pas quelle cible utilisera son implant ; l’opérateur ne voit pas le renseignement final. Cette compartimentation limite l’impact d’une trahison ou d’une infiltration.

**Heures de travail** : les opérateurs étatiques travaillent à des heures de bureau du pays sponsor. Les analyses timing ont permis d’identifier des fuseaux horaires : APT29 travaille aux heures de Moscou, les APT chinoises aux heures de Pékin (avec des variations selon les bureaux régionaux MSS), Lazarus aux heures de Pyongyang. Ce signal, seul, n’est pas probant — il peut être manipulé — mais il contribue au faisceau d’attribution.

**Langage et artefacts culturels** : les commentaires dans le code, les noms de variables, les chaînes de debug trahissent parfois la langue maternelle de l’opérateur. Les APT sophistiquées nettoient systématiquement ces artefacts, mais les erreurs arrivent.

#### 3.8 L’ATT&CK framework en pratique

ATT&CK est à la fois un langage commun et une base de connaissance exploitable opérationnellement.

**Lire une matrice ATT&CK** : les colonnes sont les 14 tactiques (objectifs adversaires), les lignes sous chaque colonne sont les techniques et sous-techniques. Une intrusion est « cartographiée » en sélectionnant les techniques effectivement observées.

**Utiliser ATT&CK pour la défense** : mapper les détections existantes (quelles techniques votre SIEM/EDR/NDR détecte déjà, avec quelle fiabilité), identifier les **gaps** (quelles techniques importantes ne sont pas détectées), construire un **détection roadmap** priorisé par fréquence d’usage et impact. Des outils comme **ATT&CK Navigator** permettent la visualisation interactive.

**Prioriser par acteur** : les techniques utilisées par les acteurs pertinents pour votre secteur/géographie sont à prioriser. Si vous êtes un opérateur énergie européen, les TTP de Sandworm, Volt Typhoon, et certains clusters chinois sont plus importantes que les TTP d’APT32 (Vietnam) ou d’un groupe régional ciblant l’Amérique latine. **ATT&CK Groups** liste pour chaque groupe les techniques documentées — point de départ pour une priorisation.

**Ingérer les rapports CTI via ATT&CK** : un bon rapport CTI d’incident référence les TTP observées par leur identifiant ATT&CK. Cela permet de confronter rapidement les TTP au profil connu de groupes, et de construire des détections transférables d’un incident à l’autre.

**Les matrices spécialisées** : ATT&CK ICS (pour l’OT, voir Ch.20-21), ATT&CK Mobile (pour iOS/Android), ATT&CK Cloud (intégré à Enterprise mais avec des techniques spécifiques par plateforme). À chaque environnement sa grammaire.

La maturité CTI d’une organisation se mesure notamment à sa capacité à parler ATT&CK : non seulement connaître les techniques, mais les utiliser pour prioriser défenses, détections, exercices, et communications avec les partenaires.

-----

### Chapitre 4 — Le cyber comme instrument de puissance étatique

#### 4.1 Le modèle DIMEFIL et la place du cyber

Les analystes stratégiques classifient les instruments de puissance étatique selon le modèle **DIMEFIL** : Diplomatic, Information, Military, Economic, Financial, Intelligence, Law Enforcement. Le cyber n’est pas une catégorie à part — il est un **instrument transverse** qui traverse tous les autres.

**Diplomatique** : attribution publique, sanctions ciblées, indictments, négociations de normes internationales (GGE, OEWG), expulsions d’opérateurs diplomatiques.

**Information** : opérations d’influence, hack-and-leak, désinformation coordonnée, contre-narratif, défense de la souveraineté informationnelle.

**Militaire** : opérations cyber offensives en soutien d’opérations conventionnelles (guerre en Ukraine), préparation du champ de bataille cyber, pré-positionnement dans les infrastructures adverses, défense cyber des systèmes militaires.

**Économique** : vol de propriété intellectuelle industrielle (espionnage économique systémique chinois), sabotage de concurrents, perturbation de chaînes d’approvisionnement.

**Financier** : cybervol pour financement étatique (DPRK), blanchiment via crypto, contournement de sanctions.

**Intelligence** : collecte cyber d’origine (SIGINT, CYBINT), pénétration de réseaux gouvernementaux adverses, collecte HUMINT facilitée par le cyber (profilage via OSINT, social engineering).

**Law Enforcement** : coopération internationale contre la cybercriminalité, extraterritorialité, saisies d’infrastructure (démantèlements Emotet, Qakbot, Hydra), exploitation judiciaire du cyber contre des menaces internes.

Chaque État dote son cyber d’une **combinaison spécifique** de ces instruments, qui reflète ses priorités et sa culture stratégique. La Russie intègre massivement le cyber dans l’information et le militaire. La Chine le concentre sur l’économique et le politique. La DPRK sur le financier. Les États-Unis sur l’intelligence, le diplomatique et le law enforcement. Israël sur le militaire et l’intelligence. Comprendre ces profils — ce que fait chaque Partie II à V — oriente l’analyse d’une cyberopération observée.

#### 4.2 Doctrines comparées : vue d’ensemble

Les doctrines cyber divergent entre blocs, et même au sein de blocs. Avant d’entrer dans le détail par pays, une vue d’ensemble fixe les repères.

**Doctrine russe** : la guerre hybride (gibridnaya voyna) intègre le cyber dans un continuum information/cyber/militaire. Pas de séparation nette entre espionnage, influence et sabotage — un même service (le GRU) mène les trois. La sophistication varie selon les services (SVR ultra-furtif, GRU destructif, FSB hétérogène). La tolérance au bruit destructif est la plus élevée de tous les blocs.

**Doctrine chinoise** : le long game. Le cyber sert d’abord l’espionnage économique massif (propriété intellectuelle, rattrapage technologique) et le pré-positionnement stratégique. Pas de destructif massif documenté (à l’exception de la période Unit 61398 avant sa réorganisation post-2014). Sophistication croissante, fragmentation croissante entre services officiels (MSS, PLA) et contractors civils. Long time preference : mois et années d’attente avant d’activer les accès.

**Doctrine nord-coréenne** : le cyber comme arme économique. RGB (Reconnaissance General Bureau) mène espionnage, destruction ponctuelle (rare), et surtout vol massif (crypto, SWIFT). Unique dans son ampleur : c’est le seul État qui finance son régime et son programme d’armement par le cybervol.

**Doctrine iranienne** : rivalité régionale et surveillance interne. Cyber centré sur Israël, Golfe, dissidents. Destructif ponctuel (wipers comme substitut aux opérations conventionnelles). Social engineering très sophistiqué (APT35). Sophistication en croissance, mais en retrait par rapport aux quatre acteurs de pointe (US, Israël, Russie, Chine).

**Doctrine américaine** : defend forward / persistent engagement. Agir en continu dans les réseaux adverses pour dégrader leurs capacités, pas seulement défendre. Cyber intégré au renseignement (NSA), au militaire (USCYBERCOM), et au law enforcement (FBI). Usage massif du droit et de l’attribution publique comme instrument diplomatique.

**Doctrine israélienne** : préemption et supériorité technologique. Cyber comme espace d’action permanent, pas réponse à agression. Intégration militaire-renseignement-privé unique. Exportation des capacités via le marché commercial (NSO, Intellexa, Candiru).

**Doctrine britannique** : disruption coordonnée avec les Five Eyes. Modèle NCSC de protection nationale influent. National Cyber Force (2020) pour les opérations offensives dédiées.

**Doctrine française** : lutte informatique offensive / défensive / d’influence (LIO/LID/L2I), officialisée en 2019. Cadre clair, capacités croissantes, ambition d’autonomie stratégique.

Ces doctrines ne sont pas hermétiques — elles évoluent, elles s’influencent (la doctrine russe de guerre hybride a inspiré certaines réflexions chinoises ; le defend forward américain a influencé le Royaume-Uni et l’Australie). Mais elles fixent des répères durables qui permettent d’interpréter une cyberopération observée.

#### 4.3 Le cyberespace comme 5ème domaine

Depuis le sommet OTAN de Varsovie (2016), le cyberespace est reconnu comme le **5ème domaine d’opérations**, après la terre, la mer, l’air et l’espace. Cette reconnaissance formalise ce qui était déjà une réalité opérationnelle depuis 2007-2010 : le cyber est un espace de confrontation militaire.

Les particularités du cyberespace comme domaine :

**Asymétrie** : un petit État peut infliger des dommages significatifs à un grand. La DPRK, avec un PIB de 30 milliards de dollars, a réalisé des vols crypto dépassant ses exportations légales. L’Iran et la Russie ont infligé des pertes industrielles se chiffrant en milliards à des économies bien plus importantes.

**Déni plausible** : l’attribution est techniquement difficile et politiquement coûteuse. Un État peut mener une opération cyber et nier publiquement pendant des années. Cette caractéristique favorise les opérations dans la zone grise (en dessous du seuil du conflit armé).

**Zone grise** : le cyber permet d’agir en dessous du seuil traditionnel du conflit armé. Des actions qui, dans le monde physique, appelleraient une réponse militaire (sabotage d’une centrale, espionnage d’un état-major) sont courantes dans le cyber avec des réponses politiques/diplomatiques seulement.

**Vitesse** : une action cyber peut se dérouler en minutes ou en heures ; une réponse diplomatique coordonnée prend des mois. Cette asymétrie temporelle favorise l’attaquant.

**Continuum** : les frontières entre espionnage, pré-positionnement, sabotage et guerre sont floues. Un même accès peut servir à l’espionnage aujourd’hui et au sabotage demain. La reconnaissance de Volt Typhoon comme pré-positionnement implique que la Chine est **déjà** en phase de préparation militaire dans les réseaux américains — sans avoir franchi aucun seuil traditionnel.

**Dual-use** : les outils cyber sont massivement dual-use. Un outil légitime de pentest (Cobalt Strike, Metasploit, Empire) est utilisé par des opérateurs autorisés et par des attaquants. Un outil comme BloodHound est utilisé par les red teams défensives et par les APT. Cette caractéristique complique la régulation export et l’attribution.

#### 4.4 Ce que les APT révèlent des intentions étatiques

La lecture géopolitique des campagnes APT est une compétence à part entière. Elle consiste à inférer les priorités stratégiques d’un État à partir des cibles qu’il attaque.

**Victimologie comme signal** : si une APT attribuable à la Chine cible systématiquement des chercheurs en semiconducteurs, on peut inférer la priorité au rattrapage technologique dans ce domaine. Si elle cible la diaspora ouïghoure, on peut inférer la priorité au contrôle politique interne projeté à l’étranger. Si APT35 (Iran) cible des chercheurs spécialisés sur le nucléaire iranien, on peut inférer la priorité à la contre-surveillance du programme national.

**Timing comme signal** : les campagnes cyber suivent souvent les évolutions politiques et militaires. Le ciblage intensifié de l’Ukraine par les groupes russes post-2022, les campagnes iraniennes post-assassinat Soleimani (2020), le ciblage chinois des think tanks Taïwan lors des élections présidentielles sont des signaux doctrinaires lisibles.

**Escalation comme signal** : le passage de l’espionnage au destructif marque une escalade. Le passage du destructif ciblé au destructif mass-market (NotPetya) marque un seuil. Le pré-positionnement massif dans les infras critiques étrangères (Volt Typhoon) marque une préparation stratégique.

**Silence comme signal** : l’absence prolongée d’activité d’un groupe très actif peut signaler une réorganisation interne, un changement de mandat, ou la préparation d’une opération majeure à venir. APT10 a eu des périodes silencieuses corrélées à des réorganisations du MSS chinois.

Pour l’analyste APT, ces signaux doivent être lus prudemment. Les biais de confirmation, les fausses corrélations, et la manipulation délibérée (false flags) peuvent tromper. La règle : une hypothèse géopolitique doit être étayée par plusieurs signaux indépendants et confrontée à des hypothèses alternatives (ACH — voir Ch.24).

#### 4.5 Fil rouge — BLACKOUT Épisode 2

> **⚡ BLACKOUT — Épisode 2 : pourquoi un opérateur énergie ?**
> 
> Le CERT élargit le cadrage de l’analyse. La question « qui attaque ? » ne peut pas être répondue sans d’abord répondre à « pourquoi cette cible ? »
> 
> **Profil de la victime** : opérateur de distribution d’énergie européen, 4 pays (France, Belgique, Allemagne, Pays-Bas), classement OIV en France (arrêté sectoriel énergie), entité essentielle NIS 2. Infrastructure de supervision SCADA reliée à plusieurs dizaines de postes de transformation haute tension. Pas de position publique politique marquée ; pas de contentieux notable avec des acteurs étatiques ; pas de rôle spécifique dans le soutien à l’Ukraine (au-delà de la solidarité européenne générale).
> 
> **Secteur d’activité** : l’énergie est un secteur **stratégique structurel**. Les cibles énergie sont attaquées par :
> 
> - **La Russie (Sandworm)** : doctrine de guerre hybride, ciblage énergie documenté depuis 2015 en Ukraine, extension à l’Europe dans le contexte du conflit ukrainien. Objectif : démonstration de capacité, pré-positionnement pour sabotage en cas d’escalade.
> - **La Chine (Volt Typhoon et clusters similaires)** : doctrine de pré-positionnement stratégique, ciblage énergie documenté aux US et dans le Pacifique (Guam), extension possible à l’Europe dans le contexte Taïwan. Objectif : capacité de dissuasion / représailles.
> - **L’Iran (groupes IRGC)** : ciblage énergie dans le contexte régional, moins présent en Europe. Objectif : démonstration de portée régionale, parfois représailles pour sanctions.
> - **Les cybercriminels** : énergie = cible à fort ROI pour ransomware (Colonial Pipeline 2021 a démontré que les opérateurs paient vite). Mais ici, pas de ransomware — élimine cette hypothèse.
> - **Les hacktivistes** : possible si le contexte politique le justifie. Ici, pas de signal hacktiviste évident — élimine cette hypothèse (pour l’instant).
> 
> **Diagnostic intermédiaire** : le profil cible + l’absence d’intention monétaire + la patience opérationnelle + le positionnement OT orientent vers **une APT étatique en phase de pré-positionnement**. Les candidats principaux sont **Sandworm (Russie)** et **Volt Typhoon ou cluster chinois similaire**. L’Iran est moins probable pour des raisons géographiques et doctrinaires. Les autres acteurs étatiques sont possibles mais improbables a priori.
> 
> Le CERT verrouille ce cadrage dans son journal d’investigation et passe au profilage détaillé des TTP, pour les confronter aux profils connus des candidats (Parties II à V du cours).

-----
