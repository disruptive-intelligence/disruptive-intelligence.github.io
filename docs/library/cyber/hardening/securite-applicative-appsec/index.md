---
title: Sécurité applicative (AppSec)
source: Cyber/05 Hardening/Applications/Sécurité applicative (AppSec).md
format: cours
revue: '2026-04-08'
revision: library/revision/hardening.md
---

*Comprendre • Attaquer • Défendre • Détecter*

**Cours complet — 32 chapitres • 7 parties • 7 annexes**

*OWASP Top 10 (2025) • API Security • Supply Chain • LLM Security • DevSecOps • Détection • Programme AppSec*

---

### Fil rouge : SecureHealth

> **Contexte narratif — ce fil rouge traverse tout le cours et se conclut au Ch.29.**
>
> **SecureHealth**, startup healthtech française, 40 développeurs, 5 squads. Stack : Python/Django + React + API REST + PostgreSQL + AWS. Plateforme de suivi patient avec données de santé (hébergement HDS). L'équipe n'a jamais eu de référent sécurité. Un pentest externe vient de tomber : **14 vulnérabilités dont 3 critiques** — injection SQL sur la recherche de patients, IDOR sur les dossiers patients (accès au dossier de n'importe qui en changeant l'ID), clé API Stripe en dur dans le repo GitHub public.
>
> Le CTO réalise que « on s'en occupe après la v2 » n'est plus tenable. Le cours suit la transformation de l'équipe sur 12 mois : de la correction d'urgence au programme AppSec mature, en passant par la mise en place du pipeline DevSecOps, l'intégration d'un assistant médical AI, la migration vers Kubernetes, et la gestion d'un incident supply chain.

---

### Introduction

Ce cours enseigne la sécurité applicative comme une discipline complète — du code à la production, de l'attaque à la défense, de la vulnérabilité individuelle au programme d'entreprise.

L'AppSec ne s'arrête pas au secure coding. Elle couvre quatre dimensions indissociables : la **prévention** (threat modeling, secure coding, code review — empêcher les vulnérabilités de naître), la **vérification** (SAST, DAST, SCA, pentest — détecter les vulnérabilités avant l'attaquant), la **détection** (logging applicatif, monitoring, alerting, intégration SOC — voir les attaques en cours sur l'application en production), et la **gouvernance** (programme AppSec, métriques, Security Champions, formation continue — pérenniser la sécurité dans l'organisation). Les Parties I à V couvrent la prévention et la vérification. La Partie VI couvre la détection et la réponse. La Partie VII couvre la gouvernance et la synthèse.

---

## Sommaire

- [Partie I — Fondations](01-partie-i-fondations.md)
- [Partie II — Vulnérabilités web en profondeur](02-partie-ii-vulnerabilites-web-en-profondeur.md)
- [Partie III — Authentification et API](03-partie-iii-authentification-et-api.md)
- [Partie IV — Supply chain, IA et sécurité cloud-native](04-partie-iv-supply-chain-ia-et-securite-cloud-native.md)
- [Partie V — Tests, CI/CD et pipeline DevSecOps](05-partie-v-tests-ci-cd-et-pipeline-devsecops.md)
- [Partie VI — Protection runtime et détection](06-partie-vi-protection-runtime-et-detection.md)
- [Partie VII — Programme appsec et cas de synthèse](07-partie-vii-programme-appsec-et-cas-de-synthese.md)
- [Annexes](08-annexes.md)
