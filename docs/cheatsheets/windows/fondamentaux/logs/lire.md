---
title: "Lire, filtrer et exporter"
---

# Lire, filtrer et exporter

Ouvrir un journal, le lister, le lire, le filtrer par identifiant et par période, voir et extraire ses champs (`.ToXml()`, `Properties`), chercher un mot ; l'exporter, voir la politique d'audit, l'agrandir.

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

Lecture de `@{…}` : une condition par paire `clé=valeur`, séparées par `;` ; toutes doivent être vraies ; `Id=4624,4625` = 4624 **ou** 4625. Clés utiles : `LogName` ou `Path` (fichier `.evtx`), `ProviderName`, `Id`, `Level` (2 erreur, 3 avertissement), `StartTime`, `EndTime`.

Pour comprendre : [Filtrer avec Get-WinEvent (provider, ID, période)](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#get-winevent) · [Event Viewer, wevtutil ou Get-WinEvent](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#event-viewer-vs-wevtutil-vs-get-winevent)
{ .kw-cs-meta }

### Voir les champs d'un événement

```powershell title="Commande"
$e = Get-WinEvent -FilterHashtable @{LogName='<journal>'; Id=<id>} -MaxEvents 1
([xml]$e.ToXml()).Event.EventData.Data
```

```powershell title="Exemple"
$e = Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=3} -MaxEvents 1
([xml]$e.ToXml()).Event.EventData.Data
```

??? example "Sortie"
    ```text
    Name            #text
    ----            -----
    ProcessGuid     {52ff3419-a7bc-647b-1901-000000001000}
    ProcessId       2480
    Image           C:\Windows\System32\svchost.exe
    SourceIp        192.168.1.15
    DestinationIp   203.0.113.10
    DestinationPort 443
    ```

`Name` : le nom exact du champ, à réutiliser dans les filtres ; `#text` : sa valeur. C'est la même liste que l'onglet **Details → XML View** de l'Observateur.

```powershell title="Exemple 2 — un seul champ"
(([xml]$e.ToXml()).Event.EventData.Data | Where-Object Name -eq 'DestinationIp').'#text'
```

### Extraire les champs d'un événement

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='<journal>'; Id=<id>} | ForEach-Object {
    $data = ([xml]$_.ToXml()).Event.EventData.Data
    [pscustomobject]@{
        Heure  = $_.TimeCreated
        Champ1 = ($data | Where-Object Name -eq '<NomDuChamp1>').'#text'
        Champ2 = ($data | Where-Object Name -eq '<NomDuChamp2>').'#text'
    }
}
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddHours(-2)} | ForEach-Object {
    $data = ([xml]$_.ToXml()).Event.EventData.Data
    [pscustomobject]@{
        Compte = ($data | Where-Object Name -eq 'TargetUserName').'#text'
        Source = ($data | Where-Object Name -eq 'IpAddress').'#text'
    }
} | Group-Object Source | Sort-Object Count -Descending | Select-Object -First 3 Count, Name
```

??? example "Sortie"
    ```text
    Count Name
    ----- ----
      198 192.168.1.77
       12 192.168.1.15
        4 -
    ```

```powershell title="Exemple 2 — les derniers processus lancés et leur parent (Sysmon 1)"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1} -MaxEvents 10 | ForEach-Object {
    $data = ([xml]$_.ToXml()).Event.EventData.Data
    [pscustomobject]@{
        Heure       = $_.TimeCreated
        Image       = ($data | Where-Object Name -eq 'Image').'#text'
        CommandLine = ($data | Where-Object Name -eq 'CommandLine').'#text'
        ParentImage = ($data | Where-Object Name -eq 'ParentImage').'#text'
    }
} | Format-List
```

Lecture : `ForEach-Object` traite chaque événement (`$_`) ; `[xml]$_.ToXml()` lit son XML ; `.Event.EventData.Data` donne la liste des champs ; `Where-Object Name -eq '…'` en choisit un ; `.'#text'` en prend la valeur ; `[pscustomobject]@{…}` fabrique une ligne de tableau. Le nom des champs se lit avec [Voir les champs d'un événement](#voir-les-champs-dun-evenement).

Pour comprendre : [Extraire les champs avec .ToXml(), pas à pas](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#pas-a-pas-du-xml-au-champ-voulu)
{ .kw-cs-meta }

### Lire un champ par son numéro

```powershell title="Commande"
$e = Get-WinEvent -FilterHashtable @{LogName='<journal>'; Id=<id>} -MaxEvents 1
for ($i = 0; $i -lt $e.Properties.Count; $i++) { "$i : $($e.Properties[$i].Value)" }
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1} |
    Where-Object { $_.Properties[21].Value -like '*-enc*' } | Format-List TimeCreated, Message
```

??? example "Sortie de la commande (Sysmon 1, raccourcie)"
    ```text
    0 : -
    1 : 2023-06-03 20:51:08.538
    2 : 52ff3419-a7bc-647b-1901-000000001000
    3 : 2480
    4 : C:\Windows\System32\SecurityHealthHost.exe
    ...
    10 : C:\Windows\System32\SecurityHealthHost.exe {08728914-3F57-4D52-9E31-49DAECA5A80A} -Embedding
    ...
    20 : C:\Windows\System32\svchost.exe
    21 : C:\Windows\system32\svchost.exe -k DcomLaunch -p
    ```

`Properties` = les valeurs de l'onglet **Details**, dans l'ordre, numérotées à partir de 0. Sysmon 1 : 4 `Image`, 10 `CommandLine`, 12 `User`, 20 `ParentImage`, 21 `ParentCommandLine`. Rapide à écrire, mais le numéro peut changer d'une version de Sysmon à l'autre : vérifier avec la boucle, ou passer par le nom du champ ([Extraire les champs d'un événement](#extraire-les-champs-dun-evenement)).

### Chercher un mot dans le message

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='<journal>'; Id=<id>} | Where-Object { $_.Message -like '*<mot>*' }
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1} |
    Where-Object { $_.Message -like '*EulaAccepted*' } | Format-List TimeCreated, Message
```

`-like '*mot*'` : contient « mot » (`*` = n'importe quoi). `-match 'clr\.dll'` : même idée avec une expression régulière. Toujours filtrer d'abord par journal et ID (`-FilterHashtable`), puis chercher le mot : sinon tout le journal est lu.

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
| Journaux des applications et des services → Microsoft → Windows → Sysmon → Operational | `Microsoft-Windows-Sysmon/Operational` | 1, 3, 11, 13, 22 | [Sysmon et requêtes SIEM](sysmon.md) |
