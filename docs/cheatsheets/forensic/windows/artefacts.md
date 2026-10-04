---
title: "Artefacts Windows"
cours:
  - library/cyber/forensic/investigation-numerique-forensic/index.md
  - library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs.md
besoin: "Retrouver ce qui s'est passé sur un poste Windows (artefacts)"
---
# Artefacts Windows

Windows garde la trace de ce qu'on y exécute, ouvre, branche et supprime, souvent sans que l'utilisateur le
sache. Pour chaque artefact : où il se trouve, ce qu'il dit, ce qu'il ne prouve pas, et la commande pour le
lire. Les outils cités sont ceux d'Eric Zimmerman (EZ Tools, gratuits) : chacun produit un CSV à ouvrir
dans Timeline Explorer.

Les incontournables : `KAPE` · `PECmd` · `AmcacheParser` · `LECmd` · `SBECmd` · `EvtxECmd` · `Get-WinEvent`
{ .kw-cs-top }

## Quelle question, quel artefact

| Je veux savoir… | Artefacts à lire | Ce qu'ils ne prouvent pas seuls |
|---|---|---|
| Ce qui a été **exécuté** | Prefetch, BAM, Amcache, ShimCache, SRUM, événement 4688 | Amcache et ShimCache montrent qu'un exécutable était présent, pas toujours qu'il a tourné |
| Ce qui a été **ouvert** | LNK, Jump Lists, RecentDocs, Shellbags | Le contenu du fichier : seulement son nom, son chemin et des dates |
| Quels **périphériques USB** | USBSTOR, `setupapi.dev.log`, MountedDevices, MountPoints2 | Ce qui a été copié : il faut croiser avec LNK et Shellbags |
| Qui s'est **connecté**, et comment | Journal Security (4624, 4625, 4672), RDP (1149, 21, 25) | L'identité réelle derrière un compte partagé ou volé |
| Ce qui a été **supprimé** | Corbeille (`$I`, `$R`), clichés instantanés (VSS) | Un effacement sécurisé, ou une suppression sans passer par la corbeille |
| Ce qui **se relance** au démarrage | Clés Run, services (7045), tâches planifiées, abonnements WMI | Une persistance purement en mémoire |
| Qui a **parlé au réseau** | SRUM (octets par application), profils réseau, journaux du pare-feu | Le contenu des échanges |

## Collecter avant d'analyser

### Récupérer les artefacts d'un coup

Les ruches du registre et les journaux sont verrouillés quand Windows tourne : un simple copier-coller
échoue. KAPE (ou FTK Imager) les copie en lecture brute, avec leurs dates.

```powershell title="Commande"
kape.exe --tsource C: --tdest <dossier_collecte> --target KapeTriage   # copie les artefacts courants en lecture brute
```

```powershell title="Exemple"
kape.exe --tsource C: --tdest E:\collecte\PC-COMPTA-07 --target KapeTriage --vhdx PC-COMPTA-07
```

??? example "Sortie"
    ```text
    KAPE version 1.3.0.2 Author: Eric Zimmerman
    Found 312 targets. Found 31 Compound Targets.
    Target 'KapeTriage' with Id '…' found. Executing…
    Copied 1 742 files (1.38 GB) in 94.2 seconds. Total execution time: 101.6 seconds
    ```

```text title="Où sont les ruches du registre"
C:\Windows\System32\config\SYSTEM, SOFTWARE, SAM, SECURITY          # ruches machine
C:\Users\<utilisateur>\NTUSER.DAT                                   # ruche de l'utilisateur
C:\Users\<utilisateur>\AppData\Local\Microsoft\Windows\UsrClass.dat # Shellbags de l'utilisateur
```

!!! warning "Attention"
    Collecter sur un support externe, et noter l'heure UTC de début. Chaque outil lancé sur la machine laisse
    lui-même des traces (Prefetch, événements) : les consigner dans le journal d'intervention.

## Exécution

### Savoir quels programmes ont été lancés (Prefetch)

- **Où :** `C:\Windows\Prefetch\*.pf`, un fichier par exécutable.
- **Ce qu'il dit :** nom et chemin du programme, nombre d'exécutions, jusqu'à 8 dernières dates de lancement
  (Windows 8 et plus), fichiers chargés dans les dix premières secondes.
- **Limites :** désactivé par défaut sur Windows Server ; 1 024 fichiers au plus, les plus anciens disparaissent.

```powershell title="Commande"
PECmd.exe -d <dossier_prefetch> --csv <dossier_sortie>   # tous les .pf en CSV, avec la chronologie des lancements
```

```powershell title="Exemple"
PECmd.exe -d E:\collecte\C\Windows\Prefetch --csv E:\analyse\prefetch
```

??? example "Sortie"
    ```text
    Executable Name: MIMIKATZ.EXE
    Run count: 2
    Last run: 2026-09-29 03:14:07
    Other run times: 2026-09-29 03:12:51
    Directories referenced: \VOLUME{…}\USERS\PUBLIC\DOWNLOADS
    ```

### Savoir qui a lancé quoi, et quand en dernier (BAM)

- **Où :** `SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\<SID>` (Windows 10 1709 et plus).
- **Ce qu'il dit :** pour chaque utilisateur (SID), les programmes lancés et la date du dernier lancement.
- **Limites :** une date par programme seulement ; les entrées de plus d'une semaine peuvent être purgées.

```powershell title="Commande"
reg query "HKLM\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings" /s   # sur la machine vivante
```

```powershell title="Exemple"
RECmd.exe -f E:\collecte\C\Windows\System32\config\SYSTEM --bn BatchExamples\Kroll_Batch.reb --csv E:\analyse\registre
```

### Retrouver les exécutables présents sur le disque (Amcache)

- **Où :** `C:\Windows\AppCompat\Programs\Amcache.hve`.
- **Ce qu'il dit :** chemin, éditeur, taille et **empreinte SHA-1** des exécutables vus par le système,
  programmes installés, pilotes.
- **Limites :** présence ne veut pas dire exécution ; l'empreinte permet en revanche de chercher le fichier
  sur VirusTotal même s'il a été effacé.

```powershell title="Commande"
AmcacheParser.exe -f <Amcache.hve> --csv <dossier_sortie> -i   # -i : inclut les entrées associées aux programmes installés
```

```powershell title="Exemple"
AmcacheParser.exe -f E:\collecte\C\Windows\AppCompat\Programs\Amcache.hve --csv E:\analyse\amcache -i
```

### Voir les exécutables connus du système (ShimCache)

- **Où :** `SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache`.
- **Ce qu'il dit :** chemins et dates de modification des exécutables que Windows a examinés, du plus récent
  au plus ancien.
- **Limites :** écrit à l'arrêt de la machine (une machine vivante montre l'état du dernier arrêt) ; sur
  Windows 10 et plus, ne prouve pas l'exécution.

```powershell title="Commande"
AppCompatCacheParser.exe -f <ruche_SYSTEM> --csv <dossier_sortie>
```

```powershell title="Exemple"
AppCompatCacheParser.exe -f E:\collecte\C\Windows\System32\config\SYSTEM --csv E:\analyse\shimcache
```

### Mesurer l'activité réseau par application (SRUM)

- **Où :** `C:\Windows\System32\sru\SRUDB.dat` (base ESE), avec la ruche `SOFTWARE`.
- **Ce qu'il dit :** octets envoyés et reçus par application et par utilisateur, heure par heure, sur
  30 à 60 jours. Idéal pour repérer une exfiltration.
- **Limites :** écrit par paquets, environ toutes les heures ; les dernières minutes manquent souvent.

```powershell title="Commande"
SrumECmd.exe -f <SRUDB.dat> -r <ruche_SOFTWARE> --csv <dossier_sortie>
```

```powershell title="Exemple"
SrumECmd.exe -f E:\collecte\C\Windows\System32\sru\SRUDB.dat -r E:\collecte\C\Windows\System32\config\SOFTWARE --csv E:\analyse\srum
```

## Fichiers et dossiers ouverts

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

## Périphériques USB

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

## Suppressions

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

## Connexions et journaux

### Retrouver les connexions, réussies ou non

- **Où :** `C:\Windows\System32\winevt\Logs\` ; journal `Security` (4624 réussite, 4625 échec, 4672 droits
  d'administrateur, 4688 processus créé, 4720 compte créé, 1102 journal effacé) ; RDP dans
  `TerminalServices-RemoteConnectionManager` (1149) et `TerminalServices-LocalSessionManager` (21, 24, 25).
- **Ce qu'il dit :** qui, quand, depuis quelle adresse, avec quel type de connexion (2 locale, 3 réseau,
  10 RDP).
- **Pour aller plus loin :** la note [Analyse des journaux d'événements Windows](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs.md).

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624,4625} -MaxEvents 50 | Format-Table TimeCreated, Id, Message -Wrap
```

```powershell title="Exemple"
EvtxECmd.exe -d E:\collecte\C\Windows\System32\winevt\Logs --csv E:\analyse\evtx   # tous les journaux, en un CSV normalisé
```

## Persistance

### Lister ce qui se relance tout seul

- **Où :** clés `Run` et `RunOnce` (machine et utilisateur), services (`SYSTEM\CurrentControlSet\Services`,
  événement 7045 à l'installation), tâches planifiées (`C:\Windows\System32\Tasks`), abonnements WMI.
- **Limites :** chaque mécanisme se lit séparément ; Autoruns (Sysinternals) les rassemble.

```powershell title="Commande"
Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Run, HKCU:\Software\Microsoft\Windows\CurrentVersion\Run   # programmes lancés à l'ouverture de session
Get-ScheduledTask | Where-Object State -ne Disabled | Select-Object TaskPath, TaskName                                    # tâches planifiées actives
Get-CimInstance -Namespace root\subscription -ClassName __EventFilter                                                     # abonnements WMI (persistance discrète)
```

```powershell title="Exemple"
autorunsc64.exe -accepteula -a * -c -h -s -m > autoruns.csv   # tout, en CSV, avec empreintes et signatures, sans les entrées Microsoft
```
