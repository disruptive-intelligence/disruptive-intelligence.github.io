---
title: Annexes
source: Cyber/02 OSINT/Méthode & enquête/OSINT — synthèse.md
note: OSINT — synthèse
up:
- - OSINT — synthèse
  - index.md
---

---


## Annexe A — Glossaire OSINT

| Terme | Définition |
|-------|-----------|
| **ACH** | Analysis of Competing Hypotheses — évaluation structurée des hypothèses |
| **Avatar / Sock puppet** | Fausse identité créée pour l'investigation |
| **Clustering** | Regroupement d'adresses crypto appartenant au même wallet |
| **Corroboration** | Confirmation d'un fait par 2+ sources indépendantes |
| **DARKINT** | Renseignement issu du dark web |
| **Dorking** | Utilisation d'opérateurs avancés dans les moteurs de recherche |
| **ELA** | Error Level Analysis — détection de manipulation d'images |
| **EXIF** | Métadonnées intégrées dans les images (GPS, appareil, date) |
| **FININT** | Renseignement financier |
| **GEOINT** | Renseignement géospatial |
| **IMINT** | Renseignement par l'imagerie |
| **KYC** | Know Your Customer — vérification d'identité |
| **LEA** | Law Enforcement Agency — forces de l'ordre |
| **OPSEC** | Operational Security — sécurité opérationnelle |
| **OSINT** | Open Source Intelligence — renseignement en sources ouvertes |
| **PEP** | Politically Exposed Person |
| **Pivot** | Passage d'un sélecteur à un autre |
| **Sélecteur** | Identifiant de recherche (nom, email, username, téléphone, photo) |
| **SOCMINT** | Renseignement issu des réseaux sociaux |
| **UBO** | Ultimate Beneficial Owner — bénéficiaire effectif réel |

---


## Annexe B — Cheat sheets par plateforme

| Plateforme | Techniques clés |
|-----------|----------------|
| **Google** | site: filetype: intitle: inurl: AROUND(n) before:/after: cache: "exact" -exclusion |
| **Facebook** | site:facebook.com + dorks, extraction d'ID, groupes publics, check-ins |
| **Instagram** | Profils publics via web app, hashtags, localisation, tagged people, stories (capturer immédiatement) |
| **LinkedIn** | site:linkedin.com (évite la notification), recommandations, réseau de connexions |
| **Twitter/X** | from: to: since: until: filter: geocode:, archivage anticipé, APIs alternatives |
| **Telegram** | site:t.me, TGStat, Telepathy, admins/membres, forwarding, bots |
| **Reddit** | Historique utilisateur (API/PRAW), subreddits fréquentés |
| **Yandex** | Recherche inversée d'images (supérieur pour visages), contenu non-anglophone |

---


## Annexe C — Outils OSINT : référence à date (2025-2026)

*Les outils cités sont des exemples opérationnels à date. L'écosystème évolue rapidement — la méthodologie est durable, l'outil spécifique est remplaçable.*

| Catégorie | Outils (exemples) | Type |
|-----------|-------------------|------|
| **Recherche personnes** | Holehe, Epieos, Sherlock, Maigret, WhatsMyName, TrueCaller | Gratuit/Freemium |
| **Reconnaissance faciale** | PimEyes, FaceCheck.id, Search4Faces, Yandex Images | Freemium/Payant |
| **SOCMINT** | TGStat, Telepathy, Nitter (instances en déclin), Redective | Gratuit |
| **Corporate** | Pappers, OpenCorporates, Companies House, ICIJ Offshore Leaks, Orbis | Gratuit/Payant |
| **Domaines/DNS** | DomainTools, SecurityTrails, crt.sh, Sublist3r, Amass | Gratuit/Payant |
| **IP/Infrastructure** | Shodan, Censys, ZoomEye, MaxMind | Freemium |
| **Images** | Google Images, Yandex Images, TinEye, FotoForensics, ExifTool | Gratuit |
| **GEOINT** | Google Earth, Sentinel Hub, SunCalc, MarineTraffic, FlightRadar24 | Gratuit/Freemium |
| **Crypto** | Blockchain.com, Etherscan, Tronscan, OXT, Chainalysis (pro) | Gratuit/Payant |
| **Breaches** | HIBP, DeHashed, Snusbase, Intelligence X | Freemium/Payant |
| **Dark web** | Ahmia, Torch, Flare, Recorded Future, DarkOwl | Gratuit/Payant |
| **Gestion** | Maltego, Hunchly, Obsidian, Timeline Explorer | Gratuit/Payant |
| **Automatisation** | Python (requests, BeautifulSoup, Selenium, Scrapy, pandas) | Gratuit |

---


## Annexe D — Templates d'investigation

**Rapport OSINT :** Sommaire exécutif → Mandat/périmètre → Méthodologie/sources → Constatations (fait + source + date + cotation + capture) → Analyse (ACH, timeline) → Conclusions (niveaux de confiance) → Recommandations → Annexes

**Fiche de cadrage :** Client → Objet → Questions d'investigation → Sélecteurs initiaux → Périmètre (géo, temporel, thématique) → Contraintes (délai, budget, OPSEC) → Livrables attendus

**Journal d'investigation :** Date/Heure → Source → Requête/Action → Résultat → Sélecteur découvert → Cotation → Capture (réf.)

---


## Annexe E — Workflow d'enquête en 10 étapes

1. **Cadrage** — Questions, sélecteurs, périmètre
2. **OPSEC** — Infrastructure, avatars, threat model
3. **Plan de collecte** — Sources, ordre, outils
4. **Collecte** — Exécuter, documenter chaque étape
5. **Préservation** — Capturer, horodater, hasher
6. **Traitement** — Nettoyer, organiser, dédupliquer
7. **Corrélation** — Graphe, pivots, liens
8. **Analyse** — ACH, cotation, timeline, biais, faux positifs
9. **Production** — Rapport, graphe, timeline, annexes
10. **Transmission et veille** — Remise au client, monitoring continu

---


## Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Ce cours (OSINT Mastery) |
|-----------|----------------|--------------------------|
| Crypto/blockchain | **OSINT Expert & Crypto-Actifs** | Ch.16 — vue opérationnelle |
| Renseignement financier | **FININT** | Ch.17 — OSINT financier |
| Dark web | **Dark Web** | Ch.12 — vue opérationnelle |
| CTI | **CTI** | Ch.18 — OSINT pour la CTI |
| Intelligence économique | **IE** | Ch.9 corporate, Ch.17 due diligence |
| Écosystèmes cybercriminels | **Écosystèmes** | Ch.12 — DARKINT |
| Digital Forensic | **Forensic** | Ch.4 méthodologie, Ch.21 rapport |

---


## Annexe G — Ressources, formations et lab

### Formations

| Formation | Organisme | Focus |
|-----------|----------|-------|
| SEC497 / GOSI | SANS / GIAC | OSINT complète — référence mondiale |
| PORP | TCM Security | Practical OSINT Research Professional |
| OSIP | IntelTechniques | Méthodologie complète (Michael Bazzell) |

### Communautés

| Ressource | Type |
|-----------|------|
| OSINT Curious | Podcast, blog, CTF |
| Sector035 | Newsletter « Week in OSINT » |
| Trace Labs | CTF OSINT humanitaires |
| Bellingcat | Investigations de référence |

### Lab

VM dédiée (Tails/Whonix ou VM Linux + VPN), Tor Browser, Maltego CE, Hunchly, Obsidian, Python 3 + bibliothèques OSINT (Sherlock, Maigret, Holehe), téléphone d'investigation dédié + cartes SIM prépayées. Optionnel : Trace Labs VM, licences Maltego Pro, clés API (Shodan, SecurityTrails, DeHashed, VirusTotal).

---

> **Note de clôture**
>
> Ce cours a été conçu comme un cours OSINT autonome et complet — la ressource de référence pour mener une investigation en sources ouvertes de bout en bout.
>
> L'opération MIRAGE illustre la réalité d'une investigation OSINT professionnelle : les pivots s'enchaînent (un email → un username → des comptes → des sociétés → des transactions crypto → une campagne de désinformation), chaque fait est coté (A-F/1-6 — pas un exercice académique mais ce qui distingue le renseignement du bruit), et les limites sont explicites (une corrélation n'est pas une preuve, un outil de détection n'est pas un verdict, l'absence de preuve de manipulation n'est pas une preuve d'authenticité).
>
> Le cours assume trois convictions. Première : l'OSINT est une discipline de renseignement, pas une collection d'outils — les outils changent tous les 6 mois, la méthodologie reste. Deuxième : chaque sous-domaine (SOCMINT, GEOINT, FININT, DARKINT, crypto, CTI) est enseigné de manière suffisamment complète pour être opérationnel seul — les cours spécialisés approfondissent, mais ce cours est autonome. Troisième : la vérification est la compétence OSINT la plus critique en 2025-2026 — face à la prolifération des contenus AI-generated et aux restrictions croissantes des plateformes, un analyste qui ne vérifie pas systématiquement et qui ne documente pas ses limites produit du bruit, pas du renseignement.
>
> *Investiguer avec méthode • Collecter avec rigueur • Analyser avec discipline • Documenter avec précision — et toujours distinguer ce qu'on sait de ce qu'on suppose.*
