---
title: Ch.24 — Cas complet
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie VI — Cas de synthèse
  - index.md
---

gestion du shadow AI et déploiement d’une alternative interne

## 24.1 Diagnostic

L’audit shadow AI révèle que 85 % des gestionnaires utilisent ChatGPT pour résumer des dossiers (données de santé incluses), trois managers utilisent Claude pour des notes de synthèse, le juridique utilise Perplexity avec des noms d’assurés. L’analyse de risque montre une violation potentielle du RGPD (transfert hors UE sans DPA, pas de base légale pour le sous-traitant), une violation potentielle de l’obligation HDS (données de santé hébergées hors infrastructure certifiée), et un risque réputationnel (si une fuite est médiatisée).

## 24.2 Stratégie en cinq niveaux

**Détection** (semaines 1-2) : analyse des logs proxy, enquête anonyme auprès des collaborateurs. **Alternative interne** (semaines 3-12) : accélération du déploiement de l’assistant RAG comme outil officiel couvrant les cas d’usage identifiés. **Politique** (semaine 4) : publication de la politique d’usage IA avec les interdictions explicites (jamais de données de santé, jamais de données nominatives, jamais de documents confidentiels dans un LLM cloud non contractualisé). **Contrôle technique** (semaine 6) : blocage des APIs ChatGPT, Claude, et Perplexity sur le proxy pour les postes des gestionnaires et du juridique (accès maintenu pour la DSI à des fins de veille technique). **Sensibilisation** (continue) : sessions de formation sur les risques spécifiques, démonstration de l’alternative interne, communication managériale.

## 24.3 Résultats

À 6 mois, le shadow AI passe de 85 % à 15 % (usage résiduel principalement sur des tâches sans données sensibles — rédaction de mails, recherche d’information générique). La satisfaction des gestionnaires sur l’assistant RAG interne est de 78 % (principal reproche : temps de réponse plus lent que ChatGPT, qualité de réponse parfois inférieure sur les questions complexes — compensé par la pertinence sur les données NovaSanté et l’absence de risque de fuite).

-----
