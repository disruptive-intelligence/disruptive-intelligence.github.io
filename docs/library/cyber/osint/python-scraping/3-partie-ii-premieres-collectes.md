---
title: PARTIE II — PREMIÈRES COLLECTES
source: Cyber/02_OSINT/Python_Scraping.md
note: Python & scraping
chapter: 3
chapters: 7
---

> **Objectif de la partie :** récupérer **une** page web, en extraire ce qu’on veut, et le faire proprement. On reste sur une page à la fois. Toute la mécanique multi-pages, APIs, et passage à l’échelle viendra dans les parties suivantes.
> 
> **Pré-requis pour cette partie :** ta fiche d’enquête est remplie (cible identifiée, méthode justifiée, robots.txt vérifié). Si ce n’est pas le cas, retour au chapitre 4.

-----


## Chapitre 5 — Premières requêtes avec `requests`

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

### Le minimum à savoir

#### Installation rappel

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

#### La première requête

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

#### L’objet Response

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

#### `text` vs `content`

- `response.text` → la réponse **décodée** en chaîne de caractères, prête à manipuler.
- `response.content` → la réponse **brute** en bytes, telle qu’elle est arrivée sur le câble.

Quand utiliser quoi ?

|Cas                                                   |À utiliser|
|------------------------------------------------------|----------|
|Parser du HTML/JSON pour exploitation immédiate       |`.text`   |
|Sauvegarder fidèlement la page pour retraitement futur|`.content`|
|Télécharger une image, un PDF, un fichier binaire     |`.content`|


> **Bonne pratique OSINT :** quand tu sauvegardes une page brute dans `data/raw/`, écris `.content` en mode binaire (`"wb"`). C’est la **preuve** de ce que tu as reçu, indépendante de l’encodage.

#### Sauvegarder une page proprement

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

#### Gérer les erreurs réseau

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

### Très utile en pratique

#### Le User-Agent identifiable

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

#### Vérifier et corriger l’encodage

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

#### Pattern de fonction `fetch` réutilisable

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

#### Une seule requête, plusieurs analyses

Quand tu mets au point ton parser (chapitre 6), tu vas vouloir itérer **vite** sans retaper le serveur. La méthode :

1. Fais **une** requête, sauvegarde le HTML dans `data/raw/`.
1. Travaille sur le **fichier local** pour tester tous tes sélecteurs.
1. Relance une requête réelle uniquement quand tu veux des données fraîches.

C’est plus rapide pour toi, plus respectueux pour le serveur, et ça rend ton enquête reproductible.

### Bonus

#### `requests.Session()` : préfiguration du chapitre 11

Si tu fais plusieurs requêtes vers le même site, une `Session` partage cookies et headers et réutilise la connexion sous-jacente :

```python
import requests

with requests.Session() as session:
    session.headers.update({"User-Agent": "MonOutil/0.1"})
    r1 = session.get("https://example.com/", timeout=10)
    r2 = session.get("https://example.com/about", timeout=10)
```

C’est plus efficace et c’est la bonne pratique dès qu’on dépasse une requête isolée. On y reviendra au chapitre 11 (bonnes pratiques pro).

#### `verify=False` : à ne **pas** utiliser

Tu croiseras dans des tutos `requests.get(url, verify=False)` pour ignorer les erreurs de certificat SSL. **Ne fais jamais ça en production OSINT** : tu désactives un mécanisme de sécurité qui protège ta connexion contre les interceptions. Si un site a un vrai problème de certificat, c’est un signal qu’il faut interroger.

### ❌ Erreur classique

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

### Exercices

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

### ✅ Tu sais maintenant…

- Installer et utiliser `requests` pour faire une requête GET
- Lire l’objet `Response` (`status_code`, `text`, `content`, `headers`, etc.)
- Gérer les erreurs réseau avec `Timeout`, `ConnectionError`, `HTTPError`
- Imposer un timeout (toujours)
- Identifier honnêtement ton script via User-Agent
- Sauvegarder le contenu brut dans `data/raw/` de manière traçable
- Le réflexe : **fetch une fois, parse hors ligne**

-----


## Chapitre 6 — Parser du HTML avec BeautifulSoup

Tu as récupéré une page HTML. C’est une grosse soupe de balises. **BeautifulSoup** est la bibliothèque qui transforme cette soupe en arbre exploitable.

### Le minimum à savoir

#### Installation rappel

```bash
pip install beautifulsoup4 lxml
```

`beautifulsoup4` est la bibliothèque, `lxml` est le parser rapide qu’elle peut utiliser en interne.

#### Premier parsing

```python
from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <h1>Bonjour</h1>
    <p class="lead">Premier paragraphe.</p>
    <a href="https://exemple.fr">Lien</a>
  </body>
</html>
"""

soup = BeautifulSoup(html, "lxml")

print(soup.h1.get_text())            # "Bonjour"
print(soup.p.get_text())              # "Premier paragraphe."
print(soup.a.get("href"))             # "https://exemple.fr"
```

#### Choix du parser

|Parser         |Caractéristiques                                    |Quand                                       |
|---------------|----------------------------------------------------|--------------------------------------------|
|`"html.parser"`|Intégré à Python, pas d’installation supplémentaire.|Petits scripts, dépannage.                  |
|`"lxml"`       |Rapide, robuste, supporte du XML.                   |Recommandé pour tout projet sérieux.        |
|`"html5lib"`   |Très tolérant aux erreurs HTML.                     |Sites au HTML « cassé » qui posent problème.|

Tous donnent le même objet `soup` derrière. On utilisera `"lxml"` par défaut.

#### Charger depuis un fichier (ton flux de travail principal)

Souvenir du chapitre 5 : tu as sauvegardé une page dans `data/raw/`. Tu vas parser **ce fichier**, pas retaper le serveur.

```python
from bs4 import BeautifulSoup
from pathlib import Path

html_brut = Path("data/raw/20260517T140000Z_books_toscrape_com.html").read_bytes()
soup = BeautifulSoup(html_brut, "lxml")
```

Note : on passe `bytes`, BeautifulSoup gère l’encodage à partir des balises `<meta charset>` du HTML. C’est plus fiable que de décoder soi-même.

#### Naviguer dans l’arbre : `find` et `find_all`

```python
# Trouver le premier élément qui correspond
title = soup.find("h1")
print(title.get_text())

# Trouver TOUS les éléments qui correspondent
liens = soup.find_all("a")
print(f"{len(liens)} liens trouvés")
for lien in liens:
    print(lien.get("href"), "—", lien.get_text(strip=True))
```

Filtrage par classe, id, attribut :

```python
soup.find("article", class_="post")          # ⚠ class_ avec underscore (class est réservé en Python)
soup.find(id="article-123")
soup.find("a", attrs={"data-type": "ext"})
soup.find_all("p", class_="lead")
```

#### Naviguer avec les sélecteurs CSS : `select` et `select_one`

Souvent plus naturel quand on vient des DevTools, parce qu’on utilise la même syntaxe :

```python
soup.select_one("h1")                       # premier h1
soup.select("article p")                     # tous les p dans un article
soup.select(".post .lead")                   # paragraphes .lead dans un .post
soup.select_one("#article-123 > h1")         # h1 enfant direct
soup.select("a[href^='https']")              # liens commençant par https
```

**`find` vs `select` ?** Les deux marchent. Règles pratiques :

- `find/find_all` : plus pythonique, idéal pour des recherches simples par balise + classe + attribut.
- `select/select_one` : plus expressif, idéal quand le sélecteur est complexe ou quand tu l’as construit dans les DevTools.

Tu peux mélanger les deux dans le même script — choisis le plus lisible cas par cas.

#### Extraire le texte

```python
tag = soup.select_one("h1")

print(tag.get_text())                # texte avec espaces internes potentiels
print(tag.get_text(strip=True))      # texte nettoyé (recommandé)
print(tag.text)                      # raccourci de .get_text()
```

`strip=True` enlève les espaces et retours à la ligne en début/fin. C’est presque toujours ce que tu veux.

#### Extraire des attributs

```python
lien = soup.select_one("a")

# Méthode crochets : crash si l’attribut n’existe pas
href = lien["href"]                  # ❌ KeyError si pas de href

# Méthode .get() : retourne None si absent (plus sûr)
href = lien.get("href")              # ✅
href = lien.get("href", "")          # ✅ avec valeur par défaut
```

> **Bonne pratique :** utilise toujours `.get("attribut")` quand tu n’es pas absolument certain que l’attribut existe.

#### Itérer proprement

```python
# Extraire texte et URL de tous les liens d’une page
for lien in soup.find_all("a"):
    texte = lien.get_text(strip=True)
    url = lien.get("href")
    if texte and url:                # filtre les liens vides
        print(f"{texte} -> {url}")
```

### Très utile en pratique

#### La méthodologie : Inspect → Sélecteur → Test

Pour chaque champ que tu veux extraire :

```
1. Va sur la page dans ton navigateur.
2. Clic droit sur la donnée qui t’intéresse → Inspecter.
3. Note la balise, ses classes, sa hiérarchie.
4. Construis le sélecteur CSS le plus simple qui cible cette donnée
   sans en attraper d’autres.
5. Teste sur le HTML sauvegardé hors ligne.
6. Vérifie le résultat sur 3-4 items différents — pas juste le premier.
```

**Le test sur plusieurs items est crucial.** Un sélecteur qui marche sur le premier livre peut échouer sur le quatrième parce que la promo est sur une autre balise, ou parce que l’auteur manque.

#### Choisir un sélecteur robuste

Tous les sélecteurs ne se valent pas dans le temps :

|Sélecteur               |Robustesse                                            |
|------------------------|------------------------------------------------------|
|`#article-main h1`      |🟢 Très robuste (id stable, hiérarchie sémantique)     |
|`article > h1`          |🟢 Robuste (structure HTML5 stable)                    |
|`.titre-principal`      |🟡 Dépend des conventions du site                      |
|`.css-x7f3k2`           |🔴 Très fragile (classe générée, change à chaque build)|
|`div > div > div > span`|🔴 Très fragile (dépend de la structure exacte)        |

**Réflexe pro :** quand plusieurs sélecteurs sont possibles, prends celui qui repose sur la **sémantique** (`article`, `header`, `nav`, `time`, `data-*`) plutôt que sur la mise en page.

#### Workflow recommandé

```
┌─────────────────────────────────────────────────┐
│  src/fetch.py    →  télécharge + sauvegarde brut │
│                     dans data/raw/               │
└──────────────┬──────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────┐
│  src/parse.py    →  lit data/raw/ et applique    │
│                     les sélecteurs                │
│                     ITÈRE ICI                     │
└──────────────┬──────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────┐
│  Liste de dicts prête pour le stockage           │
│  (chapitre 8)                                    │
└─────────────────────────────────────────────────┘
```

Ce découpage te permet de modifier ton parser **autant de fois que nécessaire** sans toucher au serveur. C’est la différence entre un débutant qui spamme le site et un pro qui itère localement.

#### Nettoyer le texte extrait

Le HTML contient souvent des artefacts invisibles :

- Espaces multiples : `Bonjour    le    monde`.
- Espaces insécables : `\xa0` (s’affichent comme un espace, mais ne match pas `" "`).
- Retours à la ligne au milieu d’un texte.

Helper pratique :

```python
import re

def clean(text):
    if text is None:
        return ""
    # Remplace les espaces insécables et autres par des espaces normaux
    text = text.replace("\xa0", " ")
    # Compacte les espaces multiples
    text = re.sub(r"\s+", " ", text)
    return text.strip()
```

À utiliser sur **tout** texte qui vient d’une page web.

### Bonus

#### XPath (mention culturelle)

`lxml` (sans BeautifulSoup) permet d’utiliser **XPath**, un langage de sélection encore plus puissant que CSS pour des cas tordus :

```python
from lxml import html

tree = html.fromstring(r.content)
titres = tree.xpath("//article//h2/text()")
```

XPath excelle pour les sélections « relatives au texte » (« le `<td>` qui suit le `<td>` contenant ‘Total’ »). En pratique, les sélecteurs CSS de BeautifulSoup couvrent 95 % des cas. Garde XPath dans un coin de ta tête pour les 5 % restants.

#### Récupérer les microdonnées : `<script type="application/ld+json">`

Beaucoup de sites (médias, e-commerce) intègrent des métadonnées structurées en JSON-LD pour le SEO. C’est **un cadeau** pour un scraper :

```python
import json

scripts = soup.find_all("script", type="application/ld+json")
for s in scripts:
    try:
        data = json.loads(s.string)
        print(data.get("@type"), "-", data.get("headline", data.get("name")))
    except json.JSONDecodeError:
        continue
```

Quand le JSON-LD existe, **utilise-le en priorité** : il est explicitement publié pour la consommation programmatique, c’est plus stable et plus propre que de parser le HTML rendu.

### ❌ Erreur classique

```python
# Cibler par classe générée dynamiquement
titres = soup.select(".css-x7f3k2")
# ❌ Marchera une semaine. Préfère .article > h1 ou article header h1.

# Accéder à un attribut absent avec les crochets
href = lien["href"]
# ❌ KeyError sur un lien qui n’a pas de href (ex. <a name="ancre">)
href = lien.get("href")  # ✅

# Parser le serveur en boucle pendant qu’on développe
for i in range(10):
    r = requests.get(url, ...)
    soup = BeautifulSoup(r.text, "lxml")
    test_selecteur(soup)
# ❌ Tu martèles le serveur sans raison.
# ✅ Sauvegarde une fois, itère sur le fichier local.

# Confondre la présence visuelle et la présence dans le HTML brut
# Tu vois la donnée à l’écran mais ton scraper ne la trouve pas.
# → C’est probablement chargé en JavaScript après le HTML initial.
# Vérifie : Ctrl+U dans le navigateur, cherche la donnée dans le source brut.

# Ne tester son sélecteur que sur le premier item
livres = soup.select(".product")[:1]  # ⚠ marche, mais tu n’as pas testé la robustesse
# ✅ Toujours boucler sur 3-5 items différents avant de considérer le scraper "fini".
```

### Exercices

**Guidé :** Sur le HTML de `https://quotes.toscrape.com` (sauvegardé localement) :

1. Charge le fichier dans `BeautifulSoup`.
1. Trouve toutes les citations affichées sur la page (ce sont les `<div class="quote">`).
1. Pour chaque citation, extrais et affiche le texte de la citation seul (sélecteur `.text`).

**Autonome :** Sur le même HTML :

1. Pour chaque citation, extrais aussi : l’auteur, et la liste des tags.
1. Affiche le tout sous forme propre : `« texte » — auteur (tags)`.
1. Vérifie que ton script trouve bien **10 citations** sur la page (c’est le nombre attendu).

### ✅ Tu sais maintenant…

- Charger une page HTML dans `BeautifulSoup` (avec parser `lxml`)
- Naviguer dans l’arbre avec `find` / `find_all` ou `select` / `select_one`
- Choisir un sélecteur **robuste** (sémantique > classe générée)
- Extraire texte avec `.get_text(strip=True)` et attributs avec `.get("attr")`
- Le workflow : fetch une fois → parser hors ligne → itérer librement
- Nettoyer le texte (espaces insécables, espaces multiples)
- Repérer et exploiter le JSON-LD quand il existe

-----


## Chapitre 7 — Extraction structurée d’une page

Récupérer du texte, c’est bien. Construire une **structure** exploitable, c’est mieux. Ce chapitre te fait passer du « j’ai sorti des trucs de la page » au « j’ai produit un dataset propre, traçable et prêt à stocker ».

### Le minimum à savoir

#### Le modèle « un item = un dict »

L’unité de base d’une collecte structurée, c’est l’**enregistrement** : un dictionnaire qui regroupe tous les champs d’un item, plus les **métadonnées de collecte**.

```python
{
    "texte": "La vie, c'est ce qui t'arrive pendant que tu fais d’autres plans.",
    "auteur": "John Lennon",
    "tags": ["change", "deep-thoughts", "thinking", "world"],
    "source_url": "https://quotes.toscrape.com/page/1/",
    "collected_at": "2026-05-17T14:32:11Z",
    "tool": "mon-collecteur/0.1"
}
```

Quatre catégories de champs :

1. **Données du domaine** (`texte`, `auteur`, `tags`) — ce qui t’intéresse.
1. **Source** (`source_url`) — d’où vient la donnée.
1. **Temporalité** (`collected_at`) — quand tu l’as collectée.
1. **Outil** (`tool`) — avec quoi.

Les trois dernières sont **obligatoires**. Sans elles, ton enregistrement n’a aucune valeur d’enquête (rappel chapitre 2 : traçabilité).

#### Le pattern de boucle d’extraction

```python
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from pathlib import Path

URL_SOURCE = "https://quotes.toscrape.com/"
TOOL = "mon-collecteur/0.1"

html = Path("data/raw/quotes_page1.html").read_bytes()
soup = BeautifulSoup(html, "lxml")

resultats = []
collected_at = datetime.now(timezone.utc).isoformat()

for bloc in soup.select(".quote"):
    enregistrement = {
        "texte": bloc.select_one(".text").get_text(strip=True),
        "auteur": bloc.select_one(".author").get_text(strip=True),
        "tags": [t.get_text(strip=True) for t in bloc.select(".tag")],
        "source_url": URL_SOURCE,
        "collected_at": collected_at,
        "tool": TOOL,
    }
    resultats.append(enregistrement)

print(f"{len(resultats)} citations extraites")
```

Trois principes que ce pattern illustre :

1. **Boucle par bloc parent** (`.quote`) — chaque bloc devient un enregistrement.
1. **Sélection relative au bloc** (`bloc.select_one(...)`) — pas de risque de mélanger les items.
1. **Ajout systématique des métadonnées** — à chaque itération.

#### Gérer les champs manquants

Si un site est cohérent, tous les blocs ont tous les champs. Dans la vraie vie, c’est l’exception. Voici comment se protéger :

```python
def safe_text(elt, selecteur, default=""):
    """Renvoie le texte d’un sous-élément, ou default si absent."""
    cible = elt.select_one(selecteur)
    return cible.get_text(strip=True) if cible else default


def safe_attr(elt, selecteur, attr, default=""):
    """Renvoie un attribut d’un sous-élément, ou default si absent."""
    cible = elt.select_one(selecteur)
    return cible.get(attr, default) if cible else default
```

Et dans la boucle :

```python
for bloc in soup.select(".article"):
    enregistrement = {
        "titre": safe_text(bloc, "h2"),
        "date": safe_attr(bloc, "time", "datetime"),
        "auteur": safe_text(bloc, ".byline .author", default="(inconnu)"),
        "resume": safe_text(bloc, ".excerpt"),
        ...
    }
```

> **À retenir :** un parser robuste produit toujours une sortie. Il ne plante pas sur un champ manquant — il enregistre la valeur manquante (`""`, `None`, `"(inconnu)"`) pour qu’on puisse la repérer en aval.

#### Extraire des liens (cas typique)

```python
from urllib.parse import urljoin

def extraire_liens(soup, url_de_base):
    """Liste tous les liens d’une page en URLs absolues."""
    liens = []
    for a in soup.find_all("a"):
        href = a.get("href")
        if not href:
            continue
        if href.startswith(("javascript:", "mailto:", "tel:", "#")):
            continue
        # Reconstruire l’URL absolue depuis une éventuelle URL relative
        url_complete = urljoin(url_de_base, href)
        liens.append({
            "texte": a.get_text(strip=True),
            "url": url_complete,
        })
    return liens
```

Trois points importants :

- **Filtrer les liens non navigables** (`javascript:`, `mailto:`, ancres `#`).
- **`urljoin`** convertit une URL relative (`/article/123`) en absolue à partir de l’URL de la page.
- **Garder le texte du lien** : c’est souvent une métadonnée précieuse.

#### Extraire un tableau HTML

```python
def extraire_tableau(soup, selecteur="table"):
    """Extrait un tableau HTML en liste de dicts (premier <tr> = entêtes)."""
    table = soup.select_one(selecteur)
    if table is None:
        return []

    lignes = table.find_all("tr")
    if not lignes:
        return []

    entetes = [th.get_text(strip=True) for th in lignes[0].find_all(["th", "td"])]
    donnees = []
    for ligne in lignes[1:]:
        cellules = [td.get_text(strip=True) for td in ligne.find_all(["th", "td"])]
        if len(cellules) == len(entetes):
            donnees.append(dict(zip(entetes, cellules)))
    return donnees
```

Pour Wikipedia et autres sites riches en tableaux, ce pattern résout 90 % des besoins.

### Très utile en pratique

#### Normaliser au moment de l’extraction

Plutôt que de stocker des données « sales » et nettoyer plus tard, profite de la boucle d’extraction pour nettoyer en passant. Quelques règles :

|Champ                          |Normalisation suggérée                                                                              |
|-------------------------------|----------------------------------------------------------------------------------------------------|
|Texte libre                    |`strip()`, suppression des espaces insécables, espaces multiples compactés.                         |
|URL                            |Conversion en absolu (`urljoin`).                                                                   |
|Date affichée (« 12 mai 2026 »)|Conserver telle quelle dans un champ `date_affichee`. Tenter le parsing dans `date_iso` si possible.|
|Liste de tags                  |Trim chaque tag, ne pas inclure les vides.                                                          |
|Nombres affichés (`"1 234 €"`) |Conserver le brut **et** une version numérique séparée.                                             |


> **Bonne pratique :** quand la valeur n’est pas évidente à parser (date locale, nombre formaté), garde **les deux** versions : le brut tel qu’extrait, et la version normalisée. Si la normalisation se trompe, tu peux corriger sans recollecter.

#### Le cas particulier de l’extraction d’emails

Extraire des emails depuis une page est techniquement trivial avec une regex :

```python
import re

emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", soup.get_text())
```

**Mais c’est précisément un cas où il faut s’imposer un cadre strict.** Tu peux légitimement vouloir extraire :

- des **contacts institutionnels** (`contact@`, `presse@`, `info@`) sur une page de mentions légales ou « nous joindre »,
- des **adresses de responsables identifiés** (auteur d’une publication scientifique, responsable de communication désigné publiquement).

Tu ne dois **pas** :

- moissonner massivement les emails d’un site pour constituer une liste de prospection,
- collecter des emails personnels qui ne sont pas explicitement publiés dans un cadre professionnel,
- agréger des emails de différentes sources pour profiler des personnes,
- vendre, partager ou exporter des listes d’emails collectés.

> **Rappel RGPD :** une adresse email est une donnée personnelle. Sa collecte automatisée tombe sous le RGPD dès qu’il s’agit d’une personne physique. Pour un usage défensif sérieux, limite-toi aux contacts professionnels explicitement publiés à des fins de contact, et applique la minimisation.

Si le cadre est solide, un helper raisonnable :

```python
import re

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

def extraire_contacts_institutionnels(soup):
    """Extrait les emails qui ressemblent à des contacts institutionnels."""
    prefixes_inst = ("contact", "info", "presse", "press", "media",
                     "communication", "support", "rh", "hr")
    texte = soup.get_text(" ", strip=True)
    emails = set(EMAIL_RE.findall(texte))
    institutionnels = {e for e in emails
                       if e.split("@")[0].lower().startswith(prefixes_inst)}
    return sorted(institutionnels)
```

Note bien que cet helper **filtre** vers des préfixes manifestement institutionnels. Il ne ramasse pas tout.

#### Toujours conserver l’URL source

Dans chaque enregistrement, le champ `source_url` permet à toi et à un tiers de :

- vérifier la donnée en l’ouvrant dans un navigateur,
- relancer une collecte sur cette page seule,
- savoir si une donnée vient de la home page, d’un article, d’une catégorie.

C’est **non négociable**.

#### Quand le sélecteur change selon la position

Sur certaines pages, le premier item a une structure légèrement différente des autres (parce qu’il est mis en avant). Deux approches :

```python
# Option 1 : filtrer le premier item (souvent en plus dans la liste générale)
items = soup.select(".article")[1:]  # ignore le mis-en-avant

# Option 2 : extraire séparément
mis_en_avant = soup.select_one(".featured-article")
items = soup.select(".article-list .article")
```

À choisir selon ce que tu veux conserver dans ton dataset.

### Bonus

#### Les microdonnées JSON-LD, encore (mais en pratique)

Si un site fournit du JSON-LD, ton extraction devient quasi triviale :

```python
import json

ld_scripts = soup.find_all("script", type="application/ld+json")

articles = []
for script in ld_scripts:
    try:
        data = json.loads(script.string)
    except (json.JSONDecodeError, TypeError):
        continue

    # JSON-LD peut être un objet, une liste, ou un @graph
    items = data if isinstance(data, list) else [data]
    for item in items:
        if item.get("@type") in ("NewsArticle", "Article", "BlogPosting"):
            articles.append({
                "titre": item.get("headline"),
                "auteur": (item.get("author") or {}).get("name"),
                "date_publication": item.get("datePublished"),
                "url": item.get("url") or item.get("mainEntityOfPage"),
            })
```

Quand c’est disponible, c’est **le** bon chemin. Vérifie systématiquement avant d’aller scraper le HTML rendu.

#### `<time datetime="...">` pour les dates machines

Les bons sites utilisent la balise `<time>` avec un attribut `datetime` au format ISO 8601 :

```html
<time datetime="2026-05-17T10:00:00Z">17 mai 2026</time>
```

Tu peux extraire :

- la version humaine : `time.get_text(strip=True)` → `"17 mai 2026"`
- la version machine : `time.get("datetime")` → `"2026-05-17T10:00:00Z"`

Toujours préférer la version machine pour le stockage et le tri.

### ❌ Erreur classique

```python
# Boucle qui plante sur le 4e item
for bloc in soup.select(".article"):
    enr = {
        "auteur": bloc.select_one(".author").get_text(strip=True),
        # ❌ Si l’item 4 n’a pas .author, AttributeError sur None
    }
# ✅ Utiliser safe_text() ou tester explicitement
for bloc in soup.select(".article"):
    auteur_elt = bloc.select_one(".author")
    enr = {
        "auteur": auteur_elt.get_text(strip=True) if auteur_elt else "",
    }

# Oublier de convertir les URLs relatives
for a in soup.find_all("a"):
    liens.append(a.get("href"))
    # ❌ Tu obtiens "/article/123" — inutilisable hors contexte.
# ✅ Reconstruire en absolu :
for a in soup.find_all("a"):
    href = a.get("href")
    if href:
        liens.append(urljoin(url_source, href))

# Confondre date affichée et date machine
date = bloc.select_one("time").get_text(strip=True)  # "il y a 3 jours"
# ❌ Impossible à comparer, à trier.
# ✅ Utiliser l’attribut datetime :
date = bloc.select_one("time").get("datetime")  # "2026-05-14T10:00:00Z"

# Oublier les métadonnées de collecte
enregistrement = {"titre": "...", "auteur": "..."}
# ❌ Pas de source_url, pas de collected_at, pas de tool
#    → l’enregistrement n’est pas traçable, donc inexploitable
#    pour une enquête sérieuse.

# Stocker les caractères "sales" tels quels
enr["texte"] = bloc.get_text()  # Contient des \xa0, retours à la ligne en boucle
# ✅ Passer par clean(...) avant de stocker.
```

### Exercices

**Guidé :** Sur le HTML de `https://books.toscrape.com/` (sauvegardé) :

1. Identifie le bloc parent qui correspond à un livre (regarde dans les DevTools).
1. Écris une boucle d’extraction qui produit une liste de dicts avec : `titre`, `prix`, `disponibilite`, `note_etoiles` (en nombre, 1-5), `source_url`, `collected_at`, `tool`.
1. Affiche les 5 premiers enregistrements.
1. Vérifie qu’il y a bien 20 livres sur la première page.

**Autonome :** Sur une page Wikipedia choisie qui contient au moins un tableau :

1. Identifie le tableau qui t’intéresse (par sa légende ou son titre proche).
1. Extrais-le en liste de dicts avec la fonction `extraire_tableau()` du chapitre.
1. Nettoie les cellules : suppression des références `[1]`, `[2]`, espaces insécables, espaces multiples.
1. Affiche le résultat sous forme de tableau lisible.
1. Joins à chaque ligne les métadonnées `source_url` et `collected_at`.

### 🧩 Mini-projet de Partie II — *Collecteur de citations*

**Objectif :** construire ton premier vrai script d’extraction structurée, de bout en bout.

**Cible :** `https://quotes.toscrape.com/` (site **fait** pour l’apprentissage, sans cadre légal limitant).

**Cahier des charges :**

1. **Configuration** dans `config/config.json` :
- `url_source` : l’URL de la page.
- `user_agent` : ton User-Agent identifiable.
- `output_dir` : dossier de sortie (par défaut `data/raw/`).
1. **Fetch** (`src/fetch.py`) :
- Récupère la page.
- Sauvegarde le HTML brut dans `data/raw/<horodatage>_quotes.html`.
- Gère les erreurs réseau.
1. **Parse** (`src/parse.py`) :
- Charge le HTML sauvegardé.
- Pour chaque citation, produit un dict avec : `texte`, `auteur`, `tags`, `source_url`, `collected_at`, `tool`.
- Utilise les helpers `safe_text()` et `clean()`.
1. **Orchestration** (`src/main.py`) :
- Lit la config.
- Appelle fetch puis parse.
- Affiche un résumé : nombre de citations extraites, premier et dernier auteur, durée totale.
1. **Fiche d’enquête** : remplis ta fiche `config/fiche-enquete.md` pour ce projet (oui, même pour un site bac à sable — l’habitude se prend là).

Note : on ne stocke pas encore le résultat en CSV/JSON — c’est le chapitre 8.

> **Rappel `.gitignore` :** si tu versionnes ce projet sur Git, **ne versionne pas** `data/raw/` ni `data/processed/`. Garde uniquement le code (`src/`), la **configuration d’exemple** (sans secrets), et la documentation (`README.md`, fiche d’enquête vierge). Les collectes sont reproductibles à partir du code ; pas besoin de les pousser, et ça peut contenir des informations qu’on ne veut pas exposer publiquement.

### ✅ Tu sais maintenant…

- Construire un enregistrement complet (données + source + horodatage + outil)
- Boucler par bloc parent pour produire une liste structurée
- Gérer les champs manquants avec `safe_text()` / `safe_attr()`
- Extraire et normaliser des liens en URLs absolues
- Extraire un tableau HTML en liste de dicts
- Encadrer strictement l’extraction d’emails (contacts institutionnels uniquement)
- Exploiter le JSON-LD et les balises `<time>` quand ils existent
- Le réflexe : **toujours** conserver `source_url`, `collected_at`, `tool`

-----

> **🎯 Tu as terminé la Partie II.**
> 
> Tu sais maintenant récupérer une page, la parser, et en sortir un dataset structuré en mémoire. Mais en mémoire, ça ne suffit pas — il faut le stocker, le nettoyer, le dédupliquer pour qu’il soit exploitable.
> 
> La Partie III s’occupe de ça : CSV / JSON / JSONL, organisation des dossiers, normalisation, déduplication.

-----
