---
title: Chapitre 20 — Crypto, blanchiment et circulation de la valeur
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie IV — Comprendre L'économie cybercriminelle
  - index.md
---

## 20.1 La crypto comme moyen, pas comme finalité

Les cryptomonnaies ne sont pas le but de l'opération criminelle — elles sont le tuyau par lequel la valeur circule. Aucun affilié RaaS ne veut accumuler du Bitcoin indéfiniment ; il veut convertir sa rançon en monnaie fiat utilisable dans l'économie réelle, pour acheter un appartement, une voiture, ou réinvestir dans des opérations futures. La crypto est un moyen de transfert pseudo-anonyme, pas une finalité.

## 20.2 Circuits de blanchiment

Le blanchiment de crypto d'origine criminelle suit des circuits relativement standardisés. Les fonds arrivent sur un wallet de rançon (une adresse unique par victime dans les opérations bien gérées). Ils sont transférés vers un wallet de consolidation contrôlé par l'affilié ou l'opérateur. Puis ils sont fragmentés et envoyés vers des services d'obfuscation.

Les techniques d'obfuscation incluent le mixing/tumbling (les services qui mélangent les fonds de plusieurs utilisateurs — les mixers centralisés sont de plus en plus saisis, la tendance est aux protocoles décentralisés et aux techniques intégrées comme CoinJoin), les bridges cross-chain (transférer des fonds de Bitcoin vers Ethereum puis vers Monero, chaque passage de chaîne compliquant le traçage), les peeling chains (fragmentation progressive — un wallet envoie une petite partie des fonds vers une adresse et le reste vers une autre adresse contrôlée, et l'opération se répète des dizaines de fois), le chain-hopping via DEX (échanges sur des exchanges décentralisés qui ne requièrent pas de KYC), et la conversion vers des privacy coins (Monero principalement, dont les transactions sont nativement opaques).

Après obfuscation, les fonds convergent vers des points de cash-out : exchanges à KYC laxiste (certaines plateformes, notamment dans les Émirats, en Russie, ou en Asie du Sud-Est, appliquent des contrôles d'identité minimaux), OTC desks (transactions de gré à gré avec des courtiers qui échangent de la crypto contre du fiat, souvent avec des commissions de 5 à 15 %), réseaux de mules (des personnes recrutées pour recevoir des virements bancaires et les retransférer, souvent sans comprendre l'origine criminelle des fonds), et sociétés écrans (des structures légales qui « facturent des services de conseil » en réalité inexistants pour justifier les flux financiers).

## 20.3 Erreurs récurrentes des opérateurs

Malgré la sophistication croissante des techniques de blanchiment, les erreurs des opérateurs restent fréquentes et constituent des points d'entrée pour l'investigation financière. La réutilisation de wallets (utiliser la même adresse pour plusieurs opérations crée un cluster identifiable), les transferts directs vers des exchanges KYC (un wallet de rançon qui envoie des fonds directement vers Binance ou Coinbase est traçable par réquisition judiciaire), les volumes incohérents (un wallet personnel qui reçoit soudainement 500 000 $ est suspect même après mixing), et les patterns temporels détectables (les transferts qui suivent un rythme régulier — chaque lundi à 14h — révèlent des habitudes).

## 20.4 Fil rouge — NEXUS : le circuit financier complet

> **🔍 NEXUS — Épisode 19**
>
> Le circuit financier de l'écosystème PhantomCrypt est cartographié à partir des rançons payées par d'autres victimes (Énergis n'a pas payé).
>
> Étape 1 : Paiement de rançon → wallet dédié par victime (adresse unique, bonne OPSEC).
> Étape 2 : Transfert vers wallet de consolidation (cluster de 47 adresses — heuristique CIO).
> Étape 3 : Fragmentation vers un service de mixing sanctionné.
> Étape 4 : Post-mixing, convergence vers deux destinations : (a) cluster associé à un exchange Dubaï (cash-out probable, 65 % du volume), (b) wallet identifié dans un rapport Chainalysis comme « possiblement lié à des activités para-étatiques » (15 % du volume).
>
> Les 20 % restants se dispersent vers des wallets non attribués (destinations inconnues).
>
> Samira note : la proportion de 15 % vers le wallet para-étatique pourrait être une « taxe » (un paiement de protection à un acteur étatique) ou un partage de revenus avec un sponsor. Mais elle pourrait aussi être un artefact du mixing (les fonds mélangés dans le mixer ne sont pas traçables de manière déterministe — voir Ch.12).

---
