---
title: PARTIE IX — CAS PRATIQUES DÉROULÉS
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
chapter: 10
chapters: 11
---

*Cinq cas pratiques fictifs mais réalistes, chacun déroulé comme une enquête complète : contexte → indices → cadrage → collecte → analyse → hypothèses → limites → livrable → bilan honnête. Les cas illustrent les méthodes des parties précédentes et préparent à la pratique. Tous les noms et données sont fictifs.*

-----

## Chapitre 55 — Cas 1 : Société écran et fournisseur suspect

### Contexte

Une grande entreprise française du secteur BTP, **CONSTRUCT FRANCE SA**, fait appel à un cabinet de compliance externe à la suite d’une alerte du contrôle interne : un fournisseur récent, **BTP SERVICES INTERNATIONAL SARL**, basé en France, présente des caractéristiques inhabituelles. La compliance a déjà identifié plusieurs signaux mais sollicite une analyse FININT externe pour qualifier.

**Demande** : qualifier la nature et le risque associés à BTP SERVICES INTERNATIONAL.

### Indices initiaux fournis

- Société française créée 11 mois avant le premier marché avec CONSTRUCT.
- Capital social 1 000 €.
- Dirigeant unique, ancien retraité du secteur agro-alimentaire.
- Domiciliation à un cabinet de domiciliation parisien.
- Aucun site web.
- Volume de prestations facturé sur 6 mois : 1,4 M€.
- Facturations très techniques (sous-traitance gros œuvre, ferraillage, étanchéité).
- Bénéficiaire effectif déclaré au RBE : le dirigeant unique.

### Cadrage initial

**Questions de renseignement** :

- QR1 — La société a-t-elle une activité économique réelle ?
- QR2 — Quel est l’UBO réel ?
- QR3 — Quel est le réseau de relations de cette société ?
- QR4 — Quel est le profil de risque (fraude fiscale, ABS, blanchiment, fronting) ?

**Budget temps estimé** : 2 semaines.

**Limites prévisibles** : sans réquisition, accès limité aux relevés bancaires et à la comptabilité détaillée.

### Collecte

**OSINT registres** :

- Pappers + INPI + Companies House (rien à l’étranger). SIREN, K-bis, statuts, comptes (1er exercice non clos).
- Recherche par dirigeant : la personne est gérante d’une seule société. Pas multi-mandats. Mais profil incohérent (retraité agro vs gros œuvre).
- BODACC : pas de procédure.

**OSINT divers** :

- LinkedIn du dirigeant : profil très minimal, aucune photo, aucune mention BTP.
- Adresse de domiciliation : 32 autres entités à la même adresse. Variées, peu de cohérence sectorielle.

**Sources adjacentes** :

- Le dirigeant a un fils. Recherche par nom : le fils, M. R, dirige une autre société de BTP en région parisienne, **R-CONSTRUCT SARL**, qui a connu une procédure collective il y a 3 ans (liquidation pour passifs URSSAF et fiscaux).
- Croisement : l’adresse personnelle déclarée par M. R correspond à celle du père (domiciliation familiale plausible).
- Recherche presse : un article local de 2021 mentionne un dossier de fraude TVA en BTP impliquant plusieurs sociétés en lien avec M. R (instruction en cours à l’époque ; pas d’information sur la suite).

**Compliance interne CONSTRUCT (partagé)** :

- Sur 6 mois, BTP SERVICES INTERNATIONAL a facturé 1,4 M€ à CONSTRUCT pour des prestations dont la traçabilité physique (présence de personnel sur chantier, signatures pointage) est faible voire absente.
- Les factures ont été acquittées par virements vers un compte de la société à la Banque XX (France).

### Analyse

**Substance économique** : faible. Pas de personnel déclaré (URSSAF non accessible à l’externe), pas de matériel, pas de présence opérationnelle visible. Le dirigeant officiel n’a aucune compétence visible en BTP.

**UBO réel probable** : *probable* que M. R (le fils) soit l’UBO réel, via prête-nom paternel. Indices convergents : profil incohérent du dirigeant officiel, historique BTP de M. R, contentieux antérieur de M. R, adresse partagée, période de création (un an après la liquidation de R-CONSTRUCT — délai typique de reconstruction sous nouveau nom).

**Typologie probable** : compatible avec **fronting** (M. R, ayant des contentieux et difficultés antérieures, utilise une société au nom du père pour continuer ses activités) **et/ou** avec un schéma de **facturation fictive** au profit de CONSTRUCT (rétrocommissions, mise à disposition de travail au noir, fraude URSSAF). Sans accès aux relevés et au pointage de chantier, distinction *indéterminable* à ce stade.

### Hypothèses calibrées

- **H1 — Fronting + activité réelle (M. R reprend une activité légale via prête-nom paternel)** : probable.
- **H2 — Facturation fictive et travail dissimulé** : possible à probable.
- **H3 — Schéma de blanchiment** : peu probable au vu des éléments (les flux sont entrants depuis CONSTRUCT, pas d’origine externe suspecte).
- **H4 — Société écran à finalité de carrousel TVA** : peu probable (pas de cycle observable, profil mono-client).

### Limites

- Sans réquisition des relevés bancaires et des pointages de chantier, impossible de distinguer H1 de H2.
- Sans accès aux déclarations URSSAF, impossible de qualifier le travail dissimulé.
- L’UBO réel = M. R reste *probable*, pas *quasi-certain*.

### Livrable

Rapport au client (CONSTRUCT) :

- Société présentant *probable* fronting.
- Risque de facturation fictive ou de travail dissimulé : *possible à probable*.
- Recommandations :
  - **Rupture progressive** de la relation commerciale, avec mention explicite du risque dans le dossier compliance.
  - **Plainte au procureur de la République** (article 40 CPP ne s’applique pas à une entreprise privée, mais une plainte est ouverte à toute personne morale victime ou témoin d’infractions) si éléments suffisants de facturation fictive ou d’escroquerie au préjudice de CONSTRUCT.
  - **Signalement à l’inspection du travail** pour le volet travail dissimulé.
  - **Signalement à l’URSSAF** et à la **DGFiP** selon les indices.
  - **Important** : une entreprise du BTP comme CONSTRUCT n’est **pas, en principe, assujettie LCB-FT** au sens du Code monétaire et financier. La déclaration de soupçon à TRACFIN concerne les **assujettis** (banques, PSP, notaires, certaines professions). CONSTRUCT ne peut donc pas faire de DS TRACFIN ; ses signalements passent par les voies évoquées ci-dessus (plainte, inspection, URSSAF, DGFiP). C’est sa **banque** qui, le cas échéant, sera assujettie et susceptible de produire une DS sur les flux observés.
  - **Audit interne** sur les processus de KYB fournisseurs.

### Bilan honnête

L’enquête a permis de qualifier rapidement (2 semaines) un fournisseur à risque, sans coût ni outils professionnels lourds (gratuits : Pappers, Companies House, BODACC, LinkedIn, presse locale, recherches d’état civil partielles). La qualification reste à un niveau *probable* — la confirmation *quasi-certaine* exigerait des éléments accessibles seulement en cadre judiciaire ou inspection. C’est une qualification utile à CONSTRUCT : suffit à motiver des décisions internes (rupture commerciale, signalement) sans engager judiciairement CONSTRUCT au-delà de ses obligations.

### Leçons FININT

- **Le profil du dirigeant** est souvent un signal de premier ordre. Un retraité agro à la tête d’une société de gros œuvre = signal fort.
- **L’antériorité familiale ou relationnelle** : un fronting via parent est un classique.
- **La cohérence sectorielle** : 32 entités domiciliées au même cabinet sans cohérence sectorielle = signal de cluster suspect.
- **Limites d’OSINT** : sans réquisition, on s’arrête à *probable*. C’est suffisant pour motiver une rupture commerciale ; insuffisant pour qualifier judiciairement.

-----

## Chapitre 56 — Cas 2 : Fraude au changement d’IBAN / BEC

### Contexte

Une PME française du secteur agroalimentaire, **ALPHA INDUSTRIE SARL**, 28 employés, 6 M€ de CA annuel, est victime d’une fraude au virement le mardi 14 mars. Montant : **215 000 €**. La fraude est découverte le mercredi matin lors d’un appel du vrai fournisseur réclamant son paiement.

ALPHA dépose plainte le mercredi 15 mars matin et saisit son cabinet d’avocats. Le cabinet sollicite une expertise FININT pour le volet traçage et reconstitution.

**Demande** : reconstituer la séquence, identifier les acteurs, évaluer les chances de récupération, préparer les éléments pour la procédure judiciaire et la coopération internationale.

### Indices initiaux fournis

- Le directeur financier d’ALPHA a reçu, le lundi 13 mars à 17h30, un email apparemment du dirigeant d’un fournisseur habituel (entreprise espagnole **TAIDA SL**), signalant un changement d’IBAN pour la prochaine facture.
- Le mardi 14 mars à 14h32, paiement effectif via SCT Inst de 215 K€ vers l’IBAN ES indiqué (compte au nom d’**IBERICA TRADING SL**, société espagnole).
- Le mercredi 15 mars vers 9h, le vrai TAIDA SL appelle ALPHA pour réclamer le paiement.
- L’examen de l’email frauduleux montre un domaine très proche du vrai TAIDA (typosquatting : `taida-sl.es` vs vrai `taidasl.es`).
- La banque d’ALPHA a tenté un rappel SCT Inst : refusé (compte récepteur a accepté l’opération ; SCT Inst irréversible sans accord).

### Cadrage initial

**Questions de renseignement** :

- QR1 — Reconstituer la séquence en aval (où sont allés les 215 K€ ?).
- QR2 — Identifier l’attaquant (groupe organisé, isolé, niveau d’expérience).
- QR3 — Quels leviers pour récupération partielle ?
- QR4 — Quelles coopérations engager ?

**Budget temps** : 1 semaine pour le cœur du travail, plus suivi.

**Limites prévisibles** : sans réquisitions des banques étrangères, traçage des comptes étrangers limité. Volet crypto à confier à Athéna Group / OSINT Crypto.

### Collecte

**OSINT sur IBERICA TRADING SL** :

- Registre espagnol (RMC) : société créée 4 mois avant les faits. Capital 3 000 €. Activité déclarée : « commerce de gros divers ». Dirigeant unique : un national espagnol d’environ 35 ans, sans expérience commerciale antérieure visible.
- Adresse : domiciliation à Madrid.
- Pas de site web. Pas de présence en ligne.
- Lecture : *probable* société de mule / shell créée pour l’opération.

**Compliance bancaire (via avocats)** :

- La banque d’IBERICA en Espagne, sollicitée, indique des transferts sortants rapides après le crédit de 215 K€.
- Détail (partiel, sous le cadre coopération européenne) :
  - 14h35-14h41 : 5 SCT Inst sortants depuis IBERICA vers 5 IBAN distincts (3 au Portugal, 2 en Lituanie).
  - Chaque sortie : 40 000 € à 45 000 €.
  - Bénéficiaires : 5 comptes ouverts récemment dans 3 banques différentes (Revolut LT, Wise via BE, et 3 banques portugaises moyennes).

**OSINT sur les 5 destinataires** : tous sont des personnes physiques (apparemment), avec profils minimaux. Aucun lien apparent entre elles. *Probable* réseau de mules.

**Volet crypto (confié à Sarah Marin / Athéna Group)** :

- Sur les 5 comptes en aval (LT, PT), 4 sur 5 ont rapidement (16h12-16h18) effectué des dépôts USDT sur un exchange A (basé hors UE, profil KYC ambigu).
- Les USDT sont sortis dans l’heure vers un wallet auto-géré, puis fragmentés via plusieurs adresses.
- Le rapport on-chain Athéna identifie une convergence : plusieurs des adresses finales correspondent à un cluster connu de cashout opérant sur des exchanges asiatiques non-KYC.
- *Quasi-certaine* attribution du cashout à un réseau organisé, mais identification individuelle des attaquants reste *indéterminable* au niveau on-chain seul.

### Analyse

**Reconstitution de la séquence** :

```
T-48h (lundi 17h30) : email frauduleux reçu par DF ALPHA, taida-sl.es (typosquat).
T-0   (mardi 14h32) : SCT Inst ALPHA → IBERICA, 215 K€.
T+3min                : Fractionnement IBERICA → 5 IBAN (PT, LT), 40-45 K€ chacun.
T+1h40                : Dépôts USDT sur exchange A par 4 des 5 comptes.
T+2h45                : Sorties USDT vers wallet auto-géré.
T+4h15                : Fragmentation crypto, convergence vers cluster cashout asiatique.
T+18h (mercredi 9h)   : ALPHA découvre la fraude.
```

**Acteurs et rôles** :

- Attaquant initial : auteur de l’email, *probable* groupe organisé (la sophistication du typosquatting + la connaissance du nom du fournisseur réel + le timing avec date de facturation suggèrent un repérage préalable).
- IBERICA TRADING SL : société écran de réception (mule de premier niveau).
- 5 comptes en aval : mules de deuxième niveau.
- Cluster cashout asiatique : infrastructure de monétisation.

**Typologie** : BEC avec layering rapide multi-PSP et cashout crypto. Schéma classique 2023-2025.

### Hypothèses calibrées

- BEC : quasi-certain.
- Réseau de mules organisé : quasi-certain.
- Attribution à un groupe spécifique : indéterminable au niveau du cabinet ; CTI / coopérations internationales nécessaires.
- Récupération totale : peu probable. Récupération partielle (50 000 € à 80 000 € si action très rapide sur comptes ES et PT non encore vidés) : possible.

### Limites

- Identification précise des attaquants : *indéterminable* au niveau de l’enquête privée. Reste à l’enquête judiciaire et aux coopérations internationales (Europol EC3, INTERPOL).
- Récupération crypto : la portion convertie en USDT est *peu probable* à récupérer (cashout déjà effectué dans des juridictions à faible coopération).
- La portion encore en comptes ES/PT (si non vidés) : *possible* à geler par requête judiciaire urgente, avec saisine du parquet européen via le PNF si applicable.

### Livrable

Rapport au client (ALPHA, via le cabinet d’avocats) :

- Reconstitution de la séquence.
- Cartographie des comptes et des juridictions.
- Pour la procédure : éléments à transmettre au parquet (déjà saisi par la plainte).
- Pour la récupération : actions immédiates (saisine du parquet européen pour gel des comptes ES et PT non vidés ; coopération via FIU.NET pour les comptes LT).
- Pour les leçons : audit des procédures internes (process de validation des changements d’IBAN, double signature, vérification téléphonique).

### Bilan honnête

La fraude est constatée. La portion fiat (encore en comptes ES/PT) peut être partiellement gelée si action très rapide (24-48h après dépôt de plainte) — en pratique, les délais administratifs et judiciaires ramènent souvent ces espoirs à 10-25 % de récupération réelle. La portion crypto (~75 % du montant) est *quasi-certainement* perdue. L’identification des attaquants est *indéterminable* au niveau du cabinet ; elle dépend des coopérations internationales et des renseignements policiers (cluster connu = identification *possible* avec temps et coopération).

Le travail FININT et OSINT Crypto a un double rôle : (1) tenter de sauver la partie fiat encore mobilisable, (2) alimenter la procédure judiciaire et les coopérations pour démantèlement à terme du réseau.

### Leçons FININT

- **La vitesse est centrale.** Au-delà de 24h, la majorité des fonds est partie.
- **FININT et OSINT Crypto se complètent.** Le partage du dossier est efficace.
- **Les mules ne sont pas l’objectif final** : elles sont des indicateurs vers les organisateurs.
- **Récupération vs identification** : deux objectifs différents, qui exigent des actions différentes.
- **Prévention vaut récupération** : un audit des procédures préviendrait l’écrasante majorité des BEC.

-----

## Chapitre 57 — Cas 3 : Corruption internationale et PEP

### Contexte

Une banque privée européenne, **BANQUE-PARTNER** (fictive), procède à un examen LCB-FT approfondi d’un compte client significatif. Le client, **M. KAMBOU**, est un ancien ministre d’un pays d’Afrique de l’Ouest (statut PEP confirmé). Le compte présente une activité importante depuis 18 mois : crédits totaux de 12 M€ provenant de diverses sources internationales, débits vers immobilier européen et fonds d’investissement.

La banque, en application de la vigilance renforcée PEP, mandate un cabinet de conformité pour une **due diligence approfondie**.

**Demande** : qualifier la cohérence des fonds avec le profil et l’historique professionnel du client, identifier risques de corruption et recommander des suites.

### Indices initiaux

- M. KAMBOU, ministre de l’Économie pendant 6 ans, sorti de fonctions il y a 4 ans.
- Patrimoine déclaré à l’entrée en relation : ~3,5 M€.
- Sources de revenus déclarées : conseils stratégiques pour des entreprises africaines et européennes, plus quelques participations.
- Comptes : ouverts depuis l’année qui a suivi la sortie des fonctions. Activité progressivement croissante.

### Cadrage initial

**Questions de renseignement** :

- QR1 — Origine des fonds : conseils légitimes ou rétrocommissions de fonctions antérieures ?
- QR2 — Quel est le profil PEP étendu (famille, collaborateurs étroits) ?
- QR3 — Y a-t-il des liens visibles avec des marchés publics du pays d’origine ?
- QR4 — Quelle qualification du compte (à approfondir, rupture, signalement) ?

### Collecte

**Sources ouvertes** :

- Wikipédia, presse africaine et internationale : parcours politique, déclarations de patrimoine durant le mandat, controverses éventuelles.
- Bases PEP commerciales (World-Check) : confirmation statut PEP, famille étendue identifiée (épouse, 3 enfants, plusieurs proches collaborateurs identifiés).
- Registres d’entreprises : sociétés détenues par M. KAMBOU et ses proches, locales et internationales.
- Pandora Papers : recherche par nom (et variantes) → 2 résultats : un trust enregistré à Jersey, contributeur M. KAMBOU, bénéficiaires sa famille étendue. Date de création : 6 mois avant la sortie de fonctions.
- Marchés publics du pays d’origine : presse, rapports d’organisations internationales (Transparency International, Global Witness, OECD Working Group). Plusieurs grands marchés (mines, infrastructures) attribués pendant le mandat de M. KAMBOU à des consortia étrangers.

**Adverse media** :

- 3 articles d’investigation (OCCRP, Reuters, presse locale) mentionnent M. KAMBOU dans le contexte de l’attribution de marchés contestés, sans poursuites formelles à ce stade.

**Profilage des sources de revenus déclarées (« conseil ») **:

- Sociétés clientes identifiées : 4 entités basées dans des juridictions de holding (Maurice, Luxembourg, Émirats). UBO de 2 de ces entités : liés à des consortia ayant remporté des marchés publics pendant le mandat de M. KAMBOU.

### Analyse

**Cohérence revenus / activité de conseil** :

- Les « conseils » facturés totalisent 8 M€ sur 18 mois, à 4 entités.
- Aucune des entités clientes n’a de site web ni d’activité opérationnelle traçable autre que des participations dans les consortia.
- Les montants des facturations sont disproportionnés par rapport à un conseil stratégique standard.
- Lecture : *probable* mécanisme de rétrocommissions différé, où les bénéficiaires de marchés publics rémunèrent l’ancien ministre par contrat de conseil après sortie de fonctions.

**Lien avec marchés publics** :

- 2 des 4 entités clientes sont liées à des consortia ayant remporté des marchés publics sous le mandat de M. KAMBOU pour des valeurs cumulées > 200 M$.
- La temporalité est cohérente avec un schéma de rétrocommissions.

**Patrimoine actuel** :

- Patrimoine déclaré à l’entrée : 3,5 M€.
- Crédits cumulés sur 18 mois : 12 M€.
- Sortie majeure : 6,8 M€ vers immobilier européen (Suisse, Sud de la France, Londres).
- Solde actuel : ~4 M€ sur le compte + actifs financiers ~5 M€ + immobilier 6,8 M€ = ~15 M€.
- Évolution : patrimoine multiplié par > 4 en 4 ans hors-mandat.

### Hypothèses calibrées

- **H1 — Rétrocommissions différées (corruption transnationale latente)** : probable.
- **H2 — Conseil stratégique légitime, à très haute valeur ajoutée** : peu probable, vu l’absence de traçabilité de l’activité de conseil réelle et la corrélation temporelle avec les marchés.
- **H3 — Combinaison de sources légitimes et illicites** : possible.

### Limites

- Sans coopération internationale (notamment via Egmont avec la CRF du pays d’origine), la qualification définitive est *indéterminable*.
- La présomption d’innocence demeure : M. KAMBOU n’a pas été condamné.
- Les contrats de conseil peuvent être légalement formalisés, ce qui complique la qualification pénale.

### Livrable

Rapport à la banque BANQUE-PARTNER :

- Le profil et l’activité du compte sont *probable* compatibles avec un schéma de rétrocommissions de corruption transnationale antérieures.
- Recommandations :
  - **Déclaration de soupçon à la CRF nationale** (TRACFIN équivalent local) : suffisamment d’éléments pour DS.
  - **Vigilance renforcée maximale** : limitation des opérations, demandes systématiques de justificatifs.
  - **Évaluer la rupture** de la relation d’affaires : décision banque selon politique interne et avis juridique.
  - **Coopérations Egmont** : la CRF pourra solliciter la CRF du pays d’origine pour qualifier les marchés publics.

### Bilan honnête

Une enquête de due diligence approfondie ne **prouve pas** la corruption. Elle qualifie un **profil de risque** avec un niveau de confiance *probable* à élevé. La décision opérationnelle (rupture, signalement, vigilance) appartient à la banque. La qualification judiciaire éventuelle relève de la procédure pénale dans le pays d’origine ou via Convention OCDE Anti-Corruption (1997).

### Leçons FININT

- Le **statut PEP** déclenche une vigilance, pas une accusation.
- La **temporalité** (sortie de fonctions → début de l’activité de conseil → flux entrants des bénéficiaires de marchés) est centrale.
- **Pandora et leaks** sont essentiels pour les volets offshore.
- La banque, dans ce cas, est **assujetti** et a une obligation de DS si soupçon ; le cabinet conseille mais ne décide pas.

-----

## Chapitre 58 — Cas 4 : Contournement de sanctions via pays tiers

### Contexte

Une banque française, **BANQUE-X**, identifie via son monitoring un client commercial atypique : une SAS française récemment créée, **EUROFLUX SARL**, qui présente une explosion d’activité avec une contrepartie turque. Les flux sont importants (~3 M€ sur 2 mois) et la nature des opérations (négoce de matériel industriel sensible) attire l’attention.

La compliance déclenche une analyse FININT interne et sollicite TRACFIN via DS.

**Demande (interne CRF)** : qualifier le profil de risque, vérifier la possibilité d’un contournement de sanctions, recommander des suites.

### Indices initiaux

- EUROFLUX SARL : créée 5 mois avant les premiers flux. Capital 5 K€. Dirigeant : un Français, 30 ans, parcours professionnel principalement dans la logistique générale.
- Contrepartie turque : ATLAS TECHNICAL TRADING (société turque créée 7 mois plus tôt).
- Flux observés : 3 M€ entrants depuis ATLAS, libellés « industrial equipment » et « technical components ».
- Sorties : achats auprès de fournisseurs européens (Allemagne, Italie, Pays-Bas) de matériel électronique sensible (CNC, composants industriels avancés).
- Destinations finales déclarées : exports vers Turquie (déclarations douanières).

### Cadrage

**Questions de renseignement** :

- QR1 — Quel est le profil réel d’EUROFLUX et d’ATLAS ?
- QR2 — Les biens commercialisés sont-ils dual-use ?
- QR3 — Y a-t-il un soupçon de réexportation vers une juridiction sanctionnée ?
- QR4 — Quels UBO et liens entre EUROFLUX, ATLAS, et éventuelles entités sanctionnées ?

### Collecte

**OSINT** :

- Pappers : EUROFLUX dirigée par M. T, sans expérience visible dans le secteur. UBO RBE : M. T lui-même.
- Recherche M. T : LinkedIn minimal, pas de réseau apparent dans la tech industrielle.
- Adresse EUROFLUX : cabinet de domiciliation parisien, 21 autres entités.
- Recherche ATLAS Technical Trading (Turquie) : registre turc accessible — UBO turc, M. Ö, 45 ans, parcours dans le négoce général à Istanbul.
- Recherche presse : ATLAS est mentionnée dans un article OCCRP de 2024 sur des sociétés turques utilisées pour acheminement de biens vers la Russie (sanctions UE et US).

**Sanctions et listes** :

- M. Ö (UBO d’ATLAS) : pas sur les listes OFAC, UE, OFSI.
- ATLAS : pas sur les listes.
- Sociétés liées (recherche par M. Ö) : plusieurs sociétés dirigées par M. Ö, dont une avait des liens commerciaux antérieurs avec une entreprise russe **désormais sanctionnée** depuis 2022.

**Nature des biens** :

- Liste détaillée des achats EUROFLUX auprès des fournisseurs européens : composants CNC, contrôleurs PLC, certains équipements de capteurs.
- Vérification dual-use : plusieurs des composants sont sur la **liste UE dual-use** (règlement 2021/821), exigeant licence d’exportation pour certaines destinations.

**Vérification douanière** :

- Déclarations douanières françaises : exports vers Turquie déclarés.
- Pas de vérification immédiate de la destination réelle après Turquie.

### Analyse

**Profil EUROFLUX** : société créée récemment, dirigeant inexpérimenté, domiciliation, faible substance économique propre. *Probable* société écran ou opérationnelle pour un schéma spécifique.

**Profil ATLAS** : société turque créée récemment, mais avec un UBO qui a des liens antérieurs (sociétés liées) avec une entreprise russe désormais sanctionnée.

**Schéma probable** : EUROFLUX achète en Europe des biens dual-use, vend à ATLAS en Turquie. ATLAS réexporte (potentiellement) vers une destination sanctionnée (probablement Russie). Le schéma est typique d’un **contournement de sanctions UE/US** via pays tiers.

**Éléments confortants** :

- Nature des biens (dual-use).
- Lien historique UBO ATLAS / entité russe sanctionnée.
- Volume soudain (3 M€ en 2 mois pour une société de 5 K€ de capital).
- Pas d’activité économique antérieure d’EUROFLUX cohérente avec le secteur.

### Hypothèses calibrées

- **H1 — Contournement de sanctions UE/US via pays tiers (Turquie)** : probable.
- **H2 — Schéma de commerce parallèle légal mais douteux** : possible.
- **H3 — Pure activité commerciale Europe-Turquie** : peu probable au vu de la nature des biens et du profil ATLAS.

### Limites

- Sans vérification de la destination réelle après Turquie, le contournement reste *probable*, pas *quasi-certain*.
- Coopération douanière France-Turquie est complexe (Turquie n’est pas dans l’UE).
- Le volet renseignement avec services spécialisés (DG Trésor pôle sanctions, DGDDI, équivalent dans services de défense) est central.

### Livrable

Note FININT interne CRF + signalement :

- Profil de risque *probable* de contournement de sanctions, biens dual-use.
- Recommandations :
  - DS validée et enrichie, transmission au PNF (équivalent fiction).
  - Saisine immédiate de la DG Trésor (pôle sanctions financières) (Direction Générale du Trésor — sanctions) et des services douaniers (DGDDI).
  - Coopération Egmont avec la CRF turque pour qualifier ATLAS et son réseau.
  - Possibilité de gel administratif si éléments suffisants confirment l’attribution sanctionnée.

### Bilan honnête

Le contournement de sanctions est une typologie particulièrement sensible. La qualification définitive est souvent **politique** autant que judiciaire. Le rôle de la CRF est de produire un dossier solide et de saisir les autorités spécialisées. Les sanctions secondaires OFAC (impact sur les opérateurs européens) ajoutent une dimension géopolitique. Le dossier peut conduire à des suites variées : enquête judiciaire en France, sanctions sur les acteurs (gel), pression diplomatique sur la Turquie pour coopération.

### Leçons FININT

- **Pays tiers** (Turquie, Émirats, Géorgie, Arménie, Asie centrale) sont des canaux d’attention prioritaire depuis 2022.
- **Biens dual-use** : connaître la liste UE, qui est mise à jour régulièrement.
- **UBO et liens passés** : un UBO non sanctionné mais lié historiquement à une entité sanctionnée = signal majeur.
- **Coordination inter-services** : sanctions ≠ FININT seul. DG Trésor (pôle sanctions financières internationales), DGDDI, MAE, parfois services de défense interviennent.

-----

## Chapitre 59 — Cas 5 : Asset tracing d’un dirigeant sous enquête

### Contexte

Un magistrat instructeur français saisit, par réquisition, une cellule spécialisée pour l’**asset tracing** d’un dirigeant français, **M. RIVIÈRE**, mis en examen pour escroquerie aggravée à hauteur de 15 M€. Le magistrat soupçonne une dissipation patrimoniale en cours et souhaite **identifier les actifs susceptibles d’une mesure conservatoire** (gel, saisie).

L’enquête a déjà identifié les flux frauduleux principaux et certains comptes bancaires français. Mais le patrimoine étranger et les structures offshore éventuelles restent à identifier.

**Demande** : asset tracing complet pour mesure conservatoire urgente.

### Indices initiaux

- M. RIVIÈRE, 55 ans, ancien dirigeant d’une PME en redressement.
- Mises en cause : ventes fictives via faux clients, fraude TVA et abus de biens sociaux. Préjudice estimé 15 M€.
- Comptes français : 6 comptes identifiés, soldes cumulés actuels ~280 K€. *Insuffisant* pour mesure conservatoire significative.
- Patrimoine français déclaré (déclarations fiscales) : 2 résidences, 1 SCI, ~2 M€ valeur.
- Signaux : voyages réguliers à Dubaï et Genève depuis 18 mois, train de vie présomé supérieur au patrimoine déclaré.

### Cadrage

**Questions de renseignement** :

- QR1 — Quels actifs cachés ou indirects ? Immobilier étranger ? Comptes étrangers ? Structures offshore ?
- QR2 — Y a-t-il des prête-noms ou des structures interposées ?
- QR3 — Quelle est la trajectoire récente du patrimoine (dissipation ? consolidation ?) ?
- QR4 — Quels actifs sont juridiquement susceptibles de mesure conservatoire ?

**Délai** : 4 semaines (mesure conservatoire à décider rapidement).

### Collecte

**Sources ouvertes** :

- DVF + cadastre : identification des biens français.
- Pappers : sociétés détenues par M. RIVIÈRE et ses proches.
- LinkedIn + presse + réseaux sociaux : profilage, identification de relations et de localisations.
- Patrim (accessible CRF) : revenus et patrimoine déclarés.
- Reverse image search : identification du yacht visible sur Instagram.

**Sources fermées (en cadre judiciaire)** :

- FICOBA : tous les comptes bancaires en France au nom de M. RIVIÈRE et de ses proches identifiés.
- FICOVIE : assurances-vie.
- EAR/CRS (via demande administrative en coopération avec DGFiP) : comptes étrangers déclarés.
- Réquisitions auprès de banques françaises : relevés détaillés.

**Coopérations internationales** :

- Egmont avec MROS (Suisse) : confirmation d’1 compte privé à Genève, soldes et historiques.
- Egmont avec CRF émiratie : identification de 2 sociétés free zone (Dubaï) liées à un proche collaborateur — *probable* UBO M. RIVIÈRE via prête-nom.
- Recherche presse mondaine : photos de M. RIVIÈRE devant un appartement à Dubaï (identifiable au quartier).

### Analyse

**Cartographie patrimoniale consolidée** :

```
France
├─ 2 résidences (déclarées) — 2 M€
├─ SCI (déclarée) — 1 M€
├─ 6 comptes bancaires — 280 K€
└─ 2 contrats assurance-vie — 850 K€

Suisse
└─ 1 compte banque privée Genève — 3,2 M€ (EAR/CRS + coop MROS)

Émirats
├─ 1 LLC Dubaï détentrice apparente d'un appartement à Dubaï Marina — valeur estimée ~1,8 M€
├─ 1 autre LLC sans actifs clairs — possible société écran
└─ Pas d'autres comptes identifiés à ce stade

Yacht
└─ Pavillon Malte, valeur estimée 1,2 M€, propriété via société écran maltaise

Total identifié : ~10,4 M€ (vs préjudice 15 M€).
```

**Dissipation observable** : sur les 6 derniers mois (post-mise en examen), virements totaux de 1,8 M€ depuis comptes français vers Suisse et Dubaï. *Probable* dissipation active.

### Hypothèses calibrées

- M. RIVIÈRE détient une fraction significative des fonds frauduleux dans des structures étrangères : quasi-certain.
- Une partie du patrimoine identifié (Suisse, Dubaï, yacht) est saisissable sous procédure judiciaire et coopérations internationales : probable.
- Dissipation active en cours : quasi-certain.

### Livrable

Rapport au magistrat instructeur :

- Cartographie patrimoniale consolidée : ~10,4 M€ identifiés.
- Actifs prioritaires pour mesures conservatoires :
  - France : saisine AGRASC pour gel et saisie des biens immobiliers et comptes.
  - Suisse : demande d’entraide pour gel via MROS et coopération judiciaire.
  - Émirats : demande d’entraide judiciaire (plus complexe et plus longue).
  - Yacht : possible saisie sous pavillon Malte (coopération MLA).
- Recommandation d’urgence : geler immédiatement les comptes français pour stopper la dissipation, puis enchaîner les coopérations internationales en parallèle.

### Bilan honnête

L’asset tracing a permis d’identifier ~10,4 M€ d’actifs (vs 15 M€ de préjudice). Le recouvrement réel dépend de :

- Réactivité des autorités (gel français immédiat).
- Vitesse des coopérations internationales (Suisse rapide, Émirats lent, Malte intermédiaire).
- Qualité juridique du dossier d’enquête (la mesure conservatoire repose sur la solidité de l’enquête pénale).

Récupération espérée : une **fraction significative** du patrimoine identifié si action rapide et coopération satisfaisante, sur le préjudice global, le recouvrement est **structurellement partiel**, sur 18 à 36 mois ou plus. Les ordres de grandeur donnés dans le cours sont **pédagogiques** ; la réalité varie fortement selon les juridictions, la qualité du dossier judiciaire, la coopération et les stratégies de protection adverses.

### Leçons FININT

- L’**asset tracing** combine OSINT (signaux visibles), sources fermées (FICOBA, EAR/CRS), et coopération internationale.
- La **rapidité** d’action conditionne le résultat (dissipation possible en parallèle).
- La **coopération avec AGRASC** en France et équivalents étrangers est indispensable.
- Les juridictions varient en réactivité : Suisse, UK, Allemagne sont relativement coopératifs ; Émirats, Asie, Liban beaucoup moins.

-----
