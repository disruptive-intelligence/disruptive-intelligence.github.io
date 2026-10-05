---
title: "Persistance"
cours:
  - library/cyber/forensic/investigation-numerique-forensic/index.md
  - library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/index.md
  - library/it/windows/windows-en-profondeur/index.md
---

# Persistance

Ce qui se relance tout seul au démarrage ou à l'ouverture de session — et les traces laissées par les mécanismes déjà supprimés.

Les incontournables : `autorunsc` · `Get-ScheduledTask` · `7045` · `4698` · `TaskScheduler/Operational` · `4720` · `4732`
{ .kw-cs-top }

## Démarrage automatique

### Lister ce qui se relance tout seul

- **Où :** clés `Run` et `RunOnce` (machine et utilisateur), services (`SYSTEM\CurrentControlSet\Services`,
  événement 7045 à l'installation), tâches planifiées (`C:\Windows\System32\Tasks`), abonnements WMI, comptes créés
  ou ajoutés à un groupe d'administration (4720, 4732).
- **Limites :** chaque mécanisme se lit séparément ; Autoruns (Sysinternals) les rassemble.

```powershell title="Commande"
Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Run, HKCU:\Software\Microsoft\Windows\CurrentVersion\Run   # programmes lancés à l'ouverture de session
Get-ScheduledTask | Where-Object State -ne Disabled | Select-Object TaskPath, TaskName                                    # tâches planifiées actives
Get-CimInstance -Namespace root\subscription -ClassName __EventFilter                                                     # abonnements WMI (persistance discrète)
```

```powershell title="Exemple"
autorunsc64.exe -accepteula -a * -c -h -s -m > autoruns.csv   # tout, en CSV, avec empreintes et signatures, sans les entrées Microsoft
```

## Traces dans les journaux

![[cheatsheets/windows/fondamentaux/logs/persistance#Retrouver les services installés ou modifiés]]

![[cheatsheets/windows/fondamentaux/logs/persistance#Retracer la vie d'une tâche planifiée]]

![[cheatsheets/windows/fondamentaux/logs/persistance#Retracer la création d'un compte et ses privilèges]]

## Vue d'ensemble

| Mécanisme | Où | Trace dans les journaux |
|---|---|---|
| Clés Run / RunOnce | `HKLM` et `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` (et `RunOnce`) | — |
| Services | `HKLM\SYSTEM\CurrentControlSet\Services` | 7045 (Journaux Windows → System) ; 4697 (Security, si audit) |
| Tâches planifiées | `C:\Windows\System32\Tasks` | 4698 (Security, si audit) ; 106, 200, 201 (TaskScheduler → Operational) |
| Abonnements WMI | Espace de noms `root\subscription` | — |
| Comptes ajoutés | Comptes locaux ou du domaine | 4720, 4732 (Journaux Windows → Security) |

Autoruns (`autorunsc.exe -a *`) rassemble tous ces mécanismes en une passe.
