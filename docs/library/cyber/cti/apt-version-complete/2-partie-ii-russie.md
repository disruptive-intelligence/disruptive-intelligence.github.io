---
title: PARTIE II — RUSSIE
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
chapter: 2
chapters: 8
---

> **Ce que cette partie apprend.** Comprendre la doctrine cyber russe (guerre hybride, intégration information/cyber/militaire), connaître la structure de l’appareil cyber russe (SVR, GRU, FSB et leurs unités), identifier les groupes APT russes majeurs et leurs spécificités, analyser les campagnes de référence depuis SolarWinds jusqu’à la guerre en Ukraine.
> 
> **Ce qu’elle ne couvre pas.** Les aspects techniques génériques des TTP (Partie I), le détail technique des campagnes OT spécifiques comme Industroyer (Ch.21), les enjeux d’attribution formels (Ch.24).
> 
> **Ce que vous saurez faire après cette partie.** Reconnaître un tradecraft russe face à une intrusion, différencier un mode opératoire SVR/GRU/FSB, situer une campagne russe dans le cadre doctrinaire de la guerre hybride, et identifier quand le cybercrime russophone est un prolongement plausible d’une opération étatique.

-----

## Chapitre 5 — Russie : contexte, doctrine et appareil cyber

### 5.1 Priorités géopolitiques et principes doctrinaux

Les cyberopérations russes sont compréhensibles à condition de les situer dans les priorités géopolitiques nationales. Quatre priorités structurent l’ensemble : maintien du statut de grande puissance face aux États-Unis et à la Chine, contrôle de l’étranger proche (ex-URSS — Ukraine, Biélorussie, Caucase, Asie centrale), confrontation avec l’OTAN, et préservation du régime interne face aux pressions extérieures perçues et à la dissidence.

Chaque priorité génère des cyberopérations cohérentes. Le maintien de puissance alimente l’espionnage stratégique (SVR contre les gouvernements occidentaux), l’influence électorale (ingérence 2016 aux US, campagnes européennes), et la démonstration de capacité (NotPetya). Le contrôle de l’étranger proche motive le ciblage massif de l’Ukraine (Gamaredon au quotidien, Sandworm en escalade), les opérations contre la Biélorussie et la Géorgie. La confrontation OTAN génère les attaques contre les ministères de la défense, les think tanks stratégiques, les ambassades. La préservation du régime alimente la surveillance des opposants, des journalistes, et la contre-ingérence.

La **doctrine de la guerre hybride** (gibridnaya voyna) est le cadre intégrateur. Formulée par Valery Gerasimov (chef d’état-major des armées russes, essai de 2013 devenu « doctrine Gerasimov » dans la lecture occidentale — lecture que Gerasimov a lui-même contestée), elle postule que les moyens non militaires (information, cyber, économie, pression diplomatique) ont dépassé les moyens militaires dans l’efficacité pour atteindre les objectifs stratégiques. Le cyber est intégré dans ce continuum, aux côtés de la désinformation et des opérations d’influence.

La conséquence opérationnelle majeure : **pas de séparation nette entre espionnage et action**. Un même service (le GRU notamment) mène simultanément de la collecte de renseignement, de la destruction, et de l’influence. Le renseignement collecté est utilisé pour des opérations d’influence (hack-and-leak — DNC 2016), pour du sabotage ciblé, ou pour préparer des opérations conventionnelles. Cette intégration est le trait le plus distinctif de la doctrine russe, comparée à la doctrine américaine où renseignement (NSA), militaire offensif (USCYBERCOM) et law enforcement (FBI) sont plus nettement séparés.

### 5.2 Le SVR : espionnage stratégique furtif

Le **SVR** (Служба внешней разведки — Service de Renseignement Extérieur) est le successeur post-soviétique du premier directorat du KGB. C’est le service russe chargé de l’espionnage stratégique — gouvernements étrangers, diplomatie, think tanks, grandes entreprises technologiques. Son style opérationnel est la **furtivité maximale** et le **long terme**.

Le groupe APT associé au SVR est **APT29** (Mandiant) / **Cozy Bear** (CrowdStrike) / **Midnight Blizzard** (Microsoft, anciennement NOBELIUM). APT29 est considéré comme l’un des trois ou quatre groupes APT les plus sophistiqués au monde. Ses caractéristiques opérationnelles se retrouvent dans chaque campagne : investissement massif en reconnaissance, infrastructure compartimentée (chaque cible a sa propre infrastructure C2), abus maîtrisé des services cloud légitimes, malware custom de haute qualité, et OPSEC quasi sans faute.

Les opérations emblématiques d’APT29 incluent **SolarWinds / SUNBURST** (2020, traité en détail au Ch.29), le **Microsoft corporate breach** de 2023-2024 (password spray sur un tenant test, pivot vers les emails de dirigeants Microsoft), les **campagnes de phishing OAuth** contre les diplomaties européennes (2022-2025), et les **ciblages continus des ministères des affaires étrangères** en Europe et en Amérique du Nord.

La tactique OAuth d’APT29 mérite une mention spécifique car elle illustre la modernité du tradecraft. Plutôt que de voler des mots de passe (détectable, temporaire), APT29 envoie à la cible des demandes d’autorisation OAuth pour des applications qui semblent légitimes (nom calqué sur Microsoft Teams, Outlook for iOS, Azure Active Directory Authenticator). Si la cible accepte, l’application malveillante obtient un jeton de refresh qui permet un accès persistant sans mot de passe, contournant la MFA. La technique est silencieuse, résiste aux rotations de mot de passe, et peut persister des mois.

### 5.3 Le GRU : opérations militaires et destructives

Le **GRU** (Главное разведывательное управление — Direction du Renseignement Militaire, rebaptisé officiellement GU — Главное управление — en 2010 mais l’acronyme GRU reste largement utilisé) est le renseignement militaire. C’est le service le plus agressif et le plus bruyant des services cyber russes. Sa mission couvre le renseignement militaire classique, mais aussi le sabotage, les opérations d’influence, et les actions déstabilisatrices.

Trois unités GRU sont publiquement identifiées comme conduisant des cyberopérations.

**Unit 26165** conduit l’espionnage militaire et politique, avec un fort volet opérations d’influence. Le groupe APT associé est **APT28** (Mandiant) / **Fancy Bear** (CrowdStrike) / **Forest Blizzard** (Microsoft) / **Sofacy** (Kaspersky). APT28 est actif depuis au moins 2007 et a été au cœur de l’ingérence électorale américaine de 2016 (hack du DNC, publication via DCLeaks et WikiLeaks). Ses campagnes incluent également le hack du Bundestag allemand (2015), les attaques contre l’Agence Mondiale Antidopage (WADA, 2016), et l’exploitation massive de la vulnérabilité Outlook CVE-2023-23397 (2023) contre les organisations européennes.

**Unit 74455** conduit les opérations destructives. Le groupe APT associé est **Sandworm** (assignation initiale par iSight Partners devenu Mandiant) / **Seashell Blizzard** (Microsoft) / **BlackEnergy group** (historique) / **Voodoo Bear** (CrowdStrike). Sandworm est le seul groupe APT au monde à avoir causé publiquement documenté des pannes d’électricité par cyberattaque (Ukraine 2015 et 2016, Ch.21). Il est également responsable de **NotPetya** (2017, wiper mondial ~10 Mrd $), d’**Olympic Destroyer** (2018, Jeux Olympiques de Pyeongchang avec false flags Lazarus), et d’une série continue de wipers contre l’Ukraine depuis 2022 (HermeticWiper, CaddyWiper, IsaacWiper, AcidRain contre le satellite Viasat KA-SAT).

**Unit 29155** a été identifiée publiquement en 2024 par un advisory conjoint (US, UK, Estonie, Pologne). C’est une unité du GRU qui conduit des **opérations déstabilisatrices cyber-physiques** au soutien d’opérations clandestines plus larges (sabotages, assassinats, harcèlement). Le malware **WhisperGate** (wiper déployé contre l’Ukraine en janvier 2022, quelques semaines avant l’invasion) est attribué à cette unité — ce qui a nécessité une révision des attributions initiales qui pointaient parfois Sandworm. Unit 29155 a également été liée à des tentatives d’attaques contre des infrastructures européennes (documentées par l’advisory CISA/NSA/FBI de septembre 2024).

La distinction entre ces unités importe pour l’analyste : une opération destructive contre l’Ukraine peut être attribuée à Sandworm (74455), à Unit 29155, ou à une coopération entre les deux. L’attribution à la bonne unité précise le cadre doctrinal et les attentes futures.

### 5.4 Le FSB : sécurité intérieure et étranger proche

Le **FSB** (Федеральная служба безопасности — Service Fédéral de Sécurité) est le successeur principal du KGB pour les missions de sécurité intérieure, de contre-espionnage, et de surveillance des voisins proches. Ses cyberopérations se concentrent sur l’Ukraine, la Biélorussie, le Caucase, et la diaspora russophone à l’étranger.

Deux centres du FSB conduisent des cyberopérations publiquement attribuées.

**Centre 16** est le centre historique de cyber-collecte du FSB, chargé de l’espionnage long terme contre des cibles gouvernementales et diplomatiques de haute valeur. Le groupe APT associé est **Turla** (Kaspersky) / **Snake** (Mandiant) / **Secret Blizzard** (Microsoft) / **Venomous Bear** (CrowdStrike). Turla est considéré comme l’un des groupes techniquement les plus avancés au monde, actif depuis au moins 1996 (ce qui en fait l’un des plus anciens groupes APT encore opérationnels). Son malware signature, **Snake** (également appelé **Uroburos**), est un rootkit multi-plateforme extraordinairement sophistiqué, actif depuis au moins 2003, avec des capacités de persistence kernel sur Windows, Linux, et macOS.

Turla est également connu pour deux signatures opérationnelles remarquables. Premièrement, l’utilisation de **communications C2 par satellite** — détournement de liaisons satellite de FAI commerciaux pour masquer l’origine réelle du C2 (documenté par Kaspersky en 2015). Deuxièmement, la technique unique de **détournement d’infrastructure d’autres groupes APT** — Turla a été observé en train d’utiliser l’infrastructure de groupes iraniens (OilRig) pour mener ses propres opérations, technique appelée « piggybacking » qui complique massivement l’attribution et représente un niveau d’OPSEC exceptionnel.

**Snake a été démantelé par le FBI en mai 2023** dans le cadre de l’**opération Medusa**. Le FBI a développé un outil qui, exploitant des fonctionnalités du malware lui-même, a pu envoyer des commandes aux implants Snake sur les machines infectées pour les rendre inopérants — sans interagir avec les systèmes eux-mêmes au-delà de la neutralisation du malware. Opération remarquable par sa technicité et par sa portée (machines infectées dans plus de 50 pays). Turla a continué ses opérations avec d’autres outils post-Snake.

**Centre 18** conduit le ciblage massif de l’Ukraine avec un volume élevé et une sophistication comparativement moindre. Le groupe APT associé est **Gamaredon** (connu aussi comme **Primitive Bear**, **Shuckworm**, **Aqua Blizzard** chez Microsoft). Gamaredon cible systématiquement les institutions ukrainiennes depuis 2013-2014 (avant l’annexion de la Crimée), avec une intensification massive depuis 2022. Son tradecraft : phishing de masse, macros Office, scripts VBA, persistance agressive (réinfection rapide après éradication), et usage de Telegram comme canal de C2 (technique inhabituelle pour un acteur étatique classique — mais Gamaredon est plus proche d’un « bruit de fond » continu qu’un opérateur furtif). Les Ukrainiens ont surnommé Gamaredon « le cadet russe » — Gamaredon est le marteau là où Turla est le scalpel.

### 5.5 L’écosystème cybercriminel russophone : zone grise

Les groupes cybercriminels russophones (opérateurs ransomware, marchés dark web, services de blanchiment) opèrent sous une **tolérance tacite** de l’État russe tant qu’ils respectent deux règles implicites : ne pas cibler la CEI (Communauté des États Indépendants — Russie, Biélorussie, Kazakhstan, etc.), et coopérer ponctuellement avec les services si sollicités.

Cette tolérance produit une zone grise qui complique l’attribution. Un ransomware qui frappe un opérateur stratégique européen peut être :

- Purement criminel, opportuniste, sans implication étatique directe ;
- Criminel, mais avec un choix de cible orienté par un signal étatique (« frappez ces secteurs, pas ces autres ») ;
- Criminel façade, avec un opérateur étatique qui utilise le ransomware comme couverture pour une opération destructive (NotPetya prétendait être un ransomware — il était en réalité un wiper destructif, avec un écran de rançon pour masquer l’intention).

Les affaires emblématiques qui documentent cette zone grise :

**Conti** (groupe ransomware russophone actif 2019-2022) a été l’un des plus prolifiques de son époque. Le groupe a été fracassé par des fuites internes en 2022 après qu’il se soit publiquement rangé du côté russe dans la guerre ukrainienne — un opérateur ukrainien interne a leaké des téraoctets de communications internes (« ContiLeaks »). Les communications révélaient des échanges évoquant le FSB, des consignes de ciblage alignées sur des priorités étatiques russes, et une structure organisationnelle plus hiérarchique que le profil cybercriminel standard. Après la dissolution publique de Conti, ses opérateurs se sont dispersés vers d’autres marques (BlackBasta, Black Suit, Karakurt).

**REvil / Sodinokibi** (groupe ransomware russophone actif 2019-2021) a conduit des opérations de grande ampleur (Kaseya MSP 2021, JBS 2021). Le groupe a été démantelé par les autorités russes en janvier 2022 (arrestation de 14 personnes) — dans un contexte de relation diplomatique Russie-US alors tendue mais pas rompue. Après l’invasion de l’Ukraine en février 2022, la coopération russe a cessé, et REvil s’est reconstitué partiellement.

**LockBit** (actif 2019-2024) a été l’un des plus prolifiques opérateurs RaaS jusqu’à son démantèlement partiel par l’opération Cronos (février 2024, coordination NCA/FBI/Europol). LockBit a montré une discipline anti-CIS claire (geoblocking, désactivation sur systèmes russophones) — marqueur typique de l’écosystème.

**BlackBasta**, **ALPHV/BlackCat**, **Play**, **Royal** : écosystème ransomware contemporain, majoritairement russophone, avec les mêmes patterns de tolérance étatique.

Pour l’analyste : un ransomware russophone frappant un secteur stratégique européen dans un contexte géopolitique tendu n’est jamais purement « criminel ». Le niveau d’implication étatique est un spectre à évaluer selon le contexte.

### 5.6 Hacktivisme instrumentalisé

À côté du cybercrime toléré, la Russie soutient ou instrumentalise plusieurs collectifs présentés comme « hacktivistes ».

**KillNet** (actif depuis 2022) revendique des cyberattaques pro-russes, principalement DDoS contre des institutions occidentales et des infrastructures ukrainiennes. La sophistication technique est modeste (essentiellement DDoS, parfois défacement), mais la coordination opérationnelle et la pérennité suggèrent un soutien ou une connivence minimale avec les services. Le groupe a muté plusieurs fois (KillNet, KillMilk, BlackSkills) et génère un volume continu d’activité pro-régime.

**NoName057(16)** (actif depuis 2022) est plus technique que KillNet. Le groupe déploie un outil DDoS distribué (**DDosia Project**) qui recrute des volontaires via Telegram et les paie en cryptomonnaies pour participer à des attaques. L’outil télécharge régulièrement des listes de cibles depuis des serveurs centralisés. Démantèlement partiel par Europol en mai 2025 — mais le modèle se reproduit.

**IT Army of Ukraine** est symétrique côté ukrainien : mouvement de volontaires cyber internationaux, lancé publiquement par le vice-premier ministre Mykhailo Fedorov via Telegram en février 2022, conduisant des opérations DDoS et de hacktivisme contre des cibles russes. Zone grise similaire : coordination étatique explicite d’un mouvement de volontaires.

Ces mouvements brouillent la distinction classique « hacktivisme vs État ». Pour l’analyste, la règle est de lire les alignements : KillNet et NoName057(16) s’alignent systématiquement sur les priorités tactiques russes (cibles sélectionnées selon l’actualité diplomatique), ce qui est incompatible avec un hacktivisme authentique.

### 5.7 Réorganisations post-2022

L’invasion de l’Ukraine en février 2022 a eu des effets sur l’appareil cyber russe qu’il est utile de documenter.

**Augmentation massive du volume opérationnel** : intensification des attaques contre l’Ukraine (wipers multiples, Gamaredon en continu, Sandworm en escalade), augmentation du ciblage des alliés de l’Ukraine (Pologne, États baltes, OTAN en général), expansion du pré-positionnement dans les infrastructures européennes.

**Professionnalisation de Unit 29155** : la publication de l’advisory de septembre 2024 a documenté l’existence et les capacités d’une unité jusque-là peu connue. Ce qui suggère que les services étatiques russes ont réalloué des ressources pour intensifier leurs opérations.

**Pression sur le cybercrime russophone** : les sanctions occidentales ont rendu plus difficile le blanchiment et la conversion des gains ransomware. Plusieurs groupes ransomware ont déplacé leurs opérations vers les cibles occidentales avec une intensité accrue. Inversement, certains opérateurs ont été observés quittant la Russie pour des juridictions plus neutres (Dubaï, Serbie), signe d’une fragilisation de l’écosystème.

**Durcissement de l’OPSEC** : post-invasion, plusieurs groupes russes ont adapté leur tradecraft. APT29 a intensifié ses campagnes OAuth et l’abus de services cloud légitimes. Sandworm a diversifié son malware (CosmicEnergy découvert 2023, variants HermeticWiper, AcidRain contre Viasat).

L’écosystème russe en 2025-2026 reste le plus actif au monde en volume d’opérations destructives documentées, avec une pression réciproque entre les services (qui doivent démontrer leur valeur opérationnelle) et les défenseurs occidentaux qui ont gagné en maturité d’attribution et de détection.

### 5.8 Fil rouge — BLACKOUT Épisode 3

> **⚡ BLACKOUT — Épisode 3 : le profil TTP observé est-il compatible Sandworm ?**
> 
> Le CERT, après la phase de triage initial, collecte les TTP observées et les confronte au profil connu de Sandworm.
> 
> **TTP observées sur BLACKOUT** :
> 
> 1. Accès initial via exploitation d’appliance Ivanti (CVE-2024-21887).
> 1. Persistence via DLL sideloading dans une application de supervision.
> 1. Mouvement latéral via PsExec et Kerberoasting (credentials de compte de service avec SPN faible).
> 1. Pivot vers OT via un poste d’ingénierie double-connecté.
> 1. C2 par beaconing HTTPS avec jitter (27 min ± 3 min).
> 1. Pas de malware custom identifié à ce stade.
> 1. Aucune action destructive ou exfiltration visible.
> 
> **Profil Sandworm typique** (profil de référence basé sur les campagnes documentées 2015-2025) :
> 
> - Accès initial : mix supply chain, exploitation edge, phishing ciblé — l’exploitation Ivanti est plausible.
> - Persistence : services Windows, tâches planifiées, parfois DLL sideloading — compatible.
> - Mouvement latéral : PsExec, WMI, Mimikatz, Kerberoasting — compatible.
> - Ciblage OT : signature historique de Sandworm — très compatible.
> - C2 : HTTPS avec beaconing — compatible, mais les patterns spécifiques de Sandworm (jitter, intervalles) varient selon les campagnes.
> - Malware custom : **Sandworm utilise typiquement du malware custom** (Industroyer, CaddyWiper, HermeticWiper, wipers, backdoors). L’absence de malware custom est un **léger décalage** avec le profil Sandworm classique.
> - Action destructive : signature Sandworm, mais absent ici (ce qui serait compatible avec une phase de pré-positionnement préalable à l’activation).
> 
> **Cohérences fortes** : ciblage énergie, pivot OT, patience opérationnelle, contexte géopolitique (conflit ukrainien en cours, tensions énergétiques).
> 
> **Décalages notables** : pas de malware custom Sandworm identifié, exploitation Ivanti (attaquée aussi par d’autres acteurs notamment chinois), C2 relativement standard.
> 
> **Diagnostic intermédiaire CERT** : profil **compatible avec Sandworm** mais **pas exclusivement**. Il est indispensable de tester d’autres hypothèses — notamment les acteurs chinois, qui ont des profils de pré-positionnement énergie (Volt Typhoon) compatibles avec certaines observations.
> 
> Le CERT passe à l’examen du profil chinois (Partie III).

-----

## Chapitre 6 — Russie : les groupes APT en détail

Ce chapitre approfondit le profil des six groupes APT russes les plus importants. Chaque profil couvre : mission, TTP signature, OPSEC, campagnes emblématiques, évolution récente.

### 6.1 APT29 / Cozy Bear / Midnight Blizzard (SVR)

**Mission** : espionnage stratégique de haut niveau — gouvernements occidentaux, diplomatie, grandes entreprises technologiques, think tanks, ONG actives sur la Russie, recherche médicale (ciblage documenté sur les développeurs de vaccins COVID en 2020).

**TTP signature** :

- **Accès initial par compromission supply chain** (SolarWinds 2020 — cas d’école), par **phishing OAuth ciblé** (demandes d’autorisation d’applications malveillantes imitant Microsoft Teams ou des applications Azure légitimes), par **password spray** sur Azure AD (tenants avec faibles politiques), et occasionnellement par **spear-phishing classique** avec macros.
- **Abus Azure AD / Entra ID / M365** : vol de tokens SAML (GoldenSAML), manipulation d’applications OAuth, pivotement entre tenants via des relations de partage, abus de permissions Graph API pour lire les emails.
- **Malware custom sophistiqué** : SUNBURST (backdoor injectée dans les builds Orion de SolarWinds), TEARDROP (loader), GoldMax / SUNSHUTTLE (backdoor Go cross-platform), GoldFinder (HTTP tracer pour reconnaissance d’infrastructure), SIBOT (VBScript), FoggyWeb (backdoor ADFS post-exploitation), MagicWeb (malware ADFS plus récent 2022).
- **C2 via services légitimes** : Azure, AWS, Dropbox, Twitter (pour des canaux secondaires), abus de canaux Slack/Teams dans certaines campagnes récentes.
- **Minimal footprint** : peu de fichiers déposés, exécution en mémoire privilégiée, nettoyage systématique des traces.

**OPSEC** : parmi la plus élevée du monde APT. Infrastructure compartimentée (chaque cible a sa propre chaîne d’infrastructure C2), opérateurs disciplinés (pas d’erreurs d’horaires documentées), adaptation rapide aux mitigations (changement de techniques dès qu’une campagne est publiée).

**Campagnes majeures** :

- **SolarWinds / SUNBURST** (2020-2021) : ~18 000 organisations infectées via la mise à jour trojanisée d’Orion, ~100 cibles de haute valeur activement exploitées (Trésor US, Département du Commerce, Département de la Sécurité Intérieure, Microsoft, FireEye/Mandiant, et autres). Détaillé au Ch.29.
- **Ciblage des développeurs de vaccins COVID** (2020) : attribué par NCSC, NSA, CSE/Canada — APT29 cible les entreprises pharmaceutiques britanniques, américaines et canadiennes développant les vaccins COVID-19 pour exfiltrer la recherche.
- **Microsoft corporate breach** (novembre 2023 - janvier 2024) : APT29 compromet un tenant Azure AD test de Microsoft via password spray, pivote vers une application OAuth permissive, et accède aux emails de dirigeants Microsoft (y compris de la direction exécutive). Microsoft a publiquement reconnu la compromission. Des entités tierces (Hewlett Packard Enterprise notamment) ont subséquemment confirmé des compromissions liées.
- **Campagnes diplomatiques continues 2022-2025** : spear-phishing OAuth contre les ministères des affaires étrangères européens, les ambassades, les missions diplomatiques. Volume élevé, taux de compromission non-public.
- **MagicWeb** (2022) : backdoor ADFS post-exploitation identifiée par Microsoft. Le malware modifie la gestion des certificats ADFS pour permettre à l’attaquant de se faire passer pour n’importe quel utilisateur.

**Évolution récente (2024-2026)** : après SolarWinds, APT29 a évolué vers un usage encore plus prononcé des abus cloud/identity (tokens, OAuth, Primary Refresh Tokens Azure AD). La dépendance aux infrastructures cloud légitimes (Microsoft, AWS, Google) rend la détection plus difficile. Les campagnes de 2024-2025 montrent un ciblage encore plus sophistiqué des ministères européens, avec des emails personnalisés qui passent les filtres anti-phishing majoritairement par leur contexte plausible.

### 6.2 APT28 / Fancy Bear / Forest Blizzard (GRU Unit 26165)

**Mission** : espionnage militaire et politique + opérations d’influence intégrées. Cibles : ministères de la défense, organisations internationales (OTAN, UE, OSCE), organisations anti-dopage (WADA), partis politiques (DNC 2016), médias, think tanks de défense.

**TTP signature** :

- **Spear-phishing** : macros VBA dans des documents Office (pendant longtemps la technique privilégiée), faux portails de login OAuth ou de services corporate (Microsoft OWA, VPN).
- **Exploitation de vulnérabilités** : APT28 est l’un des acteurs les plus actifs à exploiter rapidement les vulnérabilités Outlook et Exchange. **CVE-2023-23397** (Outlook, vulnérabilité NTLM hash leak via invitation de calendrier malveillante) a été massivement exploitée par APT28 en 2022-2023 avant sa découverte publique.
- **Credential harvesting** : fausses pages de login imitant les services corporate, password spraying massif sur Azure AD.
- **Outils custom** : **X-Tunnel** (proxy interne), **XAgent** (backdoor modulaire Windows/macOS/iOS/Android), **Zebrocy** (backdoor multi-langages — Delphi, Go, Python, C++ — tradecraft inhabituel qui complique l’analyse), **CredoMap** (stealer de credentials), **Cannon** (backdoor), **Seduploader** (implant).
- **Mimikatz** pour le credential dumping.

**OPSEC** : moyen à élevé — nettement moins furtif que le SVR/APT29. APT28 assume un niveau de bruit plus élevé pour l’efficacité opérationnelle. Plusieurs campagnes ont été identifiées par des erreurs d’OPSEC (réutilisation d’infrastructure, horaires compatibles Moscou, artefacts langue russe).

**Campagnes majeures** :

- **DNC hack** (2016) : compromission du Comité National Démocrate américain. Les données (emails, documents internes) sont publiées via DCLeaks et WikiLeaks dans une opération hack-and-leak coordonnée pour impacter l’élection présidentielle. Attribution par FBI, DHS, Office of the Director of National Intelligence (janvier 2017). Indictment DOJ en 2018 qui inculpe nommément 12 officiers du GRU Unit 26165.
- **WADA breach** (2016) : vol et publication de données médicales d’athlètes olympiques, en représailles à l’exclusion d’athlètes russes pour dopage systémique.
- **Bundestag breach** (2015) : compromission du réseau informatique du parlement allemand, accès maintenu plusieurs semaines, exfiltration massive de documents. La réponse allemande a inclus une reconstruction complète du réseau.
- **TV5Monde** (2015) : bien que revendiquée par un groupe présenté comme « CyberCaliphate » affilié à l’État islamique, l’attribution technique a pointé vers APT28 (false flag — tradecraft similaire, infrastructure compromise).
- **Exploitation massive CVE-2023-23397** (2022-2023) : APT28 a exploité cette vulnérabilité Outlook contre des dizaines d’organisations européennes (gouvernements, défense, énergie, transport) pendant près d’un an avant découverte publique.
- **Campagnes 2023-2025** : ciblage continu des organisations ukrainiennes, alliés de l’OTAN, ministères européens. Utilisation accrue de services de stockage cloud (MEGA, pCloud) pour l’exfiltration.

**Évolution récente** : APT28 a maintenu un haut niveau d’activité post-2022. Utilisation croissante d’**infostealers** comme vecteur d’accès initial (achat de logs sur les marchés dark web pour obtenir des credentials initiaux, plutôt que phishing). Campagne **MooBot** (botnet de routeurs Ubiquiti compromis, utilisé comme infrastructure de proxy) démantelée par le FBI en février 2024 — modèle similaire à Volt Typhoon mais côté russe.

### 6.3 Sandworm / Seashell Blizzard (GRU Unit 74455)

**Mission** : opérations destructives et sabotage — le bras armé du cyber russe. Cibles : infrastructures critiques (énergie principalement, télécoms, secteur financier), gouvernements, sous-traitants militaires. Ciblage privilégié : Ukraine, pays OTAN de la première ligne (Pologne, États baltes), occasionnellement infrastructures mondiales (NotPetya a touché le monde entier via la supply chain M.E.Doc).

**TTP signature** :

- **Wipers** : Sandworm est le groupe au monde qui a déployé le plus de wipers différents. **NotPetya / ExPetr** (2017, wiper masqué en ransomware, propagation via supply chain M.E.Doc + EternalBlue), **CaddyWiper** (2022, wiper destructif Ukraine), **HermeticWiper / FoxBlade** (février 2022, veille de l’invasion), **IsaacWiper** (février 2022), **AcidRain** (février 2022, contre les terminaux satellites Viasat KA-SAT — impact collatéral sur les éoliennes allemandes qui utilisaient le même opérateur). Plusieurs variants récents non publiquement catalogués.
- **Attaques OT/ICS** : **Industroyer / CrashOverride** (2016, premier malware ciblant les protocoles industriels IEC 60870-5-104 et IEC 61850 pour provoquer un blackout), **Industroyer2** (2022, tentative déjouée par CERT-UA et ESET), **CosmicEnergy** (2023, découvert par Mandiant — malware OT conçu pour attaquer les systèmes de protection IEC 60870-5-104, capacités similaires à Industroyer mais avec des différences techniques suggérant une nouvelle branche de développement). Détaillé au Ch.21.
- **Supply chain** : compromission de M.E.Doc (logiciel comptable ukrainien utilisé par des milliers d’organisations) pour la propagation initiale de NotPetya — paradigme supply chain.
- **Exploitation d’edge devices et routeurs** : **Cyclops Blink** (botnet 2022 sur routeurs ASUS et WatchGuard — démantelé par le FBI).
- **Mouvement latéral classique** : Mimikatz, PsExec, RDP.
- **False flags sophistiqués** : **Olympic Destroyer** (2018, Jeux Olympiques de Pyeongchang) incluait des fragments de code Lazarus plantés délibérément pour brouiller l’attribution. L’analyse minutieuse par Kaspersky a identifié les faux marqueurs et confirmé l’attribution Sandworm.

**Particularité historique** : Sandworm est le **seul groupe APT dans le monde à avoir causé publiquement documenté des pannes d’électricité** via cyberattaque. Ukraine 2015 (BlackEnergy/KillDisk, 230 000 foyers, 6 heures) et 2016 (Industroyer, Kiev, 1 heure). Ces événements sont les seuls cas avérés d’impact physique étendu d’une cyberattaque sur un système de distribution d’énergie.

**OPSEC** : variable. Sandworm assume un niveau de bruit élevé pour ses opérations destructives (l’impact est l’objectif, la furtivité post-impact n’est plus nécessaire). Mais les phases de reconnaissance et de déploiement sont menées avec un OPSEC sérieux. Les attributions publiques ont été facilitées par des artefacts (strings, infrastructure) qui suggèrent une discipline OPSEC moindre que celle du SVR.

**Campagnes majeures** :

- **Ukraine 2015-2016** : BlackEnergy et Industroyer (Ch.21).
- **NotPetya** (juin 2017) : déployé initialement via M.E.Doc en Ukraine, propagation mondiale en heures via EternalBlue et credentials Windows. Dommages mondiaux estimés à 10+ milliards de dollars (Maersk, Merck, FedEx/TNT Express, Saint-Gobain, etc.). Attribution publique par CIA (juin 2017), UK NCSC et DoD (février 2018). Reconnaissance formelle comme « la cyberattaque la plus destructrice de l’histoire » par les États-Unis.
- **Olympic Destroyer** (2018) : ciblage des Jeux Olympiques d’hiver de Pyeongchang, en représailles à l’exclusion de la délégation russe pour dopage. Plusieurs composants techniques des JO compromis (site web, système Wi-Fi du stade olympique, systèmes de télévision). False flags multiples (code Lazarus, infrastructure iranienne).
- **Campagne Ukraine 2022-présent** : série continue de wipers, tentatives sur les infrastructures critiques (Industroyer2 déjouée), ciblage des télécoms et des médias, opérations OT sur les réseaux électriques ukrainiens coordonnées avec des frappes militaires.
- **Viasat KA-SAT (février 2022)** : attaque via **AcidRain** contre les terminaux satellite du fournisseur Viasat, timing synchronisé avec l’invasion. Impact principal : communications militaires ukrainiennes. Impact collatéral notable : 5 800 éoliennes allemandes utilisant le même service de connectivité satellite, inopérables pendant plusieurs semaines. Attribution publique par UE, UK, US (mai 2022).

**Évolution récente (2024-2026)** : Sandworm reste actif en Ukraine et étend son ciblage aux alliés. CosmicEnergy (2023) révèle une continuité de R&D sur les malwares OT. Des rapports Mandiant et Microsoft de 2024 suggèrent une professionnalisation croissante et un élargissement géographique (ciblage documenté de l’Europe de l’Ouest, y compris la France et l’Allemagne).

### 6.4 GRU Unit 29155

**Identification publique** : advisory conjoint NSA/FBI/CISA + partenaires internationaux (UK, Pologne, Estonie, Lettonie, Lituanie, Tchéquie, Allemagne, Ukraine, Canada, Australie) en septembre 2024.

**Mission** : opérations déstabilisatrices cyber-physiques au soutien d’objectifs stratégiques plus larges. Unit 29155 était historiquement connue pour des opérations clandestines non-cyber (sabotages physiques, empoisonnements — Salisbury 2018 contre les Skripal, impliquée), mais l’advisory 2024 a confirmé son extension au cyber.

**TTP signature** (telles que documentées par l’advisory) :

- **Accès initial** : exploitation de vulnérabilités publiques (VPN, passerelles web), phishing, bruteforce.
- **Malware custom** : **WhisperGate** (wiper déployé contre l’Ukraine en janvier 2022, attribué initialement à Sandworm puis réattribué à Unit 29155 après l’advisory).
- **Outils communs** : Impacket, Mimikatz, PsExec — tradecraft partagé avec le reste de l’écosystème GRU.
- **Ciblage OT** : l’advisory mentionne des tentatives d’attaques contre des systèmes OT européens, sans détails publics précis.

**Distinction avec Sandworm** : Sandworm (Unit 74455) est une unité cyber dédiée de longue date, avec une sophistication technique importante et des malwares signature. Unit 29155 est une unité historiquement non-cyber qui a développé des capacités cyber plus récemment — sophistication technique moindre que Sandworm, mais intégration plus directe avec des opérations clandestines non-cyber. La distinction importe pour l’analyse : attribuer une opération à l’une ou l’autre unité révèle des intentions différentes.

**Campagnes connues** :

- **WhisperGate** (janvier 2022) : wiper déployé contre des organisations ukrainiennes (gouvernement, ONG, IT) quelques semaines avant l’invasion. Masqué en ransomware (note de rançon incohérente). Impact réel : destructive, non récupérable.
- **Campagnes documentées par l’advisory 2024** : tentatives d’attaques contre des infrastructures européennes, y compris dans des pays ayant soutenu activement l’Ukraine. Détails classifiés.

**Implications opérationnelles** : pour l’analyste, la reconnaissance d’Unit 29155 comme acteur distinct signifie que le GRU dispose d’au moins deux unités capables d’opérations destructives cyber — augmentation de la surface de menace et de la capacité de redondance opérationnelle.

### 6.5 Turla / Snake / Secret Blizzard (FSB Centre 16)

**Mission** : espionnage long terme contre cibles gouvernementales et diplomatiques de haute valeur. Ciblage : ministères des affaires étrangères dans le monde, ambassades, organisations internationales, parfois entreprises de défense et think tanks stratégiques.

**TTP signature** :

- **Watering hole** : compromission de sites web fréquentés par les cibles pour les infecter lors de leur visite. Sites gouvernementaux, académiques, ou institutionnels pertinents pour la cible.
- **Supply chain** : opérations de longue durée impliquant compromission d’éditeurs ou de prestataires pour atteindre les cibles finales.
- **Malware signature** — Turla développe et maintient un arsenal malware remarquable :
  - **Snake / Uroburos** : rootkit multi-plateforme (Windows, Linux, macOS) actif depuis au moins 2003. Persistence kernel, évasion sophistiquée, communications P2P entre instances. Démantelé par le FBI en mai 2023 (opération Medusa) mais les variants post-Snake continuent.
  - **Kazuar** : backdoor modulaire (.NET) utilisée pour des opérations ciblées.
  - **LightNeuron** : backdoor Exchange serveur (transport agent malveillant) — interception d’emails au niveau serveur. Actif depuis au moins 2014, découvert par ESET en 2019.
  - **Crutch** : backdoor Windows utilisée contre des cibles diplomatiques en Europe.
  - **Carbon / Cobra** : framework modulaire historique.
- **Infrastructure par satellite** : Turla est documenté pour avoir utilisé des **liaisons satellite détournées** comme canal C2 — exploitation de liaisons satellite de FAI commerciaux (clients commerciaux des FAI satellites dans des régions où la sécurité est faible) pour masquer l’origine réelle des C2. Technique documentée par Kaspersky en 2015.
- **Piggybacking sur d’autres APT** : Turla a été observé en train d’utiliser l’**infrastructure d’autres groupes APT** pour ses opérations. Le cas le plus documenté : Turla a compromis l’infrastructure d’APT34 (OilRig, Iran) et l’a utilisée pour mener ses propres opérations. Cette technique, documentée publiquement par UK NCSC et NSA en octobre 2019, est unique dans le monde APT par son niveau de sophistication opérationnelle et par l’impact qu’elle a sur l’attribution (une victime peut voir une intrusion qui semble iranienne alors qu’elle est russe).

**OPSEC** : la plus sophistiquée de l’écosystème russe, probablement parmi les plus sophistiquées du monde APT. Opérations de longue durée (certaines compromissions gouvernementales ont duré 5-10 ans). Arsenal malware constamment renouvelé. Peu d’erreurs d’OPSEC documentées.

**Campagnes majeures** :

- **Opérations contre les diplomaties européennes** (depuis au moins les années 2000) : ciblage continu des ministères des affaires étrangères, avec des compromissions parfois longues et silencieuses.
- **RUAG breach (Suisse, 2014-2016)** : la société suisse RUAG (défense, détenue par l’État) a été compromise pendant près de deux ans. Exfiltration massive de données.
- **German Federal Foreign Office** (2017-2018) : compromission du réseau du ministère allemand des affaires étrangères, accès maintenu plusieurs mois.
- **Opération Medusa** (mai 2023, côté défense) : démantèlement du malware Snake par le FBI. Le FBI a développé un outil (PERSEUS) qui exploite des fonctionnalités de Snake lui-même pour rendre le malware inopérant sur les machines infectées, sans interagir avec les systèmes au-delà. Coordination internationale (États affectés notifiés). Opération citée comme un modèle d’action offensive law enforcement contre un malware APT.

**Évolution récente (2024-2026)** : Turla a continué ses opérations avec des outils post-Snake. Un rapport Microsoft de novembre 2023 a détaillé des compromissions continues de ministères ukrainiens et européens par Secret Blizzard, utilisant des techniques post-Snake (détournements d’infrastructure d’Andromeda — un ancien crimeware — pour piggybacker sur les infections existantes). Le modèle opérationnel Turla — sophistication extrême, patience, piggybacking — reste actif.

### 6.6 Gamaredon / Aqua Blizzard (FSB Centre 18)

**Mission** : ciblage massif continu de l’Ukraine. Cibles : institutions ukrainiennes (gouvernement, défense, sécurité, énergie, médias, ONG), diaspora ukrainienne.

**TTP signature** :

- **Phishing de masse** : volume extrêmement élevé, thèmes adaptés à l’actualité ukrainienne. Documents Office avec macros VBA (technique relativement ancienne mais toujours efficace à grande échelle).
- **Templates VBA** : Gamaredon maintient une bibliothèque de templates macros mise à jour régulièrement. Les macros sont relativement simples techniquement mais produites en volume.
- **Scripts VBS et PowerShell** : petits scripts de téléchargement et d’exécution, souvent peu obfusqués.
- **Infrastructure Telegram pour C2** : Gamaredon est l’un des rares acteurs étatiques à utiliser massivement Telegram comme canal de C2. Les implants récupèrent leurs instructions depuis des canaux Telegram contrôlés. Technique inhabituelle pour un acteur étatique, plus proche d’un modèle cybercriminel — mais Gamaredon assume un profil opérationnel différent des autres APT russes.
- **Persistence agressive** : Gamaredon réinfecte rapidement après éradication. Les victimes ukrainiennes rapportent des cycles infection/détection/éradication/réinfection qui se répètent en jours ou semaines.
- **Malwares signature** : **Pterodo** (famille de backdoors légères), **Pteranodon**, **GammaLoad** — moins sophistiqués que les outils SVR ou Sandworm, mais produits et renouvelés en volume.

**Particularité** : Gamaredon est le « marteau » là où Turla est le « scalpel ». Sophistication technique modeste, mais volume massif, persistance, et impact cumulé important. Le CERT-UA classe Gamaredon comme la menace cyber la plus continue contre l’Ukraine — pas la plus dangereuse individuellement, mais la plus omniprésente.

**OPSEC** : faible à moyenne. Pas d’effort majeur pour cacher l’origine — Gamaredon assume son rôle de « bruit de fond » plutôt que d’opération clandestine sophistiquée. Des artefacts linguistiques russes, des patterns d’horaires Moscou, et des réutilisations d’infrastructure sont fréquents.

**Évolution post-invasion** : volume massivement augmenté depuis février 2022. Gamaredon est l’acteur qui génère le plus grand volume de cyberactivité hostile contre l’Ukraine au quotidien. Adaptations techniques marginales (nouveaux thèmes de phishing, quelques variants de malware), mais continuité générale du modèle opérationnel.

### 6.7 Dragonfly / Energetic Bear / Berserk Bear

**Attribution** : attribué à la Russie avec haute confiance, rattachement spécifique au FSB Centre 16 (selon des analyses US) ou à une entité distincte — la clarté d’attribution inter-services russes est moins nette que pour APT28/APT29.

**Mission** : ciblage énergie historique. Reconnaissance et pré-positionnement dans le secteur énergie (électricité, pétrole, gaz, nucléaire) aux US et en Europe. Pas d’action destructive publiquement documentée, mais patterns cohérents avec une préparation de capacités.

**TTP signature** :

- Watering hole sur des sites de publications industrielles fréquentés par les ingénieurs énergie.
- Compromission supply chain via des éditeurs de logiciels industriels (compromission d’**eWON Talk2M** en 2017).
- Exploitation SMB, Mimikatz.
- Développement de connaissances opérationnelles sur les systèmes ICS des cibles (reconnaissance approfondie, pas d’action destructive).

**Campagnes majeures** :

- **Opérations énergie US 2017-2018** : advisory conjoint US-CERT/FBI en mars 2018 détaille une campagne russe de pré-positionnement dans le secteur énergie US, avec des accès confirmés dans plusieurs organisations. Pas de destructive action.
- **Cibles énergie européenne** : ciblage documenté de sociétés énergie britanniques, allemandes, italiennes (2016-2020).

**Évolution récente** : activité Dragonfly moins documentée publiquement depuis 2020, mais le ciblage énergie par la Russie s’est poursuivi (notamment via Sandworm). Certains analystes considèrent que Dragonfly a été réorganisé ou fusionné dans d’autres structures cyber russes post-2022.

### 6.8 Évolution de l’écosystème russe post-invasion ukrainienne

Post-février 2022, plusieurs évolutions structurantes :

**Intensification opérationnelle** : volume d’attaques historiquement élevé. L’Ukraine est l’environnement de confrontation cyber le plus intense au monde. Les groupes russes sont déployés à plein régime.

**Émergence d’Unit 29155** : publiquement documentée en 2024, suggérant que l’appareil cyber GRU a été élargi ou réorganisé pour accroître les capacités destructives.

**Pression économique sur le cybercrime russophone** : sanctions, restrictions de blanchiment, pression sur les cryptomonnaies ont fragilisé l’écosystème. Certains groupes se sont reconstitués, d’autres ont migré vers d’autres juridictions.

**Professionnalisation continue** : le GRU Units 26165 et 74455 ont adapté leurs TTP, développé de nouveaux malwares (CosmicEnergy, variants de wipers), et sophistiqué leur ciblage. APT29 a renforcé son tradecraft cloud/identity.

**Visibilité accrue côté défense** : la coopération entre les services occidentaux et l’Ukraine (notamment via Microsoft Threat Intelligence, Mandiant, ESET) a produit un volume de documentation sans précédent sur les APT russes. Ce qui permet aux défenseurs occidentaux d’anticiper les tactiques.

L’équilibre offensif/défensif en cyber russe 2025-2026 est caractérisé par un écosystème russe plus actif que jamais, mais face à des défenseurs occidentaux mieux préparés et mieux informés qu’auparavant.

-----

## Chapitre 7 — Russie : campagnes de référence et opérations d’influence

Ce chapitre présente les campagnes russes les plus emblématiques, en complément des descriptions de groupes du Ch.6. Plusieurs de ces campagnes sont traitées de manière approfondie ailleurs dans le cours (SolarWinds au Ch.29, Industroyer au Ch.21). Ce chapitre les resitue dans une perspective d’ensemble et ajoute les opérations d’influence.

### 7.1 SolarWinds / SUNBURST (2020-2021)

**Acteur** : APT29 (SVR). **Paradigme** : supply chain comme vecteur d’espionnage à très grande échelle.

**Synthèse** : compromission du processus de build du logiciel SolarWinds Orion (logiciel de supervision réseau déployé dans des dizaines de milliers d’organisations). Une backdoor (SUNBURST) est injectée dans les builds officiels signés entre février et juin 2020. La mise à jour trojanisée est distribuée à ~18 000 organisations clientes. APT29 sélectionne ~100 cibles de haute valeur (Trésor US, Commerce, DHS, Pentagone partiellement, Microsoft, FireEye, autres) et déploie des outils de seconde étape (TEARDROP, RAINDROP, GoldMax). Mouvement latéral via GoldenSAML pour accéder aux emails et documents Azure AD/O365.

**Découverte** : décembre 2020 par FireEye/Mandiant, qui enquêtait initialement sur le vol de ses propres outils Red Team.

**Impact** : accès multi-mois à des communications gouvernementales stratégiques américaines, impact massif sur la confiance dans la supply chain logicielle, déclenchement de l’Executive Order 14028 (mai 2021) qui a structuré la réponse américaine sur la sécurité logicielle. Détaillé Ch.29.

### 7.2 NotPetya (juin 2017)

**Acteur** : Sandworm (GRU Unit 74455). **Paradigme** : wiper destructif masqué en ransomware, supply chain comme vecteur de propagation initiale.

**Synthèse** : déploiement initial via une mise à jour compromise du logiciel comptable ukrainien **M.E.Doc** (largement utilisé en Ukraine pour les déclarations fiscales — une forme de supply chain massive). Une fois exécuté, NotPetya se propage latéralement via **EternalBlue** (exploit SMB de la NSA leaké par Shadow Brokers) et via des credentials collectés sur les systèmes initiaux. Il chiffre les fichiers de manière **irréversible** — le mécanisme de rançon est factice, la clé de déchiffrement n’existe pas réellement. C’est un wiper déguisé, pas un ransomware.

**Propagation mondiale** : de l’Ukraine, NotPetya se propage aux multinationales ayant des bureaux en Ukraine, puis à leur réseau global. Victimes notables : **Maersk** (~300 M$ de dommages, opérations maritimes mondiales paralysées), **Merck** (~870 M$), **FedEx/TNT Express** (~400 M$), **Saint-Gobain** (~380 M$), **Mondelez** (~150 M$), et des dizaines d’autres. Dommages mondiaux estimés à **10+ milliards de dollars**.

**Attribution** : CIA (attribution interne juin 2017, publicisée février 2018), UK NCSC et DoD (février 2018), US Treasury (sanctions 2018), Five Eyes. Reconnu formellement comme « la cyberattaque la plus destructrice de l’histoire » par les autorités américaines.

**Leçons** : la supply chain d’un petit éditeur peut produire un impact mondial. Le destructif peut être masqué en criminalité. Les dommages collatéraux d’une opération étatique peuvent dépasser massivement les objectifs initiaux (NotPetya était initialement ciblé sur l’Ukraine, l’ampleur mondiale semble avoir été anticipée mais assumée).

### 7.3 Ukraine 2015-2016 : les premiers blackouts cyber

**Acteur** : Sandworm (GRU Unit 74455). **Paradigme** : cyber OT causant un impact physique direct.

**Ukraine décembre 2015 — BlackEnergy / KillDisk** : trois distributeurs d’électricité ukrainiens compromis. Les opérateurs Sandworm prennent le contrôle à distance des systèmes SCADA et ouvrent manuellement des disjoncteurs, coupant l’alimentation de ~230 000 foyers pendant ~6 heures. KillDisk efface ensuite les systèmes de supervision pour compliquer la récupération. Premier blackout confirmé causé par une cyberattaque.

**Ukraine décembre 2016 — Industroyer / CrashOverride** : cyberattaque plus sophistiquée, automatisée via le malware Industroyer. Industroyer manipule directement les protocoles industriels (IEC 60870-5-104, IEC 61850, OPC DA) pour commander les équipements sans intervention humaine. Ouverture de disjoncteurs à un poste de transformation à Kiev, blackout d’~1 heure. Premier malware conçu spécifiquement pour attaquer les systèmes de contrôle électriques via les protocoles natifs.

**Analyse complète** au Ch.21 (OT/ICS).

### 7.4 Ingérence électorale 2016 aux États-Unis

**Acteur** : APT28 (GRU Unit 26165) pour les compromissions cyber, Internet Research Agency (IRA, entité séparée) pour l’influence sur les réseaux sociaux. **Paradigme** : hack-and-leak coordonné comme instrument d’influence politique.

**Volet cyber** : APT28 compromet le **Comité National Démocrate** (DNC) et le comité de campagne de Hillary Clinton, exfiltre des milliers d’emails et de documents internes entre l’été 2015 et l’été 2016. Les documents sont ensuite publiés en vagues coordonnées via **DCLeaks** (plateforme créée par APT28), **Guccifer 2.0** (persona fictive présentée comme un hacker roumain indépendant — en réalité GRU), et surtout **WikiLeaks** (qui publie les emails Podesta le 7 octobre 2016, quelques heures après la diffusion d’une vidéo embarrassante pour Trump — le timing coordonné suggère une tentative de détournement de l’attention médiatique).

**Volet influence** : l’Internet Research Agency (IRA, troll farm à Saint-Pétersbourg liée à Prigojine) conduit une campagne massive d’influence sur les réseaux sociaux (Facebook, Instagram, Twitter, YouTube) — création de milliers de faux comptes amplifiant des messages polarisants sur des sujets sociétaux (race, armes, immigration), organisation d’événements physiques via des fausses identités.

**Attribution** : ODNI report (janvier 2017) établit l’attribution à la Russie avec « haute confiance ». Indictment DOJ 2018 inculpe nommément 12 officiers du GRU Unit 26165 et 13 personnes/3 entités de l’IRA. Les sanctions et expulsions diplomatiques qui suivent marquent une rupture.

**Leçons** : le cyber et l’influence sont intégrés, pas séparés. Les attributions publiques rapides (2 mois après l’élection) deviennent un standard.

### 7.5 Bundestag 2015 et campagnes anti-OTAN continues

**Acteur** : APT28. **Paradigme** : espionnage gouvernemental stratégique.

**Bundestag (mai 2015)** : APT28 compromet le réseau IT du parlement allemand. Accès maintenu plusieurs semaines, exfiltration massive de documents parlementaires (dont certains classifiés). La découverte conduit à une reconstruction complète du réseau (des mois de travail, des dizaines de millions d’euros). La chancelière Merkel est elle-même directement visée (son adresse email personnelle parlementaire a été compromise).

**Campagnes continues OTAN** : APT28 et APT29 maintiennent un ciblage permanent des ministères de la défense, des institutions de l’OTAN (Alliance, agences), des fournisseurs de défense majeurs, et des think tanks stratégiques. Ces campagnes sont rarement publicisées en détail (les victimes ne communiquent pas), mais des fragments apparaissent dans les rapports de Mandiant, Microsoft, ANSSI. La règle : tout ce qui touche à la stratégie OTAN est une cible prioritaire des services russes.

### 7.6 Campagne Ukraine 2022-présent

La campagne cyber russe contre l’Ukraine depuis février 2022 est la plus intense de l’histoire. Microsoft Threat Intelligence Center a publié plusieurs rapports annuels qui documentent des dizaines de campagnes distinctes et des centaines de cibles. Synthèse.

**Wipers multiples** : HermeticWiper, IsaacWiper, CaddyWiper, WhisperGate, AcidRain, plusieurs variants non catalogués. Déploiement souvent synchronisé avec des événements militaires ou politiques (invasion initiale, changements stratégiques, anniversaires).

**Attaques OT** : tentative **Industroyer2** en avril 2022 contre un opérateur électrique ukrainien — **déjouée** par le CERT-UA et ESET grâce à une détection et une réponse en quelques heures. Échec notable pour Sandworm. Des tentatives ultérieures ont été déjouées, d’autres partiellement réussies (blackouts ponctuels rapidement restaurés).

**AcidRain / Viasat (24 février 2022)** : le jour de l’invasion, Sandworm déploie AcidRain contre les terminaux satellite du fournisseur Viasat KA-SAT. Impact premier : perturbation des communications militaires ukrainiennes (dépendantes de Viasat pour certaines liaisons). Impact collatéral : **5 800 éoliennes allemandes** utilisant Viasat KA-SAT pour la télésupervision rendues inopérables — exemple frappant d’effet collatéral transfrontalier d’une cyberattaque étatique. Attribution publique par UE, UK, US en mai 2022.

**Ciblage multi-secteurs** : gouvernement ukrainien, médias, télécoms, énergie, transport, secteur financier, organisations humanitaires, infrastructure cloud. Gamaredon en continu sur le volume, Sandworm pour les opérations majeures, APT28 pour l’espionnage militaire, Unit 29155 pour les opérations déstabilisatrices.

**Coopération défensive sans précédent** : Microsoft, Google, ESET, AWS, Cloudflare, Starlink (connectivité résiliente), CERT-UA, USCYBERCOM hunt forward teams, européens (CERT-EU, ANSSI, BSI, NCSC). Cette coopération est détaillée au Ch.19 (Ukraine).

### 7.7 Microsoft breach 2023-2024

**Acteur** : APT29. **Paradigme** : compromission cloud identity contre le plus grand fournisseur cloud du monde.

**Synthèse** : en novembre 2023, APT29 conduit un password spray contre un tenant Azure AD test non-production de Microsoft. Un compte avec des permissions héritées sur un environnement de test est compromis. L’attaquant pivote via une application OAuth legacy aux permissions Graph API excessives, qui permet l’accès aux emails de dirigeants Microsoft. Persistence établie via création d’applications OAuth supplémentaires.

**Détection** : Microsoft détecte l’intrusion en janvier 2024 (dwell time : ~2 mois). Divulgation publique le 19 janvier 2024.

**Cibles additionnelles** : Hewlett Packard Enterprise révèle une compromission liée en janvier 2024. D’autres organisations (non nommées publiquement) ont été affectées via des patterns similaires.

**Leçons** : même les fournisseurs cloud les plus matures sont vulnérables via des configurations héritées et des environnements de test. Les abus d’applications OAuth avec permissions excessives sont un vecteur APT29 récurrent. La visibilité sur les consentements OAuth et les permissions Graph API est devenue une priorité de sécurité cloud.

### 7.8 Opérations d’influence

Les opérations d’influence russes méritent un traitement dédié car elles sont intégrées aux opérations cyber dans la doctrine hybride.

**Internet Research Agency (IRA)** : troll farm basée à Saint-Pétersbourg, liée à Evgueni Prigojine (fondateur du groupe Wagner, tué dans un accident d’avion en août 2023 après la mutinerie contre Poutine). L’IRA a conduit depuis les années 2010 des opérations massives d’influence sur les réseaux sociaux occidentaux (US, Europe). Post-Prigojine, l’organisation a connu une période d’incertitude puis a apparemment été reprise sous contrôle étatique direct.

**Doppelganger** : opération d’influence identifiée publiquement à partir de 2022. Création de faux sites web imitant l’apparence de médias occidentaux légitimes (Le Parisien, Der Spiegel, The Guardian), publication d’articles orientés, diffusion via réseaux sociaux. Démantèlements partiels par Meta, Google, et les autorités françaises. Attribution : proxies russes, avec liens suspectés aux services.

**RRN (Reliable Recent News) / Recent Reliable News** : opération similaire à Doppelganger, ciblage européen et français.

**Storm-1516** (nomenclature Microsoft, 2024) : opération de désinformation liée à la Russie, ciblant des événements politiques européens.

**Techniques** : création de volumes massifs de faux comptes (avec usage croissant d’IA générative pour les profils et le contenu), exploitation de faux sites médias, amplification via influenceurs complaisants, exploitation d’événements réels pour injecter des narratifs orientés.

**Lecture opérationnelle** : une opération d’influence russe typique coordonne plusieurs leviers (hack-and-leak si pertinent, sites médias fabriqués, comptes réseaux sociaux, amplification sur Telegram et plateformes alternatives). Les cyberopérations alimentent l’influence (vol de documents ensuite publiés), l’influence justifie les cyberopérations (campagne de préparation d’opinion avant une action cyber).

### 7.9 Leçons : l’intégration espionnage / destruction / influence

La synthèse de l’expérience russe en cyberopérations révèle un modèle intégré unique.

**Continuum d’opérations** : espionnage, influence, sabotage et pré-positionnement ne sont pas des catégories séparées. Un même service peut conduire plusieurs types simultanément ; les TTP se recouvrent ; le renseignement collecté à un stade nourrit les opérations du stade suivant.

**Tolérance au bruit variable selon le service** : SVR (APT29) maximise la furtivité ; GRU (APT28, Sandworm, Unit 29155) accepte le bruit pour l’efficacité opérationnelle ; FSB varie (Turla ultra-furtif, Gamaredon volumineux et peu furtif).

**Utilisation du cybercrime et de l’hacktivisme comme leviers** : la tolérance tacite de l’écosystème cybercriminel russophone et l’instrumentalisation d’hacktivistes (KillNet, NoName057(16)) permettent d’augmenter la surface opérationnelle sans attribution étatique directe.

**Exposition relativement élevée** : comparé à la Chine (furtive), la Russie assume une visibilité d’opérations supérieure — les attributions publiques sont fréquentes, les indictments nombreux, les sanctions accumulées. L’appareil russe semble juger que l’impact opérationnel dépasse le coût diplomatique.

Pour l’analyste face à une intrusion compatible avec un acteur russe : la clé est de déterminer **quel service** est probablement en jeu, car cela conditionne les attentes (espionnage furtif long terme si SVR, destructif à venir si GRU, opération déstabilisatrice si Unit 29155). Cette discrimination est souvent plus importante, opérationnellement, que l’attribution à « la Russie » en général.

-----
