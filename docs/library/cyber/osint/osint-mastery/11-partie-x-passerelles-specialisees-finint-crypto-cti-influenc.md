---
title: 'PARTIE X — Passerelles spécialisées : FININT, Crypto, CTI, Influence'
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
chapter: 11
chapters: 15
---

> **Ce que cette partie apprend.** Vue maître sur les domaines spécialisés qui ont leur cours dédié dans la bibliothèque : FININT (financier), Crypto, CTI (Cyber Threat Intelligence), Influence et désinformation, et Renseignement économique / Due diligence. Pour chaque domaine, panorama des outils, méthodes et renvois explicites vers le cours spécialisé.
>
> **Ce qu'elle ne couvre pas.** La profondeur opérationnelle de chaque domaine, traitée dans les cours dédiés.
>
> **Ce que vous saurez faire après cette partie.** Conduire un triage initial dans chaque domaine, identifier quand basculer vers un cours spécialisé, articuler une enquête multi-domaines.

-----

### Chapitre 70 — OSINT financier et patrimonial

#### 70.1 Vue maître

L'**OSINT financier** consiste à investiguer le patrimoine, les flux et la santé financière d'une personne ou entité à partir de sources ouvertes. C'est un pan majeur de l'OSINT moderne, mobilisé pour due diligence, investigation de fraude, asset recovery, journalisme économique.

Le présent chapitre fournit la **vue maître**. Pour la profondeur (UBO complexes, schémas de blanchiment, AML/CFT, asset recovery international, expertise comptable forensique), **renvoi systématique vers FININT Investigation Financière vFULL**.

#### 70.2 Patrimoine visible : sources publiques

**Patrimoine immobilier.**
- **Cadastre.gouv.fr** (France) : visualisation parcelles, références.
- **Pages Jaunes / annuaires** : adresses identifiables.
- **SCI** : dirigeants et bénéficiaires partiellement accessibles.
- **Registres fonciers internationaux** (Land Registry UK, etc.).

**Patrimoine corporate.**
- Sociétés détenues (Pappers, OpenCorporates).
- Parts dans filiales (Ch.36-37).

**Patrimoine mobilier visible.**
- Véhicules de luxe (presse spécialisée, photos publiques).
- Yachts (MarineTraffic, Ch.52).
- Jets privés (ADS-B Exchange, Ch.52).
- Œuvres d'art (catalogues de ventes, ArtPrice).

#### 70.3 Indicateurs de revenus déclarés

**Sources directes (limitées en OSINT).**
- Comptes annuels publiés (sociétés cotées : EDGAR, AMF).
- Rémunérations dirigeants (proxy statements US, RemCo UK).
- Déclarations PEP (HATVP en France pour élus).

**Indicateurs indirects.**
- Train de vie apparent vs estimation revenus.
- Patrimoine visible vs revenus déclarés.
- Cohérence des trajectoires (un DAF d'ETI ne possède pas un yacht 50m sans explication).

#### 70.4 Détection d'incohérences

**Méthode.** Comparer patrimoine et train de vie visibles avec revenus plausibles.

**Indicateurs d'alerte.**
- Patrimoine très supérieur à revenus accumulés théoriques.
- Acquisitions massives sur court délai.
- Train de vie incompatible avec revenus déclarés.
- Structures écrans massives.

**Pour MIRAGE.** Le patrimoine Delaunay identifié (mas Provence 1.8 M€, villa Marrakech 800 k€, deux appartements parisiens, SCI) cumule ~3-4 M€. Revenus DAF TechnoVert ~180-250 k€/an sur 7 ans → accumulation difficile, surtout après imposition et charges familiales. **Cohérence faible** entre patrimoine visible et revenus déclarés → indicateur d'alerte.

#### 70.5 ICIJ leaks et FININT

Les **leaks ICIJ** (Panama, Paradise, Pandora, Cyprus Confidential) sont la source publique de référence pour FININT international. Voir Ch.37.

#### 70.6 Outils OSINT financier vue maître

**Gratuit.**
- Pappers, OpenCorporates.
- OpenSanctions.
- ICIJ Offshore Leaks Database.
- OCCRP Aleph.
- HATVP (PEP France).

**Payant accessible.**
- Pappers Pro.
- DueDil (UK).
- Sayari.

**Institutionnel.**
- Orbis (Bureau van Dijk).
- WorldCheck.
- Refinitiv (LSEG).
- Dow Jones Risk.

#### 70.7 Renvoi FININT vFULL

Pour la profondeur opérationnelle :
- UBO complexes (nominees imbriqués, fondations, fiducies).
- Schémas de blanchiment (intégration, empilement, placement).
- AML/CFT (méthodologie, indicateurs).
- Asset recovery (méthodologie internationale).
- Comptabilité forensique.
- Analyse de transactions visibles (mention dans leaks, comptes consolidés).

**→ Cours FININT Investigation Financière vFULL.**

#### 70.8 Workflow triage OSINT financier

Pour un triage rapide (ce qui est dans le périmètre du master OSINT) :

1. **Identification entité** (corporate, personne).
2. **Patrimoine corporate visible** (Pappers, OpenCorporates).
3. **Patrimoine immobilier** (cadastre, registres fonciers).
4. **ICIJ leaks** (recherche Offshore Leaks Database).
5. **Sanctions et PEP** (OpenSanctions).
6. **Indicateurs d'incohérence** (revenus vs patrimoine).
7. **Synthèse triage**.
8. **Décision escalade** : si éléments suffisants pour approfondissement, **basculer vers FININT vFULL** ou partenaire spécialisé.

#### 70.9 Signaux d'alerte financiers typiques

L'analyste OSINT doit savoir reconnaître, dans les sources publiques, les **signaux d'alerte financiers** justifiant approfondissement FININT.

**Signaux corporate.**
- Capital social symbolique pour société à activité significative déclarée.
- Adresse de domiciliation partagée avec centaines d'autres entités (registered agent).
- Director ou UBO unique apparent sans cohérence avec activité.
- Activité déclarée vague (« consulting », « services », « trading ») sans précision.
- Forte croissance ou décroissance inexpliquée du capital.
- Changements fréquents de dirigeants ou commissaires aux comptes.
- Domiciliation dans juridiction à risque (paradis fiscal classé).
- Comptes annuels non publiés malgré obligation.
- Conventions réglementées avec parties liées non détaillées.

**Signaux flux.**
- Ligne comptable inhabituelle ou disproportionnée (« services consulting externes », « commissions », « honoraires »).
- Forte croissance de cette ligne sur courte période.
- Bénéficiaire des flux non identifiable publiquement.
- Pattern cyclique suspect (versements répétitifs réguliers).
- Cohérence temporelle avec création d'entités opaques.

**Signaux patrimoniaux.**
- Acquisitions massives sur courte période.
- Patrimoine très supérieur aux revenus cumulés (avec marge fiscale et charges).
- Multiplication d'entités SCI avec immobilier diversifié géographiquement.
- Présence d'actifs visibles (yacht, jet, œuvres d'art, voitures de luxe) non justifiés.
- Donations familiales suspectes sur courte période.

**Signaux comportementaux.**
- Discrétion publique anormale.
- Empreinte SOCMINT volontairement faible.
- Changements de domiciliation fiscale en série.
- Investissements crypto significatifs sans expertise sectorielle documentée.

**Indicateurs FATF 2026.** Le **GAFI/FATF** maintient une liste évolutive d'indicateurs de risque blanchiment. Catégories : **A** (opacité corporate), **B** (transactions inhabituelles), **C** (crypto et nouvelles technologies), **D** (comportements suspects), **E** (juridictions à risque).

#### 70.10 Investigation patrimoniale méthodologique

**Inventaire des sources patrimoniales (France).**

| Type de patrimoine | Source OSINT |
|---|---|
| Immobilier identifié | Cadastre.gouv.fr (visualisation, pas propriétaire direct) |
| SCI propriétaires | Pappers (dirigeants + UBO de la SCI révèlent) |
| Sociétés détenues | Pappers + OpenCorporates |
| Comptes-titres / OPCVM | AMF déclarations seuils + presse |
| Œuvres d'art | Catalogues ventes (Christie's, Sotheby's archives publiques) |
| Yachts | MarineTraffic + Equasis (propriété déclarée pavillon) |
| Jets privés | ADS-B Exchange + registres FAA/DGAC |
| Voitures de luxe | Très limité OSINT (photos publiques, presse) |
| Crypto-actifs | Pivots Etherscan, Walletexplorer (limité, voir crypto cours) |
| Actifs déclarés HATVP (PEP) | declaration.hatvp.fr |

**Méthodologie estimation cohérence revenus / patrimoine.**

1. **Estimation revenus accumulés.** Standards sectoriels par poste et secteur (baromètres APEC, cabinet RH). Pour un DAF d'ETI : 180-250 k€ brut. Pour 7 ans : 1.3-1.8 M€ brut.
2. **Soustraction fiscale.** Tranche marginale ~45 % au-delà de 175 k€. Estimation 35-40 % moyenne. Revenu net : ~0.8-1.2 M€.
3. **Soustraction charges courantes.** Train de vie cohérent avec poste (60-70 k€/an pour cadre supérieur). Sur 7 ans : 420-490 k€.
4. **Reste disponible épargne.** ~400-700 k€ sur 7 ans pour un DAF français standard.
5. **Comparaison patrimoine visible.** Si > 1 M€, incohérence à investiguer.

**Hypothèses alternatives à tester systématiquement.**
- Héritage familial substantiel (vérifiable presse, généalogie publique).
- Mariage avec personne fortunée (LinkedIn conjoint, presse).
- Gains crypto exceptionnels (rare mais possible).
- Activité parallèle déclarée (auteur, formateur, etc.).
- Stock-options exercées (si société cotée — déclarations AMF).

#### 70.11 Investigation du dispositif offshore

Le **dispositif offshore typique** détourne via trois mécanismes principaux observables en OSINT.

**Mécanisme 1 — Double fausse facturation.** Société française paye sa propre filiale offshore pour « services de conseil » non rendus. La filiale offshore reçoit les fonds, déductibles fiscalement. L'UBO bénéficie via dividendes ou structures suivantes.

*Indicateurs OSINT.* Ligne comptable « services consulting » disproportionnée. Filiale offshore avec activité non démontrable. Cohérence temporelle entre création offshore et augmentation de la ligne.

**Mécanisme 2 — Structures empilées.** Société française → société intermédiaire (UE : Malte, Luxembourg) → société finale (BVI, Cayman). L'empilement masque l'UBO final.

*Indicateurs OSINT.* Plusieurs sociétés liées par dirigeants partagés ou registered agent commun. Nominees identifiables. Documents leaks (ICIJ) révélant les couches.

**Mécanisme 3 — Trusts et fondations.** Trust dans juridiction de droit anglo-saxon ou fondation familiale. L'UBO formel disparaît au profit du trust / fondation.

*Indicateurs OSINT.* Mention de trust dans documents. Settlor / trustee / beneficiary identifiables. Leaks ICIJ Pandora notamment riches en trusts.

#### 70.12 Outils OSINT financier 2026 spécialisés

**Gratuit avancé.** OpenSanctions (sanctions, PEP, adverse media), OCCRP Aleph (documents leakés), ICIJ Offshore Leaks Database, Pappers freemium France, Companies House UK gratuit complet, OpenCorporates freemium cross-juridictions.

**Freemium ou bas coût.** DueDil (UK), Sayari (OSINT corporate moderne), Pappers Pro abonnement France.

**Institutionnel haut coût.** Bureau van Dijk Orbis (Moody's, 400M+ sociétés mondial), WorldCheck (Refinitiv/LSEG, screening institutionnel), Dow Jones Risk & Compliance, Refinitiv Eikon (marché financier intégré), Bloomberg Terminal (référence).

#### 70.13 Limites OSINT financier

**Ce que l'OSINT financier seul ne fait pas.**
- Accès aux comptes bancaires individuels.
- Identification des bénéficiaires économiques cachés derrière fiducies opaques.
- Reconstruction de flux entre comptes sans réquisitions.
- Qualification fiscale ou comptable des opérations.
- Évaluation forensique des écritures.

**Pour ces dimensions.** Réquisitions judiciaires (PNF, juge d'instruction), TRACFIN (signalement de soupçons), expertise comptable judiciaire, coopération internationale (entraide pénale, FATF, Egmont Group).

L'analyste OSINT identifie les **faisceaux d'indices** justifiant ces démarches. Il ne s'y substitue pas.

> **MIRAGE — Épisode 13 : Signaux financiers ouverts**
>
> Le triage OSINT financier sur Delaunay identifie :
> - Patrimoine immobilier visible : ~3-4 M€ (SCI La Provence Familiale + villa Marrakech + 2 appartements parisiens SCI nominee).
> - Patrimoine corporate offshore : Delta Consulting (Malte) + Verde Holdings (Chypre).
> - Revenus DAF TechnoVert : ~180-250 k€/an, cumul 7 ans = 1.3-1.8 M€ brut.
> - Incohérence : patrimoine total supérieur à revenus accumulés bruts, alors qu'il faut soustraire imposition + charges + train de vie.
> - Indicateurs ICIJ Cyprus Confidential : confirmation flux TechnoVert → Delta → Verde (B2).
> - Aucune sanction / PEP active sur les entités identifiées.
>
> **Synthèse triage.** Faisceau d'indices cohérents avec hypothèse H1 (détournement vers structures offshore). **Recommandation : escalade vers FININT vFULL** pour profondeur (schéma de blanchiment précis, asset recovery potentiel, analyse comptable forensique des comptes consolidés TechnoVert pour identification écritures suspectes).
>
> Cette enquête MIRAGE produit un rapport OSINT avec ce niveau de triage. Le PNF saisi pourra mandater expertise comptable judiciaire pour profondeur.

-----

### Chapitre 71 — Sanctions, PEP, KYC/KYB et adverse media

#### 71.1 Vue d'ensemble

Le **screening** sanctions / PEP / adverse media est l'une des composantes les plus systématiques de l'OSINT corporate moderne. Volume massif (banques screent des millions de clients), discipline mature, outils nombreux.

#### 71.2 Sanctions : régimes

Voir Ch.7 et Ch.38. Régimes principaux :
- **OFAC** (US Treasury) : SDN List. Extraterritorialité forte.
- **UE** : liste consolidée par la Commission.
- **UK OFSI** post-Brexit.
- **ONU** : sanctions obligatoires globalement.
- **Sanctions sectorielles** (Iran, Russie, Corée du Nord, etc.).

#### 71.3 PEP : politiquement exposées

**Définition.** Personnes occupant ou ayant occupé des fonctions publiques importantes (PEP étrangères, PEP nationales, PEP organisations internationales) + famille et associés proches.

**Obligation AMLD UE.** Vigilance renforcée pour toute relation avec PEP.

#### 71.4 KYC / KYB : Know Your Customer / Business

**KYC** : vérification d'identité et de risque sur clients (banque, fintech, courtier).

**KYB** : équivalent sur partenaires commerciaux et fournisseurs.

**CSDDD** UE 2024 (Ch.7) impose vigilance supply chain.

#### 71.5 Adverse media

Recherche presse négative sur entité / personne. Voir Ch.38.

#### 71.6 Outils intégrés

**OpenSanctions.** Gratuit, agrège sanctions + PEP + adverse media. Standard 2026 pour budget limité.

**WorldCheck (Refinitiv / LSEG).** Standard institutionnel.

**Dow Jones Risk & Compliance.** Équivalent.

**ComplyAdvantage, Sayari, Sigma.** Alternatives modernes.

#### 71.7 Méthodologie screening

1. Identification entité.
2. Screening sanctions OFAC / UE / UK / ONU.
3. Screening PEP (entité + dirigeants + UBO).
4. Adverse media multi-langues.
5. Match analysis (faux positifs filtrés).
6. Validation humaine.
7. Documentation pour audit.

#### 71.8 Gestion des faux positifs

Les screening produisent souvent des faux positifs (homonymes). **Validation humaine** indispensable.

**Méthode.**
- Cross-vérification (date de naissance, juridiction, profession).
- Investigation de l'homonyme.
- Décision finale documentée.

#### 71.9 Évolution réglementaire 2024-2026

- **CSDDD** : nouvel impératif supply chain.
- **Failure to Prevent Fraud UK** (sept 2025) : new offence.
- **MiCA** : régulation crypto VASPs.
- **Refonte AMLD** : 6e AMLD UE.

Conformité dynamique.

#### 71.10 Renvois

Pour profondeur : cours FININT et cours Compliance / Due Diligence dédié.

-----

### Chapitre 72 — Crypto-actifs et blockchain : panorama OSINT

#### 72.1 Vue maître crypto

L'**OSINT crypto** est devenu un pan structurant entre 2017 et 2026, avec l'explosion des actifs numériques, leur usage dans la fraude, le ransomware, le contournement de sanctions.

Le présent chapitre fournit la **vue maître**. Pour la profondeur (clustering, attribution, mixers, bridges, cashout, IA on-chain, NFTs forensique, DeFi), **renvoi systématique vers OSINT Crypto vFULL**.

#### 72.2 Lecture basique d'une transaction

**Bitcoin transaction.**
- TXID : identifiant unique.
- Inputs : adresses émettrices.
- Outputs : adresses destinataires.
- Montant.
- Frais.
- Block timestamp.

**Ethereum / EVM transaction.**
- Hash de transaction.
- From / To.
- Value.
- Gas, fees.
- Contract interaction (DeFi).

**TRON, autres.** Logiques similaires.

#### 72.3 Explorateurs publics

**Bitcoin.**
- **Blockstream.info** : standard.
- **Mempool.space** : moderne.
- **Blockchain.com** : populaire.

**Ethereum.**
- **Etherscan.io** : référence.
- **Phalcon, Tenderly** : alternatives techniques.

**TRON.**
- **Tronscan.org**.

**Multi-chain.**
- **DeBank** : portfolio multi-chain.
- **Zerion**.

#### 72.4 Clustering : vue maître

Le **clustering** consiste à regrouper plusieurs adresses appartenant probablement au même propriétaire.

**Heuristiques classiques.**
- Co-spending : adresses utilisées comme inputs dans même transaction.
- Change address heuristic.
- Patterns de transactions.

**Outils commerciaux clustering.** Chainalysis, TRM Labs, Elliptic, Crystal Blockchain.

**Outils gratuits.** Limités.

**Pour vue maître :** identifier qu'une adresse semble liée à un exchange / mixer / acteur connu (via base de connaissances publique).

#### 72.5 Attribution prudente

**Adresse ≠ personne.**

Une adresse n'est jamais directement liée à une personne physique en source ouverte pure. L'attribution suppose :
- Lien plateforme (KYC d'exchange).
- Lien public (adresse publiée par personne).
- Lien forensique (saisie, perquisition).

**Pour OSINT.**
- Identification de clusters d'adresses.
- Identification de relations avec entités connues (exchanges, mixers).
- **Attribution à une personne reste prudente** sans lien direct.

#### 72.6 Sanctions et crypto

**OFAC** sanctionne des adresses crypto spécifiques (Tornado Cash 2022, ChipMixer 2023, etc.).

**Outils.**
- **OFAC SDN crypto addresses list**.
- **Chainalysis Sanctions Screening**.
- **TRM Labs**.

**Travel Rule** (FATF) : impose aux VASPs d'échanger info émetteur/destinataire au-dessus de seuils.

#### 72.7 Wallets et exchanges labellisés

**Bases de données labellisation publiques (partielles).**
- **OXT.me** : Bitcoin clustering ouvert.
- **Bitquery, Dune** : data on-chain analytique.
- **Walletexplorer.com** : labellisation Bitcoin partielle.

**Exchanges identifiables.** Adresses Binance, Coinbase, Kraken, etc., souvent identifiées dans bases publiques.

#### 72.8 NFTs et tokenisation

**NFTs** : Non-Fungible Tokens. Investigation possible via OpenSea, Etherscan.

**Cas d'usage OSINT.** Lavage d'argent via NFTs, identification de marchés illicites.

#### 72.9 DeFi : nouveau terrain

**Decentralized Finance.** Protocoles ouverts (Uniswap, Aave, Compound, etc.).

**OSINT.** Smart contracts publics, transactions tracables, mais complexité technique.

**→ Cours OSINT Crypto vFULL.**

#### 72.10 Pivots crypto ↔ OSINT classique

**Pivots possibles.**
- Adresse → ENS (Ethereum Name Service) → username public.
- Adresse → fuite (DeHashed avec wallet) → email lié.
- Adresse → mention publique sur réseaux sociaux → identité.
- Adresse → infrastructure (domain WHOIS d'un projet crypto associé).

#### 72.11 Renvoi systématique

Toute investigation crypto au-delà du triage doit être conduite avec la profondeur du **cours OSINT Crypto vFULL**.

#### 72.12 Typologie criminelle crypto observable en OSINT

**Catégories majeures (compréhension, pas exploitation).**

**Ransomware et extorsion.** Les rançonneurs (LockBit, BlackCat / ALPHV, Royal, Play, etc.) demandent paiement en Bitcoin ou Monero. Patterns observables : adresses publiées par groupes ransomware sur leur leak site, suivi flux sur Bitcoin (Monero non-traçable par design).

**Marchés darkweb.** Drogues (anciennement Silk Road, Hydra, AlphaBay, et successeurs en émergence-fermeture). Bitcoin et Monero principaux. Cashout via mixers et P2P.

**Fraude au président via crypto.** CEO fraud avec demande conversion paiement en USDT TRC-20 (rapide, peu de frais). Cibles : DAF d'ETI. Pattern : urgence + nouveauté + non-vérification.

**Investment scams (« rug pulls »).** Faux projets DeFi / NFT / memcoins lancés pour collecter ETH/USDT puis disparaître. Volume astronomique 2021-2026.

**Pig butchering.** Arnaque sentimentale longue (semaines/mois) qui mène à investissement crypto fictif. Réseau organisé majoritairement Sud-Est asiatique (Cambodge, Birmanie, Laos).

**Money laundering / mules crypto.** Conversion stealer logs / cartes volées en crypto, puis cashout via P2P, exchanges low-KYC, ou bridges.

**Sanctions evasion.** Russie, Iran, Corée du Nord utilisent crypto pour contourner sanctions occidentales. North Korea (Lazarus Group) particulièrement actif sur DeFi, hacks d'exchanges, ransomware.

**Terrorist financing.** Volume limité mais existant. FATF documente cas.

#### 72.13 Mixers, bridges et techniques d'obfuscation

**Mixers (mélangeurs).** Services qui mélangent crypto de plusieurs utilisateurs pour casser le lien on-chain.

- **Tornado Cash** : ETH, sanctionné OFAC août 2022. Toujours utilisé après sanction (smart contracts publics).
- **ChipMixer** : sanctionné 2023.
- **Sinbad** (BTC) : sanctionné 2023, successeur de Blender.io.
- **Wasabi Wallet / Samourai Wallet** : wallets BTC avec CoinJoin.
- **Monero** : par design, anonymat natif.

**Bridges (passerelles cross-chain).** Permettent conversion entre blockchains. Utilisés pour obfuscation.

- **Wormhole, Ronin, Multichain, Across, Stargate, Synapse** : bridges majeurs.
- **Hacks de bridges** : massive perte crypto 2022-2023 (Ronin 600 M$, Wormhole 320 M$, etc.).

**P2P et OTC.** Conversion fiat-crypto sans KYC ou avec KYC faible. LocalBitcoins (fermé 2023), Bisq, plateformes émergentes. Marchés Telegram massifs.

**Privacy coins.** Monero (XMR), Zcash, Dash. Anonymat plus fort que Bitcoin.

**Pour OSINT.** Identifier dans les flux observables passage par mixer / bridge / privacy coin → signal fort de tentative d'obfuscation.

#### 72.14 Méthodologie triage OSINT crypto

**Triage en 6 étapes (vue maître, profondeur en cours crypto).**

1. **Pivots vers crypto.** Identifier dans l'enquête classique (Sherlock, breaches, presse) toute mention crypto (adresses, exchanges, projets).
2. **Validation des adresses.** Format correct (Bitcoin commence par 1, 3, bc1 ; Ethereum 0x...). Lookup sur explorateur (Etherscan, Blockstream).
3. **Labellisation.** Recherche labels publics (Walletexplorer.com pour BTC, Etherscan « public tags »).
4. **Volumes et flux.** Quelle activité, vers quels acteurs labellisés ? Exchanges connus ? Mixers connus ?
5. **Sanctions.** Cross-check OFAC SDN crypto addresses list, Chainalysis Sanctions Screening.
6. **Décision escalade.** Si volume / pattern suspects → cours OSINT Crypto vFULL ou cabinet spécialisé (Chainalysis, TRM Labs, Elliptic).

#### 72.15 Cas typique de cashout

**Pattern fraudeur typique.**

1. Détournement fonds vers crypto via exchange KYC modéré (Binance, Kraken).
2. Transfert vers wallet personnel.
3. Conversion en stablecoin (USDT TRC-20 souvent, ou USDC).
4. Mixer ou bridge cross-chain pour obfuscation.
5. Reconversion vers wallet « propre ».
6. Cashout via P2P (Binance P2P, Bisq, marketplaces Telegram).
7. Réception fiat sur compte bancaire d'une mule ou directement.

**Pour OSINT.** Les étapes 2-6 sont **partiellement observables** on-chain (avec expertise). Le cashout final (étape 7) demande réquisitions exchanges. L'OSINT identifie le pattern, l'expertise judiciaire conclut.

#### 72.16 Lien crypto ↔ identité réelle

Le lien entre adresse crypto et personne physique se construit via :

**Pivots ouverts (OSINT).**
- Adresse publiée par la personne (réseaux sociaux, blog, donation publique).
- ENS (Ethereum Name Service) ou Solana names : `marc.eth` lié à compte X public.
- Mention dans leak (Cyprus Confidential mentionne wallet associé à entité).
- NFT publics liés à compte vérifié.
- Activité sur DeFi avec patterns reliés à activité publique.

**Pivots fermés (judiciaire / institutionnel).**
- KYC d'exchange (réquisition).
- IP loguée par exchange.
- Tracé fiat → crypto sur compte bancaire identifié.

**Pour OSINT.** Lien public requiert corroboration multi-sources, cotation prudente (rarement A1). Conclusion typique : « adresse probablement associée à... niveau de confiance modéré, à confirmer judiciairement ».

> **MIRAGE — Épisode 14 : Piste crypto, renvoi OSINT Crypto**
>
> L'investigation a identifié un compte Binance personnel utilisé par Delaunay (MIRAGE 10, via stealer logs). L'email Binance étant `marc.delaunay76@gmail.com`, plusieurs pivots OSINT crypto se présentent.
>
> **Triage en surface (master OSINT).**
> - Recherche d'adresses publiques liées à `marc.delaunay76@gmail.com` ou aux usernames associés : aucun lien direct identifié sur les bases publiques (Etherscan, Walletexplorer.com).
> - Vérification sanctions : email non lié à entité OFAC.
> - L'email est dans stealer logs avec compte Binance, mais sans adresse publique exposée.
>
> **Limite du triage.** L'analyse on-chain réelle (clustering, identification d'adresses Binance retrait, attribution probable) demande l'expertise du cours OSINT Crypto vFULL.
>
> **Recommandation rapport MIRAGE.** Mentionner :
> - Existence d'un compte Binance personnel de Delaunay (cotation B2 via stealer logs).
> - Hypothèse : retraits Binance vers wallet personnel → cashout en stablecoins TRC-20 ou via P2P (pattern courant).
> - **Recommandation expertise crypto forensique** dans le cadre judiciaire pour analyse on-chain approfondie. Le PNF peut mandater cabinet spécialisé pour clustering Chainalysis-grade.
>
> Ce niveau de triage est suffisant pour MIRAGE comme rapport OSINT orienteur. La profondeur attend la procédure judiciaire avec expertise dédiée.

-----

### Chapitre 73 — Workflow intégré personne / société / finance / crypto

#### 73.1 Articulation multi-domaines

Une enquête réelle (comme MIRAGE) articule plusieurs domaines : personne physique, sociétés, finance, crypto, désinformation. L'analyste OSINT doit savoir **orchestrer** ces domaines sans perdre cohérence.

#### 73.2 Architecture d'enquête intégrée

**Phase 1 — Personne physique (Partie V).**
- Identification confirmée.
- Identité numérique (comptes, présence).
- Réseau personnel et professionnel.

**Phase 2 — Sociétés (Partie VI).**
- Cartographie corporate.
- UBO.
- Sociétés liées via dirigeants partagés.

**Phase 3 — Finance (Ch.70-71).**
- Patrimoine visible.
- Sanctions / PEP.
- Indicateurs incohérence.

**Phase 4 — Crypto (Ch.72).**
- Triage.
- Pivots vers OSINT classique.

**Phase 5 — Influence / désinformation (Ch.76).**
- Si applicable, cluster désinformation.

**Phase 6 — Infrastructure (Ch.39-44).**
- Domaines, web, leaks, dark web.

**Phase 7 — Synthèse intégrée.**
- Fiches entités liées.
- Graphe global.
- Timeline globale.
- ACH sur hypothèses principales.

#### 73.3 Cohérence du dossier

**Discipline.** Maintenir un **vault unique** (Obsidian + knowledge graph local). Chaque entité a une fiche. Chaque relation est documentée. Cross-référencement systématique.

#### 73.4 Escalade vers cours spécialisés

À chaque phase, signaux d'escalade :
- Volet crypto profond → OSINT Crypto vFULL.
- Volet financier profond → FININT vFULL.
- Volet dark web → Dark Web vFULL.
- Volet CTI → cours CTI dédié.

L'analyste OSINT master coordonne ces escalades, prépare le terrain pour les spécialistes.

#### 73.5 Limites de chaque domaine

**Personne** : ne pas tomber dans le profilage abusif.

**Sociétés** : ne pas confondre apparence légale et fonction réelle.

**Finance** : indicateurs d'incohérence ≠ preuves de fraude.

**Crypto** : adresse ≠ personne.

**Désinformation** : attribution prudente.

#### 73.6 Synthèse — méthodologie intégrée

| Domaine | Outils maître OSINT | Cours spécialisé |
|---|---|---|
| Personne | Sherlock, Hunter, PimEyes | (master) |
| Sociétés | Pappers, OpenCorporates, ICIJ | FININT vFULL |
| Finance | Cadastre, indicateurs visibles | FININT vFULL |
| Crypto | Etherscan, Walletexplorer | OSINT Crypto vFULL |
| Dark web | Vue ICIJ leaks | Dark Web vFULL |
| Désinformation | Méthodes CIB | (master + EU DisinfoLab) |

-----

### Chapitre 74 — OSINT pour Cyber Threat Intelligence

#### 74.1 OSINT au service de la CTI

La **Cyber Threat Intelligence** (CTI) est la discipline qui produit du renseignement sur les menaces cyber : acteurs, infrastructures adverses, TTP, IOCs.

L'OSINT est l'une des sources majeures de la CTI, avec les feeds commerciaux, l'analyse interne, le partage communauté.

Le présent chapitre fournit la **vue maître**. Pour la profondeur (attribution étatique, threat hunting, analyse intrusion, framework MITRE complet), renvoi vers **cours CTI dédié**.

#### 74.2 IOCs : Indicators of Compromise

**Types d'IOCs.**
- Hashs (MD5, SHA-1, SHA-256) de malware.
- Domaines malveillants.
- IPs malveillantes.
- URLs (phishing, C2).
- Emails (phishing).
- Wallets (rançonneurs).

**Sources publiques OSINT.**
- **VirusTotal** : analyse multi-AV.
- **AbuseIPDB** : IPs malveillantes.
- **URLhaus** (abuse.ch) : URLs.
- **MalwareBazaar** (abuse.ch) : samples.
- **ThreatFox** (abuse.ch) : IOCs.
- **AlienVault OTX** : community-driven.
- **MISP** instances publiques.

#### 74.3 TTPs : Tactics, Techniques, Procedures

**MITRE ATT&CK Framework.** Référence mondiale. Catalogue des comportements adverses.

**Pour OSINT.**
- Identification de TTPs dans rapports publics.
- Cross-référence cas observés vs ATT&CK.
- Cartographie de groupes par TTP signature.

#### 74.4 Modèles d'analyse

**Diamond Model.** 4 features : adversary, capability, infrastructure, victim.

**Cyber Kill Chain (Lockheed Martin).** 7 phases.

**MITRE ATT&CK.** Le plus utilisé en 2026.

#### 74.5 Acteurs et groupes

**Catalogues publics de groupes.**
- **MITRE ATT&CK Groups**.
- **MISP Galaxy**.
- **ThaiCERT APT groups**.
- **CrowdStrike adversary list**.
- **Mandiant APT reports**.

**Précaution attribution.** Attribution à un groupe nommé suppose éléments solides. OSINT permet hypothèse, pas attribution définitive sans corroboration.

#### 74.6 Plateformes CTI

**Open source.**
- **MISP** : Malware Information Sharing Platform. Standard de partage CTI.
- **OpenCTI** : plateforme moderne.
- **YARA** rules.

**Commercial.**
- Recorded Future, Mandiant Advantage, CrowdStrike Falcon X, Flashpoint.
- Coûts élevés (50 k€-500 k€/an).

#### 74.7 Sources publiques CTI

- **abuse.ch** : malware tracker (URLhaus, MalwareBazaar, ThreatFox, FeodoTracker, SSLBL).
- **AlienVault OTX**.
- **MISP communities**.
- **CISA alerts** (US).
- **ANSSI bulletins** (France).
- **NCSC alerts** (UK).
- **CERT-FR** (France).
- **Twitter/X CTI community** (suivi de chercheurs).

#### 74.8 Workflow CTI OSINT

1. **Veille** : monitoring sources publiques.
2. **Collecte IOCs**.
3. **Enrichissement** (VirusTotal, etc.).
4. **Corrélation** (avec autres IOCs, groupes connus).
5. **Diffusion** (interne, MISP communauté).
6. **Action** (blocking, alerting).

#### 74.9 Limites et renvoi

L'OSINT pour CTI couvre la **collecte et corrélation** publique. La profondeur (analyse intrusion, reverse engineering, attribution étatique forensique) est dans le cours CTI dédié.

#### 74.10 Synthèse

L'OSINT contribue substantiellement à la CTI. Pour les analystes CTI, l'OSINT est une discipline de référence. Pour les analystes OSINT, la CTI est un domaine d'application majeur.

#### 74.11 Threat hunting via OSINT

Le **threat hunting** est la recherche proactive de menaces. L'OSINT y contribue par :

**Identification d'IOCs précurseurs.** Monitoring des forums et canaux Telegram cybercriminels pour repérer dès leur émergence : nouveaux domaines de phishing, nouveaux samples malware, nouveaux services offerts (RaaS, accès initial).

**Surveillance d'acteurs.** Suivi des profils, alias, et infrastructures d'acteurs identifiés. Détection des changements de patterns.

**Anticipation de campagnes.** Identification de TTPs émergents avant qu'ils ne se généralisent. Cross-référence avec rapports vendeurs (CrowdStrike, Mandiant, Microsoft, Group-IB).

**Recherches dans les leaks.** Identification précoce de credentials compromis de l'organisation cible avant exploitation par adversaire.

#### 74.12 Méthodologie d'analyse de campagne

Pour caractériser une campagne d'attaque observée :

1. **Collecte initiale.** IOCs depuis logs SOC, EDR, sandboxes.
2. **Enrichissement OSINT.** VirusTotal, abuse.ch, AlienVault OTX pour contexte.
3. **Pivots infrastructure.** Tous domaines / IPs liées via passive DNS, certificats, registrar.
4. **Pivots TTPs.** Comparaison à campagnes connues (MITRE ATT&CK, rapports publics).
5. **Hypothèses acteurs.** Attribution probable avec ACH (Ch.79).
6. **Cotation et publication.** Partage MISP communauté si TLP permet.

#### 74.13 Acteurs majeurs CTI 2026 à connaître

**Groupes étatiques principaux documentés.**

**Russie.**
- **APT28 (Fancy Bear, GRU)** : opérations politiques et défense.
- **APT29 (Cozy Bear, SVR)** : espionnage long terme.
- **Sandworm (GRU)** : opérations destructives, infrastructures critiques.
- **Turla** : espionnage diplomatique.

**Chine.**
- **APT41 (Winnti, Barium)** : double activité espionnage et cybercrime.
- **APT10 (MenuPass)** : MSP supply chain attacks.
- **Volt Typhoon** : infrastructures critiques US.
- **Salt Typhoon** : télécoms (révélé 2024-2025).

**Iran.**
- **APT35 (Charming Kitten)** : journalistes, dissidents.
- **APT34 (OilRig)** : industrie pétrolière.
- **MuddyWater** : opérations diversifiées.

**Corée du Nord.**
- **Lazarus Group** : monétaire, ransomware, hacks crypto.
- **APT38** : finance.
- **Kimsuky** : espionnage.

**Cybercriminels.**
- **LockBit** (ransomware, opération en cours après tentative démantèlement 2024).
- **BlackCat / ALPHV** (ransomware).
- **Conti** (dissous 2022, mais successeurs : Royal, Akira, etc.).
- **FIN groups** : cybercrime financier.

**Sources de référence.** MITRE ATT&CK Groups, MISP Galaxy, ThaiCERT APT, CrowdStrike adversary list, Mandiant APT reports, Microsoft Threat Intelligence reports.

#### 74.14 Frameworks d'analyse

**Diamond Model (Caltagirone, Pendergast, Betz, 2013).** Quatre features : adversary, capability, infrastructure, victim. Permet structurer analyse intrusion.

**Cyber Kill Chain (Lockheed Martin, 2011).** Sept phases : reconnaissance, weaponization, delivery, exploitation, installation, command & control, actions on objectives. Plus orienté détection.

**MITRE ATT&CK.** Le plus utilisé en 2026. Catalogue exhaustif TTPs adverses, par technique, par groupe, par plateforme. Mises à jour régulières.

**Unified Kill Chain (Pols, 2017).** Synthèse Diamond + Kill Chain + MITRE.

**Pyramid of Pain (Bianco, 2013).** Hiérarchie des IOCs par difficulté pour l'adversaire (hashs faciles à changer, TTPs très difficiles).

#### 74.15 Workflow CTI complet

**Cycle de renseignement CTI.**

1. **Direction.** Quelles questions stratégiques ? Quels actifs à protéger ?
2. **Collecte.** OSINT + feeds payants + interne (logs, sandboxes).
3. **Traitement.** Normalisation, déduplication, enrichissement.
4. **Analyse.** Caractérisation, attribution, prédictions.
5. **Diffusion.** Bulletins, alertes, briefings.
6. **Feedback.** Boucle vers direction.

**Maturité CTI.**
- **Tactical.** IOCs, signatures, alertes opérationnelles.
- **Operational.** Campagnes, modes opératoires.
- **Strategic.** Tendances long terme, attribution étatique, contexte géopolitique.

#### 74.16 Limites et renvoi

L'OSINT pour CTI couvre la **collecte et corrélation** publique. La profondeur (analyse intrusion, reverse engineering, attribution étatique forensique, threat hunting on-prem) est dans le **cours CTI dédié** (à venir dans la bibliothèque).

-----

### Chapitre 75 — Surface d'attaque et exposition cyber

#### 75.1 De la CTI à la surface d'attaque

L'**analyse de surface d'attaque** (Attack Surface Management — ASM) identifie ce qu'un attaquant verrait d'une organisation : domaines, sous-domaines, services exposés, technologies, fuites.

C'est le pendant **défensif** de la CTI : savoir ce qu'on expose pour le protéger.

Voir Ch.41 pour la vue technique. Ce chapitre approfondit l'angle CTI.

#### 75.2 Composantes de la surface d'attaque

**Surface technique.**
- Domaines, sous-domaines (Ch.39-40).
- IPs, ASN (Ch.40).
- Services exposés (Shodan, Censys).
- Technologies (Wappalyzer, BuiltWith).
- Buckets cloud, S3 (Ch.41).
- GitHub leaks (Ch.41).

**Surface humaine.**
- Identités d'employés (LinkedIn, communiqués).
- Emails exposés.
- Présences réseaux sociaux.
- Information publiable sur procédures internes.

**Surface organisationnelle.**
- Sous-traitants, prestataires.
- Supply chain logicielle.
- Partenaires.

#### 75.3 Outils ASM

**Commercial.**
- **Bitsight** : standard.
- **SecurityScorecard**.
- **RiskIQ** (Microsoft).
- **Censys Continuous**.
- **Shodan Monitor**.
- **PaloAlto Cortex Xpanse**.

**Open source / gratuit.**
- **Amass** + **subfinder** (Ch.40).
- **GoSpider**, **httpx**.
- Combinaisons custom.

#### 75.4 Workflow ASM

1. **Inventaire** : domaines, IPs, services.
2. **Scan passif** : Shodan, Censys.
3. **Identification vulnérabilités connues**.
4. **Cloud assets** : buckets, exposed services.
5. **Code leaks** : GitHub search.
6. **Email exposure** : HIBP, DeHashed.
7. **Stealer logs** : Hudson Rock.
8. **Synthèse risque**.
9. **Recommandations**.

#### 75.5 Typosquatting et phishing

**DNSTwist** pour identifier typosquats.

**Monitoring** : alertes nouveaux enregistrements suspects.

**Pour due diligence.** Identifier campagnes de phishing visant une entité.

#### 75.6 Maturité sécurité comme signal

L'exposition cyber d'une organisation est un **signal** de maturité sécurité.

**Signaux maturité haute.**
- Bonnes pratiques SPF/DKIM/DMARC.
- Pas de secrets GitHub.
- Buckets cloud sécurisés.
- Patches à jour.

**Signaux maturité basse.**
- Services obsolètes exposés.
- Buckets ouverts.
- Secrets sur GitHub.
- Email patterns prévisibles + breaches massives.

#### 75.7 Renvoi CTI

Pour la profondeur (threat hunting, intrusion analysis, attribution avancée, reverse engineering), renvoi vers **cours CTI dédié**.

#### 75.8 Synthèse — ASM en pratique

L'ASM OSINT est une compétence de plus en plus demandée : par les RSSI (vue interne), par les acquéreurs (M&A), par les régulateurs (cyber resilience).

-----

### Chapitre 76 — Désinformation, influence et guerre cognitive

#### 76.1 La désinformation comme objet OSINT

La **désinformation** et les **opérations d'influence** sont devenues des objets centraux d'investigation OSINT. Volume massif, sophistication croissante (IA generative, deepfakes), enjeux politiques majeurs.

#### 76.2 Typologie

**Misinformation.** Information fausse diffusée sans intention de nuire (erreur, rumeur).

**Disinformation.** Information fausse diffusée avec intention de nuire (manipulation délibérée).

**Malinformation.** Information vraie diffusée pour nuire (doxxing, fuites sélectives).

#### 76.3 Coordinated Inauthentic Behavior (CIB)

**CIB** (terme Meta). Activités coordonnées simulant des opinions ou réactions organiques.

Voir Ch.35 pour méthodologie détaillée.

#### 76.4 Amplification et narratifs

**Amplification.**
- Bots et faux comptes.
- Cluster de retweets / partages.
- Trolls coordonnés.
- Médias relais (sympathisants idéologiques ou agents).

**Narratifs.**
- Histoire dominante propagée.
- Cohérence à travers comptes apparemment indépendants.
- Variations adaptées par audience.

#### 76.5 Faux médias et faux experts

**Faux médias.** Sites imitant médias établis (Doppelgänger : imitation Le Monde, Bild, Welt, etc.).

**Faux experts.** Profils synthétiques (photo IA, bio fictive) présentés comme experts dans des domaines pour donner crédibilité.

**Cas d'usage MIRAGE.** Le faux média `info-finance-eu.com` créé pour amplifier le narratif diffamatoire contre Berthier.

#### 76.6 Acteurs de référence à connaître

**Internet Research Agency (IRA, Russie).** Active 2014-2024. Saint-Pétersbourg.

**Doppelgänger (Russie).** Faux médias imitant Le Monde, Bild, etc. Documenté VIGINUM 2024.

**Spamouflage (Chine).** Campagnes pro-PRC sur X, YouTube, Facebook.

**Indian Chronicles (Inde, EU DisinfoLab 2019-2020).** 750+ faux médias.

**Storm-1516** (Russie, MS Threat Intelligence). Operations 2024-2026.

#### 76.7 Méthodes de détection

Voir Ch.35 pour détail.

**Récap.**
- Cadence et patterns temporels.
- Réseaux d'amplification (Gephi).
- Narratifs convergents.
- Coordination de hashtags.
- Photos générées par IA.
- Métadonnées techniques (registrar, hosting).
- Infrastructure partagée (GA, tracker).

#### 76.8 Cadre français : VIGINUM

**VIGINUM** (Service de vigilance et protection contre les ingérences numériques étrangères, SGDSN). Mission : détecter et caractériser les phénomènes inauthentiques affectant le débat public numérique.

**Publications.** Rapports techniques publics (notamment sur Doppelgänger).

**Coopération.** Avec acteurs européens, EU DisinfoLab.

#### 76.9 Cadre européen : EEAS et DSA

**EEAS** (European External Action Service). EUvsDisinfo : monitoring désinformation Russie.

**DSA** (Digital Services Act 2024). Obligations plateformes sur modération, transparence, accès chercheurs.

#### 76.10 Cas d'usage MIRAGE

Le volet désinformation MIRAGE intègre :
- Cluster 8 comptes X coordonnés.
- Cluster 9 canaux Telegram.
- 2 faux médias (`verites-technovert.com`, `info-finance-eu.com`).
- 3 fausses photographies (face swap + stock).
- 1 vidéo deepfake.
- Possible coordination via canal Telegram « social media boost » identifié.

**Attribution.** Cohérence d'éléments : narratifs convergents, infrastructure partagée (GA partagé), timing coordonné. **Attribution à Delaunay** : indirecte. Pas de lien direct identifiable Delaunay → service de désinformation. Cohérence d'intérêt (Delaunay cible Berthier qui l'a dénoncé). **Cotation B3** sur l'attribution à Delaunay : cohérent, non démontré, à approfondir judiciairement.

#### 76.11 Cas Doppelgänger : étude détaillée

**Doppelgänger** (2022-2026, en cours) est l'opération d'influence russe la plus médiatisée depuis l'invasion de l'Ukraine. Documentée VIGINUM 2024, EU DisinfoLab, Recorded Future.

**Méthodologie.**
- Clonage de sites de médias établis (Le Monde, Bild, Welt, The Guardian, Fox News, etc.) avec domaines typosquattés.
- Production massive d'articles favorables à narratifs pro-russes.
- Diffusion via Twitter/X, Facebook, et notamment Telegram canaux russes.
- Amplification par bots et comptes coordonnés.

**Volume.** Plus de 1000 domaines typosquats identifiés. Production mensuelle de centaines d'articles. Touches multiples langues : anglais, français, allemand, espagnol, polonais, italien, hébreu.

**Attribution.** Selon rapports US Treasury 2024 et UE Sanctions, opérée par sociétés russes Structura National Technology et Social Design Agency, liées au Kremlin.

**Indicateurs détectables.**
- Domaines typosquattés enregistrés en lot.
- Infrastructure d'hébergement commune (analyses passives DNS).
- Patterns linguistiques (traductions automatiques détectables).
- Coordination temporelle de publication.
- Cross-amplification entre comptes connus pro-russes.

#### 76.12 Cas Spamouflage : étude détaillée

**Spamouflage** (aussi appelé Dragonbridge par Mandiant) est l'opération d'influence chinoise documentée depuis 2017, intensifiée 2019-2026.

**Méthodologie.**
- Volume massif de faux comptes sur YouTube, Twitter/X, Facebook, TikTok.
- Production en masse de contenu vidéo, infographies, articles.
- Targets : sujets sensibles à Beijing (Hong Kong, Taïwan, Xinjiang, COVID origines).
- Adaptations linguistiques multiples.

**Volume.** Centaines de milliers de comptes identifiés sur durée. Plateformes ont supprimé par vagues (Twitter en 2019, 2020, 2021 ; YouTube régulier ; Meta).

**Faiblesses opérationnelles** documentées :
- Erreurs linguistiques (traduction faible).
- Bots peu sophistiqués (cadence anormale, photos volées).
- Amplification mutuelle artificielle (faible engagement organique).

**Documentation.** Graphika rapports successifs, Stanford Internet Observatory, Microsoft Threat Analysis Center, Mandiant.

#### 76.13 Cas Storm-1516 : opérations 2024-2026

**Storm-1516** (Microsoft Threat Intelligence). Opération russe identifiée à partir de 2024.

**Caractéristiques.**
- Production de fausses vidéos « whistleblower » prétendument issues d'institutions ukrainiennes ou occidentales.
- Utilisation marquée de **deepfakes audio-vidéo** (IA générative).
- Cibles : élections, soutien à l'Ukraine.
- Distribution multi-plateformes.

**Sophistication.** Storm-1516 marque la **maturation de l'usage IA dans les opérations d'influence**. Distinction avec opérations précédentes : moins de comptes-zombies, plus de production de contenu synthétique convaincant.

**Pour OSINT.** Cas d'étude pour détection deepfakes (Partie VIII du cours). Outils : Sensity, Intel FakeCatcher, analyse contextuelle. Attribution par Microsoft / partenaires.

#### 76.14 Méthodologie de détection de campagne CIB

**Étape 1 — Identification du signal.** Pic anormal de mentions sur sujet. Patterns inhabituels.

**Étape 2 — Cartographie.** Liste des comptes / domaines / canaux. Taille du cluster.

**Étape 3 — Analyse temporelle.** Heatmap d'activité. Coordination détectable.

**Étape 4 — Analyse de profils.** Photos IA, bios génériques, dates de création groupées.

**Étape 5 — Analyse de contenu.** Narratifs convergents. Indices LLM-generated.

**Étape 6 — Analyse de réseau.** Communautés détectées (Gephi Louvain). Nœuds pivots.

**Étape 7 — Analyse d'infrastructure.** Pour les domaines : registrar commun, hosting, trackers partagés.

**Étape 8 — Hypothèses d'attribution.** Acteur étatique ? Officine privée ? Concurrent ? Activiste authentique amplifié ?

**Étape 9 — Cotation et formulation.** Prudence sur attribution finale. Faisceaux d'indices.

**Étape 10 — Signalement / publication.** Plateformes, VIGINUM si applicable, communauté (EU DisinfoLab, Information Laundromat).

#### 76.15 Contre-mesures et résilience

Pour une organisation visée par campagne de désinformation :

**Détection.**
- Monitoring proactif des mentions (Brandwatch, Talkwalker).
- Veille sur acteurs connus.
- Alertes sur nouvelles campagnes.

**Documentation.**
- Captures et préservation rigoureuse.
- Analyse forensique des contenus.
- Documentation des liens entre acteurs.

**Réponse.**
- Signalement aux plateformes (X, Meta, Telegram, YouTube).
- Communication factuelle ciblée (pas amplification du narratif).
- Action judiciaire si caractérisée (diffamation, atteinte à l'image).
- Plainte VIGINUM si caractère étatique étranger.

**Résilience long terme.**
- Surveillance continue.
- Construction d'une « bande son » authentique (présence médiatique légitime).
- Formation des porte-paroles.

#### 76.16 Économie de la désinformation à louer

Un marché émergent : **désinformation as a service**. Officines proposent campagnes coordonnées clés en main.

**Acteurs documentés.**
- **Team Jorge** (Israël) : révélé par Forbidden Stories 2023. Campagnes ciblées politiques et corporates.
- **Cambridge Analytica** (UK, fermée 2018) : historique. Manipulation Brexit, Trump.
- **Officines russes** : Internet Research Agency (Prigozhin, dissoute 2024), Social Design Agency (Doppelgänger).
- **Officines diverses** au Moyen-Orient, Inde, Asie du Sud-Est, Afrique.

**Pour OSINT.** L'attribution à une officine commerciale (par opposition à étatique) est elle aussi complexe. Indicateurs : qualité technique commerciale, ciblage économique vs politique, mode opératoire.

#### 76.17 Référentiels et bibliographies

**Référentiels CIB / désinformation 2026.**
- **DISARM Framework** (anciennement AMITT). Framework communautaire pour catégoriser désinformation, équivalent MITRE ATT&CK pour info-ops.
- **NATO StratCom Centre of Excellence** (Riga). Rapports techniques.
- **VIGINUM rapports** (France).
- **EU DisinfoLab** publications.
- **Stanford Internet Observatory** études.
- **Graphika** rapports CIB.
- **First Draft / Meedan** ressources fact-checking.

> **MIRAGE — Épisode 17 : Campagne d'influence coordonnée**
>
> L'analyste synthétise le volet désinformation.
>
> **Architecture identifiée.**
> 1. Cluster X : 8 comptes coordonnés (création septembre-octobre 2025, activité concentrée sur diffamation Berthier).
> 2. Cluster Telegram : 9 canaux retweetant et amplifiant.
> 3. Faux médias : `verites-technovert.com` + `info-finance-eu.com`, Google Analytics partagé.
> 4. Fausses photographies : 3 face swap sur backgrounds Unsplash/Pexels.
> 5. Vidéo deepfake : audio-vidéo composite avec voice cloning.
> 6. Possible prestataire : canal Telegram `@socialmedia_boost_fr` propose explicitement ce type de service (cohérence des prix, timing).
>
> **Narratif central.** « Berthier est un employé malveillant ayant manipulé les comptes pour nuire à TechnoVert ».
>
> **Cohérence temporelle.** Démarrage octobre 2025 (1 mois après licenciement Berthier). Pic en mars 2026 (avant audience prud'homale).
>
> **Attribution.**
> - Lien direct au commanditaire (Delaunay ou entourage TechnoVert) : non démontré directement.
> - Cohérence d'intérêt : forte (Berthier est le lanceur d'alerte des écritures suspectes liées à Delaunay).
> - Cohérence temporelle : forte.
> - Cotation B3 sur attribution à Delaunay : hypothèse cohérente, démonstration à approfondir judiciairement.
>
> **Pour le rapport.** « Une campagne de désinformation coordonnée a été identifiée, ciblant Antoine Berthier, lanceur d'alerte, articulée sur 8 comptes X, 9 canaux Telegram, 2 faux médias, 3 photographies fabriquées, 1 vidéo deepfake. La cohérence temporelle et thématique de cette campagne avec les intérêts de Marc Delaunay (mis en cause par le signalement Berthier) suggère un lien d'attribution probable, sans démonstration directe en sources ouvertes. Une expertise complémentaire dans le cadre judiciaire (réquisitions opérateurs Telegram et registrars) permettrait l'attribution formelle. »

-----

### Chapitre 77 — Renseignement économique et due diligence

#### 77.1 Convergence avec OSINT corporate

Le **renseignement économique** (IE) et la **due diligence** convergent largement avec l'OSINT corporate (Partie VI). Différence principale : finalité (compétition économique vs investigation pénale).

#### 77.2 Cas d'usage IE

- Veille concurrentielle.
- Surveillance de marché.
- Identification de risques fournisseurs.
- Préparation de négociation.
- Veille technologique.
- Recherche d'informations sectorielles.

#### 77.3 Cas d'usage due diligence

- Pré-transaction M&A.
- Onboarding partenaire commercial.
- Vérification candidat senior.
- Conformité supply chain (CSDDD).
- Audit de portefeuille investisseur.

#### 77.4 Outils communs avec corporate

Voir Parties VI et X. Pappers, OpenCorporates, sanctions, adverse media, etc.

#### 77.5 Outils spécifiques IE / DD

**Veille technologique.**
- Brevets : Espacenet (EPO), USPTO, Google Patents.
- Publications scientifiques : Google Scholar, Semantic Scholar.
- Salons et conférences.

**Veille concurrentielle.**
- Brandwatch, Talkwalker.
- Communiqués de presse.
- Annonces d'embauche (signal de stratégie).

**Supply chain.**
- Import-export databases (Panjiva, ImportGenius).
- Customs records (US, India publics partiel).
- Bills of lading.

#### 77.6 Acteurs sectoriels

**France.** Cabinet IE : ESL & Network, Anios, etc. **École militaire** : EGE.

**International.** Kroll, Control Risks, FTI Consulting, K2 Intelligence.

#### 77.7 Méthodologie due diligence

Voir Ch.38. Standard professionnel.

#### 77.8 Conformité CSDDD

La **CSDDD** (Ch.7) impose vigilance supply chain. Méthodologie :
- Identification fournisseurs.
- Screening (sanctions, adverse media).
- Évaluation risques humains et environnementaux.
- Mesures de mitigation.
- Reporting.

OSINT massivement mobilisée.

#### 77.9 Limites

**Information asymétrique.** L'OSINT ne révèle qu'une partie. Audit terrain (visites, entretiens) complète.

**Désinformation par l'entité.** Greenwashing, ESG-washing.

#### 77.10 Synthèse

IE et due diligence sont des marchés massifs pour l'OSINT corporate professionnelle. Renvoi cours dédié pour profondeur.

-----
