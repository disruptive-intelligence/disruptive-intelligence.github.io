---
title: Chapitre 87 — Note courte OSINT
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 87.1 La note courte : format de référence quotidien

La **note courte** est le format de référence pour communiquer rapidement un résultat OSINT à un commanditaire ou à une hiérarchie. Elle existe sous plusieurs formes selon les contextes : note de renseignement militaire (RM) dans les armées, brève dans la presse, alerte CTI dans la cybersécurité, note flash en cabinet de conseil.

Elle a en commun **brièveté**, **calibration**, **structure stable**. Une note courte rate sa cible si :

- elle se perd en contexte au lieu d'aller au fait ;
- elle sur-affirme ce que l'évidence ne soutient pas ;
- elle empile sans hiérarchiser ;
- elle masque les limites pour paraître plus convaincante.

## 87.2 Structure standard de la note courte

Une note courte type comporte **5 sections** stables :

1. **En-tête identifiant.**
2. **BLUF (Bottom Line Up Front).**
3. **Contexte / cadrage minimal.**
4. **Faits saillants cotés.**
5. **Limites et recommandation.**

Une page A4, 400-700 mots, lisibilité en 3 minutes. Le destinataire saisit l'essentiel sans avoir à lire toute la note.

## 87.3 En-tête identifiant

L'en-tête doit fournir en un coup d'œil :

- **Titre** clair et neutre.
- **Auteur** (cellule, signature ou identifiant).
- **Date** d'émission.
- **Référence interne** (numéro de dossier).
- **Diffusion / classification** (TLP, RGPD si données personnelles, confidentialité contractuelle).
- **Sujet** (entité concernée).
- **Niveau de confiance global** (probable / possible / quasi-certain / indéterminable).

L'en-tête sert aussi de **traçabilité** : retrouvable dans un système d'archivage, lié à un mandat précis.

## 87.4 BLUF : la conclusion en première ligne

Le **BLUF** (Bottom Line Up Front) est l'usage militaire qui place la **conclusion** en tête. Le lecteur lit d'abord ce qui est conclu, puis lit les justifications.

**Exemple BLUF court.**

> **BLUF.** Les recherches effectuées sur la société Verde Holdings (Chypre) confirment son immatriculation, sa direction par Marc Delaunay et Marina Constantinidou, et son lien probable avec un montage offshore impliquant Delta Consulting Ltd (Malte) et TechnoVert SAS. Niveau de confiance : probable. Approfondissement et expertise complémentaires recommandés.

Le BLUF est calibré : « probable », pas « prouvé ». Il intègre la recommandation, pas seulement le constat. Il pose les enjeux : à lui seul, il informe.

## 87.5 Contexte / cadrage minimal

**Cadrage** = pourquoi cette note, pour qui, dans quel mandat, avec quelles questions de renseignement.

**Exemple.**

> Note produite à la demande du cabinet Legrand & Associés (mandat 2026-05-16) dans le cadre d'une enquête de due diligence préalable à audit forensique sur la société TechnoVert SAS. La présente note concerne les volet « structures offshore » et « bénéficiaire effectif » du dossier global MIRAGE.

Cadrage = 2-5 lignes. Pas de remplissage. Le destinataire connaît son mandat.

## 87.6 Faits saillants cotés

**Cœur de la note.** Liste structurée des faits clés, chacun avec sa cotation.

**Format recommandé.**

| Fait | Source | Cotation |
|---|---|---|
| Verde Holdings est immatriculée à Chypre depuis 01/2022 | Companies Registry CY | A1 |
| Marc Delaunay est administrateur déclaré et UBO 100 % | Registre UBO CY (accès partiel) | A1 |
| Marina Constantinidou est administratrice locale (probable nominee) | Cross-référence cabinets locaux | B2 |
| Verde a reçu des flux entrants depuis Delta Consulting Ltd | Cyprus Confidential (ICIJ leak) | B2 |
| Aucune sanction / PEP active | OpenSanctions | A1 |

Chaque fait est :

- **précisément formulé** (pas de généralité vague),
- **sourcé** (clic possible vers la source archivée),
- **coté** Admiralty,
- **autonome** (lisible isolément).

## 87.7 Limites et recommandations

**Limites.**

> - L'accès au registre UBO chypriote est restreint depuis 2022 (arrêt CJUE). Les éléments retenus s'appuient sur la portion accessible et sur Cyprus Confidential. Une réquisition judiciaire permettrait l'accès complet.
> - L'analyse des flux financiers réels reste hors périmètre OSINT (comptes consolidés non publiés au-delà des obligations légales chypriotes).
> - L'attribution effective des bénéfices économiques de Verde reste à confirmer par audit comptable forensique.

**Recommandations.**

> - Inscrire Verde Holdings dans la procédure en cours et solliciter, dans le cadre judiciaire, les pièces complètes au registre chypriote.
> - Mandater expertise comptable forensique sur les comptes consolidés TechnoVert (2020-2025) pour identifier les écritures cohérentes avec flux vers Delta puis Verde.
> - Sécuriser l'archive des captures réalisées (en annexe), aux fins de cohérence en cas de procédure.

La note courte se termine par **action attendue** explicite, jamais en l'air.

## 87.8 Cas d'usage de la note courte

**Note flash quotidienne.** Cellule de veille qui transmet à la direction l'élément du jour.

**Briefing matinal.** Avant une réunion, synthèse d'une recherche.

**Note d'alerte.** Élément critique nécessitant attention immédiate (un dirigeant cible vient d'être placé sur liste de sanctions, par exemple).

**Note préparatoire.** Avant une audition, négociation, ou démarche, synthèse de l'état des connaissances.

**Note de transition.** Passage de relai entre analystes (départ en congés, fin de mission, escalade).

## 87.9 Variantes spécialisées

**Note CTI.** Format STIX/TAXII si transmise machine-to-machine. Sinon, version humaine adaptée : IOCs, TTPs, attribution, action recommandée.

**Note judiciaire.** Plus formelle (Ch.90). Vocabulaire calibré pour magistrat.

**Note de presse / pour journaliste.** Plus pédagogique, moins de jargon, mais maintien rigueur.

**Note interne RSSI.** Concentrée sur action défensive (patches, monitoring, communications).

## 87.10 Erreurs fréquentes à éviter

**Verbosité.** Étirer ce qui pourrait être dit en 3 lignes. Le destinataire perd le fil.

**Pas de BLUF.** Forcer le lecteur à lire la note pour trouver la conclusion.

**Sur-affirmation.** Pour paraître convaincant, formuler comme une certitude ce qui est probable. Carrière courte.

**Empilement sans hiérarchisation.** Liste de 30 faits sans poids relatif.

**Pas de cotation.** Le lecteur ne sait pas évaluer la fiabilité.

**Pas de limites.** Apparence de complétude pour masquer ce qui manque.

**Pas de recommandation.** Note descriptive sans valeur ajoutée actionnable.

## 87.11 Lisibilité et accessibilité

Une note courte doit être **lisible par un non-spécialiste**. L'analyste maîtrise le sujet ; le destinataire ne le maîtrise pas nécessairement.

**Pratique.**

- Acronymes développés à la première occurrence.
- Glossaire bref si nécessaire (en bas de page ou annexe courte).
- Pas de jargon inutile.
- Schémas / tableaux pour ce qui se visualise mieux qu'il ne s'explique.

## 87.12 Modèle de note courte MIRAGE — entité Verde Holdings

```
NOTE COURTE — OSINT MIRAGE
Sujet : Société Verde Holdings (Chypre)
Mandat : 2026-05-16, Cabinet Legrand & Associés
Auteur : Cellule MIRAGE
Date : 2026-05-XX
Référence interne : MIRAGE/N-014
Diffusion : TLP:AMBER (cabinet, magistrat saisissant uniquement)
Niveau de confiance global : probable

BLUF
Verde Holdings (Chypre) est confirmée comme société détenue 
intégralement par Marc Delaunay, recevant des flux entrants depuis 
Delta Consulting Ltd (Malte) elle-même alimentée probablement par 
TechnoVert SAS. Niveau de confiance : probable. Approfondissement 
judiciaire et expertise comptable forensique recommandés.

Cadrage
Note produite dans le cadre du mandat MIRAGE (cabinet Legrand & 
Associés). Volet investigué : structures offshore et bénéficiaire 
effectif. Périmètre : sources ouvertes exclusivement.

Faits saillants cotés
[tableau de 5-7 faits cotés, comme ci-dessus]

Limites
- Registre UBO chypriote partiellement accessible (post-CJUE 2022).
- Comptes Verde non publiés.
- Attribution effective des bénéfices à confirmer par audit.

Recommandations
- Inscrire Verde dans procédure et solliciter pièces officielles.
- Mandater expertise comptable forensique TechnoVert 2020-2025.
- Préserver captures (annexe disponible sur demande).

Annexes (sur demande)
- Captures Companies Registry CY (Hunchly).
- Capture Cyprus Confidential mémo (avec hash).
- Synthèse cluster offshore (graphe Maltego).

Signature et hash de cette note : [SHA-256]
```


## 87.13 Synthèse

La note courte est l'**outil de communication quotidien** de l'analyste OSINT. Maîtrisée, elle économise du temps à tout le monde, inspire confiance, et trace l'activité de la cellule.

-----
