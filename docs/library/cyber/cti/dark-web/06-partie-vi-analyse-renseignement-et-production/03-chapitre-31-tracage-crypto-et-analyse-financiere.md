---
title: Chapitre 31 — Traçage crypto et analyse financière
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie VI — ANALYSE, renseignement et production
  - index.md
---

Le **traçage crypto** est l'un des outils les plus puissants d'investigation dark web. Couvert en profondeur dans le cours **OSINT Crypto** de la bibliothèque ; ce chapitre donne l'essentiel applicable au dark web.

## 31.1 Le paradoxe de Bitcoin

Bitcoin est **pseudonyme**, pas anonyme (Ch.8). Les transactions sont publiques et permanentes. Cette transparence est un **cadeau** pour les investigateurs — tout ce qui circule sur Bitcoin est archivé à jamais.

**Conséquences** :

- Une adresse BTC affichée publiquement sur un forum dark web est un **identifiant à vie**. Son historique est entièrement traçable.
- Une transaction d'il y a 5 ans est analysable aujourd'hui.
- Les techniques de clustering identifient les **autres adresses** probablement contrôlées par le même acteur.
- Les flux vers des exchanges KYC donnent des points d'**attribution personnelle**.

C'est pourquoi les acteurs sérieux migrent vers Monero ou mixers. Mais beaucoup continuent d'utiliser BTC par commodité, créant des opportunités pour les investigateurs.

## 31.2 Outils de traçage crypto

**Plateformes commerciales** (leaders du marché) :

- **Chainalysis** (Reactor, KYT) : standard de l'industrie. Labellisation massive d'adresses, UI puissante. Utilisé par FBI, DOJ, multiple exchanges majeurs.
- **TRM Labs** (Forensics, Know Your VASP) : concurrent solide, focus compliance et investigation.
- **Elliptic** (Navigator, Discovery) : autre leader, labellisation et graphing.
- **CipherTrace** (maintenant Mastercard).
- **Crystal** (Bitfury).
- **Merkle Science**.

**Outils open source et gratuits** :

- **Blockchain explorers** : Blockstream.info, Mempool.space (Bitcoin), Etherscan (Ethereum), Tronscan (TRON), BlockChair (multi-chain). Gratuits, informations brutes.
- **Breadcrumbs.app** : interface graphique pour exploration, version gratuite limitée.
- **OXT (OpenX Tools)** : outil communautaire pour Bitcoin, analyses heuristiques.
- **WalletExplorer** : clustering basique Bitcoin.

**Les plateformes commerciales coûtent 50 k - 500 k USD/an** et sont nécessaires pour investigation professionnelle. Les outils open source suffisent pour cas ponctuels.

## 31.3 Heuristiques de clustering

Les outils ne se contentent pas de montrer les transactions — ils **regroupent** les adresses contrôlées probablement par le même acteur.

**Heuristique de co-dépense (multi-input)**. Si une transaction inclut plusieurs inputs d'adresses différentes, elles sont probablement contrôlées par la même entité (le détenteur des clés privées). Heuristique forte historiquement, moins absolue avec les CoinJoin.

**Heuristique de change**. Une transaction typique a un output vers le destinataire + un output de change (retour) vers le payeur. Identifier l'adresse de change permet de poursuivre la chaîne.

**Heuristique temporelle**. Adresses actives dans les mêmes fenêtres temporelles, avec patterns cohérents.

**Heuristique de montants ronds**. Si une transaction envoie un montant rond, l'autre output est probablement le change.

**Heuristique de réutilisation**. Certains wallets réutilisent les adresses (mauvaise pratique), créant des clusters évidents.

**Limites** : ces heuristiques produisent des clusters **probabilistes**, pas certains. Un CoinJoin peut casser l'heuristique multi-input. Les wallets modernes (Electrum, Wasabi) emploient des techniques qui complique le clustering.

## 31.4 Labellisation

Les plateformes maintiennent des bases de données d'adresses **labellisées** — associées à un acteur ou service connu.

**Labels typiques** :

- **Exchanges** : Binance, Coinbase, Kraken, OKX, etc. — avec adresses hot wallet et cold wallet identifiées.
- **Mixers** : Tornado Cash (Ethereum), Wasabi, Samourai (Bitcoin).
- **Darknet markets** : adresses actuelles et historiques de Hydra, AlphaBay, Silk Road, etc.
- **Ransomware groups** : adresses de collecte de LockBit, Conti, ALPHV, Black Basta, etc.
- **Scammers** : adresses documentées comme impliquées dans fraudes.
- **Sanctionnés OFAC** : Tornado Cash, Garantex, Suex, multiple adresses individuelles.
- **Criminels identifiés** : adresses liées à individus inculpés publiquement.

Ces labels alimentent l'analyse. Si une adresse suspecte envoie des fonds à une adresse labellisée « Binance hot wallet », on sait que les fonds sont transités par Binance — potentiel point de requête légale pour KYC.

## 31.5 Le blanchiment et ses patterns

Comprendre comment les criminels tentent d'échapper au traçage aide à le contrer.

**Mixers et tumblers**. Envoi à un mixer, réception depuis le pool. Casse le lien direct. Mais : les mixers sont surveillés, sanctionnés, parfois saisis. Les entrées/sorties d'un mixer sont visibles — un cluster qui utilise massivement Tornado Cash est labellisé « mixer user ».

**Chain hopping**. Conversion BTC → ETH → autre chain → retour BTC, via exchanges ou DEX. Complique le traçage car change de blockchain, mais les outils modernes suivent cross-chain.

**Monero swaps**. Conversion BTC → XMR via exchange ou atomic swap. Une fois en XMR, quasi-intraçable. Revient en BTC après, chemin interrompu.

**Layering** : multiples transferts entre wallets contrôlés avant de sortir. Augmente la complexité d'analyse mais pas insurmontable.

**Off-ramp via exchange KYC**. La sortie en fiat reste le point faible. Passage par un exchange avec KYC — l'identité est accessible via requête légale.

**Off-ramp via P2P / OTC non-KYC**. Dans des juridictions peu régulées. Plus discret mais volumes limités, ou commissions élevées.

**Achats directs**. Immobilier en crypto, voitures, luxe. Dans juridictions qui l'acceptent, peut éviter la conversion fiat.

## 31.6 Les saisies réussies

Quelques cas emblématiques montrent l'efficacité du traçage.

**Bitcoin Colonial Pipeline (juin 2021)**. Le FBI récupère ~2,3 M USD des 4,4 M USD de rançon payés à DarkSide, via identification et saisie des clés privées d'une adresse de réception. Spectaculaire.

**Bitfinex (février 2022)**. DOJ saisit **3,6 milliards USD** en crypto (prix du moment), liés au hack Bitfinex de 2016. Identification via analyse blockchain après que Ilya Lichtenstein et Heather Morgan ont tenté de blanchir les fonds.

**Chipmixer (mars 2023)**. Saisie du mixer, avec 46 000 BTC (~2,73 Mrd EUR à l'époque) saisis ou traçables.

**Samourai Wallet (avril 2024)**. Fondateurs (Keonne Rodriguez et William Hill) inculpés, infrastructure saisie.

**Tornado Cash**. Sanctionné par OFAC (août 2022). Multiple inculpations des développeurs : Alexey Pertsev (Pays-Bas, condamné mai 2024), Roman Storm (US, procès en cours).

**Suex, Garantex, Bitzlato** : exchanges non-KYC ou à KYC faible sanctionnés par OFAC pour facilitation de blanchiment criminel.

Ces cas montrent que le **traçage fonctionne** — avec ressources, patience, et coopération internationale. Le criminel sophistiqué n'est pas invulnérable, juste plus difficile à attraper.

## 31.7 L'intégration dans l'investigation dark web

Pour l'analyste CTI investigant sur le dark web, le traçage crypto est un **pivot** puissant.

**Workflow type** :

1. **Observer une adresse** sur post forum, profil vendeur, paiement ransomware.
2. **Rechercher dans plateforme** (Chainalysis/TRM/Elliptic) — labels existants, cluster.
3. **Analyser historique** — transactions reçues, envoyées, comportement typique.
4. **Suivre les flux** — vers où vont les fonds ? Exchange ? Mixer ? Autre wallet ?
5. **Identifier points d'attribution** — passages par exchange KYC comme angles pour futures requêtes légales (via autorités).
6. **Cartographier cluster** — autres adresses probablement contrôlées, mises en relation avec autres acteurs.

**Intégration dans rapport** : adresses observées listées comme IoC, graphes de flux, identification des exchanges traversés, évaluation du profil financier (volumes, fréquence, patterns).

Le cours **OSINT Crypto** couvre cette discipline en profondeur.

---
