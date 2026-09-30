---
title: PARTIE VIII — CAS HISTORIQUES EMBLÉMATIQUES
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
chapter: 9
chapters: 10
---

> **Ce que cette partie apprend.** Quatre cas historiques majeurs où l’enquête crypto a abouti à des résultats marquants : la saisie Bitfinex (3,6 Mrd USD), la récupération Colonial Pipeline, le hack Ronin par Lazarus, et la saga Tornado Cash. Pour chaque cas : faits, méthodes employées, résultats, leçons. Synthèse finale du fil rouge MIXSHADOW.
> 
> **Ce qu’elle ne couvre pas.** Cas pratiques didactiques (Partie VII), production de rapport (Partie IX).
> 
> **Ce que vous saurez faire après cette partie.** Mobiliser ces cas comme références pour benchmark, formation, et communication. Comprendre ce qui est possible avec ressources, coopération internationale et temps long.

> **Note importante** : ces cas sont basés sur des informations publiquement disponibles (DOJ press releases, indictments unsealed, rapports vendor publics). Les chiffres et faits sont sourcés à la date de rédaction (2026). Pour utilisation professionnelle, vérifier les évolutions ultérieures (procédures en cours, appels, jurisprudence).

-----

## Chapitre 41 — Bitfinex 2016 → saisie 3,6 Mrd USD 2022

Le hack Bitfinex de 2016 et la saisie de 2022 constituent le **plus gros cas de récupération crypto** documenté à ce jour. Six ans entre le vol et la saisie. Démonstration que la traçabilité on-chain, combinée à la persévérance et la coopération, peut aboutir.

### 41.1 Le hack — août 2016

**Faits** :

- 2 août 2016 : Bitfinex (exchange majeur, basé à Hong Kong) annonce avoir été piraté.
- **119 756 BTC** volés (~72 M USD au cours de l’époque, ~7,2 Mrd USD au cours record post).
- Vecteur précis : compromis multi-signature wallet via failles d’implémentation BitGo (debate technique sur la responsabilité, jamais entièrement clarifié publiquement).
- Bitfinex socialise les pertes : haircut de 36% sur tous les comptes utilisateurs, émission de tokens BFX comme dette.

**Adresses** :

- 119 756 BTC sont **disséminés** entre 2 000+ adresses fraîches dans les heures suivant le hack.
- Ces adresses restent ensuite **largement dormantes** pendant des années.

**Suivi** :

- Communauté Bitcoin et chercheurs (notamment **Sergej Kotliar**, Alec Ziupsnys, et plus tard Chainalysis, Elliptic) **monitor les wallets**.
- Quelques mouvements occasionnels (petites sommes) entre 2016 et 2022, surveillés.
- Bitfinex offre des récompenses pour informations.

### 41.2 La saisie — février 2022

**Annonce DOJ — 8 février 2022** :

- **Heather « Razzlekhan » Morgan** et **Ilya « Dutch » Lichtenstein**, couple à Manhattan, arrêtés.
- Chargés de **conspiracy to commit money laundering** et **conspiracy to defraud the United States**.
- DOJ saisit **94 636 BTC** (sur les 119 756 originaux), valorisés à **3,6 Mrd USD** au cours de l’époque.

**Méthode d’investigation reconstituée** (depuis l’indictment unsealed et investigations journalistiques) :

**Étape 1 — Long monitoring**. Les adresses du hack sont surveillées par autorités et chercheurs depuis 2016. Quelques mouvements occasionnels alimentent le dossier.

**Étape 2 — Patterns émergent**. À partir de 2020-2021, des **mouvements plus actifs** émergent. Lichtenstein utilise progressivement les fonds via :

- AlphaBay (darknet market, saisi en 2017 — son historique permet aux autorités d’extraire des liens).
- Multiple exchanges (avec KYC pour certains).
- Mixers (Bitcoin Fog notamment).

**Étape 3 — KYC sur exchanges**. Lichtenstein dépose une **partie** des fonds sur exchanges utilisant **identités réelles** (lui ou Morgan, ou liens identifiables). Erreur OPSEC critique.

**Étape 4 — Décrypter l’infrastructure**. Le DOJ exécute un mandat de perquisition sur le **cloud storage** de Lichtenstein (Cloud account). Le cloud contenait un fichier chiffré avec **les clés privées des wallets contenant ~94 636 BTC**.

Le fichier était sécurisé par mot de passe. Le DOJ accède au mot de passe (modalités précises peu détaillées publiquement — possible exploitation cloud, possible recovery via partner, possible cryptanalyse). Décryption permet **prise de contrôle** des wallets et saisie effective.

**Étape 5 — Saisie**. 94 636 BTC transférés depuis les wallets compromis vers wallet contrôlé par US gouvernement.

**Étape 6 — Inculpation**. Indictment publié, charges expliquées, fonds publiquement annoncés.

### 41.3 Le procès — 2023-2024

**Lichtenstein** : plaide coupable en août 2023 pour conspiracy to commit money laundering et fraud against the United States.

**Morgan** : plaide coupable au même moment pour conspiracy.

**Sentencing** :

- **Lichtenstein** : condamné en novembre 2024 à 5 ans de prison.
- **Morgan** : condamnée en novembre 2024 à 18 mois de prison.

**Restitution** : les BTC saisis vont en partie à la restitution des victimes (utilisateurs Bitfinex de 2016 ayant subi le haircut). Procédure complexe étant donné l’évolution de la valeur (BTC valait ~600 USD en 2016, ~40-70k en 2024).

### 41.4 Méthodes mobilisées

**Tracking on-chain de longue durée** :

- Surveillance des adresses pendant 6 ans.
- Identification des mouvements progressifs.
- Outils : Chainalysis Reactor, monitoring custom, communauté.

**Saisies antérieures comme inputs** :

- AlphaBay saisi en 2017 a fourni données utilisées pour le dossier Bitfinex.
- Bitcoin Fog saisi 2021, idem.

**KYC exchange** :

- Erreurs OPSEC de Lichtenstein/Morgan exposant identité.

**Cloud forensics** :

- Mandat de perquisition sur le cloud account.
- Décryption des fichiers stockés.

**Coopération internationale** :

- DOJ + FBI + IRS + autres agences US.
- Coopération avec exchanges concernés.

**Persévérance institutionnelle** :

- 6 ans de monitoring patient.

### 41.5 Leçons

**Pour les criminels (perspective des autorités)** :

- **Long terme = vulnérabilité**. Les adresses « tranquilles » pendant des années deviennent **incentive croissant** à mauvaise OPSEC quand l’opérateur tente de monétiser.
- **Erreurs OPSEC se cumulent**. Une seule erreur sur 6 ans suffit (KYC exchange, cloud non-sécurisé, etc.).
- **Cryptographie protège les fonds, pas les humains**. Lichtenstein avait techniquement les clés privées — mais ses **comptes utilisateur** étaient compromis par perquisition.

**Pour les enquêteurs** :

- **Patience institutionnelle** : LEA peuvent maintenir surveillance pendant des années.
- **Recoupement multi-source** : crypto + cloud + exchange KYC + saisies antérieures.
- **Volume justifie l’investissement** : 3,6 Mrd USD justifie ressources LEA significatives.

**Pour les analystes** :

- **Documentation longitudinale** des wallets criminels alimente les cas futurs.
- **Le « cold storage » pendant des années** ne signifie pas « impossible à saisir ».

**Pour les victimes** :

- **Récupération possible mais lente**. Bitfinex est exemple. Beaucoup d’incidents ne aboutissent pas comme cela.

### 41.6 Bitfinex aujourd’hui

À 2026 :

- Procédure de restitution toujours en cours pour utilisateurs originaux.
- Bitfinex a survécu à l’incident, reste exchange actif (et Tether y est lié).
- Cas étudié dans formations forensiques (Chainalysis utilise comme étude de cas).

-----

## Chapitre 42 — Colonial Pipeline 2021 — récupération FBI

Le cas **Colonial Pipeline** est emblématique pour deux raisons : impact géopolitique majeur (perturbation infrastructure US critique), et **récupération significative** des fonds par le FBI dans des délais courts.

### 42.1 Les faits

**Colonial Pipeline** : opérateur de pipelines de carburant US, fournit ~45% du fuel de la côte Est des États-Unis.

**Mai 2021** :

- 7 mai 2021 : Colonial Pipeline découvre compromission par ransomware.
- Vecteur : compte VPN avec mot de passe fuité (sans MFA).
- Auteur : groupe **DarkSide** (RaaS d’origine russophone).
- Décision : Colonial paie **75 BTC** (~4,4 M USD au cours du moment).
- Paiement effectué le 8 mai 2021.
- Décryption key reçue, mais **lente** — Colonial restaure depuis backups en parallèle.

**Impact** :

- Pipeline arrêté plusieurs jours.
- Pénuries de carburant côte Est.
- Réaction politique : Joe Biden émet executive order sur cybersécurité (12 mai 2021).
- Pression sur DarkSide qui annonce sa dissolution officielle (probable rebranding).

### 42.2 La récupération — juin 2021

**Annonce DOJ — 7 juin 2021** :

- **63,7 BTC saisis** (sur 75 payés).
- Valeur au moment de la saisie : ~2,3 M USD (Bitcoin avait baissé entre mai et juin).
- FBI a obtenu accès à la clé privée du wallet contenant ces fonds.

**Méthode** (selon DOJ press release et analyse publique) :

**Étape 1 — Tracking immédiat post-paiement**. FBI suit les BTC payés via Chainalysis dès la transaction.

**Étape 2 — Identification d’un wallet de réception**. Les fonds atterrissent finalement (via plusieurs hops) sur une adresse spécifique contrôlée par un membre de DarkSide.

**Étape 3 — Obtention de la clé privée**. C’est l’élément le plus opaque publiquement. DOJ indique avoir **obtenu la clé privée**. Modalités jamais entièrement explicitées :

- Hypothèse 1 : cloud storage compromis (similaire à Bitfinex).
- Hypothèse 2 : opération sur infrastructure DarkSide (qui était pressurée par autorités à ce moment).
- Hypothèse 3 : informations d’un insider DarkSide (members défectant).
- Hypothèse 4 : exploitation de vulnérabilités dans wallet ou infrastructure.

**Étape 4 — Saisie**. FBI signe transaction avec la clé obtenue, transférant 63,7 BTC vers wallet US gouvernement.

**Étape 5 — Annonce**. DOJ rend public ~30 jours après le paiement initial.

### 42.3 Pourquoi 63,7 sur 75 ?

Différence de 11,3 BTC (~15%). Explications probables :

- Commission affilié : DarkSide opérait en RaaS (affilié garde ~70-80%, opérateur 20-30%). 11,3 BTC pourrait correspondre à la part affilié déjà extraite vers son propre wallet (qu’autorités n’ont pas pu saisir).
- Frais opérationnels (gas, mixing).
- Conversion partielle déjà effectuée.

### 42.4 Méthodes mobilisées

**Tracking on-chain rapide** :

- Réaction en jours (vs Bitfinex en années).
- Outils : Chainalysis utilisé activement.

**Coopération sectorielle** :

- Colonial coopère pleinement avec FBI dès le départ.
- Information sur transaction de paiement immédiate.

**Coordination LEA** :

- FBI Cyber Division.
- Intelligence agencies multiples.

**Pression sur DarkSide** :

- L’attention politique post-Colonial déstabilise le groupe.
- Possible facilitation du tracking par opportunités opérationnelles.

### 42.5 Leçons

**Pour les victimes** :

- **Coopérer immédiatement** avec FBI / autorités améliore probabilité de récupération partielle.
- Pas garanti, mais sans coopération = aucune chance.

**Pour les enquêteurs** :

- **Réaction rapide** = avantage. Les premiers jours / semaines sont critiques.
- **Pression médiatique / politique** peut faciliter coopération internationale.

**Pour les criminels (perspective des autorités)** :

- **Cibler infrastructure critique** = attention politique disproportionnée. DarkSide a été un moment, jamais retrouvé sa stature.

### 42.6 Suite — DarkSide → BlackMatter → ALPHV

**DarkSide** se dissout officiellement après Colonial Pipeline. Mais **rebranding probable** :

- **BlackMatter** apparaît juillet 2021. Patterns techniques similaires à DarkSide. Saisi novembre 2021.
- **ALPHV / BlackCat** apparaît novembre 2021. Patterns continuant lignée. Démantelé 2024.

Cycle classique du RaaS : démantèlement → rebranding → re-démantèlement. L’écosystème est résilient mais pressurized.

-----

## Chapitre 43 — Ronin / Lazarus 2022 — 625 M USD

Le hack du **Ronin Network** est le plus gros vol crypto à ce jour. Attribué à **Lazarus** (DPRK) par FBI et Chainalysis. Cas emblématique de l’intersection entre vulnérabilité technique et acteur étatique sophistiqué.

### 43.1 Le hack — mars 2022

**Ronin Network** : sidechain Ethereum développée par Sky Mavis pour le jeu Axie Infinity. Bridge Ronin permet transferts entre Ronin et Ethereum.

**Architecture du bridge** : 9 validators, 5 signatures requises pour autoriser un retrait. 4 contrôlés par Sky Mavis directement, 1 par Axie DAO (qui avait délégué ses signatures à Sky Mavis temporairement).

**Vecteur d’attaque** :

- Compromission de **5 des 9 clés validator** par phishing (« Operation Dream Job », fake job offer LinkedIn).
- Une fois 5 clés compromis (4 Sky Mavis + 1 Axie DAO délégué), attaquant atteint le seuil de signatures.

**L’attaque — 23 mars 2022** :

- Signature de transactions de retrait massives.
- **173 600 ETH** (~600 M USD) + **25,5 M USDC** (~25 M USD) drainés.
- **Total : ~625 M USD** au cours du moment.

**Découverte** : 6 jours après (29 mars 2022) — délai signaling failures de monitoring.

### 43.2 L’attribution

**14 avril 2022** : OFAC sanctionne adresses Lazarus liées au hack.

**Attribution** :

- FBI confirme attribution Lazarus / DPRK.
- Chainalysis confirme dans ses rapports.
- Patterns d’attaque cohérents avec opérations Lazarus (vecteur LinkedIn, techniques utilisées, infrastructure).

**Pourquoi attribution forte** :

- Patterns infra (C2 servers liés à autres opérations Lazarus).
- Vecteurs sociaux (Operation Dream Job documenté pour multiple opérations Lazarus).
- Behavioral post-hack (utilisation Tornado Cash, bridges, patterns de blanchiment cohérents).

### 43.3 Le blanchiment

**Méthode Lazarus post-hack** :

**Étape 1 — Conversion**. ETH et USDC convertis. USDC partiellement gelé par Circle (Circle a gelé ~250k USDC sur réquisition).

**Étape 2 — Tornado Cash**. Massive utilisation. ~25-30k ETH déposés à Tornado Cash dans les semaines post-hack. Volume tel que ils représentaient une fraction substantielle des dépôts Tornado.

**Étape 3 — Bridges**. Une partie passe via bridges vers Bitcoin (Ren BTC ou autre).

**Étape 4 — Mixing Bitcoin**. Sur Bitcoin, CoinJoin (Wasabi, Samourai), peeling chains.

**Étape 5 — Off-ramp**. Exchanges régionaux (Asie), OTC desks, P2P. Beaucoup en juridictions peu coopératives.

### 43.4 Récupération

**Récupération partielle documentée** :

- **Circle gel** : ~250k USDC.
- **Saisies multiples** : autorités US et Sky Mavis ont récupéré plusieurs millions USD via différents incidents.
- Total récupéré : **estimé ~30-40 M USD** sur 625 (5-6%).

**Sky Mavis** : a remboursé les utilisateurs via levée de fonds (350 M USD, dirigée par Binance), pas par récupération hack.

### 43.5 Méthodes mobilisées

**Attribution rapide** :

- OFAC dans les semaines suivant.
- Chainalysis / TRM / FBI publications.

**Sanctions** :

- Adresses Lazarus sanctionnées.
- Tornado Cash sanctionné en partie pour cette opération (août 2022).

**Coopération exchanges** :

- Multiple exchanges gelent des fonds Lazarus identifiés.
- Difficulté : Lazarus utilise exchanges non-coopératifs.

**Pression politique** :

- US, Corée du Sud, Japon, UE coordonnent sanctions DPRK élargies post-Ronin.

### 43.6 Leçons

**Pour acteurs DeFi / bridges** :

- **Sécurité validators** = critique. 5/9 c’était insuffisant. Multi-sig schemes doivent assumer compromise.
- **Monitoring real-time** des bridges essentiel.
- **Audit de gouvernance** : la délégation de signatures Axie DAO à Sky Mavis (de fait centralisation) était une faille.

**Pour enquêteurs** :

- **Attribution étatique** rapide possible avec ressources adéquates.
- **Récupération massive impossible** quand acteur étatique : Lazarus utilise tout l’arsenal d’obfuscation, opère depuis juridiction non-coopérative.
- **Sanctions et pressions** sont les outils principaux.

**Pour CTI / OSINT** :

- **Documentation des wallets Lazarus** alimentation continue.
- **Tracking long terme** parfois fournit des opportunités (saisies opportunistes des années plus tard).

### 43.7 Suite

Lazarus continue à opérer. Hacks majeurs subséquents attribués (Atomic Wallet, CoinEx, Stake.com, autres). **Plusieurs milliards USD/an** estimés volés par Lazarus selon Chainalysis. L’écosystème reste vulnérable à des acteurs ressourcés.

-----

## Chapitre 44 — Tornado Cash — sanctions OFAC et procès

**Tornado Cash** est le cas emblématique de **conflit entre code open source et responsabilité légale**. Sanctions OFAC, démantèlement partiel, procès des développeurs — débat juridique en cours.

### 44.1 Le contexte

**Tornado Cash** : mixer décentralisé sur Ethereum, lancé août 2019 par Roman Semenov, Roman Storm, Alexey Pertsev. Cf Ch.31.

**Adoption** :

- 2019-2022 : usage massif. Multi-milliards USD passés à travers les pools.
- Légitime : utilisateurs privacy-conscious, payments anonymes, donations sensibles.
- Illicite : Lazarus, ransomware, hackers DeFi.

### 44.2 Les sanctions OFAC — août 2022

**8 août 2022** : OFAC sanctionne Tornado Cash.

**Justifications** :

- Plus de **7 Mrd USD** estimés blanchis via Tornado depuis 2019.
- Usage massif par Lazarus (incluant Ronin, Ch.43).
- Usage par autres acteurs ransomware et fraude.

**Sanctions** :

- Adresses smart contracts Tornado Cash placées sur SDN list.
- Toute interaction par US persons interdite.
- Étendu à GitHub : Microsoft désactive le repo Tornado et comptes développeurs (controverse, partiellement réversé après).

**Réactions** :

- Communauté privacy : réaction forte. Paradigme de **« les développeurs ne sont pas responsables des usages »**.
- Civil liberties orgs (EFF, Coin Center) attaquent en justice.
- Multi-application : Coinbase finance partiellement le procès Coin Center vs OFAC.

**Coin Center vs OFAC** :

- Argument : OFAC outrepasse son mandat en sanctionnant un smart contract immutable (vs une personne / entité).
- Procès en cours 2023-2024-2025.
- Premiers verdicts : partiellement favorables aux plaintifs (un juge a noté que les smart contracts immutables ne peuvent pas être « personnes » sanctionnables au sens classique).
- Évolution complexe, à suivre.

### 44.3 Inculpation et procès Pertsev

**Alexey Pertsev** : développeur de Tornado Cash, Russe, résidant Pays-Bas.

**Arrestation — août 2022** : arrêté Pays-Bas suite à enquête FIOD (autorité financière néerlandaise).

**Charges** : blanchiment d’argent (faciliter le blanchiment via le service développé).

**Procès — 2023-2024** :

- Argumentation accusation : Pertsev a sciemment continué à développer un service utilisé massivement pour blanchiment, malgré conscience.
- Argumentation défense : Tornado est code open source, immutable, Pertsev ne contrôlait pas les usages.

**Verdict — 14 mai 2024** : Pertsev **condamné** par tribunal néerlandais à **5 ans et 4 mois de prison** pour blanchiment d’argent.

**Implications** :

- Premier verdict significatif sur responsabilité de développeur de mixer.
- Précédent juridique majeur EU.
- Appel en cours.

### 44.4 Inculpation Storm aux US

**Roman Storm** : co-développeur Tornado, US-resident.

**Inculpation — août 2023** : DOJ inculpe Storm pour conspiracy to commit money laundering, conspiracy to operate unlicensed money transmitter, conspiracy to violate sanctions.

**Arrestation** : Storm arrêté août 2023.

**Procès US — 2024-2025** :

- Procès initialement programmé septembre 2024.
- Reporté à plusieurs reprises.
- Procès tenu finalement 2025 selon évolution.
- **Verdict** : à confirmer selon évolution. Au moment de rédaction (2026), procédures en cours / partiellement résolues.

**Roman Semenov** : autre développeur, sanctionné OFAC août 2023, en fuite (juridiction non révélée publiquement).

### 44.5 Évolutions post-sanctions

**Tornado Cash continue de fonctionner** : code immutable. Smart contracts sur Ethereum, accessibles techniquement. Volume très réduit post-sanctions (~95% drop) mais non-nul.

**Acteurs contournant** :

- Lazarus continue à utiliser Tornado malgré sanctions.
- Autres acteurs criminels conscients du risque.

**Migrations** :

- Vers d’autres mixers (Sinbad sanctionné après).
- Vers privacy coins (Monero).
- Vers techniques mixtes (CoinJoin Bitcoin + bridges).

**Sanctions Sinbad — novembre 2023** : OFAC sanctionne Sinbad.io, mixer ayant pris une partie du volume post-Tornado. Cycle continue.

### 44.6 Leçons

**Pour l’industrie crypto** :

- **Développeurs peuvent être tenus responsables** dans certaines juridictions.
- **Code immutable n’est pas immunité légale**.
- Distinction floue entre « outils neutres » et « facilitations volontaires ».

**Pour les utilisateurs** :

- **Risque de sanctions** d’utiliser un service dont l’opérateur sera sanctionné rétroactivement.
- **Compliance** devient préoccupation majeure.

**Pour les enquêteurs** :

- **Tornado Cash post-sanctions** : moins de volume, mais acteurs criminels qui continuent sont **identifiables comme criminels** (interaction avec sanctions = signal fort).
- **Multiplications de mixers** rend tracking plus complexe mais aussi chaque service plus exposé.

### 44.7 Pour l’analyste

Le cas Tornado Cash illustre l’**évolution réglementaire rapide** de l’écosystème crypto. L’analyste suit :

- Listes OFAC SDN (mises à jour régulières).
- Sanctions UE / autres juridictions.
- Procédures judiciaires marquantes.
- Évolutions du débat « code as speech » vs régulation.

Ces cadres déterminent **ce qui est légitimement enquêtable**, **ce qui peut faire l’objet d’action** (gel, saisie), et **ce qui expose l’utilisateur final** (interaction avec sanctioned).

-----

## Chapitre 45 — Synthèse MIXSHADOW

Bilan complet du fil rouge déployé tout au long du cours.

### 45.1 Récapitulatif factuel

**Victime** : Aurélien Médical, équipementier français de matériel hospitalier (700 collaborateurs, OIV santé, Lyon).

**Incident** : ransomware Akira, mars 2026. Vecteur : compromission VPN admin via stealer log. 3 hôpitaux clients impactés (patients en attente, dont cas vitaux).

**Paiement** : 35 BTC (~2 M EUR) le 14 mars 2026. Clé déchiffrement reçue. Reprise progressive sur 3 semaines.

**Mandat** : Aurélien Médical + DGSI mandatent Athéna Group. Sarah Marin, analyste senior. 8 semaines, 80 k EUR.

**Objectifs** : tracer, cartographier, identifier off-ramps, contribuer à attribution, coopérer avec autorités.

### 45.2 Méthodes appliquées

**Outils** :

- Chainalysis Reactor (principal).
- TRM Labs (validation croisée).
- Mempool.space, Etherscan, Tronscan, BscScan (publics).
- Maltego, Excalidraw (visualisation).
- Hunchly (capture).
- OpenTimestamps (anchoring preuves).

**Méthodes** :

- Cadrage initial structuré (Ch.24).
- Fiches d’adresses pour 250+ adresses (Ch.12).
- Suivi peeling chain (Ch.7).
- Tracking cross-chain (Ch.33).
- Analyse Tornado Cash statistique (Ch.31).
- Caractérisation hubs TRON (Ch.10).
- Calibration WEP systématique (Ch.18).
- Chain of custody rigoureuse (Ch.23).

**Coordination** :

- Briefings DGSI bi-hebdomadaires.
- Coordination Tether pour gel USDT-TRON.
- Coordination FBI / Europol via DGSI.
- Réquisitions via DGSI vers Binance, Kraken, Coinbase.

### 45.3 Résultats

**Cartographie** :

- **250 adresses identifiées** au total (Bitcoin, Ethereum, TRON, Solana mineur).
- **4 chaînes principales** couvertes.
- **~75% des flux** Akira post-paiement Aurélien Médical tracés.

**Caractérisation Akira** :

- Patterns de blanchiment documentés (peeling Bitcoin → swap FixedFloat → Tornado Cash sur ETH → conversion USDT-TRON via exchange non-KYC → dispersion TRON via hubs).
- Pattern temporel suggérant fuseau horaire UTC+9 / Asie de l’Est (possible, non-conclusif).
- Choix Bitcoin (vs Monero) suggérant compromis traçabilité / facilité opérationnelle.
- **Insight transversal** : 2 hubs TRON identifiés comme **services de blanchiment partagés** entre Akira et Black Basta (insight cross-incident, alimente dossier multi-victimes).

**Coopération** :

- **3 mules identifiées** sur Binance / Kraken.
- **~45 000 USDT gelés** sur exchanges régulés.
- **~30 000 USDT gelés** via Tether (sur 6 adresses TRON).
- **6 adresses Akira principales** transmises pour évaluation sanctions OFAC.
- **2 adresses « possibles retraits Tornado »** alimentent suivi complémentaire.

**Threat Intel** :

- Fiche acteur Akira enrichie (base Athéna).
- Pattern blanchiment Akira documenté pour réutilisation.
- Insight hubs partagés pour coordination CTI plus large.

### 45.4 Bilan financier

**Récupération nominale** :

- 45 000 USDT (Binance/Kraken) + 30 000 USDT (Tether) = **75 000 USDT gelés**.
- ~ **3,75 % du paiement initial** (75k / 2 M EUR).

**Bilan en valeur de renseignement** :

- 3 mules identifiées (utiles pour enquête judiciaire ultérieure).
- 2 hubs blanchiment identifiés (alimentent base Chainalysis / TRM).
- Pattern Akira documenté (réutilisable pour autres victimes).
- Coopération multi-juridictionnelle activée.

**Bilan en valeur stratégique** :

- Aurélien Médical bénéficie d’un dossier complet pour procédure judiciaire et déclaration assurance.
- DGSI bénéficie d’un dossier alimentant ses suivis Akira / RaaS.
- Athéna renforce sa base CTI et sa crédibilité opérationnelle.

### 45.5 Limites assumées

**Pas de récupération massive**. Le bilan financier est **modeste**. C’est la réalité de l’enquête ransomware, sauf cas exceptionnels (Bitfinex, Colonial).

**Pas d’attribution civile**. Akira reste un cluster sans identités civiles attribuées par OSINT seul. Relevait des autorités via voies classifiées.

**Tornado Cash** : rupture analytique sur ~12 ETH (~36 000 USD à l’époque). Hypothèses calibrées, pas certitudes.

**Exchange non-KYC X** : ~150 000 USDT sans angle KYC direct.

**Solana** : couverture moindre des outils, sous-flux peu caractérisés.

### 45.6 Apprentissages

**Pour Sarah** :

- L’enquête « modeste en récupération » peut être **substantielle en valeur de renseignement**.
- La calibration honnête préserve la crédibilité et permet la coopération.
- Le travail de cartographie complète prend des semaines mais paie sur le long terme.

**Pour Athéna** :

- Combiner outils pro (Chainalysis + TRM) augmente la couverture et la confiance.
- La coordination DGSI active les leviers que l’OSINT pure ne peut activer.
- Les insights cross-incident (hubs partagés) construisent une vue stratégique.

**Pour Aurélien Médical** :

- Le paiement en pression vitale, choix difficile, contextualisé.
- L’enquête post-paiement maximize la valeur extraite des fonds payés.
- Renforcement des défenses pour incidents futurs.

**Pour l’écosystème** :

- L’industrie ransomware est résiliente mais pressurée.
- La coopération internationale finit par produire des résultats.
- Chaque enquête contribue à la capacité collective.

### 45.7 Devenir post-MIXSHADOW

**Aurélien Médical** :

- Reprise complète de l’activité.
- Investissement majeur dans cybersécurité (EDR, MFA universel, segmentation, surveillance 24/7).
- Plan IR durci.
- Communication transparente avec clients hospitaliers.

**Sarah Marin** :

- Continue chez Athéna, monte en seniorité.
- MIXSHADOW comme étude de cas en formations internes.
- Contribue à publication CTI sectorielle (TLP AMBER) sur Akira.

**DGSI** :

- Dossier Akira enrichi.
- Coordination Europol / FBI continue.
- Démantèlement éventuel d’Akira : à plus long terme, comme tous les groupes RaaS — cycle continue.

**Akira (groupe)** :

- Continue à opérer en 2026.
- Pression croissante des autorités.
- Possible rebranding ultérieur.
- Patterns documentés alimentent la défense collective.

### 45.8 Le message final de MIXSHADOW

> **L’enquête crypto-forensique professionnelle ne promet pas miracles. Elle produit du renseignement actionnable, contribue à la justice, et alimente la défense sectorielle. Sa valeur tient à sa rigueur méthodologique, sa calibration honnête, et son intégration dans des écosystèmes coopératifs.**

C’est ce que le cours OSINT Crypto a tenté de transmettre, à travers méthodes, outils, cas, et fil rouge.

La Partie IX va aborder la **production professionnelle** : rapport, calibration formelle, coopération, éthique, et programme durable.

-----
