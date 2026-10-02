---
title: Chapitre 9 — Nettoyer, normaliser, enrichir
source: Cyber/02 OSINT/Méthode & enquête/Python pour l'OSINT et le scraping.md
note: Python pour l'OSINT et le scraping
up:
- - Python pour l'OSINT et le scraping
  - ../index.md
- - Partie III — Structurer et nettoyer les données
  - index.md
---

Tu as collecté, tu as stocké. Maintenant tu vas transformer ces données brutes en dataset **propre et exploitable**. Un dataset propre, c’est celui qu’on peut trier, filtrer, comparer dans le temps, et croiser avec d’autres sources sans surprise.

## Le minimum à savoir

### Le pipeline `raw → processed`

Le principe :

```
data/raw/        →    src/clean.py    →    data/processed/
(intouchable)         (transformation)     (exploitable)
```


`clean.py` lit un fichier brut, applique des transformations, et écrit un nouveau fichier. À aucun moment on ne modifie le brut. Si la transformation se trompe, on relance `clean.py` ; pas besoin de retoucher au serveur.

### Nettoyer le texte

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

### Normaliser les URLs

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

### Construire une URL absolue à partir d’une relative

Rappel chapitre 7 : `urljoin` reconstruit l’URL complète à partir de l’URL de la page et d’une URL relative trouvée dans un `href`.

```python
from urllib.parse import urljoin

page = "https://exemple.fr/section/index.html"

print(urljoin(page, "article-1.html"))   # https://exemple.fr/section/article-1.html
print(urljoin(page, "/contact"))          # https://exemple.fr/contact
print(urljoin(page, "https://autre.fr")) # https://autre.fr  (URL déjà absolue conservée)
```


### Extraire le domaine

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

### Trier et filtrer une liste de dicts

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

### Déduplication, encore (avec URL canonisée)

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

### Enrichir un enregistrement

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

## Très utile en pratique

### Le helper `safe_parse_date`

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

### Validation simple

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

### Le pattern de pipeline

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

### Détection de langue (en bonus)

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

## Bonus

### Mise en cache HTTP pour le développement

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

## ❌ Erreur classique

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


## Exercices

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

## 🧩 Mini-projet de Partie III — *Extracteur de tableaux Wikipedia*

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

## ✅ Tu sais maintenant…

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
