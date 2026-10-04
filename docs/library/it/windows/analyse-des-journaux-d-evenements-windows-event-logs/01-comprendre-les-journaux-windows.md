---
title: Comprendre les journaux Windows
source: IT/02 Windows/Journaux & investigation/Analyse des journaux d'événements Windows (Event Logs).md
note: Analyse des journaux d'événements Windows (Event Logs)
up:
- - Analyse des journaux d'événements Windows (Event Logs)
  - index.md
---

## Introduction aux journaux d’événements Windows

- Les **Windows Event Logs** enregistrent les événements générés par :
    - Windows ;
    - applications ;
    - services ;
    - drivers ;
    - mécanismes de sécurité.
## Stockage des Event Logs

Les journaux Windows sont généralement stockés dans :

```
C:\Windows\System32\winevt\Logs\
```

![|541x370](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-windows-event-log-analysis-005.webp)

Extension :

```
.evtx
```


![|352x377](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-windows-event-log-analysis-006.webp)

- Les fichiers `.evtx` utilisent le format **Windows Event Log**.
- Ils ne sont pas destinés à être lus directement avec un éditeur texte classique.

```
.evtx
→ Event Viewer / PowerShell / Forensic Tools
→ Human-readable Events
```


Outils possibles :

- Event Viewer (eventvwr.msc) ;
- PowerShell ;
- `wevtutil` ;
- outils DFIR / SIEM.
## Windows Logs
Les journaux Windows principaux sont :

- Application : Liés aux app installées 
- Security : Liés aux co/déco de session, aux co RDP, aux services utilisés, aux tâches créées...
- System : Liés aux états du matériel, pilotes...
- Setup : Lors de l'installation de l'OS. Sur DC, ce journal enregistrera les évents liés à l'AD
- Forwarded Events : Journaux transférés depuis d'autres ordinateurs du même réseau.

![|273x270](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-windows-event-log-analysis-007.webp)
### Application

- Contient les événements générés par les applications.
- Exemples :
    - crash ;
    - erreur applicative ;
    - problème de base de données ;
    - événement provenant d’un logiciel installé.

```
Application
→ Application Events
```

### Security

- Contient les événements liés aux **audits de sécurité**.
- Dépend fortement des **Audit Policies** configurées.

Exemples :

- logon / logoff ;
- échecs d’authentification ;
- account management ;
- privilege usage ;
- object access ;
- process creation lorsque l’audit correspondant est activé.

```
Security
→ Authentication
→ Authorization
→ Audit
```


Quelques Event IDs courants :

```
4624 → Successful Logon
4625 → Failed Logon
4688 → Process Creation
4720 → User Account Created
1102 → Audit Log Cleared
```


> ⚠️ Tous les événements de sécurité ne sont pas présents automatiquement : la visibilité dépend des **Audit Policies / Advanced Audit Policies** activées.

### System

- Contient principalement les événements générés par Windows et ses composants système.

Exemples :

- drivers ;
- services ;
- hardware ;
- boot ;
- erreurs système.

```
System
→ OS / Driver / Service Events
```


Exemple notable :

```
7045
→ New Service Installed
```

### Setup

- Contient les événements liés à :
    - installation de Windows ;
    - configuration du système ;
    - installation de composants / rôles.

Sur un Domain Controller, il peut également contenir certains événements liés à l’installation/configuration d’Active Directory.
### Forwarded Events

- Contient les événements reçus depuis d’autres systèmes Windows.

```
Endpoint A ─┐
Endpoint B ─┼→ Windows Event Forwarding → Collector
Server C ───┘
```


Utilisé notamment avec :

- **WEF — Windows Event Forwarding** ;
- **WEC — Windows Event Collector**.

-> Cela permet de centraliser les logs avant leur éventuelle ingestion dans un SIEM.
## Applications and Services Logs
En plus de `Windows Logs`, Windows possède :

```
Applications and Services Logs
```

- Contient des journaux beaucoup plus spécifiques à :
    - composants Windows ;
    - applications ;
    - services.

![|241x347](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-windows-event-log-analysis-008.webp)
Chemin fréquent :

```
Applications and Services Logs
└─ Microsoft
   └─ Windows
```


Exemples :

```
Microsoft-Windows-PowerShell/Operational
Microsoft-Windows-Windows Defender/Operational
Microsoft-Windows-TerminalServices-LocalSessionManager/Operational
Microsoft-Windows-TaskScheduler/Operational
```


Ces logs sont particulièrement utiles pour le **SOC / DFIR**, car ils fournissent souvent davantage de contexte que les journaux Windows généraux.
