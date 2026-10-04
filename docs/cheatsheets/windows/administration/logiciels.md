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
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*', 'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*' |
    Where-Object DisplayName | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Sort-Object DisplayName
```

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
