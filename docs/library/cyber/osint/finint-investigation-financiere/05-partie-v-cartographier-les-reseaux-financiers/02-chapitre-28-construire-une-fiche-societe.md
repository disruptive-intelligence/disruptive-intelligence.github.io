---
title: Chapitre 28 — Construire une fiche société
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie V — Cartographier les réseaux financiers
  - index.md
---

## Objectif du chapitre

Maîtriser la **fiche société FININT** — pendant de la fiche personne, structurée pour les entités juridiques. Modèle complet en annexe D.

## Le concept

La fiche société consolide, sur une entité, tout ce que l’analyste sait : identification, juridiction, gouvernance, capital et UBO, activité, comptes, flux, contentieux, liens avec d’autres entités, hypothèses calibrées.

## Structure type d’une fiche société

1. **En-tête** : référence, date, version, classification, auteur.
1. **Identification** : dénomination exacte, identifiant officiel, forme juridique, juridiction, capital, date de création.
1. **Adresse(s)** : siège, établissements secondaires, adresse réelle si différente du siège déclaré.
1. **Activité déclarée** : NAF/SIC/code sectoriel, libellé, sous-activités.
1. **Gouvernance** : dirigeants actuels, mandataires, historique.
1. **Actionnariat / Capital** : associés, pourcentages, classes d’actions.
1. **UBO** : déclaré (registre UBO) et identifié (analyse), avec niveaux de confiance.
1. **Substance économique** : personnel, locaux, site web, clientèle, fournisseurs, présence opérationnelle réelle.
1. **Comptes** : derniers comptes annuels publiés, principaux indicateurs, ratios, observations.
1. **Flux observables** : profil bancaire (si DS ou OSINT), contreparties principales.
1. **Contentieux** : procédures collectives, contentieux fiscaux, sanctions, adverse media.
1. **Liens** : entités liées (capital, dirigeants partagés, adresse partagée), trust ou fondation au sommet.
1. **Crypto si pertinent** : adresses, échanges utilisés — renvoi vers OSINT Crypto.
1. **Hypothèses calibrées** : qualification de la nature de l’entité (opérationnelle légitime, holding, intermédiaire, écran probable, etc.).
1. **Sources et lacunes**.

## L’utilité opérationnelle

Comme pour la fiche personne, la fiche société est **réutilisable, sourcée, calibrée**. Elle permet de structurer un livrable complexe (note FININT couvrant plusieurs entités) en éléments atomiques cohérents.

## Méthode — bonnes pratiques

- **Préciser la juridiction** dès l’identification (pas de confusion avec sociétés homonymes).
- **Annoter l’identifiant officiel** systématiquement.
- **Mettre la substance économique en évidence** : c’est souvent la clé.
- **Présenter les comptes en ratios** plus qu’en chiffres bruts, pour comparaison.
- **Documenter les liens** avec une référence à la fiche correspondante.

## Mini-walkthrough — fiche NEXUS TRADING SAS (extrait)

```
FICHE SOCIÉTÉ — NEXUS TRADING SAS
Référence : CLEARFLOW/SOC/003 | v1.2 | 14/03 | TLP:AMBER

IDENTIFICATION (quasi-certain)
- Forme : SAS
- SIREN : 8XX XXX XXX
- Juridiction : France
- Capital : 10 000 €
- Date de création : 18/01/2023

ADRESSE(S)
- Siège : 12 rue Y, Paris 9e (cabinet de domiciliation, 47 entités à la même adresse)

ACTIVITÉ DÉCLARÉE
- NAF 4690Z : commerce de gros non spécialisé
- Activité opérationnelle visible : non identifiée (pas de site web, pas de catalogue, pas de référence client publique)

GOUVERNANCE
- Président : Monsieur X (depuis création) — multi-mandats, profil prête-nom probable (voir fiche personne)
- Aucun DG, aucun directeur, aucun salarié déclaré (URSSAF non accessible directement)

ACTIONNARIAT / CAPITAL
- Associé unique : NEXUS HOLDINGS LTD (Chypre)

UBO
- Déclaré au RBE : Monsieur X (par défaut, en tant que dirigeant)
- Identifié (probable) : Karim Élie Haddad, via chaîne CY → trust OMEGA → settlor

SUBSTANCE ÉCONOMIQUE
- Personnel : aucun salarié visible
- Locaux : domiciliation seule
- Site web : aucun
- Clientèle visible : aucune
- Fournisseurs visibles : aucune trace publique
→ Substance économique très faible. Écran probable.

COMPTES (1er exercice clos)
- CA : 12,4 M€
- Marge brute : 4 %
- Charges de personnel : 32 K€
- Résultat d'exploitation : 80 K€
- Trésorerie en fin d'exercice : 35 K€
→ Profil compatible avec activité de pure intermédiation OU société de transit.

FLUX OBSERVABLES (via DS)
- Entrées : 87 % depuis Émirats (sociétés liées au réseau Haddad) et Chypre
- Sorties : virements vers 4 sociétés du réseau + 22 % vers comptes personnels (M. X et liés)
→ Profil incompatible avec activité commerciale réelle de négoce.

CONTENTIEUX
- Aucune procédure collective.
- Aucun contentieux fiscal public.

LIENS
- Capital : 100 % NEXUS HOLDINGS LTD (CY)
- Dirigeants partagés : M. X = dirigeant de 7 autres SAS (cluster).
- Adresse partagée : 46 autres entités au même cabinet.
- Trust de contrôle : OMEGA HOLDINGS TRUST (CY).

HYPOTHÈSES CALIBRÉES
- Société écran à finalité de transit : probable.
- Implication dans schéma de blanchiment ou TBML : possible à probable (à confirmer par analyse de flux globale).
- UBO réel = Karim Haddad : probable.

LACUNES
- Substance opérationnelle réelle : non vérifiée par visite physique.
- Comptes détaillés (relevés bancaires) : accès en CRF, non encore mobilisé.

SOURCES
- Pappers, INPI, RBE
- Comptes annuels Infogreffe
- DS bancaires (interne CRF)
- Cartographie réseau (chapitre 31)
```


## Erreurs fréquentes

- **Confondre dénomination commerciale et dénomination sociale.** Toujours utiliser la dénomination officielle.
- **Ne pas mentionner les lacunes sur la substance économique.** Sans visite physique ou témoignage, la substance reste *probable* à qualifier.
- **Lire les comptes sans contexte sectoriel.** Une faible marge en intermédiation peut être normale.

## Limites

Beaucoup d’éléments de la fiche société exigent des sources fermées (comptes bancaires détaillés, contrats commerciaux, audits). En OSINT pur, la fiche est **partielle** et l’indique explicitement.

## Lien avec le fil rouge

> **CLEARFLOW — 14 fiches société**
> 
> Nassim produit une fiche pour chacune des 14 entités du réseau Haddad. Cumulées, ces fiches forment le socle de la note de transmission. Elles permettent de répondre à la question « quelle est la nature de chaque entité dans le réseau ? » avec calibration de la confiance pour chaque qualification.

## Points clés à retenir

- Fiche société : pendant structurel de la fiche personne, pour les entités.
- 15 sections type ; modèle complet en annexe D.
- Substance économique = section clé.
- Ratios > chiffres bruts pour la lecture rapide.

-----
