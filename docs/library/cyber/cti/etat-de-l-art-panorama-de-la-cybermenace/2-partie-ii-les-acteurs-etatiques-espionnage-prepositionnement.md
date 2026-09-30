---
title: 'PARTIE II — Les acteurs étatiques : espionnage, prépositionnement et déstabilisation'
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
chapter: 2
chapters: 7
---

## Chapitre 6 — La Chine : l'espionnage cyber à l'échelle globale

### 6.1 — Architecture du programme cyber chinois

Le programme cyber offensif chinois se distingue des autres par son **échelle, son ambition et sa profondeur organisationnelle**. Microsoft note dans son Digital Defense Report 2025 que « l'ampleur et l'échelle des opérations de ciblage chinoises continuent de se démarquer des autres acteurs étatiques ». Le CSE canadien est plus direct : « Parmi nos adversaires, l'échelle, le tradecraft et les ambitions du programme cyber de la RPC dans le cyberespace sont sans égal. »

L'architecture institutionnelle repose sur plusieurs piliers. Le **Ministry of State Security (MSS)** — l'agence de renseignement civil — est le principal commanditaire d'opérations de cyberespionnage. Le MSS délègue une partie de ses opérations à des entreprises privées de cybersécurité et à des « quartiers-maîtres numériques » (digital quartermasters) qui fournissent infrastructure, malware et expertise. La fuite des documents d'i-SOON en février 2024 a révélé l'ampleur de cet écosystème de sous-traitants : contrats de piratage à la demande, développement de malware sur mesure, et opérations d'intrusion ciblant des gouvernements, des entreprises et des individus dans le monde entier.

Le **People's Liberation Army (PLA)** opère ses propres unités cyber, principalement pour le renseignement militaire. L'**APT40** (également suivi comme Kryptonite Panda, Gingham Typhoon, Leviathan) est associé au MSS et cible la région Indo-Pacifique, avec un focus sur les secteurs gouvernemental, technologique et maritime.

Cette architecture de sous-traitance confère au programme chinois plusieurs avantages : la scalabilité (un réservoir de compétences extensible), la dénéabilité (les opérations sont conduites par des entités privées, pas directement par l'État), et la spécialisation (chaque sous-traitant développe une expertise sur des cibles ou des techniques spécifiques).

### 6.2 — Objectifs stratégiques

Les objectifs du programme cyber chinois s'articulent autour de quatre axes documentés par l'ensemble des sources du corpus.

Le **vol de propriété intellectuelle et l'avantage économique compétitif** reste le driver principal. Microsoft note que « la Chine utilise les opérations d'espionnage comme méthode clé pour poursuivre un avantage économique compétitif ». Les secteurs ciblés — IT, industrie manufacturière, recherche, biotechnologie — sont alignés avec les priorités du plan « Made in China 2025 » et des stratégies industrielles chinoises.

Le **remodelage de l'ordre international** est un objectif de plus en plus documenté. Microsoft observe que « à travers des campagnes coordonnées d'opérations d'influence et des intrusions cyber, la Chine cherche à affaiblir les institutions démocratiques, à semer la discorde entre alliés et à promouvoir des narratifs qui légitiment son modèle de gouvernance ». L'année 2024, qui comptait un nombre record d'élections dans le monde, a vu un investissement significatif dans la collecte de renseignement électoral et les tentatives d'influence.

La **répression transnationale** utilise le cyber pour surveiller et harceler les dissidents, les minorités (Ouïghours, Tibétains) et les critiques du Parti communiste chinois à l'étranger. Un acte d'accusation américain de 2024 documente le ciblage de membres de l'Inter-Parliamentary Alliance on China (IPAC), un groupe de parlementaires de plusieurs pays dont des Canadiens.

Le **prépositionnement** dans les infrastructures critiques occidentales — l'axe le plus préoccupant — est traité en détail dans la sous-section 6.4.

### 6.3 — Panorama des ensembles d'intrusion actifs

Le paysage des ensembles d'intrusion chinois est vaste. Les plus documentés sur la période 2024-2025 incluent :

**Volt Typhoon** se distingue par son focus exclusif sur le prépositionnement dans les infrastructures critiques américaines (énergie, transport, communications, eau). Ses TTPs sont caractérisées par l'utilisation intensive de techniques living-off-the-land (LotL) — utilisant uniquement les outils natifs des systèmes compromis — ce qui le rend extrêmement difficile à détecter. Volt Typhoon n'exfiltre pas de données et ne déploie pas de malware classique : il installe et maintient des accès dormants.

**Salt Typhoon** cible les infrastructures de télécommunications mondiales. Aux États-Unis, le groupe a été associé à la compromission d'opérateurs majeurs et au ciblage des dispositifs d'interception légale (lawful intercept) — c'est-à-dire les systèmes utilisés par les forces de l'ordre pour les écoutes autorisées par la justice. L'ANSSI note que le secteur des télécommunications est « ciblé de façon régulière et importante par les groupes d'attaquants réputés liés à la Chine ».

**Mustang Panda** cible principalement les gouvernements, les organisations internationales et les secteurs diplomatiques en Asie et en Europe. Il a été observé ciblant le secteur du transport maritime européen, avec des implants malveillants retrouvés sur des équipements embarqués.

**APT41** est un cas hybride unique : documenté par Mandiant comme un acteur menant simultanément des opérations d'espionnage étatique et de cybercriminalité à but lucratif. Cette dualité illustre la porosité entre les catégories d'acteurs dans l'écosystème chinois.

**APT40/Kryptonite Panda** se caractérise par l'exploitation rapide de vulnérabilités, souvent dans les heures ou jours suivant la publication des preuves de concept. L'ASD australien a publié un advisory détaillé sur les TTPs d'APT40 en 2024, documentant sa préférence pour l'exploitation des applications exposées à internet plutôt que le phishing.

### 6.4 — Le prépositionnement dans les infrastructures critiques

Le cas Volt Typhoon mérite un traitement approfondi parce qu'il représente un changement qualitatif dans la menace étatique. Il ne s'agit plus d'espionnage (voler de l'information) mais de **prépositionnement** (installer des accès pour une utilisation future potentiellement destructive).

Les implications stratégiques sont majeures. Si Volt Typhoon maintient des accès dans les réseaux d'énergie, de transport et de communication américains, ces accès pourraient théoriquement être activés en cas de crise — par exemple, un conflit dans le détroit de Taïwan — pour perturber la capacité de projection militaire américaine. C'est un scénario de « pré-positionnement pour le sabotage » qui dépasse le cadre traditionnel du cyberespionnage.

Les TTPs de Volt Typhoon sont spécifiquement conçues pour la persistance à long terme et l'évasion de détection : utilisation exclusive d'outils natifs du système (PowerShell, WMI, certutil), compromission de routeurs SOHO pour créer des réseaux de relais, absence de malware personnalisé déployé sur les systèmes cibles. Ces caractéristiques rendent la détection par les solutions de sécurité classiques (signatures, heuristiques) pratiquement impossible.

Le CSE canadien évalue que le Canada est également une cible potentielle de ce type de prépositionnement, « étant donné sa proximité géographique et l'interconnexion de ses infrastructures avec celles des États-Unis ». L'ANSSI observe des activités similaires ciblant l'Europe, notant que « les objectifs inconnus [des prépositionnements] doivent collectivement nous alarmer ».

### 6.5 — Le ciblage des télécommunications

Le ciblage des opérateurs de télécommunications est une constante du programme chinois, pour des raisons structurelles : les réseaux télécom transportent les communications de toutes les cibles d'intérêt (gouvernements, militaires, entreprises, individus). Compromettre un opérateur, c'est potentiellement accéder aux communications de tous ses clients.

L'ANSSI a traité en 2024-2025 des « compromissions importantes de SI d'opérateurs [de télécommunications] à des fins d'espionnage, menées par des MOA ayant développé des techniques et outils avancés spécifiques à ce domaine ». En décembre 2024, l'ASD australien s'est joint à des partenaires internationaux pour publier un advisory alertant sur la compromission de réseaux d'opérateurs télécom majeurs dans le cadre d'une campagne de cyberespionnage PRC.

Le cas Salt Typhoon est particulièrement préoccupant parce qu'il cible les dispositifs d'interception légale — les systèmes conçus pour permettre aux forces de l'ordre d'écouter les communications sous mandat judiciaire. La compromission de ces systèmes donne aux attaquants accès non seulement aux communications en cours d'écoute, mais potentiellement à l'infrastructure d'interception elle-même.

### 6.6 — Tactiques et techniques distinctives

Plusieurs caractéristiques techniques distinguent les opérations chinoises.

La **rapidité d'opérationnalisation des vulnérabilités** est une capacité distinctive documentée par l'ASD et Microsoft. APT40 est connu pour exploiter les vulnérabilités dans les heures suivant la publication des preuves de concept — un tempo qui dépasse les capacités de patching de la plupart des organisations.

L'utilisation de **réseaux de relais SOHO** (Small Office Home Office) permet aux acteurs chinois de mêler leur trafic malveillant au trafic légitime des propriétaires des équipements compromis, compliquant significativement la détection.

L'exploitation des **équipements de bordure** (VPN, firewalls, passerelles) est une préférence tactique qui reflète le fait que ces équipements sont souvent moins supervisés et moins protégés que les serveurs internes, tout en offrant un point d'entrée directement dans le réseau de la cible.

### 6.7 — Lawfare cyber : le cadre juridique chinois comme facilitateur

Un aspect spécifique de la menace chinoise, documenté par l'ANSSI, est l'utilisation du cadre juridique chinois comme outil d'espionnage. Des logiciels imposés par les autorités chinoises aux entreprises étrangères opérant en Chine peuvent comporter des fonctionnalités malveillantes intégrées par leurs éditeurs, ou être victimes d'attaques supply chain ciblant spécifiquement les entreprises étrangères.

L'ANSSI documente le cas d'un groupe pharmaceutique français dont la filiale en Chine a été confrontée à des « pressions accompagnées de menaces » exercées par les autorités locales sur un employé « afin de contourner les politiques de sécurité informatique de l'entreprise ». L'Agence recommande d'installer ces logiciels sur des postes isolés et dédiés, et de considérer la mise en place de mesures d'isolation pour mitiger les risques de fuite de données.

### 6.8 — Victimologie croisée : données quantitatives

Le croisement des données de plusieurs sources permet de construire une image plus complète de la victimologie chinoise. Microsoft identifie les 10 secteurs les plus ciblés : IT (23%), gouvernement (10%), think tanks/ONG (9%), industrie manufacturière (9%), recherche et universités (6%), commerce de détail (6%), communications (3%), finance (3%), transport (2%), santé (2%). Géographiquement, les États-Unis représentent 35% des cibles, suivis de la Thaïlande (14%), Taïwan (12%), Corée (8%) et Japon (4%).

L'ENISA ETL 2025 documente que 24% des activités étatiques contre l'UE sont attribuées à des ensembles d'intrusion China-nexus. Le CERT-EU observe que le ciblage chinois en Europe porte principalement sur les secteurs technologique, diplomatique, de la défense et de la recherche.

### 6.9 — Limites de l'analyse

Plusieurs biais doivent être explicités. Le programme chinois est probablement le plus documenté dans les sources occidentales, ce qui pourrait créer un biais de sur-représentation. La dépendance aux rapports d'éditeurs de sécurité américains introduit un biais géographique (le ciblage des États-Unis est mieux documenté que le ciblage de l'Asie du Sud-Est). L'attribution à la Chine repose souvent sur des indicateurs techniques (malwares, infrastructure) qui sont par définition manipulables. Enfin, la catégorie « China-nexus » est large et englobe des acteurs aux motivations et aux commanditaires potentiellement différents.

### 6.10 — 🔴 Fil rouge : ciblage des filiales asiatiques

> **📌 FIL ROUGE — Épisode 6**
>
> En mars 2025, la filiale malaisienne d'EuroDefense signale un incident : un employé a reçu un email contenant un document piégé portant sur un appel d'offres maritime régional. L'analyse forensique révèle un loader qui télécharge un implant PlugX — un outil historiquement associé à plusieurs groupes China-nexus, dont Mustang Panda.
>
> Sophie corrèle avec plusieurs éléments : Mustang Panda a été observé ciblant le secteur du transport maritime européen avec des implants sur des équipements embarqués. L'ANSSI documente des activités similaires. Le thème du lure (appel d'offres maritime) est cohérent avec les intérêts stratégiques chinois (Belt and Road).
>
> Sophie rédige un assessment : « L'intrusion est attribuée avec une confiance modérée (B2) à un ensemble d'intrusion China-nexus, probablement Mustang Panda, sur la base de l'outillage (PlugX), du vecteur (spearphishing thématique maritime), de la victimologie (sous-traitant défense en Asie du Sud-Est), et du contexte géopolitique. L'attribution au groupe spécifique Mustang Panda est à confiance basse en raison de la réutilisation courante de PlugX par plusieurs groupes chinois. »
>
> Elle recommande l'isolation immédiate du poste compromis, la recherche de mouvement latéral, et l'audit des connexions entre la filiale malaisienne et le réseau du groupe.

---

## Chapitre 7 — La Russie : de l'espionnage au sabotage hybride

### 7.1 — L'écosystème cyber russe

L'écosystème cyber offensif russe se distingue par sa **diversité institutionnelle et l'étendue de son réseau de proxies**. Trois services de renseignement opèrent des programmes cyber distincts, complétés par un réseau mouvant de cybercriminels patriotiques, de hacktivistes alignés et de « hackers-for-hire ».

Le **GRU** (Direction principale du renseignement militaire) opère les unités les plus offensives. L'unité 26165 (connue sous les noms APT28, Fancy Bear, Forest Blizzard) conduit des opérations d'espionnage stratégique ciblant les gouvernements, les organisations militaires et les secteurs d'intérêt pour le renseignement militaire russe. L'unité 74455 (connue comme Sandworm) est responsable des opérations les plus destructives — wipers en Ukraine, attaques contre les infrastructures énergétiques — et a été liée à l'opération de « faketivisme » Cyber Army of Russia Reborn.

Le **SVR** (Service de renseignement extérieur) opère APT29 (Nobelium, Midnight Blizzard, Cozy Bear). Le SVR se concentre sur l'espionnage stratégique de haut niveau — gouvernements, diplomatie, think tanks — avec des opérations caractérisées par leur sophistication et leur persistance. La compromission de SolarWinds (2020) et le ciblage de Microsoft en 2024 sont attribuées au SVR.

Le **FSB** (Service fédéral de sécurité) opère plusieurs groupes, dont Star Blizzard (anciennement Callisto), spécialisé dans le spearphishing ciblant les think tanks, les médias, les ONG et les personnalités impliquées dans les questions de politique étrangère. Le CERT-FR documente le ciblage par Callisto de l'ONG Reporters sans frontières. Le FSB opère également Turla, un acteur historique connu pour la sophistication de ses implants et sa capacité à compromettre d'autres acteurs pour obscurcir ses opérations.

L'écosystème russe inclut un réseau étendu de **proxies non-étatiques** — cybercriminels, hacktivistes, hackers-for-hire — motivés par un mélange de patriotisme, de profit et d'opportunisme. Le CSE canadien note que « cette stratégie hybride, qui fournit à la Russie un déni plausible, semble avoir été émulée par d'autres États, créant un environnement de cybermenace plus complexe ».

### 7.2 — Le contexte Ukraine : cyberattaques destructives et espionnage militaire

Le conflit en Ukraine reste le driver principal de l'activité cyber russe depuis février 2022. Les opérations combinent attaques destructives, espionnage militaire, ciblage logistique et opérations d'influence.

En mai 2025, l'ASD australien s'est joint à des partenaires internationaux pour alerter sur une campagne du GRU (unité 26165/APT28) ciblant les entités logistiques occidentales et les entreprises technologiques impliquées dans la livraison d'aide à l'Ukraine. La campagne utilisait un mix de TTPs connus — password spraying, spearphishing, modification de permissions Exchange — et ciblait spécifiquement les acteurs de la chaîne de transport et de coordination de l'aide. Le groupe a également ciblé des caméras de surveillance internet aux frontières ukrainiennes pour surveiller les flux d'aide.

En décembre 2023, un acteur russe a conduit une attaque destructive (wiper) contre l'opérateur télécom ukrainien Kyivstar, laissant des millions d'Ukrainiens sans internet ni service mobile pendant plusieurs jours. L'acteur avait maintenu un accès dans les systèmes de Kyivstar depuis au moins mai 2023 et a revendiqué l'attaque dans un post Telegram adressé au président Zelenskyy — illustrant la dimension psychologique de l'opération.

Le CERT-EU documente plusieurs campagnes d'espionnage cyber liées au conflit : APT29 imitant un ministère des affaires étrangères européen avec de fausses invitations à des dégustations de vin pour installer une backdoor modulaire furtive, et le groupe DoNot ciblant des entités diplomatiques d'Europe du Sud en se faisant passer pour des diplomates.

### 7.3 — L'évolution des TTPs : adoption d'outils commodity

Un phénomène notable documenté par l'ANSSI est l'adoption croissante d'outils cybercriminels « commodity » par les acteurs étatiques russes. Historiquement, les groupes APT russes développaient des outils propriétaires sophistiqués (Fancy Bear's X-Agent, Turla's Snake). Aujourd'hui, ils utilisent de plus en plus des outils disponibles publiquement ou dans l'écosystème cybercriminel — Cobalt Strike, Brute Ratel, outils de tunnelling légitimes — rendant l'attribution plus difficile.

Les campagnes d'APT28 « semblent répondre à des besoins de renseignement stratégique immédiat et présentent des niveaux de sophistication variables », note l'ANSSI. Certaines campagnes reposent sur des comptes légitimes compromis, des services de création d'adresses de messagerie temporaires, ou de l'usurpation d'adresses légitimes. D'autres utilisent l'exploitation de vulnérabilités, y compris zero-day. Cette variabilité suggère que les opérateurs adapte leur effort au niveau de valeur de la cible.

### 7.4 — Le ciblage de l'Europe : du diplomatique au destructif

L'année 2025 marque un escalade avec les attaques destructives contre les infrastructures électriques polonaises — première attaque de ce type contre un État membre de l'UE. L'ANSSI note que cet événement « illustre concrètement le scénario auquel la France se prépare : une augmentation massive — d'ici 2030 — des attaques dites hybrides, dont les cyberattaques constituent un pan majeur, avec des effets concrets voire destructeurs sur nos infrastructures critiques ».

Le ciblage européen s'étend aux processus électoraux. Les élections dans plusieurs pays européens fin 2024 et courant 2025 ont constitué des opportunités d'attaques cyber ou d'influence. VIGINUM a documenté des manipulations de l'information ciblant l'élection présidentielle roumaine de 2024, où des modes opératoires informationnels ont artificiellement promu des contenus sur TikTok. Des DDoS hacktivistes pro-russes ont ciblé les sites de partis politiques danois le jour des élections en novembre 2025.

### 7.5 — La convergence état-cybercrime : NailoLocker et le brouillage des frontières

L'un des cas les plus révélateurs de la convergence étatique-criminelle est documenté par Orange CyberDefense, Fortinet et Trendmicro : la distribution du ransomware NailoLocker en Europe via les backdoors ShadowPad et PlugX — des outils historiquement associés à l'espionnage chinois, mais dans un contexte d'opération où les éléments d'attribution sont ambigus.

L'ANSSI documente un phénomène similaire côté russe : des outils d'espionnage étatiques utilisés en conjonction avec du ransomware, et des acteurs de cyberespionnage qui « adoptent des pratiques qui caractérisaient jusqu'à présent davantage » les cybercriminels. Le groupe ChamelGang illustre cette convergence — documenté par SentinelOne comme un groupe d'espionnage ciblant les infrastructures critiques avec du ransomware.

Les motivations possibles de cette convergence sont multiples : utiliser le ransomware comme couverture pour des opérations d'espionnage (le bruit du ransomware masque l'exfiltration), générer des revenus complémentaires, créer de la confusion pour compliquer l'attribution, ou combiner déstabilisation et gain financier.

### 7.6 — L'instrumentalisation des hacktivistes

La Russie a développé un modèle sophistiqué d'instrumentalisation des hacktivistes. Le groupe **Cyber Army of Russia Reborn (CARR)** est le cas le plus documenté : précédemment lié à Sandworm (GRU), CARR se présente comme un groupe hacktiviste indépendant mais ses opérations semblent coordonnées avec les objectifs militaires russes. Le département du Trésor américain a sanctionné des membres de CARR en juillet 2024.

**NoName057(16)** est le groupe hacktiviste pro-russe le plus actif contre l'UE, représentant 66,7% des attaques hacktivistes ciblant les administrations publiques européennes selon l'ENISA. Le groupe opère la plateforme DDoSia, qui permet à des volontaires de contribuer leur bande passante aux attaques DDoS. Si le lien direct avec l'État russe n'est pas publiquement établi, le timing des attaques — systématiquement aligné sur les événements géopolitiques favorables aux intérêts russes — suggère au minimum une coordination tacite.

### 7.7 — Les opérations d'influence

La Russie « voit presque certainement son programme cyber comme partie d'une stratégie multi-couches pour influencer et façonner l'environnement informationnel », évalue le CSE canadien. Les opérations combinent espionnage cyber (vol de documents), manipulation de l'information (diffusion de documents volés, création de faux récits) et amplification (bots, trolls, faux sites d'information).

Microsoft documente l'émergence d'acteurs « AI-first » russes qui privilégient les contenus générés par IA sur les méthodes traditionnelles, « inondant l'espace informationnel de médias synthétiques pour désensibiliser les audiences et épuiser les systèmes de détection ». L'utilisation de l'IA pour créer des répliques numériques de présentateurs de journaux télévisés (AI twinning) qui diffusent des narratifs pro-russes avec un vernis de crédibilité est documentée comme une technique émergente.

### 7.8 — 🔴 Fil rouge : campagne de phishing ciblant les contrats OTAN

> **📌 FIL ROUGE — Épisode 7**
>
> En avril 2025, le département « contrats OTAN » d'EuroDefense reçoit une série d'emails contenant des fichiers .rdp (Remote Desktop Protocol) malveillants. Les emails se présentent comme des documents de travail d'un fabricant de défense européen partenaire. Le CERT-EU a publié une alerte quelques semaines plus tôt sur exactement ce type de campagne, attribuée à un acteur Russia-nexus : des fichiers RDP malveillants usurpant l'identité d'un fabricant de défense d'un État membre.
>
> Sophie corrèle immédiatement : le vecteur (fichiers RDP), le lure (secteur défense), le timing (période de renouvellement de contrats OTAN) et l'alerte CERT-EU pointent vers un acteur Russia-nexus, probablement APT28 ou un groupe affilié. Elle attribue avec une confiance modérée (B2) à un intrusion set Russia-nexus et recommande : blocage immédiat des fichiers .rdp en pièce jointe, analyse des connexions RDP sortantes des dernières 48 heures, sensibilisation ciblée du département contrats OTAN, et notification au CERT-EU.

---

## Chapitre 8 — Iran, Corée du Nord et acteurs émergents

### 8.1 — L'Iran : APT42, MuddyWater, Cyber Av3ngers

Le programme cyber iranien est plus ciblé et moins scalable que les programmes chinois et russe, mais il possède des capacités significatives, particulièrement en matière de surveillance d'individus et d'opérations de rétorsion.

**APT42** est le groupe d'espionnage le plus actif, ciblant les think tanks, les organismes de recherche, les universités et les individus perçus comme des menaces pour le régime iranien — chercheurs, journalistes, dissidents, membres de la diaspora iranienne. L'ANSSI note que depuis fin 2023, les opérations d'APT42 contre les ONG, centres de recherche et universités semblent représenter une part croissante de ses activités. Microsoft a observé cette activité ciblant des entités en Belgique, France, à Gaza, en Israël, au Royaume-Uni et aux États-Unis.

**MuddyWater** cible des secteurs plus diversifiés, incluant le secteur financier mondial. Le CERT-EU documente une campagne de MuddyWater ciblant des cadres financiers, y compris en Europe.

**Cyber Av3ngers**, affiliés aux Gardiens de la révolution, ont ciblé des systèmes OT dans le secteur de l'eau, exploitant des contrôleurs Unitronics PLC pour accéder à des systèmes de traitement d'eau et d'eaux usées. Ce ciblage OT par un acteur étatique iranien représente une escalade significative par rapport aux opérations d'espionnage traditionnelles.

Le conflit Israël-Hamas a intensifié l'activité cyber iranienne, avec un triplement des cyberattaques attribuées à l'Iran et au Hezbollah selon les autorités israéliennes. L'Iran utilise le cyber comme outil de rétorsion asymétrique — frapper des cibles civiles et économiques en réponse à des actions militaires conventionnelles.

### 8.2 — La Corée du Nord : financement du régime par la cybercriminalité

La RPDC est unique dans le paysage étatique parce que la cybercriminalité est un **outil central de financement du régime**, pas un effet secondaire. Sous sanctions internationales, la RPDC utilise le vol de cryptomonnaies, le ransomware et la fraude pour générer des revenus estimés à plusieurs milliards de dollars.

**Lazarus** (et ses sous-groupes) est l'acteur le plus documenté. Ses opérations incluent le vol massif de cryptomonnaies (les vols attribués à Lazarus représentent certaines des plus grosses pertes individuelles de l'histoire de la crypto), le ransomware ciblant les hôpitaux et les fournisseurs de soins de santé, et les campagnes d'espionnage technologique visant le secteur de la défense.

Le CERT-EU documente en octobre 2025 une campagne de Lazarus utilisant des lures d'offres d'emploi pour cibler des entreprises européennes de défense privées et publiques, en particulier les entités impliquées dans les véhicules aériens sans pilote (UAV). Ce type de ciblage combine l'ingénierie sociale (offres d'emploi attractives) avec l'espionnage technologique (vol de données sur les systèmes d'armement).

### 8.3 — Le phénomène des faux employés IT nord-coréens

Une technique distinctive de la RPDC, documentée par Microsoft et le FBI, est l'infiltration d'entreprises technologiques occidentales par de faux employés IT utilisant des identités synthétiques. Ces opérateurs nord-coréens postulent à des postes de développeurs en télétravail, utilisent des identités volées ou fabriquées, et une fois embauchés, génèrent des revenus pour le régime tout en ayant potentiellement accès à des systèmes sensibles.

La sophistication de ces opérations est croissante : les faux employés utilisent des deepfakes en temps réel pour les entretiens vidéo, des documents d'identité générés par IA (le service OnlyFake permet de créer des faux documents d'identité réalistes), et des réseaux de facilitateurs dans les pays occidentaux qui reçoivent le matériel informatique et fournissent les adresses locales.

### 8.4 — Acteurs émergents : Inde et mercenaires cyber

L'ENISA ETL 2025 documente une observation notable : l'émergence d'activités d'intrusion attribuées à des ensembles d'intrusion **India-nexus** (4% des activités étatiques contre l'UE). Les groupes Sidewinder et DoNot ont été observés ciblant des entités diplomatiques d'Europe du Sud. Bien que représentant une part faible du total, cette émergence est significative parce qu'elle diversifie le paysage d'acteurs étatiques au-delà du quadrilatère traditionnel (Chine, Russie, Iran, RPDC).

Les **mercenaires cyber** (PSOA) constituent une catégorie transversale. Le marché du spyware commercial est dominé par quelques acteurs — NSO Group (Pegasus), Candiru, Paragon — qui vendent des capacités d'intrusion sophistiquées (exploitation de zero-day, compromission de smartphones) à des clients gouvernementaux. Google TAG documente l'existence d'un marché plus large incluant des entreprises moins connues. Ce marché pose des risques spécifiques pour les institutions européennes, les journalistes, les défenseurs des droits humains et les opposants politiques.

### 8.5 — La menace insider à l'ère de la compétition géopolitique

Microsoft consacre dans son MDDR 2025 une analyse substantielle aux menaces internes dans le contexte de la compétition géopolitique. Les États-nations « ont accru leur utilisation d'insiders pour accéder au renseignement », souvent via des opérations à long terme utilisant des affiliations académiques ou professionnelles comme couverture.

Les secteurs les plus exposés — IA, technologies quantiques, biotechnologie, défense — ont à la fois une valeur économique et militaire. L'espionnage par insider peut causer des pertes financières immédiates et un préjudice compétitif à long terme, « effaçant des années d'innovation et d'avantage marché par le vol de R&D ».

Le délai moyen de confinement d'un incident insider est de **81 jours** (données Ponemon/DTEX) — un dwell time considérable qui donne aux acteurs étatiques un point d'appui persistant pour étendre leur accès, couvrir leurs traces et établir des backdoors pour un usage futur.

Les cadres de sécurité traditionnels n'ont pas été conçus pour la menace insider. Les outils de DLP détectent les transferts massifs de fichiers mais manquent l'exfiltration lente et furtive d'un insider espion. L'architecture zero trust ajoute de la protection mais nécessite une opérationnalisation cohérente pour prévenir l'utilisation non autorisée de comptes légitimes. Les licenciements et restructurations exacerbent le risque en créant des employés mécontents et en affaiblissant la supervision.

### 8.6 — 🔴 Fil rouge : alerte Lazarus sur les ingénieurs UAV

> **📌 FIL ROUGE — Épisode 8**
>
> En mai 2025, le CERT-EU diffuse une alerte TLP:AMBER signalant une campagne de Lazarus ciblant les entreprises européennes de défense via de fausses offres d'emploi sur LinkedIn, avec un focus sur les ingénieurs UAV. La branche spatial/drones d'EuroDefense emploie exactement ce profil.
>
> Sophie active immédiatement le protocole insider. Elle demande à l'équipe RH de vérifier les candidatures récentes pour les postes d'ingénieurs UAV et de drones. Parallèlement, elle sensibilise les managers de la branche spatial aux techniques de social engineering via offres d'emploi. Elle fait ajouter des indicateurs techniques (domaines, hashes) issus de l'alerte CERT-EU aux règles de détection du SOC.
>
> Un cas remonte rapidement : un ingénieur a reçu une offre LinkedIn apparemment légitime d'un recruteur d'une entreprise aérospatiale asiatique. Le profil LinkedIn du recruteur a été créé il y a trois mois, a peu de connexions, et la description de l'offre contient un lien vers un « test technique » à télécharger. L'ingénieur n'a pas cliqué, mais Sophie note que la campagne est active et que la branche spatial d'EuroDefense est bien dans le scope.

---

## Chapitre 9 — Ciblage sectoriel par les acteurs étatiques : analyse comparée

### 9.1 — Administrations publiques et diplomatie

L'ENISA ETL 2025 identifie l'administration publique comme le secteur le plus ciblé de l'UE avec 38,2% des incidents documentés — une augmentation substantielle par rapport à la période précédente, principalement due aux attaques DDoS hacktivistes. Le ciblage hacktiviste (96,2% du total pour ce secteur) est contextualisé par les événements géopolitiques : soutien à l'Ukraine, arrestations de cybercriminels, élections, sommets OTAN.

Au-delà du DDoS, le secteur public est la cible première de l'espionnage étatique. Le CERT-EU documente que le cyberespionnage et le prépositionnement représentent 38% des MAI totales dans son dataset, avec la défense comme secteur le plus ciblé et la diplomatie en deuxième position. Les campagnes d'APT29 imitant des invitations diplomatiques et le ciblage de ministères des affaires étrangères illustrent la persistance de cette menace.

### 9.2 — Défense et recherche

Le secteur de la défense est une cible permanente de l'espionnage étatique. L'ANSSI note que « le secteur de la défense a fait l'objet en 2025 d'actions de reconnaissance, de tentatives de compromissions et de compromissions par des modes opératoires réputés étatiques à des fins d'espionnage stratégique et de renseignement ». Le ciblage est conduit par les principaux acteurs étatiques (Chine, Russie, RPDC) et porte sur la propriété intellectuelle militaire, les données contractuelles, les capacités technologiques et les informations stratégiques.

Les universités et centres de recherche constituent une extension du ciblage défense — les résultats de la recherche fondamentale alimentant les programmes militaires. L'ANSSI et Microsoft documentent un ciblage persistant de ce secteur, notamment par des acteurs iraniens (APT42) et chinois.

### 9.3 — Infrastructures numériques et télécommunications

L'ENISA classe les infrastructures numériques et services comme le troisième secteur le plus ciblé (4,8% des incidents). Ce secteur a un **effet multiplicateur** : compromettre un fournisseur de services numériques permet d'accéder aux données de tous ses clients.

Le ciblage des télécommunications est traité en détail au Ch.6.5. L'ASD et les partenaires Five Eyes ont publié un advisory conjoint sur la compromission des réseaux d'opérateurs télécom par des acteurs PRC, accompagné de recommandations de durcissement pour les ingénieurs réseau et les défenseurs.

### 9.4 — Transport et logistique

Le transport est le deuxième secteur le plus ciblé dans l'UE (7,5% des incidents ETL 2025). Le ciblage russe de la logistique de livraison d'aide à l'Ukraine (documenté par l'ASD en mai 2025) illustre comment les intérêts militaires drives le ciblage sectoriel. Le ciblage chinois du transport maritime est lié aux intérêts stratégiques Belt and Road.

### 9.5 — Secteur spatial

Le Space Threat Landscape 2025 de l'ENISA est la première évaluation systématique des menaces cyber pesant sur les systèmes satellitaires. Le secteur spatial est désormais inclus dans NIS2 comme secteur de haute criticité, imposant des obligations de cybersécurité aux opérateurs de satellites et d'infrastructures sol.

Les menaces identifiées couvrent l'ensemble du cycle de vie des satellites : compromission des centres de contrôle au sol, injection de code malveillant dans les logiciels embarqués (OBC/OBSW), exploitation de vulnérabilités dans les protocoles de communication satellite, interception des liaisons TM/TC (télémétrie/télécommande), et compromission de la supply chain des composants COTS. Le détail est traité au Chapitre 19.

### 9.6 — Finance

Le secteur financier (4,5% des incidents ETL 2025) est ciblé à la fois par l'espionnage étatique (ciblage des systèmes de paiement, surveillance des flux financiers) et par la cybercriminalité (ransomware, fraude). Le CERT-EU note que le secteur financier a vu une augmentation des MAI en 2025, avec le cybercrime comme menace principale suivie du cyberespionnage. Le règlement DORA impose au secteur financier des exigences spécifiques de résilience opérationnelle numérique.

### 9.7 — Santé, énergie, industrie manufacturière

Le secteur de la **santé** est la cible la plus documentée du ransomware dans les données FBI IC3, avec 460 incidents ransomware et 355 incidents data breach signalés pour les infrastructures critiques healthcare/public health en 2025. Le ciblage de la santé est particulièrement problématique parce qu'il peut avoir des conséquences directes sur la vie des patients.

Le secteur de l'**énergie** est ciblé pour le prépositionnement (Volt Typhoon), le sabotage (cas polonais 2025) et le hacktivisme OT (Z-PENTEST-ALLIANCE). L'**industrie manufacturière** est le secteur le plus touché par les revendications ransomware en UE (14,9% des claims selon l'ENISA).

### 9.8 — Analyse croisée multi-sources

Le croisement des données de sources différentes révèle des convergences et des divergences instructives. Tous les rapports s'accordent sur la prééminence du ransomware comme menace cybercriminelle, sur l'intensification de l'espionnage étatique chinois, et sur la persistance de la menace russe amplifiée par le conflit ukrainien. Les divergences portent principalement sur les proportions (le poids relatif de chaque secteur varie selon la perspective géographique) et sur les menaces émergentes (la menace quantique, par exemple, est traitée très différemment selon les sources).

### 9.9 — 🔴 Fil rouge : matrice de risque sectorielle

> **📌 FIL ROUGE — Épisode 9**
>
> Sophie produit la matrice de risque sectorielle d'EuroDefense en croisant les PIR avec les données du corpus. Le résultat identifie quatre zones rouges : espionnage étatique (Chine/Russie) sur la branche défense et les contrats OTAN, ransomware sur la supply chain IT, menace RPDC sur la branche spatial/UAV, et prépositionnement potentiel sur les réseaux OT industriels. Elle identifie aussi une zone orange négligée : le risque de campagne d'influence ciblée visant les contrats OTAN/ESA — un scénario hybride qui n'est pas couvert par le CERT mais par la communication du groupe.

> **🎯 CAPSTONE Partie II** : Rédiger un briefing exécutif (2 pages) attribuant un intrusion set observé sur un réseau industriel européen à un nexus étatique. Le briefing doit expliciter : les éléments techniques, comportementaux et contextuels soutenant l'attribution ; le niveau de confiance (Admiralty + LCA) ; les hypothèses alternatives ; les limites de l'attribution ; et les recommandations immédiates.

---
