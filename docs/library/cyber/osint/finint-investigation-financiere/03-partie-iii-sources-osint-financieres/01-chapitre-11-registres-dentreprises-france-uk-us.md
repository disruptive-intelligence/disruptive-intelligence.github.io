---
title: 'Chapitre 11 — Registres d’entreprises : France, UK, US'
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie III — Sources OSINT financières
  - index.md
---

## Objectif du chapitre

Maîtriser les **trois principaux registres** que tout analyste FININT consulte régulièrement : France (Infogreffe / INPI), Royaume-Uni (Companies House), États-Unis (registres fédéraux et étatiques, principalement Delaware, et SEC EDGAR pour les sociétés cotées).

## Le concept

Un **registre du commerce et des sociétés** est la base officielle qui recense les entités juridiques d’un pays, leurs caractéristiques (forme, capital, dirigeants, siège), et publie certains actes (statuts, modifications, comptes annuels selon les seuils). C’est la source de premier niveau pour identifier une entité et pour ouvrir une enquête.

Tous les registres ne sont pas équivalents en richesse, en accessibilité et en gratuité. Trois pôles dominent les enquêtes occidentales modernes.

## France — INPI / Infogreffe / RCS

Architecture actuelle (2025) :

- **INPI (Registre national des entreprises — RNE)** : depuis 2023, l’INPI centralise le RNE, qui regroupe les informations historiquement réparties entre RCS (commerçants) et autres registres (artisans, agricoles, libéraux). Accès gratuit et public à beaucoup de données via [data.inpi.fr](https://data.inpi.fr/) et le portail RNE.
- **Infogreffe** : portail des greffes de tribunaux de commerce. Accès payant pour certains actes, gratuit pour la fiche identité. Toujours utilisé en pratique pour les **actes** (statuts, comptes annuels, K-bis officiel).
- **Pappers** : agrégateur tiers gratuit, très ergonomique, qui republie une grande partie des données ouvertes (siret, dirigeants, comptes annuels jusqu’aux seuils, liens entre sociétés). Devenu un réflexe d’analyste.
- **Société.com, Verif.com, Manageo, Score3** : agrégateurs concurrents avec degrés de gratuité variables.
- **BODACC** (Bulletin officiel des annonces civiles et commerciales) : publications officielles (créations, radiations, procédures collectives). Accès gratuit en ligne.

**Ce que l’analyste obtient gratuitement :**

- Identification : SIREN/SIRET, dénomination, forme juridique, capital social, date de création, NAF/APE.
- Adresse du siège, et historique des sièges.
- Dirigeants : président, gérant, DG, directeurs, administrateurs (avec dates de nomination et de fin).
- Liste des établissements secondaires.
- Procédures collectives : sauvegarde, redressement, liquidation.
- Modifications du registre (changements de dénomination, de capital, de dirigeants, transferts de siège).
- **Comptes annuels** publiés (sociétés au-delà des seuils, dans la limite du droit à confidentialité demandé par certaines petites sociétés depuis 2014).

**Pour aller plus loin (réquisition / accès professionnel) :** liste des associés (rarement publique), informations bancaires.

## Royaume-Uni — Companies House

[Companies House](https://www.gov.uk/government/organisations/companies-house) — registre officiel UK. C’est l’un des registres **les plus ouverts au monde**. Accès gratuit et complet à :

- Identification de la société (Company Number, denomination, forme, statut).
- Officers (directors, secretaries) — actuels et historiques, avec dates et adresses.
- **Persons with Significant Control (PSC)** — depuis 2016, le UK rend public le registre des personnes exerçant un contrôle significatif (équivalent UBO). Seuils : 25 % de capital ou de droits de vote, ou contrôle effectif. Accessible en ligne, gratuit, par société.
- Comptes annuels (filings) publiés pour la quasi-totalité des sociétés actives.
- Confirmations annuelles (Annual Confirmation Statement).
- Mortgages and charges (sûretés inscrites).

Cas particuliers : LLP (Limited Liability Partnership), Scottish Limited Partnership (SLP — historiquement utilisées pour le blanchiment, soumises au PSC depuis 2017).

**Limites du PSC** : déclaratif. Les fraudeurs déclarent parfois faux. Les sanctions pour fausse déclaration existent mais sont peu appliquées en pratique pour les petites entités. Reste, pour l’analyste FININT, l’une des sources les plus utiles au monde.

## États-Unis — Delaware, SEC EDGAR, registres étatiques

Les US n’ont pas de registre fédéral des sociétés. Chaque État a son propre registre. Les principaux :

- **Delaware Division of Corporations** — siège juridique d’environ 60 % des sociétés cotées américaines et de la majorité des LLC US. La consultation publique est très limitée : nom, statut, type, et c’est à peu près tout. Pas de dirigeants publics. Pas d’UBO public (en attente de la mise en œuvre du **Corporate Transparency Act** — voir infra).
- **California Secretary of State, New York Department of State, Texas, Florida, Wyoming, Nevada** — chacun a son portail.
- **OpenCorporates** — agrégateur qui aspire les registres étatiques et offre une recherche unifiée. Très utile pour l’analyste FININT.

**SEC EDGAR** : pour les **sociétés cotées** ou émettrices de titres aux US, la SEC (Securities and Exchange Commission) publie via [EDGAR](https://www.sec.gov/edgar) les déclarations détaillées (10-K, 10-Q, 8-K, S-1, proxy statements, etc.). Source d’or pour les grandes entreprises et leurs filiales.

**Corporate Transparency Act (CTA)** : loi US de 2021 ayant obligé les LLC et corporations à déclarer leurs UBO à FinCEN. Trajectoire très instable en 2024-2025 (contestations judiciaires, décisions successives). **Depuis l’interim final rule FinCEN de mars 2025**, les sociétés domestiques américaines (« domestic reporting companies ») **ne sont plus tenues** de déclarer leurs bénéficiaires effectifs à FinCEN ; l’obligation subsiste principalement pour **certaines entités étrangères enregistrées pour faire des affaires aux États-Unis**. La situation reste sujette à évolution (textes, décisions, contentieux) — un analyste consulte la mise à jour la plus récente sur le site FinCEN avant toute conclusion.

**FinCEN files** : le leak FinCEN 2020 (BuzzFeed/ICIJ) a révélé que les SAR américains contenaient des éléments sur la criminalité financière mondiale. Pas une source courante mais à connaître (Chapitre 18).

## L’utilité opérationnelle

Pour la majorité des dossiers FININT impliquant des entités françaises, britanniques ou américaines (cotées), ces trois registres couvrent l’essentiel du travail d’identification et de cartographie de premier niveau. La gratuité française et britannique permet un travail systématique sans budget. La gratuité partielle américaine est compensée par les agrégateurs (OpenCorporates) et SEC EDGAR pour les cotées.

## Méthode — workflow d’identification

1. **France** : Pappers (vue rapide) + INPI/RNE (validation officielle) + Infogreffe (acte officiel si besoin) + BODACC (procédures).
1. **UK** : Companies House (everything) + recherche par directeur/PSC pour identifier les autres sociétés liées.
1. **US** : OpenCorporates (vue agrégée) + registre étatique pertinent (validation) + SEC EDGAR si coté + FinCEN si CTA en vigueur.

Toujours **archiver** les pages consultées (capture d’écran horodatée, hash si possible — chapitre 53).

## Mini-walkthrough

Cible : *« NEXUS TRADING SAS, suspectée d’être une société écran française liée à un réseau franco-libanais. »*

- Pappers : SIREN, dénomination, capital 10 000 €, créée il y a 14 mois, dirigeant unique « Monsieur X », adresse à un cabinet de domiciliation, NAF 4690Z (commerce de gros non spécialisé). Comptes non publiés (1er exercice non clos).
- INPI : confirme + accès aux statuts initiaux.
- BODACC : aucune procédure.
- Recherche par dirigeant : Monsieur X est gérant de 7 autres SAS, toutes domiciliées à la même adresse, toutes créées entre 2023 et 2024, toutes en commerce de gros. **Pattern clair de gestionnaire multi-sociétés**.

Conclusion : à ce stade, NEXUS est **possible-à-probable** une société de façade ou un véhicule à usage spécifique. Le statut de « société écran » exige des éléments complémentaires (chapitre 26).

## Erreurs fréquentes

- **Se fier uniquement à Pappers** sans aller voir les actes officiels (Pappers est utile mais peut être en retard sur certaines mises à jour).
- **Ignorer le BODACC** (les procédures collectives sont parfois la clé d’un dossier).
- **Oublier les agrégateurs internationaux** (OpenCorporates) quand l’enquête sort de France.
- **Ne pas archiver** : un registre peut être modifié ou une fiche supprimée. La capture horodatée fait foi.

## Limites

Les registres sont **déclaratifs**. Les fraudeurs peuvent fausser les déclarations. Les modifications sont parfois en retard. L’UBO déclaré peut être un prête-nom. Croiser systématiquement avec d’autres sources.

## Lien avec le fil rouge

> **CLEARFLOW — Cartographie initiale via registres**
> 
> Sur les 14 sociétés présumées liées à Haddad, Nassim identifie 4 SAS françaises via Pappers/INPI, 2 Limited UK via Companies House (avec PSC pointant deux personnes physiques distinctes — possible alignement de prête-noms), et 1 LLC Delaware via OpenCorporates (pas d’UBO accessible — limite documentée). Le travail registre prend environ 6 heures pour cette première vague et produit un premier graphe de liens (chapitre 31).

## Points clés à retenir

- France : INPI/RNE + Pappers + Infogreffe + BODACC. Largement gratuit.
- UK : Companies House. Gratuit, riche, avec PSC.
- US : OpenCorporates + registres étatiques + SEC EDGAR. CTA à suivre.
- Toujours archiver. Toujours croiser.

-----
