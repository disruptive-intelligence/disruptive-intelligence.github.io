---
title: "Logiciels et mises à jour"
cours:
  - library/it/windows/powershell/index.md
---

# Logiciels et mises à jour

Lister les logiciels installés, installer ou mettre à jour avec winget, voir l'état de Windows Update et de Defender.

Les incontournables : `winget` · `Get-HotFix` · `Get-MpComputerStatus` · `Update-MpSignature`
{ .kw-cs-top }

### Lister les logiciels installés

```powershell title="Commande"
winget list
```

```powershell title="Exemple"
winget list --source winget | Select-Object -First 4
```

??? example "Sortie"
    ```text
    Nom              ID                    Version       Disponible  Source
    ---------------------------------------------------------------------------
    7-Zip 24.08      7zip.7zip             24.08         24.09       winget
    Google Chrome    Google.Chrome         129.0.6668.90             winget
    ```

```powershell title="Exemple 2"
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*', 'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*', 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*' -ErrorAction SilentlyContinue |
    Where-Object DisplayName | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Sort-Object DisplayName
```

`HKCU` complète avec les installations de l'utilisateur courant. Cette liste reste partielle (logiciels portables, autres profils, etc.). Croiser versions, services associés, fichiers de configuration et ACL pour l'audit.

??? warning "Commandes historiques du cours : Win32_Product"
    ```bat
    wmic product get name
    ```

    ```powershell
    Get-WmiObject -Class Win32_Product | Select-Object Name, Version
    ```

    Ces requêtes n'inventorient que les produits MSI et peuvent déclencher des vérifications/réparations d'installation. Préférer les clés de désinstallation ci-dessus en production. `wmic` peut être absent ; `Get-WmiObject` n'existe pas dans PowerShell 7. Voir [Microsoft : Win32_Product](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/msiprov/win32-product).

### Chercher, installer, mettre à jour un logiciel

```powershell title="Commande"
winget search <nom>
winget install --id <ID> -e        # -e : correspondance exacte de l'ID
winget upgrade --all               # tout mettre à jour
```

```powershell title="Exemple"
winget install --id Microsoft.Sysinternals.Suite -e
```

### Voir les mises à jour Windows installées

```powershell title="Commande"
Get-HotFix | Sort-Object InstalledOn -Descending
```

```powershell title="Exemple"
Get-HotFix -Id KB5043145 -ErrorAction SilentlyContinue   # un correctif précis est-il installé ?
```

```bat title="Exemple 2"
usoclient StartScan   :: lancer une recherche de mises à jour (Windows 10/11)
```

### Voir l'état de Microsoft Defender

```powershell title="Commande"
Get-MpComputerStatus | Select-Object AMServiceEnabled, RealTimeProtectionEnabled, AntivirusSignatureLastUpdated, QuickScanEndTime
```

```powershell title="Exemple"
Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled, AntivirusSignatureLastUpdated, IsTamperProtected
```

Pour une vue complète : `Get-MpComputerStatus`. Examiner aussi `AntivirusEnabled`, `BehaviorMonitorEnabled`, `OnAccessProtectionEnabled`, `IoavProtectionEnabled`, `NISEnabled`, `AntivirusSignatureVersion` et `AntivirusSignatureAge`. Un service actif ne signifie pas que tous ses composants protègent la machine ; interpréter les valeurs selon le mode et la configuration de Defender.

??? example "Sortie"
    ```text
    RealTimeProtectionEnabled AntivirusSignatureLastUpdated IsTamperProtected
    ------------------------- ----------------------------- -----------------
                         True 02/10/2026 06:12:44                        True
    ```

### Mettre à jour les signatures et lancer une analyse

```powershell title="Commande"
Update-MpSignature
Start-MpScan -ScanType QuickScan          # FullScan, CustomScan -ScanPath <dossier>
Get-MpThreatDetection                     # détections récentes
```

```powershell title="Exemple"
Start-MpScan -ScanType CustomScan -ScanPath C:\Users\alice\Downloads
```

### Voir les exclusions de Defender

```powershell title="Commande"
Get-MpPreference | Select-Object ExclusionPath, ExclusionProcess, ExclusionExtension
```

Une exclusion inattendue (dossier temporaire, `ProgramData`, extension `.ps1`) est un signal à vérifier : c'est un moyen classique de neutraliser l'antivirus.

## Vue d'ensemble

| Besoin | Commande | À regarder |
|---|---|---|
| Logiciels installés | `winget list` | Nom, ID, version |
| Chercher, installer, mettre à jour | `winget search` · `winget install --id <ID> -e` · `winget upgrade --all` | `-e` : ID exact |
| Mises à jour Windows | `Get-HotFix` | `HotFixID`, `InstalledOn` |
| État de Defender | `Get-MpComputerStatus` | `AMServiceEnabled`, `RealTimeProtectionEnabled`, date des signatures |
| Mettre à jour, analyser | `Update-MpSignature` · `Start-MpScan -ScanType QuickScan` | `FullScan`, `CustomScan` |
| Détections récentes | `Get-MpThreatDetection` | Menace, chemin, date |
| Exclusions de Defender | `Get-MpPreference` | `ExclusionPath`, `ExclusionProcess`, `ExclusionExtension` |
