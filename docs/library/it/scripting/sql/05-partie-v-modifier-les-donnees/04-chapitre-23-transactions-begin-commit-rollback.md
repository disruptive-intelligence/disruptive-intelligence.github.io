---
title: 'Chapitre 23 — Transactions : BEGIN, COMMIT, ROLLBACK'
source: IT/07 Scripting & programmation/Langages/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie V — Modifier les données
  - index.md
---

## Le minimum à savoir

### Le problème : et si je me trompe ?

Tu lances un `UPDATE`, tu te rends compte 2 secondes après que tu as oublié le `WHERE`. Tu as modifié toute la table. Que faire ?

Sans transaction : **rien**. Les modifications sont permanentes.

Avec transaction : tu peux **annuler**.

### Le concept

Une **transaction** est un **bloc** de modifications qu’on valide ou qu’on annule en bloc. Tant que tu n’as pas validé, rien n’est définitif.

```sql
BEGIN;                                         -- ouvrir la transaction

UPDATE readers SET city = 'Paris' WHERE id = 1;
DELETE FROM loans WHERE id = 99;

-- À ce stade, rien n'est encore enregistré définitivement.

COMMIT;                                        -- valider (rendre permanent)
-- OU
ROLLBACK;                                      -- annuler tout
```


### Les 3 mots-clés

|Mot-clé                           |Effet                                                    |
|----------------------------------|---------------------------------------------------------|
|`BEGIN;` (ou `BEGIN TRANSACTION;`)|Ouvre une transaction                                    |
|`COMMIT;`                         |Valide tout — les modifications deviennent permanentes   |
|`ROLLBACK;`                       |Annule tout — la base revient à l’état d’avant le `BEGIN`|

### Le scénario typique

```sql
BEGIN;

-- Faire les modifications
UPDATE readers SET city = 'Lyon' WHERE id = 1;

-- Vérifier
SELECT * FROM readers WHERE id = 1;

-- Si OK :
COMMIT;

-- Si pas OK :
ROLLBACK;
```


> **À retenir :** mettre tes opérations risquées (UPDATE/DELETE/INSERT en masse) dans `BEGIN ... COMMIT` te donne un filet de sécurité. C’est la pratique professionnelle standard.

### ACID en aperçu

Les transactions garantissent les propriétés **ACID** :

|Lettre        |Signification         |Ce que ça veut dire                                        |
|--------------|----------------------|-----------------------------------------------------------|
|**A**tomicité |“Tout ou rien”        |Soit toutes les modifs sont appliquées, soit aucune        |
|**C**ohérence |Règles respectées     |La base reste valide (contraintes respectées)              |
|**I**solation |Pas d’interférence    |Plusieurs transactions parallèles ne se voient pas en cours|
|**D**urabilité|Permanent après COMMIT|Une fois commité, ça reste — même en cas de crash          |


> **À retenir :** ACID c’est la garantie offerte par tout SGBD relationnel sérieux. C’est ce qui te permet de faire des virements bancaires sans qu’une coupure de courant ne crée d’incohérence.

> **📋 FIL ROUGE — Épisode 22**
> 
> Nora doit faire un nettoyage : marquer comme `'returned'` une vingtaine d’emprunts anciens, et supprimer 5 lecteurs de test. Elle ouvre une transaction :
> 
> ```sql
> BEGIN;
> UPDATE loans SET status = 'returned', return_date = '2024-12-31' WHERE status = 'late' AND loan_date < '2024-06-01';
> DELETE FROM readers WHERE first_name = 'Test';
> -- Vérification
> SELECT COUNT(*) FROM loans WHERE status = 'late';
> SELECT COUNT(*) FROM readers WHERE first_name = 'Test';
> -- Tout est bon
> COMMIT;
> ```
> 
> Si elle avait constaté une erreur, `ROLLBACK` aurait tout annulé. Filet de sécurité activé.

## Très utile en pratique

### Quand utiliser une transaction ?

|Opération                                                            |Transaction recommandée ?|
|---------------------------------------------------------------------|-------------------------|
|`SELECT` simple                                                      |Non                      |
|`INSERT` ponctuel                                                    |Optionnel                |
|`UPDATE` ou `DELETE` sur plusieurs lignes                            |**Oui**                  |
|Plusieurs modifications liées (ex : transfert d’un compte à un autre)|**Oui, obligatoire**     |
|Migration de données, refonte de la base                             |**Oui, obligatoire**     |

### Le cas d’école : le transfert bancaire

```sql
BEGIN;
UPDATE comptes SET solde = solde - 100 WHERE id = 1;     -- débite Alice
UPDATE comptes SET solde = solde + 100 WHERE id = 2;     -- crédite Bob
COMMIT;
```


Si la deuxième requête échoue (panne, erreur), un `ROLLBACK` annule la première. **Sans transaction**, Alice perdrait 100€ et Bob ne les recevrait pas — l’argent disparaîtrait.

C’est pour ça que toutes les applications financières utilisent des transactions.

## ❌ Erreur classique

```sql
-- Oublier le COMMIT (les modifs ne sont pas enregistrées définitivement)
BEGIN;
UPDATE readers SET city = 'Paris' WHERE id = 1;
-- (la session se ferme sans COMMIT)
-- → les modifications sont annulées par le SGBD au moment de la déconnexion

-- Faire un COMMIT accidentel à la place de ROLLBACK
BEGIN;
DELETE FROM readers;        -- ❌ erreur ! Toute la table
COMMIT;                      -- ❌ ❌ tu valides l'erreur
-- → trop tard, c'est permanent (sauf sauvegarde)

-- Bonne pratique : faire un SELECT après les modifs et avant le COMMIT
BEGIN;
UPDATE readers SET city = 'Paris' WHERE last_name = 'Martin';
SELECT * FROM readers WHERE last_name = 'Martin';   -- vérifier
COMMIT;   -- ou ROLLBACK selon le résultat
```


## 💡 Exercices

1. Ouvre une transaction. Insère un nouveau lecteur. Vérifie avec un `SELECT`. Annule avec `ROLLBACK`. Vérifie qu’il n’est plus là.
1. Refais la même chose, mais cette fois `COMMIT`. Vérifie qu’il est bien là après.
1. Ouvre une transaction, supprime tous les emprunts retournés (`DELETE FROM loans WHERE status = 'returned'`), regarde le nombre de lignes restantes, puis `ROLLBACK`. Vérifie que la base est revenue à l’état initial.

## ✅ Tu sais maintenant…

- Une transaction est un bloc `BEGIN ... COMMIT;` (ou `ROLLBACK;`)
- `BEGIN` ouvre, `COMMIT` valide définitivement, `ROLLBACK` annule
- Les transactions sont ton filet de sécurité pour les opérations risquées
- Les propriétés **ACID** : Atomicité, Cohérence, Isolation, Durabilité
- Toutes les applications critiques utilisent des transactions

-----
