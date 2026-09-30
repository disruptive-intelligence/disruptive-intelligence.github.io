---
title: Partie VII — Cas de synthèse ET référence
source: Cyber/02_OSINT/OSINT_Synthese.md
note: OSINT — synthèse
up:
- - OSINT — synthèse
  - index.md
---

---


## Chapitre 26 — Cas complet : synthèse Opération MIRAGE

Synthèse du fil rouge. De la sollicitation du cabinet Legrand & Associés au rapport final transmis aux autorités.

**Le schéma reconstitué :** Delaunay, DAF de TechnoVert, détourne des fonds via des paiements de « consulting » à Delta Consulting Ltd (Malte) — société contrôlée via un nominee maltais mais dont l'infrastructure est liée à Delaunay (email SPF, certificat SAN, Whois historique). Les fonds transitent de Malte vers un prestataire chypriote (identifié dans les Pandora Papers via ICIJ). Une partie est convertie en Bitcoin via Binance (compte KYC au nom de Delaunay — identifié via Holehe, adresse publiée sur Telegram, flux tracés sur la blockchain). L'immobilier (SCI, 1,2 M€) et le train de vie (forum luxe, voyages Instagram) sont incohérents avec les revenus déclarés. Parallèlement, Delaunay a orchestré une campagne de désinformation (blog lié par Whois historique, 8 faux comptes Twitter coordonnés, photos AI-generated) et publié une photo synthétique pour créer un faux alibi (détecté par la méthodologie de vérification Ch.14).

**Livrables :** rapport 25 pages (sommaire exécutif, 47 constatations cotées, ACH, conclusions avec niveaux de confiance, recommandations), graphe relationnel (47 entités, 83 relations, 5 juridictions), timeline 3 ans, annexes hashées, pistes de réquisitions (Binance KYC, Telegram admin, opérateur télécom, publicité foncière). Le C3N reprend avec les pouvoirs légaux — gel des actifs par ordonnance du juge.

---


## Chapitre 27 — Cas complet : investigation GEOINT

Une vidéo virale prétend montrer un événement dans un pays. L'investigateur applique la méthodologie complète : extraction d'indices visuels (enseignes en arabe dialecte spécifique, plaques format jordanien, signalétique non cohérente avec le pays prétendu, végétation méditerranéenne), hypothèses de localisation (3 villes possibles), vérification via Street View/Mapillary (correspondance exacte d'un carrefour), chronolocation par SunCalc (ombres → 14h30 le 15 mars, cohérent avec les archives météo), vérification d'authenticité (TinEye — pas de recyclage, ELA — pas de manipulation). Conclusion : la vidéo est authentique mais le lieu n'est pas celui prétendu.

---


## Chapitre 28 — Cas complet : dé-anonymisation d'un compte pseudonyme

Un compte pseudonyme « insider_leak42 » publie des informations confidentielles sur une entreprise. Username → Maigret → même username sur GitHub et forum de jeux. GitHub → commit signé avec j.martin.dev@outlook.com. Holehe → profils LinkedIn et Instagram. Instagram photo → PimEyes → correspondance avec Julien Martin, développeur chez l'entreprise. Corrélation : même fuseau horaire (posts Twitter et commits GitHub aux mêmes heures), même style d'écriture, même intérêts. L'attribution est « haute probabilité » (pas certitude). **Limites documentées :** le username pourrait avoir été recyclé, l'email pourrait être un piège, la reconnaissance faciale est un indice pas une preuve.

---


## Chapitre 29 — Cas complet

vérification d'une campagne de désinformation

Un réseau de faux comptes sur X et Telegram diffuse de fausses informations sur une entreprise cotée (impact sur le cours). Détection (12 comptes créés le même jour, photos AI-generated — aucune source en recherche inversée), analyse réseau (retweets mutuels, timing identique ±5 min), analyse infrastructure (3 domaines enregistrés le même jour, même registrar, même serveur — Whois + reverse IP), attribution (email dans le Whois historique lié à un concurrent), documentation (timeline, graphe, preuves cotées B2 — source fiable + info probablement vraie). Le cas illustre la convergence SOCMINT + OSINT technique + IMINT + analyse de réseau.

---


## Chapitre 30 — Exercice : investigation OSINT complète (non guidé)

Un exercice non guidé : scénario réaliste (individu suspect + sociétés + dimension internationale + Telegram + crypto). Sélecteurs initiaux fournis. L'étudiant doit : cadrer les questions, définir le plan de collecte, mener l'investigation en 8 heures, et produire un rapport complet (sommaire exécutif, constatations cotées A-F/1-6, graphe relationnel, timeline, ACH, annexes hashées, recommandations de réquisitions). Grille d'auto-évaluation fournie (cadrage, OPSEC, diversité des sources, qualité des pivots, cotation de fiabilité, identification des faux positifs, qualité du rapport, documentation des limites).

---
