---
title: Chapitre 34 — IA générative, LLM, deepfakes et privacy
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 7 — OPSEC humaine, opérationnelle et continuité
  - index.md
---

## 34.1 Quatre vagues qui changent le paysage

L’IA générative 2023-2026 a modifié quatre vecteurs :

- **Création de contenu falsifié** plausible (texte, image, vidéo, voix) à coût marginal nul.
- **Capacité d’attaque automatisée** (phishing personnalisé à grande échelle, génération de pretext crédibles).
- **Aspiration de données** : modèles entraînés sur du contenu massif incluant des données personnelles.
- **Intégration dans les appareils** (Apple Intelligence, Gemini sur Android, Copilot dans Windows) : nouvelles surfaces d’exposition.

## 34.2 LLM cloud : ce que ton fournisseur voit

Quand tu utilises ChatGPT, Claude, Gemini, Mistral Le Chat depuis le navigateur ou l’app, tu envoies tes prompts à leurs serveurs. Conséquences :

- **Stockage** : par défaut, les conversations sont stockées et utilisables pour amélioration des modèles.
- **Logs** : disponibles à l’opérateur, accessibles sur réquisition légale.
- **Pas d’E2EE** : du contenu en clair entre toi et le fournisseur.
- **Sensitivity** : un prompt révèle ton sujet d’intérêt, ton vocabulaire, ton style, ton contexte professionnel.

**Comportements à éviter** : envoyer à un LLM cloud des informations personnelles identifiantes sensibles (numéros, noms de sources, contenus internes confidentiels, dossiers médicaux).

## 34.3 Modes « privacy » des fournisseurs

Plusieurs fournisseurs proposent des options :

- **ChatGPT « Temporary Chat »** : pas de stockage long terme. À activer manuellement.
- **Claude.ai** : politique de non-entraînement sur conversations consumer par défaut depuis 2024-2025.
- **API mode** vs **interface chat** : l’API offre généralement de meilleures garanties contractuelles (pas d’entraînement, rétention configurable). Pour usage pro sérieux.
- **Plans entreprise** : politiques de rétention contrôlées contractuellement.

Lire la politique du fournisseur à jour est indispensable, les choses bougent vite.

## 34.4 LLM locaux : Ollama, LM Studio, llama.cpp

L’alternative privacy : faire tourner un LLM **sur ta machine**. Le prompt ne quitte jamais ton appareil.

- **Ollama** : runner simple pour modèles ouverts (Llama, Mistral, Qwen, etc.). Installation en quelques commandes, modèles téléchargés localement.
- **LM Studio** : interface graphique, profil grand public.
- **llama.cpp** : moteur d’inférence efficace, base de plusieurs solutions.

**Performance** : sur Mac M-series ou laptop avec GPU récent, modèles 7-13B donnent qualité utilisable. Modèles 70B exigent matériel sérieux mais possibles. Qualité légèrement inférieure aux frontières (GPT-4, Claude 4, Gemini 2.5) mais en progression rapide.

**Pour qui** : profils qui traitent des informations confidentielles et veulent rester maîtres. Excellent pour analyse de documents sensibles, brainstorming privé, drafting de notes confidentielles.

## 34.5 Connecteurs IA (MCP, plug-ins, agents)

L’année 2024-2025 a vu se généraliser les **connecteurs** entre LLM et données utilisateur : MCP (Model Context Protocol), plug-ins, agents qui lisent ton calendrier, tes emails, tes documents.

**Risques** :

- **Élargissement de surface** : l’agent peut accéder à tes données plus largement que tu ne le réalises.
- **Prompt injection** : un document piégé peut faire faire des actions à un agent (exfiltration, modifications, envoi de messages). Vecteur d’attaque actif documenté en 2024-2025.
- **Persistance** : agent qui s’authentifie une fois et tourne en arrière-plan.
- **Données exposées au fournisseur LLM** : tout ce que l’agent lit, le LLM l’a vu.

**Pratique défensive** :

- Privilégier connecteurs avec accès *en lecture* uniquement quand possible.
- Limiter la portée (scope minimal sur OAuth).
- Audit régulier des autorisations.
- Pour profil sensible : pas de connecteur sur comptes critiques.

## 34.6 Apple Intelligence, Microsoft Copilot, Gemini sur Android

Intégrations IA system-level. Spécificités :

- **Apple Intelligence** : revendique « Private Cloud Compute » avec architecture attestable. Pour requêtes locales (Siri reformulation, etc.) : on-device. Pour requêtes complexes : Apple Cloud Compute en E2EE attestable. Garanties techniques sérieuses mais auditabilité limitée pour utilisateur externe.
- **Microsoft Copilot dans Windows et Recall** : Recall est annoncée comme une fonctionnalité réservée aux **Copilot+ PCs** (matériel récent intégrant un NPU dédié), **opt-in** au niveau de l’utilisateur (la fonctionnalité n’est pas activée par défaut depuis le re-lancement), avec snapshots stockés localement et index présentés par Microsoft comme chiffrés et liés au Secure Enclave de la machine. La fonctionnalité avait été initialement déployée sans ces garanties en 2024, ce qui avait suscité une vague de critiques de chercheurs en sécurité ; Microsoft a suspendu puis re-lancé Recall fin 2024 avec ces protections additionnelles. Les critiques de fond persistent : capture régulière de l’écran indexée par IA crée par construction une base d’informations sensibles, dont la sécurité repose entièrement sur la robustesse de la TEE locale et l’absence d’exploitation de la machine. Pour profils sensibles : laisser Recall désactivé.
- **Gemini sur Android** : intégration profonde aux services Google, transmission cloud par défaut.

**Pour profils sensibles** : désactiver autant que possible les fonctionnalités IA système qui transmettent du contenu hors appareil.

## 34.7 Aspiration de données par entraînement

Les modèles LLM ont été entraînés sur des corpus massifs incluant du contenu public (web crawl) et parfois privé (litiges en cours sur sources illégales). Conséquence : il existe des cas documentés où des modèles **regurgitent** verbatim du contenu d’entraînement, y compris des données personnelles.

**Mitigation côté utilisateur** :

- Limiter ta présence publique (Ch 5-8) limite ce qui peut être ingéré.
- Demandes d’opt-out auprès des fournisseurs (parfois disponibles, parfois théoriques).
- Surveiller les outputs sur ton propre nom dans les LLM publics.

## 34.8 Robots.txt, ai.txt, droit à l’opposition au scraping

Pour qui produit du contenu en ligne et veut limiter son ingestion :

- **robots.txt** : standard historique, respecté par Google et Bing, ignoré par certains crawlers d’entraînement.
- **ai.txt** : standard émergent 2024-2025, plus spécifique pour exclure entraînement IA.
- **Méta-tags HTML** : `<meta name="robots" content="noai, noimageai">` (efficacité variable).
- **Cloudflare AI bot blocking** : depuis 2024, option dans Cloudflare pour bloquer les bots IA identifiés.
- **Cadre légal** : le RGPD (art. 21) permet l’opposition au traitement, applicable au scraping pour entraînement selon une lecture progressivement reconnue. La directive sur le droit d’auteur de 2019 (art. 4) prévoit le « opt-out » pour le data mining commercial.

## 34.9 Deepfakes vidéo : état 2025-2026

La qualité des deepfakes vidéo a passé en 2024-2025 le seuil de plausibilité pour observateur non averti. Outils : Sora (OpenAI), Veo (Google), Gen-3 (Runway), HeyGen, D-ID, plus une cohorte open source.

Cas documentés :

- Faux Zelensky annonçant capitulation (2022, peu convaincant à l’époque).
- Faux Macron en mai 2024 (deepfake politique en période électorale).
- Sextorsion par deepfake en croissance, particulièrement contre femmes (cf. Sensity, Cyber Civil Rights Initiative).
- Faux call vidéo CFO Arup, Hong Kong, début 2024 : virement de 25 M$ après deepfake convaincant en réunion vidéo.

## 34.10 Deepfakes audio : voice cloning

Encore plus mature que la vidéo. Outils : ElevenLabs, Resemble AI, plus solutions open source. **Trois secondes** d’enregistrement de voix suffisent pour cloner avec qualité plausible.

Cas en croissance :

- Faux appels « ton enfant a un accident, envoie de l’argent » utilisant la voix clonée.
- Faux PDG demandant virement urgent.
- Phishing vocal personnalisé.

## 34.11 Biométrie vocale et auth téléphonique

Implication : la sécurité par « reconnaissance de la voix » au téléphone (utilisée par certaines banques, services administratifs, parfois Apple ID via Siri) est devenue **structurellement faible**. Les institutions qui en dépendent migrent ou doivent.

**Pour toi** : si une institution te propose auth vocale comme seule MFA, refuser. Demander alternative.

## 34.12 Procédures anti-deepfake en réunion

Pour réunions sensibles à distance :

- **Codes hors bande** : convenir d’un mot de passe convenu en personne, à prononcer en début de visio pour authentifier.
- **Vidéo conférencière** : un deepfake en temps réel est aujourd’hui difficile à maintenir sous gestures complexes ; demander à la personne de poser une main de manière inattendue, tourner la tête vivement, montrer une pièce d’identité — peut révéler artefacts.
- **Rappel sur canal vérifié** : si doute, raccrocher et rappeler sur le numéro connu.

## 34.13 Détection de deepfake : état de l’art

Outils en croissance, fiabilité partielle :

- **Sensity AI, Reality Defender, Truepic** : commerciaux, focalisés enterprise.
- **Académiques** : suite d’outils universitaires (FaceForensics++, DFDC).
- **Limites** : course à l’armement permanente entre génération et détection. Pas de garantie.

**Stratégie défensive** : ne pas dépendre uniquement de détection ; combiner avec vérification hors bande systématique.

## 34.14 Watermarking : C2PA, SynthID

- **C2PA (Coalition for Content Provenance and Authenticity)** : standard de provenance cryptographique d’images, vidéos, documents. Adobe, Microsoft, Sony, BBC. Embarque dans le fichier l’historique de capture/modifications, signé. Pour authentifier l’origine d’un contenu.
- **SynthID** (Google DeepMind) : watermark invisible dans contenus générés par IA Google. Détectable par outils dédiés.
- **Limites** : volontaire, supprimable, partiellement déployé. Utile mais pas suffisant.

## 34.15 IA dans la pile attaquant

Du côté offensif :

- **Phishing personnalisé** : un LLM rédige des emails sur mesure à partir d’OSINT préalable. Qualité linguistique, registre, vocabulaire — quasi parfaits.
- **Vocal phishing** : voice cloning + LLM = conversation crédible.
- **Reconnaissance** : LLM analyse vastes corpus de données fuitées pour identifier patterns exploitables.
- **Génération de pretext** : LLM produit scénarios de social engineering convaincants.

**Conséquence** : la qualité moyenne des attaques augmente. Les indicateurs traditionnels (fautes, formulation maladroite) sont moins fiables. Le filtrage se déplace vers le **comportement** et le **canal** plutôt que le contenu.

## 34.16 IA dans la pile défenseur

Du côté défensif :

- **Détection d’anomalies** : LLM dans EDR pour analyse comportementale.
- **Triage automatique** : assistance pour analystes SOC.
- **Génération de leurres** (honeypots intelligents).
- **Aide à la rédaction de procédures, formation, sensibilisation**.

L’asymétrie en 2026 : l’IA aide les deux camps à l’avantage de l’attaquant *à court terme* (l’attaque scale plus facilement que la défense), mais à l’avantage du défenseur à moyen terme si déploiement systématique.

## 34.17 Cadre éthique : usage de l’IA dans son propre travail

Ce cours postule un usage IA éthique : compréhension, rédaction, analyse, formation. Pas de génération de contenu trompeur, pas d’impersonation, pas d’utilisation pour harceler. Le droit (loi française de 2024 sur deepfakes, AI Act UE) sanctionne désormais explicitement plusieurs usages malveillants.

## 34.18 *Fil rouge* — Léa face à un deepfake de sa source

Trois mois après sa première rencontre avec Karim, Léa reçoit un appel vidéo Signal. Voix et image de Karim, ton paniqué : « Léa, j’ai besoin que tu rendes les documents, ils savent, c’est dangereux pour ma famille. » Léa ressent le malaise — le ton n’est pas tout à fait celui de Karim. Elle applique le protocole pré-convenu : « Karim, peux-tu me redire le proverbe qu’on a échangé la première fois ? ». Silence côté appel, puis raccrochage. Léa contacte ensuite Karim sur leur canal SimpleX par texte : Karim répond, c’est bien lui, et il n’a pas appelé. Tentative de deepfake confirmée. Bascule en alerte, audit complet des canaux, vérification que la stack tient toujours.

-----
