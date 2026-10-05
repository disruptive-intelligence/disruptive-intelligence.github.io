---
title: "Fichiers et dossiers ouverts"
cours:
  - library/cyber/forensic/investigation-numerique-forensic/index.md
  - library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/index.md
  - library/it/windows/windows-en-profondeur/index.md
---

# Fichiers et dossiers ouverts

Ce que l'utilisateur a ouvert, parcouru ou tapé : les noms, chemins et dates restent même quand le fichier a disparu.

Les incontournables : `LECmd` · `JLECmd` · `SBECmd` · `reg query …\RunMRU`
{ .kw-cs-top }

## Fichiers ouverts

### Retrouver les fichiers ouverts récemment (LNK)

- **Où :** `C:\Users\<utilisateur>\AppData\Roaming\Microsoft\Windows\Recent\*.lnk`.
- **Ce qu'il dit :** chemin du fichier ouvert (même sur clé USB ou partage réseau), dates de la cible, numéro
  de série du volume, parfois le nom de la machine d'origine.
- **Limites :** un raccourci par nom de fichier ; il survit à la suppression du fichier ouvert.

```powershell title="Commande"
LECmd.exe -d <dossier_Recent> --csv <dossier_sortie>
```

```powershell title="Exemple"
LECmd.exe -d "E:\collecte\C\Users\alice\AppData\Roaming\Microsoft\Windows\Recent" --csv E:\analyse\lnk
```

### Voir les fichiers récents de chaque application (Jump Lists)

- **Où :** `…\Recent\AutomaticDestinations\` et `…\Recent\CustomDestinations\`.
- **Ce qu'il dit :** pour chaque application (Word, Explorateur, RDP…), les fichiers ou hôtes ouverts et leurs
  dates. La Jump List de `mstsc` liste les serveurs contactés en RDP.
- **Limites :** l'application est identifiée par un AppID qu'il faut traduire (JLECmd le fait).

```powershell title="Commande"
JLECmd.exe -d <dossier_Recent> --csv <dossier_sortie>
```

```powershell title="Exemple"
JLECmd.exe -d "E:\collecte\C\Users\alice\AppData\Roaming\Microsoft\Windows\Recent" --csv E:\analyse\jumplists
```

## Dossiers parcourus et saisies

### Savoir quels dossiers ont été parcourus (Shellbags)

- **Où :** `NTUSER.DAT` et surtout `UsrClass.dat` (clés `BagMRU` et `Bags`).
- **Ce qu'il dit :** les dossiers affichés dans l'Explorateur, y compris sur une clé USB, un partage réseau ou
  un dossier supprimé depuis.
- **Limites :** prouve qu'un dossier a été affiché, pas qu'un fichier précis a été ouvert.

```powershell title="Commande"
SBECmd.exe -d <dossier_des_ruches_utilisateur> --csv <dossier_sortie>
```

```powershell title="Exemple"
SBECmd.exe -d "E:\collecte\C\Users\alice" --csv E:\analyse\shellbags
```

### Lire les commandes tapées et les chemins saisis (RunMRU, TypedPaths)

- **Où :** dans `NTUSER.DAT`, sous `Software\Microsoft\Windows\CurrentVersion\Explorer\` : `RunMRU` (fenêtre
  Exécuter), `TypedPaths` (barre d'adresse de l'Explorateur), `RecentDocs` (documents récents).
- **Ce qu'il dit :** ce que l'utilisateur a tapé lui-même, dans l'ordre.

```powershell title="Commande"
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU"   # sur la machine vivante, utilisateur courant
```

```powershell title="Exemple"
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths"
```

??? example "Sortie"
    ```text
    HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
        a    REG_SZ    powershell -w hidden -enc SQBFAFgA…\1
        b    REG_SZ    cmd\1
        MRUList    REG_SZ    ab
    ```
