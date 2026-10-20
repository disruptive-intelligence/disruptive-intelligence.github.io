---
title: Chapitre 34 — Diagnostic, logs et triage
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie VIII — PowerShell pour la cybersécurité
  - index.md
---

## 🟢 Le minimum à savoir

### Les journaux d'événements Windows

Les **Event Logs** sont la mémoire de Windows : chaque événement notable (connexion, erreur, démarrage de service, création de compte…) y est enregistré. C'est **la** source d'information pour le diagnostic et la sécurité. La cmdlet moderne est `Get-WinEvent`.

```powershell
# Lister les journaux disponibles et leur volume
Get-WinEvent -ListLog * | Where-Object RecordCount -gt 0 |
    Select-Object LogName, RecordCount | Sort-Object RecordCount -Descending

# Lire les derniers événements d'un journal
Get-WinEvent -LogName System -MaxEvents 20
Get-WinEvent -LogName Security -MaxEvents 20     # [🔑 Admin]
```


> **📌 Réflexe `Get-Member` :** `Get-WinEvent -LogName System -MaxEvents 1 | Get-Member` révèle `TimeCreated`, `Id`, `LevelDisplayName`, `Message`, `ProviderName`. Ces propriétés permettent de filtrer et corréler les événements.

### Filtrer efficacement avec `-FilterHashtable`

> **⚠️ Point de performance majeur.** Sur un journal de millions d'événements, filtrer **côté serveur** avec `-FilterHashtable` est incomparablement plus rapide que tout ramener puis filtrer avec `Where-Object` (même logique qu'`-Filter` en AD, Ch.23).

```powershell
# ✅ RAPIDE : le filtre est appliqué à la source
Get-WinEvent -FilterHashtable @{
    LogName   = 'Security'
    Id        = 4625              # échecs de connexion
    StartTime = (Get-Date).AddHours(-24)
}

# ❌ LENT : ramène tout, puis filtre
Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4625 }
```


### Les Event IDs à connaître

| Event ID | Journal | Signification |
|----------|---------|--------------|
| **4624** | Security | Connexion réussie |
| **4625** | Security | **Échec** de connexion (brute-force si répété) |
| **4634 / 4647** | Security | Déconnexion |
| **4720** | Security | **Création** d'un compte utilisateur |
| **4726** | Security | Suppression d'un compte |
| **4732 / 4728** | Security | Ajout à un groupe (local / global) — surveiller les groupes admin |
| **4688** | Security | Création d'un processus (traçabilité des exécutions) |
| **7045** | System | **Installation d'un nouveau service** (persistance possible) |
| **1102** | Security | **Effacement du journal de sécurité** (signal fort) |

> **⚠️ Les Event IDs dépendent de la stratégie d'audit — l'absence d'un événement ne prouve pas l'absence d'activité.** Windows ne génère la plupart de ces événements que si l'**audit correspondant est activé** (par GPO, Ch.25). Exemple concret : l'événement **4688** (création de processus) n'apparaît que si *Audit Process Creation* est activé ; et pour que la **ligne de commande** du processus soit renseignée dans l'événement, il faut **en plus** activer *Include command line in process creation events* — sinon le champ reste vide.
>
> C'est un piège conceptuel majeur en défense : conclure « aucun 4688 → aucun processus suspect créé » est un **faux négatif**. Le bon réflexe est celui du Ch.35 sur le 4104 : avant d'interpréter une absence, **vérifier que la journalisation est configurée**. Un journal muet peut signifier « rien ne s'est passé »… ou « on n'écoutait pas ».

> **➡️ Pour aller plus loin :** ce tableau te donne les identifiants. Le Ch.37 (Partie IX, optionnelle) t'apprend à lire leurs **champs** (`LogonType`, codes d'échec, `LogonId`) et à les corréler avec Sysmon pour reconstituer une attaque.

### Comprendre XML et XPath pour analyser les journaux Windows

Chaque événement Windows est stocké sous la forme d'un document **XML**. Tant que tu te contentes de `Id`, `TimeCreated` et `Message`, tu n'en as pas besoin. Mais dès que tu veux le **détail** d'un événement (le compte visé, l'adresse IP, le type de connexion), il faut savoir lire ce XML, et savoir l'interroger. C'est ce que fait la détection de brute-force juste après, et c'est le socle des Ch.35 et 37. On procède en quatre temps.

#### 1. La structure d'un document XML

Commence par regarder le XML brut d'une connexion réussie :

```powershell
# Le XML complet du dernier événement 4624                                   [🔑 Admin]
(Get-WinEvent -FilterHashtable @{ LogName = 'Security'; Id = 4624 } -MaxEvents 1).ToXml()
```


Tu obtiens un long texte. En voici l'essentiel, simplifié :

```xml
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Security-Auditing" />
    <EventID>4624</EventID>
    <TimeCreated SystemTime="2026-10-17T14:02:11.5291430Z" />
    <Computer>CLIENT01.lab.local</Computer>
  </System>
  <EventData>
    <Data Name="TargetUserName">alice</Data>
    <Data Name="TargetLogonId">0x5a3f21</Data>
    <Data Name="LogonType">3</Data>
    <Data Name="IpAddress">192.168.1.50</Data>
  </EventData>
</Event>
```


Le vocabulaire, sur cet exemple :

| Terme | Dans l'exemple | Ce que c'est |
|---|---|---|
| **Élément** (ou balise) | `<EventID>4624</EventID>` | Une balise ouvrante, une balise fermante (avec `/`), et ce qu'il y a entre les deux |
| **Valeur** (le texte) | `4624` | Le contenu d'un élément |
| **Attribut** | `Name="TargetUserName"` | Une information placée **dans** la balise ouvrante, sous la forme `nom="valeur"` |
| **Élément vide** | `<TimeCreated SystemTime="…" />` | Aucun contenu, seulement des attributs ; il se referme lui-même avec `/>` |
| **Imbrication** | `<System>` contient `<EventID>` | Un élément **parent** contient des éléments **enfants** : c'est une arborescence, comme des dossiers |
| **Racine** | `<Event>` | L'élément qui contient tout le reste |

Tout événement a deux blocs, et la différence entre les deux est essentielle :

- **`System`** est **commun à tous les événements** : l'ID, l'heure (toujours en UTC, d'où le `Z` final), la machine, la source. Sa structure est la même partout.
- **`EventData`** est **propre à chaque type d'événement** : ce sont ses champs détaillés. Et c'est là que se cache la difficulté : tous les champs sont des éléments portant **le même nom**, `<Data>`. Ce qui les distingue, c'est leur **attribut** `Name`. On ne peut donc pas désigner « le champ TargetUserName » directement : il faut dire « l'élément `Data` dont l'attribut `Name` vaut `TargetUserName` ». Garde cette phrase en tête, elle revient partout.

> La première ligne porte un attribut `xmlns` (un « espace de noms »). Tu peux l'ignorer : il ne gêne ni la navigation PowerShell ni les filtres de `Get-WinEvent`.

#### 2. Lire et manipuler du XML avec PowerShell

`ToXml()` renvoie du **texte**. Le type `[xml]` le transforme en une arborescence d'objets dans laquelle on descend avec des points, comme dans des dossiers :

```powershell
$ev  = Get-WinEvent -FilterHashtable @{ LogName = 'Security'; Id = 4624 } -MaxEvents 1   # [🔑 Admin]
$xml = [xml]$ev.ToXml()

$xml.Event.System.EventID                   # 4624
$xml.Event.System.Computer                  # CLIENT01.lab.local
$xml.Event.System.TimeCreated.SystemTime    # un ATTRIBUT se lit comme une propriété

# EventData est une LISTE d'éléments Data : on les affiche tous
$xml.Event.EventData.Data | Format-Table Name, '#text'
```


**Le mystère du `'#text'`.** Pourquoi `.EventID` donne directement `4624`, alors qu'un `Data` exige `'#text'` ? C'est une règle de PowerShell :

- un élément **sans attribut** est présenté directement comme son texte (`<EventID>4624</EventID>` → `4624`) ;
- un élément **avec des attributs** devient un objet : ses attributs sont des propriétés (`.Name`), et son texte se range dans une propriété spéciale nommée **`#text`**. Les guillemets autour de `'#text'` sont obligatoires, à cause du `#`.

Pour extraire **un** champ, on applique la phrase à retenir, mot pour mot : « l'élément `Data` dont le `Name` vaut `TargetUserName` », puis son texte :

```powershell
($xml.Event.EventData.Data | Where-Object Name -eq 'TargetUserName').'#text'     # alice
```


C'est exactement la ligne qu'utilise la détection de brute-force ci-dessous, et le cœur de la fonction `ConvertTo-EventObject` du Ch.37.

> **📌 Le `Get-Member` des événements.** Face à un Event ID que tu ne connais pas, `$xml.Event.EventData.Data | Format-Table Name, '#text'` liste tous ses champs avec leurs valeurs. C'est le premier réflexe d'exploration.

> **Cas particulier.** Dans certains journaux, `EventID` porte lui-même un attribut (`<EventID Qualifiers="16384">7036</EventID>`) : `.EventID` affiche alors un objet au lieu d'un nombre, et il faut écrire `.EventID.'#text'`. Même règle, appliquée ailleurs. Pour l'ID, de toute façon, `$ev.Id` est plus simple.

#### 3. Interroger les journaux avec XPath

**XPath** est un langage qui désigne des parties d'un document XML. Windows l'utilise pour filtrer les événements **à la source**, aussi vite que `-FilterHashtable`, mais avec une capacité en plus : filtrer sur la **valeur des champs** de `EventData`.

Sa grammaire, pour les journaux, tient en quelques symboles :

| Symbole | Se lit | Exemple |
|---|---|---|
| `*` | « n'importe quel événement » | `*[…]` |
| `[ … ]` | « **dont** … » : une condition sur l'élément juste à sa gauche | `System[EventID=4625]` |
| `@` | « l'attribut » | `@Name`, `@SystemTime` |
| `=`, `!=`, `<`, `<=`, `>`, `>=` | comparaisons | `EventID=4625` |
| `and`, `or`, `( )` | combiner des conditions | `(EventID=4624 or EventID=4625)` |

**Lire les crochets à voix haute.** `*[System[EventID=4625]]` se lit : « tout événement (`*`) **dont** (`[`) le `System` a (`[`) un `EventID` égal à 4625 (`]]`) ». Chaque `[` ouvre une condition sur l'élément qui le précède ; les crochets s'emboîtent comme des parenthèses. Premier réflexe en cas d'erreur : **compter** qu'il y a autant de `]` que de `[`.

Des exemples, du plus simple au plus complet :

```text
*[System[EventID=4625]]
    → les échecs de connexion

*[System[(EventID=4624 or EventID=4625)]]
    → les connexions réussies OU échouées (les parenthèses regroupent le « or »)

*[EventData[Data[@Name='TargetUserName']='alice']]
    → tous les événements qui concernent le compte alice

*[System[EventID=4625] and EventData[Data[@Name='LogonType']='3']]
    → les échecs de connexion par le réseau (type 3)

*[System[EventID=4625 and TimeCreated[timediff(@SystemTime) <= 86400000]]]
    → les échecs des dernières 24 heures (86 400 000 millisecondes)
```


Le morceau le plus déroutant est `Data[@Name='LogonType']='3'`. Coupe-le en deux :

- `Data[@Name='LogonType']` → « l'élément `Data` dont l'attribut `Name` vaut `LogonType` » : il **choisit le bon champ** ;
- `='3'` → « … et dont la valeur vaut 3 » : il **compare son texte**.

C'est la traduction XPath exacte de ce que tu fais en PowerShell avec `Where-Object Name -eq 'LogonType'` puis `.'#text'`.

**Dans PowerShell**, la requête se passe à `-FilterXPath` :

```powershell
$requete = "*[System[EventID=4625] and EventData[Data[@Name='LogonType']='3']]"
Get-WinEvent -LogName Security -FilterXPath $requete                      # [🔑 Admin]
```


XPath utilise des guillemets **simples** à l'intérieur : la chaîne PowerShell se met donc entre guillemets **doubles**. Et comme une chaîne entre guillemets doubles interprète les `$`, n'en mets pas dans la requête (XPath n'en a pas besoin).

> **⚠️ Les limites du XPath des journaux.** Windows n'accepte qu'un **sous-ensemble** de XPath : pas de `contains()`, pas de `starts-with()`, pas d'expressions régulières. Pour « le nom de commande contient… », filtre d'abord à la source sur ce que XPath sait faire (ID, période, valeurs exactes), puis affine avec `Where-Object`.

**Pour aller plus loin : `-FilterXml`.** Une requête XPath ne vise qu'un journal. Le format complet, appelé *QueryList*, permet d'interroger **plusieurs journaux** d'un coup et d'**exclure** des cas avec `Suppress` :

```powershell
$requete = @'
<QueryList>
  <Query Id="0" Path="Security">
    <Select Path="Security">*[System[(EventID=4624 or EventID=4625)]]</Select>
    <Select Path="System">*[System[EventID=7045]]</Select>
    <Suppress Path="Security">*[EventData[Data[@Name='LogonType']='5']]</Suppress>
  </Query>
</QueryList>
'@
Get-WinEvent -FilterXml ([xml]$requete)                                   # [🔑 Admin]
```


Ici : les connexions (réussies ou échouées) et les installations de services, **sauf** les connexions de services (type 5), qui ne sont que du bruit.

> **💡 L'astuce pour apprendre la syntaxe.** Dans l'Observateur d'événements, construis ton filtre avec l'interface (*Filtrer le journal actuel…*), puis ouvre l'onglet **XML** : il affiche la requête correspondante, prête à copier dans PowerShell. C'est la meilleure façon de comprendre comment une requête s'écrit.

#### 4. Quel filtre choisir ?

| Ton besoin | L'outil |
|---|---|
| Filtrer sur l'ID, la période, le niveau | `-FilterHashtable` : le plus simple, à utiliser par défaut |
| Filtrer sur la valeur d'un champ, combiner `and` / `or` | `-FilterXPath` |
| Interroger plusieurs journaux d'un coup, exclure des cas | `-FilterXml` |
| « Contient », expressions régulières, logique complexe | Filtrer large à la source, puis `Where-Object` |

> **Le même XML, un tout autre usage.** Le XML sert aussi à **configurer** Sysmon, l'outil de surveillance présenté au Ch.37 : mêmes balises, mêmes attributs, mais un rôle opposé. Ici on **interroge** des événements déjà enregistrés ; là, on **décide quels événements enregistrer**. On les comparera au Ch.37, au moment d'installer Sysmon.

### Détecter une attaque par brute-force

Un cas d'école, qui réunit filtrage, lecture du XML (que tu viens de voir), regroupement et seuil :

```powershell
# Compter les échecs de connexion (4625) par compte sur 24h
Get-WinEvent -FilterHashtable @{ LogName='Security'; Id=4625; StartTime=(Get-Date).AddHours(-24) } |
    ForEach-Object {
        # On convertit l'événement en XML pour lire le champ PAR SON NOM (TargetUserName),
        # plutôt que par une position d'index fragile.
        $xml = [xml]$_.ToXml()
        ($xml.Event.EventData.Data | Where-Object Name -eq 'TargetUserName').'#text'
    } |
    Group-Object |
    Where-Object Count -gt 10 |
    Select-Object @{N="Compte";E={$_.Name}}, Count |
    Sort-Object Count -Descending
```


> **⚠️ Ne lis pas les champs d'un event par index (`$_.Properties[5]`).** L'ordre et le nombre des propriétés d'un événement **varient** selon la version de Windows et le type d'événement : un index en dur casse silencieusement (tu lis le mauvais champ). La méthode robuste : convertir l'événement en XML (`$_.ToXml()`) et lire le champ **par son nom** (`TargetUserName` pour le compte ciblé, `IpAddress` pour la source…). C'est un peu plus verbeux, mais fiable dans le temps.

Un compte avec des dizaines d'échecs en peu de temps = tentative de brute-force à investiguer. C'est exactement le genre de détection qu'un analyste blue team automatise.

## 🟡 Le triage : appliquer ses connaissances d'admin

Le **triage** consiste à examiner rapidement un système suspect. Tout ce qu'on a appris devient un point de contrôle. La logique : **comparer à la normale**.

### Vérifier l'intégrité d'un fichier : `Get-FileHash`

```powershell
Get-FileHash "C:\Windows\System32\cmd.exe" -Algorithm SHA256
```


Comparer le hash d'un fichier à une référence connue détecte une altération. On vérifie aussi un téléchargement contre le hash publié par l'éditeur.

### Vérifier la signature : `Get-AuthenticodeSignature`

```powershell
Get-AuthenticodeSignature "C:\Windows\System32\cmd.exe" |
    Select-Object Status, SignerCertificate
```


Un binaire système **non signé** ou à signature **invalide** dans un emplacement système est très suspect. `Status = Valid` et un signataire Microsoft sont attendus pour les fichiers système.

### Détecter la persistance : les points de démarrage automatique

Un attaquant cherche à **survivre au redémarrage**. Les mécanismes de persistance sont exactement les objets qu'on sait déjà administrer :

```powershell
# 1. Clés Run/RunOnce du registre (rappel Ch.12)
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue

# 2. Tâches planifiées non-Microsoft (rappel Ch.13)
Get-ScheduledTask | Where-Object { $_.TaskPath -notlike "\Microsoft\*" } |
    Select-Object TaskName, @{N="Action";E={$_.Actions.Execute}}

# 3. Services dont le binaire est dans un emplacement inhabituel (rappel Ch.11)
Get-CimInstance Win32_Service |
    Where-Object { $_.PathName -notlike "*\Windows\*" -and $_.PathName -notlike "*Program Files*" } |
    Select-Object Name, PathName, StartName

# 4. Nouveaux services récemment installés (Event ID 7045)
Get-WinEvent -FilterHashtable @{ LogName='System'; Id=7045; StartTime=(Get-Date).AddDays(-7) } -ErrorAction SilentlyContinue
```


> **La bascule admin → sécurité :** remarque que ce sont **exactement** les mêmes cmdlets qu'en administration (Ch.11, 12, 13). La différence est l'**intention** : là où l'admin configure, l'analyste **compare à la normale** pour repérer l'anomalie. C'est pour ça qu'on a appris l'administration d'abord.

### Détecter les comptes et connexions suspects

```powershell
# Membres du groupe Administrateurs locaux — ciblé par SID pour être portable FR/EN (rappel Ch.10)
$grpAdmins = Get-LocalGroup | Where-Object SID -eq "S-1-5-32-544"
Get-LocalGroupMember -Group $grpAdmins.Name

# Connexions établies HORS du réseau 192.168.x.x du lab (rappel Ch.17)
Get-NetTCPConnection -State Established |
    Where-Object { $_.RemoteAddress -notlike "192.168.*" -and $_.RemoteAddress -ne "127.0.0.1" } |
    ForEach-Object {
        [PSCustomObject]@{
            Distant = "$($_.RemoteAddress):$($_.RemotePort)"
            Process = (Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).Name
        }
    }
```


> **⚠️ Heuristique volontairement simplifiée.** Ce filtre ne dit pas « connexion externe » mais « connexion hors du réseau `192.168.x.x` du lab ». D'autres plages **privées** (`10.0.0.0/8`, `172.16.0.0/12`) et l'IPv6 seraient classées à tort comme extérieures. En entreprise, compare aux **plages internes réellement utilisées** chez toi. C'est le principe général du triage : un filtre grossier sert à **réduire le bruit**, pas à produire un verdict — le tri fin reste humain.

### Les Alternate Data Streams (ADS)

NTFS permet de cacher des données dans des **flux alternatifs** attachés à un fichier — une technique de dissimulation classique :

```powershell
# Lister les flux alternatifs d'un fichier
Get-Item "C:\suspect.txt" -Stream * | Select-Object Stream, Length

# Lire un flux caché
Get-Content "C:\suspect.txt" -Stream "cache"
```


Un fichier anodin portant un flux `:` volumineux ou exécutable mérite attention.

## 🔴 Bonus

### Un script de triage synthétique

En pratique, on regroupe ces contrôles dans un script de triage qui produit un rapport horodaté — réutilisant fonctions (Ch.7), objets (Ch.6) et gestion d'erreurs (Ch.8) :

```powershell
function Invoke-QuickTriage {
    [CmdletBinding()]
    param([string]$OutputPath = "C:\triage")

    # Test avant d'agir : le dossier de sortie doit exister
    if (-not (Test-Path $OutputPath)) { New-Item -ItemType Directory -Path $OutputPath -Force | Out-Null }

    # Groupe Administrateurs ciblé par SID → portable FR/EN (rappel Ch.10)
    $grpAdmins = Get-LocalGroup | Where-Object SID -eq "S-1-5-32-544"

    $rapport = [ordered]@{
        Date            = Get-Date
        AdminsLocaux    = (Get-LocalGroupMember -Group $grpAdmins.Name -ErrorAction SilentlyContinue).Name
        TachesNonMs     = (Get-ScheduledTask | Where-Object TaskPath -notlike "\Microsoft\*").TaskName
        RunKeys         = (Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue)
        # Nom honnête : c'est "hors 192.168.x.x", pas "externe" au sens strict
        ConnexionsHorsLAN = (Get-NetTCPConnection -State Established |
            Where-Object RemoteAddress -notlike "192.168.*").RemoteAddress
    }
    $rapport | ConvertTo-Json -Depth 4 |
        Set-Content "$OutputPath\triage_$(Get-Date -Format yyyyMMdd_HHmmss).json" -Encoding UTF8
}
```


C'est un point de départ de triage, pas un outil forensic complet — mais il montre comment tes compétences d'admin se convertissent directement en capacité défensive.

## ❌ Erreur classique

```powershell
# Filtrer les logs côté client (très lent)
Get-WinEvent -LogName Security | Where-Object Id -eq 4625   # ❌
Get-WinEvent -FilterHashtable @{LogName='Security';Id=4625}  # ✅

# Conclure trop vite ("un service hors Windows = malware")
# → un binaire hors chemin standard est un SIGNAL à investiguer, pas une preuve
# → toujours corréler (hash, signature, date, contexte) avant de conclure

# Lire le journal Security sans droits admin
Get-WinEvent -LogName Security    # ❌ sans admin → accès refusé

# Chercher un champ de EventData par son nom, comme une propriété
$xml.Event.EventData.TargetUserName                                            # ❌ rien : le champ s'appelle Data
($xml.Event.EventData.Data | Where-Object Name -eq 'TargetUserName').'#text'  # ✅

# Oublier un crochet fermant dans une requête XPath
"*[System[EventID=4625]"     # ❌ 2 « [ » pour 1 « ] » → requête invalide
"*[System[EventID=4625]]"    # ✅ autant de « ] » que de « [ »

# Utiliser contains() dans un filtre XPath
# ❌ non pris en charge par les journaux Windows
# ✅ filtrer à la source sur l'ID et la période, puis Where-Object -match
```


## 💡 Exercices

**Guidé :** Compte les échecs de connexion (Event ID 4625) des dernières 24 h et affiche les comptes ayant plus de 5 échecs.

**Guidé (XML) :** Récupère ton dernier événement 4624 et affiche son XML brut avec `.ToXml()`. Repère les blocs `System` et `EventData`, puis affiche tous les champs avec `Format-Table Name, '#text'`. Enfin, extrais seul le `LogonType`.

**Autonome (XPath) :** Écris une requête XPath qui retrouve tes connexions **réussies** (4624) de type 2 (au clavier) ou 7 (déverrouillage). Construis-la d'abord dans l'Observateur d'événements, vérifie-la dans l'onglet XML, puis utilise-la avec `-FilterXPath`. Verrouille et déverrouille ta session (`Windows + L`) pour voir apparaître un nouvel événement.

**Autonome :** Écris `Get-PersistenceReport.ps1` qui collecte les clés Run (HKLM + HKCU), les tâches planifiées non-Microsoft et les services hors chemins standard, puis exporte le tout en JSON horodaté. Réutilise ce que tu sais des Ch.11-13.

## ✅ Tu sais maintenant...

- Lire et **filtrer efficacement** les Event Logs (`Get-WinEvent -FilterHashtable`)
- Lire la structure XML d'un événement (éléments, attributs, `System` / `EventData`) et en extraire un champ avec `[xml]`, `.ToXml()` et `.'#text'`
- Écrire une requête XPath (`*[System[…]]`, `Data[@Name='…']`, `and` / `or`) et choisir entre `-FilterHashtable`, `-FilterXPath` et `-FilterXml`
- Les Event IDs clés (4624/4625/4720/7045/1102…)
- Détecter une attaque par brute-force
- Vérifier intégrité (`Get-FileHash`) et signature (`Get-AuthenticodeSignature`)
- Trier la persistance (Run, tâches, services) — les **mêmes cmdlets qu'en admin, avec l'intention de détecter**
- Repérer connexions suspectes et flux alternatifs (ADS)

## 💬 Questions d'entretien typiques

- **Comment détecter une attaque par brute-force en PowerShell ?** → Filtrer les Event ID 4625 sur une période, regrouper par compte, alerter au-dessus d'un seuil.
- **Pourquoi `-FilterHashtable` plutôt que `Where-Object` sur les logs ?** → Le filtrage est appliqué à la source : indispensable sur des journaux volumineux.
- **Comment filtrer des événements sur la valeur d'un champ, par exemple le type de connexion ?** → Avec une requête XPath passée à `-FilterXPath` : `*[System[EventID=4624] and EventData[Data[@Name='LogonType']='10']]`. Le filtre reste appliqué à la source.
- **Où un malware cherche-t-il à persister ?** → Clés Run/RunOnce, tâches planifiées, services, dossiers de démarrage — tout ce qu'on sait déjà administrer.
- **Comment vérifier qu'un binaire système est légitime ?** → Sa signature (`Get-AuthenticodeSignature`, statut Valid + signataire attendu) et son hash (`Get-FileHash`) comparé à une référence.

---
