---
title: PARTIE II — LIRE LES BLOCKCHAINS
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
chapter: 3
chapters: 10
---

> **Ce que cette partie apprend.** Lire concrètement les blockchains majeures. Décortiquer une transaction Bitcoin, comprendre le modèle UTXO, lire une transaction Ethereum, manipuler tokens et smart contracts, maîtriser les stablecoins et leur logique opérationnelle, naviguer dans les explorateurs.
> 
> **Ce qu’elle ne couvre pas.** Les méthodes d’enquête (Partie III), les outils professionnels (Partie IV), les techniques d’obfuscation (Partie VI).
> 
> **Ce que vous saurez faire après cette partie.** Lire une transaction Bitcoin sans confondre change et destinataire, interpréter une transaction Ethereum incluant transferts de tokens et internal transactions, comprendre pourquoi un même actif (USDT) se comporte différemment selon la blockchain, et naviguer fluidement Mempool/Etherscan/Tronscan.

-----

## Chapitre 6 — Lire une transaction Bitcoin

Bitcoin est la blockchain la plus ancienne, la plus étudiée, et celle dont l’analyse a le corpus de connaissances le plus mature. Mais sa lecture demande un changement mental par rapport au modèle bancaire classique. Ce chapitre apprend à lire une transaction Bitcoin sans erreur d’interprétation — en particulier la confusion fréquente entre **destinataire** et **adresse de change**.

### 6.1 Anatomie d’une transaction Bitcoin

Une transaction Bitcoin a la structure suivante :

```
Transaction TXID: e3a5f9a8c1b2d4e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0
Block height: 825 432
Timestamp: 2026-03-14 09:12:34 UTC
Confirmations: 6+

INPUTS:
  Input 0:
    From: bc1qsource1address...
    Amount: 0.4 BTC
  Input 1:
    From: bc1qsource2address...
    Amount: 0.6 BTC
  Total inputs: 1.0 BTC

OUTPUTS:
  Output 0:
    To: bc1qdestination...
    Amount: 0.7 BTC
  Output 1:
    To: bc1qchange...
    Amount: 0.299 BTC

Fee: 0.001 BTC (= total inputs - total outputs)
```

**Concepts clés** :

**Inputs** : références à des outputs **précédents** (UTXO non dépensés) que cette transaction va consommer. Chaque input pointe vers un TXID + index d’output dans une transaction antérieure. L’expéditeur prouve qu’il contrôle ces UTXO en signant.

**Outputs** : nouveaux UTXO créés par cette transaction. Chacun assigne un montant à une adresse destinataire.

**Frais (fees)** : différence entre total inputs et total outputs. Va aux mineurs qui valident le bloc.

**Pas de notion de « solde »** explicite dans Bitcoin. Une adresse a un solde **calculé** comme la somme de ses UTXO non dépensés.

### 6.2 La confusion classique : destinataire vs change

Reprenons l’exemple ci-dessus. Une lecture **naïve** dirait :

- L’expéditeur a envoyé 1 BTC à 2 destinataires : 0,7 BTC à `bc1qdestination` et 0,299 BTC à `bc1qchange`.
- Donc deux destinataires.

**Cette lecture est très probablement fausse**. La réalité, dans la grande majorité des cas :

- **Le vrai destinataire** est `bc1qdestination` qui reçoit 0,7 BTC.
- **`bc1qchange` est une adresse de change** : c’est une adresse contrôlée par **l’expéditeur lui-même**, qui récupère le « rendu de monnaie ». L’expéditeur avait des UTXO totalisant 1 BTC mais voulait n’envoyer que 0,7 BTC, donc il s’envoie 0,299 BTC à lui-même (le reste 0,001 BTC va aux frais).

**Pourquoi ce mécanisme ?** Bitcoin est **UTXO**. On ne peut pas « dépenser une partie d’un UTXO » — on consomme l’UTXO entier et on en crée de nouveaux. Si vous avez un UTXO de 1 BTC et voulez envoyer 0,7 BTC, vous devez consommer le UTXO de 1 BTC entier, créer un output de 0,7 BTC pour le destinataire, et un output de 0,299 BTC qui revient à vous (moins les frais).

**Erreur classique de lecture** : conclure que `bc1qchange` est un destinataire distinct, l’ajouter au graphe d’enquête comme entité séparée, le suivre comme un acteur indépendant. C’est une erreur **fondamentale** qui pollue toute l’enquête.

### 6.3 Reconnaître l’adresse de change

Plusieurs heuristiques permettent d’identifier l’adresse de change.

**Heuristique du nouveau wallet**. Le change va typiquement vers une **nouvelle adresse fraîchement générée** (jamais utilisée auparavant). Les adresses « destinataires » sont plus souvent réutilisées. Si dans une transaction vous avez deux outputs et que l’un pointe vers une adresse fraîche jamais vue, c’est probablement le change.

**Heuristique du round number**. Le destinataire reçoit souvent un **montant rond** (1 BTC, 0,5 BTC, 0,1 BTC). Le change reçoit un montant non-rond (0,299 BTC dans l’exemple). Si vous voyez `0,7000` et `0,2998` en outputs, le `0,7000` est très probablement le destinataire.

**Heuristique du script type**. Le change utilise **généralement le même type d’adresse** que les inputs (P2PKH, P2SH, SegWit, Taproot). Le destinataire peut être de type différent. Heuristique faible isolément, plus forte combinée.

**Heuristique du wallet client**. Certains wallets (Electrum, par exemple) ont des patterns comportementaux récurrents dans la sélection d’adresses de change. Un analyste expérimenté reconnaît parfois le wallet utilisé d’après la structure.

**Limitation** : aucune de ces heuristiques n’est **certaine**. Chacune a un taux d’erreur. Les outils professionnels (Chainalysis, TRM, Elliptic) combinent plusieurs heuristiques + ML pour scorer la probabilité.

### 6.4 Les inputs multiples : co-spending

Dans l’exemple, la transaction consomme deux inputs (0,4 BTC + 0,6 BTC). C’est le **co-spending**.

**Heuristique du co-spend (« common-input ownership »)** : si plusieurs inputs sont dépensés ensemble dans une même transaction, ils sont **probablement contrôlés par la même entité**. Pourquoi ? Parce que dépenser plusieurs UTXO ensemble nécessite de signer chacun avec sa clé privée. Une entité qui ne contrôle pas les deux clés ne peut pas faire cette transaction.

**Forte mais pas absolue** : exceptions notables :

- **CoinJoin** : protocole coopératif où plusieurs parties signent ensemble une transaction sans partager les clés (Ch.32). Dans un CoinJoin, les inputs **ne sont PAS contrôlés par la même entité**. Heuristique caduque.
- **Multi-sig collaboratif** : plus rare mais existe.
- **Transactions exchange** : un exchange agrège les fonds de plusieurs utilisateurs dans des UTXO, puis les re-dispatche. Le co-spending au niveau exchange ne dit rien sur les utilisateurs finaux.

L’heuristique du co-spend est **la base du clustering Bitcoin**. Les outils modernes l’appliquent en masse pour regrouper des millions d’adresses en clusters d’entité probable.

### 6.5 Lire une transaction sur Mempool.space

**Mempool.space** est un excellent explorateur Bitcoin gratuit, open source, populaire dans la communauté. Walkthrough de lecture.

**1. Ouvrir mempool.space**. Page d’accueil avec mempool actuel, transactions récentes, statistiques.

**2. Coller un TXID** dans la barre de recherche. La page transaction s’affiche.

**3. Ce qu’on voit** :

- **Header** : block height, timestamp, confirmations.
- **Inputs** : liste avec adresse source, montant, lien vers transaction d’origine.
- **Outputs** : liste avec adresse destinataire, montant.
- **Fee** : frais payés.
- **Size** : taille de la transaction en octets (impacte les fees).
- **Vsize** : virtual size (compte SegWit).

**4. Naviguer**. En cliquant sur une adresse, on accède à sa page :

- Solde actuel.
- Historique des transactions (entrantes et sortantes).
- Première transaction (date « d’apparition » de l’adresse).
- Dernière activité.

**5. Outils additionnels Mempool** :

- Visualisation graphique de la transaction.
- Mempool actuel et estimation des frais.
- Analyse de blocs.
- API gratuite pour scripts.

**Bonne pratique** : pour chaque transaction d’enquête, **capturer la page** (Hunchly ou équivalent), noter le TXID dans le journal, hasher la capture. Les blockchains sont immutables mais les explorateurs peuvent évoluer (UI, données enrichies).

### 6.6 Erreurs classiques

**Confondre destinataire et change**. Déjà détaillé. Erreur la plus fréquente.

**Ignorer les frais**. Un input de 1 BTC qui produit des outputs totalisant 0,999 BTC : ce n’est pas un « 0,001 BTC perdu », c’est les frais.

**Confondre montant brut et montant net**. Si vous regardez `bc1qsource1` qui a un input de 0,4 BTC dans une transaction, ce 0,4 BTC est le **UTXO consommé**, pas nécessairement « le montant envoyé par cette adresse ». Le montant net envoyé dépend des outputs.

**Mal interpréter une consolidation**. Un wallet peut **consolider** : prendre 50 petits UTXO et les regrouper en un seul gros UTXO (output unique vers une adresse contrôlée par le même wallet). C’est une opération **interne** au wallet, pas un transfert. Sans heuristique, on peut croire à un envoi de 50 sources vers un destinataire.

**Confondre adresse et personne**. Rappel : une adresse peut être contrôlée par plusieurs personnes (multisig), une personne contrôle souvent des dizaines d’adresses, un service exchange agrège des milliers d’utilisateurs derrière quelques hot wallets.

**Ignorer les fuseaux horaires**. Les timestamps sont en UTC. Si vous documentez « la transaction de 9h12 », précisez « 09:12 UTC, soit 10:12 heure de Paris ». Sinon confusion garantie quand vous corroborez avec des logs internes (bancaires, applicatifs).

**Sur-attribuer trop tôt**. Voir un cluster de 50 adresses ne dit pas qui les contrôle. Documenter le cluster = OK. Conclure « ces adresses appartiennent à X » = pas OK sans preuve externe.

### 6.7 Fil rouge — MIXSHADOW : la transaction de paiement

> **🔗 MIXSHADOW — Épisode 3 : lecture du paiement**
> 
> Sarah ouvre mempool.space et entre le TXID fourni par Aurélien Médical : `[TXID fictif 64 chars]`.
> 
> Page transaction :
> 
> - **Block height** : 873 245.
> - **Timestamp** : 2026-03-14 09:12:34 UTC.
> - **Confirmations** : 156 (bien finalisée).
> 
> **Inputs** : 4 inputs depuis 4 adresses contrôlées par Aurélien Médical (wallet d’urgence approvisionné en interne pour le paiement). Total inputs : 35,002 BTC.
> 
> **Outputs** : 1 seul output. 35,000 BTC vers `bc1q[adresse Akira fictive]`. Pas de change — Aurélien Médical avait approvisionné exactement 35,002 BTC, le 0,002 BTC va aux frais.
> 
> Sarah note l’adresse Akira comme **point de départ** de l’enquête. Elle clique sur cette adresse pour voir son historique :
> 
> - **Première transaction** : 2026-03-14 09:12 — exactement le paiement Aurélien Médical. Adresse **fraîche**.
> - **Solde actuel** : 35,000 BTC (inchangé pour l’instant).
> - **Aucune autre transaction** avant ou après. Adresse à usage unique pour ce paiement.
> 
> **Hypothèse initiale** (non confirmée) : Akira utilise probablement des **adresses uniques par victime** (pratique courante en RaaS pour cloisonner et faciliter la comptabilité interne). Cette adresse est dédiée Aurélien Médical.
> 
> Sarah capture la page Mempool.space (Hunchly), exporte le détail de la transaction en CSV, hashe le tout, et alimente le journal MIXSHADOW. Premier nœud du graphe documenté.
> 
> Question naturelle suivante : **où vont aller ces 35 BTC ?** L’adresse n’a encore rien envoyé au moment de la lecture initiale (14 mars). Sarah configure une **alerte de monitoring** sur Chainalysis et TRM Labs : elle sera notifiée dès que cette adresse fait une transaction sortante. En attendant, elle continue son cadrage et son setup.
> 
> Ch.7 va détailler le modèle UTXO en profondeur — utile car les 35 BTC vont, dans les jours qui suivent, transiter à travers de multiples transactions, et leur lecture exigera la maîtrise complète du modèle.

-----

## Chapitre 7 — Le modèle UTXO en profondeur

Comprendre le modèle UTXO sans erreur est la condition pour ne pas se perdre dans les flux Bitcoin. Ce chapitre dépasse les bases du Ch.6 pour aborder les patterns avancés : peeling chains, consolidation, splits, et les heuristiques fines.

### 7.1 La logique UTXO

Reprenons. Dans le modèle UTXO :

- Une « adresse » n’a pas de solde stocké comme variable. Son solde est **calculé** à la volée comme la somme des UTXO non dépensés qui lui sont assignés.
- Une transaction **consomme** des UTXO existants (les inputs) et **crée** de nouveaux UTXO (les outputs).
- Un UTXO est soit **non-dépensé** (UTXO actif, partie du « set UTXO ») soit **dépensé** (consommé par une transaction ultérieure).

**Implications pour l’enquête** :

L’historique d’une adresse est un **graphe** : les transactions qui ont créé des UTXO vers cette adresse, les transactions qui ont consommé ces UTXO. Pour chaque UTXO assigné à l’adresse, on peut dire « il a été créé par TX1 et consommé par TX2 ».

L’analyste qui veut comprendre **« d’où viennent les BTC actuellement à l’adresse X »** suit, pour chaque UTXO non-dépensé, la transaction qui l’a créé, puis remonte à ses inputs, etc. C’est ce qu’on appelle **« remonter la chaîne UTXO »**.

### 7.2 Le peeling chain — le pattern de blanchiment classique

Un **peeling chain** est un pattern où une grosse somme initiale est **progressivement épluchée** : chaque transaction laisse un petit montant à un destinataire et le reste continue vers une nouvelle adresse contrôlée par la même entité.

**Exemple** :

- **TX1** : 100 BTC en input. Outputs : 1 BTC vers exchange A, 99 BTC vers nouvelle adresse W1 (interne).
- **TX2** (depuis W1) : 99 BTC en input. Outputs : 1 BTC vers exchange B, 98 BTC vers nouvelle adresse W2 (interne).
- **TX3** (depuis W2) : 98 BTC en input. Outputs : 0,5 BTC vers exchange C, 97,5 BTC vers W3.
- … et ainsi de suite, sur des dizaines de transactions.

**Pourquoi faire ça ?** Plusieurs raisons :

- **Petits dépôts plus discrets** : un dépôt de 1 BTC sur un exchange déclenche moins d’alerte qu’un dépôt de 100 BTC.
- **Multiple exchanges** : diversifier les off-ramps pour ne pas être bloqué par une seule plateforme.
- **Brouiller l’analyse linéaire** : chaque pas est une nouvelle adresse, l’enquêteur doit suivre.
- **Time delay** : étaler dans le temps réduit la probabilité d’alerte coordonnée.

**Identification d’un peeling chain** :

- **Pattern** : à chaque transaction, un petit output « spent » (vers une adresse externe, souvent un exchange) et un gros output « change » (vers une nouvelle adresse interne).
- **Adresse change toujours fraîche**.
- **Continuité** : les adresses change forment une chaîne — chacune ne reçoit qu’une fois (de la transaction précédente) et envoie une fois (vers la suivante).
- **Montants décroissants** progressivement.

**Reconstitution de la chaîne** : avec les outils, suivre la chaîne de change adresses jusqu’à son extinction. Les outils professionnels visualisent automatiquement les peeling chains.

**Cas réels** : nombreux cas de blanchiment ransomware utilisent peeling chains. Cas Bitfinex (Ch.41) en est emblématique avec des chaînes étalées sur des années.

### 7.3 La consolidation

Inverse du peeling : la **consolidation** regroupe plusieurs UTXO en un seul.

**Exemple** :

- 50 UTXO existent à 50 adresses différentes (toutes contrôlées par la même entité — souvent un wallet ou un exchange).
- Une transaction prend les 50 UTXO en inputs et les consolide en 1 ou 2 gros UTXO en output.

**Pourquoi consolider ?** :

- **Réduire les frais futurs** : consommer un seul gros UTXO coûte moins qu’en consommer 50 petits.
- **Préparer un gros transfert** : avant un envoi de 100 BTC, il faut avoir des UTXO totalisant au moins 100 BTC.
- **Maintenance de wallet** : exchange qui consolide les dépôts utilisateurs vers ses cold storage.

**Pour l’analyste** :

- La consolidation est un **signal fort de clustering** : les 50 inputs co-dépensés sont probablement contrôlés par la même entité (heuristique multi-input).
- Elle peut révéler le **wallet sous-jacent** : reconnaître les patterns de consolidation d’un exchange (ex : Coinbase consolide selon une cadence et des seuils particuliers).
- Différencier **consolidation interne** (exchange agrégeant les fonds utilisateurs) **vs consolidation utilisateur final** : implications différentes pour l’enquête.

### 7.4 Les splits

Un **split** dispatche un UTXO vers de multiples destinataires en une seule transaction.

**Exemple** :

- Input : 100 BTC.
- Outputs : 5 BTC × 20 destinataires différents.

**Cas légitimes** :

- Paiements de salaires d’une entreprise crypto.
- Distribution de token holders.
- Airdrops.

**Cas illicites** :

- **Distribution post-hack** : après un vol, attaquant disperse vers plusieurs wallets pour brouiller.
- **Flow de blanchiment** : envoi vers plusieurs comptes d’exchanges pour off-ramp diversifié.
- **Mixer output** : sortie de mixer custodial vers plusieurs adresses.

**Lecture** : un split avec des montants similaires et destinataires sans pattern commun évident = signal à investiguer. Suivre **chaque destinataire** pour cartographier la dispersion.

### 7.5 Heuristiques avancées de clustering

Au-delà du co-spend (Ch.6), plusieurs heuristiques affinent le clustering Bitcoin.

**Heuristique de l’adresse change moderne**. Avec SegWit et Taproot, les wallets utilisent généralement le **même type d’adresse** pour le change que pour les inputs. Si une transaction a inputs en P2WPKH (SegWit native, `bc1q...`) et un output en P2WPKH (probable change) + un output en P2PKH (`1...`, probable destinataire), l’output P2WPKH est très probablement le change.

**Heuristique du montant exact**. Si un montant en output correspond exactement à un montant communément requis pour un service (ex : 0,5 BTC pour un dépôt minimum exchange), c’est un signal pour le destinataire. Le change a un montant « calculé » non-rond.

**Heuristique des adresses jamais réutilisées**. Les wallets modernes (BIP-32 hierarchical deterministic) génèrent une nouvelle adresse pour chaque transaction. Si une adresse n’est utilisée qu’une fois (recevoir une transaction et envoyer immédiatement), c’est cohérent avec un usage HD wallet (potentiellement adresse change ou adresse temporaire).

**Heuristique du timing**. Une transaction qui consomme rapidement après création (en quelques blocs) est cohérente avec un comportement automatisé (script, exchange) ou un peeling. Une consommation après semaines/mois suggère plutôt un wallet personnel.

**Heuristique du comportement « hot wallet »**. Une adresse qui reçoit beaucoup et envoie beaucoup en flux constants, avec des soldes rarement à zéro mais variables, est probablement un **hot wallet** d’un service (exchange, marchand, processeur de paiement).

**Heuristique du « cold storage »**. Une adresse qui reçoit beaucoup, garde longtemps, et envoie rarement (ou jamais) est probablement un **cold storage** (réserve d’un service ou d’un investisseur).

### 7.6 Limites des heuristiques

**Importance des limites**.

**CoinJoin casse le co-spending**. Wasabi, Samourai (Ch.32) — multi-input non lié à entité unique. Un cluster constitué via co-spending sur des transactions CoinJoin est **faux**. Les outils modernes détectent les CoinJoin et excluent ces transactions du clustering.

**Wallets modernes randomisent**. Certains wallets randomisent volontairement la position du change, le type d’adresse, et même le montant non-rond pour brouiller les heuristiques. Limite l’efficacité.

**Multi-sig**. Adresses multisig sont contrôlées par plusieurs parties. Heuristiques de clustering classique ne s’appliquent pas trivialement.

**Erreurs en cascade**. Une heuristique erronée à une étape pollue tout le cluster qui en découle. Les outils intègrent des **scores de confiance** pour limiter la propagation d’erreurs.

**Adversarial usage**. Un acteur qui connaît les heuristiques peut **délibérément** créer des transactions trompeuses pour brouiller l’analyse (faux co-spending, fausses peeling chains, etc.).

**Conclusion pour l’analyste** : les heuristiques sont **utiles mais probabilistes**. Toujours qualifier la confiance, croiser les sources, et documenter l’incertitude.

### 7.7 Outils pour analyse UTXO avancée

**Mempool.space** : excellent pour lecture transaction par transaction.

**OXT.me** (OpenX Tools) : outil communautaire orienté Bitcoin avancé. Visualisations de peeling chains, analyses heuristiques. Gratuit.

**KYCP.org** : outil dédié à l’analyse CoinJoin (« Know Your CoinJoin Privacy »). Permet d’évaluer la qualité d’un mélange CoinJoin.

**Breadcrumbs.app** : interface graphique pour exploration de flux. Tier gratuit limité.

**Chainalysis Reactor** : référence professionnelle. Clustering automatique, visualisation, scoring. Voir Ch.20.

**TRM Labs Investigations** : alternative pro. Même type de capacités.

**Scripts custom Python** : pour analyses spécifiques (parsing, statistiques sur des milliers de transactions). Bibliothèques : `python-bitcoinlib`, `electrum-protocol`, ou directement via API d’explorateurs.

### 7.8 Fil rouge — MIXSHADOW : premier mouvement Akira

> **🔗 MIXSHADOW — Épisode 4 : le premier hop**
> 
> 17 mars 2026, 03:42 UTC. L’alerte Chainalysis se déclenche : l’adresse Akira de réception (35 BTC) vient d’envoyer une transaction.
> 
> Sarah ouvre la transaction. Lecture :
> 
> - Input : 35,000 BTC (les fonds Aurélien Médical).
> - Output 1 : 35,000 BTC vers nouvelle adresse `bc1q[H1]...` (adresse fraîche, jamais utilisée).
> - Frais : 0,00012 BTC.
> 
> **Lecture initiale** : c’est un **simple transfer** vers une autre adresse contrôlée par Akira. Pas de split, pas de partage encore. L’adresse `bc1q[H1]` reçoit l’intégralité.
> 
> Sarah note : ce hop pourrait être :
> 
> - Une consolidation pré-blanchiment (déplacer les fonds vers wallet opérationnel).
> - Une rotation OPSEC (changer d’adresse tous les X jours).
> - Le début d’un peeling chain.
> 
> Elle continue la surveillance. À 04:18 UTC (36 minutes plus tard), `bc1q[H1]` envoie à son tour :
> 
> - Input : 35,000 BTC.
> - Output 1 : 0,500 BTC vers nouvelle adresse externe.
> - Output 2 : 34,500 BTC vers nouvelle adresse `bc1q[H2]` (probable change).
> 
> **C’est un peeling chain**. Sarah identifie le pattern : 0,5 BTC est éplutché vers ce qui sera probablement un dépôt d’exchange ou une étape de blanchiment, et le reste continue vers `bc1q[H2]`.
> 
> Sur les 6 heures suivantes, le pattern se répète :
> 
> - `bc1q[H2]` → 0,3 BTC à externe + 34,2 BTC à `bc1q[H3]`.
> - `bc1q[H3]` → 0,7 BTC à externe + 33,5 BTC à `bc1q[H4]`.
> - `bc1q[H4]` → 0,4 BTC à externe + 33,1 BTC à `bc1q[H5]`.
> - … etc.
> 
> Sarah documente chaque transaction en temps réel. Le journal MIXSHADOW capture chaque hop avec timestamp, montant, adresse externe destinatrice (qui sera analysée séparément).
> 
> Au bout de 24h, Sarah a identifié **18 hops** avec un total de **~7,5 BTC éplutchés** vers des adresses externes (à analyser une par une) et **~27,5 BTC** restant dans le wallet principal en mouvement.
> 
> Hypothèse : **peeling chain classique** post-rançon Akira. Sarah priorisera les premiers outputs externes pour identifier les destinations (exchanges, mixers, etc.) — Ch.13 développera cette priorisation. Pour l’instant, le travail est de **suivre méthodiquement chaque hop**.

-----

## Chapitre 8 — Lire une transaction Ethereum

Ethereum a un modèle radicalement différent de Bitcoin. La lecture demande des réflexes nouveaux. Ce chapitre couvre les transactions Ethereum natives, l’usage du gas, et les pièges classiques.

### 8.1 Anatomie d’une transaction Ethereum

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

### 8.2 Différences avec Bitcoin

**Source unique vs multiple inputs**. Une transaction Ethereum a **un seul émetteur**. Pas de co-spending Bitcoin-style. Heuristique de clustering différente.

**Pas de change**. Pas besoin d’adresse change — la blockchain met à jour directement les soldes.

**Smart contracts comme destinataires**. Le `To` peut être un smart contract qui exécute du code. Cela ouvre des possibilités énormes (DeFi, NFT) et complexifie la lecture.

**Gas variable**. Le coût d’une transaction dépend de sa complexité. Un simple transfer ETH = 21 000 gas. Une interaction smart contract complexe peut consommer 500 000+ gas.

**Tokens omniprésents**. Beaucoup de « valeur » sur Ethereum est dans des tokens (USDT, USDC, etc.) — pas dans ETH. Une transaction qui transfère 100 000 USDT a Value = 0 ETH (parce que la valeur est dans le token, pas dans ETH).

### 8.3 Lire une transaction Ethereum sur Etherscan

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

### 8.4 La piège des internal transactions

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

### 8.5 Le nonce et son intérêt

Le **nonce** est un compteur séquentiel par adresse. La première transaction d’une adresse a nonce 0, la deuxième nonce 1, etc.

**Implications enquête** :

**Confirmer l’auteur**. Le nonce séquentiel signifie qu’on peut savoir « combien de transactions cette adresse a déjà fait au moment de cette transaction ». Si une adresse fait sa transaction nonce 1, c’est sa **2ème transaction** de toute son histoire.

**Détecter des transactions fail**. Si une adresse a une transaction nonce N qui Fail, la prochaine transaction sera nonce N+1 (le nonce a été consommé même en cas d’échec). Voir des trous dans la séquence d’une adresse = drapeau d’investigation.

**Reconnaître l’activité d’un wallet**. Une adresse à nonce élevé (1000+) est une adresse **très active** (probable hot wallet de service). Une adresse à nonce 1 est presque vierge.

**Détection anomalie**. Une adresse avec activité importante (gros volumes) mais nonce faible (3-5 transactions) est suspicieuse — pourquoi un wallet récemment créé manipule-t-il déjà des montants significatifs ?

### 8.6 Les transactions « Failed »

Une transaction Ethereum peut **Fail** (échouer) : par exemple, si le smart contract appelé revert (annule l’opération). Le gas est tout de même consommé.

**Pourquoi voir des transactions Failed est utile** :

**Détection de tentatives de phishing/drainer**. Un drainer mal configuré peut faire fail. La transaction est visible mais sans transfert de valeur.

**Reconnaissance de tests**. Un attaquant peut tester sa logique en envoyant des transactions tests qui fail. Les nonce qui suivent pas un gap sont les vraies tentatives.

**Diagnostic d’erreur logique**. Pour analyser un hack DeFi, voir la séquence des transactions Failed avant Success peut révéler la logique exploit utilisée.

### 8.7 Erreurs classiques

**Ignorer les ERC-20 transferts**. Voir « Value: 0 ETH » et conclure qu’aucune valeur n’a bougé. Toujours regarder la section ERC-20 Tokens Transferred.

**Ignorer les internal transactions**. Pour les transactions impliquant des smart contracts, le mouvement réel d’ETH se fait souvent en internal.

**Confondre token contract et wallet**. L’adresse `0xdAC17F958D2ee523a2206206994597C13D831ec7` est le **contrat USDT** sur Ethereum. Ce n’est pas un wallet d’utilisateur — c’est l’infrastructure. Une transaction qui « envoie 100 USDT » a comme `To` cette adresse, mais le **destinataire réel** (qui reçoit les 100 USDT) est dans les logs ERC-20.

**Penser que `To = destinataire`**. Pour les interactions smart contract, `To` est le contrat appelé, pas le destinataire final de la valeur.

**Ignorer le contexte des chains**. Un transfer USDT sur Ethereum a une logique. Le même transfer sur BNB Chain a une logique similaire mais pas identique (frais différents, timings différents). L’analyste vérifie toujours **sur quelle chaîne** il regarde.

### 8.8 Outils Ethereum

**Etherscan.io** : référence absolue.

**Tenderly.co** : pour debugging avancé de transactions complexes (DeFi, exploits).

**Phalcon (BlockSec)** : analyse forensique de transactions complexes, simulation.

**EigenPhi** : analytics MEV (Maximal Extractable Value), arbitrage.

**Dune Analytics** : dashboards SQL personnalisables sur la blockchain.

**Bloxy** : explorer alternatif avec analytics.

**DeBank** : portfolio explorer multi-chain.

**Chainalysis Reactor / TRM Labs** : pour Ethereum aussi (Ch.20).

### 8.9 Fil rouge — MIXSHADOW : un détour par Ethereum

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

## Chapitre 9 — Tokens et smart contracts

L’écosystème crypto moderne ne se résume pas aux coins natifs. Une part majoritaire de l’activité économique on-chain passe par des **tokens** — actifs déployés via smart contracts. Comprendre tokens et smart contracts est indispensable pour ne pas rater l’essentiel d’une enquête.

### 9.1 Les standards de tokens

**ERC-20** (Ethereum). Standard pour tokens **fongibles** (interchangeables, divisibles). USDT, USDC, DAI, des dizaines de milliers d’autres. Spécification simple : `transfer`, `approve`, `transferFrom`, `balanceOf`, `totalSupply`, `allowance`. Chaque token ERC-20 est un smart contract dédié déployé sur Ethereum.

**ERC-721** (Ethereum). Standard pour **NFT** (Non-Fungible Tokens) — tokens uniques non-divisibles. Chaque token a un `tokenId` unique. CryptoPunks, BAYC, des millions d’autres.

**ERC-1155** (Ethereum). Standard hybride permettant tokens fongibles et non-fongibles dans un même contrat. Usage en gaming notamment.

**TRC-20** (TRON). Équivalent ERC-20 sur TRON. USDT-TRON est le plus important économiquement.

**BEP-20** (BNB Chain). Équivalent ERC-20 sur BNB Chain.

**SPL** (Solana Program Library). Standard tokens Solana, structure différente.

**Implications enquête** : un token est un smart contract avec une **adresse propre** sur la blockchain. Cette adresse est l’« infrastructure » du token, pas un wallet utilisateur. Confondre les deux = erreur classique.

### 9.2 Le contrat USDT sur Ethereum

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

### 9.3 Approve et allowance — le mécanisme central

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

### 9.4 Lire les logs ERC-20

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

### 9.5 Smart contracts : risques et opportunités d’enquête

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

### 9.6 Phishing par smart contract

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

### 9.7 Fil rouge — MIXSHADOW : analyse smart contract Tornado

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

## Chapitre 10 — Stablecoins : USDT, USDC et le rôle opérationnel

Les **stablecoins** sont devenus la **monnaie de transaction** de pans entiers de l’écosystème crypto. Légitime comme illicite. Ce chapitre approfondit leur fonctionnement, leur dominance dans certains flux illicites, et les opportunités défensives qu’ils offrent (gel d’actifs).

### 10.1 Qu’est-ce qu’un stablecoin

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

### 10.2 Pourquoi les stablecoins dominent les flux

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

### 10.3 USDT vs USDC — différences pour l’enquête

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

### 10.4 Le gel d’actifs

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

### 10.5 USDT-TRON vs USDT-Ethereum

**Erreur classique** : penser que « USDT est USDT » indépendamment de la chaîne. **Faux**.

- **USDT-Ethereum** : un token ERC-20 sur Ethereum, contrat `0xdAC17...`.
- **USDT-TRON** : un token TRC-20 sur TRON, contrat `TR7N...`.
- **Ce sont DEUX tokens distincts**, juste émis par le même émetteur (Tether) avec le même peg USD.

**Conséquences** :

**Un USDT-Ethereum NE PEUT PAS être directement transféré à une adresse TRON**. Il faut un **bridge** ou un **swap cross-chain** (passage par exchange ou service de bridging).

**Les soldes sont distincts**. Une adresse Ethereum peut avoir 1000 USDT, et l’« même utilisateur » sur TRON peut avoir 500 USDT — c’est deux balances séparées.

**Les frais sont radicalement différents**. Transfer USDT-TRON ~1 centime. Transfer USDT-Ethereum 5-30 USD selon congestion. Cette différence explique pourquoi les flux à haute fréquence (pig butchering, certains blanchiments) privilégient TRON.

**L’enquêteur** vérifie toujours **sur quelle chaîne** il regarde. Mentions « USDT » sans préciser la chaîne sont ambiguës et doivent être clarifiées.

### 10.6 Patterns de blanchiment via stablecoins

**Pattern 1 — Conversion BTC → USDT**. Après un paiement BTC (rançon, paiement darknet), conversion rapide en USDT pour stabiliser la valeur, soit via exchange centralisé, soit via swap (FixedFloat, ChangeNOW, etc.).

**Pattern 2 — Bridge cross-chain via USDT**. USDT-Ethereum → USDT-TRON via bridge ou exchange. Réduit la traçabilité et change le coût opérationnel.

**Pattern 3 — Layering USDT-TRON**. Multiple transferts entre adresses TRON contrôlées, peeling chain-style, avec frais minimes. Alimente la dispersion.

**Pattern 4 — Off-ramp via P2P**. Conversion USDT → fiat via plateformes P2P (Binance P2P, LocalCryptos, etc.) ou OTC desks. Permet de quitter la blockchain en monnaie locale.

**Pattern 5 — Obfuscation pré-cashout**. Avant cashout final, mélange via DEX ou usage de protocoles DeFi pour ajouter du bruit.

### 10.7 Investigation TRON spécifique

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

### 10.8 Fil rouge — MIXSHADOW : transit par stablecoins

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

## Chapitre 11 — Explorateurs blockchain : méthodologie de lecture

L’analyste qui passe ses journées dans des explorateurs doit en maîtriser la lecture. Ce chapitre couvre les principaux explorateurs, leurs spécificités, et la méthodologie pour les utiliser efficacement.

### 11.1 Les explorateurs Bitcoin

**Mempool.space** :

- Open source, moderne, performant.
- Excellente UX pour navigation transaction/adresse/bloc.
- Visualisations mempool en temps réel.
- API gratuite généreuse.
- Communauté active.
- **Recommandé** pour usage quotidien et vérification.

**Blockstream.info (Esplora)** :

- Blockstream, open source aussi.
- Solide, classique.
- Bon pour intégration via API.

**Blockchain.com Explorer** :

- Historique, large utilisation.
- Interface vieillissante.
- Toujours fonctionnel.

**BTC.com Explorer** :

- Géré par Bitmain.
- Statistiques mining riches.

**OXT.me** :

- Spécialisé analyses Bitcoin avancées.
- Excellent pour peeling chains et clusters.

**Blockchair.com** :

- Multi-chain (BTC, ETH, autres).
- Recherche cross-chain pratique.

**Pour l’analyste** : Mempool.space en premier choix, OXT pour analyses avancées, autres en validation croisée.

### 11.2 Les explorateurs Ethereum

**Etherscan.io** :

- **Référence absolue**.
- UX éprouvée.
- Décodage automatique des smart contracts vérifiés.
- Labels riches (exchanges, contracts, sanctions OFAC).
- API gratuite (avec limites) + tier payant.
- Indispensable.

**Beaconcha.in** :

- Couvre la beacon chain (consensus) Ethereum post-Merge.
- Utile pour analyser staking, validators.

**Phalcon.xyz (BlockSec)** :

- Analyse forensique avancée.
- Excellent pour transactions complexes (DeFi, exploits).
- Visualisation des appels internes.

**Tenderly.co** :

- Plateforme dev, mais utile pour analyse.
- Simulation de transactions, debugging.

**Bloxy.info** :

- Analytics et reporting.
- Recherche avancée.

### 11.3 Les autres explorateurs

**Tronscan.org** : référence TRON. Couvre transactions, USDT-TRON, smart contracts TRON.

**Solscan.io** : référence Solana. Tokens SPL, NFT Solana.

**BscScan.com** : BNB Chain. Clone d’Etherscan (même équipe).

**PolygonScan.com** : Polygon. Clone Etherscan.

**Arbiscan.io, Optimistic.etherscan.io, Basescan.org** : Layer-2 Ethereum. Clones Etherscan.

**Snowtrace.io** : Avalanche.

**FtmScan.com** : Fantom.

**Multiversx Explorer (anciennement Elrond)** : MultiversX.

**Cosmos / Mintscan.io** : Cosmos écosystème.

**XRPSCAN, Bithomp** : XRP Ledger.

**Pour l’analyste polyvalent** : maîtriser au minimum Etherscan + Tronscan + Mempool. Étendre selon les chaînes rencontrées dans les enquêtes.

### 11.4 Méthodologie de lecture

**Phase 1 — Validation initiale**.

- Vérifier que le TXID/adresse existe bien (mauvaise saisie, typo, mauvaise chaîne).
- Vérifier la chaîne — beaucoup d’erreurs viennent de chercher un transaction ETH sur Etherscan alors qu’elle est sur BNB Chain.
- Status : Success ou Failed.
- Confirmations suffisantes (transaction finalisée).

**Phase 2 — Lecture structurée**.

- Header (block, timestamp).
- From / To.
- Value (native).
- Logs / Events (token transfers, autres).
- Internal transactions.
- Fee.

**Phase 3 — Documentation**.

- Capture de la page (Hunchly).
- Notation dans le journal d’enquête.
- Hash de la capture.
- Lien vers l’explorateur (stable, vérifiable plus tard).

**Phase 4 — Enrichissement**.

- Vérifier les labels associés (exchange, mixer, sanction).
- Pour les contrats, vérifier le code source si vérifié.
- Pour les adresses, regarder l’historique complet.

**Phase 5 — Croisement multi-explorateurs** (selon enjeu) :

- Pour les cas critiques, vérifier la même transaction sur 2 explorateurs indépendants.
- Confirme l’absence de bug d’affichage.
- Capture les enrichissements différents (labels, etc.).

### 11.5 Citer une page d’explorateur correctement

**Format de citation** :

- URL complète et stable.
- TXID ou adresse complète (pas tronquée).
- Date et heure de consultation (UTC).
- Hash de la capture (SHA-256).
- Pour pages dynamiques (qui peuvent évoluer), capture HTML + screenshot.

**Exemple journal** :

```
2026-03-19 14:23 UTC
Consulté Mempool.space pour TXID e3a5f9a8... 
URL: https://mempool.space/tx/e3a5f9a8c1b2d4e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0
Capture: tx_e3a5f9a8_20260319.html, hash SHA-256: abc123...
Observation: Transaction confirmée, 35 BTC transférés depuis 4 inputs Aurélien Médical vers bc1q[Akira]
Document de référence: MIXSHADOW_journal.md ligne 42
```

**Pourquoi ce niveau de rigueur ?** Les blockchains sont immutables, mais les explorateurs peuvent évoluer (UI change, labels updated, données enrichies). Une capture précise garantit reproductibilité d’analyse 6 mois ou 5 ans plus tard, voire devant juge.

### 11.6 Limites des explorateurs publics

**Manque de clustering**. Les explorateurs publics affichent transactions et adresses individuellement. Pour voir le cluster d’une adresse, il faut un outil professionnel (Chainalysis Reactor, TRM Labs).

**Labels limités**. Etherscan a beaucoup de labels mais pas tous. Tronscan en a moins. Les outils pro ont des bases label propriétaires bien plus riches.

**Pas de visualisation graphe**. Les explorateurs sont transactionnels, pas graphiques. Pour visualiser des flux complexes (peeling chains, dispersions), outil dédié (Maltego, Gephi, Chainalysis Reactor).

**Pas de scoring de risque**. Les explorateurs n’évaluent pas le risque d’une adresse. Outils pro le font.

**Performance sur grosses adresses**. Une adresse avec 100 000 transactions sera lente à charger. Outils pro paginent et indexent mieux.

**Conclusion** : explorateurs publics = base nécessaire et gratuite pour vérification. Outils pro = amplification de capacité pour investigations sérieuses. Combiner les deux. Voir Ch.19 (gratuits) et Ch.20 (pro).

### 11.7 Fil rouge — MIXSHADOW : navigation multi-explorateurs

> **🔗 MIXSHADOW — Épisode 8 : routine quotidienne**
> 
> Le travail de Sarah devient routine. Chaque jour, elle :
> 
> 1. Vérifie sur Mempool.space les nouveaux mouvements depuis les adresses Akira identifiées.
> 1. Cross-check sur Etherscan pour les flux Ethereum.
> 1. Tronscan pour les flux TRON.
> 1. Chainalysis Reactor pour la vue cluster et alertes.
> 1. TRM Labs en validation parallèle.
> 
> Au bout de 3 semaines :
> 
> - **62 adresses Bitcoin** identifiées dans les peeling chains et leurs branches.
> - **18 adresses Ethereum** identifiées dans la branche Tornado Cash et post-retraits.
> - **47 adresses TRON** identifiées dans les flux USDT.
> - **12 adresses dans 4 exchanges différents** (FixedFloat, ChangeNOW, exchange non-KYC X, autre exchange non-KYC Y).
> 
> Sarah maintient un **graphe maître** dans Chainalysis Reactor + un **journal Markdown détaillé** pour chaque mouvement. Pour chaque adresse, une **fiche d’adresse** (Ch.12) est constituée.
> 
> Elle remarque : **certaines adresses TRON** (3 d’entre elles) ont un comportement « hub » — elles reçoivent de multiples sources et redistribuent. Hypothèse : ces adresses pourraient appartenir à un **service de blanchiment** (mixer manuel, OTC desk) qu’Akira utilise comme intermédiaire, plutôt qu’à Akira directement.
> 
> Cette nuance est importante : si ces hubs sont des **services**, l’attribution ne peut pas remonter directement à Akira via ces hubs. Mais identifier le **service utilisé** par Akira est en soi une **valeur de renseignement** : d’autres groupes ransomware utilisent peut-être le même service, et le service lui-même peut être ciblé par les autorités.
> 
> Sarah documente cette hypothèse comme « probable » (confiance ~70%), avec actions de vérification : continuer à surveiller, vérifier si d’autres clusters ransomware connus ont historiquement utilisé ces hubs, croiser avec bases TRM/Chainalysis (dont les labels propriétaires sont plus riches que les labels Etherscan/Tronscan).
> 
> La méthodologie d’enquête (Partie III) va structurer cette analyse — comment passer de l’observation brute (« je vois des hops, des adresses, des flux ») à la production de renseignement (« voici la topologie du réseau de blanchiment Akira, avec niveaux de confiance et angles d’action »).

-----
