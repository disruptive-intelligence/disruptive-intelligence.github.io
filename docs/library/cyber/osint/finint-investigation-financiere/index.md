---
title: FININT — investigation financière
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
---

*Suivre l’argent dans l’économie réelle — Registres, sociétés, bénéficiaires effectifs, flux bancaires, criminalité financière et asset recovery*

**Cours complet — 10 parties • 70 chapitres + 1 chapitre 0 de mise à niveau • 14 annexes • 1 parcours express • 1 fil rouge • 3 parcours de lecture**

*Renseignement financier • OSINT financier • LCB-FT • Analyse de flux • Comptabilité forensique • Coopération internationale • Asset recovery*

-----

## Avant-propos

### À qui s’adresse ce cours

Ce cours est destiné à toute personne qui doit, dans son activité professionnelle ou en formation avancée, **comprendre et pratiquer le renseignement financier** : analystes en cellule de renseignement financier (CRF), enquêteurs financiers, analystes compliance et LCB-FT, auditeurs forensiques, journalistes d’investigation, analystes OSINT financiers, profils GRC, professionnels du contentieux fiscal et douanier, équipes de threat intelligence amenées à croiser cyber et finance, et plus largement toute personne en charge de qualifier des soupçons, de cartographier des structures économiques opaques ou de tracer des avoirs.

Ce cours **ne suppose aucune spécialisation préalable** en LCB-FT, en investigation financière, en comptabilité, en droit financier ou en économie. Il commence par un **chapitre 0 de mise à niveau** permettant à un lecteur débutant d’acquérir les repères essentiels (entreprise, flux financiers, documents, comptabilité minimale, acteurs d’un dossier, notions juridiques, types de sources) avant d’aborder les méthodes FININT. La progression est introductive dans son rythme et professionnelle dans sa profondeur : un débutant peut le suivre dans l’ordre, un praticien peut y revenir comme référence par chapitre.

### Ce que ce cours est — et ce qu’il n’est pas

Ce cours **est** : un manuel d’enquête, méthodologique, opérationnel, calibré pour une pratique réelle. Il fournit des modèles de fiches, des matrices, des checklists, des walkthroughs, des templates, des cas pratiques déroulés et des cas historiques exploités comme leçons. Il distingue systématiquement ce qui est observable, ce qui est inféré, ce qui est probable, ce qui est indémontrable et ce qui nécessite une autorité compétente. Il calibre la confiance par une échelle inspirée des Words of Estimative Probability et il apprend à écrire avec rigueur — *« compatible avec »*, *« cohérent avec »*, *« hypothèse calibrée »*, plutôt qu’affirmations péremptoires.

Ce cours **n’est pas** : un manuel pour commettre une infraction, un guide pour échapper à la traçabilité, un cours de comptabilité générale, un précis de droit pénal des affaires, un manuel de l’enquête judiciaire ou un catalogue d’outils. Il ne refait pas l’enquête blockchain (renvoi systématique au cours OSINT Crypto pour le volet on-chain), ni l’OSINT général (renvoi aux cours OSINT correspondants).

### Posture éthique et déontologique

Le FININT est une discipline qui touche aux libertés individuelles, au secret bancaire, à la vie privée, à la réputation et, dans certains cas, à la liberté de personnes. Une note d’analyse mal calibrée, un soupçon pris pour une preuve, une diffusion non maîtrisée, une confusion entre renseignement et accusation peuvent causer des dommages réels — y compris à des personnes innocentes ou non concernées. La rigueur méthodologique n’est pas un luxe académique : elle est la condition même de la légitimité de la discipline. Tout au long du cours, cette rigueur est présentée comme un réflexe, pas comme un appendice.

Le cours adopte une posture **strictement défensive, analytique, conformité et investigative**. Lorsqu’une typologie criminelle est expliquée, c’est sous l’angle de la compréhension, de la détection, de l’investigation, de la prévention, du signalement et de la coopération. Aucune section ne fournit de méthode pour blanchir, frauder ou échapper aux contrôles.

### Cohérence avec le reste du corpus

Ce cours est complémentaire d’un **cours OSINT Crypto** dédié à l’enquête on-chain (blockchains, wallets, mixers, bridges, DEX, privacy coins, cashout crypto). Quand un dossier comporte une branche crypto, le cours FININT cadre le contexte financier (KYB de l’exchange, mules, BEC, sociétés écrans, conformité du VASP) et **renvoie explicitement** vers OSINT Crypto pour le traçage on-chain détaillé. Cette séparation est volontaire : refaire le traçage blockchain ici diluerait la spécificité FININT.

Des renvois ponctuels existent également vers d’autres cours du corpus quand pertinent (OSINT général, CTI, GRC, Dark Web).

### Mode d’emploi du cours

- **Lecture linéaire** : la progression Partie I → X est conçue pour un apprentissage cumulatif. Les notions des Parties I et II sont mobilisées dans les suivantes.
- **Lecture par référence** : chaque chapitre est autonome ; l’index, la table des matières et le glossaire (annexe A) permettent un usage à la demande.
- **Parcours express** : pour produire une **première fiche FININT en 45 minutes** à partir d’un simple nom de société ou de personne — utile en formation initiale, en sollicitation urgente, ou en exercice d’auto-évaluation.
- **Fil rouge CLEARFLOW** : un cas fictif, réaliste, qui traverse l’ensemble du cours sous forme d’encadrés courts, et qui est synthétisé au chapitre 64.
- **Annexes opérationnelles** : 14 annexes prêtes à copier dans un dossier d’enquête (fiches, matrices, glossaire, modèle de note, registres par pays, outils par usage, cadres d’accès aux sources, bibliographie de sources primaires).

### Conventions de notation

Plusieurs conventions sont utilisées tout au long du cours :

- **Encadré CLEARFLOW** : illustration du chapitre courant via le fil rouge.
- **Méthode** : procédure étape par étape.
- **Erreurs fréquentes** : pièges identifiés, à éviter en pratique.
- **Limites** : ce que la méthode ne permet pas, ou seulement sous condition.
- **Renvoi** : pointeur vers un autre chapitre, une annexe ou un autre cours.
- **WEP** : niveau de confiance (échelle Words of Estimative Probability — chapitre 33).
- **Quasi-certain / Très probable / Probable / Possible / Peu probable / Très peu probable / Indéterminable** : niveaux WEP utilisés en pratique.

### Actualité

Le cours est calibré pour la période **2025-2026** : paquet AML européen et création de l’AMLA, transposition LCB-FT, MiCA et Travel Rule (uniquement quand elles croisent les crypto-actifs), évolutions GAFI, pratiques TRACFIN, sanctions OFAC/UE/ONU, accès aux registres UBO post-arrêt CJUE 2022, fraudes BEC modernes, néobanques, fintechs, stablecoins comme rail de blanchiment. Lorsqu’une donnée est susceptible d’évoluer rapidement, le cours le signale et oriente vers la source primaire.

-----

## Chapitre 0 — Mise à niveau

les bases économiques, juridiques et financières indispensables

### Objectif du chapitre

Donner à un lecteur débutant les bases nécessaires pour suivre le cours sans se sentir perdu. Ce chapitre ne transforme pas le lecteur en juriste, en comptable ou en banquier — il fournit les **repères indispensables** pour comprendre les chapitres FININT qui suivent. Un lecteur déjà familier de l’environnement économique, juridique et financier peut survoler ce chapitre ; un débutant y prend une heure ou deux pour s’installer dans le vocabulaire et les concepts.

-----

### 0.1 — Comprendre ce qu’est une entreprise

#### Personne physique et personne morale

Une **personne physique** est un être humain. Elle a un nom, une date de naissance, une nationalité, une adresse. Elle peut posséder des biens, signer des contrats, ouvrir un compte bancaire, et être tenue responsable de ses actes.

Une **personne morale** est une **entité juridique** créée par le droit. Elle n’a pas de corps physique mais elle est traitée par le droit comme un sujet de droits et d’obligations. Une société, une association, une fondation sont des personnes morales. Elles peuvent, comme les personnes physiques, posséder des biens, ouvrir un compte bancaire, signer des contrats, recevoir des paiements, et être poursuivies en justice.

> **À retenir** : derrière toute société, il y a des personnes physiques (dirigeants, associés, bénéficiaires effectifs). L’enquête FININT cherche souvent à comprendre **qui contrôle réellement cette personne morale**.

#### Les formes courantes d’entités

- **Société** : entité créée pour exercer une activité économique, généralement à but lucratif (SAS, SARL, SA, Ltd, GmbH, LLC, etc. — détaillé chapitre 21).
- **Association** : entité à but non lucratif. En France, association loi 1901.
- **Fondation** : entité dotée d’un patrimoine affecté à un but d’intérêt général ou privé (fondations Liechtenstein, Panama, etc. — chapitre 25).
- **Trust** : relation juridique de droit anglo-saxon où une personne (trustee) détient et gère des biens pour le compte d’autres personnes (bénéficiaires). Le trust **n’est pas** une entité juridique distincte au sens continental, mais il est traité par l’enquête FININT comme un acteur (chapitre 25).

#### Siège, établissement, filiale, holding

- **Siège social** : adresse officielle déclarée d’une société. Lieu juridique.
- **Établissement** : lieu physique où s’exerce une activité. Une société peut avoir plusieurs établissements (établissements secondaires).
- **Filiale** : société contrôlée par une autre société (la société mère).
- **Holding** : société dont l’activité principale est de détenir des participations dans d’autres sociétés (filiales). Pas (ou peu) d’activité opérationnelle propre.

#### Dirigeant, actionnaire, associé, mandataire

- **Dirigeant** : personne qui dirige la société (président, gérant, directeur général). Désigné selon la forme juridique.
- **Actionnaire** ou **associé** : personne (physique ou morale) qui détient le capital de la société. Un associé d’une SARL ou SAS, un actionnaire d’une SA.
- **Mandataire** : toute personne qui exerce un mandat dans la société (dirigeants, administrateurs, commissaires aux comptes, etc.).

#### Trois grandes catégories d’entités vues du FININT

- **Société opérationnelle** : exerce une activité économique réelle (vente de biens, prestation de services). Elle a des clients, des fournisseurs, des salariés, des locaux, du chiffre d’affaires.
- **Société holding** : détient des participations. Souvent peu ou pas d’activité propre, mais cela peut être légitime (gouvernance, optimisation, structuration).
- **Société écran** : entité juridique sans activité économique réelle propre, créée pour porter une finalité spécifique sans substance opérationnelle (chapitre 26). Peut être légitime (SPV, holding patrimonial) ou suspecte (transit financier, opacification).

> **Exemple simple** : une société est une personne morale. Elle peut avoir un compte bancaire, signer des contrats, acheter un bien immobilier, recevoir des paiements, et être poursuivie en justice. L’enquête FININT cherche souvent à comprendre **qui contrôle réellement** cette personne morale, et **dans quel but**.

-----

### 0.2 — Comprendre les flux financiers

#### Compte bancaire

Un **compte bancaire** est un compte ouvert au nom d’une personne (physique ou morale) auprès d’une banque ou d’un PSP. Il enregistre des **opérations** : crédits (entrées d’argent) et débits (sorties).

- **Solde** : montant disponible sur le compte à une date donnée.
- **Devise** : monnaie du compte (EUR, USD, GBP, CHF, JPY, etc.). Un même titulaire peut avoir des comptes en plusieurs devises.

#### Virement

Un **virement** est un transfert d’argent d’un compte vers un autre.

- **Donneur d’ordre** : celui qui ordonne le virement (le titulaire du compte débité).
- **Bénéficiaire** : celui qui reçoit (le titulaire du compte crédité).
- **Banque émettrice** : banque qui exécute l’ordre du donneur.
- **Banque réceptrice** : banque qui crédite le bénéficiaire.
- **Libellé** : texte associé au virement (ex. « paiement facture XXX », « salaire octobre », « prêt »). Le libellé est déclaré par le donneur d’ordre, il n’est pas vérifié par la banque.

#### IBAN et BIC

- **IBAN (International Bank Account Number)** : identifiant standardisé d’un compte bancaire. Commence par le code pays sur 2 lettres (FR pour France, ES pour Espagne, GB pour UK, etc.), suivi de chiffres et lettres. Exemple : `FR76 1234 5678 9012 3456 7890 123`.
- **BIC (Bank Identifier Code)** : identifiant SWIFT d’une banque (ex. `BNPAFRPP` pour BNP Paribas France).

#### Paiement national, européen, international

- **Paiement national** : entre deux comptes français. Rapide, peu cher.
- **Paiement européen — SEPA** : entre deux comptes de la zone SEPA (36 pays). Standard européen. Existe en version classique (SCT) et instantanée (SCT Inst, qui crédite le bénéficiaire en quelques secondes mais est irréversible).
- **Paiement international — SWIFT** : entre deux comptes dans des pays différents (notamment hors SEPA). Passe par des **banques correspondantes** qui relaient le paiement. Plus long, plus cher, plus complexe.

> **Exemple FININT** : si une société française reçoit 95 000 € depuis Dubaï avec le libellé « commercial services », l’analyste **ne conclut pas** que c’est suspect. Il se demande : qui paie ? pourquoi ? pour quelle prestation ? est-ce cohérent avec l’activité déclarée de la société ? Quel est le donneur d’ordre réel derrière le compte émetteur ? Cette discipline d’interrogation, sans jugement immédiat, est l’esprit du FININT.

-----

### 0.3 — Comprendre les documents de base

Voici les documents qu’un analyste FININT rencontre régulièrement, et leur rôle :

- **Extrait de registre d’entreprise** (Kbis en France, Companies House extract au UK, etc.) : document officiel attestant de l’existence d’une société, indiquant sa dénomination, son siège, sa forme juridique, ses dirigeants, sa date de création. C’est la « pièce d’identité » de la société.
- **Statuts** : document fondateur d’une société. Définit son objet social, sa gouvernance, le pouvoir de ses dirigeants, les règles de cession des parts, etc.
- **Facture** : document émis par un vendeur ou prestataire, demandant paiement à un client. Détaille la prestation, la quantité, le prix, la TVA, l’échéance.
- **Contrat** : document liant deux ou plusieurs parties par des obligations réciproques (vente, prestation de services, prêt, location, etc.).
- **Relevé bancaire** : document récapitulant les opérations d’un compte sur une période (mois, trimestre, année). Émis par la banque.
- **Bilan** : photographie du patrimoine de la société à une date (actif = ce qu’elle possède, passif = ce qu’elle doit).
- **Compte de résultat** : récapitulatif des produits et charges sur une période. Permet de calculer le résultat (bénéfice ou perte).
- **Déclaration de bénéficiaire effectif** : déclaration au registre des UBO précisant qui contrôle ultimement la société.
- **Article de presse** : source d’information journalistique, à recouper avec d’autres sources avant utilisation.
- **Décision de justice** : jugement, ordonnance, arrêt. Si public, source précieuse pour comprendre des contentieux passés.

> L’objectif du FININT n’est pas de faire un cours de comptabilité ou de droit, mais de **savoir à quoi sert chaque document** dans une enquête, et **où trouver l’information** dont on a besoin.

-----

### 0.4 — Comprendre la logique comptable minimale

Pas besoin d’être comptable pour faire du FININT. Mais quelques notions sont indispensables :

- **Chiffre d’affaires (CA)** : somme des ventes réalisées sur une période. Indicateur de la « taille » commerciale.
- **Charges** : ce que l’entreprise dépense (achats, salaires, loyers, frais financiers, etc.).
- **Bénéfice / perte (résultat)** : différence entre produits et charges. Bénéfice si positif, perte si négatif.
- **Actif** : tout ce que possède l’entreprise (immobilier, matériel, créances clients, trésorerie, participations, etc.).
- **Passif** : tout ce que doit l’entreprise (capital et réserves, dettes financières, dettes fournisseurs, dettes fiscales et sociales, etc.).
- **Trésorerie** : argent disponible immédiatement (sur les comptes bancaires, en caisse).
- **Dettes** : ce que l’entreprise doit à des tiers (banques, fournisseurs, État, etc.).
- **Créances** : ce qui est dû à l’entreprise (par ses clients, principalement).
- **Marge** : différence entre prix de vente et coût d’achat. Indique la rentabilité d’une activité.
- **Capital social** : apport initial des associés au lancement de la société. Inscrit au passif. Peut être très faible (1 € pour une SAS) ou substantiel.

> **Formulation simple** : le **compte de résultat** raconte ce que l’entreprise a gagné et dépensé pendant une période. Le **bilan** montre ce qu’elle possède et ce qu’elle doit à une date donnée. L’analyste FININT lit ces documents pour vérifier la **cohérence** entre l’activité déclarée et la réalité économique observable.

-----

### 0.5 — Comprendre les acteurs d’un dossier financier

Un dossier FININT mobilise un écosystème d’acteurs. Les principaux :

#### Acteurs économiques

- **Banque** : institution financière qui tient des comptes, exécute des paiements, accorde des crédits. **Assujettie** aux obligations LCB-FT.
- **PSP / fintech** : prestataire de services de paiement (Stripe, Revolut, Wise, etc.). Souvent **assujetti** également.
- **Client** : celui qui achète un bien ou une prestation.
- **Fournisseur** : celui qui vend un bien ou une prestation.

#### Acteurs structurels

- **Société écran** : entité juridique sans substance économique réelle.
- **Prête-nom** : personne qui apparaît officiellement (dirigeant, associé) sans exercer le contrôle réel.
- **Bénéficiaire effectif (UBO)** : personne physique qui contrôle ultimement une entité.

#### Acteurs institutionnels — France principalement

- **TRACFIN** : Cellule de Renseignement Financier française. Reçoit les déclarations de soupçon, produit du renseignement, transmet aux autorités compétentes.
- **Parquet** : magistrats du ministère public, dirigent l’enquête pénale. En France, le **PNF (Parquet National Financier)** est spécialisé sur la criminalité financière complexe.
- **Juge d’instruction** : magistrat indépendant chargé d’instruire un dossier pénal complexe.
- **Autorités fiscales** : en France, la **DGFiP (Direction Générale des Finances Publiques)**. Contrôlent et sanctionnent les manquements fiscaux.
- **Autorités douanières** : en France, la **DGDDI (Direction Générale des Douanes et Droits Indirects)**. Contrôlent les flux de marchandises et certains flux financiers.
- **Superviseurs financiers** : **ACPR** (banques, assurances), **AMF** (marchés financiers et PSAN/CASP). Veillent au respect des règles par les acteurs régulés.

#### Acteurs internationaux

- **CRF étrangères** : équivalents de TRACFIN dans d’autres pays. Coopération via Egmont et FIU.NET (UE).
- **Europol, Interpol, Eurojust, EPPO** : agences européennes ou internationales de coopération policière et judiciaire.

> Comprendre qui fait quoi évite beaucoup d’erreurs : un cabinet privé n’a pas les mêmes pouvoirs qu’un parquet, une banque n’est pas un policier, une CRF n’est pas un tribunal.

-----

### 0.6 — Comprendre les notions juridiques minimales

Quelques distinctions essentielles, que le cours développera ensuite :

- **Soupçon** : intuition étayée d’éléments objectifs. En LCB-FT, il a un **seuil légal** : il déclenche la déclaration de soupçon (DS) par les assujettis. **Le soupçon n’est ni la certitude, ni la preuve.**
- **Preuve** : élément établi de manière formelle, recevable en justice, susceptible de fonder une décision juridictionnelle. Obtenue par des actes d’enquête (réquisitions, auditions, expertises) sous autorité judiciaire.
- **Renseignement** : produit d’analyse qui éclaire une situation, oriente une action, sans avoir la valeur formelle d’une preuve. Le FININT produit du renseignement.
- **Infraction** : comportement interdit par la loi, sanctionné. Peut être un crime, un délit ou une contravention.
- **Blanchiment** : opération de dissimulation de l’origine illicite de fonds.
- **Fraude** : tromperie pour obtenir un avantage indu (fraude fiscale, fraude au virement, etc.).
- **Corruption** : obtention d’un avantage en échange d’un acte illicite par une personne en position de pouvoir.
- **Sanctions** : mesures restrictives imposées contre des personnes, entités, pays (gel d’avoirs, interdiction de transactions, embargos).
- **Gel** : mesure conservatoire empêchant l’usage d’un avoir.
- **Saisie** : mesure judiciaire retenant juridiquement un avoir.
- **Confiscation** : transfert définitif d’un avoir à l’État après condamnation.
- **Présomption d’innocence** : principe selon lequel toute personne est présumée innocente tant qu’elle n’a pas été déclarée coupable par une décision de justice définitive.

> Cette sous-partie prépare une distinction centrale du cours : le **FININT produit du renseignement**, pas automatiquement de la preuve judiciaire. Convertir le renseignement en preuve exige des actes d’enquête conduits sous autorité juridictionnelle. Cette distinction est revue en détail au chapitre 4.

-----

### 0.7 — Comprendre les sources

Les sources mobilisées en FININT n’ont pas toutes le même statut, ni la même accessibilité. Distinguer les catégories est l’une des disciplines essentielles du métier :

- **Source ouverte (OSINT)** : accessible publiquement (registre des sociétés, presse, réseaux sociaux, données ouvertes type DVF). Pas de restriction particulière à son usage par un analyste, hors RGPD et droit d’auteur.
- **Source payante professionnelle** : accessible par abonnement (Sayari, Orbis, World-Check, Factiva). Réservée aux organisations abonnées.
- **Source bancaire** : interne à une banque (KYC, monitoring, données clients). Accessible aux **assujettis LCB-FT** dans le cadre de leurs obligations.
- **Source CRF** : interne à une cellule de renseignement financier (DS reçues, FIU.NET, Egmont). Accessible aux CRF uniquement.
- **Source judiciaire** : accessible sous autorité juridictionnelle (réquisitions bancaires, FICOBA, perquisitions). Réservée aux magistrats et enquêteurs sous procédure.
- **Source fiscale** : accessible aux autorités fiscales (DGFiP), à l’occasion de leurs contrôles ou via les échanges internationaux (EAR/CRS).
- **Source issue d’un leak** : données dévoilées par lanceurs d’alerte (Pandora Papers, Panama Papers). Accessibles selon les modalités définies par les consortiums (ICIJ Offshore Leaks public partiel, Aleph pour journalistes).
- **Source journalistique** : enquêtes publiées par la presse. Soumise à recoupement par l’analyste.

> Comprendre cette typologie évite l’erreur fréquente du débutant : penser que **tout est accessible publiquement**. Beaucoup de données critiques (relevés bancaires détaillés, comptes étrangers, données fiscales) ne sont **pas en OSINT**. L’analyste opère **dans le cadre qui est le sien** (cabinet, banque, CRF, judiciaire) et avec les sources autorisées par ce cadre. L’annexe M détaille ce point sous forme de tableau.

-----

### 0.8 — Mini-exemple de mise en pratique

Pour mettre en pratique ces notions de base, voici un mini-cas très simple :

> **Situation** : une société française, **TRADEX SAS**, créée il y a 8 mois, reçoit un virement de **400 000 €** depuis une société étrangère basée aux Émirats. TRADEX a un **capital social de 1 000 €**, **pas de site web**, un **dirigeant unique** (M. P, 31 ans, sans expérience visible dans le secteur déclaré), et une **adresse de domiciliation** dans un cabinet parisien hébergeant 50 autres sociétés.

#### Ce qu’on peut dire à ce stade

- **Faits observables** : la société est récente (8 mois), à très faible capital, sans présence opérationnelle visible (pas de site, domiciliation), avec un dirigeant au profil incohérent avec une activité commerciale internationale supposée. Le flux entrant (400 000 €) est significatif au regard de la taille apparente.
- **Hypothèses calibrées** :
  - Société écran *probable* (signaux convergents).
  - Activité économique réelle *douteuse* à ce stade.
  - Le flux entrant est *à investiguer* : est-il cohérent avec une activité légitime ?

#### Ce qu’on **ne peut pas** dire à ce stade

- On **ne peut pas** affirmer que TRADEX est une société de blanchiment : ce serait une qualification juridique non démontrée.
- On **ne peut pas** désigner M. P comme un fraudeur : il pourrait être un dirigeant inexpérimenté mais légitime, un prête-nom, ou un débutant motivé.
- On **ne peut pas** qualifier la société étrangère sans investigation.

#### Sources à consulter en premier

1. **Pappers** ou INPI : confirmer l’identification de TRADEX (SIREN, statuts, dirigeant déclaré).
1. **RBE** : bénéficiaire effectif déclaré de TRADEX.
1. **Profil du dirigeant** : LinkedIn, presse, autres mandats déclarés (recherche par nom).
1. **Adresse de domiciliation** : autres sociétés à la même adresse, profil du cabinet de domiciliation.
1. **Société émettrice émiratie** : registre Dubaï (free zone ou mainland selon la juridiction), dirigeants, activité déclarée.

#### Conclusion provisoire

À ce stade, l’analyste produit une **mini-fiche d’alerte** : signaux convergents justifiant approfondissement, hypothèses calibrées en *probable* ou *possible*, lacunes documentées, sources à mobiliser. **Aucune conclusion** sur la nature licite ou illicite de l’opération.

C’est exactement ce que le cours va apprendre à faire, avec rigueur, sur des cas plus complexes.

-----

### Points clés à retenir du Chapitre 0

- **Personne physique vs morale** : derrière chaque société, il y a des humains à identifier.
- **Flux financiers** : donneur d’ordre, bénéficiaire, libellé, banques, devise — à toujours décortiquer.
- **Documents** : Kbis, statuts, facture, bilan, relevé, leak — chacun a une fonction et des limites.
- **Logique comptable** : bilan = photo, compte de résultat = film, marge = rentabilité, trésorerie = liquidité.
- **Acteurs** : économiques, structurels, institutionnels — chacun a un rôle et des pouvoirs distincts.
- **Notions juridiques** : soupçon ≠ preuve ; renseignement ≠ accusation ; toujours présomption d’innocence.
- **Sources** : OSINT, professionnelle, bancaire, CRF, judiciaire, fiscale, leak, presse — chacune a son cadre d’accès.
- **Discipline FININT** : observer, qualifier, calibrer, documenter les lacunes — pas conclure prématurément.

Vous êtes prêt(e) pour le **parcours express** qui vient ensuite, ou pour la **Partie I** si vous suivez la progression linéaire.

-----

## Parcours express — Lire un dossier financier en 45 minutes

> **Objectif** : à partir d’un simple nom de société ou de personne, produire en 45 minutes une **première fiche FININT exploitable** — qui ne tranche rien, mais qui pose les bases d’une analyse plus poussée.

Cette procédure ne remplace pas une enquête approfondie. Elle constitue un **premier filtre** : qualifier rapidement un dossier (faut-il s’y attarder ?), repérer les points saillants (quelles sont les zones d’ombre ?), formuler quelques hypothèses calibrées (qu’est-ce que je peux dire ? qu’est-ce que je ne peux pas dire ?), et produire un livrable court (une mini-note d’une à deux pages).

Le parcours est volontairement borné dans le temps. La discipline est la suivante : on ne cherche pas l’exhaustivité, on cherche la **première lecture** d’un dossier. Si un point mérite approfondissement, on le note comme tel et on y reviendra dans une seconde phase.

### Étape 1 — Identifier l’entité exacte (3 min)

Avant toute recherche, **stabiliser le périmètre**. Une recherche lancée sans cette étape produit du bruit (homonymes, sociétés homonymes, variantes orthographiques) qui pollue toute la suite.

Pour une **société** : récupérer la dénomination sociale exacte, la forme juridique, le numéro d’identification (SIREN/SIRET en France, Companies House Number au UK, EIN aux US, RCS, NIF, etc.). Croiser avec un registre officiel pour confirmer.

Pour une **personne physique** : nom, prénoms (tous, dans l’ordre), date de naissance approximative ou exacte, lieu de naissance si possible, nationalité connue. Sans ces éléments, le risque d’homonymie est élevé.

Notation : `Entité = [dénomination] | [identifiant officiel] | [forme] | [pays]` ou `Personne = [nom] [prénom] | né(e) [JJ/MM/AAAA ou approx] à [lieu] | nationalité [pays]`.

### Étape 2 — Vérifier le statut légal (3 min)

Confirmer que l’entité **existe**, est **active** et n’est pas en procédure. Pour une société : statut au registre (active / radiée / en liquidation / en redressement), date de création, dernière modification (changements récents = signal). Pour une personne : présence sur listes de sanctions internationales (OFAC SDN, UE, ONU, HM Treasury, sanctions spécifiques), statut PEP éventuel, mentions visibles dans des procédures.

Outils gratuits : registres publics nationaux (chapitres 11-12), portails de sanctions consolidés (OpenSanctions, Sanctions.io en lecture libre partielle), bases adverse media (presse).

### Étape 3 — Identifier dirigeants et mandataires (5 min)

Lister les personnes physiques exerçant une fonction déclarée : président, gérant, directeur général, administrateurs, membres du conseil de surveillance, secrétaire (UK), commissaires aux comptes, fondés de pouvoir. Pour chaque mandataire, noter la **date de prise de fonction** et la **durée** : un mandataire installé depuis 15 ans ne dit pas la même chose qu’un mandataire arrivé il y a 4 mois.

Repérer les **profils suspects** sans les diaboliser : mandataires multi-sociétés (« corporate service providers » professionnels), mandataires retraités ou très jeunes, mandataires à l’adresse identique à la société, mandataires figurant comme dirigeants de dizaines d’entités sans cohérence sectorielle.

### Étape 4 — Chercher actionnaires et bénéficiaires effectifs (5 min)

Distinguer **actionnariat déclaré** et **bénéficiaire effectif** (UBO). L’actionnariat est ce qui apparaît dans les statuts ou la liste d’associés ; l’UBO est la personne physique qui détient ou contrôle ultimement l’entité (seuils de 25 % en UE, mais le contrôle peut être indirect).

Sources : registres des bénéficiaires effectifs (accès variable selon les juridictions depuis l’arrêt CJUE 2022 — voir chapitre 13), Companies House (UK) avec registre PSC, OpenCorporates en agrégation, et bases professionnelles (Orbis, Sayari) si disponibles.

Si l’UBO n’est pas accessible via les sources ouvertes : noter l’opacité comme **fait** (pas comme faute), et formuler la question pour la suite.

### Étape 5 — Cartographier les sociétés liées (5 min)

Identifier les **liens** : sociétés ayant le même dirigeant, sociétés à la même adresse, sociétés détenues par la même holding, sociétés figurant dans les mêmes leaks. Ne pas chercher l’exhaustivité ; cibler les liens visibles en quelques requêtes.

Première représentation graphique mentale : un noyau (l’entité initiale), une couronne directe (sociétés liées de premier degré), une couronne indirecte (sociétés liées via un mandataire ou une adresse partagée). Cette esquisse sera affinée plus tard avec un outil dédié (Maltego, Linkurious, Gephi — chapitre 52).

### Étape 6 — Sanctions, PEP, adverse media (5 min)

Trois sources à interroger systématiquement.

**Sanctions** : OFAC SDN, sanctions UE consolidées, ONU, HM Treasury, et listes nationales spécifiques selon le pays. Une mention sur l’une de ces listes change radicalement la qualification du dossier.

**PEP** (Politiquement Exposée) : ancien ou actuel dirigeant politique, haut fonctionnaire, membre de la famille proche ou collaborateur connu. Statut PEP ≠ culpabilité, mais déclenche une vigilance renforcée.

**Adverse media** : presse économique généraliste (Le Monde, Les Échos, Reuters, Bloomberg, FT, WSJ), presse d’investigation (Mediapart, OCCRP, ICIJ), bases d’agrégation (Factiva, LexisNexis, Dow Jones Risk & Compliance — Ch.51).

### Étape 7 — Repérer les actifs visibles (5 min)

Première cartographie patrimoniale : biens immobiliers visibles (Patrim France, registres fonciers étrangers, données cadastrales si publiques), véhicules ou bateaux dont l’enregistrement est public dans certains pays, parts dans d’autres sociétés, signaux de train de vie (réseaux sociaux, presse mondaine — voir chapitre 17).

Mise en regard : actifs visibles vs revenus déclarés (lorsque les comptes annuels sont accessibles) vs activité observable. Une discordance massive est un signal — pas une preuve.

### Étape 8 — Identifier les incohérences (5 min)

Cinq familles d’incohérences à repérer rapidement :

1. **Économique** — chiffre d’affaires sans rapport avec la taille apparente de la société (1 employé, 50 M€ de CA), marges incohérentes avec le secteur, charges incohérentes avec l’activité.
1. **Géographique** — sociétés dans des juridictions sans rapport avec leur activité visible (négociant en produits agricoles d’Afrique de l’Ouest avec siège à Tortola).
1. **Temporelle** — créations en cascade, changements de dirigeants ou de dénomination juste avant un appel d’offres ou un signalement.
1. **Documentaire** — comptes non publiés, comptes publiés en retard, mentions « non significatives » récurrentes, absence de commissaire aux comptes au-delà des seuils.
1. **Déclarative** — UBO « inconnu » alors qu’une personne contrôle visiblement l’entité par d’autres canaux.

### Étape 9 — Formuler des hypothèses calibrées (5 min)

À ce stade, le réflexe à éviter est la **conclusion prématurée**. On ne cherche pas à dire *« c’est une société écran »*, mais *« les éléments observés sont compatibles avec X, Y ou Z, avec tel niveau de confiance pour chaque hypothèse »*.

Exemple de formulation :

- *H1 — Activité commerciale légitime atypique mais réelle. Compatible avec : siège à l’adresse du comptable, faible nombre d’employés (sous-traitance possible), liens sectoriels cohérents. Niveau de confiance : possible.*
- *H2 — Société écran utilisée à des fins d’opacification. Compatible avec : UBO masqué, adresse partagée avec 14 autres sociétés du même corporate service provider, comptes non publiés depuis 3 ans, aucune trace d’activité visible. Niveau de confiance : probable.*
- *H3 — Implication dans un schéma de fraude active. Compatible avec : … (à étayer). Niveau de confiance : insuffisant à ce stade.*

Toujours mentionner les **éléments qui contredisent** les hypothèses retenues. C’est la marque d’un raisonnement honnête.

### Étape 10 — Produire la mini-note (4 min)

La mini-note tient en une à deux pages. Structure proposée :

```
RÉFÉRENCE : [identifiant du dossier] | DATE : [JJ/MM/AAAA]
CLASSIFICATION : [TLP : X]

OBJET (2 lignes)
  Mini-fiche FININT initiale sur [entité ou personne].

ÉLÉMENTS RECUEILLIS (puces)
  - Identification stabilisée
  - Statut légal et présence sur listes
  - Dirigeants / UBO
  - Sociétés liées
  - Patrimoine visible
  - Incohérences relevées

HYPOTHÈSES CALIBRÉES
  H1 ... [niveau de confiance]
  H2 ... [niveau de confiance]
  H3 ... [niveau de confiance]

LACUNES
  Sources non consultées
  Juridictions non couvertes
  Données manquantes

RECOMMANDATIONS
  Approfondir : [oui / non / sous condition]
  Sollicitations utiles : [registres complémentaires / réquisition / OSINT approfondi / coopération]
```


La mini-note est un **livrable de cadrage**. Elle ne tranche pas. Elle permet à l’analyste, au demandeur ou à l’équipe de décider si le dossier mérite d’être approfondi, et avec quelle priorité.

### Erreurs fréquentes du parcours express

- **Conclure trop tôt** sur la base de quelques signaux. La règle d’or : tant que vous n’avez pas suivi les 10 étapes, vous n’avez pas une première lecture — vous avez une intuition.
- **Accumuler du bruit** : recherches « tout azimut » qui produisent un dossier illisible. Le parcours est borné dans le temps précisément pour éviter cela.
- **Ignorer l’homonymie** : sauter l’étape 1 conduit à attribuer à une cible des éléments qui ne la concernent pas. C’est l’erreur la plus dommageable et la plus fréquente.
- **Confondre opacité et culpabilité** : l’absence d’information n’est pas une preuve d’irrégularité. Elle est une *contrainte d’enquête*.
- **Ne pas documenter les sources** : une mini-note sans sources est inexploitable. Chaque élément doit pouvoir être reproduit.

### Limites

Le parcours express ne répond pas à des questions du type *« est-ce que cette personne blanchit ? »* — il répond à *« cette entité mérite-t-elle un examen approfondi ? »*. Pour des dossiers à enjeux (signalement parquet, gel, dissémination internationale), un workflow complet (chapitre 49) est nécessaire, avec des sources fermées (réquisitions, données fiscales, droits de communication CRF) qui ne sont mobilisables qu’en cadre légal approprié.

-----

## Fil rouge — Opération CLEARFLOW

> **Statut narratif** : ce fil rouge est une fiction pédagogique. Il accompagne le cours du chapitre 1 jusqu’à la synthèse en chapitre 64. Il est conçu pour illustrer concrètement chaque section, sans empiéter sur la matière théorique.

### Le contexte

Une **cellule de renseignement financier (CRF) européenne fictive**, inspirée du fonctionnement d’une CRF de type TRACFIN, traite quotidiennement plusieurs centaines de déclarations de soupçon (DS) provenant des assujettis (banques, PSP, notaires, marchands d’art, professions juridiques, VASP). La CRF fictive du fil rouge est un **environnement institutionnel inspiré**, pas une représentation officielle d’une CRF réelle.

Au sein du département « Analyse et renseignement », **Nassim Belhaj** est analyste senior FININT. Son profil : sept ans d’expérience, solide en LCB-FT, lecture des registres d’entreprises, analyse des flux bancaires, identification des bénéficiaires effectifs et analyse patrimoniale. Formation initiale en finance et en droit des affaires, certification CAMS, formation continue sur les typologies GAFI et l’analyse de réseaux.

### Le signalement initial

Sur six mois consécutifs, la CRF reçoit **dix-sept déclarations de soupçon convergentes** émanant de :

- 5 banques françaises (1 grande banque mutualiste, 2 grandes banques de réseau, 2 banques privées) ;
- 2 établissements de paiement européens (un PSP français et un EME lituanien) ;
- 1 notaire (DS lors d’une acquisition immobilière inhabituellement rapide) ;
- 1 marchand d’art (DS sur une vente aux enchères payée en cash partiel).

Les DS pointent un homme d’affaires franco-libanais, **Karim Haddad**, et un réseau d’environ une douzaine de sociétés gravitant autour de lui dans plusieurs juridictions : France, Chypre, Émirats arabes unis, Bénin, Côte d’Ivoire, Suisse, Liban.

Les anomalies signalées : virements entrants depuis des sociétés de négoce basées à Dubaï et Istanbul vers des comptes français pour des montants compris entre 45 000 € et 95 000 € (sous le seuil de surveillance interne renforcée), libellés vagues (« commercial services », « trade payment »), paiements sortants vers des fournisseurs ouest-africains pour des marchandises agricoles dont la réalité physique paraît douteuse, transferts vers des comptes personnels en Suisse et au Luxembourg, dépôts en espèces structurés sous le seuil de 15 000 €, conversions partielles en USDT via un exchange européen, et au moins une opération de marché public en Côte d’Ivoire suspectée d’avoir été remportée dans des conditions opaques.

Montant cumulé sur la période : **environ 22 M€** de flux non encore qualifiés.

### Le mandat de Nassim

Le pôle réception/traitement transmet le dossier à Nassim avec un mandat structuré :

1. **Reconstituer le périmètre** — toutes les sociétés et personnes physiques liées au noyau Haddad.
1. **Cartographier les flux** — origine, transit, destination, mécanismes d’opacification.
1. **Qualifier le ou les schémas** — typologie probable (TBML ? cascade de sociétés ? corruption de marché public ? contournement de sanctions ?).
1. **Identifier les acteurs et leurs rôles** — organisateur, prête-noms, facilitateurs, bénéficiaires.
1. **Recommander les suites** — signalement parquet, gel TRACFIN, dissémination internationale via Egmont, sollicitations complémentaires.

### Les questions de renseignement (QR)

Nassim formule, dès le cadrage, **quatre questions de renseignement** qui structureront son travail :

- **QR1** — D’où vient l’argent ? Quelle est l’infraction prédécesseur probable ?
- **QR2** — Comment est-il opacifié ? Quel est le ou les schémas combinés ?
- **QR3** — Où va-t-il ? Quel est le patrimoine réel de Haddad ?
- **QR4** — Qui participe ? Quel est le réseau d’acteurs (prête-noms, complices, facilitateurs) ?

Une cinquième question de gestion du dossier émerge rapidement :

- **QR5** — Quelles coopérations sont nécessaires ? Athéna Group (volet crypto), CRF étrangères (Chypre, Émirats, Suisse), services nationaux (DGSI, DGDDI, DGFiP) ?

### Coopérations prévues

Le dossier comporte une **branche crypto limitée** : conversions USDT identifiées, mais le traçage on-chain dépasse le périmètre méthodologique de la CRF fictive. Nassim sollicitera **Sarah Marin** (Athéna Group, analyste crypto-forensique senior, ancienne TRACFIN) dans le cadre d’une convention pré-existante : la CRF fictive dispose d’un **cadre contractuel et juridique** (marché public, habilitation des intervenants, clauses de confidentialité, traitement des données minimisées et journalisées) permettant, sous contrôle interne strict et secret professionnel, de solliciter Athéna Group pour une **expertise technique on-chain limitée**. Le rapport produit par Athéna est intégré comme **intrant analytique au renseignement**, non comme preuve judiciaire autonome. Tout le volet on-chain (traçage, clustering, attribution d’adresses, identification des cashout) sera traité dans ce cadre et renvoyé au cours OSINT Crypto pour la méthode.

Un **volet documentaire** secondaire pourrait apparaître plus tard : suspicion de fausses factures et de faux certificats d’origine. Si ce volet se confirme, **Lucas Ferreira** (collègue de Sarah chez Athéna, spécialisé Dark Web et faux documents) pourra être consulté ponctuellement. Cette branche reste secondaire dans le fil rouge.

### Distinction renseignement / preuve — fondamentale

> **À garder à l’esprit pendant tout le cours** : la note d’analyse de Nassim est du **renseignement**. Elle oriente l’enquête, identifie les pistes, recommande des actions. Elle n’est pas une preuve au sens du Code de procédure pénale. La transformation du renseignement en preuve nécessite des **actes d’enquête judiciaire** (réquisitions, auditions, expertises) conduits sous l’autorité d’un magistrat. L’analyste FININT doit, en permanence, savoir ce qu’il peut écrire, ce qui peut être disséminé, ce qui est exploitable judiciairement, et ce qui n’est qu’un faisceau d’indices à corroborer.

### Bilan attendu — sans happy ending

Le fil rouge sera synthétisé au chapitre 64. Le bilan, conformément à la réalité opérationnelle des dossiers FININT complexes, sera **honnête** :

- Schéma probable cartographié, hypothèses calibrées, recommandations transmises ;
- Une partie des flux identifiée avec un haut niveau de confiance, une autre seulement présumée ;
- Coopérations engagées avec délais réalistes (mois à années pour la MLA, plus rapide pour Egmont) ;
- Recouvrement éventuellement partiel, sur plusieurs années, sans garantie ;
- Quelques branches du dossier qui resteront ouvertes ou non concluantes — c’est la norme.

Pas de dénouement spectaculaire : le FININT, dans la réalité, produit du renseignement actionnable. Le reste appartient au judiciaire et au politique.

-----

## Sommaire

- [Partie I — Comprendre le renseignement financier](01-partie-i-comprendre-le-renseignement-financier/index.md)
    - [Chapitre 1 — Pourquoi le FININT est central aujourd’hui](01-partie-i-comprendre-le-renseignement-financier/01-chapitre-1-pourquoi-le-finint-est-central-aujourdh.md)
    - [Chapitre 2 — Ce que le FININT permet vraiment](01-partie-i-comprendre-le-renseignement-financier/02-chapitre-2-ce-que-le-finint-permet-vraiment.md)
    - [Chapitre 3 — Ce que le FININT ne permet pas](01-partie-i-comprendre-le-renseignement-financier/03-chapitre-3-ce-que-le-finint-ne-permet-pas.md)
    - [Chapitre 4 — Renseignement, soupçon, preuve et judiciarisation](01-partie-i-comprendre-le-renseignement-financier/04-chapitre-4-renseignement-soupcon-preuve-et-judicia.md)
    - [Chapitre 5 — FININT, OSINT financier, AML, CTI et OSINT Crypto](01-partie-i-comprendre-le-renseignement-financier/05-chapitre-5-finint-osint-financier-aml-cti-et-osint.md)
- [Partie II — Le système financier pour L’enquêteur](02-partie-ii-le-systeme-financier-pour-lenqueteur/index.md)
    - [Chapitre 6 — Le système bancaire et la circulation de l’argent](02-partie-ii-le-systeme-financier-pour-lenqueteur/01-chapitre-6-le-systeme-bancaire-et-la-circulation-d.md)
    - [Chapitre 7 — Rails de paiement : SWIFT, SEPA, TARGET2, Fedwire, ACH](02-partie-ii-le-systeme-financier-pour-lenqueteur/02-chapitre-7-rails-de-paiement-swift-sepa-target2-fe.md)
    - [Chapitre 8 — PSP, EME, néobanques et fintechs](02-partie-ii-le-systeme-financier-pour-lenqueteur/03-chapitre-8-psp-eme-neobanques-et-fintechs.md)
    - [Chapitre 9 — Comptes bancaires, relevés et opérations](02-partie-ii-le-systeme-financier-pour-lenqueteur/04-chapitre-9-comptes-bancaires-releves-et-operations.md)
    - [Chapitre 10 — Offshore, secret bancaire et juridictions opaques](02-partie-ii-le-systeme-financier-pour-lenqueteur/05-chapitre-10-offshore-secret-bancaire-et-juridictio.md)
- [Partie III — Sources OSINT financières](03-partie-iii-sources-osint-financieres/index.md)
    - [Chapitre 11 — Registres d’entreprises : France, UK, US](03-partie-iii-sources-osint-financieres/01-chapitre-11-registres-dentreprises-france-uk-us.md)
    - [Chapitre 12 — Registres d’entreprises : reste de l’Europe et du monde](03-partie-iii-sources-osint-financieres/02-chapitre-12-registres-dentreprises-reste-de-leurop.md)
    - [Chapitre 13 — Identifier les bénéficiaires effectifs](03-partie-iii-sources-osint-financieres/03-chapitre-13-identifier-les-beneficiaires-effectifs.md)
    - [Chapitre 14 — Comptes annuels, bilans et documents financiers](03-partie-iii-sources-osint-financieres/04-chapitre-14-comptes-annuels-bilans-et-documents-fi.md)
    - [Chapitre 15 — Marchés publics, subventions et appels d’offres](03-partie-iii-sources-osint-financieres/05-chapitre-15-marches-publics-subventions-et-appels.md)
    - [Chapitre 16 — Contentieux, procédures collectives et sanctions administratives](03-partie-iii-sources-osint-financieres/06-chapitre-16-contentieux-procedures-collectives-et.md)
    - [Chapitre 17 — Presse, adverse media et SOCMINT financier](03-partie-iii-sources-osint-financieres/07-chapitre-17-presse-adverse-media-et-socmint-financ.md)
    - [Chapitre 18 — Leaks financiers : ICIJ, OCCRP, Aleph, Panama/Pandora](03-partie-iii-sources-osint-financieres/08-chapitre-18-leaks-financiers-icij-occrp-aleph-pana.md)
- [Partie IV — Personnes, sociétés et contrôle](04-partie-iv-personnes-societes-et-controle/index.md)
    - [Chapitre 19 — Identifier une personne physique sans se tromper d’homonyme](04-partie-iv-personnes-societes-et-controle/01-chapitre-19-identifier-une-personne-physique-sans.md)
    - [Chapitre 20 — Identifier une société et ses variantes internationales](04-partie-iv-personnes-societes-et-controle/02-chapitre-20-identifier-une-societe-et-ses-variante.md)
    - [Chapitre 21 — Formes juridiques comparées](04-partie-iv-personnes-societes-et-controle/03-chapitre-21-formes-juridiques-comparees.md)
    - [Chapitre 22 — Dirigeants, mandataires et administrateurs](04-partie-iv-personnes-societes-et-controle/04-chapitre-22-dirigeants-mandataires-et-administrate.md)
    - [Chapitre 23 — Actionnaires, UBO et contrôle indirect](04-partie-iv-personnes-societes-et-controle/05-chapitre-23-actionnaires-ubo-et-controle-indirect.md)
    - [Chapitre 24 — Holdings, filiales et montages en cascade](04-partie-iv-personnes-societes-et-controle/06-chapitre-24-holdings-filiales-et-montages-en-casca.md)
    - [Chapitre 25 — Trusts, fondations, nominees et prête-noms](04-partie-iv-personnes-societes-et-controle/07-chapitre-25-trusts-fondations-nominees-et-prete-no.md)
    - [Chapitre 26 — Sociétés écrans et sociétés dormantes](04-partie-iv-personnes-societes-et-controle/08-chapitre-26-societes-ecrans-et-societes-dormantes.md)
- [Partie V — Cartographier les réseaux financiers](05-partie-v-cartographier-les-reseaux-financiers/index.md)
    - [Chapitre 27 — Construire une fiche personne](05-partie-v-cartographier-les-reseaux-financiers/01-chapitre-27-construire-une-fiche-personne.md)
    - [Chapitre 28 — Construire une fiche société](05-partie-v-cartographier-les-reseaux-financiers/02-chapitre-28-construire-une-fiche-societe.md)
    - [Chapitre 29 — Construire une fiche flux](05-partie-v-cartographier-les-reseaux-financiers/03-chapitre-29-construire-une-fiche-flux.md)
    - [Chapitre 30 — Construire une fiche actif](05-partie-v-cartographier-les-reseaux-financiers/04-chapitre-30-construire-une-fiche-actif.md)
    - [Chapitre 31 — Graphes relationnels FININT](05-partie-v-cartographier-les-reseaux-financiers/05-chapitre-31-graphes-relationnels-finint.md)
    - [Chapitre 32 — Distinguer lien faible, lien fort et contrôle réel](05-partie-v-cartographier-les-reseaux-financiers/06-chapitre-32-distinguer-lien-faible-lien-fort-et-co.md)
    - [Chapitre 33 — Échelle de confiance WEP et hypothèses calibrées](05-partie-v-cartographier-les-reseaux-financiers/07-chapitre-33-echelle-de-confiance-wep-et-hypotheses.md)
- [Partie VI — Analyse DE flux et comptabilité forensique](06-partie-vi-analyse-de-flux-et-comptabilite-forensiq/index.md)
    - [Chapitre 34 — Lire un relevé bancaire](06-partie-vi-analyse-de-flux-et-comptabilite-forensiq/01-chapitre-34-lire-un-releve-bancaire.md)
    - [Chapitre 35 — Reconstituer des flux financiers](06-partie-vi-analyse-de-flux-et-comptabilite-forensiq/02-chapitre-35-reconstituer-des-flux-financiers.md)
    - [Chapitre 36 — Lire un bilan et un compte de résultat](06-partie-vi-analyse-de-flux-et-comptabilite-forensiq/03-chapitre-36-lire-un-bilan-et-un-compte-de-resultat.md)
    - [Chapitre 37 — Détecter anomalies comptables et signaux faibles](06-partie-vi-analyse-de-flux-et-comptabilite-forensiq/04-chapitre-37-detecter-anomalies-comptables-et-signa.md)
    - [Chapitre 38 — Factures, marges, marchandises et cohérence économique](06-partie-vi-analyse-de-flux-et-comptabilite-forensiq/05-chapitre-38-factures-marges-marchandises-et-cohere.md)
    - [Chapitre 39 — Reconstitution patrimoniale et train de vie](06-partie-vi-analyse-de-flux-et-comptabilite-forensiq/06-chapitre-39-reconstitution-patrimoniale-et-train-d.md)
- [Partie VII — Typologies DE criminalité financière](07-partie-vii-typologies-de-criminalite-financiere/index.md)
    - [Chapitre 40 — Blanchiment : placement, empilement, intégration](07-partie-vii-typologies-de-criminalite-financiere/01-chapitre-40-blanchiment-placement-empilement-integ.md)
    - [Chapitre 41 — Trade-Based Money Laundering (TBML)](07-partie-vii-typologies-de-criminalite-financiere/02-chapitre-41-trade-based-money-laundering-tbml.md)
    - [Chapitre 42 — Corruption, commissions occultes et PEP](07-partie-vii-typologies-de-criminalite-financiere/03-chapitre-42-corruption-commissions-occultes-et-pep.md)
    - [Chapitre 43 — Fraude fiscale, carrousel TVA et abus de biens sociaux](07-partie-vii-typologies-de-criminalite-financiere/04-chapitre-43-fraude-fiscale-carrousel-tva-et-abus-d.md)
    - [Chapitre 44 — BEC, fraude au fournisseur et réseaux de mules](07-partie-vii-typologies-de-criminalite-financiere/05-chapitre-44-bec-fraude-au-fournisseur-et-reseaux-d.md)
    - [Chapitre 45 — Contournement de sanctions et biens dual-use](07-partie-vii-typologies-de-criminalite-financiere/06-chapitre-45-contournement-de-sanctions-et-biens-du.md)
    - [Chapitre 46 — Ponzi, pyramides et fraudes à l’investissement](07-partie-vii-typologies-de-criminalite-financiere/07-chapitre-46-ponzi-pyramides-et-fraudes-a-linvestis.md)
    - [Chapitre 47 — Criminalité organisée et économie légale](07-partie-vii-typologies-de-criminalite-financiere/08-chapitre-47-criminalite-organisee-et-economie-lega.md)
    - [Chapitre 48 — Cybercriminalité, cashout et renvoi vers OSINT Crypto](07-partie-vii-typologies-de-criminalite-financiere/09-chapitre-48-cybercriminalite-cashout-et-renvoi-ver.md)
- [Partie VIII — Outils, workflow et production](08-partie-viii-outils-workflow-et-production/index.md)
    - [Chapitre 49 — Workflow complet d’une enquête FININT](08-partie-viii-outils-workflow-et-production/01-chapitre-49-workflow-complet-dune-enquete-finint.md)
    - [Chapitre 50 — Outils gratuits : registres, sanctions, presse, leaks](08-partie-viii-outils-workflow-et-production/02-chapitre-50-outils-gratuits-registres-sanctions-pr.md)
    - [Chapitre 51 — Outils professionnels](08-partie-viii-outils-workflow-et-production/03-chapitre-51-outils-professionnels.md)
    - [Chapitre 52 — Visualisation](08-partie-viii-outils-workflow-et-production/04-chapitre-52-visualisation.md)
    - [Chapitre 53 — Chaîne de preuve, captures, horodatage, hash](08-partie-viii-outils-workflow-et-production/05-chapitre-53-chaine-de-preuve-captures-horodatage-h.md)
    - [Chapitre 54 — Note FININT, rapport et diffusion](08-partie-viii-outils-workflow-et-production/06-chapitre-54-note-finint-rapport-et-diffusion.md)
- [Partie IX — Cas pratiques déroulés](09-partie-ix-cas-pratiques-deroules/index.md)
    - [Chapitre 55 — Cas 1 : Société écran et fournisseur suspect](09-partie-ix-cas-pratiques-deroules/01-chapitre-55-cas-1-societe-ecran-et-fournisseur-sus.md)
    - [Chapitre 56 — Cas 2 : Fraude au changement d’IBAN / BEC](09-partie-ix-cas-pratiques-deroules/02-chapitre-56-cas-2-fraude-au-changement-diban-bec.md)
    - [Chapitre 57 — Cas 3 : Corruption internationale et PEP](09-partie-ix-cas-pratiques-deroules/03-chapitre-57-cas-3-corruption-internationale-et-pep.md)
    - [Chapitre 58 — Cas 4 : Contournement de sanctions via pays tiers](09-partie-ix-cas-pratiques-deroules/04-chapitre-58-cas-4-contournement-de-sanctions-via-p.md)
    - [Chapitre 59 — Cas 5 : Asset tracing d’un dirigeant sous enquête](09-partie-ix-cas-pratiques-deroules/05-chapitre-59-cas-5-asset-tracing-dun-dirigeant-sous.md)
- [Partie X — Cas historiques, coopération et professionnalisation](10-partie-x-cas-historiques-cooperation-et-profession/index.md)
    - [Chapitre 60 — Panama Papers](10-partie-x-cas-historiques-cooperation-et-profession/01-chapitre-60-panama-papers.md)
    - [Chapitre 61 — 1MDB : corruption, banques, luxe et asset recovery](10-partie-x-cas-historiques-cooperation-et-profession/02-chapitre-61-1mdb-corruption-banques-luxe-et-asset.md)
    - [Chapitre 62 — Wirecard : fraude comptable et défaillance systémique](10-partie-x-cas-historiques-cooperation-et-profession/03-chapitre-62-wirecard-fraude-comptable-et-defaillan.md)
    - [Chapitre 63 — Danske Bank Estonia](10-partie-x-cas-historiques-cooperation-et-profession/04-chapitre-63-danske-bank-estonia.md)
    - [Chapitre 64 — Synthèse du fil rouge CLEARFLOW](10-partie-x-cas-historiques-cooperation-et-profession/05-chapitre-64-synthese-du-fil-rouge-clearflow.md)
    - [Chapitre 65 — Coopération internationale : Egmont, GAFI, Europol, FIU](10-partie-x-cas-historiques-cooperation-et-profession/06-chapitre-65-cooperation-internationale-egmont-gafi.md)
    - [Chapitre 66 — Gel, saisie, confiscation et asset recovery](10-partie-x-cas-historiques-cooperation-et-profession/07-chapitre-66-gel-saisie-confiscation-et-asset-recov.md)
    - [Chapitre 67 — Cadre français : TRACFIN, ACPR, AMF, PNF, AGRASC](10-partie-x-cas-historiques-cooperation-et-profession/08-chapitre-67-cadre-francais-tracfin-acpr-amf-pnf-ag.md)
    - [Chapitre 68 — Éthique, RGPD, secret bancaire et limites](10-partie-x-cas-historiques-cooperation-et-profession/09-chapitre-68-ethique-rgpd-secret-bancaire-et-limite.md)
    - [Chapitre 69 — Construire une capacité FININT durable](10-partie-x-cas-historiques-cooperation-et-profession/10-chapitre-69-construire-une-capacite-finint-durable.md)
    - [Chapitre 70 — Évolutions réglementaires 2024-2026 : mise à niveau](10-partie-x-cas-historiques-cooperation-et-profession/11-chapitre-70-evolutions-reglementaires-2024-2026-mi.md)
- [Annexes](11-annexes/index.md)
    - [Annexe A — Glossaire opérationnel FININT](11-annexes/01-annexe-a-glossaire-operationnel-finint.md)
    - [Annexe B — Lire un message SWIFT : MT103, MT202, MT940](11-annexes/02-annexe-b-lire-un-message-swift-mt103-mt202-mt940.md)
    - [Annexe C — Modèle de fiche personne](11-annexes/03-annexe-c-modele-de-fiche-personne.md)
    - [Annexe D — Modèle de fiche société](11-annexes/04-annexe-d-modele-de-fiche-societe.md)
    - [Annexe E — Modèle de fiche flux](11-annexes/05-annexe-e-modele-de-fiche-flux.md)
    - [Annexe F — Modèle de fiche actif](11-annexes/06-annexe-f-modele-de-fiche-actif.md)
    - [Annexe G — Matrice des red flags FININT (par typologie)](11-annexes/07-annexe-g-matrice-des-red-flags-finint-par-typologi.md)
    - [Annexe H — Matrice “ce que je peux conclure / ce que je ne peux pas conclure”](11-annexes/08-annexe-h-matrice-ce-que-je-peux-conclure-ce-que-je.md)
    - [Annexe I — Registres et sources par pays](11-annexes/09-annexe-i-registres-et-sources-par-pays.md)
    - [Annexe J — Outils par usage (catalogue raisonné)](11-annexes/10-annexe-j-outils-par-usage-catalogue-raisonne.md)
    - [Annexe K — Modèle de note FININT](11-annexes/11-annexe-k-modele-de-note-finint.md)
    - [Annexe L — Erreurs fréquentes et 5 mini-cas d’entraînement](11-annexes/12-annexe-l-erreurs-frequentes-et-5-mini-cas-dentrain.md)
    - [Annexe M — Cadres d’accès aux sources](11-annexes/13-annexe-m-cadres-dacces-aux-sources.md)
    - [Annexe N — Bibliographie de sources primaires](11-annexes/14-annexe-n-bibliographie-de-sources-primaires.md)
    - [Parcours de lecture recommandés](11-annexes/15-parcours-de-lecture-recommandes.md)
- [Clôture](12-cloture.md)
