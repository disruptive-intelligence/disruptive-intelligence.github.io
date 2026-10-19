---
title: Repérer un DLL hijacking
source: IT/02 Windows/Repérer une attaque/Repérer un DLL hijacking.md
format: detection
provenance: HTB Academy
revue: '2026-10-19'
---

Un exécutable légitime charge une DLL placée par l'attaquant à la place de la bibliothèque attendue. Cette fiche montre comment le repérer dans les événements Sysmon `7` : où regarder, quelles requêtes lancer, quels indices retenir.

Installer et configurer Sysmon : [Sysmon et ETW](sysmon-et-etw/index.md). Lecture des journaux et requêtes XML : [Analyse des journaux d'événements Windows (Event Logs)](analyse-des-journaux-d-evenements-windows-event-logs/index.md).

## En bref

| | |
|---|---|
| Technique | Détournement de l'ordre de recherche des DLL (DLL hijacking) |
| MITRE ATT&CK | [T1574.001 — Hijack Execution Flow : DLL](https://attack.mitre.org/techniques/T1574/001/) |
| Journal | `Microsoft-Windows-Sysmon/Operational` |
| Événement | Sysmon `7` — chargement d'image (Image Loaded) |
| Indice clé | DLL système chargée hors de `System32`, non signée, par un exécutable lui aussi hors de sa place |

## Comprendre l'attaque

Le DLL hijacking exploite le mécanisme de recherche et de chargement des DLL de Windows : l'exécutable cherche d'abord ses DLL dans son propre dossier. Une DLL du même nom placée à côté de lui est chargée à la place de celle de Windows.

### Scénario du lab — calc.exe / WININET.dll

- `calc.exe`, un exécutable Windows légitime ;
- `WININET.dll`, une bibliothèque normalement fournie par Windows ;
- une DLL de démonstration renommée `WININET.dll`.

`calc.exe` est copié depuis `C:\Windows\System32` vers un dossier accessible en écriture (le bureau), avec la DLL de démonstration renommée `WININET.dll`. Au lancement de cette copie, la DLL de démonstration est chargée et affiche une [MessageBox](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxa) à la place de la Calculatrice.

![DLL detournables par calc.exe (dont WININET.dll)](../../assets/reperer-un-dll-hijacking-htb-windows-event-logs-21.png)

![calc.exe lance depuis le bureau : MessageBox Hello from DllMain!](../../assets/reperer-un-dll-hijacking-htb-windows-event-logs-22.png)

La DLL utilisée provient d'un exemple de Reflective DLL, mais le DLL hijacking ne nécessite pas de DLL réfléchissante.

Ressources :

- [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) (Sysinternals) ;
- [HijackLibs — calc.exe](https://hijacklibs.net/#calc.exe) : les DLL qu'un exécutable peut charger depuis son propre dossier ;
- [ReflectiveDLLInjection](https://github.com/stephenfewer/ReflectiveDLLInjection/tree/master/bin) : la DLL de démonstration du lab.

## Les traces

### Sysmon Event ID 7 — chargement d'image (Image Loaded)

L'Event ID `7` enregistre les chargements de modules, notamment de DLL. Sa collecte doit être activée dans la configuration Sysmon : voir [Configurer la collecte (ImageLoad)](sysmon-et-etw/01-detecter-avec-sysmon/01-installer-et-configurer-sysmon.md#configurer-la-collecte-imageload).

| Champ       | Description                                 |
| ----------- | ------------------------------------------- |
| Image       | Chemin du processus qui charge la DLL       |
| ImageLoaded | Chemin de la DLL chargée                    |
| ProcessId   | PID du processus                            |
| Signed      | Indication de signature numérique de la DLL |
| Signature   | Informations sur le signataire              |
| Hashes      | Empreintes de la DLL (`SHA256=…`)           |
| User        | Compte associé au processus                 |

Exemple légitime :

```
Image        : C:\Windows\System32\mmc.exe
ImageLoaded  : C:\Windows\System32\psapi.dll
Signed       : true
```


![Sysmon Event 7 : mmc.exe charge psapi.dll, signee](../../assets/reperer-un-dll-hijacking-htb-windows-event-logs-20.png)

L'événement indique que `mmc.exe` a chargé `psapi.dll`, signée par Microsoft.

### Le chargement détourné

Filtrer les événements Sysmon sur l'Event ID `7`, puis utiliser *Find* sur `calc.exe`.

![Filter Current Log : Sysmon/Operational, Event ID 7](../../assets/reperer-un-dll-hijacking-htb-windows-event-logs-23.png)

- *Find* retrouve la copie détournée de `calc.exe` :

![Chargement suspect : calc.exe charge WININET.dll non signee](../../assets/reperer-un-dll-hijacking-htb-windows-event-logs-24.png)

- La comparaison avec le `calc.exe` d'origine fait ressortir les chemins et les IOC à relever :

![Chargement legitime : calc.exe charge wininet.dll signee](../../assets/reperer-un-dll-hijacking-htb-windows-event-logs-25.png)

| Critère    | Chargement légitime                            | Chargement suspect du lab                   |
| ---------- | ---------------------------------------------- | ------------------------------------------- |
| Exécutable | `calc.exe` dans un emplacement Windows attendu | `calc.exe` copié dans un dossier modifiable |
| DLL        | `wininet.dll` depuis `System32`                | `WININET.dll` depuis le bureau              |
| Signature  | DLL Microsoft signée                           | DLL non signée                              |

## Les requêtes

*Find* parcourt tout le journal à la recherche d'un mot. Le filtre XML (*Filter Current Log…* → onglet **XML** → *Edit query manually*) vise directement les champs de l'Event ID 7 : `Image`, `ImageLoaded`, `Signed`. Gabarits et pièges : cheat sheet [Requêtes XML de l'Observateur](/cheatsheets/windows/fondamentaux/logs/requetes-xml/).

**1. Partir de la DLL suspecte** : quel processus a chargé la `WININET.dll` du bureau ?

```xml
<QueryList>
  <Query Id="0" Path="Microsoft-Windows-Sysmon/Operational">
    <Select Path="Microsoft-Windows-Sysmon/Operational">
      *[
        System[EventID=7]
        and EventData[
          Data[@Name='ImageLoaded']='C:\Users\Administrator\Desktop\WININET.dll'
        ]
      ]
    </Select>
  </Query>
</QueryList>
```


- `System[EventID=7]` : seulement les chargements d'image.
- `Data[@Name='ImageLoaded']` : la DLL chargée, chemin exact copié depuis la vue XML de l'événement (l'égalité est stricte).
- Dans l'événement obtenu : `Image` = l'exécutable qui l'a chargée (la copie de `calc.exe`) ; `Signed` = `false` ; `Hashes` = l'empreinte `SHA256=…` de la DLL, un IOC à rechercher ensuite sur d'autres machines.

**2. Partir de l'exécutable** : toutes les DLL chargées par la copie de `calc.exe`.

```xml
*[
  System[EventID=7]
  and EventData[
    Data[@Name='Image']='C:\Users\Administrator\Desktop\calc.exe'
  ]
]
```


- Le résultat liste toutes les DLL chargées au démarrage ; celle qui ne vient pas de `C:\Windows\System32\` ressort.
- Même requête avec `Image` = `C:\Windows\System32\calc.exe` : le chargement légitime, pour comparer chemin, signature et hash.

**3. Lister les DLL non signées** : quand on ne sait pas encore quel processus chercher (journaux exportés à trier, par exemple).

```xml
*[
  System[EventID=7]
  and EventData[
    Data[@Name='Signed']='false'
  ]
]
```


- Point de départ du tri : relever les couples `Image` / `ImageLoaded` situés hors de `C:\Windows\` et `C:\Program Files\`.

**4. « Hors de System32 » : ce que le XML ne sait pas faire.** L'Observateur ne compare que des valeurs exactes ; pour « toute `wininet.dll` chargée ailleurs que dans `C:\Windows\` », passer par PowerShell :

```powershell
Get-WinEvent -LogName 'Microsoft-Windows-Sysmon/Operational' -FilterXPath "*[System[EventID=7]]" |
    ForEach-Object {
        $data = ([xml]$_.ToXml()).Event.EventData.Data
        [PSCustomObject]@{
            Heure       = $_.TimeCreated
            Image       = ($data | Where-Object Name -eq 'Image').'#text'
            ImageLoaded = ($data | Where-Object Name -eq 'ImageLoaded').'#text'
            Signed      = ($data | Where-Object Name -eq 'Signed').'#text'
        }
    } |
    Where-Object { $_.ImageLoaded -like '*\wininet.dll' -and $_.ImageLoaded -notlike 'C:\Windows\*' }
```


- `-FilterXPath` garde les Event ID 7 ; `ForEach-Object` extrait les champs de chaque événement (méthode détaillée dans [Extraire les champs d'un événement avec .ToXml()](analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#extraire-les-champs-dun-evenement-avec-toxml)) ; `Where-Object` garde les `wininet.dll` chargées hors de `C:\Windows\`.
- `-like` ignore la casse : `WININET.dll` et `wininet.dll` sont trouvées toutes les deux.
- Remplacer `wininet.dll` par une autre DLL listée par HijackLibs pour l'exécutable étudié.
- Journaux exportés : `-Path 'C:\…\fichier.evtx'` à la place de `-LogName '…'`.

### Dans un journal exporté (.evtx)

Exemple : le journal Sysmon `DLLHijack.evtx`.

#### Découvrir le contenu du fichier

```powershell
Get-WinEvent -Path ".\DLLHijack.evtx" -MaxEvents 5 |
    Format-List TimeCreated, Id, ProviderName, Message
```


#### Filtrer sur l'Id 7

```powershell
Get-WinEvent -FilterHashtable @{
    Path = ".\DLLHijack.evtx"
    Id   = 7
} -MaxEvents 10 |
    Format-List TimeCreated, Message
```


#### Filtrer une DLL à examiner

```powershell
Get-WinEvent -FilterHashtable @{
    Path = ".\DLLHijack.evtx"
    Id   = 7
} |
    Where-Object { $_.Message -like "*NOM_DLL.dll*" } |
    Format-List TimeCreated, Message
```


#### Réduire le bruit : filtrer sur un dossier (Temp en exemple)

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '.\DLLHijack.evtx'
    Id   = 7
} |
    Where-Object { $_.Message -like '*ImageLoaded:*Temp\*' } |
    Format-List TimeCreated, Message
```


#### Chercher les DLL non signées

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '.\DLLHijack.evtx'
    Id   = 7
} |
Where-Object { $_.Message -match 'Signed: false' } |
Select-Object -First 20 |
Format-List TimeCreated, Message
```


- `Get-WinEvent` : récupère les événements Sysmon ID 7.
- `Where-Object` : conserve ceux dont le message indique `Signed: false`.
- `-match` : recherche une correspondance avec une expression régulière.
- `Select-Object -First 20` : limite l'affichage aux 20 premiers résultats correspondants.
- `Format-List` : affiche les événements sans tronquer le message comme pourrait le faire un tableau.

#### Extraire les champs Image et ImageLoaded

Cette commande :

1. lit le fichier EVTX ;
2. conserve les événements ID 7 ;
3. convertit chaque événement en XML ;
4. extrait les champs `Image` et `ImageLoaded` ;
5. affiche les résultats sous forme d'objets PowerShell.

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '.\DLLHijack.evtx'
    Id   = 7
} -MaxEvents 10 |
ForEach-Object {
    $data = ([xml]$_.ToXml()).Event.EventData.Data

    [pscustomobject]@{
        Heure       = $_.TimeCreated
        Image       = ($data | Where-Object Name -eq 'Image').'#text'
        ImageLoaded = ($data | Where-Object Name -eq 'ImageLoaded').'#text'
    }
} | Format-List
```


On reprend la commande précédente, mais on stocke les résultats dans `$events` :

```powershell
$events = Get-WinEvent -FilterHashtable @{
    Path = '.\DLLHijack.evtx'
    Id   = 7
} | ForEach-Object {
    $data = ([xml]$_.ToXml()).Event.EventData.Data

    [pscustomobject]@{
        Image       = ($data | Where-Object Name -eq 'Image').'#text'
        ImageLoaded = ($data | Where-Object Name -eq 'ImageLoaded').'#text'
    }
}
```


Rappel :

- `Image` = processus qui charge une DLL.
- `ImageLoaded` = chemin de la DLL chargée.

#### Compter les processus et les DLL différents

Nombre de processus distincts :

```powershell
$events.Image | Sort-Object -Unique | Measure-Object
```


Nombre de DLL distinctes :

```powershell
$events.ImageLoaded | Sort-Object -Unique | Measure-Object
```


`Sort-Object -Unique` élimine les doublons, et `Measure-Object` compte les valeurs restantes.

#### Voir chaque processus et son nombre d'apparitions

```powershell
$events |
    Group-Object Image |
    Sort-Object Count -Descending |
    Select-Object Count, Name
```


Exemple fictif :

```text
Count Name
----- ----
   25 C:\Windows\System32\svchost.exe
   12 C:\Windows\System32\notepad.exe
    4 C:\Tools\test.exe
```


Un processus peut apparaître plusieurs fois parce qu'il a chargé plusieurs DLL.

Même chose pour `ImageLoaded` :

```powershell
$events |
    Group-Object ImageLoaded |
    Sort-Object Count -Descending |
    Select-Object Count, Name
```


Exemple fictif :

```text
Count Name
----- ----
   15 C:\Windows\System32\kernel32.dll
    8 C:\Windows\System32\ntdll.dll
    3 C:\Temp\test.dll
```


On voit immédiatement quelles DLL sont les plus fréquemment chargées.

#### Bonus : compter les associations processus / DLL

Très intéressant pour détecter un DLL hijacking :

```powershell
$events |
    Group-Object Image, ImageLoaded |
    Sort-Object Count -Descending |
    Select-Object Count, Name
```


On obtient le nombre d'occurrences pour chaque association entre un processus et une DLL.

#### À retenir

| Ce que tu recherches | Commande |
|---|---|
| Nombre total d'événements Sysmon 7 récupérés | `$events.Count` |
| Nombre de processus distincts | `$events.Image \| Sort-Object -Unique \| Measure-Object` |
| Nombre de DLL distinctes | `$events.ImageLoaded \| Sort-Object -Unique \| Measure-Object` |
| Nombre d'apparitions de chaque processus | `$events \| Group-Object Image` |
| Nombre d'apparitions de chaque DLL | `$events \| Group-Object ImageLoaded` |

Chaque événement Sysmon ID 7 contient normalement un champ `Image` et un champ `ImageLoaded`, mais plusieurs événements peuvent concerner le même processus ou la même DLL. En forensic, `Group-Object` est particulièrement puissant.

## Les indicateurs

1. Exécutable hors de son emplacement (Unexpected Executable Path) : `calc.exe` s'exécute depuis un emplacement utilisateur modifiable. Il se trouve normalement dans System32, pas dans un répertoire accessible en écriture.
2. DLL hors de son emplacement (Unexpected DLL Location) : `WININET.dll` est chargée depuis un emplacement inhabituel. Elle se trouve normalement dans System32 ; si `calc.exe` la charge ailleurs, c'est un détournement de DLL au sein de `calc.exe`.
3. DLL non signée (Unsigned DLL) : la `WININET.dll` originale est signée par Microsoft, la DLL de démonstration ne l'est pas.

```
calc.exe — Unexpected Location
          ↓
Loads WININET.dll — User-Writable Directory
          ↓
Unsigned DLL
          ↓
Potential DLL Hijacking
```


Ces critères peuvent alimenter une règle de détection.

## Les faux positifs

- `Image` désigne le processus qui charge la DLL, pas son processus parent.
- Une DLL non signée ou située hors de `System32` n'est pas malveillante à elle seule : logiciels tiers, applications portables et outils internes chargent souvent leurs propres DLL non signées depuis leur dossier.
- Les trois indicateurs se lisent ensemble : un nom de DLL système, chargée hors de `System32`, non signée, par un exécutable Windows copié ailleurs.
- L'Event ID 7 est très volumineux : en production, la configuration Sysmon le restreint souvent, et le chargement recherché peut ne pas avoir été journalisé.

## Pour s'entraîner

- Lab pas à pas : [Sysmon et ETW › Labs › Question 1 — DLL hijacking : WININET.dll](sysmon-et-etw/04-labs/01-lab-2-analyser-avec-sysmon.md#question-1-dll-hijacking-wininetdll).
- Event IDs Sysmon et requêtes SIEM : cheat sheet [Sysmon](/cheatsheets/windows/fondamentaux/logs/sysmon/).

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
