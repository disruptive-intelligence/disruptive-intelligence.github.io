---
title: PARTIE VI — Corporate, infrastructure et données exposées
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
chapter: 7
chapters: 15
---

> **Ce que cette partie apprend.** Conduire une investigation corporate (sociétés, dirigeants, UBO, structures), exploiter les registres internationaux, traiter les sanctions et adverse media, investiguer l'infrastructure numérique d'une entité (domaines, DNS, certificats, sous-domaines, IP), exploiter les breaches et stealer logs, comprendre le Dark Web en vue opérationnelle.
>
> **Ce qu'elle ne couvre pas.** La profondeur FININT (UBO complexes, schémas de blanchiment), la profondeur Crypto, la profondeur Dark Web, la profondeur CTI — toutes traitées dans les cours spécialisés correspondants.
>
> **Ce que vous saurez faire après cette partie.** Investiguer une société, identifier les UBO en vue maître, screening sanctions/PEP, cartographier l'infrastructure web d'une cible, exploiter HIBP/DeHashed/IntelX, comprendre le marché stealer logs, situer le dark web dans une enquête OSINT.

-----

### Chapitre 36 — Investigation corporate généraliste

#### 36.1 Cadre et enjeux

L'**investigation corporate** OSINT consiste à comprendre une personne morale : sa raison sociale, ses dirigeants, ses actionnaires, ses bénéficiaires effectifs (UBO), ses filiales, son activité, ses signaux de risque.

Les cas d'usage sont multiples : due diligence pré-transaction, KYC/KYB, investigation de fraude, vérification de partenaire commercial, application des sanctions, conformité CSDDD, journalisme financier, recherche d'actifs (asset recovery).

Le présent chapitre couvre la **vue maître**. La profondeur (UBO complexes, schémas de blanchiment, asset recovery, AML/CFT) est traitée dans **FININT Investigation Financière vFULL**.

#### 36.2 Anatomie d'une société

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

#### 36.3 Méthodologie générale

**Phase 1 — Identification fiable.** Confirmer qu'on parle de la bonne entité. Numéro d'enregistrement unique = sélecteur fort.

**Phase 2 — Profil de base.** Identité légale, gouvernance, activité, taille.

**Phase 3 — Structure capitalistique.** Actionnaires, UBO, participations.

**Phase 4 — Indicateurs financiers.** Comptes, évolution.

**Phase 5 — Risque.** Sanctions, PEP, adverse media, contentieux.

**Phase 6 — Network.** Dirigeants partagés, sociétés liées (cluster).

**Phase 7 — Cotation et synthèse.**

#### 36.4 Bénéficiaire effectif (UBO) : concept central

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

#### 36.5 Sources principales — vue d'ensemble

**Registres officiels FR.** Pappers (interface), Infogreffe, RNE (Registre National des Entreprises), RBE (UBO), BODACC (annonces).

**Registres officiels EU.** OpenCorporates (méta-agrégateur), Companies House (UK), BORIS (registres UBO européens), Handelsregister (DE), Companies Registry (IE), etc.

**Registres officiels internationaux.** SEC EDGAR (US), Companies Bureau (CA), ASIC (AU), MCA (IN), Companies Registry (HK, SG, MT, CY).

**Bases agrégées.** OpenCorporates, Sayari, Bureau van Dijk Orbis, Dun & Bradstreet, Bisnode.

**Sources journalistiques.** OCCRP Aleph, ICIJ Offshore Leaks Database (Panama, Paradise, Pandora, Cyprus Confidential).

**Sanctions et risque.** OpenSanctions (gratuit), OFAC SDN List, EU Sanctions Map, OFSI Consolidated List UK, ONU.

**Adverse media et PEP.** OpenSanctions inclut, WorldCheck (Refinitiv), Dow Jones Risk & Compliance, Sayari.

#### 36.6 Méthodologie de désambiguation

**Piège.** Une société peut avoir plusieurs entités (raison sociale identique, juridictions différentes). Une « TechnoVert » en France, une « TechnoVert Ltd » à Malte, une « TechnoVert SA » au Luxembourg peuvent être totalement indépendantes ou liées.

**Méthode.**
- **Numéro unique** (SIREN, registration) = discriminant.
- Cross-recherche sur OpenCorporates qui agrège.
- Vérification des dirigeants : si même dirigeant sur plusieurs entités → lien probable.

#### 36.7 Hiérarchie corporative : groupe, mère, filiales

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

#### 36.8 Indicateurs de risque corporate

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

#### 36.9 Adresse de domiciliation comme sélecteur

Une **adresse de domiciliation** partagée est un sélecteur très puissant.

**Cas type.** Plusieurs centaines de sociétés enregistrées à la même adresse en Malte, BVI, Belize → registered agent commun. Si on identifie une société à cette adresse, on peut investiguer les centaines d'autres (peut-être détenues par les mêmes UBO ou prête-noms).

**Outils.**
- **OpenCorporates** : recherche par adresse.
- Registres locaux pour la juridiction.

#### 36.10 Investigation corporate en vue maître : le périmètre du cours

Le présent cours couvre la **vue maître**. Pour les cas complexes :
- Schémas de blanchiment multi-juridictions → FININT vFULL.
- UBO multi-couches (fiducies, fondations, nominees imbriqués) → FININT vFULL.
- Asset recovery international → FININT vFULL.
- Forensic comptable → cours dédié.

Le master OSINT donne les bases. La spécialisation FININT prend le relais.

-----

### Chapitre 37 — Registres corporate et sources internationales

#### 37.1 Tour d'horizon

Ce chapitre détaille les **registres officiels** et **sources internationales** par juridiction, en se concentrant sur ceux qui sont accessibles en source ouverte gratuite ou semi-gratuite.

#### 37.2 France — l'écosystème complet

**Pappers** (pappers.fr). Interface publique gratuite (limitée) et payante. Combine RNE, RBE, BODACC, INPI, ARCEP. C'est le standard pour la France.

**Infogreffe** (infogreffe.fr). Registre officiel des greffes. Accès gratuit aux KBIS partiel, payant pour comptes détaillés.

**RNE — Registre National des Entreprises.** Depuis 2023, registre unifié remplaçant RCS, RM, registre des actifs agricoles. Accessible via Pappers, INPI.

**RBE — Registre des Bénéficiaires Effectifs.** Géré par INPI. Accessible avec authentification.

**BODACC** (bodacc.fr). Bulletin Officiel des Annonces Civiles et Commerciales. Création, modifications, ventes, procédures collectives. Recherchable en ligne.

**INPI**. Marques, brevets, dessins.

**societe.com**, **manageo.fr**, **verif.com**. Agrégateurs gratuits, données partielles.

#### 37.3 Royaume-Uni — Companies House

**Companies House** (gov.uk/government/organisations/companies-house). Registre officiel UK, **entièrement gratuit** et très bien documenté. Standard mondial de transparence.

**Données accessibles.**
- Identité légale complète.
- Dirigeants et anciens dirigeants.
- UBO (depuis 2016, registre PSC — People with Significant Control).
- Comptes annuels publiés.
- Filings (statuts, modifications).

**API gratuite** disponible.

#### 37.4 États-Unis — fragmentation par état

L'enregistrement des sociétés est **étatique** aux US, pas fédéral.

**Delaware** : juridiction préférée. Search via Delaware Department of State.

**Californie, Nevada, Texas, New York, Floride** : portails dédiés par état.

**Pour les sociétés cotées.** **SEC EDGAR** (sec.gov/edgar) : référence pour filings boursiers (10-K, 10-Q, 8-K, proxy statements). Mine d'information sur dirigeants, rémunérations, transactions internes.

**Limites US.**
- Registres étatiques souvent peu transparents (Delaware notamment).
- Pas de registre UBO fédéral (Corporate Transparency Act 2024 ralenti par contentieux).
- Coût d'accès aux comptes détaillés.

#### 37.5 Union Européenne — registres nationaux

**Belgique** : Banque-Carrefour des Entreprises (BCE / CBE), gratuit.

**Allemagne** : Handelsregister, gratuit base, payant pour comptes.

**Pays-Bas** : KvK (Kamer van Koophandel), payant la plupart des données.

**Italie** : Registro Imprese, accès payant pour la plupart des fonctions.

**Espagne** : Registro Mercantil, payant.

**Irlande** : Companies Registration Office (CRO), gratuit.

**Luxembourg** : RCS (Registre de Commerce et des Sociétés), gratuit base.

**Malte** : Companies Registry, gratuit (recherche), payant (extracts).

**Chypre** : Department of Registrar of Companies, gratuit base.

#### 37.6 Paradis fiscaux et juridictions opaques

Les juridictions opaques varient en transparence.

**Plus accessibles.** Malte (UE, donc registre UBO récent), Chypre (UE), Luxembourg.

**Difficiles.** BVI, Cayman Islands, Bermuda, Liechtenstein. Registres existants mais accès très restreint.

**Très difficiles.** Panama (avant Panama Papers), Belize, Seychelles, certaines juridictions Pacifique.

**Pour ces juridictions opaques :**
- **ICIJ leaks** sont la principale source (Panama, Paradise, Pandora, Cyprus Confidential).
- **OCCRP Aleph** agrège.
- Documents internes leakés sur dark web (à manier avec déontologie).

#### 37.7 OpenCorporates : méta-agrégateur

**OpenCorporates** (opencorporates.com) agrège les registres officiels de **140+ juridictions**.

**Forces.**
- Recherche cross-juridiction.
- Graph d'officiers (dirigeants partagés).
- API.
- Données mises à jour.

**Limites.**
- Couverture variable selon registres (parfois superficielle).
- API payante au-delà du freemium.
- Pas tous les UBO (dépend des registres sources).

#### 37.8 ICIJ Offshore Leaks Database

L'**ICIJ Offshore Leaks Database** (offshoreleaks.icij.org) est un agrégateur public des grands leaks.

**Inclus.**
- Panama Papers (2016).
- Paradise Papers (2017).
- Pandora Papers (2021).
- FinCEN Files (2020) — partiel.
- Cyprus Confidential (2023).
- Other leaks plus anciens (Offshore Leaks 2013).

**Forces.**
- Recherche par nom, juridiction.
- Visualisation des liens.
- Sources documentaires partielles consultables.

**Limites.**
- Ce qui est leaké ≠ exhaustif.
- Recoupements nécessaires.
- Données d'années diverses.

#### 37.9 OCCRP Aleph

**Aleph** (aleph.occrp.org) est la plateforme journalistique OCCRP.

**Contenu.**
- Registres corporate (sélection).
- Leaks (sélection des ICIJ et autres).
- Documents publics (filings, contrats publics).
- Listes sanctions, PEP.
- Documents OCCRP propres.

**Accès.**
- Une partie public (gratuit).
- Accès journaliste pour fonctions avancées (sur demande motivée).

#### 37.10 Bureau van Dijk Orbis et alternatives payantes

Pour les usages corporate intensifs :
- **Orbis** (Bureau van Dijk / Moody's) : 400+ M de sociétés mondiales, données financières profondes. ~50-200 k€/an.
- **Sayari** : alternative orientée OSINT, fortes capacités sur Chine, Russie, Iran.
- **Dun & Bradstreet** : standard credit reporting.
- **Bisnode** : européen.

Réservés aux cabinets professionnels avec budget.

#### 37.11 Synthèse — quelle source pour quel besoin

| Besoin | Source prioritaire |
|---|---|
| Société française | Pappers + Infogreffe + BODACC |
| Société UK | Companies House (gratuit, complet) |
| Société UE | OpenCorporates + registre national |
| Société US cotée | SEC EDGAR |
| Société US non cotée | Registre étatique (Delaware, etc.) |
| Paradis fiscal | OpenCorporates + ICIJ leaks + Aleph |
| UBO multi-juridictions | Aleph + Orbis (si dispo) + Pappers + ICIJ |
| Cross-juridiction rapide | OpenCorporates |
| Investigation journalistique | OCCRP Aleph + ICIJ |

-----

### Chapitre 38 — Due diligence, sanctions, PEP et adverse media

#### 38.1 Du registre à l'évaluation de risque

L'investigation corporate ne se limite pas à l'identification structurelle. L'**évaluation de risque** intègre sanctions, PEP, adverse media, contentieux. C'est le cœur de la due diligence moderne.

#### 38.2 Sanctions : tour d'horizon

**OFAC (US Treasury).** Liste SDN (Specially Designated Nationals). Extraterritorialité forte. Sanctions secondaires possibles. ofac.treasury.gov

**UE.** Liste consolidée publiée par la Commission européenne. eeas.europa.eu sanctions database. Effet direct dans tous États membres.

**UK** post-Brexit. OFSI (HM Treasury). Liste consolidée. gov.uk/government/publications/the-uk-sanctions-list

**ONU.** Sanctions ONU obligatoires pour tous États membres. un.org/securitycouncil/sanctions

**Sanctions sectorielles.** Iran, Corée du Nord, Russie (régime complexe depuis 2022), Belarus, Syrie, Venezuela, autres.

#### 38.3 Outils de screening sanctions

**OpenSanctions** (opensanctions.org). **Gratuit**, agrège les listes principales. Standard de référence pour OSINT. API disponible.

**OFAC search engine** (sanctionssearch.ofac.treas.gov). Lookup direct OFAC.

**Sanctions Explorer** (UE). Recherche dans listes UE consolidées.

**Outils payants.**
- **WorldCheck** (Refinitiv) : standard institutionnel. ~5-50 k€/an.
- **Dow Jones Risk & Compliance** : équivalent.
- **Accuity** : transactional screening.
- **Sayari**, **Sigma Ratings**, **ComplyAdvantage** : alternatives modernes.

#### 38.4 PEP — Politically Exposed Persons

**PEP** (Politiquement Exposées) : personnes occupant ou ayant occupé des fonctions publiques importantes. Risque accru de corruption.

**Catégories.**
- PEP étrangères (chefs d'État, ministres, hauts fonctionnaires, juges supérieurs, militaires hauts gradés, dirigeants d'entreprises d'État).
- PEP nationales.
- PEP des organisations internationales (Commission UE, ONU, FMI).
- Membres de famille et associés proches (1er degré famille + business partners).

**Obligation AMLD UE.** Toute transaction avec PEP impose vigilance renforcée.

**Outils.**
- **OpenSanctions** intègre PEP.
- **Wikidata** : listes structurées de PEP.
- **WorldCheck** : standard institutionnel.

**Méthode.** Cross-référencer dirigeants/UBO d'une cible avec listes PEP. Tout match = approfondissement.

#### 38.5 Adverse media — la presse négative

L'**adverse media screening** recherche les mentions négatives dans la presse, blogs, sources publiques.

**Méthode manuelle.**
- Recherche Google `"[nom entité]" (fraude OR scandale OR corruption OR enquête OR sanctions)`.
- Filtres dates.
- Multi-langues.
- Couverture sources locales.

**Outils dédiés.**
- **Google Alerts** (gratuit, suivi continu).
- **Mention.com**.
- **Brandwatch** / **Talkwalker** (payant).
- **LexisNexis** / **Nexis Diligence** (payant institutionnel).
- **NewsBank** (archives presse).

**OpenSanctions** inclut adverse media.

#### 38.6 Contentieux et procédures

**Sources contentieux.**

**France.**
- **JuriCA**, **Légifrance** (jurisprudence).
- **Doctrine.fr** (jurisprudence enrichie).
- BODACC (procédures collectives).
- Presse spécialisée (Les Échos Patrimoine, AGEFI).

**International.**
- **PACER** (US judiciaire).
- **CourtListener** (US).
- **CaseLaw Access** (US).
- **GOV.UK Tribunals** (UK).
- Sources judiciaires nationales.

#### 38.7 KYC, KYB et CSDDD

**KYC** (Know Your Customer). Vigilance client en finance.

**KYB** (Know Your Business). Vigilance partenaire commercial.

**CSDDD** (Corporate Sustainability Due Diligence Directive, UE 2024). Obligation vigilance droits humains et environnement sur supply chain. Mobilise massivement l'OSINT corporate.

#### 38.8 Méthodologie due diligence complète

Pour une **due diligence corporate intégrée** :

1. **Identification fiable** : numéro d'enregistrement, juridiction.
2. **Profil structurel** : forme, capital, dirigeants, actionnaires, UBO.
3. **Activité réelle** : croisement déclaration / activité observable.
4. **Indicateurs financiers** : comptes, évolution, ratio.
5. **Network** : groupe, filiales, sociétés liées via dirigeants partagés.
6. **Screening sanctions** : OFAC, UE, UK, ONU sur entité + dirigeants + UBO.
7. **Screening PEP** : sur dirigeants et UBO.
8. **Adverse media** : multi-langues, multi-périodes.
9. **Contentieux** : recherches juridictions pertinentes.
10. **Risque géographique** : juridictions à risque (paradis fiscaux, pays sanctionnés).
11. **Risque sectoriel** : industrie à risque (extractives, défense, casinos).
12. **Synthèse cotée** : feu vert / orange / rouge avec justification.

#### 38.9 Limites de la due diligence OSINT

- **Incomplétude** : ce qu'on ne trouve pas peut exister.
- **Faux négatifs** : absence de match sanctions ne prouve pas absence de risque.
- **Adverse media biaisé** : couverture variable selon langues / pays.
- **Temporalité** : info datée.

#### 38.10 Synthèse — workflow due diligence

| Étape | Source(s) |
|---|---|
| Identification | OpenCorporates + registre national |
| UBO | RBE + Companies House PSC + leaks |
| Sanctions | OpenSanctions + OFAC + UE + UK |
| PEP | OpenSanctions + Wikidata |
| Adverse media | Google + agrégateurs presse |
| Contentieux | Légifrance + PACER + presse |
| Synthèse | Fiche entité + cotation Admiralty + WEP |

> **MIRAGE — Épisode 8 : Sociétés, dirigeants et UBO**
>
> L'analyste investigue les sociétés liées à Delaunay.
>
> **TechnoVert SAS (France).** Pappers : SIREN identifié, créée 2008, capital 8M €, siège Paris 8e. Dirigeants : Pierre Dubois (Président, DG), Marc Delaunay (DAF, depuis 2019), Sophie Martin (DRH). Activité : 38.32Z (récupération de déchets triés). Comptes 2024 : CA 84.7M €, résultat +3.2M €. UBO : Pierre Dubois (67.3 %), Fonds Industriel SAS (28.4 %), divers minoritaires. Aucune mention de Delaunay au-delà de son rôle DAF. OK pour TechnoVert.
>
> **Pivot vers Delta Consulting Ltd (Malte).** Companies Registry Malte : identifiée. Créée 03/2020. Capital 1200 €. Director unique : Marc Delaunay. Adresse de siège : 24 St. Andrew's Street, Valletta (vérifié sur OpenCorporates : 47 autres entités enregistrées à cette adresse → registered agent typique). Activité déclarée : « consulting services ». Pas de comptes publiés détaillés. UBO déclaré : Marc Delaunay (100 %).
>
> **Cross-search adresse domiciliation.** Les 47 autres entités à la même adresse à Valletta sont listées via OpenCorporates. Examen rapide : 12 d'entre elles ont des directors avec des prénoms français. Cluster de domiciliation française à Malte. Une piste à explorer dans le cadre de l'enquête (qui sont ces autres directors français ? Liens éventuels avec Delaunay ?).
>
> **Verde Holdings (Chypre).** Companies Registry Chypre : identifiée. Créée 01/2022. Capital symbolique. Directors : « Marina Constantinidou » (apparemment locale, possiblement nominee chypriote), « Marc Delaunay ». UBO déclaré (RBE chypriote, accès partiel) : « M. Delaunay 100 % ». Adresse de siège : Limassol, dans un building qui héberge 230 autres sociétés (registered agent classique).
>
> **Recherche complémentaire ICIJ Offshore Leaks Database.** Recherche « Marc Delaunay » : un hit dans Cyprus Confidential (leak 2023). Document publié : un mémo d'un cabinet d'avocats chypriote détaillant la structure de Verde Holdings et mentionnant un flux entrant de Delta Consulting Ltd. **Pièce majeure** — cotation A2 (leak journalistique vérifié par ICIJ).
>
> **Screening sanctions et PEP.** OpenSanctions sur Marc Delaunay, Delta Consulting, Verde Holdings : aucun match. OK.
>
> **Adverse media.** Recherches Google sur ces entités : aucun article négatif identifié. Delaunay n'est pas connu publiquement (DAF de groupe ETI, pas de profil médiatique).
>
> **Cluster identifié.** TechnoVert (employeur) → Delta Consulting (Malte) → Verde Holdings (Chypre). Hypothèse de travail : Delta reçoit des contrats consulting de TechnoVert (à confirmer via BODACC ou comptes), puis transfère partie vers Verde, qui détient probablement des actifs (immobilier, crypto). Le tout sous contrôle Delaunay.
>
> Ce cluster sera approfondi sur le volet flux (MIRAGE 13 — signaux financiers ouverts), patrimoine, et crypto (MIRAGE 14 — renvoi OSINT Crypto).

-----

### Chapitre 39 — Domaines, DNS, WHOIS/RDAP et certificats

#### 39.1 L'infrastructure numérique comme objet d'enquête

L'**infrastructure numérique** d'une entité (domaines, serveurs, certificats, services exposés) est un terrain d'investigation OSINT majeur. Elle révèle :
- Qui possède quoi (via WHOIS, certificats).
- Comment c'est hébergé (révèle prestataires, géographie technique).
- Quelles technologies (révèle compétences, choix techniques).
- Quels services exposés (peut révéler activité).
- Liens entre entités (infrastructure partagée).

Ce chapitre couvre **domaines, DNS, WHOIS, certificats**. Le chapitre 40 couvre **sous-domaines, IP, ASN, BGP**. Le chapitre 41 couvre **surface d'attaque moderne**.

#### 39.2 Le système de noms de domaine

Un **nom de domaine** (`technovert.fr`) est résolu par DNS en adresse(s) IP. Le domaine est enregistré auprès d'un **registrar** (OVH, Gandi, GoDaddy, etc.), qui transmet à un **registre** par TLD (Afnic pour `.fr`, Verisign pour `.com`).

L'enregistrement crée des informations stockées dans le **WHOIS** historiquement, et désormais le **RDAP** (Registration Data Access Protocol).

#### 39.3 WHOIS : l'histoire

Le **WHOIS** historique exposait publiquement :
- Nom et email du propriétaire.
- Coordonnées du contact administratif, technique, facturation.
- Date de création et expiration.
- Registrar.
- Nameservers.

**Rupture RGPD 2018.** Depuis l'entrée en vigueur du RGPD, les registrars EU et la plupart des autres ont **masqué** les données personnelles dans le WHOIS public. Désormais, on voit typiquement « REDACTED FOR PRIVACY » ou un proxy de protection.

**Impact OSINT.** Le WHOIS direct est devenu moins utile pour l'investigation des domaines récents. Mais :
- WHOIS reste utile pour les domaines anciens (avant 2018).
- WHOIS historique conserve les enregistrements antérieurs.
- WHOIS de certaines juridictions reste partiellement ouvert.

#### 39.4 RDAP : le successeur

Le **RDAP** (Registration Data Access Protocol) standardise l'accès aux données d'enregistrement. Fonctionnellement, le contenu est similaire au WHOIS (avec mêmes restrictions RGPD), mais format JSON, query HTTPS.

**Outils.**
- `rdap` CLI (linux).
- Sites RDAP : rdap.org, search.arin.net.
- API.

#### 39.5 Outils WHOIS/RDAP modernes

**Sites publics.**
- **whois.icann.org** : standard.
- **DomainTools** (domaintools.com) : extensions payantes puissantes.
- **WhoIsHistory** : historique.
- **ViewDNS.info** : ensemble d'outils gratuits.
- **CentralOps**.

**CLI.**
```bash
whois technovert.fr
rdap technovert.fr
```

#### 39.6 WHOIS historique : pépite OSINT

Le **WHOIS historique** (DomainTools, WhoIsHistory) conserve les enregistrements WHOIS **antérieurs à 2018**. Pour les domaines créés avant cette date, on peut souvent retrouver le propriétaire originel.

**Cas d'usage.** Un domaine `delaunay-patrimoine.fr` créé en 2017 (avant RGPD) → WHOIS historique peut révéler email et coordonnées du propriétaire à cette époque.

**Outils.**
- **DomainTools Historical WHOIS** (payant, ~$95/mois).
- **WhoIsHistory** (alternative moins riche).
- **WHOISology** (commercial).

C'est l'un des cas où l'investissement dans un outil payant se justifie.

#### 39.7 DNS : enregistrements

Le **DNS** (Domain Name System) résout les noms en IPs et fournit d'autres informations via différents types d'enregistrements.

**Types d'enregistrements clés.**
- **A** : IPv4.
- **AAAA** : IPv6.
- **MX** : serveurs mail.
- **NS** : nameservers (DNS).
- **TXT** : texte libre (souvent SPF, DKIM, vérifications domaines tiers).
- **CNAME** : alias.
- **SOA** : autorité.

**Outils.**
- `dig` (CLI Linux/Mac).
- `nslookup` (multi-OS).
- **DNSDumpster** (dnsdumpster.com) : analyse rapide.
- **SecurityTrails** (securitytrails.com) : historique DNS riche, payant.
- **ViewDNS.info**.

```bash
dig technovert.fr ANY
dig technovert.fr MX
dig _dmarc.technovert.fr TXT
```

#### 39.8 DNS records révélateurs

**MX records.** Révèlent le fournisseur email (Google Workspace, Microsoft 365, OVH, etc.).

**TXT records.** Souvent contiennent :
- SPF (qui peut envoyer email depuis ce domaine).
- DKIM (signature).
- Vérifications domaines tiers (Google Site verification, Atlassian, Office 365, Adobe, Stripe, etc.) → révèle quels services tiers sont utilisés.

**NS records.** Révèlent l'opérateur DNS (Cloudflare, OVH, AWS Route 53). Cohérence avec hébergement supposé.

**Exemple révélateur.**
```
technovert.fr TXT "google-site-verification=abc..."
technovert.fr TXT "atlassian-domain-verification=xyz..."
technovert.fr TXT "stripe-verification=def..."
```
→ TechnoVert utilise Google, Atlassian (Jira/Confluence), Stripe.

#### 39.9 Passive DNS

Le **passive DNS** archive l'historique des résolutions DNS observées. Permet de voir l'évolution d'un domaine.

**Cas d'usage.**
- Un domaine pointait vers IP X en 2020, vers IP Y en 2024 → évolution d'hébergement.
- Sous-domaine ayant existé puis disparu.
- Reconstruction d'infrastructure ancienne.

**Outils.**
- **SecurityTrails** : historique passive DNS riche.
- **PassiveTotal / RiskIQ** (Microsoft).
- **Farsight DNSDB** (industrie référence).
- **DNSDumpster** (limité gratuit).
- **CIRCL Passive DNS** (CERT.lu, accès gratuit chercheurs).

#### 39.10 Certificats TLS : pépite moderne

Les **certificats TLS/SSL** sont émis pour authentifier les sites HTTPS. Leur **transparence (Certificate Transparency, CT)** depuis 2018 a créé une mine OSINT majeure.

**Principe CT.** Chaque émission de certificat est loguée publiquement dans des logs CT (Google, Cloudflare, Let's Encrypt, etc.). Ces logs sont consultables.

**Ce qui est exposé.**
- Le **domaine principal** (Common Name CN).
- Les **Subject Alternative Names (SAN)** — domaines alternatifs couverts par le même certificat. Peut révéler des dizaines de domaines liés.
- Date d'émission, expiration, autorité émettrice.
- Empreinte du certificat (peut être utilisée pour corrélations cross-domaines).

**Outils.**
- **crt.sh** (crt.sh) : interface publique sur les logs CT. Gratuit, puissant.
- **Censys** : recherche avancée par certificats.
- **Shodan** : intègre certificats.

```
# Recherche crt.sh
crt.sh?q=technovert.fr
crt.sh?q=%25.technovert.fr   # tous les sous-domaines
```

**Cas d'usage.** Si TechnoVert a émis un certificat couvrant `technovert.fr` + `intranet.technovert.fr` + `dev.technovert.fr` + `staging.technovert.fr`, ces sous-domaines sont **révélés** même s'ils ne sont pas accessibles publiquement.

#### 39.11 Pivot infrastructure → autres domaines

Un même propriétaire opère souvent plusieurs domaines. Les pivots :

**Email WHOIS commun.** Si deux domaines ont le même email administrateur (visible si pre-2018), ils sont liés.

**Nameservers communs.** Pas un signal fort (beaucoup de domaines partagent OVH ou Cloudflare), mais NS très spécifique peut être discriminant.

**SOA email commun** : email administratif technique dans le SOA record.

**Certificats partagés** : un certificat couvrant plusieurs domaines révèle relation.

**Hostings communs** (IP/ASN partagés — Ch.40).

**Trackers / analytics communs** : code Google Analytics, Facebook Pixel, Mixpanel partagé entre sites = signal fort de propriété commune.

**Outils trackers.**
- **DNSlytics** (dnslytics.com) : reverse Google Analytics, AdSense.
- **SpyOnWeb**.
- **NerdyData**.

#### 39.12 Méthodologie complète domaine

Pour investiguer un domaine cible :

1. **WHOIS actuel** : minimal (RGPD).
2. **WHOIS historique** : DomainTools si pre-2018.
3. **DNS records** : A, MX, NS, TXT, SOA, etc.
4. **Passive DNS** : historique résolutions.
5. **Certificats TLS** : crt.sh pour SAN et sous-domaines.
6. **Trackers analytics** : DNSlytics pour cross-références.
7. **Sous-domaines** : voir Ch.40.
8. **Capture web** : archive.org + archive.today pour contenu historique.
9. **Technologies** : Wappalyzer, BuiltWith.
10. **Pivot** : domaines liés via mêmes traits.

> **MIRAGE — Épisode 9 : Infrastructure web et domaines**
>
> L'analyste investigue l'infrastructure web de la campagne de désinformation.
>
> **Domaine `verites-technovert.com`.** WHOIS actuel : masqué RGPD. WHOIS historique (DomainTools) : créé 12 octobre 2025, registrar Namecheap, email contact `proxy@withheldforprivacy.com` (masqué). DNS : NS Namecheap default, hébergement Cloudflare (IP origine masquée). MX : aucun mail handler configuré.
>
> **Certificat TLS** (crt.sh). Recherche : un certificat Let's Encrypt émis le 12 octobre 2025 couvre `verites-technovert.com` + `www.verites-technovert.com`. Pas de SAN révélateur d'autres domaines liés.
>
> **Trackers analytics.** Le site utilise Google Analytics avec un Property ID identifié. DNSlytics : reverse search sur ce GA ID → un autre site utilise le même : `info-finance-eu.com`. **Pivot critique** : les deux sites de désinformation sont liés par la même Property GA, donc opérés très probablement par le même opérateur.
>
> **Domaine `info-finance-eu.com`.** WHOIS historique : créé 18 octobre 2025 (6 jours après verites-technovert.com). Registrar Namecheap (identique). Email contact masqué. Trackers identiques. NS et hébergement Cloudflare.
>
> **Hypothèse confortée.** Les deux domaines sont opérés par le même opérateur, créés à 6 jours d'intervalle, utilisant la même stack technique. Cluster de désinformation confirmé.
>
> **Recherche complémentaire** : `crt.sh?q=verites-technovert.com` et `crt.sh?q=info-finance-eu.com` ne révèlent pas d'autres certificats liés (l'opérateur a évité de mutualiser).
>
> **Pivot suivant** : analyser le contenu publié sur les deux sites, archiver immédiatement (anticipation de retrait), identifier qui contribue (auteurs déclarés ? métadonnées documents ?), identifier les autres canaux d'amplification (cluster X de 8 comptes, canaux Telegram).
>
> **Cotation cluster désinformation.** Existence confirmée A1 (sites observables). Lien entre les deux sites : B1 (GA partagé + cohérences temporelles et techniques). Lien au commanditaire (Delaunay ou son entourage) : à confirmer (pas encore de pivot direct vers Delaunay).

-----

### Chapitre 40 — Sous-domaines, IP, ASN, BGP et exposition technique

#### 40.1 Au-delà du domaine principal

Le **domaine principal** (`technovert.fr`) n'est que la pointe de l'iceberg. Les organisations opèrent typiquement des dizaines à des milliers de **sous-domaines** (`intranet.technovert.fr`, `dev.technovert.fr`, `mail.technovert.fr`, `staging-eu.technovert.fr`). Identifier l'arbre complet des sous-domaines est un objectif majeur de l'investigation infrastructure.

#### 40.2 Découverte de sous-domaines

**Sources passives (sans interaction avec la cible).**
- **Certificate Transparency** (crt.sh) : sous-domaines couverts par certificats émis.
- **Passive DNS** (SecurityTrails, DNSDumpster).
- **Search engines** : Google `site:technovert.fr -www`.
- **Wayback Machine** : URL historiques crawled.
- **DNS bruteforce list publics** (subdomains.txt sur GitHub).

**Sources actives (interaction modérée).**
- Bruteforce DNS (Amass, subfinder).
- ZoneTransfer (très rare, si serveur mal configuré).

**Outils combinés.**

**Amass** (OWASP). Le standard. Combine passif + actif. CLI.
```bash
amass enum -d technovert.fr -passive
amass enum -d technovert.fr -active
```

**subfinder** (ProjectDiscovery). Rapide, passif.
```bash
subfinder -d technovert.fr
```

**Sublist3r**, **assetfinder**, **findomain** : alternatives.

**Pour automatiser** : combiner les sorties (`sort -u`).

#### 40.3 Sous-domaines révélateurs

Les sous-domaines révèlent :
- **Services internes** (`intranet.`, `crm.`, `erp.`, `wiki.`).
- **Environnements** (`dev.`, `staging.`, `preprod.`, `test.`).
- **Géographies** (`fr.`, `de.`, `apac.`, `us.`).
- **Filiales** (`subsidiary.`).
- **Outils tiers déployés** (`okta.`, `slack.`, `confluence.`).

Un sous-domaine `dev.api.payments.technovert.fr` révèle l'existence d'une API de paiements en développement.

#### 40.4 Adresses IP : résolution et géolocalisation

Une fois les sous-domaines découverts, **résoudre en IPs** révèle l'hébergement.

**Outils.**
- `dig` : résolution DNS.
- `host`.
- **ipinfo.io**, **ipgeolocation.io** : géolocalisation et infos IP.
- **MaxMind GeoIP** : standard.

**Information par IP.**
- **Géolocalisation** : pays, ville (précision variable).
- **ASN** (Autonomous System Number) : qui possède l'IP.
- **Organization** : opérateur.
- **Hostname reverse** : nom DNS associé.
- **Services ouverts** (via Shodan, Censys).

#### 40.5 ASN : Autonomous System Numbers

L'**ASN** identifie l'organisation propriétaire d'un bloc IP. Exemples :
- AS15169 : Google.
- AS16509 : Amazon AWS.
- AS13335 : Cloudflare.
- AS16276 : OVH.

**Outils.**
- **Hurricane Electric BGP** (bgp.he.net) : standard.
- **bgp.tools** (alternative moderne).
- **RIPEstat** (RIPE NCC) : Europe particulièrement.

**Cas d'usage.** Toutes les IPs de TechnoVert sont en AS16276 (OVH) → TechnoVert héberge chez OVH. Sauf si une IP est en AS13335 (Cloudflare) → utilisation Cloudflare devant.

#### 40.6 BGP : routage Internet

Le **BGP** (Border Gateway Protocol) est le protocole de routage entre ASNs. Pour OSINT, peu d'usage direct (sauf cas avancés CTI), mais l'observation BGP peut révéler :
- Changements d'opérateur.
- Anomalies de routage (signal d'incident).
- Cartographie de connectivité.

#### 40.7 Reverse IP : autres sites hébergés

Une **IP partagée** (typique en mutualisé) héberge potentiellement des centaines de sites. Reverse IP révèle ces sites.

**Outils.**
- **DomainTools Reverse IP** : payant.
- **ViewDNS.info reverse IP** : gratuit limité.
- **Shodan reverse**.

**Cas d'usage.** Identifier toutes les autres entités hébergées sur la même IP → peut révéler partenaires, infrastructure commune.

#### 40.8 Shodan, Censys, FOFA, ZoomEye

Voir Ch.21 pour la présentation. Sur l'infrastructure d'une entité :

**Shodan dorks.**
```
hostname:technovert.fr
ssl.cert.subject.cn:technovert
org:"TechnoVert"
```

**Révèle.** Services ouverts (HTTP, SSH, FTP, RDP, RTSP, MQTT, ICS), bannières, versions, vulnérabilités connues, géographie.

#### 40.9 GreyNoise et bruit Internet

**GreyNoise** filtre le « bruit » Internet (IPs qui scannent constamment).

**Cas d'usage OSINT.** Une IP suspecte qui contacte la cible : est-ce un scan opportuniste (bruit) ou un scan ciblé ? GreyNoise classe.

#### 40.10 Méthodologie complète infrastructure

Pour investiguer l'infrastructure technique d'une entité :

1. **Domaine principal** (Ch.39).
2. **Sous-domaines** : Amass / subfinder passif puis actif modéré.
3. **Résolution IPs** : `dig` sur chaque sous-domaine.
4. **ASN** : Hurricane Electric, bgp.tools.
5. **Reverse IP** : autres sites hébergés.
6. **Services exposés** : Shodan + Censys.
7. **Technologies** : Wappalyzer + BuiltWith sur les sites.
8. **Cartographie** : graphe entités → domaines → sous-domaines → IPs → services.

#### 40.11 Limites légales

**Scan actif (nmap, masscan).** Légalité variable selon juridiction. En France, scan modéré sans tentative d'exploitation est généralement toléré. **Scan agressif** = zone pénale (art. 323-1).

**Recommandation.** Privilégier outils passifs (Shodan, Censys agrègent des scans tiers). Scans actifs uniquement avec autorisation explicite.

-----

### Chapitre 41 — Surface d'attaque moderne

#### 41.1 De l'infrastructure à la surface d'attaque

Au-delà de l'inventaire, l'**analyse de surface d'attaque** identifie les **points d'exposition** d'une organisation : services mal configurés, secrets exposés, données fuitées, technologies vulnérables.

Cette analyse intéresse l'OSINT pour :
- **Due diligence** : évaluer la maturité sécurité d'un partenaire/cible.
- **CTI** : comprendre ce qu'un attaquant verrait.
- **Investigation** : identifier l'origine d'un incident.
- **Bug bounty** : recherche éthique de vulnérabilités.

#### 41.2 Cloud et SaaS exposés

**Buckets S3 / Azure Blob / GCS.** Stockage cloud souvent mal configuré.

**Outils.**
- **Bucket finders** (S3Scanner, etc.).
- **GrayhatWarfare** : index public de buckets ouverts.
- **Cloud Storage Finder**.

**Cas d'usage.** Vérifier si TechnoVert a des buckets S3 publics potentiellement exposant des données.

**Précaution juridique.** Identifier un bucket ouvert ≠ y accéder. Consulter peut basculer en Bluetouff. En cas de découverte, signaler à l'organisation.

#### 41.3 GitHub leaks et secrets exposés

**GitHub** est une mine de secrets accidentellement exposés : API keys, credentials, configurations internes.

**Outils.**
- **GitHub Code Search** (avec opérateurs).
- **gitleaks** : scan local de repos.
- **TruffleHog** : détection de secrets.
- **GitGraber**.

**Dorks GitHub.**
```
"technovert" "password"
"@technovert.fr" extension:env
"DB_PASSWORD" "technovert"
filename:.env "technovert"
```

**Pour due diligence.** Identifier l'exposition GitHub d'une cible révèle :
- Maturité sécurité interne.
- Secrets actuellement valides (risque).
- Identités d'employés (via commits).

**Déontologie.** Si découverte de secrets actifs, signaler à l'organisation. Ne pas exploiter.

#### 41.4 Technologies web et empreinte applicative

Identifier les **technologies utilisées** par un site révèle :
- Stack technique (Apache, Nginx, PHP, Python, Node.js).
- Frameworks (Laravel, Django, React, Vue).
- CMS (WordPress, Drupal, Joomla).
- Plugins, librairies.
- Outils analytics (GA, Mixpanel, Hotjar).
- CDN, hébergement.

**Outils.**
- **Wappalyzer** (extension navigateur, gratuit).
- **BuiltWith** (builtwith.com) : profile complet, payant pour fonctions avancées.
- **WhatRuns** : alternative.

**Cas d'usage OSINT.** Identifier les technologies vieilles ou vulnérables. Identifier les correspondants tiers (révèle écosystème).

#### 41.5 Typosquatting et domaines frauduleux

Le **typosquatting** est l'enregistrement de domaines proches d'un domaine légitime pour piéger les utilisateurs (`technovrt.fr`, `technowert.fr`, `technovert-rh.com`).

**Outils.**
- **DNSTwist** : génère et vérifie les variantes.
- **URLCrazy**.
- **dnstwister.report**.

**Cas d'usage.**
- Identifier les domaines suspects autour de la cible.
- Détection précoce de campagnes de phishing visant la cible.
- Cluster de domaines frauduleux (un même attaquant enregistre plusieurs typosquats).

#### 41.6 Email exposure et compromissions

Voir Ch.42 et Ch.43 pour le détail. L'exposition d'emails dans des breaches est un volet majeur de la surface d'attaque.

#### 41.7 Surface d'attaque continue (ASM)

**ASM** (Attack Surface Management) : monitoring continu de la surface d'attaque.

**Outils commerciaux.**
- **Bitsight**.
- **SecurityScorecard**.
- **RiskIQ** (Microsoft).
- **Censys Continuous**.
- **Shodan Monitor**.

**Pour OSINT.** Souvent réservé aux usages CTI / cybersécurité, mais certains éléments accessibles en consultation ponctuelle.

#### 41.8 Audit de surface d'attaque OSINT : workflow

1. **Inventaire domaines + sous-domaines** (Ch.39-40).
2. **Inventaire IPs** + ASN.
3. **Scan passif** (Shodan, Censys) : services exposés.
4. **Cloud assets** : buckets, Azure, GCS via outils dédiés.
5. **GitHub** : secrets exposés.
6. **Technologies** : Wappalyzer, BuiltWith.
7. **Typosquatting** : DNSTwist.
8. **Breaches emails** : HIBP, DeHashed (Ch.42).
9. **Stealer logs** : Hudson Rock, SpyCloud (Ch.43).
10. **Synthèse de risque**.

-----

### Chapitre 42 — Breaches, leaks et pastebins

#### 42.1 L'écosystème des données fuitées

Depuis 15 ans, l'écosystème des **breaches** (intrusions menant à exfiltration de données) et **leaks** (publications de données) a explosé. Yahoo, LinkedIn, Adobe, Dropbox, Equifax, T-Mobile, Marriott, plus récemment 23andMe, MOVEit, etc. — des milliards de credentials et informations personnelles circulent.

Pour l'analyste OSINT, ces données représentent une **source riche mais juridiquement et déontologiquement complexe**.

#### 42.2 HIBP — Have I Been Pwned

**HIBP** (haveibeenpwned.com) est le standard public.

**Capacités.**
- Recherche par email : « cet email est-il dans des breaches connues ? ».
- Recherche par téléphone (limitée).
- API : Pwned Passwords (vérification password sans le révéler).

**Sources.** Troy Hunt vérifie chaque breach avant inclusion. Pas tous les leaks (filtré).

**Tarification.** Lookup gratuit individuel, API payante ($3.95/mois pour API key).

#### 42.3 DeHashed

**DeHashed** (dehashed.com) est plus complet, plus profond, plus controversé.

**Capacités.**
- Recherche par email, username, IP, password hash, name, address, phone.
- Données dans certaines breaches en clair (selon ce que le leak originel contenait).
- Pivots multi-fields.

**Tarification.** ~$5/jour ou abonnement mensuel ~$30/mois.

**Précaution.** Les données peuvent inclure passwords. **Ne jamais utiliser** pour tenter d'accéder à un compte. Usage strictement d'investigation.

#### 42.4 Intelligence X (IntelX)

**IntelX** (intelx.io) explore **deep web et leaks**.

**Capacités.**
- Recherche par email, username, domaine, BTC, IP, passport, etc.
- Pastes, dumps, archives Tor.
- Index très large.
- Snapshots historiques.

**Tarification.** Plus chère, orientée institutionnel.

#### 42.5 Snusbase, LeakPeek et autres

**Snusbase**, **LeakPeek** : alternatives variées, qualité et légalité variables. Vérification du fournisseur recommandée.

#### 42.6 ICIJ leaks — Pandora, Panama, etc.

Les **leaks journalistiques majeurs** sont différents techniquement (documents internes, pas credentials), mais constituent une famille apparentée :

- **Panama Papers** (2016) : 11.5 M docs Mossack Fonseca.
- **Paradise Papers** (2017) : 13.4 M docs Appleby.
- **Pandora Papers** (2021) : 11.9 M docs multi-cabinets.
- **FinCEN Files** (2020) : 2100 Suspicious Activity Reports.
- **Cyprus Confidential** (2023) : leak chypriote majeur.

**Accès.** ICIJ Offshore Leaks Database (extracts + métadonnées). Documents bruts réservés aux journalistes ICIJ partenaires.

#### 42.7 Pastebins

**Pastebins** (pastebin.com, paste.ee, ghostbin, etc.) hébergent des bouts de texte, souvent éphémères. Utilisés pour partager du code, mais aussi pour publier des leaks.

**Outils.**
- **PasteHunter** : monitoring de pastes.
- **Searches IntelX** indexent pastes.
- **Pastes archive** sur archive.org parfois.

#### 42.8 Cadre légal d'usage

**Pour les LEA.** Largement autorisés à utiliser les leaks pour orientation.

**Pour les journalistes.** Liberté de presse et intérêt public sont des protections fortes (jurisprudence française et européenne).

**Pour les analystes privés non-journalistes.** Zone grise :
- **Consulter** un leak public reste généralement toléré.
- **Exploiter** (intégrer dans rapport commercial, citer comme source) est juridiquement plus risqué, particulièrement si données issues d'un piratage avéré.

**Règle pratique.**
- Documenter l'origine.
- Ne pas reproduire les données brutes.
- Citer les analyses publiées par sources autorisées (ICIJ notamment) plutôt qu'accès aux dumps.
- Consultation avocat en cas de doute.

#### 42.9 Pivots OSINT depuis breaches

Une fois un email/username confirmé dans une breach, plusieurs pivots :

- **Password reuse** : si un password leakée pour un compte est testé sur un autre compte de la même personne. **Ne jamais exploiter** (CFAA US, art. 323-1 FR). Mais signal que la personne réutilise → faiblesse OPSEC.
- **Date de breach** : situe la création du compte avant la date de breach.
- **Username dans breach** : ouvre Sherlock pour autres plateformes.
- **Phone dans breach** : pivot téléphone.

#### 42.10 Minimisation et déontologie

Le travail avec breaches impose :
- **Minimisation** : utiliser uniquement ce qui sert l'enquête.
- **Non-publication** : pas de diffusion des données brutes.
- **Stockage chiffré** : si conservation nécessaire.
- **Destruction** à fin d'enquête.

> **Principe.** Les breaches sont des sources d'orientation, pas des preuves directes. Une affirmation « Cet email apparaît dans la breach LinkedIn 2012 » est une orientation (cotation prudente). Pas une preuve d'identité.

-----

### Chapitre 43 — Infostealers et stealer logs

#### 43.1 Le phénomène stealer logs

Les **infostealers** (malwares voleurs d'informations : RedLine, Vidar, Raccoon, Lumma, Stealc, etc.) sont devenus une économie criminelle massive depuis 2020-2021. Ils infectent des PC personnels, exfiltrent les données stockées dans les navigateurs (cookies, mots de passe), wallets crypto, fichiers récents.

Les **stealer logs** (dumps de ces exfiltrations) sont vendus ou publiés sur Telegram, marketplaces dark web, forums. Volume astronomique : des millions de logs par mois.

#### 43.2 Anatomie d'un stealer log

Un log typique contient :
- **Credentials browser** : URL + email + password sauvegardés.
- **Cookies session** : peuvent permettre session hijacking.
- **Wallets crypto** : fichiers wallet, seeds (rare en clair).
- **Autofill data** : adresses, cartes (partielles).
- **System info** : machine name, user, IP, OS.
- **Screenshot** parfois.

#### 43.3 Marché stealer logs

**Telegram** est la plateforme principale.

**Canaux observables (en consultation passive).**
- Dumps gratuits (logs « publics ») destinés à attirer.
- Channels payants (private logs).
- Marketplaces brokers.

**Tarifs.** Quelques cents par log basique, plusieurs $ pour log avec wallets crypto ou credentials premium.

#### 43.4 Outils OSINT pour stealer logs

**Hudson Rock** (hudsonrock.com). Service commercial spécialisé. Permet de tester si un email est dans des logs récents.

**SpyCloud** (spycloud.com). Standard institutionnel CTI. Très complet.

**LeakIX** : alternative.

**Telegram observation directe** : compte d'investigation observe les canaux publics.

#### 43.5 Cas d'usage OSINT

**Pour investigation personne.** Tester si l'email perso de la cible apparaît dans des logs → révèle compromission, peut révéler comptes utilisés (Binance, ProtonMail, etc.).

**Pour CTI.** Identifier les machines compromises dans une organisation cible.

**Pour due diligence.** Maturité sécurité.

#### 43.6 Cadre légal et déontologique

**Consultation.** Légalement plus risqué que breaches publiques car les logs sont issus d'intrusions illégales. Toléré en cadre d'investigation documenté, à manier avec précaution.

**Pas d'exploitation** des credentials (CFAA, art. 323-1).

**Documentation.** Capture du résultat de recherche (Hudson Rock par exemple), pas téléchargement des logs bruts.

#### 43.7 Stealer logs sur Telegram : méthodologie

1. Compte d'investigation Telegram dédié.
2. Identification de canaux publics (Telegago).
3. Observation passive (joindre, ne pas interagir).
4. Recherche par email dans channels gratuits / search bots disponibles.
5. Capture du résultat (sans télécharger le log entier).
6. Documentation rigoureuse.

#### 43.8 Limites

- Les logs peuvent contenir des erreurs.
- Date d'infection variable.
- Email peut être valide mais compte de longue date inutilisé.
- Faux logs (fabriqués pour usage marchand).

> **MIRAGE — Épisode 10 : Breaches, leaks et stealer logs**
>
> L'analyste poursuit l'investigation de Delaunay via breaches.
>
> **HIBP sur `marc.delaunay76@gmail.com`** : 6 hits dans breaches (LinkedIn 2012, Adobe 2013, Dropbox 2012, MyFitnessPal 2018, Disqus 2017, Canva 2019). Confirmation que c'est un email actif depuis 2010+.
>
> **DeHashed sur même email** : confirme et ajoute Anti-Public Combo List, Collection #1. Pas de pivots majeurs au-delà de l'identification du compte.
>
> **Hudson Rock** : test sur `marc.delaunay76@gmail.com`. **Hit positif** : machine compromise par RedLine Stealer en septembre 2025, IP française (Paris), 47 credentials capturés. Liste des URLs : LinkedIn, ProtonMail (compte perso), Binance, Apple ID, plusieurs e-commerces, et notamment **Binance** avec credentials.
>
> **Capture sur Telegram (compte invest)** : recherche du dump dans canal `@cloudsec_dumps` (visité au MIRAGE 7). Trouvé : un dump du 15 septembre 2025 incluant `marc.delaunay76@gmail.com`. Capture en lecture seule : 47 credentials, dont compte Binance (URL + email + password en clair partiellement masqué dans la capture).
>
> **Implications majeures.**
> 1. Delaunay utilise un compte Binance personnel. **Pivot crypto majeur** — à explorer dans MIRAGE 14 (renvoi OSINT Crypto vFULL).
> 2. La compromission est récente (septembre 2025) → credentials probablement encore frais à la date du dump.
> 3. Le compte ProtonMail perso révèle une infrastructure email plus complexe que l'email Gmail seul (Delaunay a un compte chiffré pour communications sensibles).
> 4. La compromission étant due à un infostealer, ce n'est pas un signe de compétence de la part des attaquants ciblant Delaunay — c'est une infection opportuniste classique. Mais le **rapport offre des sélecteurs**.
>
> **Précautions OPSEC déontologiques.**
> - Aucun téléchargement du log (consultation visuelle uniquement).
> - Aucune tentative d'usage des credentials.
> - Documentation : capture horodatée + cotation B2 (source secondaire de qualité moyenne).
> - Le rapport mentionnera l'existence du log pour orientation procédure (PNF peut réquisitionner le log s'il devient pertinent).

-----

### Chapitre 44 — Dark Web et DARKINT : panorama opérationnel

#### 44.1 Définition et périmètre

Le **dark web** désigne l'ensemble des services accessibles uniquement via des réseaux de routage anonymisé : principalement **Tor** (The Onion Router), mais aussi **I2P** (Invisible Internet Project), **Freenet**, et plus récemment des solutions émergentes.

Le **DARKINT** (Dark Web Intelligence) est la discipline OSINT spécialisée dans la collecte et analyse de ces espaces.

Ce chapitre fournit une **vue opérationnelle**. Pour la profondeur (architecture Tor, marketplaces, leak sites, méthodologies LEA, IA criminelle dans le dark web), **renvoi systématique vers Dark Web vFULL**.

#### 44.2 Tor : architecture brève

**Tor** route le trafic via 3 relais successifs (entry guard, middle relay, exit node). Chaque relais ne connaît qu'une partie du chemin. Les services `.onion` sont accessibles uniquement via Tor.

**Anonymat fourni.** L'IP source est masquée. Mais OPSEC stricte nécessaire au-delà.

**Tor Browser.** Le navigateur officiel. Préconfigurations privacy par défaut.

#### 44.3 Marketplaces dark web

**Évolution 2020-2026.** AlphaBay (fermé 2017, revenu 2021, refermé 2023), Hydra (RUS, fermé 2022 par opération germano-russe), Genesis Market (fermé 2023), divers successeurs en émergence-fermeture continue.

**Typologie.**
- Marketplaces drogues/fraudes (Mainstream).
- Forums clandestins cybercriminels (XSS, Exploit — surface borderline ; Russian Anonymous Marketplace en dark web).
- Leak sites ransomware (Conti, LockBit, etc.).
- Carding shops.
- Services divers (faux papiers, etc.).

**Pour OSINT.**
- **Consultation** : possible, OPSEC stricte.
- **Interaction** : réservée LEA et journalisme spécialisé strictement encadré.
- **Achat** : sortie immédiate du périmètre OSINT pur.

#### 44.4 Leak sites ransomware

Les **leak sites** des gangs ransomware (Conti, LockBit, ALPHV/BlackCat, AlphV) publient les données des victimes qui n'ont pas payé.

**Pour OSINT corporate.**
- Vérifier si une entité figure sur un leak site = elle a été victime de ransomware.
- Données exposées = peuvent contenir des informations stratégiques.

**Approche.**
- Monitoring via outils CTI (Recorded Future, Flashpoint, KELA, Flare, Searchlight).
- Vue indirecte via rapports publiés (DarkOwl, Cybersixgill).

#### 44.5 Outils de monitoring dark web

**Outils commerciaux.**
- **Flare** : monitoring dark web et leaks.
- **Recorded Future** : standard institutionnel CTI.
- **KELA** : focus dark web.
- **Cybersixgill** : standard CTI.
- **DarkOwl** : indexation deep web.
- **Searchlight Cyber**.

Tous payants, abonnements lourds (5-50 k€/an).

#### 44.6 Méthodologie de consultation prudente

Si consultation directe nécessaire :

1. **VM Whonix** ou Tails sur clé USB.
2. **Tor Browser** uniquement.
3. **Pas de comptes** sauf strictement nécessaire (compte d'investigation dédié, créé sur cette VM uniquement).
4. **Pas d'interaction** active.
5. **Capture** via SingleFile dans la VM.
6. **Pas de téléchargement de contenus illégaux** (CSAM, données piratées exploitables) — **refus immédiat et signalement** si rencontre.
7. **Documentation** stricte dans journal d'enquête.

#### 44.7 Cas d'usage OSINT légitime

**Investigation corporate.** Vérifier si données d'une cible figurent sur leak sites.

**Investigation criminelle (consultative).** Identifier réseaux, méthodes, prix.

**CTI.** Monitoring d'acteurs malveillants visant l'organisation cliente.

**Journalisme.** Documentation de l'écosystème criminel.

**Recherche.** Académique, droits humains.

#### 44.8 Renvoi systématique Dark Web vFULL

Le présent cours s'arrête ici sur le dark web. **Tout approfondissement** (architecture détaillée, marketplaces vivantes, forums, opérations LEA, IA criminelle dans le dark web, OPSEC avancée, attribution) est traité dans **Dark Web vFULL**.

Ce renvoi est explicite parce que :
- Le dark web est un domaine où l'erreur (technique ou déontologique) a des conséquences graves.
- L'écosystème évolue très vite (marketplaces qui ouvrent / ferment mensuellement).
- Les protocoles d'investigation diffèrent du dark web vers le surface web.

> **MIRAGE — Épisode 15 : Piste dark web, renvoi Dark Web vFULL**
>
> L'analyste s'interroge sur d'éventuelles traces de Delaunay ou TechnoVert sur le dark web.
>
> **Vérification leak sites ransomware.** Recherche dans agrégateurs publics (DarkTracer, RansomLook) : aucune mention de TechnoVert. Pas victime ransomware identifiée.
>
> **Vérification marketplaces.** Hors de portée pour OSINT privé sans outil CTI premium. Si pertinence forte se révèle, escalade vers partenaire CTI ou inclusion dans réquisition judiciaire ultérieure.
>
> **Conclusion sur ce volet.** Aucune piste dark web significative identifiée à ce stade. Le cluster de désinformation observé semble opérer principalement sur surface web (X, Telegram, blogs). Pas de bascule dark web nécessaire pour l'enquête MIRAGE.
>
> **Documentation.** Le rapport mentionnera cette vérification (« couverture dark web limitée à la consultation de leak sites publics ; aucune mention de TechnoVert identifiée ; couverture marketplaces réservée à des outils CTI non mobilisés ») pour transparence sur les limites.
>
> Pour les enquêtes nécessitant approfondissement dark web (criminalité organisée, ransomware victims, marketplaces narcotiques), **renvoi vers Dark Web vFULL**.

-----
