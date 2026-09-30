---
title: Chapitre 5 — Premières requêtes avec requests
source: Cyber/02_OSINT/Python_Scraping.md
note: Python pour l'OSINT et le scraping
up:
- - Python pour l'OSINT et le scraping
  - ../index.md
- - Partie II — Premières collectes
  - index.md
---

C’est ton premier chapitre où on touche au clavier pour faire dialoguer ton script avec un serveur. La règle d’or de ce chapitre : **on récupère, on sauvegarde, on parse hors ligne**. On ne tape pas le serveur dix fois pendant qu’on debug le parser.

> **Checklist avant chaque requête réelle :**
> 
> - ☑ Cible pédagogique (`toscrape.com`, `httpbin.org`) ou autorisée par les CGU
> - ☑ `robots.txt` consulté
> - ☑ CGU vérifiées si cible réelle
> - ☑ User-Agent identifiable défini
> - ☑ `timeout=` défini sur toutes les requêtes
> - ☑ Volume limité (plafond explicite)
> - ☑ Sauvegarde brute dans `data/raw/` prévue
> 
> Si une case n’est pas cochée, ne lance pas le script.

## Le minimum à savoir

### Installation rappel

Si tu as fait le chapitre 0, c’est déjà installé. Sinon :

```bash
source .venv/bin/activate
pip install requests
```


Vérifie :

```python
import requests
print(requests.__version__)
```


### La première requête

```python
import requests

response = requests.get("https://httpbin.org/get", timeout=10)
print(response.status_code)
print(response.text[:200])
```


Trois choses essentielles :

1. **`requests.get(url, ...)`** envoie une requête GET.
1. **`timeout=10`** : **non négociable**. Sans timeout, ton script peut pendre indéfiniment si le serveur ne répond pas.
1. **`response`** est l’objet qui contient toute la réponse.

> **À retenir :** **jamais** de `requests.get()` sans `timeout=`. C’est la première règle des scripts web.

### L’objet Response

|Attribut              |Contenu                                    |
|----------------------|-------------------------------------------|
|`response.status_code`|Code de statut (`200`, `404`, etc.)        |
|`response.text`       |Corps de la réponse en `str` (texte décodé)|
|`response.content`    |Corps de la réponse en `bytes` (brut)      |
|`response.headers`    |Dictionnaire des headers de réponse        |
|`response.encoding`   |Encodage utilisé pour décoder `.text`      |
|`response.url`        |URL finale (après éventuelles redirections)|
|`response.history`    |Liste des redirections qui ont précédé     |
|`response.json()`     |Parse le corps comme JSON (si applicable)  |

Exemple :

```python
import requests

r = requests.get("https://httpbin.org/get", timeout=10)

print(f"Statut       : {r.status_code}")
print(f"URL finale   : {r.url}")
print(f"Encodage     : {r.encoding}")
print(f"Type contenu : {r.headers.get('Content-Type')}")
print(f"Taille       : {len(r.content)} octets")
```


### `text` vs `content`

- `response.text` → la réponse **décodée** en chaîne de caractères, prête à manipuler.
- `response.content` → la réponse **brute** en bytes, telle qu’elle est arrivée sur le câble.

Quand utiliser quoi ?

|Cas                                                   |À utiliser|
|------------------------------------------------------|----------|
|Parser du HTML/JSON pour exploitation immédiate       |`.text`   |
|Sauvegarder fidèlement la page pour retraitement futur|`.content`|
|Télécharger une image, un PDF, un fichier binaire     |`.content`|


> **Bonne pratique OSINT :** quand tu sauvegardes une page brute dans `data/raw/`, écris `.content` en mode binaire (`"wb"`). C’est la **preuve** de ce que tu as reçu, indépendante de l’encodage.

### Sauvegarder une page proprement

```python
import requests
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

url = "https://books.toscrape.com/"
headers = {"User-Agent": "MonOutilOSINT/0.1 (+contact: osint-projet@example.org)"}

r = requests.get(url, headers=headers, timeout=10)
r.raise_for_status()  # lève une exception si statut >= 400

# Construire un nom de fichier traçable
host = urlparse(url).netloc.replace(".", "_")
run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
chemin = Path("data/raw") / f"{run_id}_{host}.html"
chemin.parent.mkdir(parents=True, exist_ok=True)

chemin.write_bytes(r.content)
print(f"Sauvegardé : {chemin} ({len(r.content)} octets, statut {r.status_code})")
```


Quelques détails importants :

- **`headers={"User-Agent": ...}`** : on s’identifie honnêtement.
- **`r.raise_for_status()`** : transforme une réponse 4xx/5xx en exception. Pratique pour ne pas continuer à parser une page d’erreur.
- **`datetime.now(timezone.utc)`** : horodatage **explicitement en UTC**, sans ambiguïté de fuseau. C’est essentiel quand plusieurs personnes ou machines collaborent.
- **`run_id`** : c’est ton identifiant d’exécution. Il sera réutilisé pour nommer le HTML brut, le log, les données traitées et le rapport produit par cette même collecte. On y reviendra dans les parties suivantes — pour l’instant, retiens juste l’idée.
- **`Path.write_bytes()`** : écriture brute, sans transformation.

> **Nuance sur `raise_for_status()`** : pour un script pédagogique, c’est très bien — ça t’évite de parser une page d’erreur. Mais dans un outil d’enquête avancé, une réponse `403`, `404` ou `500` est elle-même une information utile (la page existait avant, la cible bloque, le serveur est en panne). On garde alors la réponse + métadonnées (statut, headers) dans les logs, même si on ne parse pas le contenu. On y reviendra au chapitre 12.

### Gérer les erreurs réseau

```python
import requests

try:
    r = requests.get("https://exemple-introuvable.invalid", timeout=5)
    r.raise_for_status()
except requests.exceptions.Timeout:
    print("Le serveur n’a pas répondu à temps.")
except requests.exceptions.ConnectionError:
    print("Impossible de se connecter au serveur.")
except requests.exceptions.HTTPError as e:
    print(f"Erreur HTTP : {e.response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Erreur générique : {e}")
```


|Exception         |Cause                                                             |
|------------------|------------------------------------------------------------------|
|`Timeout`         |Le serveur ne répond pas dans le délai imparti.                   |
|`ConnectionError` |DNS, réseau, refus de connexion.                                  |
|`HTTPError`       |Statut 4xx ou 5xx (uniquement si `raise_for_status()` est appelé).|
|`RequestException`|Classe parente — tout le reste.                                   |


> **À retenir :** capturer `RequestException` en dernier filet de sécurité est une bonne pratique. Mais distinguer les cas (Timeout vs Connection vs HTTPError) permet des réactions plus fines.

## Très utile en pratique

### Le User-Agent identifiable

Sans header explicite, `requests` envoie un User-Agent type `python-requests/2.31.0`. C’est honnête, mais peu informatif.

Pour un outil OSINT, identifie-toi proprement :

```python
HEADERS = {
    "User-Agent": "MonOutilOSINT/0.1 (+contact: osint-projet@example.org)",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "fr,en;q=0.8",
}

r = requests.get(url, headers=HEADERS, timeout=10)
```


> **Rappel :** **pas** d’usurpation de navigateur (Chrome récent, etc.) pour contourner des filtres anti-bot. C’est un signal d’intention douteuse et ça nuit à la traçabilité de ton enquête.

### Vérifier et corriger l’encodage

```python
r = requests.get(url, timeout=10)

print(r.encoding)            # ce que requests a deviné
print(r.headers.get("Content-Type"))
# Souvent : 'text/html; charset=utf-8'

# Si l’encodage est mal détecté :
r.encoding = "utf-8"         # forcer
print(r.text[:200])          # maintenant correct
```


Symptôme classique d’encodage cassé : tu vois `Caf\xc3\xa9` au lieu de `Café`, ou `Ã©` au lieu de `é`. C’est presque toujours un problème UTF-8 mal interprété.

### Pattern de fonction `fetch` réutilisable

Un mini-module à garder sous la main :

```python
# src/fetch.py
import logging
import requests
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlparse

USER_AGENT = "MonOutilOSINT/0.1 (+contact: osint-projet@example.org)"
HEADERS = {"User-Agent": USER_AGENT, "Accept-Language": "fr,en;q=0.8"}

logger = logging.getLogger(__name__)


def fetch(url, session=None, raw_dir="data/raw", run_id=None, timeout=10):
    """Récupère une URL, sauvegarde le contenu brut, retourne (Response, chemin).

    - `session` : une `requests.Session` partagée (recommandé pour les collectes multi-pages).
      Si non fournie, une session jetable est créée pour cette requête.
    - `run_id` : identifiant d’exécution **partagé** entre toutes les requêtes d’une même
      collecte. Si non fourni, un nouveau `run_id` est calculé — à éviter pour les
      collectes multi-pages, où toutes les pages doivent partager le même `run_id`.

    Lève une exception en cas d’erreur HTTP ou réseau.
    """
    session = session or requests.Session()
    if run_id is None:
        run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    r = session.get(url, headers=HEADERS, timeout=timeout)
    r.raise_for_status()

    parsed = urlparse(url)
    host = parsed.netloc.replace(".", "_")
    path_safe = parsed.path.strip("/").replace("/", "_") or "index"
    out = Path(raw_dir) / f"{run_id}_{host}_{path_safe}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(r.content)

    logger.info("Fetched %s (%d bytes, status %d) -> %s",
                url, len(r.content), r.status_code, out)
    return r, out
```


Ce pattern (fetch + sauvegarde brute + retour structuré) est la **brique de base** de tous tes scrapers. Tu vas le réutiliser dans toute la partie II et III.

### Une seule requête, plusieurs analyses

Quand tu mets au point ton parser (chapitre 6), tu vas vouloir itérer **vite** sans retaper le serveur. La méthode :

1. Fais **une** requête, sauvegarde le HTML dans `data/raw/`.
1. Travaille sur le **fichier local** pour tester tous tes sélecteurs.
1. Relance une requête réelle uniquement quand tu veux des données fraîches.

C’est plus rapide pour toi, plus respectueux pour le serveur, et ça rend ton enquête reproductible.

## Bonus

### `requests.Session()` : préfiguration du chapitre 11

Si tu fais plusieurs requêtes vers le même site, une `Session` partage cookies et headers et réutilise la connexion sous-jacente :

```python
import requests

with requests.Session() as session:
    session.headers.update({"User-Agent": "MonOutil/0.1"})
    r1 = session.get("https://example.com/", timeout=10)
    r2 = session.get("https://example.com/about", timeout=10)
```


C’est plus efficace et c’est la bonne pratique dès qu’on dépasse une requête isolée. On y reviendra au chapitre 11 (bonnes pratiques pro).

### `verify=False` : à ne **pas** utiliser

Tu croiseras dans des tutos `requests.get(url, verify=False)` pour ignorer les erreurs de certificat SSL. **Ne fais jamais ça en production OSINT** : tu désactives un mécanisme de sécurité qui protège ta connexion contre les interceptions. Si un site a un vrai problème de certificat, c’est un signal qu’il faut interroger.

## ❌ Erreur classique

```python
# Oublier le timeout
r = requests.get(url)
# ❌ Si le serveur ne répond pas, ton script attend... indéfiniment.

r = requests.get(url, timeout=10)  # ✅

# Considérer un 200 comme un succès logique
r = requests.get(url, timeout=10)
if r.status_code == 200:
    parse(r.text)
# ❌ Certains sites renvoient 200 + page "ressource introuvable"
# → toujours vérifier aussi que le contenu correspond à ce qu’on attend.

# User-Agent qui se fait passer pour Chrome
HEADERS = {"User-Agent": "Mozilla/5.0 ... Chrome/120 ..."}
# ❌ Sauf cas pédagogique très balisé, c’est de l’usurpation.
# Le serveur peut légitimement traiter ton script comme un humain
# et tu pollues ses statistiques d’usage.

# Confondre .text et .content quand on sauvegarde
chemin.write_text(r.text)
# ❌ Tu sauvegardes une version déjà décodée. Si requests s’est trompé
# sur l’encodage, tu sauvegardes du texte cassé.

chemin.write_bytes(r.content)  # ✅ — préserve le brut

# Capturer Exception largement
try:
    r = requests.get(url, timeout=10)
except Exception:
    pass
# ❌ Tu masques tout, y compris les bugs de ton propre code.
# Capture les exceptions du module requests, pas tout.
```


## Exercices

**Guidé :**

1. Récupère la page d’accueil de `https://httpbin.org/`.
1. Affiche : statut, URL finale, encodage détecté, `Content-Type`, taille en octets, et 3 headers de réponse de ton choix.
1. Sauvegarde le contenu brut dans `data/raw/`.

**Autonome :** Écris un script `src/fetch_cli.py` qui :

1. Prend une URL en argument (`sys.argv[1]`).
1. Vérifie qu’elle commence par `http://` ou `https://`.
1. Fait la requête avec User-Agent identifiable et timeout.
1. Gère séparément `Timeout`, `ConnectionError`, `HTTPError`.
1. Sauvegarde le HTML dans `data/raw/<horodatage>_<host>.html`.
1. Affiche un résumé (statut, taille, durée de la requête, chemin du fichier).

Astuce : pour mesurer la durée, utilise `time.perf_counter()` autour de l’appel.

## ✅ Tu sais maintenant…

- Installer et utiliser `requests` pour faire une requête GET
- Lire l’objet `Response` (`status_code`, `text`, `content`, `headers`, etc.)
- Gérer les erreurs réseau avec `Timeout`, `ConnectionError`, `HTTPError`
- Imposer un timeout (toujours)
- Identifier honnêtement ton script via User-Agent
- Sauvegarder le contenu brut dans `data/raw/` de manière traçable
- Le réflexe : **fetch une fois, parse hors ligne**

-----
