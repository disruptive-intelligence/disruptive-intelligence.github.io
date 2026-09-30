---
title: OSINT — synthèse
source: Cyber/02_OSINT/OSINT_Synthese.md
---

*Investiguer • Collecter • Analyser • Documenter*

**Cours complet — 30 chapitres • 7 parties • 7 annexes**

*Investigation numérique • SOCMINT • GEOINT • IMINT • DARKINT • FININT • Crypto • Vérification • Rapport*

---

## Table des matières

- [Fil rouge : Opération MIRAGE](#fil-rouge-operation-mirage)
- **PARTIE I — FONDATIONS ET POSTURE DE L'INVESTIGATEUR (Ch.1-4)**
  - [Ch.1 — L'OSINT : doctrine, cycle du renseignement et positionnement](#chapitre-1-losint-doctrine-cycle-du-renseignement-et-positionnement)
  - [Ch.2 — Cadre juridique et éthique](#chapitre-2-cadre-juridique-et-ethique)
  - [Ch.3 — OPSEC : sécurité opérationnelle de l'investigateur](#chapitre-3-opsec-securite-operationnelle-de-linvestigateur)
  - [Ch.4 — Méthodologie, outillage et gestion de l'investigation](#chapitre-4-methodologie-outillage-et-gestion-de-linvestigation)
- **PARTIE II — INVESTIGATION SUR LES PERSONNES ET LES RÉSEAUX SOCIAUX (Ch.5-8)**
  - [Ch.5 — Moteurs de recherche et Google Dorking](#chapitre-5-moteurs-de-recherche-et-google-dorking)
  - [Ch.6 — Investigation sur les personnes](#chapitre-6-investigation-sur-les-personnes)
  - [Ch.7 — SOCMINT : investigation sur les réseaux sociaux](#chapitre-7-socmint-investigation-sur-les-reseaux-sociaux)
  - [Ch.8 — Telegram : investigation en profondeur](#chapitre-8-telegram-investigation-en-profondeur)
- **PARTIE III — SOURCES TECHNIQUES, DONNÉES EXPOSÉES ET DARK WEB (Ch.9-12)**
  - [Ch.9 — Investigation corporate et structures juridiques](#chapitre-9-investigation-corporate-et-structures-juridiques)
  - [Ch.10 — Investigation sur les domaines, DNS et infrastructure](#chapitre-10-investigation-sur-les-domaines-dns-et-infrastructure)
  - [Ch.11 — Breaches, leaks et exploitation de données fuitées](#chapitre-11-breaches-leaks-et-exploitation-de-donnees-fuitees)
  - [Ch.12 — Dark Web et DARKINT](#chapitre-12-dark-web-et-darkint)
- **PARTIE IV — IMINT, GEOINT ET VÉRIFICATION VISUELLE (Ch.13-15)**
  - [Ch.13 — IMINT : analyse d'images et recherche inversée](#chapitre-13-imint-analyse-dimages-et-recherche-inversee)
  - [Ch.14 — Contenus AI-generated et deepfakes : méthodologie de vérification](#chapitre-14-contenus-ai-generated-et-deepfakes-methodologie-de-verification)
  - [Ch.15 — GEOINT : géolocalisation, chronolocation et OSINT spatial](#chapitre-15-geoint-geolocalisation-chronolocation-et-osint-spatial)
- **PARTIE V — CRYPTO, FINANCE, CTI ET ANALYSE (Ch.16-20)**
  - [Ch.16 — Crypto-actifs et blockchain OSINT](#chapitre-16-crypto-actifs-et-blockchain-osint)
  - [Ch.17 — OSINT financier, corporate avancé et compliance](#chapitre-17-osint-financier-corporate-avance-et-compliance)
  - [Ch.18 — OSINT et cybersécurité : Threat Intelligence](#chapitre-18-osint-et-cybersecurite-threat-intelligence)
  - [Ch.19 — Restrictions de plateformes, techniques avancées et automatisation](#chapitre-19-restrictions-de-plateformes-techniques-avancees-et-automatisation)
  - [Ch.20 — Analyse, vérification et production de renseignement](#chapitre-20-analyse-verification-et-production-de-renseignement)
- **PARTIE VI — DU RENSEIGNEMENT À L'ACTION (Ch.21-25)**
  - [Ch.21 — Rédaction du rapport d'investigation OSINT](#chapitre-21-redaction-du-rapport-dinvestigation-osint)
  - [Ch.22 — OSINT et investigation judiciaire](#chapitre-22-osint-et-investigation-judiciaire)
  - [Ch.23 — Veille opérationnelle et monitoring continu](#chapitre-23-veille-operationnelle-et-monitoring-continu)
  - [Ch.24 — Désinformation, influence et fact-checking](#chapitre-24-desinformation-influence-et-fact-checking)
  - [Ch.25 — Adapter la méthodologie OSINT aux contextes spécialisés](#chapitre-25-adapter-la-methodologie-osint-aux-contextes-specialises)
- **PARTIE VII — CAS DE SYNTHÈSE ET RÉFÉRENCE (Ch.26-30)**
  - [Ch.26 — Cas complet : synthèse Opération MIRAGE](#chapitre-26-cas-complet-synthese-operation-mirage)
  - [Ch.27 — Cas complet : investigation GEOINT](#chapitre-27-cas-complet-investigation-geoint)
  - [Ch.28 — Cas complet : dé-anonymisation d'un compte pseudonyme](#chapitre-28-cas-complet-de-anonymisation-dun-compte-pseudonyme)
  - [Ch.29 — Cas complet : vérification d'une campagne de désinformation](#chapitre-29-cas-complet-verification-dune-campagne-de-desinformation)
  - [Ch.30 — Exercice : investigation OSINT complète (non guidé)](#chapitre-30-exercice-investigation-osint-complete-non-guide)
- **ANNEXES**

---

## Fil rouge : Opération MIRAGE

> **Contexte narratif — ce fil rouge traverse les 25 premiers chapitres et se conclut au Ch.26.**
>
> Un cabinet d'avocats parisien, **Legrand & Associés**, mandate une investigation OSINT sur **Marc Delaunay**, 48 ans, directeur financier de **TechnoVert SAS** — ETI française spécialisée dans les technologies de recyclage industriel, 450 collaborateurs, CA 85 M€. Le cabinet représente un actionnaire minoritaire qui soupçonne Delaunay de détournement de fonds vers des structures offshore, de blanchiment partiel via des crypto-actifs, et de campagne de désinformation contre un lanceur d'alerte interne.
>
> Sélecteurs initiaux fournis par le client : nom complet (Marc Delaunay), poste (DAF TechnoVert SAS), email professionnel (m.delaunay@technovert.fr).

---

## PARTIE I — FONDATIONS ET POSTURE DE L'INVESTIGATEUR

*Avant de chercher, comprendre le cadre, la méthode et la sécurité. Le socle opérationnel de toute investigation crédible.*

---

### Chapitre 1 — L'OSINT : doctrine, cycle du renseignement et positionnement

#### 1.1 Définition opérationnelle

L'OSINT (Open Source Intelligence) est la discipline du renseignement qui collecte, traite, analyse et exploite de l'information accessible publiquement pour produire du renseignement actionnable. Le mot clé est « discipline » : pas une collection d'outils, pas une recherche Google. C'est un processus structuré, reproductible et documenté qui transforme de l'information brute en renseignement exploitable par un décideur. L'OSINT se distingue de la simple recherche par trois traits : elle est **orientée par un objectif** (« Delaunay contrôle-t-il des sociétés offshore ? » est une question OSINT ; « que sais-je sur Delaunay ? » n'en est pas une), elle suit une **méthodologie rigoureuse** (le cycle du renseignement), et elle produit un **livrable avec un niveau de confiance explicite**.

#### 1.2 Les disciplines du renseignement

L'OSINT s'inscrit dans un écosystème : **HUMINT** (renseignement humain — entretiens, informateurs ; légal si transparent, illégal si usurpation d'identité pour un privé), **SIGINT** (interception de communications — réservé à l'État), **IMINT** (renseignement par l'imagerie — accessible si sources ouvertes), **GEOINT** (renseignement géospatial — imagerie satellite, cartographie), **SOCMINT** (réseaux sociaux), **FININT** (renseignement financier — registres, flux, blockchain ; renvoi cours FININT pour la profondeur métier), **DARKINT** (dark web — consultation légale, interaction très encadrée). En pratique, une investigation typique combine OSINT + SOCMINT + IMINT + GEOINT + FININT + parfois DARKINT. Ce cours les enseigne de manière intégrée.

#### 1.3 Le cycle du renseignement adapté à l'OSINT

**Orientation** (formuler les questions investigatives et le plan de collecte), **Collecte** (mobiliser les sources — documenter chaque donnée), **Traitement** (nettoyer, organiser, dédupliquer), **Analyse** (corréler, tester les hypothèses, coter la fiabilité), **Diffusion** (rapport avec conclusions et niveaux de confiance), **Feedback** (le commanditaire réagit — nouvelles pistes).

#### 1.4 Les niveaux de confiance et la cotation de fiabilité

La grille à double entrée : fiabilité de la source (A = totalement fiable → F = inconnue) × crédibilité de l'information (1 = confirmée → 6 = non évaluable). Un registre officiel qui indique un dirigeant = A1. Un post anonyme sur un forum = F6. La cotation accompagne CHAQUE fait dans le rapport — c'est ce qui distingue le renseignement professionnel du bruit.

---

### Chapitre 2 — Cadre juridique et éthique

Le cadre français : RGPD (données personnelles — collecte proportionnelle, minimisation, finalité), Code pénal art. 226-1 (vie privée), art. 323-1 (accès frauduleux), art. 226-18 (collecte déloyale). Le principe fondamental : **accessible ≠ public** (un bucket S3 ouvert par erreur n'est pas une source OSINT — jurisprudence Bluetouff 2014). Proportionnalité, minimisation, finalité.

Le cadre par pays : USA (plus permissif — premier amendement), UK (Data Protection Act — modéré), Allemagne (forte protection vie privée), France (position intermédiaire). L'OSINT pour les LEA vs le secteur privé (les LEA ont des pouvoirs que le privé n'a pas — réquisitions, interceptions, perquisitions). L'éthique au-delà du droit : ne pas harceler, ne pas doxxer, ne pas manipuler, signaler les contenus illicites, ne pas stocker plus longtemps que nécessaire.

---

### Chapitre 3 — OPSEC : sécurité opérationnelle de l'investigateur

Le **threat model** (calibrer l'OPSEC sur la menace — un suspect financier a des moyens de contre-investigation différents d'un suspect lié au crime organisé). L'infrastructure : VM dédiée par enquête (Tails, Whonix, ou VM Linux + VPN), VPN non-corporate sans logs, navigateur profil vierge, DNS chiffré, stockage chiffré.

Les **avatars/sock puppets** : légende résistant au contrôle OSINT (nom crédible, photo IA non détectable en reverse search, historique de publications cohérent, maturation avant utilisation), registre interne, téléphones d'investigation (cartes SIM prépayées, IMEI dédié), destruction après usage. Les erreurs courantes : LinkedIn connecté au vrai profil, réutilisation VPN perso/investigation, copier-coller entre VM et machine personnelle, métadonnées dans les captures envoyées au client.

**Limites :** l'OPSEC parfaite n'existe pas — chaque interaction en ligne laisse une trace potentielle. L'objectif n'est pas l'invisibilité totale mais la réduction du risque à un niveau acceptable pour la mission. L'investigateur qui surévalue sa sécurité est aussi dangereux que celui qui la néglige — le premier prend des risques en croyant être invisible.

---

### Chapitre 4 — Méthodologie, outillage et gestion de l'investigation

Le processus structuré : cadrage → plan de collecte → collecte → traitement → corrélation → analyse → production → feedback. Les outils de gestion : **Obsidian** (notes structurées — un vault par enquête), **Maltego** (graphe de liens — entités, arêtes, transforms), **Hunchly** (capture horodatée + hashing — chaîne de custody), **Timeline Explorer** (chronologie visuelle).

Le **pivoting** (un sélecteur mène à un autre ; les 6 sélecteurs principaux : nom, email, username, téléphone, photo, adresse). La **préservation** : capturer AVANT disparition (la règle n°1), horodatage, hashing SHA-256, chaîne de custody.

*Note sur les outils cités dans ce cours :* les outils mentionnés tout au long du cours sont des exemples opérationnels à date (2025-2026). L'écosystème OSINT évolue rapidement — des outils ferment, d'autres apparaissent, les API changent, les plateformes bloquent. La méthodologie (comment chercher, pourquoi, dans quel ordre) est durable ; l'outil spécifique est remplaçable. Chaque chapitre enseigne d'abord le principe et la technique, puis cite les outils comme illustrations.

> **🎯 MIRAGE — Épisode 1 :** Cadrage. Questions : QI-1 sociétés offshore ? QI-2 flux de TechnoVert vers ces sociétés ? QI-3 crypto-actifs ? QI-4 campagne de désinformation ? Sélecteurs initiaux : nom, email pro, employeur.

---

## PARTIE II — INVESTIGATION SUR LES PERSONNES ET LES RÉSEAUX SOCIAUX

---

### Chapitre 5 — Moteurs de recherche et Google Dorking

Les moteurs : **Google** (index le plus large, opérateurs avancés), **Bing** (indexe des résultats différents — toujours tester les deux), **Yandex** (supérieur pour la reconnaissance faciale et le contenu non-anglophone), **DuckDuckGo** (agrège Bing sans tracking), **Baidu** (contenu chinois). Les **Google Dorks** : site:, filetype:, intitle:, inurl:, AROUND(n), before:/after:, cache:, "exact phrase", -exclusion. Les dorks par objectif : documents financiers, organigrammes, emails exposés, directory listings, mentions officielles, recherche temporelle.

L'**archivage web** : Wayback Machine (retrouver des contenus supprimés, comparer les versions passées — l'outil de vérification temporelle le plus puissant), archive.today (capture instantanée), Google Cache (dernière version indexée).

**Limites et faux positifs :** les dorks ne renvoient que ce que Google a indexé — le contenu non indexé (deep web) est invisible. Les résultats sont influencés par la personnalisation, la localisation et le filtre SafeSearch. Un résultat Google n'est pas une preuve — c'est une piste à vérifier.

> **🎯 MIRAGE — Épisode 2 :** Google Dorking. "Marc Delaunay" site:linkedin.com → profil identifié. "m.delaunay" filetype:pdf → CV trouvé avec email perso marcdelaunay75@gmail.com. "TechnoVert" "Delta Consulting" → document PDF maltais mentionnant les deux entités.

---

### Chapitre 6 — Investigation sur les personnes

#### 6.1 La logique du pivot

L'investigation repose sur le pivot : passer d'un sélecteur à un autre. Nom → email → comptes en ligne → username → autres plateformes → photo → reconnaissance faciale → autres identités. À chaque pivot : documenter (sélecteur, source, date, confiance), mettre à jour le graphe, et vérifier la cohérence (même personne ou homonyme ?).

#### 6.2 Recherche par nom et registres publics

Combiner le nom avec des qualificateurs pour éliminer les homonymes. Moteurs de recherche de personnes par pays (exemples à date : France — 118712.fr, PagesJaunes ; US — ThatsThem, FastPeopleSearch — VPN US requis depuis l'Europe ; international — Lampyre). Les registres publics de haute fiabilité (A1) : cadastre.gouv.fr, publicité foncière, SCI via Pappers/Infogreffe, BODACC, JO associations, Légifrance jurisprudence.

**Faux positifs fréquents :** les homonymes sont le piège n°1 — deux personnes portent le même nom et l'investigateur attribue à sa cible des informations d'un tiers. Parade : toujours croiser avec 2+ sélecteurs indépendants (même ville ET même âge ET même employeur). Si la confirmation est impossible, l'attribution est « incertaine » et signalée comme telle dans le rapport.

#### 6.3 Recherche d'emails

Découverte : Hunter.io (emails par domaine + pattern), Phonebook.cz (emails dans les fuites), email permutator. Le pivot le plus puissant : **Holehe** et **Epieos** (vérifient sur quels services un email est enregistré sans alerter la cible). Si l'email est enregistré sur un exchange crypto = signal majeur dans une investigation financière.

**Limites :** ces outils open source se font régulièrement bloquer par les plateformes (rate limiting, changements d'API). Leur maintenance dépend de contributeurs bénévoles. Un résultat négatif (« email non trouvé ») ne signifie PAS que le compte n'existe pas — cela peut signifier que la détection a échoué. Compléter par des vérifications manuelles et des solutions commerciales maintenues.

#### 6.4 Recherche de numéros de téléphone

TrueCaller, Sync.me, annuaires inversés nationaux. Pivot vers les messageries : le numéro dans les contacts du téléphone d'investigation révèle WhatsApp (nom, photo, statut) et Telegram (username). Le dump Facebook 2021 (533M profils) relie des numéros à des profils.

#### 6.5 Recherche par username

**Sherlock** (300+ plateformes), **Maigret** (2500+, extraction de données), **WhatsMyName** (moins de faux positifs). Corrélation entre comptes : même avatar, même bio, même style, même fuseau horaire. **Piège :** les usernames recyclés — un username populaire peut avoir été utilisé par différentes personnes. La vérification de cohérence temporelle et stylistique est indispensable.

#### 6.6 Reconnaissance faciale

PimEyes, FaceCheck.id, Search4Faces (VK/OK), Yandex Images. La reconnaissance faciale **suggère, ne prouve jamais**. Le taux de faux positifs est significatif, le taux de faux négatifs aussi (angle différent, lunettes, coupe de cheveux). Chaque correspondance doit être validée par corroboration indépendante. **Risque juridique :** le RGPD classe les données biométriques comme sensibles — l'utilisation de la reconnaissance faciale par un privé est soumise à des précautions renforcées.

> **🎯 MIRAGE — Épisode 3 :** Holehe → comptes Binance, Coinbase, Instagram, Booking, Airbnb. Username Instagram marc_del75. Maigret → même username sur GitHub, forum voitures de luxe, poker en ligne. PimEyes → correspondance site de rencontres « Marco D., 48 ans, Paris ». Pappers → SCI Delaunay Patrimoine (bien 1,2 M€). Graphe : 5 emails, 8 comptes, 2 sociétés françaises, 1 bien immobilier.

---

### Chapitre 7 — SOCMINT : investigation sur les réseaux sociaux

Méthodologie en 5 étapes par plateforme : identification → extraction → analyse de contenu → analyse de réseau → préservation. Règle n°1 : **capturer avant disparition**.

**Facebook** : Google dorks site:facebook.com, extraction d'ID utilisateur, analyse amis/likes/groupes/événements, check-ins. Les restrictions croissantes (Graph Search supprimée, profils fermés par défaut) → dorks et outils tiers restent efficaces. **Instagram** : profils publics via web app, stories (capturer immédiatement), hashtags/localisation/tagged people, followers/following. **LinkedIn** : observation passive UNIQUEMENT (LinkedIn notifie les visites) → recherche via Google dorks site:linkedin.com. Les recommandations révèlent les relations professionnelles réelles. **Twitter/X** : recherche avancée (from: since: until: filter: geocode:), analyse de timeline. Adaptation 2025 : X quasi inaccessible sans API payante → instances Nitter (en déclin), archivage anticipé. **TikTok** : username/hashtag, localisation dans les vidéos. **Reddit** : historique complet (API, Redective), subreddits fréquentés.

**Faux positifs fréquents :** les comptes inactifs ou abandonnés (un profil Facebook datant de 2012 avec 0 activité récente peut être un ancien compte abandonné, pas le profil actif de la cible). Les comptes parodiques ou fan accounts (même nom, même photo, mais pas la même personne). Les informations auto-déclarées (un profil LinkedIn qui déclare un poste n'est pas une preuve que la personne occupe réellement ce poste — vérifier par d'autres sources). **Limite fondamentale :** les réseaux sociaux montrent ce que les gens veulent montrer — l'absence d'information sur un réseau social ne signifie pas l'absence de l'activité.

---

### Chapitre 8 — Telegram : investigation en profondeur

*Telegram est devenu LA plateforme d'investigation en 2025 — criminalité, extrémisme, marchés clandestins, fuites de données.*

Les **canaux et groupes** : canaux publics (indexés, cherchables), groupes (jusqu'à 200 000 membres). La recherche : recherche interne, Google dorks site:t.me, **TGStat** (statistiques et recherche de canaux), **Telepathy** (outil OSINT Telegram — collecte de messages, membres, métadonnées). L'investigation des **administrateurs** (numéro de téléphone parfois visible, bots associés, canaux croisés — un admin gère souvent plusieurs canaux). L'investigation des **membres** (dans les groupes publics : noms, usernames, parfois numéros). Les **bots** comme source (@getcontact_bot, @SangMata_bot — historique des changements de nom). Le **forwarding** (un message forwardé porte le nom du canal d'origine → révèle le réseau de canaux liés). Les canaux clandestins (vente de données, carding, accès — migration massive de Tor vers Telegram).

**Limites :** les bots d'investigation Telegram sont instables (bloqués, modifiés, ou supprimés régulièrement). Les numéros de téléphone des admins ne sont visibles que si la confidentialité n'est pas configurée correctement — de plus en plus d'admins masquent leur numéro. Les groupes privés nécessitent une invitation — l'investigateur privé ne peut pas y accéder sans compromettre son OPSEC. **Risque juridique :** rejoindre un groupe clandestin pour observer = zone grise ; interagir (poster, acheter) = potentiellement illégal pour un privé.

> **🎯 MIRAGE — Épisode 4 :** Delaunay admin du groupe Telegram « Offshore Trading Club » (560 membres) sous marc_offshore. Le numéro de l'admin = numéro du dump Facebook. Canal lié par forwarding : « Crypto Tax Free ». Graphe enrichi de 2 canaux, 560 contacts potentiels, liens vers des prestataires offshore.

---

## PARTIE III — SOURCES TECHNIQUES, DONNÉES EXPOSÉES ET DARK WEB

*Au-delà des réseaux sociaux, l'investigateur interroge les registres d'entreprises, l'infrastructure technique, les données fuitées et le dark web — des sources qui partagent un point commun : elles sont techniques, souvent structurées, et révèlent ce que la surface du web ne montre pas.*

---

### Chapitre 9 — Investigation corporate et structures juridiques

#### 9.1 Les registres d'entreprises par juridiction

**France** : Pappers (gratuit — RCS, statuts, comptes, dirigeants, bénéficiaires effectifs), Infogreffe (payant pour certains documents), BODACC, INPI. **UK** : Companies House (gratuit — comptes, dirigeants, PSC). **US** : SEC EDGAR (cotées), State registries. **Luxembourg** : LBR. **Suisse** : Zefix. **Multi-pays** : OpenCorporates, Orbis/BvD (commercial — le plus complet en international). Les **juridictions opaques** (BVI, Seychelles, Panama — registres inaccessibles → utiliser les leaks ICIJ, OCCRP, et les registres des juridictions de transit).

#### 9.2 Le workflow d'investigation corporate

Registre → dirigeants/actionnaires → UBO → screening PEP/sanctions → liens entre sociétés (mêmes dirigeants, même adresse, même expert-comptable) → analyse financière (comptes publiés) → OSINT technique (domaines, infrastructure) → cartographie réseau (Maltego). Les red flags : société récente avec CA élevé, adresse de domiciliation, pas de site web, pas d'employés visibles, dirigeants avec multiples mandats non liés, sociétés en cascade multi-juridictions.

#### 9.3 Les montages opaques

Sociétés écrans, trusts, nominees, layering, round-tripping. Pour chaque : principe, red flags, sources d'investigation. L'articulation : ce cours identifie les structures et les red flags ; le cours FININT analyse les flux financiers en profondeur.

**Faux positifs fréquents :** une société dans une juridiction offshore n'est pas intrinsèquement suspecte (de nombreuses structures légitimes utilisent des holdings luxembourgeoises ou irlandaises pour des raisons fiscales légales). Un nominee director n'est pas nécessairement un prête-nom criminel (c'est une pratique courante dans certaines juridictions). **Ce qui constitue un signal vs un élément corroboré :** une société au Panama = signal (à investiguer davantage). Une société au Panama + même adresse que 45 autres sociétés + nominee connu des leaks ICIJ + flux incohérents avec l'activité déclarée = faisceau d'indices fortement corroboré.

> **🎯 MIRAGE — Épisode 5 :** Pappers → TechnoVert SAS, Delaunay DAF. Recherche des mandats → SCI Delaunay Patrimoine + Delta Consulting Ltd (Malte, nominee maltais, centre de domiciliation avec 45 sociétés). ICIJ Offshore Leaks → pas de résultat direct mais adresse email deltaconsulting.mt liée à un prestataire chypriote des Pandora Papers. Le réseau se dessine.

---

### Chapitre 10 — Investigation sur les domaines, DNS et infrastructure

Le **Whois** (propriétaire, dates, registrar — beaucoup anonymisés RGPD ; les Whois historiques révèlent les anciens propriétaires — DomainTools, SecurityTrails). Le **DNS** : enregistrements A (IP), MX (serveur mail → fournisseur email), TXT (SPF, DKIM — révèlent les services utilisés), NS, CNAME, CAA. Les changements DNS dans le temps (SecurityTrails — historique complet). Les **certificats SSL/TLS** : crt.sh (Certificate Transparency — TOUS les certificats sont publics). Les SAN révèlent les domaines liés (*.technovert.fr et *.deltaconsulting.mt dans le même certificat = lien d'infrastructure).

Le **reverse DNS** et les sous-domaines (Sublist3r, Amass, SecurityTrails → cartographie de la surface). Le fingerprinting technologique (Wappalyzer, BuiltWith). L'analyse d'**adresses IP** (géolocalisation, ASN, Whois IP — RIPE/ARIN/APNIC). Les moteurs d'infrastructure : **Shodan** (services exposés), **Censys** (cartographie Internet). Le reverse IP (domaines co-hébergés → lien d'infrastructure).

**Limites :** les Whois anonymisés (RGPD) réduisent considérablement la valeur du Whois actuel — les Whois historiques (avant anonymisation) sont la source la plus riche. Les résultats Shodan/Censys ne sont pas en temps réel (scans périodiques) — un service exposé hier peut être fermé aujourd'hui. Le reverse IP sur un hébergeur mutualisé (OVH, AWS) peut montrer des milliers de domaines co-hébergés sans lien entre eux — le co-hébergement n'est un signal que sur un serveur dédié ou un petit hébergeur.

---

### Chapitre 11 — Breaches, leaks et exploitation de données fuitées

*Les données fuitées sont parmi les sources OSINT les plus puissantes — et les plus sensibles juridiquement.*

Les sources : Have I Been Pwned (vérification gratuite, 14 Mrd de comptes), DeHashed (recherche par email, username, nom, IP, téléphone), Snusbase, Intelligence X (archives de pastes et leaks). L'exploitation comme pivot : un email dans un dump avec un mot de passe révèle les habitudes (mots de passe réutilisés), un numéro dans le dump Facebook 2021 lie un numéro à un profil, le dump Ledger 2020 révèle les détenteurs de crypto-hardware.

**Cadre légal :** la consultation de données fuitées accessibles en sources ouvertes est une zone grise — les données sont techniquement accessibles mais leur collecte initiale est illicite. Les LEA et CRF les exploitent ; les investigateurs privés doivent documenter la source et la méthode, et ne pas les utiliser comme preuve unique mais comme piste à corroborer par des sources indépendantes. La sécurisation : VM dédiée, stockage chiffré, suppression après usage, ne JAMAIS télécharger de dumps massifs sur une machine non sécurisée.

**Ce qui constitue une piste vs un élément corroboré :** un email trouvé dans un dump = piste (l'email existait au moment de la fuite). Un email dans un dump Ledger + un compte Binance identifié via Holehe + une adresse Bitcoin publiée sur Telegram = faisceau convergent fortement corroboré (le suspect détient des crypto-actifs).

> **🎯 MIRAGE — Épisode 6 :** DeHashed → marcdelaunay75@gmail.com présent dans les dumps LinkedIn 2021, Adobe 2013, Ledger 2020. Le dump Ledger confirme la détention d'un hardware wallet crypto. Le mot de passe Adobe (« Marco75Paris! ») est cohérent avec le pattern marc_del75 / Marco D.

---

### Chapitre 12 — Dark Web et DARKINT

*Le dark web est à la fois une source d'investigation et un terrain d'enquête. Ce chapitre couvre les deux dimensions de manière opérationnelle.*

#### 12.1 Accès et navigation

Le dark web est un ensemble de réseaux accessibles via des protocoles spécifiques : **Tor** (sites .onion — le plus courant), **I2P** (services .i2p — plus niche). Accès obligatoirement depuis une VM dédiée avec OPSEC maximale (Tails ou Whonix). Les erreurs courantes : accéder sans VM, cliquer sur des liens non vérifiés, interagir avec des vendeurs (ligne rouge pour un privé).

#### 12.2 Les sources principales

Les **forums cybercriminels** : vente d'accès (RDP, VPN, credentials — Initial Access Brokers), vente de données volées, outils (malware, exploits, kits de phishing), et services (blanchiment, cashout, faux documents). Les **marketplaces** (drogues, armes, services). Les **paste sites** (fuites de données, dox, revendications). Le **Telegram comme extension du dark web** : en 2024-2025, une grande partie de l'activité clandestine a migré de Tor vers Telegram — vente de données, carding, distribution de malware. Cette migration est motivée par la facilité d'accès (pas besoin de Tor), la rapidité, et le volume d'utilisateurs (Ch.8).

#### 12.3 L'OSINT sur le dark web

Les erreurs OPSEC des criminels sont la principale source d'investigation : un vendeur qui réutilise un username entre le dark web et un réseau social clearnet, un PGP key avec un email identifiable (le fingerprint PGP est un pivot vers l'identité), une adresse Bitcoin réutilisée entre le dark web et un exchange KYC (Ch.16), des métadonnées dans des fichiers partagés (PDF avec auteur, images avec EXIF), et des patterns stylistiques (même style d'écriture entre un profil dark web et un profil clearnet).

Le **monitoring dark web** : outils commerciaux (Flare, Recorded Future, DarkOwl — alertes quand des données de l'organisation apparaissent), outils open source (Ahmia — moteur de recherche .onion, Torch). Les moteurs indexent une fraction du contenu — la majorité des forums nécessite un compte et une « réputation ».

**Limites pour l'investigateur privé :** la consultation est légale (observer un forum n'est pas un crime). L'interaction (acheter, vendre, participer) est très risquée juridiquement et opérationnellement. L'investigateur privé **observe et documente** — il ne participe PAS. Les LEA ont un cadre différent (opérations sous couverture, achat contrôlé). Le cours Dark Web de la bibliothèque traite ces opérations en profondeur.

**Faux positifs :** les vendeurs dark web utilisent des noms et des marques pour attirer (un forum « FrenchHackers » n'est pas nécessairement français). Les données vendues sont souvent recyclées ou fausses (un vendeur qui prétend vendre 10 millions de comptes peut vendre un vieux dump déjà public). La vérification est indispensable avant de traiter une information dark web comme fiable.

---

## PARTIE IV — IMINT, GEOINT ET VÉRIFICATION VISUELLE

---

### Chapitre 13 — IMINT : analyse d'images et recherche inversée

La **recherche inversée** : Google Images (le plus large index), Yandex Images (supérieur pour les visages), TinEye (le plus fiable pour trouver la source originale — tri par date), Bing Visual Search, Google Lens. Les métadonnées **EXIF** : coordonnées GPS, appareil, date/heure — ExifTool. La plupart des réseaux sociaux suppriment les EXIF au upload — mais les images par email ou messagerie (WhatsApp en mode document) les conservent souvent.

L'**analyse sans EXIF** (le cas le plus fréquent) : indices visuels systématiques — enseignes (langue, marque), plaques d'immatriculation (format), végétation (espèces → climat), architecture (style → culture), signalétique routière (panneaux → pays), uniformes, conditions météo. Chaque indice est un pivot de géolocalisation.

La **vérification d'authenticité** : Error Level Analysis (ELA — les zones modifiées ont un niveau d'erreur différent — FotoForensics), cohérence des ombres (direction et longueur cohérentes ?), recherche de première occurrence (TinEye tri par date — si l'image existait avant l'événement prétendu, c'est du recyclage).

**Limites :** la recherche inversée ne fonctionne que si l'image (ou une version proche) est indexée — une photo originale non publiée ne donnera aucun résultat. L'ELA a des limites (les compressions multiples JPEG créent des artefacts qui ressemblent à des modifications). L'analyse des ombres nécessite des ombres visibles et un sol plat. **La convergence de plusieurs indices est toujours plus fiable qu'un seul test technique.**

---

### Chapitre 14 — Contenus AI-generated et deepfakes : méthodologie de vérification

*Ce chapitre est méthodologique. Les outils de détection vieillissent vite et ne sont jamais fiables seuls. La discipline de vérification, elle, reste.*

#### 14.1 Le principe fondamental

**Absence de preuve de manipulation ≠ authenticité.** Un outil de détection qui dit « probablement authentique » ne PROUVE PAS l'authenticité. Un outil qui dit « probablement AI-generated » donne un indice, pas une certitude. **Un seul indice technique ne suffit jamais** — la vérification repose sur la convergence de multiples indicateurs indépendants.

#### 14.2 Images synthétiques

Signaux visuels (avec la précaution qu'ils deviennent de moins en moins fiables) : mains/doigts incohérents (de moins en moins discriminant), texte dans l'image illisible, arrière-plans avec structures impossibles, symétrie excessive des visages, métadonnées absentes (les images IA n'ont pas d'EXIF caméra — mais l'absence d'EXIF n'est pas une preuve de synthèse puisque les réseaux sociaux les suppriment aussi).

La méthodologie de vérification (plus fiable que les outils seuls) : (1) recherche inversée — l'image existe-t-elle ailleurs avant la date prétendue ? (2) vérification des métadonnées, (3) ELA, (4) contexte — l'image est-elle cohérente avec d'autres sources ? (5) corroboration — d'autres sources confirment-elles le contenu ? Les outils de détection (Hive Moderation, Illuminarty, SynthID — exemples à date) sont des **aides, pas des verdicts**.

#### 14.3 Deepfakes vidéo, audio et texte

Vidéo (face swap, lip sync) : clignement anormal, contour du visage flou, incohérence d'éclairage. Audio (voice cloning) : microprosodie anormale, transitions abruptes. Texte : la détection technique est la moins fiable (taux de faux positifs élevé) → vérifier les faits cités (l'IA hallucine), rechercher la première occurrence, comparer le style (stylométrie).

#### 14.4 Impact sur l'investigation

Un suspect peut publier de fausses preuves AI-generated. Une campagne de désinformation peut fabriquer des « preuves » visuelles. L'analyste OSINT doit **systématiquement vérifier l'authenticité AVANT d'utiliser un contenu comme élément d'analyse** — et documenter la vérification dans le rapport avec le niveau de confiance.

> **🎯 MIRAGE — Épisode 7 :** Delaunay publie une photo « preuve » de sa présence à Genève le jour d'une transaction suspecte. Vérification : (1) recherche inversée → aucune source antérieure ni confirmante, (2) EXIF → absentes, (3) ELA → incohérences, (4) contexte → la configuration du lieu ne correspond pas (Google Street View), (5) corroboration → aucun participant ne mentionne Delaunay. Conclusion : probablement synthétique ou manipulée — cotation E5. Non utilisable comme preuve, documentée comme tentative d'alibi.

---

### Chapitre 15 — GEOINT : géolocalisation, chronolocation et OSINT spatial

La **géolocalisation par indices visuels** (méthode Bellingcat) : enseignes (langue, marque → pays/ville), plaques d'immatriculation (format → pays), signalétique routière (panneaux, marquage → normes locales), végétation (espèces → climat/région), architecture (style → culture/époque), soleil et ombres (direction → hémisphère, longueur → latitude et heure). Outils : Google Maps, Street View, Mapillary, KartaView, Sentinel Hub.

La **chronolocation** : ombres → angle du soleil → calculable via SunCalc (suncalc.org) pour un lieu et une date ; conditions météo → archives (Weather Underground, ogimet.com). L'**OSINT géospatial** : imagerie satellite (Sentinel-2 — gratuit 10m, Google Earth — historique 20+ ans, Maxar/Planet — commercial haute résolution). L'OSINT **maritime** (MarineTraffic, VesselFinder — AIS tracking, historique des routes). L'OSINT **aéronautique** (FlightRadar24, ADS-B Exchange — historique de vols ; un jet privé Paris → Malte → Chypre régulièrement = indicateur). L'OSINT **véhicules** (plaques par pays, immatriculations aéronautiques, numéros de coques).

**Limites :** la géolocalisation par indices visuels nécessite des indices visibles — une photo en intérieur sans fenêtre est quasi impossible à localiser. Google Street View ne couvre pas toutes les régions (Afrique subsaharienne, Asie centrale — couverture partielle). La chronolocation par ombres nécessite un sol plat et des ombres nettes. **Risque de sur-interprétation :** un panneau en arabe ne signifie pas « Syrie » — il peut être au Maroc, en Tunisie, en Jordanie, en Irak. La combinaison de multiples indices est la seule approche fiable.

---

## PARTIE V — CRYPTO, FINANCE, CTI ET ANALYSE

*Cinq chapitres avec chacun un angle précis : Ch.16 = blockchain OSINT (tracer les fonds), Ch.17 = finance et compliance (évaluer une structure), Ch.18 = CTI (l'OSINT au service de la cybersécurité), Ch.19 = techniques d'adaptation (contourner les restrictions, automatiser), Ch.20 = analyse et vérification finale (produire le renseignement).*

---

### Chapitre 16 — Crypto-actifs et blockchain OSINT

*Angle : tracer les fonds sur la blockchain et faire le lien avec l'identité. Le cours OSINT Expert & Crypto-Actifs approfondit le traçage avec les outils professionnels et les schémas de blanchiment crypto avancés.*

#### 16.1 Concepts pour l'investigateur

**Bitcoin** : pseudo-anonyme (adresses publiques, transactions publiques, identité derrière l'adresse = investigation OSINT). Explorateurs : Blockchain.com, Blockchair, OXT. **Ethereum** : comptes + tokens + smart contracts ; Etherscan. **Stablecoins** (USDT/USDC — la majorité des flux illicites en 2025 passe par les stablecoins, principalement USDT sur TRON — Tronscan). Les **exchanges** (Binance, Coinbase, Kraken — les exchanges KYC sont le point de dé-anonymisation : la réquisition judiciaire révèle l'identité).

#### 16.2 Les pivots OSINT → crypto

Un email lié à un exchange via Holehe (signal fort), un ENS (.eth → adresse Ethereum), une adresse publiée sur un profil (forum, Telegram, site web, QR code), un wallet hardware via un leak (dump Ledger 2020), un paiement crypto visible sur la blockchain.

#### 16.3 Investigation blockchain de base

Explorer une adresse : volume total, nombre de transactions, dates, adresses en relation. Le **clustering** (heuristiques de co-spending — si deux adresses sont inputs dans la même transaction, elles appartiennent probablement au même wallet). Le suivi des flux : adresse → adresse → exchange KYC → réquisition = identité. Outils : explorateurs gratuits (Blockchain.com, Etherscan, Tronscan), OXT (analyse graphique Bitcoin), outils professionnels (Chainalysis Reactor, TRM Labs, Elliptic — cours OSINT Crypto pour la profondeur).

#### 16.4 Limites et schémas d'opacification

Les **mixers/tumblers** (mélangent les fonds → cassent la traçabilité — le traçage au-delà nécessite des outils pro et des heuristiques probabilistes). Les **bridges cross-chain** (Bitcoin → Ethereum → TRON — complique le suivi). Le **DeFi** (exchanges décentralisés sans KYC → traçage possible mais complexe). Les **privacy coins** (Monero — traçage extrêmement difficile). L'analyste OSINT doit connaître ces limites et savoir quand le traçage nécessite une expertise spécialisée.

**Ce qui constitue une piste vs un élément corroboré :** une adresse Bitcoin trouvée sur un profil Telegram = piste. La même adresse avec des flux vers un exchange KYC dont le compte est au nom du suspect (via Holehe + corroboration) = élément fortement corroboré.

> **🎯 MIRAGE — Épisode 8 :** L'adresse Bitcoin du groupe Telegram (bc1q...xyz) → Blockchain.com → 12,4 BTC sur 18 mois, flux vers Binance. Le compte Binance de Delaunay (identifié via Holehe) correspond. Lien OSINT → blockchain → exchange KYC établi.

---

### Chapitre 17 — OSINT financier, corporate avancé et compliance

*Angle : évaluer une structure et un individu par les sources financières ouvertes. Le cours FININT approfondit le renseignement financier institutionnel (CRF, analyse de flux, typologies de blanchiment).*

#### 17.1 Analyse financière par sources ouvertes

Les comptes publiés (Infogreffe, Companies House, SEC EDGAR). Red flags comptables pour l'analyste OSINT : CA en forte croissance sans explication, charges de « conseil » à des sociétés liées, résultat très faible malgré un CA élevé, absence de commissaire aux comptes au-delà des seuils. **Limite :** les comptes publiés sont une déclaration — ils montrent ce que la société veut montrer. L'analyste cherche les incohérences entre les comptes, les flux visibles et la réalité opérationnelle.

#### 17.2 Due diligence et KYC/AML

Le KYC utilise l'OSINT pour vérifier l'identité au-delà des documents (profil LinkedIn cohérent ? présence en ligne plausible ? sanctions ?). Screening sanctions (OFAC, listes UE, ONU). Identification PEP (dirigeants politiques, hauts fonctionnaires, proches). Due diligence approfondie M&A (le cours IE traite l'IE stratégique — ici c'est la composante OSINT).

#### 17.3 Investigation patrimoniale

L'immobilier (cadastre, publicité foncière, SCI), les véhicules, les biens de luxe (bateaux, avions — registres d'immatriculation publics), le train de vie visible (Instagram, Facebook — voyages, hôtels, marques). L'incohérence patrimoine/revenus est un signal fort.

**Faux positifs :** un patrimoine élevé peut être hérité, pas nécessairement frauduleux. Un dirigeant qui possède une société au Luxembourg peut faire de l'optimisation fiscale légale. **Distinguer signal et corroboration :** patrimoine incohérent avec les revenus = signal à investiguer. Patrimoine incohérent + sociétés offshore + flux crypto + train de vie excessif = faisceau convergent.

---

### Chapitre 18 — OSINT et cybersécurité : Threat Intelligence

*Angle : comment l'OSINT alimente la CTI. Le cours CTI approfondit le cycle de renseignement de menace, les frameworks (ATT&CK, Diamond Model), et la production CTI.*

#### 18.1 L'OSINT comme source de CTI

Les APT et cybercriminels laissent des traces en sources ouvertes : infrastructure C2 dans DNS/certificats (domaines C2 enregistrés avec des patterns détectables — DGA, typosquatting, domaines récents), malware sur VirusTotal (relations entre fichiers, domaines, IPs), communications sur forums dark web et Telegram (acteurs qui recrutent, vendent, discutent), et code sur GitHub (malwares, exploits, outils offensifs publiés).

#### 18.2 Reconnaissance offensive passive

Ce que le pentester collecte en OSINT avant de tester : DNS/sous-domaines (Amass, Sublist3r → surface d'attaque), services exposés (Shodan, Censys → versions vulnérables), technologies web (Wappalyzer → CMS, frameworks), emails d'employés (Hunter.io → phishing ciblé), credentials dans les leaks (DeHashed → password spraying).

#### 18.3 Monitoring de surface d'attaque

Surveiller en continu : domaines, sous-domaines, services exposés (SecurityTrails, Censys), fuites de credentials (Intelligence X, paste sites), mentions sur forums dark web et Telegram.

**Limites :** le monitoring de surface d'attaque ne couvre que ce qui est exposé et indexé. Un C2 sur une infrastructure cloud éphémère (serverless) peut être invisible pour Shodan/Censys. Les IOCs trouvés en OSINT doivent être vérifiés — un domaine similaire peut être un typosquatting légitime (une entreprise qui enregistre des variantes défensives de son propre domaine).

---

### Chapitre 19 — Restrictions de plateformes, techniques avancées et automatisation

*Angle : comment continuer à collecter quand les plateformes ferment leurs portes, et comment automatiser la collecte à l'échelle.*

#### 19.1 Les restrictions 2025

X/Twitter quasi inaccessible sans API payante, LinkedIn bloque les profils OSINT, Facebook restreint les recherches, Instagram limite l'accès sans compte, Google réduit les résultats des dorks avancés. Ces restrictions transforment l'OSINT : ce qui était simple en 2020 est devenu complexe en 2025.

#### 19.2 Stratégies d'adaptation

L'archivage anticipé (capturer AVANT que les données ne deviennent inaccessibles), les APIs alternatives (Nitter pour X — instances en déclin mais encore utiles à date, unddit pour Reddit supprimé), les moteurs alternatifs (Yandex, Baidu), le Google Cache, la recherche multi-langues (translitération, moteurs locaux). Chaque stratégie a une durée de vie — l'adaptabilité est la compétence, pas la connaissance d'un outil spécifique.

#### 19.3 Automatisation Python

requests (APIs), BeautifulSoup (parsing HTML), Selenium (sites dynamiques), Scrapy (crawling à grande échelle), pandas (traitement de données), networkx (graphes), rapidfuzz (entity resolution). La gestion des anti-scraping (rotation user-agents, délais, proxies, CAPTCHAs). Les APIs (Shodan, VirusTotal, Reddit/PRAW — pagination, rate limiting, authentification). Les LLMs comme assistant (résumé, extraction d'entités — avec précaution : les LLMs hallucinent → vérifier chaque fait).

---

### Chapitre 20 — Analyse, vérification et production de renseignement

*Angle : transformer les données collectées en renseignement fiable — c'est la compétence qui distingue l'analyste du chercheur amateur.*

L'**ACH** (Analysis of Competing Hypotheses) : H1 Delaunay détourne des fonds, H2 optimisation fiscale agressive mais légale, H3 innocent. Tester chaque hypothèse contre les évidences : quel fait est compatible avec H1 mais pas H2 ? Quel fait pourrait invalider H1 ? L'ACH force l'analyste à considérer les alternatives et à documenter son raisonnement.

La **cotation de fiabilité** (grille A-F/1-6 — chaque fait porte une cotation explicite). La **corroboration multi-sources** (un fait n'est établi que s'il est confirmé par 2+ sources indépendantes). Les **biais cognitifs** : biais de confirmation (on cherche ce qui confirme notre hypothèse), biais d'ancrage (la première info pèse trop), biais de disponibilité (on surestime ce qui est facilement trouvable), effet de halo (un suspect qui ment sur un point est suspecté de tout — ce n'est pas nécessairement vrai). La **timeline** (chronologie annotée — ordonne les éléments dans le temps et révèle les corrélations temporelles).

**La distinction fondamentale** — ce qui constitue une piste vs un élément corroboré : une piste = un indice unique, issu d'une source, non vérifié par une source indépendante (ex : un username commun entre deux plateformes). Un élément corroboré = un indice confirmé par 2+ sources indépendantes (ex : le même username + même avatar + même fuseau horaire + même style d'écriture sur deux plateformes). Le rapport doit distinguer les deux explicitement.

---

## PARTIE VI — DU RENSEIGNEMENT À L'ACTION

*Transformer l'investigation en livrables exploitables — le rapport, le cadre judiciaire, la veille, la désinformation, et l'adaptation de la méthode aux contextes spécifiques.*

---

### Chapitre 21 — Rédaction du rapport d'investigation OSINT

La structure du rapport professionnel : **sommaire exécutif** (1 page pour le décideur — conclusions, confiance, recommandations critiques), **mandat et périmètre**, **méthodologie et sources** (transparence totale), **constatations** (chaque fait avec source, date, cotation A-F/1-6, capture horodatée en annexe), **analyse** (ACH, timeline, inférences), **conclusions** (réponse aux questions d'investigation avec niveau de confiance — « les éléments sont compatibles avec... » pas « il est coupable de... »), **recommandations** (pistes, réquisitions), **annexes** (captures hashées, graphes, timelines).

Le **graphe relationnel** (la visualisation la plus impactante pour le client). La **timeline** (le « quand » de chaque événement). Le **vocabulaire calibré** (renseignement ≠ verdict — le rapport fournit du renseignement, le tribunal établit la culpabilité).

---

### Chapitre 22 — OSINT et investigation judiciaire

Investigateur privé vs LEA : le privé fait l'OSINT en sources ouvertes, les LEA font les réquisitions (opérateurs télécom, plateformes, banques), interceptions, perquisitions, auditions, gel d'actifs. Le rapport OSINT fournit la trame investigative, les autorités complètent avec les moyens légaux.

La transmission : format exploitable par les enquêteurs, preuves préservées (hash, horodatage, chaîne de custody), pistes de réquisitions identifiées (quelles données, à quel opérateur, pour quel motif). Le dépôt de plainte (procureur, services spécialisés — C3N cyber, OCLCTIC criminalité financière, JUNALCO crime organisé). L'expertise judiciaire OSINT (expert mandaté par un magistrat, cadre contradictoire, rapport à valeur probante).

---

### Chapitre 23 — Veille opérationnelle et monitoring continu

La veille post-rapport : le suspect tente de supprimer des preuves (dissolution de sociétés, passage en privé, suppression de contenus) → l'archivage anticipé protège. Les outils de monitoring : alertes Google (noms, sociétés), monitoring DNS/Whois (SecurityTrails), monitoring réseaux sociaux (Mention, Brand24 — exemples à date), monitoring dark web/Telegram. La collecte en temps réel (surveillance d'événement en cours — agrégation X, Telegram, médias, webcams). Le geofencing (publications géolocalisées dans une zone). La coordination d'équipe (répartition, fusion, déconfliction).

> **🎯 MIRAGE — Épisode 9 :** Semaine 3 post-rapport. Alerte Google : dissolution volontaire de Delta Consulting Ltd (Malte). Le suspect tente de faire disparaître la structure avant les autorités. Capture immédiate (Hunchly). Le profil Instagram marc_del75 passe en privé — captures déjà réalisées. Le blog antiwhistleblower.com est mis hors ligne — Wayback Machine conserve le contenu.

---

### Chapitre 24 — Désinformation, influence et fact-checking

*Ce chapitre enseigne la détection et l'investigation de la désinformation comme compétence OSINT opérationnelle — pas comme un résumé académique.*

La **détection de faux comptes** : signaux (création récente, nom générique ou généré, photo AI-generated ou volée — recherche inversée, peu de publications originales, activité coordonnée, ratio followers/following anormal). L'**analyse de réseau coordonné** : les faux comptes interagissent entre eux et partagent les mêmes contenus dans les mêmes fenêtres temporelles (±5 minutes) → le réseau est identifiable par les patterns d'interaction et de timing. L'**analyse d'infrastructure** : les liens partagés pointent vers des domaines enregistrés récemment, souvent le même jour, hébergés sur la même infrastructure → DNS/Whois révèle les liens.

L'**attribution** : relier les faux comptes à leur opérateur (infrastructure — les domaines sont enregistrés avec un email identifiable, patterns linguistiques, fuseaux horaires). Le **fact-checking** : vérification de l'image originale (TinEye — recyclage), vérification géographique (Street View), vérification temporelle (archives météo), vérification de source (le média cité existe-t-il ? l'expert a-t-il dit ce qu'on lui attribue ?).

**Limites :** l'attribution de campagnes de désinformation est intrinsèquement incertaine — les opérateurs utilisent des VPN, des domaines jetables, et des identités multiples. Un réseau de faux comptes coordonnés est un signal fort, mais l'attribution au commanditaire final nécessite souvent des preuves que seules les LEA peuvent obtenir (réquisitions aux plateformes, aux registrars). **Risque :** accuser publiquement un acteur de désinformation sans preuves solides = diffamation potentielle.

> **🎯 MIRAGE — Épisode 10 :** Blog antiwhistleblower.com — Whois historique → email de création marc.consulting@proton.me, même email dans le SPF de deltaconsulting.mt. Lien Delaunay → blog établi. 8 faux comptes Twitter amplifient le blog — création le même jour, photos AI-generated, patterns de publication identiques. Campagne documentée.

---

### Chapitre 25 — Adapter la méthodologie OSINT aux contextes spécialisés

*Ce chapitre ne liste pas des domaines — il montre comment la même méthodologie OSINT s'adapte à différents contextes, ce qui change et ce qui reste constant.*

#### 25.1 Le noyau méthodologique invariant

Quel que soit le contexte (financier, criminel, géopolitique, corporate), le cycle du renseignement reste le même (orientation → collecte → traitement → analyse → diffusion), la logique du pivot reste la même (un sélecteur mène à un autre), la cotation de fiabilité reste la même (A-F/1-6), et la discipline de vérification reste la même (corroboration multi-sources, ACH). Ce qui change, c'est le **focus des sources**, les **types de sélecteurs prioritaires**, et les **red flags spécifiques** au domaine.

#### 25.2 Les adaptations par contexte

L'**investigation financière/compliance** (KYC/AML, due diligence) : les sources prioritaires sont les registres d'entreprises, les comptes publiés, les listes de sanctions, et les leaks ICIJ. Le sélecteur prioritaire est la société (pas la personne — on part de la structure pour remonter à l'individu). Les red flags sont les montages multi-juridictions, les nominees, et les flux incohérents. L'erreur courante est de conclure « suspect » sur la base d'une seule société offshore sans autre élément.

L'**investigation criminelle** (personnes disparues, traite, extrémisme) : les sources prioritaires sont les réseaux sociaux (SOCMINT intensive), les messageries (Telegram, WhatsApp), les archives de données (Wayback Machine pour les profils supprimés). Le sélecteur prioritaire est la personne (dernier lieu connu, dernières connexions, réseau social). La spécificité est la dimension humanitaire (Trace Labs pour les personnes disparues) ou la dimension sécuritaire (surveillance de la radicalisation). L'erreur courante est de confondre un individu radicalisé en ligne avec un individu qui passe à l'acte — le discours n'est pas l'action.

L'**investigation conflits/géopolitique** (méthodologie Bellingcat) : les sources prioritaires sont l'imagerie satellite (Sentinel-2, Google Earth historique), les vidéos géolocalisées (GEOINT), et les bases de données de mouvements (FlightRadar24, MarineTraffic). Le sélecteur prioritaire est le lieu et le temps (pas la personne). La spécificité est la chronolocation et la vérification d'authenticité (Ch.13-14). L'erreur courante est de prendre une vidéo virale pour argent comptant sans vérifier le lieu, la date et l'authenticité.

L'**investigation réputationnelle** (e-réputation, défense) : les sources prioritaires sont les moteurs de recherche (Google — ce que les gens voient en premier), les réseaux sociaux (mentions, tags), et les avis en ligne. Le sélecteur prioritaire est le nom de la personne/marque. La spécificité est le volet défensif (droit à l'oubli RGPD, suppression de données personnelles, nettoyage de résultats).

---

## PARTIE VII — CAS DE SYNTHÈSE ET RÉFÉRENCE

---

### Chapitre 26 — Cas complet : synthèse Opération MIRAGE

Synthèse du fil rouge. De la sollicitation du cabinet Legrand & Associés au rapport final transmis aux autorités.

**Le schéma reconstitué :** Delaunay, DAF de TechnoVert, détourne des fonds via des paiements de « consulting » à Delta Consulting Ltd (Malte) — société contrôlée via un nominee maltais mais dont l'infrastructure est liée à Delaunay (email SPF, certificat SAN, Whois historique). Les fonds transitent de Malte vers un prestataire chypriote (identifié dans les Pandora Papers via ICIJ). Une partie est convertie en Bitcoin via Binance (compte KYC au nom de Delaunay — identifié via Holehe, adresse publiée sur Telegram, flux tracés sur la blockchain). L'immobilier (SCI, 1,2 M€) et le train de vie (forum luxe, voyages Instagram) sont incohérents avec les revenus déclarés. Parallèlement, Delaunay a orchestré une campagne de désinformation (blog lié par Whois historique, 8 faux comptes Twitter coordonnés, photos AI-generated) et publié une photo synthétique pour créer un faux alibi (détecté par la méthodologie de vérification Ch.14).

**Livrables :** rapport 25 pages (sommaire exécutif, 47 constatations cotées, ACH, conclusions avec niveaux de confiance, recommandations), graphe relationnel (47 entités, 83 relations, 5 juridictions), timeline 3 ans, annexes hashées, pistes de réquisitions (Binance KYC, Telegram admin, opérateur télécom, publicité foncière). Le C3N reprend avec les pouvoirs légaux — gel des actifs par ordonnance du juge.

---

### Chapitre 27 — Cas complet : investigation GEOINT

Une vidéo virale prétend montrer un événement dans un pays. L'investigateur applique la méthodologie complète : extraction d'indices visuels (enseignes en arabe dialecte spécifique, plaques format jordanien, signalétique non cohérente avec le pays prétendu, végétation méditerranéenne), hypothèses de localisation (3 villes possibles), vérification via Street View/Mapillary (correspondance exacte d'un carrefour), chronolocation par SunCalc (ombres → 14h30 le 15 mars, cohérent avec les archives météo), vérification d'authenticité (TinEye — pas de recyclage, ELA — pas de manipulation). Conclusion : la vidéo est authentique mais le lieu n'est pas celui prétendu.

---

### Chapitre 28 — Cas complet : dé-anonymisation d'un compte pseudonyme

Un compte pseudonyme « insider_leak42 » publie des informations confidentielles sur une entreprise. Username → Maigret → même username sur GitHub et forum de jeux. GitHub → commit signé avec j.martin.dev@outlook.com. Holehe → profils LinkedIn et Instagram. Instagram photo → PimEyes → correspondance avec Julien Martin, développeur chez l'entreprise. Corrélation : même fuseau horaire (posts Twitter et commits GitHub aux mêmes heures), même style d'écriture, même intérêts. L'attribution est « haute probabilité » (pas certitude). **Limites documentées :** le username pourrait avoir été recyclé, l'email pourrait être un piège, la reconnaissance faciale est un indice pas une preuve.

---

### Chapitre 29 — Cas complet : vérification d'une campagne de désinformation

Un réseau de faux comptes sur X et Telegram diffuse de fausses informations sur une entreprise cotée (impact sur le cours). Détection (12 comptes créés le même jour, photos AI-generated — aucune source en recherche inversée), analyse réseau (retweets mutuels, timing identique ±5 min), analyse infrastructure (3 domaines enregistrés le même jour, même registrar, même serveur — Whois + reverse IP), attribution (email dans le Whois historique lié à un concurrent), documentation (timeline, graphe, preuves cotées B2 — source fiable + info probablement vraie). Le cas illustre la convergence SOCMINT + OSINT technique + IMINT + analyse de réseau.

---

### Chapitre 30 — Exercice : investigation OSINT complète (non guidé)

Un exercice non guidé : scénario réaliste (individu suspect + sociétés + dimension internationale + Telegram + crypto). Sélecteurs initiaux fournis. L'étudiant doit : cadrer les questions, définir le plan de collecte, mener l'investigation en 8 heures, et produire un rapport complet (sommaire exécutif, constatations cotées A-F/1-6, graphe relationnel, timeline, ACH, annexes hashées, recommandations de réquisitions). Grille d'auto-évaluation fournie (cadrage, OPSEC, diversité des sources, qualité des pivots, cotation de fiabilité, identification des faux positifs, qualité du rapport, documentation des limites).

---

## ANNEXES

---

### Annexe A — Glossaire OSINT

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

### Annexe B — Cheat sheets par plateforme

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

### Annexe C — Outils OSINT : référence à date (2025-2026)

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

### Annexe D — Templates d'investigation

**Rapport OSINT :** Sommaire exécutif → Mandat/périmètre → Méthodologie/sources → Constatations (fait + source + date + cotation + capture) → Analyse (ACH, timeline) → Conclusions (niveaux de confiance) → Recommandations → Annexes

**Fiche de cadrage :** Client → Objet → Questions d'investigation → Sélecteurs initiaux → Périmètre (géo, temporel, thématique) → Contraintes (délai, budget, OPSEC) → Livrables attendus

**Journal d'investigation :** Date/Heure → Source → Requête/Action → Résultat → Sélecteur découvert → Cotation → Capture (réf.)

---

### Annexe E — Workflow d'enquête en 10 étapes

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

### Annexe F — Mapping de la bibliothèque

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

### Annexe G — Ressources, formations et lab

#### Formations

| Formation | Organisme | Focus |
|-----------|----------|-------|
| SEC497 / GOSI | SANS / GIAC | OSINT complète — référence mondiale |
| PORP | TCM Security | Practical OSINT Research Professional |
| OSIP | IntelTechniques | Méthodologie complète (Michael Bazzell) |

#### Communautés

| Ressource | Type |
|-----------|------|
| OSINT Curious | Podcast, blog, CTF |
| Sector035 | Newsletter « Week in OSINT » |
| Trace Labs | CTF OSINT humanitaires |
| Bellingcat | Investigations de référence |

#### Lab

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
