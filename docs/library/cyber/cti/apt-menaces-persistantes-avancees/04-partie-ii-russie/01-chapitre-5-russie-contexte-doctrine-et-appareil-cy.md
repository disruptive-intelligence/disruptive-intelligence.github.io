---
title: 'Chapitre 5 — Russie : contexte, doctrine et appareil cyber'
source: Cyber/01_CTI/APT_vFULL.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie II — Russie
  - index.md
---

## 5.1 Priorités géopolitiques et principes doctrinaux

Les cyberopérations russes sont compréhensibles à condition de les situer dans les priorités géopolitiques nationales. Quatre priorités structurent l’ensemble : maintien du statut de grande puissance face aux États-Unis et à la Chine, contrôle de l’étranger proche (ex-URSS — Ukraine, Biélorussie, Caucase, Asie centrale), confrontation avec l’OTAN, et préservation du régime interne face aux pressions extérieures perçues et à la dissidence.

Chaque priorité génère des cyberopérations cohérentes. Le maintien de puissance alimente l’espionnage stratégique (SVR contre les gouvernements occidentaux), l’influence électorale (ingérence 2016 aux US, campagnes européennes), et la démonstration de capacité (NotPetya). Le contrôle de l’étranger proche motive le ciblage massif de l’Ukraine (Gamaredon au quotidien, Sandworm en escalade), les opérations contre la Biélorussie et la Géorgie. La confrontation OTAN génère les attaques contre les ministères de la défense, les think tanks stratégiques, les ambassades. La préservation du régime alimente la surveillance des opposants, des journalistes, et la contre-ingérence.

La **doctrine de la guerre hybride** (gibridnaya voyna) est le cadre intégrateur. Formulée par Valery Gerasimov (chef d’état-major des armées russes, essai de 2013 devenu « doctrine Gerasimov » dans la lecture occidentale — lecture que Gerasimov a lui-même contestée), elle postule que les moyens non militaires (information, cyber, économie, pression diplomatique) ont dépassé les moyens militaires dans l’efficacité pour atteindre les objectifs stratégiques. Le cyber est intégré dans ce continuum, aux côtés de la désinformation et des opérations d’influence.

La conséquence opérationnelle majeure : **pas de séparation nette entre espionnage et action**. Un même service (le GRU notamment) mène simultanément de la collecte de renseignement, de la destruction, et de l’influence. Le renseignement collecté est utilisé pour des opérations d’influence (hack-and-leak — DNC 2016), pour du sabotage ciblé, ou pour préparer des opérations conventionnelles. Cette intégration est le trait le plus distinctif de la doctrine russe, comparée à la doctrine américaine où renseignement (NSA), militaire offensif (USCYBERCOM) et law enforcement (FBI) sont plus nettement séparés.

## 5.2 Le SVR : espionnage stratégique furtif

Le **SVR** (Служба внешней разведки — Service de Renseignement Extérieur) est le successeur post-soviétique du premier directorat du KGB. C’est le service russe chargé de l’espionnage stratégique — gouvernements étrangers, diplomatie, think tanks, grandes entreprises technologiques. Son style opérationnel est la **furtivité maximale** et le **long terme**.

Le groupe APT associé au SVR est **APT29** (Mandiant) / **Cozy Bear** (CrowdStrike) / **Midnight Blizzard** (Microsoft, anciennement NOBELIUM). APT29 est considéré comme l’un des trois ou quatre groupes APT les plus sophistiqués au monde. Ses caractéristiques opérationnelles se retrouvent dans chaque campagne : investissement massif en reconnaissance, infrastructure compartimentée (chaque cible a sa propre infrastructure C2), abus maîtrisé des services cloud légitimes, malware custom de haute qualité, et OPSEC quasi sans faute.

Les opérations emblématiques d’APT29 incluent **SolarWinds / SUNBURST** (2020, traité en détail au Ch.29), le **Microsoft corporate breach** de 2023-2024 (password spray sur un tenant test, pivot vers les emails de dirigeants Microsoft), les **campagnes de phishing OAuth** contre les diplomaties européennes (2022-2025), et les **ciblages continus des ministères des affaires étrangères** en Europe et en Amérique du Nord.

La tactique OAuth d’APT29 mérite une mention spécifique car elle illustre la modernité du tradecraft. Plutôt que de voler des mots de passe (détectable, temporaire), APT29 envoie à la cible des demandes d’autorisation OAuth pour des applications qui semblent légitimes (nom calqué sur Microsoft Teams, Outlook for iOS, Azure Active Directory Authenticator). Si la cible accepte, l’application malveillante obtient un jeton de refresh qui permet un accès persistant sans mot de passe, contournant la MFA. La technique est silencieuse, résiste aux rotations de mot de passe, et peut persister des mois.

## 5.3 Le GRU : opérations militaires et destructives

Le **GRU** (Главное разведывательное управление — Direction du Renseignement Militaire, rebaptisé officiellement GU — Главное управление — en 2010 mais l’acronyme GRU reste largement utilisé) est le renseignement militaire. C’est le service le plus agressif et le plus bruyant des services cyber russes. Sa mission couvre le renseignement militaire classique, mais aussi le sabotage, les opérations d’influence, et les actions déstabilisatrices.

Trois unités GRU sont publiquement identifiées comme conduisant des cyberopérations.

**Unit 26165** conduit l’espionnage militaire et politique, avec un fort volet opérations d’influence. Le groupe APT associé est **APT28** (Mandiant) / **Fancy Bear** (CrowdStrike) / **Forest Blizzard** (Microsoft) / **Sofacy** (Kaspersky). APT28 est actif depuis au moins 2007 et a été au cœur de l’ingérence électorale américaine de 2016 (hack du DNC, publication via DCLeaks et WikiLeaks). Ses campagnes incluent également le hack du Bundestag allemand (2015), les attaques contre l’Agence Mondiale Antidopage (WADA, 2016), et l’exploitation massive de la vulnérabilité Outlook CVE-2023-23397 (2023) contre les organisations européennes.

**Unit 74455** conduit les opérations destructives. Le groupe APT associé est **Sandworm** (assignation initiale par iSight Partners devenu Mandiant) / **Seashell Blizzard** (Microsoft) / **BlackEnergy group** (historique) / **Voodoo Bear** (CrowdStrike). Sandworm est le seul groupe APT au monde à avoir causé publiquement documenté des pannes d’électricité par cyberattaque (Ukraine 2015 et 2016, Ch.21). Il est également responsable de **NotPetya** (2017, wiper mondial ~10 Mrd $), d’**Olympic Destroyer** (2018, Jeux Olympiques de Pyeongchang avec false flags Lazarus), et d’une série continue de wipers contre l’Ukraine depuis 2022 (HermeticWiper, CaddyWiper, IsaacWiper, AcidRain contre le satellite Viasat KA-SAT).

**Unit 29155** a été identifiée publiquement en 2024 par un advisory conjoint (US, UK, Estonie, Pologne). C’est une unité du GRU qui conduit des **opérations déstabilisatrices cyber-physiques** au soutien d’opérations clandestines plus larges (sabotages, assassinats, harcèlement). Le malware **WhisperGate** (wiper déployé contre l’Ukraine en janvier 2022, quelques semaines avant l’invasion) est attribué à cette unité — ce qui a nécessité une révision des attributions initiales qui pointaient parfois Sandworm. Unit 29155 a également été liée à des tentatives d’attaques contre des infrastructures européennes (documentées par l’advisory CISA/NSA/FBI de septembre 2024).

La distinction entre ces unités importe pour l’analyste : une opération destructive contre l’Ukraine peut être attribuée à Sandworm (74455), à Unit 29155, ou à une coopération entre les deux. L’attribution à la bonne unité précise le cadre doctrinal et les attentes futures.

## 5.4 Le FSB : sécurité intérieure et étranger proche

Le **FSB** (Федеральная служба безопасности — Service Fédéral de Sécurité) est le successeur principal du KGB pour les missions de sécurité intérieure, de contre-espionnage, et de surveillance des voisins proches. Ses cyberopérations se concentrent sur l’Ukraine, la Biélorussie, le Caucase, et la diaspora russophone à l’étranger.

Deux centres du FSB conduisent des cyberopérations publiquement attribuées.

**Centre 16** est le centre historique de cyber-collecte du FSB, chargé de l’espionnage long terme contre des cibles gouvernementales et diplomatiques de haute valeur. Le groupe APT associé est **Turla** (Kaspersky) / **Snake** (Mandiant) / **Secret Blizzard** (Microsoft) / **Venomous Bear** (CrowdStrike). Turla est considéré comme l’un des groupes techniquement les plus avancés au monde, actif depuis au moins 1996 (ce qui en fait l’un des plus anciens groupes APT encore opérationnels). Son malware signature, **Snake** (également appelé **Uroburos**), est un rootkit multi-plateforme extraordinairement sophistiqué, actif depuis au moins 2003, avec des capacités de persistence kernel sur Windows, Linux, et macOS.

Turla est également connu pour deux signatures opérationnelles remarquables. Premièrement, l’utilisation de **communications C2 par satellite** — détournement de liaisons satellite de FAI commerciaux pour masquer l’origine réelle du C2 (documenté par Kaspersky en 2015). Deuxièmement, la technique unique de **détournement d’infrastructure d’autres groupes APT** — Turla a été observé en train d’utiliser l’infrastructure de groupes iraniens (OilRig) pour mener ses propres opérations, technique appelée « piggybacking » qui complique massivement l’attribution et représente un niveau d’OPSEC exceptionnel.

**Snake a été démantelé par le FBI en mai 2023** dans le cadre de l’**opération Medusa**. Le FBI a développé un outil qui, exploitant des fonctionnalités du malware lui-même, a pu envoyer des commandes aux implants Snake sur les machines infectées pour les rendre inopérants — sans interagir avec les systèmes eux-mêmes au-delà de la neutralisation du malware. Opération remarquable par sa technicité et par sa portée (machines infectées dans plus de 50 pays). Turla a continué ses opérations avec d’autres outils post-Snake.

**Centre 18** conduit le ciblage massif de l’Ukraine avec un volume élevé et une sophistication comparativement moindre. Le groupe APT associé est **Gamaredon** (connu aussi comme **Primitive Bear**, **Shuckworm**, **Aqua Blizzard** chez Microsoft). Gamaredon cible systématiquement les institutions ukrainiennes depuis 2013-2014 (avant l’annexion de la Crimée), avec une intensification massive depuis 2022. Son tradecraft : phishing de masse, macros Office, scripts VBA, persistance agressive (réinfection rapide après éradication), et usage de Telegram comme canal de C2 (technique inhabituelle pour un acteur étatique classique — mais Gamaredon est plus proche d’un « bruit de fond » continu qu’un opérateur furtif). Les Ukrainiens ont surnommé Gamaredon « le cadet russe » — Gamaredon est le marteau là où Turla est le scalpel.

## 5.5 L’écosystème cybercriminel russophone : zone grise

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

## 5.6 Hacktivisme instrumentalisé

À côté du cybercrime toléré, la Russie soutient ou instrumentalise plusieurs collectifs présentés comme « hacktivistes ».

**KillNet** (actif depuis 2022) revendique des cyberattaques pro-russes, principalement DDoS contre des institutions occidentales et des infrastructures ukrainiennes. La sophistication technique est modeste (essentiellement DDoS, parfois défacement), mais la coordination opérationnelle et la pérennité suggèrent un soutien ou une connivence minimale avec les services. Le groupe a muté plusieurs fois (KillNet, KillMilk, BlackSkills) et génère un volume continu d’activité pro-régime.

**NoName057(16)** (actif depuis 2022) est plus technique que KillNet. Le groupe déploie un outil DDoS distribué (**DDosia Project**) qui recrute des volontaires via Telegram et les paie en cryptomonnaies pour participer à des attaques. L’outil télécharge régulièrement des listes de cibles depuis des serveurs centralisés. Démantèlement partiel par Europol en mai 2025 — mais le modèle se reproduit.

**IT Army of Ukraine** est symétrique côté ukrainien : mouvement de volontaires cyber internationaux, lancé publiquement par le vice-premier ministre Mykhailo Fedorov via Telegram en février 2022, conduisant des opérations DDoS et de hacktivisme contre des cibles russes. Zone grise similaire : coordination étatique explicite d’un mouvement de volontaires.

Ces mouvements brouillent la distinction classique « hacktivisme vs État ». Pour l’analyste, la règle est de lire les alignements : KillNet et NoName057(16) s’alignent systématiquement sur les priorités tactiques russes (cibles sélectionnées selon l’actualité diplomatique), ce qui est incompatible avec un hacktivisme authentique.

## 5.7 Réorganisations post-2022

L’invasion de l’Ukraine en février 2022 a eu des effets sur l’appareil cyber russe qu’il est utile de documenter.

**Augmentation massive du volume opérationnel** : intensification des attaques contre l’Ukraine (wipers multiples, Gamaredon en continu, Sandworm en escalade), augmentation du ciblage des alliés de l’Ukraine (Pologne, États baltes, OTAN en général), expansion du pré-positionnement dans les infrastructures européennes.

**Professionnalisation de Unit 29155** : la publication de l’advisory de septembre 2024 a documenté l’existence et les capacités d’une unité jusque-là peu connue. Ce qui suggère que les services étatiques russes ont réalloué des ressources pour intensifier leurs opérations.

**Pression sur le cybercrime russophone** : les sanctions occidentales ont rendu plus difficile le blanchiment et la conversion des gains ransomware. Plusieurs groupes ransomware ont déplacé leurs opérations vers les cibles occidentales avec une intensité accrue. Inversement, certains opérateurs ont été observés quittant la Russie pour des juridictions plus neutres (Dubaï, Serbie), signe d’une fragilisation de l’écosystème.

**Durcissement de l’OPSEC** : post-invasion, plusieurs groupes russes ont adapté leur tradecraft. APT29 a intensifié ses campagnes OAuth et l’abus de services cloud légitimes. Sandworm a diversifié son malware (CosmicEnergy découvert 2023, variants HermeticWiper, AcidRain contre Viasat).

L’écosystème russe en 2025-2026 reste le plus actif au monde en volume d’opérations destructives documentées, avec une pression réciproque entre les services (qui doivent démontrer leur valeur opérationnelle) et les défenseurs occidentaux qui ont gagné en maturité d’attribution et de détection.

## 5.8 Fil rouge — BLACKOUT Épisode 3

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
