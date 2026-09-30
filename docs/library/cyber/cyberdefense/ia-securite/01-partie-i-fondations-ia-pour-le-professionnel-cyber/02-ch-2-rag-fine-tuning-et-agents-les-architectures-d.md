---
title: 'Ch.2 — RAG, fine-tuning et agents : les architectures de déploiement'
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA & sécurité
up:
- - IA & sécurité
  - ../index.md
- - Partie I — Fondations IA pour le professionnel cyber
  - index.md
---

## 2.1 Retrieval Augmented Generation (RAG)

Le RAG est l’architecture dominante pour déployer un LLM en entreprise avec des données propriétaires. Son principe est simple : plutôt que de fine-tuner le modèle avec les données de l’entreprise (coûteux, lent, risqué en termes de mémorisation), on injecte les données pertinentes dans le contexte du modèle au moment de chaque requête.

Le flux complet d’un système RAG se décompose comme suit. L’utilisateur pose une question. Cette question est convertie en vecteur numérique (embedding) par un modèle d’embedding. Ce vecteur est comparé aux vecteurs des documents de la base documentaire, pré-calculés et stockés dans une base vectorielle. Les documents les plus similaires (les « chunks » les plus proches dans l’espace vectoriel) sont récupérés. Ces documents sont injectés dans le prompt, avec la question de l’utilisateur et les instructions système. Le LLM génère une réponse basée sur ces documents contextuels.

Ce mécanisme résout plusieurs problèmes : le modèle peut répondre sur des données qu’il n’a jamais vues à l’entraînement, les données restent à jour sans ré-entraînement, et on peut tracer quelles sources ont été utilisées pour chaque réponse (citabilité). Mais il introduit aussi des surfaces d’attaque spécifiques : les documents injectés dans le contexte sont un vecteur d’injection indirecte (un document malveillant dans la base peut détourner le comportement du modèle), la base vectorielle est un composant critique souvent mal sécurisé, et l’absence de RBAC vectoriel peut provoquer des fuites de données transversales (voir Ch.6 et Ch.13).

**L’embedding** est la transformation d’un texte en vecteur numérique de dimension fixe (typiquement 384 à 1536 dimensions) qui capture sa signification sémantique. Deux textes sémantiquement proches auront des vecteurs proches dans l’espace vectoriel. C’est le cœur du retrieval dans le RAG. Le choix du modèle d’embedding a un impact direct sur la qualité du retrieval — et donc sur la qualité (et la sécurité) des réponses. Un modèle d’embedding inadapté au domaine peut rater des documents pertinents ou en remonter d’inadéquats.

**La base vectorielle** (pgvector, Pinecone, Weaviate, Chroma, Qdrant, Milvus) stocke les embeddings et permet la recherche par similarité. En production, c’est un composant d’infrastructure critique souvent négligé dans le threat model. Par défaut, la plupart des bases vectorielles n’ont pas de contrôle d’accès granulaire : quiconque peut interroger la base peut potentiellement accéder à l’ensemble des documents indexés. C’est le problème fondamental du RBAC vectoriel détaillé au Ch.13.

**Le chunking** est le découpage des documents en fragments de taille appropriée pour l’indexation. Un chunk trop grand dilue la pertinence ; un chunk trop petit perd le contexte. Le chunking a aussi des implications de sécurité : un document contenant une injection cachée dans ses métadonnées ou dans un fragment de texte invisible peut être indexé et injecté dans des réponses ultérieures sans que l’utilisateur en soit conscient (voir Ch.5 sur l’injection indirecte).

## 2.2 Fine-tuning

Le fine-tuning consiste à reprendre un modèle pré-entraîné et à poursuivre son entraînement sur un jeu de données spécifique pour adapter son comportement. On l’utilise quand le RAG ne suffit pas : quand on veut modifier le style de réponse du modèle, l’adapter à un vocabulaire très spécialisé, ou lui enseigner un format de sortie structuré spécifique.

Le fine-tuning est plus risqué que le RAG du point de vue de la sécurité des données. Les données d’entraînement sont intégrées dans les poids du modèle — elles deviennent littéralement partie du modèle. Cela crée un risque de mémorisation : le modèle fine-tuné peut régurgiter des fragments de ses données d’entraînement, y compris des données personnelles ou confidentielles. Contrairement à un document dans une base RAG (qu’on peut supprimer), une donnée mémorisée dans les poids d’un modèle ne peut pas être chirurgicalement retirée — il faut ré-entraîner le modèle. Le « machine unlearning » (désapprentissage) fait l’objet de recherches actives mais n’est pas encore fiable en production.

Le fine-tuning a aussi un coût significatif (compute GPU, curation de données, validation) et introduit un risque de dégradation : un fine-tuning mal calibré peut détériorer les capacités générales du modèle ou affaiblir ses guardrails de sécurité. Des chercheurs ont démontré qu’un fine-tuning avec aussi peu que 100 exemples soigneusement choisis pouvait neutraliser l’alignement de sécurité d’un LLM.

Les variantes efficientes comme LoRA (Low-Rank Adaptation) et QLoRA réduisent le coût en ne modifiant qu’un petit nombre de paramètres, mais ne changent pas fondamentalement le profil de risque en termes de mémorisation et de sécurité.

## 2.3 Agents IA

Un agent IA est un système où le LLM ne se contente pas de générer du texte : il planifie, appelle des outils externes, observe les résultats, et itère. C’est le scénario à plus haut risque en sécurité IA, car l’agent passe de l’information à l’action.

L’architecture typique d’un agent comprend un LLM comme « cerveau » qui reçoit une tâche, décompose cette tâche en étapes, sélectionne les outils appropriés pour chaque étape, exécute les outils, observe les résultats, et décide s’il faut itérer ou répondre. Les outils peuvent être des API, des requêtes de base de données, des commandes système, des appels à d’autres services — tout ce qu’on peut interfacer.

Le risque fondamental est l’**excessive agency** : un agent manipulé (via prompt injection) ou mal configuré (privilèges excessifs) peut causer des dommages réels sur le SI. Un agent avec accès à l’Active Directory qui reçoit une instruction de reset de mot de passe via une injection cachée dans un ticket de support peut compromettre un compte admin. Un agent avec accès à un système de paiement peut initier des virements. La surface d’attaque n’est plus limitée à la génération de texte — elle inclut toutes les actions que l’agent peut effectuer.

Le **Model Context Protocol (MCP)**, standardisé par Anthropic et adopté de façon croissante par l’écosystème, formalise la connexion entre les LLMs et les outils/données externes. Chaque serveur MCP expose des « outils » (fonctions) et des « ressources » (données) que le LLM peut utiliser. Du point de vue sécurité, chaque serveur MCP est une surface d’attaque distincte avec ses propres permissions, ses propres vulnérabilités, et ses propres vecteurs d’injection. Un serveur MCP compromis ou malveillant peut injecter des données falsifiées dans le contexte du LLM, exfiltrer des informations via les paramètres d’appel, ou exécuter des actions non autorisées. L’ANSSI et des travaux de recherche (notamment Elastic Security Labs fin 2025) ont identifié les agents MCP comme un vecteur d’attaque émergent majeur.

## 2.4 Le serving : infrastructure d’inférence

Le serving désigne l’infrastructure qui expose le modèle via une API d’inférence. Les solutions courantes en auto-hébergement sont Ollama (simple, orienté développement et small-scale), vLLM (haute performance, batching optimisé, utilisé en production), et TGI (Text Generation Inference de Hugging Face). En cloud, les APIs des fournisseurs (OpenAI, Anthropic, Google, Mistral) fournissent le serving.

Le serving est un composant d’infrastructure classique — il hérite de toutes les vulnérabilités web habituelles (exposition réseau, authentification, TLS, rate limiting) auxquelles s’ajoutent des risques spécifiques : consommation GPU disproportionnée par des prompts complexes (DoS par compute), absence de rate limiting par utilisateur permettant l’extraction de données par interrogation massive, et logs de conversation contenant des données sensibles.

Par défaut, la plupart des serveurs d’inférence auto-hébergés n’ont pas d’authentification activée — Ollama écoute sur le port 11434 sans authentification, vLLM expose son API sans token par défaut. En production, un reverse proxy avec authentification (mTLS, API key, OAuth) est indispensable.

## 2.5 Les frameworks d’orchestration

LangChain et LlamaIndex sont les deux frameworks dominants pour construire des applications LLM (RAG, agents, pipelines). Ils simplifient considérablement le développement mais introduisent une couche de complexité et de dépendances. LangChain en particulier a connu plusieurs vulnérabilités critiques documentées (RCE, path traversal) en raison de son architecture permissive qui exécute du code arbitraire via certains modules. En production sécurisée, chaque module de framework utilisé doit être audité et mis à jour — l’approche « installer LangChain et utiliser tous les modules disponibles » est une exposition majeure (voir Ch.8 sur la supply chain).

> **🔵 Fil rouge — Épisode 2**
> Karim cartographie les architectures techniques des trois cas d’usage de NovaSanté :
> 
> - **Assistant RAG santé** : Mistral 7B (ou Llama 3.1 8B) servi via Ollama sur un serveur on-premise, pgvector pour la base vectorielle, FastAPI pour l’API backend, reverse proxy Nginx avec mTLS. Les documents sources proviennent du SharePoint interne (règlements, jurisprudence, procédures).
> - **Module fraude SIEM** : modèle XGBoost pour le scoring de sinistres (ML classique), enrichi par un LLM (via API Mistral on-premise) pour l’analyse textuelle des déclarations écrites suspectes. Intégration avec le SIEM (Splunk) via collecteur.
> - **Agent help desk** : LLM (Mistral) avec accès à deux outils via MCP — un serveur MCP Active Directory (reset password, lookup user) et un serveur MCP ServiceNow (créer ticket, mettre à jour ticket, consulter FAQ).
> 
> Karim note que chaque architecture a une surface d’attaque radicalement différente. L’assistant RAG expose la base documentaire santé. Le module fraude expose le pipeline de scoring. L’agent help desk expose l’AD et le système de ticketing. Trois threat models distincts à construire.

-----
