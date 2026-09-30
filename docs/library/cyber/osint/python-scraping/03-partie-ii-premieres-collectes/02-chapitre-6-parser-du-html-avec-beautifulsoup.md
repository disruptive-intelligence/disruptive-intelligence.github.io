---
title: Chapitre 6 — Parser du HTML avec BeautifulSoup
source: Cyber/02_OSINT/Python_Scraping.md
note: Python & scraping
up:
- - Python & scraping
  - ../index.md
- - Partie II — Premières collectes
  - index.md
---

Tu as récupéré une page HTML. C’est une grosse soupe de balises. **BeautifulSoup** est la bibliothèque qui transforme cette soupe en arbre exploitable.

## Le minimum à savoir

### Installation rappel

```bash
pip install beautifulsoup4 lxml
```


`beautifulsoup4` est la bibliothèque, `lxml` est le parser rapide qu’elle peut utiliser en interne.

### Premier parsing

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


### Choix du parser

|Parser         |Caractéristiques                                    |Quand                                       |
|---------------|----------------------------------------------------|--------------------------------------------|
|`"html.parser"`|Intégré à Python, pas d’installation supplémentaire.|Petits scripts, dépannage.                  |
|`"lxml"`       |Rapide, robuste, supporte du XML.                   |Recommandé pour tout projet sérieux.        |
|`"html5lib"`   |Très tolérant aux erreurs HTML.                     |Sites au HTML « cassé » qui posent problème.|

Tous donnent le même objet `soup` derrière. On utilisera `"lxml"` par défaut.

### Charger depuis un fichier (ton flux de travail principal)

Souvenir du chapitre 5 : tu as sauvegardé une page dans `data/raw/`. Tu vas parser **ce fichier**, pas retaper le serveur.

```python
from bs4 import BeautifulSoup
from pathlib import Path

html_brut = Path("data/raw/20260517T140000Z_books_toscrape_com.html").read_bytes()
soup = BeautifulSoup(html_brut, "lxml")
```


Note : on passe `bytes`, BeautifulSoup gère l’encodage à partir des balises `<meta charset>` du HTML. C’est plus fiable que de décoder soi-même.

### Naviguer dans l’arbre : `find` et `find_all`

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


### Naviguer avec les sélecteurs CSS : `select` et `select_one`

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

### Extraire le texte

```python
tag = soup.select_one("h1")

print(tag.get_text())                # texte avec espaces internes potentiels
print(tag.get_text(strip=True))      # texte nettoyé (recommandé)
print(tag.text)                      # raccourci de .get_text()
```


`strip=True` enlève les espaces et retours à la ligne en début/fin. C’est presque toujours ce que tu veux.

### Extraire des attributs

```python
lien = soup.select_one("a")

# Méthode crochets : crash si l’attribut n’existe pas
href = lien["href"]                  # ❌ KeyError si pas de href

# Méthode .get() : retourne None si absent (plus sûr)
href = lien.get("href")              # ✅
href = lien.get("href", "")          # ✅ avec valeur par défaut
```


> **Bonne pratique :** utilise toujours `.get("attribut")` quand tu n’es pas absolument certain que l’attribut existe.

### Itérer proprement

```python
# Extraire texte et URL de tous les liens d’une page
for lien in soup.find_all("a"):
    texte = lien.get_text(strip=True)
    url = lien.get("href")
    if texte and url:                # filtre les liens vides
        print(f"{texte} -> {url}")
```


## Très utile en pratique

### La méthodologie : Inspect → Sélecteur → Test

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

### Choisir un sélecteur robuste

Tous les sélecteurs ne se valent pas dans le temps :

|Sélecteur               |Robustesse                                            |
|------------------------|------------------------------------------------------|
|`#article-main h1`      |🟢 Très robuste (id stable, hiérarchie sémantique)     |
|`article > h1`          |🟢 Robuste (structure HTML5 stable)                    |
|`.titre-principal`      |🟡 Dépend des conventions du site                      |
|`.css-x7f3k2`           |🔴 Très fragile (classe générée, change à chaque build)|
|`div > div > div > span`|🔴 Très fragile (dépend de la structure exacte)        |

**Réflexe pro :** quand plusieurs sélecteurs sont possibles, prends celui qui repose sur la **sémantique** (`article`, `header`, `nav`, `time`, `data-*`) plutôt que sur la mise en page.

### Workflow recommandé

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

### Nettoyer le texte extrait

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

## Bonus

### XPath (mention culturelle)

`lxml` (sans BeautifulSoup) permet d’utiliser **XPath**, un langage de sélection encore plus puissant que CSS pour des cas tordus :

```python
from lxml import html

tree = html.fromstring(r.content)
titres = tree.xpath("//article//h2/text()")
```


XPath excelle pour les sélections « relatives au texte » (« le `<td>` qui suit le `<td>` contenant ‘Total’ »). En pratique, les sélecteurs CSS de BeautifulSoup couvrent 95 % des cas. Garde XPath dans un coin de ta tête pour les 5 % restants.

### Récupérer les microdonnées : `<script type="application/ld+json">`

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

## ❌ Erreur classique

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


## Exercices

**Guidé :** Sur le HTML de `https://quotes.toscrape.com` (sauvegardé localement) :

1. Charge le fichier dans `BeautifulSoup`.
1. Trouve toutes les citations affichées sur la page (ce sont les `<div class="quote">`).
1. Pour chaque citation, extrais et affiche le texte de la citation seul (sélecteur `.text`).

**Autonome :** Sur le même HTML :

1. Pour chaque citation, extrais aussi : l’auteur, et la liste des tags.
1. Affiche le tout sous forme propre : `« texte » — auteur (tags)`.
1. Vérifie que ton script trouve bien **10 citations** sur la page (c’est le nombre attendu).

## ✅ Tu sais maintenant…

- Charger une page HTML dans `BeautifulSoup` (avec parser `lxml`)
- Naviguer dans l’arbre avec `find` / `find_all` ou `select` / `select_one`
- Choisir un sélecteur **robuste** (sémantique > classe générée)
- Extraire texte avec `.get_text(strip=True)` et attributs avec `.get("attr")`
- Le workflow : fetch une fois → parser hors ligne → itérer librement
- Nettoyer le texte (espaces insécables, espaces multiples)
- Repérer et exploiter le JSON-LD quand il existe

-----
