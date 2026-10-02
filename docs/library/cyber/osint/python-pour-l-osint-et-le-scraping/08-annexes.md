---
title: Annexes
source: Cyber/02 OSINT/Méthode & enquête/Python pour l'OSINT et le scraping.md
note: Python pour l'OSINT et le scraping
up:
- - Python pour l'OSINT et le scraping
  - index.md
---

## Annexe A — Sites d’entraînement légaux et reproductibles

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

## Annexe B — Modules à explorer ensuite

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

## Annexe C — Repères juridiques à vérifier avant usage réel

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

## Annexe D — Modèle de fiche d’enquête

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
