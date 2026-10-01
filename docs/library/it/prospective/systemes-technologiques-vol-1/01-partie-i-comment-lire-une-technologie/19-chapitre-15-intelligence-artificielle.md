---
title: Chapitre 15 — Intelligence artificielle
source: IT/09 Technologies & prospective/Systèmes technologiques (vol. 1).md
note: Systèmes technologiques (vol. 1)
up:
- - Systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

> **🎯 Pour lire ce chapitre**
>
> **À retenir :**
> * l'apprentissage échange de la certitude contre de la capacité : on ne peut plus démontrer, seulement mesurer ;
> * hors de sa distribution d'entraînement, un modèle produit une sortie plausible sans que rien n'alerte.
>
> **À reconnaître :** représentation vectorielle · entraînement vs inférence · hors distribution · domaine d'emploi
>
> **Le reste se consulte.** Les mécanismes de détail, les chiffres et les variantes ne sont pas à mémoriser : ils sont là pour que vous puissiez y revenir.

Ce chapitre est le plus délicat de la carte, pour trois raisons qu'il vaut mieux annoncer.

C'est le domaine dont vous entendez le plus parler, donc celui où l'écart entre familiarité et compréhension est le plus grand. C'est celui où l'actualité change le plus vite, donc celui qui vieillirait le plus mal si nous l'écrivions autour de l'état de l'art. Et c'est celui où la tentation de développer est la plus forte.

Le chapitre est donc volontairement resserré sur les mécanismes, et il ne nomme aucun modèle ni aucun acteur. Il doit rester valide quand les produits d'aujourd'hui auront disparu.

## 15.1 Pourquoi cette famille existe : quand on ne sait pas spécifier

Le logiciel classique repose sur une hypothèse : quelqu'un sait décrire ce qu'il faut faire, sous forme de règles. Cette hypothèse tient pour une comptabilité, un protocole réseau, un système de réservation.

Elle échoue pour une catégorie entière de tâches : reconnaître un objet dans une image, transcrire de la parole, traduire, détecter une anomalie dans un signal complexe. Non pas parce que ces tâches seraient plus difficiles, mais parce que **personne ne sait écrire les règles**. Un humain reconnaît un visage sans pouvoir énoncer le critère qu'il applique.

**Le déplacement conceptuel est là.** Au lieu d'écrire les règles, on fournit des exemples de couples entrée-sortie et on laisse un procédé d'ajustement automatique trouver une fonction qui les reproduit — en espérant qu'elle se comporte correctement sur des entrées nouvelles.

**Ce que ce déplacement gagne et ce qu'il perd**, et tout le chapitre découle de cette ligne :

> **Résout / coûte.** L'apprentissage à partir d'exemples : *résout* des tâches qu'on ne sait pas spécifier · *coûte* la garantie — on ne peut plus démontrer ce que le système fera, seulement mesurer ce qu'il a fait sur un échantillon.

C'est un échange de **certitude contre capacité**. Il est souvent avantageux. Il n'est jamais gratuit, et il explique presque toutes les difficultés qui suivent.

## 15.2 Représenter : transformer des choses en nombres

Un système d'apprentissage ne manipule que des nombres. Tout ce qu'on lui donne doit donc être converti.

**Le découpage.** Un texte est découpé en unités élémentaires — des fragments de mots plutôt que des mots entiers, ce qui permet de traiter des termes jamais rencontrés. Une image est découpée en régions, un son en tranches temporelles.

**La représentation vectorielle.** Chaque unité est associée à une liste de nombres, apprise de façon à ce que **des éléments employés dans des contextes similaires reçoivent des représentations proches**. On obtient un espace où la proximité numérique traduit une forme de similarité d'usage.

**Ce que cela permet.** Comparer, regrouper, retrouver par similarité, et surtout combiner des modalités différentes dans un même espace — c'est ce qui rend possible qu'un même système traite du texte et des images.

**Ce que cela ne dit pas.** La proximité dans cet espace reflète la **régularité statistique des données d'entraînement**, pas une vérité sur le monde. Deux termes systématiquement employés ensemble seront proches, qu'ils désignent des choses effectivement liées ou qu'ils partagent un biais du corpus. C'est le premier endroit où une propriété du jeu de données se transforme en propriété du système.

## 15.3 Le mécanisme : couches, attention, échelle

**Une couche transforme.** Un réseau de neurones est une succession de transformations numériques : chacune combine ses entrées avec des coefficients ajustables, applique une opération non linéaire, et transmet. La profondeur permet de composer des transformations simples en transformations complexes.

**L'ajustement se fait par correction d'erreur.** On présente un exemple, on compare la sortie à la réponse attendue, on mesure l'écart, et on modifie légèrement tous les coefficients dans le sens qui réduit cet écart. Répété sur un très grand nombre d'exemples, ce procédé fait converger le système vers un comportement qui reproduit les données. **Il n'y a ni compréhension ni raisonnement dans ce mécanisme : il y a une descente progressive vers une configuration qui produit les bonnes sorties.**

**L'attention.** Le mécanisme qui a débloqué le traitement des séquences consiste à laisser le système déterminer lui-même, pour chaque élément traité, quels autres éléments de la séquence sont pertinents — plutôt que de fixer à l'avance une fenêtre de contexte. C'est ce qui permet de relier des éléments distants dans un texte long.

**Ce que ce mécanisme coûte, et c'est une contrainte majeure :** relier chaque élément à tous les autres implique un nombre de comparaisons qui croît avec le carré de la longueur de la séquence. Doubler la longueur du contexte quadruple ce coût. C'est une contrainte structurelle, et elle explique pourquoi l'extension du contexte est un sujet d'ingénierie difficile plutôt qu'un simple réglage.

**L'échelle.** Une observation empirique robuste a structuré le domaine : la performance s'améliore de façon régulière quand on augmente conjointement la taille du modèle, le volume de données et la quantité de calcul. Cette régularité a un statut précis, au sens du chapitre 7 : c'est une **régularité empirique**, pas une loi. Elle décrit ce qui a été observé sur une plage donnée. Elle ne garantit ni sa poursuite, ni l'apparition de telle capacité à tel niveau, et elle porte sur des mesures agrégées qui masquent des comportements très variables tâche par tâche.

## 15.4 Entraînement et inférence : deux économies distinctes

Distinction essentielle et souvent absente des discussions.

| | Entraînement | Inférence |
|---|---|---|
| Quand | une fois, puis mises à jour | à chaque usage |
| Coût | très élevé, concentré | modeste par appel |
| Nature | investissement | coût d'exploitation |
| Contrainte dominante | calcul et données disponibles | latence, mémoire, énergie par requête |
| Économie | dominée par le capital (ch. 22) | dominée par le coût marginal |

**Ce que cette distinction permet de comprendre.**

**Le coût cumulé d'exploitation peut dépasser le coût d'entraînement.** Un système très utilisé paie son inférence à chaque appel. L'arbitrage entre un modèle plus gros entraîné une fois et un modèle plus petit appelé des milliards de fois est donc économique, pas seulement technique.

**Le mur de la mémoire gouverne l'inférence.** Le chapitre 9 l'a chiffré : déplacer une donnée coûte plusieurs centaines de fois une opération arithmétique. Or l'inférence consiste largement à faire circuler des coefficients depuis la mémoire vers les unités de calcul. **Pour beaucoup de configurations, ce n'est pas la puissance de calcul qui limite, mais la bande passante mémoire.** C'est pourquoi les gains annoncés en opérations par seconde ne se traduisent pas mécaniquement en gains d'usage — le goulet est ailleurs.

**Cela explique le mouvement vers l'exécution locale.** Faire tourner un modèle sur l'appareil de l'utilisateur supprime la latence réseau, le coût par appel et la dépendance à une infrastructure distante — au prix d'une contrainte de mémoire et d'énergie qui borne la taille du modèle. C'est un arbitrage, pas un progrès unilatéral.

## 15.5 De quoi dépend la performance

Trois ressources, et une quatrième que l'on oublie.

**Les données** — leur volume, mais surtout leur qualité et leur représentativité. Le chapitre 9 l'a établi : la question n'est jamais « combien ? » mais « collectées comment, représentant quelle population ? ». Un système est bon là où ses données sont denses.

**Le calcul** — dont la disponibilité est aujourd'hui contrainte par les chapitres 10, 12 et 13, ce qui fait de cette famille une consommatrice majeure d'infrastructure physique.

**Les coefficients ajustables** — dont le nombre borne ce que le système peut représenter.

**Et l'objectif d'optimisation** — souvent oublié, et pourtant décisif. Un système apprend exactement ce qu'on lui a demandé d'optimiser, ce qui n'est jamais exactement ce qu'on voulait. C'est la loi de Goodhart du chapitre 6, appliquée à l'intérieur du système : **la mesure devient l'objectif, donc cesse d'être une bonne mesure.**

## 15.6 Ce qu'un système appris ne fait pas

Section importante, et à formuler avec précision — ni concession ni exagération.

**Il n'a pas de mémoire persistante par construction.** Ce qu'il a appris est figé dans ses coefficients au moment de l'entraînement. Ce qu'on lui fournit au moment de l'usage n'est pas mémorisé au-delà de l'échange. Des dispositifs externes permettent de conserver et de réinjecter de l'information ; ce sont des architectures, pas une propriété du modèle.

**Il ne se met pas à jour tout seul.** Intégrer une information nouvelle suppose un nouvel entraînement, ou un mécanisme externe de recherche et d'injection. Cela a une conséquence pratique : **un système appris a une date**, et son comportement reflète l'état du monde de ses données.

**Il ne fournit pas de garantie.** On peut mesurer sa performance sur un échantillon ; on ne peut pas démontrer son comportement sur une entrée non testée. C'est le coût annoncé en 15.1, et c'est ce qui rend la certification difficile — chapitre 28.

**Il capture des régularités, ce qui ne coïncide pas avec la causalité.** Deux phénomènes systématiquement associés dans les données seront associés dans le système, que l'un cause l'autre ou non. Cela n'invalide pas les prédictions — une régularité stable prédit correctement tant qu'elle est stable — mais cela invalide les conclusions sur ce qui se passerait **si l'on intervenait**. La distinction entre prédire et agir est ici structurelle.

**Ce que cette section ne dit pas.** Elle ne dit pas que ces systèmes seraient superficiels ou inutiles ; le chapitre 6 a mis en garde contre le scepticisme automatique aussi fermement que contre l'enthousiasme. Elle dit que **ces propriétés déterminent où l'on peut déployer ces systèmes sans surveillance**, ce qui est une question d'ingénierie, pas de jugement.

## 15.7 Évaluer, et l'échec silencieux

**Le chapitre 6 a établi la méthode**, et elle s'applique intégralement ici : un score est une performance sur une distribution, et sans ensemble de contrôle, on ne sait pas ce qu'il mesure. Le cas d'un benchmark d'arithmétique reconstruit à l'identique y a montré que des écarts significatifs apparaissent quand on teste sur des problèmes équivalents mais inédits — sans que cela signifie pour autant que les systèmes concernés ne raisonnaient pas.

**Ce qu'il faut ajouter ici : le comportement hors distribution.**

Un système est bon là où ses données sont denses. Confronté à une entrée éloignée de ce qu'il a vu, il ne produit pas un message d'erreur : **il produit une sortie, avec la même assurance apparente.** Rien dans sa forme n'indique qu'elle est le résultat d'une extrapolation.

**C'est exactement la panne silencieuse du chapitre 14**, transposée du capteur au modèle. Le rapprochement mérite d'être fait explicitement, parce qu'il est l'un des acquis les plus utiles de cette partie :

| | Capteur dérivé (14.8) | Modèle hors distribution (15.7) |
|---|---|---|
| Ce qui se passe | la relation grandeur-signal s'est déformée | l'entrée est loin des données d'entraînement |
| Ce que le système produit | une valeur plausible | une sortie plausible |
| Ce qui alerte | rien | rien |
| Parade principale | redondance dissemblable, vraisemblance, étalonnage | détection de nouveauté, vérification externe, limitation du domaine d'emploi |

**La formulation à retenir :**

> Un système de mesure et un système appris partagent le même mode de défaillance le plus dangereux : continuer à produire quelque chose de crédible quand ils ne fonctionnent plus.

**Trois conséquences pratiques.** Il faut définir un **domaine d'emploi** — les conditions dans lesquelles la performance a été établie — au sens du chapitre 21. Il faut détecter les entrées qui en sortent, ce qui est un problème en soi. Et il faut prévoir ce que le système fait quand il en sort, ce qui est l'objet du chapitre suivant.

## 15.8 Ce que cela implique

**Les grandeurs qui comptent.** L'écart de plusieurs ordres de grandeur entre le coût d'un entraînement et celui d'une inférence unitaire. Le rapport entre bande passante mémoire et puissance de calcul, qui détermine où se situe le goulet. Le coût quadratique de l'attention en fonction de la longueur de contexte. Et la consommation énergétique cumulée, qui relève du chapitre 12 et se paie à chaque appel.

**Le passage à l'échelle.** Cette famille est celle qui a le plus rapidement transformé une contrainte logicielle en contrainte d'infrastructure physique : la limite n'est plus l'algorithme mais l'électricité, le raccordement et le refroidissement. Le chapitre 32 en a fait la chaîne complète.

**Dépendances.** Elle dépend des semi-conducteurs, de l'énergie, des réseaux, des données et de la disponibilité de compétences rares. De plus en plus de systèmes dépendent d'elle, ce qui déplace la question de la fiabilité vers les chapitres 21 et 28.

**Implication cyber.** Trois points : la **qualité et l'intégrité des données d'entraînement**, qui deviennent une surface d'attaque nouvelle — altérer des données en amont modifie durablement un système en aval ; la **dépendance à des modèles tiers** qu'on n'a ni entraînés ni audités, qui est la confiance transitive du chapitre 9 appliquée à un objet opaque ; et l'**intégrité des sorties**, quand une décision automatisée agit sur un système réel.

⏱ **Note de maintenance.** Ce chapitre est écrit pour rester valide sans mise à jour de son corps. Toute donnée chiffrée sur l'état de l'art appartient à l'Annexe I et non au texte.

🎓 **À ce stade, vous savez…** dire pourquoi cette famille existe et quel échange elle opère ; expliquer ce qu'est une représentation vectorielle et ce qu'elle ne dit pas ; décrire l'ajustement par correction d'erreur et le mécanisme d'attention avec son coût quadratique ; distinguer entraînement et inférence comme deux économies ; identifier le goulet mémoire de l'inférence ; énoncer précisément ce qu'un système appris ne fait pas ; reconnaître l'échec silencieux et le rapprocher de la panne de capteur.

---
