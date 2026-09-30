---
title: Chapitre 4 — Le dark web comme écosystème
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - 'Partie I — Fondations : COMPRENDRE LE DARK WEB'
  - index.md
---

Le dark web n'est pas une seule chose — c'est un **écosystème** composé d'acteurs aux rôles distincts, d'espaces aux fonctions différentes, et de mécanismes de circulation qui le font fonctionner. Ce chapitre pose le cadre que les parties suivantes approfondiront.

## 4.1 Les types d'espaces

Six grandes catégories d'espaces dark web, détaillées en Partie III.

**Forums** (Ch.10) : espaces de discussion structurés autour de thèmes (fraude, hacking, drogues, données, géographie). Modérés, avec hiérarchie de membres (newbie, member, trusted, VIP, moderator, admin), système de réputation. XSS Forum, Exploit.in, BreachForums successive, IndustrialLeaks (fictif, inspiré de cas réels).

**Marchés (marketplaces)** (Ch.11) : plateformes d'e-commerce clandestin, avec listings, panier, escrow, ratings. AlphaBay historique, Abacus Market, BlackSprut (ru), Mega (ru), TorZon.

**Leak sites** (Ch.12) : vitrines publiques des groupes ransomware, où ils revendiquent les victimes et menacent de publier les données volées. LockBit, ALPHV/BlackCat, Black Basta, RansomHub, Play, Qilin — chacun avec son esthétique propre.

**Messageries et canaux** (Ch.13) : Telegram, Matrix via Tor, Session, Jabber/XMPP, Tox. Les messageries servent à la fois comme canaux opérationnels (négociations, coordination) et comme canaux de diffusion (canaux publics avec abonnés).

**Marchés spécialisés** : marchés de logs (Russian Market), marchés de fraude (Genesis historique, successeurs), marchés 0-day (Ch.17).

**Services** : infrastructure hosting bulletproof, blanchiment-as-a-service, cryptage-as-a-service, bot-as-a-service, phishing kits.

## 4.2 Les types d'acteurs

**Opérateurs de plateformes** : développeurs et administrateurs des forums, marchés, leak sites. Économiquement, ils prélèvent des commissions (1-10% sur les transactions), des frais d'inscription, des frais de vendeur. Politiquement, ils arbitrent les conflits. Opérationnellement, ils gèrent la résilience technique.

**Vendeurs** : acteurs qui monétisent des produits ou services sur les marchés. Spécialisations multiples : drug vendors, carders, credential brokers, fullz vendors, weapon vendors, 0-day brokers, service providers.

**Acheteurs** : clients finaux ou intermédiaires. Profils variés — particuliers cherchant drogues ou documents, cybercriminels achetant des outils, fraudeurs achetant des données, opérateurs ransomware achetant des accès IAB.

**Initial Access Brokers (IAB)** : acteurs spécialisés dans la compromission initiale d'organisations et la vente des accès à d'autres acteurs (typiquement des opérateurs ransomware). Chaîne de valeur centrale de la cybercriminalité contemporaine.

**Affiliés RaaS** : opérateurs qui déploient un ransomware-as-a-service moyennant partage des gains avec le propriétaire du malware.

**Blanchisseurs** : spécialistes de la conversion crypto → fiat utilisable, typiquement 10-30% de commission sur le montant blanchi.

**Services transversaux** : hébergeurs bulletproof, développeurs de malware, opérateurs botnets, crypters, spammers.

**Analystes CTI, forces de l'ordre, journalistes** : observateurs, dans des postures légales variées (voir Partie V sur le cadre légal et Ch.30 sur l'infiltration policière).

## 4.3 Les flux qui font fonctionner l'écosystème

**Flux d'information** : montée en crédibilité des vendeurs, annonces de produits/services, négociations, litiges. Support : forums, canaux dédiés aux marchés, messageries privées.

**Flux financier** : paiements via cryptomonnaies (Bitcoin historique mais en repli, Monero en hausse, quelques stablecoins type USDT), escrow sur les marchés, blanchiment aval. Ch.8 détaille les mécanismes.

**Flux de confiance** : réputation construite par l'historique transactionnel, vouching par membres établis, arbitrage en cas de litige. Sans ces mécanismes, l'économie ne fonctionnerait pas. Ch.19 détaille.

**Flux de données** : données volées circulent des breachers initiaux vers les courtiers, puis vers les acheteurs finaux. Chaîne typique : breach → vente exclusive à prix élevé → revente en baisse → diffusion gratuite tardive (Ch.14).

**Flux d'accès** : les IAB compromettent → vendent l'accès → l'acheteur déploie ransomware ou autre monétisation. Chaîne souvent constatée dans les investigations post-incident.

## 4.4 La géographie linguistique et culturelle

L'écosystème dark web est structuré par **plusieurs blocs linguistiques** largement cloisonnés.

**Bloc russophone** : le plus large historiquement. Forums majeurs (XSS, Exploit.in, RAMP historique), marchés (Hydra historique, successeurs), opérateurs ransomware (LockBit, Conti, ALPHV). La ligne russophone inclut ex-URSS (Russie, Bélarus, Ukraine pré-2022, Kazakhstan, etc.). Règle opérationnelle tacite des groupes russophones : **ne pas cibler la CEI** (Communauté des États indépendants) — règle respectée en grande partie, traduite dans le code de certains ransomware (vérification de la langue du clavier, exclusion des locales russophones).

**Bloc anglophone** : historiquement dominant pour les marchés généralistes (Silk Road, AlphaBay, Dream), devenu plus discret post-grandes saisies. Forums anglophones majeurs (BreachForums multiple, RaidForums historique).

**Bloc chinois** : opère largement sur des plateformes spécifiques, avec forums et canaux accessibles aux sinophones. Moins documenté dans les analyses vendor occidentales, nécessite une expertise linguistique spécialisée.

**Bloc persophone et arabophone** : croissance notable depuis 2020, avec des forums et canaux dédiés, activités orientées fraude, credentials, et parfois opérations liées à des tensions géopolitiques régionales.

**Autres** : francophone (présence modeste, parfois sur forums anglophones), hispanophone (Amérique latine, forums cartels), portugaise (Brésil), turc, coréen.

Pour l'analyste, la **barrière linguistique** est structurante : un analyste non russophone a une visibilité très partielle sur l'écosystème russophone. Les équipes CTI matures recrutent des locuteurs natifs ou utilisent des partenariats (SentinelOne, Recorded Future, Kaspersky, Sekoia, Group-IB ont tous des équipes multilingues).

## 4.5 Les évolutions structurantes 2020-2026

Plusieurs tendances transforment l'écosystème.

**Professionnalisation continue**. Les opérateurs sont devenus plus matures techniquement, OPSEC plus rigoureuse, modèles économiques plus articulés (RaaS, CaaS). L'amateurisme des années 2010 est en recul.

**Commoditisation de l'accès**. Les stealer logs et les IAB ont abaissé les barrières d'entrée. Un acteur peu sophistiqué peut désormais, avec quelques centaines de dollars, acquérir un accès à une entreprise et lancer une attaque.

**Convergence clearnet/darkweb**. Beaucoup d'activité qui aurait été sur Tor en 2015 est maintenant sur Telegram, Discord, certains forums clearnet à accès restreint. L'analyste doit donc couvrir un spectre plus large que le seul .onion.

**Pression réglementaire et policière**. Multiplication des opérations de démantèlement, sanctions ciblées (Tornado Cash, adresses OFAC), coopération internationale renforcée, durcissement du KYC sur les exchanges crypto. Impact : augmentation des coûts opérationnels, accélération de la rotation des plateformes, montée de la paranoïa.

**Intégration de l'IA**. Deepfakes, chatbots criminels, automatisation du phishing, assistance au développement de malware. L'IA abaisse encore les barrières pour les acteurs peu qualifiés, même si elle ne transforme pas un script kiddie en APT.

**Retour de balancier vers les .onion**. Après le durcissement de Telegram post-Durov, certains acteurs retournent vers les forums .onion historiques — meilleure résilience juridique, même si accès plus friction.

## 4.6 Ce que l'analyste doit retenir

Trois principes opérationnels pour aborder le dark web.

**C'est un écosystème, pas un lieu**. On n'« entre pas dans le dark web » comme on entre dans un bâtiment — on observe un ensemble d'espaces distincts, chacun avec ses règles, sa langue, ses acteurs. L'investigation se déplace entre forums, marchés, messageries, leak sites selon les pistes.

**Les acteurs jouent des rôles spécialisés**. L'IAB ne fait pas de ransomware ; l'opérateur RaaS n'exfiltre pas ; le blanchisseur ne vole pas. Cette spécialisation structure les chaînes d'attaque et fournit les angles d'investigation.

**L'écosystème évolue vite**. Un forum qui dominait il y a 18 mois a pu exit-scammer, être saisi, ou migrer. Les statistiques de prix bougent, les pseudonymes changent, les plateformes tombent. La connaissance acquise doit être rafraîchie en continu — ce qui fait de la veille (Ch.27) un pilier de la pratique.

---
