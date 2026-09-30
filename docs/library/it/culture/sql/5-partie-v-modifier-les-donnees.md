---
title: PARTIE V — MODIFIER LES DONNÉES
source: IT/Culture/SQL.md
note: SQL
chapter: 5
chapters: 8
---

> **⚠️ Important — À partir de cette partie, travaille sur une copie de la base.**
> 
> Les chapitres `INSERT`, `UPDATE` et `DELETE` modifient réellement les données. Avant de commencer :
> 
> - **Option simple :** copie le fichier `bibliotheque.db` en `bibliotheque_lab.db` et travaille sur la copie. Si tu casses quelque chose, tu réimportes le script du Ch.4.
> - **Option recommandée :** apprends et utilise systématiquement les transactions (`BEGIN ... ROLLBACK`) pour t’entraîner sans altérer la base. Le Ch.23 te l’apprend formellement, mais tu peux déjà l’utiliser dès maintenant.
> 
> Si tu casses la base par accident, ce n’est pas grave : il te suffit de relancer le script du Ch.4 (qui est rejouable grâce aux `DROP TABLE IF EXISTS`).

-----


## Chapitre 20 — Ajouter des données avec INSERT

### Le minimum à savoir

#### La structure de base

```sql
INSERT INTO readers (first_name, last_name, email, city, registration_date)
VALUES ('Marie', 'Lefort', 'marie.lefort@example.com', 'Paris', '2025-12-01');
```

Décodage :

- `INSERT INTO readers` → “ajouter dans la table `readers`”
- `(first_name, last_name, email, city, registration_date)` → les colonnes que tu remplis
- `VALUES (...)` → les valeurs, **dans le même ordre** que les colonnes

#### Insérer plusieurs lignes en une fois

```sql
INSERT INTO readers (first_name, last_name, email, city, registration_date)
VALUES
    ('Marie', 'Lefort', 'marie@example.com', 'Paris', '2025-12-01'),
    ('Paul', 'Dupuis', 'paul@example.com', 'Lyon', '2025-12-02'),
    ('Anne', 'Roy', NULL, 'Bordeaux', '2025-12-03');
```

Une seule requête, trois lignes ajoutées.

#### Omettre des colonnes : valeurs par défaut

Tu peux omettre certaines colonnes — elles prendront leur valeur par défaut (souvent `NULL`, ou ce qui est défini dans `CREATE TABLE`).

```sql
-- email et phone ne sont pas listés → ils prendront NULL
INSERT INTO readers (first_name, last_name, city, registration_date)
VALUES ('Sophia', 'Lambert', 'Paris', '2025-12-04');
```

> **À retenir :** une colonne marquée `NOT NULL` (sans valeur par défaut) doit obligatoirement recevoir une valeur — sinon erreur.

#### L’ordre des valeurs doit correspondre à l’ordre des colonnes

```sql
INSERT INTO readers (first_name, last_name, email)
VALUES ('Marie', 'Lefort', 'marie@example.com');     -- ✅ correspondance

INSERT INTO readers (first_name, last_name, email)
VALUES ('marie@example.com', 'Marie', 'Lefort');     -- ❌ ordre inversé
-- → Marie devient l'email, "Marie" devient le first_name (l'email)
-- → SQL ne détecte pas l'erreur, c'est une catastrophe silencieuse
```

> **Bonne pratique :** **toujours** lister explicitement les colonnes dans `INSERT INTO ... (...)`. Ne jamais utiliser la syntaxe sans colonnes (`INSERT INTO readers VALUES (...)`) — si la table évolue, ton script casse silencieusement.

#### Que se passe-t-il si la colonne `id` n’est pas fournie ?

Pour une colonne `INTEGER PRIMARY KEY`, SQLite (et la plupart des SGBD) génère automatiquement la valeur suivante. Tu n’as pas besoin de la fournir :

```sql
INSERT INTO readers (first_name, last_name, registration_date)
VALUES ('Marie', 'Lefort', '2025-12-01');
-- → id sera attribué automatiquement (16, par exemple)
```

> **📋 FIL ROUGE — Épisode 19**
> 
> Une nouvelle famille s’inscrit à la médiathèque. Trois personnes : les deux parents et l’enfant. Nora ajoute les trois en une seule requête :
> 
> ```sql
> INSERT INTO readers (first_name, last_name, email, city, registration_date)
> VALUES
>     ('Julien', 'Mercier', 'julien.mercier@example.com', 'Saint-Cloud', '2026-05-03'),
>     ('Sandra', 'Mercier', 'sandra.mercier@example.com', 'Saint-Cloud', '2026-05-03'),
>     ('Léo', 'Mercier', NULL, 'Saint-Cloud', '2026-05-03');
> ```
> 
> Les trois nouveaux lecteurs sont enregistrés. Léo (l’enfant) n’a pas d’email — `NULL` est accepté car la colonne le permet.

### ❌ Erreur classique

```sql
-- Insérer du texte sans guillemets
INSERT INTO readers (first_name, last_name, registration_date)
VALUES (Marie, Lefort, 2025-12-01);             -- ❌ erreur ou comportement bizarre
INSERT INTO readers (first_name, last_name, registration_date)
VALUES ('Marie', 'Lefort', '2025-12-01');       -- ✅

-- Violer une contrainte NOT NULL
INSERT INTO readers (first_name, city)
VALUES ('Marie', 'Paris');         -- ❌ last_name est NOT NULL → erreur

-- Violer une contrainte UNIQUE (ex : email déjà utilisé)
INSERT INTO readers (first_name, last_name, email, registration_date)
VALUES ('Bob', 'Smith', 'alice.martin@example.com', '2025-12-01');
-- ❌ erreur si email a une contrainte UNIQUE et que cet email existe déjà
```

> **Note sur notre base de démo :** dans `readers`, la colonne `email` n’est volontairement **pas** déclarée `UNIQUE`. C’est ce qui permet d’avoir deux Alice Martin avec le même email — et d’avoir une vraie réponse à la question “quels emails sont en double ?” (Q9 du Skills Assessment). Dans une vraie application, tu mettrais probablement `UNIQUE` sur l’email pour garantir qu’il identifie un seul lecteur. C’est un choix de modélisation qui dépend du métier.

### ✅ Tu sais maintenant…

- Insérer une ligne : `INSERT INTO table (col1, col2) VALUES (val1, val2);`
- Insérer plusieurs lignes en une requête
- Omettre les colonnes optionnelles (elles prendront `NULL` ou la valeur par défaut)
- Toujours **lister explicitement** les colonnes pour éviter les surprises

-----


## Chapitre 21 — Modifier avec UPDATE

### Le minimum à savoir

#### La structure de base

```sql
UPDATE readers
SET email = 'alice.martin.new@example.com'
WHERE id = 1;
```

Décodage :

- `UPDATE readers` → modifier la table `readers`
- `SET email = ...` → la colonne et sa nouvelle valeur
- `WHERE id = 1` → **uniquement** la ligne où `id = 1`

#### Modifier plusieurs colonnes

```sql
UPDATE readers
SET email = 'new@example.com', city = 'Lyon'
WHERE id = 1;
```

Sépare les colonnes par des virgules dans `SET`.

#### **LA RÈGLE ABSOLUE : toujours faire un `SELECT` avant**

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

#### L’ERREUR FATALE : oublier le `WHERE`

```sql
UPDATE readers
SET city = 'Paris';
-- ❌ ❌ ❌ MET TOUS LES LECTEURS À PARIS
```

Sans `WHERE`, SQL applique l’`UPDATE` à **toutes les lignes** de la table. Pour 15 lecteurs, c’est gênant. Pour 1 million d’utilisateurs, c’est une catastrophe — et la plupart du temps, c’est irréversible (sauf si tu travailles dans une transaction, voir Ch.23).

> **À retenir :** `UPDATE` sans `WHERE` modifie **toute la table**. C’est l’erreur n°1 en SQL. Le mécanisme de protection s’appelle… le `SELECT` préalable et la transaction.

#### Modifier en se basant sur la valeur actuelle

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

### Très utile en pratique

#### Combiner `UPDATE` et calcul

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

### ❌ Erreur classique

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

### 💡 Exercices

1. Modifie l’email du lecteur d’id 3 vers `'lea.dubois.nouveau@example.com'`. Fais d’abord un `SELECT` !
1. Marque comme `'returned'` tous les emprunts dont le `return_date` est renseigné mais qui sont encore en `'late'`.
1. Mets la ville en majuscules pour tous les lecteurs habitant à Paris (utilise `UPPER`).

### ✅ Tu sais maintenant…

- La structure : `UPDATE table SET col = val WHERE condition;`
- **TOUJOURS faire un `SELECT` avec le même `WHERE` avant**
- L’erreur fatale : `UPDATE` sans `WHERE` modifie toute la table
- Modifier plusieurs colonnes en une requête
- Référencer la valeur existante dans `SET` (`SET col = col + 1`)

-----


## Chapitre 22 — Supprimer avec DELETE

### Le minimum à savoir

#### La structure de base

```sql
DELETE FROM readers
WHERE id = 1;
```

Aussi simple que dangereux. Une seule ligne, mais qui supprime définitivement.

#### **LA MÊME RÈGLE ABSOLUE : `SELECT` avant `DELETE`**

> **⚠️ Avant tout `DELETE`, fais TOUJOURS un `SELECT` avec le même `WHERE`** pour vérifier ce que tu vas supprimer.

```sql
-- 1. Vérifier
SELECT * FROM readers WHERE id = 1;

-- 2. Si c'est bien la ligne attendue, supprimer
DELETE FROM readers WHERE id = 1;
```

#### L’ERREUR FATALE : oublier le `WHERE`

```sql
DELETE FROM readers;
-- ❌ ❌ ❌ SUPPRIME TOUS LES LECTEURS
```

Sans `WHERE`, **toutes les lignes** de la table sont supprimées. Le contenu est perdu, la table reste (vide). Avec une transaction (Ch.23), on peut annuler. Sans transaction, c’est définitif.

#### `DELETE` ne supprime pas la table

`DELETE` supprime des **lignes**, pas la table elle-même. Pour supprimer la table : `DROP TABLE` (à manier avec extrême précaution, voir Ch.24).

|Commande                          |Effet                                                |
|----------------------------------|-----------------------------------------------------|
|`DELETE FROM readers WHERE id = 1`|Supprime une ligne                                   |
|`DELETE FROM readers`             |Supprime **toutes** les lignes (la table reste, vide)|
|`DROP TABLE readers`              |Supprime la table elle-même                          |

#### Le piège : les contraintes de clé étrangère

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

### Très utile en pratique

#### Le `DELETE` conditionnel

```sql
-- Supprimer les comptes de personnel inactifs depuis plus de 2 ans
DELETE FROM staff_users
WHERE is_active = 0
  AND created_at < DATE('now', '-2 years');
```

Cette requête combine `WHERE` et calcul de date — typique d’une opération de nettoyage.

### ❌ Erreur classique

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

### 💡 Exercices

1. Supprime les emprunts retournés depuis plus de 30 jours (utilise `julianday`).
1. Supprime les comptes `staff_users` inactifs (`is_active = 0`).
1. Vérifie : combien de lignes contient maintenant chaque table ?

### ✅ Tu sais maintenant…

- La structure : `DELETE FROM table WHERE condition;`
- **TOUJOURS faire un `SELECT` avant** (la règle d’or se répète)
- L’erreur fatale : `DELETE` sans `WHERE` vide la table
- Les contraintes `FOREIGN KEY` peuvent bloquer une suppression
- L’alternative “soft delete” (marquer comme inactif au lieu de supprimer)

-----


## Chapitre 23 — Transactions : BEGIN, COMMIT, ROLLBACK

### Le minimum à savoir

#### Le problème : et si je me trompe ?

Tu lances un `UPDATE`, tu te rends compte 2 secondes après que tu as oublié le `WHERE`. Tu as modifié toute la table. Que faire ?

Sans transaction : **rien**. Les modifications sont permanentes.

Avec transaction : tu peux **annuler**.

#### Le concept

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

#### Les 3 mots-clés

|Mot-clé                           |Effet                                                    |
|----------------------------------|---------------------------------------------------------|
|`BEGIN;` (ou `BEGIN TRANSACTION;`)|Ouvre une transaction                                    |
|`COMMIT;`                         |Valide tout — les modifications deviennent permanentes   |
|`ROLLBACK;`                       |Annule tout — la base revient à l’état d’avant le `BEGIN`|

#### Le scénario typique

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

#### ACID en aperçu

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

### Très utile en pratique

#### Quand utiliser une transaction ?

|Opération                                                            |Transaction recommandée ?|
|---------------------------------------------------------------------|-------------------------|
|`SELECT` simple                                                      |Non                      |
|`INSERT` ponctuel                                                    |Optionnel                |
|`UPDATE` ou `DELETE` sur plusieurs lignes                            |**Oui**                  |
|Plusieurs modifications liées (ex : transfert d’un compte à un autre)|**Oui, obligatoire**     |
|Migration de données, refonte de la base                             |**Oui, obligatoire**     |

#### Le cas d’école : le transfert bancaire

```sql
BEGIN;
UPDATE comptes SET solde = solde - 100 WHERE id = 1;     -- débite Alice
UPDATE comptes SET solde = solde + 100 WHERE id = 2;     -- crédite Bob
COMMIT;
```

Si la deuxième requête échoue (panne, erreur), un `ROLLBACK` annule la première. **Sans transaction**, Alice perdrait 100€ et Bob ne les recevrait pas — l’argent disparaîtrait.

C’est pour ça que toutes les applications financières utilisent des transactions.

### ❌ Erreur classique

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

### 💡 Exercices

1. Ouvre une transaction. Insère un nouveau lecteur. Vérifie avec un `SELECT`. Annule avec `ROLLBACK`. Vérifie qu’il n’est plus là.
1. Refais la même chose, mais cette fois `COMMIT`. Vérifie qu’il est bien là après.
1. Ouvre une transaction, supprime tous les emprunts retournés (`DELETE FROM loans WHERE status = 'returned'`), regarde le nombre de lignes restantes, puis `ROLLBACK`. Vérifie que la base est revenue à l’état initial.

### ✅ Tu sais maintenant…

- Une transaction est un bloc `BEGIN ... COMMIT;` (ou `ROLLBACK;`)
- `BEGIN` ouvre, `COMMIT` valide définitivement, `ROLLBACK` annule
- Les transactions sont ton filet de sécurité pour les opérations risquées
- Les propriétés **ACID** : Atomicité, Cohérence, Isolation, Durabilité
- Toutes les applications critiques utilisent des transactions

-----
