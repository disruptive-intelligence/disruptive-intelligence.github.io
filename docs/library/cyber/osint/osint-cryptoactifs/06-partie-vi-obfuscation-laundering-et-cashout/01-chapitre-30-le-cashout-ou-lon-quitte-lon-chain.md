---
title: 'Chapitre 30 — Le cashout : où l’on quitte l’on-chain'
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VI — Obfuscation, laundering et cashout
  - index.md
---

Le **cashout** est le moment où les fonds quittent la blockchain pour entrer dans le monde fiat (ou être consommés sous forme de biens/services). C’est **le maillon le plus important** pour l’enquêteur et le plus vulnérable pour le criminel.

## 30.1 Pourquoi le cashout est central

**Pour le criminel** : le crypto en lui-même est rarement « utile ». Pour acheter une voiture, payer un loyer, financer une opération, il faut **convertir** en monnaie utilisable.

**Pour l’enquêteur** : le cashout est où le KYC entre en jeu. Les exchanges régulés exigent identification. Le moment du cashout est souvent **le seul** où on peut relier une adresse blockchain à une identité civile.

**Stratégique** : si l’enquête identifie le cashout, elle a identifié **l’angle d’attaque** des autorités — réquisition pour KYC, gel de fonds, identification.

## 30.2 Les méthodes de cashout

**Exchange centralisé régulé (CEX KYC)**. La méthode standard mais risquée pour le criminel.

- Avantages criminels : volume élevé, facilité, multi-paires.
- Inconvénients : KYC obligatoire, monitoring AML, possibilité de gel.

**Exchange centralisé non-KYC ou faible KYC**. Plateformes dans juridictions permissives. KYC inexistant ou contournable.

- Cas connus : multiple petits exchanges (souvent peu durables, fermés / sanctionnés).
- Garantex (sanctionné OFAC 2022). Bitzlato (sanctionné 2023). Suex (sanctionné 2021). Successeurs émergent et sont sanctionnés à leur tour.

**OTC desks (Over-The-Counter)**. Brokers qui matchent acheteurs / vendeurs hors orderbook public.

- Régulés (intégrés à exchanges) : KYC requis.
- Non-régulés : permissif, populaire pour gros montants.
- Spread (différence d’achat/vente) plus élevé pour montants importants.

**P2P (peer-to-peer) trading**. Plateformes où particuliers échangent crypto/fiat directement.

- **Binance P2P** : marché P2P intégré à Binance, KYC requis pour comptes.
- **HodlHodl, AgoraDesk** : alternatives sans KYC.
- **LocalCoinSwap, autres** : variantes.
- Permet conversion en monnaie locale par virement bancaire entre individus.

**ATM crypto (BTM)**. Distributeurs Bitcoin permettant achat / vente cash. Présents dans plusieurs pays. KYC variable selon machine et juridiction. Limites de montant.

**Cartes prepaid crypto**. Crypto debit cards (Wirex, Crypto.com, autres). Permettent conversion progressive crypto vers achats en ligne / retraits ATM.

**Achats directs** :

- Immobilier (dans juridictions permissives — quelques pays acceptent crypto pour transactions immobilières).
- Voitures, luxe (cars, montres, art).
- Or et métaux précieux.

**Mules / muleware**. Réseaux de personnes (souvent recrutées en ligne) qui reçoivent fonds crypto et convertissent / transfèrent. Communs dans pig butchering et fraudes massives.

**Gambling**. Casinos crypto (Stake, Bitcasino, autres). Permettent conversion via dépôt crypto + retrait fiat ou autres crypto. Moins efficace mais pratiqué.

**Gift cards / vouchers**. Achats de gift cards Amazon, Apple, Walmart payés en crypto. Revente sur marchés secondaires.

**Conversion sur DEX puis off-ramp ailleurs**. DEX permet swap entre cryptos sans KYC. Mais final off-ramp en fiat nécessite quand même un point centralisé quelque part.

## 30.3 Reconnaître les patterns de cashout

**Signaux d’un dépôt sur exchange régulé** :

- Adresse destinatrice labellisée par outils pro.
- Montant cohérent avec dépôt utilisateur (quelques centaines à milliers USD typiquement, parfois plus).
- Pattern de dépôt unique (l’adresse de dépôt utilisateur reçoit, le hot wallet exchange centralise).

**Signaux d’OTC ou P2P** :

- Transferts vers wallets « privés » (pas exchange).
- Patterns « hub » : adresse recevant multiples dépôts et redistributant en montants équivalents (broker P2P matchant trades).

**Signaux de cards crypto** :

- Conversion progressive en stablecoins (USDC notamment, intégré aux cartes).
- Petits transferts réguliers vers wallets de cards providers.

## 30.4 Coopération avec les exchanges

**Exchanges régulés** :

- Procédures d’investigation établies.
- Coopèrent avec autorités sur réquisition (USA, EU, UK, autres juridictions).
- Capacité de **gel** des comptes utilisateurs et **fourniture de KYC**.
- Délais variables (heures à semaines).

**Exchanges non-KYC ou peu coopérants** :

- Souvent dans juridictions permissives.
- Coopération difficile.
- Action possible via sanctions (OFAC) ou pressions juridictionnelles.

**Pour l’enquêteur** : identifier l’exchange traversé est **étape critique**. Permet d’orienter l’action des autorités. Sarah Marin dans MIXSHADOW a identifié plusieurs exchanges à risque traversés par les fonds Akira ; cette information est transmise à la DGSI pour évaluation de coopération.

## 30.5 Mules et réseaux de cashout

**Mules** : individus utilisés pour recevoir / convertir des fonds illicites.

**Mode de recrutement** :

- Annonces fausses « gagnez de l’argent en travaillant à domicile ».
- Romance scam (la mule est elle-même victime).
- Recrutement direct via Telegram / forums.
- Coercition / trafic humain (cas extrêmes, pig butchering compounds).

**Implications** :

- La mule peut être identifiée KYC sur exchange, mais l’**enquête remonte à la mule**, pas au cerveau.
- Coopération de la mule (si pas complice consciente) peut donner indications sur les commanditaires.

## 30.6 Limites OSINT au cashout

**Le KYC est off-chain**. L’analyste OSINT identifie l’adresse de dépôt exchange, mais **ne peut pas** accéder aux données KYC sans réquisition légale.

**Identification finale = autorités**. OSINT prépare le terrain (« cette adresse a déposé chez exchange X »), autorités opèrent la requête.

**Délais**. Entre identification du cashout et obtention du KYC, plusieurs semaines/mois peuvent passer. Pendant ce temps, les fonds peuvent avoir été déjà retirés.

**Multi-juridiction**. Réquisitions internationales sont lentes. Coopération variable selon juridiction.

## 30.7 Le cashout comme point d’attention défensif

Pour défense :

**Monitoring de cashout**. Pour fonds tracés à des activités illicites, alerter dès que mouvement vers exchange régulé connu = opportunité de gel.

**Coopération sectorielle**. Exchanges qui partagent informations (FATF Travel Rule, ISACs financiers) accroissent capacité collective.

**AML automation**. Outils intégrés (Chainalysis KYT, TRM, Elliptic Discovery) permettent screening en temps réel des dépôts.

## 30.8 Le message à intérioriser

> Le cashout est souvent le moment le plus intéressant pour l’enquête, mais aussi celui où l’OSINT atteint ses limites sans coopération d’un VASP ou réquisition.

L’OSINT identifie. Les autorités agissent. La coopération entre les deux est le multiplicateur de capacité.

## 30.9 Fil rouge — MIXSHADOW : les cashouts identifiés

> **🔗 MIXSHADOW — Épisode 17 : points de cashout**
> 
> À 6 semaines de mission, Sarah a identifié les **points de cashout** des fonds Akira issus du paiement Aurélien Médical :
> 
> **Exchange régulé via dépôts identifiables** :
> 
> - **3 dépôts sur Binance** : ~80 000 USDT cumulés. Adresses de dépôt identifiables, KYC potentiel via réquisition.
> - **2 dépôts sur Kraken** : ~25 000 USDT. Idem.
> - **1 dépôt sur Coinbase** : ~12 000 USDT. Idem.
> 
> **Exchange non-KYC** :
> 
> - **Exchange non-KYC X** : ~150 000 USDT cumulés transités. Pas d’angle KYC. Sanctions OFAC sur cet exchange demandées par l’enquête (alimente dossier).
> 
> **OTC / P2P (probable)** :
> 
> - **2 hubs TRON** identifiés (cf Ch.13). Probable services de blanchiment (broker P2P / OTC). Pas d’angle KYC direct, mais alimentation profil pour traque future.
> 
> **Cartes prepaid (suspecté)** :
> 
> - Quelques flux résiduels semblent transiter par des wallets compatibles avec providers de cartes prepaid crypto. Volume modéré (~30 000 USDT). Investigation continue.
> 
> **Non identifiés / dispersion** :
> 
> - **~50 000 USDT** dans un layering profond TRON, destination finale non encore caractérisée à 6 semaines.
> 
> **Bilan** :
> 
> - **~120 000 USDT** identifiés sur exchanges régulés (Binance / Kraken / Coinbase) — **angle KYC fort**, transmission DGSI pour coordination réquisition.
> - **~150 000 USDT** sur exchange non-KYC X — angle sanctions / coordination internationale.
> - **~80 000 USDT** dispersés / non identifiés pour le moment.
> 
> Sarah note dans le rapport intermédiaire : **120 000 USDT sur exchanges régulés** = potentiel **angle de récupération partielle** via gel et identification. Si les exchanges identifient les comptes (probable, dépôts récents) et coopèrent rapidement, une partie peut être gelée. La DGSI prend en charge la coordination.
> 
> 6 semaines plus tard (semaine finale), retour : **~45 000 USDT effectivement gelés** sur Binance et Kraken (3 comptes mules identifiés), KYC fournis aux autorités. Dossiers transmis à FBI Cyber Division pour enquête sur les mules. Récupération définitive des fonds dépend de la procédure judiciaire ultérieure.
> 
> 45 000 USDT sur 2 M EUR initial = **~2,3% récupération nominale**, mais **valeur de renseignement** beaucoup plus large : 3 mules identifiées, alimentent dossier multi-juridictionnel sur réseau Akira.

-----
