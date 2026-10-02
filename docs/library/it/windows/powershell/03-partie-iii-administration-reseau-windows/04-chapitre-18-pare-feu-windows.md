---
title: Chapitre 18 — Pare-feu Windows
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie III — Administration réseau Windows
  - index.md
---

## 🟢 Le minimum à savoir

### Les profils de pare-feu

Le Pare-feu Windows Defender applique des règles selon un **profil** correspondant au type de réseau :

- **Domain** : la machine est connectée à son domaine AD
- **Private** : réseau privé de confiance (maison, bureau)
- **Public** : réseau non fiable (café, aéroport) — le plus restrictif

```powershell
Get-NetFirewallProfile |
    Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
```


> **Important :** un même poste applique le profil correspondant au réseau où il se trouve. Une règle peut être active sur `Private` mais pas sur `Public`.

### Lister les règles

```powershell
Get-NetFirewallRule | Where-Object Enabled -eq "True" |
    Select-Object DisplayName, Direction, Action, Profile -First 20

# Les règles entrantes qui autorisent quelque chose
Get-NetFirewallRule -Direction Inbound -Action Allow -Enabled True |
    Select-Object DisplayName, Profile
```


> **📌 Réflexe `Get-Member` :** une règle de pare-feu a beaucoup de propriétés (`DisplayName`, `Direction`, `Action`, `Profile`, `Enabled`). Le détail des ports/protocoles se lit via des cmdlets associées (`Get-NetFirewallPortFilter`), car une règle est liée à des filtres.

### Direction et action

- **Direction** : `Inbound` (trafic entrant) ou `Outbound` (sortant)
- **Action** : `Allow` (autoriser) ou `Block` (bloquer)

La logique par défaut d'un poste : **entrant bloqué** sauf exceptions, **sortant autorisé**.

### Créer une règle `[🔑 Admin]`

```powershell
# Autoriser le port TCP 8080 en entrée, sur les profils Domain et Private
New-NetFirewallRule -DisplayName "App interne 8080" `
    -Direction Inbound -Action Allow `
    -Protocol TCP -LocalPort 8080 `
    -Profile Domain,Private
```


### Modifier et supprimer `[🔑 Admin]`

```powershell
Set-NetFirewallRule -DisplayName "App interne 8080" -Enabled False   # désactiver
Remove-NetFirewallRule -DisplayName "App interne 8080"               # supprimer
```


> **⚠️ Prudence :** créer une règle trop permissive (par ex. autoriser 3389/RDP depuis n'importe où sur le profil `Public`) ouvre une porte d'entrée. Restreins toujours au **profil** et, idéalement, à la **plage d'adresses** (`-RemoteAddress`) nécessaires. Et comme pour le réseau : ne te bloque pas toi-même en désactivant une règle qui autorise ta propre session distante.

## 🟡 Très utile en pratique

### Vérifier qu'un port est autorisé

```powershell
# Existe-t-il une règle Allow entrante pour le port 445 ?
Get-NetFirewallRule -Direction Inbound -Action Allow -Enabled True |
    Where-Object { ($_ | Get-NetFirewallPortFilter).LocalPort -eq 445 } |
    Select-Object DisplayName, Profile
```


Utile pour diagnostiquer « pourquoi le partage de fichiers ne répond pas ? » — souvent une règle de pare-feu.

### Auditer les règles entrantes autorisées

```powershell
Get-NetFirewallRule -Direction Inbound -Action Allow -Enabled True |
    ForEach-Object {
        $port = ($_ | Get-NetFirewallPortFilter).LocalPort
        [PSCustomObject]@{
            Regle   = $_.DisplayName
            Profil  = $_.Profile
            Port    = $port
        }
    } | Sort-Object Port
```


Cet audit — « qu'est-ce qui est ouvert en entrée ? » — est un contrôle de sécurité de base.

## 🔴 Bonus

### État global du pare-feu

```powershell
# S'assurer que le pare-feu est actif sur tous les profils
Get-NetFirewallProfile | Where-Object Enabled -eq $false
# → si cette commande renvoie quelque chose, un profil est désactivé (à corriger)
```


Un pare-feu désactivé sur un profil est un écart de sécurité classique à détecter.

## ❌ Erreur classique

```powershell
# Créer une règle sans restreindre le profil
New-NetFirewallRule -DisplayName "X" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 3389
# ❌ ouvre le port sur TOUS les profils (dont Public !)
# ✅ ajouter -Profile Domain,Private et/ou -RemoteAddress

# Désactiver une règle dont dépend ta session RDP/WinRM
Set-NetFirewallRule ... -Enabled False    # ❌ risque de te couper l'accès

# Confondre "règle existe" et "règle activée"
Get-NetFirewallRule -DisplayName "X"      # peut exister mais être Enabled False
```


## 💡 Exercices

**Guidé :** Affiche l'état (`Enabled`, actions par défaut) des trois profils de pare-feu. Signale en rouge tout profil désactivé.

**Autonome :** Écris un script qui liste les règles entrantes autorisées avec leur port et leur profil, et exporte le résultat en CSV (un audit d'ouverture réseau).

## 🧩 Mini-projet — Diagnostic réseau du poste

Crée `Get-NetworkDiagnostic.ps1` qui réunit toute la Partie III et produit un rapport :

- La fiche réseau : interface, IPv4, passerelle, DNS (Ch.15-16)
- Un test de connectivité vers la passerelle et vers un hôte externe (Ch.17)
- Un test de résolution DNS d'un nom connu (Ch.16)
- L'état des profils de pare-feu (Ch.18)
- Le tout en PSCustomObject, avec résumé coloré et export CSV, robuste aux erreurs (`try/catch`)

C'est le pendant « réseau » de ta boîte à outils. Combiné au Capstone de la Partie II, tu obtiens un véritable outil de diagnostic de poste.

## ✅ Tu sais maintenant...

- Les profils de pare-feu (Domain/Private/Public) et pourquoi ils comptent
- Lister, créer, modifier, supprimer des règles (`*-NetFirewallRule`)
- Direction (Inbound/Outbound) et action (Allow/Block)
- Restreindre par profil et adresse pour ne pas trop ouvrir
- Auditer ce qui est ouvert en entrée

## 💬 Questions d'entretien typiques

- **À quoi servent les profils de pare-feu ?** → Appliquer des règles différentes selon le type de réseau (Domain/Private/Public), Public étant le plus restrictif.
- **Comment ouvrir un port sans trop exposer la machine ?** → `New-NetFirewallRule` en restreignant `-Profile` et `-RemoteAddress` au strict nécessaire.
- **Comment savoir quel port est ouvert en entrée ?** → Croiser `Get-NetFirewallRule` (Inbound/Allow/Enabled) avec `Get-NetFirewallPortFilter`.

---
