---
title: Chapitre 26 — Sociétés écrans et sociétés dormantes
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie IV — Personnes, sociétés et contrôle
  - index.md
---

## Objectif du chapitre

Comprendre la notion de **société écran**, distinguer les **sociétés dormantes**, et caractériser quand une structure est probablement écran sur la base d’un faisceau d’indices.

## Le concept

**Société écran** (shell company). Notion ambiguë. En sens strict : entité juridique sans activité économique réelle, sans personnel, sans actifs autres que les titres de la société, créée pour porter une finalité spécifique sans substance opérationnelle propre.

**Société de façade**. Entité avec une activité économique de façade (apparente) mais dont la véritable fonction est tout autre (canal de blanchiment, fraude, etc.).

**Société dormante**. Entité existante mais qui n’exerce plus d’activité, ni de manière à façade. Distinct de la société écran : dormante = inactive, écran = active mais sans substance économique propre.

**Société boîte aux lettres** (mailbox company, letterbox company). Entité avec une simple adresse de domiciliation, sans présence opérationnelle. Souvent synonyme de société écran selon les contextes.

**Important** : toutes les sociétés écrans **ne sont pas illégales**. Beaucoup ont des usages légitimes :

- Holding de gestion patrimoniale.
- Véhicule de financement (SPV — Special Purpose Vehicle).
- Société de portage temporaire (M&A).
- Société pré-IPO.
- Société pour acquisition immobilière (SCI, REIT, etc.).

**Société écran à finalité illicite** : créée pour dissimuler des transactions, opacifier une chaîne, fictivement justifier des flux, ou frauder.

## L’utilité opérationnelle

L’analyste cherche à qualifier : cette entité est-elle une société écran ? Si oui, à quelle finalité (légitime ou illicite) ?

**Indices d’écran à finalité illicite** :

1. **Absence de substance économique** : pas de personnel, pas de locaux propres, pas d’activité visible.
1. **Adresse de domiciliation** partagée avec de nombreuses autres entités.
1. **Dirigeant unique** avec multi-mandats (signal prête-nom probable).
1. **Création récente** (souvent juste avant la transaction d’intérêt).
1. **Capital social minimal** (1 €, 100 €, 10 000 €).
1. **Comptes non publiés** ou publiés en retard, ou « confidentiels » dès l’origine.
1. **Activité déclarée** (NAF/SIC code) très large et vague (« commerce de gros non spécialisé », « activités de holding »).
1. **Pas de présence web** ou site web vide / générique.
1. **Pas de comptes bancaires identifiables** dans la juridiction du siège, ou banque exotique disproportionnée.
1. **Transactions disproportionnées** avec la taille apparente (CA en M€ avec 1 employé et 1 € de capital).
1. **Liens avec d’autres entités du même profil** (cluster de coquilles).
1. **Présence dans des leaks** (Panama, Pandora) ou dans des bases adverse media.

Aucun indice n’est suffisant ; **plusieurs convergents** qualifient *probable* écran ; **beaucoup convergents + recoupements** approchent du *quasi-certain*.

## Méthode — qualification d’une société écran

1. **Profil de base** : registre, comptes, dirigeants, UBO.
1. **Substance économique** : personnel ? locaux ? site web ? clientèle ? fournisseurs ?
1. **Cohérence sectorielle** : flux compatibles avec activité déclarée ?
1. **Liens à d’autres entités** : appartenance à un cluster ?
1. **Adresse de domiciliation** : combien d’autres sociétés à la même adresse ?
1. **Cumul d’indices** : 5+ indices convergents = *probable* écran.
1. **Calibrer la finalité** : écran légitime (holding patrimonial, SPV) ou écran suspect (canal de blanchiment, fraude, transit fictif) ?

## Mini-walkthrough — NEXUS DELAWARE LLC

- Registre : LLC enregistrée à Delaware en 2022. UBO non accessible (CTA contesté).
- Substance économique : pas de personnel public, pas de site web, pas de présence physique identifiable.
- Adresse de domiciliation : un service de registered agent partagé avec des milliers d’autres LLC Delaware (standard, sans valeur diagnostique en soi).
- Activité : non identifiable.
- Comptes : non publiés (Delaware LLC, exemption).
- Flux observables (via DS) : 850 K€ reçus depuis Chypre, 800 K€ transférés vers un compte personnel suisse. Quelques jours d’écart.
- Lien à d’autres entités : appartient à la chaîne NEXUS du réseau Haddad.

Cumul d’indices : opacité, absence de substance visible, activité non identifiable, flux disproportionnés, cluster d’entités liées. *Probable* société écran à finalité de transit. La finalité (blanchiment ? optimisation ? simple holding ?) reste à confirmer par l’analyse globale des flux et la coopération.

## Erreurs fréquentes

- **Qualifier « société écran » trop facilement.** Beaucoup de PME légitimes ont peu de personnel, un site web minimaliste, une faible présence en ligne.
- **Ignorer les usages légitimes** : SPV, holdings patrimoniaux, sociétés en cours de création.
- **Confondre dormante et écran.** Une société dormante peut être un actif stratégique non frauduleux.
- **Conclure sans cumul d’indices.** Un seul indice ne suffit jamais.

## Limites

La qualification *quasi-certaine* d’écran à finalité illicite exige presque toujours des éléments judiciaires (réquisition des relevés bancaires montrant absence d’activité réelle, audition du dirigeant). L’analyste OSINT s’arrête à *probable*.

## Lien avec le fil rouge

> **CLEARFLOW — Cartographie des écrans probables**
> 
> Sur les 14 entités du réseau Haddad, Nassim qualifie : 4 SAS françaises = *possible* écran (substance économique faible, mais activité commerciale apparente — nécessite confirmation par analyse de flux), NEXUS DELAWARE LLC = *probable* écran de transit, 2 Limited UK = *possible* écran (activité commerciale apparente mais déconnectée du réel à confirmer), entités libanaise et émiraties = données insuffisantes (*indéterminable*). Conclusion : présence d’écrans probables à des fins minimum d’opacification ; finalité illicite *possible* à *probable* selon la confirmation par les flux.

## Points clés à retenir

- Société écran ≠ illégale par nature. Beaucoup d’usages légitimes.
- Société dormante ≠ écran.
- Qualification par **cumul d’indices** : substance économique, personnel, locaux, activité, cohérence, cluster.
- L’analyste OSINT atteint *probable*, rarement *quasi-certain* sans éléments judiciaires.

-----
