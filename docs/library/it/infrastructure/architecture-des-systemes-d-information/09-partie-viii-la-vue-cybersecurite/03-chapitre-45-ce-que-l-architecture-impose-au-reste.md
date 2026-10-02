---
title: Chapitre 45 — Ce que l'architecture impose au reste
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE VIII — La vue cybersécurité
  - index.md
---

> Le chapitre de raccordement. Il explique pourquoi les autres volumes de la collection demandent d'assumer certains compromis : **ils sont déterminés ici**.

## 45.1 Ce que l'architecture impose au maintien en condition de sécurité

| Ce que l'architecture détermine | Conséquence sur le maintien |
|---|---|
| **L'interruptibilité** | Un composant qui ne peut pas s'arrêter ne sera pas corrigé — quelle que soit la politique |
| **La redondance** | Sans elle, toute correction impose une interruption |
| **Le nombre de composants uniques** | Chaque point de rupture est une fenêtre de maintenance négociée |
| **Les dépendances** | Corriger un composant peut arrêter un service qu'on ne soupçonnait pas |
| **Le cycle de vie du plus ancien composant** | Il fixe le plancher de modernisation de tout ce qui en dépend |

> **La formulation qui résume** : *aucune politique de correctifs ne rattrape une architecture non interruptible.*

**C'est le principe 7 du volume Maintien en condition de sécurité** — *le coût du maintien se décide en conception, pas en exploitation* — et ce chapitre en donne la démonstration architecturale.

🔥 **SCÉNARIO — le correctif ne sera jamais appliqué**

| Question | Réponse |
|---|---|
| Symptôme | Une vulnérabilité critique reste ouverte depuis quatorze mois |
| Hypothèse naïve | « L'équipe ne fait pas son travail » |
| Dépendance réelle | **Le composant est unique, et son arrêt stoppe une chaîne de production** |
| Ce que le schéma aurait dû montrer | Qu'aucune redondance n'existe sur ce composant |
| Concevoir différemment | **La décision qui a produit cette situation date de la conception**, pas de l'exploitation |

## 45.2 Ce que l'architecture impose à l'inventaire

| Ce que l'architecture détermine | Conséquence sur l'inventaire |
|---|---|
| **Ce qui est découvrable** | Un actif sur un segment non balayé n'apparaîtra pas |
| **Ce qui a une adresse stable** | Un actif éphémère échappe aux méthodes classiques — §41.4 |
| **Ce qui appartient à un tiers** | Ne se découvre pas : **se déclare** |
| **Ce qui est derrière un filtre** | Invisible au scanner, existant quand même — §44.5 |
| **Le nombre de zones** | Chaque zone est une campagne de découverte distincte |

**Les cinq lignes annoncent le chapitre 11 du volume Asset Management**, et elles expliquent pourquoi cinq zones sont restées non couvertes chez HELIOMED en février 2026 : **ce n'était pas un défaut de méthode, c'était une conséquence de l'architecture.**

## 45.3 Ce que l'architecture impose à la détection

| Ce que l'architecture détermine | Conséquence sur la détection |
|---|---|
| **Les points de passage** | Ce sont les seuls endroits où l'on peut observer — §43.1 |
| **Le chiffrement de bout en bout** | Rend la sonde réseau inopérante sur le contenu |
| **La position du mandataire** | Détermine si l'identité réelle est visible en aval — §34.2 |
| **La segmentation** | Détermine si un mouvement latéral traverse un point observable |
| **Les composants sans agent** | Créent des angles morts structurels |

⚠️ **La quatrième ligne est celle qui décide de tout.** Dans une architecture plate, un mouvement latéral ne traverse **aucun** point observable : il est invisible par construction. **Segmenter n'est donc pas seulement une mesure de protection, c'est une condition de détection.**

## 45.4 Ce que l'architecture impose à la réponse à incident

| Ce que l'architecture détermine | Conséquence sur la réponse |
|---|---|
| **Les dépendances** | Ce qu'on peut isoler sans arrêter un service |
| **La segmentation** | Si l'isolement est possible du tout |
| **Les chemins d'administration** | Si l'on peut encore administrer un système compromis — §27.4 |
| **Les sauvegardes et leur chemin** | Si la restauration est possible depuis un environnement sain |
| **La journalisation et sa rétention** | **Si l'on peut savoir ce qui s'est passé** — §34.3 |

⚠️ **La troisième ligne est celle qu'on découvre en crise.** Si le chemin d'administration passe par le réseau compromis, on ne peut plus administrer sans risquer d'exposer des identifiants privilégiés. **C'est une décision d'architecture prise des années plus tôt qui détermine ce qu'on peut faire un dimanche soir.**

🔥 **SCÉNARIO — on ne peut isoler que tout ou rien**

| Question | Réponse |
|---|---|
| Symptôme | Compromission confirmée sur un serveur. **Aucun confinement partiel possible** |
| Hypothèse naïve | « Il faut couper le réseau » |
| Dépendance réelle | **Une seule zone** : isoler ce serveur suppose de savoir ce qui en dépend, et rien ne le dit |
| Ce que le schéma aurait dû montrer | L'arbre de dépendance du service — §35.2 |
| Ce que cela coûte | **On coupe tout, ou on ne coupe rien.** Les deux options sont mauvaises |

## 45.5 Le tableau de synthèse

**Ce que le lecteur doit emporter du chapitre** :

| Une décision d'architecture… | …détermine des années plus tard |
|---|---|
| Redonder ou non | **Si un correctif pourra être appliqué** |
| Segmenter ou non | **Si une compromission sera visible** |
| Isoler l'administration ou non | **Si l'on pourra intervenir pendant un incident** |
| Journaliser et conserver ou non | **Si l'on pourra savoir ce qui s'est passé** |
| Documenter les dépendances ou non | **Si l'on pourra confiner sans tout casser** |

> **Aucune de ces cinq lignes ne se rattrape par un produit, un budget ou une procédure.** Elles sont déterminées à la conception, et c'est pourquoi ce volume est le premier de la collection.

## 45.6 🔬 Mini-lab 10 — Placer les cinq actions

**Objectif** — Décider où placer chaque action sur une architecture donnée, et déclarer les zones non couvrables.
**Durée** 40 min · **Difficulté** 🔴 avancé · **Prérequis** chapitres 43 à 45

**L'architecture** : celle du mini-lab 7 — cinq zones, aucune frontière entre DMZ et interne, un annuaire dans le segment des 400 postes, une supervision industrielle joignable depuis les postes.

**Le budget** : trois actions seulement peuvent être financées cette année.

❓ Lesquelles, où, et que déclarez-vous non couvert ?

---

**Corrigé**

**Les trois actions retenues, et leur justification**

| # | Action | Emplacement | Pourquoi celle-ci |
|---|---|---|---|
| **1** | **Segmenter** | Entre les 400 postes et le segment industriel | **Un poste compromis atteint aujourd'hui la supervision sans traverser aucun filtre.** C'est le chemin le plus court vers le risque le plus grave — atteinte à la sûreté, §28.1 |
| **2** | **Segmenter** | Frontière 2, entre DMZ et interne | Sans elle, la DMZ n'en est pas une. Un composant exposé compromis atteint tout — §25.1 |
| **3** | **Journaliser** | Applicatif et annuaire | Les deux seuls points qui connaissent **l'utilisateur réel et l'action** — §43.3 |

**Pourquoi pas les autres**

| Écartée | Motif |
|---|---|
| Sonde réseau au périmètre | Voit ce qui entre, pas les 400 postes — §44.4 |
| Détection sur poste | Souhaitable, mais ne corrige pas les deux brèches structurelles |
| Authentification renforcée | Pertinente, et sans effet tant que la segmentation manque |

**Ce qu'on déclare non couvert**

> *Les échanges à l'intérieur du segment des 400 postes ne sont ni observés, ni filtrés. Une compromission d'un poste atteint les 399 autres sans traverser aucun point de contrôle. Cette situation est connue, non traitée cette année faute de moyens, et réexaminée au budget suivant.*

**Les trois erreurs attendues**

1. **Choisir la sonde réseau au périmètre.** C'est le réflexe, et c'est l'erreur du §44.4 — elle voit le moins de l'activité réelle.
2. **Choisir l'authentification renforcée en premier.** Elle est utile, et elle ne change rien tant qu'un poste compromis atteint la supervision industrielle par un chemin direct.
3. **Ne rien déclarer non couvert.** Trois actions ne couvrent pas tout. **Ce qui n'est pas traité doit être écrit** — sinon c'est un angle mort, pas un arbitrage.

---

> ### 🎓 À ce stade de la Partie VIII, vous savez…
>
> ✓ que toute la sécurité opérationnelle se ramène à **cinq actions**, et que chacune exige un **point d'observation ou de décision** ;
> ✓ que les points où l'on peut agir sont **exactement les points de passage** de l'architecture ;
> ✓ **où chaque action est impossible** — à l'intérieur d'un segment, dans un flux chiffré non terminé, chez un tiers ;
> ✓ que le **mandataire inverse** est le point le plus riche techniquement, et qu'il **ne voit que les accès externes** ;
> ✓ que l'**applicatif** est le seul point qui connaisse l'utilisateur réel et l'action métier — et qu'il reçoit rarement les moyens ;
> ✓ que le **bon emplacement dépend de l'architecture, pas du produit** ;
> ✓ que face à un emplacement impossible, on **déplace, on remplace, ou on déclare non couvert** — jamais on ne fait semblant ;
> ✓ que **segmenter est une condition de détection**, pas seulement une mesure de protection ;
> ✓ qu'une décision d'architecture prise il y a des années détermine **ce que vous pourrez faire un dimanche soir**.
>
> **Ce que vous ne savez pas encore** : comment proposer vous-même une architecture, et comment critiquer celle des autres. C'est l'objet de la Partie IX.

---
