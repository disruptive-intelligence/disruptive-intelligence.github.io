---
title: 'Chapitre 53 — Contenus synthétiques : image, vidéo, audio, texte'
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VIII — Vérification, deepfakes et provenance
  - index.md
---

## 53.1 Le tournant 2022-2026

Entre 2022 et 2026, la génération de contenus synthétiques est passée de **prototype de recherche** à **disponibilité grand public**. DALL-E 2 (avril 2022), Stable Diffusion (août 2022), Midjourney en montée, GPT-4 (mars 2023), Sora (vidéo, février 2024), ElevenLabs et HeyGen pour audio/vidéo cloning, Veo / Runway pour vidéo.

Conséquences pour l'OSINT :

- **Tout contenu** doit désormais être considéré comme **potentiellement synthétique** jusqu'à preuve du contraire.
- Le coût de production d'un faux convaincant est tombé à **quelques minutes et quelques euros**.
- La distinction « réel vs faux » est devenue le **premier réflexe** d'analyse.
- L'infrastructure de désinformation est passée à l'industrialisation.

## 53.2 Typologie des contenus synthétiques

**Images.**

- **StyleGAN** classique (ThisPersonDoesNotExist 2018+). Visages photoréalistes mais reconnaissables par défauts caractéristiques.
- **Diffusion models** (Stable Diffusion, DALL-E, Midjourney, Flux). Qualité photoréaliste atteinte 2023-2024.
- **Édition / inpainting** : modification ciblée (face swap, ajout/retrait d'éléments).

**Vidéos.**

- **Face swap** : remplacer un visage dans une vidéo (DeepFaceLab, FaceFusion, dernières évolutions IA).
- **Reenactment** : faire dire / faire faire des choses à un visage existant (Wav2Lip, et nouvelles générations).
- **Synthèse complète** : créer une vidéo entièrement (Sora, Veo, Runway Gen-3, Pika).
- **Avatars vidéo** : HeyGen, Synthesia créent des présentateurs synthétiques convaincants.

**Audio.**

- **Voice cloning** : reproduire une voix à partir de courts samples (ElevenLabs, Resemble AI, Tortoise TTS). En 2026, 10-30 secondes d'échantillon suffisent.
- **Synthèse vocale** : créer une voix originale (TTS classique évolué).

**Texte.**

- **LLMs** (ChatGPT, Claude, Gemini, Llama, Mistral, et innombrables) : texte ressemblant à humain, fluide, contextualisé.
- Génération de **faux articles, faux tweets, faux posts** en quantité industrielle.
- Combinaison avec personae IA (faux profils animés par LLM).

**Documents.**

- Faux passeports, fausses factures, faux contrats — combinaison IA visuelle + IA texte.
- En 2026, certains faux résistent à l'inspection humaine non-experte.

## 53.3 Cas d'usage adverse

**Désinformation politique.** Faux discours, fausses déclarations attribuées à dirigeants.

**Fraude financière.** CEO fraud par voice cloning (« le PDG appelle son DAF pour autoriser un virement »), faux investissements.

**Harcèlement et atteintes.** Deepfakes pornographiques non consentis, fabrication de scènes compromettantes.

**Manipulation électorale.** Campagnes synthétiques à l'échelle.

**Atteinte à la réputation.** Le cas MIRAGE en est une illustration : vidéo deepfake du lanceur d'alerte tenant des propos compromettants fictifs.

## 53.4 Cas d'usage légitimes (à connaître)

Pour contextualiser : tous les usages d'IA générative ne sont pas adverses.

**Production créative** (cinéma, design).

**Éducation** (visualisation, simulations).

**Accessibilité** (synthèse vocale pour malvoyants).

**Personnalisation** (avatars personnels).

L'analyste OSINT doit pouvoir distinguer **usage légitime** (souvent étiqueté, transparent) de **usage trompeur** (faux étiqueté comme vrai).

## 53.5 Détection : limites de l'œil humain

L'**œil humain non-entraîné** ne distingue plus fiablement un deepfake moderne d'une vidéo réelle. Études 2024-2025 :

- Visages synthétiques (StyleGAN3, diffusion) : taux de détection humaine ~50 % (équivalent hasard).
- Voix clonées sophistiquées : taux de détection humaine ~60 %.
- Vidéos deepfake haut de gamme : taux de détection ~55-65 %.

**Implication.** La détection technique est devenue **obligatoire**.

## 53.6 Outils de détection 2026

Voir Ch.56 pour le détail. Liste indicative :

**Images.**

- **Hive Moderation** : multi-modèles, score AI-generated.
- **Optic AI or Not** : interface simple.
- **AI or Not** (similaire).
- **Sensity AI** : détection deepfakes.

**Vidéos.**

- **Sensity AI** : ground truth video.
- **Intel FakeCatcher** : analyse physiologique (rougeurs, micro-mouvements).
- **Deepware Scanner** : grand public.
- **Reality Defender** : standard institutionnel.

**Audio.**

- **AI Voice Detector** (variantes diverses).
- **Resemble Detect**.

**Texte.**

- **GPTZero**, **Originality.AI**, **Copyleaks** : détection texte IA. **Tous très imparfaits** en 2026 (faux positifs, faux négatifs). À utiliser comme indice, pas comme conclusion.

## 53.7 Provenance comme contre-mesure (Ch.55 et Ch.56)

Face à l'inutilité progressive de la détection a posteriori, une approche complémentaire émerge : la **provenance**. Plutôt que de chercher à détecter ce qui a été fabriqué, **authentifier** ce qui est légitime.

**C2PA** (Content Credentials) attache des métadonnées signées à chaque média : qui l'a créé, avec quoi, quand, modifications successives. Voir Ch.55.

**Watermarking** (SynthID Google) insère des signatures invisibles dans contenus IA pour faciliter détection. Voir Ch.56.

## 53.8 Cycle générer / détecter : course armement

Génération et détection évoluent en parallèle. Un détecteur efficace en 2024 peut être obsolète en 2025. Les générateurs sont entraînés à passer les détecteurs connus.

**Implication méthodologique.**

- Pas un seul outil de détection.
- Combiner plusieurs (Hive + Sensity + Optic).
- Cotation prudente, jamais « 100 % réel » ou « 100 % fake ».
- Veille continue sur outils.

## 53.9 Faux profils animés par IA

Une variante émergente : **faux profils sociaux animés par IA**. Avatar IA + posts générés par LLM + interactions automatisées.

**Détection.**

- Photos générées par IA (Ch.30, Ch.35).
- Cadence inhumaine ou trop régulière.
- Sujets sans variation contextuelle réelle.
- Réseaux corrélés.

Voir Ch.35 sur CIB pour le développement.

## 53.10 Synthèse — paysage 2026

| Type contenu | État de la détection 2026 |
|---|---|
| Images StyleGAN classiques | Bonne détection (Hive, Optic) |
| Images diffusion (SD, Midjourney récent) | Moyenne, en course |
| Vidéos face swap | Variable selon qualité |
| Vidéos full synth (Sora, Veo) | Mauvaise, en émergence |
| Voix clonées sophistiquées | Difficile |
| Texte IA fluent | Très mauvaise (faux positifs) |
| Documents IA | Mauvaise, ad hoc |

> **Principe 2026.** La présomption d'authenticité ne se justifie plus par défaut. Tout contenu critique d'enquête doit être interrogé sur son authenticité — non par paranoïa, mais par méthode.

-----
