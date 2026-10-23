---
title: Détecter avec ETW
source: IT/02 Windows/Journaux & investigation/Sysmon et ETW.md
note: Sysmon et ETW
up:
- - Sysmon et ETW
  - index.md
---

Event Tracing for Windows (ETW) permet d'obtenir une télémétrie plus détaillée que certains événements Sysmon afin d'investiguer des techniques d'attaque avancées.

Cette section présente deux scénarios de Threat Hunting :

- Détecter les relations parent-enfant étranges : détecter des relations anormales entre processus et le Parent PID Spoofing.
    
- Malicious .NET Assembly Loading : identifier le chargement et l'exécution d'assemblages .NET suspects.
    

L'objectif est de compléter les observations de Sysmon avec des informations provenant de fournisseurs ETW spécialisés.


## Chapitre 11 — Trois détections avec ETW

Chaque détection a sa fiche dans la sous-rubrique « Repérer une attaque » :

- [Repérer une relation parent-enfant anormale](../../../../cheatsheets/windows/reperer-une-attaque/reperer-une-relation-parent-enfant-anormale.md) : un parent qui n'a pas vocation à lancer cet enfant (Process Hacker, Sysmon `1`).
- [Démasquer un faux processus parent (PPID spoofing)](../../../../cheatsheets/windows/reperer-une-attaque/demasquer-un-faux-processus-parent-ppid-spoofing.md) : le parent affiché par Sysmon `1` contredit par le provider `Microsoft-Windows-Kernel-Process`.
- [Repérer le chargement d'assemblies .NET](../../../../cheatsheets/windows/reperer-une-attaque/reperer-le-chargement-d-assemblies-net.md) : Sysmon `7` voit le runtime .NET se charger, le provider `Microsoft-Windows-DotNETRuntime` montre les assemblies et les méthodes.

### Sysmon ou ETW — comparaison des détections

| Scénario                | Sysmon                                                          | ETW                                                                          |
| ----------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| PPID Spoofing           | Event ID 1 : relation parent/enfant apparente                   | `Kernel-Process` : informations supplémentaires sur la création du processus |
| .NET Assembly Execution | Event ID 7 : chargement de DLL comme `clr.dll`                  | `DotNETRuntime` : détails sur les assemblages, chargements et méthodes       |
| Type de visibilité      | Événements prédéfinis                                           | Télémétrie spécialisée selon le provider                                     |
| Limite principale       | Certaines informations peuvent être insuffisantes ou trompeuses | Nécessite une collecte et des filtres adaptés                                |

### Démarche de threat hunting avec ETW

```
Suspicious Activity
        ↓
Identify Sysmon Evidence
        ↓
Determine Telemetry Limitations
        ↓
Select Relevant ETW Provider
        ↓
Collect Events with SilkETW
        ↓
Analyze JSON Output
        ↓
Correlate Sysmon & ETW
        ↓
Validate Hunting Hypothesis
```


Les deux scénarios montrent que Sysmon et ETW sont complémentaires.

Sysmon constitue une excellente source pour rechercher rapidement des événements comme les créations de processus ou les chargements de DLL. ETW permet ensuite d'approfondir l'investigation avec des informations plus spécialisées.

La leçon centrale est de ne pas limiter une investigation aux événements Sysmon lorsqu'ils ne suffisent pas à expliquer le comportement observé : une collecte ETW ciblée peut révéler des détails déterminants sur l'origine réelle d'un processus ou l'exécution d'un assemblage .NET.

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
