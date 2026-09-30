---
title: Chapitre 39 — Le CTI dans une petite organisation
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
up:
- - CTI — travaux pratiques
  - ../index.md
- - PARTIE VIII — Piloter et industrialiser
  - index.md
---

> **Ce chapitre s'adresse à la majorité des lecteurs.** La plupart des organisations n'auront jamais une fonction CTI à temps plein. Ce qui suit décrit ce qui est réellement faisable, et ce à quoi il faut renoncer explicitement.

## 39.1 Ce qui est faisable à temps partiel

**Le budget réaliste** : deux à quatre heures par semaine, pour quelqu'un qui a un autre métier.

**Ce que ce budget permet** :

| Activité | Temps hebdomadaire | Faisable ? |
|---|---|---|
| Veille sur quatre sources (§21.6) | 1 h 40 | ✅ |
| Rapprochement avec l'inventaire | 30 min | ✅ |
| Un produit court par mois | 30 min amorti | ✅ |
| Répondre aux questions posées | Variable | ✅ |
| Une revue hebdomadaire de la file | 15 min | ✅ |
| **Total** | **≈ 3 h** | |

**Ce que ce budget ne permet pas** : l'analyse structurée systématique, le suivi de campagnes, le pivot d'infrastructure, la production stratégique, la cartographie de couverture.

## 39.2 Les trois sources qui suffisent

| Source | Temps | Ce qu'elle couvre |
|---|---|---|
| **Catalogue d'exploitation avérée** | 5 min/jour | Le signal le plus fort |
| **Avis des éditeurs de vos 3-4 produits critiques** | 10 min/jour | La source de vérité sur ce qui vous affecte |
| **Bulletins de votre centre de réponse national** | 15 min/semaine | Contexte, alertes, gratuité |

**Une quatrième si votre secteur en dispose** : un dispositif de partage sectoriel. C'est la seule source qui vous dira ce qui vise vos pairs, et son coût est une adhésion.

**Ce qu'il faut abandonner sans regret** : les réseaux professionnels comme source, les publications de chercheurs suivies systématiquement, les flux commerciaux généralistes.

## 39.3 Le produit minimal viable

**Une page par mois**, cinq sections :

```
CE QUI NOUS CONCERNE CE MOIS-CI
    2 à 4 éléments maximum, avec l'action associée

CE QUE NOUS AVONS VÉRIFIÉ ET QUI NE NOUS CONCERNE PAS
    3 à 5 lignes — c'est la section qui rassure et qui prouve le travail

CE QUE NOUS SURVEILLONS
    1 à 2 éléments, avec ce qui déclencherait une action

CE QUE NOUS NE SAVONS PAS
    1 à 2 lignes

CE QUE NOUS DEMANDONS
    Une décision, ou rien — et le dire
```


**La deuxième section est la plus importante dans une petite structure**, parce qu'elle est celle qui démontre que le travail a lieu. Le §29.9 en est la version développée : *ce contre quoi nous sommes protégés*.

## 39.4 Ce à quoi renoncer, et comment l'assumer

**La règle** : ce qui n'est pas fait doit être **écrit**, avec son motif.

| Renoncement | Formulation |
|---|---|
| Le niveau stratégique | *« Nous ne produisons pas d'analyse prospective. Nous nous appuierons sur des publications sectorielles en cas de besoin. »* |
| Le suivi de campagnes | *« Nous traitons les éléments à l'unité. Le regroupement en campagnes n'est pas assuré. »* |
| L'infrastructure adverse | *« Nous vérifions la fraîcheur et la colocation avant tout blocage. Nous ne conduisons pas de travail de pivot. »* |
| La cartographie de couverture | *« Non réalisée. Nous priorisons la détection sur les incidents réels. »* |
| Le partage actif | *« Nous consommons le dispositif sectoriel. Nous partageons les confirmations et infirmations. »* |

**Pourquoi l'écrire** : c'est le même principe que les périmètres déclarés non couverts du cours MCS. Un renoncement écrit est une décision ; un renoncement tacite est une lacune que personne ne verra jusqu'à l'incident.

## 39.5 Les quatre gestes qui produisent le plus, dans l'ordre

**Si vous ne deviez faire que quatre choses** :

| # | Geste | Temps | Effet |
|---|---|---|---|
| **1** | Rapprocher le catalogue d'exploitation avérée avec votre inventaire | 15 min/jour | Le meilleur rapport effort/valeur du domaine |
| **2** | Relire vos incidents des 18 derniers mois | 2 jours, une fois | Vos angles morts réels (§23.5) |
| **3** | Exploiter vos tentatives d'exploitation bloquées | 30 min/mois | Ce qui est testé contre vous (§23.3) |
| **4** | Adhérer à un dispositif sectoriel et poser des questions | 30 min/semaine | L'antériorité, et l'entraide |

**Aucun des quatre ne coûte d'argent.** Trois d'entre eux exploitent des données que vous possédez déjà.

🎯 **ET MAINTENANT ?**
*Vous êtes administrateur système dans une organisation de 120 personnes. On vous demande de « faire du CTI ». Vous avez trois heures par semaine. Par quoi commencez-vous ?*
**Réponse** : pas par une source. Par **deux questions posées à trois personnes** — le dirigeant, le responsable métier principal, et vous-même : *quelles décisions devez-vous prendre où il vous manque quelque chose ?* et *qu'est-ce qui vous a surpris cette année ?* Une heure au total. Vous en tirerez deux ou trois besoins réels. Ensuite seulement, vous choisissez les sources qui y répondent — et il y en aura moins que vous ne pensiez. Commencer par les sources, c'est garantir de consommer vos trois heures sans jamais produire de décision.

## 39.6 🔴 FIL ROUGE — le cas d'une PME cliente d'HELIOMED

*Cet épisode sort du fil rouge principal pour illustrer le chapitre.*

En 2031, HELIOMED propose à ses clients un modèle de dispositif CTI minimal, à la demande de plusieurs d'entre eux. L'un des premiers à l'adopter est un fabricant de matériel médical de 140 personnes, sans fonction de sécurité dédiée.

**Ce qui est mis en place**, par un administrateur système à trois heures par semaine :

| Élément | Mise en œuvre |
|---|---|
| Besoins | **2** — priorisation des correctifs · ce qui vise les fournisseurs du secteur |
| Sources | 3 gratuites + adhésion au dispositif sectoriel |
| Produit | Une page par mois, cinq sections |
| Destinataires | 2 — le dirigeant, le responsable production |
| Renoncements écrits | 5 |

**Le bilan à douze mois** :

| Indicateur | Valeur |
|---|---|
| Produits diffusés | 11 |
| Décisions documentées | **6** |
| — dont priorisations de correctifs réordonnées | 4 |
| — dont un fournisseur écarté après signalement sectoriel | 1 |
| — dont un investissement en authentification renforcée | 1 |
| Alertes émises | **1** |
| Coût direct | Adhésion sectorielle uniquement |

**Ce que l'administrateur écrit dans son bilan**, transmis à HELIOMED :

> *La section « ce que nous avons vérifié et qui ne nous concerne pas » est celle que mon dirigeant lit en premier. Il m'a dit que c'était la première fois qu'on lui expliquait pourquoi il ne fallait pas s'inquiéter.*

**Ce que Nour en tire pour le cours qu'elle finit par écrire** :

> *Six décisions en un an, pour trois heures par semaine et le prix d'une adhésion. Le rapport est meilleur que le nôtre. Ce n'est pas parce qu'il est meilleur analyste — c'est parce qu'il a deux besoins et qu'il les sert.*

**Livrable de l'épisode.** Le modèle de dispositif CTI minimal — deux besoins, trois sources, une page par mois, cinq renoncements écrits — annexe D.

## Synthèse mentale du chapitre 39

Deux à quatre heures par semaine suffisent à couvrir la veille sur quatre sources, le rapprochement avec l'inventaire, un produit mensuel et une revue de file — et ne suffisent pas à l'analyse structurée systématique, au suivi de campagnes ni à la production stratégique. Trois sources gratuites couvrent l'essentiel, plus une adhésion sectorielle si le secteur en dispose. Le produit minimal tient en une page et cinq sections, dont la plus importante en petite structure est *ce que nous avons vérifié et qui ne nous concerne pas* — elle démontre que le travail a lieu. Ce à quoi on renonce doit être écrit avec son motif, sinon c'est une lacune et non une décision. Enfin, les quatre gestes au meilleur rendement ne coûtent aucun argent et trois d'entre eux exploitent des données que vous possédez déjà.

**Trois questions de vérification**

1. Vous disposez de trois heures par semaine. Par quoi commencez-vous, et pourquoi pas par une source ?
2. Quelle section du produit mensuel démontre le mieux que le travail a lieu, et pourquoi ?
3. Pourquoi un renoncement écrit vaut-il mieux qu'un renoncement tacite ?

---
