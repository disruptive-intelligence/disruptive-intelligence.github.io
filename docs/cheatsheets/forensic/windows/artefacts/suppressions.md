---
title: "Suppressions"
cours:
  - library/cyber/forensic/investigation-numerique-forensic/index.md
  - library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/index.md
  - library/it/windows/windows-en-profondeur/index.md
---

# Suppressions

Ce qui a été supprimé, d'où et quand ; et comment retrouver une version antérieure.

Les incontournables : `RBCmd` · `vssadmin list shadows`
{ .kw-cs-top }

## Corbeille

### Retrouver ce qui est passé par la corbeille

- **Où :** `C:\$Recycle.Bin\<SID>\`. Chaque fichier supprimé y laisse deux fichiers : `$I…` (chemin d'origine,
  taille, date de suppression) et `$R…` (le contenu).
- **Limites :** rien si l'utilisateur a supprimé avec Maj+Suppr ou vidé la corbeille ; il reste alors les
  clichés instantanés et la récupération sur disque.

```powershell title="Commande"
RBCmd.exe -d "C:\$Recycle.Bin" --csv <dossier_sortie>   # chemin d'origine et date de suppression de chaque fichier
```

```powershell title="Exemple"
RBCmd.exe -d "E:\collecte\C\$Recycle.Bin" --csv E:\analyse\corbeille
```

??? example "Sortie"
    ```text
    Source file: E:\collecte\C\$Recycle.Bin\S-1-5-21-…-1104\$IAK3F2.xlsx
    Version: 2   File size: 48 213   Deleted on: 2026-09-29 03:41:55
    File name: C:\Users\alice\Documents\Paie\salaires_2026.xlsx
    ```

## Clichés instantanés

### Remonter dans le temps avec les clichés instantanés (VSS)

- **Où :** dans `\System Volume Information` à la racine du volume, visibles avec `vssadmin`.
- **Ce qu'il dit :** l'état des fichiers à la date du cliché : une version antérieure d'un fichier modifié,
  ou un fichier supprimé depuis.
- **Limites :** un rançongiciel commence souvent par les supprimer (`vssadmin delete shadows`) : leur absence
  est un indice en soi.

```powershell title="Commande"
vssadmin list shadows                                                                  # clichés disponibles
cmd /c mklink /d C:\vss1 \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\              # monter le cliché n° 1 comme dossier
```

```powershell title="Exemple"
Get-ChildItem C:\vss1\Users\alice\Documents -Recurse | Where-Object Name -like "*salaires*"
```

## Vue d'ensemble

| Source | Où | Outil | Ce qu'on retrouve | Limites |
|---|---|---|---|---|
| Corbeille | `C:\$Recycle.Bin\<SID>\` (`$I…` métadonnées, `$R…` contenu) | RBCmd | Chemin d'origine, taille, date de suppression, contenu | Rien après Maj+Suppr ou corbeille vidée |
| Clichés instantanés (VSS) | `\System Volume Information` | `vssadmin list shadows`, `mklink /d` | Version antérieure ou fichier supprimé depuis | Souvent supprimés par les rançongiciels : leur absence est un indice |
