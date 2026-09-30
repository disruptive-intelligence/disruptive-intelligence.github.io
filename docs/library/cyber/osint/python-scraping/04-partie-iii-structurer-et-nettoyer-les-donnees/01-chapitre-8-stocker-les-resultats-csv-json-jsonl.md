---
title: Chapitre 8 — Stocker les résultats (CSV, JSON, JSONL)
source: Cyber/02_OSINT/Python_Scraping.md
note: Python & scraping
up:
- - Python & scraping
  - ../index.md
- - Partie III — Structurer et nettoyer les données
  - index.md
---

Tu as construit une liste de dicts en Partie II. Elle vit en mémoire et disparaît à la fin du script. Il est temps de la **persister** correctement.

## Le minimum à savoir

### La règle d’or : `raw` est intouchable

Rappel du chapitre 0 :

```
data/
├── raw/        ← HTML brut horodaté, JAMAIS modifié
└── processed/  ← données extraites, nettoyées, exploitables
```


`data/raw/` contient **les preuves**. Tu n’y touches jamais. Si tu casses ton parsing, tu peux toujours rejouer depuis `raw/` sans relancer la moindre requête.

Tous les formats de sortie de ce chapitre (CSV, JSON, JSONL) vivent dans `data/processed/`.

### Choisir entre CSV, JSON et JSONL

|Format                |Cas idéal                                                                       |Avantages                                                                                 |Limites                                                    |
|----------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------|
|**CSV**               |Données tabulaires, mêmes champs partout (citations, livres, lignes de tableau).|Ouvert dans n’importe quel tableur. Léger. Universel.                                     |Ne supporte pas les structures imbriquées (listes, objets).|
|**JSON**              |Données hétérogènes ou imbriquées (un objet riche par enquête).                 |Fidèle aux structures Python. Lisible humainement.                                        |Doit être chargé en entier ; pas pratique pour l’append.   |
|**JSONL** (JSON Lines)|Collectes longues, append-friendly, streaming.                                  |Une ligne = un objet. Lecture/écriture incrémentale. Excellent pour les grosses collectes.|Pas un standard universel pour les tableurs.               |


> **Règle pratique :**
> 
> - Quelques centaines d’items homogènes destinés à un tableur → **CSV**.
> - Données structurées avec listes ou imbrications → **JSON**.
> - Collecte par flux, append au fil de l’eau, gros volumes → **JSONL**.

### Écrire en CSV avec `csv.DictWriter`

```python
import csv
from pathlib import Path

resultats = [
    {"texte": "...", "auteur": "Einstein", "source_url": "...", "collected_at": "..."},
    {"texte": "...", "auteur": "Wilde",    "source_url": "...", "collected_at": "..."},
]

chemin = Path("data/processed/quotes.csv")
chemin.parent.mkdir(parents=True, exist_ok=True)

# Champs explicites : tu décides de l’ordre des colonnes
champs = ["texte", "auteur", "source_url", "collected_at"]

with chemin.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=champs)
    writer.writeheader()
    writer.writerows(resultats)

print(f"{len(resultats)} lignes écrites dans {chemin}")
```


Trois points cruciaux :

- **`encoding="utf-8"`** : pour les accents et caractères non-ASCII.
- **`newline=""`** : sur Windows, sans ça, tu obtiens des doubles sauts de ligne.
- **`fieldnames`** : tu maîtrises l’ordre des colonnes. Indispensable pour des fichiers comparables d’une exécution à l’autre.

### Quand un champ est une liste (cas des tags)

CSV n’aime pas les listes. Deux options :

```python
# Option 1 : joindre avec un séparateur
enregistrement["tags"] = "|".join(enregistrement["tags"])

# Option 2 : exporter en JSON plutôt
```


Le séparateur `|` est plus sûr que `,` ou `;` (rares dans les tags). Au moment de relire :

```python
tags = ligne["tags"].split("|") if ligne["tags"] else []
```


### Écrire en JSON

```python
import json
from pathlib import Path

chemin = Path("data/processed/quotes.json")
chemin.parent.mkdir(parents=True, exist_ok=True)

with chemin.open("w", encoding="utf-8") as f:
    json.dump(resultats, f, indent=2, ensure_ascii=False)

print(f"{len(resultats)} enregistrements écrits dans {chemin}")
```


Deux arguments qui changent tout :

- **`indent=2`** : indentation lisible. Sans ça, tout est sur une ligne.
- **`ensure_ascii=False`** : conserve les caractères Unicode (`é`, `中`, `→`) au lieu de les échapper en `\u00e9`. Plus lisible et plus léger.

### Écrire en JSONL (un objet par ligne)

```python
import json
from pathlib import Path

chemin = Path("data/processed/quotes.jsonl")
chemin.parent.mkdir(parents=True, exist_ok=True)

with chemin.open("w", encoding="utf-8") as f:
    for item in resultats:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
```


Pour relire :

```python
with chemin.open("r", encoding="utf-8") as f:
    for ligne in f:
        item = json.loads(ligne)
        # traiter item
```


JSONL brille pour les **collectes incrémentales** : tu peux ouvrir le fichier en mode `"a"` (append) et ajouter des enregistrements au fil de l’eau, sans tout recharger en mémoire.

### Convention de nommage des fichiers

Un nom de fichier propre est un nom **traçable** :

```
<run_id>_<source>_<sujet>.<format>

Exemples :
20260517T140000Z_quotes_toscrape_collection.csv
20260517T143012Z_books_toscrape_inventory.json
20260517T150000Z_legifrance_decret_2026-401.json
```


Composantes :

- **`run_id`** (horodatage UTC ISO compact) : identifie une exécution unique.
- **`source`** : nom court de la cible.
- **`sujet`** : ce qu’on a collecté.

> **À retenir :** ton `run_id` est partagé entre le HTML brut (`data/raw/`), les données traitées (`data/processed/`), le log (`logs/`) et le rapport (`reports/`). C’est ce qui permet de **tout retrouver** d’une exécution donnée en une recherche.

### Les métadonnées au niveau du dataset

Au-delà des métadonnées **par enregistrement** (`source_url`, `collected_at`, `tool`), un dataset complet doit aussi porter ses propres métadonnées **globales**. Format recommandé en JSON :

```python
sortie = {
    "metadata": {
        "tool": "mon-collecteur",
        "tool_version": "0.1.0",
        "run_id": "20260517T140000Z",
        "collected_at": "2026-05-17T14:00:00Z",
        "source_url": "https://quotes.toscrape.com/",
        "count": len(resultats),
    },
    "data": resultats,
}

with chemin.open("w", encoding="utf-8") as f:
    json.dump(sortie, f, indent=2, ensure_ascii=False)
```


C’est ce qu’un analyste qui reçoit ton fichier veut voir en premier : « ça vient d’où, c’est de quand, combien il y en a ».

## Très utile en pratique

### Déduplication par clé naturelle

À chaque collecte, tu risques d’avoir des doublons (même citation sur deux pages, même article dans deux flux). On déduplique avec une **clé naturelle** stable :

```python
def dedupliquer(items, cle):
    """Garde le premier exemplaire de chaque clé."""
    vus = set()
    uniques = []
    for item in items:
        valeur = item.get(cle)
        if valeur and valeur not in vus:
            vus.add(valeur)
            uniques.append(item)
    return uniques


# Exemple : dédupliquer des articles par URL
articles_uniques = dedupliquer(articles, "source_url")
print(f"{len(articles)} → {len(articles_uniques)} après déduplication")
```


> **Choix de la clé** : utilise quelque chose de **stable** et **unique**. `source_url` canonisée est souvent le meilleur choix **quand chaque item correspond à une page distincte** (un article = une URL). Si plusieurs items viennent d’une même page (citations, livres, lignes de tableau), utilise plutôt un `item_id` construit par hash sur les champs métier (voir juste après).

### Hash d’un enregistrement pour déduplication fine

Quand aucun champ unique n’existe :

```python
import hashlib
import json

def hash_enregistrement(item, champs):
    """Hash SHA-256 de la concaténation de certains champs."""
    base = json.dumps([item.get(c, "") for c in champs], ensure_ascii=False)
    return hashlib.sha256(base.encode("utf-8")).hexdigest()


# Exemple :
for item in resultats:
    item["item_id"] = hash_enregistrement(item, ["texte", "auteur"])
```


Le `item_id` est désormais stable : si tu re-collectes la même citation demain, elle aura le même hash. Idéal pour la détection de doublons et la comparaison entre collectes (chapitre 13).

### Organisation des dossiers : récap

```
data/
├── raw/
│   ├── 20260517T140000Z_quotes_toscrape.html
│   ├── 20260517T143012Z_books_toscrape.html
│   └── ...
├── processed/
│   ├── 20260517T140000Z_quotes_toscrape_collection.json
│   └── ...
└── reports/  (vient au chapitre 14)
```


Une exécution = un `run_id` = un fichier par étape, tous reliés.

### Lire un CSV existant

```python
import csv
from pathlib import Path

with Path("data/processed/quotes.csv").open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    enregistrements = list(reader)

print(f"{len(enregistrements)} lignes lues")
```


`DictReader` te donne directement des dicts avec les en-têtes comme clés. C’est presque toujours ce que tu veux.

## Bonus

### SQLite en mention

Quand JSON/CSV deviennent insuffisants (gros volumes, requêtes croisées, jointures), Python intègre **SQLite** sans installation supplémentaire :

```python
import sqlite3

con = sqlite3.connect("data/processed/collecte.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS quotes (texte TEXT, auteur TEXT, url TEXT)")
cur.executemany("INSERT INTO quotes VALUES (?, ?, ?)",
                [(q["texte"], q["auteur"], q["source_url"]) for q in resultats])
con.commit()
con.close()
```


C’est hors-scope pour ce cours, mais à connaître pour quand tes datasets grandissent.

### Une fonction d’écriture qui choisit le bon format

```python
import csv
import json
from pathlib import Path

def write(items, chemin, format="auto"):
    """Écrit items dans chemin. Format auto-détecté par extension."""
    chemin = Path(chemin)
    chemin.parent.mkdir(parents=True, exist_ok=True)

    if format == "auto":
        format = chemin.suffix.lstrip(".").lower()

    if format == "csv":
        champs = list(items[0].keys()) if items else []
        with chemin.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=champs)
            writer.writeheader()
            writer.writerows(items)
    elif format == "json":
        with chemin.open("w", encoding="utf-8") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
    elif format == "jsonl":
        with chemin.open("w", encoding="utf-8") as f:
            for item in items:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
    else:
        raise ValueError(f"Format inconnu : {format}")
```


À glisser dans `src/store.py` de ton projet.

## ❌ Erreur classique

```python
# Oublier encoding="utf-8" sur Windows
with open("sortie.csv", "w") as f:
    csv.writer(f).writerows(...)
# ❌ Caractères accentués cassés, BOM parasites
# ✅ Toujours encoding="utf-8" en lecture et écriture

# Oublier newline="" pour CSV
with open("sortie.csv", "w", encoding="utf-8") as f:
    ...
# ❌ Sur Windows : double saut de ligne entre chaque ligne
# ✅ newline="" obligatoire pour CSV

# Écraser une collecte précédente
with open("data/processed/quotes.json", "w") as f:
    json.dump(...)
# ❌ La collecte d’hier est perdue.
# ✅ Toujours préfixer avec un run_id horodaté.

# Stocker une liste Python dans une cellule CSV
ligne = {"tags": ["a", "b", "c"]}
csv.DictWriter(...).writerow(ligne)
# ❌ Tu obtiens "['a', 'b', 'c']" littéralement — pas exploitable
# ✅ Joindre avec un séparateur : "|".join(tags)
# ✅ Ou stocker en JSON plutôt qu’en CSV

# Polluer le dossier courant
json.dump(items, open("sortie.json", "w"))
# ❌ Le fichier atterrit n’importe où, écrase peut-être autre chose
# ✅ Toujours dans data/processed/, avec mkdir(parents=True, exist_ok=True)
```


## Exercices

**Guidé :** Reprends le mini-projet « collecteur de citations » du chapitre 7 et ajoute :

1. Une fonction `write_csv(items, chemin)` qui écrit les citations dans `data/processed/<run_id>_quotes.csv`. Sérialise les tags avec `|`.
1. Une fonction `write_json(items, chemin, source_url)` qui écrit un fichier `data/processed/<run_id>_quotes.json` au format `{metadata: {...}, data: [...]}`.
1. Une exécution qui produit les deux fichiers en parallèle.

**Autonome :** Écris un script `src/append_jsonl.py` qui :

1. Prend un fichier JSONL en argument (créé s’il n’existe pas).
1. Demande à l’utilisateur de saisir une note (`titre`, `contenu`) en boucle.
1. Ajoute chaque note au JSONL en mode append, avec `id` (hash) et `created_at` (UTC ISO).
1. S’arrête sur saisie vide.

À la fin, ouvre le fichier et vérifie que chaque ligne est un JSON valide indépendant.

## ✅ Tu sais maintenant…

- Choisir entre CSV, JSON et JSONL selon le cas
- Écrire en CSV (avec `encoding`, `newline`, `fieldnames` explicites)
- Écrire en JSON (`indent`, `ensure_ascii=False`)
- Écrire en JSONL pour les collectes append-friendly
- Ajouter des métadonnées globales `{metadata: {...}, data: [...]}`
- Dédupliquer par clé naturelle ou par hash
- Nommer tes fichiers avec un `run_id` partagé entre raw / processed / logs / reports
- Organiser proprement `data/raw/` et `data/processed/`

-----
