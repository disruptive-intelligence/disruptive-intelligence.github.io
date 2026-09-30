---
title: 'Fil rouge : Opération MUSIC BOX'
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
chapter: 1
chapters: 9
---

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
