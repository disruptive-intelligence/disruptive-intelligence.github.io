---
title: Chapitre 10 — Objets financiers
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie II — Les entités de L'écosystème
  - index.md
---

## 10.1 Wallets et clusters d'adresses

Une adresse Bitcoin (ou Ethereum, ou toute autre cryptomonnaie) n'est pas une identité — c'est un nœud financier dans un réseau de flux. Un même acteur peut contrôler des centaines d'adresses, et une même adresse peut être utilisée successivement par plusieurs acteurs (dans le cas de wallets de services comme les exchanges ou les mixers).

Le **clustering** est la technique fondamentale de l'analyse blockchain. L'heuristique la plus courante pour Bitcoin est le Common Input Ownership (CIO) : si deux adresses sont utilisées comme inputs dans une même transaction, elles sont probablement contrôlées par la même entité (parce qu'il faut détenir les clés privées de toutes les inputs pour signer la transaction). Cette heuristique permet de regrouper des dizaines ou des centaines d'adresses en « clusters » représentant une seule entité.

Les limites du clustering sont réelles. L'heuristique CIO échoue quand les transactions utilisent des techniques de privacy (CoinJoin, PayJoin) qui mélangent les inputs de plusieurs utilisateurs. Elle peut aussi produire des faux positifs quand un service (exchange, mixer) utilise des inputs de plusieurs clients dans une même transaction. Les clusters ne sont pas des certitudes — ils sont des estimations probabilistes.

Les plateformes comme Chainalysis Reactor enrichissent le clustering brut avec des données d'attribution : elles associent des clusters à des entités connues (exchanges identifiés, services de mixing, portefeuilles de ransomware, adresses de darknet markets) grâce à une combinaison de heuristiques, de données de coopération avec les exchanges, et de monitoring OSINT. La base d'attribution de Chainalysis couvre plus de 5 milliards de clusters (mars 2026).

## 10.2 Flux entrants et sortants comme révélateurs de pouvoir

La cartographie des flux financiers d'un écosystème révèle les relations de pouvoir et de dépendance entre acteurs. Qui paie qui, dans quel sens, à quel volume, et à quelle fréquence — ces informations structurent l'analyse économique.

Les **flux entrants** d'un wallet révèlent ses sources de revenus : paiements de victimes (rançons), revenus de ventes (accès, données, services), transferts d'autres acteurs de l'écosystème. Les **flux sortants** révèlent ses dépenses et ses relations : paiement de l'opérateur (commission RaaS), paiement du IAB (achat d'accès), achat de services (hébergement, crypter), et blanchiment (transfert vers mixers, exchanges, ou wallets intermédiaires).

Un acteur qui reçoit beaucoup et distribue peu est un accumulateur (typiquement un opérateur ou un investisseur). Un acteur qui reçoit peu et redistribue immédiatement est un intermédiaire de transit (typiquement un service de mixing ou une mule). Un acteur qui reçoit de sources multiples et diversifiées est un hub financier (typiquement un exchange ou un service de blanchiment).

## 10.3 Passerelles, mixers, bridges et exchanges

Les points de conversion et d'obfuscation sont les nœuds critiques de l'analyse financière.

Les **exchanges KYC** (qui appliquent les procédures de vérification d'identité) sont les points de dé-anonymisation potentielle. Si un wallet criminel envoie des fonds vers un exchange régulé, les forces de l'ordre peuvent théoriquement obtenir l'identité du titulaire du compte par réquisition judiciaire. C'est pourquoi les acteurs sophistiqués évitent les grands exchanges et passent par des OTC desks (transactions de gré à gré, souvent dans des juridictions peu coopératives) ou des exchanges non régulés.

Les **mixers et tumblers** sont des services qui mélangent les fonds de plusieurs utilisateurs pour rompre le lien entre l'adresse d'origine et l'adresse de destination. Les mixers centralisés (comme Chipmixer, saisi par les autorités en 2023, ou Sinbad, saisi en novembre 2023) sont vulnérables aux saisies. La tendance est aux protocoles décentralisés et aux techniques de mixing intégrées aux wallets (comme le protocole Wasabi, bien que celui-ci ait fermé son service de coordination en 2024, et ses successeurs comme JoinMarket).

Les **bridges cross-chain** permettent de transférer de la valeur d'une blockchain à une autre (de Bitcoin vers Ethereum, par exemple), ce qui complique le traçage. Les **DEX** (exchanges décentralisés) permettent d'échanger des tokens sans intermédiaire centralisé, rendant le traçage plus difficile mais pas impossible pour les plateformes d'analyse avancées.

## 10.4 Wallets dormants, jetables et de transit

Un wallet peut jouer différents rôles selon son pattern d'utilisation.

Un **wallet dormant** reçoit des fonds et ne les déplace pas pendant une longue période. Il peut s'agir d'un stockage long terme (l'acteur attend que l'attention se dissipe avant de blanchir) ou d'un wallet abandonné. Un **wallet jetable** est utilisé une seule fois : il reçoit des fonds, les transfère immédiatement vers une autre adresse, et n'est plus jamais utilisé. Les chaînes de wallets jetables (peeling chains) sont une technique de blanchiment courante. Un **wallet de transit** est un nœud intermédiaire qui ne « possède » pas les fonds mais les relaye — typiquement un wallet d'un service de mixing ou d'un exchange.

La distinction entre ces rôles est critique pour éviter les erreurs d'attribution. Attribuer un wallet de transit à un acteur parce que « des fonds de la rançon y sont passés » est une erreur fréquente : le wallet peut appartenir au service de mixing, pas à l'acteur criminel.

## 10.5 Fil rouge — NEXUS : la piste financière

> **🔍 NEXUS — Épisode 10**
>
> Bien qu'Énergis n'ait pas payé la rançon (l'EDR a bloqué le chiffrement), Samira peut tracer les wallets associés à l'écosystème PhantomCrypt grâce aux rançons payées par d'autres victimes.
>
> Le leak site de PhantomCrypt liste 23 victimes sur les 6 derniers mois. L'analyste identifie les adresses Bitcoin de paiement à partir des notes de rançon partagées dans des rapports CTI communautaires. OXT.me permet de tracer les flux à partir de ces adresses.
>
> Le pattern est récurrent : les paiements arrivent sur des wallets dédiés par victime (une adresse unique par rançon — bonne OPSEC), puis sont transférés vers un wallet de consolidation (cluster de 47 adresses), puis fragmentés vers un service de mixing identifié par Chainalysis comme « Mixer X » (service sanctionné par l'OFAC en 2024). Après le mixing, les fonds réapparaissent sous forme de multiples petites transactions convergent vers deux destinations principales.
>
> La première : un cluster associé à un exchange basé à Dubaï, connu pour ses contrôles KYC laxistes. C'est le cash-out probable.
>
> La seconde : un wallet identifié dans un rapport de Chainalysis de 2025 comme « possiblement lié à des activités de collecte de fonds para-étatiques » — sans attribution définitive, avec un niveau de confiance modéré.
>
> La piste financière rejoint la piste géopolitique. Samira documente le lien avec un niveau de confiance C3 (source : rapport commercial d'éditeur CTI, fiabilité modérée ; information : lien indirect via chaîne de mixing, fiabilité modérée).

---
