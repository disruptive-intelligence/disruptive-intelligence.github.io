---
title: Chapitre 14 — Filtrer les groupes avec HAVING
source: IT/07 Scripting & programmation/Langages/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie III — Calculer et regrouper
  - index.md
---

## Le minimum à savoir

### Le problème : filtrer après agrégation

`WHERE` filtre les **lignes** avant le regroupement. Mais que faire si tu veux filtrer les **groupes** après calcul ?

Exemple : “Quels lecteurs ont emprunté 3 livres ou plus ?”

Tu ne peux pas écrire `WHERE COUNT(*) >= 3` — `COUNT(*)` n’existe qu’après agrégation. Il faut une autre clause : `HAVING`.

### `WHERE` vs `HAVING`

```sql
-- ❌ Ne marche pas : COUNT(*) n'est pas connu au moment du WHERE
SELECT reader_id, COUNT(*)
FROM loans
WHERE COUNT(*) >= 3
GROUP BY reader_id;

-- ✅ Correct : HAVING filtre les groupes après agrégation
SELECT reader_id, COUNT(*) AS nb_emprunts
FROM loans
GROUP BY reader_id
HAVING COUNT(*) >= 3;
```


> **À retenir :** `WHERE` filtre les **lignes** (avant `GROUP BY`). `HAVING` filtre les **groupes** (après `GROUP BY`). Tu peux utiliser les deux dans la même requête — ils ne servent pas à la même chose.

### L’exemple combiné

```sql
-- Lecteurs ayant eu plus de 2 emprunts en retard
SELECT reader_id, COUNT(*) AS nb_retards
FROM loans
WHERE status = 'late'                  -- ← filtre les lignes "en retard"
GROUP BY reader_id
HAVING COUNT(*) >= 2;                  -- ← garde les lecteurs avec ≥ 2 retards
```


L’ordre logique :

1. `WHERE status = 'late'` → on ne garde que les emprunts en retard
1. `GROUP BY reader_id` → on regroupe par lecteur
1. `HAVING COUNT(*) >= 2` → on garde les groupes ayant au moins 2 retards

> **📋 FIL ROUGE — Épisode 13**
> 
> La directrice : “Identifie les lecteurs qui ont plus d’un retard. On va leur envoyer un rappel.” Nora :
> 
> ```sql
> SELECT reader_id, COUNT(*) AS nb_retards
> FROM loans
> WHERE status = 'late'
> GROUP BY reader_id
> HAVING COUNT(*) >= 2;
> ```
> 
> Elle identifie les “récidivistes”. Sans `HAVING`, elle aurait obtenu tous les lecteurs avec leur nombre de retards (y compris ceux qui en ont 1) — `HAVING` lui permet de cibler spécifiquement les problématiques.

## Très utile en pratique

### Le tableau récapitulatif

|Clause  |Filtre quoi ?       |Quand ?         |Peut utiliser des agrégations ?|
|--------|--------------------|----------------|-------------------------------|
|`WHERE` |Lignes individuelles|Avant `GROUP BY`|❌ Non                          |
|`HAVING`|Groupes             |Après `GROUP BY`|✅ Oui                          |

### Sans `GROUP BY` ?

`HAVING` peut techniquement s’utiliser sans `GROUP BY` (la table est alors traitée comme un seul groupe), mais c’est rare. Le cas standard est `GROUP BY ... HAVING ...`.

## ❌ Erreur classique

```sql
-- Mettre une condition d'agrégation dans WHERE
SELECT reader_id, COUNT(*)
FROM loans
WHERE COUNT(*) >= 3      -- ❌ COUNT(*) n'existe pas à ce stade
GROUP BY reader_id;

-- ✅ Correct
SELECT reader_id, COUNT(*)
FROM loans
GROUP BY reader_id
HAVING COUNT(*) >= 3;

-- Mettre une condition simple dans HAVING (techniquement possible mais inefficace)
SELECT reader_id, COUNT(*)
FROM loans
GROUP BY reader_id
HAVING reader_id = 1;     -- ⚠️ ça marche, mais c'est plus efficace dans WHERE

-- ✅ Plus efficace
SELECT reader_id, COUNT(*)
FROM loans
WHERE reader_id = 1
GROUP BY reader_id;
```


## 💡 Exercices

1. Quelles villes ont au moins 3 lecteurs ?
1. Quels livres ont été empruntés au moins 2 fois ?
1. Quels lecteurs ont au moins 2 emprunts encore en cours (`status = 'borrowed'`) ?

## ✅ Tu sais maintenant…

- `WHERE` filtre les lignes (avant `GROUP BY`)
- `HAVING` filtre les groupes (après `GROUP BY`)
- `HAVING` peut utiliser des fonctions d’agrégation, `WHERE` non
- Combiner les deux dans une même requête est non seulement possible mais recommandé pour les conditions appropriées

-----
