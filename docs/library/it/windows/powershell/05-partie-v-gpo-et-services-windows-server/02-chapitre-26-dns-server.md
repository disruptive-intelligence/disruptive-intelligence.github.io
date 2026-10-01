---
title: Chapitre 26 — DNS Server
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie V — GPO et services Windows server
  - index.md
---

## 🟢 Le minimum à savoir

### Client vs serveur DNS

Au Ch.16, on configurait le DNS **côté client** (quels serveurs interroger, résoudre un nom). Ici, on administre le **serveur DNS** lui-même — celui qui héberge les enregistrements. Dans un domaine AD, le DNS est presque toujours installé sur les contrôleurs de domaine (AD en dépend fortement).

Le module : **DnsServer** (`[🖥️ Server]`, sur un serveur DNS ou via RSAT).

### Les zones

Une **zone** est une portion de l'espace de noms DNS que le serveur gère (ex : la zone `lab.local`). Deux grandes familles :

- **Zone de recherche directe** : nom → IP (le cas normal)
- **Zone de recherche inversée** : IP → nom (pour les requêtes PTR)

```powershell
Get-DnsServerZone                          # lister les zones
Get-DnsServerZone -Name "lab.local"        # une zone précise
```


### Les enregistrements

Une zone contient des **enregistrements** (records). Les types courants :

| Type | Rôle |
|------|------|
| **A** | Nom → adresse IPv4 |
| **AAAA** | Nom → adresse IPv6 |
| **CNAME** | Alias (un nom pointe vers un autre nom) |
| **PTR** | IP → nom (résolution inverse) |
| **MX** | Serveur de messagerie du domaine |
| **NS** | Serveur de noms de la zone |

```powershell
# Lister les enregistrements d'une zone
Get-DnsServerResourceRecord -ZoneName "lab.local"

# Filtrer par type
Get-DnsServerResourceRecord -ZoneName "lab.local" -RRType A
```


> **📌 Réflexe `Get-Member` :** `Get-DnsServerResourceRecord -ZoneName lab.local | Get-Member` révèle `HostName`, `RecordType`, `RecordData`, `TimeToLive`. La structure `RecordData` contient l'IP (pour un A) ou la cible (pour un CNAME).

### Créer et supprimer des enregistrements `[🔑 Admin]`

```powershell
# Ajouter un enregistrement A
Add-DnsServerResourceRecordA -ZoneName "lab.local" `
    -Name "srv-app" -IPv4Address "192.168.1.60"

# Ajouter un CNAME (alias)
Add-DnsServerResourceRecordCName -ZoneName "lab.local" `
    -Name "intranet" -HostNameAlias "srv-app.lab.local"

# Supprimer un enregistrement
Remove-DnsServerResourceRecord -ZoneName "lab.local" -Name "srv-app" -RRType A -Force
```


> **📌 `Get` avant d'agir :** avant d'ajouter un enregistrement `srv-app`, vérifie qu'il n'existe pas déjà (`Get-DnsServerResourceRecord -ZoneName lab.local -Name srv-app`). Un doublon d'enregistrement A crée des résolutions imprévisibles.

## 🟡 Très utile en pratique

### Vérifier la cohérence client/serveur

Le Ch.16 (client) et ce chapitre (serveur) se combinent pour diagnostiquer :

```powershell
# Côté serveur : l'enregistrement existe-t-il ?
Get-DnsServerResourceRecord -ZoneName "lab.local" -Name "srv-app"

# Côté client : la résolution fonctionne-t-elle ? (rappel Ch.16)
Resolve-DnsName "srv-app.lab.local" -Server 192.168.1.10
```


Si l'enregistrement existe côté serveur mais que le client ne résout pas : problème de cache client (`Clear-DnsClientCache`) ou de serveur DNS interrogé.

### Auditer les enregistrements d'une zone

```powershell
Get-DnsServerResourceRecord -ZoneName "lab.local" -RRType A |
    Select-Object HostName, @{N="IP";E={$_.RecordData.IPv4Address}} |
    Sort-Object HostName |
    Export-Csv "C:\rapports\dns_A_records.csv" -NoTypeInformation -Encoding UTF8
```


## 🔴 Bonus

### Zones intégrées à AD

Dans un domaine, les zones DNS sont souvent **intégrées à Active Directory** : elles sont répliquées automatiquement entre tous les DC (via la réplication AD) et sécurisées. C'est la configuration recommandée, mais sa mise en place relève d'un cours DNS/AD dédié.

## ❌ Erreur classique

```powershell
# Créer un doublon d'enregistrement A
Add-DnsServerResourceRecordA ...    # ❌ sans vérifier l'existant → résolution aléatoire
Get-DnsServerResourceRecord -ZoneName lab.local -Name srv-app   # ✅ vérifier d'abord

# Oublier de vider le cache client après un changement serveur (Ch.16)
Clear-DnsClientCache

# Confondre zone directe et inversée
# Un enregistrement PTR va dans la zone INVERSÉE, pas la directe
```


## 💡 Exercices

**Guidé :** Liste les zones du serveur DNS, puis affiche tous les enregistrements A de `lab.local` avec leur IP.

**Autonome :** Ajoute un enregistrement A `test-srv` pointant vers une IP, vérifie sa création côté serveur (`Get-DnsServerResourceRecord`) et côté client (`Resolve-DnsName`), puis supprime-le.

## ✅ Tu sais maintenant...

- La différence DNS client (Ch.16) / serveur (ici)
- Les zones (directe/inversée) et les types d'enregistrements (A, AAAA, CNAME, PTR, MX, NS)
- Lister, créer, supprimer des enregistrements (`*-DnsServerResourceRecord*`)
- Diagnostiquer en croisant serveur et client

## 💬 Questions d'entretien typiques

- **Différence entre un enregistrement A et un CNAME ?** → A pointe un nom vers une IP ; CNAME pointe un nom vers un autre nom (alias).
- **Où va un enregistrement PTR ?** → Dans une zone de recherche **inversée** (résolution IP → nom).
- **Pourquoi le DNS est-il critique en AD ?** → Active Directory repose sur le DNS pour localiser les contrôleurs de domaine et les services ; un DNS cassé casse l'authentification.

---
