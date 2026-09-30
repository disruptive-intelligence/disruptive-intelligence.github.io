---
title: PARTIE IV — PASSER À L’ÉCHELLE
source: Cyber/02_OSINT/Python_Scraping.md
note: Python & scraping
chapter: 5
chapters: 7
---

> **Objectif de la partie :** sortir d’une page unique. Plusieurs pages, plusieurs requêtes, des APIs, une architecture qui tient. Cette partie introduit les outils qui distinguent un script jetable d’un outil OSINT durable : rate limiting, retries, logs, configuration externe, sessions.
> 
> **Garde en tête :** monter à l’échelle, c’est aussi multiplier l’impact sur les serveurs cibles. Tout ce qu’on apprend ici doit être appliqué **avec retenue volontaire**, jamais pour pousser à fond.

-----


## Chapitre 10 — Pagination et collecte multi-pages

Tu sais collecter une page. Maintenant : comment passer à 5, 50, 500 pages, **sans devenir une nuisance** et **sans casser à la première erreur**.

### Le minimum à savoir

#### Les principaux schémas de pagination

Avant d’écrire la moindre boucle, identifie **comment** le site pagine. Quatre patterns courants :

|Schéma                    |Exemple d’URL              |Comment savoir ?                                            |
|--------------------------|---------------------------|------------------------------------------------------------|
|**Query string `?page=N`**|`/articles?page=2`         |Aller à la page 2 et observer l’URL.                        |
|**Path `/page/N/`**       |`/articles/page/2/`        |Idem. Très courant sur WordPress.                           |
|**Offset / limit**        |`/items?offset=20&limit=10`|Souvent les APIs et les sites avec pas d’items configurable.|
|**Next link**             |`<a rel="next" href="...">`|Lien explicite « page suivante » dans le HTML.              |

Cas particulier : **infinite scroll** (chargement automatique au défilement). Sous le capot, c’est presque toujours une API JSON appelée par la page → voir le chapitre 11. **Ne pas essayer de scraper le HTML rendu** pour ce cas.

#### Boucle de collecte avec arrêt explicite

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

#### Jitter : ne pas être trop régulier

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

#### Pagination par « next link »

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

#### Plafond de volume

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

### Très utile en pratique

#### Tracer chaque page : le journal de collecte

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

#### Continuer ou arrêter sur erreur ?

Trois stratégies, à choisir selon le contexte :

|Stratégie                                                             |Pour quoi                                                   |
|----------------------------------------------------------------------|------------------------------------------------------------|
|**Strict** : on s’arrête à la première erreur réseau                  |Petites collectes critiques où on veut tout ou rien.        |
|**Tolérant** : on logge l’erreur et on continue                       |Grandes collectes où une page perdue est acceptable.        |
|**Retry + tolérant** : on retente N fois, puis on logge et on continue|Le bon compromis pour la plupart des cas (voir chapitre 12).|


> **Bonne pratique OSINT** : tolérance par défaut, **mais** chaque page perdue est **explicitement loguée** dans le journal de collecte. Pas de perte silencieuse.

#### Détecter la fin de pagination proprement

Quelques signaux fiables de fin :

- Le sélecteur d’items ne renvoie rien sur la page.
- L’URL `next` est absente.
- Le serveur renvoie un 404 sur la page suivante.

**Signaux à ignorer** (ils peuvent être trompeurs) :

- Un 500 isolé : peut être temporaire — on retente.
- Une page avec moins d’items qu’habituellement : peut être la dernière page incomplète, pas une erreur.

#### Le squelette réutilisable

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

### Bonus

#### Checkpoint et reprise

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

#### Pagination par cursor (avancé)

Certaines APIs paginent par **cursor** : la réponse contient un jeton qu’on renvoie pour la suivante. C’est plus stable que `page=N` quand les données changent en cours de collecte. On y reviendra au chapitre 11.

### ❌ Erreur classique

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

### Exercices

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

### ✅ Tu sais maintenant…

- Reconnaître les schémas de pagination (query, path, offset, next link)
- Écrire une boucle de collecte avec **deux** conditions d’arrêt (plafond + fin détectée)
- Espacer les requêtes avec `time.sleep` + jitter
- Suivre un `next link` plutôt qu’inventer des URLs
- Tracer chaque page dans un journal de collecte
- Distinguer fin de pagination, erreur transitoire, et erreur définitive
- Le squelette réutilisable `collect_paginated()`

-----


## Chapitre 11 — Utiliser des APIs publiques

C’est le chapitre où tu apprends à exploiter des APIs proprement. Et c’est aussi le chapitre où tu vas comprendre **pourquoi l’API est presque toujours préférable au scraping** quand elle existe.

### Le minimum à savoir

#### Pourquoi préférer une API

|Critère       |Scraping HTML                                   |API                                                  |
|--------------|------------------------------------------------|-----------------------------------------------------|
|Stabilité     |🔴 Le site peut changer son HTML demain.         |🟢 Les APIs ont des versions et un cycle de vie clair.|
|Cadre légal   |🟡 CGU générales, parfois floues sur le scraping.|🟢 CGU spécifiques de l’API, claires.                 |
|Données       |🟡 Telles qu’affichées (parfois moins riches).   |🟢 Souvent plus riches que ce qui est affiché.        |
|Charge serveur|🔴 Plus lourde (HTML, CSS, JS).                  |🟢 Strict minimum (JSON).                             |
|Identification|🟡 Anonyme par défaut.                           |🟢 Via clé API : tu sais qui tu es, le serveur aussi. |


> **Quand l’API existe et couvre ton besoin, tu l’utilises. Point.** Le scraping ne devient pertinent que si l’API n’existe pas ou ne couvre pas ton cas d’usage.

#### Une requête API en pratique

```python
import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 48.85,
    "longitude": 2.35,
    "current": "temperature_2m,relative_humidity_2m",
}
headers = {"User-Agent": "MonOutilOSINT/0.1 (+contact: osint-projet@example.org)"}

r = requests.get(url, params=params, headers=headers, timeout=10)
r.raise_for_status()

data = r.json()
print(data["current"])
```

Trois nouveautés par rapport au scraping HTML :

1. **`params={...}`** : `requests` construit l’URL complète (`?latitude=48.85&...`) pour toi. Plus lisible et plus sûr (échappement automatique).
1. **`r.json()`** : parse la réponse JSON en dict/list Python. Pas de BeautifulSoup à l’horizon.
1. **`User-Agent`** : recommandé même pour les APIs publiques. Plusieurs APIs gratuites le **demandent** explicitement.

#### Le JSON, en deux minutes

JSON (JavaScript Object Notation) est un format de données structurées que toute API REST utilise. Quatre types :

|Type JSON                                       |Équivalent Python                             |
|------------------------------------------------|----------------------------------------------|
|`{"clé": "valeur"}`                             |`dict`                                        |
|`["a", "b", "c"]`                               |`list`                                        |
|`"texte"`, `42`, `3.14`, `true`, `false`, `null`|`str`, `int`, `float`, `True`, `False`, `None`|

Une réponse typique :

```json
{
  "current": {
    "temperature_2m": 21.4,
    "relative_humidity_2m": 65
  },
  "elevation": 35.0,
  "timezone": "Europe/Paris"
}
```

Côté Python :

```python
data = r.json()
print(data["current"]["temperature_2m"])  # 21.4
```

#### Gérer les erreurs spécifiques aux APIs

```python
try:
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 401:
        print("Authentification refusée (clé API manquante ou invalide).")
    elif e.response.status_code == 403:
        print("Accès interdit (droits insuffisants).")
    elif e.response.status_code == 429:
        print("Rate limit atteint, ralentir.")
    else:
        print(f"Erreur HTTP : {e.response.status_code}")
except ValueError:
    print("La réponse n’est pas du JSON valide.")
except requests.exceptions.RequestException as e:
    print(f"Erreur réseau : {e}")
```

Les codes typiques d’une API :

|Code |Sens API                                 |
|-----|-----------------------------------------|
|`200`|Succès.                                  |
|`201`|Création réussie (pour les POST).        |
|`204`|Succès sans contenu.                     |
|`400`|Requête malformée (paramètres invalides).|
|`401`|Authentification requise/invalide.       |
|`403`|Authentifié mais pas autorisé.           |
|`404`|Ressource inexistante.                   |
|`429`|**Rate limit dépassé**.                  |
|`5xx`|Erreur côté serveur — à retenter.        |

#### Authentification : la clé API

Beaucoup d’APIs te demandent une **clé** pour t’identifier. Deux modes :

```python
# Mode 1 : clé en paramètre de query
r = requests.get(url, params={"key": API_KEY, "q": "Paris"})

# Mode 2 : header Authorization (plus courant)
headers = {"Authorization": f"Bearer {API_TOKEN}"}
r = requests.get(url, headers=headers)
```

#### Stocker une clé API en sécurité

**Jamais en dur dans le code.** Trois bonnes pratiques :

1. **Variable d’environnement** :

```python
import os
API_KEY = os.getenv("MON_API_KEY")
if not API_KEY:
    raise RuntimeError("Définis la variable d’environnement MON_API_KEY")
```

Tu définis la variable hors de ton code :

```bash
export MON_API_KEY="abc123..."     # Linux/Mac
$env:MON_API_KEY = "abc123..."     # PowerShell
```

1. **Fichier `.env`** (non versionné, dans `.gitignore`) lu par `python-dotenv` :

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
load_dotenv()  # charge .env
API_KEY = os.getenv("MON_API_KEY")
```

1. **Gestionnaire de secrets** (avancé) : Keychain, KeePass, Vault…

> **Risque réel :** une clé API commitée sur GitHub est trouvée et exploitée par des bots en moins d’une heure. Tu peux te retrouver avec une facture, un compte bloqué, ou pire — un mauvais usage attribué à toi. **Jamais en dur, jamais commitée.**

#### Rate limits côté API

Les APIs sérieuses te disent leurs limites dans les headers de réponse :

```python
print(r.headers.get("X-RateLimit-Limit"))      # par ex. "60"
print(r.headers.get("X-RateLimit-Remaining"))  # par ex. "12"
print(r.headers.get("X-RateLimit-Reset"))      # timestamp avant remise à zéro
```

Et quand tu dépasses : `429 Too Many Requests`, souvent avec un header `Retry-After: 30` (secondes à attendre).

```python
if r.status_code == 429:
    retry_after = int(r.headers.get("Retry-After", 60))
    print(f"Rate limit atteint, attente de {retry_after} s...")
    time.sleep(retry_after)
```

> **À retenir :** **respecte** les rate limits. Un compte qui ignore les limites finit bloqué, et il finit **bien** par être bloqué. Ralentir volontairement est plus rentable que se faire bannir.

#### Pagination d’API

Trois patterns courants :

```python
# 1. page / per_page
r = requests.get(url, params={"page": 2, "per_page": 100})

# 2. offset / limit
r = requests.get(url, params={"offset": 200, "limit": 100})

# 3. cursor (jeton renvoyé par la réponse précédente)
cursor = None
while True:
    params = {"limit": 100}
    if cursor:
        params["cursor"] = cursor
    r = requests.get(url, params=params, timeout=10)
    data = r.json()
    items.extend(data["results"])
    cursor = data.get("next_cursor")
    if not cursor:
        break
```

Le pattern « cursor » est le plus robuste pour les APIs qui changent en cours de collecte (ajouts, suppressions). Lis toujours la doc de l’API avant.

### Très utile en pratique

#### Le pattern complet pour une API publique

```python
# src/api_client.py
import os
import time
import logging
import requests
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

class ApiClient:
    def __init__(self, base_url, api_key=None, user_agent=None, timeout=10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        if user_agent:
            self.session.headers["User-Agent"] = user_agent
        if api_key:
            self.session.headers["Authorization"] = f"Bearer {api_key}"

    def get(self, path, params=None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        for attempt in range(3):
            r = self.session.get(url, params=params, timeout=self.timeout)
            if r.status_code == 429:
                wait = int(r.headers.get("Retry-After", 30))
                logger.warning("Rate limit, attente %ds (essai %d/3)", wait, attempt + 1)
                time.sleep(wait)
                continue
            r.raise_for_status()
            return r.json()
        raise RuntimeError("Trop de rate limits successifs")
```

Cet objet `ApiClient` encapsule : `User-Agent`, clé API, session HTTP, retries sur 429, timeout. C’est ton point d’entrée pour toute API.

> **Note :** ce client gère explicitement le `429` (rate limit). Les erreurs `5xx` transitoires (502, 503, 504) ne sont pas retentées ici — elles le seront proprement avec `Retry` + backoff exponentiel au chapitre 12. Pour l’instant, elles remontent en exception et l’appelant décide.

#### Exemple complet sans clé : Open-Meteo

```python
client = ApiClient(
    "https://api.open-meteo.com",
    user_agent="MonOutilOSINT/0.1 (+contact: osint-projet@example.org)"
)

data = client.get("/v1/forecast", params={
    "latitude": 48.85,
    "longitude": 2.35,
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "Europe/Paris",
})

print(data["daily"])
```

Cette API ne demande pas de clé et fournit des données météo riches. Idéale pour s’entraîner.

#### Exemple avec clé : pattern défensif

Un exemple générique (le nom de l’API n’a pas d’importance, le pattern est le même) :

```python
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("CTI_API_KEY")
if not API_KEY:
    raise RuntimeError("Définis CTI_API_KEY dans ton .env")

client = ApiClient(
    base_url="https://api.exemple-cti.example/v1",
    api_key=API_KEY,
    user_agent="MonOutilOSINT/0.1 (+contact: osint-projet@example.org)"
)

# Exemple d’interrogation
indicators = client.get("/indicators/recent", params={"limit": 50})
```

Avant d’interroger une API CTI avec une vraie clé, **lis ses CGU** : usage défensif, données autorisées, rate limits, conditions de partage des résultats. Une API qui t’autorise à interroger ne t’autorise pas toujours à republier.

#### APIs sans clé utiles pour s’entraîner

|API                          |Sans clé ?|Cas d’usage                                 |
|-----------------------------|----------|--------------------------------------------|
|**Open-Meteo**               |✅         |Météo, climat.                              |
|**REST Countries**           |✅         |Données pays (frontières, devises, langues).|
|**Hacker News API**          |✅         |Actualité tech.                             |
|**MediaWiki / Wikipedia API**|✅         |Articles, métadonnées, modifications.       |
|**JSONPlaceholder**          |✅         |Bac à sable pour apprendre.                 |
|**Datagouv.fr API**          |✅         |Open data administratif français.           |

Pour les APIs avec clé orientées CTI/OSINT, va voir : VirusTotal (clé gratuite avec rate limit serré), urlscan.io, AbuseIPDB, OTX AlienVault, Shodan (clé payante). **Toutes** demandent de respecter strictement leurs CGU.

### Bonus

#### Sauvegarder la réponse brute

Comme pour le HTML : sauvegarde toujours la réponse JSON brute dans `data/raw/` avant de la transformer.

```python
import json
from pathlib import Path
from datetime import datetime, timezone

def save_api_response(data, source, run_id, raw_dir="data/raw"):
    """Sauvegarde une réponse JSON brute avec métadonnées."""
    out = Path(raw_dir) / f"{run_id}_{source}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    wrapped = {
        "metadata": {
            "source": source,
            "run_id": run_id,
            "collected_at": datetime.now(timezone.utc).isoformat(),
        },
        "data": data,
    }
    out.write_text(json.dumps(wrapped, ensure_ascii=False, indent=2),
                   encoding="utf-8")
    return out
```

Ça garantit la **reproductibilité** : tu peux refaire ton analyse plus tard sans réinterroger l’API.

#### Identifier les endpoints d’API d’un site

Souvenir du chapitre 3 : si une page charge ses données en JavaScript, le navigateur appelle un endpoint JSON publiquement observable. Tu peux souvent passer du scraping HTML à un usage d’API « non documentée ». Précautions :

- **Vérifie les CGU** : l’absence de doc ne signifie pas l’absence de cadre.
- **Ne contourne aucune authentification** : si l’endpoint exige un token de session, c’est qu’il n’est pas destiné à l’usage automatisé.
- **Respecte la même politesse** que pour une API documentée : rate limit, User-Agent.

Si tu n’es pas certain du cadre, **demande**. Beaucoup de sites répondent positivement à un mail « j’ai vu votre endpoint X, puis-je l’interroger à hauteur de Y requêtes/heure pour Z ? ».

### ❌ Erreur classique

```python
# Clé API en dur dans le code
API_KEY = "sk_live_abc123..."   # ❌ commit accidentel = clé compromise
# ✅ os.getenv("API_KEY") + .env dans .gitignore

# Ignorer le 429
r = requests.get(url, params=...)
if r.status_code == 200:
    process(r.json())
# ❌ Tous les 429 sont ignorés silencieusement → données manquantes
# ✅ Gérer explicitement le 429 avec Retry-After

# Confondre params et data
r = requests.get(url, data={"q": "Paris"})
# ❌ data= envoie un corps en POST. Pour GET avec query, c’est params=.
r = requests.get(url, params={"q": "Paris"})   # ✅

# Oublier r.raise_for_status() puis appeler r.json()
r = requests.get(url, timeout=10)
data = r.json()
# ❌ Si la réponse est une page d’erreur HTML, r.json() lève ValueError
# ✅ raise_for_status() d’abord, json() ensuite

# Marteler une API gratuite
for i in range(10000):
    requests.get(url, params={...})
# ❌ Ban quasi garanti, perte de la ressource pour tous les autres
# ✅ Respecter les rate limits annoncés + plafond local
```

### Exercices

**Guidé :**

1. Choisis l’API Open-Meteo.
1. Pour une liste de 5 villes (lat/lon), récupère la température actuelle.
1. Sauvegarde chaque réponse brute dans `data/raw/<run_id>_openmeteo_<ville>.json`.
1. Produit un fichier `data/processed/<run_id>_meteo.csv` avec colonnes : `ville`, `latitude`, `longitude`, `temperature`, `collected_at`.
1. Respecte une pause de 1 seconde entre chaque ville.

**Autonome :**

1. Choisis une API publique sans clé qui t’intéresse (REST Countries, MediaWiki, etc.).
1. Identifie un endpoint et un paramètre intéressants.
1. Écris `src/api_explore.py` qui : prend un argument en CLI, interroge l’API, sauvegarde la réponse brute, et affiche un résumé.
1. Gère explicitement les erreurs 404 et 429.
1. Documente dans un mini-README : URL de l’API, endpoint utilisé, rate limit annoncé, lien vers les CGU.

### 🧩 Mini-projet de Partie IV (1/2) — *Inventaire DNS d’une liste de domaines*

**Objectif :** combiner des sources publiques d’infrastructure (principalement DNS, éventuellement RDAP) et un peu de Python pour produire un inventaire minimal d’une liste de domaines fournis en entrée. Cas d’usage défensif typique : avoir une vue d’ensemble des serveurs d’un périmètre qu’on connaît.

**Cible :** **uniquement** des domaines que tu administres, ou des domaines publics manifestement de test (`example.com`, `iana.org`).

**Outils :**

- `dnspython` (`pip install dnspython`) pour les résolutions DNS classiques (A, AAAA, MX, NS, TXT) — c’est plus propre qu’une API tierce pour ces données.
- Optionnellement, une API publique RDAP pour récupérer les infos d’enregistrement quand elles sont disponibles (`https://rdap.org/`).

**Cahier des charges :**

1. **Entrée** : `config/domaines.txt` (un domaine par ligne).
1. **Pour chaque domaine** :
- résolution A, AAAA, MX, NS, TXT,
- éventuellement appel RDAP (gestion d’erreur si non disponible),
- délai de 1 s entre deux domaines.
1. **Sortie** :
- `data/processed/<run_id>_dns_inventory.json` avec une entrée structurée par domaine,
- `logs/<run_id>_dns.log` avec progression et erreurs.
1. **Fiche d’enquête** remplie en amont.
1. **Aucune** tentative de zone transfer ou de fuzzing — c’est de la résolution publique normale.

### ✅ Tu sais maintenant…

- Distinguer scraping et exploitation d’API (et préférer l’API quand elle existe)
- Faire une requête API avec `params`, `headers`, `timeout`
- Exploiter une réponse JSON avec `.json()`
- Gérer les codes spécifiques aux APIs (401, 403, 429)
- Stocker une clé API hors du code (env, `.env`)
- Respecter les rate limits (`429`, `Retry-After`)
- Pagination d’API (page, offset, cursor)
- Pattern `ApiClient` réutilisable avec session, retries 429, User-Agent
- Sauvegarder la réponse brute dans `data/raw/` pour reproductibilité

-----


## Chapitre 12 — Bonnes pratiques professionnelles

Tu sais collecter, parser, stocker, paginer, interroger des APIs. Ce chapitre rassemble les **outils qui transforment un script qui marche en outil qui dure**. Pas de nouveau concept de collecte ici — uniquement de la robustesse, de la lisibilité, et de la maintenance.

### Le minimum à savoir

#### `requests.Session()` : la base

Tu l’as vue en bonus au chapitre 5. Maintenant on l’adopte par défaut :

```python
import requests

session = requests.Session()
session.headers.update({
    "User-Agent": "MonOutilOSINT/0.1 (+contact: osint-projet@example.org)",
    "Accept-Language": "fr,en;q=0.8",
})

# Toutes les requêtes utilisent les mêmes headers et réutilisent la connexion
r1 = session.get("https://exemple.fr/page1", timeout=10)
r2 = session.get("https://exemple.fr/page2", timeout=10)
```

Avantages :

- Headers partagés en une seule définition.
- Réutilisation de la connexion TCP/TLS (plus rapide).
- Gestion automatique des cookies (utile pour suivre une session si nécessaire).

#### Retries avec backoff exponentiel

Plutôt que d’abandonner à la première erreur réseau, on retente avec un délai qui **augmente** à chaque essai :

```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import requests

def make_session():
    session = requests.Session()
    session.headers["User-Agent"] = "MonOutilOSINT/0.1 (+contact: osint-projet@example.org)"

    retry = Retry(
        total=4,                       # nombre max d’essais
        backoff_factor=1.5,            # délai = backoff * (2 ** (essai - 1))
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods={"GET", "HEAD"},
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session
```

Avec `backoff_factor=1.5`, les délais sont : 0, 1.5, 3, 6, 12 s.

> **Important :** ce retry **automatique** se déclenche sur les statuts définis. Pour autant, tu dois **toujours** plafonner par toi-même (`MAX_PAGES`, `MAX_ITEMS`) — la combinaison « retry + plafond » te protège de tous les côtés.

#### Le module `logging` : la base professionnelle

`print()` est très bien pour débug rapide. Pour un outil maintenable, on passe à `logging` :

```python
import logging
from datetime import datetime, timezone
from pathlib import Path

def setup_logging(run_id, log_dir="logs", level=logging.INFO):
    """Configure logs vers fichier ET console."""
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    log_file = Path(log_dir) / f"{run_id}.log"

    fmt = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"

    logging.basicConfig(
        level=level,
        format=fmt,
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )
    logger = logging.getLogger("collecteur")
    logger.info("Démarrage run_id=%s", run_id)
    return logger
```

Usage dans le code :

```python
logger = logging.getLogger(__name__)

logger.debug("Détail technique pour le développement")
logger.info("Information attendue (avancement normal)")
logger.warning("Quelque chose d’anormal mais non bloquant")
logger.error("Erreur — on continue avec d’autres données")
logger.critical("Erreur grave — arrêt du programme")
```

Niveaux à retenir :

|Niveau    |Quand l’utiliser                           |
|----------|-------------------------------------------|
|`DEBUG`   |Détails utiles uniquement en développement.|
|`INFO`    |Étapes normales du programme.              |
|`WARNING` |Anomalie qu’on tolère.                     |
|`ERROR`   |Échec d’une opération.                     |
|`CRITICAL`|Échec qui arrête le programme.             |


> **À retenir :** un `logger.info("Récupération de %s", url)` qui passe sa variable en argument séparé est plus performant qu’un f-string, parce que le formatage n’a lieu que si le niveau est actif. À adopter par habitude.

#### Configuration externe

**Tout** ce qui change entre deux exécutions ou deux utilisateurs doit sortir du code. Trois mécanismes complémentaires :

**1. Arguments CLI avec `argparse`**

```python
import argparse

def parse_args():
    p = argparse.ArgumentParser(description="Collecteur OSINT")
    p.add_argument("--config", default="config/config.yaml", help="Fichier de config")
    p.add_argument("--target", required=True, help="URL ou identifiant de cible")
    p.add_argument("--max-pages", type=int, default=20)
    p.add_argument("--delay", type=float, default=1.0)
    p.add_argument("-v", "--verbose", action="store_true")
    return p.parse_args()
```

**2. Fichier de configuration (`config/config.yaml` ou `config/config.json`)**

```yaml
# config/config.yaml
output_dir: data/processed
raw_dir: data/raw
log_dir: logs
user_agent: "MonOutilOSINT/0.1 (+contact: osint-projet@example.org)"
default_timeout: 10
default_delay: 1.5
max_pages: 50
max_items: 1000
```

```python
import yaml
from pathlib import Path

config = yaml.safe_load(Path("config/config.yaml").read_text(encoding="utf-8"))
```

(Nécessite `pip install pyyaml` ; alternative sans dépendance : JSON.)

**3. Variables d’environnement (secrets uniquement)**

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("CTI_API_KEY")
```

Règle simple :

|Type                               |Où ?                              |
|-----------------------------------|----------------------------------|
|Paramètres de runtime              |CLI args                          |
|Paramètres stables d’un déploiement|Fichier de config                 |
|Secrets                            |Variables d’environnement / `.env`|

#### Séparation code / données / config / secrets

Arborescence d’un projet OSINT mature :

```
osint-collecte/
├── src/                  ← code Python
│   ├── __init__.py
│   ├── fetch.py
│   ├── parse.py
│   ├── clean.py
│   ├── store.py
│   ├── paginate.py
│   ├── api_client.py
│   ├── report.py         (chapitre 14)
│   └── main.py
├── config/
│   ├── config.yaml       ← paramètres (versionné)
│   ├── targets.txt       ← cibles (selon le projet : versionné ou non)
│   └── fiche-enquete.md  ← gabarit (versionné)
├── data/
│   ├── raw/              ← collectes brutes (NON versionné)
│   └── processed/        ← données traitées (NON versionné)
├── logs/                 ← journaux (NON versionné)
├── reports/              ← rapports (selon sensibilité)
├── tests/                ← tests (versionné)
├── .env                  ← secrets (NON versionné)
├── .env.example          ← modèle de .env (versionné)
├── .gitignore
├── requirements.txt
└── README.md
```

Le `.env.example` est un détail qui change tout : il documente quelles variables d’environnement sont attendues, sans les valeurs réelles. Toi ou un collègue n’a qu’à le copier en `.env` et remplir.

```
# .env.example
CTI_API_KEY=
WEATHER_API_KEY=
```

#### Reproductibilité

Pour qu’une enquête soit reproductible, conserve :

1. **`requirements.txt`** figé (`pip freeze > requirements.txt`).
1. **Version Python** documentée dans le README (`Python 3.12+`).
1. **`run_id` partagé** entre tous les artefacts d’une exécution.
1. **Fiche d’enquête** complète, archivée dans `reports/`.
1. **Le code lui-même versionné** (Git), avec une **release** ou un **commit** identifiable cité dans le rapport.

> **À retenir :** une enquête OSINT non reproductible n’a pas de valeur d’enquête. Un collègue (ou toi-même dans six mois) doit pouvoir refaire la collecte et arriver au même résultat.

#### Documentation : le README minimum vital

```markdown
# Mon collecteur OSINT

## Objectif
Une phrase. Pour quoi ce projet existe.

## Limites et cadre
- Sources autorisées : <liste>
- Cibles interdites : <liste>
- Base légale et finalité : <résumé>

## Installation
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    cp .env.example .env  # puis remplir

## Usage
    python -m src.main --target <url> --max-pages 20

## Structure
- `src/` : code
- `config/` : paramètres et cibles
- `data/raw/` : collectes brutes (non versionné)
- `data/processed/` : données traitées (non versionné)
- `logs/` : journaux

## Cadre éthique
Ce projet collecte uniquement des données publiques, dans le respect
de robots.txt et des CGU des sites cibles. Pour toute question :
osint-projet@example.org

## Auteur et licence
<...>
```

### Très utile en pratique

#### Pattern de `main.py` complet

Voici à quoi ressemble un point d’entrée mature :

```python
# src/main.py
import sys
import logging
import yaml
from datetime import datetime, timezone
from pathlib import Path

from src.fetch import make_session, fetch
from src.parse import parse_page
from src.paginate import collect_paginated
from src.store import write
from src.clean import clean_pipeline


def main():
    args = parse_args()
    config = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    logger = setup_logging(run_id, log_dir=config["log_dir"])

    logger.info("Cible : %s", args.target)
    logger.info("Max pages : %d, délai : %.1fs", args.max_pages, args.delay)

    session = make_session()

    try:
        items, journal = collect_paginated(
            args.target,
            fetch=lambda url: fetch(url, session=session,
                                    raw_dir=config["raw_dir"], run_id=run_id),
            parse=parse_page,
            max_pages=args.max_pages,
            max_items=config["max_items"],
            delay=args.delay,
        )
    except Exception as e:
        logger.critical("Collecte interrompue : %s", e)
        sys.exit(1)

    logger.info("Collecte terminée : %d items, %d pages", len(items), len(journal))

    cleaned = clean_pipeline(items, source_url=args.target)
    out = Path(config["output_dir"]) / f"{run_id}_collecte.json"
    write({"metadata": {"run_id": run_id, "tool": "collecteur/0.1",
                        "count": len(cleaned), "target": args.target},
           "data": cleaned}, out, format="json")
    logger.info("Sortie : %s", out)


if __name__ == "__main__":
    main()
```

Tu reconnais toutes les briques des chapitres précédents : `fetch`, `parse`, `paginate`, `clean`, `store`. Le `main` les **orchestre**, mais ne fait pas de travail de collecte lui-même.

#### OPSEC : rappel final

|Réflexe                                  |Pourquoi                                           |
|-----------------------------------------|---------------------------------------------------|
|User-Agent identifiable                  |Honnêteté, traçabilité, contact en cas de problème.|
|Timeout obligatoire                      |Pas de script qui pend.                            |
|Rate limit volontaire                    |Respect du serveur, anti-bannissement.             |
|Pas d’usurpation anti-bot                |Question éthique et signal d’intention.            |
|Secrets hors code                        |Pas de fuite via Git.                              |
|VPN si besoin (selon contexte)           |Séparer ses identités d’enquête et personnelles.   |
|`data/raw/` et `data/processed/` hors Git|Pas de fuite de données sensibles.                 |
|Logs structurés et conservés             |Reproductibilité, traçabilité.                     |

#### Tests basiques (bonus)

Pour les fonctions pures (parsing, nettoyage), des tests `pytest` simples valent leur pesant d’or :

```python
# tests/test_clean.py
from src.clean import clean_text, canonical_url

def test_clean_text_removes_nbsp():
    assert clean_text("Bonjour\xa0le\xa0monde") == "Bonjour le monde"

def test_canonical_url_removes_utm():
    url = "https://Ex.fr/page?utm_source=x&id=42"
    assert canonical_url(url) == "https://ex.fr/page?id=42"
```

`pytest` détecte automatiquement les fichiers `test_*.py` et les fonctions `test_*`. Lance avec :

```bash
pip install pytest
pytest
```

C’est hors-scope pour ce cours, mais à adopter dès qu’un projet dépasse quelques scripts.

### Bonus

#### `requests-cache` pour le développement

Évite de retélécharger la même page pendant que tu mets au point ton parser :

```python
import requests_cache
session = requests_cache.CachedSession("dev_cache", expire_after=3600)
```

**À désactiver en production** — tu veux des données fraîches.

#### Niveau `logging` configurable

```python
# Permettre -v pour DEBUG, -vv pour tout, sinon INFO
def log_level(verbose):
    return [logging.WARNING, logging.INFO, logging.DEBUG][min(verbose, 2)]
```

```python
logging.basicConfig(level=log_level(args.verbose), ...)
```

### ❌ Erreur classique

```python
# Hardcoder les paramètres dans le script
TARGET = "https://exemple.fr"
MAX_PAGES = 20
# ❌ Pour changer une cible, il faut éditer le code.
# ✅ argparse + config.yaml.

# print() pour tout
print(f"Récupération de {url}")
# ❌ Pas de niveaux, pas de fichier de log, pas de timestamps automatiques.
# ✅ logging.info("Récupération de %s", url)

# Logger les secrets
logger.info("Auth header : %s", session.headers)
# ❌ Tu loggues ta clé API en clair dans logs/...log
# ✅ Filtrer les headers sensibles avant de logger

# Capture trop large
try:
    ...
except Exception:
    pass
# ❌ Tu masques tous les bugs, y compris dans ton propre code.
# ✅ Capture des exceptions spécifiques + logging.error pour les inattendues.

# Pas de requirements.txt
# ❌ Personne ne peut reproduire ton environnement, y compris toi dans 6 mois.
# ✅ pip freeze > requirements.txt après chaque ajout de dépendance.

# Versionner data/raw/ ou .env
# ❌ Fuite de données + secrets exposés
# ✅ .gitignore strict, .env.example pour documenter
```

### Exercices

**Guidé :**

1. Reprends le mini-projet « Collecteur de citations » et refactorise-le pour utiliser :
- `requests.Session()` avec User-Agent partagé,
- `Retry` automatique sur les statuts transitoires,
- `logging` avec fichier `logs/<run_id>.log`,
- `argparse` pour `--url`, `--max-pages`, `--delay`, `-v`,
- `config/config.yaml` pour les paramètres stables.
1. Vérifie qu’il fonctionne toujours sans paramètres explicites (valeurs par défaut sensées).
1. Vérifie qu’il logge bien la durée totale et le nombre de retries effectués.

**Autonome :**

1. Écris un script `src/check.py` qui charge `config/config.yaml`, vérifie que tous les dossiers `raw_dir`, `output_dir`, `log_dir` existent (et les crée sinon), et qu’une variable d’environnement `CTI_API_KEY` est définie (sans afficher sa valeur).
1. Affiche un rapport `✓` / `✗` par vérification.
1. Renvoie un code de sortie 0 si tout va bien, 1 sinon.
1. Documente l’usage dans le README.

### 🧩 Mini-projet de Partie IV (2/2) — *Collecteur d’articles publics*

**Objectif :** un collecteur d’articles paginé, complet et professionnel. C’est l’occasion de mettre ensemble pagination, sessions, retries, logs, configuration externe.

**Cibles autorisées (par ordre de préférence, conformément à la doctrine API > RSS > sitemap > open data > scraping) :**

- soit un **site bac à sable** qui pagine en HTML (`books.toscrape.com`, `quotes.toscrape.com` avec sa pagination par `/page/N/`) ;
- soit un **blog technique public** qui **n’expose ni RSS ni sitemap exploitable** pour le besoin précis du projet ;
- soit un **flux RSS ou un sitemap** lorsqu’il existe — dans ce cas, **le projet doit consommer cette source propre** plutôt que scraper le HTML rendu, et on adapte l’architecture en conséquence (parsing XML via `feedparser` ou `xml.etree`).

Le but pédagogique reste le même : pagination, sessions, retries, logs, configuration externe — mais on n’invente pas une raison de scraper si une source plus propre est disponible.

**Cahier des charges :**

1. **Configuration** (`config/articles.yaml`) :
- URL de départ,
- `max_pages`,
- `max_items`,
- `delay`,
- `output_dir`, `raw_dir`, `log_dir`.
1. **Architecture** :
- `src/fetch.py` : session, retries, sauvegarde brute.
- `src/parse.py` : extraction des articles (titre, URL canonique, date, auteur, résumé, tags).
- `src/paginate.py` : collecte multi-pages avec `next link`.
- `src/clean.py` : nettoyage + canonisation + déduplication par URL canonique (chaque article = une URL distincte, donc `source_url` convient).
- `src/store.py` : sortie en JSON Lines (append-friendly).
- `src/main.py` : orchestration + CLI + logging.
1. **Politesse** :
- `Crawl-delay` de robots.txt respecté.
- User-Agent identifiable.
- Plafonds explicites.
1. **Reproductibilité** :
- `run_id` partagé entre `data/raw/`, `data/processed/`, `logs/`.
- `requirements.txt` figé.
- `README.md` avec installation, usage, cadre éthique.
1. **Livrables** :
- Une exécution complète avec ses artefacts.
- Le journal `logs/<run_id>.log` lisible et complet.
- Le dataset propre dans `data/processed/<run_id>_articles.jsonl`.

> **Rappel** : `data/` et `.env` restent hors de Git. Ne pousse que `src/`, `config/` (sans secrets), `requirements.txt`, `README.md`, et éventuellement `tests/`.

### ✅ Tu sais maintenant…

- Utiliser `requests.Session()` par défaut
- Configurer `Retry` avec backoff exponentiel pour les statuts transitoires
- Mettre en place `logging` avec fichier + console et niveaux pertinents
- Sortir les paramètres du code : `argparse` + `config.yaml` + `.env`
- Architecturer un projet OSINT mature (`src/`, `data/`, `config/`, `logs/`, `reports/`)
- Documenter avec un README clair et un `.env.example`
- Tenir une enquête **reproductible** (run_id, requirements.txt, version Python, code versionné)
- Orchestrer une collecte complète depuis un `main.py` lisible

-----

> **🎯 Tu as terminé la Partie IV.**
> 
> Tu sais maintenant collecter à l’échelle, exploiter des APIs et structurer un projet professionnel. Mais l’OSINT ne s’arrête pas à la collecte ponctuelle. Une bonne partie du métier consiste à **surveiller dans le temps** : détecter les nouvelles publications, repérer les changements, produire des rapports lisibles.
> 
> La Partie V s’attaque à ça : veille et reporting.

-----
