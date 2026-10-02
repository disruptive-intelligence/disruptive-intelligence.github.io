---
title: Chapitre 49 — Critiquer une architecture
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE IX — Concevoir
  - index.md
---

> La compétence de fin de cours, et la plus délicate à exercer.

## 49.1 La grille en six points

```
  ①  POINT FORT             Ce qui est bien pensé, et pourquoi
  ②  POINT FAIBLE           Ce qui est fragile, et sous quelle condition
  ③  POINT DE RUPTURE       Ce qui n'a pas de doublure
  ④  DÉPENDANCE CACHÉE      Ce dont tout dépend et qui n'est pas dessiné
  ⑤  RISQUE PRINCIPAL       Le scénario le plus probable et le plus coûteux
  ⑥  AMÉLIORATION           Le meilleur rapport effet/coût — une seule
```


**L'ordre compte, et le premier point aussi.** Une critique qui commence par les faiblesses ne sera pas entendue par ceux qui ont conçu l'architecture. **Commencer par ce qui est bien pensé n'est pas une politesse : c'est une condition d'efficacité.**

## 49.2 Ce qui distingue une critique utile

| Critique inutile | Critique utile |
|---|---|
| « Il n'y a pas de zone démilitarisée » | « Aucun service n'est publié aujourd'hui. Si l'un devait l'être, la publication directe deviendrait un problème — c'est le déclencheur à surveiller » |
| « L'applicatif n'est pas redondé » | « L'applicatif est unique. Est-ce un arbitrage documenté ? Si oui, quelle interruption a été jugée tolérable ? » |
| « Cette passerelle ne devrait pas exister » | « Cette passerelle date de 2018 et porte un export vers le contrôle de gestion. Le besoin existe-t-il encore, et peut-il passer autrement ? » |
| « C'est du legacy » | « Ce composant a quinze ans. Que dépend de lui, et l'éditeur le supporte-t-il encore ? » |

⚠️ **Le point commun des critiques utiles** : elles **posent une question** au lieu d'énoncer un verdict, et elles supposent que la personne en face avait une raison — chapitre 4.

## 49.3 Les cinq erreurs du critique débutant

| Erreur | Pourquoi c'est une erreur |
|---|---|
| **Juger sans demander l'histoire** | §4.4 — chaque anomalie a une date |
| **Comparer à un idéal théorique** | Aucune architecture réelle n'y ressemble |
| **Traiter la taille comme une norme** | *Principe de la contrainte* |
| **Proposer dix améliorations** | Aucune ne sera faite. **Une seule sera peut-être faite** |
| **Oublier le coût de sa propre proposition** | *Principe du coût* — ajouter n'est jamais gratuit |

**La quatrième est la plus coûteuse en crédibilité.** Une liste de dix recommandations est reçue comme un jugement global ; une recommandation unique, chiffrée et justifiée est reçue comme une contribution.

## 49.4 Formuler une critique qui sera entendue

🧪 **EN PRATIQUE — le format en cinq lignes**

```
CE QUI FONCTIONNE      [1 à 2 éléments, précis]
CE QUE J'AI OBSERVÉ    [le constat, factuel, sans jugement]
CE QUE JE N'AI PAS SU  [ce qui manque pour conclure — souvent l'histoire]
LE RISQUE              [scénario, probabilité, conséquence]
CE QUE JE PROPOSE      [une action, son coût, son effet attendu]
```


**La troisième ligne est celle qui change la réception.** Dire *« je n'ai pas su pourquoi l'applicatif n'est pas redondé »* ouvre une conversation ; dire *« l'applicatif n'est pas redondé »* ferme la porte.

## 49.5 🔬 Mini-lab 13 — Critiquer trois architectures

**Objectif** — Appliquer la grille en six points et produire une critique en cinq lignes.
**Durée** 45 min · **Difficulté** 🔴 avancé · **Prérequis** chapitres 36, 47, 49

Trois architectures : celle d'Atelier Martin · celle du mini-lab 7 · celle du §37.4, avec `HERMES`.

---

**Corrigé — Atelier Martin**

| Point | Constat |
|---|---|
| ① Fort | **L'architecture est proportionnée** : deux segments, peu de composants, exploitable par une personne à mi-temps. C'est cohérent |
| ② Faible | Les machines à commande numérique sont sur le segment bureautique |
| ③ Rupture | Le contrôleur d'annuaire unique · le pare-feu tout-en-un |
| ④ Dépendance cachée | Le prestataire local, **avec un accès permanent et aucune traçabilité** |
| ⑤ Risque principal | Un poste bureautique compromis atteint les machines de production. **Conséquence : arrêt de production, et potentiellement sûreté** |
| ⑥ Amélioration | **Une seule** : séparer le segment atelier. Coût faible, effet majeur |

**La critique en cinq lignes** :

> *Ce qui fonctionne : l'architecture est dimensionnée pour ce que l'organisation peut exploiter, ce qui est rare et précieux.*
> *Ce que j'ai observé : les deux machines à commande numérique sont sur le même segment que les postes bureautiques.*
> *Ce que je n'ai pas su : si cette situation résulte d'un choix ou de l'absence de question posée.*
> *Le risque : un poste compromis — une voie d'entrée majeure — atteint directement les machines de production. Conséquence : arrêt de production, et selon les machines, question de sûreté.*
> *Ce que je propose : séparer le segment atelier. Un commutateur et une règle de filtrage sur le boîtier existant. Coût faible, c'est la seule action que je recommande cette année.*

⚠️ **Ce que la critique ne dit pas** : que l'absence d'annuaire redondé est un problème. Elle en est un techniquement, et **elle n'est pas la priorité** — §49.3, quatrième erreur.

⚠️ **Cohérence avec le §36.4** : la grille en six points **relève** six éléments, la critique formulée **n'en propose qu'un**. Les cinq autres constats servent à établir que le sixième est bien le plus urgent — ils ne sont pas énoncés en réunion.

---
