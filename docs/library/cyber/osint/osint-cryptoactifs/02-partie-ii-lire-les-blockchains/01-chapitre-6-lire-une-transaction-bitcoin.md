---
title: Chapitre 6 — Lire une transaction Bitcoin
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie II — Lire les blockchains
  - index.md
---

Bitcoin est la blockchain la plus ancienne, la plus étudiée, et celle dont l’analyse a le corpus de connaissances le plus mature. Mais sa lecture demande un changement mental par rapport au modèle bancaire classique. Ce chapitre apprend à lire une transaction Bitcoin sans erreur d’interprétation — en particulier la confusion fréquente entre **destinataire** et **adresse de change**.

## 6.1 Anatomie d’une transaction Bitcoin

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

## 6.2 La confusion classique : destinataire vs change

Reprenons l’exemple ci-dessus. Une lecture **naïve** dirait :

- L’expéditeur a envoyé 1 BTC à 2 destinataires : 0,7 BTC à `bc1qdestination` et 0,299 BTC à `bc1qchange`.
- Donc deux destinataires.

**Cette lecture est très probablement fausse**. La réalité, dans la grande majorité des cas :

- **Le vrai destinataire** est `bc1qdestination` qui reçoit 0,7 BTC.
- **`bc1qchange` est une adresse de change** : c’est une adresse contrôlée par **l’expéditeur lui-même**, qui récupère le « rendu de monnaie ». L’expéditeur avait des UTXO totalisant 1 BTC mais voulait n’envoyer que 0,7 BTC, donc il s’envoie 0,299 BTC à lui-même (le reste 0,001 BTC va aux frais).

**Pourquoi ce mécanisme ?** Bitcoin est **UTXO**. On ne peut pas « dépenser une partie d’un UTXO » — on consomme l’UTXO entier et on en crée de nouveaux. Si vous avez un UTXO de 1 BTC et voulez envoyer 0,7 BTC, vous devez consommer le UTXO de 1 BTC entier, créer un output de 0,7 BTC pour le destinataire, et un output de 0,299 BTC qui revient à vous (moins les frais).

**Erreur classique de lecture** : conclure que `bc1qchange` est un destinataire distinct, l’ajouter au graphe d’enquête comme entité séparée, le suivre comme un acteur indépendant. C’est une erreur **fondamentale** qui pollue toute l’enquête.

## 6.3 Reconnaître l’adresse de change

Plusieurs heuristiques permettent d’identifier l’adresse de change.

**Heuristique du nouveau wallet**. Le change va typiquement vers une **nouvelle adresse fraîchement générée** (jamais utilisée auparavant). Les adresses « destinataires » sont plus souvent réutilisées. Si dans une transaction vous avez deux outputs et que l’un pointe vers une adresse fraîche jamais vue, c’est probablement le change.

**Heuristique du round number**. Le destinataire reçoit souvent un **montant rond** (1 BTC, 0,5 BTC, 0,1 BTC). Le change reçoit un montant non-rond (0,299 BTC dans l’exemple). Si vous voyez `0,7000` et `0,2998` en outputs, le `0,7000` est très probablement le destinataire.

**Heuristique du script type**. Le change utilise **généralement le même type d’adresse** que les inputs (P2PKH, P2SH, SegWit, Taproot). Le destinataire peut être de type différent. Heuristique faible isolément, plus forte combinée.

**Heuristique du wallet client**. Certains wallets (Electrum, par exemple) ont des patterns comportementaux récurrents dans la sélection d’adresses de change. Un analyste expérimenté reconnaît parfois le wallet utilisé d’après la structure.

**Limitation** : aucune de ces heuristiques n’est **certaine**. Chacune a un taux d’erreur. Les outils professionnels (Chainalysis, TRM, Elliptic) combinent plusieurs heuristiques + ML pour scorer la probabilité.

## 6.4 Les inputs multiples : co-spending

Dans l’exemple, la transaction consomme deux inputs (0,4 BTC + 0,6 BTC). C’est le **co-spending**.

**Heuristique du co-spend (« common-input ownership »)** : si plusieurs inputs sont dépensés ensemble dans une même transaction, ils sont **probablement contrôlés par la même entité**. Pourquoi ? Parce que dépenser plusieurs UTXO ensemble nécessite de signer chacun avec sa clé privée. Une entité qui ne contrôle pas les deux clés ne peut pas faire cette transaction.

**Forte mais pas absolue** : exceptions notables :

- **CoinJoin** : protocole coopératif où plusieurs parties signent ensemble une transaction sans partager les clés (Ch.32). Dans un CoinJoin, les inputs **ne sont PAS contrôlés par la même entité**. Heuristique caduque.
- **Multi-sig collaboratif** : plus rare mais existe.
- **Transactions exchange** : un exchange agrège les fonds de plusieurs utilisateurs dans des UTXO, puis les re-dispatche. Le co-spending au niveau exchange ne dit rien sur les utilisateurs finaux.

L’heuristique du co-spend est **la base du clustering Bitcoin**. Les outils modernes l’appliquent en masse pour regrouper des millions d’adresses en clusters d’entité probable.

## 6.5 Lire une transaction sur Mempool.space

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

## 6.6 Erreurs classiques

**Confondre destinataire et change**. Déjà détaillé. Erreur la plus fréquente.

**Ignorer les frais**. Un input de 1 BTC qui produit des outputs totalisant 0,999 BTC : ce n’est pas un « 0,001 BTC perdu », c’est les frais.

**Confondre montant brut et montant net**. Si vous regardez `bc1qsource1` qui a un input de 0,4 BTC dans une transaction, ce 0,4 BTC est le **UTXO consommé**, pas nécessairement « le montant envoyé par cette adresse ». Le montant net envoyé dépend des outputs.

**Mal interpréter une consolidation**. Un wallet peut **consolider** : prendre 50 petits UTXO et les regrouper en un seul gros UTXO (output unique vers une adresse contrôlée par le même wallet). C’est une opération **interne** au wallet, pas un transfert. Sans heuristique, on peut croire à un envoi de 50 sources vers un destinataire.

**Confondre adresse et personne**. Rappel : une adresse peut être contrôlée par plusieurs personnes (multisig), une personne contrôle souvent des dizaines d’adresses, un service exchange agrège des milliers d’utilisateurs derrière quelques hot wallets.

**Ignorer les fuseaux horaires**. Les timestamps sont en UTC. Si vous documentez « la transaction de 9h12 », précisez « 09:12 UTC, soit 10:12 heure de Paris ». Sinon confusion garantie quand vous corroborez avec des logs internes (bancaires, applicatifs).

**Sur-attribuer trop tôt**. Voir un cluster de 50 adresses ne dit pas qui les contrôle. Documenter le cluster = OK. Conclure « ces adresses appartiennent à X » = pas OK sans preuve externe.

## 6.7 Fil rouge — MIXSHADOW : la transaction de paiement

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
