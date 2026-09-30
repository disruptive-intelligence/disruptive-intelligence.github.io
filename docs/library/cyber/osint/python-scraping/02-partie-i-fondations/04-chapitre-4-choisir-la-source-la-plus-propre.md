---
title: Chapitre 4 — Choisir la source la plus propre
source: Cyber/02_OSINT/Python_Scraping.md
note: Python & scraping
up:
- - Python & scraping
  - ../index.md
- - Partie I — Fondations
  - index.md
---

Avant d’écrire ton premier scraper, **un dernier réflexe à intégrer** : chercher systématiquement la source la plus propre. C’est ce qui transforme un script jetable en démarche d’enquête durable.

## Le minimum à savoir

### La hiérarchie des sources

Quand tu as identifié l’information que tu cherches, monte la pyramide **dans cet ordre** :

```
1. API officielle              → propre, contractuel, stable
        ↓ (si absente)
2. Flux RSS / Atom             → léger, prévu pour ça
        ↓
3. Sitemap XML                 → inventaire complet du site
        ↓
4. Open data (CSV, JSON)       → données publiées intentionnellement
        ↓
5. Scraping HTML               → dernier recours
```


À chaque étape, demande-toi : **« Cette source répond-elle à ma question ? »** Si oui, arrête de monter, descends à l’étape « écrire le code ».

### Pourquoi cet ordre ?

|Critère                  |API      |RSS          |Sitemap |Open data|Scraping     |
|-------------------------|---------|-------------|--------|---------|-------------|
|Prévu pour les programmes|✅        |✅            |✅       |✅        |❌            |
|Stable dans le temps     |🟢        |🟢            |🟢       |🟢        |🔴            |
|Charge serveur           |🟢 Faible |🟢 Faible     |🟢 Faible|🟢 Faible |🔴 Plus lourde|
|Cadre légal clair        |🟢 CGU API|🟢            |🟢       |🟢 Licence|🟡 Flou       |
|Effort de développement  |🟡 Moyen  |🟢 Très faible|🟢 Faible|🟢 Faible |🔴 Élevé      |

À chaque ligne, le scraping perd. Ce n’est pas un hasard si on le place en dernier.

### Reconnaître une API

Une API REST t’expose des données sous forme d’URLs qui renvoient du **JSON** (généralement). Exemple :

```
https://api.exemple.fr/v1/articles?published=2026-05
```


Réponse :

```json
{
  "articles": [
    {"id": 123, "title": "Hello", "published_at": "2026-05-10"},
    {"id": 124, "title": "World", "published_at": "2026-05-11"}
  ],
  "next": "https://api.exemple.fr/v1/articles?page=2"
}
```


Pour savoir si un site propose une API :

- Cherche `<site> API` sur ton moteur préféré.
- Vérifie `<site>/api`, `<site>/developers`, `<site>/dev`.
- Lis la documentation des grandes plateformes (la plupart en proposent).

### Reconnaître un flux RSS / Atom

Un flux RSS, c’est un fichier XML standardisé que les sites publient pour signaler leurs **nouveaux contenus**. C’est **fait pour la veille**.

Exemple typique d’URL :

```
https://exemple.fr/feed
https://exemple.fr/rss
https://exemple.fr/atom.xml
https://exemple.fr/index.xml
```


Contenu d’un flux RSS (simplifié) :

```xml
<rss version="2.0">
  <channel>
    <title>Mon blog</title>
    <link>https://exemple.fr</link>
    <item>
      <title>Mon article</title>
      <link>https://exemple.fr/article-1</link>
      <pubDate>Mon, 12 May 2026 10:00:00 GMT</pubDate>
      <description>Résumé de l’article...</description>
    </item>
  </channel>
</rss>
```


C’est **structuré**, **léger**, **prévu pour les programmes**. Pour de la veille de blogs, médias, podcasts, agences gouvernementales : c’est presque toujours le bon choix.

> **Comment trouver le flux d’un site ?** Beaucoup de sites mettent un lien « RSS » dans leur footer. Sinon, regarde dans le code source de la page : un `<link rel="alternate" type="application/rss+xml" href="...">` indique le flux.

### Reconnaître un sitemap XML

Un sitemap, c’est un **plan du site** au format XML, listant les URLs publiques. Il est destiné aux moteurs de recherche, mais tu peux l’utiliser pour :

- inventorier les pages d’un site sans crawler,
- détecter les nouvelles publications,
- découvrir des sections que la navigation ne met pas en avant.

Localisation habituelle :

```
https://exemple.fr/sitemap.xml
https://exemple.fr/sitemap_index.xml
```


Et son emplacement est souvent indiqué dans le `robots.txt` (`Sitemap: https://...`).

Contenu :

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://exemple.fr/article-1</loc>
    <lastmod>2026-05-12</lastmod>
  </url>
  <url>
    <loc>https://exemple.fr/article-2</loc>
    <lastmod>2026-05-13</lastmod>
  </url>
</urlset>
```


### Reconnaître un dataset open data

Les administrations, ONG, institutions de recherche publient leurs données en accès libre, souvent en CSV, JSON ou API dédiée.

Portails à connaître :

- **France** : `data.gouv.fr`
- **Union européenne** : `data.europa.eu`
- **International** : `data.worldbank.org`, `data.un.org`
- **Recherche** : Zenodo, OpenAIRE

Pour un sujet donné, avant de scraper : **vérifie qu’un dataset open data n’existe pas déjà**. Tu gagnes du temps et tu obtiens des données autoritatives.

### Quand le scraping est-il justifié ?

|Situation                                                                                            |Justifié ?                             |
|-----------------------------------------------------------------------------------------------------|---------------------------------------|
|Le site n’a ni API, ni RSS, ni sitemap, ni open data, et l’information est essentielle à ton enquête.|✅                                      |
|Le site a une API mais elle ne couvre pas l’info que tu cherches.                                    |✅ (raisonnable)                        |
|Le site a un RSS mais tu trouves le scraping « plus pratique ».                                      |❌                                      |
|Tu veux scraper « pour t’entraîner ».                                                                |✅ uniquement sur des sites bac à sable.|

## Très utile en pratique

### Méthode en 5 étapes pour choisir la bonne source

```
1. Définir précisément la donnée cherchée.

2. Vérifier les sources alternatives :
   - L’éditeur a-t-il une API ?
   - Y a-t-il un flux RSS sur cette section ?
   - robots.txt mentionne-t-il un sitemap ?
   - Existe-t-il un dataset open data sur le sujet ?

3. Si oui à une de ces options : changer de stratégie,
   ne pas scraper.

4. Si non : vérifier robots.txt et CGU pour le scraping.

5. Si OK : scraper, le plus poliment possible.
```


### Cas d’usage classés

|Besoin                                          |Source idéale              |
|------------------------------------------------|---------------------------|
|Suivre les nouveaux articles d’un blog          |RSS                        |
|Suivre les communiqués officiels d’un ministère |RSS + open data            |
|Récupérer la météo                              |API (Open-Meteo)           |
|Lister tous les articles d’un site              |Sitemap                    |
|Obtenir des statistiques économiques            |Open data (INSEE, Eurostat)|
|Suivre les commits d’un projet open source      |API GitHub                 |
|Récupérer les modifications d’une page Wikipedia|API MediaWiki              |
|Suivre les nouveaux noms de domaine en `.fr`    |Open data AFNIC            |
|Comparer des prix sur un site sans API ni RSS   |Scraping (avec précautions)|

## ❌ Erreur classique

```
# Ignorer la documentation officielle
"Le site n’a probablement pas d’API."
→ Tu n’en sais rien tant que tu n’as pas regardé.
   Cherche "<site> developer", "<site> API", "<site> docs".

# Scraper un site qui publie un RSS
"Je vais scraper la page des actualités pour suivre les nouveaux articles."
→ Le RSS te donne exactement ça, en plus propre.
   Vérifie /feed, /rss, /atom.xml, /index.xml.

# Confondre sitemap et liste exhaustive
"Le sitemap doit contenir toutes les URLs du site."
→ Pas forcément. Beaucoup de sites n’y mettent que les pages
   destinées à l’indexation. Lis ce que le sitemap propose,
   ne suppose pas.

# Pousser une API jusqu’au rate limit
"L’API marche, je vais aspirer tout d’un coup."
→ Toute API a des limites. Lis la doc, respecte les rate limits.
   Un compte bloqué est un compte qui ne sert plus à rien.
```


## Bonus

### Parser un flux RSS rapidement

`feedparser` est la bibliothèque Python de référence pour lire les flux RSS / Atom :

```bash
pip install feedparser
```


```python
import feedparser

flux = feedparser.parse("https://exemple.fr/feed")
for article in flux.entries[:5]:
    print(article.title, "-", article.link)
```


C’est plus simple et plus stable que de parser le XML à la main. On y reviendra dans la partie sur les sources alternatives au scraping.

### Lire un sitemap

Un sitemap est du XML simple, parsable avec la bibliothèque standard :

```python
import requests
from xml.etree import ElementTree as ET

# Remplace l’URL par celle d’un site qui expose réellement un sitemap.
# Vérifie d’abord son existence (souvent indiquée dans robots.txt).
SITEMAP_URL = "https://exemple.fr/sitemap.xml"

r = requests.get(SITEMAP_URL, timeout=10)
root = ET.fromstring(r.content)
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
urls = [loc.text for loc in root.findall(".//sm:loc", ns)]
print(f"{len(urls)} URLs trouvées")
```


## Exercices

**Guidé :** Pour `https://www.lemonde.fr` :

1. Cherche si un flux RSS existe (inspecte la page d’accueil, cherche un lien « RSS »).
1. Vérifie le `robots.txt`.
1. Y a-t-il un `Sitemap:` mentionné ?
1. Compare : si tu voulais suivre les nouveaux articles, quelle serait la méthode la plus propre ?

**Autonome :** Choisis trois sites de natures différentes que tu consultes régulièrement (un média, une administration, une plateforme). Pour chacun, identifie :

1. Existe-t-il une API publique ?
1. Existe-t-il un flux RSS ?
1. Existe-t-il un sitemap ?
1. Existent des datasets open data sur des sujets connexes ?

Compile tes résultats dans un tableau Markdown.

## 🧩 Mini-projet de Partie I — *Fiche d’enquête*

Avant de passer à la pratique, prépare le **gabarit de fiche d’enquête** que tu rempliras pour chaque mini-projet du reste du cours. Crée le fichier `config/fiche-enquete.md` :

```markdown
# Fiche d’enquête

## Métadonnées
- Titre :
- Auteur :
- Date de création :
- Version :

## Question
- Question d’enquête (1 phrase) :

## Sources
- Sources envisagées :
- API officielle disponible ? (oui/non, URL) :
- Flux RSS disponible ? (oui/non, URL) :
- Sitemap disponible ? (oui/non, URL) :
- Open data pertinent ? (oui/non, URL) :

## Méthode
- Méthode retenue :
- Justification (pourquoi pas une source plus propre ?) :

## Cadre
- robots.txt vérifié (oui/non, extraits pertinents) :
- CGU vérifiées (oui/non) :
- Base légale et finalité :
- Données personnelles concernées ? (oui/non, lesquelles) :

## Collecte
- Données minimales collectées (liste exhaustive) :
- Format de sortie :
- Volume attendu :
- Délai entre requêtes :
- Plafond de volume :

## Limites
- Angles morts identifiés :
- Risques techniques (site dynamique, anti-bot) :
- Risques éthiques :
```


Cette fiche t’accompagnera dans tous les projets suivants.

## ✅ Tu sais maintenant…

- La hiérarchie des sources : API > RSS > sitemap > open data > scraping
- Pourquoi cet ordre n’est pas négociable
- Reconnaître une API, un flux RSS, un sitemap, un dataset open data
- Trouver ces ressources sur un site donné
- La méthode en 5 étapes pour choisir la bonne source
- Quand le scraping est réellement justifié

-----

> **🎯 Tu as terminé la Partie I.**
> 
> Tu n’as pas encore écrit une seule requête. C’est volontaire. Tout ce qui suit — `requests`, BeautifulSoup, APIs, veille — va beaucoup plus loin et beaucoup plus vite parce que tu as posé les fondations.
> 
> La Partie II commence par `requests` : la bibliothèque qui fait dialoguer ton script avec le web.

-----
