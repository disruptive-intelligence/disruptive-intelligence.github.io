---
title: Ch.10 — Shadow AI, disponibilité et risques organisationnels
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie II — Menaces spécifiques aux systèmes IA
  - index.md
---

## 10.1 Le shadow AI

Le shadow AI désigne l’utilisation non autorisée d’outils IA par les collaborateurs — typiquement ChatGPT, Claude, Gemini, ou des outils spécialisés (Copilot, Jasper, Midjourney) en version grand public, pour des tâches professionnelles impliquant des données de l’entreprise.

Le problème n’est pas l’IA en soi mais l’absence de contrôle : les données envoyées à ces services quittent le SI de l’entreprise, sont potentiellement stockées par le fournisseur, potentiellement utilisées pour l’entraînement, et transférées hors UE sans les garanties contractuelles (DPA article 28 du RGPD, clauses de transfert).

Le shadow AI est massif. Les études de 2024-2025 montrent que 60 à 80 % des collaborateurs en entreprise utilisent des outils IA grand public pour des tâches professionnelles, dont une proportion significative avec des données sensibles (contrats, données clients, code source, données financières). Le blocage pur (proxy bloquant les domaines des fournisseurs IA) est une réponse tentante mais contre-productive : les collaborateurs contournent (VPN personnels, appareils personnels, applications mobiles) et le blocage prive l’entreprise des gains de productivité réels de l’IA.

## 10.2 Stratégie de gestion en cinq niveaux

La stratégie la plus efficace combine cinq niveaux complémentaires.

**Niveau 1 — Détection.** Identifier le shadow AI existant via les logs proxy/firewall (requêtes vers api.openai.com, claude.ai, gemini.google.com), le DLP réseau, et les enquêtes utilisateurs. L’objectif n’est pas de sanctionner mais de quantifier le phénomène et d’identifier les cas d’usage réels.

**Niveau 2 — Alternative interne.** Fournir une solution IA interne cadrée et sécurisée qui couvre les cas d’usage légitimes identifiés. C’est la mesure la plus efficace : si les collaborateurs ont un outil IA interne qui fonctionne bien, la motivation à utiliser des outils non autorisés diminue considérablement. L’assistant RAG de NovaSanté joue ce rôle pour les gestionnaires de sinistres.

**Niveau 3 — Politique d’usage formalisée.** Rédiger et communiquer une politique claire : quels outils IA sont autorisés, quelles données peuvent y être envoyées (jamais de données personnelles, jamais de données classifiées, jamais de code propriétaire dans un LLM cloud non contractualisé), quelles vérifications sont obligatoires sur les résultats.

**Niveau 4 — Contrôle technique ciblé.** Bloquer l’accès aux services IA non autorisés pour les populations à risque (accès à des données sensibles) tout en laissant l’accès ouvert pour les populations à risque faible. Implémenter le DLP sur les requêtes sortantes vers les APIs IA pour détecter les envois de données sensibles.

**Niveau 5 — Sensibilisation continue.** Former les collaborateurs aux risques spécifiques du shadow AI (fuite de données, non-conformité RGPD, propriété intellectuelle), aux bons réflexes (anonymisation, vérification), et aux alternatives internes disponibles.

## 10.3 Risques de disponibilité

Au-delà du shadow AI, les systèmes IA introduisent des risques de disponibilité spécifiques.

**Le DoS par prompts complexes.** Un prompt particulièrement long ou complexe peut consommer une quantité disproportionnée de ressources GPU, dégradant le service pour les autres utilisateurs. Un attaquant peut exploiter ce vecteur pour rendre l’assistant indisponible. La défense : rate limiting par utilisateur, timeout sur les requêtes, limitation de la taille des prompts.

**L’épuisement des crédits.** Pour les services IA cloud (API OpenAI, Anthropic, etc.), un usage excessif — légitime ou malveillant — peut épuiser le budget alloué. La défense : alertes sur les seuils de consommation, quotas par utilisateur ou par application, monitoring des coûts en temps réel.

**La dépendance cloud.** Si l’IA est fournie par un service cloud unique (API OpenAI, par exemple), une panne du fournisseur impacte tous les systèmes qui en dépendent. La défense : architecture de fallback (modèle on-premise de secours, dégradation gracieuse — l’application fonctionne sans l’IA, même de façon réduite), et diversification des fournisseurs quand c’est pertinent.

> **🔵 Fil rouge — Épisode 8**
> Avant même le déploiement des trois cas d’usage IA officiels, Karim fait réaliser un audit shadow AI chez NovaSanté. Résultat : 85 % des gestionnaires de sinistres utilisent ChatGPT (version gratuite) pour résumer des dossiers de sinistre — y compris des dossiers contenant des données de santé. Trois managers utilisent Claude pour rédiger des notes de synthèse à partir de rapports médicaux. Le service juridique utilise Perplexity pour la recherche jurisprudentielle sur des cas impliquant des assurés nommément cités.
> 
> Karim présente les résultats au COMEX avec une analyse de risque : violation RGPD (transfert de données de santé vers les US sans DPA), violation potentielle de l’obligation HDS, et risque de notification à la CNIL si une fuite était avérée. Le COMEX valide immédiatement l’accélération du déploiement de l’assistant RAG interne comme alternative et la rédaction d’une politique d’usage IA.

-----
