---
title: 'Chapitre 37 — Analyser : journaux, Sysmon et timeline'
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie IX — Initiation à l'investigation numérique
  - index.md
---

## 🟢 Le minimum à savoir

### L'outil du chapitre : transformer un événement en objet

Au Ch.34 (section « Comprendre XML et XPath »), tu as appris à lire **un** champ d'événement par son nom grâce à `ToXml()` et `.'#text'`. Tout ce chapitre repose sur ce geste. On en fait donc une fonction qui convertit un événement **entier** en `PSCustomObject`, avec une propriété par champ :

```powershell
function ConvertTo-EventObject {
    [CmdletBinding()]
    param(
        # Pas « $Event » : c'est une variable automatique de PowerShell, à ne pas réutiliser
        [Parameter(Mandatory, ValueFromPipeline)] $Evenement
    )
    process {
        $xml = [xml]$Evenement.ToXml()
        $obj = [ordered]@{
            TimeUtc = $Evenement.TimeCreated.ToUniversalTime()
            Id      = $Evenement.Id
            Journal = $Evenement.LogName
            Machine = $Evenement.MachineName
        }
        # Une propriété par champ de l'événement, nommée comme dans l'événement
        foreach ($champ in $xml.Event.EventData.Data) {
            if ($champ.Name) { $obj[$champ.Name] = $champ.'#text' }
        }
        [PSCustomObject]$obj
    }
}
```


```powershell
# Les 5 dernières connexions réussies, lisibles                       [🔑 Admin]
Get-WinEvent -FilterHashtable @{ LogName = 'Security'; Id = 4624 } -MaxEvents 5 |
    ConvertTo-EventObject |
    Select-Object TimeUtc, TargetUserName, LogonType, IpAddress, TargetLogonId
```


> **📌 Réflexe `Get-Member` :** `… | ConvertTo-EventObject | Get-Member` te montre tous les champs disponibles pour ce type d'événement. Chaque Event ID a les siens : c'est le meilleur moyen de les découvrir.

> **Performance :** `ToXml()` est lent sur des dizaines de milliers d'événements. Le bon réflexe : **filtrer d'abord** avec `-FilterHashtable` (Id, période), **convertir ensuite**, et stocker le résultat dans une variable plutôt que de reconvertir à chaque requête.

### Le journal Security en profondeur

Le Ch.34 t'a donné les identifiants. Ici, on apprend à lire les **champs** — c'est là qu'est l'information.

#### 4624 — Connexion réussie : le `LogonType`

Un 4624 sans son `LogonType`, c'est la moitié de l'information. C'est lui qui dit **comment** la personne s'est connectée :

| LogonType | Nom | Ce que ça veut dire |
|---|---|---|
| **2** | Interactive | Quelqu'un au clavier de la machine |
| **3** | Network | Accès réseau : partage SMB, remoting PowerShell |
| **4** | Batch | Tâche planifiée |
| **5** | Service | Démarrage d'un service |
| **7** | Unlock | Déverrouillage de session |
| **8** | NetworkCleartext | Connexion réseau où le mot de passe a été remis **non haché** au composant d'authentification de la machine (ex. : authentification « basique » d'un site IIS). Il n'a pas forcément circulé en clair sur le réseau : HTTPS peut l'avoir protégé |
| **9** | NewCredentials | `runas /netonly` |
| **10** | RemoteInteractive | Connexion **RDP** |
| **11** | CachedInteractive | Connexion avec des identifiants en cache (contrôleur de domaine injoignable) |

Les autres champs clés : `TargetUserName` et `TargetDomainName` (**qui**), `IpAddress` et `WorkstationName` (**d'où**), `AuthenticationPackageName` (NTLM ou Kerberos), et surtout **`TargetLogonId`** : l'identifiant de la session qui vient de s'ouvrir. On le retrouvera dans les événements de processus, et c'est lui qui fera le pont entre « qui s'est connecté » et « ce que cette session a fait ».

```powershell
# Qui s'est connecté en RDP ces 7 derniers jours, et d'où ?            [🔑 Admin]
Get-WinEvent -FilterHashtable @{ LogName = 'Security'; Id = 4624; StartTime = (Get-Date).AddDays(-7) } |
    ConvertTo-EventObject |
    Where-Object LogonType -eq "10" |
    Select-Object TimeUtc, TargetUserName, IpAddress, TargetLogonId
```


> **Réduire le bruit.** Un poste génère énormément de 4624 : services (type 5), compte `SYSTEM`, comptes d'ordinateur (dont le nom se termine par `$`, comme `CLIENT01$`). Filtrer sur le type et exclure les comptes en `$` divise le volume par dix.

#### 4625 — Échec de connexion : pourquoi ?

Le 4625 dit qu'une connexion a échoué ; ses champs `Status` et `SubStatus` disent **pourquoi**. Le code général est souvent dans `Status`, le détail dans `SubStatus` : lis les deux.

| Code | Signification | Ce que ça peut suggérer |
|---|---|---|
| `0xC000006A` | Mot de passe incorrect (le compte **existe**) | Faute de frappe… ou attaque ciblée sur ce compte |
| `0xC0000064` | Le compte **n'existe pas** | Nom mal tapé… ou énumération de comptes au hasard |
| `0xC0000234` | Compte verrouillé | Conséquence d'une rafale d'échecs |
| `0xC0000072` | Compte désactivé | Tentative sur le compte d'un ancien employé ? |
| `0xC0000071` | Mot de passe expiré | Le plus souvent légitime |

La **forme** des échecs en dit autant que les codes :

- **beaucoup d'échecs sur un seul compte** → force brute (Ch.34) ;
- **peu d'échecs sur beaucoup de comptes**, depuis la même source → *password spraying* (un mot de passe courant essayé partout) ;
- **beaucoup de `0xC0000064`** → l'attaquant devine des noms de comptes.

```powershell
# Les combinaisons « source + raison » les plus fréquentes sur 24 h      [🔑 Admin]
Get-WinEvent -FilterHashtable @{ LogName = 'Security'; Id = 4625; StartTime = (Get-Date).AddDays(-1) } |
    ConvertTo-EventObject |
    Group-Object IpAddress, SubStatus |
    Sort-Object Count -Descending |
    Select-Object Count, Name -First 10
```


> Les codes apparaissent en minuscules dans les événements (`0xc000006a`). Aucun souci : les comparaisons de chaînes de PowerShell ignorent la casse.

#### Les autres événements Security à lire

| ID | Événement | Champs utiles |
|---|---|---|
| **4672** | Privilèges spéciaux attribués à la session (session de niveau administrateur) | `SubjectUserName`, `SubjectLogonId` (= le `TargetLogonId` du 4624) |
| **4688** | Processus créé | `NewProcessName`, `ParentProcessName`, `CommandLine`, `NewProcessId`, `SubjectLogonId` |
| **4697** | Service installé | `ServiceName`, `ServiceFileName` |
| **4698** | Tâche planifiée créée | `TaskName`, `TaskContent` (la définition XML complète de la tâche) |

> **⚠️ Rappel Ch.34 :** 4688, 4697 et 4698 n'existent que si la **stratégie d'audit** correspondante est activée. Leur absence ne prouve rien.

> **⚠️ Piège des identifiants hexadécimaux.** Dans le journal Security, les numéros de processus et de session sont écrits en **hexadécimal** : `NewProcessId = 0x1a2c`. Sysmon, lui, écrit les PID en décimal. Pour comparer : `[Convert]::ToInt32("0x1a2c", 16)` donne `6700`.

### Le journal System : la vie de la machine

Le journal System raconte quand la machine a été allumée, éteinte, et ce qui a changé dans ses services :

| ID | Source | Signification |
|---|---|---|
| **6005** | EventLog | Service de journalisation démarré : ≈ **démarrage** de la machine |
| **6006** | EventLog | Service de journalisation arrêté : ≈ **arrêt propre** |
| **6008** | EventLog | L'arrêt précédent était **inattendu** (plantage, coupure… ou prise arrachée) |
| **1074** | User32 | Arrêt ou redémarrage **demandé** : par quel processus, quel utilisateur, pour quelle raison |
| **7045** | Service Control Manager | Nouveau service installé (persistance, Ch.34) |
| **7040** | Service Control Manager | Type de démarrage d'un service modifié |
| **104** | EventLog | Un journal (autre que Security) a été **effacé** |

```powershell
# Les démarrages et arrêts récents de la machine
Get-WinEvent -FilterHashtable @{ LogName = 'System'; Id = 6005, 6006, 6008, 1074 } -MaxEvents 30 |
    Select-Object TimeCreated, Id, Message
```


> **Un journal vide n'est pas un journal propre.** Un attaquant qui efface ses traces vide souvent les journaux. Mais l'effacement lui-même est journalisé : **1102** dans Security, **104** dans System pour les autres journaux. Un journal anormalement court, qui commence par l'un de ces événements, est un signal fort.

### Sysmon : la télémétrie qui manque aux journaux natifs

Les journaux natifs ont des angles morts. Le 4688 dit qu'un processus a été créé (si l'audit est actif), mais pas son empreinte, ni avec qui il a communiqué, ni quels noms DNS il a demandés, ni quels fichiers il a déposés. **Sysmon** (*System Monitor*), un outil gratuit de Microsoft, comble précisément ces manques.

**L'installer** `[🔑 Admin]` :

- **Version Sysinternals** (toutes versions de Windows, serveurs compris) : on télécharge Sysmon sur le site Microsoft Sysinternals, puis on l'installe **avec un fichier de configuration** :
    ```powershell
    .\Sysmon64.exe -accepteula -i .\sysmonconfig.xml
    ```
    Sans configuration, Sysmon journalise peu de choses. Le point de départ standard est une configuration communautaire reconnue, comme celle de SwiftOnSecurity (*sysmon-config*) ou d'Olaf Hartong (*sysmon-modular*). Tu apprendras à lire ce fichier un peu plus bas (« Lire une configuration Sysmon »).
- **Version intégrée à Windows** : depuis 2026, Windows 11 (24H2 et ultérieures) propose Sysmon comme **fonctionnalité facultative** (*Paramètres → Système → Fonctionnalités facultatives*), qu'on active puis qu'on initialise avec `sysmon -i`. Une version Sysinternals déjà installée doit d'abord être désinstallée. Les serveurs ne sont pas encore concernés au moment où ce cours est écrit : vérifie la documentation Microsoft à jour.

**Trouver son journal** (réflexe de découverte, comme au Ch.1) :

```powershell
Get-WinEvent -ListLog *Sysmon*      # en général : Microsoft-Windows-Sysmon/Operational
```


#### Les cinq Event IDs à connaître

Ces cinq événements répondent aux questions de toute investigation : *qu'est-ce qui s'est exécuté*, *avec qui ça a communiqué*, *quelles traces ça a laissées*.

| ID | Événement | Champs clés | La question |
|---|---|---|---|
| **1** | Création de processus | `Image`, `CommandLine`, `ParentImage`, `ParentCommandLine`, `User`, `LogonId`, `Hashes`, `ProcessGuid`, `ParentProcessGuid` | Qu'est-ce qui s'est exécuté, et lancé par quoi ? |
| **3** | Connexion réseau | `Image`, `DestinationIp`, `DestinationPort`, `DestinationHostname`, `Initiated`, `ProcessGuid` | Avec qui ça a communiqué ? |
| **11** | Création de fichier | `Image`, `TargetFilename`, `ProcessGuid` | Qu'est-ce que ça a déposé sur le disque ? |
| **13** | Valeur de registre modifiée | `Image`, `TargetObject`, `Details`, `ProcessGuid` | Qu'est-ce que ça a changé dans le registre ? (persistance, Ch.12) |
| **22** | Requête DNS | `Image`, `QueryName`, `QueryResults`, `ProcessGuid` | Quels noms a-t-il cherché à joindre ? |

> Dans l'événement 3, `Initiated = true` signifie que c'est la machine qui a **ouvert** la connexion (sortante) : c'est le cas d'un malware qui contacte son serveur de commande.

#### `ProcessGuid` : pourquoi pas le PID ?

Windows **recycle** les numéros de processus : le PID 4512 de 10 h peut désigner un tout autre programme à 14 h. Sysmon attribue donc à chaque processus un **`ProcessGuid`**, unique pour toute la vie de la machine. Deux conséquences décisives :

- **Tout ce qu'un processus a fait** (événements 3, 11, 13, 22) porte son `ProcessGuid` : on peut tout rassembler en une seule requête.
- **Son parent** est désigné par `ParentProcessGuid` : on peut remonter la chaîne jusqu'à l'origine.

#### Le signal classique : un parent inattendu

Un document Word qui lance PowerShell, c'est le scénario typique d'une macro malveillante. La relation **parent → enfant** est l'un des signaux les plus utiles de Sysmon :

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Microsoft-Windows-Sysmon/Operational'; Id = 1; StartTime = (Get-Date).AddDays(-1)
} | ConvertTo-EventObject |
    Where-Object { $_.ParentImage -match '\\(winword|excel|outlook)\.exe$' -and
                   $_.Image -match '\\(powershell|pwsh|cmd|wscript|mshta)\.exe$' } |
    Select-Object TimeUtc, ParentImage, Image, CommandLine, User
```


## 🟡 Très utile en pratique

### Lire une configuration Sysmon : le même XML, un autre usage

Au Ch.34, le XML servait à **interroger** des événements déjà enregistrés. Le fichier de configuration de Sysmon utilise le même langage pour une tâche opposée : **décider quels événements enregistrer**. Confondre les deux est une source classique d'heures perdues.

| | Requête XPath / QueryList (Ch.34) | Configuration Sysmon |
|---|---|---|
| **Rôle** | Rechercher dans des événements **déjà enregistrés** | Décider ce que Sysmon **enregistrera** |
| **Quand** | Après coup, pendant l'analyse | Avant, à l'installation ou à la mise à jour |
| **Où** | `-FilterXPath`, `-FilterXml`, Observateur d'événements | `sysmonconfig.xml`, chargé par `Sysmon64 -i` (installation) ou `Sysmon64 -c` (mise à jour) |
| **À quoi ça ressemble** | `*[System[EventID=1]]` | `<ProcessCreate onmatch="include">` |

Voici une configuration minimale, pour apprendre à la lire :

```xml
<Sysmon schemaversion="4.90">
  <EventFiltering>
    <!-- Événement 1 : on enregistre TOUT, sauf ce qui est exclu -->
    <RuleGroup name="" groupRelation="or">
      <ProcessCreate onmatch="exclude">
        <Image condition="is">C:\Program Files\Outil\scanner.exe</Image>
      </ProcessCreate>
    </RuleGroup>
    <!-- Événement 7 : on n'enregistre QUE ce qui est inclus -->
    <RuleGroup name="" groupRelation="or">
      <ImageLoad onmatch="include">
        <ImageLoaded condition="contains">\Temp\</ImageLoaded>
      </ImageLoad>
    </RuleGroup>
  </EventFiltering>
</Sysmon>
```


> La valeur de `schemaversion` dépend de ta version de Sysmon : `Sysmon64 -s` affiche le schéma qu'elle attend. Et `Sysmon64 -c`, sans fichier, affiche la configuration actuellement chargée.

**Règle n°1 — L'élément extérieur est un TYPE d'événement, les éléments intérieurs sont des CHAMPS.** `<ImageLoad>` désigne l'événement 7, le chargement d'une DLL par un processus. `<ImageLoaded>`, à l'intérieur, est le **champ** qui contient le chemin de la DLL chargée. Une lettre d'écart, deux natures différentes : l'un est une catégorie, l'autre une donnée. C'est le piège le plus fréquent en lisant une configuration.

| Event ID | Balise du type d'événement | Exemples de champs utilisables à l'intérieur |
|---|---|---|
| 1 | `ProcessCreate` | `Image`, `CommandLine`, `ParentImage` |
| 3 | `NetworkConnect` | `DestinationIp`, `DestinationPort` |
| 7 | `ImageLoad` | `ImageLoaded` (la DLL chargée), `Image` (le processus **qui** la charge), `Signed` |
| 11 | `FileCreate` | `TargetFilename` |
| 12, 13, 14 | `RegistryEvent` | `TargetObject` |
| 22 | `DnsQuery` | `QueryName` |

La bonne nouvelle : **le nom d'un champ est le même partout**. Balise dans la configuration (`<ImageLoaded>`), attribut dans l'événement enregistré (`<Data Name="ImageLoaded">`), et donc dans tes requêtes : `Data[@Name='ImageLoaded']`. Par exemple, pour retrouver les DLL non signées chargées :

```powershell
Get-WinEvent -LogName 'Microsoft-Windows-Sysmon/Operational' `
    -FilterXPath "*[System[EventID=7] and EventData[Data[@Name='Signed']='false']]"
```


**Règle n°2 — `include` et `exclude` ne fonctionnent pas en miroir.**

- `onmatch="include"` : n'enregistrer **que** ce qui correspond aux règles.
- `onmatch="exclude"` : enregistrer **tout, sauf** ce qui correspond.
- **Le piège :** un bloc `include` **vide** n'enregistre **rien** (rien ne correspond), tandis qu'un bloc `exclude` vide enregistre **tout**. C'est d'ailleurs ainsi que les configurations désactivent un type d'événement : `<ProcessTerminate onmatch="include" />`.

**Règle n°3 — Plusieurs conditions dans un bloc, c'est OU.** Par défaut, il suffit qu'**une** condition corresponde. Pour exiger plusieurs conditions **ensemble**, on les regroupe dans une `<Rule groupRelation="and">` :

```xml
<ProcessCreate onmatch="include">
  <Rule groupRelation="and">
    <ParentImage condition="end with">\winword.exe</ParentImage>
    <Image condition="end with">\powershell.exe</Image>
  </Rule>
</ProcessCreate>
```


Cette règle enregistre PowerShell **lancé par** Word : le signal du parent inattendu, vu plus haut. Sans le `<Rule groupRelation="and">`, elle enregistrerait n'importe quel processus lancé par Word, **ainsi que** n'importe quel PowerShell quel que soit son parent : ce n'est plus du tout la même règle.

> **Un contraste utile avec le Ch.34.** La configuration Sysmon dispose de conditions riches (`is`, `contains`, `begin with`, `end with`…), alors que le XPath des journaux ne connaît pas `contains()`. Ce que Sysmon a filtré à l'enregistrement n'existe plus : aucune requête, aussi bien écrite soit-elle, ne le fera réapparaître.

### Analyser des journaux hors ligne

C'est le cas normal en investigation : on n'analyse pas la machine suspecte, on analyse les `.evtx` collectés au Ch.36, **sur une autre machine**. La commande est la même, avec `-Path` à la place de `-LogName`, et la clé `Path` dans le filtre :

```powershell
$preuves = "D:\Analyse\Collecte_SRV01"      # une COPIE de la collecte, pas l'original

# 0. Avant tout : les preuves sont-elles intactes ? (Test-EvidenceIntegrity, Ch.36)

# 1. Lire un fichier .evtx
Get-WinEvent -Path "$preuves\Security.evtx" -MaxEvents 10

# 2. Filtrer efficacement : la clé Path remplace LogName
Get-WinEvent -FilterHashtable @{ Path = "$preuves\Security.evtx"; Id = 4624, 4625 } |
    ConvertTo-EventObject
```


Trois pièges propres à l'analyse hors ligne :

1. **Travaille sur une copie**, après avoir vérifié les empreintes. `Get-WinEvent` ne modifie rien, mais c'est une discipline : l'original ne sert qu'à prouver.
2. **La propriété `Message` peut être vide.** Le texte lisible d'un événement est fabriqué à partir de fichiers installés sur la machine **d'analyse**. Si Sysmon n'y est pas installé, les événements Sysmon d'un `.evtx` n'auront pas de message. Les **champs**, eux, sont bien dans le fichier : `ConvertTo-EventObject` fonctionne. Encore une raison de lire les champs par leur nom.
3. **Le fuseau horaire.** `TimeCreated` s'affiche dans le fuseau de **ta** machine. Si la preuve vient d'une machine réglée sur un autre fuseau, compare tout en UTC (la propriété `TimeUtc` de `ConvertTo-EventObject`), et garde sous la main le fuseau noté dans `00_contexte.json`.

> **S'entraîner sans attaquer son lab.** Des chercheurs publient des fichiers `.evtx` enregistrés pendant de vraies techniques d'attaque, par exemple le dépôt GitHub **EVTX-ATTACK-SAMPLES**. Ce ne sont que des journaux : ils s'ouvrent sans risque avec `Get-WinEvent -Path`, et chacun raconte une attaque que tu peux essayer de reconstituer.

### Corréler : les trois clés

Corréler, c'est relier des événements de sources différentes qui parlent de la même chose. Trois clés le permettent :

| Clé | Ce qu'elle relie | Attention |
|---|---|---|
| **Le temps (UTC)** | Tout avec tout, mais seulement pour **ordonner** | Fuseaux horaires ; horloges de machines différentes pas toujours synchronisées |
| **Le `LogonId`** | Une session (4624, 4672) avec les processus lancés dedans (Sysmon 1 : `LogonId` ; 4688 : `SubjectLogonId`) | Écrit en hexadécimal, avec une casse variable selon la source |
| **Le `ProcessGuid`** | Un processus avec tout ce qu'il a fait (Sysmon 3, 11, 13, 22) et avec son parent | Sysmon uniquement |

Pour comparer des `LogonId` de sources différentes sans se soucier du format, on les convertit en nombre :

```powershell
function ConvertFrom-HexId([string]$Valeur) { [Convert]::ToInt64($Valeur, 16) }

ConvertFrom-HexId "0x3E7"     # 999 : le LogonId de SYSTEM
ConvertFrom-HexId "0x3e7"     # 999 aussi : la casse ne compte plus
```


> Quelques `LogonId` reviennent sans cesse et sont bons à reconnaître : `0x3e7` (SYSTEM), `0x3e4` (NETWORK SERVICE), `0x3e5` (LOCAL SERVICE).

### Pivoter : remonter le fil d'une attaque

La méthode d'analyse s'appelle le **pivot** : on part d'**un** événement suspect, et on tire les fils un par un grâce aux clés.

```powershell
$preuves = "D:\Analyse\Collecte_SRV01"

# Charger et convertir UNE fois, puis travailler sur ces variables
$evSysmon   = Get-WinEvent -Path "$preuves\Microsoft-Windows-Sysmon_Operational.evtx" |
              ConvertTo-EventObject
$evSessions = Get-WinEvent -FilterHashtable @{ Path = "$preuves\Security.evtx"; Id = 4624 } |
              ConvertTo-EventObject

# 1. Le point de départ : un PowerShell lancé avec une commande encodée
$suspect = $evSysmon |
    Where-Object { $_.Id -eq 1 -and $_.CommandLine -match '-enc' } |
    Select-Object -First 1

# 2. Lancé par quoi ? Le parent, via ParentProcessGuid
$evSysmon | Where-Object { $_.Id -eq 1 -and $_.ProcessGuid -eq $suspect.ParentProcessGuid } |
    Select-Object TimeUtc, Image, CommandLine

# 3. Dans quelle session ? La connexion d'origine, via le LogonId
$id = ConvertFrom-HexId $suspect.LogonId
$evSessions | Where-Object { (ConvertFrom-HexId $_.TargetLogonId) -eq $id } |
    Select-Object TimeUtc, TargetUserName, LogonType, IpAddress

# 4. Qu'a-t-il fait ? Tout ce qui porte son ProcessGuid
$evSysmon | Where-Object ProcessGuid -eq $suspect.ProcessGuid |
    Select-Object TimeUtc, Id, DestinationIp, DestinationPort, QueryName, TargetFilename, TargetObject
```


Ce que tu viens de faire, c'est exactement le travail d'un analyste : **point de départ → parent → session → actions**. Chaque étape n'est qu'une requête filtrée ; c'est leur enchaînement qui raconte l'histoire.

> Si l'étape 1 ne trouve rien, `$suspect` est vide et les étapes suivantes ne renvoient rien : vérifie-le avant de continuer (Réflexe n°2 : on teste avant d'agir). Et note que `-enc` est un **signal**, pas une preuve : des outils légitimes utilisent aussi des commandes encodées.

### La timeline : tout remettre dans l'ordre

Une timeline rassemble des événements hétérogènes dans un format **commun**, puis les trie par date. On normalise chaque événement en quelques colonnes identiques :

```powershell
function ConvertTo-TimelineEntry {
    param([Parameter(ValueFromPipeline)] $E)
    process {
        # Les Id ne sont uniques qu'au sein d'un journal : ici on ne mélange que Security et Sysmon
        $quoi = switch ($E.Id) {
            4624    { "Connexion (type $($E.LogonType)) : $($E.TargetUserName) depuis $($E.IpAddress)" }
            4625    { "Échec de connexion : $($E.TargetUserName) ($($E.SubStatus))" }
            1       { "Processus : $($E.Image)  ←  $($E.ParentImage)" }
            3       { "Réseau : $($E.Image) → $($E.DestinationIp):$($E.DestinationPort)" }
            11      { "Fichier créé : $($E.TargetFilename)" }
            13      { "Registre : $($E.TargetObject)" }
            22      { "DNS : $($E.QueryName)" }
            default { "Événement $($E.Id)" }
        }
        [PSCustomObject]@{
            TimeUtc     = $E.TimeUtc
            Journal     = $E.Journal
            EventId     = $E.Id
            Quoi        = $quoi
            ProcessGuid = $E.ProcessGuid
            LogonId     = if ($E.LogonId) { $E.LogonId } else { $E.TargetLogonId }
        }
    }
}

$timeline = (@($evSessions) + @($evSysmon)) |
    ConvertTo-TimelineEntry |
    Sort-Object TimeUtc

$timeline | Export-Csv "D:\Analyse\timeline.csv" -NoTypeInformation -Encoding UTF8

# Zoom : une heure autour de l'événement suspect
$debut = $suspect.TimeUtc.AddMinutes(-30)
$fin   = $suspect.TimeUtc.AddMinutes(30)
$timeline | Where-Object { $_.TimeUtc -ge $debut -and $_.TimeUtc -le $fin } |
    Format-Table TimeUtc, EventId, Quoi -AutoSize
```


> **Une timeline n'est pas une preuve, c'est un récit.** Deux événements proches dans le temps ne sont pas forcément liés. Ce sont les **clés** (`LogonId`, `ProcessGuid`) qui établissent un lien ; le temps ne fait que l'ordonner.

## 🔴 Bonus

### Kerberos sur le contrôleur de domaine

Sur un contrôleur de domaine, le journal Security contient les événements Kerberos :

| ID | Événement |
|---|---|
| **4768** | Ticket d'authentification (TGT) demandé : une ouverture de session au domaine |
| **4769** | Ticket de service demandé : l'accès à un service (partage, base de données…) |
| **4771** | Pré-authentification Kerberos échouée : l'équivalent Kerberos du 4625 |

Une attaque classique, le *Kerberoasting*, consiste à demander en masse des tickets de service pour tenter de casser hors ligne le mot de passe des comptes de service. Elle se repère souvent à une rafale de 4769 demandés par un même compte avec un chiffrement faible (`TicketEncryptionType` = `0x17`, c'est-à-dire RC4).

### Repérer un binaire renommé

Sysmon enregistre dans l'événement 1 le champ `OriginalFileName` : le nom **inscrit à l'intérieur** du programme lors de sa compilation. Un attaquant qui renomme `powershell.exe` en `svchost.exe` change le nom du fichier, pas son nom interne :

```powershell
$evSysmon |
    Where-Object { $_.Id -eq 1 -and $_.OriginalFileName -and
                   (Split-Path $_.Image -Leaf) -ne $_.OriginalFileName } |
    Select-Object TimeUtc, Image, OriginalFileName
```


Attends-toi à des faux positifs : certains programmes légitimes ont un nom interne différent de leur nom de fichier. C'est une liste **à trier**, pas une liste de coupables.

### Au-delà de PowerShell

Pour de gros volumes, des outils spécialisés appliquent automatiquement des milliers de règles de détection (au format **Sigma**) sur des fichiers `.evtx` : **Hayabusa** et **Chainsaw**, par exemple. Et **Timeline Explorer** (d'Eric Zimmerman) est un visualiseur confortable pour les timelines au format CSV, comme celle que tu viens de produire. Ce que tu as appris ici reste la base : ces outils font plus vite ce que tu sais désormais faire à la main, et tu comprendras ce qu'ils te montrent.

## ❌ Erreur classique

```powershell
# Utiliser le PID comme identifiant unique
Where-Object ProcessId -eq 4512        # ⚠️ recyclé : peut désigner un autre processus plus tard
Where-Object ProcessGuid -eq $guid     # ✅ unique

# Comparer un PID hexadécimal (journal Security) à un PID décimal (Sysmon)
"0x1a2c" -eq 6700                           # ❌ False
[Convert]::ToInt32("0x1a2c", 16) -eq 6700   # ✅ True

# Mélanger heure locale et UTC dans une timeline
# ❌ un décalage d'une ou deux heures peut inverser l'ordre des événements
# ✅ tout convertir en UTC (TimeUtc) avant de trier

# Se fier à la propriété Message hors ligne
# ❌ vide si le fournisseur (ex. : Sysmon) n'est pas installé sur la machine d'analyse
# ✅ lire les champs par leur nom (ConvertTo-EventObject)

# Conclure de l'absence d'un événement
# ❌ « pas de 4688, donc rien n'a été exécuté » : l'audit était peut-être désactivé (Ch.34)
```


Et deux erreurs classiques dans une configuration Sysmon :

```xml
<!-- Confondre le type d'événement et le champ -->
<ImageLoad condition="contains">\Temp\</ImageLoad>          <!-- ❌ ImageLoad est le TYPE (événement 7) -->
<ImageLoad onmatch="include">
  <ImageLoaded condition="contains">\Temp\</ImageLoaded>    <!-- ✅ ImageLoaded est le CHAMP, DANS le type -->
</ImageLoad>

<!-- Laisser un bloc include vide en croyant tout enregistrer -->
<NetworkConnect onmatch="include" />    <!-- ❌ n'enregistre AUCUNE connexion -->
<NetworkConnect onmatch="exclude" />    <!-- ✅ enregistre tout (à affiner ensuite) -->
```


## 💡 Exercices

**Guidé :** Sur ton poste, liste tes 10 dernières connexions (4624) en excluant les comptes en `$` et les services (type 5), avec `TimeUtc`, `TargetUserName`, `LogonType` et `TargetLogonId`. Verrouille puis déverrouille ta session (`Windows + L`), relance la commande, et identifie le nouvel événement grâce à son `LogonType`.

**Guidé (hors ligne) :** Ouvre le `Security.evtx` de ta collecte du Ch.36 (après avoir vérifié son empreinte), et compte les événements par Id avec `Group-Object`.

**Autonome :** Écris `Get-ProcessTree`, qui part d'un `ProcessGuid` et remonte récursivement les `ParentProcessGuid` pour afficher la chaîne complète, par exemple `explorer.exe → winword.exe → powershell.exe`. Prévois le cas où un parent est absent des journaux (il a démarré avant l'installation de Sysmon, ou ses événements ont tourné).

**Autonome :** Télécharge un fichier du dépôt EVTX-ATTACK-SAMPLES et réponds aux quatre questions de la méthode du pivot : qu'est-ce qui s'est exécuté, lancé par quoi, dans quelle session, avec quelles actions ?

## 🧩 Capstone Partie IX — Rapport d'investigation

L'avantage d'un lab, c'est que **tu connais la vérité** : tu vas jouer toi-même un petit scénario, puis vérifier que ton analyse le retrouve.

1. **Prépare** : installe Sysmon sur CLIENT01 avec une configuration communautaire.
2. **Joue le scénario** (inoffensif) : depuis `cmd.exe`, lance PowerShell ; exécute `Resolve-DnsName example.com` ; crée un fichier dans `$env:TEMP` ; ajoute une valeur dans `HKCU:\Software\Microsoft\Windows\CurrentVersion\Run` (par exemple `notepad.exe`), puis **supprime-la**. Note l'heure.
3. **Collecte** avec ton `Invoke-LiveResponse.ps1` (Ch.36), journal Sysmon compris.
4. **Analyse hors ligne**, sur une copie, après vérification du manifeste : retrouve la session (4624), le processus et son parent (Sysmon 1), la requête DNS (22), le fichier (11) et la modification du registre (13).
5. **Livre** : la timeline en CSV, et un court rapport en trois parties : *les faits* (ce que les journaux prouvent), *la chronologie*, et *ce qui reste inexpliqué*.

> Si un événement attendu manque, ne conclus pas trop vite : certaines configurations Sysmon filtrent volontairement des événements pour limiter le bruit. Regarde ta configuration avec `Sysmon64 -c` (section « Lire une configuration Sysmon »). C'est aussi une leçon : ce que tu ne vois pas dépend de ce que tu as choisi d'écouter.

## ✅ Tu sais maintenant...

- Convertir n'importe quel événement en objet (`ConvertTo-EventObject`) et explorer ses champs
- Lire un 4624 (`LogonType`, `TargetLogonId`) et un 4625 (codes d'échec), et reconnaître force brute, *spraying* et énumération
- Lire le journal System : démarrages, arrêts, arrêts inattendus, effacements de journaux
- Ce que Sysmon ajoute aux journaux natifs, ses Event IDs 1, 3, 11, 13, 22 et leurs champs
- Lire une configuration Sysmon : type d'événement contre champ (`ImageLoad` / `ImageLoaded`), `include` contre `exclude`, conditions combinées avec `<Rule groupRelation="and">`
- Pourquoi on suit un processus par son `ProcessGuid` et non par son PID
- Analyser des `.evtx` hors ligne, et éviter ses trois pièges
- Corréler avec le temps, le `LogonId` et le `ProcessGuid`, pivoter depuis un événement suspect, et construire une timeline

## 💬 Questions d'entretien typiques

- **Comment distinguer une connexion RDP d'un accès à un partage dans les journaux ?** → Par le `LogonType` du 4624 : 10 pour RDP, 3 pour un accès réseau.
- **Comment relier une connexion aux processus lancés pendant cette session ?** → Par le `LogonId` : le `TargetLogonId` du 4624 se retrouve dans le `LogonId` de Sysmon 1 et le `SubjectLogonId` du 4688.
- **Dans une configuration Sysmon, quelle différence entre `<ImageLoad>` et `<ImageLoaded>` ?** → `<ImageLoad>` désigne le type d'événement (7, chargement d'une DLL) ; `<ImageLoaded>` est un champ de cet événement, le chemin de la DLL chargée. Le premier contient le second.
- **Un bloc `<NetworkConnect onmatch="include" />` vide : que se passe-t-il ?** → Aucune connexion n'est enregistrée, puisque rien ne correspond à une liste d'inclusion vide. Un bloc `exclude` vide, à l'inverse, enregistrerait tout.
- **Pourquoi `ProcessGuid` plutôt que le PID ?** → Windows recycle les PID ; le `ProcessGuid` de Sysmon est unique et relie un processus à toutes ses actions et à son parent.
- **Force brute ou *password spraying* : comment les distinguer ?** → La force brute vise un compte avec beaucoup d'essais ; le spraying vise beaucoup de comptes avec peu d'essais chacun. Le `SubStatus` des 4625 précise la cause de chaque échec.
- **Le journal Security est presque vide : que conclus-tu ?** → Rien de rassurant : on cherche un 1102 (effacement), on vérifie la stratégie d'audit et la taille maximale du journal.

---
