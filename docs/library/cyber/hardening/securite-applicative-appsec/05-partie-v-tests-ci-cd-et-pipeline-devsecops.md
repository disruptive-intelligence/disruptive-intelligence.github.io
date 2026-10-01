---
title: Partie V — Tests, CI/CD et pipeline DevSecOps
source: Cyber/05 Hardening/Sécurité applicative (AppSec).md
note: Sécurité applicative (AppSec)
up:
- - Sécurité applicative (AppSec)
  - index.md
---

---


## Chapitre 20 — Secure Code Review

La code review comme activité de sécurité : la review manuelle trouve ce que les outils manquent — failles de logique métier, erreurs d'autorisation subtiles, problèmes de conception. La méthodologie (quoi chercher en priorité) : entrées utilisateur non validées, requêtes SQL/NoSQL par concaténation, gestion des sessions et tokens (création, validation, invalidation), vérification d'autorisation manquante (l'endpoint vérifie-t-il que l'utilisateur a le droit ?), gestion des erreurs (stack traces exposées ? catch trop large ?), secrets dans le code (clés, tokens, credentials), utilisation de fonctions dangereuses (eval, exec, pickle.loads, innerHTML, dangerouslySetInnerHTML).

La checklist par type de PR : nouvelle fonctionnalité (threat modeling fait ?, input validation, output encoding, auth check, logging), modification d'API (autorisation vérifiée, validation du schéma, rate limiting, backward compatibility), mise à jour de dépendances (CVE connue ? changelog vérifié ? tests passés ?), changement d'infrastructure (secrets dans les manifests ? permissions trop larges ?). Les outils d'aide : Semgrep (règles custom — `rules: pattern: cursor.execute("..." + $VAR)` → détecte les raw queries par concaténation), CodeQL (analyse sémantique profonde).

---


## Chapitre 21 — SAST, DAST, SCA et tests automatisés

**SAST** (Static Application Security Testing — analyse le code source sans l'exécuter ; Semgrep — rapide, rules custom, open source, SonarQube — qualité + sécurité, CodeQL — analyse sémantique ; forces : trouve tôt, couvre tout le code ; faiblesses : faux positifs, ne voit pas les failles de logique). **DAST** (Dynamic Application Security Testing — teste l'application en cours d'exécution ; OWASP ZAP — open source référence, Burp Suite — l'outil du pentester, Nuclei — templates communautaires ; forces : trouve les vulnérabilités exploitables ; faiblesses : ne couvre que les endpoints atteints, plus lent). **SCA** (Software Composition Analysis — scanne les dépendances ; pip-audit, npm audit, Snyk, Dependabot, Trivy). **IAST** (Interactive AST — agent dans l'application, combine SAST et DAST, moins de faux positifs mais plus intrusif). La complémentarité : SAST + DAST + SCA ensemble couvrent plus que chacun seul.

---


## Chapitre 22 — CI/CD Security et pipeline DevSecOps

Le pipeline comme surface d'attaque (un pipeline compromis injecte du code malveillant dans chaque build). Les secrets dans le CI (gitleaks, truffleHog, detect-secrets — pré-commit hooks ; vault pour les secrets de production — HashiCorp Vault, AWS Secrets Manager). Le pipeline DevSecOps complet : pré-commit (secrets detection gitleaks), build (SAST Semgrep + SCA pip-audit), build Docker (scan image Trivy), test staging (DAST ZAP authentifié), deploy (policy check, signature cosign), runtime (monitoring, WAF, alerting). Les PR ne mergent pas si un finding critique est détecté. Le SBOM généré à chaque build (CycloneDX). La signature des artefacts (Sigstore/cosign — intégrité de la chaîne de production).

Le workflow de gestion des vulnérabilités : découverte → triage (vrai positif ?) → priorisation (SLA par sévérité : critique = 24h, élevé = 1 semaine, moyen = 1 mois) → correction → vérification → clôture. Les exceptions documentées avec justification et date de revue. Dashboard de suivi (Grafana, Jira).

> **🎯 SecureHealth — pipeline :** pré-commit gitleaks, CI Semgrep + pip-audit + Trivy, staging ZAP. Les PR ne mergent pas si critique. Dashboard : vulnérabilités ouvertes par sévérité, MTTR, couverture. Temps de correction : de « jamais » à 72h pour les critiques.

---


## Chapitre 23 — Pentest applicatif et bug bounty

La méthodologie de pentest applicatif (OWASP Testing Guide v4.2 — 12 catégories de tests). La reconnaissance (cartographie endpoints via OpenAPI/Swagger, technologies, versions). L'exploitation (ZAP, Burp Suite, sqlmap — pour chaque vulnérabilité du cours, l'outil de test). Le rapport (findings classés par criticité, preuve d'exploitation, impact, recommandation de correction).

Le **bug bounty** (HackerOne, YesWeHack — complète les tests internes avec des regards extérieurs). Prérequis : niveau de sécurité de base (sinon le volume de rapports est ingérable), processus de triage défini, budget, et règles du scope (ce qui est testable et ce qui ne l'est pas). Les programmes privés (invitation) vs publics (ouvert à tous). La coordination avec l'équipe de développement (le rapport d'un chercheur externe arrive → triage → validation → correction → rémunération → clôture).

---
