---
title: Ch.12 — Contrôles techniques
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie III — Sécuriser le déploiement
  - index.md
---

IAM, réseau, chiffrement, DLP et sécurité applicative de la stack IA

## 12.1 IAM et RBAC granulaire

Le contrôle d’accès d’un système IA doit être granulaire et multi-couche. Au niveau de l’API du modèle : authentification par API key ou OAuth, différenciation admin / analyste / utilisateur, quotas par rôle. Au niveau de la base vectorielle : RBAC vectoriel (voir Ch.13). Au niveau des logs : accès restreint aux logs de conversation (ils contiennent des données sensibles). Au niveau des outils de l’agent : chaque outil a ses propres credentials avec des permissions scoped (voir Ch.9).

L’erreur classique est le contrôle d’accès unique au niveau de l’application front-end sans contrôle au niveau des composants backend (base vectorielle, API de serving, serveurs MCP). Un attaquant qui bypasse le front-end a alors accès direct à tous les composants.

## 12.2 Segmentation réseau

Le serveur d’inférence doit être dans un VLAN dédié avec des flux contrôlés par allow-list. La base vectorielle doit être dans un segment isolé, accessible uniquement par le backend applicatif. Les serveurs MCP doivent être dans des segments correspondant à la criticité de leurs fonctions (le serveur MCP AD dans le segment admin, le serveur MCP ServiceNow dans le segment applicatif). Les flux entre les composants doivent être chiffrés (TLS 1.3 minimum) et authentifiés (mTLS en production).

## 12.3 Chiffrement

TLS 1.3 pour tous les flux en transit (utilisateur → frontend → backend → modèle → base vectorielle). Chiffrement at rest pour les données stockées : base vectorielle, logs de conversation, documents sources, modèles stockés. KMS (Key Management Service) pour la gestion centralisée des clés. Chiffrement des sauvegardes des modèles et des bases vectorielles.

## 12.4 DLP adapté à l’IA

Le proxy DLP IA se positionne entre l’utilisateur et le modèle (et entre le modèle et les outils de l’agent). Il filtre en entrée (détection de PII, secrets, données classifiées dans les prompts) et en sortie (détection de fuites dans les réponses). Les solutions existantes incluent les modules IA des DLP traditionnels (Symantec, Digital Guardian, Microsoft Purview avec les politiques IA), les solutions spécialisées (Nightfall, Protect AI), et les guardrails open source (LLM Guard, NeMo Guardrails).

## 12.5 Sécurité applicative classique de la stack IA

Un système IA reste une application exposée. Il hérite de toutes les vulnérabilités applicatives classiques — et les additionne aux risques spécifiques de l’IA.

**AuthN/AuthZ.** L’API de serving doit avoir une authentification robuste (pas de Ollama sans auth en production). Le frontend doit valider les sessions. Les endpoints d’administration doivent être protégés par un accès renforcé.

**API security.** Rate limiting, validation des inputs, protection contre les requêtes volumétriques, headers de sécurité, CORS correctement configuré.

**SSRF via connecteurs.** Un agent ou un RAG qui récupère du contenu depuis des URLs (pages web, APIs externes) est potentiellement vulnérable au SSRF — l’attaquant peut rediriger les requêtes vers des services internes. Le filtrage des URLs et l’utilisation d’un proxy sortant dédié sont essentiels.

**Désérialisation.** Au-delà du pickle pour les modèles (voir Ch.8), les frameworks ML utilisent la sérialisation pour les configurations, les pipelines, et les résultats intermédiaires. Chaque point de désérialisation est un vecteur potentiel de RCE.

**Vulnérabilités dans les frameworks d’orchestration.** LangChain, LlamaIndex, et les frameworks similaires ont des historiques de CVE significatifs. Les modules qui exécutent du code arbitraire (Python REPL, shell), qui accèdent au système de fichiers, ou qui font des requêtes réseau sont des surfaces d’attaque directes. En production, n’activer que les modules strictement nécessaires et les maintenir à jour.

Une application IA n’annule pas les vulnérabilités applicatives classiques ; elle les additionne.

-----
