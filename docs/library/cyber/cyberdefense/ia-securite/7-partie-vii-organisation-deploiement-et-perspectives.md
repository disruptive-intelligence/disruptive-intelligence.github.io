---
title: PARTIE VII — ORGANISATION, DÉPLOIEMENT ET PERSPECTIVES
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA & sécurité
chapter: 7
chapters: 7
---

### Ch.26 — Déployer l’IA en entreprise : phases, gates, conduite du changement et overreliance

#### 26.1 Le déploiement itératif

Le déploiement d’un système IA en entreprise suit un cycle itératif : cadrage (définition du besoin, évaluation de faisabilité, classification du risque), POC (preuve de concept technique — « est-ce que ça fonctionne ? »), pilote (test en conditions réelles avec un groupe restreint d’utilisateurs — « est-ce que ça fonctionne pour les utilisateurs ? »), production (déploiement complet avec monitoring — « est-ce que ça tient ? »), scaling (extension à d’autres équipes, cas d’usage adjacents), et run (exploitation continue, maintenance, mise à jour).

Chaque transition entre phases est une gate de sécurité (voir Ch.14). Le passage direct du POC à la production — fréquent dans les projets IA poussés par le COMEX — est une des principales causes d’incidents.

#### 26.2 Overreliance et facteur humain

L’intégration de l’IA dans les processus métier modifie le comportement des utilisateurs de façon profonde et souvent sous-estimée.

**L’automation bias** fait que les utilisateurs tendent à suivre les recommandations de l’IA même quand elles sont manifestement incorrectes, simplement parce que « la machine l’a dit ». Pour le module de fraude de NovaSanté, cela signifie que les gestionnaires risquent de valider un scoring IA sans vérification, manquant des faux négatifs ou confirmant des faux positifs.

**La surconfiance dans les réponses** du RAG est le pendant de l’automation bias pour l’IA générative : le gestionnaire qui reçoit une réponse fluide et bien sourcée de l’assistant a tendance à la prendre pour argent comptant sans vérifier les sources citées. Si la réponse est une hallucination (ou pire, le résultat d’un RAG poisoning), l’absence de vérification humaine transforme une erreur IA en erreur métier.

**L’effondrement de la vigilance** se produit quand les utilisateurs, habitués à ce que l’IA fonctionne correctement 95 % du temps, cessent de vérifier systématiquement. Les 5 % restants — qui incluent les cas les plus critiques et les plus subtils — ne sont plus rattrapés.

**La fatigue de validation** est le risque associé au human-in-the-loop : si l’agent help desk demande une validation humaine pour chaque action AD, et que 99 % des actions sont légitimes, le validateur va finir par approuver automatiquement sans lire — annulant l’effet du contrôle.

**Le transfert de responsabilité implicite** se produit quand les utilisateurs considèrent que la responsabilité d’une décision a été transférée au système IA : « ce n’est pas moi qui ai décidé, c’est l’IA ». En réalité, l’utilisateur (et l’entreprise) restent responsables des décisions prises sur la base des sorties de l’IA.

Les contre-mesures incluent la formation explicite et répétée à la faillibilité de l’IA, la conception d’interfaces qui présentent les sorties IA comme des suggestions (pas des certitudes), la variation des tâches de validation (ne pas toujours les mêmes validateurs), les vérifications aléatoires par des superviseurs, et les métriques de qualité qui mesurent la capacité de détection humaine indépendante de l’IA.

#### 26.3 Conduite du changement

L’IA modifie les processus, les rôles et les responsabilités. La résistance au changement est normale et doit être gérée activement. Les facteurs de succès incluent l’implication des utilisateurs dès le cadrage (pas de déploiement « top-down » sans consultation), la transparence sur les capacités et les limites de l’IA (ne pas survendre), la formation pratique (pas seulement théorique), le support dédié pendant la phase de transition, et les quick wins visibles (démontrer la valeur ajoutée rapidement pour créer l’adhésion).

-----

### Ch.27 — Construire une capacité de sécurité IA dans l’organisation

#### 27.1 Les compétences nécessaires

La sécurité IA requiert des compétences à l’intersection de la cybersécurité et du ML/IA. Le RSSI doit comprendre les architectures IA (RAG, agents, MCP), les menaces spécifiques (prompt injection, data poisoning), et les cadres de référence (OWASP Top 10 for LLM, MITRE ATLAS) pour évaluer les risques et définir les contrôles. Le ML Engineer doit comprendre les principes de sécurité (moindre privilège, défense en profondeur, logging) pour concevoir des systèmes sûrs dès la conception. Le SOC doit être formé aux alertes spécifiques IA (injection détectée, fuite détectée, action agent bloquée) pour les traiter efficacement.

#### 27.2 Formation et montée en compétence

Les formations de référence incluent SANS SEC595 (Applied Data Science and AI/Machine Learning for Cybersecurity Professionals), la certification OWASP sur la sécurité des LLMs, les CTF spécialisés IA security (Gandalf, HackAPrompt), et les formations internes (red teaming IA sur les systèmes de l’entreprise). La veille continue sur les publications ANSSI, NIST, ENISA, et les publications de recherche est indispensable dans un domaine qui évolue aussi rapidement.

#### 27.3 L’articulation avec les équipes existantes

La sécurité IA n’est pas une équipe séparée — elle s’intègre dans les équipes existantes. L’équipe sécurité apporte l’expertise threat model, contrôles, monitoring, incident response. L’équipe data/ML apporte l’expertise technique IA et implémente les contrôles (RBAC vectoriel, sanitization, guardrails). L’équipe développement intègre les contrôles dans les pipelines CI/CD. Le métier valide la pertinence des résultats et assume la responsabilité de l’usage.

-----

### Ch.28 — Perspectives : évolution des menaces et de la défense

#### 28.1 Agents IA de plus en plus autonomes

La tendance dominante est l’autonomisation croissante des agents IA. Les agents actuels exécutent des tâches unitaires (reset password, création de ticket). Les agents de demain orchestreront des workflows complets (diagnostic d’un incident, remédiation complète, communication aux parties prenantes). Le risque d’excessive agency augmente mécaniquement avec l’autonomie : plus l’agent peut faire de choses, plus les conséquences d’une manipulation sont graves. La défense doit évoluer en parallèle : les contrôles actuels (allow-list, human-in-the-loop) devront être complétés par des mécanismes d’évaluation de confiance en temps réel sur les actions de l’agent.

#### 28.2 Modèles multimodaux

Les modèles qui traitent simultanément du texte, des images, de l’audio et de la vidéo ouvrent de nouvelles surfaces d’injection. Une image contenant une instruction cachée (stéganographie, texte dans les pixels), un audio avec des instructions dans les fréquences inaudibles, une vidéo avec un QR code flash — les vecteurs d’injection se multiplient au-delà du texte. Les défenses actuelles, très orientées texte, devront s’adapter.

#### 28.3 IA embarquée (on-device)

L’exécution de modèles IA directement sur les terminaux (smartphones, laptops, objets connectés) pose de nouvelles questions de sécurité et de confidentialité. D’un côté, les données restent sur l’appareil (avantage vie privée). De l’autre, le modèle est directement accessible à l’attaquant qui a compromis le terminal (pas de protection périmétrique), et les mises à jour de sécurité du modèle sont plus difficiles à déployer.

#### 28.4 Réglementation en durcissement

L’AI Act entre en application progressive jusqu’en 2027. D’autres juridictions développent leurs propres cadres. Les exigences de conformité vont se complexifier et s’uniformiser à l’international. La capacité à démontrer la conformité (documentation technique, AIPD, évaluations de risques, audits) deviendra un facteur différenciant.

#### 28.5 Questions ouvertes

L’alignement (comment garantir qu’un modèle IA se comporte comme prévu dans tous les cas, y compris les cas non prévus ?) reste un problème ouvert. L’explicabilité (comment expliquer pourquoi le modèle a produit cette réponse ?) progresse mais reste difficile pour les modèles les plus complexes. La responsabilité juridique des décisions IA (qui est responsable quand l’IA se trompe — l’utilisateur ? l’entreprise ? le fournisseur du modèle ?) est en cours de clarification. Le droit d’effacement dans les poids d’un modèle (comment supprimer les données d’une personne des poids d’un modèle sans le ré-entraîner ?) est un défi technique et juridique ouvert.

-----


## ANNEXES

### Annexe A — Glossaire IA & SSI (60+ termes)

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

### Annexe B — OWASP Top 10 for LLM Applications (Version 2025) et MITRE ATLAS : référence rapide

#### OWASP Top 10 for LLM Applications — Nomenclature officielle Version 2025

|Rang |Risque officiel                 |Description résumée                                                                                                                                              |
|-----|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|LLM01|Prompt Injection                |Manipulation du comportement du LLM via des instructions injectées — directes (jailbreak) ou indirectes (via documents, emails, pages web)                       |
|LLM02|Sensitive Information Disclosure|Divulgation de données sensibles (PII, données propriétaires, credentials) via les réponses du modèle ou par extraction des données d’entraînement               |
|LLM03|Supply Chain                    |Vulnérabilités dans la chaîne d’approvisionnement — modèles pré-entraînés compromis, dépendances vulnérables, datasets empoisonnés, adaptateurs LoRA malveillants|
|LLM04|Data and Model Poisoning        |Corruption des données de pré-entraînement, fine-tuning ou embedding pour introduire des vulnérabilités, backdoors ou biais dans le modèle                       |
|LLM05|Improper Output Handling        |Validation insuffisante des sorties du LLM avant passage à des systèmes downstream — risque de XSS, SSRF, RCE, injection SQL de second ordre                     |
|LLM06|Excessive Agency                |Actions non autorisées exécutées par un agent IA en raison de fonctionnalités excessives, permissions excessives ou autonomie excessive                          |
|LLM07|System Prompt Leakage           |Fuite du prompt système révélant des informations sensibles (architecture, credentials, règles internes, rôles)                                                  |
|LLM08|Vector and Embedding Weaknesses |Vulnérabilités dans les systèmes RAG — accès non autorisé aux embeddings, fuites cross-contexte, empoisonnement des données vectorielles                         |
|LLM09|Misinformation                  |Production de contenu faux ou trompeur apparaissant crédible (hallucinations, biais) — risque aggravé par l’overreliance des utilisateurs                        |
|LLM10|Unbounded Consumption           |Consommation excessive et non contrôlée de ressources — DoS, Denial of Wallet, extraction de modèle via interrogation massive                                    |

#### Mapping OWASP Top 10 2025 → Chapitres du cours

|Risque OWASP                          |Chapitre(s) principal(aux)|Chapitres complémentaires|
|--------------------------------------|--------------------------|-------------------------|
|LLM01 Prompt Injection                |Ch.5                      |Ch.9, Ch.13, Ch.14       |
|LLM02 Sensitive Information Disclosure|Ch.6                      |Ch.13, Ch.15             |
|LLM03 Supply Chain                    |Ch.8                      |Ch.12, Ch.18             |
|LLM04 Data and Model Poisoning        |Ch.7                      |Ch.8, Ch.13              |
|LLM05 Improper Output Handling        |Ch.14 (section 14.1b)     |Ch.9, Ch.12              |
|LLM06 Excessive Agency                |Ch.9                      |Ch.14, Ch.23             |
|LLM07 System Prompt Leakage           |Ch.5, Ch.6                |Ch.14                    |
|LLM08 Vector and Embedding Weaknesses |Ch.13                     |Ch.6, Ch.7               |
|LLM09 Misinformation                  |Ch.26 (overreliance)      |Ch.17                    |
|LLM10 Unbounded Consumption           |Ch.10                     |Ch.12, Ch.15             |

#### MITRE ATLAS — Tactiques principales

|Tactique ATLAS      |Description                                                        |Chapitre(s)|
|--------------------|-------------------------------------------------------------------|-----------|
|Reconnaissance      |Collecte d’informations sur le système IA cible                    |Ch.16      |
|Resource Development|Préparation des outils et infrastructures d’attaque                |Ch.16      |
|Initial Access      |Accès initial au système IA (prompt injection, API compromise)     |Ch.5       |
|ML Model Access     |Accès au modèle pour l’interroger ou l’extraire                    |Ch.7       |
|Execution           |Exécution d’actions malveillantes via le système IA                |Ch.9       |
|Persistence         |Maintien de l’accès (backdoor dans le modèle, poisoning persistant)|Ch.7       |
|Exfiltration        |Extraction de données via le système IA                            |Ch.6       |
|Impact              |Dégradation, manipulation ou destruction du système IA             |Ch.7, Ch.10|

-----

### Annexe C — Checklists réutilisables

#### Checklist avant déploiement d’un système IA

- [ ] Threat model spécifique documenté
- [ ] Classification du système selon l’AI Act (inacceptable / haut risque / limité / minimal)
- [ ] AIPD réalisée si données personnelles traitées
- [ ] Base légale RGPD identifiée et documentée
- [ ] RBAC vectoriel implémenté et testé (si RAG)
- [ ] Sanitization des sources activée (si RAG)
- [ ] Guardrails en entrée et sortie configurés et testés
- [ ] Red teaming IA réalisé avec rapport (Garak + tests manuels)
- [ ] Seuils de fuite/hallucination mesurés et acceptables
- [ ] Human-in-the-loop implémenté pour les actions critiques (si agent)
- [ ] Allow-list d’actions configurée (si agent)
- [ ] Kill switch testé (si agent)
- [ ] Monitoring et intégration SIEM opérationnels
- [ ] DPA signé avec le fournisseur de modèle (si cloud)
- [ ] Politique d’usage IA rédigée et communiquée
- [ ] Formation des utilisateurs réalisée
- [ ] Plan de réponse à incident IA formalisé
- [ ] Décision go/no-go formelle par le RSSI

#### Checklist pendant l’exploitation

- [ ] Monitoring des alertes IA (injection, fuite, action bloquée) opérationnel
- [ ] Revue périodique des logs (mensuelle minimum)
- [ ] Suivi des métriques de performance et de qualité
- [ ] Suivi des coûts
- [ ] Red teaming périodique (trimestriel minimum)
- [ ] Mise à jour des guardrails et des techniques de détection
- [ ] Revue des permissions RBAC (alignement avec l’annuaire)
- [ ] Monitoring du drift (si ML classique)
- [ ] Mise à jour des dépendances (SCA)
- [ ] Suivi de la politique d’usage (taux de shadow AI résiduel)

#### Checklist en cas d’incident IA

- [ ] Activation du kill switch si nécessaire
- [ ] Confinement du composant impacté (base vectorielle, modèle, agent)
- [ ] Identification de l’incident (injection ? poisoning ? fuite ? abus ?)
- [ ] Analyse des logs pour déterminer l’étendue (quelles requêtes/réponses impactées ?)
- [ ] Identification des utilisateurs impactés
- [ ] Purge des données malveillantes (base vectorielle, source documentaire)
- [ ] Évaluation par le DPO (violation de données personnelles ? notification CNIL ?)
- [ ] Communication aux utilisateurs impactés
- [ ] Remédiation technique (correction des contrôles, re-indexation, mise à jour)
- [ ] Retex et mise à jour du threat model
- [ ] Rapport d’incident formel

-----

### Annexe D — Architecture de référence : assistant RAG sécurisé

```
┌─────────────────────────────────────────────────────────────────┐
│                         UTILISATEUR                              │
│                    (authentifié via SSO/LDAP)                     │
└──────────────────────────┬──────────────────────────────────────┘
                           │ HTTPS (mTLS)
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│                    REVERSE PROXY (Nginx)                          │
│  - TLS 1.3 termination                                           │
│  - Rate limiting par utilisateur                                 │
│  - Authentification (JWT/mTLS)                                   │
│  - WAF basique                                                   │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│                    BACKEND API (FastAPI)                          │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────────┐  │
│  │ INPUT DLP    │→ │ GUARDRAIL IN │→ │ ORCHESTRATEUR RAG     │  │
│  │ (PII, secrets│  │ (injection   │  │ - embedding requête    │  │
│  │  detection)  │  │  detection)  │  │ - retrieval + RBAC     │  │
│  └──────────────┘  └──────────────┘  │ - construction prompt  │  │
│                                       │ - appel LLM            │  │
│  ┌──────────────┐  ┌──────────────┐  │ - traçabilité sources  │  │
│  │ OUTPUT DLP   │← │ GUARDRAIL OUT│← └───────────────────────┘  │
│  │ (fuite, PII) │  │ (cohérence,  │                              │
│  └──────────────┘  │  hallucin.)  │                              │
│                     └──────────────┘                              │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ LOGGING → SIEM (Splunk)                                   │    │
│  │ (timestamp, user, prompt_hash, response_hash, sources,    │    │
│  │  guardrail_results, latency, cost)                        │    │
│  └──────────────────────────────────────────────────────────┘    │
└──────┬───────────────────────────┬──────────────────────────────┘
       │                           │
       ▼                           ▼
┌──────────────┐          ┌──────────────────────────────────┐
│ LLM SERVER   │          │ BASE VECTORIELLE (pgvector)       │
│ (Ollama/vLLM)│          │ - Embeddings + métadonnées RBAC   │
│ - Mistral/   │          │ - Filtrage par permissions AVANT   │
│   Llama      │          │   recherche de similarité          │
│ - GPU dédié  │          │ - Chiffrement at rest              │
│ - Pas d'accès│          │ - Accès restreint au backend       │
│   direct     │          └──────────────────────────────────┘
└──────────────┘                       ▲
                                       │ Réindexation périodique
                          ┌────────────┴─────────────────────┐
                          │ PIPELINE D'INDEXATION             │
                          │ - Extraction (Apache Tika)         │
                          │ - Sanitization (injection scan)    │
                          │ - Chunking + embedding             │
                          │ - Enrichissement métadonnées RBAC  │
                          │ - Validation référent documentaire │
                          └────────────┬─────────────────────┘
                                       │
                          ┌────────────┴─────────────────────┐
                          │ SOURCES DOCUMENTAIRES              │
                          │ (SharePoint, Confluence)            │
                          │ - Contrôle d'accès en écriture     │
                          │ - Monitoring des modifications      │
                          │ - Workflow de validation             │
                          └──────────────────────────────────┘
```

-----

### Annexe E — Matrice de décision cloud vs on-premise vs hybride

|Critère                                 |Cloud (API)                                   |On-premise                   |Hybride                                    |
|----------------------------------------|----------------------------------------------|-----------------------------|-------------------------------------------|
|**Données sensibles (santé, financier)**|⚠️ DPA obligatoire, transfert hors UE à évaluer|✅ Données restent dans le SI |✅ Données sensibles on-prem, reste en cloud|
|**Réglementation HDS**                  |❌ Peu de fournisseurs LLM certifiés HDS       |✅ Infrastructure certifiable |✅ Séparation par criticité                 |
|**Coût initial**                        |✅ Faible (pay-per-use)                        |❌ Élevé (GPU, infrastructure)|⚠️ Modéré                                   |
|**Coût récurrent**                      |⚠️ Variable, peut exploser                     |✅ Prévisible (amortissement) |⚠️ Double gestion                           |
|**Performance / qualité**               |✅ Meilleurs modèles disponibles               |⚠️ Modèles plus petits        |✅ Best of both                             |
|**Contrôle**                            |❌ Dépendance fournisseur                      |✅ Contrôle total             |⚠️ Complexité accrue                        |
|**Maintenance**                         |✅ Gérée par le fournisseur                    |❌ Responsabilité interne     |⚠️ Mixte                                    |
|**Latence**                             |⚠️ Variable (réseau)                           |✅ Prévisible (locale)        |⚠️ Variable selon le composant              |
|**Disponibilité**                       |⚠️ Dépendance fournisseur                      |✅ Maîtrisée                  |⚠️ Points de défaillance multiples          |
|**Compétences requises**                |✅ Faibles (API)                               |❌ ML Ops, GPU management     |⚠️ Les deux                                 |

**Recommandation NovaSanté :** on-premise pour l’assistant RAG (données HDS) et le module fraude, cloud possible pour des cas d’usage à données non sensibles (génération de contenu marketing, assistance à la rédaction sans données personnelles).

-----

### Annexe F — Mapping de la bibliothèque

|Thématique                         |Cours IA & Sécurité|Cours complémentaires   |
|-----------------------------------|-------------------|------------------------|
|Threat model et gestion des risques|Ch.4, Ch.11        |Cours GRC               |
|Détection et monitoring            |Ch.15, Ch.17       |Cours SOC               |
|Réponse à incident                 |Ch.25              |Cours Incident Response |
|Sécurité applicative               |Ch.12, Ch.18       |Cours AppSec            |
|Supply chain                       |Ch.8               |Cours AppSec (SBOM, SCA)|
|Cadre réglementaire                |Ch.19, Ch.20, Ch.21|Cours GRC               |
|Menaces et attaques                |Ch.5-10, Ch.16     |Cours CTI, APT          |
|OSINT augmenté par IA              |Ch.16              |Cours OSINT             |
|Cryptographie et chiffrement       |Ch.12              |Cours Cryptographie     |
|Active Directory                   |Ch.9, Ch.23        |Cours Active Directory  |
|Infrastructure                     |Ch.12, Annexe D    |Cours Infrastructure IT |

Chaque cours de la bibliothèque est autonome mais s’enrichit mutuellement. Les renvois sont informatifs, pas créateurs de dépendance.

-----

### Annexe G — Ressources, formations et outils

#### Référentiels et guides

|Organisme|Publication                                                             |Lien / Référence                                                  |
|---------|------------------------------------------------------------------------|------------------------------------------------------------------|
|OWASP    |Top 10 for LLM Applications (v2025)                                     |owasp.org/www-project-top-10-for-large-language-model-applications|
|MITRE    |ATLAS (Adversarial Threat Landscape for AI Systems)                     |atlas.mitre.org                                                   |
|NIST     |AI Risk Management Framework (AI RMF)                                   |nist.gov/artificial-intelligence                                  |
|NIST     |AI 100-2 — Adversarial Machine Learning                                 |nist.gov (NIST AI 100-2e2023)                                     |
|ANSSI    |Recommandations de sécurité pour un système d’IA générative (avril 2024)|cyber.gouv.fr                                                     |
|ANSSI-BSI|Recommandations sur les assistants de programmation IA (octobre 2024)   |cyber.gouv.fr                                                     |
|ANSSI    |Développer la confiance dans l’IA par les risques cyber (février 2025)  |cyber.gouv.fr                                                     |
|ANSSI    |Synthèse CTI — IA et menaces (CERTFR-2026-CTI-001)                      |cert.ssi.gouv.fr                                                  |
|CNIL     |Recommandations IA et RGPD (fiches pratiques, juillet 2025)             |cnil.fr                                                           |
|ENISA    |Artificial Intelligence Cybersecurity Challenges                        |enisa.europa.eu                                                   |
|NCSC UK  |Guidelines for secure AI system development                             |ncsc.gov.uk                                                       |

#### Outils de sécurité IA

|Outil                   |Type                         |Usage                                   |Licence    |
|------------------------|-----------------------------|----------------------------------------|-----------|
|Garak (NVIDIA)          |Scanner de vulnérabilités LLM|Red teaming automatisé                  |Open source|
|Promptfoo               |Framework d’évaluation       |Tests systématiques des prompts/réponses|Open source|
|LLM Guard               |Guardrails                   |Filtrage entrées/sorties                |Open source|
|NeMo Guardrails (NVIDIA)|Guardrails                   |Framework de rails conversationnels     |Open source|
|Guardrails AI           |Validation de sorties        |Validation structurée des outputs LLM   |Open source|
|Protect AI              |Plateforme                   |Sécurité ML/IA complète                 |Commercial |
|Nightfall               |DLP IA                       |Détection PII/secrets dans les flux IA  |Commercial |
|Rebuff                  |Détection injection          |Détection de prompt injection           |Open source|

#### Formations et certifications

|Formation                                                |Organisme|Contenu                                                             |
|---------------------------------------------------------|---------|--------------------------------------------------------------------|
|SEC595 — Applied Data Science and AI/ML for Cybersecurity|SANS     |ML/IA appliqués à la cybersécurité — détection, analyse, red teaming|
|AI Security Fundamentals                                 |OWASP    |Sécurité des applications LLM                                       |
|Gandalf CTF                                              |Lakera   |CTF spécialisé prompt injection (entraînement pratique)             |
|HackAPrompt                                              |AICrowd  |Compétition de red teaming IA                                       |

#### Communautés et veille

|Ressource                          |Type                                      |
|-----------------------------------|------------------------------------------|
|OWASP AI Security and Privacy Guide|Guide communautaire maintenu              |
|MITRE ATLAS Community              |Communauté de praticiens                  |
|AI Village (DEF CON)               |Communauté de recherche en sécurité IA    |
|Publications ANSSI                 |Veille réglementaire et technique (France)|
|Publications CNIL — section IA     |Veille réglementaire données personnelles |
|ArXiv — cs.CR + cs.AI              |Publications de recherche                 |
|AI Incident Database               |Base de cas d’incidents IA documentés     |

-----

*Ce cours a été conçu pour être un document de référence opérationnel pour le professionnel de la cybersécurité confronté aux enjeux de l’IA en entreprise. Il reflète l’état de l’art à mi-2026 dans un domaine en évolution rapide — les outils, réglementations et techniques mentionnés doivent être réévalués régulièrement.*

*Les sources principales incluent les publications ANSSI (recommandations IA générative 2024, synthèse CTI 2026, étude IA pour le SOC 2026, guide ANSSI-BSI assistants de code 2024), les recommandations CNIL (fiches pratiques IA et RGPD 2025), le NIST AI 100-2 (Adversarial Machine Learning 2023), l’OWASP Top 10 for LLM, MITRE ATLAS, et l’ENISA (AI Cybersecurity Challenges).*
