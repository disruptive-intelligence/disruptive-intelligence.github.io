---
title: PARTIE III — SÉCURISER LE DÉPLOIEMENT
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA & sécurité
chapter: 3
chapters: 7
---

## Ch.11 — Politique d’usage IA et gouvernance

### 11.1 La politique d’usage IA

La politique d’usage IA est le document fondateur de la gouvernance IA de l’entreprise. Elle n’est pas un document isolé — elle s’intègre dans la PSSI existante comme une extension couvrant les risques spécifiques de l’IA.

Son contenu minimum inclut le périmètre (quels systèmes IA sont couverts — internes, externes, shadow AI), la classification des données par type de modèle (quelles données peuvent être envoyées à un LLM cloud vs un LLM on-premise vs aucun LLM), les interdictions explicites (jamais de données de santé dans un LLM cloud sans DPA et HDS, jamais de credentials dans un prompt, jamais d’exécution de code généré par IA sans revue), les responsabilités (qui valide un nouveau cas d’usage IA, qui est responsable de la sécurité, qui est responsable de la conformité, qui assure le monitoring), les procédures de validation (gate de sécurité avant déploiement — voir Ch.14), et les sanctions (alignées avec le règlement intérieur).

La politique doit être pragmatique, pas prohibitive. Une politique qui interdit tout pousse au shadow AI. Une politique qui autorise sous conditions, avec des alternatives internes, est respectée.

### 11.2 La gouvernance IA

La gouvernance IA définit les rôles et les processus de décision. Les rôles clés sont le comité IA / sponsor (valide les cas d’usage, arbitre les budgets, assume le risque résiduel), le RSSI (évalue les risques, définit les exigences de sécurité, valide les architectures, pilote le monitoring — c’est le rôle de Karim), le DPO (évalue la conformité RGPD, pilote les AIPD, gère les droits des personnes), le ML Engineer / architecte IA (conçoit et déploie les systèmes, implémente les contrôles techniques), le métier (définit le besoin, valide la pertinence des résultats, assume la responsabilité de l’usage), et les utilisateurs finaux (utilisent le système dans le cadre de la politique, remontent les anomalies).

L’articulation avec la gouvernance SI existante est essentielle : le comité IA peut être un sous-comité du comité de sécurité existant, les revues de risques IA s’intègrent dans le processus de gestion des risques SSI, les incidents IA sont traités dans le processus de gestion des incidents existant.

### 11.3 KPI de gouvernance IA

Les indicateurs de pilotage incluent le nombre de cas d’usage IA déployés (vs demandés vs refusés), le taux de shadow AI résiduel, le nombre d’incidents IA (par type et par gravité), les coûts IA (par cas d’usage et au global), la satisfaction utilisateurs, la conformité (nombre d’AIPD réalisées vs requises, nombre de non-conformités identifiées), et la couverture de monitoring (pourcentage de systèmes IA avec un monitoring actif).

-----

## Ch.12 — Contrôles techniques : IAM, réseau, chiffrement, DLP et sécurité applicative de la stack IA

### 12.1 IAM et RBAC granulaire

Le contrôle d’accès d’un système IA doit être granulaire et multi-couche. Au niveau de l’API du modèle : authentification par API key ou OAuth, différenciation admin / analyste / utilisateur, quotas par rôle. Au niveau de la base vectorielle : RBAC vectoriel (voir Ch.13). Au niveau des logs : accès restreint aux logs de conversation (ils contiennent des données sensibles). Au niveau des outils de l’agent : chaque outil a ses propres credentials avec des permissions scoped (voir Ch.9).

L’erreur classique est le contrôle d’accès unique au niveau de l’application front-end sans contrôle au niveau des composants backend (base vectorielle, API de serving, serveurs MCP). Un attaquant qui bypasse le front-end a alors accès direct à tous les composants.

### 12.2 Segmentation réseau

Le serveur d’inférence doit être dans un VLAN dédié avec des flux contrôlés par allow-list. La base vectorielle doit être dans un segment isolé, accessible uniquement par le backend applicatif. Les serveurs MCP doivent être dans des segments correspondant à la criticité de leurs fonctions (le serveur MCP AD dans le segment admin, le serveur MCP ServiceNow dans le segment applicatif). Les flux entre les composants doivent être chiffrés (TLS 1.3 minimum) et authentifiés (mTLS en production).

### 12.3 Chiffrement

TLS 1.3 pour tous les flux en transit (utilisateur → frontend → backend → modèle → base vectorielle). Chiffrement at rest pour les données stockées : base vectorielle, logs de conversation, documents sources, modèles stockés. KMS (Key Management Service) pour la gestion centralisée des clés. Chiffrement des sauvegardes des modèles et des bases vectorielles.

### 12.4 DLP adapté à l’IA

Le proxy DLP IA se positionne entre l’utilisateur et le modèle (et entre le modèle et les outils de l’agent). Il filtre en entrée (détection de PII, secrets, données classifiées dans les prompts) et en sortie (détection de fuites dans les réponses). Les solutions existantes incluent les modules IA des DLP traditionnels (Symantec, Digital Guardian, Microsoft Purview avec les politiques IA), les solutions spécialisées (Nightfall, Protect AI), et les guardrails open source (LLM Guard, NeMo Guardrails).

### 12.5 Sécurité applicative classique de la stack IA

Un système IA reste une application exposée. Il hérite de toutes les vulnérabilités applicatives classiques — et les additionne aux risques spécifiques de l’IA.

**AuthN/AuthZ.** L’API de serving doit avoir une authentification robuste (pas de Ollama sans auth en production). Le frontend doit valider les sessions. Les endpoints d’administration doivent être protégés par un accès renforcé.

**API security.** Rate limiting, validation des inputs, protection contre les requêtes volumétriques, headers de sécurité, CORS correctement configuré.

**SSRF via connecteurs.** Un agent ou un RAG qui récupère du contenu depuis des URLs (pages web, APIs externes) est potentiellement vulnérable au SSRF — l’attaquant peut rediriger les requêtes vers des services internes. Le filtrage des URLs et l’utilisation d’un proxy sortant dédié sont essentiels.

**Désérialisation.** Au-delà du pickle pour les modèles (voir Ch.8), les frameworks ML utilisent la sérialisation pour les configurations, les pipelines, et les résultats intermédiaires. Chaque point de désérialisation est un vecteur potentiel de RCE.

**Vulnérabilités dans les frameworks d’orchestration.** LangChain, LlamaIndex, et les frameworks similaires ont des historiques de CVE significatifs. Les modules qui exécutent du code arbitraire (Python REPL, shell), qui accèdent au système de fichiers, ou qui font des requêtes réseau sont des surfaces d’attaque directes. En production, n’activer que les modules strictement nécessaires et les maintenir à jour.

Une application IA n’annule pas les vulnérabilités applicatives classiques ; elle les additionne.

-----

## Ch.13 — Sécuriser le RAG : sources, RBAC vectoriel et sanitization

### 13.1 Contrôle des sources

Seuls les documents validés et provenant de sources approuvées doivent être indexés dans le RAG. Cela suppose un inventaire des sources (SharePoint, Confluence, bases documentaires, tickets résolus), un workflow de validation (qui approuve l’ajout d’une nouvelle source ?), un contrôle d’accès en écriture sur les sources (qui peut modifier un document qui sera indexé ?), et un monitoring des modifications (alerte quand un document source est modifié).

Le RAG poisoning (voir Ch.7) exploite précisément l’absence de ces contrôles. Un prestataire avec un accès en écriture trop large sur le SharePoint peut insérer un document malveillant qui sera indexé sans validation.

### 13.2 RBAC vectoriel en détail

L’implémentation du RBAC vectoriel passe par plusieurs étapes. Lors de l’indexation, chaque chunk de document est enrichi avec les métadonnées de permission : identifiant du propriétaire, groupe(s) autorisé(s), niveau de classification, date de validité. Ces métadonnées sont stockées dans la base vectorielle aux côtés du vecteur d’embedding.

Lors du retrieval, le système injecte automatiquement un filtre de permission dans la requête de recherche vectorielle. En pgvector, cela se traduit par une clause WHERE sur les colonnes de permission qui est évaluée AVANT le calcul de similarité cosinus. En Pinecone ou Weaviate, c’est un filtre de métadonnées natif.

Le point critique est la synchronisation des permissions : quand les droits d’un utilisateur changent dans le système source (changement d’équipe, de rôle, départ), les filtres du RBAC vectoriel doivent être mis à jour. Un mécanisme de synchronisation régulière (ou en temps réel via webhook) entre l’annuaire (AD/LDAP) et les métadonnées de la base vectorielle est nécessaire.

### 13.3 Sanitization des documents

Avant indexation, chaque document doit être scanné pour détecter les injections cachées. Les vecteurs à chercher incluent le texte invisible (police blanche sur fond blanc, texte en taille 0, texte caché par CSS ou formatage), les instructions dans les métadonnées (propriétés du document, commentaires, champs personnalisés), le contenu encodé (base64, hex, Unicode homoglyphe), et les instructions dans les champs de formulaire, les cellules Excel cachées, ou les notes de bas de page.

La sanitization peut être automatisée (extraction de texte brut et comparaison avec le texte visible, détection de patterns d’injection par classificateur ML) mais doit aussi inclure une revue manuelle pour les documents provenant de sources à risque (prestataires, partenaires, sources publiques).

### 13.4 Traçabilité et anti-exfiltration

Chaque réponse de l’assistant RAG doit citer les sources utilisées — les documents (ou chunks) qui ont été injectés dans le contexte pour produire la réponse. Cette traçabilité permet à l’utilisateur de vérifier la cohérence de la réponse, au monitoring de détecter l’utilisation de documents suspects, et à l’audit de retracer l’origine de toute information.

L’anti-exfiltration complète la traçabilité : un filtre de sortie vérifie que la réponse ne contient pas de données que l’utilisateur n’est pas censé voir (même après le filtrage RBAC — défense en profondeur), de PII non pertinentes pour la requête, ou de patterns d’injection (l’attaquant tente d’injecter du code ou des URLs dans la réponse via un document RAG poisoned).

-----

## Ch.14 — Guardrails, red teaming, tests de sécurité IA et gates de validation

### 14.1 Les guardrails

Les guardrails sont les contrôles de sécurité appliqués aux entrées et sorties du LLM. Ils se décomposent en deux catégories.

**Guardrails en entrée.** Détection de patterns de prompt injection (classificateurs entraînés sur des corpus de jailbreaks connus), filtrage de contenu inapproprié (requêtes offensantes, hors périmètre), classification des requêtes (routage vers différents modèles ou comportements selon le type de requête), et validation de format (rejet des requêtes mal formées ou anormalement longues).

**Guardrails en sortie.** Vérification de cohérence (la réponse est-elle cohérente avec les sources RAG ? — détection d’hallucination par comparaison), filtrage de contenu (rejet des réponses contenant du contenu offensant, biaisé, ou hors périmètre), DLP (détection de PII, secrets, données classifiées dans la réponse), et validation de format (la réponse respecte-t-elle le format attendu ?).

### 14.1b Improper Output Handling (OWASP LLM05)

Le traitement non sécurisé des sorties du LLM mérite une attention particulière car c’est un risque classé LLM05 par l’OWASP (Version 2025). Le problème ne réside pas dans la qualité de la réponse mais dans ce qu’on en fait en aval. Quand la sortie du modèle est réinjectée dans un système — interprétée comme commande shell, collée dans une requête SQL, exécutée comme code, insérée dans un template HTML, ou utilisée pour construire un appel d’API — ce n’est plus une « mauvaise réponse », c’est une surface d’exploitation downstream.

Les scénarios concrets incluent un agent qui construit une requête SQL à partir de la réponse du LLM (injection SQL de second ordre), une interface qui affiche la réponse en HTML sans échappement (XSS via le LLM), un pipeline qui exécute du code Python suggéré par le modèle (RCE), et un système qui utilise la sortie du LLM comme paramètre d’un appel API sans validation (SSRF, injection de commande). La défense est systématique : toute sortie du LLM qui sera traitée par un autre système doit être validée, échappée et sanitizée exactement comme un input utilisateur non fiable dans une application web classique. Le LLM est un utilisateur non fiable — ses sorties doivent être traitées comme telles.

Les outils de guardrails incluent NeMo Guardrails (NVIDIA — framework de rails en entrée et sortie), LLM Guard (open source — classification et filtrage), Guardrails AI (validation structurée des sorties), et les solutions intégrées des fournisseurs cloud.

### 14.2 Red teaming IA

Le red teaming IA est une discipline spécifique qui teste la résistance d’un système IA aux attaques adversariales. La méthodologie comprend la définition du scope (quels composants tester — modèle, RAG, agent, API, infrastructure), les objectifs (jailbreak, exfiltration, injection, excessive agency, hallucination), les techniques (catalogue MITRE ATLAS, techniques manuelles, fuzzing automatisé), et les métriques (taux de réussite des attaques, temps de détection, impact des actions réussies).

**Garak** (de NVIDIA, anciennement LLM Vulnerability Scanner) est l’outil de référence pour le scan automatisé de vulnérabilités LLM. Il teste des centaines de techniques de jailbreak, d’injection, et d’exfiltration sur un modèle ou une API. C’est un outil de screening, pas un pentest complet — il identifie les vulnérabilités évidentes mais ne remplace pas un red teaming manuel par des experts.

**Promptfoo** est un framework d’évaluation systématique des prompts et des réponses. Il permet de définir des jeux de tests (cas d’usage légitimes + cas adversariaux), de les exécuter automatiquement contre le système, et de mesurer les résultats selon des métriques prédéfinies (taux de refus correct, taux de fuite, qualité des réponses). C’est l’outil de choix pour la validation continue en CI/CD.

Le red teaming IA doit être continu, pas ponctuel. Les techniques d’attaque évoluent, les modèles changent (mises à jour du fournisseur, ajustements de prompts, ajout de documents au RAG), et les régressions sont fréquentes.

### 14.3 Gates de validation avant go-live

Avant tout passage en production d’un système IA, une gate de sécurité formelle doit être franchie. C’est le formalisme qui manque souvent entre le POC et la production.

**Gate pilote (POC → pilote).** Critères minimaux : threat model documenté, RBAC vectoriel implémenté (si RAG), politique d’usage rédigée, sanitization des sources activée, jeu de tests fonctionnels et adversariaux de base passé, monitoring minimal en place (logs des requêtes).

**Gate production (pilote → prod).** Critères minimaux : AIPD réalisée (si données personnelles), red teaming IA passé avec rapport, guardrails en entrée et sortie activés et testés, seuils de fuite tolérables définis et mesurés (quel pourcentage de requêtes adversariales passe les défenses ?), métriques d’hallucination mesurées et sous le seuil acceptable, human-in-the-loop implémenté pour les actions critiques (si agent), kill switch testé, intégration SIEM opérationnelle, plan de réponse à incident IA formalisé, formation des utilisateurs réalisée.

L’ANSSI recommande explicitement, dans son guide sur les systèmes d’IA générative, de réaliser un audit de sécurité avant tout déploiement en production et de sécuriser la chaîne de déploiement conformément aux bonnes pratiques d’administration sécurisée. Cet audit doit couvrir non seulement les composants IA spécifiques (modèle, base vectorielle, guardrails) mais aussi l’infrastructure sous-jacente (serveurs, réseau, authentification, chiffrement), en suivant les référentiels reconnus et en intégrant des tests de type red teaming. La CNIL recommande par ailleurs la mise en œuvre d’audits de sécurité reposant sur des référentiels reconnus, incluant les tentatives d’attaque les plus courantes sur le modèle du red teaming.

**Décision go/no-go.** Le RSSI (ou le comité de sécurité) prend la décision formelle sur la base des résultats de la gate. Un no-go n’est pas un échec — c’est un constat que les contrôles ne sont pas encore suffisants et que des actions correctives sont nécessaires avant le déploiement.

-----

## Ch.15 — Observabilité, monitoring et intégration SIEM

### 15.1 Logging

Chaque interaction avec le système IA doit être tracée. Le log minimal inclut le timestamp, l’identifiant de l’utilisateur, le prompt (ou un hash si la taille est prohibitive), la réponse (ou un résumé), le modèle utilisé, les sources RAG consultées (identifiants des chunks), les actions de l’agent (si applicable), la latence, le coût (tokens consommés), et le résultat des guardrails (requête filtrée ? réponse filtrée ? raison ?).

Les logs eux-mêmes sont des données sensibles — ils contiennent en clair les questions et les réponses, qui peuvent inclure des données personnelles, des informations médicales, des données financières. Ils doivent être chiffrés at rest, avec un contrôle d’accès strict, et une durée de conservation définie (alignée avec la politique de rétention des données et les exigences RGPD).

### 15.2 Métriques opérationnelles

Les métriques de monitoring IA couvrent la performance (latence par requête, throughput, taux d’erreur, disponibilité), la qualité (taux d’hallucination mesuré par spot-check, satisfaction utilisateur, taux de correction des réponses), la sécurité (nombre de tentatives d’injection détectées, nombre de fuites détectées, nombre d’actions agent bloquées), le coût (coût par requête, coût par cas d’usage, tendance du coût dans le temps), et l’usage (volume de requêtes par utilisateur/groupe, heures d’utilisation, requêtes les plus fréquentes).

### 15.3 Détection d’abus

Les patterns suspects à surveiller incluent le volume anormal d’un utilisateur (extraction de données potentielle), les requêtes de type extraction (« liste tous les… », « donne-moi toutes les informations sur… »), les tentatives de jailbreak répétées (l’utilisateur essaie différentes formulations pour contourner les guardrails), les requêtes hors périmètre (un gestionnaire de sinistres qui pose des questions sur la comptabilité ou les RH), et les patterns temporels anormaux (requêtes à 3h du matin, weekend, vacances).

### 15.4 Intégration SIEM/SOAR

Les événements du système IA doivent alimenter le SIEM existant pour permettre la corrélation avec les autres logs de sécurité. Un jailbreak détecté sur l’assistant peut être corrélé avec une connexion suspecte sur l’AD. Une injection détectée dans un ticket peut être corrélée avec l’identité du soumetteur. Un pic de requêtes peut être corrélé avec une alerte DLP sur les flux sortants.

L’intégration se fait typiquement via syslog ou via une API de collecte (Splunk HEC, Elastic API). Les alertes SIEM spécifiques à l’IA doivent être définies : jailbreak détecté, fuite de données détectée, action agent bloquée par le kill switch, modification d’un document source du RAG, échec d’authentification sur l’API du modèle.

Le monitoring des coûts mérite une attention particulière : un pic de consommation (tokens, GPU) peut être un signe d’abus (un utilisateur qui extrait massivement des données), d’attaque (DoS par prompts complexes), ou simplement d’un usage inattendu à investiguer.

-----
