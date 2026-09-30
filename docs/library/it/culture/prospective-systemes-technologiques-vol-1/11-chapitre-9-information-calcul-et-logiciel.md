---
title: Chapitre 9 — Information, calcul et logiciel
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
chapter: 11
chapters: 53
---

> **🎯 Pour lire ce chapitre**
>
> **À retenir :**
> * déplacer une donnée coûte des centaines de fois plus que la traiter, et cet écart se creuse ;
> * la sécurité cryptographique repose sur des hypothèses de difficulté, pas sur des impossibilités physiques.
>
> **À reconnaître :** mur de la mémoire · abstraction qui fuit · confidentialité / intégrité / authenticité · dette technique
>
> **Le reste se consulte.** Les mécanismes de détail, les chiffres et les variantes ne sont pas à mémoriser : ils sont là pour que vous puissiez y revenir.

Nous commençons la carte par le domaine où vous êtes le plus à l'aise. C'est délibéré, et pour deux raisons opposées.

La première est de vous donner un point d'ancrage : les notions de ce chapitre serviront d'analogie dans les dix suivants. La seconde est plus importante : c'est ici que vous verrez le plus vite **où vos modèles habituels cessent de fonctionner**, parce que vous connaissez assez bien le terrain pour repérer l'écart.

## 9.1 Pourquoi cette famille existe : représenter et transformer

Toute la famille répond à un seul problème : **comment représenter quelque chose du monde sous une forme qui permette de le transformer de façon fiable et reproductible ?**

Trois notions suffisent à structurer la réponse.

**L'information est ce qui réduit une incertitude.** Un message qui vous apprend ce que vous saviez déjà ne contient aucune information. Cette définition, contre-intuitive au premier abord, a une conséquence pratique immédiate : **plus un message est prévisible, moins il contient d'information — et plus il se comprime.**

**La redondance est de l'information répétée.** Elle est un coût, et elle est aussi la seule protection contre l'erreur. Un message sans aucune redondance ne peut pas être vérifié : toute altération produit un autre message parfaitement valide. C'est pourquoi tout système de transmission ou de stockage fiable ajoute délibérément de la redondance — et pourquoi il existe une tension permanente entre compression et robustesse.

**La compression exploite la structure.** Le chapitre 8 l'a établi : il existe un plancher, fixé par le contenu et non par l'ingéniosité de l'algorithme. Un fichier déjà comprimé ne se comprime plus, parce que sa structure a déjà été exploitée — il ressemble désormais à du bruit.

> **Résout / coûte.** Comprimer : *résout* le volume de stockage et de transmission · *coûte* de la redondance, donc de la résistance à l'erreur, et du calcul aux deux extrémités.

## 9.2 Représenter le monde : ce que le numérique perd

Le chapitre 8 a montré que toute mesure perd. Le numérique ajoute une seconde perte, cette fois délibérée : la **discrétisation**.

Une grandeur continue est ramenée à un nombre fini de valeurs, à intervalles réguliers. Ce choix n'est pas une concession technique regrettable : c'est ce qui rend le traitement fiable et reproductible. Une chaîne analogique dégrade le signal à chaque étape ; une chaîne numérique le recopie à l'identique, indéfiniment, tant que le bruit reste sous le seuil de décision. **Le numérique n'est pas plus fidèle que l'analogique : il est plus stable.** Il fige la dégradation au lieu de la laisser s'accumuler.

Ce point sera essentiel au chapitre 19, quand nous verrons pourquoi le calcul analogique, malgré son efficacité énergétique, se heurte à un problème de précision.

## 9.3 Calculer : quatre grandeurs et leurs tensions

Un calculateur fait trois choses : lire une donnée, la transformer, écrire un résultat. Toute l'architecture des machines découle de la tension entre ces trois opérations.

**La capacité de traitement** — combien d'opérations par seconde. C'est la grandeur la plus citée et la moins limitante aujourd'hui.

**Le parallélisme** — combien d'opérations simultanées. Il est borné par les **dépendances** : si le calcul B a besoin du résultat de A, aucune quantité de matériel ne les rendra simultanés. C'est pourquoi certains problèmes s'accélèrent presque indéfiniment en ajoutant des unités de calcul, et d'autres pas du tout. Cette borne n'est pas technique, elle est logique.

**La mémoire** — combien de données on peut garder à disposition, et à quelle distance.

**L'interconnexion** — à quelle vitesse les données circulent entre les unités.

**La tension centrale**, qui structure tout le reste : les trois premières se sont améliorées à des rythmes très différents, et c'est cet écart qui fait aujourd'hui le goulet.

## 9.4 Le mur de la mémoire

Voici le mécanisme le plus important de ce chapitre, et l'un des plus importants du volume.

**Le fait.** Déplacer une donnée coûte beaucoup plus d'énergie et de temps que la traiter. Dans la référence la plus citée sur le sujet — les mesures publiées par Mark Horowitz en 2014, réalisées sur une technologie de 45 nm — les ordres de grandeur sont les suivants :

| Opération | Énergie approximative |
|---|---|
| Addition sur un entier 8 bits | environ 0,03 pJ |
| Addition sur un flottant 32 bits | environ 0,9 pJ |
| Multiplication-accumulation flottante 32 bits | environ 4,6 pJ |
| Lecture dans une mémoire cache intégrée | environ 5 à 10 pJ |
| **Accès à une mémoire externe (DRAM)** | **environ 640 pJ** |

Un accès à la mémoire externe coûte donc de l'ordre de **plusieurs centaines de fois** une opération arithmétique. Ce n'est pas un détail d'optimisation : c'est la donnée qui gouverne la conception des machines modernes.

**Ce qui rend ce fait décisif, c'est son évolution.** Entre 45 nm et 7 nm, l'énergie des opérations logiques a été divisée par un facteur de l'ordre de trois — un flottant 32 bits passant d'environ 3,7 pJ à environ 1,3 pJ. Sur la même période, **l'énergie d'un accès à la mémoire externe classique n'a pratiquement pas bougé**, restant de l'ordre du millier de picojoules. Les mémoires les plus récentes à forte bande passante ramènent ce coût à quelques centaines de picojoules — une amélioration réelle, mais sans commune mesure avec celle du calcul. ⏱ *Valeurs indicatives ; le rapport est le point, pas les chiffres.*

**Formulation à retenir :**

> Le calcul est devenu beaucoup moins cher. Le déplacement des données, presque pas. Le rapport entre les deux s'est donc creusé d'un facteur considérable, et c'est ce rapport qui détermine où se situe le goulet.

**Quatre conséquences, que vous retrouverez ailleurs dans le volume.**

**Rapprocher le calcul de la donnée.** Toute l'architecture des machines vise à éviter les accès lointains : hiérarchies de caches, mémoires empilées au plus près, et à l'échelle d'un système, traitement au bord plutôt qu'au centre.

**L'efficacité dépend du motif d'accès.** Deux programmes effectuant le même nombre d'opérations peuvent avoir des consommations très différentes selon la façon dont ils parcourent la mémoire. C'est une des raisons pour lesquelles les gains annoncés en performance brute ne se traduisent pas mécaniquement en gains réels.

**Le calcul en mémoire devient une piste sérieuse.** Si déplacer coûte cher, on peut envisager de calculer là où la donnée réside. C'est l'objet d'une section du chapitre 19.

**Le goulet s'est déplacé.** Le chapitre 32 a montré la chaîne complète : capacité de calcul, puis accès mémoire, puis énergie, puis chaleur, puis raccordement. Vous en tenez ici le deuxième maillon, avec ses chiffres.

## 9.5 Le logiciel : abstraction et dette

**L'abstraction est le mécanisme fondamental du logiciel.** Elle permet de raisonner à un niveau sans connaître le niveau inférieur, et c'est ce qui rend possible la construction de systèmes qu'aucun individu ne comprend entièrement.

**Les abstractions fuient.** C'est la contrepartie, et elle est systématique : à un moment, une propriété du niveau inférieur remonte et devient visible. Le mur de la mémoire en est un exemple parfait — le programmeur qui manipule un tableau croit manipuler une abstraction uniforme, et découvre que l'ordre de parcours change les performances d'un facteur dix.

**La dette technique** est le coût différé d'un choix ancien. Elle a une propriété que le lecteur connaît bien et qu'il doit maintenant généraliser : **elle se paie longtemps après avoir été contractée, par des gens qui n'ont pas décidé**. Cette structure — un choix ancien qui contraint durablement — n'est pas propre au logiciel. C'est exactement la dépendance de sentier du chapitre 27, appliquée à l'intérieur d'un système.

**Une durée de vie sous-estimée.** Le logiciel paraît immatériel et donc facile à remplacer. En pratique, un logiciel d'entreprise dure souvent plus longtemps que le matériel qui l'exécute, parce qu'il incorpore des règles métier que personne n'a documentées ailleurs. C'est une **base installée** au sens du chapitre 27.

## 9.6 Les données

Trois points suffisent à ce niveau.

**La qualité domine la quantité.** Un volume de données important mais mal caractérisé produit des conclusions fausses avec une grande confiance. La question pertinente n'est jamais « combien ? » mais **« collectées comment, dans quelles conditions, et représentant quelle population ? »**.

**Les données ont un cycle de vie.** Elles se périment, changent de signification quand le processus qui les produit change, et perdent leur contexte quand ceux qui les ont collectées partent. Une série temporelle dont la définition a changé en cours de route est un piège classique.

**Elles portent des droits.** Propriété, licence, données personnelles, secret industriel. Ces contraintes ne sont pas juridiques au sens décoratif : elles déterminent ce qu'on a le droit de faire, donc ce qui est faisable. C'est une condition ⑧ appliquée à une ressource.

## 9.7 Cryptographie : sur quoi repose la confiance

Cette section est courte et son enjeu est important. Vous connaissez probablement l'usage des mécanismes cryptographiques ; l'objectif ici est que vous en connaissiez le **fondement**, car c'est de lui que dépendent plusieurs sujets majeurs du Volume 2.

**Trois propriétés distinctes, qu'il ne faut jamais confondre :**

| Propriété | Question à laquelle elle répond |
|---|---|
| **Confidentialité** | qui peut lire ce contenu ? |
| **Intégrité** | ce contenu a-t-il été modifié ? |
| **Authenticité** | qui en est réellement l'origine ? |

Un système peut assurer l'une sans les autres. Un message chiffré peut être altéré ; un message signé peut être parfaitement lisible.

**Le point fondamental.** La sécurité de ces mécanismes ne repose pas sur une impossibilité physique, comme la vitesse de la lumière ou la conservation de l'énergie. Elle repose sur des **hypothèses de difficulté calculatoire** : on suppose que certains problèmes mathématiques demanderaient un temps de calcul déraisonnable. Ces hypothèses sont solidement éprouvées, et elles restent des hypothèses.

**Trois conséquences en découlent, et elles sont contre-intuitives pour qui n'a vu que l'usage :**

**Une hypothèse peut tomber.** Un progrès mathématique ou une nouvelle forme de calcul peut rendre praticable ce qu'on supposait hors d'atteinte. Ce n'est pas une hypothèse théorique : c'est la raison d'être des travaux sur la cryptographie post-quantique, que le Volume 2 traitera.

**La migration cryptographique est un problème d'infrastructure, pas de logiciel.** Changer un algorithme suppose de le changer partout, simultanément, dans des équipements dont certains ont une durée de vie de plusieurs décennies et ne seront jamais mis à jour. C'est un problème de base installée au sens du chapitre 27, et de renouvellement de parc au sens du chapitre 30.

**Une donnée capturée aujourd'hui peut être déchiffrée plus tard.** Cette asymétrie temporelle signifie que la date de bascule pertinente n'est pas celle où l'hypothèse tombe, mais celle où l'information cesse d'avoir de la valeur.

**Une signature n'atteste pas la vérité.** Elle atteste l'origine et l'intégrité. Un capteur compromis qui signe correctement une mesure fausse produit une donnée authentique et fausse. Nous y reviendrons au chapitre 14 : c'est une distinction que le vocabulaire courant efface, et qui deviendra centrale pour les systèmes autonomes.

## 9.8 Ce que cela implique

**Les grandeurs à retenir.** Le rapport de plusieurs centaines entre le coût d'un accès mémoire externe et celui d'une opération arithmétique. La hiérarchie des latences, du registre au stockage, qui couvre plusieurs ordres de grandeur. Et le fait que ces deux échelles n'ont pas progressé au même rythme.

**Le passage à l'échelle.** D'une machine à un centre de calcul, ce sont les mêmes contraintes qui reviennent d'un cran plus haut : l'interconnexion devient le réseau, la hiérarchie mémoire devient la distribution des données entre machines, et la dissipation devient un problème de bâtiment. Le chapitre 13 reprendra là où celui-ci s'arrête.

**Implication cyber.** Trois éléments, tous prolongés ailleurs dans le volume : la **confiance transitive** — vous dépendez de composants logiciels dont vous n'avez jamais audité les auteurs, ce qui est la version logicielle des chaînes du chapitre 25 ; l'**intégrité à travers les couches** — une donnée traverse de nombreuses abstractions et chacune est un endroit où elle peut être altérée sans que cela se voie ; et la **dépendance aux hypothèses cryptographiques**, dont la section précédente a montré qu'elles sont datées.

**Où vos modèles se transfèrent, et où ils cassent.** C'est la promesse du chapitre 1, et voici son premier acquittement.

| Modèle | Se transfère à | Cesse de fonctionner quand |
|---|---|---|
| Dépendance et transitivité | chaînes d'approvisionnement, réseaux électriques, écosystèmes industriels | le délai de substitution passe de jours à années (ch. 25) |
| Abstraction en couches | tous les systèmes complexes | il n'existe pas de couche inférieure remplaçable : la physique ne s'abstrait pas |
| Latence et bande passante | capteurs, contrôle, énergie, spatial | la latence est bornée par la distance et non par l'équipement (ch. 8) |
| Scaling | production industrielle, énergie, déploiement | le coût marginal cesse d'être quasi nul (ch. 22, 31) |
| Dette technique | infrastructures, normes, parc installé | la dette est incarnée dans des objets physiques qu'il faut remplacer un par un (ch. 30) |
| « On corrigera en production » | nulle part | dès que l'objet est physique (ch. 24) |

🎓 **À ce stade, vous savez…** définir l'information par la réduction d'incertitude et en déduire la tension entre compression et redondance ; expliquer pourquoi le numérique est plus stable et non plus fidèle ; citer le rapport entre coût d'un accès mémoire et coût d'une opération, et son évolution divergente ; reconnaître une abstraction qui fuit ; distinguer confidentialité, intégrité et authenticité, et savoir sur quoi repose leur sécurité ; identifier six modèles issus de votre domaine et la frontière de chacun.

---
