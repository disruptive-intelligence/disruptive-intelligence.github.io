---
title: Infrastructure IT
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Infrastructure IT.md
format: cours
revue: '2026-04-08'
revision: library/revision/infrastructure.md
---

*Comprendre ce qu'on attaque et ce qu'on défend*

**Cours complet — 31 chapitres • 7 parties • 7 annexes**

*Réseau • Systèmes • Cloud • Identité • Données • Virtualisation • Hardening*

---

### Fil rouge : Opération BACKBONE

> **Contexte narratif — ce fil rouge traverse les 29 premiers chapitres et se conclut aux Ch.30-31.**
>
> **Lucas Moreira**, ingénieur sécurité chez **Stratosphere** (MSSP, 80 personnes), est mandaté pour l'audit d'infrastructure et le hardening du SI de **CargoPlex** — entreprise de logistique européenne, 2 500 collaborateurs, 8 entrepôts connectés, SI hybride (datacenter on-premise Lyon sur VMware vSphere + Azure + 3 SaaS critiques), ERP SAP, WMS (Warehouse Management System) connecté aux automates d'entrepôt, 150 sous-traitants transporteurs avec accès VPN, classée entité importante NIS 2.
>
> L'infrastructure de CargoPlex s'est construite par couches sur 15 ans :
>
> **Couche legacy :** Windows Server 2012 R2 toujours en production, SQL Server sur la même VM que l'ERP, flat network sans segmentation, vCenter avec mot de passe par défaut accessible depuis le réseau utilisateur, LDAP anonymous bind actif, NTP avec 3 sources différentes et 7 minutes d'écart entre les serveurs, interfaces iLO des serveurs physiques accessibles depuis le LAN utilisateur avec credentials par défaut, NAS de sauvegarde joint au domaine AD.
>
> **Couche de modernisation partielle :** migration Azure commencée mais non terminée (hybrid AD via Entra Connect, Exchange Online, quelques VMs Azure), AD Connect sur un serveur non durci.
>
> **Couche récente non maîtrisée :** 3 SaaS souscrits par les métiers sans validation IT, API transporteurs en HTTP sans authentification forte avec documentation Swagger exposée publiquement, containers Docker en développement sans registry privé, pipeline GitLab CI avec secrets en clair.
>
> Lucas doit cartographier l'infrastructure, identifier les vulnérabilités architecturales, prioriser le hardening, et construire la baseline de sécurité.

---

## Sommaire

- [Partie I — Réseau, protocoles et services fondamentaux](01-partie-i-reseau-protocoles-et-services-fondamentau/index.md)
    - [Chapitre 1 — Modèle client-serveur, TCP/IP et protocoles fondamentaux](01-partie-i-reseau-protocoles-et-services-fondamentau/01-chapitre-1-modele-client-serveur-tcp-ip-et-protoco.md)
    - [Chapitre 2 — Architecture réseau d'entreprise](01-partie-i-reseau-protocoles-et-services-fondamentau/02-chapitre-2-architecture-reseau-d-entreprise.md)
    - [Chapitre 3 — Sécurité réseau : firewalls, segmentation et détection](01-partie-i-reseau-protocoles-et-services-fondamentau/03-chapitre-3-securite-reseau-firewalls-segmentation.md)
    - [Chapitre 4 — Sécurité du Wi-Fi et des accès distants](01-partie-i-reseau-protocoles-et-services-fondamentau/04-chapitre-4-securite-du-wi-fi-et-des-acces-distants.md)
    - [Chapitre 5 — Bastion, PAM et Zero Trust](01-partie-i-reseau-protocoles-et-services-fondamentau/05-chapitre-5-bastion-pam-et-zero-trust.md)
    - [Chapitre 6 — Services d'infrastructure vitaux](01-partie-i-reseau-protocoles-et-services-fondamentau/06-chapitre-6-services-d-infrastructure-vitaux.md)
- [Partie II — Systèmes, virtualisation et hardening](02-partie-ii-systemes-virtualisation-et-hardening.md)
- [Partie III — Données, stockage, messagerie et transferts](03-partie-iii-donnees-stockage-messagerie-et-transfer.md)
- [Partie IV — Applications, web et API](04-partie-iv-applications-web-et-api.md)
- [Partie V — Identité et authentification](05-partie-v-identite-et-authentification.md)
- [Partie VI — Cloud, containers et architectures modernes](06-partie-vi-cloud-containers-et-architectures-modern.md)
- [Partie VII — Opérations, monitoring et cas de synthèse](07-partie-vii-operations-monitoring-et-cas-de-synthes.md)
- [Annexes](08-annexes.md)
