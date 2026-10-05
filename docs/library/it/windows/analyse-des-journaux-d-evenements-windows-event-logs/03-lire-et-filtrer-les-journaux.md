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

- Cmdlet PowerShell destiné à consulter les Windows Event Logs.
- Peut fonctionner sur :
    - machine locale ;
    - machine distante.
- Permet des requêtes beaucoup plus avancées grâce notamment à :
    - `FilterHashtable` ;
    - XPath ;
    - XML queries ;
    - pipeline PowerShell.
### Lister les journaux

```powershell
Get-WinEvent -ListLog *
```


![Liste des journaux avec Get-WinEvent](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-htb-event-log-analysis-30.png)

Équivalent conceptuel de :

```cmd
wevtutil el
```

### Lire un journal
Exemple :

```powershell
Get-WinEvent -LogName System
```


→ retourne les événements du journal `System`.
### Filtrer selon le Provider
Exemple du cours :

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


Le résultat de ton screenshot montre justement des événements du provider :

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

Certains Event IDs visibles dans ton screenshot :

#### Event ID 7040

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
A service was installed in the system
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

- Signale qu’un ou plusieurs drivers `boot-start` ou `system-start` n’ont pas pu être chargés.

Ce type d’événement relève davantage du troubleshooting, mais peut également fournir du contexte lors d’une investigation.

---

### Filtrer par Event ID avec PowerShell

Même si le cours commence avec `Where-Object`, `Get-WinEvent` permet de filtrer directement à la source.

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
