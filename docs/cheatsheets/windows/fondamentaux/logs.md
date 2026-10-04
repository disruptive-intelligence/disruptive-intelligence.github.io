---
title: "Journaux et événements"
cours:
  - library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/index.md
  - library/it/windows/windows-en-profondeur/index.md
---

# Journaux et événements

Lire les journaux Windows, filtrer par identifiant et par période, retrouver les ouvertures de session, les processus lancés, les services et tâches créés, les scripts PowerShell ; exporter pour analyse.

Les incontournables : `Get-WinEvent -FilterHashtable` · `wevtutil` · `eventvwr.msc` · `auditpol /get` · `Get-WinEvent -Path`
{ .kw-cs-top }

## Lire

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

Ensuite : [retrouver les ouvertures de session](#retrouver-les-ouvertures-de-session)
{ .kw-cs-meta }

## Retrouver une activité

### Retrouver les ouvertures de session

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624}   # 4625 = échecs, 4634/4647 = fermetures
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624; StartTime=(Get-Date).AddDays(-1)} | ForEach-Object {
    $x = [xml]$_.ToXml(); $d = @{}; $x.Event.EventData.Data | ForEach-Object { $d[$_.Name] = $_.'#text' }
    [pscustomobject]@{ Heure=$_.TimeCreated; Compte=$d['TargetUserName']; Type=$d['LogonType']; Source=$d['IpAddress'] } } |
    Where-Object Type -in 3,10 | Select-Object -First 3
```

??? example "Sortie"
    ```text
    Heure                Compte     Type Source
    -----                ------     ---- ------
    02/10/2026 09:44:07  adm.martin 10   192.168.1.15
    02/10/2026 09:12:33  svc_backup 3    192.168.1.40
    02/10/2026 08:01:12  alice      3    192.168.1.10
    ```

| Logon Type | Signification |
|---|---|
| 2 | Interactif (console) |
| 3 | Réseau (partage SMB) |
| 4 / 5 | Tâche planifiée / service |
| 7 | Déverrouillage |
| 9 | Nouveaux identifiants (`runas /netonly`) |
| 10 | Bureau à distance (RDP) |
| 11 | Identifiants mis en cache |

Pour comprendre : [Analyse des journaux Windows, authentification et ouvertures de session](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/04-authentification-et-ouvertures-de-session.md)
{ .kw-cs-meta }

### Retrouver les processus lancés

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4688}                                   # si l'audit est activé
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1}          # si Sysmon est installé
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1} -MaxEvents 200 |
    Where-Object Message -match 'ParentImage:.*WINWORD' | Select-Object -First 1 -ExpandProperty Message
```

??? example "Sortie"
    ```text
    Process Create:
    UtcTime: 2026-10-02 07:15:01.284
    Image: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
    CommandLine: "powershell.exe" -nop -w hidden -File C:\Users\alice\AppData\Local\Temp\maj.ps1
    User: MERIDIAN\alice
    ParentImage: C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE
    ```

!!! warning "Attention"
    Sans la GPO *Include command line in process creation events*, l'événement 4688 ne contient pas la ligne de commande.

### Retrouver les services et tâches planifiées créés

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='System'; Id=7045}     # service installé
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4698}   # tâche planifiée créée (audit requis)
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='System'; Id=7045} -MaxEvents 2 | Select-Object TimeCreated, Message | Format-List
```

??? example "Sortie"
    ```text
    TimeCreated : 01/10/2026 23:12:40
    Message     : Un service a été installé sur le système.
                  Nom du service :  UpdaterSvc
                  Nom du fichier du service :  C:\ProgramData\Updater\upd.exe
                  Type de démarrage du service :  démarrage automatique
                  Compte du service :  LocalSystem
    ```

Ensuite : [voir le binaire, le compte et le mode de démarrage d'un service](processus.md#voir-le-binaire-le-compte-et-le-mode-de-demarrage-dun-service)
{ .kw-cs-meta }

### Retrouver les scripts PowerShell exécutés

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational'; Id=4104}   # Script Block Logging
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational'; Id=4104} -MaxEvents 50 |
    Where-Object Message -match 'DownloadString|FromBase64String|Invoke-Expression' |
    Select-Object -First 1 TimeCreated, @{n='Extrait';e={$_.Message.Substring(0,120)}}
```

??? example "Sortie"
    ```text
    TimeCreated          Extrait
    -----------          -------
    02/10/2026 09:15:03  Création du texte Scriptblock (1 sur 1) : $d = [System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String(…
    ```

### Repérer un effacement de journal

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=1102}   # journal de sécurité effacé
Get-WinEvent -FilterHashtable @{LogName='System'; Id=104}      # autre journal effacé
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=1102} -ErrorAction SilentlyContinue | Select-Object TimeCreated, Message
```

??? example "Sortie"
    ```text
    TimeCreated          Message
    -----------          -------
    01/10/2026 23:20:11  Le journal d'audit a été effacé. Sujet : … Nom du compte : adm.martin …
    ```

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

## Repères : quel événement pour quoi

| Event ID | Journal | Signification |
|---|---|---|
| 4624 / 4625 | Security | Ouverture de session réussie / échouée |
| 4648 | Security | Ouverture avec identifiants explicites |
| 4672 | Security | Session avec privilèges spéciaux (admin) |
| 4688 | Security | Processus créé |
| 4697 / 7045 | Security / System | Service installé |
| 4698 | Security | Tâche planifiée créée |
| 4720 / 4732 | Security | Compte créé / ajouté à un groupe local |
| 4740 | Security | Compte verrouillé |
| 4768 / 4769 / 4771 / 4776 | Security (DC) | Kerberos TGT / ticket de service / échec de pré-auth / validation NTLM |
| 1102 / 104 | Security / System | Journal effacé |
| 4104 | PowerShell/Operational | Bloc de script exécuté |
| 1, 3, 11, 13, 22 | Sysmon | Processus, réseau, fichier, registre, DNS |
| 1149, 21, 25 | TerminalServices | Connexion RDP, ouverture, reconnexion |
