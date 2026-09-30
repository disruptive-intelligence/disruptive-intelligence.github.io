---
title: OSINT & cryptoactifs
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
format: cours
revue: '2026-05-10'
---

*Adresse → Transaction → Entité → Flux → Cashout → Attribution prudente → Rapport*

**Cours complet — 50 chapitres, 9 parties, 10 annexes, parcours express d’ouverture.**

-----

## Avant-propos

Ce cours apprend à **investiguer les crypto-actifs** dans une posture professionnelle. Il s’adresse aux analystes CTI, investigateurs financiers, RSSI, équipes IR, professionnels de la conformité (AML/CFT), et services de renseignement. Il est conçu pour être **auto-suffisant** — un lecteur qui part de zéro, travaille le cours dans l’ordre, et fait les exercices proposés, acquiert un niveau professionnel d’enquête crypto-forensique.

**Ce que ce cours fait** : il vous apprend à lire les blockchains majeures (Bitcoin, Ethereum, TRON, Solana), à construire un raisonnement d’enquête depuis un indice (adresse, transaction hash, ransom note) jusqu’à un rapport actionnable, à utiliser les outils gratuits et professionnels (Chainalysis, TRM, Elliptic) avec discernement, à comprendre les techniques d’obfuscation (mixers, bridges, privacy coins) et leurs limites, à investiguer les grandes typologies d’abus (pig butchering, ransomware, hacks DeFi, NFT scams), et à coopérer avec VASP et autorités. Il intègre le cadre français/UE (TRACFIN, MiCA, Travel Rule, sanctions OFAC).

**Ce que ce cours ne fait pas** : il ne vous apprend pas à blanchir ou contourner la traçabilité. Il ne fournit pas de guide de cashout. Il ne promet pas l’attribution magique d’une adresse à une personne — il vous apprend à **calibrer** ce que les données publiques permettent de dire, ce qu’elles suggèrent, et ce qu’elles ne permettent pas de conclure.

**Posture pédagogique** : factuelle, calibrée, vérifiable. Chaque affirmation forte renvoie à une source publique (rapport vendor, document FATF, jurisprudence, advisory officiel). Les ordres de grandeur sont donnés avec leurs limites. Les analyses sont honnêtes sur l’incertitude.

**Continuité avec la bibliothèque** : ce cours s’articule avec **Dark Web — Comprendre, Naviguer, Investiguer** (le dark web est l’écosystème où les flux crypto illicites s’organisent), **AU CŒUR DES APT** (Lazarus et autres acteurs étatiques utilisant le crypto-laundering), **FININT — Investigation financière** (OSINT financier corporate, complémentaire à l’analyse on-chain), **Cartographie des écosystèmes cybercriminels** (contexte structurel), et **CTI** (production de renseignement actionnable). Les renvois explicites permettent d’approfondir sans dupliquer.

**Sur la séparation OSINT_Crypto / FININT** : ce cours traite l’**enquête crypto pure** (lecture blockchain, traçage on-chain, attribution probabiliste, cashout). FININT traite l’**OSINT financier classique** (registres, UBO, sanctions, structures corporate, SOCMINT financier). Beaucoup d’investigations réelles combinent les deux — les renvois inter-cours organisent cette complémentarité.

-----

## Parcours express — Lire une transaction crypto en 30 minutes

> Avant les chapitres experts, ce parcours express donne les bases minimales pour ne pas être perdu. Si vous lisez régulièrement des transactions blockchain, vous pouvez le sauter. Sinon, 30 minutes ici font gagner des heures plus loin.

### Étape 1 — Qu’est-ce qu’une adresse crypto ?

Une **adresse crypto** est une chaîne de caractères qui identifie un point de réception sur une blockchain. Trois exemples concrets :

- **Bitcoin** : `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh` (format SegWit, ~42 caractères) ou `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa` (format historique, ~34 caractères).
- **Ethereum** : `0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb1` (42 caractères, commence toujours par `0x`).
- **TRON** : `TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t` (34 caractères, commence par `T`).

**Ce qu’il faut comprendre** : une adresse est un **identifiant cryptographique** dérivé d’une clé privée. Qui contrôle la clé privée contrôle les fonds à l’adresse. **L’adresse n’est pas une personne** — c’est un endroit. Une même personne peut contrôler des milliers d’adresses ; une adresse peut être contrôlée par plusieurs personnes (multi-signature) ou par un service (exchange custodian).

### Étape 2 — Qu’est-ce qu’une transaction ?

Une **transaction** est un transfert d’actif (BTC, ETH, USDT…) d’une ou plusieurs adresses vers une ou plusieurs adresses, enregistré publiquement et **immutablement** dans la blockchain. Chaque transaction a un identifiant unique : le **TXID** (transaction hash).

Exemple Bitcoin TXID : `e3a5f9a8c1b2d4e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0` (64 caractères hexadécimaux).

Une transaction est **horodatée** (timestamp), incluse dans un **bloc** (groupé avec d’autres transactions), et propagée à tous les nœuds du réseau. Une fois confirmée (typiquement 6 confirmations pour Bitcoin, ~1h ; quelques secondes à minutes pour les blockchains plus rapides), elle est irréversible.

### Étape 3 — Comment lire un explorateur blockchain ?

Un **explorateur blockchain** (block explorer) est un site web qui affiche les transactions et adresses d’une blockchain de manière humainement lisible. Les principaux :

- **Bitcoin** : mempool.space, blockstream.info, blockchair.com.
- **Ethereum** : etherscan.io.
- **TRON** : tronscan.org.
- **Multi-chain** : blockchair.com.

Quand vous chargez l’adresse `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh` sur mempool.space, vous voyez :

- Le **solde** actuel (combien de BTC à cette adresse).
- L’**historique des transactions** : entrées (reçues) et sorties (envoyées).
- La **première transaction** (date de création de l’adresse en activité).
- La **dernière transaction**.

C’est gratuit, public, et la base de toute enquête crypto.

### Étape 4 — Comment identifier l’actif transféré ?

Une transaction peut transférer :

- **Le coin natif** de la blockchain : BTC sur Bitcoin, ETH sur Ethereum, TRX sur TRON.
- **Un token** déployé sur cette blockchain : USDT, USDC, des milliers de tokens ERC-20 sur Ethereum, des tokens TRC-20 sur TRON.

**Sur Etherscan**, regardez :

- L’**onglet « Overview »** pour le solde ETH et l’activité native.
- L’**onglet « Token Holdings »** pour les tokens détenus.
- Les **« ERC-20 Token Txns »** pour l’historique des transferts de tokens.

Une erreur classique : voir « 0 ETH » sur une transaction et conclure qu’aucune valeur n’a été transférée. Souvent, la **valeur réelle** est dans un transfert de token (USDT par exemple), visible dans le détail mais pas dans le solde ETH.

### Étape 5 — Comment repérer un exchange, un smart contract, un bridge, un mixer ?

En cliquant sur une adresse dans Etherscan ou un autre explorateur, certaines sont **labellisées** :

- **Exchange** : `Binance Hot Wallet`, `Coinbase 1`, `Kraken Cold Storage`. Indique que l’adresse est contrôlée par un exchange.
- **Smart contract** : si l’adresse contient du code, l’explorateur l’indique avec onglet « Contract ».
- **Bridge** : `Wormhole Bridge`, `Multichain Bridge`. Permet le transfert cross-chain.
- **Mixer** : `Tornado Cash 1 ETH`, `Wasabi CoinJoin`. Service d’anonymisation.

Ces labels viennent de sources variées (annonces officielles, recherche communautaire, analyse vendor). Ils sont **utiles mais non infaillibles** — un label peut être obsolète, mal attribué, ou marketing.

### Étape 6 — Pourquoi adresse ≠ personne

C’est **le concept à intérioriser**.

Une adresse est un identifiant technique. Pour relier une adresse à une personne identifiable, il faut un **lien externe** : l’adresse a été utilisée pour s’inscrire sur un exchange KYC, l’adresse a été publiée par son propriétaire, l’adresse apparaît dans une plainte, etc.

Sans ce lien externe, l’enquête peut établir :

- Que l’adresse est **active** (transactions observables).
- Que l’adresse a **interagi** avec d’autres adresses (graphes de flux).
- Que l’adresse a **transité** par tel service (passages à des points labellisés).
- Que l’adresse fait **partie d’un cluster** (heuristiques de regroupement).

Mais elle ne peut pas, sur les seules données publiques, dire **qui contrôle** l’adresse. C’est la différence fondamentale entre **OSINT crypto** (analyse on-chain) et **investigation judiciaire** (qui peut, par réquisition, obtenir des données KYC d’un exchange).

### Étape 7 — Comment formuler une hypothèse d’enquête proprement

Au terme d’une analyse, on **n’écrit pas** : « Cette adresse appartient à X ».

On écrit (selon le niveau de preuve) :

- « Cette adresse a reçu un paiement de 0,5 BTC le [date] depuis [adresse source]. » → **fait observable**.
- « Cette adresse fait partie d’un cluster de 47 adresses présentant des heuristiques de co-spending. » → **observation analytique**.
- « Le cluster auquel appartient cette adresse a, à plusieurs reprises, déposé des fonds vers une adresse labellisée Binance Hot Wallet. » → **observation enrichie**.
- « Le pattern de flux suggère, avec un niveau de confiance modéré, une activité de collecte type pig butchering. » → **hypothèse calibrée**.
- « L’identification du titulaire effectif de l’adresse n’est pas possible sur les seules données publiques. Une réquisition auprès du VASP destinataire serait nécessaire. » → **limite explicite**.

Le **vocabulaire calibré** (Words of Estimative Probability — WEP) est la signature de l’analyste sérieux. Toute affirmation forte non démontrée détruit la crédibilité d’un rapport.

-----

Vous avez maintenant les bases pour aborder le cours. Le reste va vous apprendre à creuser chaque étape avec rigueur, méthode, et discernement.

-----

## Fil rouge : Opération MIXSHADOW

Pour ancrer la théorie dans la pratique, ce cours suit un cas fictif inspiré de cas réels. **Opération MIXSHADOW** déroule, chapitre après chapitre, l’investigation d’un paiement de rançon ransomware.

**Le contexte.** **Aurélien Médical** est un équipementier français de matériel hospitalier (700 collaborateurs, OIV santé, basé à Lyon). En mars 2026, son SI est compromis par le ransomware **Akira** (groupe RaaS actif depuis 2023). Production paralysée : machines de dialyse, scanners, pousse-seringues, dispositifs cardio-vasculaires — l’arrêt de la chaîne logicielle bloque les livraisons. Trois hôpitaux clients alertent sur des patients en attente de soins, dont des cas vitaux.

Sous pression vitale, et après concertation avec ANSSI, DGSI, ministère de la santé, et juridique, la direction d’Aurélien Médical décide de **payer la rançon**. 35 BTC (~2 M EUR au cours du moment) versés le 14 mars 2026 à l’adresse fournie par l’opérateur Akira via portail de négociation. La clé de déchiffrement est obtenue 6 heures plus tard. Reprise progressive de l’activité sur 3 semaines.

**Le mandat.** Aurélien Médical et la DGSI mandatent **Athéna Group** (cabinet CTI français, déjà acteur de DARKSTREAM) pour : **(1)** tracer les BTC payés depuis l’adresse de paiement initial ; **(2)** cartographier la chaîne de blanchiment ; **(3)** identifier les off-ramps potentiels et points de coopération ; **(4)** contribuer à l’attribution du groupe Akira (affilié individuel, équipe régionale, lien avec d’autres opérations) ; **(5)** coopérer avec TRACFIN, DGSI, et leurs homologues internationaux (FBI Cyber Division, BKA allemand, Europol EC3).

**L’analyste.** **Sarah Marin**, analyste crypto-forensique senior chez Athéna Group. 6 ans d’expérience dont 3 ans à TRACFIN comme analyste financière, transition vers le privé en 2023. Certifiée Chainalysis Reactor (CRC), TRM Labs Investigations, formation Elliptic. Background master Finance + master Cybersécurité. Collègue de **Lucas Ferreira** (DARKSTREAM) chez Athéna — ils collaborent occasionnellement sur des dossiers transverses.

**La méthode.** Sarah applique la doctrine Athéna : OPSEC stricte, outils combinés (Chainalysis Reactor pour l’investigation principale, TRM Labs en validation croisée, OXT et explorateurs publics pour la documentation reproductible), workflow méthodologique reproductible, calibration WEP systématique, livrables structurés.

**Le bilan attendu.** Sarah travaillera 8 semaines sur le dossier. Le bilan honnête, à la fin, sera : récupération **partielle** (quelques pourcents), attribution **probable** (pas certaine), apport **significatif** à un dossier multi-juridictionnel en cours, contribution à la **CTI** sectorielle santé. Pas de happy ending hollywoodien — la réalité du métier.

Les épisodes MIXSHADOW jalonnent le cours aux moments où le concept enseigné éclaire la progression de Sarah.

-----

## Sommaire

- [Partie I — Comprendre L’écosystème crypto SANS fantasme](01-partie-i-comprendre-lecosysteme-crypto-sans-fantas/index.md)
    - [Chapitre 1 — Pourquoi l’OSINT crypto est devenu central](01-partie-i-comprendre-lecosysteme-crypto-sans-fantas/01-chapitre-1-pourquoi-losint-crypto-est-devenu-centr.md)
    - [Chapitre 2 — Ce que l’enquête crypto permet vraiment (et ne permet pas)](01-partie-i-comprendre-lecosysteme-crypto-sans-fantas/02-chapitre-2-ce-que-lenquete-crypto-permet-vraiment.md)
    - [Chapitre 3 — Lexique opérationnel des crypto-actifs](01-partie-i-comprendre-lecosysteme-crypto-sans-fantas/03-chapitre-3-lexique-operationnel-des-crypto-actifs.md)
    - [Chapitre 4 — Les grandes familles de blockchains](01-partie-i-comprendre-lecosysteme-crypto-sans-fantas/04-chapitre-4-les-grandes-familles-de-blockchains.md)
    - [Chapitre 5 — Le métier d’analyste crypto-forensique](01-partie-i-comprendre-lecosysteme-crypto-sans-fantas/05-chapitre-5-le-metier-danalyste-crypto-forensique.md)
- [Partie II — Lire les blockchains](02-partie-ii-lire-les-blockchains/index.md)
    - [Chapitre 6 — Lire une transaction Bitcoin](02-partie-ii-lire-les-blockchains/01-chapitre-6-lire-une-transaction-bitcoin.md)
    - [Chapitre 7 — Le modèle UTXO en profondeur](02-partie-ii-lire-les-blockchains/02-chapitre-7-le-modele-utxo-en-profondeur.md)
    - [Chapitre 8 — Lire une transaction Ethereum](02-partie-ii-lire-les-blockchains/03-chapitre-8-lire-une-transaction-ethereum.md)
    - [Chapitre 9 — Tokens et smart contracts](02-partie-ii-lire-les-blockchains/04-chapitre-9-tokens-et-smart-contracts.md)
    - [Chapitre 10 — Stablecoins : USDT, USDC et le rôle opérationnel](02-partie-ii-lire-les-blockchains/05-chapitre-10-stablecoins-usdt-usdc-et-le-role-opera.md)
    - [Chapitre 11 — Explorateurs blockchain : méthodologie de lecture](02-partie-ii-lire-les-blockchains/06-chapitre-11-explorateurs-blockchain-methodologie-d.md)
- [Partie III — Méthodologie d’enquête](03-partie-iii-methodologie-denquete/index.md)
    - [Chapitre 12 — Construire une fiche d’adresse](03-partie-iii-methodologie-denquete/01-chapitre-12-construire-une-fiche-dadresse.md)
    - [Chapitre 13 — Point de départ d’une enquête : typologie d’indices](03-partie-iii-methodologie-denquete/02-chapitre-13-point-de-depart-dune-enquete-typologie.md)
    - [Chapitre 14 — De l’indice au graphe : chaîne de raisonnement](03-partie-iii-methodologie-denquete/03-chapitre-14-de-lindice-au-graphe-chaine-de-raisonn.md)
    - [Chapitre 15 — Construire un graphe de flux lisible](03-partie-iii-methodologie-denquete/04-chapitre-15-construire-un-graphe-de-flux-lisible.md)
    - [Chapitre 16 — Temporalité et chronologie d’enquête](03-partie-iii-methodologie-denquete/05-chapitre-16-temporalite-et-chronologie-denquete.md)
    - [Chapitre 17 — Clustering : heuristiques, promesses et limites](03-partie-iii-methodologie-denquete/06-chapitre-17-clustering-heuristiques-promesses-et-l.md)
    - [Chapitre 18 — Attribution : adresse → service → personne](03-partie-iii-methodologie-denquete/07-chapitre-18-attribution-adresse-service-personne.md)
- [Partie IV — Outils ET workflow](04-partie-iv-outils-et-workflow/index.md)
    - [Chapitre 19 — Outils gratuits et explorateurs avancés](04-partie-iv-outils-et-workflow/01-chapitre-19-outils-gratuits-et-explorateurs-avance.md)
    - [Chapitre 20 — Outils professionnels : Chainalysis, TRM Labs, Elliptic](04-partie-iv-outils-et-workflow/02-chapitre-20-outils-professionnels-chainalysis-trm.md)
    - [Chapitre 21 — Outils de visualisation](04-partie-iv-outils-et-workflow/03-chapitre-21-outils-de-visualisation.md)
    - [Chapitre 22 — Labels publics et qualification des sources](04-partie-iv-outils-et-workflow/04-chapitre-22-labels-publics-et-qualification-des-so.md)
    - [Chapitre 23 — Collecte, conservation et chaîne de preuve crypto](04-partie-iv-outils-et-workflow/05-chapitre-23-collecte-conservation-et-chaine-de-pre.md)
    - [Chapitre 24 — Workflow complet d’une enquête crypto](04-partie-iv-outils-et-workflow/06-chapitre-24-workflow-complet-dune-enquete-crypto.md)
- [Partie V — Typologies d’abus crypto](05-partie-v-typologies-dabus-crypto/index.md)
    - [Chapitre 25 — Scams retail : romance scam et pig butchering](05-partie-v-typologies-dabus-crypto/01-chapitre-25-scams-retail-romance-scam-et-pig-butch.md)
    - [Chapitre 26 — Ransomware et extorsion](05-partie-v-typologies-dabus-crypto/02-chapitre-26-ransomware-et-extorsion.md)
    - [Chapitre 27 — Hacks DeFi et compromission de wallets](05-partie-v-typologies-dabus-crypto/03-chapitre-27-hacks-defi-et-compromission-de-wallets.md)
    - [Chapitre 28 — Fraudes NFT, tokens frauduleux et rug pulls](05-partie-v-typologies-dabus-crypto/04-chapitre-28-fraudes-nft-tokens-frauduleux-et-rug-p.md)
    - [Chapitre 29 — Acteurs étatiques](05-partie-v-typologies-dabus-crypto/05-chapitre-29-acteurs-etatiques.md)
- [Partie VI — Obfuscation, laundering ET cashout](06-partie-vi-obfuscation-laundering-et-cashout/index.md)
    - [Chapitre 30 — Le cashout : où l’on quitte l’on-chain](06-partie-vi-obfuscation-laundering-et-cashout/01-chapitre-30-le-cashout-ou-lon-quitte-lon-chain.md)
    - [Chapitre 31 — Mixers et tumblers](06-partie-vi-obfuscation-laundering-et-cashout/02-chapitre-31-mixers-et-tumblers.md)
    - [Chapitre 32 — CoinJoin : Wasabi, Samourai](06-partie-vi-obfuscation-laundering-et-cashout/03-chapitre-32-coinjoin-wasabi-samourai.md)
    - [Chapitre 33 — Bridges et cross-chain laundering](06-partie-vi-obfuscation-laundering-et-cashout/04-chapitre-33-bridges-et-cross-chain-laundering.md)
    - [Chapitre 34 — DEX, swaps et obfuscation DeFi](06-partie-vi-obfuscation-laundering-et-cashout/05-chapitre-34-dex-swaps-et-obfuscation-defi.md)
    - [Chapitre 35 — Privacy coins : Monero, Zcash, limites radicales](06-partie-vi-obfuscation-laundering-et-cashout/06-chapitre-35-privacy-coins-monero-zcash-limites-rad.md)
- [Partie VII — Cas pratiques déroulés](07-partie-vii-cas-pratiques-deroules/index.md)
    - [Chapitre 36 — Cas 1 : victime de pig butchering USDT Tron](07-partie-vii-cas-pratiques-deroules/01-chapitre-36-cas-1-victime-de-pig-butchering-usdt-t.md)
    - [Chapitre 37 — Cas 2 : paiement ransomware BTC à un affilié RaaS](07-partie-vii-cas-pratiques-deroules/02-chapitre-37-cas-2-paiement-ransomware-btc-a-un-aff.md)
    - [Chapitre 38 — Cas 3 : wallet drain Ethereum par approval phishing](07-partie-vii-cas-pratiques-deroules/03-chapitre-38-cas-3-wallet-drain-ethereum-par-approv.md)
    - [Chapitre 39 — Cas 4 : flux multi-chaînes avec bridge et stablecoins](07-partie-vii-cas-pratiques-deroules/04-chapitre-39-cas-4-flux-multi-chaines-avec-bridge-e.md)
    - [Chapitre 40 — Cas 5](07-partie-vii-cas-pratiques-deroules/05-chapitre-40-cas-5.md)
- [Partie VIII — Cas historiques emblématiques](08-partie-viii-cas-historiques-emblematiques/index.md)
    - [Chapitre 41 — Bitfinex 2016 → saisie 3,6 Mrd USD 2022](08-partie-viii-cas-historiques-emblematiques/01-chapitre-41-bitfinex-2016-saisie-3-6-mrd-usd-2022.md)
    - [Chapitre 42 — Colonial Pipeline 2021 — récupération FBI](08-partie-viii-cas-historiques-emblematiques/02-chapitre-42-colonial-pipeline-2021-recuperation-fb.md)
    - [Chapitre 43 — Ronin / Lazarus 2022 — 625 M USD](08-partie-viii-cas-historiques-emblematiques/03-chapitre-43-ronin-lazarus-2022-625-m-usd.md)
    - [Chapitre 44 — Tornado Cash — sanctions OFAC et procès](08-partie-viii-cas-historiques-emblematiques/04-chapitre-44-tornado-cash-sanctions-ofac-et-proces.md)
    - [Chapitre 45 — Synthèse MIXSHADOW](08-partie-viii-cas-historiques-emblematiques/05-chapitre-45-synthese-mixshadow.md)
- [Partie IX — Production, cadre ET professionnalisation](09-partie-ix-production-cadre-et-professionnalisation/index.md)
    - [Chapitre 46 — Produire un rapport OSINT crypto](09-partie-ix-production-cadre-et-professionnalisation/01-chapitre-46-produire-un-rapport-osint-crypto.md)
    - [Chapitre 47 — Échelle de confiance et formulation analytique](09-partie-ix-production-cadre-et-professionnalisation/02-chapitre-47-echelle-de-confiance-et-formulation-an.md)
    - [Chapitre 48 — Coopération avec VASP, autorités et compliance](09-partie-ix-production-cadre-et-professionnalisation/03-chapitre-48-cooperation-avec-vasp-autorites-et-com.md)
    - [Chapitre 49 — Éthique, légalité et sécurité de l’enquêteur](09-partie-ix-production-cadre-et-professionnalisation/04-chapitre-49-ethique-legalite-et-securite-de-lenque.md)
    - [Chapitre 50 — Maturité analyste et programme de surveillance crypto durable](09-partie-ix-production-cadre-et-professionnalisation/05-chapitre-50-maturite-analyste-et-programme-de-surv.md)
- [Annexes](10-annexes/index.md)
    - [Annexe A — Glossaire opérationnel crypto](10-annexes/01-annexe-a-glossaire-operationnel-crypto.md)
    - [Annexe B — Modèle de fiche adresse](10-annexes/02-annexe-b-modele-de-fiche-adresse.md)
    - [Annexe C — Modèle de fiche transaction](10-annexes/03-annexe-c-modele-de-fiche-transaction.md)
    - [Annexe D — Modèle de timeline d’enquête](10-annexes/04-annexe-d-modele-de-timeline-denquete.md)
    - [Annexe E — Matrice des signaux d’alerte](10-annexes/05-annexe-e-matrice-des-signaux-dalerte.md)
    - [Annexe F — Matrice « ce que je peux conclure / ce que je ne peux pas conclure »](10-annexes/06-annexe-f-matrice-ce-que-je-peux-conclure-ce-que-je.md)
    - [Annexe G — Outils par usage (catalogue raisonné)](10-annexes/07-annexe-g-outils-par-usage-catalogue-raisonne.md)
    - [Annexe H — Modèle de rapport OSINT crypto](10-annexes/08-annexe-h-modele-de-rapport-osint-crypto.md)
    - [Annexe I — Erreurs fréquentes d’analyse](10-annexes/09-annexe-i-erreurs-frequentes-danalyse.md)
    - [Annexe J — 5 mini-cas synthétiques d’entraînement](10-annexes/10-annexe-j-5-mini-cas-synthetiques-dentrainement.md)
