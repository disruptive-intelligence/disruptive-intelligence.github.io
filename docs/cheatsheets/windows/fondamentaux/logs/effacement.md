---
title: "Effacement des traces"
---

# Effacement des traces

Journaux effacés et journalisation arrêtée.

Les incontournables : `1102` · `104` · `1100` · `wevtutil cl`
{ .kw-cs-top }

## Effacement des traces

### Repérer un effacement de journal

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=1102}   # journal de sécurité effacé
Get-WinEvent -FilterHashtable @{LogName='System'; Id=104}      # autre journal effacé
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=1100}   # service de journalisation arrêté
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=1102} -ErrorAction SilentlyContinue | Select-Object TimeCreated, Message
```

??? example "Sortie"
    ```text
    TimeCreated          Message
    -----------          -------
    01/10/2026 23:20:11  Le journal d'audit a été effacé. Sujet : … Nom du compte : adm.martin …
    ```

Un **1102** donne le compte qui a effacé le journal Security ; un **104** dit quel autre journal a été effacé. Un **1100** apparaît aussi lors d'un arrêt ou redémarrage normal : le croiser avec 1074, 6005, 6006, 6008. Avec l'audit des processus, un 4688 `wevtutil.exe cl Security` juste avant confirme l'effacement. Les événements déjà envoyés au SIEM restent consultables.

Pour comprendre : [Manipulation des journaux : 1102, 104, 1100](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/09-manipulation-des-journaux.md) · [Effacer un filtre ou effacer un journal](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#effacer-un-filtre-vs-effacer-un-journal)
{ .kw-cs-meta }

## Vue d'ensemble

| Event ID | Journal | Signification | À retenir |
|---|---|---|---|
| **1102** | Security | Journal Security effacé | Donne le compte qui a effacé |
| **104** | System (Microsoft-Windows-Eventlog) | Autre journal effacé | Dit quel journal (System, PowerShell/Operational…) |
| **1100** | Security | Service de journalisation arrêté | Aussi lors d'un arrêt normal : croiser avec 1074, 6005, 6006, 6008 |
| **4688** | Security | Processus créé | `wevtutil.exe cl Security` juste avant un 1102 confirme l'effacement |

Pattern : 104 (PowerShell/Operational) → 104 (System) → 1102 → 1100, en quelques minutes : Defense Evasion. Les événements déjà envoyés au SIEM restent consultables.
