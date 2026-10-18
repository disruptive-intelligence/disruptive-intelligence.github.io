---
title: Lire et filtrer les journaux
source: IT/02 Windows/Journaux & investigation/Analyse des journaux d'événements Windows (Event Logs).md
note: Analyse des journaux d'événements Windows (Event Logs)
up:
- - Analyse des journaux d'événements Windows (Event Logs)
  - index.md
---

## Analyse des journaux d’événements Windows
Trois outils natifs permettent principalement de consulter et analyser les **Windows Event Logs** :

```text
Event Viewer
→ GUI

wevtutil
→ CLI

Get-WinEvent
→ PowerShell
```

## Event Viewer — Observateur d’événements

- Interface graphique native de Windows pour :
    - consulter les Event Logs ;
    - examiner le détail d’un événement ;
    - filtrer les événements ;
    - exporter les résultats.

Lancement :

```text
eventvwr.msc
```


![Lancement de l Observateur d evenements|336x383](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-01.png)

![Interface principale de l Observateur d evenements|506x230](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-02.png)

### Organisation
Dans `Windows Logs`, on retrouve notamment :

```text
Application
Security
System
Setup
Forwarded Events
```

![Developper Windows Logs](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-03.png)

![Selection du journal System](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-04.png)
Lorsqu’un journal est sélectionné, le panneau central affiche notamment :

- `Level` ;
- `Date and Time` ;
- `Source / Provider` ;
- `Event ID` ;
- `Task Category`.

![Liste des evenements du journal System](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-05.png)
## Détails d’un événement

En ouvrant un événement, on peut retrouver :

```text
Event ID
Level
Provider / Source
Logged Time
Computer
User
Task Category
Message
Event Data
```

Deux vues principales sont disponibles :

### General
![Selection d un evenement|417x324](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-06.png)

![Message et informations generales de l evenement|557x111](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-07.png)

![Champs de l evenement selectionne|493x136](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-08.png)

- Vue lisible présentant le message et les principaux attributs.

### Details
Permet d’afficher :

```text
Friendly View
ou
XML View
```

La vue XML est particulièrement intéressante pour l’analyse technique car elle expose directement les champs structurés de l’événement.

```xml
<Event>
  <System>...</System>
  <EventData>...</EventData>
</Event>
```


![Vue Details en affichage convivial|428x275](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-09.png)
![Vue Details en XML|432x251](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-10.png)

### Exemple : Application → SideBySide → Event ID 35

![Erreur SideBySide, Event ID 35](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-windows-event-logs-05.png)

- Cet événement décrit une erreur de génération du contexte d'activation d'une application, liée ici à une incompatibilité d'architecture.
- L'onglet `Details` donne les données structurées de l'en-tête (`System`), notamment :
    - `SystemTime` : timestamp ;
    - `EventRecordID` : numéro de l'enregistrement ;
    - `ProcessID` : identifiant du processus associé ;
    - `ThreadID` : identifiant du thread ;
    - `Computer` : machine source.

![Onglet Details de l'Event 35 : provider, version, level, date de creation](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-windows-event-logs-06.png)

![Details : SystemTime, EventRecordID, ProcessID, ThreadID, Computer](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-windows-event-logs-07.png)
## Filtrage dans Event Viewer

### Filter Current Log
Permet de filtrer selon plusieurs critères :

- Event ID ;
- niveau ;
- source ;
- date / heure ;
- utilisateur ;
- autres attributs.

![Volet Actions de l Observateur d evenements|200x357](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-11.png)

![Action Filter Current Log|343x351](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-12.png)
#### Filtrer par Event ID
Exemple :

```text
7040
```


![Saisie d un Event ID dans le filtre|483x71](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-13.png)

![Filtre configure pour l Event ID 7040|395x180](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-14.png)

![Resultats filtres sur l Event ID 7040|480x190](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-15.png)

→ affiche uniquement les événements portant cet ID.

Plusieurs Event IDs peuvent être fournis :

```text
7040,10016
```


![Saisie de plusieurs Event IDs|436x109](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-16.png)
![Resultats du filtre sur plusieurs Event IDs|530x186](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-17.png)
### Filtrage temporel
Les filtres peuvent être combinés avec une période.
![Menu de filtrage temporel|407x97](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-18.png)

![Choix d une periode|279x99](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-19.png)

![Choix d une plage personnalisee|293x118](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-20.png)

![Borne de debut de la plage|202x62](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-21.png)

![Borne de fin de la plage|380x104](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-22.png)

Exemple :
![Plage de dates configuree|354x165](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-23.png)

![Evenements correspondant aux IDs et a la plage de dates|582x166](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-24.png)
Très utile en Incident Response lorsqu’une fenêtre temporelle de compromission est déjà connue.
## Requêtes XML personnalisées

Event Viewer permet de créer des filtres XML pour effectuer des recherches plus précises.

Chemin :

`Event Viewer → Filter Current Log → XML → Edit Query Manually`

### Objectif

Dans cet exemple, la recherche porte sur :

`SubjectLogonId = 0x3E7`

![Filtre XML du journal Security sur SubjectLogonId 0x3E7](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-windows-event-logs-09.png)

L'objectif est de retrouver des événements associés à ce contexte de session afin de reconstruire une séquence d'activités.

Exemple de filtre XML :

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

Gabarits prêts à l'emploi (Event ID, période, champ, plusieurs champs, session, exclusion) : cheat sheet [Requêtes XML de l'Observateur](/cheatsheets/windows/fondamentaux/logs/requetes-xml/).

### Exemple d'investigation : 4907, 4624 et 4672

Analyse progressive de plusieurs événements Windows liés à un même contexte.

#### Event ID 4907 — paramètres d'audit modifiés sur un objet

L'Event ID 4907 est généré lorsque les paramètres d'audit d'un objet Windows sont modifiés, notamment sa SACL (System Access Control List).

![Event 4907 : modification des parametres d'audit, Logon ID 0x3E7](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-windows-event-logs-11.png)

La SACL définit quelles tentatives d'accès à un objet doivent être journalisées.

Elle est constituée d'ACE (Access Control Entries) pouvant spécifier :

- les comptes ou groupes concernés ;
- les opérations à auditer ;
- les accès réussis, échoués ou les deux.

Distinction : la SACL contrôle l'audit des accès, tandis que la DACL contrôle principalement les autorisations d'accès.

#### Analyse

Les détails de l'Event 4907 montrent :

| Champ         | Information                                          |
| ------------- | ---------------------------------------------------- |
| Process Name  | `SetupHost.exe`                                      |
| Object Type   | File                                                 |
| Object Name   | Objet associé au boot manager                        |
| OldSd / NewSd | Descripteurs de sécurité avant et après modification |

![Details de l'Event 4907 : ObjectType File, ProcessName SetupHost.exe, OldSd / NewSd](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-windows-event-logs-12.png)

Les champs `OldSd` et `NewSd` utilisent le format SDDL (Security Descriptor Definition Language).

Ils permettent d'examiner les changements apportés au descripteur de sécurité.

`SetupHost.exe` est associé à des opérations de configuration Windows. Son nom est cohérent avec une activité d'installation, mais un nom de processus légitime ne garantit pas qu'une activité soit saine.

#### Event ID 4672 — privilèges spéciaux attribués à une nouvelle session

![Events 4624 Logon puis 4672 Special Logon](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-windows-event-logs-13.png)

L'Event ID 4672 indique que des privilèges sensibles ont été attribués au token d'une nouvelle session de connexion.

Exemple :

`SeDebugPrivilege`

![Event 4672 : SYSTEM avec SeAssignPrimaryTokenPrivilege, SeDebugPrivilege](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-windows-event-logs-14.png)

Ce privilège peut permettre à un processus disposant des autorisations nécessaires d'interagir avec d'autres processus de manière privilégiée.

#### Corrélation

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

## Effacer un filtre vs effacer un journal
Deux opérations à ne pas confondre :

```text
Clear Filter
→ retire uniquement le filtre d'affichage

Clear Log
→ supprime les événements du journal
```


![Action Clear Filter dans Event Viewer](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-25.png)

> ⚠️ `Clear Log` peut supprimer une source de preuves importante lors d’une investigation.

Un effacement du journal `Security` peut lui-même laisser une trace, notamment :
## Export des événements
Event Viewer permet d’enregistrer les événements sélectionnés ou affichés.

Si un filtre est appliqué :

```text
Full Log
→ Filter
→ Displayed Events
→ Save
```


![Action de sauvegarde des evenements affiches|323x162](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-26.png)
→ seuls les événements correspondant au filtre peuvent être exportés selon l’action choisie.

Format typique :

```text
.evtx
```


Cela permet de conserver les événements pour :

- investigation ;
- forensic analysis ;
- partage ;
- archivage.

## `wevtutil`

`wevtutil.exe` est un outil CLI natif permettant de gérer les Windows Event Logs.

Fonctions principales :

- lister les journaux ;
- lire les événements ;
- exporter les logs ;
- récupérer les informations de configuration ;
- effacer un journal.

### Aide

```cmd
wevtutil.exe /?
```

![Aide de wevtutil](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-27.png)
### Lister les journaux

```cmd
wevtutil.exe el
```


![Liste des journaux avec wevtutil](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-28.png)

`el` :

```text
enum-logs
→ liste les journaux disponibles
```

### Lire des événements

Exemple :

```cmd
wevtutil.exe qe System /c:3 /rd:true /f:text
```


![Lecture des evenements System avec wevtutil](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-29.png)

Décomposition :

```text
qe System
→ Query Events du journal System

/c:3
→ retourne 3 événements

/rd:true
→ ordre inverse, les événements récents en premier

/f:text
→ sortie au format texte
```


Conceptuellement :

```text
System Log
→ Query
→ Last 3 Events
→ Text Output
```


---

## `Get-WinEvent`

- Cmdlet PowerShell destiné à consulter les Windows Event Logs, les journaux Sysmon et certains événements issus de l'infrastructure ETW.
- En threat hunting et en DFIR, elle automatise les recherches sur de gros volumes de journaux, de façon reproductible.
- Peut fonctionner sur :
    - machine locale ;
    - machine distante.
- Permet des requêtes beaucoup plus avancées grâce notamment à :
    - `FilterHashtable` ;
    - XPath ;
    - XML queries ;
    - pipeline PowerShell.

Ses principales capacités :

- Log Discovery : identifier les journaux et fournisseurs disponibles.
- Event Retrieval : récupérer des événements locaux, distants ou archivés (`.evtx`).
- Event Filtering : filtrer par Event ID, date, fournisseur ou contenu.
- XML / XPath Analysis : rechercher des champs précis dans les événements.
- Event Correlation : rapprocher plusieurs événements pour reconstruire une activité suspecte.
### Lister les journaux

```powershell
Get-WinEvent -ListLog *
```


![Liste des journaux avec Get-WinEvent](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-30.png)

Équivalent conceptuel de :

```cmd
wevtutil el
```


Avec les propriétés utiles :

```powershell
Get-WinEvent -ListLog * |
    Select-Object LogName, RecordCount, IsClassicLog, IsEnabled, LogMode, LogType |
    Format-Table -AutoSize
```


![Get-WinEvent ListLog](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-get-winevent-listlog.png)

|Propriété|Description|
|---|---|
|`LogName`|Nom du journal|
|`RecordCount`|Nombre d'événements enregistrés|
|`IsClassicLog`|Indique si le journal utilise l'ancienne infrastructure de journalisation|
|`IsEnabled`|Indique si le journal est activé|
|`LogMode`|Mode de conservation des événements|
|`LogType`|Catégorie du journal|

#### Mode de journalisation

- Circular : les événements anciens peuvent être écrasés lorsque la limite de stockage est atteinte.
    
- Retain : les événements existants sont conservés lorsque le journal atteint sa limite.
    
- AutoBackup : archivage automatique lorsque le journal est plein, selon sa configuration.
    

#### Types de journaux

Les journaux peuvent être classés notamment en :

- Administrative : événements destinés à l'administration et à la résolution de problèmes.
    
- Operational : événements détaillant les opérations d'un composant.
    
- Analytic : traces destinées à une analyse approfondie.
    
- Debug : événements particulièrement détaillés, généralement utilisés pour le diagnostic.
    

Les journaux Analytic et Debug ne sont pas nécessairement activés ou accessibles par défaut.

### Lister les fournisseurs

```powershell
Get-WinEvent -ListProvider * | Format-Table -AutoSize
```


Cette commande liste les Providers disponibles et les journaux auxquels ils écrivent (`LogLinks`). Un même fournisseur peut publier des événements dans plusieurs journaux.

![Get-WinEvent ListProvider](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-get-winevent-listprovider.png)
### Lire un journal
Exemple :

```powershell
Get-WinEvent -LogName System
```


→ retourne les événements du journal `System`.

Les 50 plus récents, avec les colonnes utiles :

```powershell
Get-WinEvent -LogName 'System' -MaxEvents 50 |
    Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message |
    Format-Table -AutoSize
```


![Get-WinEvent System MaxEvents](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-get-winevent-system-maxevents.png)

|Propriété|Fonction|
|---|---|
|`TimeCreated`|Date et heure de l'événement|
|`ID`|Event ID|
|`ProviderName`|Fournisseur ayant généré l'événement|
|`LevelDisplayName`|Niveau : Information, Warning, Error, etc.|
|`Message`|Description de l'événement|

Le même principe vaut pour un journal d'application, par exemple `Microsoft-Windows-WinRM/Operational` (administration et exécution à distance) :

```powershell
Get-WinEvent -LogName 'Microsoft-Windows-WinRM/Operational' -MaxEvents 30 |
    Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message |
    Format-Table -AutoSize
```


![Get-WinEvent WinRM MaxEvents](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-get-winevent-winrm-maxevents.png)

Par défaut, `Get-WinEvent` lit du plus récent au plus ancien. `-Oldest` inverse l'ordre, pour commencer par les premiers événements disponibles :

```powershell
Get-WinEvent -LogName 'Microsoft-Windows-WinRM/Operational' -Oldest -MaxEvents 30 |
    Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message |
    Format-Table -AutoSize
```


### Lire un fichier .evtx exporté

```powershell
Get-WinEvent -Path 'C:\Tools\chainsaw\EVTX-ATTACK-SAMPLES\Execution\exec_sysmon_1_lolbin_pcalua.evtx' -MaxEvents 5 |
    Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message
```


- `-Path` désigne le fichier à analyser : ici des événements Sysmon Event ID 1 (création de processus).
- L'analyse porte directement sur la preuve exportée, hors de la machine d'origine : Sysmon n'a pas besoin d'être encore actif sur le poste analysé.
### Filtrer selon le Provider
Exemple :

```powershell
Get-WinEvent -LogName System |
Where-Object {$_.ProviderName -match 'Service Control Manager'}
```


![Filtrage des evenements par ProviderName](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-31.png)

Workflow :

```text
System Events
→ PowerShell Pipeline
→ ProviderName = Service Control Manager
→ Matching Events
```


La capture montre des événements du provider :

```text
Service Control Manager
```


avec notamment :

```text
7040
7045
7026
```

#### ProviderName
Le `ProviderName` représente le composant ayant généré l’événement.

Exemple :

```text
ProviderName:
Service Control Manager
```


Il permet d’ajouter du contexte à l’Event ID :

```text
Event ID
+
Provider
→ Meaning
```


### Service Control Manager
Le **Service Control Manager — SCM** gère les services Windows.

Certains Event IDs visibles dans la capture :

#### Event ID 7040

```text
System
→ Service Control Manager
→ 7040
→ Start type changed
```


- Changement du **Start Type** d’un service.

Exemple :

```text
Background Intelligent Transfer Service

Automatic
→ Manual
```


En investigation, un changement inattendu du mode de démarrage d’un service peut être intéressant.

---

#### Event ID 7045

```text
System
→ Service Control Manager
→ 7045
→ A service was installed in the system
```


→ création / installation d’un nouveau service.

Particulièrement intéressant pour le SOC car les attaquants peuvent créer des services pour :

- persistence ;
- execution ;
- privilege escalation ;
- lateral movement.

```text
New Service
→ Legitimate?
ou
→ Suspicious Persistence / Execution?
```


---

#### Event ID 7026

```text
System
→ Service Control Manager
→ 7026
→ Boot-start / system-start driver(s) failed to load
```


- Signale qu’un ou plusieurs drivers `boot-start` ou `system-start` n’ont pas pu être chargés.

Ce type d’événement relève davantage du troubleshooting, mais peut également fournir du contexte lors d’une investigation.

---

### Filtrer par Event ID avec PowerShell

`Get-WinEvent` permet de filtrer directement à la source, plutôt qu’après coup avec `Where-Object`.

Exemple :

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'System'
    Id      = 7045
}
```


```text
FilterHashtable
→ filtering performed during event retrieval
```


Cela est généralement préférable à :

```powershell
Get-WinEvent -LogName System |
Where-Object {$_.Id -eq 7045}
```


car `Where-Object` récupère d’abord les événements avant de les filtrer.

```text
Where-Object
System Log → Retrieve → Filter

FilterHashtable
System Log → Filter → Retrieve
```


→ sur de gros journaux, `FilterHashtable` est généralement beaucoup plus efficace.

#### Exemple : processus et connexions Sysmon (1 et 3)

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Microsoft-Windows-Sysmon/Operational'
    ID = 1,3
} | Select-Object TimeCreated, ID, ProviderName, Message
```


Un processus créé (Sysmon 1) qui établit aussitôt une connexion réseau (Sysmon 3) peut signaler un C2, surtout si le processus ou la destination sont inhabituels :

```text
Sysmon Event ID 1
Process Creation
        ↓
Sysmon Event ID 3
Network Connection
        ↓
Investigate Potential C2
```


Event 1 + Event 3 ≠ Confirmed C2 : beaucoup d'applications légitimes font exactement cela.

`FilterHashtable` accepte aussi un fichier exporté, avec la clé `Path` :

```powershell
Get-WinEvent -FilterHashtable @{
    Path = 'C:\Tools\chainsaw\EVTX-ATTACK-SAMPLES\Execution\sysmon_mshta_sharpshooter_stageless_meterpreter.evtx'
    ID = 1,3
}
```


---

### Filtrer par Provider

Exemple équivalent :

```powershell
Get-WinEvent -FilterHashtable @{
    LogName      = 'System'
    ProviderName = 'Service Control Manager'
}
```


---

### Filtrer plusieurs Event IDs

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'System'
    Id      = 7040,7045
}
```


---

### Filtrer selon une période

```powershell
Get-WinEvent -FilterHashtable @{
    LogName   = 'System'
    StartTime = (Get-Date).AddDays(-1)
}
```


Conceptuellement :

```text
System
+
Last 24 Hours
+
Relevant Event IDs
→ Focused Investigation
```


Une plage précise, ici du 28 mai au 2 juin 2023 inclus :

```powershell
$startDate = (Get-Date -Year 2023 -Month 5 -Day 28).Date
$endDate   = (Get-Date -Year 2023 -Month 6 -Day 3).Date

Get-WinEvent -FilterHashtable @{
    LogName   = 'Microsoft-Windows-Sysmon/Operational'
    ID        = 1,3
    StartTime = $startDate
    EndTime   = $endDate
}
```


La borne de fin au 3 juin à minuit couvre intégralement la journée du 2 juin. En DFIR : réduire l'analyse à la période où l'activité suspecte a été observée.

---

### Extraire les champs d'un événement avec .ToXml()

Les événements Windows peuvent être représentés en XML, ce qui facilite l'extraction de champs spécifiques.

La méthode :

```
$event.ToXml()
```


permet d'obtenir la représentation XML d'un événement.

#### Exemple : enquêter sur une IP suspecte

Scénario : rechercher les connexions Sysmon vers l'adresse IP :

`203.0.113.10` (adresse d'exemple)

On lit les événements Sysmon ID 3 et on en extrait plusieurs champs XML :

|Champ XML|Description|
|---|---|
|`SourceIp`|Adresse IP source|
|`DestinationIp`|Adresse IP de destination|
|`ProcessGuid`|Identifiant Sysmon du processus|
|`ProcessId`|PID du processus|

Exemple condensé :

```
Get-WinEvent -FilterHashtable @{
    LogName = 'Microsoft-Windows-Sysmon/Operational'
    ID = 3
} | ForEach-Object {
    $event = $_
    $data = ([xml]$event.ToXml()).Event.EventData.Data

    $fields = @{}
    foreach ($item in $data) {
        $fields[$item.Name] = $item.'#text'
    }

    if ($fields['DestinationIp'] -eq '203.0.113.10') {
        [PSCustomObject]@{
            SourceIp      = $fields['SourceIp']
            DestinationIp = $fields['DestinationIp']
            ProcessGuid   = $fields['ProcessGuid']
            ProcessId     = $fields['ProcessId']
        }
    }
}
```


Cette recherche identifie les connexions vers l'IP sélectionnée et permet de retrouver les processus associés.

#### Pourquoi le ProcessGuid

Le `ProcessGuid` est particulièrement utile pour corréler les événements Sysmon.

Il permet notamment de relier :

```
Sysmon Event ID 3
Network Connection
       ↓
ProcessGuid
       ↓
Sysmon Event ID 1
Process Creation
       ↓
Executable / Command Line / Parent
```


Le `ProcessGuid` est généralement plus fiable qu'un PID seul pour corréler des événements sur une période, puisque les PIDs peuvent être réutilisés.

### Filtrer avec -FilterXml

Le paramètre `-FilterXml` permet d'exécuter une requête XML structurée sur les Windows Event Logs.

#### Exemple : chargement des DLL du runtime .NET

Cas du chargement, inattendu dans certains processus, des DLL du runtime .NET :

- `clr.dll`
    
- `mscoree.dll`
    

Ces bibliothèques sont associées à l'exécution du runtime .NET.

On recherche leurs chargements avec Sysmon Event ID 7 — Image Loaded.

Une requête XML peut sélectionner les événements de cette catégorie :

```
$Query = @'
<QueryList>
  <Query Id="0" Path="Microsoft-Windows-Sysmon/Operational">
    <Select Path="Microsoft-Windows-Sysmon/Operational">
      *[System[(EventID=7)]]
    </Select>
  </Query>
</QueryList>
'@

Get-WinEvent -FilterXml $Query |
    Where-Object {
        $_.Message -match '\\(clr|mscoree)\.dll\b'
    } |
    Select-Object TimeCreated, ID, Message
```


L'exemple conserve uniquement les événements faisant référence aux DLL recherchées.

On peut aussi mettre les DLL dans la condition XML elle-même : il faut alors donner le chemin complet enregistré dans `ImageLoaded`, pas seulement le nom du fichier.

#### Investigation

L'analyste peut ainsi identifier :

- le processus ayant chargé la DLL ;
    
- le chemin du module ;
    
- le compte utilisateur ;
    
- le `ProcessGuid` ;
    
- les signatures et hashes, lorsqu'ils sont disponibles.
    

Charger une bibliothèque .NET est normal pour un processus utilisant le CLR. La détection devient pertinente lorsque ce chargement est inattendu dans le contexte du processus.

### Filtrer avec -FilterXPath

Le paramètre `-FilterXPath` permet d'utiliser directement une expression XPath pour sélectionner certains événements.

#### Exemple 1 : acceptation de la licence Sysinternals

Rechercher une exécution de `reg.exe` qui modifie la clé :

`HKCU\Software\Sysinternals`

avec la valeur :

`EulaAccepted`

Cette opération peut correspondre à l'acceptation automatisée de la licence d'un outil Sysinternals.

La requête filtre les événements Sysmon Process Creation sur les champs :

- `Image` : `C:\Windows\System32\reg.exe`
    
- `CommandLine` : commande modifiant la valeur `EulaAccepted`.
    

L'objectif est de rechercher une exécution spécifique de `reg.exe` dans la télémétrie.

L'observation de cette activité peut fournir un indice d'utilisation ou de préparation d'outils Sysinternals, mais ne démontre pas à elle seule une activité malveillante.

#### Exemple 2 : connexions vers une IP

Pour rechercher directement les événements Sysmon ID 3 vers une adresse IP précise :

```
Get-WinEvent `
    -LogName 'Microsoft-Windows-Sysmon/Operational' `
    -FilterXPath "*[System[(EventID=3)] and EventData[Data[@Name='DestinationIp']='203.0.113.10']]"
```


La requête sélectionne les événements respectant simultanément :

- `EventID = 3`
    
- `DestinationIp = 203.0.113.10`
    

Avantage : filtrer directement pendant la lecture des journaux permet d'éviter de récupérer inutilement tous les événements avant de les examiner.

### Filtrer sur les propriétés d'un événement

`Get-WinEvent` retourne des objets PowerShell disposant de nombreuses propriétés exploitables.

#### Afficher toutes les propriétés

```
Get-WinEvent -FilterHashtable @{
    LogName = 'Microsoft-Windows-Sysmon/Operational'
    ID = 1
} -MaxEvents 1 | Select-Object -Property *
```


Cette commande affiche l'ensemble des propriétés de l'objet retourné.

On retrouve notamment :

- `Message`
    
- `Id`
    
- `TimeCreated`
    
- `ProviderName`
    
- `RecordId`
    
- `MachineName`
    
- `Properties`
    

Pour un événement Sysmon ID 1, le message détaillé peut inclure :

|Champ|Utilisation|
|---|---|
|`Image`|Exécutable lancé|
|`CommandLine`|Arguments du processus|
|`User`|Compte associé|
|`IntegrityLevel`|Niveau d'intégrité|
|`ProcessGuid`|Identifiant unique Sysmon du processus|
|`ParentProcessGuid`|Identifiant Sysmon du processus parent|
|`ParentImage`|Chemin du processus parent|
|`ParentCommandLine`|Ligne de commande du parent|

#### Exemple : PowerShell encodé suspect

Recherche :

```
Get-WinEvent -FilterHashtable @{
    LogName = 'Microsoft-Windows-Sysmon/Operational'
    ID = 1
} | Where-Object {
    $_.Properties[21].Value -like '*-enc*'
} | Format-List
```


#### Lire le pipeline

- `Where-Object` : filtre les événements récupérés.
    
- `$_` : représente l'événement actuellement traité.
    
- `.Properties[21].Value` : correspond à `ParentCommandLine` dans le schéma Sysmon utilisé par le lab.
    
- `-like '*-enc*'` : recherche la chaîne `-enc` n'importe où dans la valeur.
    
- `Format-List` : affiche les événements correspondants sous forme de liste détaillée.
    

Le paramètre PowerShell `-EncodedCommand`, souvent abrégé en `-enc`, permet d'exécuter une commande encodée.

Il peut être utilisé pour obfusquer des scripts malveillants, mais également dans des outils d'automatisation légitimes.

#### Ce que montre le lab

L'exemple montre des processus tels que :

```
powershell.exe
   ├── csc.exe
   └── chcp.com
```


Leurs événements Sysmon comportent une ParentCommandLine contenant `-EncodedCommand`.

Point important : le filtre recherche la ligne de commande du parent, et pas nécessairement celle du processus enfant.

Par ailleurs, l'utilisation de `.Properties[21]` est dépendante de la structure et de la version de l'événement. Dans une investigation réutilisable, il est préférable d'extraire le champ XML nommé `ParentCommandLine`.

### Choisir sa méthode de filtrage

|Méthode|Utilisation|
|---|---|
|`-LogName`|Lire un journal Windows précis|
|`-Path`|Analyser un fichier EVTX exporté|
|`-MaxEvents`|Limiter le nombre d'événements retournés|
|`-Oldest`|Lire les événements des plus anciens vers les plus récents|
|`-FilterHashtable`|Filtrer efficacement par journal, Event ID et dates|
|`-FilterXml`|Utiliser une requête XML structurée|
|`-FilterXPath`|Rechercher des événements selon des champs XML|
|`Where-Object`|Appliquer des conditions supplémentaires aux objets récupérés|
|`.ToXml()`|Extraire les champs détaillés d'un événement|

### Démarche de threat hunting avec Get-WinEvent

```
Identify Hunting Hypothesis
          ↓
Select Relevant Event Logs
          ↓
Choose Event IDs / Time Range
          ↓
Apply Hashtable / XML / XPath Filters
          ↓
Extract Relevant Event Fields
          ↓
Correlate ProcessGuid / Timestamps
          ↓
Investigate Suspicious Behavior
```


#### Points essentiels

- `Get-WinEvent` permet d'automatiser l'analyse des journaux Windows et Sysmon avec PowerShell.
    
- `FilterHashtable` est particulièrement pratique pour les recherches par Event ID et période.
    
- `FilterXml` et `FilterXPath` permettent d'effectuer des recherches plus précises dans les champs des événements.
    
- `ProcessGuid` facilite la corrélation entre exécutions de processus et connexions réseau.
    
- `ParentCommandLine` peut révéler des scripts ou commandes associés à l'origine d'une activité.
    
- Les résultats doivent être contextualisés : une commande encodée, une connexion réseau ou un chargement de DLL ne constituent pas automatiquement une compromission.
    

L'intérêt de `Get-WinEvent` est de transformer les journaux Windows en données interrogeables et corrélables, ce qui permet de passer d'une recherche manuelle dans Event Viewer à des investigations DFIR et Threat Hunting reproductibles.

---

## Event Viewer vs `wevtutil` vs `Get-WinEvent`

| Outil | Interface | Usage principal |
|---|---|---|
| **Event Viewer** | GUI | Analyse manuelle / exploration |
| **wevtutil** | CMD | Gestion et requêtes CLI |
| **Get-WinEvent** | PowerShell | Analyse, filtrage et automatisation |

```text
Event Viewer
→ rapide pour explorer visuellement

wevtutil
→ administration CLI

Get-WinEvent
→ scripting / hunting / analyse avancée
```


---

## Approche SOC

Pour une investigation, on cherchera rarement simplement :

```text
"Montre-moi tous les logs"
```


mais plutôt :

```text
Relevant Log
+
Event ID
+
Provider
+
Time Window
+
Host
+
User
→ Relevant Events
```


Exemple :

```text
System
+
Service Control Manager
+
7045
+
Incident Time Window
→ Newly Installed Services
```


Puis :

```text
New Service
→ Service Name
→ Executable Path
→ Account
→ Timestamp
→ Correlate with Process / Network / Authentication Logs
```


La puissance de ces outils vient donc moins de la simple lecture d’un `.evtx` que de la capacité à **réduire rapidement des dizaines de milliers d’événements à ceux qui sont pertinents pour l’investigation**.

Source des captures : [Hack The Box Academy - Event Log Analysis](https://academy.hackthebox.com/app/module/387/section/4529)

## Démarche de threat hunting dans les journaux

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
