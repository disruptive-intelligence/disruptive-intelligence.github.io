---
title: Chapitre 7 — Le modèle UTXO en profondeur
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie II — Lire les blockchains
  - index.md
---

Comprendre le modèle UTXO sans erreur est la condition pour ne pas se perdre dans les flux Bitcoin. Ce chapitre dépasse les bases du Ch.6 pour aborder les patterns avancés : peeling chains, consolidation, splits, et les heuristiques fines.

## 7.1 La logique UTXO

Reprenons. Dans le modèle UTXO :

- Une « adresse » n’a pas de solde stocké comme variable. Son solde est **calculé** à la volée comme la somme des UTXO non dépensés qui lui sont assignés.
- Une transaction **consomme** des UTXO existants (les inputs) et **crée** de nouveaux UTXO (les outputs).
- Un UTXO est soit **non-dépensé** (UTXO actif, partie du « set UTXO ») soit **dépensé** (consommé par une transaction ultérieure).

**Implications pour l’enquête** :

L’historique d’une adresse est un **graphe** : les transactions qui ont créé des UTXO vers cette adresse, les transactions qui ont consommé ces UTXO. Pour chaque UTXO assigné à l’adresse, on peut dire « il a été créé par TX1 et consommé par TX2 ».

L’analyste qui veut comprendre **« d’où viennent les BTC actuellement à l’adresse X »** suit, pour chaque UTXO non-dépensé, la transaction qui l’a créé, puis remonte à ses inputs, etc. C’est ce qu’on appelle **« remonter la chaîne UTXO »**.

## 7.2 Le peeling chain — le pattern de blanchiment classique

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

## 7.3 La consolidation

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

## 7.4 Les splits

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

## 7.5 Heuristiques avancées de clustering

Au-delà du co-spend (Ch.6), plusieurs heuristiques affinent le clustering Bitcoin.

**Heuristique de l’adresse change moderne**. Avec SegWit et Taproot, les wallets utilisent généralement le **même type d’adresse** pour le change que pour les inputs. Si une transaction a inputs en P2WPKH (SegWit native, `bc1q...`) et un output en P2WPKH (probable change) + un output en P2PKH (`1...`, probable destinataire), l’output P2WPKH est très probablement le change.

**Heuristique du montant exact**. Si un montant en output correspond exactement à un montant communément requis pour un service (ex : 0,5 BTC pour un dépôt minimum exchange), c’est un signal pour le destinataire. Le change a un montant « calculé » non-rond.

**Heuristique des adresses jamais réutilisées**. Les wallets modernes (BIP-32 hierarchical deterministic) génèrent une nouvelle adresse pour chaque transaction. Si une adresse n’est utilisée qu’une fois (recevoir une transaction et envoyer immédiatement), c’est cohérent avec un usage HD wallet (potentiellement adresse change ou adresse temporaire).

**Heuristique du timing**. Une transaction qui consomme rapidement après création (en quelques blocs) est cohérente avec un comportement automatisé (script, exchange) ou un peeling. Une consommation après semaines/mois suggère plutôt un wallet personnel.

**Heuristique du comportement « hot wallet »**. Une adresse qui reçoit beaucoup et envoie beaucoup en flux constants, avec des soldes rarement à zéro mais variables, est probablement un **hot wallet** d’un service (exchange, marchand, processeur de paiement).

**Heuristique du « cold storage »**. Une adresse qui reçoit beaucoup, garde longtemps, et envoie rarement (ou jamais) est probablement un **cold storage** (réserve d’un service ou d’un investisseur).

## 7.6 Limites des heuristiques

**Importance des limites**.

**CoinJoin casse le co-spending**. Wasabi, Samourai (Ch.32) — multi-input non lié à entité unique. Un cluster constitué via co-spending sur des transactions CoinJoin est **faux**. Les outils modernes détectent les CoinJoin et excluent ces transactions du clustering.

**Wallets modernes randomisent**. Certains wallets randomisent volontairement la position du change, le type d’adresse, et même le montant non-rond pour brouiller les heuristiques. Limite l’efficacité.

**Multi-sig**. Adresses multisig sont contrôlées par plusieurs parties. Heuristiques de clustering classique ne s’appliquent pas trivialement.

**Erreurs en cascade**. Une heuristique erronée à une étape pollue tout le cluster qui en découle. Les outils intègrent des **scores de confiance** pour limiter la propagation d’erreurs.

**Adversarial usage**. Un acteur qui connaît les heuristiques peut **délibérément** créer des transactions trompeuses pour brouiller l’analyse (faux co-spending, fausses peeling chains, etc.).

**Conclusion pour l’analyste** : les heuristiques sont **utiles mais probabilistes**. Toujours qualifier la confiance, croiser les sources, et documenter l’incertitude.

## 7.7 Outils pour analyse UTXO avancée

**Mempool.space** : excellent pour lecture transaction par transaction.

**OXT.me** (OpenX Tools) : outil communautaire orienté Bitcoin avancé. Visualisations de peeling chains, analyses heuristiques. Gratuit.

**KYCP.org** : outil dédié à l’analyse CoinJoin (« Know Your CoinJoin Privacy »). Permet d’évaluer la qualité d’un mélange CoinJoin.

**Breadcrumbs.app** : interface graphique pour exploration de flux. Tier gratuit limité.

**Chainalysis Reactor** : référence professionnelle. Clustering automatique, visualisation, scoring. Voir Ch.20.

**TRM Labs Investigations** : alternative pro. Même type de capacités.

**Scripts custom Python** : pour analyses spécifiques (parsing, statistiques sur des milliers de transactions). Bibliothèques : `python-bitcoinlib`, `electrum-protocol`, ou directement via API d’explorateurs.

## 7.8 Fil rouge — MIXSHADOW : premier mouvement Akira

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
