---
title: Chapitre 8 — Cryptomonnaies et anonymat financier
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie II — Infrastructures techniques et anonymat
  - index.md
---

Les cryptomonnaies sont la couche **financière** du dark web. Sans elles, l'économie clandestine à l'échelle observée serait impossible. Mais les propriétés d'anonymat des cryptomonnaies sont largement mal comprises, y compris par leurs utilisateurs criminels — ce qui explique une part importante des identifications réussies.

## 8.1 Bitcoin : pseudonymat, pas anonymat

Bitcoin (2009, Satoshi Nakamoto) est la cryptomonnaie historique. Propriété fondamentale souvent mécomprise : Bitcoin est **pseudonyme**, pas **anonyme**.

**Principe** : chaque transaction Bitcoin est enregistrée publiquement dans la blockchain. Tout le monde peut voir : quelle adresse a envoyé combien à quelle adresse, à quel moment. Les adresses sont des chaînes de caractères (par exemple `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh`) sans lien apparent avec une identité réelle.

**Mais** : à un moment, une adresse Bitcoin doit être liée à une identité pour être utile — que ce soit via un exchange (qui fait du KYC), une merchant (qui a votre livraison), ou toute interaction qui relie l'adresse à un nom. Une fois ce lien établi, l'historique entier de l'adresse devient attribuable.

Cette propriété a structuré toutes les investigations crypto du dark web : les grandes saisies (Silk Road, AlphaBay, Hydra, multiples ransomware) ont reposé sur le traçage blockchain des flux financiers. **Les cryptocurrency tracing firms** (Chainalysis, TRM Labs, Elliptic, CipherTrace/Mastercard) ont construit un écosystème de renseignement blockchain qui est devenu un outil central de lutte contre la cybercriminalité (Ch.31).

## 8.2 Le traçage Bitcoin en pratique

Plusieurs techniques de traçage sont systématiquement appliquées.

**Clusterisation** : regrouper les adresses qui appartiennent probablement à la même entité, en observant les patterns (adresses qui co-dépensent dans une même transaction sont probablement contrôlées par la même entité).

**Heuristiques de change** : identifier les adresses de change (monnaie rendue) lors d'une transaction pour suivre le portefeuille source.

**Labellisation** : des milliers d'adresses connues sont labellisées (adresses Silk Road historiques, adresses ransomware connues, adresses de grands exchanges type Binance, Coinbase). Les transactions qui touchent ces adresses labellisées donnent des points d'attribution.

**Suivi cross-chain** : les flux passent souvent par plusieurs blockchains (Bitcoin → Ethereum → stablecoin). Les outils modernes suivent ces chaînes.

**Corrélation on-chain / off-chain** : croisement avec données exchanges (requêtes légales pour identifier un compte), surveillance de forums (vendeurs postent parfois leur adresse de paiement), et autres sources.

L'efficacité a été démontrée par une série de cas emblématiques : saisie des fonds Colonial Pipeline (FBI récupère ~2,3 M USD en juin 2021), saisie Bitfinex (DOJ saisit ~3,6 Mrd USD en février 2022), multiples saisies Lazarus, démantèlement Chipmixer (mars 2023), etc.

## 8.3 Monero : anonymat par construction

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

## 8.4 Stablecoins : le nouveau facilitateur

Depuis 2020-2021, les **stablecoins** (USDT Tether principalement, USDC dans une moindre mesure) sont devenus **un vecteur massif de transactions dark web**. Raisons :

- **Stabilité** : pas de volatilité (contrairement à Bitcoin qui peut varier de 20% en une semaine).
- **Liquidité** : facilement convertibles partout.
- **Blockchain TRON** : USDT sur TRON est dominant — frais très faibles (~1 cent par transaction), confirmations rapides (~3 secondes). TRON est devenu la blockchain dominante des flux illicites crypto en volume transactionnel.

**Mais** : les stablecoins ne sont **pas anonymes**. Chaque transaction est on-chain et visible. Les émetteurs (Tether pour USDT, Circle pour USDC) peuvent **geler** les adresses sur requête des autorités — Tether a gelé des centaines de millions de dollars d'adresses suspectes sur les années 2022-2024. USDC est encore plus coopérant avec les autorités américaines.

L'attrait des stablecoins pour le dark web est donc structurellement ambigu : plus facile que Bitcoin pour les transactions, plus surveillé que Monero. Beaucoup d'acteurs utilisent USDT comme monnaie d'échange opérationnelle (prix affichés, paiements rapides) mais convertissent en Monero pour le stockage à long terme.

## 8.5 Les mixers et tumblers

Les **mixers** (ou tumblers) sont des services qui mélangent les fonds de plusieurs utilisateurs pour casser la traçabilité. Vous envoyez 1 BTC, le mixer reçoit aussi les BTC d'autres utilisateurs, et vous renvoie 1 BTC (moins une commission de 1-3%) depuis un pool partagé — théoriquement impossible à relier à votre adresse source.

**Services historiques et statut** :

- **Helix** (saisi en 2020, Larry Harmon condamné à 3 ans de prison).
- **Bitcoin Fog** (saisi en 2021, Roman Sterlingov condamné en 2024).
- **Chipmixer** (saisi en mars 2023 — le DOJ et EPRS estiment ~152 000 BTC blanchis soit ~2,73 Mrd EUR).
- **Tornado Cash** : mixer Ethereum, **sanctionné par l'OFAC en août 2022** — première sanction d'un smart contract dans l'histoire. Des développeurs ont été inculpés, y compris Alexey Pertsev (condamné aux Pays-Bas en mai 2024) et Roman Storm (procès aux US en 2024-2025).
- **Wasabi Wallet, Samourai Wallet** : wallets Bitcoin avec CoinJoin intégré. **Samourai saisi en avril 2024, fondateurs inculpés**. Wasabi continue mais avec restrictions accrues.

**Limites actuelles** : les mixers sont une cible prioritaire des forces de l'ordre et des régulateurs. Leur utilisation est devenue un **signal** — les exchanges KYC refusent souvent de créditer des fonds qui ont transité par un mixer connu. Pour un criminel moderne, utiliser un mixer peut être plus coûteux (frais, délais, déclassement du fund) que de convertir directement en Monero.

## 8.6 L'off-ramp comme talon d'Achille

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

## 8.7 Fil rouge — DARKSTREAM : préparation financière

> **🌐 DARKSTREAM — Épisode 4 : le wallet d'investigation**
>
> Athéna alloue un budget opérationnel à Lucas pour son investigation DARKSTREAM. **3 000 USDT** sur un wallet dédié, financé depuis un exchange professionnel (KYC Athéna, pas Lucas). Usage prévu : paiement du droit d'entrée IndustrialLeaks (~0,005 BTC si requis), achats éventuels d'échantillons (sous coordination DGSI), pourboires occasionnels pour obtenir des informations de membres coopératifs.
>
> Lucas note que le vendeur aero_source demande **65 000 USDT** pour les 420 Go. Athéna **n'a aucune intention d'acheter** — le cadre mandaté est investigation, pas acquisition. Mais le prix demandé est un signal : 65 000 USDT correspond à un dump « premium », ce qui suggère soit de vraies données de valeur, soit un scammer ambitieux.
>
> Lucas prévoit d'utiliser les capacités de traçage blockchain de ses outils (Chainalysis, TRM Labs via l'abonnement Athéna) pour **surveiller** l'adresse BTC affichée par aero_source dans son post — capter les paiements éventuels et identifier les acheteurs. C'est un angle d'attribution précieux : même sans identifier aero_source, identifier **un** acheteur peut donner un point d'entrée investigatif.

---
