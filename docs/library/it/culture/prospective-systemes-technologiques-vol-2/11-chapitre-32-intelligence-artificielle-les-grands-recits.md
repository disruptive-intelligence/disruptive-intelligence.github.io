---
title: 'Chapitre 32 — Intelligence artificielle : les grands récits'
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
chapter: 11
chapters: 14
---

Douze termes que vous entendrez cette semaine.

---

### IA générative

**Niveau** — cadrage transversal. **Couches** — apprendre et décider.

**Ce qu'il désigne.** Les systèmes qui produisent du contenu — texte, image, son, code, structure moléculaire — plutôt que de classer ou de prédire une valeur. Le terme s'est imposé en 2022-2023 pour distinguer cette famille des usages antérieurs de l'apprentissage automatique.

**Ce qu'il mélange.** Des architectures très différentes réunies par leur sortie et non par leur mécanisme. Il mélange aussi un type de tâche et un type de produit : « faire de l'IA générative » peut désigner l'entraînement d'un modèle, son intégration, ou son simple usage via une interface.

**Ce qu'il ne signifie pas.** Que le système crée. Il produit des sorties conformes aux régularités de ses données d'entraînement. Le terme ne dit rien non plus du niveau de fiabilité, qui varie de plusieurs ordres de grandeur selon la tâche.

**Ce qu'il vous fait manquer.** La question du **coût par sortie**. Un système génératif est facturé à l'usage ; son économie est celle d'un coût marginal, pas d'un investissement. Le cadrage « IA générative » fait raisonner sur la capacité alors que la contrainte réelle est souvent le prix de l'appel multiplié par le volume.

**Pourquoi il est employé.** Il a permis de nommer une rupture d'usage réelle et de la distinguer de vingt ans d'apprentissage automatique dont les résultats étaient invisibles pour le public.

**Dans l'atlas** — modèles de fondation (ch. 11) · multimodalité (ch. 11) · modèles compacts (ch. 11).

---

### Agentic AI

**Niveau** — cadrage, en cours de stabilisation vers une capacité. **Couches** — apprendre et décider, parfois relier.

**Ce qu'il désigne.** Des systèmes qui décomposent un objectif en étapes, invoquent des outils extérieurs, observent le résultat et poursuivent — au lieu de produire une réponse unique.

**Ce qu'il mélange.** Trois choses de natures très différentes : une **capacité** du modèle à planifier, une **architecture logicielle** d'orchestration qui existait bien avant, et une **doctrine** d'usage consistant à déléguer une tâche entière. Beaucoup de produits dits agentiques sont l'architecture sans la capacité.

**Ce qu'il ne signifie pas.** Autonomie. Un agent exécute des étapes dans un périmètre défini par son concepteur ; l'autonomie suppose de décider dans des situations non prévues. La fiche « automatisation, agentivité, autonomie » du chapitre 12 traite précisément de cette gradation.

**Ce qu'il vous fait manquer.** **La question de la vérification.** Un système qui enchaîne dix étapes sans supervision produit dix occasions d'erreur, et une erreur intermédiaire se propage sans se signaler. Le cadrage met en avant ce que le système peut entreprendre et masque ce qu'il faut contrôler.

**Pourquoi il est employé.** Il nomme un déplacement réel : du modèle qui répond au système qui agit. C'est un bon cadrage, dont l'usage précède la maturité.

**Dans l'atlas** — agents IA (ch. 12) · systèmes multi-agents (ch. 12) · automatisation, agentivité, autonomie (ch. 12).

---

### Modèles de raisonnement

**Niveau** — capacité. **Couches** — apprendre et décider.

**Ce qu'il désigne.** Des modèles entraînés ou configurés pour consacrer davantage de calcul à la production d'une réponse, en décomposant le problème avant de conclure.

**Ce qu'il mélange.** Une technique — allouer du calcul au moment de l'inférence — et une revendication cognitive — « raisonner ». La première est mesurable, la seconde ne l'est pas.

**Ce qu'il ne signifie pas.** Que le système suit une chaîne logique vérifiable. Ce qu'il produit ressemble à un raisonnement et n'a pas les propriétés d'une démonstration : il peut arriver à la bonne conclusion par un chemin faux, et inversement.

**Ce qu'il vous fait manquer.** **Le coût.** Ces modèles consomment beaucoup plus par requête, et l'arbitrage entre qualité et coût par appel est devenu une décision d'architecture. Le terme met en avant la capacité et masque son prix.

**Pourquoi il est employé.** Il désigne une avancée technique réelle : le calcul dépensé à l'inférence améliore certains résultats, ce qui n'était pas évident.

**Dans l'atlas** — modèles de raisonnement (ch. 11) · modèles de fondation (ch. 11).

---

### AGI

**Niveau** — récit. **Couches** — sans objet.

**Ce qu'il désigne.** Rien de vérifiable en l'état. Le terme n'a pas de définition partagée : selon les auteurs, il désigne un système égalant l'humain sur toute tâche cognitive, un système capable d'apprendre n'importe quelle tâche, ou un seuil économique — un système capable d'effectuer une fraction donnée du travail rémunéré.

**Ce qu'il mélange.** Une hypothèse scientifique, un objectif d'entreprise, un seuil contractuel dans certains accords commerciaux, et un objet de débat public sur les risques.

**Ce qu'il ne signifie pas.** Une étape technique identifiable. Aucun test accepté ne permettrait de constater son franchissement, ce qui est le problème central du terme.

**Ce qu'il vous fait manquer.** **Toutes les questions opérationnelles.** Discuter d'AGI conduit à ne pas discuter de fiabilité, de coût par tâche, de domaine d'emploi et de vérification — c'est-à-dire des seules choses qui déterminent ce qu'un système peut faire dans une organisation.

**Pourquoi il est employé.** Il fixe un horizon commun, il structure un débat sur les risques, et il sert d'argument de financement. Ces trois fonctions sont réelles ; aucune n'est technique.

**Traitement dans ce volume.** Le terme est expliqué et n'est pas utilisé comme catégorie d'analyse. Ce n'est pas un jugement sur la question de fond, qui est légitime : c'est l'application de la règle du chapitre 2 — on ne raisonne pas avec un cadrage qu'on ne peut pas délimiter.

---

### Multimodalité

**Niveau** — capacité. **Couches** — percevoir, apprendre et décider.

**Ce qu'il désigne.** La capacité d'un système à traiter conjointement plusieurs types d'entrées — texte, image, son, vidéo, signaux — dans une représentation commune.

**Ce qu'il mélange.** Trois niveaux souvent confondus : accepter plusieurs entrées, les traiter dans un espace partagé, et produire plusieurs types de sorties. Un système « multimodal » peut ne faire que le premier.

**Ce qu'il ne signifie pas.** Que le système perçoit. Il traite des représentations issues de capteurs ; la fiabilité de la chaîne dépend d'abord de ces capteurs, et la couche *percevoir* rappelle qu'aucune mesure n'est parfaite.

**Ce qu'il vous fait manquer.** **L'alignement temporel et spatial** entre modalités. Combiner des sources suppose de savoir quand et où chacune a été acquise — c'est le problème de recalage traité au chapitre 7, et c'est là que la fusion échoue en pratique.

**Dans l'atlas** — multimodalité (ch. 11) · fusion de capteurs (ch. 7) · VLA (ch. 13).

---

### Edge AI

**Niveau** — doctrine. **Couches** — calculer, apprendre et décider, relier.

**Ce qu'il désigne.** L'exécution de traitements d'apprentissage au plus près de la source de données plutôt que dans une infrastructure distante.

**Ce qu'il mélange.** Trois termes voisins que l'usage confond : *edge* désigne une position dans une architecture, *on-device* une exécution sur l'appareil de l'utilisateur, *embarqué* une contrainte de ressources et souvent de temps réel. Ils se recouvrent sans être interchangeables — la fiche comparative du chapitre 25 les sépare.

**Ce qu'il ne signifie pas.** Une technologie. C'est un choix de placement du calcul, motivé par la latence, le coût par appel, la confidentialité ou l'indépendance vis-à-vis d'un réseau.

**Ce qu'il vous fait manquer.** **La mise à jour.** Un modèle distant se corrige en une opération ; un modèle déployé sur un million d'appareils se corrige au rythme du parc. Le cadrage met en avant l'autonomie et masque la dette de maintenance.

**Dans l'atlas** — edge, on-device et embarqué (ch. 25) · modèles compacts (ch. 11) · accélérateurs (ch. 8).

---

### Sovereign AI

**Niveau** — récit, à composante politique. **Couches** — calculer, alimenter, apprendre et décider.

**Ce qu'il désigne.** La volonté d'un État ou d'un ensemble d'États de disposer, sur son territoire et sous son droit, des moyens de développer et d'exploiter des systèmes d'apprentissage : calcul, données, modèles, compétences.

**Ce qu'il mélange.** Des exigences très différentes : localisation des données, propriété des modèles, contrôle de la chaîne matérielle, indépendance opérationnelle. Un dispositif peut satisfaire l'une et aucune des autres.

**Ce qu'il ne signifie pas.** Indépendance. La chaîne de fabrication des accélérateurs, les équipements de lithographie et certains matériaux restent concentrés dans un très petit nombre de lieux — un centre de calcul national fonctionne avec des composants qu'aucun État ne produit seul.

**Ce qu'il vous fait manquer.** **La question du niveau de dépendance résiduelle.** La souveraineté n'est pas binaire : elle se mesure par ce qu'on ne peut pas remplacer, et à quel délai. C'est exactement l'analyse de chaîne d'approvisionnement, et le cadrage la remplace par une déclaration d'intention.

**Traitement dans ce volume.** Analysé comme mécanisme de dépendance, sans position sur l'opportunité des politiques concernées.

---

### AI factories

**Niveau** — catégorie industrielle, en formation. **Couches** — calculer, alimenter.

**Ce qu'il désigne.** Des installations de calcul dimensionnées pour l'entraînement et l'inférence à grande échelle, décrites comme des unités de production plutôt que comme des centres de données classiques.

**Ce qu'il mélange.** Une réalité physique — des bâtiments à très forte puissance électrique — et une métaphore industrielle qui suggère une production continue et prévisible.

**Ce qu'il ne signifie pas.** Une innovation d'architecture. Ce sont des centres de données, avec les contraintes de la couche *calculer* : densité de puissance, évacuation thermique, raccordement électrique.

**Ce qu'il vous fait manquer.** **Le délai de raccordement.** Construire le bâtiment se compte en mois ; obtenir la puissance se compte en années. Le cadrage industriel suggère une capacité qui se déploie au rythme de la demande, alors qu'elle se déploie au rythme du réseau électrique.

**Dans l'atlas** — réseaux électriques pilotés (ch. 23) · raccordement et files d'attente (ch. 23) · accélérateurs (ch. 8).

---

### AI-native

**Niveau** — récit. **Couches** — variable.

**Ce qu'il désigne.** Un produit, une organisation ou une architecture conçus autour de l'apprentissage automatique plutôt que l'ayant ajouté à un existant.

**Ce qu'il mélange.** Une propriété de conception, une posture commerciale et une revendication de génération — le terme sert souvent à distinguer un entrant d'un acteur établi.

**Ce qu'il ne signifie pas.** Une supériorité. Une conception native évite certaines dettes et en crée d'autres, notamment une dépendance forte à des composants dont le comportement n'est pas garanti.

**Ce qu'il vous fait manquer.** **Ce qui se passe quand le composant change.** Un système conçu autour d'un modèle hérite de ses évolutions, de ses dépréciations et de ses variations de comportement. Le cadrage met en avant l'agilité et masque cette dépendance.

---

### AI for Science

**Niveau** — cadrage transversal. **Couches** — apprendre et décider, fabriquer.

**Ce qu'il désigne.** L'usage de méthodes d'apprentissage dans le processus scientifique : prédiction de structures, exploration d'espaces de conception, analyse de grands volumes expérimentaux, pilotage d'instruments.

**Ce qu'il mélange.** Des situations très inégales. Prédire une structure est un problème où la donnée est abondante et la validation possible ; concevoir un matériau nouveau est un problème où la validation expérimentale reste lente et coûteuse.

**Ce qu'il ne signifie pas.** Que la découverte s'accélère globalement. Elle s'accélère là où la génération d'hypothèses était le goulet. Là où le goulet était la vérification, le cadrage déplace le problème sans le résoudre — et l'aggrave, en produisant plus d'hypothèses qu'on ne peut en tester.

**Ce qu'il vous fait manquer.** **Le rapport entre coût d'hypothèse et coût de vérification.** C'est la question centrale du dossier de convergence correspondant, et le cadrage ne la pose jamais.

**Dans l'atlas** — conception de protéines (ch. 20) · laboratoires autonomes (ch. 20) · découverte de médicaments assistée (ch. 20).

---

### Frontier AI

**Niveau** — récit, à usage réglementaire. **Couches** — apprendre et décider.

**Ce qu'il désigne.** Les modèles les plus capables du moment, généralement définis par un seuil de calcul d'entraînement ou par une évaluation de capacités.

**Ce qu'il mélange.** Une catégorie technique — les modèles les plus grands — et une catégorie juridique — ceux soumis à des obligations spécifiques. Les deux ne coïncident pas nécessairement.

**Ce qu'il ne signifie pas.** Les plus performants sur une tâche donnée. Des modèles plus petits et spécialisés surpassent régulièrement les modèles frontière sur des tâches précises.

**Ce qu'il vous fait manquer.** **Le fait que le seuil se déplace.** Une définition par un niveau de calcul devient obsolète à mesure que le calcul devient moins cher — ce qui pose un problème réel aux dispositifs réglementaires qui l'emploient.

---

### Modèle de fondation

**Niveau** — ambigu : plateforme dans l'atlas, récit dans l'usage courant. **Couches** — apprendre et décider.

**Ce qu'il désigne.** Un modèle entraîné à grande échelle sur des données larges, destiné à être adapté à de nombreuses tâches en aval plutôt qu'à une seule.

**Ce qu'il mélange.** L'objet technique et le modèle économique : le terme désigne à la fois une manière d'entraîner et une manière de vendre — un socle réutilisable, avec un rapport de dépendance entre celui qui l'entraîne et ceux qui l'adaptent.

**Ce qu'il ne signifie pas.** Généralité. Un modèle de fondation est bon là où ses données sont denses ; l'adaptation en aval ne crée pas de compétence là où le socle n'en avait pas.

**Ce qu'il vous fait manquer.** **La question de la dépendance.** Construire sur un socle qu'on n'a pas entraîné, dont on ne connaît pas les données et qui peut changer de comportement, est une dépendance au sens du chapitre 2 — et elle est rarement traitée comme telle.

---


## Chapitre 33 — Monde physique et autonomie

Douze termes, dont plusieurs sont employés comme s'ils étaient synonymes alors qu'ils désignent des objets de quatre niveaux différents.

---

### Physical AI

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


## Chapitre 35 — Deep Tech et grands regroupements industriels

Douze catégories qui ne correspondent à **aucune famille scientifique**. Elles regroupent des objets par leur mode de financement, leur finalité ou leur secteur d'application — jamais par leurs contraintes techniques.

**Pourquoi elles méritent un chapitre.** Parce qu'elles gouvernent les budgets, les appels à projets, les politiques publiques et les organigrammes. Vous les rencontrerez plus souvent que n'importe quel terme technique de cet atlas, et les employer sans savoir ce qu'elles regroupent conduit à des comparaisons impossibles.

---

### Deep Tech

**Niveau** — catégorie économique. **Couches** — toutes, sans discrimination.

**Ce qu'il désigne.** Les entreprises dont l'activité repose sur une avancée scientifique ou technique substantielle, par opposition à celles reposant sur un modèle commercial ou un logiciel d'assemblage.

**Ce qu'il mélange.** Un contenu scientifique, un profil de risque et un besoin de capital patient. Ces trois traits sont corrélés sans coïncider : il existe des activités très scientifiques et peu capitalistiques, et l'inverse.

**Ce qu'il ne signifie pas.** Une famille technologique. Une entreprise de biologie synthétique et une entreprise de photonique n'ont aucune contrainte commune ; elles partagent un horizon d'investissement.

**Ce qu'il vous fait manquer.** **La question du marché.** La catégorie met en avant l'intensité scientifique et laisse entièrement de côté qui achètera, combien, et à la place de quoi. C'est précisément la condition qui fait échouer le plus grand nombre de ces entreprises.

**Pourquoi il est employé.** Il a servi à justifier des instruments de financement à horizon long, là où les instruments existants étaient calibrés sur des cycles courts. C'est une fonction légitime et strictement financière.

---

### Frontier Tech et Hard Tech

**Niveau** — catégories économiques, quasi synonymes de la précédente.

**Ce qu'ils désignent.** *Hard Tech* insiste sur la difficulté d'ingénierie et sur la présence de matériel ; *Frontier Tech* sur la proximité avec la recherche. Les périmètres se recouvrent largement avec *Deep Tech*.

**Ce qu'ils vous font manquer.** Rien de plus que la précédente. **Ils figurent ici pour une raison précise :** rencontrer trois termes voisins conduit à supposer trois catégories distinctes. Il n'y en a qu'une, avec trois accents. Savoir qu'ils sont interchangeables évite de chercher une distinction qui n'existe pas.

---

### Climate Tech et Clean Tech

**Niveau** — catégories économiques, par finalité. **Couches** — alimenter, fabriquer principalement.

**Ce qu'ils désignent.** *Clean Tech* est le terme des années 2000, associé aux énergies renouvelables et à l'efficacité. *Climate Tech* l'a remplacé dans les années 2020, avec un périmètre plus large incluant l'adaptation, la mesure et le captage.

**Ce qu'ils mélangent.** Des objets sans aucune contrainte technique commune : un logiciel de comptabilité carbone, un procédé de production d'acier, une chimie de batterie, un service d'assurance paramétrique.

**Ce qu'ils ne signifient pas.** Une performance environnementale établie. L'appartenance à la catégorie relève d'une déclaration d'intention, pas d'une mesure.

**Ce qu'ils vous font manquer.** **L'échelle et le délai.** Une technologie de réduction d'émissions ne compte que par le produit de son effet unitaire et de son déploiement, sur un calendrier donné. La catégorie regroupe indifféremment des dispositifs dont l'effet potentiel diffère de plusieurs ordres de grandeur.

**Remarque de vocabulaire utile.** Le remplacement de *Clean Tech* par *Climate Tech* suit un cycle antérieur d'enthousiasme et de reflux. Le changement de nom d'une catégorie après un reflux est un phénomène régulier, et il vaut la peine de le remarquer : il indique que le récit a été renouvelé, pas nécessairement la technologie.

---

### BioTech et HealthTech

**Niveau** — catégories industrielles. **Couches** — fabriquer, percevoir, apprendre.

**Ce qu'ils désignent.** *BioTech* recouvre l'usage du vivant comme moyen de production ou d'intervention — thérapeutique, agricole, industriel. *HealthTech* recouvre les technologies appliquées au soin, y compris purement numériques.

**Ce qu'ils mélangent.** Des régimes réglementaires sans rapport. Un dispositif médical logiciel, un médicament biologique et un service de suivi à distance relèvent de procédures d'autorisation, de délais et de modèles de remboursement entièrement différents.

**Ce qu'ils vous font manquer.** **Le délai et l'attrition.** Dans le thérapeutique, la majorité des candidats échoue, et l'échec est concentré aux étapes les plus coûteuses. La catégorie fait raisonner sur des pipelines et masque la structure de coût qui en découle : le prix de ce qui aboutit inclut celui de tout ce qui a échoué.

---

### Quantum Tech

**Niveau** — catégorie industrielle. **Couches** — calculer, percevoir, relier.

**Ce qu'il désigne.** L'ensemble des technologies exploitant des propriétés quantiques : calcul, capteurs, communication.

**Ce qu'il mélange.** **Trois branches dont la maturité diffère de plusieurs ordres de grandeur.** Les capteurs quantiques sont déployés dans des applications réelles ; les communications quantiques sont expérimentées à des échelles limitées ; le calcul quantique utile reste un objectif. Les réunir sous un mot est la source de confusion la plus fréquente du domaine.

**Ce qu'il ne signifie pas.** Une trajectoire commune. Un progrès en capteurs n'indique rien sur le calcul.

**Ce qu'il vous fait manquer.** **La distinction entre les trois.** C'est un cas où la catégorie coûte directement : un décideur qui entend « le quantique progresse » peut en tirer une conclusion sur une branche à partir d'une information sur une autre.

**Dans l'atlas** — capteurs quantiques (ch. 7) · calcul quantique (ch. 10) · correction d'erreur (ch. 10) · communications quantiques (ch. 10).

---

### SpaceTech et New Space

**Niveau** — catégories industrielles. **Couches** — infrastructure spatiale, relier, percevoir.

**Ce qu'ils désignent.** *SpaceTech* recouvre l'ensemble du secteur. *New Space* désigne plus étroitement un changement de modèle : acteurs privés, production en série, réutilisation, cycles de développement courts, par opposition aux programmes institutionnels.

**Ce qu'ils mélangent.** Le second terme mélange un modèle industriel et une génération d'acteurs. Certains programmes institutionnels ont adopté ce modèle ; certains acteurs récents fonctionnent selon l'ancien.

**Ce qu'ils vous font manquer.** **Que le changement décisif est un changement de régime de production, pas de technologie.** Ce que *New Space* nomme réellement, c'est le passage d'objets uniques à une production répétée — ce qui permet un apprentissage industriel que le spatial n'avait jamais connu. Le cadrage par les acteurs masque le mécanisme.

**Dans l'atlas** — lanceurs réutilisables (ch. 26) · constellations (ch. 26) · charges utiles et miniaturisation (ch. 27).

---

### NeuroTech

**Niveau** — catégorie industrielle. **Couches** — percevoir, interagir, décider.

**Ce qu'il désigne.** Les technologies d'interface avec le système nerveux : mesure, stimulation, prothèses, dispositifs de suivi.

**Ce qu'il mélange.** **Le thérapeutique démontré, l'augmentation plausible et la spéculation.** L'écart entre les trois est considérable, et c'est la catégorie où il est le plus souvent effacé dans la présentation publique.

**Ce qu'il vous fait manquer.** **Le nombre de patients et la durée.** Les résultats les plus spectaculaires portent sur un très petit nombre de personnes, sur des durées limitées, avec des dispositifs dont la durabilité en milieu biologique est le verrou principal.

**Dans l'atlas** — interfaces cerveau-machine (ch. 31) · neuroprothèses (ch. 31) · interfaces neuromusculaires (ch. 31).

---

### Advanced Materials et Advanced Manufacturing

**Niveau** — catégories industrielles. **Couches** — fabriquer.

**Ce qu'ils désignent.** Les matériaux aux propriétés supérieures ou nouvelles, et les procédés de production intégrant instrumentation, adaptation et automatisation.

**Ce qu'ils mélangent.** Le qualificatif « avancé » n'a aucune définition stable : il désigne ce qui est récent relativement à une pratique de référence, laquelle diffère selon les secteurs.

**Ce qu'ils vous font manquer.** **Le couple matériau-procédé.** Un matériau annoncé n'est disponible que lorsqu'un procédé de mise en œuvre existe, est qualifié et est industrialisé. La catégorie fait raisonner sur les propriétés et masque le procédé, qui est le verrou.

---

### Defense Tech et Dual-use Tech

**Niveau** — catégories industrielles et réglementaires. **Couches** — toutes.

**Ce qu'ils désignent.** *Defense Tech* recouvre les technologies destinées à des usages de défense. *Dual-use* désigne celles susceptibles d'usages civils et militaires, ce qui déclenche des régimes de contrôle à l'exportation.

**Ce qu'ils mélangent.** Une destination et un statut juridique. Le second est établi par des listes de contrôle qui varient selon les juridictions et évoluent — de sorte que le périmètre du terme est mouvant par construction.

**Ce qu'ils vous font manquer.** **L'effet du contrôle sur la trajectoire.** Un classement en double usage modifie les délais, les partenaires accessibles, les financements et parfois la localisation d'une activité. C'est une contrainte de diffusion de premier ordre, et le cadrage par la destination ne l'évoque pas.

**Traitement dans ce volume.** Les technologies duales sont analysées sous l'angle industriel, économique, réglementaire, de sûreté et de gouvernance. Le volume ne fournit aucun paramètre d'emploi, aucune méthode opérationnelle, aucune information conférant une capacité concrète — y compris lorsque cette information est publiquement accessible.

---

### Trust Technologies

**Niveau** — catégorie émergente. **Couches** — vérifier.

**Ce qu'il désigne.** L'ensemble des dispositifs établissant l'origine, l'intégrité et l'autorité d'une donnée, d'un contenu ou d'une action : identité, attestation, provenance, cryptographie avancée.

**Ce qu'il mélange.** Des objets qui partagent effectivement une fonction — c'est un cadrage plutôt cohérent — mais dont les niveaux de maturité vont du déployé depuis vingt ans à l'expérimental.

**Ce qu'il vous fait manquer.** **La distinction entre authenticité et véracité.** Ces technologies attestent l'origine et la non-altération. Aucune n'atteste qu'une donnée est vraie. Un capteur compromis qui signe correctement une mesure fausse produit une donnée authentique et fausse — et c'est le point le plus important de toute la couche *vérifier*.

**Dans l'atlas** — identité machine (ch. 29) · attestation (ch. 28) · provenance et authenticité (ch. 29) · cryptographie post-quantique (ch. 29).

---


## Clôture de la Partie III — L'exercice des cinq termes

Vous avez parcouru quarante-cinq termes. Voici l'exercice qui résume ce que cette partie devait produire.

**Cinq mots que vous entendrez dans la même phrase :**

| Terme | Niveau | Couches | Ce qu'il ne faut pas en faire |
|---|---|---|---|
| **VLA** | architecture, donc capacité | apprendre et décider | ce n'est pas un robot |
| **Humanoïde** | plateforme | agir — mais dépend de percevoir, décider, alimenter | ce n'est pas la seule forme de robot généraliste |
| **Optronique** | catégorie industrielle | percevoir | ce n'est pas une technologie unique |
| **Service autonomy** | capacité organisationnelle | décider et vérifier | ce n'est pas un produit |
| **Physical AI** | récit, cadrage transversal | percevoir + décider + agir | ce n'est pas une brique comparable à un lidar |

**Ce que ce tableau démontre.** Cinq mots, cinq niveaux différents, et donc cinq types de questions différentes. Demander « faut-il investir dans le VLA ou dans la Physical AI ? » n'a pas de réponse — non parce que la question serait difficile, mais parce qu'elle compare une architecture à un cadrage.

**Ce que vous devez pouvoir faire maintenant.** Prendre cinq termes que vous entendez pour la première fois, leur attribuer un niveau, identifier les couches qu'ils mobilisent, et reformuler la question qui les met en concurrence en questions qui ont une réponse.

Le chapitre 47 vous mettra à l'épreuve sur une technologie absente de cet atlas.

---


## Ce que la taxonomie complète enseigne

Quarante-cinq fiches, et quatre observations que seul le décompte fait apparaître.

**Un.** Dans **trente-quatre cas sur quarante-cinq**, ce que la catégorie masque est une contrainte **institutionnelle, économique ou temporelle** — cadre d'autorisation, coût par appel, délai de raccordement, renouvellement du parc, attrition, contrôle à l'exportation, durée contractuelle. Presque jamais une contrainte physique. Le vocabulaire déplace systématiquement l'attention vers la capacité technique, c'est-à-dire vers la partie du problème qui bloque le moins souvent.

**Deux.** Les meilleurs cadrages regroupent des objets qui **partagent une contrainte réelle** : *cyber-physical systems*, *smart grid*, *trust technologies*. Les moins bons regroupent par finalité — *Climate Tech* — ou par mode de financement — *Deep Tech*. Ces derniers sont utiles à l'investisseur et inutiles à l'ingénieur, ce qui n'est pas un défaut tant qu'on sait à qui ils servent.

**Trois.** Plusieurs termes sont **des cycles de vocabulaire plutôt que des générations technologiques**. *Clean Tech* devenu *Climate Tech*, *ubiquitous computing* devenu *ambient computing*, *intelligent robotics* remplacé par une succession de termes. Le renouvellement d'un nom après un reflux indique que le récit a été refait — pas nécessairement la technologie.

**Quatre.** Les catégories les plus employées sont les plus larges, et c'est mécanique : un terme large est adoptable par davantage d'acteurs, donc il circule davantage. **Sa fréquence dans le discours est un indice inverse de sa précision.**

---

---


## Ouverture de la Partie IV

L'atlas répondait à une question : **qu'est-ce que cet objet ?**

Cette partie en pose une autre : **que se passe-t-il lorsque plusieurs de ces objets deviennent simultanément suffisamment bons ?**

### Ce qu'est une convergence

> Une rupture provient rarement d'une technologie isolée. Elle apparaît lorsque plusieurs capacités deviennent **simultanément suffisamment performantes, suffisamment fiables et suffisamment abordables**.

Les trois « suffisamment » sont indissociables. Une capacité excellente mais chère ne converge pas. Une capacité bon marché mais peu fiable non plus. **C'est la conjonction qui produit l'effet** — et c'est pourquoi le raisonnement porte toujours sur **le maillon le plus en retard**, jamais sur le plus avancé.

### Ce que chaque dossier produit

Dix mouvements, dans cet ordre, pour les six dossiers :

**① La capacité recherchée** — formulée précisément, sans terme de récit.
**② Les briques nécessaires** — quelles couches, quelles entrées d'atlas.
**③ Ce qui empêche encore** — verrous hiérarchisés, pas énumérés.
**④ Le maillon le plus en retard** — un seul, désigné et argumenté.
**⑤ Quel mur domine** — parmi les cinq du volume 1.
**⑥ Ce qui est en train de changer** — technologies, coûts, infrastructures.
**⑦ Ce que la convergence débloquerait** — usages, échelles, acteurs.
**⑧ Le verrou suivant** — le problème déplacé.
**⑨ La chronologie conditionnelle** — trois à cinq étapes, aucune date.
**⑩ Signaux et réfutation** — observables, datables.

**Les mouvements ④, ⑤ et ⑧ sont ceux qu'aucun autre ouvrage ne produit.** Ce sont eux qui justifient l'existence de cette partie à côté de l'atlas.

### Une thèse à éprouver

L'atlas et la taxonomie ont produit une thèse, et cette partie va la tester dossier par dossier :

> **Le maillon le plus en retard se situe rarement dans la couche qui donne son nom à la convergence — et le plus souvent dans une contrainte industrielle ou institutionnelle.**

Elle sera vérifiée quatre fois et partiellement contredite deux fois. **Le chapitre 41 fera le bilan de cette confrontation**, sans arrondir le résultat.

### Aucune date

Aucun de ces dossiers ne comporte de calendrier. Le volume 1 a établi pourquoi : quelques points d'écart sur un taux d'apprentissage produisent, sur vingt ans, un ordre de grandeur de différence. **Une méthode qui produirait des dates à partir de paramètres aussi dispersés serait fausse par construction.**

Ce que les dossiers produisent à la place est réfutable, hiérarchisant et résistant au temps.

---


## Chapitre 36 — La robotique généraliste

### ① La capacité recherchée

**Formulation courante, et pourquoi elle ne convient pas.** « Un robot capable de tout faire » n'est pas une capacité analysable : elle n'a pas de seuil, pas de mesure, pas de condition de vérification.

**Formulation retenue.**

> **Manipuler des objets variés, dans des environnements non préparés, sans reprogrammation pour chaque tâche — au point que le seuil de variété au-delà duquel la spécialisation cesse d'être rentable se déplace significativement.**

**Ce que cette formulation change.** Elle rend la question économique et mesurable. Un robot spécialisé et bon marché bat un robot généraliste et cher sur toute tâche répétitive : **la généralité ne devient pertinente que là où la variété rend la spécialisation impossible.** Cette frontière existe aujourd'hui, elle est calculable, et la question est de savoir de combien elle se déplacera.

**Ce que le dossier ne traite pas.** La forme des machines. La question « humanoïde ou morphologie spécialisée » est un moyen, pas la capacité — et la monographie du chapitre 15 traite déjà la plateforme. **Ce dossier considère toutes les morphologies** : bras fixe, robot mobile manipulateur, humanoïde, combinaison de plateformes.

**Le récit associé.** C'est ce que le marché appelle *Physical AI* ou *general-purpose robotics*. Les fiches des chapitres 33 le situent ; ce dossier l'analyse.

---

### ② Les briques nécessaires

| Couche | Ce que la convergence en attend | Entrées d'atlas |
|---|---|---|
| **Percevoir** | perception en contact, estimation de pose incertaine | peau électronique et tactile (7) · fusion de capteurs (7) · lidar (6) · caméras événementielles (6) |
| **Apprendre** | correspondance observation-commande, origine des données | VLA (13) · modèles du monde (13) · apprentissage par imitation (13) · sim-to-real (13) · modèles de fondation robotiques (13) |
| **Agir** | ce qui limite le geste, ce qui s'use | manipulation et préhension (14) · actionneurs (15) · mains et préhenseurs (15) · téléopération (15) |
| **Alimenter** | boucle masse-énergie, autonomie réelle | lithium-ion (21) |
| **Vérifier** | comportement quand le geste rate | dégradation maîtrisée (30) · détection de sortie de domaine (30) |

**Dix-sept entrées mobilisées** — la dépendance la plus large de tous les dossiers.

**Observation immédiate, et elle est contre-intuitive.** La couche *apprendre* fournit cinq entrées, la couche *agir* quatre. **La convergence dite « robotique » dépend plus fortement de l'apprentissage que de la mécanique** — ce qui n'apparaît dans aucun des récits qui la désignent.

---

### ③ Ce qui empêche encore

Quatre verrous, hiérarchisés.

**Premier — la fiabilité de la manipulation en contact.** Une démonstration montre une saisie réussie ; une exploitation exige un taux d'échec assez faible pour que le traitement des échecs coûte moins que le gain. **L'écart se compte en ordres de grandeur**, et il n'est pas visible dans une vidéo. Le chapitre 14 en a donné les quatre causes : le contact change brutalement la dynamique, il faut contrôler des forces et non des positions, les objets diffèrent alors qu'ils se ressemblent, et certaines erreurs sont irréversibles.

**Deuxième — les données d'interaction physique.** L'apprentissage de tâches variées exige des exemples associant observation, instruction et action réelle. Ils s'acquièrent **une démonstration à la fois**, généralement par téléopération. Il n'existe aucun équivalent physique d'un corpus textuel collecté en ligne, et les données recueillies sur une plateforme ne se transposent pas directement sur une autre.

**Troisième — le coût de l'actionnement et de la maintenance.** Les actionneurs dominent le coût d'une machine multi-articulée, et leur baisse dépend de la série. La maintenance croît avec le nombre d'articulations sollicitées, et le jeu qui apparaît avec l'usure rend la machine imprécise **sans que ses capteurs le voient**.

**Quatrième — l'énergie embarquée.** La boucle masse-énergie borne l'autonomie : ajouter de la batterie ajoute de la masse qu'il faut déplacer. Le gain est moins que proportionnel, et il existe un point au-delà duquel ajouter n'apporte plus rien.

---

### ④ Le maillon le plus en retard

**Deux candidats sérieux, et il faut trancher.**

**La fiabilité domine ; la donnée la conditionne.**

Voici l'argument. Si les données étaient abondantes et partagées, la fiabilité progresserait — c'est le pari des architectures du chapitre 13. Mais si la fiabilité atteignait le seuil d'exploitation sans surveillance, le déploiement s'engagerait, et **le déploiement produirait des données**. Les deux se conditionnent mutuellement.

**Ce qui départage : l'ordre d'observabilité.** On peut mesurer un taux de succès ; on ne peut pas mesurer directement « la disponibilité des données ». Et surtout, **c'est la fiabilité qui décide de l'engagement économique** : un exploitant n'accepte pas une machine à 90 % de succès, quelle que soit la quantité de données ayant servi à l'entraîner.

**Conclusion du dossier.** Le maillon le plus en retard est **la fiabilité de la manipulation en environnement varié**, et le facteur qui la conditionne est **la disponibilité de données d'interaction mutualisées**.

**Position par rapport à la thèse du volume.** Le maillon en retard se situe **dans la couche éponyme** — *agir* — avec un conditionnement par *apprendre*. **La thèse est ici partiellement contredite**, et c'était prévu : quand la couche éponyme est celle où se joue le contact physique, le verrou peut y rester.

---

### ⑤ Quel mur domine

**Deux murs, parmi les cinq du volume 1.**

**Le rendement de production**, au sens du taux de succès. Un robot dont le geste échoue une fois sur cent produit, à l'échelle d'une ligne, un flux d'incidents dont le traitement dépasse le gain. **C'est la même arithmétique que le rendement de fabrication au chapitre 8** : la pénalité n'est pas proportionnelle, elle est inverse.

**La défaillance silencieuse**, sous trois formes. Un préhenseur usé continue de saisir, moins bien, sans le signaler. Une articulation avec du jeu positionne mal alors que ses capteurs disent le contraire. Et un modèle hors distribution produit une commande plausible et fausse.

**Ni la dissipation ni le coût du déplacement des données ne dominent** — ce qui écarte deux hypothèses fréquentes.

---

### ⑥ Ce qui est en train de changer

**Les architectures.** Le passage de chaînes modulaires — perception, puis planification, puis contrôle — à des architectures apprenant la correspondance de bout en bout supprime les interfaces où l'information se perdait. C'est un déplacement réel et récent.

**La collecte.** Des efforts de mutualisation de données d'interaction entre laboratoires et industriels sont engagés. **C'est le développement le plus significatif du domaine**, et il porte sur ce que le dossier identifie comme le facteur conditionnant.

**Le transfert depuis la simulation.** Il fonctionne bien pour la locomotion, où la physique est dominée par des effets bien modélisés. Il fonctionne mal pour la manipulation fine, où le contact est mal simulé. **Cet écart indique exactement où le progrès compte.**

**Le coût des plateformes**, en baisse, notamment sur les architectures d'actionnement à réduction faible.

**Ce qui n'a pas changé.** La densité de puissance des actionneurs. Le compromis entre couple, vitesse et précision. Le jeu qui apparaît avec l'usure. Et l'écart entre démonstration et fiabilité exploitable.

---

### ⑦ Ce que la convergence débloquerait

**Le déplacement du seuil de variété.** Aujourd'hui, automatiser une tâche physique suppose une série suffisante pour amortir l'intégration — préhenseur spécifique, adaptation du poste, programmation. Si une machine peut exécuter des tâches variées sans réintégration, **le seuil de série rentable baisse**, et des segments aujourd'hui manuels deviennent accessibles.

**Les usages qui deviendraient possibles**, par ordre de proximité. La manutention en environnement non préparé — chargement, transfert, préparation de commandes variées. L'assemblage en petite série. L'inspection et la maintenance en milieu encombré. Les services à faible valeur unitaire mais forte variété.

**Ce qui resterait hors de portée.** Les tâches exigeant une dextérité fine soutenue, celles où l'erreur est inacceptable, et celles où une machine spécialisée reste moins chère — c'est-à-dire toute production de masse répétitive.

**L'échelle.** Le déploiement serait borné par le nombre de techniciens formés bien avant par la capacité de production — mécanisme établi au volume 1.

---

### ⑧ Le verrou suivant

**La maintenance et les compétences de terrain.**

Si la fiabilité franchit le seuil, le goulet devient l'exploitation d'une flotte : pièces de rechange, interventions, étalonnages, mises à jour, diagnostic. **Le nombre de personnes capables d'entretenir ces machines borne le déploiement**, et former un technicien qualifié se compte en années.

**Une conséquence économique, souvent omise.** Le coût total de possession d'une flotte robotique est dominé par la maintenance et non par l'acquisition. **Un exploitant qui raisonne sur le prix d'achat se trompe de poste.**

**Et un verrou de second ordre.** Si les machines deviennent nombreuses et partagent des modèles appris, une défaillance de modèle affecte simultanément toute la flotte — c'est une défaillance de mode commun, et elle n'existe pas avec des machines programmées individuellement.

---

### ⑨ La chronologie conditionnelle

```text
① si des données d'interaction physique mutualisées atteignent une taille
   permettant un transfert mesurable entre plateformes différentes
        → alors la fiabilité en environnement varié devient le maillon limitant

② si la fiabilité franchit le seuil d'exploitation sans surveillance continue
   sur une famille de tâches
        → alors le coût de l'actionnement et de la maintenance devient limitant

③ si ce coût baisse par la série et si les compétences de maintenance
   se constituent
        → la généralité s'étend aux environnements à variété moyenne

④ si le coût ne baisse pas ou si les compétences manquent
        → la généralité reste confinée aux environnements à forte variété
          et forte valeur, où le coût est absorbable
```

**Lecture.** L'étape ④ n'est pas un échec : c'est une trajectoire, et c'est celle qui décrit l'état actuel. Une convergence qui reste confinée à un segment de valeur n'a pas échoué — elle a trouvé son domaine.

---

### ⑩ Signaux et réfutation

**Signaux de progression, par ordre d'informativité.**

**Un jeu de données d'interaction partagé** dont la taille et la diversité de plateformes sont publiées, et dont on démontre le transfert.

**Des données d'exploitation publiées par un tiers** : taux d'intervention humaine, disponibilité, coût de maintenance sur une flotte en production pendant plusieurs mois. **C'est le signal le plus difficile à obtenir et le plus décisif.**

**Une baisse du coût des actionneurs à couple élevé**, observable sur les catalogues.

**Une offre d'assurance** couvrant l'exploitation de machines de manipulation en environnement partagé.

**Signaux qui ne sont pas informatifs.** Une démonstration, quelle que soit son impressionnante variété. Une annonce de production en série, qui est un objectif. Un nombre de plateformes livrées, qui ne dit rien de leur usage.

**Ce qui réfuterait l'analyse.**

**Le taux de succès plafonne** malgré l'augmentation des données mutualisées — ce qui indiquerait que la donnée n'était pas le facteur conditionnant.

**Le coût de maintenance par unité ne baisse pas** avec la taille de la flotte, ce qui invaliderait l'étape ③.

**Les déploiements annoncés se révèlent être des environnements structurés déguisés** — objets présentés en position connue, scène préparée. Ce serait le signe que le seuil de variété n'a pas bougé.

**Et une réfutation de la formulation elle-même** : si des machines spécialisées et bon marché captaient les segments visés avant que la généralité n'arrive, la question deviendrait sans objet. **C'est une trajectoire possible et elle n'est pas dans les récits.**

---
