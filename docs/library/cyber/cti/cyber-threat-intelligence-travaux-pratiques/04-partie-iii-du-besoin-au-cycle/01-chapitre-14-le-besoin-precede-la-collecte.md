---
title: Chapitre 14 — Le besoin précède la collecte
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE III — Du besoin au cycle
  - index.md
---

## 14.1 Les besoins prioritaires de renseignement

**Ce que c'est** : une question, formulée par un décideur identifié, à laquelle la fonction CTI s'engage à répondre, et qui éclaire une décision qu'il doit prendre.

**Les cinq propriétés d'un besoin bien formulé** :

| Propriété | Test | Contre-exemple |
|---|---|---|
| **C'est une question** | Elle se termine par un point d'interrogation | « La menace rançongiciel » — c'est un sujet |
| **Elle a un demandeur nommé** | Une personne, pas une fonction | « la direction » |
| **Elle éclaire une décision** | On peut nommer la décision | « pour information » |
| **La réponse est concevable** | On peut imaginer à quoi elle ressemblerait | « quelles sont les menaces ? » |
| **Elle a une échéance** | La décision a une date | Aucune |

**La transformation d'un sujet en besoin**, sur trois exemples réels :

| Sujet exprimé | Besoin reformulé |
|---|---|
| « La menace rançongiciel » | *Quels vecteurs d'entrée sont employés contre les organisations comparables à la nôtre, et lesquels sont ouverts chez nous ?* |
| « L'intelligence artificielle » | *L'emploi de modèles de langage par des attaquants modifie-t-il les mesures de défense que nous devons prendre en 2031 ?* |
| « Nos concurrents se font attaquer » | *Ce qui est arrivé à ces trois organisations est-il transposable chez nous, et par quel chemin ?* |

**Remarquez ce que la reformulation ajoute** : un périmètre, un critère de réponse, et une décision implicite. Les trois manquaient au sujet.

## 14.2 Obtenir un besoin d'un décideur qui ne sait pas ce qu'il veut

C'est la situation normale, et il ne faut pas s'en étonner : personne ne sait exprimer un besoin de renseignement s'il n'en a jamais reçu.

**La question qui ne fonctionne pas** : *« de quoi avez-vous besoin ? »*. Elle produit soit « tout », soit « je ne sais pas », soit un sujet.

**Les trois questions qui fonctionnent**, dans cet ordre :

```
1. « Quelles décisions devez-vous prendre dans les six prochains mois,
    et sur lesquelles vous manque-t-il quelque chose ? »

2. « Qu'est-ce qui vous a surpris cette année ? »

3. « Qu'est-ce que vous feriez différemment si vous saviez X ? »
```


**Pourquoi la deuxième fonctionne si bien** : une surprise signale un angle mort, et un angle mort est un besoin de renseignement qui ne s'est pas exprimé. Elle produit régulièrement les besoins les plus utiles, parce qu'elle contourne la difficulté de formuler ce qu'on ignore.

**La troisième est un test.** Si la réponse est « rien », le besoin n'en est pas un — c'est une curiosité. Ce n'est pas illégitime, mais cela ne justifie pas d'y consacrer une capacité rare.

🎯 **ET MAINTENANT ?**
*Votre direction générale vous dit : « j'aimerais être tenue au courant de ce qui se passe ». Que faites-vous ?*
**Réponse** : vous ne produisez pas de lettre d'information — ce serait de la veille (§1.4), et elle ne sera pas lue au bout de trois mois. Vous posez la deuxième question : *« qu'est-ce qui vous a surpris cette année ? »*. Les réponses typiques — « qu'un concurrent soit à l'arrêt trois semaines », « qu'un client nous demande des comptes sur notre sécurité », « que ça coûte si cher » — sont trois besoins réels, exprimables et actionnables. Vous en retenez deux.

## 14.3 Du besoin à la question renseignement

Un besoin exprimé par un décideur est rarement traitable tel quel. Il faut le décomposer en **questions renseignement** — des questions auxquelles une source peut répondre.

**La décomposition, sur un exemple :**

> **Besoin (Malik Ferhaoui, exploitation)** : *sur quoi corriger en premier quand j'ai trente constats et deux semaines ?*

| # | Question renseignement | Source envisagée | Fréquence |
|---|---|---|---|
| 1 | Quelles vulnérabilités affectant nos produits sont **activement exploitées** ? | Catalogues d'exploitation avérée, avis d'éditeurs | Quotidienne |
| 2 | Quelles vulnérabilités sont exploitées **contre notre secteur** ? | Dispositif sectoriel, publications | Hebdomadaire |
| 3 | Quels vecteurs d'entrée sont employés dans les incidents comparables ? | Publications, retours d'incidents | Mensuelle |
| 4 | Quel délai observe-t-on entre publication et exploitation, par famille de produit ? | Analyse propre, sur historique | Trimestrielle |

**Ce que la décomposition révèle** : un besoin unique produit quatre questions, de fréquences différentes, appelant des sources différentes. C'est cela qu'on appelle un **plan de collecte**.

⚠️ **PIÈGE — la question sans réponse concevable**
*« Sommes-nous ciblés ? »* est un besoin légitime et une mauvaise question renseignement : aucune source ne répond directement. Elle se décompose en questions traitables — *observons-nous une activité dirigée contre nos actifs ? · les organisations comparables signalent-elles quelque chose ? · nos produits sont-ils mentionnés quelque part ?* Le travail de décomposition est ce qui rend le besoin traitable.

## 14.4 Le plan de collecte

**Ce que c'est** : le tableau qui relie chaque question à une source, une fréquence et un responsable.

🧪 **EN PRATIQUE — le format**

| Question | Besoin d'origine | Demandeur | Source | Fréquence | Coût | Couverte ? |
|---|---|---|---|---|---|---|
| Vulnérabilités activement exploitées sur nos produits | Priorisation MCS | M. Ferhaoui | Catalogue public + avis éditeurs | Quotidienne | Gratuit | ✅ |
| Vulnérabilités exploitées contre notre secteur | Priorisation MCS | M. Ferhaoui | Dispositif sectoriel | Hebdomadaire | Adhésion | ⚠️ partielle |
| Mentions de nos produits | Sécurité produit | Y. Prigent | Surveillance ciblée | Hebdomadaire | ? | ❌ |

**Ce que le tableau produit immédiatement**, et c'est sa vraie utilité : **la colonne « couverte ? »**. Elle révèle en une lecture ce qui est déjà satisfait par des sources gratuites, ce qui est partiel, et ce qui ne l'est pas du tout.

**L'observation qui surprend systématiquement** : dans une organisation qui n'a jamais fait cet exercice, une majorité des besoins exprimés sont **déjà couverts** par des sources gratuites qu'elle reçoit sans les exploiter. Le manque n'est presque jamais un manque de sources — c'est un manque de rapprochement entre les sources et les questions.

✅ **BONNE PRATIQUE (P0)** — Construisez le plan de collecte **avant** toute souscription. Il montre où le besoin réel se situe, et il évite de payer pour ce que vous recevez déjà.

## 14.5 Réviser les besoins

Un besoin n'est pas éternel. Trois régimes de révision :

| Régime | Fréquence | Déclencheur |
|---|---|---|
| **Révision périodique** | Semestrielle | Calendrier |
| **Révision par événement** | À la demande | Incident, changement d'activité, exigence client, nouveau projet |
| **Révision par obsolescence** | Continue | Un besoin dont on n'a pas produit de réponse depuis six mois : est-il encore réel ? |

**Le troisième est le plus utile et le moins pratiqué.** Un besoin qui n'a rien produit depuis six mois est soit satisfait, soit mal formulé, soit abandonné par son demandeur — et dans les trois cas, le savoir libère de la capacité.

## 14.6 ⚠️ La collecte tous azimuts, et pourquoi elle rassure

**Le mécanisme** : faute de savoir ce qu'on cherche, on cherche tout. C'est confortable pour trois raisons, toutes mauvaises.

| Raison | Ce qu'elle masque |
|---|---|
| **L'activité est visible** | On peut montrer des flux, des volumes, des tableaux de bord |
| **L'échec est invisible** | On ne peut pas rater ce qu'on ne cherchait pas explicitement |
| **La décision est reportée** | Choisir ce qu'on ne suivra pas est inconfortable ; ne pas choisir l'évite |

**Le coût réel**, lui, est différé et considérable : une capacité saturée, des destinataires noyés, et l'incapacité à répondre à une question précise le jour où elle est posée — parce qu'on n'a jamais organisé la collecte autour d'elle.

> **Le test de la collecte tous azimuts** : demandez à la fonction *quelles sources avez-vous décidé de ne pas suivre, et pourquoi ?* Si la liste est vide, il n'y a pas de plan de collecte — il y a une accumulation.

## 14.7 ✅ Livrable — La matrice besoins × sources

Document d'une à deux pages, révisé semestriellement.

**Section 1 — Les besoins**

| Réf | Question | Demandeur | Décision éclairée | Échéance | Niveau | Statut |
|---|---|---|---|---|---|---|
| B-01 | | | | | strat/opé/tact | actif / satisfait / abandonné |

**Section 2 — Les questions renseignement**

| Réf | Rattachée à | Question | Réponse concevable ? |
|---|---|---|---|

**Section 3 — Le plan de collecte**

| Question | Source | Type | Fréquence | Coût annuel | Responsable | **Couverte ?** |
|---|---|---|---|---|---|---|

**Section 4 — Ce que nous avons décidé de ne pas suivre**

| Sujet écarté | Motif | Date | À réexaminer |
|---|---|---|---|

**La section 4 est celle qui prouve qu'un plan existe.** Elle est aussi celle qui protège la fonction : le jour où un sujet non suivi devient important, la décision de ne pas le suivre était écrite, datée et motivée — ce n'était pas un oubli.

## 14.8 🔬 Mini-lab 5 — Transformer des demandes en plan de collecte

**Objectif** — Reformuler des demandes floues en besoins, les décomposer, et construire un plan.
**Durée** 45 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §14.1 à §14.4 · **Livrable** matrice besoins × sources, sections 1 à 4
**Compétences validées** — ✔ transformer un sujet en question ✔ identifier la décision sous-jacente ✔ décomposer en questions traitables ✔ repérer ce qui est déjà couvert ✔ écarter explicitement

**Les six demandes recueillies** dans une organisation de 900 personnes, secteur industriel, avec une équipe de détection interne et un dispositif de MCS mature :

```
① Direction générale
   « J'aimerais savoir si on est plus exposés que les autres. »

② RSSI
   « Il me faut de quoi défendre mon budget 2031 au comité de novembre. »

③ Responsable de l'exploitation
   « Quand je vois quarante alertes de vulnérabilités, je ne sais pas
     par où commencer. »

④ Responsable de la détection
   « Je voudrais savoir ce que je ne détecte pas. »

⑤ Directeur industriel
   « Est-ce que ce qui est arrivé à [concurrent] peut nous arriver ? »

⑥ Directeur des achats
   « On me demande d'évaluer la sécurité de nos fournisseurs, je ne sais
     pas comment m'y prendre. »
```


**Consigne** : reformulez chaque demande en besoin, indiquez le niveau et la décision éclairée, décomposez-en deux en questions renseignement, et identifiez ce que vous décidez de ne pas suivre.

---

**Corrigé commenté**

**Section 1 — Les besoins reformulés**

| Réf | Demande | Besoin reformulé | Niveau | Décision éclairée | Verdict |
|---|---|---|---|---|---|
| **B-01** | ① | *Notre exposition aux vecteurs employés contre notre secteur diffère-t-elle de celle d'organisations comparables ?* | Stratégique | Orientation des investissements | Traitable, mais lourd |
| **B-02** | ② | *Quels vecteurs d'entrée et quelles techniques ont produit les incidents majeurs de notre secteur en 2030, et lesquels sommes-nous capables de traiter aujourd'hui ?* | Stratégique | Arbitrage budgétaire de novembre | **Traitable, échéance claire** |
| **B-03** | ③ | *Parmi les vulnérabilités affectant notre parc, lesquelles sont activement exploitées, et lesquelles le sont contre notre secteur ?* | Opérationnel | Ordre de traitement | **Le plus actionnable des six** |
| **B-04** | ④ | *Quelles techniques employées dans les incidents de notre secteur ne sont couvertes par aucune de nos règles de détection ?* | Opérationnel + tactique | Priorités de développement de détection | **Excellemment formulé à l'origine** |
| **B-05** | ⑤ | *Le vecteur d'entrée et la chaîne d'événements de l'incident [concurrent] sont-ils reproductibles chez nous ?* | Opérationnel | Mesures correctives ciblées | Traitable si l'incident est documenté |
| **B-06** | ⑥ | *Quels de nos fournisseurs critiques présentent une exposition publique connue ou ont subi un incident signalé ?* | Opérationnel | Sélection et suivi fournisseurs | Traitable, périmètre à borner |

**Ce que la reformulation change sur ① et ⑥** :

- **①** est le plus difficile. « Plus exposés que les autres » suppose une comparaison qu'aucune source ne fournit directement. La reformulation le rend traitable en le ramenant aux vecteurs, mais reste coûteuse. C'est un candidat au report.
- **⑥** est le plus mal formulé à l'origine et le plus facile à traiter une fois reformulé : le directeur des achats demandait une méthode, il obtient une question à laquelle des sources répondent.

**Section 2 — Décomposition de B-03 et B-04**

*B-03 — priorisation de la remédiation*

| # | Question renseignement | Réponse concevable ? |
|---|---|---|
| 1 | Quelles vulnérabilités de notre parc figurent dans un catalogue d'exploitation avérée ? | Oui, directement |
| 2 | Quelles vulnérabilités sont mentionnées comme exploitées dans les publications sectorielles ? | Oui, avec du travail |
| 3 | Quel est le délai observé entre publication et exploitation par famille de produit ? | Oui, sur historique propre |
| 4 | Lesquelles sont exposées sur des actifs accessibles depuis l'extérieur ? | **Oui — et cette donnée vient de l'organisation, pas de l'extérieur** |

*B-04 — écart de détection*

| # | Question renseignement | Réponse concevable ? |
|---|---|---|
| 1 | Quelles techniques sont documentées dans les incidents de notre secteur sur 12 mois ? | Oui |
| 2 | Quelles techniques nos règles couvrent-elles aujourd'hui ? | **Oui — donnée interne** |
| 3 | Parmi les non couvertes, lesquelles sont détectables avec nos capteurs actuels ? | Oui, avec l'équipe détection |
| 4 | Lesquelles nécessiteraient une source de journaux dont nous ne disposons pas ? | Oui |

⚠️ **Remarquez la question 4 de B-03 et la question 2 de B-04** : les deux appellent des données **internes**. Une part significative d'un plan de collecte ne pointe pas vers l'extérieur — c'est le chapitre 23.

**Section 3 — Le plan de collecte, extrait**

| Question | Source | Type | Fréquence | Coût | **Couverte ?** |
|---|---|---|---|---|---|
| B-03/1 — catalogue d'exploitation | Catalogue public | Ouverte | Quotidienne | Gratuit | ✅ **déjà reçue** |
| B-03/2 — publications sectorielles | Dispositif sectoriel | Communautaire | Hebdo | Adhésion | ⚠️ partielle |
| B-03/4 — exposition externe | Inventaire + cartographie interne | **Interne** | Continue | Néant | ✅ **existe déjà** |
| B-04/1 — techniques documentées | Publications + dispositif sectoriel | Ouverte | Mensuelle | Gratuit | ⚠️ non exploitée |
| B-04/2 — couverture de nos règles | Équipe détection | **Interne** | Trimestrielle | Néant | ❌ jamais formalisée |
| B-06 — exposition fournisseurs | Découverte externe + signalements publics | Mixte | Trimestrielle | À évaluer | ❌ |

**Le constat attendu** : sur six lignes, **deux sont déjà couvertes sans le savoir**, deux existent mais ne sont pas exploitées, et deux nécessitent un travail nouveau — dont une est purement interne et gratuite.

**Section 4 — Ce que nous décidons de ne pas suivre**

| Sujet écarté | Motif | Réexamen |
|---|---|---|
| **B-01 dans sa version comparative** | Aucune source ne permet une comparaison fiable entre organisations. Traité partiellement via B-02 | Dans 12 mois |
| Suivi nominatif d'acteurs | Sans effet sur nos décisions (§13.4) | Dans 12 mois |
| Surveillance de forums criminels | Cadre juridique à instruire, moyens insuffisants, faible rapport à nos besoins actuels | Dans 6 mois |
| Renseignement géopolitique | Aucun besoin exprimé le justifiant | Dans 12 mois |

**Les trois erreurs attendues**

1. **Traiter les six demandes.** Six besoins actifs pour une fonction naissante est le chemin le plus direct vers la saturation. Trois — B-03, B-04, B-02 — constituent un périmètre tenable la première année.
2. **Chercher des sources externes pour tout.** Deux des questions les plus utiles trouvent leur réponse dans l'organisation.
3. **Laisser la section 4 vide.** Un plan sans exclusions n'est pas un plan.

## 14.9 🔴 FIL ROUGE — mars 2030 : le plan de collecte, dix mois après

Nour a formalisé les six questions de mai 2029 (§5.7) en janvier 2030. Voici l'état à un an, présenté au comité du 12 mars.

| Réf | Besoin | Statut à 10 mois |
|---|---|---|
| B-01 | Priorisation de la remédiation *(Malik)* | **Actif** — le plus productif, alimente le MCS chaque semaine |
| B-02 | Mentions de nos produits *(Yann)* | **Actif** — a produit trois signalements, dont celui de décembre (§11.8) |
| B-03 | Ce qui arrive à nos pairs *(Claire)* | **Actif** — a produit l'évaluation de septembre (§8.9) |
| B-04 | Orientation des investissements *(Sonia)* | **Reporté** — une seule production en dix mois, échéance budgétaire manquée |
| B-05 | Écart de détection *(référent détection)* | **Actif** — le mieux formulé, le plus facile à servir |
| B-06 | *(refus d'Hélène Fabre)* | **Sans objet** — et c'est un succès, pas un échec |

**Le cas B-04 est le plus instructif.** Le besoin était réel, le demandeur légitime, et la fonction n'a produit qu'une note en dix mois — arrivée après l'arbitrage budgétaire de novembre.

**L'analyse que Nour en fait**, sans se dérober :

| Cause | Effet |
|---|---|
| Le besoin était **stratégique**, donc coûteux à servir | Chaque production demandait plusieurs jours |
| Il n'avait **pas d'échéance écrite** | Les besoins opérationnels, urgents, passaient toujours devant |
| Le demandeur ne relançait pas | Un besoin non relancé se comporte comme un besoin abandonné |

**La décision prise** : B-04 est **reformulé avec une échéance ferme** — une note pour le 15 septembre 2030, en vue de l'arbitrage de novembre — et une demi-journée par mois lui est réservée, protégée, dans le planning de Nour.

> *« Un besoin sans date n'est pas un besoin, c'est un souhait »*, note Claire au compte rendu.

**Ce que le comité retient d'autre.** Sur les quinze sources identifiées au plan de collecte, **onze étaient déjà disponibles** en mai 2029 — reçues, ingérées, ou accessibles gratuitement. Une seule souscription payante a été engagée en dix mois, pour une question précise que rien d'autre ne couvrait.

Le budget « outillage et sources » de la fonction, sur la première année : nettement inférieur à ce qui avait été provisionné. Karim Lebrun le relève lui-même.

**Livrable de l'épisode.** La matrice besoins × sources d'HELIOMED, révisée, avec cinq besoins actifs, un reporté avec échéance, et une section « non suivi » de quatre lignes.

→ La suite en 🔴 §15.6, quand Nour constatera que le cycle du renseignement qu'elle a appris ne décrit pas ce qu'elle fait.

## Synthèse mentale du chapitre 14

Un besoin de renseignement est une question, posée par un demandeur nommé, éclairant une décision datée, et dont on peut concevoir la réponse — cinq propriétés dont l'absence d'une seule rend le besoin intraitable. On ne l'obtient pas en demandant « de quoi avez-vous besoin » mais en interrogeant les décisions à venir et surtout **ce qui a surpris** : une surprise signale un angle mort, et un angle mort est un besoin qui ne s'est pas exprimé. La décomposition en questions renseignement révèle qu'un besoin unique appelle plusieurs sources et plusieurs fréquences, et qu'une part significative des réponses vient de l'organisation elle-même. Le plan de collecte produit son information la plus utile dans une seule colonne : ce qui est déjà couvert — et dans une organisation qui n'a jamais fait l'exercice, la majorité des besoins est satisfaite par des sources gratuites déjà reçues. Enfin, un plan sans liste de ce qu'on a décidé de ne pas suivre n'est pas un plan, c'est une accumulation.

**Trois questions de vérification**

1. Votre direction demande « à être tenue au courant ». Quelle question posez-vous, et pourquoi celle-là ?
2. Pourquoi « sommes-nous ciblés ? » est-il un besoin légitime et une mauvaise question renseignement ?
3. Un besoin n'a produit aucune réponse depuis six mois. Quelles sont les trois explications possibles, et que faites-vous dans chaque cas ?

→ **Chapitre 15 — Le cycle du renseignement** : le modèle que tout le monde enseigne, et pourquoi il ne décrit pas votre travail.

---
