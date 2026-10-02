---
title: 'Chapitre 35 — Privacy coins : Monero, Zcash, limites radicales'
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VI — Obfuscation, laundering et cashout
  - index.md
---

Les **privacy coins** sont des cryptomonnaies conçues pour l’anonymat. Contrairement à Bitcoin (pseudonyme) ou aux mixers (obfuscation ajoutée), les privacy coins ont l’anonymat **par construction**. Ce chapitre couvre les principales et leurs implications pour l’enquête.

## 35.1 Monero (XMR)

**Lancé** : avril 2014 (fork de Bytecoin).

**Principes** :

**Ring signatures**. Chaque transaction Monero contient des signatures multiples — la vraie + plusieurs « decoys » (faux signataires plausibles). Impossible de savoir quel signataire est le vrai. Effet : l’**émetteur** d’une transaction est ambigu parmi un ring de candidats.

**Ring Confidential Transactions (RingCT)**. Les **montants** sont cachés cryptographiquement. Visible : « cette transaction transfère un montant X ». Pas visible : la valeur de X.

**Stealth addresses**. Le **destinataire** d’une transaction est caché. Adresse de réception « one-time » dérivée pour chaque transaction. Lien entre adresse on-chain et destinataire réel non-trivial.

**Effet combiné** : émetteur masqué, montant masqué, destinataire masqué. Quasi-anonymat.

**Adoption** : populaire dans dark web markets, ransomware (certains exigent Monero), particuliers privacy-conscious.

## 35.2 Limites de Monero

**Pas absolument anonyme** :

**Decoy quality**. Les decoys sont sélectionnés selon algorithme. Si l’algorithme a des biais ou si le ring inclut decoys peu plausibles (par exemple, decoys « trop vieux »), analyse statistique peut réduire l’incertitude. Recherche académique active.

**Vulnérabilités d’implémentation**. Certaines versions de Monero ont eu des vulnérabilités permettant dé-anonymisation partielle. Patches successifs.

**Usage off-chain**. Si l’utilisateur achète Monero sur exchange KYC, l’achat est traçable. La conversion en autres actifs après usage Monero est aussi un point.

**Erreurs OPSEC**. Réutilisation de wallets avec multiple couches d’obfuscation peut leak. Patterns d’usage peuvent identifier acteur.

**Decoy attacks** : des chercheurs ont publié plusieurs papers sur dé-anonymisation partielle Monero. Exemples : sélection de decoys old enough to be unrealistic, timing analysis sur outputs.

**Pour l’enquêteur** : Monero est **largement opaque** pour l’analyse on-chain pure. L’enquête se déplace vers les **points off-chain** (exchanges, achats fiat, OPSEC errors).

## 35.3 Zcash (ZEC)

**Lancé** : octobre 2016.

**Principes** :

**zk-SNARKs** : zero-knowledge proofs avancés permettant transactions complètement privées (montants, parties cachés).

**Mode dual** :

- **Transparent** : transactions comme Bitcoin, lisibles publiquement.
- **Shielded** : transactions privées via zk-SNARKs.

**Adoption** : majoritairement transparent. La fraction shielded est faible. Des recherches indiquent que les transactions Zcash sont à >80% transparentes.

## 35.4 Limites Zcash

**Mode transparent** : analysable comme Bitcoin.

**Mode shielded** : opaque, mais **anonymity set faible** (peu d’utilisateurs en mode shielded). Patterns d’entrée/sortie shielded peuvent réduire l’incertitude.

**Trusted setup** : Zcash early required a trusted setup ceremony. Si la randomness a été compromise, attaque théorique possible. Ceremonies multiples, peu probable d’être compromis pour les versions récentes.

**Pour l’enquêteur** : Zcash est **moins opaque que Monero en pratique** parce que l’usage shielded est minoritaire. Pour transactions transparentes, méthode standard. Pour shielded, limites similaires à Monero.

## 35.5 Dash et autres

**Dash** (lancé 2014) : « PrivateSend » est CoinJoin amélioré. Moins efficace que Monero, plus simple à analyser.

**Beam, Grin** (lancés 2019) : implémentent Mimblewimble. Concept différent (no addresses, transactions agrégées). Adoption faible.

**Pirate Chain (ARRR)** : zk-SNARKs forced (pas de mode transparent). Faible volume.

**Pour l’enquêteur** : Monero domine clairement le segment privacy. Autres rares en pratique.

## 35.6 Méthode d’enquête face à Monero

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

## 35.7 Cas réels Monero

**Ransomware Monero-only** : Akira (cf MIXSHADOW), REvil (historique), DarkSide variantes. Demandent paiement en XMR pour rupture immédiate.

**Darknet markets** : multiple marchés russophones et anglophones acceptent ou exigent Monero.

**Acteurs étatiques Lazarus** : utilisation de Monero documentée pour certaines opérations.

**Limitation** : exchanges régulés ont **massivement délistsé Monero** depuis 2020. Coinbase, Kraken, Binance ont retiré Monero. Cela limite cashout pour criminels (plus difficile de revenir en fiat sans suspicion). Effet partiel — exchanges secondaires et P2P continuent.

## 35.8 Tendances 2024-2026

**Pression réglementaire** : Monero ciblé par autorités. Multiples démarches pour limiter accessibilité.

**Améliorations techniques Monero** : protocole évolue (Bulletproofs, Triptych, autres). Augmente anonymat.

**Recherche académique active** : papers réguliers sur dé-anonymisation partielle.

**Migration** : certains acteurs criminels migrent vers Monero alternatives ou vers techniques mixtes (Bitcoin + privacy layers comme Lightning Network ou CoinJoin chained).

## 35.9 Le message à intérioriser

> Monero est une rupture de visibilité quasi-totale pour l’analyse on-chain. L’enquêteur OSINT honnête le reconnaît, le documente, et déplace l’enquête vers les angles off-chain. Promettre un « démêlage » Monero = sur-promesse risquée.

## 35.10 Fil rouge — MIXSHADOW : pas de Monero pour Akira… cette fois

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
