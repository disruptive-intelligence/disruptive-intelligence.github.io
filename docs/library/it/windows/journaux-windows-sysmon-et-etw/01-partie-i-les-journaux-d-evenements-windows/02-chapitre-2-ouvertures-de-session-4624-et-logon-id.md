---
title: 'Chapitre 2 — Ouvertures de session : 4624 et Logon ID'
source: IT/02 Windows/Journaux & investigation/Journaux Windows, Sysmon et ETW.md
note: Journaux Windows, Sysmon et ETW
up:
- - Journaux Windows, Sysmon et ETW
  - ../index.md
- - Partie I — Les journaux d'événements Windows
  - index.md
---

## 3. Événement de sécurité 4624 — ouverture de session réussie

L'Event ID 4624 indique qu'une session de connexion a été créée avec succès sur une machine Windows.

Il fournit notamment :

- Target Account : compte auquel la session est associée ;
- Logon ID : identifiant de session ;
- Logon Type : type d'authentification ;
- Logon Process : mécanisme de connexion utilisé ;
- informations complémentaires selon le type de connexion.

![Event 4624 : connexion reussie de SYSTEM, Logon Type 5](../../../../assets/journaux-windows-sysmon-et-etw-htb-windows-event-logs-08.png)

### Types d'ouverture de session (Logon Types) courants

| Logon Type | Signification                               |
| ---------- | ------------------------------------------- |
| 2          | Interactive — connexion locale              |
| 3          | Network — connexion réseau                  |
| 5          | Service — connexion utilisée par un service |
| 10         | RemoteInteractive — notamment RDP           |

### Exemple — SYSTEM / Logon Type 5

Ici, l'Event 4624 concerne le compte `SYSTEM` avec un Logon Type 5.

Il indique une session de type Service Logon.

![Details de l'Event 4624 : TargetUserName SYSTEM, LogonType 5, LogonProcessName Advapi](../../../../assets/journaux-windows-sysmon-et-etw-htb-windows-event-logs-10.png)

Cela ne prouve pas, à lui seul, qu'un nouveau service a été installé. Pour comprendre l'activité, il faut corréler cet événement avec d'autres logs.

### Corrélation par Logon ID

Le Logon ID permet de rapprocher certains événements associés à une même session sur une machine.

Valeur utilisée :

`0x3E7`

Cette valeur correspond couramment à la session Local System.

Attention : il faut distinguer `SubjectLogonId` et `TargetLogonId`, qui représentent des rôles différents selon les événements. Leur utilisation dans une recherche doit être adaptée au schéma du log.
