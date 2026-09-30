---
title: PARTIE II — Le métier d'analyste
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
chapter: 2
chapters: 8
---

> **Le cœur du cours.** Huit chapitres consacrés à une seule question : comment construire un jugement fiable quand on ne possède jamais toutes les informations.
>
> **Où nous sommes dans la boucle analytique** : segments ③ **ANALYSE** et ④ **JUGEMENT**. Nous ne collectons pas encore — c'est la Partie V. Nous apprenons ce qu'il faut savoir faire du matériau **avant** d'aller le chercher, parce que collecter sans savoir analyser produit du volume et rien d'autre.
>
> **Rappel de la règle éditoriale.** Chaque notion introduite ici doit passer un test : *en quoi cela permet-il de produire un meilleur renseignement ?* Vous ne trouverez donc ni développement sur les mécanismes cognitifs, ni digression épistémologique. Chaque biais est illustré par un extrait de produit réel ; chaque technique est présentée avec son coût et le cas où il ne faut pas l'employer.

---

## Chapitre 6 — Raisonner sous incertitude

### 6.1 Ce qu'est une hypothèse, et pourquoi il en faut plusieurs

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

### 6.2 Preuve, indice, corrélation, coïncidence

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

### 6.3 Le raisonnement abductif : puissant et piégeux

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

### 6.4 Ce qu'on peut affirmer, ce qu'on peut estimer, ce qu'on doit ignorer

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

### 6.5 ⚠️ La tentation de la conclusion unique

Trois formes, par ordre de fréquence.

**1. La conclusion arrivée trop tôt.** L'hypothèse se forme dans les premières minutes, et tout ce qui suit sert à la documenter. C'est le biais d'ancrage (§7.3), et il est d'autant plus fort que l'analyste est expérimenté — parce que sa première intuition est souvent bonne, ce qui le dispense de la tester.

**2. La conclusion imposée par le format.** Un produit qui exige une conclusion en une phrase pousse à en produire une, même quand la situation ne le permet pas. Le remède n'est pas d'allonger le produit : c'est d'autoriser explicitement la conclusion « nous ne pouvons pas trancher entre A et B, voici ce qui les départagerait ».

**3. La conclusion attendue.** Le destinataire a une idée en tête, l'analyste le sait, et il produit sans s'en rendre compte le renseignement qui la conforte. C'est le biais du client (§7.7), et c'est le plus difficile à corriger seul.

✅ **BONNE PRATIQUE (P0) — la ligne obligatoire**
Toute évaluation comporte une ligne : *« hypothèse alternative envisagée : … , écartée parce que … »*. Une seule ligne. Elle prouve que le travail a eu lieu, elle donne au lecteur de quoi contester, et elle vous protège le jour où l'alternative se révèle juste — parce que vous l'aviez envisagée et dit pourquoi vous l'écartiez.

### 6.6 🔬 Mini-lab 2 — Trois hypothèses pour un même faisceau

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

### Synthèse mentale du chapitre 6

Une hypothèse est une explication candidate, et le raisonnement spontané n'en produit qu'une, qu'il passe ensuite son temps à confirmer. La différence décisive est de chercher ce qui **discrimine** plutôt que ce qui confirme : une observation compatible avec toutes les hypothèses est sans valeur, une observation qui en contredit trois vaut de l'or. En CTI, on travaille presque exclusivement avec des indices, rarement avec des preuves — et dix indices faibles ne font pas un indice fort s'ils sont tous compatibles avec l'hypothèse concurrente. Le raisonnement abductif est le bon mode et il est piégeux, parce qu'il produit du plausible, et que le plausible convainc : le contre-poids tient en une question, *quelle observation rendrait cette explication fausse ?* Enfin, trois registres ne se mélangent jamais — affirmer, estimer, ignorer — et le troisième, le plus difficile à employer, est celui qui distingue un analyste qui sait ce qu'il ignore d'un analyste qui ne le distingue pas.

**Trois questions de vérification**

1. Vous avez cinq observations qui vont toutes dans le sens de votre hypothèse. Pourquoi n'est-ce pas nécessairement un bon signe, et que devez-vous chercher à la place ?
2. Une explication vous paraît très plausible. Quelle question posez-vous avant de la retenir, et que signifie le fait de n'y trouver aucune réponse ?
3. Comment écrire « nous ne savons pas » dans un produit destiné à une direction, sans donner l'impression de n'avoir pas travaillé ?

→ **Chapitre 7 — Les biais de l'analyste** : sept mécanismes normaux du raisonnement, illustrés chacun par un extrait de produit réel.

---

## Chapitre 7 — Les biais de l'analyste

### 7.1 Les biais ne sont pas un défaut de rigueur

Une mise au point préalable, parce qu'elle change complètement la façon d'aborder ce chapitre.

**Un biais n'est pas une erreur qu'on commet par manque d'attention.** C'est un mode de fonctionnement normal du raisonnement, qui produit d'excellents résultats dans la plupart des situations et des résultats faux dans un contexte précis : information incomplète, ambiguë, et pression temporelle. C'est-à-dire le contexte permanent du CTI.

**Trois conséquences pratiques :**

| Conséquence | Ce que ça implique |
|---|---|
| On ne se débarrasse pas d'un biais par la volonté | « Je vais faire attention » ne fonctionne pas. Il faut des dispositifs |
| L'expérience aggrave certains biais | Un analyste chevronné a des intuitions justes, ce qui le dispense de les tester |
| **On ne détecte pas ses propres biais** | On détecte ceux des autres. D'où la relecture croisée du chapitre 12 |

⚠️ Ce chapitre n'expose aucun mécanisme cognitif sous-jacent. Ce qui compte ici est : **comment ça se voit dans un livrable**, et **quel dispositif l'évite**. Les références académiques figurent en annexe.

### 7.2 Le biais de confirmation

**Ce que c'est** : chercher, retenir et pondérer plus fortement ce qui va dans le sens de l'hypothèse qu'on a déjà.

**Comment ça se voit dans un produit** :

> *« Plusieurs éléments confirment cette hypothèse : l'infrastructure utilisée correspond à celle décrite dans le rapport de mars, le mode opératoire est similaire, et le ciblage sectoriel est cohérent. »*

Trois éléments **compatibles**, présentés comme trois **confirmations**. Aucun n'est discriminant : ils sont tous également compatibles avec « un autre acteur utilise les mêmes techniques », hypothèse que le paragraphe n'envisage pas.

**La reformulation :**

> *« Trois éléments sont compatibles avec cette hypothèse : […]. Ils sont également compatibles avec l'hypothèse d'un acteur distinct employant des techniques largement diffusées. Aucun élément discriminant n'a été identifié à ce stade. »*

**Le dispositif qui fonctionne** : la matrice du §6.6. On ne remplit pas une colonne « éléments à l'appui », on remplit une ligne par élément et une colonne par hypothèse. La structure du tableau rend le biais visible.

### 7.3 L'ancrage

**Ce que c'est** : la première information reçue fixe le cadre, et tout ce qui suit est interprété par rapport à elle.

**Comment ça se voit** : dans la chronologie d'un dossier. La première hypothèse formulée survit à des éléments qui auraient dû la faire abandonner, parce qu'ils sont réinterprétés pour s'y loger.

> *Jour 1 : « probablement une compromission par hameçonnage »*
> *Jour 3 : découverte d'un accès par une passerelle exposée*
> *Jour 3, produit : « l'accès par la passerelle a probablement servi à consolider la compromission initiale »*

Le jour 3 aurait dû remettre en cause le jour 1. Il a été absorbé.

**Le dispositif** : dater les hypothèses et les relire. Concrètement, une ligne dans le dossier — *hypothèse formulée le [date] sur la base de [éléments]* — et une relecture explicite à chaque élément majeur : *cette hypothèse tiendrait-elle si je découvrais cet élément en premier ?*

⚠️ **L'ancrage par le titre.** Un rapport intitulé « Campagne du groupe X contre le secteur de la santé » ancre son lecteur avant la première ligne. Si vous lisez un tel document, notez votre hypothèse **avant** de l'ouvrir. Si vous en écrivez un, sachez que votre titre fait la moitié du travail de persuasion — et pesez-le.

### 7.4 La disponibilité et la saillance

**Ce que c'est** : on surestime ce qui vient facilement à l'esprit — ce dont on a récemment parlé, ce qui est spectaculaire, ce qui raconte une histoire.

**C'est le biais le plus actif en CTI**, pour une raison structurelle : le domaine est saturé de récits. Les publications décrivent des acteurs, des campagnes, des noms de code. Ce qui est raconté devient disponible ; ce qui n'est raconté par personne devient invisible — y compris quand c'est plus probable.

**Comment ça se voit** :

| Ce qui est surestimé | Ce qui est sous-estimé |
|---|---|
| Les acteurs étatiques, très documentés | La criminalité opportuniste, banale |
| Les techniques sophistiquées | Le vol d'identifiants et l'erreur de configuration |
| Ce qui a fait l'objet d'un rapport récent | Ce qui n'intéresse personne parce que trop courant |
| Une menace nommée | Une menace sans nom |

**L'exemple du mini-lab 2** en est une illustration : la démission d'un salarié — élément ④, saillant, romanesque — a plus de poids intuitif que l'appartenance d'un poste — élément ⑤, factuel, ennuyeux. Le second est pourtant décisif et le premier ne l'est pas.

**Le dispositif** : la question de la fréquence de base. *Sur cent situations de ce type, combien relèvent de l'explication que j'envisage ?* Si votre hypothèse est un acteur étatique sophistiqué et que la réponse honnête est « une ou deux sur cent », il vous faut des éléments nettement plus forts que ceux dont vous disposez.

### 7.5 La récence

**Ce que c'est** : le dernier élément reçu pèse plus lourd que les précédents, indépendamment de sa qualité.

**Comment ça se voit** : dans les révisions successives d'une évaluation. À chaque nouvelle information, la conclusion bascule — non parce que la nouvelle information est décisive, mais parce qu'elle est fraîche.

**Le dispositif** : relire l'ensemble du dossier avant chaque révision, et exiger que le changement de conclusion soit justifié par le **caractère discriminant** de l'élément nouveau, pas par son existence. Une question suffit : *si j'avais reçu cet élément il y a trois semaines, aurait-il changé quelque chose ?*

### 7.6 La pensée de groupe et le récit dominant

**Ce que c'est** : dans un collectif, la convergence prématurée vers une conclusion partagée, et la difficulté croissante à exprimer un désaccord à mesure que le consensus se forme.

**Sa forme particulière en CTI** : le **récit dominant** du domaine à un moment donné. Il existe toujours une explication en vogue — une année ce sont les acteurs étatiques, une autre les chaînes d'approvisionnement, une autre l'automatisation par des modèles de langage. Ces sujets sont réels. Le biais consiste à les voir **partout**, y compris là où une explication banale suffirait.

**Comment ça se voit** : quand tous les produits d'une organisation, sur six mois, convergent vers le même type d'explication.

**Le dispositif** : la note dissidente, traitée au §12.4. Et pour l'analyste seul, un exercice simple — *si je devais défendre l'explication la plus banale possible, que dirais-je ?*

### 7.7 Le biais du client

**Ce que c'est** : produire, sans intention consciente, le renseignement que le destinataire attend.

**C'est le biais le plus spécifique au métier**, et le moins traité dans la littérature générale sur les biais. Il ne relève pas de la complaisance : il opère en amont, dans la sélection de ce qu'on retient et dans le choix des mots.

**Ses trois manifestations** :

| Manifestation | Exemple |
|---|---|
| **Le renforcement** | Le RSSI prépare un dossier d'investissement en détection ; les produits de la période mettent en avant les menaces que la détection traiterait |
| **L'atténuation** | Une conclusion embarrassante pour un projet en cours est formulée avec plus de prudence qu'elle ne le mériterait |
| **L'anticipation** | L'analyste ne creuse pas une piste dont il pressent qu'elle dérangera |

**La troisième est la plus grave**, parce qu'elle ne laisse aucune trace : ce qui n'a pas été cherché n'apparaît nulle part.

**Le dispositif** — deux mesures :

1. **Écrire la conclusion avant de connaître l'usage qui en sera fait**, quand c'est possible.
2. **La relecture croisée par quelqu'un qui ne connaît pas le contexte politique** de la demande. C'est l'un des arguments les plus solides en faveur du chapitre 12, y compris dans une petite structure : le relecteur n'a pas besoin d'être analyste, il a besoin d'être extérieur à l'enjeu.

🎯 **ET MAINTENANT ?**
*Votre RSSI vous demande une note sur les menaces visant les accès distants, trois semaines avant un arbitrage budgétaire sur un projet d'authentification renforcée. Comment vous protégez-vous du biais du client ?*
**Réponse** : vous écrivez la note en trois sections nettement séparées — *ce que nous observons* · *ce que nous en estimons* · *ce que cela implique* — et vous rédigez les deux premières **sans lire le dossier du projet**. Puis vous ajoutez une ligne : *« évaluation produite indépendamment du dossier d'investissement en cours, dont l'analyste a eu connaissance après rédaction »*. Cette mention paraît excessive ; elle vaut beaucoup le jour où quelqu'un contestera l'indépendance de l'analyse.

### 7.8 ⚠️ Les sept biais, et où les repérer dans un produit

Grille de relecture. Elle figure en annexe C, et se lit en cinq minutes sur n'importe quel produit.

| Biais | Signe dans le texte | Question de vérification |
|---|---|---|
| **Confirmation** | « Plusieurs éléments confirment » · aucune hypothèse alternative mentionnée | Ces éléments sont-ils compatibles avec autre chose ? |
| **Ancrage** | La conclusion du dossier est celle du premier jour | Cette hypothèse tiendrait-elle si l'ordre des découvertes était inversé ? |
| **Disponibilité** | Une explication sophistiquée là où une banale suffirait | Sur cent cas semblables, combien relèvent de cette explication ? |
| **Saillance** | Le détail romanesque occupe plus de place que le détail décisif | Quel élément discrimine réellement ? |
| **Récence** | La conclusion a changé à la dernière information | Cet élément était-il discriminant, ou seulement récent ? |
| **Groupe / récit dominant** | Tous les produits du semestre concluent dans le même sens | Que dirait l'explication la plus banale ? |
| **Client** | Le produit conforte une décision en préparation | La conclusion aurait-elle été écrite ainsi sans ce contexte ? |

### 7.9 🔴 FIL ROUGE — juillet 2029 : les trois biais de Nour

Le 11 juillet, un dispositif de partage sectoriel diffuse une alerte : une campagne de rançongiciel viserait les fournisseurs de dispositifs médicaux européens. Deux victimes sont mentionnées, sans être nommées.

Nour produit en deux jours une évaluation de quatre pages. Sa conclusion :

> *« Nous estimons très probable qu'HELIOMED figure parmi les cibles de cette campagne. Un renforcement immédiat de la surveillance et un report des travaux non critiques sont recommandés. »*

Claire fait appliquer la procédure : mobilisation de l'exploitation, surveillance renforcée, deux projets décalés. Coût estimé de la semaine : environ 9 000 € en temps mobilisé.

**Ce qui se passe ensuite.** Le 24 juillet, une seconde publication du même dispositif précise que les deux victimes étaient **des distributeurs**, non des fabricants, et que le vecteur d'entrée était un progiciel de gestion commerciale qu'HELIOMED n'utilise pas. La campagne existe. Elle ne concerne pas HELIOMED.

**L'analyse a posteriori**, conduite par Nour et Claire avec la grille du §7.8. Trois biais, cumulés.

| # | Biais | Comment il a opéré |
|---|---|---|
| **1** | **Saillance** | « Fournisseurs de dispositifs médicaux » a été lu comme « nous ». Le terme correspondait à l'identité d'HELIOMED, ce qui a court-circuité la vérification de ce qu'il recouvrait exactement dans l'alerte |
| **2** | **Confirmation** | Nour a listé quatre éléments « allant dans le sens » d'un ciblage. Les quatre étaient compatibles avec une campagne opportuniste sur un progiciel. Aucun n'était discriminant |
| **3** | **Client** | C'était sa première alerte depuis son recrutement, six semaines après un épisode où son travail n'avait produit aucune décision (§3.8). Elle avait besoin que celle-ci en produise une |

**Le troisième est celui qui la marque le plus.** Il n'était ni conscient, ni malhonnête, et il est parfaitement compréhensible — ce qui ne le rend pas moins coûteux.

**Ce qui manquait dans son évaluation**, et qui aurait suffi :

| Élément absent | Ce qu'il aurait produit |
|---|---|
| Une hypothèse alternative | « Campagne opportuniste exploitant un composant commun » — celle qui était vraie |
| La question du vecteur | *Par où entrent-ils ?* — l'alerte ne le disait pas, et cela aurait dû être signalé comme une lacune majeure |
| Un niveau de confiance | « Très probable » sans confiance associée, sur une source unique et partielle |
| Ce qui l'invaliderait | Une seule ligne — *cette évaluation serait remise en cause si les victimes n'étaient pas des fabricants* — aurait déclenché la vérification |

**Ce que Claire ne fait pas.** Elle ne reproche rien, et elle le dit explicitement au comité : *l'erreur est dans le dispositif, pas dans la personne*. Aucune procédure n'exigeait alors une hypothèse alternative, un niveau de confiance ni une clause de réfutation.

**Les trois mesures.**

1. **La clause de réfutation devient obligatoire** sur toute évaluation destinée à déclencher une action — une ligne, non négociable.
2. **Le niveau de confiance devient obligatoire** sur toute affirmation d'évaluation (chapitre 9).
3. **Le seuil de déclenchement d'une mobilisation** est écrit : une source unique, non corroborée, ne déclenche pas de mobilisation — elle déclenche une **vérification**. C'est le chapitre 27.

**Ce que Nour écrit dans son carnet** :

> *J'ai eu raison sur l'existence de la campagne et tort sur tout le reste. Le pire est que si les victimes avaient été des fabricants, personne n'aurait jamais su que mon raisonnement était faux — j'aurais eu raison par accident, et j'aurais recommencé.*

**Livrable de l'épisode.** Trois lignes ajoutées au modèle de fiche opérationnelle : hypothèse alternative · niveau de confiance · ce qui invaliderait. Elles figurent en annexe D.

→ La suite en 🔴 §8.9, quand Nour appliquera pour la première fois une analyse d'hypothèses concurrentes complète.

### Synthèse mentale du chapitre 7

Un biais n'est pas un défaut de rigueur mais un mode de fonctionnement normal, efficace ailleurs et fautif ici : on ne s'en débarrasse pas par la volonté, il faut des dispositifs, et on ne détecte jamais les siens. Le biais de confirmation transforme des éléments compatibles en confirmations ; la matrice à hypothèses concurrentes le rend visible par sa structure même. L'ancrage fait survivre la première hypothèse à des éléments qui auraient dû l'abattre, et un titre ancre son lecteur avant la première ligne. La disponibilité et la saillance sont les biais les plus actifs en CTI, parce que le domaine est saturé de récits : ce qui est raconté devient disponible, ce qui n'intéresse personne devient invisible — y compris quand c'est plus probable. Le biais du client est le plus spécifique au métier et le plus difficile à corriger seul, surtout dans sa forme la plus grave : la piste qu'on ne creuse pas ne laisse aucune trace. Enfin, avoir raison par accident est plus dangereux qu'avoir tort, parce qu'on recommence.

**Trois questions de vérification**

1. « Plusieurs éléments confirment cette hypothèse. » Pourquoi cette phrase doit-elle systématiquement déclencher une vérification, et laquelle ?
2. Vous concluez à l'action d'un acteur sophistiqué. Quelle question de fréquence vous posez-vous, et que faites-vous si la réponse est défavorable ?
3. Pourquoi la forme la plus grave du biais du client est-elle celle qui ne laisse aucune trace, et quel dispositif la corrige ?

→ **Chapitre 8 — Les techniques d'analyse structurée** : les méthodes qui rendent ces dispositifs opérationnels, avec leur coût et les cas où il ne faut pas les employer.

---

## Chapitre 8 — Les techniques d'analyse structurée

### 8.1 Pourquoi structurer

La raison n'est pas que les analystes raisonnent mal. C'est que **la mémoire de travail est limitée**, et que le raisonnement non écrit dépasse rapidement sa capacité.

Concrètement : au-delà de trois hypothèses et cinq éléments, personne ne tient mentalement la matrice de qui contredit quoi. On simplifie sans s'en apercevoir — et la simplification retient ce qui est saillant, pas ce qui est discriminant. C'est le §7.4, appliqué à sa propre pensée.

**Ce qu'une technique structurée apporte**, et c'est tout ce qu'elle apporte :

| Apport | Mécanisme |
|---|---|
| **Externaliser** | Le raisonnement est sur la table, plus dans la tête |
| **Rendre visible ce qui manque** | Une case vide dans un tableau se voit ; une absence dans un raisonnement, non |
| **Forcer l'exhaustivité minimale** | On ne peut pas remplir une colonne « hypothèse C » sans en formuler une |
| **Rendre le raisonnement auditable** | Un tiers peut contester une case, pas une intuition |

📌 **Ce qu'une technique n'apporte pas.** Elle ne rend pas une analyse juste. Elle rend une analyse **contestable** — c'est-à-dire vérifiable par autrui. Une matrice remplie avec des éléments faux produit une conclusion fausse, proprement documentée. La structuration discipline le raisonnement ; elle ne remplace ni la qualité des sources ni le jugement.

### 8.2 L'analyse d'hypothèses concurrentes

La technique centrale du métier. Voici la méthode complète, en sept étapes.

**Étape 1 — Énumérer les hypothèses.** Trois minimum, y compris celles qui déplaisent et celle qui est banale. Elles doivent être **mutuellement exclusives** autant que possible, et couvrir l'espace des possibles.

**Étape 2 — Lister les éléments.** Tout ce dont vous disposez : observations, informations de source externe, absences significatives. Chaque élément sur une ligne.

**Étape 3 — Construire la matrice.** Une ligne par élément, une colonne par hypothèse.

**Étape 4 — Remplir, en évaluant la compatibilité.** Pour chaque case, une seule question : *si cette hypothèse était vraie, cet élément serait-il attendu ?*

| Symbole | Signification |
|---|---|
| `++` | Fortement attendu — l'hypothèse le prédit |
| `+` | Compatible |
| `0` | Neutre — n'apporte rien |
| `−` | Peu compatible — l'hypothèse le rend surprenant |
| `−−` | **Fortement contredit** — l'hypothèse le rend très improbable |

**Étape 5 — Lire les colonnes, pas les lignes.** C'est le renversement méthodologique de la technique.

> **On ne retient pas l'hypothèse qui a le plus de `++`. On élimine celles qui ont des `−−`.**

Une hypothèse qui explique tout n'est pas nécessairement forte : elle est peut-être seulement vague. Une hypothèse contredite par un seul élément solide est éliminée, même si dix autres éléments la soutiennent.

**Étape 6 — Identifier ce qui manque.** Quelle information, si vous l'obteniez, produirait un `−−` quelque part ? C'est votre priorité de collecte — et c'est la jonction avec le chapitre 14.

**Étape 7 — Conclure.** L'hypothèse retenue, celle qui vient ensuite, ce qui les départagerait, et le niveau de confiance.

🧪 **EN PRATIQUE — la matrice, format court**

| Élément | H-A | H-B | H-C |
|---|---|---|---|
| ① … | `+` | `+` | `++` |
| ② … | `++` | `−−` | `0` |
| ③ … | `+` | `−` | `−−` |
| **Verdict** | Tient | **Éliminée** (②) | Affaiblie (③) |

**Ce que la lecture en colonnes révèle immédiatement** : ici, l'hypothèse B est éliminée par un seul élément, quelle que soit la quantité de soutien qu'elle recueille par ailleurs. C'est exactement ce qui s'est passé au mini-lab 2 avec l'appartenance du poste.

### 8.3 Génération d'hypothèses et test de complétude

L'étape 1 est celle qu'on bâcle, et une matrice construite sur des hypothèses mal choisies produit une conclusion propre et fausse.

**Trois méthodes de génération**, à combiner :

| Méthode | Principe | Ce qu'elle débloque |
|---|---|---|
| **Par acteur** | Qui pourrait produire cette observation ? | Les hypothèses d'origine |
| **Par mécanisme** | Quel enchaînement produirait cela ? | Les hypothèses techniques et **les explications légitimes** |
| **Par inversion** | Que faudrait-il pour que ce ne soit rien ? | L'hypothèse banale, celle qu'on n'écrit jamais |

**Le test de complétude** — trois questions à poser à votre liste :

1. Ai-je une hypothèse **bénigne** ? Erreur de configuration, service légitime, coïncidence.
2. Ai-je une hypothèse **désagréable** ? Celle qui impliquerait que nous avons échoué quelque part.
3. Ai-je une hypothèse **ennuyeuse** ? Celle qui ne produira aucun rapport intéressant.

⚠️ Si les trois manquent, votre matrice est déjà orientée avant d'être remplie. Les hypothèses bénignes et ennuyeuses sont, statistiquement, les plus souvent vraies — et les moins souvent écrites.

### 8.4 Indicateurs et signaux d'alerte

**Le principe** : au lieu d'attendre de savoir laquelle des hypothèses est vraie, on définit **à l'avance** ce qui trancherait, et on surveille.

**Comment on construit une grille de signaux :**

| Hypothèse | Si elle est vraie, on devrait observer… | Ce qui l'infirmerait |
|---|---|---|
| A — compromission externe | Persistance, mouvement latéral, communication sortante inhabituelle | Aucune activité au-delà de l'événement initial |
| B — menace interne | Accès en dehors du périmètre habituel de la personne, sur ses propres identifiants | Les accès proviennent d'un compte qui n'est pas le sien |
| C — changement légitime | Correspondance avec une note de version, un ticket, un déploiement | Aucune trace de changement dans les registres |

**Ce que cette grille change** : elle transforme une analyse figée en **dispositif de veille orienté**. Et surtout, elle permet de conclure honnêtement en attendant : *« nous ne pouvons pas trancher ; voici les trois signaux que nous surveillons et qui trancheraient »*. C'est une conclusion parfaitement acceptable, et infiniment plus utile qu'une conclusion forcée.

✅ **BONNE PRATIQUE (P1)** — Cette grille est aussi ce qui alimente le chapitre 30 : les signaux d'alerte deviennent des requêtes de détection. C'est le lien le plus direct entre l'analyse et l'opérationnel, et il est rarement exploité.

### 8.5 Avocat du diable et équipe rouge analytique

Deux dispositifs contre le consensus prématuré et le biais de confirmation.

| Dispositif | Principe | Quand l'employer | Coût |
|---|---|---|---|
| **Avocat du diable** | Une personne est chargée d'attaquer la conclusion retenue, quelle que soit son opinion réelle | Décision engageante, conclusion consensuelle trop rapide | 30 à 60 min |
| **Équipe rouge analytique** | Un groupe construit l'argumentaire complet de l'hypothèse concurrente | Enjeu majeur, désaccord persistant | Une demi-journée |

**La condition de fonctionnement du premier**, et elle est souvent manquée : le rôle doit être **explicitement attribué**, pas spontané. Une objection spontanée est reçue comme une opposition personnelle ; une objection produite au titre d'un rôle est reçue comme un service. La différence de climat est considérable, et elle décide de l'efficacité du dispositif.

📌 **LIMITES** — L'avocat du diable ritualisé perd son effet. S'il est systématique et que chacun sait que « c'est le rôle », l'exercice devient une formalité. Employez-le sur les décisions qui comptent, pas sur toutes.

### 8.6 L'analyse des hypothèses clés

**Ce que c'est** : identifier les **présupposés** sur lesquels repose votre raisonnement, et les tester un par un.

Une hypothèse clé n'est pas une hypothèse au sens du §6.1. C'est quelque chose que vous tenez pour acquis **sans l'avoir formulé** — et qui, s'il est faux, effondre tout.

**Exemples d'hypothèses clés courantes en CTI** :

| Présupposé implicite | Ce qui se passe s'il est faux |
|---|---|
| « Nos journaux couvrent le périmètre concerné » | L'absence d'observation ne vaut rien (§4.3) |
| « Les deux sources sont indépendantes » | Le recoupement n'existe pas (§10.4) |
| « L'adversaire n'a pas connaissance de nos mesures » | Toute la logique de détection est fragilisée |
| « Ce produit est déployé dans la version que nous croyons » | L'exposition est mal évaluée |
| « Le comportement observé est intentionnel » | On analyse une erreur comme une attaque |

**La méthode** : écrire la conclusion, puis se demander *qu'est-ce que je tiens pour vrai sans l'avoir vérifié ?* Lister trois à cinq présupposés, et pour chacun : *comment le vérifier, et que se passe-t-il s'il est faux ?*

C'est la technique la moins coûteuse du chapitre — quinze minutes — et celle dont le rendement est le plus élevé, parce qu'elle attaque le raisonnement à sa base plutôt qu'à ses conclusions.

### 8.7 📌 Le coût de chaque technique, et quand ne pas l'employer

C'est la section que les cours de méthode omettent, et c'est celle qui décide de l'adoption réelle.

| Technique | Coût | À employer quand | **À ne pas employer quand** |
|---|---|---|---|
| Règle des trois hypothèses (§6.1) | 2 min | **Toujours** | Jamais d'exception |
| Matrice d'hypothèses concurrentes | 1 à 3 h | Dossier ambigu, décision engageante, désaccord | Le fait est établi · l'urgence est réelle · une seule hypothèse est plausible et vérifiable en dix minutes |
| Génération structurée d'hypothèses | 20 min | Dossier complexe, ou quand la première liste paraît courte | Situation routinière |
| Grille de signaux d'alerte | 30 min | Quand on ne peut pas trancher maintenant | Quand la question sera résolue avant que la grille ne serve |
| Avocat du diable | 30-60 min | Décision engageante, consensus rapide | Décisions courantes — l'effet s'use |
| Équipe rouge analytique | 1/2 journée | Enjeu majeur | Le reste du temps |
| Analyse des hypothèses clés | 15 min | **Presque toujours** — meilleur rendement du chapitre | Rarement inutile |

⚠️ **PIÈGE — la méthode qui coûte plus que la décision**
Une matrice complète sur un constat qui sera tranché par une requête de dix minutes est du gaspillage, et pire : elle discrédite la méthode auprès de ceux qui la subissent. **La proportionnalité est une compétence analytique à part entière.** Deux règles simples : si la décision est réversible et peu coûteuse, décidez et corrigez ; si elle est engageante ou irréversible, structurez.

🎯 **ET MAINTENANT ?**
*Il est 17 h, un signalement arrive, une décision de blocage est attendue avant 18 h. Vous n'avez pas le temps d'une matrice. Que faites-vous ?*
**Réponse** : la règle des trois hypothèses — deux minutes — et l'analyse des hypothèses clés — dix minutes, sur les deux ou trois présupposés qui portent la décision. Vous écrivez les trois hypothèses, vous identifiez ce que vous tenez pour acquis, et vous décidez en le disant. La conclusion sera : *« nous recommandons le blocage, sur l'hypothèse A ; cette recommandation repose sur le présupposé que [X], non vérifié à cette heure ; si [X] est faux, la mesure est inutile mais sans effet de bord »*. C'est court, honnête, et cela permet de décider.

### 8.8 ✅ Livrable — La matrice d'hypothèses concurrentes

Modèle complet, à reprendre en annexe C.

**En-tête**

| Champ | Contenu |
|---|---|
| Question analytique | *(formulée comme une question, pas comme un sujet)* |
| Demandeur | *(nom)* |
| Date | *(et date de réexamen prévue)* |
| Analyste | *(nom)* · Relecteur : *(nom)* |

**Hypothèses** — trois minimum, dont une bénigne et une ennuyeuse

| Réf | Hypothèse | Origine de la formulation |
|---|---|---|
| H-A | | |
| H-B | | |
| H-C | | |

**Matrice**

| Réf | Élément | Source | Date | H-A | H-B | H-C |
|---|---|---|---|---|---|---|
| ① | | | | | | |

**Lecture**

| Hypothèse | Éliminée par | Verdict |
|---|---|---|

**Hypothèses clés** *(ce que je tiens pour acquis)*

| Présupposé | Vérifié ? | Si faux, alors… |
|---|---|---|

**Conclusion**

- Hypothèse retenue : … — **confiance** : …
- Hypothèse suivante la plus probable : …
- **Ce qui trancherait** : …
- **Ce qui invaliderait cette conclusion** : …
- Réexamen : …

### 8.9 🔴 FIL ROUGE — septembre 2029 : la première matrice

Six semaines après l'épisode de juillet (§7.9), un nouveau signalement arrive : un partenaire industriel d'HELIOMED informe que trois de ses clients — dont deux fournisseurs de dispositifs médicaux — ont subi une intrusion en août. Le vecteur n'est pas précisé.

**Ce que Nour aurait fait en juillet** : conclure au ciblage sectoriel, recommander une mobilisation.

**Ce qu'elle fait cette fois.** Elle bloque deux heures et construit une matrice.

**Les hypothèses**

| Réf | Hypothèse | Origine |
|---|---|---|
| **H-A** | Ciblage sectoriel des fournisseurs de dispositifs médicaux | Par acteur — l'hypothèse spontanée |
| **H-B** | Exploitation opportuniste d'un composant commun au secteur | Par mécanisme — celle qui manquait en juillet |
| **H-C** | Compromission du partenaire lui-même, ses clients étant atteints par ricochet | Par inversion — **l'hypothèse ennuyeuse** |

**La matrice**

| Réf | Élément | H-A | H-B | H-C |
|---|---|---|---|---|
| ① | Trois clients touchés en un mois | `+` | `+` | `++` |
| ② | Deux sur trois sont des fabricants de dispositifs médicaux | `++` | `+` | `0` |
| ③ | **Le troisième est un équipementier automobile** | `−−` | `+` | `+` |
| ④ | Les trois utilisent le même prestataire d'infogérance — le partenaire | `0` | `0` | `++` |
| ⑤ | Aucune revendication publique | `+` | `+` | `+` |
| ⑥ | Le partenaire n'a pas signalé d'incident chez lui | `0` | `0` | `−` |

**La lecture en colonnes**

| Hypothèse | Verdict |
|---|---|
| **H-A** | **Éliminée** par ③. Un équipementier automobile n'entre pas dans un ciblage sectoriel médical |
| H-B | Tient. Aucun élément ne la contredit |
| **H-C** | **La plus soutenue** — ① et ④ la prédisent fortement. Affaiblie par ⑥, mais faiblement : une organisation peut ignorer sa propre compromission |

**L'élément ③ est le pivot**, et il aurait pu passer inaperçu. Nour ne l'avait obtenu qu'en rappelant le partenaire pour demander la liste complète des victimes — dix minutes de téléphone. Sans cette question, sa matrice comportait deux fabricants sur deux, et H-A tenait.

**Les hypothèses clés identifiées**

| Présupposé | Vérifié ? | Si faux |
|---|---|---|
| Les trois victimes sont bien clientes du même partenaire | ✅ confirmé | — |
| Le partenaire nous dit tout ce qu'il sait | ❌ non vérifiable | H-C serait renforcée |
| HELIOMED est cliente de ce partenaire pour un périmètre significatif | ✅ vérifié — **poste de travail et support N1** | — |

**La conclusion produite**

> *Nous estimons **probable** que ces trois intrusions procèdent d'une compromission du prestataire commun plutôt que d'un ciblage sectoriel — **confiance moyenne**, fondée sur la présence d'une victime hors secteur et sur le prestataire partagé, affaiblie par l'absence de signalement du prestataire lui-même.*
>
> *L'hypothèse d'un ciblage sectoriel est **écartée** : l'une des trois victimes est un équipementier automobile.*
>
> *HELIOMED est exposée à cette hypothèse : le prestataire concerné administre notre parc bureautique.*
>
> *Ce qui trancherait : le vecteur d'entrée constaté chez les trois victimes · la confirmation ou l'infirmation d'un incident chez le prestataire · l'existence d'une connexion d'administration anormale sur notre propre parc.*
>
> *Ce qui invaliderait : la découverte d'un vecteur commun indépendant du prestataire.*

**Ce que la décision devient.** Pas une mobilisation générale. Trois actions ciblées : une recherche rétrospective sur les connexions d'administration du prestataire depuis juillet · une question écrite au prestataire sur son propre état · une revue des accès dont il dispose. Coût : une journée-homme, contre neuf mille euros en juillet.

**Le résultat, trois semaines plus tard.** Le prestataire confirme une compromission de l'un de ses postes d'administration, détectée fin août, non signalée à ses clients. La recherche rétrospective d'HELIOMED ne trouve rien — les accès du prestataire au parc d'HELIOMED transitaient par un chemin non concerné. Aucune compromission.

**Ce que Nour retient**, et qui est différent de juillet :

> *Cette fois j'ai eu raison, mais ce n'est pas ce qui compte. Ce qui compte est que j'aurais pu avoir tort et qu'on l'aurait vu : la matrice disait exactement ce qui l'aurait renversée.*

**Livrable de l'épisode.** La matrice complète, versée au dossier — et la question de dix minutes au partenaire, devenue un réflexe : *avez-vous la liste complète des victimes ?*

→ La suite en 🔴 §9.7, quand il faudra mettre un mot sur « probable » et « confiance moyenne ».

### Synthèse mentale du chapitre 8

On structure parce que la mémoire de travail est limitée : au-delà de trois hypothèses et cinq éléments, on simplifie sans s'en apercevoir, et la simplification retient le saillant plutôt que le discriminant. Une technique n'apporte pas la justesse, elle apporte la contestabilité — une matrice remplie d'éléments faux produit une conclusion fausse proprement documentée. Le renversement méthodologique de l'analyse d'hypothèses concurrentes tient dans une phrase : on ne retient pas l'hypothèse la plus soutenue, on élimine celles qui sont contredites. La génération d'hypothèses se teste par trois questions — en ai-je une bénigne, une désagréable, une ennuyeuse — et leur absence signale une matrice déjà orientée. L'analyse des hypothèses clés attaque le raisonnement à sa base pour quinze minutes de travail : c'est le meilleur rendement du chapitre. Enfin, la proportionnalité est une compétence analytique : une méthode qui coûte plus que la décision qu'elle éclaire discrédite la méthode.

**Trois questions de vérification**

1. Une hypothèse est soutenue par huit éléments et contredite par un seul. Que faites-vous, et pourquoi ce n'est pas une question de comptage ?
2. Vous avez trois hypothèses et aucune n'est bénigne. Qu'est-ce que cela révèle, et que faites-vous avant de remplir la matrice ?
3. Une décision de blocage est attendue dans une heure. Quelles techniques employez-vous, et laquelle écartez-vous malgré son intérêt ?

→ **Chapitre 9 — Calibrer** : mettre un mot sur « probable », un chiffre derrière « confiance moyenne », et cesser de confondre la solidité d'une conclusion avec la gravité de son objet.

---

## Chapitre 9 — Calibrer

### 9.1 Confiance, probabilité, gravité : trois axes indépendants

C'est la distinction fondatrice du chapitre, et la faute la plus fréquente du métier consiste à en fusionner deux — ou les trois.

| Axe | Question | Ce qu'il mesure |
|---|---|---|
| **Probabilité** | Quelle est la chance que ce soit vrai ? | Une **estimation sur le monde** |
| **Confiance** | Quelle est la solidité de ma base pour l'affirmer ? | Une **estimation sur mon propre travail** |
| **Gravité** | Qu'est-ce que ça change si c'est vrai ? | Une **estimation de l'impact** |

**Les quatre combinaisons qui montrent leur indépendance :**

| Probabilité | Confiance | Gravité | Situation | Ce qu'on en fait |
|---|---|---|---|---|
| Élevée | Élevée | Faible | Une campagne massive nous vise, mais nos mesures la neutralisent | Informer, ne pas mobiliser |
| Élevée | **Faible** | Élevée | Une source unique et non vérifiée annonce une menace majeure | **Vérifier en priorité** — ne pas agir, ne pas ignorer |
| Faible | Élevée | Élevée | Un scénario peu probable mais dont nous savons qu'il serait dévastateur | Préparer, sans urgence |
| Faible | Faible | Faible | Une rumeur sans conséquence | Archiver avec motif |

**La deuxième ligne est celle qui compte.** C'est exactement la situation de juillet 2029 dans le fil rouge (§7.9) : probabilité annoncée élevée, gravité élevée, **confiance non exprimée** — et la mobilisation a été déclenchée sur une source unique. Si la confiance avait été écrite, la décision aurait été « vérifier », pas « mobiliser ».

> **Une menace terrible peut être établie avec une confiance faible. Ce n'est pas une contradiction : c'est l'information la plus utile que vous puissiez transmettre.**

⚠️ **PIÈGE — la fusion silencieuse**
« Menace critique » fusionne les trois axes en un mot. Le destinataire ne sait ni si c'est probable, ni si c'est établi, ni pourquoi c'est critique. Il réagira à l'adjectif — c'est-à-dire au ton, pas au contenu.

### 9.2 Le langage estimatif : pourquoi « possible » ne veut rien dire

**Le problème.** Les mots de probabilité sont interprétés très différemment d'une personne à l'autre. Des études menées dans plusieurs contextes professionnels montrent que des expressions comme *probable*, *possible* ou *vraisemblable* recouvrent, selon les lecteurs, des fourchettes qui vont du quasi-certain au peu vraisemblable — et que ces écarts persistent y compris entre professionnels du même domaine.

**Le cas de « possible »** mérite un traitement à part : il est le mot le plus employé et le moins informatif de la langue analytique. *Possible* signifie littéralement « non exclu », ce qui est vrai de presque tout. Une phrase qui dit « il est possible que X » n'a transmis aucune information au lecteur.

🧪 **EN PRATIQUE — le test du remplacement**

Prenez une phrase de votre produit contenant un mot de probabilité, et remplacez-le par « non exclu ». Si la phrase reste acceptable, le mot ne portait rien.

| Phrase originale | Test | Verdict |
|---|---|---|
| « Il est possible que ce groupe cible notre secteur » | « Il n'est pas exclu que ce groupe cible notre secteur » | ❌ Aucune information |
| « Nous estimons probable que… » | « Il n'est pas exclu que… » | ✅ Le sens change — le mot portait |

### 9.3 L'échelle de probabilité verbale

**Le principe** : une échelle fermée, avec des correspondances numériques indicatives, publiée en annexe de chaque produit — pour que le lecteur sache ce que les mots signifient chez vous.

| Expression | Fourchette indicative | Usage |
|---|---|---|
| **Quasi certain** | > 90 % | Rare. Réservé aux faits presque établis |
| **Très probable** | 75 - 90 % | Conclusion forte |
| **Probable** | 55 - 75 % | Conclusion ordinaire |
| **Aussi probable qu'improbable** | 45 - 55 % | **À employer** — on ne peut pas trancher |
| **Peu probable** | 25 - 45 % | |
| **Très peu probable** | 10 - 25 % | |
| **Quasi exclu** | < 10 % | Rare |

**Quatre règles d'emploi**, sans lesquelles l'échelle ne sert à rien :

1. **Un seul mot par affirmation.** Pas de « probable à très probable » — c'est un refus déguisé de trancher.
2. **Le mot porte sur une affirmation précise.** « Probable que le prestataire soit compromis » et « probable que nous soyons touchés » sont deux affirmations distinctes qui appellent deux calibrages.
3. **Les chiffres sont indicatifs, pas calculés.** Ne les faites pas figurer comme des résultats — ils donneraient une fausse précision.
4. **L'échelle est publiée**, ou elle est inutile.

⚠️ **PIÈGE — la fausse précision**
« Nous estimons à 73 % la probabilité que… » n'est pas plus rigoureux que « probable ». C'est moins rigoureux, parce que le chiffre suggère un calcul qui n'a pas eu lieu. Réservez les valeurs numériques précises aux cas où elles proviennent réellement d'un dénombrement.

### 9.4 Sur quoi repose un niveau de confiance

La confiance n'est pas une impression. Elle s'appuie sur quatre facteurs, et l'exercice consiste à les évaluer explicitement.

| Facteur | Question | Effet |
|---|---|---|
| **Qualité des sources** | Fiables ? directes ? intéressées ? (chapitre 10) | Fondamental |
| **Corroboration réelle** | Plusieurs sources **indépendantes** ? | Fondamental — attention à la circularité |
| **Ancienneté** | L'information est-elle encore valide ? (§4.4) | Décroissant avec le temps |
| **Cohérence interne** | Le raisonnement tient-il sans hypothèse ad hoc ? | Décisif |

**L'échelle de confiance, en trois niveaux** — trois suffisent, cinq brouillent :

| Niveau | Signification | Ce qui le caractérise |
|---|---|---|
| **Élevée** | Base solide, peu susceptible d'être renversée | Sources multiples et indépendantes, information récente, raisonnement sans zone d'ombre |
| **Moyenne** | Base correcte avec des lacunes identifiées | Sources limitées ou partiellement corroborées, ou raisonnement reposant sur un présupposé non vérifié |
| **Faible** | Base fragile | Source unique, information ancienne, ou nombreux présupposés |

✅ **BONNE PRATIQUE (P0) — la confiance s'explique en une ligne**
N'écrivez jamais un niveau seul. Écrivez toujours *pourquoi*.

> *— confiance moyenne, fondée sur deux sources dont l'indépendance n'est pas établie et sur un présupposé non vérifié quant au périmètre de nos journaux.*

Cette ligne coûte quinze secondes. Elle transforme une étiquette en information exploitable : le lecteur sait **quoi faire pour améliorer la confiance**.

### 9.5 Exprimer une incertitude sans paraître incompétent

C'est la difficulté pratique du chapitre, et elle est réelle : beaucoup d'analystes surestiment leur confiance par crainte de paraître inutiles.

**Ce qui produit l'impression d'incompétence :**

| Formulation | Pourquoi elle dessert |
|---|---|
| « On ne sait pas. » | Aucune information, aucune direction |
| « C'est difficile à dire. » | Décrit votre état d'esprit, pas la situation |
| « Il faudrait creuser. » | Sans dire quoi ni combien de temps |
| « Plusieurs hypothèses sont possibles. » | Vrai de toute situation |

**Ce qui produit l'impression de maîtrise** — la même incertitude, exprimée en quatre éléments :

```
1. Ce que nous savons        « Nous observons X, établi par Y. »
2. Ce que nous estimons      « Nous estimons probable Z — confiance moyenne, parce que… »
3. Ce que nous ignorons      « Nous ne pouvons pas déterminer W, faute de V. »
4. Ce qui trancherait        « L'accès à V permettrait de conclure sous N jours. »
```

**La différence entre les deux colonnes n'est pas le niveau de connaissance.** C'est la structure. Un analyste qui expose son incertitude de manière structurée paraît maîtriser sa question ; un analyste qui l'exprime globalement paraît la subir.

🎯 **ET MAINTENANT ?**
*Votre direction vous demande en réunion : « est-ce qu'on est visés, oui ou non ? ». Que répondez-vous ?*
**Réponse** : jamais « oui » ni « non », et jamais « c'est compliqué ». La formulation qui fonctionne tient en trois phrases : *« Nous n'avons aucune observation d'activité dirigée contre nous — c'est établi, nos journaux couvrent la période. Nous estimons probable que nous entrions dans le périmètre d'une campagne opportuniste en cours, avec une confiance moyenne. La question qui trancherait est celle du vecteur d'entrée employé chez les victimes connues ; nous l'avons posée et attendons la réponse sous 48 heures. »* Vous n'avez pas répondu oui ou non, et votre interlocuteur sait exactement où il en est.

### 9.6 ⚠️ Les formulations à bannir, et par quoi les remplacer

| À bannir | Pourquoi | Remplacer par |
|---|---|---|
| « Il est possible que » | Vrai de presque tout | Un mot de l'échelle, ou rien |
| « Certains experts estiment » | Source non identifiable | Le nom de la source, ou l'affirmation disparaît |
| « Il ne fait aucun doute » | Une certitude n'a pas besoin d'être annoncée | *Nous observons* si c'est un fait ; *quasi certain* si c'est une estimation |
| « Probable à très probable » | Refus de trancher déguisé | Choisir |
| « Menace critique » | Fusionne trois axes | Probabilité + confiance + impact, séparément |
| « Nos sources indiquent » | Ni nombre, ni nature, ni indépendance | *Deux sources, dont l'indépendance est/n'est pas établie* |
| « Cela pourrait indiquer que » | Enchaîne les conditionnels sans jamais conclure | *Nous estimons [mot] que…* |
| « Une attaque sophistiquée » | Qualificatif non défini, souvent projectif | Décrire les techniques employées |
| « Selon nos analyses » | Non vérifiable | Décrire la méthode ou la source |

### 9.7 ✅ Livrable — L'échelle de calibrage de l'organisation

Document d'une page, publié en annexe de chaque produit et validé une fois.

**Section 1 — Registres**

| Registre | Formulation | Emploi |
|---|---|---|
| Fait | *Nous observons / Le journal enregistre* | Constaté, vérifiable, daté |
| Estimation | *Nous estimons [mot] que… — confiance [niveau], parce que…* | Jugement argumenté |
| Ignorance | *Nous ne disposons pas d'éléments permettant de déterminer…* | Quand c'est le cas |

**Section 2 — Échelle de probabilité** — les sept expressions du §9.3, avec fourchettes indicatives.

**Section 3 — Échelle de confiance** — les trois niveaux du §9.4, avec les quatre facteurs.

**Section 4 — Règles**
1. Toute estimation porte un mot de probabilité **et** un niveau de confiance.
2. Le niveau de confiance est **toujours expliqué en une ligne**.
3. Un seul mot par affirmation.
4. Les trois axes ne sont jamais fusionnés.
5. Toute évaluation destinée à déclencher une action comporte une clause de réfutation.

### 9.8 🔴 FIL ROUGE — octobre 2029 : mettre un mot sur « probable »

L'évaluation de septembre (§8.9) a bien fonctionné. Elle contenait pourtant deux expressions que Nour a employées sans les avoir définies : *probable* et *confiance moyenne*.

Le 3 octobre, Sonia Weber, directrice des systèmes d'information, pose une question en réunion :

> *« Quand vous écrivez "probable", vous voulez dire quoi ? Parce que moi je lis ça comme "c'est presque sûr", et j'ai décalé un projet en conséquence. »*

**Nour vérifie.** Elle voulait dire environ deux chances sur trois. Sonia avait compris neuf sur dix. L'écart n'a pas eu de conséquence — les actions décidées étaient proportionnées dans les deux lectures — mais il aurait pu.

**L'expérience que Claire propose.** Avant de rédiger une échelle, elle fait un test sur les sept destinataires réguliers : une phrase, la même pour tous, et une question — *quelle probabilité mettez-vous derrière ce mot ?*

> *« Nous estimons probable que ce prestataire ait été compromis. »*

| Destinataire | Interprétation de « probable » |
|---|---|
| Claire Nadeau (RSSI) | 65 % |
| Sonia Weber (DSI) | **90 %** |
| Malik Ferhaoui (MCS) | 70 % |
| Yann Prigent (produit) | 60 % |
| Le référent détection | 75 % |
| Karim Lebrun (DAF) | **50 %** |
| Dr Hélène Fabre | *« je ne sais pas quoi en faire »* |

**L'écart va de 50 à 90 %** sur un même mot, dans une même organisation, entre sept personnes qui travaillent ensemble depuis des années. Et la dernière réponse est la plus révélatrice : une personne à qui le mot ne dit rien du tout.

**Ce que Nour construit** : l'échelle du §9.7, une page, validée en comité le 17 octobre. Elle est désormais jointe en annexe à chaque produit — pas dans le corps, où elle alourdirait, mais en dernière page.

**L'effet observé, trois mois plus tard.** Deux changements, dont un inattendu.

*Attendu* : les destinataires calibrent mieux leurs réactions. Sonia Weber ne décale plus de projet sur un « probable ».

*Inattendu, et plus important* : **Nour écrit différemment**. Devoir choisir un mot dans une échelle fermée l'oblige à se demander où elle se situe réellement — exercice qu'elle ne faisait pas quand tous les mots étaient disponibles. Trois fois sur la période, elle a révisé sa conclusion en cherchant le bon mot : ce qu'elle allait écrire « très probable » était en réalité « probable », et cette différence l'a conduite à ajouter une vérification.

> *« Je croyais que l'échelle servait à mes lecteurs, écrit-elle. Elle me sert surtout à moi. »*

**Livrable de l'épisode.** L'échelle de calibrage d'HELIOMED, une page, annexée à tout produit. Elle figure en annexe C.

→ La suite en 🔴 §10.8, quand deux sources « indépendantes » se révéleront n'en être qu'une.

### Synthèse mentale du chapitre 9

Probabilité, confiance et gravité sont trois axes indépendants, et la faute la plus fréquente du métier consiste à les fusionner en un adjectif — « menace critique » ne dit ni si c'est probable, ni si c'est établi. La combinaison la plus utile à transmettre est celle d'une gravité élevée avec une confiance faible : elle appelle une vérification, pas une mobilisation. Les mots de probabilité sont interprétés très différemment selon les lecteurs, et « possible » signifie « non exclu », donc presque rien : le test consiste à remplacer le mot et voir si la phrase perd du sens. Une échelle fermée de sept expressions et trois niveaux de confiance, publiée en annexe de chaque produit, résout le problème — à condition que le niveau de confiance soit toujours expliqué en une ligne. Enfin, exprimer une incertitude ne dessert pas quand elle est structurée en quatre temps : ce que nous savons, ce que nous estimons, ce que nous ignorons, ce qui trancherait. La différence entre paraître subir sa question et paraître la maîtriser n'est pas le niveau de connaissance, c'est la structure.

**Trois questions de vérification**

1. Une source unique annonce une menace majeure contre votre organisation. Comment calibrez-vous, et quelle décision cela appelle-t-il ?
2. Pourquoi « nous estimons à 73 % la probabilité que » est-il moins rigoureux que « probable » ?
3. Votre direction exige une réponse par oui ou non. Construisez une réponse en trois phrases qui ne soit ni un oui, ni un non, ni une dérobade.

→ **Chapitre 10 — Évaluer une source et une information** : deux axes à ne jamais fusionner, et le mécanisme par lequel trois sources n'en font qu'une.

---

## Chapitre 10 — Évaluer une source et une information

### 10.1 Fiabilité et crédibilité : deux axes à ne jamais fusionner

C'est la distinction structurante du chapitre, et elle est l'équivalent, côté sources, des trois axes du chapitre 9.

| Axe | Porte sur | Question |
|---|---|---|
| **Fiabilité** | La **source** | Cette source s'est-elle montrée exacte par le passé ? A-t-elle un intérêt dans l'affaire ? Est-elle en position de savoir ? |
| **Crédibilité** | L'**information** | Cette affirmation précise est-elle plausible, cohérente, corroborée ? |

**Pourquoi les séparer** : une source fiable peut transmettre une information fausse — parce qu'elle a été trompée, parce qu'elle rapporte sans vérifier, parce qu'elle se trompe cette fois-ci. Et une source douteuse peut transmettre une information exacte.

**Les quatre combinaisons, avec ce qu'elles impliquent :**

| Fiabilité | Crédibilité | Situation | Traitement |
|---|---|---|---|
| Élevée | Élevée | Le cas confortable | Utilisable, en citant |
| Élevée | **Faible** | Une source sérieuse rapporte quelque chose d'invraisemblable | **Le cas le plus intéressant** : chercher pourquoi. Souvent une reprise non vérifiée |
| **Faible** | Élevée | Une source douteuse dit quelque chose de très plausible | Utilisable **si corroboré** — le danger est que la plausibilité tienne lieu de vérification |
| Faible | Faible | — | Écarter, et le tracer |

⚠️ **PIÈGE — l'auréole de la source**
Une source réputée bénéficie d'un crédit qui s'étend à tout ce qu'elle publie, y compris à ce qu'elle rapporte sans l'avoir établi. Un éditeur excellent sur l'analyse technique n'est pas nécessairement rigoureux sur l'attribution ; une agence fiable sur son propre périmètre peut relayer sans filtre ce qui vient d'ailleurs. **La fiabilité s'évalue par domaine, pas globalement.**

### 10.2 Les grilles de cotation, et leur usage réel

Il existe des grilles classiques croisant un axe de fiabilité de source, noté de A à F, et un axe de crédibilité de l'information, noté de 1 à 6. On obtient des cotations du type `B2` ou `C3`.

**Ce qu'elles apportent** : un vocabulaire commun, une discipline d'évaluation, et une trace.

**Leurs limites pratiques, qu'il faut connaître avant de les adopter :**

| Limite | Manifestation |
|---|---|
| La cotation devient mécanique | On note `B2` par habitude, sans réévaluer |
| L'échelle est trop fine | Six niveaux sur chaque axe donnent 36 combinaisons ; personne ne distingue un `C3` d'un `C4` |
| Elle masque le raisonnement | La cote remplace l'explication, alors qu'elle devrait l'accompagner |
| Elle est rarement lue | Le destinataire voit `B2` et n'en fait rien, faute de connaître l'échelle |

✅ **BONNE PRATIQUE (P1) — la version courte qui fonctionne**
Dans une organisation qui débute, une échelle à trois niveaux par axe suffit, **accompagnée d'une phrase**. Ce qui importe n'est pas la finesse de la cote, c'est que l'évaluation ait été **faite consciemment** et qu'elle soit **explicable**.

> *Source : éditeur spécialisé, fiable sur l'analyse technique, sans exposition connue sur ce sujet — fiabilité **élevée**.*
> *Information : affirmation sur le ciblage sectoriel, non détaillée, sans élément à l'appui — crédibilité **moyenne**.*

### 10.3 La chaîne de provenance

**Le principe** : pour toute affirmation importante, savoir **qui l'a dite le premier**, sur quelle base, et par combien de mains elle est passée avant d'arriver à vous.

**Pourquoi c'est le travail le plus rentable du chapitre** : chaque reprise dégrade l'information selon le mécanisme du §4.6 — perte du mode, perte des réserves, perte de la base factuelle. Après trois reprises, une hypothèse prudente est devenue un fait.

🧪 **EN PRATIQUE — remonter une chaîne en quatre questions**

```
1. Qui affirme ceci dans le document que je lis ?
2. Ce document cite-t-il une source ? Laquelle, précisément ?
3. Cette source dit-elle la même chose, avec le même mode et les mêmes réserves ?
4. Sur quoi la source d'origine fonde-t-elle son affirmation ?
```

La quatrième question est celle qui s'arrête le plus souvent sur du vide. Il est fréquent d'arriver, au bout de la chaîne, à une affirmation sans base explicite — non par malhonnêteté, mais parce que l'auteur d'origine disposait d'éléments qu'il n'a pas publiés, ou qu'il exprimait une appréciation.

**Ce qu'on écrit alors** : *« affirmation d'origine non étayée publiquement ; nous ne pouvons pas évaluer sa base »*. C'est une conclusion parfaitement recevable, et elle est infiniment plus utile que la reprise.

### 10.4 ⚠️ La circularité

Le piège le plus coûteux du métier, parce qu'il produit exactement la sensation qu'on recherche : la confirmation.

**Le mécanisme** :

```
        Une source primaire publie une évaluation prudente
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
   Éditeur A       Presse B        Chercheur C
   la reprend      la reprend      la reprend
        │               │               │
        └───────────────┼───────────────┘
                        ▼
         Vous lisez trois sources qui "concordent"
                        │
                        ▼
          Vous concluez à une forte corroboration
```

**Ce qui rend le piège efficace** : les trois reprises emploient des formulations différentes, citent parfois d'autres éléments périphériques, et arrivent à des dates différentes. Rien, en surface, ne signale qu'il s'agit d'une source unique.

**Les quatre signaux qui doivent alerter :**

| Signal | Pourquoi il compte |
|---|---|
| Les trois sources publient dans un intervalle court | Une reprise est rapide ; une observation indépendante l'est rarement |
| Aucune n'apporte d'élément factuel propre | Elles reprennent le même corpus d'exemples |
| Les tournures se ressemblent | Y compris les précautions et les chiffres |
| **Aucune ne cite les deux autres** | Elles citent toutes la même quatrième |

**Le test décisif** : *si je retirais la source X, resterait-il quelque chose ?* Si la réponse est non, vous avez une source, pas trois.

**Le cas particulier de la reprise croisée.** Il arrive que A cite B et que B cite A — chacun renforçant l'autre sans qu'aucune observation nouvelle n'existe. C'est plus rare et plus difficile à détecter, et cela suppose de lire les notes de bas de page.

🎯 **ET MAINTENANT ?**
*Trois publications de trois éditeurs différents, parues en dix jours, affirment qu'un acteur cible votre secteur. Que faites-vous avant d'y croire ?*
**Réponse** : vous ouvrez les trois et vous cherchez les références. Quinze minutes. Trois issues possibles : elles citent toutes la même source antérieure — vous avez **une** source, et vous l'écrivez ; chacune apporte des victimes ou des observations distinctes — vous avez une vraie corroboration, et votre confiance monte ; aucune ne cite quoi que ce soit — vous avez **zéro** source évaluable, ce qui est la situation la plus fréquente et la moins reconnue.

### 10.5 Les sources intéressées

Toute source a un intérêt. Le savoir ne disqualifie personne — l'ignorer fausse l'évaluation.

| Type de source | Intérêt structurel | Ce que cela produit | Ce qu'elle apporte malgré tout |
|---|---|---|---|
| **Éditeur de sécurité** | Vendre un produit ou un service | Une menace décrite comme plus large, plus sophistiquée ou plus nouvelle qu'elle ne l'est | La meilleure analyse technique disponible, souvent |
| **Autorité publique** | Alerter, mais aussi protéger ses sources et ses relations | Des informations solides mais partielles, des attributions prudentes ou absentes | Une fiabilité élevée sur ce qu'elle affirme |
| **Victime** | Préserver sa réputation, limiter sa responsabilité | Une minimisation, ou l'insistance sur la sophistication de l'attaque | Le seul témoignage direct |
| **Chercheur indépendant** | Reconnaissance, publication | Parfois une survalorisation d'une découverte mineure | Une profondeur technique rare |
| **Presse** | Audience | Amplification, raccourcis, pertes de nuance | Une alerte rapide |
| **Fournisseur de renseignement** | Justifier son abonnement | Un volume et une couverture mis en avant | Un accès à des sources non publiques |

**Le cas de la victime mérite une remarque** : l'insistance sur la sophistication de l'attaque est un mécanisme bien identifié — une attaque sophistiquée est moins imputable à une négligence. Cela ne signifie pas que le témoignage soit faux ; cela signifie que l'adjectif « sophistiquée » doit être traité comme une appréciation intéressée, et remplacé par une description des techniques employées.

📌 **Ce qu'il ne faut pas en conclure.** L'existence d'un intérêt ne justifie pas le cynisme. Un éditeur qui vend une solution produit régulièrement l'analyse technique la plus rigoureuse du marché sur un sujet donné. La bonne posture n'est pas la défiance mais **la lecture différenciée** : on retient l'analyse technique, on interroge l'évaluation de portée.

### 10.6 Évaluer une publication commerciale

Sept questions, dans l'ordre. Elles prennent dix minutes et évitent l'essentiel des erreurs.

| # | Question | Ce qu'elle révèle |
|---|---|---|
| 1 | **La méthodologie est-elle décrite ?** | Une publication qui ne dit pas comment elle a obtenu ses données ne peut pas être évaluée |
| 2 | **Les faits sont-ils distingués des évaluations ?** | Le §4.1, appliqué à autrui |
| 3 | **Des niveaux de confiance sont-ils exprimés ?** | Signe de maturité analytique |
| 4 | **Les chiffres ont-ils un dénominateur ?** | « 300 % d'augmentation » sur quelle base, quel périmètre, quelle méthode de comptage ? |
| 5 | **Le périmètre d'observation est-il déclaré ?** | Un éditeur observe **sa** télémétrie : ses clients, ses secteurs, ses géographies |
| 6 | **Y a-t-il une conclusion commerciale ?** | Sa présence ne disqualifie pas ; son absence de séparation, si |
| 7 | **La publication dit-elle ce qu'elle ne sait pas ?** | Le meilleur indicateur de fiabilité, et le plus rare |

⚠️ **PIÈGE — le biais de télémétrie**
Un éditeur constate ce que ses capteurs voient, chez ses clients. Si sa clientèle est majoritairement composée de grandes organisations d'un secteur donné, ses statistiques décriront ce secteur — et pas la menace en général. Ce biais n'est pas une malhonnêteté : c'est une propriété structurelle de toute observation. Ce qui est fautif, c'est de ne pas déclarer son périmètre.

### 10.7 ⏱ Évaluer une affirmation sur une menace nouvelle

*Bloc daté. Vérifié le 2 août 2026.*

Le cas particulier des menaces émergentes mérite un traitement à part, parce que c'est là que l'écart entre la couverture et les faits établis est le plus grand.

**Le mécanisme observé** : une capacité nouvelle apparaît · un premier cas documenté est publié · la couverture s'emballe · des affirmations générales circulent — « les attaquants utilisent désormais X » — sans que le nombre de cas documentés ait augmenté.

**Les quatre questions à poser à toute affirmation sur une menace nouvelle** :

| # | Question | Ce qu'elle établit |
|---|---|---|
| 1 | **Combien de cas documentés ?** | Un cas n'est pas une tendance |
| 2 | **Documentés par qui, et avec quel accès ?** | Une observation directe ou une reprise ? |
| 3 | **Qu'est-ce qui change réellement dans le mode opératoire ?** | Une capacité nouvelle, ou une automatisation de ce qui existait ? |
| 4 | **Qu'est-ce que cela change pour ma défense ?** | Souvent : rien de nouveau |

**La quatrième est la plus importante et la moins posée.** Une nouveauté qui ne modifie ni le vecteur d'entrée, ni les techniques employées, ni les mesures de défense pertinentes est un sujet d'analyse intéressant et une non-information opérationnelle.

⏱ **Illustration au 2 août 2026.** Des entrées documentant l'emploi de modèles de langage par des attaquants ont été intégrées aux référentiels publics de modes opératoires — décrivant à la fois des opérations largement automatisées et un maliciel interrogeant un modèle en cours d'exécution. 📎 [S-02]

> **Note de transparence.** L'un de ces cas documentés concerne un usage détourné de Claude, l'assistant développé par Anthropic — l'organisation qui m'a créé. Je le mentionne pour que vous puissiez en tenir compte dans votre lecture. Ce cours traite ce cas exactement comme les autres, à partir des sources publiques.

**Appliquons les quatre questions à ce sujet**, à titre d'exercice :

| Question | Réponse au 2 août 2026 |
|---|---|
| Combien de cas documentés ? | **Un petit nombre**, individuellement documentés |
| Par qui ? | Par les fournisseurs des modèles concernés, avec un accès direct à leur télémétrie — donc une observation de première main, sur **leur** périmètre |
| Qu'est-ce qui change dans le mode opératoire ? | Principalement une **automatisation et une accélération** d'étapes existantes ; les techniques d'intrusion documentées restent celles des référentiels |
| Qu'est-ce que cela change pour ma défense ? | **Peu de choses à ce stade** : les vecteurs d'entrée et les mesures pertinentes sont inchangés. L'effet principal est une possible réduction des délais |

**La conclusion analytique honnête** ressemble donc à ceci :

> *Nous estimons **probable** que l'emploi de modèles de langage réduise les délais entre la découverte d'une vulnérabilité et son exploitation à grande échelle — **confiance faible**, le nombre de cas documentés étant restreint et l'observation provenant d'un petit nombre d'acteurs disposant d'un accès privilégié à leur propre télémétrie.*
>
> *Nous n'identifions à ce stade aucune modification des mesures de défense pertinentes. Le sujet appelle une surveillance, pas une réorientation.*

**Ce que cet exemple enseigne**, au-delà de son objet : une menace peut être réelle, correctement documentée, et **sans conséquence opérationnelle immédiate**. Savoir écrire cela est une compétence — et c'est l'inverse de ce que produit la pression médiatique.

### 10.8 ✅ Livrable — Fiche d'évaluation de source

| Champ | Contenu |
|---|---|
| Identification de la source | Nom, type, date de publication |
| **Position pour savoir** | La source est-elle en mesure d'observer ce qu'elle rapporte ? |
| **Intérêt identifié** | Commercial, réputationnel, institutionnel, aucun apparent |
| **Fiabilité** | Élevée / moyenne / faible — **et pourquoi, en une ligne** |
| Historique | Cette source s'est-elle montrée exacte par le passé, sur ce domaine ? |
| **Chaîne de provenance** | Source primaire ou reprise ? Si reprise : de qui, en combien de mains ? |
| **Indépendance** | Cette source est-elle indépendante des autres dont je dispose ? |
| Méthodologie déclarée | Oui / non / partielle |
| Périmètre d'observation déclaré | Oui / non |
| **Crédibilité de l'information** | Élevée / moyenne / faible — **et pourquoi** |
| Éléments propres apportés | Ce que cette source ajoute et qu'aucune autre n'apporte |
| Décision | Utilisable / utilisable si corroboré / à écarter — avec motif |

**La ligne « éléments propres » est le test final.** Une source qui n'apporte aucun élément que vous n'ayez déjà n'augmente pas votre confiance, quelle que soit sa réputation.

### 10.9 🔬 Mini-lab 4 — Trois sources, ou une seule ?

**Objectif** — Reconstituer une chaîne de provenance et détecter une circularité.
**Durée** 35 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §10.3, §10.4, §4.6 · **Livrable** chaîne de provenance + évaluation de confiance révisée
**Compétences validées** — ✔ remonter une chaîne de provenance ✔ détecter une circularité ✔ distinguer corroboration réelle et apparente ✔ requalifier une confiance ✔ écrire une évaluation sur source unique

**Le dossier fourni** — quatre extraits, dans l'ordre où ils vous parviennent.

> **Extrait 1 — Publication d'un éditeur de sécurité, 12 janvier**
> *« Notre équipe évalue avec une confiance modérée que le groupe désigné TEMPEST-14 a étendu son ciblage au secteur des équipements médicaux. Cette évaluation repose sur l'observation, chez un client, d'une infrastructure présentant des similarités avec celle décrite dans notre rapport de septembre. Nous n'avons pas identifié de victime confirmée dans ce secteur. »*

> **Extrait 2 — Article de presse spécialisée, 15 janvier**
> *« Le groupe TEMPEST-14 cible désormais le secteur des équipements médicaux, selon une analyse publiée cette semaine par un éditeur de sécurité. Cette extension du périmètre de ciblage inquiète les acteurs du secteur. »*

> **Extrait 3 — Bulletin d'un dispositif de partage sectoriel, 19 janvier**
> *« Plusieurs sources publiques font état d'un ciblage du secteur des équipements médicaux par le groupe TEMPEST-14. Les membres sont invités à renforcer leur vigilance. »*

> **Extrait 4 — Note d'un cabinet de conseil, 26 janvier**
> *« Il est établi que TEMPEST-14 mène une campagne contre les fabricants d'équipements médicaux. Les organisations du secteur doivent considérer qu'elles figurent parmi les cibles potentielles. »*

**Questions**
(a) Reconstituez la chaîne de provenance.
(b) Combien de sources indépendantes ?
(c) Que devient l'affirmation à chaque étape ?
(d) Quel niveau de confiance retenez-vous ?
(e) Rédigez l'évaluation à destination de votre RSSI.

---

**Corrigé commenté**

**(a) La chaîne**

```
Extrait 1 (12 janv.) — ÉDITEUR — source primaire
   │  Base : une observation chez un client. Aucune victime confirmée.
   │  Mode : "évalue avec une confiance modérée"
   ▼
Extrait 2 (15 janv.) — PRESSE — reprise, cite l'éditeur
   │  Mode perdu : "cible désormais" (affirmation)
   │  Réserve perdue : la mention "aucune victime confirmée" disparaît
   │  Ajout non factuel : "inquiète les acteurs du secteur"
   ▼
Extrait 3 (19 janv.) — DISPOSITIF SECTORIEL — reprise, ne cite personne
   │  "Plusieurs sources publiques" : formulation qui masque une source unique
   ▼
Extrait 4 (26 janv.) — CABINET — reprise, ne cite personne
      "Il est établi que" : le maximum de certitude, sur la base la plus faible
```

**(b) Une seule source indépendante** : l'éditeur. Les trois autres sont des reprises successives, dont deux ne citent personne.

**Le signal le plus fort** est l'extrait 3 : *« plusieurs sources publiques »*. C'est une formulation qui décrit un nombre de **publications**, pas un nombre d'**observations**. Elle est fréquente, et elle est le principal vecteur de circularité dans les dispositifs de partage — non par malhonnêteté, mais parce que celui qui rédige a effectivement lu plusieurs textes.

**(c) La dégradation, en quatre étapes**

| Extrait | Statut de l'affirmation | Ce qui a été perdu |
|---|---|---|
| 1 | Évaluation, confiance modérée, base déclarée, réserve explicite | — |
| 2 | Affirmation | Le mode · la réserve « aucune victime confirmée » |
| 3 | Affirmation, avec pluralisation des sources | La source unique · toute base factuelle |
| 4 | **Fait établi** | Tout. « Il est établi » sur une observation d'infrastructure similaire chez un client |

C'est le §4.6 en action, sur quatorze jours.

**(d) Le niveau de confiance**

**Faible.** Justification, en une ligne comme le veut le §9.4 : *source unique, évaluation d'origine elle-même modérée, aucune victime confirmée dans le secteur, base factuelle limitée à une similarité d'infrastructure.*

⚠️ **L'erreur à ne pas commettre** : conclure que l'information est fausse. Rien ne permet de le dire. L'éditeur a peut-être raison. Ce que l'exercice établit, ce n'est pas la fausseté de l'affirmation — c'est que **le nombre de publications ne dit rien de sa solidité**.

**(e) L'évaluation attendue**

> *Quatre publications font état d'un ciblage du secteur des équipements médicaux par un acteur désigné TEMPEST-14. **Nous n'identifions qu'une seule source primaire** : l'évaluation d'un éditeur du 12 janvier, elle-même donnée avec une confiance modérée, fondée sur une similarité d'infrastructure observée chez un client, et précisant qu'aucune victime du secteur n'a été confirmée. Les trois autres publications en dérivent.*
>
> *Nous estimons **aussi probable qu'improbable** que ce ciblage soit avéré — **confiance faible**, pour les raisons ci-dessus.*
>
> *Nous ne recommandons pas de mobilisation. Nous recommandons deux vérifications : demander à l'éditeur si des victimes ont été confirmées depuis le 12 janvier · interroger le dispositif sectoriel sur l'existence d'observations propres à ses membres.*
>
> *Cette évaluation serait révisée à la hausse si une victime du secteur était confirmée par une source disposant d'une observation directe.*

**Les trois erreurs attendues**

1. **Compter quatre sources.** C'est l'objet du lab, et c'est ce que fait la majorité des lecteurs en première lecture.
2. **Conclure que l'information est fausse.** L'exercice porte sur la solidité de la base, pas sur la véracité.
3. **Ne pas remarquer la perte de la réserve.** La disparition, entre les extraits 1 et 2, de la mention *« nous n'avons pas identifié de victime confirmée »* est la transformation la plus lourde de conséquence — et c'est une suppression, pas une déformation, donc elle est invisible sans comparaison.

### 10.10 🔴 FIL ROUGE — novembre 2029 : deux sources qui n'en font qu'une

Nour prépare une évaluation pour le comité de sécurité du 21 novembre. Le sujet : une technique d'accès initial signalée comme employée contre des organisations de santé européennes.

Elle dispose de trois publications. Elle applique la procédure du §10.3 — désormais systématique depuis l'épisode de juin (§4.9).

| Publication | Date | Ce qu'elle cite | Éléments propres |
|---|---|---|---|
| Éditeur A | 4 nov. | Rien | **Trois victimes, avec dates et pays** |
| Éditeur B | 9 nov. | « des observations récentes » | Aucun |
| Chercheur C | 12 nov. | Éditeur A, explicitement | **Une analyse technique du mécanisme** |

**Le cas de l'éditeur B** est le plus instructif. Il ne cite personne, emploie une formulation vague, et n'apporte aucune victime, aucune date, aucun élément technique. Nour lui écrit — deux lignes, une question : *votre publication du 9 novembre repose-t-elle sur des observations propres ?*

**La réponse, reçue en trois jours** : non. Elle repose sur la publication de l'éditeur A, qui n'est pas citée parce que « l'usage ne l'impose pas dans ce format ».

**Le résultat de l'évaluation** :

| | Avant vérification | Après |
|---|---|---|
| Sources apparentes | 3 | 3 |
| **Sources indépendantes** | 3 | **2** |
| Éléments factuels distincts | ? | 3 victimes (A) + 1 analyse technique (C) |
| Confiance retenue | *aurait été* élevée | **moyenne** |

**Ce qui change concrètement.** L'éditeur C est une corroboration réelle — il apporte une analyse technique indépendante du mécanisme, qu'il a produite lui-même. L'éditeur B n'ajoute rien. La confiance passe d'élevée à moyenne, et l'évaluation le dit explicitement.

**La question posée en comité par Claire** : *« si tu n'avais pas écrit à l'éditeur B, qu'aurais-tu conclu ? »*

Réponse de Nour : confiance élevée, sur trois sources. Coût de la vérification : deux lignes de courriel et trois jours d'attente.

**La décision prise.** Une règle est ajoutée au processus : **toute source qui n'apporte aucun élément factuel propre est traitée comme une reprise jusqu'à preuve du contraire**, et cette qualification figure dans l'évaluation. Si l'origine peut être vérifiée à peu de frais, on vérifie ; sinon, on écrit le doute.

**L'effet secondaire, observé sur six mois.** Nour prend l'habitude d'écrire aux éditeurs. Sur onze demandes, elle obtient neuf réponses. Deux d'entre elles conduisent à des échanges réguliers, et l'un des éditeurs finit par lui transmettre des éléments avant publication. **La vérification de source est devenue une source.**

> *« Je pensais que vérifier m'isolerait, écrit-elle. En pratique, c'est ce qui m'a fait connaître. »*

**Livrable de l'épisode.** La fiche d'évaluation de source du §10.8, intégrée au processus, avec la règle de la reprise présumée.

→ La suite en 🔴 §11.7, quand une évaluation devra dire ce qui l'invaliderait — et que cette ligne changera la décision.

### Synthèse mentale du chapitre 10

Fiabilité et crédibilité sont deux axes distincts : une source fiable peut transmettre une information fausse, et la fiabilité s'évalue par domaine, jamais globalement. Les grilles de cotation apportent un vocabulaire commun mais deviennent mécaniques ; ce qui compte n'est pas la finesse de la cote mais que l'évaluation ait été faite consciemment et soit explicable en une phrase. Remonter une chaîne de provenance est le travail le plus rentable du chapitre, et la question qui s'arrête le plus souvent sur du vide est la quatrième : sur quoi la source d'origine fonde-t-elle son affirmation ? La circularité produit exactement la sensation qu'on recherche — la confirmation — et le test décisif tient en une question : si je retirais cette source, resterait-il quelque chose ? Toute source a un intérêt, ce qui n'autorise pas le cynisme mais impose une lecture différenciée : retenir l'analyse technique, interroger l'évaluation de portée. Enfin, une menace peut être réelle, correctement documentée, et sans conséquence opérationnelle immédiate — savoir l'écrire est une compétence.

**Trois questions de vérification**

1. Un bulletin sectoriel affirme que « plusieurs sources publiques font état de… ». Pourquoi cette formulation doit-elle déclencher une vérification, et laquelle ?
2. Un éditeur publie des statistiques montrant une hausse de 300 % d'un type d'attaque. Quelles deux questions posez-vous avant d'utiliser ce chiffre ?
3. Une source réputée affirme quelque chose d'invraisemblable. Est-ce le cas le plus embarrassant ou le plus intéressant, et pourquoi ?

→ **Chapitre 11 — Produire un jugement analytique** : construire une évaluation qui s'engage, se conteste et se révise.

---

## Chapitre 11 — Produire un jugement analytique

### 11.1 Décrire et évaluer

Le chapitre 6 a posé l'axiome : une analyse est une hypothèse argumentée, pas une description. Voici comment on en fabrique une.

**La différence, en une comparaison :**

| Description | Évaluation |
|---|---|
| *« Trois publications font état d'un ciblage sectoriel. Une victime a été confirmée. L'infrastructure employée présente des similarités avec une campagne antérieure. »* | *« Nous estimons probable que ces incidents relèvent d'une campagne unique — confiance moyenne, fondée sur la réutilisation d'infrastructure et sur la concentration temporelle, affaiblie par l'absence de vecteur commun identifié. »* |
| Tout est vrai | Tout est vrai **et** quelqu'un s'est engagé |
| Le lecteur doit conclure | Le lecteur peut décider ou contester |

**Ce qui fait la différence n'est pas la quantité d'information.** C'est la présence de quatre éléments que la description ne contient pas : un verbe d'estimation, un mot de probabilité, un niveau de confiance, et une justification de ce niveau.

⚠️ **PIÈGE — la prudence qui n'en est pas une**
Refuser de conclure passe pour de la rigueur. C'en est parfois. Mais le plus souvent, c'est un transfert : l'analyste renvoie au destinataire un travail qu'il aurait dû faire, en se protégeant de l'erreur. Le destinataire, lui, conclura quand même — avec moins d'éléments et moins de méthode.

### 11.2 Construire une évaluation

Cinq blocs, dans cet ordre. C'est le modèle qui figure en annexe D.

```
① LA QUESTION        À quoi répond ce document, et qui l'a posée
② LES FAITS          Ce que nous observons, avec sources et dates
③ LE RAISONNEMENT    Les hypothèses envisagées, ce qui les départage
④ LA CONCLUSION      L'estimation, calibrée, avec la suivante
⑤ LA RÉFUTATION      Ce qui l'invaliderait, et ce qui trancherait
```

**Ce que chaque bloc doit contenir**, et l'erreur qui lui correspond :

| Bloc | Contenu | Erreur fréquente |
|---|---|---|
| ① Question | Une question, formulée comme telle | Un sujet — « la campagne TEMPEST-14 » — qui n'appelle aucune réponse |
| ② Faits | Uniquement des observations, avec source et date | Des verbes d'intention (§4.1) |
| ③ Raisonnement | Les hypothèses concurrentes, et ce qui les discrimine | Une liste d'éléments « à l'appui » (§7.2) |
| ④ Conclusion | Estimation + probabilité + confiance + justification | Une affirmation nue |
| ⑤ Réfutation | Ce qui la renverserait, ce qui trancherait | **Absente huit fois sur dix** |

**Le bloc ⑤ est le marqueur de maturité.** Un produit qui ne dit pas ce qui l'invaliderait ne peut pas être révisé — il ne peut qu'être cru ou rejeté. Le §11.3 lui est consacré.

### 11.3 Ce qui invaliderait votre analyse

**La section que personne n'écrit**, et qui distingue une analyse d'une opinion.

**Ce qu'elle est** : la liste explicite des observations qui, si elles se produisaient, vous conduiraient à changer de conclusion.

**Ce qu'elle n'est pas** : une précaution rhétorique. *« Cette évaluation pourrait évoluer en fonction de nouveaux éléments »* ne dit rien — c'est vrai de toute évaluation.

🧪 **EN PRATIQUE — construire une clause de réfutation**

Trois questions, et une ligne par réponse :

```
1. Quelle observation rendrait mon hypothèse retenue improbable ?
2. Quelle observation rendrait l'hypothèse suivante plus probable que la mienne ?
3. Quel présupposé, s'il était faux, effondrerait le raisonnement ?
```

**Exemple, sur le cas du prestataire (§8.9)** :

> *Cette évaluation serait invalidée si :*
> *— un vecteur d'entrée commun aux trois victimes, indépendant du prestataire, était identifié ;*
> *— le prestataire démontrait l'absence de compromission de son infrastructure d'administration ;*
> *— une quatrième victime, non cliente du prestataire, était constatée.*

**Ce que cette section produit concrètement**, et ce sont trois effets distincts :

| Effet | Mécanisme |
|---|---|
| **Elle oriente la collecte** | Chaque ligne est une question à poser (§14.4) |
| **Elle protège l'analyste** | Le jour où l'alternative se vérifie, il l'avait envisagée et dit pourquoi il l'écartait |
| **Elle discipline le raisonnement** | Une hypothèse qu'on ne sait pas réfuter n'est pas une hypothèse forte : elle est irréfutable, donc vide (§6.3) |

**Le troisième effet est le plus important**, et il agit **pendant** la rédaction : chercher ce qui invaliderait sa propre conclusion oblige à l'examiner. C'est le même mécanisme que l'échelle de calibrage du §9.8 — l'outil sert d'abord à celui qui l'emploie.

### 11.4 Les indicateurs de changement

**Le principe** : à côté de ce qui invaliderait l'analyse, on précise ce qui la **ferait évoluer**, sans nécessairement la renverser.

| | Réfutation | Indicateur de changement |
|---|---|---|
| Effet | La conclusion tombe | La conclusion se déplace |
| Exemple | « Une quatrième victime hors clientèle du prestataire » | « Une revendication publique » — cela ne change pas l'origine, cela change la nature de la menace |
| Ce qu'on en fait | On réécrit | On révise la confiance ou la portée |

**La grille de signaux du §8.4 alimente directement cette section.** Et sa vertu opérationnelle est double : elle permet de **conclure en attendant**, et elle constitue une liste de requêtes exploitables par la détection (chapitre 30).

### 11.5 Distinguer évaluation et recommandation

**Deux registres distincts, deux responsabilités distinctes.**

| | **Évaluation** | **Recommandation** |
|---|---|---|
| Répond à | *Qu'est-ce qui se passe ?* | *Que faut-il faire ?* |
| Relève de | L'analyste | **Le décideur** — l'analyste peut proposer |
| Dépend de | Les faits et le raisonnement | L'évaluation **plus** le contexte, les moyens, les priorités |
| Peut être juste alors que l'autre est fausse | Oui, dans les deux sens | Oui |

**Pourquoi les séparer physiquement dans le document** : parce qu'un désaccord sur la recommandation ne doit pas contaminer l'évaluation. Un RSSI peut accepter votre analyse et refuser votre recommandation — pour des raisons de moyens ou de calendrier qui ne vous concernent pas. Si les deux sont mêlées, le refus de l'une emporte le rejet de l'autre.

⚠️ **PIÈGE — la recommandation déguisée en évaluation**
*« La menace est critique et impose un renforcement immédiat de la surveillance »* mélange les deux. La première partie est une évaluation mal calibrée, la seconde une recommandation présentée comme une conséquence nécessaire. Le destinataire n'a plus d'espace de décision — et c'est exactement ce qu'il faut lui laisser.

✅ **BONNE PRATIQUE (P0)** — Deux sections séparées, avec un titre chacune. Et dans la recommandation, indiquez **le coût estimé** : une recommandation sans ordre de grandeur de coût est une recommandation que le décideur ne peut pas arbitrer.

### 11.6 ⚠️ L'analyse qui n'engage à rien

Quatre formes, toutes fréquentes, toutes reconnaissables.

| Forme | Exemple | Ce qui manque |
|---|---|---|
| **Le conditionnel en cascade** | « Cela pourrait indiquer que l'acteur chercherait à… » | Toute prise de position |
| **L'inventaire d'hypothèses sans hiérarchie** | « Plusieurs explications sont envisageables : A, B, C. » | Laquelle vous retenez, et pourquoi |
| **La conclusion tautologique** | « La vigilance reste de mise. » | Une information |
| **L'évaluation sans calibrage** | « Le risque est significatif. » | Probabilité, confiance, et une définition de « significatif » |

**Le test qui les détecte tous** : *si je supprimais cette phrase, le lecteur perdrait-il quelque chose ?* Appliqué à une conclusion, il élimine l'essentiel du remplissage.

🎯 **ET MAINTENANT ?**
*Vous relisez votre évaluation et la conclusion dit : « la situation appelle une surveillance accrue et une vigilance particulière sur les accès distants ». Que faites-vous ?*
**Réponse** : vous la réécrivez, parce qu'elle ne contient ni évaluation ni recommandation exploitable. La version utilisable sépare les deux : *« Nous estimons probable que les accès distants constituent le vecteur privilégié de cette campagne — confiance moyenne, fondée sur deux victimes documentées. Nous recommandons trois actions : recherche rétrospective sur 90 jours des authentifications depuis des origines inhabituelles (2 jours-homme) · vérification de l'activation de l'authentification multifacteur sur les 4 comptes de service concernés (2 heures) · règle d'alerte sur les authentifications hors plage horaire (1 jour). »* La différence n'est pas la longueur : c'est qu'on peut décider.

### 11.7 ✅ Livrable — Structure d'une évaluation

| Section | Contenu | Longueur |
|---|---|---|
| **En-tête** | Question · demandeur · date · **date de réexamen** · analyste · relecteur | 3 lignes |
| **Réponse en une phrase** | La conclusion, calibrée | 1 phrase |
| **Ce que nous observons** | Faits uniquement, avec source et date | ½ page |
| **Ce que nous en estimons** | Hypothèses envisagées · ce qui les départage · conclusion calibrée · hypothèse suivante | ½ à 1 page |
| **Ce qui invaliderait cette analyse** | 2 à 4 lignes, opérationnelles | 4 lignes |
| **Ce qui trancherait** | Les questions à poser, les données à obtenir | 3 lignes |
| **Ce que nous recommandons** | **Section séparée**, avec coût estimé par action | ½ page |
| **Ce que nous ne savons pas** | Les lacunes, et leur effet sur la conclusion | 3 lignes |
| Annexe | L'échelle de calibrage (§9.7) | 1 page |

**La « réponse en une phrase » en tête est ce qui fait lire le reste.** Elle applique le principe du chapitre 25 : conclusion d'abord, preuve ensuite.

### 11.8 🔴 FIL ROUGE — décembre 2029 : la ligne qui change la décision

Le 6 décembre, Yann Prigent, responsable produit, sollicite Nour. Un client hospitalier a signalé un comportement anormal de la passerelle HelioBox installée chez lui : redémarrages inexpliqués, deux fois en trois semaines.

**L'enjeu est important.** Si HelioBox est compromise chez un client, l'obligation de signalement réglementaire s'applique, avec des délais courts. Yann veut savoir s'il doit déclencher la procédure.

Nour dispose de peu d'éléments : les journaux du client sur 30 jours, la version installée, et le fait que deux autres clients sur les quarante-trois équipés ont signalé des redémarrages au cours du trimestre.

**Son évaluation, structurée selon le §11.7** :

> **Réponse en une phrase.** *Nous estimons peu probable que ces redémarrages résultent d'une compromission — confiance moyenne.*
>
> **Ce que nous observons.** Deux redémarrages non planifiés en trois semaines chez un client · trois clients sur quarante-trois ayant signalé des redémarrages ce trimestre · aucun élément anormal dans les journaux disponibles · la version installée correspond à la version courante · aucun signalement de vulnérabilité affectant ce produit.
>
> **Ce que nous en estimons.** Trois hypothèses ont été envisagées. *Compromission* : aucun élément à l'appui, mais les journaux ne couvrent que 30 jours et ne tracent pas les modifications de configuration. *Défaut logiciel* : compatible avec la répartition sur trois clients distincts, et avec l'absence d'élément dans les journaux. *Cause environnementale locale* — alimentation, réseau, température : compatible chez un client, moins probable sur trois sites différents. Nous retenons le défaut logiciel, **peu probable** pour la compromission, **confiance moyenne**.
>
> **Ce qui invaliderait cette analyse.** *— Un quatrième client signalant des redémarrages avec un profil d'usage différent · une modification de configuration non expliquée sur l'un des équipements · **la découverte que les trois clients concernés partagent une caractéristique que nous n'avons pas identifiée**.*
>
> **Ce qui trancherait.** L'extraction des journaux de configuration des trois équipements, si le produit les conserve · la comparaison des versions de micrologiciel exactes.
>
> **Ce que nous ne savons pas.** Nos journaux clients ne tracent pas les modifications de configuration. Cette lacune est structurelle et concerne les quarante-trois équipements : nous ne pourrions pas détecter une compromission silencieuse.

**Ce qui se passe.** Yann lit la troisième ligne de la clause de réfutation — *une caractéristique commune que nous n'avons pas identifiée* — et fait une vérification que personne n'avait demandée : les trois clients concernés utilisent-ils quelque chose en commun ?

**Réponse en une demi-journée** : oui. Les trois sont les seuls, sur quarante-trois, à avoir souscrit une option de synchronisation avec un système d'information hospitalier tiers — activée chez eux, inactive chez les quarante autres.

**La conclusion révisée**, le 11 décembre :

> *Nous estimons très probable que ces redémarrages soient liés au module de synchronisation optionnel — confiance élevée, fondée sur la correspondance exacte entre les trois clients concernés et les trois seuls clients ayant activé cette option.*

Le développement identifie une semaine plus tard une fuite de mémoire dans ce module, corrigée en janvier. Aucune compromission, aucune obligation de signalement.

**Ce que Claire souligne au comité** : la clause de réfutation n'a pas servi à protéger l'analyste. **Elle a produit la bonne réponse.** La troisième ligne n'était pas une précaution rhétorique : c'était une question ouverte, écrite parce que le modèle l'exigeait, et quelqu'un est allé y répondre.

**L'autre effet, moins visible et plus durable.** La section *« ce que nous ne savons pas »* a signalé une lacune structurelle : les équipements ne tracent pas les modifications de configuration. Personne ne l'avait formulé jusque-là. Cette phrase devient une exigence de conception pour la version suivante d'HelioBox — et elle est portée par le responsable produit, pas par la sécurité.

> *« Une évaluation utile ne répond pas seulement à la question posée, écrit Nour. Elle montre où on ne voit rien. »*

**Livrable de l'épisode.** Le modèle d'évaluation en neuf sections, adopté comme standard — annexe D.

→ La suite en 🔴 §12.6, quand une seconde paire d'yeux verra ce qu'un analyste seul ne pouvait pas voir.

### Synthèse mentale du chapitre 11

Une évaluation se distingue d'une description par quatre éléments : un verbe d'estimation, un mot de probabilité, un niveau de confiance et sa justification — refuser de conclure n'est pas de la rigueur mais un transfert de travail vers le destinataire, qui conclura de toute façon avec moins de méthode. Cinq blocs la structurent, et le cinquième — ce qui l'invaliderait — est le marqueur de maturité : absent huit fois sur dix, il oriente la collecte, protège l'analyste et discipline le raisonnement pendant la rédaction. Évaluation et recommandation relèvent de deux responsabilités distinctes et se séparent physiquement, faute de quoi un désaccord sur l'une emporte le rejet de l'autre. Quatre formes d'analyse n'engagent à rien — le conditionnel en cascade, l'inventaire sans hiérarchie, la conclusion tautologique, l'évaluation non calibrée — et un test les détecte toutes : si je supprimais cette phrase, le lecteur perdrait-il quelque chose ? Enfin, une évaluation utile ne répond pas seulement à la question posée : elle montre où l'on ne voit rien.

**Trois questions de vérification**

1. Pourquoi « cette évaluation pourrait évoluer en fonction de nouveaux éléments » n'est-elle pas une clause de réfutation ?
2. Votre destinataire accepte votre analyse et rejette votre recommandation. Est-ce un échec ? Qu'est-ce que cela indique sur la structure de votre document ?
3. Construisez une clause de réfutation en trois lignes pour une évaluation concluant à une campagne opportuniste plutôt qu'à un ciblage.

→ **Chapitre 12 — Analyser à plusieurs** : pourquoi l'analyse solitaire dérive, et ce qu'on peut faire quand on est seul.

---

## Chapitre 12 — Analyser à plusieurs

### 12.1 Pourquoi l'analyse solitaire dérive

Le chapitre 7 a posé le constat décisif : **on ne détecte pas ses propres biais**. On détecte ceux des autres, immédiatement et sans effort. C'est une asymétrie robuste, et elle a une conséquence directe : un analyste seul ne peut pas se relire utilement sur le fond.

**Les quatre dérives spécifiques du travail solitaire :**

| Dérive | Mécanisme |
|---|---|
| **La cohérence interne prise pour de la justesse** | À force de travailler un dossier, l'explication retenue devient évidente. Sa cohérence est confondue avec sa probabilité |
| **L'implicite non formulé** | Ce qui est évident pour l'analyste n'est pas écrit, donc pas questionné |
| **L'absence de contradiction** | Aucune hypothèse alternative ne survit longtemps quand personne ne la défend |
| **L'accumulation de présupposés** | Chaque dossier hérite des conclusions du précédent, sans réexamen |

**La quatrième est la plus insidieuse** : elle produit, au bout de quelques mois, une vision du monde cohérente et progressivement décalée du réel. Rien dans le travail quotidien ne la corrige.

⚠️ Ce chapitre ne suppose pas une équipe. Le §12.5 traite le cas — majoritaire — de l'analyste seul, et les substituts qui fonctionnent réellement.

### 12.2 La revue par les pairs

**Ce que c'est** : une relecture par une seconde personne, avec une consigne précise, avant diffusion.

**Ce que ce n'est pas** : une validation hiérarchique. Le relecteur ne dit pas si l'analyse est bonne — il dit ce qui n'est pas défendable en l'état.

**Ce qu'on relit, et dans quel ordre** :

| # | Point | Question posée au texte | Temps |
|---|---|---|---|
| 1 | **Séparation faits / estimations** | Y a-t-il des verbes d'intention en section factuelle ? | 2 min |
| 2 | **Hypothèses alternatives** | Sont-elles présentes, et discriminées ? | 2 min |
| 3 | **Calibrage** | Chaque estimation porte-t-elle probabilité **et** confiance justifiée ? | 2 min |
| 4 | **Sources** | Provenance tracée ? Indépendance vérifiée ? | 3 min |
| 5 | **Réfutation** | La clause est-elle présente et opérationnelle ? | 1 min |
| 6 | **Utilité** | Le destinataire saura-t-il quoi faire ? | 2 min |

**Douze minutes.** C'est le budget réel d'une relecture efficace, et c'est ce qui la rend praticable.

✅ **BONNE PRATIQUE (P0) — le relecteur n'a pas besoin d'être analyste**
C'est le point qui rend le dispositif accessible à toutes les organisations. Les six vérifications ci-dessus sont **formelles** : elles portent sur la structure du raisonnement, pas sur le fond du sujet. Un administrateur système, un juriste ou un chef de projet peut les conduire avec la grille en main — et son extériorité au sujet est un avantage, pas un handicap, notamment contre le biais du client (§7.7).

### 12.3 Le désaccord analytique

**Le principe qui gouverne ce paragraphe** : un désaccord entre analystes n'est pas un problème à résoudre. C'est une **information à conserver**.

**Ce qu'on fait habituellement** : on discute jusqu'à ce qu'une position l'emporte, puis on écrit la position gagnante. Le désaccord disparaît du document, et avec lui l'information qu'il portait — à savoir qu'un professionnel compétent, avec les mêmes éléments, arrivait à une autre conclusion.

**Ce qu'il faut faire** : documenter les deux positions et **ce qui les sépare**.

🧪 **EN PRATIQUE — formaliser un désaccord**

```
Position retenue      : [conclusion], confiance [niveau]
Position alternative  : [conclusion], soutenue par [qui]
Ce qui les sépare     : [le point précis de divergence]
                        — une lecture différente d'un élément ?
                        — une pondération différente ?
                        — un présupposé différent ?
Ce qui trancherait    : [l'information manquante]
```

**La ligne « ce qui les sépare » est celle qui a de la valeur.** Un désaccord porte presque toujours sur un point identifiable — souvent un présupposé implicite que l'un des deux tient pour acquis. L'expliciter est un progrès analytique, indépendamment de qui a raison.

### 12.4 La note dissidente

**Quand l'employer** : lorsque le désaccord porte sur une conclusion engageante et qu'il n'a pas été résolu.

**Ce que c'est** : un encadré d'une demi-page, joint au produit, signé, exposant la position minoritaire et son argumentation.

**Pourquoi c'est utile**, et les trois raisons sont indépendantes :

| Raison | Mécanisme |
|---|---|
| **Le décideur reçoit l'information complète** | Il sait que la conclusion n'est pas unanime, ce qui l'aide à calibrer sa propre confiance |
| **Elle préserve la capacité de contradiction** | Un analyste dont la position minoritaire a été publiée une fois continuera d'en exprimer |
| **Elle documente le raisonnement pour la suite** | Si l'alternative se vérifie, l'organisation sait qu'elle avait été envisagée, et pourquoi elle a été écartée |

📌 **LIMITES** — Le dispositif s'use s'il devient systématique. Une note dissidente sur chaque produit signale que le processus de discussion ne fonctionne pas en amont. Réservez-la aux désaccords réels et engageants — quelques fois par an au plus.

### 12.5 L'analyste seul

C'est le cas le plus fréquent, et il serait malhonnête de traiter ce chapitre sans lui.

**Ce qui n'est pas possible** : la revue par un pair analyste, la note dissidente au sens strict, l'équipe rouge analytique.

**Ce qui est possible, et ce qui fonctionne réellement** :

| Substitut | Principe | Coût | Efficacité |
|---|---|---|---|
| **Le relecteur non spécialiste** | Un collègue quelconque, la grille du §12.2 en main | 12 min | **Élevée** — la grille est formelle |
| **Le décalage temporel** | Relire son produit le lendemain, avec la grille | 15 min | Moyenne — l'ancrage persiste, mais s'atténue |
| **L'écriture de l'hypothèse adverse** | Rédiger un paragraphe défendant l'hypothèse écartée, comme si on y croyait | 20 min | **Élevée** — c'est l'avocat du diable, en solitaire |
| **Le pair externe** | Un homologue d'une autre organisation, sur des cas anonymisés | Variable | Élevée, mais suppose un réseau (chapitre 28) |
| **La relecture par le destinataire** | Faire relire l'évaluation par celui qui a posé la question, avant diffusion large | 10 min | Moyenne — risque de biais du client |

**Les deux premiers sont accessibles à tout le monde, immédiatement.** Le troisième est le plus efficace des trois, et le plus inconfortable : écrire sincèrement l'argumentaire de la conclusion qu'on rejette révèle régulièrement qu'elle tient mieux qu'on ne le croyait.

🎯 **ET MAINTENANT ?**
*Vous êtes seul, votre évaluation est prête, et vous n'avez personne à qui la faire relire. Que faites-vous avant de l'envoyer ?*
**Réponse** : vingt minutes, deux gestes. D'abord, vous écrivez un paragraphe qui défend l'hypothèse que vous avez écartée — sincèrement, comme si vous deviez la présenter. Si ce paragraphe vous paraît faible, votre conclusion tient ; s'il vous paraît recevable, votre confiance était trop haute et vous la corrigez. Ensuite, vous passez la grille en six points du §12.2 sur votre propre texte. Ce n'est pas aussi bon qu'une relecture par un tiers — c'est très supérieur à rien, et cela prend moins de temps qu'une réunion.

### 12.6 ⚠️ Le consensus prématuré

**Le mécanisme** : dans un groupe, la première conclusion exprimée par une personne perçue comme compétente devient rapidement la conclusion du groupe. Les positions divergentes ne s'expriment plus, non par lâcheté mais parce que le coût social de la contradiction augmente à mesure que le consensus se forme.

**Les trois signaux** :

| Signal | Ce qu'il indique |
|---|---|
| La discussion converge en moins de dix minutes sur un dossier complexe | Personne n'a formulé d'alternative |
| Les objections sont formulées comme des questions plutôt que comme des positions | Le coût social est déjà élevé |
| La conclusion est celle du premier qui a parlé | Ancrage collectif (§7.3) |

**Les deux dispositifs qui fonctionnent** :

1. **L'écriture avant la discussion.** Chacun écrit sa conclusion et son niveau de confiance **avant** que le sujet ne soit discuté. Cinq minutes. Les écarts apparaissent alors, et ils sont exploitables.
2. **L'attribution explicite du rôle contradictoire** (§8.5). Une objection produite au titre d'un rôle est reçue comme un service ; la même objection produite spontanément est reçue comme une opposition.

### 12.7 🔴 FIL ROUGE — janvier 2030 : ce qu'une seconde paire d'yeux voit

La relecture croisée est en place depuis juillet (§4.9). Le relecteur habituel de Nour est Malik Ferhaoui — responsable de l'exploitation, **pas analyste**, et c'est précisément l'intérêt.

Le 15 janvier, Nour lui soumet une évaluation sur une technique d'accès initial signalée dans le secteur. Douze minutes de relecture, grille en main.

**Les trois remarques de Malik** :

| # | Remarque | Point de la grille |
|---|---|---|
| 1 | *« Tu écris que l'attaquant "privilégie" cette technique. Comment tu sais ce qu'il préfère ? »* | Point 1 — verbe d'intention en section factuelle |
| 2 | *« Tes deux sources, c'est deux publications ou deux observations ? »* | Point 4 — indépendance |
| 3 | *« Là tu dis que la technique exploite un défaut de configuration courant. Chez nous, il est courant ce défaut ? Parce que si je dois chercher, il me faut savoir où. »* | Point 6 — utilité |

**Les deux premières sont formelles**, et Nour les corrige en cinq minutes.

**La troisième change l'évaluation.** Nour avait repris de la source l'expression *« configuration par défaut fréquemment rencontrée »*, sans se demander si elle était fréquente **chez HELIOMED**. Vérification faite en une heure : la configuration en cause n'existe sur aucun des serveurs concernés — HELIOMED avait durci ce point en 2027, dans le cadre du dispositif de maintien en condition de sécurité.

**La conclusion révisée** passe d'une recommandation de recherche rétrospective sur trente serveurs — trois jours-homme — à une note d'information de cinq lignes indiquant que la technique décrite n'est pas applicable en l'état à l'organisation, avec la référence de la mesure qui la neutralise.

**Ce que l'épisode démontre**, et c'est le point du chapitre : **le relecteur n'a repéré aucune erreur d'analyse.** Il a repéré trois défauts de forme, dont l'un a révélé un défaut de fond — l'étape 4 du chapitre 2, celle qui rapporte la connaissance au contexte propre de l'organisation, avait été sautée.

Malik n'a aucune compétence en analyse de renseignement. Il a une grille et une connaissance du parc. C'est suffisant.

**Ce que Claire en tire pour l'organisation** : la relecture croisée est étendue à tous les produits sortants, avec un relecteur **tournant** parmi cinq personnes de domaines différents. Le tour de rôle est délibéré : chacun repère des choses différentes, et aucun ne s'habitue au point de relire mécaniquement.

**Les chiffres après six mois**, présentés au comité de juillet 2030 :

| Indicateur | Valeur |
|---|---|
| Produits relus | 47 |
| Remarques formelles | 112 |
| **Remarques ayant modifié une conclusion** | **9** |
| Temps total consacré | ≈ 10 heures |

Neuf conclusions modifiées pour dix heures de relecture. Aucun autre dispositif du dossier n'affiche un rapport comparable.

> *« Ce n'est pas qu'ils sont meilleurs que moi, écrit Nour. C'est qu'ils ne sont pas moi. »*

**Livrable de l'épisode.** La grille de relecture en six points, une demi-page, avec la règle du relecteur tournant — annexe C.

→ **Fin de la Partie II, prochain chapitre excepté.** La suite en 🔴 §13.8, quand un client demandera de nommer un coupable.

### Synthèse mentale du chapitre 12

On ne détecte pas ses propres biais, on détecte ceux des autres : un analyste seul ne peut donc pas se relire utilement sur le fond, et le travail solitaire produit quatre dérives dont la plus insidieuse est l'accumulation de présupposés hérités de dossier en dossier. La revue par les pairs porte sur six points formels et prend douze minutes — et le relecteur n'a pas besoin d'être analyste, son extériorité étant un avantage contre le biais du client. Un désaccord analytique n'est pas un problème à résoudre mais une information à conserver, et la ligne qui compte est celle qui identifie **ce qui sépare** les deux positions, presque toujours un présupposé implicite. Pour l'analyste seul, trois substituts fonctionnent : le relecteur non spécialiste avec la grille, le décalage temporel, et l'écriture sincère de l'hypothèse adverse — le plus efficace et le plus inconfortable des trois. Enfin, le consensus prématuré se combat en faisant écrire chacun avant de discuter.

**Trois questions de vérification**

1. Vous êtes seul dans votre fonction. Quels trois dispositifs mettez-vous en place cette semaine, et lequel est le plus efficace ?
2. Pourquoi un relecteur non analyste peut-il être plus utile qu'un pair expérimenté sur certains points précis ?
3. Deux analystes arrivent à des conclusions opposées avec les mêmes éléments. Que faites-vous du désaccord, et quelle ligne du document a le plus de valeur ?

→ **Chapitre 13 — L'attribution** : le sujet qui fascine, et pourquoi vous n'en avez presque jamais besoin.

---

## Chapitre 13 — L'attribution

> 📌 **Périmètre de ce chapitre.** Il traite l'attribution du point de vue d'une organisation qui se défend. Le renseignement étatique, les équipes d'attribution spécialisées et les enjeux judiciaires relèvent d'autres métiers, avec d'autres moyens, d'autres accès et d'autres cadres juridiques. Quand ce chapitre écrit « vous ne pouvez pas », cela signifie *une organisation ordinaire ne le peut pas* — pas *personne ne le peut*.

### 13.1 Ce que l'attribution cherche à établir

**L'attribution consiste à relier une activité observée à son auteur.** Le mot recouvre en réalité quatre questions distinctes, de difficulté croissante, et la confusion entre elles explique une grande partie des malentendus.

| Niveau | Question | Difficulté | Utile à qui |
|---|---|---|---|
| **1 — Technique** | Quelle machine, quelle infrastructure ? | Accessible | Détection, blocage |
| **2 — Opérationnelle** | Quel ensemble d'activités forme un tout cohérent ? | Accessible avec du travail | **Vous** — c'est le regroupement en campagnes |
| **3 — Organisationnelle** | Quel groupe, quelle structure ? | Difficile | Rarement vous |
| **4 — Politique** | Quel commanditaire, quel État ? | **Très difficile, souvent impossible sans moyens régaliens** | Presque jamais vous |

**Le niveau 2 est celui qui vous concerne, et il est rarement appelé « attribution ».** Regrouper des activités en un ensemble cohérent — même infrastructure, mêmes outils, même séquence — permet de raisonner, de prévoir et de détecter. Cela ne nécessite aucun nom.

**Les niveaux 3 et 4 sont ceux dont on parle**, et ce sont ceux dont vous n'avez presque jamais besoin. Le §13.5 le démontre.

### 13.2 Les méthodes, et leurs faiblesses

| Méthode | Principe | Faiblesse |
|---|---|---|
| **Infrastructure** | Réutilisation d'adresses, de domaines, d'hébergeurs | Infrastructure partagée, louée, revendue, compromise chez un tiers |
| **Outillage** | Réutilisation de code, de configurations, d'outils | **Outils partagés, vendus, volés, publiés** — c'est la faiblesse majeure |
| **Modes opératoires** | Similarité des séquences d'actions | Les techniques efficaces se diffusent ; la ressemblance est attendue |
| **Artefacts linguistiques** | Langue, fuseau horaire, encodage, fautes | Falsifiables trivialement, et souvent falsifiés |
| **Horaires d'activité** | Rythme de travail, jours chômés | Falsifiable, et brouillé par les infrastructures intermédiaires |
| **Ciblage** | Cohérence des victimes avec un intérêt supposé | Raisonnement circulaire : on attribue à qui « aurait intérêt », ce qui suppose la conclusion |
| **Renseignement d'origine humaine ou technique étatique** | — | **Hors de portée d'une organisation privée** |

**Le point commun de toutes ces méthodes** : elles établissent des **ressemblances**, jamais des identités. Une ressemblance est un indice au sens du §6.2, et l'accumulation d'indices faibles ne produit pas une preuve (§6.2, piège).

⚠️ **PIÈGE — le raisonnement par le ciblage**
« Cette attaque bénéficie à X, donc X en est l'auteur » est la faiblesse la plus séduisante de la liste, parce qu'elle produit un récit satisfaisant. Elle suppose que l'auteur soit rationnel, informé, et seul à en tirer bénéfice — trois hypothèses rarement vérifiées. Elle est aussi trivialement exploitable par un adversaire qui souhaite être attribué à un autre.

### 13.3 Les opérations sous faux drapeau et la réutilisation d'outillage

**Deux phénomènes distincts, souvent confondus.**

**La réutilisation d'outillage** est le cas ordinaire, et il n'implique aucune intention de tromper. Les outils circulent : vendus, loués, publiés après une fuite, réimplémentés. Un outil associé à un groupe dans un rapport de 2027 peut être employé en 2030 par n'importe qui. **C'est le mécanisme qui invalide le plus d'attributions**, sans qu'aucun adversaire n'ait rien fait pour cela.

**Le faux drapeau** est délibéré : l'adversaire imite les caractéristiques d'un autre pour orienter l'attribution. C'est plus rare, plus coûteux, et cela cible précisément les méthodes du §13.2 — artefacts linguistiques, réutilisation d'outils connus, horaires.

**Ce qu'il faut en retenir opérationnellement** : *l'ensemble des caractéristiques observables d'une intrusion est falsifiable par un adversaire qui en a la volonté et les moyens*. Toute attribution de niveau 3 ou 4 fondée uniquement sur des éléments techniques est donc réfutable — ce qui ne la rend pas fausse, mais interdit d'y accorder une confiance élevée.

### 13.4 ⚠️ Pourquoi un défenseur n'en a presque jamais besoin

Voici la démonstration, et c'est le cœur du chapitre.

**Le test** : prenez les mesures de défense que vous prendriez, et demandez lesquelles changent selon l'auteur.

| Mesure | Change selon l'auteur ? |
|---|---|
| Corriger la vulnérabilité exploitée | **Non** |
| Réinitialiser les identifiants compromis | **Non** |
| Rechercher les indicateurs dans les journaux | **Non** |
| Renforcer la détection sur les techniques observées | **Non** |
| Segmenter le périmètre atteint | **Non** |
| Notifier les personnes concernées | **Non** |
| Restaurer et reconstruire | **Non** |
| Alerter un partenaire exposé | **Non** |

**Aucune.** Les mesures de défense découlent de **ce qui a été fait**, pas de **qui l'a fait**. C'est le niveau 2 de l'attribution — le regroupement opérationnel — qui les informe, jamais le niveau 3 ou 4.

**La conséquence, formulée franchement** : le temps consacré à identifier un auteur est du temps qui n'est pas consacré à comprendre le mode opératoire — lequel, lui, change vos mesures.

📌 **Ce que l'attribution apporte malgré tout, indirectement** : connaître un acteur permet parfois d'**anticiper** ce qu'il fera ensuite, s'il a un comportement stable. C'est un apport réel, mais il est de nature prédictive et faible : les acteurs évoluent, se recomposent, et les rapports qui les décrivent ont dix-huit mois de retard.

### 13.5 Les rares cas où elle compte

Ils existent, et il faut les connaître pour ne pas être dogmatique.

| Cas | Pourquoi l'attribution compte | Qui la produit |
|---|---|---|
| **Assurance** | Certaines polices excluent les actes relevant d'un conflit armé ou d'un acteur étatique | L'assureur, pas vous — mais vous fournissez les éléments |
| **Contentieux** | Une action judiciaire suppose un auteur identifiable | Les autorités et les experts judiciaires |
| **Sanctions et conformité** | Verser une rançon à une entité sanctionnée expose à des poursuites | Le juridique, sur la base de listes officielles |
| **Décision politique ou diplomatique** | Hors du champ d'une organisation privée | Les États |
| **Communication de crise** | Un client ou un régulateur peut demander | **Vous — et c'est le §13.7** |

⚠️ Dans les trois premiers cas, remarquez que **ce n'est pas vous qui attribuez**. Votre rôle est de fournir des éléments factuels et de ne pas produire d'affirmation que vous ne pouvez pas soutenir. Une attribution hasardeuse figurant dans un document interne peut se retourner contre l'organisation dans une procédure.

### 13.6 Le coût d'une attribution erronée

Quatre coûts, dans l'ordre où ils se manifestent :

| Coût | Mécanisme |
|---|---|
| **Défense mal orientée** | On se prépare au comportement supposé de l'acteur nommé, pas à ce qui se passe réellement |
| **Crédibilité** | Une attribution démentie publiquement décrédibilise l'ensemble de la fonction, y compris ses analyses justes |
| **Juridique** | Une désignation d'un tiers, même interne, peut engager la responsabilité de l'organisation |
| **Diplomatique ou commercial** | Nommer un État ou une entité peut avoir des conséquences hors du champ de la sécurité |

**Le deuxième est le plus fréquent et le plus durable.** Une fonction CTI qui s'est trompée une fois sur une attribution voit ses évaluations ultérieures reçues avec réserve, y compris celles qui sont solides. Le gain d'une attribution juste est faible ; le coût d'une attribution fausse est élevé et prolongé. **L'asymétrie du pari est défavorable.**

### 13.7 Répondre à « qui nous attaque ? » sans mentir ni esquiver

La question sera posée. Par une direction, un client, un journaliste, un partenaire. Voici comment y répondre.

**Ce qui ne fonctionne pas** :

| Réponse | Pourquoi |
|---|---|
| « Nous ne faisons pas d'attribution. » | Reçu comme une dérobade, ou comme de l'incompétence |
| « C'est probablement [nom]. » | Vous engagez l'organisation sur ce que vous ne pouvez pas soutenir |
| « C'est trop complexe pour être expliqué. » | Condescendant, et faux |

**Ce qui fonctionne** — quatre temps, trente secondes :

```
1. Ce que nous savons du COMPORTEMENT
   « Nous avons identifié le vecteur d'entrée, les techniques employées
     et le périmètre atteint. »

2. Ce que cela nous permet de FAIRE
   « Cela nous a permis de fermer l'accès, de corriger la faille et de
     vérifier l'absence de persistance. »

3. Pourquoi le NOM ne change rien
   « L'identité de l'auteur ne modifierait aucune de ces mesures. »

4. Ce que nous pouvons dire, honnêtement
   « Le mode opératoire présente des similarités avec des activités
     décrites publiquement. Nous ne sommes pas en mesure d'attribuer
     avec un niveau de confiance suffisant pour l'affirmer. »
```

**Le troisième point est celui qui désamorce.** La question « qui nous attaque ? » exprime presque toujours un besoin de contrôle — comprendre pour maîtriser. Montrer que la maîtrise vient du comportement, pas du nom, y répond réellement.

🎯 **ET MAINTENANT ?**
*Un journaliste vous demande si l'attaque que vous avez subie provient d'un acteur étatique. Que répondez-vous ?*
**Réponse** : rien de plus que les quatre temps ci-dessus, et vous ne vous laissez pas entraîner sur le terrain de la spéculation — y compris quand la question est reformulée en « mais ce serait cohérent avec… ». La phrase utile : *« nous ne disposons pas d'éléments permettant d'attribuer cette activité avec un niveau de confiance qui justifierait une affirmation publique »*. Elle est vraie, elle n'est pas une esquive, et elle ne vous engage pas. Si votre organisation dispose d'une procédure de communication de crise, cette réponse y figure — écrite à froid, comme le veut le chapitre 32.

### 13.8 🔴 FIL ROUGE — février 2030 : Nour refuse de confirmer

Le 4 février, un article de presse spécialisée affirme qu'une campagne visant des fournisseurs du secteur de la santé européen est « attribuée au groupe TEMPEST-14 ». HELIOMED n'est pas citée.

Le 5 février, le directeur des systèmes d'information du centre hospitalier universitaire — celui-là même dont le courriel de mars 2029 a déclenché toute l'histoire (§1.10) — écrit à Yann Prigent :

> *« Nous lisons que le groupe TEMPEST-14 cible nos fournisseurs. Confirmez-vous que c'est bien cet acteur qui est à l'origine des incidents que vous nous avez signalés en septembre ? Notre comité de sécurité se réunit jeudi. »*

**La tentation est réelle.** Confirmer donnerait une réponse claire à un client important, avant son comité, et l'article dit ce que tout le monde pense.

**Ce que Nour vérifie**, en une demi-journée :

| Vérification | Résultat |
|---|---|
| Sur quoi l'article fonde-t-il l'attribution ? | Une publication d'éditeur du 28 janvier |
| Que dit cette publication exactement ? | *« présente des similarités avec l'outillage associé à TEMPEST-14 »* — une similarité d'outillage, avec confiance modérée |
| L'incident de septembre chez HELIOMED est-il lié ? | **Non** — il s'agissait de la compromission du prestataire (§8.9), avec un vecteur documenté et sans rapport |
| L'outillage cité a-t-il circulé ? | **Oui** — publié après une fuite en 2028, employé depuis par plusieurs acteurs distincts |

**Ce que Nour écrit à Yann**, pour transmission au client — quatre paragraphes :

> *Nous ne sommes pas en mesure de confirmer cette attribution, et nous ne pouvons pas l'infirmer.*
>
> *L'affirmation reprise par la presse provient d'une publication du 28 janvier, qui indique une similarité d'outillage avec un ensemble d'activités désigné TEMPEST-14, avec une confiance modérée. L'outillage concerné a été rendu public en 2028 et est employé depuis par plusieurs acteurs distincts ; sa présence ne permet donc pas d'identifier un auteur.*
>
> *Concernant les incidents que nous vous avons signalés en septembre 2029 : leur origine est documentée et sans rapport avec cette campagne. Il s'agissait de la compromission d'un prestataire d'infogérance, confirmée par ce dernier, avec un vecteur d'entrée identifié.*
>
> *Ce que nous pouvons affirmer : le vecteur employé en septembre est fermé, la mesure correspondante est en place et vérifiée, et nous n'avons observé aucune activité comparable depuis. Nous restons disponibles pour présenter ces éléments à votre comité.*

**La réaction du client** — et c'est ce que l'épisode enseigne. Le directeur répond le lendemain :

> *« C'est exactement ce dont j'avais besoin. Mon comité voulait un nom ; ce que je vais leur présenter est mieux : ce qui s'est passé, ce qui a été fait, et ce que vous savez ne pas savoir. »*

**Ce que Claire relève au comité de sécurité.** Refuser de confirmer aurait pu être perçu comme une faiblesse. Ce qui l'a évité, ce n'est pas le refus lui-même — c'est ce qui l'accompagnait : une explication du raisonnement, une réponse à la question sous-jacente, et une proposition d'aller plus loin.

> *« Dire "je ne sais pas" tout court, c'est une dérobade, note-t-elle. Dire "je ne sais pas, voici pourquoi, voici ce que je sais et voici ce que je peux faire", c'est du renseignement. »*

**L'épilogue, six semaines plus tard.** Le 19 mars, l'éditeur à l'origine de la publication du 28 janvier publie une mise à jour : l'attribution est retirée, la similarité d'outillage s'expliquant par la diffusion publique du code. Deux autres fournisseurs du secteur, qui avaient confirmé l'attribution à leurs clients, doivent se rétracter.

**Livrable de l'épisode.** La réponse type en quatre temps du §13.7, intégrée à la procédure de communication de crise d'HELIOMED — et validée par la direction juridique.

→ **Fin de la Partie II.** La suite en Partie III, quand il faudra transformer six questions posées en mai 2029 en un dispositif de collecte.

---

> ### 🎓 À ce stade de la Partie II, vous savez…
>
> - **raisonner avec plusieurs hypothèses**, et chercher ce qui les discrimine plutôt que ce qui les confirme ;
> - **reconnaître les sept biais** dans un produit — le vôtre comme celui des autres — et savoir qu'aucun ne se corrige par la volonté seule ;
> - **structurer une analyse** avec une matrice d'hypothèses concurrentes, et **savoir quand ne pas le faire** ;
> - **calibrer** une affirmation sur trois axes indépendants, et écrire un niveau de confiance qui s'explique en une ligne ;
> - **évaluer une source**, remonter une chaîne de provenance, et détecter une circularité en quinze minutes ;
> - **produire un jugement** qui s'engage, dit ce qui l'invaliderait, et sépare l'évaluation de la recommandation ;
> - **faire relire** votre travail par un non-spécialiste avec une grille en six points ;
> - **répondre à « qui nous attaque ? »** sans mentir, sans esquiver, et sans engager votre organisation.
>
> **Ce que vous ne savez pas encore** : comment obtenir d'un décideur ce qu'il a réellement besoin de savoir, et comment organiser la collecte qui en découle. C'est l'objet de la Partie III.

---
