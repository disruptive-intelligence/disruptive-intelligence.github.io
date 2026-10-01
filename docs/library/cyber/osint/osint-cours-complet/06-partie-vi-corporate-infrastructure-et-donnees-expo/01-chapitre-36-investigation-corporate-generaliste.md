---
title: Chapitre 36 — Investigation corporate généraliste
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VI — Corporate, infrastructure et données exposées
  - index.md
---

## 36.1 Cadre et enjeux

L'**investigation corporate** OSINT consiste à comprendre une personne morale : sa raison sociale, ses dirigeants, ses actionnaires, ses bénéficiaires effectifs (UBO), ses filiales, son activité, ses signaux de risque.

Les cas d'usage sont multiples : due diligence pré-transaction, KYC/KYB, investigation de fraude, vérification de partenaire commercial, application des sanctions, conformité CSDDD, journalisme financier, recherche d'actifs (asset recovery).

Le présent chapitre couvre la **vue maître**. La profondeur (UBO complexes, schémas de blanchiment, asset recovery, AML/CFT) est traitée dans **FININT Investigation Financière vFULL**.

## 36.2 Anatomie d'une société

Une société est définie par plusieurs dimensions à investiguer.

**Identité légale.**

- Raison sociale (et sigles, marques, dénominations commerciales).
- Forme juridique (SARL, SAS, SA, Ltd, GmbH, LLC, etc.).
- Juridiction d'enregistrement.
- Numéro d'enregistrement (SIREN, registration number, EIN).
- Date de création, dates de modifications statutaires.
- Capital social, évolution.
- Adresse de siège (et changements).

**Gouvernance.**

- Dirigeants (président, DG, DAF, etc.).
- Conseil d'administration / surveillance.
- Commissaires aux comptes.
- Procurations.

**Actionnariat.**

- Capital social, structure.
- Actionnaires identifiés (souvent partiellement public).
- Pactes d'actionnaires (rarement publics).
- **UBO** (Ultimate Beneficial Owner) : personne physique contrôlant in fine.

**Activité.**

- Code activité (NAF en France, NACE en UE, NAICS US).
- Description d'activité réelle.
- Marchés, produits, clients (selon disponibilité).
- Filiales et participations.

**Indicateurs financiers.**

- Comptes annuels publiés (obligation variable selon juridiction et taille).
- Chiffre d'affaires, résultat, dette.
- Évolution sur 3-5 ans.

**Indicateurs de risque.**

- Procédures judiciaires.
- Sanctions.
- Adverse media.
- Liens avec personnalités politiquement exposées (PEP).
- Juridictions à risque.

## 36.3 Méthodologie générale

**Phase 1 — Identification fiable.** Confirmer qu'on parle de la bonne entité. Numéro d'enregistrement unique = sélecteur fort.

**Phase 2 — Profil de base.** Identité légale, gouvernance, activité, taille.

**Phase 3 — Structure capitalistique.** Actionnaires, UBO, participations.

**Phase 4 — Indicateurs financiers.** Comptes, évolution.

**Phase 5 — Risque.** Sanctions, PEP, adverse media, contentieux.

**Phase 6 — Network.** Dirigeants partagés, sociétés liées (cluster).

**Phase 7 — Cotation et synthèse.**

## 36.4 Bénéficiaire effectif (UBO) : concept central

L'**UBO** (Ultimate Beneficial Owner — Bénéficiaire Effectif) est la **personne physique** qui détient ou contrôle in fine une entité.

**Définition standard (FATF, UE).**

- Détention directe ou indirecte ≥ 25 % du capital ou droits de vote (seuil indicatif).
- Ou exercice du contrôle par tout autre moyen.

**Pourquoi central.** Une investigation corporate qui ne remonte pas à l'UBO est incomplète. Les structures écrans (nominees, fiducies, fondations) existent précisément pour masquer l'UBO.

**Sources UBO.**

- **France** : RBE (Registre des Bénéficiaires Effectifs), accessible via Pappers ou Infogreffe (gratuit base, payant détaillé).
- **UE** : registres UBO nationaux (issus de la 5e AMLD). Accessibilité variable depuis arrêt CJUE 2022 (limitation accès public).
- **UK** : Companies House (registre UBO public depuis 2016).
- **OpenCorporates, ICIJ leaks** : sources complémentaires.

## 36.5 Sources principales — vue d'ensemble

**Registres officiels FR.** Pappers (interface), Infogreffe, RNE (Registre National des Entreprises), RBE (UBO), BODACC (annonces).

**Registres officiels EU.** OpenCorporates (méta-agrégateur), Companies House (UK), BORIS (registres UBO européens), Handelsregister (DE), Companies Registry (IE), etc.

**Registres officiels internationaux.** SEC EDGAR (US), Companies Bureau (CA), ASIC (AU), MCA (IN), Companies Registry (HK, SG, MT, CY).

**Bases agrégées.** OpenCorporates, Sayari, Bureau van Dijk Orbis, Dun & Bradstreet, Bisnode.

**Sources journalistiques.** OCCRP Aleph, ICIJ Offshore Leaks Database (Panama, Paradise, Pandora, Cyprus Confidential).

**Sanctions et risque.** OpenSanctions (gratuit), OFAC SDN List, EU Sanctions Map, OFSI Consolidated List UK, ONU.

**Adverse media et PEP.** OpenSanctions inclut, WorldCheck (Refinitiv), Dow Jones Risk & Compliance, Sayari.

## 36.6 Méthodologie de désambiguation

**Piège.** Une société peut avoir plusieurs entités (raison sociale identique, juridictions différentes). Une « TechnoVert » en France, une « TechnoVert Ltd » à Malte, une « TechnoVert SA » au Luxembourg peuvent être totalement indépendantes ou liées.

**Méthode.**

- **Numéro unique** (SIREN, registration) = discriminant.
- Cross-recherche sur OpenCorporates qui agrège.
- Vérification des dirigeants : si même dirigeant sur plusieurs entités → lien probable.

## 36.7 Hiérarchie corporative : groupe, mère, filiales

Une enquête corporate sérieuse cartographie :

- **Société cible** : entité directement concernée.
- **Société mère** : entité contrôlant.
- **Filiales** : entités contrôlées.
- **Affiliées** : entités liées sans contrôle pur.
- **Holding** : entité de structure capitalistique.

**Outils.**

- **Pappers** : graphe de participations partiel.
- **OpenCorporates** : cross-juridictions.
- **Orbis** (Bureau van Dijk, payant) : graphes capitalistiques massifs.

## 36.8 Indicateurs de risque corporate

**Signaux d'alerte.**

- Capital symbolique (1 euro, 1 livre).
- Dirigeant unique ou prête-nom apparent (nominee détectable).
- Adresse de domiciliation partagée par centaines d'entités (registered agents typiques de Malte, BVI, Delaware).
- Activité déclarée vague (« consulting », « services »).
- Activité réelle non documentée.
- Juridiction à risque (paradis fiscal classé).
- Liens PEP (politiquement exposés).
- Contentieux multiples.
- Évolutions statutaires fréquentes.

## 36.9 Adresse de domiciliation comme sélecteur

Une **adresse de domiciliation** partagée est un sélecteur très puissant.

**Cas type.** Plusieurs centaines de sociétés enregistrées à la même adresse en Malte, BVI, Belize → registered agent commun. Si on identifie une société à cette adresse, on peut investiguer les centaines d'autres (peut-être détenues par les mêmes UBO ou prête-noms).

**Outils.**

- **OpenCorporates** : recherche par adresse.
- Registres locaux pour la juridiction.

## 36.10 Investigation corporate en vue maître : le périmètre du cours

Le présent cours couvre la **vue maître**. Pour les cas complexes :

- Schémas de blanchiment multi-juridictions → FININT vFULL.
- UBO multi-couches (fiducies, fondations, nominees imbriqués) → FININT vFULL.
- Asset recovery international → FININT vFULL.
- Forensic comptable → cours dédié.

Le master OSINT donne les bases. La spécialisation FININT prend le relais.

-----
