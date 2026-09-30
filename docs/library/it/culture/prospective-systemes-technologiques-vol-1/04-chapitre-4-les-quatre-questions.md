---
title: Chapitre 4 — Les quatre questions
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
chapter: 4
chapters: 53
---

Le chapitre précédent était dense, et c'était voulu. Vous venez de recevoir neuf conditions, chacune avec sa preuve attendue et son échec typique. Si vous avez eu l'impression qu'il y avait beaucoup à retenir, ce chapitre existe précisément pour vous détromper.

Vous n'avez pas neuf éléments à mémoriser. Vous en avez quatre — et les neuf conditions ne sont qu'un endroit où aller chercher quand la deuxième question demande à être creusée.

## 4.1 Les quatre questions

> **① De quoi parle-t-on ?**
> **② Qu'est-ce qui le contraint ?**
> **③ Qu'est-ce qui devrait devenir vrai ?**
> **④ Qu'est-ce qui me ferait changer d'avis ?**

Ce sont les seules choses que vous devez savoir restituer de mémoire, à froid, sans support. Tout le reste de ce cours se range dessous.

### ① De quoi parle-t-on ?

* À quel niveau d'abstraction se situe l'objet ? Brique, capacité, plateforme, système, doctrine, récit ?
* Quelle capacité concrète est en jeu — pas quel mot, quelle capacité ?
* Quel problème cela résout-il, et pour qui ?
* Quel écart y a-t-il entre l'objet réel et la manière dont on en parle ?

C'est la question la plus négligée et la plus rentable. Dans une conversation professionnelle, elle se pose sous une forme anodine : *« concrètement, ça fait quoi ? »* Vous constaterez qu'elle reste souvent sans réponse précise, et que c'est déjà une réponse.

### ② Qu'est-ce qui le contraint ?

* Contraintes physiques : y a-t-il un mur que rien ne franchira ?
* Fiabilité : cela fonctionne-t-il assez souvent, assez longtemps, hors des conditions choisies ?
* Coût : existe-t-il un mécanisme crédible de baisse ?
* Industrie : sait-on fabriquer, à quelle cadence, avec quel rendement ?
* Infrastructure et compétences : le complément nécessaire existe-t-il ?
* Demande : qui paie, combien, à la place de quoi ?
* Institutions : qui certifie, qui assure, qui répond en cas de dommage ?

C'est ici que la grille des neuf conditions se déploie. Vous n'avez pas à la connaître par cœur : vous devez savoir qu'elle existe et savoir la consulter quand la réponse à ② vous paraît trop courte.

### ③ Qu'est-ce qui devrait devenir vrai ?

* Quelle condition bloque **aujourd'hui** ?
* Quelles dépendances doivent progresser, et dans quel ordre ?
* Qu'est-ce qui change si l'on multiplie l'échelle par dix, par mille ?
* Le déblocage d'une condition en débloquerait-il d'autres ?

Cette question transforme une description en analyse. Elle vous oblige à formuler une **conditionnelle** — *si A et B deviennent vrais, alors C devient plausible* — plutôt qu'une prédiction.

### ④ Qu'est-ce qui me ferait changer d'avis ?

* Quels signaux observables confirmeraient la trajectoire ?
* Quels signaux la contrediraient ?
* Quelle hypothèse de mon raisonnement est la plus fragile ?
* À quelle date devrais-je réexaminer ce diagnostic ?

C'est la question qui distingue une analyse d'une opinion, et c'est celle qu'on oublie systématiquement. Nous y revenons en 4.4.

## 4.2 Pourquoi quatre, et pas quinze

Un modèle mental n'est utile que s'il est disponible **au moment où l'on en a besoin** : en réunion, en lisant un article, en écoutant un commercial. Une grille de quinze points n'est jamais disponible dans ces moments-là. Elle est consultée après coup, quand elle est consultée.

Quatre questions tiennent en mémoire de travail. C'est le seul critère qui compte pour un outil de poche.

Le tableau ci-dessous montre où vont les neuf conditions du chapitre 3. Vous n'avez pas à le mémoriser : il sert à vous convaincre qu'aucune information n'a été perdue dans la compression.

| Condition | Se range sous |
|---|---|
| ① Principe | ② Qu'est-ce qui le contraint ? |
| ② Démonstration | ① De quoi parle-t-on ? |
| ③ Fiabilité | ② Qu'est-ce qui le contraint ? |
| ④ Coût | ② puis ③ |
| ⑤ Demande | ② Qu'est-ce qui le contraint ? |
| ⑥ Industrialisation | ② puis ③ |
| ⑦ Infrastructure et compétences | ③ Qu'est-ce qui devrait devenir vrai ? |
| ⑧ Cadre institutionnel | ② puis ③ |
| ⑨ Usage et doctrine | ③ Qu'est-ce qui devrait devenir vrai ? |

Trois remarques sur ce tableau.

D'abord, plusieurs conditions apparaissent deux fois, sous ② et sous ③. Ce n'est pas une imprécision : une condition non satisfaite est une **contrainte** quand on décrit l'état actuel, et un **objectif** quand on décrit ce qui doit changer. C'est la même information vue depuis deux moments.

Ensuite, la condition ② (démonstration) se range sous la première question et non sous la deuxième. C'est délibéré : savoir ce qui a été démontré fait partie de la description de l'objet, pas de ce qui le limite. Confondre les deux, c'est prendre une démonstration pour un état du monde.

Enfin, aucune condition ne se range sous ④. La quatrième question ne porte pas sur la technologie : elle porte sur **votre raisonnement**.

## 4.3 Observation, interprétation, hypothèse, preuve, décision

Les quatre questions ne servent à rien si l'on confond les statuts de ce qu'on manipule. Cinq niveaux doivent rester distincts, et le vocabulaire courant les mélange en permanence.

| Statut | Définition | Formulation correcte |
|---|---|---|
| **Observation** | ce qui a été constaté, avec son protocole | « le système a parcouru X kilomètres sans intervention, dans telles conditions » |
| **Interprétation** | ce que l'observation semble signifier | « cela suggère que la perception fonctionne dans ce type d'environnement » |
| **Hypothèse** | une explication candidate, non encore établie | « il est plausible que le verrou soit désormais la fiabilité longue durée » |
| **Preuve** | une observation qui exclut les explications concurrentes | « le remplacement du composant a supprimé la panne dans les vingt essais suivants » |
| **Décision** | ce qu'on fait compte tenu de l'incertitude | « nous expérimentons sur un périmètre limité pendant six mois » |

L'erreur la plus fréquente consiste à sauter directement de l'observation à la décision, en laissant implicites l'interprétation et l'hypothèse. Cela produit des décisions qui paraissent fondées sur des faits alors qu'elles reposent sur une interprétation non formulée — et donc jamais discutée.

L'erreur symétrique consiste à traiter une hypothèse solide comme une preuve parce qu'elle est confortable. Une hypothèse qui explique bien les observations reste une hypothèse tant qu'on n'a pas éliminé les explications concurrentes.

**Une décision peut parfaitement être prise sur une hypothèse.** C'est même la situation normale : on décide presque toujours avant de savoir. Ce qui compte est de savoir qu'on le fait, et donc de savoir ce qui, plus tard, montrera qu'on s'est trompé.

## 4.4 Construire sa propre réfutation

La quatrième question est un exercice actif, pas une clause de style. Elle se pratique en trois temps.

**Temps 1 — Identifier l'hypothèse porteuse.** Dans toute analyse, une hypothèse porte plus de poids que les autres. Retirez-la mentalement : si la conclusion tombe, vous l'avez trouvée. C'est celle-là qu'il faut surveiller, pas les neuf autres.

**Temps 2 — Formuler l'observation contraire.** Non pas « si ça ne marche pas », mais : *qu'est-ce que j'observerais, concrètement, dans les dix-huit prochains mois, si cette hypothèse était fausse ?* Une réfutation utile est **observable** et **datée**.

**Temps 3 — Fixer un point de réexamen.** Une analyse sans date de péremption devient une croyance. Écrivez la date. C'est la différence entre « je pense que » et « je pense que, et voici quand je vérifierai ».

### Exemple appliqué

Reprenons le cas Ford du chapitre 1, tel qu'il se présentait en 2016.

| | |
|---|---|
| **Analyse** | un véhicule autonome commercial en 2021 |
| **Hypothèse porteuse** | la fiabilité continuera de progresser au même rythme jusqu'au niveau requis pour supprimer le conducteur |
| **Réfutation observable** | si, au bout de deux ans, le kilométrage entre interventions humaines plafonne au lieu de continuer à croître, l'hypothèse est fausse |
| **Point de réexamen** | fin 2018 |
| **Signal secondaire** | apparition ou absence d'un cadre d'homologation applicable à un système apprenant |

Cette grille tenait en cinq lignes et pouvait être écrite en 2016 avec l'information disponible à l'époque. Elle n'aurait pas garanti la bonne décision. Elle aurait garanti que la mauvaise soit détectée plus tôt — ce qui, dans la plupart des situations professionnelles, est exactement ce qu'on peut espérer de mieux.

## 4.5 « Je ne sais pas encore »

Il existe une compétence professionnelle rare et sous-valorisée : formuler précisément l'étendue de son ignorance.

Comparez trois réponses à la question *« est-ce que cette technologie va s'imposer ? »* :

> **A —** « Oui, c'est l'avenir. »
> **B —** « Personne ne peut le savoir. »
> **C —** « Je ne sais pas encore. Ce qui est établi : la capacité fonctionne en conditions réelles chez trois acteurs. Ce qui ne l'est pas : le coût de maintenance sur cinq ans, et l'existence d'un assureur. Je saurai trancher quand le premier déploiement à cent unités aura douze mois de recul. »

A est une opinion. B est une abdication déguisée en prudence — et elle est fausse, puisqu'on peut toujours savoir quelque chose. C est une analyse.

La réponse C a une propriété que les deux autres n'ont pas : elle **désigne le travail à faire**. Elle dit ce qu'il faut aller chercher et quand la question sera tranchable. C'est la forme que devraient prendre la plupart de vos conclusions dans ce cours.

🗣 **Vocabulaire de réunion**

| Ce que vous entendez | Ce que cela signifie probablement | La question à poser |
|---|---|---|
| « Les signaux sont au vert » | agrégation d'indicateurs favorables, sans indicateur contraire | quel signal, s'il apparaissait, vous ferait changer d'avis ? |
| « C'est prouvé » | il existe une observation compatible | qu'est-ce que cette observation exclut comme explication ? |
| « On a validé le POC » | une démonstration a réussi dans des conditions choisies | quelles conditions, quel taux de succès, quel écart avec la production ? |
| « Il faut y aller maintenant » | argument de fenêtre, souvent non étayé | qu'est-ce qui se passe si on décide dans six mois ? |
| « De toute façon, c'est inéluctable » | affirmation non réfutable | à quoi verrait-on que ça ne l'est pas ? |

🧪 **Lab 2 — Première analyse guidée**

**Objectif.** Produire une analyse complète et réfutable sur une technologie choisie, avec les seuls instruments des chapitres 2 à 4.
**Durée.** 90 minutes. **Difficulté.** 2/3. **Prérequis.** Chapitres 2, 3, 4.
**Contexte.** Choisissez une technologie dont on parle actuellement dans votre secteur, et sur laquelle vous avez un avis. Cet avis préexistant fait partie de l'exercice.
**Travail demandé.**
(a) Répondez à ① en classant l'objet sur l'échelle d'abstraction et en énonçant la capacité concrète en une phrase, sans aucun terme de niveau récit.
(b) Répondez à ② en parcourant les neuf conditions, et désignez **une seule** condition bloquante à ce jour.
(c) Répondez à ③ sous forme conditionnelle explicite.
(d) Répondez à ④ : hypothèse porteuse, observation qui la réfuterait, date de réexamen.
(e) Comparez le résultat à votre avis de départ et notez ce qui a bougé.
**Livrable.** Une page, structurée par les quatre questions. La partie (e) fait trois lignes.
**Compétences validées.** Enchaînement complet des quatre questions ; désignation d'une condition bloquante unique ; formulation d'une réfutation observable et datée.
**Éléments attendus.** Il n'y a pas de réponse unique. Une copie acceptable désigne une condition bloquante et l'argumente ; une copie faible en désigne cinq, ce qui revient à ne pas trancher. La difficulté principale est en (d) : la plupart des premières tentatives produisent une réfutation non observable (« si ça ne marche pas ») au lieu d'un signal daté et constatable. Une copie forte se reconnaît en (e) : elle documente un déplacement, même petit. Si rien n'a bougé, c'est souvent que la grille a été utilisée pour justifier l'avis initial plutôt que pour l'éprouver.

🎓 **À ce stade, vous savez…**

* restituer de mémoire les quatre questions et les dérouler sur un cas ;
* dire où se rangent les neuf conditions, sans les avoir mémorisées ;
* distinguer observation, interprétation, hypothèse, preuve et décision ;
* identifier l'hypothèse porteuse d'une analyse et formuler une réfutation observable et datée ;
* énoncer votre ignorance de manière qui désigne le travail restant.

**Ce que vous ne savez pas encore :** répondre à la question ② quand elle appelle un chiffre. C'est l'objet du chapitre 5.

---
