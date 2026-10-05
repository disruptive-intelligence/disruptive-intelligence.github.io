---
title: "Processus et PowerShell"
---

# Processus et PowerShell

Les processus lancés (4688) et le code PowerShell exécuté (4104, 4103).

Les incontournables : `4688` · `4104` · `4103`
{ .kw-cs-top }

## Processus et scripts

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

### Retrouver les scripts PowerShell exécutés

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational'; Id=4104}   # Script Block Logging : le code exécuté
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational'; Id=4103}   # Module Logging : cmdlets et paramètres
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

À chercher dans un 4104 : `-EncodedCommand`, `IEX` / `Invoke-Expression`, `FromBase64String`, `DownloadString`, `Invoke-WebRequest`, `WebClient`. Un long script est découpé en plusieurs 4104 (« 1 sur 3 », « 2 sur 3 »…) : les rassembler par `ScriptBlockId`. `whoami`, `Get-LocalUser`, `Get-LocalGroup` seuls ne prouvent rien ; juste après une connexion suspecte, ils dessinent une reconnaissance. Sans Script Block Logging activé (GPO), tout le code n'est pas journalisé.

Pour comprendre : [Exécution PowerShell : 4104, 4103, transcription, corrélations](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/12-execution-powershell.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Event ID | Journal | Signification | À retenir |
|---|---|---|---|
| **4688** | Security | Processus créé | Ligne de commande seulement si la GPO « Include command line » est activée |
| **1** | Sysmon | Processus créé | Plus riche que 4688 : hash, processus parent, ligne de commande |
| **4104** | PowerShell/Operational | Script Block Logging : code exécuté | Rassembler les fragments par `ScriptBlockId` ; chercher `-EncodedCommand`, `IEX`, `FromBase64String`, `DownloadString` |
| **4103** | PowerShell/Operational | Module Logging : cmdlets et paramètres | Complète 4104 |

Chaîne typique : 4688 `powershell.exe` → 4104 (code) → connexion réseau (EDR, pare-feu).
