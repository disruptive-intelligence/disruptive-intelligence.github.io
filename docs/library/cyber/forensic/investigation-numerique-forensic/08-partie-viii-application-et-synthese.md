---
title: Partie VIII — Application et synthèse
source: Cyber/04 Forensic/Investigation numérique (forensic).md
note: Investigation numérique (forensic)
up:
- - Investigation numérique (forensic)
  - index.md
---

*Cette partie est un atelier de synthèse : 4 cas complets qui appliquent l'intégralité de la méthodologie forensic sur des types d'incidents distincts. Chaque cas suit le processus complet : identification → préservation → acquisition → analyse → rapport.*

---


## Chapitre 30 — Cas complet : compromission Windows avec mouvement latéral et exfiltration

Synthèse du fil rouge MUSIC BOX sous forme de cas autonome. Du spearphishing initial (J-60) au rapport final, en passant par le dump RAM, le triage KAPE, l'image disque, l'analyse mémoire (process hollowing, credentials en mémoire), l'analyse des artefacts d'exécution (Prefetch, Amcache, SRUM confirmant l'exfiltration), la détection du mouvement latéral (PsExec traces, RDP traces, SSH vers le serveur Linux), l'investigation AD (Kerberoasting, DCSync), la détection de l'anti-forensics (timestomping, log clearing), et la production du rapport pour le juge et le COMEX. La timeline unifiée de 60 jours est le livrable central.


## Chapitre 31 — Cas complet : investigation insider threat

Un chercheur senior de NovaPharma annonce son départ pour un concurrent. Trois semaines après son départ, un audit DLP révèle : 45 Go de documentation de recherche copiée sur une clé USB personnelle dans les 10 jours précédant le départ, et un upload de 12 Go vers un compte Google Drive personnel depuis le réseau d'entreprise.

L'investigation forensic du poste (Windows 11) utilise les artefacts USB (registre USBSTOR, SetupAPI logs — identification du modèle et du numéro de série de la clé USB, dates de connexion), les ShellBags (navigation dans les dossiers de recherche confidentielle), les LNK files (fichiers ouverts depuis la clé USB), le navigateur Chrome (historique de connexion à Google Drive, volumes uploadés — confirmés par les logs proxy), et le SRUM (confirmation du volume de données transférées par Chrome vers Google Drive).

Spécificités de l'investigation insider : droit du travail (la charte informatique autorise-t-elle l'usage personnel de clés USB ?), RGPD (les données copiées contiennent-elles des données personnelles de patients d'essais cliniques ?), et procédure disciplinaire/pénale (les preuves doivent être exploitables devant les prud'hommes ET potentiellement devant le tribunal correctionnel pour vol de secrets de fabrication — article L.1227-1 du Code du travail). Le rapport est rédigé en deux versions : une pour le DRH (procédure disciplinaire) et une pour l'avocat (procédure pénale).


## Chapitre 32 — Cas complet : investigation serveur Linux compromis

Un serveur web exposé sur Internet (Ubuntu 22.04, Apache, application PHP interne) est compromis via une vulnérabilité d'injection SQL dans l'application. L'attaquant a obtenu un shell via un webshell PHP, escaladé ses privilèges via un exploit kernel local, et déployé un cryptominer.

L'investigation Linux : logs Apache (identification de la requête d'injection SQL initiale, accès au webshell), auth.log (tentatives de su, sudo, escalade de privilèges), bash_history (commandes de l'attaquant — reconnaissance, téléchargement du cryptominer, installation du crontab de persistance), crontab (le cryptominer est relancé toutes les 5 minutes), analyse du webshell PHP (code obfusqué, capacités de commande), et analyse du binaire cryptominer (IoC, pool de mining, wallet — pour estimer les revenus de l'attaquant).

Spécificités : pas d'EDR sur le serveur (l'investigation repose entièrement sur les logs système et les artefacts du système de fichiers), logs limités (auth.log rotaîne à 4 fichiers, les logs les plus anciens sont perdus), et reconstruction à partir d'artefacts fragiles (l'attaquant a supprimé son bash_history, mais des fragments sont récupérés dans le swap par recherche de strings).


## Chapitre 33 — Cas complet : compromission AD et identités hybrides cloud

Un groupe hospitalier français (3 sites, 2 000 utilisateurs, AD synchronisé avec Microsoft 365 E3 via Azure AD Connect) est victime d'une compromission qui commence par un phishing sur M365 (token volé via un kit AitM — Adversary-in-the-Middle), pivot vers l'AD on-premise (l'attaquant utilise le token pour accéder à Azure AD Connect et obtenir les credentials de synchronisation), puis Golden Ticket sur l'AD on-premise (DCSync → forge de TGT), et enfin accès aux données de santé des patients via l'application métier hospitalière.

L'investigation combine forensic cloud (UAL M365 — identification du phishing initial et du token volé, Sign-in Logs — détection du MFA bypass par le kit AitM), forensic AD (Event Logs DC — DCSync détecté via 4662, Golden Ticket détecté via anomalies Kerberos, ADTimeline — modifications d'objets), et forensic endpoint (analyse du serveur Azure AD Connect — extraction de la configuration de synchronisation et des credentials stockées par le connecteur).

Ce cas illustre la complexité croissante des investigations dans les environnements hybrides : l'attaquant pivote entre le cloud et l'on-premise en exploitant les mécanismes de synchronisation qui, par design, font le pont entre les deux mondes. L'investigation doit couvrir les deux environnements de manière intégrée, pas séparée.

---
