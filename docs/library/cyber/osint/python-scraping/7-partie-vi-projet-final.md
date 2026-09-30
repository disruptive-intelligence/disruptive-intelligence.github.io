---
title: PARTIE VI — PROJET FINAL
source: Cyber/02_OSINT/Python_Scraping.md
note: Python & scraping
chapter: 7
chapters: 7
---

> **Objectif de la partie :** assembler **toutes les briques** des parties précédentes dans un véritable petit outil OSINT défensif. Tu vas livrer un projet présentable, reproductible, documenté, et conforme à tout ce qu’on a vu.
> 
> À la fin, tu auras un outil que tu peux montrer en portfolio, réutiliser dans une mission, ou faire évoluer pour un cas réel.

-----


## Chapitre 15 — Outil OSINT de collecte web défensive

### Présentation

Tu vas construire **`osint-web-collector`** : un collecteur web qui, à partir d’une liste d’URLs publiques, produit un inventaire structuré (liens, titres, métadonnées visibles), avec stockage, logs, et rapport.

Ce n’est pas un défi technique — toutes les briques ont déjà été vues. C’est un **exercice d’intégration** : prendre des modules cohérents, les faire dialoguer, les documenter, et livrer un tout présentable.

#### Ce que le projet doit faire

```
                     ┌────────────────────┐
config/targets.txt   │                    │   data/raw/<run_id>_*.html
       ──────────►   │                    │   ──────────────────────►
                     │                    │
config/config.yaml   │   osint-web-       │   data/processed/<run_id>.csv
       ──────────►   │   collector        │   data/processed/<run_id>.json
                     │                    │   ──────────────────────►
.env (secrets)       │                    │
       ──────────►   │                    │   reports/<run_id>.md
                     │                    │   logs/<run_id>.log
                     └────────────────────┘   ──────────────────────►
```

#### Ce que le projet ne doit **pas** faire

- Contourner un anti-bot.
- S’authentifier sur des services qui ne sont pas les tiens.
- Collecter massivement des données personnelles.
- Marteler une cible (toujours plafonner et espacer).
- Imiter un service de monitoring payant.

Ces interdits sont rappelés dans le README du projet, pas en ornement, mais comme **contrat de fonctionnement**.

### Cahier des charges

#### Entrée

1. **`config/targets.txt`** : une URL publique par ligne. Commentaires possibles avec `#`.
   
   ```
   # Liste des cibles
   https://books.toscrape.com/
   https://quotes.toscrape.com/
   ```
1. **`config/config.yaml`** : paramètres globaux.
   
   ```yaml
   user_agent: "osint-web-collector/1.0 (+contact: osint-projet@example.org)"
   timeout: 10
   delay: 1.5
   max_pages_per_target: 5      # pour cible avec pagination
   max_items_total: 2000
   raw_dir: data/raw
   processed_dir: data/processed
   log_dir: logs
   report_dir: reports
   ```
1. **`.env`** (optionnel, pour les éventuelles APIs) : secrets, jamais versionné.

#### Traitement (par URL)

Pour chaque URL de `targets.txt` :

1. **Vérification préalable** : récupérer et logger le `robots.txt` du domaine. Respecter `Crawl-delay` s’il est défini (override le `delay` config s’il est plus strict).
1. **Fetch propre** : User-Agent identifiable, timeout, retries, sauvegarde brute dans `data/raw/<run_id>_<host>_<path>.html`.
1. **Extraction** : liens (avec URLs canoniques), titres (`<title>`, `<h1>`, `<h2>`), métadonnées visibles (`<meta name=...>`, JSON-LD si présent), date détectée (`<time datetime=...>` ou `<meta property="article:published_time">`).
1. **Normalisation** : `clean_text` + `canonical_url`, déduplication par `item_id` (hash sur champs métier).
1. **Robustesse** : un site qui répond `5xx` ou qui timeout **ne fait pas planter** la collecte ; l’erreur est loguée, on passe à la cible suivante.

#### Sortie

Tous les artefacts d’une exécution partagent le **même `run_id`** (UTC, ISO compact, ex. `20260520T143012Z`).

|Artefact            |Chemin                                |Contenu                                                                |
|--------------------|--------------------------------------|-----------------------------------------------------------------------|
|HTML brut           |`data/raw/<run_id>_<host>_<path>.html`|Tel que reçu, intouché.                                                |
|Inventaire des liens|`data/processed/<run_id>_links.csv`   |Une ligne = un lien (URL canonique, texte, page source, domaine).      |
|Inventaire par URL  |`data/processed/<run_id>_pages.json`  |Une entrée = une URL cible, avec ses métadonnées.                      |
|Journal d’exécution |`logs/<run_id>.log`                   |Logs structurés (INFO/WARNING/ERROR).                                  |
|Rapport             |`reports/<run_id>.md`                 |Markdown avec front matter, résumé, top-N, anomalies, reproductibilité.|

### Architecture

#### Arborescence

```
osint-web-collector/
├── src/
│   ├── __init__.py
│   ├── config.py           # chargement config.yaml + .env
│   ├── robots.py           # lecture et interprétation robots.txt
│   ├── fetch.py            # session, retries, sauvegarde brute
│   ├── parse.py            # extraction liens / titres / méta / dates
│   ├── clean.py            # clean_text, canonical_url, déduplication
│   ├── store.py            # CSV / JSON / JSONL
│   ├── report.py           # rapport Markdown
│   └── main.py             # orchestration + CLI
├── config/
│   ├── config.yaml
│   ├── targets.txt
│   └── fiche-enquete.md    # gabarit
├── data/
│   ├── raw/                # .gitkeep, contenu non versionné
│   └── processed/          # .gitkeep, contenu non versionné
├── logs/                   # .gitkeep
├── reports/                # .gitkeep
├── tests/
│   ├── test_clean.py
│   └── test_parse.py
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE                  # MIT ou autre, selon ton choix
```

#### Responsabilités des modules

|Module     |Rôle                                                                                   |S’appuie sur                    |
|-----------|---------------------------------------------------------------------------------------|--------------------------------|
|`config.py`|Charger `config.yaml`, lire `.env`, créer les dossiers.                                |`yaml`, `dotenv`, `pathlib`     |
|`robots.py`|Lire `robots.txt`, déterminer si une URL est autorisée et quel `Crawl-delay` appliquer.|`urllib.robotparser`, `requests`|
|`fetch.py` |Session HTTP partagée, `Retry`, User-Agent, timeout, sauvegarde brute.                 |`requests`, `urllib3`           |
|`parse.py` |Extraire liens, titres, métadonnées, dates.                                            |`bs4`, `urllib.parse`           |
|`clean.py` |Nettoyer texte, canoniser URLs, calculer `item_id`, dédupliquer.                       |`unicodedata`, `re`, `hashlib`  |
|`store.py` |Écrire CSV et JSON avec métadonnées globales.                                          |`csv`, `json`                   |
|`report.py`|Générer le rapport Markdown.                                                           |`collections.Counter`           |
|`main.py`  |Lire la config, parcourir les cibles, orchestrer, écrire la sortie, générer le rapport.|Tous les modules ci-dessus      |

#### Squelette de `main.py`

```python
# src/main.py
import sys
import argparse
import logging
from datetime import datetime, timezone
from pathlib import Path

from src.config import load_config, setup_dirs
from src.robots import RobotsCache
from src.fetch import make_session, fetch
from src.parse import extract_page
from src.clean import clean_page, dedup_links
from src.store import write_links_csv, write_pages_json
from src.report import generate_report


def parse_args():
    p = argparse.ArgumentParser(description="osint-web-collector")
    p.add_argument("--config", default="config/config.yaml")
    p.add_argument("--targets", default="config/targets.txt")
    p.add_argument("-v", "--verbose", action="store_true")
    return p.parse_args()


def setup_logging(run_id, log_dir, verbose=False):
    log_file = Path(log_dir) / f"{run_id}.log"
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[logging.FileHandler(log_file, encoding="utf-8"),
                  logging.StreamHandler()],
    )
    return logging.getLogger("collector")


def main():
    args = parse_args()
    config = load_config(args.config)
    setup_dirs(config)

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    logger = setup_logging(run_id, config["log_dir"], args.verbose)
    logger.info("Démarrage run_id=%s", run_id)

    # Charger les cibles
    targets = [line.strip() for line in Path(args.targets).read_text(encoding="utf-8").splitlines()
               if line.strip() and not line.strip().startswith("#")]
    logger.info("%d cibles à collecter", len(targets))

    session = make_session(config["user_agent"])
    robots = RobotsCache(session)

    pages = []
    all_links = []

    for i, url in enumerate(targets, 1):
        logger.info("[%d/%d] %s", i, len(targets), url)

        if not robots.is_allowed(url, config["user_agent"]):
            logger.warning("  → bloqué par robots.txt, ignoré")
            continue

        delay = max(config["delay"], robots.crawl_delay(url))

        try:
            r, raw_path = fetch(url, session=session,
                                raw_dir=config["raw_dir"], run_id=run_id,
                                timeout=config["timeout"])
            page = extract_page(r.content, source_url=url)
            page = clean_page(page)
            page["raw_file"] = str(raw_path)
            page["status_code"] = r.status_code
            page["run_id"] = run_id
            page["tool"] = "osint-web-collector/1.0"
            pages.append(page)
            all_links.extend(page["links"])
        except Exception as e:
            logger.error("  → erreur : %s", e)
            pages.append({
                "source_url": url, "error": str(e),
                "run_id": run_id, "tool": "osint-web-collector/1.0",
            })

        # Politesse
        robots.sleep_after(url, base=delay)

    # Dédup et écriture
    all_links = dedup_links(all_links)

    csv_path = Path(config["processed_dir"]) / f"{run_id}_links.csv"
    json_path = Path(config["processed_dir"]) / f"{run_id}_pages.json"
    report_path = Path(config["report_dir"]) / f"{run_id}.md"

    write_links_csv(all_links, csv_path)
    write_pages_json(pages, json_path, run_id=run_id,
                     tool="osint-web-collector/1.0")
    generate_report(pages, all_links, report_path, run_id=run_id)

    logger.info("Sortie CSV    : %s", csv_path)
    logger.info("Sortie JSON   : %s", json_path)
    logger.info("Rapport       : %s", report_path)
    logger.info("Fin run_id=%s : %d pages, %d liens uniques",
                run_id, len(pages), len(all_links))


if __name__ == "__main__":
    sys.exit(main() or 0)
```

Note : `robots.py` et le détail des autres modules sont **à toi à implémenter**. Toutes les briques techniques sont dans les chapitres 5 à 14.

### Étapes proposées

Une progression réaliste, à faire dans l’ordre :

1. **Initialiser le squelette** (chapitre 0 + chapitre 12) : arborescence, venv, `requirements.txt`, `.gitignore`, `README.md` initial.
1. **`config.py`** : charger `config.yaml`, lire `.env`, créer les dossiers manquants.
1. **`robots.py`** : utiliser `urllib.robotparser` pour vérifier l’autorisation par URL et lire le `Crawl-delay`.
1. **`fetch.py`** : `make_session()` avec `Retry`, `fetch()` qui accepte `session` et `run_id` (chapitre 12).
1. **`parse.py`** : `extract_page(html_bytes, source_url)` qui renvoie `{title, h1, h2, meta, links, published_at, source_url}`.
1. **`clean.py`** : `clean_page` (texte + canonisation des URLs), `dedup_links` (par URL canonique).
1. **`store.py`** : CSV + JSON avec métadonnées globales.
1. **`report.py`** : rapport Markdown complet (chapitre 14).
1. **`main.py`** : orchestration, logs, gestion d’erreurs.
1. **Tests** sur 2-3 cibles éthiques (sites bac à sable).
1. **README** complet, `.env.example`, `LICENSE`.
1. **Revue personnelle** avec la checklist ci-dessous.

### Checklist de revue personnelle

Avant de considérer le projet « livré », vérifie chaque case :

#### Technique

- ☑ Le script tombe **proprement** si une cible est inaccessible (pas de plantage global).
- ☑ Toutes les requêtes ont un `timeout`.
- ☑ Toutes les requêtes utilisent une `Session` partagée avec `Retry`.
- ☑ Le User-Agent est identifiable et identique à `config.yaml`.
- ☑ Le `Crawl-delay` de `robots.txt` est respecté quand il est plus strict que `delay`.
- ☑ Un plafond explicite limite le volume total collecté.
- ☑ Les sorties dans `data/processed/` sont reproductibles à partir des `data/raw/`.

#### Traçabilité

- ☑ Un seul `run_id` partagé entre HTML brut, CSV, JSON, log et rapport.
- ☑ Chaque enregistrement contient `source_url`, `collected_at`, `tool`, `run_id`.
- ☑ Le rapport contient son front matter complet.
- ☑ Le rapport cite les chemins exacts des datasets et logs.

#### Documentation

- ☑ `README.md` complet (objectif, installation, usage, limites, cadre éthique, contact).
- ☑ `.env.example` documente les secrets attendus.
- ☑ Fiche d’enquête remplie pour l’exécution de référence.
- ☑ La commande de reproduction est dans le README **et** dans le rapport.

#### Sécurité / éthique

- ☑ Aucune clé API ou secret dans le code (vérifier avec `git log -p` ou `git secrets`).
- ☑ `data/raw/`, `data/processed/`, `logs/`, `.env` sont dans `.gitignore`.
- ☑ Le projet n’imite pas un service commercial protégé.
- ☑ Les cibles d’exemple sont éthiques (bac à sable ou cibles autorisées explicitement).
- ☑ Aucune donnée personnelle inutile dans les datasets ou le rapport.

#### Robustesse

- ☑ Le script tourne deux fois de suite sans rien casser.
- ☑ Une cible qui renvoie `404` n’interrompt pas la collecte.
- ☑ Une cible qui timeout n’interrompt pas la collecte.
- ☑ Un `429` est respecté (attente + retry contrôlé).

### Livrables attendus

1. **Le dépôt** (Git fortement recommandé) avec arborescence standard et toutes les cases ci-dessus cochées.
1. **Une exécution de référence** : un `run_id` complet dont tous les artefacts (`raw`, `processed`, `logs`, `reports`) sont conservés et liés.
1. **Le `README.md`** avec installation, usage, limites, base légale, contact.
1. **La fiche d’enquête** remplie pour l’exécution de référence.
1. **Optionnel mais recommandé** : 2-3 tests `pytest` sur les fonctions pures de `clean.py` et `parse.py`.

### Extensions possibles (pour aller plus loin)

Une fois la version de base livrée, plusieurs directions :

|Extension                                                                       |Difficulté|Apport                                   |
|--------------------------------------------------------------------------------|----------|-----------------------------------------|
|Mode **veille** : 2ᵉ commande qui compare avec le snapshot précédent            |🟡         |Réutilise tout le chapitre 13.           |
|Sortie HTML stylée pour le rapport                                              |🟢         |Pandoc ou `markdown` package.            |
|Plugin RSS / sitemap : si la cible expose un flux, l’utiliser au lieu de scraper|🟡         |Cohérence avec la doctrine du chapitre 4.|
|Test d’intégration avec `requests-mock`                                         |🟡         |Tester sans toucher au réseau.           |
|Mode interactif : choix des cibles via prompts plutôt que `targets.txt`         |🟢         |Confort utilisateur.                     |
|Export SQLite                                                                   |🟡         |Quand le volume dépasse JSON.            |
|Webhook de notification                                                         |🟡         |Veille collaborative.                    |


> **Conseil :** ne te lance dans les extensions qu’**après** avoir une version de base parfaitement propre. Mieux vaut un outil minimal et carré qu’un outil ambitieux et fragile.

### ✅ Tu sais maintenant…

- Concevoir et architecturer un projet OSINT complet
- Implémenter chaque module en s’appuyant sur les chapitres précédents
- Orchestrer le tout dans un `main.py` lisible
- Documenter, tester, et livrer un projet présentable en portfolio
- Auto-évaluer ton outil sur les critères technique, traçabilité, documentation, sécurité, robustesse

-----


## Annexes

### Annexe A — Sites d’entraînement légaux et reproductibles

|Site                                                                      |Pour quoi                                                                                       |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
|`https://books.toscrape.com`                                              |Catalogue paginé. Idéal pour `requests`, BeautifulSoup, pagination.                             |
|`https://quotes.toscrape.com`                                             |Citations paginées avec variantes (JS, login factice). Excellent pour s’entraîner.              |
|`https://httpbin.org`                                                     |Bac à sable HTTP : statuts personnalisés, headers, délais. Indispensable pour tester `requests`.|
|`https://jsonplaceholder.typicode.com`                                    |API REST fictive pour s’entraîner aux APIs.                                                     |
|`https://api.open-meteo.com`                                              |API météo réelle, sans clé. Très bien pour s’entraîner aux APIs publiques.                      |
|`https://restcountries.com`                                               |API REST sur les pays. Sans clé.                                                                |
|`https://en.wikipedia.org/api/rest_v1/`                                   |API Wikipedia (lecture, modifications, métadonnées). Doc claire, rate limit raisonnable.        |
|`https://news.ycombinator.com` / API : `https://github.com/HackerNews/API`|API Hacker News (lecture seule). Sans clé.                                                      |
|`https://www.data.gouv.fr/api/`                                           |Open data administratif français.                                                               |
|`https://data.europa.eu/api/hub/search`                                   |Portail européen d’open data.                                                                   |

### Annexe B — Modules à explorer ensuite

|Module                   |Pour quoi                                                                                                        |
|-------------------------|-----------------------------------------------------------------------------------------------------------------|
|`tldextract`             |Extraction propre du domaine racine (gère les TLD composés comme `.co.uk`).                                      |
|`requests-cache`         |Cache HTTP transparent en développement.                                                                         |
|`feedparser`             |Parser RSS/Atom robuste.                                                                                         |
|`scrapy`                 |Framework de crawling à grande échelle, avec planification, middlewares, pipelines.                              |
|`playwright` / `selenium`|Navigateurs automatisés pour sites réellement dynamiques — **outils avancés**, à utiliser dans un cadre autorisé.|
|`dnspython`              |Résolution DNS programmatique (A, AAAA, MX, NS, TXT, etc.).                                                      |
|`python-whois` / RDAP    |Infos d’enregistrement de domaines (RDAP est l’approche moderne).                                                |
|`pandas`                 |Analyse de datasets une fois propres : agrégations, jointures, exports.                                          |
|`pytest`                 |Tests unitaires et d’intégration.                                                                                |
|`pyyaml`                 |Lecture/écriture YAML, pour les configurations.                                                                  |
|`jinja2`                 |Templates pour les rapports récurrents.                                                                          |
|`pandoc` (externe)       |Conversion Markdown ↔ HTML ↔ PDF.                                                                                |

### Annexe C — Repères juridiques à vérifier avant usage réel

> **Rappel essentiel :** ce qui suit n’est ni un conseil juridique, ni un état exhaustif du droit applicable. Le droit évolue. Pour un projet réel et engageant (entreprise, mission, journalisme), consulte un juriste.

|Cadre                                         |Pour vérifier                                                                                                                                   |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
|**RGPD (UE)**                                 |Toute collecte qui touche à des données personnelles. Vérifier finalité, base légale, minimisation, durée de conservation, droits des personnes.|
|**LCEN + Code pénal (FR, art. 323-1 et s.)**  |Atteintes aux systèmes de traitement automatisé de données. **Ne jamais** contourner une protection technique.                                  |
|**Droit d’auteur**                            |Textes, images, vidéos, bases de données. Le fait qu’un contenu soit accessible ne le rend pas réutilisable.                                    |
|**Droit sui generis sur les bases de données**|Extraction « substantielle » d’une base de données protégée.                                                                                    |
|**CGU / ToS**                                 |Force contractuelle variable selon les juridictions, mais leur violation peut t’exposer.                                                        |
|**Affaires de référence**                     |hiQ Labs vs LinkedIn (US), Ryanair vs PR Aviation (UE), décisions CNIL. À titre culturel uniquement — chaque cas est spécifique.                |

**Réflexe :** en cas de doute sur une cible réelle, documente le doute dans la fiche d’enquête **et** consulte avant d’agir.

### Annexe D — Modèle de fiche d’enquête

À copier dans `config/fiche-enquete.md` et à remplir avant chaque projet.

```markdown
# Fiche d’enquête

## Métadonnées
- Titre :
- Auteur :
- Date de création :
- Version :
- run_id de référence :

## Question
- Question d’enquête (1 phrase) :

## Sources envisagées
- Sources possibles :
- API officielle disponible ? (oui/non, URL, lien CGU) :
- Flux RSS / Atom disponible ? (oui/non, URL) :
- Sitemap disponible ? (oui/non, URL) :
- Open data pertinent ? (oui/non, URL, licence) :
- Scraping HTML envisagé ? (oui/non) :

## Méthode retenue
- Méthode :
- Justification (pourquoi pas une source plus propre ?) :

## Cadre
- robots.txt vérifié ? (oui/non, extraits pertinents) :
- CGU vérifiées ? (oui/non, points marquants) :
- Base légale et finalité :
- Données personnelles concernées ? (oui/non, lesquelles, minimisation appliquée) :

## Collecte
- Données minimales collectées (liste exhaustive) :
- Format de sortie attendu :
- Volume attendu :
- Délai entre requêtes :
- Plafond de volume :
- User-Agent utilisé :

## Limites et angles morts
- Angles morts identifiés :
- Risques techniques (site dynamique, anti-bot, encodage) :
- Risques éthiques :
- Doutes non levés (à documenter !) :

## Reproductibilité
- Commande exacte :
- Version Python :
- requirements.txt figé (oui/non) :
- Chemins des artefacts produits :
```

-----


## Conclusion du cours

Tu es arrivé au bout du cours. Faisons le point.

### Ce que tu sais faire maintenant

**Méthode**

- Poser les 4 questions préalables à toute collecte.
- Lire un `robots.txt` et appliquer ses contraintes.
- Choisir entre API, RSS, sitemap, open data et scraping — dans cet ordre.
- Documenter une enquête dans une fiche structurée.

**Technique**

- Faire des requêtes HTTP propres avec `requests` (timeout, User-Agent, retries).
- Parser du HTML avec BeautifulSoup (sélecteurs robustes, méthodologie Inspect → Sélecteur → Test).
- Extraire des données structurées en respectant un modèle `{données + source + horodatage + outil}`.
- Stocker en CSV, JSON, JSONL selon le cas.
- Nettoyer, normaliser, dédupliquer.
- Paginer une collecte avec deux conditions d’arrêt.
- Consommer une API REST et gérer rate limits et authentification.
- Mettre en place sessions, retries, logs, configuration externe.

**Enquête**

- Construire un veilleur basé sur des snapshots versionnés.
- Détecter les changements (ajouts / retraits / modifications).
- Produire un rapport OSINT structuré, borné à la collecte, reproductible.

**Architecture**

- Organiser un projet (`src/`, `data/`, `config/`, `logs/`, `reports/`).
- Séparer code, données, configuration, secrets.
- Documenter avec README et `.env.example`.
- Auto-évaluer son projet avec une checklist sérieuse.

### Ce que ce cours ne couvre pas (et où aller ensuite)

- **Sites réellement dynamiques** : Playwright, Selenium. À approcher **dans un cadre autorisé** uniquement.
- **Crawling à grande échelle** : Scrapy, avec middlewares, planification, pipelines.
- **Analyse de données** : pandas, visualisation, NLP.
- **Reverse engineering d’endpoints d’API non documentées** : précautions juridiques importantes.
- **Sécurité opérationnelle avancée** (VPN d’investigation, environnements isolés, persona OSINT) : sujet à part entière.
- **Aspects organisationnels** : gestion d’équipe d’analystes, partage sécurisé des données, archivage long terme.

Chacun de ces domaines vaut son propre cours. Tu as maintenant la base technique et méthodologique pour les aborder sereinement.

### Le mot de la fin

Tu as appris à collecter du web. Mais la **valeur** ne vient pas du code que tu écris : elle vient de la **question** que tu poses, et de la **rigueur** avec laquelle tu cherches la réponse.

Un mauvais analyste avec un excellent scraper produit du bruit. Un bon analyste avec un scraper modeste produit de la connaissance.

Vise toujours la deuxième catégorie.

Bonne collecte. **Et bonne enquête.**

-----

*Fin du cours.*
