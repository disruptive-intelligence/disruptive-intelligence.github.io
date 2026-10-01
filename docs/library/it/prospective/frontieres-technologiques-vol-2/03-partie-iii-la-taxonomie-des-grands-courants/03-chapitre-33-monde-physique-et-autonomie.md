---
title: Chapitre 33 — Monde physique et autonomie
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie III — La taxonomie des grands courants
  - index.md
---

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
