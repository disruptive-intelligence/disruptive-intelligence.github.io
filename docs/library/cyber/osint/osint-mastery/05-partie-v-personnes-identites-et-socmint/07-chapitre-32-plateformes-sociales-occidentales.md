---
title: Chapitre 32 — Plateformes sociales occidentales
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE V — Personnes, identités et SOCMINT
  - index.md
---

## 32.1 Pourquoi un chapitre par plateforme

Chaque plateforme a sa logique, ses limites, ses sources, ses outils. Une méthodologie générale (Ch.31) ne suffit pas. Maîtriser le SOCMINT implique de connaître plateforme par plateforme.

Ce chapitre couvre les **plateformes occidentales majeures** en 2026. Telegram, Discord, et plateformes alternatives sont traités séparément (Ch.33-34).

## 32.2 LinkedIn

**Usage OSINT.** Vérification d'identité et de parcours, due diligence, recherche d'experts, cartographie d'organisations.

**Forces.**

- Profils enrichis, généralement véridiques.
- Cartographie d'organisations (qui travaille où).
- Network effects visibles (qui connaît qui).
- Recommandations (signaux qualitatifs).

**Méthode.**

- Recherche directe (compte d'investigation mature).
- **Sales Navigator** pour recherches avancées (filtres profession, école, ancienneté).
- **PhantomBuster** pour automatisation légère (attention CGU et suspension).
- Google `site:linkedin.com/in/` pour recherche externe.
- Bing aussi indexe LinkedIn.

**Limites 2026.**

- Pas d'API publique.
- Détection agressive des bots.
- CGU strictes contre scraping.
- Profils en mode privé non visibles.

**Stratégie.** Compte d'investigation mature, observation discrète, captures Hunchly, pas d'interaction sans nécessité.

## 32.3 Facebook

**Usage OSINT.** Sphère personnelle, événements, groupes, photos.

**Forces.**

- Volume d'informations personnelles élevé (mais en baisse depuis 2018).
- Groupes thématiques riches.
- Marketplace pour activité commerciale informelle.
- Events.

**Méthode.**

- Recherche directe (compte invest, attention restrictions).
- Recherche par nom + ville / employeur.
- **Sowsearch** (sowsearch.info, en évolution) : Facebook search avec UI dédiée.
- **Meta Content Library** (DSA art. 40) si statut chercheur.
- Search graph (recherche par interactions).

**Limites 2026.**

- Restrictions fortes sur recherches.
- Profils en mode privé très protégés.
- CrowdTangle fermé (cf. Ch.24).
- Photos sans EXIF (stripping à l'upload).

## 32.4 Instagram

**Usage OSINT.** Visuel, géolocalisation, lifestyle.

**Forces.**

- Photos riches en signaux (lieux, train de vie, cercles).
- Stories (éphémères mais capturables).
- Stories highlights (persistantes).
- Tag de localisation.
- Mentions et tags.

**Méthode.**

- Compte invest (Meta).
- Recherche par hashtag, lieu, mention.
- Suivi de cercles (followings, followers).
- Captures Hunchly pour préserver.
- **InstaLoader** (open source, Python) pour download conforme.

**Limites.**

- Restrictions API.
- Stories disparaissent.
- Comptes privés non visibles aux non-followers.

## 32.5 X (Twitter)

**Usage OSINT.** Expression publique, débat, breaking news, opérations d'influence.

**Forces.**

- Volume massif d'expressions.
- Plateforme de désinformation et d'influence.
- Métadonnées riches (geo si activé, timing précis).
- Trends en temps réel.

**Méthode 2026.**

- Compte d'investigation pour consultation directe.
- **X API Basic** ($100/mois) pour besoins ciblés.
- **X API Pro** ($5000/mois) pour gros usage.
- Archivage anticipé (Wayback + archive.today).
- Recherche via Google `site:twitter.com` ou `site:x.com`.

**Limites massives.** Voir Ch.24.

## 32.6 TikTok

**Usage OSINT.** Investigation contemporaine sur publics jeunes, viralité, désinformation visuelle.

**Forces.**

- Volume de vidéos courtes.
- Algorithme révélateur (For You Page).
- Géolocalisation par hashtag et son.

**Méthode.**

- Compte invest.
- **TikTok Research API** (chercheurs académiques EU/US agréés).
- Outils tiers payants (Brandwatch).
- yt-dlp pour téléchargement.

**Limites.**

- API restrictive.
- Pas de timeline historique facile.
- Algorithme opaque.

## 32.7 YouTube

**Usage OSINT.** Vidéos publiques, chaînes, commentaires, transcripts.

**Forces.**

- Archive vidéo massive.
- Transcripts automatiques (utilisables pour recherche full-text).
- Commentaires (sources d'expression).
- YouTube Data Viewer (Amnesty) pour extraction métadonnées.

**Méthode.**

- **YouTube Data API v3** : gratuit avec quota.
- **yt-dlp** pour download.
- **YouTube Data Viewer** (Amnesty International) pour metadata d'une vidéo.
- Recherche par chaîne, par mot-clé, par date.

**Limites.**

- Suppression possible des vidéos.
- Modération content.
- Limites de quota API.

## 32.8 Reddit

**Usage OSINT.** Communautés thématiques, discussions, fuites informelles.

**Forces.**

- Communautés riches (subreddits).
- Discussions approfondies.
- Archive historique (avant fermeture Pushshift).

**Méthode 2026.**

- **Reddit API officielle** (payante depuis 2023).
- **undelete.pullpush** (mirror partiel).
- Recherche Google `site:reddit.com`.
- **PRAW** (Python Reddit API Wrapper) avec API officielle.

**Limites.**

- Fermeture Pushshift = perte d'archives historiques.
- API payante.

## 32.9 Threads

**Usage OSINT.** Émergente, écosystème lié à Instagram.

**Forces.**

- Croissance rapide depuis 2023.
- Authentification via Instagram (cross-plateforme natif).
- Mode public majoritaire.

**Méthode.**

- Compte invest (lié Instagram).
- Pas d'API publique au lancement, en évolution.
- Captures manuelles.

## 32.10 Bluesky et Mastodon

**Bluesky.** Protocole AT, plus ouvert que X. API publique. Cible des analystes en quête d'alternative à X.

**Mastodon.** Fédéré, protocole ActivityPub. Très ouvert. Outils OSINT en émergence (Magnifying.glass, Garlic.io).

**Méthode.**

- API ouvertes : automatisation possible.
- Captures simples.
- Mais volume encore limité (vs X).

## 32.11 Synthèse plateformes occidentales

| Plateforme | Difficulté | Outils principaux | Stratégie 2026 |
|---|---|---|---|
| LinkedIn | Très haute | Sales Nav, compte invest | Maturation + Hunchly |
| Facebook | Très haute | Compte invest, MCL | Captures, archivage |
| Instagram | Très haute | Compte invest, InstaLoader | Captures stories urgentes |
| X | Très haute | API payante, compte invest | Archivage anticipé |
| TikTok | Très haute | Research API, compte invest | Captures, outils payants |
| YouTube | Moyenne | API, yt-dlp | Volume gérable |
| Reddit | Haute | API payante, Google site: | Reconstruction historique limitée |
| Threads | Faible-moyenne | Compte invest | Émergent |
| Bluesky | Faible | API ouverte | Confortable |
| Mastodon | Faible | API ActivityPub | Très ouvert |

> **MIRAGE — Épisode 6 : SOCMINT multi-plateformes**
>
> L'analyste mène la cartographie SOCMINT autour de Delaunay.
>
> **LinkedIn** : profil professionnel accessible via Camille Roux (avatar du cabinet). Parcours confirmé, 487 contacts, 23 recommandations, 4 posts publiés sur 5 ans (sobre, surtout repartages presse industrielle). Pas d'élément critique. Capture Hunchly.
>
> **Facebook** : un compte au nom de Marc Delaunay, photo de profil correspondante, mode privé. Aucun contenu public visible. Liste d'amis non accessible. Note dans la fiche.
>
> **Instagram** (sous username `mdelaunay76`) : compte privé, photo silhouette. Aucune story / post public. Pas exploitable directement.
>
> **X / Twitter** (`@mdelaunay76`) : compte verrouillé. Quelques retweets publics datant de 2014-2017 (sport, finance). Aucun contenu récent visible. Faible.
>
> **TikTok** : aucun compte identifié.
>
> **YouTube** : la vidéo interview 2023 (TechnoVert) est confirmée. Pas d'autres apparitions de Delaunay.
>
> **Reddit** : recherche `mdelaunay76` ne retourne aucun compte significatif.
>
> **Bluesky, Mastodon** : absence.
>
> **Conclusion SOCMINT** : Delaunay a une faible empreinte volontaire sur les réseaux sociaux. Stratégie OPSEC personnelle robuste. Les pivots SOCMINT sont limités pour Delaunay personnellement.
>
> **Bascule sur le volet désinformation** : le cluster des faux comptes amplifiant la diffamation contre Berthier sera l'objet du gros du SOCMINT. La recherche s'oriente vers l'identification de ces comptes, leur activité, leurs liens — sujet qui sera développé en MIRAGE 17 (Ch.76 désinformation).

-----
