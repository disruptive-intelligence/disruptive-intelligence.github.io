---
title: Chapitre 9 — Tokens et smart contracts
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie II — Lire les blockchains
  - index.md
---

L’écosystème crypto moderne ne se résume pas aux coins natifs. Une part majoritaire de l’activité économique on-chain passe par des **tokens** — actifs déployés via smart contracts. Comprendre tokens et smart contracts est indispensable pour ne pas rater l’essentiel d’une enquête.

## 9.1 Les standards de tokens

**ERC-20** (Ethereum). Standard pour tokens **fongibles** (interchangeables, divisibles). USDT, USDC, DAI, des dizaines de milliers d’autres. Spécification simple : `transfer`, `approve`, `transferFrom`, `balanceOf`, `totalSupply`, `allowance`. Chaque token ERC-20 est un smart contract dédié déployé sur Ethereum.

**ERC-721** (Ethereum). Standard pour **NFT** (Non-Fungible Tokens) — tokens uniques non-divisibles. Chaque token a un `tokenId` unique. CryptoPunks, BAYC, des millions d’autres.

**ERC-1155** (Ethereum). Standard hybride permettant tokens fongibles et non-fongibles dans un même contrat. Usage en gaming notamment.

**TRC-20** (TRON). Équivalent ERC-20 sur TRON. USDT-TRON est le plus important économiquement.

**BEP-20** (BNB Chain). Équivalent ERC-20 sur BNB Chain.

**SPL** (Solana Program Library). Standard tokens Solana, structure différente.

**Implications enquête** : un token est un smart contract avec une **adresse propre** sur la blockchain. Cette adresse est l’« infrastructure » du token, pas un wallet utilisateur. Confondre les deux = erreur classique.

## 9.2 Le contrat USDT sur Ethereum

Cas concret. Le contrat USDT sur Ethereum a comme adresse : `0xdAC17F958D2ee523a2206206994597C13D831ec7`.

Sur Etherscan, cette adresse :

- Est marquée « Contract ».
- A des onglets « Code », « Read Contract », « Write Contract ».
- Affiche son ABI (Application Binary Interface).

**Quand quelqu’un envoie 100 USDT à un destinataire** :

- La transaction a `From: l'expéditeur`.
- `To: 0xdAC17F958D2ee523a2206206994597C13D831ec7` (le contrat USDT).
- `Value: 0 ETH` (parce que le transfert n’est pas en ETH).
- Dans les **logs ERC-20**, on voit l’événement `Transfer(from=expéditeur, to=destinataire, value=100000000)` (USDT a 6 décimales, donc 100 USDT = 100 000 000 unités).

**Ne pas confondre** :

- L’adresse `0xdAC17...` est l’**infrastructure** USDT. Aucun utilisateur final n’a ses USDT « stockés là » au sens propre.
- Les balances utilisateurs sont stockées dans une **mapping interne** du smart contract.
- Le destinataire réel d’un transfert est dans les **logs**, pas dans le `To`.

## 9.3 Approve et allowance — le mécanisme central

Pour qu’un smart contract (DEX, lending) puisse manipuler vos tokens, vous devez lui donner une **autorisation préalable** via `approve`.

**Mécanisme** :

1. Vous appelez `approve(spender, amount)` sur le contrat token. Cela autorise `spender` à dépenser jusqu’à `amount` de vos tokens.
1. Plus tard, `spender` (souvent un DEX) appelle `transferFrom(from=vous, to=destinataire, amount)` qui transfère vos tokens.

**Cas légitime** : utiliser Uniswap pour échanger USDT contre ETH. Vous approuvez Uniswap pour dépenser X USDT. Uniswap exécute le swap via `transferFrom`.

**Cas malveillant — drainer** : un site de phishing imitant une plateforme légitime vous demande de signer un `approve` pour un montant **illimité** (`type(uint256).max`). Une fois la signature obtenue, le drainer (smart contract du scammer) peut vider tous vos tokens à tout moment via `transferFrom`.

**Implications enquête** :

- Investigation d’un wallet drain : toujours regarder l’historique des **approvals** de la victime. Quel contrat a-t-elle approuvé ? Quand ? Pour quel montant ?
- Reconnaître une transaction de drain : le contrat malveillant appelle `transferFrom` quelques minutes/heures après l’`approve` de la victime, vide les tokens.
- Outils : `revoke.cash` permet à un utilisateur de **révoquer** des approvals existants. Pour l’analyste, l’historique des approvals d’une adresse est une mine d’information.

## 9.4 Lire les logs ERC-20

Sur Etherscan, l’onglet **Logs** d’une transaction affiche tous les événements émis par les smart contracts appelés.

Format type d’un Transfer ERC-20 :

```
Address: 0xdAC17F958D2ee523a2206206994597C13D831ec7 (USDT)
Name: Transfer (index_topic_1 address from, index_topic_2 address to, uint256 value)
Topics:
  0: 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef (signature de l'event Transfer)
  1: 0x000...0xExpediteur
  2: 0x000...0xDestinataire
Data:
  0x0000...montant en hex
```


**Décodage** :

- `Address` : le contrat émetteur de l’event = le contrat token (ici USDT).
- `from` et `to` : les vraies parties du transfert.
- `value` : montant en plus petite unité du token. Pour USDT (6 décimales), 100000000 = 100 USDT.

Etherscan **décode automatiquement** ces events si l’ABI du contrat est publié, ce qui simplifie la lecture humainement. Mais comprendre le format brut est utile pour parser massivement (scripts) ou analyser des contrats sans ABI publique.

## 9.5 Smart contracts : risques et opportunités d’enquête

**Smart contract** = code immutable déployé sur la blockchain. Une fois déployé, peut être appelé par n’importe qui (selon les permissions définies).

**Pour l’enquête** :

**Code souvent vérifié et public**. Les développeurs « vérifient » leur contrat sur Etherscan en publiant le code source Solidity. L’analyste peut **lire le code** pour comprendre la logique. Particulièrement utile pour analyser les drainers, exploits, fraudes.

**Code non-vérifié = drapeau rouge**. Un contrat sans code vérifié est plus suspect. L’analyste doit alors lire le **bytecode** (langage machine EVM) ou **désassembler**, beaucoup plus difficile.

**Honeypot tokens**. Token déployé avec code malveillant : la fonction `transfer` est altérée pour empêcher les acheteurs de revendre. L’analyse du code révèle le piège (souvent via condition cachée : seul le créateur peut transferer, blacklist abusive, taxe à 100%, etc.).

**Backdoors et privilèges**. Beaucoup de contrats ont des fonctions « owner-only » (mint, burn, pause, blacklist). L’analyste vérifie qui détient l’ownership et si le contrat est « renoncé » (ownership transférée à 0x0).

**Outils d’analyse smart contract** :

- **Etherscan Read/Write Contract** : interface basique d’inspection.
- **Tenderly** : simulation et debugging avancé.
- **Phalcon (BlockSec)** : forensique de transactions complexes.
- **GoPlus, Token Sniffer** : analyse automatique de tokens (détection de honeypots).
- **DeFiSafety, CertiK** : audits publics.

## 9.6 Phishing par smart contract

Les attaques par smart contract phishing sont devenues un vecteur majeur 2022-2026.

**Schémas typiques** :

**Faux site DEX**. L’utilisateur croit interagir avec Uniswap, signe un `approve` pour un drainer.

**Faux mint NFT**. Site qui propose de minter un NFT « gratuit » mais demande l’approval de tokens existants.

**Faux airdrop**. Notification d’airdrop, l’utilisateur doit « claim » via signature qui en réalité approuve un drainer.

**Walletconnect malveillant**. Faux dApp connecté qui demande des signatures abusives.

**EIP-712 / signature de message**. Au lieu d’une transaction visible, l’attaquant fait signer un **message off-chain** (EIP-712). La signature est ensuite utilisée on-chain pour drainer. Plus subtil parce que l’utilisateur croit « juste signer un message ».

**Investigation post-drain** :

- Identifier l’adresse drainer (qui a appelé `transferFrom`).
- Tracer où vont les fonds drainés (souvent vers mixer ou bridge).
- Si le drainer est public, analyser le code pour comprendre la mécanique.
- Identifier le **draining service** sous-jacent (services-as-a-service comme Inferno Drainer, Pink Drainer, Angel Drainer en 2023-2024 — multiples variantes ensuite).

## 9.7 Fil rouge — MIXSHADOW : analyse smart contract Tornado

> **🔗 MIXSHADOW — Épisode 6 : Tornado Cash inspection**
> 
> Sarah continue MIXSHADOW. Elle a identifié plusieurs dépôts Tornado Cash de la branche Ethereum. Avant d’analyser les sorties potentielles (Ch.31), elle veut comprendre **précisément** ce qui s’est passé.
> 
> Elle ouvre la transaction de dépôt Tornado Cash sur Etherscan :
> 
> - Hash : `0xdef...456`.
> - From : `0xAk1...` (adresse de Akira sur Ethereum).
> - To : `0x910Cbv...` (Tornado Cash 10 ETH pool, contrat connu).
> - Value : 10 ETH.
> - Status : Success.
> 
> **Logs** : un événement `Deposit` émis par le contrat Tornado, contenant un **commitment** (hash cryptographique).
> 
> Sarah note : Tornado Cash fonctionne par **pools de montants fixes** (0,1 ETH, 1 ETH, 10 ETH, 100 ETH). Akira a utilisé le pool 10 ETH × 2 + le pool 1 ETH × 2 pour anonymiser les 12 ETH (en pratique, légèrement moins parce que des frais de gaz s’appliquent).
> 
> Le **commitment** est un engagement cryptographique. Pour retirer, l’utilisateur fournira un **proof zero-knowledge** prouvant qu’il connaît le secret correspondant à un commitment dans la pool, sans révéler **lequel**. C’est la magie cryptographique de Tornado Cash.
> 
> Sarah documente :
> 
> - Le **dépôt** est observable on-chain (qui a déposé, quand, combien).
> - Le **retrait correspondant** (somewhere later) sera observable on-chain (qui retire, quand, combien) — mais **non-liable au dépôt** sans information additionnelle.
> - Il existe néanmoins des **techniques d’analyse statistique** pour réduire l’incertitude (timing analysis, montants atypiques, comportement post-retrait). Ch.31 détaillera.
> 
> Sarah ajoute aux indices MIXSHADOW : **timestamp précis du dépôt**, **gas price** payé (signe d’urgence ou non), **nonce** de l’adresse Akira au moment du dépôt (combien d’autres opérations elle a faites avant et après), **adresses adjacentes** dans le bloc (qui d’autre déposait à Tornado Cash dans le même bloc, créant des co-occurrences potentiellement exploitables).
> 
> Cette analyse fine n’est pas du « lire un explorateur ». C’est du **raisonnement crypto-forensique** : comprendre la mécanique du smart contract, identifier les signaux exploitables, documenter ce que les données permettent de faire et ne pas faire.
> 
> Au passage, Sarah note pour l’attribution Akira : **utilisation de Tornado Cash post-sanctions OFAC (août 2022)**. Akira accepte donc d’utiliser un service sanctionné, ce qui contraint les off-ramps possibles (la plupart des exchanges régulés bloquent les fonds tracés à Tornado). Signal sur le profil opérationnel d’Akira.

-----
