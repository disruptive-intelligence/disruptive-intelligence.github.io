---
title: Chapitre 45 — Les dépendances que personne n'a décidées
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
chapter: 13
chapters: 14
---

### ① Ce qui devient abondant

**Les briques communes réutilisables**, disponibles à un coût si faible que les reconstruire n'est jamais le choix rationnel : une référence de temps et de position, un jeu de primitives cryptographiques, une identité machine, un modèle de fondation tiers, une bibliothèque, une capacité de calcul louée.

**Et c'est une bonne chose** — c'est même le mécanisme de diffusion décrit au chapitre 1. Chaque réutilisation est individuellement rationnelle, économe et sans alternative défendable au moment où elle est faite.

**Précision nécessaire, et elle définit le chapitre.** Il ne traite pas des dépendances **choisies** — un fournisseur, un contrat, un risque identifié et arbitré. Il traite de celles qui se constituent **par agrégation** : le chapitre 2 les nomme *infrastructures*, au sens de ce dont d'autres dépendent sans l'avoir choisi ni le contrôler. **Personne ne les a décidées, et pourtant elles existent.**

**Le volume 1 avait signalé ce phénomène comme un angle mort de sa propre méthode**, parce qu'une grille qui interroge une technologie à la fois ne peut pas voir une dépendance qui n'appartient à aucune d'entre elles. L'atlas en a produit cinq cas : positionnement et temps, congestion orbitale, cryptographie déployée, identité machine, modèles de fondation tiers.

---

### ② Ce qui devient rare

**La substituabilité.**

**Le mécanisme.** Une brique réutilisée par tout le monde cesse d'avoir des concurrents, non parce qu'elle les élimine, mais parce que **personne n'a plus intérêt à financer une alternative dont le seul usage serait de ne pas servir.** Le repli existe parfois techniquement — la navigation sans référence satellitaire en est l'exemple documenté au chapitre 6 — mais il est rarement entretenu, rarement exercé, et son coût réapparaît entièrement le jour où il faudrait s'en servir.

**La connaissance de sa propre dépendance.** Peu d'organisations savent dire de quelles briques leurs systèmes dépendent au troisième niveau. **Ce n'est pas de la négligence** : la dépendance est invisible dans les performances, elle n'apparaît dans aucune spécification, et elle ne se manifeste qu'à la défaillance.

**Le temps de sortie.** La cryptographie déployée en est le cas d'école : le chapitre 29 a établi qu'une migration porte sur un parc, des protocoles, des certifications et des produits embarqués dont la durée de vie dépasse la décennie. **Ce qui a été adopté en quelques années se remplace en quelques décennies** — et la crypto-agilité est précisément la reconnaissance de ce déséquilibre.

**Et l'autorité de gestion, dont le degré varie fortement selon les cas.** Le spectre fait exception : il dispose de régimes d'allocation et d'autorités de régulation nationales et internationales dotées d'un pouvoir contraignant réel. **Les quatre autres cas en sont dépourvus ou n'en ont qu'une forme coordinatrice sans sanction.** Les débris orbitaux le montrent sur un bien physique : chaque acteur a intérêt à utiliser la ressource, aucun n'a intérêt à en financer l'entretien, et la dégradation est le résultat agrégé de comportements dont aucun n'est fautif — **c'est un problème de bien commun mal gouverné, pas d'absence universelle de gouvernance.**

---

### ③ Ce qui ne change pas

**La structure d'incitation.** Prendre la brique la moins coûteuse reste, pour chaque acteur pris isolément, la bonne décision — y compris pour celui qui a parfaitement compris le mécanisme décrit ici. **Aucun progrès technique ne modifie cela**, parce que le problème n'est pas dans la brique.

**L'asymétrie entre constitution et sortie.** Une dépendance se constitue sans coordination, gratuitement, par addition de choix indépendants. Se défaire en suppose une : quelqu'un doit payer un coût présent et certain contre un risque futur et diffus, sans en tirer d'avantage compétitif. **Ce n'est pas une difficulté technique, c'est une difficulté d'agrégation** — et elle est aussi ancienne que la notion de bien commun.

**L'invisibilité tant que cela fonctionne.** Une infrastructure qui tient ne produit aucun signal. **La qualité d'une dépendance ne se lit jamais dans le fonctionnement nominal**, ce qui est la raison pour laquelle la Partie I recommandait d'interroger explicitement les briques d'une capacité plutôt que ses performances.

**Et le fait que le stock physique d'un bien commun ne s'étend pas.** Le nombre d'orbites utiles et la largeur du spectre sont bornés par la physique. **Ce qui augmente n'est pas le stock, c'est le service qu'on en tire** : efficacité spectrale, réutilisation spatiale des fréquences, coordination d'usage. Cette marge est réelle et considérable — elle repousse la contrainte, elle ne la supprime pas, et elle se paie en complexité de coordination, c'est-à-dire en gouvernance.

---

### ④ Le rythme imposé

**Constitution : quelques années.** Le temps qu'une brique devienne le choix par défaut.

**Révélation : instantanée.** La dépendance devient visible au moment exact où elle défaille, et pas avant.

**Sortie : de quelques mois à plusieurs décennies**, selon ce qui porte la dépendance. Une brique purement logicielle peut se remplacer vite quand une alternative existe ; **dès qu'un parc matériel, un protocole déployé ou une certification sont en jeu, l'ordre de grandeur devient la décennie**, et c'est le cas des cinq exemples traités ici.

**La conséquence est le résultat central du chapitre.** La fenêtre où l'on pourrait décider quelque chose est ouverte **avant** l'incident, quand rien ne l'indique ; elle se referme quand l'incident survient, puisqu'il ne reste alors que la durée de sortie. **L'attention et la décision sont systématiquement en décalage de phase**, et c'est structurel : ce n'est pas un défaut d'organisation, c'est la forme du problème.

---

### ⑤ Les positions en présence

**Le marché produira les alternatives.** Argument : dès qu'une dépendance devient une rente ou un risque assurable, un fournisseur concurrent apparaît. **Hypothèse sous-jacente** : le coût de commutation reste franchissable et l'alternative peut atteindre l'échelle où elle devient crédible — ce qui est plausible pour un service logiciel, douteux pour une constellation ou une référence de temps.

**Il faut une obligation publique de résilience.** Argument : le coût est présent, le bénéfice est diffus, donc seul un mandat le fait porter. **Hypothèses sous-jacentes**, au nombre de deux : qu'un régulateur puisse imposer un coût certain contre un risque incertain, et que le périmètre réglementaire coïncide avec celui de la dépendance — or il ne coïncide pas, puisqu'elle est transnationale par construction.

**La redondance technique suffit.** Argument : doubler les sources traite le problème. **Hypothèse sous-jacente** : les redondances sont indépendantes. **Elle est fausse dès qu'elles partagent une brique commune** — deux constellations distinctes peuvent dépendre de la même référence de temps, deux fournisseurs distincts d'un même modèle sous-jacent. La redondance apparente est le mode de défaillance le plus fréquent de ce chapitre.

**Ce que ce volume constate.** Les cinq cas ont été identifiés séparément, dans des couches différentes, et présentent **le même mécanisme** : agrégation de décisions individuellement rationnelles, absence d'autorité, invisibilité jusqu'à la défaillance, asymétrie entre constitution et sortie. C'est un constat, pas une position.

**Et il faut signaler le déséquilibre de preuve.** L'existence des dépendances est documentée et vérifiable cas par cas. **L'efficacité comparée des remèdes ne l'est pas** : aucun des trois n'a été mis à l'épreuve à l'échelle où il prétend agir.

---

### ⑥ Ce qu'il faudrait observer

**L'exercice réel d'un repli**, et non son existence sur le papier : une opération conduite sans référence satellitaire, une bascule vers un fournisseur alternatif effectivement réalisée. **Un plan de continuité non exercé n'est pas une information.**

**La part d'un parc effectivement migrée** vers des primitives cryptographiques de remplacement, par secteur. C'est la grandeur la plus directement mesurable du chapitre, et elle mesure une vitesse de sortie.

**Le nombre d'acteurs capables de fournir une brique**, à distinguer soigneusement du nombre d'offres commerciales : plusieurs offres peuvent reposer sur un fournisseur unique.

**L'apparition d'un mandat de gestion contraignant** sur un bien commun — orbites, spectre, source de temps. **Ce serait l'événement le plus significatif de ce chapitre**, et il n'est pas survenu.

**Le prix de l'assurance** couvrant l'indisponibilité d'une brique commune, quand il existe : un assureur estime ce qu'un discours de résilience ne dit pas.

**Signaux non informatifs.** Les annonces de souveraineté. Le nombre de fournisseurs listés dans un catalogue. Les déclarations d'indépendance technologique non assorties d'un calendrier de migration.

---


## Clôture de la Partie V

### Trois observations, qu'aucun chapitre ne produisait seul

#### Une — Ce qui devient rare est presque toujours une capacité d'aval

Quatre chapitres, quatre goulets : la **vérification** quand produire du plausible devient gratuit ; la **maintenance et la responsabilité** quand les machines agissent ; la **qualification** quand observer devient permanent ; la **substituabilité** quand les briques deviennent communes.

**Aucun de ces goulets n'est une capacité de production.** Tous relèvent de ce qui vient après : établir, entretenir, opposer, remplacer. **C'est le même résultat que celui de la Partie IV**, obtenu par un chemin différent — l'atlas et les convergences l'avaient produit sur les technologies, cette partie le produit sur les systèmes.

#### Deux — Le mouvement ③ converge vers quatre familles

Sur les quatre chapitres, ce qui ne change pas relève systématiquement de : **la physique** ; **le coût d'établissement d'un fait** ; **le rythme des institutions** ; **la structure d'incitation**.

**C'est une liste courte, et elle est réutilisable.** Devant n'importe quelle transformation annoncée, elle fournit la question de contrôle : laquelle de ces quatre familles la transformation prétend-elle modifier ? **Si la réponse est aucune, l'ampleur annoncée est probablement surestimée.**

#### Trois — L'effet vient du décalage, jamais de la capacité

Dans les quatre chapitres, la capacité nouvelle se diffuse vite et ce qui la borne se déplace lentement. **Le phénomène analysé n'est jamais la capacité elle-même : c'est l'écart entre trois rythmes** — celui de l'usage, celui de l'exploitation, celui du cadre.

Le chapitre 45 en donne la forme la plus dure : **la fenêtre de décision précède le signal qui la justifierait.** Ce constat commande directement la partie suivante, puisqu'il définit ce qu'une veille utile doit chercher — non pas ce qui vient d'arriver, mais ce qui est en train de se constituer sans produire de signal.

---

### Ce que cette partie ne dit pas

**Aucune date**, aucun calendrier, aucun pronostic — comme la Partie IV, et pour la même raison : les déplacements décrits restent valides quand les échéances glissent.

**Aucun arbitrage de valeurs.** Vie privée et sécurité, automatisation et emploi, souveraineté et efficacité : ces arbitrages sont exposés avec leurs hypothèses et laissés au lecteur, parce que les trancher supposerait des jugements qui n'appartiennent pas à un livre technique.

**Aucune position sur ce qu'il faudrait faire.** La partie dit ce qui se déplace, ce qui ne se déplace pas, et ce qu'il faudrait observer pour savoir laquelle des lectures est en train de gagner.

---

### Passage à la Partie VI

Cinq parties ont produit une carte, un vocabulaire, six dossiers de convergence et quatre analyses de déplacement. **Il manque la seule chose qui les rend durables : une méthode pour les tenir à jour.**

La Partie VI traite la veille et la prospective opérationnelle — **actualité contre signal**, suivi des goulets plutôt que des annonces, capacités en attente, décision sous incertitude — et se clôt par cinq affirmations datées et réfutables. **Le chapitre 47 met ensuite l'ensemble à l'épreuve sur une frontière absente de cet atlas.**

---

---


## Ouverture de la Partie VI

Les cinq parties précédentes ont produit une carte. **Une carte se périme.**

Cette partie ne traite donc pas des technologies, mais de **l'entretien de ce que vous venez de lire** : comment savoir ce qui doit être mis à jour, ce qui ne le doit pas, et ce qu'il faut regarder pour l'apprendre avant tout le monde.

Deux chapitres. Le premier expose la méthode de veille et se clôt par cinq affirmations que ce volume prend le risque d'énoncer, avec ce qui les réfuterait. **Le second applique l'ensemble du volume à une frontière qui ne figure pas dans l'atlas** — c'est l'épreuve annoncée à la clôture de la Partie III.

---


## Chapitre 46 — Tenir sa carte à jour

### 46.1 Trois manières d'échouer

**Suivre l'actualité.** Le flux d'information technologique est produit par ceux qui ont intérêt à ce qu'on en parle. Le suivre revient à déléguer son agenda d'attention à des services de communication — ce qui n'est pas une critique morale, mais une observation sur la sélection.

**Suivre les acteurs.** Surveiller quelques entreprises donne une vue précise de ce qu'elles annoncent et aveugle sur ce qui les contraint. **La Partie IV l'a établi : cinq verrous sur six sont hors de la technique**, donc hors du périmètre de ce que les acteurs technologiques communiquent.

**Suivre son propre domaine.** C'est l'échec le plus fréquent chez les professionnels compétents. Le chapitre 3 en donnait déjà la règle : **ne commencez pas par la famille de verrous que vous maîtrisez.** Une veille conduite depuis l'informatique voit des progrès d'algorithme et manque les délais de raccordement, la formation des techniciens et les régimes de responsabilité.

> **Une veille utile ne suit pas des sujets. Elle suit des goulets.**

---

### 46.2 Actualité contre signal

Les deux mots désignent des objets différents, et la distinction est opérationnelle.

**Une actualité est un événement rapporté.** Elle informe sur ce qui s'est passé et sur l'émetteur.

**Un signal est une information qui modifie une position sur un goulet identifié.** Il n'existe donc pas de signal en soi : une information n'est un signal que **relativement à une question que vous vous posiez déjà**.

**Le test en trois questions**, applicable en une minute :

| Question | Ce qu'elle élimine |
|---|---|
| **Quel goulet cette information concerne-t-elle ?** | tout ce qui ne concerne aucun goulet identifié |
| **À quel échelon de preuve se situe-t-elle ?** | l'intention prise pour un fait — chapitre 4 |
| **Qu'aurais-je observé si l'inverse était vrai ?** | ce qui ne pouvait pas être contredit |

**La troisième question est la plus discriminante**, et c'est celle du chapitre 4 appliquée à la veille : une information qui aurait été rapportée de la même façon quel que soit l'état du monde ne vous apprend rien.

**Conséquence pratique.** La liste des goulets se constitue **avant** la veille, pas pendant. Sans elle, tout est intéressant — ce qui est la définition d'une veille inutile.

---

### 46.3 Suivre les goulets

**Le résultat central de la Partie IV fournit la forme du goulet** : ce qui bloque n'est presque jamais une grandeur, c'est **un rapport entre deux grandeurs**. Coût d'acquisition contre coût annuel d'exploitation. Capacité démontrée contre capacité démontrable. Délai de construction contre délai de raccordement. Vitesse de conception contre capacité de production.

**La conséquence pour la veille est directe.** Un progrès sur le numérateur ne déplace rien si le dénominateur ne bouge pas — et c'est exactement ce que le discours public rapporte : des numérateurs.

**Le tableau de bord minimal**, tiré des mouvements ⑥ et ⑩ des Parties IV et V :

| Goulet | La grandeur à suivre | Où elle se lit |
|---|---|---|
| Fiabilité robotique | ratio d'opérateurs par machine | rapports d'exploitants |
| Autonomie mobile | dossiers de sûreté acceptés, offre d'assurance | régulateurs, assureurs |
| Énergie et calcul | délais de raccordement, carnets de commandes d'équipements réseau | gestionnaires de réseau, industriels |
| Découverte accélérée | coût et durée d'un cycle expérimental complet | publications d'installations |
| Perception distribuée | coût complet d'exploitation par capteur et par an | exploitants |
| Bioproduction | capacité qualifiée par site et par produit | autorités, industriels |
| Vérification des contenus | couverture effective des dispositifs de provenance | fabricants, plateformes |
| Dépendances communes | exercices de repli réellement conduits | opérateurs critiques |

**Ces grandeurs ont un point commun, et il est décourageant** : ce sont des grandeurs d'exploitation, et elles sont rarement publiées. **Ce n'est pas une dissimulation** — on publie ce qui progresse, pas ce qui borne. Cela désigne les bonnes sources : **les exploitants avant les concepteurs**, les documents financiers réglementés avant les communiqués, les appels d'offres et les carnets de commandes avant les feuilles de route.

---

### 46.4 Les signaux non informatifs

L'apport le plus original des Parties IV et V est cette liste. **Savoir ce qui ne renseigne pas économise davantage de temps que savoir ce qui renseigne.**

**Récurrents dans tout le volume** : démonstrations, quelle que soit leur variété · records de performance en conditions choisies · nombre d'unités livrées ou lancées · levées de fonds · annonces de production en série, qui sont des objectifs · scores sur jeux de données publics · résolutions ou capacités annoncées · plans de continuité non exercés · annonces de souveraineté sans calendrier de migration · nombre de fournisseurs listés au catalogue.

**Le critère commun** : aucun de ces éléments ne porte sur un rapport, et aucun ne pouvait ressortir différent si l'hypothèse inverse était vraie.

---

### 46.5 Les capacités en attente

**Définition.** Une capacité en attente est une capacité dont **toutes les briques sont disponibles sauf une**, identifiée.

**Pourquoi cette notion est la plus utile de la veille.** Une capacité en attente se diffuse vite lorsque son maillon cède, parce que tout le reste est déjà prêt et déjà amorti. **La surprise n'est jamais l'apparition de la capacité : c'est la rapidité qui suit.** Inversement, une capacité dont trois briques manquent ne surprendra personne, même si elle est plus spectaculaire.

**Les six dossiers de la Partie IV en fournissent la liste**, et chacun nomme son maillon : la fiabilité en environnement non structuré · la démonstration de sûreté opposable · le raccordement et le délai d'infrastructure · le cycle expérimental physique · le coût d'exploitation d'un parc de capteurs · la capacité de bioproduction qualifiée.

**La question de veille se réduit alors à une seule**, posée maillon par maillon : *ce maillon a-t-il bougé, et l'ai-je appris d'un exploitant ou d'un concepteur ?*

---

### 46.6 Maintenir sa carte

**Le volume est instrumenté pour cela**, et c'est l'objet des deux lignes de chaque fiche.

**La ligne ⏱ se balaye, elle ne se relit pas.** Elle est au même endroit et dans la même syntaxe partout : une révision se conduit en parcourant les seules lignes ⏱, sans rouvrir les fiches.

**La ligne 🔄 se déclenche.** Elle nomme un événement observable dont la survenue rend la fiche obsolète. Tant qu'il ne survient pas, la fiche tient — **y compris si le sujet fait l'actualité.** C'est la protection la plus efficace contre la réaction au bruit.

**Le corps de fiche ne se met pas à jour, il se remplace ou se retire.** Le critère de retrait est celui de l'admission : **une entrée qui cesse d'être un terme que le lecteur risque de rencontrer sort de l'atlas** au lieu d'être actualisée. Une carte qui ne perd jamais d'entrées devient un cimetière de vocabulaire.

**Et la règle d'ajout est une règle d'échange.** Toute entrée ajoutée au-delà du plafond en remplace une ou en fusionne deux. Sans cette règle, la carte grossit jusqu'à cesser d'être consultable — ce qui est le seul mode de mort d'un atlas.

> **Rythme praticable.** Balayage des ⏱ deux fois par an. Réexamen d'une fiche uniquement si sa ligne 🔄 s'est déclenchée. Revue du périmètre — ajouts et retraits — une fois par an, jamais en continu.

---

### 46.7 Décider sous incertitude

La veille ne sert à rien si elle ne produit pas de décisions. Or les décisions dont il est question ici se prennent **sans savoir**, et c'est une situation normale, pas un échec de l'analyse.

**Première distinction — l'incertitude n'est presque jamais où on la place.** Le volume retrouve le même constat par trois lectures distinctes : l'incertitude porte rarement sur la faisabilité, presque toujours sur **le rythme** — industriel, institutionnel, de renouvellement. **Une décision construite sur « est-ce que ça marchera » se trompe de question.** Celle qui compte est : *si cela marche, en combien de temps cela devient-il disponible pour moi, et à quel prix ?*

**Deuxième distinction — réversible ou non.** Une décision réversible peut être prise sur un signal faible ; une décision irréversible exige un échelon de preuve élevé. **Confondre les deux régimes est l'erreur la plus coûteuse**, dans les deux sens : attendre une certitude pour un pilote, engager une infrastructure sur une démonstration.

**Troisième distinction — acheter de l'option plutôt que parier.** Compétences, interfaces, contrats courts, architectures qui n'enferment pas, pilotes conçus pour produire une information et non une vitrine : ce sont des dépenses qui **augmentent la valeur d'une information future**. Elles sont rationnelles précisément quand on ne sait pas.

**Les trois questions à poser avant tout engagement :**

> **Qu'est-ce qui rendrait cette décision mauvaise ?**
> **Quel signal observable l'annoncerait, et où le lirais-je ?**
> **À quelle date la réexamine-t-on, indépendamment de tout événement ?**

**Si la première question n'a pas de réponse, la décision n'a pas été analysée** — elle a été justifiée. C'est le test du chapitre 4 appliqué à soi-même, et il est le même pour l'enthousiasme et pour le scepticisme.

---

### 46.8 Cinq affirmations datées et réfutables

Ce volume a exigé de chaque annonce qu'elle dise ce qui la contredirait. **Il se soumet ici à sa propre règle.**

Les cinq affirmations portent sur des **mécanismes**, jamais sur un produit ni sur un acteur. Elles sont formulées pour qu'un lecteur de 2029 puisse les juger sans avoir à interpréter l'intention de l'auteur. **La cinquième porte sur le domaine où l'auteur se sait le plus faible** — sans quoi l'exercice serait décoratif.

---

> ### Affirmation 1 — août 2026
>
> **Nous jugeons aujourd'hui que** le verrou dominant restera, dans la majorité des frontières de cet atlas, **non technique** : industriel, institutionnel, ou de compétences.
>
> **Elle sera affaiblie si** des domaines aujourd'hui bloqués par la certification, le raccordement ou la maintenance voient ces contraintes levées à un rythme comparable à celui de leurs progrès techniques.
>
> **Elle sera renforcée si** de nouvelles capacités techniques atteignent la maturité sans produire de déploiement, faute de cadre, d'installation ou de personnel.
>
> **Date de réexamen :** août 2029.

> ### Affirmation 2 — août 2026
>
> **Nous jugeons aujourd'hui que** l'expansion de la capacité de calcul sera bornée davantage par **le raccordement électrique et les délais d'infrastructure** que par la disponibilité des accélérateurs.
>
> **Elle sera affaiblie si** des délais de raccordement se réduisent significativement dans les zones de concentration, ou si des installations autonomes en énergie deviennent une pratique courante et non une exception.
>
> **Elle sera renforcée si** les gains d'efficacité énergétique par unité de calcul continuent d'être absorbés par l'augmentation de la demande, et si les files d'attente de raccordement s'allongent.
>
> **Date de réexamen :** août 2028.

> ### Affirmation 3 — août 2026
>
> **Nous jugeons aujourd'hui que** le **ratio d'opérateurs par machine** ne baissera pas d'un ordre de grandeur dans les déploiements robotiques en environnement non structuré, et que la fiabilité — non la capacité — restera le maillon en retard.
>
> **Elle sera affaiblie si** un exploitant publie des données d'exploitation montrant une supervision très largement réduite sur une flotte importante et durant une période longue.
>
> **Elle sera renforcée si** les déploiements continuent de progresser en nombre de machines sans que le ratio publié se déplace, ou si ce ratio continue de n'être pas publié.
>
> **Date de réexamen :** août 2029.

> ### Affirmation 4 — août 2026
>
> **Nous jugeons aujourd'hui que** les dispositifs de provenance des contenus **ne produiront pas de discrimination fiable** entre contenu authentique et contenu fabriqué, faute de couverture — l'absence d'attestation restant indiscernable de la fabrication.
>
> **Elle sera affaiblie si** l'attestation à la capture devient une propriété par défaut du parc d'appareils et si les chaînes de diffusion la préservent au lieu de la détruire.
>
> **Elle sera renforcée si** l'écart entre couverture des dispositifs et volume de contenus produits continue de croître, ou si les méthodes de détection automatique restent en course avec les générateurs sans les distancer.
>
> **Date de réexamen :** août 2029.

> ### Affirmation 5 — août 2026 · *domaine où l'auteur se sait faible*
>
> **Nous jugeons aujourd'hui que** la **correction d'erreur** restera le goulet dominant du calcul quantique, et qu'aucun avantage économique reproductible ne sera établi hors de niches étroites.
>
> **Déclaration de faiblesse.** L'auteur n'est pas en mesure d'évaluer indépendamment les annonces relatives aux qubits logiques : il dépend, sur ce point, de la lecture d'autrui. **Cette affirmation est donc la moins solide des cinq, et elle est incluse pour cette raison.**
>
> **Elle sera affaiblie si** une machine exécute un calcul utile à une entreprise, reproductible par un tiers, et dont le résultat n'est pas obtenable classiquement à coût comparable.
>
> **Elle sera renforcée si** les progrès continuent de porter sur le nombre de qubits physiques et la fidélité sans convertir en durée d'exploitation d'un qubit logique à l'échelle requise.
>
> **Date de réexamen :** août 2029.

---

**Ce que ces cinq affirmations engagent.** Elles peuvent être fausses ; c'est leur intérêt. **Ce qui compte est qu'elles nomment à l'avance ce qui les tuerait**, ce qu'aucune prédiction confortable ne fait.

🧪 **Lab 3 — Une veille en trente jours**

**Objectif.** Constituer un dispositif de veille qui produise des décisions, pas des lectures.
**Durée.** 3 heures réparties sur un mois. **Difficulté.** 2/3. **Prérequis.** Parties I, IV, V.
**Travail demandé.** (a) Choisir trois goulets pertinents pour votre organisation et les formuler comme rapports entre deux grandeurs. (b) Pour chacun, identifier deux sources d'exploitant et une source réglementée. (c) Pendant trente jours, classer tout ce qui vous parvient en *signal* / *actualité* / *non informatif*, en justifiant par le test des trois questions. (d) À la fin, énoncer une affirmation datée et réfutable par goulet.
**Éléments attendus.** La proportion de *non informatif* dépasse généralement les trois quarts ; découvrir ce ratio est le but du lab. Une veille qui ne produit aucun *non informatif* n'a pas appliqué le test.

---


## Chapitre 47 — Protocole final : une frontière absente de l'atlas

### 47.1 Règle du jeu

L'atlas comporte cent soixante-deux entrées. **Il en manque nécessairement.** L'utilité du volume ne se mesure donc pas à ce qu'il contient, mais à ce qu'il permet de faire devant ce qu'il ne contient pas.

**Le sujet retenu : le stockage thermique haute température.** Il est mentionné une fois dans l'atlas, à l'intérieur de l'entrée *stockage longue durée non électrochimique*, et n'y est pas traité. **Vous disposez donc d'un point d'ancrage et de rien d'autre** — situation exactement représentative de celle où vous serez.

Le protocole ci-dessous applique dans l'ordre : les niveaux, les quatre questions, l'échelle des preuves, le rapport qui décide, les signaux, la réfutation, la décision. **Il ne conclut pas que la technologie est bonne ou mauvaise.**

---

### 47.2 Étape 1 — Situer le terme avant de l'étudier

**Niveau d'abstraction : famille de solutions**, pas composant et pas récit. Le terme recouvre des approches qui partagent une fonction — accumuler de la chaleur à température élevée, la restituer plus tard — et diffèrent par le milieu, le contenant et le mode de restitution.

**Ce que le terme mélange, et c'est immédiat.** *Stockage thermique* et *stockage thermique haute température* ne posent pas la même question : le second vise des usages que le premier ne peut pas servir. **La température de restitution est la variable qui décide de l'usage**, pas la quantité stockée.

**Ce qu'il ne faut pas en faire.** Le comparer à une batterie. **Ce sont deux réponses à deux questions différentes** — l'une restitue de l'électricité, l'autre de la chaleur — et l'atlas signalait déjà que « le stockage » sans précision de durée et d'usage final n'est pas une affirmation exploitable.

---

### 47.3 Étape 2 — Les quatre questions

**① Qu'est-ce que c'est réellement ?** Accumuler de la chaleur dans un milieu peu coûteux et abondant — matériaux réfractaires, roche, sels, métaux, matériaux à changement de phase — porté à haute température par de l'électricité, puis restituer cette chaleur à un procédé. **Le principe est ancien et sans difficulté conceptuelle** ; la nouveauté est le contexte, pas le mécanisme.

**② Qu'est-ce que cela permet ?** Trois choses distinctes, qu'il faut séparer. **Décarboner de la chaleur industrielle** sans changer le procédé aval. **Découpler dans le temps** la consommation d'électricité et l'usage de chaleur, donc consommer quand l'électricité est peu chère ou excédentaire. Et **fournir un service au réseau**, en absorbant des surplus.

**③ Qu'est-ce qui l'empêche encore ?** Les sept familles, avec la consigne du chapitre 3 : désigner celle qui domine, pas les énumérer.

| Famille | État du verrou |
|---|---|
| Physique | faible — le stockage de chaleur sensible ne bute sur aucun mur ; les pertes croissent avec la durée et la température, ce qui borne l'usage saisonnier, pas l'usage journalier |
| Fiabilité | modéré — cyclage thermique, tenue des matériaux et des isolants dans la durée |
| Coût | modéré — le milieu est bon marché, le contenant et l'échangeur le sont moins |
| Industriel | modéré — pas de matériau rare ni de procédé exotique |
| Infrastructure et compétences | **fort** — puissance électrique raccordée, intégration dans un site existant, personnel |
| Demande | **fort** — la valeur dépend entièrement de l'écart de prix entre électricité et combustible substitué |
| Institutionnel | **fort** — tarification de l'électricité, prix du carbone, garanties de performance, financement |

**Le verrou dominant n'est pas thermique.** Il est économique et institutionnel — ce qui est, au mot près, le résultat que le volume produit sur les trois quarts de son atlas.

**④ Qu'est-ce qui changerait si le verrou sautait ?** Une chaleur industrielle décarbonée sans modification du procédé aval, donc adressant un gisement d'émissions que l'électrification directe traite mal. **Et le verrou suivant serait immédiatement le raccordement** : ces installations consomment de la puissance électrique, et le chapitre 23 a établi que le délai de raccordement est devenu la contrainte dominante de la couche *alimenter*. **La capacité déplacerait le goulet vers le réseau**, elle ne le supprimerait pas.

---

### 47.4 Étape 3 — Le rapport qui décide

Le résultat central de la Partie IV impose de chercher **deux grandeurs dont le rapport décide**, et non le composant le plus avancé.

> **L'écart entre le prix de l'électricité aux heures où l'on charge et le prix du combustible substitué, rapporté au nombre de cycles annuels.**

**Pourquoi ce rapport et pas un autre.** L'investissement est un capital fixe : il ne s'amortit que par le nombre de fois où il sert. Un écart de prix favorable mais rare ne rentabilise rien ; un écart faible mais quotidien peut suffire. **Aucune caractéristique du matériau n'entre dans ce rapport** — ce qui explique pourquoi les annonces portant sur la température atteinte ou la densité de stockage n'informent pas sur l'adoption.

**Second rapport, subordonné au premier** : la température restituée rapportée à la température requise par le procédé visé. **Il est binaire plus que continu** — au-dessous du seuil du procédé, la valeur ne diminue pas, elle disparaît.

---

### 47.5 Étape 4 — De quoi cela dépend, par couche

| Couche | Ce que la capacité en attend |
|---|---|
| **Alimenter** | électricité bon marché à certaines heures · **puissance raccordée** · réseaux pilotés et signaux de prix |
| **Fabriquer** | matériaux réfractaires et isolants · contenants et échangeurs · intégration à un site existant |
| **Percevoir** | mesure de température et d'état du milieu dans la durée |
| **Vérifier** | garanties de performance opposables, sans lesquelles le financement ne se fait pas |
| **Calculer** | marginal — pilotage et arbitrage horaire, sans difficulté propre |

**Ce tableau contient le diagnostic.** Les dépendances lourdes sont dans *alimenter* et *vérifier*, c'est-à-dire hors du dispositif lui-même. **Une technologie dont les dépendances critiques sont extérieures ne progresse pas au rythme de ses propres améliorations.**

---

### 47.6 Étape 5 — Situer sur l'échelle des preuves

**L'exercice consiste à répartir**, et non à donner une note globale.

**Déployé** pour le stockage de chaleur industriel classique, ancien et banal. **Pilote à premières installations commerciales** pour les dispositifs à haute température alimentés en électricité. **Démonstrateur ou prototype** pour les architectures les plus ambitieuses en température de restitution. **Aucun échelon atteint** pour la production en série et pour la démonstration de marge à l'échelle.

> ⏱ **État au 24/08/2026** — 🏭 pour l'usage thermique classique, 🔬 pour l'usage haute température piloté par l'électricité. Verrou actif : économique et institutionnel.
> 🔄 **À revoir si** un exploitant industriel publie des données d'exploitation pluriannuelles sur une installation en service, incluant le nombre de cycles réalisés.

**Remarquez ce que cette répartition évite.** Une note globale — « mature » ou « émergent » — aurait été fausse dans les deux sens. **La question « à quel échelon sommes-nous ? » n'a de réponse que par usage.**

---

### 47.7 Étape 6 — Signaux, non-signaux, réfutation

**Signaux informatifs.** Contrats de fourniture de chaleur de longue durée signés par des industriels — ils prouvent une demande solvable et une confiance dans la performance · nombre de cycles annuels réalisés par une installation en service · apparition de **garanties de performance assurées** · tarification horaire de l'électricité industrielle rendant l'écart de prix exploitable · files d'attente de raccordement dans les zones industrielles concernées.

**Signaux non informatifs.** Températures records annoncées · densité de stockage · capacité installée annoncée en projet · levées de fonds · démonstrateurs visités par des officiels · comparaisons avec le coût des batteries, qui portent sur un service différent.

**Réfutation — ce qui montrerait que cette lecture est fausse.** Des installations qui plafonnent au démonstrateur pendant plusieurs années sans contrat industriel de long terme · un coût du contenant et de l'échangeur qui ne baisse pas avec le nombre d'unités · une électrification directe des procédés qui progresse plus vite que prévu et rend le détour par le stockage inutile · et, dans l'autre sens, un déploiement rapide malgré des écarts de prix défavorables, ce qui invaliderait le rapport retenu à l'étape 3.

---

### 47.8 Étape 7 — La décision

**Situation type.** Un site industriel consommant de la chaleur doit décider s'il s'engage.

**La question n'est pas « la technologie fonctionne-t-elle ».** Elle fonctionne. La question est : *combien de cycles par an mon profil d'activité permet-il, quel écart de prix mon contrat d'électricité me donne réellement, et quelle puissance de raccordement puis-je obtenir, dans quel délai ?*

**Régime de la décision.** Une étude de raccordement et un pilote sont réversibles : ils s'engagent sur un signal faible et produisent l'information manquante. **Le remplacement d'un équipement de production est irréversible pour quinze à trente ans** et exige l'échelon *client payant* documenté chez un tiers comparable.

**Les trois questions du chapitre 46**, renseignées : la décision serait mauvaise si l'écart de prix se referme ou si le raccordement excède le calendrier industriel ; ces deux éléments sont observables et publiés ; le réexamen se fait à date fixe, indépendamment de toute annonce.

---

### 47.9 Le corrigé — ce que l'exercice devait montrer

**Un.** Le verrou dominant d'une technologie thermique n'est **pas thermique**. Un lecteur qui aurait passé son analyse sur les matériaux et les températures aurait produit un travail exact et inutile.

**Deux.** La grandeur qui décide est **un rapport**, et il ne figure dans aucune communication technique. Le volume l'avait annoncé ; l'exercice le vérifie sur un sujet non traité.

**Trois.** Les dépendances critiques sont **extérieures au dispositif** — réseau, tarification, garantie, financement. C'est le motif dominant de tout l'atlas, retrouvé sur une entrée qui n'en fait pas partie.

**Quatre, et c'est le test le plus sévère.** Appliquons la double condition d'admission de l'atlas. **Utilité** : oui — le terme circule dans les plans de décarbonation industrielle et le lecteur le rencontrera. **Irréductibilité** : non — tout ce qui précède se rattache à l'entrée *stockage longue durée non électrochimique*, dont il constitue une famille. **Le sujet mérite donc une section, pas une entrée** — et cette décision, prise en trois minutes par la règle, est exactement ce que le volume voulait vous rendre capable de faire.

> **Le volume a réussi si vous pouvez refaire ce protocole seul, sur un terme entendu pour la première fois, en moins d'une heure et sans conclure par un verdict.**

---


## Clôture de la Partie VI

**Deux chapitres, deux fonctions distinctes.** Le premier a donné la méthode d'entretien : suivre des goulets et non des sujets, distinguer signal et actualité, tenir la carte par balayage, décider en distinguant réversible et irréversible. Le second l'a mise à l'épreuve sur une frontière absente de l'atlas et a retrouvé, sans l'y chercher, le résultat central du volume.

**Ce que la partie ne fournit pas.** Aucune liste de sources à jour, aucun outil, aucun dispositif organisationnel. Ces éléments se périment plus vite que le reste du livre et relèvent des annexes, où ils sont isolés pour cette raison.

---


## Conclusion — ce que ce volume a produit

**Cent soixante-deux entrées, quarante-cinq termes, six convergences, quatre transformations, un protocole.** Le décompte ne dit rien de ce qui compte, et il faut donc dire ce qui compte.

### Ce qui a été construit

**Une carte, et non un catalogue.** La différence tient à une seule discipline, appliquée cent soixante-deux fois : chaque fiche consacre plus de place à ce qui bloque qu'à ce qui est promis. **Un catalogue accumule des objets ; une carte dit où l'on peut aller et par où l'on ne passe pas.**

**Un vocabulaire désencombré.** Deux cent cinquante termes du marché renvoient à l'entrée qui les traite, sans fiche propre. C'est la décision la plus impopulaire du volume et la plus utile : **un mot de plus n'est pas une distinction de plus.**

**Une séparation tenue entre la chose et le mot.** L'atlas décrit ce qui existe, la taxonomie décrit ce que l'on en dit. Le décompte de l'Annexe H le vérifie mécaniquement : **aucune entrée de l'atlas n'est un récit, et aucun récit n'a de fiche technique.**

### Les quatre résultats

**Un — le verrou est rarement là où le vocabulaire le place.** Vérifié dossier par dossier : sur six convergences, un seul maillon en retard est proprement technique. Les cinq autres sont industriels, opérationnels ou institutionnels. **Ce n'est pas un jugement sur la technique, c'est une observation sur l'endroit où elle bute.**

**Deux — un verrou n'est pas une grandeur, c'est un rapport entre deux grandeurs.** Coût d'acquisition contre coût d'exploitation ; capacité démontrée contre capacité démontrable ; délai de construction contre délai de raccordement. **Les annonces portent presque toujours sur le numérateur.**

**Trois — ce qui devient rare est presque toujours une capacité d'aval.** Quand produire devient abondant, ce qui borne est de vérifier, d'entretenir, de qualifier, de remplacer. Les quatre chapitres de la Partie V y arrivent par quatre chemins distincts.

**Quatre — l'effet vient du décalage des rythmes, jamais de la capacité seule.** L'usage se diffuse vite, l'exploitation suit, le cadre suit encore. **Et la fenêtre de décision précède le signal qui la justifierait** — ce qui est la raison d'être de la Partie VI.

### Ce que ce volume ne fait pas

**Il ne prédit pas.** Aucune date, aucun calendrier, aucun classement de gagnants. Les cinq affirmations du chapitre 46 sont l'exception assumée, et chacune énonce ce qui la tuerait.

**Il ne tranche pas les arbitrages de valeurs.** Vie privée et sécurité, automatisation et emploi, souveraineté et efficacité : les positions sont exposées avec leurs hypothèses, et la méthode s'arrête là où elle cesse d'avoir compétence. **Fabriquer une symétrie entre des preuves inégales aurait été une faute, trancher au nom de la technique en aurait été une autre.**

**Il ne remplace pas le volume 1.** Les mécanismes de diffusion, les courbes d'apprentissage, l'administration de la preuve y sont démontrés ; ils sont ici employés.

### Ce qu'il faut en garder

Trois instruments, et ils tiennent en une ligne : **neuf niveaux, quatre questions, deux échelles.** Tout le reste se consulte.

Et une habitude, qui est le véritable objet du livre :

> **Devant une technologie inconnue, ne pas demander si elle est prometteuse — demander ce qui doit devenir vrai pour qu'elle compte, et ce qu'on observerait si l'on se trompait.**

**Le volume aura réussi le jour où vous n'en aurez plus besoin pour le faire.**

---


## Ouverture des annexes

Les six parties du volume se lisent. **Les annexes se consultent.**

Elles ont une fonction précise, et une seule : **permettre d'entrer dans le volume par un mot** — celui qu'on vient d'entendre en réunion, de lire dans un appel d'offres, ou de croiser dans un article — sans savoir où il est traité.

**Trois règles gouvernent l'ensemble des annexes.**

**Le nom canonique fait foi.** Un renvoi cite toujours le nom exact de l'entrée tel qu'il figure à l'Annexe A, jamais une variante approchante. C'est la règle qui rend les renvois vérifiables mécaniquement, et elle a été tenue sur l'ensemble du manuscrit.

**Les synonymes ne sont pas des entrées.** Un terme du marché qui ne satisfait pas la condition d'irréductibilité n'a pas de fiche : il figure à l'Annexe B avec un renvoi. **C'est le dispositif qui empêche l'atlas de reproduire les synonymes du marché** — objectif énoncé dès l'ouverture du volume.

**Les annexes datées sont isolées.** Tout ce qui se périme — états de maturité, informations chiffrées — est regroupé dans des annexes dédiées, de manière qu'une réédition ne touche ni au corps du volume ni aux index.

---


## Annexe A — Index alphabétique des technologies

**162 entrées.** Le tri ignore les articles initiaux. La colonne ◆ donne la profondeur de traitement : ◆◆◆ majeure, ◆◆ standard, ◆ reconnaissance.

| Terme canonique | ◆ | Couche(s) | Ch. |
|---|:---:|---|---:|
| Accélérateurs de calcul spécialisés | ◆◆◆ | calculer | 8 |
| Acoustique sous-marine | ◆ | percevoir | 6 |
| Actionneurs robotiques | ◆◆◆ | agir | 15 |
| Affichages avancés | ◆◆ | interagir | 31 |
| Agents IA | ◆◆◆ | apprendre et décider, relier | 12 |
| Apprentissage par imitation | ◆◆ | apprendre et décider | 13 |
| Apprentissage par renforcement | ◆◆ | apprendre et décider | 13 |
| Architecture de sûreté d'un système autonome — *entrée comparative* | ◆◆◆ | vérifier | 30 |
| Architectures non von Neumann | ◆ | calculer | 9 |
| Attestation | ◆◆ | vérifier | 28 |
| Augmentation humaine | ◆◆ | interagir | 31 |
| Automatisation, agentivité, autonomie | ◆◆◆ | décider | 12 |
| Autonomie maritime, aérienne et ferroviaire civiles | ◆◆ | agir, décider | 17 |
| Autonomie supervisée | ◆◆ | décider | 16 |
| Les bandes infrarouges — *NIR, SWIR, MWIR, LWIR* | ◆◆◆ | percevoir | 5 |
| Batteries à flux | ◆◆ | alimenter | 21 |
| Batteries solides | ◆◆◆ | alimenter | 21 |
| Bio-impression | ◆ | fabriquer | 20 |
| Biocapteurs | ◆◆ | percevoir | 7 |
| Biologie synthétique | ◆◆◆ | fabriquer | 20 |
| Bioproduction | ◆◆◆ | fabriquer | 20 |
| Biosécurité | ◆◆ | vérifier | 20 |
| Calcul à faible précision | ◆◆ | calculer | 8 |
| Calcul analogique | ◆◆ | calculer | 9 |
| Calcul en mémoire | ◆◆◆ | calculer | 8 |
| Calcul en orbite | ◆◆ | infrastructure spatiale, calculer | 27 |
| Calcul photonique | ◆◆ | calculer | 9 |
| Calcul quantique | ◆◆◆ | calculer | 10 |
| Calcul supraconducteur | ◆ | calculer | 9 |
| Caméras événementielles | ◆◆ | percevoir | 6 |
| Capteurs chimiques | ◆ | percevoir | 7 |
| Capteurs inertiels | ◆◆ | percevoir | 6 |
| Capteurs quantiques | ◆◆◆ | percevoir | 7 |
| Carburants de synthèse | ◆◆ | alimenter | 22 |
| Charges utiles et miniaturisation | ◆◆ | infrastructure spatiale | 26 |
| Chiffrement homomorphe et calcul multipartite | ◆◆ | vérifier, calculer | 29 |
| Chiplets et assemblage avancé | ◆◆◆ | calculer | 8 |
| Communications en environnement dégradé | ◆◆ | relier | 24 |
| Communications optiques | ◆◆ | relier | 24 |
| Communications quantiques | ◆◆ | relier, vérifier | 10 |
| Composites avancés | ◆◆ | fabriquer | 19 |
| Conception de protéines | ◆◆◆ | apprendre et décider, fabriquer | 20 |
| Constellations en orbite basse | ◆◆◆ | infrastructure spatiale, relier | 26 |
| Continuum cloud-edge | ◆◆ | calculer, relier | 25 |
| Correction d'erreur quantique | ◆◆◆ | calculer | 10 |
| Crypto-agilité | ◆◆ | vérifier | 29 |
| Cryptographie post-quantique | ◆◆◆ | vérifier | 29 |
| Débris et congestion orbitale | ◆◆◆ | infrastructure spatiale | 27 |
| Découverte de médicaments assistée | ◆◆ | apprendre et décider, fabriquer | 20 |
| Dégradation maîtrisée | ◆◆ | vérifier | 30 |
| Détecteurs refroidis et non refroidis | ◆◆ | percevoir | 5 |
| Détection de sortie de domaine | ◆◆◆ | vérifier | 30 |
| Détection radiologique | ◆ | percevoir | 7 |
| Domaine de conception opérationnelle | ◆◆◆ | décider, vérifier | 17 |
| Données synthétiques | ◆◆ | apprendre et décider | 11 |
| Dossiers de sûreté | ◆◆ | vérifier | 30 |
| Drones aériens | ◆◆◆ | agir, percevoir, relier | 16 |
| Edge, on-device et embarqué | ◆◆◆ | calculer, relier | 25 |
| Édition génomique | ◆◆◆ | fabriquer | 20 |
| Électronique de puissance avancée | ◆◆ | alimenter | 23 |
| Embodied AI | ◆◆ | percevoir, apprendre, agir | 13 |
| Environnements d'exécution de confiance | ◆◆◆ | vérifier, calculer | 28 |
| Essaims et coordination distribuée | ◆◆◆ | agir, décider, relier | 16 |
| Fabrication additive | ◆◆◆ | fabriquer | 18 |
| Fabrication distribuée | ◆ | fabriquer | 18 |
| La fibre optique comme capteur | ◆◆ | percevoir | 7 |
| Fission avancée | ◆◆ | alimenter | 22 |
| FPGA | ◆ | calculer | 8 |
| Fusion | ◆◆◆ | alimenter | 22 |
| Géothermie avancée | ◆◆ | alimenter | 22 |
| GNSS et positionnement par satellite | ◆◆ | percevoir, relier | 6 |
| Haptique | ◆◆ | interagir | 31 |
| Hydrogène | ◆◆◆ | alimenter | 22 |
| Identité machine | ◆◆◆ | vérifier | 29 |
| Imagerie computationnelle | ◆◆ | percevoir, calculer | 5 |
| Imagerie hyperspectrale | ◆◆ | percevoir | 5 |
| Informatique portée | ◆◆ | interagir, percevoir | 31 |
| Informatique spatiale | ◆◆ | interagir, percevoir, calculer | 31 |
| Intensification d'image | ◆ | percevoir | 5 |
| Interfaces cerveau-machine | ◆◆◆ | interagir, percevoir | 31 |
| Interfaces neuromusculaires | ◆◆ | interagir | 31 |
| Interfaces vocales persistantes | ◆ | interagir | 31 |
| Jumeaux numériques industriels | ◆◆◆ | fabriquer, calculer, décider | 18 |
| Laboratoires autonomes | ◆◆◆ | fabriquer, percevoir, décider | 20 |
| Lanceurs réutilisables | ◆◆◆ | infrastructure spatiale | 26 |
| Lidar | ◆◆◆ | percevoir | 6 |
| Lithium-ion et ses chimies | ◆◆◆ | alimenter | 21 |
| Localisation et cartographie | ◆◆ | percevoir, décider | 17 |
| Locomotion | ◆◆ | agir | 14 |
| Lunettes connectées | ◆◆ | interagir | 31 |
| Mains et préhenseurs | ◆◆ | agir | 15 |
| Manipulation et préhension | ◆◆◆ | agir | 14 |
| Matériaux bidimensionnels | ◆◆ | fabriquer | 19 |
| Matériaux critiques et substitution | ◆◆◆ | fabriquer | 19 |
| Matériaux programmables et intelligents | ◆◆ | fabriquer | 19 |
| Mémoire et contexte long | ◆◆ | apprendre et décider | 11 |
| Mémoires à forte bande passante | ◆◆ | calculer | 8 |
| MEMS avancés | ◆ | percevoir, agir | 7 |
| Métamatériaux | ◆◆ | fabriquer | 19 |
| Métrologie avancée | ◆◆ | fabriquer, percevoir | 18 |
| Microgrids et centrales virtuelles | ◆◆ | alimenter, décider | 23 |
| Microrobotique | ◆ | agir | 14 |
| Modèles compacts | ◆◆ | apprendre et décider | 11 |
| Modèles de fondation | ◆◆◆ | apprendre et décider | 11 |
| Modèles de fondation robotiques | ◆◆ | apprendre et décider, agir | 13 |
| Modèles de raisonnement | ◆◆◆ | apprendre et décider | 11 |
| Modèles du monde | ◆◆◆ | apprendre et décider | 13 |
| Multimodalité | ◆◆ | percevoir, apprendre et décider | 11 |
| Nanomatériaux | ◆ | fabriquer | 19 |
| Navigation sans référence satellitaire | ◆◆◆ | percevoir | 6 |
| Neuromorphique | ◆◆◆ | calculer | 9 |
| Neuroprothèses | ◆◆ | interagir | 31 |
| Observation de la Terre | ◆◆◆ | infrastructure spatiale, percevoir | 26 |
| Opérations autonomes | ◆◆ | décider | 12 |
| Optronique — *electro-optics, EO/IR* | ◆◆◆ | percevoir | 5 |
| Organoïdes et organes sur puce | ◆◆ | fabriquer, percevoir | 20 |
| Peau électronique et perception tactile | ◆◆ | percevoir | 7 |
| Perception distribuée | ◆◆ | percevoir, relier | 7 |
| Petits réacteurs modulaires | ◆◆◆ | alimenter | 22 |
| Photonique intégrée | ◆◆◆ | calculer, relier | 9 |
| Photovoltaïque avancé | ◆◆ | alimenter | 22 |
| Positionnement, navigation et temps depuis l'espace | ◆◆ | infrastructure spatiale, percevoir | 27 |
| Preuves à divulgation nulle | ◆◆◆ | vérifier | 29 |
| Provenance et authenticité des contenus | ◆◆◆ | vérifier | 29 |
| Raccordement et files d'attente | ◆◆◆ | alimenter | 23 |
| Racine de confiance matérielle | ◆◆◆ | vérifier | 28 |
| Radar imageur | ◆◆ | percevoir | 6 |
| Réalité augmentée, mixte et virtuelle | ◆◆◆ | interagir | 31 |
| Récupération d'énergie | ◆ | alimenter | 23 |
| Reproductibilité et réplication | ◆◆ | fabriquer, vérifier | 20 |
| Réseaux déterministes | ◆◆ | relier | 24 |
| Réseaux électriques pilotés | ◆◆◆ | alimenter, décider, relier | 23 |
| Réseaux mobiles avancés | ◆◆◆ | relier | 24 |
| Réseaux non terrestres | ◆◆◆ | relier | 24 |
| Réseaux privés | ◆ | relier | 24 |
| Robot humanoïde — *monographie* | ◆◆◆ | agir | 15 |
| Robotique agricole | ◆ | agir | 14 |
| Robotique industrielle et cobots | ◆◆ | agir | 14 |
| Robotique médicale | ◆◆ | agir | 14 |
| Robotique souple | ◆◆ | agir | 14 |
| Robots mobiles autonomes | ◆◆ | agir, percevoir | 14 |
| SAR — ouverture synthétisée | ◆◆◆ | percevoir | 6 |
| Segment sol | ◆◆ | infrastructure spatiale, relier | 26 |
| Semi-conducteurs à grand gap | ◆◆◆ | fabriquer, alimenter | 19 |
| Service autonomy | ◆◆ | décider, vérifier | 12 |
| Services en orbite | ◆◆ | infrastructure spatiale | 27 |
| Sim-to-real | ◆◆◆ | apprendre et décider | 13 |
| Sodium-ion | ◆◆ | alimenter | 21 |
| Stockage longue durée non électrochimique | ◆◆ | alimenter | 21 |
| Suivi oculaire et gestuel | ◆◆ | interagir, percevoir | 31 |
| Supercondensateurs | ◆ | alimenter | 21 |
| Supraconductivité | ◆◆ | fabriquer, alimenter | 19 |
| Sûreté mémoire matérielle | ◆ | vérifier, calculer | 28 |
| Systèmes maritimes et sous-marins | ◆◆ | agir, relier | 16 |
| Systèmes multi-agents | ◆◆ | apprendre et décider, relier | 12 |
| Systèmes terrestres sans équipage | ◆ | agir | 16 |
| Téléopération | ◆◆ | agir, relier | 15 |
| Thérapies géniques et cellulaires | ◆◆ | fabriquer | 20 |
| Usines autonomes | ◆◆ | fabriquer, décider | 18 |
| Véhicules autonomes | ◆◆◆ | agir, percevoir, décider | 17 |
| Vérification formelle | ◆◆ | vérifier | 30 |
| VLA — Vision-Language-Action | ◆◆◆ | percevoir, apprendre et décider, agir | 13 |

---


## Annexe B — Index des synonymes, variantes et termes absorbés

**250 termes**, chacun renvoyant à l'entrée qui le traite. Ce sont les termes que le volume a délibérément **refusé de transformer en entrées** : ils désignent une variante, une technique interne, un acronyme commercial ou un sous-cas, et leur donner une fiche aurait encombré le vocabulaire au lieu de le désencombrer.

**Comment s'en servir.** Vous entendez un mot qui ne figure pas à l'Annexe A ; cherchez-le ici ; l'entrée indiquée le traite comme section. **Si le mot ne figure ni en A ni en B, appliquez le protocole du chapitre 47.**

| Terme rencontré | Entrée de l'atlas | Ch. |
|---|---|---:|
| 2.5D | Chiplets et assemblage avancé | 8 |
| 3D | Chiplets et assemblage avancé | 8 |
| 4D | Matériaux programmables et intelligents | 19 |
| actionneurs déformables | Robotique souple | 14 |
| ADAS | Véhicules autonomes | 17 |
| AGV | Robots mobiles autonomes | 14 |
| AIOps | Opérations autonomes | 12 |
| air comprimé | Stockage longue durée non électrochimique | 21 |
| algorithmes normalisés | Cryptographie post-quantique | 29 |
| alliages à mémoire | Matériaux programmables et intelligents | 19 |
| AMR | Robots mobiles autonomes | 14 |
| analyse d'atteignabilité | Vérification formelle | 30 |
| ancrage spatial | Réalité augmentée, mixte et virtuelle | 31 |
| anodes silicium | Lithium-ion et ses chimies | 21 |
| appariement de terrain | Navigation sans référence satellitaire | 6 |
| AR | Réalité augmentée, mixte et virtuelle | 31 |
| ASIC | Accélérateurs de calcul spécialisés | 8 |
| assurance case | Dossiers de sûreté | 30 |
| atomes neutres | Calcul quantique | 10 |
| auto-réparants | Matériaux programmables et intelligents | 19 |
| auto-réparation | Opérations autonomes | 12 |
| bagues | Informatique portée | 31 |
| base editing | Édition génomique | 20 |
| boules gyrostabilisées | Optronique | 5 |
| bras articulés | Robotique industrielle et cobots | 14 |
| calcul au moment de l'inférence | Modèles de raisonnement | 11 |
| calcul confidentiel | Environnements d'exécution de confiance | 28 |
| calcul événementiel | Neuromorphique | 9 |
| capteurs de force | Peau électronique et perception tactile | 7 |
| CAR-T | Thérapies géniques et cellulaires | 20 |
| cartes HD | Localisation et cartographie | 17 |
| cartographie partagée | Perception distribuée | 7 |
| chaîne d'édition | Provenance et authenticité des contenus | 29 |
| chaîne de confiance | Attestation | 28 |
| chaînes optroniques | Optronique | 5 |
| champ lumineux | Affichages avancés | 31 |
| châssis | Biologie synthétique | 20 |
| chenilles | Locomotion | 14 |
| chirurgie assistée | Robotique médicale | 14 |
| circuits génétiques | Biologie synthétique | 20 |
| clonage de comportement | Apprentissage par imitation | 13 |
| codes de surface | Correction d'erreur quantique | 10 |
| collage hybride | Chiplets et assemblage avancé | 8 |
| communication en immersion | Systèmes maritimes et sous-marins | 16 |
| comportement collectif | Essaims et coordination distribuée | 16 |
| conception de novo | Conception de protéines | 20 |
| confinement magnétique | Fusion | 22 |
| contrôle adaptatif | Usines autonomes | 18 |
| contrôle en force | Manipulation et préhension | 14 |
| conversion électron-photon | Photonique intégrée | 9 |
| coordination sans centre | Essaims et coordination distribuée | 16 |
| coût au kilo | Lanceurs réutilisables | 26 |
| coût de génération | Preuves à divulgation nulle | 29 |
| coût quadratique | Mémoire et contexte long | 11 |
| criblage | Découverte de médicaments assistée | 20 |
| CRISPR | Édition génomique | 20 |
| culture cellulaire | Bioproduction | 20 |
| cyclage | Lithium-ion et ses chimies | 21 |
| DAS | La fibre optique comme capteur | 7 |
| dataflow | Architectures non von Neumann | 9 |
| décohérence | Calcul quantique | 10 |
| démarrage vérifié | Racine de confiance matérielle | 28 |
| désignation | Optronique | 5 |
| dichalcogénures | Nanomatériaux | 19 |
| direct-to-device | Réseaux non terrestres | 24 |
| distillation | Modèles compacts | 11 |
| données de téléopération | Apprentissage par imitation | 13 |
| DTS | La fibre optique comme capteur | 7 |
| durée de vie | Constellations en orbite basse | 26 |
| écart au réel | Jumeaux numériques industriels | 18 |
| écart de simulation | Sim-to-real | 13 |
| écouteurs augmentés | Informatique portée | 31 |
| effets hors cible | Édition génomique | 20 |
| électrochimiques | Biocapteurs | 7 |
| électrolyse | Hydrogène | 22 |
| électrolytes | Batteries solides | 21 |
| électronique de puissance | Semi-conducteurs à grand gap | 19 |
| élément sécurisé | Racine de confiance matérielle | 28 |
| emballement | Lithium-ion et ses chimies | 21 |
| EMG | Interfaces neuromusculaires | 31 |
| émission thermique | Les bandes infrarouges | 5 |
| enclaves | Environnements d'exécution de confiance | 28 |
| entraînement quasi-direct | Actionneurs robotiques | 15 |
| enveloppe | Domaine de conception opérationnelle | 17 |
| environnements synthétiques | Sim-to-real | 13 |
| espace libre | Communications optiques | 24 |
| fail-operational | Dégradation maîtrisée | 30 |
| fail-safe | Dégradation maîtrisée | 30 |
| fenêtre de contexte | Mémoire et contexte long | 11 |
| fenêtres atmosphériques | Les bandes infrarouges | 5 |
| fermentation de précision | Bioproduction | 20 |
| filigrane | Provenance et authenticité des contenus | 29 |
| flash | Lidar | 6 |
| flexibilité | Réseaux électriques pilotés | 23 |
| FMCW | Lidar · Radar imageur | 6, 6 |
| formats réduits | Calcul à faible précision | 8 |
| GaN | Semi-conducteurs à grand gap | 19 |
| GPU | Accélérateurs de calcul spécialisés | 8 |
| graphène | Nanomatériaux | 19 |
| gravimétrie | Capteurs quantiques | 7 |
| gravitaire | Stockage longue durée non électrochimique | 21 |
| guides d'ondes | Affichages avancés | 31 |
| HBM | Mémoires à forte bande passante | 8 |
| horloges | Capteurs quantiques | 7 |
| hors distribution | Détection de sortie de domaine | 30 |
| hors vue | Drones aériens | 16 |
| HSM | Racine de confiance matérielle | 28 |
| HTR | Fission avancée | 22 |
| humain dans/sur la boucle | Autonomie supervisée | 16 |
| HVDC | Électronique de puissance avancée | 23 |
| hybride sol-espace | Réseaux non terrestres | 24 |
| hydrogène | Stockage longue durée non électrochimique | 21 |
| identifiants de contenu | Provenance et authenticité des contenus | 29 |
| identité d'agent | Identité machine | 29 |
| identité de charge | Identité machine | 29 |
| IMU | Capteurs inertiels | 6 |
| inertie synthétique | Réseaux électriques pilotés | 23 |
| InSAR | SAR — ouverture synthétisée | 6 |
| interférométrie atomique | Capteurs quantiques | 7 |
| interposeur | Chiplets et assemblage avancé | 8 |
| intersatellite | Communications optiques | 24 |
| intrication | Calcul quantique | 10 |
| invasives | Interfaces cerveau-machine | 31 |
| ions piégés | Calcul quantique | 10 |
| latence de descente | Calcul en orbite | 27 |
| LFP | Lithium-ion et ses chimies | 21 |
| licensing | Petits réacteurs modulaires | 22 |
| LLM | Modèles de fondation | 11 |
| LWIR | Les bandes infrarouges | 5 |
| magnétométrie | Capteurs quantiques | 7 |
| mains multi-doigts | Mains et préhenseurs | 15 |
| matériaux de détection | Détecteurs refroidis et non refroidis | 5 |
| matériaux sous flux | Fusion | 22 |
| matrices analogiques | Calcul en mémoire | 8 |
| mélange d'experts | Modèles compacts | 11 |
| MEMS gyroscopiques | Capteurs inertiels | 6 |
| micro-LED | Affichages avancés | 31 |
| microbolomètre | Détecteurs refroidis et non refroidis | 5 |
| mode replié | Communications en environnement dégradé | 24 |
| model checking | Vérification formelle | 30 |
| moisson différée | Cryptographie post-quantique | 29 |
| montres | Informatique portée | 31 |
| MR | Réalité augmentée, mixte et virtuelle | 31 |
| multi-constellation | GNSS et positionnement par satellite | 6 |
| multi-matériaux | Fabrication additive | 18 |
| multiplication matricielle optique | Calcul photonique | 9 |
| multispectral | Imagerie hyperspectrale | 5 |
| MWIR | Les bandes infrarouges | 5 |
| navigation en entrepôt | Robots mobiles autonomes | 14 |
| near-memory | Calcul en mémoire | 8 |
| neutrons rapides | Fission avancée | 22 |
| nez électronique | Capteurs chimiques | 7 |
| NIR | Les bandes infrarouges | 5 |
| niveaux SAE | Véhicules autonomes | 17 |
| NMC | Lithium-ion et ses chimies | 21 |
| non invasives | Interfaces cerveau-machine | 31 |
| NPU | Accélérateurs de calcul spécialisés | 8 |
| ODD | Domaine de conception opérationnelle | 17 |
| odométrie visuelle | Navigation sans référence satellitaire | 6 |
| optique co-packagée | Photonique intégrée | 9 |
| ouverture codée | Imagerie computationnelle | 5 |
| passthrough | Réalité augmentée, mixte et virtuelle | 31 |
| pattes | Locomotion | 14 |
| perception collective | Perception distribuée | 7 |
| pérovskites | Photovoltaïque avancé | 22 |
| photonique | Calcul quantique | 10 |
| pinces | Mains et préhenseurs | 15 |
| placement de charge | Continuum cloud-edge | 25 |
| poignet | Interfaces neuromusculaires | 31 |
| politiques d'action | VLA — Vision-Language-Action | 13 |
| pré-entraînement | Modèles de fondation | 11 |
| prédiction de structure | Conception de protéines | 20 |
| prime editing | Édition génomique | 20 |
| problème de précision | Calcul analogique | 9 |
| proprioception | Peau électronique et perception tactile | 7 |
| purification | Bioproduction | 20 |
| QKD | Communications quantiques | 10 |
| quadrupèdes | Locomotion | 14 |
| qubit | Calcul quantique | 10 |
| qubit physique/logique | Correction d'erreur quantique | 10 |
| radar automobile | Radar imageur | 6 |
| RAG | Mémoire et contexte long | 11 |
| randomisation de domaine | Sim-to-real | 13 |
| récompense | Apprentissage par renforcement | 13 |
| reconfigurable | Architectures non von Neumann | 9 |
| recuit quantique | Calcul quantique | 10 |
| régularités d'échelle | Modèles de fondation | 11 |
| répéteurs | Communications quantiques | 10 |
| repli minimal | Domaine de conception opérationnelle | 17 |
| représentation d'état | Modèles du monde | 13 |
| représentations partagées | Multimodalité | 11 |
| reprise en main | Autonomie supervisée | 16 |
| réseaux continus | Électronique de puissance avancée | 23 |
| réseaux impulsionnels | Neuromorphique | 9 |
| réseaux quantiques | Communications quantiques | 10 |
| réseaux systoliques | Accélérateurs de calcul spécialisés | 8 |
| résolution vs altitude | SAR — ouverture synthétisée | 6 |
| retour d'effort | Téléopération | 15 |
| retour de force | Haptique | 31 |
| robotaxi | Véhicules autonomes | 17 |
| robotique de laboratoire | Laboratoires autonomes | 20 |
| roues | Locomotion | 14 |
| RTK | GNSS et positionnement par satellite | 6 |
| safety case | Dossiers de sûreté | 30 |
| saisie | Manipulation et préhension | 14 |
| sans lentille | Imagerie computationnelle | 5 |
| saut de fréquence | Communications en environnement dégradé | 24 |
| sécurité collaborative | Robotique industrielle et cobots | 14 |
| self-driving labs | Laboratoires autonomes | 20 |
| sels fondus | Fission avancée | 22 |
| SiC | Semi-conducteurs à grand gap | 19 |
| silicon photonics | Photonique intégrée | 9 |
| SLAM | Localisation et cartographie | 17 |
| solid-state | Lidar | 6 |
| sonar actif/passif | Acoustique sous-marine | 6 |
| sortie de domaine | Domaine de conception opérationnelle | 17 |
| spins | Calcul quantique | 10 |
| super-résolution | Imagerie computationnelle | 5 |
| superposition | Calcul quantique | 10 |
| supraconducteurs | Calcul quantique | 10 |
| surfaces reconfigurables | Métamatériaux | 19 |
| SWIR | Les bandes infrarouges | 5 |
| synchronisation | Jumeaux numériques industriels | 18 |
| systèmes stimulés | Géothermie avancée | 22 |
| tandem | Photovoltaïque avancé | 22 |
| TEE | Environnements d'exécution de confiance | 28 |
| téléchirurgie | Robotique médicale | 14 |
| températures critiques | Supraconductivité | 19 |
| terres rares | Matériaux critiques et substitution | 19 |
| ToF | Lidar | 6 |
| tomographie | Métrologie avancée | 18 |
| TPM | Racine de confiance matérielle | 28 |
| TPU | Accélérateurs de calcul spécialisés | 8 |
| traitement à bord | Calcul en orbite | 27 |
| transformateurs | Raccordement et files d'attente | 23 |
| TSN | Réseaux déterministes | 24 |
| usage d'ordinateur | Agents IA | 12 |
| usage d'outils | Agents IA | 12 |
| USV | Systèmes maritimes et sous-marins | 16 |
| UUV | Systèmes maritimes et sous-marins | 16 |
| V2G | Microgrids et centrales virtuelles | 23 |
| validation clinique | Découverte de médicaments assistée | 20 |
| vecteurs | Thérapies géniques et cellulaires | 20 |
| ventouses | Mains et préhenseurs | 15 |
| vérifiabilité | Preuves à divulgation nulle | 29 |
| visible | Les bandes infrarouges | 5 |
| vision industrielle | Usines autonomes | 18 |
| vision nocturne classique | Intensification d'image | 5 |
| VR | Réalité augmentée, mixte et virtuelle | 31 |
| VTOL | Drones aériens | 16 |

---


## Annexe C — Index des grands courants, cadrages et buzzwords

**45 termes**, traités en Partie III. La colonne *Niveau* est l'information décisive : elle dit s'il s'agit d'une capacité, d'une catégorie industrielle, d'une doctrine ou d'un récit — et donc quel type de question le terme autorise.

**Rappel de la règle de lecture.** Un terme de cette annexe ne désigne jamais un objet comparable à une entrée de l'Annexe A. Mettre en concurrence un terme de C et une entrée de A produit une question sans réponse.

| Terme | Niveau | Couche(s) mobilisée(s) | Ch. |
|---|---|---|---:|
| Advanced Materials et Advanced Manufacturing | catégories industrielles | fabriquer | 35 |
| Agentic AI | cadrage, en cours de stabilisation vers une capacité | apprendre et décider, parfois relier | 32 |
| AGI | récit | sans objet | 32 |
| AI factories | catégorie industrielle, en formation | calculer, alimenter | 32 |
| AI for Science | cadrage transversal | apprendre et décider, fabriquer | 32 |
| AI-native | récit | variable | 32 |
| Autonomous enterprise | récit organisationnel | décider, vérifier | 34 |
| Autonomous mobility | catégorie industrielle | percevoir + décider + agir + relier | 33 |
| Autonomous networks | doctrine | relier, décider, vérifier | 34 |
| Autonomous systems | catégorie industrielle | percevoir + décider + agir + vérifier | 33 |
| BioTech et HealthTech | catégories industrielles | fabriquer, percevoir, apprendre | 35 |
| Climate Tech et Clean Tech | catégories économiques, par finalité | alimenter, fabriquer principalement | 35 |
| Cyber-physical systems | cadrage analytique, l'un des meilleurs de cette partie | toutes | 33 |
| Deep Tech | catégorie économique | toutes, sans discrimination | 35 |
| Defense Tech et Dual-use Tech | catégories industrielles et réglementaires | toutes | 35 |
| Digital twin — jumeau numérique | ambigu, et c'est le problème : capacité, plateforme ou doctrine selon l'emploi | calculer, percevoir, décider | 34 |
| Drone economy | récit à composante économique | percevoir + décider + agir + relier | 33 |
| Edge AI | doctrine | calculer, apprendre et décider, relier | 32 |
| Embodied AI | cadrage, plus étroit que le précédent | percevoir + apprendre et décider + agir | 33 |
| Frontier AI | récit, à usage réglementaire | apprendre et décider | 32 |
| Frontier Tech et Hard Tech | catégories économiques | sans objet | 35 |
| General-purpose robotics | capacité visée | percevoir + apprendre + agir + alimenter | 33 |
| Humanoid robotics | catégorie industrielle, autour d'une plateforme | agir principalement | 33 |
| IA générative | cadrage transversal | apprendre et décider | 32 |
| Industrial metaverse | récit | interagir, calculer, fabriquer | 34 |
| Industrie 4.0 et Industrie 5.0 | récit, à origine institutionnelle | fabriquer, calculer, relier | 34 |
| Intelligent robotics | cadrage vieillissant | percevoir + décider + agir | 33 |
| IoT et IIoT | catégorie industrielle | percevoir, relier, calculer | 34 |
| Machine autonomy | cadrage | décider, vérifier | 33 |
| Modèle de fondation | ambigu : plateforme dans l'atlas, récit dans l'usage courant | apprendre et décider | 32 |
| Modèles de raisonnement | capacité | apprendre et décider | 32 |
| Multimodalité | capacité | percevoir, apprendre et décider | 32 |
| NeuroTech | catégorie industrielle | percevoir, interagir, décider | 35 |
| Physical AI | récit, cadrage transversal | percevoir + apprendre et décider + agir | 33 |
| Quantum Tech | catégorie industrielle | calculer, percevoir, relier | 35 |
| Service autonomy | capacité organisationnelle | décider, vérifier, relier | 33 |
| Smart city | récit à composante politique | percevoir, relier, décider | 34 |
| Smart factory | doctrine | fabriquer, percevoir, décider | 34 |
| Smart grid | infrastructure | alimenter, percevoir, décider, relier | 34 |
| Software-defined everything | doctrine | calculer, relier | 34 |
| Sovereign AI | récit, à composante politique | calculer, alimenter, apprendre et décider | 32 |
| SpaceTech et New Space | catégories industrielles | infrastructure spatiale, relier, percevoir | 35 |
| Swarm intelligence | cadrage scientifique, employé comme doctrine | décider + relier + agir | 33 |
| Trust Technologies | catégorie émergente | vérifier | 35 |
| Ubiquitous computing et ambient computing | récit, ancien pour le premier | calculer, interagir, relier | 34 |

---


## Annexe D — Matrice technologies × couches

### D.1 Répartition par couche

| Couche | Chapitres | Entrées | ◆◆◆ | ◆◆ | ◆ |
|---|---|---:|---:|---:|---:|
| **A — percevoir** | 5-7 | 22 | 6 | 11 | 5 |
| **B — calculer** | 8-10 | 15 | 7 | 5 | 3 |
| **C — apprendre et décider** | 11-13 | 18 | 7 | 11 | 0 |
| **D — agir** | 14-17 | 21 | 7 | 11 | 3 |
| **E — fabriquer** | 18-20 | 24 | 9 | 12 | 3 |
| **F — alimenter** | 21-23 | 18 | 7 | 9 | 2 |
| **G — relier** | 24-25 | 8 | 3 | 4 | 1 |
| **G-bis — plan d'infrastructure spatiale** | 26-27 | 9 | 4 | 5 | 0 |
| **H — vérifier** | 28-30 | 15 | 8 | 6 | 1 |
| **I — interagir** | 31-31 | 12 | 2 | 9 | 1 |
| **Total** | **5-31** | **162** | **60** | **83** | **19** |

**Ce que la matrice montre, et qui ne se voit pas en lisant l'atlas.** *Percevoir* et *fabriquer* concentrent le plus d'entrées, parce que ce sont les couches les plus fragmentées en familles distinctes. *Interagir* en compte le moins et ne porte que deux majeures — la couche la plus homogène du volume, et celle dont le verrou est le plus uniforme.

### D.2 Les entrées transversales

**48 entrées sur 162 relèvent de plus d'une couche.** Ce sont les entrées les plus difficiles à classer et, en général, les plus structurantes : une technologie qui traverse deux couches est presque toujours un point de couplage, donc un endroit où un verrou se propage.

| Entrée | Couches | Ch. |
|---|---|---:|
| Drones aériens | agir, percevoir, relier | 16 |
| Embodied AI | percevoir, apprendre, agir | 13 |
| Essaims et coordination distribuée | agir, décider, relier | 16 |
| Informatique spatiale | interagir, percevoir, calculer | 31 |
| Jumeaux numériques industriels | fabriquer, calculer, décider | 18 |
| Laboratoires autonomes | fabriquer, percevoir, décider | 20 |
| Réseaux électriques pilotés | alimenter, décider, relier | 23 |
| Véhicules autonomes | agir, percevoir, décider | 17 |
| VLA — Vision-Language-Action | percevoir, apprendre et décider, agir | 13 |
| Agents IA | apprendre et décider, relier | 12 |
| Autonomie maritime, aérienne et ferroviaire civiles | agir, décider | 17 |
| Calcul en orbite | infrastructure spatiale, calculer | 27 |
| Chiffrement homomorphe et calcul multipartite | vérifier, calculer | 29 |
| Communications quantiques | relier, vérifier | 10 |
| Conception de protéines | apprendre et décider, fabriquer | 20 |
| Constellations en orbite basse | infrastructure spatiale, relier | 26 |
| Continuum cloud-edge | calculer, relier | 25 |
| Découverte de médicaments assistée | apprendre et décider, fabriquer | 20 |
| Domaine de conception opérationnelle | décider, vérifier | 17 |
| Edge, on-device et embarqué | calculer, relier | 25 |
| Environnements d'exécution de confiance | vérifier, calculer | 28 |
| GNSS et positionnement par satellite | percevoir, relier | 6 |
| Imagerie computationnelle | percevoir, calculer | 5 |
| Informatique portée | interagir, percevoir | 31 |
| Interfaces cerveau-machine | interagir, percevoir | 31 |
| Localisation et cartographie | percevoir, décider | 17 |
| MEMS avancés | percevoir, agir | 7 |
| Métrologie avancée | fabriquer, percevoir | 18 |
| Microgrids et centrales virtuelles | alimenter, décider | 23 |
| Modèles de fondation robotiques | apprendre et décider, agir | 13 |
| Multimodalité | percevoir, apprendre et décider | 11 |
| Observation de la Terre | infrastructure spatiale, percevoir | 26 |
| Organoïdes et organes sur puce | fabriquer, percevoir | 20 |
| Perception distribuée | percevoir, relier | 7 |
| Photonique intégrée | calculer, relier | 9 |
| Positionnement, navigation et temps depuis l'espace | infrastructure spatiale, percevoir | 27 |
| Reproductibilité et réplication | fabriquer, vérifier | 20 |
| Robots mobiles autonomes | agir, percevoir | 14 |
| Segment sol | infrastructure spatiale, relier | 26 |
| Semi-conducteurs à grand gap | fabriquer, alimenter | 19 |
| Service autonomy | décider, vérifier | 12 |
| Suivi oculaire et gestuel | interagir, percevoir | 31 |
| Supraconductivité | fabriquer, alimenter | 19 |
| Sûreté mémoire matérielle | vérifier, calculer | 28 |
| Systèmes maritimes et sous-marins | agir, relier | 16 |
| Systèmes multi-agents | apprendre et décider, relier | 12 |
| Téléopération | agir, relier | 15 |
| Usines autonomes | fabriquer, décider | 18 |

---
