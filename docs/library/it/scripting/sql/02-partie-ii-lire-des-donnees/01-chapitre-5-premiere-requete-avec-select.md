---
title: Chapitre 5 — Première requête avec SELECT
source: IT/07 Scripting & programmation/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie II — Lire des données
  - index.md
---

## Le minimum à savoir

### La requête de base : `SELECT ... FROM`

Toute lecture de données commence par `SELECT` :

```sql
SELECT * FROM readers;
```


Décomposé :

- `SELECT` → “je veux lire”
- `*` → “toutes les colonnes”
- `FROM readers` → “depuis la table `readers`”
- `;` → fin de la requête

Le résultat : toutes les lignes et toutes les colonnes de la table `readers`.

### Sélectionner certaines colonnes

Plutôt que tout afficher, choisis les colonnes utiles :

```sql
SELECT first_name, last_name, email
FROM readers;
```


Tu obtiens uniquement le prénom, le nom et l’email — plus lisible quand la table a beaucoup de colonnes.

### L’ordre des colonnes

L’ordre dans lequel tu listes les colonnes après `SELECT` est l’ordre dans lequel elles s’affichent :

```sql
SELECT email, last_name, first_name
FROM readers;
```


Ça affiche d’abord l’email, puis le nom, puis le prénom. Tu choisis ton ordre.

### Le point-virgule final

En SQL, chaque requête se termine par un point-virgule `;`. C’est ce qui dit au moteur “j’ai fini, exécute”.

Dans DB Browser, tu peux te passer du `;` quand tu n’exécutes qu’une seule requête. Mais prends le réflexe — c’est obligatoire dans la plupart des outils.

### La convention : SQL en MAJUSCULES

Par convention, on écrit les **mots-clés SQL** (`SELECT`, `FROM`, `WHERE`…) en majuscules, et les **noms de tables/colonnes** en minuscules. C’est juste une convention de lisibilité — SQL n’est pas sensible à la casse pour les mots-clés :

```sql
-- ✅ Convention recommandée (lisible)
SELECT first_name, last_name FROM readers;

-- ⚠️ Marche aussi, mais moins lisible
select first_name, last_name from readers;
```


> **📋 FIL ROUGE — Épisode 4**
> 
> La directrice demande à Nora : “Combien de lecteurs avons-nous, et qui sont-ils ?”. Nora ouvre DB Browser et tape sa toute première requête : `SELECT * FROM readers;`. Le résultat s’affiche : 15 lecteurs. Premier succès. Mais elle réalise vite qu’afficher *toutes* les colonnes est trop bavard — elle simplifie : `SELECT first_name, last_name, city FROM readers;`. Plus lisible.

## Très utile en pratique

### `SELECT *` vs colonnes explicites

|Approche                |Quand l’utiliser                                    |
|------------------------|----------------------------------------------------|
|`SELECT *`              |Pour explorer une table, voir ce qu’elle contient   |
|`SELECT col1, col2, ...`|Pour les requêtes finales, les rapports, les exports|


> **Bonne pratique :** `SELECT *` est pratique pour explorer, mais évite-le dans les requêtes “de production”. Pourquoi ? Parce que si la table évolue (nouvelles colonnes), ton résultat change sans que tu ne contrôles rien.

## ❌ Erreur classique

```sql
-- Oublier le FROM
SELECT first_name, last_name;       -- ❌ "no such column" ou "missing FROM clause"
SELECT first_name, last_name FROM readers;  -- ✅

-- Mettre une virgule de trop
SELECT first_name, last_name, FROM readers;  -- ❌ erreur de syntaxe
SELECT first_name, last_name FROM readers;   -- ✅

-- Confondre nom de colonne et nom de table
SELECT readers FROM readers;        -- ❌ "readers" n'est pas une colonne
SELECT * FROM readers;              -- ✅
```


## 💡 Exercices

1. Affiche tous les livres (table `books`).
1. Affiche uniquement le titre et l’année de publication des livres.
1. Affiche le nom complet et la ville des lecteurs.

## ✅ Tu sais maintenant…

- La structure de base : `SELECT colonnes FROM table;`
- `SELECT *` pour toutes les colonnes
- Choisir et ordonner les colonnes manuellement
- La convention : mots-clés SQL en majuscules
- Le point-virgule final

-----
