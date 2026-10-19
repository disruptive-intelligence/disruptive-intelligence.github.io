---
title: Repérer le chargement d'assemblies .NET
source: IT/02 Windows/Repérer une attaque/Repérer le chargement d'assemblies .NET.md
format: detection
provenance: HTB Academy
revue: '2026-10-19'
---

Un attaquant apporte ses propres outils .NET et les exécute, parfois directement en mémoire. Cette fiche montre comment le repérer en deux niveaux : le chargement du runtime .NET dans Sysmon `7`, puis le détail des assemblies et des méthodes avec le provider ETW `Microsoft-Windows-DotNETRuntime`.

Sysmon et ETW (installation, providers, SilkETW) : [Sysmon et ETW](sysmon-et-etw/index.md). Détection voisine, du code .NET injecté dans un processus natif : [Repérer du PowerShell non managé](reperer-du-powershell-non-manage.md).

## En bref

| | |
|---|---|
| Technique | Chargement d'assemblies .NET malveillants (Bring Your Own Land) |
| MITRE ATT&CK | [T1620 — Reflective Code Loading](https://attack.mitre.org/techniques/T1620/) |
| Journaux | `Microsoft-Windows-Sysmon/Operational` ; trace ETW `Microsoft-Windows-DotNETRuntime` (SilkETW) |
| Événements | Sysmon `7` (chargement de `clr.dll`, `mscoree.dll`) ; ETW : assemblies chargées, méthodes compilées |
| Indice clé | Un exécutable inconnu ou lancé depuis un dossier inhabituel initialise .NET ; ETW donne les noms de ses méthodes |

## Comprendre l'attaque

### Living off the Land — LotL

Le Living off the Land (LotL) consiste à utiliser des outils légitimes déjà présents sur le système pour des activités malveillantes : PowerShell, outils natifs Windows, composants d'administration. Les exécutables utilisés appartenant à l'environnement légitime, la détection est plus difficile.

Des contre-mesures ont depuis compliqué cet usage ; les attaquants ont développé une autre approche, que Mandiant qualifie de BYOL.

### Bring Your Own Land — BYOL

Avec le Bring Your Own Land (BYOL), décrit par Mandiant, les attaquants introduisent leurs propres outils plutôt que de s'appuyer seulement sur les outils natifs, par exemple des assemblages .NET développés en C#. Ces assemblages peuvent être chargés et exécutés directement en mémoire.

### Pourquoi .NET ?

| Caractéristique               | Intérêt                                                                                                                                                                                                                                  |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Common Language Runtime (CLR) | Permet l'exécution de code managé                                                                                                                                                                                                        |
| Memory Management             | Fournit notamment le Garbage Collection                                                                                                                                                                                                  |
| In-Memory Assembly Loading    | Permet de charger des assemblages sans nécessairement écrire leur fichier sur disque                                                                                                                                                     |
| .NET Libraries                | Fournissent des fonctionnalités HTTP, cryptographiques et IPC. Ces outils pré-construits rationalisent le processus de développement, réduisent la probabilité d'erreurs et facilitent la création d'applications robustes et efficaces. |
| Windows Integration           | Les composants .NET sont présents dans de nombreux environnements Windows. Chaque système Windows est équipé par défaut d'une certaine version de .NET pré-installée.                                                                    |

L'exécution en mémoire réduit certains artefacts sur disque et complique les détections fondées seulement sur l'analyse des fichiers. Elle ne rend cependant pas le code invisible aux outils de sécurité.

### Exemple — Cobalt Strike execute-assembly

La commande ["execute-assembly"](https://www.cobaltstrike.com/blog/cobalt-strike-3-11-the-snake-that-eats-its-tail/) de Cobalt Strike exécute des assemblages .NET en mémoire, une capacité utilisée dans les opérations Red Team et dans certaines attaques. On la repère en examinant le chargement des [DLL associées à .NET](https://redhead0ntherun.medium.com/detecting-net-c-injection-execute-assembly-1894dbb04ff7), en particulier `clr.dll` et `mscoree.dll`.

### Scénario du lab — Seatbelt

[Seatbelt](https://github.com/GhostPack/Seatbelt) est un outil .NET du projet GhostPack qui énumère diverses informations du système.

```
.\Seatbelt.exe TokenPrivileges
```


Cette commande affiche les privilèges du token associé au processus (`SeDebugPrivilege`, `SeImpersonatePrivilege`, `SeBackupPrivilege`, etc.) avec leur état.

![image-42](../../assets/reperer-le-chargement-d-assemblies-net-image-42.png)

## Les traces

### Sysmon Event ID 7 — le runtime .NET se charge

Le premier niveau de détection consiste à surveiller, avec l'Event ID 7 (Image Loaded), le chargement des DLL de l'environnement .NET :

- `clr.dll` : composant du Common Language Runtime ;
- `clrjit.dll` : composant de compilation Just-In-Time ;
- `mscoree.dll` : composant associé à l'initialisation et à l'hébergement du runtime .NET Framework.

Si Sysmon journalise les chargements d'image, l'exécution de `Seatbelt.exe` fait apparaître le chargement de `clr.dll` et `mscoree.dll`.

![Sysmon Event 7 : chargement d'image par Seatbelt.exe](../../assets/reperer-le-chargement-d-assemblies-net-htb-windows-event-logs-44.png)

![Sysmon Event 7 : second chargement de DLL .NET par Seatbelt.exe](../../assets/reperer-le-chargement-d-assemblies-net-htb-windows-event-logs-45.png)

Sysmon dit quelles DLL ont été chargées et par quel processus, avec deux limites :

1. Volume élevé (High Event Volume) : l'Event ID 7 peut générer de très nombreux événements.
2. Visibilité limitée sur l'assembly (Limited Assembly Visibility) : le chargement de `clr.dll` ne révèle pas l'assemblage .NET exécuté.

Seatbelt est ici exécuté depuis le disque ; la technique concerne aussi des assemblages chargés uniquement en mémoire.

### ETW — le provider Microsoft-Windows-DotNETRuntime

Le provider ETW `Microsoft-Windows-DotNETRuntime` observe l'activité du runtime .NET, notamment le chargement des assemblages et certaines opérations de compilation. SilkETW collecte ses événements :

```
SilkETW.exe -t user -pn Microsoft-Windows-DotNETRuntime -uk 0x2038 -ot file -p C:\Windows\Temp\etw.json
```


Cette commande collecte un sous-ensemble d'événements du provider et les écrit dans `etw.json`. Le paramètre `-uk 0x2038` sélectionne les mots-clés ETW (keywords) suivants :

| Keyword        | Fonction                                                                    | Intérêt Threat Hunting                                                                                                         |
| -------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| JitKeyword     | Événements liés à la compilation Just-In-Time                               | Examiner certaines méthodes compilées pendant l'exécution, utile pour comprendre le flux d'exécution de l'assemblage .NET.     |
| InteropKeyword | Interactions entre code managé et non managé                                | Pourraient fournir des informations sur les interactions potentielles avec des API natives ou d'autres composants non managés. |
| LoaderKeyword  | Détails sur le processus de chargement d'assemblage au sein du runtime .NET | Identifier les assemblages chargés et potentiellement exécutés.                                                                |
| NGenKeyword    | Activités liées aux images natives précompilées                             | Examiner l'utilisation de composants .NET précompilés                                                                          |

Le filtrage par keywords cible les événements pertinents sans collecter toute la télémétrie du provider. Cet [article de blog](https://medium.com/threat-hunters-forge/threat-hunting-with-etw-events-and-helk-part-1-installing-silketw-6eb74815e4a0) détaille SilkETW et l'identification de logiciels malveillants .NET.

Après une nouvelle exécution de Seatbelt, `etw.json` contient davantage d'informations sur l'assemblage chargé, notamment des noms de méthodes : une visibilité bien plus détaillée qu'un événement Sysmon signalant le chargement de `clr.dll`.

![etw.json : evenements DotNETRuntime de Seatbelt avec les noms de methodes](../../assets/reperer-le-chargement-d-assemblies-net-htb-windows-event-logs-46.png)

## Les requêtes

**Un exécutable précis initialise-t-il .NET ?** La requête du lab : `Seatbelt.exe` et `mscoree.dll`.

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


- L'événement prouve l'initialisation du runtime .NET, pas ce que l'outil a exécuté : pour les méthodes, voir la recherche dans la trace ETW ci-dessous.
- Plusieurs DLL d'un coup : `(Data[@Name='ImageLoaded']='…\mscoree.dll' or Data[@Name='ImageLoaded']='…\clr.dll')`, parenthèses comprises.

**Quelles méthodes ont été appelées ?** Dans la trace SilkETW, chercher les noms de méthodes plutôt que de parcourir le JSON à la main :

```powershell
Select-String -Path "C:\Windows\Temp\etw.json" `
    -Pattern '"ManagedInteropMethodName"\s*:\s*"[^"]+"' -AllMatches |
ForEach-Object { $_.Matches.Value } |
Sort-Object -Unique
```


- Résultat : les noms de méthodes distincts de toute la trace. Pour les attribuer à une exécution, les replacer dans leur contexte (heure, processus).

Gabarits et pièges du XML : cheat sheet [Requêtes XML de l'Observateur](/cheatsheets/windows/fondamentaux/logs/requetes-xml/).

## Les indicateurs

```
Seatbelt.exe Execution
          ↓
.NET Runtime Initialization
          ↓
Sysmon Event ID 7
 → CLR DLL Loading
          ↓
Microsoft-Windows-DotNETRuntime
 → Assembly Loading
 → JIT / Method Information
          ↓
Detailed .NET Investigation
```


- Un exécutable inconnu, ou lancé depuis un dossier utilisateur, un dossier d'outils ou `Temp`, qui charge `mscoree.dll` / `clr.dll`.
- Dans la trace ETW, des noms d'assemblies ou de méthodes typiques d'outils offensifs (énumération des privilèges, du système, des identifiants).

## Les faux positifs

- Beaucoup d'applications légitimes sont écrites en .NET : le chargement de `clr.dll` est banal, seul le contexte (exécutable, dossier, utilisateur, moment) le rend suspect.
- Les informations ETW dépendent des keywords activés, des événements effectivement émis et du comportement de compilation du runtime : tous les appels de méthodes ne sont pas enregistrés.
- Une collecte ETW est volumineuse : la lancer de façon ciblée, le temps de vérifier une hypothèse.

## Pour s'entraîner

- Lab pas à pas : [Sysmon et ETW › Labs › Question 1 — Suivre Seatbelt avec Sysmon et ETW](sysmon-et-etw/04-labs/02-lab-3-travailler-avec-etw.md#question-1-suivre-seatbelt-avec-sysmon-et-etw).
- Commandes ETW et SilkETW : cheat sheet [ETW](/cheatsheets/windows/fondamentaux/logs/etw/).

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
