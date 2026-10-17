---
title: Windows Event Logs & Finding Evil — Windows Event Logs
source: IT/02 Windows/Journaux & investigation/Débusquer l'attaquant dans les journaux Windows et Sysmon (Windows Event Logs & Finding Evil).md
note: Débusquer l'attaquant dans les journaux Windows et Sysmon (Windows Event Logs & Finding Evil)
up:
- - Débusquer l'attaquant dans les journaux Windows et Sysmon (Windows Event Logs & Finding Evil)
  - index.md
---

Les Windows Event Logs sont des journaux natifs de Windows qui enregistrent les événements générés par le système d'exploitation, les applications, les services et certains fournisseurs ETW (Event Tracing for Windows).

Ils constituent une source essentielle pour le SOC, le Threat Hunting et le DFIR, notamment pour analyser les authentifications, modifications système, activités suspectes et tentatives d'effacement de traces.

## 1. Windows Event Logging Basics

Les journaux Windows peuvent être consultés avec Event Viewer (`eventvwr.msc`) ou exploités par programmation avec la Windows Event Log API.

![Recherche Windows : ouvrir Event Viewer](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-01.png)

### Principaux journaux Windows

| Log              | Contenu                                                        |
| ---------------- | -------------------------------------------------------------- |
| Application      | Événements, erreurs et diagnostics des applications            |
| Security         | Authentifications, accès, privilèges et événements d'audit     |
| Setup            | Événements liés à l'installation et à la configuration Windows |
| System           | Événements du système, des services et des composants Windows  |
| Forwarded Events | Événements transmis depuis d'autres machines                   |

![Windows Logs : Application, Security, Setup, System et Forwarded Events](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-02.png)

Forwarded Events permet de consulter des événements reçus via Windows Event Forwarding (WEF), lorsque cette fonctionnalité est configurée.

Event Viewer peut également ouvrir des fichiers de journaux sauvegardés au format `.evtx`, accessibles dans la section `Saved Logs`.

![Fichier .evtx ouvert dans Saved Logs (evenements Sysmon)](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-03.png)

## 2. Anatomy of a Windows Event

Chaque événement Windows contient des métadonnées permettant de comprendre son origine et son contexte.

| Champ             | Description                                                         |
| ----------------- | ------------------------------------------------------------------- |
| Log Name          | Journal contenant l'événement                                       |
| Source / Provider | Composant ayant généré l'événement                                  |
| Event ID          | Identifiant du type d'événement                                     |
| Task Category     | Catégorie fonctionnelle de l'événement                              |
| Level             | Niveau : Information, Warning, Error, Critical ou Verbose           |
| Keywords          | Indicateurs de classification, comme Audit Success ou Audit Failure |
| User              | Compte associé à l'événement, lorsqu'il est renseigné               |
| OpCode            | Opération spécifique décrite par l'événement                        |
| Logged            | Date et heure de l'enregistrement                                   |
| Computer          | Machine ayant généré l'événement                                    |
| XML Data          | Représentation structurée des champs et données supplémentaires     |

![Niveaux Information et Error du journal Application](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-04.png)

### Event ID & Provider

Un Event ID identifie un type d'événement dans le contexte de son fournisseur.

Exemple :

`Application → SideBySide → Event ID 35`

![Erreur SideBySide, Event ID 35](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-05.png)

Cet événement décrit une erreur de génération du contexte d'activation d'une application, liée dans l'exemple à une incompatibilité d'architecture.

L'onglet `Details` permet d'examiner les données structurées, notamment :

- `SystemTime` : timestamp ;
- `EventRecordID` : numéro de l'enregistrement ;
- `ProcessID` : identifiant du processus associé ;
- `ThreadID` : identifiant du thread ;
- `Computer` : machine source.

![Onglet Details de l'Event 35 : provider, version, level, date de creation](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-06.png)

![Details : SystemTime, EventRecordID, ProcessID, ThreadID, Computer](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-07.png)

Important : un Event ID ne doit pas être interprété indépendamment de son Provider et de son journal.

## 3. Windows Security Event 4624 — Successful Logon

L'Event ID 4624 indique qu'une session de connexion a été créée avec succès sur une machine Windows.

Il fournit notamment :

- Target Account : compte auquel la session est associée ;
- Logon ID : identifiant de session ;
- Logon Type : type d'authentification ;
- Logon Process : mécanisme de connexion utilisé ;
- informations complémentaires selon le type de connexion.

![Event 4624 : connexion reussie de SYSTEM, Logon Type 5](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-08.png)

### Logon Types courants

| Logon Type | Signification                               |
| ---------- | ------------------------------------------- |
| 2          | Interactive — connexion locale              |
| 3          | Network — connexion réseau                  |
| 5          | Service — connexion utilisée par un service |
| 10         | RemoteInteractive — notamment RDP           |

### Exemple — SYSTEM / Logon Type 5

Ici, l'Event 4624 concerne le compte `SYSTEM` avec un Logon Type 5.

Il indique une session de type Service Logon.

![Details de l'Event 4624 : TargetUserName SYSTEM, LogonType 5, LogonProcessName Advapi](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-10.png)

Cela ne prouve pas, à lui seul, qu'un nouveau service a été installé. Pour comprendre l'activité, il faut corréler cet événement avec d'autres logs.

### Logon ID Correlation

Le Logon ID permet de rapprocher certains événements associés à une même session sur une machine.

Valeur utilisée :

`0x3E7`

Cette valeur correspond couramment à la session Local System.

Attention : il faut distinguer `SubjectLogonId` et `TargetLogonId`, qui représentent des rôles différents selon les événements. Leur utilisation dans une recherche doit être adaptée au schéma du log.

## 4. Custom XML Queries — Event Viewer

Event Viewer permet de créer des filtres XML pour effectuer des recherches plus précises.

Chemin :

`Event Viewer → Filter Current Log → XML → Edit Query Manually`

### Objectif

Dans cet exemple, la recherche porte sur :

`SubjectLogonId = 0x3E7`

![Filtre XML du journal Security sur SubjectLogonId 0x3E7](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-09.png)

L'objectif est de retrouver des événements associés à ce contexte de session afin de reconstruire une séquence d'activités.

Exemple de filtre XML illustratif :

```
<QueryList>
  <Query Id="0" Path="Security">
    <Select Path="Security">
      *[EventData[Data[@Name='SubjectLogonId']='0x3e7']]
    </Select>
  </Query>
</QueryList>
```


Ce filtre sélectionne les événements du journal `Security` possédant le champ `SubjectLogonId` avec la valeur indiquée.

Il ne récupère pas automatiquement tous les événements de la session si ceux-ci utilisent d'autres champs, notamment `TargetLogonId`.

### Intérêt DFIR

- Réduire le volume d'événements à examiner.
- Rechercher les opérations associées à un contexte utilisateur.
- Corréler authentifications, changements de privilèges et modifications système.
- Reconstituer une Event Timeline.

Il est également possible de créer des filtres dans l'interface graphique et d'en examiner ensuite la représentation XML.

## 5. Exemple d'investigation — Event IDs 4907, 4624 et 4672

Analyse progressive de plusieurs événements Windows liés à un même contexte.

### Event ID 4907 — Auditing Settings Changed on Object

L'Event ID 4907 est généré lorsque les paramètres d'audit d'un objet Windows sont modifiés, notamment sa SACL (System Access Control List).

![Event 4907 : modification des parametres d'audit, Logon ID 0x3E7](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-11.png)

La SACL définit quelles tentatives d'accès à un objet doivent être journalisées.

Elle est constituée d'ACE (Access Control Entries) pouvant spécifier :

- les comptes ou groupes concernés ;
- les opérations à auditer ;
- les accès réussis, échoués ou les deux.

Distinction : la SACL contrôle l'audit des accès, tandis que la DACL contrôle principalement les autorisations d'accès.

### Analyse

Les détails de l'Event 4907 montrent :

| Champ         | Information                                          |
| ------------- | ---------------------------------------------------- |
| Process Name  | `SetupHost.exe`                                      |
| Object Type   | File                                                 |
| Object Name   | Objet associé au boot manager                        |
| OldSd / NewSd | Descripteurs de sécurité avant et après modification |

![Details de l'Event 4907 : ObjectType File, ProcessName SetupHost.exe, OldSd / NewSd](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-12.png)

Les champs `OldSd` et `NewSd` utilisent le format SDDL (Security Descriptor Definition Language).

Ils permettent d'examiner les changements apportés au descripteur de sécurité.

`SetupHost.exe` est associé à des opérations de configuration Windows. Son nom est cohérent avec une activité d'installation, mais un nom de processus légitime ne garantit pas qu'une activité soit saine.

### Event ID 4672 — Special Privileges Assigned to New Logon

![Events 4624 Logon puis 4672 Special Logon](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-13.png)

L'Event ID 4672 indique que des privilèges sensibles ont été attribués au token d'une nouvelle session de connexion.

Exemple :

`SeDebugPrivilege`

![Event 4672 : SYSTEM avec SeAssignPrimaryTokenPrivilege, SeDebugPrivilege](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-14.png)

Ce privilège peut permettre à un processus disposant des autorisations nécessaires d'interagir avec d'autres processus de manière privilégiée.

### Corrélation

```
Event 4907
Audit Configuration Modified
          ↓
Event 4624
Successful Logon
          ↓
Event 4672
Special Privileges Assigned
          ↓
Timeline & Contextual Investigation
```


Cette séquence permet d'étudier les modifications d'audit et le contexte de connexion privilégiée.

Un Event 4672 associé à SYSTEM peut être parfaitement normal. De même, la présence successive de ces événements ne suffit pas à confirmer une compromission.

## 6. Useful Windows Event IDs

### System Logs — Services, Shutdown & Restart

| Event ID | Événement                    | Intérêt                                                     |
| -------- | ---------------------------- | ----------------------------------------------------------- |
| 1074     | Shutdown / Restart initié    | Identifier l'origine d'un arrêt ou redémarrage              |
| 6005     | Event Log Service Started    | Repérer un démarrage du service, souvent lié au boot        |
| 6006     | Event Log Service Stopped    | Repérer un arrêt du service, souvent lié au shutdown        |
| 6013     | System Uptime                | Consulter la durée de fonctionnement du système             |
| 7040     | Service Startup Type Changed | Détecter une modification du type de démarrage d'un service |
| 7045     | Service Installed            | Identifier l'installation d'un nouveau service              |

L'Event 7045 est un événement du journal System, pas du journal Security.

Ces événements permettent notamment d'investiguer des redémarrages inhabituels, l'installation de services suspects et certaines modifications pouvant soutenir la Persistence.

### Security Logs — Authentication & Privileges

| Event ID | Événement                          | Intérêt                                                   |
| -------- | ---------------------------------- | --------------------------------------------------------- |
| 4624     | Successful Logon                   | Identifier les connexions réussies                        |
| 4625     | Failed Logon                       | Rechercher des tentatives d'authentification échouées     |
| 4648     | Explicit Credentials Used          | Examiner l'utilisation explicite d'identifiants           |
| 4672     | Special Privileges Assigned        | Surveiller les sessions disposant de privilèges sensibles |
| 4771     | Kerberos Pre-Authentication Failed | Rechercher des échecs de préauthentification Kerberos     |
| 4776     | Credential Validation Attempt      | Examiner les validations d'identifiants via NTLM          |

Les Events `4624`, `4625`, `4648`, `4771` et `4776` sont particulièrement utiles pour rechercher des activités suspectes d'authentification et de Lateral Movement.

### Security Logs — Persistence & Account Changes

| Event ID | Événement               | Intérêt                                            |
| -------- | ----------------------- | -------------------------------------------------- |
| 4698     | Scheduled Task Created  | Détecter la création d'une tâche planifiée         |
| 4700     | Scheduled Task Enabled  | Identifier l'activation d'une tâche                |
| 4701     | Scheduled Task Disabled | Identifier la désactivation d'une tâche            |
| 4702     | Scheduled Task Updated  | Examiner les modifications de tâches planifiées    |
| 4738     | User Account Changed    | Détecter des modifications de comptes utilisateurs |

Les Scheduled Tasks peuvent être utilisées légitimement pour l'administration, mais également comme mécanismes de Persistence.

### Security Logs — Audit & Object Access

| Event ID | Événement                        | Intérêt                                         |
| -------- | -------------------------------- | ----------------------------------------------- |
| 1102     | Security Audit Log Cleared       | Détecter l'effacement du journal Security       |
| 4656     | Handle to an Object Requested    | Rechercher des demandes d'accès à des objets    |
| 4719     | System Audit Policy Changed      | Identifier des changements de politique d'audit |
| 4907     | Object Auditing Settings Changed | Analyser les modifications de SACL              |

L'Event `4656` signale une demande de handle, pas nécessairement un accès effectivement réalisé.

Les Events `1102`, `4719` et `4907` peuvent révéler des tentatives de modification ou de suppression des traces d'audit, mais doivent être contextualisés.

### Security Logs — Network Shares & Filtering

| Event ID | Événement                                     | Intérêt                                                                  |
| -------- | --------------------------------------------- | ------------------------------------------------------------------------ |
| 5140     | Network Share Accessed                        | Identifier les accès aux partages réseau                                 |
| 5142     | Network Share Created                         | Détecter la création de partages                                         |
| 5145     | Detailed File Share Access Check              | Examiner les demandes d'accès aux ressources partagées                   |
| 5157     | Windows Filtering Platform Blocked Connection | Identifier les connexions bloquées par la plateforme de filtrage Windows |

Ces événements peuvent soutenir les investigations liées aux accès SMB, aux partages non autorisés et aux communications suspectes.

### Microsoft Defender Antivirus Logs

Les événements suivants relèvent du journal Microsoft-Windows-Windows Defender/Operational, et non du journal Security :

| Event ID | Événement                     | Intérêt                                               |
| -------- | ----------------------------- | ----------------------------------------------------- |
| 1116     | Malware Detected              | Identifier une détection antivirus                    |
| 1118     | Remediation Started           | Suivre le début d'une action de remédiation           |
| 1119     | Remediation Succeeded         | Identifier une remédiation réussie                    |
| 1120     | Remediation Failed            | Identifier un échec de remédiation                    |
| 5001     | Real-Time Protection Disabled | Détecter la désactivation de la protection temps réel |

La distinction Detection / Remediation Started / Remediation Succeeded / Remediation Failed est essentielle : détecter un malware ne garantit pas qu'il ait été neutralisé.

## 7. Windows Event Logs — Threat Hunting Workflow

```
Suspicious Activity
        ↓
Identify Relevant Event IDs
        ↓
Collect Windows Event Logs
        ↓
Filter by Time / User / Host
        ↓
Correlate Logon IDs & Events
        ↓
Reconstruct Event Timeline
        ↓
Investigate Suspicious Behavior
```


### Bonnes pratiques

- Baseline : connaître les comportements normaux des systèmes et utilisateurs.
- Centralized Logging : collecter les événements dans un SIEM ou une infrastructure centralisée.
- Log Correlation : rapprocher plusieurs Event IDs et sources de données.
- Time Synchronization : synchroniser les horloges pour faciliter l'analyse chronologique.
- Audit Configuration : activer les politiques d'audit nécessaires à la production des événements recherchés.
- Alert Tuning : adapter les règles de détection à l'environnement pour limiter les False Positives.

## 8. Synthèse

| Objectif d'investigation        | Événements utiles            |
| ------------------------------- | ---------------------------- |
| Authentication Analysis         | 4624, 4625, 4648, 4771, 4776 |
| Privileged Access               | 4672                         |
| Persistence                     | 4698, 4700–4702, 7040, 7045  |
| Account Modification            | 4738                         |
| Log Tampering                   | 1102, 4719, 4907             |
| Network Share Activity          | 5140, 5142, 5145             |
| Blocked Connections             | 5157                         |
| Malware Detection & Remediation | 1116, 1118–1120              |
| Security Protection Disabled    | 5001                         |
| Shutdown / Restart              | 1074, 6005, 6006, 6013       |

Les Windows Event Logs constituent une source centrale pour reconstruire une activité suspecte et identifier des traces d'attaque.

Le point essentiel est de ne pas interpréter un événement isolément : les Event IDs doivent être analysés avec leurs champs détaillés, leur contexte utilisateur, la chronologie des événements et les autres sources de télémétrie disponibles.

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
