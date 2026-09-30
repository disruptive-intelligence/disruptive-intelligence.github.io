---
title: ANNEXE E — Catalogue d'outils OSINT par usage
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - Annexes
  - index.md
---

> **État des connaissances : mai 2026.** Catalogue à vérifier trimestriellement. Les outils marqués « risque élevé » sont susceptibles d'évolutions rapides (changement de tarification, restrictions, abandon). Pour chaque outil utilisé en enquête critique, consulter la documentation officielle au moment de l'usage. Les colonnes « Dernière vérification » et « Risque obsolescence » sont indicatives à mai 2026.

Catalogue structuré des outils essentiels mobilisés dans le cours, classés par usage. Pour chaque outil : description courte, accès (gratuit / freemium / payant), chapitre principal, dernière vérification, niveau de risque d'obsolescence.


### E.1 — Captures et préservation

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Hunchly | Payant (~130 $/an) | Capture web auto avec hash | 10, 15 | 2026-05 | Faible |
| SingleFile | Gratuit (extension) | Capture one-file HTML+resources | 15 | 2026-05 | Faible |
| Wayback Machine | Gratuit | Archive web Internet Archive | 20 | 2026-05 | Faible |
| archive.today | Gratuit | Archive web alternatif | 20 | 2026-05 | Moyen (financement) |
| FreezePage | Gratuit | Capture page web horodatée | 15 | 2026-05 | Moyen |
| ExifTool | Gratuit | Métadonnées multi-formats | 29, 45 | 2026-05 | Faible (standard) |
| OpenTimestamps | Gratuit | Horodatage blockchain | 16, 90 | 2026-05 | Faible |
| VeraCrypt | Gratuit | Chiffrement volumes | 16 | 2026-05 | Faible |


### E.2 — Moteurs et recherche

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Google | Gratuit | Standard, dorks puissants | 19 | 2026-05 | Moyen (opérateurs évolutifs) |
| DuckDuckGo | Gratuit | Privacy, !bangs | 19 | 2026-05 | Faible |
| Yandex | Gratuit | Reverse image excellent | 19, 46 | 2026-05 | Moyen (géopolitique) |
| Bing | Gratuit | Indexation différente | 19 | 2026-05 | Faible |
| Brave Search | Gratuit | Index indépendant | 19 | 2026-05 | Faible |
| Marginalia / Mojeek | Gratuit | Index alternatif | 19 | 2026-05 | Moyen |
| Internet Archive Search | Gratuit | Texte historique | 20 | 2026-05 | Faible |


### E.3 — Sociétés et corporate

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Pappers | Freemium | Standard FR | 37 | 2026-05 | Faible |
| Infogreffe | Mixte | Greffes FR officiel | 37 | 2026-05 | Faible |
| Companies House | Gratuit | Standard UK | 37 | 2026-05 | Faible |
| OpenCorporates | Freemium | Multi-juridictions (140+) | 37 | 2026-05 | Faible |
| SEC EDGAR | Gratuit | Cotées US | 37 | 2026-05 | Faible |
| ICIJ Offshore Leaks | Gratuit | Leaks consolidés | 37 | 2026-05 | Faible |
| OCCRP Aleph | Gratuit (registration) | Plateforme journalistique | 37 | 2026-05 | Faible |
| Sayari | Payant | OSINT corporate moderne | 37 | 2026-05 | Faible |
| Orbis (Bureau van Dijk) | Payant lourd | 400M sociétés mondial | 37 | 2026-05 | Faible |
| Dun & Bradstreet | Payant | Credit reporting | 37 | 2026-05 | Faible |


### E.4 — Sanctions et risque

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| OpenSanctions | Gratuit / API freemium | Standard gratuit | 38 | 2026-05 | Faible |
| OFAC SDN | Gratuit | US Treasury | 38 | 2026-05 | Faible |
| EU Sanctions Map | Gratuit | UE Commission | 38 | 2026-05 | Faible |
| OFSI consolidated list | Gratuit | UK | 38 | 2026-05 | Faible |
| WorldCheck (Refinitiv/LSEG) | Payant | Institutionnel | 38 | 2026-05 | Faible |
| Dow Jones Risk | Payant | Équivalent | 38 | 2026-05 | Faible |
| ComplyAdvantage | Payant | Moderne | 38 | 2026-05 | Faible |
| Sigma Ratings | Payant | Alternative | 38 | 2026-05 | Faible |


### E.5 — Identités et personnes

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Sherlock | Gratuit | Username cross-plateformes | 27 | 2026-05 | **Élevé** (plateformes bloquent) |
| WhatsMyName | Gratuit | Alternative Sherlock | 27 | 2026-05 | **Élevé** |
| Hunter.io | Freemium | Validation email | 27 | 2026-05 | Moyen |
| Holehe | Gratuit | Comptes liés à email | 27 | 2026-05 | **Élevé** (plateformes bloquent) |
| Epieos | Freemium | Pivots email | 27 | 2026-05 | Moyen |
| GHunt | Gratuit | Google account info | 27 | 2026-05 | **Élevé** (Google restreint) |
| HIBP | Gratuit (API payante) | Breaches | 42 | 2026-05 | Faible |
| DeHashed | Payant | Breaches profond | 42 | 2026-05 | Moyen |
| IntelX | Payant | Deep web, leaks | 42 | 2026-05 | Moyen |
| Hudson Rock | Payant | Stealer logs | 43 | 2026-05 | Moyen |
| SpyCloud | Payant institutionnel | CTI/breaches | 43 | 2026-05 | Faible |
| PimEyes | Payant | Reconnaissance faciale | 30 | 2026-05 | **Juridique élevé** (AI Act, RGPD) |
| FaceCheck.ID | Payant | Alternative | 30 | 2026-05 | **Juridique élevé** |


### E.6 — Réseaux sociaux

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| X API | Payant ($100-5000/mois) | Volume limité | 32 | 2026-05 | **Très élevé** (changements tarifaires) |
| LinkedIn Sales Navigator | Payant | Filtres avancés | 32 | 2026-05 | Moyen |
| InstaLoader | Gratuit | Instagram download | 32 | 2026-05 | **Élevé** (CGU Meta) |
| yt-dlp | Gratuit | YouTube et + | 32 | 2026-05 | Moyen (mises à jour fréquentes) |
| Telegago | Gratuit | Telegram search | 33 | 2026-05 | **Élevé** (financement) |
| TGStat | Gratuit | Stats Telegram | 33 | 2026-05 | Moyen |
| DiscordChatExporter | Gratuit | Discord export | 34 | 2026-05 | **Élevé** (CGU Discord) |
| Maltego (Casefile, free) | Gratuit / Payant | Graphes | 31 | 2026-05 | Faible |
| Gephi | Gratuit | Graphes académique | 31 | 2026-05 | Faible |
| NodeXL | Gratuit | Réseaux Excel | 31 | 2026-05 | Moyen |


### E.7 — Infrastructure et CTI

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Amass | Gratuit | Sous-domaines OWASP | 40 | 2026-05 | Faible |
| subfinder | Gratuit | Sous-domaines passifs | 40 | 2026-05 | Faible |
| crt.sh | Gratuit | Certificate Transparency | 39 | 2026-05 | Faible |
| Shodan | Freemium | Infrastructure exposée | 21, 40 | 2026-05 | Faible |
| Censys | Freemium | Alternative Shodan | 21, 40 | 2026-05 | Faible |
| FOFA / ZoomEye | Mixte | Chinois | 21 | 2026-05 | Moyen (géopolitique) |
| GreyNoise | Freemium | Bruit Internet | 40 | 2026-05 | Faible |
| DNSDumpster | Gratuit | DNS analyse | 39 | 2026-05 | Faible |
| SecurityTrails | Payant | Passive DNS historique | 39 | 2026-05 | Faible |
| DomainTools | Payant | WHOIS historique | 39 | 2026-05 | Faible |
| ViewDNS.info | Gratuit | Outils DNS | 39 | 2026-05 | Faible |
| Wappalyzer | Gratuit (extension) | Technologies | 41 | 2026-05 | Faible |
| BuiltWith | Freemium | Technologies profil | 41 | 2026-05 | Faible |
| DNSlytics | Freemium | Reverse trackers | 39 | 2026-05 | Moyen |
| DNSTwist | Gratuit | Typosquatting | 41 | 2026-05 | Faible |
| VirusTotal | Freemium | Malware analyse | 74 | 2026-05 | Faible |
| AbuseIPDB | Gratuit | IPs malveillantes | 74 | 2026-05 | Faible |
| URLhaus (abuse.ch) | Gratuit | URLs malveillantes | 74 | 2026-05 | Faible |
| MISP | Gratuit | Partage CTI | 74 | 2026-05 | Faible |


### E.8 — IMINT et GEOINT

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| ExifTool | Gratuit | Métadonnées | 45 | 2026-05 | Faible |
| Yandex Images | Gratuit | Reverse image excellent | 46 | 2026-05 | Moyen (géopolitique) |
| Google Lens | Gratuit | Reconnaissance | 46 | 2026-05 | Faible |
| TinEye | Freemium | First seen | 46 | 2026-05 | Faible |
| Bing Visual | Gratuit | Alternative | 46 | 2026-05 | Faible |
| Forensically | Gratuit | ELA, clone detection | 47 | 2026-05 | Faible |
| FotoForensics | Gratuit | ELA simple | 47 | 2026-05 | Faible |
| Hive Moderation | Freemium | IA detection | 47, 56 | 2026-05 | Moyen (course armement) |
| Optic AI or Not | Freemium | IA detection | 47, 56 | 2026-05 | Moyen |
| Sensity AI | Payant | Deepfake detection | 53, 56 | 2026-05 | Moyen |
| Intel FakeCatcher | Pro | Physiologique | 53, 56 | 2026-05 | Moyen |
| Google Maps | Gratuit | Cartographie | 48 | 2026-05 | Faible |
| Google Earth Pro | Gratuit | Satellite historique | 50 | 2026-05 | Faible |
| OpenStreetMap | Gratuit | Cartographie OSM | 48 | 2026-05 | Faible |
| Overpass Turbo | Gratuit | OSM queries | 48 | 2026-05 | Faible |
| Mapillary | Gratuit | Street View communautaire | 48 | 2026-05 | Faible |
| KartaView | Gratuit | Alternative OSM | 48 | 2026-05 | Faible |
| Sentinel Hub | Gratuit (limité) | Imagerie satellite | 50 | 2026-05 | Faible |
| Planet Labs | Payant | Imagerie quotidienne | 50 | 2026-05 | Faible |
| Maxar | Payant lourd | Très haute résolution | 50 | 2026-05 | Faible |
| SunCalc | Gratuit | Position solaire | 49 | 2026-05 | Faible |
| ShadowMap | Gratuit | Visualisation 3D ombres | 49 | 2026-05 | Faible |
| Wolfram Alpha | Freemium | Météo historique | 49 | 2026-05 | Faible |
| GeoSpy | Freemium | Géolocalisation IA | 51 | 2026-05 | Moyen (rapide évolution) |
| GeoSeer / PicArta | Freemium | Alternatives | 51 | 2026-05 | Moyen |


### E.9 — Transport

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| MarineTraffic | Freemium | AIS maritime | 52 | 2026-05 | Faible |
| VesselFinder | Freemium | Alternative | 52 | 2026-05 | Faible |
| FleetMon | Freemium | Maritime | 52 | 2026-05 | Faible |
| Equasis | Gratuit | Multi-sources navires | 52 | 2026-05 | Faible |
| Tankertrackers | Payant | Pétroliers sanctions | 52 | 2026-05 | Faible |
| Flightradar24 | Freemium | ADS-B (filtré) | 52 | 2026-05 | Faible |
| ADS-B Exchange | Gratuit | ADS-B non filtré | 52 | 2026-05 | Moyen (financement community) |
| planespotters.net | Gratuit | Photos | 52 | 2026-05 | Faible |
| Aviation Safety Network | Gratuit | Sécurité aérienne | 52 | 2026-05 | Faible |


### E.10 — Vérification et provenance

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| contentcredentials.org | Gratuit | Verify C2PA | 55 | 2026-05 | Faible |
| C2PA viewer | Gratuit (extension) | Inspecteur | 55 | 2026-05 | Faible |
| SynthID detector | Limité Google | Watermark IA | 56 | 2026-05 | Moyen (déploiement progressif) |
| GPTZero | Freemium | Détection texte IA | 56 | 2026-05 | **Élevé** (faible fiabilité reconnue) |
| Originality.AI | Payant | Détection texte IA | 56 | 2026-05 | **Élevé** (idem) |
| Copyleaks | Payant | Détection texte IA | 56 | 2026-05 | **Élevé** (idem) |
| Resemble Detect | Payant | Voix clonée | 56 | 2026-05 | Moyen |
| Information Laundromat | Gratuit | Cross-narratifs SIO | 58 | 2026-05 | Faible |
| Hamilton 2.0 | Gratuit | Monitoring RU/CN | 35 | 2026-05 | Faible |


### E.11 — IA et automatisation

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Claude (Anthropic) | Freemium / Payant | LLM analyste | 60 | 2026-05 | Moyen (générations successives) |
| ChatGPT / GPT-4 (OpenAI) | Freemium / Payant | LLM | 60 | 2026-05 | Moyen |
| Gemini (Google) | Freemium / Payant | LLM | 60 | 2026-05 | Moyen |
| Mistral | Freemium / Payant | LLM européen | 60, 65 | 2026-05 | Moyen |
| Llama 3.3 / 4 (Meta) | Open source local | LLM local | 65 | 2026-05 | Moyen (générations) |
| Qwen 2.5 / 3 (Alibaba) | Open source | LLM multilingue | 65 | 2026-05 | Moyen |
| Ollama | Gratuit | Serveur LLMs locaux | 65 | 2026-05 | Faible |
| LM Studio | Gratuit | Interface LLMs locaux | 65 | 2026-05 | Faible |
| Perplexity | Freemium | RAG search avec citations | 63 | 2026-05 | Moyen |
| LangChain | Open source | Framework agents | 67 | 2026-05 | Moyen (évolutions API) |
| CrewAI | Open source | Multi-agents | 67 | 2026-05 | Moyen |
| AutoGen (Microsoft) | Open source | Multi-agents | 67 | 2026-05 | Moyen |
| Whisper (OpenAI) | Open source | Transcription audio | 61 | 2026-05 | Faible |


### E.12 — Knowledge graphs et données

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Apache Jena | Open source | RDF/SPARQL stack | 66 | 2026-05 | Faible |
| Neo4j Community | Open source | Property graph | 66 | 2026-05 | Faible |
| Stardog | Freemium | RDF moderne | 66 | 2026-05 | Faible |
| RapidFuzz | Open source | Fuzzy matching | 68, 82 | 2026-05 | Faible |
| dedupe.io | Open source | Entity resolution | 82 | 2026-05 | Faible |
| Splink (UK gov) | Open source | Entity resolution volume | 82 | 2026-05 | Faible |
| Obsidian | Freemium | Vault markdown + graphe | 17 | 2026-05 | Faible |


### E.13 — Visualisation et timeline

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Gephi | Open source | Graphes | 31, 83 | 2026-05 | Faible |
| Cytoscape | Open source | Graphes biologiques | 31 | 2026-05 | Faible |
| Maltego | Freemium / Payant | OSINT graphes | 31, 83 | 2026-05 | Faible |
| Timeline Explorer (Zimmerman) | Gratuit | Timeline | 83 | 2026-05 | Faible |
| Aeon Timeline | Payant | Timeline pro | 83 | 2026-05 | Faible |
| TimelineJS (Knightlab) | Gratuit | Timeline web publish | 83 | 2026-05 | Faible |


### E.14 — Outils à risque obsolescence Très Élevé (vigilance)

Liste des outils dont l'accès / l'existence est particulièrement volatile en 2026, à surveiller au moment de l'enquête :

| Outil | Usage typique | Statut mai 2026 | Alternative |
|---|---|---|---|
| **Nitter** | Miroir X/Twitter | Quasi tous instances down | yt-dlp pour vidéos, archive.today, X API payante |
| **Pushshift** | Reddit archive | Restreint à modérateurs/chercheurs | API Reddit officielle (payante), undelete.pullpush (mirror partiel) |
| **Holehe** | Comptes liés email | Fonctionne partiellement, plateformes bloquent | Combinaisons manuelles, Epieos |
| **GHunt** | Google account info | Restreint régulièrement par Google | Pivots indirects, recherche manuelle |
| **InstaLoader** | Instagram download | Risque CGU Meta, blocages fréquents | Compte invest + Hunchly |
| **Sherlock** | Username cross-plateformes | Mises à jour communauté nécessaires | WhatsMyName en complément |
| **Diverses instances Searx, Whoogle** | Privacy search | Instances ouvrent/ferment | Self-host, multi-instances |
| **CrowdTangle (Meta)** | Recherche réseau social | **Fermé août 2024** | Meta Content Library (chercheurs), Brandwatch |
| **Plus de 50 % des outils crypto on-chain gratuits 2021-2023** | Clustering, attribution | Payants ou abandonnés | Etherscan, Walletexplorer, services payants |

**Discipline.** Tester tout outil sensible **avant** d'en dépendre dans une enquête critique. Documenter l'état au moment de l'usage. Identifier au moins une alternative pour chaque outil critique du parc.


### E.15 — Politique de mise à jour

L'écosystème OSINT évolue **mensuellement**. L'analyste révise son catalogue d'outils **au minimum tous les trimestres** :

- Quels outils n'ont plus de support / sont obsolètes ?
- Quels nouveaux outils sont apparus ?
- Quels outils ont changé de modèle (gratuit → payant) ?
- Quelles modifications d'API ou de fonctionnalités ?

Sources de veille : Bellingcat resources, OSINT Framework, OSINT Combine, Trace Labs, communautés Discord et Reddit (/r/OSINT, /r/cybersecurity).

-----


## ANNEXE F — Checklist OPSEC

Checklist opérationnelle d'OPSEC à appliquer pour toute enquête OSINT. À adapter au niveau de menace (cible peu équipée vs cible étatique).


### F.1 — Avant l'enquête : préparation

**Matériel.**

- [ ] Machine d'investigation dédiée (physique ou VM cloisonnée).
- [ ] Disque dur chiffré (VeraCrypt ou équivalent).
- [ ] Sauvegarde chiffrée 3-2-1.
- [ ] Câble réseau ou Wi-Fi dédié (pas Wi-Fi personnel).

**Réseau.**

- [ ] VPN no-log auditésuite, payé via moyens non-traçants si menace élevée.
- [ ] Tor Browser installé sur VM dédiée.
- [ ] Killswitch VPN activé (déconnexion auto si VPN tombe).
- [ ] DNS over HTTPS / DNS chiffrés (NextDNS, Cloudflare 1.1.1.1).

**Navigateurs.**

- [ ] Profils navigateur séparés (Firefox profils, Brave profils).
- [ ] Extensions privacy (uBlock, Privacy Badger, Cookie AutoDelete).
- [ ] Mode privé activé par défaut.
- [ ] Pas d'extension non vérifiée (risque exfiltration).
- [ ] User-Agent réaliste (pas custom révélateur).

**Comptes d'investigation.**

- [ ] Comptes matures (créés 6-12 mois avant usage critique).
- [ ] Email burner dédié (ProtonMail / Tutanota).
- [ ] Numéros virtuels pour SMS confirmation (TextNow, etc.).
- [ ] Photos avatars cohérentes (pas IA détectable au premier coup).
- [ ] Cohérence biographique entre plateformes.


### F.2 — Pendant l'enquête : pratique

**Captures.**

- [ ] Hunchly activé (toutes pages d'enquête capturées).
- [ ] Hashes calculés sur chaque pièce critique.
- [ ] Horodatage qualifié (OpenTimestamps) sur pièces sensibles.
- [ ] Pas d'usage d'outils en SaaS pour pièces sensibles (préférer locaux).

**Requêtes.**

- [ ] Pas d'usage de Google / Bing direct pour cibles sensibles (privilégier Yandex, DuckDuckGo, ou via Tor).
- [ ] Pas d'usage de WHOIS via service sans VPN.
- [ ] Pas d'usage de Shodan / Censys directement depuis IP traçable à l'analyste.
- [ ] LLMs cloud (Claude, GPT) uniquement pour tâches non-sensibles ; sensibles → LLM local.

**Interactions.**

- [ ] Pas d'interaction directe avec cible (likes, comments, follows) — observation passive uniquement.
- [ ] Pas de message direct.
- [ ] Pas de demande d'amitié / connexion.

**Fichiers.**

- [ ] EXIF strippés sur tout fichier transmis hors workspace chiffré.
- [ ] Aucun fichier non chiffré sur cloud public.
- [ ] Hashage avant transmission, vérification à réception.


### F.3 — Communications

**Avec commanditaire.**

- [ ] Email chiffré (PGP/GPG ou S/MIME).
- [ ] Signal (chiffrement bout en bout).
- [ ] Plateforme dédiée (Tresorit Send, OnionShare).
- [ ] Pas de SMS pour information sensible.
- [ ] Confirmation à réception.

**Stockage des communications.**

- [ ] Chiffrement local.
- [ ] Durée de conservation documentée.
- [ ] Purge programmée.


### F.4 — Niveau de menace : adaptations

**Niveau 1 (cible peu équipée).** OPSEC standard suffisante.

**Niveau 2 (cible compétente).** Renforcer : LLMs locaux, VPN multi-saut, Tor pour requêtes sensibles, durcissement comptes invest.

**Niveau 3 (cible étatique).** OPSEC maximale : Tails sur USB, Whonix VM, jamais de cloud, communications PGP, devices air-gapped pour stockage, possibilité d'analyste itinérant.

**Niveau 4 (urgence vie).** Coopération avec services compétents (DGSI, gendarmerie). L'OSINT privée seule est inadéquate.


### F.5 — Après l'enquête : clôture

**Diffusion.**

- [ ] Rapport chiffré (PAdES, AES).
- [ ] Watermark destinataire si pertinent.
- [ ] TLP marqué.
- [ ] Confirmation à destinataire.

**Archivage.**

- [ ] Stockage chiffré 3-2-1.
- [ ] Durée de conservation documentée.
- [ ] Intégrité vérifiée périodiquement (re-hash).

**Purge.**

- [ ] Données personnelles purgées à fin de période (RGPD).
- [ ] Comptes d'investigation maintenus ou archivés selon usage.
- [ ] LLMs locaux : modèles téléchargés peuvent être conservés (pas de risque).
- [ ] Logs d'enquête conservés ou purgés selon mandat.


### F.6 — Erreurs OPSEC fréquentes à éviter

- Mélanger compte personnel et compte d'investigation.
- Liker / follower par erreur depuis compte invest.
- Oublier VPN sur certaines requêtes.
- Conserver fichiers non chiffrés sur disque pour « gagner du temps ».
- Cloud sync (Dropbox, OneDrive, iCloud) sur fichiers d'enquête.
- Mention du nom du commanditaire dans recherches Google.
- Photos perso accidentellement uploadées avec EXIF.
- Captures contenant URL de l'analyste dans la barre d'adresse.
- Métadonnées de fichiers (auteur Word, chemin) révélant identité analyste.


### F.7 — Audit OPSEC régulier

L'analyste / cabinet audite régulièrement (semestriellement) sa propre OPSEC :

- Test d'attaque hypothétique (que verrait un adversaire ?).
- Mise à jour des bonnes pratiques.
- Renouvellement des comptes d'investigation si compromis.
- Veille sur évolutions menaces et contre-mesures.

> **Principe.** L'OPSEC est une discipline continue, pas un état. Une enquête sans OPSEC, c'est une investigation qui se retournera tôt ou tard contre l'analyste ou son commanditaire.

-----


## ANNEXE G — Modèle de journal d'investigation

Le **journal d'investigation** est la mémoire écrite et structurée de l'enquête. Tout est inscrit, daté, sourcé, coté. Modèle de référence pour usage en vault Obsidian / fichier Markdown local chiffré.


### G.1 — Structure du journal

**Niveau 1 — Index du dossier.**

- Page d'index avec liens vers tous les éléments du dossier.

**Niveau 2 — Sections principales.**

- 0-mandat.md : Mandat reçu et cadrage.
- 1-methodologie.md : Méthodologie spécifique adoptée.
- 2-fiches/ : Dossier contenant les fiches entités.
- 3-journal/ : Dossier contenant les entrées chronologiques.
- 4-pieces/ : Dossier contenant les pièces archivées avec hashes.
- 5-analyse/ : Dossier contenant ACH, matrices, hypothèses.
- 6-livrables/ : Dossier contenant les versions du rapport.


### G.2 — Entrée type de journal

Chaque entrée de journal contient :

```markdown
# Entrée [YYYY-MM-DD-HHmm] [Action]

## Contexte
[Pourquoi cette entrée, dans quel cadre]

## Action conduite
[Quoi exactement : recherche, capture, vérification]

## Sources consultées
- [URL 1] — [date d'accès] — [hash si applicable]
- [URL 2] — ...

## Résultats
[Ce qui a été trouvé]

## Cotation préliminaire
- Source : [A-F]
- Information : [1-6]

## Pivots possibles identifiés
- [Pivot 1]
- [Pivot 2]

## Limites / questions ouvertes
[Ce qui reste à investiguer]

## Liens dossier
- Fiches mises à jour : [[Fiche P-001]]
- Pièces archivées : pieces/[ref]

## Notes méthodologiques
[Bonnes pratiques, leçons, biais détectés]

---
Hash de cette entrée (post-rédaction) : [SHA-256]
```
