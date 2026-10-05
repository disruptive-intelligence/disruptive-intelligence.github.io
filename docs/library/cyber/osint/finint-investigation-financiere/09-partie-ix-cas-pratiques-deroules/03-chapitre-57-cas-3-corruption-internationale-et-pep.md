---
title: 'Chapitre 57 — Cas 3 : Corruption internationale et PEP'
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie IX — Cas pratiques déroulés
  - index.md
---

## Contexte

Une banque privée européenne, **BANQUE-PARTNER** (fictive), procède à un examen LCB-FT approfondi d’un compte client significatif. Le client, **M. KAMBOU**, est un ancien ministre d’un pays d’Afrique de l’Ouest (statut PEP confirmé). Le compte présente une activité importante depuis 18 mois : crédits totaux de 12 M€ provenant de diverses sources internationales, débits vers immobilier européen et fonds d’investissement.

La banque, en application de la vigilance renforcée PEP, mandate un cabinet de conformité pour une **due diligence approfondie**.

**Demande** : qualifier la cohérence des fonds avec le profil et l’historique professionnel du client, identifier risques de corruption et recommander des suites.

## Indices initiaux

- M. KAMBOU, ministre de l’Économie pendant 6 ans, sorti de fonctions il y a 4 ans.
- Patrimoine déclaré à l’entrée en relation : ~3,5 M€.
- Sources de revenus déclarées : conseils stratégiques pour des entreprises africaines et européennes, plus quelques participations.
- Comptes : ouverts depuis l’année qui a suivi la sortie des fonctions. Activité progressivement croissante.

## Cadrage initial

**Questions de renseignement** :

- QR1 — Origine des fonds : conseils légitimes ou rétrocommissions de fonctions antérieures ?
- QR2 — Quel est le profil PEP étendu (famille, collaborateurs étroits) ?
- QR3 — Y a-t-il des liens visibles avec des marchés publics du pays d’origine ?
- QR4 — Quelle qualification du compte (à approfondir, rupture, signalement) ?

## Collecte

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

## Analyse

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

## Hypothèses calibrées

- **H1 — Rétrocommissions différées (corruption transnationale latente)** : probable.
- **H2 — Conseil stratégique légitime, à très haute valeur ajoutée** : peu probable, vu l’absence de traçabilité de l’activité de conseil réelle et la corrélation temporelle avec les marchés.
- **H3 — Combinaison de sources légitimes et illicites** : possible.

## Limites

- Sans coopération internationale (notamment via Egmont avec la CRF du pays d’origine), la qualification définitive est *indéterminable*.
- La présomption d’innocence demeure : M. KAMBOU n’a pas été condamné.
- Les contrats de conseil peuvent être légalement formalisés, ce qui complique la qualification pénale.

## Livrable

Rapport à la banque BANQUE-PARTNER :

- Le profil et l’activité du compte sont *probable* compatibles avec un schéma de rétrocommissions de corruption transnationale antérieures.
- Recommandations :
    - **Déclaration de soupçon à la CRF nationale** (TRACFIN équivalent local) : suffisamment d’éléments pour DS.
    - **Vigilance renforcée maximale** : limitation des opérations, demandes systématiques de justificatifs.
    - **Évaluer la rupture** de la relation d’affaires : décision banque selon politique interne et avis juridique.
    - **Coopérations Egmont** : la CRF pourra solliciter la CRF du pays d’origine pour qualifier les marchés publics.

## Bilan honnête

Une enquête de due diligence approfondie ne **prouve pas** la corruption. Elle qualifie un **profil de risque** avec un niveau de confiance *probable* à élevé. La décision opérationnelle (rupture, signalement, vigilance) appartient à la banque. La qualification judiciaire éventuelle relève de la procédure pénale dans le pays d’origine ou via Convention OCDE Anti-Corruption (1997).

## Leçons FININT

- Le **statut PEP** déclenche une vigilance, pas une accusation.
- La **temporalité** (sortie de fonctions → début de l’activité de conseil → flux entrants des bénéficiaires de marchés) est centrale.
- **Pandora et leaks** sont essentiels pour les volets offshore.
- La banque, dans ce cas, est **assujetti** et a une obligation de DS si soupçon ; le cabinet conseille mais ne décide pas.

-----
