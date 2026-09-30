---
title: PARTIE II — LE SYSTÈME FINANCIER POUR L’ENQUÊTEUR
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
chapter: 3
chapters: 11
---

*Cinq chapitres pour comprendre l’infrastructure dans laquelle circule l’argent. Sans cette compréhension, l’analyste lit les flux comme on lit une langue étrangère.*

-----

## Chapitre 6 — Le système bancaire et la circulation de l’argent

### Objectif du chapitre

Comprendre l’**architecture institutionnelle** du système bancaire — banques de détail, banques d’investissement, banques privées, correspondent banks, banques centrales — et la manière dont l’argent circule entre ces acteurs. C’est le socle sans lequel les flux observables n’ont pas de sens.

### Le concept

Le système bancaire est organisé en **plusieurs strates**.

Les **banques commerciales de détail** sont l’interface du grand public et des entreprises : comptes courants, dépôts, crédits, moyens de paiement. En France : banques mutualistes (Crédit Agricole, Crédit Mutuel, BPCE), grands réseaux (BNP Paribas, Société Générale, Crédit du Nord), banques en ligne (Boursorama, Fortuneo). Au UK : Barclays, HSBC, NatWest, Lloyds. Aux US : JPMorgan Chase, Bank of America, Wells Fargo, Citibank.

Les **banques privées** (private banking) servent une clientèle aisée à très aisée (seuils variables, souvent 1 M€+ d’actifs). Elles cumulent gestion de patrimoine, conseil patrimonial, fiscalité internationale. En Suisse : UBS, Credit Suisse historiquement (absorbé par UBS en 2023), Pictet, Julius Baer, Lombard Odier. Au Luxembourg : Banque de Luxembourg, BIL. Une partie significative des dossiers FININT touchant à la fraude fiscale ou à la corruption transnationale impliquent des banques privées.

Les **banques d’investissement** opèrent sur les marchés financiers, financent les grandes entreprises, structurent les fusions-acquisitions, émettent les obligations souveraines. Goldman Sachs, Morgan Stanley, J.P. Morgan, Deutsche Bank, BNP Paribas CIB, Rothschild & Co.

Les **banques correspondantes** (correspondent banks) jouent un rôle clé : elles permettent à des banques sans présence directe dans une juridiction d’y opérer en passant par elles. Quasiment toutes les grandes banques occidentales offrent ce service. C’est par ces points de passage que transite la majorité du commerce international et des paiements transfrontaliers.

Les **banques centrales** (BCE, Fed, BoE, BNS) régulent la masse monétaire, fixent les taux directeurs et opèrent les systèmes de règlement de gros (TARGET2 en zone euro, Fedwire aux US). Pour l’analyste FININT, leur intérêt opérationnel est limité, sauf en supervision et statistiques.

Les **banques offshore** sont des établissements implantés dans des juridictions à fiscalité réduite et à secret bancaire historique (chapitre 10). Beaucoup ont des relations correspondantes avec les banques internationales.

### L’utilité opérationnelle

Lire un flux suspect, c’est lire un parcours dans cette architecture.

Exemple : *« virement de 850 000 € depuis HSBC Hong Kong vers Crédit Agricole Île-de-France, transitant par Deutsche Bank Frankfurt »*. L’analyste voit immédiatement :

- une banque correspondante européenne (Deutsche Bank) — point de contrôle AML majeur ;
- un trajet HK → DE → FR — atypique pour un flux purement européen, ce qui interroge sur l’origine ;
- le passage par une banque privée à Hong Kong — clientèle particulière, vérifications KYC supposément renforcées.

Cette lecture en quelques secondes oriente les questions à poser au coordinateur du dossier.

### Méthode — décoder un flux à partir des codes BIC/IBAN

Tout virement bancaire transite par des banques identifiables via leurs **codes BIC (Bank Identifier Code)** SWIFT et les comptes via leurs **IBAN (International Bank Account Number)**.

**BIC** : 8 ou 11 caractères, structuré ainsi `AAAA BB CC XXX` :

- 4 lettres : code banque (ex : `BNPA` pour BNP Paribas, `CHAS` pour JPMorgan Chase, `DEUT` pour Deutsche Bank).
- 2 lettres : code pays ISO (ex : `FR`, `DE`, `US`, `GB`, `CH`).
- 2 caractères : code lieu/ville (ex : `PP` pour Paris, `LL` pour Londres).
- 3 caractères optionnels : code agence ou département.

**IBAN** : longueur variable selon le pays, structuré `[Pays 2 lettres][Clé contrôle 2 chiffres][Identifiant national bancaire]`. En France, l’IBAN fait 27 caractères ; en Lituanie 20 ; au Luxembourg 20 ; en Suisse 21.

Pour l’analyste, l’IBAN livre :

- le **pays** (premier indice : un IBAN LT ou EE pour un résident français en BTP, sans lien évident, est un signal contextuel) ;
- le **code banque** (les 5 caractères suivant la clé en France pointent l’établissement) ;
- le **type d’établissement** par recoupement (banque traditionnelle vs PSP/EME — chapitre 8).

Outils gratuits utiles : annuaires SWIFT BIC publics (sites de banques centrales, services en ligne), validateurs IBAN, tables ISO 9362 et ISO 13616.

### Mini-walkthrough

Un flux typique dans un dossier de TBML : *« 4 virements, libellés “trade payment”, 75 000 € à 95 000 € chacun, depuis IBAN AE [Émirats] via BIC HSBC Dubaï, passant par BIC HSBC Londres comme correspondant, vers IBAN FR d’une SAS de négoce agricole »*.

Lecture : (1) Émirats → UK → France, trajet avec étapes correspondantes en ligne avec les usages du commerce ; (2) HSBC est à la fois banque émettrice et correspondant — concentration sur un acteur donnant une bonne traçabilité par recoupement ; (3) montants tous sous le seuil de 100 000 € — pourrait être de la structuration intentionnelle ou un ordre de grandeur typique du secteur ; (4) libellés vagues, à creuser. Cette lecture rapide oriente la suite de l’analyse.

### Erreurs fréquentes

- **Confondre un IBAN national « exotique » avec une fraude.** Beaucoup de fintechs européennes (Revolut, Wise) opèrent depuis la Lituanie ou l’Estonie pour des raisons réglementaires parfaitement légales. Un IBAN LT n’est pas suspect en soi.
- **Ignorer la distinction banque émettrice / banque réceptrice / banques correspondantes.** Une « banque » sur un virement n’est jamais évidente : il peut y avoir 2 à 4 banques impliquées dans la chaîne.
- **Lire le BIC sans vérifier le réseau de l’établissement.** Une grande marque sur une plaque ne garantit pas que la filiale locale ait le même standard de conformité que la maison mère.

### Limites

L’analyse des codes ne dit rien sur l’**activité** bancaire (motifs réels du flux). Elle dit qui a transité, pas pourquoi. Le « pourquoi » exige les libellés, les contreparties, les volumes et le contexte économique du compte.

### Lien avec le fil rouge

> **CLEARFLOW — Lecture rapide des chaînes**
> 
> Sur un échantillon de 60 virements entrants, Nassim repère que 80 % transitent par seulement 3 banques correspondantes : Deutsche Bank (Francfort), JPMorgan Chase (Londres), HSBC (Hong Kong). C’est un indice de structuration de la chaîne de paiement choisie par le réseau. Cela oriente les coopérations : un signalement à BaFin (DE) et à FCA (UK) pourrait éclairer les pratiques de KYC sur les flux concernés.

### Points clés à retenir

- Le système bancaire est multi-strates : détail, privée, investissement, correspondant, centrale, offshore.
- Les banques correspondantes sont un point de passage — et de contrôle AML — majeur.
- Les codes BIC et IBAN permettent une lecture rapide des chaînes de paiement.
- Cette lecture oriente, mais ne conclut pas.

-----

## Chapitre 7 — Rails de paiement : SWIFT, SEPA, TARGET2, Fedwire, ACH

### Objectif du chapitre

Connaître les **principaux rails de paiement** mondiaux, leurs caractéristiques techniques, leurs vitesses, leurs niveaux de surveillance, et la signification de leur usage dans un schéma observé.

### Le concept

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

### L’utilité opérationnelle

Le rail utilisé dit beaucoup de choses sur le flux :

- **SWIFT** = transfrontalier, gros montant typique, transit par correspondants (donc traces détaillées dans les MT).
- **SEPA SCT Inst** = euro, instantané, irréversible. Si vu en cascade, signal de layering rapide.
- **ACH** = US-domestique, lent, faible coût. Pas adapté à un layering rapide.
- **TARGET2 / Fedwire** = gros, institutionnel, peu visible aux particuliers.
- **FPS / FedNow** = équivalents nationaux instantanés.

Une fraude BEC moderne typique combine SCT Inst (pour la rapidité) puis transfert vers une PSP/EME, puis sortie cash ou crypto en moins de 6 heures. Le suivi exige une rapidité d’action (gel d’urgence) — voir chapitre 44.

### Méthode — lire un flux et identifier le rail

À partir d’un relevé bancaire, le rail utilisé apparaît :

- via la mention explicite (« SCT Inst », « SEPA », « SWIFT », etc.) ;
- via la **vitesse** (heure de débit chez l’émetteur ↔ heure de crédit chez le bénéficiaire) ;
- via le **format de la référence** (références SWIFT MT distinctives, MMSCT pour SEPA) ;
- via les **frais** appliqués (un SCT est gratuit ou à coût marginal ; un SWIFT international peut coûter 15 à 50 € côté donneur d’ordre, plus côté correspondant).

### Mini-walkthrough

Un dossier BEC : *« mardi 14h32, virement de 215 000 € depuis le compte d’une PME française vers un IBAN ES (Espagne) via SCT Inst. À 14h41, fractionné en 5 virements de 40 000 € à 45 000 € via SCT Inst vers 5 IBANs (3 au Portugal, 2 en Lituanie). À 16h12, l’ensemble converti en USDT sur un exchange via 5 dépôts. À 18h45, sortie depuis l’exchange vers un wallet auto-géré »*.

Lecture FININT : SCT Inst utilisé exclusivement (irréversibilité — fenêtre de gel quasi-nulle si la banque PME n’a pas réagi dans la minute), pattern de layering rapide multi-PSP, sortie crypto en moins de 4 heures. Le suivi du dossier exige : (a) immédiat contact avec la banque PME française et la banque espagnole pour gel, (b) saisine CRF française pour droit d’opposition, (c) ouverture d’un volet OSINT Crypto avec Sarah Marin pour le suivi blockchain.

### Erreurs fréquentes

- **Croire que SWIFT « contrôle » les paiements.** SWIFT est un réseau de messages ; il ne valide pas les paiements (les banques le font). Les sanctions SWIFT (déconnexion d’une banque) sont une exception à valeur politique forte (cas Iran, Russie partielle 2022).
- **Sous-estimer la vitesse du SCT Inst.** Les fraudes modernes l’exploitent. Le réflexe « j’ai 24h pour réagir » est dépassé.
- **Confondre les rails.** Un transfert intra-zone euro entre deux particuliers en SCT Inst n’a rien à voir avec un transfert SWIFT inter-correspondants : la lecture, les leviers de gel, et les coopérations diffèrent.

### Limites

L’analyse du rail ne dit rien sur la **légalité** du flux. Un SCT Inst de 200 000 € peut être un flux parfaitement légitime (achat immobilier, transaction commerciale) — c’est le contexte qui qualifie.

### Lien avec le fil rouge

> **CLEARFLOW — Cartographie des rails**
> 
> Nassim recense les rails utilisés dans les 17 DS : majorité de SWIFT MT103 (virements depuis Émirats vers France, comme attendu pour du commerce international), un nombre significatif de SCT Inst depuis des comptes en France vers des IBANs LT et EE (signal d’un layering rapide via fintechs européennes), et une trace de SCT classique vers un compte Suisse (banque privée). Cette cartographie oriente les coopérations à demander en priorité.

### Points clés à retenir

- SWIFT (international, MT103/MT202/MT940), SEPA (SCT, SCT Inst, SDD), TARGET2/Fedwire (gros), ACH (US-domestique), FPS/FedNow (instant nationaux).
- Le rail utilisé révèle la vitesse, la traçabilité et les leviers de gel disponibles.
- SCT Inst est aujourd’hui un canal privilégié des fraudes — avec une fenêtre de gel très étroite.
- ISO 20022 améliorera la richesse des données disponibles à l’analyse.

-----

## Chapitre 8 — PSP, EME, néobanques et fintechs

### Objectif du chapitre

Comprendre l’écosystème des **prestataires de services de paiement** (PSP), des **établissements de monnaie électronique** (EME), des **néobanques** et des **fintechs** : ce qu’ils sont, comment ils sont régulés, où ils se situent dans la chaîne de paiement, et pourquoi ils figurent souvent dans les schémas modernes de blanchiment et de fraude.

### Le concept

Le paysage est complexe et évolutif. Quelques distinctions clés.

Un **PSP** (Payment Service Provider) est un acteur agréé pour fournir des services de paiement (initiation, exécution, encaissement). Sa surface réglementaire est définie par la directive PSD2 (et bientôt PSR/PSD3). Tous les acteurs émettant des instruments de paiement ou opérant des comptes de paiement sont, à un titre ou un autre, PSP. Exemples : Stripe, Adyen, Worldline, PayPal, Mangopay, Lemon Way.

Un **EME** (Établissement de Monnaie Électronique) est agréé spécifiquement pour émettre de la monnaie électronique (e-money). Sa réglementation découle de la directive 2009/110/CE. Beaucoup de néobanques et fintechs sont juridiquement des EME plutôt que des banques. Exemples historiques : Revolut (initialement EME au UK puis banque), Wise (anciennement TransferWise — EME), Anytime, Qonto.

Une **néobanque** est une banque (ou EME ou hybride) opérant principalement en ligne, sans réseau d’agences physiques. Par abus de langage, le mot recouvre des statuts variés. N26 (banque allemande), Revolut (banque lituanienne pour ses comptes EU), Bunq (banque néerlandaise), Monzo et Starling (banques UK).

Une **fintech** est un terme générique qui désigne toute entreprise technologique opérant dans la finance — peut être un PSP, un EME, une néobanque, un agrégateur, un courtier, un assureur. Le terme n’a pas de portée réglementaire propre.

### L’utilité opérationnelle

Pourquoi ces acteurs concentrent l’attention FININT ?

**Onboarding rapide et 100 % digital.** Création de compte en quelques minutes via un smartphone, vérification d’identité automatisée. Cela permet à un fraudeur de créer rapidement plusieurs comptes (ou à un prête-nom de faciliter cela), beaucoup plus difficilement qu’avec une banque traditionnelle.

**Vitesse des opérations.** Virements instantanés intra-réseau (Revolut → Revolut), conversions multi-devises en un clic, virements internationaux à coût faible. Le **layering** se fait en heures, là où le circuit traditionnel prenait des jours.

**Effectifs compliance plus tendus.** Beaucoup de PSP/EME ont scalé leur base clients très rapidement et leurs équipes compliance moins. Conséquences observables : taux d’alerte traités en backlog, faux négatifs, parfois des sanctions ACPR/FCA/BaFin.

**IBANs « exotiques ».** Revolut (LT), Wise (BE/UK selon les comptes), N26 (DE), Bunq (NL), etc. La réglementation européenne facilite le passporting : une fintech agréée en Lituanie peut opérer dans toute l’UE. Un IBAN LT pour un résident français n’est pas suspect en soi (surtout depuis Revolut, Wise, etc.) — c’est l’absence de cohérence avec l’activité du compte qui peut l’être.

**Cartes prépayées.** Certaines fintechs émettent des cartes prépayées (rechargeables en ligne, parfois anonymes sous certains seuils dans certaines juridictions). Vecteur de placement et de cashout.

**Intégration native crypto.** Plusieurs fintechs proposent l’achat-vente de cryptos directement dans leur application (Revolut, Bitpanda en partenariat). Le passage fiat-crypto se fait sans changer d’environnement, ce qui complique la chaîne de surveillance (chapitre 48 et OSINT Crypto).

### Méthode — lire un flux fintech

Un flux passant par une fintech présente des spécificités :

1. **L’IBAN du compte fintech** est dans le pays de licence (LT pour Revolut, BE pour Wise, DE pour N26, NL pour Bunq). Le titulaire peut être résident dans n’importe quel pays UE (passporting).
1. **Les libellés sont parfois plus pauvres** que dans la banque traditionnelle, mais s’améliorent (depuis ISO 20022).
1. **Les transferts intra-réseau** (Revolut → Revolut, par username ou tag) ne laissent pas de trace SEPA visible aux contreparties extérieures — il faut une réquisition pour les obtenir.
1. **Les conversions multi-devises** apparaissent sur le relevé (par exemple : EUR → USD interne, puis virement USD).

L’analyste qui rencontre un flux passant par une fintech doit :

- Identifier précisément le statut juridique et l’agrément (banque, EME, PSP, et pays).
- Identifier l’autorité de supervision (ACPR pour France, BaFin pour Allemagne, Bank of Lithuania, FCA pour UK, Bank of Lithuania pour la majorité des comptes Revolut européens, etc.).
- Pour les sollicitations bancaires (réquisitions, droits de communication), passer par le canal compétent (banque licence-holder).

### Mini-walkthrough

Un cas BEC : *« 215 000 € transitent depuis une PME française par 4 comptes Revolut (LT) → Wise (BE) → N26 (DE) → Bunq (NL) en 2 heures, avant conversion crypto »*.

Lecture FININT :

- Layering rapide multi-fintech, profil typique des fraudes BEC modernes.
- Quatre juridictions de licence, donc quatre coopérations potentielles avec les autorités locales (Banque de Lituanie, Banque nationale de Belgique, BaFin, DNB).
- Dans la pratique opérationnelle : la coopération via les autorités prend du temps. La réactivité passe par la **CRF** qui peut activer des canaux plus directs avec les compliance des fintechs concernées (FIU.NET en EU).
- Renvoi crypto pour la suite : vers Sarah Marin / OSINT Crypto.

### Erreurs fréquentes

- **Considérer toutes les fintechs comme « suspectes ».** Elles sont des outils financiers majeurs et largement légitimes. Le profil de risque dépend de l’usage par l’utilisateur, pas de la marque.
- **Ne pas distinguer banque / EME / PSP.** Cela change le cadre réglementaire et la liste des autorités à solliciter.
- **Croire qu’un IBAN LT/EE/BE est nécessairement « offshore ».** Ces IBANs sont européens et soumis à la réglementation UE complète.
- **Sous-estimer la richesse des données fintech.** Les fintechs ont souvent des **logs très détaillés** (géolocalisation des sessions, device fingerprinting, IP) — exploités sur réquisition, ils sont parfois plus utiles que les relevés bancaires classiques.

### Limites

La supervision peut varier en maturité d’une autorité nationale à l’autre. La **réactivité** dans la coopération aussi. L’analyste qui dépend de la coopération transfrontalière entre fintechs note les délais réels (parfois des semaines pour des demandes pourtant urgentes).

### Lien avec le fil rouge

> **CLEARFLOW — Branche fintech**
> 
> Plusieurs flux du dossier Haddad transitent par des comptes Wise (au nom d’une société chypriote, IBAN BE). Nassim demande à la CRF de solliciter — via FIU.NET — les KYB associés (qui contrôle le compte ?), les logs de session (depuis où sont effectuées les opérations ?), et les patterns de transferts intra-Wise qui ne seraient pas visibles sur les relevés bancaires classiques. La réponse arrive en 11 jours — ce qui, pour une coopération européenne, est un délai correct.

### Points clés à retenir

- PSP / EME / néobanque / fintech : termes recouvrant des statuts juridiques variés.
- L’écosystème est largement légitime ; l’attention FININT cible des **usages** spécifiques.
- Layering rapide, IBAN passportés, intégration crypto, cartes prépayées : facteurs typiques.
- La coopération exige d’identifier l’autorité de supervision compétente et le bon canal d’instruction.

-----

## Chapitre 9 — Comptes bancaires, relevés et opérations

### Objectif du chapitre

Comprendre les **différents types de comptes**, la structure d’un **relevé bancaire**, et la grammaire des opérations courantes — pour savoir lire un relevé et y reconnaître l’anormal.

### Le concept

**Types de comptes (vue analyste).**

- **Compte courant / compte de paiement** — usage quotidien, encaissements, virements, dépenses. Le compte « visible » d’un particulier ou d’une entreprise.
- **Compte d’épargne** (Livret A, LDDS, livrets bancaires, etc.) — dépôts rémunérés, plafonds, fiscalité spécifique en France.
- **Compte à terme / compte de dépôt à terme** — sommes immobilisées sur une durée, rémunération supérieure.
- **Compte titres / portefeuille** — détention d’instruments financiers (actions, obligations, OPCVM, ETF).
- **Compte sur livret de société** — pour entreprises, plus rare.
- **Compte de séquestre / escrow** — fonds bloqués au profit d’un tiers (notaire, avocat).
- **Compte de paiement chez une fintech / EME** — fonctionnellement proche d’un compte courant, mais juridiquement distinct.
- **Compte de cantonnement** — pour certains professionnels (avocats, agents immobiliers, agents de change), fonds reçus pour le compte de tiers.
- **Compte client / compte tiers** — fonds détenus par un professionnel pour ses clients.

**Structure d’un relevé bancaire (lecture FININT).**

Un relevé moderne contient typiquement, par ligne d’opération :

- **Date de l’opération** (date où l’opération est passée).
- **Date de valeur** (date à laquelle l’opération est prise en compte pour le calcul d’intérêts).
- **Libellé** — texte plus ou moins riche : référence SEPA, nom du donneur ou bénéficiaire, motif éventuel, référence interne.
- **Montant** (débit ou crédit, devise).
- **Solde après opération** (parfois).
- **Référence interne** — souvent utile pour relier les opérations.

Pour un compte d’entreprise, le relevé peut être enrichi : code analytique, journal comptable, rapprochement automatique.

**Grammaire des opérations courantes.**

- **Virement émis / reçu** (SEPA, SWIFT, instantané) — la trace la plus courante.
- **Prélèvement** (SDD) — paiement récurrent avec mandat (loyers, factures).
- **Carte bancaire — débit / paiement / retrait** — paiements en ligne ou physiques, retraits espèces.
- **Dépôt / versement d’espèces** — en agence, en automate.
- **Retrait d’espèces** — au DAB ou en agence.
- **Chèque — émis / reçu / encaissé / rejeté** — en déclin en Europe, encore courant en certains secteurs.
- **Effets de commerce / LCR / BOR** — papiers commerciaux entre entreprises.
- **Frais bancaires** — nombreux, souvent peu lus mais analytiquement utiles (un fort volume de frais sur découvert peut être signal de difficulté ; un volume anormalement élevé de frais SWIFT peut signaler une activité de transit).
- **Intérêts / agios** — produits ou charges financières.
- **Achats-ventes de titres** sur compte titre.

### L’utilité opérationnelle

Le relevé est la **matière première** de l’analyse de flux. L’analyste le lit en plusieurs passes :

1. **Vue panoramique** — structure globale : combien d’opérations / mois ? combien d’entrées ? sorties ? quel est le solde moyen ? quel est le pic ?
1. **Vue temporelle** — distribution des opérations dans le temps : pics d’activité ? saisonnalité ? périodes de creux ?
1. **Vue par contreparties** — top 20 des contreparties émettrices, top 20 des bénéficiaires : qui paie qui, combien, sur quelle période ?
1. **Vue par type d’opération** — répartition virements / cartes / espèces / chèques.
1. **Vue par libellés** — détection de patterns dans les libellés (mots clés récurrents, formats répétitifs).
1. **Vue par cohérence économique** — les flux sont-ils compatibles avec l’activité déclarée (secteur, taille, géographie) ?

À chaque passe, l’analyste note les **anomalies** : montants ronds inhabituels, structuration sous des seuils, libellés vagues, contreparties géographiquement incohérentes, soldes nuls répétés (compte de transit), pics non expliqués.

### Méthode — la lecture en 6 passes

Pour un relevé d’1 an d’opérations sur un compte courant typique (1 000 à 5 000 lignes) :

**Passe 1 — Profilage** (15 min). Statistiques globales. Outils : tableur ou pandas.

```
Période : 12 mois
Lignes : 3 247
Crédits : 1 421 — 4,2 M€
Débits : 1 826 — 4,1 M€
Solde moyen : 87 K€
Solde max : 542 K€ (pic le 18/03)
Nombre de contreparties uniques : 187
Top 5 émetteurs : 73 % du volume entrant
Top 5 bénéficiaires : 51 % du volume sortant
```

**Passe 2 — Concentrations**. Les top contreparties représentent quoi ? Sont-elles cohérentes avec l’activité ?

**Passe 3 — Anomalies temporelles**. Pics, creux, ruptures (changement de comportement).

**Passe 4 — Anomalies de contreparties**. Pays inhabituels, contreparties inconnues, contreparties créées récemment.

**Passe 5 — Libellés**. Mots clés vagues (« services », « paiement », « avance », « régularisation »), libellés répétés à l’identique, libellés contradictoires.

**Passe 6 — Cohérence économique**. Recoupement avec l’activité déclarée : pour une SAS de négoce, attendre des achats matières + ventes clients ; les virements perso massifs depuis le compte société sont anormaux (ABS — chapitre 43).

### Mini-walkthrough

Un compte personnel d’un dirigeant français, secteur « consultant indépendant », revenus déclarés 80 K€/an :

- 87 % des entrées sur 6 mois proviennent de 2 sociétés étrangères (CY et AE) que l’OSINT identifie comme contrôlées par le même groupe ;
- Les libellés sont uniformément « consulting fees » ;
- Les sorties incluent : 240 K€ vers une SCI Paris (achat immobilier), 95 K€ vers un compte personnel suisse, dépôt récurrent de 8 500 € à 14 000 € en espèces (10 dépôts en 6 mois) ;
- Aucun frais professionnel apparent (pas de loyer bureau, pas de cotisations sociales pro, pas d’achat matériel).

Lecture FININT initiale : profil compatible avec **(H1)** prestation de conseil légitime mais à clientèle restreinte hors France ; **(H2)** rétrocommissions ou facturation de complaisance ; **(H3)** prête-nom pour le compte d’un tiers. Niveau de confiance : impossible à trancher sur les seules données du relevé. Sollicitations recommandées : coopération avec les CRF chypriote et émiratie pour qualifier les contreparties, OSINT sur l’activité réelle du « consultant », réquisition des libellés détaillés des dépôts cash si possible.

### Erreurs fréquentes

- **Lire un relevé ligne à ligne sans vue panoramique préalable.** L’analyste se noie dans les détails et passe à côté du schéma.
- **Ignorer les frais bancaires.** Ils racontent une histoire (volume d’opérations, opérations rejetées, découverts).
- **Ne pas faire le rapprochement avec l’activité économique réelle** — un relevé bancaire ne se lit qu’avec le contexte du compte.

### Limites

Le relevé bancaire est un point de vue **partiel** sur les flux d’une personne ou d’une entreprise. Une personne peut avoir 3 comptes dans 2 banques différentes ; une entreprise peut opérer via 5 comptes dans 4 juridictions. Une analyse complète exige la consolidation, qui est rarement possible sans réquisitions (FICOBA en France pour identifier les comptes ouverts par une personne).

### Lien avec le fil rouge

> **CLEARFLOW — Premier relevé Haddad**
> 
> Nassim obtient, via les DS, un échantillon des relevés des comptes français de Haddad. Sur 18 mois : 1 421 lignes, 4,2 M€ de crédits totaux, 87 % concentrés sur 4 contreparties étrangères (Chypre, Émirats, Turquie, Suisse). Libellés à 75 % vagues (« services », « commercial », « avance »). Ratio comptes pro / perso anormal : 60 % des dépenses du compte société sont des transferts vers des comptes perso ou des entités liées. Le relevé seul ne prouve rien. Il pose le décor.

### Points clés à retenir

- Relevé = matière première, lecture en 6 passes (profilage, concentrations, temps, contreparties, libellés, cohérence).
- Le relevé est partiel ; le FICOBA (et équivalents) permet de consolider.
- Les frais bancaires et les libellés sont des indices souvent négligés.
- Le relevé seul ne tranche pas — il oriente, en attendant le recoupement.

-----

## Chapitre 10 — Offshore, secret bancaire et juridictions opaques

### Objectif du chapitre

Comprendre ce qu’est l’**offshore**, comment fonctionne le **secret bancaire**, quelles sont les **juridictions opaques** clés, et comment l’analyste FININT compose avec ces obstacles structurels.

### Le concept

**Offshore.** Un terme imprécis qui désigne, dans le langage courant, les juridictions à fiscalité réduite et à régulation faible utilisées pour héberger des structures (sociétés, trusts, fondations) ou des comptes bancaires. Les analystes professionnels préfèrent le terme **« juridictions à risque »** ou **« juridictions à transparence limitée »** car il est plus précis et moins polémique.

**Secret bancaire.** Obligation légale faite aux banques de ne pas révéler à des tiers les informations sur leurs clients. Tous les pays ont une forme de secret bancaire, mais certaines juridictions l’ont historiquement renforcé au point d’en faire un argument commercial (Suisse, Liechtenstein, Luxembourg, Singapour, Hong Kong). Sous la pression internationale (GAFI, EAR/CRS, FATCA), le secret bancaire a perdu une grande partie de sa portée vis-à-vis des autorités fiscales étrangères, mais il reste opposable aux particuliers et à de nombreux acteurs privés.

**EAR/CRS** (Échange Automatique de Renseignements / Common Reporting Standard, OCDE). Mécanisme par lequel les juridictions adhérentes échangent automatiquement les informations sur les comptes bancaires détenus par des non-résidents. Plus de 100 juridictions adhérentes en 2025. La Suisse, le Liechtenstein, Singapour, Hong Kong, le Luxembourg, les BVI, les Cayman, sont parties au CRS. Les **non-adhérents** notables incluent les États-Unis (qui ont leur propre système, FATCA, asymétrique). En CRF, les données EAR/CRS reçues et envoyées sont une source primordiale.

**FATCA** (Foreign Account Tax Compliance Act, US). Obligation faite aux institutions financières étrangères de déclarer aux US les comptes détenus par des contribuables américains. Asymétrique (les US ne livrent pas l’équivalent en sortie).

**Listes GAFI.**

- **Liste noire** (« High-Risk Jurisdictions subject to a Call for Action »). Juridictions présentant des défaillances stratégiques en matière de LCB-FT. La liste évolue ; un analyste consulte le site officiel du GAFI au moment de l’analyse.
- **Liste grise** (« Jurisdictions under Increased Monitoring »). Juridictions sous surveillance renforcée mais coopérantes. La liste évolue plusieurs fois par an. Pour une donnée actuelle, consulter le site officiel du GAFI (fatf-gafi.org).

**Listes UE.** L’UE publie sa propre liste de juridictions tierces non coopératives à des fins fiscales. Liste mise à jour régulièrement, à consulter sur EUR-Lex et le site du Conseil.

### L’utilité opérationnelle

Pour l’analyste, ces concepts servent à :

- **Qualifier le risque** d’un flux sortant ou entrant (juridiction du compte / pays de résidence du titulaire / activité du compte).
- **Calibrer la coopération** attendue (un EAR/CRS facilite ; un pays sur liste grise complique ; un pays sur liste noire ferme presque toutes les portes).
- **Anticiper les délais** de toute coopération internationale.
- **Identifier les secteurs vulnérables** (les juridictions à secret bancaire fort sont souvent des destinations finales de blanchiment).

### Méthode — qualifier rapidement une juridiction

Pour toute juridiction inhabituelle apparaissant dans un dossier, l’analyste répond rapidement à :

1. **Statut GAFI** — pays sur liste noire, grise, ou hors liste ?
1. **Statut UE** — pays sur la liste UE des juridictions non coopératives ?
1. **Adhésion EAR/CRS** — oui / non ?
1. **Coopération via Egmont** — la CRF locale est-elle membre d’Egmont ? Active ?
1. **Type de structures fréquentes** — sociétés ? trusts ? fondations ? IBC (International Business Company) ? exemptes de fiscalité ? exemptes de comptes annuels publiés ?
1. **Registre des bénéficiaires effectifs** — existe-t-il ? est-il accessible ?

Outils gratuits : site GAFI, base UE, CRS country status (OCDE), Tax Justice Network (Financial Secrecy Index — académique, point de référence).

### Mini-walkthrough — quelques juridictions emblématiques

**Suisse.** Place financière historique. Membre Egmont actif. Adhérente CRS (depuis 2017). Le secret bancaire absolu vis-à-vis des autorités fiscales étrangères a été levé pour les pays partenaires CRS. Reste opposable au public et à de nombreuses procédures civiles. Coopération via FINMA et MROS (la CRF suisse).

**Luxembourg.** Place financière européenne majeure. Membre UE et Egmont. Adhérente CRS. Coopération possible et structurée via la CRF luxembourgeoise. Mais la **densité de holdings, SOPARFI, fonds, et structures de gestion d’actifs** rend l’identification opérationnelle parfois lourde.

**Chypre.** Membre UE et Egmont. Adhérente CRS. Coopération via Mokas (CRF chypriote). Densité de sociétés détenues par des non-résidents (notamment liées à des intérêts russes pré-2022, libanais, turcs). Réformes post-2018 sous pression EU. Point d’attention pour les schémas d’opacification européens.

**Émirats arabes unis (EAU).** Place financière en croissance, hub commercial régional. Membre Egmont. Adhérente CRS. Sur liste grise GAFI 2022 (sortie en 2024 — vérifier la liste actuelle au moment de l’analyse). Coopération possible mais variable selon les émirats (Dubai vs Abu Dhabi vs autres). Free zones (Jebel Ali, DMCC, ADGM, DIFC) avec régimes spécifiques.

**British Virgin Islands (BVI).** Juridiction britannique d’outre-mer. Adhérente CRS. Densité historique d’IBC. Registre des bénéficiaires effectifs introduit progressivement (BOSS — Beneficial Ownership Secure Search), accessible aux autorités sous conditions.

**Cayman Islands.** Similaire BVI sur de nombreux aspects. Hub majeur des fonds d’investissement.

**Panama.** Juridiction historique des sociétés anonymes. Réputation lourdement atteinte par les Panama Papers (2016) et Pandora Papers (2021). Coopération améliorée mais inégale.

**Liechtenstein.** Petite juridiction, historiquement associée aux fondations privées (Stiftung) — véhicules de protection patrimoniale très opaques. Membre Egmont, adhérent CRS.

**Singapour, Hong Kong.** Centres financiers asiatiques. Adhérents CRS. Coopération possible mais avec des inflexions politiques notables (notamment HK depuis 2020).

**Delaware (US).** Sans être offshore au sens géographique, Delaware (et certains autres États US comme le Wyoming, le Nevada) propose des structures (LLC) à transparence très limitée — registre PSC limité, pas d’EAR/CRS sortant équivalent (FATCA asymétrique). C’est un point d’attention sous-estimé.

### Erreurs fréquentes

- **Considérer toute juridiction non européenne comme « offshore ».** La nuance est essentielle.
- **Croire que CRS résout tout.** CRS échange des données fiscales entre administrations. Il ne les rend pas accessibles aux particuliers ni à toute autorité.
- **Sous-estimer Delaware / Nevada / Wyoming.** Une part significative des structures à risque dans les dossiers transatlantiques transitent par ces États US.
- **Ignorer le free zone factor.** Les free zones (Jebel Ali, DIFC, ADGM, etc.) ont des régimes fiscaux et réglementaires propres — distincts de la juridiction « parent ».

### Limites

Les listes GAFI et UE évoluent. La liste précise à un instant donné doit être vérifiée à la source (sites officiels). Une juridiction sortie de la liste grise reste un facteur de risque pertinent dans une analyse — la sortie ne vaut pas absolution.

### Lien avec le fil rouge

> **CLEARFLOW — Cartographie offshore**
> 
> Le dossier Haddad implique au moins 5 juridictions non-françaises : Chypre (UE, structurelle), Émirats (commerce + free zone), Bénin (intermédiaire), Suisse (banque privée), Liban (origine, suspicion d’infraction prédécesseur). Nassim qualifie chaque juridiction (statut GAFI/UE, EAR/CRS, Egmont) et anticipe les délais de coopération. Dès le cadrage, il prévoit que les éléments chypriotes seront accessibles en 2 à 4 semaines via Egmont, les émiratis en 4 à 8 semaines, les libanais à très long terme et avec un haut degré d’incertitude.

### Points clés à retenir

- « Offshore » est imprécis ; préférer « juridiction à risque » et qualifier précisément.
- EAR/CRS, GAFI, listes UE structurent la qualification.
- Le secret bancaire moderne s’est érodé vis-à-vis des fiscs ; il reste fort vis-à-vis des particuliers et de nombreuses procédures civiles.
- Delaware / Nevada / Wyoming sont des points d’attention transatlantiques sous-estimés.

-----
