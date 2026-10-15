---
title: "Analyse — Dark web et renseignement sur la menace : un panorama utile, des preuves fragiles"
date: 2026-09-29
kind: analysis
document_type: preprint
theme: cyber
slug: dark-web-et-renseignement-sur-la-menace
author: "Abdullah Abid Ali"
organization: "Punjab University College of Information Technology"
tags:
  - dark web
  - CTI
  - ransomware
  - courtiers d'accès initial
  - cybercriminalité
source_file: inbox/Cyber_Dark_Web_Intelligence.pdf
source_url: https://www.researchgate.net/publication/404397293_Dark_Web_Threat_Intelligence_Monitoring_Cybercriminal_Activities_and_Emerging_Cyber_Threats
---

# Analyse — Dark web et renseignement sur la menace : un panorama utile, des preuves fragiles

## Métadonnées

- **Document :** *Dark Web Threat Intelligence: Monitoring Cybercriminal Activities and Emerging Cyber Threats*, article de 5 pages au format de conférence (deux colonnes, sections numérotées en chiffres romains).
- **Auteur :** Abdullah Abid Ali, présenté en note comme étudiant du Punjab University College of Information Technology (PUCIT), avec une adresse de contact sur la plateforme de soumission papercept.net (p. 1). Les remerciements mentionnent un superviseur du PUCIT (p. 5).
- **Date :** aucune date dans le PDF ni dans ses métadonnées ; mise en ligne sur ResearchGate, dont l'adresse a été communiquée par l'utilisateur.
- **Financement :** « ce travail n'a été soutenu par aucune organisation » (p. 1).
- **Support :** PDF conservé dans `inbox/Cyber_Dark_Web_Intelligence.pdf`. Ni revue, ni conférence, ni procédure de relecture ne sont indiquées.
- **Périmètre :** l'écosystème du dark web, les activités cybercriminelles qui s'y déploient, les cadres d'analyse et outils de surveillance, les menaces émergentes et les stratégies défensives des organisations.
- **Méthode de la fiche :** jusqu'aux « Cinq éléments essentiels », seule la lecture du PDF fonde les constats, avec renvoi aux pages. La dernière section confronte ces constats à des sources extérieures citées et datées.

## Repères pour comprendre le document

Le texte relève du renseignement sur la menace cyber (CTI) appliqué au dark web, que l'auteur abrège en DWTI (*Dark Web Threat Intelligence*). Il suit la logique d'un manuel en cinq temps : décrire l'infrastructure (comment on accède au dark web), inventorier les activités criminelles (ce qui s'y vend), rattacher la surveillance aux modèles d'analyse connus (Kill Chain, ATT&CK, modèle en diamant), présenter les outils de collecte, puis recommander des défenses aux entreprises. Il faut garder à l'esprit une distinction que le texte brouille parfois : le **dark web** au sens strict (services accessibles par Tor, I2P ou Freenet) n'est qu'une partie des lieux où se négocie la cybercriminalité, qui passe aussi par des forums du web ouvert, des hébergeurs de fichiers et des messageries comme Telegram.

- **Web de surface, web profond, dark web** — Le web indexé par les moteurs de recherche ; le web non indexé (bases protégées, portails bancaires, dossiers médicaux) ; et la partie volontairement anonymisée du web profond, accessible seulement par des réseaux dédiés (p. 1).
- **Tor (The Onion Router)** — Réseau qui fait transiter le trafic par une suite de relais bénévoles en chiffrant chaque couche, si bien qu'aucun relais ne connaît à la fois la source et la destination ; il héberge des services cachés en `.onion` (p. 1).
- **I2P et Freenet** — Deux autres réseaux d'anonymisation : I2P, par « routage en ail » qui regroupe plusieurs messages chiffrés, est conçu pour des services internes au réseau ; Freenet stocke les données de façon décentralisée et résistante à la censure (p. 1).
- **DWTI (renseignement sur la menace issu du dark web)** — Collecte et analyse d'informations trouvées sur le dark web pour anticiper et contrer des attaques ; notion centrale de l'article (p. 1).
- **Fullz** — Lot complet de données d'identité et de carte bancaire d'une personne, revendu pour la fraude (p. 2).
- **RaaS (Ransomware-as-a-Service)** — Modèle où les développeurs d'un rançongiciel louent leur infrastructure à des « affiliés » qui mènent les attaques et leur reversent une commission (p. 2).
- **CaaS (Cybercrime-as-a-Service)** — Offre de services criminels clés en main (attaques par déni de service, kits d'hameçonnage, accès initiaux, développement de logiciels malveillants), qui abaisse la barrière d'entrée (p. 2).
- **Courtier d'accès initial (IAB)** — Acteur qui compromet des réseaux sans les exploiter lui-même et revend ces accès, du simple identifiant de bureau à distance à l'accès administrateur de domaine (p. 4).
- **Cyber Kill Chain, MITRE ATT&CK, modèle en diamant** — Trois cadres d'analyse des attaques : les sept étapes d'une intrusion selon Lockheed Martin, la taxonomie des tactiques et techniques des attaquants, et la lecture d'un incident par quatre pôles, adversaire, infrastructure, capacité, victime (p. 3).
- **Infostealer** — Logiciel malveillant qui aspire identifiants, cookies et données d'un poste pour les revendre ; l'auteur le cite parmi les sources des identifiants mis en vente (p. 2).
- **HUMINT cyber** — Infiltration de forums criminels par des analystes sous identité d'emprunt, pour recueillir ce que les outils automatiques ne voient pas (p. 4).
- **MISP, STIX, TAXII** — Plateforme et formats standardisés de partage de renseignement sur la menace entre organisations (p. 4).

## Résumé exécutif

L'article présente le dark web comme un centre de coordination de la cybercriminalité et soutient que les entreprises doivent étendre leur surveillance au-delà de leur périmètre pour y détecter les menaces avant qu'elles ne les frappent. Il se veut une vue d'ensemble destinée aux praticiens : structure des réseaux anonymes, grands marchés et incidents, types d'activités, cadres d'analyse, outils de collecte, menaces émergentes et défenses (p. 1).

Le déroulé est celui d'un manuel. L'auteur décrit Tor, I2P et Freenet, dresse deux tableaux, l'un de marchés célèbres (Silk Road, AlphaBay, Hansa, Dream Market, Hydra, BreachForums), l'autre d'incidents marquants de 2013 à 2022, puis passe en revue le rançongiciel en tant que service, le commerce des données volées avec une grille de prix, les *zero-days*, le cybercrime en tant que service et l'activité des États (p. 2). Il rattache ensuite la surveillance du dark web à la Kill Chain, à ATT&CK et au modèle en diamant, propose une formule de notation du renseignement et inventorie les méthodes et outils : collecte automatisée, veille par mots-clés, analyse des transactions en cryptomonnaie, infiltration humaine, plateformes de partage (p. 3-4).

Les menaces émergentes retenues sont l'IA détournée (WormGPT, FraudGPT), l'essor des courtiers d'accès initial, le ciblage des infrastructures critiques et la coordination d'attaques contre la chaîne d'approvisionnement. Les défenses recommandées forment un ensemble classique : surveillance continue, réponse aux incidents automatisée, architecture Zero Trust, priorisation des correctifs selon ce qui se vend réellement, programme contre les menaces internes et coopération avec les forces de l'ordre (p. 4-5).

Pour la veille, l'intérêt est **pédagogique** : le texte offre un plan clair du sujet et un vocabulaire de base. Sa valeur probante est en revanche faible. Aucune des quinze références n'est appelée dans le corps du texte, les chiffres et prix ne sont pas sourcés, plusieurs faits historiques sont inexacts (voir la section externe), la formule de notation n'est ni justifiée ni testée, et la rédaction présente des signes de reformulation automatique. À lire comme une introduction, jamais comme une source de faits.

## Chronologie

L'article retrace l'évolution du dark web criminel, des marchés de drogue aux écosystèmes cybercriminels (p. 2). Les dates ci-dessous sont celles du document :

- **2011-2013 :** Silk Road, premier grand marché, consacré à la drogue et aux faux documents ; fermé par le FBI en 2013.
- **2013-2019 :** Dream Market (drogue, fraude à la carte, kits d'exploitation).
- **2014-2017 :** AlphaBay (drogue, logiciels malveillants, données volées) ; **2015-2017 :** Hansa Market.
- **2015 :** fuite d'Ashley Madison, 37 millions de comptes diffusés sur des forums.
- **2015-2022 :** Hydra, marché russophone de drogue et de blanchiment, saisi en 2022.
- **2017 :** WannaCry, rançongiciel exploitant EternalBlue, 4 milliards de dollars de dommages estimés.
- **2019 :** « Collection #1 », 773 millions de combinaisons courriel/mot de passe publiées.
- **2020-2021 :** REvil vend ses kits en mode RaaS sur des forums du dark web.
- **2022 :** fuite des conversations internes du groupe Conti ; **2022-2023 :** BreachForums, marché de bases de données et d'identifiants volés.

## Thèse principale

L'auteur soutient que le dark web est devenu un environnement de menace permanent et mouvant, et que les organisations ne peuvent plus se contenter de défendre leur périmètre : elles doivent **surveiller ce qui se dit et se vend sur le dark web**, l'intégrer à leurs modèles d'analyse et à leurs outils de sécurité, et le compléter par une architecture Zero Trust et par la coopération avec les forces de l'ordre (p. 1, 5). Il en fait une capacité « urgente », que l'IA, les courtiers d'accès et le ciblage des infrastructures critiques rendent plus nécessaire encore (p. 5).

Il s'agit d'une synthèse descriptive et prescriptive, non d'une étude : l'article ne présente ni données collectées, ni expérimentation, ni évaluation d'outil, et conclut sur la nécessité de standardiser la collecte (p. 5).

## Informations et arguments importants

### L'infrastructure : trois couches et trois réseaux

L'auteur part de la représentation classique de l'internet en trois couches. Le web profond, qui contient aussi des ressources anodines (bases universitaires, intranets), serait de plusieurs ordres de grandeur plus vaste que le web de surface ; le dark web en est la partie volontairement anonymisée, de plus en plus associée aux marchés criminels, à la revente de données et à l'organisation d'attaques étatiques (p. 1). Trois technologies y donnent accès :

- **Tor** assure l'anonymat par un chiffrement en couches et héberge les services cachés `.onion`.
- **I2P** chiffre et regroupe les messages par routage « en ail » ; il sert surtout aux services internes, forums et partage de fichiers.
- **Freenet** stocke l'information de façon décentralisée, ce qui rend sa récupération et son attribution très difficiles pour les enquêteurs.

### Un écosystème de marchés et de forums

Les marchés fonctionnent comme des boutiques en ligne pour biens et services illicites ; à côté d'eux, des forums criminels comme RaidForums, XSS.is et Exploit.in servent à la fois au partage de connaissances et au recrutement (p. 1-2). Le tableau des marchés notables décrit une succession d'enseignes, chacune fermée ou saisie au bout de quelques années :

- **Silk Road** (2011-2013) : drogue et faux documents.
- **AlphaBay** (2014-2017) : drogue, logiciels malveillants, données volées.
- **Hansa Market** (2015-2017) : drogue et outils de cybercriminalité.
- **Dream Market** (2013-2019) : drogue, fraude à la carte, kits d'exploitation.
- **Hydra** (2015-2022) : drogue et blanchiment.
- **BreachForums** (2022-2023) : bases de données et identifiants volés.

### Ce qui se vend : cinq familles d'activités

L'auteur décrit un glissement des simples marchés de drogue vers des **écosystèmes cybercriminels complets**, dont il distingue cinq familles (p. 2).

#### Le rançongiciel en tant que service

Les développeurs louent leur infrastructure à des affiliés qui attaquent et leur reversent une commission, habituellement de 20 à 30 %. Le recrutement et la diffusion passent par les forums et les sites `.onion` ; REvil, Conti, LockBit et BlackCat (ALPHV) ont tenu des sites de fuite pour faire pression sur leurs victimes en menaçant de publier leurs données.

#### Les marchés de données volées

C'est selon l'auteur l'une des menaces les plus répandues. Les identifiants issus d'hameçonnage, de fuites ou de logiciels voleurs d'informations sont regroupés et vendus en gros, à des prix qui varient selon la nature des données :

- **Fullz** (données complètes de carte) : 10 à 50 dollars la fiche.
- **Identifiants VPN d'entreprise** : 500 à 10 000 par compte.
- **Dossiers médicaux** : 250 à 1 000 dollars la fiche.
- **Numéros de sécurité sociale américains** : 1 à 10 dollars.

Ces données alimentent l'usurpation d'identité, la fraude au président (BEC) et la prise de contrôle de comptes.

#### Les failles *zero-day*

Les vulnérabilités inconnues des éditeurs se négocient de quelques dizaines de milliers à plusieurs millions de dollars lorsqu'elles visent des logiciels d'entreprise répandus, des systèmes mobiles ou des systèmes industriels, avant de servir contre des administrations, des institutions financières ou des infrastructures critiques.

#### Le cybercrime en tant que service

Déni de service à la demande, abonnements à des kits d'hameçonnage, vente d'accès initiaux et développement de logiciels malveillants : cette offre permet à des acteurs peu qualifiés de mener des attaques avancées en achetant l'expertise d'autres criminels.

#### Les États et les groupes APT

Au-delà du gain financier, le dark web servirait de plateforme de coordination à des acteurs étatiques : achat d'outils sur mesure, recrutement d'informateurs, blanchiment de bitcoins, et acquisition de *zero-days*, d'outils de désinformation ou de données de reconnaissance d'infrastructures critiques, selon des liens établis « par des services de renseignement » que l'article ne cite pas (p. 2).

### Relier la surveillance aux modèles d'analyse

L'auteur veut montrer que le renseignement issu du dark web enrichit les cadres existants plutôt qu'il ne les remplace (p. 3). Dans la **Cyber Kill Chain**, il apporte du contexte à chaque étape, par exemple la mise en vente d'un kit d'exploitation (armement) ou d'une infrastructure de commande et de contrôle. Avec **MITRE ATT&CK**, il permet d'associer publications et échantillons aux techniques connues : la vente d'outils de *credential stuffing* renvoie à la technique T1110 (force brute), les annonces de courtiers d'accès à T1078 (comptes valides). Dans le **modèle en diamant**, il alimente les pôles « adversaire » et « infrastructure » : pseudonymes, portefeuilles de cryptomonnaie, domaines et adresses IP promus dans les communautés criminelles.

L'auteur rattache enfin la DWTI à l'OSINT et propose une **formule de notation** pour prioriser les informations recueillies : un score égal à la somme pondérée de la crédibilité de la source, de sa pertinence pour les actifs de l'organisation, de sa fraîcheur et de son caractère actionnable, les poids totalisant 1 (p. 3). Aucune valeur de pondération, aucun exemple d'application ni aucune validation ne sont fournis.

### Les méthodes et outils de surveillance

La collecte combine automatisation et intervention humaine (p. 3-4).

- **Collecte automatisée :** des robots d'indexation parcourent forums, marchés et sites de collage de texte ; contrairement à ceux du web ouvert, ils doivent passer par Tor ou I2P, composer avec leur lenteur et avec des contenus générés dynamiquement. OnionScan et des robots développés avec Scrapy sont cités.
- **Veille par mots-clés :** surveillance de noms de marque, de dirigeants, d'identifiants de produits ou de domaines, avec alerte dès leur apparition dans une nouvelle publication.
- **Analyse des cryptomonnaies :** le bitcoin et des monnaies axées sur la confidentialité comme Monero dominent les transactions ; des outils d'analyse de chaîne de blocs (Chainalysis, CipherTrace) servent à suivre les fonds et à attribuer des portefeuilles.
- **HUMINT cyber :** des analystes expérimentés infiltrent les forums sous une identité d'emprunt pour recueillir cibles, outils préférés et fonctionnement interne des groupes, dans un cadre éthique et juridique strict.
- **Partage :** MISP, STIX et TAXII permettent d'échanger ce renseignement dans des formats lisibles par machine.

Le tableau des outils cite Recorded Future, DarkOwl Vision, Flashpoint, Chainalysis Reactor, OnionScan, Maltego et SpiderFoot, avec des fonctions allant de l'agrégation automatisée à la visualisation de liens ; dans le PDF, la correspondance ligne à ligne entre outils et fonctions est désalignée (p. 3).

### Les menaces émergentes

Quatre évolutions sont mises en avant (p. 4).

- **L'IA au service du crime :** des modèles débridés ou conçus pour l'occasion, vendus sous des noms comme WormGPT ou FraudGPT, aident à rédiger des messages d'hameçonnage, du code malveillant et des scripts d'ingénierie sociale, ce qui abaisse le niveau de compétence requis.
- **Les courtiers d'accès initial :** leur écosystème a fortement grandi ; ils vendent des accès par paliers, de l'identifiant RDP à l'accès administrateur de domaine dans de très grandes entreprises. Leur activité peut annoncer un déploiement de rançongiciel.
- **Les infrastructures critiques :** les publications sur les vulnérabilités des systèmes industriels se multiplient, avec des ventes d'identifiants SCADA et de repérages d'usines de traitement d'eau ou de centrales, favorisées par la convergence des réseaux informatiques et industriels.
- **La chaîne d'approvisionnement :** à l'image de SolarWinds ou de 3CX, des forums servent à coordonner ces attaques, et des initiés y proposent des accès aux chaînes de développement logiciel.

### Les stratégies défensives

L'auteur recommande une défense en profondeur, qui mêle technique, procédures et coopération (p. 4-5). Il conseille une **surveillance continue** du dark web ciblant la marque, les domaines, les dirigeants et les technologies de l'organisation, y compris les canaux Telegram liés à ces communautés, et l'**intégration** des alertes aux outils SIEM et SOAR, qui déclenchent automatiquement changement de mots de passe et audit des comptes lorsqu'un identifiant d'entreprise apparaît sur un forum. Il recommande sans réserve l'**architecture Zero Trust**, qui vérifie en continu chaque utilisateur, appareil et application et réduit ainsi la valeur des identifiants volés, ainsi qu'une **priorisation des correctifs** selon ce qui se vend réellement plutôt que selon le seul score CVSS. S'y ajoutent un **programme contre les menaces internes**, puisque des criminels recrutent des employés pour obtenir des accès, et la **coopération public-privé** avec le FBI, le centre EC3 d'Europol et les CERT nationaux, dont la saisie d'Hydra en 2022 serait l'exemple.

## Points particulièrement intéressants pour la veille

- **Les courtiers d'accès comme signal avancé.** L'auteur présente la vente d'un accès comme un indice possible d'un rançongiciel à venir (p. 4). *Inférence pour la veille :* suivre les annonces de courtiers visant un secteur ou une région donne une fenêtre d'alerte que la seule surveillance des fuites publiées n'offre pas.
- **La valeur économique des données.** La grille de prix, même non sourcée, montre que ce qui se vend cher est l'accès (VPN d'entreprise) plutôt que la donnée de masse (numéros de sécurité sociale) (p. 2). *Inférence pour la veille :* la protection des identifiants d'accès et des sessions est la priorité défensive, bien plus que la seule confidentialité des bases clients.
- **L'IA abaisse la barrière d'entrée.** WormGPT et FraudGPT illustrent une démocratisation des capacités offensives (p. 4). *Inférence pour la veille :* la question n'est plus de savoir si des criminels utilisent l'IA, mais comment elle change le volume et la cible des attaques.
- **Le dark web déborde du dark web.** L'auteur inclut Telegram dans la surveillance à mener (p. 4). *Inférence pour la veille :* une veille qui se limiterait aux services `.onion` manquerait une large part du commerce criminel, qui s'est déplacé vers des messageries et des forums du web ouvert.
- **Priorisation des correctifs par l'exploitation réelle.** Corriger d'abord ce qui se vend et s'exploite, plutôt que ce qui a le score le plus élevé (p. 4). *Inférence pour la veille :* c'est l'approche des catalogues de vulnérabilités activement exploitées, comme celui de la CISA, et un bon critère pour la rubrique Cyber / CTI du brief.

## Faits, opinions et interprétations

### Faits rapportés par la source

Le document rapporte des repères historiques (Silk Road et sa fermeture en 2013, la fuite d'Ashley Madison en 2015, WannaCry en 2017, Collection #1 en 2019, les fuites Conti en 2022, la saisie d'Hydra en 2022) et des chiffres : **1 milliard de dollars** en bitcoins saisis lors de la fermeture de Silk Road, **37 millions** de comptes Ashley Madison, **4 milliards de dollars** de dommages pour WannaCry, **773 millions** de combinaisons pour Collection #1, une commission RaaS de **20 à 30 %** et une grille de prix des données volées (p. 2). Il cite des outils et des cadres d'analyse existants (p. 3). Aucun de ces éléments n'est rattaché à une source dans le texte : ce sont des affirmations du document, dont plusieurs sont vérifiées, et parfois corrigées, dans la section externe.

### Opinions ou positions de l'auteur

L'auteur juge le rôle du dark web dans la cybersécurité impossible à surestimer (p. 1) et la DWTI devenue « urgente » (p. 5). Sa position la plus nette est une recommandation personnelle : il dit ne pas pouvoir recommander assez l'architecture Zero Trust (p. 4). Il prône aussi l'automatisation des réponses « sans délai humain » après une alerte (p. 4) et insiste sur le cadre éthique et juridique strict que doit respecter l'infiltration humaine des forums, sans le détailler (p. 4).

### Interprétations et inférences

L'auteur interprète l'essor des courtiers d'accès comme un signe avant-coureur des attaques par rançongiciel et l'IA criminelle comme un facteur de baisse du niveau de compétence requis (p. 4). Pour la présente analyse, le texte ressemble davantage à une **synthèse de cours** qu'à une contribution de recherche : il reprend des notions connues de la littérature professionnelle sans données nouvelles. Certaines tournures, comme « adventures » pour désigner des *exploits* ou « intel pathologies » (p. 2, 5), évoquent un passage par un outil de reformulation automatique ; c'est une hypothèse sur le mode de rédaction, qui invite à ne reprendre aucun chiffre sans vérification.

## Limites et points à vérifier

1. **Des références jamais appelées.** Les quinze références de la bibliographie, dont plusieurs sont solides (Moore et Rid, Holt, Europol, CrowdStrike), ne sont reliées à aucune affirmation du texte. Il est impossible de savoir d'où viennent les chiffres, les prix ou les faits historiques.
2. **Des faits historiques inexacts ou confondus.** Plusieurs données des tableaux ne résistent pas à la vérification : montant attribué à la saisie de Silk Road, mode de propagation de WannaCry, nature de Collection #1. Les tableaux ne peuvent donc pas servir de référence en l'état (détails dans la section externe).
3. **Des prix sans date ni source.** La grille de prix des données volées ne précise ni période, ni marché, ni méthode de relevé ; or ces prix varient fortement selon les années et les régions.
4. **Une formule de notation sans fondement.** Le score pondéré (crédibilité, pertinence, fraîcheur, caractère actionnable) n'est ni justifié, ni calibré, ni testé ; il reprend des critères connus sans montrer comment les mesurer.
5. **Un périmètre flou.** Le texte parle du dark web mais cite aussi des forums du web ouvert, des hébergeurs et Telegram, sans distinguer ces lieux ; certains incidents présentés comme liés au dark web ne le sont pas vraiment.
6. **Des affirmations sur les États sans preuve.** L'implication d'acteurs étatiques dans l'achat de *zero-days* ou de données de reconnaissance est affirmée « selon des services de renseignement » non cités (p. 2).
7. **Des enjeux juridiques et éthiques à peine évoqués.** L'infiltration de forums, l'achat de données volées ou le traitement de données personnelles issues de fuites posent des questions légales sérieuses, que l'article réduit à une mention d'un « cadre strict » (p. 4).
8. **Une qualité éditoriale faible.** Structure de sections décousue, tableaux désalignés, phrases parfois incohérentes et annexe rédigée comme une consigne au lecteur (p. 5) : autant d'indices d'une relecture insuffisante, qui fragilisent la confiance dans le fond.

## Sources et références mentionnées

La bibliographie compte quinze références (p. 5), plutôt de bonne tenue mais souvent anciennes : des travaux académiques sur les marchés du dark web et la confiance entre criminels (Moore et Rid, « Cryptopolitik and the Darknet », 2016 ; Holt et Lampke sur les marchés de données volées, 2010 ; Dupont sur la confiance entre pirates, 2016 ; Weimann sur la migration terroriste vers le dark web, 2016), des travaux d'informatique sur l'analyse automatisée des forums et la prédiction d'exploitation (DarkEmbed, 2018 ; AZSecure, 2016 ; Caines et al., 2018 ; Huang et al. sur le suivi des rançongiciels, 2018), et quelques documents institutionnels ou professionnels (MITRE ATT&CK, 2020 ; IOCTA d'Europol, 2023 ; Recorded Future, 2022 ; CrowdStrike, 2024). Le défaut tient moins à leur choix qu'à leur absence d'usage : aucune n'est citée à l'appui d'une affirmation précise.

## Cinq éléments essentiels à retenir

1. L'article propose une **introduction structurée** à la surveillance du dark web : infrastructure, activités criminelles, cadres d'analyse, outils, menaces et défenses.
2. Il décrit une **économie criminelle de services** (rançongiciel, accès initiaux, données volées, *zero-days*, cybercrime en tant que service) qui abaisse la barrière d'entrée des attaquants.
3. Il rattache la surveillance aux modèles connus (**Kill Chain, ATT&CK, modèle en diamant**) et recommande de l'intégrer aux outils de sécurité et à une architecture Zero Trust.
4. Ses **chiffres et faits ne sont pas sourcés** et plusieurs sont inexacts ; aucune donnée nouvelle, aucune évaluation d'outil n'est présentée.
5. À utiliser comme **plan de lecture et glossaire**, en s'appuyant pour les faits sur les rapports d'Europol, de Chainalysis ou des éditeurs cités dans la section suivante.

## État de l'art et regards extérieurs

Recherches effectuées le 2026-09-29. Les constats suivants complètent ou corrigent la lecture du PDF ; ils ne modifient pas les sections précédentes, fondées sur la seule source. Le document n'étant pas daté, les évolutions présentées sont les plus récentes connues.

### Travaux de référence

- **Le rapport européen de référence.** [Europol — « Steal, deal and repeat: How cybercriminals trade and exploit your data » (IOCTA 2025)](https://www.europol.europa.eu/publication-events/main-reports/steal-deal-and-repeat-how-cybercriminals-trade-and-exploit-your-data) (juin 2025) est l'évaluation annuelle de la menace cybercriminelle par Europol. Il fait des données volées la marchandise centrale de l'écosystème : collectées par hameçonnage, *vishing* et logiciels voleurs d'informations, revendues puis réutilisées de main en main, y compris par des courtiers d'accès initial qui vendent l'entrée dans des systèmes compromis. C'est la version sourcée et à jour du tableau que dresse l'article, qui cite l'édition 2023.
- **La mesure économique des marchés.** Le [rapport annuel de Chainalysis sur la criminalité liée aux cryptomonnaies (chapitre drogues et marchés du darknet)](https://www.chainalysis.com/blog/crypto-drug-sales-darknet-markets-2026/) (2026) chiffre les flux des marchés du darknet à partir de la chaîne de blocs. C'est l'outil que l'article cite pour le suivi des fonds, utilisé ici pour mesurer l'économie elle-même.
- **Le cadre juridique de la veille sur le dark web.** Le [département de la Justice américain — « Legal Considerations when Gathering Online Cyber Threat Intelligence and Purchasing Data from Illicit Sources »](https://www.justice.gov/criminal/criminal-ccips/page/file/1252341/dl?inline=) (2020) est le document de référence pour les entreprises qui surveillent ou infiltrent des forums criminels : ce qui est permis (pseudonyme, surveillance passive) et ce qui expose à des poursuites (identifiants volés, achats hasardeux). Il n'est pas contraignant et vaut pour le droit américain, mais il comble le silence de l'article sur ce point.

### Compléments sur le sujet

L'article décrit un dark web assez figé, centré sur les marchés en `.onion` et les grands noms des années 2010. Quatre dimensions récentes changent la lecture du sujet : l'économie réelle des marchés, le déplacement vers les messageries, l'efficacité mitigée des opérations policières, et l'industrialisation de la criminalité par l'IA.

- **Un marché de la drogue qui résiste, dominé par les russophones.** Selon Chainalysis, l'activité des marchés du darknet a atteint environ **2,6 milliards de dollars en 2025**, en hausse continue depuis 2022 malgré les fermetures successives ([Chainalysis — « Drugs and Darknet Markets: 2026 Crypto Crime Report »](https://www.chainalysis.com/blog/crypto-drug-sales-darknet-markets-2026/), 2026). Cinq grands marchés russophones issus de l'après-Hydra (Mega, Kraken, BlackSprut, OMG!OMG!, Nova) y concentrent l'essentiel des flux, et les marchés fonctionnent désormais en réseau mondial d'approvisionnement : quand l'un ferme, comme Abacus Market en juillet 2025, les vendeurs migrent vers un autre (ici TorZon). La saisie d'Hydra, citée par l'article comme succès de coopération, a donc surtout redistribué le marché.
- **Le crime se déplace vers Telegram, et y reste.** Après l'arrestation de son fondateur à Paris en août 2024, Telegram s'est engagé à transmettre numéros de téléphone et adresses IP aux autorités pour les enquêtes pénales ; il a répondu à 900 demandes américaines touchant 2 253 utilisateurs sur l'année 2024, contre 14 sur les neuf premiers mois ([CyberInsider — « Telegram Shared Data on 2,253 Users with U.S. Authorities in 2024 »](https://cyberinsider.com/telegram-shared-data-on-2253-users-with-u-s-authorities-in-2024/), 2025). Les criminels annonçaient un exode vers Signal, Discord ou Matrix, qui n'a pas eu lieu : selon KELA, plus de 246 000 liens vers des canaux Telegram circulent chaque mois dans les communautés cybercriminelles, contre 682 pour Signal et Discord réunis ([CyberInsider — « Telegram's Dominance in Cybercrime Persists Despite Policy Shift »](https://cyberinsider.com/telegrams-dominance-in-cybercrime-persists-despite-policy-shift/), 2025). Check Point constate en 2026 que ces communautés continuent de s'adapter ([Check Point Research — « Telegram's crackdown in 2026 and why cyber criminals are still winning »](https://blog.checkpoint.com/research/telegrams-crackdown-in-2026-and-why-cyber-criminals-are-still-winning/), 2026). Une veille « dark web » est aujourd'hui, pour une large part, une veille Telegram.
- **Des opérations policières qui frappent fort mais pas durablement.** Plusieurs coups majeurs ont visé exactement les maillons décrits par l'article. L'opération Cronos a démantelé l'infrastructure de LockBit le 20 février 2024 (34 serveurs saisis, clés de déchiffrement récupérées), mais le groupe est revenu en quelques jours ([National Crime Agency — « The NCA announces the disruption of LockBit with Operation Cronos »](https://www.nationalcrimeagency.gov.uk/the-nca-announces-the-disruption-of-lockbit-with-operation-cronos), février 2024). En mai 2025, Microsoft, le FBI et Europol ont saisi quelque 2 300 domaines de Lumma, le plus répandu des logiciels voleurs d'informations ([Europol — « Europol and Microsoft disrupt world's largest infostealer Lumma »](https://www.europol.europa.eu/media-press/newsroom/news/europol-and-microsoft-disrupt-world%E2%80%99s-largest-infostealer-lumma), mai 2025), qui s'est pourtant reconstitué depuis ; l'opération Endgame a visé la même année les logiciels d'accès initial ([Eurojust — « Operation Endgame continues »](https://www.eurojust.europa.eu/news/operation-endgame-continues-international-coalition-takes-malware-offline), 2025). En France, la brigade de lutte contre la cybercriminalité a interpellé en juin 2025 plusieurs administrateurs présumés de BreachForums, dont « ShinyHunters », « IntelBroker » ayant été arrêté en février ([The Record — « French police reportedly arrest suspected BreachForums administrators »](https://therecord.media/france-breachforums-suspects-arrests), juin 2025). Le schéma est constant : fermeture, dispersion, reconstitution.
- **L'IA industrialise l'attaque bien au-delà de WormGPT.** Le WormGPT d'origine a fermé dès août 2023 après l'identification de son créateur ; le nom est depuis devenu une marque pour des modèles détournés, comme deux variantes vendues sur BreachForums en 2024-2025 et construites sur Grok et Mixtral de Mistral AI par simple manipulation des instructions système ([Cato Networks — « WormGPT Variants Powered by Grok and Mixtral »](https://www.catonetworks.com/blog/cato-ctrl-wormgpt-variants-powered-by-grok-and-mixtral/), juin 2025). Le changement le plus net vient des agents d'IA légitimes. Anthropic a documenté en août 2025 un acteur qui a mené avec Claude Code une campagne d'extorsion contre au moins 17 organisations, de la reconnaissance jusqu'aux demandes de rançon personnalisées de 75 000 à plus de 500 000 dollars, et un criminel aux compétences limitées vendant des rançongiciels générés par IA ([Anthropic — « Detecting and countering misuse of AI: August 2025 »](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025), août 2025). Son rapport de septembre 2026 en tire la conséquence économique : en réduisant le temps et l'effort nécessaires, les agents rendent rentables des cibles jusqu'ici jugées secondaires ([Fortune — « AI could make more companies worth hacking, Anthropic report suggests »](https://fortune.com/2026/09/24/ai-could-make-more-companies-worth-hacking-anthropic-report-suggests/), 24 septembre 2026).

### Vérification des affirmations de la source

| Affirmation du document | Verdict | Source de la vérification |
|---|---|---|
| Fermeture de Silk Road en 2013 : 1 milliard de dollars en bitcoins confisqués (p. 2) | **Contredit.** Le milliard correspond à la saisie en 2020 de 69 370 bitcoins dérobés à Silk Road par un pirate (« Individual X »), valant environ 14 millions de dollars à l'époque du vol ; l'article confond deux épisodes | [Département de la Justice — « United States Files Civil Action To Forfeit Cryptocurrency Valued At Over One Billion »](https://www.justice.gov/usao-ndca/pr/united-states-files-civil-action-forfeit-cryptocurrency-valued-over-one-billion-us) (5 novembre 2020) |
| WannaCry « diffusé via le dark web » (p. 2) | **Contredit.** Le rançongiciel s'est propagé comme un ver en exploitant EternalBlue, outil de la NSA divulgué publiquement par les Shadow Brokers en avril 2017 ; Washington et Londres l'ont attribué au groupe nord-coréen Lazarus en décembre 2017 | [CyberScoop — « Mounting evidence points to North Korean group for global ransomware attack »](https://cyberscoop.com/wannacry-symantec-lazarus-group/) (2017) |
| Collection #1 : 773 millions de combinaisons courriel/mot de passe publiées sur le dark web (p. 2) | **Nuancé.** 773 millions d'adresses uniques et 21 millions de mots de passe uniques, soit plus d'un milliard de combinaisons, hébergés sur le service de fichiers MEGA et diffusés sur un forum de piratage ; il s'agit surtout d'une compilation de fuites antérieures | [Troy Hunt — « The 773 Million Record "Collection #1" Data Breach »](https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/) (janvier 2019) |
| Prix des données volées : fullz 10-50 $, dossiers médicaux 250-1 000 $, numéros de sécurité sociale 1-10 $ (p. 2) | **Nuancé.** Les relevés d'août 2025 donnent un ordre de grandeur voisin (fullz 20 à 100 $, dossier médical complet jusqu'à 500 $, numéro de sécurité sociale 1 à 6 $) ; l'offre surabondante fait baisser les données de masse, tandis qu'un accès administrateur de domaine dépasse plusieurs dizaines de milliers de dollars | [DeepStrike — « Dark Web Data Pricing 2025 »](https://deepstrike.io/blog/dark-web-data-pricing-2025) (août 2025) |
| WormGPT et FraudGPT, outils d'IA criminels (p. 4) | **Confirmé mais daté.** WormGPT a fermé en août 2023 ; le nom désigne depuis des modèles grand public détournés | [Cato Networks](https://www.catonetworks.com/blog/cato-ctrl-wormgpt-variants-powered-by-grok-and-mixtral/) (juin 2025) |
| La saisie d'Hydra en 2022 illustre l'efficacité de la coopération (p. 5) | **Nuancé.** La saisie a eu lieu, mais le marché russophone s'est reconstitué autour de nouveaux acteurs, qui traitent aujourd'hui l'essentiel des flux | [Chainalysis](https://www.chainalysis.com/blog/crypto-drug-sales-darknet-markets-2026/) (2026) |
| Les courtiers d'accès initial, maillon en forte croissance (p. 4) | **Confirmé.** Europol les classe parmi les préoccupations principales de 2025 | [Europol — IOCTA 2025](https://www.europol.europa.eu/publication-events/main-reports/steal-deal-and-repeat-how-cybercriminals-trade-and-exploit-your-data) (juin 2025) |

### Contrepoints et critiques

- **Le dark web n'est plus le centre de gravité.** L'article en fait le « centre de coordination » de la cybercriminalité ; les données de KELA sur Telegram et la place des forums du web ouvert comme BreachForums montrent que le commerce criminel s'est largement déplacé vers des espaces qui ne demandent pas Tor. Une stratégie de surveillance fondée sur les seuls services `.onion` sous-estime la menace.
- **Surveiller n'est pas sans risque juridique.** L'infiltration de forums et l'achat de données, que l'article évoque comme des pratiques normales de HUMINT, exposent les entreprises à des poursuites si elles utilisent des identifiants volés, achètent des données appartenant à des tiers ou financent indirectement des criminels ([département de la Justice américain](https://www.justice.gov/criminal/criminal-ccips/page/file/1252341/dl?inline=), 2020). Le même guide recommande de documenter le plan d'opération, de garder trace des activités menées et de fixer des « règles d'engagement » validées par un juriste, ce qui fait de la HUMINT cyber une activité encadrée plutôt qu'un simple outil de collecte.
- **Les démantèlements déplacent plus qu'ils ne suppriment.** Le retour de LockBit après Cronos, la reconstitution de Lumma et la redistribution du marché russophone après Hydra relativisent l'optimisme de l'article sur la coopération public-privé. Son vrai bénéfice est souvent le renseignement recueilli et l'effet de déstabilisation sur la confiance entre criminels, plus que la fermeture elle-même.

### Évolutions depuis la publication

Le document n'étant pas daté, cette section retient les évolutions les plus récentes connues au moment de l'analyse.

- **L'IA agentique change l'économie des attaques.** Le rapport de renseignement sur la menace publié par Anthropic en septembre 2026, qui couvre les abus détectés de décembre 2025 à août 2026, conclut que l'IA réduit fortement l'expertise et l'effort nécessaires, rendant « rentables » des organisations jusqu'ici épargnées faute d'intérêt financier suffisant ([Fortune](https://fortune.com/2026/09/24/ai-could-make-more-companies-worth-hacking-anthropic-report-suggests/), 24 septembre 2026). C'est une extension directe du constat de l'article sur la baisse de la barrière d'entrée.
- **Des marchés en hausse malgré la répression.** Les 2,6 milliards de dollars de flux mesurés par Chainalysis pour 2025 montrent que l'économie décrite par l'article s'est renforcée, non affaiblie.
- **Telegram sous pression mais toujours central.** L'année 2026 confirme que la coopération accrue de Telegram avec les autorités n'a pas vidé la plateforme de ses communautés criminelles ([Check Point Research](https://blog.checkpoint.com/research/telegrams-crackdown-in-2026-and-why-cyber-criminals-are-still-winning/), 2026).

### Cadre juridique et éthique

- **États-Unis — veille et achat de données.** Le guide du département de la Justice de 2020 admet l'usage d'un pseudonyme pour accéder à un forum illicite, mais pas l'emploi d'identifiants volés ni l'usurpation de l'identité d'un tiers ; racheter ses propres données volées expose peu, racheter celles d'autrui soulève d'autres questions ([département de la Justice](https://www.justice.gov/criminal/criminal-ccips/page/file/1252341/dl?inline=), 2020). Le document n'est pas contraignant et ne crée aucune immunité.
- **Union européenne et France — données personnelles issues de fuites.** Une donnée visible en ligne, y compris dans une fuite, reste une donnée personnelle : sa collecte et sa réutilisation exigent une base légale, une finalité définie et la minimisation des données ([CNIL — « Ouverture et réutilisation de données personnelles sur Internet »](https://www.cnil.fr/fr/ouverture-et-reutilisation-de-donnees-personnelles-sur-internet-la-cnil-publie-ses-recommandations), 12 juin 2024). Une plateforme de surveillance qui stocke des identifiants volés de salariés ou de clients entre dans ce cadre.
- **Plateformes — obligations de coopération.** L'engagement de Telegram, depuis septembre 2024, à transmettre numéros et adresses IP sur demande judiciaire illustre le nouveau levier des autorités sur les messageries utilisées par les criminels ([CyberInsider](https://cyberinsider.com/telegram-shared-data-on-2253-users-with-u-s-authorities-in-2024/), 2025).

### Pour aller plus loin

- [Europol — IOCTA 2025 « Steal, deal and repeat »](https://www.europol.europa.eu/publication-events/main-reports/steal-deal-and-repeat-how-cybercriminals-trade-and-exploit-your-data) (2025) : le panorama de référence de l'économie criminelle des données, à lire à la place des tableaux de l'article.
- [Chainalysis — marchés du darknet, rapport 2026](https://www.chainalysis.com/blog/crypto-drug-sales-darknet-markets-2026/) (2026) : les chiffres de l'économie réelle des marchés et de leurs migrations.
- [Département de la Justice — guide juridique de la veille sur les sources illicites](https://www.justice.gov/criminal/criminal-ccips/page/file/1252341/dl?inline=) (2020) : à lire avant toute démarche de HUMINT cyber.
- [Anthropic — « Detecting and countering misuse of AI: August 2025 »](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025) (2025) : des cas concrets d'attaques menées avec un agent d'IA.
- [Troy Hunt — analyse de Collection #1](https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/) (2019) : un modèle de vérification rigoureuse d'une fuite massive.
