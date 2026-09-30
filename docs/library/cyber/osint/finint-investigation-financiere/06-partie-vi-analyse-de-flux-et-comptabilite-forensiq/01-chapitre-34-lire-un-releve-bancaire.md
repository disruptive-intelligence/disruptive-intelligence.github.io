---
title: Chapitre 34 — Lire un relevé bancaire
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VI — Analyse DE flux et comptabilité forensique
  - index.md
---

## Objectif du chapitre

Maîtriser la **lecture analytique d’un relevé bancaire** — au-delà de la simple consultation. Le chapitre 9 a posé la structure du relevé ; ici, on développe les techniques d’analyse en profondeur.

## Le concept

Un relevé bancaire est une **série temporelle d’opérations**. Le lire analytiquement revient à le traiter comme un **dataset** : structurer les données, calculer des indicateurs, repérer des patterns, comparer à des références (sectorielles, historiques, comportementales).

## Les passes d’analyse (approfondissement chapitre 9)

**Passe 1 — Profilage statistique global.**

Indicateurs clés à calculer :

- Nombre total d’opérations sur la période.
- Volume crédité, volume débité, ratio.
- Solde moyen, médian, maximum, minimum.
- Nombre de contreparties uniques.
- Top 5, 10, 20 des contreparties (entrants et sortants).
- Distribution des montants : nombre d’opérations par tranche (< 1 K€, 1-10 K€, 10-50 K€, 50-100 K€, > 100 K€).
- Saisonnalité : opérations par jour de la semaine, par heure, par mois.

Outils : tableur Excel ou LibreOffice, ou pandas (Python) pour les gros volumes.

**Passe 2 — Concentration et asymétrie.**

- Concentration : si les top 5 contreparties représentent > 70 % du volume, le compte est *concentré* — atypique pour la plupart des comptes personnels.
- Asymétrie crédit/débit : un compte qui reçoit beaucoup mais peu sortant accumule la valeur ; un compte qui passe (entrant = sortant en cycle court) est un compte de **transit**.
- Cycles : entrée 100 K€, sortie 95-99 K€ dans les 48h — pattern de transit.

**Passe 3 — Vue temporelle.**

- Activité par mois : pics, creux.
- Détection de **ruptures de comportement** : avant/après un événement (changement d’activité, début ou fin d’une fraude).
- Saisonnalité cohérente avec le secteur ? (un commerce saisonnier a un profil annuel marqué).

**Passe 4 — Contreparties.**

- Identification des principales contreparties : sociétés (croisement registres), particuliers, comptes propres.
- Nouvelles contreparties (n’apparaissant pas dans l’historique antérieur).
- Contreparties géographiquement incohérentes.
- Contreparties dans des juridictions à risque (chapitre 10).

**Passe 5 — Libellés et références.**

- Mots clés vagues : « services », « avance », « régularisation », « paiement », « contractuel ».
- Libellés répétés à l’identique sur plusieurs flux.
- Libellés faisant référence à des factures (chercher les factures correspondantes).
- Absence de libellé ou libellé pauvre.

**Passe 6 — Cohérence économique.**

- Flux compatible avec l’activité ?
- Ratios sectoriels respectés ?
- Transferts au dirigeant (compte personnel) en proportion raisonnable ?

## Méthode — workflow type

Sur un relevé d’1 an, environ 3000-5000 lignes pour une PME active :

1. **Import** dans tableur ou pandas.
1. **Nettoyage** : harmonisation des libellés, parsing des montants.
1. **Catégorisation** : assigner chaque opération à une catégorie (CA encaissé, achats fournisseurs, salaires, charges fiscales, virements intra-groupe, dividendes, frais bancaires, prélèvements perso).
1. **Tableau de synthèse** : volume par catégorie, ratio, évolution.
1. **Tableau des contreparties** : top 20 en entrée, top 20 en sortie.
1. **Détection d’anomalies** : opérations sortant des patterns habituels.
1. **Annotation** : signaux faibles documentés.

## Mini-walkthrough — relevé NEXUS TRADING SAS

Année 1 (1er exercice clos), compte principal :

- 1 421 crédits = 4,2 M€.
- 1 826 débits = 4,1 M€.
- Solde moyen 87 K€, max 542 K€.
- Top 5 entrées : 73 % du volume (4 sociétés étrangères + 1 compte personnel inconnu).
- Top 5 sorties : 51 % du volume (3 sociétés du réseau + 2 comptes personnels).

Vue temporelle : 3 pics d’activité en mars, juin, octobre — chaque pic précède de quelques jours un transfert vers la Suisse. Pattern de **cycles**.

Libellés : 75 % vagues, 22 % faisant référence à des factures non identifiables, 3 % explicites mais douteux.

Cohérence : la SAS déclare une activité de négoce de matériel agricole. Aucun fournisseur de matériel agricole identifié parmi les contreparties (entrants ou sortants). Aucun client final identifié. La SAS apparaît comme un compte de **pure intermédiation**, avec activité économique réelle non démontrée.

Hypothèses : transit financier (probable), TBML (possible à probable), pure structure d’opacification (probable).

## Erreurs fréquentes

- **Lire ligne à ligne sans agrégation préalable.** L’analyste se perd.
- **Ignorer les frais bancaires** : ils racontent une histoire (volume d’opérations, opérations rejetées, descouverts).
- **Sous-estimer la temporalité** : un même montant à un mois différent peut être un signal différent.

## Limites

Le relevé seul ne suffit jamais. Il faut croiser avec : comptes annuels, libellés détaillés (parfois enrichis par réquisition), correspondance entre flux et factures (chapitre 38), réquisitions des contreparties.

## Lien avec le fil rouge

> **CLEARFLOW — Analyse système des relevés**
> 
> Nassim consolide les analyses des relevés des 4 SAS françaises. Cumulés, ces relevés couvrent ~5 600 opérations sur 18 mois, ~22 M€ de volume crédit, 16 M€ vers l’étranger. La signature globale : système de **transit multi-comptes avec cycles** intra-groupe, sortie principale vers Suisse et destinations offshore. Activité commerciale réelle douteuse. Sous réserve de coopération internationale pour les contreparties étrangères.

## Points clés à retenir

- Relevé bancaire = série temporelle à traiter comme dataset.
- 6 passes d’analyse : profil, concentration, temps, contreparties, libellés, cohérence.
- Catégoriser, agréger, comparer.
- Tout pattern doit être confronté à l’activité économique réelle.

-----
