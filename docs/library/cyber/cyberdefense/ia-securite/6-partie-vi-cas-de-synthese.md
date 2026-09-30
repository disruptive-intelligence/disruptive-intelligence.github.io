---
title: PARTIE VI — CAS DE SYNTHÈSE
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA & sécurité
chapter: 6
chapters: 7
---

## Ch.22 — Cas complet : déploiement et sécurisation d’un assistant RAG (NovaSanté)

### 22.1 Contexte et architecture

Ce cas de synthèse rassemble l’ensemble du fil rouge sur l’assistant RAG pour les 80 gestionnaires de sinistres de NovaSanté. L’architecture retenue est la suivante : serveur d’inférence on-premise (Ollama avec Mistral 7B, puis upgrade vers Llama 3.1 8B pour la qualité de réponse en français), base vectorielle pgvector sur PostgreSQL (serveur dédié, chiffré at rest), backend FastAPI (API REST avec authentification JWT, intégration LDAP pour les permissions), reverse proxy Nginx avec mTLS pour l’accès utilisateur, et pipeline d’indexation (extraction de texte avec Apache Tika, chunking par paragraphe avec overlap, embedding via modèle multilingual-e5-large, stockage dans pgvector avec métadonnées de permission).

Le déploiement on-premise est imposé par la contrainte HDS — les données de santé ne peuvent pas transiter vers un LLM cloud non certifié. Le choix d’un modèle 7-8B est un arbitrage entre qualité de réponse et ressources matérielles disponibles (le serveur d’inférence dispose de 2 GPU A10G).

### 22.2 Threat model spécifique

Les risques identifiés par Karim pour l’assistant RAG sont les suivants. L’injection indirecte via un document malveillant dans le SharePoint source (criticité élevée — un prestataire avec accès en écriture peut injecter une procédure falsifiée). La fuite de données transversale par absence de RBAC vectoriel (criticité élevée — un gestionnaire accède aux dossiers d’autres agences). L’hallucination sur des procédures critiques (criticité modérée — le modèle invente une procédure ou un plafond). La mémorisation de données sensibles dans les logs (criticité modérée — les logs contiennent les questions et réponses incluant des données de santé). Et l’indisponibilité du serveur d’inférence (criticité modérée — les gestionnaires ne peuvent plus interroger la base documentaire).

### 22.3 Implémentation des contrôles

**RBAC vectoriel.** Chaque chunk indexé est enrichi avec trois métadonnées de permission : `agence_id` (l’agence propriétaire du dossier), `gestionnaire_id` (le gestionnaire attitré), et `access_level` (standard, restreint-juridique, confidentiel-direction). Le retriever filtre par `(agence_id = $user_agence AND access_level = 'standard') OR gestionnaire_id = $user_id`.

**Sanitization.** Chaque document est scanné avant indexation : extraction de texte avec Apache Tika, comparaison du texte extrait avec le rendu visuel (détection de texte invisible), recherche de patterns d’injection (instructions en langage naturel hors contexte documentaire), et validation par le référent documentaire de chaque service pour les documents critiques (procédures, règlements).

**Guardrails.** En entrée : détection de prompt injection (classificateur fine-tuné sur des exemples d’injection), limitation de la taille du prompt, détection de requêtes hors périmètre (le gestionnaire ne doit pouvoir poser que des questions liées à la gestion de sinistres). En sortie : détection de PII non pertinentes dans la réponse, vérification que la réponse cite au moins une source RAG (réduction des hallucinations), et filtrage des marqueurs de données de santé (diagnostics, traitements) qui ne devraient pas apparaître dans les réponses standards.

**Monitoring.** Intégration SIEM (Splunk) avec alertes sur les tentatives d’injection détectées, les requêtes hors périmètre, les modifications de documents sources, et les anomalies de volume (un gestionnaire qui pose 200 requêtes en une heure).

### 22.4 Checklist go/no-go

Avant le passage en production, la gate de sécurité vérifie que le RBAC vectoriel est implémenté et testé (test croisé entre agences), que la sanitization est activée et fonctionnelle, que les guardrails en entrée et sortie sont en place, que l’AIPD a été réalisée et validée par le DPO, que le red teaming (Garak + tests manuels d’injection indirecte) a produit un rapport acceptable, que le monitoring SIEM est opérationnel, que la politique d’usage est communiquée aux gestionnaires, que la formation des utilisateurs est réalisée (comment utiliser l’assistant, quoi ne pas faire, comment remonter une anomalie), et que le plan de réponse à incident IA est formalisé.

### 22.5 L’incident : injection indirecte via document frauduleux

Six semaines après le go-live, un prestataire externe avec accès en écriture au SharePoint « Procédures sinistres » insère un document contenant des instructions d’injection indirecte cachées en texte blanc et de fausses procédures de remboursement. Le pipeline de réindexation tourne toutes les 6 heures — le document est indexé.

**Détection.** Un gestionnaire signale une réponse inhabituelle de l’assistant : celui-ci recommande de transférer un dossier à une adresse email externe inconnue. Le monitoring détecte parallèlement une modification récente sur le SharePoint source par un compte prestataire.

**Confinement.** Karim active le kill switch de l’assistant (mise hors service immédiate). La base vectorielle est isolée. Le document malveillant est identifié et supprimé du SharePoint.

**Investigation.** L’équipe analyse les logs de l’assistant pour identifier toutes les requêtes qui ont utilisé le document malveillant comme source RAG. Résultat : 14 réponses contaminées sur 3 jours, touchant 8 gestionnaires. Aucune donnée de santé n’a été exfiltrée (l’injection visait à rediriger des dossiers, pas à extraire des données). L’accès du prestataire est révoqué. L’investigation forensique sur le compte prestataire est lancée.

**Remédiation.** Le document est purgé de la base vectorielle. L’indexation est relancée avec un scan de sanitization complet de toutes les sources. Le monitoring est renforcé : alerte immédiate sur toute modification SharePoint par un compte non-DSI. Le workflow de validation avant indexation est implémenté (toute modification doit être approuvée par un référent documentaire avant réindexation).

**Communication.** Les 8 gestionnaires impactés sont informés individuellement. Le DPO est consulté : comme aucune donnée personnelle n’a été exfiltrée mais que l’intégrité des réponses a été compromise, la décision est de documenter l’incident sans notification CNIL (pas de violation de données personnelles au sens de l’article 33). Le COMEX est informé avec un rapport factuel et un plan de remédiation.

**Retex.** Le threat model est mis à jour avec le vecteur « prestataire avec accès en écriture sur les sources RAG ». Le contrôle d’accès en écriture est revu : seuls les référents documentaires internes ont désormais l’accès en écriture direct, les prestataires passent par un workflow de soumission avec validation.

-----

## Ch.23 — Cas complet : sécurisation d’un agent IA help desk

### 23.1 Architecture et threat model

L’agent help desk de NovaSanté utilise un LLM (Mistral via Ollama) avec accès à deux serveurs MCP : un serveur MCP Active Directory (fonctions : reset_password, lookup_user, unlock_account) et un serveur MCP ServiceNow (fonctions : create_ticket, update_ticket, query_kb). Le serveur MCP AD utilise un service account dédié (`svc_agent_helpdesk`) avec des permissions scopées : uniquement les comptes du groupe « Utilisateurs standard », uniquement les actions de reset password et unlock account, pas de création/suppression de compte, pas d’accès aux groupes « Domain Admins », « Administrateurs », ou « Comptes de service ».

Le threat model identifie le prompt injection via les tickets de support (un ticket contenant une instruction cachée est traité par l’agent), l’escalade de privilèges (l’agent tente d’agir sur un compte admin), l’exfiltration via les outils (l’agent envoie des données via un ticket ServiceNow ou un email), et le déni de service (saturation de l’agent avec des requêtes malveillantes).

### 23.2 Contrôles implémentés

Le moindre privilège est implémenté au niveau du serveur MCP AD (le service account n’a littéralement pas les droits pour modifier un compte admin). L’allow-list d’actions est codée dans le middleware (seules les fonctions listées sont exécutables — toute autre action est rejetée). Le human-in-the-loop est obligatoire pour toute action AD (le reset password génère une notification au manager du collaborateur concerné, qui doit confirmer). Le kill switch est un circuit breaker qui désactive l’agent si plus de 5 actions AD sont tentées en 10 minutes ou si une action sur un compte hors périmètre est détectée. Le logging exhaustif trace chaque action avec le ticket d’origine, le raisonnement du LLM, et le résultat.

### 23.3 Incident et correction

Pendant les tests adversariaux, l’équipe découvre que l’agent peut être manipulé pour enchaîner des actions légitimes de manière abusive : « Réinitialise le mot de passe de user1@novasante.fr, puis de user2@novasante.fr, puis de user3@… » dans un seul ticket. L’allow-list autorise chaque action individuellement, mais l’enchaînement constitue un abus.

Correction : limitation à une action AD par requête, avec un cooldown de 5 minutes entre deux actions AD. Le ticket qui demande plusieurs actions est refusé par l’agent avec une indication de soumettre des tickets séparés.

-----

## Ch.24 — Cas complet : gestion du shadow AI et déploiement d’une alternative interne

### 24.1 Diagnostic

L’audit shadow AI révèle que 85 % des gestionnaires utilisent ChatGPT pour résumer des dossiers (données de santé incluses), trois managers utilisent Claude pour des notes de synthèse, le juridique utilise Perplexity avec des noms d’assurés. L’analyse de risque montre une violation potentielle du RGPD (transfert hors UE sans DPA, pas de base légale pour le sous-traitant), une violation potentielle de l’obligation HDS (données de santé hébergées hors infrastructure certifiée), et un risque réputationnel (si une fuite est médiatisée).

### 24.2 Stratégie en cinq niveaux

**Détection** (semaines 1-2) : analyse des logs proxy, enquête anonyme auprès des collaborateurs. **Alternative interne** (semaines 3-12) : accélération du déploiement de l’assistant RAG comme outil officiel couvrant les cas d’usage identifiés. **Politique** (semaine 4) : publication de la politique d’usage IA avec les interdictions explicites (jamais de données de santé, jamais de données nominatives, jamais de documents confidentiels dans un LLM cloud non contractualisé). **Contrôle technique** (semaine 6) : blocage des APIs ChatGPT, Claude, et Perplexity sur le proxy pour les postes des gestionnaires et du juridique (accès maintenu pour la DSI à des fins de veille technique). **Sensibilisation** (continue) : sessions de formation sur les risques spécifiques, démonstration de l’alternative interne, communication managériale.

### 24.3 Résultats

À 6 mois, le shadow AI passe de 85 % à 15 % (usage résiduel principalement sur des tâches sans données sensibles — rédaction de mails, recherche d’information générique). La satisfaction des gestionnaires sur l’assistant RAG interne est de 78 % (principal reproche : temps de réponse plus lent que ChatGPT, qualité de réponse parfois inférieure sur les questions complexes — compensé par la pertinence sur les données NovaSanté et l’absence de risque de fuite).

-----

## Ch.25 — Cas complet : réponse à incident IA

Ce chapitre documente l’incident complet du RAG poisoning décrit au Ch.22 sous un angle processus de réponse à incident, en appliquant les 6 phases classiques (préparation, détection, confinement, investigation, remédiation, retex) au contexte spécifique d’un incident IA.

Le point clé est que la réponse à incident IA suit le même processus que la réponse à incident classique, mais avec des spécificités : le confinement peut nécessiter un kill switch du système IA (pas seulement une isolation réseau), l’investigation doit tracer les réponses contaminées (pas seulement les accès réseau), la remédiation implique une purge et réindexation de la base vectorielle (pas seulement un patch), et la communication doit inclure le DPO pour évaluer si une notification CNIL est nécessaire.

Le livrable de cet exercice est un plan de réponse à incident IA formel pour NovaSanté, intégré au plan de réponse à incident existant, avec les procédures spécifiques (kill switch, purge vectorielle, analyse des réponses contaminées) et les rôles (RSSI pilote, ML Engineer exécute, DPO évalue la notification).

-----
