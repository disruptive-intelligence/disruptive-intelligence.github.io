---
title: IA et sécurité
source: Cyber/05_Cyberdefense/IA_Secu.md
format: cours
revue: '2026-04-15'
---

**Cours expert — 28 chapitres · 7 parties · 7 annexes**
**Version 2025-2026 — État de l’art**

-----

> **Fil rouge — Opération CORTEX**
> NovaSanté, mutuelle régionale (1 200 collaborateurs, DSI de 35 personnes, SOC externalisé chez un MSSP). Le COMEX veut déployer l’IA « partout » après avoir vu les gains chez les concurrents. La DSI et le RSSI doivent cadrer, sécuriser et déployer trois cas d’usage IA en douze mois :
> 
> 1. **Assistant RAG interne** pour 80 gestionnaires de sinistres (recherche dans la base documentaire — règlements, jurisprudence, procédures, historique). Données de santé (HDS). On-premise obligatoire.
> 1. **Module IA de détection de fraude** dans le SIEM (scoring des déclarations suspectes). ML classique + enrichissement LLM.
> 1. **Agent IA help desk IT** (reset de mot de passe, création de tickets, FAQ interne). Premier cas où l’IA **agit** sur le SI.
> 
> Le fil rouge suit **Karim** (38 ans, CISSP, passé par le SOC puis la GRC), RSSI de NovaSanté, qui doit évaluer les risques, définir la politique, sécuriser les déploiements, former les équipes, gérer un incident et arbitrer la montée en puissance de l’agent IA.

-----

## Sommaire

- [Partie I — Fondations IA pour le professionnel cyber](01-partie-i-fondations-ia-pour-le-professionnel-cyber/index.md)
    - [Ch.1 — Intelligence artificielle : concepts fondamentaux](01-partie-i-fondations-ia-pour-le-professionnel-cyber/01-ch-1-intelligence-artificielle-concepts-fondamenta.md)
    - [Ch.2 — RAG, fine-tuning et agents : les architectures de déploiement](01-partie-i-fondations-ia-pour-le-professionnel-cyber/02-ch-2-rag-fine-tuning-et-agents-les-architectures-d.md)
    - [Ch.3 — Cas d’usage de l’IA en entreprise : cartographie et criticité](01-partie-i-fondations-ia-pour-le-professionnel-cyber/03-ch-3-cas-dusage-de-lia-en-entreprise-cartographie.md)
    - [Ch.4 — Modèle de menaces d’un système IA](01-partie-i-fondations-ia-pour-le-professionnel-cyber/04-ch-4-modele-de-menaces-dun-systeme-ia.md)
- [Partie II — Menaces spécifiques aux systèmes IA](02-partie-ii-menaces-specifiques-aux-systemes-ia/index.md)
    - [Ch.5 — Prompt injection : directe et indirecte](02-partie-ii-menaces-specifiques-aux-systemes-ia/01-ch-5-prompt-injection-directe-et-indirecte.md)
    - [Ch.6 — Fuite de données et exfiltration via l’IA](02-partie-ii-menaces-specifiques-aux-systemes-ia/02-ch-6-fuite-de-donnees-et-exfiltration-via-lia.md)
    - [Ch.7 — Data poisoning, RAG poisoning, intégrité des données et attaques sur le ML classique](02-partie-ii-menaces-specifiques-aux-systemes-ia/03-ch-7-data-poisoning-rag-poisoning-integrite-des-do.md)
    - [Ch.8 — Supply chain IA : modèles, dépendances et datasets](02-partie-ii-menaces-specifiques-aux-systemes-ia/04-ch-8-supply-chain-ia-modeles-dependances-et-datase.md)
    - [Ch.9 — Agents IA et excessive agency : quand l’IA agit sur le SI](02-partie-ii-menaces-specifiques-aux-systemes-ia/05-ch-9-agents-ia-et-excessive-agency-quand-lia-agit.md)
    - [Ch.10 — Shadow AI, disponibilité et risques organisationnels](02-partie-ii-menaces-specifiques-aux-systemes-ia/06-ch-10-shadow-ai-disponibilite-et-risques-organisat.md)
- [Partie III — Sécuriser le déploiement](03-partie-iii-securiser-le-deploiement/index.md)
    - [Ch.11 — Politique d’usage IA et gouvernance](03-partie-iii-securiser-le-deploiement/01-ch-11-politique-dusage-ia-et-gouvernance.md)
    - [Ch.12 — Contrôles techniques](03-partie-iii-securiser-le-deploiement/02-ch-12-controles-techniques.md)
    - [Ch.13 — Sécuriser le RAG : sources, RBAC vectoriel et sanitization](03-partie-iii-securiser-le-deploiement/03-ch-13-securiser-le-rag-sources-rbac-vectoriel-et-s.md)
    - [Ch.14 — Guardrails, red teaming, tests de sécurité IA et gates de validation](03-partie-iii-securiser-le-deploiement/04-ch-14-guardrails-red-teaming-tests-de-securite-ia.md)
    - [Ch.15 — Observabilité, monitoring et intégration SIEM](03-partie-iii-securiser-le-deploiement/05-ch-15-observabilite-monitoring-et-integration-siem.md)
- [Partie IV — IA offensive et défensive](04-partie-iv-ia-offensive-et-defensive/index.md)
    - [Ch.16 — L’IA comme outil d’attaque : menaces augmentées par l’IA](04-partie-iv-ia-offensive-et-defensive/01-ch-16-lia-comme-outil-dattaque-menaces-augmentees.md)
    - [Ch.17 — L’IA au service de la cybersécurité : potentiel et limites](04-partie-iv-ia-offensive-et-defensive/02-ch-17-lia-au-service-de-la-cybersecurite-potentiel.md)
    - [Ch.18 — Le code AI-generated : risques et gouvernance](04-partie-iv-ia-offensive-et-defensive/03-ch-18-le-code-ai-generated-risques-et-gouvernance.md)
- [Partie V — Conformité et cadre juridique](05-partie-v-conformite-et-cadre-juridique/index.md)
    - [Ch.19 — RGPD et traitements IA](05-partie-v-conformite-et-cadre-juridique/01-ch-19-rgpd-et-traitements-ia.md)
    - [Ch.20 — AI Act : classification, obligations et mise en conformité](05-partie-v-conformite-et-cadre-juridique/02-ch-20-ai-act-classification-obligations-et-mise-en.md)
    - [Ch.21 — Propriété intellectuelle, secret des affaires, contrats fournisseurs et articulation NIS2/DORA/HDS](05-partie-v-conformite-et-cadre-juridique/03-ch-21-propriete-intellectuelle-secret-des-affaires.md)
- [Partie VI — Cas de synthèse](06-partie-vi-cas-de-synthese/index.md)
    - [Ch.22 — Cas complet](06-partie-vi-cas-de-synthese/01-ch-22-cas-complet.md)
    - [Ch.23 — Cas complet : sécurisation d’un agent IA help desk](06-partie-vi-cas-de-synthese/02-ch-23-cas-complet-securisation-dun-agent-ia-help-d.md)
    - [Ch.24 — Cas complet](06-partie-vi-cas-de-synthese/03-ch-24-cas-complet.md)
    - [Ch.25 — Cas complet : réponse à incident IA](06-partie-vi-cas-de-synthese/04-ch-25-cas-complet-reponse-a-incident-ia.md)
- [Partie VII — Organisation, déploiement et perspectives](07-partie-vii-organisation-deploiement-et-perspective.md)
- [Annexes](08-annexes/index.md)
    - [Annexe A — Glossaire IA & SSI (60+ termes)](08-annexes/01-annexe-a-glossaire-ia-ssi-60-termes.md)
    - [Annexe B — OWASP Top 10 for LLM Applications (Version 2025) et MITRE ATLAS : référence rapide](08-annexes/02-annexe-b-owasp-top-10-for-llm-applications-version.md)
    - [Annexe C — Checklists réutilisables](08-annexes/03-annexe-c-checklists-reutilisables.md)
    - [Annexe D — Architecture de référence : assistant RAG sécurisé](08-annexes/04-annexe-d-architecture-de-reference-assistant-rag-s.md)
    - [Annexe E — Matrice de décision cloud vs on-premise vs hybride](08-annexes/05-annexe-e-matrice-de-decision-cloud-vs-on-premise-v.md)
    - [Annexe F — Mapping de la bibliothèque](08-annexes/06-annexe-f-mapping-de-la-bibliotheque.md)
    - [Annexe G — Ressources, formations et outils](08-annexes/07-annexe-g-ressources-formations-et-outils.md)
