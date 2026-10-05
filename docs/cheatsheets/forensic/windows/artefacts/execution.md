---
title: "Exécution"
cours:
  - library/cyber/forensic/investigation-numerique-forensic/index.md
  - library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/index.md
  - library/it/windows/windows-en-profondeur/index.md
---

# Exécution

Ce programme a-t-il été lancé, par qui et quand ? Aucun artefact ne répond seul : Prefetch et BAM attestent un lancement, Amcache et ShimCache une présence, SRUM l'activité réseau.

Les incontournables : `PECmd` · `RECmd` · `AmcacheParser` · `AppCompatCacheParser` · `SrumECmd`
{ .kw-cs-top }

## Programmes lancés

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

## Programmes présents sur le disque

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

## Activité par application

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

Pour comprendre : [Windows en profondeur, ch. 23 (artefacts d'exécution)](../../../../library/it/windows/windows-en-profondeur/index.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Artefact | Où | Outil | Ce qu'il prouve | Limites |
|---|---|---|---|---|
| Prefetch | `C:\Windows\Prefetch\*.pf` | PECmd | Exécution : nombre, jusqu'à 8 dernières dates | Désactivé par défaut sur Windows Server ; 1 024 fichiers au plus |
| BAM | `SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\<SID>` | `reg query`, Registry Explorer | Qui a lancé quoi, dernier lancement | Une date par programme ; purge après une semaine environ |
| Amcache | `C:\Windows\AppCompat\Programs\Amcache.hve` | AmcacheParser | Présence, éditeur, **SHA-1** | Présence ≠ exécution |
| ShimCache | `SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache` | AppCompatCacheParser | Exécutables examinés par Windows | Écrit à l'arrêt ; ne prouve pas l'exécution (Windows 10 et plus) |
| SRUM | `C:\Windows\System32\sru\SRUDB.dat` | SrumECmd | Octets échangés par application et par utilisateur (30 à 60 jours) | Écrit environ toutes les heures |
| Événement 4688 | Journaux Windows → Security | EvtxECmd, `Get-WinEvent` | Processus créé, ligne de commande | Seulement si l'audit est activé |
