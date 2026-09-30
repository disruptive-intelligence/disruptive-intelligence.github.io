---
title: 'Chapitre 18 — Attribution : adresse → service → personne'
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie III — Méthodologie d’enquête
  - index.md
---

L’**attribution** est l’opération qui consiste à associer une adresse, un cluster, ou un flux à une **entité identifiée**. Plusieurs niveaux existent. Ce chapitre les distingue et calibre les niveaux de preuve.

## 18.1 Les trois niveaux d’attribution

**Niveau 1 — Attribution à un service**. « Cette adresse est un dépôt Binance. » L’entité attribuée est un **service** (exchange, custodian, marchand). Le service connaît l’identité civile de l’utilisateur (via KYC), mais l’analyste OSINT ne la connaît pas — elle nécessite réquisition.

**Niveau 2 — Attribution à un acteur connu**. « Cette adresse est contrôlée par Lazarus / Akira / AlphaBay. » L’entité attribuée est un **acteur identifié** (groupe, individu connu, organisation). L’attribution s’appuie sur preuves publiques (annonces vendor, labels OFAC, recoupements OSINT).

**Niveau 3 — Attribution à une personne nommée**. « Cette adresse est contrôlée par [Nom de personne réelle]. » L’entité attribuée est un **individu civil identifié**. Très rare en OSINT pur, généralement issue de procédures judiciaires (saisies, inculpations).

L’analyste opère principalement aux niveaux 1 et 2. Niveau 3 relève des autorités.

## 18.2 Distinguer adresse, wallet, service, personne

**Adresse** : identifiant cryptographique. Singulier.

**Wallet** : ensemble d’adresses contrôlées par une même clé privée racine (HD wallet) ou une même infrastructure (multi-sig, custody). Peut contenir des centaines ou milliers d’adresses.

**Service** : entité qui opère un wallet (ou des wallets) pour servir des clients. Exchange, custodian, processeur de paiement, mixer. Le service contrôle les clés ; les utilisateurs ont des **comptes** chez le service mais pas les clés.

**Personne** : individu civil. Peut être :

- Utilisateur direct d’un wallet (non-custodial).
- Utilisateur d’un service (custodial).
- Salarié / dirigeant d’un service.
- Membre d’un groupe criminel utilisant un wallet collectif.

Chaque niveau requiert un type d’attribution différent.

**Erreur classique** : « cette adresse appartient à [personne] » alors que l’enquête montre seulement « cette adresse a déposé chez Binance ». Personne ≠ adresse de dépôt.

## 18.3 Sources d’attribution

**Preuve directe** :

- Publication volontaire par le propriétaire (« voici mon adresse de tip »).
- Données KYC obtenues via réquisition (autorités).
- Aveu / coopération (procédure judiciaire).

**Preuve forte** :

- Saisies officielles avec adresses publiquement attribuées (FBI press release, DOJ unsealed indictment).
- Sanctions OFAC (SDN list inclut adresses crypto).
- Documents judiciaires publics (acte d’accusation, jugement).

**Preuve modérée** :

- Labels d’outils professionnels (Chainalysis, TRM, Elliptic) — basés sur recherche propriétaire, parfois leaks, parfois partenariats.
- Annonces publiques de vendeurs, services (« notre adresse hot wallet est X »).
- Patterns d’usage cohérents avec attribution (très haut volume, pattern exchange).

**Preuve faible** :

- Recoupement par cluster avec une adresse labellisée.
- Mention sur forum non-vérifiée.
- Inférence par pattern.

**Les outils pro mélangent souvent ces niveaux** — un label dans Chainalysis peut être basé sur preuve forte (annonce officielle exchange) ou modérée (inférence pattern). La documentation interne précise généralement, mais l’analyste sérieux **vérifie la source**.

## 18.4 L’échelle de confiance d’attribution

**Format type** (Annexe E pour matrice complète) :

|Niveau       |Probabilité|Critères                                            |
|-------------|-----------|----------------------------------------------------|
|Certain      |>95%       |Preuve directe (saisie officielle, OFAC, KYC obtenu)|
|Très probable|80-95%     |Multiple labels convergents + comportement cohérent |
|Probable     |60-80%     |Label outil pro + patterns soutenant                |
|Possible     |40-60%     |Inférence par cluster + label faible                |
|Spéculatif   |<40%       |Pattern observé sans support fort                   |

**Bonne pratique** : noter le niveau dans la fiche d’adresse et dans le rapport.

**Évolution dans le temps** : attribution peut **monter** (nouvelles preuves) ou **descendre** (preuves contradictoires émergentes). La fiche évolue.

## 18.5 Cas typiques de mauvaise attribution

**Mauvaise attribution 1 — confondre dépôt exchange et exchange lui-même**.

Une adresse de **dépôt** chez un exchange (créée par l’exchange pour un utilisateur précis) est différente du **hot wallet** de l’exchange. L’adresse de dépôt est attribuée à **l’utilisateur** (via KYC exchange), pas à l’exchange en tant qu’entité criminelle.

Erreur : « cette adresse est Binance » alors que c’est en fait l’adresse de dépôt d’un utilisateur de Binance.

Bon : « cette adresse est une adresse de dépôt utilisateur chez Binance. L’identification de l’utilisateur nécessite réquisition ».

**Mauvaise attribution 2 — sur-attribution par cluster**.

Cluster reconstitué par heuristiques regroupe 50 adresses. Une des adresses est labellisée « possibly Lazarus ». Conclure « tout le cluster est Lazarus » est une **sur-attribution** : le label est faible, le cluster peut contenir d’autres entités, l’erreur peut se propager.

Bon : « cluster contient une adresse labellisée ‘possibly Lazarus’ avec confiance modérée. Le label peut être correct ou ne couvrir qu’une partie du cluster ».

**Mauvaise attribution 3 — attribution à un acteur étatique sans preuve**.

Un cluster qui utilise Tornado Cash et bridges → tentation de l’attribuer à Lazarus. Mais Lazarus n’est pas le seul à utiliser ces outils. Sans preuve spécifique (technique d’attaque, infrastructure, adresses précédemment attribuées), l’attribution étatique est spéculative.

Bon : « patterns cohérents avec acteurs étatiques type Lazarus, mais attribution requiert éléments additionnels pour confirmation ».

**Mauvaise attribution 4 — confondre opérateur et affilié**.

Dans le RaaS, l’opérateur (qui fournit le malware et l’infrastructure) est distinct des affiliés (qui exécutent les attaques). Une adresse de paiement ransomware peut être contrôlée par l’affilié, le service de blanchiment, l’opérateur, ou une combinaison.

Bon : « adresse contrôlée par un acteur du programme Akira, sans précision possible sur affilié ou opérateur sans preuves additionnelles ».

## 18.6 L’attribution dans les rapports

**Bonnes formulations** :

- « L’adresse X est très probablement (confiance >90%) une adresse de hot wallet de Binance, sur la base du label Chainalysis et du pattern d’activité cohérent. »
- « Le cluster Y contient une adresse précédemment attribuée par OFAC à Lazarus. Le cluster lui-même est probablement (confiance ~75%) lié à des opérations Lazarus, sans pouvoir préciser si l’ensemble du cluster est dédié ou partagé. »
- « L’adresse Z a un comportement cohérent avec un opérateur de pig butchering, mais sans label vendor ni recoupement OSINT, l’attribution reste possible (~50%). »
- « L’identification de l’utilisateur final derrière l’adresse de dépôt nécessite une réquisition auprès de l’exchange concerné, qui dépend des autorités compétentes. »

**Mauvaises formulations** (à éviter) :

- « L’adresse X est Lazarus. » (Sans calibration ni preuve.)
- « Le propriétaire de cette adresse est [nom]. » (Sans preuve directe.)
- « Le cluster est entièrement contrôlé par [groupe]. » (Sur-attribution.)

## 18.7 La responsabilité de l’analyste

L’attribution **engage**. Une attribution incorrecte peut :

**Nuire à un tiers innocent**. Si Sarah attribue à tort un wallet à un individu nommé, et que le rapport est utilisé contre cet individu, dommage réputationnel et juridique potentiel.

**Compromettre une enquête**. Mauvaise attribution oriente l’enquête dans la mauvaise direction, ressources gaspillées.

**Discréditer l’analyste et son organisation**. Une attribution démontrée fausse érode la crédibilité.

**Implications légales**. Diffamation crypto : possible si nom propre attribué sans base solide.

**Discipline** : l’analyste calibre **systématiquement**. Mieux vaut « probable » correct que « certain » incorrect. Mieux vaut « identité non déterminable sans réquisition » que « propriétaire X » erroné.

## 18.8 Fil rouge — MIXSHADOW : attribution prudente

> **🔗 MIXSHADOW — Épisode 12 : calibration d’attribution**
> 
> Sarah finalise l’attribution dans son rapport intermédiaire (semaine 4).
> 
> **Adresse de réception ransomware** :
> 
> - Niveau d’attribution : **probable**, dédiée à l’opération Aurélien Médical, contrôlée par un opérateur Akira ou affilié.
> - Confiance : ~85%.
> - Base : pattern dédié (adresse fraîche utilisée une seule fois pour cette victime), montant correspondant exactement à la rançon négociée, contexte (le portail de négociation Akira a fourni cette adresse).
> - Pas plus précis que « opérateur Akira ou affilié » — distinction non déterminable.
> 
> **Cluster Bitcoin opérationnel post-paiement** :
> 
> - Niveau d’attribution : **probable** Akira (contrôle continu post-paiement).
> - Confiance : ~80%.
> - Base : continuité du peeling chain depuis l’adresse de réception, pattern cohérent, pas de discontinuité.
> - Reste : pourrait être un **service de blanchiment** sous-traitant pour Akira, plutôt qu’Akira directement.
> 
> **Hubs TRON suspects (services de blanchiment)** :
> 
> - Niveau d’attribution : **possible** services de blanchiment.
> - Confiance : ~65%.
> - Base : patterns hub (multi-sources / multi-destinations), pas attribué dans labels Chainalysis/TRM mais cohérent avec services à risque.
> - Action : alerter labels Chainalysis pour enrichir leur base, croiser avec d’autres incidents Akira.
> 
> **FixedFloat / exchange non-KYC X / Tornado Cash** :
> 
> - Niveau d’attribution : **certain** (services publiquement identifiés).
> - Pas de confusion possible — ce sont des services connus.
> 
> **Acteur Akira lui-même (groupe)** :
> 
> - Niveau d’attribution : **certain** que ces fonds sont liés à l’opération ransomware Aurélien Médical attribuée à Akira (le groupe Akira a revendiqué via leak site et négocié avec Aurélien Médical).
> - Mais attribution **personnelle** (qui est dans Akira ?) : **non déterminable** dans le périmètre OSINT MIXSHADOW. Réservé aux autorités via coopération internationale.
> 
> Sarah documente chaque niveau dans le rapport. Pas de précipitation. Pas d’attribution civile spéculative. Calibration honnête. Le rapport est crédible parce qu’il est calibré.
> 
> Cette discipline va payer : la DGSI valide le rapport intermédiaire et le transmet à Europol pour exploitation, parce que les attributions sont exploitables (claires, calibrées, sourcées) — pas politiquement compromises par des sur-attributions.

-----
