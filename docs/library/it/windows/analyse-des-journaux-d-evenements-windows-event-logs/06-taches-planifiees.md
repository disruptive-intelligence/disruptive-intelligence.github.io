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

MITRE ATT&CK : **T1053.005** — Scheduled Task/Job: Scheduled Task.

```text
Malicious Script
→ Scheduled Task
→ Trigger every day
→ Persistence
```


> Une tâche ne s’exécute pas automatiquement avec les « privilèges du Task Scheduler » : elle s’exécute dans le **security context configuré pour la tâche**. Si elle est configurée sous `SYSTEM` ou avec `Run with highest privileges`, l’impact peut être particulièrement important.

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
Attacker → Create Task → Execute → Delete Task

Task no longer exists ≠ Evidence no longer exists
```


## Où chercher : Security ou TaskScheduler/Operational

- **Security** (`Windows Logs → Security`) : les Event IDs les plus intéressants (4698 à 4702).
    - Auteur, nom, trigger, commande, arguments, définition de la tâche.
    - **Seulement si l’audit est activé — ce n’est pas le cas par défaut.**
    - Advanced Audit Policy → Object Access → **Audit Other Object Access Events**.
- **TaskScheduler/Operational** : le passage obligé quand l’audit n’est pas activé.
    - `Applications and Services Logs → Microsoft → Windows → TaskScheduler → Operational`
    - 106, 140, 141, 200, 201 : même cycle de vie de la tâche, avec moins de détails.

> **Réflexe** : chercher d’abord 4698 à 4702 dans Security. S’ils n’apparaissent pas, l’audit n’est probablement pas activé : lire TaskScheduler/Operational.
>
> Ce journal peut lui aussi être désactivé selon la version de Windows ou la configuration du poste : dans le Planificateur de tâches, **Enable All Tasks History** (« Activer l’historique de toutes les tâches ») le rallume. Les événements antérieurs ne sont pas récupérables.

![Chemin Applications and Services Logs](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-05.png)

![Journal TaskScheduler Operational](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-06.png)

Vue d’ensemble, étape par étape :

| Étape | Security (si l’audit est activé) | TaskScheduler/Operational (sinon) |
|---|---|---|
| Création | **4698** — A scheduled task was created | **106** — Task registered |
| Exécution | — | **200** — Action started · **201** — Action completed |
| Modification | **4702** — A scheduled task was updated | **140** — Task updated |
| Activation / désactivation | **4700** — Task enabled · **4701** — Task disabled | — |
| Suppression | **4699** — A scheduled task was deleted | **141** — Task deleted |

## Création : 4698 et 106

### 4698 — Scheduled Task Created (Security)

- Peut fournir :
    - utilisateur ayant créé la tâche ;
    - nom de la tâche ;
    - trigger ;
    - account / security context ;
    - programme exécuté ;
    - command-line arguments ;
    - définition XML de la tâche selon la version de Windows.

```text
Task Name:  \Windows Update Task
Author:     CyberJunkie
Trigger:    Friday 15:00
Command:    powershell.exe
Arguments:  -File C:\Users\user\Documents\malicious.ps1
```


![Filtre Security sur Event ID 4698](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-01.png)

![Evenements 4698 de creation de tache](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-02.png)

Champs à examiner :

| Question | Champs |
|---|---|
| Qui l’a créée ? | `SubjectUserName`, `Author` |
| Quelle tâche ? | `TaskName` |
| Quand s’exécute-t-elle ? | `Triggers` |
| Sous quel compte, avec quels privilèges ? | `UserId`, `RunLevel` |
| Qu’exécute-t-elle, et depuis où ? | `Command`, `Arguments` |

![Details du 4698 avec auteur description et declencheur](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-03.png)

### 106 — Task Registered (TaskScheduler/Operational)

- Indique qu’une tâche a été enregistrée/créée : elle apparaît sur le système.
- Fournit notamment le **Task Name**.

![Evenement 106 Task registered avec nom de tache](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-07.png)

## Exécution : 200 et 201

- **200** → Action started.
- **201** → Action completed : permet de retrouver des informations sur l’action exécutée (c’est celui que présente le cours).
- Avec 106, ils distinguent une tâche qui existe d’une tâche réellement exécutée : **Task exists ≠ Task actually executed**.

![Execution manuelle de la tache dans Task Scheduler](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-08.png)

![Evenement 201 indiquant action terminee et commande executee](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-09.png)

## Modification : 4702 et 140

### 4702 — Scheduled Task Updated (Security)

- Déclenché lorsqu’une tâche existante est modifiée.
- Informations comparables à la création :
    - Task Name ;
    - nouvelle définition ;
    - trigger ;
    - programme ;
    - arguments.
- Pourquoi modifier une tâche existante ? C’est plus discret que d’en créer une nouvelle :

```text
Existing Legitimate Task → Attacker modifies action → Malicious Code Execution
```


- Exemple du cours : trigger `Friday 15:00` → `Every day 12:00`.
- Comparer `4698 ↔ 4702` pour identifier exactement ce qui a changé.

![Declencheur modifie chaque jour a midi](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-10.png)

![Evenement Security 4702 avec nouvelle definition de tache](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-11.png)

### 140 — Task Updated (TaskScheduler/Operational)

- Permet d’identifier qu’une modification a eu lieu.
- Généralement moins détaillé que `Security / 4702`.

![Evenement TaskScheduler 140 mise a jour de tache](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-12.png)

### 4700 / 4701 — Task Enabled / Disabled (Security)

- Utiles lorsqu’un attaquant **réactive une tâche existante** plutôt que d’en créer une nouvelle.

## Suppression : 4699 et 141

### 4699 — Scheduled Task Deleted (Security)

- Fournit : Task Name, utilisateur ayant effectué l’action, timestamp.
- La suppression peut être légitime, mais une séquence `Task Created → Malicious Execution → Task Deleted shortly after` peut indiquer une tentative de **cleanup / Defense Evasion**.

![Suppression de la tache dans Task Scheduler](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-13.png)

![Evenement Security 4699 avec nom de tache supprimee](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-14.png)

### 141 — Task Deleted (TaskScheduler/Operational)

- Indique également la suppression d’une tâche.
- Surtout utile pour le nom de tâche et le timestamp.

![Evenement TaskScheduler 141 suppression de tache](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-15.png)

## Indicateurs suspects

### Nom trompeur

- Noms ressemblant à des tâches légitimes : `Windows Update`, `Microsoft Update Service`, `System Maintenance`, `AdobeUpdate`, `ChromeUpdate`.
- Exemple du cours : « Windows Update Task » créée par CyberJunkie → suspect.

> Le nom d’une tâche n’est jamais une preuve de légitimité.

### Chemin inhabituel

- Exécutable au nom système dans un dossier modifiable par l’utilisateur → très suspect.
    - Exemple : `C:\Users\user\Documents\Windows Update.exe` pour un composant supposé être Windows Update.
- Répertoires à surveiller : `%TEMP%`, `%APPDATA%`, `%LOCALAPPDATA%`, `Downloads`, `Documents`, `C:\Users\Public`.

![Commande de la tache dans le dossier Documents](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-scheduled-tasks-event-logs-04.png)

### Commandes suspectes

- Programmes : `powershell.exe`, `cmd.exe`, `wscript.exe`, `cscript.exe`, `mshta.exe`, `rundll32.exe`, `regsvr32.exe`.
- Encore plus intéressant avec : `-EncodedCommand`, `-ExecutionPolicy Bypass`, `-hidden`, `DownloadString`, `IEX`, `http://` / `https://`.
- `Scheduled Task → PowerShell → Encoded Command → External Network Connection` → priorité d’investigation élevée.

### NT AUTHORITY\SYSTEM

- Les tâches légitimes Windows sont souvent créées/exécutées sous `NT AUTHORITY\SYSTEM`.
- Mais **SYSTEM ≠ automatically legitimate** : un attaquant ayant déjà obtenu des privilèges administrateur peut créer une tâche exécutée sous `SYSTEM`.
- Il faut corréler : créateur de la tâche + commande + chemin + timestamp + trigger + contexte de l’incident.

## Corrélation et chronologie

L’analyse ne doit pas s’arrêter au seul `4698` : croiser avec la création de processus (`4688`) et les traces réseau / EDR.

| Heure | Source | Événement |
|---|---|---|
| 10:14 | Security **4698** | Tâche « \Windows Update » créée |
| 10:15 | TaskScheduler **200** | Action démarrée |
| 10:15 | Security **4688** | `powershell.exe` exécuté |
| 10:15 | EDR / réseau | Connexion vers le C2 de l’attaquant |
| 12:03 | Security **4702** | Tâche modifiée |
| 15:47 | **4699** / **141** | Tâche supprimée |

→ **Persistence → Execution → C2 → Cleanup**, reconstruit même si la tâche a disparu du système.

## Points à rechercher en SOC

- tâches nouvellement créées ;
- noms ressemblant à Microsoft / Windows ;
- exécutables dans `%TEMP%`, `%APPDATA%`, `Downloads` ;
- PowerShell / CMD / WScript / MSHTA ;
- URLs ou IP dans les arguments ;
- tâche exécutée sous `SYSTEM` ;
- triggers inhabituels ;
- tâches créées puis rapidement supprimées ;
- modifications pendant la fenêtre d’incident.

> Plusieurs de ces caractéristiques réunies → suspicion élevée. Les Event Logs permettent de reconstruire **la création, les modifications, l’exécution et la suppression** d’une tâche : une source clé pour détecter la **Persistence / Execution** basée sur `T1053.005`.
