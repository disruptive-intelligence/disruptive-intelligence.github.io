---
title: Chapitre 3 — Comment fonctionne le web (vu côté collecteur)
source: Cyber/02_OSINT/Python_Scraping.md
note: Python pour l'OSINT et le scraping
up:
- - Python pour l'OSINT et le scraping
  - ../index.md
- - Partie I — Fondations
  - index.md
---

Avant de coder une requête, il faut comprendre **ce qu’on demande, à qui, et ce qu’on récupère**. Ce chapitre est volontairement dense — c’est le socle technique de tout ce qui suit.

## Le minimum à savoir

### Le modèle client / serveur

```
        REQUÊTE
   ┌──────────────────────►
[CLIENT]                  [SERVEUR]
   │  (ton navigateur       │  (le site web)
   │   ou ton script)       │
   ◄──────────────────────┘
        RÉPONSE
```


À chaque action sur le web, ton **client** (navigateur ou script Python) envoie une **requête** à un **serveur**, et reçoit une **réponse**.

Une requête, c’est : « donne-moi cette URL ». Une réponse, c’est : « voilà le contenu (ou voilà pourquoi je ne peux pas) ».

### Anatomie d’une URL

```
https://www.exemple.fr:443/articles/2026/recent?page=2&sort=date#commentaires
  │       │           │   │                     │                │
  │       │           │   │                     │                └── Fragment (côté client uniquement)
  │       │           │   │                     └─────────────────── Query string (paramètres)
  │       │           │   └───────────────────────────────────────── Chemin (path)
  │       │           └───────────────────────────────────────────── Port (souvent implicite : 443 pour HTTPS)
  │       └───────────────────────────────────────────────────────── Hôte (host)
  └─────────────────────────────────────────────────────────────────── Schéma (protocole)
```


|Partie      |Rôle                                                               |
|------------|-------------------------------------------------------------------|
|**Schéma**  |`https` ou `http`. HTTPS = chiffré, HTTP = en clair.               |
|**Hôte**    |Le serveur cible. Souvent un sous-domaine (`www`).                 |
|**Port**    |Le canal d’écoute. 443 pour HTTPS, 80 pour HTTP. Souvent implicite.|
|**Chemin**  |Le « dossier/fichier » côté serveur.                               |
|**Query**   |Paramètres après le `?`, séparés par `&`. Clé/valeur.              |
|**Fragment**|Après le `#`. **Jamais envoyé au serveur** — ancre côté client.    |


> **À retenir :** le fragment (`#...`) ne sert qu’au navigateur pour scroller jusqu’à une ancre. Il n’est **pas** envoyé dans la requête HTTP.

### HTTPS vs HTTP

**HTTPS** chiffre la communication entre toi et le serveur. **HTTP** la laisse en clair. Aujourd’hui, presque tous les sites sont en HTTPS.

Pour un scraper, ça change peu — `requests` gère HTTPS de manière transparente. Mais à savoir : HTTPS protège **le contenu**, pas l’identité (le serveur sait toujours qui tu es par ton IP).

### Une requête HTTP en détail

Une requête HTTP, en réalité, ressemble à ceci (côté coulisses) :

```
GET /articles/123 HTTP/1.1
Host: www.exemple.fr
User-Agent: MonOutilOSINT/0.1
Accept: text/html
Accept-Language: fr-FR,fr;q=0.9

(corps vide pour un GET)
```


Trois parties :

1. **Ligne de requête** : méthode (`GET`), chemin (`/articles/123`), version HTTP.
1. **Headers** : métadonnées (qui demande, ce qu’il accepte, etc.).
1. **Corps** (optionnel) : pour les requêtes qui envoient des données (POST, PUT).

Et une réponse :

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 1532

<!DOCTYPE html>
<html>...
```


1. **Ligne de statut** : version, code, message.
1. **Headers** : métadonnées de la réponse.
1. **Corps** : le contenu (HTML, JSON, image, etc.).

### Les méthodes HTTP

Tu en croiseras surtout deux :

|Méthode |Sens                           |Quand                                        |
|--------|-------------------------------|---------------------------------------------|
|**GET** |« Donne-moi cette ressource »  |Lecture. C’est 95 % de ce qu’un scraper fait.|
|**POST**|« Voici des données à traiter »|Envoi de formulaire, création de ressource.  |

Les autres (`PUT`, `DELETE`, `HEAD`, `OPTIONS`) existent, mais sont rares en OSINT défensif.

### Les codes de statut

|Code         |Famille             |Sens                                      |
|-------------|--------------------|------------------------------------------|
|**200**      |2xx — Succès        |OK, la ressource est dans le corps.       |
|**301 / 302**|3xx — Redirection   |La ressource a déménagé.                  |
|**400**      |4xx — Erreur client |Ta requête est malformée.                 |
|**401**      |4xx                 |Authentification requise.                 |
|**403**      |4xx                 |Accès interdit.                           |
|**404**      |4xx                 |Pas trouvé.                               |
|**429**      |4xx                 |**Trop de requêtes** — tu vas trop vite.  |
|**500**      |5xx — Erreur serveur|Le serveur a planté.                      |
|**503**      |5xx                 |Service indisponible (souvent temporaire).|


> **À retenir :** un `200` n’est **pas** une garantie de succès logique. Un site peut renvoyer une page d’erreur ou « contenu introuvable » en `200`. Toujours vérifier le **contenu**, pas juste le statut.

### Les headers importants

|Header                    |Rôle                                                        |
|--------------------------|------------------------------------------------------------|
|`User-Agent`              |Dit qui fait la requête.                                    |
|`Accept`                  |Types de contenu acceptés (`text/html`, `application/json`).|
|`Accept-Language`         |Langues préférées.                                          |
|`Referer`                 |D’où vient la requête (page précédente).                    |
|`Cookie`                  |Données de session côté client.                             |
|`Content-Type` (réponse)  |Format du corps renvoyé.                                    |
|`Content-Length` (réponse)|Taille du corps.                                            |

### HTML, balises, attributs

Le HTML est un langage de **structure**. Il décrit la mise en forme d’une page sous forme d’arborescence.

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <title>Mon article</title>
  </head>
  <body>
    <article class="post" id="article-123">
      <h1>Titre de l'article</h1>
      <p class="lead">Introduction.</p>
      <a href="https://exemple.fr/source">Source</a>
    </article>
  </body>
</html>
```


- Une **balise** est délimitée par `<...>` et `</...>` (ou auto-fermée comme `<img />`).
- Un **attribut** est une info dans la balise ouvrante (`class="post"`, `href="..."`).
- La **classe** (`class`) sert à grouper des éléments stylés similairement.
- L’**identifiant** (`id`) est unique dans la page.

### Le DOM : l’arbre des éléments

Une fois la page chargée, le navigateur en construit une représentation en **arbre** : le **DOM (Document Object Model)**.

```
html
├── head
│   └── title
└── body
    └── article (.post #article-123)
        ├── h1
        ├── p (.lead)
        └── a (href=...)
```


C’est dans cet arbre que tu vas naviguer pour extraire ce qui t’intéresse, en utilisant des **sélecteurs CSS**.

### Les sélecteurs CSS

Quelques exemples qui couvrent 90 % des cas :

|Sélecteur         |Cible                                          |
|------------------|-----------------------------------------------|
|`a`               |Toutes les balises `<a>`                       |
|`.post`           |Tous les éléments avec `class="post"`          |
|`#article-123`    |L’élément avec `id="article-123"`              |
|`article p`       |Tous les `<p>` à l’intérieur d’un `<article>`  |
|`article > h1`    |Les `<h1>` enfants **directs** d’un `<article>`|
|`a[href^="https"]`|Les `<a>` dont `href` commence par `https`     |
|`p.lead`          |Les `<p>` qui ont la classe `lead`             |

Ces sélecteurs sont les mêmes qu’en CSS pour styliser une page. BeautifulSoup les comprend tels quels.

### Site statique vs site dynamique

|Type         |Comment ça marche                                                                                   |Conséquence pour le scraping                                 |
|-------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
|**Statique** |Le serveur envoie directement le HTML final.                                                        |`requests` reçoit ce que tu vois. Facile à scraper.          |
|**Dynamique**|Le serveur envoie un squelette + du JavaScript. Le navigateur exécute le JS pour construire la page.|`requests` ne reçoit **que** le squelette. Le contenu manque.|

**Comment savoir ?** Dans ton navigateur, ouvre la page, fais clic droit → **« Afficher le code source »** (pas « Inspecter »). Si tu vois le texte qui t’intéresse dans le code source brut, c’est statique. Sinon, c’est dynamique et `requests` ne suffira pas.

> **À retenir :** pour les sites dynamiques, on commence **toujours** par chercher la source plus propre (API, RSS, sitemap). Les outils de pilotage de navigateur (Playwright, Selenium) sont un **dernier recours** dans un cadre autorisé.

### Les DevTools du navigateur

Apprends à utiliser les outils de développement de ton navigateur (F12 ou clic droit → « Inspecter ») :

|Onglet                      |À quoi ça sert                                                                                            |
|----------------------------|----------------------------------------------------------------------------------------------------------|
|**Elements** (ou Inspecteur)|Voir et explorer le DOM, identifier les sélecteurs.                                                       |
|**Network** (ou Réseau)     |Voir toutes les requêtes que la page fait. Indispensable pour repérer un endpoint JSON appelé par la page.|
|**Console**                 |Tester des sélecteurs, lire les erreurs JS.                                                               |


> **Méthode** : sur la page, clic droit sur l’élément qui t’intéresse → « Inspecter ». Le DOM s’ouvre exactement sur ce nœud. Tu peux y lire la classe, l’id, la hiérarchie. C’est comme ça qu’on construit un sélecteur CSS fiable.

## Très utile en pratique

### Reconnaître un site dynamique en 30 secondes

1. Ouvre la page dans ton navigateur.
1. Clic droit → « Afficher le code source » (Ctrl+U).
1. Ctrl+F → cherche un mot que tu vois à l’écran.
1. Trouvé ? → Statique. Pas trouvé ? → Dynamique.

C’est la première chose à faire avant d’écrire le moindre scraper.

### Identifier un endpoint JSON publiquement appelé par la page

Beaucoup de sites « dynamiques » récupèrent leurs données en appelant une URL JSON depuis le navigateur. C’est souvent **bien plus propre à exploiter** que le HTML rendu.

1. Ouvre les DevTools (F12) → onglet **Network**.
1. Recharge la page.
1. Filtre sur **XHR** ou **Fetch**.
1. Repère les réponses en JSON.
1. Clique → onglet **Response** → tu vois la donnée brute.

Si tu trouves un endpoint qui sert exactement ce qui t’intéresse, **change de stratégie** : interroge cet endpoint directement (chapitre 11), c’est plus stable et plus propre que de scraper le HTML rendu.

> **Vocabulaire :** on ne parle pas d’« API cachée ». L’endpoint est appelé en clair par la page que tu visites — il est publiquement observable. On parle simplement de **l’endpoint JSON appelé par la page**.

### Pourquoi un scraper casse

Un scraper est par nature **fragile**. Voici les causes typiques de casse :

|Cause                           |Symptôme                                                   |Mitigation                                             |
|--------------------------------|-----------------------------------------------------------|-------------------------------------------------------|
|**Changement de HTML**          |Le sélecteur ne trouve plus rien.                          |Sélecteurs robustes (id stables, attributs `data-*`).  |
|**Classes CSS dynamiques**      |Classes du genre `css-x7f3k2`, qui changent à chaque build.|Cibler par structure plutôt que par classe.            |
|**Contenu chargé en JavaScript**|Données absentes du HTML brut.                             |API ou RSS ; en dernier recours, navigateur automatisé.|
|**Pagination modifiée**         |Les pages 2, 3… renvoient autre chose.                     |Détection d’arrêt explicite ; logs.                    |
|**Redirections (301/302)**      |Tu collectes la mauvaise URL.                              |Lire `response.url` après la requête.                  |
|**Erreurs réseau (timeouts)**   |Requêtes qui pendent ou échouent.                          |Timeout obligatoire, retries.                          |
|**Encodage**                    |Caractères cassés (`Ã©` au lieu de `é`).                   |Forcer `utf-8`, vérifier `response.encoding`.          |
|**Contenu personnalisé**        |Pages qui changent selon la langue, le pays, la session.   |Headers explicites, isolation de session.              |
|**Anti-bot**                    |Captcha, bannissement IP, 403 systématique.                |Signal qu’il faut chercher l’API ou abandonner.        |


> **À retenir :** un scraper sera révisé. Plusieurs fois. C’est normal. La qualité d’un scraper se mesure non pas à sa beauté du premier jour, mais à la facilité avec laquelle on le maintient quand le site change.

## ❌ Erreur classique

```
# Confondre "ce que je vois dans le navigateur"
# et "ce que requests reçoit"

L’apprenant ouvre la page, voit les données, écrit son scraper,
et obtient une page vide → c’était un site dynamique.

→ Toujours faire le test "Afficher le code source" avant de coder.

# Oublier l’encodage
Le HTML est en UTF-8, mais le système suppose autre chose.
Résultat : "Caf\u00e9" ou "Café" devient "Café".

→ Toujours forcer encoding="utf-8" en écriture, et vérifier
   response.encoding en lecture.

# Cibler par classe générée dynamiquement
Le scraper utilise .css-x7f3k2 comme sélecteur. Une semaine
plus tard, c’est .css-y9h4m1 et tout casse.

→ Préférer les id stables, les attributs sémantiques
   (data-testid, role), ou la structure (article > h1).

# Considérer un 200 comme une réussite
Le site renvoie 200 + page "article introuvable".
Le scraper enregistre du vide en pensant que tout va bien.

→ Vérifier le contenu en plus du statut.
```


## Bonus

### Les en-têtes de sécurité (culture générale)

Tu croiseras parfois des headers comme :

- `Content-Security-Policy` (CSP)
- `Strict-Transport-Security` (HSTS)
- `X-Frame-Options`

Ce sont des mécanismes de **défense du site**, qui n’affectent pas directement le scraping en lecture, mais qui te donnent une indication sur le sérieux de l’hébergeur.

### Cookies et sessions

Un cookie est un petit fichier que le serveur demande au client de garder. À la requête suivante, le client renvoie ce cookie, ce qui permet au serveur de « reconnaître » la session.

En OSINT défensif, on touche peu aux cookies — on travaille sur des contenus accessibles **sans session**. Si une donnée nécessite d’être connecté pour être vue, c’est qu’elle n’est pas vraiment publique.

## Exercices

**Guidé :** Sur la page `https://books.toscrape.com/` :

1. Ouvre les DevTools, onglet Elements.
1. Trouve la balise contenant le premier livre.
1. Note sa balise, ses classes, et la hiérarchie jusqu’au titre du livre.
1. Construis un sélecteur CSS qui ciblerait **uniquement** les titres de livres.

**Autonome :** Trouve un site **public non sensible** (idéalement un média, une documentation, un site institutionnel ou un site d’open data) qui charge certaines de ses données via JavaScript :

1. Identifie-le (clic droit → « Afficher le code source », données absentes du HTML brut).
1. Ouvre l’onglet Network des DevTools, recharge, filtre sur XHR/Fetch.
1. Identifie un endpoint JSON appelé par la page.
1. Note son URL et la structure de sa réponse (clés principales).

> **Important :** l’objectif de cet exercice est **uniquement d’observer** le mécanisme dans les DevTools. **Ne lance aucune collecte automatisée** sur cet endpoint à ce stade. La question « ai-je le droit d’interroger cet endpoint en boucle ? » se traite avec la fiche d’enquête et les chapitres suivants, pas par curiosité technique.

## ✅ Tu sais maintenant…

- Décomposer une URL et lire ses parties
- Le modèle requête/réponse HTTP
- Les principaux codes de statut (200, 301, 403, 404, 429, 500)
- Les headers utiles (`User-Agent`, `Accept`, etc.)
- Lire un arbre HTML et utiliser les sélecteurs CSS
- Distinguer site statique et site dynamique en 30 secondes
- Repérer un endpoint JSON appelé par la page via les DevTools
- Anticiper les causes typiques de casse d’un scraper

-----
