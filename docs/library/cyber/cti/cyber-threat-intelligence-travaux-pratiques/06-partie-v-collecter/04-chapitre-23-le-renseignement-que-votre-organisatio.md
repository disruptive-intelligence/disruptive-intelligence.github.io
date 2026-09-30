---
title: Chapitre 23 — Le renseignement que votre organisation produit
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE V — Collecter
  - index.md
---

## 23.1 La source la plus pertinente et la moins exploitée

**Le constat qui ouvre ce chapitre** découle directement du chapitre 2 :

> **Aucun fournisseur ne peut vous vendre du renseignement, parce que le renseignement suppose de connaître votre contexte.** Ce contexte, vous êtes seul à le détenir — et il produit de l'information, en permanence, que presque personne n'exploite.

**Ce que votre organisation observe et que personne d'autre ne voit** :

| Ce que vous voyez | Ce que ça dit |
|---|---|
| Ce qui a été **tenté** contre vous | Le seul renseignement qui vous concerne à coup sûr |
| Ce qui a **échoué**, et pourquoi | Quelles mesures fonctionnent réellement |
| Ce qui a **réussi** | Vos angles morts, précisément localisés |
| Ce que vos utilisateurs **signalent** | Des signaux faibles inaccessibles autrement |
| Ce que vos **outils écartent** | Des tentatives que personne ne regarde |
| Ce que vos **partenaires** vous disent | Une vue élargie de votre chaîne |

**Pourquoi cette source est négligée**, en trois raisons :

| Raison | Mécanisme |
|---|---|
| **Elle ne ressemble pas à du renseignement** | Un ticket d'incident, un faux positif, un refus de connexion : ce sont des données d'exploitation |
| **Elle est dispersée** | Aucune n'est dans un flux ; elles sont dans des outils différents, tenus par des équipes différentes |
| **Elle demande de demander** | Il faut aller la chercher auprès de collègues, ce qui est plus coûteux qu'un abonnement |

⚠️ **PIÈGE — l'asymétrie d'attention**
Une organisation consacre volontiers 40 k€ par an à un flux externe et zéro heure par mois à exploiter ses propres incidents. Le rapport de valeur est pourtant inverse : le flux décrit le monde, l'incident décrit **vous**.

## 23.2 Les incidents, les alertes et les faux positifs

**Ce qu'un incident produit**, et qui est presque toujours perdu :

| Élément | Valeur de renseignement |
|---|---|
| Le **vecteur d'entrée** | Ce qui est ouvert chez vous, factuellement établi |
| La **séquence d'actions** | Un mode opératoire observé, de première main |
| Les **indicateurs** | Datés, contextualisés, et certainement pertinents |
| Ce qui a **arrêté** l'adversaire | La mesure qui fonctionne — information rare |
| Ce qui a **échoué à le détecter** | Un écart de couverture, précisément localisé |
| La **durée** entre entrée et détection | Un indicateur de votre capacité réelle |

**Le mécanisme de la perte** : un incident se clôt par un rapport de réponse à incident, orienté remédiation, archivé. Personne n'en extrait la partie renseignement, et six mois plus tard, plus personne ne sait ce qu'il a appris.

✅ **BONNE PRATIQUE (P0) — la fiche de renseignement post-incident**
Une page, produite systématiquement à la clôture, **par la fonction CTI et non par l'équipe de réponse**. Elle ne remplace pas le rapport d'incident : elle en extrait ce qui servira ailleurs.

**Les faux positifs sont la source la plus négligée du chapitre.** Une règle qui déclenche à tort dit quelque chose : sur votre environnement, sur ce qui y est normal, et parfois sur une activité légitime que vous ne connaissiez pas. Une revue trimestrielle des dix faux positifs les plus fréquents produit régulièrement des découvertes — des flux non documentés, des outils non déclarés, des comportements applicatifs inconnus.

## 23.3 Journaux, télémétrie, tentatives échouées

**Ce qui est écarté avant même de produire une alerte** constitue un gisement.

| Source | Ce qu'elle contient | Ce qu'on en tire |
|---|---|---|
| Authentifications échouées | Volume, origines, comptes visés | Détection de tests d'identifiants, exposition de comptes |
| Connexions refusées par filtrage | Ce qui essaie d'entrer | Balayages, ciblage, évolution dans le temps |
| Requêtes bloquées en frontal | Tentatives d'exploitation | **Quelles vulnérabilités sont testées contre vous** |
| Courriels bloqués | Thématiques, expéditeurs, pièces jointes | Campagnes visant vos collaborateurs |
| Alertes de faible sévérité | Ce qui n'est pas remonté | Signaux faibles agrégés |

**La ligne la plus utile est la troisième.** Les tentatives d'exploitation bloquées en frontal vous disent **quelles vulnérabilités des acteurs cherchent activement chez vous** — c'est-à-dire le renseignement le plus directement actionnable qui soit pour la priorisation de la remédiation (§29). Cette donnée existe dans la quasi-totalité des organisations et n'est presque jamais exploitée.

🧪 **EN PRATIQUE — l'exercice mensuel en trente minutes**

```
1. Extraire le top 20 des tentatives d'exploitation bloquées du mois
2. Croiser avec l'inventaire : ces vulnérabilités existent-elles chez nous ?
3. Croiser avec les correctifs : sont-elles corrigées ?
4. Produire trois lignes : ce qui est testé · ce qui nous concerne · ce qui reste ouvert
```


**Ce que cet exercice produit régulièrement** : la découverte qu'une vulnérabilité activement testée contre l'organisation figure encore au *backlog* de remédiation avec une priorité basse.

## 23.4 Ce que le dispositif de MCS produit

Pour le lecteur venu du cours précédent, cette section est une jonction directe. Pour les autres, elle décrit un gisement qui existe dans toute organisation dotée d'une gestion des vulnérabilités.

| Ce que le MCS produit | Ce que le CTI en fait |
|---|---|
| **L'inventaire** | Le rapprochement entre une menace et votre applicabilité (§19.4) |
| **La cartographie d'exposition** | Le deuxième critère de priorisation, que nul ne fournit |
| **Les constats ouverts** | Ce qui est vulnérable **maintenant**, à croiser avec ce qui est exploité |
| **Les dérogations** | Des risques acceptés, à réévaluer si la menace évolue |
| **Les périmètres non couverts** | Vos angles morts déclarés |

**La ligne des dérogations mérite d'être soulignée.** Une dérogation est une décision de ne pas corriger, prise sur la base d'une évaluation du risque à un instant donné. Si le CTI apprend qu'une vulnérabilité couverte par une dérogation devient activement exploitée, **la base de la décision a changé** — et personne ne le verra si les deux dispositifs ne se parlent pas.

✅ **BONNE PRATIQUE (P0)** — Croisez trimestriellement le registre des dérogations avec les catalogues d'exploitation avérée. L'exercice prend une heure et produit, en moyenne, une à deux réévaluations.

## 23.5 Ce que le support et les métiers savent

**Le gisement le moins technique et le plus négligé.**

| Source | Ce qu'elle sait |
|---|---|
| Le support utilisateurs | Les tentatives d'ingénierie sociale signalées, les comportements anormaux |
| Le service commercial | Ce que les clients demandent, ce qui inquiète le secteur |
| Les achats | Les incidents chez les fournisseurs, les questionnaires reçus |
| Les affaires réglementaires | Les obligations émergentes, les signalements sectoriels |
| Les ressources humaines | Les tentatives d'approche, les faux recrutements |
| La communication | Les usurpations d'identité, les mentions publiques |

**Ce qui bloque** : aucune de ces personnes ne pense détenir du renseignement, et aucune ne sait à qui le dire.

**Ce qui débloque, et ce n'est pas un outil** : une question posée régulièrement. Un point de quinze minutes par trimestre avec chacun de ces interlocuteurs, avec une seule question — *avez-vous vu quelque chose d'inhabituel ?* — produit davantage que la plupart des flux.

🎯 **ET MAINTENANT ?**
*Vous prenez un poste de CTI dans une organisation qui n'en avait pas. Quelle est votre première source ?*
**Réponse** : les incidents des dix-huit derniers mois. Avant tout abonnement, avant toute veille, vous relisez ce qui est réellement arrivé à cette organisation — vecteurs d'entrée, ce qui a fonctionné pour l'adversaire, ce qui l'a arrêté, ce qui n'a pas été détecté. Deux à trois jours de travail. Vous en tirerez trois choses qu'aucune source externe ne vous donnera : les angles morts réels, les mesures qui tiennent, et le profil des menaces qui atteignent effectivement cette organisation. C'est aussi ce qui vous rendra crédible auprès des équipes, parce que vous parlerez de ce qu'elles ont vécu.

## 23.6 Transformer un incident en fiche de renseignement

**Le format**, une page, produit à la clôture de chaque incident significatif.

| Section | Contenu | Destinataire ultérieur |
|---|---|---|
| **Vecteur d'entrée** | Précis, avec la mesure qui aurait dû l'empêcher | MCS, architecture |
| **Séquence observée** | Les étapes, dans l'ordre, avec les techniques employées | Détection |
| **Indicateurs** | Avec dates de première et dernière observation | Détection, partage sectoriel |
| **Ce qui a arrêté l'adversaire** | La mesure efficace, nommée | Direction — argumentaire d'investissement |
| **Ce qui n'a pas détecté** | L'écart de couverture, localisé | Détection |
| **Délai entrée → détection** | En heures ou en jours | Indicateur de capacité (§35) |
| **Ce qui est partageable** | Après anonymisation, selon les catégories du §20.8 | Dispositif sectoriel |
| **Ce que cela change** | Les décisions à réexaminer | Tous |

**La dernière ligne est celle qui distingue une fiche d'un compte rendu.** Un incident produit des faits ; la fiche dit ce qu'il faut en faire ailleurs.

## 23.7 🔴 FIL ROUGE — février 2030 : plus qu'un an de flux

Le 3 février, HELIOMED subit un incident : un poste de la R&D de Nantes est compromis par une pièce jointe. L'adversaire progresse pendant onze jours avant d'être détecté par une alerte sur un accès inhabituel au dépôt de code. Aucune donnée n'est exfiltrée.

**L'équipe de réponse produit son rapport le 20 février** : chronologie, périmètre, actions de remédiation, recommandations techniques. Vingt-deux pages. Il est archivé.

**Nour produit sa fiche de renseignement le 24 février.** Une page. Voici ce qu'elle contient, et ce qu'elle déclenche.

| Section | Contenu | Effet |
|---|---|---|
| **Vecteur** | Pièce jointe, macro, exécution après avertissement ignoré. La politique de blocage des macros existe mais **exclut le service R&D depuis 2027** | Exclusion réexaminée et supprimée en mars |
| **Séquence** | 6 techniques identifiées, dont 3 non couvertes par la détection | Trois règles écrites en mars |
| **Indicateurs** | 14, dont 9 encore valides à la date de la fiche | Partagés au dispositif sectoriel le 26 février |
| **Ce qui a arrêté** | L'alerte sur accès inhabituel au dépôt de code — **règle écrite six mois plus tôt sur la base du besoin B-05** | **Argumentaire d'investissement en détection** |
| **Ce qui n'a pas détecté** | L'accès initial, la persistance, le mouvement latéral — 11 jours d'invisibilité | Analyse d'écart §18.8 confirmée par le réel |
| **Délai entrée → détection** | **11 jours** | Premier indicateur de capacité chiffré |
| **Ce que cela change** | 4 décisions listées | — |

**Ce que la fiche produit, et que le rapport de vingt-deux pages n'avait pas produit** :

1. **L'exclusion de 2027 est réexaminée.** Elle figurait dans le rapport de réponse comme une observation technique ; la fiche la formule comme une décision à revoir, avec un destinataire.
2. **Trois règles de détection sont écrites.** Le rapport listait les techniques ; la fiche les croise avec la cartographie du §18.8 et identifie lesquelles manquaient.
3. **Les indicateurs sont partagés.** Neuf sur quatorze étaient encore valides — deux membres du dispositif sectoriel signalent une activité correspondante dans les trois semaines suivantes.
4. **L'argument d'investissement change de nature.** Ce n'est plus « il faudrait investir en détection », c'est *« la règle qui nous a sauvés a été écrite en août à partir d'un besoin exprimé en mai ; nous en avons trois autres en attente »*.

**Le chiffre que Claire porte au comité du 12 mars**, et qui frappe :

> *Cet incident a produit plus de renseignement exploitable — quatorze indicateurs contextualisés, six techniques confirmées, un écart de couverture localisé, une décision de configuration à revoir — que douze mois de flux externe.*

**Ce que Karim Lebrun demande alors**, et qui devient un point de méthode : *« est-ce que ça vaut pour tous les incidents, ou seulement pour celui-là ? »*

**Réponse honnête de Nour** : non. Un incident mineur — un poste isolé, sans progression — produit peu. Le critère retenu est écrit : **une fiche est produite pour tout incident ayant impliqué une progression au-delà de l'actif initial, ou une durée de détection supérieure à 48 heures.** Sur l'année 2030, cela représente quatre incidents sur onze.

**L'effet mesuré à douze mois** :

| Source | Éléments exploités en 2030 |
|---|---|
| Flux commercial (fournisseur B) | 14 |
| Sources ouvertes | 61 |
| Dispositif sectoriel | 23 |
| **Incidents internes (4 fiches)** | **38** |

Trente-huit éléments exploités issus de quatre incidents. Le coût de production : environ une journée de travail par fiche.

> *« La source la moins chère est celle qu'on paie déjà »*, écrit Nour.

**Livrable de l'épisode.** La fiche de renseignement post-incident en huit sections, et le critère de déclenchement — annexe D.

→ La suite en 🔴 §24.5, quand un pivot d'infrastructure produira une découverte et deux faux positifs.

## Synthèse mentale du chapitre 23

Aucun fournisseur ne peut vous vendre du renseignement, parce que le renseignement suppose votre contexte — que vous seul détenez, et qui produit de l'information en permanence. Cette source est négligée pour trois raisons : elle ne ressemble pas à du renseignement, elle est dispersée, et elle demande de demander. Un incident produit six éléments de valeur presque toujours perdus, dont le plus rare est *ce qui a arrêté l'adversaire* — la mesure qui fonctionne. Les tentatives d'exploitation bloquées en frontal disent quelles vulnérabilités sont activement testées contre vous : c'est le renseignement le plus directement actionnable qui soit, il existe partout et n'est presque jamais exploité. Le registre des dérogations doit être croisé avec les catalogues d'exploitation, parce qu'une décision de ne pas corriger repose sur une évaluation qui peut avoir changé. Enfin, le gisement le moins technique — support, commercial, achats, ressources humaines — se débloque par une question posée trimestriellement, pas par un outil.

**Trois questions de vérification**

1. Vous prenez un poste de CTI dans une organisation sans dispositif existant. Quelle est votre première source, et pourquoi avant tout abonnement ?
2. Quelle donnée, présente dans presque toutes les organisations, indique quelles vulnérabilités sont activement testées contre vous ?
3. Pourquoi un registre de dérogations est-il une source de renseignement, et que faites-vous de ce croisement ?

---
