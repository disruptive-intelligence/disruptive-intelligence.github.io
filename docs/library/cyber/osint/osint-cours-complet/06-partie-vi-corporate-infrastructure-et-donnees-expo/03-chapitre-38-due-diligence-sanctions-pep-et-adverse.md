---
title: Chapitre 38 — Due diligence, sanctions, PEP et adverse media
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VI — Corporate, infrastructure et données exposées
  - index.md
---

## 38.1 Du registre à l'évaluation de risque

L'investigation corporate ne se limite pas à l'identification structurelle. L'**évaluation de risque** intègre sanctions, PEP, adverse media, contentieux. C'est le cœur de la due diligence moderne.

## 38.2 Sanctions : tour d'horizon

**OFAC (US Treasury).** Liste SDN (Specially Designated Nationals). Extraterritorialité forte. Sanctions secondaires possibles. ofac.treasury.gov

**UE.** Liste consolidée publiée par la Commission européenne. eeas.europa.eu sanctions database. Effet direct dans tous États membres.

**UK** post-Brexit. OFSI (HM Treasury). Liste consolidée. gov.uk/government/publications/the-uk-sanctions-list

**ONU.** Sanctions ONU obligatoires pour tous États membres. un.org/securitycouncil/sanctions

**Sanctions sectorielles.** Iran, Corée du Nord, Russie (régime complexe depuis 2022), Belarus, Syrie, Venezuela, autres.

## 38.3 Outils de screening sanctions

**OpenSanctions** (opensanctions.org). **Gratuit**, agrège les listes principales. Standard de référence pour OSINT. API disponible.

**OFAC search engine** (sanctionssearch.ofac.treas.gov). Lookup direct OFAC.

**Sanctions Explorer** (UE). Recherche dans listes UE consolidées.

**Outils payants.**

- **WorldCheck** (Refinitiv) : standard institutionnel. ~5-50 k€/an.
- **Dow Jones Risk & Compliance** : équivalent.
- **Accuity** : transactional screening.
- **Sayari**, **Sigma Ratings**, **ComplyAdvantage** : alternatives modernes.

## 38.4 PEP — Politically Exposed Persons

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

## 38.5 Adverse media — la presse négative

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

## 38.6 Contentieux et procédures

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

## 38.7 KYC, KYB et CSDDD

**KYC** (Know Your Customer). Vigilance client en finance.

**KYB** (Know Your Business). Vigilance partenaire commercial.

**CSDDD** (Corporate Sustainability Due Diligence Directive, UE 2024). Obligation vigilance droits humains et environnement sur supply chain. Mobilise massivement l'OSINT corporate.

## 38.8 Méthodologie due diligence complète

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

## 38.9 Limites de la due diligence OSINT

- **Incomplétude** : ce qu'on ne trouve pas peut exister.
- **Faux négatifs** : absence de match sanctions ne prouve pas absence de risque.
- **Adverse media biaisé** : couverture variable selon langues / pays.
- **Temporalité** : info datée.

## 38.10 Synthèse — workflow due diligence

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
