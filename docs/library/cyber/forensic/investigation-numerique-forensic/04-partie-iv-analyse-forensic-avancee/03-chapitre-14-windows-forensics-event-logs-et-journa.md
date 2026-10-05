---
title: 'Chapitre 14 — Windows forensics : Event Logs et journaux d''audit'
source: Cyber/04 Forensic/Investigation numérique (forensic).md
note: Investigation numérique (forensic)
up:
- - Investigation numérique (forensic)
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

| Event ID | Journal | En une ligne |
|---|---|---|
| **4624** | Security | Authentification réussie (+ type de logon) |
| **4625** | Security | Échec d'authentification (+ sub-status) |
| **4648** | Security | Logon avec credentials explicites |
| **4672** | Security | Privilèges spéciaux (admin) attribués au logon |
| **4688** | Security | Création de processus (+ ligne de commande si GPO) |
| **7045** | System | Service installé |
| **4698** | Security | Tâche planifiée créée |
| **4769** | Security (DC) | Ticket de service Kerberos demandé (RC4 = Kerberoasting) |
| **1102** | Security | Security Log effacé |

### 4624 — Successful Logon

```text
Security
→ 4624
→ Successful Logon
```


- Enregistre chaque authentification réussie, avec le **type de logon**.
- Types pertinents pour le forensic :
    - **Type 2** (Interactive) : login physique ou RDP via console ;
    - **Type 3** (Network) : accès à un partage réseau, authentification WMI ou PsExec ;
    - **Type 7** (Unlock) : déverrouillage de session ;
    - **Type 10** (RemoteInteractive) : RDP.
- Contient :
    - le nom du compte et le domaine ;
    - l'adresse IP source (pour les logons réseau) ;
    - le processus d'authentification (NTLM vs Kerberos).

```text
4624 Type 3
+
IP inconnue
+
compte de service
+
3 h du matin
→ indicateur de mouvement latéral
```


### 4625 — Failed Logon

```text
Security
→ 4625
→ Failed Logon
```


- Enregistre les échecs d'authentification.
- Volume élevé de 4625, comptes variés, même source → **password spraying** ou **brute force**.
- Le **sub-status code** précise la raison de l'échec :
    - `0xC0000064` : compte inexistant ;
    - `0xC000006A` : mot de passe incorrect ;
    - `0xC0000234` : compte verrouillé.

### 4648 — Logon with Explicit Credentials

```text
Security
→ 4648
→ Logon with Explicit Credentials
```


- Un processus s'authentifie avec des credentials **différentes de celles de la session en cours** :
    - `runas` ;
    - PsExec avec `-u` ;
    - pass-the-hash.
- Indicateur fort de **mouvement latéral** : l'attaquant utilise des credentials volées pour accéder à d'autres machines.

### 4672 — Special Privileges Assigned

```text
Security
→ 4672
→ Special Privileges Assigned
```


- Attribution de privilèges administratifs lors d'un logon.
- Un 4672 pour un **compte utilisateur standard** est suspect : l'utilisateur a obtenu des droits qu'il ne devrait pas avoir.

### 4688 — Process Creation

```text
Security
→ 4688
→ Process Creation
```


- Création d'un processus, avec le nom de l'exécutable.
- Ligne de commande complète **si** la journalisation est activée : GPO `Process Creation → Include command line`.
- L'Event ID le plus riche pour le forensic d'exécution : la ligne de commande révèle exactement ce que l'attaquant a tapé.
- Sans cette GPO, le 4688 est beaucoup moins informatif.

### 7045 — Service Installed

```text
System
→ 7045
→ Service Installed
```


- Installation d'un nouveau service.
- PsExec crée un service **PSEXESVC**.
- Les malwares installent souvent des services pour la persistence.
- Mérite investigation :
    - nom de service inhabituel ;
    - chemin d'exécutable dans un répertoire temporaire ;
    - service Type `0x10` (own process).

### 4698 — Scheduled Task Created

```text
Security
→ 4698
→ Scheduled Task Created
```


- Création d'une tâche planifiée : mécanisme de persistence courant.
- Le contenu inclut le **XML de la tâche** : action exécutée, déclencheur, compte utilisé.

### 4769 — Kerberos Service Ticket Requested

```text
Security (DC)
→ 4769
→ Kerberos Service Ticket Requested
```


- Avec **encryption type `0x17` (RC4)** : signature du **Kerberoasting**.
- Volume élevé de 4769 RC4 depuis une seule machine → l'attaquant demande des TGS pour craquer les mots de passe des comptes de service.
- Détail au Ch.20 (AD forensics).

### 1102 — Security Log Cleared

```text
Security
→ 1102
→ Security Log Cleared
```


- Effacement du Security Event Log : ironiquement, l'acte de nettoyage produit lui-même un événement.
- Indicateur d'**anti-forensics**.
- Si les logs sont centralisés dans un SIEM, les événements antérieurs au clearing sont préservés.

### Sysmon Event IDs (si Sysmon est déployé)

```text
Sysmon
→ Microsoft-Windows-Sysmon/Operational
```


- **Event 1** (Process Creation) : plus détaillé que 4688 — hash du binaire, ligne de commande complète, processus parent.
- **Event 3** (Network Connection) : quel processus se connecte à quelle IP.
- **Event 7** (Image Loaded) : DLL chargées par un processus.
- **Event 10** (Process Access) : accès à LSASS.
- **Event 11** (File Create) : fichiers créés.
- **Event 22** (DNS Query) : résolutions DNS par processus.

> Sysmon transforme la visibilité forensic d'une machine Windows : son déploiement est la recommandation de forensic readiness la plus impactante.

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
