---
title: PARTIE III — STRUCTURER ET NETTOYER LES DONNÉES
source: Cyber/02_OSINT/Python_Scraping.md
note: Python & scraping
chapter: 4
chapters: 7
---

> **Objectif de la partie :** transformer une collecte brute en un dataset propre, dédupliqué, daté, prêt à être analysé ou versionné. Tu vas apprendre à stocker tes résultats dans les bons formats, à organiser ton dossier de sortie, à nettoyer le texte et à dédupliquer.
> 
> À la fin de cette partie, tu auras un pipeline `raw → processed → exploitable`.

-----


## Chapitre 8 — Stocker les résultats (CSV, JSON, JSONL)

Tu as construit une liste de dicts en Partie II. Elle vit en mémoire et disparaît à la fin du script. Il est temps de la **persister** correctement.

### Le minimum à savoir

#### La règle d’or : `raw` est intouchable

Rappel du chapitre 0 :

```
data/
├── raw/        ← HTML brut horodaté, JAMAIS modifié
└── processed/  ← données extraites, nettoyées, exploitables
```

`data/raw/` contient **les preuves**. Tu n’y touches jamais. Si tu casses ton parsing, tu peux toujours rejouer depuis `raw/` sans relancer la moindre requête.

Tous les formats de sortie de ce chapitre (CSV, JSON, JSONL) vivent dans `data/processed/`.

#### Choisir entre CSV, JSON et JSONL

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

#### Écrire en CSV avec `csv.DictWriter`

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

#### Quand un champ est une liste (cas des tags)

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

#### Écrire en JSON

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

#### Écrire en JSONL (un objet par ligne)

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

#### Convention de nommage des fichiers

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

#### Les métadonnées au niveau du dataset

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

### Très utile en pratique

#### Déduplication par clé naturelle

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

#### Hash d’un enregistrement pour déduplication fine

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

#### Organisation des dossiers : récap

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

#### Lire un CSV existant

```python
import csv
from pathlib import Path

with Path("data/processed/quotes.csv").open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    enregistrements = list(reader)

print(f"{len(enregistrements)} lignes lues")
```

`DictReader` te donne directement des dicts avec les en-têtes comme clés. C’est presque toujours ce que tu veux.

### Bonus

#### SQLite en mention

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

#### Une fonction d’écriture qui choisit le bon format

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

### ❌ Erreur classique

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

### Exercices

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

### ✅ Tu sais maintenant…

- Choisir entre CSV, JSON et JSONL selon le cas
- Écrire en CSV (avec `encoding`, `newline`, `fieldnames` explicites)
- Écrire en JSON (`indent`, `ensure_ascii=False`)
- Écrire en JSONL pour les collectes append-friendly
- Ajouter des métadonnées globales `{metadata: {...}, data: [...]}`
- Dédupliquer par clé naturelle ou par hash
- Nommer tes fichiers avec un `run_id` partagé entre raw / processed / logs / reports
- Organiser proprement `data/raw/` et `data/processed/`

-----


## Chapitre 9 — Nettoyer, normaliser, enrichir

Tu as collecté, tu as stocké. Maintenant tu vas transformer ces données brutes en dataset **propre et exploitable**. Un dataset propre, c’est celui qu’on peut trier, filtrer, comparer dans le temps, et croiser avec d’autres sources sans surprise.

### Le minimum à savoir

#### Le pipeline `raw → processed`

Le principe :

```
data/raw/        →    src/clean.py    →    data/processed/
(intouchable)         (transformation)     (exploitable)
```

`clean.py` lit un fichier brut, applique des transformations, et écrit un nouveau fichier. À aucun moment on ne modifie le brut. Si la transformation se trompe, on relance `clean.py` ; pas besoin de retoucher au serveur.

#### Nettoyer le texte

On reprend le helper du chapitre 6, en le complétant :

```python
import re
import unicodedata

def clean_text(text):
    """Nettoie un texte extrait du web."""
    if text is None:
        return ""
    # Normalisation Unicode (caractères composés -> forme stable)
    text = unicodedata.normalize("NFKC", text)
    # Espaces insécables et autres → espace normal
    text = text.replace("\xa0", " ").replace("\u200b", "")
    # Compacte les espaces multiples et trim
    text = re.sub(r"\s+", " ", text).strip()
    return text
```

|Opération      |Pourquoi                                                                                                                           |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------|
|`NFKC`         |Convertit les variantes Unicode (`é` en deux caractères vs un seul) en forme canonique. Indispensable pour comparer et dédupliquer.|
|`\xa0` → espace|L’espace insécable s’affiche comme un espace mais ne match pas `" "` — source de bugs invisibles.                                  |
|`\u200b`       |Zero-Width Space, parfois inséré par des CMS et invisible à l’œil nu.                                                              |
|`\s+` → `" "`  |Compacte tabulations, retours à la ligne, espaces multiples.                                                                       |

À appliquer à **tout** champ texte qui vient du web.

#### Normaliser les URLs

Une URL peut s’écrire de plusieurs façons qui pointent vers la même ressource. Pour dédupliquer correctement, il faut la **canoniser**.

```python
from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode, urljoin

TRACKING_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "fbclid", "gclid", "mc_cid", "mc_eid", "ref", "ref_src", "_ga",
}

def canonical_url(url):
    """Renvoie une version canonique d’une URL (sans tracking, normalisée)."""
    p = urlparse(url)

    # Schéma et hôte en minuscules
    scheme = p.scheme.lower()
    host = p.netloc.lower()

    # Retirer le port par défaut
    if (scheme == "http" and host.endswith(":80")) or \
       (scheme == "https" and host.endswith(":443")):
        host = host.rsplit(":", 1)[0]

    # Path : enlever le slash final sauf pour la racine
    path = p.path or "/"
    if len(path) > 1 and path.endswith("/"):
        path = path.rstrip("/")

    # Query : retirer les paramètres de tracking, trier le reste
    params = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True)
              if k.lower() not in TRACKING_PARAMS]
    params.sort()
    query = urlencode(params)

    # Pas de fragment (#) — il n’a pas de sens côté serveur
    return urlunparse((scheme, host, path, "", query, ""))
```

Exemple :

```python
print(canonical_url("https://Exemple.fr/Article/?utm_source=newsletter&id=42"))
# → https://exemple.fr/Article?id=42

print(canonical_url("https://exemple.fr/article"))
print(canonical_url("https://exemple.fr/article/"))
# → https://exemple.fr/article  (les deux)
```

Maintenant, deux URLs « équivalentes » se ressemblent vraiment. La déduplication devient fiable.

#### Construire une URL absolue à partir d’une relative

Rappel chapitre 7 : `urljoin` reconstruit l’URL complète à partir de l’URL de la page et d’une URL relative trouvée dans un `href`.

```python
from urllib.parse import urljoin

page = "https://exemple.fr/section/index.html"

print(urljoin(page, "article-1.html"))   # https://exemple.fr/section/article-1.html
print(urljoin(page, "/contact"))          # https://exemple.fr/contact
print(urljoin(page, "https://autre.fr")) # https://autre.fr  (URL déjà absolue conservée)
```

#### Extraire le domaine

Pour comparer ou regrouper par site :

```python
from urllib.parse import urlparse

def domain_of(url):
    return urlparse(url).netloc.lower()

print(domain_of("https://www.exemple.fr/article"))
# → www.exemple.fr
```

Mais attention : `www.exemple.fr` et `exemple.fr` sont techniquement deux hôtes différents. Pour traiter `news.bbc.co.uk` correctement (extraire `bbc.co.uk` comme domaine racine), il faut `tldextract` :

```bash
pip install tldextract
```

```python
import tldextract

t = tldextract.extract("https://news.bbc.co.uk/article")
print(t.domain)         # bbc
print(t.suffix)         # co.uk
print(t.registered_domain)  # bbc.co.uk
```

`tldextract` connaît la liste à jour des suffixes publics et fait le travail proprement. À ajouter à `requirements.txt` quand tu travailles avec des URLs variées.

#### Trier et filtrer une liste de dicts

```python
articles = [
    {"titre": "C", "date": "2026-05-15"},
    {"titre": "A", "date": "2026-05-12"},
    {"titre": "B", "date": "2026-05-14"},
]

# Trier par date
articles.sort(key=lambda a: a["date"])

# Trier par date décroissante
articles.sort(key=lambda a: a["date"], reverse=True)

# Filtrer
recents = [a for a in articles if a["date"] >= "2026-05-13"]
```

`sorted(iterable, key=..., reverse=...)` crée une nouvelle liste si tu ne veux pas modifier l’originale.

#### Déduplication, encore (avec URL canonisée)

```python
def dedupliquer_par_url(items):
    """Déduplique en utilisant l’URL canonique.

    À utiliser UNIQUEMENT quand chaque item correspond à une page distincte
    (ex. liste d’articles dont chaque titre pointe vers sa propre URL).
    Pour plusieurs items issus de la même page (citations, livres, lignes
    de tableau...), source_url est partagée — utiliser `dedupliquer(items, "item_id")`
    avec un hash construit sur les champs métier.
    """
    vus = set()
    uniques = []
    for item in items:
        url = canonical_url(item.get("source_url", ""))
        if url and url not in vus:
            vus.add(url)
            uniques.append(item)
    return uniques
```

C’est l’association `clean_text` + `canonical_url` + `dedupliquer` qui transforme un dataset brut en dataset exploitable.

#### Enrichir un enregistrement

L’enrichissement, c’est ajouter de la valeur sans recollecter. Quelques enrichissements courants :

```python
def enrichir(item):
    """Enrichit un enregistrement avec des champs dérivés."""
    url = item.get("source_url", "")
    item["domain"] = domain_of(url)
    item["url_canonical"] = canonical_url(url)
    if "texte" in item:
        item["text_length"] = len(item["texte"])
        item["word_count"] = len(item["texte"].split())
    return item
```

Ce ne sont pas de **nouvelles** données — ce sont des **vues** sur les données existantes, calculées pour faciliter l’analyse en aval.

### Très utile en pratique

#### Le helper `safe_parse_date`

Les dates affichées sur le web sont infiniment variées (« 17 mai 2026 », « il y a 3 jours », « 2026-05-17T10:00:00Z », « 05/17/26 »). Une stratégie défensive :

```python
from datetime import datetime

def safe_parse_date(value):
    """Tente de parser une date ISO. Retourne None sinon."""
    if not value:
        return None
    # ISO 8601 (le cas idéal — depuis <time datetime="...">)
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S",
                "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return None
```

> **Bonne pratique :** garde **toujours** la version brute (`date_affichee`) **en plus** de la version parsée (`date_iso`). Si le parsing se trompe, tu peux corriger sans recollecter.

#### Validation simple

Quelques regex utiles pour valider — sans tomber dans l’over-engineering :

```python
import re

URL_RE = re.compile(r"^https?://[\w.-]+(?:/[\w./?=&%-]*)?$", re.I)
EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def is_valid_url(s):
    return bool(URL_RE.match(s)) if s else False

def is_valid_email(s):
    return bool(EMAIL_RE.match(s)) if s else False
```

À utiliser pour signaler les enregistrements suspects, **pas** pour rejeter silencieusement (mieux vaut un dataset honnête avec un champ `valid_url: False` qu’un dataset amputé).

#### Le pattern de pipeline

```python
# src/clean.py
from pathlib import Path
import json

def clean_pipeline(items, source_url):
    """Pipeline complet : nettoyage + normalisation + enrichissement + déduplication.

    Adapté à des items multiples extraits d’une même page (citations, livres,
    lignes de tableau). On déduplique sur un `item_id` calculé à partir des
    champs métier, pas sur `source_url` (qui serait partagée par tous les items).
    """
    out = []
    for it in items:
        cleaned = {
            "texte": clean_text(it.get("texte")),
            "auteur": clean_text(it.get("auteur")),
            "tags": [clean_text(t) for t in it.get("tags", []) if t.strip()],
            "source_url": canonical_url(it.get("source_url", source_url)),
            "collected_at": it.get("collected_at"),
            "tool": it.get("tool"),
        }
        cleaned = enrichir(cleaned)
        # Identifiant stable construit sur les champs métier
        cleaned["item_id"] = hash_enregistrement(cleaned, ["texte", "auteur"])
        out.append(cleaned)

    out = dedupliquer(out, "item_id")
    out.sort(key=lambda x: x.get("collected_at", ""), reverse=True)
    return out
```

> **Choisir la bonne clé de déduplication :**
> 
> |Type de dataset                                                            |Clé recommandée                   |
> |---------------------------------------------------------------------------|----------------------------------|
> |Liste d’articles (1 article = 1 URL)                                       |`source_url` canonisée            |
> |Citations, livres, lignes de tableau (plusieurs items par page)            |`item_id` = hash sur champs métier|
> |Profils avec identifiant naturel (n° SIRET, ISBN, identifiant scientifique)|Champ ID natif                    |
> 
> En cas de doute, **construis un `item_id` par hash**. C’est l’option la plus défensive.

Ce module reçoit un dataset brut et produit un dataset propre, dans `data/processed/`. C’est la dernière étape avant l’analyse.

#### Détection de langue (en bonus)

Pour des sources internationales, savoir dans quelle langue est un texte est précieux :

```bash
pip install langdetect
```

```python
from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0   # reproductibilité

def detect_lang(text):
    try:
        return detect(text[:500]) if text else None
    except Exception:
        return None
```

> **Limites :** `langdetect` se trompe sur les textes courts (< 30 mots), les textes mixtes, et certaines langues proches (catalan vs espagnol). À utiliser comme **indication**, pas comme vérité absolue.

### Bonus

#### Mise en cache HTTP pour le développement

Pendant que tu mets au point ton script de nettoyage, tu ne veux pas non plus retélécharger le HTML. Une `requests.Session()` + `requests-cache` font ça pour toi :

```bash
pip install requests-cache
```

```python
import requests_cache

session = requests_cache.CachedSession("cache_dev", expire_after=3600)
r = session.get(url, timeout=10)   # première fois : requête réelle
r = session.get(url, timeout=10)   # ensuite : récupéré depuis le cache local
```

À utiliser **uniquement en développement**. En production, on veut des données fraîches et un cache explicite.

### ❌ Erreur classique

```python
# Comparer des URLs sans normaliser
"https://exemple.fr/page" == "https://Exemple.fr/page/"
# → False, mais c’est la même ressource.
# ✅ Toujours canonical_url() avant comparaison.

# Considérer "" et None comme équivalents
if item["auteur"] == "":
    item["auteur"] = "(inconnu)"
# ❌ Casse si auteur vaut None
# ✅ if not item.get("auteur"): ...

# Modifier la liste qu’on parcourt
for item in items:
    if not item["texte"]:
        items.remove(item)
# ❌ Comportement imprévisible
# ✅ items = [i for i in items if i["texte"]]

# Croire que les espaces insécables sont des espaces
"Bonjour\xa0monde".split(" ")  # ❌ ["Bonjour\xa0monde"] (un seul élément)
# ✅ Toujours clean_text() avant traitement

# Sur-nettoyer et perdre l’information brute
item["texte"] = clean_text(item["texte"]).lower().replace("'", "")
# ❌ Tu écrases la donnée originale. Plus moyen de revenir en arrière.
# ✅ Garder l’original ET ajouter une version normalisée si nécessaire :
item["texte_normalized"] = clean_text(item["texte"]).lower()
```

### Exercices

**Guidé :**

1. Reprends le fichier JSON produit au chapitre 8 à partir du mini-projet « Collecteur de citations ».
1. Écris `src/clean.py` qui :
- lit le fichier brut depuis `data/processed/`,
- applique `clean_text` sur chaque champ texte,
- applique `canonical_url` sur les URLs,
- construit un `item_id` par hash sur les champs métier (`texte`, `auteur`),
- déduplique les enregistrements par `item_id`,
- écrit le résultat dans `data/processed/<run_id>_quotes_clean.json`.
1. Compare le nombre d’enregistrements avant/après.

**Autonome :** Écris un script `src/url_inventory.py` qui :

1. Prend en argument un fichier JSON contenant une liste d’URLs (collectées précédemment).
1. Pour chaque URL : canonise, extrait le domaine racine avec `tldextract`, et regroupe.
1. Produit un fichier `data/processed/<run_id>_domains.csv` listant chaque domaine avec le nombre d’URLs associées, trié par fréquence décroissante.

### 🧩 Mini-projet de Partie III — *Extracteur de tableaux Wikipedia*

**Objectif :** combiner toutes les briques des parties II et III sur un cas réel.

**Cible :** une page Wikipedia de ton choix contenant **au moins un tableau de données structurées** (liste de pays, classement, comparaison technique, etc.).

**Contraintes pédagogiques :**

- Respecter le `robots.txt` de Wikipedia.
- Identifier honnêtement ton User-Agent.
- Ne pas dépasser quelques requêtes.
- Wikipedia propose une API officielle (MediaWiki) — pour cet exercice, on scrape **délibérément** le HTML pour s’entraîner. Pour une enquête réelle, on utiliserait l’API.

**Cahier des charges :**

1. **Fiche d’enquête** (`config/fiche-enquete-wiki.md`) remplie avant de coder.
1. **`src/fetch.py`** : récupère la page Wikipedia, sauvegarde le HTML brut dans `data/raw/`.
1. **`src/parse.py`** :
- charge le HTML sauvegardé,
- identifie le tableau pertinent (par sa légende, son `id`, ou son rang dans la page),
- extrait les lignes en liste de dicts,
- applique `clean_text` sur chaque cellule,
- retire les références de type `[1]`, `[note]`.
1. **`src/clean.py`** :
- canonise les URLs trouvées dans les cellules,
- construit un `item_id` par hash sur les champs métier de chaque ligne (par exemple `nom_du_pays` + `année`, ou `produit` + `version`),
- déduplique les lignes par `item_id`,
- enrichit chaque ligne avec `source_url`, `collected_at`, `tool`, `run_id`.
1. **`src/store.py`** : écrit à la fois en CSV (en sérialisant les champs de type liste avec `|` si nécessaire) **et** en JSON avec métadonnées globales.
1. **`src/main.py`** : orchestre, affiche un résumé.

**Livrable :** une exécution complète qui produit :

```
data/raw/<run_id>_wikipedia_<sujet>.html
data/processed/<run_id>_wikipedia_<sujet>.csv
data/processed/<run_id>_wikipedia_<sujet>.json
```

…tous trois reliés par le même `run_id`.

> **Rappel** : `data/raw/` et `data/processed/` restent hors de Git.

### ✅ Tu sais maintenant…

- Nettoyer un texte web (Unicode, espaces insécables, espaces multiples)
- Canoniser une URL (schéma, hôte, slash final, tracking)
- Reconstruire des URLs absolues avec `urljoin`
- Extraire le domaine racine avec `tldextract`
- Trier et filtrer des listes de dicts
- Dédupliquer par URL canonique ou par hash
- Enrichir un enregistrement (champs dérivés)
- Le pipeline `raw → clean → enrich → dedup → processed`

-----

> **🎯 Tu as terminé la Partie III.**
> 
> Tu sais maintenant produire un dataset propre, complet, traçable et dédupliqué à partir d’une seule page. Mais une enquête sérieuse ne s’arrête presque jamais à **une** page : il faut souvent parcourir des dizaines, voire des centaines de pages, ou interroger une API.
> 
> La Partie IV s’attaque à ce passage à l’échelle : pagination, APIs, bonnes pratiques professionnelles (rate limiting, retries, logs, configuration).

-----
