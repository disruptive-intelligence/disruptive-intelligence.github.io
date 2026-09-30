---
title: Chapitre 1 — Introduction
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
up:
- - État de l'art — panorama de la cybermenace
  - ../index.md
- - PARTIE I — Fondations
  - index.md
---

pourquoi un panorama stratégique de la cybermenace ?

## 1.1 — Le contexte 2025-2026

un niveau de menace systémique, durable et en mutation

L'année 2025 s'est achevée sur un événement qui devrait collectivement alarmer l'ensemble des professionnels de la cybersécurité : une série d'attaques informatiques coordonnées à visée destructive contre les infrastructures électriques polonaises. Il s'agit d'une première pour un État membre de l'Union européenne — un seuil franchi qui matérialise concrètement le scénario auquel les démocraties occidentales se préparent depuis une décennie. L'objectif était clair : provoquer des coupures d'électricité et de chauffage pour un nombre conséquent de citoyens. Si le pire semble avoir été évité, cet événement illustre la trajectoire dans laquelle la cybermenace mondiale s'inscrit désormais.

Le panorama de la cybermenace en 2025-2026 ne se résume pas à un catalogue d'incidents. Il révèle un **système de menace** structurel, dont les caractéristiques fondamentales méritent d'être comprises avant d'entrer dans le détail technique.

**Première caractéristique : la menace est systémique.** Elle ne touche plus uniquement les grandes entreprises ou les administrations centrales. L'ANSSI constate que la menace cyber « n'épargne personne » et qu'elle « est devenue systémique, touchant l'ensemble du tissu économique et social ». Les données du FBI IC3 confirment cette tendance à l'échelle mondiale, avec plus de 20 milliards de dollars de pertes déclarées en 2025 — un chiffre qui ne représente qu'une fraction de la réalité, tant le sous-signalement reste structurel.

**Deuxième caractéristique : les frontières entre acteurs s'érodent.** Le phénomène le plus structurant de la période est sans doute l'effacement progressif des frontières qui séparaient traditionnellement les acteurs étatiques des cybercriminels. L'ANSSI parle d'un « brouillard technologique et organisationnel » résultant d'un « partage de capacités plus prononcé entre ces acteurs » et de « l'adoption croisée de pratiques ». Europol, dans sa SOCTA 2025, documente ce phénomène sous l'angle de la criminalité organisée, montrant comment les réseaux criminels servent les objectifs d'acteurs étatiques hybrides — et réciproquement. Cette convergence complique fondamentalement l'attribution, la défense et la réponse.

**Troisième caractéristique : la menace se déplace vers l'infrastructure.** Les attaquants ciblent de moins en moins les utilisateurs finaux par le phishing classique et de plus en plus les équipements d'infrastructure — VPN, firewalls, passerelles réseau, équipements de bordure. L'ANSSI note que plus de la moitié de ses opérations de cyberdéfense en 2024 ont eu pour origine l'exploitation de vulnérabilités sur ces équipements, en 2025, les équipements de bordure restent des cibles privilégiées. Ce pivot est stratégique : il permet un accès silencieux, persistant, et souvent indétectable par les solutions de sécurité classiques.

**Quatrième caractéristique : l'intelligence artificielle amplifie les deux côtés.** L'IA n'est plus un facteur théorique. Elle est désormais utilisée opérationnellement tant par les attaquants (phishing personnalisé, deepfakes, automatisation de la reconnaissance) que par les défenseurs (détection augmentée, automatisation du SOC, analyse comportementale). Microsoft documente dans son Digital Defense Report 2025 une croissance significative des contenus générés par IA dans les opérations d'influence étatiques — une tendance qui s'accélère.

**Cinquième caractéristique : la réponse s'organise, mais reste fragmentée.** L'écosystème réglementaire s'est considérablement renforcé avec la transposition de NIS2, l'entrée en vigueur du Cyber Resilience Act, et DORA pour le secteur financier. Les opérations de disruption contre les groupes cybercriminels (Endgame, LockBit takedown, démantèlement LummaC2) ont produit des résultats tangibles. Mais la fragmentation réglementaire entre juridictions, la résilience structurelle de l'écosystème cybercriminel, et l'existence de « safe haven states » limitent l'impact durable de ces avancées.

Ce cours a pour ambition de fournir au praticien une **compréhension structurée, analytique et opérationnelle** de ce système de menace. Il ne s'agit ni d'un catalogue d'incidents, ni d'un résumé de rapports, mais d'une synthèse qui relie les dimensions stratégique, analytique, opérationnelle et décisionnelle de la cybermenace contemporaine.

## 1.2 — Définition et périmètre d'un Cyber Threat Landscape (CTL) : ce que c'est, ce que ce n'est pas

Un Cyber Threat Landscape (CTL) est un produit d'intelligence qui fournit une **compréhension contextualisée des menaces passées et présentes**, permettant à son audience d'anticiper les menaces qu'elle est susceptible de rencontrer. La méthodologie ENISA 2025 le définit comme un livrable issu d'un processus intelligence-driven — c'est-à-dire structuré selon le cycle du renseignement — qui transforme des données brutes en intelligence exploitable.

Un CTL n'est pas un rapport d'incident. Il ne décrit pas un événement unique mais un **environnement de menace**. Il n'est pas non plus un catalogue d'outils ou une liste de vulnérabilités. Il articule des acteurs, des motivations, des capacités, des tendances et des impacts dans un cadre analytique cohérent, pour une audience définie et avec un périmètre explicite.

La distinction est fondamentale parce qu'elle conditionne la valeur du livrable. Un rapport d'incident informe sur ce qui s'est passé. Un CTL informe sur ce qui **pourrait** se passer, avec quel niveau de probabilité, et avec quelles implications — ce qui en fait un outil de décision, pas seulement de connaissance.

Les CTL peuvent être produits à différentes échelles : global (ENISA Threat Landscape, Microsoft Digital Defense Report), national (ANSSI Panorama de la cybermenace, ASD Annual Cyber Threat Report, CSE National Cyber Threat Assessment), sectoriel (ENISA Space Threat Landscape, CERT-EU Threat Landscape Report), ou organisationnel (CTL interne d'un CERT d'entreprise). Chaque échelle implique des choix méthodologiques différents en termes de sources, de profondeur et de format.

Le CTL peut être décliné en formats textuels (rapports PDF, briefings) ou machine-readable (feeds STIX/TAXII, indicateurs enrichis). Les deux formats sont complémentaires : le premier permet la communication stratégique et la prise de décision humaine, le second permet l'opérationnalisation automatisée dans les systèmes de détection et de défense.

> **⚠️ Piège fréquent** : confondre un CTL avec un rapport de veille. La veille est un flux continu d'informations brutes ou triées. Le CTL est un **produit analytique fini**, avec des assessments, des niveaux de confiance, et des recommandations. Produire un CTL exige un travail d'analyse qui va bien au-delà de la compilation.

## 1.3 — Pourquoi le CTL est devenu un livrable stratégique

NIS2, DORA, gouvernance cyber

Le CTL a longtemps été un produit réservé aux équipes CTI spécialisées. Trois facteurs l'ont transformé en **livrable stratégique attendu au niveau de la gouvernance**.

**Le facteur réglementaire.** La directive NIS2, dont la transposition est en cours dans les États membres, impose aux entités essentielles et importantes une approche de la cybersécurité fondée sur les risques. L'article 21 exige des mesures de gestion des risques « tenant compte de l'état de l'art » — ce qui suppose une connaissance actualisée du paysage de menace. Le règlement DORA, spécifique au secteur financier, va plus loin en exigeant des tests de résilience fondés sur des scénarios de menace crédibles. Le Cyber Resilience Act étend cette logique aux produits numériques tout au long de leur cycle de vie. Dans ce cadre réglementaire, le CTL passe du « nice to have » au « requis pour la conformité ».

**Le facteur de gouvernance.** Les conseils d'administration et les comités exécutifs sont de plus en plus tenus responsables de la posture de cybersécurité de leur organisation. Les normes de gouvernance (ISO 27001:2022, NIST CSF 2.0) intègrent désormais explicitement l'analyse de la menace comme input de la gestion des risques. Le CTL devient l'outil qui permet au RSSI de traduire l'intelligence technique en langage de décision business.

**Le facteur opérationnel.** Les équipes de détection et de réponse ont besoin de prioriser. Face à un flux continu d'alertes, de vulnérabilités et de rapports, le CTL fournit le cadre de priorisation fondé sur la menace réelle — pas sur la menace théorique. L'approche « threat-informed defense » — défendre en fonction de ce que les attaquants font réellement, pas de ce qu'ils pourraient théoriquement faire — repose entièrement sur un CTL de qualité.

## 1.4 — Les producteurs de threat landscape

cartographie des publications mondiales

Le paysage de la cybermenace est documenté par un écosystème dense de producteurs institutionnels et privés. Chaque producteur apporte une perspective distincte, conditionnée par sa mission, son périmètre géographique, ses sources et ses biais de collecte. Comprendre qui produit quoi — et avec quelles limites — est un prérequis pour exploiter ces sources de manière rigoureuse.

**L'ENISA** (Agence de l'Union européenne pour la cybersécurité) publie annuellement l'ENISA Threat Landscape (ETL), le panorama de référence au niveau européen. L'ETL 2025 couvre la période juillet 2024 – juillet 2025 et documente 4 875 événements. Sa force réside dans sa couverture sectorielle structurée (alignée sur NIS2), sa rigueur méthodologique publiée, et ses données quantitatives sur les incidents EU. Son biais principal est son périmètre européen : les menaces qui ne touchent pas l'UE y sont sous-représentées. L'ENISA publie également des threat landscapes sectoriels — notamment le Space Threat Landscape 2025, premier du genre, et la méthodologie CTL (mise à jour août 2025).

**Le CERT-EU** (service de cybersécurité des institutions de l'UE) publie un Threat Landscape Report annuel centré sur les institutions, organes et agences de l'Union. Le TLR 2025 apporte une perspective unique sur le ciblage spécifique des institutions européennes. Le CERT-EU a également publié en 2025 son Cyber Threat Intelligence Framework, un document méthodologique de référence définissant les standards analytiques utilisés pour classifier, évaluer et prioriser les activités malveillantes. Ce framework sera abondamment utilisé dans ce cours.

**L'ANSSI** (Agence nationale de la sécurité des systèmes d'information, France) publie le Panorama de la cybermenace, centré sur les incidents traités ou portés à la connaissance de l'Agence. Les éditions 2024 et 2025 sont particulièrement riches en cas concrets d'incidents réels traités en France — supply chain attacks, compromissions de prestataires, exploitation d'équipements de bordure. Le Panorama ANSSI est précieux pour la profondeur des cas techniques, mais son périmètre est principalement français.

**Europol** produit deux publications complémentaires. L'IOCTA (Internet Organised Crime Threat Assessment) est centré sur la cybercriminalité, avec un focus sur l'écosystème criminel, les données volées, le ransomware et la fraude. La SOCTA (Serious and Organised Crime Threat Assessment) replace la cybercriminalité dans le contexte plus large de la criminalité organisée et des menaces hybrides. La SOCTA 2025 est particulièrement notable pour son analyse de la convergence entre réseaux criminels et acteurs étatiques hybrides.

**Le FBI/IC3** (Internet Crime Complaint Center) publie un rapport annuel apportant la perspective quantitative américaine : nombre de plaintes, pertes financières par type de crime, tendances de signalement. Le rapport IC3 2025 documente 20,877 milliards de dollars de pertes déclarées. Ces données sont précieuses mais reflètent un biais de déclaration (les victimes américaines qui choisissent de signaler).

**Le CSE/CCCS** (Centre de la sécurité des télécommunications / Centre canadien pour la cybersécurité) publie le National Cyber Threat Assessment, qui identifie les grandes tendances structurantes. L'édition 2025-2026 est remarquable pour son analyse structurée en cinq tendances (IA, évasion de détection, acteurs non-étatiques géopolitiquement inspirés, concentration des fournisseurs, services à double usage) et sa couverture détaillée de l'écosystème ransomware.

**L'ASD** (Australian Signals Directorate) publie l'Annual Cyber Threat Report avec une perspective Indo-Pacifique unique. Le rapport 2024-25 apporte des informations détaillées sur les TTPs de groupes étatiques (notamment APT40/PRC) et sur les programmes de résilience des infrastructures critiques.

**Le GCHQ/NCSC** (National Cyber Security Centre, Royaume-Uni) publie une Annual Review qui se concentre sur la construction de la résilience à grande échelle et les menaces pesant sur le Royaume-Uni.

**Microsoft** publie le Digital Defense Report (MDDR), qui apporte une perspective unique par sa télémétrie mondiale. Avec des milliards de signaux traités quotidiennement, Microsoft documente des tendances que les agences nationales ne peuvent pas observer à cette échelle — notamment sur l'utilisation de l'IA dans les opérations d'influence, la fraude à l'identité synthétique, et les techniques d'accès initial.

**INTERPOL** publie des documents stratégiques sur la lutte globale contre le cybercrime, articulant la coopération entre les 195 pays membres autour de quatre objectifs : cadres et recommandations, renseignement et analyse, coordination opérationnelle, et renforcement des capacités.

> **💡 Bonne pratique** : un CTL de qualité ne s'appuie jamais sur une source unique. Le croisement de sources ayant des biais différents (géographiques, sectoriels, méthodologiques) est le meilleur moyen de mitiger les angles morts. Un analyste CTI qui ne consulte que les rapports de son propre pays ou de son propre éditeur de sécurité produit un CTL biaisé.

## 1.5 — Architecture du cours et guide de lecture

Ce cours est structuré en sept parties suivant une progression en entonnoir : des fondations méthodologiques (comment analyse-t-on la menace ?) vers les acteurs (qui menace ?), l'écosystème criminel (comment fonctionne l'industrie du cybercrime ?), les surfaces et vecteurs (où et comment les attaques se produisent-elles ?), les cadres de réponse (comment se défend-on et qui coordonne ?), la prospective et la mise en pratique (comment anticiper et produire un CTL ?), et enfin les cas de synthèse intégrant l'ensemble.

Chaque partie se termine par un **capstone** — un exercice de synthèse qui intègre les concepts des chapitres précédents dans un livrable opérationnel. Chaque chapitre contient un épisode du fil rouge, qui illustre les concepts dans un contexte professionnel réaliste.

Le cours est conçu pour être lu séquentiellement, mais chaque partie est suffisamment autonome pour servir de référence indépendante. Les renvois croisés entre chapitres sont explicites et systématiques.

## 1.6 — 🔴 Fil rouge : Sophie prend ses fonctions

> **📌 FIL ROUGE — Épisode 1**
>
> Sophie Renard, 34 ans, rejoint le CERT d'EuroDefense Industries le 6 janvier 2025 comme analyste CTI senior. Son parcours : cinq ans au CERT-FR (ANSSI), deux ans chez un éditeur de CTI privé. EuroDefense est un groupe industriel européen — aéronautique, défense, spatial — classé entité essentielle sous NIS2. Le groupe opère dans 14 pays, fournit des systèmes critiques à l'OTAN et à l'ESA, et gère une supply chain logicielle et matérielle complexe impliquant plus de 200 sous-traitants.
>
> Le RSSI, Marc Vidal, la convoque dès le premier jour. La mission est claire : « On n'a jamais produit de CTL structuré. Le COMEX veut savoir ce qui nous menace réellement, et l'audit NIS2 arrive dans neuf mois. J'ai besoin d'un threat landscape sectoriel complet, et de quelqu'un capable de transformer ce CERT réactif en capacité d'anticipation. »
>
> Sophie commence par un inventaire : quelles sources sont disponibles ? Le CERT reçoit les flux CERT-FR et CERT-EU, a un abonnement Recorded Future, et monitore une dizaine de feeds OSINT. Aucune méthodologie formalisée, aucun framework d'analyse structuré, aucun template de livrable. Tout est à construire.
>
> Elle note ses premières questions : quel périmètre pour le CTL (groupe entier ? France uniquement ? avec ou sans les filiales asiatiques ?) ? Quelle audience (COMEX ? équipes SOC ? responsables OT ?) ? Quel niveau de classification ? Et surtout : par quoi commencer ?

---
