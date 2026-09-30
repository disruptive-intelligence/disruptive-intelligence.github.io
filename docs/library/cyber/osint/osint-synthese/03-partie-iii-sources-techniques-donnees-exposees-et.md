---
title: Partie III — Sources techniques, données exposées ET dark web
source: Cyber/02_OSINT/OSINT_Synthese.md
note: OSINT — synthèse
up:
- - OSINT — synthèse
  - index.md
---

*Au-delà des réseaux sociaux, l'investigateur interroge les registres d'entreprises, l'infrastructure technique, les données fuitées et le dark web — des sources qui partagent un point commun : elles sont techniques, souvent structurées, et révèlent ce que la surface du web ne montre pas.*

---


## Chapitre 9 — Investigation corporate et structures juridiques

### 9.1 Les registres d'entreprises par juridiction

**France** : Pappers (gratuit — RCS, statuts, comptes, dirigeants, bénéficiaires effectifs), Infogreffe (payant pour certains documents), BODACC, INPI. **UK** : Companies House (gratuit — comptes, dirigeants, PSC). **US** : SEC EDGAR (cotées), State registries. **Luxembourg** : LBR. **Suisse** : Zefix. **Multi-pays** : OpenCorporates, Orbis/BvD (commercial — le plus complet en international). Les **juridictions opaques** (BVI, Seychelles, Panama — registres inaccessibles → utiliser les leaks ICIJ, OCCRP, et les registres des juridictions de transit).

### 9.2 Le workflow d'investigation corporate

Registre → dirigeants/actionnaires → UBO → screening PEP/sanctions → liens entre sociétés (mêmes dirigeants, même adresse, même expert-comptable) → analyse financière (comptes publiés) → OSINT technique (domaines, infrastructure) → cartographie réseau (Maltego). Les red flags : société récente avec CA élevé, adresse de domiciliation, pas de site web, pas d'employés visibles, dirigeants avec multiples mandats non liés, sociétés en cascade multi-juridictions.

### 9.3 Les montages opaques

Sociétés écrans, trusts, nominees, layering, round-tripping. Pour chaque : principe, red flags, sources d'investigation. L'articulation : ce cours identifie les structures et les red flags ; le cours FININT analyse les flux financiers en profondeur.

**Faux positifs fréquents :** une société dans une juridiction offshore n'est pas intrinsèquement suspecte (de nombreuses structures légitimes utilisent des holdings luxembourgeoises ou irlandaises pour des raisons fiscales légales). Un nominee director n'est pas nécessairement un prête-nom criminel (c'est une pratique courante dans certaines juridictions). **Ce qui constitue un signal vs un élément corroboré :** une société au Panama = signal (à investiguer davantage). Une société au Panama + même adresse que 45 autres sociétés + nominee connu des leaks ICIJ + flux incohérents avec l'activité déclarée = faisceau d'indices fortement corroboré.

> **🎯 MIRAGE — Épisode 5 :** Pappers → TechnoVert SAS, Delaunay DAF. Recherche des mandats → SCI Delaunay Patrimoine + Delta Consulting Ltd (Malte, nominee maltais, centre de domiciliation avec 45 sociétés). ICIJ Offshore Leaks → pas de résultat direct mais adresse email deltaconsulting.mt liée à un prestataire chypriote des Pandora Papers. Le réseau se dessine.

---


## Chapitre 10 — Investigation sur les domaines, DNS et infrastructure

Le **Whois** (propriétaire, dates, registrar — beaucoup anonymisés RGPD ; les Whois historiques révèlent les anciens propriétaires — DomainTools, SecurityTrails). Le **DNS** : enregistrements A (IP), MX (serveur mail → fournisseur email), TXT (SPF, DKIM — révèlent les services utilisés), NS, CNAME, CAA. Les changements DNS dans le temps (SecurityTrails — historique complet). Les **certificats SSL/TLS** : crt.sh (Certificate Transparency — TOUS les certificats sont publics). Les SAN révèlent les domaines liés (*.technovert.fr et *.deltaconsulting.mt dans le même certificat = lien d'infrastructure).

Le **reverse DNS** et les sous-domaines (Sublist3r, Amass, SecurityTrails → cartographie de la surface). Le fingerprinting technologique (Wappalyzer, BuiltWith). L'analyse d'**adresses IP** (géolocalisation, ASN, Whois IP — RIPE/ARIN/APNIC). Les moteurs d'infrastructure : **Shodan** (services exposés), **Censys** (cartographie Internet). Le reverse IP (domaines co-hébergés → lien d'infrastructure).

**Limites :** les Whois anonymisés (RGPD) réduisent considérablement la valeur du Whois actuel — les Whois historiques (avant anonymisation) sont la source la plus riche. Les résultats Shodan/Censys ne sont pas en temps réel (scans périodiques) — un service exposé hier peut être fermé aujourd'hui. Le reverse IP sur un hébergeur mutualisé (OVH, AWS) peut montrer des milliers de domaines co-hébergés sans lien entre eux — le co-hébergement n'est un signal que sur un serveur dédié ou un petit hébergeur.

---


## Chapitre 11 — Breaches, leaks et exploitation de données fuitées

*Les données fuitées sont parmi les sources OSINT les plus puissantes — et les plus sensibles juridiquement.*

Les sources : Have I Been Pwned (vérification gratuite, 14 Mrd de comptes), DeHashed (recherche par email, username, nom, IP, téléphone), Snusbase, Intelligence X (archives de pastes et leaks). L'exploitation comme pivot : un email dans un dump avec un mot de passe révèle les habitudes (mots de passe réutilisés), un numéro dans le dump Facebook 2021 lie un numéro à un profil, le dump Ledger 2020 révèle les détenteurs de crypto-hardware.

**Cadre légal :** la consultation de données fuitées accessibles en sources ouvertes est une zone grise — les données sont techniquement accessibles mais leur collecte initiale est illicite. Les LEA et CRF les exploitent ; les investigateurs privés doivent documenter la source et la méthode, et ne pas les utiliser comme preuve unique mais comme piste à corroborer par des sources indépendantes. La sécurisation : VM dédiée, stockage chiffré, suppression après usage, ne JAMAIS télécharger de dumps massifs sur une machine non sécurisée.

**Ce qui constitue une piste vs un élément corroboré :** un email trouvé dans un dump = piste (l'email existait au moment de la fuite). Un email dans un dump Ledger + un compte Binance identifié via Holehe + une adresse Bitcoin publiée sur Telegram = faisceau convergent fortement corroboré (le suspect détient des crypto-actifs).

> **🎯 MIRAGE — Épisode 6 :** DeHashed → marcdelaunay75@gmail.com présent dans les dumps LinkedIn 2021, Adobe 2013, Ledger 2020. Le dump Ledger confirme la détention d'un hardware wallet crypto. Le mot de passe Adobe (« Marco75Paris! ») est cohérent avec le pattern marc_del75 / Marco D.

---


## Chapitre 12 — Dark Web et DARKINT

*Le dark web est à la fois une source d'investigation et un terrain d'enquête. Ce chapitre couvre les deux dimensions de manière opérationnelle.*

### 12.1 Accès et navigation

Le dark web est un ensemble de réseaux accessibles via des protocoles spécifiques : **Tor** (sites .onion — le plus courant), **I2P** (services .i2p — plus niche). Accès obligatoirement depuis une VM dédiée avec OPSEC maximale (Tails ou Whonix). Les erreurs courantes : accéder sans VM, cliquer sur des liens non vérifiés, interagir avec des vendeurs (ligne rouge pour un privé).

### 12.2 Les sources principales

Les **forums cybercriminels** : vente d'accès (RDP, VPN, credentials — Initial Access Brokers), vente de données volées, outils (malware, exploits, kits de phishing), et services (blanchiment, cashout, faux documents). Les **marketplaces** (drogues, armes, services). Les **paste sites** (fuites de données, dox, revendications). Le **Telegram comme extension du dark web** : en 2024-2025, une grande partie de l'activité clandestine a migré de Tor vers Telegram — vente de données, carding, distribution de malware. Cette migration est motivée par la facilité d'accès (pas besoin de Tor), la rapidité, et le volume d'utilisateurs (Ch.8).

### 12.3 L'OSINT sur le dark web

Les erreurs OPSEC des criminels sont la principale source d'investigation : un vendeur qui réutilise un username entre le dark web et un réseau social clearnet, un PGP key avec un email identifiable (le fingerprint PGP est un pivot vers l'identité), une adresse Bitcoin réutilisée entre le dark web et un exchange KYC (Ch.16), des métadonnées dans des fichiers partagés (PDF avec auteur, images avec EXIF), et des patterns stylistiques (même style d'écriture entre un profil dark web et un profil clearnet).

Le **monitoring dark web** : outils commerciaux (Flare, Recorded Future, DarkOwl — alertes quand des données de l'organisation apparaissent), outils open source (Ahmia — moteur de recherche .onion, Torch). Les moteurs indexent une fraction du contenu — la majorité des forums nécessite un compte et une « réputation ».

**Limites pour l'investigateur privé :** la consultation est légale (observer un forum n'est pas un crime). L'interaction (acheter, vendre, participer) est très risquée juridiquement et opérationnellement. L'investigateur privé **observe et documente** — il ne participe PAS. Les LEA ont un cadre différent (opérations sous couverture, achat contrôlé). Le cours Dark Web de la bibliothèque traite ces opérations en profondeur.

**Faux positifs :** les vendeurs dark web utilisent des noms et des marques pour attirer (un forum « FrenchHackers » n'est pas nécessairement français). Les données vendues sont souvent recyclées ou fausses (un vendeur qui prétend vendre 10 millions de comptes peut vendre un vieux dump déjà public). La vérification est indispensable avant de traiter une information dark web comme fiable.

---
