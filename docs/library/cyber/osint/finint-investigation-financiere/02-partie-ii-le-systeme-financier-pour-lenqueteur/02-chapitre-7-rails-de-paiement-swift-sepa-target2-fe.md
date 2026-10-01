---
title: 'Chapitre 7 — Rails de paiement : SWIFT, SEPA, TARGET2, Fedwire, ACH'
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie II — Le système financier pour l’enquêteur
  - index.md
---

## Objectif du chapitre

Connaître les **principaux rails de paiement** mondiaux, leurs caractéristiques techniques, leurs vitesses, leurs niveaux de surveillance, et la signification de leur usage dans un schéma observé.

## Le concept

Un « rail de paiement » est l’**infrastructure technique** qui permet à un ordre de paiement émis par une banque d’arriver à une autre banque. Plusieurs rails coexistent, chacun avec son périmètre, sa vitesse, sa fiabilité et son niveau de transparence.

**SWIFT** (Society for Worldwide Interbank Financial Telecommunication). Réseau de **messagerie** sécurisée entre banques, utilisé pour les paiements internationaux et de gros. SWIFT n’est pas un rail de règlement : il transmet des *messages* qui déclenchent des règlements via les comptes correspondants ou des systèmes de règlement nationaux. Les messages SWIFT pertinents pour l’analyste FININT (annexe B pour la lecture détaillée) :

- **MT103** — virement client (single customer credit transfer). Le format de référence pour un virement international depuis un client donneur d’ordre vers un bénéficiaire dans une autre banque.
- **MT202** — transfert interbancaire (financial institution transfer). Mouvement de fonds entre banques correspondantes pour le compte de leurs clients ou pour leurs propres besoins de trésorerie.
- **MT940** — relevé de compte SWIFT (customer statement message). Utilisé pour la reconstitution de flux quand le compte est tenu par une banque tierce.

Depuis 2022-2024, SWIFT migre progressivement vers le format **ISO 20022** (richesse des données plus grande, structuration améliorée). C’est une bonne nouvelle pour l’analyse FININT (champs plus complets, structurés), à condition que les contreparties soient également migrées.

**SEPA** (Single Euro Payments Area). Espace de paiement européen unifié pour les virements en euros. Couvre 36 pays (UE + EEE + UK + Suisse + Andorre + Monaco + Saint-Marin + Vatican). Les rails :

- **SEPA Credit Transfer (SCT)** : virement standard, J+1.
- **SEPA Instant Credit Transfer (SCT Inst)** : virement instantané (10 secondes), 24/7, plafond historique 100 000 €, étendu en pratique. Depuis le règlement « Instant Payments » de 2024, les banques européennes doivent proposer ce service par défaut, avec une montée en charge progressive.
- **SEPA Direct Debit (SDD)** : prélèvement.

L’analyste FININT note : un virement instantané est **non-réversible** (sauf consentement du bénéficiaire) ; il est devenu un canal privilégié des fraudes au virement avec urgence (BEC, voir chapitre 44).

**TARGET2 / TARGET / T2** (Trans-European Automated Real-time Gross settlement Express Transfer system). Système de règlement de gros de la BCE. Règlements interbancaires de la zone euro pour gros montants. Utilisé pour les transferts entre banques centrales, les marchés monétaires, les opérations de politique monétaire. En 2023 a été remplacé techniquement par **TARGET / T2** (avec T2S pour les titres) — l’analyste retient surtout que TARGET2 est l’infrastructure de gros de la zone euro.

**Fedwire** (US). Système de règlement de gros de la Réserve fédérale. Équivalent fonctionnel de TARGET2.

**ACH** (Automated Clearing House) (US). Rail de paiement de détail (équivalent fonctionnel de SEPA). Utilisé pour les salaires, les paiements récurrents, les transferts inter-banques aux US. Lent (1 à 3 jours), bon marché, peu utilisé en transfrontalier.

**CHIPS** (Clearing House Interbank Payments System) (US). Système privé de règlement de gros aux US, complémentaire de Fedwire.

**FedNow** (US). Système de paiement instantané des banques américaines, lancé en 2023, équivalent fonctionnel de SCT Inst. Adoption progressive.

**FPS** (Faster Payments Service) (UK). Paiement instantané au UK depuis 2008, antérieur à SCT Inst.

**RTGS** (Real-Time Gross Settlement) — terme générique désignant les systèmes de règlement brut en temps réel des banques centrales (TARGET, Fedwire, RTGS de la BoE, etc.).

## L’utilité opérationnelle

Le rail utilisé dit beaucoup de choses sur le flux :

- **SWIFT** = transfrontalier, gros montant typique, transit par correspondants (donc traces détaillées dans les MT).
- **SEPA SCT Inst** = euro, instantané, irréversible. Si vu en cascade, signal de layering rapide.
- **ACH** = US-domestique, lent, faible coût. Pas adapté à un layering rapide.
- **TARGET2 / Fedwire** = gros, institutionnel, peu visible aux particuliers.
- **FPS / FedNow** = équivalents nationaux instantanés.

Une fraude BEC moderne typique combine SCT Inst (pour la rapidité) puis transfert vers une PSP/EME, puis sortie cash ou crypto en moins de 6 heures. Le suivi exige une rapidité d’action (gel d’urgence) — voir chapitre 44.

## Méthode — lire un flux et identifier le rail

À partir d’un relevé bancaire, le rail utilisé apparaît :

- via la mention explicite (« SCT Inst », « SEPA », « SWIFT », etc.) ;
- via la **vitesse** (heure de débit chez l’émetteur ↔ heure de crédit chez le bénéficiaire) ;
- via le **format de la référence** (références SWIFT MT distinctives, MMSCT pour SEPA) ;
- via les **frais** appliqués (un SCT est gratuit ou à coût marginal ; un SWIFT international peut coûter 15 à 50 € côté donneur d’ordre, plus côté correspondant).

## Mini-walkthrough

Un dossier BEC : *« mardi 14h32, virement de 215 000 € depuis le compte d’une PME française vers un IBAN ES (Espagne) via SCT Inst. À 14h41, fractionné en 5 virements de 40 000 € à 45 000 € via SCT Inst vers 5 IBANs (3 au Portugal, 2 en Lituanie). À 16h12, l’ensemble converti en USDT sur un exchange via 5 dépôts. À 18h45, sortie depuis l’exchange vers un wallet auto-géré »*.

Lecture FININT : SCT Inst utilisé exclusivement (irréversibilité — fenêtre de gel quasi-nulle si la banque PME n’a pas réagi dans la minute), pattern de layering rapide multi-PSP, sortie crypto en moins de 4 heures. Le suivi du dossier exige : (a) immédiat contact avec la banque PME française et la banque espagnole pour gel, (b) saisine CRF française pour droit d’opposition, (c) ouverture d’un volet OSINT Crypto avec Sarah Marin pour le suivi blockchain.

## Erreurs fréquentes

- **Croire que SWIFT « contrôle » les paiements.** SWIFT est un réseau de messages ; il ne valide pas les paiements (les banques le font). Les sanctions SWIFT (déconnexion d’une banque) sont une exception à valeur politique forte (cas Iran, Russie partielle 2022).
- **Sous-estimer la vitesse du SCT Inst.** Les fraudes modernes l’exploitent. Le réflexe « j’ai 24h pour réagir » est dépassé.
- **Confondre les rails.** Un transfert intra-zone euro entre deux particuliers en SCT Inst n’a rien à voir avec un transfert SWIFT inter-correspondants : la lecture, les leviers de gel, et les coopérations diffèrent.

## Limites

L’analyse du rail ne dit rien sur la **légalité** du flux. Un SCT Inst de 200 000 € peut être un flux parfaitement légitime (achat immobilier, transaction commerciale) — c’est le contexte qui qualifie.

## Lien avec le fil rouge

> **CLEARFLOW — Cartographie des rails**
> 
> Nassim recense les rails utilisés dans les 17 DS : majorité de SWIFT MT103 (virements depuis Émirats vers France, comme attendu pour du commerce international), un nombre significatif de SCT Inst depuis des comptes en France vers des IBANs LT et EE (signal d’un layering rapide via fintechs européennes), et une trace de SCT classique vers un compte Suisse (banque privée). Cette cartographie oriente les coopérations à demander en priorité.

## Points clés à retenir

- SWIFT (international, MT103/MT202/MT940), SEPA (SCT, SCT Inst, SDD), TARGET2/Fedwire (gros), ACH (US-domestique), FPS/FedNow (instant nationaux).
- Le rail utilisé révèle la vitesse, la traçabilité et les leviers de gel disponibles.
- SCT Inst est aujourd’hui un canal privilégié des fraudes — avec une fenêtre de gel très étroite.
- ISO 20022 améliorera la richesse des données disponibles à l’analyse.

-----
