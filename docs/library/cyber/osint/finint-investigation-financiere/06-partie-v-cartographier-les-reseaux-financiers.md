---
title: PARTIE V — CARTOGRAPHIER LES RÉSEAUX FINANCIERS
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
chapter: 6
chapters: 11
---

*Sept chapitres pour transformer les données collectées en livrables structurés : fiches par type d’objet, graphes relationnels, qualification des liens, calibration de la confiance. C’est le passage de la collecte brute à l’analyse présentable.*

-----

## Chapitre 27 — Construire une fiche personne

### Objectif du chapitre

Maîtriser la **fiche personne FININT** : structure standardisée pour consolider, en un livrable réutilisable, tous les éléments collectés sur une personne physique. Le modèle complet est en annexe C ; ce chapitre expose la logique et les choix méthodologiques.

### Le concept

Une fiche personne est un livrable **atomique** : elle concentre, sur une personne, l’ensemble des éléments d’identification, de profil, de mandats, de patrimoine, de relations et de contentieux. Elle est conçue pour être :

- **Autonome** : lisible sans contexte préalable.
- **Sourcée** : chaque élément factuel renvoie à sa source.
- **Calibrée** : niveau de confiance pour chaque élément non trivial.
- **Versionnée** : date de production, date de dernière mise à jour, version.
- **Actionnable** : conclusions et recommandations en fin.

### Structure type d’une fiche personne

1. **En-tête** : référence, date, version, classification (TLP), auteur.
1. **Identification** : nom complet, date de naissance, lieu, nationalité(s), adresse(s), photo si disponible. Niveau de confiance global de l’identification.
1. **Profil** : parcours professionnel, formation, langues parlées (signaux d’enquête utiles), affiliations professionnelles, fonctions publiques antérieures, profil PEP éventuel.
1. **Mandats actuels** : liste des sociétés où la personne exerce un mandat, avec rôle, juridiction, période.
1. **Mandats antérieurs** : historique.
1. **UBO et contrôle indirect** : entités où la personne est UBO identifié, déclaré ou *probable*.
1. **Patrimoine identifié** : immobilier, financier, actifs particuliers (œuvres, véhicules, bateaux, etc.), train de vie observable.
1. **Réseau** : famille proche, collaborateurs réguliers, associés, personnes clés du dossier.
1. **Contentieux et réputation** : procédures publiques, condamnations, sanctions, adverse media.
1. **Sanctions et PEP** : présence sur listes, statut PEP, vérifications screening.
1. **Liens crypto** (si pertinent) : adresses ou attributions on-chain — renvoi vers OSINT Crypto pour le traitement détaillé.
1. **Hypothèses calibrées** : ce que l’analyste retient sur cette personne, avec niveaux de confiance.
1. **Sources** : liste exhaustive avec dates.
1. **Lacunes et actions complémentaires** : ce qui n’a pas pu être établi, et comment le faire.

### L’utilité opérationnelle

La fiche personne est **réutilisable** : produite une fois, elle alimente plusieurs livrables (note FININT, dossier d’enquête, dossier compliance). Elle est **interopérable** : un format standardisé permet à différents analystes de se transmettre l’information sans perte.

Elle est aussi un **outil de discipline** : la rédiger oblige à expliciter ce qu’on sait et ce qu’on ne sait pas. C’est un puissant antidote aux conclusions précipitées.

### Méthode — bonnes pratiques

- **Ne pas confondre fiche et résumé** : la fiche est exhaustive sur ce qui est connu, pas un résumé.
- **Sourcer chaque élément** : pas d’affirmation sans référence.
- **Calibrer chaque conclusion** : niveau de confiance.
- **Distinguer mandat déclaré et contrôle réel**.
- **Respecter la présomption d’innocence** : un mis en examen n’est pas un coupable.
- **Mentionner les lacunes** : la fiche ne fait pas semblant de tout savoir.

### Mini-walkthrough — fiche Karim Haddad (extrait)

```
FICHE PERSONNE — KARIM ÉLIE HADDAD
Référence : CLEARFLOW/PER/001 | v1.3 | 14/03 | TLP:AMBER

IDENTIFICATION (quasi-certain)
- Né le 17/04/1968 à Beyrouth, Liban
- Nationalités : libanaise (par naissance), française (par naturalisation, 2006)
- Adresses : Paris 16e (résidence principale déclarée), Beyrouth (Achrafieh), Dubaï (DIFC apartments)
- Photo : LinkedIn, presse libanaise 2023

PROFIL (probable)
- Diplômé ESCP Paris (1992), parcours négoce international depuis 1995
- Langues : arabe, français, anglais
- Pas de fonction publique connue
- Pas de statut PEP au sens strict
- Affiliation : Chambre de commerce franco-libanaise (membre actif)

MANDATS ACTUELS DÉCLARÉS (quasi-certain)
- NEXUS LIBAN SAL — administrateur (Liban, depuis 2002)
- NEXUS INTERNATIONAL FZ — propriétaire (Émirats, free zone)
- (aucun mandat déclaré dans les 4 SAS françaises ni dans les 2 Limited UK)

UBO PROBABLE OU IDENTIFIÉ
- OMEGA HOLDINGS TRUST (Chypre) — settlor identifié via Pandora (quasi-certain)
- NEXUS HOLDINGS LTD (Chypre) — UBO probable via chaîne (probable)
- 4 SAS françaises — UBO réel probable via prête-noms (probable)
- LLC Delaware — non confirmé (indéterminable)
- (autres entités, voir fiche groupe)

PATRIMOINE IDENTIFIÉ
- Immobilier : 3 biens à Paris (SCI), 1 villa à Beyrouth, présence à Dubaï (location non confirmée)
- Financier : participations dans le groupe, comptes bancaires en France, présomé en Suisse (DS)
- Train de vie : voyages réguliers Paris-Beyrouth-Dubaï-Genève, événements caritatifs au Liban

RÉSEAU
- Famille : épouse française, 3 enfants. Frère installé à Dubaï (lien d'affaires).
- Collaborateurs identifiés : M. Y (Dubaï, dirigeant déclaré Limited UK), Mme Z (présidente d'une SAS, lien personnel)

CONTENTIEUX ET RÉPUTATION
- Transaction fiscale française 2018 (sans poursuite pénale ; presse)
- Aucune condamnation publique
- Adverse media : présence dans presse régionale, allégations 2023 (Côte d'Ivoire) sans nomination explicite

SANCTIONS / PEP
- Aucune sanction OFAC, UE, ONU, OFSI vérifiées
- Non-PEP au sens strict (pas de fonction publique)

LIENS CRYPTO
- Mentions USDT dans certaines DS — volet renvoyé à Athéna Group / Sarah Marin pour analyse on-chain

HYPOTHÈSES CALIBRÉES
- UBO réel d'une majorité des entités du réseau Haddad : probable.
- Implication dans schéma de transit financier multi-juridictionnel : probable.
- Implication directe dans blanchiment ou contournement de sanctions : possible à ce stade, à confirmer par flux et coopération.

LACUNES
- Comptes bancaires libanais et suisses : accès non obtenu (coopération en cours).
- Liste exhaustive des bénéficiaires d'OMEGA TRUST : non connue.
- Substance économique des entités émiraties : non vérifiée.

SOURCES (extrait)
- Pappers, INPI, RBE [04/03]
- Companies House, PSC [05/03]
- OpenCorporates, Sayari [05/03]
- ICIJ Pandora Papers, Aleph OCCRP [06/03]
- LinkedIn, presse [07/03]
- Patrim France [08/03]
- DS reçues par CRF (référencées en interne)
```

### Erreurs fréquentes

- **Fiche incomplète sans mention des lacunes.** Un livrable lisse passe pour exhaustif et trompe le lecteur.
- **Mélanger les niveaux de confiance.** Tout n’est pas *quasi-certain*. La calibration explicite est obligatoire.
- **Ne pas dater chaque élément.** Les profils changent.

### Limites

Une fiche ne remplace pas une analyse contextuelle. Elle l’alimente. Elle ne dit pas non plus *« cette personne est coupable »* — ce vocabulaire n’a pas sa place ici.

### Lien avec le fil rouge

> **CLEARFLOW — La fiche au cœur du dossier**
> 
> La fiche Karim Haddad est le pivot du dossier de Nassim. Elle est mise à jour à chaque étape majeure. À la finale, elle sera produite en annexe de la note de transmission au PNF. Toute autre fiche du dossier (M. Y, Mme Z, M. X, etc.) suit le même modèle.

### Points clés à retenir

- Fiche = livrable autonome, sourcé, calibré, versionné, actionnable.
- 14 sections type ; modèle complet en annexe C.
- Discipline d’explicitation des lacunes.
- Pas de conclusion de culpabilité dans une fiche.

-----

## Chapitre 28 — Construire une fiche société

### Objectif du chapitre

Maîtriser la **fiche société FININT** — pendant de la fiche personne, structurée pour les entités juridiques. Modèle complet en annexe D.

### Le concept

La fiche société consolide, sur une entité, tout ce que l’analyste sait : identification, juridiction, gouvernance, capital et UBO, activité, comptes, flux, contentieux, liens avec d’autres entités, hypothèses calibrées.

### Structure type d’une fiche société

1. **En-tête** : référence, date, version, classification, auteur.
1. **Identification** : dénomination exacte, identifiant officiel, forme juridique, juridiction, capital, date de création.
1. **Adresse(s)** : siège, établissements secondaires, adresse réelle si différente du siège déclaré.
1. **Activité déclarée** : NAF/SIC/code sectoriel, libellé, sous-activités.
1. **Gouvernance** : dirigeants actuels, mandataires, historique.
1. **Actionnariat / Capital** : associés, pourcentages, classes d’actions.
1. **UBO** : déclaré (registre UBO) et identifié (analyse), avec niveaux de confiance.
1. **Substance économique** : personnel, locaux, site web, clientèle, fournisseurs, présence opérationnelle réelle.
1. **Comptes** : derniers comptes annuels publiés, principaux indicateurs, ratios, observations.
1. **Flux observables** : profil bancaire (si DS ou OSINT), contreparties principales.
1. **Contentieux** : procédures collectives, contentieux fiscaux, sanctions, adverse media.
1. **Liens** : entités liées (capital, dirigeants partagés, adresse partagée), trust ou fondation au sommet.
1. **Crypto si pertinent** : adresses, échanges utilisés — renvoi vers OSINT Crypto.
1. **Hypothèses calibrées** : qualification de la nature de l’entité (opérationnelle légitime, holding, intermédiaire, écran probable, etc.).
1. **Sources et lacunes**.

### L’utilité opérationnelle

Comme pour la fiche personne, la fiche société est **réutilisable, sourcée, calibrée**. Elle permet de structurer un livrable complexe (note FININT couvrant plusieurs entités) en éléments atomiques cohérents.

### Méthode — bonnes pratiques

- **Préciser la juridiction** dès l’identification (pas de confusion avec sociétés homonymes).
- **Annoter l’identifiant officiel** systématiquement.
- **Mettre la substance économique en évidence** : c’est souvent la clé.
- **Présenter les comptes en ratios** plus qu’en chiffres bruts, pour comparaison.
- **Documenter les liens** avec une référence à la fiche correspondante.

### Mini-walkthrough — fiche NEXUS TRADING SAS (extrait)

```
FICHE SOCIÉTÉ — NEXUS TRADING SAS
Référence : CLEARFLOW/SOC/003 | v1.2 | 14/03 | TLP:AMBER

IDENTIFICATION (quasi-certain)
- Forme : SAS
- SIREN : 8XX XXX XXX
- Juridiction : France
- Capital : 10 000 €
- Date de création : 18/01/2023

ADRESSE(S)
- Siège : 12 rue Y, Paris 9e (cabinet de domiciliation, 47 entités à la même adresse)

ACTIVITÉ DÉCLARÉE
- NAF 4690Z : commerce de gros non spécialisé
- Activité opérationnelle visible : non identifiée (pas de site web, pas de catalogue, pas de référence client publique)

GOUVERNANCE
- Président : Monsieur X (depuis création) — multi-mandats, profil prête-nom probable (voir fiche personne)
- Aucun DG, aucun directeur, aucun salarié déclaré (URSSAF non accessible directement)

ACTIONNARIAT / CAPITAL
- Associé unique : NEXUS HOLDINGS LTD (Chypre)

UBO
- Déclaré au RBE : Monsieur X (par défaut, en tant que dirigeant)
- Identifié (probable) : Karim Élie Haddad, via chaîne CY → trust OMEGA → settlor

SUBSTANCE ÉCONOMIQUE
- Personnel : aucun salarié visible
- Locaux : domiciliation seule
- Site web : aucun
- Clientèle visible : aucune
- Fournisseurs visibles : aucune trace publique
→ Substance économique très faible. Écran probable.

COMPTES (1er exercice clos)
- CA : 12,4 M€
- Marge brute : 4 %
- Charges de personnel : 32 K€
- Résultat d'exploitation : 80 K€
- Trésorerie en fin d'exercice : 35 K€
→ Profil compatible avec activité de pure intermédiation OU société de transit.

FLUX OBSERVABLES (via DS)
- Entrées : 87 % depuis Émirats (sociétés liées au réseau Haddad) et Chypre
- Sorties : virements vers 4 sociétés du réseau + 22 % vers comptes personnels (M. X et liés)
→ Profil incompatible avec activité commerciale réelle de négoce.

CONTENTIEUX
- Aucune procédure collective.
- Aucun contentieux fiscal public.

LIENS
- Capital : 100 % NEXUS HOLDINGS LTD (CY)
- Dirigeants partagés : M. X = dirigeant de 7 autres SAS (cluster).
- Adresse partagée : 46 autres entités au même cabinet.
- Trust de contrôle : OMEGA HOLDINGS TRUST (CY).

HYPOTHÈSES CALIBRÉES
- Société écran à finalité de transit : probable.
- Implication dans schéma de blanchiment ou TBML : possible à probable (à confirmer par analyse de flux globale).
- UBO réel = Karim Haddad : probable.

LACUNES
- Substance opérationnelle réelle : non vérifiée par visite physique.
- Comptes détaillés (relevés bancaires) : accès en CRF, non encore mobilisé.

SOURCES
- Pappers, INPI, RBE
- Comptes annuels Infogreffe
- DS bancaires (interne CRF)
- Cartographie réseau (chapitre 31)
```

### Erreurs fréquentes

- **Confondre dénomination commerciale et dénomination sociale.** Toujours utiliser la dénomination officielle.
- **Ne pas mentionner les lacunes sur la substance économique.** Sans visite physique ou témoignage, la substance reste *probable* à qualifier.
- **Lire les comptes sans contexte sectoriel.** Une faible marge en intermédiation peut être normale.

### Limites

Beaucoup d’éléments de la fiche société exigent des sources fermées (comptes bancaires détaillés, contrats commerciaux, audits). En OSINT pur, la fiche est **partielle** et l’indique explicitement.

### Lien avec le fil rouge

> **CLEARFLOW — 14 fiches société**
> 
> Nassim produit une fiche pour chacune des 14 entités du réseau Haddad. Cumulées, ces fiches forment le socle de la note de transmission. Elles permettent de répondre à la question « quelle est la nature de chaque entité dans le réseau ? » avec calibration de la confiance pour chaque qualification.

### Points clés à retenir

- Fiche société : pendant structurel de la fiche personne, pour les entités.
- 15 sections type ; modèle complet en annexe D.
- Substance économique = section clé.
- Ratios > chiffres bruts pour la lecture rapide.

-----

## Chapitre 29 — Construire une fiche flux

### Objectif du chapitre

Maîtriser la **fiche flux** : livrable structurel qui consolide, sur un flux financier ou un ensemble de flux liés, les éléments d’origine, de transit, de destination, et leur qualification typologique. Modèle en annexe E.

### Le concept

Une fiche flux peut concerner :

- **Un flux unique** : un virement, un dépôt, une opération.
- **Une séquence** : plusieurs flux liés (cascade, fractionnement, layering).
- **Un schéma** : une typologie observée sur une période, impliquant plusieurs comptes et entités.

### Structure type

1. **En-tête** : référence, date, version, classification.
1. **Description** : type de flux (virement, dépôt cash, paiement carte, opération crypto), montant, devise, date(s).
1. **Origine** : compte donneur d’ordre, banque, juridiction, titulaire, libellé.
1. **Transit** : banques correspondantes, comptes intermédiaires, rails utilisés (SWIFT, SEPA, SCT Inst, etc.).
1. **Destination** : compte bénéficiaire, banque, juridiction, titulaire, libellé reçu.
1. **Délai** : heure de débit, heure de crédit, délais inter-étapes.
1. **Contexte** : autres flux liés, comportement antérieur, motif déclaré.
1. **Cohérence économique** : flux compatible avec l’activité ? avec les comptes annuels ? avec le profil du titulaire ?
1. **Typologie possible** : à quel schéma ce flux est-il compatible (TBML, BEC, layering, structuration, etc.) ?
1. **Hypothèses calibrées** et niveaux de confiance.
1. **Sources** : DS, relevés (référence interne), OSINT.
1. **Lacunes** et actions complémentaires.

### L’utilité opérationnelle

La fiche flux **isole un cas** pour qu’il puisse être analysé, présenté à un magistrat, ou intégré dans une typologie sectorielle. Elle est particulièrement utile dans les dossiers complexes où plusieurs typologies coexistent : isoler les flux par type permet une analyse plus claire.

### Méthode

1. **Définir le périmètre** : un flux, une cascade, un schéma — préciser dès l’en-tête.
1. **Recueillir tous les attributs** (montants, dates, parties, rails).
1. **Identifier la cohérence ou l’anomalie**.
1. **Confronter à une typologie** : le flux ressemble-t-il à un schéma connu (chapitres 40-47) ?
1. **Calibrer**.

### Mini-walkthrough — séquence BEC fictive (extrait fiche flux)

```
FICHE FLUX — SÉQUENCE BEC LAYERING 14/03
Référence : CLEARFLOW/FLX/021 | v1.0 | TLP:AMBER

DESCRIPTION
- Type : séquence SCT Inst + SCT Inst + dépôts USDT
- Montant total : 215 000 €
- Période : 14/03, 14h32 → 14/03, 18h45 (4h13)

ORIGINE
- Compte source : PME française "ALPHA INDUSTRIE SARL", banque XYZ, IBAN FR...
- Donneur d'ordre : signature du gérant, validation à 14h28
- Contexte : virement présenté comme paiement à un nouveau fournisseur, libellé "trade payment - facture XXXX"

TRANSIT
1. ALPHA SARL → IBAN ES (nouveau) "Iberica Trading SL" : 215 000 €, 14h32, SCT Inst, irréversible.
2. Iberica Trading SL → 5 IBANs (PT x3, LT x2) : fractionnement 40 000 € à 45 000 €, 14h35-14h41.
3. Comptes PT/LT → exchange A : 5 dépôts USDT, 16h12.
4. Exchange A → wallet auto-géré : sortie crypto, 18h45.

DÉLAI TOTAL
- Origine → wallet : 4h13. Fenêtre de gel : quasi-nulle (SCT Inst irréversible).

CONTEXTE
- ALPHA SARL avait reçu un email frauduleux 48h avant, simulant le gérant d'une société partenaire et demandant un changement d'IBAN.
- Le mail provenait d'un domaine très proche du vrai (typosquatting).

COHÉRENCE ÉCONOMIQUE
- Incompatible avec l'activité d'ALPHA (pas de relation antérieure avec Iberica, montant inhabituel, IBAN ES nouveau).

TYPOLOGIE POSSIBLE
- Fraude au virement (BEC) avec layering instantané et cashout crypto.

HYPOTHÈSES CALIBRÉES
- BEC : quasi-certain (séquence et contexte univoques).
- Cashout crypto : quasi-certain.
- Identification de l'auteur : indéterminable à ce stade ; volet on-chain renvoyé à Athéna Group.

SOURCES
- Plainte ALPHA SARL
- Relevés bancaires (réquisition en cours pour comptes ES, PT, LT)
- DS de la banque XYZ
- Analyse on-chain Athéna (en cours)

LACUNES
- Identification de l'attaquant.
- Lien éventuel avec d'autres cas (cluster d'attaques BEC).
```

### Erreurs fréquentes

- **Mélanger plusieurs séquences dans une seule fiche.** Une fiche = un flux ou une séquence cohérente.
- **Ne pas mentionner le délai entre étapes.** La vitesse est un signal essentiel.
- **Conclure sur la typologie sans calibration.** Une « ressemblance » à un schéma TBML ne vaut pas typologie *quasi-certaine*.

### Limites

Beaucoup d’éléments (libellés détaillés, références internes bancaires, métadonnées de l’opération) ne sont accessibles qu’en sources fermées (réquisition, droit de communication CRF).

### Lien avec le fil rouge

> **CLEARFLOW — Une vingtaine de fiches flux**
> 
> Nassim produit, pour le dossier Haddad, environ 22 fiches flux : des séquences de virements depuis l’étranger vers la France, des transferts intra-groupe, des opérations vers la Suisse, des conversions USDT. Chaque fiche, isolée, est lisible ; cumulées, elles forment la base de l’analyse globale (chapitre 35).

### Points clés à retenir

- Fiche flux : un flux ou une séquence cohérente, jamais davantage.
- Délai entre étapes = signal critique.
- Typologie possible = hypothèse, jamais conclusion sans calibration.
- Modèle complet en annexe E.

-----

## Chapitre 30 — Construire une fiche actif

### Objectif du chapitre

Maîtriser la **fiche actif** : livrable centré sur un bien (immobilier, financier, mobilier de valeur), structurant son identification, ses détenteurs (juridiques et effectifs), son historique d’acquisition, sa valeur estimée, et sa pertinence dans l’enquête. Modèle en annexe F.

### Le concept

Une fiche actif documente :

- **Identification** : nature du bien (immobilier, véhicule, bateau, œuvre, participation), localisation, identifiants.
- **Détenteurs** : propriétaire juridique (SCI, société, personne), UBO probable, financement.
- **Historique** : date d’acquisition, prix, mode de financement, transactions antérieures.
- **Valeur** : valorisation actuelle, source de l’estimation.
- **Pertinence** : pourquoi cet actif est dans le dossier, lien avec la personne ou la société cible.
- **Asset recovery** : susceptibilité de gel / saisie, juridiction, autorité compétente.

### Types d’actifs traités

**Immobilier** : maisons, appartements, biens commerciaux. Sources : registres fonciers (variables selon pays), Patrim France (consultation administrative), DVF (Demandes de Valeurs Foncières en France, données ouvertes), bases de données commerciales (CityScan, RealCapital), presse mondaine pour les transactions remarquables.

**Véhicules** : voitures de luxe, supercars. Registre des véhicules selon pays.

**Bateaux et yachts** : registres internationaux (Lloyd’s Register, MarineTraffic pour le tracking AIS), pavillons (souvent Malte, Cayman, Bahamas, Marshall pour les yachts).

**Aéronefs** : FAA (US), EASA (UE), pavillon de l’aéronef, traçage ADS-B (FlightAware, ADS-B Exchange).

**Participations financières** : actions, parts sociales, obligations, OPCVM, ETF.

**Œuvres d’art, objets de collection** : registres internes des maisons de ventes (Sotheby’s, Christie’s), bases académiques (Art Loss Register), provenance.

**Comptes bancaires** : pas directement « actifs » mais véhicules de détention. Existence parfois traçable via EAR/CRS pour la CRF.

**Cryptos** : adresses on-chain (renvoi vers OSINT Crypto).

### L’utilité opérationnelle

La fiche actif sert deux objectifs :

1. **Documenter le patrimoine** d’une personne ou d’un groupe — base de la reconstitution patrimoniale (chapitre 39).
1. **Préparer l’asset recovery** : gel, saisie, confiscation (chapitre 66) — l’identification précise et juridictionnellement qualifiée des actifs est la condition préalable.

### Méthode

1. **Identifier le bien** par sources ouvertes (cadastre, DVF, AIS, presse).
1. **Identifier le propriétaire juridique** : personne physique, SCI, société.
1. **Remonter jusqu’à l’UBO** quand possible.
1. **Documenter l’historique** : date d’acquisition, prix, mode (cash, prêt, virement, mixte).
1. **Estimer la valeur actuelle**.
1. **Qualifier la cohérence** : ce bien est-il cohérent avec les revenus déclarés du détenteur ?
1. **Identifier la juridiction** et l’autorité compétente pour un éventuel asset recovery.

### Mini-walkthrough — fiche actif (extrait)

```
FICHE ACTIF — APPARTEMENT PARIS 8e
Référence : CLEARFLOW/ACT/004 | v1.0 | TLP:AMBER

IDENTIFICATION
- Nature : appartement résidentiel
- Localisation : 5 rue X, Paris 8e
- Surface : ~280 m², 6e étage
- Identifiant cadastral : 75108-XXXX-XXXX

DÉTENTEUR JURIDIQUE (quasi-certain)
- SCI HADDAD INVESTISSEMENTS (France), détention 100 %
- Gérance : Mme Z (présidente d'une autre SAS du réseau, lien personnel à K. Haddad)

UBO PROBABLE
- Karim Élie Haddad, via SCI

HISTORIQUE
- Acquisition : 09/2019
- Prix d'acquisition (DVF) : 4,2 M€
- Financement : non transparent en OSINT. Pas de prêt notarié inscrit visible (vérifier hypothèques inscrites).

VALEUR ACTUELLE ESTIMÉE
- Estimation marché : 4,7 M€ (basé sur prix au m² du quartier — DVF récent)
- Source : DVF + cabinet d'estimation (à approfondir)

PERTINENCE
- Bien probablement détenu par K. Haddad via SCI.
- Cohérence avec revenus déclarés : à examiner (déclaration fiscale via réquisition).

ASSET RECOVERY
- Juridiction : France.
- Autorité compétente : AGRASC (gel/saisie/confiscation), sous procédure judiciaire.
- Réalisable si infraction qualifiée et procédure ouverte.

SOURCES
- DVF data.gouv.fr
- Registre foncier (consultation)
- Pappers (SCI)
```

### Erreurs fréquentes

- **Confondre détenteur juridique et UBO.** Une SCI détient ; l’UBO contrôle la SCI.
- **Estimer la valeur sans source.** Mention explicite de la méthode et de la source.
- **Considérer un bien comme « confiscable » sans procédure.** L’asset recovery exige un cadre judiciaire.

### Limites

L’estimation de la valeur est **indicative**. Les biens à l’étranger (Dubaï, Beyrouth, Genève) ne sont pas accessibles avec la même précision que les biens français.

### Lien avec le fil rouge

> **CLEARFLOW — Cartographie patrimoniale**
> 
> Nassim identifie 11 actifs significatifs : 3 biens immobiliers à Paris (via SCI), 1 villa à Beyrouth (présomée, à confirmer), 1 yacht enregistré sous pavillon Malte (présent dans presse), 2 véhicules de luxe immatriculés à Paris, 4 participations dans des sociétés non encore consolidées dans la cartographie. Le total estimé : environ 18 M€ pour les actifs visibles français + 6 à 12 M€ pour les actifs étrangers présumés. À comparer aux revenus déclarés français (à obtenir via DGFiP).

### Points clés à retenir

- Fiche actif : un bien, un livrable.
- Distinguer détenteur juridique et UBO.
- Estimation de valeur sourcée.
- Préparer l’éventuel asset recovery par juridiction.

-----

## Chapitre 31 — Graphes relationnels FININT

### Objectif du chapitre

Comprendre la **représentation graphique** d’un réseau financier : nœuds (personnes, entités, actifs, flux), arcs (liens typés), et les usages opérationnels de cette représentation.

### Le concept

Un graphe relationnel FININT est une représentation visuelle d’un réseau. Les **nœuds** sont des entités (personnes, sociétés, comptes, actifs, transactions). Les **arcs** (ou arêtes) sont les liens (capital, mandat, virement, propriété, etc.).

Les arcs sont typés : capital, mandat, paiement, propriété, parenté, adresse partagée. Chaque type a sa logique et son intensité.

**Outils** :

- **Maltego** : référence pour l’OSINT et le FININT, transforms multiples.
- **i2 Analyst’s Notebook** : standard du renseignement, lourd mais puissant.
- **Linkurious** : web-based, neo4j-backed, professionnel.
- **Gephi** : open source, analytique (centralités, communautés).
- **Graphistry** : web-based, GPU-accelerated, exploration interactive.
- **Neo4j** : base de données graphe sous-jacente.
- **Outils intégrés à Sayari, Orbis, Dow Jones** : graphes pré-construits sur leur référentiel.

### L’utilité opérationnelle

Le graphe permet :

- **Détection de patterns** : clusters, structures en étoile, chaînes longues, ponts.
- **Identification de nœuds centraux** : qui est le « hub » du réseau ? — souvent l’UBO réel.
- **Détection de liens cachés** : ponts entre clusters apparemment indépendants.
- **Présentation visuelle** : un graphe bien construit communique en quelques secondes ce qui exige des pages de description.

### Méthode — construire un graphe FININT

1. **Définir le périmètre** : périmètre initial (entités cibles), puis périmètres d’extension.
1. **Choisir les types de nœuds et d’arcs** :
- Nœuds : personnes, sociétés, comptes bancaires, adresses physiques, actifs significatifs, transactions clés.
- Arcs : capital (avec %), mandat (avec rôle), UBO (avec niveau de confiance), virement (avec montant et date), parenté (conjoint, enfant, fratrie), adresse partagée, employeur, contact réseau social.
1. **Charger les données** depuis les fiches (Ch.27-30) et les sources.
1. **Annoter** : libeller chaque arc avec son type, sa date, son intensité.
1. **Calculer des métriques** quand pertinent : centralité (degré, betweenness), communautés (Louvain), shortest paths.
1. **Itérer** : enrichir, déplacer, simplifier pour lisibilité.

### Mini-walkthrough — graphe CLEARFLOW (description)

Le graphe central du dossier Haddad compte ~40 nœuds (14 sociétés, 12 personnes physiques, 11 actifs, et quelques nœuds techniques de transaction). Une fois construit dans Linkurious avec les liens typés, les patterns suivants émergent visuellement :

- **Cluster français** (4 SAS + dirigeants prête-noms probables) — fortement connecté en interne, faiblement à l’extérieur sauf via 1 arc capital vers le cluster chypriote.
- **Cluster chypriote** (NEXUS HOLDINGS + trust OMEGA) — au sommet, avec arc UBO probable vers Karim Haddad.
- **Cluster émirats / asiatique** (sociétés free zone, contacts à Dubaï) — autour de M. Y (PSC des Limited UK).
- **Branche Liban** — entités libanaises, faiblement visible mais positionnée à l’origine.
- **Branche Afrique de l’Ouest** (Bénin, Côte d’Ivoire) — débouchés opérationnels.
- **Karim Haddad** au centre : nœud de plus haute centralité dans le graphe (intuition confirmée par calcul de betweenness).

Cette représentation, présentée en réunion, communique en quelques secondes ce que 30 pages de note racontent.

### Erreurs fréquentes

- **Graphe trop chargé** : illisible. Limiter à 30-50 nœuds visibles à la fois.
- **Arcs non typés** : ambiguïté.
- **Pas de date** : un lien actuel et un lien obsolète sont traités à l’identique.
- **Confondre forte connexité et causalité** : un nœud central peut être un facilitateur, pas un contrôleur.

### Limites

Le graphe **résume** ; il ne **prouve** pas. Une représentation peut renforcer une hypothèse erronée si les nœuds sont mal qualifiés. Il doit accompagner une analyse écrite, jamais la remplacer.

### Lien avec le fil rouge

> **CLEARFLOW — Le graphe en réunion de bilan**
> 
> Lors de la réunion de bilan du dossier, Nassim présente le graphe en première intention. En 2 minutes, le coordinateur et les collègues comprennent la structure du réseau, l’architecture du contrôle, et les zones d’incertitude. Le graphe accompagne la note dans le dossier transmis au PNF.

### Points clés à retenir

- Graphe = représentation, pas preuve.
- Nœuds + arcs typés + dates + niveaux de confiance.
- Outils : Maltego, i2, Linkurious, Gephi, Graphistry.
- Métriques utiles : centralité (qui est central ?), communautés (clusters ?).

-----

## Chapitre 32 — Distinguer lien faible, lien fort et contrôle réel

### Objectif du chapitre

Calibrer la **force des liens** dans un graphe FININT — éviter de surinterpréter une coïncidence comme un lien fort, et inversement de sous-estimer un lien faible qui s’avère structurant.

### Le concept

Tous les liens ne se valent pas. Trois catégories :

**Lien faible** — coïncidence, adresse partagée, employeur commun lointain dans le temps, nom de famille identique (sans confirmation de parenté), interactions distantes sur réseaux sociaux. Niveau de confiance : *possible* à *probable* selon contexte. À documenter mais à manier avec prudence.

**Lien fort** — lien capital (>10 %), mandat conjoint (siéger ensemble dans un CA), virement direct récurrent, parenté avérée, conjoint, association professionnelle active, présence dans le même leak avec contexte similaire. Niveau de confiance : *probable* à *quasi-certain*.

**Contrôle réel** — UBO identifié *quasi-certain*, settlor de trust contrôlant les flux, dirigeant exécutif effectif. Distinct du lien fort : implique une **direction**.

### L’utilité opérationnelle

Un graphe avec lien typé en force permet de :

- **Hiérarchiser** : qui est central vs périphérique.
- **Calibrer les hypothèses** : un lien fort soutient une attribution, un lien faible une simple suggestion.
- **Identifier les liens manquants** : où devrais-je trouver un lien et n’en trouve pas (peut signaler une zone d’opacification).
- **Détecter les liens cachés** : un lien faible récurrent dans plusieurs angles (LinkedIn + adresse + leak) devient fort par cumul.

### Méthode — qualifier la force d’un lien

Pour chaque lien :

1. **Quelle est la source** ? (registre = fort ; presse = à recouper ; réseau social = variable ; leak = fort si authentique).
1. **Combien de recoupements indépendants** ? (1 source = à confirmer ; 2 sources indépendantes = probable ; 3+ = quasi-certain).
1. **Quelle est la nature du lien** ? (capital > mandat > parenté > adresse > présence partagée).
1. **Quelle est l’intensité dans le temps** ? (récent et durable > ancien ou ponctuel).
1. **Est-ce dans la même direction** que d’autres liens ? (cohérence d’un faisceau).

### Mini-walkthrough — lien Haddad / Mme Z

- Source initiale : Mme Z est présidente d’une SAS du réseau (lien fort de mandat).
- Recoupement 1 : article de presse libanaise 2018 mentionne Mme Z lors d’un événement caritatif organisé par K. Haddad (lien fort de coreligionnaire).
- Recoupement 2 : photos LinkedIn 2022 montrent Mme Z et K. Haddad à un événement professionnel à Paris (lien fort de présence).
- Recoupement 3 : adresse domicile commune dans une ancienne année (registre foncier) — *quasi-certain* d’une cohabitation passée à un certain moment.

Calibration : lien personnel et professionnel fort entre K. Haddad et Mme Z, *quasi-certain*. Mais cela ne fait pas de Mme Z une prête-nom : elle pourrait être collaboratrice de confiance, partenaire dans certaines activités, ou amie. La nature exacte du lien (financier, amical, romantique) est *indéterminable* par OSINT seul.

### Mini-walkthrough — lien faible mal interprété

Un analyste novice repère : K. Haddad et M. P étaient employés de la même entreprise en 2002 (LinkedIn). Tentation : « lien historique ». Calibration : *possible* mais lien faible — beaucoup de personnes ont travaillé pour les mêmes employeurs sans être en relation. Sans recoupement, ne pas mentionner comme un fait structurant.

### Erreurs fréquentes

- **Surinterpréter un lien faible** : tirer une hypothèse forte d’une coïncidence.
- **Sous-estimer un cumul de liens faibles** : 4 ou 5 indices faibles convergents valent un lien probable.
- **Confondre lien fort et contrôle** : co-présence dans un CA = lien fort mais ne dit pas qui contrôle.

### Limites

La force d’un lien n’est jamais binaire. C’est une **calibration**, pas un classement.

### Lien avec le fil rouge

> **CLEARFLOW — Mme Z et le réseau**
> 
> Le lien Haddad / Mme Z, fort par cumul, alimente l’hypothèse que Mme Z est une présidente nominale agissant pour le compte de Haddad (mais avec autonomie et lien personnel — différent d’un prête-nom anonyme). Cette qualification nuancée se retrouve dans la fiche personne Mme Z, dans la fiche société de la SAS qu’elle préside, et dans la note finale.

### Points clés à retenir

- Lien faible / lien fort / contrôle réel : trois catégories à distinguer.
- Calibrer par : source, recoupements, nature, durée, cohérence.
- Cumul de liens faibles convergents = potentiellement un lien fort.
- Lien fort ≠ contrôle automatique.

-----

## Chapitre 33 — Échelle de confiance WEP et hypothèses calibrées

### Objectif du chapitre

Formaliser et appliquer l’**échelle de confiance** inspirée des **Words of Estimative Probability** (WEP) pour calibrer toutes les conclusions d’une note FININT. C’est la discipline qui distingue un livrable professionnel d’un texte affirmatif sans nuance.

### Le concept

Les WEP sont une convention sémantique pour exprimer la confiance d’une affirmation. Origine : Sherman Kent, CIA, années 1960 — repris dans le renseignement civil et militaire et adapté en FININT.

**Échelle utilisée dans ce cours** :

|Niveau               |Plage  |Quand l’utiliser                                                           |
|---------------------|-------|---------------------------------------------------------------------------|
|**Quasi-certain**    |> 95 % |Multi-sources indépendantes, documents probants, recoupements convergents. |
|**Très probable**    |80-95 %|Plusieurs sources concordantes, hypothèses alternatives faibles.           |
|**Probable**         |60-80 %|Indices convergents mais incomplets, hypothèses alternatives moins fortes. |
|**Possible**         |40-60 %|Compatibilité avec les éléments, mais hypothèses alternatives équivalentes.|
|**Peu probable**     |15-40 %|Compatibilité faible, hypothèses alternatives dominantes.                  |
|**Très peu probable**|< 15 % |Quasi-exclusion.                                                           |
|**Indéterminable**   |n/a    |Données insuffisantes pour calibrer.                                       |

Cette échelle est utilisée systématiquement dans le cours, les fiches, les cas pratiques, la note FININT et les annexes.

### L’utilité opérationnelle

Cinq usages :

1. **Discipline analytique** : forcer l’analyste à se demander, pour chaque conclusion, *« quelle est la solidité réelle de ce que j’écris ? »*.
1. **Communication précise** : le lecteur (magistrat, comité, partenaire) sait à quel point il peut s’appuyer sur chaque élément.
1. **Honnêteté épistémique** : ne pas faire semblant de savoir ce qu’on ne sait pas.
1. **Calibration des actions** : un gel d’avoirs sur la base d’un *quasi-certain* n’est pas la même décision qu’un signalement sur la base d’un *probable*.
1. **Comparabilité** : entre analystes, entre dossiers, entre périodes.

### Méthode — calibrer une conclusion

1. **Identifier les sources** qui soutiennent la conclusion.
1. **Identifier les sources qui la contredisent** ou la nuancent.
1. **Identifier les hypothèses alternatives** : que d’autres explications restent compatibles avec les éléments ?
1. **Évaluer la solidité** : robustesse des sources, recoupements indépendants, cohérence avec le reste du dossier.
1. **Choisir le niveau** dans l’échelle.

### Mini-walkthrough — calibration progressive

Hypothèse : *« Karim Haddad est l’UBO réel de NEXUS TRADING SAS (France) »*.

**Étape 1** : seul élément initial — chaîne de capital remonte à NEXUS HOLDINGS LTD (CY).
→ Calibration : *indéterminable* sur Haddad spécifiquement.

**Étape 2** : ajout du hit Pandora — settlor du trust OMEGA = Karim Haddad.
→ Calibration : *probable*. La chaîne est plausible mais formelle ; le contrôle effectif n’est pas démontré.

**Étape 3** : ajout des analyses de flux — Haddad reçoit personnellement des fonds en sortie du réseau et signe des opérations critiques.
→ Calibration : *très probable*.

**Étape 4** : coopération Mokas confirme la qualité de bénéficiaire principal de Haddad dans le trust, et témoignage du trustee si obtenu.
→ Calibration : *quasi-certain*.

À chaque étape, l’évolution de la calibration est documentée. La note finale présente la calibration *finale*, mais les annexes peuvent retracer l’évolution pour transparence.

### Erreurs fréquentes

- **Utiliser un vocabulaire affirmatif sans calibration** : « c’est l’UBO », « il blanchit » — sans support, c’est faux ou exposé à contestation.
- **Sur-calibrer** par excès de prudence : tout est *possible* — devient ininterprétable.
- **Sous-calibrer** par enthousiasme : tout est *quasi-certain* — fait perdre la crédibilité.
- **Confondre absence de preuve et preuve d’absence** : si on ne trouve pas un élément, ce n’est pas qu’il n’existe pas — peut-être qu’on n’a pas la bonne source.

### Limites

L’échelle WEP est une convention sémantique, pas une mesure objective. La calibration reste un **jugement informé**. Deux analystes peuvent diverger légèrement sur le niveau — c’est attendu et acceptable, à condition que chacun **justifie** son choix.

### Lien avec le fil rouge

> **CLEARFLOW — Calibration systématique**
> 
> La note finale du dossier Haddad utilise systématiquement l’échelle WEP. Exemple d’extrait : *« La qualification de NEXUS DELAWARE LLC comme société écran de transit à finalité d’opacification est probable. La qualification de la finalité illicite (blanchiment) est possible à ce stade et nécessiterait, pour être qualifiée probable, la confirmation par audition de bénéficiaires de fonds et expertise comptable. La qualification du rôle de M. X comme prête-nom est probable. La qualification de K. Haddad comme UBO réel du réseau est très probable. »*

### Points clés à retenir

- WEP : quasi-certain > très probable > probable > possible > peu probable > très peu probable > indéterminable.
- Utiliser systématiquement, dans fiches, notes, cas pratiques.
- Calibration = jugement informé, à justifier.
- Permet honnêteté, communication, discipline analytique.

-----
