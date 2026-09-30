---
title: Agentic AI
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

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
