---
title: Tâches planifiées
source: IT/02 Windows/Journaux & investigation/Analyse des journaux d'événements Windows (Event Logs).md
note: Analyse des journaux d'événements Windows (Event Logs)
up:
- - Analyse des journaux d'événements Windows (Event Logs)
  - index.md
---

Source des captures : [Hack The Box Academy - Event Log Analysis](https://academy.hackthebox.com/course/preview/event-log-analysis)

## Journaux d’événements des tâches planifiées Windows

- **Task Scheduler** permet d’exécuter automatiquement :
    - programmes ;
    - scripts ;
    - sauvegardes ;
    - tâches de maintenance ;
    - actions déclenchées par une heure, un calendrier ou un événement.
- Les tâches peuvent être créées :
    - localement ;
    - à distance ;
    - via GUI ;
    - CLI / PowerShell ;
    - API Windows.

```text
Trigger
→ Scheduled Task
→ Action
→ Program / Script / Command
```


## Abus offensif des Scheduled Tasks

Les attaquants peuvent créer ou modifier une tâche afin de :

- exécuter du code ;
- maintenir une **persistence** ;
- relancer régulièrement un malware ;
- exécuter une action avec des privilèges élevés ;
- masquer leur activité derrière une tâche au nom légitime.

MITRE ATT&CK :

```text
T1053.005
→ Scheduled Task/Job: Scheduled Task
```


Exemple :

```text
Malicious Script
→ Scheduled Task
→ Trigger every day
→ Persistence
```


> Une tâche ne s’exécute pas automatiquement avec les « privilèges du Task Scheduler » : elle s’exécute dans le **security context configuré pour la tâche**. Si elle est configurée sous `SYSTEM` ou avec `Run with highest privileges`, l’impact peut être particulièrement important.

---

## Intérêt forensique

- Les Event Logs peuvent conserver la trace d’une tâche même après sa suppression.
- Cela permet de retrouver :
    - nom ;
    - auteur ;
    - trigger ;
    - commande ;
    - arguments ;
    - modifications ;
    - suppression.

```text
Attacker
→ Create Task
→ Execute
→ Delete Task

Task no longer exists
≠
Evidence no longer exists
```


---

## Journal Security

Les événements détaillés liés aux Scheduled Tasks peuvent être enregistrés dans :

```text
Windows Logs
→ Security
```


Ils nécessitent que l’audit approprié soit activé.

Dans **Advanced Audit Policy**, cela relève notamment de :

```text
Object Access
→ Audit Other Object Access Events
```


> Si cette journalisation n’est pas activée, les Event IDs `4698/4699/4702` peuvent être absents.

---

## Event ID 4698 — Scheduled Task Created

```text
Security
→ 4698
→ A scheduled task was created
```


Lorsqu’une tâche est créée, l’événement peut fournir :

- utilisateur ayant créé la tâche ;
- nom de la tâche ;
- trigger ;
- account / security context ;
- programme exécuté ;
- command-line arguments ;
- définition XML de la tâche selon la version de Windows.

Exemple :

```text
Task Name:
\Windows Update Task

Author:
CyberJunkie

Trigger:
Friday 15:00

Command:
powershell.exe

Arguments:
-File C:\Users\user\Documents\malicious.ps1
```


![Filtre Security sur Event ID 4698](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-01.png)

![Evenements 4698 de creation de tache](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-02.png)

---

### Champs importants à examiner

```text
Who created it?
What does it execute?
From where?
When does it execute?
Under which account?
With which privileges?
```


Rechercher notamment :

- `SubjectUserName` ;
- `TaskName` ;
- `Author` ;
- `Triggers` ;
- `UserId` ;
- `RunLevel` ;
- `Command` ;
- `Arguments`.

![Details du 4698 avec auteur description et declencheur](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-03.png)

---

## Indicateurs suspects

### Nom trompeur

Les attaquants utilisent souvent des noms ressemblant à des tâches légitimes :

```text
Windows Update
Microsoft Update Service
System Maintenance
AdobeUpdate
ChromeUpdate
```


> Le nom d’une tâche n’est jamais une preuve de légitimité.

Dans l’exemple du cours :

```text
"Windows Update Task"
+
Created by CyberJunkie
→ Suspicious
```


---

### Chemin inhabituel

Exemple :

```text
C:\Users\user\Documents\Windows Update.exe
```


Pour un composant supposé être Windows Update :

```text
User-writable directory
+
System-looking filename
→ Highly Suspicious
```


Répertoires particulièrement intéressants :

```text
%TEMP%
%APPDATA%
%LOCALAPPDATA%
Downloads
Documents
C:\Users\Public
```


![Commande de la tache dans le dossier Documents](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-04.png)

---

### Commandes suspectes

Exemples :

```text
powershell.exe
cmd.exe
wscript.exe
cscript.exe
mshta.exe
rundll32.exe
regsvr32.exe
```


Encore plus intéressant avec :

```text
-EncodedCommand
-ExecutionPolicy Bypass
-hidden
DownloadString
IEX
http:// / https://
```


```text
Scheduled Task
→ PowerShell
→ Encoded Command
→ External Network Connection
```


→ priorité d’investigation élevée.

---

## NT AUTHORITY\SYSTEM

Les tâches légitimes Windows sont souvent créées/exécutées sous :

```text
NT AUTHORITY\SYSTEM
```


Mais :

```text
SYSTEM
≠ automatically legitimate
```


Un attaquant ayant déjà obtenu des privilèges administrateur peut également créer une tâche exécutée sous `SYSTEM`.

Il faut donc corréler :

```text
Task Creator
+
Command
+
Path
+
Timestamp
+
Trigger
+
Incident Context
```


---

## Task Scheduler Operational Log

Même lorsque les événements détaillés du journal `Security` ne sont pas disponibles, Windows possède un journal spécialisé :

```text
Applications and Services Logs
→ Microsoft
→ Windows
→ TaskScheduler
→ Operational
```


Il fournit généralement moins d’informations que les événements `Security`, mais reste très utile pour reconstruire l’activité.

![Chemin Applications and Services Logs](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-05.png)

![Journal TaskScheduler Operational](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-06.png)

---

## Event ID 106 — Task Registered

```text
TaskScheduler/Operational
→ 106
→ Task registered
```


- Indique qu’une tâche a été enregistrée/créée.
- Le journal fournit notamment le **Task Name**.

```text
106
→ task appeared on the system
```


![Evenement 106 Task registered avec nom de tache](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-07.png)

---

## Event IDs 200 / 201 — Exécution

Deux Event IDs particulièrement utiles dans `TaskScheduler/Operational` :

```text
200
→ Action started

201
→ Action completed
```


Le cours présente notamment `201`, qui permet de retrouver des informations sur l’action exécutée.

Conceptuellement :

```text
106
→ Task Registered

200
→ Action Started

201
→ Action Completed
```


Cela permet de distinguer :

```text
Task exists
≠
Task actually executed
```


![Execution manuelle de la tache dans Task Scheduler](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-08.png)

![Evenement 201 indiquant action terminee et commande executee](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-09.png)

---

## Event ID 4702 — Scheduled Task Updated

```text
Security
→ 4702
→ A scheduled task was updated
```


- Déclenché lorsqu’une tâche existante est modifiée.
- Peut contenir des informations comparables à l’événement de création :
    - Task Name ;
    - nouvelle définition ;
    - trigger ;
    - programme ;
    - arguments.

### Pourquoi modifier une tâche existante ?

Cela peut être plus discret que d’en créer une nouvelle :

```text
Existing Legitimate Task
        ↓
Attacker modifies action
        ↓
Malicious Code Execution
```


Exemple du cours :

```text
Before:
Friday → 15:00

After:
Every day → 12:00
```


→ comparaison `4698 ↔ 4702` utile pour identifier exactement ce qui a changé.

![Declencheur modifie chaque jour a midi](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-10.png)

![Evenement Security 4702 avec nouvelle definition de tache](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-11.png)

---

## Event ID 140 — Task Updated

Dans :

```text
TaskScheduler/Operational
```


```text
140
→ Task updated
```


- Permet d’identifier qu’une modification a eu lieu.
- Généralement moins détaillé que `Security / 4702`.

![Evenement TaskScheduler 140 mise a jour de tache](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-12.png)

---

## Event ID 4699 — Scheduled Task Deleted

```text
Security
→ 4699
→ A scheduled task was deleted
```


Permet notamment de retrouver :

- Task Name ;
- utilisateur ayant effectué l’action ;
- timestamp.

La suppression peut être légitime, mais dans une investigation :

```text
Task Created
→ Malicious Execution
→ Task Deleted shortly after
```


peut indiquer une tentative de **cleanup / Defense Evasion**.

![Suppression de la tache dans Task Scheduler](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-13.png)

![Evenement Security 4699 avec nom de tache supprimee](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-14.png)

---

## Event ID 141 — Task Deleted

Dans :

```text
TaskScheduler/Operational
```


```text
141
→ Task deleted
```


- Indique également la suppression d’une tâche.
- Principalement utile pour :
    - nom de tâche ;
    - timestamp.

![Evenement TaskScheduler 141 suppression de tache](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-15.png)

---

## Autres Event IDs utiles

Dans le journal `Security` :

```text
4698 → Task created
4699 → Task deleted
4700 → Task enabled
4701 → Task disabled
4702 → Task updated
```


Pour une investigation complète, `4700` et `4701` peuvent être utiles lorsqu’un attaquant **réactive une tâche existante** plutôt que d’en créer une nouvelle.

---

## Corrélation recommandée

L’analyse d’une Scheduled Task ne doit pas s’arrêter au seul événement `4698`.

Exemple :

```text
4698
→ suspicious task created

        ↓

4688
→ powershell.exe executed

        ↓

TaskScheduler 200
→ task action started

        ↓

Network Logs / EDR
→ connection to suspicious domain

        ↓

4699 / 141
→ task deleted
```


→ permet de reconstruire :

```text
Persistence
→ Execution
→ C2
→ Cleanup
```


---

## Timeline d’une tâche malveillante

```text
10:14
4698
→ Task "\Windows Update" created

10:15
200
→ Action started

10:15
4688
→ powershell.exe

10:15
EDR / Network
→ connection to attacker C2

12:03
4702
→ Task modified

15:47
4699 / 141
→ Task deleted
```


Même si la tâche a disparu du système :

```text
Event Logs
→ reconstruct attacker activity
```


---

## Points à rechercher en SOC

Une Scheduled Task devient plus suspecte lorsqu’elle présente plusieurs caractéristiques :

```text
New / Modified Task
+
User-writable Path
+
LOLBin / Script
+
Encoded Command
+
SYSTEM Privileges
+
Unusual Trigger
+
Incident Time Window
→ High Suspicion
```


Rechercher notamment :

- tâches nouvellement créées ;
- noms ressemblant à Microsoft / Windows ;
- exécutables dans `%TEMP%`, `%APPDATA%`, `Downloads` ;
- PowerShell / CMD / WScript / MSHTA ;
- URLs ou IP dans les arguments ;
- tâche exécutée sous `SYSTEM` ;
- triggers inhabituels ;
- tâches créées puis rapidement supprimées ;
- modifications pendant la fenêtre d’incident.

---

## Vue d’ensemble

```text
Security Log
├─ 4698 → Created
├─ 4699 → Deleted
├─ 4700 → Enabled
├─ 4701 → Disabled
└─ 4702 → Updated

TaskScheduler/Operational
├─ 106 → Registered
├─ 140 → Updated
├─ 141 → Deleted
├─ 200 → Action Started
└─ 201 → Action Completed
```


Le point important est de ne pas seulement chercher **si une tâche existe actuellement** : les Event Logs permettent de reconstruire **sa création, ses modifications, son exécution et sa suppression**, ce qui en fait une source particulièrement utile pour détecter les mécanismes de **Persistence / Execution** basés sur `T1053.005`.

Source des captures : [Hack The Box Academy - Event Log Analysis](https://academy.hackthebox.com/course/preview/event-log-analysis)
