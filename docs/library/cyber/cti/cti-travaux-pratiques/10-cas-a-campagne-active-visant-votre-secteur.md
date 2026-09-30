---
title: Cas A — Campagne active visant votre secteur
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
up:
- - CTI — travaux pratiques
  - index.md
---

> **Format** — Cas de décision sous incertitude et sous pression. Durée : **2 h 30**.
> **Livrables** : évaluation calibrée · décision d'exploitation · bulletin direction · bulletin client.
> **Prérequis** : chapitres 6 à 11, 19, 27, 29.

## A.1 Le dossier

**Vous êtes analyste CTI** dans une entreprise de 900 personnes, fabricant d'équipements industriels, 60 clients dont 12 grands comptes. Nous sommes le **mardi 14 septembre, 9 h 15**.

### Artefact 1 — le message reçu

> **Dispositif de partage sectoriel — Bulletin SEC-2031-0912 — 14/09, 07 h 40 — Diffusion : membres**
>
> *Trois membres du dispositif ont signalé, entre le 28 août et le 11 septembre, des intrusions présentant des caractéristiques communes. Les trois organisations sont des fabricants d'équipements industriels. Le vecteur d'entrée n'est pas établi à ce stade.*
>
> *Éléments communs relevés : utilisation d'un outil d'administration légitime pour le mouvement latéral · exfiltration vers un hébergeur à la demande · absence de chiffrement ou de demande de rançon.*
>
> *Les membres sont invités à renforcer leur vigilance et à signaler toute observation.*

### Artefact 2 — ce que vous savez de votre organisation

```
Secteur              : fabricant d'équipements industriels ✅ correspond
Effectif             : 900 personnes
Sites                : 3 (siège, usine, R&D)
Outil d'administration cité : PRÉSENT — utilisé par l'exploitation
Journalisation       : postes 90 j · annuaire 12 mois · pare-feu 12 mois
                       serveur de fichiers : NON COLLECTÉ
Détection            : 89 règles, couverture testée 33 %
                       mouvement latéral : 44 % · exfiltration : 22 %
Dernier incident     : février, poste compromis, 11 j avant détection
```


### Artefact 3 — le contexte du jour

- Votre RSSI est en déplacement, joignable.
- Le comité de direction se réunit **jeudi 16 à 14 h**.
- Un grand compte a demandé la semaine dernière un point sur votre dispositif de sécurité.
- Vous êtes seul sur la fonction.

## A.2 Les questions, dans l'ordre

| # | Question | Livrable |
|---|---|---|
| 1 | Que faites-vous dans les deux premières heures ? | Actions listées |
| 2 | Quelle information manquante est la plus déterminante ? | — |
| 3 | Formulez trois hypothèses concurrentes. | Matrice |
| 4 | Quelle décision d'exploitation ? | Arbre §29.2 |
| 5 | Rédigez l'évaluation calibrée. | Une page |
| 6 | Que dites-vous au comité de jeudi ? | 10 lignes |
| 7 | Que dites-vous au grand compte qui a demandé un point ? | 8 lignes |
| 8 | Quatre erreurs sont insérées dans le dossier. Lesquelles ? | — |

## A.3 Corrigé — les deux premières heures

**Ce qu'il ne faut pas faire** : alerter. Les conditions du §27.1 ne sont pas réunies — l'applicabilité n'est pas établie, et aucune action n'est identifiée.

**Ce qu'il faut faire, dans cet ordre** :

| Heure | Action | Justification |
|---|---|---|
| 9 h 15 | **Poser la question manquante au dispositif** : quel est le vecteur d'entrée ? | C'est la condition ① du §19.4 |
| 9 h 30 | Vérifier l'applicabilité des éléments connus : l'outil d'administration est-il présent, comment est-il utilisé, par qui | Nœud ① de l'arbre |
| 10 h 00 | Recherche rétrospective sur ce qui est disponible : usages inhabituels de l'outil dans l'annuaire sur 12 mois | Ne coûte rien, peut trancher |
| 10 h 45 | Établir ce qu'on **ne peut pas** vérifier : le serveur de fichiers n'est pas journalisé | §4.3 — l'absence appelle une question sur la capacité d'observation |
| 11 h 00 | Informer le RSSI — **information, pas alerte** | §27.1, condition 3 non remplie |

**La question posée au dispositif est l'action la plus rentable de la matinée.** Elle coûte deux minutes et conditionne tout le reste : sans le vecteur, l'applicabilité ne peut pas être établie.

## A.4 Corrigé — l'information manquante

**Le vecteur d'entrée.** Sans lui :

| Ce qu'on ne peut pas faire | Pourquoi |
|---|---|
| Établir l'applicabilité | On ne sait pas si le chemin existe chez nous |
| Prioriser une remédiation | On ne sait pas quoi corriger |
| Écrire une règle de détection | On ne sait pas quoi chercher en amont |
| Décider d'une mesure d'atténuation | On ne sait pas quoi fermer |

**Ce que l'artefact 1 donne en revanche** : trois éléments de la **phase post-intrusion** — mouvement latéral, exfiltration, absence de rançon. Ils permettent une recherche rétrospective, mais pas une prévention.

⚠️ **La distinction est essentielle** : un bulletin qui décrit ce qui se passe **après** l'entrée permet de chercher, pas de se protéger.

## A.5 Corrigé — les trois hypothèses

| Réf | Hypothèse | Origine |
|---|---|---|
| **H-A** | Ciblage sectoriel des fabricants d'équipements industriels | L'hypothèse spontanée, suggérée par le bulletin |
| **H-B** | Exploitation opportuniste d'un composant ou service commun au secteur | Par mécanisme (§8.3) |
| **H-C** | Compromission d'un prestataire ou fournisseur commun aux trois | Par inversion — **l'hypothèse ennuyeuse** |

**La matrice, avec les éléments disponibles** :

| Élément | H-A | H-B | H-C |
|---|---|---|---|
| Trois victimes du même secteur | `++` | `+` | `+` |
| Intervalle de 15 jours entre la première et la dernière | `+` | `++` | `++` |
| **Absence de chiffrement et de rançon** | `++` | `−` | `0` |
| Outil d'administration légitime employé | `+` | `+` | `++` |
| Exfiltration vers un hébergeur à la demande | `+` | `+` | `+` |
| **Vecteur d'entrée inconnu** | `0` | `0` | `0` |

**La lecture** : l'absence de chiffrement et de demande de rançon est l'élément le plus discriminant du dossier. Elle rend H-B moins probable — une exploitation opportuniste de masse aboutit généralement à une monétisation directe (§16.3). Elle soutient H-A.

**Mais aucune hypothèse n'est éliminée**, et c'est le point : avec cinq éléments dont aucun ne porte sur le vecteur, on ne peut pas trancher.

**Les hypothèses clés à identifier** (§8.6) :

| Présupposé | Vérifié ? | Si faux |
|---|---|---|
| Les trois victimes sont bien du même secteur | ✅ selon le bulletin | — |
| Elles n'ont pas de prestataire commun | ❌ **non vérifié** | H-C deviendrait dominante |
| Le bulletin rapporte tous les cas connus | ❌ non vérifiable | Une victime hors secteur éliminerait H-A |

**La deuxième ligne est celle qui manque**, et c'est exactement l'élément ③ du §8.9 du fil rouge.

## A.6 Corrigé — la décision d'exploitation

**Parcours de l'arbre du §29.2** :

```
① Applicable chez nous ?     → INDÉTERMINÉ (vecteur inconnu)
                                Les éléments post-intrusion, eux, sont applicables
② Exploitable en l'état ?     → Indéterminé
③ Action possible maintenant ? → OUI, partiellement :
                                 recherche rétrospective sur l'outil d'administration
④ Inaction déraisonnable ?     → Non — aucune urgence caractérisée
```


**Décision : DIFFÉRER, avec une action de collecte et une recherche rétrospective.**

| Action | Délai | Porteur |
|---|---|---|
| Question au dispositif sur le vecteur | Immédiat | Vous |
| **Question au dispositif sur l'existence d'un prestataire commun** | Immédiat | Vous |
| Recherche rétrospective sur l'outil d'administration, 12 mois | 48 h | Vous + détection |
| Évaluation de la faisabilité d'une règle sur l'usage anormal de l'outil | 5 j | Détection |
| **Constat écrit** : le serveur de fichiers n'est pas journalisé, donc l'exfiltration ne serait pas détectable | Immédiat | Vous |

⚠️ **La dernière ligne est celle qu'on oublie.** Elle ne répond pas à la question du jour ; elle documente une lacune structurelle que le dossier vient de révéler.

## A.7 Corrigé — l'évaluation calibrée

> **Objet** : campagne signalée contre des fabricants d'équipements industriels — évaluation au 14 septembre
>
> **Nous estimons *aussi probable qu'improbable* que notre organisation entre dans le périmètre de cette campagne — *confiance faible*.** Cette faible confiance tient à l'absence d'information sur le vecteur d'entrée, qui empêche d'établir notre applicabilité.
>
> **Ce que nous observons.** Un bulletin sectoriel du 14 septembre signale trois intrusions chez des fabricants d'équipements industriels entre le 28 août et le 11 septembre. Les éléments communs rapportés concernent la phase post-intrusion : emploi d'un outil d'administration légitime, exfiltration vers un hébergeur à la demande, absence de chiffrement et de demande de rançon. **Le vecteur d'entrée n'est pas établi.**
>
> **Ce que nous en estimons.** Trois hypothèses ont été envisagées : un ciblage sectoriel, une exploitation opportuniste d'un composant commun, ou la compromission d'un prestataire partagé. L'absence de monétisation directe est l'élément le plus discriminant et soutient l'hypothèse d'un ciblage. Aucune hypothèse n'est cependant éliminée, faute d'information sur le vecteur et sur l'existence éventuelle d'un prestataire commun aux trois victimes.
>
> **Ce qui trancherait.** Le vecteur d'entrée employé chez les trois victimes · l'existence d'un prestataire ou fournisseur commun · la survenue d'un cas hors secteur.
>
> **Ce qui invaliderait cette évaluation.** Une quatrième victime n'appartenant pas au secteur éliminerait l'hypothèse de ciblage · l'identification d'un prestataire commun aux trois la rendrait secondaire.
>
> **Ce que nous ne savons pas.** Nos journaux ne couvrent pas le serveur de fichiers. Une exfiltration comparable à celle décrite ne serait **pas détectable** chez nous, ni a posteriori. Cette lacune est structurelle et dépasse le cadre de cette évaluation.
>
> **Ce que nous recommandons.** Deux questions au dispositif sectoriel (immédiat, sans coût) · une recherche rétrospective sur l'usage de l'outil d'administration (48 h, 1 jour-homme) · l'évaluation d'une collecte des journaux du serveur de fichiers (à instruire, hors urgence).
>
> *Évaluation au 14 septembre. Réexamen à réception des réponses du dispositif, ou sous 7 jours.*

## A.8 Corrigé — le comité de jeudi

> **Campagne signalée dans notre secteur — point d'information**
>
> Un dispositif de partage sectoriel a signalé mardi trois intrusions chez des fabricants d'équipements industriels au cours des trois dernières semaines.
>
> **Sommes-nous concernés ?** Nous ne pouvons pas l'établir : le vecteur d'entrée n'est pas connu. Nous avons posé la question et attendons une réponse.
>
> **Ce que nous avons fait.** Une recherche rétrospective sur douze mois n'a rien mis en évidence. Une évaluation complète est disponible.
>
> **Ce que nous avons découvert au passage.** Nos journaux ne couvrent pas notre serveur de fichiers. Une exfiltration de données comparable à celle décrite ne serait pas détectable chez nous. **C'est le point que nous portons à votre attention** ; il dépasse cette campagne.
>
> **Ce que nous attendons de vous.** Rien à ce stade sur la campagne. Sur la journalisation du serveur de fichiers, nous demanderons un arbitrage lorsque nous aurons chiffré la mesure.

⚠️ **Ce qui fait la valeur de cette note** : elle transforme un événement extérieur incertain en constat interne actionnable. C'est ce que la direction peut réellement décider.

## A.9 Corrigé — le grand compte

> **Objet : votre demande de point sur notre dispositif de sécurité**
>
> Nous avons pris connaissance d'un signalement sectoriel concernant des intrusions chez des fabricants d'équipements industriels. Nous n'avons identifié aucune activité comparable dans notre environnement, sur la base d'une recherche rétrospective portant sur douze mois.
>
> Nous ne sommes pas en mesure d'établir si nous entrons dans le périmètre de cette campagne, le vecteur d'entrée n'ayant pas été communiqué. Nous avons demandé cette information.
>
> Nous restons disponibles pour un échange, et nous vous informerons si des éléments nouveaux nous concernaient.

⚠️ **Ce qui n'y figure pas** : nos hypothèses, notre lacune de journalisation, nos taux de couverture, et le nom du dispositif sectoriel. Ce sont des informations internes — §26.7.

## A.10 Corrigé — les quatre erreurs insérées

| # | Erreur | Où | Effet |
|---|---|---|---|
| **1** | **Le bulletin ne donne pas le vecteur d'entrée** | Artefact 1 | C'est l'information la plus déterminante, et son absence n'est pas signalée comme une lacune par l'émetteur |
| **2** | **« Les trois organisations sont des fabricants »** — aucune mention d'une vérification d'exhaustivité | Artefact 1 | Le dispositif ne dit pas s'il connaît d'autres victimes hors secteur (§8.9) |
| **3** | **Le serveur de fichiers n'est pas journalisé** | Artefact 2 | La lacune est présente dans le dossier et facile à ne pas voir — c'est celle qui compte le plus |
| **4** | **La couverture de détection sur l'exfiltration est de 22 %** | Artefact 2 | Le dossier contient l'information disant que vous ne détecteriez pas ce qui est décrit |

**Les erreurs 3 et 4 se renforcent** : le dossier vous dit deux fois, de deux façons différentes, que vous ne verriez pas cette campagne si elle vous touchait. Un analyste qui se concentre sur « sommes-nous ciblés ? » les manque toutes les deux.

## A.11 Barème

| Critère | Pts |
|---|---|
| Poser la question du vecteur en premier | 15 |
| Ne pas alerter, et justifier par la condition 3 | 10 |
| Trois hypothèses dont une par inversion | 15 |
| Identifier le présupposé du prestataire commun | 10 |
| **Relever la lacune de journalisation** | **20** |
| Évaluation calibrée avec confiance faible justifiée | 15 |
| Note comité transformant l'incertitude en constat actionnable | 10 |
| Bulletin client sans information interne | 5 |

**Seuil** : 70/100. **Élimination** : alerter, ou conclure au ciblage sur la base du bulletin seul.

## A.12 Variante — une seconde source contredit la première

*Le 16 septembre, un éditeur publie une analyse portant sur la même campagne, et mentionne une quatrième victime : un distributeur de matériel électronique.*

**Ce que cela change** :

| Élément | Effet |
|---|---|
| H-A — ciblage sectoriel | **Fortement contredit** — une victime hors secteur |
| H-B — exploitation opportuniste | Renforcée |
| H-C — prestataire commun | Renforcée, si le distributeur partage un prestataire |
| Votre évaluation | À réviser, et **c'était écrit dans la clause de réfutation** |

**Ce que la variante enseigne** : la clause de réfutation du §A.7 n'était pas une précaution rhétorique. Elle avait nommé exactement l'observation qui allait se produire — et sa présence rend la révision naturelle plutôt qu'embarrassante.

**La note de révision, deux lignes** :

> *Notre évaluation du 14 septembre est révisée : l'hypothèse d'un ciblage sectoriel est écartée, une quatrième victime n'appartenant pas au secteur ayant été documentée le 16 septembre. Nous estimons désormais probable une exploitation opportuniste d'un composant commun — confiance moyenne.*

---
