---
title: Chapitre 21 — Les sources ouvertes
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE V — Collecter
  - index.md
---

## 21.1 Ce que couvrent réellement les sources ouvertes

**Le constat qui structure ce chapitre**, et qui contredit une intuition répandue :

> **Pour une organisation ordinaire, les sources ouvertes couvrent la majorité des besoins de renseignement.** Le manque n'est presque jamais un manque de sources — c'est un manque de rapprochement entre les sources et les questions (§14.4).

**Ce qu'elles couvrent bien** :

| Besoin | Couverture |
|---|---|
| Vulnérabilités affectant vos produits | **Excellente** |
| Vulnérabilités activement exploitées | **Bonne** |
| Modes opératoires documentés | **Bonne**, avec un décalage |
| Tendances sectorielles | Correcte |
| Incidents publics comparables | Correcte, mais partielle |
| Analyse technique approfondie | **Excellente** — souvent meilleure que le payant |

**Ce qu'elles ne couvrent pas** :

| Besoin | Pourquoi |
|---|---|
| Ce qui vous vise **spécifiquement** | Personne ne le publie |
| Ce qui n'est pas encore public | Par définition |
| Ce qui circule dans des espaces fermés | Sauf reprise par un tiers |
| Votre propre exposition | Elle vient de vous (chapitre 23) |

## 21.2 Les familles de sources ouvertes

| Famille | Ce qu'elle apporte | Fraîcheur | Fiabilité | Effort |
|---|---|---|---|---|
| **Autorités nationales et centres de réponse** | Alertes, avis, recommandations, contexte national | Bonne | **Élevée** | Faible |
| **Bases de vulnérabilités** | Identification, description, versions affectées | Bonne | Élevée sur le factuel | Faible |
| **Catalogues d'exploitation avérée** | Le signal le plus fort du domaine | Bonne | Élevée | Très faible |
| **Avis des éditeurs de vos produits** | **La source de vérité** sur ce qui vous affecte | Excellente | Élevée | Faible |
| **Publications de chercheurs et d'éditeurs** | Analyse technique, modes opératoires | Variable | Variable (§10.5) | Moyen |
| **Dispositifs sectoriels** | Ce qui vise votre secteur, parfois avant publication | **Excellente** | Élevée | Adhésion |
| **Communautés et réseaux professionnels** | Signaux faibles, retours d'expérience | Excellente | **Faible** | Élevé — bruit important |
| **Presse spécialisée** | Alerte rapide | Excellente | Faible (§10.5) | Faible |

**Les trois premières lignes, plus la quatrième, couvrent à elles seules le besoin de priorisation de la remédiation** — qui est, dans la plupart des organisations, le besoin le plus productif. Elles sont gratuites et demandent peu d'effort.

⚠️ **PIÈGE — les réseaux professionnels comme source principale**
Ils sont excellents pour repérer un signal faible et détestables comme source de renseignement : pas de vérification, pas de provenance, amplification des affirmations spectaculaires, et forte circularité (§10.4). Ils servent à **repérer**, jamais à **établir**.

## 21.3 Construire une veille tenable

**Le problème n'est pas de trouver des sources.** C'est de tenir dans la durée sans y consacrer trois heures par jour ni passer à côté de ce qui compte.

**Les quatre principes d'une veille tenable** :

| Principe | Application |
|---|---|
| **Le filtrage vient du plan de collecte, pas des sources** | On suit une source parce qu'elle répond à une question, pas parce qu'elle est réputée |
| **La cadence est différenciée** | Quotidienne pour trois sources, hebdomadaire pour cinq, mensuelle pour le reste |
| **Le temps est borné** | Vingt minutes le matin, pas « quand j'aurai le temps » |
| **Ce qui n'est pas traité est archivé, pas reporté** | Une file de veille en retard ne se rattrape jamais |

🧪 **EN PRATIQUE — la veille en vingt minutes**

```
5 min   Catalogue d'exploitation avérée + avis des éditeurs de vos produits C1
        → rapprochement immédiat avec l'inventaire
        → tout ce qui matche entre en file avec une priorité

7 min   Bulletins des autorités et centres de réponse
        → lecture des titres, ouverture de ce qui touche un besoin actif

5 min   Dispositif sectoriel
        → tout est lu, le volume est faible et la pertinence élevée

3 min   Le reste — publications, réseaux, presse
        → repérage uniquement, aucune lecture approfondie
```


**Ce que cette répartition traduit** : l'essentiel du temps va aux sources de **haute fiabilité et haute pertinence**, et le reste est du repérage. C'est l'inverse de ce que fait spontanément une personne qui découvre le domaine.

## 21.4 La fatigue de veille

**Un phénomène réel**, qu'il faut nommer parce qu'il détruit des fonctions CTI.

**Le mécanisme** : le volume est infini, la pertinence est faible, la gratification est différée. Au bout de quelques mois, l'analyste lit en diagonale, puis lit moins, puis ne rattrape plus — et le jour où l'information importante passe, elle passe.

**Les quatre signes** :

| Signe | Ce qu'il indique |
|---|---|
| La file de veille a plus de trois jours de retard | Le volume dépasse la capacité |
| On ne lit plus que les titres | Le filtrage a cessé d'être conscient |
| On ne se souvient pas de ce qu'on a lu hier | La lecture n'est plus reliée à un besoin |
| On ajoute des sources pour se rassurer | §14.6 |

**Les trois remèdes** :

1. **Réduire le nombre de sources**, en repartant du plan de collecte. C'est contre-intuitif et c'est le seul qui fonctionne durablement.
2. **Archiver sans culpabilité.** Ce qui n'est pas traité en trois jours ne le sera jamais : on archive, avec motif, et on passe.
3. **Relier chaque lecture à un besoin.** Une lecture sans destination est une lecture qui fatigue sans produire.

## 21.5 📌 Les limites des sources ouvertes

- **Le décalage.** Ce qui est public a été observé plus tôt, parfois de plusieurs mois. Vous travaillez toujours avec du retard (§19.3).
- **Le biais de publication.** On publie ce qui est spectaculaire, nouveau, ou commercialement intéressant. Le banal et le récurrent — qui produisent la majorité des incidents — sont sous-représentés.
- **La couverture inégale.** Certains secteurs, certaines géographies et certains types de produits sont bien couverts ; d'autres ne le sont pas du tout.
- **La circularité** (§10.4), particulièrement forte en sources ouvertes.
- **Rien sur vous.** C'est la limite fondamentale, et elle justifie le chapitre 23.

🎯 **ET MAINTENANT ?**
*Vous démarrez une fonction CTI et disposez de deux heures par semaine. Quelles sources retenez-vous ?*
**Réponse** : quatre, pas davantage. *Le catalogue d'exploitation avérée* — cinq minutes par jour, et c'est le signal le plus fort du domaine. *Les avis des éditeurs de vos trois ou quatre produits les plus critiques* — c'est la source de vérité sur ce qui vous affecte. *Les bulletins de votre centre de réponse national* — contexte, alertes, et gratuité. *Un dispositif sectoriel* si votre secteur en a un — c'est le seul qui vous dira ce qui vise vos pairs. Tout le reste attend que vous ayez du temps, et vous n'en aurez pas la première année. Cette liste couvre les besoins de priorisation et d'alerte, qui sont les deux plus productifs.

## 21.6 🔴 FIL ROUGE — juin 2029 : ce qui était déjà là

En juin 2029, Nour instruit une demande de souscription à un flux commercial. Le fournisseur propose un abonnement à 38 k€ par an, avec une couverture décrite comme complète sur le secteur de la santé.

**Avant de comparer les offres, elle applique le §14.4** : que couvre déjà ce qu'HELIOMED reçoit gratuitement ?

**Le résultat, établi en trois jours** :

| Besoin | Couvert par le payant ? | Couvert par le gratuit ? |
|---|---|---|
| Vulnérabilités exploitées sur nos produits | Oui | **Oui — catalogue public, déjà reçu** |
| Vulnérabilités visant notre secteur | Oui | **Partiellement** — dispositif sectoriel, non adhérent |
| Modes opératoires documentés | Oui | **Oui** — publications, non exploitées |
| Analyse technique approfondie | Oui | **Oui, et souvent meilleure** |
| Indicateurs techniques en volume | **Oui** | Partiellement |
| Ce qui vise HELIOMED spécifiquement | **Non** | Non |
| Mentions de nos produits | **Non** | Non |

**Le constat** : sur sept besoins, cinq sont couverts ou couvrables gratuitement. Les deux qui ne le sont pas — ce qui vise HELIOMED spécifiquement et les mentions de ses produits — **ne sont pas couverts par l'offre payante non plus**.

**Ce qui est décidé** :

| Décision | Coût |
|---|---|
| Exploiter réellement le flux gratuit déjà ingéré | 0 € |
| Adhérer au dispositif sectoriel | Cotisation annuelle modeste |
| Reporter la souscription commerciale | 0 € |
| Instruire séparément une surveillance des mentions de produits | À évaluer |

**Ce qui frappe Claire**, et qu'elle relève au comité : le flux d'indicateurs livré avec la solution de protection des postes — celui qui figurait dans l'inventaire de mars 2029 (§1.10) comme *« ingéré automatiquement, personne ne l'a jamais examiné »* — contenait, sur les six mois écoulés, **onze indicateurs correspondant à des actifs d'HELIOMED**.

Aucun n'avait produit d'alerte, parce que personne n'avait relié le flux à l'inventaire.

> *« Nous allions payer 38 000 € pour recevoir mieux ce que nous ne lisions pas », note-t-elle au compte rendu.*

**L'épilogue, dix mois plus tard.** En avril 2030, une souscription commerciale est finalement engagée — pour un besoin précis, non couvert autrement, et après un test comparatif (§22.3). Le montant est nettement inférieur à l'offre de 2029, parce que le périmètre est nettement plus étroit.

**Livrable de l'épisode.** La matrice de couverture besoin par besoin, gratuit contre payant — annexe C. Et l'exploitation effective du flux existant, qui devient le besoin B-01 opérationnel.

→ La suite en 🔴 §22.6, avec le test comparatif d'avril 2030.

## Synthèse mentale du chapitre 21

Pour une organisation ordinaire, les sources ouvertes couvrent la majorité des besoins : le manque n'est presque jamais un manque de sources, c'est un manque de rapprochement entre les sources et les questions. Quatre familles suffisent à couvrir les deux besoins les plus productifs — catalogue d'exploitation avérée, avis des éditeurs de vos produits critiques, bulletins des autorités, dispositif sectoriel — et elles sont gratuites ou peu coûteuses. Les réseaux professionnels servent à repérer, jamais à établir. Une veille tenable filtre depuis le plan de collecte, différencie ses cadences, borne son temps, et archive sans culpabilité ce qui n'a pas été traité en trois jours. La fatigue de veille détruit des fonctions CTI, et son seul remède durable est contre-intuitif : réduire le nombre de sources. Enfin, les sources ouvertes ne disent rien de vous — c'est leur limite fondamentale, et elle justifie que la source la plus pertinente soit interne.

**Trois questions de vérification**

1. Vous disposez de deux heures par semaine. Quelles quatre sources retenez-vous, et quels besoins couvrent-elles ?
2. Votre file de veille a une semaine de retard. Que faites-vous, et pourquoi ajouter du temps est la mauvaise réponse ?
3. Un flux gratuit est ingéré par votre outil depuis deux ans. Quelle vérification faites-vous avant d'envisager une souscription payante ?

---
