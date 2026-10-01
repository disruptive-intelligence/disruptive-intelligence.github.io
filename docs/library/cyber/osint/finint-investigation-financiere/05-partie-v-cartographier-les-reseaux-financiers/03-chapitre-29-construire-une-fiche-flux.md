---
title: Chapitre 29 — Construire une fiche flux
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie V — Cartographier les réseaux financiers
  - index.md
---

## Objectif du chapitre

Maîtriser la **fiche flux** : livrable structurel qui consolide, sur un flux financier ou un ensemble de flux liés, les éléments d’origine, de transit, de destination, et leur qualification typologique. Modèle en annexe E.

## Le concept

Une fiche flux peut concerner :

- **Un flux unique** : un virement, un dépôt, une opération.
- **Une séquence** : plusieurs flux liés (cascade, fractionnement, layering).
- **Un schéma** : une typologie observée sur une période, impliquant plusieurs comptes et entités.

## Structure type

1. **En-tête** : référence, date, version, classification.
1. **Description** : type de flux (virement, dépôt cash, paiement carte, opération crypto), montant, devise, date(s).
1. **Origine** : compte donneur d’ordre, banque, juridiction, titulaire, libellé.
1. **Transit** : banques correspondantes, comptes intermédiaires, rails utilisés (SWIFT, SEPA, SCT Inst, etc.).
1. **Destination** : compte bénéficiaire, banque, juridiction, titulaire, libellé reçu.
1. **Délai** : heure de débit, heure de crédit, délais inter-étapes.
1. **Contexte** : autres flux liés, comportement antérieur, motif déclaré.
1. **Cohérence économique** : flux compatible avec l’activité ? avec les comptes annuels ? avec le profil du titulaire ?
1. **Typologie possible** : à quel schéma ce flux est-il compatible (TBML, BEC, layering, structuration, etc.) ?
1. **Hypothèses calibrées** et niveaux de confiance.
1. **Sources** : DS, relevés (référence interne), OSINT.
1. **Lacunes** et actions complémentaires.

## L’utilité opérationnelle

La fiche flux **isole un cas** pour qu’il puisse être analysé, présenté à un magistrat, ou intégré dans une typologie sectorielle. Elle est particulièrement utile dans les dossiers complexes où plusieurs typologies coexistent : isoler les flux par type permet une analyse plus claire.

## Méthode

1. **Définir le périmètre** : un flux, une cascade, un schéma — préciser dès l’en-tête.
1. **Recueillir tous les attributs** (montants, dates, parties, rails).
1. **Identifier la cohérence ou l’anomalie**.
1. **Confronter à une typologie** : le flux ressemble-t-il à un schéma connu (chapitres 40-47) ?
1. **Calibrer**.

## Mini-walkthrough — séquence BEC fictive (extrait fiche flux)

```
FICHE FLUX — SÉQUENCE BEC LAYERING 14/03
Référence : CLEARFLOW/FLX/021 | v1.0 | TLP:AMBER

DESCRIPTION
- Type : séquence SCT Inst + SCT Inst + dépôts USDT
- Montant total : 215 000 €
- Période : 14/03, 14h32 → 14/03, 18h45 (4h13)

ORIGINE
- Compte source : PME française "ALPHA INDUSTRIE SARL", banque XYZ, IBAN FR...
- Donneur d'ordre : signature du gérant, validation à 14h28
- Contexte : virement présenté comme paiement à un nouveau fournisseur, libellé "trade payment - facture XXXX"

TRANSIT
1. ALPHA SARL → IBAN ES (nouveau) "Iberica Trading SL" : 215 000 €, 14h32, SCT Inst, irréversible.
2. Iberica Trading SL → 5 IBANs (PT x3, LT x2) : fractionnement 40 000 € à 45 000 €, 14h35-14h41.
3. Comptes PT/LT → exchange A : 5 dépôts USDT, 16h12.
4. Exchange A → wallet auto-géré : sortie crypto, 18h45.

DÉLAI TOTAL
- Origine → wallet : 4h13. Fenêtre de gel : quasi-nulle (SCT Inst irréversible).

CONTEXTE
- ALPHA SARL avait reçu un email frauduleux 48h avant, simulant le gérant d'une société partenaire et demandant un changement d'IBAN.
- Le mail provenait d'un domaine très proche du vrai (typosquatting).

COHÉRENCE ÉCONOMIQUE
- Incompatible avec l'activité d'ALPHA (pas de relation antérieure avec Iberica, montant inhabituel, IBAN ES nouveau).

TYPOLOGIE POSSIBLE
- Fraude au virement (BEC) avec layering instantané et cashout crypto.

HYPOTHÈSES CALIBRÉES
- BEC : quasi-certain (séquence et contexte univoques).
- Cashout crypto : quasi-certain.
- Identification de l'auteur : indéterminable à ce stade ; volet on-chain renvoyé à Athéna Group.

SOURCES
- Plainte ALPHA SARL
- Relevés bancaires (réquisition en cours pour comptes ES, PT, LT)
- DS de la banque XYZ
- Analyse on-chain Athéna (en cours)

LACUNES
- Identification de l'attaquant.
- Lien éventuel avec d'autres cas (cluster d'attaques BEC).
```


## Erreurs fréquentes

- **Mélanger plusieurs séquences dans une seule fiche.** Une fiche = un flux ou une séquence cohérente.
- **Ne pas mentionner le délai entre étapes.** La vitesse est un signal essentiel.
- **Conclure sur la typologie sans calibration.** Une « ressemblance » à un schéma TBML ne vaut pas typologie *quasi-certaine*.

## Limites

Beaucoup d’éléments (libellés détaillés, références internes bancaires, métadonnées de l’opération) ne sont accessibles qu’en sources fermées (réquisition, droit de communication CRF).

## Lien avec le fil rouge

> **CLEARFLOW — Une vingtaine de fiches flux**
> 
> Nassim produit, pour le dossier Haddad, environ 22 fiches flux : des séquences de virements depuis l’étranger vers la France, des transferts intra-groupe, des opérations vers la Suisse, des conversions USDT. Chaque fiche, isolée, est lisible ; cumulées, elles forment la base de l’analyse globale (chapitre 35).

## Points clés à retenir

- Fiche flux : un flux ou une séquence cohérente, jamais davantage.
- Délai entre étapes = signal critique.
- Typologie possible = hypothèse, jamais conclusion sans calibration.
- Modèle complet en annexe E.

-----
