---
title: "Système et arborescence"
cours:
  - library/it/windows/windows-en-profondeur/index.md
  - library/it/windows/powershell/index.md
  - library/it/windows/windows-fiche-cyber/index.md
---

# Système et arborescence

Identifier la machine (version, build, correctifs, domaine), se repérer dans l'arborescence, savoir qui est connecté.

Les incontournables : `systeminfo` · `Get-ComputerInfo` · `hostname` · `Get-HotFix` · `query user` · `Get-ChildItem Env:`
{ .kw-cs-top }

Les blocs `powershell` se tapent dans PowerShell, les blocs `bat` dans l'invite de commandes (CMD). La plupart des commandes CMD fonctionnent aussi dans PowerShell.

## Identifier la machine

### Voir la version et le build de Windows

```powershell title="Commande"
Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, BuildNumber, OSArchitecture
```

```powershell title="Exemple"
Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, BuildNumber, OSArchitecture
```

??? example "Sortie"
    ```text
    Caption                         Version    BuildNumber OSArchitecture
    -------                         -------    ----------- --------------
    Microsoft Windows 11 Entreprise 10.0.22631 22631       64 bits
    ```

```bat title="Exemple 2"
ver
winver
```

| Version | Système |
|---|---|
| 6.1 | Windows 7 / Server 2008 R2 |
| 6.2 / 6.3 | Windows 8 / 8.1 — Server 2012 / 2012 R2 |
| 10.0 (build < 22000) | Windows 10 / Server 2016, 2019, 2022 |
| 10.0 (build ≥ 22000) | Windows 11 / Server 2025 |

Ensuite : [voir les correctifs installés](#voir-les-correctifs-installes) — Pour comprendre : [Windows en profondeur, ch. 1](../../../library/it/windows/windows-en-profondeur/01-partie-i-architecture-fondamentale/01-chapitre-1-vue-d-ensemble-de-windows.md)
{ .kw-cs-meta }

### Avoir la vue d'ensemble de la machine

```bat title="Commande"
systeminfo   :: OS, build, date d'installation, dernier démarrage, domaine, correctifs, cartes réseau
```

```bat title="Exemple"
systeminfo | findstr /B /C:"Nom de l'hôte" /C:"Nom du système" /C:"Version du système" /C:"Domaine" /C:"Heure de démarrage"
```

??? example "Sortie"
    ```text
    Nom de l'hôte:                              PC-COMPTA-07
    Nom du système d'exploitation:              Microsoft Windows 11 Entreprise
    Version du système:                         10.0.22631 N/A version 22631
    Domaine:                                    meridian.local
    Heure de démarrage du système:              02/10/2026, 07:58:12
    ```

```powershell title="Exemple 2"
Get-ComputerInfo -Property CsName, CsDomain, OsName, OsVersion, OsLastBootUpTime, OsInstallDate
```

!!! warning "Attention"
    Les libellés de `systeminfo` suivent la langue du système : sur un Windows anglais, filtrer sur `"Host Name"`, `"OS Name"`, `"Domain"`… `Get-ComputerInfo` a des noms de propriétés fixes.

### Savoir si la machine est dans un domaine

```powershell title="Commande"
(Get-CimInstance Win32_ComputerSystem) | Select-Object Name, Domain, PartOfDomain
```

```powershell title="Exemple"
Get-CimInstance Win32_ComputerSystem | Select-Object Name, Domain, PartOfDomain, Manufacturer, Model
```

??? example "Sortie"
    ```text
    Name         Domain         PartOfDomain Manufacturer Model
    ----         ------         ------------ ------------ -----
    PC-COMPTA-07 meridian.local         True Dell Inc.    Latitude 5440
    ```

```bat title="Exemple 2"
nltest /dsgetdc:meridian.local   :: quel contrôleur de domaine le poste utilise
```

Ensuite : [fiche Active Directory](../administration/active-directory/index.md)
{ .kw-cs-meta }

### Voir le numéro de série et le BIOS

```powershell title="Commande"
Get-CimInstance Win32_BIOS | Select-Object Manufacturer, SerialNumber, SMBIOSBIOSVersion, ReleaseDate
```

```powershell title="Exemple"
Get-CimInstance Win32_BIOS | Select-Object Manufacturer, SerialNumber, SMBIOSBIOSVersion
```

??? example "Sortie"
    ```text
    Manufacturer SerialNumber SMBIOSBIOSVersion
    ------------ ------------ -----------------
    Dell Inc.    7HX2Q93      1.18.0
    ```

Le numéro de série identifie le poste dans l'inventaire et auprès du constructeur, par exemple pour une fiche d'incident. `Get-CimInstance` remplace `Get-WmiObject`, qui marche encore mais n'existe plus dans PowerShell 7.

### Voir les correctifs installés

```powershell title="Commande"
Get-HotFix | Sort-Object InstalledOn -Descending   # correctifs (KB) et date d'installation
```

```powershell title="Exemple"
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 3 HotFixID, Description, InstalledOn
```

??? example "Sortie"
    ```text
    HotFixID  Description     InstalledOn
    --------  -----------     -----------
    KB5043145 Update          24/09/2026 00:00:00
    KB5043080 Security Update 11/09/2026 00:00:00
    KB5042352 Update          14/08/2026 00:00:00
    ```

```bat title="Exemple 2"
wmic qfe list brief   :: équivalent CMD (wmic est déprécié mais encore présent)
```

### Savoir depuis quand la machine tourne

```powershell title="Commande"
(Get-CimInstance Win32_OperatingSystem).LastBootUpTime
```

```powershell title="Exemple"
(Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime | Select-Object Days, Hours, Minutes
```

??? example "Sortie"
    ```text
    Days Hours Minutes
    ---- ----- -------
       2     1      17
    ```

## Se repérer dans l'arborescence

### Lister un dossier, fichiers cachés compris

```powershell title="Commande"
Get-ChildItem -Force <dossier>   # -Force : fichiers cachés et système
```

```powershell title="Exemple"
Get-ChildItem -Force C:\Users\alice\AppData
```

??? example "Sortie"
    ```text
        Répertoire : C:\Users\alice\AppData

    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d-----        01/10/2026     08:12                Local
    d-----        12/03/2026     14:02                LocalLow
    d-----        01/10/2026     08:15                Roaming
    ```

```bat title="Exemple 2"
dir /a C:\ProgramData   :: /a : tous les attributs, cachés compris
tree C:\Users\alice /f | more
```

### Retrouver les dossiers clés

| Chemin | Variable | Contenu |
|---|---|---|
| `C:\Windows\System32` | `%SystemRoot%\System32` | Binaires et DLL système (64 bits) |
| `C:\Windows\SysWOW64` | — | Binaires 32 bits sur un système 64 bits |
| `C:\Windows\System32\config` | — | Ruches du registre (SAM, SYSTEM, SOFTWARE, SECURITY) |
| `C:\Program Files` / `(x86)` | `%ProgramFiles%` | Programmes installés (64 / 32 bits) |
| `C:\ProgramData` (caché) | `%ProgramData%` | Données partagées des applications |
| `C:\Users\<user>\AppData\Roaming`, `Local`, `LocalLow` | `%APPDATA%`, `%LOCALAPPDATA%` | Données de l'utilisateur, configurations, caches |
| `C:\Users\<user>\AppData\Local\Temp` | `%TEMP%` | Fichiers temporaires de l'utilisateur |
| `C:\Users\Public` | `%PUBLIC%` | Partagé entre utilisateurs locaux |
| `C:\Windows\Temp` | — | Temporaires système |

Pour comprendre : [Windows en profondeur, ch. 1](../../../library/it/windows/windows-en-profondeur/01-partie-i-architecture-fondamentale/01-chapitre-1-vue-d-ensemble-de-windows.md)
{ .kw-cs-meta }

### Afficher les variables d'environnement

```powershell title="Commande"
Get-ChildItem Env:          # toutes les variables
$env:<NOM>                  # une variable
```

```powershell title="Exemple"
$env:USERNAME; $env:COMPUTERNAME; $env:TEMP
```

??? example "Sortie"
    ```text
    alice
    PC-COMPTA-07
    C:\Users\alice\AppData\Local\Temp
    ```

```bat title="Exemple 2"
set           :: toutes les variables en CMD
echo %PATH%
```

## Savoir qui est là

### Voir qui est connecté à la machine

```bat title="Commande"
query user   :: sessions ouvertes, locales et RDP (alias : quser)
```

```bat title="Exemple"
query user
```

??? example "Sortie"
    ```text
     UTILISATEUR           SESSION            ID  ÉTAT    TEMPS INACT DATE OUVERTURE
    >alice                 console             1  Actif           aucun 02/10/2026 08:01
     adm.martin            rdp-tcp#3           2  Actif               5 02/10/2026 09:44
    ```

Ensuite : [retrouver les ouvertures de session](logs/sessions-rdp.md#retrouver-les-ouvertures-de-session)
{ .kw-cs-meta }

### Savoir qui je suis

```bat title="Commande"
whoami        :: utilisateur courant (DOMAINE\nom)
whoami /all   :: SID, groupes, privilèges, niveau d'intégrité
```

```bat title="Exemple"
whoami /user
```

??? example "Sortie"
    ```text
    INFORMATIONS SUR L'UTILISATEUR
    -------------------------------
    Nom d'utilisateur SID
    ================= =============================================
    meridian\alice    S-1-5-21-3623811015-3361044348-30300820-1104
    ```

Ensuite : [droits et identités](droits.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Je veux savoir… | Commande | À regarder |
|---|---|---|
| Version et build de Windows | `Get-CimInstance Win32_OperatingSystem` | `Caption`, `Version`, `BuildNumber` |
| Tout sur la machine d'un coup | `systeminfo` | OS, date d'installation, dernier démarrage, domaine, correctifs |
| Si la machine est dans un domaine | `Get-CimInstance Win32_ComputerSystem` | `Domain`, `PartOfDomain` |
| Numéro de série, BIOS | `Get-CimInstance Win32_BIOS` | `Manufacturer`, `SerialNumber` |
| Correctifs installés | `Get-HotFix` | `HotFixID`, `InstalledOn` |
| Depuis quand elle tourne | `(Get-CimInstance Win32_OperatingSystem).LastBootUpTime` | Date du dernier démarrage |
| Fichiers cachés d'un dossier | `Get-ChildItem -Force` | Attributs `h` (caché), `s` (système) |
| Variables d'environnement | `Get-ChildItem Env:` · `$env:<NOM>` | `%TEMP%`, `%APPDATA%`, `PATH` |
| Qui est connecté | `query user` | Sessions locales et RDP |
| Qui je suis | `whoami /all` | SID, groupes, privilèges, niveau d'intégrité |
