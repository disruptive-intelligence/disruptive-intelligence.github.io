---
title: Chapitre 38 — Factures, marges, marchandises et cohérence économique
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VI — Analyse de flux et comptabilité forensique
  - index.md
---

## Objectif du chapitre

Maîtriser la **vérification de la cohérence économique** : confronter les flux financiers à la réalité opérationnelle attendue — marchandises, marges, factures, transport, logistique.

## Le concept

Une fraude moderne (notamment TBML — chapitre 41) repose sur la **dissociation entre flux financier et flux physique**. Une facture peut être payée sans contrepartie réelle de marchandise ; une marchandise peut être surfacturée ou sous-facturée ; un transport peut être déclaré sans avoir lieu.

L’analyse de cohérence économique cherche à confronter :

- **Le flux financier déclaré** (virement, facture).
- **La marchandise présumée** (nature, quantité, valeur de marché).
- **La logistique attendue** (transport, douane, certificats).
- **La marge réalisée** (cohérence avec les pratiques sectorielles).

## L’utilité opérationnelle

Pour de nombreux schémas, c’est l’analyse de cohérence économique qui **trahit la fraude**. Une facture intracommunautaire de 800 K€ pour une marchandise dont la valeur de marché est de 200 K€ est un signal fort.

## Méthode — vérifier la cohérence

1. **Identifier la marchandise** (nature, quantité, qualité) via la facture, le contrat, les documents douaniers.
1. **Estimer la valeur de marché** : sources sectorielles, comparables, expertise.
1. **Vérifier la cohérence du prix** : sur-facturation ? sous-facturation ?
1. **Vérifier la logistique** : la marchandise a-t-elle été transportée ? Quels documents (CMR, BL, EUR1, certificats d’origine) ?
1. **Vérifier les contreparties** : le fournisseur et le client ont-ils l’activité, la capacité, les références pour cette opération ?
1. **Confronter avec les flux bancaires** : le paiement correspond-il en montant, en date, en parties ?

## Sources de référence pour les valeurs de marché

- **Indices sectoriels** : matières premières (LME, ICE, CME), agricoles (Bourse de Chicago, Euronext Paris), énergie.
- **Statistiques douanières** : Eurostat Comext (UE), UN Comtrade, customs databases (CBP US).
- **Bases B2B** : Alibaba, plateformes sectorielles (prix indicatifs).
- **Expertise sectorielle** : cabinets spécialisés.

## Mini-walkthrough — TBML avec sur-facturation

Cas type : une SARL française importe du matériel agricole d’occasion (tracteurs) depuis un fournisseur émirati.

- Facture : 8 tracteurs Massey Ferguson 5710 SL d’occasion, 95 000 € chacun, soit 760 K€.
- Valeur de marché de référence (occasion, modèles 2018-2020) : environ 35-45 K€ pièce, soit 280-360 K€ pour 8 unités.
- Sur-facturation apparente : environ × 2.
- Documents : CMR sommaire, certificats d’origine douteux (mise en cause par presse régionale).

Lecture FININT : profil compatible avec une **sur-facturation TBML** où le surplus payé (~400 K€) est en réalité une **rétrocession** vers le payeur ou un destinataire désigné. C’est un schéma classique pour transférer de la valeur sous couvert de commerce.

## Erreurs fréquentes

- **Confondre prix sur facture et valeur réelle** : prendre la facture au pied de la lettre.
- **Ignorer les particularités sectorielles** : un matériel sur-spécifié peut être légitimement plus cher.
- **Conclure trop vite sans expertise** : la cohérence économique fine exige parfois un sectoriste.

## Limites

La vérification de cohérence économique exige une **expertise sectorielle** ou un accès à des bases de prix. Sans cela, l’analyste se borne à signaler une probable anomalie et propose une expertise.

## Lien avec le fil rouge

> **CLEARFLOW — Le marché ivoirien réexaminé**
> 
> Le marché public ivoirien de fourniture de matériel agricole remporté par NEXUS NEGOCE (Côte d’Ivoire) en 2023 pour 3,2 M€ peut être réexaminé : les types de tracteurs livrés (selon les documents publics ivoiriens) valent au marché européen environ 1,5 M€. Sur-facturation apparente : ×2. Compatible avec un schéma combinant favoritisme (marché remporté dans des conditions discutées) et sur-facturation (rétrocommissions probables). Le volet ivoirien est renvoyé en coopération internationale ; depuis la France, on documente la *probable* sur-facturation comme élément du faisceau.

## Points clés à retenir

- Dissociation flux financier / flux physique = vecteur classique de fraude.
- Vérifier marchandise, valeur de marché, logistique, contreparties.
- Sur-facturation et sous-facturation = signaux TBML.
- Expertise sectorielle souvent requise pour la qualification fine.

-----
