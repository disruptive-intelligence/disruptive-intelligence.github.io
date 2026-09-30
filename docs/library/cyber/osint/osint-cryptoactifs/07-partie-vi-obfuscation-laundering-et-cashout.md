---
title: PARTIE VI — OBFUSCATION, LAUNDERING ET CASHOUT
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
chapter: 7
chapters: 10
---

> **Ce que cette partie apprend.** Comprendre les techniques d’obfuscation utilisées par les acteurs criminels pour casser la traçabilité on-chain. Mixers et tumblers, CoinJoin, bridges cross-chain, DEX et swaps, privacy coins. Pour chaque technique : fonctionnement, ce qui reste observable, ce qui devient opaque, et signaux exploitables.
> 
> **Ce qu’elle ne couvre pas.** Les cas pratiques déroulés (Partie VII), les cas historiques (Partie VIII), la production de rapport (Partie IX).
> 
> **Ce que vous saurez faire après cette partie.** Reconnaître chaque technique d’obfuscation à sa signature on-chain. Évaluer ce qui reste analysable malgré l’obfuscation. Calibrer la confiance dans les conclusions face à des techniques mixtes. Identifier les opportunités défensives (gel d’actifs, coopération exchanges).

-----

## Chapitre 30 — Le cashout : où l’on quitte l’on-chain

Le **cashout** est le moment où les fonds quittent la blockchain pour entrer dans le monde fiat (ou être consommés sous forme de biens/services). C’est **le maillon le plus important** pour l’enquêteur et le plus vulnérable pour le criminel.

### 30.1 Pourquoi le cashout est central

**Pour le criminel** : le crypto en lui-même est rarement « utile ». Pour acheter une voiture, payer un loyer, financer une opération, il faut **convertir** en monnaie utilisable.

**Pour l’enquêteur** : le cashout est où le KYC entre en jeu. Les exchanges régulés exigent identification. Le moment du cashout est souvent **le seul** où on peut relier une adresse blockchain à une identité civile.

**Stratégique** : si l’enquête identifie le cashout, elle a identifié **l’angle d’attaque** des autorités — réquisition pour KYC, gel de fonds, identification.

### 30.2 Les méthodes de cashout

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

### 30.3 Reconnaître les patterns de cashout

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

### 30.4 Coopération avec les exchanges

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

### 30.5 Mules et réseaux de cashout

**Mules** : individus utilisés pour recevoir / convertir des fonds illicites.

**Mode de recrutement** :

- Annonces fausses « gagnez de l’argent en travaillant à domicile ».
- Romance scam (la mule est elle-même victime).
- Recrutement direct via Telegram / forums.
- Coercition / trafic humain (cas extrêmes, pig butchering compounds).

**Implications** :

- La mule peut être identifiée KYC sur exchange, mais l’**enquête remonte à la mule**, pas au cerveau.
- Coopération de la mule (si pas complice consciente) peut donner indications sur les commanditaires.

### 30.6 Limites OSINT au cashout

**Le KYC est off-chain**. L’analyste OSINT identifie l’adresse de dépôt exchange, mais **ne peut pas** accéder aux données KYC sans réquisition légale.

**Identification finale = autorités**. OSINT prépare le terrain (« cette adresse a déposé chez exchange X »), autorités opèrent la requête.

**Délais**. Entre identification du cashout et obtention du KYC, plusieurs semaines/mois peuvent passer. Pendant ce temps, les fonds peuvent avoir été déjà retirés.

**Multi-juridiction**. Réquisitions internationales sont lentes. Coopération variable selon juridiction.

### 30.7 Le cashout comme point d’attention défensif

Pour défense :

**Monitoring de cashout**. Pour fonds tracés à des activités illicites, alerter dès que mouvement vers exchange régulé connu = opportunité de gel.

**Coopération sectorielle**. Exchanges qui partagent informations (FATF Travel Rule, ISACs financiers) accroissent capacité collective.

**AML automation**. Outils intégrés (Chainalysis KYT, TRM, Elliptic Discovery) permettent screening en temps réel des dépôts.

### 30.8 Le message à intérioriser

> Le cashout est souvent le moment le plus intéressant pour l’enquête, mais aussi celui où l’OSINT atteint ses limites sans coopération d’un VASP ou réquisition.

L’OSINT identifie. Les autorités agissent. La coopération entre les deux est le multiplicateur de capacité.

### 30.9 Fil rouge — MIXSHADOW : les cashouts identifiés

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

## Chapitre 31 — Mixers et tumblers

Les **mixers** (ou tumblers) sont des services qui mélangent les fonds de multiples utilisateurs pour casser la traçabilité. Ils existent depuis les premiers jours du Bitcoin. Plusieurs ont été démantelés ; d’autres continuent. Ce chapitre couvre leur fonctionnement et limites de l’analyse.

### 31.1 Qu’est-ce qu’un mixer

**Principe** : un mixer reçoit les fonds d’utilisateur A et lui restitue, après délai, des fonds **différents** (issus d’autres utilisateurs B, C, D, etc.) à une adresse de destination différente.

**Effet** : casser le lien direct entre origine des fonds et destination. Si A a déposé 1 BTC entaché et reçoit 1 BTC « propre » (anciennement détenu par B), le lien on-chain entre origine et destination est rompu.

**Types** :

- **Mixers custodial** : service centralisé qui détient les fonds pendant le mélange. Tornado Cash (originellement), Helix, Bitcoin Fog, Chipmixer, Samourai Whirlpool partiellement.
- **CoinJoin (peer-to-peer, non-custodial)** : protocole coopératif sans custodian central. Wasabi, Samourai. Cf Ch.32.

**Différence** :

- Custodial : confiance dans l’opérateur (qui peut voler les fonds).
- Non-custodial : pas de risque de vol, mais moins « profond » comme mélange.

### 31.2 Fonctionnement d’un mixer custodial classique

Schéma type (mixer historique type Helix, Bitcoin Fog) :

**Étape 1 — Dépôt**. Utilisateur envoie ses BTC à une adresse fournie par le mixer.

**Étape 2 — Pool**. Les fonds sont agrégés dans un pool central.

**Étape 3 — Délai**. Le mixer attend un délai variable (heures à jours) pour que d’autres dépôts arrivent.

**Étape 4 — Restitution**. Le mixer envoie à l’utilisateur, depuis le pool, des BTC issus d’autres dépôts. Souvent via plusieurs petites transactions vers adresses fournies par l’utilisateur.

**Étape 5 — Fees**. Le mixer prélève une commission (1-5% typiquement).

**Failles** :

- **Confiance** : l’opérateur peut voler.
- **Logs internes** : si saisi, les logs peuvent dé-mixer (cf saisie Helix, Bitcoin Fog, Chipmixer).
- **Patterns observables** : timing, montants, adresses peuvent permettre des inférences statistiques.

### 31.3 Tornado Cash : le mixer décentralisé

**Tornado Cash** (lancé août 2019) est un mixer **non-custodial** sur Ethereum, basé sur **zero-knowledge proofs**. Référence du genre.

**Fonctionnement** :

**Pool fixe** : Tornado opère par pools de montants fixes (0,1 ETH, 1 ETH, 10 ETH, 100 ETH).

**Dépôt** :

- Utilisateur génère un **secret** (note) localement.
- Calcule le **hash du secret** (commitment).
- Appelle `deposit(commitment)` sur le smart contract pool, en envoyant le montant fixe.
- Smart contract enregistre le commitment dans un Merkle tree.

**Délai** : utilisateur attend (recommandation : plusieurs jours à semaines pour maximiser anonymat).

**Retrait** :

- Utilisateur génère un **proof zero-knowledge** prouvant qu’il connaît le secret correspondant à un commitment dans le Merkle tree, **sans révéler lequel**.
- Appelle `withdraw(proof, recipient)` sur le smart contract.
- Smart contract vérifie le proof, marque le commitment comme « spent », et envoie le montant fixe au `recipient`.

**Effet** : depuis l’extérieur, on voit que A a déposé (transaction publique) et que X a retiré (transaction publique), mais le **lien entre A et X** est cryptographiquement caché.

**Anonymity set** : le degré d’anonymat dépend du **nombre de dépôts non-retirés** dans la pool au moment du retrait. Plus la pool est utilisée, plus l’anonymat est fort.

### 31.4 Sanctions OFAC sur Tornado Cash

**Août 2022** : OFAC sanctionne Tornado Cash. Justifications : usage massif par Lazarus et autres acteurs criminels, blanchiment de centaines de millions USD.

**Implications** :

- Adresses smart contracts Tornado sur SDN list.
- Interactions avec ces adresses depuis US persons = violation.
- Multiple plateformes (DEX, frontend wallets) ont retiré l’accès.
- Volume utilisateurs a chuté.

**Procès des développeurs** :

- **Alexey Pertsev** : développeur Tornado, arrêté Pays-Bas août 2022. **Condamné mai 2024** à 5 ans 4 mois prison pour blanchiment.
- **Roman Storm** : co-développeur, inculpé US août 2023. **Procès US 2024-2025** en cours, verdict attendu / partiellement rendu selon évolution.
- **Roman Semenov** : autre co-développeur, sanctionné OFAC 2023, en fuite.

**Débat** : développeurs de logiciel open source vs responsabilité légale. Tornado est code immutable, fonctionne sans intervention. Les développeurs ont écrit le code mais ne le contrôlent plus. Question juridique structurante.

### 31.5 Analyse statistique des sorties Tornado

Bien que Tornado casse le lien direct, **analyse statistique** peut réduire l’incertitude.

**Techniques** :

**Timing analysis** :

- Si dépôt à T0 et retrait à T0 + 5 minutes, et que peu d’autres dépôts ont eu lieu entre, lien probable.
- Si retrait correspond exactement au timing typique d’un opérateur connu, indication.

**Montant matching** :

- Si total dépôts = total retraits dans une fenêtre temporelle, possibilité de pairing.
- Plus complexe si l’utilisateur dépose / retire des montants non-uniformes.

**Address reuse** :

- Si l’adresse de retrait apparaît dans d’autres contextes liés à l’opérateur, indication.

**Funding source du gas** :

- Le gas pour le retrait Tornado est payé. Si la source de gas est traçable, indication sur l’utilisateur.

**Behavioral patterns** :

- Comportement post-retrait peut matcher patterns connus.

**Limites** : ces techniques produisent **probabilités**, pas certitudes. Pour cas avec petite anonymity set (dépôts/retraits peu nombreux dans la pool), efficacité plus forte. Pour pool très active, efficacité faible.

### 31.6 Mixers démantelés

**Helix** (saisi 2020) : opérateur Larry Harmon condamné, 11 M USD saisis.

**Bitcoin Fog** (saisi 2021) : opérateur Roman Sterlingov condamné en 2024.

**Chipmixer** (saisi mars 2023) : opération Allemagne / Belgique, 46 000 BTC (~2,7 Mrd EUR) saisis ou identifiés.

**Sinbad.io** (sanctionné OFAC novembre 2023) : successeur d’autres mixers démantelés.

**Samourai Wallet** (saisi avril 2024) : opérateurs Keonne Rodriguez et William Hill inculpés US.

**Pour l’enquêteur** : démantèlements créent **opportunités d’analyse** post-saisie. Logs récupérés permettent dé-mixage rétroactif. Multiple cas où des fonds ransomware historiques ont été tracés grâce à logs Helix / Bitcoin Fog post-saisie.

### 31.7 Méthode d’enquête face à un mixer

**Étape 1 — Reconnaître le mixer**. Dépôts vers adresses connues de mixers (labels outils pro, listes publiques).

**Étape 2 — Documenter le dépôt**. Timestamp, montant, adresse source, identifiant du pool / mixer.

**Étape 3 — Lister les retraits dans la pool autour du timing**. Pour pool active, peut être beaucoup. Pour pool peu active, peut être peu.

**Étape 4 — Analyse statistique**. Timing, montant, behavioral. Identifier candidats probables.

**Étape 5 — Croiser avec contexte externe**. Si l’opérateur est suspecté d’utiliser Tornado et a une adresse de retrait probable, vérifier cohérence.

**Étape 6 — Calibrer la confiance**. Pour analyse statistique pure, attribution rarement « probable » (souvent « possible » ou plus faible).

**Étape 7 — Rapport avec limites explicites**.

### 31.8 L’impact des sanctions sur l’usage

**Pre-sanctions août 2022** : Tornado Cash utilisé massivement, par Lazarus et nombreux autres acteurs. Volume mensuel : centaines de M USD.

**Post-sanctions** : volume a chuté drastiquement. Mais Tornado **continue à fonctionner** (code immutable). Acteurs critiques (Lazarus) continuent à l’utiliser malgré sanctions, acceptant la pression sur off-ramps.

**Migrations** : certains acteurs ont migré vers :

- Sinbad.io (avant sanctions OFAC).
- Mixers Bitcoin résiduels (Wasabi, Samourai pre-saisie).
- Bridges + DEX comme alternatives partielles.
- Privacy coins (Monero).

### 31.9 Stratégie défensive face aux mixers

**Côté exchange** : screening de dépôts pour détecter fonds tracés à mixers (KYT Chainalysis, équivalents). Refus d’acceptation ou alerting.

**Côté plateforme** : Many DEX et frontends ont implémenté blocages des adresses Tornado post-sanctions.

**Côté autorités** : poursuite des opérateurs (Pertsev, Storm), sanctions continues.

### 31.10 Fil rouge — MIXSHADOW : analyse Tornado

> **🔗 MIXSHADOW — Épisode 18 : limite de l’analyse Tornado**
> 
> Sarah revient sur les **dépôts Tornado** d’Akira (12 ETH cumulés sur 3 dépôts).
> 
> Elle applique l’analyse statistique :
> 
> **Anonymity set au moment des dépôts** : ~50-200 dépôts non-retirés par pool selon la fenêtre. Anonymity set moyen.
> 
> **Recherche de retraits candidats** :
> 
> - Sarah liste tous les retraits sur les pools 10 ETH et 1 ETH dans la fenêtre 3-30 jours post-dépôts Akira.
> - Total : ~120 retraits candidats à examiner.
> 
> **Filtrage par pattern** :
> 
> - Retraits avec timing très court post-dépôt (<1 jour) éliminés (probable autres utilisateurs avec patterns d’urgence — pas Akira qui semble patient).
> - Retraits vers adresses sanctionnées éliminés (autres acteurs).
> - Retraits vers adresses à patterns clairement non-criminels éliminés.
> 
> **Reste** : ~30 retraits candidats.
> 
> **Recoupement avec autres données MIXSHADOW** :
> 
> - Sarah compare les adresses de retrait avec les adresses Akira identifiées sur les autres branches.
> - **Aucune correspondance directe**.
> - **2 adresses « similaires »** dans le sens où elles montrent ensuite des patterns cohérents avec opérations de blanchiment Akira ultérieures.
> 
> **Calibration** :
> 
> - Attribution des **2 adresses comme retraits Akira probables** : confiance ~50% (« possible » fort, mais pas « probable » solide).
> - Autres retraits candidats : indéterminable sans données additionnelles.
> 
> Sarah documente dans le rapport :
> > « Sur les 12 ETH déposés à Tornado Cash, l’analyse statistique des retraits dans la fenêtre temporelle compatible identifie 2 candidats de retrait avec des patterns d’usage post-retrait cohérents avec les opérations Akira observées sur les autres branches. La confiance d’attribution est cependant limitée à « possible » (~50%). Pour les 10 ETH restants, aucun candidat avec confiance suffisante n’a été identifié. La rupture de visibilité induite par Tornado Cash limite intrinsèquement l’enquête sur cette branche. »
> 
> Calibration honnête. Pas de sur-attribution. Pas non plus de capitulation totale (les 2 candidats identifiés alimentent la fiche acteurs).
> 
> Sarah ajoute pour le rapport : **possibilité de coordination internationale** sur les 30 retraits candidats. Si la DGSI / FBI peuvent confronter ces 30 adresses à leurs propres données (renseignement, autres enquêtes), des matches peuvent émerger qui passeront du statut « possible » à « probable ». Cf Ch.43 — Tornado Cash dans le cas Ronin / Lazarus a été partiellement « démêlé » par cette approche multi-source.

-----

## Chapitre 32 — CoinJoin : Wasabi, Samourai

Le **CoinJoin** est une technique d’anonymisation Bitcoin différente des mixers custodial. Coopérative, non-custodial. Wasabi et Samourai sont les implémentations principales.

### 32.1 Principe du CoinJoin

**Idée** : multiple utilisateurs créent **collectivement une transaction** Bitcoin avec multiples inputs et outputs, sans révéler à un opérateur central qui possède quoi.

**Mécanisme simplifié** :

1. Plusieurs utilisateurs (5 à 100+ selon implémentation) coordonnent.
1. Chacun fournit des inputs (UTXO qu’il contrôle).
1. Tous signent une transaction agrégée.
1. Outputs sont mélangés : impossible de dire depuis l’extérieur quel input correspond à quel output.

**Exemple** :

- 10 utilisateurs, chacun 1 BTC en input (10 BTC total).
- Outputs : 10 × 1 BTC vers 10 nouvelles adresses.
- Heuristique du co-spend appliquée naïvement dirait : tous appartiennent à même entité. **C’est faux** dans le CoinJoin.

**Effet** : casser l’heuristique du co-spend. Chaque output, vu de l’extérieur, peut appartenir à n’importe quel input.

### 32.2 Wasabi Wallet

**Wasabi Wallet** est un wallet Bitcoin avec CoinJoin intégré. Implémentation **ZeroLink** (variante CoinJoin avec Chaumian e-cash).

**Caractéristiques** :

- Coordinator central (mais ne détient pas les fonds).
- Anonymity set fixe (~100 utilisateurs par round historiquement).
- Frais (sur le coordinator).

**Évolution** :

- Wasabi 1.0 : protocole ZeroLink pur.
- Wasabi 2.0 : WabiSabi, anonymity set plus flexible, frais plus bas.

**Réputation** : utilisé par utilisateurs privacy-conscious légitimes ET par criminels. Coordinator peut blacklister certains UTXO (controverse).

### 32.3 Samourai Wallet

**Samourai Wallet** : wallet Bitcoin alternatif, focus privacy.

**Whirlpool** : implémentation CoinJoin de Samourai. Différences :

- Anonymity set plus petit par round (5 utilisateurs).
- Mais cycles répétés pour augmenter anonymat cumulatif.
- Coordinator distinct.

**Saisie avril 2024** : opération US, fondateurs Keonne Rodriguez et William Lonergan Hill inculpés. Infrastructure saisie. Whirlpool stoppé.

**Implications** :

- Logs du coordinator récupérés permettent investigation rétroactive.
- Saisie envoie message sur acceptabilité légale des CoinJoin services, débat actif.

### 32.4 Détection de CoinJoin

**Signaux** :

**Multiple inputs et multiple outputs avec montants identiques**. Une transaction CoinJoin Wasabi typique : 100 inputs, 100 outputs de même valeur. Très distinctif.

**Coordinator address**. Wasabi prélève une fee qui va à un coordinator. Adresse identifiable.

**Patterns de timing**. Les CoinJoin ont des cycles temporels. Wasabi v2 fait des CoinJoin réguliers.

**Outils d’analyse** : KYCP.org analyse spécifiquement les CoinJoin. Détecte les transactions, calcule l’anonymity set, score la qualité du mix.

### 32.5 Limites du dé-mixage CoinJoin

**Heuristique cassée** : le co-spend dans CoinJoin n’est pas une indication d’entité commune. Outils pro **doivent détecter** les CoinJoin et **exclure** ces transactions du clustering. Reactor / TRM le font.

**Analyse possible mais limitée** :

- **Sub-mixing** : si l’anonymity set est petit (Whirlpool 5 inputs), inférence statistique partielle.
- **Toxic UTXO** : si un UTXO entré dans CoinJoin est entaché (par exemple, vient d’une adresse sanctionnée), le mélange CoinJoin ne « purifie » pas pour les autorités — les outputs gardent une « contamination » statistique.
- **Behavioral analysis** : patterns post-CoinJoin peuvent identifier l’utilisateur initial.

**Coordinator logs** : si coordinator coopère ou est saisi, logs permettent dé-mixage substantiel. Cas Samourai.

### 32.6 Wasabi vs mixers custodial

|Critère      |CoinJoin (Wasabi)                        |Mixer custodial (Tornado)                                                                 |
|-------------|-----------------------------------------|------------------------------------------------------------------------------------------|
|Custody      |Non-custodial                            |Custodial (Tornado est non-custodial via smart contract, autres mixers BTC sont custodial)|
|Risque de vol|Faible                                   |Élevé (mixers traditionnels)                                                              |
|Anonymat     |Modéré                                   |Variable                                                                                  |
|Logs         |Coordinator a logs (Wasabi)              |Variable                                                                                  |
|Légalité     |Moins claire mais usage légitime fréquent|Plus contestée                                                                            |
|Démantèlement|Wasabi continue, Samourai saisi          |Multiple démantèlements (Helix, BitcoinFog, ChipMixer, Tornado sanctionné)                |

### 32.7 Méthode d’enquête face à CoinJoin

**Étape 1 — Détecter le CoinJoin**. Outils pro indiquent. Manuellement : pattern de transaction (multiple in/out de même valeur).

**Étape 2 — Documenter**. Quelle implémentation (Wasabi v1, v2, Samourai), quel anonymity set, quel coordinator.

**Étape 3 — Continuer le tracking**. Outils pro continuent souvent à suivre la « probabilité » de chaque input vers chaque output (pas certain mais probabiliste).

**Étape 4 — Calibrer**. Confidence sur destinataires post-CoinJoin = limitée.

**Étape 5 — Coopération**. Pour cas critiques, demande au coordinator (si encore actif) ou récupération de logs post-saisie.

### 32.8 Tendances 2024-2026

**Saisie Samourai (avril 2024)** : impact majeur. Samourai était populaire. Migration vers Wasabi ou autres alternatives.

**Wasabi** : continue, mais sous pression. Coordinator en juridiction permissive pour minimiser risque. Updates régulières.

**Joinmarket** : alternative décentralisée (pas de coordinator central), moins user-friendly mais plus résiliente.

**Lightning Network** : autre approche privacy (pas CoinJoin technique, mais effet similaire — paiements off-chain limitent traçabilité on-chain).

**Pour l’enquêteur** : CoinJoin reste une **rupture analytique** sur Bitcoin, mais pas absolue. Combinaison avec autres indices et analyse temporelle / behavioral peut donner des angles.

-----

## Chapitre 33 — Bridges et cross-chain laundering

Les **bridges** sont des protocoles permettant de transférer des actifs entre blockchains. Ils sont **infrastructure légitime** mais aussi vecteur majeur de blanchiment et de hacks. Comprendre leur fonctionnement et leurs limites pour l’enquête est central.

### 33.1 Pourquoi les bridges existent

**Problème** : un Bitcoin natif ne peut pas exister directement sur Ethereum. Une USDT ERC-20 (Ethereum) ne peut pas être directement transférée à une adresse TRC-20 (TRON). Les blockchains sont **isolées** par construction.

**Solution** : bridges permettent de « migrer » un actif d’une chaîne à une autre, par mécanismes variés.

**Mécanismes** :

**Wrapped tokens** : sur la chaîne destinataire, un token « wrapped » est créé représentant l’actif natif de la chaîne source. Exemple : WBTC (Wrapped Bitcoin) sur Ethereum est un ERC-20 dont la valeur correspond à du BTC réel détenu en custody.

- Étapes : utilisateur dépose BTC sur custody → mint WBTC sur Ethereum → utilise WBTC dans DeFi → burn WBTC + retrait BTC depuis custody.

**Lock-and-mint** : actif locké sur chaîne source, équivalent miné sur chaîne destinataire.

**Burn-and-mint** : actif burned sur chaîne source, miné sur chaîne destinataire.

**Liquidity pools cross-chain** : pools de liquidité présents sur multiples chaînes, swap effectif entre chaînes.

**Intermediate exchanges** : non un « bridge » technique, mais effet équivalent — passer par exchange centralisé pour switch entre chaînes.

### 33.2 Bridges majeurs

**Wormhole** : Ethereum, Solana, BNB, Avalanche, Polygon, etc. Hack majeur février 2022 (326 M USD).

**Multichain (anciennement Anyswap)** : multi-chain. Compromis 2023, ~130 M USD volés dans circumstances opaques.

**Stargate** : LayerZero-based, multi-chain.

**Synapse** : multi-chain.

**Hop Protocol** : Layer-2 Ethereum focus.

**Across** : multi-chain, optimistic.

**deBridge** : multi-chain.

**Rainbow Bridge** (Aurora / NEAR) : Ethereum-NEAR.

**WBTC** : centralisé, Bitcoin → Ethereum.

**RenBTC** : décentralisé, multi-chain BTC. RenVM stoppé en 2023, mais cf forks.

**THORChain** : decentralized cross-chain swaps. Multiple incidents et reprises.

**FixedFloat, ChangeNOW, SimpleSwap** : services de swap cross-chain non-KYC. Différents techniquement (intermediaires opérant des pools propres) mais effet bridge utilisateur.

**Pour l’enquêteur** : la liste évolue rapidement. Vérifier la couverture par les outils pro.

### 33.3 Pourquoi les bridges sont attractifs pour le blanchiment

**Casser la chaîne**. Un fonds passe d’Ethereum à BNB Chain via bridge. Suivre cross-chain demande capacité spécifique.

**Multi-juridictionnel**. Différentes blockchains ont différents écosystèmes (régulés / non-régulés, KYC / non-KYC). Bridge permet de glisser du « monitoré » au « moins monitoré ».

**Faible KYC**. Bridges typiques sont smart contracts non-custodial — pas de KYC.

**Vitesse**. Bridge typique : minutes à heures. Plus rapide que conversion via exchange centralisé.

**Volume liquide**. Multi-billion USD passent par bridges quotidiennement. Fonds illicites se fondent dans le bruit.

### 33.4 Hacks de bridges

Les bridges ont été ciblés massivement pour leurs vulnérabilités.

**Top hacks** :

- **Ronin** (mars 2022, 625 M USD) — Lazarus.
- **Wormhole** (février 2022, 326 M USD).
- **Nomad** (août 2022, 190 M USD).
- **Multichain** (juillet 2023, 130 M USD) — circumstances opaques.
- **Harmony Bridge** (juin 2022, 100 M USD) — Lazarus.
- **Orbit Chain** (janvier 2024, 80+ M USD).
- **Multiple autres** 2023-2026.

**Pourquoi cibles** :

- **Concentration de fonds** : bridges détiennent des centaines de millions USD en custody.
- **Code complexe** : surfaces d’attaque larges.
- **Validators externes** : si compromis, takeover possible.
- **Monitoring limité** : moins de regards techniques que sur protocoles DeFi mainstream.

**Pour l’enquêteur** : un hack de bridge nécessite **tracking cross-chain** intensif. Les attaquants utilisent les fonds pour disperser sur multiple chaînes immédiatement.

### 33.5 Suivre un fonds à travers un bridge

**Méthode** :

**Étape 1 — Identifier la transaction de dépôt sur chaîne source**. Adresse utilisateur → smart contract bridge.

**Étape 2 — Consulter les logs / events du bridge**. Le bridge émet un event décrivant la transaction destinataire (chaîne, adresse, montant).

**Étape 3 — Identifier la transaction correspondante sur chaîne destinataire**. Souvent quelques minutes à heures plus tard. Rechercher par adresse destinataire et montant.

**Étape 4 — Continuer le suivi sur la nouvelle chaîne**.

**Outils pro** : Reactor / TRM / Elliptic suivent automatiquement les bridges majeurs. Mais couverture variable selon bridge et selon outil.

**Outils gratuits** : pour bridges populaires (Stargate, Across), sites comme `socket.tech` ou `debridge.finance` ont des explorateurs cross-chain. Utile pour traçage manuel.

### 33.6 Limites du tracking cross-chain

**Pas tous les bridges sont supportés** par les outils pro. Bridges obscurs ou spécialisés peuvent passer sous le radar.

**Délai de résolution**. Sur certains bridges, le matching entre dépôt et retrait est différé. L’analyste peut perdre la trace si pas vigilant.

**Multiple hops cross-chain**. Fonds qui passent ETH → BSC → TRON → Polygon → ETH représentent une chaîne compliquée à suivre. Erreurs possibles à chaque saut.

**Liquidity pools** : les bridges via pools (Stargate, etc.) ne maintiennent pas un mapping 1-to-1 entre dépôts et retraits. Fonds entrent dans un pool, autres fonds sortent — l’utilisateur reçoit des fonds différents (en termes de UTXO).

**Wrapped tokens et redemption**. Un utilisateur peut wrap, déwrap, re-wrap — multiple cycles brouillent.

### 33.7 Tracking spécifique par bridge

**Wormhole** : explorateur Wormhole Scan permet de matcher transactions cross-chain. Émet events détaillés.

**Stargate** : Stargate Finance interface, transactions traçables via LayerZero events.

**Multichain** : historiquement traçable, mais post-compromis 2023, situation chaotique.

**WBTC / wrapped centralisés** : custody centralisée, mints et burns visibles. Mais pour suivre quel BTC correspond à quel WBTC, custody internal logs nécessaires.

**FixedFloat / ChangeNOW** : pas de matching public direct (services internalisent). Suivi par timing et montant possible mais probabiliste.

### 33.8 Coopération avec opérateurs de bridges

**Bridges decentralisés** : pas d’opérateur central à qui demander coopération. Smart contract immutable.

**Bridges semi-centralisés** (multisig validators, custodial) : peuvent coopérer sur réquisition. Cas variés.

**Wrapped tokens centralisés** (WBTC) : custody peut coopérer. WBTC custody (BitGo) coopère avec autorités sur cas légaux.

**FixedFloat / ChangeNOW / similaires** : politique de KYC / coopération variable. Souvent limitée.

### 33.9 Tendances 2024-2026

**Bridges restent vulnerables** : continuent à se faire hacker régulièrement.

**Sophistication de tracking** : Reactor / TRM / Elliptic améliorent couverture cross-chain. Mais lag sur nouveaux bridges.

**Régulation** : MiCA en EU pourrait éventuellement imposer KYC sur bridges, mais débat actif. Les bridges décentralisés posent question juridique (qui régule un smart contract ?).

**Layer-2 et bridges natifs** : Arbitrum, Optimism, Base bridges ont architectures différentes (rollups), tracking spécifique.

### 33.10 Fil rouge — MIXSHADOW : tracking cross-chain Akira

> **🔗 MIXSHADOW — Épisode 19 : la branche cross-chain**
> 
> Sarah a tracé une **branche secondaire** dans MIXSHADOW : ~5 BTC depuis le peeling chain ont été convertis via FixedFloat en USDT-Ethereum. Ces USDT ont ensuite été bridgés via **Stargate** vers BNB Chain.
> 
> **Tracking** :
> 
> - Transaction Ethereum : USDT-ETH → Stargate router contract.
> - Event Stargate : transfer to BNB Chain, destination address `0x[BNB-Akira]`.
> - Transaction BNB Chain : USDT-BNB reçus quelques minutes plus tard.
> 
> Reactor a suivi automatiquement. Validation manuelle via Stargate Finance interface confirme la correspondance.
> 
> Sur BNB Chain, suite : USDT-BNB swappés via DEX en BUSD (Binance USD), puis transférés vers adresses dépôt Binance. **3 dépôts Binance** identifiés sur cette branche.
> 
> **Coopération** : ces 3 adresses Binance (avec USDT cumulés ~30 000 USDT équivalent) sont transmises à la DGSI pour réquisition KYC. **2 mules identifiées** (cf Ch.30.9). Coopération Binance-DGSI productive.
> 
> Sarah note dans le rapport : la **branche cross-chain** Akira est plus modeste en volume (~5 BTC sur 35) que la branche TRON-USDT (~3 BTC qui sont devenus 290k USDT). Mais elle est **plus traçable** parce que Stargate est bien couvert par les outils et Binance KYC est solide. Paradoxe : le criminel qui choisit la « simplicité » (Stargate + Binance) est plus exposé que celui qui choisit le « non-KYC + dispersion » (FixedFloat + exchange non-KYC + hubs TRON). Akira a fait les deux choix sur des branches différentes — diversification des risques pour l’opérateur.
> 
> Cette observation (Akira diversifie les chemins de blanchiment) alimente la fiche acteur Akira pour la base Athéna et CTI sectoriel.

-----

## Chapitre 34 — DEX, swaps et obfuscation DeFi

Les **DEX** (decentralized exchanges) et plus largement les **protocoles DeFi** offrent des outils additionnels d’obfuscation. Plus subtils que mixers ou bridges, ils permettent transformations d’actifs et brouillage des origines.

### 34.1 Les principaux DEX

**Uniswap** (Ethereum) : référence. Multi-version (V2, V3, V4). Pools de liquidité automated market maker (AMM).

**SushiSwap** : fork Uniswap, multi-chain.

**Curve Finance** : spécialisé stablecoins et actifs corrélés. Faible slippage sur paires similaires.

**PancakeSwap** : leader sur BNB Chain. Équivalent Uniswap.

**Balancer** : pools customisables, multi-actifs.

**1inch, Matcha, Paraswap** : aggregators (routent à travers multiple DEX pour meilleur prix).

**dYdX, GMX** : DEX dérivés (perpétuels, options).

**Trader Joe** : DEX Avalanche.

**Raydium, Orca, Jupiter** : DEX Solana.

**SunSwap, JustLend** : écosystème TRON.

### 34.2 Pourquoi les DEX permettent obfuscation

**Pas de KYC**. Smart contracts non-custodial. Pas d’identité requise.

**Conversion d’actifs**. ETH → USDT en quelques secondes. Brouille l’origine.

**Liquidité massive**. Volumes énormes. Fonds illicites se fondent dans le bruit.

**Multi-pool / multi-route**. Aggregators routent via plusieurs pools. Trace plus complexe.

**Multi-chain**. Combinaison DEX + bridge donne transformations multi-chaînes.

### 34.3 Patterns d’obfuscation via DEX

**Conversion simple**. Adresse reçoit ETH suspect, swap en USDT, USDT déposé sur exchange → KYC trace plus difficile.

**Multi-hop**. ETH → USDT → DAI → USDC → ETH. Multiple swaps redondants avant l’objectif. Brouille analyse simple.

**Yield farming intermédiaire**. Dépôt en pools de liquidité, claim de fees, retrait. Crée de l’historique « DeFi natural » qui peut tromper analyse superficielle.

**Flash loan layering**. Plus avancé : utilisation de flash loans pour manipulation de pools / arbitrage. Les fonds passent par multiple protocoles en une seule transaction.

### 34.4 Tracker un swap DEX

**Étape 1 — Identifier la transaction de swap**. Sur Etherscan, transaction qui appelle un DEX router.

**Étape 2 — Lire les logs**. Events `Swap` indiquent montants et tokens d’entrée/sortie.

**Étape 3 — Comprendre la route**. Aggregators peuvent passer par 2-5 pools en une transaction. Analyser tous les hops.

**Étape 4 — Continuer le tracking sur les fonds reçus**. Adresse user reçoit le token de sortie.

**Outils pro** : Reactor / TRM / Elliptic suivent automatiquement à travers DEX. Excellente couverture pour DEX mainstream.

**Outils gratuits** : Etherscan affiche transactions DEX bien décodées si contrats vérifiés (presque toujours le cas pour DEX majeurs).

### 34.5 Limites

**Multi-hop complexe**. Un aggregator routant via 5 pools est plus difficile à parser visuellement (mais bien décodé par les outils).

**MEV (Maximal Extractable Value)**. Les bots MEV peuvent intervenir dans les transactions, complexifiant l’analyse.

**Liquidity provider activity**. Si le criminel agit comme LP (provide liquidity), ses fonds sont mélangés avec la liquidité globale du pool. Tracking devient probabiliste.

**Pool extractables**. Certains LPs custodial peuvent retirer (par exemple, récupération fonds d’une pool LP), brouillant les traces.

### 34.6 Cas typiques

**Hack DeFi → swap rapide**. Attaquant draine un protocole DeFi, swap rapidement les tokens volés en stablecoin ou ETH (plus liquide), puis suit chemin classique d’obfuscation. Vu dans nombreux hacks 2022-2026.

**Pig butchering → swap pré-cashout**. Fonds USDT-TRON consolidés peuvent être swappés en autres stablecoins ou BTC pour faciliter cashout sur certaines plateformes.

**Ransomware → swap pour anonymisation**. Cf MIXSHADOW : Akira a swappé partiellement BTC en ETH via FixedFloat avant Tornado Cash.

### 34.7 Différence DEX vs CEX vs swap services

**DEX** (Uniswap, etc.) : smart contract pur. Pas de KYC. Pas d’opérateur central pour coopération.

**CEX** (Binance, etc.) : entreprise centralisée. KYC. Possible coopération.

**Swap services** (FixedFloat, ChangeNOW, SimpleSwap) : services qui permettent swap sans KYC mais avec opérateur central. Hybrides — pas vraiment décentralisés (l’opérateur peut blacklister, refuser), pas vraiment KYC. Souvent utilisés pour cross-chain rapide. Coopération variable selon service.

### 34.8 Tendances 2024-2026

**Volume DEX en croissance**. DeFi mature, plus d’utilisateurs.

**Cross-chain DEX** : 1inch Cross-chain, autres aggregators cross-chain.

**Régulation** : MiCA cible exchange centralisés, mais DEX est zone grise. Débat actif.

**Réseaux MEV-dominants** : MEV-Boost et auctions deviennent partie intégrale de l’écosystème, complexifiant l’analyse.

**Pour l’enquêteur** : DEX est **moins une rupture de visibilité qu’un détour traçable**. Ne pas avoir peur, mais ajouter au temps d’analyse.

-----

## Chapitre 35 — Privacy coins : Monero, Zcash, limites radicales

Les **privacy coins** sont des cryptomonnaies conçues pour l’anonymat. Contrairement à Bitcoin (pseudonyme) ou aux mixers (obfuscation ajoutée), les privacy coins ont l’anonymat **par construction**. Ce chapitre couvre les principales et leurs implications pour l’enquête.

### 35.1 Monero (XMR)

**Lancé** : avril 2014 (fork de Bytecoin).

**Principes** :

**Ring signatures**. Chaque transaction Monero contient des signatures multiples — la vraie + plusieurs « decoys » (faux signataires plausibles). Impossible de savoir quel signataire est le vrai. Effet : l’**émetteur** d’une transaction est ambigu parmi un ring de candidats.

**Ring Confidential Transactions (RingCT)**. Les **montants** sont cachés cryptographiquement. Visible : « cette transaction transfère un montant X ». Pas visible : la valeur de X.

**Stealth addresses**. Le **destinataire** d’une transaction est caché. Adresse de réception « one-time » dérivée pour chaque transaction. Lien entre adresse on-chain et destinataire réel non-trivial.

**Effet combiné** : émetteur masqué, montant masqué, destinataire masqué. Quasi-anonymat.

**Adoption** : populaire dans dark web markets, ransomware (certains exigent Monero), particuliers privacy-conscious.

### 35.2 Limites de Monero

**Pas absolument anonyme** :

**Decoy quality**. Les decoys sont sélectionnés selon algorithme. Si l’algorithme a des biais ou si le ring inclut decoys peu plausibles (par exemple, decoys « trop vieux »), analyse statistique peut réduire l’incertitude. Recherche académique active.

**Vulnérabilités d’implémentation**. Certaines versions de Monero ont eu des vulnérabilités permettant dé-anonymisation partielle. Patches successifs.

**Usage off-chain**. Si l’utilisateur achète Monero sur exchange KYC, l’achat est traçable. La conversion en autres actifs après usage Monero est aussi un point.

**Erreurs OPSEC**. Réutilisation de wallets avec multiple couches d’obfuscation peut leak. Patterns d’usage peuvent identifier acteur.

**Decoy attacks** : des chercheurs ont publié plusieurs papers sur dé-anonymisation partielle Monero. Exemples : sélection de decoys old enough to be unrealistic, timing analysis sur outputs.

**Pour l’enquêteur** : Monero est **largement opaque** pour l’analyse on-chain pure. L’enquête se déplace vers les **points off-chain** (exchanges, achats fiat, OPSEC errors).

### 35.3 Zcash (ZEC)

**Lancé** : octobre 2016.

**Principes** :

**zk-SNARKs** : zero-knowledge proofs avancés permettant transactions complètement privées (montants, parties cachés).

**Mode dual** :

- **Transparent** : transactions comme Bitcoin, lisibles publiquement.
- **Shielded** : transactions privées via zk-SNARKs.

**Adoption** : majoritairement transparent. La fraction shielded est faible. Des recherches indiquent que les transactions Zcash sont à >80% transparentes.

### 35.4 Limites Zcash

**Mode transparent** : analysable comme Bitcoin.

**Mode shielded** : opaque, mais **anonymity set faible** (peu d’utilisateurs en mode shielded). Patterns d’entrée/sortie shielded peuvent réduire l’incertitude.

**Trusted setup** : Zcash early required a trusted setup ceremony. Si la randomness a été compromise, attaque théorique possible. Ceremonies multiples, peu probable d’être compromis pour les versions récentes.

**Pour l’enquêteur** : Zcash est **moins opaque que Monero en pratique** parce que l’usage shielded est minoritaire. Pour transactions transparentes, méthode standard. Pour shielded, limites similaires à Monero.

### 35.5 Dash et autres

**Dash** (lancé 2014) : « PrivateSend » est CoinJoin amélioré. Moins efficace que Monero, plus simple à analyser.

**Beam, Grin** (lancés 2019) : implémentent Mimblewimble. Concept différent (no addresses, transactions agrégées). Adoption faible.

**Pirate Chain (ARRR)** : zk-SNARKs forced (pas de mode transparent). Faible volume.

**Pour l’enquêteur** : Monero domine clairement le segment privacy. Autres rares en pratique.

### 35.6 Méthode d’enquête face à Monero

**Étape 1 — Reconnaître la rupture**. Si fonds passent en Monero, traçabilité on-chain quasi-impossible.

**Étape 2 — Documenter la rupture**. « À l’étape N, fonds convertis en Monero via [exchange/swap]. Au-delà, traçabilité on-chain non possible sans données off-chain. »

**Étape 3 — Identifier les points off-chain** :

- **Achat de Monero** : comment ont-ils été obtenus ? Si depuis exchange KYC, identité achat traçable.
- **Vente de Monero** : si reconvertis en autre actif via exchange, identité vente traçable.
- **OPSEC errors** : réutilisation, patterns, mentions publiques.

**Étape 4 — Inférer ce qui peut être inféré** :

- Si fonds entrent en Monero à T0 et un autre acteur reconvertit Monero en USDT à T0+5min via même exchange, **possible** lien.
- Pas certain — coïncidence possible.

**Étape 5 — Calibrer**. Confidence sur attribution post-Monero = très limitée sans autres données.

**Étape 6 — Coopération**. Si Monero a été obtenu/vendu via exchange KYC, réquisition possible. Si privé tout du long, impasse OSINT.

### 35.7 Cas réels Monero

**Ransomware Monero-only** : Akira (cf MIXSHADOW), REvil (historique), DarkSide variantes. Demandent paiement en XMR pour rupture immédiate.

**Darknet markets** : multiple marchés russophones et anglophones acceptent ou exigent Monero.

**Acteurs étatiques Lazarus** : utilisation de Monero documentée pour certaines opérations.

**Limitation** : exchanges régulés ont **massivement délistsé Monero** depuis 2020. Coinbase, Kraken, Binance ont retiré Monero. Cela limite cashout pour criminels (plus difficile de revenir en fiat sans suspicion). Effet partiel — exchanges secondaires et P2P continuent.

### 35.8 Tendances 2024-2026

**Pression réglementaire** : Monero ciblé par autorités. Multiples démarches pour limiter accessibilité.

**Améliorations techniques Monero** : protocole évolue (Bulletproofs, Triptych, autres). Augmente anonymat.

**Recherche académique active** : papers réguliers sur dé-anonymisation partielle.

**Migration** : certains acteurs criminels migrent vers Monero alternatives ou vers techniques mixtes (Bitcoin + privacy layers comme Lightning Network ou CoinJoin chained).

### 35.9 Le message à intérioriser

> Monero est une rupture de visibilité quasi-totale pour l’analyse on-chain. L’enquêteur OSINT honnête le reconnaît, le documente, et déplace l’enquête vers les angles off-chain. Promettre un « démêlage » Monero = sur-promesse risquée.

### 35.10 Fil rouge — MIXSHADOW : pas de Monero pour Akira… cette fois

> **🔗 MIXSHADOW — Épisode 20 : absence de Monero**
> 
> Akira accepte généralement les paiements en Bitcoin (selon docs récentes du groupe). Le paiement Aurélien Médical était en BTC, comme négocié.
> 
> Sarah note cependant que **certains autres acteurs ransomware** exigent Monero (REvil historique, certains affiliés ciblés). Dans le cadre d’Akira spécifiquement, Bitcoin domine.
> 
> Si Akira avait demandé du Monero, l’enquête MIXSHADOW serait **très différente** :
> 
> - Traçabilité on-chain quasi nulle au-delà de la conversion BTC → XMR.
> - Enquête se serait déplacée vers : analyse de l’exchange où conversion XMR/USD effectuée, points OPSEC d’Akira, ciblage de cashout fiat.
> - Couverture beaucoup plus faible (~10-20% des flux possibles à tracer vs ~75% atteints en BTC).
> - Rapport aurait conclu rapidement sur **rupture de visibilité** et pivot vers angles off-chain.
> 
> Sarah documente dans le rapport final :
> > « Le choix Bitcoin par Akira pour le paiement Aurélien Médical, plutôt que Monero, a permis une investigation crypto-forensique substantielle. Si Akira avait imposé Monero (comme certains autres opérateurs ransomware), la traçabilité on-chain aurait été drastiquement réduite. Cette observation suggère qu’Akira accepte un compromis traçabilité / facilité opérationnelle, peut-être par contrainte de liquidité (BTC plus liquide / acceptable pour victimes), peut-être par sous-estimation de la capacité forensique. »
> 
> Insight : pour victimes futures d’Akira, négocier paiement en BTC plutôt qu’en Monero peut être un angle (si négociation possible, ce qui n’est pas toujours le cas — l’opérateur impose).
> 
> La Partie VII va dérouler **5 cas pratiques** complets pour appliquer toutes les méthodes apprises.

-----
