---
title: 'Ch.3 — Cas d’usage de l’IA en entreprise : cartographie et criticité'
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie I — Fondations IA pour le professionnel cyber
  - index.md
---

## 3.1 Cartographie par fonction métier

L’IA en entreprise ne se résume pas aux chatbots. Une cartographie réaliste des cas d’usage par fonction métier permet de comprendre les profils de risque et d’adapter les exigences de sécurité.

**Ressources humaines.** Le tri automatique de CV, le matching candidat-poste, l’analyse de sentiment dans les enquêtes internes. Le pattern technique dominant est le ML classique (classification, NLP) ou le RAG pour la recherche dans des référentiels de compétences. Le risque majeur est le biais discriminatoire — un modèle entraîné sur des historiques de recrutement peut reproduire et amplifier les biais existants (genre, origine, âge). L’AI Act classe explicitement les systèmes IA utilisés pour le recrutement et la gestion du personnel comme systèmes à haut risque (Annexe III), avec des obligations de conformité renforcées à compter d’août 2026.

**Finance et contrôle.** Le scoring de crédit, la détection de fraude, l’analyse prédictive de trésorerie, la conformité automatisée (KYC/AML). Le ML classique domine (gradient boosting, forêts aléatoires, réseaux de neurones pour la détection d’anomalies). Les enjeux : la fiabilité du scoring (un faux positif bloque un client légitime, un faux négatif laisse passer une fraude), l’explicabilité (le client ou le régulateur peut exiger une explication de la décision), et la conformité RGPD (article 22 sur les décisions automatisées). Le module de détection de fraude de NovaSanté relève directement de cette catégorie.

**Juridique.** L’analyse de contrats, la recherche jurisprudentielle, la rédaction d’actes. Le RAG est le pattern naturel (recherche dans des bases documentaires juridiques). Le risque principal est l’hallucination : un assistant juridique qui invente une jurisprudence ou interprète incorrectement une clause peut induire une erreur aux conséquences financières ou légales significatives. La vérification humaine est non négociable dans ce contexte.

**Support et relation client.** Chatbots, FAQ automatisées, analyse de tickets, routage intelligent. Le RAG pour les réponses contextuelles, les agents pour les actions (escalade, création de ticket). Le risque est la divulgation d’informations confidentielles via le chatbot (données d’autres clients, informations internes) et l’excessive agency si l’agent peut effectuer des actions sur les comptes clients.

**IT et cybersécurité.** Tri d’alertes SOC, détection d’anomalies (UEBA), analyse de malware, agent help desk, assistants de code. C’est le domaine où les deux mondes (ML classique pour la détection, IA générative pour l’analyse et l’assistance) coexistent le plus naturellement. Les enjeux spécifiques sont détaillés aux Ch.17 et Ch.18.

**Marketing et communication.** Génération de contenu, personnalisation, analyse de sentiment. Le risque est moindre en termes de sécurité SI mais significatif en termes de conformité (RGPD pour le profilage, droit d’auteur pour le contenu généré) et de réputation (contenu biaisé ou inapproprié).

## 3.2 Classification par criticité : informer, décider, agir

Au-delà de la fonction métier, la classification la plus opérationnelle pour le RSSI est celle qui distingue trois niveaux de criticité selon ce que fait l’IA.

**L’IA qui informe** (risque modéré) : elle fournit des données, des analyses, des suggestions. L’humain reste décideur et exécutant. Exemple : un assistant RAG qui résume des documents. En cas de défaillance (hallucination, injection), l’impact est limité si l’utilisateur vérifie. Le risque principal est la fuite de données via les réponses.

**L’IA qui décide** (risque élevé) : elle produit une décision qui influence directement un processus. Exemple : un scoring de fraude qui déclenche une alerte, un tri de CV qui élimine des candidats. En cas de défaillance, l’impact est direct sur des personnes ou des processus. Les risques incluent le biais, le manque d’explicabilité, et la conformité réglementaire (AI Act haut risque, RGPD article 22).

**L’IA qui agit** (risque très élevé) : elle exécute des actions sur le SI ou des systèmes métier. Exemple : un agent qui reset des mots de passe, crée des tickets, envoie des emails, modifie des données. En cas de défaillance ou de compromission, l’impact est immédiat et potentiellement irréversible. C’est le scénario de l’excessive agency. Les contrôles requis sont maximaux : moindre privilège, human-in-the-loop pour les actions critiques, allow-list, kill switch (voir Ch.9).

## 3.3 Erreurs courantes de déploiement

Plusieurs erreurs reviennent systématiquement dans les déploiements IA en entreprise. La première est l’absence de threat model spécifique : « c’est juste un chatbot » sous-estime les risques de fuite de données, d’injection, et d’impact réputationnel. La deuxième est le défaut de RBAC : les droits d’accès du système source ne sont pas reproduits dans le système IA (un utilisateur voit via l’IA des données auxquelles il n’a pas accès directement). La troisième est la surconfiance dans les guardrails du fournisseur : les filtres de sécurité des APIs commerciales sont conçus pour le grand public, pas pour protéger des données sensibles d’entreprise. La quatrième est l’absence de monitoring en production : pas de suivi des requêtes, des réponses, des coûts, des anomalies — ce qui rend la détection d’abus ou de compromission impossible.

-----
