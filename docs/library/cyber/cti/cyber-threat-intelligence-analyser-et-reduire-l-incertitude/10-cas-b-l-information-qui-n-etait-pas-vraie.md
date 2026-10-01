---
title: Cas B — L'information qui n'était pas vraie
source: Cyber/01 CTI & renseignement/Menace cyber/Cyber Threat Intelligence — analyser et réduire l'incertitude.md
note: Cyber Threat Intelligence — analyser et réduire l'incertitude
up:
- - Cyber Threat Intelligence — analyser et réduire l'incertitude
  - index.md
---

> **Format** — Cas de rétractation. Durée : **2 h**.
> **Livrables** : reconstitution de chaîne · note de rétractation interne · communication client · retour d'expérience analytique.
> **Prérequis** : chapitres 4, 9, 10, 12, 35.

## B.1 Le dossier

**Vous êtes analyste CTI** dans un groupe de 1 400 personnes du secteur de l'énergie. Nous sommes le **3 mars**. Les faits qui suivent se sont déroulés sur cinq semaines, et vous les reconstituez.

### Artefact 1 — le point de départ, 22 janvier

> **Rapport d'un fournisseur de renseignement — abonnement souscrit en 2030 — 22 janvier**
>
> *« Notre équipe a identifié une campagne visant le secteur de l'énergie en Europe occidentale. Parmi les organisations dont l'infrastructure a été observée dans le périmètre de reconnaissance de l'acteur figure [VOTRE ORGANISATION].*
>
> *Nous recommandons un renforcement immédiat de la surveillance des accès distants. »*

### Artefact 2 — ce qui a été fait, du 23 janvier au 6 février

```
23 janv.  Évaluation produite en 4 h. Conclusion : "très probable que
          nous soyons ciblés". Confiance : non exprimée.
23 janv.  Alerte émise. Cellule constituée.
24-31 j.  Recherche rétrospective sur 90 jours : 5 jours-homme.
          Aucune activité anormale identifiée.
27 janv.  Restriction des accès distants aux plages d'adresses connues.
          14 collaborateurs en déplacement impactés.
30 janv.  Deux projets décalés pour libérer l'équipe.
3 févr.   Information du comité de direction.
5 févr.   Un grand compte informé "par transparence" que nous faisons
          l'objet d'une campagne de reconnaissance.
6 févr.   Levée de la restriction. Coût estimé : 23 000 €.
```


### Artefact 3 — ce que vous découvrez le 28 février

En préparant le retour d'expérience trimestriel, vous relisez le rapport du 22 janvier et cherchez sa base. Vous écrivez au fournisseur.

> **Réponse du fournisseur, 2 mars**
>
> *« La mention de votre organisation provient de l'observation, dans un jeu de données de reconnaissance attribué à cet acteur, d'une adresse appartenant à une plage annoncée par votre fournisseur d'hébergement.*
>
> *Nous ne sommes pas en mesure de confirmer que cette adresse vous était attribuée à la date de l'observation. Notre formulation aurait dû être plus prudente. »*

### Artefact 4 — vérification faite le 3 mars

```
Adresse concernée : appartenait à une plage d'hébergement mutualisé.
Attribuée à votre organisation : du 12 mars 2029 au 8 novembre 2030.
Date de l'observation citée : 14 décembre 2030.
                              → 5 semaines APRÈS la fin d'attribution.
```


## B.2 Les questions

| # | Question |
|---|---|
| 1 | Reconstituez la chaîne de provenance et identifiez le point de rupture. |
| 2 | Quelles étapes du chapitre 10 auraient évité les 23 000 € ? |
| 3 | Où le calibrage a-t-il manqué, précisément ? |
| 4 | Rédigez la note de rétractation interne. |
| 5 | Que dites-vous au grand compte informé le 5 février ? |
| 6 | Conduisez le retour d'expérience analytique. |
| 7 | Quelles mesures pérennes ? |

## B.3 Corrigé — la chaîne de provenance

```
Une adresse figure dans un jeu de données de reconnaissance
        │  observation réelle, non contestée
        ▼
L'adresse appartient à une plage d'hébergement mutualisé
        │  ← PREMIÈRE RUPTURE : rien n'établit qui l'utilisait
        ▼
Le fournisseur associe l'adresse à votre organisation
        │  ← DEUXIÈME RUPTURE : attribution périmée de 5 semaines
        ▼
Le rapport écrit : "figure dans le périmètre de reconnaissance"
        │  ← TROISIÈME RUPTURE : perte du mode, l'hypothèse devient constat
        ▼
Votre évaluation : "très probable que nous soyons ciblés"
        │  ← QUATRIÈME RUPTURE : reprise sans vérification, calibrage absent
        ▼
Alerte, mobilisation, 23 000 €, et information d'un client
```


**Le point de rupture décisif est le deuxième** : l'adresse n'était plus attribuée à l'organisation cinq semaines avant l'observation. Cette vérification demandait **une requête et dix minutes**.

**Ce que le cas illustre** : il ne s'agit pas de circularité (§10.4) — il n'y a qu'une source. Il s'agit d'une **chaîne de provenance non remontée** (§10.3), et de la quatrième question qui s'arrête toujours sur du vide : *sur quoi la source fonde-t-elle son affirmation ?*

## B.4 Corrigé — ce qui aurait évité les 23 000 €

| Étape du chapitre 10 | Ce qu'elle aurait produit | Coût |
|---|---|---|
| **§10.3 — remonter la chaîne** | La question « sur quoi repose la mention ? » posée le 23 janvier | 5 min pour écrire |
| **§10.1 — fiabilité ≠ crédibilité** | Le fournisseur est fiable ; **cette affirmation précise** ne l'est pas nécessairement | 0 |
| **§10.6 — évaluer la publication** | La méthodologie n'est pas décrite, le niveau de confiance n'est pas exprimé | 10 min |
| **§10.8 — éléments propres apportés** | Une seule mention, aucun élément corroborant | 0 |

**Le geste unique qui aurait suffi** : écrire au fournisseur le 23 janvier, avant d'alerter. Cinq minutes, une réponse en quelques jours — et l'alerte aurait été remplacée par une vérification.

⚠️ **La difficulté réelle** : le 23 janvier, l'organisation est nommée dans un rapport payant. La pression à agir est maximale, et attendre une réponse paraît irresponsable. **C'est précisément la situation que le §29.4 traite** : gravité élevée, confiance faible non exprimée. La bonne décision était *vérifier en priorité*, pas *mobiliser*.

## B.5 Corrigé — le calibrage manquant

**Ce qui a été écrit** : *« très probable que nous soyons ciblés »*.

**Ce qui manquait** :

| Élément | Effet de son absence |
|---|---|
| **Le niveau de confiance** | Le lecteur ignore que l'évaluation repose sur une source unique non vérifiée |
| **La base** | Personne ne sait sur quoi repose le « très probable » |
| **La clause de réfutation** | Personne ne sait ce qui la renverserait — or c'était vérifiable |
| **La distinction ciblé / observé** | « Figurer dans un périmètre de reconnaissance » ≠ « être ciblé » |

**La quatrième est celle qui aurait le plus changé la décision.** Même si l'attribution d'adresse avait été correcte, figurer dans un jeu de reconnaissance signifie que votre adresse a été balayée — ce qui est le cas de toute adresse publique, en permanence.

**L'évaluation qu'il aurait fallu écrire** :

> *Nous estimons **aussi probable qu'improbable** que notre infrastructure ait fait l'objet d'une reconnaissance par cet acteur — **confiance faible** : source unique, base de l'affirmation non communiquée, et « reconnaissance » ne constitue pas un ciblage.*
>
> *Ce qui trancherait : la nature de l'observation, et la confirmation que l'adresse citée nous était attribuée à la date concernée.*
>
> *Nous recommandons une vérification auprès du fournisseur avant toute mobilisation.*

**Le même dossier, correctement calibré, produit une décision à zéro euro.**

## B.6 Corrigé — la note de rétractation interne

> **Objet : révision de l'évaluation du 23 janvier — campagne visant le secteur de l'énergie**
>
> **Notre évaluation du 23 janvier était erronée.** Nous avions estimé très probable que notre organisation soit ciblée par une campagne de reconnaissance. Cette conclusion ne tient pas.
>
> **Ce que nous avons établi.** La mention de notre organisation dans le rapport du 22 janvier repose sur l'observation d'une adresse appartenant à une plage d'hébergement mutualisé. Cette adresse ne nous était plus attribuée depuis le 8 novembre 2030, soit cinq semaines avant l'observation citée. Le fournisseur a confirmé le 2 mars ne pas être en mesure d'établir l'attribution à la date concernée.
>
> **Ce qui a manqué de notre part.** Nous n'avons pas remonté la chaîne de provenance avant d'agir, et nous n'avons pas exprimé de niveau de confiance. Une question écrite au fournisseur, le 23 janvier, aurait produit la même réponse en quelques jours et évité la mobilisation.
>
> **Ce que cela a coûté.** Environ 23 000 € en temps mobilisé, deux projets décalés de trois semaines, et l'information d'un client sur une base erronée.
>
> **Ce que nous changeons.** *(voir §B.9)*
>
> **Ce qui reste vrai.** La campagne visant le secteur de l'énergie est réelle et documentée. Nous n'avons simplement aucun élément indiquant qu'elle nous concerne.

⚠️ **Les trois choses que cette note fait, et qui la rendent acceptable** : elle affirme l'erreur en première phrase · elle établit les faits sans se dérober · elle distingue ce qui est faux de ce qui reste vrai.

## B.7 Corrigé — la communication au grand compte

**La difficulté** : vous l'avez informé le 5 février « par transparence ». Ne rien dire est la pire option — il l'apprendra, ou il continuera à croire une information fausse.

> **Objet : précision sur notre information du 5 février**
>
> Le 5 février, nous vous avons informés qu'un signalement suggérait que notre infrastructure faisait l'objet d'une reconnaissance dans le cadre d'une campagne visant notre secteur.
>
> **Cette information n'est pas confirmée, et nous l'écartons.** La vérification que nous avons conduite établit que l'élément à l'origine du signalement concerne une adresse qui ne nous était plus attribuée à la date de l'observation.
>
> Nous n'avons identifié, à ce jour, aucun élément indiquant que notre organisation soit concernée. Les vérifications conduites entre le 24 et le 31 janvier, portant sur quatre-vingt-dix jours, n'ont mis en évidence aucune activité anormale.
>
> Nous avons revu notre processus de vérification des signalements externes. Nous restons à votre disposition.

**Ce que la dernière phrase du troisième paragraphe apporte** : elle transforme un aveu en démonstration de capacité. La recherche rétrospective a été faite, et son résultat est utile indépendamment de l'erreur d'origine.

## B.8 Corrigé — le retour d'expérience analytique

**La méthode du §35.6, appliquée** :

| Question | Réponse |
|---|---|
| **L'estimation était-elle juste ?** | Non |
| **La confiance était-elle juste ?** | **Non exprimée** — donc implicitement élevée |
| Position dans le tableau du §35.6 | **Estimation fausse + confiance élevée = le pire cas** |
| Quel biais ? | Ancrage sur le nom de l'organisation dans un rapport payant · biais du client — la fonction avait besoin de justifier l'abonnement · absence de recherche d'hypothèse alternative |
| Quelle méthode a manqué ? | La chaîne de provenance (§10.3) et le calibrage (§9) |
| Qu'est-ce qui change dans ma pratique ? | *(§B.9)* |

**Le biais le plus difficile à admettre est le deuxième.** L'abonnement avait été souscrit en 2030 et n'avait produit aucun signalement majeur. Le rapport du 22 janvier était le premier à nommer l'organisation. Il y avait, sans intention consciente, un intérêt à ce qu'il soit important.

C'est le §7.7 — et il opère ici sur le fournisseur autant que sur le destinataire.

## B.9 Corrigé — les mesures pérennes

| # | Mesure | Effet attendu |
|---|---|---|
| **1** | **Toute mention nominative de l'organisation dans une source externe déclenche une remontée de chaîne avant toute action** | C'est la mesure qui aurait tout évité |
| **2** | **Aucune évaluation sans niveau de confiance** — champ obligatoire | §9 |
| **3** | **Aucune alerte sur source unique non vérifiée** — la source unique déclenche une vérification | §27.1, §29.4 |
| **4** | **Toute évaluation destinée à déclencher une action porte une clause de réfutation** | §11.3 |
| **5** | **Communication externe sur une base non vérifiée : interdite** | Le 5 février n'aurait pas dû avoir lieu |
| **6** | Revue trimestrielle du fournisseur, avec les cinq tests du §22.3 | La méthodologie non décrite est un signal |

**La mesure 5 mérite un mot** : informer un client « par transparence » sur une information non vérifiée n'est pas de la transparence, c'est un transfert d'incertitude. La transparence consiste à dire ce qu'on sait, avec son niveau de confiance — ce qui, ici, aurait produit un message très différent.

## B.10 Ce que le cas enseigne

**Trois enseignements, dans l'ordre d'importance** :

1. **Une source unique, fiable, peut transmettre une information fausse.** C'est le §10.1 : fiabilité et crédibilité sont deux axes. Le fournisseur n'a pas menti — il a formulé imprudemment une observation réelle.

2. **Le calibrage absent est ce qui transforme une erreur en catastrophe.** L'évaluation aurait pu être fausse sans conséquence si elle avait porté « confiance faible » : la décision aurait été de vérifier.

3. **Le coût d'une rétractation est très inférieur au coût de ne pas se rétracter.** L'organisation a informé un client sur une base fausse ; la correction, faite rapidement et complètement, a préservé la relation. Une non-correction découverte plus tard l'aurait détruite.

**Le barème** :

| Critère | Pts |
|---|---|
| Reconstituer la chaîne et identifier la deuxième rupture | 20 |
| Identifier le geste unique qui aurait suffi | 15 |
| Distinguer « reconnaissance » de « ciblage » | 15 |
| Note de rétractation affirmant l'erreur en première phrase | 15 |
| Communication client sans dérobade | 10 |
| Retour d'expérience situant le cas dans le tableau du §35.6 | 15 |
| Identifier le biais du client | 10 |

**Élimination** : ne pas corriger l'information transmise au client.

---
