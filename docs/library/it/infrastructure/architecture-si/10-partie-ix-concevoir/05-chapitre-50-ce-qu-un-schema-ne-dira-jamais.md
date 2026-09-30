---
title: Chapitre 50 — Ce qu'un schéma ne dira jamais
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - PARTIE IX — Concevoir
  - index.md
---

> **Clôture du cours.** Il apprend la leçon qui empêche de terminer ce livre avec une confiance excessive.

#### 50.1 Le tableau visible / invisible

| Ce qu'un schéma montre | Ce qu'il ne montrera jamais |
|---|---|
| Les segments et les zones | **Les procédures d'exploitation** |
| Les pare-feu | **Les règles réellement en place** |
| Les serveurs | **Ce qui s'y exécute vraiment** |
| Les liens | **Ce qui les traverse** |
| Les flux dessinés | **Les flux de dépendance** — principe des trois flux |
| Les services | **Les contraintes métier qui les ont produits** |
| La redondance | **Si elle a déjà été testée** |
| Les composants | **Les compétences pour les exploiter** |
| L'agencement | **Les décisions et les arbitrages** |
| Le nominal | **Les contournements en place depuis trois ans** |
| Les versions, parfois | **Les correctifs réellement appliqués** |
| L'instantané | **L'histoire, et ce qui est en cours de migration** |

**Les quatre dernières lignes font la leçon.** Un schéma décrit un système ; il ne décrit ni l'organisation qui le tient, ni l'histoire qui l'a produit, ni l'écart entre l'intention et le réel.

#### 50.2 Les deux écarts symétriques

| Écart | Fréquence | Comment on le détecte |
|---|---|---|
| **Dessiné et jamais construit** | Fréquent | Le composant n'apparaît dans aucun inventaire, aucun journal, aucune facture |
| **Construit et jamais dessiné** | **Plus fréquent encore** | Un flux observé sans origine documentée · une machine qui répond et n'est nulle part |

⚠️ **Le second est le plus dangereux.** Il désigne exactement ce que le volume Asset Management appelle un actif orphelin ou une informatique parallèle : quelque chose existe, fonctionne, expose — et n'est connu de personne.

#### 50.3 Comment on vérifie

| Méthode | Ce qu'elle révèle | Coût |
|---|---|---|
| **Suivre un flux en vrai**, avec l'exploitation | L'écart entre le chemin dessiné et le chemin réel | Une demi-journée |
| **Comparer avec l'inventaire** | Ce qui existe et n'est pas dessiné | Selon la qualité de l'inventaire |
| **Lire les règles de pare-feu** | Ce qui est réellement autorisé, contre ce qui est supposé l'être | Quelques heures, souvent instructives |
| **Regarder les journaux** | Les flux qui existent vraiment | Variable |
| **Demander à quelqu'un d'ancien** | L'histoire, les contournements, les raisons | **Une heure, le meilleur rapport du tableau** |

⚠️ **La dernière ligne est la plus efficace et la moins pratiquée.** Une conversation d'une heure avec quelqu'un présent depuis dix ans apprend davantage sur une architecture que trois jours de lecture de documents.

#### 50.4 La phrase de clôture

> ### Une architecture dessinée n'est pas une architecture réelle.

**Ce que cela impose** :

| Devant un schéma | La bonne posture |
|---|---|
| Il est complet | **Il ne l'est jamais** — la question est de savoir de combien |
| Il est à jour | **Datez-le**, et demandez ce qui a changé depuis |
| Il est vrai | Il représente une intention. Vérifiez ce qui a été construit |
| Il est neutre | **Il a été fait pour quelqu'un** — §5.5 |

#### 50.5 🔬 Mini-lab 14 — Dessiner l'architecture de votre organisation

**Objectif** — Produire un schéma, puis lister ce qu'il tait.
**Durée** 2 h · **Difficulté** 🔴 avancé · **Prérequis** l'ensemble du cours

```
1. Dessinez l'architecture de votre organisation, ou d'un service
   que vous connaissez. Une page, à la main.

2. Appliquez les sept passes du chapitre 36 à VOTRE schéma.

3. Listez les onze éléments du §3.4 qui n'y figurent pas.

4. Écrivez les trois questions que vous ne savez pas trancher.

5. Allez poser ces trois questions.
```


**Ce que l'exercice produit systématiquement** : entre trois et six découvertes, dont au moins une concerne un flux ou un composant dont l'existence n'était pas connue de la personne qui a dessiné.

#### 50.6 🔴 FIL ROUGE — décembre 2025 : ce qu'Amélie a compris

*Dernier épisode du cours. Il se raccorde au premier chapitre du volume Asset Management.*

Le 19 décembre, Amélie remet à Claire Nadeau un document de deux pages. Il ne contient aucun inventaire.

**Page 1 — le schéma redessiné.** Le même que celui de mars 2023, avec onze ajouts au crayon : la résolution de noms, l'annuaire relié à tout, la synchronisation d'horloge, le réseau d'administration, les 620 postes, les 180 nomades, la passerelle d'accès distant, le site de Nantes, les postes de prestataires, la collecte de journaux, et une zone marquée d'un point d'interrogation : *services en ligne — nombre inconnu*.

**Page 2 — ce que le schéma ne dit pas.** Vingt-trois lignes, chacune une question sans réponse.

**Ce que Claire lui dit en le lisant** :

> *« C'est la première fois en trois ans que je vois ce document. »*

**Ce qu'Amélie écrit en conclusion**, et qui est la phrase qui ouvre le volume suivant :

> *Le schéma de mars 2023 n'était pas faux. Il montrait ce que quelqu'un avait choisi de montrer, à un moment, pour une raison. Mon travail ne consiste pas à le corriger. Il consiste à savoir de combien il s'écarte de ce qui existe — et à écrire cet écart.*

**Le 5 janvier 2026, sa mission d'inventaire démarre.** Elle sait ce qu'elle regarde.

---

> ### 🎓 Ce que vous savez faire
>
> **Lire**
> ☐ Poser les quatre questions du lecteur devant n'importe quel schéma
> ☐ Appliquer les sept passes dans l'ordre, et produire une lecture d'une page
> ☐ Distinguer trois familles de flux, et savoir laquelle arrête un service
> ☐ Suivre une requête en douze étapes, dont sept ne sont pas dessinées
> ☐ Reconnaître une strate ancienne à trois signes convergents
> ☐ Identifier les points de rupture, y compris ceux qui ne sont reliés à rien
>
> **Comprendre**
> ☐ Expliquer ce que chaque composant résout et ce qu'il coûte
> ☐ Reconstituer l'arbitrage qui a produit une architecture
> ☐ Dire à partir de quelle contrainte un composant devient nécessaire
> ☐ Construire l'arbre de dépendance d'un service métier
> ☐ Dire où l'on peut agir, et où c'est structurellement impossible
>
> **Concevoir et critiquer**
> ☐ Chiffrer des contraintes plutôt que de les énoncer
> ☐ Proposer une architecture proportionnée à ce que l'organisation sait exploiter
> ☐ Écrire un registre des compromis
> ☐ Critiquer en six points, et ne recommander qu'une seule action
> ☐ Formuler une critique en cinq lignes qui sera entendue
>
> **Savoir ce qu'on ne sait pas**
> ☐ Lister ce qu'un schéma ne dit pas
> ☐ Distinguer ce qui a été dessiné et jamais construit de l'inverse
> ☐ Poser trois questions plutôt qu'un jugement
>
> ---
>
> **Ce que ce cours ne vous a pas appris** : dimensionner, choisir un produit, administrer un composant, concevoir un système à forte contrainte. Ces métiers existent, et ils s'apprennent ailleurs.
>
> **Ce que seule la pratique donne** : le sens de ce qui va casser avant que ça casse, la mémoire des architectures qu'on a vues échouer, et la patience de demander l'histoire avant de juger.

---


## Cas de synthèse

---
