---
title: Active Directory
source: IT/03 Active Directory/Active Directory.md
format: cours
revue: '2026-10-04'
revision: library/revision/active-directory.md
---

*Comprendre • Attaquer • Défendre • Répondre*

**Cours complet — 32 chapitres • 7 parties • 7 annexes**

*Architecture • Kerberos/NTLM • AD CS • BloodHound • Attaques • Détection • Hardening • IR • Hybrid*

---

### Fil rouge : Opération KERBEROS

> **Contexte narratif — ce fil rouge alterne entre perspective offensive et défensive tout au long du cours.**
>
> **Thomas Granier**, consultant senior en sécurité offensive chez **RedForge** (cabinet de pentest et réponse à incident, 30 personnes), est mandaté pour un **test d'intrusion interne** sur l'AD de **Meridian Pharma** — laboratoire pharmaceutique européen, 4 200 collaborateurs, 3 sites (siège Lyon, usine Strasbourg, R&D Genève), forêt AD mono-domaine (meridian.local), ~120 serveurs, ~3 500 postes, hybrid AD avec Entra ID (Azure AD Connect, PHS), AD CS déployé (PKI interne pour les certificats machines et VPN), 2 DC physiques au siège + 1 RODC sur le site de Genève.
>
> Thomas démarre avec un accès réseau standard (poste utilisateur joint au domaine, compte sans privilèges). Objectif : atteindre le Domain Admin, documenter chaque étape, et produire le rapport de pentest avec recommandations priorisées.
>
> En parallèle, la **Blue Team** de Meridian (SOC interne, 3 analystes) a pour mission de détecter l'intrusion et de pratiquer la réponse à incident.

---

## Sommaire

- [Partie I — Fondations](01-partie-i-fondations/index.md)
    - [Chapitre 1 — Active Directory](01-partie-i-fondations/01-chapitre-1-active-directory.md)
    - [Chapitre 2 — Architecture et composants](01-partie-i-fondations/02-chapitre-2-architecture-et-composants.md)
    - [Chapitre 3 — Objets, attributs et structure LDAP](01-partie-i-fondations/03-chapitre-3-objets-attributs-et-structure-ldap.md)
    - [Chapitre 4 — Autorisations, ACL et modèle de sécurité](01-partie-i-fondations/04-chapitre-4-autorisations-acl-et-modele-de-securite.md)
- [Partie II — Authentification](02-partie-ii-authentification/index.md)
    - [Avant les protocoles : LSASS et l'ouverture de session](02-partie-ii-authentification/01-avant-les-protocoles-lsass-et-l-ouverture-de-sessi.md)
    - [Chapitre 5 — NTLM : le protocole hérité qui refuse de disparaître](02-partie-ii-authentification/02-chapitre-5-ntlm-le-protocole-herite-qui-refuse-de.md)
    - [Chapitre 6 — Kerberos : le flux complet et les subtilités](02-partie-ii-authentification/03-chapitre-6-kerberos-le-flux-complet-et-les-subtili.md)
    - [Chapitre 7 — Où sont stockés les secrets et comment ils sont volés](02-partie-ii-authentification/04-chapitre-7-ou-sont-stockes-les-secrets-et-comment.md)
    - [Chapitre 8 — AD CS : PKI interne, certificats et surface d'attaque](02-partie-ii-authentification/05-chapitre-8-ad-cs-pki-interne-certificats-et-surfac.md)
- [Partie III — Administration et contrôle](03-partie-iii-administration-et-controle/index.md)
    - [Chapitre 9 — Group Policy (GPO) : configuration et sécurité](03-partie-iii-administration-et-controle/01-chapitre-9-group-policy-gpo-configuration-et-secur.md)
    - [Chapitre 10 — Outils d'administration et requêtage](03-partie-iii-administration-et-controle/02-chapitre-10-outils-d-administration-et-requetage.md)
    - [Chapitre 11 — Tiering model et séparation des privilèges](03-partie-iii-administration-et-controle/03-chapitre-11-tiering-model-et-separation-des-privil.md)
    - [Chapitre 12 — Journalisation et audit AD](03-partie-iii-administration-et-controle/04-chapitre-12-journalisation-et-audit-ad.md)
- [Partie IV — Attaques AD](04-partie-iv-attaques-ad.md)
- [Partie V — Détection](05-partie-v-detection.md)
- [Partie VI — Hardening](06-partie-vi-hardening.md)
- [Partie VII — Incident response, hybrid identity et synthèse](07-partie-vii-incident-response-hybrid-identity-et-sy.md)
- [Annexes](08-annexes.md)
