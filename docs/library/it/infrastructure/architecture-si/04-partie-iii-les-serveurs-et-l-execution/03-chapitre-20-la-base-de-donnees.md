---
title: Chapitre 20 — La base de données
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - PARTIE III — Les serveurs et l'exécution
  - index.md
---

> **Pourquoi elle se trouve au fond dans ce modèle.**

## 20.1 À quoi ça sert

Conserver les données de manière durable, cohérente et interrogeable, en gérant les accès concurrents.

**Pourquoi ça existe comme composant séparé.** Deux utilisateurs qui modifient la même donnée au même instant doivent obtenir un résultat cohérent. C'est ce problème — la concurrence — qui justifie un composant spécialisé, davantage que le stockage lui-même.

## 20.2 Pourquoi elle est au fond, et pourquoi c'est un choix

🖼 **SCHÉMA 20.1 — La raison de l'empilement**

```
   EXPOSÉ, REMPLAÇABLE           web ×3      ← perte = aucune conséquence
        ▲                          │
        │                          ▼
        │                     applicatif      ← perte = service arrêté,
        │                          │             données intactes
        ▼                          ▼
   PROTÉGÉ, IRREMPLAÇABLE       base ×1       ← perte = données perdues

   Dans ce modèle : plus on descend, moins de composants,
   plus de valeur, moins d'exposition, plus de conséquences.
```


⚠️ **Ce schéma décrit le modèle à trois niveaux, pas une propriété générale des systèmes d'information.** Les architectures modernes le cassent régulièrement — stockage objet joignable directement, sources de données multiples, données réparties. Le chapitre 42 y revient.

**Les quatre raisons de cette position** :

| Raison | Explication |
|---|---|
| **Valeur** | Ce qui est irremplaçable doit être le plus loin de l'extérieur |
| **Exposition** | Chaque couche traversée est un contrôle de plus |
| **Redondance décroissante** | Redonder une base est difficile et coûteux |
| **Cycle de vie** | Une base vit dix ou vingt ans ; une couche web se remplace tous les trois ans |

## 20.3 Trois façons de tenir une base

```
  A — EXEMPLAIRE UNIQUE
      [ base ]
      → simple · une panne = arrêt · restauration depuis sauvegarde
      → convient quand l'interruption tolérable dépasse
        le délai de restauration MESURÉ

  B — RÉPLICATION AVEC BASCULE
      [ primaire ] ══► [ secondaire ]
      → interruption courte SI la bascule fonctionne — ⚠️ *principe de preuve*
      → deux exemplaires à exploiter, corriger, surveiller
      → attention : réplication ASYNCHRONE = perte possible
        des dernières transactions

  C — RÉPARTITION SUR PLUSIEURS NŒUDS
      [ nœud 1 ] [ nœud 2 ] [ nœud 3 ]
      → tolérance à la panne d'un nœud
      → un système distribué complet à exploiter — §47.3
```


⚠️ **Le passage de A à B ne se justifie pas par la taille**, mais par la comparaison entre **l'interruption tolérable** et **le délai de restauration mesuré**. Si restaurer prend deux heures et que quatre heures d'arrêt sont acceptables, **l'option A suffit** — et coûte trois fois moins.

⚠️ **Le point que le mode B cache** : une réplication **asynchrone** copie les transactions avec un léger retard. En cas de bascule, **les dernières transactions peuvent être perdues**. C'est un compromis entre performance et perte de données tolérable — et il doit figurer au registre des compromis, §46.5.

## 20.4 Ce qu'il fait à la donnée

Dans ce modèle, elle **porte l'état durable principal** du service.

⚠️ **Ce qu'il ne faut pas en conclure** : la base n'*est* pas la donnée. Elle est **un endroit où une partie de la donnée réside**. Le chapitre 32 montrera que la même donnée existe simultanément dans des réplicas, des sauvegardes, des exports, des rapports, des environnements de recette et des messageries. Confondre les deux conduit à sous-évaluer un périmètre d'impact — §32.2.

## 20.5 S'il disparaît

Dans le modèle à trois niveaux employé ici, ce qui en dépend s'arrête. Et contrairement aux couches au-dessus, sa perte peut être **définitive** : un serveur web se réinstalle en une heure, une base perdue sans sauvegarde valide ne se reconstitue pas.

📌 **Ce qui nuance ce modèle**, et qu'il faut connaître :

| Cas | Effet réel |
|---|---|
| L'application dispose d'un cache | Elle sert des données en lecture pendant un temps |
| Les écritures sont mises en file | Elles sont rejouées ensuite, sans perte |
| L'application utilise plusieurs sources de données | Seule une partie du service s'arrête |
| Base répliquée avec bascule automatique | Interruption courte, **si la bascule fonctionne** — ⚠️ *principe de preuve* |

🔥 **SCÉNARIO — la base répond, le service est lent puis s'arrête**

| Question | Réponse |
|---|---|
| Symptôme | Ralentissement progressif sur deux heures, puis arrêt |
| Hypothèse naïve | « Trop de charge » |
| Dépendance réelle | **Le stockage sous-jacent est saturé.** La base fonctionne, elle ne peut plus écrire |
| Ce que le schéma aurait dû montrer | Que la base dépend d'un stockage partagé, souvent commun à d'autres machines |
| Concevoir différemment | Superviser l'espace disponible, pas seulement l'état du service |

⚠️ **Ce scénario illustre une dépendance en cascade que les schémas ne montrent jamais** : base → stockage → et parfois le même stockage porte l'hyperviseur qui héberge la base.

## 20.6 Sur un schéma

En bas, dans la grande majorité des représentations. Fréquemment en un seul exemplaire, parfois en deux avec une mention de réplication.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On est en cluster » | Plusieurs nœuds de base | **Actif/passif ou actif/actif ? Stockage partagé ou non ?** |
| « On a de la réplication » | Une copie existe | **Synchrone ou asynchrone ?** Combien de données peut-on perdre ? |
| « La bascule est automatique » | Un mécanisme existe | **Quand a-t-elle été testée pour la dernière fois ?** — *principe de preuve* |
| « La base est saturée » | Un seuil est atteint | Espace disque · connexions · mémoire · trois causes distinctes |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Conserver des données cohérentes et durables | **Souvent le point de rupture principal** |
| Gérer les accès concurrents | Une administration spécialisée |
| Se répliquer pour la disponibilité | Une complexité importante · **un basculement à tester** · une perte possible en asynchrone |

⚠️ **Principes du coût et de preuve, appliqués** : une réplication non testée n'est pas une redondance, c'est une **croyance**. Elle figure au schéma, elle rassure, et personne ne sait si le basculement fonctionne.

---
