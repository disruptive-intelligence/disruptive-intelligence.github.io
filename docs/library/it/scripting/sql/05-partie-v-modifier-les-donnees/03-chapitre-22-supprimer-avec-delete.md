---
title: Chapitre 22 — Supprimer avec DELETE
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
DELETE FROM readers
WHERE id = 1;
```


Aussi simple que dangereux. Une seule ligne, mais qui supprime définitivement.

### **LA MÊME RÈGLE ABSOLUE : `SELECT` avant `DELETE`**

> **⚠️ Avant tout `DELETE`, fais TOUJOURS un `SELECT` avec le même `WHERE`** pour vérifier ce que tu vas supprimer.

```sql
-- 1. Vérifier
SELECT * FROM readers WHERE id = 1;

-- 2. Si c'est bien la ligne attendue, supprimer
DELETE FROM readers WHERE id = 1;
```


### L’ERREUR FATALE : oublier le `WHERE`

```sql
DELETE FROM readers;
-- ❌ ❌ ❌ SUPPRIME TOUS LES LECTEURS
```


Sans `WHERE`, **toutes les lignes** de la table sont supprimées. Le contenu est perdu, la table reste (vide). Avec une transaction (Ch.23), on peut annuler. Sans transaction, c’est définitif.

### `DELETE` ne supprime pas la table

`DELETE` supprime des **lignes**, pas la table elle-même. Pour supprimer la table : `DROP TABLE` (à manier avec extrême précaution, voir Ch.24).

|Commande                          |Effet                                                |
|----------------------------------|-----------------------------------------------------|
|`DELETE FROM readers WHERE id = 1`|Supprime une ligne                                   |
|`DELETE FROM readers`             |Supprime **toutes** les lignes (la table reste, vide)|
|`DROP TABLE readers`              |Supprime la table elle-même                          |

### Le piège : les contraintes de clé étrangère

Si tu essaies de supprimer un lecteur qui a des emprunts (dans `loans`), SQL peut **refuser** la suppression à cause de la contrainte `FOREIGN KEY`. C’est une protection — sans elle, tu aurais des emprunts pointant vers un lecteur fantôme.

```sql
DELETE FROM readers WHERE id = 1;
-- ❌ "FOREIGN KEY constraint failed" si Alice a des emprunts dans loans
```


**Solutions :**

1. Supprimer d’abord les lignes liées :

```sql
DELETE FROM loans WHERE reader_id = 1;
DELETE FROM readers WHERE id = 1;
```


1. Ou, mieux, ne pas supprimer mais marquer comme inactif (**soft delete**) :

```sql
-- Hypothétique : si readers avait une colonne is_active (ce qui n'est pas le cas
-- dans notre base de démo). Dans staff_users, en revanche, cette colonne existe :
UPDATE staff_users SET is_active = 0 WHERE id = 4;
```


Cette deuxième approche est très fréquente en pratique — on garde l’historique. La table `staff_users` de notre base de démo l’illustre déjà : Olivier Bernard (id=4) a `is_active = 0`.

> **📋 FIL ROUGE — Épisode 21**
> 
> Un lecteur fantôme : un test inscrit pendant l’apprentissage de Nora a été créé par erreur. Elle veut le supprimer. D’abord, vérification :
> 
> ```sql
> SELECT * FROM readers WHERE first_name = 'Test';
> ```
> 
> Une seule ligne (id=99). Elle vérifie qu’il n’a pas d’emprunt :
> 
> ```sql
> SELECT * FROM loans WHERE reader_id = 99;
> ```
> 
> Aucune. Suppression sécurisée :
> 
> ```sql
> DELETE FROM readers WHERE id = 99;
> ```
> 
> Une ligne supprimée.

## Très utile en pratique

### Le `DELETE` conditionnel

```sql
-- Supprimer les comptes de personnel inactifs depuis plus de 2 ans
DELETE FROM staff_users
WHERE is_active = 0
  AND created_at < DATE('now', '-2 years');
```


Cette requête combine `WHERE` et calcul de date — typique d’une opération de nettoyage.

## ❌ Erreur classique

```sql
-- Oublier le WHERE
DELETE FROM readers;        -- ❌ supprime TOUS les lecteurs

-- Confondre DELETE et DROP TABLE
DELETE TABLE readers;       -- ❌ syntaxe incorrecte
DROP TABLE readers;         -- ❌ supprime la table elle-même !

-- Croire que DELETE est annulable sans transaction
-- → c'est définitif sauf si tu es dans une transaction (BEGIN ... COMMIT/ROLLBACK)
-- → voir Ch.23
```


## 💡 Exercices

1. Supprime les emprunts retournés depuis plus de 30 jours (utilise `julianday`).
1. Supprime les comptes `staff_users` inactifs (`is_active = 0`).
1. Vérifie : combien de lignes contient maintenant chaque table ?

## ✅ Tu sais maintenant…

- La structure : `DELETE FROM table WHERE condition;`
- **TOUJOURS faire un `SELECT` avant** (la règle d’or se répète)
- L’erreur fatale : `DELETE` sans `WHERE` vide la table
- Les contraintes `FOREIGN KEY` peuvent bloquer une suppression
- L’alternative “soft delete” (marquer comme inactif au lieu de supprimer)

-----
