---
title: Chapitre 1 — Internet, web visible, deep web, dark web
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - 'Partie I — Fondations : COMPRENDRE le DARK WEB'
  - index.md
---

remettre les mots à l'endroit

## 1.1 Internet n'est pas le web

La confusion commence ici. **Internet** est le réseau physique mondial — un ensemble de câbles sous-marins, de fibres optiques, de routeurs, de satellites, et de protocoles (principalement TCP/IP) qui relient des milliards de machines à travers la planète. Internet transporte beaucoup plus que le web : email (SMTP, IMAP), streaming vidéo (RTP, HLS), trafic VPN (IPsec, WireGuard), requêtes DNS, pair-à-pair (BitTorrent), voix sur IP, jeux en ligne, protocoles industriels, trafic de mise à jour automatique.

Le **web** (World Wide Web) est un **service** qui fonctionne sur Internet, basé sur le protocole HTTP/HTTPS et des standards de présentation (HTML, CSS, JavaScript). C'est ce qu'on consulte avec un navigateur. Le web est une couche applicative parmi d'autres — une partie importante d'Internet, certes, mais pas la totalité.

Confondre Internet et web, c'est confondre le réseau routier et les magasins qu'on peut atteindre en voiture. Cette précision est importante parce que **les darknets sont des réseaux overlay** — ils fonctionnent sur Internet, en utilisant son infrastructure physique, mais construisent au-dessus une couche logique séparée avec des propriétés différentes (anonymat, routage alternatif). Comprendre cette distinction empêche de confondre le transport (TCP/IP classique) et la couche logique d'anonymisation.

## 1.2 Les trois couches du web

Dans le langage courant, on distingue trois couches — simplification utile même si les frontières sont poreuses.

**Surface web (clearnet)**. L'ensemble des pages indexées par les moteurs de recherche généralistes (Google, Bing, Yandex, DuckDuckGo, Baidu). En volume, le surface web représente environ 5 à 10% du contenu web total — estimation stable depuis une décennie malgré la croissance du web en valeur absolue. Tout site accessible par une URL classique (`https://example.com`) et dont les pages apparaissent dans les résultats Google fait partie du surface web.

**Deep web**. L'ensemble des contenus web **non indexés** par les moteurs de recherche généralistes. C'est la couche **la plus vaste et la plus banale** : intranets d'entreprise, bases de données académiques, contenu derrière authentification (compte bancaire, messagerie, réseaux sociaux privés, factures de services publics), archives techniques non indexées, pages dynamiques générées à la demande. Le deep web représente environ **90% du contenu web** en volume.

**La quasi-totalité du deep web est parfaitement légale et banale**. Quand on parle du deep web, on ne parle **pas** de cybercriminalité — on parle de tout ce que Google ne voit pas, pour des raisons techniques (robots.txt, authentification requise) ou de design (bases de données consultables uniquement via un formulaire). Votre boîte mail Gmail est du deep web. L'intranet de votre employeur est du deep web. La base de données d'un laboratoire universitaire est du deep web. Cette banalité est structurante — elle rappelle que l'absence d'indexation n'a rien de sinistre.

**Dark web**. Sous-ensemble du deep web accessible **uniquement via des réseaux d'anonymisation spécifiques** — principalement Tor (sites `.onion`), accessoirement I2P (eepsites), Freenet, Lokinet, ZeroNet, et quelques autres darknets plus confidentiels. Le dark web n'est pas simplement « non indexé » — il est **volontairement caché**, hébergé sur des infrastructures d'anonymisation qui masquent à la fois l'identité du serveur (son IP) et du visiteur (son IP). En volume, le dark web est une fraction **minuscule** d'Internet : quelques centaines de milliers de domaines .onion observés par le Tor Project, dont la majorité sont inactifs, abandonnés, dupliqués, ou artefacts de tests.

## 1.3 Darknets vs dark web : une distinction technique utile

Un **darknet** est un réseau **overlay** (superposé à Internet) conçu pour l'anonymat. Tor est un darknet. I2P est un darknet. Freenet est un darknet. Chacun implémente un modèle d'anonymisation différent (onion routing, garlic routing, freenet caching) avec ses propres propriétés.

Le **dark web** est l'ensemble des **contenus accessibles via ces darknets**. La distinction est importante : on peut utiliser le darknet Tor **sans visiter de site .onion** — par exemple, en utilisant Tor uniquement comme proxy pour naviguer de manière anonyme sur le web classique. Et on ne peut visiter un site .onion **qu'en passant par le réseau Tor**.

En pratique, l'analyste manipule les deux termes. « Investiguer sur le dark web » signifie explorer les contenus hébergés sur les darknets. « Utiliser le darknet Tor » signifie exploiter l'infrastructure d'anonymisation, qu'on aille sur un .onion ou sur le clearnet via Tor.

## 1.4 Pourquoi le terme « dark web » est souvent mal utilisé

Les médias utilisent « dark web » comme synonyme de « cybercriminalité » — raccourci compréhensible, mais analytiquement dommageable pour trois raisons.

**Il surestime le dark web comme espace criminel**. Beaucoup d'activité cybercriminelle se déroule sur le **clear web** (forums à accès restreint, marketplaces à ciel ouvert dans certaines juridictions, plateformes de communication grand public). Telegram, Discord, Signal, pastebins publics, forums publics, GitHub — tous hébergent des activités illicites sans être du dark web. Genesis Market et RaidForums, deux plateformes criminelles majeures, opéraient sur le web de surface. Inversement, beaucoup de sites .onion sont parfaitement légaux.

**Il sous-estime les usages légitimes du dark web**. Contournement de censure dans les régimes autoritaires, protection des sources journalistiques, communication sécurisée pour lanceurs d'alerte, recherche en cybersécurité, protection de la vie privée — ce sont des usages essentiels et pleinement légaux. Des institutions parfaitement légitimes (BBC, New York Times, Deutsche Welle, Facebook, ProPublica, Amnesty International) maintiennent des miroirs .onion officiels.

**Il crée une fascination sensationnaliste** qui obscurcit la réalité opérationnelle. Le dark web, en vrai, est souvent **lent** (latence de plusieurs secondes par clic), **fréquemment en panne** (les .onion disparaissent, les marchés tombent, les forums exit-scament), **rempli d'arnaques** (un post sur trois est une tentative de scam), et **plus petit qu'on ne le croit**. Ce n'est pas un bazar secret infini — c'est un espace opérationnel limité, où les vrais acteurs compétents se connaissent, où la confiance est rare et chère, et où le folklore médiatique sur les « services de tueurs à gages » est quasi entièrement fictif (les rares sites qui proposent cela sont des scams).

## 1.5 Ordres de grandeur

Les mesures publiques du Tor Project (metrics.torproject.org) donnent les ordres de grandeur suivants pour 2025-2026. Le nombre d'adresses .onion v3 uniques observées par les relais directory oscille autour de **800 000**, avec une variation quotidienne importante. Parmi ces adresses, seule une fraction est **active** à un instant donné — les estimations convergent sur 10 à 30% de sites répondant aux requêtes. Parmi les sites actifs, environ 50 à 60% sont des **usages légitimes, miroirs, ou services abandonnés**, 20 à 30% sont des **arnaques** (fausses marketplaces, faux services), et 10 à 20% hébergent du **contenu illicite réel** (forums criminels, marchés actifs, leak sites ransomware, CSAM — qui fait l'objet d'une lutte prioritaire des forces de l'ordre).

Côté usage : le Tor Project rapporte environ **2 à 3 millions d'utilisateurs quotidiens** du réseau Tor. Le Congressional Research Service estimait en 2015 qu'environ **3,4% seulement** des utilisateurs Tor visitaient des hidden services — la **grande majorité** utilise Tor pour naviguer sur le web classique de manière anonyme (résistance à la surveillance, contournement de censure).

Ces chiffres importent : le dark web est un espace **modeste** comparé au web classique. Une investigation dark web n'est pas une exploration d'un océan infini — c'est un travail ciblé dans un écosystème connaissable, dont on peut cartographier les principaux acteurs en quelques semaines de travail méthodique.

## 1.6 Fil rouge — DARKSTREAM : le point de départ

> **🌐 DARKSTREAM — Épisode 1 : le mandat**
>
> Lucas reçoit le brief de Vectris Aerospace le lundi matin. Réunion de cadrage en visio avec le RSSI de Vectris, la DGSI (deux interlocuteurs), et le directeur d'Athéna Group. Le RSSI présente les faits : exfiltration détectée il y a 11 jours, investigation IR en cours avec un prestataire PRIS (Mandiant), signal faible sur le dark web via Recorded Future.
>
> La DGSI précise le cadre : coopération ouverte avec Athéna, remontée bi-hebdomadaire des observations, **ne pas engager de contact direct avec le vendeur** sans concertation préalable, respect strict du périmètre légal de la collecte.
>
> Le mandat d'Athéna est clair : **confirmer ou infirmer** la circulation des données sur le dark web, **authentifier** les données si elles circulent, **cartographier** l'écosystème du vendeur et des acheteurs potentiels, **produire** un rapport actionnable pour la cellule de crise Vectris et la DGSI.
>
> Lucas commence par la première question : les alertes de monitoring dark web sont souvent des **faux positifs**. Avant de déclencher une investigation approfondie, il doit vérifier que la mention « Vectris » sur IndustrialLeaks est réelle, pertinente, et pas un artefact d'homonymie ou un scam opportuniste. Le Ch.2 contextualise le forum cible dans l'histoire des darknet markets ; le Ch.24 détaillera la méthode d'accès.

---
