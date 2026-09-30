---
title: Chapitre 15 — Humanoïdes et robots généralistes
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
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
