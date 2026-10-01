---
title: Annexe A — Glossaire IA & SSI (60+ termes)
source: Cyber/09 IA & sécurité/IA et sécurité.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Annexes
  - index.md
---

|Terme                            |Définition                                                                                                                                                                           |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Adversarial example**          |Entrée subtilement modifiée pour tromper un modèle ML tout en restant visuellement ou sémantiquement identique pour un humain                                                        |
|**Agent IA**                     |Système où un LLM planifie, appelle des outils externes, observe les résultats et itère — passage de l’information à l’action                                                        |
|**AI Act**                       |Règlement (UE) 2024/1689 sur l’intelligence artificielle — approche par les risques avec quatre niveaux (inacceptable, élevé, limité, minimal)                                       |
|**AIPD**                         |Analyse d’Impact relative à la Protection des Données — obligatoire RGPD pour les traitements à risque élevé                                                                         |
|**Alignement**                   |Processus visant à s’assurer qu’un modèle IA se comporte conformément aux valeurs et intentions humaines                                                                             |
|**Allow-list**                   |Liste explicite des actions autorisées pour un agent — tout ce qui n’est pas listé est interdit                                                                                      |
|**Automation bias**              |Tendance des utilisateurs à suivre les recommandations d’un système automatisé sans vérification critique                                                                            |
|**Backdoor poisoning**           |Insertion d’un déclencheur caché dans les données d’entraînement qui active un comportement malveillant en production                                                                |
|**Base vectorielle**             |Base de données spécialisée dans le stockage et la recherche par similarité de vecteurs d’embedding (pgvector, Pinecone, Weaviate, Chroma, Qdrant)                                   |
|**Chunking**                     |Découpage de documents en fragments de taille appropriée pour l’indexation dans un RAG                                                                                               |
|**Circuit breaker / kill switch**|Mécanisme automatique de désactivation d’un agent IA quand des conditions anormales sont détectées                                                                                   |
|**Concept drift**                |Évolution de la relation entre features et cible au fil du temps — dégrade la performance du modèle                                                                                  |
|**Data drift**                   |Évolution de la distribution des données d’entrée au fil du temps                                                                                                                    |
|**Data poisoning**               |Corruption des données d’entraînement pour altérer le comportement d’un modèle                                                                                                       |
|**Deepfake**                     |Contenu synthétique (image, vidéo, audio) généré par IA imitant l’apparence ou la voix d’une personne réelle                                                                         |
|**Deep Learning**                |Sous-ensemble du ML utilisant des réseaux de neurones à multiples couches                                                                                                            |
|**Differential privacy**         |Technique mathématique ajoutant du bruit calibré pendant l’entraînement pour protéger la vie privée des individus dans le dataset                                                    |
|**DLP (Data Loss Prevention)**   |Ensemble de technologies et processus de prévention des fuites de données — adapté à l’IA pour filtrer prompts et réponses                                                           |
|**DPA**                          |Data Processing Agreement — contrat obligatoire RGPD entre responsable de traitement et sous-traitant (article 28)                                                                   |
|**Embedding**                    |Représentation vectorielle numérique d’un texte capturant sa signification sémantique                                                                                                |
|**Evasion attack**               |Attaque adversariale au moment de l’inférence visant à tromper le classifieur                                                                                                        |
|**Excessive agency**             |Risque qu’un agent IA exécute des actions non souhaitées en raison de manipulation ou de mauvaise configuration                                                                      |
|**Feature store**                |Composant centralisé stockant les features pré-calculées pour les modèles ML                                                                                                         |
|**Few-shot learning**            |Capacité d’un LLM à adapter son comportement à partir d’un petit nombre d’exemples fournis dans le contexte                                                                          |
|**Fine-tuning**                  |Poursuite de l’entraînement d’un modèle pré-entraîné sur un jeu de données spécifique                                                                                                |
|**Garak**                        |Outil open source (NVIDIA) de scan automatisé de vulnérabilités LLM                                                                                                                  |
|**GPAI**                         |General Purpose AI — modèles de fondation à usage général au sens de l’AI Act                                                                                                        |
|**Guardrails**                   |Mécanismes de sécurité filtrant les entrées et sorties d’un LLM                                                                                                                      |
|**Hallucination**                |Production par un modèle IA de contenu factuellement faux formulé avec assurance                                                                                                     |
|**HDS**                          |Hébergement de Données de Santé — certification française obligatoire pour l’hébergement de données de santé                                                                         |
|**Human-in-the-loop**            |Exigence de validation humaine avant l’exécution d’actions critiques par un agent IA                                                                                                 |
|**Injection directe**            |Prompt injection où l’utilisateur lui-même tente de contourner les guardrails (jailbreak)                                                                                            |
|**Injection indirecte**          |Prompt injection via des données de contexte (documents RAG, emails, pages web) contenant des instructions cachées                                                                   |
|**Jailbreak**                    |Technique de prompt injection visant à contourner les garde-fous de sécurité d’un LLM                                                                                                |
|**Kill switch**                  |Voir circuit breaker                                                                                                                                                                 |
|**LLM**                          |Large Language Model — grand modèle de langage basé sur l’architecture Transformer                                                                                                   |
|**LoRA**                         |Low-Rank Adaptation — technique de fine-tuning efficiente ne modifiant qu’un petit nombre de paramètres                                                                              |
|**Machine unlearning**           |Technique (en recherche) permettant de supprimer l’influence de données spécifiques des poids d’un modèle                                                                            |
|**Many-shot jailbreak**          |Technique d’injection fournissant de nombreux exemples pour pousser le modèle hors de ses guardrails                                                                                 |
|**MCP**                          |Model Context Protocol — standard de connexion entre LLMs et outils/données externes                                                                                                 |
|**Membership inference**         |Attaque déterminant si un échantillon spécifique faisait partie des données d’entraînement                                                                                           |
|**Memorization**                 |Phénomène où un modèle retient et peut régurgiter des fragments de ses données d’entraînement                                                                                        |
|**MITRE ATLAS**                  |Adversarial Threat Landscape for AI Systems — cartographie des TTPs contre les systèmes IA                                                                                           |
|**Model collapse**               |Dégradation de performance d’un modèle entraîné sur des données elles-mêmes générées par IA                                                                                          |
|**Model extraction**             |Reconstruction d’un modèle fonctionnellement équivalent par interrogation répétée                                                                                                    |
|**Model inversion**              |Tentative de reconstruction des données d’entraînement à partir du modèle                                                                                                            |
|**NIST AI RMF**                  |AI Risk Management Framework du NIST — cadre de gestion des risques IA                                                                                                               |
|**Ollama**                       |Solution de serving de modèles LLM en local, orientée simplicité                                                                                                                     |
|**OWASP Top 10 for LLM**         |Liste des 10 risques de sécurité les plus critiques pour les applications LLM (Version 2025, publiée nov. 2024)                                                                      |
|**Model Theft**                  |Vol ou extraction d’un modèle propriétaire par interrogation répétée, distillation adversariale ou accès non autorisé (couvert par OWASP LLM10 Unbounded Consumption en version 2025)|
|**Pickle**                       |Format de sérialisation Python permettant l’exécution de code arbitraire au chargement — dangereux pour les modèles                                                                  |
|**Prompt injection**             |Technique d’attaque exploitant l’absence de séparation entre instructions et données dans un LLM                                                                                     |
|**Promptfoo**                    |Framework d’évaluation systématique des prompts et des réponses                                                                                                                      |
|**RAG**                          |Retrieval Augmented Generation — architecture injectant des données contextuelles dans le prompt du LLM                                                                              |
|**RAG poisoning**                |Insertion de documents malveillants dans la base documentaire d’un RAG                                                                                                               |
|**RBAC vectoriel**               |Contrôle d’accès par rôle appliqué à la base vectorielle d’un RAG — filtre les résultats par permissions                                                                             |
|**Red teaming IA**               |Tests adversariaux systématiques d’un système IA                                                                                                                                     |
|**RLHF**                         |Reinforcement Learning from Human Feedback — alignement d’un LLM via des évaluations humaines                                                                                        |
|**SafeTensors**                  |Format de sérialisation de modèles ne permettant pas l’exécution de code — standard de sécurité                                                                                      |
|**Sanitization**                 |Nettoyage des documents avant indexation pour détecter les injections cachées                                                                                                        |
|**Shadow AI**                    |Utilisation non autorisée d’outils IA par les collaborateurs                                                                                                                         |
|**Slopsquatting**                |Création de packages malveillants portant des noms hallucinés par des LLMs dans leur suggestions de code                                                                             |
|**Temperature**                  |Paramètre contrôlant l’aléatoire de la génération d’un LLM                                                                                                                           |
|**Token**                        |Unité de base du traitement textuel d’un LLM (fragment de texte, typiquement 3-4 caractères)                                                                                         |
|**Transformer**                  |Architecture de réseau de neurones dominante pour les LLMs, basée sur le mécanisme d’attention                                                                                       |
|**UEBA**                         |User and Entity Behavior Analytics — détection d’anomalies comportementales                                                                                                          |
|**vLLM**                         |Solution de serving de modèles LLM haute performance, optimisée pour la production                                                                                                   |

-----
