---
title: Chapitre 1 — Qu’est-ce que l’OSINT et le web scraping ?
source: Cyber/02_OSINT/Python_Scraping.md
note: Python & scraping
up:
- - Python & scraping
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## Le minimum à savoir

### Définitions, clairement

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

### Tableau comparatif

|Approche               |Vitesse |Stabilité    |Légitimité             |Quand l’utiliser                                            |
|-----------------------|--------|-------------|-----------------------|------------------------------------------------------------|
|**Manuel**             |⚪ Lent  |🟢 Très stable|🟢 Toujours OK          |Vérification, faibles volumes, sources sensibles            |
|**API**                |🟢 Rapide|🟢 Très stable|🟢 Cadre clair (CGU API)|Dès qu’elle existe — c’est presque toujours la bonne réponse|
|**Flux RSS / Atom**    |🟢 Rapide|🟢 Stable     |🟢 Prévu pour ça        |Veille d’actualités, blogs, publications régulières         |
|**Sitemap / open data**|🟢 Rapide|🟢 Stable     |🟢 Prévu pour ça        |Inventaire d’un site, datasets publics                      |
|**Scraping**           |🟡 Moyen |🔴 Fragile    |🟡 Cadre flou           |Dernier recours, quand rien d’autre n’existe                |

### La pyramide de la collecte OSINT

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

### Cas d’usage défensifs typiques

|Domaine                   |Exemple concret                                                                            |
|--------------------------|-------------------------------------------------------------------------------------------|
|**CTI**                   |Suivre les bulletins publics d’un éditeur de logiciels pour repérer les CVE critiques.     |
|**Brand protection**      |Surveiller la création de domaines proches de ta marque (typosquatting).                   |
|**Veille concurrentielle**|Suivre les annonces d’embauche d’un concurrent pour détecter une réorientation stratégique.|
|**Journalisme**           |Vérifier des prises de position publiques d’un acteur sur plusieurs années.                |
|**Recherche académique**  |Constituer un corpus de publications scientifiques d’un domaine.                           |
|**Transparence publique** |Suivre les modifications d’un règlement gouvernemental.                                    |
|**Sécurité de marque**    |Repérer les copies frauduleuses d’un site officiel.                                        |

### Ce que le scraping **n’est pas**

- **Ce n’est pas du hacking.** Tu accèdes à la même chose qu’un navigateur — tu n’exploites aucune faille.
- **Ce n’est pas une autorisation universelle.** Le fait qu’une page soit publique ne signifie pas que tu peux l’aspirer en masse.
- **Ce n’est pas magique.** Si le site change son HTML demain, ton script casse.
- **Ce n’est pas anonyme.** Chaque requête laisse une trace dans les logs du serveur cible : IP, User-Agent, horodatage, URL.

## Très utile en pratique

### Quand préférer une API à un scraper

Toujours, quand :

- l’API existe et donne accès aux données qui t’intéressent,
- les CGU de l’API t’autorisent ton usage,
- les rate limits sont compatibles avec ton volume.

L’API est **stable** (le site peut changer son HTML, l’API change rarement), **rapide**, **contractuelle** (tu sais ce que tu as le droit de faire), et **traçable** (souvent via une clé qui t’identifie).

### Quand préférer la lecture manuelle

- Quand le volume est petit (10-20 pages).
- Quand la source est sensible (forum spécialisé, presse engagée).
- Quand il faut interpréter le contenu, pas juste l’extraire.
- Quand l’automatisation présenterait un risque légal ou éthique.

### Notion de « source autoritative »

Une **source autoritative**, c’est la source d’origine — celle qui a publié l’information en premier. Privilégier les sources autoritatives :

- évite la déformation,
- permet de citer correctement,
- limite la duplication de données.

Exemple : pour une mention d’entreprise, le registre officiel des entreprises est autoritatif. Un agrégateur tiers ne l’est pas.

## Bonus

### L’écosystème OSINT au-delà de Python

Pour situer Python dans le paysage :

- **Maltego** : plateforme graphique de pivots OSINT.
- **SpiderFoot** : outil d’automatisation OSINT modulaire.
- **Recon-ng** : framework de reconnaissance en ligne de commande.

Ces outils existent et sont puissants. Apprendre à scripter en Python te donne quelque chose qu’ils n’ont pas : la flexibilité totale. Tu peux construire **exactement** ce dont tu as besoin, sans dépendance.

## ❌ Erreur classique

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


## Exercices

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

## ✅ Tu sais maintenant…

- Distinguer OSINT, scraping, crawling, API et collecte manuelle
- Identifier les grands cas d’usage défensifs
- Choisir la méthode de collecte adaptée à un besoin
- La hiérarchie : manuel → API → RSS → sitemap/open data → scraping
- Ce que le scraping n’est **pas** (ni hacking, ni anonyme, ni stable)

-----
