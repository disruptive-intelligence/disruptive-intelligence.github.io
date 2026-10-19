---
title: Repérer le chargement d'assemblies .NET
source: IT/02 Windows/Journaux & investigation/Sysmon et ETW.md
note: Sysmon et ETW
up:
- - Sysmon et ETW
  - ../index.md
- - Détecter avec ETW
  - index.md
---

## 3. Détecter le chargement d'assemblages .NET malveillants

Cette seconde technique consiste à analyser les chargements de composants .NET afin d'identifier des exécutions suspectes, notamment celles réalisées directement en mémoire.

### Living off the Land — LotL

Le Living off the Land (LotL) consiste à utiliser des outils légitimes déjà présents sur le système pour effectuer des activités malveillantes.

Exemples :

- PowerShell ;
- outils natifs Windows ;
- composants d'administration.

Cette approche peut compliquer la détection, puisque les exécutables utilisés appartiennent à l'environnement légitime.

Cependant des contre-mesures face à cette stratégie ont été mises en place, ce qui complique son usage, les attaquants ont développé de nouvelles approches que Mandiant qualifie de BYOL.

### Bring Your Own Land — BYOL

Le cours présente l'approche Bring Your Own Land (BYOL), notamment décrite par Mandiant.

Plutôt que de s'appuyer exclusivement sur les outils natifs, les attaquants peuvent introduire leurs propres outils, par exemple des assemblages .NET développés en C#.

Ces assemblages peuvent être chargés et exécutés directement en mémoire.

### Pourquoi .NET ?

Le cours met en avant plusieurs caractéristiques :

| Caractéristique               | Intérêt                                                                                                                                                                                                                                  |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Common Language Runtime (CLR) | Permet l'exécution de code managé                                                                                                                                                                                                        |
| Memory Management             | Fournit notamment le Garbage Collection                                                                                                                                                                                                  |
| In-Memory Assembly Loading    | Permet de charger des assemblages sans nécessairement écrire leur fichier sur disque                                                                                                                                                     |
| .NET Libraries                | Fournissent des fonctionnalités HTTP, cryptographiques et IPC. Ces outils pré-construits rationalisent le processus de développement, réduisent la probabilité d'erreurs et facilitent la création d'applications robustes et efficaces. |
| Windows Integration           | Les composants .NET sont présents dans de nombreux environnements Windows. Chaque système Windows est équipé par défaut d'une certaine version de .NET pré-installée.                                                                    |

L'exécution en mémoire peut réduire certains artefacts sur disque et compliquer les détections reposant exclusivement sur l'analyse des fichiers.

Elle ne rend cependant pas le code invisible aux outils de sécurité.

### Exemple — Cobalt Strike execute-assembly

Le cours cite la commande ["execute-assembly"](https://www.cobaltstrike.com/blog/cobalt-strike-3-11-the-snake-that-eats-its-tail/) de Cobalt Strike.

Elle permet d'exécuter des assemblages .NET en mémoire, une capacité utilisée notamment dans les opérations Red Team et dans certaines attaques.

Ceci est réalisé en examinant de près l'activité liée au chargement des [DLL associées à .NET](https://redhead0ntherun.medium.com/detecting-net-c-injection-execute-assembly-1894dbb04ff7), en particulier `clr.dll` et `mscoree.dll`.

## 4. Détection avec Sysmon Event ID 7

Le premier niveau de détection consiste à surveiller le chargement de DLL associées à l'environnement .NET.

Ce type de comportement de chargement de DLL peut souvent être détecté en exploitant l'ID d'événement 7 de Sysmon, qui correspond aux événements "Image Loaded" (Image chargée).

### DLL importantes

- `clr.dll` : composant du Common Language Runtime.
- `clrjit.dll` : composant de compilation Just-In-Time.
- `mscoree.dll` : composant associé à l'initialisation et à l'hébergement du runtime .NET Framework.

Sysmon Event ID 7 — Image Loaded permet d'identifier le chargement de ces DLL lorsqu'il est configuré pour les enregistrer.

### Scénario du lab — Seatbelt

Le cours utilise  [Seatbelt](https://github.com/GhostPack/Seatbelt), un outil .NET du projet GhostPack permettant d'énumérer diverses informations du système.

Commande de démonstration :

```
.\Seatbelt.exe TokenPrivileges
```


Cette commande affiche les privilèges du token associé au processus, notamment :

`SeDebugPrivilege`, `SeImpersonatePrivilege`, `SeBackupPrivilege`, etc., accompagnés de leur état.

![image-42](../../../../assets/sysmon-et-etw-image-42.png)

Dans le lab, l'exécution de `Seatbelt.exe` entraîne le chargement de bibliothèques .NET observables via Sysmon Event ID 7.

En supposant que Sysmon est configuré de manière appropriée pour journaliser les événements de chargement d'image (ID d'événement 7), l'exécution de 'Seatbelt.exe' déclencherait le chargement de DLL clés liées à .NET telles que 'clr.dll' et 'mscoree.dll'.

![Sysmon Event 7 : chargement d'image par Seatbelt.exe](../../../../assets/sysmon-et-etw-htb-windows-event-logs-44.png)

![Sysmon Event 7 : second chargement de DLL .NET par Seatbelt.exe](../../../../assets/sysmon-et-etw-htb-windows-event-logs-45.png)

### Limites de Sysmon

Sysmon permet de savoir quelles DLL ont été chargées et par quel processus, mais deux limites sont soulignées :

1. High Event Volume : l'Event ID 7 peut générer de très nombreux événements.
2. Limited Assembly Visibility : le chargement de `clr.dll` ne révèle pas directement les détails de l'assemblage .NET exécuté.

Par ailleurs, l'exemple Seatbelt est exécuté depuis le disque, même si la technique étudiée peut également concerner des assemblages chargés uniquement en mémoire.

### Retrouver les assemblies .NET avec un filtre XML

**1. Un exécutable précis initialise-t-il .NET ?** La requête du lab : `Seatbelt.exe` et `mscoree.dll`.

```xml
<QueryList>
  <Query Id="0" Path="Microsoft-Windows-Sysmon/Operational">
    <Select Path="Microsoft-Windows-Sysmon/Operational">
      *[
        System[EventID=7]
        and EventData[
          Data[@Name='Image']='C:\Tools\GhostPack Compiled Binaries\Seatbelt.exe'
          and Data[@Name='ImageLoaded']='C:\Windows\System32\mscoree.dll'
        ]
      ]
    </Select>
  </Query>
</QueryList>
```


- L'événement prouve l'initialisation du runtime .NET, pas ce que l'outil a exécuté : pour les méthodes, voir [Aller plus loin avec le provider DotNETRuntime](04-aller-plus-loin-avec-le-provider-dotnetruntime.md).
- Plusieurs DLL d'un coup : `(Data[@Name='ImageLoaded']='…\mscoree.dll' or Data[@Name='ImageLoaded']='…\clr.dll')`, parenthèses comprises.

**2. Quels exécutables .NET tournent depuis un dossier inhabituel ?** Les outils comme Seatbelt sont souvent déposés hors des dossiers d'installation :

```powershell
Get-WinEvent -LogName 'Microsoft-Windows-Sysmon/Operational' `
    -FilterXPath "*[System[EventID=7] and EventData[Data[@Name='ImageLoaded']='C:\Windows\System32\mscoree.dll']]" |
    ForEach-Object {
        $data = ([xml]$_.ToXml()).Event.EventData.Data
        ($data | Where-Object Name -eq 'Image').'#text'
    } |
    Where-Object { $_ -notlike 'C:\Windows\*' -and $_ -notlike 'C:\Program Files*' } |
    Sort-Object -Unique
```


- Résultat : les exécutables .NET lancés depuis un dossier utilisateur, un dossier d'outils ou `Temp`.
- Limite : un assembly chargé uniquement en mémoire dans un processus légitime n'apparaît pas ici ; c'est le rôle d'ETW.

Le lab pas à pas : [Question 1 — Suivre Seatbelt avec Sysmon et ETW](../04-labs/02-lab-3-travailler-avec-etw.md#question-1-suivre-seatbelt-avec-sysmon-et-etw).
