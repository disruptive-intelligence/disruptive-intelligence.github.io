---
title: Digital forensics
source: Cyber/03_Forensic/Digital_Forensics.md
format: cours
revue: '2026-04-08'
---

*Acquisition • Analyse • Preuve • Rapport*

**Cours complet — 33 chapitres • 8 parties • 6 annexes**

*Forensic judiciaire • Triage DFIR • Investigation numérique*

---

### Fil rouge : Opération MUSIC BOX

> **Contexte narratif — ce fil rouge traverse les 29 premiers chapitres du cours.**
>
> **Vendredi 7 mars 2026, 17h12.** L'EDR CrowdStrike Falcon déployé chez **NovaPharma** — laboratoire pharmaceutique français de 800 collaborateurs, spécialisé dans la recherche sur les molécules anticancéreuses, coté sur Euronext Growth — déclenche une alerte de sévérité « critique » : un processus `svchost.exe` avec un arbre de parenté anormal (parent : `explorer.exe` au lieu de `services.exe`) tente d'accéder au processus LSASS (Local Security Authority Subsystem Service) sur le poste de travail d'un chercheur du département R&D.
>
> L'analyste SOC, **Romain Vasquez**, qualifie l'alerte comme un vrai positif de gravité élevée : l'accès à LSASS est un indicateur classique de credential dumping (technique T1003 ATT&CK). Le poste n'est pas isolé immédiatement — Romain contacte d'abord l'IR lead, **Claire Desjardins**, pour cadrer la réponse.
>
> L'investigation forensic va progressivement révéler une compromission qui remonte à J-60 : un spearphishing ciblé avec un document Word piégé (macro VBA → téléchargement d'un RAT custom via certutil), une élévation de privilèges via Kerberoasting sur un compte de service avec droits Domain Admin, un mouvement latéral via PsExec et RDP vers le serveur R&D Linux (Ubuntu 22.04, données de recherche sur la molécule NP-427), une exfiltration de 180 Go de données R&D vers un bucket S3 AWS via rclone, des tentatives d'anti-forensics (timestomping sur les fichiers accédés, effacement partiel des Security Event Logs), et un RAT custom avec capacités de keylogging, screenshot, et file listing.
>
> L'enquête posera des questions méthodologiques à chaque chapitre : comment préserver la RAM avant que l'admin ne redémarre le poste, comment distinguer un svchost légitime d'un svchost injecté dans le dump mémoire, comment reconstituer la timeline de 60 jours de compromission, comment tracer le mouvement latéral entre Windows et Linux, comment identifier le Kerberoasting dans les Event Logs AD, comment prouver l'exfiltration via les logs proxy et AWS CloudTrail, comment détecter le timestomping par comparaison $STANDARD_INFORMATION/$FILE_NAME, et comment produire un rapport exploitable à la fois par le juge d'instruction et par le COMEX de NovaPharma.
>
> L'équipe forensic : Claire Desjardins (IR lead et forensicienne senior), Romain Vasquez (analyste SOC/forensic junior), et **Maître Élise Fournier** (experte judiciaire inscrite à la cour d'appel de Paris, mandatée dès le samedi pour sécuriser la chaîne de custody en vue d'une judiciarisation probable).

---

## Sommaire

- [Partie I — Fondations](01-partie-i-fondations/index.md)
    - [Chapitre 1 — Qu'est-ce que le digital forensics](01-partie-i-fondations/01-chapitre-1-qu-est-ce-que-le-digital-forensics.md)
    - [Chapitre 2 — Cadre juridique et recevabilité de la preuve](01-partie-i-fondations/02-chapitre-2-cadre-juridique-et-recevabilite-de-la-p.md)
    - [Chapitre 3 — Méthodologie forensic et posture d'enquêteur](01-partie-i-fondations/03-chapitre-3-methodologie-forensic-et-posture-d-enqu.md)
    - [Chapitre 4 — Environnement technique et outils fondamentaux](01-partie-i-fondations/04-chapitre-4-environnement-technique-et-outils-fonda.md)
- [Partie II — Acquisition de preuves](02-partie-ii-acquisition-de-preuves/index.md)
    - [Chapitre 5 — Acquisition disque et supports de stockage](02-partie-ii-acquisition-de-preuves/01-chapitre-5-acquisition-disque-et-supports-de-stock.md)
    - [Chapitre 6 — Acquisition mémoire vive (RAM)](02-partie-ii-acquisition-de-preuves/02-chapitre-6-acquisition-memoire-vive-ram.md)
    - [Chapitre 7 — Acquisition réseau et captures de trafic](02-partie-ii-acquisition-de-preuves/03-chapitre-7-acquisition-reseau-et-captures-de-trafi.md)
    - [Chapitre 8 — Acquisition des logs, des données d'identité et du cloud](02-partie-ii-acquisition-de-preuves/04-chapitre-8-acquisition-des-logs-des-donnees-d-iden.md)
- [Partie III — Analyse fondamentale ET raisonnement forensic](03-partie-iii-analyse-fondamentale-et-raisonnement-fo/index.md)
    - [Chapitre 9 — Systèmes de fichiers : comprendre ce qu'on analyse](03-partie-iii-analyse-fondamentale-et-raisonnement-fo/01-chapitre-9-systemes-de-fichiers-comprendre-ce-qu-o.md)
    - [Chapitre 10 — Timeline analysis et corrélation temporelle](03-partie-iii-analyse-fondamentale-et-raisonnement-fo/02-chapitre-10-timeline-analysis-et-correlation-tempo.md)
    - [Chapitre 11 — Corrélation, raisonnement analytique et gestion des biais](03-partie-iii-analyse-fondamentale-et-raisonnement-fo/03-chapitre-11-correlation-raisonnement-analytique-et.md)
- [Partie IV — Analyse forensic avancée](04-partie-iv-analyse-forensic-avancee/index.md)
    - [Chapitre 12 — Windows forensics : registre et artefacts d'exécution](04-partie-iv-analyse-forensic-avancee/01-chapitre-12-windows-forensics-registre-et-artefact.md)
    - [Chapitre 13 — Windows forensics](04-partie-iv-analyse-forensic-avancee/02-chapitre-13-windows-forensics.md)
    - [Chapitre 14 — Windows forensics : Event Logs et journaux d'audit](04-partie-iv-analyse-forensic-avancee/03-chapitre-14-windows-forensics-event-logs-et-journa.md)
    - [Chapitre 15 — Linux forensics](04-partie-iv-analyse-forensic-avancee/04-chapitre-15-linux-forensics.md)
    - [Chapitre 16 — macOS forensics](04-partie-iv-analyse-forensic-avancee/05-chapitre-16-macos-forensics.md)
    - [Chapitre 17 — Memory forensics](04-partie-iv-analyse-forensic-avancee/06-chapitre-17-memory-forensics.md)
    - [Chapitre 18 — Malware forensics](04-partie-iv-analyse-forensic-avancee/07-chapitre-18-malware-forensics.md)
- [Partie V — Investigation réseau ET identité](05-partie-v-investigation-reseau-et-identite/index.md)
    - [Chapitre 19 — Network forensics](05-partie-v-investigation-reseau-et-identite/01-chapitre-19-network-forensics.md)
    - [Chapitre 20 — Active Directory forensics](05-partie-v-investigation-reseau-et-identite/02-chapitre-20-active-directory-forensics.md)
    - [Chapitre 21 — Investigation des identités hybrides, du cloud et des accès distants](05-partie-v-investigation-reseau-et-identite/03-chapitre-21-investigation-des-identites-hybrides-d.md)
- [Partie VI — Forensic spécialisé](06-partie-vi-forensic-specialise.md)
- [Partie VII — Finalisation ET production](07-partie-vii-finalisation-et-production.md)
- [Partie VIII — Application ET synthèse](08-partie-viii-application-et-synthese.md)
- [Annexes](09-annexes/index.md)
    - [Annexe A — Glossaire forensic](09-annexes/01-annexe-a-glossaire-forensic.md)
    - [Annexe B — Cheat sheets outils](09-annexes/02-annexe-b-cheat-sheets-outils.md)
    - [Annexe C — Artefacts Windows : référence rapide](09-annexes/03-annexe-c-artefacts-windows-reference-rapide.md)
    - [Annexe D — Artefacts Linux et macOS : référence rapide](09-annexes/04-annexe-d-artefacts-linux-et-macos-reference-rapide.md)
    - [Annexe E — Templates](09-annexes/05-annexe-e-templates.md)
    - [Annexe F — Ressources et certifications](09-annexes/06-annexe-f-ressources-et-certifications.md)
- [Questions essentielles](10-questions-essentielles.md)
- [Réponses flash](11-reponses-flash.md)
