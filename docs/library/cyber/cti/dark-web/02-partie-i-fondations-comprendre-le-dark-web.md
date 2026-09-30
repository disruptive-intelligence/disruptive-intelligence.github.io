---
title: 'PARTIE I — FONDATIONS : COMPRENDRE LE DARK WEB'
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
chapter: 2
chapters: 10
---

> **Ce que cette partie apprend.** Situer le dark web dans le paysage numérique, comprendre la différence entre surface, deep et dark web, connaître son histoire, saisir pourquoi il existe, et le considérer comme un écosystème plutôt qu'un lieu.
>
> **Ce qu'elle ne couvre pas.** Les détails techniques de Tor (Partie II), les méthodes d'investigation (Partie V), les acteurs et espaces précis (Partie III).
>
> **Ce que vous saurez faire après cette partie.** Répondre correctement à la question « qu'est-ce que le dark web ? », expliquer pourquoi il existe et à qui il sert, et présenter son écosystème à un non-spécialiste sans tomber dans les clichés médiatiques.

---

## Chapitre 1 — Internet, web visible, deep web, dark web : remettre les mots à l'endroit

### 1.1 Internet n'est pas le web

La confusion commence ici. **Internet** est le réseau physique mondial — un ensemble de câbles sous-marins, de fibres optiques, de routeurs, de satellites, et de protocoles (principalement TCP/IP) qui relient des milliards de machines à travers la planète. Internet transporte beaucoup plus que le web : email (SMTP, IMAP), streaming vidéo (RTP, HLS), trafic VPN (IPsec, WireGuard), requêtes DNS, pair-à-pair (BitTorrent), voix sur IP, jeux en ligne, protocoles industriels, trafic de mise à jour automatique.

Le **web** (World Wide Web) est un **service** qui fonctionne sur Internet, basé sur le protocole HTTP/HTTPS et des standards de présentation (HTML, CSS, JavaScript). C'est ce qu'on consulte avec un navigateur. Le web est une couche applicative parmi d'autres — une partie importante d'Internet, certes, mais pas la totalité.

Confondre Internet et web, c'est confondre le réseau routier et les magasins qu'on peut atteindre en voiture. Cette précision est importante parce que **les darknets sont des réseaux overlay** — ils fonctionnent sur Internet, en utilisant son infrastructure physique, mais construisent au-dessus une couche logique séparée avec des propriétés différentes (anonymat, routage alternatif). Comprendre cette distinction empêche de confondre le transport (TCP/IP classique) et la couche logique d'anonymisation.

### 1.2 Les trois couches du web

Dans le langage courant, on distingue trois couches — simplification utile même si les frontières sont poreuses.

**Surface web (clearnet)**. L'ensemble des pages indexées par les moteurs de recherche généralistes (Google, Bing, Yandex, DuckDuckGo, Baidu). En volume, le surface web représente environ 5 à 10% du contenu web total — estimation stable depuis une décennie malgré la croissance du web en valeur absolue. Tout site accessible par une URL classique (`https://example.com`) et dont les pages apparaissent dans les résultats Google fait partie du surface web.

**Deep web**. L'ensemble des contenus web **non indexés** par les moteurs de recherche généralistes. C'est la couche **la plus vaste et la plus banale** : intranets d'entreprise, bases de données académiques, contenu derrière authentification (compte bancaire, messagerie, réseaux sociaux privés, factures de services publics), archives techniques non indexées, pages dynamiques générées à la demande. Le deep web représente environ **90% du contenu web** en volume.

**La quasi-totalité du deep web est parfaitement légale et banale**. Quand on parle du deep web, on ne parle **pas** de cybercriminalité — on parle de tout ce que Google ne voit pas, pour des raisons techniques (robots.txt, authentification requise) ou de design (bases de données consultables uniquement via un formulaire). Votre boîte mail Gmail est du deep web. L'intranet de votre employeur est du deep web. La base de données d'un laboratoire universitaire est du deep web. Cette banalité est structurante — elle rappelle que l'absence d'indexation n'a rien de sinistre.

**Dark web**. Sous-ensemble du deep web accessible **uniquement via des réseaux d'anonymisation spécifiques** — principalement Tor (sites `.onion`), accessoirement I2P (eepsites), Freenet, Lokinet, ZeroNet, et quelques autres darknets plus confidentiels. Le dark web n'est pas simplement « non indexé » — il est **volontairement caché**, hébergé sur des infrastructures d'anonymisation qui masquent à la fois l'identité du serveur (son IP) et du visiteur (son IP). En volume, le dark web est une fraction **minuscule** d'Internet : quelques centaines de milliers de domaines .onion observés par le Tor Project, dont la majorité sont inactifs, abandonnés, dupliqués, ou artefacts de tests.

### 1.3 Darknets vs dark web : une distinction technique utile

Un **darknet** est un réseau **overlay** (superposé à Internet) conçu pour l'anonymat. Tor est un darknet. I2P est un darknet. Freenet est un darknet. Chacun implémente un modèle d'anonymisation différent (onion routing, garlic routing, freenet caching) avec ses propres propriétés.

Le **dark web** est l'ensemble des **contenus accessibles via ces darknets**. La distinction est importante : on peut utiliser le darknet Tor **sans visiter de site .onion** — par exemple, en utilisant Tor uniquement comme proxy pour naviguer de manière anonyme sur le web classique. Et on ne peut visiter un site .onion **qu'en passant par le réseau Tor**.

En pratique, l'analyste manipule les deux termes. « Investiguer sur le dark web » signifie explorer les contenus hébergés sur les darknets. « Utiliser le darknet Tor » signifie exploiter l'infrastructure d'anonymisation, qu'on aille sur un .onion ou sur le clearnet via Tor.

### 1.4 Pourquoi le terme « dark web » est souvent mal utilisé

Les médias utilisent « dark web » comme synonyme de « cybercriminalité » — raccourci compréhensible, mais analytiquement dommageable pour trois raisons.

**Il surestime le dark web comme espace criminel**. Beaucoup d'activité cybercriminelle se déroule sur le **clear web** (forums à accès restreint, marketplaces à ciel ouvert dans certaines juridictions, plateformes de communication grand public). Telegram, Discord, Signal, pastebins publics, forums publics, GitHub — tous hébergent des activités illicites sans être du dark web. Genesis Market et RaidForums, deux plateformes criminelles majeures, opéraient sur le web de surface. Inversement, beaucoup de sites .onion sont parfaitement légaux.

**Il sous-estime les usages légitimes du dark web**. Contournement de censure dans les régimes autoritaires, protection des sources journalistiques, communication sécurisée pour lanceurs d'alerte, recherche en cybersécurité, protection de la vie privée — ce sont des usages essentiels et pleinement légaux. Des institutions parfaitement légitimes (BBC, New York Times, Deutsche Welle, Facebook, ProPublica, Amnesty International) maintiennent des miroirs .onion officiels.

**Il crée une fascination sensationnaliste** qui obscurcit la réalité opérationnelle. Le dark web, en vrai, est souvent **lent** (latence de plusieurs secondes par clic), **fréquemment en panne** (les .onion disparaissent, les marchés tombent, les forums exit-scament), **rempli d'arnaques** (un post sur trois est une tentative de scam), et **plus petit qu'on ne le croit**. Ce n'est pas un bazar secret infini — c'est un espace opérationnel limité, où les vrais acteurs compétents se connaissent, où la confiance est rare et chère, et où le folklore médiatique sur les « services de tueurs à gages » est quasi entièrement fictif (les rares sites qui proposent cela sont des scams).

### 1.5 Ordres de grandeur

Les mesures publiques du Tor Project (metrics.torproject.org) donnent les ordres de grandeur suivants pour 2025-2026. Le nombre d'adresses .onion v3 uniques observées par les relais directory oscille autour de **800 000**, avec une variation quotidienne importante. Parmi ces adresses, seule une fraction est **active** à un instant donné — les estimations convergent sur 10 à 30% de sites répondant aux requêtes. Parmi les sites actifs, environ 50 à 60% sont des **usages légitimes, miroirs, ou services abandonnés**, 20 à 30% sont des **arnaques** (fausses marketplaces, faux services), et 10 à 20% hébergent du **contenu illicite réel** (forums criminels, marchés actifs, leak sites ransomware, CSAM — qui fait l'objet d'une lutte prioritaire des forces de l'ordre).

Côté usage : le Tor Project rapporte environ **2 à 3 millions d'utilisateurs quotidiens** du réseau Tor. Le Congressional Research Service estimait en 2015 qu'environ **3,4% seulement** des utilisateurs Tor visitaient des hidden services — la **grande majorité** utilise Tor pour naviguer sur le web classique de manière anonyme (résistance à la surveillance, contournement de censure).

Ces chiffres importent : le dark web est un espace **modeste** comparé au web classique. Une investigation dark web n'est pas une exploration d'un océan infini — c'est un travail ciblé dans un écosystème connaissable, dont on peut cartographier les principaux acteurs en quelques semaines de travail méthodique.

### 1.6 Fil rouge — DARKSTREAM : le point de départ

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

## Chapitre 2 — Histoire et évolution des darknets

Comprendre le dark web contemporain nécessite de connaître son histoire. Les darknets ont une trajectoire de 25 ans, marquée par des ruptures technologiques, des figures emblématiques, et des grandes opérations de police qui ont reconfiguré l'écosystème à plusieurs reprises.

### 2.1 Les origines : anonymat et recherche militaire (1990s)

L'histoire du dark web commence dans les années 1990 au **Naval Research Laboratory** (NRL) américain, où des chercheurs (notamment **Paul Syverson**, **Michael Reed**, **David Goldschlag**) développent le concept d'**onion routing** : un protocole où les communications sont chiffrées en couches successives, chaque nœud intermédiaire ne pouvant déchiffrer que la couche qui lui est destinée, révélant le saut suivant sans connaître ni l'origine ni la destination finale. L'objectif initial est la **protection des communications de renseignement** — permettre à des agents de communiquer sans que leur trafic puisse être identifié par un adversaire observant le réseau.

Paradoxe fondamental vite identifié : un réseau d'anonymat **ne fonctionne que si beaucoup de gens l'utilisent**. Si seuls les agents de renseignement américains utilisent l'onion routing, tout le trafic observé devient attribuable (« cette communication vient d'un agent américain »). L'anonymat requiert une **foule** — et la foule requiert des usages multiples, y compris civils.

En 2002, **Roger Dingledine** et **Nick Mathewson**, rejoints par Paul Syverson, lancent le **Tor Project** comme implémentation **open source** de l'onion routing. Le projet devient indépendant en 2006 sous la forme d'une organisation à but non lucratif, avec un financement mixte — initialement beaucoup du gouvernement américain (Naval Research Laboratory, Broadcasting Board of Governors, State Department DRL), puis progressivement diversifié (donations individuelles, Mozilla, DARPA, fondations). Cette structure de financement mixte est emblématique du paradoxe : le gouvernement américain finance un outil qui protège aussi les criminels (cible d'investigation FBI), parce qu'il protège surtout les usages légitimes qui justifient stratégiquement l'existence du réseau.

### 2.2 L'ère Silk Road (2011-2013)

**Silk Road**, créé par **Ross Ulbricht** (alias « Dread Pirate Roberts ») en février 2011, est le premier darknet market généraliste significatif. L'idée : un e-commerce clandestin inspiré d'eBay, utilisant Tor pour l'anonymat et Bitcoin pour les paiements. Ulbricht articule une vision libertarienne — vendre n'importe quel produit entre adultes consentants sans intervention étatique.

Silk Road grandit rapidement. Au moment de sa saisie par le FBI en octobre 2013, la plateforme totalise plus de **1,2 million de transactions** avec plus de **150 000 acheteurs** et **4 000 vendeurs**. Dominé par les drogues (~70% des ventes), le catalogue inclut aussi documents contrefaits, services de hacking, armes (controversé, règles internes restrictives sur ce point), mais exclut explicitement CSAM et contrats de tueurs à gages (règles internes interdisant l'« harm against others »).

Ulbricht est arrêté le 1er octobre 2013 dans une bibliothèque publique de San Francisco, ordinateur portable ouvert sur son interface administrateur. Identifié via plusieurs **erreurs OPSEC** cumulatives : un post sur StackOverflow avec son vrai email rthomeumm sous le pseudonyme « frosty », un post sur un forum Bitcoin en avril 2011 sous le pseudonyme « altoid » promouvant Silk Road (alors tout nouveau), un serveur CAPTCHA qui a leaké l'IP du serveur Silk Road lors d'une requête mal configurée (point débattu — les défenseurs d'Ulbricht ont soutenu que cette découverte était une reconstruction *a posteriori* par le FBI, possiblement couvrant une méthode de collecte classifiée).

Ulbricht est condamné en mai 2015 à **double perpétuité sans possibilité de libération conditionnelle plus 40 ans**, peine considérée comme disproportionnée par de nombreux observateurs (aucun meurtre n'ayant été commis — les accusations de tentative de contrat sur des témoins ont été utilisées pendant le sentencing sans inculpation formelle). Grâce présidentielle obtenue en janvier 2025 sous l'administration Trump.

L'héritage Silk Road est ambivalent : démonstration que l'e-commerce clandestin à grande échelle est possible (inspiration pour des dizaines de successeurs), mais aussi démonstration des limites de l'OPSEC individuelle face à une enquête FBI déterminée.

### 2.3 La professionnalisation (2014-2019)

Après Silk Road, les successeurs se professionnalisent. **Silk Road 2.0** est lancé en novembre 2013, saisi un an plus tard (novembre 2014, operation Onymous — opération coordonnée qui saisit aussi plusieurs dizaines d'autres marchés). **Evolution Market** devient leader en 2014-2015 avant un exit scam retentissant (mars 2015, ~12 millions de dollars envolés). **Agora**, **Abraxas**, **Dream Market** se succèdent.

**AlphaBay**, lancé en décembre 2014 par **Alexandre Cazes** (canadien basé en Thaïlande, alias « alpha02 »), devient le **plus grand darknet market de l'histoire**. Au moment de sa saisie, le Département de la Justice américain documente **plus de 250 000 listings de drogues et produits chimiques**, auxquels s'ajoutent **plus de 100 000 listings** pour faux documents, accès frauduleux, malwares, armes et services divers. AlphaBay mature significativement le modèle : multiple cryptomonnaies acceptées (Bitcoin, Monero, Ethereum), 2FA obligatoire, PGP, système d'escrow robuste, ratings élaborés.

**Operation Bayonet** (juillet 2017) est une double frappe coordonnée entre le FBI américain et la police néerlandaise. AlphaBay est saisi suite à une erreur OPSEC de Cazes (inclusion de son email personnel `pimp_alex_91@hotmail.com` dans l'en-tête d'un email de bienvenue automatique généré en 2014). Cazes est arrêté en Thaïlande le 5 juillet 2017. Il est retrouvé mort en cellule le 12 juillet 2017 — officiellement suicide, version contestée par sa famille.

Le coup génial de l'opération : la police néerlandaise avait pris le contrôle de **Hansa Market** quelques semaines avant la saisie d'AlphaBay. Quand AlphaBay tombe, les utilisateurs et vendeurs migrent en masse vers Hansa — qui est maintenant opéré par la police. Pendant **30 jours**, les autorités néerlandaises collectent les données (vraies adresses de livraison, IPs, communications, patterns de transactions) avant de saisir Hansa à son tour. Cette opération devient la référence moderne de l'**infiltration active** par les forces de l'ordre.

### 2.4 Hydra et la domination russophone (2015-2022)

**Hydra Market** (ru-center : hydraruzxpnew4af.onion et successeurs) est un cas à part. Lancé en 2015 et exclusivement opéré en russe, Hydra devient le **leader absolu** de l'écosystème russophone. Le DOJ américain et les autorités allemandes indiquent, lors de la saisie d'avril 2022, qu'Hydra a reçu environ **5,2 milliards de dollars en cryptomonnaies depuis 2015** et représentait environ **80% des transactions crypto liées aux darknet markets en 2021**.

Deux particularités structurantes. **Exclusivement russophone** : barrière d'entrée linguistique qui l'a partiellement protégé des actions law enforcement occidentales et de l'infiltration par analystes étrangers. **Système de dead drops physiques** unique : contrairement aux marchés occidentaux qui utilisent la poste (avec les risques que cela implique), Hydra fonctionnait avec des *kladmen* — courriers qui cachaient physiquement les produits dans des endroits spécifiques (sous une pierre dans un parc, dans un interstice de mur), dont les coordonnées GPS étaient ensuite communiquées à l'acheteur. Modèle qui supprime l'interception postale mais crée un écosystème de travailleurs à bas salaire (les kladmen) avec une rotation élevée.

La saisie d'Hydra en avril 2022 par les autorités allemandes (Zentrale Kriminalinspektion, Bundeskriminalamt, avec soutien du FBI) a créé une **fragmentation** massive de l'écosystème russophone : plusieurs marchés successeurs (OMG!OMG!, Mega, BlackSprut, Kraken) se sont partagé le marché sans qu'un leader clair ne s'impose comme Hydra l'était. La fragmentation complique le monitoring (plus de plateformes à suivre) et augmente la méfiance (exit scams plus fréquents sur les nouveaux marchés).

### 2.5 L'ère post-Hydra et les tendances 2024-2026

L'écosystème 2024-2026 présente plusieurs caractéristiques structurantes.

**Fragmentation des marchés généralistes**. Les marchés « tout-en-un » type AlphaBay cèdent la place à des marchés **spécialisés** : marchés de logs (Russian Market), marchés de fraude (BriansClub, WWH Club, anciens 2easy.gg), marchés de ransomware-as-a-service, marchés de services (CaaS). Cette spécialisation reflète la professionnalisation de la cybercriminalité organisée.

**Montée de Telegram comme concurrent**. Telegram est devenu, dans la période 2020-2024, un canal majeur de communication cybercriminelle. Plus accessible que Tor (pas besoin d'outils spéciaux), plus réactif (chats en temps réel), avec des canaux publics et privés. Les canaux Telegram cybercriminels comptent des centaines de milliers de membres cumulés. **Arrestation de Pavel Durov en France le 24 août 2024** — inculpation incluant complicité dans la diffusion de contenus illicites. Impact : Telegram a considérablement durci sa modération (suppression massive de canaux criminels, coopération accrue avec les autorités), conduisant à une migration **partielle** des acteurs vers d'autres plateformes (Session, Matrix sur Tor, retour partiel vers les forums .onion).

**Glissement du vecteur d'accès initial**. L'évolution majeure 2025-2026 documentée par SOCRadar, Flare, Recorded Future : les attaquants **achètent** des credentials valides sur le dark web via des **stealer logs** à prix dérisoire (dès 15 USD) plutôt que de développer des exploits sophistiqués. Le dark web est devenu le **supermarché de l'accès initial**. L'attaquant moderne n'exploite plus la sophistication technique mais la **commoditisation** : pour 15 USD il achète un log d'infostealer, pour 500-50 000 USD il achète un accès VPN corporate préqualifié auprès d'un IAB, et il n'a plus qu'à monétiser.

**Intégration massive de l'IA**. Deepfakes, génération de phishing, chatbots criminels, analyse assistée — l'IA a basculé d'outil émergent à commodité dans la cybercriminalité. Parallèlement, les défenseurs adoptent l'IA pour le monitoring, l'analyse linguistique, et la détection d'anomalies (Ch.39).

**Pression croissante des forces de l'ordre**. Opérations de démantèlement plus fréquentes et plus sophistiquées (LockBit/Cronos février 2024, Kidflix mars 2025, BreachForums multiple, Qakbot, Hive, ALPHV/BlackCat, Genesis Market). Les grands opérateurs RaaS perdent en moyenne **18 mois** d'existence opérationnelle avant démantèlement. La pression a des effets : le niveau de paranoia opérationnelle augmente, les infrastructures se fragmentent pour résilience, et certains opérateurs se « retirent » après un gain significatif.

### 2.6 Chronologie synthétique des grandes dates

| Période | Événement | Impact structurant |
|---------|-----------|--------------------|
| 1995-2002 | Développement onion routing (NRL) | Foundation technique |
| 2002 | Lancement Tor | Accessibilité publique |
| 2009 | Lancement Bitcoin | Couche financière du dark web |
| 2011 | Lancement Silk Road | Premier grand market généraliste |
| 2013 | Saisie Silk Road, arrestation Ulbricht | Premier shock LE majeur |
| 2014 | Lancement AlphaBay, saisie Silk Road 2.0 | Professionnalisation |
| 2015 | Lancement Hydra (ru) | Émergence bloc russophone |
| 2017 | Operation Bayonet (AlphaBay + Hansa) | Référence infiltration LE |
| 2018-2019 | Dream Market, Wall Street Market | Succession post-AlphaBay |
| 2020-2022 | Ascension Telegram / CaaS | Convergence dark web / clearnet |
| 2022 (avril) | Saisie Hydra | Fragmentation russophone |
| 2023 | Operation Cookie Monster (Genesis) | Saisie marché de logs |
| 2024 (février) | Operation Cronos (LockBit) | Disruption grand RaaS |
| 2024 (août) | Arrestation Pavel Durov | Durcissement Telegram |
| 2025-2026 | Commoditisation accès, montée IA | Paradigme contemporain |

### 2.7 Fil rouge — DARKSTREAM : le forum ciblé

> **🌐 DARKSTREAM — Épisode 2 : IndustrialLeaks dans son contexte**
>
> Avant d'y accéder, Lucas documente le forum signalé. **IndustrialLeaks** est un forum .onion russophone créé fin 2022, dans le contexte post-Hydra. Il s'est positionné sur une niche : les **données industrielles** (pas le ransomware classique, pas les credentials bancaires) — documents techniques, spécifications, bases clients, données de supply chain industrielle.
>
> Environ 3 000 membres enregistrés selon les rares rapports publics disponibles. Accès sur **vouching** (parrainage par un membre établi) ou paiement d'un droit d'entrée (0,005 BTC, ~250 USD au cours actuel). Le forum a changé d'adresse .onion **trois fois** en 18 mois — comportement classique face à la pression (soit d'attaques DDoS concurrentes, soit de tentatives d'infiltration). Un miroir I2P est maintenu, indice de maturité technique des opérateurs. La langue principale est le russe ; l'anglais est toléré mais réservé aux ventes grand format.
>
> L'activité principale documentée : ventes de données d'entreprises industrielles (énergie, défense, aérospatial, chimie), occasionnellement services associés (accès persistant, exfiltration ciblée sur commande). Quelques posts de « dumps » publics pour établir la réputation de vendeurs cherchant à monter en crédibilité.
>
> Pour Lucas, ce contexte suggère qu'**IndustrialLeaks est un forum sérieux plus qu'un bazar à scams** — ce qui augmente la probabilité que la mention Vectris soit réelle. Mais il reste prudent : même dans un forum sérieux, l'opportunisme scam est fréquent. La vérification d'authenticité (Ch.14, Ch.25) reste incontournable.

---

## Chapitre 3 — Pourquoi le dark web existe

Le dark web n'est pas une accumulation fortuite d'infrastructures. Il existe parce qu'il répond à des besoins réels, et il persiste parce que ces besoins persistent. Ce chapitre articule les raisons légitimes, les usages détournés, et la tension fondamentale qui structure le débat public.

### 3.1 L'anonymat comme besoin fondamental

**Résistance à la censure**. Dans les régimes autoritaires (République populaire de Chine, Iran, Russie depuis 2022, Biélorussie, Myanmar, Érythrée, Corée du Nord dans une certaine mesure, Turkménistan), l'accès à des contenus jugés subversifs par l'État est filtré, surveillé, parfois criminalisé. Tor permet, dans beaucoup de ces contextes, d'accéder à Wikipedia, à des médias indépendants (Voice of America, BBC Persian, Deutsche Welle), à des réseaux sociaux bloqués (Twitter/X bloqué en Chine, Facebook en Iran). **Reporters Sans Frontières** opère des miroirs .onion de médias dissidents. Le **Tor Project** développe des techniques dédiées (bridges, pluggable transports comme obfs4, meek, snowflake) pour contourner le Deep Packet Inspection des censeurs.

La mesure n'est pas théorique. Pendant les manifestations en Iran (2022-2023, mouvement Woman Life Freedom), l'usage de Tor a bondi. Après l'invasion russe de l'Ukraine (février 2022) et le durcissement du régime russe vis-à-vis des médias (blocage de Facebook, Twitter, de nombreux médias indépendants), les connexions russes à Tor ont augmenté. Ces périodes de pic confirment que Tor est un **outil opérationnel de résistance informationnelle**.

**Protection des sources journalistiques**. La protection des sources est un pilier de la liberté de la presse, reconnu dans les législations démocratiques (article 10 CEDH, jurisprudence Goodwin c. Royaume-Uni 1996, First Amendment américain, loi française sur la liberté de la presse). Le dark web offre des canaux techniques pour que les sources communiquent avec les journalistes sans risque d'identification.

**SecureDrop** (développée initialement par Aaron Swartz et James Dolan, maintenue par la Freedom of the Press Foundation) est la plateforme de référence. Déployée par : le New York Times, le Guardian, le Washington Post, Le Monde, Der Spiegel, ProPublica, The Intercept, la BBC, et des dizaines d'autres médias. L'affaire **Panama Papers** (2016) et l'affaire **LuxLeaks** (2014) n'auraient pas été techniquement possibles sans des canaux de transmission anonymes.

**AfriLeaks** pour les lanceurs d'alerte africains, **GlobaLeaks** comme plateforme open source généraliste, **Hermes Center** pour le soutien technique à ces déploiements — un écosystème s'est structuré autour de cet usage.

**Vie privée comme droit fondamental**. Article 8 de la CEDH (respect de la vie privée et familiale), article 12 de la Déclaration universelle des droits de l'homme, article 7 de la Charte des droits fondamentaux de l'UE. L'anonymat en ligne est un **instrument** de ces droits. Dans un contexte de surveillance massive (activités commerciales de profilage, surveillance étatique légale ou illégale, collecte par des États hostiles), l'anonymat permet des choix informationnels libres.

**Communications sensibles légitimes**. Défenseurs des droits humains en zones hostiles, avocats consultant des cas sensibles, médecins communiquant sur des patients en zones de conflit, chercheurs en sécurité testant des infrastructures, employés lanceurs d'alerte envers leur propre employeur. L'anonymat technique protège des usages légitimes qui, sans anonymat, seraient impossibles ou dangereux.

### 3.2 L'anonymat comme facilitateur criminel

Le dark web offre aux acteurs malveillants un espace où :
- **L'identification est difficile** : l'IP source est masquée, les pseudonymes sont jetables, les artefacts de compilation et les conventions linguistiques peuvent être contrôlés.
- **Les transactions sont pseudonymes ou anonymes** : Bitcoin pseudonyme avec traçabilité croissante, Monero anonyme par construction.
- **L'infrastructure est résistante aux saisies** : un site .onion ne dépend d'aucun registre centralisé ; la saisie nécessite soit la compromission du serveur physique, soit l'identification de l'opérateur.

Les usages criminels documentés couvrent un spectre large : marchés de drogues (de loin le volume dominant historiquement, en baisse relative depuis 2020), données volées et credentials, armes (volume marginal, beaucoup de scams), documents contrefaits, services de hacking, CSAM (priorité 1 des forces de l'ordre), blanchiment, forums de fraude, infrastructures de communication pour cybercriminels sophistiqués.

La diversité de ces usages, du trafiquant solo au groupe ransomware étatique, montre que le dark web n'est **ni un repaire de super-criminels ni un simple outil de liberté** — l'anonymat est moralement neutre, c'est **l'usage** qui est qualifiable.

### 3.3 La tension fondamentale et ses régulations

La tension n'a pas de résolution simple : **l'anonymat technique qui protège les dissidents protège aussi les criminels**. Supprimer Tor (si c'était techniquement faisable, ce qui est contesté) ne supprimerait pas le besoin d'anonymat des dissidents — il les priverait d'un outil essentiel. Surveiller massivement Tor (comme certaines juridictions autoritaires tentent de le faire) compromet structurellement les usages légitimes.

Les régulations contemporaines tentent de naviguer cette tension par plusieurs approches.

**Lutte ciblée contre les usages criminels spécifiques**. Approche occidentale dominante : ne pas interdire Tor, mais poursuivre les opérateurs de plateformes criminelles (Ulbricht, Cazes, Khoroshev/LockBitSupp), les utilisateurs de CSAM identifiables, les infrastructures de paiement du crime. Les investigations combinent OSINT, analyse blockchain, erreurs OPSEC, infiltration, coopération internationale.

**Régulation des cryptomonnaies**. Parce que l'anonymat financier est le **maillon faible** de la cybercriminalité (à un moment, l'argent doit être converti en fiat utilisable), les régulateurs durcissent les exchanges (KYC renforcé, déclaration de transactions, sanctions ciblées type Tornado Cash en août 2022). Voir Ch.8 et Ch.31.

**Coopération internationale**. Convention de Budapest sur la cybercriminalité (2001), élargie par un deuxième protocole additionnel en 2022 sur la coopération renforcée et la divulgation électronique de preuves. Europol, Interpol, J-CAT, FBI Legal Attaché en poste dans les ambassades. Un écosystème d'échanges de renseignement et de coordination d'opérations.

**Approches contestées dans les démocraties**. Certaines juridictions explorent des pistes qui posent des questions de libertés publiques : lois sur la « responsabilité des plateformes » (Royaume-Uni Online Safety Act, UE Digital Services Act), tentatives de contrer le chiffrement de bout en bout pour permettre l'accès des autorités (projets récurrents type EARN IT aux US, Chat Control en UE — encore débattu), extension des pouvoirs d'interception (projets de mise à jour des législations nationales). Ces approches divisent, parce qu'elles pèsent sur l'équilibre vie privée / sécurité publique.

**Approches criminelles dans les régimes autoritaires**. Blocage pur et simple de Tor (Chine, Iran périodiquement), criminalisation de son usage (Russie depuis 2021 sous certaines formes), surveillance agressive des utilisateurs identifiés. Ces approches s'alignent sur des objectifs de contrôle politique plus que de lutte contre la criminalité.

L'équilibre exact entre anonymat et responsabilité reste un débat politique et sociétal vivant, sans résolution consensuelle à l'horizon.

---

## Chapitre 4 — Le dark web comme écosystème

Le dark web n'est pas une seule chose — c'est un **écosystème** composé d'acteurs aux rôles distincts, d'espaces aux fonctions différentes, et de mécanismes de circulation qui le font fonctionner. Ce chapitre pose le cadre que les parties suivantes approfondiront.

### 4.1 Les types d'espaces

Six grandes catégories d'espaces dark web, détaillées en Partie III.

**Forums** (Ch.10) : espaces de discussion structurés autour de thèmes (fraude, hacking, drogues, données, géographie). Modérés, avec hiérarchie de membres (newbie, member, trusted, VIP, moderator, admin), système de réputation. XSS Forum, Exploit.in, BreachForums successive, IndustrialLeaks (fictif, inspiré de cas réels).

**Marchés (marketplaces)** (Ch.11) : plateformes d'e-commerce clandestin, avec listings, panier, escrow, ratings. AlphaBay historique, Abacus Market, BlackSprut (ru), Mega (ru), TorZon.

**Leak sites** (Ch.12) : vitrines publiques des groupes ransomware, où ils revendiquent les victimes et menacent de publier les données volées. LockBit, ALPHV/BlackCat, Black Basta, RansomHub, Play, Qilin — chacun avec son esthétique propre.

**Messageries et canaux** (Ch.13) : Telegram, Matrix via Tor, Session, Jabber/XMPP, Tox. Les messageries servent à la fois comme canaux opérationnels (négociations, coordination) et comme canaux de diffusion (canaux publics avec abonnés).

**Marchés spécialisés** : marchés de logs (Russian Market), marchés de fraude (Genesis historique, successeurs), marchés 0-day (Ch.17).

**Services** : infrastructure hosting bulletproof, blanchiment-as-a-service, cryptage-as-a-service, bot-as-a-service, phishing kits.

### 4.2 Les types d'acteurs

**Opérateurs de plateformes** : développeurs et administrateurs des forums, marchés, leak sites. Économiquement, ils prélèvent des commissions (1-10% sur les transactions), des frais d'inscription, des frais de vendeur. Politiquement, ils arbitrent les conflits. Opérationnellement, ils gèrent la résilience technique.

**Vendeurs** : acteurs qui monétisent des produits ou services sur les marchés. Spécialisations multiples : drug vendors, carders, credential brokers, fullz vendors, weapon vendors, 0-day brokers, service providers.

**Acheteurs** : clients finaux ou intermédiaires. Profils variés — particuliers cherchant drogues ou documents, cybercriminels achetant des outils, fraudeurs achetant des données, opérateurs ransomware achetant des accès IAB.

**Initial Access Brokers (IAB)** : acteurs spécialisés dans la compromission initiale d'organisations et la vente des accès à d'autres acteurs (typiquement des opérateurs ransomware). Chaîne de valeur centrale de la cybercriminalité contemporaine.

**Affiliés RaaS** : opérateurs qui déploient un ransomware-as-a-service moyennant partage des gains avec le propriétaire du malware.

**Blanchisseurs** : spécialistes de la conversion crypto → fiat utilisable, typiquement 10-30% de commission sur le montant blanchi.

**Services transversaux** : hébergeurs bulletproof, développeurs de malware, opérateurs botnets, crypters, spammers.

**Analystes CTI, forces de l'ordre, journalistes** : observateurs, dans des postures légales variées (voir Partie V sur le cadre légal et Ch.30 sur l'infiltration policière).

### 4.3 Les flux qui font fonctionner l'écosystème

**Flux d'information** : montée en crédibilité des vendeurs, annonces de produits/services, négociations, litiges. Support : forums, canaux dédiés aux marchés, messageries privées.

**Flux financier** : paiements via cryptomonnaies (Bitcoin historique mais en repli, Monero en hausse, quelques stablecoins type USDT), escrow sur les marchés, blanchiment aval. Ch.8 détaille les mécanismes.

**Flux de confiance** : réputation construite par l'historique transactionnel, vouching par membres établis, arbitrage en cas de litige. Sans ces mécanismes, l'économie ne fonctionnerait pas. Ch.19 détaille.

**Flux de données** : données volées circulent des breachers initiaux vers les courtiers, puis vers les acheteurs finaux. Chaîne typique : breach → vente exclusive à prix élevé → revente en baisse → diffusion gratuite tardive (Ch.14).

**Flux d'accès** : les IAB compromettent → vendent l'accès → l'acheteur déploie ransomware ou autre monétisation. Chaîne souvent constatée dans les investigations post-incident.

### 4.4 La géographie linguistique et culturelle

L'écosystème dark web est structuré par **plusieurs blocs linguistiques** largement cloisonnés.

**Bloc russophone** : le plus large historiquement. Forums majeurs (XSS, Exploit.in, RAMP historique), marchés (Hydra historique, successeurs), opérateurs ransomware (LockBit, Conti, ALPHV). La ligne russophone inclut ex-URSS (Russie, Bélarus, Ukraine pré-2022, Kazakhstan, etc.). Règle opérationnelle tacite des groupes russophones : **ne pas cibler la CEI** (Communauté des États indépendants) — règle respectée en grande partie, traduite dans le code de certains ransomware (vérification de la langue du clavier, exclusion des locales russophones).

**Bloc anglophone** : historiquement dominant pour les marchés généralistes (Silk Road, AlphaBay, Dream), devenu plus discret post-grandes saisies. Forums anglophones majeurs (BreachForums multiple, RaidForums historique).

**Bloc chinois** : opère largement sur des plateformes spécifiques, avec forums et canaux accessibles aux sinophones. Moins documenté dans les analyses vendor occidentales, nécessite une expertise linguistique spécialisée.

**Bloc persophone et arabophone** : croissance notable depuis 2020, avec des forums et canaux dédiés, activités orientées fraude, credentials, et parfois opérations liées à des tensions géopolitiques régionales.

**Autres** : francophone (présence modeste, parfois sur forums anglophones), hispanophone (Amérique latine, forums cartels), portugaise (Brésil), turc, coréen.

Pour l'analyste, la **barrière linguistique** est structurante : un analyste non russophone a une visibilité très partielle sur l'écosystème russophone. Les équipes CTI matures recrutent des locuteurs natifs ou utilisent des partenariats (SentinelOne, Recorded Future, Kaspersky, Sekoia, Group-IB ont tous des équipes multilingues).

### 4.5 Les évolutions structurantes 2020-2026

Plusieurs tendances transforment l'écosystème.

**Professionnalisation continue**. Les opérateurs sont devenus plus matures techniquement, OPSEC plus rigoureuse, modèles économiques plus articulés (RaaS, CaaS). L'amateurisme des années 2010 est en recul.

**Commoditisation de l'accès**. Les stealer logs et les IAB ont abaissé les barrières d'entrée. Un acteur peu sophistiqué peut désormais, avec quelques centaines de dollars, acquérir un accès à une entreprise et lancer une attaque.

**Convergence clearnet/darkweb**. Beaucoup d'activité qui aurait été sur Tor en 2015 est maintenant sur Telegram, Discord, certains forums clearnet à accès restreint. L'analyste doit donc couvrir un spectre plus large que le seul .onion.

**Pression réglementaire et policière**. Multiplication des opérations de démantèlement, sanctions ciblées (Tornado Cash, adresses OFAC), coopération internationale renforcée, durcissement du KYC sur les exchanges crypto. Impact : augmentation des coûts opérationnels, accélération de la rotation des plateformes, montée de la paranoïa.

**Intégration de l'IA**. Deepfakes, chatbots criminels, automatisation du phishing, assistance au développement de malware. L'IA abaisse encore les barrières pour les acteurs peu qualifiés, même si elle ne transforme pas un script kiddie en APT.

**Retour de balancier vers les .onion**. Après le durcissement de Telegram post-Durov, certains acteurs retournent vers les forums .onion historiques — meilleure résilience juridique, même si accès plus friction.

### 4.6 Ce que l'analyste doit retenir

Trois principes opérationnels pour aborder le dark web.

**C'est un écosystème, pas un lieu**. On n'« entre pas dans le dark web » comme on entre dans un bâtiment — on observe un ensemble d'espaces distincts, chacun avec ses règles, sa langue, ses acteurs. L'investigation se déplace entre forums, marchés, messageries, leak sites selon les pistes.

**Les acteurs jouent des rôles spécialisés**. L'IAB ne fait pas de ransomware ; l'opérateur RaaS n'exfiltre pas ; le blanchisseur ne vole pas. Cette spécialisation structure les chaînes d'attaque et fournit les angles d'investigation.

**L'écosystème évolue vite**. Un forum qui dominait il y a 18 mois a pu exit-scammer, être saisi, ou migrer. Les statistiques de prix bougent, les pseudonymes changent, les plateformes tombent. La connaissance acquise doit être rafraîchie en continu — ce qui fait de la veille (Ch.27) un pilier de la pratique.

---
