---
title: Chapitre 11 — Utiliser des APIs publiques
source: Cyber/02 OSINT/Méthode & enquête/Python pour l'OSINT et le scraping.md
note: Python pour l'OSINT et le scraping
up:
- - Python pour l'OSINT et le scraping
  - ../index.md
- - Partie IV — Passer à l’échelle
  - index.md
---

C’est le chapitre où tu apprends à exploiter des APIs proprement. Et c’est aussi le chapitre où tu vas comprendre **pourquoi l’API est presque toujours préférable au scraping** quand elle existe.

## Le minimum à savoir

### Pourquoi préférer une API

|Critère       |Scraping HTML                                   |API                                                  |
|--------------|------------------------------------------------|-----------------------------------------------------|
|Stabilité     |🔴 Le site peut changer son HTML demain.         |🟢 Les APIs ont des versions et un cycle de vie clair.|
|Cadre légal   |🟡 CGU générales, parfois floues sur le scraping.|🟢 CGU spécifiques de l’API, claires.                 |
|Données       |🟡 Telles qu’affichées (parfois moins riches).   |🟢 Souvent plus riches que ce qui est affiché.        |
|Charge serveur|🔴 Plus lourde (HTML, CSS, JS).                  |🟢 Strict minimum (JSON).                             |
|Identification|🟡 Anonyme par défaut.                           |🟢 Via clé API : tu sais qui tu es, le serveur aussi. |


> **Quand l’API existe et couvre ton besoin, tu l’utilises. Point.** Le scraping ne devient pertinent que si l’API n’existe pas ou ne couvre pas ton cas d’usage.

### Une requête API en pratique

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

### Le JSON, en deux minutes

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


### Gérer les erreurs spécifiques aux APIs

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

### Authentification : la clé API

Beaucoup d’APIs te demandent une **clé** pour t’identifier. Deux modes :

```python
# Mode 1 : clé en paramètre de query
r = requests.get(url, params={"key": API_KEY, "q": "Paris"})

# Mode 2 : header Authorization (plus courant)
headers = {"Authorization": f"Bearer {API_TOKEN}"}
r = requests.get(url, headers=headers)
```


### Stocker une clé API en sécurité

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

### Rate limits côté API

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

### Pagination d’API

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

## Très utile en pratique

### Le pattern complet pour une API publique

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

### Exemple complet sans clé : Open-Meteo

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

### Exemple avec clé : pattern défensif

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

### APIs sans clé utiles pour s’entraîner

|API                          |Sans clé ?|Cas d’usage                                 |
|-----------------------------|----------|--------------------------------------------|
|**Open-Meteo**               |✅         |Météo, climat.                              |
|**REST Countries**           |✅         |Données pays (frontières, devises, langues).|
|**Hacker News API**          |✅         |Actualité tech.                             |
|**MediaWiki / Wikipedia API**|✅         |Articles, métadonnées, modifications.       |
|**JSONPlaceholder**          |✅         |Bac à sable pour apprendre.                 |
|**Datagouv.fr API**          |✅         |Open data administratif français.           |

Pour les APIs avec clé orientées CTI/OSINT, va voir : VirusTotal (clé gratuite avec rate limit serré), urlscan.io, AbuseIPDB, OTX AlienVault, Shodan (clé payante). **Toutes** demandent de respecter strictement leurs CGU.

## Bonus

### Sauvegarder la réponse brute

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

### Identifier les endpoints d’API d’un site

Souvenir du chapitre 3 : si une page charge ses données en JavaScript, le navigateur appelle un endpoint JSON publiquement observable. Tu peux souvent passer du scraping HTML à un usage d’API « non documentée ». Précautions :

- **Vérifie les CGU** : l’absence de doc ne signifie pas l’absence de cadre.
- **Ne contourne aucune authentification** : si l’endpoint exige un token de session, c’est qu’il n’est pas destiné à l’usage automatisé.
- **Respecte la même politesse** que pour une API documentée : rate limit, User-Agent.

Si tu n’es pas certain du cadre, **demande**. Beaucoup de sites répondent positivement à un mail « j’ai vu votre endpoint X, puis-je l’interroger à hauteur de Y requêtes/heure pour Z ? ».

## ❌ Erreur classique

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


## Exercices

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

## 🧩 Mini-projet de Partie IV (1/2) — *Inventaire DNS d’une liste de domaines*

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

## ✅ Tu sais maintenant…

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
