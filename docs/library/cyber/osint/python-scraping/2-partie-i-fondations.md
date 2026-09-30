---
title: PARTIE I — FONDATIONS
source: Cyber/02_OSINT/Python_Scraping.md
note: Python & scraping
chapter: 2
chapters: 7
---

> **Objectif de la partie :** comprendre **ce qu’on fait, pourquoi, et dans quel cadre**. Aucune ligne de code de scraping dans cette partie. Ce sont les fondations conceptuelles, juridiques et techniques. C’est aussi la partie qui te distingue d’un simple « scrapeur » : un analyste sérieux sait poser le cadre avant de toucher au clavier.

-----


## Chapitre 1 — Qu’est-ce que l’OSINT et le web scraping ?

### Le minimum à savoir

#### Définitions, clairement

**OSINT (Open-Source Intelligence)** = renseignement obtenu à partir de **sources publiquement accessibles**. Les sources peuvent être :

- des sites web (médias, blogs, forums),
- des registres publics (entreprises, marques, domaines),
- des bases open data (gouvernementales, ONG),
- des médias sociaux (parties publiques uniquement),
- des publications scientifiques, des archives, etc.

**Scraping** = extraire automatiquement des données depuis une page web destinée à être lue par un humain (HTML).

**Crawling** = parcourir automatiquement un site en suivant ses liens, sans nécessairement en extraire des données.

**API (Application Programming Interface)** = une interface **prévue par le site** pour qu’un programme accède aux données, généralement en format JSON, souvent avec authentification et règles d’usage claires.

**Collecte manuelle** = un humain lit, copie, prend des captures d’écran. Lent, mais indispensable pour la vérification.

#### Tableau comparatif

|Approche               |Vitesse |Stabilité    |Légitimité             |Quand l’utiliser                                            |
|-----------------------|--------|-------------|-----------------------|------------------------------------------------------------|
|**Manuel**             |⚪ Lent  |🟢 Très stable|🟢 Toujours OK          |Vérification, faibles volumes, sources sensibles            |
|**API**                |🟢 Rapide|🟢 Très stable|🟢 Cadre clair (CGU API)|Dès qu’elle existe — c’est presque toujours la bonne réponse|
|**Flux RSS / Atom**    |🟢 Rapide|🟢 Stable     |🟢 Prévu pour ça        |Veille d’actualités, blogs, publications régulières         |
|**Sitemap / open data**|🟢 Rapide|🟢 Stable     |🟢 Prévu pour ça        |Inventaire d’un site, datasets publics                      |
|**Scraping**           |🟡 Moyen |🔴 Fragile    |🟡 Cadre flou           |Dernier recours, quand rien d’autre n’existe                |

#### La pyramide de la collecte OSINT

```
                  ┌─────────────────────┐
                  │   1. Lecture humaine │ ← toujours par là qu’on commence
                  └──────────┬──────────┘
                             │
                  ┌──────────▼──────────┐
                  │     2. API officielle│
                  └──────────┬──────────┘
                             │
                  ┌──────────▼──────────┐
                  │   3. RSS / Atom      │
                  └──────────┬──────────┘
                             │
                  ┌──────────▼──────────┐
                  │   4. Sitemap / Open  │
                  │      Data            │
                  └──────────┬──────────┘
                             │
                  ┌──────────▼──────────┐
                  │   5. Scraping HTML   │ ← dernier recours
                  └──────────────────────┘
```

> **À retenir :** on monte la pyramide **dans l’ordre**. On ne scrape pas un site dont l’API existe. On ne crawle pas un site qui publie un sitemap. Cette discipline est ce qui fait la différence entre un analyste OSINT pro et un script-kiddie.

#### Cas d’usage défensifs typiques

|Domaine                   |Exemple concret                                                                            |
|--------------------------|-------------------------------------------------------------------------------------------|
|**CTI**                   |Suivre les bulletins publics d’un éditeur de logiciels pour repérer les CVE critiques.     |
|**Brand protection**      |Surveiller la création de domaines proches de ta marque (typosquatting).                   |
|**Veille concurrentielle**|Suivre les annonces d’embauche d’un concurrent pour détecter une réorientation stratégique.|
|**Journalisme**           |Vérifier des prises de position publiques d’un acteur sur plusieurs années.                |
|**Recherche académique**  |Constituer un corpus de publications scientifiques d’un domaine.                           |
|**Transparence publique** |Suivre les modifications d’un règlement gouvernemental.                                    |
|**Sécurité de marque**    |Repérer les copies frauduleuses d’un site officiel.                                        |

#### Ce que le scraping **n’est pas**

- **Ce n’est pas du hacking.** Tu accèdes à la même chose qu’un navigateur — tu n’exploites aucune faille.
- **Ce n’est pas une autorisation universelle.** Le fait qu’une page soit publique ne signifie pas que tu peux l’aspirer en masse.
- **Ce n’est pas magique.** Si le site change son HTML demain, ton script casse.
- **Ce n’est pas anonyme.** Chaque requête laisse une trace dans les logs du serveur cible : IP, User-Agent, horodatage, URL.

### Très utile en pratique

#### Quand préférer une API à un scraper

Toujours, quand :

- l’API existe et donne accès aux données qui t’intéressent,
- les CGU de l’API t’autorisent ton usage,
- les rate limits sont compatibles avec ton volume.

L’API est **stable** (le site peut changer son HTML, l’API change rarement), **rapide**, **contractuelle** (tu sais ce que tu as le droit de faire), et **traçable** (souvent via une clé qui t’identifie).

#### Quand préférer la lecture manuelle

- Quand le volume est petit (10-20 pages).
- Quand la source est sensible (forum spécialisé, presse engagée).
- Quand il faut interpréter le contenu, pas juste l’extraire.
- Quand l’automatisation présenterait un risque légal ou éthique.

#### Notion de « source autoritative »

Une **source autoritative**, c’est la source d’origine — celle qui a publié l’information en premier. Privilégier les sources autoritatives :

- évite la déformation,
- permet de citer correctement,
- limite la duplication de données.

Exemple : pour une mention d’entreprise, le registre officiel des entreprises est autoritatif. Un agrégateur tiers ne l’est pas.

### Bonus

#### L’écosystème OSINT au-delà de Python

Pour situer Python dans le paysage :

- **Maltego** : plateforme graphique de pivots OSINT.
- **SpiderFoot** : outil d’automatisation OSINT modulaire.
- **Recon-ng** : framework de reconnaissance en ligne de commande.

Ces outils existent et sont puissants. Apprendre à scripter en Python te donne quelque chose qu’ils n’ont pas : la flexibilité totale. Tu peux construire **exactement** ce dont tu as besoin, sans dépendance.

### ❌ Erreur classique

```
# Croire que "public" = "tout permis"
"Cette page est publique, donc je peux l’aspirer en boucle, vendre les
 données et en faire ce que je veux."
→ Faux. Le fait qu’une page soit accessible ne libère pas du droit
   applicable (CGU, RGPD, droits voisins, etc.).

# Sauter directement au scraping
"J’ai besoin des actualités de ce média, je vais scraper leur site."
→ Vérifie d’abord : ont-ils un flux RSS ? Une API ? Un sitemap ?
   Dans 80 % des cas, oui.

# Confondre OSINT et "espionnage en ligne"
"OSINT = trouver des trucs cachés sur les gens."
→ Non. OSINT = utiliser des sources publiques avec rigueur et éthique.
```

### Exercices

**Guidé :** Pour chacun des besoins suivants, dis quelle méthode est la plus appropriée (manuelle / API / RSS / sitemap / open data / scraping) et pourquoi :

1. Récupérer la météo de Paris pour les 7 prochains jours.
1. Surveiller les communiqués de presse d’une administration française.
1. Vérifier une information de CV à partir d’une page professionnelle publique fournie par la personne (lecture manuelle, sans automatisation).
1. Récupérer la liste des entreprises créées en 2024 en France.
1. Suivre les changements de tarification d’un concurrent.

**Autonome :** Choisis un sujet d’intérêt personnel (sport, jeu vidéo, actualité scientifique…) et :

1. Formule **une** question d’enquête claire en une phrase.
1. Liste 3 sources publiques pertinentes.
1. Pour chaque source, indique la méthode de collecte appropriée et justifie en 2 lignes.

### ✅ Tu sais maintenant…

- Distinguer OSINT, scraping, crawling, API et collecte manuelle
- Identifier les grands cas d’usage défensifs
- Choisir la méthode de collecte adaptée à un besoin
- La hiérarchie : manuel → API → RSS → sitemap/open data → scraping
- Ce que le scraping n’est **pas** (ni hacking, ni anonyme, ni stable)

-----


## Chapitre 2 — Cadre légal, éthique et OPSEC du scraping

> **Avertissement :** ce chapitre fournit des **repères**, pas un conseil juridique. Le droit applicable varie selon ton pays, ton statut (particulier, entreprise, journaliste, chercheur), la nature de la donnée et l’usage final. En cas de doute sur un projet réel, consulte un juriste.

### Le minimum à savoir

#### Les 5 questions à se poser avant de scraper

Avant chaque collecte, ce mini-questionnaire :

```
1. La source est-elle publiquement accessible
   sans authentification ni contournement ?

2. Les CGU autorisent-elles cet usage automatisé ?

3. Le robots.txt comporte-t-il des restrictions
   pertinentes pour ce que je veux faire ?

4. La donnée comporte-t-elle des éléments personnels ?
   Si oui, ma collecte respecte-t-elle le principe
   de minimisation et un cadre juridique clair ?

5. Si le site m’écrivait demain pour me demander
   pourquoi je collecte, ma réponse serait-elle solide ?
```

> **Important :** CGU et robots.txt sont **deux choses distinctes**. Les CGU sont un texte contractuel, le robots.txt est une convention technique. Ils doivent être vérifiés séparément. Un robots.txt permissif ne dispense pas de lire les CGU, et inversement.

Si tu réponds **NON** ou **« je ne sais pas »** à l’une de ces questions, **arrête** la collecte automatisée et documente le doute avant d’aller plus loin. En enquête sérieuse, un doute non levé se transcrit dans la fiche d’enquête : c’est une trace honnête, pas une faiblesse.

#### Données publiques ≠ données librement exploitables

C’est l’erreur la plus commune. Le fait qu’une donnée soit visible sans connexion ne signifie pas :

- qu’elle est libre de droits (un texte sur un blog reste protégé par le droit d’auteur),
- qu’elle peut être collectée massivement,
- qu’elle peut être republiée,
- qu’elle peut être traitée à des fins commerciales,
- qu’elle peut être croisée avec d’autres sources pour profiler des personnes.

**Une donnée publique reste soumise à un cadre.** Le scraping ne crée pas de droit ; il ne fait que techniquement automatiser une consultation.

#### Le fichier `robots.txt`

C’est un fichier texte placé à la racine d’un site (`https://exemple.fr/robots.txt`) dans lequel le propriétaire indique aux robots ce qu’il accepte d’être parcouru.

Exemple :

```
User-agent: *
Disallow: /admin/
Disallow: /api/private/
Allow: /
Crawl-delay: 5

Sitemap: https://exemple.fr/sitemap.xml
```

Lecture :

- `User-agent: *` → règles pour tous les robots.
- `Disallow: /admin/` → ne pas parcourir cette section.
- `Crawl-delay: 5` → attendre 5 secondes entre deux requêtes.
- `Sitemap:` → emplacement du plan du site (bonus pour toi !).

> **Important :** `robots.txt` est une **convention**, pas une loi. Le respecter n’est pas une obligation juridique stricte, mais le **bafouer** est un signal très net que ta démarche est problématique. En pratique : on respecte robots.txt.

#### Les CGU (Conditions Générales d’Utilisation)

Les CGU sont un **contrat** entre le service et toi. Beaucoup interdisent :

- l’accès automatisé,
- l’extraction massive,
- la réutilisation commerciale,
- la constitution de bases dérivées.

Lire les CGU avant de scraper professionnellement n’est pas optionnel. La portée juridique des CGU dépend de plusieurs facteurs (acceptation effective, position du droit local), mais leur violation peut t’exposer à des poursuites civiles, voire pénales selon le contexte.

#### Le RGPD en 5 principes (UE)

Si tu touches à des **données personnelles** (un nom, un email, une photo identifiable…), tu entres dans le périmètre du RGPD. Cinq principes à retenir :

1. **Finalité** : tu dois savoir pour quoi tu collectes, et le dire clairement.
1. **Minimisation** : tu collectes le strict nécessaire.
1. **Base légale** : tu dois pouvoir justifier ta collecte (intérêt légitime, mission d’intérêt public, etc.).
1. **Conservation limitée** : tu ne gardes pas indéfiniment.
1. **Droits des personnes** : la personne peut demander accès, rectification, suppression.

Pour un projet OSINT défensif sérieux qui touche des données personnelles, un **registre des traitements** simplifié est une bonne pratique.

#### Ce qu’on ne fait **jamais**

- Contourner une authentification.
- Utiliser un compte qui n’est pas le sien.
- Exploiter une faille technique (CAPTCHA bypass, exploitation d’une vulnérabilité).
- Scraper massivement des données personnelles pour profilage commercial.
- Republier des contenus protégés sans autorisation.
- Surcharger un site (assimilable à un déni de service).
- Constituer des listes de prospection à partir d’emails moissonnés.

### Très utile en pratique

#### Le principe de minimisation, en action

Tu surveilles un blog d’expert pour de la veille. La minimisation, c’est :

- ❌ Aspirer tout le blog tous les jours pour tout garder.
- ✅ Récupérer la liste des nouveaux articles publiés depuis ta dernière collecte.

Tu surveilles les annonces d’embauche d’un concurrent. La minimisation, c’est :

- ❌ Stocker le profil complet de chaque candidat mentionné.
- ✅ Stocker uniquement intitulé du poste, date de publication et URL.

#### La traçabilité, en pratique

Chaque enregistrement de ta collecte doit contenir, au minimum :

|Champ         |Exemple                         |
|--------------|--------------------------------|
|`source_url`  |`https://exemple.fr/article/123`|
|`collected_at`|`2026-05-17T14:32:11Z`          |
|`tool`        |`mon-collecteur/0.3.1`          |
|`status_code` |`200`                           |
|`content_hash`|`a3f5...` (SHA-256 du HTML brut)|

Ces métadonnées sont **non négociables**. Sans elles, ta collecte n’est pas reproductible et n’a aucune valeur d’enquête.

#### Identifier honnêtement ton script

Quand tu envoies une requête, le serveur reçoit un header `User-Agent`. Par défaut, `requests` envoie quelque chose comme `python-requests/2.31.0`. C’est honnête, mais peu informatif.

**Bonne pratique** : un User-Agent identifiable, qui dit qui tu es et comment te contacter en cas de problème :

```
MonOutilOSINT/0.1 (+contact: osint-projet@example.org)
```

> **OPSEC :** utilise idéalement une adresse **dédiée au projet** (ex. `osint-veille@<ton-domaine>`, un alias, ou une boîte spécifique), **pas** ton adresse personnelle principale. Si quelqu’un veut te recontacter ou te signaler un problème, c’est très bien. Si l’adresse fuit dans des dumps, des spams ou des listes, tu veux que ce soit l’alias projet, pas ta boîte principale.

**Mauvaise pratique** : se faire passer pour un navigateur récent pour échapper aux filtres anti-bot. Sauf cas pédagogique très balisé, c’est un signal d’intention douteuse.

#### Charte personnelle de l’analyste OSINT

Voici un modèle, à adapter et signer (au sens : à t’engager intérieurement à respecter) :

```
1. Je collecte des données publiques pour des finalités défensives,
   de veille, de recherche ou de transparence.
2. Je respecte robots.txt et les CGU des sites que je consulte.
3. Je collecte le minimum nécessaire à ma question d’enquête.
4. Je trace systématiquement la source, la date et la méthode.
5. Je ne contourne aucune protection technique.
6. Je n’utilise pas mes outils contre des personnes physiques
   sans cadre légal explicite (mission, mandat, ordre légitime).
7. Je ne republie pas de données protégées sans autorisation.
8. Je respecte le rythme des serveurs (rate limit volontaire).
9. Je m’identifie honnêtement (User-Agent, contact).
10. En cas de doute, je m’arrête et je consulte.
```

### ❌ Erreur classique

```
# Croire que robots.txt protège juridiquement
"Le site a un robots.txt qui interdit le scraping, donc je m’expose
 à des poursuites si je passe outre."
→ Pas si simple. robots.txt est une convention, pas un dispositif
   contractuel. Mais l’ignorer est un signal fort de mauvaise foi
   qui pèsera lourd si un litige survient.

# Croire que l’absence de robots.txt = autorisation
"Pas de robots.txt, donc je peux tout faire."
→ Faux. Les CGU s’appliquent, le droit d’auteur s’applique, le RGPD
   s’applique. robots.txt n’est qu’un signal additionnel.

# Tester le scraper agressif directement sur la cible
"Je veux voir à partir de combien de requêtes le site bloque."
→ Ne fais jamais ça. Tu peux dégrader un service public, exposer
   ton IP, et déclencher des procédures de sécurité automatiques.
   Pour tester un scraper, utilise des sites bac à sable
   (toscrape.com, httpbin.org).

# Confondre "données accessibles" et "données librement réutilisables"
"Cet article de presse est lisible sans abonnement, je peux le
 republier sur mon site."
→ Faux. Le droit d’auteur s’applique indépendamment du paywall.
```

### Bonus

#### Affaires juridiques de référence (à titre culturel)

> Ces affaires sont citées **à titre indicatif**. Elles évoluent, leurs conclusions ne sont pas transposables tel quel à ton cas. Pour un projet réel, vérifie l’état du droit avec un juriste.

- **hiQ Labs vs LinkedIn (États-Unis)** : longue bataille judiciaire sur le scraping de profils publics, illustrant la complexité du « public » en pratique.
- **Ryanair vs PR Aviation (UE)** : a précisé que les CGU peuvent restreindre l’usage automatisé même si les données ne sont pas protégées par un droit sui generis.
- **Décisions CNIL** : sanctions répétées sur des moissonnages d’emails à des fins commerciales.

L’annexe C de ce cours liste des ressources pour aller plus loin.

### Exercices

**Guidé :** Récupère manuellement (dans ton navigateur) les fichiers `robots.txt` de trois sites de natures différentes :

1. un grand média (ex. `lemonde.fr/robots.txt`),
1. une administration publique (ex. `service-public.fr/robots.txt`),
1. un site bac à sable (`books.toscrape.com/robots.txt`).

Pour chacun, identifie :

- les sections interdites (`Disallow`),
- la présence éventuelle d’un `Crawl-delay`,
- la présence d’un `Sitemap`.

**Autonome :** Rédige ta propre charte OSINT en 10 règles maximum. Garde-la dans `config/charte.md` à la racine de ton projet. C’est un engagement, pas une décoration.

### ✅ Tu sais maintenant…

- Les 5 questions préalables à toute collecte
- Que « données publiques » ne signifie pas « données librement exploitables »
- Lire et interpréter un `robots.txt`
- Les 5 principes RGPD applicables aux données personnelles
- Ce qu’on ne fait jamais
- Identifier honnêtement son script via User-Agent
- Tenir un cadre éthique personnel

-----


## Chapitre 3 — Comment fonctionne le web (vu côté collecteur)

Avant de coder une requête, il faut comprendre **ce qu’on demande, à qui, et ce qu’on récupère**. Ce chapitre est volontairement dense — c’est le socle technique de tout ce qui suit.

### Le minimum à savoir

#### Le modèle client / serveur

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

#### Anatomie d’une URL

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

#### HTTPS vs HTTP

**HTTPS** chiffre la communication entre toi et le serveur. **HTTP** la laisse en clair. Aujourd’hui, presque tous les sites sont en HTTPS.

Pour un scraper, ça change peu — `requests` gère HTTPS de manière transparente. Mais à savoir : HTTPS protège **le contenu**, pas l’identité (le serveur sait toujours qui tu es par ton IP).

#### Une requête HTTP en détail

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

#### Les méthodes HTTP

Tu en croiseras surtout deux :

|Méthode |Sens                           |Quand                                        |
|--------|-------------------------------|---------------------------------------------|
|**GET** |« Donne-moi cette ressource »  |Lecture. C’est 95 % de ce qu’un scraper fait.|
|**POST**|« Voici des données à traiter »|Envoi de formulaire, création de ressource.  |

Les autres (`PUT`, `DELETE`, `HEAD`, `OPTIONS`) existent, mais sont rares en OSINT défensif.

#### Les codes de statut

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

#### Les headers importants

|Header                    |Rôle                                                        |
|--------------------------|------------------------------------------------------------|
|`User-Agent`              |Dit qui fait la requête.                                    |
|`Accept`                  |Types de contenu acceptés (`text/html`, `application/json`).|
|`Accept-Language`         |Langues préférées.                                          |
|`Referer`                 |D’où vient la requête (page précédente).                    |
|`Cookie`                  |Données de session côté client.                             |
|`Content-Type` (réponse)  |Format du corps renvoyé.                                    |
|`Content-Length` (réponse)|Taille du corps.                                            |

#### HTML, balises, attributs

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

#### Le DOM : l’arbre des éléments

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

#### Les sélecteurs CSS

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

#### Site statique vs site dynamique

|Type         |Comment ça marche                                                                                   |Conséquence pour le scraping                                 |
|-------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
|**Statique** |Le serveur envoie directement le HTML final.                                                        |`requests` reçoit ce que tu vois. Facile à scraper.          |
|**Dynamique**|Le serveur envoie un squelette + du JavaScript. Le navigateur exécute le JS pour construire la page.|`requests` ne reçoit **que** le squelette. Le contenu manque.|

**Comment savoir ?** Dans ton navigateur, ouvre la page, fais clic droit → **« Afficher le code source »** (pas « Inspecter »). Si tu vois le texte qui t’intéresse dans le code source brut, c’est statique. Sinon, c’est dynamique et `requests` ne suffira pas.

> **À retenir :** pour les sites dynamiques, on commence **toujours** par chercher la source plus propre (API, RSS, sitemap). Les outils de pilotage de navigateur (Playwright, Selenium) sont un **dernier recours** dans un cadre autorisé.

#### Les DevTools du navigateur

Apprends à utiliser les outils de développement de ton navigateur (F12 ou clic droit → « Inspecter ») :

|Onglet                      |À quoi ça sert                                                                                            |
|----------------------------|----------------------------------------------------------------------------------------------------------|
|**Elements** (ou Inspecteur)|Voir et explorer le DOM, identifier les sélecteurs.                                                       |
|**Network** (ou Réseau)     |Voir toutes les requêtes que la page fait. Indispensable pour repérer un endpoint JSON appelé par la page.|
|**Console**                 |Tester des sélecteurs, lire les erreurs JS.                                                               |


> **Méthode** : sur la page, clic droit sur l’élément qui t’intéresse → « Inspecter ». Le DOM s’ouvre exactement sur ce nœud. Tu peux y lire la classe, l’id, la hiérarchie. C’est comme ça qu’on construit un sélecteur CSS fiable.

### Très utile en pratique

#### Reconnaître un site dynamique en 30 secondes

1. Ouvre la page dans ton navigateur.
1. Clic droit → « Afficher le code source » (Ctrl+U).
1. Ctrl+F → cherche un mot que tu vois à l’écran.
1. Trouvé ? → Statique. Pas trouvé ? → Dynamique.

C’est la première chose à faire avant d’écrire le moindre scraper.

#### Identifier un endpoint JSON publiquement appelé par la page

Beaucoup de sites « dynamiques » récupèrent leurs données en appelant une URL JSON depuis le navigateur. C’est souvent **bien plus propre à exploiter** que le HTML rendu.

1. Ouvre les DevTools (F12) → onglet **Network**.
1. Recharge la page.
1. Filtre sur **XHR** ou **Fetch**.
1. Repère les réponses en JSON.
1. Clique → onglet **Response** → tu vois la donnée brute.

Si tu trouves un endpoint qui sert exactement ce qui t’intéresse, **change de stratégie** : interroge cet endpoint directement (chapitre 11), c’est plus stable et plus propre que de scraper le HTML rendu.

> **Vocabulaire :** on ne parle pas d’« API cachée ». L’endpoint est appelé en clair par la page que tu visites — il est publiquement observable. On parle simplement de **l’endpoint JSON appelé par la page**.

#### Pourquoi un scraper casse

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

### ❌ Erreur classique

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

### Bonus

#### Les en-têtes de sécurité (culture générale)

Tu croiseras parfois des headers comme :

- `Content-Security-Policy` (CSP)
- `Strict-Transport-Security` (HSTS)
- `X-Frame-Options`

Ce sont des mécanismes de **défense du site**, qui n’affectent pas directement le scraping en lecture, mais qui te donnent une indication sur le sérieux de l’hébergeur.

#### Cookies et sessions

Un cookie est un petit fichier que le serveur demande au client de garder. À la requête suivante, le client renvoie ce cookie, ce qui permet au serveur de « reconnaître » la session.

En OSINT défensif, on touche peu aux cookies — on travaille sur des contenus accessibles **sans session**. Si une donnée nécessite d’être connecté pour être vue, c’est qu’elle n’est pas vraiment publique.

### Exercices

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

### ✅ Tu sais maintenant…

- Décomposer une URL et lire ses parties
- Le modèle requête/réponse HTTP
- Les principaux codes de statut (200, 301, 403, 404, 429, 500)
- Les headers utiles (`User-Agent`, `Accept`, etc.)
- Lire un arbre HTML et utiliser les sélecteurs CSS
- Distinguer site statique et site dynamique en 30 secondes
- Repérer un endpoint JSON appelé par la page via les DevTools
- Anticiper les causes typiques de casse d’un scraper

-----


## Chapitre 4 — Choisir la source la plus propre

Avant d’écrire ton premier scraper, **un dernier réflexe à intégrer** : chercher systématiquement la source la plus propre. C’est ce qui transforme un script jetable en démarche d’enquête durable.

### Le minimum à savoir

#### La hiérarchie des sources

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

#### Pourquoi cet ordre ?

|Critère                  |API      |RSS          |Sitemap |Open data|Scraping     |
|-------------------------|---------|-------------|--------|---------|-------------|
|Prévu pour les programmes|✅        |✅            |✅       |✅        |❌            |
|Stable dans le temps     |🟢        |🟢            |🟢       |🟢        |🔴            |
|Charge serveur           |🟢 Faible |🟢 Faible     |🟢 Faible|🟢 Faible |🔴 Plus lourde|
|Cadre légal clair        |🟢 CGU API|🟢            |🟢       |🟢 Licence|🟡 Flou       |
|Effort de développement  |🟡 Moyen  |🟢 Très faible|🟢 Faible|🟢 Faible |🔴 Élevé      |

À chaque ligne, le scraping perd. Ce n’est pas un hasard si on le place en dernier.

#### Reconnaître une API

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

#### Reconnaître un flux RSS / Atom

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

#### Reconnaître un sitemap XML

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

#### Reconnaître un dataset open data

Les administrations, ONG, institutions de recherche publient leurs données en accès libre, souvent en CSV, JSON ou API dédiée.

Portails à connaître :

- **France** : `data.gouv.fr`
- **Union européenne** : `data.europa.eu`
- **International** : `data.worldbank.org`, `data.un.org`
- **Recherche** : Zenodo, OpenAIRE

Pour un sujet donné, avant de scraper : **vérifie qu’un dataset open data n’existe pas déjà**. Tu gagnes du temps et tu obtiens des données autoritatives.

#### Quand le scraping est-il justifié ?

|Situation                                                                                            |Justifié ?                             |
|-----------------------------------------------------------------------------------------------------|---------------------------------------|
|Le site n’a ni API, ni RSS, ni sitemap, ni open data, et l’information est essentielle à ton enquête.|✅                                      |
|Le site a une API mais elle ne couvre pas l’info que tu cherches.                                    |✅ (raisonnable)                        |
|Le site a un RSS mais tu trouves le scraping « plus pratique ».                                      |❌                                      |
|Tu veux scraper « pour t’entraîner ».                                                                |✅ uniquement sur des sites bac à sable.|

### Très utile en pratique

#### Méthode en 5 étapes pour choisir la bonne source

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

#### Cas d’usage classés

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

### ❌ Erreur classique

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

### Bonus

#### Parser un flux RSS rapidement

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

#### Lire un sitemap

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

### Exercices

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

### 🧩 Mini-projet de Partie I — *Fiche d’enquête*

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

### ✅ Tu sais maintenant…

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
