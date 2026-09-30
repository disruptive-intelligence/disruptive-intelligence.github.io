---
title: Chapitre 4 — Les axiomes de l'analyste
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
up:
- - CTI — travaux pratiques
  - ../index.md
- - PARTIE I — Fondamentaux du renseignement
  - index.md
---

> Six énoncés, avant toute théorie de l'analyse. Ils paraissent évidents. Ils sont pourtant violés en permanence, y compris dans des publications professionnelles — et chacun d'eux, une fois posé, élimine une famille entière de mauvais raisonnements.
>
> Ils sont réutilisés dans les trente-six chapitres suivants. Le chapitre 8, sur les techniques d'analyse structurée, n'est au fond qu'un ensemble de méthodes pour les respecter quand l'intuition tire dans l'autre sens.

## 4.1 Observer n'est pas conclure

**L'énoncé.** Ce que vous constatez et ce que vous en déduisez sont deux affirmations distinctes. Elles ont des statuts différents, des degrés de certitude différents, et elles doivent être écrites séparément.

**Le mécanisme de la violation.** Le cerveau produit l'interprétation *en même temps* que l'observation, pas après. Vous ne voyez pas « douze tentatives d'authentification échouées » puis concluez « quelqu'un teste des identifiants » : vous percevez immédiatement un test d'identifiants. L'interprétation arrive déjà collée au fait, et il faut un effort délibéré pour les décoller.

🧪 **EN PRATIQUE — le test de séparation**

Prenez n'importe quelle phrase de votre dernier produit et demandez : *si je remplace le verbe par « nous observons », la phrase reste-t-elle vraie ?*

| Phrase | Test | Verdict |
|---|---|---|
| « L'attaquant a tenté de compromettre le compte administrateur » | *Nous observons que l'attaquant a tenté…* | ❌ **Faux.** Vous observez des échecs d'authentification sur ce compte. Que ce soit un attaquant, qu'il ait « tenté de compromettre », et qu'il y ait une intention : ce sont trois déductions |
| « Douze tentatives d'authentification ont échoué sur le compte administrateur entre 02 h 50 et 03 h 40 » | *Nous observons que…* | ✅ **Vrai.** C'est une observation |
| « Le groupe X cible le secteur de la santé » | *Nous observons que…* | ❌ **Faux.** Vous observez des victimes du secteur ; « cible » suppose une intention |

**Ce que ça change concrètement** : votre produit devient utilisable par quelqu'un qui n'a pas votre contexte. Il peut distinguer ce sur quoi il peut s'appuyer sans réserve de ce qu'il doit interroger.

⚠️ **PIÈGE — le verbe d'intention**
*Cibler, chercher à, tenter de, viser, s'intéresser à* — tous ces verbes attribuent une intention à un acteur dont vous n'observez que des effets. Ils ne sont pas interdits : ils appartiennent au registre du jugement, pas du fait. Écrivez-les dans la section évaluation, jamais dans la section observation.

## 4.2 Corrélation n'est pas causalité — et en renseignement, la coïncidence est fréquente

**L'énoncé** est connu. Ce qui l'est moins, c'est **pourquoi il mord particulièrement fort ici**.

Le CTI travaille sur des données massives, faiblement structurées, provenant de sources hétérogènes. Dans ce contexte, les coïncidences sont **abondantes** :

| Coïncidence typique | Interprétation tentante | Explication alternative banale |
|---|---|---|
| Deux organisations du même secteur touchées la même semaine | Campagne ciblée sur le secteur | Elles utilisent le même produit vulnérable, exploité massivement |
| Une adresse apparaît dans deux incidents distincts | Même acteur | Hébergement mutualisé, adresse réattribuée, service légitime détourné |
| Une intrusion suit de peu une publication de vulnérabilité | Exploitation de cette vulnérabilité | Le vecteur réel est ailleurs ; la proximité temporelle est fortuite |
| Un pic d'activité coïncide avec un événement géopolitique | Réaction à l'événement | Le pic correspond à une campagne opportuniste sans rapport |

**Le test à appliquer** : *quelle autre explication produirait exactement la même observation ?* Si vous n'en trouvez aucune, ce n'est pas que l'explication est certaine — c'est que vous n'avez pas assez cherché. Le chapitre 8 en fait une méthode.

🎯 **ET MAINTENANT ?**
*Trois de vos concurrents ont été victimes d'un rançongiciel en six semaines. Un rapport en conclut que le secteur est ciblé. Que faites-vous de cette conclusion ?*
**Réponse** : vous cherchez ce qui les relie **autrement que par le secteur**. Même prestataire informatique ? Même progiciel métier ? Même solution d'accès distant ? Trois victimes d'un même secteur peuvent être trois victimes d'un même fournisseur — et la mesure à prendre n'est alors pas du tout la même. C'est une question à poser avant d'accepter la conclusion, pas après.

## 4.3 Absence de preuve n'est pas preuve d'absence — et l'inverse est tout aussi faux

**Le premier volet** est classique : ne rien avoir trouvé ne signifie pas qu'il n'y a rien.

**Le second volet l'est beaucoup moins**, et il est tout aussi important : **l'absence n'est pas non plus une preuve de présence**. La formule provocatrice *« l'absence d'information est une information »* circule beaucoup et autorise, mal comprise, exactement le raisonnement qu'on veut éviter :

```
Je n'ai rien trouvé
        ↓
Donc l'adversaire est discret
        ↓
Donc il est sophistiqué
        ↓
Donc c'est grave
```


Chaque flèche est une déduction non fondée. Ce raisonnement est plus fréquent qu'on ne croit, particulièrement après un incident où l'on n'a pas trouvé grand-chose.

**La formulation robuste** est celle-ci :

> **L'absence appelle une question sur votre capacité d'observation, pas une conclusion sur le réel.**

Trois questions, dans cet ordre :

| # | Question | Ce qu'elle vérifie |
|---|---|---|
| 1 | **Ai-je cherché au bon endroit ?** | Le périmètre de la recherche |
| 2 | **Avais-je les bons capteurs ?** | La capacité technique à voir ce type d'activité |
| 3 | **Ai-je cherché assez longtemps ?** | La profondeur d'historique disponible |

Si les trois réponses sont *oui*, l'absence devient un élément d'appréciation — faible, mais réel. Si l'une est *non*, l'absence ne dit **rien du tout**, et le produit doit le dire explicitement.

⚠️ Ceux qui viennent du cours MCS reconnaîtront la formulation du §21.3 : *l'absence de preuve de compromission n'est pas la preuve de l'absence de compromission, a fortiori quand la journalisation est insuffisante*. C'est le même axiome, appliqué à un autre métier.

## 4.4 Un renseignement est périssable

**L'énoncé.** Toute affirmation de renseignement a une date de péremption. Elle n'est pas toujours connue, mais elle existe toujours.

**Les rythmes**, repris du chapitre 3 :

| Objet | Durée de validité typique | Ce qui la fait expirer |
|---|---|---|
| Une adresse d'infrastructure | Jours à semaines | L'adversaire change d'infrastructure |
| Une empreinte de fichier | Une variante | Une recompilation suffit |
| Un mode opératoire | Mois à années | L'adversaire adapte, ou une défense se généralise |
| Une évaluation de motivation | Années | Un changement de contexte géopolitique ou économique |
| Un rapport lu sans vérifier sa date | **Immédiate** | — |

**La conséquence pratique la plus importante** : un produit de renseignement doit **porter sa date et son horizon de validité**. Pas seulement la date de rédaction — la date jusqu'à laquelle l'analyste estime que la conclusion tient.

🧪 **EN PRATIQUE — la mention à ajouter systématiquement**

```
Évaluation au 14 novembre 2029.
Réexamen prévu : février 2030, ou plus tôt si [événement déclencheur].
```


Cette mention coûte quinze secondes. Elle évite qu'un rapport soit cité deux ans plus tard comme s'il décrivait le présent — situation dont vous serez témoin plus souvent que vous ne le croyez.

## 4.5 Une analyse est une hypothèse argumentée, pas une description

**L'énoncé.** Décrire n'est pas analyser. Un document qui expose des faits sans conclure n'est pas une analyse prudente : c'est une analyse absente.

**La confusion** est entretenue par une bonne intention. L'analyste veut être rigoureux, il évite d'affirmer, il expose les éléments et laisse le lecteur juger. Le résultat est que **le destinataire doit faire l'analyse lui-même** — c'est-à-dire faire le travail pour lequel la fonction existe.

| Ce que ce n'est pas | Ce que c'est |
|---|---|
| Un résumé de ce qui a été publié | Une position argumentée sur ce qui est le plus probable |
| Une liste d'éléments | Un raisonnement qui les relie |
| « Plusieurs hypothèses sont possibles » | « Nous retenons l'hypothèse B, pour ces trois raisons, avec cette confiance » |
| Une description neutre | **Un engagement révisable** |

**Le mot important est *révisable*.** Une analyse s'engage — et prévoit ce qui la ferait changer d'avis. C'est ce qui la distingue à la fois de la description, qui n'engage rien, et de l'opinion, qui ne prévoit pas de révision. Le chapitre 11 en fait la méthode complète.

## 4.6 Une source n'est pas un fait

**L'énoncé.** Que quelqu'un l'ait écrit ne le rend pas vrai. Que trois personnes l'aient écrit ne le rend pas trois fois plus vrai.

C'est l'axiome le plus violé du domaine, parce que la violation est **invisible** : elle se produit au moment où l'on recopie une affirmation en changeant simplement de mode grammatical.

| Ce que la source dit | Ce qui est recopié | La transformation opérée |
|---|---|---|
| *« Nous évaluons avec une confiance modérée que… »* | « Le groupe X fait… » | Un jugement calibré devient un fait |
| *« Selon des chercheurs, il est possible que… »* | « Il est établi que… » | Une hypothèse devient une certitude |
| *« Un incident a été rapporté »* | « Une campagne vise… » | Un cas devient une campagne |
| *« Cette activité présente des similarités avec… »* | « Cette activité est attribuée à… » | Une similarité devient une attribution |

**Le mécanisme** est la perte de la chaîne de provenance à chaque reprise. Au bout de trois reprises successives, une hypothèse prudente est devenue un fait établi, et personne ne peut plus remonter à l'affirmation d'origine. C'est ce qui produit la **circularité** du §10.4, et c'est le cas de synthèse B en entier.

✅ **BONNE PRATIQUE (P0)** — Quand vous reprenez une affirmation, **conservez son mode**. Si la source évalue, vous rapportez une évaluation ; si la source observe, vous rapportez une observation. Et citez la source précisément : *« [éditeur] évalue avec une confiance modérée que… »* est infiniment plus utile que *« il apparaît que… »*.

## 4.7 ⚠️ Comment ces axiomes sont violés en pratique

Les six violations, dans l'ordre où on les rencontre :

| Axiome | Violation typique | Où on la trouve |
|---|---|---|
| Observer ≠ conclure | Verbes d'intention dans une section de faits | Partout, y compris dans des rapports officiels |
| Corrélation ≠ causalité | Trois victimes d'un secteur → « le secteur est ciblé » | Rapports commerciaux, presse spécialisée |
| Absence de preuve | « Nous n'avons rien trouvé, donc l'adversaire est sophistiqué » | Rapports post-incident |
| Périssabilité | Un rapport de 2027 cité en 2029 au présent | Notes internes, présentations |
| Analyse ≠ description | Dix pages de faits, aucune conclusion | Produits internes de fonctions immatures |
| Source ≠ fait | Une évaluation modérée recopiée comme un fait établi | **Toute la chaîne de reprise, du premier au dernier maillon** |

## 4.8 🔬 Mini-lab 1 — Repérer les six violations

**Objectif** — Identifier les violations d'axiomes dans un produit réel et les corriger.
**Durée** 30 min · **Difficulté** 🟢 débutant · **Prérequis** §4.1 à §4.6 · **Livrable** version corrigée du texte
**Compétences validées** — ✔ séparer observation et déduction ✔ repérer un verbe d'intention ✔ identifier une corrélation prise pour une cause ✔ détecter une perte de mode dans une reprise de source ✔ dater une évaluation

**Le texte à analyser** — extrait d'une note interne fictive, huit phrases numérotées :

> **(1)** Le 3 novembre, notre passerelle d'accès distant a été prise pour cible par un acteur cherchant à obtenir un accès initial. **(2)** Douze tentatives d'authentification ont échoué entre 02 h 50 et 03 h 40 sur des comptes inexistants. **(3)** L'adresse source appartient à un fournisseur d'infrastructure à la demande et apparaît dans deux publications récentes. **(4)** Selon ces publications, il est établi que le groupe TEMPEST-14 mène une campagne contre le secteur de la santé. **(5)** Trois établissements de santé européens ont été victimes de rançongiciels en six semaines, ce qui confirme le ciblage sectoriel. **(6)** Nos recherches dans les journaux n'ont mis en évidence aucune compromission, l'adversaire est donc soit absent, soit particulièrement discret. **(7)** Le mode opératoire correspond à celui décrit dans un rapport de référence sur ce groupe. **(8)** Nous recommandons un renforcement de la surveillance.

**Consigne** : identifiez la violation dans chaque phrase concernée, nommez l'axiome, et proposez une reformulation.

---

**Corrigé commenté**

| # | Violation | Axiome | Reformulation |
|---|---|---|---|
| **(1)** | *Prise pour cible*, *acteur cherchant à obtenir* : trois déductions présentées comme des observations — qu'il y ait un acteur, qu'il cible, qu'il cherche un accès initial | **4.1** | *« Notre passerelle a fait l'objet d'une activité d'authentification anormale. »* La déduction va en section évaluation |
| **(2)** | Aucune. C'est une observation correcte, datée, bornée | — | À conserver telle quelle — c'est le modèle |
| **(3)** | Aucune violation, mais **une information manquante** : ces deux publications sont-elles indépendantes ? | 4.6 *(en germe)* | Ajouter : *« indépendance des deux sources à vérifier »* |
| **(4)** | *Il est établi que* : la source dit « selon ces publications », donc rapporte une évaluation. Le mode a été perdu | **4.6** | *« Ces publications évaluent — avec un niveau de confiance qu'elles ne précisent pas — que… »* |
| **(5)** | *Ce qui confirme* : trois victimes du même secteur ne confirment rien. Elles sont compatibles avec un ciblage sectoriel **et** avec l'exploitation massive d'un produit commun | **4.2** | *« Trois établissements ont été victimes en six semaines. Cette concomitance est compatible avec un ciblage sectoriel comme avec l'exploitation d'un composant commun ; nous n'avons pas d'élément pour trancher. »* |
| **(6)** | *L'adversaire est donc soit absent, soit particulièrement discret* : conclusion tirée du vide. La troisième possibilité — nous n'avons pas les capteurs — est omise | **4.3** | *« Nos recherches n'ont pas mis en évidence de compromission. Nos journaux couvrent 30 jours et ne tracent pas [X] ; cette absence ne permet donc pas de conclure. »* |
| **(7)** | *Correspond à* : une similarité présentée comme une identification. Et *rapport de référence* n'est pas une source citable | **4.6** | *« Le mode opératoire présente des similarités avec celui décrit dans [référence précise, date]. »* Et **aucune** conclusion d'attribution — voir chapitre 13 |
| **(8)** | Recommandation sans évaluation préalable ni horizon | **4.5, 4.4** | La note ne contient aucune évaluation calibrée : elle enchaîne des faits et une recommandation. Ajouter une section d'évaluation, et dater : *« évaluation au 5 novembre 2029, réexamen sous 30 jours »* |

**Le score** : six violations sur huit phrases. Ce n'est pas une note particulièrement mauvaise — c'est une note ordinaire, et vous en lirez beaucoup de ce type.

**Les deux erreurs attendues chez le lecteur**

1. Considérer la phrase (2) comme insuffisante parce qu'elle « ne conclut rien ». C'est au contraire la seule phrase parfaitement écrite : elle est dans la section faits, et son rôle est d'observer.
2. Corriger la phrase (5) en supprimant la conclusion sans proposer d'explication alternative. Le travail d'analyse ne consiste pas à retirer les conclusions, mais à les mettre en concurrence.

## 4.9 🔴 FIL ROUGE — juin 2029 : Nour relit sa première note

Après l'épisode du redécoupage (§3.8), Claire Nadeau demande à Nour un exercice inhabituel : relire sa note du 22 mai avec les six axiomes en main, et marquer chaque phrase qui n'y résiste pas.

Nour y passe deux heures. Le résultat la surprend.

| Constat | Nombre |
|---|---|
| Phrases contenant un verbe d'intention en section factuelle | 9 |
| Affirmations reprises d'une source en ayant perdu son mode | **4** |
| Conclusions tirées d'une concomitance | 2 |
| Évaluations sans date de réexamen | Toutes |
| Sections indiquant ce qui invaliderait l'analyse | **0** |

**Les quatre affirmations qu'elle ne peut pas justifier** sont les plus instructives. Toutes proviennent de la même mécanique : elle a lu trois publications, formé une image cohérente, et écrit cette image — sans revenir vérifier ce que chaque source disait exactement, ni avec quelle prudence.

En remontant, elle découvre que **deux des trois publications citaient la même source primaire**. Son « recoupement » n'en était pas un.

**Ce qu'elle en tire**, et qu'elle écrit dans son carnet :

> *Je n'ai pas menti et je n'ai pas été négligente. J'ai fait ce que fait tout le monde : j'ai résumé. Le problème est que résumer, c'est perdre le mode. Et perdre le mode, c'est transformer une prudence en certitude sans s'en apercevoir.*

**Ce que Claire décide.** Pas un contrôle supplémentaire — une **relecture croisée** : à partir de juillet, tout produit destiné à sortir d'HELIOMED est relu par une seconde personne, avec une seule consigne, les six axiomes en main. Dix minutes par produit. C'est le chapitre 12.

**Livrable de l'épisode.** Une grille de relecture d'une demi-page — les six axiomes, une case par phrase suspecte. Elle figure en annexe C.

→ La suite en 🔴 §5.6, avec la première semaine de Nour racontée heure par heure — et ce qu'elle révèle de la répartition réelle du temps.

## Synthèse mentale du chapitre 4

Six énoncés simples éliminent l'essentiel des mauvais raisonnements. Observer n'est pas conclure : l'interprétation arrive collée au fait, et il faut un effort délibéré pour les séparer — le test consiste à remplacer le verbe par « nous observons ». La corrélation mord particulièrement fort en CTI, où les coïncidences sont abondantes : trois victimes d'un secteur peuvent être trois clients d'un même fournisseur. L'absence appelle une question sur votre capacité d'observation, jamais une conclusion sur le réel — ai-je cherché au bon endroit, avec les bons capteurs, assez longtemps. Tout renseignement se périme, et un produit doit porter son horizon de validité, pas seulement sa date. Une analyse est une hypothèse argumentée et révisable : décrire sans conclure n'est pas de la prudence, c'est une analyse absente. Enfin, une source n'est pas un fait, et la violation est invisible : elle se produit au moment où l'on recopie en perdant le mode, transformant une évaluation prudente en certitude établie.

**Trois questions de vérification**

1. « Le groupe X cible le secteur bancaire. » Cette phrase peut-elle figurer dans une section de faits observés ? Justifiez, et proposez la reformulation.
2. Une recherche dans vos journaux ne trouve aucune trace de compromission. Quelles trois questions posez-vous avant d'en tirer la moindre conclusion ?
3. Vous reprenez une affirmation d'un rapport d'éditeur dans votre propre note. Qu'est-ce qui se perd si vous n'y prenez pas garde, et pourquoi cette perte est-elle invisible ?

→ **Chapitre 5 — Ce que fait réellement un analyste** : une journée heure par heure, et la part surprenante du temps consacrée à autre chose que la technique.

---
