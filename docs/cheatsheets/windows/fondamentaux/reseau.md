---
title: "Réseau"
cours:
  - library/it/windows/powershell/index.md
  - library/it/windows/windows-en-profondeur/index.md
---

# Réseau

Voir ses adresses, routes, ports et connexions par processus ; tester la connectivité, un port et la résolution de noms ; voir les partages.

Les incontournables : `ipconfig /all` · `Get-NetIPConfiguration` · `Get-NetTCPConnection` · `netstat -ano` · `Test-NetConnection` · `Resolve-DnsName`
{ .kw-cs-top }

## Configuration

### Voir ses adresses IP, passerelle et DNS

```powershell title="Commande"
Get-NetIPConfiguration   # par interface : IPv4, passerelle, serveurs DNS
```

```powershell title="Exemple"
Get-NetIPConfiguration -InterfaceAlias Ethernet
```

??? example "Sortie"
    ```text
    InterfaceAlias       : Ethernet
    InterfaceIndex       : 12
    IPv4Address          : 192.168.1.50
    IPv4DefaultGateway   : 192.168.1.1
    DNSServer            : 192.168.1.10
                           192.168.1.11
    ```

```bat title="Exemple 2"
ipconfig /all   :: avec adresse MAC, DHCP, suffixe DNS
```

### Voir la table de routage

```powershell title="Commande"
Get-NetRoute -AddressFamily IPv4
```

```bat title="Exemple"
route print -4
```

??? example "Sortie"
    ```text
    Itinéraires actifs :
    Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
              0.0.0.0          0.0.0.0      192.168.1.1     192.168.1.50     25
          192.168.1.0    255.255.255.0         On-link      192.168.1.50    281
    ```

### Voir la table ARP

```bat title="Commande"
arp -a   :: correspondances IP ↔ MAC connues
```

```powershell title="Exemple"
Get-NetNeighbor -AddressFamily IPv4 -State Reachable
```

??? example "Sortie"
    ```text
    ifIndex IPAddress      LinkLayerAddress  State
    ------- ---------      ----------------  -----
    12      192.168.1.1    00-1A-2B-3C-4D-5E Reachable
    12      192.168.1.10   00-15-5D-01-0A-02 Reachable
    ```

## Connexions

### Voir quel processus écoute ou communique

```powershell title="Commande"
Get-NetTCPConnection -State Listen, Established |
    Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, OwningProcess,
        @{n='Processus';e={(Get-Process -Id $_.OwningProcess).ProcessName}}
```

```powershell title="Exemple"
Get-NetTCPConnection -State Established | Where-Object RemoteAddress -notlike '192.168.*' |
    Select-Object RemoteAddress, RemotePort, OwningProcess, @{n='Processus';e={(Get-Process -Id $_.OwningProcess).ProcessName}}
```

??? example "Sortie"
    ```text
    RemoteAddress  RemotePort OwningProcess Processus
    -------------  ---------- ------------- ---------
    13.107.42.14          443          4812 msedge
    203.0.113.15          443          7720 powershell
    ```

```bat title="Exemple 2"
netstat -ano | findstr ESTABLISHED   :: -o : PID
netstat -anob                        :: -b : nom du binaire (console administrateur)
```

Ensuite : [tout savoir sur un processus](processus.md#tout-savoir-sur-un-processus)
{ .kw-cs-meta }

### Voir les ports en écoute

```powershell title="Commande"
Get-NetTCPConnection -State Listen | Sort-Object LocalPort | Select-Object LocalAddress, LocalPort, OwningProcess
Get-NetUDPEndpoint | Sort-Object LocalPort | Select-Object LocalAddress, LocalPort, OwningProcess
```

```powershell title="Exemple"
Get-NetTCPConnection -State Listen | Where-Object LocalPort -in 135,445,3389,5985 | Select-Object LocalPort, OwningProcess
```

??? example "Sortie"
    ```text
    LocalPort OwningProcess
    --------- -------------
          135          1004
          445             4
         3389          1340
         5985             4
    ```

Le PID 4 (System) pour 445 et 5985 est normal : SMB et WinRM passent par le noyau (`http.sys`).

## Tester

### Tester qu'un port est ouvert

```powershell title="Commande"
Test-NetConnection <hôte> -Port <port>   # alias : tnc
```

```powershell title="Exemple"
Test-NetConnection srv-fs01.meridian.local -Port 445
```

??? example "Sortie"
    ```text
    ComputerName     : srv-fs01.meridian.local
    RemoteAddress    : 192.168.1.30
    RemotePort       : 445
    InterfaceAlias   : Ethernet
    SourceAddress    : 192.168.1.50
    TcpTestSucceeded : True
    ```

```bat title="Exemple 2"
ping -n 2 192.168.1.30
tracert -d 8.8.8.8   :: -d : sans résolution de noms
```

### Résoudre un nom

```powershell title="Commande"
Resolve-DnsName <nom> [-Type A|MX|SRV|TXT] [-Server <dns>]
```

```powershell title="Exemple"
Resolve-DnsName _ldap._tcp.dc._msdcs.meridian.local -Type SRV | Select-Object NameTarget, Port
```

??? example "Sortie"
    ```text
    NameTarget                 Port
    ----------                 ----
    dc01-lyo.meridian.local     389
    dc02-lyo.meridian.local     389
    ```

```bat title="Exemple 2"
nslookup intranet.meridian.local 192.168.1.10
```

### Voir et vider le cache DNS

```bat title="Commande"
ipconfig /displaydns   :: noms résolus récemment (volatil : à relever avant redémarrage)
ipconfig /flushdns     :: vider le cache
```

```powershell title="Exemple"
Get-DnsClientCache | Select-Object -First 3 Entry, Data
```

??? example "Sortie"
    ```text
    Entry                     Data
    -----                     ----
    intranet.meridian.local   192.168.1.20
    login.microsoftonline.com 20.190.151.7
    maj-logiciel.example.com  203.0.113.15
    ```

## Partages

### Voir les partages de la machine et ceux montés

```powershell title="Commande"
Get-SmbShare         # partages offerts par la machine
Get-SmbMapping       # lecteurs réseau montés
Get-SmbSession       # qui est connecté à mes partages (console administrateur)
```

```bat title="Exemple"
net share
```

??? example "Sortie"
    ```text
    Nom partage  Ressource                       Remarque
    -------------------------------------------------------------------------
    C$           C:\                             Partage par défaut
    IPC$                                         IPC distant
    ADMIN$       C:\Windows                      Administration à distance
    Compta       D:\Partages\Compta
    ```

```bat title="Exemple 2"
net use                          :: lecteurs réseau de la session
net view \\srv-fs01.meridian.local
```

Pour comprendre : [Windows en profondeur, ch. 15 (SMB)](../../../library/it/windows/windows-en-profondeur/index.md)
{ .kw-cs-meta }

### Voir qui a accès à un partage

```powershell title="Commande"
Get-SmbShareAccess -Name "<partage>"   # droits du partage (accès par le réseau)
icacls "<dossier partagé>"             # droits NTFS (accès au disque)
```

```powershell title="Exemple"
Get-SmbShareAccess -Name Compta
```

??? example "Sortie"
    ```text
    Name   ScopeName AccountName        AccessControlType AccessRight
    ----   --------- -----------        ----------------- -----------
    Compta *         Everyone           Allow             Read
    Compta *         MERIDIAN\GG-Compta Allow             Change
    ```

```bat title="Exemple 2"
icacls D:\Partages\Compta
```

Par le réseau, les deux s'appliquent et **le plus restrictif l'emporte** : partage en contrôle total et NTFS en lecture donnent une lecture seule. Les partages terminés par `$` (`C$`, `ADMIN$`) n'apparaissent pas dans la liste des partages mais restent accessibles aux administrateurs.

Pour comprendre : [Windows en profondeur, ch. 15 (permissions de partage et NTFS)](../../../library/it/windows/windows-en-profondeur/04-partie-iv-reseau-et-communication.md)
{ .kw-cs-meta }

### Voir le profil et l'état du pare-feu

```powershell title="Commande"
Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
Get-NetConnectionProfile   # profil réseau de chaque interface (Domain, Private, Public)
```

```powershell title="Exemple"
Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction
```

??? example "Sortie"
    ```text
    Name    Enabled DefaultInboundAction
    ----    ------- --------------------
    Domain     True                Block
    Private    True                Block
    Public     True                Block
    ```

Ensuite : [ouvrir un port dans le pare-feu](../administration/reseau.md#ouvrir-un-port-dans-le-pare-feu)
{ .kw-cs-meta }

## Vue d'ensemble

| Besoin | PowerShell | Équivalent Linux |
|---|---|---|
| Adresses, passerelle, DNS | `Get-NetIPConfiguration` | `ip -br a`, `ip route`, `resolvectl status` |
| Table de routage | `Get-NetRoute -AddressFamily IPv4` | `ip route` |
| Table ARP | `arp -a` | `ip neigh` |
| Ports en écoute | `Get-NetTCPConnection -State Listen` · `Get-NetUDPEndpoint` | `ss -tulpn` |
| Connexions et leur processus | `Get-NetTCPConnection` (`OwningProcess`) | `ss -tnp` |
| Tester un port | `Test-NetConnection <hôte> -Port <port>` | `nc -zv` |
| Résoudre un nom | `Resolve-DnsName <nom>` | `dig` |
| Cache DNS | `ipconfig /displaydns` · `/flushdns` | `resolvectl statistics` · `resolvectl flush-caches` |
| Partages offerts, montés, sessions | `Get-SmbShare` · `Get-SmbMapping` · `Get-SmbSession` | `smbclient -L`, `mount` |
| État du pare-feu | `Get-NetFirewallProfile` | `ufw status`, `nft list ruleset` |
