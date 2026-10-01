---
title: Python pour l'OSINT et le scraping
source: Cyber/02 OSINT/Python pour l'OSINT et le scraping.md
format: cours
revue: '2026-05-20'
---

*De la collecte web à l’automatisation d’enquête*

-----

> **Prérequis :** avoir terminé un cours Python débutant. Tu dois être à l’aise avec les variables, listes, dictionnaires, boucles, fonctions, fichiers, gestion d’erreurs.
> 
> **Aucun prérequis web :** pas besoin de connaître HTTP, HTML, ni les APIs. On part de zéro côté web.

-----

### Avant-propos

Ce cours n’est pas un cours de Python. C’est un cours d’**enquête en sources ouvertes** qui se sert de Python comme outil. La nuance compte. Un analyste OSINT qui code **simplement mais proprement** vaut mieux qu’un excellent codeur qui collecte sans cadre.

Toute la pédagogie s’organise autour de quatre réflexes :

1. **Penser avant de coder** — quelle question, quelle source, quelle méthode minimale.
1. **Minimiser** — collecter ce qui répond à la question, pas plus.
1. **Tracer** — garder la trace de ce qu’on a collecté, quand et pourquoi.
1. **Respecter** — le droit applicable, les conditions du site, et l’infrastructure de la cible.

Ces réflexes seront rappelés à chaque chapitre. Ils ne sont pas optionnels.

-----

### Avertissement légal et éthique

Ce cours forme à la collecte de **données publiquement accessibles** à des fins défensives : veille, CTI, journalisme, recherche, transparence, sécurité. Il **ne forme pas** à :

- contourner des protections techniques,
- s’authentifier sur des comptes qui ne sont pas les tiens,
- collecter massivement des données personnelles,
- harceler une personne ou une entité,
- enfreindre les CGU d’un service.

Les exemples utilisent des sites conçus pour l’apprentissage (`books.toscrape.com`, `quotes.toscrape.com`, `httpbin.org`) ou des sources publiques explicitement ouvertes. Toute autre cible est sous **ta responsabilité**.

-----

### Glossaire — Les mots à connaître

Reviens ici à chaque fois qu’un terme te semble flou.

#### OSINT et enquête

|Terme           |Définition simple                                                                              |
|----------------|-----------------------------------------------------------------------------------------------|
|**OSINT**       |Open-Source Intelligence — renseignement de sources ouvertes (publiques).                      |
|**CTI**         |Cyber Threat Intelligence — renseignement sur les menaces cyber.                               |
|**Source**      |Un site, un flux, une API d’où provient une donnée.                                            |
|**Sourcing**    |Le fait de tracer la provenance d’une donnée.                                                  |
|**Pivot**       |Un élément (domaine, email, hash) qui permet de rebondir d’une source à une autre.             |
|**Traçabilité** |Capacité à remonter à quand, comment, depuis où une donnée a été collectée.                    |
|**Minimisation**|Principe : ne collecter que ce dont tu as besoin.                                              |
|**OPSEC**       |Operational Security — bonnes pratiques pour ne pas se compromettre soi-même pendant l’enquête.|

#### Web

|Terme         |Définition simple                                                       |
|--------------|------------------------------------------------------------------------|
|**URL**       |Adresse d’une ressource web (`https://exemple.fr/page`).                |
|**HTTP**      |Protocole de communication client/serveur du web.                       |
|**Requête**   |Demande envoyée par ton script au serveur.                              |
|**Réponse**   |Ce que le serveur renvoie (statut + headers + corps).                   |
|**Statut**    |Code numérique de la réponse (200 = OK, 404 = pas trouvé, etc.).        |
|**Header**    |Métadonnée d’une requête ou d’une réponse (langue, type, User-Agent…).  |
|**User-Agent**|Header qui dit qui fait la requête (un navigateur, un script, un robot).|
|**Cookie**    |Petite donnée stockée côté client pour identifier une session.          |

#### HTML et parsing

|Terme            |Définition simple                                                             |
|-----------------|------------------------------------------------------------------------------|
|**HTML**         |Langage de structure des pages web.                                           |
|**Balise**       |Élément HTML (`<p>`, `<a>`, `<div>`…).                                        |
|**Attribut**     |Information attachée à une balise (`href`, `class`, `id`).                    |
|**DOM**          |Représentation en arbre du HTML, telle que vue par le navigateur.             |
|**Sélecteur CSS**|Expression pour cibler des éléments dans le DOM (`.classe`, `#id`, `div > a`).|
|**Parser**       |Programme qui transforme du HTML brut en structure exploitable.               |
|**Scraper**      |Programme qui extrait des données d’une page.                                 |
|**Crawler**      |Programme qui parcourt un site en suivant les liens.                          |

#### Données et bonnes pratiques

|Terme         |Définition simple                                                                                                                                            |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**API**       |Interface conçue pour qu’un programme dialogue avec un service.                                                                                              |
|**REST**      |Style d’API courant fondé sur HTTP.                                                                                                                          |
|**JSON**      |Format de données structurées (`{"clé": "valeur"}`).                                                                                                         |
|**Rate limit**|Limite du nombre de requêtes par unité de temps.                                                                                                             |
|**robots.txt**|Fichier dans lequel un site indique aux robots les zones qu’il préfère autoriser ou interdire au parcours automatisé. Convention, pas autorisation juridique.|
|**CGU / ToS** |Conditions générales d’utilisation d’un service.                                                                                                             |
|**Open data** |Données publiques mises à disposition de tous, souvent en CSV/JSON.                                                                                          |

-----

### Comment penser une collecte OSINT

Avant la moindre ligne de code, un analyste se pose **quatre questions**. Cet ordre n’est pas négociable.

```
1. QUESTION    → Quelle question d’enquête je cherche à répondre ?
                 ↓
2. SOURCE      → Quelle source publique y répond ?
                 ↓
3. MÉTHODE     → Quelle méthode minimale suffit ?
                 (lecture humaine ? API ? RSS ? scraping ?)
                 ↓
4. TRACES      → Quelles traces je conserve pour rendre
                 l’enquête reproductible ?
```


Tout le cours s’articule autour de cette boucle. À la fin, tu auras une **fiche d’enquête** type que tu rempliras pour chaque projet.

> **À retenir :** on ne scrape **jamais** « pour voir ». Si tu n’as pas répondu aux quatre questions ci-dessus, n’écris pas de code.

-----

### La grande différence avec le scripting Python pur

Dans ton cours Python initial, tu manipulais **ton ordinateur** : variables, fichiers, dossiers, scripts. Ici, tu manipules **le web**, c’est-à-dire des serveurs **distants** que tu **ne contrôles pas**. Cela change tout.

|Scripting local               |Collecte web                                             |
|------------------------------|---------------------------------------------------------|
|Le code dépend de toi         |Le code dépend d’un serveur distant                      |
|Une erreur t’affecte toi      |Une erreur peut perturber un service public              |
|Pas de cadre légal particulier|Cadre légal applicable (CGU, RGPD, droit pénal)          |
|Aucune empreinte externe      |Chaque requête laisse une trace dans les logs du serveur |
|Tu peux relancer 1000 fois    |Relancer 1000 fois peut s’apparenter à du déni de service|

Tu vas devoir apprendre des **réflexes nouveaux** : prudence, lenteur volontaire, journalisation systématique, et minimisation.

-----

### Table des matières

#### Partie I — Fondations

- **Chapitre 0 — Préparer son environnement de travail**
- Chapitre 1 — Qu’est-ce que l’OSINT et le web scraping ?
- Chapitre 2 — Cadre légal, éthique et OPSEC du scraping
- Chapitre 3 — Comment fonctionne le web (vu côté collecteur)
- Chapitre 4 — Choisir la source la plus propre

#### Partie II — Premières collectes

- Chapitre 5 — Premières requêtes avec `requests`
- Chapitre 6 — Parser du HTML avec BeautifulSoup
- Chapitre 7 — Extraction structurée d’une page

#### Partie III — Structurer et nettoyer les données

- Chapitre 8 — Stocker les résultats (CSV, JSON, JSONL)
- Chapitre 9 — Nettoyer, normaliser, enrichir

#### Partie IV — Passer à l’échelle

- Chapitre 10 — Pagination et collecte multi-pages
- Chapitre 11 — Utiliser des APIs publiques
- Chapitre 12 — Bonnes pratiques professionnelles

#### Partie V — Enquête, veille et reporting

- Chapitre 13 — Veille et détection de changements
- Chapitre 14 — Du script au rapport d’enquête

#### Partie VI — Projet final

- Chapitre 15 — Outil OSINT de collecte web défensive

#### Annexes

- A — Sites d’entraînement légaux
- B — Modules à explorer ensuite
- C — Repères juridiques à vérifier avant usage réel
- D — Modèle de fiche d’enquête

-----

## Sommaire

- [Chapitre 0 — Préparer son environnement de travail](01-chapitre-0-preparer-son-environnement-de-travail.md)
- [Partie I — Fondations](02-partie-i-fondations/index.md)
    - [Chapitre 1 — Qu’est-ce que l’OSINT et le web scraping ?](02-partie-i-fondations/01-chapitre-1-quest-ce-que-losint-et-le-web-scraping.md)
    - [Chapitre 2 — Cadre légal, éthique et OPSEC du scraping](02-partie-i-fondations/02-chapitre-2-cadre-legal-ethique-et-opsec-du-scrapin.md)
    - [Chapitre 3 — Comment fonctionne le web (vu côté collecteur)](02-partie-i-fondations/03-chapitre-3-comment-fonctionne-le-web-vu-cote-colle.md)
    - [Chapitre 4 — Choisir la source la plus propre](02-partie-i-fondations/04-chapitre-4-choisir-la-source-la-plus-propre.md)
- [Partie II — Premières collectes](03-partie-ii-premieres-collectes/index.md)
    - [Chapitre 5 — Premières requêtes avec requests](03-partie-ii-premieres-collectes/01-chapitre-5-premieres-requetes-avec-requests.md)
    - [Chapitre 6 — Parser du HTML avec BeautifulSoup](03-partie-ii-premieres-collectes/02-chapitre-6-parser-du-html-avec-beautifulsoup.md)
    - [Chapitre 7 — Extraction structurée d’une page](03-partie-ii-premieres-collectes/03-chapitre-7-extraction-structuree-dune-page.md)
- [Partie III — Structurer et nettoyer les données](04-partie-iii-structurer-et-nettoyer-les-donnees/index.md)
    - [Chapitre 8 — Stocker les résultats (CSV, JSON, JSONL)](04-partie-iii-structurer-et-nettoyer-les-donnees/01-chapitre-8-stocker-les-resultats-csv-json-jsonl.md)
    - [Chapitre 9 — Nettoyer, normaliser, enrichir](04-partie-iii-structurer-et-nettoyer-les-donnees/02-chapitre-9-nettoyer-normaliser-enrichir.md)
- [Partie IV — Passer à l’échelle](05-partie-iv-passer-a-lechelle/index.md)
    - [Chapitre 10 — Pagination et collecte multi-pages](05-partie-iv-passer-a-lechelle/01-chapitre-10-pagination-et-collecte-multi-pages.md)
    - [Chapitre 11 — Utiliser des APIs publiques](05-partie-iv-passer-a-lechelle/02-chapitre-11-utiliser-des-apis-publiques.md)
    - [Chapitre 12 — Bonnes pratiques professionnelles](05-partie-iv-passer-a-lechelle/03-chapitre-12-bonnes-pratiques-professionnelles.md)
- [Partie V — Enquête, veille et reporting](06-partie-v-enquete-veille-et-reporting/index.md)
    - [Chapitre 13 — Veille et détection de changements](06-partie-v-enquete-veille-et-reporting/01-chapitre-13-veille-et-detection-de-changements.md)
    - [Chapitre 14 — Du script au rapport d’enquête](06-partie-v-enquete-veille-et-reporting/02-chapitre-14-du-script-au-rapport-denquete.md)
- [Partie VI — Projet final](07-partie-vi-projet-final/index.md)
    - [Chapitre 15 — Outil OSINT de collecte web défensive](07-partie-vi-projet-final/01-chapitre-15-outil-osint-de-collecte-web-defensive.md)
- [Annexes](08-annexes.md)
- [Conclusion du cours](09-conclusion-du-cours.md)
