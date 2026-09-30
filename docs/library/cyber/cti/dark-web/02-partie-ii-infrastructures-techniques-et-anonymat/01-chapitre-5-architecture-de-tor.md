---
title: Chapitre 5 — Architecture de Tor
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie II — Infrastructures techniques et anonymat
  - index.md
---

Tor (The Onion Router) est le darknet dominant. Comprendre son architecture permet de comprendre ses propriétés, ses limites, et les angles d'attaque — défensifs ou offensifs — qui s'appliquent.

## 5.1 Principe de l'onion routing

L'idée centrale de l'onion routing est **séparer la connaissance de l'origine et de la destination** entre plusieurs nœuds intermédiaires, de telle sorte qu'**aucun nœud seul** ne connaisse les deux extrémités de la communication.

Mécanisme : le client Tor construit un **circuit** à trois nœuds (guard, middle, exit) en négociant des clés de chiffrement successives. Chaque paquet envoyé est **chiffré trois fois**, dans des couches successives. Chaque nœud intermédiaire déchiffre **une couche** pour révéler le saut suivant, sans pouvoir déchiffrer les autres couches.

Concrètement, pour une requête du client Alice vers le site `example.com` :

1. Le client Tor d'Alice choisit trois nœuds : un **guard** (premier relais, connu du client), un **middle** (relais intermédiaire), un **exit** (relais de sortie qui parle au site final).
2. Alice chiffre sa requête en trois couches, dans l'ordre inverse du chemin : couche exit, couche middle, couche guard — chaque couche chiffrée avec la clé du nœud correspondant.
3. Le paquet transite : Alice → guard. Le guard déchiffre sa couche, voit l'adresse du middle mais pas la destination finale.
4. Guard → middle. Le middle déchiffre sa couche, voit l'adresse de l'exit mais ne connaît ni Alice (qui a parlé au guard) ni la destination finale.
5. Middle → exit. L'exit déchiffre sa couche, voit la requête en clair (si HTTP) et l'envoie vers example.com. L'exit connaît la destination mais ne connaît pas Alice.

Réponse : même mécanisme en sens inverse. Chaque nœud ne chiffre qu'une couche avec sa clé sur le retour.

**Propriété clé** : dans ce modèle, aucun nœud seul ne connaît à la fois l'identité de l'origine (Alice) et la destination (example.com). Un adversaire doit contrôler **à la fois le guard et l'exit** pour corréler. C'est toute la sécurité du système — et son talon d'Achille.

## 5.2 Les types de relais

Le réseau Tor comprend environ **7 000 à 8 000 relais** actifs en 2025-2026, répartis géographiquement (concentration en Europe, US, Canada, quelques en Asie). Ils se classent en catégories.

**Guard relays** : premier nœud d'un circuit, choisi parmi un ensemble de relais stables et bien connectés. Un client Tor utilise le **même petit ensemble de guards** pendant plusieurs mois (rotation lente), pour limiter l'exposition à un attaquant qui compromettrait des guards aléatoirement (l'attaquant a plus de chances de tomber sur un mauvais guard avec rotation rapide).

**Middle relays** : relais intermédiaires, les plus nombreux. Rôle de relais pur, sans visibilité ni sur l'origine ni sur la destination.

**Exit relays** : relais qui parlent au monde extérieur. Les moins nombreux (risque juridique élevé — un abus commis via Tor sort par l'exit, dont l'opérateur peut recevoir des plaintes ou des requêtes légales). Environ 1 000 exits actifs. Certains exits ont des politiques restrictives (bloquent certains ports, certains protocoles).

**Directory authorities** : serveurs qui maintiennent la liste des relais (le « consensus »). Il y a **9 directory authorities** actuellement, opérées par des entités de confiance (universités, Tor Project, individus de long terme). Tous les clients Tor téléchargent périodiquement ce consensus pour choisir leurs circuits.

**Bridges** : relais **non publics** (absents du consensus public), accessibles uniquement à ceux qui en obtiennent l'adresse par des canaux spécifiques (site web du Tor Project, email, Telegram, Messenger). Usage : contourner la censure là où les relais publics sont bloqués.

**Pluggable transports** : techniques d'obfuscation du trafic Tor pour contourner le Deep Packet Inspection. **obfs4** (fait ressembler Tor à du trafic aléatoire), **meek** (fait ressembler Tor à du trafic vers un grand service cloud type Azure, AWS, Fastly — « domain fronting »), **snowflake** (utilise des volontaires côté client comme relais WebRTC).

## 5.3 Construction d'un circuit — détail

Plus précisément, voici comment un client Tor construit un circuit (simplifié).

1. **Téléchargement du consensus** : le client télécharge la liste des relais et leurs clés publiques auprès d'un directory authority ou d'un cache.

2. **Sélection des relais** : le client choisit un guard (parmi ses guards persistants), un middle, un exit — selon des critères de stabilité, bande passante, géographie (pour éviter par exemple de choisir trois relais dans le même pays), et politiques d'exit.

3. **Handshake avec le guard** : le client établit une connexion TLS avec le guard et négocie une clé symétrique via un protocole d'échange de clés (actuellement NTor — Noise-based Tor handshake).

4. **Extension vers le middle** : le client envoie au guard une commande « extend » chiffrée, qui demande au guard de contacter le middle et de négocier une clé symétrique avec lui. Le client obtient ainsi une clé partagée avec le middle via le guard comme relais.

5. **Extension vers l'exit** : pareil, le client étend le circuit vers l'exit.

Le client dispose maintenant de trois clés symétriques, une avec chaque relais. Toute donnée envoyée sera chiffrée en trois couches.

6. **Envoi de données** : le client construit son paquet en trois couches chiffrées et l'envoie au guard. Le guard déchiffre sa couche, fait suivre au middle, etc.

La durée de vie d'un circuit est typiquement de **10 minutes**, après quoi un nouveau circuit est construit pour les nouvelles connexions. Les streams existants peuvent continuer sur l'ancien circuit.

## 5.4 Attaques et limites

Tor fournit un anonymat **fort mais pas absolu**. Plusieurs classes d'attaques existent.

**Attaque par corrélation de trafic**. Si un adversaire contrôle (ou observe) à la fois le guard et l'exit d'un circuit, il peut corréler les flux entrants et sortants par leur timing et leur volume, et identifier l'origine et la destination. Cette attaque nécessite une observation globale ou la compromission massive de relais. Les grands services de renseignement (NSA, GCHQ) sont crédités de cette capacité dans certaines conditions.

**Attaques sur les bridges**. Les censeurs ciblent les bridges en enregistrant leur trafic ou en les bloquant par DPI. La course entre obfuscations (nouveaux pluggable transports) et détection est continue.

**Attaques sur le navigateur**. Les utilisateurs de Tor Browser sont parfois attaqués via des exploits navigateur (historiques : **NIT du FBI en 2015 contre Playpen**, plusieurs opérations documentées contre Freedom Hosting). Ces attaques exploitent des vulnérabilités du navigateur sous-jacent (Firefox modifié) pour faire exécuter du code chez l'utilisateur et révéler son IP réelle hors de Tor. Voir Ch.30.

**Attaques par fingerprinting**. Même si l'IP est masquée, l'ensemble du comportement d'un utilisateur (timing, patterns de clics, taille de fenêtre, fingerprint navigateur) peut contribuer à son identification. Tor Browser est conçu pour uniformiser autant que possible les fingerprints (même résolution, même user-agent, anti-canvas), mais la recherche académique montre que l'anonymat parfait est illusoire.

**Attaques sur le DNS**. Si une application autre que Tor Browser fait des requêtes DNS non-tunnelées, elle leak l'IP réelle. C'est pourquoi Tor Browser isole le DNS dans le circuit.

**Erreurs utilisateur**. Loggin avec un compte identifié, réutilisation de pseudonymes, corrélation temporelle par les actions — beaucoup de dé-anonymisations historiques viennent d'erreurs d'OPSEC plus que d'attaques cryptographiques (Ulbricht, Cazes, beaucoup d'administrateurs de Hansa ou Silk Road 2.0).

## 5.5 Tor Browser et les bonnes pratiques

**Tor Browser** (basé sur Firefox ESR avec modifications majeures) est le client de référence. Il intègre Tor, configure les proxies correctement, active NoScript, définit des paramètres de confidentialité par défaut (pas de cookies tiers persistants, pas de WebRTC, canvas bloqué). Disponible pour Windows, macOS, Linux, Android (Android via Orbot + Firefox-based browser). iOS n'a pas de Tor Browser officiel (limitations App Store) mais Onion Browser est une alternative acceptable.

**Mode Safer / Safest** : Tor Browser offre trois niveaux de sécurité (Standard, Safer, Safest). Safest désactive JavaScript sur tous les sites — recommandé pour l'investigation dark web (beaucoup de sites illicites exploitent des vulnérabilités JS pour identifier les visiteurs, voir Ch.30).

**Tails** : distribution Linux live qui force tout le trafic à passer par Tor, ne laisse aucune trace sur la machine. Usage recommandé pour les analystes travaillant sur des cas sensibles, et pour les journalistes/sources (Edward Snowden l'utilisait). Pas d'amnésie parfaite — une compromission exploitée en live peut leaker des données.

**Whonix** : architecture en deux VM (Whonix-Gateway qui fait le routage Tor, Whonix-Workstation où tournent les applications). L'isolation renforce la sécurité : si la workstation est compromise, elle ne peut pas obtenir l'IP réelle (qui n'est connue que de la gateway).

## 5.6 Fil rouge — DARKSTREAM : préparation technique

> **🌐 DARKSTREAM — Épisode 3 : setup**
>
> Lucas prépare son environnement d'investigation. Protocole Athéna : **machine dédiée**, non reliée au réseau d'entreprise, allumée uniquement pour les sessions d'investigation. OS : Whonix, Gateway + Workstation dans VirtualBox, patchs à jour. Tor Browser en mode **Safest** (JavaScript désactivé par défaut). Outils : navigateur uniquement pour la première phase, pas de screenshot direct de la machine (passage par OCR d'une photo d'écran pour éviter les métadonnées).
>
> Pseudonymes dédiés à l'investigation : jamais de réutilisation d'un pseudo personnel, jamais de référence à Athéna. Lucas prépare trois pseudonymes distincts, un par type de forum à explorer, avec des styles linguistiques légèrement différents. Pas de paiement depuis un compte personnel — budget alloué par Athéna via un wallet crypto dédié à l'investigation, financé depuis un exchange professionnel avec KYC Athéna (pas de KYC Lucas personnel).
>
> Ch.22 détaillera le cadre légal qui encadre cette préparation, Ch.23 l'OPSEC complète.

---
