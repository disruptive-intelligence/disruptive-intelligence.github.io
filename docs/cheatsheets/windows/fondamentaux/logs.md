---
title: "Journaux et événements"
cours:
  - library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/index.md
  - library/it/windows/windows-en-profondeur/index.md
---

# Journaux et événements

Lire les journaux Windows, filtrer par identifiant et par période, retrouver les ouvertures de session, les processus lancés, les services et tâches créés, les scripts PowerShell ; exporter pour analyse.

Les incontournables : `Get-WinEvent -FilterHashtable` · `wevtutil` · `eventvwr.msc` · `auditpol /get` · `Get-WinEvent -Path`
{ .kw-cs-top }

## Lire

### Ouvrir un journal dans l'Observateur d'événements

```bat title="Commande"
eventvwr.msc   :: Observateur d'événements
```

| Je cherche… | Chemin dans l'Observateur |
|---|---|
| Ouvertures de session, comptes, privilèges | Journaux Windows → **Security** |
| Services, pilotes, démarrages | Journaux Windows → **System** |
| Connexions RDP reçues (1149, 261) | Journaux des applications et des services → Microsoft → Windows → **TerminalServices-RemoteConnectionManager** → Operational |
| Sessions RDP ouvertes, déconnectées, reconnectées (21, 24, 25) | … → **TerminalServices-LocalSessionManager** → Operational |
| Connexions RDP **émises** par ce poste (1102) | … → **TerminalServices-RDPClient** → Operational |
| Tâches planifiées (106, 140, 141, 200, 201) | … → **TaskScheduler** → Operational |
| Scripts PowerShell (4104) | … → **PowerShell** → Operational |
| Sysmon | … → **Sysmon** → Operational |

Clic droit sur le journal → **Filtrer le journal actuel** : Event ID (plusieurs séparés par des virgules, plages avec un tiret, exclusions précédées de `-`), source, période. L'onglet **Détails** d'un événement montre tous ses champs en XML.

!!! warning "Attention"
    « Effacer le filtre » réaffiche simplement tout le journal ; « Effacer le journal » le **vide** (et produit un 1102). Ne jamais confondre les deux en investigation.

Pour comprendre : [Event Viewer, filtres et détails d'un événement](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#event-viewer-observateur-devenements) · [Les journaux et leur emplacement](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/01-comprendre-les-journaux-windows.md#applications-and-services-logs)
{ .kw-cs-meta }

### Lister les journaux et leur taille

```powershell title="Commande"
Get-WinEvent -ListLog * | Where-Object RecordCount -gt 0 | Sort-Object RecordCount -Descending
```

```powershell title="Exemple"
Get-WinEvent -ListLog Security, System, 'Microsoft-Windows-PowerShell/Operational' |
    Select-Object LogName, RecordCount, @{n='Max (Mo)';e={$_.MaximumSizeInBytes/1MB}}
```

??? example "Sortie"
    ```text
    LogName                                 RecordCount Max (Mo)
    -------                                 ----------- --------
    Security                                     184211      128
    System                                        42177       20
    Microsoft-Windows-PowerShell/Operational      12955       15
    ```

### Lire les derniers événements d'un journal

```powershell title="Commande"
Get-WinEvent -LogName <journal> -MaxEvents <n>
```

```powershell title="Exemple"
Get-WinEvent -LogName System -MaxEvents 3 | Select-Object TimeCreated, Id, ProviderName, Message
```

??? example "Sortie"
    ```text
    TimeCreated          Id ProviderName                       Message
    -----------          -- ------------                       -------
    02/10/2026 09:44:10 7036 Service Control Manager           Le service Windows Update est entré dans l'état : en cours d'exécution.
    02/10/2026 09:30:02 7040 Service Control Manager           Le type de démarrage du service Background Intelligent Transfer Service…
    02/10/2026 08:01:55 6005 EventLog                          Le service Journal des événements a été démarré.
    ```

```bat title="Exemple 2"
wevtutil qe System /c:3 /rd:true /f:text   :: /c : nombre, /rd:true : du plus récent au plus ancien
```

### Filtrer par identifiant et par période

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='<journal>'; Id=<id1>,<id2>; StartTime=<date>; EndTime=<date>}
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddHours(-2)} |
    Measure-Object | Select-Object Count
```

??? example "Sortie"
    ```text
    Count
    -----
      214
    ```

`-FilterHashtable` filtre côté journal : beaucoup plus rapide qu'un `Where-Object` après coup.

Pour comprendre : [Filtrer avec Get-WinEvent (provider, ID, période)](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#get-winevent) · [Event Viewer, wevtutil ou Get-WinEvent](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#event-viewer-vs-wevtutil-vs-get-winevent)
{ .kw-cs-meta }

### Extraire les champs d'un événement

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='<journal>'; Id=<id>} | ForEach-Object {
    $x = [xml]$_.ToXml(); $d = @{}; $x.Event.EventData.Data | ForEach-Object { $d[$_.Name] = $_.'#text' }
    [pscustomobject]@{ Heure = $_.TimeCreated; Champ1 = $d['<NomDuChamp>'] } }
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddHours(-2)} | ForEach-Object {
    $x = [xml]$_.ToXml(); $d = @{}; $x.Event.EventData.Data | ForEach-Object { $d[$_.Name] = $_.'#text' }
    [pscustomobject]@{ Compte = $d['TargetUserName']; Source = $d['IpAddress'] } } |
    Group-Object Source | Sort-Object Count -Descending | Select-Object -First 3 Count, Name
```

??? example "Sortie"
    ```text
    Count Name
    ----- ----
      198 192.168.1.77
       12 192.168.1.15
        4 -
    ```

Ensuite : [retrouver les ouvertures de session](#retrouver-les-ouvertures-de-session)
{ .kw-cs-meta }

## Ouvertures de session

### Retrouver les ouvertures de session

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624}   # 4625 = échecs, 4634/4647 = fermetures
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624; StartTime=(Get-Date).AddDays(-1)} | ForEach-Object {
    $x = [xml]$_.ToXml(); $d = @{}; $x.Event.EventData.Data | ForEach-Object { $d[$_.Name] = $_.'#text' }
    [pscustomobject]@{ Heure=$_.TimeCreated; Compte=$d['TargetUserName']; Type=$d['LogonType']; Source=$d['IpAddress'] } } |
    Where-Object Type -in 3,10 | Select-Object -First 3
```

??? example "Sortie"
    ```text
    Heure                Compte     Type Source
    -----                ------     ---- ------
    02/10/2026 09:44:07  adm.martin 10   192.168.1.15
    02/10/2026 09:12:33  svc_backup 3    192.168.1.40
    02/10/2026 08:01:12  alice      3    192.168.1.10
    ```

| Logon Type | Signification |
|---|---|
| 2 | Interactif (console) |
| 3 | Réseau (partage SMB) |
| 4 / 5 | Tâche planifiée / service |
| 7 | Déverrouillage |
| 9 | Nouveaux identifiants (`runas /netonly`) |
| 10 | Bureau à distance (RDP) |
| 11 | Identifiants mis en cache |

Pour comprendre : [Analyse des journaux Windows, authentification et ouvertures de session](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/04-authentification-et-ouvertures-de-session.md)
{ .kw-cs-meta }

## Bureau à distance (RDP)

### Retrouver les connexions RDP reçues

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational'; Id=1149}   # authentification RDP réussie
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-TerminalServices-LocalSessionManager/Operational'; Id=21,24,25}   # session ouverte, déconnectée, reconnectée
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational'; Id=1149} -MaxEvents 3 | ForEach-Object {
    $u = ([xml]$_.ToXml()).Event.UserData.EventXML
    [pscustomobject]@{ Heure = $_.TimeCreated; Compte = "$($u.Param2)\$($u.Param1)"; Source = $u.Param3 } }
```

??? example "Sortie"
    ```text
    Heure                Compte               Source
    -----                ------               ------
    02/10/2026 09:44:05  MERIDIAN\adm.martin  192.168.1.15
    01/10/2026 17:02:41  MERIDIAN\adm.martin  192.168.1.15
    ```

Confirmer dans le journal Security : un **4624 avec Logon Type 10** (session interactive à distance) au même moment, pour le même compte et la même source.

Pour comprendre : [Logs côté machine cible RDP, Event ID 1149](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#event-id-1149)
{ .kw-cs-meta }

### Repérer les connexions RDP et les échecs d'authentification

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational'; Id=261}   # connexion TCP reçue sur l'écouteur RDP
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625}                                                                  # échecs d'ouverture : garder le Logon Type 10
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddHours(-24)} | ForEach-Object {
    $d = @{}; ([xml]$_.ToXml()).Event.EventData.Data | ForEach-Object { $d[$_.Name] = $_.'#text' }
    [pscustomobject]@{ Compte = $d['TargetUserName']; Type = $d['LogonType']; Source = $d['IpAddress'] } } |
    Where-Object Type -eq 10 | Group-Object Source | Select-Object Count, Name
```

??? example "Sortie"
    ```text
    Count Name
    ----- ----
       57 203.0.113.80
        2 192.168.1.15
    ```

Un **261 n'est pas un échec** : c'est une connexion TCP sur le port 3389, qui peut aussi venir d'un simple scan. Un 261 suivi d'un 1149 = authentification réussie ; un 261 sans 1149 fait **suspecter** un échec, que seul le **4625 Logon Type 10** confirme (compte, source, raison de l'échec).

Pour comprendre : [Event ID 261](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#event-id-261) · [Corrélation 261 + 1149](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#correlation-261-1149) · [Méthode fiable : 4625](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#methode-plus-fiable-event-id-4625)
{ .kw-cs-meta }

### Savoir vers quelles machines un poste s'est connecté en RDP

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-TerminalServices-RDPClient/Operational'; Id=1102}   # côté poste source : destination de la connexion
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-TerminalServices-RDPClient/Operational'; Id=1102} -MaxEvents 3 |
    Select-Object TimeCreated, Message
```

??? example "Sortie"
    ```text
    TimeCreated          Message
    -----------          -------
    02/10/2026 09:44:03  Le client a établi une connexion multitransport avec le serveur 192.168.1.30.
    ```

Sur un poste compromis, chaque destination devient une nouvelle piste. Attention : **le même numéro 1102 signifie « journal effacé » dans Security** — un Event ID ne se lit qu'avec son journal et son fournisseur. Les connexions sortantes laissent aussi un **4648** (identifiants explicites) dans le Security du poste source.

Pour comprendre : [Logs côté machine source RDP, Event ID 1102](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#event-id-1102-rdp-client) · [Corrélation RDP recommandée](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#correlation-rdp-recommandee)
{ .kw-cs-meta }

## Processus et scripts

### Retrouver les processus lancés

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4688}                                   # si l'audit est activé
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1}          # si Sysmon est installé
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1} -MaxEvents 200 |
    Where-Object Message -match 'ParentImage:.*WINWORD' | Select-Object -First 1 -ExpandProperty Message
```

??? example "Sortie"
    ```text
    Process Create:
    UtcTime: 2026-10-02 07:15:01.284
    Image: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
    CommandLine: "powershell.exe" -nop -w hidden -File C:\Users\alice\AppData\Local\Temp\maj.ps1
    User: MERIDIAN\alice
    ParentImage: C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE
    ```

!!! warning "Attention"
    Sans la GPO *Include command line in process creation events*, l'événement 4688 ne contient pas la ligne de commande.

### Retrouver les scripts PowerShell exécutés

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational'; Id=4104}   # Script Block Logging
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational'; Id=4104} -MaxEvents 50 |
    Where-Object Message -match 'DownloadString|FromBase64String|Invoke-Expression' |
    Select-Object -First 1 TimeCreated, @{n='Extrait';e={$_.Message.Substring(0,120)}}
```

??? example "Sortie"
    ```text
    TimeCreated          Extrait
    -----------          -------
    02/10/2026 09:15:03  Création du texte Scriptblock (1 sur 1) : $d = [System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String(…
    ```

## Services et tâches planifiées

### Retrouver les services installés ou modifiés

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Service Control Manager'; Id=7045,7040,7036}   # installé, démarrage modifié, état changé
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4697}                                                  # service installé (si l'audit est activé)
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='System'; Id=7045} -MaxEvents 2 | Select-Object TimeCreated, Message | Format-List
```

??? example "Sortie"
    ```text
    TimeCreated : 01/10/2026 23:12:40
    Message     : Un service a été installé sur le système.
                  Nom du service :  WindowsUpdateCritical
                  Nom du fichier du service :  C:\Users\alice\Documents\Windows Update.exe
                  Type de service :  service en mode utilisateur
                  Type de démarrage du service :  démarrage automatique
                  Compte du service :  LocalSystem
    ```

```powershell title="Exemple 2"
Get-WinEvent -FilterHashtable @{LogName='System'; Id=7040} -MaxEvents 5 | Select-Object TimeCreated, Message   # type de démarrage changé (ex. antivirus passé en « désactivé »)
```

| Event ID | Journal | Ce qu'il dit |
|---|---|---|
| **7045** | System (Service Control Manager) | Service installé : nom, binaire, type de démarrage, compte |
| **4697** | Security | Même information, si l'audit est activé : complète le 7045 |
| **7040** | System | Type de démarrage modifié (manuel → automatique : persistance ; automatique → désactivé : antivirus ou EDR neutralisé) |
| **7036** | System | Service démarré ou arrêté |

À regarder dans un 7045 : un **nom qui imite Windows** + un **binaire dans un dossier inscriptible par l'utilisateur** (`Documents`, `%TEMP%`, `%APPDATA%`, `C:\Users\Public`) + un **démarrage automatique** + le compte **LocalSystem** = investigation prioritaire. Le champ « type de service » dit comment le service s'exécute, pas qui l'a installé.

Pour comprendre : [Services Windows : 7045, binaire, compte, 7040, 7036](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/07-services-windows.md) · [Corrélation 7045 → 4688 → 7036 → C2](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/07-services-windows.md#correlation-recommandee-services) — Ensuite : [voir le binaire, le compte et le mode de démarrage d'un service](processus.md#voir-le-binaire-le-compte-et-le-mode-de-demarrage-dun-service)
{ .kw-cs-meta }

### Retracer la vie d'une tâche planifiée

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4698,4699,4700,4701,4702}   # créée, supprimée, activée, désactivée, modifiée (audit requis)
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-TaskScheduler/Operational'; Id=106,140,141,200,201}   # enregistrée, modifiée, supprimée, action lancée, terminée
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-TaskScheduler/Operational'; Id=106,140,141,200,201} -MaxEvents 5 |
    Select-Object TimeCreated, Id, @{n='Message';e={($_.Message -split "`r?`n")[0]}}
```

??? example "Sortie"
    ```text
    TimeCreated          Id Message
    -----------          -- -------
    02/10/2026 15:47:02 141 L'utilisateur « MERIDIAN\alice » a supprimé la tâche « \Windows Update Task ».
    02/10/2026 12:03:10 140 L'utilisateur « MERIDIAN\alice » a mis à jour la tâche « \Windows Update Task ».
    02/10/2026 10:15:04 201 Le Planificateur de tâches a terminé l'action « powershell.exe » de la tâche « \Windows Update Task ».
    02/10/2026 10:15:01 200 Le Planificateur de tâches a lancé l'action « powershell.exe » de la tâche « \Windows Update Task ».
    02/10/2026 10:14:22 106 L'utilisateur « MERIDIAN\alice » a inscrit la tâche « \Windows Update Task ».
    ```

Une tâche supprimée a disparu du système, pas des journaux. Le 4698 donne l'auteur, le déclencheur, le compte et la commande ; 200/201 prouvent que l'action a réellement tourné ; comparer 4698 et 4702 montre ce qui a été modifié.

Pour comprendre : [Journaux des tâches planifiées : 4698, 106, 200/201, 4702, 4699 et chronologie d'une tâche malveillante](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/06-taches-planifiees.md) — Voir aussi : [lister les tâches et ce qu'elles lancent](../administration/taches.md#lister-les-taches-et-ce-quelles-lancent)
{ .kw-cs-meta }

## Effacement des traces

### Repérer un effacement de journal

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=1102}   # journal de sécurité effacé
Get-WinEvent -FilterHashtable @{LogName='System'; Id=104}      # autre journal effacé
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

Pour comprendre : [Effacer un filtre ou effacer un journal](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#effacer-un-filtre-vs-effacer-un-journal)
{ .kw-cs-meta }

## Exporter et configurer

### Exporter un journal pour l'analyser ailleurs

```bat title="Commande"
wevtutil epl <journal> <fichier.evtx>   :: copie cohérente, même si le journal est ouvert
```

```bat title="Exemple"
wevtutil epl Security E:\collecte\PC-COMPTA-07_Security.evtx
```

```powershell title="Exemple 2"
Get-WinEvent -Path E:\collecte\PC-COMPTA-07_Security.evtx -FilterXPath "*[System[EventID=4624]]" -MaxEvents 5   # relire un .evtx exporté
```

Pour comprendre : [Export des événements et wevtutil](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#export-des-evenements)
{ .kw-cs-meta }

### Voir la politique d'audit active

```bat title="Commande"
auditpol /get /category:*   :: console administrateur
```

```bat title="Exemple"
auditpol /get /subcategory:"Création du processus","Ouvrir la session"
```

??? example "Sortie"
    ```text
    Catégorie/Sous-catégorie                  Paramètre
    Suivi détaillé
      Création du processus                   Succès
    Ouverture/Fermeture de session
      Ouvrir la session                       Succès et échec
    ```

### Agrandir un journal

```bat title="Commande"
wevtutil sl <journal> /ms:<octets>   :: taille maximale
```

```bat title="Exemple"
wevtutil sl Security /ms:1073741824   :: 1 Go
```

!!! warning "Attention"
    En parc, régler la taille et l'audit par GPO plutôt que machine par machine, et centraliser vers le SIEM.

## Repères : quel événement pour quoi

| Event ID | Journal | Signification |
|---|---|---|
| 4624 / 4625 | Security | Ouverture de session réussie / échouée |
| 4648 | Security | Ouverture avec identifiants explicites |
| 4672 | Security | Session avec privilèges spéciaux (admin) |
| 4688 | Security | Processus créé |
| 7045 / 4697 | System / Security | Service installé (7040 : démarrage modifié ; 7036 : démarré / arrêté) |
| 4698 / 4702 / 4699 | Security | Tâche planifiée créée / modifiée / supprimée (4700 / 4701 : activée / désactivée) |
| 4720 / 4732 | Security | Compte créé / ajouté à un groupe local |
| 4740 | Security | Compte verrouillé |
| 4768 / 4769 / 4771 / 4776 | Security (DC) | Kerberos TGT / ticket de service / échec de pré-auth / validation NTLM |
| 1102 / 104 | Security / System | Journal effacé |
| 4104 | PowerShell/Operational | Bloc de script exécuté |
| 1, 3, 11, 13, 22 | Sysmon | Processus, réseau, fichier, registre, DNS |
| 1149 / 261 | TerminalServices-RemoteConnectionManager | Authentification RDP réussie / connexion TCP reçue sur l'écouteur RDP |
| 21 / 24 / 25 | TerminalServices-LocalSessionManager | Session RDP ouverte / déconnectée / reconnectée |
| 1102 | TerminalServices-RDPClient | Connexion RDP **émise** par le poste (≠ 1102 de Security) |
| 106 / 140 / 141 / 200 / 201 | TaskScheduler/Operational | Tâche enregistrée / modifiée / supprimée / action lancée / terminée |

Pour la méthode complète (approche SOC, corrélations, brute force, password spray, RDP), voir le cours [Analyse des journaux d'événements Windows](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/index.md).
{ .kw-cs-meta }
