---
title: 'Annexe D — Architecture de référence : assistant RAG sécurisé'
source: Cyber/09 IA & sécurité/IA et sécurité.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Annexes
  - index.md
---

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
