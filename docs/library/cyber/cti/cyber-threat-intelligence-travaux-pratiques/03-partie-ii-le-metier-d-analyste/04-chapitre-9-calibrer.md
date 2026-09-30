---
title: Chapitre 9 — Calibrer
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE II — Le métier d'analyste
  - index.md
---

## 9.1 Confiance, probabilité, gravité : trois axes indépendants

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

## 9.2 Le langage estimatif : pourquoi « possible » ne veut rien dire

**Le problème.** Les mots de probabilité sont interprétés très différemment d'une personne à l'autre. Des études menées dans plusieurs contextes professionnels montrent que des expressions comme *probable*, *possible* ou *vraisemblable* recouvrent, selon les lecteurs, des fourchettes qui vont du quasi-certain au peu vraisemblable — et que ces écarts persistent y compris entre professionnels du même domaine.

**Le cas de « possible »** mérite un traitement à part : il est le mot le plus employé et le moins informatif de la langue analytique. *Possible* signifie littéralement « non exclu », ce qui est vrai de presque tout. Une phrase qui dit « il est possible que X » n'a transmis aucune information au lecteur.

🧪 **EN PRATIQUE — le test du remplacement**

Prenez une phrase de votre produit contenant un mot de probabilité, et remplacez-le par « non exclu ». Si la phrase reste acceptable, le mot ne portait rien.

| Phrase originale | Test | Verdict |
|---|---|---|
| « Il est possible que ce groupe cible notre secteur » | « Il n'est pas exclu que ce groupe cible notre secteur » | ❌ Aucune information |
| « Nous estimons probable que… » | « Il n'est pas exclu que… » | ✅ Le sens change — le mot portait |

## 9.3 L'échelle de probabilité verbale

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

## 9.4 Sur quoi repose un niveau de confiance

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

## 9.5 Exprimer une incertitude sans paraître incompétent

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

## 9.6 ⚠️ Les formulations à bannir, et par quoi les remplacer

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

## 9.7 ✅ Livrable — L'échelle de calibrage de l'organisation

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

## 9.8 🔴 FIL ROUGE — octobre 2029 : mettre un mot sur « probable »

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

## Synthèse mentale du chapitre 9

Probabilité, confiance et gravité sont trois axes indépendants, et la faute la plus fréquente du métier consiste à les fusionner en un adjectif — « menace critique » ne dit ni si c'est probable, ni si c'est établi. La combinaison la plus utile à transmettre est celle d'une gravité élevée avec une confiance faible : elle appelle une vérification, pas une mobilisation. Les mots de probabilité sont interprétés très différemment selon les lecteurs, et « possible » signifie « non exclu », donc presque rien : le test consiste à remplacer le mot et voir si la phrase perd du sens. Une échelle fermée de sept expressions et trois niveaux de confiance, publiée en annexe de chaque produit, résout le problème — à condition que le niveau de confiance soit toujours expliqué en une ligne. Enfin, exprimer une incertitude ne dessert pas quand elle est structurée en quatre temps : ce que nous savons, ce que nous estimons, ce que nous ignorons, ce qui trancherait. La différence entre paraître subir sa question et paraître la maîtriser n'est pas le niveau de connaissance, c'est la structure.

**Trois questions de vérification**

1. Une source unique annonce une menace majeure contre votre organisation. Comment calibrez-vous, et quelle décision cela appelle-t-il ?
2. Pourquoi « nous estimons à 73 % la probabilité que » est-il moins rigoureux que « probable » ?
3. Votre direction exige une réponse par oui ou non. Construisez une réponse en trois phrases qui ne soit ni un oui, ni un non, ni une dérobade.

→ **Chapitre 10 — Évaluer une source et une information** : deux axes à ne jamais fusionner, et le mécanisme par lequel trois sources n'en font qu'une.

---
