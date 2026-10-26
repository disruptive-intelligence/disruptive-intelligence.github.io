---
title: "Réseau et accès distant"
cours:
  - library/it/windows/windows-en-profondeur/index.md
---

# Réseau et accès distant

N'exposer que le nécessaire : pare-feu actif sur les trois profils, peu de règles entrantes et restreintes à leur source, protocoles de résolution de secours et SMBv1 coupés, signature SMB, partages contrôlés, bureau à distance et WinRM fermés ou bornés.

Les incontournables : `Get-NetFirewallProfile` · `Set-NetFirewallProfile` · `Get-NetFirewallRule` · `Get-SmbServerConfiguration` · `Get-SmbShareAccess` · `fDenyTSConnections`
{ .kw-cs-top }

Un pare-feu local bien réglé freine fortement les déplacements latéraux : le poste n'a pas à accepter SMB, RDP ou WinRM de tous les autres postes.

## Pare-feu

### Activer le pare-feu sur les trois profils

| Profil | Appliqué quand… |
|---|---|
| Domaine | La machine joint un contrôleur de son domaine |
| Privé | Réseau marqué de confiance |
| Public | Tout autre réseau (le plus restrictif) |

```powershell title="Vérifier"
Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
Get-NetFirewallProfile | Where-Object Enabled -eq $false   # rien en retour : les trois profils sont actifs
```

```powershell title="Appliquer"
Set-NetFirewallProfile -Profile Domain,Private,Public -Enabled True -DefaultInboundAction Block
```

En parc : *Paramètres de sécurité → Pare-feu Windows Defender avec fonctions avancées de sécurité* dans une GPO (ou Intune), pour qu'un utilisateur ou un attaquant ne le coupe pas durablement.

Ensuite : [voir le profil et l'état du pare-feu](../fondamentaux/reseau.md#voir-le-profil-et-letat-du-pare-feu) — Pour comprendre : [Windows en profondeur, ch. 14.2 (le pare-feu)](../../../library/it/windows/windows-en-profondeur/04-partie-iv-reseau-et-communication.md#142-le-pare-feu-windows) · [PowerShell, ch. 18](../../../library/it/windows/powershell/03-partie-iii-administration-reseau-windows/04-chapitre-18-pare-feu-windows.md) — Ajout hors cours : `Set-NetFirewallProfile`
{ .kw-cs-meta }

### Réduire les règles entrantes au strict nécessaire

Chaque règle `Allow` entrante est une porte. Lister ce qui est ouvert, supprimer l'inutile, restreindre le reste au profil et à la plage d'adresses qui en ont besoin (réseau d'administration, serveur de supervision). Sur les serveurs, filtrer aussi la sortie.

```powershell title="Vérifier"
Get-NetFirewallRule -Direction Inbound -Action Allow -Enabled True | ForEach-Object {
    [PSCustomObject]@{
        Regle  = $_.DisplayName
        Profil = $_.Profile
        Port   = ($_ | Get-NetFirewallPortFilter).LocalPort
        Source = ($_ | Get-NetFirewallAddressFilter).RemoteAddress
    }
} | Sort-Object Port
```

```powershell title="Exemple — restreindre une règle existante à sa source"
Set-NetFirewallRule -DisplayName "<règle>" -RemoteAddress 192.168.100.0/24 -Profile Domain
```

`Source = Any` sur RDP (3389), SMB (445), WinRM (5985/5986) : à restreindre. Ne pas couper la règle dont dépend sa propre session à distance.

Ensuite : [ouvrir un port en restreignant la source](../administration/reseau.md#ouvrir-un-port-dans-le-pare-feu) · [lister et supprimer des règles](../administration/reseau.md#lister-et-supprimer-des-regles) — Pour comprendre : [PowerShell, ch. 18 (auditer les règles entrantes)](../../../library/it/windows/powershell/03-partie-iii-administration-reseau-windows/04-chapitre-18-pare-feu-windows.md) — Ajout hors cours : la colonne `Source` (`Get-NetFirewallAddressFilter`)
{ .kw-cs-meta }

### Journaliser les connexions refusées par le pare-feu

Sans journalisation, `pfirewall.log` reste vide : on ne voit ni les balayages, ni les tentatives refusées.

```powershell title="Appliquer"
Set-NetFirewallProfile -All -LogBlocked True -LogMaxSizeKilobytes 16384
```

```powershell title="Vérifier"
Get-NetFirewallProfile | Select-Object Name, LogBlocked, LogAllowed, LogFileName, LogMaxSizeKilobytes
```

Fichier : `%SystemRoot%\System32\LogFiles\Firewall\pfirewall.log` (`DROP` / `ALLOW`). Les changements de règles se lisent dans *Journaux des applications et des services → Microsoft → Windows → Windows Firewall With Advanced Security → Firewall* (2004 ajout, 2005 modification, 2003 réglage changé).

Ensuite : [retracer les changements du pare-feu](../fondamentaux/logs/pare-feu-defender.md#retracer-les-changements-du-pare-feu) — Pour comprendre : [Analyse des journaux, pare-feu Windows](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/10-pare-feu-windows.md) — Ajout hors cours : la commande d'activation
{ .kw-cs-meta }

## Protocoles à risque

Quand le DNS échoue, Windows interroge tout le segment (LLMNR, NBT-NS, mDNS) : n'importe quelle machine peut répondre, et la victime tente de s'authentifier auprès d'elle. Ces mécanismes n'apportent presque rien en entreprise.

![[cheatsheets/windows/administration/reseau#Désactiver LLMNR et NetBIOS]]

### Couper aussi mDNS et WPAD s'ils ne servent pas

mDNS (UDP 5353) présente le même risque que LLMNR sur les postes ; WPAD (découverte automatique du proxy) permet à un faux serveur de se déclarer proxy.

```powershell title="Vérifier"
Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters -Name EnableMDNS -ErrorAction SilentlyContinue
```

```powershell title="Appliquer"
Set-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters -Name EnableMDNS -Value 0 -Type DWord
```

WPAD : déclarer explicitement le proxy par GPO (ou désactiver la détection automatique des paramètres), plutôt que de laisser le poste le chercher.

Pour comprendre : [Windows en profondeur, ch. 16.2 (les protocoles de secours)](../../../library/it/windows/windows-en-profondeur/04-partie-iv-reseau-et-communication.md#162-les-protocoles-de-secours) — Ajout hors cours : la valeur `EnableMDNS`
{ .kw-cs-meta }

![[cheatsheets/windows/administration/reseau#Désactiver SMBv1 et exiger la signature SMB]]

Côté client aussi : `Set-SmbClientConfiguration -RequireSecuritySignature $true -Force` (*Client réseau Microsoft : communications signées numériquement (toujours)*). La signature empêche de rejouer une authentification NTLM vers SMB ; tester d'abord les équipements anciens (copieurs, NAS). SMBv3 permet aussi de chiffrer un partage sensible (`EncryptData`).
{ .kw-cs-meta }

## Partages

### Fermer les partages inutiles et resserrer leurs droits

Un partage lisible par `Everyone` expose son contenu à tout le réseau ; les partages administratifs (`C$`, `ADMIN$`, `IPC$`) sont réservés aux administrateurs locaux, d'où l'importance de LAPS. Par le réseau, le plus restrictif des droits de partage et des droits NTFS l'emporte : partage large pour les utilisateurs authentifiés, finesse en NTFS.

```powershell title="Vérifier"
Get-SmbShare | Where-Object Name -notmatch '\$$' | ForEach-Object { Get-SmbShareAccess -Name $_.Name } |
    Select-Object Name, AccountName, AccessRight
```

```powershell title="Appliquer"
Revoke-SmbShareAccess -Name "<partage>" -AccountName Everyone -Force
Grant-SmbShareAccess -Name "<partage>" -AccountName "<groupe>" -AccessRight Change -Force
```

`Remove-SmbShare -Name "<partage>"` supprime un partage qui ne sert plus (les fichiers restent sur le disque).

Ensuite : [voir qui a accès à un partage](../fondamentaux/reseau.md#voir-qui-a-acces-a-un-partage) — Pour comprendre : [Windows en profondeur, ch. 15 (SMB, partages)](../../../library/it/windows/windows-en-profondeur/04-partie-iv-reseau-et-communication.md#152-permissions-de-partage-et-permissions-ntfs) · [PowerShell, ch. 28](../../../library/it/windows/powershell/05-partie-v-gpo-et-services-windows-server/04-chapitre-28-file-server-et-partages-smb.md) — Ajout hors cours : `Revoke-SmbShareAccess`, `Remove-SmbShare`
{ .kw-cs-meta }

## Accès distant

### Fermer le bureau à distance, ou le borner

Sur un poste, le bureau à distance est souvent inutile : le désactiver. S'il sert : authentification au niveau du réseau (NLA), groupe *Utilisateurs du Bureau à distance* réduit, port ouvert seulement depuis le réseau d'administration, MFA, Remote Credential Guard pour les administrateurs.

```powershell title="Vérifier"
Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections                 # 1 = RDP fermé
Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name UserAuthentication # 1 = NLA exigée
```

```powershell title="Appliquer — fermer"
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections -Value 1
```

```powershell title="Exemple — garder, mais avec NLA"
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name UserAuthentication -Value 1
```

GPO : *Composants Windows → Services Bureau à distance → Hôte de la session Bureau à distance → Connexions* (autoriser ou non) et *→ Sécurité → Requérir l'authentification utilisateur pour les connexions à distance à l'aide de l'authentification au niveau du réseau*.

Ensuite : [ne pas déposer ses identifiants en RDP](identifiants.md#ne-pas-laisser-ses-identifiants-sur-la-machine-administree-rdp) · [repérer les connexions RDP](../fondamentaux/logs/sessions-rdp.md#reperer-les-connexions-rdp-et-les-echecs-dauthentification) — Pour comprendre : [Sécurité système Windows, journaux RDP](../../../library/cyber/hardening/securite-systeme-windows/07-infrastructure-de-journalisation-windows.md#remote-desktop-rdp-logs) — Ajout hors cours : toute l'entrée (valeurs de registre et GPO)
{ .kw-cs-meta }

### Restreindre WinRM et PowerShell Remoting

En domaine, Kerberos authentifie et chiffre le contenu même sur le port HTTP 5985. Hors domaine : HTTPS (5986, avec certificat), pas `TrustedHosts = *`. Ouvrir WinRM seulement depuis le réseau d'administration, et déléguer des tâches précises par **JEA** (*Just Enough Administration*) plutôt que des droits d'administrateur complets.

```powershell title="Vérifier"
Get-Service WinRM | Select-Object Status, StartType
Get-Item WSMan:\localhost\Client\TrustedHosts
```

```powershell title="Appliquer — limiter TrustedHosts au nécessaire"
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "<machine>" -Force
```

`TrustedHosts` à `*` fait confiance à toutes les machines et contourne des protections : à remplacer par la liste nécessaire, ou par HTTPS.

Pour comprendre : [PowerShell, ch. 29 (WinRM, authentification et sécurité)](../../../library/it/windows/powershell/06-partie-vi-administration-distante-api-et-automatis/01-chapitre-29-powershell-remoting.md) · [ch. 35 (JEA)](../../../library/it/windows/powershell/08-partie-viii-powershell-pour-la-cybersecurite/02-chapitre-35-securite-de-l-execution-et-durcissemen.md#jea-just-enough-administration) — Ajout hors cours : la lecture de `TrustedHosts`
{ .kw-cs-meta }

### Vérifier ce qui écoute sur le poste

Chaque port en écoute doit correspondre à un besoin connu. `0.0.0.0` écoute sur toutes les interfaces (le pare-feu peut encore bloquer), `127.0.0.1` seulement en local.

```powershell title="Vérifier"
Get-NetTCPConnection -State Listen | Sort-Object LocalPort |
    Select-Object LocalAddress, LocalPort, OwningProcess, @{n='Processus';e={(Get-Process -Id $_.OwningProcess).ProcessName}}
```

Ensuite : [voir les ports en écoute](../fondamentaux/reseau.md#voir-les-ports-en-ecoute) · [identifier un port et son processus](../fondamentaux/enumeration.md#identifier-un-port-en-ecoute-et-son-processus) — Pour comprendre : [Élévation de privilèges, 127.0.0.1 vs 0.0.0.0](../../../library/it/windows/elevation-de-privileges-sous-windows-windows-privilege-escalation/03-enumeration-initiale.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Mesure | Vérifier | Attendu |
|---|---|---|
| Pare-feu | `Get-NetFirewallProfile` | `Enabled = True` sur les trois profils, entrant `Block` |
| Règles entrantes | `Get-NetFirewallRule -Direction Inbound -Action Allow` | Peu de règles, source restreinte |
| Journal du pare-feu | `Get-NetFirewallProfile` → `LogBlocked` | `True` |
| LLMNR | `…\Windows NT\DNSClient\EnableMulticast` | `0` |
| NetBIOS sur TCP/IP | `TcpipNetbiosOptions` | `2` |
| mDNS | `…\Dnscache\Parameters\EnableMDNS` | `0` s'il ne sert pas |
| WPAD | GPO proxy | Proxy déclaré |
| SMBv1 | `Get-SmbServerConfiguration` → `EnableSMB1Protocol` | `False` |
| Signature SMB | `RequireSecuritySignature` (serveur et client) | `True` |
| Partages | `Get-SmbShareAccess` | Pas d'`Everyone`, partages inutiles supprimés |
| Bureau à distance | `fDenyTSConnections` ; `UserAuthentication` | `1` (fermé) ; sinon NLA `1` et source restreinte |
| WinRM | `TrustedHosts` | Pas de `*` ; HTTPS hors domaine ; JEA |
| Ports en écoute | `Get-NetTCPConnection -State Listen` | Chacun justifié |

| Port | Service | Pourquoi le restreindre |
|---|---|---|
| 445/TCP | SMB | Partages, partages administratifs, déplacement latéral |
| 3389/TCP | RDP | Ouverture de session à distance |
| 5985 / 5986/TCP | WinRM (HTTP / HTTPS) | Exécution de commandes à distance |
| 135/TCP | RPC (WMI, DCOM) | Exécution à distance |
| 5355/UDP · 137/UDP · 5353/UDP | LLMNR · NBT-NS · mDNS | Résolution par diffusion, captation d'authentifications |
