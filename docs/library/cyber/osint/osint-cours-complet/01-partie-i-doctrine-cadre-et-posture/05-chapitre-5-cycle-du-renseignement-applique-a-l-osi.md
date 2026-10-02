---
title: Chapitre 5 — Cycle du renseignement appliqué à l'OSINT
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE I — Doctrine, cadre et posture
  - index.md
---

## 5.1 Origine et utilité du cycle

Le **cycle du renseignement** est le cadre méthodologique qui structure toute production de renseignement, quelle que soit la discipline (HUMINT, SIGINT, OSINT, all-source). Il a été formalisé par les services occidentaux dans les années 1940-1950 et reste la référence doctrinale, malgré ses limites (le « cycle » n'est en réalité jamais strictement séquentiel).

Son utilité, appliquée à l'OSINT, est triple : il **prévient les deux pièges classiques** (collecte qui ne mène à rien faute d'orientation, rapport bâclé faute d'analyse), il **structure la communication** avec le commanditaire (chaque étape est lisible), et il **rend l'enquête reproductible** (un confrère peut reprendre à n'importe quelle étape).

## 5.2 Phase 1 — Orientation

L'**orientation** est la phase la plus importante et la plus négligée. C'est ici que se forme la **question de renseignement**.

**Activités.**

- Réception et compréhension de la demande du commanditaire.
- Reformulation en questions de renseignement (intelligence requirements).
- Identification des sélecteurs initiaux.
- Définition du périmètre et des limites.
- Évaluation des risques juridiques et éthiques.
- Validation du mandat.
- Fixation des critères d'arrêt (quand l'enquête est-elle suffisante ?).

**Erreurs classiques.**

- Lancer la collecte sans questions claires.
- Accepter un mandat trop large (« faire le tour de tout ce qu'on sait sur X »).
- Ne pas reformuler la demande avec le commanditaire.
- Ne pas définir le périmètre, ce qui mène à la dérive d'enquête.
- Sous-estimer les risques juridiques.

L'orientation prend typiquement **5-15 % du temps total** d'une enquête. C'est peu en temps, beaucoup en impact. Une orientation bâclée invalide tout ce qui suit.

## 5.3 Phase 2 — Collecte

La **collecte** est la mobilisation des sources pour répondre aux questions.

**Activités.**

- Identification des sources prioritaires.
- Mise en place de l'OPSEC.
- Exécution de la collecte (recherches, captures, requêtes API).
- Documentation systématique dans le journal d'enquête.
- Préservation (Hunchly, SingleFile, hashing).
- Premier tri de pertinence.

**Erreurs classiques.**

- Collecter au hasard, sans hiérarchie de sources.
- Ne pas documenter chaque action.
- Capturer trop ou trop peu.
- Oublier d'archiver les sources fragiles (réseaux sociaux, articles éphémères).
- Sous-estimer les restrictions plateformes en 2026 (Ch.24).

La collecte prend **30-50 % du temps**. C'est la phase la plus chronophage. Une collecte structurée alimente une analyse fluide ; une collecte chaotique paralyse tout ce qui suit.

## 5.4 Phase 3 — Traitement

Le **traitement** est la mise en forme des données collectées pour les rendre exploitables.

**Activités.**

- Nettoyage (suppression des doublons, des éléments hors périmètre).
- Organisation (vault Obsidian structuré, taxonomie d'entités).
- Indexation (référencement des éléments, codes de suivi).
- Déduplication (fusion d'entités, résolution d'identités — Ch.82).
- Conversion (PDF, OCR, transcription audio/vidéo si nécessaire).
- Traduction (LLMs comme assistants — Ch.61).
- Préparation du matériau pour l'analyse.

**Erreurs classiques.**

- Sauter le traitement (« je vais analyser au fil de l'eau »).
- Conserver tout en vrac sans structuration.
- Confondre traitement et analyse.

Le traitement prend **10-20 % du temps**. Il est invisible dans le livrable final mais indispensable.

## 5.5 Phase 4 — Analyse

L'**analyse** est la transformation du matériau collecté et traité en renseignement.

**Activités.**

- Corrélation des éléments (graphes, timelines, matrices source/information).
- Formulation d'hypothèses concurrentes.
- Application de l'**ACH** (Analysis of Competing Hypotheses — Ch.79).
- Test contre les évidences (quelles hypothèses sont compatibles ? Lesquelles sont infirmées ?).
- Cotation de chaque fait (Admiralty — Ch.84).
- Évaluation des biais cognitifs (Ch.80).
- Raisonnement adversaire (Ch.81).
- Formulation des conclusions en niveau de confiance (WEP — Ch.85).

**Erreurs classiques.**

- Sauter à l'hypothèse confortable sans test.
- Confondre indices et faits (Ch.4).
- Confirmer ce qu'on cherche (biais de confirmation).
- Surinterpréter (chercher une preuve dans un indice).
- Mal coter (cotation par confort, pas par méthode).

L'analyse prend **20-30 % du temps**. C'est la phase qui fait la valeur du métier. Une analyse rigoureuse distingue le renseignement du bruit.

## 5.6 Phase 5 — Diffusion

La **diffusion** est la production et la transmission du livrable au commanditaire.

**Activités.**

- Rédaction du rapport (note courte ou rapport complet).
- Production des annexes (graphes, timelines, fiches entités).
- Revue par pair (si possible).
- Choix du canal de transmission (TLP, sécurité).
- Transmission effective.
- Briefing oral si demandé.

**Erreurs classiques.**

- Rédiger à chaud, dans l'enthousiasme de la découverte.
- Ne pas faire revoir le rapport.
- Excéder le vocabulaire calibré.
- Diffuser par canal non sécurisé.
- Oublier la classification TLP.

La diffusion prend **10-20 % du temps**. C'est la phase la plus visible — c'est le seul moment où le commanditaire voit votre travail.

## 5.7 Phase 6 — Feedback

Le **feedback** est le retour du commanditaire et l'itération de l'enquête.

**Activités.**

- Réception du retour du commanditaire (questions, demandes de précision, nouvelles pistes).
- Identification des questions ouvertes.
- Planification éventuelle d'une seconde itération.
- Veille post-rapport (Ch.92).
- Capitalisation interne (leçons apprises, modèles réutilisables).

**Erreurs classiques.**

- Considérer l'enquête terminée à la diffusion.
- Ne pas solliciter de retour structuré.
- Ne pas mettre en place la veille post-rapport.
- Ne pas capitaliser pour les enquêtes futures.

## 5.8 Le cycle n'est pas linéaire

En pratique, les phases **se chevauchent et se rétroactivent**.

- L'orientation est souvent affinée pendant la collecte (on découvre que la question initiale était mal posée).
- La collecte se poursuit pendant l'analyse (on identifie de nouveaux sélecteurs à explorer).
- L'analyse peut renvoyer à de la collecte complémentaire.
- La diffusion peut générer un feedback qui relance un nouveau cycle.

Le cycle est donc un **cycle en spirale** : on monte en compréhension à chaque itération. Une enquête complexe peut comporter 3-5 itérations du cycle. La discipline du cycle prévient le chaos, mais elle n'impose pas une rigidité contre-productive.

## 5.9 Adaptation aux contextes urgents

Dans certains contextes (urgence opérationnelle, crise, breaking news), le cycle est **compressé**. Une note flash en 4 heures suit toujours les six phases, mais chacune ne dure que 30-45 minutes. Le risque est de sacrifier l'analyse au profit de la vitesse. La discipline reste : même en urgence, on cote, on trace, on documente les limites.

## 5.10 Le cycle et l'IA

L'**arrivée de l'IA en 2025-2026** transforme partiellement le cycle.

- **Collecte automatisée** : agents qui collectent en continu (Ch.67).
- **Traitement assisté** : LLMs pour extraction d'entités, traduction, classification.
- **Analyse augmentée** : LLMs pour synthèse de corpus, génération d'hypothèses (à valider).
- **Diffusion accélérée** : aide à la rédaction.

Mais le cœur du cycle — formulation de la question, jugement, cotation, formulation calibrée, décision éthique — **reste humain**. L'analyste devient orchestrateur d'agents, pas exécutant manuel. C'est ce que la Partie IX du cours développe.

-----
