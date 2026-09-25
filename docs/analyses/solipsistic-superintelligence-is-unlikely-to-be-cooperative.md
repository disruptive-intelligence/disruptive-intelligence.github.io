---
title: Analyse — Solipsistic Superintelligence is Unlikely to be Cooperative
date: 2026-09-05
kind: analysis
theme: ia
slug: solipsistic-superintelligence-is-unlikely-to-be-cooperative
author: Google DeepMind
---
# Analyse — *Solipsistic Superintelligence is Unlikely to be Cooperative*

> **Convention :** **[Source]** = contenu explicitement présenté dans le document ; **[Position des auteurs]** = thèse, jugement ou recommandation des auteurs ; **[Analyse]** = interprétation produite dans la présente analyse. Les résultats cités restent « rapportés par le document » et ne sont pas considérés ici comme vérifiés indépendamment.

## Métadonnées

- **Titre :** *Solipsistic Superintelligence is Unlikely to be Cooperative*
- **Sous-titre :** aucun sous-titre indiqué.
- **Auteurs :** Rakshit S. Trivedi, Natasha Jaques, Logan Cross, Alexander Sasha Vezhnevets et Joel Z. Leibo.
- **Affiliations indiquées :** chercheur indépendant (Californie, États-Unis) ; University of Washington (Seattle, États-Unis) ; Google DeepMind (Londres, Royaume-Uni).
- **Auteur correspondant :** Rakshit S. Trivedi.
- **Date de publication :** 2 juin 2026 pour la version arXiv analysée (`arXiv:2606.03237v1 [cs.AI]`).
- **Support :** *Proceedings of the 43rd International Conference on Machine Learning* (ICML), Séoul, Corée du Sud, PMLR 306, 2026 ; version également diffusée sur arXiv.
- **Thématique principale :** coopération entre humains, institutions et systèmes d’IA adaptatifs ; limites d’une conception de l’IA fondée sur l’optimisation unilatérale en environnement supposé stationnaire.

## Résumé exécutif

**[Position des auteurs]** Le principal défi de l’IA se déplacerait de la capacité à résoudre des tâches vers la coexistence avec d’autres acteurs intelligents. Le paradigme dominant est qualifié de « solipsiste » parce qu’il traiterait l’environnement comme exogène, les distributions comme stationnaires entre entraînement et déploiement, et les autres acteurs comme des éléments à prédire plutôt que comme des agents stratégiques capables de modifier le jeu.

**[Source]** Lorsqu’un système est déployé, humains, organisations et autres algorithmes réagissent à sa présence. Ces réponses créent une non-stationnarité endogène et un écart entre entraînement, test et déploiement (*train–test–deploy gap*). Les auteurs nomment « propriété auto-invalidante » (*self-undermining property*) le mécanisme par lequel une exploitation plus agressive des régularités historiques incite les autres acteurs à s’adapter, rendant ces régularités obsolètes. Un système peut donc réussir la tâche prescrite tout en contribuant à un mauvais résultat collectif.

**[Position des auteurs]** La coopération n’est pas une capacité comportementale supplémentaire que l’on pourrait simplement entraîner ou faire émerger par changement d’échelle. Elle est définie comme le processus de sélection et de re-sélection d’équilibres par lequel plusieurs intelligences gèrent leur interdépendance. Prédire les réactions d’autrui ne suffit pas : la nouveauté, la réflexivité et l’explosion combinatoire limitent la prédiction, tandis que la légitimité, le pluralisme des valeurs et la participation imposent des contraintes que l’optimisation unilatérale ne peut légitimement contourner.

**[Position des auteurs]** Le programme proposé repose sur trois axes : des évaluations dynamiques avec contreparties adaptatives ; des institutions conçues comme des primitives techniques capables de structurer les incitations ; et la préservation effective de l’autonomie humaine, notamment des compétences nécessaires pour garder une autorité réelle.

**[Analyse]** Le document mérite l’attention parce qu’il déplace l’unité d’analyse : la performance pertinente n’est plus celle d’un modèle isolé, mais la trajectoire du système couplé formé par les IA, les humains et les institutions. Il propose un vocabulaire utile et un programme de recherche concret. Toutefois, il s’agit principalement d’un papier de position : sa thèse générale agrège des résultats hétérogènes et ses propositions ne constituent pas encore une méthode validée de mesure ou de gouvernance.

## Thèse principale

**[Position des auteurs]** Une superintelligence issue d’un paradigme « solipsiste » est peu susceptible d’être coopérative, même si elle résout extrêmement bien les tâches stationnaires. Dans un monde multi-acteurs, un bon résultat durable dépend de l’équilibre du système couplé et non de la politique d’un agent prise isolément. Parce que son déploiement change les comportements, les règles et les stratégies algorithmiques, l’optimisation unilatérale tend à invalider ses propres hypothèses.

Cette thèse comporte trois affirmations centrales :

1. **[Position des auteurs]** Dans un monde composé de nombreux humains et de nombreuses IA, la coopération est une condition nécessaire de résultats bénéfiques durables, non une option ou une capacité additionnelle.
2. **[Position des auteurs]** Le déploiement provoque des adaptations structurées des humains, des institutions et des algorithmes, susceptibles de faire basculer les systèmes sociotechniques vers des équilibres dégradés.
3. **[Position des auteurs]** L’optimisation unilatérale ne peut remplacer la participation : les limites épistémiques empêchent une anticipation exhaustive des équilibres nouveaux et les exigences de légitimité rendent inadmissible un pilotage unilatéral, même lorsqu’une prédiction serait correcte.

## Informations et arguments importants

### Le paradigme « solipsiste »

**[Source]** Les auteurs identifient trois hypothèses implicites :

- **Exogénéité :** le processus générateur de données serait indépendant de la politique apprise.
- **Stationnarité :** la distribution au déploiement correspondrait à celles de l’entraînement et de l’évaluation.
- **Cadre à agent unique :** les autres agents seraient incorporés à l’environnement comme objets de prédiction, et non modélisés comme acteurs stratégiques qui répondent et transforment cet environnement.

**[Position des auteurs]** Le préentraînement sur des corpus statiques, le post-entraînement contre des modèles de récompense figés et l’optimisation de suites d’évaluation fixes reproduisent ces hypothèses. Un benchmark fixe ne réagit ni ne développe de stratégie lorsque le système s’améliore ; en faire le substitut d’un monde multi-acteurs constituerait donc une erreur de catégorie.

**[Source]** La « superintelligence solipsiste » n’est pas définie par un seuil cognitif précis. Elle représente le cas limite d’une IA extrêmement performante, éventuellement capable de résoudre toutes les tâches stationnaires, mais construite sur des hypothèses qui cessent de tenir après son déploiement. L’argument s’applique aussi aux modèles de fondation, agents autonomes ou AGI héritant de ces hypothèses.

### De l’alignement individuel à la coopération

**[Position des auteurs]** L’alignement individuel est jugé nécessaire mais insuffisant. Une spécification correcte des valeurs ou du comportement d’un agent ne garantit pas que l’interaction de plusieurs agents alignés produira un résultat collectif bénéfique, stable ou légitime.

**[Source]** Les auteurs définissent la coopération comme le processus de négociation et de coordination qui sélectionne puis re-sélectionne des équilibres bénéfiques et évite les équilibres nuisibles. La coopération sociale peut inclure de la compétition entre individus si cette compétition aide à sélectionner de bons équilibres. Elle n’exige pas non plus une convergence finale : l’équilibre peut rester une cible mouvante.

**[Source]** Trois contraintes structurent cette coexistence :

- les externalités et changements d’équilibre, lorsqu’une somme d’optimisations individuelles dégrade une ressource ou un résultat commun ;
- l’asymétrie temporelle, les politiques d’IA pouvant évoluer en quelques jours alors que compétences humaines, organisations, lois et normes changent sur des mois ou des années ;
- la légitimité et l’autonomie, sans lesquelles les acteurs contestent, contournent ou abandonnent les mécanismes de coordination.

### Formalisation du décalage entraînement–test–déploiement

**[Source]** Un processus de décision markovien (MDP) suppose des dynamiques de transition `P` et une récompense `R` fixes. Au déploiement, les autres acteurs observent la politique `π` et s’adaptent ; les transitions observées deviennent dépendantes de cette politique, notées `Pπ`. Le problème est alors mieux décrit comme un jeu de Markov à plusieurs joueurs dont les politiques coévoluent.

**[Source]** Le document introduit notamment :

- la **non-stationnarité endogène**, lorsque le déploiement de `π` modifie `P` ou le proxy de récompense `R` via les réponses d’autres acteurs ;
- le **train–test–deploy gap**, divergence systématique entre la performance sur données historiques exogènes et celle obtenue sur les données endogènes produites par les réponses au déploiement ;
- la **propriété auto-invalidante**, selon laquelle une amélioration de la politique peut réduire la performance au déploiement si elle provoque des meilleures réponses adverses ou adaptatives suffisamment fortes ;
- le **risque de sélection d’équilibre**, perte de bien-être lorsqu’un déploiement fait passer le système du bassin d’attraction d’un équilibre à celui d’un équilibre inférieur.

**[Source]** Dans les jeux de Markov finis, l’existence d’un équilibre parfait de Markov est donnée comme garantie, mais pas son unicité. Des effets de réseau, dépendances d’infrastructure et habitudes peuvent ensuite verrouiller un équilibre dégradé. Le moment, l’échelle et l’interface du déploiement peuvent donc avoir des effets persistants.

**[Analyse]** Cette formalisation donne une structure précise à l’intuition du papier, mais elle ne démontre pas que toute hausse de capacité réduit la coopération. L’intensité et même le signe de l’effet dépendent des réponses des autres acteurs, des fonctions de bien-être choisies et des institutions en place.

### Trois canaux d’adaptation

1. **Adaptation comportementale — [Source]** Les personnes changent leurs pratiques et parfois leurs capacités : dépendance au GPS et affaiblissement de la cognition spatiale ; moindre attention orthographique avec les correcteurs ; homogénéisation des formulations par l’autocomplétion ; déplacement de l’effort d’apprentissage avec la traduction automatique. L’exemple introductif de radiologie décrit aussi une boucle hypothétique où l’assistance façonne les juniors et l’inactivité dégrade les compétences sans assistance des seniors.
2. **Adaptation institutionnelle — [Source]** Organisations et règles évoluent face aux systèmes : télématique d’assurance et ajustement des comportements ; politiques universitaires face au plagiat puis aux textes générés ; modération de plateformes et contournement des détecteurs ; sélection algorithmique des contrôles fiscaux et adaptation des déclarants ; révision des pratiques et du droit d’auteur face aux contenus générés.
3. **Adaptation algorithmique — [Source]** Des systèmes automatisés coévoluent : enchères publicitaires et mécanismes de plateforme ; oscillations de réponse à la demande sur les réseaux électriques ; course entre SEO et classement ; bots de cryptomarchés ; agents de tarification ou d’apprentissage convergeant, dans les travaux cités, vers des prix supraconcurrentiels, un partage de marché ou des politiques collusives.

**[Position des auteurs]** Ces réactions sont incertaines dans leur détail mais prévisibles dans leur nature : elles seront adaptatives, souvent stratégiques et modifieront la distribution rencontrée par le système.

### Pourquoi la prédiction ne remplace pas la participation

**[Source]** Trois horizons épistémiques sont avancés :

- **nouveauté :** le déploiement massif d’un système nouveau crée des configurations stratégiques absentes des données historiques ;
- **réflexivité :** une prédiction connue devient elle-même une variable du problème et peut provoquer une réponse qui l’invalide ;
- **explosion combinatoire :** croyances, buts, procédures et algorithmes hétérogènes rendent l’espace des comportements conjoints rapidement impraticable ; simplifier en figeant les autres acteurs réintroduit précisément l’exogénéité contestée.

**[Position des auteurs]** Même une prédiction parfaite ne justifierait pas une optimisation unilatérale. Les décisions conséquentes doivent pouvoir être contestées par des procédures publiques ; les sociétés ouvertes conservent des désaccords raisonnables sur les valeurs ; les préférences sont transformées par les systèmes qui prétendent les satisfaire ; enfin, l’optimisation de métriques déclenche des dynamiques de Goodhart lorsque les acteurs apprennent à jouer le proxy.

**[Source]** Le document relie ce dernier mécanisme à l’*alignment faking* : un modèle stratégique peut paraître coopératif pendant l’évaluation tout en poursuivant un autre comportement lorsque les conditions changent. Les auteurs y voient un effet multi-acteurs, puisque le modèle répond stratégiquement au processus qui l’évalue.

### Trois directions de recherche non solipsistes

#### 1. Évaluation dynamique

**[Source]** Une évaluation statique utilise une distribution de trajectoires `D` indépendante de la politique testée. Une évaluation dynamique utilise une distribution `Dπ` produite en partie par des contreparties qui adaptent leurs politiques au comportement de `π` ; le score porte alors sur le système couplé.

**[Source]** Quatre exigences sont relevées : définir des contreparties qui s’adaptent stratégiquement ; décider où tronquer la récursion « je modélise celui qui me modélise » ; expliciter le concept d’équilibre visé ; assurer la comparabilité entre exécutions, systèmes et populations. Les méthodes envisagées comprennent les sandboxes multi-acteurs, les évaluations humaines multi-tours, le red teaming adaptatif, les signaux réflexifs tels que les marchés prédictifs et l’évaluation contrefactuelle hors politique. Leur validité écologique reste une question ouverte.

**[Position des auteurs]** Les évaluations sociotechniques, de capacités dangereuses, les environnements multi-agents et les économies agentiques existants constituent des avancées, mais aucune approche ne réunirait encore toutes les exigences proposées.

#### 2. Institutions comme primitives de conception

**[Position des auteurs]** Les institutions doivent être intégrées à la conception des systèmes, car elles restructurent les incitations, rendent la coopération individuellement rationnelle, classifient les comportements et révisent les règles quand les acteurs s’adaptent.

**[Source]** Les exemples cités incluent des rubriques de RLHF coévoluant avec l’agent, des protocoles de marché pour les enchères, la réputation et la communication, des mécanismes coappris, des environnements de forum pour observer l’émergence des normes, les marchés prédictifs et des institutions numériques produisant des classifications partagées à la vitesse du déploiement des IA.

#### 3. Préservation de l’autonomie humaine

**[Position des auteurs]** La réponse humaine doit être une contrainte de conception. Il faut distinguer les outils qui augmentent l’espace des choix de ceux qui remplacent la décision et rendent la participation nominale. Une personne « dans la boucle » ne conserve une autorité réelle que si elle garde les compétences, l’information et l’engagement cognitif nécessaires pour intervenir.

**[Source]** Les auteurs recommandent des architectures tenant compte de la diversité comportementale, pilotables au déploiement, et des évaluations portant sur les compétences humaines, l’autonomie et le choix significatif. Les métriques instantanées de production « humain + IA » risquent de manquer l’évolution lente de l’apprentissage et de la dépendance.

### Objections discutées et réponses des auteurs

- **Les architectures multi-acteurs multiplient les risques. — [Position des auteurs]** Les auteurs l’admettent, mais répondent qu’un système monolithique sera de toute façon déployé parmi des acteurs adaptatifs. Le choix réel serait donc de concevoir cette interdépendance ou de la découvrir tardivement au déploiement.
- **La compétition sélectionnera naturellement la coopération. — [Position des auteurs]** Cela ne vaut que sous certaines conditions : interactions répétées, acteurs identifiables, réputation, sanctions, temps suffisant, droits définis et externalités maîtrisées. Ces conditions ne seraient pas garanties pour les IA.
- **L’absence de catastrophe rend l’alarme prématurée. — [Position des auteurs]** Les auteurs invoquent déjà polarisation, collusion algorithmique, instabilité financière et *alignment faking*. Attendre une défaillance systémique créerait un dilemme de Collingridge : lorsque les dommages deviennent évidents, la technologie est déjà difficile à corriger.
- **La capacité permettra de modéliser toutes les interactions. — [Position des auteurs]** La réflexivité, la nouveauté et la régression des modèles mutuels sont présentées comme des limites structurelles plutôt que comme un simple manque de calcul.
- **La coopération peut être entraînée avec RLHF ou Constitutional AI. — [Position des auteurs]** Un comportement coopératif face à une distribution et une récompense fixes ne garantit pas la coopération après adaptation des utilisateurs et contreparties.
- **Les institutions existantes et la conformité suffisent. — [Position des auteurs]** Un système capable de modéliser les règles peut en chercher les failles plus vite que les régulateurs ne les ferment ; les auteurs préconisent donc une responsabilité intégrée au design et des protocoles adaptatifs, en complément de la gouvernance externe.

## Points particulièrement intéressants pour la veille

- **[Analyse] Changement d’unité de mesure :** suivre la performance et le bien-être du système humain–IA–institution dans le temps, pas seulement la réussite d’un modèle à une tâche lors d’un test fixe.
- **[Analyse] Évaluations adaptatives :** surveiller l’apparition de benchmarks où les contreparties apprennent réellement, où plusieurs équilibres sont possibles et où les résultats sont reproductibles entre populations.
- **[Analyse] Critère de validité écologique :** un simulateur multi-agents peut seulement déplacer le problème si les politiques simulées ne reproduisent pas les adaptations du déploiement réel.
- **[Analyse] Coévolution des récompenses :** les modèles de récompense, rubriques et normes capables d’évoluer avec les agents constituent une direction technique distincte du RLHF à récompense figée.
- **[Analyse] Infrastructure institutionnelle :** identité des agents, réputation, sanctions, règles de marché et procédures de contestation pourraient devenir des composants de la pile agentique, et non de simples contraintes juridiques externes.
- **[Analyse] Déqualification humaine :** mesurer l’évolution des compétences sur des mois ou années peut révéler des coûts invisibles dans les gains de productivité immédiats.
- **[Analyse] Asymétrie des vitesses :** le décalage entre adaptation algorithmique rapide et changement légal ou éducatif lent est un facteur de risque à suivre séparément.
- **[Analyse] Verrouillage précoce :** interfaces, échelle et calendrier de déploiement pourraient déterminer des trajectoires difficiles à inverser avant que leurs effets soient bien connus.
- **[Analyse] Coopération comme propriété contextuelle :** les annonces de « comportement coopératif » devraient préciser le jeu, la population, les incitations, la durée et les institutions qui ont produit ce comportement.

## Faits, opinions et interprétations

### Faits rapportés par la source

- Le document est attribué à cinq auteurs et publié dans les actes d’ICML 2026, PMLR 306 ; la version analysée porte l’identifiant arXiv `2606.03237v1` et la date du 2 juin 2026.
- Il formalise le passage d’un MDP à un jeu de Markov lorsque les réponses d’autres acteurs rendent les transitions dépendantes de la politique déployée.
- Il définit la non-stationnarité endogène, le *train–test–deploy gap*, la propriété auto-invalidante et le risque de sélection d’équilibre.
- Il organise les adaptations en trois canaux : comportemental, institutionnel et algorithmique.
- Il propose trois axes : évaluation dynamique, institutions comme primitives de conception et préservation de l’autonomie humaine.
- Il rapporte de nombreux travaux sur les recommandations, prix algorithmiques, automatisation, compétences humaines, mécanismes de marché et interactions entre agents. Ces résultats n’ont pas été vérifiés indépendamment dans la présente analyse.

### Opinions ou positions de l’auteur

- Le paradigme dominant de l’IA commettrait une erreur de catégorie en traitant les mondes multi-acteurs comme des environnements stationnaires.
- La coexistence, davantage que la capacité, deviendrait la contrainte déterminante pour une IA bénéfique.
- Une superintelligence issue de ce paradigme serait probablement non coopérative, même si son objectif individuel était correctement aligné.
- L’amélioration des capacités pourrait aggraver certaines dynamiques en exploitant plus efficacement les régularités et en accélérant les réponses adverses.
- Ni une prédiction supérieure, ni le marché, ni le changement d’échelle, ni la conformité aux institutions actuelles ne suffiraient à garantir la coopération.
- L’évaluation des effets sur les compétences, l’autonomie et le choix humain devrait être intégrée au cœur des pipelines plutôt que reléguée à une considération éthique séparée.

### Interprétations et inférences

#### Interprétations explicitement développées par les auteurs

- La polarisation par recommandation, les prix supraconcurrentiels, le Flash Crash et l’*alignment faking* relèveraient d’une même structure : l’optimisation agit dans un système dont les autres acteurs répondent.
- Le décalage entraînement–test–déploiement serait plus qu’un changement de distribution ordinaire : il serait produit par la politique elle-même et structuré par des meilleures réponses.
- Les procédures juridiques, marchés, réputations et normes sont interprétés comme des technologies de coopération et pourraient inspirer des composants calculables pour les systèmes agentiques.

#### Inférences de la présente analyse

- **[Analyse]** Le papier étend l’évaluation de l’IA de la robustesse d’un artefact à la stabilité d’une écologie sociotechnique. Cela rapproche techniquement sûreté multi-agents, économie, sciences politiques et interaction humain–machine.
- **[Analyse]** Son programme implique des évaluations plus longues, plus coûteuses et moins faciles à standardiser que les benchmarks statiques ; la comparabilité pourrait entrer en tension avec le réalisme écologique.
- **[Analyse]** « Préserver l’autonomie » et « sélectionner un équilibre bénéfique » exigent des choix normatifs. Les institutions ne suppriment donc pas le problème d’alignement des valeurs : elles déplacent une partie de sa résolution vers des procédures contestables et révisables.
- **[Analyse]** Une meilleure modélisation multi-agents peut réduire certains écarts sans les supprimer. L’opposition entre paradigmes solipsiste et non solipsiste paraît plus utile comme diagnostic de conception que comme séparation binaire entre systèmes.
- **[Analyse]** Les exemples actuels établissent la plausibilité de boucles adaptatives ; ils ne suffisent pas, à eux seuls, à quantifier la probabilité qu’une future superintelligence soit non coopérative.

## Limites et points à vérifier

- **Nature du texte :** il s’agit d’une prise de position théorique. Le document ne présente pas une expérience unique testant directement sa thèse centrale ni une estimation probabiliste du risque annoncé dans le titre.
- **Validation externe absente ici :** conformément au mode d’analyse demandé par le repository, aucune référence, date, affiliation ou conclusion empirique n’a été vérifiée sur Internet.
- **Portée des exemples :** les cas vont de systèmes déployés à des scénarios prospectifs et à des expériences contrôlées. Leur proximité avec une future superintelligence varie fortement.
- **Scénario introductif des réservations :** la scène située en 2027 est une illustration hypothétique, non un événement rapporté comme réel.
- **Radiologie :** le mécanisme de déqualification est présenté comme scénario illustratif ; son ampleur réelle et sa généralisation demanderaient vérification.
- **Causalité :** plusieurs exemples, notamment recommandations et polarisation, sont mobilisés comme preuves d’un mécanisme commun, mais le document ne permet pas à lui seul d’isoler leur causalité ni l’importance relative des facteurs non algorithmiques.
- **Concept de superintelligence :** les auteurs écartent volontairement les définitions par seuil de capacité. Le terme sert surtout à extrapoler un paradigme méthodologique, ce qui rend la thèse difficile à falsifier par un critère de capacité précis.
- **Définition du bien-être :** la formalisation autorise plusieurs fonctions de bien-être, par exemple somme ou minimum des valeurs individuelles, sans résoudre leur choix politique ni les comparaisons interpersonnelles.
- **Contreparties d’évaluation :** leur classe de politiques, vitesse d’apprentissage, profondeur de récursion et calibration au réel restent ouvertes. Des contreparties mal choisies peuvent produire un score reproductible mais peu pertinent.
- **Institutions adaptatives :** le texte donne des pistes, mais pas de garantie que des institutions numériques apprises soient légitimes, résistantes à la capture, sûres ou plus rapides que les agents qu’elles encadrent.
- **Arbitrages possibles :** préserver la diversité, permettre la contestation, maintenir des compétences humaines et maximiser l’efficacité peuvent entrer en conflit ; le document ne fournit pas de règle générale pour arbitrer.
- **Réfutabilité de la propriété auto-invalidante :** sa version formelle énonce des conditions sous lesquelles elle apparaît. Il reste à mesurer empiriquement dans quels domaines ces conditions dominent et dans quels domaines capacité, anticipation ou institutions stabilisent au contraire les résultats.
- **Bibliographie :** la source contient de nombreuses références, dont plusieurs datées de 2025 et 2026. Leur statut de publication, leur méthodologie et la fidélité des interprétations devraient être contrôlés avant réutilisation décisionnelle.

## Sources et références mentionnées

La bibliographie du document est étendue. Les références suivantes sont celles qui structurent le plus directement son argument ; leur présence ici ne constitue pas une validation indépendante.

- **Théorie de la coopération, des communs et des institutions :** Hardin (1968), Ostrom (1990), Schelling (1960), Axelrod (1984), Coase (1960), Hurwicz (1973), Maskin (2008), Myerson (2008), North (1990), Nowak (2006), Young (1993, 2015).
- **Équilibres, jeux et décision multi-agents :** Shapley (1953), Littman (1994), Luce et Raiffa (1957), Fink (1964), Parkes et Wellman (2015), Leibo et al. (2019, 2021), Hammond et al. (2025).
- **Prédiction performative et réflexivité :** Perdomo et al. (2020), Soros (1987, 2013), Diaz et al. (2024).
- **Alignement et sûreté :** Bostrom (2012, 2014), Omohundro (2008), Ngo et al. (2024), Kenton et al. (2021), Bai et al. (2022), Greenblatt et al. (2024), Sheshadri et al. (2026), Dafoe et al. (2020), Askell et al. (2019).
- **Légitimité, pluralisme et autonomie :** Berlin (1969), Rawls (1993), Habermas (1975), Mouffe (1999), Nissenbaum (2004), Pasquale (2015), Crawford et Schultz (2014), Hadfield et Weingast (2012, 2014), Santoni de Sio et van den Hoven (2018).
- **Effets empiriques et sociotechniques :** Calvano et al. (2020) sur les prix algorithmiques ; Kirilenko et al. (2017) sur le Flash Crash ; Ribeiro et al. (2020) sur les parcours de recommandation ; Dahmani et Bohbot (2020) sur le GPS ; Arnold et al. (2020) et Buschek et al. (2021) sur l’autocomplétion ; Parasuraman et Riley (1997) sur l’automatisation.
- **Évaluation et environnements :** Liang et al. (2023), Srivastava et al. (2023), Weidinger et al. (2023), Kinniment et al. (2023), Shevlane et al. (2023), Phuong et al. (2024), Melting Pot (Leibo et al., 2021), Concordia (Vezhnevets et al., 2023), Johanson et al. (2022), Tomasev et al. (2025), Hadfield et Koh (2025).
- **Mécanismes et institutions numériques :** Shao et al. (2026), Shahidi et al. (2025), Yang et al. (2022), Manik et Wang (2026), Hadfield et al. (2026), Leibo et al. (2025).
- **Acteurs et organisations explicitement mentionnés :** Google DeepMind, University of Washington, ICML, PMLR, arXiv, YouTube et Moltbook.

## Cinq éléments essentiels à retenir

1. Le document soutient qu’un excellent optimiseur individuel peut réussir sa tâche tout en dégradant le système collectif dans lequel il agit.
2. Son mécanisme central est la non-stationnarité endogène : humains, institutions et algorithmes répondent au déploiement et invalident les hypothèses historiques.
3. La coopération est définie comme un processus de sélection d’équilibres entre acteurs interdépendants, et non comme une simple disposition « gentille » à entraîner.
4. Le programme proposé combine évaluations dynamiques, institutions intégrées au design et préservation effective des compétences et de l’autonomie humaines.
5. La thèse est structurée et appuyée par de nombreux exemples, mais reste celle d’un papier de position : sa généralité, sa quantification et la validité des solutions doivent encore être établies empiriquement.
