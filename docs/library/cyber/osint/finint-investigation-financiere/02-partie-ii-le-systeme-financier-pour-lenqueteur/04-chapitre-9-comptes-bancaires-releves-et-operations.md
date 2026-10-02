---
title: Chapitre 9 — Comptes bancaires, relevés et opérations
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie II — Le système financier pour l’enquêteur
  - index.md
---

## Objectif du chapitre

Comprendre les **différents types de comptes**, la structure d’un **relevé bancaire**, et la grammaire des opérations courantes — pour savoir lire un relevé et y reconnaître l’anormal.

## Le concept

**Types de comptes (vue analyste).**

- **Compte courant / compte de paiement** — usage quotidien, encaissements, virements, dépenses. Le compte « visible » d’un particulier ou d’une entreprise.
- **Compte d’épargne** (Livret A, LDDS, livrets bancaires, etc.) — dépôts rémunérés, plafonds, fiscalité spécifique en France.
- **Compte à terme / compte de dépôt à terme** — sommes immobilisées sur une durée, rémunération supérieure.
- **Compte titres / portefeuille** — détention d’instruments financiers (actions, obligations, OPCVM, ETF).
- **Compte sur livret de société** — pour entreprises, plus rare.
- **Compte de séquestre / escrow** — fonds bloqués au profit d’un tiers (notaire, avocat).
- **Compte de paiement chez une fintech / EME** — fonctionnellement proche d’un compte courant, mais juridiquement distinct.
- **Compte de cantonnement** — pour certains professionnels (avocats, agents immobiliers, agents de change), fonds reçus pour le compte de tiers.
- **Compte client / compte tiers** — fonds détenus par un professionnel pour ses clients.

**Structure d’un relevé bancaire (lecture FININT).**

Un relevé moderne contient typiquement, par ligne d’opération :

- **Date de l’opération** (date où l’opération est passée).
- **Date de valeur** (date à laquelle l’opération est prise en compte pour le calcul d’intérêts).
- **Libellé** — texte plus ou moins riche : référence SEPA, nom du donneur ou bénéficiaire, motif éventuel, référence interne.
- **Montant** (débit ou crédit, devise).
- **Solde après opération** (parfois).
- **Référence interne** — souvent utile pour relier les opérations.

Pour un compte d’entreprise, le relevé peut être enrichi : code analytique, journal comptable, rapprochement automatique.

**Grammaire des opérations courantes.**

- **Virement émis / reçu** (SEPA, SWIFT, instantané) — la trace la plus courante.
- **Prélèvement** (SDD) — paiement récurrent avec mandat (loyers, factures).
- **Carte bancaire — débit / paiement / retrait** — paiements en ligne ou physiques, retraits espèces.
- **Dépôt / versement d’espèces** — en agence, en automate.
- **Retrait d’espèces** — au DAB ou en agence.
- **Chèque — émis / reçu / encaissé / rejeté** — en déclin en Europe, encore courant en certains secteurs.
- **Effets de commerce / LCR / BOR** — papiers commerciaux entre entreprises.
- **Frais bancaires** — nombreux, souvent peu lus mais analytiquement utiles (un fort volume de frais sur découvert peut être signal de difficulté ; un volume anormalement élevé de frais SWIFT peut signaler une activité de transit).
- **Intérêts / agios** — produits ou charges financières.
- **Achats-ventes de titres** sur compte titre.

## L’utilité opérationnelle

Le relevé est la **matière première** de l’analyse de flux. L’analyste le lit en plusieurs passes :

1. **Vue panoramique** — structure globale : combien d’opérations / mois ? combien d’entrées ? sorties ? quel est le solde moyen ? quel est le pic ?
1. **Vue temporelle** — distribution des opérations dans le temps : pics d’activité ? saisonnalité ? périodes de creux ?
1. **Vue par contreparties** — top 20 des contreparties émettrices, top 20 des bénéficiaires : qui paie qui, combien, sur quelle période ?
1. **Vue par type d’opération** — répartition virements / cartes / espèces / chèques.
1. **Vue par libellés** — détection de patterns dans les libellés (mots clés récurrents, formats répétitifs).
1. **Vue par cohérence économique** — les flux sont-ils compatibles avec l’activité déclarée (secteur, taille, géographie) ?

À chaque passe, l’analyste note les **anomalies** : montants ronds inhabituels, structuration sous des seuils, libellés vagues, contreparties géographiquement incohérentes, soldes nuls répétés (compte de transit), pics non expliqués.

## Méthode — la lecture en 6 passes

Pour un relevé d’1 an d’opérations sur un compte courant typique (1 000 à 5 000 lignes) :

**Passe 1 — Profilage** (15 min). Statistiques globales. Outils : tableur ou pandas.

```
Période : 12 mois
Lignes : 3 247
Crédits : 1 421 — 4,2 M€
Débits : 1 826 — 4,1 M€
Solde moyen : 87 K€
Solde max : 542 K€ (pic le 18/03)
Nombre de contreparties uniques : 187
Top 5 émetteurs : 73 % du volume entrant
Top 5 bénéficiaires : 51 % du volume sortant
```


**Passe 2 — Concentrations**. Les top contreparties représentent quoi ? Sont-elles cohérentes avec l’activité ?

**Passe 3 — Anomalies temporelles**. Pics, creux, ruptures (changement de comportement).

**Passe 4 — Anomalies de contreparties**. Pays inhabituels, contreparties inconnues, contreparties créées récemment.

**Passe 5 — Libellés**. Mots clés vagues (« services », « paiement », « avance », « régularisation »), libellés répétés à l’identique, libellés contradictoires.

**Passe 6 — Cohérence économique**. Recoupement avec l’activité déclarée : pour une SAS de négoce, attendre des achats matières + ventes clients ; les virements perso massifs depuis le compte société sont anormaux (ABS — chapitre 43).

## Mini-walkthrough

Un compte personnel d’un dirigeant français, secteur « consultant indépendant », revenus déclarés 80 K€/an :

- 87 % des entrées sur 6 mois proviennent de 2 sociétés étrangères (CY et AE) que l’OSINT identifie comme contrôlées par le même groupe ;
- Les libellés sont uniformément « consulting fees » ;
- Les sorties incluent : 240 K€ vers une SCI Paris (achat immobilier), 95 K€ vers un compte personnel suisse, dépôt récurrent de 8 500 € à 14 000 € en espèces (10 dépôts en 6 mois) ;
- Aucun frais professionnel apparent (pas de loyer bureau, pas de cotisations sociales pro, pas d’achat matériel).

Lecture FININT initiale : profil compatible avec **(H1)** prestation de conseil légitime mais à clientèle restreinte hors France ; **(H2)** rétrocommissions ou facturation de complaisance ; **(H3)** prête-nom pour le compte d’un tiers. Niveau de confiance : impossible à trancher sur les seules données du relevé. Sollicitations recommandées : coopération avec les CRF chypriote et émiratie pour qualifier les contreparties, OSINT sur l’activité réelle du « consultant », réquisition des libellés détaillés des dépôts cash si possible.

## Erreurs fréquentes

- **Lire un relevé ligne à ligne sans vue panoramique préalable.** L’analyste se noie dans les détails et passe à côté du schéma.
- **Ignorer les frais bancaires.** Ils racontent une histoire (volume d’opérations, opérations rejetées, découverts).
- **Ne pas faire le rapprochement avec l’activité économique réelle** — un relevé bancaire ne se lit qu’avec le contexte du compte.

## Limites

Le relevé bancaire est un point de vue **partiel** sur les flux d’une personne ou d’une entreprise. Une personne peut avoir 3 comptes dans 2 banques différentes ; une entreprise peut opérer via 5 comptes dans 4 juridictions. Une analyse complète exige la consolidation, qui est rarement possible sans réquisitions (FICOBA en France pour identifier les comptes ouverts par une personne).

## Lien avec le fil rouge

> **CLEARFLOW — Premier relevé Haddad**
> 
> Nassim obtient, via les DS, un échantillon des relevés des comptes français de Haddad. Sur 18 mois : 1 421 lignes, 4,2 M€ de crédits totaux, 87 % concentrés sur 4 contreparties étrangères (Chypre, Émirats, Turquie, Suisse). Libellés à 75 % vagues (« services », « commercial », « avance »). Ratio comptes pro / perso anormal : 60 % des dépenses du compte société sont des transferts vers des comptes perso ou des entités liées. Le relevé seul ne prouve rien. Il pose le décor.

## Points clés à retenir

- Relevé = matière première, lecture en 6 passes (profilage, concentrations, temps, contreparties, libellés, cohérence).
- Le relevé est partiel ; le FICOBA (et équivalents) permet de consolider.
- Les frais bancaires et les libellés sont des indices souvent négligés.
- Le relevé seul ne tranche pas — il oriente, en attendant le recoupement.

-----
