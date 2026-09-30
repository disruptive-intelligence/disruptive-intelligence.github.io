---
title: Chapitre 55 — C2PA, Content Credentials et provenance
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE VIII — Vérification, deepfakes et provenance
  - index.md
---

## 55.1 Le tournant provenance

Face à l'impasse de la détection a posteriori, l'industrie a basculé vers la **provenance** : prouver l'**origine** et l'**historique** d'un contenu plutôt que tenter de détecter sa falsification.

**Coalition for Content Provenance and Authenticity (C2PA).** Coalition créée 2021 par Adobe, Microsoft, BBC, Intel, Truepic, autres. Standard ouvert.

**Implication.** En 2026, les principales plateformes et créateurs commencent à intégrer C2PA. **Standard émergent de référence** pour la preuve d'authenticité.

## 55.2 Principe C2PA

À chaque création / modification d'un contenu, des **métadonnées signées cryptographiquement** sont attachées :

- **Créateur** (identité, certificat).
- **Outil de création** (appareil photo, logiciel).
- **Date et heure**.
- **Modifications successives** (chaîne d'éditions).
- **Signature** prouvant l'intégrité.

L'ensemble est appelé **manifest C2PA**. Embarqué dans le fichier ou stocké séparément (lien dans le fichier).

## 55.3 Comment ça fonctionne

**Création.** Un appareil photo C2PA (Leica M11-P, Sony Alpha 1 II, etc.) ou un logiciel C2PA (Photoshop avec Content Credentials, etc.) crée un manifest signé.

**Édition.** Toute édition signée ajoute un nouveau manifest à la chaîne, prouvant ce qui a été modifié.

**Consultation.** Un viewer C2PA (extension navigateur, Verify Tool) affiche la chaîne de provenance.

## 55.4 Content Credentials (Adobe)

**Content Credentials** est l'implémentation grand public d'Adobe basée sur C2PA. Intégrée dans Photoshop, Lightroom, Firefly.

**Indicateur visuel.** Petite icône « CR » sur les contenus avec Content Credentials.

**Verify Tool.** contentcredentials.org/verify permet de vérifier un fichier.

## 55.5 Déploiement 2024-2026

**Plateformes adoptant C2PA.**

- **TikTok** : étiquetage automatique des contenus IA (2024).
- **Meta** (Facebook, Instagram) : étiquetage IA progressif.
- **YouTube** : labels « altered / synthetic content ».
- **OpenAI** : intègre C2PA dans DALL-E.
- **Adobe Firefly** : C2PA natif.
- **Leica, Sony, Nikon** : appareils photo C2PA-compatibles.

**Mais.** Adoption fragmentaire en 2026. Beaucoup de contenus ne portent pas encore C2PA. **Absence** de C2PA ne prouve pas faux.

## 55.6 Outils de vérification C2PA

**contentcredentials.org/verify** : interface web officielle.

**C2PA viewer** : extension navigateur.

**Verify CLI** : outil terminal.

**Adobe Verify** : interface intégrée Adobe.

## 55.7 Limites C2PA

**Adoption partielle.** Pas tous les créateurs / appareils / logiciels intègrent C2PA en 2026.

**Manipulation possible.** Un faux peut être créé sans C2PA, ou avec un C2PA falsifié si la clé privée du créateur est compromise.

**Stripping.** Les métadonnées peuvent être supprimées (capture d'écran, re-upload sans préservation).

**Identité du créateur.** Le manifest prouve l'identité de l'**outil** (signature). Pour prouver l'identité du **créateur humain**, lien à infrastructure de certificats plus complexe.

**Vie privée.** Manifest peut exposer information de l'auteur, contraire à anonymat parfois souhaité.

## 55.8 Pratique OSINT 2026

**Toujours vérifier C2PA** sur contenu critique :

1. Inspecter présence de manifest.
2. Verify Tool si présent.
3. Examiner la chaîne (créateur, outil, édition).
4. Documenter résultat.

**Présence C2PA cohérent = forte présomption d'authenticité.**

**Absence C2PA ≠ preuve de faux.** Beaucoup de contenus légitimes (anciens, ou créateurs non équipés) n'ont pas C2PA.

## 55.9 Méthodologie de vérification provenance

Pour un contenu critique :

1. **Inspecter C2PA** (presence + chain).
2. **Examiner métadonnées** (EXIF, IPTC, XMP).
3. **Rechercher source originelle** (Ch.46).
4. **Comparer avec C2PA de référence** si l'auteur est identifié.
5. **Synthèse cotée**.

## 55.10 Au-delà C2PA : SynthID, watermarking (Ch.56)

Voir chapitre suivant pour l'autre branche : watermarks invisibles dans contenu IA pour faciliter détection.

## 55.11 Implication judiciaire émergente

En 2026, les magistrats commencent à demander des **provenance reports** sur les pièces numériques sensibles. Pas obligation légale en France, mais tendance.

**Pour l'analyste OSINT.**

- Documenter systématiquement la provenance dans le rapport.
- Préserver les manifests C2PA quand ils existent.
- Recommander expertise complémentaire pour pièces centrales.

-----
