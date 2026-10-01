---
title: Chapitre 7 — Extraction structurée d’une page
source: Cyber/02 OSINT/Python pour l'OSINT et le scraping.md
note: Python pour l'OSINT et le scraping
up:
- - Python pour l'OSINT et le scraping
  - ../index.md
- - Partie II — Premières collectes
  - index.md
---

Récupérer du texte, c’est bien. Construire une **structure** exploitable, c’est mieux. Ce chapitre te fait passer du « j’ai sorti des trucs de la page » au « j’ai produit un dataset propre, traçable et prêt à stocker ».

## Le minimum à savoir

### Le modèle « un item = un dict »

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

### Le pattern de boucle d’extraction

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

### Gérer les champs manquants

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

### Extraire des liens (cas typique)

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

### Extraire un tableau HTML

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

## Très utile en pratique

### Normaliser au moment de l’extraction

Plutôt que de stocker des données « sales » et nettoyer plus tard, profite de la boucle d’extraction pour nettoyer en passant. Quelques règles :

|Champ                          |Normalisation suggérée                                                                              |
|-------------------------------|----------------------------------------------------------------------------------------------------|
|Texte libre                    |`strip()`, suppression des espaces insécables, espaces multiples compactés.                         |
|URL                            |Conversion en absolu (`urljoin`).                                                                   |
|Date affichée (« 12 mai 2026 »)|Conserver telle quelle dans un champ `date_affichee`. Tenter le parsing dans `date_iso` si possible.|
|Liste de tags                  |Trim chaque tag, ne pas inclure les vides.                                                          |
|Nombres affichés (`"1 234 €"`) |Conserver le brut **et** une version numérique séparée.                                             |


> **Bonne pratique :** quand la valeur n’est pas évidente à parser (date locale, nombre formaté), garde **les deux** versions : le brut tel qu’extrait, et la version normalisée. Si la normalisation se trompe, tu peux corriger sans recollecter.

### Le cas particulier de l’extraction d’emails

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

### Toujours conserver l’URL source

Dans chaque enregistrement, le champ `source_url` permet à toi et à un tiers de :

- vérifier la donnée en l’ouvrant dans un navigateur,
- relancer une collecte sur cette page seule,
- savoir si une donnée vient de la home page, d’un article, d’une catégorie.

C’est **non négociable**.

### Quand le sélecteur change selon la position

Sur certaines pages, le premier item a une structure légèrement différente des autres (parce qu’il est mis en avant). Deux approches :

```python
# Option 1 : filtrer le premier item (souvent en plus dans la liste générale)
items = soup.select(".article")[1:]  # ignore le mis-en-avant

# Option 2 : extraire séparément
mis_en_avant = soup.select_one(".featured-article")
items = soup.select(".article-list .article")
```


À choisir selon ce que tu veux conserver dans ton dataset.

## Bonus

### Les microdonnées JSON-LD, encore (mais en pratique)

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

### `<time datetime="...">` pour les dates machines

Les bons sites utilisent la balise `<time>` avec un attribut `datetime` au format ISO 8601 :

```html
<time datetime="2026-05-17T10:00:00Z">17 mai 2026</time>
```


Tu peux extraire :

- la version humaine : `time.get_text(strip=True)` → `"17 mai 2026"`
- la version machine : `time.get("datetime")` → `"2026-05-17T10:00:00Z"`

Toujours préférer la version machine pour le stockage et le tri.

## ❌ Erreur classique

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


## Exercices

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

## 🧩 Mini-projet de Partie II — *Collecteur de citations*

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

## ✅ Tu sais maintenant…

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
