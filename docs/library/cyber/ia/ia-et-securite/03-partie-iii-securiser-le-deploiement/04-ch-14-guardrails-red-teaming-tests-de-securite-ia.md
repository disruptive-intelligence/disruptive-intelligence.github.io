---
title: Ch.14 — Guardrails, red teaming, tests de sécurité IA et gates de validation
source: Cyber/09 IA & sécurité/IA et sécurité.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie III — Sécuriser le déploiement
  - index.md
---

## 14.1 Les guardrails

Les guardrails sont les contrôles de sécurité appliqués aux entrées et sorties du LLM. Ils se décomposent en deux catégories.

**Guardrails en entrée.** Détection de patterns de prompt injection (classificateurs entraînés sur des corpus de jailbreaks connus), filtrage de contenu inapproprié (requêtes offensantes, hors périmètre), classification des requêtes (routage vers différents modèles ou comportements selon le type de requête), et validation de format (rejet des requêtes mal formées ou anormalement longues).

**Guardrails en sortie.** Vérification de cohérence (la réponse est-elle cohérente avec les sources RAG ? — détection d’hallucination par comparaison), filtrage de contenu (rejet des réponses contenant du contenu offensant, biaisé, ou hors périmètre), DLP (détection de PII, secrets, données classifiées dans la réponse), et validation de format (la réponse respecte-t-elle le format attendu ?).

## 14.1b Improper Output Handling (OWASP LLM05)

Le traitement non sécurisé des sorties du LLM mérite une attention particulière car c’est un risque classé LLM05 par l’OWASP (Version 2025). Le problème ne réside pas dans la qualité de la réponse mais dans ce qu’on en fait en aval. Quand la sortie du modèle est réinjectée dans un système — interprétée comme commande shell, collée dans une requête SQL, exécutée comme code, insérée dans un template HTML, ou utilisée pour construire un appel d’API — ce n’est plus une « mauvaise réponse », c’est une surface d’exploitation downstream.

Les scénarios concrets incluent un agent qui construit une requête SQL à partir de la réponse du LLM (injection SQL de second ordre), une interface qui affiche la réponse en HTML sans échappement (XSS via le LLM), un pipeline qui exécute du code Python suggéré par le modèle (RCE), et un système qui utilise la sortie du LLM comme paramètre d’un appel API sans validation (SSRF, injection de commande). La défense est systématique : toute sortie du LLM qui sera traitée par un autre système doit être validée, échappée et sanitizée exactement comme un input utilisateur non fiable dans une application web classique. Le LLM est un utilisateur non fiable — ses sorties doivent être traitées comme telles.

Les outils de guardrails incluent NeMo Guardrails (NVIDIA — framework de rails en entrée et sortie), LLM Guard (open source — classification et filtrage), Guardrails AI (validation structurée des sorties), et les solutions intégrées des fournisseurs cloud.

## 14.2 Red teaming IA

Le red teaming IA est une discipline spécifique qui teste la résistance d’un système IA aux attaques adversariales. La méthodologie comprend la définition du scope (quels composants tester — modèle, RAG, agent, API, infrastructure), les objectifs (jailbreak, exfiltration, injection, excessive agency, hallucination), les techniques (catalogue MITRE ATLAS, techniques manuelles, fuzzing automatisé), et les métriques (taux de réussite des attaques, temps de détection, impact des actions réussies).

**Garak** (de NVIDIA, anciennement LLM Vulnerability Scanner) est l’outil de référence pour le scan automatisé de vulnérabilités LLM. Il teste des centaines de techniques de jailbreak, d’injection, et d’exfiltration sur un modèle ou une API. C’est un outil de screening, pas un pentest complet — il identifie les vulnérabilités évidentes mais ne remplace pas un red teaming manuel par des experts.

**Promptfoo** est un framework d’évaluation systématique des prompts et des réponses. Il permet de définir des jeux de tests (cas d’usage légitimes + cas adversariaux), de les exécuter automatiquement contre le système, et de mesurer les résultats selon des métriques prédéfinies (taux de refus correct, taux de fuite, qualité des réponses). C’est l’outil de choix pour la validation continue en CI/CD.

Le red teaming IA doit être continu, pas ponctuel. Les techniques d’attaque évoluent, les modèles changent (mises à jour du fournisseur, ajustements de prompts, ajout de documents au RAG), et les régressions sont fréquentes.

## 14.3 Gates de validation avant go-live

Avant tout passage en production d’un système IA, une gate de sécurité formelle doit être franchie. C’est le formalisme qui manque souvent entre le POC et la production.

**Gate pilote (POC → pilote).** Critères minimaux : threat model documenté, RBAC vectoriel implémenté (si RAG), politique d’usage rédigée, sanitization des sources activée, jeu de tests fonctionnels et adversariaux de base passé, monitoring minimal en place (logs des requêtes).

**Gate production (pilote → prod).** Critères minimaux : AIPD réalisée (si données personnelles), red teaming IA passé avec rapport, guardrails en entrée et sortie activés et testés, seuils de fuite tolérables définis et mesurés (quel pourcentage de requêtes adversariales passe les défenses ?), métriques d’hallucination mesurées et sous le seuil acceptable, human-in-the-loop implémenté pour les actions critiques (si agent), kill switch testé, intégration SIEM opérationnelle, plan de réponse à incident IA formalisé, formation des utilisateurs réalisée.

L’ANSSI recommande explicitement, dans son guide sur les systèmes d’IA générative, de réaliser un audit de sécurité avant tout déploiement en production et de sécuriser la chaîne de déploiement conformément aux bonnes pratiques d’administration sécurisée. Cet audit doit couvrir non seulement les composants IA spécifiques (modèle, base vectorielle, guardrails) mais aussi l’infrastructure sous-jacente (serveurs, réseau, authentification, chiffrement), en suivant les référentiels reconnus et en intégrant des tests de type red teaming. La CNIL recommande par ailleurs la mise en œuvre d’audits de sécurité reposant sur des référentiels reconnus, incluant les tentatives d’attaque les plus courantes sur le modèle du red teaming.

**Décision go/no-go.** Le RSSI (ou le comité de sécurité) prend la décision formelle sur la base des résultats de la gate. Un no-go n’est pas un échec — c’est un constat que les contrôles ne sont pas encore suffisants et que des actions correctives sont nécessaires avant le déploiement.

-----
