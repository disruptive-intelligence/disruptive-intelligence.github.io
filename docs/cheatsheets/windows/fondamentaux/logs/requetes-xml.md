---
title: "Requêtes XML de l'Observateur"
---

# Requêtes XML de l'Observateur

Choisir entre *Filtrer*, *Rechercher* et une requête XML ; la structure d'une requête ; des gabarits à recopier (Event ID, période, champ, plusieurs champs, session, exclusion, journal exporté) ; la même requête en PowerShell.

Les incontournables : `Filter Current Log → XML` · `Edit query manually` · `System[EventID=…]` · `EventData[Data[@Name='…']='…']` · `Get-WinEvent -FilterXPath`
{ .kw-cs-top }

## Choisir son outil

### Savoir quand passer au XML

| Je cherche… | Outil | Pourquoi |
|---|---|---|
| Un ou plusieurs Event IDs, un niveau, une période, une source | *Filter Current Log…* → onglet **Filter** | Formulaire, sans syntaxe |
| Une valeur vue quelque part (un nom de fichier, une IP), une fois | *Find…* (`CTRL + F`) | Rapide, mais passe d'un événement à l'autre sans filtrer |
| Un **champ précis** (`TargetLogonId`, `Image`, `ImageLoaded`…), plusieurs conditions, plusieurs journaux | *Filter Current Log…* → onglet **XML** | Seul moyen de filtrer sur les champs d'`EventData` |
| La même chose en script, ou dans un `.evtx` exporté | `Get-WinEvent -FilterXPath` / `-FilterXml` | Reproductible, exportable |

Règle simple : dès que le critère est **dans l'onglet Details** de l'événement (pas dans les colonnes de la liste), il faut du XML.

Pour comprendre : [Requêtes XML personnalisées dans l'Observateur d'événements](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#requetes-xml-personnalisees)
{ .kw-cs-meta }

## Écrire une requête

### Ouvrir l'éditeur XML

1. Sélectionner le journal, puis *Filter Current Log…* (ou *Create Custom View…* pour garder la requête).
2. Onglet **XML** → cocher **Edit query manually** → confirmer.
3. Coller la requête, **OK**.

Une fois la requête éditée à la main, l'onglet *Filter* n'est plus utilisable pour ce filtre : garder sa requête dans un fichier texte. *Clear Filter* revient à la liste complète.

### Lire la structure d'une requête

```xml title="Gabarit"
<QueryList>
  <Query Id="0" Path="NOM_DU_JOURNAL">
    <Select Path="NOM_DU_JOURNAL">
      *[
        System[ CONDITIONS SUR L'EN-TÊTE ]
        and
        EventData[ CONDITIONS SUR LES CHAMPS ]
      ]
    </Select>
  </Query>
</QueryList>
```

| Élément | Rôle |
|---|---|
| `Path="Security"` | Le journal : `Security`, `System`, `Application`, `Microsoft-Windows-Sysmon/Operational`, `Microsoft-Windows-PowerShell/Operational`… |
| `System[…]` | L'en-tête commun à tous les événements : `EventID`, `TimeCreated`, `Level`, `Provider`, `Computer` |
| `EventData[Data[@Name='Champ']='valeur']` | Un champ propre à l'événement, avec son nom exact |
| `and` / `or` | Combiner des conditions (des parenthèses pour grouper) |

Trouver le nom exact d'un champ : ouvrir un événement → onglet **Details** → **XML View**. Chaque `<Data Name="…">` est un champ utilisable tel quel.

## Gabarits

### Un ou plusieurs Event IDs

```xml title="Gabarit"
*[System[(EventID=4624 or EventID=4625)]]
```

Seule la partie `*[…]` change d'une requête à l'autre : la placer dans le `<Select>` du gabarit ci-dessus.

### Une période

```xml title="Gabarit"
*[System[(EventID=4907)
  and TimeCreated[@SystemTime&gt;='2022-08-03T17:00:00.000Z'
              and @SystemTime&lt;='2022-08-03T17:30:00.999Z']]]
```

```xml title="Variante : les dernières 24 h"
*[System[TimeCreated[timediff(@SystemTime) &lt;= 86400000]]]
```

Les heures sont en **UTC** (le `Z`), alors que la liste affiche l'heure locale : en France, retirer 1 h (hiver) ou 2 h (été). `>` et `<` s'écrivent `&gt;` et `&lt;` dans le XML. `timediff` compte en millisecondes (86400000 = 24 h).

### Un champ égal à une valeur

```xml title="Gabarit"
*[System[EventID=4907]
  and EventData[Data[@Name='ObjectName']='C:\chemin\complet\du\fichier.dll']]
```

L'égalité est **exacte** : chemin complet, même orthographe. Copier la valeur depuis la vue XML d'un événement plutôt que la retaper.

### Deux champs à la fois

```xml title="Gabarit"
*[System[EventID=7]
  and EventData[Data[@Name='Image']='C:\Windows\System32\spoolsv.exe'
            and Data[@Name='ImageLoaded']='C:\Windows\Microsoft.NET\Framework64\v4.0.30319\clr.dll']]
```

Lecture : « les Sysmon 7 où ce processus charge cette DLL ». Avec `Path="Microsoft-Windows-Sysmon/Operational"`.

### Plusieurs valeurs pour un même champ

```xml title="Gabarit"
*[System[EventID=1]
  and EventData[(Data[@Name='Image']='C:\Windows\System32\cmd.exe'
              or Data[@Name='Image']='C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')]]
```

### Suivre une session par son Logon ID

```xml title="Gabarit"
*[EventData[Data[@Name='SubjectLogonId']='0x3e7' or Data[@Name='TargetLogonId']='0x3e7']]
```

Méthode : relever le `TargetLogonId` d'un **4624** (ouverture de session), puis chercher ce même identifiant dans les autres événements, où il apparaît en `SubjectLogonId` (actions faites par cette session : 4672, 4907, 4688…). `0x3e7` est le compte SYSTEM.

### Exclure du bruit

```xml title="Gabarit"
<QueryList>
  <Query Id="0" Path="Security">
    <Select Path="Security">*[System[EventID=4624]]</Select>
    <Suppress Path="Security">*[EventData[Data[@Name='TargetUserName']='SYSTEM']]</Suppress>
  </Query>
</QueryList>
```

`<Suppress>` retire de la sélection ce qui correspond : utile pour écarter les comptes système ou un processus légitime très bavard.

### Plusieurs journaux dans une même requête

```xml title="Gabarit"
<QueryList>
  <Query Id="0">
    <Select Path="Security">*[System[EventID=4688]]</Select>
    <Select Path="Microsoft-Windows-Sysmon/Operational">*[System[EventID=1]]</Select>
  </Query>
</QueryList>
```

### Un journal exporté (.evtx)

```xml title="Gabarit"
<QueryList>
  <Query Id="0" Path="file://C:\Cas\sysmon.evtx">
    <Select Path="file://C:\Cas\sysmon.evtx">*[System[EventID=3]]</Select>
  </Query>
</QueryList>
```

Ou plus simple : *Open Saved Log…*, puis le filtre XML habituel sur le journal ouvert.

## La même requête en PowerShell

### Filtrer avec -FilterXPath

```powershell title="Commande"
Get-WinEvent -LogName 'Security' -FilterXPath "*[System[EventID=4907] and EventData[Data[@Name='SubjectLogonId']='0x3e7']]"
Get-WinEvent -Path 'C:\Cas\sysmon.evtx' -FilterXPath "*[System[EventID=7]]"      # journal exporté
```

```powershell title="Exemple"
Get-WinEvent -LogName 'Security' -FilterXPath "*[System[EventID=4907]]" |
    ForEach-Object { ([xml]$_.ToXml()).Event.EventData.Data | Where-Object Name -eq 'ProcessName' | ForEach-Object '#text' } |
    Sort-Object -Unique
```

??? example "Sortie"
    ```text
    C:\Windows\System32\svchost.exe
    C:\Windows\WinSxS\amd64_microsoft-windows-servicingstack_…\TiWorker.exe
    ```

`-FilterXPath` prend la partie `*[…]` ; `-FilterXml` prend une requête `<QueryList>` complète (copiée de l'Observateur). Pour lire un champ, passer par le XML de l'événement (`[xml]$_.ToXml()`).

```powershell title="Exemple 2 — une requête de l'Observateur réutilisée telle quelle"
$q = @'
<QueryList><Query Id="0" Path="Security">
  <Select Path="Security">*[System[EventID=4907]]</Select>
</Query></QueryList>
'@
Get-WinEvent -FilterXml $q -MaxEvents 5 | Select-Object TimeCreated, Id
```

Pour comprendre : [Lire un journal Sysmon exporté](sysmon.md#lire-un-journal-sysmon-exporte) · [Filtrer par identifiant et par période](lire.md#filtrer-par-identifiant-et-par-periode)
{ .kw-cs-meta }

## Cas concrets

??? example "Cas concret : quel processus a modifié les paramètres d'audit, dans la session SYSTEM et une fenêtre de 30 minutes ?"
    ```xml
    <QueryList>
      <Query Id="0" Path="Security">
        <Select Path="Security">
          *[System[(EventID=4907)
                   and TimeCreated[@SystemTime&gt;='2022-08-03T17:00:00.000Z' and @SystemTime&lt;='2022-08-03T17:30:00.999Z']]
            and EventData[Data[@Name='SubjectLogonId']='0x3e7']]
        </Select>
      </Query>
    </QueryList>
    ```
    4624 → `TargetLogonId` → 4907 de la même session → champ `ProcessName`. [Lab 1 — Les bases des journaux d'événements Windows, question 1](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/14-lab-1-les-bases-des-journaux-d-evenements-windows.md#question-1-le-processus-qui-a-modifie-les-parametres-daudit)

??? example "Cas concret : ce processus a-t-il modifié l'audit d'un fichier précis ?"
    ```xml
    *[System[EventID=4907]
      and EventData[Data[@Name='ObjectName']='C:\Windows\Microsoft.NET\Framework64\v4.0.30319\WPF\wpfgfx_v0400.dll']]
    ```

    Requête complète, à coller dans *Filter Current Log…* → **XML** → *Edit query manually* :

    ```xml
    <QueryList>
      <Query Id="0" Path="Security">
        <Select Path="Security">
          *[System[EventID=4907]
            and EventData[Data[@Name='ObjectName']='C:\Windows\Microsoft.NET\Framework64\v4.0.30319\WPF\wpfgfx_v0400.dll']]
        </Select>
      </Query>
    </QueryList>
    ```

    Lire ensuite `ProcessName` et l'heure de l'événement.

??? example "Cas concret : quel processus charge une DLL donnée (Sysmon 7) ?"
    ```xml
    *[System[EventID=7]
      and EventData[Data[@Name='Image']='C:\Windows\System32\spoolsv.exe'
                and Data[@Name='ImageLoaded']='C:\Windows\Microsoft.NET\Framework64\v4.0.30319\clr.dll']]
    ```
    Requête complète, à coller dans *Filter Current Log…* → **XML** → *Edit query manually* :

    ```xml
    <QueryList>
      <Query Id="0" Path="Microsoft-Windows-Sysmon/Operational">
        <Select Path="Microsoft-Windows-Sysmon/Operational">
          *[System[EventID=7]
            and EventData[Data[@Name='Image']='C:\Windows\System32\spoolsv.exe'
                      and Data[@Name='ImageLoaded']='C:\Windows\Microsoft.NET\Framework64\v4.0.30319\clr.dll']]
        </Select>
      </Query>
    </QueryList>
    ```

    Un service natif qui charge le runtime .NET (`clr.dll`, `clrjit.dll`) est inhabituel : voir [la détection dans le cours](../../../../library/it/windows/sysmon-et-etw/01-detecter-avec-sysmon/03-reperer-du-powershell-non-manage.md#3-detection-n-2-powershell-non-manage-injection-c).

    Pour relever le SHA256 d'une DLL, ouvrir l'événement Sysmon 7 correspondant : `ImageLoaded` donne la DLL chargée, et `Hashes` contient sa valeur `SHA256=…`. Dans le lab `WININET.dll`, vérifier `ImageLoaded` avant de copier ce hash ; `Image` désigne le processus qui l'a chargée.

??? example "Cas concret : un exécutable charge-t-il le runtime .NET (Sysmon 7) ?"
    ```xml
    *[System[EventID=7]
      and EventData[Data[@Name='Image']='C:\chemin\vers\programme.exe'
                and (Data[@Name='ImageLoaded']='C:\Windows\System32\mscoree.dll'
                  or Data[@Name='ImageLoaded']='C:\Windows\Microsoft.NET\Framework64\v4.0.30319\clr.dll')]]
    ```
    Requête complète, à coller dans *Filter Current Log…* → **XML** → *Edit query manually* :

    ```xml
    <QueryList>
      <Query Id="0" Path="Microsoft-Windows-Sysmon/Operational">
        <Select Path="Microsoft-Windows-Sysmon/Operational">
          *[System[EventID=7]
            and EventData[Data[@Name='Image']='C:\chemin\vers\programme.exe'
                      and (Data[@Name='ImageLoaded']='C:\Windows\System32\mscoree.dll'
                        or Data[@Name='ImageLoaded']='C:\Windows\Microsoft.NET\Framework64\v4.0.30319\clr.dll')]]
        </Select>
      </Query>
    </QueryList>
    ```

    `mscoree.dll` puis `clr.dll` chargés par un programme signent l'exécution de code .NET. Pour un outil d'administration connu, c'est normal ; pour un exécutable inconnu, lancé depuis un dossier utilisateur, c'est une piste. Le détail des méthodes .NET appelées passe par ETW (voir [ETW et logman](etw.md)).

## Pièges

| Piège | Ce qui se passe | Parade |
|---|---|---|
| Valeur approximative | Aucun résultat : l'égalité est exacte | Copier la valeur depuis la vue XML |
| Joker ou « contient » (`*`, `contains()`) | Non pris en charge par les requêtes de l'Observateur | *Find…*, ou PowerShell : filtrer par ID puis `Where-Object Message -like '*mot*'` |
| Nom de champ mal écrit (`imageloaded`) | Aucun résultat | Respecter la casse des noms de la vue XML |
| `<` / `>` en clair | Requête refusée | `&lt;` / `&gt;` |
| Heure locale dans `@SystemTime` | Décalage d'1 à 2 h | Convertir en UTC (`Z`) |
| Champ dans `System` cherché dans `EventData` (ou l'inverse) | Aucun résultat | `EventID`, `TimeCreated`, `Level` : `System` ; le reste : `EventData` |
| Retour à l'onglet *Filter* après édition manuelle | Impossible | Garder ses requêtes dans un fichier texte |

## Vue d'ensemble

| Besoin | Gabarit |
|---|---|
| Un ou plusieurs Event IDs | `*[System[(EventID=A or EventID=B)]]` |
| Une période | `TimeCreated[@SystemTime&gt;='…Z' and @SystemTime&lt;='…Z']` |
| Les dernières 24 h | `TimeCreated[timediff(@SystemTime) &lt;= 86400000]` |
| Un champ | `EventData[Data[@Name='Champ']='valeur']` |
| Deux champs | `EventData[Data[@Name='A']='x' and Data[@Name='B']='y']` |
| Une session | `Data[@Name='SubjectLogonId']='0x…' or Data[@Name='TargetLogonId']='0x…'` |
| Exclure | `<Suppress Path="…">*[…]</Suppress>` |
| Plusieurs journaux | plusieurs `<Select Path="…">` dans la même `<Query>` |
| Journal exporté | `Path="file://C:\…\fichier.evtx"` |
| En PowerShell | `Get-WinEvent -FilterXPath "*[…]"` / `-FilterXml $requete` |
