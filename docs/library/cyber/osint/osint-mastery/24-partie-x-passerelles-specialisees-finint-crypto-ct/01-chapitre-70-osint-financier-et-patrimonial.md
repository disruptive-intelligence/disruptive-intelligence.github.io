---
title: Chapitre 70 — OSINT financier et patrimonial
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - 'PARTIE X — Passerelles spécialisées : FININT, Crypto, CTI, Influence'
  - index.md
---

## 70.1 Vue maître

L'**OSINT financier** consiste à investiguer le patrimoine, les flux et la santé financière d'une personne ou entité à partir de sources ouvertes. C'est un pan majeur de l'OSINT moderne, mobilisé pour due diligence, investigation de fraude, asset recovery, journalisme économique.

Le présent chapitre fournit la **vue maître**. Pour la profondeur (UBO complexes, schémas de blanchiment, AML/CFT, asset recovery international, expertise comptable forensique), **renvoi systématique vers FININT Investigation Financière vFULL**.

## 70.2 Patrimoine visible : sources publiques

**Patrimoine immobilier.**

- **Cadastre.gouv.fr** (France) : visualisation parcelles, références.
- **Pages Jaunes / annuaires** : adresses identifiables.
- **SCI** : dirigeants et bénéficiaires partiellement accessibles.
- **Registres fonciers internationaux** (Land Registry UK, etc.).

**Patrimoine corporate.**

- Sociétés détenues (Pappers, OpenCorporates).
- Parts dans filiales (Ch.36-37).

**Patrimoine mobilier visible.**

- Véhicules de luxe (presse spécialisée, photos publiques).
- Yachts (MarineTraffic, Ch.52).
- Jets privés (ADS-B Exchange, Ch.52).
- Œuvres d'art (catalogues de ventes, ArtPrice).

## 70.3 Indicateurs de revenus déclarés

**Sources directes (limitées en OSINT).**

- Comptes annuels publiés (sociétés cotées : EDGAR, AMF).
- Rémunérations dirigeants (proxy statements US, RemCo UK).
- Déclarations PEP (HATVP en France pour élus).

**Indicateurs indirects.**

- Train de vie apparent vs estimation revenus.
- Patrimoine visible vs revenus déclarés.
- Cohérence des trajectoires (un DAF d'ETI ne possède pas un yacht 50m sans explication).

## 70.4 Détection d'incohérences

**Méthode.** Comparer patrimoine et train de vie visibles avec revenus plausibles.

**Indicateurs d'alerte.**

- Patrimoine très supérieur à revenus accumulés théoriques.
- Acquisitions massives sur court délai.
- Train de vie incompatible avec revenus déclarés.
- Structures écrans massives.

**Pour MIRAGE.** Le patrimoine Delaunay identifié (mas Provence 1.8 M€, villa Marrakech 800 k€, deux appartements parisiens, SCI) cumule ~3-4 M€. Revenus DAF TechnoVert ~180-250 k€/an sur 7 ans → accumulation difficile, surtout après imposition et charges familiales. **Cohérence faible** entre patrimoine visible et revenus déclarés → indicateur d'alerte.

## 70.5 ICIJ leaks et FININT

Les **leaks ICIJ** (Panama, Paradise, Pandora, Cyprus Confidential) sont la source publique de référence pour FININT international. Voir Ch.37.

## 70.6 Outils OSINT financier vue maître

**Gratuit.**

- Pappers, OpenCorporates.
- OpenSanctions.
- ICIJ Offshore Leaks Database.
- OCCRP Aleph.
- HATVP (PEP France).

**Payant accessible.**

- Pappers Pro.
- DueDil (UK).
- Sayari.

**Institutionnel.**

- Orbis (Bureau van Dijk).
- WorldCheck.
- Refinitiv (LSEG).
- Dow Jones Risk.

## 70.7 Renvoi FININT vFULL

Pour la profondeur opérationnelle :

- UBO complexes (nominees imbriqués, fondations, fiducies).
- Schémas de blanchiment (intégration, empilement, placement).
- AML/CFT (méthodologie, indicateurs).
- Asset recovery (méthodologie internationale).
- Comptabilité forensique.
- Analyse de transactions visibles (mention dans leaks, comptes consolidés).

**→ Cours FININT Investigation Financière vFULL.**

## 70.8 Workflow triage OSINT financier

Pour un triage rapide (ce qui est dans le périmètre du master OSINT) :

1. **Identification entité** (corporate, personne).
2. **Patrimoine corporate visible** (Pappers, OpenCorporates).
3. **Patrimoine immobilier** (cadastre, registres fonciers).
4. **ICIJ leaks** (recherche Offshore Leaks Database).
5. **Sanctions et PEP** (OpenSanctions).
6. **Indicateurs d'incohérence** (revenus vs patrimoine).
7. **Synthèse triage**.
8. **Décision escalade** : si éléments suffisants pour approfondissement, **basculer vers FININT vFULL** ou partenaire spécialisé.

## 70.9 Signaux d'alerte financiers typiques

L'analyste OSINT doit savoir reconnaître, dans les sources publiques, les **signaux d'alerte financiers** justifiant approfondissement FININT.

**Signaux corporate.**

- Capital social symbolique pour société à activité significative déclarée.
- Adresse de domiciliation partagée avec centaines d'autres entités (registered agent).
- Director ou UBO unique apparent sans cohérence avec activité.
- Activité déclarée vague (« consulting », « services », « trading ») sans précision.
- Forte croissance ou décroissance inexpliquée du capital.
- Changements fréquents de dirigeants ou commissaires aux comptes.
- Domiciliation dans juridiction à risque (paradis fiscal classé).
- Comptes annuels non publiés malgré obligation.
- Conventions réglementées avec parties liées non détaillées.

**Signaux flux.**

- Ligne comptable inhabituelle ou disproportionnée (« services consulting externes », « commissions », « honoraires »).
- Forte croissance de cette ligne sur courte période.
- Bénéficiaire des flux non identifiable publiquement.
- Pattern cyclique suspect (versements répétitifs réguliers).
- Cohérence temporelle avec création d'entités opaques.

**Signaux patrimoniaux.**

- Acquisitions massives sur courte période.
- Patrimoine très supérieur aux revenus cumulés (avec marge fiscale et charges).
- Multiplication d'entités SCI avec immobilier diversifié géographiquement.
- Présence d'actifs visibles (yacht, jet, œuvres d'art, voitures de luxe) non justifiés.
- Donations familiales suspectes sur courte période.

**Signaux comportementaux.**

- Discrétion publique anormale.
- Empreinte SOCMINT volontairement faible.
- Changements de domiciliation fiscale en série.
- Investissements crypto significatifs sans expertise sectorielle documentée.

**Indicateurs FATF 2026.** Le **GAFI/FATF** maintient une liste évolutive d'indicateurs de risque blanchiment. Catégories : **A** (opacité corporate), **B** (transactions inhabituelles), **C** (crypto et nouvelles technologies), **D** (comportements suspects), **E** (juridictions à risque).

## 70.10 Investigation patrimoniale méthodologique

**Inventaire des sources patrimoniales (France).**

| Type de patrimoine | Source OSINT |
|---|---|
| Immobilier identifié | Cadastre.gouv.fr (visualisation, pas propriétaire direct) |
| SCI propriétaires | Pappers (dirigeants + UBO de la SCI révèlent) |
| Sociétés détenues | Pappers + OpenCorporates |
| Comptes-titres / OPCVM | AMF déclarations seuils + presse |
| Œuvres d'art | Catalogues ventes (Christie's, Sotheby's archives publiques) |
| Yachts | MarineTraffic + Equasis (propriété déclarée pavillon) |
| Jets privés | ADS-B Exchange + registres FAA/DGAC |
| Voitures de luxe | Très limité OSINT (photos publiques, presse) |
| Crypto-actifs | Pivots Etherscan, Walletexplorer (limité, voir crypto cours) |
| Actifs déclarés HATVP (PEP) | declaration.hatvp.fr |

**Méthodologie estimation cohérence revenus / patrimoine.**

1. **Estimation revenus accumulés.** Standards sectoriels par poste et secteur (baromètres APEC, cabinet RH). Pour un DAF d'ETI : 180-250 k€ brut. Pour 7 ans : 1.3-1.8 M€ brut.
2. **Soustraction fiscale.** Tranche marginale ~45 % au-delà de 175 k€. Estimation 35-40 % moyenne. Revenu net : ~0.8-1.2 M€.
3. **Soustraction charges courantes.** Train de vie cohérent avec poste (60-70 k€/an pour cadre supérieur). Sur 7 ans : 420-490 k€.
4. **Reste disponible épargne.** ~400-700 k€ sur 7 ans pour un DAF français standard.
5. **Comparaison patrimoine visible.** Si > 1 M€, incohérence à investiguer.

**Hypothèses alternatives à tester systématiquement.**

- Héritage familial substantiel (vérifiable presse, généalogie publique).
- Mariage avec personne fortunée (LinkedIn conjoint, presse).
- Gains crypto exceptionnels (rare mais possible).
- Activité parallèle déclarée (auteur, formateur, etc.).
- Stock-options exercées (si société cotée — déclarations AMF).

## 70.11 Investigation du dispositif offshore

Le **dispositif offshore typique** détourne via trois mécanismes principaux observables en OSINT.

**Mécanisme 1 — Double fausse facturation.** Société française paye sa propre filiale offshore pour « services de conseil » non rendus. La filiale offshore reçoit les fonds, déductibles fiscalement. L'UBO bénéficie via dividendes ou structures suivantes.

*Indicateurs OSINT.* Ligne comptable « services consulting » disproportionnée. Filiale offshore avec activité non démontrable. Cohérence temporelle entre création offshore et augmentation de la ligne.

**Mécanisme 2 — Structures empilées.** Société française → société intermédiaire (UE : Malte, Luxembourg) → société finale (BVI, Cayman). L'empilement masque l'UBO final.

*Indicateurs OSINT.* Plusieurs sociétés liées par dirigeants partagés ou registered agent commun. Nominees identifiables. Documents leaks (ICIJ) révélant les couches.

**Mécanisme 3 — Trusts et fondations.** Trust dans juridiction de droit anglo-saxon ou fondation familiale. L'UBO formel disparaît au profit du trust / fondation.

*Indicateurs OSINT.* Mention de trust dans documents. Settlor / trustee / beneficiary identifiables. Leaks ICIJ Pandora notamment riches en trusts.

## 70.12 Outils OSINT financier 2026 spécialisés

**Gratuit avancé.** OpenSanctions (sanctions, PEP, adverse media), OCCRP Aleph (documents leakés), ICIJ Offshore Leaks Database, Pappers freemium France, Companies House UK gratuit complet, OpenCorporates freemium cross-juridictions.

**Freemium ou bas coût.** DueDil (UK), Sayari (OSINT corporate moderne), Pappers Pro abonnement France.

**Institutionnel haut coût.** Bureau van Dijk Orbis (Moody's, 400M+ sociétés mondial), WorldCheck (Refinitiv/LSEG, screening institutionnel), Dow Jones Risk & Compliance, Refinitiv Eikon (marché financier intégré), Bloomberg Terminal (référence).

## 70.13 Limites OSINT financier

**Ce que l'OSINT financier seul ne fait pas.**

- Accès aux comptes bancaires individuels.
- Identification des bénéficiaires économiques cachés derrière fiducies opaques.
- Reconstruction de flux entre comptes sans réquisitions.
- Qualification fiscale ou comptable des opérations.
- Évaluation forensique des écritures.

**Pour ces dimensions.** Réquisitions judiciaires (PNF, juge d'instruction), TRACFIN (signalement de soupçons), expertise comptable judiciaire, coopération internationale (entraide pénale, FATF, Egmont Group).

L'analyste OSINT identifie les **faisceaux d'indices** justifiant ces démarches. Il ne s'y substitue pas.

> **MIRAGE — Épisode 13 : Signaux financiers ouverts**
>
> Le triage OSINT financier sur Delaunay identifie :
> - Patrimoine immobilier visible : ~3-4 M€ (SCI La Provence Familiale + villa Marrakech + 2 appartements parisiens SCI nominee).
> - Patrimoine corporate offshore : Delta Consulting (Malte) + Verde Holdings (Chypre).
> - Revenus DAF TechnoVert : ~180-250 k€/an, cumul 7 ans = 1.3-1.8 M€ brut.
> - Incohérence : patrimoine total supérieur à revenus accumulés bruts, alors qu'il faut soustraire imposition + charges + train de vie.
> - Indicateurs ICIJ Cyprus Confidential : confirmation flux TechnoVert → Delta → Verde (B2).
> - Aucune sanction / PEP active sur les entités identifiées.
>
> **Synthèse triage.** Faisceau d'indices cohérents avec hypothèse H1 (détournement vers structures offshore). **Recommandation : escalade vers FININT vFULL** pour profondeur (schéma de blanchiment précis, asset recovery potentiel, analyse comptable forensique des comptes consolidés TechnoVert pour identification écritures suspectes).
>
> Cette enquête MIRAGE produit un rapport OSINT avec ce niveau de triage. Le PNF saisi pourra mandater expertise comptable judiciaire pour profondeur.

-----
