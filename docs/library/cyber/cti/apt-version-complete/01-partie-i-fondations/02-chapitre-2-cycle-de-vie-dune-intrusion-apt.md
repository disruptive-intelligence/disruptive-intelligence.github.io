---
title: Chapitre 2 — Cycle de vie d’une intrusion APT
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
up:
- - APT — version complète
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 2.1 Modèles de cycle : Kill Chain, Unified Kill Chain, ATT&CK

Plusieurs modèles structurent l’analyse d’une intrusion APT de bout en bout. Ils ne se contredisent pas ; ils offrent des vues complémentaires.

La **Cyber Kill Chain** (Lockheed Martin, 2011) propose sept phases linéaires : Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command & Control, Actions on Objectives. Simple, pédagogique, elle reste la référence conceptuelle d’entrée de gamme. Sa limite : elle suggère une progression linéaire, alors qu’une APT réelle fait des allers-retours (nouvelle reconnaissance interne après chaque étape, re-compromission si éjectée).

La **Unified Kill Chain** (Paul Pols, 2017) enrichit le modèle avec 18 phases couvrant aussi le mouvement latéral, la reconnaissance interne, les pivots vers de nouveaux réseaux, et la persistence multi-couches. Plus complète pour les intrusions sophistiquées, elle est moins pédagogique pour l’introduction mais plus fidèle à la réalité des APT.

**MITRE ATT&CK** (2013, enrichi continuellement) est le framework dominant aujourd’hui. Il organise les TTP en **14 tactiques** (Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact, et — plus récentes — Reconnaissance et Resource Development). Chaque tactique contient de nombreuses **techniques** (200+ au total) et **sous-techniques** (400+). Pour chaque technique, ATT&CK documente les groupes qui l’utilisent, les malwares connus, les mitigations, et les détections. C’est à la fois un langage commun et une base de données. Dans la suite du cours, toutes les TTP sont référencées par leur identifiant ATT&CK (Txxxx).

ATT&CK couvre plusieurs matrices : **Enterprise** (Windows, Linux, macOS, cloud, containers — la plus complète), **Mobile** (iOS, Android), et **ICS** (systèmes industriels, voir Partie VI). Les matrices se complètent pour couvrir les attaques multi-environnements.

La suite du chapitre parcourt le cycle ATT&CK en l’enrichissant des spécificités APT.

## 2.2 Reconnaissance et Resource Development

La **reconnaissance** (TA0043) est la phase où l’attaquant collecte de l’information sur la cible avant tout contact. Pour une APT étatique, cette phase dure des semaines à des mois et mobilise des sources variées : OSINT (LinkedIn pour identifier les employés et leur rôle, sites d’entreprise, conférences, presse), scan technique (Shodan, Censys pour l’infrastructure exposée), breach databases (credentials potentiellement réutilisables), et parfois HUMINT ou SIGINT quand l’acteur dispose de ces capacités.

Les APT les plus sophistiquées investissent lourdement dans la reconnaissance. APT29 est documenté pour avoir passé des mois à identifier les administrateurs SolarWinds avant la compromission initiale. APT35 (Iran) construit des profils d’ingénierie sociale extrêmement détaillés sur ses cibles (chercheurs, journalistes, dissidents) — jusqu’à des faux profils LinkedIn de « collègues » qui interagissent pendant des mois avant d’aborder l’objectif réel.

Le **Resource Development** (TA0042) est la phase où l’attaquant prépare son infrastructure et ses outils : acquisition de domaines (via des registrars permissifs, avec des identités fictives), mise en place des serveurs C2 (VPS chez des hébergeurs peu coopératifs, ou abus de services cloud légitimes), développement ou acquisition du malware, préparation des comptes d’opération (faux profils LinkedIn, faux comptes email pour le spear-phishing). Pour les APT matures, cette infrastructure est **compartimentée** : chaque opération a sa propre infrastructure, ce qui limite le risque de propagation d’une découverte.

## 2.3 Accès initial : les vecteurs dominants 2024-2026

L’**Initial Access** (TA0001) est la phase où l’attaquant obtient son premier foothold. Cinq vecteurs dominent aujourd’hui.

**Phishing** (T1566) reste le vecteur statistiquement le plus fréquent. Le spear-phishing APT est très différent du phishing de masse : message personnalisé (fonction, projet en cours, relations), pretexte crédible (invitation à une conférence, message d’un faux collègue, notification d’un service légitime), leurre adapté (document Word avec macro, PDF avec exploit, lien vers un faux portail OAuth). APT29 a excellé dans le **phishing OAuth** — messages imitant des invitations Microsoft Teams ou des demandes d’autorisation d’application, qui, si acceptés, donnent à l’attaquant un accès persistant au compte sans avoir à voler de mot de passe.

**Exploitation d’appliances edge** (T1190) est devenue le vecteur n°1 des APT les plus sophistiquées depuis 2022-2023. Les VPN, firewalls, passerelles web et autres équipements exposés sur Internet sont des cibles privilégiées : ils ne supportent souvent pas d’EDR, leurs vulnérabilités sont exploitables massivement dès publication, et ils donnent un accès privilégié au réseau interne. Les vagues **Ivanti Connect Secure** (CVE-2023-46805, CVE-2024-21887, CVE-2024-21888 en 2024), **Fortinet FortiOS** (multiples CVE 2022-2024), **Citrix ADC / NetScaler** (CVE-2023-4966 — Citrix Bleed), **Barracuda Email Security Gateway** (CVE-2023-2868 exploité par UNC4841/Chine pendant 8 mois), **Palo Alto GlobalProtect** (CVE-2024-3400) ont toutes été exploitées en vagues massives par des acteurs étatiques dans les heures ou jours suivant la publication.

**Supply chain compromise** (T1195) est la catégorie la plus sophistiquée. Elle a plusieurs variantes : compromission d’un éditeur logiciel pour injecter une backdoor dans son produit (SolarWinds / SUNBURST par APT29 — Ch.29 ; 3CX par Lazarus en 2023), compromission d’un MSP pour atteindre ses clients (Opération Cloud Hopper — APT10 sur des MSP internationaux), compromission de dépôts de code (attaques sur des dépendances npm, PyPI), compromission du pipeline de build (modification de binaires signés).

**Credential abuse** (T1078) exploite des credentials volés ou réutilisés. Les sources : breaches publiques (un employé utilise le même mot de passe sur un site compromis et sur son compte professionnel), **infostealers** (Lumma, RedLine, Vidar — qui volent les credentials stockés dans les navigateurs), password spray (essais automatisés de mots de passe faibles sur des comptes M365/Azure AD), **AitM** (Adversary-in-the-Middle phishing, avec outils comme Evilginx, qui capture aussi les cookies de session — permettant de contourner la MFA).

**Exploitation de vulnérabilités publiques** (T1190 aussi) sur des services web exposés (Exchange, OWA, SharePoint, logiciels métier exposés) reste un vecteur massif. Les vagues Exchange **ProxyLogon** (CVE-2021-26855, exploitée massivement par Hafnium / Chine en 2021) et **ProxyShell** (2021) ont compromis des dizaines de milliers d’organisations mondialement.

Le choix du vecteur dépend du niveau de sophistication de l’acteur, de sa patience, et du profil de la cible. Une APT sophistiquée contre une cible de haute valeur privilégiera supply chain ou exploit 0-day. Une APT opportuniste contre des cibles multiples privilégiera l’exploitation massive d’edge devices non patchés.

## 2.4 Execution, persistence, privilege escalation

Une fois le foothold obtenu, l’attaquant doit **exécuter** son code sur la machine compromise, **persister** à travers les redémarrages et les éjections, et **escalader ses privilèges** pour accéder à plus de ressources.

L’**Execution** (TA0002) se fait via des méthodes qui varient en discrétion. Les plus sophistiquées privilégient la **Living off the Land** : exécuter du code via des outils légitimes du système plutôt qu’en déposant un binaire dédié. PowerShell (T1059.001), wmic (T1047), rundll32 (T1218.011), regsvr32 (T1218.010), mshta (T1218.005), cmd.exe avec des techniques d’obfuscation, Python/Perl interpréteurs sont les LOLBins (Living Off the Land Binaries) de référence. L’exécution sans dépôt sur disque (fileless) via PowerShell en mémoire ou via WMI event consumers est le standard APT moderne.

La **Persistence** (TA0003) doit survivre aux redémarrages et aux tentatives d’éradication. Les mécanismes courants incluent les **tâches planifiées** (T1053, Windows Task Scheduler ou Linux cron), les **services Windows** (T1543.003), les **clés de registre Run/RunOnce** (T1547.001), le **DLL sideloading** (T1574.002 — placer une DLL malveillante dans le répertoire d’une application légitime qui la charge au démarrage ; très utilisée par les APT chinoises), le **COM hijacking** (T1546.015), le **WMI event subscription** (T1546.003 — déclenchement à chaque événement système), et les **bootkits** (T1542 — persistence au niveau UEFI/BIOS, techniquement complexe mais ultra-résiliente).

Les APT les plus sophistiquées déploient de la **persistence multi-couches** : plusieurs mécanismes indépendants, sur des systèmes différents, pour garantir qu’un nettoyage partiel laisse un point de réinfection. APT29 est documenté pour avoir maintenu quatre mécanismes de persistence simultanés sur certaines compromissions importantes.

La **Privilege Escalation** (TA0004) vise à passer d’un compte limité à un compte administrateur local, puis à un compte de domaine, puis à des credentials de service ou à des comptes hautement privilégiés. Les techniques classiques : exploitation de vulnérabilités locales (Windows local privilege escalation — CVE récentes kernel, print spooler), abus de mauvaises configurations (AlwaysInstallElevated, services mal configurés avec permissions faibles), vol de tokens (T1134), DLL search order hijacking (T1574.001). Les privilèges obtenus conditionnent la suite : sans privilèges admin, l’attaquant est limité ; avec des privilèges de domaine, il peut aller quasiment partout.

## 2.5 Defense evasion et credential access

La **Defense Evasion** (TA0005) est le théâtre principal de l’évolution du tradecraft APT. Les techniques se multiplient avec le renforcement des défenses.

**Obfuscation** (T1027) : brouiller le code pour échapper à la détection signature-based. Scripts PowerShell en base64, binaires packés, strings chiffrées, noms de fonctions randomisés. **Signed binary proxy execution** (T1218) : détourner des binaires Windows signés légitimes (rundll32, regsvr32, mshta, installutil, msiexec) pour exécuter du code malveillant — l’exécution apparaît comme provenant d’un binaire de confiance. **Process injection** (T1055) : injecter du code dans le processus d’une application légitime (explorer.exe, svchost.exe) — le malware n’a pas de processus visible distinct. **Timestomping** (T1070.006) : modifier les timestamps des fichiers pour échapper aux analyses temporelles. **Indicator removal** (T1070) : nettoyage des logs, suppression des traces, désactivation de la télémétrie EDR.

La **Credential Access** (TA0006) est une phase critique car elle conditionne le mouvement latéral. Les outils de référence sont bien connus mais évoluent constamment pour échapper aux EDR.

**Mimikatz** reste l’outil emblématique — extraction de credentials depuis la mémoire LSASS. **DCSync** (T1003.006) : simule un contrôleur de domaine pour récupérer les hashs de tous les comptes AD — devient possible dès qu’on dispose d’un compte avec les bons droits (Domain Admin, ou droits de réplication accordés). **Kerberoasting** (T1558.003) : demander des tickets Kerberos pour des comptes de service avec SPN, puis cracker les hashs hors ligne. **AS-REP Roasting** (T1558.004) : cibler les comptes qui ne nécessitent pas de pré-authentification Kerberos. **Credential dumping** de LSASS (T1003.001) directement via procdump, comsvcs.dll, ou des techniques récentes anti-EDR (NanoDump, SafetyKatz). **Cloud credential access** : vol de tokens SAML (GoldenSAML — forgeage de tokens SAML via la compromission d’ADFS, technique pivot de SolarWinds), abus d’Azure AD (vol de Primary Refresh Tokens, pass-the-cookie, abus d’applications OAuth sur-permissives).

La sophistication de la phase credential access distingue les APT modernes. Les acteurs de pointe (APT29, Sandworm) combinent plusieurs techniques en chaîne, testent les détections, et adaptent leur approche si l’EDR alerte.

## 2.6 Discovery et lateral movement

Le **Discovery** (TA0007) est la reconnaissance interne au réseau de la victime. L’attaquant cartographie : comptes (net user, net group, AD enumeration via BloodHound / SharpHound), systèmes (net view, DNS enumeration), partages (net share), groupes privilégiés, trusts de domaine, chemins vers les cibles de valeur. **BloodHound** (outil open source, aussi utilisé par les red teamers légitimes) est devenu central : il modélise l’AD en graphe et révèle les chemins d’escalade les plus courts. Les APT sophistiquées l’utilisent couramment.

Le **Lateral Movement** (TA0008) déplace l’attaquant de la machine de foothold vers les cibles de valeur. Plusieurs techniques standards.

**Remote Services** (T1021) : RDP (T1021.001 — le plus courant), SMB/Admin Shares (T1021.002 — `\\target\C$`), WinRM, SSH. Utilisent des credentials légitimes obtenus en phase Credential Access. **PsExec** et **WMI remoting** exécutent des commandes à distance sur des machines du domaine. **Pass-the-Hash** (T1550.002) : authentification avec un hash NTLM sans avoir le mot de passe en clair. **Pass-the-Ticket** (T1550.003) : réutilisation d’un ticket Kerberos volé. **Overpass-the-Hash** : utiliser un hash NTLM pour obtenir un ticket Kerberos (contourne certaines limitations).

Les mouvements latéraux modernes sont **orientés identité** : plutôt que de pivoter machine-à-machine avec des credentials locaux, les attaquants compromettent des comptes de domaine privilégiés et utilisent leurs droits pour accéder aux ressources cibles. La compromission de comptes administrateurs de domaine ou de comptes de service permet un mouvement quasi illimité — d’où l’importance de la segmentation des comptes privilégiés (tiering AD).

Dans le cloud, le mouvement latéral prend des formes différentes : pivoter entre tenants M365 en abusant de relations de partage, se déplacer entre abonnements Azure, exploiter des relations de confiance fédérées SAML.

## 2.7 Collection, Command and Control, Exfiltration

La **Collection** (TA0009) rassemble les données d’intérêt. Pour une APT d’espionnage, ce sont des documents (Office, PDF), des emails (Exchange, O365), des bases de données, des dumps d’AD, des artefacts de messagerie, des fichiers de code source. Les données sont stagées localement (T1074) — rassemblées dans un répertoire de collecte avant l’exfiltration — et souvent compressées et chiffrées pour faciliter le transfert.

Le **Command and Control** (TA0011) est le canal par lequel l’attaquant contrôle ses implants et reçoit les données. Les C2 modernes ont évolué massivement depuis les années 2010.

**HTTPS mimicry** (T1071.001) : C2 transitant par HTTPS vers des domaines qui imitent des services légitimes (cdn-microsoft-updates.com, office365-patches.net). Catégorisation automatique des domaines côté défense, d’où l’innovation constante côté attaquant. **Domain fronting** (T1090.004) : faire transiter le C2 via un CDN légitime (Fastly, Akamai, Azure CDN) pour masquer la destination réelle — technique moins efficace aujourd’hui car les CDN ont restreint la pratique. **Abus de services cloud légitimes** (T1102) : utiliser Slack, Discord, Telegram, GitHub, Pastebin, Dropbox comme canaux C2. APT29 est documenté pour abuser de Microsoft OneDrive et Google Drive. **DNS tunneling** (T1071.004) : encoder les communications dans des requêtes DNS — lent mais très difficile à bloquer. **Routeurs SOHO compromis** : Volt Typhoon et APT28 (MooBot campaign) ont construit des botnets de routeurs résidentiels pour faire sortir le trafic C2 depuis des IP résidentielles légitimes — rendant la détection réseau extrêmement difficile.

Le **beaconing** est le pattern caractéristique du C2 APT : l’implant « appelle » à intervalles réguliers (chaque X minutes, avec un jitter pour éviter la détection par périodicité) pour recevoir des ordres. Les intervalles sont longs pour les opérations patientes (30 minutes à 24 heures), courts pour les actions en cours (quelques secondes à quelques minutes). La détection du beaconing repose sur l’analyse statistique des patterns temporels — un domaine consulté à intervalles réguliers est suspect, même si le domaine lui-même n’est pas sur liste noire.

L’**Exfiltration** (TA0010) extrait les données collectées. Elle peut utiliser le même canal que le C2 (T1041 — Exfiltration Over C2), un canal alternatif (T1048 — webshell séparé, upload vers un service cloud), ou des supports physiques si l’accès permet (T1052 — rare en pratique APT).

Les APT sophistiquées maîtrisent l’art du **low and slow** : exfiltration étalée dans le temps, à faible débit, pendant les heures de bureau (pour se fondre dans le trafic légitime), par petits volumes. Exfiltrer 10 Go en continu sur quelques heures est détectable ; exfiltrer 100 Mo chaque jour pendant 3 mois est beaucoup moins.

## 2.8 Impact : espionnage silencieux, destruction, pré-positionnement

La phase **Impact** (TA0040) est l’objectif final. Pour une APT d’espionnage, l’impact est paradoxalement **invisible** : les données ont été collectées et exfiltrées, la cible continue ses activités normales sans le savoir. Pour une APT destructive, l’impact est brutal : wiper qui efface les disques (NotPetya, Shamoon), manipulation OT qui provoque un blackout (Industroyer), chiffrement ransomware déployé par un acteur étatique (Iran contre Albanie 2022 — wiper+ransomware combinés).

Pour une APT de pré-positionnement (Volt Typhoon, Sandworm sur les infras critiques européennes), la phase Impact n’est **pas encore activée**. L’attaquant maintient l’accès et attend un déclencheur (conflit, ordre politique, escalade). Cette configuration — intrusion complète sans impact visible — est la plus difficile à détecter et la plus lourde de conséquences stratégiques. C’est l’enjeu central de la Partie VI.

## 2.9 Spécificités APT dans ce cycle

Comparé à un incident de cybercrime opportuniste, une intrusion APT se caractérise par quelques spécificités transversales au cycle.

**Durée** : l’APT investit dans le temps. Une intrusion ransomware typique passe de l’accès initial à l’impact en quelques jours à quelques semaines. Une intrusion APT d’espionnage dure des mois à des années, avec des phases d’activité et de dormance.

**OPSEC** : l’APT sophistiquée ne fait pas de bruit. Elle limite ses actions aux minimums nécessaires, évite les outils bruyants, efface ses traces, et adapte son comportement à ce qu’elle détecte de la défense.

**Adaptation** : quand l’APT est détectée ou éjectée d’une partie du réseau, elle revient via ses accès redondants, change de TTP, modifie son infrastructure. L’éradication complète nécessite une réponse coordonnée — d’où la règle « scope before contain » (Ch.28).

**Objectif stratégique** : l’APT ne monétise pas. Elle collecte du renseignement, prépare un levier, ou dégrade une capacité adverse. Cela implique que l’analyse ne peut pas s’arrêter à la technique — comprendre l’objectif stratégique est indispensable pour calibrer la réponse (Ch.32 BLACKOUT).

-----
