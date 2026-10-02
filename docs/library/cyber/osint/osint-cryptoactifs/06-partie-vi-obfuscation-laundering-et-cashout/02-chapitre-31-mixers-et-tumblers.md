---
title: Chapitre 31 — Mixers et tumblers
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VI — Obfuscation, laundering et cashout
  - index.md
---

Les **mixers** (ou tumblers) sont des services qui mélangent les fonds de multiples utilisateurs pour casser la traçabilité. Ils existent depuis les premiers jours du Bitcoin. Plusieurs ont été démantelés ; d’autres continuent. Ce chapitre couvre leur fonctionnement et limites de l’analyse.

## 31.1 Qu’est-ce qu’un mixer

**Principe** : un mixer reçoit les fonds d’utilisateur A et lui restitue, après délai, des fonds **différents** (issus d’autres utilisateurs B, C, D, etc.) à une adresse de destination différente.

**Effet** : casser le lien direct entre origine des fonds et destination. Si A a déposé 1 BTC entaché et reçoit 1 BTC « propre » (anciennement détenu par B), le lien on-chain entre origine et destination est rompu.

**Types** :

- **Mixers custodial** : service centralisé qui détient les fonds pendant le mélange. Tornado Cash (originellement), Helix, Bitcoin Fog, Chipmixer, Samourai Whirlpool partiellement.
- **CoinJoin (peer-to-peer, non-custodial)** : protocole coopératif sans custodian central. Wasabi, Samourai. Cf Ch.32.

**Différence** :

- Custodial : confiance dans l’opérateur (qui peut voler les fonds).
- Non-custodial : pas de risque de vol, mais moins « profond » comme mélange.

## 31.2 Fonctionnement d’un mixer custodial classique

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

## 31.3 Tornado Cash : le mixer décentralisé

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

## 31.4 Sanctions OFAC sur Tornado Cash

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

## 31.5 Analyse statistique des sorties Tornado

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

## 31.6 Mixers démantelés

**Helix** (saisi 2020) : opérateur Larry Harmon condamné, 11 M USD saisis.

**Bitcoin Fog** (saisi 2021) : opérateur Roman Sterlingov condamné en 2024.

**Chipmixer** (saisi mars 2023) : opération Allemagne / Belgique, 46 000 BTC (~2,7 Mrd EUR) saisis ou identifiés.

**Sinbad.io** (sanctionné OFAC novembre 2023) : successeur d’autres mixers démantelés.

**Samourai Wallet** (saisi avril 2024) : opérateurs Keonne Rodriguez et William Hill inculpés US.

**Pour l’enquêteur** : démantèlements créent **opportunités d’analyse** post-saisie. Logs récupérés permettent dé-mixage rétroactif. Multiple cas où des fonds ransomware historiques ont été tracés grâce à logs Helix / Bitcoin Fog post-saisie.

## 31.7 Méthode d’enquête face à un mixer

**Étape 1 — Reconnaître le mixer**. Dépôts vers adresses connues de mixers (labels outils pro, listes publiques).

**Étape 2 — Documenter le dépôt**. Timestamp, montant, adresse source, identifiant du pool / mixer.

**Étape 3 — Lister les retraits dans la pool autour du timing**. Pour pool active, peut être beaucoup. Pour pool peu active, peut être peu.

**Étape 4 — Analyse statistique**. Timing, montant, behavioral. Identifier candidats probables.

**Étape 5 — Croiser avec contexte externe**. Si l’opérateur est suspecté d’utiliser Tornado et a une adresse de retrait probable, vérifier cohérence.

**Étape 6 — Calibrer la confiance**. Pour analyse statistique pure, attribution rarement « probable » (souvent « possible » ou plus faible).

**Étape 7 — Rapport avec limites explicites**.

## 31.8 L’impact des sanctions sur l’usage

**Pre-sanctions août 2022** : Tornado Cash utilisé massivement, par Lazarus et nombreux autres acteurs. Volume mensuel : centaines de M USD.

**Post-sanctions** : volume a chuté drastiquement. Mais Tornado **continue à fonctionner** (code immutable). Acteurs critiques (Lazarus) continuent à l’utiliser malgré sanctions, acceptant la pression sur off-ramps.

**Migrations** : certains acteurs ont migré vers :

- Sinbad.io (avant sanctions OFAC).
- Mixers Bitcoin résiduels (Wasabi, Samourai pre-saisie).
- Bridges + DEX comme alternatives partielles.
- Privacy coins (Monero).

## 31.9 Stratégie défensive face aux mixers

**Côté exchange** : screening de dépôts pour détecter fonds tracés à mixers (KYT Chainalysis, équivalents). Refus d’acceptation ou alerting.

**Côté plateforme** : Many DEX et frontends ont implémenté blocages des adresses Tornado post-sanctions.

**Côté autorités** : poursuite des opérateurs (Pertsev, Storm), sanctions continues.

## 31.10 Fil rouge — MIXSHADOW : analyse Tornado

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
