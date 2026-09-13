---
title: "Analyse — Recommandations de sécurité pour un système d’IA générative"
date: 2026-09-05
kind: analysis
---
# Analyse — *Recommandations de sécurité pour un système d’IA générative*

> **Convention :** **[Source]** = information explicitement présentée dans le guide ; **[Position de l’ANSSI]** = recommandation, appréciation ou principe de précaution formulé par l’ANSSI ; **[Analyse]** = interprétation produite dans la présente analyse. Les éléments cités sont rapportés d’après le document et n’ont pas été vérifiés indépendamment.

## Métadonnées

- **Titre :** *Recommandations de sécurité pour un système d’IA générative*
- **Sous-titre :** aucun sous-titre distinct indiqué ; document présenté comme un « Guide ANSSI ».
- **Auteur institutionnel :** Agence nationale de la sécurité des systèmes d’information (ANSSI). Aucun auteur individuel n’est indiqué.
- **Référence :** ANSSI-PA-102, version 1.0.
- **Date de publication :** 29 avril 2024 ; dépôt légal en avril 2024.
- **Source / support :** guide institutionnel téléchargeable sur `cyber.gouv.fr`, sous Licence Ouverte v2.0 (Étalab).
- **ISBN :** 978-2-11-167156-0 (papier) ; 978-2-11-167157-7 (numérique).
- **Public visé :** développeurs, administrateurs, RSSI, DSI et utilisateurs.
- **Thématique principale :** sécurisation du cycle de vie et de l’intégration dans un système d’information des systèmes d’IA générative reposant sur des grands modèles de langage (LLM).
- **Périmètre :** synthèse ou résumé documentaire, extraction d’informations et génération de texte, agents conversationnels et génération de code ; entrées éventuellement multimodales, mais sortie principalement textuelle.

## Résumé exécutif

**[Source]** Le guide propose un cadre de cybersécurité pour les systèmes d’IA générative fondés sur des LLM, à destination des organisations publiques et privées. Il décrit un cycle de vie en trois phases — entraînement, déploiement et production — et considère qu’un système d’IA doit d’abord recevoir le socle de sécurité d’une application métier classique, complété par des mesures propres aux modèles génératifs, à leurs données et à leurs interactions.

**[Source]** Les menaces spécifiques sont regroupées en trois familles : manipulation du comportement par des requêtes malveillantes, infection du système ou des données pendant l’entraînement, et exfiltration des données ou des paramètres du modèle. Elles affectent la confidentialité, l’intégrité, la disponibilité et la traçabilité. Le document illustre aussi les risques de chaîne d’approvisionnement, d’empoisonnement des données, de porte dérobée, d’injection indirecte de requête, de latéralisation vers le SI et de vulnérabilités introduites dans du code généré.

**[Position de l’ANSSI]** La sécurité doit être intégrée dès la conception et dans chaque phase. Le choix d’hébergement et le partage des responsabilités doivent dépendre de la sensibilité des données et de la criticité métier. L’ANSSI place la protection des données au centre : un modèle hérite de la sensibilité de ses données d’entraînement, peut en « régurgiter » une partie, et ne permet pas d’appliquer directement des droits d’accès à ce qu’il a appris. Le besoin d’en connaître doit donc orienter le choix entre données d’entraînement et données additionnelles accessibles en production.

**[Position de l’ANSSI]** Le guide adopte un principe de maîtrise humaine : une IA générative, en raison de son non-déterminisme et de ses hallucinations possibles, ne doit pas exécuter automatiquement des actions critiques sur le métier ou l’infrastructure. Les interactions avec des applications et des plugins doivent être limitées, filtrées, authentifiées, autorisées et journalisées. Les entrées non maîtrisées, notamment les contenus Internet ou les courriels, ne doivent pas pouvoir déclencher librement des actions sur le SI.

**[Source]** Les 35 recommandations couvrent l’analyse de risque, la sécurité de la chaîne logicielle et des données, le cloisonnement, les accès privilégiés, l’hébergement de confiance, la résilience, les GPU, l’entraînement et le ré-entraînement, les audits avant production, le filtrage des entrées et sorties, les interconnexions, la journalisation, la génération de code, les services publics sur Internet et le recours à des prestataires tiers.

**[Analyse]** Ce guide mérite l’attention parce qu’il transpose les fondamentaux de la cybersécurité à l’IA sans présenter celle-ci comme un objet isolé. Son apport le plus structurant est de traiter ensemble le modèle, les données, la chaîne de développement, les identités, l’hébergement et les applications interconnectées. Il fournit une base concrète pour une architecture et une gouvernance de sécurité, mais pas une norme, une procédure exhaustive de conformité ni une méthode quantitative permettant de mesurer la robustesse d’un LLM.

## Chronologie

La séquence utile à la compréhension est celle du cycle de vie, cyclique plutôt qu’historique :

1. **Entraînement :** sélection et préparation des données, construction ou adaptation du modèle, fine-tuning et alignement. Cette phase concentre notamment les risques d’empoisonnement, de fuite des données et de compromission de la chaîne logicielle.
2. **Déploiement :** intégration, tests fonctionnels et de sécurité, puis transfert contrôlé vers la production au moyen d’un environnement et de chaînes CI/CD sécurisés.
3. **Production :** accès des utilisateurs au système, traitement des requêtes, consultation éventuelle de données additionnelles ou de plugins, filtrage des sorties et journalisation.
4. **Ré-entraînement :** lorsqu’il est nécessaire, il doit relancer le cycle dans les environnements dédiés ; l’ANSSI recommande de ne pas ajuster continuellement le modèle directement en production.

**[Source]** Ces phases peuvent être confiées à des acteurs et hébergées dans des environnements différents. Le guide demande donc d’adapter les mesures au partage réel des responsabilités et aux interactions internes ou externes du projet.

## Thèse principale

**[Position de l’ANSSI]** Un système d’IA générative doit être sécurisé comme un système d’information complet, sur l’ensemble de son cycle de vie et en fonction du risque, et non comme un modèle autonome. Les propriétés des LLM — données d’entraînement difficilement dissociables du modèle, sorties non déterministes, hallucinations, attaques adverses et connexions à des ressources externes — rendent indispensables la défense en profondeur, le cloisonnement, la traçabilité, la protection des données et le contrôle humain des actions critiques.

Cette position repose sur cinq principes :

1. **Sécurité dès la conception :** analyse de risque, DevSecOps et cartographie des composants, données, responsabilités et flux avant l’entraînement.
2. **Sensibilité héritée :** le modèle doit être protégé au niveau des données utilisées pour sa conception et son entraînement.
3. **Moindre privilège et cloisonnement :** séparer phases, environnements, comptes, secrets, stockages et zones réseau, puis limiter chaque interaction au besoin opérationnel.
4. **Maîtrise humaine :** proscrire l’autonomie sur les décisions ou actions critiques, et soumettre le code généré ainsi que les réponses sensibles à des contrôles.
5. **Méfiance envers les tiers non maîtrisés :** évaluer bibliothèques, jeux de données, modèles, hébergeurs et services ; ne jamais soumettre de données sensibles à un outil grand public sur Internet.

## Informations et arguments importants

### Périmètre et architecture considérés

**[Source]** Le guide distingue le **modèle d’IA** — réseau de neurones et paramètres tels que poids et biais — du **système d’IA**, qui comprend son implémentation, les services frontaux, bases de données, journaux et autres composants applicatifs. Cette distinction justifie que l’analyse de sécurité dépasse le seul comportement du LLM.

**[Source]** L’architecture générique comprend différentes populations d’accès (utilisateurs, développeurs, administrateurs, auditeurs), une base vectorielle servant à enrichir les requêtes dans une approche RAG, des filtres en entrée et en sortie, ainsi que des plugins ou composants reliant le système à des ressources métier et techniques. Ces éléments constituent autant de frontières de confiance et de chemins d’attaque.

**[Source]** Le document exclut de son champ la qualité métier des données et la performance du modèle. Il ne traite pas non plus en profondeur de l’éthique, de la propriété intellectuelle, du secret des affaires, de la vie privée ou de la protection des données personnelles, qu’il renvoie notamment aux travaux de l’ENISA, du BSI, du NIST et de la CNIL. Certaines recommandations touchent néanmoins à ces sujets lorsqu’ils ont une incidence directe sur la sécurité.

### Menaces et impacts

**[Source]** Les attaques sont organisées en trois catégories :

- **manipulation :** requêtes malveillantes destinées à détourner le comportement, provoquer des actions dangereuses, des réponses inattendues ou un déni de service ;
- **infection :** altération des données d’entraînement, insertion d’une porte dérobée ou compromission d’un élément de la chaîne de développement ;
- **exfiltration :** extraction des données d’entraînement, des requêtes d’autres utilisateurs, de données additionnelles ou des paramètres internes du modèle.

**[Source]** Six chemins d’attaque sont illustrés : empoisonnement d’une source de données ; porte dérobée depuis l’environnement de développement ; détournement d’un service externe de test ; attaque adverse contre le modèle en production ; réponse malveillante issue d’une ressource externe ; commande injectée via un plugin vers une application métier.

**[Source]** Les conséquences envisagées sont l’atteinte à la réputation d’un service public, l’exfiltration de données sensibles, le vol des poids d’un modèle propriétaire, la latéralisation vers des applications métier et le sabotage d’une application au moyen de vulnérabilités dans du code généré. La traçabilité est incluse parmi les besoins de sécurité afin de soutenir l’explicabilité, l’imputabilité et l’investigation après incident.

### Recommandations générales : R1 à R17

- **R1 — Sécurité sur tout le cycle de vie :** identifier et appliquer des mesures spécifiques aux phases d’entraînement, de déploiement et de production, en tenant compte de la sous-traitance et des interconnexions.
- **R2 — Analyse de risque précoce :** avant l’entraînement, cartographier bibliothèques, sources de données et applications reliées ; localiser le traitement des données de l’organisation ; attribuer les responsabilités ; évaluer les impacts des réponses erronées ou malveillantes ; protéger les données d’entraînement. EBIOS Risk Manager est cité comme méthode possible.
- **R3 — Composants externes :** inventorier bibliothèques et modules tiers et évaluer leur niveau de confiance pour réduire le risque de chaîne d’approvisionnement.
- **R4 — Sources externes :** cartographier et évaluer les jeux d’entraînement, de validation et les données additionnelles que l’entité ne maîtrise pas.
- **R5 — DevSecOps :** sécuriser et durcir les chaînes CI/CD avec le moindre privilège ; gérer les secrets ; automatiser les analyses statiques et dynamiques ; protéger le code par authentification multifacteur, signature et droits d’accès ; employer des langages sécurisés.
- **R6 — Formats de modèles :** privilégier des formats séparant strictement paramètres et code, comme `safetensor` selon le document, et proscrire les formats peu sûrs tels que `pickle`, susceptibles d’exécuter du code lors de la désérialisation.
- **R7 — Confidentialité dès la conception :** cartographier tous les jeux de données des trois phases, y compris requêtes et réponses en production, et éventuellement les paramètres du modèle propriétaire.
- **R8 — Besoin d’en connaître :** décider quelles informations peuvent entrer dans l’entraînement, où des droits individuels ne peuvent plus être appliqués, et lesquelles doivent rester des données additionnelles protégées par rôles ; définir les données et moments de chaque ré-entraînement.
- **R9 — Actions critiques :** empêcher l’exécution automatique d’actions à fort impact métier, humain ou technique, telles que transactions bancaires, publication, création de comptes privilégiés, règles de pare-feu ou déploiement de serveurs.
- **R10 — Accès privilégiés :** définir et faire valider les opérations sensibles ; employer des comptes et postes d’administration dédiés ; appliquer le moindre privilège et privilégier des jetons temporaires ; protéger le développement au même niveau que la production.
- **R11 — Hébergement de confiance :** choisir, à chacune des phases, un environnement adapté aux besoins de confidentialité et d’intégrité, notamment pour les données d’entraînement au repos, en transit et en traitement.
- **R12 — Séparation des phases :** cloisonner entraînement, déploiement et production aux niveaux réseau, système, stockage, comptes et secrets afin de réduire la latéralisation.
- **R13 — Exposition à Internet :** placer le service derrière une passerelle sécurisée comprenant un reverse proxy et deux zones de filtrage ; ne pas exposer l’annuaire interne ; éviter de mutualiser sur un même hyperviseur les fonctions de sécurité distinctes.
- **R14 — Cloud public :** privilégier une offre qualifiée SecNumCloud si les données sont sensibles, si l’impact métier est critique ou si les utilisateurs ne sont pas de confiance.
- **R15 — Résilience :** prévoir un mode dégradé ou, au minimum, une procédure permettant de contourner l’IA pour maintenir le service métier.
- **R16 — GPU :** dédier les GPU au système d’IA ; en environnement virtualisé, dédier les hyperviseurs concernés ou appliquer au minimum un filtrage matériel tel qu’un IOMMU. Plusieurs modèles peuvent partager les GPU s’ils ont une sensibilité et des besoins homogènes.
- **R17 — Canaux auxiliaires :** considérer les fuites ou perturbations fondées sur le temps d’exécution, la consommation ou d’autres signaux, qui peuvent notamment aider à reconstruire une réponse.

### Données et besoin d’en connaître

**[Source]** Les données sont multiples, volumineuses, régulièrement actualisées, parfois prétraitées pour réduire leur sensibilité et employées à plusieurs phases. Elles incluent les corpus d’entraînement, les jeux de test, les données additionnelles, les requêtes des utilisateurs et les réponses. Le guide considère qu’un modèle hérite de la sensibilité des informations qui l’ont entraîné ou ré-entraîné, car il peut générer des réponses proches de celles-ci.

**[Source]** Trois situations sont distinguées : les données d’entraînement, sur lesquelles des droits par utilisateur ne peuvent pas être appliqués dans le réseau neuronal ; les données additionnelles de production, pour lesquelles un contrôle par rôles peut être mis en œuvre selon les outils ; et les données d’usage, qui peuvent être sensibles, sont au moins temporairement traitées et peuvent servir à un ré-entraînement ou à un alignement par RLHF.

**[Position de l’ANSSI]** L’anonymisation ou les données synthétiques ne constituent pas une garantie absolue : inférence d’attribut ou d’appartenance et recoupement avec d’autres sources peuvent permettre de retrouver l’information initiale. Lors d’une sous-traitance, l’organisation doit examiner chiffrement, cloisonnement entre clients, gestion des clés et effacement lors de la réallocation des ressources.

### Entraînement : R18 à R21

- **R18 — Légitimité d’accès :** entraîner le modèle uniquement avec des données dont la sensibilité correspond au besoin d’en connaître de tous ses utilisateurs.
- **R19 — Intégrité des données :** vérifier pendant tout le cycle d’entraînement les signatures ou empreintes des fichiers ou archives de données.
- **R20 — Intégrité du système :** contrôler celle des paramètres du modèle, scripts, binaires et autres fichiers nécessaires au fonctionnement.
- **R21 — Pas de ré-entraînement en production :** éviter l’apprentissage continu à partir des entrées courantes ; repartir dans le cycle à trois phases avec des jeux sélectionnés et testés. Le guide admet des déclenchements récurrents, par seuil de performance, par obsolescence des données ou à la demande, mais dans l’environnement prévu.

### Déploiement : R22 à R24

- **R22 — Chaîne de déploiement :** opérer le passage en production depuis un système d’administration et des postes dédiés et durcis, au moyen de CI/CD maîtrisées.
- **R23 — Audits de sécurité :** avant la production, combiner tests d’intrusion classiques, SAST/DAST, tests automatisés propres aux modèles (attaques adverses, extraction) et examens manuels de scénarios sophistiqués. Le recours à un prestataire PASSI est mentionné.
- **R24 — Tests fonctionnels :** mesurer performance et qualité des réponses avant déploiement et, si pertinent, en continu afin de repérer plus tôt les dysfonctionnements.

### Production : R25 à R29

- **R25 — Filtres d’entrée et de sortie :** filtrer les requêtes malveillantes ou non légitimes ; retirer des réponses les paramètres, mécanismes internes et informations sensibles ; limiter éventuellement la longueur des sorties. Les réponses devraient être simples et ne pas révéler des vecteurs de score internes.
- **R26 — Interactions métier :** documenter et valider tous les flux ; les filtrer, chiffrer et authentifier ; employer des protocoles sécurisés comme OpenID Connect ; vérifier l’autorisation en plus de l’identité ; journaliser avec une granularité adaptée.
- **R27 — Entrées non maîtrisées :** limiter fortement, voire proscrire, les actions automatiques déclenchées à partir de pages Web, courriels ou autres contenus externes, en raison notamment de l’injection indirecte de requête.
- **R28 — Cloisonnement en production :** placer le système dans une ou plusieurs zones logiques dédiées, selon sa criticité, pour contenir une compromission.
- **R29 — Journalisation :** enregistrer les requêtes utilisateur, leur transformation avant le modèle, les appels aux plugins et aux données additionnelles, les filtres de sortie et les réponses. Les journaux contenant des données personnelles ou sensibles doivent eux-mêmes être protégés et respecter les exigences de conservation applicables.

### Génération de code : R30 à R32

- **R30 — Contrôle systématique :** ne pas exécuter ni committer automatiquement le code généré ; intégrer des outils d’assainissement et d’analyse ; vérifier les bibliothèques suggérées ; organiser des revues humaines régulières avec des requêtes types suffisamment élaborées.
- **R31 — Modules critiques :** ne pas générer par IA des blocs complets destinés à la cryptographie, à la gestion des droits d’accès ou au traitement de données sensibles.
- **R32 — Sensibilisation :** former les développeurs aux risques et aux outils d’analyse, ainsi qu’à la formulation de requêtes susceptible d’améliorer la qualité et la sécurité. Le guide évoque aussi un alignement empêchant la génération volontaire de code malveillant.

### Services grand public exposés : R33

**[Source]** L’exposition publique augmente notamment les risques de déni de service, de fuite, d’abus et d’atteinte à la réputation.

- **R33 — Durcissement :** entraîner le modèle seulement sur des données publiques ; authentifier les utilisateurs ; analyser toutes les requêtes ; contrôler et valider les réponses ; protéger les historiques ; prévoir une défense contre les DDoS ; sécuriser le frontal Web.

### Services d’IA tiers : R34 et R35

**[Source]** Envoyer texte, image ou document à un service d’IA tiers revient à remettre ces informations à l’espace de traitement du prestataire. L’organisation ne maîtrise ni le cloisonnement entre clients ni la confidentialité et dépend des garanties contractuelles et techniques de celui-ci. Le guide cite ChatGPT, Gemini, Copilot, DeepL et Perplexity comme exemples de services grand public.

- **R34 — Données sensibles :** ne jamais inclure dans un service grand public des informations de Diffusion Restreinte ou classifiées, des recherches relevant de la protection du potentiel scientifique et technique, des données personnelles, contractuelles, juridiques ou financières, ni des secrets comme mots de passe et clés d’API. Cette règle couvre également la création de données synthétiques et le fine-tuning par un service externe.
- **R35 — Droits des connecteurs :** vérifier les autorisations d’un outil d’IA sur les courriels, espaces documentaires, dépôts de code et services de réunion dès son activation, puis régulièrement — le guide donne une revue mensuelle comme exemple — car les mises à jour peuvent modifier les accès.

## Points particulièrement intéressants pour la veille

- **[Analyse] L’IA comme système, non comme modèle :** la surface de risque inclut RAG, base vectorielle, filtres, plugins, CI/CD, identité, journaux, GPU et prestataires. Une veille limitée aux vulnérabilités du LLM manquerait une part essentielle du risque opérationnel.
- **[Analyse] Le modèle comme dérivé sensible des données :** la classification des corpus devrait se propager au modèle entraîné et à ses sauvegardes. Cela affecte directement hébergement, partage, téléchargement et déploiement en périphérie.
- **[Analyse] Arbitrage entraînement contre RAG :** intégrer une donnée au modèle rend difficile le contrôle fin des accès ; la conserver comme donnée additionnelle peut préserver un RBAC. Le choix d’architecture devient donc une décision de sécurité et pas seulement de performance.
- **[Analyse] Injection indirecte et agentification :** plus un système consulte des contenus externes et dispose d’outils d’action, plus une donnée devient potentiellement une instruction. R9, R26 et R27 préfigurent les enjeux de sécurité des agents connectés au SI.
- **[Analyse] Gouvernance du ré-entraînement :** interdire l’apprentissage direct en production transforme chaque mise à jour du modèle en changement contrôlé, testable et traçable. La dérive et l’amélioration continue doivent alors être gérées par une boucle hors ligne formalisée.
- **[Analyse] Sécurité matérielle :** la recommandation de dédier les GPU et de considérer les canaux auxiliaires rappelle que la confidentialité ne se limite ni aux API ni aux fichiers de poids ; la mémoire des accélérateurs et leur mutualisation font partie du modèle de menace.
- **[Analyse] Journalisation à double tranchant :** une trace complète est nécessaire à l’investigation, mais elle agrège précisément des requêtes, réponses et contextes susceptibles d’être sensibles. Le stockage des journaux devient donc lui-même un actif critique.
- **[Analyse] Code généré comme apport non fiable :** le guide traite implicitement le code de l’IA comme une contribution externe à inspecter, et refuse à la fois son exécution et son commit automatiques. Ce principe peut servir de garde-fou générique dans les workflows agentiques de développement.
- **[Analyse] Dépendance et continuité :** l’exigence d’un mode dégradé sans IA indique que l’adoption d’une IA ne doit pas supprimer immédiatement les procédures métier alternatives ni créer un point unique de défaillance.
- **[Analyse] Contrôle continu des droits SaaS :** la revue des permissions après chaque évolution d’un produit est un signal important pour la gouvernance des assistants intégrés aux suites bureautiques et dépôts de code.
- **[Analyse] Évolution à surveiller :** le guide est daté d’avril 2024 et se déclare adapté aux menaces connues à cette date. Les taxonomies d’attaque, capacités agentiques, pratiques de filtrage, qualifications Cloud et règles applicables devront être confrontées à des versions ultérieures avant emploi comme référentiel courant.

## Faits, opinions et interprétations

### Faits rapportés par la source

- Le document est un guide ANSSI référencé ANSSI-PA-102, version 1.0 du 29 avril 2024, publié sous Licence Ouverte v2.0.
- Il comporte 35 recommandations et organise le cycle de vie en trois phases : entraînement, déploiement et production.
- Il décrit trois catégories d’attaques — manipulation, infection et exfiltration — et quatre besoins de sécurité — confidentialité, intégrité, disponibilité et traçabilité.
- Son architecture générique comprend notamment un frontal, un modèle, des filtres, une base vectorielle pour le RAG, des plugins, des données additionnelles et différents profils d’accès.
- Il cite les phénomènes de régurgitation, hallucination, empoisonnement, injection indirecte, extraction ou inversion du modèle, inférence d’appartenance et attaques par canaux auxiliaires.
- Il renvoie à des publications de l’ANSSI, de la CNIL, du BSI, de l’ENISA, du NIST, du NCSC-UK, de la CISA et de l’OWASP, ainsi qu’à plusieurs articles et outils de recherche.
- Le guide précise que ses recommandations ne sont pas normatives sauf disposition réglementaire contraire et qu’elles doivent être adaptées puis validées par les responsables compétents du système cible.

### Opinions ou positions de l’auteur

- L’envoi de données sensibles à des outils grand public sur Internet est à proscrire.
- Un modèle doit être considéré au même niveau de sensibilité que les données ayant servi à sa conception et à son entraînement.
- Un utilisateur ayant accès à un modèle entraîné doit, par prudence, être considéré comme potentiellement capable d’accéder à ses données d’entraînement.
- Les actions critiques ne doivent pas être automatisées sur la seule décision d’une IA générative.
- L’apprentissage continu en production doit être évité au profit d’un ré-entraînement dans des environnements dédiés et contrôlés.
- Les formats de modèles pouvant exécuter du code, comme `pickle`, sont jugés inadaptés ; un format séparant données et code, tel que `safetensor`, est recommandé.
- Les blocs de code touchant à la cryptographie, aux autorisations ou aux données sensibles ne devraient pas être générés par IA.
- Une offre SecNumCloud devrait être privilégiée en Cloud public quand la sensibilité, la criticité ou l’absence de confiance envers les utilisateurs le justifie.

### Interprétations et inférences

#### Interprétations explicitement développées par l’ANSSI

- Un modèle peut mémoriser ou restituer une information sensible ; la sécurité du modèle et celle du corpus sont donc liées.
- Une source externe, un courriel ou une page Web peut véhiculer une instruction malveillante interprétée par un système connecté, d’où le risque particulier des actions automatiques.
- Le partage des responsabilités avec des tiers modifie le risque à chaque phase et doit être pris en compte dans l’architecture, l’hébergement, les audits et les contrats.
- L’anonymisation et les données synthétiques diminuent parfois l’exposition sans éliminer les possibilités de ré-identification ou d’inférence.
- Un système non déterministe peut produire un résultat erroné malgré des tests, ce qui justifie à la fois le contrôle humain et un fonctionnement dégradé indépendant de l’IA.

#### Inférences de la présente analyse

- **[Analyse]** Les recommandations dessinent une approche « zéro confiance » appliquée aux composants d’IA : corpus, modèles, sorties, code généré, plugins et prestataires sont évalués et confinés plutôt que présumés fiables.
- **[Analyse]** Le contrôle humain n’est utile que s’il intervient avant l’effet critique et dispose de suffisamment d’information pour refuser l’action. Le guide demande une validation, mais ne précise pas les critères ergonomiques ou organisationnels qui garantissent son efficacité réelle.
- **[Analyse]** La séparation entraînement/déploiement/production améliore l’intégrité et la traçabilité, mais augmente le coût d’exploitation et ralentit l’adaptation du modèle. Ce compromis devra être explicité dans la gouvernance du changement.
- **[Analyse]** R25 ne suffit pas isolément à sécuriser un système : aucun filtre n’est présenté comme infaillible. La réduction des privilèges, le cloisonnement et la validation des actions demeurent les barrières déterminantes si une injection franchit le filtrage.
- **[Analyse]** La recommandation R33 d’entraîner un service grand public uniquement sur des données publiques est une position de prudence forte. Elle ne traite pas les éventuels droits de propriété intellectuelle ou de protection des données attachés à des contenus pourtant accessibles publiquement.
- **[Analyse]** Le guide constitue une base de contrôle utile, mais la mise en œuvre nécessite de transformer chaque recommandation en exigences vérifiables : propriétaire, actif, preuve attendue, fréquence de contrôle, exception et risque résiduel.

## Limites et points à vérifier

- **Date du référentiel :** les recommandations reflètent l’état des menaces au 29 avril 2024. Il faudrait vérifier l’existence d’une version plus récente avant toute décision opérationnelle ou réglementaire.
- **Absence de vérification externe :** conformément à la consigne du repository, les références, URLs, qualifications, politiques de services tiers et résultats de recherche n’ont pas été contrôlés sur Internet.
- **Caractère non normatif :** l’ANSSI précise que les recommandations n’ont pas, sauf texte contraire, de valeur normative et nécessitent une adaptation au SI cible. Le document ne prouve donc pas à lui seul une conformité juridique ou réglementaire.
- **Périmètre limité :** génération d’images et de vidéos, qualité des données, performance du modèle, éthique, propriété intellectuelle, secret des affaires et protection des données ne sont pas traités exhaustivement.
- **Mesure de l’efficacité :** aucun taux de détection, niveau de robustesse minimal, protocole de benchmark ou seuil d’acceptation n’est donné pour les filtres et audits propres aux LLM.
- **Contrôle humain :** les modalités concrètes — délai, compétence, indépendance, information présentée et prévention de l’approbation routinière — restent à définir.
- **Définition des données sensibles :** des exemples sont fournis, mais chaque organisation doit établir sa classification, ses propriétaires de données et les conséquences d’une agrégation de données apparemment non sensibles.
- **RAG et contrôle d’accès :** le guide indique qu’un RBAC est possible sur les données additionnelles, sans détailler comment prévenir les fuites entre utilisateurs lors de la recherche vectorielle, du cache ou de la construction du contexte.
- **Formats sécurisés :** `safetensor` est cité comme exemple et `pickle` comme format à proscrire ; la sécurité réelle dépend aussi de l’implémentation, du chargeur, des métadonnées et de la provenance du fichier.
- **GPU et canaux auxiliaires :** les recommandations sont générales. Le niveau d’isolation matériel requis et les attaques effectivement applicables au contexte cible nécessitent une étude technique spécifique.
- **Services tiers :** l’affirmation selon laquelle les données sont, dans la majorité des offres, collectées pour optimiser les modèles dépend des produits, contrats, paramètres et politiques en vigueur à la date d’usage ; elle doit être vérifiée service par service.
- **SecNumCloud et administrations :** l’applicabilité de la doctrine « Cloud au centre », des règles de sensibilité et des qualifications doit être confirmée dans leur version actuelle et selon le statut de l’entité.
- **Journalisation :** le document renvoie à la CNIL et au RGPD mais ne fixe pas de durée uniforme de conservation ; celle-ci doit être justifiée selon les finalités et les obligations applicables.
- **Liste de menaces non exhaustive :** les scénarios présentés facilitent la compréhension mais ne remplacent pas une analyse propre aux actifs, adversaires, dépendances, modèles et capacités d’action réels.

## Sources et références mentionnées

Le guide contient une bibliographie de 32 entrées. Les références ci-dessous sont rapportées telles qu’elles apparaissent dans le document et ne sont pas validées indépendamment.

- **Organismes et référentiels internationaux :** BSI sur l’IA ; ENISA, *Artificial Intelligence Cybersecurity Challenges* (2020) et *Securing Machine Learning Algorithms* (2021) ; NIST, *AI Risk Management Framework* (2023), *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations* (2024), SSDF 1.1 (2022) et outils d’analyse de code ; NCSC-UK, recommandations de développement sécurisé (2018) et *Guidelines for Secure AI System Development* (2023) ; CISA sur la chaîne d’approvisionnement et les environnements CI/CD ; OWASP sur les outils d’analyse de code.
- **CNIL :** portail Intelligence artificielle ; conformité de l’IA au RGPD ; critères relatifs à la collecte et à la gestion des données ; taxonomie des attaques contre les systèmes d’IA ; travaux sur les données synthétiques.
- **Guides et référentiels ANSSI :** hygiène informatique ; attaques DDoS ; EBIOS Risk Manager ; protection du potentiel scientifique et technique ; maîtrise du risque numérique ; TLS ; OpenID Connect ; interconnexion à Internet ; sécurité des sites Web ; administration sécurisée ; architecture de journalisation ; DevSecOps ; instruction interministérielle n°901 ; référentiel PASSI ; SecNumCloud.
- **Autres textes publics français :** DINUM et doctrine « Cloud au centre » ; instruction générale interministérielle n°1300 du SGDSN.
- **Recherche et documentation technique :** *Datasheets for Datasets* ; *Not What You’ve Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection* ; article sur les canaux auxiliaires des LLM ; rapports Snyk et recherche de Stanford sur la sécurité du code généré.
- **Outils de test cités :** Microsoft Responsible AI Toolbox, IBM/Trusted-AI Adversarial Robustness Toolbox et Protect AI `ai-exploits`.
- **Services et technologies explicitement nommés :** ChatGPT, Gemini, Copilot, DeepL, Perplexity, RAG, RLHF, OpenID Connect, TLS, SAST, DAST, CI/CD, IOMMU, `safetensor` et `pickle`.

## Cinq éléments essentiels à retenir

1. Un système d’IA générative doit être sécurisé sur tout son cycle de vie et dans toutes ses dépendances, pas seulement au niveau du modèle.
2. Le modèle hérite de la sensibilité de ses données d’entraînement ; le choix entre entraînement et données additionnelles conditionne le contrôle des accès.
3. Les sorties non déterministes et les entrées non maîtrisées interdisent de confier sans validation humaine des actions critiques à l’IA.
4. Cloisonnement, moindre privilège, intégrité des données et fichiers, audits, filtres, journalisation et mode dégradé forment une défense en profondeur.
5. Les données sensibles ne doivent pas être envoyées à un service grand public non maîtrisé, et les droits des assistants tiers sur les applications métier doivent être revus régulièrement.
