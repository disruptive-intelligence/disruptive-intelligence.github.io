---
title: 'Chapitre 28 — Index et performance : introduction'
source: IT/Culture/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie VII — Pour aller plus loin — 🔴 Bonus
  - index.md
---

## Le minimum à savoir

### Pourquoi une requête est-elle parfois lente ?

Quand tu écris `SELECT * FROM readers WHERE email = 'alice@example.com'`, le moteur doit parcourir **toutes les lignes** de la table pour trouver celles qui correspondent. Sur 15 lignes, c’est instantané. Sur 10 millions, c’est très lent.

**L’index** est la solution.

### L’analogie du livre

Imagine un livre de 1000 pages. Tu cherches le mot “transaction”.

- **Sans index** : tu parcours toutes les pages une par une.
- **Avec un index** (à la fin du livre) : tu vas directement à la page indiquée.

Un **index SQL** fonctionne pareil — c’est une structure annexe qui pointe rapidement vers les lignes contenant une certaine valeur.

### Créer un index

```sql
CREATE INDEX idx_readers_email
ON readers(email);
```


Décodage :

- `CREATE INDEX idx_readers_email` → un index nommé (par convention : `idx_table_colonne`)
- `ON readers(email)` → sur la colonne `email` de la table `readers`

Maintenant, `SELECT * FROM readers WHERE email = 'alice@example.com'` est ultra-rapide même avec des millions de lignes.

### Les colonnes naturellement indexées

|Colonne                   |Indexée par défaut ?         |
|--------------------------|-----------------------------|
|`PRIMARY KEY`             |✅ Oui, automatiquement       |
|`UNIQUE`                  |✅ Oui, automatiquement       |
|Colonne avec `FOREIGN KEY`|❌ Non, à indexer manuellement|
|Colonnes ordinaires       |❌ Non                        |


> **À retenir :** les clés primaires et `UNIQUE` sont déjà indexées. Pour le reste — surtout les clés étrangères et les colonnes souvent filtrées — il faut créer l’index manuellement.

### Quand créer un index ?

**Bonnes raisons :**

- Une colonne est souvent dans le `WHERE`
- Une colonne est souvent dans les conditions `JOIN ... ON`
- Une colonne est souvent dans `ORDER BY`

**Mauvaises raisons :**

- “Au cas où” → un index a un coût (voir ci-dessous)
- Indexer toutes les colonnes → ralentit énormément les écritures

### Le coût d’un index

Un index a deux coûts :

1. **Espace disque** : l’index est une structure annexe qui prend de la place
1. **Ralentissement des écritures** : à chaque `INSERT`/`UPDATE`/`DELETE`, l’index doit être mis à jour

Sur les bases en lecture quasi-exclusive, indexer généreusement. Sur les bases en écriture intensive, indexer parcimonieusement. C’est un arbitrage classique.

### Mention : `EXPLAIN QUERY PLAN`

SQLite (et tous les SGBD) ont une commande pour voir comment une requête sera exécutée :

```sql
EXPLAIN QUERY PLAN
SELECT * FROM readers WHERE email = 'alice@example.com';
```


Le résultat te dit si l’index est utilisé. C’est utile pour le debug de performance, mais c’est un sujet plus avancé — on le mentionne ici, on n’en fait pas plus.

> **📋 FIL ROUGE — Épisode 27**
> 
> La base est encore petite, mais Nora anticipe sa croissance. Elle ajoute deux index sur les colonnes les plus filtrées :
> 
> ```sql
> CREATE INDEX idx_loans_reader_id ON loans(reader_id);
> CREATE INDEX idx_loans_book_id ON loans(book_id);
> ```
> 
> Désormais, les jointures `loans` ↔ `readers` et `loans` ↔ `books` seront rapides même avec 100 000 emprunts.

## ❌ Erreur classique

```sql
-- Croire qu'indexer tout est gratuit
-- → Sur une table avec 50 colonnes, tu ne crées pas 50 index !
-- → Indexer ce qui est *réellement* utilisé dans WHERE / JOIN / ORDER BY

-- Oublier d'indexer une FOREIGN KEY
-- → Les jointures sur cette colonne seront lentes
-- → Toujours indexer les FK que tu joindras

-- Croire qu'un index sur (a, b) accélère un WHERE b = ...
-- → Un index composite est ordonné — il accélère a, ou (a, b), mais pas b seul
```


## ✅ Tu sais maintenant…

- Un index accélère les recherches comme l’index d’un livre
- Les `PRIMARY KEY` et `UNIQUE` sont auto-indexées
- Les `FOREIGN KEY` ne le sont **pas** par défaut — à indexer manuellement
- Un index a un coût (espace + écritures)
- `EXPLAIN QUERY PLAN` permet de vérifier l’utilisation des index

-----
