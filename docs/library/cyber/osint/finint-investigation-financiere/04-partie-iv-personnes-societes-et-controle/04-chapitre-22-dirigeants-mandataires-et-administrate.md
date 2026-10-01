---
title: Chapitre 22 — Dirigeants, mandataires et administrateurs
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie IV — Personnes, sociétés et contrôle
  - index.md
---

## Objectif du chapitre

Cartographier les **personnes physiques exerçant des fonctions officielles** dans une entité : présidents, gérants, directeurs généraux, administrateurs, membres du conseil de surveillance, secrétaires (UK), commissaires aux comptes, fondés de pouvoir. Identifier les profils anormaux et les patterns suspects.

## Le concept

Toute entité juridique a au moins une **personne physique** investie d’un mandat officiel — c’est le minimum pour qu’elle puisse être représentée. Ces mandats sont déclarés au registre et accessibles publiquement dans la plupart des juridictions.

**Mandats principaux selon les formes** :

- SAS française : président (et éventuellement DG, directeurs adjoints).
- SARL française : gérant(s).
- SA française : conseil d’administration (membres + président) et directeur général, OU directoire + conseil de surveillance.
- Limited UK : directors et secretary.
- GmbH allemande : Geschäftsführer.
- AG allemande : Vorstand (directoire) et Aufsichtsrat (conseil de surveillance).
- LLC américaine : member(s) ou manager(s).
- Trust : trustee(s), settlor, protecteur(s).

**Mandataires accessoires** : commissaires aux comptes (sociétés au-delà des seuils), fondés de pouvoir (pour certaines opérations), liquidateurs (en cas de procédure).

## L’utilité opérationnelle

L’analyse des mandataires permet :

1. **Identifier les acteurs déclarés** — qui répond officiellement de l’entité.
1. **Détecter les profils anormaux** — multi-mandats, retraités âgés, jeunes sans expérience.
1. **Cartographier les liens entre entités** — un même dirigeant pour plusieurs entités = lien fort de contrôle ou de coordination.
1. **Identifier les corporate service providers** — cabinets qui fournissent des mandataires professionnels (« nominee directors ») dans le cadre d’une opacification.

## Méthode — analyse des mandataires

1. **Récupérer la liste des mandataires actuels et passés** (registre).
1. **Profiler chacun** : date d’entrée en fonction, durée, autres mandats déclarés (recherche par nom), profession, profil LinkedIn.
1. **Repérer les patterns** :
- Mandataire avec 20+ mandats actifs dans des sociétés non liées sectoriellement.
- Mandataire âgé sans expérience apparente du secteur.
- Mandataire à l’adresse identique à la société.
- Mandataire d’une société de domiciliation connue.
- Rotation rapide des mandataires (changements multiples en peu de temps).
1. **Croiser avec sanctions, PEP, adverse media** (chapitre 17).

## Mini-walkthrough — analyse des mandataires CLEARFLOW

**Sur les 4 SAS françaises** :

- 2 SAS : Monsieur X comme président, en fonction depuis la création (14 à 22 mois).
- 1 SAS : Mme Z comme présidente, en fonction depuis 11 mois.
- 1 SAS : société de domiciliation comme directeur (rare en France — admis pour certaines formes).

Profilage de Monsieur X :

- LinkedIn minimal, « activité de conseil aux entreprises ».
- 8 mandats actifs identifiés dans Pappers (croisement par nom + date de naissance).
- Tous les mandats dans des SAS de commerce de gros, créées 2022-2024.
- Toutes domiciliées à la même adresse (cabinet de domiciliation).
- Aucune expérience préalable visible dans le négoce.
- 2 procédures collectives sur des sociétés antérieurement gérées (chapitre 16).

→ Profil compatible avec un **gestionnaire multi-mandats au service d’un cabinet de domiciliation**. Niveau de confiance *probable* sur la qualification prête-nom.

Profilage de Mme Z :

- LinkedIn présent, parcours d’agente commerciale dans un autre secteur (parfumerie).
- 1 seul mandat actuel.
- Adresse personnelle distincte de la société.

→ Profil moins suspect, mais à recouper avec relation potentielle à Haddad (réseau personnel).

**Sur les 2 Limited UK** :

- Director déclaré : un Libanais résidant à Dubaï, M. Y.
- PSC : même M. Y (déclaré comme exerçant contrôle significatif via droits de vote).
- Profilage : LinkedIn affichant un parcours dans le négoce libanais, lien visible avec Haddad (employé de longue date selon presse).

→ Profil compatible avec un **collaborateur de confiance** plutôt qu’un prête-nom anonyme. La qualification UBO reste à confirmer (un collaborateur peut être lui-même un prête-nom).

## Erreurs fréquentes

- **Conclure « prête-nom » sans recoupement.** Un mandataire avec plusieurs mandats peut être un gestionnaire légitime (cabinet d’expertise comptable, par exemple).
- **Ignorer les commissaires aux comptes.** Le choix d’un CAC reconnu vs un CAC inconnu peut être un signal.
- **Ne pas chercher les mandats antérieurs.** Les anciennes fonctions racontent l’histoire de la personne.

## Limites

Les registres sont déclaratifs. Un mandataire peut être nominalement en fonction sans exercer réellement le contrôle. Inversement, le contrôle réel peut être exercé par une personne sans mandat déclaré (chapitre 23 sur le contrôle indirect).

## Lien avec le fil rouge

> **CLEARFLOW — Cartographie des mandataires**
> 
> Nassim produit un tableau croisé : 12 personnes physiques exercent des mandats dans les 14 entités du réseau. 5 de ces personnes ont 3+ mandats, dont Monsieur X (gestionnaire français multi-mandats, profil prête-nom probable) et M. Y (libanais à Dubaï, collaborateur de confiance probable). Aucune n’est Karim Haddad lui-même : il **n’apparaît dans aucun mandat officiel** des entités françaises et UK du dossier. Ce constat est important — cela conforte l’hypothèse d’un contrôle indirect (chapitre 23) plutôt que d’une gestion directe.

## Points clés à retenir

- Tous les mandataires des entités cibles sont à profiler.
- Patterns suspects : multi-mandats, profils inadaptés, adresses partagées, rotation rapide.
- Mandataire déclaré ≠ contrôle réel — vérifier par croisement avec UBO.
- Une cartographie « mandataires × entités » est l’un des livrables les plus utiles d’une enquête FININT.

-----
