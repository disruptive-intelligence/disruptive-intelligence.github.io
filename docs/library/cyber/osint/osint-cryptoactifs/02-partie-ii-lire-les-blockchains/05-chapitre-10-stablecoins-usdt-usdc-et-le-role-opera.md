---
title: 'Chapitre 10 — Stablecoins : USDT, USDC et le rôle opérationnel'
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie II — Lire les blockchains
  - index.md
---

Les **stablecoins** sont devenus la **monnaie de transaction** de pans entiers de l’écosystème crypto. Légitime comme illicite. Ce chapitre approfondit leur fonctionnement, leur dominance dans certains flux illicites, et les opportunités défensives qu’ils offrent (gel d’actifs).

## 10.1 Qu’est-ce qu’un stablecoin

Un **stablecoin** est un crypto-actif dont la valeur est arrimée à une référence stable, généralement le **dollar US** (1 stablecoin = 1 USD).

**Mécanismes d’arrimage** :

**Adossés à des réserves fiat (« centralized fiat-backed »)** : émis par une entreprise (Tether, Circle, Paxos) qui détient des réserves USD (cash + bons du Trésor + autres) en quantité équivalente aux tokens en circulation. C’est le modèle dominant.

- USDT (Tether) — émetteur Tether Limited.
- USDC (USD Coin) — émetteur Circle.
- BUSD (Binance USD) — émetteur Paxos, en déclin depuis 2023.
- TUSD (TrueUSD), USDP (Pax Dollar), GUSD (Gemini Dollar) — plus petits.

**Adossés à du crypto (« crypto-collateralized »)** : maintien du peg via collatéralisation crypto + mécanismes algorithmiques.

- DAI (MakerDAO) — adossé à un panier d’actifs crypto (ETH, USDC, autres) avec sur-collatéralisation.

**Algorithmiques** : sans collatéral réel, pegging par algorithme. Modèle qui a connu des effondrements catastrophiques.

- UST (TerraUSD) — effondré en mai 2022, perte ~40 Mrd USD pour les investisseurs. Modèle discrédité.

## 10.2 Pourquoi les stablecoins dominent les flux

**Stabilité de valeur**. Pour un criminel comme pour un usager légitime, la **volatilité** de Bitcoin/Ethereum est un problème. Recevoir 35 BTC à 9h et les convertir 6h plus tard peut signifier une perte de 5-10% (ou un gain — symétrique). Les stablecoins éliminent ce risque pour les opérations de trésorerie.

**Liquidité globale**. USDT et USDC sont disponibles sur la quasi-totalité des exchanges, DEX, plateformes DeFi. Conversion en/depuis n’importe quel autre actif crypto en quelques secondes.

**Multi-chaînes**. USDT existe sur Ethereum, TRON, BNB Chain, Solana, Polygon, Avalanche, Arbitrum, Optimism, et des dizaines d’autres. Permet l’arbitrage entre chaînes selon coûts et disponibilités.

**Rapidité et coût**. Sur TRON, un transfer USDT coûte ~1 centime et confirme en 3 secondes. Sur Ethereum, plus cher (5-30 USD) mais flexible.

**Inclusion bancaire informelle**. Dans des pays à banking dysfonctionnel (Argentine, Liban, Nigeria, Venezuela, Zimbabwe), USDT sert de **dollar de remplacement** accessible.

**Pour l’écosystème criminel**, les stablecoins offrent :

- Pas de volatilité pendant le blanchiment.
- Rapidité de transfert.
- Multi-chaînes pour cross-chain laundering.
- Volume liquide pour fondre les flux dans le bruit légitime.

Selon les rapports Chainalysis 2024-2025, **les stablecoins représentent une part dominante des volumes de transactions on-chain** et une fraction significative et croissante des **flux illicites identifiables**. TRON est devenu particulièrement central pour USDT illicite.

## 10.3 USDT vs USDC — différences pour l’enquête

**USDT (Tether)** :

- Émetteur : **Tether Limited**, opaque historiquement, basée hors juridictions strictes.
- **Dominant** en volume (~110 Mrd USD en circulation 2025).
- Coopération avec autorités : **variable**. Tether gèle des adresses sur réquisition mais pas systématiquement, et avec délais variables. Plus rapide depuis 2023.
- Disponible sur **toutes les chaînes principales**.

**USDC (Circle)** :

- Émetteur : **Circle**, US-based, régulé.
- ~30 Mrd USD en circulation 2025.
- Coopération avec autorités : **forte et rapide**. Circle gèle les adresses listées par OFAC quasi-immédiatement. Bien intégré aux processus US.
- Disponible sur multiples chaînes mais moins que USDT.

**Pour l’analyste** :

- Voir des fonds illicites passer par **USDC** est moins fréquent que par USDT (les criminels savent que Circle gèle vite).
- **USDT-TRON** est aujourd’hui le pipeline majeur des flux illicites stablecoin (frais bas + Tether moins réactif + multi-juridictionnel).
- **USDT-Ethereum** reste utilisé, surtout pour interactions DeFi.
- Identifier dès qu’un fonds passe en USDC = potentiel **angle de gel** rapide.

## 10.4 Le gel d’actifs

Les stablecoins centralisés (USDT, USDC, autres) ont une **fonction blacklist** dans leur smart contract. L’émetteur peut **geler** une adresse — les tokens à cette adresse deviennent intransférables, même si l’utilisateur a la clé privée.

**Mécanisme technique** :

- Dans le contrat USDT, fonction `addBlackList(address)` (réservée à l’owner).
- Une fois une adresse blacklistée, ses tokens ne peuvent plus être transférés.
- L’émetteur peut aussi `destroyBlackFunds(address)` — détruire les tokens de l’adresse blacklistée (équivalent à les retirer de la circulation).

**Cas d’usage pour les autorités** :

- Réquisition adressée à Tether ou Circle pour geler une adresse identifiée comme criminelle.
- En coopération étroite, le délai entre demande et gel peut être de quelques heures (USDC, Circle bien préparé).
- Pour USDT, le délai est plus variable (heures à jours selon la procédure et la juridiction demandeuse).

**Cas réels** :

- Tether a gelé des centaines de millions USDT cumulés depuis 2017, en réponse à demandes OFAC, FBI, autorités étrangères.
- Circle a gelé Tornado Cash addresses immédiatement après la sanction OFAC d’août 2022.
- En cas de hack majeur (ex : Ronin, Wormhole), les fonds qui transitent par stablecoins sont parfois gelés à la requête des victimes.

**Pour l’enquêteur** : identifier dès qu’un flux transite par un stablecoin gel-able = **opportunité de coordination**. Remontée rapide à l’émetteur via les autorités peut figer des fonds avant cashout.

## 10.5 USDT-TRON vs USDT-Ethereum

**Erreur classique** : penser que « USDT est USDT » indépendamment de la chaîne. **Faux**.

- **USDT-Ethereum** : un token ERC-20 sur Ethereum, contrat `0xdAC17...`.
- **USDT-TRON** : un token TRC-20 sur TRON, contrat `TR7N...`.
- **Ce sont DEUX tokens distincts**, juste émis par le même émetteur (Tether) avec le même peg USD.

**Conséquences** :

**Un USDT-Ethereum NE PEUT PAS être directement transféré à une adresse TRON**. Il faut un **bridge** ou un **swap cross-chain** (passage par exchange ou service de bridging).

**Les soldes sont distincts**. Une adresse Ethereum peut avoir 1000 USDT, et l’« même utilisateur » sur TRON peut avoir 500 USDT — c’est deux balances séparées.

**Les frais sont radicalement différents**. Transfer USDT-TRON ~1 centime. Transfer USDT-Ethereum 5-30 USD selon congestion. Cette différence explique pourquoi les flux à haute fréquence (pig butchering, certains blanchiments) privilégient TRON.

**L’enquêteur** vérifie toujours **sur quelle chaîne** il regarde. Mentions « USDT » sans préciser la chaîne sont ambiguës et doivent être clarifiées.

## 10.6 Patterns de blanchiment via stablecoins

**Pattern 1 — Conversion BTC → USDT**. Après un paiement BTC (rançon, paiement darknet), conversion rapide en USDT pour stabiliser la valeur, soit via exchange centralisé, soit via swap (FixedFloat, ChangeNOW, etc.).

**Pattern 2 — Bridge cross-chain via USDT**. USDT-Ethereum → USDT-TRON via bridge ou exchange. Réduit la traçabilité et change le coût opérationnel.

**Pattern 3 — Layering USDT-TRON**. Multiple transferts entre adresses TRON contrôlées, peeling chain-style, avec frais minimes. Alimente la dispersion.

**Pattern 4 — Off-ramp via P2P**. Conversion USDT → fiat via plateformes P2P (Binance P2P, LocalCryptos, etc.) ou OTC desks. Permet de quitter la blockchain en monnaie locale.

**Pattern 5 — Obfuscation pré-cashout**. Avant cashout final, mélange via DEX ou usage de protocoles DeFi pour ajouter du bruit.

## 10.7 Investigation TRON spécifique

**Tronscan.org** : explorateur principal TRON.

**Lecture de transaction USDT-TRON** :

- Page transaction TRON, similaire à Etherscan.
- Section « TRC-20 Tokens Transferred » montre les transferts USDT (et autres TRC-20).
- Adresse contrat USDT-TRON : `TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t`.

**Heuristiques TRON** :

- Beaucoup de wallets utilisateurs (vs services), donc moins d’agrégation que Bitcoin.
- Pattern pig butchering reconnaissable : adresses recevant de **multiples victimes**, consolidant rapidement, et déposant sur exchange.
- Vérifier les **labels Tronscan** (limités vs Etherscan), enrichir avec Chainalysis ou TRM.

**Limites** :

- Outils forensiques moins matures que pour Bitcoin/Ethereum.
- Documentation communautaire moins riche.
- Cooperation Tron Foundation variable.

## 10.8 Fil rouge — MIXSHADOW : transit par stablecoins

> **🔗 MIXSHADOW — Épisode 7 : conversion partielle vers USDT**
> 
> Sarah continue le suivi des branches éplutchées du peeling chain Akira. L’une des branches (~3 BTC envoyés à un exchange non-KYC en hop 12) ressort, 4 heures plus tard, sous forme d’**USDT-TRON**.
> 
> Sequence :
> 
> - 3 BTC déposés sur exchange non-KYC X (identifié par Chainalysis comme « Exchange à risque, pas de KYC, juridiction grise »).
> - Conversion BTC → USDT-TRON sur l’exchange (interne, pas observable on-chain).
> - Retrait : ~290 000 USDT-TRON envoyés depuis l’adresse retrait de l’exchange vers `TR[Akira-TRON]...` (nouvelle adresse Akira sur TRON).
> 
> Sur Tronscan, Sarah observe :
> 
> - Adresse `TR[Akira-TRON]` reçoit 290 000 USDT.
> - Quelques heures plus tard, dispersion : 6 transferts vers 6 nouvelles adresses TRON, montants variables (40-60k USDT chacun).
> - Chaque sub-adresse refait à son tour des transferts (peeling-style adapté à TRON).
> 
> **Hypothèse Sarah** : Akira utilise USDT-TRON comme **monnaie d’opération** pour la phase de blanchiment finale. Les frais bas permettent un layering étendu. Les destinations finales seront probablement :
> 
> - Off-ramp via P2P / OTC dans des juridictions grises (Russie, Asie centrale).
> - Cashout via cartes prepaid crypto.
> - Certains flux peuvent revenir vers fiat via exchanges régionaux moins regardants.
> 
> Sarah note : **opportunité de coordination Tether**. Bien que Tether soit moins réactif que Circle, dans le cadre d’une coordination DGSI/TRACFIN avec FBI/OFAC, une demande de gel sur les principales adresses Akira identifiées peut être tentée. Elle prépare la liste des **6 adresses TRON principales** + **2 adresses Ethereum** pour transmission.
> 
> Le rapport intermédiaire MIXSHADOW (à 4 semaines de mission) inclura cette demande de coordination Tether.
> 
> Au passage, Sarah documente les **patterns Akira** observés : peeling Bitcoin → swap partiel via FixedFloat → Tornado Cash sur Ethereum → conversion vers USDT-TRON via exchange non-KYC → dispersion TRON. C’est un pattern qu’elle pourrait reconnaître chez d’autres victimes Akira pour corroboration. Elle alerte d’autres investigateurs Athéna et la DGSI : si d’autres victimes Akira nécessitent investigation, ce template de blanchiment est potentiellement réutilisé.

-----
