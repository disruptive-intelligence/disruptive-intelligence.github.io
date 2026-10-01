---
title: Chapitre 10 — Offshore, secret bancaire et juridictions opaques
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie II — Le système financier pour l’enquêteur
  - index.md
---

## Objectif du chapitre

Comprendre ce qu’est l’**offshore**, comment fonctionne le **secret bancaire**, quelles sont les **juridictions opaques** clés, et comment l’analyste FININT compose avec ces obstacles structurels.

## Le concept

**Offshore.** Un terme imprécis qui désigne, dans le langage courant, les juridictions à fiscalité réduite et à régulation faible utilisées pour héberger des structures (sociétés, trusts, fondations) ou des comptes bancaires. Les analystes professionnels préfèrent le terme **« juridictions à risque »** ou **« juridictions à transparence limitée »** car il est plus précis et moins polémique.

**Secret bancaire.** Obligation légale faite aux banques de ne pas révéler à des tiers les informations sur leurs clients. Tous les pays ont une forme de secret bancaire, mais certaines juridictions l’ont historiquement renforcé au point d’en faire un argument commercial (Suisse, Liechtenstein, Luxembourg, Singapour, Hong Kong). Sous la pression internationale (GAFI, EAR/CRS, FATCA), le secret bancaire a perdu une grande partie de sa portée vis-à-vis des autorités fiscales étrangères, mais il reste opposable aux particuliers et à de nombreux acteurs privés.

**EAR/CRS** (Échange Automatique de Renseignements / Common Reporting Standard, OCDE). Mécanisme par lequel les juridictions adhérentes échangent automatiquement les informations sur les comptes bancaires détenus par des non-résidents. Plus de 100 juridictions adhérentes en 2025. La Suisse, le Liechtenstein, Singapour, Hong Kong, le Luxembourg, les BVI, les Cayman, sont parties au CRS. Les **non-adhérents** notables incluent les États-Unis (qui ont leur propre système, FATCA, asymétrique). En CRF, les données EAR/CRS reçues et envoyées sont une source primordiale.

**FATCA** (Foreign Account Tax Compliance Act, US). Obligation faite aux institutions financières étrangères de déclarer aux US les comptes détenus par des contribuables américains. Asymétrique (les US ne livrent pas l’équivalent en sortie).

**Listes GAFI.**

- **Liste noire** (« High-Risk Jurisdictions subject to a Call for Action »). Juridictions présentant des défaillances stratégiques en matière de LCB-FT. La liste évolue ; un analyste consulte le site officiel du GAFI au moment de l’analyse.
- **Liste grise** (« Jurisdictions under Increased Monitoring »). Juridictions sous surveillance renforcée mais coopérantes. La liste évolue plusieurs fois par an. Pour une donnée actuelle, consulter le site officiel du GAFI (fatf-gafi.org).

**Listes UE.** L’UE publie sa propre liste de juridictions tierces non coopératives à des fins fiscales. Liste mise à jour régulièrement, à consulter sur EUR-Lex et le site du Conseil.

## L’utilité opérationnelle

Pour l’analyste, ces concepts servent à :

- **Qualifier le risque** d’un flux sortant ou entrant (juridiction du compte / pays de résidence du titulaire / activité du compte).
- **Calibrer la coopération** attendue (un EAR/CRS facilite ; un pays sur liste grise complique ; un pays sur liste noire ferme presque toutes les portes).
- **Anticiper les délais** de toute coopération internationale.
- **Identifier les secteurs vulnérables** (les juridictions à secret bancaire fort sont souvent des destinations finales de blanchiment).

## Méthode — qualifier rapidement une juridiction

Pour toute juridiction inhabituelle apparaissant dans un dossier, l’analyste répond rapidement à :

1. **Statut GAFI** — pays sur liste noire, grise, ou hors liste ?
1. **Statut UE** — pays sur la liste UE des juridictions non coopératives ?
1. **Adhésion EAR/CRS** — oui / non ?
1. **Coopération via Egmont** — la CRF locale est-elle membre d’Egmont ? Active ?
1. **Type de structures fréquentes** — sociétés ? trusts ? fondations ? IBC (International Business Company) ? exemptes de fiscalité ? exemptes de comptes annuels publiés ?
1. **Registre des bénéficiaires effectifs** — existe-t-il ? est-il accessible ?

Outils gratuits : site GAFI, base UE, CRS country status (OCDE), Tax Justice Network (Financial Secrecy Index — académique, point de référence).

## Mini-walkthrough — quelques juridictions emblématiques

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

## Erreurs fréquentes

- **Considérer toute juridiction non européenne comme « offshore ».** La nuance est essentielle.
- **Croire que CRS résout tout.** CRS échange des données fiscales entre administrations. Il ne les rend pas accessibles aux particuliers ni à toute autorité.
- **Sous-estimer Delaware / Nevada / Wyoming.** Une part significative des structures à risque dans les dossiers transatlantiques transitent par ces États US.
- **Ignorer le free zone factor.** Les free zones (Jebel Ali, DIFC, ADGM, etc.) ont des régimes fiscaux et réglementaires propres — distincts de la juridiction « parent ».

## Limites

Les listes GAFI et UE évoluent. La liste précise à un instant donné doit être vérifiée à la source (sites officiels). Une juridiction sortie de la liste grise reste un facteur de risque pertinent dans une analyse — la sortie ne vaut pas absolution.

## Lien avec le fil rouge

> **CLEARFLOW — Cartographie offshore**
> 
> Le dossier Haddad implique au moins 5 juridictions non-françaises : Chypre (UE, structurelle), Émirats (commerce + free zone), Bénin (intermédiaire), Suisse (banque privée), Liban (origine, suspicion d’infraction prédécesseur). Nassim qualifie chaque juridiction (statut GAFI/UE, EAR/CRS, Egmont) et anticipe les délais de coopération. Dès le cadrage, il prévoit que les éléments chypriotes seront accessibles en 2 à 4 semaines via Egmont, les émiratis en 4 à 8 semaines, les libanais à très long terme et avec un haut degré d’incertitude.

## Points clés à retenir

- « Offshore » est imprécis ; préférer « juridiction à risque » et qualifier précisément.
- EAR/CRS, GAFI, listes UE structurent la qualification.
- Le secret bancaire moderne s’est érodé vis-à-vis des fiscs ; il reste fort vis-à-vis des particuliers et de nombreuses procédures civiles.
- Delaware / Nevada / Wyoming sont des points d’attention transatlantiques sous-estimés.

-----
