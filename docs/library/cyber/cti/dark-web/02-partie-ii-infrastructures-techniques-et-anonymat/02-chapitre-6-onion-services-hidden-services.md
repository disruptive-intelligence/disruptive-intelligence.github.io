---
title: Chapitre 6 — Onion services (hidden services)
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie II — Infrastructures techniques et anonymat
  - index.md
---

Les sites `.onion` sont l'une des fonctionnalités les plus emblématiques de Tor. Ils permettent à un serveur d'être **anonyme lui-même** — pas seulement ses visiteurs. Le serveur n'expose pas son IP, et les visiteurs qui s'y connectent ne connaissent pas non plus son IP.

## 6.1 Principe des hidden services

Un hidden service (aussi appelé **onion service**) est un service accessible uniquement via Tor, identifié par une adresse se terminant en `.onion`. L'adresse elle-même est dérivée cryptographiquement de la **clé publique** du service — elle n'est **pas résolue par DNS**.

**Architecture** :

- Le serveur hidden service choisit plusieurs relais Tor comme **introduction points** et leur annonce qu'il est disponible via eux.
- Le serveur publie cette information dans la **hidden service directory** (une table de hachage distribuée sur les relais).
- Quand un client veut se connecter, il recherche dans la directory l'adresse `.onion` du service, trouve ses introduction points, et négocie avec eux.
- Un **rendezvous point** (relais tiers) est établi où client et serveur se rencontrent.
- Les deux parties communiquent via ce rendezvous, chacune masquée par son propre circuit Tor.

Cette architecture implique **six hops** (trois côté client + trois côté serveur) pour la communication — ce qui explique la lenteur relative des sites .onion.

## 6.2 Onion v3 : les adresses modernes

Les adresses .onion historiques (« v2 ») étaient des hashs tronqués de 16 caractères, par exemple `3g2upl4pq6kufc4m.onion`. Cette génération a été **dépréciée** en octobre 2021 pour cause de vulnérabilités cryptographiques.

Les **onion v3** (actives depuis 2017, seules supportées depuis 2021) sont des adresses de **56 caractères**, dérivées d'une clé Ed25519 (256 bits) plus quelques éléments. Exemple : `duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion` (DuckDuckGo).

Les propriétés des v3 :

- Sécurité cryptographique forte (résistant aux attaques actuellement connues).
- Authentification mutuelle par défaut.
- Possibilité de **onion services authentifiés** — seuls les clients connaissant une clé préalable peuvent se connecter.
- Meilleure résistance au « directory scraping » — il est plus difficile d'énumérer les .onion actifs qu'avec v2.

## 6.3 Propriétés de sécurité

Un hidden service bien configuré offre plusieurs propriétés.

**Anonymat du serveur** : l'IP réelle du serveur n'est pas exposée aux clients. Même un attaquant qui compromet un client ne peut pas remonter à l'IP du serveur via des moyens cryptographiques simples.

**Authentification du serveur** : l'adresse `.onion` **est** la clé publique du service. Un man-in-the-middle est quasi impossible — si vous vous connectez à `xxxxxxx.onion`, vous êtes cryptographiquement certain de parler à celui qui détient la clé privée correspondante.

**Pas de dépendance aux autorités de certification** : contrairement à HTTPS qui dépend d'une PKI centralisée (autorités de certification), les hidden services n'ont pas ce point de centralisation.

**Résistance aux saisies** : l'infrastructure est globalement distribuée. Pour saisir un service, les autorités doivent identifier et saisir le serveur physique — ce qui nécessite de dé-anonymiser l'opérateur.

**Cependant, ces propriétés ne garantissent pas que le service soit inviolable**. L'histoire des saisies montre que la chaîne faible est souvent :

- L'**OPSEC de l'opérateur** (Ulbricht, Cazes identifiés par leurs erreurs personnelles).
- Les **vulnérabilités applicatives** du service (SQL injection, RCE) qui exposent l'IP via des misconfigurations.
- Les **leaks d'infrastructure** (serveurs DNS publics mal configurés, headers HTTP, fuites via iframes).
- L'**infiltration** (opérations de police sur des années, compromission des clés).

## 6.4 Les services légitimes en .onion

Beaucoup d'organisations légitimes maintiennent des miroirs .onion pour servir les utilisateurs dans des contextes sensibles (censure, surveillance) ou simplement comme service additionnel.

- **DuckDuckGo** : `duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion`
- **BBC News** : miroir Tor pour servir les pays où la BBC est censurée.
- **New York Times** : miroir pour la protection des sources.
- **ProPublica** : miroir, un des premiers grands médias à en avoir créé un.
- **Facebook** : miroir .onion depuis 2014, notamment pour les utilisateurs en Chine et en Iran.
- **Protonmail** : miroir .onion pour l'accès à la messagerie chiffrée.
- **SecureDrop** : chaque déploiement SecureDrop est un onion service (NYT, Guardian, etc.).
- **Tor Project** lui-même : tous les services (site web, documentation, téléchargements) ont des miroirs .onion.
- **Amnesty International, Reporters Sans Frontières** : miroirs pour les régions sensibles.
- **Ahmia, Torch, Haystak** : moteurs de recherche .onion (indexation limitée de ressources publiques).

Ces miroirs légitimes constituent une part significative des sites actifs — contre-exemple direct au cliché « tout ce qui est .onion est criminel ».

## 6.5 Les limites pratiques pour les opérateurs

Exploiter un hidden service n'est pas trivial. Plusieurs difficultés.

**Latence élevée** : six hops + chiffrement multiple = latence typique de 500 ms à plusieurs secondes par requête. Un site .onion interactif (forum, marché) est intrinsèquement lent. Les utilisateurs habitués au web clearnet le ressentent.

**DDoS**. Les hidden services sont notoirement vulnérables aux DDoS. Un attaquant peut saturer le service en générant du trafic via Tor (qui le masque) — la cible ne peut pas bloquer l'origine puisqu'elle ne la connaît pas. De nombreux grands forums ont été indisponibles des jours ou semaines suite à des DDoS concurrents. Des techniques de protection existent (proof-of-work, rate-limiting intelligent, Vanguards/onion-balance) mais restent imparfaites.

**Maintenance**. Maintenir un service .onion stable dans la durée est techniquement exigeant. Patching, monitoring, gestion des attaques, renouvellement d'infrastructure — beaucoup de services échouent par épuisement opérationnel des admins plus que par saisie.

**Référencement**. Les .onion ne sont pas indexés par Google. La découverte se fait par liste communautaires (Hidden Wiki historique, The Onion Link List), word-of-mouth, posts sur forums clearnet, moteurs de recherche .onion eux-mêmes (Ahmia, Haystak — indexation partielle).

## 6.6 Vanity addresses et reconnaissance

Les adresses .onion sont dérivées cryptographiquement, mais il est possible de générer des **vanity addresses** (adresses contenant un préfixe choisi) en brute-forçant des clés jusqu'à trouver une qui donne le préfixe voulu.

Exemples historiques :

- `facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion` commence par `facebook`.
- `propub3r6espa33w.onion` (ProPublica v2 historique) commençait par `propub`.

Pour un préfixe court (4-6 caractères), c'est trivial ; pour un préfixe de 10+ caractères, cela demande des ressources GPU significatives. Générer `facebookwkhpilnemxj7` a mobilisé des ressources Facebook pour en faire une démonstration.

Cette pratique permet aux services légitimes de signaler leur authenticité par un préfixe reconnaissable, mais aussi aux scammers de créer des adresses qui ressemblent aux vrais services (typosquatting .onion — un faux AlphaBay avec un préfixe similaire à l'original).

L'investigateur vérifie toujours l'adresse complète avant de conclure à l'authenticité d'un service.

---
