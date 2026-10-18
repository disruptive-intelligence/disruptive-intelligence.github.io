---
title: "ETW et logman"
---

# ETW et logman

Event Tracing for Windows (ETW) : voir les sessions de trace actives, inspecter leurs providers, trouver un provider et ses mots-clés, enregistrer une trace et la relire ; avec `logman`, PowerShell et l'Analyseur de performances.

Les incontournables : `logman query -ets` · `logman query "<session>" -ets` · `logman query providers` · `logman create trace` · `Get-WinEvent -Path *.etl -Oldest` · `perfmon`
{ .kw-cs-top }

## Sessions de trace

### Lister les sessions ETW actives

```powershell title="Commande"
logman query -ets          # sessions de suivi d'événements en cours (-ets : directement les sessions, pas les collecteurs enregistrés)
```

```powershell title="Exemple"
logman query -ets | findstr /i "eventlog sysmon"
```

??? example "Sortie"
    ```text
    EventLog-Application                          Trace                         Running
    Eventlog-Security                             Trace                         Running
    EventLog-System                               Trace                         Running
    EventLog-Microsoft-Windows-Sysmon-Operational Trace                         Running
    SYSMON TRACE                                  Trace                         Running
    SysmonDnsEtwSession                           Trace                         Running
    ```

Chaque journal de l'Observateur est alimenté par une session `EventLog-…`. Les autres sessions disent quels outils collectent sur la machine (Sysmon, antivirus, EDR, télémétrie) : une session attendue **absente** mérite une question.

Pour comprendre : [Interagir avec ETW : logman](../../../../library/it/windows/sysmon-et-etw/02-comprendre-etw/02-explorer-etw-logman-et-interfaces.md#3-interagir-avec-etw-logman)
{ .kw-cs-meta }

### Inspecter une session

```powershell title="Commande"
logman query "EventLog-System" -ets      # paramètres de la session et providers qu'elle écoute
```

??? example "Sortie"
    ```text
    Name:                 EventLog-System
    Status:               Running
    Buffer Size:          64
    Buffers Lost:         0
    Buffers Written:      1503
    Clock Type:           System
    File Mode:            Real-time

    Provider:
    Name:                 Microsoft-Windows-Kernel-General
    Provider Guid:        {A68CA8B7-004F-D7B6-A698-07E2DE0F1F5D}
    Level:                255
    KeywordsAny:          0x8000000000000000 (System)
    ```

| Champ | À lire |
|---|---|
| `Status` | `Running` : la session collecte |
| `Buffers Lost` | Différent de 0 : des événements ont été **perdus** (session saturée) |
| `File Mode` | `Real-time` : consommée en direct ; sinon écrite dans un fichier (`Root Path`) |
| `Provider` → `Name` / `Guid` | Chaque source d'événements écoutée par la session |
| `Level` | Niveau de détail collecté (`4` = informations, `5` = verbeux, `255` = tout) |
| `KeywordsAny` / `KeywordsAll` | Filtre par catégories d'événements : au moins un / tous les mots-clés |

## Providers

### Trouver un provider

```powershell title="Commande"
logman query providers | findstr /i "winlogon"                 # par mot dans le nom
Get-WinEvent -ListProvider '*Winlogon*' | Select-Object Name   # même recherche en PowerShell
```

??? example "Sortie"
    ```text
    Microsoft-Windows-Winlogon               {DBE9B383-7CF3-4331-91CC-A3CB16A3B538}
    Windows Winlogon Trace                   {D451642C-63A6-11D7-9720-00B0D03E0347}
    ```

Windows compte plus d'un millier de providers : toujours filtrer. Un même composant peut avoir plusieurs providers (manifeste moderne et trace historique).

### Lire les métadonnées d'un provider

```powershell title="Commande"
logman query providers "Microsoft-Windows-Winlogon"      # GUID, mots-clés, niveaux, journaux et processus qui l'utilisent
logman query providers -pid 1234                         # providers enregistrés par un processus donné
```

```powershell title="Exemple"
(Get-WinEvent -ListProvider 'Microsoft-Windows-Winlogon').Events | Select-Object -First 5 Id, Description
```

??? example "Sortie"
    ```text
    Value               Keyword              Description
    -----------------------------------------------------------------
    0x0000000000010000  NotificationEvents
    0x0000000000020000  PerfDiagnostics
    0x0000400000000000  ms:Telemetry

    Value  Level             Description
    -----------------------------------------------------------------
    0x02   win:Error         Error
    0x03   win:Warning       Warning
    0x04   win:Informational Information
    ```

Les **mots-clés** et **niveaux** servent à filtrer une trace (entrée suivante). Les journaux liés (par ex. `Microsoft-Windows-Winlogon/Operational`) disent où ses événements sont déjà visibles dans l'Observateur.

## Enregistrer et relire une trace

### Créer une trace, l'arrêter, la relire

```powershell title="Commande"
logman create trace MaTrace -p "Microsoft-Windows-Kernel-Process" 0x10 0x4 -o C:\Cas\trace.etl -ets   # provider, mots-clés, niveau ; -ets : démarre tout de suite
logman stop MaTrace -ets                                                                              # arrête et ferme le fichier .etl
```

```powershell title="Exemple"
Get-WinEvent -Path C:\Cas\trace.etl -Oldest | Select-Object -First 5 TimeCreated, Id, ProviderName
tracerpt C:\Cas\trace.etl -o C:\Cas\trace.csv -of CSV     # export pour un tableur
```

??? example "Sortie"
    ```text
    TimeCreated          Id ProviderName
    -----------          -- ------------
    18/10/2026 10:02:11   1 Microsoft-Windows-Kernel-Process
    18/10/2026 10:02:11   2 Microsoft-Windows-Kernel-Process
    ```

Console administrateur. `-Oldest` est obligatoire pour lire un `.etl`. Une trace verbeuse grossit vite : la limiter à un provider, des mots-clés et une courte durée. Écrire le fichier sur un support d'analyse, pas sur un disque à préserver.

## Dans l'interface

### Voir les sessions dans l'Analyseur de performances

`perfmon` → **Ensembles de collecteurs de données** → **Sessions de suivi d'événements** : les sessions actives ; double-clic pour leurs providers et paramètres. **Défini par l'utilisateur** → *Nouveau* → *Ensemble de collecteurs de données* : créer sa propre session sans ligne de commande. Pour parcourir les providers, leurs GUID et leurs événements : EtwExplorer.

Pour comprendre : [GUI pour l'analyse ETW](../../../../library/it/windows/sysmon-et-etw/02-comprendre-etw/02-explorer-etw-logman-et-interfaces.md#5-interfaces-graphiques-pour-lanalyse-etw)
{ .kw-cs-meta }

## Vue d'ensemble

| Besoin | Commande |
|---|---|
| Sessions actives | `logman query -ets` |
| Détail d'une session | `logman query "<session>" -ets` |
| Chercher un provider | `logman query providers | findstr /i "<mot>"` · `Get-WinEvent -ListProvider '*<mot>*'` |
| Mots-clés et niveaux d'un provider | `logman query providers "<provider>"` |
| Providers d'un processus | `logman query providers -pid <PID>` |
| Enregistrer une trace | `logman create trace <nom> -p "<provider>" <mots-clés> <niveau> -o <fichier>.etl -ets` |
| Arrêter la trace | `logman stop <nom> -ets` |
| Relire un .etl | `Get-WinEvent -Path <fichier>.etl -Oldest` · `tracerpt <fichier>.etl -of CSV` |
| Interface | `perfmon` → Sessions de suivi d'événements |

| Provider | Ce qu'il apporte en chasse |
|---|---|
| Microsoft-Windows-Kernel-Process | Processus et threads : création, fin, parent réel |
| Microsoft-Windows-Kernel-File | Opérations sur les fichiers (fichiers système, chiffrement de masse) |
| Microsoft-Windows-Kernel-Registry | Modifications du registre (persistance) |
| Microsoft-Windows-Kernel-Network | Activité réseau des processus |
| Microsoft-Windows-DotNETRuntime | Chargement d'assemblies .NET, méthodes appelées |
| Microsoft-Windows-PowerShell | Exécution PowerShell, Script Block Logging |
| Microsoft-Windows-DNS-Client | Requêtes DNS (C2, tunneling) |
| Microsoft-Windows-SMBClient / SMBServer | Accès SMB (mouvements latéraux) |
| Microsoft-Windows-TerminalServices-LocalSessionManager | Sessions Bureau à distance |
| Microsoft-Windows-CodeIntegrity · Security-Mitigations | Contrôles d'intégrité du code, mesures d'atténuation |
| Microsoft-Windows-Threat-Intelligence | Restreint : réservé aux processus protégés (antivirus, EDR) |

ETW ou Sysmon ? Sysmon livre des événements prêts à lire dans un journal ; ETW donne accès à bien plus de sources, plus brutes, à collecter soi-même. Voir [ETW vs Sysmon](../../../../library/it/windows/sysmon-et-etw/02-comprendre-etw/04-etw-en-investigation.md#9-synthese-etw-ou-sysmon) et la cheat sheet [Sysmon et requêtes SIEM](sysmon.md).
