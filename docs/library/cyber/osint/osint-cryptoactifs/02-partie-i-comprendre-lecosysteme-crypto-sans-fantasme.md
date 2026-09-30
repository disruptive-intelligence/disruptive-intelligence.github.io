---
title: PARTIE I — COMPRENDRE L’ÉCOSYSTÈME CRYPTO SANS FANTASME
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
chapter: 2
chapters: 10
---

> **Ce que cette partie apprend.** Situer les crypto-actifs dans leur réalité économique et criminologique. Comprendre pourquoi ils sont devenus centraux dans les enquêtes financières contemporaines, ce que l’enquête crypto permet réellement (et ne permet pas), maîtriser le lexique opérationnel, distinguer les grandes familles de blockchains, et adopter la posture professionnelle d’analyste crypto-forensique.
> 
> **Ce qu’elle ne couvre pas.** Les techniques de lecture détaillée des blockchains (Partie II), les méthodes d’enquête (Partie III), les outils précis (Partie IV).
> 
> **Ce que vous saurez faire après cette partie.** Expliquer à un non-spécialiste pourquoi le crypto est traçable mais pas anonyme, présenter les limites honnêtes de l’OSINT crypto, manier le vocabulaire opérationnel, et différencier Bitcoin, Ethereum, TRON, Solana dans leur logique d’enquête.

-----

## Chapitre 1 — Pourquoi l’OSINT crypto est devenu central

Les crypto-actifs ne sont plus une curiosité technique réservée aux passionnés. En 2026, ils sont **infrastructure de transfert de valeur** pour des pans entiers de la cybercriminalité, de la fraude retail, du contournement de sanctions, et plus marginalement de l’économie légitime. L’analyste financier ou cyber qui ne sait pas lire une transaction blockchain est aujourd’hui handicapé sur une part croissante de ses dossiers.

### 1.1 Le crypto comme infrastructure de transfert de valeur

Les blockchains publiques offrent une fonctionnalité que les systèmes bancaires traditionnels n’ont jamais su offrir aussi simplement : **transférer de la valeur de pair à pair, sans intermédiaire de confiance, à travers les frontières, en quelques minutes**. Cette propriété, neutre par construction, sert :

- L’**économie légitime** : remittances internationales (envois d’argent par les diasporas), paiements B2B cross-border, marchés DeFi régulés, achats institutionnels (entreprises listées détenant du Bitcoin en trésorerie).
- L’**économie grise** : contournement de contrôles des changes (Chine, Argentine, Liban, Nigeria), utilisation par des entrepreneurs dans des juridictions à banking dysfonctionnel.
- L’**économie criminelle** : ransomware, fraudes retail (pig butchering, Ponzi crypto), darknet markets, contournement de sanctions internationales (Russie post-2022, Corée du Nord), blanchiment d’argent.

Pour l’analyste, comprendre que le crypto est **infrastructure neutre** — pas intrinsèquement criminelle — est important. La même blockchain qui transporte une rançon ransomware transporte aussi le salaire d’un développeur ukrainien payé par une entreprise européenne. La distinction est dans **l’usage**, pas dans l’outil.

### 1.2 Pourquoi les criminels utilisent le crypto

Plusieurs propriétés rendent les crypto-actifs attractifs pour la criminalité.

**Pseudonymat**. Les adresses ne sont pas directement reliées à l’identité civile. Pour un criminel ne maîtrisant pas l’OPSEC, c’est une protection apparente.

**Globalité**. Une transaction crypto traverse les frontières instantanément, sans contrôle bancaire intermédiaire. Pratique pour les transactions internationales criminelles.

**Irréversibilité**. Une transaction confirmée ne peut pas être annulée par chargeback (contrairement aux cartes bancaires). Pour le ransomware, c’est essentiel — la victime ne peut pas « rappeler » la rançon.

**Liquidité globale**. Les marchés crypto fonctionnent 24/7, dans toutes les juridictions, avec des centaines d’exchanges. La conversion en monnaie utilisable est, en principe, possible partout.

**Absence d’intermédiaire centralisé** (pour les blockchains publiques). Pas de banque à convaincre, pas de régulateur à contourner — du moins en théorie.

**Mais ces avantages criminels sont contrebalancés par une faiblesse structurelle** : la **traçabilité publique**. Sur une blockchain comme Bitcoin ou Ethereum, **toutes les transactions sont visibles à jamais**. C’est une différence fondamentale avec le cash (anonyme et sans trace) ou même le système bancaire (où les transactions sont privées sauf réquisition légale). Le criminel crypto laisse une trace **publique, permanente, analysable**. C’est l’opportunité que l’OSINT crypto exploite.

### 1.3 La transparence partielle des blockchains

Les blockchains publiques sont **transparentes**. Toute transaction est visible :

- Quelle adresse a envoyé combien à quelle adresse.
- Quand (timestamp précis).
- Quel actif (BTC, ETH, USDT, etc.).
- Avec quels frais.

Cette transparence est **publique** : pas besoin d’être bank, pas besoin de réquisition, pas besoin de mandat. N’importe qui avec un explorateur peut lire les transactions de n’importe quelle adresse, à tout moment, depuis le bloc genesis.

**Mais transparence ≠ identité**. Voir qu’une adresse a reçu 10 BTC ne dit pas qui contrôle cette adresse. C’est ici qu’intervient le travail d’enquête : relier les adresses observées à des **entités** (services, individus, groupes) via des labels publics, des heuristiques de clustering, et des recoupements OSINT off-chain.

### 1.4 Pseudonymat vs anonymat — la nuance fondamentale

**Pseudonymat** : les transactions sont publiques mais associées à des pseudonymes (adresses) qui ne révèlent pas directement l’identité. Bitcoin et Ethereum sont pseudonymes. Une fois le pseudonyme relié à une identité (KYC d’exchange, publication volontaire, erreur OPSEC), **l’historique entier devient attribuable**.

**Anonymat** : les transactions ne révèlent ni les parties ni les montants. Monero, Zcash (mode shielded). Casser cet anonymat nécessite des moyens cryptographiques avancés ou des erreurs spécifiques de l’utilisateur.

Cette distinction est **structurante** pour l’analyste :

- Sur **Bitcoin / Ethereum / TRON / Solana / la plupart des blockchains** : l’enquête est faisable, parfois fastidieuse mais méthodologiquement claire.
- Sur **Monero** : l’enquête on-chain est largement bloquée. Le travail se déplace vers les **points off-chain** (exchanges, OPSEC errors, infrastructure).

### 1.5 « Tout est public » ne veut pas dire « tout est attribuable »

Erreur répandue, y compris chez certains journalistes : confondre la **lisibilité publique** des transactions avec la **possibilité d’attribuer** chaque adresse à une personne.

La réalité :

- **~10-20%** des adresses Bitcoin actives sont labellisées (services connus, exchanges, mixers, sanctioned entities). Source : observations Chainalysis et autres vendors.
- **~80-90%** restent **unlabelled** — appartenant à des entités non identifiées (utilisateurs particuliers, services obscurs, criminels n’ayant jamais interagi avec un service KYC).
- Les **clusters** regroupent des adresses appartenant probablement à une même entité, mais l’identification de cette entité reste ouverte sans données off-chain.

Pour le criminel sophistiqué qui n’utilise jamais un exchange KYC, dont les wallets sont créés avec OPSEC stricte, et dont les flux passent par mixers et privacy coins, **l’attribution complète peut être impossible** sur les seules données publiques.

### 1.6 Place de l’OSINT crypto dans l’écosystème professionnel

L’OSINT crypto s’intègre dans plusieurs métiers :

**CTI (Cyber Threat Intelligence)**. Suivi de wallets de groupes ransomware, IAB, opérateurs malware. Identification de patterns de paiement. Alimentation de threat intel actionnable.

**SOC et IR**. Validation de paiements de rançon, traçage post-incident, identification de wallets compromis. Coordination avec les enquêteurs financiers.

**Forensique**. Capture et analyse de preuves crypto dans le cadre d’investigations. Documentation pour procédures judiciaires.

**Lutte anti-fraude**. Investigation de scams retail (pig butchering, faux investissements), détection de patterns de blanchiment.

**Conformité (AML/CFT)**. Screening de transactions, surveillance de clientèle, déclarations TRACFIN, application des sanctions OFAC/UE.

**Enquête judiciaire**. Soutien technique aux enquêteurs financiers et magistrats. Production de pièces à conviction. Coopération internationale via réquisitions.

**Enquête patrimoniale**. Identification d’avoirs crypto dans le cadre de successions, divorces, recouvrement de créances.

**Renseignement**. Suivi des flux financiers liés à des acteurs étatiques sanctionnés, organisations terroristes, prolifération.

Pour chacun de ces métiers, l’OSINT crypto est un **outil** parmi d’autres, à intégrer dans une démarche plus large. Rare est le dossier qui se résout uniquement par analyse on-chain — le crypto **complète** l’OSINT classique, le SIGINT, le HUMINT, la coopération institutionnelle.

### 1.7 L’évolution 2020-2026

L’écosystème crypto et son investigation ont profondément évolué.

**Maturation des outils**. Chainalysis (fondé 2014), TRM Labs (2018), Elliptic (2013) ont structuré une industrie de la blockchain intelligence. Capacités de clustering, labellisation, scoring de risque, intégration AML — tout cela était embryonnaire en 2017, mature en 2026.

**Saisies massives**. La saisie Bitfinex (3,6 Mrd USD en 2022, Ch.41), Colonial Pipeline (2,3 M USD récupérés, Ch.42), opérations contre mixers (Helix, Bitcoin Fog, Chipmixer, Tornado Cash, Samourai) montrent que **le traçage fonctionne** — quand les ressources et la coopération internationale s’alignent.

**Diversification des typologies**. Le ransomware reste dominant en volume médiatique, mais le **pig butchering** est devenu un fléau retail en explosion (estimations Chainalysis 2024-2025 : plusieurs milliards USD/an), les **hacks DeFi** alimentent des vols récurrents, les **acteurs étatiques** (Lazarus en tête) mobilisent des techniques de plus en plus sophistiquées.

**Essor des stablecoins**. USDT et USDC sont devenus la **monnaie de transaction** de pans entiers de l’écosystème, légitime comme illicite. Le FATF souligne en 2024-2025 que les stablecoins représentent une part majeure des volumes on-chain et une fraction significative des flux illicites observables. TRON est devenu la blockchain dominante pour les flux USDT illicites en volume.

**Pression réglementaire**. MiCA en UE (entrée en vigueur 2024), Travel Rule étendue, sanctions OFAC ciblant des entités crypto (Tornado Cash août 2022, Garantex, Suex, Bitzlato), durcissement KYC sur les exchanges centralisés. L’écosystème devient progressivement **moins anonyme** par couche réglementaire.

**Intégration IA**. Les outils de blockchain intelligence intègrent du ML pour détection de patterns, automatisation d’attribution, scoring de risque. Côté criminel, l’IA assiste la création de faux profils (pig butchering automatisé), le contournement de KYC.

### 1.8 Fil rouge — MIXSHADOW : la sollicitation

> **🔗 MIXSHADOW — Épisode 1 : le mandat**
> 
> Lundi 16 mars 2026. Sarah Marin reçoit le brief de mission. Réunion de cadrage en visio avec :
> 
> - Le **RSSI d’Aurélien Médical**, qui a piloté la cellule de crise depuis le 8 mars (date de chiffrement).
> - Deux **interlocuteurs DGSI** (officier traitant + spécialiste cyber).
> - Un **représentant TRACFIN** (cellule cyber).
> - Le **directeur d’Athéna Group**.
> 
> Le RSSI présente les faits. Compromission Akira datée du 8 mars vers 03h47 (chiffrement effectif). Vecteur d’entrée : compromission d’un compte VPN administrateur via stealer log acquis sur Russian Market (forensics Mandiant). Demande de rançon initiale : 80 BTC (~4,5 M EUR). Négociation via portail Tor descend à 35 BTC (~2 M EUR). Paiement effectué le 14 mars à 09h12. Décryption key reçue à 15h28 le même jour. Reprise opérationnelle progressive sur 3 semaines.
> 
> La DGSI précise le cadre : Athéna travaille sous mandat client (Aurélien Médical) avec **coopération étroite** mais non exclusive avec la DGSI. Remontée bi-hebdomadaire. Pas d’engagement public, TLP RED jusqu’à autorisation contraire. Coordination prévue avec Europol EC3 (le groupe Akira étant suivi par plusieurs services européens). FBI Cyber Division en partenaire potentiel via la DGSI (les US ont également des victimes Akira documentées).
> 
> Le mandat Athéna : tracer, cartographier, identifier les off-ramps, contribuer à l’attribution, coopérer.
> 
> Sarah note : objectif réaliste. Pas de promesse de récupération. La mission est de **maximiser la valeur de renseignement** extraite des 35 BTC payés, et d’alimenter des dossiers en cours qui dépassent largement le cas Aurélien Médical isolé.
> 
> Première action : préparer son environnement d’investigation et démarrer le traçage. Ch.5 détaillera l’OPSEC ; Ch.6 l’environnement ; Ch.13 le démarrage formel.

-----

## Chapitre 2 — Ce que l’enquête crypto permet vraiment (et ne permet pas)

Avant de plonger dans les techniques, il est essentiel de **calibrer les attentes**. Un mandat client mal cadré ou un management qui croit que « le crypto est traçable, donc tout se résout » conduit à des frustrations et des rapports inadaptés.

### 2.1 Ce que l’enquête crypto permet

**Suivre des flux publics**. L’analyste peut, sur Bitcoin/Ethereum/etc., suivre les mouvements depuis une adresse de départ jusqu’à la dispersion finale ou la rupture de visibilité (mixer, privacy coin, off-ramp non coopératif). Cette traçabilité est gratuite, publique, vérifiable.

**Identifier des points de contact avec des services connus**. Quand les fonds passent par un exchange labellisé, un mixer connu, un bridge identifié — l’analyse capture ces points. Ils servent d’**ancrage** pour la suite (réquisition, coopération exchange, qualification de risque).

**Repérer des patterns**. Récurrence dans les flux, montants typiques, fenêtres temporelles, structures de wallets. Patterns qui aident à identifier la **typologie** d’activité (pig butchering, ransomware, fraude, etc.).

**Documenter un chemin de fonds**. Reconstituer, pas à pas, la trajectoire d’une somme entre l’adresse de départ et un point d’aboutissement (ou d’opacité). Cette documentation est un **livrable** essentiel — pour la victime, le procureur, l’autorité, ou la communauté CTI.

**Produire des hypothèses calibrées**. À partir des observations, formuler des hypothèses sur la nature de l’activité, les acteurs probables, les juridictions impliquées, les moyens de coopération.

**Appuyer un signalement ou une plainte**. Un rapport OSINT crypto solide permet à la victime de déposer plainte avec éléments tangibles, à TRACFIN de qualifier un signalement de soupçon, à un magistrat de fonder une commission rogatoire internationale, à une autorité de geler des fonds via émetteur stablecoin coopératif.

**Soutenir une saisie**. Quand la coopération internationale s’aligne, l’enquête OSINT prépare les éléments techniques permettant aux forces de l’ordre d’opérer une saisie effective (cf cas Bitfinex, Colonial Pipeline, Ch.41-42).

### 2.2 Ce que l’enquête crypto ne permet pas

**Identifier directement une personne à partir d’une adresse**. Sauf cas particulier (publication volontaire, mismatch OPSEC évident, données KYC obtenues via réquisition), l’OSINT crypto pure ne donne pas l’identité civile. Le mandat « identifie qui possède cette adresse » est un mandat **mal posé**.

**Récupérer des fonds dispersés sans intervention extérieure**. L’analyste documente le chemin ; la récupération nécessite une action **off-chain** (gel par émetteur stablecoin, saisie par autorité, coopération exchange). Sans cette action, les fonds restent où ils sont.

**Casser le chiffrement Monero**. Sauf cas spécifiques (vulnérabilités d’implémentation, decoy patterns exploitables), Monero reste opaque. L’enquête se déplace vers d’autres angles.

**Démixer avec certitude un mixer custodial**. Un mixer comme Tornado Cash mélange les fonds de centaines d’utilisateurs. Reconstituer **avec certitude** les paires entrée/sortie est dans la plupart des cas impossible — sauf erreurs spécifiques (montants atypiques, timings exploitables, patterns d’usage).

**Garantir la traçabilité cross-chain sans outil professionnel**. Les bridges complexifient considérablement le suivi. Un fonds qui passe d’Ethereum à BNB Chain via plusieurs bridges, swaps DEX, et conversions stablecoin peut devenir difficile à suivre avec les seuls outils gratuits.

**Obtenir des données KYC d’exchanges**. Réservé aux autorités via réquisition légale. L’analyste OSINT prépare la cible (« cette adresse est probablement un exchange deposit address de [exchange X] »), l’autorité opère la requête.

**Produire une attribution judiciairement opposable sans corroboration**. Un rapport OSINT seul, même excellent, ne suffit généralement pas à condamner devant un tribunal. Il sert à **orienter** une enquête, pas à la conclure judiciairement.

### 2.3 Les zones grises

Entre le « je peux » et le « je ne peux pas », plusieurs zones intermédiaires.

**Attribution probabiliste**. Avec recoupement de plusieurs signaux faibles (style d’usage, patterns temporels, infrastructure, mentions OSINT), on peut formuler une attribution **probable** (60-80% confiance). Utilisable opérationnellement, pas judiciairement.

**Identification d’une typologie d’activité**. Reconnaître qu’un cluster fait du pig butchering est généralement faisable (patterns de collection, tailles de transactions, flux vers exchanges). L’identification du **réseau précis** derrière est plus dure.

**Contribution à l’identification d’un VASP non coopératif**. Plusieurs investigations montrent qu’analyser les patterns d’un exchange permet d’identifier sa juridiction probable, ses banques partenaires, ses points faibles — utile pour pression réglementaire et coordination internationale.

**Détection de fraude en temps réel**. Avec des feeds adaptés, on peut alerter sur des transactions suspectes en cours (paiements vers des adresses sanctionnées, patterns de pump-and-dump). Capacité défensive valable, attribution post-hoc nécessaire.

### 2.4 Calibration des attentes du mandant

Un mandat client crypto bien cadré contient :

**Périmètre clair**. Quelles adresses, quels flux, quelle période. « Tracez tout » est un mandat creux.

**Objectifs réalistes**. « Documenter le chemin des fonds, identifier les points de contact avec des services, produire un rapport actionnable » plutôt que « identifier le criminel ».

**Livrables explicites**. Rapport, captures, IoC structurés, recommandations.

**Cadre coopératif**. Avec quelles autorités, quelle TLP, quelle politique de communication.

**Budget et délai**. Une investigation crypto sérieuse prend 2-12 semaines selon complexité. Pas 48h.

**Sortie attendue**. Que doit-il se passer après le rapport ? Plainte, signalement, gel d’actifs, communication interne, threat intel partagée ?

Sarah Marin, dans MIXSHADOW, opère sous mandat **bien cadré** : le DGSI et le client sont alignés sur des attentes réalistes — pas de promesse de récupération, pas d’attribution magique, valeur ajoutée par renseignement et coopération.

### 2.5 Le piège des promesses excessives

L’industrie de la blockchain intelligence est, à juste titre, en croissance. Mais elle peut aussi être tentée par le marketing excessif — promesses de « démixage parfait », « attribution garantie », « récupération assurée ». L’analyste sérieux résiste à ces promesses, autant pour préserver sa crédibilité que pour aligner les attentes du mandant sur la réalité opérationnelle.

Phrase à intérioriser : **« Je vais documenter tout ce que les données publiques permettent de dire. Je ne vais pas inventer ce qu’elles ne permettent pas de conclure. »** C’est la signature de l’analyste pro.

-----

## Chapitre 3 — Lexique opérationnel des crypto-actifs

Maîtriser le vocabulaire est la condition pour comprendre le reste du cours, mais aussi pour **communiquer crédiblement** avec ses interlocuteurs (autres analystes, autorités, exchanges, journalistes). Ce chapitre n’est pas un glossaire encyclopédique mais un panorama opérationnel des termes que l’analyste manipule quotidiennement.

### 3.1 Termes fondamentaux

**Blockchain**. Registre distribué de transactions, validé cryptographiquement, partagé entre les nœuds d’un réseau. Bitcoin (depuis 2009), Ethereum (depuis 2015), TRON (depuis 2018), Solana (depuis 2020), des centaines d’autres. Chaque blockchain a ses règles propres (consensus, structure de transaction, capacités de smart contracts).

**Wallet**. Logiciel ou matériel qui stocke les clés privées et permet de signer des transactions. Distinction importante :

- **Wallet logiciel** : application sur ordinateur ou mobile (MetaMask, Phantom, Trust Wallet, Electrum).
- **Wallet matériel** : appareil dédié hors ligne (Ledger, Trezor) — plus sécurisé.
- **Wallet custodial** : géré par un tiers (exchange) qui détient les clés à votre place — Binance, Coinbase. **Vous ne contrôlez pas vraiment** les fonds.
- **Wallet non-custodial** : vous détenez les clés. « Not your keys, not your coins ».

**Adresse**. Identifiant public d’un point de réception sur une blockchain. Dérivée cryptographiquement d’une clé publique elle-même dérivée d’une clé privée. Voir Ch.3.4 pour les formats.

**Clé privée**. Secret cryptographique permettant de signer des transactions depuis une adresse. Connaissance de la clé privée = contrôle de l’adresse. Si une clé privée est compromise, les fonds peuvent être volés.

**Seed phrase / Mnemonic**. Suite de 12 ou 24 mots permettant de reconstituer une clé privée. Format standardisé (BIP-39). **Si quelqu’un obtient votre seed phrase, il prend le contrôle de tous les wallets qu’elle génère**. Utilisée pour récupération.

**Transaction (TX)**. Transfert d’actif entre adresses, signé cryptographiquement, propagé sur la blockchain.

**Transaction hash (TXID)**. Identifiant unique d’une transaction. Référence pour citer ou rechercher une transaction.

**Bloc**. Groupe de transactions agrégées et validées ensemble. Identifié par un numéro (block height) et un hash.

**Confirmations**. Nombre de blocs ajoutés depuis qu’une transaction a été incluse. Plus de confirmations = plus de finalité. Bitcoin : 6 confirmations standard (~1h). Ethereum post-Merge : finalité après ~12-15 minutes.

### 3.2 Termes économiques

**Coin natif**. L’actif intrinsèque d’une blockchain. BTC sur Bitcoin, ETH sur Ethereum, TRX sur TRON, SOL sur Solana, BNB sur BNB Chain.

**Token**. Actif déployé sur une blockchain via un smart contract (sans avoir sa propre blockchain). USDT, USDC, des dizaines de milliers d’autres. Distinction des standards :

- **ERC-20** sur Ethereum (et chaînes EVM-compatibles).
- **TRC-20** sur TRON.
- **BEP-20** sur BNB Chain.
- **SPL** sur Solana.

**Stablecoin**. Token dont la valeur est arrimée à une référence stable (généralement USD). USDT (Tether), USDC (Circle), DAI (MakerDAO). Détaillé Ch.10.

**NFT (Non-Fungible Token)**. Token unique non-divisible (contrairement aux fungibles type USDT). ERC-721 standard sur Ethereum. Représente collectibles, art numérique, droits, etc.

**Gas**. Frais de transaction sur Ethereum (et chaînes EVM). Mesuré en gwei (10^-9 ETH). Plus le réseau est congestionné, plus le gas coûte cher.

**Mining / Staking**. Mécanismes de validation des blocs. Bitcoin utilise Proof-of-Work (mining). Ethereum a basculé en Proof-of-Stake en septembre 2022 (The Merge). Implications pour l’analyste : peu directes, mais impact sur certaines heuristiques.

### 3.3 Termes d’enquête

**UTXO (Unspent Transaction Output)**. Modèle Bitcoin (et clones) où chaque transaction consomme des « pièces » (outputs précédents) et en génère de nouvelles. Détaillé Ch.7.

**Account model**. Modèle Ethereum (et chaînes EVM) où les adresses ont un solde directement (pas d’UTXO). Plus simple en surface, complexité différente en profondeur. Détaillé Ch.8.

**Clustering**. Regroupement d’adresses appartenant probablement à la même entité, basé sur des heuristiques (co-spending, change detection, etc.). Détaillé Ch.17.

**Attribution**. Association d’une adresse ou d’un cluster à une entité identifiable (exchange, mixer, individu, organisation). Niveaux de confiance variables. Détaillé Ch.18.

**Label**. Étiquette publique ou propriétaire associée à une adresse. Sources : annonces officielles, recherche communautaire, vendor commerciaux. Détaillé Ch.22.

**Heuristique**. Règle d’inférence non garantie, utilisée pour faire des hypothèses. Exemple : « si plusieurs inputs sont co-dépensés dans une même transaction, ils appartiennent probablement à la même entité ».

**Peeling chain**. Technique d’obfuscation Bitcoin où une grosse somme est progressivement « épluchée » en transferts successifs, chaque transaction laissant un petit montant à un destinataire et le reste à une nouvelle adresse de change. Détaillé Ch.7.

**Cluster**. Ensemble d’adresses regroupées comme appartenant probablement à la même entité.

**Cashout / Off-ramp**. Conversion de crypto en monnaie utilisable (fiat, biens, services). Le moment où l’on **quitte la blockchain**. Point critique d’enquête. Détaillé Ch.30.

### 3.4 Termes liés aux services

**CEX (Centralized Exchange)**. Plateforme d’échange centralisée. Binance, Coinbase, Kraken, OKX, Bybit, Bitstamp, Bitfinex. Détient les fonds des utilisateurs (custodial). Soumis à KYC dans les juridictions régulées.

**DEX (Decentralized Exchange)**. Plateforme d’échange décentralisée, sur smart contracts. Uniswap, PancakeSwap, Curve, dYdX. Pas de KYC (en principe), pas de custodian. L’utilisateur conserve ses clés.

**VASP (Virtual Asset Service Provider)**. Terme FATF désignant tout service qui manipule des actifs virtuels (exchanges, custodians, wallet providers, parfois DEX selon interprétation). Soumis à la Travel Rule.

**Bridge**. Pont permettant le transfert d’actifs entre blockchains. Wormhole, Multichain (compromis 2023), Stargate, etc. Souvent ciblé par hacks (cf Ronin, Ch.43). Détaillé Ch.33.

**Mixer / Tumbler**. Service mélangeant les fonds de plusieurs utilisateurs pour casser la traçabilité. Tornado Cash (sanctionné 2022), Helix (saisi 2020), Bitcoin Fog (saisi 2021), Chipmixer (saisi 2023), Samourai (saisi 2024). Détaillé Ch.31.

**CoinJoin**. Technique de mélange Bitcoin coopérative (sans custodian central). Wasabi, Samourai. Détaillé Ch.32.

**Privacy coin**. Cryptomonnaie conçue pour anonymat. Monero, Zcash, Dash. Détaillé Ch.35.

**Smart contract**. Programme déployé sur une blockchain, exécuté quand des conditions sont remplies. Ethereum est la blockchain pionnière. Détaillé Ch.9.

**DeFi (Decentralized Finance)**. Écosystème d’applications financières sur blockchain (DEX, lending, yield farming, dérivés). Détaillé Ch.34.

### 3.5 Termes liés à la conformité et la réglementation

**KYC (Know Your Customer)**. Procédure d’identification des clients par les VASP. Exigée par MiCA et la plupart des juridictions sérieuses.

**AML (Anti-Money Laundering) / CFT (Counter-Financing of Terrorism)**. Cadre réglementaire de lutte contre le blanchiment et le financement du terrorisme.

**Travel Rule**. Recommandation FATF étendue aux VASP : pour transferts au-delà d’un certain seuil (1 000 USD/EUR), l’expéditeur doit transmettre des informations sur l’expéditeur et le destinataire au VASP destinataire.

**MiCA (Markets in Crypto-Assets)**. Règlement UE 2023/1114, entré en vigueur progressivement à partir de 2024. Cadre réglementaire crypto unifié pour l’UE.

**Sanctions OFAC**. Sanctions américaines ciblant entités, individus, et désormais adresses crypto. Tornado Cash (août 2022), Garantex, Suex, Bitzlato, multiples wallets Lazarus.

**TRACFIN**. Cellule française de renseignement financier. Reçoit les déclarations de soupçon des assujettis (banques, VASP). Cadre français de lutte AML/CFT.

**SAR (Suspicious Activity Report)**. Déclaration de soupçon (équivalent international du signalement TRACFIN).

### 3.6 Termes spécifiques d’enquête

**Drainer**. Smart contract ou script malveillant qui vide automatiquement un wallet une fois que la victime signe une transaction d’approval. Vecteur de phishing crypto majeur 2022-2026.

**Approval**. Permission accordée à un smart contract de dépenser certains tokens. Mécanisme légitime (DEX, lending) mais détourné par phishing.

**Rug pull**. Arnaque où les créateurs d’un projet crypto disparaissent avec les fonds des investisseurs. Variante : honeypot token (impossible à revendre).

**Pig butchering** (« 杀猪盘 », shā zhū pán). Type de fraude combinant manipulation sentimentale (romance scam) et faux investissement crypto. Volumes massifs depuis 2022. Ch.25 détaillé.

**Pump-and-dump**. Manipulation coordonnée du cours d’un token : achats coordonnés (pump) suivis d’une revente massive (dump) qui plante le cours.

**Wash trading**. Fausses transactions entre wallets contrôlés par la même entité, pour simuler du volume.

**Dust attack**. Envoi de petits montants vers de nombreuses adresses pour tenter de les corréler par heuristiques de co-spending si elles « consolident » la poussière.

-----

## Chapitre 4 — Les grandes familles de blockchains

Toutes les blockchains ne sont pas équivalentes. Pour l’analyste, comprendre les différences structurelles entre familles est essentiel — elles déterminent les méthodes d’enquête applicables, les outils utilisables, et les patterns à observer.

### 4.1 Bitcoin et le modèle UTXO

**Bitcoin** (lancé 2009). Première blockchain. Modèle **UTXO** (Unspent Transaction Output). Pas de smart contracts (au sens Ethereum) — Bitcoin est volontairement minimaliste.

**Caractéristiques pour l’enquête** :

- **Très grande lisibilité** : chaque transaction est un graphe d’inputs et outputs.
- **Heuristiques de clustering matures** (co-spend, change detection, peeling).
- **Outils nombreux** : Mempool.space, Blockstream.info, OXT, Breadcrumbs, Chainalysis, etc.
- **Communauté de recherche active** depuis 15+ ans.

**Usages illicites observés** : ransomware (BTC reste dominant pour les rançons selon Chainalysis 2024-2025), darknet markets (BTC + Monero), saisies historiques (Silk Road, AlphaBay, Bitfinex, Colonial Pipeline). En **baisse relative** vs stablecoins pour les autres typologies.

**Forks et clones notables** : Bitcoin Cash (BCH), Bitcoin SV (BSV), Litecoin (LTC), Dogecoin (DOGE). Mêmes principes d’analyse. Volumes illicites significativement moindres.

### 4.2 Ethereum et chaînes EVM

**Ethereum** (lancé 2015). Modèle **account-based** (pas UTXO). Introduction des **smart contracts** programmables. Dominance dans DeFi, NFT, DAO, et multiples couches d’application.

**Caractéristiques pour l’enquête** :

- **Lisibilité bonne mais différente** : transactions plus simples (un emetteur, un destinataire, un montant), mais complexité dans les **internal transactions** (appels entre smart contracts) et **logs d’événements**.
- **Outil dominant** : Etherscan.
- **Tokens omniprésents** : transferts ETH directs souvent moins importants que les transferts de tokens (USDT, USDC, autres).

**EVM (Ethereum Virtual Machine) compatibles** : BNB Chain, Polygon, Avalanche, Arbitrum, Optimism, Fantom, Base. **Mêmes principes d’enquête**, mêmes adresses (compatibles 0x…), mêmes outils dérivés (BscScan, PolygonScan, etc.). L’analyste qui maîtrise Ethereum peut travailler sur ces chaînes avec courbe d’apprentissage faible.

**Usages illicites** : DeFi exploits, rug pulls, NFT scams, drainers de wallets, certains flux ransomware (en hausse). Moins dominante que Bitcoin pour ransomware, mais centrale pour fraudes retail et acteurs étatiques (Lazarus utilise massivement Ethereum + Tornado Cash).

### 4.3 TRON

**TRON** (lancé 2018, fondateur Justin Sun). Blockchain à modèle compte, transactions très bon marché (~quelques centimes USD), confirmation rapide (~3 secondes).

**Caractéristiques structurantes pour l’enquête** :

- **USDT-TRON est dominant** : la blockchain TRON est devenue **la plate-forme principale** pour les flux USDT, légitimes et illicites. Source : observations Chainalysis, TRM Labs, Elliptic 2024-2026.
- **Frais minimes** : un transfert USDT-TRON coûte ~1 centime, contre ~5-30 USD sur Ethereum (selon congestion). Cette économie attire les flux à haute fréquence, dont le pig butchering et certaines opérations de blanchiment.
- **Confirmation rapide** : en 3 secondes, une transaction est finalisée. Pratique pour les criminels qui veulent disperser rapidement.
- **Outil principal** : Tronscan.

**Usages illicites observés** : pig butchering massif (volumes en milliards USD selon estimations), certaines fraudes ransomware (en hausse), opérations Lazarus, blanchiment et placement.

**Critique** : l’écosystème TRON est moins coopératif sur la régulation que d’autres. La fondation TRON est controversée. Plusieurs procédures aux US visent Justin Sun et entités liées.

**Pour l’analyste** : TRON ne peut **pas être ignoré**. Une part majeure des flux illicites stablecoin y transite. Maîtriser Tronscan et les heuristiques TRON est aussi important que maîtriser Etherscan.

### 4.4 Solana

**Solana** (lancé 2020). Architecture différente, très haute performance (théorique 65 000 TPS), confirmation quasi-instantanée, frais infimes.

**Caractéristiques pour l’enquête** :

- **Modèle compte** différent d’Ethereum (account model spécifique Solana).
- **Tokens SPL** (Solana Program Library) — équivalent ERC-20.
- **Outil** : Solscan, Solana Explorer.
- **Volumes croissants** : DeFi Solana, NFT Solana, memecoins (pump.fun et écosystème associé 2024-2025).

**Usages illicites observés** : memecoin scams massifs (rug pulls quasi-industriels via pump.fun), certaines fraudes retail. En forte croissance.

**Pour l’analyste** : Solana est **moins mature** dans l’outillage forensique que Bitcoin/Ethereum. Les outils commerciaux (Chainalysis, TRM, Elliptic) couvrent Solana mais avec moins de profondeur historique. Les heuristiques de clustering sont moins éprouvées.

### 4.5 Autres chaînes pertinentes

**BNB Chain (ex-Binance Smart Chain)**. EVM-compatible. Volumes massifs, particulièrement DeFi et memecoins. Outil : BscScan.

**Polygon**. Layer-2 Ethereum. EVM-compatible. Croissance.

**Avalanche**. EVM-compatible. Subnets. Croissance modérée.

**Arbitrum, Optimism, Base**. Layer-2 Ethereum (rollups). EVM-compatibles. Forte croissance 2023-2026.

**Cosmos écosystème** (Cosmos Hub, Osmosis, etc.). Différent d’Ethereum, IBC pour cross-chain. Outils moins matures.

**XRP Ledger (Ripple)**. Modèle différent. Usage majoritaire institutionnel.

**Stellar**. Similaire dans la philosophie à XRP.

### 4.6 Privacy coins

**Monero (XMR)** (lancé 2014). Anonymat par construction. Ring signatures, RingCT, stealth addresses. Détaillé Ch.35.

**Zcash (ZEC)** (lancé 2016). Optionnellement anonymisable (transparent par défaut, shielded en option). Une fraction des transactions est shielded.

**Dash** (lancé 2014). Anonymisation via PrivateSend (CoinJoin amélioré). Moins efficace que Monero, plus simple à analyser.

**Pour l’analyste** : Monero est **largement opaque**. Zcash transparent est lisible. Zcash shielded est opaque (mais peu utilisé en pratique). Dash est analysable avec effort.

### 4.7 Implications opérationnelles

**Pour Bitcoin**, l’analyste a besoin :

- Maîtrise du modèle UTXO.
- Heuristiques de clustering (co-spend, change).
- Outils : Mempool.space, OXT, Chainalysis.

**Pour Ethereum et EVM-chains**, l’analyste a besoin :

- Compréhension du model account.
- Lecture de smart contracts et events.
- Outils : Etherscan + équivalents par chaîne.

**Pour TRON**, l’analyste a besoin :

- Maîtrise de Tronscan.
- Spécificités USDT-TRON.
- Patterns pig butchering et blanchiment.

**Pour Solana**, l’analyste a besoin :

- Solscan.
- Spécificités SPL tokens.
- Conscience des limites d’outillage forensique.

**Pour Monero**, l’analyste se prépare à :

- Utiliser les **points off-chain** (exchanges, KYC, OPSEC errors).
- Documenter la rupture de visibilité.

Une enquête moderne touche **fréquemment plusieurs chaînes**. L’analyste polyvalent est l’analyste utile.

-----

## Chapitre 5 — Le métier d’analyste crypto-forensique

Avant les techniques, la **posture professionnelle**. Ce chapitre couvre les compétences, l’OPSEC, l’éthique, et l’organisation du métier.

### 5.1 Le profil d’analyste crypto-forensique

**Compétences techniques** :

- Lecture fluide des blockchains majeures (Bitcoin, Ethereum, TRON minimum).
- Maîtrise des explorateurs publics (Mempool, Etherscan, Tronscan).
- Maîtrise d’au moins un outil professionnel (Chainalysis, TRM, ou Elliptic) si budget disponible.
- Capacité à lire et interpréter du code de smart contract basique (Solidity).
- Compréhension des techniques d’obfuscation (mixers, bridges, swaps).
- Fluence avec un environnement Python pour scripts d’analyse personnalisés.

**Compétences analytiques** :

- Méthodologie d’enquête structurée.
- Vocabulaire calibré (WEP).
- Capacité de discernement (distinguer observation, inférence, attribution).
- Discipline anti-biais.
- Rédaction analytique claire.

**Compétences transverses** :

- Curiosité (l’écosystème évolue, il faut suivre).
- Rigueur (la documentation conditionne la valeur du travail).
- Patience (les enquêtes prennent semaines/mois).
- Communication (rapports adaptés à des audiences variées).
- Éthique (résistance aux dérives, alignement avec mandat).

**Background typique** :

- Parcours **finance/AML** reconverti vers crypto (ex-banquier, ex-analyste TRACFIN, ex-compliance officer).
- Parcours **technique/cyber** étendu vers crypto (ex-SOC, ex-pentester, ex-CTI).
- Parcours **académique** (master Finance, master Cybersécurité, parfois doctorat en cryptographie).
- Parcours **enquêteur** (gendarmerie/police, services de renseignement) reconverti.

Sarah Marin, dans MIXSHADOW, illustre le profil hybride : 3 ans TRACFIN (analyste financière) puis 3 ans Athéna (crypto-forensique pure). Combinaison appréciée.

### 5.2 OPSEC de l’analyste crypto

L’analyste crypto manipule des données sensibles : adresses de criminels actifs, flux en cours, méthodologies. Plusieurs principes OPSEC.

**Séparation des univers**. Ne pas mélanger comptes personnels et infrastructure d’investigation. Une machine dédiée pour les analyses sensibles (comme pour Dark Web — voir cours associé).

**Wallet d’investigation séparé**. Si l’enquête nécessite des transactions de test (rare en OSINT pur, plus fréquent en undercover), wallet dédié, financé par circuit professionnel, jamais lié à l’identité personnelle de l’analyste.

**Pas d’interaction directe avec les wallets cibles**. L’analyste OSINT **observe**, il ne **transacte pas** avec les wallets criminels. Envoyer même 1 satoshi vers un wallet ransomware peut alerter l’opérateur et compromettre l’investigation. C’est aussi potentiellement illégal (financement de groupe sanctionné selon l’acteur).

**Pas de phishing aux acteurs**. Tentation parfois : « contacter le scammer en feignant être une victime ». Cela dépasse souvent le cadre OSINT et peut tomber dans l’enquête sous couverture, réservée aux autorités.

**Documentation immédiate**. Toute observation est captée, horodatée, hachée. Pas de mémoire orale. Voir Ch.23.

**Pas de rediffusion incontrôlée**. Les observations ne sont partagées qu’au cercle justifié (mandant, autorités, ISAC selon TLP). Pas de bavardage entre analystes ou avec journalistes.

**Confidentialité du mandat client**. Sauf accord explicite, l’identité du mandant et la nature exacte de l’enquête restent confidentielles, y compris vis-à-vis de l’écosystème pro.

### 5.3 Cadre éthique

**Principes** :

**Légalité scrupuleuse**. L’OSINT crypto opère dans un cadre légal — RGPD, sanctions, AML, secret professionnel. L’analyste connaît le cadre applicable à son périmètre.

**Mandat respecté**. L’enquête se déroule selon le mandat. Pas d’extension non autorisée vers d’autres cibles, pas de curiosité incontrôlée.

**Minimisation**. Collecter ce qui est nécessaire. Ne pas extraire systématiquement toutes les données accessibles « au cas où ».

**Non-prolifération**. Les données collectées ne fuitent pas hors du cercle justifié.

**Calibration honnête**. Ne pas embellir les conclusions. Ne pas masquer les limites.

**Respect des victimes**. Beaucoup d’enquêtes impliquent des victimes (pig butchering, ransomware). Leurs données et leur dignité sont respectées.

**Coopération avec autorités**. Si l’enquête révèle des infractions graves, signalement obligatoire (article 40 CPP pour fonctionnaires, signalement TRACFIN pour assujettis).

**Refus des dérives**. L’analyste résiste aux pressions pour produire des rapports orientés (« attribuer cet acteur à tel groupe pour des raisons politiques »).

### 5.4 Outils, certifications, formation

**Certifications utiles** :

- **Chainalysis Certified Reactor (CRC)** : référence industrie, formation officielle Chainalysis.
- **TRM Labs Certified Investigator (CTI)** : certification TRM Labs.
- **Certified Cryptocurrency Investigator (CCI)** : certification de la blockchain forensics community.
- **CAMS (Certified Anti-Money Laundering Specialist)** : certification AML transverse, utile pour le contexte.

**Formations courtes** :

- **Bellingcat OSINT trainings** (volet crypto inclus).
- **SANS FOR578 / FOR589** (CTI / cybercrime intelligence, modules crypto).
- **Webinars vendors** (Chainalysis, TRM, Elliptic — gratuits ou peu coûteux).

**Auto-formation** :

- Lecture des rapports annuels Chainalysis Crypto Crime, TRM Labs reports, Elliptic publications.
- Suivre Twitter/X de chercheurs publics : @zachxbt, @mishasolovyov (Solovyov), @pcaversaccio (smart contract security), @0x_lasagna, @samczsun (security DeFi), @tayvano_ (Tay).
- Outils de pratique : explorateurs publics gratuits, analyse de cas historiques publiés.
- Communautés : OnChain Investigators, OSINT Curious, SEAL ISAC.

**Veille à entretenir** :

- Rapports Chainalysis (annuels + mid-year updates).
- TRM Labs blog et threat reports.
- Elliptic publications.
- Rapports FATF (Virtual Assets, Targeted Financial Sanctions, etc.).
- Bulletins OFAC SDN.
- Travaux ZachXBT (chercheur indépendant prolifique).
- Blogs communautaires (Defillama, DeFiLlama Adapter, Rekt News pour les hacks).

### 5.5 L’organisation du travail

**Outillage informatique** :

- Machine principale propre (Linux ou macOS, Windows acceptable).
- VM dédiée pour analyses sensibles (Whonix ou équivalent si interaction Tor).
- Espace de stockage dédié et sauvegardé pour les preuves.
- Outils de capture (Hunchly ou équivalent).
- Outils blockchain (cf Partie IV).

**Workflow type** :

- Réception du mandat / alerte.
- Cadrage et planification.
- Investigation structurée (Partie III).
- Documentation continue.
- Rédaction du rapport (Ch.46).
- Présentation et coopération.
- Clôture et archivage.

**Gestion des dossiers** :

- Un dossier = un répertoire structuré (notes, captures, exports, rapport final).
- Versioning (Git ou équivalent pour rapports).
- Archivage immutable post-clôture.

**Travail en équipe** :

- Pour les grandes investigations, plusieurs analystes (un lead, des contributeurs).
- Partage via plateforme sécurisée (Mattermost, Element/Matrix self-hosted, etc.).
- Peer review systématique des rapports.

### 5.6 Carrière et évolution

**Trajectoires possibles** :

- **Cabinet de conseil / forensique** : Athéna (fictif), Wavestone, Mandiant, Kroll, etc.
- **Vendor blockchain intelligence** : Chainalysis, TRM Labs, Elliptic recrutent.
- **Forces de l’ordre** : SDLC, OFAC français, gendarmerie nationale (cellule cyber), magistrature spécialisée.
- **TRACFIN, ANSSI, DGSI**.
- **Compliance d’exchange ou banque** : équipes AML internes des VASP régulés.
- **Renseignement** : DGSE, services partenaires.
- **Indépendant** : ZachXBT comme modèle (mais rare).

**Évolution des compétences** :

- Junior (0-2 ans) : maîtrise technique, lecture, outils.
- Senior (3-7 ans) : pilotage d’enquêtes complètes, mentoring, livrables.
- Lead (7+ ans) : direction d’équipe, méthodologie, contribution doctrinale.

**Rémunération** (indicatif France 2025-2026) : junior 45-55 k€, senior 65-90 k€, lead 100-150 k€+. Plus élevé chez vendors (Chainalysis, TRM) et en finance (banques d’investissement, hedge funds).

### 5.7 Fil rouge — MIXSHADOW : préparation de l’analyste

> **🔗 MIXSHADOW — Épisode 2 : setup**
> 
> Sarah prépare son environnement. Protocole Athéna pour MIXSHADOW :
> 
> - **Machine dédiée** : laptop sécurisé, OS Ubuntu LTS hardened, accès limité au sous-réseau d’investigation.
> - **Outils blockchain** : Chainalysis Reactor (licence Athéna), TRM Labs Investigations (validation croisée), Etherscan/Tronscan/Mempool en accès direct, scripts Python pour exports CSV.
> - **Espace de travail** : dossier MIXSHADOW chiffré, accès restreint à l’équipe (Sarah + 1 analyste junior + revue par directeur Athéna), backup quotidien sur stockage immutable.
> - **Documentation** : Hunchly pour captures de pages d’explorateur, journal d’enquête en Markdown, exports CSV horodatés et hashés.
> - **Pas de wallets de test** : MIXSHADOW est OSINT pur, pas d’interaction transactionnelle.
> - **Communication** : Element/Matrix interne Athéna pour discussions équipe, email chiffré avec DGSI, audio sécurisé pour les briefings.
> 
> Avant de démarrer le traçage proprement dit, Sarah complète le **dossier de cadrage** : périmètre, objectifs, livrables attendus, contacts, échéances. Validation directeur Athéna et DGSI. Le cadrage prend 4 heures — temps bien investi.
> 
> Action immédiate : récupérer l’**adresse Bitcoin** où les 35 BTC ont été versés. Le RSSI Aurélien Médical fournit la clé : adresse de paiement BTC fournie par Akira via portail Tor, montant exact 35,00000000 BTC, TXID de la transaction de paiement, timestamp 14 mars 09:12 UTC.
> 
> Sarah valide le TXID sur Mempool.space. Le paiement est bien enregistré, 6 confirmations atteintes. Adresse réceptrice : `bc1q...[adresse fictive de 42 caractères]`. Premier nœud du graphe MIXSHADOW.
> 
> Ch.6 va détailler comment lire cette transaction Bitcoin en profondeur. Ch.13 reprendra MIXSHADOW pour l’investigation proprement dite.

-----
