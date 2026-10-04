---
title: "Processus et services"
cours:
  - library/it/windows/windows-en-profondeur/index.md
  - library/it/windows/powershell/index.md
---

# Processus et services

Repérer un processus, remonter à son parent, voir sa ligne de commande, ses DLL et ses connexions, l'arrêter ; observer les services et ce que chaque `svchost.exe` héberge.

Les incontournables : `Get-Process` · `Get-CimInstance Win32_Process` · `tasklist /svc` · `Stop-Process` · `Get-Service` · `sc.exe qc`
{ .kw-cs-top }

## Observer les processus

### Lister les processus

```powershell title="Commande"
Get-Process   # alias : ps, gps
```

```powershell title="Exemple"
Get-Process | Sort-Object CPU -Descending | Select-Object -First 3 Id, ProcessName, CPU, WorkingSet
```

??? example "Sortie"
    ```text
       Id ProcessName        CPU WorkingSet
       -- -----------        --- ----------
     4812 msedge          312,45  412337152
     2290 MsMpEng         188,02  289116160
     6104 Teams           140,77  356777984
    ```

```bat title="Exemple 2"
tasklist /v   :: avec l'utilisateur et le titre de fenêtre
```

### Voir la ligne de commande et le parent de chaque processus

```powershell title="Commande"
Get-CimInstance Win32_Process | Select-Object ProcessId, ParentProcessId, Name, CommandLine
```

```powershell title="Exemple"
Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" | Select-Object ProcessId, ParentProcessId, CommandLine
```

??? example "Sortie"
    ```text
    ProcessId ParentProcessId CommandLine
    --------- --------------- -----------
         7720            6644 "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -nop -w hidden -File C:\Users\alice\AppData\Local\Temp\maj.ps1
    ```

Ensuite : [trouver le parent d'un processus](#trouver-le-parent-dun-processus)
{ .kw-cs-meta }

### Trouver le parent d'un processus

```powershell title="Commande"
$p = Get-CimInstance Win32_Process -Filter "ProcessId=<PID>"
Get-CimInstance Win32_Process -Filter "ProcessId=$($p.ParentProcessId)" | Select-Object ProcessId, Name, CommandLine
```

```powershell title="Exemple"
$p = Get-CimInstance Win32_Process -Filter "ProcessId=7720"
Get-CimInstance Win32_Process -Filter "ProcessId=$($p.ParentProcessId)" | Select-Object ProcessId, Name, CommandLine
```

??? example "Sortie"
    ```text
    ProcessId Name        CommandLine
    --------- ----        -----------
         6644 WINWORD.EXE "C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE" /n "C:\Users\alice\Downloads\facture.docm"
    ```

Un document Word qui lance PowerShell : chaîne parent → enfant à examiner en priorité.

Pour comprendre : [Windows en profondeur, ch. 31 (arbre de processus de référence)](../../../library/it/windows/windows-en-profondeur/index.md)
{ .kw-cs-meta }

### Voir l'arbre des processus

```powershell title="Commande"
# Pas d'équivalent natif de pstree : Process Explorer (Sysinternals) ou ce parcours
function Show-Tree($id, $n = 0) {
  Get-CimInstance Win32_Process -Filter "ParentProcessId=$id" | ForEach-Object {
    ('  ' * $n) + "$($_.Name) ($($_.ProcessId))"; Show-Tree $_.ProcessId ($n + 1) }
}
Show-Tree <PID>
```

```powershell title="Exemple"
Show-Tree (Get-Process -Name services).Id | Select-Object -First 4
```

??? example "Sortie"
    ```text
    svchost.exe (912)
      WmiPrvSE.exe (3380)
    svchost.exe (1004)
    svchost.exe (1088)
    ```

### Tout savoir sur un processus

```powershell title="Commande"
Get-Process -Id <PID> | Format-List *                     # toutes les propriétés
Get-Process -Id <PID> -IncludeUserName                    # compte (console administrateur)
(Get-Process -Id <PID>).Modules | Select-Object FileName  # DLL chargées
```

```powershell title="Exemple"
Get-Process -Id 7720 -IncludeUserName | Select-Object Id, UserName, Path, StartTime
```

??? example "Sortie"
    ```text
      Id UserName       Path                                                      StartTime
      -- --------       ----                                                      ---------
    7720 MERIDIAN\alice C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe 02/10/2026 09:15:01
    ```

Ensuite : [voir les connexions d'un processus](reseau.md#voir-quel-processus-ecoute-ou-communique)
{ .kw-cs-meta }

### Vérifier qu'un processus système est légitime

```powershell title="Commande"
Get-CimInstance Win32_Process -Filter "Name='<nom>'" | Select-Object ProcessId, ParentProcessId, ExecutablePath
```

```powershell title="Exemple"
Get-CimInstance Win32_Process -Filter "Name='lsass.exe'" | Select-Object ProcessId, ParentProcessId, ExecutablePath
```

??? example "Sortie"
    ```text
    ProcessId ParentProcessId ExecutablePath
    --------- --------------- --------------
          744             612 C:\Windows\system32\lsass.exe
    ```

| Processus | Parent attendu | Instances | Chemin |
|---|---|---|---|
| `smss.exe` | System (4) | 1 | `System32` |
| `wininit.exe` | (orphelin) | 1 | `System32` |
| `services.exe` | `wininit.exe` | 1 | `System32` |
| `lsass.exe` | `wininit.exe` | **1** | `System32` |
| `svchost.exe` | `services.exe` | nombreuses, avec `-k` | `System32` |
| `explorer.exe` | (orphelin, lancé par userinit) | 1 par session | `C:\Windows` |

### Arrêter un processus

```powershell title="Commande"
Stop-Process -Id <PID>          # -Force si le processus résiste
Stop-Process -Name <nom>
```

```powershell title="Exemple"
Stop-Process -Id 7720 -Force
```

```bat title="Exemple 2"
taskkill /PID 7720 /F
taskkill /IM notepad.exe /T   :: /T : avec les processus enfants
```

!!! warning "Attention"
    En investigation, ne pas tuer un processus suspect avant d'avoir relevé sa ligne de commande, son parent, ses connexions et, si possible, capturé la mémoire : l'arrêter efface ces preuves.

## Observer les services

### Lister les services et leur état

```powershell title="Commande"
Get-Service   # Status, Name, DisplayName
```

```powershell title="Exemple"
Get-Service | Where-Object Status -eq Running | Select-Object -First 3 Status, Name, DisplayName
```

??? example "Sortie"
    ```text
    Status  Name      DisplayName
    ------  ----      -----------
    Running Appinfo   Informations d'application
    Running AudioSrv  Audio Windows
    Running BFE       Moteur de filtrage de base
    ```

### Voir le binaire, le compte et le mode de démarrage d'un service

```powershell title="Commande"
Get-CimInstance Win32_Service -Filter "Name='<service>'" | Select-Object Name, State, StartMode, StartName, PathName
```

```powershell title="Exemple"
Get-CimInstance Win32_Service | Where-Object StartMode -eq Auto |
    Select-Object -First 3 Name, StartName, PathName
```

??? example "Sortie"
    ```text
    Name     StartName                   PathName
    ----     ---------                   --------
    BFE      NT AUTHORITY\LocalService   C:\Windows\system32\svchost.exe -k LocalServiceNoNetworkFirewall -p
    Dhcp     NT Authority\LocalService   C:\Windows\system32\svchost.exe -k LocalServiceNetworkRestricted -p
    MsMpSvc  LocalSystem                 "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.24080.9-0\MsMpEng.exe"
    ```

```bat title="Exemple 2"
sc.exe qc wuauserv   :: BINARY_PATH_NAME, START_TYPE, SERVICE_START_NAME, DEPENDENCIES
```

Pour comprendre : [Windows en profondeur, ch. 7 (services)](../../../library/it/windows/windows-en-profondeur/index.md)
{ .kw-cs-meta }

### Savoir ce qu'héberge chaque svchost.exe

```bat title="Commande"
tasklist /svc /fi "imagename eq svchost.exe"
```

```bat title="Exemple"
tasklist /svc /fi "imagename eq svchost.exe"
```

??? example "Sortie"
    ```text
    Nom de l'image                 PID Services
    ========================= ======== ============================================
    svchost.exe                    912 BrokerInfrastructure, DcomLaunch, PlugPlay,
                                       Power, SystemEventsBroker
    svchost.exe                   1004 RpcEptMapper, RpcSs
    ```

```powershell title="Exemple 2"
Get-CimInstance Win32_Service | Where-Object ProcessId -eq 1004 | Select-Object Name, DisplayName
```

### Lire les permissions d'un service

```bat title="Commande"
sc.exe sdshow <service>   :: descripteur au format SDDL
```

```bat title="Exemple"
sc.exe sdshow wuauserv
```

??? example "Sortie"
    ```text
    D:(A;;CCLCSWRPLORC;;;AU)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;SY)
    ```

`AU` (utilisateurs authentifiés) peut lire et démarrer ; seuls `BA` (administrateurs) et `SY` (SYSTEM) ont `DC` (modifier la configuration), `WD` et `WO`. Un groupe large avec ces droits est à corriger.

Pour comprendre : [Windows en profondeur, ch. 17 (lire le SDDL)](../../../library/it/windows/windows-en-profondeur/05-partie-v-modele-de-securite-et-protections/01-chapitre-17-modele-de-securite-integrite-et-mitiga.md)
{ .kw-cs-meta }

### Repérer un service mal configuré

```powershell title="Commande"
# Chemin du binaire avec des espaces mais sans guillemets
Get-CimInstance Win32_Service |
    Where-Object { $_.PathName -notmatch '^"' -and ($_.PathName -split '\.exe')[0] -match ' ' } |
    Select-Object Name, StartName, PathName
# Qui peut écrire dans le dossier du binaire
icacls "<dossier du binaire>"
```

```powershell title="Exemple"
Get-CimInstance Win32_Service |
    Where-Object { $_.PathName -notmatch '^"' -and ($_.PathName -split '\.exe')[0] -match ' ' } |
    Select-Object Name, StartName, PathName
```

??? example "Sortie"
    ```text
    Name     StartName   PathName
    ----     ---------   --------
    MonAgent LocalSystem C:\Program Files\Mon Agent\agent.exe
    ```

```bat title="Exemple 2"
icacls "C:\Program Files\Mon Agent"   :: Users ou Authenticated Users en (M), (W) ou (F) : à corriger
```

Sans guillemets, Windows essaie `C:\Program.exe`, puis `C:\Program Files\Mon.exe`, avant le vrai binaire ; et un dossier modifiable par tous permet de remplacer ce que le service lance avec son compte. Correction : mettre le chemin entre guillemets dans la valeur `ImagePath` de `HKLM\SYSTEM\CurrentControlSet\Services\<service>`, et réserver l'écriture du dossier aux administrateurs.

Pour comprendre : [Windows en profondeur, ch. 7 (services)](../../../library/it/windows/windows-en-profondeur/02-partie-ii-processus-execution-et-code.md)
{ .kw-cs-meta }
