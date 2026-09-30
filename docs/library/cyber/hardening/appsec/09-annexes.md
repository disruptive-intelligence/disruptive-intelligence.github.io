---
title: Annexes
source: IT/03_Networking/AppSec.md
note: AppSec
up:
- - AppSec
  - index.md
---

---


#### Annexe A — Glossaire AppSec

| Terme | Définition |
|-------|-----------|
| **ABAC** | Attribute-Based Access Control — contrôle d'accès par attributs |
| **ASVS** | Application Security Verification Standard (OWASP) |
| **BOLA** | Broken Object Level Authorization (API Top 10) |
| **CORS** | Cross-Origin Resource Sharing |
| **CSP** | Content Security Policy |
| **CSRF** | Cross-Site Request Forgery |
| **DAST** | Dynamic Application Security Testing |
| **DFD** | Data Flow Diagram (threat modeling) |
| **HSTS** | HTTP Strict Transport Security |
| **IDOR** | Insecure Direct Object Reference |
| **IAST** | Interactive Application Security Testing |
| **JWT** | JSON Web Token |
| **LLM** | Large Language Model |
| **Mass assignment** | Injection de champs non prévus via l'API |
| **mTLS** | Mutual TLS — authentification mutuelle par certificat |
| **OWASP** | Open Web Application Security Project |
| **PKCE** | Proof Key for Code Exchange (OAuth) |
| **RAG** | Retrieval-Augmented Generation (IA) |
| **RASP** | Runtime Application Self-Protection |
| **RBAC** | Role-Based Access Control |
| **SAMM** | Software Assurance Maturity Model (OWASP) |
| **SAST** | Static Application Security Testing |
| **SBOM** | Software Bill of Materials |
| **SCA** | Software Composition Analysis |
| **SOP** | Same-Origin Policy |
| **SSRF** | Server-Side Request Forgery |
| **SSTI** | Server-Side Template Injection |
| **STRIDE** | Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation |
| **TOCTOU** | Time of Check to Time of Use (race condition) |
| **WAF** | Web Application Firewall |
| **WebAuthn** | Web Authentication API (passkeys) |
| **XSS** | Cross-Site Scripting |

---


#### Annexe B — OWASP Top 10 (2025) et API Top 10 (2023) : référence rapide

| # | OWASP Top 10 2025 | Chapitre |
|---|------------------|---------|
| A01 | Broken Access Control | Ch.7 |
| A02 | Cryptographic Failures | Ch.9 |
| A03 | Injection | Ch.6 |
| A04 | Insecure Design | Ch.5 (Threat Modeling) |
| A05 | Security Misconfiguration | Ch.15 |
| A06 | Vulnerable and Outdated Components | Ch.15, Ch.16 |
| A07 | Identification and Authentication Failures | Ch.13 |
| A08 | Software and Data Integrity Failures | Ch.16 (Supply Chain) |
| A09 | Security Logging and Monitoring Failures | Ch.25 |
| A10 | Server-Side Request Forgery | Ch.11 |

| # | API Top 10 2023 | Chapitre |
|---|----------------|---------|
| API1 | Broken Object Level Authorization (BOLA) | Ch.7, Ch.14 |
| API2 | Broken Authentication | Ch.13 |
| API3 | Broken Object Property Level Authorization (BOPLA) | Ch.14 (mass assignment) |
| API4 | Unrestricted Resource Consumption | Ch.14 (rate limiting) |
| API5 | Broken Function Level Authorization (BFLA) | Ch.7 |
| API6 | SSRF | Ch.11 |
| API7 | Security Misconfiguration | Ch.15 |
| API8 | Lack of Protection from Automated Threats | Ch.14, Ch.24 |
| API9 | Improper Inventory Management | Ch.14 (versioning) |
| API10 | Unsafe Consumption of APIs | Ch.16 (supply chain) |

---


#### Annexe C — Cheat sheets par langage/framework

| Langage/Framework | Input Validation | Output Encoding | Auth | Query | File Upload |
|------------------|-----------------|----------------|------|-------|-------------|
| **Python/Django** | Django Forms, DRF Serializers | Template auto-escaping | Django auth, django-allauth | ORM (pas raw queries) | Rename UUID, S3, scan AV |
| **JS/Node/Express** | express-validator, Joi | DOMPurify (client), template escaping (server) | Passport.js, express-session | Sequelize/Prisma ORM | multer + rename + S3 |
| **Java/Spring** | Bean Validation (@Valid) | Thymeleaf auto-escaping | Spring Security | JPA/Hibernate | MultipartFile + rename + scan |

---


#### Annexe D — Pipeline DevSecOps : template

```
PRE-COMMIT
  └── gitleaks (secrets detection)

BUILD
  ├── Semgrep (SAST — rules custom + OWASP)
  ├── pip-audit / npm audit (SCA)
  └── Trivy (scan image Docker)

TEST (staging)
  └── OWASP ZAP (DAST authentifié)

DEPLOY
  ├── Policy check (OPA/Kyverno)
  ├── cosign verify (signature artefact)
  └── SBOM generate (CycloneDX)

RUNTIME
  ├── WAF (AWS WAF / Cloudflare)
  ├── Logging structuré (Datadog / ELK)
  └── Alerting (patterns de détection Ch.25)

GATE : PR ne merge pas si finding critique SAST/SCA/DAST
```


---


#### Annexe E — Checklist de code review sécurité

| Type de PR | Points à vérifier |
|-----------|------------------|
| **Nouvelle fonctionnalité** | Threat modeling fait ? Input validation ? Output encoding ? Auth check sur chaque endpoint ? Logging des actions sensibles ? |
| **Modification API** | Autorisation vérifiée ? Validation schéma ? Rate limiting ? Mass assignment bloqué ? Backward compatible ? |
| **Update dépendances** | CVE connue ? Changelog vérifié ? Tests passés ? Lockfile mis à jour avec hashes ? |
| **Changement infra** | Secrets dans les manifests ? Permissions IAM minimales ? Network policies ? Pod security ? |
| **Intégration LLM** | Input sanitization avant LLM ? Output encoding après LLM ? RAG filtré par user ? Moindre privilège actions ? Logging prompts ? |

---


#### Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Ce cours (AppSec) |
|-----------|----------------|-------------------|
| Détection SOC | **Cours SOC** | Ch.25 — logging applicatif alimente le SOC |
| Incident Response | **Cours IR** | Ch.26 — forensic et IR web |
| Infrastructure | **Cours Infra** | Ch.18 — sécurité d'exécution cloud-native |
| Active Directory | **Cours AD** | Ch.13 — authentification domaine |
| GRC | **Cours GRC** | Ch.27 — conformité données (RGPD, HDS, PCI) |
| CTI | **Cours CTI** | Ch.16 — supply chain compromise (indicateurs) |
| APT | **Cours APT** | Ch.16 — SolarWinds, XZ Utils comme cas APT |

---


#### Annexe G — Ressources, formations et lab

##### Formations

| Formation | Organisme | Focus |
|-----------|----------|-------|
| PortSwigger Web Security Academy | PortSwigger | Gratuit, interactif — LA meilleure ressource |
| SANS SEC522 | SANS | Application Security |
| SANS SEC542 | SANS | Web App Penetration Testing |
| eWPT | INE | Web App Penetration Testing (pratique) |
| HTB CWEE | HackTheBox | Certified Web Exploitation Expert |

##### Outils

| Outil | Type | Usage |
|-------|------|-------|
| Burp Suite | Proxy/DAST | Pentest web — l'outil de référence |
| OWASP ZAP | DAST | Scan automatisé — open source |
| Semgrep | SAST | Analyse statique — rules custom |
| Trivy | SCA/Container | Scan dépendances + images Docker |
| gitleaks | Secrets | Détection de secrets dans le code |
| OWASP WebGoat | Lab | Application vulnérable pour apprendre |
| OWASP Juice Shop | Lab | Application vulnérable moderne (SPA+API) |
| sqlmap | Exploitation | Injection SQL automatisée |
| Nuclei | DAST | Templates de scan communautaires |

##### Lab

OWASP Juice Shop (application vulnérable moderne — SPA + API REST + Node.js — 100+ challenges classés par difficulté), OWASP WebGoat (exercices guidés par vulnérabilité), PortSwigger Labs (exercices interactifs dans le navigateur — gratuit), Burp Suite Community Edition, et un pipeline CI/CD local (GitHub Actions ou GitLab CI + Semgrep + ZAP + Trivy).

---

---


## Annexe — Questions types d'entretien et réponses types
