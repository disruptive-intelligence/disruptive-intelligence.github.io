---
title: Physical AI
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — récit, cadrage transversal. **Couches** — percevoir + apprendre et décider + agir.

**Ce qu'il désigne.** Le mouvement consistant à appliquer aux systèmes physiques les méthodes d'apprentissage qui ont transformé le traitement du langage et de l'image : modèles entraînés sur de grandes quantités de données, capables de généraliser à des situations non spécifiées.

**Ce qu'il mélange.** Tout, et c'est sa fonction. Des composants — capteurs, actionneurs. Des architectures — modèles reliant observation et commande. Des plateformes — robots, véhicules. Des systèmes — flottes. Et une doctrine — délégation de tâches physiques.

**Ce qu'il ne signifie pas.** Une technologie. **Vous ne pouvez pas acheter de la Physical AI, en mesurer la performance, ni comparer deux fournisseurs sur ce critère.** C'est le cas d'école du chapitre 2 : mis en concurrence avec « lidar » ou « humanoïde », le terme produit une conclusion mal formée.

**Ce qu'il vous fait manquer.** **Le maillon le plus en retard.** En regroupant six couches sous un mot, le cadrage suggère que l'ensemble progresse d'un bloc. Or une convergence avance au rythme de son constituant le plus lent, qui est ici la fiabilité de la manipulation et le coût de l'actionnement — pas la perception, ni les modèles.

**Pourquoi il est employé.** Parce qu'il nomme quelque chose de réel : un déplacement d'attention et d'investissement du logiciel vers le monde physique. C'est un cadrage utile pour désigner un mouvement, inutilisable pour analyser un objet.

**Comment l'employer correctement.** Comme nom d'une convergence, jamais comme nom d'une technologie. Le dossier du chapitre 36 traite cette convergence sous son vrai nom : la robotique généraliste.

**Dans l'atlas** — VLA (ch. 13) · modèles du monde (ch. 13) · sim-to-real (ch. 13) · manipulation (ch. 14) · actionneurs (ch. 15).

---


### Embodied AI

**Niveau** — cadrage, plus étroit que le précédent. **Couches** — percevoir + apprendre et décider + agir.

**Ce qu'il désigne.** L'idée qu'un système apprenant qui dispose d'un corps et interagit avec un environnement acquiert des capacités qu'un système traitant uniquement des données ne peut acquérir. Le terme vient de la recherche et précède l'usage commercial.

**Ce qu'il mélange.** Une hypothèse scientifique sur la nature de l'apprentissage et une catégorie de produits.

**Ce qu'il ne signifie pas.** Humanoïde. Un bras fixe, un drone, un véhicule sont des systèmes incarnés. **La confusion entre incarnation et forme humaine est l'une des plus fréquentes du domaine.**

**À ne pas confondre avec Physical AI.** *Embodied AI* est une thèse sur l'apprentissage ; *Physical AI* est un cadrage de marché qui l'englobe. Le premier a une histoire académique, le second n'en a pas.

**Ce qu'il vous fait manquer.** **La question des données.** L'apprentissage par interaction suppose de collecter des interactions, ce qui est lent, coûteux et difficile à mettre à l'échelle — c'est le verrou principal, et le terme ne l'évoque pas.

---


### Autonomous systems

**Niveau** — catégorie industrielle. **Couches** — percevoir + décider + agir + vérifier.

**Ce qu'il désigne.** Les systèmes capables d'accomplir une mission sans intervention humaine continue. La catégorie couvre l'aérien, le terrestre, le maritime, l'industriel.

**Ce qu'il mélange.** **Des degrés d'autonomie sans commune mesure.** Un robot d'entrepôt suivant un itinéraire cartographié et un véhicule circulant en ville partagent une étiquette et rien d'autre. Le terme masque aussi la distinction entre autonomie de navigation et autonomie de décision.

**Ce qu'il ne signifie pas.** Absence d'humain. La plupart des systèmes déployés fonctionnent avec supervision à distance, assistance en cas de blocage, ou reprise en main possible. **C'est une différence économique majeure** : un système supervisé conserve un coût d'opérateur, réparti sur plusieurs machines.

**Ce qu'il vous fait manquer.** **Le domaine de conception opérationnelle.** La question utile n'est jamais « ce système est-il autonome ? » mais « dans quelles conditions son comportement a-t-il été validé, sait-il quand il en sort, et que fait-il alors ? ». La catégorie évacue cette question.

**Dans l'atlas** — domaine de conception opérationnelle (ch. 17) · autonomie supervisée (ch. 16) · architecture de sûreté (ch. 30).

---


### Machine autonomy

**Niveau** — cadrage. **Couches** — décider, vérifier.

**Ce qu'il désigne.** L'autonomie considérée comme propriété générale d'une machine, indépendamment de son domaine — logiciel, physique, industriel.

**Ce qu'il mélange.** Trois régimes que le chapitre 12 sépare : **automatisation** — exécuter une séquence prévue ; **agentivité** — décomposer un objectif et choisir les étapes ; **autonomie** — décider dans une situation non prévue, y compris celle de s'arrêter.

**Ce qu'il vous fait manquer.** **Le seuil.** Ces trois régimes n'appellent ni les mêmes preuves, ni les mêmes assurances, ni les mêmes responsabilités juridiques. Un terme unique pour les trois efface précisément la frontière qui compte.

---


### Service autonomy

**Niveau** — capacité organisationnelle. **Couches** — décider, vérifier, relier.

**Ce qu'il désigne.** La capacité d'un service — informatique, industriel, logistique — à se maintenir en fonctionnement, se corriger et s'adapter sans intervention humaine de routine.

**Ce qu'il mélange.** Une capacité technique et une transformation d'organisation. Le second aspect domine largement, et il est presque toujours sous-estimé.

**Ce qu'il ne signifie pas.** Absence d'équipe. Il signifie déplacement du travail humain : de l'exécution vers la conception des règles, la supervision des exceptions et l'analyse des incidents. **Les compétences requises augmentent en niveau et diminuent en volume.**

**Ce qu'il vous fait manquer.** **La question du mode dégradé.** Un service autonome doit savoir ce qu'il fait quand il ne sait plus quoi faire — et à qui il le signale, dans quel délai. C'est la question la plus difficile et la moins traitée.

**Dans l'atlas** — service autonomy (ch. 12) · opérations autonomes (ch. 12) · dégradation maîtrisée (ch. 30).

---


### General-purpose robotics

**Niveau** — capacité visée. **Couches** — percevoir + apprendre + agir + alimenter.

**Ce qu'il désigne.** L'objectif d'un système robotique capable d'accomplir un large éventail de tâches physiques non spécifiées à l'avance, dans des environnements non préparés.

**Ce qu'il mélange.** Deux généralités distinctes : **généralité de tâche** — le même robot fait plusieurs choses — et **généralité d'environnement** — le même robot fonctionne dans plusieurs lieux. La seconde est bien plus difficile, et les démonstrations portent presque toujours sur la première.

**Ce qu'il ne signifie pas.** Humanoïde. La forme humaine est une réponse possible à la généralité, motivée par l'adaptation à des espaces conçus pour l'humain ; ce n'est ni la seule ni nécessairement la meilleure.

**Ce qu'il vous fait manquer.** **Le point de bascule économique.** Un robot spécialisé et bon marché bat un robot généraliste et cher sur toute tâche répétitive. La généralité ne devient économiquement pertinente que là où la variété des tâches rend la spécialisation impossible — et cette frontière se calcule.

**Dans l'atlas** — manipulation (ch. 14) · robot humanoïde (ch. 15) · robots mobiles autonomes (ch. 14).

---


### Humanoid robotics

**Niveau** — catégorie industrielle, autour d'une plateforme. **Couches** — agir principalement.

**Ce qu'il désigne.** Les robots à morphologie humaine — bipèdes, à bras et mains, à hauteur d'homme.

**Ce qu'il mélange.** Des objets aux ambitions radicalement différentes : plateformes de recherche, démonstrateurs, machines destinées à des tâches logistiques précises, et projets de robot polyvalent.

**Ce qu'il ne signifie pas.** Généralité, ni autonomie. La morphologie n'implique aucune des deux.

**Ce qu'il vous fait manquer.** **Le coût de la forme.** La bipédie coûte en énergie, en complexité de contrôle, en risque de chute et en sécurité pour les personnes proches. Ces coûts sont justifiés si l'environnement impose la forme humaine — escaliers, poignées, espaces étroits — et injustifiés sinon. La catégorie fait raisonner sur la ressemblance plutôt que sur ce compromis.

**Dans l'atlas** — robot humanoïde (ch. 15) · actionneurs (ch. 15) · mains et préhenseurs (ch. 15).

---


### Intelligent robotics

**Niveau** — cadrage vieillissant. **Couches** — percevoir + décider + agir.

**Ce qu'il désigne.** Historiquement, les robots dotés de perception et d'adaptation, par opposition aux robots à trajectoire programmée.

**Ce qu'il mélange.** Le terme a désigné successivement des choses très différentes — capteurs de fin de course, vision industrielle, planification, apprentissage. Il porte quarante ans de sédimentation.

**Ce qu'il vous fait manquer.** Rien de spécifique : c'est un terme largement remplacé par d'autres. **Il est présent ici pour une raison précise** — vous le rencontrerez dans des documents anciens, des appels d'offres publics et des intitulés académiques, et il faut savoir qu'il ne dit rien de la génération technologique concernée.

---


### Autonomous mobility

**Niveau** — catégorie industrielle. **Couches** — percevoir + décider + agir + relier.

**Ce qu'il désigne.** L'ensemble des systèmes de transport fonctionnant sans conducteur : véhicules particuliers, taxis, navettes, camions, mais aussi navires et trains.

**Ce qu'il mélange.** Des situations dont les difficultés n'ont rien de commun. Un train circule sur une voie dédiée ; un navire évolue dans un espace peu encombré avec des temps de réaction longs ; un véhicule urbain fait face à un environnement non structuré et à des piétons.

**Ce qu'il ne signifie pas.** Un marché unique. Les cadres réglementaires, les modèles économiques et les verrous techniques diffèrent complètement selon le mode.

**Ce qu'il vous fait manquer.** **Le rôle du renouvellement du parc.** Même une adoption totale sur les véhicules neufs mettrait plus d'une décennie à transformer le parc en circulation. La catégorie fait raisonner sur la capacité et masque la contrainte temporelle qui borne toute transformation.

---


### Drone economy

**Niveau** — récit à composante économique. **Couches** — percevoir + décider + agir + relier.

**Ce qu'il désigne.** L'ensemble des activités reposant sur des aéronefs sans équipage : inspection, cartographie, agriculture, logistique, sécurité civile.

**Ce qu'il mélange.** Des plateformes allant de quelques centaines de grammes à plusieurs tonnes, des cadres réglementaires distincts selon le poids et le type de vol, et des modèles économiques sans rapport entre eux.

**Ce qu'il ne signifie pas.** Que le verrou est technique. Dans la plupart des applications, la contrainte dominante est le **cadre d'autorisation du vol hors vue directe**, et secondairement l'assurabilité — deux conditions institutionnelles.

**Ce qu'il vous fait manquer.** Exactement cela : la catégorie économique fait raisonner sur des marchés potentiels alors que la variable décisive est réglementaire.

**Traitement dual.** Ce volume analyse les technologies, les chaînes industrielles, l'économie et la gouvernance. Il ne traite d'aucun paramètre d'emploi.

---


### Swarm intelligence

**Niveau** — cadrage scientifique, employé comme doctrine. **Couches** — décider + relier + agir.

**Ce qu'il désigne.** À l'origine, une famille de méthodes inspirées des collectifs biologiques, où un comportement global émerge de règles locales simples sans coordination centrale.

**Ce qu'il mélange.** La méthode d'optimisation, le comportement collectif observé, et l'emploi coordonné de nombreuses plateformes — trois objets qui n'ont ni les mêmes contraintes ni les mêmes verrous.

**Ce qu'il ne signifie pas.** Nombre. Un grand nombre de plateformes coordonnées depuis un centre n'est pas un essaim ; ce qui définit l'essaim est **l'absence de coordination centrale**, avec les propriétés de robustesse et les difficultés de prévisibilité qui en découlent.

**Ce qu'il vous fait manquer.** **La contrainte de communication.** Une coordination sans centre suppose des échanges locaux, donc de la bande passante, de l'énergie et une tolérance à la latence. C'est là que se situe le verrou, et le cadrage biologique le masque en suggérant que la coordination est gratuite.

**Dans l'atlas** — essaims et coordination distribuée (ch. 16) · perception distribuée (ch. 7).

---


### Cyber-physical systems

**Niveau** — cadrage analytique, l'un des meilleurs de cette partie. **Couches** — toutes.

**Ce qu'il désigne.** Les systèmes où un calcul commande un processus physique en boucle fermée : industrie, énergie, transport, santé, bâtiment.

**Ce qu'il mélange.** Peu de choses, et c'est ce qui en fait un bon cadrage : les objets qu'il regroupe partagent des contraintes réelles — temps de boucle, sûreté, conséquences physiques d'une défaillance, difficulté de mise à jour.

**Ce qu'il ne signifie pas.** Connecté. Un système cyber-physique peut être isolé ; ce qui le définit est l'action sur le monde, pas la connectivité.

**Ce qu'il vous fait manquer.** Peu de chose — mais il faut noter ce qu'il **fait voir**, ce qui est plus rare : que les modèles de menace du système d'information ne s'y transposent pas. La confidentialité y est souvent secondaire ; **l'intégrité des commandes et la disponibilité du contrôle sont primordiales**. Un attaquant n'a besoin de rien lire : altérer une consigne ou retarder une boucle suffit.

**Pourquoi il est employé.** Parce qu'il a rendu visible une catégorie de risque que ni le vocabulaire industriel ni le vocabulaire informatique ne nommaient. C'est un cadrage qui a produit une compétence.

**Dans l'atlas** — architecture de sûreté (ch. 30) · dégradation maîtrisée (ch. 30) · racine de confiance matérielle (ch. 28).

---


## Ce que ces vingt-quatre termes enseignent

Trois observations, avant les deux chapitres suivants.

**Les meilleurs cadrages sont ceux qui rendent visible une contrainte partagée.** *Cyber-physical systems* réunit des objets qui partagent réellement un problème, et il a produit une discipline. *Deep Tech* ou *Climate Tech* réunissent des objets qui partagent un mode de financement ou une finalité, mais aucune contrainte technique — ce sont des catégories utiles à l'investisseur et inutiles à l'ingénieur.

**Les termes les plus employés sont les plus larges, et c'est mécanique.** Un terme large est adoptable par davantage d'acteurs, donc il circule davantage. Sa fréquence dans le discours n'est pas un indice de sa précision — elle en est plutôt l'inverse.

**La question « ce que le terme vous fait manquer » a produit un résultat régulier.** Dans dix-huit cas sur vingt-quatre, ce que la catégorie masque est **une contrainte institutionnelle, économique ou temporelle** : coût par appel, délai de raccordement, cadre d'autorisation, renouvellement du parc, coût de vérification, dépendance résiduelle. Presque jamais une contrainte physique.

C'est cohérent avec ce que le volume 1 avait établi et que la Partie IV vérifiera dossier par dossier : **le verrou est rarement là où le vocabulaire le place.**

---

---


## Chapitre 34 — Industrie, infrastructure et monde programmable

Onze termes qui décrivent moins des technologies que des **projets de transformation**. Leur caractéristique commune : ils sont énoncés avant d'exister, et ils désignent un objectif plutôt qu'un état.

---


### Industrie 4.0 et Industrie 5.0

**Niveau** — récit, à origine institutionnelle. **Couches** — fabriquer, calculer, relier.

**Ce qu'il désigne.** *Industrie 4.0* est né d'un programme public allemand au début des années 2010 pour désigner la mise en réseau des systèmes de production : capteurs, échange de données, pilotage adaptatif. *Industrie 5.0* est apparu ensuite, porté par des institutions européennes, pour y adjoindre des finalités humaines et environnementales.

**Ce qu'il mélange.** Une génération technologique, un programme de politique industrielle et un argument commercial. La numérotation suggère une succession de révolutions industrielles dont l'historiographie est discutée, et dont la quatrième aurait été identifiée avant d'avoir eu lieu.

**Ce qu'il ne signifie pas.** Un état atteint. La très grande majorité des sites de production dans le monde ne relève d'aucune des deux descriptions, et le parc d'équipements industriels se renouvelle sur quinze à trente ans.

**Ce qu'il vous fait manquer.** **L'âge du parc machine.** Une usine s'équipe au rythme de ses investissements, et un site moyen fait cohabiter des équipements de quatre décennies. La catégorie fait raisonner sur une cible, jamais sur la trajectoire de renouvellement qui seule détermine le rythme réel.

**Pourquoi il est employé.** Il a servi de langage commun à des programmes de financement, ce qui est une fonction légitime — mais qui explique sa formulation en objectif plutôt qu'en description.

---


### Smart factory

**Niveau** — doctrine. **Couches** — fabriquer, percevoir, décider.

**Ce qu'il désigne.** Une installation de production instrumentée, dont les données de fonctionnement sont collectées et exploitées pour ajuster les paramètres, anticiper les pannes et adapter les séries.

**Ce qu'il mélange.** Des degrés très éloignés : collecter des données, les visualiser, les analyser, agir automatiquement. Le premier est courant ; le dernier est rare, parce qu'il suppose de confier une commande à un système apprenant dans un contexte où une erreur détruit de la matière.

**Ce qu'il ne signifie pas.** Absence d'opérateurs. L'automatisation déplace le travail vers la supervision, la maintenance et le traitement des exceptions — qui restent des métiers en tension.

**Ce qu'il vous fait manquer.** **Le coût de l'instrumentation d'un existant.** Équiper une ligne neuve est une décision de conception ; équiper une ligne en service suppose des arrêts, des reprises et une intégration à des automates anciens. C'est là que les projets échouent, et le terme ne l'évoque pas.

**Dans l'atlas** — usines autonomes (ch. 18) · métrologie avancée (ch. 18) · jumeaux numériques industriels (ch. 18).

---


### Digital twin — jumeau numérique

**Niveau** — ambigu, et c'est le problème : capacité, plateforme ou doctrine selon l'emploi. **Couches** — calculer, percevoir, décider.

**Ce qu'il désigne.** Un modèle d'un objet ou d'un système réel, alimenté par des données de ce système, utilisé pour observer, simuler ou décider.

**Ce qu'il mélange.** **Cinq objets distincts** portent ce nom : une maquette tridimensionnelle ; un modèle de simulation physique ; un tableau de bord synchronisé sur des capteurs ; un modèle prédictif de comportement ; et un système de commande fondé sur ce modèle. Ils diffèrent par la fidélité exigée, la fréquence de synchronisation et les conséquences d'une erreur.

**Ce qu'il ne signifie pas.** Une copie. **Tout modèle est une représentation qui conserve ce que son concepteur a jugé pertinent** — la question n'est jamais « le jumeau est-il exact ? » mais « qu'a-t-il été construit pour ignorer, et cet aspect est-il négligeable dans mon usage ? ».

**Ce qu'il vous fait manquer.** **L'écart au réel et sa dérive.** Un modèle calé sur un système neuf s'écarte progressivement à mesure que le système s'use. Sans procédure de recalage, le jumeau devient faux sans le signaler — c'est une défaillance silencieuse, au sens de la couche *percevoir*.

**Dans l'atlas** — jumeaux numériques industriels (ch. 18) · sim-to-real (ch. 13).

---


### Software-defined everything

**Niveau** — doctrine. **Couches** — calculer, relier.

**Ce qu'il désigne.** Le déplacement de fonctions historiquement réalisées par du matériel spécialisé vers du logiciel exécuté sur du matériel générique : réseau, stockage, radio, instrumentation, et désormais véhicule.

**Ce qu'il mélange.** Un principe d'architecture et une promesse commerciale de flexibilité. Le principe est réel et ancien ; la promesse suppose que le matériel générique soit assez performant, ce qui dépend entièrement du domaine.

**Ce qu'il ne signifie pas.** Que le matériel disparaît. Il devient générique et se déplace en amont — la contrainte passe de la conception d'un équipement à la disponibilité d'un calculateur suffisant, avec son énergie et sa dissipation.

**Ce qu'il vous fait manquer.** **La surface d'attaque et la dette de mise à jour.** Une fonction devenue logicielle devient corrigeable, donc doit être corrigée, sur toute la durée de vie du produit — qui se compte en années pour un véhicule ou un équipement industriel. Le cadrage met en avant la flexibilité et masque l'obligation de maintenance qu'elle crée.

---


### Industrial metaverse

**Niveau** — récit. **Couches** — interagir, calculer, fabriquer.

**Ce qu'il désigne.** L'usage d'environnements tridimensionnels partagés pour concevoir, former, superviser ou maintenir des installations industrielles.

**Ce qu'il mélange.** Des usages matures — revue de conception en trois dimensions, formation par simulation — et une promesse d'environnement persistant et partagé qui reste largement à l'état de démonstration.

**Ce qu'il ne signifie pas.** Une continuité avec les usages grand public du même mot. Les exigences industrielles portent sur la fidélité géométrique, la traçabilité et l'intégration aux systèmes de gestion, pas sur la présence sociale.

**Ce qu'il vous fait manquer.** **La question de la source de vérité.** Un environnement partagé n'a de valeur que si ce qu'il montre correspond à l'état réel de l'installation — ce qui renvoie au problème de synchronisation du jumeau numérique, et non à la qualité du rendu.

---


### Autonomous enterprise

**Niveau** — récit organisationnel. **Couches** — décider, vérifier.

**Ce qu'il désigne.** Une organisation dont une part croissante des processus de décision courante s'exécute sans intervention humaine.

**Ce qu'il mélange.** Automatisation de processus, aide à la décision, et délégation réelle de décision — trois choses qui n'engagent ni les mêmes responsabilités ni les mêmes garanties.

**Ce qu'il ne signifie pas.** Une entreprise sans salariés. Il signifie un déplacement du travail vers la conception des règles, la supervision et le traitement des cas non prévus.

**Ce qu'il vous fait manquer.** **La question de l'imputation.** Quand une décision automatisée cause un dommage, qui répond ? Le cadrage porte sur l'efficacité et n'aborde jamais cette question, qui est pourtant la première que posera un assureur.

---


### Smart city

**Niveau** — récit à composante politique. **Couches** — percevoir, relier, décider.

**Ce qu'il désigne.** L'instrumentation d'un territoire urbain — mobilité, énergie, eau, déchets, sécurité — et l'usage des données produites pour piloter ces services.

**Ce qu'il mélange.** Des projets d'une ambition et d'une nature incomparables : optimisation d'un réseau de transport, comptage de places de stationnement, gestion de l'éclairage, dispositifs de surveillance. Le terme couvre les quatre sans les distinguer.

**Ce qu'il ne signifie pas.** Un modèle unique. Les réalisations diffèrent radicalement selon les cadres juridiques applicables aux données personnelles et selon les modes de gouvernance locale.

**Ce qu'il vous fait manquer.** **Qui exploite, et pendant combien de temps.** Une ville instrumentée dépend d'opérateurs, de plateformes et de contrats dont la durée est bien inférieure à celle des infrastructures équipées. Le cadrage porte sur la capacité et masque la dépendance contractuelle qu'elle installe.

---


### Smart grid

**Niveau** — infrastructure. **Couches** — alimenter, percevoir, décider, relier.

**Ce qu'il désigne.** Un réseau électrique instrumenté et pilotable, capable d'ajuster production, consommation et stockage à une échelle fine.

**Ce qu'il mélange.** Peu de choses — c'est l'un des termes les plus solides de ce chapitre. Il regroupe des dispositifs qui partagent une contrainte réelle : maintenir l'équilibre instantané d'un réseau qui ne stocke rien.

**Ce qu'il ne signifie pas.** Un remplacement du réseau physique. La flexibilité logicielle ne crée aucune capacité de transport : une production que le réseau ne peut pas évacuer reste inutilisable, quelle que soit l'intelligence du pilotage.

**Ce qu'il vous fait manquer.** **La distinction entre flexibilité et capacité.** C'est la confusion la plus coûteuse du domaine énergétique : piloter finement une pénurie de transport ne la résout pas.

**Dans l'atlas** — réseaux électriques pilotés (ch. 23) · raccordement et files d'attente (ch. 23) · microgrids (ch. 23).

---


### IoT et IIoT

**Niveau** — catégorie industrielle. **Couches** — percevoir, relier, calculer.

**Ce qu'il désigne.** Les objets instrumentés et connectés — grand public pour le premier, industriels pour le second.

**Ce qu'il mélange.** Des objets dont les exigences sont incompatibles : un capteur grand public alimenté par pile, remplacé au bout de deux ans, et un capteur industriel qualifié pour quinze ans en environnement sévère.

**Ce qu'il ne signifie pas.** Une technologie. C'est un mode de déploiement — beaucoup d'objets, peu coûteux, largement distribués.

**Ce qu'il vous fait manquer.** **Le coût de possession à grande échelle.** Un million de capteurs, c'est un million de mises à jour, d'étalonnages, de remplacements de batterie et de fins de vie. La couche *percevoir* le rappelle : à grande échelle, c'est l'étalonnage qui borne la qualité de la donnée, pas la qualité du capteur.

---


### Ubiquitous computing et ambient computing

**Niveau** — récit, ancien pour le premier. **Couches** — calculer, interagir, relier.

**Ce qu'il désigne.** L'idée d'un calcul présent partout et invisible, sollicité sans interface dédiée. Le premier terme date de la fin des années 1980 ; le second en est la reformulation contemporaine.

**Ce qu'il mélange.** Une vision de recherche et une catégorie de produits domestiques.

**Ce qu'il vous fait manquer.** **Trente-cinq ans d'écart entre l'énoncé et la réalisation.** C'est un cas d'école de promesse récurrente : la vision est ancienne, cohérente et jamais entièrement advenue, parce que le verrou n'était pas le calcul mais l'interface — c'est-à-dire la couche où la bande passante d'entrée reste le mur.

---


### Autonomous networks

**Niveau** — doctrine. **Couches** — relier, décider, vérifier.

**Ce qu'il désigne.** Des réseaux de télécommunications capables de se configurer, s'optimiser et se réparer sans intervention, souvent décrits selon une échelle de niveaux inspirée de celle de la conduite automobile.

**Ce qu'il mélange.** L'automatisation de tâches d'exploitation et la délégation de décisions d'architecture.

**Ce qu'il vous fait manquer.** **Le comportement en incident majeur.** Un réseau qui se répare seul en régime courant peut aggraver un incident systémique en propageant des reconfigurations. C'est le mode de défaillance qui compte, et l'échelle de niveaux ne le mesure pas.

**Dans l'atlas** — opérations autonomes (ch. 12) · dégradation maîtrisée (ch. 30).

---
