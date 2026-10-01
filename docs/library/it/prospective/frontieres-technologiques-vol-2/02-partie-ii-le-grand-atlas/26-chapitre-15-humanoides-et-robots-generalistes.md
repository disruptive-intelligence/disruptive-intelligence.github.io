---
title: Chapitre 15 — Humanoïdes et robots généralistes
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie II — Le grand atlas
  - index.md
---

> **Ce que ce chapitre ajoute — et ce qu'il ne fait pas.** Ce chapitre traite **la plateforme humanoïde comme objet** : comment elle est faite, ce qu'elle coûte, ce qui s'use, ce qui la borne.
>
> **Il ne traite pas de la capacité de généralité robotique**, qui fait l'objet du dossier de convergence 36 — lequel considère toutes les morphologies, y compris non humanoïdes. La question « quelle forme gagnera » n'appartient pas à ce chapitre.
>
> **Format exceptionnel.** L'entrée principale est une monographie plus longue que le format standard, parce que l'objet est le plus médiatisé de l'atlas et le plus mal évalué. Trois entrées de composants la complètent.

---

## ◆◆◆ Robot humanoïde — *monographie*

**Niveau** — plateforme · **Couche** — agir

**En une phrase.** Une machine à morphologie humaine — bipède, à deux bras, à hauteur d'homme — conçue pour opérer dans des environnements aménagés pour l'humain.

**Pourquoi on en parle.** Parce que c'est l'objet technologique le plus visible de la période, celui qui concentre le plus d'investissement et de démonstrations — et celui où l'écart entre ce qui est montré et ce qui est exploitable est le plus grand.

### Pourquoi une morphologie humaine

L'argument est précis et mérite d'être compris avant d'être discuté : **le monde bâti est conçu pour des humains**. Escaliers, poignées, interrupteurs, hauteurs de plan de travail, largeurs de passage, outils à main. Une machine de forme humaine peut, en principe, opérer dans cet environnement sans le modifier — ce qui supprime le coût d'aménagement qui domine l'économie de la robotique industrielle.

**Le contre-argument est tout aussi précis.** La forme humaine résulte d'une évolution biologique sous des contraintes qui ne sont pas celles d'une machine. Elle est instable par construction, énergétiquement coûteuse, et impose de porter une masse en hauteur. Une machine libre de sa forme choisirait rarement celle-là.

**Le vrai critère est donc économique** : la fraction des tâches visées qui exige réellement la forme humaine, comparée au coût qu'elle impose. Cette fraction n'est pas nulle et n'est pas la majorité — c'est ce que le dossier 36 instruira.

### Ce qui compose la machine

**Les actionneurs** dominent le coût, la masse et la performance. Un humanoïde en compte plusieurs dizaines, chacun devant produire un couple élevé dans un volume réduit, avec une réponse rapide et une capacité à absorber les chocs. Ils font l'objet d'une entrée dédiée.

**Les mains** concentrent la difficulté : c'est là que se joue la généralité, et c'est le sous-système le moins mature.

**L'énergie embarquée** est soumise à la boucle de la couche : ajouter de la batterie ajoute de la masse, qu'il faut déplacer, ce qui consomme davantage. L'autonomie utile des plateformes actuelles se compte en heures, et le gain d'autonomie est moins que proportionnel à l'énergie ajoutée.

**Le calcul embarqué** doit exécuter la perception et la commande dans une enveloppe thermique et énergétique contrainte — ce qui renvoie aux modèles compacts du chapitre 11.

**La structure** doit être légère et rigide, et supporter des cycles de sollicitation qui produisent du jeu et de l'usure.

### Ce qui bloque

**La fiabilité, très loin devant tout le reste.** Une démonstration montre une tâche réussie ; une exploitation exige un taux d'échec compatible avec une supervision légère. Sur des tâches de manipulation variées, l'écart entre les deux se compte en ordres de grandeur.

**Le coût.** Il est dominé par les actionneurs et l'intégration, et sa baisse dépend de la série — donc de la demande, donc de la fiabilité. **C'est une boucle** : sans fiabilité, pas de série ; sans série, pas de baisse de coût ; sans baisse de coût, pas de demande.

**La maintenance.** Une machine à plusieurs dizaines d'articulations sollicitées produit du jeu, de l'usure et des pannes. Le nombre de techniciens formés borne le déploiement bien avant la capacité de production.

**Les données.** L'apprentissage de tâches variées dépend de démonstrations acquises une à une, généralement par téléopération.

### Pourquoi la démonstration est particulièrement trompeuse ici

Cinq raisons, toutes vérifiables :

**La téléopération n'est pas toujours déclarée.** Une machine pilotée à distance et une machine autonome produisent des images identiques.

**Le nombre de prises n'est pas indiqué.** Une réussite sur cinquante donne la même vidéo qu'une réussite sur deux.

**La scène est préparée.** Objets connus, positions favorables, éclairage maîtrisé, sol plan.

**Le montage masque les durées.** Une accélération, une coupure, un changement de plan suffisent à effacer une reprise.

**Et l'échec n'est jamais montré**, alors que c'est l'information la plus utile — un système qui échoue proprement est très différent d'un système qui échoue dangereusement.

**Ce qu'il faut demander devant toute démonstration :** combien de prises · quelle part de téléopération · quelle variété d'objets et de positions · quelle durée continue sans intervention · et que se passe-t-il quand ça rate.

### Ce que cela implique

L'humanoïde est **une plateforme, pas une capacité**. Sa présence dans une démonstration ne dit rien sur la généralité du système qui la pilote, laquelle relève des architectures du chapitre 13.

Et les premiers déploiements crédibles se situent là où **l'environnement est humain mais la tâche répétitive** — manutention en entrepôt, chargement, transfert entre postes. C'est-à-dire précisément là où une machine spécialisée serait souvent moins chère, ce qui explique que le débat économique reste ouvert.

**À ne pas confondre avec.** **La robotique généraliste** (dossier 36), qui est une capacité et non une forme. **L'embodied AI** (ch. 13), qui est une thèse sur l'apprentissage. **Physical AI** (ch. 33), qui est un cadrage.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Nombreux acteurs, plateformes disponibles, premiers programmes pilotes en environnement industriel avec supervision. Aucune exploitation autonome documentée à l'échelle. Les annonces de production en série sont des objectifs, non des capacités installées.
> 🔄 **À revoir si** un exploitant tiers publie des données d'exploitation sur plusieurs mois — taux d'intervention humaine, disponibilité, coût de maintenance — sur une flotte en production.

**Renvois** — Couche : agir · Courants : humanoid robotics, Physical AI (ch. 33) · Convergence : robotique généraliste (36).

---

## ◆◆◆ Actionneurs robotiques

**Niveau** — composant · **Couche** — agir

**En une phrase.** Les dispositifs qui convertissent l'énergie en mouvement — et qui déterminent, plus que toute autre pièce, ce qu'une machine peut faire et ce qu'elle coûte.

**Pourquoi on en parle.** Parce que c'est **la brique déterminante de toute la couche et la moins discutée**. Les débats portent sur les modèles et la perception ; les limites viennent le plus souvent d'ici.

**Comment ça fonctionne — trois familles.**

**Électrique.** Un moteur associé à un réducteur. Précis, propre, facile à commander, rendement élevé. Mais un moteur tourne vite avec peu de couple, alors que l'application demande l'inverse : il faut donc un **réducteur**, qui introduit du jeu, du frottement, de l'inertie et de l'usure. **Le réducteur devient souvent le composant qui limite la précision et la durée de vie de l'ensemble** — cas net du mécanisme du volume 1 : résoudre le problème du couple crée le problème du jeu.

**Hydraulique.** Densité de puissance très supérieure, capacité à encaisser les chocs. Mais une centrale, des conduites, des fuites, un rendement moindre et un entretien lourd.

**Quasi-direct.** Un moteur à couple élevé avec une réduction faible ou nulle. On perd en couple maximal, on gagne en absence de jeu, en réversibilité — la machine peut être poussée à la main — et en capacité à mesurer les efforts sans capteur dédié. **C'est l'approche qui a rendu praticables les machines à pattes et une partie des humanoïdes.**

**Les grandeurs qui comptent.** Couple maximal · densité de puissance par kilogramme · précision et jeu · rendement · durée de vie en cycles · et **capacité à encaisser un choc**, souvent oubliée alors qu'elle décide de la survie de la machine en usage réel.

**Ce qui bloque.** **La dissipation.** Un actionneur perd son énergie en chaleur, dans un volume restreint, souvent sans circulation d'air. **La densité de puissance réellement utilisable est bornée par l'évacuation thermique**, non par les caractéristiques électriques — c'est pourquoi un actionneur peut délivrer un couple élevé brièvement et pas en continu.

S'y ajoutent le **coût**, qui domine celui d'une machine multi-articulée, et **l'usure**, qui produit du jeu et donc une imprécision que les capteurs articulaires ne voient pas.

**Ce que cela implique.** Une machine peut être précise selon ses capteurs et imprécise en réalité, parce que le jeu se situe en aval de la mesure. **C'est une défaillance silencieuse d'origine mécanique**, et elle croît avec l'usage.

**À ne pas confondre avec.** **Le moteur seul**, qui n'est qu'un élément de l'actionneur — lequel comprend aussi la réduction, l'électronique de commande, les capteurs et souvent le refroidissement.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Progrès continus sur la densité de puissance et sur les architectures quasi-directes ; le coût unitaire reste le facteur dominant du prix des machines multi-articulées.
> 🔄 **À revoir si** un actionneur combine densité de puissance hydraulique et propreté électrique à un coût de série.

**Renvois** — Couche : agir · Convergence : robotique généraliste (36) · Voir aussi : électronique de puissance (ch. 23).

---

## ◆◆ Mains et préhenseurs

**Niveau** — composant · **Couche** — agir

**En une phrase.** L'interface entre la machine et l'objet — et le sous-système où se joue la généralité.

**Comment ça fonctionne.** Un continuum, du plus spécialisé au plus général. La **ventouse** saisit rapidement des surfaces planes et lisses, à faible coût. La **pince à deux doigts** couvre une large variété d'objets rigides. La **main multi-doigts** permet en principe la réorientation en main et la manipulation fine, au prix d'une complexité considérable.

**L'arbitrage est net** : plus le préhenseur est général, plus il est cher, fragile et difficile à commander. En pratique, la plupart des déploiements industriels utilisent le préhenseur le plus spécialisé que la tâche autorise.

**Ce qui bloque.** **La perception du contact.** Sans retour tactile, la machine ne sait pas si elle tient, si elle serre trop, si l'objet glisse. C'est le lien direct avec la peau électronique du chapitre 7, et c'est le verrou. **La durabilité** : le préhenseur est la pièce qui frotte et qui reçoit les chocs. Et **le nombre d'actionneurs** d'une main multi-doigts, qui multiplie coût, masse et modes de panne.

**Ce que cela implique.** La généralité d'une machine se mesure moins à sa morphologie qu'à **la variété d'objets que son préhenseur peut saisir sans changement d'outil**. C'est une grandeur observable, rarement publiée.

**À ne pas confondre avec.** **La main humaine**, dont la densité de capteurs et la capacité de réorientation restent hors de portée — la comparaison est trompeuse et alimente des attentes non fondées.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour les préhenseurs simples, 🔬 émergent pour les mains multi-doigts en exploitation.
> 🔄 **À revoir si** une main multi-doigts démontre plusieurs milliers d'heures d'exploitation avec un taux de panne compatible avec un usage industriel.

**Renvois** — Couche : agir.

---

## ◆◆ Téléopération

**Niveau** — capacité et doctrine · **Couche** — agir, relier

**En une phrase.** Commander une machine à distance, l'humain fournissant la perception, la décision ou les deux.

**Pourquoi on en parle.** Pour deux raisons de nature opposée, et il faut les tenir ensemble. **C'est la principale source de données** pour l'apprentissage de la manipulation. Et **c'est ce que masquent la plupart des démonstrations spectaculaires**.

**Comment ça fonctionne.** Un opérateur pilote via une interface — manettes, exosquelette, capture de mouvement — et reçoit un retour visuel, parfois haptique. Trois régimes coexistent : **pilotage direct**, l'humain fait tout ; **assistance**, la machine corrige et sécurise ; **supervision**, la machine agit seule et l'humain intervient sur demande — un opérateur pouvant alors superviser plusieurs machines.

**Ce que ça permet.** Opérer en environnement inaccessible ou dangereux · déployer une capacité avant qu'elle soit autonome · **collecter des démonstrations**, ce qui en fait l'infrastructure de collecte du chapitre 13 · et amortir le coût humain sur plusieurs machines en régime de supervision.

**Ce qui bloque.** **La latence.** Au-delà de quelques centaines de millisecondes, le pilotage direct devient difficile et le retour de force instable. Cela borne la distance et impose une liaison de qualité. **Le retour haptique**, dont la fidélité reste limitée. Et **le ratio opérateurs par machine**, qui détermine l'économie : une machine supervisée à un opérateur pour une machine ne réduit pas le coût du travail, elle le déplace.

**Ce que cela implique.** Le **ratio de supervision** est la grandeur économique décisive de toute la couche, et elle est rarement publiée. Une flotte de machines supervisées à un pour un est une solution de mobilité du travail, pas d'automatisation.

**Sûreté et sécurité.** Une liaison de commande est une surface d'attaque dont la compromission produit un effet physique. Traitement au niveau du principe.

**À ne pas confondre avec.** **L'autonomie supervisée** (ch. 16), où la machine décide et l'humain surveille — ici, l'humain décide.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Usage établi en milieu dangereux et en médecine ; usage massif et souvent non déclaré dans les démonstrations et la collecte de données.
> 🔄 **À revoir si** des exploitants publient couramment leur ratio d'opérateurs par machine — ce qui rendrait comparable l'économie réelle des déploiements.

**Renvois** — Couche : agir, relier · Convergence : robotique généraliste (36) · Voir aussi : apprentissage par imitation (ch. 13), haptique (ch. 31).

---

---
