---
title: Partie VII — Organisation, déploiement et perspectives
source: Cyber/09 IA & sécurité/IA et sécurité.md
note: IA et sécurité
up:
- - IA et sécurité
  - index.md
---

## Ch.26 — Déployer l’IA en entreprise

phases, gates, conduite du changement et overreliance

### 26.1 Le déploiement itératif

Le déploiement d’un système IA en entreprise suit un cycle itératif : cadrage (définition du besoin, évaluation de faisabilité, classification du risque), POC (preuve de concept technique — « est-ce que ça fonctionne ? »), pilote (test en conditions réelles avec un groupe restreint d’utilisateurs — « est-ce que ça fonctionne pour les utilisateurs ? »), production (déploiement complet avec monitoring — « est-ce que ça tient ? »), scaling (extension à d’autres équipes, cas d’usage adjacents), et run (exploitation continue, maintenance, mise à jour).

Chaque transition entre phases est une gate de sécurité (voir Ch.14). Le passage direct du POC à la production — fréquent dans les projets IA poussés par le COMEX — est une des principales causes d’incidents.

### 26.2 Overreliance et facteur humain

L’intégration de l’IA dans les processus métier modifie le comportement des utilisateurs de façon profonde et souvent sous-estimée.

**L’automation bias** fait que les utilisateurs tendent à suivre les recommandations de l’IA même quand elles sont manifestement incorrectes, simplement parce que « la machine l’a dit ». Pour le module de fraude de NovaSanté, cela signifie que les gestionnaires risquent de valider un scoring IA sans vérification, manquant des faux négatifs ou confirmant des faux positifs.

**La surconfiance dans les réponses** du RAG est le pendant de l’automation bias pour l’IA générative : le gestionnaire qui reçoit une réponse fluide et bien sourcée de l’assistant a tendance à la prendre pour argent comptant sans vérifier les sources citées. Si la réponse est une hallucination (ou pire, le résultat d’un RAG poisoning), l’absence de vérification humaine transforme une erreur IA en erreur métier.

**L’effondrement de la vigilance** se produit quand les utilisateurs, habitués à ce que l’IA fonctionne correctement 95 % du temps, cessent de vérifier systématiquement. Les 5 % restants — qui incluent les cas les plus critiques et les plus subtils — ne sont plus rattrapés.

**La fatigue de validation** est le risque associé au human-in-the-loop : si l’agent help desk demande une validation humaine pour chaque action AD, et que 99 % des actions sont légitimes, le validateur va finir par approuver automatiquement sans lire — annulant l’effet du contrôle.

**Le transfert de responsabilité implicite** se produit quand les utilisateurs considèrent que la responsabilité d’une décision a été transférée au système IA : « ce n’est pas moi qui ai décidé, c’est l’IA ». En réalité, l’utilisateur (et l’entreprise) restent responsables des décisions prises sur la base des sorties de l’IA.

Les contre-mesures incluent la formation explicite et répétée à la faillibilité de l’IA, la conception d’interfaces qui présentent les sorties IA comme des suggestions (pas des certitudes), la variation des tâches de validation (ne pas toujours les mêmes validateurs), les vérifications aléatoires par des superviseurs, et les métriques de qualité qui mesurent la capacité de détection humaine indépendante de l’IA.

### 26.3 Conduite du changement

L’IA modifie les processus, les rôles et les responsabilités. La résistance au changement est normale et doit être gérée activement. Les facteurs de succès incluent l’implication des utilisateurs dès le cadrage (pas de déploiement « top-down » sans consultation), la transparence sur les capacités et les limites de l’IA (ne pas survendre), la formation pratique (pas seulement théorique), le support dédié pendant la phase de transition, et les quick wins visibles (démontrer la valeur ajoutée rapidement pour créer l’adhésion).

-----


## Ch.27 — Construire une capacité de sécurité IA dans l’organisation

### 27.1 Les compétences nécessaires

La sécurité IA requiert des compétences à l’intersection de la cybersécurité et du ML/IA. Le RSSI doit comprendre les architectures IA (RAG, agents, MCP), les menaces spécifiques (prompt injection, data poisoning), et les cadres de référence (OWASP Top 10 for LLM, MITRE ATLAS) pour évaluer les risques et définir les contrôles. Le ML Engineer doit comprendre les principes de sécurité (moindre privilège, défense en profondeur, logging) pour concevoir des systèmes sûrs dès la conception. Le SOC doit être formé aux alertes spécifiques IA (injection détectée, fuite détectée, action agent bloquée) pour les traiter efficacement.

### 27.2 Formation et montée en compétence

Les formations de référence incluent SANS SEC595 (Applied Data Science and AI/Machine Learning for Cybersecurity Professionals), la certification OWASP sur la sécurité des LLMs, les CTF spécialisés IA security (Gandalf, HackAPrompt), et les formations internes (red teaming IA sur les systèmes de l’entreprise). La veille continue sur les publications ANSSI, NIST, ENISA, et les publications de recherche est indispensable dans un domaine qui évolue aussi rapidement.

### 27.3 L’articulation avec les équipes existantes

La sécurité IA n’est pas une équipe séparée — elle s’intègre dans les équipes existantes. L’équipe sécurité apporte l’expertise threat model, contrôles, monitoring, incident response. L’équipe data/ML apporte l’expertise technique IA et implémente les contrôles (RBAC vectoriel, sanitization, guardrails). L’équipe développement intègre les contrôles dans les pipelines CI/CD. Le métier valide la pertinence des résultats et assume la responsabilité de l’usage.

-----


## Ch.28 — Perspectives : évolution des menaces et de la défense

### 28.1 Agents IA de plus en plus autonomes

La tendance dominante est l’autonomisation croissante des agents IA. Les agents actuels exécutent des tâches unitaires (reset password, création de ticket). Les agents de demain orchestreront des workflows complets (diagnostic d’un incident, remédiation complète, communication aux parties prenantes). Le risque d’excessive agency augmente mécaniquement avec l’autonomie : plus l’agent peut faire de choses, plus les conséquences d’une manipulation sont graves. La défense doit évoluer en parallèle : les contrôles actuels (allow-list, human-in-the-loop) devront être complétés par des mécanismes d’évaluation de confiance en temps réel sur les actions de l’agent.

### 28.2 Modèles multimodaux

Les modèles qui traitent simultanément du texte, des images, de l’audio et de la vidéo ouvrent de nouvelles surfaces d’injection. Une image contenant une instruction cachée (stéganographie, texte dans les pixels), un audio avec des instructions dans les fréquences inaudibles, une vidéo avec un QR code flash — les vecteurs d’injection se multiplient au-delà du texte. Les défenses actuelles, très orientées texte, devront s’adapter.

### 28.3 IA embarquée (on-device)

L’exécution de modèles IA directement sur les terminaux (smartphones, laptops, objets connectés) pose de nouvelles questions de sécurité et de confidentialité. D’un côté, les données restent sur l’appareil (avantage vie privée). De l’autre, le modèle est directement accessible à l’attaquant qui a compromis le terminal (pas de protection périmétrique), et les mises à jour de sécurité du modèle sont plus difficiles à déployer.

### 28.4 Réglementation en durcissement

L’AI Act entre en application progressive jusqu’en 2027. D’autres juridictions développent leurs propres cadres. Les exigences de conformité vont se complexifier et s’uniformiser à l’international. La capacité à démontrer la conformité (documentation technique, AIPD, évaluations de risques, audits) deviendra un facteur différenciant.

### 28.5 Questions ouvertes

L’alignement (comment garantir qu’un modèle IA se comporte comme prévu dans tous les cas, y compris les cas non prévus ?) reste un problème ouvert. L’explicabilité (comment expliquer pourquoi le modèle a produit cette réponse ?) progresse mais reste difficile pour les modèles les plus complexes. La responsabilité juridique des décisions IA (qui est responsable quand l’IA se trompe — l’utilisateur ? l’entreprise ? le fournisseur du modèle ?) est en cours de clarification. Le droit d’effacement dans les poids d’un modèle (comment supprimer les données d’une personne des poids d’un modèle sans le ré-entraîner ?) est un défi technique et juridique ouvert.

-----
