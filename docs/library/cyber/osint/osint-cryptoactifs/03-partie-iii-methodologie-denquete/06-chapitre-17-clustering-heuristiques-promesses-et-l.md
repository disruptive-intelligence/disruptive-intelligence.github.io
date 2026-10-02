---
title: 'Chapitre 17 — Clustering : heuristiques, promesses et limites'
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie III — Méthodologie d’enquête
  - index.md
---

Le **clustering** — regroupement d’adresses appartenant probablement à la même entité — est l’une des techniques fondamentales de l’enquête crypto. Mais c’est aussi un domaine où les illusions sont nombreuses. Ce chapitre détaille promesses et limites.

## 17.1 Le concept

**Clustering** : à partir des observations on-chain, on regroupe les adresses qui semblent contrôlées par la **même entité** (un même utilisateur, un même service, une même organisation).

**Pourquoi clusters** :

- Une entité utilise typiquement **multiples adresses** (rotation, séparation par usage, hot/cold).
- Reconstituer le **portefeuille complet** d’une entité permet une vue économique réaliste.
- Identifier l’entité (si possible) sur **n’importe quelle adresse du cluster** étend l’attribution à tout le cluster.

**Comment** : par application d’**heuristiques** sur les transactions observées.

## 17.2 Les heuristiques principales

**1. Heuristique du co-spend (multi-input)**. Sur Bitcoin, plusieurs inputs co-dépensés dans une transaction sont contrôlés par la même entité (qui possède les clés privées de tous). Forte mais cassée par CoinJoin.

**2. Heuristique du change**. Sur Bitcoin, l’output « change » d’une transaction est contrôlé par l’entité qui a émis. Diverses sous-heuristiques pour identifier le change (Ch.6).

**3. Heuristique du timing**. Adresses actives dans des fenêtres temporelles très proches sont possiblement liées.

**4. Heuristique du wallet**. Certains wallets (Electrum, Bitcoin Core, etc.) génèrent les adresses selon des patterns reconnaissables. Reconnaissance du wallet utilisé est un signal.

**5. Heuristique de l’address reuse**. Une adresse qui reçoit un dépôt unique puis envoie immédiatement vers une nouvelle adresse jamais vue suit un pattern HD wallet (transit).

**6. Heuristique des patterns de service**. Exchange consolide selon patterns reconnaissables (cadence, seuils). L’analyste expérimenté identifie les patterns d’exchange spécifiques.

**7. Heuristique des labels propriétaires**. Les outils Chainalysis/TRM/Elliptic ont des **bases label** internes (acquises par : recherche, KYC achetés, leaks, partenariats avec exchanges). Une adresse labellisée est un point d’attribution dans un cluster.

## 17.3 Le clustering Ethereum : différent

Ethereum n’a **pas** d’heuristique du co-spend (transactions à un seul émetteur). Le clustering Ethereum repose sur :

**Patterns d’activité**. Adresses contrôlées par une même entité se comportent souvent de manière cohérente (interactions avec mêmes smart contracts, paiements gas par même source, etc.).

**Funding source**. Si une adresse est créée et immédiatement financée par une autre adresse, c’est un signal de contrôle commun.

**Smart contract ownership**. Une adresse qui a déployé un smart contract est probablement liée aux adresses qui interagissent avec ce contrat de manière privilégiée.

**Cross-chain activity**. Une adresse Ethereum qui bridge des fonds vers TRON, et l’adresse TRON destinataire qui a un pattern d’activité similaire, suggère même entité.

**Limites** : clustering Ethereum est **moins robuste** que Bitcoin co-spend. Les outils s’appuient massivement sur **labels propriétaires** et heuristiques mixtes.

## 17.4 Promesses du clustering

**Quand le clustering fonctionne bien** :

**Wallets utilisateurs simples**. Un utilisateur basique avec wallet Bitcoin Core génère plusieurs adresses, fait des transactions classiques. Heuristique du co-spend reconstitue le wallet en cluster. Précision élevée.

**Services / exchanges**. Les services consolident des fonds utilisateurs vers hot wallets. Le co-spend massif et patterns reconnaissables identifient le service. Cluster Coinbase = des centaines de milliers d’adresses, identifié avec précision élevée.

**Acteurs criminels naïfs**. Les acteurs qui n’ont pas pris de précautions OPSEC (réutilisation d’adresses, co-spend entre wallets « privés » et wallets « publics ») sont rapidement identifiés.

**Ransomware classique**. Les opérateurs ransomware qui collectent des dizaines de paiements vers un même wallet opérationnel forment un cluster identifiable.

## 17.5 Limites du clustering

**Quand le clustering échoue ou induit en erreur** :

**CoinJoin**. Wasabi et Samourai cassent l’heuristique du co-spend. Inputs co-dépensés ne sont **pas** d’une même entité. Un cluster constitué via co-spending sur des transactions CoinJoin est **faux**. Les outils modernes détectent les CoinJoin et excluent ces transactions du clustering — vérifier que c’est le cas.

**Wallets modernes anti-tracking**. Wallets qui randomisent volontairement la structure des transactions (montants non-ronds aléatoires, position du change, etc.) limitent l’efficacité des heuristiques.

**Multi-sig**. Adresses multisig sont contrôlées par plusieurs parties (M-of-N). Pas une seule entité. Heuristiques qui supposent contrôle unique se trompent.

**Smart contracts (Ethereum)**. Adresses contrôlées par smart contracts (exchanges décentralisés, pools de liquidité, comptes contrats) ont des patterns propres qui ne se prêtent pas au clustering classique.

**Adresses partagées implicites**. Certains wallets « shared » ou exchanges qui n’utilisent qu’un seul wallet pour multiples utilisateurs créent des « clusters » qui sont en fait des **agrégations**, pas des entités uniques.

**Erreurs en cascade**. Si une heuristique commet une erreur en début de chaîne, tout le cluster qui en découle est faux. Outils intègrent scores de confiance pour limiter, mais erreurs existent.

**Adversarial design**. Acteurs qui connaissent les heuristiques peuvent **délibérément** créer des transactions trompeuses pour brouiller (faux co-spending, fausses peeling chains).

## 17.6 Vocabulaire et calibration

**Cluster** : ensemble d’adresses regroupées comme appartenant probablement à la même entité.

**Niveau de confiance d’un cluster** :

- **Très fiable** : multiple heuristiques convergentes, peu de risques d’erreur (cluster d’exchange majeur, par exemple).
- **Fiable** : heuristique principale solide, validation par patterns secondaires.
- **Probable** : heuristique principale plausible, mais alternatives existent.
- **Spéculatif** : pattern observé mais sans fort support, à vérifier.

**Affirmer « le cluster X »** sans calibration de confiance est une erreur. Toujours expliciter.

**Vocabulaire à utiliser** :

- « Le cluster comprend X adresses, attribué par Chainalysis avec confiance « high » à l’entité Y ».
- « Le cluster reconstruit par heuristiques de co-spend regroupe N adresses ; cette construction est probable (~80%) sauf erreur de heuristique non détectée ».
- « L’entité présumée derrière le cluster est probablement [exchange/individu/groupe] (confiance Y%) ».

## 17.7 Validation croisée

**Multi-outils**. Si Chainalysis et TRM Labs concluent au même cluster, confiance plus élevée que si un seul outil. Validation indépendante.

**Cohérence comportementale**. Le cluster a-t-il un comportement **cohérent** dans le temps ? Patterns d’activité stables ? Si le cluster évolue brusquement (devient hyperactif, change de patterns), il peut s’agir d’un **changement de contrôle** (vente, hack, changement opérationnel).

**Recoupement OSINT**. Si le cluster correspond à une entité publiquement attribuée (annonce officielle, label vendor, mention OSINT), validation externe.

## 17.8 Le clustering n’est pas une preuve d’identité

**Message clé à intérioriser** :

> Le clustering ne prouve pas une identité. Il propose un regroupement probable d’adresses contrôlées par une même entité ou un même service, selon des heuristiques discutables.

Une entité du cluster peut être :

- Un wallet utilisateur unique.
- Un service (exchange, mixer).
- Un agrégat artificiel (erreur de heuristique).

L’**identité civile** derrière n’est pas dans le cluster. Elle nécessite des éléments **off-chain** (KYC exchange, mention publique, recoupement OSINT).

Le cluster est un outil pour **structurer la vue**, pas pour conclure. L’analyste avisé manipule les clusters comme des hypothèses calibrées, pas comme des vérités.

-----
