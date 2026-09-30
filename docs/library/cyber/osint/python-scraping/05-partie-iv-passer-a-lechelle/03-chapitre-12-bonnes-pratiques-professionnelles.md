---
title: Chapitre 12 — Bonnes pratiques professionnelles
source: Cyber/02_OSINT/Python_Scraping.md
note: Python & scraping
up:
- - Python & scraping
  - ../index.md
- - Partie IV — Passer à L’échelle
  - index.md
---

Tu sais collecter, parser, stocker, paginer, interroger des APIs. Ce chapitre rassemble les **outils qui transforment un script qui marche en outil qui dure**. Pas de nouveau concept de collecte ici — uniquement de la robustesse, de la lisibilité, et de la maintenance.

## Le minimum à savoir

### `requests.Session()` : la base

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

### Retries avec backoff exponentiel

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

### Le module `logging` : la base professionnelle

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

### Configuration externe

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

### Séparation code / données / config / secrets

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


### Reproductibilité

Pour qu’une enquête soit reproductible, conserve :

1. **`requirements.txt`** figé (`pip freeze > requirements.txt`).
1. **Version Python** documentée dans le README (`Python 3.12+`).
1. **`run_id` partagé** entre tous les artefacts d’une exécution.
1. **Fiche d’enquête** complète, archivée dans `reports/`.
1. **Le code lui-même versionné** (Git), avec une **release** ou un **commit** identifiable cité dans le rapport.

> **À retenir :** une enquête OSINT non reproductible n’a pas de valeur d’enquête. Un collègue (ou toi-même dans six mois) doit pouvoir refaire la collecte et arriver au même résultat.

### Documentation : le README minimum vital

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


## Très utile en pratique

### Pattern de `main.py` complet

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

### OPSEC : rappel final

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

### Tests basiques (bonus)

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

## Bonus

### `requests-cache` pour le développement

Évite de retélécharger la même page pendant que tu mets au point ton parser :

```python
import requests_cache
session = requests_cache.CachedSession("dev_cache", expire_after=3600)
```


**À désactiver en production** — tu veux des données fraîches.

### Niveau `logging` configurable

```python
# Permettre -v pour DEBUG, -vv pour tout, sinon INFO
def log_level(verbose):
    return [logging.WARNING, logging.INFO, logging.DEBUG][min(verbose, 2)]
```


```python
logging.basicConfig(level=log_level(args.verbose), ...)
```


## ❌ Erreur classique

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


## Exercices

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

## 🧩 Mini-projet de Partie IV (2/2) — *Collecteur d’articles publics*

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

## ✅ Tu sais maintenant…

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
