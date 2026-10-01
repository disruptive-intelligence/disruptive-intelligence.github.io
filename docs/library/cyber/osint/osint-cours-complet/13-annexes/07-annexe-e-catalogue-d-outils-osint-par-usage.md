---
title: ANNEXE E — Catalogue d'outils OSINT par usage
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - Annexes
  - index.md
---

> **État des connaissances : mai 2026.** Catalogue à vérifier trimestriellement. Les outils marqués « risque élevé » sont susceptibles d'évolutions rapides (changement de tarification, restrictions, abandon). Pour chaque outil utilisé en enquête critique, consulter la documentation officielle au moment de l'usage. Les colonnes « Dernière vérification » et « Risque obsolescence » sont indicatives à mai 2026.

Catalogue structuré des outils essentiels mobilisés dans le cours, classés par usage. Pour chaque outil : description courte, accès (gratuit / freemium / payant), chapitre principal, dernière vérification, niveau de risque d'obsolescence.


## E.1 — Captures et préservation

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


## E.2 — Moteurs et recherche

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Google | Gratuit | Standard, dorks puissants | 19 | 2026-05 | Moyen (opérateurs évolutifs) |
| DuckDuckGo | Gratuit | Privacy, !bangs | 19 | 2026-05 | Faible |
| Yandex | Gratuit | Reverse image excellent | 19, 46 | 2026-05 | Moyen (géopolitique) |
| Bing | Gratuit | Indexation différente | 19 | 2026-05 | Faible |
| Brave Search | Gratuit | Index indépendant | 19 | 2026-05 | Faible |
| Marginalia / Mojeek | Gratuit | Index alternatif | 19 | 2026-05 | Moyen |
| Internet Archive Search | Gratuit | Texte historique | 20 | 2026-05 | Faible |


## E.3 — Sociétés et corporate

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


## E.4 — Sanctions et risque

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


## E.5 — Identités et personnes

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


## E.6 — Réseaux sociaux

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


## E.7 — Infrastructure et CTI

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
