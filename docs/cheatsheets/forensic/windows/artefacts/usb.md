---
title: "Périphériques USB"
cours:
  - library/cyber/forensic/investigation-numerique-forensic/index.md
  - library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/index.md
  - library/it/windows/windows-en-profondeur/index.md
---

# Périphériques USB

Quelles clés ou disques ont été branchés, quand, et par qui. Pour savoir ce qui a été copié, croiser avec les [fichiers et dossiers ouverts](fichiers-ouverts.md).

Les incontournables : `USBSTOR` · `setupapi.dev.log` · `MountedDevices` · `MountPoints2`
{ .kw-cs-top }

## Clés et disques USB

### Lister les clés USB branchées et leur numéro de série (USBSTOR)

- **Où :** `SYSTEM\CurrentControlSet\Enum\USBSTOR` ; date de première connexion dans
  `C:\Windows\INF\setupapi.dev.log` ; lettre attribuée dans `SYSTEM\MountedDevices` ; utilisateur dans
  `NTUSER.DAT\…\Explorer\MountPoints2`.
- **Ce qu'il dit :** fabricant, modèle, numéro de série, dates de première et dernière connexion.
- **Limites :** ne dit pas ce qui a été copié : croiser avec LNK, Shellbags et Jump Lists (même lettre de
  lecteur, même numéro de série de volume).

```powershell title="Commande"
Get-ChildItem HKLM:\SYSTEM\CurrentControlSet\Enum\USBSTOR | Select-Object PSChildName   # fabricant et modèle
```

```powershell title="Exemple"
Select-String -Path C:\Windows\INF\setupapi.dev.log -Pattern "USBSTOR" -Context 0,1   # première connexion de chaque clé
```

## Vue d'ensemble

| Question | Artefact | Où |
|---|---|---|
| Quels périphériques (fabricant, modèle, n° de série) | USBSTOR | `SYSTEM\CurrentControlSet\Enum\USBSTOR` |
| Première connexion | setupapi | `C:\Windows\INF\setupapi.dev.log` |
| Quelle lettre de lecteur | MountedDevices | `SYSTEM\MountedDevices` |
| Quel utilisateur | MountPoints2 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` |
| Ce qui a été ouvert sur la clé | LNK, Shellbags, Jump Lists | Même lettre de lecteur, même n° de série de volume |
