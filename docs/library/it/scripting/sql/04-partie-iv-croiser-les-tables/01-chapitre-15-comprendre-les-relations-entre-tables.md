---
title: Chapitre 15 — Comprendre les relations entre tables
source: IT/07 Scripting & programmation/Langages/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie IV — Croiser les tables
  - index.md
---

## Le minimum à savoir

### Pourquoi croiser les tables ?

Reprenons la base. Si on veut afficher “Alice a emprunté Les Misérables le 10 janvier 2025”, l’information est répartie sur **trois tables** :

```
readers              loans                       books
┌────┬────────────┐  ┌────┬───────────┬─────────┐  ┌────┬─────────────────┐
│ id │ first_name │  │ id │ reader_id │ book_id │  │ id │ title           │
├────┼────────────┤  ├────┼───────────┼─────────┤  ├────┼─────────────────┤
│ 1  │ Alice      │  │ 1  │ 1         │ 1       │  │ 1  │ Les Misérables  │
└────┴────────────┘  └────┴───────────┴─────────┘  └────┴─────────────────┘
       ↑                       ↑           ↑                  ↑
    "Alice"              "id du lecteur"  "id du livre"   "Les Misérables"
```


Pour reconstituer la phrase complète, il faut **joindre** les tables sur leurs identifiants.

C’est ce que fait `JOIN`.

### Les types de relations

|Relation                       |Exemple                                                          |Modélisation                                |
|-------------------------------|-----------------------------------------------------------------|--------------------------------------------|
|**1-N** (un-à-plusieurs)       |Un lecteur a plusieurs emprunts                                  |Clé étrangère dans la table “côté plusieurs”|
|**N-N** (plusieurs-à-plusieurs)|Un livre a plusieurs auteurs ; un auteur a écrit plusieurs livres|Table d’**association** intermédiaire       |

### Une relation 1-N : `readers` → `loans`

Un lecteur peut avoir plusieurs emprunts, mais un emprunt appartient à un seul lecteur.

```
readers (côté "1")              loans (côté "N")
┌────┬────────────┐              ┌────┬───────────┬─────────┐
│ id │ first_name │              │ id │ reader_id │ book_id │
├────┼────────────┤              ├────┼───────────┼─────────┤
│ 1  │ Alice      │ ←──────────  │ 1  │ 1         │ 1       │
│    │            │ ←──────────  │ 3  │ 1         │ 3       │
│    │            │ ←──────────  │ 6  │ 1         │ 6       │
│ 2  │ Karim      │ ←──────────  │ 2  │ 2         │ 2       │
└────┴────────────┘              └────┴───────────┴─────────┘
```


Alice (id=1) a 3 emprunts. Karim (id=1) en a un. La clé étrangère `reader_id` dans `loans` pointe vers `readers.id`.

### Une relation N-N : `books` ↔ `authors`

Un livre peut avoir plusieurs auteurs (un livre coécrit), et un auteur peut avoir écrit plusieurs livres. On ne peut pas modéliser ça avec une simple clé étrangère — il faut une **table d’association**.

```
books                book_authors                  authors
┌────┬──────────┐   ┌─────────┬───────────┐       ┌────┬─────────────────┐
│ id │ title    │   │ book_id │ author_id │       │ id │ name            │
├────┼──────────┤   ├─────────┼───────────┤       ├────┼─────────────────┤
│ 1  │ Les Mis. │ ←─│ 1       │ 1         │──→    │ 1  │ Victor Hugo     │
│ 9  │ N-D Paris│ ←─│ 9       │ 1         │──→    │    │                 │
│ 2  │ 1984     │ ←─│ 2       │ 2         │──→    │ 2  │ George Orwell   │
└────┴──────────┘   └─────────┴───────────┘       └────┴─────────────────┘
```


La table `book_authors` ne contient que des **références** : “le livre 1 a pour auteur l’auteur 1”. Pas de doublons, pas d’incohérence — chaque relation est une ligne.

### Les tables de la base `bibliotheque.db`

|Table         |Type                            |Lien                                                                                                                                                                        |
|--------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|`categories`  |Référence (catégories de livres)|—                                                                                                                                                                           |
|`authors`     |Référence (auteurs)             |—                                                                                                                                                                           |
|`books`       |Entité principale (livres)      |`category_id` → `categories.id`                                                                                                                                             |
|`book_authors`|**Association N-N**             |`book_id` → `books.id`, `author_id` → `authors.id`                                                                                                                          |
|`readers`     |Entité principale (lecteurs)    |—                                                                                                                                                                           |
|`loans`       |Association + données (emprunts)|`reader_id` → `readers.id`, `book_id` → `books.id`                                                                                                                          |
|`staff_users` |Comptes du personnel            |—                                                                                                                                                                           |
|`login_events`|Événements de connexion         |lien logique `username` → `staff_users.username`, **non contraint volontairement** (un attaquant peut tenter avec des comptes inexistants — il faut pouvoir les journaliser)|


> **📋 FIL ROUGE — Épisode 14**
> 
> Nora dessine sur un papier le schéma de la base. Elle se rend compte que c’est presque un graphe : `readers` et `books` sont reliés par `loans`. `books` et `authors` sont reliés par `book_authors`. Cette représentation visuelle l’aide énormément — elle comprend que toutes les questions vont passer par les jointures.

## Très utile en pratique

### Quand utiliser une table d’association ?

Si tu te poses la question “un X peut-il avoir plusieurs Y, et un Y plusieurs X ?” — si oui, c’est du N-N → table d’association.

Exemples classiques :

- Étudiants ↔ cours
- Films ↔ acteurs
- Articles ↔ tags
- Utilisateurs ↔ rôles

## ✅ Tu sais maintenant…

- Pourquoi les données sont réparties sur plusieurs tables
- La relation **1-N** : clé étrangère côté “plusieurs”
- La relation **N-N** : table d’association intermédiaire
- Le schéma complet de la base `bibliotheque.db`

-----
