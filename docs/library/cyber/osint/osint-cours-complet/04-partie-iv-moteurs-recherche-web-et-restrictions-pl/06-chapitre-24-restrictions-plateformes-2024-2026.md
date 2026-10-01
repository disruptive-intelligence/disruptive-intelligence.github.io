---
title: Chapitre 24 — Restrictions plateformes 2024-2026
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE IV — Moteurs, recherche web et restrictions plateformes
  - index.md
---

## 24.1 La grande fermeture

Entre 2022 et 2026, les grandes plateformes ont progressivement **fermé** l'accès libre à leurs données pour les chercheurs, journalistes et investigateurs OSINT. C'est l'une des transformations les plus importantes du métier.

Causes principales : (1) modèles économiques fondés sur l'accès payant aux données, (2) protection légale (RGPD, DSA), (3) compétition avec les LLMs (les plateformes craignent l'aspiration de leurs données pour entraînement IA), (4) durcissement vis-à-vis des outils tiers perçus comme parasites.

Conséquence : l'OSINT 2026 doit s'adapter à un paysage de plateformes hostiles ou semi-hostiles.

## 24.2 X (Twitter) : la rupture la plus brutale

**X** (anciennement Twitter, racheté par Elon Musk en octobre 2022) est le cas d'école.

**Restrictions imposées 2023-2026.**

- API gratuite supprimée (mars 2023).
- API payante à partir de $100/mois (basic), $5000/mois (pro), entreprise sur devis.
- Limitation drastique des résultats par requête.
- Suppression de la consultation déconnectée pour de nombreux contenus.
- Dégradation puis fermeture de Nitter (alternative non-officielle).
- Removal de l'export TweetDeck classique.

**Impact OSINT.**

- Twint, snscrape (anciennement utilisés) : largement inopérants.
- TweetBeaver, Tweetdeck : dégradés.
- Recherche historique très limitée sans API payante.
- Beaucoup d'investigateurs ont basculé vers une combinaison : compte d'investigation actif + archivage anticipé + outils payants ciblés.

**Stratégies 2026.**

- Compte d'investigation maturé pour consultation directe.
- Archivage anticipé systématique (Wayback + archive.today).
- API payante pour besoins ponctuels (basic à $100/mois supportable).
- Outils tiers payants : Brandwatch, Talkwalker, Meltwater pour cas pro.
- Recherche via Bing/Google avec `site:twitter.com` (couverture partielle mais utile).

## 24.3 Meta (Facebook, Instagram, Threads)

**Meta** a verrouillé son écosystème.

**Restrictions.**

- Graph API restreinte aux applications agréées.
- CrowdTangle (outil journalistique vital) fermé en août 2024 (rapatrié partiellement en Meta Content Library).
- Recherche par mot-clé sur Facebook quasi-impossible sans compte connecté.
- Stories Instagram : disparition après 24h sans archivage.
- Threads : API non publique au lancement.

**Impact OSINT.**

- Meta Content Library (depuis 2024) remplace partiellement CrowdTangle mais avec accès restreint (chercheurs agréés DSA art. 40).
- Outils tiers (Sowsearch, etc.) : largement obsolètes.
- Investigation passive uniquement, via compte d'investigation.

**Stratégies 2026.**

- Comptes Facebook/Instagram d'investigation maturés.
- Demande d'accès Meta Content Library si statut chercheur DSA.
- Archivage immédiat de tout contenu d'intérêt (stories surtout).
- Bing image search sur Instagram (couverture partielle).

## 24.4 LinkedIn : forteresse

**LinkedIn** (Microsoft) est probablement la plateforme la plus restrictive.

**Restrictions.**

- Pas d'API publique pour observation tiers (uniquement applications Sales Navigator agréées).
- Sales Navigator coûteux ($79-150/mois).
- Limite stricte aux profils consultables par compte.
- Détection agressive des comptes d'investigation (suspension fréquente).
- CGU explicitement contre le scraping.

**Jurisprudence US.** L'affaire **hiQ Labs v. LinkedIn** (2022 SCOTUS) a établi que le scraping de données **publiques** ne viole pas le CFAA — mais reste contractuellement risqué (CGU). Pas de précédent équivalent UE.

**Stratégies 2026.**

- Comptes d'investigation matures (3-6 mois min).
- Sales Navigator pour les cabinets avec budget.
- Phantombuster (outil tiers payant) pour automatisation modérée — risque suspension.
- Combinaison consultation passive + Google `site:linkedin.com/in/` pour recherche externe.

## 24.5 Reddit : la fermeture API 2023

**Reddit** a fermé son API gratuite en juin 2023, après une crise majeure (suppressions d'outils tiers populaires comme Apollo).

**Restrictions.**

- API payante à partir de $0.24 / 1000 calls (élevé).
- Apollo, RIF, BaconReader : fermés.
- Pushshift (archive Reddit historique vitale) : fermé pour public.
- Camas (UI Pushshift) : non maintenu.

**Stratégies 2026.**

- API officielle payante pour usage pro.
- undelete.pullpush (mirror partiel Pushshift) : utile mais limité.
- Recherche Google `site:reddit.com` pour découverte.
- Archivage manuel de threads critiques.

## 24.6 Google : dégradation progressive

**Google** lui-même a dégradé son service de recherche.

**Restrictions.**

- Opérateurs avancés (cf. Ch.20) : silencieusement ignorés ou dégradés.
- Cache : largement retiré.
- Image search Reverse : moins puissant que Yandex.
- Personnalisation forte (deux utilisateurs voient des résultats différents).
- CAPTCHA fréquent pour requêtes complexes.

**Stratégies.**

- Multi-moteurs systématique (Bing, Yandex, Brave, Mojeek).
- Tools alternatifs (SearXNG instances).
- API Google Custom Search pour automatisation (payante, $5/1000 queries).

## 24.7 TikTok : opacité

**TikTok** propose peu d'accès officiel.

**Restrictions.**

- TikTok Research API (depuis 2023) : restreinte aux chercheurs académiques agréés EU/US.
- Pas de scraping autorisé.
- Détection forte des comptes anormaux.

**Stratégies 2026.**

- Comptes d'investigation.
- Outils tiers payants (Brandwatch, Talkwalker — équivalents).
- Recherche directe via tags et profils.

## 24.8 Telegram : encore relativement ouvert

**Telegram** reste relativement accessible mais la dynamique change.

**Évolution post-Durov 2024.** Arrestation de Pavel Durov en France (août 2024) a déclenché des évolutions : coopération avec autorités françaises et autres LEA, modération renforcée, partage d'IP pour requêtes pénales graves.

**Restrictions.**

- API utilisable mais limites rate.
- Channels privés non accessibles sans invitation.
- Bots Telegram pour interaction (avec limites).

**Stratégies 2026.**

- API Telethon / Pyrogram pour automatisation conforme.
- Compte d'investigation pour observation.
- Outils dédiés (TGStat, Telemetr.io, Lyzem).

## 24.9 GitHub, GitLab : encore ouverts

**GitHub** et **GitLab** restent globalement accessibles pour recherche publique.

**Restrictions.**

- Rate limits sur API.
- Detection scraping agressif.
- Compte requis pour la plupart des features avancées.

**Bonne pratique.** Token API personnel pour rate limits raisonnables.

## 24.10 Synthèse — niveau de difficulté par plateforme

| Plateforme | Difficulté 2026 | Solution principale |
|---|---|---|
| X (Twitter) | Très haute | API payante + archivage + compte invest |
| Facebook / Instagram | Très haute | Meta Content Library (si chercheur) + compte invest |
| LinkedIn | Très haute | Sales Navigator + compte invest |
| Reddit | Haute | API payante + Google site: |
| Google search | Moyenne | Multi-moteurs |
| TikTok | Très haute | Compte invest + outils payants |
| Telegram | Moyenne | API Telethon + compte invest |
| GitHub / GitLab | Faible | Token API |
| YouTube | Moyenne | yt-dlp + API officielle |
| Bluesky | Faible | API ouverte |
| Mastodon | Faible | Federated, ouvert |

## 24.11 Tendance à anticiper : l'IA accélère la fermeture

Les LLMs scrapent massivement le web pour entraînement. Les plateformes réagissent en se fermant (Reddit cite explicitement la pression IA dans sa décision API 2023). La tendance est à la **fermeture continue**.

Pour l'analyste OSINT, c'est une réalité structurante : les outils gratuits d'aujourd'hui peuvent disparaître demain. La discipline d'archivage anticipé devient vitale.

-----
