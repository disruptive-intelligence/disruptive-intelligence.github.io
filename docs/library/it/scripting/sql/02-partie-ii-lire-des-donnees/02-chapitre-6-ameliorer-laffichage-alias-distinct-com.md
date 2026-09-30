---
title: 'Chapitre 6 — Améliorer l’affichage : alias, DISTINCT, commentaires'
source: IT/Culture/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie II — Lire des données
  - index.md
---

## Le minimum à savoir

### Renommer une colonne avec `AS` (alias)

Tu peux donner un nom temporaire à une colonne dans le résultat :

```sql
SELECT first_name AS prenom, last_name AS nom, email AS courriel
FROM readers;
```


Le résultat affiche les colonnes sous les noms `prenom`, `nom`, `courriel`, sans modifier la table elle-même.

> **À retenir :** un alias ne change rien dans la base — il modifie seulement l’**affichage**. C’est utile pour rendre les résultats plus lisibles, ou pour franciser un export.

Le `AS` est même optionnel — ces deux requêtes sont équivalentes :

```sql
SELECT first_name AS prenom FROM readers;
SELECT first_name prenom FROM readers;       -- même chose, mais moins lisible
```


> **Bonne pratique :** garde le `AS` pour la clarté. Tu le verras partout.

### Éliminer les doublons avec `DISTINCT`

Sans `DISTINCT`, SQL te montre toutes les lignes — y compris les valeurs répétées :

```sql
SELECT city FROM readers;
-- Paris, Lyon, Paris, Marseille, Paris, Lyon, ... (avec doublons)
```


Avec `DISTINCT`, tu n’obtiens que les valeurs **uniques** :

```sql
SELECT DISTINCT city FROM readers;
-- Paris, Lyon, Marseille, Bordeaux, Toulouse (sans doublons)
```


C’est l’équivalent de “supprimer les doublons” dans Excel.

### Commentaires SQL

Comme dans les autres langages, tu peux annoter ton code :

```sql
-- Ceci est un commentaire sur une ligne (deux tirets)

/* Ceci est un commentaire
   sur plusieurs lignes
   (style C) */

SELECT first_name, last_name   -- commentaire en fin de ligne
FROM readers;
```


> **Bonne pratique :** commente tes requêtes complexes. Tu te remercieras dans 6 mois quand tu reliras.

> **📋 FIL ROUGE — Épisode 5**
> 
> La directrice demande à Nora : “Dans quelles villes nos lecteurs habitent-ils ?”. Nora utilise `DISTINCT` :
> 
> ```sql
> SELECT DISTINCT city FROM readers;
> ```
> 
> Résultat : Paris, Lyon, Marseille, Bordeaux, Toulouse. 5 villes. Elle peut maintenant proposer de cibler des animations dans chacune.

## Très utile en pratique

### `DISTINCT` sur plusieurs colonnes

`DISTINCT` s’applique à **la combinaison** de toutes les colonnes sélectionnées :

```sql
SELECT DISTINCT first_name, city FROM readers;
-- Élimine les couples (prénom, ville) en double
```


Donc deux Alice dans deux villes différentes apparaîtront **deux fois** — c’est le couple qui doit être unique.

## ❌ Erreur classique

```sql
-- Mettre AS au mauvais endroit
SELECT AS prenom first_name FROM readers;     -- ❌ AS vient APRÈS la colonne
SELECT first_name AS prenom FROM readers;      -- ✅

-- DISTINCT mal placé
SELECT first_name, DISTINCT city FROM readers; -- ❌ DISTINCT s'applique à toute la sélection
SELECT DISTINCT city FROM readers;             -- ✅
```


## ✅ Tu sais maintenant…

- Renommer une colonne dans le résultat avec `AS`
- Éliminer les doublons avec `DISTINCT`
- Commenter avec `--` ou `/* ... */`

-----
