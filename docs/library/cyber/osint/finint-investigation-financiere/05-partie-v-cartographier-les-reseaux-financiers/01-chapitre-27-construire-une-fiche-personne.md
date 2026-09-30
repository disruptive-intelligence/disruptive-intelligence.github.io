---
title: Chapitre 27 — Construire une fiche personne
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie V — Cartographier les réseaux financiers
  - index.md
---

## Objectif du chapitre

Maîtriser la **fiche personne FININT** : structure standardisée pour consolider, en un livrable réutilisable, tous les éléments collectés sur une personne physique. Le modèle complet est en annexe C ; ce chapitre expose la logique et les choix méthodologiques.

## Le concept

Une fiche personne est un livrable **atomique** : elle concentre, sur une personne, l’ensemble des éléments d’identification, de profil, de mandats, de patrimoine, de relations et de contentieux. Elle est conçue pour être :

- **Autonome** : lisible sans contexte préalable.
- **Sourcée** : chaque élément factuel renvoie à sa source.
- **Calibrée** : niveau de confiance pour chaque élément non trivial.
- **Versionnée** : date de production, date de dernière mise à jour, version.
- **Actionnable** : conclusions et recommandations en fin.

## Structure type d’une fiche personne

1. **En-tête** : référence, date, version, classification (TLP), auteur.
1. **Identification** : nom complet, date de naissance, lieu, nationalité(s), adresse(s), photo si disponible. Niveau de confiance global de l’identification.
1. **Profil** : parcours professionnel, formation, langues parlées (signaux d’enquête utiles), affiliations professionnelles, fonctions publiques antérieures, profil PEP éventuel.
1. **Mandats actuels** : liste des sociétés où la personne exerce un mandat, avec rôle, juridiction, période.
1. **Mandats antérieurs** : historique.
1. **UBO et contrôle indirect** : entités où la personne est UBO identifié, déclaré ou *probable*.
1. **Patrimoine identifié** : immobilier, financier, actifs particuliers (œuvres, véhicules, bateaux, etc.), train de vie observable.
1. **Réseau** : famille proche, collaborateurs réguliers, associés, personnes clés du dossier.
1. **Contentieux et réputation** : procédures publiques, condamnations, sanctions, adverse media.
1. **Sanctions et PEP** : présence sur listes, statut PEP, vérifications screening.
1. **Liens crypto** (si pertinent) : adresses ou attributions on-chain — renvoi vers OSINT Crypto pour le traitement détaillé.
1. **Hypothèses calibrées** : ce que l’analyste retient sur cette personne, avec niveaux de confiance.
1. **Sources** : liste exhaustive avec dates.
1. **Lacunes et actions complémentaires** : ce qui n’a pas pu être établi, et comment le faire.

## L’utilité opérationnelle

La fiche personne est **réutilisable** : produite une fois, elle alimente plusieurs livrables (note FININT, dossier d’enquête, dossier compliance). Elle est **interopérable** : un format standardisé permet à différents analystes de se transmettre l’information sans perte.

Elle est aussi un **outil de discipline** : la rédiger oblige à expliciter ce qu’on sait et ce qu’on ne sait pas. C’est un puissant antidote aux conclusions précipitées.

## Méthode — bonnes pratiques

- **Ne pas confondre fiche et résumé** : la fiche est exhaustive sur ce qui est connu, pas un résumé.
- **Sourcer chaque élément** : pas d’affirmation sans référence.
- **Calibrer chaque conclusion** : niveau de confiance.
- **Distinguer mandat déclaré et contrôle réel**.
- **Respecter la présomption d’innocence** : un mis en examen n’est pas un coupable.
- **Mentionner les lacunes** : la fiche ne fait pas semblant de tout savoir.

## Mini-walkthrough — fiche Karim Haddad (extrait)

```
FICHE PERSONNE — KARIM ÉLIE HADDAD
Référence : CLEARFLOW/PER/001 | v1.3 | 14/03 | TLP:AMBER

IDENTIFICATION (quasi-certain)
- Né le 17/04/1968 à Beyrouth, Liban
- Nationalités : libanaise (par naissance), française (par naturalisation, 2006)
- Adresses : Paris 16e (résidence principale déclarée), Beyrouth (Achrafieh), Dubaï (DIFC apartments)
- Photo : LinkedIn, presse libanaise 2023

PROFIL (probable)
- Diplômé ESCP Paris (1992), parcours négoce international depuis 1995
- Langues : arabe, français, anglais
- Pas de fonction publique connue
- Pas de statut PEP au sens strict
- Affiliation : Chambre de commerce franco-libanaise (membre actif)

MANDATS ACTUELS DÉCLARÉS (quasi-certain)
- NEXUS LIBAN SAL — administrateur (Liban, depuis 2002)
- NEXUS INTERNATIONAL FZ — propriétaire (Émirats, free zone)
- (aucun mandat déclaré dans les 4 SAS françaises ni dans les 2 Limited UK)

UBO PROBABLE OU IDENTIFIÉ
- OMEGA HOLDINGS TRUST (Chypre) — settlor identifié via Pandora (quasi-certain)
- NEXUS HOLDINGS LTD (Chypre) — UBO probable via chaîne (probable)
- 4 SAS françaises — UBO réel probable via prête-noms (probable)
- LLC Delaware — non confirmé (indéterminable)
- (autres entités, voir fiche groupe)

PATRIMOINE IDENTIFIÉ
- Immobilier : 3 biens à Paris (SCI), 1 villa à Beyrouth, présence à Dubaï (location non confirmée)
- Financier : participations dans le groupe, comptes bancaires en France, présomé en Suisse (DS)
- Train de vie : voyages réguliers Paris-Beyrouth-Dubaï-Genève, événements caritatifs au Liban

RÉSEAU
- Famille : épouse française, 3 enfants. Frère installé à Dubaï (lien d'affaires).
- Collaborateurs identifiés : M. Y (Dubaï, dirigeant déclaré Limited UK), Mme Z (présidente d'une SAS, lien personnel)

CONTENTIEUX ET RÉPUTATION
- Transaction fiscale française 2018 (sans poursuite pénale ; presse)
- Aucune condamnation publique
- Adverse media : présence dans presse régionale, allégations 2023 (Côte d'Ivoire) sans nomination explicite

SANCTIONS / PEP
- Aucune sanction OFAC, UE, ONU, OFSI vérifiées
- Non-PEP au sens strict (pas de fonction publique)

LIENS CRYPTO
- Mentions USDT dans certaines DS — volet renvoyé à Athéna Group / Sarah Marin pour analyse on-chain

HYPOTHÈSES CALIBRÉES
- UBO réel d'une majorité des entités du réseau Haddad : probable.
- Implication dans schéma de transit financier multi-juridictionnel : probable.
- Implication directe dans blanchiment ou contournement de sanctions : possible à ce stade, à confirmer par flux et coopération.

LACUNES
- Comptes bancaires libanais et suisses : accès non obtenu (coopération en cours).
- Liste exhaustive des bénéficiaires d'OMEGA TRUST : non connue.
- Substance économique des entités émiraties : non vérifiée.

SOURCES (extrait)
- Pappers, INPI, RBE [04/03]
- Companies House, PSC [05/03]
- OpenCorporates, Sayari [05/03]
- ICIJ Pandora Papers, Aleph OCCRP [06/03]
- LinkedIn, presse [07/03]
- Patrim France [08/03]
- DS reçues par CRF (référencées en interne)
```


## Erreurs fréquentes

- **Fiche incomplète sans mention des lacunes.** Un livrable lisse passe pour exhaustif et trompe le lecteur.
- **Mélanger les niveaux de confiance.** Tout n’est pas *quasi-certain*. La calibration explicite est obligatoire.
- **Ne pas dater chaque élément.** Les profils changent.

## Limites

Une fiche ne remplace pas une analyse contextuelle. Elle l’alimente. Elle ne dit pas non plus *« cette personne est coupable »* — ce vocabulaire n’a pas sa place ici.

## Lien avec le fil rouge

> **CLEARFLOW — La fiche au cœur du dossier**
> 
> La fiche Karim Haddad est le pivot du dossier de Nassim. Elle est mise à jour à chaque étape majeure. À la finale, elle sera produite en annexe de la note de transmission au PNF. Toute autre fiche du dossier (M. Y, Mme Z, M. X, etc.) suit le même modèle.

## Points clés à retenir

- Fiche = livrable autonome, sourcé, calibré, versionné, actionnable.
- 14 sections type ; modèle complet en annexe C.
- Discipline d’explicitation des lacunes.
- Pas de conclusion de culpabilité dans une fiche.

-----
