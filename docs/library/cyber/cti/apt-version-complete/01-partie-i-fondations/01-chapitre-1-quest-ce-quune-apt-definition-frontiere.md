---
title: 'Chapitre 1 — Qu’est-ce qu’une APT : définition, frontières, typologies'
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
up:
- - APT — version complète
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 1.1 Définition opérationnelle : Advanced, Persistent, Threat

Le terme **APT** (Advanced Persistent Threat) désigne un adversaire généralement state-sponsored ou state-aligned qui mène des cyberopérations sophistiquées, durables et ciblées. Chaque mot compte, et chacun corrige une erreur d’interprétation fréquente.

**Advanced** ne signifie pas forcément « zero-day » ou « malware jamais vu ». Beaucoup d’APT réussissent avec des credentials volés, des vulnérabilités connues non patchées, ou du Living off the Land quasi exclusif (Volt Typhoon est l’exemple canonique). Ce qui est « advanced », c’est la combinaison de quatre éléments : **capacité d’adaptation** (l’attaquant change de TTP quand il est détecté), **tradecraft mature** (OPSEC, évasion, persistence multi-couches), **ressources conséquentes** (temps, budget, opérateurs formés, infrastructure renouvelable), et **renseignement préalable** sur la cible (reconnaissance, HUMINT, collection passive en amont).

**Persistent** signifie que l’objectif n’est pas un coup unique. L’adversaire investit dans la persistence — backdoors multiples, accès redondants, mécanismes de réinfection si éjecté. Le **dwell time** (temps écoulé entre la compromission initiale et la détection) se mesure typiquement en semaines à mois. Pour les opérations de pré-positionnement sophistiquées (Volt Typhoon dans les infrastructures US, Sandworm dans les réseaux énergétiques européens), il se mesure en **années**. La moyenne observée par Mandiant dans son rapport M-Trends est passée de 205 jours en 2014 à 10 jours en 2023 — mais cette baisse cache une bimodalité : les compromissions de ransomware sont détectées vite (impact visible), les compromissions APT silencieuses restent longtemps sous le radar.

**Threat** rappelle qu’on parle d’une menace intentionnelle, dirigée par des humains. Des opérateurs prennent des décisions en temps réel, adaptent leur approche aux contre-mesures de la victime, et ont des objectifs stratégiques définis par un commanditaire — un service de renseignement, un état-major militaire, ou un appareil gouvernemental. Cette dimension humaine distingue l’APT d’un malware automatisé ou d’un ransomware opportuniste.

La définition opérationnelle qui en résulte : une APT est un **intrusion set** suivi dans le temps, caractérisé par une victimologie cohérente, des TTP stables ou évoluant lentement, une infrastructure réutilisée, et dont les objectifs s’inscrivent dans l’agenda stratégique d’un État — directement (opérateur interne à un service) ou indirectement (contractor, proxy, hacktiviste instrumentalisé).

## 1.2 APT vs cybercriminalité vs hacktivisme vs insider

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

## 1.3 Typologie d’objectifs APT

Les APT poursuivent cinq grands types d’objectifs, souvent combinés dans une même opération ou une même campagne.

Le **cyberespionnage** est l’objectif le plus courant en volume. Il vise la collecte de données stratégiques : propriété intellectuelle industrielle (semiconducteurs, aéronautique, pharmaceutique), plans militaires, communications diplomatiques, positions de négociation, secrets commerciaux, données personnelles de cibles d’intérêt (dissidents, journalistes, diplomates). L’espionnage cyber remplace ou complète les méthodes traditionnelles (HUMINT, SIGINT). APT29 (Russie/SVR) en est l’archétype sophistiqué ; APT10 (Chine/MSS) en est l’archétype massif.

Le **pré-positionnement** est l’objectif stratégique le plus inquiétant. Il consiste à maintenir un accès dormant dans des infrastructures critiques — énergie, eau, télécoms, transport — pour une activation future en cas de conflit. L’opération ne vise pas l’exfiltration ni le sabotage immédiat ; elle vise à disposer d’un levier. **Volt Typhoon** (Chine, traité au Ch.22 et Ch.31) en est le cas d’école moderne. Sandworm (GRU) a pratiqué le pré-positionnement sur les infrastructures européennes dans le contexte du conflit ukrainien.

Le **sabotage** vise à endommager ou détruire des systèmes. **NotPetya** (Sandworm, 2017) a causé plus de 10 milliards de dollars de dégâts mondiaux ; **Industroyer** (Sandworm, 2016) a provoqué un blackout à Kiev via la manipulation des protocoles industriels ; **Shamoon** (Iran, 2012) a détruit 30 000 postes de Saudi Aramco. Le sabotage cyber produit des effets physiques (blackouts) ou quasi physiques (destruction de capacité opérationnelle d’une organisation pendant des semaines).

L’**influence** et la **désinformation** manipulent l’opinion et déstabilisent politiquement. L’**ingérence électorale** de 2016 aux US (APT28 — DNC hack, puis publication coordonnée via WikiLeaks et DCLeaks) est le cas fondateur. Les campagnes russes contre les élections européennes, la campagne chinoise sur les réseaux sociaux occidentaux, les opérations iraniennes contre les diasporas sont la suite contemporaine. Le hack-and-leak (vol de données + publication orchestrée) est devenu un instrument standard de la guerre cognitive.

Le **financement** est l’objectif le plus caractéristique de la DPRK, mais d’autres acteurs l’emploient ponctuellement. **Lazarus** vole des crypto-actifs pour financer le programme nucléaire et balistique nord-coréen (Ch.30). Certaines opérations iraniennes ont inclus de la fraude financière pour contourner les sanctions. Ce mélange cybercrime/action étatique brouille les catégorisations classiques.

Ces objectifs ne sont pas exclusifs. Une opération APT29 classique combine espionnage (exfiltration de documents) et pré-positionnement (maintien d’accès). Une campagne Sandworm peut combiner espionnage (reconnaissance OT) et sabotage (wiper). L’analyste lit les TTP pour inférer les objectifs — et inversement, connaître les objectifs oriente l’investigation.

## 1.4 Le vocabulaire terrain

Le vocabulaire APT a des nuances que les débutants confondent régulièrement. Les préciser évite des contresens d’analyse.

Un **intrusion set** est un ensemble d’activités malveillantes regroupées par TTP, infrastructure et victimologie communes. C’est ce que les vendors CTI appellent un « groupe APT » (APT29, Sandworm, etc.), mais c’est un **regroupement analytique**, pas forcément une seule équipe physique. L’intrusion set peut correspondre à une unité militaire précise (Sandworm = GRU Unit 74455), à un sous-ensemble d’opérateurs d’un service (APT29 regroupe plusieurs sous-groupes au sein du SVR), ou même à un consortium d’opérateurs partageant des outils (certains clusters chinois).

Un **cluster** est un regroupement préliminaire, pas encore attribué ou pas encore formellement promu au rang de groupe nommé. Mandiant utilise le préfixe **UNC** (Uncategorized) : UNC2452 était le cluster initial avant son identification comme APT29 dans l’affaire SolarWinds. Microsoft utilisait historiquement **DEV** (Developing) avant sa refonte en thèmes météo. Promouvoir un cluster en groupe nommé exige une convergence suffisante de TTP, d’infrastructure et d’objectifs dans le temps.

Une **campaign** (campagne) est une série d’intrusions liées par un objectif commun sur une période donnée. Une campagne peut être conduite par un seul groupe APT (campagne APT29 contre les ministères européens des affaires étrangères en 2023-2024) ou par plusieurs (campagne de ciblage des MSP — Managed Service Providers — impliquant APT10 et APT41 autour de 2016-2018).

Les **TTP** (Tactics, Techniques, Procedures) décrivent le « comment » de l’attaquant. Les **tactiques** sont les objectifs à haut niveau (gagner un foothold, établir la persistence). Les **techniques** sont les méthodes générales (phishing, DLL sideloading). Les **procédures** sont les implémentations spécifiques (utilisation d’un document Word avec une macro VBA spécifique, obfuscation par une méthode particulière). Les TTP sont plus durables que les IoC : un attaquant change facilement un hash de malware, rarement son tradecraft profond.

Le **tradecraft** est le savoir-faire opérationnel global : OPSEC, TTP, habitudes, réflexes, style. Un tradecraft mature est un marqueur d’acteur étatique professionnel. Reconnaître un tradecraft (la façon dont Turla compartimente son infrastructure, la manière dont APT29 abuse des services cloud légitimes) est l’un des exercices les plus sophistiqués de l’analyse CTI.

Les **IoC** (Indicators of Compromise) sont les artefacts techniques ponctuels : hash de fichier, adresse IP, domaine, clé de registre, chaîne de caractères. Les IoC vieillissent très vite (hash changé à chaque nouvelle compilation, IP brûlée dès qu’elle est signalée). Leur valeur tactique est immédiate, leur valeur stratégique est faible — d’où la **Pyramide de la Douleur** (David Bianco) qui hiérarchise les indicateurs par coût pour l’attaquant : les TTP sont tout en haut (coût élevé pour changer), les hashs sont tout en bas (coût nul). Cette pyramide structure toute la défense moderne (voir Ch.3).

## 1.5 Le naming chaos : conventions par vendor

L’un des premiers obstacles de l’apprenant est le **naming chaos** : un même acteur peut avoir 5 à 10 noms différents selon le vendor CTI qui le désigne. Il n’existe pas d’autorité centrale de nommage — chaque éditeur utilise sa propre convention.

**Mandiant** (Google Cloud) utilise historiquement **APTxx** (pour les groupes étatiques attribués : APT28, APT29, APT41), **UNCxxx** (pour les clusters en attente), **FINxx** (pour les groupes financièrement motivés : FIN7, FIN8), et **TEMP.xxx** (préfixe temporaire).

**CrowdStrike** utilise des **animaux par pays** : Bear (Russie — Fancy Bear = APT28, Cozy Bear = APT29), Panda (Chine — Wicked Panda = APT41, Stone Panda = APT10), Chollima (DPRK — Stardust Chollima = APT38, Velvet Chollima = APT43), Kitten (Iran — Charming Kitten = APT35, Fox Kitten), Jackal (hacktivisme), Buffalo (Vietnam — OceanBuffalo = APT32), Crane (Corée du Sud), Spider (cybercrime — Scattered Spider, Wizard Spider).

**Microsoft** a refondu sa convention en 2023 autour de **thèmes météo par origine** : Blizzard (Russie — Midnight Blizzard = APT29, Forest Blizzard = APT28, Seashell Blizzard = Sandworm, Aqua Blizzard = Gamaredon, Secret Blizzard = Turla), Typhoon (Chine — Volt Typhoon, Salt Typhoon, Flax Typhoon, Brass Typhoon = APT41), Sleet (DPRK — Diamond Sleet = Lazarus, Sapphire Sleet = APT38, Emerald Sleet = Kimsuky), Sandstorm (Iran — Peach Sandstorm = APT33, Mint Sandstorm = APT35, Hazel Sandstorm = APT34, Mango Sandstorm = MuddyWater), Storm (cybercrime), Tempest (acteurs privés), Flood (DDoS).

**Kaspersky** utilise des noms variables et créatifs (Turla, Equation Group, BlueNoroff, ProjectSauron) sans convention systématique.

**Secureworks** utilise les **métaux par origine** : Bronze (Chine — Bronze Butler = Tick, Bronze President = Mustang Panda), Cobalt (Russie — Cobalt Mirage = Iran), Gold (cybercrime), Iron (Iran), Tin (DPRK).

**Palo Alto Networks / Unit 42** utilise des noms ciblés par nature (Stately Taurus, Fighting Ursa, Mushroom — plus descriptifs de TTP qu’organisés par pays).

L’**Annexe C** consolide les correspondances. Pour l’opérationnel : quand vous lisez un rapport, notez systématiquement le mapping vers APTxx (Mandiant) ou vers le nom Microsoft — ce sont les conventions les plus largement partagées.

## 1.6 État des lieux quantitatif

Plusieurs centaines de groupes APT sont suivis publiquement par l’écosystème CTI mondial. L’ordre de grandeur :

- **MITRE ATT&CK Groups** répertorie environ 160 groupes documentés publiquement (février 2026).
- **Malpedia** (Fraunhofer FKIE) référence plusieurs centaines de familles de malware attribuées à des acteurs étatiques.
- **CrowdStrike** déclare suivre plus de 230 acteurs (adversaires nommés, 2024 Global Threat Report).
- **Mandiant** suit plus de 300 intrusion sets dans son périmètre interne (dont beaucoup restent en UNC, non promus en APTxx publics).
- **Microsoft Threat Intelligence** publie une liste de plus de 150 threat actors nommés.

Deux implications pour l’analyste. La première : même un expert ne peut pas connaître en profondeur tous les groupes. La discipline consiste à **maîtriser les 30-40 groupes les plus actifs** (couverts par ce cours), puis à savoir **rechercher efficacement** les autres sur Mandiant, Microsoft TI, MITRE ATT&CK, Malpedia. La seconde : le nombre croît chaque année. La prolifération des capacités offensives (Ch.25) produit une fragmentation des acteurs — plus de contractors, plus de clusters éphémères, plus de difficultés d’attribution.

## 1.7 Fil rouge — BLACKOUT Épisode 1

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
