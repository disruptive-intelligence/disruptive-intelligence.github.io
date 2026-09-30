---
title: Acteurs, écosystèmes, méthodes d'analyse et stratégies de résilience (2025–2026)
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
chapter: 1
chapters: 7
---

---

> **Niveau** : Expert — Professionnel — Opérationnel
>
> **Périmètre** : Analyse stratégique multi-sources du paysage mondial de la cybermenace, fondée sur les productions 2025-2026 de l'ANSSI, l'ENISA, le CERT-EU, Europol, le FBI/IC3, INTERPOL, le CSE/CCCS (Canada), l'ASD (Australie), le GCHQ/NCSC (Royaume-Uni) et Microsoft.
>
> **Public cible** : Analystes CTI, responsables CERT/CSIRT, RSSI, consultants en cybersécurité, décideurs en gouvernance cyber, auditeurs NIS2/DORA, officiers de renseignement.

---


## PARTIE I — Fondations : comprendre et analyser la cybermenace contemporaine

### Chapitre 1 — Introduction : pourquoi un panorama stratégique de la cybermenace ?

#### 1.1 — Le contexte 2025-2026 : un niveau de menace systémique, durable et en mutation

L'année 2025 s'est achevée sur un événement qui devrait collectivement alarmer l'ensemble des professionnels de la cybersécurité : une série d'attaques informatiques coordonnées à visée destructive contre les infrastructures électriques polonaises. Il s'agit d'une première pour un État membre de l'Union européenne — un seuil franchi qui matérialise concrètement le scénario auquel les démocraties occidentales se préparent depuis une décennie. L'objectif était clair : provoquer des coupures d'électricité et de chauffage pour un nombre conséquent de citoyens. Si le pire semble avoir été évité, cet événement illustre la trajectoire dans laquelle la cybermenace mondiale s'inscrit désormais.

Le panorama de la cybermenace en 2025-2026 ne se résume pas à un catalogue d'incidents. Il révèle un **système de menace** structurel, dont les caractéristiques fondamentales méritent d'être comprises avant d'entrer dans le détail technique.

**Première caractéristique : la menace est systémique.** Elle ne touche plus uniquement les grandes entreprises ou les administrations centrales. L'ANSSI constate que la menace cyber « n'épargne personne » et qu'elle « est devenue systémique, touchant l'ensemble du tissu économique et social ». Les données du FBI IC3 confirment cette tendance à l'échelle mondiale, avec plus de 20 milliards de dollars de pertes déclarées en 2025 — un chiffre qui ne représente qu'une fraction de la réalité, tant le sous-signalement reste structurel.

**Deuxième caractéristique : les frontières entre acteurs s'érodent.** Le phénomène le plus structurant de la période est sans doute l'effacement progressif des frontières qui séparaient traditionnellement les acteurs étatiques des cybercriminels. L'ANSSI parle d'un « brouillard technologique et organisationnel » résultant d'un « partage de capacités plus prononcé entre ces acteurs » et de « l'adoption croisée de pratiques ». Europol, dans sa SOCTA 2025, documente ce phénomène sous l'angle de la criminalité organisée, montrant comment les réseaux criminels servent les objectifs d'acteurs étatiques hybrides — et réciproquement. Cette convergence complique fondamentalement l'attribution, la défense et la réponse.

**Troisième caractéristique : la menace se déplace vers l'infrastructure.** Les attaquants ciblent de moins en moins les utilisateurs finaux par le phishing classique et de plus en plus les équipements d'infrastructure — VPN, firewalls, passerelles réseau, équipements de bordure. L'ANSSI note que plus de la moitié de ses opérations de cyberdéfense en 2024 ont eu pour origine l'exploitation de vulnérabilités sur ces équipements, en 2025, les équipements de bordure restent des cibles privilégiées. Ce pivot est stratégique : il permet un accès silencieux, persistant, et souvent indétectable par les solutions de sécurité classiques.

**Quatrième caractéristique : l'intelligence artificielle amplifie les deux côtés.** L'IA n'est plus un facteur théorique. Elle est désormais utilisée opérationnellement tant par les attaquants (phishing personnalisé, deepfakes, automatisation de la reconnaissance) que par les défenseurs (détection augmentée, automatisation du SOC, analyse comportementale). Microsoft documente dans son Digital Defense Report 2025 une croissance significative des contenus générés par IA dans les opérations d'influence étatiques — une tendance qui s'accélère.

**Cinquième caractéristique : la réponse s'organise, mais reste fragmentée.** L'écosystème réglementaire s'est considérablement renforcé avec la transposition de NIS2, l'entrée en vigueur du Cyber Resilience Act, et DORA pour le secteur financier. Les opérations de disruption contre les groupes cybercriminels (Endgame, LockBit takedown, démantèlement LummaC2) ont produit des résultats tangibles. Mais la fragmentation réglementaire entre juridictions, la résilience structurelle de l'écosystème cybercriminel, et l'existence de « safe haven states » limitent l'impact durable de ces avancées.

Ce cours a pour ambition de fournir au praticien une **compréhension structurée, analytique et opérationnelle** de ce système de menace. Il ne s'agit ni d'un catalogue d'incidents, ni d'un résumé de rapports, mais d'une synthèse qui relie les dimensions stratégique, analytique, opérationnelle et décisionnelle de la cybermenace contemporaine.

#### 1.2 — Définition et périmètre d'un Cyber Threat Landscape (CTL) : ce que c'est, ce que ce n'est pas

Un Cyber Threat Landscape (CTL) est un produit d'intelligence qui fournit une **compréhension contextualisée des menaces passées et présentes**, permettant à son audience d'anticiper les menaces qu'elle est susceptible de rencontrer. La méthodologie ENISA 2025 le définit comme un livrable issu d'un processus intelligence-driven — c'est-à-dire structuré selon le cycle du renseignement — qui transforme des données brutes en intelligence exploitable.

Un CTL n'est pas un rapport d'incident. Il ne décrit pas un événement unique mais un **environnement de menace**. Il n'est pas non plus un catalogue d'outils ou une liste de vulnérabilités. Il articule des acteurs, des motivations, des capacités, des tendances et des impacts dans un cadre analytique cohérent, pour une audience définie et avec un périmètre explicite.

La distinction est fondamentale parce qu'elle conditionne la valeur du livrable. Un rapport d'incident informe sur ce qui s'est passé. Un CTL informe sur ce qui **pourrait** se passer, avec quel niveau de probabilité, et avec quelles implications — ce qui en fait un outil de décision, pas seulement de connaissance.

Les CTL peuvent être produits à différentes échelles : global (ENISA Threat Landscape, Microsoft Digital Defense Report), national (ANSSI Panorama de la cybermenace, ASD Annual Cyber Threat Report, CSE National Cyber Threat Assessment), sectoriel (ENISA Space Threat Landscape, CERT-EU Threat Landscape Report), ou organisationnel (CTL interne d'un CERT d'entreprise). Chaque échelle implique des choix méthodologiques différents en termes de sources, de profondeur et de format.

Le CTL peut être décliné en formats textuels (rapports PDF, briefings) ou machine-readable (feeds STIX/TAXII, indicateurs enrichis). Les deux formats sont complémentaires : le premier permet la communication stratégique et la prise de décision humaine, le second permet l'opérationnalisation automatisée dans les systèmes de détection et de défense.

> **⚠️ Piège fréquent** : confondre un CTL avec un rapport de veille. La veille est un flux continu d'informations brutes ou triées. Le CTL est un **produit analytique fini**, avec des assessments, des niveaux de confiance, et des recommandations. Produire un CTL exige un travail d'analyse qui va bien au-delà de la compilation.

#### 1.3 — Pourquoi le CTL est devenu un livrable stratégique : NIS2, DORA, gouvernance cyber

Le CTL a longtemps été un produit réservé aux équipes CTI spécialisées. Trois facteurs l'ont transformé en **livrable stratégique attendu au niveau de la gouvernance**.

**Le facteur réglementaire.** La directive NIS2, dont la transposition est en cours dans les États membres, impose aux entités essentielles et importantes une approche de la cybersécurité fondée sur les risques. L'article 21 exige des mesures de gestion des risques « tenant compte de l'état de l'art » — ce qui suppose une connaissance actualisée du paysage de menace. Le règlement DORA, spécifique au secteur financier, va plus loin en exigeant des tests de résilience fondés sur des scénarios de menace crédibles. Le Cyber Resilience Act étend cette logique aux produits numériques tout au long de leur cycle de vie. Dans ce cadre réglementaire, le CTL passe du « nice to have » au « requis pour la conformité ».

**Le facteur de gouvernance.** Les conseils d'administration et les comités exécutifs sont de plus en plus tenus responsables de la posture de cybersécurité de leur organisation. Les normes de gouvernance (ISO 27001:2022, NIST CSF 2.0) intègrent désormais explicitement l'analyse de la menace comme input de la gestion des risques. Le CTL devient l'outil qui permet au RSSI de traduire l'intelligence technique en langage de décision business.

**Le facteur opérationnel.** Les équipes de détection et de réponse ont besoin de prioriser. Face à un flux continu d'alertes, de vulnérabilités et de rapports, le CTL fournit le cadre de priorisation fondé sur la menace réelle — pas sur la menace théorique. L'approche « threat-informed defense » — défendre en fonction de ce que les attaquants font réellement, pas de ce qu'ils pourraient théoriquement faire — repose entièrement sur un CTL de qualité.

#### 1.4 — Les producteurs de threat landscape : cartographie des publications mondiales

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

#### 1.5 — Architecture du cours et guide de lecture

Ce cours est structuré en sept parties suivant une progression en entonnoir : des fondations méthodologiques (comment analyse-t-on la menace ?) vers les acteurs (qui menace ?), l'écosystème criminel (comment fonctionne l'industrie du cybercrime ?), les surfaces et vecteurs (où et comment les attaques se produisent-elles ?), les cadres de réponse (comment se défend-on et qui coordonne ?), la prospective et la mise en pratique (comment anticiper et produire un CTL ?), et enfin les cas de synthèse intégrant l'ensemble.

Chaque partie se termine par un **capstone** — un exercice de synthèse qui intègre les concepts des chapitres précédents dans un livrable opérationnel. Chaque chapitre contient un épisode du fil rouge, qui illustre les concepts dans un contexte professionnel réaliste.

Le cours est conçu pour être lu séquentiellement, mais chaque partie est suffisamment autonome pour servir de référence indépendante. Les renvois croisés entre chapitres sont explicites et systématiques.

#### 1.6 — 🔴 Fil rouge : Sophie prend ses fonctions

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

### Chapitre 2 — Méthodologie de production d'un Threat Landscape

#### 2.1 — Le cycle du renseignement appliqué au CTL

La production d'un Cyber Threat Landscape repose sur le cycle du renseignement — un processus itératif en six phases que l'ENISA a formalisé dans sa méthodologie CTL 2025 et que le CERT-EU opérationnalise dans son framework CTI.

**Phase 1 — Direction (planification).** Cette phase définit le « pourquoi » du CTL : quel est son objectif ? Pour qui est-il produit ? Quelles questions doit-il résoudre ? L'ENISA distingue trois éléments fondamentaux à établir : le périmètre (scope), l'audience (target audience) et les intelligence requirements (besoins en renseignement). Sans direction claire, le CTL risque de devenir un exercice de compilation sans valeur analytique.

Les intelligence requirements se déclinent en trois niveaux. Les Priority Intelligence Requirements (PIR) sont les questions stratégiques fondamentales : « Quels acteurs menacent notre secteur ? Quelles sont les tendances émergentes ? ». Les Specific Intelligence Requirements (SIR) détaillent les PIR en questions opérationnelles : « Quels groupes ransomware ciblent l'industrie de défense en Europe ? ». Les Requests for Information (RFI) sont des besoins ponctuels : « Quel est le TTP utilisé par APT28 dans la campagne X ? ».

**Phase 2 — Collecte.** La collecte consiste à identifier, valider et acquérir les données nécessaires pour répondre aux intelligence requirements. Le plan de collecte doit préciser les types de sources (OSINT, CTI feeds commerciaux, télémétrie interne, partage entre pairs, partenaires institutionnels), les critères de sélection et le scoring de fiabilité. La méthodologie ENISA 2025 insiste sur l'importance d'un score de pertinence EU (EU relevancy score) pour filtrer les données pertinentes dans un flux global massif.

Les sources se répartissent en plusieurs catégories. Les sources ouvertes (OSINT) incluent les rapports publics des agences nationales, les blogs de sécurité des éditeurs (Mandiant/Google TI, Microsoft MSTIC, CrowdStrike, Recorded Future), les publications académiques, et les communications officielles des CERT. Les sources fermées incluent les feeds CTI commerciaux, les échanges entre CERT au sein de réseaux de confiance (FIRST, TF-CSIRT, ISACs sectoriels), et la télémétrie interne des organisations. Les sources primaires — données brutes issues de l'observation directe d'incidents — sont les plus précieuses mais les plus difficiles à obtenir en dehors des CERT nationaux.

> **⚠️ Piège fréquent** : le biais de source unique. Un analyste qui ne consomme que les rapports d'un seul éditeur de sécurité hérite de tous les biais de cet éditeur (clientèle spécifique, géographie limitée, focus sectoriel). Le CERT-EU note dans son TLR 2025 que l'expansion de son propre monitoring par IA en 2025 a augmenté certaines métriques — ce qui reflète une meilleure capacité de collecte, pas nécessairement une augmentation des menaces. Ce type de biais méthodologique doit toujours être explicité.

**Phase 3 — Traitement.** Le traitement transforme les données brutes en un format exploitable pour l'analyse. Cette phase inclut la normalisation (conversion vers un format commun — typiquement STIX 2.1), la corrélation (rapprochement de données provenant de sources différentes), l'enrichissement (ajout de contexte aux indicateurs bruts) et le triage (priorisation selon les intelligence requirements). Le traitement linguistique est également un enjeu : les rapports collectés dans différentes langues doivent être traduits et normalisés en un langage cohérent, avec le risque de perdre des nuances.

**Phase 4 — Analyse et production.** C'est le cœur du processus — le passage de l'information à l'intelligence. L'analyse CTL combine plusieurs techniques : l'identification des key assessments (les conclusions principales que le CTL doit établir), l'analyse d'alternatives (considérer des hypothèses concurrentes), l'identification des drivers clés (les facteurs qui expliquent le mieux les phénomènes observés), et la gestion des inconsistances (les données qui contredisent les hypothèses de travail).

La méthodologie ENISA identifie plusieurs défis récurrents de cette phase : le manque de confiance dans les données collectées, la multiplicité des auteurs et des experts impliqués, et la nécessité de produire des statistiques fiables. La recommandation centrale est de maintenir une rigueur constante : vérifier ses assessments, considérer les alternatives, traiter les inconsistances, se concentrer sur les drivers clés et maintenir le contexte global.

**Phase 5 — Dissémination.** La dissémination livre le CTL à son audience. Elle peut prendre trois formes : push (envoi actif au destinataire), pull (mise à disposition sur une plateforme), ou interactive (briefing, présentation, échange). Le choix du modèle dépend de l'audience et de l'objectif. Un CTL destiné au COMEX sera typiquement disseminé en push (présentation + document), tandis qu'un CTL opérationnel sera disponible en pull sur une plateforme interne et en feeds machine-readable.

Le Traffic Light Protocol (TLP) régit les conditions de partage : TLP:RED (destinataires nommés uniquement), TLP:AMBER (organisation du destinataire), TLP:AMBER+STRICT (limité aux participants), TLP:GREEN (communauté élargie), TLP:CLEAR (diffusion publique). Le choix du TLP est un arbitrage entre la valeur du partage et la protection des sources.

**Phase 6 — Feedback.** Le cycle se boucle par la collecte du retour d'expérience de l'audience. Ce feedback informe la direction de la prochaine itération : les intelligence requirements étaient-ils pertinents ? Le format était-il adapté ? Quels sujets manquaient ? Le feedback transforme le CTL d'un produit ponctuel en un processus d'amélioration continue.

#### 2.2 — La méthodologie ENISA CTL 2025 : principes directeurs et phases

L'ENISA a publié en août 2025 une version mise à jour de sa méthodologie de production du Cyber Threat Landscape. Ce document est la référence méthodologique la plus complète disponible publiquement pour la production de CTL à grande échelle.

La méthodologie ENISA repose sur une approche coopérative : la production du CTL implique des analystes internes, des parties prenantes externes (États membres, partenaires privés), et un processus de validation multi-niveaux. Le cycle de production est visualisé comme un processus itératif où chaque phase génère du feedback pour les phases précédentes.

Plusieurs principes méritent d'être soulignés. Le premier est l'importance des taxonomies conséquentes : la manière dont les menaces sont classifiées conditionne la qualité de l'analyse et la comparabilité des résultats dans le temps. Le second est l'ancrage dans des frameworks reconnus : STIX 2.1 pour la représentation, MITRE ATT&CK pour la structuration des TTPs, et la taxonomie ENISA des menaces comme grille de classification. Le troisième est la distinction entre formats textuels (pour la communication humaine) et machine-readable (pour l'opérationnalisation automatisée).

L'ENISA note que des changements sont prévus pour les templates CTL en 2025, signe que la méthodologie est un document vivant qui évolue avec les besoins de ses parties prenantes. L'automatisation croissante du traitement des données — y compris via l'IA — est identifiée comme un axe de développement futur, avec des implications sur la vitesse de production, la couverture, et les risques de biais algorithmique.

#### 2.3 — Définir le périmètre, l'audience et les intelligence requirements

La qualité d'un CTL dépend de la qualité de son cadrage initial. Trois questions doivent être tranchées avant toute collecte.

**Le périmètre** définit ce que le CTL couvre et ce qu'il exclut. Un périmètre géographique (UE, France, mondial), sectoriel (défense, finance, santé), technique (IT, OT, cloud, spatial), ou temporel (12 mois, 6 mois, temps réel). Le périmètre doit être explicite et documenté, car il conditionne l'interprétation des résultats. Un CTL qui couvre uniquement l'UE ne peut pas prétendre évaluer la menace mondiale — même si les tendances sont souvent transposables.

**L'audience** détermine le niveau de détail, le format et le vocabulaire. Un CTL pour le COMEX sera synthétique, orienté décision, en langage business. Un CTL pour les analystes SOC sera technique, détaillé, riche en IOCs et en TTPs. Un CTL pour le régulateur sera structuré autour des obligations réglementaires. Le même corpus d'intelligence peut — et devrait — être décliné en plusieurs formats selon les audiences.

**Les intelligence requirements** transforment le besoin implicite de l'audience en questions explicites et actionnables. La formulation est essentielle : « Quelles sont les menaces ? » est une mauvaise question (trop large, pas actionnable). « Quels groupes ransomware ont ciblé le secteur aéronautique européen au cours des 12 derniers mois, avec quelles TTPs et quels taux de succès ? » est une bonne question (périmètre clair, actionnable, mesurable).

#### 2.4 — Plan de collecte : types de sources, validation, scoring

Le plan de collecte opérationnalise les intelligence requirements en identifiant les sources nécessaires et les modalités de leur exploitation. Il doit répondre à trois questions : quelles données collecter ? Auprès de quelles sources ? Comment valider leur fiabilité ?

La validation des sources repose sur le scoring de confiance. La méthodologie ENISA et le framework CERT-EU utilisent tous deux le code Admiralty (NATO), qui évalue séparément la fiabilité de la source (de A — complètement fiable à F — fiabilité impossible à juger) et la crédibilité de l'information (de 1 — confirmée par d'autres sources à 6 — crédibilité impossible à juger). La combinaison des deux dimensions produit un score de confiance (par exemple A1, B2) qui conditionne l'utilisation de l'information dans le CTL. Le détail de ce système est traité au Chapitre 5.

Le CERT-EU applique un seuil strict : seules les informations de sources A ou B avec une crédibilité de 1 ou 2 sont utilisées dans ses produits CTI. Ce seuil garantit que les produits sont basés sur des sources ayant un track record démontré et une corroboration suffisante. C'est un choix méthodologique fort, qui sacrifie la couverture au profit de la fiabilité.

#### 2.5 — Traitement et structuration des données collectées

Le traitement convertit les données brutes en formats exploitables. Trois opérations clés structurent cette phase.

La **normalisation** consiste à convertir les données hétérogènes (rapports textuels en différentes langues, feeds techniques en différents formats, communications informelles) en un format commun. Pour les données techniques, STIX 2.1 s'est imposé comme le standard de représentation. Pour les données textuelles, la normalisation passe par l'extraction des éléments structurants (acteurs, TTPs, victimes, dates, IOCs) et leur codification.

La **corrélation** rapproche des données provenant de sources différentes pour identifier des patterns. Un IOC technique repéré dans un feed commercial peut être corrélé avec un TTP documenté dans un rapport CERT, lui-même corrélé avec un incident observé en interne. La corrélation est le mécanisme qui transforme des données isolées en intelligence.

L'**enrichissement** ajoute du contexte aux données brutes. Un hash de malware brut a peu de valeur ; enrichi avec son historique de détection, ses associations à des groupes connus, et son comportement observé, il devient un indicateur exploitable. Les plateformes CTI (MISP, OpenCTI) automatisent partiellement cet enrichissement.

#### 2.6 — Analyse et production du livrable

L'analyse est le passage de l'information à l'intelligence — la phase où l'analyste produit des assessments, identifie des tendances et formule des recommandations. C'est aussi la phase la plus exigeante intellectuellement.

La méthodologie ENISA recommande plusieurs disciplines analytiques : établir les key assessments (les conclusions principales que l'audience attend), considérer les alternatives (quelles autres explications sont possibles ?), identifier les drivers clés (quels facteurs expliquent le mieux les phénomènes ?), et traiter les inconsistances (les données qui contredisent les hypothèses).

La production du livrable final exige une structuration rigoureuse. Le CERT-EU recommande l'utilisation de templates standardisés qui guident la rédaction et assurent la cohérence entre les éditions successives. Le langage analytique doit être calibré : les mots de probabilité estimative (WEP) doivent être utilisés de manière cohérente, et les niveaux de confiance doivent être explicités pour chaque assessment.

La validation avant publication est une étape critique. Le CTL doit être revu par des pairs, des experts du domaine et la hiérarchie. Cette revue vérifie l'exactitude des données, la cohérence des assessments, et la pertinence des recommandations.

#### 2.7 — Dissémination : formats, TLP et modèles d'interaction

La dissémination est souvent sous-estimée dans le processus CTL, alors qu'elle conditionne l'impact du produit. Un CTL excellent mais mal diffusé n'a aucune valeur.

Les formats textuels (rapports PDF, présentations) restent le vecteur principal pour la communication humaine. Les formats machine-readable (feeds STIX/TAXII, indicateurs enrichis) permettent l'opérationnalisation automatisée. L'ENISA note que ces deux catégories de formats servent des besoins complémentaires et que le choix dépend de l'audience et de l'objectif.

Le modèle d'interaction avec l'audience peut être push (envoi proactif), pull (mise à disposition) ou interactif (briefing, atelier). Les trois modèles ont des valeurs différentes : le push garantit que le livrable atteint sa cible, le pull permet une consultation à la demande, et l'interactif permet l'échange et l'approfondissement.

#### 2.8 — Limites méthodologiques : biais et mitigation

Tout CTL est soumis à des biais qu'il convient d'identifier, de documenter et de mitiger.

Le **biais de collecte** résulte de la nature des sources utilisées. Un CERT national ne voit que les incidents qui lui sont signalés. Un éditeur de sécurité ne voit que les menaces qui touchent ses clients. Le CERT-EU note explicitement dans son TLR 2025 que sa propre télémétrie offre une meilleure visibilité sur les menaces ciblant les institutions de l'UE que les divulgations tierces — ce qui signifie que certaines catégories de menaces sont structurellement sur-représentées ou sous-représentées.

Le **biais de visibilité** favorise les menaces qui se manifestent bruyamment (ransomware, DDoS, défigurations) au détriment des menaces silencieuses (espionnage persistant, prépositionnement). L'espionnage étatique est systématiquement sous-représenté dans les statistiques d'incidents parce qu'il est conçu pour ne pas être détecté.

Le **biais de publication** favorise les menaces qui génèrent des rapports publics. Les éditeurs de sécurité publient sur les menaces qu'ils ont détectées — ce qui crée un biais en faveur des menaces que leurs produits sont capables de détecter. Les menaces qui échappent aux solutions de sécurité dominantes sont structurellement sous-documentées.

Le **biais linguistique** — identifié par l'ENISA — résulte de la collecte principalement en anglais. Les rapports publiés dans d'autres langues (chinois, russe, arabe, farsi) sont souvent sous-exploités, alors qu'ils contiennent des informations précieuses sur les acteurs et les victimes de ces régions.

La mitigation de ces biais passe par la **diversification des sources**, l'**explicitation des limites** dans le CTL, et la **distinction systématique entre ce qui est observé et ce qui est inféré**. Un CTL honnête ne cache pas ses angles morts — il les documente.

#### 2.9 — 🔴 Fil rouge : Sophie structure sa méthodologie

> **📌 FIL ROUGE — Épisode 2**
>
> Sophie consacre sa première semaine à formaliser la méthodologie du CTL d'EuroDefense. Elle commence par les intelligence requirements, formulés avec le RSSI et les responsables de chaque BU :
>
> — PIR 1 : Quels acteurs étatiques menacent le secteur aéronautique/défense/spatial européen ?
> — PIR 2 : Quel est l'état de l'écosystème ransomware ciblant notre secteur ?
> — PIR 3 : Quels vecteurs d'attaque sont les plus utilisés contre nos systèmes (IT, OT, spatial) ?
> — PIR 4 : Quelle est la menace sur notre supply chain logicielle et matérielle ?
>
> Elle choisit ses frameworks : MITRE ATT&CK pour structurer les TTPs, le code Admiralty pour le scoring de confiance, le framework CERT-EU pour la catégorisation des menaces et le scoring des acteurs. Elle crée un template de livrable en deux versions : un executive summary de 10 pages pour le COMEX, et un rapport technique de 80+ pages pour les équipes CERT et SOC.
>
> Premier constat : le CERT d'EuroDefense manque de sources sur les filiales asiatiques. Sophie note ce biais de collecte dans son plan et prévoit de le combler par un abonnement à un feed CTI spécialisé Asie-Pacifique et un rapprochement avec l'ASD australien via le réseau FIRST.

---

### Chapitre 3 — Taxonomies, frameworks et outils analytiques

#### 3.1 — La taxonomie ENISA des menaces

La classification des menaces est le squelette structurant de tout CTL. Sans taxonomie cohérente, les données collectées ne peuvent être ni organisées, ni comparées dans le temps, ni corrélées entre sources. La taxonomie ENISA des menaces, établie en 2016 et mise à jour en 2022, est la référence européenne. Elle classe les menaces en grandes catégories : ransomware, malware, ingénierie sociale, menaces contre les données, menaces contre la disponibilité (DDoS), manipulation de l'information, attaques sur la supply chain, et menaces liées à la compromission de comptes.

L'ENISA note que cette taxonomie est actuellement en révision « pour développer un cadre plus mature et actionnable ». Cette révision est motivée par l'évolution du paysage de menace : certaines catégories se chevauchent (un ransomware est aussi un malware), certaines menaces émergentes (IA offensive, compromission de modèles) ne rentrent pas proprement dans les catégories existantes, et la granularité actuelle ne permet pas toujours une analyse opérationnelle fine.

Pour le praticien, la taxonomie est un outil — pas une fin en soi. L'important est de choisir une taxonomie, de l'appliquer de manière cohérente, et de documenter les écarts lorsque les données ne rentrent pas proprement dans les catégories. La comparabilité dans le temps (pouvoir comparer le CTL de cette année avec celui de l'année dernière) exige une stabilité taxonomique que les révisions fréquentes peuvent compromettre.

Le CERT-EU a développé sa propre taxonomie des catégories de menace dans son framework CTI, organisée en plusieurs niveaux. Au niveau le plus élevé, les « threat domains » distinguent le cyberespionnage et prépositionnement, le cybercrime, le hacktivisme, les opérations d'information, et les activités opportunistes. Cette distinction par finalité (plutôt que par technique) est particulièrement pertinente pour la communication avec les décideurs, qui raisonnent en termes de motivations et d'impacts plutôt que de vecteurs techniques.

#### 3.2 — Le framework CTI du CERT-EU

Le Cyber Threat Intelligence Framework du CERT-EU, publié en 2025, mérite une attention particulière car il définit les standards analytiques et opérationnels utilisés pour classifier, évaluer et prioriser les activités malveillantes pertinentes pour les institutions de l'Union.

Le concept central est celui de **Malicious Activity of Interest (MAI)** — une activité malveillante qui satisfait les critères de pertinence pour les constituants du CERT-EU et leur écosystème. Le MAI est l'unité de base de l'analyse : chaque activité malveillante observée est qualifiée (ou non) comme MAI, puis classifiée, évaluée et priorisée selon le framework.

Le framework introduit plusieurs dimensions structurantes. Les **niveaux de menace** (threat levels) évaluent la gravité de la menace sur une échelle définie. Les **niveaux d'acteurs** (threat actor levels) évaluent la sophistication et les ressources de l'acteur. Le **scoring** combine ces dimensions pour prioriser la réponse. L'ensemble est conçu pour permettre la « Full-Spectrum Adversary Approach » — une approche de défense informée par la menace qui couvre à la fois les dimensions stratégiques et techniques.

Le framework définit également les secteurs d'intérêt, alignés sur les secteurs NIS2 (énergie, transport, finance, santé, etc.) plus des secteurs additionnels pertinents pour les institutions de l'UE (diplomatie, défense, administration parlementaire, droits fondamentaux, etc.). Cette liste sectorielle structure l'analyse et la classification des MAI.

> **💡 Implication opérationnelle** : le framework CERT-EU est un excellent modèle pour toute organisation souhaitant formaliser sa propre approche CTI. Ses principes — MAI comme unité de base, scoring multi-dimensionnel, secteurs d'intérêt définis, niveaux de confiance explicites — sont transposables à n'importe quel contexte.

#### 3.3 — MITRE ATT&CK comme grille structurante des TTPs

MITRE ATT&CK est une base de connaissances des tactiques et techniques adverses fondée sur des observations réelles. Organisée en matrices (Enterprise, Mobile, ICS), elle structure les TTPs en tactiques (le « pourquoi » — l'objectif tactique de l'attaquant) et en techniques (le « comment » — les moyens utilisés pour atteindre cet objectif).

La force d'ATT&CK réside dans sa granularité et sa factualité : chaque technique est documentée avec des exemples réels, des procédures de détection et des mesures de mitigation. Cela en fait un outil de travail quotidien pour les analystes CTI, les detection engineers et les red teamers.

Dans le contexte d'un CTL, ATT&CK sert de grille de structuration des TTPs observés. Plutôt que de décrire les techniques d'un acteur dans un texte libre, l'analyste les mappe sur les techniques ATT&CK, ce qui permet la comparaison entre acteurs, la traçabilité dans le temps, et l'opérationnalisation dans les règles de détection.

Les limites d'ATT&CK doivent être connues. Le framework décrit le « quoi » mais pas le « comment exact » — deux acteurs peuvent utiliser la même technique ATT&CK de manière très différente. Le framework est principalement centré sur l'Enterprise IT et couvre moins bien les environnements OT, cloud-natif et spatial — même si les matrices ICS et Cloud existent. Enfin, ATT&CK est un framework descriptif, pas prédictif : il dit ce que les attaquants ont fait, pas ce qu'ils feront.

Pour le secteur spatial, des adaptations spécifiques existent : le framework SPARTA (Space Attack Research & Tactic Analysis) de l'Aerospace Corporation et le ESA SPACE-SHIELD, tous deux basés sur MITRE ATT&CK mais adaptés au domaine spatial.

#### 3.4 — STIX 2.1 et TAXII : représentation et échange normalisés

STIX (Structured Threat Information eXpression) est le standard de représentation de la CTI développé par l'OASIS CTI Technical Committee. Publié comme standard OASIS en 2021, STIX 2.1 est un langage (et une ontologie) qui décrit les cyber-menaces et les observables associés de manière cohérente et machine-readable.

STIX 2.1 intègre d'autres frameworks : les TTPs sont structurées selon MITRE ATT&CK, les indicateurs techniques sont enrichis par des observables standardisés, et les relations entre entités (acteur → utilise → malware → cible → secteur) sont formalisées dans un graphe exploitable programmatiquement.

TAXII (Trusted Automated Exchange of Intelligence Information) est le mécanisme de transport associé à STIX. Il définit comment les données STIX sont échangées entre systèmes — typiquement via des serveurs TAXII qui exposent des collections de données auxquelles les consommateurs peuvent s'abonner.

Pour le praticien, STIX/TAXII est le format de référence pour toute CTI machine-readable. Les plateformes CTI (MISP, OpenCTI) supportent nativement STIX 2.1, et les feeds commerciaux sont de plus en plus disponibles dans ce format. Le bénéfice principal est l'interopérabilité : des données STIX produites par un CERT national peuvent être consommées automatiquement par les systèmes de détection d'une entreprise, sans intervention humaine.

#### 3.5 — Cyber Kill Chain, Diamond Model : complémentarités et limites

La **Cyber Kill Chain** (Lockheed Martin) modélise l'attaque comme une séquence de phases : reconnaissance, armement, livraison, exploitation, installation, commande et contrôle, actions sur objectif. Son intérêt est la linéarité : elle permet de visualiser une attaque comme un processus séquentiel et d'identifier les points d'interception possibles à chaque étape. Sa limite est justement cette linéarité : les attaques modernes sont rarement séquentielles et impliquent souvent des itérations, des pivots et des retours en arrière.

Le **Diamond Model** (Caltagirone, Pendergast, Betz) modélise l'intrusion comme un losange à quatre sommets : adversaire, capacité, infrastructure, victime. Chaque intrusion est décrite par la relation entre ces quatre éléments. L'intérêt du Diamond Model est sa capacité à modéliser les relations entre acteurs et à structurer l'analyse d'attribution. Sa limite est son abstraction : il décrit la structure d'une intrusion mais pas sa dynamique.

Ces frameworks sont complémentaires avec MITRE ATT&CK. La Kill Chain donne la vision séquentielle, le Diamond Model donne la vision relationnelle, et ATT&CK donne la vision granulaire des techniques. Un analyste CTI expérimenté utilise les trois, en fonction du besoin analytique.

#### 3.6 — L'EUVD : un nouvel outil de coordination pan-européen (2025)

L'European Union Vulnerability Database (EUVD), lancée en 2025, est un nouvel outil de coordination pan-européen pour la gestion des vulnérabilités. Complémentaire du catalogue KEV (Known Exploited Vulnerabilities) de la CISA américaine et du système CVE du NIST, l'EUVD vise à fournir une perspective européenne sur les vulnérabilités exploitées, en intégrant les signalements des CERT nationaux européens et les obligations de notification prévues par NIS2 et le CRA.

Pour le praticien, l'EUVD s'inscrit dans un écosystème de gestion des vulnérabilités qui inclut : le CVE (identification), le CVSS (scoring de sévérité), l'EPSS (probabilité d'exploitation), le KEV CISA (confirmation d'exploitation active), et désormais l'EUVD (perspective européenne). L'articulation entre ces outils est un enjeu opérationnel : prioriser les vulnérabilités en combinant leur sévérité technique (CVSS), leur probabilité d'exploitation (EPSS) et leur exploitation confirmée (KEV/EUVD) est significativement plus efficace qu'un simple classement par score CVSS.

#### 3.7 — 🔴 Fil rouge : Sophie choisit ses frameworks

> **📌 FIL ROUGE — Épisode 3**
>
> Sophie doit arbitrer entre couverture et exploitabilité. Elle présente à son équipe CERT le choix des frameworks pour le CTL d'EuroDefense :
>
> — **Taxonomie** : taxonomie ENISA adaptée au périmètre EuroDefense, avec ajout de catégories spatiales issues du Space Threat Landscape 2025.
> — **Structuration des TTPs** : MITRE ATT&CK (Enterprise + ICS), complété par SPARTA pour les systèmes spatiaux.
> — **Scoring de confiance** : code Admiralty avec le seuil CERT-EU (A1, A2, B1, B2 uniquement).
> — **Classification des acteurs** : niveaux d'acteurs du framework CERT-EU.
> — **Représentation machine-readable** : STIX 2.1, partagé via l'instance MISP interne.
>
> Un analyste junior demande : « Pourquoi ne pas utiliser aussi le Diamond Model ? ». Sophie répond que le Diamond Model sera utilisé ponctuellement pour l'analyse d'attribution, mais que le structurer comme grille systématique pour l'ensemble du CTL serait trop lourd pour la taille de l'équipe. « On choisit ses batailles. L'important, c'est la cohérence, pas l'exhaustivité des frameworks. »

---

### Chapitre 4 — Acteurs de la menace : typologies, motivations et convergences

#### 4.1 — Catégorisation des threat actors

La catégorisation des acteurs de la menace est un exercice fondamental mais intrinsèquement imparfait. Les catégories sont des outils analytiques — pas des réalités ontologiques. Un acteur peut appartenir à plusieurs catégories simultanément, migrer d'une catégorie à l'autre, ou être instrumentalisé par un acteur d'une autre catégorie. Cette fluidité est précisément le phénomène le plus structurant du paysage 2025-2026.

Les **acteurs étatiques** (state-sponsored ou state-aligned) opèrent au service des objectifs stratégiques d'un État. Leurs motivations incluent l'espionnage stratégique (renseignement politique, militaire, économique), le prépositionnement (installation d'accès persistants dans les infrastructures critiques en prévision d'un conflit futur), la déstabilisation (attaques destructives, manipulation de l'information) et la répression transnationale (surveillance de dissidents, opposants, diasporas). Les principaux programmes étatiques documentés dans le corpus sont ceux de la Chine, de la Russie, de l'Iran et de la Corée du Nord — traités en détail dans la Partie II.

Le CERT-EU identifie, sur la période de reporting 2025, 46 ensembles d'intrusion distincts actifs contre l'UE, dont les attributions se répartissent ainsi : Russie-nexus (32%), Chine-nexus (24%), RPDC-nexus (12%), PSOA (6,7%), Iran-nexus (5,3%), Inde-nexus (4%). Environ 14,2% des activités étatiques n'ont pas pu être attribuées à un ensemble d'intrusion connu — un rappel que la visibilité est toujours partielle.

Les **acteurs cybercriminels** sont motivés par le gain financier. Leur écosystème s'est industrialisé autour du modèle Crime-as-a-Service (CaaS), avec une division du travail entre développeurs de malware, opérateurs de ransomware, courtiers en accès initial, services de blanchiment, et hébergeurs bulletproof. Le détail de cet écosystème est traité dans la Partie III.

Les **hacktivistes** sont motivés par des convictions idéologiques ou politiques. La résurgence hacktiviste 2024-2025 est étroitement liée aux conflits géopolitiques — guerre en Ukraine, conflit Israël-Hamas — et se manifeste principalement par des attaques DDoS contre les administrations publiques et les entreprises des pays perçus comme adversaires. Le CERT-EU et l'ENISA documentent que le hacktivisme représente 79% des incidents enregistrés contre l'UE en 2025, mais avec un impact opérationnel généralement limité.

Les **mercenaires cyber** (Private Sector Offensive Actors — PSOA) sont des entreprises privées qui vendent des capacités offensives à des clients gouvernementaux ou privés. Le marché du spyware commercial (NSO Group/Pegasus, Candiru, Paragon) est le segment le plus documenté, mais il existe également un marché de services d'intrusion, de surveillance et de déstabilisation. Les PSOA opèrent dans des zones grises juridiques et posent des risques spécifiques pour la société civile, les journalistes, les défenseurs des droits humains et les institutions démocratiques.

Les **insiders** — individus disposant d'un accès légitime qui l'utilisent à des fins malveillantes — constituent une catégorie distincte dont l'importance croît dans le contexte de la compétition géopolitique. Microsoft note que les États-nations recrutent de plus en plus des insiders pour accéder au renseignement, souvent via des opérations à long terme utilisant des affiliations académiques ou professionnelles comme couverture.

#### 4.2 — Motivations : espionnage, gain financier, déstabilisation, prépositionnement

Les motivations des acteurs déterminent leur ciblage, leurs TTPs et leur persistance. Comprendre la motivation, c'est pouvoir prédire le comportement — au moins partiellement.

L'**espionnage stratégique** vise la collecte de renseignement politique, militaire, technologique ou économique. C'est la motivation dominante des acteurs étatiques chinois, russes et iraniens. La victimologie typique inclut les gouvernements, les institutions de défense, les centres de recherche, les télécommunications et les think tanks. L'espionnage est caractérisé par sa discrétion et sa persistance : les acteurs investissent des ressources considérables pour maintenir un accès durable sans être détectés.

Le **gain financier** est la motivation de l'écosystème cybercriminel. Il se décline en ransomware (extorsion), vol de données (revente), fraude (BEC, pig butchering), et vol de cryptomonnaies. La RPDC constitue un cas hybride où le gain financier finance directement les programmes étatiques — le ransomware et le vol de crypto servant à contourner les sanctions internationales.

La **déstabilisation** vise à perturber le fonctionnement normal d'un État, d'un secteur ou d'une société. Les attaques destructives russes contre l'Ukraine (wipers, attaques sur les infrastructures énergétiques) et leur spillover vers l'UE (cas polonais 2025) sont les manifestations les plus extrêmes. Le hacktivisme géopolitiquement aligné participe de cette logique à une échelle moindre.

Le **prépositionnement** est la motivation la plus préoccupante à moyen terme. Il consiste à installer des accès persistants dans les infrastructures critiques en prévision d'un conflit futur, sans les activer immédiatement. Le cas Volt Typhoon (Chine) est l'exemple le plus documenté : des accès dormants dans les infrastructures énergétiques, de transport et de communication américaines, prêts à être activés en cas de crise dans le détroit de Taïwan. L'ANSSI observe que les objectifs de ces prépositionnements « doivent collectivement nous alarmer ».

#### 4.3 — Niveaux de sophistication et de ressources

Tous les acteurs n'ont pas les mêmes capacités. Le framework CERT-EU introduit des **niveaux d'acteurs** (threat actor levels) qui évaluent la sophistication et les ressources disponibles. Cette gradation va de l'acteur opportuniste (outils publics, pas de ciblage spécifique) à l'acteur étatique avancé (développement de zero-day, capacités de cryptanalyse, opérations multi-domaines).

En pratique, la sophistication n'est pas monolithique. Un même acteur peut utiliser des techniques très avancées (exploitation de zero-day) pour l'accès initial et des techniques banales (commandes PowerShell standard) pour le mouvement latéral. L'adoption croissante d'outils cybercriminels « commodity » par les acteurs étatiques — un phénomène documenté par l'ANSSI, le CERT-EU et Microsoft — complique cette évaluation : un acteur qui utilise des outils courants n'est pas nécessairement peu sophistiqué.

Le CSE canadien propose une analyse pertinente : le modèle CaaS a rendu les outils sophistiqués accessibles à des acteurs moins compétents, ce qui a « presque certainement contribué à l'augmentation des incidents de ransomware en abaissant les barrières techniques à l'entrée ». En d'autres termes, le niveau de sophistication de l'outil ne reflète plus le niveau de sophistication de l'opérateur.

#### 4.4 — Le continuum état / cybecriminalité / hacktivisme

Le phénomène le plus structurant du paysage 2025-2026 est l'érosion des frontières entre ces catégories. Plusieurs mécanismes sont documentés.

La **convergence étatique-criminelle** prend plusieurs formes. Des acteurs étatiques utilisent des outils cybercriminels pour obscurcir l'attribution (l'ANSSI documente l'utilisation du ransomware NailoLocker combiné aux outils d'espionnage ShadowPad et PlugX). Des réseaux criminels fournissent des services aux acteurs étatiques (ransomware contre des infrastructures critiques, vol de données stratégiques) en échange de protection ou de rémunération. Europol note dans la SOCTA 2025 que les acteurs hybrides et les réseaux criminels « coopèrent pour un bénéfice mutuel, exploitant mutuellement leurs ressources, leur expertise et leur protection ».

Le **faketivisme** est un phénomène où des opérations étatiques se déguisent en hacktivisme. Le groupe Cyber Army of Russia Reborn (CARR), précédemment documenté comme opéré par le groupe étatique Sandworm (GRU), en est l'exemple emblématique. La revendication hacktiviste sert de couverture à des opérations qui auraient des implications géopolitiques si elles étaient ouvertement attribuées à un État.

La **convergence post-conflit** est un scénario prospectif documenté par Europol : dans un scenario post-guerre en Ukraine, les cybercriminels dirigés par des acteurs étatiques pourraient « rediriger leur expertise vers la cybercriminalité financière pure et continuer à cibler les institutions publiques, les entreprises et les individus ». Cette convergence pourrait intensifier la menace cybercriminelle en injectant des compétences étatiques dans l'écosystème criminel.

#### 4.5 — Les menaces hybrides : instrumentalisation croisée

La SOCTA 2025 d'Europol consacre une analyse substantielle aux menaces hybrides — définies comme des activités menées par des acteurs étatiques qui exploitent l'écosystème criminel pour atteindre des objectifs stratégiques.

Les activités documentées incluent : les attaques ransomware contre les infrastructures critiques (qui génèrent des revenus tout en perturbant les adversaires), le vol de données stratégiques (espionnage outsourcé à des réseaux criminels), les campagnes de propagande et de désinformation (utilisant des réseaux de bots et des trolls), l'instrumentalisation des flux migratoires et du trafic de drogue (pour déstabiliser les sociétés cibles), et l'évasion de sanctions (pour renforcer les économies sanctionnées).

Pour le praticien, les menaces hybrides posent un défi fondamental : elles ne rentrent dans aucune case proprement. Elles ne sont ni purement étatiques (ce qui permettrait une réponse diplomatique), ni purement criminelles (ce qui permettrait une réponse judiciaire). Elles exploitent précisément cette ambiguïté pour maximiser leur impact tout en minimisant les conséquences pour le commanditaire.

#### 4.6 — Limites de la catégorisation : attribution et manipulation

L'ANSSI résume le défi en une phrase : « S'il a toujours été complexe d'imputer une attaque informatique à un mode opératoire ou à un groupe d'attaquants, il est aujourd'hui également difficile de détecter et de faire sens de leurs traces dissimulées dans la complexité générale des environnements numériques. »

L'attribution est un processus analytique qui combine des indicateurs techniques (infrastructure, malware, TTPs), comportementaux (ciblage, timing, persistance) et contextuels (géopolitique, motivation, intérêt). Aucun indicateur n'est suffisant à lui seul. Les faux drapeaux sont courants : un acteur peut délibérément utiliser les outils ou l'infrastructure d'un autre pour brouiller l'attribution.

La réutilisation d'outillage complique encore l'analyse. Quand un acteur étatique utilise des outils cybercriminels disponibles publiquement, la présence de ces outils dans un incident n'est plus un indicateur d'attribution. La convergence des TTPs entre catégories d'acteurs rend les distinctions analytiques plus difficiles à maintenir.

> **⚠️ Garde-fou analytique** : ne jamais présenter une attribution comme un fait établi sans expliciter le niveau de confiance et les éléments qui la soutiennent. L'attribution est toujours un assessment — une conclusion analytique fondée sur des preuves, pas une vérité absolue. Le vocabulaire doit refléter cette nuance : « attribué avec une confiance modérée à un ensemble d'intrusion Russia-nexus » est correct. « L'attaque a été menée par la Russie » est une assertion qui dépasse le cadre de l'analyse technique.

#### 4.7 — 🔴 Fil rouge : Sophie cartographie les acteurs pertinents

> **📌 FIL ROUGE — Épisode 4**
>
> Sophie commence la cartographie des acteurs pertinents pour EuroDefense. Elle identifie quatre profils de menace prioritaires :
>
> 1. **Espionnage étatique chinois** (priorité haute) : EuroDefense développe des systèmes de défense avancés et des composants satellites. Les groupes Mustang Panda et APT41 ont un historique de ciblage du secteur aéronautique et de défense européen.
> 2. **Espionnage étatique russe** (priorité haute) : en tant que fournisseur OTAN, EuroDefense est dans le périmètre de ciblage du GRU (APT28) et du SVR (APT29). Le contexte Ukraine amplifie la menace.
> 3. **Ransomware / supply chain** (priorité haute) : la dépendance à 200+ sous-traitants crée une surface d'attaque étendue. Les groupes Qilin et Akira ciblent activement l'industrie européenne.
> 4. **RPDC** (priorité moyenne) : Lazarus cible le secteur défense via des offres d'emploi fictives. La branche spatiale d'EuroDefense est potentiellement visée pour le vol de technologie.
>
> Sophie note un angle mort : la filiale en Malaisie, qui partage un réseau avec des partenaires locaux dont la posture de sécurité est inconnue. C'est un risque de supply chain géographique qui n'apparaît dans aucun rapport public.

---

### Chapitre 5 — Indicateurs, niveaux de confiance et attribution

#### 5.1 — Types d'indicateurs : IoC, IoA et signaux faibles

Les indicateurs sont les données élémentaires sur lesquelles repose l'analyse CTI. Ils se déclinent en plusieurs catégories de valeur et de durée de vie différentes.

Les **Indicators of Compromise (IoC)** sont des artefacts techniques qui signalent une compromission : hashes de fichiers malveillants, adresses IP de serveurs C2, domaines malveillants, URLs de phishing, signatures de malware. Les IoC sont faciles à opérationnaliser (ils peuvent être chargés dans les systèmes de détection) mais ont une durée de vie courte : les attaquants changent régulièrement leur infrastructure et leurs outils. Un hash de malware est utile pendant quelques semaines ; une adresse IP de C2 peut être abandonnée en quelques jours.

Les **Indicators of Attack (IoA)** sont des patterns comportementaux qui signalent une attaque en cours ou imminente : séquences d'actions sur un système (exécution de PowerShell après ouverture d'un document Office), patterns de communication (beaconing régulier vers un domaine externe), ou anomalies de comportement utilisateur (accès inhabituels à des partages réseau). Les IoA sont plus durables que les IoC (les comportements changent moins vite que les outils) mais plus difficiles à opérationnaliser (ils nécessitent une analyse comportementale, pas un simple matching de signatures).

Les **TTPs** (Tactics, Techniques and Procedures), structurés selon MITRE ATT&CK, sont les indicateurs les plus durables et les plus stratégiques. Un acteur peut changer ses outils et son infrastructure quotidiennement, mais ses TTPs évoluent beaucoup plus lentement — parce qu'ils reflètent son expertise, son entraînement et ses objectifs. Identifier les TTPs d'un acteur permet de le reconnaître même lorsqu'il change tous ses indicateurs techniques.

Les **signaux faibles** sont des indicateurs partiels, ambigus ou non confirmés qui, pris isolément, ne permettent pas de conclure mais qui, combinés avec d'autres, peuvent révéler une menace émergente. Un scan inhabituel sur un port spécifique, une requête DNS vers un domaine récemment enregistré, un changement de comportement d'un compte utilisateur — chacun de ces éléments est anodin isolément mais peut être significatif en contexte.

#### 5.2 — Évaluer la confiance : le code Admiralty et la matrice CERT-EU

Le code Admiralty (ou NATO system) est le standard utilisé par l'ENISA et le CERT-EU pour évaluer la confiance dans les informations collectées. Il repose sur deux dimensions indépendantes.

La **fiabilité de la source** évalue le track record du producteur d'information : A (complètement fiable — source avec un historique long et vérifié), B (habituellement fiable), C (relativement fiable), D (habituellement peu fiable), E (peu fiable), F (fiabilité impossible à juger). Un CERT national avec lequel on collabore depuis des années sera typiquement noté A ou B. Un post anonyme sur un forum underground sera noté E ou F.

La **crédibilité de l'information** évalue la plausibilité et la corroboration de l'information elle-même : 1 (confirmée par d'autres sources), 2 (probablement vraie), 3 (possiblement vraie), 4 (douteuse), 5 (improbable), 6 (crédibilité impossible à juger). La crédibilité est indépendante de la source : une source fiable peut transmettre une information non confirmée (B3), et une source non testée peut transmettre une information corroborée (F1).

Le CERT-EU applique un **seuil d'acceptation strict** : seules les combinaisons A1, A2, B1 et B2 sont autorisées dans ses produits CTI. Toutes les autres combinaisons sont exclues. Ce seuil garantit que les produits sont basés sur des sources ayant un track record démontré (A ou B) et une corroboration ou plausibilité suffisante (1 ou 2). C'est un choix qui privilégie la fiabilité sur la couverture — un CTL qui ne rapporte que des informations de haute confiance sera plus fiable mais potentiellement moins complet qu'un CTL avec un seuil plus bas.

#### 5.3 — Communiquer l'incertitude : LCA, WEP et standards FIRST

Le CERT-EU implémente les guidelines FIRST pour la communication de l'incertitude dans les produits CTI, utilisant deux systèmes complémentaires.

Les **Levels of Confidence in Assessment (LCA)** expriment le degré de confiance dans un jugement analytique : low confidence (peu de données, analyse faible), moderate confidence (données partielles, analyse plausible), high confidence (données solides, analyse robuste). Le LCA reflète la qualité et la quantité des preuves ainsi que la solidité du raisonnement analytique.

Les **Words of Estimative Probability (WEP)** expriment la probabilité d'un événement futur ou l'exactitude d'une évaluation : « almost certainly » (>95%), « very likely » (80-95%), « likely » (55-80%), « roughly even chance » (45-55%), « unlikely » (20-45%), « very unlikely » (5-20%), « almost certainly not » (<5%). Ces mots sont calibrés — chaque terme correspond à une fourchette de probabilité définie — ce qui évite l'ambiguïté du langage courant.

L'utilisation cohérente de ces systèmes est une discipline analytique exigeante. L'erreur la plus fréquente est l'overconfidence — présenter un assessment comme « high confidence » alors que les données ne le justifient pas. L'erreur inverse — l'excès de prudence — produit des CTL tellement hédgés qu'ils perdent leur valeur décisionnelle. Le bon calibrage vient avec l'expérience et la rigueur.

#### 5.4 — Scoring et priorisation des menaces

Le scoring transforme l'analyse qualitative en évaluation quantifiable, nécessaire pour la priorisation. Le framework CERT-EU combine plusieurs dimensions dans son scoring : la sophistication de l'acteur, l'impact potentiel sur les constituants, la probabilité de matérialisation, et la capacité de détection et de réponse.

En pratique, le scoring doit être pragmatique. Un système trop complexe (20 critères pondérés) ne sera pas maintenu. Un système trop simple (haut/moyen/bas) ne différencie pas suffisamment. Le bon compromis dépend de la maturité de l'organisation et de la taille de l'équipe CTI.

#### 5.5 — Le problème de l'attribution

L'attribution — déterminer qui est responsable d'une cyberattaque — est l'un des problèmes les plus complexes de la CTI. Elle repose sur la convergence d'indicateurs techniques, comportementaux et contextuels, et reste intrinsèquement probabiliste.

Les **indicateurs techniques** incluent les malwares utilisés (certaines familles sont associées à des acteurs spécifiques), l'infrastructure C2 (certains acteurs réutilisent des blocs d'adresses IP ou des registrars), et les artefacts de développement (langues, fuseaux horaires, conventions de nommage dans le code). Chacun de ces indicateurs est manipulable : un acteur peut délibérément utiliser le malware d'un autre, enregistrer son infrastructure via des services associés à un tiers, ou insérer de faux artefacts.

Les **indicateurs comportementaux** incluent les TTPs (la manière dont l'attaque est conduite), la victimologie (le choix des cibles), le timing (heures de travail, jours de la semaine) et la persistance (durée et intensité de la campagne). Ces indicateurs sont plus difficiles à falsifier parce qu'ils reflètent les capacités et les objectifs réels de l'acteur.

Les **indicateurs contextuels** incluent le contexte géopolitique (qui a intérêt à attaquer cette cible à ce moment ?), les capacités connues (quels acteurs ont la capacité technique de mener cette attaque ?) et les précédents (cette attaque ressemble-t-elle à des attaques précédemment attribuées ?).

L'attribution publique — lorsqu'un gouvernement attribue officiellement une cyberattaque à un État — est un acte politique autant que technique. Elle implique des conséquences diplomatiques et doit être distinguée de l'attribution technique (qui est un assessment analytique) et de l'attribution judiciaire (qui répond à des standards de preuve beaucoup plus élevés).

#### 5.6 — Distinguer fait, hypothèse et piste exploratoire

La rigueur analytique exige une distinction permanente entre trois niveaux d'assertion.

Un **fait vérifié** est un élément objectivement constaté et confirmé : « Le malware X a été observé sur le réseau Y le 15 mars 2025 ». Un fait ne nécessite pas de qualificatif de probabilité.

Une **hypothèse probable** est une conclusion analytique fondée sur des preuves : « L'intrusion est attribuée avec une confiance modérée à un ensemble d'intrusion China-nexus, sur la base des TTPs observés et de la victimologie ». Une hypothèse doit toujours être accompagnée de son niveau de confiance et de ses éléments de soutien.

Une **piste exploratoire** est une possibilité non confirmée qui mérite investigation : « Les horaires de connexion pourraient indiquer un acteur opérant depuis le fuseau horaire UTC+8, ce qui est cohérent avec une origine chinoise mais aussi avec d'autres hypothèses ». Une piste exploratoire doit être explicitement identifiée comme telle.

Mélanger ces niveaux — présenter une hypothèse comme un fait, ou une piste comme une hypothèse — est l'erreur analytique la plus grave et la plus fréquente. Elle détruit la crédibilité du CTL et peut conduire à des décisions mal fondées.

#### 5.7 — 🔴 Fil rouge : signaux faibles sur un serveur exposé

> **📌 FIL ROUGE — Épisode 5**
>
> En février 2025, le SOC d'EuroDefense remonte à Sophie un pattern inhabituel : un serveur Exchange exposé à Internet génère un trafic sortant régulier (beaconing) vers un domaine enregistré il y a trois semaines, hébergé chez un fournisseur cloud légitime. Le volume est faible — quelques Ko toutes les 4 heures. Le domaine ne figure dans aucun feed CTI connu.
>
> Sophie applique sa grille d'analyse :
> — **Fait vérifié** : le beaconing existe, le domaine est récent, le pattern est régulier.
> — **Hypothèse** : le serveur est possiblement compromis. Le pattern de beaconing est cohérent avec un implant C2 de type Cobalt Strike ou ShadowPad (confiance : basse — les données sont insuffisantes pour discriminer).
> — **Piste exploratoire** : le ciblage d'un serveur Exchange exposé est cohérent avec les TTPs de plusieurs groupes — APT28, APT29, et des acteurs cybercriminels. L'attribution est impossible à ce stade.
>
> Sophie rédige une note de renseignement à confiance basse (B4 dans le code Admiralty — source habituellement fiable mais information douteuse) et recommande une investigation approfondie sans alerter le COMEX à ce stade. Elle applique le principe : « escalader quand le niveau de confiance justifie l'action, pas quand il justifie l'inquiétude ».

> **🎯 CAPSTONE Partie I** : À partir d'un briefing fictif décrivant le contexte d'une organisation industrielle européenne classée NIS2, définir : le périmètre du CTL (géographique, sectoriel, technique), les 4 PIR prioritaires, le framework d'analyse retenu (taxonomie, scoring, format), la grille de confiance, et les 5 principales sources à exploiter en justifiant leur sélection.

---
