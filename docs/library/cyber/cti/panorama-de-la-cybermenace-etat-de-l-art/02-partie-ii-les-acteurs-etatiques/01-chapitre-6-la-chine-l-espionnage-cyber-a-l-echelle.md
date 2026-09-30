---
title: 'Chapitre 6 — La Chine : l''espionnage cyber à l''échelle globale'
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: Panorama de la cybermenace — état de l'art
up:
- - Panorama de la cybermenace — état de l'art
  - ../index.md
- - PARTIE II — Les acteurs étatiques
  - index.md
---

## 6.1 — Architecture du programme cyber chinois

Le programme cyber offensif chinois se distingue des autres par son **échelle, son ambition et sa profondeur organisationnelle**. Microsoft note dans son Digital Defense Report 2025 que « l'ampleur et l'échelle des opérations de ciblage chinoises continuent de se démarquer des autres acteurs étatiques ». Le CSE canadien est plus direct : « Parmi nos adversaires, l'échelle, le tradecraft et les ambitions du programme cyber de la RPC dans le cyberespace sont sans égal. »

L'architecture institutionnelle repose sur plusieurs piliers. Le **Ministry of State Security (MSS)** — l'agence de renseignement civil — est le principal commanditaire d'opérations de cyberespionnage. Le MSS délègue une partie de ses opérations à des entreprises privées de cybersécurité et à des « quartiers-maîtres numériques » (digital quartermasters) qui fournissent infrastructure, malware et expertise. La fuite des documents d'i-SOON en février 2024 a révélé l'ampleur de cet écosystème de sous-traitants : contrats de piratage à la demande, développement de malware sur mesure, et opérations d'intrusion ciblant des gouvernements, des entreprises et des individus dans le monde entier.

Le **People's Liberation Army (PLA)** opère ses propres unités cyber, principalement pour le renseignement militaire. L'**APT40** (également suivi comme Kryptonite Panda, Gingham Typhoon, Leviathan) est associé au MSS et cible la région Indo-Pacifique, avec un focus sur les secteurs gouvernemental, technologique et maritime.

Cette architecture de sous-traitance confère au programme chinois plusieurs avantages : la scalabilité (un réservoir de compétences extensible), la dénéabilité (les opérations sont conduites par des entités privées, pas directement par l'État), et la spécialisation (chaque sous-traitant développe une expertise sur des cibles ou des techniques spécifiques).

## 6.2 — Objectifs stratégiques

Les objectifs du programme cyber chinois s'articulent autour de quatre axes documentés par l'ensemble des sources du corpus.

Le **vol de propriété intellectuelle et l'avantage économique compétitif** reste le driver principal. Microsoft note que « la Chine utilise les opérations d'espionnage comme méthode clé pour poursuivre un avantage économique compétitif ». Les secteurs ciblés — IT, industrie manufacturière, recherche, biotechnologie — sont alignés avec les priorités du plan « Made in China 2025 » et des stratégies industrielles chinoises.

Le **remodelage de l'ordre international** est un objectif de plus en plus documenté. Microsoft observe que « à travers des campagnes coordonnées d'opérations d'influence et des intrusions cyber, la Chine cherche à affaiblir les institutions démocratiques, à semer la discorde entre alliés et à promouvoir des narratifs qui légitiment son modèle de gouvernance ». L'année 2024, qui comptait un nombre record d'élections dans le monde, a vu un investissement significatif dans la collecte de renseignement électoral et les tentatives d'influence.

La **répression transnationale** utilise le cyber pour surveiller et harceler les dissidents, les minorités (Ouïghours, Tibétains) et les critiques du Parti communiste chinois à l'étranger. Un acte d'accusation américain de 2024 documente le ciblage de membres de l'Inter-Parliamentary Alliance on China (IPAC), un groupe de parlementaires de plusieurs pays dont des Canadiens.

Le **prépositionnement** dans les infrastructures critiques occidentales — l'axe le plus préoccupant — est traité en détail dans la sous-section 6.4.

## 6.3 — Panorama des ensembles d'intrusion actifs

Le paysage des ensembles d'intrusion chinois est vaste. Les plus documentés sur la période 2024-2025 incluent :

**Volt Typhoon** se distingue par son focus exclusif sur le prépositionnement dans les infrastructures critiques américaines (énergie, transport, communications, eau). Ses TTPs sont caractérisées par l'utilisation intensive de techniques living-off-the-land (LotL) — utilisant uniquement les outils natifs des systèmes compromis — ce qui le rend extrêmement difficile à détecter. Volt Typhoon n'exfiltre pas de données et ne déploie pas de malware classique : il installe et maintient des accès dormants.

**Salt Typhoon** cible les infrastructures de télécommunications mondiales. Aux États-Unis, le groupe a été associé à la compromission d'opérateurs majeurs et au ciblage des dispositifs d'interception légale (lawful intercept) — c'est-à-dire les systèmes utilisés par les forces de l'ordre pour les écoutes autorisées par la justice. L'ANSSI note que le secteur des télécommunications est « ciblé de façon régulière et importante par les groupes d'attaquants réputés liés à la Chine ».

**Mustang Panda** cible principalement les gouvernements, les organisations internationales et les secteurs diplomatiques en Asie et en Europe. Il a été observé ciblant le secteur du transport maritime européen, avec des implants malveillants retrouvés sur des équipements embarqués.

**APT41** est un cas hybride unique : documenté par Mandiant comme un acteur menant simultanément des opérations d'espionnage étatique et de cybercriminalité à but lucratif. Cette dualité illustre la porosité entre les catégories d'acteurs dans l'écosystème chinois.

**APT40/Kryptonite Panda** se caractérise par l'exploitation rapide de vulnérabilités, souvent dans les heures ou jours suivant la publication des preuves de concept. L'ASD australien a publié un advisory détaillé sur les TTPs d'APT40 en 2024, documentant sa préférence pour l'exploitation des applications exposées à internet plutôt que le phishing.

## 6.4 — Le prépositionnement dans les infrastructures critiques

Le cas Volt Typhoon mérite un traitement approfondi parce qu'il représente un changement qualitatif dans la menace étatique. Il ne s'agit plus d'espionnage (voler de l'information) mais de **prépositionnement** (installer des accès pour une utilisation future potentiellement destructive).

Les implications stratégiques sont majeures. Si Volt Typhoon maintient des accès dans les réseaux d'énergie, de transport et de communication américains, ces accès pourraient théoriquement être activés en cas de crise — par exemple, un conflit dans le détroit de Taïwan — pour perturber la capacité de projection militaire américaine. C'est un scénario de « pré-positionnement pour le sabotage » qui dépasse le cadre traditionnel du cyberespionnage.

Les TTPs de Volt Typhoon sont spécifiquement conçues pour la persistance à long terme et l'évasion de détection : utilisation exclusive d'outils natifs du système (PowerShell, WMI, certutil), compromission de routeurs SOHO pour créer des réseaux de relais, absence de malware personnalisé déployé sur les systèmes cibles. Ces caractéristiques rendent la détection par les solutions de sécurité classiques (signatures, heuristiques) pratiquement impossible.

Le CSE canadien évalue que le Canada est également une cible potentielle de ce type de prépositionnement, « étant donné sa proximité géographique et l'interconnexion de ses infrastructures avec celles des États-Unis ». L'ANSSI observe des activités similaires ciblant l'Europe, notant que « les objectifs inconnus [des prépositionnements] doivent collectivement nous alarmer ».

## 6.5 — Le ciblage des télécommunications

Le ciblage des opérateurs de télécommunications est une constante du programme chinois, pour des raisons structurelles : les réseaux télécom transportent les communications de toutes les cibles d'intérêt (gouvernements, militaires, entreprises, individus). Compromettre un opérateur, c'est potentiellement accéder aux communications de tous ses clients.

L'ANSSI a traité en 2024-2025 des « compromissions importantes de SI d'opérateurs [de télécommunications] à des fins d'espionnage, menées par des MOA ayant développé des techniques et outils avancés spécifiques à ce domaine ». En décembre 2024, l'ASD australien s'est joint à des partenaires internationaux pour publier un advisory alertant sur la compromission de réseaux d'opérateurs télécom majeurs dans le cadre d'une campagne de cyberespionnage PRC.

Le cas Salt Typhoon est particulièrement préoccupant parce qu'il cible les dispositifs d'interception légale — les systèmes conçus pour permettre aux forces de l'ordre d'écouter les communications sous mandat judiciaire. La compromission de ces systèmes donne aux attaquants accès non seulement aux communications en cours d'écoute, mais potentiellement à l'infrastructure d'interception elle-même.

## 6.6 — Tactiques et techniques distinctives

Plusieurs caractéristiques techniques distinguent les opérations chinoises.

La **rapidité d'opérationnalisation des vulnérabilités** est une capacité distinctive documentée par l'ASD et Microsoft. APT40 est connu pour exploiter les vulnérabilités dans les heures suivant la publication des preuves de concept — un tempo qui dépasse les capacités de patching de la plupart des organisations.

L'utilisation de **réseaux de relais SOHO** (Small Office Home Office) permet aux acteurs chinois de mêler leur trafic malveillant au trafic légitime des propriétaires des équipements compromis, compliquant significativement la détection.

L'exploitation des **équipements de bordure** (VPN, firewalls, passerelles) est une préférence tactique qui reflète le fait que ces équipements sont souvent moins supervisés et moins protégés que les serveurs internes, tout en offrant un point d'entrée directement dans le réseau de la cible.

## 6.7 — Lawfare cyber : le cadre juridique chinois comme facilitateur

Un aspect spécifique de la menace chinoise, documenté par l'ANSSI, est l'utilisation du cadre juridique chinois comme outil d'espionnage. Des logiciels imposés par les autorités chinoises aux entreprises étrangères opérant en Chine peuvent comporter des fonctionnalités malveillantes intégrées par leurs éditeurs, ou être victimes d'attaques supply chain ciblant spécifiquement les entreprises étrangères.

L'ANSSI documente le cas d'un groupe pharmaceutique français dont la filiale en Chine a été confrontée à des « pressions accompagnées de menaces » exercées par les autorités locales sur un employé « afin de contourner les politiques de sécurité informatique de l'entreprise ». L'Agence recommande d'installer ces logiciels sur des postes isolés et dédiés, et de considérer la mise en place de mesures d'isolation pour mitiger les risques de fuite de données.

## 6.8 — Victimologie croisée : données quantitatives

Le croisement des données de plusieurs sources permet de construire une image plus complète de la victimologie chinoise. Microsoft identifie les 10 secteurs les plus ciblés : IT (23%), gouvernement (10%), think tanks/ONG (9%), industrie manufacturière (9%), recherche et universités (6%), commerce de détail (6%), communications (3%), finance (3%), transport (2%), santé (2%). Géographiquement, les États-Unis représentent 35% des cibles, suivis de la Thaïlande (14%), Taïwan (12%), Corée (8%) et Japon (4%).

L'ENISA ETL 2025 documente que 24% des activités étatiques contre l'UE sont attribuées à des ensembles d'intrusion China-nexus. Le CERT-EU observe que le ciblage chinois en Europe porte principalement sur les secteurs technologique, diplomatique, de la défense et de la recherche.

## 6.9 — Limites de l'analyse

Plusieurs biais doivent être explicités. Le programme chinois est probablement le plus documenté dans les sources occidentales, ce qui pourrait créer un biais de sur-représentation. La dépendance aux rapports d'éditeurs de sécurité américains introduit un biais géographique (le ciblage des États-Unis est mieux documenté que le ciblage de l'Asie du Sud-Est). L'attribution à la Chine repose souvent sur des indicateurs techniques (malwares, infrastructure) qui sont par définition manipulables. Enfin, la catégorie « China-nexus » est large et englobe des acteurs aux motivations et aux commanditaires potentiellement différents.

## 6.10 — 🔴 Fil rouge : ciblage des filiales asiatiques

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
