---
title: Chapitre 59 — Preuve OSINT dans un monde post-deepfake
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VIII — Vérification, deepfakes et provenance
  - index.md
---

## 59.1 La question juridique centrale

Avec la maturation des contenus synthétiques, la **valeur probante** des preuves numériques est remise en question. Une photo, une vidéo, un audio peuvent désormais être falsifiés au point de tromper un examen visuel.

**Conséquence judiciaire.** Les magistrats deviennent prudents face aux pièces numériques. Le standard de preuve évolue. Les experts judiciaires sont plus sollicités.

Pour l'analyste OSINT, cette évolution impose une adaptation :

- Documentation provenance renforcée.
- Cotation prudente.
- Recommandation d'expertise complémentaire pour pièces centrales.
- Vocabulaire calibré (« compatible avec », « éléments techniques convergents suggèrent », pas « prouve »).

## 59.2 Chain of custody renforcée

La chaîne de conservation (Ch.16) prend une importance accrue.

**Pour preuves susceptibles d'usage judiciaire en 2026.**

- Capture immédiate à la source.
- Hash cryptographique systématique.
- Horodatage qualifié (eIDAS, OpenTimestamps blockchain).
- Préservation des manifests C2PA quand présents.
- Documentation rigoureuse de la chaîne.
- Pas d'altération entre collecte et présentation.

## 59.3 Provenance comme standard émergent

**Tendance 2026.** Les magistrats demandent de plus en plus :

- Présence de manifest C2PA (preuve d'origine).
- Chaîne d'éditions documentée.
- Outils de création identifiés.

**Pour analyste OSINT.** Privilégier les sources qui produisent du C2PA. Documenter systématiquement la provenance dans le rapport.

## 59.4 Outils non déterministes

Les outils de détection IA (Hive, Sensity, Optic, etc.) sont **probabilistes**, pas déterministes. Leur sortie est un score, pas une certitude.

**Implication.**

- Ne jamais écrire « cette image EST une IA » dans un rapport.
- Écrire « cette image présente des signaux techniques (scores Hive 78 %, Sensity 67 %) suggérant qu'elle pourrait être générée par IA, niveau de confiance modéré ».

## 59.5 Rapport de vérification : structure

Pour une pièce centrale d'enquête, **rapport de vérification dédié** :

1. **Pièce examinée** : description, hash, source.
2. **Provenance** : C2PA, métadonnées, première occurrence.
3. **Authenticité technique** : EXIF, ELA, détection IA, signaux visuels.
4. **Contextualisation** : géolocalisation, chronolocation, cohérence.
5. **Sources de corroboration** : autres versions, témoignages.
6. **Conclusion cotée** : niveau de confiance, vocabulaire calibré.
7. **Limites** : ce qui n'a pas pu être vérifié.
8. **Recommandations** : expertise complémentaire si pièce centrale.

## 59.6 Prudence judiciaire 2026

**Pour les magistrats.**

- Les preuves numériques sont **utiles** mais **insuffisantes seules**.
- **Expertise judiciaire** recommandée pour pièces centrales.
- **Cross-référencement** avec preuves traditionnelles (témoignages, documents physiques).

**Pour les analystes OSINT.**

- Ne pas présenter votre travail comme « preuve définitive ».
- Présenter comme « éléments d'orientation justifiant approfondissement ».
- Préparer le terrain pour expertise judiciaire ultérieure.

## 59.7 Admissibilité variable selon juridictions

**France.** Pas de cadre spécifique deepfakes en 2026. Évaluation au cas par cas par magistrat, souvent avec expertise.

**UE.** AI Act impose étiquetage des contenus IA. Évolution jurisprudentielle en cours.

**US.** Cadre fédéral en débat. Variabilité étatique.

**UK.** Cadre en évolution. Voice cloning fraud criminalisée 2024.

## 59.8 Formulations recommandées

| À éviter | Préférer |
|---|---|
| « C'est un deepfake » | « Présente des signaux techniques compatibles avec un contenu synthétique » |
| « La photo est authentique » | « Les vérifications techniques et contextuelles n'ont pas identifié d'éléments suggérant manipulation » |
| « Prouvé par IA detection » | « Score Hive Moderation 78 % en faveur de l'hypothèse IA-generated » |
| « Source fiable » | « Source [X], cotation Admiralty A1 (média établi, fiabilité historique élevée) » |

## 59.9 Cas particulier : enregistrements audio

L'audio est particulièrement sensible :

- Voice cloning indiscernable en 2026.
- Pas de standard C2PA équivalent pour l'audio (en cours).
- Expertise audio judiciaire pas toujours équipée pour deepfakes.

**Pour rapport.** Toute pièce audio centrale → recommandation expertise.

## 59.10 Synthèse — preuve OSINT 2026

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
