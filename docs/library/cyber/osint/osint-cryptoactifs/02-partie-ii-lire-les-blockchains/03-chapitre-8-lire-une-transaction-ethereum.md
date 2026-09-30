---
title: Chapitre 8 — Lire une transaction Ethereum
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie II — Lire les blockchains
  - index.md
---

Ethereum a un modèle radicalement différent de Bitcoin. La lecture demande des réflexes nouveaux. Ce chapitre couvre les transactions Ethereum natives, l’usage du gas, et les pièges classiques.

## 8.1 Anatomie d’une transaction Ethereum

Une transaction Ethereum a la structure suivante :

```
Transaction Hash: 0xabc123...def
Block: 19 234 567
Timestamp: 2026-03-14 14:23:11 UTC
Status: Success ✓

From: 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb1
To: 0x8e9F23456...A1B2C3
Value: 1.5 ETH

Nonce: 142
Gas Limit: 21 000
Gas Price: 25 gwei
Gas Used: 21 000 (100%)
Transaction Fee: 0.000525 ETH ($1.25 at the time)
```


**Concepts clés** :

**From** : adresse émettrice (signataire). Une seule.

**To** : adresse destinataire. Une seule (peut être un wallet ou un smart contract).

**Value** : montant ETH transféré. Peut être 0 si la transaction appelle un smart contract sans transférer ETH directement.

**Nonce** : numéro séquentiel de la transaction pour cette adresse émettrice. Empêche le rejeu.

**Gas** : « carburant » consommé. `Gas Used` × `Gas Price` = `Transaction Fee`.

**Status** : Success ou Failed. Une transaction Failed paie quand même les frais (gas consommé) mais l’effet voulu n’a pas eu lieu.

**Pas d’UTXO**. Le modèle est **account-based** : chaque adresse a un solde direct stocké dans la blockchain. Une transaction modifie deux soldes (from -= value, to += value) plus les frais.

## 8.2 Différences avec Bitcoin

**Source unique vs multiple inputs**. Une transaction Ethereum a **un seul émetteur**. Pas de co-spending Bitcoin-style. Heuristique de clustering différente.

**Pas de change**. Pas besoin d’adresse change — la blockchain met à jour directement les soldes.

**Smart contracts comme destinataires**. Le `To` peut être un smart contract qui exécute du code. Cela ouvre des possibilités énormes (DeFi, NFT) et complexifie la lecture.

**Gas variable**. Le coût d’une transaction dépend de sa complexité. Un simple transfer ETH = 21 000 gas. Une interaction smart contract complexe peut consommer 500 000+ gas.

**Tokens omniprésents**. Beaucoup de « valeur » sur Ethereum est dans des tokens (USDT, USDC, etc.) — pas dans ETH. Une transaction qui transfère 100 000 USDT a Value = 0 ETH (parce que la valeur est dans le token, pas dans ETH).

## 8.3 Lire une transaction Ethereum sur Etherscan

**Etherscan.io** est l’explorateur de référence Ethereum. Walkthrough.

**1. Coller un transaction hash** dans la barre de recherche.

**2. Onglet « Overview »** :

- Status, Block, Timestamp.
- From, To.
- Value (ETH transféré natif).
- Transaction Fee.
- Gas Price.

**3. Onglet « Logs »** :

- **Events émis par les smart contracts** appelés. Crucial pour les transferts de tokens.
- Format : event name, paramètres, topics, data.

**4. Onglet « State »** :

- Modifications d’état (avancé).

**5. Onglet « Comments »** :

- Notes communautaires (rare).

**6. Section « ERC-20 Tokens Transferred »** :

- Si la transaction a déclenché des transferts de tokens, ils sont listés ici.
- Format : `From → To, Amount, Token (Symbol)`.

**7. Section « ERC-721 Tokens Transferred »** :

- Pour les NFT.

**8. Section « Internal Transactions »** :

- **Très important**. Les internal transactions sont les **appels entre smart contracts** déclenchés par la transaction principale. Elles ne sont **pas** des transactions séparées au sens propre, mais des effets internes.
- Format : Type (call, delegatecall, etc.), From, To, Value.

## 8.4 La piège des internal transactions

**Erreur classique** : regarder l’onglet Overview, voir « Value: 0 ETH », et conclure « pas de transfert de valeur ».

**Réalité** : la transaction peut avoir déclenché :

- Des **transferts de tokens** (USDT, USDC) dans les logs ERC-20.
- Des **internal transactions** transférant ETH entre smart contracts.
- Des **ERC-721 transfers** (NFT).

Sans regarder ces sections, on **rate** la majeure partie de l’activité économique de la transaction.

**Exemple concret** : une transaction d’achat d’NFT typique :

- Value : 0 ETH (l’utilisateur n’envoie pas directement d’ETH au vendeur).
- Mais : ETH transféré via internal transactions du smart contract de marketplace vers le vendeur.
- Et : ERC-721 transféré du vendeur à l’acheteur.
- Et : éventuels frais transférés à la marketplace.

Tout ça sur **une seule transaction** principale. Lire correctement nécessite de regarder logs + internal transactions + token transfers.

## 8.5 Le nonce et son intérêt

Le **nonce** est un compteur séquentiel par adresse. La première transaction d’une adresse a nonce 0, la deuxième nonce 1, etc.

**Implications enquête** :

**Confirmer l’auteur**. Le nonce séquentiel signifie qu’on peut savoir « combien de transactions cette adresse a déjà fait au moment de cette transaction ». Si une adresse fait sa transaction nonce 1, c’est sa **2ème transaction** de toute son histoire.

**Détecter des transactions fail**. Si une adresse a une transaction nonce N qui Fail, la prochaine transaction sera nonce N+1 (le nonce a été consommé même en cas d’échec). Voir des trous dans la séquence d’une adresse = drapeau d’investigation.

**Reconnaître l’activité d’un wallet**. Une adresse à nonce élevé (1000+) est une adresse **très active** (probable hot wallet de service). Une adresse à nonce 1 est presque vierge.

**Détection anomalie**. Une adresse avec activité importante (gros volumes) mais nonce faible (3-5 transactions) est suspicieuse — pourquoi un wallet récemment créé manipule-t-il déjà des montants significatifs ?

## 8.6 Les transactions « Failed »

Une transaction Ethereum peut **Fail** (échouer) : par exemple, si le smart contract appelé revert (annule l’opération). Le gas est tout de même consommé.

**Pourquoi voir des transactions Failed est utile** :

**Détection de tentatives de phishing/drainer**. Un drainer mal configuré peut faire fail. La transaction est visible mais sans transfert de valeur.

**Reconnaissance de tests**. Un attaquant peut tester sa logique en envoyant des transactions tests qui fail. Les nonce qui suivent pas un gap sont les vraies tentatives.

**Diagnostic d’erreur logique**. Pour analyser un hack DeFi, voir la séquence des transactions Failed avant Success peut révéler la logique exploit utilisée.

## 8.7 Erreurs classiques

**Ignorer les ERC-20 transferts**. Voir « Value: 0 ETH » et conclure qu’aucune valeur n’a bougé. Toujours regarder la section ERC-20 Tokens Transferred.

**Ignorer les internal transactions**. Pour les transactions impliquant des smart contracts, le mouvement réel d’ETH se fait souvent en internal.

**Confondre token contract et wallet**. L’adresse `0xdAC17F958D2ee523a2206206994597C13D831ec7` est le **contrat USDT** sur Ethereum. Ce n’est pas un wallet d’utilisateur — c’est l’infrastructure. Une transaction qui « envoie 100 USDT » a comme `To` cette adresse, mais le **destinataire réel** (qui reçoit les 100 USDT) est dans les logs ERC-20.

**Penser que `To = destinataire`**. Pour les interactions smart contract, `To` est le contrat appelé, pas le destinataire final de la valeur.

**Ignorer le contexte des chains**. Un transfer USDT sur Ethereum a une logique. Le même transfer sur BNB Chain a une logique similaire mais pas identique (frais différents, timings différents). L’analyste vérifie toujours **sur quelle chaîne** il regarde.

## 8.8 Outils Ethereum

**Etherscan.io** : référence absolue.

**Tenderly.co** : pour debugging avancé de transactions complexes (DeFi, exploits).

**Phalcon (BlockSec)** : analyse forensique de transactions complexes, simulation.

**EigenPhi** : analytics MEV (Maximal Extractable Value), arbitrage.

**Dune Analytics** : dashboards SQL personnalisables sur la blockchain.

**Bloxy** : explorer alternatif avec analytics.

**DeBank** : portfolio explorer multi-chain.

**Chainalysis Reactor / TRM Labs** : pour Ethereum aussi (Ch.20).

## 8.9 Fil rouge — MIXSHADOW : un détour par Ethereum

> **🔗 MIXSHADOW — Épisode 5 : un peeling vers Ethereum**
> 
> Sarah continue de suivre les flux Akira sur Bitcoin. Le 19 mars, elle observe quelque chose de différent : une des adresses externes éplutchées (vers laquelle 0,8 BTC ont été envoyés en sortie de peeling chain, hop 7) est une **adresse exchange** étiquetée par Chainalysis comme « FixedFloat hot wallet ».
> 
> **FixedFloat** est un service de swap crypto **non-KYC**, populaire dans les flux illicites. Il permet de convertir un actif en un autre (BTC → ETH par exemple) sans création de compte ni vérification d’identité, en quelques minutes.
> 
> Sarah pose l’hypothèse : Akira utilise FixedFloat pour convertir partiellement les BTC en ETH, probablement en route vers Tornado Cash ou un autre service Ethereum.
> 
> Sarah suit la suite. Sur la blockchain Ethereum, en croisant les timestamps, elle identifie une transaction Ethereum avec :
> 
> - **Hash** : `0xabc...123`.
> - **Timestamp** : 2026-03-19 11:43 UTC (cohérent avec un swap FixedFloat ~10 minutes après le dépôt BTC).
> - **From** : adresse FixedFloat.
> - **To** : `0xAk1...` (nouvelle adresse, fraîche).
> - **Value** : ~12,5 ETH (cohérent avec swap de 0,8 BTC à taux de marché du moment, moins frais).
> 
> Sarah ouvre cette transaction sur Etherscan :
> 
> - Status : Success.
> - Logs : pas d’événements ERC-20 (transfer ETH natif simple).
> - Internal transactions : aucune.
> 
> Lecture simple : 12,5 ETH transférés de FixedFloat hot wallet vers `0xAk1...`. Cette adresse est désormais dans le périmètre MIXSHADOW.
> 
> Sarah suit `0xAk1...`. Quelques heures plus tard, elle observe une transaction sortante :
> 
> - Value : 0 ETH (suspect au premier abord).
> - To : `0x47CE...` (adresse smart contract).
> - Section logs : ERC-20 Token Transferred — **12 ETH transférés vers Tornado Cash 10 ETH pool**.
> 
> Sarah identifie **deux dépôts Tornado Cash de 5 ETH** + **un dépôt de 2 ETH résiduel**. Akira a utilisé Tornado Cash pour anonymiser une partie des fonds.
> 
> **Implication enquête** : à partir du dépôt Tornado Cash, la **traçabilité directe est cassée** (Ch.31 expliquera Tornado Cash). L’analyse va se déplacer vers l’analyse statistique des sorties Tornado Cash pour tenter d’identifier les retraits correspondants — possible mais probabiliste.
> 
> Sarah documente cette branche du flux. Le graphe MIXSHADOW commence à montrer la complexité réelle : Bitcoin (peeling chain) → FixedFloat (swap) → Ethereum (transfert) → Tornado Cash (anonymisation). Quatre étapes, deux chaînes, plusieurs services. Et c’est juste **une** des branches éplutchées du peeling chain initial.
> 
> Le métier de crypto-forensique se révèle dans ces enchaînements multi-chaînes. Ch.9 va détailler les tokens et smart contracts, qui sont au cœur de l’écosystème Ethereum et des flux illicites.

-----
