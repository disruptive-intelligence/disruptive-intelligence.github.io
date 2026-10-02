---
title: Chapitre 27 — DHCP Server
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie V — GPO et services Windows server
  - index.md
---

## 🟢 Le minimum à savoir

### À quoi sert le DHCP

Le **DHCP** (Dynamic Host Configuration Protocol) attribue automatiquement une configuration IP (adresse, masque, passerelle, DNS) aux machines qui se connectent au réseau. Sans lui, il faudrait configurer chaque poste à la main. Au Ch.15, on voyait le côté client (« l'interface est en DHCP ») ; ici, on administre le **serveur** qui distribue les adresses.

Le module : **DhcpServer** (`[🖥️ Server]`).

### Les concepts clés

| Terme | Ce que c'est |
|-------|-------------|
| **Scope (étendue)** | Une plage d'adresses distribuables (ex : `192.168.1.100` → `192.168.1.200`) |
| **Lease (bail)** | Une adresse attribuée à une machine pour une durée limitée |
| **Reservation** | Une adresse toujours attribuée à la même machine (via son adresse MAC) |
| **Option** | Un paramètre distribué avec l'adresse (passerelle = option 3, DNS = option 6…) |

### Lister les scopes et les baux

```powershell
Get-DhcpServerv4Scope                          # les étendues configurées

# Les baux actifs d'une étendue (qui a quelle IP ?)
Get-DhcpServerv4Lease -ScopeId 192.168.1.0
```


> **📌 Réflexe `Get-Member` :** `Get-DhcpServerv4Lease -ScopeId 192.168.1.0 | Get-Member` révèle `IPAddress`, `ClientId` (la MAC), `HostName`, `AddressState`, `LeaseExpiryTime`. C'est ainsi qu'on répond à « quelle machine a l'adresse .150 ? ».

### Les réservations `[🔑 Admin]`

Une **réservation** garantit qu'une machine (identifiée par sa MAC) reçoit toujours la même IP — indispensable pour les imprimantes, serveurs, équipements :

```powershell
# Réserver 192.168.1.150 pour une imprimante (via sa MAC)
Add-DhcpServerv4Reservation -ScopeId 192.168.1.0 `
    -IPAddress 192.168.1.150 `
    -ClientId "00-11-22-33-44-55" `
    -Description "Imprimante Compta"

# Lister les réservations
Get-DhcpServerv4Reservation -ScopeId 192.168.1.0
```


## 🟡 Très utile en pratique

### Diagnostiquer l'épuisement d'un scope

Un problème classique : « plus personne ne reçoit d'adresse ». Souvent, le scope est **épuisé** (toutes les adresses distribuées) :

```powershell
# Statistiques d'une étendue (taux d'utilisation)
Get-DhcpServerv4ScopeStatistics -ScopeId 192.168.1.0 |
    Select-Object ScopeId, Free, InUse, PercentageInUse
```


Un `PercentageInUse` proche de 100 % explique pourquoi les nouvelles machines n'obtiennent pas d'adresse.

### Auditer les baux actifs

```powershell
Get-DhcpServerv4Lease -ScopeId 192.168.1.0 |
    Where-Object AddressState -eq "Active" |
    Select-Object IPAddress, HostName, ClientId, LeaseExpiryTime |
    Sort-Object IPAddress
```


Utile pour repérer une machine inconnue sur le réseau (un `HostName` ou une MAC non identifiés = point d'attention sécurité).

## 🔴 Bonus

### Convertir un bail en réservation

Quand une machine a déjà un bail et qu'on veut fixer son adresse, on peut créer la réservation depuis son bail existant — pratique pour « figer » l'IP d'un serveur récemment déployé :

```powershell
$bail = Get-DhcpServerv4Lease -ScopeId 192.168.1.0 |
    Where-Object HostName -like "SRV-APP*"
Add-DhcpServerv4Reservation -ScopeId 192.168.1.0 `
    -IPAddress $bail.IPAddress -ClientId $bail.ClientId -Description "SRV-APP fixé"
```


## ❌ Erreur classique

```powershell
# Créer une réservation sans vérifier l'état de l'adresse
# → s'assurer qu'elle n'est pas déjà utilisée ou réservée à un AUTRE client
# ✅ regarder les baux actifs et les réservations existantes avant de réserver
#
# ⚠️ Idée fausse fréquente : une réservation DHCP n'a PAS besoin d'être exclue du scope.
#    La réservation lie l'adresse au client désigné : le serveur ne la distribuera pas
#    à quelqu'un d'autre. Les EXCLUSIONS servent surtout aux adresses configurées
#    STATIQUEMENT sur les machines (serveurs, imprimantes, équipements réseau),
#    que le DHCP ne doit jamais proposer.

# Confondre ClientId (MAC) et IPAddress dans une réservation
Add-DhcpServerv4Reservation -ClientId "192.168.1.150"   # ❌ le ClientId est la MAC
Add-DhcpServerv4Reservation -ClientId "00-11-22-33-44-55" -IPAddress "192.168.1.150"  # ✅

# Ignorer les statistiques quand "personne n'a d'IP"
# → vérifier PercentageInUse (scope peut-être épuisé)
```


## 💡 Exercices

**Guidé :** Affiche les statistiques d'utilisation de ton étendue DHCP et ses baux actifs (IP, nom d'hôte, expiration).

**Autonome :** Crée une réservation pour une machine fictive, vérifie-la, puis supprime-la (`Remove-DhcpServerv4Reservation`). Exporte la liste des baux actifs en CSV.

## ✅ Tu sais maintenant...

- Le rôle du DHCP (attribution IP automatique) — côté serveur
- Les concepts : scope, lease, reservation, option
- Lister scopes et baux, créer des réservations (`*-DhcpServerv4*`)
- Diagnostiquer un scope épuisé (`Get-DhcpServerv4ScopeStatistics`)

## 💬 Questions d'entretien typiques

- **Différence entre un bail et une réservation ?** → Un bail est temporaire et dynamique ; une réservation attribue toujours la même IP à une machine (via sa MAC).
- **Pourquoi une machine n'obtient-elle plus d'adresse ?** → Souvent un scope épuisé (`PercentageInUse` ~100 %), à vérifier via les statistiques.
- **Comment garantir une IP fixe à une imprimante sans la configurer en statique ?** → Une réservation DHCP basée sur sa MAC.

---
