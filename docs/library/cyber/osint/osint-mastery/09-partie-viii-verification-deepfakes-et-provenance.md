---
title: PARTIE VIII — Vérification, deepfakes et provenance
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
chapter: 9
chapters: 15
---

> **Ce que cette partie apprend.** Identifier et caractériser les contenus synthétiques (image, vidéo, audio, texte), détecter les signaux de manipulation, exploiter les standards de provenance (C2PA, Content Credentials), comprendre le watermarking (SynthID), conduire une méthodologie de vérification intégrée, articuler OSINT et fact-checking, gérer la preuve OSINT dans un monde post-deepfakes.
>
> **Ce qu'elle ne couvre pas.** L'IA générale pour OSINT (Partie IX), les cas pratiques (Partie XII).
>
> **Ce que vous saurez faire après cette partie.** Évaluer l'authenticité d'un contenu suspect, mobiliser les outils de détection 2026, vérifier la provenance via C2PA, formuler une conclusion d'authenticité calibrée, gérer l'admissibilité judiciaire de la preuve.

-----

### Chapitre 53 — Contenus synthétiques : image, vidéo, audio, texte

#### 53.1 Le tournant 2022-2026

Entre 2022 et 2026, la génération de contenus synthétiques est passée de **prototype de recherche** à **disponibilité grand public**. DALL-E 2 (avril 2022), Stable Diffusion (août 2022), Midjourney en montée, GPT-4 (mars 2023), Sora (vidéo, février 2024), ElevenLabs et HeyGen pour audio/vidéo cloning, Veo / Runway pour vidéo.

Conséquences pour l'OSINT :
- **Tout contenu** doit désormais être considéré comme **potentiellement synthétique** jusqu'à preuve du contraire.
- Le coût de production d'un faux convaincant est tombé à **quelques minutes et quelques euros**.
- La distinction « réel vs faux » est devenue le **premier réflexe** d'analyse.
- L'infrastructure de désinformation est passée à l'industrialisation.

#### 53.2 Typologie des contenus synthétiques

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

#### 53.3 Cas d'usage adverse

**Désinformation politique.** Faux discours, fausses déclarations attribuées à dirigeants.

**Fraude financière.** CEO fraud par voice cloning (« le PDG appelle son DAF pour autoriser un virement »), faux investissements.

**Harcèlement et atteintes.** Deepfakes pornographiques non consentis, fabrication de scènes compromettantes.

**Manipulation électorale.** Campagnes synthétiques à l'échelle.

**Atteinte à la réputation.** Le cas MIRAGE en est une illustration : vidéo deepfake du lanceur d'alerte tenant des propos compromettants fictifs.

#### 53.4 Cas d'usage légitimes (à connaître)

Pour contextualiser : tous les usages d'IA générative ne sont pas adverses.

**Production créative** (cinéma, design).

**Éducation** (visualisation, simulations).

**Accessibilité** (synthèse vocale pour malvoyants).

**Personnalisation** (avatars personnels).

L'analyste OSINT doit pouvoir distinguer **usage légitime** (souvent étiqueté, transparent) de **usage trompeur** (faux étiqueté comme vrai).

#### 53.5 Détection : limites de l'œil humain

L'**œil humain non-entraîné** ne distingue plus fiablement un deepfake moderne d'une vidéo réelle. Études 2024-2025 :
- Visages synthétiques (StyleGAN3, diffusion) : taux de détection humaine ~50 % (équivalent hasard).
- Voix clonées sophistiquées : taux de détection humaine ~60 %.
- Vidéos deepfake haut de gamme : taux de détection ~55-65 %.

**Implication.** La détection technique est devenue **obligatoire**.

#### 53.6 Outils de détection 2026

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

#### 53.7 Provenance comme contre-mesure (Ch.55 et Ch.56)

Face à l'inutilité progressive de la détection a posteriori, une approche complémentaire émerge : la **provenance**. Plutôt que de chercher à détecter ce qui a été fabriqué, **authentifier** ce qui est légitime.

**C2PA** (Content Credentials) attache des métadonnées signées à chaque média : qui l'a créé, avec quoi, quand, modifications successives. Voir Ch.55.

**Watermarking** (SynthID Google) insère des signatures invisibles dans contenus IA pour faciliter détection. Voir Ch.56.

#### 53.8 Cycle générer / détecter : course armement

Génération et détection évoluent en parallèle. Un détecteur efficace en 2024 peut être obsolète en 2025. Les générateurs sont entraînés à passer les détecteurs connus.

**Implication méthodologique.**
- Pas un seul outil de détection.
- Combiner plusieurs (Hive + Sensity + Optic).
- Cotation prudente, jamais « 100 % réel » ou « 100 % fake ».
- Veille continue sur outils.

#### 53.9 Faux profils animés par IA

Une variante émergente : **faux profils sociaux animés par IA**. Avatar IA + posts générés par LLM + interactions automatisées.

**Détection.**
- Photos générées par IA (Ch.30, Ch.35).
- Cadence inhumaine ou trop régulière.
- Sujets sans variation contextuelle réelle.
- Réseaux corrélés.

Voir Ch.35 sur CIB pour le développement.

#### 53.10 Synthèse — paysage 2026

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

### Chapitre 54 — Signaux faibles de manipulation

#### 54.1 La grammaire des défauts

Au-delà des outils techniques, l'analyste expérimenté apprend à reconnaître les **signaux faibles de manipulation** : petites incohérences que les générateurs IA produisent encore en 2026, faute de modèles parfaits.

Ces signaux ne sont pas définitifs (un faux haut de gamme peut être propre, une vraie photo peut avoir des artefacts), mais ils orientent.

#### 54.2 Mains et doigts

**Le piège classique des modèles d'image IA**. Mains avec 4 ou 6 doigts, doigts fusionnés, articulations impossibles, longueurs incohérentes. Diffusion models progressent (DALL-E 3, Midjourney v6, Flux), mais les défauts subsistent fréquemment.

**Réflexe.** Toujours examiner les mains attentivement.

#### 54.3 Yeux et regards

**Pupilles asymétriques.** StyleGAN classique laissait souvent un défaut (les deux pupilles légèrement différentes). Diffusion récente meilleur mais pas parfait.

**Reflets cornéens.** Dans la vraie vie, les deux yeux reflètent la même source de lumière. Sur faux, parfois reflets incohérents.

**Regard non-naturel.** Direction du regard légèrement vacillante.

#### 54.4 Dents

**Dents fusionnées, asymétriques, nombre anormal.** Diffusion models ont du mal avec dents.

#### 54.5 Oreilles

**Oreilles asymétriques** (toujours difficile pour modèles). Boucles d'oreille incohérentes.

#### 54.6 Cheveux

**Contours flous.** Les cheveux se « fondent » dans l'arrière-plan de manière non naturelle.

**Mèches qui partent dans le vide.**

**Coupes irréalistes** (longueurs incohérentes des deux côtés).

#### 54.7 Arrière-plan et contexte

**Arrière-plan flou anormalement.** Pas la bonne profondeur de champ.

**Objets dans l'arrière-plan déformés.** Bâtiments avec géométrie impossible, textes illisibles dans le décor.

**Cohérence physique.** Gravité, ombres, perspectives doivent être cohérents.

#### 54.8 Ombres et reflets

**Ombres incohérentes.** Plusieurs ombres dans directions opposées. Ombre absente alors qu'attendue.

**Reflets incohérents.** Reflets de fenêtres / surfaces réfléchissantes ne correspondent pas.

#### 54.9 Texte dans l'image

**Texte illisible ou défectueux.** Les diffusion models ont longtemps eu du mal avec le texte. Même en 2026, du texte fin (étiquettes, panneaux) reste souvent défectueux.

**Réflexe.** Zoomer sur tout texte visible. Lisible et correct = signal de vrai. Défectueux = signal de faux.

#### 54.10 Compression et artefacts

**Compression locale anormale.** ELA peut révéler (Ch.47).

**Artefacts spécifiques par modèle.**
- StyleGAN : artefacts type damier dans les fonds.
- Diffusion : « over-smoothness » de certaines régions.

#### 54.11 Signaux dans vidéos deepfake

**Boundary artifacts.** Le contour du visage swappé peut « tremble » ou ne pas parfaitement coller à la tête originale.

**Cohérence temporelle.** Les détails (mèches, lumière sur la peau) peuvent fluctuer d'une frame à l'autre.

**Synchronisation labiale.** Pas parfaite (lèvres et son décalés).

**Micro-mouvements physiologiques.** Intel FakeCatcher analyse rougissement, pulsations qui sont mal reproduites par face swap.

#### 54.12 Signaux dans voix synthétiques

**Respiration absente** ou artificielle.

**Bruit de fond constant** (signature de génération).

**Intonations plates** sur certains mots.

**Pauses inhabituelles** ou absentes.

**Sons de bouche manquants** (clics, claquements de langue).

#### 54.13 Signaux dans texte IA

**Tournures favorites des LLMs.**
- « Il est important de noter que… ».
- « Cependant, il est essentiel de… ».
- Listes à puces excessives.
- Conclusions auto-générées (« En conclusion, … »).
- Structure tripartite systématique.

**Manque de spécificité.** Détails génériques, dates floues, sources non vérifiables.

**Cohérence stylométrique.** Variations naturelles humaines absentes.

#### 54.14 Méthode du « zoom et détail »

Pour tout contenu suspect :

1. **Vue d'ensemble** : impression globale.
2. **Zoom sur visages** : mains, yeux, dents, oreilles, cheveux.
3. **Zoom sur arrière-plan** : géométrie, textes.
4. **Zoom sur ombres et reflets**.
5. **Examen frame par frame** (vidéo).
6. **Outils techniques** (ELA, AI detection).

#### 54.15 Limites

Ces signaux **deviennent obsolètes** à mesure que les modèles s'améliorent. Un déepfake de 2025 a moins de défauts qu'un de 2022. Un de 2027 en aura moins encore.

**Implication.** Ces signaux **orientent**, jamais ne prouvent. La cotation reste prudente.

-----

### Chapitre 55 — C2PA, Content Credentials et provenance

#### 55.1 Le tournant provenance

Face à l'impasse de la détection a posteriori, l'industrie a basculé vers la **provenance** : prouver l'**origine** et l'**historique** d'un contenu plutôt que tenter de détecter sa falsification.

**Coalition for Content Provenance and Authenticity (C2PA).** Coalition créée 2021 par Adobe, Microsoft, BBC, Intel, Truepic, autres. Standard ouvert.

**Implication.** En 2026, les principales plateformes et créateurs commencent à intégrer C2PA. **Standard émergent de référence** pour la preuve d'authenticité.

#### 55.2 Principe C2PA

À chaque création / modification d'un contenu, des **métadonnées signées cryptographiquement** sont attachées :

- **Créateur** (identité, certificat).
- **Outil de création** (appareil photo, logiciel).
- **Date et heure**.
- **Modifications successives** (chaîne d'éditions).
- **Signature** prouvant l'intégrité.

L'ensemble est appelé **manifest C2PA**. Embarqué dans le fichier ou stocké séparément (lien dans le fichier).

#### 55.3 Comment ça fonctionne

**Création.** Un appareil photo C2PA (Leica M11-P, Sony Alpha 1 II, etc.) ou un logiciel C2PA (Photoshop avec Content Credentials, etc.) crée un manifest signé.

**Édition.** Toute édition signée ajoute un nouveau manifest à la chaîne, prouvant ce qui a été modifié.

**Consultation.** Un viewer C2PA (extension navigateur, Verify Tool) affiche la chaîne de provenance.

#### 55.4 Content Credentials (Adobe)

**Content Credentials** est l'implémentation grand public d'Adobe basée sur C2PA. Intégrée dans Photoshop, Lightroom, Firefly.

**Indicateur visuel.** Petite icône « CR » sur les contenus avec Content Credentials.

**Verify Tool.** contentcredentials.org/verify permet de vérifier un fichier.

#### 55.5 Déploiement 2024-2026

**Plateformes adoptant C2PA.**
- **TikTok** : étiquetage automatique des contenus IA (2024).
- **Meta** (Facebook, Instagram) : étiquetage IA progressif.
- **YouTube** : labels « altered / synthetic content ».
- **OpenAI** : intègre C2PA dans DALL-E.
- **Adobe Firefly** : C2PA natif.
- **Leica, Sony, Nikon** : appareils photo C2PA-compatibles.

**Mais.** Adoption fragmentaire en 2026. Beaucoup de contenus ne portent pas encore C2PA. **Absence** de C2PA ne prouve pas faux.

#### 55.6 Outils de vérification C2PA

**contentcredentials.org/verify** : interface web officielle.

**C2PA viewer** : extension navigateur.

**Verify CLI** : outil terminal.

**Adobe Verify** : interface intégrée Adobe.

#### 55.7 Limites C2PA

**Adoption partielle.** Pas tous les créateurs / appareils / logiciels intègrent C2PA en 2026.

**Manipulation possible.** Un faux peut être créé sans C2PA, ou avec un C2PA falsifié si la clé privée du créateur est compromise.

**Stripping.** Les métadonnées peuvent être supprimées (capture d'écran, re-upload sans préservation).

**Identité du créateur.** Le manifest prouve l'identité de l'**outil** (signature). Pour prouver l'identité du **créateur humain**, lien à infrastructure de certificats plus complexe.

**Vie privée.** Manifest peut exposer information de l'auteur, contraire à anonymat parfois souhaité.

#### 55.8 Pratique OSINT 2026

**Toujours vérifier C2PA** sur contenu critique :
1. Inspecter présence de manifest.
2. Verify Tool si présent.
3. Examiner la chaîne (créateur, outil, édition).
4. Documenter résultat.

**Présence C2PA cohérent = forte présomption d'authenticité.**

**Absence C2PA ≠ preuve de faux.** Beaucoup de contenus légitimes (anciens, ou créateurs non équipés) n'ont pas C2PA.

#### 55.9 Méthodologie de vérification provenance

Pour un contenu critique :

1. **Inspecter C2PA** (presence + chain).
2. **Examiner métadonnées** (EXIF, IPTC, XMP).
3. **Rechercher source originelle** (Ch.46).
4. **Comparer avec C2PA de référence** si l'auteur est identifié.
5. **Synthèse cotée**.

#### 55.10 Au-delà C2PA : SynthID, watermarking (Ch.56)

Voir chapitre suivant pour l'autre branche : watermarks invisibles dans contenu IA pour faciliter détection.

#### 55.11 Implication judiciaire émergente

En 2026, les magistrats commencent à demander des **provenance reports** sur les pièces numériques sensibles. Pas obligation légale en France, mais tendance.

**Pour l'analyste OSINT.**
- Documenter systématiquement la provenance dans le rapport.
- Préserver les manifests C2PA quand ils existent.
- Recommander expertise complémentaire pour pièces centrales.

-----

### Chapitre 56 — Watermarking, SynthID et détection IA

#### 56.1 Le watermarking comme contre-mesure complémentaire

Le **watermarking** insère des signatures **invisibles** dans les contenus générés par IA. Ces signatures permettent de détecter ultérieurement qu'un contenu a été généré par un modèle spécifique.

C'est complémentaire à C2PA : C2PA authentifie le **légitime**, le watermarking flague le **synthétique**.

#### 56.2 SynthID (Google DeepMind)

**SynthID** (Google DeepMind, lancé 2023-2024). Watermark invisible pour images, audio, vidéo, texte généré par Google AI (Imagen, Veo, etc.).

**Principe.**
- **Image** : modification subtile des pixels invisible à l'œil mais détectable par modèle.
- **Texte** : biais dans le choix de tokens, signature détectable statistiquement.
- **Audio** : signature spectrale subtile.

**Détection.** Outil de détection SynthID (déployé en interne Google, accessibilité progressive externe).

#### 56.3 Autres watermarks

**Stable Signature** (Meta). Watermark intégré dans génération Stable Diffusion.

**OpenAI**. Plans pour watermarking de contenus DALL-E, Sora (en évolution 2025-2026).

**Anthropic, autres**. Approches diverses en développement.

#### 56.4 Limites du watermarking

**Robustesse face à modifications.** Crop, compression, re-encoding peuvent endommager le watermark.

**Effacement délibéré.** Outils anti-watermark en émergence.

**Couverture partielle.** Seulement modèles avec watermark intégré. Modèles ouverts (Stable Diffusion non-officiel, Llama avec fine-tunes) peuvent être utilisés pour éviter watermarks.

**Faux positifs / négatifs.** Pas 100 % fiable.

#### 56.5 Outils de détection IA 2026

**Pour images.**

**Hive Moderation.** Multi-modèles. Standard professionnel. Score par modèle source supposé.

**Optic AI or Not.** Interface simple, freemium.

**Sensity AI.** Standard institutionnel pour deepfakes.

**Intel FakeCatcher.** Analyse physiologique vidéos.

**Reality Defender.** Plateforme entreprise.

**AI or Not** : équivalent.

**Pour audio.**

**Resemble Detect.** Détection voix clonées.

**AI Voice Detector** (multi-outils).

**Pour texte.**

**GPTZero** : populaire mais faux positifs élevés.

**Originality.AI** : commercial.

**Copyleaks AI Detector.**

**Mais.** Tous très imparfaits pour le texte. À utiliser comme indice, pas conclusion.

**Pour vidéo.**

**Sensity AI** (deepfakes).

**Intel FakeCatcher**.

**Deepware Scanner**.

#### 56.6 Méthodologie de test multi-outils

**Principe.** Aucun outil n'est fiable seul. **Combiner 3+ outils** pour cotation pondérée.

**Exemple image.**
- Hive Moderation : 78 % AI-generated.
- Optic AI or Not : « AI ».
- Sensity : 67 % AI.
- → Faisceau cohérent, hypothèse « AI-generated » forte (cotation B2 ou meilleur).

**Si discordance.**
- Hive : 45 % AI.
- Optic : « real ».
- Sensity : 38 %.
- → Incertain. Cotation prudente. Recherche complémentaire.

#### 56.7 Calibration et faux positifs

**Faux positifs** (réel classé comme IA).
- Images très lissées, retouchées.
- Photos en condition lumière artificielle uniforme.
- Photos pro studio retouchées Photoshop classique.

**Faux négatifs** (IA classée comme réel).
- Modèles récents qui passent les détecteurs.
- IA générées puis dégradées intentionnellement.

**Pratique.** Ne jamais sur-interpréter un score. « Probable » ≠ « confirmé ».

#### 56.8 Détection contenus audio

L'audio est devenu particulièrement difficile.

**Voice cloning en 2026.**
- ElevenLabs : qualité indiscernable pour locuteur non-expert avec 30 secondes d'échantillon.
- HeyGen : avatars vidéo synchronisés audio.
- Tortoise TTS et open source : accessibles à tous.

**Outils détection.**
- Limited.
- Combinaison spectral analysis + IA detection.
- AICheck, Resemble Detect.

#### 56.9 Détection contenus texte

**État de l'art 2026 : très imparfait.**

**Pourquoi difficile.**
- LLMs s'améliorent (style indiscernable).
- Edition humaine d'IA-generated rend détection impossible.
- Différences inter-individuelles humaines élevées.

**Outils.**
- GPTZero, Originality, Copyleaks, etc.
- **Tous unreliable pour décision binaire**.

**Pratique.** Pour identifier texte IA, **contexte** (cohérence, sources citées, tournures typiques) est plus fiable que détecteurs automatiques.

#### 56.10 Synthèse — détection 2026

| Type | Outils | Fiabilité |
|---|---|---|
| Image StyleGAN | Hive, Optic | Bonne |
| Image diffusion | Hive, Sensity | Moyenne |
| Vidéo deepfake | Sensity, FakeCatcher | Variable |
| Vidéo synth full | Limité | Faible |
| Audio voix clonée | Resemble Detect | Difficile |
| Texte IA | GPTZero, Originality | Très faible |
| Combinaison multi-outils | Toujours préférer | Meilleure |

> **Principe.** En 2026, la détection IA est nécessaire mais insuffisante. Toujours combiner avec : provenance C2PA, recherche source originelle, contextualisation, signal faible visuel, cotation prudente.

-----

### Chapitre 57 — Méthodologie de vérification intégrée

#### 57.1 La vérification comme discipline

La **vérification** est la discipline qui transforme une information collectée en un fait coté. Elle a été codifiée par le journalisme d'investigation (Verification Handbook, Bellingcat), et l'OSINT moderne l'a adoptée.

Cinq dimensions de vérification : **source**, **contenu**, **contexte**, **temporalité**, **corroboration**.

#### 57.2 Vérification de la source

**Qui publie ?** Un compte vérifié, un média établi, un blog inconnu, un compte anonyme ?

**Fiabilité historique.** La source a-t-elle un track record de fiabilité ? Est-elle connue pour publier de la désinformation ?

**Motivations.** La source a-t-elle un intérêt à publier ? (Promotion, vengeance, idéologie, agent étranger.)

**Cotation Admiralty A-F** : voir Ch.84. La source est cotée systématiquement.

#### 57.3 Vérification du contenu

**Authenticité technique.**
- Métadonnées (EXIF, C2PA).
- Recherche inversée (Ch.46).
- Analyse technique (ELA, etc. — Ch.47).
- Détection IA (Ch.56).

**Cohérence interne.**
- Éléments visuels cohérents (Ch.54).
- Affirmations vérifiables.

**Faits invariants.**
- Géographie correcte ?
- Date plausible ?
- Personnes existantes ?

#### 57.4 Vérification du contexte

**Contexte de production.**
- Où, quand, par qui a-t-il été produit ?
- Conditions de production cohérentes avec ce qu'il montre ?

**Contexte de diffusion.**
- Quand et par qui diffusé ?
- Premier publié ou recyclage d'ancien ?
- Diffusion organique ou amplification coordonnée ?

**Contexte sémantique.**
- Cadrage tronqué qui change le sens ?
- Légende trompeuse ?

#### 57.5 Vérification temporelle

**Date de prise effective.**
- Métadonnées EXIF.
- Chronolocation (Ch.49).
- Cross-référence événements.

**Date de publication.**
- Première apparition (TinEye « first seen », Wayback).
- Diffusion ultérieure.

**Cohérence chronologique.**
- Présentée comme récente alors qu'ancienne ?
- Diffusion avant les événements supposés ?

#### 57.6 Corroboration

**Multiple sources indépendantes.**
- Deux sources de la même chaîne d'agence ne sont pas indépendantes.
- Différentes perspectives géographiques et politiques renforcent.

**Cross-check sur faits vérifiables.**
- Détails qui peuvent être confirmés ou infirmés (météo, événements concurrents, présence de personnes connues).

**Triangulation.**
- Témoignages multiples.
- Sources documentaires.
- Sources techniques.

#### 57.7 Workflow Verification Handbook

Le **Verification Handbook** (European Journalism Centre, multiples éditions) propose un workflow standard.

1. **Provenance** : d'où vient ?
2. **Source** : qui a posté ?
3. **Date** : quand ?
4. **Localisation** : où ?
5. **Motivation** : pourquoi ?

#### 57.8 Bellingcat methodology

**Méthodologie Bellingcat** : ouverte, documentée, transparente.

**Principes.**
- Sources publiques exclusivement.
- Captures avec horodatage et préservation.
- Documentation de chaque étape.
- Conclusions cotées avec vocabulaire calibré.
- Publication transparente du raisonnement.

#### 57.9 Information Laundromat et outils

**Information Laundromat** (Stanford Internet Observatory). Outil de cross-référencement de narratifs et opérations d'influence. Plus mature en 2025-2026.

**Hamilton 2.0** (German Marshall Fund). Monitoring opérations Russie/Chine.

**EU DisinfoLab.** Méthodologie référence pour CIB.

**Graphika** (sociale enterprise). Standards de référence sur CIB et analyse de réseaux.

#### 57.10 Fact-checking professionnel

Les organisations de fact-checking professionnel (AFP Factuel, FactCheck.org, Snopes, Les Décodeurs, Liberation CheckNews) utilisent OSINT massivement.

**Différence OSINT vs fact-checking.**
- Fact-checking : finalité publication, vérification ponctuelle d'une affirmation.
- OSINT : finalité investigation, vue d'ensemble structurée.

Mais méthodologies convergent largement.

#### 57.11 Cotation calibrée

À la fin de la vérification, **cotation explicite** :
- Source : A-F (Ch.84).
- Information : 1-6 (Ch.84).
- Conclusion : WEP (Ch.85).

**Exemple.**
- Image vérifiée comme authentique : source A1, contenu corroboré.
- Image vérifiée comme manipulée : source B (créateur opaque), contenu C (signaux techniques + recherche source).
- Conclusion : « la photographie est très probablement manipulée par face swap, niveau de confiance élevé ».

#### 57.12 Synthèse — méthodologie de vérification

| Dimension | Méthode |
|---|---|
| Source | Identification, fiabilité, motivation |
| Contenu | Authenticité technique + cohérence interne |
| Contexte | Production + diffusion + sémantique |
| Temporalité | Date prise + date publication + cohérence |
| Corroboration | Sources indépendantes + cross-check |
| Synthèse | Cotation Admiralty + WEP + formulation calibrée |

-----

### Chapitre 58 — Fact-checking et OSINT

#### 58.1 Convergence des disciplines

Le **fact-checking** est issu du journalisme. L'**OSINT** est issu du renseignement. En 2026, les deux **convergent** largement : méthodologie identique, outils partagés, communautés croisées.

**Convergence opérationnelle.** Un fact-checker AFP utilise reverse image search, géolocalisation, vérification de comptes — exactement comme un analyste OSINT.

**Différences résiduelles.**
- **Finalité** : fact-checking publie ; OSINT livre à commanditaire.
- **Périmètre** : fact-checking traite affirmations isolées ; OSINT couvre dossiers complets.
- **Cycle** : fact-checking continu ; OSINT par mission.

#### 58.2 Acteurs majeurs

**International.**
- **AFP Factuel** (France et international).
- **Reuters Fact Check**.
- **AP Fact Check**.
- **Snopes**.
- **FactCheck.org**.
- **PolitiFact**.

**France.**
- **Les Décodeurs** (Le Monde).
- **CheckNews** (Libération).
- **AFP Factuel**.
- **Désintox** (Libération).
- **20Minutes Fake Off**.

**Réseau international.** **IFCN** (International Fact-Checking Network, Poynter). Code de déontologie partagé.

#### 58.3 Méthodologie Verification Handbook

Le **Verification Handbook** (European Journalism Centre, première édition 2014, mise à jour régulière) est le manuel de référence du fact-checking moderne.

**Sommaire type.**
1. Réception de la rumeur ou affirmation.
2. Vérification de la source.
3. Vérification du contenu (technique, contextuelle).
4. Cross-référencement.
5. Publication transparente du raisonnement.
6. Suivi des éventuelles évolutions.

#### 58.4 EU DisinfoLab : méthodologie CIB

**EU DisinfoLab** a structuré la méthodologie d'investigation des opérations d'influence (Coordinated Inauthentic Behavior).

**Cas de référence : Indian Chronicles** (2019-2020). 750+ faux médias dans 116 pays orchestrés depuis un seul opérateur indien. Investigation modèle.

#### 58.5 Information Laundromat (Stanford)

**Information Laundromat** propose des outils cross-référencement narratifs et identification campagnes coordonnées.

#### 58.6 Bellingcat Online Investigation Toolkit

**Bellingcat Online Investigation Toolkit** (bellingcat.com/resources). Catalogue ouvert d'outils, méthodologies, formations. Référence du domaine.

#### 58.7 Convergence sur opérations d'influence

Les opérations Russie (Doppelgänger, IRA), Chine (Spamouflage), Iran sont documentées de manière convergente par :
- Fact-checkers (AFP, Reuters).
- OSINT investigateurs (Bellingcat, EU DisinfoLab).
- Agences spécialisées (VIGINUM, Graphika).
- Académiques (Stanford SIO).

La discipline tend à un standard commun.

#### 58.8 Publication responsable

**Principes adoptés par fact-checkers et OSINT investigateurs.**

**Transparence méthodologique.** Le raisonnement est publié, pas seulement la conclusion.

**Cotation explicite.** Niveau de confiance, sources, limites.

**Mise à jour si nouvelles évidences.**

**Pas de doxxing.** Anonymisation des comptes individuels sauf cas exceptionnels.

**Pas d'amplification involontaire.** Citer le narratif sans le légitimer.

#### 58.9 Collaboration entre disciplines

En 2026, beaucoup d'investigations majeures sont **collaboratives**.

**Exemple.** Documentation de Doppelgänger : combinaison de :
- VIGINUM (France) pour caractérisation technique.
- EU DisinfoLab pour cross-pays.
- Bellingcat pour cas d'usage.
- AFP Factuel pour pédagogie public.
- Stanford SIO pour analyse académique.

#### 58.10 Synthèse

| Discipline | Force | Limite |
|---|---|---|
| Fact-checking | Publication, cas isolés | Périmètre limité |
| OSINT | Dossier complet, profondeur | Diffusion limitée |
| Convergence | Méthodologie partagée, écosystème croisé | — |

-----

### Chapitre 59 — Preuve OSINT dans un monde post-deepfake

#### 59.1 La question juridique centrale

Avec la maturation des contenus synthétiques, la **valeur probante** des preuves numériques est remise en question. Une photo, une vidéo, un audio peuvent désormais être falsifiés au point de tromper un examen visuel.

**Conséquence judiciaire.** Les magistrats deviennent prudents face aux pièces numériques. Le standard de preuve évolue. Les experts judiciaires sont plus sollicités.

Pour l'analyste OSINT, cette évolution impose une adaptation :
- Documentation provenance renforcée.
- Cotation prudente.
- Recommandation d'expertise complémentaire pour pièces centrales.
- Vocabulaire calibré (« compatible avec », « éléments techniques convergents suggèrent », pas « prouve »).

#### 59.2 Chain of custody renforcée

La chaîne de conservation (Ch.16) prend une importance accrue.

**Pour preuves susceptibles d'usage judiciaire en 2026.**
- Capture immédiate à la source.
- Hash cryptographique systématique.
- Horodatage qualifié (eIDAS, OpenTimestamps blockchain).
- Préservation des manifests C2PA quand présents.
- Documentation rigoureuse de la chaîne.
- Pas d'altération entre collecte et présentation.

#### 59.3 Provenance comme standard émergent

**Tendance 2026.** Les magistrats demandent de plus en plus :
- Présence de manifest C2PA (preuve d'origine).
- Chaîne d'éditions documentée.
- Outils de création identifiés.

**Pour analyste OSINT.** Privilégier les sources qui produisent du C2PA. Documenter systématiquement la provenance dans le rapport.

#### 59.4 Outils non déterministes

Les outils de détection IA (Hive, Sensity, Optic, etc.) sont **probabilistes**, pas déterministes. Leur sortie est un score, pas une certitude.

**Implication.**
- Ne jamais écrire « cette image EST une IA » dans un rapport.
- Écrire « cette image présente des signaux techniques (scores Hive 78 %, Sensity 67 %) suggérant qu'elle pourrait être générée par IA, niveau de confiance modéré ».

#### 59.5 Rapport de vérification : structure

Pour une pièce centrale d'enquête, **rapport de vérification dédié** :

1. **Pièce examinée** : description, hash, source.
2. **Provenance** : C2PA, métadonnées, première occurrence.
3. **Authenticité technique** : EXIF, ELA, détection IA, signaux visuels.
4. **Contextualisation** : géolocalisation, chronolocation, cohérence.
5. **Sources de corroboration** : autres versions, témoignages.
6. **Conclusion cotée** : niveau de confiance, vocabulaire calibré.
7. **Limites** : ce qui n'a pas pu être vérifié.
8. **Recommandations** : expertise complémentaire si pièce centrale.

#### 59.6 Prudence judiciaire 2026

**Pour les magistrats.**
- Les preuves numériques sont **utiles** mais **insuffisantes seules**.
- **Expertise judiciaire** recommandée pour pièces centrales.
- **Cross-référencement** avec preuves traditionnelles (témoignages, documents physiques).

**Pour les analystes OSINT.**
- Ne pas présenter votre travail comme « preuve définitive ».
- Présenter comme « éléments d'orientation justifiant approfondissement ».
- Préparer le terrain pour expertise judiciaire ultérieure.

#### 59.7 Admissibilité variable selon juridictions

**France.** Pas de cadre spécifique deepfakes en 2026. Évaluation au cas par cas par magistrat, souvent avec expertise.

**UE.** AI Act impose étiquetage des contenus IA. Évolution jurisprudentielle en cours.

**US.** Cadre fédéral en débat. Variabilité étatique.

**UK.** Cadre en évolution. Voice cloning fraud criminalisée 2024.

#### 59.8 Formulations recommandées

| À éviter | Préférer |
|---|---|
| « C'est un deepfake » | « Présente des signaux techniques compatibles avec un contenu synthétique » |
| « La photo est authentique » | « Les vérifications techniques et contextuelles n'ont pas identifié d'éléments suggérant manipulation » |
| « Prouvé par IA detection » | « Score Hive Moderation 78 % en faveur de l'hypothèse IA-generated » |
| « Source fiable » | « Source [X], cotation Admiralty A1 (média établi, fiabilité historique élevée) » |

#### 59.9 Cas particulier : enregistrements audio

L'audio est particulièrement sensible :
- Voice cloning indiscernable en 2026.
- Pas de standard C2PA équivalent pour l'audio (en cours).
- Expertise audio judiciaire pas toujours équipée pour deepfakes.

**Pour rapport.** Toute pièce audio centrale → recommandation expertise.

#### 59.10 Synthèse — preuve OSINT 2026

| Type de preuve | Solidité 2026 |
|---|---|
| Document officiel avec C2PA | Forte |
| Photo avec C2PA + métadonnées | Forte |
| Photo sans C2PA, source identifiée | Moyenne |
| Photo orpheline | Faible |
| Vidéo avec C2PA + provenance | Moyenne-forte |
| Vidéo sans provenance | Faible |
| Audio sans provenance | Très faible |
| Texte | Difficilement preuve à elle seule |

> **Principe 2026.** L'OSINT produit du renseignement orienteur de haute qualité. Pour la preuve judiciaire au sens fort, l'expertise complémentaire reste nécessaire. La rigueur méthodologique OSINT facilite cette expertise — elle ne s'y substitue pas.

> **MIRAGE — Épisode 16 : Deepfake et contenu synthétique**
>
> L'analyste examine la vidéo deepfake d'Antoine Berthier (mentionnée dans le mandat MIRAGE).
>
> **Description.** Vidéo MP4 de 47 secondes, qualité moyenne (720p), publiée sur YouTube le 3 mars 2026 par un compte créé le 1er mars 2026 (durée de vie : 4 heures avant suppression par YouTube après signalement). Préservée par yt-dlp avant suppression. Hash SHA-256 enregistré.
>
> **Contenu.** Visage identifié comme Berthier, propos prononcés : « j'ai trafiqué les comptes pour servir mes intérêts personnels, je voulais nuire à mon employeur... ». Background : décor de bureau générique.
>
> **Authenticité technique.**
>
> **Provenance.** Aucun manifest C2PA. Métadonnées EXIF vidéo strippées (upload YouTube).
>
> **Détection IA.**
> - Sensity AI : score 89 % « very likely deepfake ».
> - Intel FakeCatcher : analyse physiologique → 92 % « non-physiological », alerte forte.
> - Deepware Scanner : « deepfake detected ».
> - Score combiné : très forte présomption de deepfake.
>
> **Signaux visuels (lecture frame par frame).**
> - Boundary artifacts visibles autour du visage de Berthier (légère oscillation des contours).
> - Synchronisation labiale imparfaite (lèvres en retard de 1-2 frames).
> - Texture peau anormalement lisse sur certaines zones.
>
> **Source audio.** Voix très ressemblante à celle de Berthier (cross-comparée avec une vidéo de présentation interne TechnoVert 2024, capturée avant licenciement). Signaux de voice cloning :
> - Resemble Detect : « 76 % AI-generated voice ».
> - Légères pauses inhabituelles.
> - Absence de respiration naturelle.
>
> **Cohérence contextuelle.**
> - Berthier a publiquement (interview presse régionale, novembre 2025) démenti tout détournement, attribuant les soupçons à une vengeance après son signalement interne.
> - La vidéo prétend Berthier admettant ce qu'il a publiquement nié.
> - Timing : publication 4 mois après le licenciement, en pleine phase de procédure prud'homale Berthier vs TechnoVert.
>
> **Conclusion (formulation calibrée).** « Les analyses techniques (multi-outils de détection deepfake, analyse physiologique, signaux visuels frame par frame, détection voice cloning) et la cohérence contextuelle (incompatibilité avec déclarations publiques antérieures de Berthier, timing suspect) **convergent fortement vers l'hypothèse que cette vidéo est un deepfake audio-vidéo composite**, fabriqué pour discréditer Antoine Berthier. **Niveau de confiance : élevé.** **Recommandation : expertise judiciaire complémentaire** pour validation indépendante avant usage en procédure pénale. »
>
> **Cotation.** A1 sur les analyses techniques (sources multiples convergentes). B1 sur la conclusion globale. A1 sur l'incompatibilité contextuelle (déclarations publiques documentées).
>
> Cette pièce devient l'un des éléments majeurs du rapport MIRAGE : démonstration formelle de l'usage de l'IA générative dans la campagne de diffamation. Combinée aux trois fausses photographies (MIRAGE 11) et au cluster de désinformation (MIRAGE 9, 17), elle dessine une campagne sophistiquée et délibérée.

-----
