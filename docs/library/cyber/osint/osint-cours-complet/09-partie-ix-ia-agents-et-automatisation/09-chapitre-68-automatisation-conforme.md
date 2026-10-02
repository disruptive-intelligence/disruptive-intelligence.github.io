---
title: Chapitre 68 — Automatisation conforme
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE IX — IA, agents et automatisation
  - index.md
---

## 68.1 L'automatisation comme nécessité

L'OSINT 2026 traite des **volumes** que l'humain seul ne peut gérer. Automatiser certaines tâches devient une nécessité opérationnelle.

Mais l'automatisation soulève des **questions** :

- Conformité aux CGU plateformes.
- Respect des limites légales (scraping, anti-bot).
- Charge serveur (DoS involontaire).
- Reproductibilité et auditabilité.

## 68.2 Python comme langage OSINT

**Python** est le langage standard de l'automatisation OSINT pour :

- Lisibilité.
- Écosystème de librairies massives.
- Communauté.
- Multi-OS.

**Stack OSINT type.**

- `requests`, `httpx` : requêtes HTTP.
- `BeautifulSoup`, `lxml` : parsing HTML.
- `pandas` : data manipulation.
- `networkx` : graphes.
- `rapidfuzz` : matching de strings.
- `Playwright`, `Selenium` : scraping navigateur.
- `Scrapy` : framework scraping.
- `Telethon`, `Pyrogram` : Telegram API.
- `praw` : Reddit API.
- `tweepy` : Twitter API.

## 68.3 API officielles

**Toujours privilégier API officielles** quand disponibles.

**APIs OSINT principales.**

- **Shodan** : infrastructure.
- **HIBP** : breaches.
- **VirusTotal** : malware, IOCs.
- **GitHub** : code search.
- **Twitter (X) v2** : payante.
- **Reddit** : payante.
- **Telegram (Telethon)** : conditions strictes.
- **OpenSanctions** : gratuit.

**Authentification** : tokens API personnels, jamais hardcoded dans code.

## 68.4 Scraping résilient

Quand pas d'API, **scraping** mais avec rigueur.

**Outils.**

- **Playwright** (Microsoft) : moderne, multi-navigateurs.
- **Selenium** : classique.
- **Scrapy** : framework structuré.
- **httpx + BeautifulSoup** : simple.

**Bonnes pratiques.**

- **Respect robots.txt**.
- **Rate limiting** auto-imposé (1 requête / 3-10 sec).
- **User-Agent** identifiable et honnête.
- **Pas de charge sur serveur** (modération du parallélisme).
- **Conservation traçabilité** (logs des requêtes).

## 68.5 Anti-anti-scraping

Plateformes déploient des anti-bot. Contournements technologiques :

**Rotation User-Agents.** Sélection aléatoire dans liste réaliste.

**Proxies résidentiels.** BrightData, Smartproxy. Coûteux mais efficaces.

**CAPTCHA solvers.** 2Captcha, anti-captcha (déontologie variable).

**Cloudflare bypass.** FlareSolverr, Cloudscraper (durée de vie limitée).

**Behavioral fingerprinting.** Émuler comportement humain (pauses aléatoires, scroll, mouse).

**Précautions juridiques.** Tous ces contournements peuvent enfreindre CGU. Selon juridiction, frottements pénaux potentiels. À documenter et limiter.

## 68.6 Conformité légale

**Robots.txt** : respecter par défaut.

**CGU** : lire, respecter dans la mesure du raisonnable.

**Charge** : ne pas DoS un site.

**Données personnelles** : RGPD compliance, finalité, minimisation.

**Juridiction** : législations variables. Allemagne plus stricte, US plus permissif (hiQ v. LinkedIn 2022 SCOTUS).

## 68.7 Reproductibilité

**Scripts versionnés.** Git local.

**Documentation.** Comment lancer, paramètres, attendus.

**Logs.** Chaque exécution traçable.

**Test.** Unit tests pour fonctions critiques.

## 68.8 Workflows reproductibles

**Notebook Jupyter.** Pour investigation interactive avec traçabilité.

**Scripts orchestrés** (`make`, `snakemake`, `Airflow`). Pour pipelines complexes.

**Dockerized.** Image Docker reproductible avec dépendances figées.

## 68.9 Stockage des données automatisées

**Formats structurés.** JSON, CSV, Parquet.

**Bases locales.** SQLite (simple), PostgreSQL (volume).

**Pas de cloud non chiffré.** Toujours chiffrement côté client.

## 68.10 Synthèse — règles d'or automation

1. **API officielle** > scraping.
2. **Respect des CGU et robots.txt** par défaut.
3. **Rate limiting** auto-imposé.
4. **Logs** traçables.
5. **Versioning** Git.
6. **Reproductibilité** documentée.
7. **OPSEC** maintenue (pas de fuite d'intent).
8. **Conformité RGPD** par design.

-----
