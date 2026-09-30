---
title: 'Chapitre 14 — Windows forensics : Event Logs et journaux d''audit'
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - ../index.md
- - Partie IV — Analyse forensic avancée
  - index.md
---

*Ce chapitre est le référentiel de l'interprétation des Event Logs Windows pour le forensic. Il ne répète pas les artefacts de registre (Ch.12) ni les artefacts d'activité utilisateur (Ch.13) — il se concentre sur ce que les journaux d'audit racontent, comment les lire, et comment les corréler.*

## 14.1 Architecture des Event Logs Windows

Les Event Logs Windows sont stockés au format `.evtx` (XML binaire) dans `C:\Windows\System32\winevt\Logs\`. Chaque fichier correspond à un canal (channel) : `Security.evtx` (authentification, audit de sécurité — la source la plus importante pour le forensic), `System.evtx` (services, pilotes, erreurs système), `Application.evtx` (événements applicatifs), et de nombreux canaux spécialisés (`Microsoft-Windows-PowerShell/Operational`, `Microsoft-Windows-Sysmon/Operational`, `Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational`, etc.).

La **rotation** des Event Logs est configurée par taille maximale (par défaut : 20 Mo pour Security, ce qui est insuffisant pour une investigation — les événements les plus anciens sont écrasés quand le fichier est plein). Sur un DC actif avec la configuration par défaut, le Security log peut tourner en quelques heures. La recommandation forensic readiness (Ch.27) est d'augmenter la taille à 1 Go minimum et de centraliser les logs dans un SIEM.

La **collecte** et le **parsing** avec EvtxECmd (Eric Zimmerman) sont la méthode de référence : `EvtxECmd.exe -f Security.evtx --csv output/ --csvf security_parsed.csv`. Le résultat est un CSV structuré analysable dans Timeline Explorer, avec chaque Event ID parsé en colonnes exploitables.

Des outils complémentaires accélèrent l'analyse. **Chainsaw** (WithSecure, open source) applique des règles Sigma sur les Event Logs pour détecter automatiquement les patterns d'attaque. **Hayabusa** (open source, japonais) offre une détection similaire basée sur Sigma avec un focus sur la vitesse. **LogParser** (Microsoft, gratuit) permet des requêtes SQL sur les fichiers evtx.

## 14.2 Event IDs critiques pour le forensic — interprétation détaillée

Plutôt qu'une simple liste, chaque Event ID est expliqué avec son contexte, son contenu, son interprétation forensic, et ses faux positifs.

**4624 (Successful Logon) :** enregistre chaque authentification réussie avec le type de logon. Les types pertinents pour le forensic : Type 2 (Interactive — login physique ou RDP via console), Type 3 (Network — accès à un partage réseau, authentification WMI ou PsExec), Type 7 (Unlock — déverrouillage de session), Type 10 (RemoteInteractive — RDP). L'Event 4624 contient le nom du compte, le domaine, l'adresse IP source (pour les logons réseau), et le processus d'authentification (NTLM vs Kerberos). Un 4624 Type 3 depuis une IP inconnue avec un compte de service à 3h du matin est un indicateur de mouvement latéral.

**4625 (Failed Logon) :** enregistre les échecs d'authentification. Un volume élevé de 4625 avec des comptes variés depuis une même source indique un password spraying ou un brute force. Le sous-status code précise la raison de l'échec (0xC0000064 = compte inexistant, 0xC000006A = mot de passe incorrect, 0xC0000234 = compte verrouillé).

**4648 (Logon with Explicit Credentials) :** enregistre quand un processus s'authentifie avec des credentials différentes de celles de la session en cours (runas, PsExec avec `-u`, ou pass-the-hash). C'est un indicateur fort de mouvement latéral — l'attaquant utilise des credentials volées pour accéder à d'autres machines.

**4672 (Special Privileges Assigned) :** enregistre l'attribution de privilèges administratifs lors d'un logon. Un 4672 pour un compte utilisateur standard est suspect (l'utilisateur a obtenu des droits qu'il ne devrait pas avoir).

**4688 (Process Creation) :** enregistre la création d'un processus avec le nom de l'exécutable et, si la journalisation de la ligne de commande est activée (GPO `Process Creation → Include command line`), la ligne de commande complète. C'est l'Event ID le plus riche pour le forensic d'exécution — la ligne de commande révèle exactement ce que l'attaquant a tapé. Sans l'activation de cette GPO, le 4688 est beaucoup moins informatif.

**7045 (Service Installed) :** enregistre l'installation d'un nouveau service. PsExec crée un service PSEXESVC. Les malwares installent souvent des services pour la persistence. Un 7045 avec un nom de service inhabituel, un chemin d'exécutable dans un répertoire temporaire, ou un service Type 0x10 (own process) mérite investigation.

**4698 (Scheduled Task Created) :** enregistre la création d'une tâche planifiée. Les tâches planifiées sont un mécanisme de persistence courant. Le contenu de l'événement inclut le XML de la tâche — action exécutée, déclencheur, compte utilisé.

**4769 (Kerberos Service Ticket Requested) :** avec encryption type 0x17 (RC4), c'est la signature du Kerberoasting. Un volume élevé de 4769 avec encryption RC4 depuis une seule machine indique que l'attaquant demande des TGS pour craquer les mots de passe des comptes de service. Détail au Ch.20 (AD forensics).

**1102 (Security Log Cleared) :** enregistre l'effacement du Security Event Log — ironiquement, l'acte de nettoyage produit lui-même un événement. Un 1102 est un indicateur d'anti-forensics. Si les logs sont centralisés dans un SIEM, les événements antérieurs au clearing sont préservés.

**Sysmon Event IDs** (si Sysmon est déployé) : Event 1 (Process Creation — plus détaillé que 4688, avec hash du binaire, ligne de commande complète, processus parent), Event 3 (Network Connection — quel processus se connecte à quelle IP), Event 7 (Image Loaded — DLL chargées par un processus), Event 10 (Process Access — accès à LSASS), Event 11 (File Create — fichiers créés), Event 22 (DNS Query — résolutions DNS par processus). Sysmon transforme la visibilité forensic d'une machine Windows — son déploiement est la recommandation de forensic readiness la plus impactante.

## 14.3 Corrélation des Event Logs entre machines

Reconstituer le mouvement latéral exige de corréler les Event Logs de plusieurs machines. Sur la machine source : 4648 (logon avec credentials explicites), Prefetch de l'outil de latéralisation (PsExec, wmic). Sur la machine destination : 4624 (logon réussi, type 3 ou 10), 7045 (service installé par PsExec), 4688 (processus créé). La corrélation repose sur les timestamps (les événements doivent être proches dans le temps), les comptes (le même compte apparaît sur les deux machines), et les IP (l'IP source du 4624 sur la destination correspond à l'IP de la machine source).

## 14.4 Fil rouge — MUSIC BOX : les Event Logs racontent l'histoire

> **🔬 MUSIC BOX — Épisode 13**
>
> L'analyse des Event Logs de DC01 (parsés avec EvtxECmd + Chainsaw) révèle la séquence de la compromission AD.
>
> J-45 : série de 4769 (Kerberos TGS) avec encryption type RC4 depuis WKS-RD-047 pour 12 comptes de service — **Kerberoasting confirmé**. Le compte `svc-backup` avait un SPN et un mot de passe faible (`NovaPharma2024!`, cracké en 2h).
>
> J-30 : 4624 type 3 depuis WKS-RD-047 avec le compte `svc-backup` (domain admin) — première utilisation du compte compromis pour le mouvement latéral.
>
> J-14 : 4662 avec les GUID de réplication (`1131f6ad-...`) depuis WKS-RD-047 — **DCSync confirmé**. Tous les hashes NTLM sont compromis.
>
> J-1, 03h42 : **1102 — Security Log cleared** sur DC01. L'attaquant a effacé le Security Log. Mais les événements antérieurs au clearing sont préservés dans le SIEM Splunk de NovaPharma — l'anti-forensics a échoué grâce à la centralisation des logs.

---
