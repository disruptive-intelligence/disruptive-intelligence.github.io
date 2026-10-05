---
title: "Lire, filtrer et exporter"
---

# Lire, filtrer et exporter

Ouvrir un journal, le lister, le lire, le filtrer par identifiant et par période, en extraire les champs ; l'exporter, voir la politique d'audit, l'agrandir.

Les incontournables : `eventvwr.msc` · `Get-WinEvent -FilterHashtable` · `wevtutil` · `auditpol /get`
{ .kw-cs-top }

## Lire

### Ouvrir un journal dans l'Observateur d'événements

```bat title="Commande"
eventvwr.msc   :: Observateur d'événements
```

| Je cherche… | Chemin dans l'Observateur |
|---|---|
| Ouvertures de session, comptes, privilèges | Journaux Windows → **Security** |
| Services, pilotes, démarrages | Journaux Windows → **System** |
| Connexions RDP reçues (1149, 261) | Journaux des applications et des services → Microsoft → Windows → **TerminalServices-RemoteConnectionManager** → Operational |
| Sessions RDP ouvertes, déconnectées, reconnectées (21, 24, 25) | Journaux des applications et des services → Microsoft → Windows → **TerminalServices-LocalSessionManager** → Operational |
| Connexions RDP **émises** par ce poste (1102) | Journaux des applications et des services → Microsoft → Windows → **TerminalServices-RDPClient** → Operational |
| Tâches planifiées (106, 140, 141, 200, 201) | Journaux des applications et des services → Microsoft → Windows → **TaskScheduler** → Operational |
| Scripts PowerShell (4104) | Journaux des applications et des services → Microsoft → Windows → **PowerShell** → Operational |
| Journaux des applications et des services → Microsoft → Windows → Sysmon → Operational | Journaux des applications et des services → Microsoft → Windows → **Sysmon** → Operational |

Clic droit sur le journal → **Filtrer le journal actuel** : Event ID (plusieurs séparés par des virgules, plages avec un tiret, exclusions précédées de `-`), source, période. L'onglet **Détails** d'un événement montre tous ses champs en XML.

!!! warning "Attention"
    « Effacer le filtre » réaffiche simplement tout le journal ; « Effacer le journal » le **vide** (et produit un 1102). Ne jamais confondre les deux en investigation.

Pour comprendre : [Event Viewer, filtres et détails d'un événement](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#event-viewer-observateur-devenements) · [Les journaux et leur emplacement](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/01-comprendre-les-journaux-windows.md#applications-and-services-logs)
{ .kw-cs-meta }

### Lister les journaux et leur taille

```powershell title="Commande"
Get-WinEvent -ListLog * | Where-Object RecordCount -gt 0 | Sort-Object RecordCount -Descending
```

```powershell title="Exemple"
Get-WinEvent -ListLog Security, System, 'Microsoft-Windows-PowerShell/Operational' |
    Select-Object LogName, RecordCount, @{n='Max (Mo)';e={$_.MaximumSizeInBytes/1MB}}
```

??? example "Sortie"
    ```text
    LogName                                 RecordCount Max (Mo)
    -------                                 ----------- --------
    Security                                     184211      128
    System                                        42177       20
    Microsoft-Windows-PowerShell/Operational      12955       15
    ```

### Lire les derniers événements d'un journal

```powershell title="Commande"
Get-WinEvent -LogName <journal> -MaxEvents <n>
```

```powershell title="Exemple"
Get-WinEvent -LogName System -MaxEvents 3 | Select-Object TimeCreated, Id, ProviderName, Message
```

??? example "Sortie"
    ```text
    TimeCreated          Id ProviderName                       Message
    -----------          -- ------------                       -------
    02/10/2026 09:44:10 7036 Service Control Manager           Le service Windows Update est entré dans l'état : en cours d'exécution.
    02/10/2026 09:30:02 7040 Service Control Manager           Le type de démarrage du service Background Intelligent Transfer Service…
    02/10/2026 08:01:55 6005 EventLog                          Le service Journal des événements a été démarré.
    ```

```bat title="Exemple 2"
wevtutil qe System /c:3 /rd:true /f:text   :: /c : nombre, /rd:true : du plus récent au plus ancien
```

### Filtrer par identifiant et par période

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='<journal>'; Id=<id1>,<id2>; StartTime=<date>; EndTime=<date>}
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddHours(-2)} |
    Measure-Object | Select-Object Count
```

??? example "Sortie"
    ```text
    Count
    -----
      214
    ```

`-FilterHashtable` filtre côté journal : beaucoup plus rapide qu'un `Where-Object` après coup.

Pour comprendre : [Filtrer avec Get-WinEvent (provider, ID, période)](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#get-winevent) · [Event Viewer, wevtutil ou Get-WinEvent](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#event-viewer-vs-wevtutil-vs-get-winevent)
{ .kw-cs-meta }

### Extraire les champs d'un événement

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='<journal>'; Id=<id>} | ForEach-Object {
    $x = [xml]$_.ToXml(); $d = @{}; $x.Event.EventData.Data | ForEach-Object { $d[$_.Name] = $_.'#text' }
    [pscustomobject]@{ Heure = $_.TimeCreated; Champ1 = $d['<NomDuChamp>'] } }
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddHours(-2)} | ForEach-Object {
    $x = [xml]$_.ToXml(); $d = @{}; $x.Event.EventData.Data | ForEach-Object { $d[$_.Name] = $_.'#text' }
    [pscustomobject]@{ Compte = $d['TargetUserName']; Source = $d['IpAddress'] } } |
    Group-Object Source | Sort-Object Count -Descending | Select-Object -First 3 Count, Name
```

??? example "Sortie"
    ```text
    Count Name
    ----- ----
      198 192.168.1.77
       12 192.168.1.15
        4 -
    ```

Ensuite : [retrouver les ouvertures de session](sessions-rdp.md#retrouver-les-ouvertures-de-session)
{ .kw-cs-meta }

## Exporter et configurer

### Exporter un journal pour l'analyser ailleurs

```bat title="Commande"
wevtutil epl <journal> <fichier.evtx>   :: copie cohérente, même si le journal est ouvert
```

```bat title="Exemple"
wevtutil epl Security E:\collecte\PC-COMPTA-07_Security.evtx
```

```powershell title="Exemple 2"
Get-WinEvent -Path E:\collecte\PC-COMPTA-07_Security.evtx -FilterXPath "*[System[EventID=4624]]" -MaxEvents 5   # relire un .evtx exporté
```

Pour comprendre : [Export des événements et wevtutil](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#export-des-evenements)
{ .kw-cs-meta }

### Voir la politique d'audit active

```bat title="Commande"
auditpol /get /category:*   :: console administrateur
```

```bat title="Exemple"
auditpol /get /subcategory:"Création du processus","Ouvrir la session"
```

??? example "Sortie"
    ```text
    Catégorie/Sous-catégorie                  Paramètre
    Suivi détaillé
      Création du processus                   Succès
    Ouverture/Fermeture de session
      Ouvrir la session                       Succès et échec
    ```

### Agrandir un journal

```bat title="Commande"
wevtutil sl <journal> /ms:<octets>   :: taille maximale
```

```bat title="Exemple"
wevtutil sl Security /ms:1073741824   :: 1 Go
```

!!! warning "Attention"
    En parc, régler la taille et l'audit par GPO plutôt que machine par machine, et centraliser vers le SIEM.

## Vue d'ensemble

Les journaux utiles en investigation, leur nom pour `Get-WinEvent -FilterHashtable @{LogName=…}` et leurs Event IDs clés.

| Journal | Nom à donner à `LogName` | Event IDs clés | Fiche |
|---|---|---|---|
| Journaux Windows → Security | `Security` | 4624, 4625, 4648, 4688, 4720, 4732, 4698, 1102, 1100 | [Sessions](sessions-rdp.md), [processus](processus-powershell.md), [persistance](persistance.md), [effacement](effacement.md) |
| Journaux Windows → System | `System` | 7045, 7040, 7036, 104 | [Persistance](persistance.md), [effacement](effacement.md) |
| Journaux des applications et des services → Microsoft → Windows → TerminalServices-RemoteConnectionManager → Operational | `Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational` | 261, 1149 | [Sessions et RDP](sessions-rdp.md) |
| Journaux des applications et des services → Microsoft → Windows → TerminalServices-LocalSessionManager → Operational | `Microsoft-Windows-TerminalServices-LocalSessionManager/Operational` | 21, 24, 25 | [Sessions et RDP](sessions-rdp.md) |
| Journaux des applications et des services → Microsoft → Windows → TerminalServices-RDPClient → Operational | `Microsoft-Windows-TerminalServices-RDPClient/Operational` | 1102 | [Sessions et RDP](sessions-rdp.md) |
| Journaux des applications et des services → Microsoft → Windows → TaskScheduler → Operational | `Microsoft-Windows-TaskScheduler/Operational` | 106, 140, 141, 200, 201 | [Persistance](persistance.md) |
| Journaux des applications et des services → Microsoft → Windows → PowerShell → Operational | `Microsoft-Windows-PowerShell/Operational` | 4104, 4103 | [Processus et PowerShell](processus-powershell.md) |
| Journaux des applications et des services → Microsoft → Windows → Windows Firewall With Advanced Security → Firewall | `Microsoft-Windows-Windows Firewall With Advanced Security/Firewall` | 2004, 2005, 2003 | [Pare-feu et Defender](pare-feu-defender.md) |
| Journaux des applications et des services → Microsoft → Windows → Windows Defender → Operational | `Microsoft-Windows-Windows Defender/Operational` | 1116, 1117, 5001, 5007 | [Pare-feu et Defender](pare-feu-defender.md) |
| Journaux des applications et des services → Microsoft → Windows → Sysmon → Operational | `Microsoft-Windows-Sysmon/Operational` | 1, 3, 11, 13, 22 | [Processus et PowerShell](processus-powershell.md) |
