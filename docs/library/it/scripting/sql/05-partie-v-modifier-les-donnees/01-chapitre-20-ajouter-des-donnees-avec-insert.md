---
title: Chapitre 20 — Ajouter des données avec INSERT
source: IT/07 Scripting & programmation/SQL.md
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
INSERT INTO readers (first_name, last_name, email, city, registration_date)
VALUES ('Marie', 'Lefort', 'marie.lefort@example.com', 'Paris', '2025-12-01');
```


Décodage :

- `INSERT INTO readers` → “ajouter dans la table `readers`”
- `(first_name, last_name, email, city, registration_date)` → les colonnes que tu remplis
- `VALUES (...)` → les valeurs, **dans le même ordre** que les colonnes

### Insérer plusieurs lignes en une fois

```sql
INSERT INTO readers (first_name, last_name, email, city, registration_date)
VALUES
    ('Marie', 'Lefort', 'marie@example.com', 'Paris', '2025-12-01'),
    ('Paul', 'Dupuis', 'paul@example.com', 'Lyon', '2025-12-02'),
    ('Anne', 'Roy', NULL, 'Bordeaux', '2025-12-03');
```


Une seule requête, trois lignes ajoutées.

### Omettre des colonnes : valeurs par défaut

Tu peux omettre certaines colonnes — elles prendront leur valeur par défaut (souvent `NULL`, ou ce qui est défini dans `CREATE TABLE`).

```sql
-- email et phone ne sont pas listés → ils prendront NULL
INSERT INTO readers (first_name, last_name, city, registration_date)
VALUES ('Sophia', 'Lambert', 'Paris', '2025-12-04');
```


> **À retenir :** une colonne marquée `NOT NULL` (sans valeur par défaut) doit obligatoirement recevoir une valeur — sinon erreur.

### L’ordre des valeurs doit correspondre à l’ordre des colonnes

```sql
INSERT INTO readers (first_name, last_name, email)
VALUES ('Marie', 'Lefort', 'marie@example.com');     -- ✅ correspondance

INSERT INTO readers (first_name, last_name, email)
VALUES ('marie@example.com', 'Marie', 'Lefort');     -- ❌ ordre inversé
-- → Marie devient l'email, "Marie" devient le first_name (l'email)
-- → SQL ne détecte pas l'erreur, c'est une catastrophe silencieuse
```


> **Bonne pratique :** **toujours** lister explicitement les colonnes dans `INSERT INTO ... (...)`. Ne jamais utiliser la syntaxe sans colonnes (`INSERT INTO readers VALUES (...)`) — si la table évolue, ton script casse silencieusement.

### Que se passe-t-il si la colonne `id` n’est pas fournie ?

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

## ❌ Erreur classique

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

## ✅ Tu sais maintenant…

- Insérer une ligne : `INSERT INTO table (col1, col2) VALUES (val1, val2);`
- Insérer plusieurs lignes en une requête
- Omettre les colonnes optionnelles (elles prendront `NULL` ou la valeur par défaut)
- Toujours **lister explicitement** les colonnes pour éviter les surprises

-----
