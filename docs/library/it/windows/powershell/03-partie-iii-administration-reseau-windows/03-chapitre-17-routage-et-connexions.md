---
title: Chapitre 17 — Routage et connexions
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie III — Administration réseau Windows
  - index.md
---

## 🟢 Le minimum à savoir

### Tester la connectivité : `Test-Connection` et `Test-NetConnection`

```powershell
# Ping simple (renvoie des objets, pas du texte) — forme positionnelle, valable 5.1 et 7
Test-Connection dc01.lab.local -Count 2

# Ping "booléen" pour un if
if (Test-Connection dc01.lab.local -Count 1 -Quiet) { "En ligne" }

# LE couteau suisse : Test-NetConnection (ping + test de PORT + route)
Test-NetConnection -ComputerName dc01.lab.local -Port 445    # le port SMB est-il ouvert ?
Test-NetConnection -ComputerName google.com -Port 443        # HTTPS accessible ?
```


> **Note version :** le nom du premier paramètre de `Test-Connection` diffère selon la version — `-ComputerName` en Windows PowerShell 5.1, `-TargetName` en PowerShell 7. Pour rester compatible avec les deux, utilise la **forme positionnelle** (`Test-Connection dc01.lab.local`), comme ci-dessus.

> **`Test-NetConnection` est essentiel :** il ne fait pas que pinguer — il teste si un **port TCP** est joignable. « Le serveur répond au ping mais l'application ne marche pas » se diagnostique avec `-Port`. C'est l'outil de dépannage réseau n°1.

> **📌 Réflexe `Get-Member` :** `Test-NetConnection google.com -Port 443 | Get-Member` montre `TcpTestSucceeded`, `PingSucceeded`, `RemoteAddress`, `SourceAddress`. On peut donc scripter des tests de connectivité qui renvoient `True`/`False` par port.

### La table de routage

La table de routage décide par où sortent les paquets :

```powershell
Get-NetRoute -AddressFamily IPv4 |
    Select-Object DestinationPrefix, NextHop, RouteMetric, InterfaceAlias

# La route par défaut (0.0.0.0/0) = la passerelle
Get-NetRoute -DestinationPrefix "0.0.0.0/0"
```


`DestinationPrefix 0.0.0.0/0` est la **route par défaut** : tout ce qui n'a pas de route spécifique passe par là (la passerelle).

### Les connexions TCP actives : `Get-NetTCPConnection`

L'équivalent objet de `netstat` :

```powershell
Get-NetTCPConnection -State Established |
    Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, OwningProcess

# Quel PROCESSUS écoute sur un port donné ?
Get-NetTCPConnection -LocalPort 445 -State Listen |
    Select-Object LocalPort, OwningProcess
```


> **Astuce puissante :** `OwningProcess` est le PID du processus. En le croisant avec `Get-Process`, on répond à « quel programme écoute sur ce port ? » — utile en admin comme en sécurité :
> ```powershell
> Get-NetTCPConnection -LocalPort 3389 -State Listen |
>     ForEach-Object { Get-Process -Id $_.OwningProcess }
> ```

## 🟡 Très utile en pratique

### Un test de connectivité multi-ports

```powershell
$cible = "dc01.lab.local"
$ports = @{ "DNS/TCP"=53; "Kerberos"=88; "LDAP"=389; "SMB"=445; "RDP"=3389 }

foreach ($nom in $ports.Keys) {
    $ok = (Test-NetConnection $cible -Port $ports[$nom] -WarningAction SilentlyContinue).TcpTestSucceeded
    [PSCustomObject]@{ Service = $nom; Port = $ports[$nom]; OuvertTCP = $ok }
}
```


Ce genre de test « quels ports d'un contrôleur de domaine sont joignables ? » est un diagnostic classique.

> **⚠️ `Test-NetConnection -Port` teste uniquement le TCP.** Le résultat `TcpTestSucceeded` signifie « **TCP/53 joignable** », pas « le service DNS fonctionne ». Or le DNS utilise **UDP et TCP** selon les opérations (les requêtes courantes passent en UDP/53, TCP/53 servant surtout aux transferts de zone et grandes réponses). Un `Test-NetConnection -Port 53` peut donc échouer alors que la résolution marche très bien. **Pour tester réellement le service DNS**, interroge-le avec `Resolve-DnsName` (Ch.16) :
> ```powershell
> Resolve-DnsName lab.local -Server 192.168.1.10   # le serveur répond-il VRAIMENT à une requête DNS ?
> ```
> Règle générale : `Test-NetConnection -Port` répond à « le port TCP est-il joignable ? » ; pour « le service applicatif répond-il ? », utilise l'outil du protocole (ici `Resolve-DnsName`).

## 🔴 Bonus

### Tracer la route (`traceroute`)

```powershell
Test-NetConnection google.com -TraceRoute        # chemin réseau saut par saut
```


### Ajouter une route statique `[🔑 Admin]`

```powershell
New-NetRoute -DestinationPrefix "10.0.0.0/16" -InterfaceAlias "Ethernet" -NextHop "192.168.1.254"
```


Rare sur un poste, plus courant sur des serveurs à réseaux multiples.

## ❌ Erreur classique

```powershell
# Croire que "ping OK" = "service OK"
Test-Connection SRV01 -Count 1    # ⚠️ teste seulement ICMP, pas l'application
Test-NetConnection SRV01 -Port 445   # ✅ teste le vrai port applicatif

# Lire du texte de netstat au lieu d'objets
netstat -ano | findstr 445    # ⚠️ texte à parser
Get-NetTCPConnection -LocalPort 445   # ✅ objets exploitables

# Oublier -Quiet quand on veut juste un booléen dans un if
if (Test-Connection SRV01 -Count 1) { }          # ⚠️ renvoie des objets
if (Test-Connection SRV01 -Count 1 -Quiet) { }   # ✅ True/False
```


## 💡 Exercices

**Guidé :** Teste si le port 443 de `google.com` est joignable et affiche `TcpTestSucceeded`. Puis trouve quel processus écoute sur le port 135 en local.

**Autonome :** Écris un script `-ComputerName` qui teste une liste de ports (par exemple 53, 389, 445) et renvoie un PSCustomObject par port (Port, Ouvert). Exporte en CSV.

## ✅ Tu sais maintenant...

- Tester connectivité et ports avec `Test-Connection` et surtout `Test-NetConnection -Port`
- Lire la table de routage (`Get-NetRoute`) et repérer la route par défaut
- Lister les connexions TCP (`Get-NetTCPConnection`) et relier un port à son processus (`OwningProcess`)
- Diagnostiquer « ping OK mais service KO » via les ports

## 💬 Questions d'entretien typiques

- **Comment vérifier qu'un port applicatif est joignable ?** → `Test-NetConnection -ComputerName X -Port N` (propriété `TcpTestSucceeded`).
- **Quelle cmdlet remplace `netstat` ?** → `Get-NetTCPConnection`, avec `OwningProcess` pour retrouver le programme via `Get-Process`.
- **Qu'est-ce que la route `0.0.0.0/0` ?** → La route par défaut : tout le trafic sans route spécifique passe par sa passerelle.

---
