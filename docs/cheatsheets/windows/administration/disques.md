---
title: "Disques, archives et transferts"
cours:
  - library/it/windows/powershell/index.md
---

# Disques, archives et transferts

Espace disque et volumes, état de BitLocker, archives zip, copie de dossiers volumineux, transfert vers une autre machine.

Les incontournables : `Get-Volume` · `Get-PSDrive` · `manage-bde -status` · `Compress-Archive` · `robocopy`
{ .kw-cs-top }

### Voir l'espace disque

```powershell title="Commande"
Get-Volume | Select-Object DriveLetter, FileSystemLabel, FileSystem, @{n='Libre (Go)';e={[math]::Round($_.SizeRemaining/1GB,1)}}, @{n='Taille (Go)';e={[math]::Round($_.Size/1GB,1)}}
```

```powershell title="Exemple"
Get-PSDrive -PSProvider FileSystem
```

??? example "Sortie"
    ```text
    Name  Used (GB)  Free (GB) Provider    Root
    ----  ---------  --------- --------    ----
    C        182,41      54,12 FileSystem  C:\
    D        611,90     318,07 FileSystem  D:\
    ```

### Voir la taille d'un dossier

```powershell title="Commande"
(Get-ChildItem <dossier> -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum / 1GB
```

```powershell title="Exemple"
Get-ChildItem C:\Users -Directory | ForEach-Object {
  [pscustomobject]@{ Dossier = $_.Name; Go = [math]::Round(((Get-ChildItem $_.FullName -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum / 1GB), 1) } } |
  Sort-Object Go -Descending
```

### Voir les disques et partitions

```powershell title="Commande"
Get-Disk
Get-Partition
```

```bat title="Exemple"
diskpart
  list disk
  list volume
```

### Voir l'état de BitLocker

```bat title="Commande"
manage-bde -status   :: console administrateur
```

```powershell title="Exemple"
Get-BitLockerVolume | Select-Object MountPoint, VolumeStatus, ProtectionStatus, EncryptionPercentage
```

??? example "Sortie"
    ```text
    MountPoint VolumeStatus     ProtectionStatus EncryptionPercentage
    ---------- ------------     ---------------- --------------------
    C:         FullyEncrypted                 On                  100
    D:         FullyDecrypted                Off                    0
    ```

### Créer et extraire une archive zip

```powershell title="Commande"
Compress-Archive -Path <source> -DestinationPath <archive.zip>
Expand-Archive -Path <archive.zip> -DestinationPath <dossier>
```

```powershell title="Exemple"
Compress-Archive -Path E:\collecte\PC-COMPTA-07 -DestinationPath E:\collecte\PC-COMPTA-07.zip
```

```bat title="Exemple 2"
tar -a -cf archive.zip dossier   :: tar est livré avec Windows 10 et 11
tar -xf archive.zip
```

### Copier un dossier volumineux de façon fiable

```bat title="Commande"
robocopy <source> <destination> /E /COPY:DAT /R:2 /W:5 /LOG:<journal>   :: /E : sous-dossiers ; reprend après interruption
```

```bat title="Exemple"
robocopy D:\Partages\Compta \\srv-backup\Compta /MIR /COPY:DATSO /R:2 /W:5 /LOG:C:\Logs\robocopy-compta.log
```

!!! warning "Attention"
    `/MIR` rend la destination identique à la source : les fichiers absents de la source **sont supprimés** de la destination.

### Copier un fichier vers une autre machine

```powershell title="Commande"
Copy-Item <fichier> -Destination \\<hôte>\<partage>\
# Avec une session PowerShell distante (WinRM)
$s = New-PSSession -ComputerName <hôte>; Copy-Item <fichier> -Destination <chemin> -ToSession $s
```

```bat title="Exemple"
scp C:\Collecte\triage.zip analyste@192.168.1.200:/srv/collecte/   :: client OpenSSH intégré à Windows
```

## Vue d'ensemble

| Besoin | PowerShell / Windows | Équivalent Linux |
|---|---|---|
| Espace disque | `Get-Volume` | `df -h` |
| Taille d'un dossier | `Get-ChildItem -Recurse -File | Measure-Object Length -Sum` | `du -sh` |
| Disques et partitions | `Get-Disk` · `Get-Partition` | `lsblk` |
| Chiffrement du disque | `manage-bde -status` (BitLocker) | `cryptsetup status` (LUKS) |
| Créer, extraire une archive | `Compress-Archive` · `Expand-Archive` (zip) | `tar -czf` · `tar -xzf` |
| Copier un gros dossier avec reprise | `robocopy /E` | `rsync -a` |
| Copier vers une autre machine | `Copy-Item \\<hôte>\<partage>` ou session PowerShell distante | `scp`, `rsync` |
