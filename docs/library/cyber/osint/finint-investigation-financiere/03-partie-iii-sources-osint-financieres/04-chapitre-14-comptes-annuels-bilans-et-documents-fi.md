---
title: Chapitre 14 — Comptes annuels, bilans et documents financiers
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie III — Sources OSINT financières
  - index.md
---

## Objectif du chapitre

Savoir trouver et **lire les documents financiers publiés** par les entreprises pour en extraire des indicateurs de cohérence économique, des signaux d’anomalie, et étayer les hypothèses d’enquête. Le détail technique de l’analyse comptable sera couvert au chapitre 36 ; ici, on se concentre sur l’accès et la lecture rapide.

## Le concept

Selon les juridictions et la taille des entreprises, les **comptes annuels** publiés varient en richesse :

- **Bilan** — photo du patrimoine à une date (actif / passif).
- **Compte de résultat** — flux d’activité sur une période (produits / charges / résultat).
- **Annexe** — explications, méthodes, tableaux complémentaires.
- **Tableau des flux de trésorerie** — variations de cash sur la période (très utile, mais pas obligatoire pour les petites sociétés).
- **Rapport de gestion** — narratif des dirigeants.
- **Rapport des commissaires aux comptes** (CAC) — quand la société y est tenue.

En France : seuils de publication. Au-delà des seuils (à la fois en CA, total bilan, effectif), publication obligatoire au greffe. Possibilité depuis 2014 pour les très petites sociétés de demander la **confidentialité** des comptes (publication avec accès restreint aux assujettis et autorités, pas au public). Chez Pappers et autres agrégateurs, on voit fréquemment la mention « comptes confidentiels ».

Au UK : la quasi-totalité des sociétés publient. Format selon la taille (statutory accounts, abridged, micro-entity).

Aux US : les sociétés non cotées ne publient pas en règle générale ; les sociétés cotées publient via SEC EDGAR (très riches : 10-K, 10-Q, 8-K).

En Allemagne, les sociétés publient au Bundesanzeiger ; en Belgique, au Moniteur belge ; en Italie, à la Camera di Commercio ; au Luxembourg, au RCS (avec certaines obligations spécifiques).

## L’utilité opérationnelle

Lecture FININT d’un bilan / compte de résultat (pour le détail technique : chapitre 36) :

- **Cohérence sectorielle** : la marge brute est-elle cohérente avec le secteur ? Le ratio CA / effectif est-il vraisemblable ?
- **Évolution dans le temps** : les chiffres explosent-ils sans justification ? Sont-ils stables tandis que l’apparence opérationnelle change ?
- **Postes anormaux** : créances clients gigantesques (fictives ?), prêts intragroupe sans contrepartie, immobilisations incorporelles surévaluées, charges de « conseil » dominantes, charges de sous-traitance massives sans personnel propre ?
- **Engagements hors bilan** : garanties, cautions données — souvent dans l’annexe.
- **Écart résultat / trésorerie** : un beau résultat sans cash correspondant est suspect.

## Méthode — récupération et lecture rapide

Pour une société française :

- Pappers : aperçu des comptes publiés.
- Infogreffe : téléchargement de l’acte officiel (PDF) — gratuit ou modique selon les actes.
- INPI/RNE : équivalent.

Pour une société UK : Companies House — téléchargement gratuit.

Pour une société US cotée : SEC EDGAR — téléchargement gratuit.

Pour une société non publique US ou hors UE : selon le pays. Souvent, comptes inaccessibles (juridiction opaque ou exemption). Mention explicite dans le livrable.

**Lecture rapide en 5 ratios clés** :

1. **Marge brute** = (CA - achats consommés) / CA. À comparer avec le secteur.
1. **Marge d’exploitation** = résultat d’exploitation / CA.
1. **Charges de personnel / CA** — donne l’intensité main-d’œuvre.
1. **Stock / CA** — rotation des stocks, anomalie si très élevé.
1. **Créances clients / CA** — délai de paiement clients, anomalie si très élevé (ventes fictives ou clients fragiles).

À comparer avec les ratios moyens du secteur (sources : INSEE, statistiques sectorielles, base de données des cabinets comptables).

## Mini-walkthrough

NEXUS TRADING SAS (France), 1er exercice clos. Comptes publiés (non confidentiels).

- CA : 12,4 M€ — élevé pour un 1er exercice avec dirigeant unique.
- Achats consommés : 11,9 M€. Marge brute : 4 % — très faible pour le négoce de gros (5-10 % attendu).
- Charges de personnel : 32 K€ (un dirigeant, sans salariés). Cohérent avec un dirigeant unique et activité de pure intermédiation.
- Stock : 0 €. Cohérent avec une activité d’intermédiation sans détention.
- Créances clients : 280 K€ (≈ 8 % du CA, soit ~30 jours de délai — normal).
- Résultat d’exploitation : 80 K€. Faible mais positif.
- Trésorerie en fin d’exercice : 35 K€.

Lecture FININT : profil compatible avec une activité de **pure intermédiation commerciale** (pas de stock, pas de salariés autres que le dirigeant) sur un volume élevé pour un 1er exercice. Marge faible mais cohérente avec une intermédiation. Attention : un tel profil est aussi compatible avec une **société de transit** dans un schéma TBML (passage de fonds avec apparence commerciale). Ne tranche pas — élément de soupçon **possible**, à recouper avec la cohérence des contreparties et des marchandises.

## Erreurs fréquentes

- **Lire les chiffres sans les comparer.** Un CA de 12 M€ ne dit rien sans le secteur, la taille, l’historique.
- **Ignorer l’annexe.** Beaucoup d’informations utiles y figurent (engagements, méthodes comptables, événements postérieurs).
- **Surinterpréter une faible marge.** Faible marge ≠ blanchiment automatique. Elle est cohérente avec le négoce de gros, l’intermédiation, certains modèles online.
- **Considérer la « confidentialité » comme un signal en soi.** Beaucoup de TPE françaises légitimes optent pour la confidentialité pour des raisons concurrentielles.

## Limites

Les comptes annuels sont **historiques** (publiés généralement 6 à 12 mois après la clôture). Ils peuvent être **falsifiés** (sans CAC, le contrôle externe est minimal). L’analyste ne peut pas conclure sur les seuls comptes — il les croise.

## Lien avec le fil rouge

> **CLEARFLOW — Lecture des comptes**
> 
> Sur les 4 SAS françaises du réseau Haddad, 2 ont publié des comptes (les 2 plus anciennes), 2 sont en 1er exercice. Sur celles qui ont publié : marges brutes faibles (3-5 %), charges de conseil à des sociétés liées chypriotes (cumulé 280 K€/an), prêts intragroupe sans intérêts apparents. Profil compatible avec un schéma de **transit avec rétention de marge minimale** et **transferts intragroupe possiblement de complaisance**. Soupçons : *probable* à *quasi-certain* sur le schéma de transit, *possible* sur la qualification fraude. Approfondissements requis.

## Points clés à retenir

- Comptes annuels = source publique précieuse, surtout en France et UK.
- Lecture rapide en 5 ratios + comparaison sectorielle.
- Pas de conclusion sur les seuls comptes — toujours croiser.
- L’absence de comptes (confidentialité ou non publication) est documentée mais n’est pas un soupçon en soi.

-----
