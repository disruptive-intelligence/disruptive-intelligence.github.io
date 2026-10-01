---
title: Chapitre 15 — Interfaces et configuration IP
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie III — Administration réseau Windows
  - index.md
---

## 🟢 Le minimum à savoir

### Voir la configuration réseau

La cmdlet à connaître en premier, qui remplace `ipconfig` :

```powershell
Get-NetIPConfiguration          # vue synthétique : interface, IP, passerelle, DNS
```


Pour aller dans le détail, trois cmdlets par couche :

```powershell
Get-NetAdapter                  # les cartes réseau (physiques/virtuelles) et leur état
Get-NetIPAddress                # les adresses IP configurées
Get-NetIPInterface              # les propriétés d'interface (DHCP on/off, métrique...)
```


> **📌 Réflexe `Get-Member` :** `Get-NetAdapter | Get-Member` révèle `Name`, `Status` (`Up`/`Disconnected`), `MacAddress`, `LinkSpeed`, `InterfaceIndex`. L'`InterfaceIndex` est la clé qui relie les cartes, adresses et routes entre elles.

### Lire l'adresse IPv4 d'une interface

```powershell
Get-NetIPAddress -AddressFamily IPv4 |
    Where-Object { $_.IPAddress -ne "127.0.0.1" } |
    Select-Object InterfaceAlias, IPAddress, PrefixLength
```


Le `PrefixLength` est le masque en notation CIDR : `/24` = `255.255.255.0`.

### Les cartes réseau et leur état

```powershell
Get-NetAdapter | Select-Object Name, Status, LinkSpeed, MacAddress

# Activer / désactiver une carte                          [🔑 Admin]
Disable-NetAdapter -Name "Ethernet" -Confirm:$false
Enable-NetAdapter  -Name "Ethernet"
```


### Configurer une IP statique `[🔑 Admin]`

**Discipline `Get` avant `Set`/`New`** : on lit la config actuelle avant de la changer.

```powershell
# 1. Regarder l'existant
Get-NetIPConfiguration -InterfaceAlias "Ethernet"

# 2. Supprimer l'ancienne IP si besoin, puis en créer une nouvelle
New-NetIPAddress -InterfaceAlias "Ethernet" `
    -IPAddress 192.168.1.50 -PrefixLength 24 -DefaultGateway 192.168.1.1

# (pour repasser en DHCP)
Set-NetIPInterface -InterfaceAlias "Ethernet" -Dhcp Enabled
```


> **⚠️ Attention en session distante :** changer l'IP d'une interface par laquelle tu es **connecté à distance** peut te couper l'accès à la machine. C'est un piège classique. Sur un serveur distant, on planifie ce genre de changement avec précaution (console physique/hors-bande disponible).

### DHCP vs statique

- **DHCP** : l'adresse est attribuée automatiquement par un serveur DHCP (Ch.27). C'est le cas des postes clients.
- **Statique** : l'adresse est fixée manuellement. C'est le cas des serveurs, imprimantes, équipements réseau.

```powershell
# L'interface est-elle en DHCP ?
Get-NetIPInterface -InterfaceAlias "Ethernet" -AddressFamily IPv4 |
    Select-Object InterfaceAlias, Dhcp
```


## 🟡 Très utile en pratique

### Une fiche réseau complète

```powershell
Get-NetIPConfiguration | ForEach-Object {
    [PSCustomObject]@{
        Interface = $_.InterfaceAlias
        Statut    = $_.NetAdapter.Status
        IPv4      = $_.IPv4Address.IPAddress
        Passerelle = $_.IPv4DefaultGateway.NextHop
        DNS       = ($_.DNSServer | Where-Object AddressFamily -eq 2).ServerAddresses -join ", "
    }
}
```


Ce PSCustomObject réunit interface, IP, passerelle et DNS — exactement ce qu'un admin veut voir d'un coup d'œil. On l'intègre au diagnostic réseau (mini-projet Ch.18).

## 🔴 Bonus

### Renommer une interface

```powershell
Rename-NetAdapter -Name "Ethernet 2" -NewName "LAN-Serveur"    # [🔑 Admin]
```


Nommer clairement ses interfaces (`LAN`, `DMZ`, `Backup`) facilite l'administration sur les serveurs multi-cartes.

## ❌ Erreur classique

```powershell
# Changer l'IP de l'interface qui te connecte à distance
New-NetIPAddress ...    # ❌ risque de te déconnecter du serveur

# Oublier -AddressFamily et mélanger IPv4/IPv6
Get-NetIPAddress | Select IPAddress    # ⚠️ mélange v4 et v6
Get-NetIPAddress -AddressFamily IPv4   # ✅

# Créer une IP sans supprimer l'ancienne → conflit / double IP
# Vérifier avec Get-NetIPAddress avant, retirer avec Remove-NetIPAddress si besoin
```


## 💡 Exercices

**Guidé :** Affiche, pour chaque interface active (`Status -eq "Up"`), son nom, son IPv4 et son débit (`LinkSpeed`).

**Autonome :** Écris un script qui produit la « fiche réseau » (PSCustomObject : Interface, IPv4, Passerelle, DNS) pour toutes les interfaces connectées, et l'exporte en CSV.

## ✅ Tu sais maintenant...

- `Get-NetIPConfiguration` (remplace `ipconfig`) et les cmdlets par couche (`Get-NetAdapter`, `Get-NetIPAddress`, `Get-NetIPInterface`)
- Lire IP, masque (PrefixLength), passerelle
- Configurer une IP statique ou repasser en DHCP — avec la prudence en session distante
- Construire une fiche réseau exploitable

## 💬 Questions d'entretien typiques

- **Quelle cmdlet remplace `ipconfig` ?** → `Get-NetIPConfiguration` (vue synthétique) ; `Get-NetIPAddress` pour le détail des adresses.
- **DHCP ou statique pour un serveur ?** → Statique en général, pour une adresse stable et prévisible.
- **Quel risque à reconfigurer l'IP à distance ?** → Se couper soi-même l'accès à la machine si on modifie l'interface de connexion.

---
