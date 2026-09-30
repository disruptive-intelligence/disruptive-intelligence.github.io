---
title: Chapitre 40 — Cas 5
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VII — Cas pratiques déroulés
  - index.md
---

enquête Monero — quand la blockchain ne suffit pas

**Profil de l’enquête** : enquête honnête sur un cas où Monero rompt la traçabilité on-chain. Cas pédagogique pour montrer comment **gérer la rupture** et déplacer l’enquête vers les angles off-chain.

## 40.1 Le contexte

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

## 40.2 Phase 1 — Documenter la transaction Monero

**Étape 1 — TXID Monero**.

SantéTech fournit le TXID Monero de la transaction de paiement.

Sur explorateurs Monero (xmrchain.net, etc.) :

- TXID confirmée.
- Date / heure.
- **Mais** : pas de visibilité sur expéditeur (ring signatures), pas de visibilité sur destinataire (stealth address), pas de visibilité sur montant exact (RingCT) — sauf information transmise hors-chain par les parties.

SantéTech a la « view key » de sa propre transaction (donnée par leur wallet) qui permet de **vérifier qu’ils ont bien envoyé X XMR**. Mais pas de visibilité sur ce qui se passe ensuite.

**Étape 2 — Limite explicite**.

L’analyste documente : « La transaction de 35 XMR est confirmée par les view keys de SantéTech. Au-delà de la réception par Helldown, la traçabilité on-chain Monero n’est pas possible. »

## 40.3 Phase 2 — Tracer les XMR avant le paiement

**Insight** : si on ne peut pas tracer les XMR **après** le paiement, on peut tenter de tracer **comment** SantéTech a obtenu les 35 XMR.

**Pourquoi utile ?**

- Les XMR ont été **achetés** via un service OTC français.
- Le service OTC a obtenu ces XMR de quelque part.
- Si on remonte la chaîne d’origine, on pourrait identifier des patterns.

Mais pour ce cas spécifique : les XMR achetés par SantéTech proviennent d’un service OTC légitime — origine sans intérêt pour l’enquête Helldown (qui a reçu les XMR, pas envoyé).

## 40.4 Phase 3 — Pivot vers caractérisation Helldown

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

## 40.5 Phase 4 — Angles off-chain

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

## 40.6 Phase 5 — Rapport et limites

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

## 40.7 Bilan

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

## 40.8 Apprentissage clé

**Pour Monero, l’enquête est différente** :

1. **Mandat doit être réaliste**. Cf cadrage révisé. Le client doit comprendre **dès le départ** que tracker Monero on-chain n’est pas possible.
1. **L’enquête se déplace off-chain**. Profil acteur, vecteurs, infrastructure, communications, services off-chain — tout sauf on-chain pure.
1. **Valeur = renseignement et coordination**. Pas récupération.
1. **Calibration honnête essentielle**. Le rapport ne « tente pas » de faire passer pour acquis ce qui ne l’est pas.
1. **Coordination multi-source amplifie**. Une victime isolée a peu d’angles ; multi-victimes consolidées peuvent révéler des patterns convergents.

**Pour l’analyste OSINT** : refuser un mandat « tracker mes XMR » est parfois la décision **professionnellement correcte**. Proposer un mandat alternatif réaliste préserve la crédibilité et apporte de la valeur.

## 40.9 Synthèse Partie VII

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
