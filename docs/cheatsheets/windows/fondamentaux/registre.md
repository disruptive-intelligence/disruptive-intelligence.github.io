---
title: "Registre"
cours:
  - library/it/windows/windows-en-profondeur/index.md
  - library/it/windows/powershell/index.md
---

# Registre

Lire une clé et ses valeurs, chercher dans le registre, voir ce qui se lance au démarrage, exporter avant de modifier.

Les incontournables : `Get-ItemProperty` · `Get-ChildItem HKLM:` · `reg query` · `reg export` · `Autoruns`
{ .kw-cs-top }

## Lire

### Lire les valeurs d'une clé

```powershell title="Commande"
Get-ItemProperty -Path '<HKLM:|HKCU:>\<chemin>'
```

```powershell title="Exemple"
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion' | Select-Object ProductName, DisplayVersion, CurrentBuild
```

??? example "Sortie"
    ```text
    ProductName           DisplayVersion CurrentBuild
    -----------           -------------- ------------
    Windows 10 Enterprise 23H2           22631
    ```

`ProductName` affiche encore « Windows 10 » sur Windows 11 : c'est le build (≥ 22000) qui fait foi.

```bat title="Exemple 2"
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v CurrentBuild
```

### Lister les sous-clés

```powershell title="Commande"
Get-ChildItem -Path '<HKLM:|HKCU:>\<chemin>'
```

```powershell title="Exemple"
Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall' |
    Get-ItemProperty | Where-Object DisplayName | Select-Object -First 3 DisplayName, DisplayVersion, InstallDate
```

??? example "Sortie"
    ```text
    DisplayName              DisplayVersion InstallDate
    -----------              -------------- -----------
    7-Zip 24.08 (x64)        24.08          20260312
    Google Chrome            129.0.6668.90  20260929
    Microsoft Edge           129.0.2792.65  20261001
    ```

C'est la liste des logiciels installés (ajouter `HKLM:\SOFTWARE\WOW6432Node\…\Uninstall` pour les 32 bits et `HKCU:` pour les installations par utilisateur).

### Chercher une valeur dans le registre

```bat title="Commande"
reg query <clé> /f "<texte>" /s   :: /s : récursif ; /k clés, /v valeurs, /d données
```

```bat title="Exemple"
reg query HKCU\Software /f "upd.exe" /s /d
```

??? example "Sortie"
    ```text
    HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
        Updater    REG_SZ    C:\ProgramData\Updater\upd.exe
    Fin de la recherche : 1 correspondance(s) trouvée(s).
    ```

## Démarrage et persistance

### Voir ce qui se lance à l'ouverture de session

```powershell title="Commande"
'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce',
'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce' |
  ForEach-Object { Get-ItemProperty $_ -ErrorAction SilentlyContinue | Select-Object * -ExcludeProperty PS* }
```

```bat title="Exemple"
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

??? example "Sortie"
    ```text
    HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
        OneDrive    REG_SZ    "C:\Users\alice\AppData\Local\Microsoft\OneDrive\OneDrive.exe" /background
        Updater     REG_SZ    C:\ProgramData\Updater\upd.exe
    ```

```powershell title="Exemple 2"
Get-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location, User   # clés Run et dossiers de démarrage
```

Ensuite : [voir tout ce qui démarre avec la machine](../administration/services.md#voir-tout-ce-qui-demarre-avec-la-machine)
{ .kw-cs-meta }

### Les clés à connaître

| Clé | Rôle |
|---|---|
| `HKLM\…\CurrentVersion\Run` · `RunOnce` (et `HKCU`) | Programmes lancés à l'ouverture de session |
| `HKLM\SYSTEM\CurrentControlSet\Services\<nom>` | Configuration des services (`ImagePath`, `Start`, `ObjectName`) |
| `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon` | `Shell`, `Userinit` : programmes de l'ouverture de session |
| `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options` | Débogueur associé à un exécutable |
| `HKLM\SYSTEM\CurrentControlSet\Control\Lsa` | Paramètres LSA (`RunAsPPL`) |
| `HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR` | Périphériques USB branchés |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` | Documents récents |

Pour comprendre : [Windows en profondeur, ch. 5 (registre et persistance)](../../../library/it/windows/windows-en-profondeur/01-partie-i-architecture-fondamentale/05-chapitre-5-registre-windows-ruches-et-persistance.md)
{ .kw-cs-meta }

## Modifier

### Exporter une clé avant de la modifier

```bat title="Commande"
reg export <clé> <fichier.reg>   :: restauration : reg import <fichier.reg>
```

```bat title="Exemple"
reg export "HKLM\SYSTEM\CurrentControlSet\Services\UpdaterSvc" C:\Sauvegarde\UpdaterSvc.reg
```

??? example "Sortie"
    ```text
    L'opération a réussi.
    ```

### Créer, modifier ou supprimer une valeur

```powershell title="Commande"
New-ItemProperty -Path '<clé>' -Name <nom> -Value <valeur> -PropertyType <String|DWord|…> -Force   # crée ou remplace
Remove-ItemProperty -Path '<clé>' -Name <nom>
```

```powershell title="Exemple"
New-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Lsa' -Name RunAsPPL -Value 1 -PropertyType DWord -Force
```

```bat title="Exemple 2"
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v RunAsPPL /t REG_DWORD /d 1 /f
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v Updater /f
```

!!! warning "Attention"
    Une erreur dans `HKLM` peut empêcher le démarrage : exporter la clé d'abord, et préférer une GPO pour un réglage à appliquer sur tout un parc.
