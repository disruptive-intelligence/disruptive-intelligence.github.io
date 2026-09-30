---
title: PARTIE II — INFRASTRUCTURES TECHNIQUES ET ANONYMAT
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
chapter: 3
chapters: 10
---

> **Ce que cette partie apprend.** Comprendre les infrastructures techniques qui rendent le dark web possible — architecture Tor, onion services v3, réseaux alternatifs (I2P, Freenet), cryptomonnaies et leur traçabilité, hébergement bulletproof. Comprendre aussi leurs limites — Tor n'est pas magique, Monero n'est pas absolu, un bulletproof host peut être saisi.
>
> **Ce qu'elle ne couvre pas.** Les méthodes d'investigation exploitant ces infrastructures (Partie V et VI), les méthodes concrètes de dé-anonymisation (Ch.29), les techniques de configuration offensive (hors périmètre).
>
> **Ce que vous saurez faire après cette partie.** Expliquer techniquement le fonctionnement de Tor à un collègue, évaluer la résistance d'un service .onion à une saisie, distinguer les propriétés d'anonymat de Bitcoin et Monero, identifier les points de faiblesse typiques d'une infrastructure criminelle.

---

## Chapitre 5 — Architecture de Tor

Tor (The Onion Router) est le darknet dominant. Comprendre son architecture permet de comprendre ses propriétés, ses limites, et les angles d'attaque — défensifs ou offensifs — qui s'appliquent.

### 5.1 Principe de l'onion routing

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

### 5.2 Les types de relais

Le réseau Tor comprend environ **7 000 à 8 000 relais** actifs en 2025-2026, répartis géographiquement (concentration en Europe, US, Canada, quelques en Asie). Ils se classent en catégories.

**Guard relays** : premier nœud d'un circuit, choisi parmi un ensemble de relais stables et bien connectés. Un client Tor utilise le **même petit ensemble de guards** pendant plusieurs mois (rotation lente), pour limiter l'exposition à un attaquant qui compromettrait des guards aléatoirement (l'attaquant a plus de chances de tomber sur un mauvais guard avec rotation rapide).

**Middle relays** : relais intermédiaires, les plus nombreux. Rôle de relais pur, sans visibilité ni sur l'origine ni sur la destination.

**Exit relays** : relais qui parlent au monde extérieur. Les moins nombreux (risque juridique élevé — un abus commis via Tor sort par l'exit, dont l'opérateur peut recevoir des plaintes ou des requêtes légales). Environ 1 000 exits actifs. Certains exits ont des politiques restrictives (bloquent certains ports, certains protocoles).

**Directory authorities** : serveurs qui maintiennent la liste des relais (le « consensus »). Il y a **9 directory authorities** actuellement, opérées par des entités de confiance (universités, Tor Project, individus de long terme). Tous les clients Tor téléchargent périodiquement ce consensus pour choisir leurs circuits.

**Bridges** : relais **non publics** (absents du consensus public), accessibles uniquement à ceux qui en obtiennent l'adresse par des canaux spécifiques (site web du Tor Project, email, Telegram, Messenger). Usage : contourner la censure là où les relais publics sont bloqués.

**Pluggable transports** : techniques d'obfuscation du trafic Tor pour contourner le Deep Packet Inspection. **obfs4** (fait ressembler Tor à du trafic aléatoire), **meek** (fait ressembler Tor à du trafic vers un grand service cloud type Azure, AWS, Fastly — « domain fronting »), **snowflake** (utilise des volontaires côté client comme relais WebRTC).

### 5.3 Construction d'un circuit — détail

Plus précisément, voici comment un client Tor construit un circuit (simplifié).

1. **Téléchargement du consensus** : le client télécharge la liste des relais et leurs clés publiques auprès d'un directory authority ou d'un cache.

2. **Sélection des relais** : le client choisit un guard (parmi ses guards persistants), un middle, un exit — selon des critères de stabilité, bande passante, géographie (pour éviter par exemple de choisir trois relais dans le même pays), et politiques d'exit.

3. **Handshake avec le guard** : le client établit une connexion TLS avec le guard et négocie une clé symétrique via un protocole d'échange de clés (actuellement NTor — Noise-based Tor handshake).

4. **Extension vers le middle** : le client envoie au guard une commande « extend » chiffrée, qui demande au guard de contacter le middle et de négocier une clé symétrique avec lui. Le client obtient ainsi une clé partagée avec le middle via le guard comme relais.

5. **Extension vers l'exit** : pareil, le client étend le circuit vers l'exit.

Le client dispose maintenant de trois clés symétriques, une avec chaque relais. Toute donnée envoyée sera chiffrée en trois couches.

6. **Envoi de données** : le client construit son paquet en trois couches chiffrées et l'envoie au guard. Le guard déchiffre sa couche, fait suivre au middle, etc.

La durée de vie d'un circuit est typiquement de **10 minutes**, après quoi un nouveau circuit est construit pour les nouvelles connexions. Les streams existants peuvent continuer sur l'ancien circuit.

### 5.4 Attaques et limites

Tor fournit un anonymat **fort mais pas absolu**. Plusieurs classes d'attaques existent.

**Attaque par corrélation de trafic**. Si un adversaire contrôle (ou observe) à la fois le guard et l'exit d'un circuit, il peut corréler les flux entrants et sortants par leur timing et leur volume, et identifier l'origine et la destination. Cette attaque nécessite une observation globale ou la compromission massive de relais. Les grands services de renseignement (NSA, GCHQ) sont crédités de cette capacité dans certaines conditions.

**Attaques sur les bridges**. Les censeurs ciblent les bridges en enregistrant leur trafic ou en les bloquant par DPI. La course entre obfuscations (nouveaux pluggable transports) et détection est continue.

**Attaques sur le navigateur**. Les utilisateurs de Tor Browser sont parfois attaqués via des exploits navigateur (historiques : **NIT du FBI en 2015 contre Playpen**, plusieurs opérations documentées contre Freedom Hosting). Ces attaques exploitent des vulnérabilités du navigateur sous-jacent (Firefox modifié) pour faire exécuter du code chez l'utilisateur et révéler son IP réelle hors de Tor. Voir Ch.30.

**Attaques par fingerprinting**. Même si l'IP est masquée, l'ensemble du comportement d'un utilisateur (timing, patterns de clics, taille de fenêtre, fingerprint navigateur) peut contribuer à son identification. Tor Browser est conçu pour uniformiser autant que possible les fingerprints (même résolution, même user-agent, anti-canvas), mais la recherche académique montre que l'anonymat parfait est illusoire.

**Attaques sur le DNS**. Si une application autre que Tor Browser fait des requêtes DNS non-tunnelées, elle leak l'IP réelle. C'est pourquoi Tor Browser isole le DNS dans le circuit.

**Erreurs utilisateur**. Loggin avec un compte identifié, réutilisation de pseudonymes, corrélation temporelle par les actions — beaucoup de dé-anonymisations historiques viennent d'erreurs d'OPSEC plus que d'attaques cryptographiques (Ulbricht, Cazes, beaucoup d'administrateurs de Hansa ou Silk Road 2.0).

### 5.5 Tor Browser et les bonnes pratiques

**Tor Browser** (basé sur Firefox ESR avec modifications majeures) est le client de référence. Il intègre Tor, configure les proxies correctement, active NoScript, définit des paramètres de confidentialité par défaut (pas de cookies tiers persistants, pas de WebRTC, canvas bloqué). Disponible pour Windows, macOS, Linux, Android (Android via Orbot + Firefox-based browser). iOS n'a pas de Tor Browser officiel (limitations App Store) mais Onion Browser est une alternative acceptable.

**Mode Safer / Safest** : Tor Browser offre trois niveaux de sécurité (Standard, Safer, Safest). Safest désactive JavaScript sur tous les sites — recommandé pour l'investigation dark web (beaucoup de sites illicites exploitent des vulnérabilités JS pour identifier les visiteurs, voir Ch.30).

**Tails** : distribution Linux live qui force tout le trafic à passer par Tor, ne laisse aucune trace sur la machine. Usage recommandé pour les analystes travaillant sur des cas sensibles, et pour les journalistes/sources (Edward Snowden l'utilisait). Pas d'amnésie parfaite — une compromission exploitée en live peut leaker des données.

**Whonix** : architecture en deux VM (Whonix-Gateway qui fait le routage Tor, Whonix-Workstation où tournent les applications). L'isolation renforce la sécurité : si la workstation est compromise, elle ne peut pas obtenir l'IP réelle (qui n'est connue que de la gateway).

### 5.6 Fil rouge — DARKSTREAM : préparation technique

> **🌐 DARKSTREAM — Épisode 3 : setup**
>
> Lucas prépare son environnement d'investigation. Protocole Athéna : **machine dédiée**, non reliée au réseau d'entreprise, allumée uniquement pour les sessions d'investigation. OS : Whonix, Gateway + Workstation dans VirtualBox, patchs à jour. Tor Browser en mode **Safest** (JavaScript désactivé par défaut). Outils : navigateur uniquement pour la première phase, pas de screenshot direct de la machine (passage par OCR d'une photo d'écran pour éviter les métadonnées).
>
> Pseudonymes dédiés à l'investigation : jamais de réutilisation d'un pseudo personnel, jamais de référence à Athéna. Lucas prépare trois pseudonymes distincts, un par type de forum à explorer, avec des styles linguistiques légèrement différents. Pas de paiement depuis un compte personnel — budget alloué par Athéna via un wallet crypto dédié à l'investigation, financé depuis un exchange professionnel avec KYC Athéna (pas de KYC Lucas personnel).
>
> Ch.22 détaillera le cadre légal qui encadre cette préparation, Ch.23 l'OPSEC complète.

---

## Chapitre 6 — Onion services (hidden services)

Les sites `.onion` sont l'une des fonctionnalités les plus emblématiques de Tor. Ils permettent à un serveur d'être **anonyme lui-même** — pas seulement ses visiteurs. Le serveur n'expose pas son IP, et les visiteurs qui s'y connectent ne connaissent pas non plus son IP.

### 6.1 Principe des hidden services

Un hidden service (aussi appelé **onion service**) est un service accessible uniquement via Tor, identifié par une adresse se terminant en `.onion`. L'adresse elle-même est dérivée cryptographiquement de la **clé publique** du service — elle n'est **pas résolue par DNS**.

**Architecture** :
- Le serveur hidden service choisit plusieurs relais Tor comme **introduction points** et leur annonce qu'il est disponible via eux.
- Le serveur publie cette information dans la **hidden service directory** (une table de hachage distribuée sur les relais).
- Quand un client veut se connecter, il recherche dans la directory l'adresse `.onion` du service, trouve ses introduction points, et négocie avec eux.
- Un **rendezvous point** (relais tiers) est établi où client et serveur se rencontrent.
- Les deux parties communiquent via ce rendezvous, chacune masquée par son propre circuit Tor.

Cette architecture implique **six hops** (trois côté client + trois côté serveur) pour la communication — ce qui explique la lenteur relative des sites .onion.

### 6.2 Onion v3 : les adresses modernes

Les adresses .onion historiques (« v2 ») étaient des hashs tronqués de 16 caractères, par exemple `3g2upl4pq6kufc4m.onion`. Cette génération a été **dépréciée** en octobre 2021 pour cause de vulnérabilités cryptographiques.

Les **onion v3** (actives depuis 2017, seules supportées depuis 2021) sont des adresses de **56 caractères**, dérivées d'une clé Ed25519 (256 bits) plus quelques éléments. Exemple : `duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion` (DuckDuckGo).

Les propriétés des v3 :
- Sécurité cryptographique forte (résistant aux attaques actuellement connues).
- Authentification mutuelle par défaut.
- Possibilité de **onion services authentifiés** — seuls les clients connaissant une clé préalable peuvent se connecter.
- Meilleure résistance au « directory scraping » — il est plus difficile d'énumérer les .onion actifs qu'avec v2.

### 6.3 Propriétés de sécurité

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

### 6.4 Les services légitimes en .onion

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

### 6.5 Les limites pratiques pour les opérateurs

Exploiter un hidden service n'est pas trivial. Plusieurs difficultés.

**Latence élevée** : six hops + chiffrement multiple = latence typique de 500 ms à plusieurs secondes par requête. Un site .onion interactif (forum, marché) est intrinsèquement lent. Les utilisateurs habitués au web clearnet le ressentent.

**DDoS**. Les hidden services sont notoirement vulnérables aux DDoS. Un attaquant peut saturer le service en générant du trafic via Tor (qui le masque) — la cible ne peut pas bloquer l'origine puisqu'elle ne la connaît pas. De nombreux grands forums ont été indisponibles des jours ou semaines suite à des DDoS concurrents. Des techniques de protection existent (proof-of-work, rate-limiting intelligent, Vanguards/onion-balance) mais restent imparfaites.

**Maintenance**. Maintenir un service .onion stable dans la durée est techniquement exigeant. Patching, monitoring, gestion des attaques, renouvellement d'infrastructure — beaucoup de services échouent par épuisement opérationnel des admins plus que par saisie.

**Référencement**. Les .onion ne sont pas indexés par Google. La découverte se fait par liste communautaires (Hidden Wiki historique, The Onion Link List), word-of-mouth, posts sur forums clearnet, moteurs de recherche .onion eux-mêmes (Ahmia, Haystak — indexation partielle).

### 6.6 Vanity addresses et reconnaissance

Les adresses .onion sont dérivées cryptographiquement, mais il est possible de générer des **vanity addresses** (adresses contenant un préfixe choisi) en brute-forçant des clés jusqu'à trouver une qui donne le préfixe voulu.

Exemples historiques :
- `facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion` commence par `facebook`.
- `propub3r6espa33w.onion` (ProPublica v2 historique) commençait par `propub`.

Pour un préfixe court (4-6 caractères), c'est trivial ; pour un préfixe de 10+ caractères, cela demande des ressources GPU significatives. Générer `facebookwkhpilnemxj7` a mobilisé des ressources Facebook pour en faire une démonstration.

Cette pratique permet aux services légitimes de signaler leur authenticité par un préfixe reconnaissable, mais aussi aux scammers de créer des adresses qui ressemblent aux vrais services (typosquatting .onion — un faux AlphaBay avec un préfixe similaire à l'original).

L'investigateur vérifie toujours l'adresse complète avant de conclure à l'authenticité d'un service.

---

## Chapitre 7 — I2P, Freenet et réseaux alternatifs

Tor n'est pas le seul darknet. Plusieurs réseaux alternatifs coexistent, avec des propriétés différentes. Pour un analyste CTI, leur connaissance est utile : certains acteurs migrent vers ces réseaux quand Tor devient trop surveillé ou quand ils cherchent des propriétés spécifiques.

### 7.1 I2P (Invisible Internet Project)

**I2P** (invisibleinternet.net) est un darknet développé depuis 2003, conçu pour les communications peer-to-peer dans un réseau fermé (contrairement à Tor qui permet aussi de sortir vers l'Internet clearnet).

**Architecture — « garlic routing »** : variation de l'onion routing où plusieurs messages sont **regroupés en ail** (garlic) avant d'être chiffrés. Cette approche offre des propriétés d'obfuscation du trafic différentes.

**Tunnels unidirectionnels** : contrairement à Tor qui utilise des circuits bidirectionnels, I2P utilise des tunnels séparés pour l'entrée et la sortie. Un serveur a ses tunnels entrants, un client a ses tunnels sortants — cette séparation complique l'analyse de trafic.

**Distribution peer-to-peer** : I2P n'a pas de directory authorities centraux (contrairement aux 9 directory authorities Tor). Chaque nœud participe au routage. Cette décentralisation renforce la résilience mais complique le bootstrap.

**Terminologie propre** : les sites sur I2P s'appellent des **eepsites** et utilisent des adresses en `.i2p` (par exemple `stats.i2p`, `i2p-projekt.i2p`).

**Usages**. I2P est moins populaire que Tor — réseau plus petit (quelques dizaines de milliers de nœuds vs millions d'utilisateurs Tor), interface moins accessible, écosystème applicatif restreint. Les forums cybercriminels russophones maintiennent souvent un miroir I2P en plus de leur .onion, par résilience. Certains acteurs préfèrent I2P pour des communications ciblées où Tor est perçu comme trop surveillé (perception plutôt qu'évidence technique).

**Exemple concret** : IndustrialLeaks (le forum fictif de DARKSTREAM) mentionne un miroir I2P. C'est un pattern typique — un forum sérieux maintient deux points d'entrée indépendants pour résilience face aux saisies.

**Attaques et limites**. I2P a été moins étudié académiquement que Tor, et moins attaqué publiquement — mais les propriétés de sécurité sont similaires. La décentralisation peut être un faux confort : un adversaire qui participe en masse au réseau (sybil attack) peut potentiellement compromettre l'anonymat.

### 7.2 Freenet / Hyphanet

**Freenet** (rebaptisé **Hyphanet** en 2023) est l'un des plus anciens darknets, lancé en 2000 par Ian Clarke. Modèle radicalement différent de Tor et I2P : **stockage distribué**.

**Principe** : les utilisateurs contribuent de l'espace disque local au réseau. Les contenus publiés sont **chiffrés et dispersés** sur les machines des utilisateurs, sans qu'aucune ne connaisse l'intégralité d'un contenu. Les contenus populaires sont automatiquement répliqués ; les contenus oubliés s'effacent.

**Propriétés** :
- **Résistance à la censure** : supprimer un contenu de Freenet est très difficile — il faudrait saisir toutes les machines qui en hébergent un fragment.
- **Déni plausible** : un utilisateur hébergeant des fragments chiffrés peut plausiblement ignorer ce qu'il héberge.
- **Usage principal** : publication de contenu (sites statiques, blogs, fichiers) plutôt que communication en temps réel.

**Opennet vs Darknet** : Freenet offre deux modes. **Opennet** : tout nœud peut rejoindre. **Darknet** (« friend-to-friend ») : vous n'êtes connecté qu'à des nœuds opérés par des personnes que vous connaissez — résilience maximale mais effet réseau limité.

**Usages criminels** : Freenet a historiquement été un canal de diffusion de CSAM, raison pour laquelle de nombreuses opérations de police l'ont visé. La capacité à poursuivre un utilisateur sur la seule présence de fragments chiffrés (sans preuve qu'il connaissait le contenu) a été discutée dans plusieurs juridictions.

**Population** : très modeste par rapport à Tor. Usage résiduel, plutôt activiste/libertaire que cybercriminel organisé.

### 7.3 ZeroNet, Lokinet et autres

**ZeroNet** : réseau décentralisé basé sur Bitcoin (identité et signature via clés Bitcoin) et BitTorrent (hosting distribué). Usage modeste, quelques sites politiques, quelques activistes.

**Lokinet** : darknet associé à la cryptomonnaie Loki/Oxen, basé sur une architecture type onion routing mais incentivée par la crypto. Usage limité, écosystème jeune.

**Yggdrasil, cjdns** : réseaux expérimentaux de mesh networking, pas spécifiquement orientés anonymat mais parfois utilisés comme alternatives.

**GNUnet** : projet académique de longue date, très peu déployé en pratique.

**Matrix fédéré** : pas un darknet à proprement parler, mais Matrix (protocole de messagerie fédéré) est parfois utilisé sur Tor pour des communications chiffrées de groupe. Session (basé sur Oxen/Lokinet) est une messagerie qui a émergé.

### 7.4 Pourquoi la multiplicité des darknets ?

Aucun darknet ne domine totalement. Les raisons de la coexistence :
- **Préférences techniques** : Tor pour latence modérée + grande communauté ; I2P pour architectures peer-to-peer ; Freenet pour publication résistante.
- **Segmentation communautaire** : certains acteurs préfèrent se concentrer là où ils sont connus.
- **Redondance** : les opérateurs sérieux maintiennent souvent deux ou trois points d'entrée (onion, i2p, éventuellement Tor v3 authenticated + i2p) pour survivre à une saisie.
- **Évolution défensive** : quand un darknet devient intensément surveillé (perception), une partie de la population migre.

Pour l'investigateur CTI, l'implication pratique : **toujours vérifier si un service cible a un miroir sur un autre darknet**. Un forum saisi sur Tor peut rester opérationnel sur I2P pendant des semaines avant que les autorités l'attrapent aussi. Un acteur privé peut continuer ses activités via I2P après que son .onion est compromis.

---

## Chapitre 8 — Cryptomonnaies et anonymat financier

Les cryptomonnaies sont la couche **financière** du dark web. Sans elles, l'économie clandestine à l'échelle observée serait impossible. Mais les propriétés d'anonymat des cryptomonnaies sont largement mal comprises, y compris par leurs utilisateurs criminels — ce qui explique une part importante des identifications réussies.

### 8.1 Bitcoin : pseudonymat, pas anonymat

Bitcoin (2009, Satoshi Nakamoto) est la cryptomonnaie historique. Propriété fondamentale souvent mécomprise : Bitcoin est **pseudonyme**, pas **anonyme**.

**Principe** : chaque transaction Bitcoin est enregistrée publiquement dans la blockchain. Tout le monde peut voir : quelle adresse a envoyé combien à quelle adresse, à quel moment. Les adresses sont des chaînes de caractères (par exemple `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh`) sans lien apparent avec une identité réelle.

**Mais** : à un moment, une adresse Bitcoin doit être liée à une identité pour être utile — que ce soit via un exchange (qui fait du KYC), une merchant (qui a votre livraison), ou toute interaction qui relie l'adresse à un nom. Une fois ce lien établi, l'historique entier de l'adresse devient attribuable.

Cette propriété a structuré toutes les investigations crypto du dark web : les grandes saisies (Silk Road, AlphaBay, Hydra, multiples ransomware) ont reposé sur le traçage blockchain des flux financiers. **Les cryptocurrency tracing firms** (Chainalysis, TRM Labs, Elliptic, CipherTrace/Mastercard) ont construit un écosystème de renseignement blockchain qui est devenu un outil central de lutte contre la cybercriminalité (Ch.31).

### 8.2 Le traçage Bitcoin en pratique

Plusieurs techniques de traçage sont systématiquement appliquées.

**Clusterisation** : regrouper les adresses qui appartiennent probablement à la même entité, en observant les patterns (adresses qui co-dépensent dans une même transaction sont probablement contrôlées par la même entité).

**Heuristiques de change** : identifier les adresses de change (monnaie rendue) lors d'une transaction pour suivre le portefeuille source.

**Labellisation** : des milliers d'adresses connues sont labellisées (adresses Silk Road historiques, adresses ransomware connues, adresses de grands exchanges type Binance, Coinbase). Les transactions qui touchent ces adresses labellisées donnent des points d'attribution.

**Suivi cross-chain** : les flux passent souvent par plusieurs blockchains (Bitcoin → Ethereum → stablecoin). Les outils modernes suivent ces chaînes.

**Corrélation on-chain / off-chain** : croisement avec données exchanges (requêtes légales pour identifier un compte), surveillance de forums (vendeurs postent parfois leur adresse de paiement), et autres sources.

L'efficacité a été démontrée par une série de cas emblématiques : saisie des fonds Colonial Pipeline (FBI récupère ~2,3 M USD en juin 2021), saisie Bitfinex (DOJ saisit ~3,6 Mrd USD en février 2022), multiples saisies Lazarus, démantèlement Chipmixer (mars 2023), etc.

### 8.3 Monero : anonymat par construction

**Monero (XMR)** (2014, projet open source) est conçu dès l'origine pour l'anonymat. Trois mécanismes cryptographiques :

**Ring signatures** : chaque transaction inclut plusieurs inputs possibles, dont un seul est le vrai. Un observateur ne peut pas distinguer le véritable input. Par défaut, 16 inputs de décoi ("ring size 16" depuis 2022, renforcé par hard fork).

**Stealth addresses** : chaque transaction génère une adresse unique pour le destinataire, dérivée de sa clé publique. Impossible de lier plusieurs transactions reçues par un même destinataire.

**RingCT** (Ring Confidential Transactions) : les montants des transactions sont chiffrés. Un observateur ne voit pas combien a été transféré — seulement qu'une transaction valide a eu lieu.

**Propriétés** : anonymat par défaut, fungibilité (chaque Monero est interchangeable avec tout autre Monero — impossible de « marquer » une pièce comme suspecte). Monero est devenu la cryptomonnaie de choix pour beaucoup d'acteurs cybercriminels depuis 2019-2020.

**Mais pas infaillible**. La recherche académique et les praticiens ont documenté des **faiblesses** :
- Les **decoys** ne sont pas parfaitement aléatoires — des patterns de sélection peuvent être exploités statistiquement.
- Les anciennes transactions (avant 2017 notamment) étaient bien moins protégées et ont pu être analysées rétrospectivement.
- Des **vulnérabilités d'implémentation** ont été corrigées au fil des ans (problèmes de génération d'aléatoire, fuites dans les logs).
- Les flux **on-ramp / off-ramp** (conversion fiat → Monero, Monero → fiat) passent par des exchanges soumis au KYC, donnant des points d'attribution.
- Les **atomic swaps BTC↔XMR** permettent de convertir sans exchange, mais posent des défis logistiques.
- Certaines agences de renseignement (US, multiples) ont annoncé des **contrats** pour développer des capacités de traçage Monero — le statut exact de ces capacités n'est pas public.

L'état consensuel : Monero offre un anonymat **très fort mais pas absolu**. Traçable avec des moyens importants et des conditions particulières ; intraçable dans la pratique courante face à un adversaire standard.

### 8.4 Stablecoins : le nouveau facilitateur

Depuis 2020-2021, les **stablecoins** (USDT Tether principalement, USDC dans une moindre mesure) sont devenus **un vecteur massif de transactions dark web**. Raisons :
- **Stabilité** : pas de volatilité (contrairement à Bitcoin qui peut varier de 20% en une semaine).
- **Liquidité** : facilement convertibles partout.
- **Blockchain TRON** : USDT sur TRON est dominant — frais très faibles (~1 cent par transaction), confirmations rapides (~3 secondes). TRON est devenu la blockchain dominante des flux illicites crypto en volume transactionnel.

**Mais** : les stablecoins ne sont **pas anonymes**. Chaque transaction est on-chain et visible. Les émetteurs (Tether pour USDT, Circle pour USDC) peuvent **geler** les adresses sur requête des autorités — Tether a gelé des centaines de millions de dollars d'adresses suspectes sur les années 2022-2024. USDC est encore plus coopérant avec les autorités américaines.

L'attrait des stablecoins pour le dark web est donc structurellement ambigu : plus facile que Bitcoin pour les transactions, plus surveillé que Monero. Beaucoup d'acteurs utilisent USDT comme monnaie d'échange opérationnelle (prix affichés, paiements rapides) mais convertissent en Monero pour le stockage à long terme.

### 8.5 Les mixers et tumblers

Les **mixers** (ou tumblers) sont des services qui mélangent les fonds de plusieurs utilisateurs pour casser la traçabilité. Vous envoyez 1 BTC, le mixer reçoit aussi les BTC d'autres utilisateurs, et vous renvoie 1 BTC (moins une commission de 1-3%) depuis un pool partagé — théoriquement impossible à relier à votre adresse source.

**Services historiques et statut** :
- **Helix** (saisi en 2020, Larry Harmon condamné à 3 ans de prison).
- **Bitcoin Fog** (saisi en 2021, Roman Sterlingov condamné en 2024).
- **Chipmixer** (saisi en mars 2023 — le DOJ et EPRS estiment ~152 000 BTC blanchis soit ~2,73 Mrd EUR).
- **Tornado Cash** : mixer Ethereum, **sanctionné par l'OFAC en août 2022** — première sanction d'un smart contract dans l'histoire. Des développeurs ont été inculpés, y compris Alexey Pertsev (condamné aux Pays-Bas en mai 2024) et Roman Storm (procès aux US en 2024-2025).
- **Wasabi Wallet, Samourai Wallet** : wallets Bitcoin avec CoinJoin intégré. **Samourai saisi en avril 2024, fondateurs inculpés**. Wasabi continue mais avec restrictions accrues.

**Limites actuelles** : les mixers sont une cible prioritaire des forces de l'ordre et des régulateurs. Leur utilisation est devenue un **signal** — les exchanges KYC refusent souvent de créditer des fonds qui ont transité par un mixer connu. Pour un criminel moderne, utiliser un mixer peut être plus coûteux (frais, délais, déclassement du fund) que de convertir directement en Monero.

### 8.6 L'off-ramp comme talon d'Achille

Le problème fondamental pour le criminel : **à un moment, il faut convertir la crypto en monnaie utilisable** (fiat pour des achats du quotidien, biens physiques, immobilier). Cette étape **off-ramp** est le talon d'Achille.

Plusieurs canaux, tous partiellement compromis :
- **Exchanges KYC** (Binance, Coinbase, Kraken, OKX) : conversion facile mais laisse des traces sous un nom réel. Soumis à GAFI Travel Rule, TRF, etc.
- **Exchanges non-KYC** (historiquement BTC-e, plus récemment quelques plateformes peu réglementées) : de plus en plus rares sous pression internationale.
- **P2P platforms** (LocalBitcoins historique, Paxful, Binance P2P) : permettent des échanges directs avec moins de KYC, mais volumes limités, risque de scam.
- **OTC desks clandestins** : traders informels, souvent basés dans des juridictions peu régulées (Russie, quelques zones d'Asie), commissions élevées (5-20%).
- **Cartes de débit crypto** : convertissent en fiat au point de vente, mais émetteurs majoritaires KYC.
- **Achats directs en crypto** : immobilier, luxe, voitures — dans les juridictions qui l'acceptent.
- **Nested exchanges** : exchanges qui ont un compte sur un exchange majeur et ré-sertent en interne. Plusieurs ont été sanctionnés par OFAC (Suex, Garantex, Bitzlato).

Les investigations crypto identifient souvent le criminel à l'off-ramp — même après plusieurs mixers, une fois que le fund atteint un exchange KYC, l'identité est obtenue par requête légale. Ch.31 détaille le traçage crypto en profondeur.

### 8.7 Fil rouge — DARKSTREAM : préparation financière

> **🌐 DARKSTREAM — Épisode 4 : le wallet d'investigation**
>
> Athéna alloue un budget opérationnel à Lucas pour son investigation DARKSTREAM. **3 000 USDT** sur un wallet dédié, financé depuis un exchange professionnel (KYC Athéna, pas Lucas). Usage prévu : paiement du droit d'entrée IndustrialLeaks (~0,005 BTC si requis), achats éventuels d'échantillons (sous coordination DGSI), pourboires occasionnels pour obtenir des informations de membres coopératifs.
>
> Lucas note que le vendeur aero_source demande **65 000 USDT** pour les 420 Go. Athéna **n'a aucune intention d'acheter** — le cadre mandaté est investigation, pas acquisition. Mais le prix demandé est un signal : 65 000 USDT correspond à un dump « premium », ce qui suggère soit de vraies données de valeur, soit un scammer ambitieux.
>
> Lucas prévoit d'utiliser les capacités de traçage blockchain de ses outils (Chainalysis, TRM Labs via l'abonnement Athéna) pour **surveiller** l'adresse BTC affichée par aero_source dans son post — capter les paiements éventuels et identifier les acheteurs. C'est un angle d'attribution précieux : même sans identifier aero_source, identifier **un** acheteur peut donner un point d'entrée investigatif.

---

## Chapitre 9 — Hébergement, infrastructure et résilience

Les services illicites du dark web ne sont pas hébergés par magie. Un serveur physique existe quelque part, avec un opérateur, une facture d'hébergement, et une exposition juridique — même masqués par Tor. Comprendre les mécanismes d'hébergement permet de comprendre où sont les points de défaillance.

### 9.1 Les choix d'hébergement d'un service .onion

L'opérateur d'un service .onion a plusieurs options.

**Hébergement classique dans un pays « coopératif »** : un VPS chez OVH, Hetzner, Digital Ocean, AWS. Facile, bon marché, mais **totalement exposé à une saisie** si l'opérateur est identifié. La plupart des grandes saisies de marchés dark web ont concerné des infrastructures hébergées dans des clouds classiques — Silk Road chez des hébergeurs américains et islandais, AlphaBay chez des hébergeurs lituaniens, etc.

**Bulletproof hosting** : hébergeurs situés dans des juridictions où la coopération avec les forces de l'ordre est limitée (historiquement Russie, quelques pays d'Europe de l'Est, certaines zones asiatiques), ou hébergeurs qui se spécialisent explicitement dans l'hébergement de contenus « contestés ». Prix 5 à 10 fois plus élevés qu'un hébergement classique, mais résistance accrue. Bulletproof **ne signifie pas invulnérable** — plusieurs grands bulletproof hosts ont été saisis (Atrivo/Intercage 2008, McColo 2008, Russian Business Network, Hostinger/Cyberbunker 2019).

**Auto-hébergement physique** : machine chez soi ou dans un local loué, connexion Internet standard, Tor masquant l'IP. Solution la plus résiliente juridiquement (pas de tiers coopératif à contacter pour les autorités) mais la plus risquée pour l'opérateur (saisie physique de son domicile s'il est identifié, pas de redondance).

**Hébergement distribué** : plusieurs serveurs miroirs dans plusieurs pays, avec load balancing. Augmente la résilience, mais chaque miroir est un point de compromission potentiel.

**Hybrides** : opérateurs sophistiqués combinent plusieurs approches. Un frontend bulletproof pour la face publique, un backend chez un hébergeur différent moins exposé, des backups chiffrés distribués.

### 9.2 Les mécanismes de résilience typiques

Les grands services clandestins mettent en place plusieurs mécanismes pour survivre aux tentatives de saisie.

**Multiple onion addresses**. Un même service peut publier plusieurs adresses .onion (v3 le permet), avec load balancing via onion-balance. Si une adresse est compromise, les autres restent fonctionnelles.

**Rotation d'adresse**. Certains services changent d'adresse .onion périodiquement (tous les X mois) et communiquent la nouvelle aux utilisateurs via des canaux out-of-band (Telegram, XMPP, mailing list chiffrée). Complique le monitoring long terme mais cohérent avec une posture défensive.

**Multiple darknets**. Maintenir simultanément un .onion et un .i2p (ou Lokinet, ou Freenet) — si un darknet devient intenable, l'autre reste. IndustrialLeaks (fictif) illustre ce pattern.

**Infrastructure distribuée**. Frontend, backend, base de données, stockage de fichiers sur des machines séparées, dans des juridictions différentes. Saisir le frontend ne suffit pas ; il faut aussi identifier les autres composants.

**Clés hors ligne**. Les clés privées les plus critiques (signature des annonces, wallet principal) sont conservées hors ligne, sur des machines air-gapped. Une saisie du serveur public ne donne pas accès aux fonds principaux.

**Backups chiffrés**. Les données opérationnelles sont régulièrement sauvegardées chiffrées sur des infrastructures tierces (cloud storage avec chiffrement client-side, stockage distribué type IPFS). Permet de relancer le service même après saisie complète du serveur principal.

**Kill switches**. Certains opérateurs implémentent des kill switches qui effacent automatiquement les données en cas de signes de compromission (pas d'accès admin depuis X heures, tentative de boot sans la bonne clé). Destiné à limiter les preuves collectables lors d'une saisie.

### 9.3 Les points d'attaque des forces de l'ordre

Face à cette résilience, les investigateurs visent les points de faiblesse structurels.

**Identification de l'opérateur**. La méthode la plus efficace historiquement. Une fois l'opérateur identifié, son domicile/bureau peut être perquisitionné, ses infrastructures connues saisies simultanément, et ses clés capturées avant qu'il ne puisse les détruire. Ulbricht capturé ordinateur ouvert, Cazes de même en Thaïlande.

**Vulnérabilités applicatives du service**. Une SQL injection, une RCE, une mauvaise configuration CORS peuvent exposer l'IP réelle du serveur. Les services matures font tester régulièrement leur propre sécurité ; les services amateurs sont souvent identifiables ainsi.

**Fuites d'infrastructure**. Headers HTTP qui révèlent le vrai IP, certificats TLS utilisés à la fois sur clearnet et onion, iframes vers des ressources externes qui font un DNS lookup hors Tor, misconfigurations NTP. Le Tor Project publie régulièrement des recommandations pour éviter ces fuites, mais toutes ne sont pas suivies.

**Analyse de trafic**. Pour un adversaire qui peut observer le trafic entrant/sortant d'un hébergeur suspect, corréler avec les patterns d'activité du service .onion peut permettre d'identifier le serveur. Technique coûteuse, mais documentée dans plusieurs investigations.

**Infiltration**. Opérer le service depuis l'intérieur après saisie (Hansa model) ou infiltrer des comptes admin via social engineering, compromission de machines d'opérateurs, ou pivoting via des services tiers qu'ils utilisent.

**Coopération de l'hébergeur**. Pour les services hébergés chez des clouds mainstream, une simple requête légale suffit à obtenir l'identité du client. C'est pourquoi les opérateurs sérieux n'utilisent pas ces hébergeurs — mais beaucoup d'amateurs le font, et les petits services tombent souvent ainsi.

### 9.4 Le cas emblématique des bulletproof hosts

**Cyberbunker** (originellement Pays-Bas, puis Allemagne) : ancien bunker OTAN reconverti en bulletproof host à partir de 2013. Hébergeait des marchés dark web, des CSAM, des infrastructures criminelles. Saisi en septembre 2019 par la police allemande après une opération de surveillance de trois ans. Le fondateur et plusieurs associés condamnés en 2021. Cas souvent cité comme démonstration que même les bulletproof hosts finissent par tomber.

**Russian Business Network (RBN)** : actif dans les années 2000, St Pétersbourg. Hébergeait malware, phishing, botnets. Jamais saisi stricto sensu, mais progressivement neutralisé par pression sur ses opérateurs de paiement et upstream providers. Dissolution de facto vers 2009.

**Atrivo/Intercage** : US, fermé en 2008 suite à une campagne de denaming par les autres hébergeurs (« de-peering ») qui ont refusé de lui faire du transit.

**McColo** : US, fermé en 2008 de la même manière.

Ces cas illustrent un pattern : les bulletproof hosts finissent par être neutralisés, soit par saisie directe, soit par pression sur leur écosystème (upstream providers, moyens de paiement, banquiers). Durée de vie typique : 5 à 15 ans. Rarement plus.

### 9.5 L'émergence des « underground ISPs »

Ces dernières années, certains acteurs ont tenté de construire des **infrastructures d'ISP entièrement sous contrôle** — leurs propres connexions Internet, leurs propres IPs, leur propre transit. L'idée : ne plus dépendre d'un hébergeur tiers saisissable, mais opérer comme un FAI miniature.

Cas observés avec profils divers : hébergeurs ayant leur propre AS (Autonomous System) BGP dans des juridictions permissives, liaisons satellite pour bypass des FAI nationaux, infrastructure mesh dans des zones sans contrôle étatique effectif. Reste marginal — exige des investissements importants et des compétences techniques avancées.

### 9.6 Fil rouge — DARKSTREAM : l'infrastructure d'IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 5 : analyse d'infrastructure**
>
> Lucas documente ce qu'il peut apprendre de l'infrastructure d'IndustrialLeaks. Depuis le forum lui-même, peu d'indices techniques directs — les opérateurs ont suivi les bonnes pratiques OPSEC.
>
> Mais plusieurs signaux indirects :
> - **Trois changements d'adresse .onion** en 18 mois, toujours annoncés à l'avance sur un canal Telegram public associé au forum. Cohérent avec une posture défensive proactive (pas avec une saisie réussie — pas d'interruption longue observable).
> - **Miroir I2P fonctionnel**, avec la même base de données (posts synchronisés). Indique une architecture centralisée avec deux points d'accès plutôt que deux services indépendants.
> - **Disponibilité élevée** : le forum répond en ~800 ms la plupart du temps, quelques pannes de 2-4 heures observables dans les archives communautaires. Cohérent avec un hébergement sérieux, possiblement bulletproof.
> - **Règles internes publiées** : modération active, bannissements documentés, posts de warning aux scammers. Indique un opérateur impliqué, pas un dump-and-forget.
>
> Hypothèse de travail : IndustrialLeaks est probablement hébergé sur un bulletproof host d'Europe de l'Est, avec une équipe de 2-5 opérateurs (un admin principal, des modérateurs russophones), et une infrastructure miroir I2P active. Son modèle économique : droits d'entrée (250 USD × 3 000 membres = ~750 000 USD si on suppose tous payants — irréaliste, plus réaliste quelques centaines de payants), commissions sur ventes (1-3% probablement), peut-être services premium.
>
> Pour Lucas, les implications d'investigation : accès via vouching (privilégier pour la crédibilité de la persona d'investigation), attentes réalistes de durée de vie (1-3 ans avant rotation ou saisie), priorité à la capture d'indices d'authentification des données **avant** que le forum ne disparaisse.

---
