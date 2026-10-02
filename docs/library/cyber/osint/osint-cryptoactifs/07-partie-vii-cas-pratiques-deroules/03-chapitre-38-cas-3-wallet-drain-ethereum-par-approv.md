---
title: 'Chapitre 38 — Cas 3 : wallet drain Ethereum par approval phishing'
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VII — Cas pratiques déroulés
  - index.md
---

**Profil de l’enquête** : compromission d’un wallet personnel via approval phishing. Mécanisme moderne typique 2023-2026.

## 38.1 Le contexte

**Victime** : Karim (nom fictif), 38 ans, développeur crypto-enthusiaste. Wallet auto-géré (MetaMask), participe activement DeFi et NFT depuis 2021. Patrimoine crypto estimé à ~280 000 USD au moment des faits.

**L’incident** :

- 2026-04-15 vers 22:30 UTC : Karim navigue sur Discord, suit lien partagé dans une community NFT (« nouveau drop exclusif »).
- Site web crédible imitant marketplace NFT légitime. Karim connecte son MetaMask.
- Site demande signature pour « vérifier l’éligibilité ». Karim signe sans relire attentivement.
- 2026-04-15 22:34 UTC : son wallet est vidé. NFT, ETH, tokens — tout part.

**Pertes** :

- ~12 ETH (~36 000 USD).
- Plusieurs NFT (CryptoPunks #XXXX, Bored Ape #YYYY, autres collections) — valeur estimée ~200 000 USD.
- ~30 000 USDC.
- Plusieurs autres tokens DeFi.
- Total ~280 000 USD.

Karim signale immédiatement à plusieurs outils communautaires (chainabuse, OpenSea pour les NFT volés). Il mandate un cabinet privé pour enquête détaillée et soutien à plainte.

**Mandat** : 4 semaines, 20 000 EUR.

## 38.2 Phase 1 — Lecture des transactions de drainage

**Étape 1 — Adresse Karim**.

Karim fournit son adresse Ethereum : `0xKarim...`. L’analyste consulte sur Etherscan.

**Étape 2 — Identification des transactions de drainage**.

Sur la dernière demi-heure du 2026-04-15, ~15 transactions sortantes. Toutes vers une **adresse inconnue** : `0xDrainer1...`.

Examen détaillé d’une transaction type :

- TX hash : `0x...drain001`.
- From : `0xKarim`.
- To : `0xDrainer1`.
- Method : `transferFrom` appelé sur le contrat USDC.
- Logs : `Transfer(from=0xKarim, to=0xDrainer1, value=30000 USDC)`.

C’est un **transfer via approval**. Le drainer a appelé `transferFrom` parce que Karim avait préalablement signé un `approve`.

**Étape 3 — Identification de la transaction d’approve**.

L’analyste cherche dans l’historique de Karim juste avant le drainage. Trouve :

- TX hash : `0x...approve001`.
- From : `0xKarim`.
- To : USDC contract.
- Method : `approve`.
- Spender : `0xDrainer1`.
- Amount : `type(uint256).max` (illimité).
- Timestamp : 22:33 UTC (1 minute avant les drainages).

**Confirmation** : Karim a approuvé un montant illimité au drainer 1 minute avant. Pattern classique d’approval phishing.

## 38.3 Phase 2 — Analyse du drainer

**Étape 1 — Caractérisation `0xDrainer1`**.

`0xDrainer1` est analysé. Smart contract (l’analyste vérifie sur Etherscan onglet « Contract »).

**Code source vérifié** : oui, le drainer a publié son code Solidity. Analyse rapide :

- Fonctions `transferFromAll(token, victim)` qui appellent `transferFrom` avec les approvals existants.
- Fonctions de retrait pour l’opérateur.
- Pas d’audit, pas de réputation.

**Activité** :

- Smart contract déployé il y a 6 mois.
- A été utilisé par ~340 victimes différentes selon analyse Etherscan.
- Volume cumulé : ~14 M USD équivalent (estimations).

**Reconnaissance du drainer service**.

Le code et les patterns du drainer correspondent à un service connu : **« Inferno Drainer »** (drainer-as-a-service identifié par chercheurs comme @scamsniffer en 2023). Il a évolué : variantes successives, multiples déploiements.

L’analyste note : Karim n’est pas victime d’un attaquant individuel, mais d’un **service utilisé par un affilié** d’Inferno Drainer (le service prend une commission, les affiliés font la distribution / le phishing).

## 38.4 Phase 3 — Suivi des fonds

**Étape 1 — Consolidation drainer**.

Sur les 30 minutes post-drainage, `0xDrainer1` consolide vers `0xDrainerOps1` (wallet opérationnel de l’affilié) :

- ETH : 12 ETH → `0xDrainerOps1`.
- USDC : 30 000 → `0xDrainerOps1`.
- Tokens autres : converti via DEX (1inch) en ETH d’abord.
- NFT : transférés à `0xDrainerOps1` en l’état.

**Étape 2 — Suivi des NFT**.

NFT sont **traçables** publiquement (chaque NFT a un ID unique, leur historique est visible).

À J+3, les NFT sont listés sur OpenSea (depuis `0xDrainerOps1`) à des prix bas. Karim et ses contacts dans la communauté ont alerté OpenSea : les **NFT sont gelés** sur OpenSea (delisted, non-transférables sur la marketplace).

Mais : sur d’autres marketplaces moins coopératives, NFT sont vendus. À J+10, ~60% des NFT ont été vendus à des acheteurs tiers (qui les ont peut-être achetés sans savoir qu’ils sont volés).

Récupération des NFT : **complexe juridiquement**. Acheteurs tiers de bonne foi peuvent revendiquer propriété. Procédure longue.

**Étape 3 — Suivi des fonds liquides**.

ETH + USDC : `0xDrainerOps1` consolide :

- Étape A : swap USDC → ETH via Uniswap (J+0).
- Étape B : split en 4 sub-adresses (J+1).
- Étape C : 2 sub-adresses → Tornado Cash (~12 ETH au total).
- Étape D : 2 sub-adresses → bridge Stargate vers BNB Chain.
- Étape E : sur BNB, dispersion vers exchanges non-KYC.

Pattern d’obfuscation classique. ~70% via Tornado Cash, 30% via bridge.

## 38.5 Phase 4 — Identification de l’affilié

**Étape 1 — `0xDrainerOps1` historique**.

`0xDrainerOps1` n’est pas seulement utilisé pour Karim. Analyse révèle :

- Adresse active depuis 4 mois.
- A consolidé fonds de **~80 victimes** différentes.
- Volume cumulé : ~3,2 M USD équivalent.

**Étape 2 — Patterns affilié**.

Patterns observables :

- Quelques fois par semaine, drainages.
- Fonds disparaissent rapidement (Tornado Cash, bridges).
- Adresse de payment de **service Inferno Drainer** : ~10% des fonds reversés à une adresse spécifique du service (commission).
- Pas d’erreur OPSEC visible (pas de réutilisation, pas de mention publique).

**Étape 3 — Possibilité d’attribution**.

Affilié reste **anonyme** au sens civil. Patterns suggèrent acteur expérimenté.

Pas de fonds vers exchange régulé identifié — l’affilié maintient OPSEC stricte.

**Recoupement Inferno Drainer général** : selon @scamsniffer et reports vendor, certains affiliés Inferno Drainer ont été identifiés (Telegram handles, infrastructure leaks). Pour cet affilié spécifique, pas de match identifiable dans les sources publiques au moment de l’enquête.

## 38.6 Phase 5 — Coopération et action

**Étape 1 — OpenSea**.

NFT volés signalés. OpenSea a délisté les NFT compromis. **Action partielle** : les acheteurs tiers ne peuvent plus les revendre sur OpenSea. Mais marketplaces alternatives (Blur, X2Y2 historique) moins coopératives.

**Étape 2 — Coordination autorités**.

Plainte de Karim auprès de la gendarmerie. L’analyste fournit son rapport. Coordination via gendarmerie cyber → Pharos → potentiel relais vers FBI Cyber Division (drainer service est multi-juridictionnel).

**Étape 3 — Communauté**.

Information partagée sur Chainabuse. ScamSniffer alerté avec nouvelles indications sur le drainer / affilié. Alimente la base communautaire.

## 38.7 Phase 6 — Rapport et restitution

**Rapport de 25 pages** :

- Executive summary.
- Méthodologie.
- Faits Karim (timeline précise — minutes).
- Mécanisme du drainer (analyse Solidity).
- Suivi des fonds.
- Identification de l’affilié et du service.
- Limites.
- Recommandations.

**Recommandations à Karim** :

- Action prioritaire : révoquer **tous les approvals existants** sur tous ses wallets via revoke.cash.
- Migration vers nouveau wallet (assumer compromission seed phrase est peu probable mais prudent).
- Hardware wallet pour fonds significatifs.
- Vigilance sur signatures (lire toujours le détail).
- Suivre la procédure judiciaire ; espoir limité de récupération.

**Recommandations communauté** :

- Signaler le service de drainer aux outils anti-phishing.
- Alerter chercheurs (scamsniffer) avec données enrichies.

## 38.8 Bilan

✅ **Réussites** :

- Reconstitution complète du mécanisme.
- Identification du drainer-as-a-service utilisé.
- Identification de l’affilié (en tant que cluster, pas personne).
- ~60% des NFT délistsés OpenSea (limites valorisation).
- Alimentation base communautaire anti-phishing.

⚠️ **Limites** :

- Récupération financière improbable sans coopération internationale exhaustive.
- 70% des fonds liquides perdus dans Tornado Cash.
- Affilié reste anonyme.
- Acheteurs NFT tiers de bonne foi posent problème juridique pour récupération.

📊 **Métriques** :

- Durée : 4 semaines.
- Coût : 20 000 EUR.
- Récupération : indirecte (NFT délistsés sur OpenSea, mais valeur incertaine).

**Apprentissage clé** : pour wallet drain individuel, l’enquête **caractérise** mais récupère rarement. Valeur principale = clarification pour la victime et alimentation communauté.

-----
