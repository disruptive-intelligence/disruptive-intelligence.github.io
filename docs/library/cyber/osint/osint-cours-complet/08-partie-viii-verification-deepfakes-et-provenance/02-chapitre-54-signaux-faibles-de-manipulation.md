---
title: Chapitre 54 — Signaux faibles de manipulation
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VIII — Vérification, deepfakes et provenance
  - index.md
---

## 54.1 La grammaire des défauts

Au-delà des outils techniques, l'analyste expérimenté apprend à reconnaître les **signaux faibles de manipulation** : petites incohérences que les générateurs IA produisent encore en 2026, faute de modèles parfaits.

Ces signaux ne sont pas définitifs (un faux haut de gamme peut être propre, une vraie photo peut avoir des artefacts), mais ils orientent.

## 54.2 Mains et doigts

**Le piège classique des modèles d'image IA**. Mains avec 4 ou 6 doigts, doigts fusionnés, articulations impossibles, longueurs incohérentes. Diffusion models progressent (DALL-E 3, Midjourney v6, Flux), mais les défauts subsistent fréquemment.

**Réflexe.** Toujours examiner les mains attentivement.

## 54.3 Yeux et regards

**Pupilles asymétriques.** StyleGAN classique laissait souvent un défaut (les deux pupilles légèrement différentes). Diffusion récente meilleur mais pas parfait.

**Reflets cornéens.** Dans la vraie vie, les deux yeux reflètent la même source de lumière. Sur faux, parfois reflets incohérents.

**Regard non-naturel.** Direction du regard légèrement vacillante.

## 54.4 Dents

**Dents fusionnées, asymétriques, nombre anormal.** Diffusion models ont du mal avec dents.

## 54.5 Oreilles

**Oreilles asymétriques** (toujours difficile pour modèles). Boucles d'oreille incohérentes.

## 54.6 Cheveux

**Contours flous.** Les cheveux se « fondent » dans l'arrière-plan de manière non naturelle.

**Mèches qui partent dans le vide.**

**Coupes irréalistes** (longueurs incohérentes des deux côtés).

## 54.7 Arrière-plan et contexte

**Arrière-plan flou anormalement.** Pas la bonne profondeur de champ.

**Objets dans l'arrière-plan déformés.** Bâtiments avec géométrie impossible, textes illisibles dans le décor.

**Cohérence physique.** Gravité, ombres, perspectives doivent être cohérents.

## 54.8 Ombres et reflets

**Ombres incohérentes.** Plusieurs ombres dans directions opposées. Ombre absente alors qu'attendue.

**Reflets incohérents.** Reflets de fenêtres / surfaces réfléchissantes ne correspondent pas.

## 54.9 Texte dans l'image

**Texte illisible ou défectueux.** Les diffusion models ont longtemps eu du mal avec le texte. Même en 2026, du texte fin (étiquettes, panneaux) reste souvent défectueux.

**Réflexe.** Zoomer sur tout texte visible. Lisible et correct = signal de vrai. Défectueux = signal de faux.

## 54.10 Compression et artefacts

**Compression locale anormale.** ELA peut révéler (Ch.47).

**Artefacts spécifiques par modèle.**

- StyleGAN : artefacts type damier dans les fonds.
- Diffusion : « over-smoothness » de certaines régions.

## 54.11 Signaux dans vidéos deepfake

**Boundary artifacts.** Le contour du visage swappé peut « tremble » ou ne pas parfaitement coller à la tête originale.

**Cohérence temporelle.** Les détails (mèches, lumière sur la peau) peuvent fluctuer d'une frame à l'autre.

**Synchronisation labiale.** Pas parfaite (lèvres et son décalés).

**Micro-mouvements physiologiques.** Intel FakeCatcher analyse rougissement, pulsations qui sont mal reproduites par face swap.

## 54.12 Signaux dans voix synthétiques

**Respiration absente** ou artificielle.

**Bruit de fond constant** (signature de génération).

**Intonations plates** sur certains mots.

**Pauses inhabituelles** ou absentes.

**Sons de bouche manquants** (clics, claquements de langue).

## 54.13 Signaux dans texte IA

**Tournures favorites des LLMs.**

- « Il est important de noter que… ».
- « Cependant, il est essentiel de… ».
- Listes à puces excessives.
- Conclusions auto-générées (« En conclusion, … »).
- Structure tripartite systématique.

**Manque de spécificité.** Détails génériques, dates floues, sources non vérifiables.

**Cohérence stylométrique.** Variations naturelles humaines absentes.

## 54.14 Méthode du « zoom et détail »

Pour tout contenu suspect :

1. **Vue d'ensemble** : impression globale.
2. **Zoom sur visages** : mains, yeux, dents, oreilles, cheveux.
3. **Zoom sur arrière-plan** : géométrie, textes.
4. **Zoom sur ombres et reflets**.
5. **Examen frame par frame** (vidéo).
6. **Outils techniques** (ELA, AI detection).

## 54.15 Limites

Ces signaux **deviennent obsolètes** à mesure que les modèles s'améliorent. Un déepfake de 2025 a moins de défauts qu'un de 2022. Un de 2027 en aura moins encore.

**Implication.** Ces signaux **orientent**, jamais ne prouvent. La cotation reste prudente.

-----
