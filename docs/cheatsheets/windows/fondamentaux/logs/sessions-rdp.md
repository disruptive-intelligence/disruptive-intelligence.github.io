---
title: "Ouvertures de session et RDP"
---

# Ouvertures de session et RDP

Qui s'est connecté, comment (Logon Type), et les connexions RDP reçues, échouées ou émises.

Les incontournables : `4624` · `4625` · `1149` · `261` · `21 / 24 / 25` · `RDPClient 1102`
{ .kw-cs-top }

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

Pour comprendre : [Analyse des journaux Windows, authentification et ouvertures de session](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/04-authentification-et-ouvertures-de-session.md)
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

Pour comprendre : [Logs côté machine cible RDP, Event ID 1149](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#event-id-1149)
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

Pour comprendre : [Event ID 261](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#event-id-261) · [Corrélation 261 + 1149](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#correlation-261-1149) · [Méthode fiable : 4625](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#methode-plus-fiable-event-id-4625)
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

Pour comprendre : [Logs côté machine source RDP, Event ID 1102](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#event-id-1102-rdp-client) · [Corrélation RDP recommandée](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#correlation-rdp-recommandee)
{ .kw-cs-meta }
