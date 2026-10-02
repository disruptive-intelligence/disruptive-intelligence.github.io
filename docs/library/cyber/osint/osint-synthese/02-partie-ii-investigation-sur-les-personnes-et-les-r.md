---
title: Partie II — Investigation sur les personnes et les réseaux sociaux
source: Cyber/02 OSINT/Méthode & enquête/OSINT — synthèse.md
note: OSINT — synthèse
up:
- - OSINT — synthèse
  - index.md
---

---


## Chapitre 5 — Moteurs de recherche et Google Dorking

Les moteurs : **Google** (index le plus large, opérateurs avancés), **Bing** (indexe des résultats différents — toujours tester les deux), **Yandex** (supérieur pour la reconnaissance faciale et le contenu non-anglophone), **DuckDuckGo** (agrège Bing sans tracking), **Baidu** (contenu chinois). Les **Google Dorks** : site:, filetype:, intitle:, inurl:, AROUND(n), before:/after:, cache:, "exact phrase", -exclusion. Les dorks par objectif : documents financiers, organigrammes, emails exposés, directory listings, mentions officielles, recherche temporelle.

L'**archivage web** : Wayback Machine (retrouver des contenus supprimés, comparer les versions passées — l'outil de vérification temporelle le plus puissant), archive.today (capture instantanée), Google Cache (dernière version indexée).

**Limites et faux positifs :** les dorks ne renvoient que ce que Google a indexé — le contenu non indexé (deep web) est invisible. Les résultats sont influencés par la personnalisation, la localisation et le filtre SafeSearch. Un résultat Google n'est pas une preuve — c'est une piste à vérifier.

> **🎯 MIRAGE — Épisode 2 :** Google Dorking. "Marc Delaunay" site:linkedin.com → profil identifié. "m.delaunay" filetype:pdf → CV trouvé avec email perso marcdelaunay75@gmail.com. "TechnoVert" "Delta Consulting" → document PDF maltais mentionnant les deux entités.

---


## Chapitre 6 — Investigation sur les personnes

### 6.1 La logique du pivot

L'investigation repose sur le pivot : passer d'un sélecteur à un autre. Nom → email → comptes en ligne → username → autres plateformes → photo → reconnaissance faciale → autres identités. À chaque pivot : documenter (sélecteur, source, date, confiance), mettre à jour le graphe, et vérifier la cohérence (même personne ou homonyme ?).

### 6.2 Recherche par nom et registres publics

Combiner le nom avec des qualificateurs pour éliminer les homonymes. Moteurs de recherche de personnes par pays (exemples à date : France — 118712.fr, PagesJaunes ; US — ThatsThem, FastPeopleSearch — VPN US requis depuis l'Europe ; international — Lampyre). Les registres publics de haute fiabilité (A1) : cadastre.gouv.fr, publicité foncière, SCI via Pappers/Infogreffe, BODACC, JO associations, Légifrance jurisprudence.

**Faux positifs fréquents :** les homonymes sont le piège n°1 — deux personnes portent le même nom et l'investigateur attribue à sa cible des informations d'un tiers. Parade : toujours croiser avec 2+ sélecteurs indépendants (même ville ET même âge ET même employeur). Si la confirmation est impossible, l'attribution est « incertaine » et signalée comme telle dans le rapport.

### 6.3 Recherche d'emails

Découverte : Hunter.io (emails par domaine + pattern), Phonebook.cz (emails dans les fuites), email permutator. Le pivot le plus puissant : **Holehe** et **Epieos** (vérifient sur quels services un email est enregistré sans alerter la cible). Si l'email est enregistré sur un exchange crypto = signal majeur dans une investigation financière.

**Limites :** ces outils open source se font régulièrement bloquer par les plateformes (rate limiting, changements d'API). Leur maintenance dépend de contributeurs bénévoles. Un résultat négatif (« email non trouvé ») ne signifie PAS que le compte n'existe pas — cela peut signifier que la détection a échoué. Compléter par des vérifications manuelles et des solutions commerciales maintenues.

### 6.4 Recherche de numéros de téléphone

TrueCaller, Sync.me, annuaires inversés nationaux. Pivot vers les messageries : le numéro dans les contacts du téléphone d'investigation révèle WhatsApp (nom, photo, statut) et Telegram (username). Le dump Facebook 2021 (533M profils) relie des numéros à des profils.

### 6.5 Recherche par username

**Sherlock** (300+ plateformes), **Maigret** (2500+, extraction de données), **WhatsMyName** (moins de faux positifs). Corrélation entre comptes : même avatar, même bio, même style, même fuseau horaire. **Piège :** les usernames recyclés — un username populaire peut avoir été utilisé par différentes personnes. La vérification de cohérence temporelle et stylistique est indispensable.

### 6.6 Reconnaissance faciale

PimEyes, FaceCheck.id, Search4Faces (VK/OK), Yandex Images. La reconnaissance faciale **suggère, ne prouve jamais**. Le taux de faux positifs est significatif, le taux de faux négatifs aussi (angle différent, lunettes, coupe de cheveux). Chaque correspondance doit être validée par corroboration indépendante. **Risque juridique :** le RGPD classe les données biométriques comme sensibles — l'utilisation de la reconnaissance faciale par un privé est soumise à des précautions renforcées.

> **🎯 MIRAGE — Épisode 3 :** Holehe → comptes Binance, Coinbase, Instagram, Booking, Airbnb. Username Instagram marc_del75. Maigret → même username sur GitHub, forum voitures de luxe, poker en ligne. PimEyes → correspondance site de rencontres « Marco D., 48 ans, Paris ». Pappers → SCI Delaunay Patrimoine (bien 1,2 M€). Graphe : 5 emails, 8 comptes, 2 sociétés françaises, 1 bien immobilier.

---


## Chapitre 7 — SOCMINT : investigation sur les réseaux sociaux

Méthodologie en 5 étapes par plateforme : identification → extraction → analyse de contenu → analyse de réseau → préservation. Règle n°1 : **capturer avant disparition**.

**Facebook** : Google dorks site:facebook.com, extraction d'ID utilisateur, analyse amis/likes/groupes/événements, check-ins. Les restrictions croissantes (Graph Search supprimée, profils fermés par défaut) → dorks et outils tiers restent efficaces. **Instagram** : profils publics via web app, stories (capturer immédiatement), hashtags/localisation/tagged people, followers/following. **LinkedIn** : observation passive UNIQUEMENT (LinkedIn notifie les visites) → recherche via Google dorks site:linkedin.com. Les recommandations révèlent les relations professionnelles réelles. **Twitter/X** : recherche avancée (from: since: until: filter: geocode:), analyse de timeline. Adaptation 2025 : X quasi inaccessible sans API payante → instances Nitter (en déclin), archivage anticipé. **TikTok** : username/hashtag, localisation dans les vidéos. **Reddit** : historique complet (API, Redective), subreddits fréquentés.

**Faux positifs fréquents :** les comptes inactifs ou abandonnés (un profil Facebook datant de 2012 avec 0 activité récente peut être un ancien compte abandonné, pas le profil actif de la cible). Les comptes parodiques ou fan accounts (même nom, même photo, mais pas la même personne). Les informations auto-déclarées (un profil LinkedIn qui déclare un poste n'est pas une preuve que la personne occupe réellement ce poste — vérifier par d'autres sources). **Limite fondamentale :** les réseaux sociaux montrent ce que les gens veulent montrer — l'absence d'information sur un réseau social ne signifie pas l'absence de l'activité.

---


## Chapitre 8 — Telegram : investigation en profondeur

*Telegram est devenu LA plateforme d'investigation en 2025 — criminalité, extrémisme, marchés clandestins, fuites de données.*

Les **canaux et groupes** : canaux publics (indexés, cherchables), groupes (jusqu'à 200 000 membres). La recherche : recherche interne, Google dorks site:t.me, **TGStat** (statistiques et recherche de canaux), **Telepathy** (outil OSINT Telegram — collecte de messages, membres, métadonnées). L'investigation des **administrateurs** (numéro de téléphone parfois visible, bots associés, canaux croisés — un admin gère souvent plusieurs canaux). L'investigation des **membres** (dans les groupes publics : noms, usernames, parfois numéros). Les **bots** comme source (@getcontact_bot, @SangMata_bot — historique des changements de nom). Le **forwarding** (un message forwardé porte le nom du canal d'origine → révèle le réseau de canaux liés). Les canaux clandestins (vente de données, carding, accès — migration massive de Tor vers Telegram).

**Limites :** les bots d'investigation Telegram sont instables (bloqués, modifiés, ou supprimés régulièrement). Les numéros de téléphone des admins ne sont visibles que si la confidentialité n'est pas configurée correctement — de plus en plus d'admins masquent leur numéro. Les groupes privés nécessitent une invitation — l'investigateur privé ne peut pas y accéder sans compromettre son OPSEC. **Risque juridique :** rejoindre un groupe clandestin pour observer = zone grise ; interagir (poster, acheter) = potentiellement illégal pour un privé.

> **🎯 MIRAGE — Épisode 4 :** Delaunay admin du groupe Telegram « Offshore Trading Club » (560 membres) sous marc_offshore. Le numéro de l'admin = numéro du dump Facebook. Canal lié par forwarding : « Crypto Tax Free ». Graphe enrichi de 2 canaux, 560 contacts potentiels, liens vers des prestataires offshore.

---
