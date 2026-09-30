---
title: PARTIE VI — DIMENSIONS AVANCÉES
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
chapter: 6
chapters: 7
---

---

## Chapitre 26 — Social engineering et IA : la révolution en cours

### 26.1 Le phishing AI-powered

Les LLM (Large Language Models) transforment le phishing de deux manières fondamentales. Premièrement, la personnalisation à l'échelle : un LLM peut générer des centaines d'emails de spear-phishing, chacun personnalisé à partir du profil OSINT de la cible (poste, entreprise, intérêts, publications récentes), dans n'importe quelle langue, avec une qualité linguistique indistinguable d'un email humain. La barrière d'entrée qui protégeait les cibles francophones (les phishings en mauvais français étaient faciles à détecter) a disparu. Deuxièmement, l'adaptation culturelle : le LLM adapte le registre, le ton et les conventions de communication au contexte culturel de la cible — un email de phishing destiné à un cadre allemand ne ressemblera pas à celui destiné à un ingénieur japonais.

Le rapport Unit 42 2025 confirme cette tendance : dans plusieurs investigations, les acteurs de la menace ont utilisé l'IA générative pour créer des leurres hautement personnalisés à partir d'informations publiques, avec un niveau de ton et de timing qui nécessitait auparavant un opérateur humain qualifié.

**Implications pour la défense** : les marqueurs linguistiques de phishing (fautes, registre inapproprié, formulations inhabituelles) ne sont plus des indicateurs fiables. La défense doit se reporter sur les indicateurs structurels (domaine d'expéditeur, headers, comportement de l'email) et les processus de vérification (callback, double validation).

### 26.2 Le vishing deepfake

Le clonage vocal en temps réel atteint en 2025 un niveau de maturité opérationnelle. Les plateformes comme ElevenLabs ou les modèles open source (XTTS, Bark) permettent de cloner une voix à partir d'échantillons audio courts (30 secondes à quelques minutes suffisent pour un clone de qualité acceptable). L'intégration en temps réel dans un appel téléphonique est techniquement possible avec une latence de quelques centaines de millisecondes — souvent indétectable sur un réseau téléphonique standard.

Les cas d'utilisation offensifs documentés incluent : fraude au président par deepfake vocal (l'attaquant clone la voix du DG à partir d'interviews publiques et appelle le DAF), confirmation téléphonique pour renforcer un BEC email (le « DG » rappelle pour confirmer son email de demande de virement), et vishing de helpdesk avec la voix d'un employé légitime.

**Détection** : les détecteurs de deepfake vocal sont en cours de développement mais restent peu fiables en conditions réelles (compression téléphonique, bruit ambiant, diversité des technologies de synthèse). La défense la plus efficace reste procédurale : pour toute demande sensible par téléphone, vérification out-of-band obligatoire (callback sur un autre canal, validation en personne, code de vérification préétabli).

### 26.3 La vidéo deepfake en temps réel

La visioconférence deepfake en temps réel a franchi le seuil de l'opérationnel. Le cas de Hong Kong (début 2024) — 25 millions de dollars volés via une visioconférence où plusieurs participants étaient des deepfakes — est le cas le plus médiatisé, mais d'autres cas moins spectaculaires ont été rapportés par des cabinets de réponse à incident.

En 2025, la génération vidéo deepfake en temps réel est accessible via des plateformes commerciales et des outils open source. La qualité est variable mais suffisante pour une visioconférence de résolution standard, en particulier si l'attaquant simule une connexion internet de mauvaise qualité (réduction de la résolution et du framerate, ce qui masque les artefacts).

**Défense** : demander à l'interlocuteur un geste imprévu (tourner la tête, montrer ses mains, placer un objet devant le visage) peut révéler les artefacts des deepfakes actuels — mais cette parade deviendra obsolète à mesure que la technologie progresse. La vérification d'identité multi-facteur (question de sécurité, code préétabli, confirmation par un second canal) reste la défense la plus robuste.

### 26.4 Les chatbots de social engineering

L'IA agentic appliquée au social engineering représente la prochaine frontière. Des agents conversationnels autonomes, capables de maintenir des conversations cohérentes sur des jours ou des semaines, de s'adapter au style de leur interlocuteur, de gérer les objections et de progresser méthodiquement vers un objectif (collecte d'identifiants, élicitation d'information, construction d'une relation de confiance), permettent le passage à l'échelle de techniques qui étaient auparavant limitées par la disponibilité d'opérateurs humains qualifiés.

Le rapport Unit 42 2025 identifie l'IA agentic comme une couche émergente dans le paysage des menaces, avec des systèmes capables d'exécuter de manière autonome des tâches en plusieurs étapes avec un minimum d'intervention humaine. Bien que l'adoption reste limitée à ce jour, les cas observés incluent la reconnaissance multi-plateforme automatisée et la distribution de messages coordonnée.

Les implications sont considérables pour les romance scams (un seul opérateur peut gérer des centaines de « relations » simultanées via des chatbots IA), pour l'élicitation (des agents conversationnels capables de mener des conversations d'élicitation structurées en salon professionnel virtuel), et pour le phishing conversationnel (des agents qui répondent aux questions de la cible et adaptent leur pretexte en temps réel).

### 26.5 La course aux armements

La défense face à la menace IA s'organise autour de trois axes : la détection (analyse comportementale des communications, détection d'anomalies dans le style d'écriture, détecteurs de deepfake audio et vidéo — tous avec des taux de faux positifs significatifs en 2025), les processus (vérification out-of-band, double validation, codes de confirmation préétablis — les défenses procédurales sont agnostiques à la technologie utilisée par l'attaquant), et la sensibilisation (former les employés à la réalité de la menace deepfake et IA, sans verser dans l'alarmisme — l'objectif est la vigilance, pas la paranoïa).

L'enjeu stratégique est que l'IA avantage structurellement l'attaquant : l'attaquant n'a besoin de réussir qu'une fois, tandis que le défenseur doit réussir à chaque fois. L'IA permet à l'attaquant de multiplier les tentatives avec une qualité constante et un coût marginal décroissant. La seule réponse durable est de construire des processus qui fonctionnent même quand la manipulation est parfaite — c'est-à-dire des processus qui ne reposent pas sur la capacité d'un individu isolé à détecter une tromperie.

---

## Chapitre 27 — Sécurité physique avancée : au-delà du badge

### 27.1 Les systèmes de contrôle d'accès en profondeur

**RFID basse fréquence (125 kHz).** Technologies HID ProxCard, EM4100 — largement déployées, facilement clonables. L'investissement minimal (Proxmark3 — environ 300 €, Flipper Zero — environ 200 €) permet le clonage en quelques secondes à une distance de quelques centimètres. Ces technologies ne devraient plus être utilisées pour le contrôle d'accès de zones sensibles, mais restent massivement déployées par inertie dans de nombreuses organisations.

**RFID haute fréquence (13.56 MHz).** MIFARE Classic (vulnérable — attaques connues sur le chiffrement Crypto-1), MIFARE DESFire EV2/EV3 (robuste — chiffrement AES 128 bits, authentification mutuelle), iCLASS Standard (vulnérable), iCLASS SE/SEOS (robuste). La migration vers DESFire EV2+ ou SEOS est la recommandation de référence pour les organisations à risque élevé.

**Badges mobiles (NFC/BLE).** Apple Wallet, Google Wallet, applications dédiées (HID Mobile Access, SALTO JustIN) — protégés par la cryptographie du smartphone (enclave sécurisée), résistants au clonage à distance. L'avantage opérationnel est considérable : révocation à distance (en cas de perte ou de départ), provisioning sans contact physique, audit détaillé des accès. Les inconvénients : dépendance au smartphone (batterie, panne), compatibilité variable entre les fabricants de téléphones et les systèmes de contrôle d'accès, et le fait que certains sites sensibles interdisent les smartphones.

**Biométrie.** Empreintes digitales, reconnaissance faciale, reconnaissance de l'iris — offrent un facteur d'authentification non transférable (en théorie). En pratique, les systèmes biométriques ont des taux de faux rejet (l'employé légitime est refusé — frustration et contournement) et de faux acceptation (un attaquant est accepté — plus rare mais possible avec des attaques de présentation). Les considérations RGPD sont significatives : les données biométriques sont des données sensibles qui nécessitent une base légale spécifique et une analyse d'impact.

### 27.2 Le crochetage et le bypass physique

Dans le cadre d'un red team autorisé, les techniques de bypass physique complètent le social engineering quand l'accès par manipulation humaine échoue ou n'est pas applicable.

**Lock picking.** Le crochetage de serrures à goupilles standard est une compétence de base du red teamer physique. Les serrures à goupilles standard (cylindres européens de base) peuvent être crochetées en quelques minutes avec un jeu de crochets (tension wrench + pick). Les serrures haute sécurité (Abloy, Mul-T-Lock, Medeco) sont significativement plus résistantes et nécessitent des compétences et du matériel spécialisés.

**Bypass de serrures électriques.** Les serrures électriques à ventouse (maglocks) peuvent souvent être contournées en passant un objet fin (shim card) entre la porte et le cadre pour actionner le capteur de demande de sortie (REX — Request to Exit). Les serrures à gâche électrique sont vulnérables à des techniques similaires si elles sont en mode « fail-safe » (déverrouillées en cas de coupure de courant).

**Les faiblesses architecturales.** Faux plafonds (passage entre deux pièces par le plénum), gaines techniques (passage par les conduits de câblage ou de ventilation), fenêtres non verrouillées aux étages supérieurs, cloisons légères (certaines cloisons de bureau sont en plaque de plâtre et peuvent être traversées). Un audit de sécurité physique sérieux inclut l'évaluation de ces vecteurs.

### 27.3 Les implants physiques

Les implants physiques sont des dispositifs matériels déployés par le red teamer pour maintenir un accès persistant après l'intrusion physique.

**Clé USB drop.** Rubber Ducky (émule un clavier et exécute des commandes en quelques secondes), Bash Bunny (multi-payload, émulation de périphériques multiples), O.MG Cable (câble USB avec implant intégré — visuellement indistinguable d'un câble normal). En contexte offensif, la clé USB est déposée dans un lieu où elle sera trouvée et branchée (parking, accueil, salle de réunion) — le baiting exploite la curiosité.

**Implant réseau.** LAN Turtle (implant réseau passif se branchant sur un port Ethernet — fournit un accès distant au réseau interne), rogue access point WiFi (Raspberry Pi ou device dédié émettant un réseau WiFi qui capture les connections ou fournit un accès au réseau filaire), keylogger hardware (se place entre le clavier et le port USB — capture toutes les frappes).

La documentation de chaque implant déployé (localisation, horodatage, durée de présence, données collectées) est une obligation du rapport de red team. Tous les implants doivent être retirés à la fin du test — un implant oublié constitue une vulnérabilité réelle.

### 27.4 Conception d'un site résistant au social engineering physique

La sécurité physique contre le social engineering se conçoit dès l'architecture du site, pas comme un ajout après coup.

**Flux de circulation.** Les visiteurs et les prestataires doivent emprunter des circuits distincts des employés, avec accompagnement systématique. Les zones sensibles (R&D, salle serveur, direction) doivent être physiquement séparées des zones communes (accueil, réfectoire, salles de réunion visiteurs) avec un contrôle d'accès intermédiaire.

**Zone d'accueil comme sas de sécurité.** L'accueil ne doit pas être une simple réception — c'est un sas de sécurité qui vérifie l'identité, contacte l'hôte, émet le badge visiteur et assure l'accompagnement. Le gardien/réceptionniste doit être formé au contre-social engineering (détection des pretextes, refus poli, procédure d'escalade).

**Surveillance intégrée.** Caméras aux points d'accès et de circulation, avec monitoring en direct (pas seulement enregistrement). Détection d'anomalies (accès en horaires inhabituels, badge utilisé simultanément à deux endroits, tentatives d'accès répétées échouées).

---

## Chapitre 28 — Élicitation, investigation et contre-ingérence : usages encadrés et expertise

### 28.1 L'élicitation comme outil d'investigation

Les techniques d'élicitation ne sont pas réservées aux attaquants et aux services de renseignement. Elles sont utilisées légalement dans de nombreux contextes professionnels.

**Les enquêteurs privés** utilisent l'élicitation dans le cadre d'investigations autorisées (fraude interne, compliance, due diligence). Le cadre juridique est strict : l'enquêteur ne peut pas usurper une identité officielle (force de l'ordre, administration), ne peut pas recourir à la contrainte, et doit respecter la vie privée. Les techniques d'élicitation conversationnelle (questions ouvertes, partage réciproque, silence stratégique) sont permises tant qu'elles ne constituent pas un stratagème déloyal au sens de la jurisprudence.

**Les journalistes d'investigation** utilisent des techniques proches de l'élicitation pour obtenir des informations de sources. Le droit français protège le secret des sources journalistiques, ce qui crée un cadre juridique spécifique.

**Les compliance officers** utilisent l'entretien structuré (distinct de l'élicitation — l'entretien est consenti et identifié) dans le cadre d'enquêtes internes sur des suspicions de fraude, de corruption ou de violation de conformité.

### 28.2 Le pretexting dans les enquêtes : cadre légal

Le pretexting — l'utilisation d'un faux pretexte pour obtenir des informations — est juridiquement encadré de manière stricte.

En France, la fabrication et l'utilisation de faux documents sont des infractions pénales (art. 441-1 et suivants du Code pénal). L'usurpation d'identité est un délit (art. 226-4-1). L'enregistrement d'une conversation sans le consentement des participants est interdit (art. 226-1). Ces restrictions limitent significativement les techniques disponibles pour les enquêteurs privés et les compliance officers par rapport aux pratiques anglo-saxonnes (aux États-Unis, le pretexting est plus largement toléré dans certains contextes d'investigation).

Le red team autorisé par lettre de mission constitue une exception encadrée : le pretexting est autorisé dans le cadre et les limites définis par la lettre de mission, qui vaut consentement de l'employeur. Mais cette autorisation ne couvre que les interactions avec les employés de l'organisation mandataire, pas avec des tiers (prestataires, visiteurs, voisins).

### 28.3 Investigation sur les arnaques de social engineering

L'investigation post-incident sur une arnaque de social engineering combine analyse technique et analyse relationnelle.

**Analyse technique.** Forensique email (headers, infrastructure de phishing — domaines, hébergement, certificats), analyse de la landing page (code source, exfiltration des données), traçage des flux financiers (pour le BEC — les fonds transitent typiquement par plusieurs comptes avant d'être convertis en crypto-monnaie ou retirés en liquide).

**Analyse OSINT.** Investigation sur les éléments identifiants de l'attaquant : numéros de téléphone (opérateur, géolocalisation), domaines (Whois, historique DNS, hébergement), profils en ligne (analyse de la fabrication des faux profils, recherche d'image inversée), et croisement avec les bases de données d'incidents connus.

**Coopération.** Avec les plateformes (signalement des faux profils, demande de désactivation), avec les banques (gel de fonds, traçage des virements), avec les forces de l'ordre (dépôt de plainte, transmission des éléments techniques), et avec les agences de renseignement si l'incident relève de l'ingérence étrangère (DGSI en France).

### 28.4 L'entretien et l'interrogatoire

Les techniques d'entretien professionnel (modèle PEACE — Preparation and Planning, Engage and Explain, Account, Closure, Evaluate) et l'entretien cognitif sont des outils d'investigation légaux distincts de l'élicitation.

La différence fondamentale : l'entretien est consenti et identifié (la personne sait qu'elle est interrogée et accepte de répondre), l'élicitation est clandestine (la personne ne sait pas qu'elle est interrogée). Cette distinction a des implications juridiques et éthiques majeures.

Le modèle PEACE, développé au Royaume-Uni, privilégie la collecte d'un récit libre (laisser le sujet raconter sa version sans interruption), la recherche de précisions par des questions non suggestives, et l'identification des incohérences par recoupement — plutôt que la confrontation directe ou les techniques d'interrogatoire agressives (qui produisent des faux aveux et des informations peu fiables).

### 28.5 Le témoignage de l'expert

L'expert en social engineering peut être amené à intervenir dans un cadre judiciaire : rapport d'expertise (analyse technique d'une arnaque, évaluation de la sophistication de l'attaque, évaluation de la responsabilité de la victime), expertise judiciaire (désigné par un tribunal pour éclairer une décision de justice), et contre-expertise (analyse critique d'un rapport d'expertise adverse).

L'expert doit être capable d'expliquer des concepts techniques complexes (phishing, deepfake, élicitation) à un public non technique (magistrats, jurés) de manière claire, rigoureuse et neutre. La crédibilité de l'expert repose sur ses qualifications, son expérience, la rigueur de sa méthodologie et sa capacité à distinguer fait établi, hypothèse probable et piste exploratoire.

---
