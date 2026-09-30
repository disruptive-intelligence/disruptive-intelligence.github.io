---
title: Chapitre 89 — Fiches opérationnelles
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 89.1 La fiche comme atome du dossier

Les **fiches opérationnelles** sont les briques élémentaires d'un dossier OSINT mature. Là où le rapport raconte, la fiche **structure**. Une fiche par entité, mise à jour au fil de l'enquête, exploitée en annexe du rapport, réutilisable d'une enquête à l'autre (avec déontologie de cloisonnement).

## 89.2 Types de fiches

**Fiche personne physique.**

- Identité civile vérifiée.
- Identités numériques (comptes, emails, téléphones, usernames).
- Parcours (formation, carrière).
- Réseau personnel et professionnel.
- Patrimoine visible.
- Présence médiatique.
- Indicateurs de risque (sanctions, PEP, adverse media).
- Cotation globale et niveau de confiance.

**Fiche société.**

- Identité légale (numéro, juridiction, forme, capital, dates).
- Gouvernance (dirigeants, conseil, commissaires aux comptes).
- Actionnariat et UBO.
- Activité déclarée vs observée.
- Indicateurs financiers visibles.
- Sociétés liées (filiales, groupe, dirigeants partagés).
- Indicateurs de risque.
- Cotation globale.

**Fiche domaine / infrastructure.**

- Domaine principal et sous-domaines.
- WHOIS (actuel + historique).
- DNS records.
- Certificats TLS.
- Hébergement (IPs, ASN).
- Technologies (Wappalyzer).
- Trackers / analytics.
- Liens vers autres domaines (via WHOIS, certificats, trackers).
- Cotation globale.

**Fiche compte (réseau social).**

- Plateforme.
- Username, ID interne.
- Date de création.
- Profil (photo, bio).
- Activité (cadence, sujets, ton).
- Réseau social (followers / followings).
- Liens vers autres comptes.
- Indicateurs d'inauthenticité éventuels.
- Cotation globale.

**Fiche contenu (image, vidéo, audio, document).**

- Identification (URL, hash, taille, format).
- Métadonnées (EXIF, C2PA, IPTC).
- Source originelle (provenance).
- Recherche inversée (autres apparitions).
- Analyse technique (ELA, AI detection).
- Géolocalisation et chronolocation si applicable.
- Cotation d'authenticité.
- Cotation de pertinence.

**Fiche lieu.**

- Coordonnées GPS / adresse.
- Cadastre / immatriculation.
- Propriétaire (s'il est public).
- Photos et contexte.
- Indicateurs (visite cible documentée, etc.).

**Fiche événement.**

- Date / heure / lieu.
- Acteurs présents.
- Sources documentant.
- Patterns associés.

## 89.3 Format standard d'une fiche

**Une fiche tient idéalement sur 1-3 pages** lisibles.

**Sections type.**

1. **En-tête.** Type d'entité, identifiant interne, statut (en cours / clos), dernière mise à jour.
2. **Sélecteurs forts.** Identifiants uniques (numéro entreprise, email confirmé, téléphone).
3. **Caractéristiques structurelles.**
4. **Liens vers autres entités.** Cross-références.
5. **Sources principales.**
6. **Cotation globale.** Avec justification.
7. **Notes d'enquête.** Observations, hypothèses, pistes.

## 89.4 Cotation par fiche

Chaque fiche porte une **cotation globale** qui résume :

- Solidité de l'identification (l'entité est-elle bien celle qu'on pense ?).
- Complétude (combien de dimensions investiguées ?).
- Niveau de confiance des éléments retenus.

**Exemple.**

- Fiche Verde Holdings : identification A1 (registre officiel), complétude moyenne (registre UBO partiel post-CJUE), niveau de confiance global : élevé sur l'existence et le contrôle, modéré sur les flux financiers.

## 89.5 Maintenance dans la durée

Une fiche **vit**. Elle est mise à jour à chaque nouvelle information pertinente.

**Discipline.**

- Versioning des fiches.
- Historique des modifications (git si vault).
- Mention de la date de dernière vérification de chaque fait.

## 89.6 Fiches comme annexe du rapport

Dans le rapport final, les fiches apparaissent en annexe. Elles permettent au lecteur de retrouver rapidement le détail sur n'importe quelle entité mentionnée dans le corps du rapport.

**Format.** Fiches au sein du même document (PDF) ou liées (références hyperliens).

## 89.7 Réutilisabilité (avec déontologie)

Les fiches sont **précieuses** : elles capitalisent le travail.

**Déontologie.**

- Pas de mélange entre enquêtes différentes (un mandat de cabinet A ne nourrit pas un cabinet B).
- Données personnelles purgées en fin de mandat (RGPD).
- Réutilisation des fiches « génériques » (organisations, infrastructure publique) seule.
- Documentation rigoureuse de l'origine.

## 89.8 Exemple — fiche personne MIRAGE (extrait)

```
FICHE PERSONNE — Marc Delaunay
Identifiant interne : MIRAGE/P-001
Statut : en cours
Dernière mise à jour : 2026-05-XX
Cotation globale : élevée (identification multi-corroborée)

Sélecteurs forts
- Nom complet : Marc Henri Delaunay (cohérent multi-sources)
- Date de naissance : 1976-XX-XX (déduite, à confirmer)
- SIREN administrateur Delta Consulting Ltd
- UBO Verde Holdings 100 %
- Email perso présumé : marc.delaunay76@gmail.com (B2)

Identité civile vérifiée
- Citoyenneté : française (présomption forte)
- Adresse résidentielle : Paris 17e (confirmée, via Pappers SCI)
- État civil : marié, deux enfants (déduit photos LinkedIn)

Identités numériques
- LinkedIn : marc-delaunay-XX (vérifié)
- Twitter/X : @mdelaunay76 (verrouillé, faible activité)
- Instagram : mdelaunay76 (privé)
- GitHub : mdelaunay (inactif depuis 2019)
- Email perso : marc.delaunay76@gmail.com (HIBP, Holehe confirment)
- ProtonMail : ********** (existe selon stealer log, non confirmé)

Parcours
- 2002 : X-Ponts (LinkedIn, A1)
- 2007 : audit Big 4 (LinkedIn, A1)
- 2014 : DAF société industrielle (LinkedIn, A1)
- 2019-06 : DAF TechnoVert SAS (LinkedIn + communiqué TechnoVert, A1)

Patrimoine visible
- SCI La Provence Familiale (Goult, Vaucluse) : mas estimé 1.8 M€
- Villa Marrakech : 800 k€ (Cyprus Confidential mention)
- Appartements parisiens : SCI nominee, à confirmer
- Compte Binance perso (stealer log)

Indicateurs de risque
- Sanctions : aucune (OpenSanctions A1)
- PEP : non
- Adverse media : aucun public identifié
- Liens offshore : Delta Consulting (Malte), Verde Holdings (Chypre)
- Patrimoine vs revenus : incohérence apparente (élément d'alerte)

Réseau professionnel et personnel
- TechnoVert (DAF) : Pierre Dubois (DG), Sophie Martin (DRH)
- Réseau LinkedIn : 487 contacts, dont 12 PDG/DG identifiés
- Cabinet conseil : non identifié à ce stade

Liens vers autres fiches
- Société TechnoVert SAS (E-001)
- Société Delta Consulting Ltd (E-002)
- Société Verde Holdings (E-003)
- SCI La Provence Familiale (E-004)
- Compte Twitter/X @mdelaunay76 (C-007)
- Mas Goult (L-002)

Notes d'enquête
- Empreinte SOCMINT volontairement faible.
- Stealer logs offrent pivot crypto significatif.
- Profil patrimonial à approfondir judiciairement.

Sources principales avec captures
- LinkedIn (Hunchly 2026-XX-XX, hash)
- Pappers TechnoVert (Hunchly, hash)
- Companies Registry Malta (Delta Consulting, hash)
- Companies Registry Cyprus (Verde Holdings, hash)
- Cyprus Confidential ICIJ (capture, hash)
- HIBP / Hudson Rock (capture, hash)
- [autres]
```


Une fiche personne mature peut représenter 3-5 pages structurées.

## 89.9 Pièges fréquents

**Sur-déclaration.** Affirmer ce qui n'est pas certain dans la fiche. Cotation absente.

**Sous-déclaration.** Ne pas documenter ce qui est connu, par paresse.

**Pas de cross-référence.** Fiches isolées, sans liens entre elles. Le dossier devient illisible.

**Pas de versioning.** Modifications non tracées. Une analyse contestée n'a pas d'historique.

## 89.10 Synthèse

Les fiches sont le **squelette** du dossier d'enquête. Bien tenues, elles structurent le travail, soutiennent le rapport, capitalisent l'expertise. Mal tenues, elles désorganisent.

-----
