---
title: Chapitre 10 — Pagination et collecte multi-pages
source: Cyber/02_OSINT/Python_Scraping.md
note: Python pour l'OSINT et le scraping
up:
- - Python pour l'OSINT et le scraping
  - ../index.md
- - Partie IV — Passer à L’échelle
  - index.md
---

Tu sais collecter une page. Maintenant : comment passer à 5, 50, 500 pages, **sans devenir une nuisance** et **sans casser à la première erreur**.

## Le minimum à savoir

### Les principaux schémas de pagination

Avant d’écrire la moindre boucle, identifie **comment** le site pagine. Quatre patterns courants :

|Schéma                    |Exemple d’URL              |Comment savoir ?                                            |
|--------------------------|---------------------------|------------------------------------------------------------|
|**Query string `?page=N`**|`/articles?page=2`         |Aller à la page 2 et observer l’URL.                        |
|**Path `/page/N/`**       |`/articles/page/2/`        |Idem. Très courant sur WordPress.                           |
|**Offset / limit**        |`/items?offset=20&limit=10`|Souvent les APIs et les sites avec pas d’items configurable.|
|**Next link**             |`<a rel="next" href="...">`|Lien explicite « page suivante » dans le HTML.              |

Cas particulier : **infinite scroll** (chargement automatique au défilement). Sous le capot, c’est presque toujours une API JSON appelée par la page → voir le chapitre 11. **Ne pas essayer de scraper le HTML rendu** pour ce cas.

### Boucle de collecte avec arrêt explicite

La règle d’or : **deux conditions d’arrêt**, jamais une seule.

```python
import time
from pathlib import Path

BASE_URL = "https://quotes.toscrape.com/page/{page}/"
MAX_PAGES = 20           # plafond dur — sécurité anti-boucle infinie
DELAY = 1.0              # secondes entre deux requêtes

resultats = []
for page in range(1, MAX_PAGES + 1):
    url = BASE_URL.format(page=page)
    print(f"[{page}/{MAX_PAGES}] {url}")

    r, _ = fetch(url)   # fetch défini au chapitre 5
    items = parse(r.content, source_url=url)

    if not items:
        print("Plus de résultats, arrêt.")
        break

    resultats.extend(items)
    time.sleep(DELAY)

print(f"Total collecté : {len(resultats)} items sur {page} pages")
```


Quatre éléments cruciaux :

1. **`MAX_PAGES`** : plafond inconditionnel. Même si le site renvoie indéfiniment des pages, ton script s’arrête.
1. **Arrêt si liste vide** : signal naturel de fin de pagination.
1. **`time.sleep(DELAY)`** : pause entre deux requêtes.
1. **Log de progression** : indispensable pour suivre, debug, et abandonner si besoin (Ctrl+C).

### Jitter : ne pas être trop régulier

Une cadence parfaitement fixe (« exactement 1 requête par seconde, pendant 1 heure ») produit des pics réguliers qui pèsent inutilement sur le serveur. Un peu d’aléa dans le délai lisse la charge, réduit ces pics, et rend la collecte plus respectueuse :

```python
import time
import random

def polite_sleep(base=1.0, jitter=0.5):
    """Dort base + un peu d’aléa, pour éviter une cadence parfaitement régulière."""
    time.sleep(base + random.uniform(0, jitter))
```


`polite_sleep(1.0, 0.5)` dort entre 1.0 et 1.5 seconde. C’est suffisant pour le confort des deux côtés.

> **À retenir :** le jitter est une **politesse réseau**, pas un mécanisme de contournement anti-bot. On ne cherche pas à « ressembler à un humain » pour passer sous les radars : on cherche à étaler la charge sur le serveur. Si le site bloque ou impose une limite explicite, on ralentit ou on arrête — on ne ruse pas. Et si `robots.txt` annonce `Crawl-delay: 5`, on met `DELAY = 5` et on arrête de discuter.

### Pagination par « next link »

C’est le pattern le plus propre : tu suis le lien explicite plutôt que de deviner.

```python
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def next_page(soup, current_url):
    """Cherche un lien rel=next ou un sélecteur explicite."""
    # Méthode 1 : la balise <link rel="next">
    link = soup.find("link", rel="next")
    if link and link.get("href"):
        return urljoin(current_url, link["href"])
    # Méthode 2 : un <a rel="next">
    a = soup.find("a", rel="next")
    if a and a.get("href"):
        return urljoin(current_url, a["href"])
    # Méthode 3 : sélecteur dédié sur la page (à adapter selon le site)
    a = soup.select_one(".next a") or soup.select_one("a.next")
    if a and a.get("href"):
        return urljoin(current_url, a["href"])
    return None
```


Et la boucle devient :

```python
url = BASE_URL
pages_visitees = 0
while url and pages_visitees < MAX_PAGES:
    r, _ = fetch(url)
    soup = BeautifulSoup(r.content, "lxml")
    items = parse(soup, source_url=url)
    resultats.extend(items)
    pages_visitees += 1
    url = next_page(soup, url)
    polite_sleep()
```


C’est plus robuste qu’une boucle basée sur `page=N`, parce que **tu n’inventes pas d’URLs** — tu suis ce que le site te donne.

### Plafond de volume

Au-delà des pages, un plafond sur le **nombre d’items** est une bonne ceinture de sécurité :

```python
MAX_PAGES = 50
MAX_ITEMS = 1000

for page in range(1, MAX_PAGES + 1):
    ...
    if len(resultats) >= MAX_ITEMS:
        print(f"Plafond {MAX_ITEMS} items atteint, arrêt.")
        break
```


## Très utile en pratique

### Tracer chaque page : le journal de collecte

Pour rendre la collecte **reproductible**, journalise chaque page :

```python
import csv
from datetime import datetime, timezone

journal = []  # ou ouvrir un CSV en append

for page in range(1, MAX_PAGES + 1):
    url = BASE_URL.format(page=page)
    started = datetime.now(timezone.utc).isoformat()
    try:
        r, fichier_brut = fetch(url)
        journal.append({
            "page": page,
            "url": url,
            "status": r.status_code,
            "bytes": len(r.content),
            "raw_file": str(fichier_brut),
            "started_at": started,
            "error": "",
        })
    except Exception as e:
        journal.append({
            "page": page,
            "url": url,
            "status": "",
            "bytes": 0,
            "raw_file": "",
            "started_at": started,
            "error": str(e),
        })
        # on continue les autres pages
    polite_sleep()
```


Puis on écrit `journal` dans `logs/<run_id>_pagination.csv`. C’est précieux quand quelque chose s’est mal passé : tu sais exactement quelles pages ont réussi, lesquelles ont échoué, et tu peux reprendre.

### Continuer ou arrêter sur erreur ?

Trois stratégies, à choisir selon le contexte :

|Stratégie                                                             |Pour quoi                                                   |
|----------------------------------------------------------------------|------------------------------------------------------------|
|**Strict** : on s’arrête à la première erreur réseau                  |Petites collectes critiques où on veut tout ou rien.        |
|**Tolérant** : on logge l’erreur et on continue                       |Grandes collectes où une page perdue est acceptable.        |
|**Retry + tolérant** : on retente N fois, puis on logge et on continue|Le bon compromis pour la plupart des cas (voir chapitre 12).|


> **Bonne pratique OSINT** : tolérance par défaut, **mais** chaque page perdue est **explicitement loguée** dans le journal de collecte. Pas de perte silencieuse.

### Détecter la fin de pagination proprement

Quelques signaux fiables de fin :

- Le sélecteur d’items ne renvoie rien sur la page.
- L’URL `next` est absente.
- Le serveur renvoie un 404 sur la page suivante.

**Signaux à ignorer** (ils peuvent être trompeurs) :

- Un 500 isolé : peut être temporaire — on retente.
- Une page avec moins d’items qu’habituellement : peut être la dernière page incomplète, pas une erreur.

### Le squelette réutilisable

```python
# src/paginate.py
import time, random, logging
from urllib.parse import urljoin
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

def polite_sleep(base=1.0, jitter=0.5):
    time.sleep(base + random.uniform(0, jitter))


def next_page(soup, current_url):
    """Cherche un lien rel=next ou un sélecteur explicite vers la page suivante."""
    link = soup.find("link", rel="next")
    if link and link.get("href"):
        return urljoin(current_url, link["href"])
    a = soup.find("a", rel="next")
    if a and a.get("href"):
        return urljoin(current_url, a["href"])
    a = soup.select_one(".next a") or soup.select_one("a.next")
    if a and a.get("href"):
        return urljoin(current_url, a["href"])
    return None


def collect_paginated(start_url, fetch, parse, max_pages=50,
                      max_items=1000, delay=1.0):
    """Collecte paginée par suivi de next link.

    fetch(url) -> (response, raw_file_path)
    parse(soup, source_url) -> list[dict]
    """
    url = start_url
    pages = 0
    items_total = []
    journal = []

    while url and pages < max_pages and len(items_total) < max_items:
        pages += 1
        try:
            r, raw = fetch(url)
            soup = BeautifulSoup(r.content, "lxml")
            items = parse(soup, source_url=url)
            items_total.extend(items)
            journal.append({"url": url, "status": r.status_code,
                            "items": len(items), "raw_file": str(raw)})
            url = next_page(soup, url)
        except Exception as e:
            logger.warning("Erreur sur %s : %s", url, e)
            journal.append({"url": url, "status": "error",
                            "items": 0, "error": str(e)})
            break
        polite_sleep(delay)

    return items_total, journal
```


À glisser dans ton projet `src/paginate.py`. C’est la brique que tu vas réutiliser dès qu’une collecte dépasse une seule page.

## Bonus

### Checkpoint et reprise

Pour les grosses collectes, sauvegarder après chaque page permet de reprendre sans tout refaire :

```python
import json
from pathlib import Path

checkpoint = Path("data/processed/checkpoint.json")

# Si un checkpoint existe : reprendre depuis là
if checkpoint.exists():
    state = json.loads(checkpoint.read_text(encoding="utf-8"))
    url = state["next_url"]
    items_total = state["items"]
else:
    url = START_URL
    items_total = []

while url:
    ...
    # Après chaque page, sauvegarder l’état
    checkpoint.write_text(json.dumps({
        "next_url": url,
        "items": items_total,
    }, ensure_ascii=False), encoding="utf-8")
```


À la fin, supprime le checkpoint. C’est une logique simple, utile dès que la collecte dépasse quelques minutes.

### Pagination par cursor (avancé)

Certaines APIs paginent par **cursor** : la réponse contient un jeton qu’on renvoie pour la suivante. C’est plus stable que `page=N` quand les données changent en cours de collecte. On y reviendra au chapitre 11.

## ❌ Erreur classique

```python
# Pas de plafond
page = 1
while True:
    fetch(f"/page/{page}")
    page += 1
# ❌ Si le site renvoie indéfiniment (page 9999, 10000…), ton script
# ne s’arrête jamais. Plafond DUR obligatoire.

# Pas de pause
for page in range(1, 100):
    fetch(...)
    parse(...)
# ❌ 100 requêtes en quelques secondes = comportement abusif.
# Au minimum time.sleep(1) entre chaque.

# Confondre fin de pagination et erreur réseau
if r.status_code != 200:
    break
# ❌ Un 503 transitoire peut faire croire à la fin de la pagination.
# ✅ Distinguer les statuts : 404 → fin probable, 5xx → retry.

# Inventer des URLs au lieu de suivre les liens
for page in range(1, 100):
    fetch(f"/page/{page}")
# ❌ Si le site a moins de 100 pages, tu fais des requêtes inutiles
# (et tu charges des pages 404 répétées).
# ✅ Détecte la fin via la liste vide ou via next link.

# Tout perdre sur une exception
try:
    for page in range(...):
        ...
except Exception:
    pass
# ❌ Tu perds tous les items collectés avant l’erreur.
# ✅ Try/except à l’intérieur de la boucle, par page.
```


## Exercices

**Guidé :** Sur `https://quotes.toscrape.com/page/{N}/` :

1. Récupère les 5 premières pages avec une pause de 1 seconde entre chaque.
1. Concatène toutes les citations en une seule liste.
1. Affiche le total et le nombre d’auteurs distincts.
1. Sauvegarde un journal `logs/<run_id>_pagination.csv` avec une ligne par page (page, URL, statut, nombre d’items).

**Autonome :** Sur `https://books.toscrape.com/` :

1. Identifie le schéma de pagination utilisé (regarde le lien « next »).
1. Parcours **toute** la pagination en suivant les `next link`.
1. Plafond : 50 pages, 1500 items.
1. Pour chaque livre : titre, prix, disponibilité, note (1-5), URL canonique.
1. Sauvegarde en JSON Lines dans `data/processed/<run_id>_books.jsonl`.
1. Log structuré dans `logs/<run_id>_pagination.csv`.

## ✅ Tu sais maintenant…

- Reconnaître les schémas de pagination (query, path, offset, next link)
- Écrire une boucle de collecte avec **deux** conditions d’arrêt (plafond + fin détectée)
- Espacer les requêtes avec `time.sleep` + jitter
- Suivre un `next link` plutôt qu’inventer des URLs
- Tracer chaque page dans un journal de collecte
- Distinguer fin de pagination, erreur transitoire, et erreur définitive
- Le squelette réutilisable `collect_paginated()`

-----
