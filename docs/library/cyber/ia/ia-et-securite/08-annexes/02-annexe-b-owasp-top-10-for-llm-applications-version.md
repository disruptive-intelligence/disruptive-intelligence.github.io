---
title: 'Annexe B — OWASP Top 10 for LLM Applications (Version 2025) et MITRE ATLAS : référence rapide'
source: Cyber/09 IA & sécurité/IA et sécurité.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Annexes
  - index.md
---

## OWASP Top 10 for LLM Applications — Nomenclature officielle Version 2025

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

## Mapping OWASP Top 10 2025 → Chapitres du cours

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

## MITRE ATLAS — Tactiques principales

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
