---
title: Chapitre 41 — Décider sous incertitude
source: IT/09 Technologies & prospective/Systèmes technologiques (vol. 1).md
note: Systèmes technologiques (vol. 1)
up:
- - Systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

Une analyse ne sert à rien si elle ne débouche pas sur une décision. Ce chapitre traite de la question qui vient après.

## 41.1 Cinq décisions, pas deux

🖼 **SCHÉMA — Les cinq décisions.** Axe horizontal : coût et engagement croissants, d'« ignorer pour l'instant » à « agir ». Axe vertical : réversibilité décroissante. Positionner les cinq décisions et faire apparaître que les trois du milieu occupent l'essentiel de l'espace utile.



L'erreur la plus fréquente est de poser la question en binaire : y aller ou non. Il existe cinq réponses, et les trois du milieu sont les plus utilisées.

| Décision | Quand | Coût | Ce qu'elle préserve |
|---|---|---|---|
| **Agir** | conditions réunies, avantage à être tôt | élevé, engageant | l'avance |
| **Expérimenter** | incertitude réductible par l'essai | modéré, borné | l'apprentissage |
| **Préparer** | trajectoire crédible, échéance incertaine | faible | la capacité à agir vite |
| **Surveiller** | verrou identifié, signal observable | très faible | l'attention au bon moment |
| **Ignorer pour l'instant** | verrou structurel, pas de signal proche | nul | le temps et l'attention |

**Deux précisions.**

**« Préparer » est la plus sous-utilisée.** Elle consiste à réduire le coût d'une action future sans l'engager : former quelques personnes, cartographier ses dépendances, éviter des choix qui fermeraient des options. Le cas de la migration cryptographique du chapitre 9.7 en est l'exemple type — on ne peut pas attendre le signal pour commencer.

**« Ignorer pour l'instant » est une décision légitime**, à condition d'être datée et motivée. Ce n'est pas la même chose que de ne pas y avoir pensé.

## 41.2 Le coût de l'erreur dans les deux sens

Toute décision peut se tromper de deux façons, et elles ne coûtent pas la même chose.

**Agir trop tôt** coûte : investissement dans une technologie qui n'aboutit pas, choix d'un standard perdant, engagement dans une base installée qu'il faudra abandonner.

**Agir trop tard** coûte : rattrapage plus cher, dépendance à un fournisseur en position de force, perte d'un marché, incapacité à recruter des compétences devenues rares.

**La question à poser n'est donc pas « quelle est la trajectoire la plus probable ? » mais « laquelle des deux erreurs coûte le plus cher dans mon cas ? »**

Ces deux questions ont des réponses différentes, et c'est la seconde qui commande la décision. Une trajectoire peu probable mais dont l'occurrence serait catastrophique justifie de préparer ; une trajectoire probable dont le retard coûterait peu justifie d'attendre.

## 41.3 Réversibilité, option, engagement

Trois notions qui structurent le choix.

**La réversibilité.** Une décision réversible peut être prise avec moins d'information. Une décision irréversible exige davantage. Beaucoup de choix paraissent réversibles et ne le sont pas : ce qui crée une base installée, forme des équipes ou établit une dépendance est difficile à défaire — chapitre 27.3.

**L'option.** Certaines actions n'engagent pas mais préservent la possibilité d'agir. Elles ont un coût faible et une valeur d'autant plus grande que l'incertitude est forte. Le chapitre 29.4 l'a montré sous l'angle de l'acceptabilité : un déploiement progressif franchit des seuils qu'un déploiement massif ne franchirait pas.

**L'engagement.** Certaines décisions valent précisément parce qu'elles sont irréversibles : elles signalent aux autres acteurs, sécurisent une place, déclenchent des investissements complémentaires. **Mais un engagement pris sur une analyse fausse est le plus coûteux des choix.**

## 41.4 Le signal de réexamen daté

C'est le livrable le plus utile de tout ce cours, et le plus rarement produit.

Une décision doit s'accompagner de :

* **un signal observable** — pas « si la technologie progresse », mais un fait constatable ;
* **une date de réexamen** ;
* **la décision alternative** — que fait-on si le signal apparaît ?

**Exemple de formulation :**

> Nous surveillons cette technologie sans investir. Nous réexaminerons si l'une des conditions suivantes est observée : un déploiement en production chez un acteur comparable au nôtre pendant plus de douze mois ; ou l'existence d'une offre assurable. Revue programmée dans dix-huit mois. Si l'un de ces signaux apparaît, nous passons en expérimentation avec un périmètre limité.

Cette formulation tient en quatre lignes. Elle est réfutable, datée, et elle désigne l'action suivante. **C'est ce qu'une analyse technologique doit produire.**

## 41.5 La note d'analyse en une page

Format recommandé, dérivé du protocole du chapitre 40.

| Section | Contenu | Longueur |
|---|---|---|
| **Objet** | ce dont on parle, à quel niveau d'abstraction, en une phrase sans terme de récit | 1 ligne |
| **État** | échelon de preuve atteint, et ce qui est démontré | 3 lignes |
| **Ce qui bloque** | la condition dominante, et pourquoi | 3 lignes |
| **Ce qui devrait devenir vrai** | formulation conditionnelle, deux ou trois étapes | 4 lignes |
| **Ordres de grandeur** | deux ou trois chiffres qui calibrent le sujet | 3 lignes |
| **Recommandation** | l'une des cinq décisions, avec sa justification | 3 lignes |
| **Signaux et réexamen** | ce qui la ferait changer, et à quelle date | 4 lignes |
| **Ce que j'ignore** | explicite | 2 lignes |

**La dernière section est celle qui donne sa crédibilité au reste.** Une note qui n'énonce aucune incertitude sera lue comme une prise de position ; une note qui délimite précisément son ignorance sera lue comme une analyse.

## 41.6 Défendre une position sans surjouer la certitude

Trois situations récurrentes.

**« Donnez-nous une réponse simple. »** Le chapitre 4.5 fournit la forme : ce qui est établi, ce qui ne l'est pas, ce qui trancherait, et quand. C'est une réponse simple — elle n'est pas courte, ce qui n'est pas la même chose.

**« Nos concurrents y vont. »** Argument de marché, non technique. La réponse utile est de demander à quel échelon : pilote, production, ou communiqué. Le chapitre 6.2 fournit la grille.

**« Vous étiez contre, et ça a marché. »** Situation inconfortable et normale. La réponse honnête consiste à revenir à l'analyse d'origine : quelle hypothèse était fausse, et ce signal était-il observable à l'époque ? **Une analyse qui s'est trompée mais dont on peut dire pourquoi vaut mieux qu'une analyse qui a eu raison sans raison.** C'est la seule façon d'améliorer une méthode.

🗣 **Vocabulaire de réunion**

| Ce que vous entendez | Ce que cela signifie | La réponse utile |
|---|---|---|
| « Il faut décider maintenant » | pression, rarement fondée | que se passe-t-il si nous décidons dans six mois ? |
| « On ne peut pas rester spectateur » | argument d'image | entre agir et ignorer, il y a préparer et surveiller |
| « C'est stratégique » | affirmation non testable | quel est le coût de l'erreur dans chaque sens ? |
| « On verra bien » | absence de décision déguisée | quel signal, à quelle date, pour quelle action ? |

🎓 **À ce stade, vous savez…** choisir entre cinq décisions plutôt que deux ; raisonner sur le coût de l'erreur dans les deux sens plutôt que sur la probabilité ; distinguer réversibilité, option et engagement ; formuler un signal de réexamen daté ; et produire une note d'analyse d'une page.

---
