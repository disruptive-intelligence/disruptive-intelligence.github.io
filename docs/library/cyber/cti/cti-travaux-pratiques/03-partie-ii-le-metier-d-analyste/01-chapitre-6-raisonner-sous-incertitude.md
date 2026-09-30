---
title: Chapitre 6 — Raisonner sous incertitude
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
up:
- - CTI — travaux pratiques
  - ../index.md
- - PARTIE II — Le métier d'analyste
  - index.md
---

## 6.1 Ce qu'est une hypothèse, et pourquoi il en faut plusieurs

**Une hypothèse est une explication candidate.** Elle n'est ni vraie ni fausse : elle est plus ou moins compatible avec ce que vous observez, et plus ou moins probable au regard de ce que vous savez par ailleurs.

Le mot est employé partout, et presque toujours au singulier. C'est le problème.

**Le mécanisme du raisonnement à hypothèse unique**, celui que produit le cerveau spontanément :

```
J'observe quelque chose
        ↓
Une explication me vient
        ↓
Je cherche ce qui la confirme
        ↓
Je trouve (on trouve toujours)
        ↓
Je conclus
```


Ce raisonnement n'est pas malhonnête. Il est **efficace** — c'est ce qui permet de traverser une rue sans envisager quatre modèles de circulation. Il devient fautif dès qu'on travaille sur de l'information incomplète et ambiguë, c'est-à-dire en permanence en CTI.

**Le raisonnement à hypothèses concurrentes** :

```
J'observe quelque chose
        ↓
J'énumère les explications possibles, y compris celles qui me déplaisent
        ↓
Pour chaque observation, je regarde quelles hypothèses elle CONTREDIT
        ↓
J'élimine, je hiérarchise
        ↓
Je conclus sur celle qui résiste le mieux, en disant laquelle vient ensuite
```


**La différence décisive est à la troisième ligne.** On ne cherche pas ce qui confirme : on cherche ce qui **discrimine**. Une observation compatible avec les cinq hypothèses est sans valeur analytique, même si elle est spectaculaire. Une observation incompatible avec trois d'entre elles vaut de l'or, même si elle est banale.

🧪 **EN PRATIQUE — la règle des trois**

Devant toute observation qui appelle une explication, imposez-vous d'en écrire **trois** avant d'en retenir une. Pas cinq — trois suffisent, et l'exercice reste faisable en deux minutes.

La troisième est presque toujours la plus utile, parce que les deux premières viennent seules et la troisième demande un effort. C'est aussi celle qui, statistiquement, contient l'explication banale qu'on n'a pas envie de considérer : une erreur de configuration, un service légitime, une coïncidence.

## 6.2 Preuve, indice, corrélation, coïncidence

Quatre mots employés comme synonymes, et qui ne le sont pas.

| Terme | Définition | Ce qu'on peut en faire |
|---|---|---|
| **Preuve** | Un élément qui **exclut** toutes les hypothèses sauf une | Conclure. C'est rare en CTI |
| **Indice** | Un élément qui rend une hypothèse **plus probable** que les autres | Hiérarchiser, cumuler |
| **Corrélation** | Deux phénomènes qui varient ensemble | Formuler une hypothèse, jamais conclure |
| **Coïncidence** | Deux phénomènes simultanés sans lien | Rien — mais elle **ressemble** à une corrélation |

**Le point qui compte** : en CTI, vous travaillez presque exclusivement avec des **indices**. La preuve au sens strict — un élément qui exclut toutes les autres explications — existe surtout après investigation approfondie, et rarement en amont d'une décision.

**La conséquence sur l'écriture** : le mot « preuve » ne doit apparaître dans un produit que lorsqu'il est mérité. Employé pour désigner un indice, il fait passer un faisceau pour une démonstration. Préférez *élément*, *indice*, *observation compatible avec*.

⚠️ **PIÈGE — l'accumulation d'indices faibles**
Dix indices faibles ne font pas un indice fort. Ils peuvent même n'en faire aucun, s'ils sont tous compatibles avec l'hypothèse concurrente. La question n'est jamais *combien d'éléments vont dans mon sens*, mais *combien d'éléments ne vont que dans mon sens*.

## 6.3 Le raisonnement abductif : puissant et piégeux

**Ce que c'est.** Face à une observation, on remonte à l'explication qui la rendrait le mieux compréhensible. C'est le mode de raisonnement dominant du renseignement, de l'enquête et du diagnostic médical — et c'est le bon.

```
Observation : la passerelle reçoit des tentatives d'authentification sur des comptes inexistants
        ↓
Quelle explication rendrait cela normal ?
        ↓
Quelqu'un teste une liste d'identifiants issue d'une fuite
```


**Pourquoi il est piégeux** : il produit une explication **plausible**, et la plausibilité est extrêmement convaincante. Or plausible ne veut pas dire probable, et encore moins vrai.

**Les trois défauts à connaître :**

| Défaut | Manifestation |
|---|---|
| **La meilleure explication disponible n'est pas forcément bonne** | Elle est simplement la meilleure **parmi celles auxquelles vous avez pensé** |
| **Le récit cohérent est plus séduisant que le récit exact** | Une histoire qui se tient emporte l'adhésion, y compris quand elle repose sur peu |
| **La plausibilité augmente avec la familiarité** | Vous trouverez plausible ce qui ressemble à ce que vous avez déjà vu (§7.4) |

**Le contre-poids** est simple et tient en une question : *quelle observation devrais-je faire pour que cette explication devienne fausse ?* Si vous n'en trouvez aucune, votre explication n'est pas solide — elle est **irréfutable**, ce qui en analyse est un défaut et non une qualité.

🎯 **ET MAINTENANT ?**
*Un serveur de votre parc établit chaque nuit à 3 h 15 une connexion sortante vers une adresse inconnue. L'explication qui vient : exfiltration de données. Que faites-vous avant de la retenir ?*
**Réponse** : vous en écrivez deux autres. *Une tâche planifiée légitime — sauvegarde, mise à jour, télémétrie éditeur — dont personne ne se souvient · un agent installé par un projet et jamais documenté.* Puis vous cherchez ce qui **discrimine** : le volume transféré, sa régularité au format près, la présence d'un service correspondant sur la machine, l'existence d'une tâche planifiée. Trente minutes. Dans la majorité des cas rencontrés, l'explication banale gagne — et le rare cas où elle perd est celui où vous serez content d'avoir vérifié plutôt que supposé.

## 6.4 Ce qu'on peut affirmer, ce qu'on peut estimer, ce qu'on doit ignorer

Trois registres, à ne jamais mélanger dans une même phrase.

| Registre | Formulation type | Condition d'emploi |
|---|---|---|
| **Affirmer** | *Nous observons que…* / *Le journal enregistre…* | Un fait constaté, vérifiable, daté |
| **Estimer** | *Nous estimons probable que… — confiance moyenne* | Un jugement argumenté, calibré |
| **Ignorer** | *Nous ne disposons pas d'éléments permettant de déterminer si…* | Quand c'est le cas — et c'est fréquent |

**Le troisième registre est le plus difficile à employer**, pour une raison qui n'a rien d'analytique : il donne l'impression de ne pas faire son travail. C'est faux, et c'est exactement l'inverse.

> **Un produit qui ne contient jamais « nous ne savons pas » n'est pas un produit d'un analyste très bon. C'est un produit d'un analyste qui ne distingue pas ce qu'il sait de ce qu'il suppose.**

**Comment l'écrire sans se dévaloriser** — la différence tient à trois éléments :

| Formulation faible | Formulation professionnelle |
|---|---|
| « On ne sait pas. » | « Nous ne disposons pas d'éléments permettant de déterminer X. » |
| — | + **pourquoi** : « nos journaux ne couvrent que 30 jours » |
| — | + **ce qu'il faudrait** : « une réponse exigerait l'accès à Y » |
| — | + **ce que ça change** : « en conséquence, la décision Z doit être prise sans cet élément » |

La seconde version ne dit pas moins que la première. Elle dit la même chose, et elle est **actionnable** : le destinataire sait quoi faire de son ignorance.

## 6.5 ⚠️ La tentation de la conclusion unique

Trois formes, par ordre de fréquence.

**1. La conclusion arrivée trop tôt.** L'hypothèse se forme dans les premières minutes, et tout ce qui suit sert à la documenter. C'est le biais d'ancrage (§7.3), et il est d'autant plus fort que l'analyste est expérimenté — parce que sa première intuition est souvent bonne, ce qui le dispense de la tester.

**2. La conclusion imposée par le format.** Un produit qui exige une conclusion en une phrase pousse à en produire une, même quand la situation ne le permet pas. Le remède n'est pas d'allonger le produit : c'est d'autoriser explicitement la conclusion « nous ne pouvons pas trancher entre A et B, voici ce qui les départagerait ».

**3. La conclusion attendue.** Le destinataire a une idée en tête, l'analyste le sait, et il produit sans s'en rendre compte le renseignement qui la conforte. C'est le biais du client (§7.7), et c'est le plus difficile à corriger seul.

✅ **BONNE PRATIQUE (P0) — la ligne obligatoire**
Toute évaluation comporte une ligne : *« hypothèse alternative envisagée : … , écartée parce que … »*. Une seule ligne. Elle prouve que le travail a eu lieu, elle donne au lecteur de quoi contester, et elle vous protège le jour où l'alternative se révèle juste — parce que vous l'aviez envisagée et dit pourquoi vous l'écartiez.

## 6.6 🔬 Mini-lab 2 — Trois hypothèses pour un même faisceau

**Objectif** — Produire des hypothèses concurrentes et identifier ce qui les discrimine.
**Durée** 35 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §6.1 à §6.4 · **Livrable** trois hypothèses + éléments discriminants
**Compétences validées** — ✔ générer des hypothèses concurrentes ✔ distinguer confirmation et discrimination ✔ identifier l'information manquante ✔ formuler une conclusion calibrée avec alternative

**Les éléments fournis**

Une organisation du secteur industriel constate les faits suivants sur une période de trois semaines :

```
① 14 nov. — Un compte de service applicatif s'authentifie depuis un poste
             bureautique, ce qu'il n'avait jamais fait en deux ans.
② 16 nov. — Le même compte accède à un partage de fichiers contenant des
             plans techniques. Volume : 340 Mo.
③ 19 nov. — Trois requêtes d'annuaire énumérant les membres du groupe
             d'administration, depuis le même poste.
④ 21 nov. — Un salarié du bureau d'études a démissionné le 8 novembre ;
             son préavis se termine le 8 décembre.
⑤ 24 nov. — Le poste concerné est celui d'un administrateur système, pas
             celui du salarié démissionnaire.
⑥ 26 nov. — Une mise à jour de l'application métier a été déployée le
             13 novembre, la veille du premier événement.
```


**Consigne** : formulez trois hypothèses, indiquez pour chaque élément quelles hypothèses il soutient ou contredit, identifiez ce qui manque, et concluez.

---

**Corrigé commenté**

**Les trois hypothèses**

| # | Hypothèse | Origine |
|---|---|---|
| **A** | **Compromission externe** — un attaquant a obtenu le poste d'un administrateur et utilise le compte de service pour progresser | Vient en premier chez la plupart des analystes |
| **B** | **Menace interne** — le salarié démissionnaire prépare un départ avec des documents | Suggérée par l'élément ④ |
| **C** | **Changement légitime non documenté** — la mise à jour du 13 novembre a modifié le fonctionnement du compte de service, et l'administrateur intervient normalement | **La troisième, celle qui demande un effort** |

**La matrice de discrimination** — pour chaque élément, ce qu'il fait à chaque hypothèse :

| Élément | A — externe | B — interne | C — légitime |
|---|---|---|---|
| ① Compte de service depuis un poste bureautique | Compatible | Compatible | **Compatible et attendu** si la mise à jour a changé le mode d'exécution |
| ② Accès aux plans, 340 Mo | Compatible | **Fortement compatible** | Compatible si l'application traite ces fichiers |
| ③ Énumération du groupe d'administration | **Fortement compatible** | Peu compatible — un salarié du bureau d'études n'a pas ce réflexe | Peu compatible |
| ④ Démission, préavis en cours | Neutre | **Compatible** | Neutre |
| ⑤ **Le poste est celui d'un administrateur, pas du démissionnaire** | Compatible | **Fortement contredit** | Compatible |
| ⑥ Mise à jour la veille du premier événement | Neutre | Neutre | **Fortement compatible** |

**Ce que la matrice montre immédiatement**

L'élément ⑤ **contredit fortement l'hypothèse B**. C'est l'élément le plus discriminant du dossier, et il est le plus banal : il ne s'agit que d'identifier à qui appartient un poste. L'hypothèse B, qui paraissait séduisante grâce à l'élément ④, ne tient plus — sauf à supposer que le démissionnaire ait accès au poste d'un administrateur, ce qui est une hypothèse supplémentaire et non un élément.

L'élément ③ **discrimine entre A et C**. Une mise à jour applicative n'explique pas une énumération du groupe d'administration. C'est le seul élément qui ne trouve pas d'explication dans l'hypothèse légitime.

L'élément ⑥ **soutient fortement C** pour les événements ① et ②, mais pas pour ③.

**La conclusion attendue** — et remarquez qu'elle n'est pas univoque :

> *Nous estimons que les événements ① et ② sont vraisemblablement liés au déploiement du 13 novembre — confiance moyenne, fondée sur la concomitance et sur la nature des accès, cohérente avec le fonctionnement de l'application.*
>
> *L'événement ③ n'est expliqué par aucune hypothèse légitime identifiée et constitue le point d'attention prioritaire — confiance élevée sur le fait, aucune conclusion sur sa cause.*
>
> *L'hypothèse d'une menace interne liée au départ du 8 novembre est **écartée** : le poste concerné n'est pas celui du salarié.*
>
> *Ce qui trancherait : les notes de version du déploiement du 13 novembre · l'existence d'un ticket d'intervention couvrant le 19 novembre · l'origine réseau de la session du poste administrateur ce jour-là.*

**Les trois erreurs attendues**

1. **Retenir A dès le départ** et lire les six éléments comme sa confirmation. L'élément ⑥ est alors ignoré, alors qu'il explique la moitié du dossier.
2. **Retenir B à cause de l'élément ④.** La démission est saillante — elle raconte une histoire. Elle est pourtant contredite par ⑤, qui est factuel et ennuyeux. C'est exactement le biais de saillance du §7.4.
3. **Conclure sur une seule hypothèse.** Le dossier contient probablement **deux phénomènes distincts** : un changement légitime et un événement inexpliqué. Chercher une explication unique à six éléments est une erreur fréquente et coûteuse.

## Synthèse mentale du chapitre 6

Une hypothèse est une explication candidate, et le raisonnement spontané n'en produit qu'une, qu'il passe ensuite son temps à confirmer. La différence décisive est de chercher ce qui **discrimine** plutôt que ce qui confirme : une observation compatible avec toutes les hypothèses est sans valeur, une observation qui en contredit trois vaut de l'or. En CTI, on travaille presque exclusivement avec des indices, rarement avec des preuves — et dix indices faibles ne font pas un indice fort s'ils sont tous compatibles avec l'hypothèse concurrente. Le raisonnement abductif est le bon mode et il est piégeux, parce qu'il produit du plausible, et que le plausible convainc : le contre-poids tient en une question, *quelle observation rendrait cette explication fausse ?* Enfin, trois registres ne se mélangent jamais — affirmer, estimer, ignorer — et le troisième, le plus difficile à employer, est celui qui distingue un analyste qui sait ce qu'il ignore d'un analyste qui ne le distingue pas.

**Trois questions de vérification**

1. Vous avez cinq observations qui vont toutes dans le sens de votre hypothèse. Pourquoi n'est-ce pas nécessairement un bon signe, et que devez-vous chercher à la place ?
2. Une explication vous paraît très plausible. Quelle question posez-vous avant de la retenir, et que signifie le fait de n'y trouver aucune réponse ?
3. Comment écrire « nous ne savons pas » dans un produit destiné à une direction, sans donner l'impression de n'avoir pas travaillé ?

→ **Chapitre 7 — Les biais de l'analyste** : sept mécanismes normaux du raisonnement, illustrés chacun par un extrait de produit réel.

---
