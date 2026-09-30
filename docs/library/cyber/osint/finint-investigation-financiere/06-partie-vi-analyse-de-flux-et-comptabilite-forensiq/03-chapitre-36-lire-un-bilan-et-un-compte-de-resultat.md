---
title: Chapitre 36 — Lire un bilan et un compte de résultat
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VI — Analyse DE flux et comptabilité forensique
  - index.md
---

## Objectif du chapitre

Maîtriser la **lecture analytique** des documents comptables clés — bilan, compte de résultat, annexe — pour détecter cohérence et incohérence dans le profil économique d’une entreprise.

## Le concept

Le **bilan** est une photo à une date : actifs (ce que l’entreprise possède) = passifs (ce qu’elle doit, y compris ses fonds propres).

Le **compte de résultat** est un flux sur une période : produits (revenus) − charges (coûts) = résultat.

L’**annexe** explicite, contextualise, détaille.

## Lecture du bilan

**Actif** :

- **Immobilisations** : incorporelles (fonds de commerce, brevets), corporelles (terrains, bâtiments, matériel), financières (participations, prêts).
- **Actif circulant** : stocks, créances clients, autres créances, trésorerie.

**Passif** :

- **Capitaux propres** : capital social, réserves, report à nouveau, résultat de l’exercice.
- **Provisions pour risques et charges**.
- **Dettes** : emprunts bancaires, dettes fournisseurs, dettes fiscales et sociales, dettes diverses.

Indicateurs clés :

- **Ratio d’endettement** = dettes / fonds propres. Un ratio très élevé peut signaler une fragilité ; très faible peut signaler une accumulation atypique.
- **Liquidité** = actif circulant / dettes à court terme.
- **Capacité d’autofinancement** : produit la capacité de l’entreprise à financer ses investissements et son remboursement de dette.

## Lecture du compte de résultat

**Produits** :

- Chiffre d’affaires (ventes de marchandises, prestations de services).
- Production stockée et immobilisée.
- Subventions d’exploitation.
- Produits financiers, produits exceptionnels.

**Charges** :

- Achats consommés (matières premières, marchandises).
- Services extérieurs (sous-traitance, locations, honoraires, transports, etc.).
- Impôts et taxes.
- Charges de personnel (salaires, charges sociales).
- Dotations aux amortissements et provisions.
- Charges financières (intérêts), charges exceptionnelles.

**Soldes intermédiaires de gestion** :

- **Marge commerciale** = ventes − coût d’achat (pour les négoces).
- **Valeur ajoutée** = production de l’exercice − consommations en provenance des tiers.
- **EBE / Excédent Brut d’Exploitation** = VA − charges de personnel − impôts et taxes.
- **Résultat d’exploitation** = EBE − dotations.
- **Résultat courant avant impôts** = résultat d’exploitation + résultat financier.
- **Résultat net**.

## L’utilité opérationnelle FININT

Les comptes annuels permettent à l’analyste :

- **Apprécier la cohérence sectorielle** : la marge, la productivité, l’intensité capitalistique sont-elles vraisemblables ?
- **Détecter les anomalies** : postes anormalement gonflés, charges récurrentes douteuses, créances clients fictives, stocks invraisemblables.
- **Évaluer la substance économique** : présence ou absence de moyens humains et matériels.
- **Comprendre la stratégie financière** : endettement, distribution de dividendes, conventions intragroupe.

## Méthode — lecture rapide

1. **Vue d’ensemble** : taille (CA, total bilan), forme juridique, exercice, secteur.
1. **Ratios sectoriels** : marge commerciale, marge d’exploitation, productivité (CA/effectif), intensité capitalistique (immo/CA).
1. **Évolution** : sur 3 ans si disponibles — croissance, rupture, stabilité.
1. **Postes anormaux** : > 10 % de l’actif ou du résultat sans explication évidente.
1. **Annexe** : engagements hors bilan, conventions réglementées, événements postérieurs.

## Mini-walkthrough — NEXUS TRADING SAS suite

Comptes 1er exercice :

- CA 12,4 M€, achats consommés 11,9 M€, marge commerciale 0,5 M€ (4 %).
- Charges de personnel 32 K€ (1 dirigeant, pas de salariés).
- Services extérieurs : 195 K€ (dont 140 K€ « conseil » à NEXUS HOLDINGS LTD CY).
- EBE : 273 K€.
- Résultat d’exploitation : 80 K€ (après dotations).
- Résultat financier : -8 K€ (frais bancaires SWIFT importants).
- Résultat net : 60 K€.

Bilan :

- Actif immobilisé : 12 K€ (équipement minimum).
- Actif circulant : 350 K€ (créances clients 280 K€, trésorerie 35 K€, autres 35 K€).
- Total actif : 362 K€.
- Capitaux propres : 70 K€ (capital 10 K€ + résultat).
- Dettes fournisseurs : 215 K€.
- Dettes fiscales et sociales : 25 K€.
- Comptes courants associés (NEXUS HOLDINGS CY) : 52 K€.

Lecture FININT : profil typique d’une **société d’intermédiation à très faible substance**. Charges de « conseil » à la holding chypriote représentent 70 % des services extérieurs — *probable* canal d’évasion de bénéfices vers la juridiction chypriote (à juridiction CRS, mais le levier de taxation peut être différent). Marge brute de 4 % cohérente avec intermédiation pure, ne tranche pas en soi. Le faible niveau d’immobilisations (12 K€) et l’absence de salariés signalent une coquille sans substance économique réelle propre.

## Erreurs fréquentes

- **Lire les chiffres absolus** sans comparaison sectorielle ou ratiométrique.
- **Ignorer l’annexe** : conventions réglementées intragroupe, engagements, événements postérieurs y figurent.
- **Surinterpréter un seul exercice** : la cohérence se voit sur la trajectoire (3 ans+).

## Limites

La comptabilité est **construite par l’entreprise** ; sans CAC, le contrôle externe est limité. Les comptes peuvent être falsifiés. Le forensique poussé exige un expert-comptable de formation forensique (chapitre 37).

## Lien avec le fil rouge

> **CLEARFLOW — Analyse des 2 SAS publiantes**
> 
> Sur les 2 SAS françaises publiant des comptes, Nassim repère : pattern récurrent de charges de conseil à des entités liées (15-25 % du résultat brut diverté vers Chypre par exercice), faible substance économique propre, profils de marge cohérents avec intermédiation mais non démontratifs d’une activité commerciale réelle. Cumulé avec l’analyse de flux, l’hypothèse de **structures de transit avec évasion de bénéfices** est *probable* à *quasi-certaine*.

## Points clés à retenir

- Bilan = photo ; compte de résultat = flux ; annexe = explication.
- Indicateurs : marge, EBE, résultat, ratios.
- Cohérence sectorielle et évolution sur 3 ans : essentiels.
- L’absence de substance économique (faible immo, pas de salariés) est un signal fort.

-----
