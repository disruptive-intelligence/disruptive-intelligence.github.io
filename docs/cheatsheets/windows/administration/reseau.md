---
title: "Réseau et pare-feu"
cours:
  - library/it/windows/powershell/index.md
---

# Réseau et pare-feu

Changer d'adresse IP ou de DNS, ajouter un nom dans le fichier hosts, ouvrir ou fermer un port dans le pare-feu, désactiver les protocoles de résolution de secours, ouvrir une session de bureau à distance.

Les incontournables : `New-NetIPAddress` · `Set-DnsClientServerAddress` · `New-NetFirewallRule` · `netsh` · `mstsc`
{ .kw-cs-top }

## Adressage et noms

### Fixer une adresse IP

```powershell title="Commande"
New-NetIPAddress -InterfaceAlias <interface> -IPAddress <ip> -PrefixLength <masque> -DefaultGateway <passerelle>
```

```powershell title="Exemple"
New-NetIPAddress -InterfaceAlias Ethernet -IPAddress 192.168.1.60 -PrefixLength 24 -DefaultGateway 192.168.1.1
```

```bat title="Exemple 2"
netsh interface ipv4 set address name="Ethernet" static 192.168.1.60 255.255.255.0 192.168.1.1
```

Revenir en DHCP : `Set-NetIPInterface -InterfaceAlias Ethernet -Dhcp Enabled` puis `Remove-NetRoute` de la passerelle fixe.

### Changer de serveurs DNS

```powershell title="Commande"
Set-DnsClientServerAddress -InterfaceAlias <interface> -ServerAddresses <dns1>,<dns2>
```

```powershell title="Exemple"
Set-DnsClientServerAddress -InterfaceAlias Ethernet -ServerAddresses 192.168.1.10, 192.168.1.11
```

Revenir aux DNS du DHCP : `-ResetServerAddresses`.

### Ajouter un nom dans le fichier hosts

```powershell title="Commande"
Add-Content -Path C:\Windows\System32\drivers\etc\hosts -Value "<ip>`t<nom>"   # console administrateur
```

```powershell title="Exemple"
Add-Content -Path C:\Windows\System32\drivers\etc\hosts -Value "192.168.1.20`tintranet.meridian.local"
Clear-DnsClientCache
```

!!! warning "Attention"
    Le fichier hosts passe avant le DNS : une entrée inattendue est un classique de détournement. Le vérifier en investigation.

## Pare-feu

### Ouvrir un port dans le pare-feu

```powershell title="Commande"
New-NetFirewallRule -DisplayName "<nom>" -Direction Inbound -Protocol TCP -LocalPort <port> -RemoteAddress <source> -Action Allow
```

```powershell title="Exemple"
New-NetFirewallRule -DisplayName "WinRM depuis le réseau admin" -Direction Inbound -Protocol TCP -LocalPort 5985 -RemoteAddress 192.168.100.0/24 -Action Allow -Profile Domain
```

??? example "Sortie"
    ```text
    Name          : {6f3c…}
    DisplayName   : WinRM depuis le réseau admin
    Enabled       : True
    Direction     : Inbound
    Action        : Allow
    ```

```bat title="Exemple 2"
netsh advfirewall firewall add rule name="WinRM admin" dir=in action=allow protocol=TCP localport=5985 remoteip=192.168.100.0/24
```

Toujours restreindre la source (`-RemoteAddress`) : un port ouvert à tout le réseau facilite les déplacements latéraux.

### Lister et supprimer des règles

```powershell title="Commande"
Get-NetFirewallRule -Enabled True -Direction Inbound | Where-Object Action -eq Allow
Remove-NetFirewallRule -DisplayName "<nom>"
```

```powershell title="Exemple"
Get-NetFirewallRule -DisplayName "*admin*" | Get-NetFirewallPortFilter | Select-Object Protocol, LocalPort
```

### Bloquer une adresse

```powershell title="Commande"
New-NetFirewallRule -DisplayName "<nom>" -Direction Outbound -RemoteAddress <ip> -Action Block
```

```powershell title="Exemple"
New-NetFirewallRule -DisplayName "Blocage C2 incident 2026-10" -Direction Outbound -RemoteAddress 203.0.113.15 -Action Block
```

En parc, le blocage se fait sur le pare-feu périmétrique ou le proxy ; la règle locale sert de mesure immédiate sur un poste isolé.

## Durcissement

### Désactiver LLMNR et NetBIOS

```powershell title="Commande"
# LLMNR (équivalent de la GPO « Turn off multicast name resolution »)
New-Item 'HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient' -Force | Out-Null
Set-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient' -Name EnableMulticast -Value 0 -Type DWord
# NetBIOS sur TCP/IP, toutes interfaces (2 = désactivé)
Get-CimInstance Win32_NetworkAdapterConfiguration -Filter "IPEnabled=True" | Invoke-CimMethod -MethodName SetTcpipNetbios -Arguments @{TcpipNetbiosOptions=2}
```

En parc : GPO pour LLMNR, option DHCP pour NetBIOS.

Pour comprendre : [Windows en profondeur, ch. 16 (résolution de noms)](../../../library/it/windows/windows-en-profondeur/index.md)
{ .kw-cs-meta }

### Désactiver SMBv1 et exiger la signature SMB

```powershell title="Commande"
Get-SmbServerConfiguration | Select-Object EnableSMB1Protocol, RequireSecuritySignature
Set-SmbServerConfiguration -EnableSMB1Protocol $false -RequireSecuritySignature $true -Force
```

```powershell title="Exemple"
Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -NoRestart
```

## Bureau à distance

### Ouvrir une session de bureau à distance (RDP)

```bat title="Commande"
mstsc /v:<machine>
```

```bat title="Exemple"
mstsc /v:srv-fs01.meridian.local
```

```bash title="Exemple 2"
# Depuis Linux : fenêtre ajustable, presse-papiers partagé, dossier /tmp monté dans la session
xfreerdp /v:srv-fs01.meridian.local /u:'MERIDIAN\m.laurent' /dynamic-resolution +clipboard /drive:partage,/tmp
```

Sans `/p:`, xfreerdp demande le mot de passe : il ne reste pas dans l'historique du shell. Les ouvertures de session RDP laissent un événement 4624 de type 10 sur la machine cible.

Pour comprendre : [Analyse des journaux d'événements, RDP](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Action | PowerShell | `netsh` |
|---|---|---|
| Fixer une adresse IP | `New-NetIPAddress` | `netsh interface ip set address` |
| Changer de DNS | `Set-DnsClientServerAddress` | `netsh interface ip set dns` |
| Ouvrir un port | `New-NetFirewallRule -Direction Inbound -Action Allow` | `netsh advfirewall firewall add rule` |
| Lister les règles | `Get-NetFirewallRule` | `netsh advfirewall firewall show rule name=all` |
| Supprimer une règle | `Remove-NetFirewallRule` | `netsh advfirewall firewall delete rule name=<nom>` |

| Durcissement | Réglage | Valeur |
|---|---|---|
| LLMNR | `HKLM\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient\EnableMulticast` | `0` |
| NetBIOS sur TCP/IP | `TcpipNetbiosOptions` de chaque interface | `2` (désactivé) |
| SMBv1 | `Set-SmbServerConfiguration -EnableSMB1Protocol` | `$false` |
| Signature SMB | `Set-SmbServerConfiguration -RequireSecuritySignature` | `$true` |

Fichier hosts : `C:\Windows\System32\drivers\etc\hosts`.
