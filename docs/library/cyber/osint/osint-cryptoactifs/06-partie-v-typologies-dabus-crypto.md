---
title: PARTIE V — TYPOLOGIES D’ABUS CRYPTO
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
chapter: 6
chapters: 10
---

> **Ce que cette partie apprend.** Reconnaître les grandes typologies d’abus crypto contemporains : pig butchering et scams retail, ransomware et extorsion, hacks DeFi et compromission de wallets, fraudes NFT et tokens, acteurs étatiques (Lazarus). Pour chacune : patterns, modus operandi, signaux, méthodes d’enquête spécifiques.
> 
> **Ce qu’elle ne couvre pas.** Les techniques d’obfuscation détaillées (Partie VI), les cas pratiques déroulés (Partie VII), les cas historiques (Partie VIII).
> 
> **Ce que vous saurez faire après cette partie.** Identifier rapidement la typologie d’une affaire à partir des indices initiaux. Adapter la méthode d’enquête à la typologie. Reconnaître les signaux d’alerte spécifiques. Comprendre où chaque type d’abus s’inscrit dans l’écosystème crypto criminel global.

-----

## Chapitre 25 — Scams retail : romance scam et pig butchering

Le **pig butchering** (« 杀猪盘 », *shā zhū pán* — « élevage du cochon avant l’abattage ») est devenu en 2022-2026 l’un des plus gros postes de pertes financières liées au crypto, avec des estimations Chainalysis cumulées en milliards USD/an. Il combine manipulation sentimentale et faux investissement, ciblant des victimes individuelles sur des durées de plusieurs mois.

### 25.1 Le modus operandi

**Phase 1 — Approche**. La victime est contactée :

- Via réseaux sociaux (Instagram, LinkedIn, Facebook).
- Via applications de rencontre (Tinder, Bumble, Hinge).
- Via WhatsApp ou Telegram (« mauvais numéro » prétendu).
- Via groupes d’investissement crypto Telegram / Discord.

L’approche est **généralement chaleureuse**, sans demande financière initiale. Construction d’une relation (amicale, sentimentale, professionnelle).

**Phase 2 — Construction de la confiance**. Sur plusieurs semaines/mois :

- Communications quotidiennes.
- Partage de détails « personnels » (vie, famille, succès).
- Création d’intimité.
- Mention progressive du « succès en investissement crypto ».
- Photos volées d’autres personnes (réelles ou IA-générées).

**Phase 3 — Introduction de l’investissement**. Le scammer mentionne :

- Une « plateforme exclusive » avec « gains garantis ».
- Un « mentor » ou « insider tip ».
- Des « gains incroyables » que le scammer prétend avoir réalisés (captures truquées montrant son « portefeuille »).

**Phase 4 — Premier dépôt et premier retrait**. La victime dépose une **petite somme** (500-5000 USD) sur la plateforme frauduleuse. Le scammer **autorise un petit retrait** initial pour crédibiliser. La victime voit ses fonds revenir, gagne confiance.

**Phase 5 — Escalade**. Encouragée par le « succès initial », la victime augmente progressivement :

- Investissements plus gros.
- Prises de prêts pour investir plus.
- Liquidation d’épargne.
- Demande aux proches.

**Phase 6 — Le « chômage » du retrait**. Quand la victime tente de retirer une somme significative :

- « Frais d’audit fiscal » à payer.
- « Caution de sécurité » exigée.
- « Vérification d’identité supplémentaire » qui débloque un retrait moyennant nouveau paiement.
- Cycle : chaque demande de retrait génère une nouvelle demande de paiement.

**Phase 7 — Disparition**. Quand la victime réalise (ou n’a plus rien à donner), le scammer disparaît. Compte coupé, profil supprimé, plateforme inaccessible.

**Bilans typiques** : pertes individuelles de 50 k à 1 M USD+. Cas documentés dépassant 5 M USD pour victimes uniques.

### 25.2 Le réseau opérateur

**Pig butchering n’est PAS un scam individuel**. C’est une **industrie**.

**Structure typique** :

- **Scam compounds** localisés en Asie du Sud-Est (Cambodge, Laos, Myanmar, Philippines). Bâtiments où des centaines à milliers de **« scammeurs »** (parfois eux-mêmes victimes de trafic humain) opèrent sous coercion.
- **Opérateurs / patrons** : organisations criminelles (souvent liées à des syndicats chinois) qui gèrent les compounds.
- **Réseau de blanchiment** : flux USDT-TRON consolidant les paiements des victimes.
- **Infrastructure** : plateformes web crédibles, sites de phishing, canaux Telegram/WhatsApp.

**Cooperation avec le crime organisé**. ZachXBT, OFAC et plusieurs reports (Chainalysis, TRM, Elliptic) documentent depuis 2022-2024 le rôle de syndicats criminels asiatiques dans le pig butchering. Sanctions contre certains compounds documentées.

**Pour la victime** : dans la grande majorité des cas, le « scammeur » qui lui parle quotidiennement n’est **pas le décideur** — c’est un opérateur de bas niveau sous pression (parfois traffiqué). La structure derrière est ce qui prélève les fonds et organise le blanchiment.

### 25.3 Les flux crypto typiques

**Pattern observable on-chain** :

**Étape 1 — Réception sur adresse de collecte**. La plateforme frauduleuse demande à la victime d’envoyer USDT-TRON (le plus fréquent, ou parfois USDT-Ethereum, plus rarement BTC) vers une adresse spécifique.

**Étape 2 — Adresses de collecte multi-victimes**. Sur Tronscan, on observe l’**adresse de collecte** recevant des USDT depuis plusieurs adresses de victimes différentes. Un cluster typique :

- Adresse de collecte centrale.
- 10-100 adresses de victimes envoyant.
- Montants variables (de 500 à 100 000+ USD chacun).
- Période étalée sur semaines/mois.

**Étape 3 — Consolidation rapide**. L’adresse de collecte transfère rapidement les fonds vers une adresse hub.

**Étape 4 — Layering**. Le hub fait du peeling chain TRON-style ou disperse vers multiples sub-adresses.

**Étape 5 — Off-ramp**. Les fonds finissent vers :

- Exchanges régionaux moins regardants (souvent Asie).
- P2P / OTC.
- Conversion en autres cryptos (BTC, monero, autres).
- Cartes prepaid crypto.

### 25.4 Reconnaître un cluster pig butchering

**Signaux** :

**Adresse de collecte centrale** recevant de **multiples sources** (>5-10 victimes différentes).

**Montants variables** (pas tous identiques) — caractéristique de victimes individuelles vs scam d’identité de masse.

**Pattern temporel étalé** sur des semaines/mois (vs scam ponctuel).

**Consolidation rapide** vers hub après réception.

**Flux vers exchanges régionaux** ou P2P en finale.

**Activité concentrée** sur USDT-TRON.

**Fraîcheur** : les adresses de collecte sont souvent fraîches (créées peu avant l’opération), réutilisées sur quelques semaines, puis abandonnées au profit de nouvelles.

### 25.5 Méthode d’enquête

**Étape 1 — Indice initial**. Souvent : adresse fournie par victime + screenshots conversation + détails plateforme frauduleuse.

**Étape 2 — Validation**. TXID confirmant le dépôt. Lecture sur Tronscan.

**Étape 3 — Expansion vers cluster**. Identifier l’**adresse de collecte** (premier destinataire). Lire son historique : combien d’autres dépôts a-t-elle reçu ? Volume cumulé ? Patterns ?

**Étape 4 — Identification d’autres victimes**. Les autres adresses ayant déposé sur la même collecte sont **probablement d’autres victimes**. Si la victime principale fait plainte, ces co-victimes peuvent être identifiées (et alerter les autorités si plaintes coordonnées).

**Étape 5 — Suivi des flux post-collecte**. Le hub redistribue vers où ? Identification des chemins de blanchiment.

**Étape 6 — Off-ramps**. Identification des exchanges utilisés en finale. Si exchange régulé : possibilité de réquisition KYC.

**Étape 7 — Rapport et action**.

### 25.6 Limites de l’enquête pig butchering

**Récupération rare**. Les fonds sont souvent dispersés rapidement. Le délai entre dépôt victime et cashout est court (jours/semaines). Au moment où la victime réalise et porte plainte, fonds sont souvent déjà out.

**Identification du « scammeur » individuel** : très difficile. C’est rarement un acteur identifiable (compounds Asie du Sud-Est).

**Identification des opérateurs** : possible via patterns à grande échelle, mais judiciairement complexe (juridictions, coopération internationale variable).

**Effet psychologique sur victime**. La victime est souvent **doublement traumatisée** : perte financière + manipulation sentimentale révélée. Approche humaine importante.

**Réponse défensive sectorielle** : sensibilisation grand public, alertes plateformes, partenariats avec banques pour détecter virements suspects.

### 25.7 Coordination

**Signalement aux autorités** :

- **Cybermalveillance.gouv.fr** (France) : pour victimes individuelles.
- **TRACFIN** : pour banque détectant flux suspect.
- **Plainte police / gendarmerie** locale.
- **FBI IC3** (US) si concerné.

**Coopération internationale** :

- **Operation Shamrock** (US, depuis 2024) : coordination LEA contre pig butchering.
- **GLACY+ Council of Europe** : capacity building anti-cybercrime.
- **Europol EC3** : coordination EU.

**Sanctions** : OFAC a sanctionné certains compounds et opérateurs depuis 2024. Suivre les listes pour adresses sanctionnées.

### 25.8 Cas typiques

**Romance scam pure** : intimité construite, demande de fonds pour « urgence familiale » ou « problème médical ». Moins de prétention investissement, plus d’émotionnel.

**Faux investissement plateformes**. Plateforme prétendant être trading bot, AI investment, DeFi proprietary. Captures truquées de gains.

**Faux investissement « insider »**. Le scammer prétend avoir un « tip » d’initié sur une crypto qui va exploser. Transfert vers « sa » plateforme.

**Faux investissement pyramidal**. Combinaison schéma de Ponzi et scam — les premiers déposants peuvent retirer (avec fonds des suivants) jusqu’à effondrement.

**Job scam**. Variation : la victime est « recrutée » pour faire du « trading test », doit déposer pour qualifier, puis bloquée.

### 25.9 Tendances 2024-2026

**Augmentation explosive** depuis 2022.

**IA dans le scam** :

- Génération d’images de profil par IA (StyleGAN, Stable Diffusion, etc.).
- Voice cloning pour appels téléphoniques crédibles.
- Chatbots IA pour gérer multiples victimes simultanément.
- Multi-langue automatique pour cibler globalement.

**Blanchiment via stablecoins** dominant.

**Sophistication accrue** des plateformes frauduleuses (UI proche d’exchanges légitimes).

**Pour l’enquêteur** : la **typologie évolue**. Les patterns 2026 incluent IA et stablecoins multi-chaînes. La méthodologie de base reste mais s’adapte.

-----

## Chapitre 26 — Ransomware et extorsion

Le ransomware est l’un des plus gros postes médiatisés de cybercriminalité. Pour l’enquêteur crypto, c’est aussi un **flux structuré et reconnaissable**, particulièrement adapté à l’analyse on-chain.

### 26.1 Le modèle économique

**Acteurs** :

- **Opérateurs / développeurs** : fournissent malware + infrastructure (leak site, portail négociation).
- **Affiliés** : exécutent les attaques, prennent typiquement 70-80% des rançons.
- **Initial Access Brokers (IAB)** : vendent les accès initiaux aux affiliés.
- **Négociateurs** : négocient avec les victimes côté criminel.
- **Services de blanchiment** : prennent en charge les flux post-paiement.

**Flux financier typique** :

1. Victime paie en crypto (BTC dominant, parfois XMR pour Monero-only).
1. Adresse de réception dédiée à la victime.
1. Mouvement post-paiement : peeling chain ou consolidation rapide.
1. Conversion potentielle (vers stablecoins, autres chaînes).
1. Anonymisation : mixers, bridges, swaps.
1. Cashout : exchanges non-KYC, P2P, OTC.

### 26.2 Le paiement

**Formats** :

- **Adresse fournie via portail Tor** : opérateurs maintiennent portails de négociation .onion, victime y accède pour négocier et obtenir l’adresse.
- **Adresse dans note de rançon** : moins courant pour gros opérateurs (préfèrent négociation), plus fréquent pour ransomware moins ciblé.
- **Email avec adresse** : sextortion et ransomware basique.

**Délai de paiement** : typiquement 7-14 jours négociés. Au-delà, leak site publication ou augmentation de la demande.

**Adresses fraîches dédiées**. La pratique standard est : **une adresse par victime**, fraîche, jamais utilisée. Évite que d’autres victimes (ou des observateurs) voient les paiements totaux.

### 26.3 Reconnaître un cluster ransomware

**Signaux d’une adresse ransomware** :

**Réception unique de gros montant**. Adresse fraîche reçoit un montant rond ou semi-rond (35 BTC, 50 BTC, 100 BTC…) en une seule transaction.

**Mouvement rapide post-paiement**. Le délai entre réception et premier mouvement est souvent court (heures à 1-2 jours).

**Pattern de blanchiment standardisé**. Peeling chain, consolidation, conversions. Les opérateurs établis ont des patterns reconnaissables.

**Multiple paiements pour le même opérateur**. Sur les outils pro, les clusters ransomware sont identifiés (« cluster Akira », « cluster LockBit », « cluster Black Basta »). Les nouvelles adresses sont assignées au cluster sur la base d’heuristiques + labels propriétaires.

### 26.4 Cluster opérateur vs cluster affilié

Distinction importante.

**Cluster opérateur** : infrastructure de l’opérateur (développeurs du ransomware). Reçoit la part de l’opérateur (~20-30% des rançons). Stable dans le temps.

**Cluster affilié** : infrastructure des affiliés. Reçoit la part de l’affilié (~70-80%). Multiple affiliés par opérateur, chacun avec ses patterns.

**Pour l’enquêteur** : identifier si l’enquête remonte vers opérateur ou affilié change la lecture. Affilié = un acteur parmi N. Opérateur = peut révéler infrastructure plus large.

### 26.5 Méthode d’enquête

**Étape 1 — Indices initiaux**. Adresse de paiement (du portail négociation, de la note ransomware, ou de la victime).

**Étape 2 — Validation**. TXID confirmant le paiement. Lecture sur Mempool.

**Étape 3 — Identification du cluster**. Outils pro identifient le cluster. Parfois directement attribué à un groupe ransomware.

**Étape 4 — Suivi des flux**. Comme MIXSHADOW : peeling chain, conversions, etc.

**Étape 5 — Identification des points de coopération**. Exchanges traversés, mixers, bridges.

**Étape 6 — Caractérisation du groupe**. Patterns, infrastructure, leak site, victimologie.

**Étape 7 — Rapport et coopération**.

### 26.6 Coopération avec les autorités

**FBI Cyber Division** (US) : référence pour ransomware. Multiple opérations (saisie Bitfinex, opération Cronos contre LockBit, etc.).

**NCA (UK)** : équivalent.

**Europol EC3** : coordination EU.

**ANSSI / DGSI / TRACFIN** (France) : pour victimes françaises.

**BKA (Allemagne)**.

**Coopération exchanges** : nombreux exchanges réguliers gèlent fonds tracés à ransomware sur réquisition.

**Coopération émetteurs stablecoins** : Tether et Circle ont gelé à plusieurs reprises des fonds de groupes ransomware.

### 26.7 Le débat « payer ou pas »

**Position officielle (US, France, UK)** : **déconseiller le paiement**. Arguments :

- Finance la criminalité.
- Ne garantit pas le déchiffrement.
- Crée incitation pour autres attaques.
- Peut violer sanctions OFAC (si groupe sanctionné).

**Réalité** : la décision relève de la victime, sous pression vitale (cf MIXSHADOW). Pas de critère universel.

**Pour l’enquêteur** : pas de jugement moral. Si paiement, l’enquête maximize la valeur (récupération potentielle, attribution, contribution sectorielle).

### 26.8 Tendances 2024-2026

**Multi-extorsion** : chiffrement + exfiltration + chantage clients + DDoS. Rançons plus élevées.

**Dual ransomware** : double chiffrement par deux groupes différents (rare mais documenté).

**Ciblage de la santé et OIV** : croissance.

**Sanctions et démantèlements** : LockBit (Operation Cronos février 2024), AlphaV/BlackCat, Hive (saisie 2023). Écosystème en mutation continue.

**Akira, Black Basta, Play, LockBit (relaunch), Medusa** : groupes actifs 2025-2026.

**Pour l’enquêteur** : la **typologie ransomware est pleine d’enjeux** mais aussi de **success stories** (Bitfinex saisie 3,6 Mrd, Colonial Pipeline récupération 2,3 M, opérations Cronos). L’enquête contribue.

-----

## Chapitre 27 — Hacks DeFi et compromission de wallets

Les hacks DeFi et compromissions de wallets représentent des **milliards USD/an** depuis 2021 selon Chainalysis. Différent du ransomware (où victime paie volontairement) — ici, fonds sont **volés** sans consentement.

### 27.1 Hacks de protocoles DeFi

**Vecteurs typiques** :

**Vulnérabilités de smart contracts**. Bug dans le code (re-entrancy, overflow, logique faillible). Permet à attaquant de drainer le protocole.

**Compromission de clés admin**. Si un protocole DeFi a des fonctions admin (upgrade, pause, mint), compromission de la clé admin = takeover total.

**Oracles attaques**. Manipulation des oracles de prix utilisés par le protocole. Permet de profiter des conditions favorables artificielles.

**Flash loan attacks**. Combinaison de flash loans (prêts non-collatéralisés sur 1 transaction) avec exploitation de vulnérabilités. Permet à attaquant sans capital initial de drainer un protocole.

**Bridge exploits**. Bridges cross-chain sont particulièrement vulnérables (combinaison de smart contracts complexes et de validateurs externes). Cf Ronin (Ch.43), Wormhole (2022, 326 M USD), Nomad (2022, 190 M USD), Multichain (2023, 130 M USD).

**Cas marquants** :

- **Ronin Network** (mars 2022, 625 M USD) — Lazarus / DPRK.
- **Wormhole** (février 2022, 326 M USD) — restitution partielle suite à exploit reverse.
- **Nomad** (août 2022, 190 M USD) — exploitation chaotique multi-acteurs.
- **Mango Markets** (octobre 2022, 117 M USD) — Avraham Eisenberg, condamné aux US.
- **Curve Finance** (juillet 2023, 70 M USD).
- **Mixin Network** (septembre 2023, 200 M USD).
- **Multiple en 2024-2026** : pertes cumulées en milliards.

**Bilan annuel** : Chainalysis 2024 indique des fonds volés dans crypto en hausse, atteignant des chiffres records. Mid-year update 2025 confirme la tendance.

### 27.2 Compromission de wallets utilisateurs

**Vecteurs** :

**Stealer logs**. Malware (Lumma, RedLine, Vidar, etc.) qui vole credentials, cookies, seed phrases stockées localement. Cf cours Dark Web.

**Phishing de seed phrase**. Sites imitant wallet officiel demandant seed phrase « pour vérification ».

**Compromission email + reset MFA**. Reset password exchange / SMS swap / SIM swap.

**Approval phishing / drainers** (Ch.9). Site faux qui fait signer approval, drainer vide le wallet.

**Compromission physique**. Vol de hardware wallet, contraintes physiques. Plus rare.

**Bilan** : Chainalysis 2024-2025 souligne **augmentation forte** des fonds volés via compromission de wallets personnels. Particulièrement pour adresses high-value (whale wallets).

### 27.3 Reconnaître un hack vs vol vs scam

**Hack DeFi** :

- Exploit technique d’un protocole.
- Smart contract vidé.
- Souvent montant élevé (millions à centaines de millions USD).
- Communauté DeFi alertée immédiatement (twitter, dashboards).

**Compromission wallet individuel** :

- Wallet personnel vidé.
- Drainer ou transfert direct.
- Montants variables (quelques USD à millions USD).
- Souvent identifié par victime via alerte mouvement inattendu.

**Scam** (rug pull, fake token, etc.) :

- Investisseurs ont **volontairement** investi.
- Token déprécié à zéro après dump du créateur (rug pull).
- Différent du hack — pas de vulnérabilité exploitée techniquement, mais escroquerie sur l’intention.

L’enquête diffère selon catégorie.

### 27.4 Méthode d’enquête : hack DeFi

**Étape 1 — Détection / annonce**. Souvent annoncé immédiatement par victime ou observers (Twitter/X, Rekt News, Defi Watch).

**Étape 2 — Identification de la transaction d’exploit**. Le hash de la transaction où l’exploit s’est produit est public (sinon on cherche dans les transactions du protocole).

**Étape 3 — Lecture de la transaction**. Sur Etherscan / Phalcon / Tenderly :

- Comprendre la **logique exploit**.
- Identifier les **smart contracts** appelés.
- Identifier les **adresses attaquant**.

**Étape 4 — Suivi des fonds volés**. Méthode standard. Souvent les attaquants utilisent immédiatement Tornado Cash, bridges, ou d’autres techniques d’obfuscation.

**Étape 5 — Identification de l’attaquant**. Si trace publique (white hat hack annoncé), identification facile. Si exploit anonyme, attribution probable via patterns.

**Étape 6 — Coopération avec protocole victime et exchanges**. Souvent demande de gel à exchanges si fonds y atterrissent. Bounty du protocole pour incitation à restitution.

**Étape 7 — Rapport et action**.

### 27.5 Méthode d’enquête : compromission wallet

**Étape 1 — Indices initiaux**. La victime fournit son adresse, le timestamp du drainage, et idéalement des informations sur le vecteur (« j’ai cliqué sur ce lien… », « je crois que mon ordinateur a un virus… »).

**Étape 2 — Lecture des transactions de drainage**. Sur Etherscan, les **dernières transactions** du wallet de la victime montrent où sont allés les fonds.

**Étape 3 — Identification du drainer**. Si pattern approval phishing : voir les transactions d’`approve` précédentes. Identifier le smart contract du drainer.

**Étape 4 — Suivi des fonds drainés**. Le drainer consolide vers son propre wallet, qui ensuite blanchit.

**Étape 5 — Identification du drainer service**. Beaucoup de drainers sont **services-as-a-service** (Inferno Drainer, Pink Drainer historiquement, autres en 2024-2026). Identification du service permet attribution macro.

**Étape 6 — Coopération**. Si fonds vers exchange régulé : demande de gel.

### 27.6 Limites

**Récupération**. Variable. Hacks DeFi : parfois récupération via négociation (white hat reward) ou pression. Compromissions individuelles : récupération rare.

**Attribution**. Hacks sophistiqués (Lazarus) : attribution publique parfois. Drainers individuels : souvent anonymes.

**Vitesse**. Les hackers sont rapides. Les premières heures sont critiques. Si l’enquête ne démarre pas dans la journée, fonds souvent déjà out.

### 27.7 Tendances 2024-2026

**Hacks DeFi** : continuent à grand échelle. Bridges restent ciblés.

**Drainer-as-a-service** : démocratisation des drainers, baisse de la barrière technique.

**Lazarus** : continue à dominer les hacks majeurs. ~Mrd USD/an attribués.

**Compromission de wallets via stealer logs** : croissance massive.

**Retraits forcés via violence physique** : émergent (« 5 dollar wrench attacks », attaques contre des holders identifiés).

-----

## Chapitre 28 — Fraudes NFT, tokens frauduleux et rug pulls

L’écosystème NFT et tokens connaît une **forte sinistralité fraude**. Différentes typologies, chacune avec ses patterns.

### 28.1 Rug pulls

**Schéma** :

1. Création d’un token (ERC-20, BEP-20, SPL, etc.).
1. Marketing intense (Twitter, Discord, Telegram, parfois influenceurs).
1. Liquidité ajoutée sur DEX (paire token/ETH ou token/USDT).
1. Investisseurs achètent.
1. Au pic, **les créateurs vident la liquidité** (« pull the rug »).
1. Token à zéro, investisseurs perdent tout.

**Variantes** :

- **Soft rug** : créateurs disparaissent silencieusement, abandon du projet.
- **Hard rug** : drain explicite de la liquidité.
- **Honeypot** : token codé pour empêcher acheteurs de revendre (techniquement plus subtil).

**Reconnaissance** :

- Tokens nouveaux sans audit.
- Concentration de l’offre dans quelques wallets (owner garde 50%+).
- Liquidité non « locked ».
- Communauté artificielle (bots).

### 28.2 Honeypot tokens

**Mécanisme** : le smart contract du token contient une fonction cachée qui empêche les acheteurs (sauf le créateur) de revendre. Investisseurs achètent, **ne peuvent jamais sortir**.

**Détection** : analyse du code Solidity. Fonctions avec conditions cachées sur `transfer`. Outils comme Token Sniffer, GoPlus automatisent.

### 28.3 Pump-and-dump

**Schéma** :

1. Création / sélection d’un token de faible capitalisation.
1. Coordination dans groupes Telegram / Discord (« pump signal »).
1. Achats coordonnés synchronisés.
1. Cours du token explose (multiplication 5-50x).
1. Insiders / leaders **dumpent** au pic.
1. Cours s’effondre, late-comers perdent.

Sur Solana 2024-2026, l’écosystème **memecoin** (pump.fun et associés) industrialise ce schéma à échelle massive.

### 28.4 Fraude NFT

**Faux mint**. Site phishing imitant un drop NFT légitime. Demande approval qui draine wallet.

**Faux marketplace**. Plateforme imitant OpenSea/Blur, avec listings frauduleux ou drainer.

**Wash trading**. Achats / ventes d’NFT entre wallets contrôlés par même entité, pour gonfler artificiellement le « volume » et tromper acheteurs.

**Fake collections**. Collections imitant collections célèbres (CryptoPunks, BAYC) avec léger changement de nom ou logo.

**Fake floor**. Listings à très bas prix (faux) pour attirer attention sur une collection.

**Phishing Discord**. Hack de Discord officiel d’un projet NFT, annonce de mint frauduleux qui draine wallets.

### 28.5 Méthode d’enquête : rug pull

**Étape 1 — Indices**. Token contracté, plainte d’investisseurs.

**Étape 2 — Analyse du contrat**. Lecture Solidity (si vérifié) ou bytecode. Identification de fonctions backdoor.

**Étape 3 — Identification des wallets créateurs**. Adresse de déploiement du contrat. Premiers holders. Adresses ayant ajouté la liquidité initiale.

**Étape 4 — Analyse des mouvements**. Quand les créateurs ont-ils dump ? Vers où ?

**Étape 5 — Suivi des fonds**. Standard.

**Étape 6 — Identification des créateurs**. Si OPSEC faible (réutilisation d’adresses, déposit sur exchange KYC), attribution possible.

### 28.6 Méthode d’enquête : phishing NFT

**Étape 1 — Indices**. Victime fournit transaction de drain.

**Étape 2 — Identification du drainer**. Smart contract appelé. Souvent service connu (drainer-as-a-service).

**Étape 3 — Suivi des fonds**. Standard.

### 28.7 Limites

**Volume massif**. Trop de rug pulls / scams pour tous les enquêter individuellement. Triage obligatoire (impact, victimes notables).

**Anonymat des créateurs**. Souvent OPSEC stricte (création depuis wallets fonds Tornado Cash, etc.).

**Aspects civils vs pénaux**. Beaucoup de rug pulls relèvent de **fraude civile** plus que pénale (selon juridiction, intentionnalité difficile à prouver).

### 28.8 Tendances 2024-2026

**Memecoin scams** : explosion via pump.fun et écosystème Solana.

**AI-generated NFT scams** : NFT générés en masse pour rug pull.

**Cross-chain rug pulls** : exploitation de bridges et confusion multi-chaîne.

-----

## Chapitre 29 — Acteurs étatiques : Lazarus et contournement de sanctions

Les acteurs étatiques sophistiqués utilisent le crypto à grande échelle. **Lazarus** (DPRK / Corée du Nord) est l’archétype documenté. Les opérations de contournement de sanctions (Russie post-2022, Iran) sont également structurantes.

### 29.1 Le profil Lazarus

**Lazarus Group** (alias APT38, alias Hidden Cobra). Cluster d’acteurs DPRK opérant sous direction du Bureau 121 / Reconnaissance General Bureau (RGB).

**Évolution** :

- 2014-2016 : ciblage banques traditionnelles (SWIFT). Heist Bangladesh Bank 2016 : 81 M USD.
- 2017+ : pivot massif vers crypto. Cible exchanges, particuliers, DeFi.
- 2022+ : domination des plus gros vols crypto annuels.

**Cas marquants attribués** :

- **Ronin Network** (mars 2022, 625 M USD).
- **Harmony Bridge** (juin 2022, 100 M USD).
- **Atomic Wallet** (juin 2023, 100 M USD).
- **CoinEx** (septembre 2023, 54 M USD).
- **Stake.com** (septembre 2023, 41 M USD).
- **Multiple incidents** 2024-2025.

Estimations cumulées : **plusieurs milliards USD** volés depuis 2017. Selon TRM Labs et Chainalysis, Lazarus est l’acteur étatique le plus prolifique en crypto.

**Usage des fonds** : finance les programmes étatiques DPRK, contourne les sanctions internationales.

### 29.2 TTP Lazarus crypto

**Vecteurs d’accès** :

- Phishing sophistiqué (fake recruiters, fake job offers — « Operation Dream Job »).
- Compromission d’employés clés d’exchanges et protocoles.
- Vulnérabilités de smart contracts.
- Compromission d’infrastructure (nodes, relayers).

**Patterns de blanchiment** :

- **Tornado Cash** historiquement (avant sanctions août 2022, après aussi).
- **Bridges cross-chain** intensifs.
- **CoinJoin** Bitcoin.
- **Conversion en privacy coins** (Monero) parfois.
- **Off-ramp via OTC asiatiques** (Russie, Asie centrale).
- **Réseau de mules** pour cashout.

**Sophistication opérationnelle** : OPSEC souvent élevée. Wallets fraîs, infrastructure rotative, blanchiment méticuleusement structuré.

### 29.3 Reconnaître un cluster Lazarus

**Indicators** (selon TRM, Chainalysis, FBI) :

- Adresses précédemment attribuées à Lazarus dans les bases vendor.
- Patterns de blanchiment cohérents avec doctrine Lazarus.
- TTP de compromise compatibles.
- Liens infrastructure (mêmes serveurs, même malware family).

**Important** : Lazarus n’est **pas** la seule explanation pour des patterns sophistiqués. Sur-attribution est piège. Validation requise.

### 29.4 Sanctions et coopération

**OFAC** :

- A sanctionné de multiples wallets Lazarus.
- Sanction Tornado Cash (août 2022) cite Lazarus comme une des raisons.
- Mises à jour régulières.

**FBI** : très actif sur ransomware DPRK et Lazarus. Multiple advisory et identifications publiques.

**Coopération internationale** : tendue (DPRK n’est pas coopératif), mais pression des US/UE/Japon/Corée du Sud sur exchanges et points de cashout.

### 29.5 Russie et contournement de sanctions

Depuis 2022, contournement de sanctions Russie via crypto est documenté.

**Acteurs** :

- Particuliers russes contournant restrictions financières.
- Exchanges russes / liés (Garantex, sanctionné OFAC).
- Acteurs étatiques utilisant crypto pour transactions internationales.

**Outils** :

- Stablecoins (USDT-TRON dominant).
- P2P trading (LocalBitcoins historiquement, Binance P2P, autres).
- OTC desks dans juridictions permissives.

**Pour l’enquêteur** : flux Russie-related identifiables par patterns. Coopération avec exchanges pour gel possible (USDT-Tether a gelé multiples adresses Russie sur réquisition).

### 29.6 Iran et autres

**Iran** : usage crypto pour contourner sanctions, financer programmes étatiques. Cluster acteurs étatiques iraniens (« Pioneer Kitten », « APT34 », autres) avec activité crypto.

**Autres acteurs étatiques** : Chine (moins dans crypto direct, plus dans surveillance et minage), pays émergents avec capacité cyber moindre.

### 29.7 Méthode d’enquête : acteurs étatiques

**Étape 1 — Hypothèse étatique**. Patterns sophistiqués + indicateurs ne signifient **pas automatiquement** acteur étatique. Validation requise.

**Étape 2 — Recoupement avec bases vendor**. Chainalysis, TRM, Elliptic ont des labels « Lazarus », « Iran-related », etc. avec des niveaux de confiance.

**Étape 3 — Recoupement avec sources publiques**. OFAC SDN, FBI advisory, Mandiant / CrowdStrike threat reports.

**Étape 4 — Analyse TTP**. Patterns techniques (vecteurs, infrastructure, malware) si applicables.

**Étape 5 — Coopération**. Impossible directement (les acteurs sont étatiques). Coopération via FBI / Europol / autorités équivalentes pour suivre les flux et identifier points d’action (exchanges traversés, cashout).

**Étape 6 — Rapport et calibration**. Attribution étatique nécessite calibration prudente (cf Ch.18). Rarement « certain » sans accès renseignement classifié.

### 29.8 Limites

**Attribution civile impossible**. L’identification des opérateurs individuels au sein de Lazarus est réservée aux services de renseignement. OSINT identifie les **clusters** et **patterns**, pas les **individus**.

**Coopération minimale avec juridictions sanctuaires**. DPRK, Russie, Iran ne coopèrent pas. Action via points externes (exchanges, services, transit).

**Récupération limitée**. Quelques cas (Bitfinex saisie 3,6 Mrd, autres opérations FBI), mais dans l’ensemble, fonds Lazarus difficiles à récupérer.

### 29.9 Tendances 2024-2026

**Lazarus en croissance**. Vols cumulés en milliards USD/an.

**Sophistication croissante**. Usage de tous les outils d’obfuscation (mixers post-Tornado, bridges, privacy coins, réseaux de mules complexes).

**Coopération internationale renforcée**. Mais lente et fragmentée.

**Sanctions ciblées** : OFAC continue d’ajouter wallets et entités. UE suit progressivement.

**Pour l’analyste** : les acteurs étatiques sont **angle stratégique** pour les services de renseignement et CTI privé senior. Pour l’analyste défensif d’organisation, les détecter dans son périmètre = **alerte rouge** justifiant escalade immédiate (ANSSI, DGSI selon contexte).

-----
