---
title: Chapitre 2 — Comprendre le modèle relationnel
source: IT/07 Scripting & programmation/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie I — Comprendre les bases
  - index.md
---

## Le minimum à savoir

### Les briques fondamentales

Une base de données **relationnelle** est organisée en **tables**, chacune ressemblant à un tableau structuré.

```
Table : readers
┌────┬────────────┬───────────┬──────────────────────┬────────┐
│ id │ first_name │ last_name │ email                │ city   │
├────┼────────────┼───────────┼──────────────────────┼────────┤
│ 1  │ Alice      │ Martin    │ alice@example.com    │ Paris  │
│ 2  │ Karim      │ Bernard   │ karim@example.com    │ Lyon   │
│ 3  │ Léa        │ Dubois    │ lea.dubois@mail.fr   │ Paris  │
└────┴────────────┴───────────┴──────────────────────┴────────┘
   ↑       ↑           ↑             ↑                  ↑
 colonnes (champs) — chacune a un nom et un type
```


Vocabulaire :

|Terme                  |Signification                                           |
|-----------------------|--------------------------------------------------------|
|**Table**              |Un tableau de données (`readers` = les lecteurs)        |
|**Colonne (column)**   |Un champ — une propriété (`first_name`, `email`, `city`)|
|**Ligne (row, record)**|Un enregistrement — une instance (un lecteur précis)    |
|**Valeur**             |Le contenu d’une cellule (`Alice`, `Paris`)             |


> **Note :** une table SQL ressemble à une feuille Excel, à une grande différence près — chaque colonne a un **type fixé** (texte, nombre, date…) et des **règles** qui empêchent les incohérences.

### La clé primaire

La **clé primaire** (primary key) est une colonne qui identifie de façon **unique** chaque ligne d’une table. Souvent, c’est une colonne `id` qui contient un nombre auto-incrémenté.

```
readers
┌────┬────────────┐
│ id │ first_name │  ← id est la clé primaire
├────┼────────────┤
│ 1  │ Alice      │
│ 2  │ Karim      │
│ 3  │ Léa        │  ← chaque id est unique
└────┴────────────┘
```


Pourquoi c’est crucial ? Parce que dans la vraie vie, plusieurs personnes peuvent s’appeler “Alice Martin”. Mais l’**id** est unique. Quand tu cherches “le lecteur d’id 1”, il n’y en a qu’un — pas d’ambiguïté.

### Plusieurs tables, et des liens entre elles

Une médiathèque ne stocke pas que des lecteurs. Elle stocke aussi des **livres** :

```
Table : books
┌────┬─────────────────────┬────────────────────┐
│ id │ title               │ category           │
├────┼─────────────────────┼────────────────────┤
│ 4  │ Les Misérables      │ Roman              │
│ 7  │ 1984                │ Roman              │
│ 12 │ Sapiens             │ Histoire           │
└────┴─────────────────────┴────────────────────┘
```


Et des **emprunts** — c’est ici que la magie du modèle relationnel opère :

```
Table : loans
┌────┬───────────┬─────────┬────────────┐
│ id │ reader_id │ book_id │ loan_date  │
├────┼───────────┼─────────┼────────────┤
│ 1  │ 1         │ 4       │ 2026-01-10 │  ← Alice (id=1) a emprunté Les Misérables (id=4)
│ 2  │ 2         │ 7       │ 2026-01-12 │  ← Karim (id=2) a emprunté 1984 (id=7)
│ 3  │ 1         │ 12      │ 2026-01-15 │  ← Alice (id=1) a aussi emprunté Sapiens (id=12)
└────┴───────────┴─────────┴────────────┘
```


Au lieu de répéter “Alice Martin” et “Les Misérables” dans chaque ligne d’emprunt, on stocke seulement les **identifiants** : `reader_id = 1` et `book_id = 4`.

### La clé étrangère

`reader_id` dans la table `loans` est une **clé étrangère** (foreign key). Elle pointe vers la **clé primaire** `id` de la table `readers`. C’est ce qui crée la **relation** entre les deux tables.

```
   loans                                  readers
   ┌────┬───────────┬─────────┐          ┌────┬────────────┐
   │ id │ reader_id │ book_id │          │ id │ first_name │
   ├────┼───────────┼─────────┤          ├────┼────────────┤
   │ 1  │     1 ────┼─────────┼─────────→│ 1  │ Alice      │
   │ 2  │     2 ────┼─────────┼─────────→│ 2  │ Karim      │
   └────┴───────────┴─────────┘          └────┴────────────┘
            clé étrangère                       clé primaire
```


> **À retenir :** la clé primaire **identifie**, la clé étrangère **relie**. C’est le concept central du modèle relationnel — la “relation” dans “base de données relationnelle” vient de là.

### Pourquoi séparer les données ?

Trois raisons fondamentales :

1. **Éviter les doublons** : on stocke “Alice Martin” une seule fois (dans `readers`), pas dans chaque emprunt
1. **Garantir la cohérence** : si Alice change d’email, on le modifie en un seul endroit
1. **Permettre les relations** : un lecteur peut avoir 50 emprunts sans qu’on duplique 50 fois ses informations

> **📋 FIL ROUGE — Épisode 2**
> 
> Nora ouvre la base `bibliotheque.db` et découvre 8 tables : `readers`, `books`, `authors`, `categories`, `book_authors`, `loans`, `staff_users`, `login_events`. Au début, ça l’intimide. Puis elle comprend la logique : chaque entité a sa table (lecteurs, livres, auteurs…), et les tables d’**association** comme `book_authors` ou `loans` font le lien entre elles. Le schéma devient lisible.

## Très utile en pratique

### Les types de relations

|Relation                       |Exemple                                                                       |Comment c’est modélisé                                    |
|-------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------|
|**Un-à-plusieurs (1-N)**       |Un lecteur a plusieurs emprunts                                               |Une clé étrangère dans la table “côté plusieurs”          |
|**Plusieurs-à-plusieurs (N-N)**|Un livre peut avoir plusieurs auteurs ; un auteur peut écrire plusieurs livres|Une table d’**association** intermédiaire (`book_authors`)|
|**Un-à-un (1-1)**              |Un utilisateur a un profil détaillé                                           |Rare, géré par une clé étrangère unique                   |

On reverra tout ça en détail au Ch.15 quand on attaquera les jointures.

## ✅ Tu sais maintenant…

- Une base relationnelle est composée de **tables** (lignes + colonnes)
- La **clé primaire** identifie de façon unique chaque ligne
- La **clé étrangère** relie une table à une autre
- Les données sont **séparées** pour éviter les doublons et garantir la cohérence
- Les relations 1-N et N-N sont les patterns de base du modèle relationnel

-----
