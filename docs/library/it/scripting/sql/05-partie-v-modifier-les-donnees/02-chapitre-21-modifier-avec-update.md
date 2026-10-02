---
title: Chapitre 21 — Modifier avec UPDATE
source: IT/07 Scripting & programmation/Langages/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie V — Modifier les données
  - index.md
---

## Le minimum à savoir

### La structure de base

```sql
UPDATE readers
SET email = 'alice.martin.new@example.com'
WHERE id = 1;
```


Décodage :

- `UPDATE readers` → modifier la table `readers`
- `SET email = ...` → la colonne et sa nouvelle valeur
- `WHERE id = 1` → **uniquement** la ligne où `id = 1`

### Modifier plusieurs colonnes

```sql
UPDATE readers
SET email = 'new@example.com', city = 'Lyon'
WHERE id = 1;
```


Sépare les colonnes par des virgules dans `SET`.

### **LA RÈGLE ABSOLUE : toujours faire un `SELECT` avant**

> **⚠️ Avant tout `UPDATE`, fais TOUJOURS un `SELECT` avec le même `WHERE`** pour vérifier ce que tu vas modifier.

```sql
-- 1. Vérifier ce qu'on va modifier
SELECT * FROM readers WHERE id = 1;

-- 2. Si c'est bien la ligne attendue, modifier
UPDATE readers
SET email = 'alice.martin.new@example.com'
WHERE id = 1;
```


C’est la règle d’or. Toute personne qui a fait du SQL en production a déjà fait l’erreur de modifier toute une table en oubliant le `WHERE`. C’est ainsi qu’on perd ses données.

### L’ERREUR FATALE : oublier le `WHERE`

```sql
UPDATE readers
SET city = 'Paris';
-- ❌ ❌ ❌ MET TOUS LES LECTEURS À PARIS
```


Sans `WHERE`, SQL applique l’`UPDATE` à **toutes les lignes** de la table. Pour 15 lecteurs, c’est gênant. Pour 1 million d’utilisateurs, c’est une catastrophe — et la plupart du temps, c’est irréversible (sauf si tu travailles dans une transaction, voir Ch.23).

> **À retenir :** `UPDATE` sans `WHERE` modifie **toute la table**. C’est l’erreur n°1 en SQL. Le mécanisme de protection s’appelle… le `SELECT` préalable et la transaction.

### Modifier en se basant sur la valeur actuelle

Tu peux référencer la valeur existante dans `SET` :

```sql
-- Ajouter " (vérifié)" à la fin de tous les emails
UPDATE readers
SET email = email || ' (vérifié)'
WHERE id = 1;
```


> **📋 FIL ROUGE — Épisode 20**
> 
> Une lectrice signale qu’elle a déménagé. Nora lui demande son ancien et son nouveau nom de ville pour bien identifier. Avant de modifier, elle vérifie :
> 
> ```sql
> SELECT * FROM readers WHERE last_name = 'Martin' AND city = 'Paris';
> ```
> 
> Plusieurs lignes — il y a 2 Alice Martin ! Nora demande l’id de la lectrice et corrige :
> 
> ```sql
> SELECT * FROM readers WHERE id = 10;
> -- (vérification)
> UPDATE readers SET city = 'Toulouse' WHERE id = 10;
> ```
> 
> Une seule ligne modifiée. Sans le `SELECT` préalable, elle aurait pu modifier la mauvaise Alice.

## Très utile en pratique

### Combiner `UPDATE` et calcul

```sql
-- Marquer comme retournés tous les emprunts en retard de plus de 30 jours
UPDATE loans
SET status = 'returned', return_date = DATE('now')
WHERE status = 'late'
  AND julianday('now') - julianday(loan_date) > 30;
```


Trois choses à noter :

- On modifie deux colonnes en une fois
- La condition `WHERE` peut être complexe
- `julianday()` permet de calculer une différence de jours

## ❌ Erreur classique

```sql
-- L'erreur fatale : oublier le WHERE
UPDATE readers SET city = 'Paris';      -- ❌ ❌ ❌

-- Confondre UPDATE et SELECT
UPDATE readers WHERE id = 1 SET city = 'Lyon';   -- ❌ syntaxe incorrecte
UPDATE readers SET city = 'Lyon' WHERE id = 1;   -- ✅

-- Mettre les valeurs sans guillemets
UPDATE readers SET city = Paris WHERE id = 1;    -- ❌ "Paris" pris comme une colonne
UPDATE readers SET city = 'Paris' WHERE id = 1;  -- ✅
```


## 💡 Exercices

1. Modifie l’email du lecteur d’id 3 vers `'lea.dubois.nouveau@example.com'`. Fais d’abord un `SELECT` !
1. Marque comme `'returned'` tous les emprunts dont le `return_date` est renseigné mais qui sont encore en `'late'`.
1. Mets la ville en majuscules pour tous les lecteurs habitant à Paris (utilise `UPPER`).

## ✅ Tu sais maintenant…

- La structure : `UPDATE table SET col = val WHERE condition;`
- **TOUJOURS faire un `SELECT` avec le même `WHERE` avant**
- L’erreur fatale : `UPDATE` sans `WHERE` modifie toute la table
- Modifier plusieurs colonnes en une requête
- Référencer la valeur existante dans `SET` (`SET col = col + 1`)

-----
