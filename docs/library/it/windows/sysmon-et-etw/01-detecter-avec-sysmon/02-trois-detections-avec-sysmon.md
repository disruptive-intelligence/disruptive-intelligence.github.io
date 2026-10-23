---
title: Trois détections avec Sysmon
source: IT/02 Windows/Journaux & investigation/Sysmon et ETW.md
note: Sysmon et ETW
up:
- - Sysmon et ETW
  - ../index.md
- - Détecter avec Sysmon
  - index.md
---

Chaque détection a sa fiche dans la sous-rubrique « Repérer une attaque » : l'attaque, les traces, les requêtes XML et PowerShell, les indicateurs, les faux positifs et le lab.

- [Repérer un DLL hijacking](../../../../../cheatsheets/windows/reperer-une-attaque/reperer-un-dll-hijacking.md) : une DLL chargée depuis un chemin inhabituel par un exécutable légitime (Sysmon `7`).
- [Repérer du PowerShell non managé](../../../../../cheatsheets/windows/reperer-une-attaque/reperer-du-powershell-non-manage.md) : le runtime .NET chargé dans un processus qui ne l'utilise pas (Sysmon `7`).
- [Repérer un accès à LSASS](../../../../../cheatsheets/windows/reperer-une-attaque/reperer-un-acces-a-lsass.md) : un processus suspect qui ouvre `lsass.exe` (Sysmon `10`).

## Comparaison des trois détections

| Technique                           | Event ID principal | Indicateur clé                                                     |
| ----------------------------------- | ------------------ | ------------------------------------------------------------------ |
| DLL Hijacking                       | Sysmon 7           | DLL chargée depuis un chemin inhabituel par un exécutable légitime |
| Unmanaged PowerShell / C# Injection | Sysmon 7           | Chargement inattendu de `clr.dll` / `clrjit.dll`                   |
| Credential Dumping                  | Sysmon 10          | Processus suspect accédant à `lsass.exe`                           |

### Démarche d'investigation

```
Sysmon Telemetry
       ↓
Identify Relevant Event ID
       ↓
Inspect Process & Target
       ↓
Examine Paths / Signatures / Access Rights
       ↓
Correlate Related Events
       ↓
Validate Suspicious Behavior
       ↓
Threat Hunting / DFIR Investigation
```


Pour renforcer les investigations, ces événements peuvent être corrélés avec :

- Sysmon Event ID 1 : création de processus ;
- Windows Security Event ID 4688 : création de processus, selon la politique d'audit ;
- Windows Security Event ID 4624 : sessions de connexion ;
- d'autres événements Sysmon, EDR et réseau.

## Points essentiels

La valeur de Sysmon en Threat Hunting réside dans la capacité à observer des comportements techniques précis qui ne seraient pas toujours visibles dans les journaux Windows traditionnels.

Les trois exemples illustrent des méthodes de détection différentes :

- DLL Hijacking : examiner l'origine et les caractéristiques des DLL chargées.
- Code Injection : identifier les composants .NET chargés dans des processus inhabituels.
- Credential Dumping : surveiller les accès suspects à LSASS.

Dans chaque cas, un événement Sysmon constitue une observation à analyser, et non une preuve automatique d'activité malveillante. La détection devient plus fiable lorsque plusieurs éléments sont corrélés : processus, fichiers, chemins, signatures, utilisateurs et chronologie des événements.

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
