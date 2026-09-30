---
title: PARTIE VII — CAS PRATIQUES DÉROULÉS
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
chapter: 8
chapters: 10
---

> **Ce que cette partie apprend.** Voir 5 enquêtes complètes déroulées bout en bout, depuis l’indice initial jusqu’au rapport. Chaque cas mobilise toutes les méthodes des Parties précédentes en contexte. Cas fictifs construits pédagogiquement pour montrer la méthode pure ; les cas historiques réels sont en Partie VIII.
> 
> **Ce qu’elle ne couvre pas.** Théorie (déjà vue). Cas historiques (Partie VIII).
> 
> **Ce que vous saurez faire après cette partie.** Conduire vous-même une investigation crypto en suivant les méthodes apprises. Adapter aux typologies (pig butchering, ransomware, drainer, multi-chain, Monero). Anticiper les difficultés et calibrer vos conclusions.

-----

## Chapitre 36 — Cas 1 : victime de pig butchering USDT Tron

**Profil de l’enquête** : enquête typique sur un cas individuel de pig butchering. Volume modeste (~200 000 USD), pattern reconnaissable, méthode standard.

### 36.1 Le contexte

Marie (nom d’emprunt), 52 ans, cadre supérieure dans une PME française, contacte un cabinet d’investigation après réalisation d’une fraude. Elle a été victime d’une opération de pig butchering sur 4 mois (octobre 2025 - février 2026).

**Récit factuel** (synthétisé à partir du briefing client) :

- Octobre 2025 : Marie est contactée sur Instagram par un certain « Daniel Wang », se présentant comme entrepreneur à Singapour. Approche amicale, pas de demande financière initiale.
- Novembre 2025 : la relation devient amicale-puis-sentimentale (à distance). Daniel partage des « histoires » de succès en investissement crypto.
- Décembre 2025 : Daniel introduit Marie à une « plateforme exclusive » d’investissement DeFi, gérée par un « ami fonds ». Premier dépôt suggéré : 3 000 USDT.
- Janvier 2026 : la plateforme montre des « gains » de 30% en deux semaines. Marie augmente : 15 000 USDT, puis 50 000 USDT.
- Février 2026 : Marie liquide une partie de son épargne et investit 130 000 USDT supplémentaires.
- Mi-février : Marie tente un retrait de 50 000 USDT. La plateforme demande une « caution fiscale » de 20 000 USDT pour débloquer. Marie refuse et tente de contacter Daniel. Plus de réponse. Plateforme inaccessible.

**Total perdu** : ~198 000 USDT (~ 198 000 EUR au cours du moment).

Marie a porté plainte (gendarmerie locale + signalement Pharos + cybermalveillance.gouv.fr). Elle mandate un cabinet privé pour cartographier les flux et préparer un dossier solide pour la procédure.

### 36.2 Le cadrage de la mission

**Objectifs** :

1. Confirmer les flux on-chain depuis Marie vers la plateforme frauduleuse.
1. Identifier l’écosystème : autres victimes probables, opérateurs derrière la plateforme, points de cashout.
1. Identifier les **angles d’action** des autorités (exchanges traversés, demandes de gel possibles).
1. Produire un **rapport actionnable** pour soutien à la procédure judiciaire.

**Limites** :

- Pas d’identification civile espérée (compounds Asie du Sud-Est probables).
- Récupération des fonds peu probable (déjà 2 mois après dernier paiement).
- Mission OSINT pure, pas d’engagement direct avec scammer.

**Budget** : 15 jours analyste senior, ~25 000 EUR.

**Cadre légal** : mission privée mandatée, RGPD respecté, livrables transmissibles à autorités.

### 36.3 Phase 1 — Collecte initiale

**Inputs fournis par Marie** :

- 18 transactions USDT-TRON (sur 4 mois).
- TXIDs de chacune.
- Captures de l’app de la plateforme frauduleuse (avec adresses de dépôt).
- Captures des conversations Instagram avec Daniel.
- Photos partagées par Daniel (à analyser pour reverse image search).

**Étape 1 — Vérification on-chain**.

L’analyste ouvre Tronscan et vérifie les 18 transactions. Toutes confirmées. Total : 198 200 USDT. Cohérent avec le récit Marie.

**Étape 2 — Adresses de réception**.

Marie a déposé sur **3 adresses différentes** (la plateforme rotait les adresses) :

- T1 : 7 dépôts cumulés ~45 000 USDT (octobre-novembre).
- T2 : 6 dépôts cumulés ~75 000 USDT (décembre-janvier).
- T3 : 5 dépôts cumulés ~78 000 USDT (janvier-février).

**Étape 3 — Constitution fiches initiales**.

Pour chaque adresse :

- Première transaction : voit Marie comme dépositaire principal mais aussi **autres adresses sources**.
- Solde actuel : 0 (consolidé).
- Pattern de réception : multi-source, montants variables.

**Insight initial** : ces adresses ont **chacune reçu de multiples sources** (~30-50 sources par adresse). Marie n’est pas la seule victime.

### 36.4 Phase 2 — Expansion vers le cluster

**Étape 1 — Identifier l’adresse hub**.

T1, T2, T3 ont consolidé leurs fonds vers une **adresse hub commune** : T-HUB. Cette adresse a reçu cumulativement ~3,2 M USDT (donc bien plus que Marie — l’opération a multiple branches).

**Étape 2 — Caractériser T-HUB**.

T-HUB :

- Active depuis ~6 mois.
- Reçoit de ~12 adresses de collecte (T1-T12 dans la fiche).
- Volume total entrée : ~3,2 M USDT.
- Volume sortie : ~3,1 M USDT (consolidation rapide).
- Pas de label public Tronscan.
- Label Chainalysis Reactor : **« High risk - probable scam »** (label propriétaire basé sur patterns).

**Étape 3 — Identifier les sources des autres adresses de collecte**.

Sur Tronscan, l’analyste liste les sources de T1-T12. Total : ~400 adresses sources distinctes. Probables **400 victimes** différentes de la même opération de pig butchering.

**Étape 4 — Suivi post-T-HUB**.

T-HUB envoie ses fonds vers :

- 30% : exchange non-KYC asiatique (label Chainalysis : « Asian exchange, KYC weak »).
- 25% : 4 adresses « hub-niveau-2 » (probable layering supplémentaire).
- 20% : DEX SunSwap (TRON DEX) pour swap USDT → TRX → puis re-swap.
- 15% : adresses inconnues sans label.
- 10% : Garantex (avant sanctions OFAC), sinon successeur identifié.

**Insight** : opération **structurée** avec consolidation, layering, et points de cashout multiples.

### 36.5 Phase 3 — Investigation off-chain

**Étape 1 — Reverse image search sur photos Daniel**.

Les photos partagées par Daniel sont passées à l’analyse. Résultat : **3 photos sont issues d’un compte Instagram d’un homme réel (entrepreneur singapourien légitime)**. Identité volée. Daniel n’existe pas — c’est un alias utilisant les photos d’un tiers innocent.

**Note importante** : l’identité réelle volée n’est **pas mise en cause**. Le rapport mentionne la victime collatérale (l’entrepreneur singapourien), avec recommandation que Marie / autorités le contactent pour signaler abus de son identité.

**Étape 2 — Recherche OSINT sur la « plateforme »**.

Le nom de la plateforme (« CryptoYield Pro » — fictif) est recherché :

- Site web (capture Wayback Machine) : créé 8 mois avant arnaque, design crédible imitant exchange légitime.
- Domaine : enregistré chez registrar opaque, propriétaire masqué.
- Adresses mentionnées sur le site (« contacts ») : adresse à Singapour qui correspond à un coworking commercial — pas de bureau réel.
- Multiple signalements sur Chainabuse, Reddit r/CryptoScams, autres forums anti-scam.
- Plateforme listée comme **scam** sur multiple sites de recensement.

**Étape 3 — Recoupement avec autres victimes**.

L’analyste contacte le forum r/CryptoScams où des victimes ont signalé la même plateforme. **6 autres victimes identifiées** publiquement avec adresses crypto perdues. Les adresses correspondent à T-HUB ou T1-T12. **Confirmation** que c’est la même opération.

**Étape 4 — Tentative attribution opérateur**.

Patterns observables :

- Adresses fraîches utilisées par cycles (T1-T12 alternées sur 6 mois).
- Consolidation rapide post-réception (souvent dans les 24h).
- Cashout via exchanges asiatiques.

Patterns cohérents avec **compound asiatique** (Cambodge, Myanmar, Laos selon distribution typologique 2024-2026 documentée par TRM Labs et Elliptic). Pas d’attribution individuelle.

### 36.6 Phase 4 — Analyse et synthèse

**Calibration** :

|Élément                                                 |Niveau       |Confiance|
|--------------------------------------------------------|-------------|---------|
|Marie a déposé 198 200 USDT vers T1, T2, T3             |Fait         |Certain  |
|T1, T2, T3 sont liés à l’opération « CryptoYield Pro »  |Très probable|90%      |
|T-HUB est la consolidation centrale de l’opération      |Probable     |80%      |
|Au moins 400 victimes affectées par l’opération         |Probable     |75%      |
|L’opération est gérée depuis un compound Asie du Sud-Est|Possible     |50%      |
|L’identité « Daniel Wang » est usurpée                  |Très probable|90%      |
|Récupération des fonds Marie possible                   |Peu probable |15%      |

**Volume de l’opération** :

- ~3,2 M USDT cumulé sur 6 mois identifiés (probablement plus avant et après).
- Marie représente ~6% du volume total observé.

**Points de cashout identifiés** :

- Exchange asiatique (KYC faible).
- Garantex (sanctionné).
- DEX TRON.
- Adresses inconnues (probables OTC/P2P).

### 36.7 Phase 5 — Rapport et recommandations

**Rapport de 22 pages** structuré (Annexe H) :

- Executive summary.
- Méthodologie.
- Faits Marie (timeline, transactions).
- Cartographie de l’opération (graphes).
- Volume estimé et nombre de victimes.
- Points de cashout et angles d’action.
- Limites et incertitudes.
- Recommandations.

**Recommandations** :

1. **Pour Marie** :
- Transmettre le rapport au procureur en charge de la plainte.
- Signaler l’identité usurpée à l’entrepreneur singapourien (action de courtoisie).
- Documenter ses pertes pour fiscalité (déduction de pertes en investissement frauduleux selon législation).
- Soutien psychologique recommandé.
1. **Pour les autorités** (si transmettent) :
- Coordination internationale via Europol / Interpol.
- Contact avec autorités cambodgiennes / myanmarcaises / laotiennes (limite : coopération variable).
- Demande de gel à exchange asiatique identifié (faible probabilité de succès).
- Surveillance des adresses identifiées (futures activités).
1. **Pour la communauté** :
- Signalement à Chainabuse pour enrichissement base communautaire.
- Partage anonymisé avec ISAC financier.

### 36.8 Restitution

Restitution à Marie : 1 heure. Marie est soulagée d’avoir une compréhension claire et un dossier solide, même si récupération improbable. Marie remercie pour la calibration honnête (pas de fausse promesse de récupération).

Le rapport est transmis par Marie au procureur en charge. Devenir ultérieur : fonction de la procédure judiciaire, hors mission cabinet.

### 36.9 Bilan honnête

✅ **Réussites** :

- Cartographie complète de l’opération.
- Identification de 400+ co-victimes potentielles.
- Volume total documenté.
- Rapport actionnable pour autorités.

⚠️ **Limites** :

- Pas de récupération des fonds Marie (probabilité faible reconnue dès le départ).
- Pas d’identification civile des opérateurs (probable compound asiatique, hors d’atteinte OSINT).
- Cashout via exchange non-KYC = peu d’angles directs.

📊 **Métriques** :

- Durée : 12 jours analyste senior.
- Coût : 22 000 EUR.
- Couverture : 100% des flux Marie tracés. ~75% des flux opération globale identifiés.
- Calibration : tous les éléments avec WEP explicite.

**Apprentissage clé** : pour pig butchering, l’enquête **fonctionne** (cartographie, identification écosystème, alimente justice) mais ne **récupère** pas les fonds dans la grande majorité des cas. Honnêteté du mandat dès le départ = relation client saine.

-----

## Chapitre 37 — Cas 2 : paiement ransomware BTC à un affilié RaaS

**Profil de l’enquête** : enquête sur paiement ransomware par une PME française. Cas similaire à MIXSHADOW dans son schéma général mais d’un autre opérateur, pour montrer la diversité.

### 37.1 Le contexte

**Société** : « TechIndustrie » (nom fictif), PME française de 180 employés, fournisseur de pièces industrielles pour automobile. Compromission ransomware début mars 2026.

**Récit** :

- Vecteur initial : email phishing ciblé sur compte VPN d’un commercial.
- Découverte : 2026-03-04 vers 06:00 UTC. Postes de production chiffrés.
- Note de rançon : groupe « Black Basta » (cluster bien documenté).
- Demande initiale : 60 BTC (~3,5 M EUR au cours).
- Négociation : descend à 22 BTC (~1,3 M EUR).
- Décision direction : payer (impossibilité de reprise rapide via backups, pression production).
- Paiement : 2026-03-10 14:32 UTC.
- Réception clé : 2026-03-10 18:45 UTC. Reprise progressive sur 2 semaines.

**Mandat** : la cyber-assurance de TechIndustrie mandate Athéna Group pour investigation post-paiement. Sarah Marin (déjà engagée sur MIXSHADOW) est trop chargée ; un collègue, **Thomas Lefèvre** (analyste senior Athéna, 4 ans expérience, certifié TRM Labs), prend en charge.

**Objectifs** :

1. Tracer les fonds.
1. Cartographier le blanchiment.
1. Contribuer à la threat intelligence Black Basta.
1. Coopérer avec autorités.

**Budget** : 6 semaines analyste, 65 000 EUR.

### 37.2 Phase 1 — Collecte initiale

**Inputs** :

- TXID du paiement.
- Adresse Black Basta de réception : `bc1q[BB-receive]...` (fictif).
- Note de rançon en pièce jointe (avec adresse mentionnée).
- Logs forensics (Mandiant) du vecteur d’entrée.

**Étape 1 — Vérification on-chain**.

Mempool.space confirme : 22 BTC reçus sur l’adresse `bc1q[BB-receive]` le 2026-03-10 14:32 UTC. Cohérent.

**Étape 2 — Caractérisation initiale**.

Adresse fraîche, jamais vue avant le paiement. Solde 22 BTC. Pas encore de mouvement sortant au moment de l’analyse initiale (J+1 du paiement).

**Étape 3 — Cluster Reactor**.

Reactor : adresse intégrée à un cluster de **180 adresses** déjà labellisé **« Black Basta operational wallet »** par Chainalysis. Confiance high.

**Bonne nouvelle** : Black Basta est un cluster bien suivi. Patterns documentés. Threat intel disponible.

### 37.3 Phase 2 — Suivi post-paiement

**Étape 1 — Premier mouvement (J+1)**.

2026-03-11 09:15 UTC : adresse de réception envoie ses 22 BTC vers une **autre adresse Black Basta** (cluster identifié) : `bc1q[BB-ops1]...`. Transaction simple (1 input, 1 output, plus frais).

Hypothèse : rotation OPSEC standard (déplacer fonds après réception pour limiter exposition).

**Étape 2 — Peeling chain (J+2 à J+7)**.

Sur 5 jours, peeling chain avec ~30 hops. Chaque hop : 0,3-1,5 BTC vers adresse externe + reste vers nouvelle adresse Black Basta.

Total éplutchés : ~14 BTC (sur 22).

Reste dans wallet principal : ~8 BTC en mouvement continu.

**Étape 3 — Analyse des branches**.

Chaque output externe est suivi. Catégorisation :

- **6 branches** vers exchanges non-KYC (4 exchanges différents).
- **8 branches** vers Tornado Cash (~5,5 BTC convertis ETH puis dépôts Tornado).
- **5 branches** vers wallets intermédiaires non-attribués (probable layering supplémentaire).
- **3 branches** vers des hubs USDT-TRON (similaire à MIXSHADOW — services de blanchiment partagés).
- **8 branches** vers adresses non encore caractérisées.

**Insight cross-incident** : **2 des 3 hubs TRON** identifiés sont les **MÊMES** que ceux observés dans MIXSHADOW (Akira). Service de blanchiment partagé entre Black Basta et Akira. Confirme l’insight de Sarah dans MIXSHADOW. Thomas alerte Sarah qui complète sa fiche.

### 37.4 Phase 3 — Caractérisation du cluster Black Basta

**Étape 1 — Examen du cluster Reactor élargi**.

Les 180 adresses du cluster Black Basta (avant le nouveau paiement) montrent :

- ~95 paiements de victimes identifiés sur 8 mois.
- Volumes individuels : 5-150 BTC par paiement.
- Total cumulé reçu : ~1 200 BTC (~70 M EUR équivalent moyen).

**TechIndustrie** est la victime n°96 du cluster (visible).

**Étape 2 — Patterns Black Basta**.

Patterns reconnus :

- Adresses fraîches dédiées par victime.
- Délai paiement → premier mouvement : 12-72h (variable).
- Peeling chain systématique.
- Tornado Cash usage.
- Bridges occasionnels vers BNB Chain.

Patterns cohérents avec opérations Black Basta documentées par Mandiant, CrowdStrike, Sophos en 2024-2025.

**Étape 3 — Threat intel sectoriel**.

Thomas alimente la base CTI Athéna :

- Nouvelles adresses identifiées dans cluster Black Basta.
- Pattern temporel du paiement (cohérent avec autres incidents Black Basta).
- Confirmation usage des hubs TRON partagés (avec Akira).

### 37.5 Phase 4 — Cashouts et coopération

**Étape 1 — Identification des cashouts**.

À 4 semaines :

- **5 dépôts identifiés sur exchanges régulés** : Binance (3), Kraken (1), Bitstamp (1). Total ~2,3 BTC équivalent USDT (~140 000 EUR au cours).
- **3 dépôts identifiés sur exchange non-KYC** spécifique : ~3,5 BTC. Pas d’angle KYC.
- **Tornado Cash** : ~5,5 BTC. Rupture analytique.
- **Hubs TRON** : ~6 BTC convertis. Layering en cours.
- **Non encore caractérisé** : ~5 BTC.

**Étape 2 — Coordination DGSI / Europol**.

Thomas transmet à la DGSI :

- Liste des 5 adresses sur exchanges régulés (KYC potentiel).
- Liste des adresses Black Basta nouvellement identifiées (alimente fichier Black Basta multi-victimes).
- Insight sur hubs partagés Akira / Black Basta.

DGSI valide. Réquisitions envoyées vers Binance, Kraken, Bitstamp.

**Étape 3 — Retours coopération (à 6 semaines)**.

- Binance : 2 comptes identifiés, ~85 000 EUR équivalent gelés. KYC fournis (deux mules différentes).
- Kraken : 1 compte identifié, ~45 000 EUR équivalent gelés. KYC fourni.
- Bitstamp : 1 compte identifié mais fonds déjà retirés avant gel. KYC fourni mais fonds dispersés.
- Total gelés : ~130 000 EUR équivalent.

**Étape 4 — Tentative gel Tether**.

Pour les flux USDT-TRON via hubs, Tether contacté via DGSI. **Réponse Tether** : étude en cours, gel partiel sur 2 adresses identifiées (~30 000 USDT). Plusieurs autres adresses pas gelées (volume opérationnel Tether limité).

### 37.6 Phase 5 — Rapport et restitution

**Rapport de 38 pages** :

- Executive summary.
- Cadrage et méthodologie.
- Faits TechIndustrie (timeline, paiement).
- Cartographie des flux (graphes Reactor + Maltego).
- Caractérisation du cluster Black Basta.
- Insight cross-incident (hubs partagés Akira / Black Basta).
- Cashouts identifiés et résultats coopération.
- Recommandations défensives.
- Limites.

**Restitution** :

- Briefing TechIndustrie + cyber-assurance + DGSI : 90 minutes + Q&A.
- Rapport diffusé en TLP RED initialement, puis TLP AMBER pour partage ISAC sectoriel.

### 37.7 Bilan

✅ **Réussites** :

- Tracking complet sur ~85% des flux.
- Coordination DGSI productive : ~130 000 EUR gelés (sur 1,3 M EUR initial = **~10% récupération nominale**).
- 3 mules identifiées pour enquête judiciaire.
- 30 000 USDT additionnels gelés via Tether.
- Insight cross-incident : confirmation hubs partagés, alimente base CTI.
- Threat intel Black Basta enrichie.

⚠️ **Limites** :

- Tornado Cash : rupture sur ~5,5 BTC.
- Exchange non-KYC : ~3,5 BTC sans angle direct.
- Attribution civile Black Basta : non possible (relevait du FBI / autorités US qui ont opérations en cours).

📊 **Métriques** :

- Durée : 6 semaines.
- Coût : 65 000 EUR.
- Récupération nominale : ~12% (130k EUR + 30k USDT sur 1,3 M EUR).
- ROI cyber-assurance : positif (rapport produit + récupération partielle dépasse coût mission).

**Apprentissage clé** : pour ransomware d’opérateur établi (Black Basta, Akira), la **threat intel cumulative** finit par produire des résultats. L’investissement Athéna sur la base de connaissance interne paie sur le long terme.

-----

## Chapitre 38 — Cas 3 : wallet drain Ethereum par approval phishing

**Profil de l’enquête** : compromission d’un wallet personnel via approval phishing. Mécanisme moderne typique 2023-2026.

### 38.1 Le contexte

**Victime** : Karim (nom fictif), 38 ans, développeur crypto-enthusiaste. Wallet auto-géré (MetaMask), participe activement DeFi et NFT depuis 2021. Patrimoine crypto estimé à ~280 000 USD au moment des faits.

**L’incident** :

- 2026-04-15 vers 22:30 UTC : Karim navigue sur Discord, suit lien partagé dans une community NFT (« nouveau drop exclusif »).
- Site web crédible imitant marketplace NFT légitime. Karim connecte son MetaMask.
- Site demande signature pour « vérifier l’éligibilité ». Karim signe sans relire attentivement.
- 2026-04-15 22:34 UTC : son wallet est vidé. NFT, ETH, tokens — tout part.

**Pertes** :

- ~12 ETH (~36 000 USD).
- Plusieurs NFT (CryptoPunks #XXXX, Bored Ape #YYYY, autres collections) — valeur estimée ~200 000 USD.
- ~30 000 USDC.
- Plusieurs autres tokens DeFi.
- Total ~280 000 USD.

Karim signale immédiatement à plusieurs outils communautaires (chainabuse, OpenSea pour les NFT volés). Il mandate un cabinet privé pour enquête détaillée et soutien à plainte.

**Mandat** : 4 semaines, 20 000 EUR.

### 38.2 Phase 1 — Lecture des transactions de drainage

**Étape 1 — Adresse Karim**.

Karim fournit son adresse Ethereum : `0xKarim...`. L’analyste consulte sur Etherscan.

**Étape 2 — Identification des transactions de drainage**.

Sur la dernière demi-heure du 2026-04-15, ~15 transactions sortantes. Toutes vers une **adresse inconnue** : `0xDrainer1...`.

Examen détaillé d’une transaction type :

- TX hash : `0x...drain001`.
- From : `0xKarim`.
- To : `0xDrainer1`.
- Method : `transferFrom` appelé sur le contrat USDC.
- Logs : `Transfer(from=0xKarim, to=0xDrainer1, value=30000 USDC)`.

C’est un **transfer via approval**. Le drainer a appelé `transferFrom` parce que Karim avait préalablement signé un `approve`.

**Étape 3 — Identification de la transaction d’approve**.

L’analyste cherche dans l’historique de Karim juste avant le drainage. Trouve :

- TX hash : `0x...approve001`.
- From : `0xKarim`.
- To : USDC contract.
- Method : `approve`.
- Spender : `0xDrainer1`.
- Amount : `type(uint256).max` (illimité).
- Timestamp : 22:33 UTC (1 minute avant les drainages).

**Confirmation** : Karim a approuvé un montant illimité au drainer 1 minute avant. Pattern classique d’approval phishing.

### 38.3 Phase 2 — Analyse du drainer

**Étape 1 — Caractérisation `0xDrainer1`**.

`0xDrainer1` est analysé. Smart contract (l’analyste vérifie sur Etherscan onglet « Contract »).

**Code source vérifié** : oui, le drainer a publié son code Solidity. Analyse rapide :

- Fonctions `transferFromAll(token, victim)` qui appellent `transferFrom` avec les approvals existants.
- Fonctions de retrait pour l’opérateur.
- Pas d’audit, pas de réputation.

**Activité** :

- Smart contract déployé il y a 6 mois.
- A été utilisé par ~340 victimes différentes selon analyse Etherscan.
- Volume cumulé : ~14 M USD équivalent (estimations).

**Reconnaissance du drainer service**.

Le code et les patterns du drainer correspondent à un service connu : **« Inferno Drainer »** (drainer-as-a-service identifié par chercheurs comme @scamsniffer en 2023). Il a évolué : variantes successives, multiples déploiements.

L’analyste note : Karim n’est pas victime d’un attaquant individuel, mais d’un **service utilisé par un affilié** d’Inferno Drainer (le service prend une commission, les affiliés font la distribution / le phishing).

### 38.4 Phase 3 — Suivi des fonds

**Étape 1 — Consolidation drainer**.

Sur les 30 minutes post-drainage, `0xDrainer1` consolide vers `0xDrainerOps1` (wallet opérationnel de l’affilié) :

- ETH : 12 ETH → `0xDrainerOps1`.
- USDC : 30 000 → `0xDrainerOps1`.
- Tokens autres : converti via DEX (1inch) en ETH d’abord.
- NFT : transférés à `0xDrainerOps1` en l’état.

**Étape 2 — Suivi des NFT**.

NFT sont **traçables** publiquement (chaque NFT a un ID unique, leur historique est visible).

À J+3, les NFT sont listés sur OpenSea (depuis `0xDrainerOps1`) à des prix bas. Karim et ses contacts dans la communauté ont alerté OpenSea : les **NFT sont gelés** sur OpenSea (delisted, non-transférables sur la marketplace).

Mais : sur d’autres marketplaces moins coopératives, NFT sont vendus. À J+10, ~60% des NFT ont été vendus à des acheteurs tiers (qui les ont peut-être achetés sans savoir qu’ils sont volés).

Récupération des NFT : **complexe juridiquement**. Acheteurs tiers de bonne foi peuvent revendiquer propriété. Procédure longue.

**Étape 3 — Suivi des fonds liquides**.

ETH + USDC : `0xDrainerOps1` consolide :

- Étape A : swap USDC → ETH via Uniswap (J+0).
- Étape B : split en 4 sub-adresses (J+1).
- Étape C : 2 sub-adresses → Tornado Cash (~12 ETH au total).
- Étape D : 2 sub-adresses → bridge Stargate vers BNB Chain.
- Étape E : sur BNB, dispersion vers exchanges non-KYC.

Pattern d’obfuscation classique. ~70% via Tornado Cash, 30% via bridge.

### 38.5 Phase 4 — Identification de l’affilié

**Étape 1 — `0xDrainerOps1` historique**.

`0xDrainerOps1` n’est pas seulement utilisé pour Karim. Analyse révèle :

- Adresse active depuis 4 mois.
- A consolidé fonds de **~80 victimes** différentes.
- Volume cumulé : ~3,2 M USD équivalent.

**Étape 2 — Patterns affilié**.

Patterns observables :

- Quelques fois par semaine, drainages.
- Fonds disparaissent rapidement (Tornado Cash, bridges).
- Adresse de payment de **service Inferno Drainer** : ~10% des fonds reversés à une adresse spécifique du service (commission).
- Pas d’erreur OPSEC visible (pas de réutilisation, pas de mention publique).

**Étape 3 — Possibilité d’attribution**.

Affilié reste **anonyme** au sens civil. Patterns suggèrent acteur expérimenté.

Pas de fonds vers exchange régulé identifié — l’affilié maintient OPSEC stricte.

**Recoupement Inferno Drainer général** : selon @scamsniffer et reports vendor, certains affiliés Inferno Drainer ont été identifiés (Telegram handles, infrastructure leaks). Pour cet affilié spécifique, pas de match identifiable dans les sources publiques au moment de l’enquête.

### 38.6 Phase 5 — Coopération et action

**Étape 1 — OpenSea**.

NFT volés signalés. OpenSea a délisté les NFT compromis. **Action partielle** : les acheteurs tiers ne peuvent plus les revendre sur OpenSea. Mais marketplaces alternatives (Blur, X2Y2 historique) moins coopératives.

**Étape 2 — Coordination autorités**.

Plainte de Karim auprès de la gendarmerie. L’analyste fournit son rapport. Coordination via gendarmerie cyber → Pharos → potentiel relais vers FBI Cyber Division (drainer service est multi-juridictionnel).

**Étape 3 — Communauté**.

Information partagée sur Chainabuse. ScamSniffer alerté avec nouvelles indications sur le drainer / affilié. Alimente la base communautaire.

### 38.7 Phase 6 — Rapport et restitution

**Rapport de 25 pages** :

- Executive summary.
- Méthodologie.
- Faits Karim (timeline précise — minutes).
- Mécanisme du drainer (analyse Solidity).
- Suivi des fonds.
- Identification de l’affilié et du service.
- Limites.
- Recommandations.

**Recommandations à Karim** :

- Action prioritaire : révoquer **tous les approvals existants** sur tous ses wallets via revoke.cash.
- Migration vers nouveau wallet (assumer compromission seed phrase est peu probable mais prudent).
- Hardware wallet pour fonds significatifs.
- Vigilance sur signatures (lire toujours le détail).
- Suivre la procédure judiciaire ; espoir limité de récupération.

**Recommandations communauté** :

- Signaler le service de drainer aux outils anti-phishing.
- Alerter chercheurs (scamsniffer) avec données enrichies.

### 38.8 Bilan

✅ **Réussites** :

- Reconstitution complète du mécanisme.
- Identification du drainer-as-a-service utilisé.
- Identification de l’affilié (en tant que cluster, pas personne).
- ~60% des NFT délistsés OpenSea (limites valorisation).
- Alimentation base communautaire anti-phishing.

⚠️ **Limites** :

- Récupération financière improbable sans coopération internationale exhaustive.
- 70% des fonds liquides perdus dans Tornado Cash.
- Affilié reste anonyme.
- Acheteurs NFT tiers de bonne foi posent problème juridique pour récupération.

📊 **Métriques** :

- Durée : 4 semaines.
- Coût : 20 000 EUR.
- Récupération : indirecte (NFT délistsés sur OpenSea, mais valeur incertaine).

**Apprentissage clé** : pour wallet drain individuel, l’enquête **caractérise** mais récupère rarement. Valeur principale = clarification pour la victime et alimentation communauté.

-----

## Chapitre 39 — Cas 4 : flux multi-chaînes avec bridge et stablecoins

**Profil de l’enquête** : enquête sur une fraude internationale (intermédiaire commercial frauduleux) impliquant flux multi-chaînes complexes. Cas qui montre la complexité de l’enquête moderne.

### 39.1 Le contexte

**Société victime** : « ImportExport SAS » (nom fictif), ETI française d’import-export de matériels électroniques, ~50 employés, CA ~25 M EUR/an.

**L’incident** :

ImportExport est cliente d’un fournisseur asiatique (Vietnam). Pour un contrat de 800 000 USD, négociation avec interlocuteur habituel (M. Tran, directeur achat, ImportExport est en relation depuis 3 ans).

Mi-février 2026, M. Tran annonce changement de procédure de paiement : fournisseur a souffert de problèmes bancaires (sanctions banques vietnamiennes liées à un autre dossier), nouvelle procédure : paiement en **USDT-Tron** vers une adresse fournie. Justification crédible. Email de confirmation reçu sur l’adresse habituelle de M. Tran.

Mi-février 2026 : ImportExport convertit 800 000 USD en USDT (via partenaire crypto OTC français régulé) et transfère vers l’adresse fournie.

Une semaine plus tard, contact direct au téléphone avec M. Tran (pas à Tran officiel mais à son standard) : Tran n’a **jamais demandé de paiement crypto**. Compromission de son email professionnel découverte. ImportExport est **victime de BEC (Business Email Compromise)** sophistiquée — avec demande de paiement détournée vers crypto.

**Mandat** : ImportExport mandate un cabinet pour cartographier les flux et soutenir plainte. Coopération avec autorités françaises ET vietnamiennes (M. Tran réel coopère également pour son côté). 6 semaines, 50 000 EUR.

### 39.2 Phase 1 — Lecture initiale

**Inputs** :

- TXID du transfert USDT-TRON.
- Adresse destinataire : `TR[fraud-receive]...`.
- Email frauduleux et son origine technique.

**Étape 1 — Vérification on-chain**.

Tronscan : 800 000 USDT transférés à 2026-02-18 09:43 UTC vers `TR[fraud-receive]...`.

Adresse fraîche, première activité = ce transfert. Suggère adresse dédiée à cette fraude.

**Étape 2 — Suite immédiate**.

À 2026-02-18 11:15 UTC (90 minutes après réception), `TR[fraud-receive]` envoie l’intégralité (800 000 USDT) vers `TR[fraud-ops1]`.

Délai bref : opérateur supervise le compte ou bot automatique.

### 39.3 Phase 2 — Cascade multi-chaîne

**Étape 1 — Mouvement TR[fraud-ops1]**.

À 2026-02-18 12:30 UTC, `TR[fraud-ops1]` :

- Conserve 200 000 USDT-TRON.
- Convertit 600 000 USDT-TRON via SunSwap DEX en TRX puis re-swap en USDT-Ethereum via service de swap cross-chain (FixedFloat ou équivalent).

Le swap cross-chain est **traçable** mais demande matching manuel : USDT-TRON sortie sur TRON, USDT-Ethereum entrée sur Ethereum quelques minutes plus tard.

**Étape 2 — Sur Ethereum**.

À 2026-02-18 13:45 UTC, 600 000 USDT-Ethereum reçus sur `0x[fraud-eth1]...`.

Quelques minutes plus tard :

- 300 000 USDT-Ethereum → bridge **Stargate** vers BNB Chain.
- 300 000 USDT-Ethereum → swap via Uniswap en ETH (~85 ETH au cours du moment).

**Étape 3 — Sur BNB Chain**.

USDT-BNB reçus. Quelques minutes plus tard, swap en BUSD via PancakeSwap.

BUSD transférés en 5 sub-adresses (60 000 BUSD chaque). Patterns de dispersion.

**Étape 4 — Sur Ethereum (suite swap ETH)**.

85 ETH dans `0x[fraud-eth1]`. Sur les 24h suivantes :

- 50 ETH déposés en 5 dépôts vers Tornado Cash (10 ETH × 5).
- 25 ETH transférés vers `0x[fraud-eth2]`.
- 10 ETH consolidés vers wallet opérationnel.

### 39.4 Phase 3 — Cartographie complète

**À 1 semaine** : l’analyste a reconstitué la cascade :

```
ImportExport (800k USDT-TRON)
    ↓
TR[fraud-receive] (90 min)
    ↓
TR[fraud-ops1]
    ↓ split:
    ├── 200k USDT-TRON (reste sur TRON, dispersion vers hubs)
    └── 600k → cross-chain
              ↓
         0x[fraud-eth1] sur Ethereum
              ↓ split:
              ├── 300k → Stargate → BNB Chain → BUSD → 5 sub-addresses
              └── 300k → Uniswap swap → 85 ETH
                        ↓ split:
                        ├── 50 ETH → Tornado Cash
                        ├── 25 ETH → 0x[fraud-eth2]
                        └── 10 ETH → consolidation
```

**Outils utilisés** : Reactor pour suivi automatique, validation manuelle sur Etherscan / Tronscan / BscScan, Stargate Finance pour matching cross-chain.

**Étape — Caractérisation des destinations finales** (à 4 semaines) :

**Sur TRON** (200k USDT) :

- Layering via 6 hops jusqu’à dépôts vers exchange asiatique non-KYC.
- ~150k USDT cumulés identifiés sur exchange Y.

**Sur BNB Chain** (300k USDT puis BUSD) :

- 5 sub-adresses → consolidation puis dépôts Binance (KYC).
- 5 dépôts Binance identifiés totalisant ~280k BUSD.

**Sur Ethereum** :

- Tornado Cash (~50 ETH = ~150k USD équivalent) : rupture de visibilité.
- `0x[fraud-eth2]` → bridge vers Polygon → swap → consolidation. ~75k USD équivalent suivi jusqu’à dépôts Coinbase Pro.
- Consolidation 10 ETH : reste dormant, pas de mouvement à 4 semaines.

### 39.5 Phase 4 — Coopération et identification

**Étape 1 — Binance (BNB Chain dépôts)**.

DGSI envoie réquisition à Binance pour les 5 dépôts BNB Chain.

Retour Binance (3 semaines plus tard) :

- 5 comptes identifiés, KYC complets.
- 4 mules : individus en Asie du Sud-Est avec patterns de mules (comptes ouverts récemment, multiple flux de dépôts crypto, retraits rapides).
- 1 compte semble-t-il du « cerveau » : individu en Russie (KYC valide), ~80k BUSD récupérés (gel) avant retrait.
- Total gelé Binance : ~80k EUR équivalent.

**Étape 2 — Coinbase Pro (75k USD via Polygon)**.

Réquisition Coinbase. Retour : 1 compte, mule en Roumanie. Fonds déjà retirés. Pas de gel.

**Étape 3 — Exchange non-KYC asiatique**.

Pas de coopération directe. Sanctions évaluées par DGSI mais procédures internationales lentes.

**Étape 4 — Email frauduleux**.

Forensics email coordonnée avec FAI vietnamien : compromission révèle malware infostealer sur poste de M. Tran ayant volé credentials email il y a 3 mois. **Pas un acteur étatique** — fraude opportuniste par groupe BEC.

Patterns techniques cohérents avec **groupe BEC russophone** (même infrastructure / même style de messages que d’autres incidents BEC documentés). Attribution **probable** russophone, mais pas plus précis.

### 39.6 Phase 5 — Bilan

**Total tracé** : ~625k USD sur 800k initial (78%).

**Total gelé / récupéré** : ~80k EUR (Binance, ~10% du total).

**Tornado Cash** : ~150k USD perdus dans rupture analytique.

**Exchange non-KYC asiatique** : ~150k USDT, possible récupération via coopération internationale ultérieure.

**Identification** :

- 4 mules identifiées (utiles pour enquête judiciaire).
- 1 acteur principal en Russie (KYC fourni).
- Profil acteur principal : russophone, BEC professionnel.

### 39.7 Rapport et action

**Rapport de 42 pages** :

- Executive summary.
- Méthodologie.
- Reconstitution timeline complète.
- Cartographie multi-chaînes (graphes Reactor + Maltego).
- Identifications et coopérations.
- Recommandations.
- Limites.

**Recommandations à ImportExport** :

- Sécurisation des emails (MFA, monitoring).
- Procédure de validation pour changements de paiement (téléphone direct + canal indépendant).
- Formation des équipes finance.
- Cyber-insurance évaluation.

**Recommandations autorités** :

- Soutenir procédure judiciaire avec pièces fournies.
- Coopération DGSI / Vietnam / Russie selon accords bilatéraux.
- Sanctions OFAC évaluation pour exchange non-KYC asiatique.

### 39.8 Bilan honnête

✅ **Réussites** :

- Cartographie multi-chaînes complète (BTC → ETH → BNB → Polygon).
- Identification de 5 KYC (4 mules + 1 acteur principal).
- 80k EUR gelés.
- Profil acteur établi.

⚠️ **Limites** :

- 22% des flux non tracés (Tornado Cash, exchange non-KYC).
- Récupération limitée à ~10%.
- Acteur principal en Russie : peu coopération attendue.

**Apprentissage clé** : pour fraude multi-chaîne sophistiquée, l’enquête est **fastidieuse mais payante**. Les outils pro permettent le tracking cross-chain. La coopération exchanges régulés finit par produire des KYC. Le bilan financier est modeste mais le bilan **renseignement** est solide.

-----

## Chapitre 40 — Cas 5 : enquête Monero — quand la blockchain ne suffit pas

**Profil de l’enquête** : enquête honnête sur un cas où Monero rompt la traçabilité on-chain. Cas pédagogique pour montrer comment **gérer la rupture** et déplacer l’enquête vers les angles off-chain.

### 40.1 Le contexte

**Société victime** : « SantéTech » (nom fictif), startup française BioTech (~80 employés), produit logiciel de gestion hospitalière. Compromise en mars 2026 par un opérateur ransomware **Helldown** (variante émergente de la galaxie Akira / Babuk).

**L’incident** :

- Compromission via vulnérabilité VPN Fortinet non patchée.
- Chiffrement le 2026-03-22.
- Helldown demande **35 XMR** (~6 000 USD au cours, mais valeur de levier psychologique liée à la criticité).

**Décision** : SantéTech décide de payer (impossibilité de reprise rapide, données sensibles en jeu — patients).

**Mais** : Helldown exige **Monero** (XMR). Pas de Bitcoin accepté.

**Conséquences** :

- SantéTech doit acquérir 35 XMR.
- L’acquisition se fait via partenaire crypto OTC français : conversion EUR → XMR via service partenaire (LocalMonero était option mais fermé en 2024 ; alternatives autres).
- Paiement effectué le 2026-03-25.
- Réception clé déchiffrement.

**Mandat** : SantéTech mandate Athéna pour « tenter de tracer ces 35 XMR autant que possible et identifier des angles d’action ». Sarah Marin (qui a déjà MIXSHADOW en cours) est consultée pour le cadrage. **Constat dès le départ** : Monero = traçabilité on-chain quasi-nulle. Sarah déconseille un mandat « tracking complet » mais propose un mandat différent — caractérisation Helldown + analyses des points off-chain.

**Mandat révisé** : 3 semaines, 25 000 EUR, focus sur :

1. Documenter ce qui peut l’être on-chain (rare).
1. Caractériser le profil Helldown.
1. Identifier les points off-chain potentiellement exploitables.
1. Coordonner avec autorités sur l’écosystème Helldown plus large.

### 40.2 Phase 1 — Documenter la transaction Monero

**Étape 1 — TXID Monero**.

SantéTech fournit le TXID Monero de la transaction de paiement.

Sur explorateurs Monero (xmrchain.net, etc.) :

- TXID confirmée.
- Date / heure.
- **Mais** : pas de visibilité sur expéditeur (ring signatures), pas de visibilité sur destinataire (stealth address), pas de visibilité sur montant exact (RingCT) — sauf information transmise hors-chain par les parties.

SantéTech a la « view key » de sa propre transaction (donnée par leur wallet) qui permet de **vérifier qu’ils ont bien envoyé X XMR**. Mais pas de visibilité sur ce qui se passe ensuite.

**Étape 2 — Limite explicite**.

L’analyste documente : « La transaction de 35 XMR est confirmée par les view keys de SantéTech. Au-delà de la réception par Helldown, la traçabilité on-chain Monero n’est pas possible. »

### 40.3 Phase 2 — Tracer les XMR avant le paiement

**Insight** : si on ne peut pas tracer les XMR **après** le paiement, on peut tenter de tracer **comment** SantéTech a obtenu les 35 XMR.

**Pourquoi utile ?**

- Les XMR ont été **achetés** via un service OTC français.
- Le service OTC a obtenu ces XMR de quelque part.
- Si on remonte la chaîne d’origine, on pourrait identifier des patterns.

Mais pour ce cas spécifique : les XMR achetés par SantéTech proviennent d’un service OTC légitime — origine sans intérêt pour l’enquête Helldown (qui a reçu les XMR, pas envoyé).

### 40.4 Phase 3 — Pivot vers caractérisation Helldown

**Étape 1 — Recherche threat intel publique**.

Helldown est un opérateur récent (apparition fin 2024 / début 2025). Caractérisation par vendor reports :

- TRM Labs publication 2025 mentionne Helldown comme variante de la « galaxie Akira ».
- Mandiant / CrowdStrike : Helldown analysé. Codebase partagé avec Babuk leak 2021. Probable acteur(s) ayant adapté.
- Patterns de victimes : santé, manufacturing, ETI.
- Demandes de paiement : Bitcoin et **Monero** (préférence Monero affichée).
- Leak site Helldown actif sur Tor.

**Étape 2 — Recherche du leak site Helldown**.

Sur Tor, le leak site Helldown affiche ~25 victimes publiées (sur 8 mois d’activité). SantéTech n’y figure pas (paiement effectué, donc pas publication).

Captures du leak site (méthode Dark Web cours associé) :

- Liste des victimes.
- Statistiques de paiement (revendiquées).
- Communications avec victims (portail de négociation séparé).

**Étape 3 — Patterns Helldown**.

Caractérisation :

- Volume modéré (vs LockBit historique ou Black Basta).
- Cible de niche (souvent santé / éducation).
- Demandes monétaires modérées (3-50k USD typique).
- Préférence Monero **forte**.
- Communications professionnelles via portail Tor.

**Étape 4 — Hypothèse profil opérateur**.

Patterns suggèrent :

- Opérateur moins sophistiqué que LockBit / Black Basta.
- Possible affilié individuel ou petit groupe.
- Préférence Monero suggère **conscience forensique** — l’opérateur sait que Bitcoin se trace, choisit Monero pour rupture analytique.

Pas d’attribution civile possible.

### 40.5 Phase 4 — Angles off-chain

**Angle 1 — Communications Helldown / SantéTech**.

Le portail Tor de Helldown a été utilisé pour négociation (passage de demande initiale à l’accord 35 XMR). Le portail est **observable** (URL .onion documentée).

Communications archivées par SantéTech (captures du portail) :

- Style : anglais correct, idiomatique. Pas de patterns linguistiques évidents.
- Délais de réponse : 4-24h, suggère opérateur seul ou petite équipe.
- Concession sur prix : flexibilité. Suggère acteur opportuniste (préfère paiement modéré à pas de paiement).

Pas de leak OPSEC évident dans les communications.

**Angle 2 — Vecteur d’attaque**.

Forensics SantéTech (par Mandiant) : compromission via Fortinet vulnerability. Patterns techniques :

- Outils utilisés : Cobalt Strike, Mimikatz, AnyDesk (LotL), Rclone pour exfiltration.
- C2 infrastructure : 2 IP utilisées (l’une saisie depuis par autorités sur autre dossier).

**Insight** : croisement avec autre dossier (saisie C2 IP). Possible coordination DGSI sur dossier multi-victimes Helldown si autres victimes françaises identifiées.

**Angle 3 — Service OTC Monero**.

Question hypothétique : Helldown va probablement convertir les XMR en autre actif (USDT, BTC) à un moment via service OTC ou exchange. Si l’opérateur utilise un service identifiable pour cette conversion, angle de coopération.

L’analyste n’a pas accès aux flux post-paiement (Monero opaque), mais documente les **services Monero** populaires (LocalMonero historique, autres) et propose à DGSI de **monitorer ces services pour transactions cohérentes** avec timing post-paiement Helldown — analyse statistique probabiliste.

**Angle 4 — Profil Helldown plus large**.

Recoupements multi-source :

- Vendor reports (Mandiant, TRM, Elliptic).
- Communications victimologie (autres victimes Helldown identifiées via leak site).
- Discussions communauté CTI (FIRST, ISACs).

**Étape 5 — Coordination avec autres victimes**.

L’analyste note que **2 autres victimes Helldown** sont identifiées dans la communauté CTI française (sans nom, par discrétion). DGSI peut potentiellement consolider une vue **multi-victimes Helldown** pour orienter enquête plus large.

Athéna soumet à DGSI une **demande de coordination** : si plusieurs victimes Helldown coopèrent ensemble, des signaux convergents peuvent émerger qui dépassent ce qu’une enquête isolée peut voir.

### 40.6 Phase 5 — Rapport et limites

**Rapport de 18 pages** (volontairement plus court — moins à dire qu’avec Bitcoin) :

- Executive summary.
- Cadrage et limitations Monero (section dédiée explicite).
- Documentation transaction de paiement (limitée).
- Caractérisation Helldown (section principale du rapport).
- Angles off-chain explorés.
- Recommandations.
- Limites assumées.

**Section limites prend une place importante** :

> « En raison de l’usage de Monero pour le paiement, la traçabilité on-chain est intrinsèquement limitée. Le rapport documente ce qui peut l’être (transaction de paiement par view key SantéTech, profil Helldown via threat intel publique, angles off-chain identifiés) et expose honnêtement ce qui ne peut pas l’être (chemin des fonds post-paiement, identification des comptes Helldown sur exchanges, attribution civile). Cette enquête contribue à la threat intel sectorielle et à la coordination autorités, mais ne produit pas de récupération financière ni d’attribution personnelle. »

**Recommandations à SantéTech** :

- Rapport transmis à plainte (procédure judiciaire enregistrée).
- Considérer cyber-insurance pour incidents futurs.
- Mesures défensives durcies (patch management Fortinet, MFA, segmentation, EDR avancé).
- Plan IR pour incidents futurs.

**Recommandations DGSI** :

- Coordination multi-victimes Helldown (Athéna identifie 2 autres victimes potentielles via communauté CTI).
- Surveillance des services Monero pour patterns cohérents.
- Coordination internationale (Helldown a victimes US, UE, Asie).

### 40.7 Bilan

✅ **Réussites** :

- Caractérisation profil Helldown.
- Identification du contexte plus large (multi-victimes Helldown documentées).
- Mandat **réaliste** dès le départ — pas de fausse promesse de tracking.
- Coordination DGSI productive sur dossier multi-victimes.
- Threat intel sectorielle enrichie.

⚠️ **Limites assumées dès le mandat** :

- Pas de tracking on-chain au-delà de la transaction de paiement.
- Pas d’identification civile.
- Pas de récupération.

📊 **Métriques** :

- Durée : 3 semaines (volume modeste vs cas Bitcoin).
- Coût : 22 000 EUR (sur 25 000 budgétés).
- Couverture : limitée par nature Monero. Mais 100% de ce qui était possible.

### 40.8 Apprentissage clé

**Pour Monero, l’enquête est différente** :

1. **Mandat doit être réaliste**. Cf cadrage révisé. Le client doit comprendre **dès le départ** que tracker Monero on-chain n’est pas possible.
1. **L’enquête se déplace off-chain**. Profil acteur, vecteurs, infrastructure, communications, services off-chain — tout sauf on-chain pure.
1. **Valeur = renseignement et coordination**. Pas récupération.
1. **Calibration honnête essentielle**. Le rapport ne « tente pas » de faire passer pour acquis ce qui ne l’est pas.
1. **Coordination multi-source amplifie**. Une victime isolée a peu d’angles ; multi-victimes consolidées peuvent révéler des patterns convergents.

**Pour l’analyste OSINT** : refuser un mandat « tracker mes XMR » est parfois la décision **professionnellement correcte**. Proposer un mandat alternatif réaliste préserve la crédibilité et apporte de la valeur.

### 40.9 Synthèse Partie VII

Cinq cas, cinq typologies, cinq logiques d’enquête :

1. **Pig butchering USDT-TRON** : cartographie d’écosystème, identification de co-victimes, peu de récupération.
1. **Ransomware BTC** : tracking systématique, threat intel cumulative, récupération partielle via exchanges régulés.
1. **Wallet drain Ethereum** : reconstitution mécanisme, identification du service drainer, récupération limitée.
1. **Multi-chaînes BEC** : tracking cross-chain complexe, coopération internationale, récupération modeste.
1. **Monero ransomware** : reconnaissance des limites, pivot off-chain, valeur en renseignement.

**Patterns transverses** :

- **Récupération nominale** souvent **5-15%** dans les meilleurs cas, **0%** dans certains.
- **Identification civile** rare en OSINT pur.
- **Threat intel et coordination** sont la valeur principale.
- **Calibration honnête** maintient la crédibilité.

La Partie VIII va aborder des **cas historiques réels emblématiques** où des enquêtes complètes ont permis des saisies majeures. Ces cas montrent ce qui est possible **avec ressources, coopération internationale, et persévérance** sur des années.

-----
