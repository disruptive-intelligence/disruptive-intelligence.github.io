---
title: "Services et démarrage"
cours:
  - library/it/windows/powershell/index.md
  - library/it/windows/windows-en-profondeur/index.md
---

# Services et démarrage

Démarrer, arrêter, redémarrer un service ; changer son mode de démarrage ; voir tout ce qui démarre avec la machine.

Les incontournables : `Start-Service` · `Stop-Service` · `Set-Service` · `sc.exe config` · `Autoruns`
{ .kw-cs-top }

## Piloter un service

### Démarrer, arrêter, redémarrer un service

```powershell title="Commande"
Start-Service <nom>
Stop-Service <nom>
Restart-Service <nom>
```

```powershell title="Exemple"
Restart-Service Spooler -PassThru
```

??? example "Sortie"
    ```text
    Status   Name               DisplayName
    ------   ----               -----------
    Running  Spooler            Spouleur d'impression
    ```

```bat title="Exemple 2"
sc.exe stop Spooler
net start Spooler
```

### Changer le mode de démarrage

```powershell title="Commande"
Set-Service -Name <nom> -StartupType <Automatic|AutomaticDelayedStart|Manual|Disabled>
```

```powershell title="Exemple"
Set-Service -Name Spooler -StartupType Disabled   # spouleur inutile sur un contrôleur de domaine
```

```bat title="Exemple 2"
sc.exe config Spooler start= disabled   :: l'espace après « start= » est obligatoire
```

### Voir les dépendances d'un service

```powershell title="Commande"
Get-Service <nom> -DependentServices   # qui dépend de lui
Get-Service <nom> -RequiredServices    # de qui il dépend
```

```powershell title="Exemple"
Get-Service LanmanServer -DependentServices
```

## Ce qui démarre avec la machine

### Voir tout ce qui démarre avec la machine

```bat title="Commande"
autorunsc.exe -accepteula -a * -c -h -s -m > autoruns.csv   :: Sysinternals : toutes les familles, CSV, hash, signatures, hors Microsoft
```

```powershell title="Exemple"
Get-CimInstance Win32_Service | Where-Object { $_.StartMode -eq 'Auto' -and $_.PathName -notmatch 'Windows\\system32' } |
    Select-Object Name, StartName, PathName
```

??? example "Sortie"
    ```text
    Name        StartName   PathName
    ----        ---------   --------
    MsMpSvc     LocalSystem "C:\ProgramData\Microsoft\Windows Defender\Platform\…\MsMpEng.exe"
    UpdaterSvc  LocalSystem C:\ProgramData\Updater\upd.exe
    ```

| Famille | Où regarder |
|---|---|
| Services | `Get-CimInstance Win32_Service`, `HKLM\SYSTEM\CurrentControlSet\Services` |
| Clés Run | [Registre](../fondamentaux/registre.md#voir-ce-qui-se-lance-a-louverture-de-session) |
| Tâches planifiées | [Tâches planifiées](taches.md) |
| Dossiers de démarrage | `shell:startup`, `shell:common startup` |
| WMI | `Get-CimInstance -Namespace root\subscription -ClassName __EventFilter` (et `__EventConsumer`, `__FilterToConsumerBinding`) |

Pour comprendre : [Windows en profondeur, ch. 23 (persistance)](../../../library/it/windows/windows-en-profondeur/index.md)
{ .kw-cs-meta }

### Ouvrir les dossiers de démarrage

```bat title="Commande"
explorer shell:startup          :: utilisateur courant
explorer "shell:common startup" :: tous les utilisateurs
```

```powershell title="Exemple"
Get-ChildItem "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup", "$env:ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
```

## Vue d'ensemble

| Mode de démarrage | `Set-Service -StartupType` | `sc.exe config <nom> start=` | Effet |
|---|---|---|---|
| Automatique | `Automatic` | `auto` | Démarre avec Windows |
| Automatique différé | `AutomaticDelayedStart` | `delayed-auto` | Démarre peu après le démarrage |
| Manuel | `Manual` | `demand` | Démarre à la demande |
| Désactivé | `Disabled` | `disabled` | Ne peut pas démarrer |

| Action | PowerShell | `sc.exe` |
|---|---|---|
| Démarrer, arrêter | `Start-Service` · `Stop-Service` | `sc.exe start` · `sc.exe stop` |
| Voir la configuration | `Get-CimInstance Win32_Service` | `sc.exe qc <nom>` |
| Dépendances | `Get-Service -DependentServices` · `-RequiredServices` | `sc.exe enumdepend <nom>` |
| Tout ce qui démarre | `autorunsc.exe -a *` | — |

Dossiers de démarrage : `shell:startup` = `C:\Users\<utilisateur>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` ; `shell:common startup` = `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`.
