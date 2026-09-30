---
title: PARTIE III — ADMINISTRATION RÉSEAU WINDOWS
source: IT/02_Windows/Powershell.md
note: PowerShell
chapter: 3
chapters: 8
---

Le réseau est le système nerveux de toute infrastructure. Cette partie t'apprend à inspecter et configurer le réseau d'un poste Windows avec PowerShell : interfaces, adresses IP, DNS, routes, connexions et pare-feu. On y remplace avantageusement les vieux outils (`ipconfig`, `ping`, `netstat`, `nslookup`) par des cmdlets qui renvoient des **objets** exploitables.

> **Comparaison Linux :** là où Linux utilise `ip`, `ping`, `ss`, `dig`, PowerShell offre `Get-NetIPConfiguration`, `Test-Connection`, `Get-NetTCPConnection`, `Resolve-DnsName`. Même logique, mais avec des objets au lieu de texte à parser.

---


## Chapitre 15 — Interfaces et configuration IP

### 🟢 Le minimum à savoir

#### Voir la configuration réseau

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

#### Lire l'adresse IPv4 d'une interface

```powershell
Get-NetIPAddress -AddressFamily IPv4 |
    Where-Object { $_.IPAddress -ne "127.0.0.1" } |
    Select-Object InterfaceAlias, IPAddress, PrefixLength
```

Le `PrefixLength` est le masque en notation CIDR : `/24` = `255.255.255.0`.

#### Les cartes réseau et leur état

```powershell
Get-NetAdapter | Select-Object Name, Status, LinkSpeed, MacAddress

# Activer / désactiver une carte                          [🔑 Admin]
Disable-NetAdapter -Name "Ethernet" -Confirm:$false
Enable-NetAdapter  -Name "Ethernet"
```

#### Configurer une IP statique `[🔑 Admin]`

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

#### DHCP vs statique

- **DHCP** : l'adresse est attribuée automatiquement par un serveur DHCP (Ch.27). C'est le cas des postes clients.
- **Statique** : l'adresse est fixée manuellement. C'est le cas des serveurs, imprimantes, équipements réseau.

```powershell
# L'interface est-elle en DHCP ?
Get-NetIPInterface -InterfaceAlias "Ethernet" -AddressFamily IPv4 |
    Select-Object InterfaceAlias, Dhcp
```

### 🟡 Très utile en pratique

#### Une fiche réseau complète

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

### 🔴 Bonus

#### Renommer une interface

```powershell
Rename-NetAdapter -Name "Ethernet 2" -NewName "LAN-Serveur"    # [🔑 Admin]
```

Nommer clairement ses interfaces (`LAN`, `DMZ`, `Backup`) facilite l'administration sur les serveurs multi-cartes.

### ❌ Erreur classique

```powershell
# Changer l'IP de l'interface qui te connecte à distance
New-NetIPAddress ...    # ❌ risque de te déconnecter du serveur

# Oublier -AddressFamily et mélanger IPv4/IPv6
Get-NetIPAddress | Select IPAddress    # ⚠️ mélange v4 et v6
Get-NetIPAddress -AddressFamily IPv4   # ✅

# Créer une IP sans supprimer l'ancienne → conflit / double IP
# Vérifier avec Get-NetIPAddress avant, retirer avec Remove-NetIPAddress si besoin
```

### 💡 Exercices

**Guidé :** Affiche, pour chaque interface active (`Status -eq "Up"`), son nom, son IPv4 et son débit (`LinkSpeed`).

**Autonome :** Écris un script qui produit la « fiche réseau » (PSCustomObject : Interface, IPv4, Passerelle, DNS) pour toutes les interfaces connectées, et l'exporte en CSV.

### ✅ Tu sais maintenant...

- `Get-NetIPConfiguration` (remplace `ipconfig`) et les cmdlets par couche (`Get-NetAdapter`, `Get-NetIPAddress`, `Get-NetIPInterface`)
- Lire IP, masque (PrefixLength), passerelle
- Configurer une IP statique ou repasser en DHCP — avec la prudence en session distante
- Construire une fiche réseau exploitable

### 💬 Questions d'entretien typiques

- **Quelle cmdlet remplace `ipconfig` ?** → `Get-NetIPConfiguration` (vue synthétique) ; `Get-NetIPAddress` pour le détail des adresses.
- **DHCP ou statique pour un serveur ?** → Statique en général, pour une adresse stable et prévisible.
- **Quel risque à reconfigurer l'IP à distance ?** → Se couper soi-même l'accès à la machine si on modifie l'interface de connexion.

---


## Chapitre 16 — DNS client et résolution

### 🟢 Le minimum à savoir

#### Le DNS, en une phrase

Le **DNS** (Domain Name System) traduit les noms (`serveur.lab.local`, `google.com`) en adresses IP. Côté client, deux choses nous intéressent : **quels serveurs DNS** la machine utilise, et **comment résoudre** un nom.

#### Voir et définir les serveurs DNS

```powershell
# Quels serveurs DNS utilise chaque interface ?
Get-DnsClientServerAddress -AddressFamily IPv4 |
    Select-Object InterfaceAlias, ServerAddresses

# Définir les serveurs DNS d'une interface                 [🔑 Admin]
# Machine jointe au domaine : UNIQUEMENT des DNS INTERNES (les DC/DNS du domaine)
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" `
    -ServerAddresses "192.168.1.10"                 # un seul DC/DNS
# Avec deux contrôleurs/serveurs DNS internes :
# Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses "192.168.1.10","192.168.1.11"

# Revenir au DNS automatique (via DHCP)
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ResetServerAddresses
```

> **⚠️ Ne mets JAMAIS un DNS public (8.8.8.8…) sur un poste joint au domaine.** Une machine du domaine doit interroger **exclusivement les DNS internes**, seuls capables de résoudre les enregistrements AD (localisation des contrôleurs de domaine, services…). Mettre `8.8.8.8` en secondaire casse la résolution AD de façon intermittente (le client peut interroger le mauvais serveur). La résolution des **noms Internet** se fait ensuite via des **forwarders configurés côté serveur DNS** (Ch.26) — pas en ajoutant un DNS public sur le client. C'est un pré-requis pour tout le lab AD des parties IV-V.

#### Résoudre un nom : `Resolve-DnsName`

L'équivalent moderne et puissant de `nslookup` :

```powershell
Resolve-DnsName google.com                       # résolution simple (A/AAAA)
Resolve-DnsName lab.local -Type A                # enregistrements A (IPv4)
Resolve-DnsName lab.local -Type MX               # serveurs mail
Resolve-DnsName 192.168.1.10 -Type PTR           # résolution inverse (IP → nom)
Resolve-DnsName dc01.lab.local -Server 192.168.1.10   # interroger un serveur précis
```

> **📌 Réflexe `Get-Member` :** `Resolve-DnsName google.com | Get-Member` montre que le résultat est un objet avec `Name`, `Type`, `IPAddress`, `TTL`. On peut donc filtrer et exploiter la réponse, contrairement au texte brut de `nslookup`.

> **Comparaison :** `Resolve-DnsName` ≈ `dig`/`nslookup` sous Linux, mais renvoie des objets. `-Type` sélectionne le type d'enregistrement (A, AAAA, MX, CNAME, PTR, TXT, NS…).

#### Le cache DNS du client

Windows garde en cache les résolutions récentes :

```powershell
Get-DnsClientCache               # voir le cache
Clear-DnsClientCache             # vider le cache (équivaut à ipconfig /flushdns)
```

> **Cas pratique :** après un changement DNS côté serveur, un client peut continuer à résoudre l'ancienne IP tant que son cache n'est pas expiré. `Clear-DnsClientCache` règle ce genre de « pourquoi ça pointe encore vers l'ancienne adresse ? ».

### 🟡 Très utile en pratique

#### Diagnostiquer une résolution qui échoue

```powershell
# 1. La machine a-t-elle des serveurs DNS configurés ?
Get-DnsClientServerAddress -AddressFamily IPv4 | Select InterfaceAlias, ServerAddresses

# 2. Le serveur DNS répond-il pour ce nom ?
Resolve-DnsName dc01.lab.local -Server 192.168.1.10 -ErrorAction SilentlyContinue

# 3. Le cache contient-il une vieille entrée ?
Get-DnsClientCache -Name "*lab.local*"
```

Cette séquence est un mini-arbre de décision de dépannage DNS très courant.

### 🔴 Bonus

#### Comparer résolution interne et externe

Interroger explicitement deux serveurs DNS différents permet de repérer une incohérence (split-horizon, cache empoisonné, mauvaise configuration) :

```powershell
Resolve-DnsName intranet.lab.local -Server 192.168.1.10    # DNS interne
Resolve-DnsName intranet.lab.local -Server 8.8.8.8 -ErrorAction SilentlyContinue   # DNS public
```

### ❌ Erreur classique

```powershell
# Oublier de vider le cache après un changement DNS
# → le client résout encore l'ancienne IP
Clear-DnsClientCache    # ✅

# Confondre "pas de réponse DNS" et "hôte injoignable"
# Resolve-DnsName teste la RÉSOLUTION (nom→IP), pas la connectivité
# Pour la connectivité → Test-Connection / Test-NetConnection (Ch.17)

# Interroger le DNS système alors qu'on veut tester un serveur précis
Resolve-DnsName x.lab.local -Server 192.168.1.10   # ✅ cible explicite
```

### 💡 Exercices

**Guidé :** Affiche les serveurs DNS configurés sur chaque interface, puis résous `google.com` et affiche uniquement les adresses IPv4 (`Type -eq "A"`).

**Autonome :** Écris un script `-Name` qui résout un nom, et si la résolution échoue, affiche les serveurs DNS configurés et suggère de vider le cache. Utilise `try/catch`.

### ✅ Tu sais maintenant...

- Le rôle du DNS et comment voir/définir les serveurs DNS d'une interface
- Résoudre des noms avec `Resolve-DnsName` (types A, MX, PTR…) — objets exploitables
- Gérer le cache DNS (`Get`/`Clear-DnsClientCache`)
- Une séquence de diagnostic de résolution

### 💬 Questions d'entretien typiques

- **Quelle cmdlet remplace `nslookup` ?** → `Resolve-DnsName`, qui renvoie des objets (avec `-Type`, `-Server`).
- **Pourquoi vider le cache DNS ?** → Pour forcer une nouvelle résolution après un changement côté serveur (l'ancienne entrée peut persister).
- **`Resolve-DnsName` teste-t-il la connectivité ?** → Non, seulement la résolution nom→IP. La connectivité se teste avec `Test-Connection`/`Test-NetConnection`.

---


## Chapitre 17 — Routage et connexions

### 🟢 Le minimum à savoir

#### Tester la connectivité : `Test-Connection` et `Test-NetConnection`

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

#### La table de routage

La table de routage décide par où sortent les paquets :

```powershell
Get-NetRoute -AddressFamily IPv4 |
    Select-Object DestinationPrefix, NextHop, RouteMetric, InterfaceAlias

# La route par défaut (0.0.0.0/0) = la passerelle
Get-NetRoute -DestinationPrefix "0.0.0.0/0"
```

`DestinationPrefix 0.0.0.0/0` est la **route par défaut** : tout ce qui n'a pas de route spécifique passe par là (la passerelle).

#### Les connexions TCP actives : `Get-NetTCPConnection`

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

### 🟡 Très utile en pratique

#### Un test de connectivité multi-ports

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

### 🔴 Bonus

#### Tracer la route (`traceroute`)

```powershell
Test-NetConnection google.com -TraceRoute        # chemin réseau saut par saut
```

#### Ajouter une route statique `[🔑 Admin]`

```powershell
New-NetRoute -DestinationPrefix "10.0.0.0/16" -InterfaceAlias "Ethernet" -NextHop "192.168.1.254"
```

Rare sur un poste, plus courant sur des serveurs à réseaux multiples.

### ❌ Erreur classique

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

### 💡 Exercices

**Guidé :** Teste si le port 443 de `google.com` est joignable et affiche `TcpTestSucceeded`. Puis trouve quel processus écoute sur le port 135 en local.

**Autonome :** Écris un script `-ComputerName` qui teste une liste de ports (par exemple 53, 389, 445) et renvoie un PSCustomObject par port (Port, Ouvert). Exporte en CSV.

### ✅ Tu sais maintenant...

- Tester connectivité et ports avec `Test-Connection` et surtout `Test-NetConnection -Port`
- Lire la table de routage (`Get-NetRoute`) et repérer la route par défaut
- Lister les connexions TCP (`Get-NetTCPConnection`) et relier un port à son processus (`OwningProcess`)
- Diagnostiquer « ping OK mais service KO » via les ports

### 💬 Questions d'entretien typiques

- **Comment vérifier qu'un port applicatif est joignable ?** → `Test-NetConnection -ComputerName X -Port N` (propriété `TcpTestSucceeded`).
- **Quelle cmdlet remplace `netstat` ?** → `Get-NetTCPConnection`, avec `OwningProcess` pour retrouver le programme via `Get-Process`.
- **Qu'est-ce que la route `0.0.0.0/0` ?** → La route par défaut : tout le trafic sans route spécifique passe par sa passerelle.

---


## Chapitre 18 — Pare-feu Windows

### 🟢 Le minimum à savoir

#### Les profils de pare-feu

Le Pare-feu Windows Defender applique des règles selon un **profil** correspondant au type de réseau :

- **Domain** : la machine est connectée à son domaine AD
- **Private** : réseau privé de confiance (maison, bureau)
- **Public** : réseau non fiable (café, aéroport) — le plus restrictif

```powershell
Get-NetFirewallProfile |
    Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
```

> **Important :** un même poste applique le profil correspondant au réseau où il se trouve. Une règle peut être active sur `Private` mais pas sur `Public`.

#### Lister les règles

```powershell
Get-NetFirewallRule | Where-Object Enabled -eq "True" |
    Select-Object DisplayName, Direction, Action, Profile -First 20

# Les règles entrantes qui autorisent quelque chose
Get-NetFirewallRule -Direction Inbound -Action Allow -Enabled True |
    Select-Object DisplayName, Profile
```

> **📌 Réflexe `Get-Member` :** une règle de pare-feu a beaucoup de propriétés (`DisplayName`, `Direction`, `Action`, `Profile`, `Enabled`). Le détail des ports/protocoles se lit via des cmdlets associées (`Get-NetFirewallPortFilter`), car une règle est liée à des filtres.

#### Direction et action

- **Direction** : `Inbound` (trafic entrant) ou `Outbound` (sortant)
- **Action** : `Allow` (autoriser) ou `Block` (bloquer)

La logique par défaut d'un poste : **entrant bloqué** sauf exceptions, **sortant autorisé**.

#### Créer une règle `[🔑 Admin]`

```powershell
# Autoriser le port TCP 8080 en entrée, sur les profils Domain et Private
New-NetFirewallRule -DisplayName "App interne 8080" `
    -Direction Inbound -Action Allow `
    -Protocol TCP -LocalPort 8080 `
    -Profile Domain,Private
```

#### Modifier et supprimer `[🔑 Admin]`

```powershell
Set-NetFirewallRule -DisplayName "App interne 8080" -Enabled False   # désactiver
Remove-NetFirewallRule -DisplayName "App interne 8080"               # supprimer
```

> **⚠️ Prudence :** créer une règle trop permissive (par ex. autoriser 3389/RDP depuis n'importe où sur le profil `Public`) ouvre une porte d'entrée. Restreins toujours au **profil** et, idéalement, à la **plage d'adresses** (`-RemoteAddress`) nécessaires. Et comme pour le réseau : ne te bloque pas toi-même en désactivant une règle qui autorise ta propre session distante.

### 🟡 Très utile en pratique

#### Vérifier qu'un port est autorisé

```powershell
# Existe-t-il une règle Allow entrante pour le port 445 ?
Get-NetFirewallRule -Direction Inbound -Action Allow -Enabled True |
    Where-Object { ($_ | Get-NetFirewallPortFilter).LocalPort -eq 445 } |
    Select-Object DisplayName, Profile
```

Utile pour diagnostiquer « pourquoi le partage de fichiers ne répond pas ? » — souvent une règle de pare-feu.

#### Auditer les règles entrantes autorisées

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

### 🔴 Bonus

#### État global du pare-feu

```powershell
# S'assurer que le pare-feu est actif sur tous les profils
Get-NetFirewallProfile | Where-Object Enabled -eq $false
# → si cette commande renvoie quelque chose, un profil est désactivé (à corriger)
```

Un pare-feu désactivé sur un profil est un écart de sécurité classique à détecter.

### ❌ Erreur classique

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

### 💡 Exercices

**Guidé :** Affiche l'état (`Enabled`, actions par défaut) des trois profils de pare-feu. Signale en rouge tout profil désactivé.

**Autonome :** Écris un script qui liste les règles entrantes autorisées avec leur port et leur profil, et exporte le résultat en CSV (un audit d'ouverture réseau).

### 🧩 Mini-projet — Diagnostic réseau du poste

Crée `Get-NetworkDiagnostic.ps1` qui réunit toute la Partie III et produit un rapport :

- La fiche réseau : interface, IPv4, passerelle, DNS (Ch.15-16)
- Un test de connectivité vers la passerelle et vers un hôte externe (Ch.17)
- Un test de résolution DNS d'un nom connu (Ch.16)
- L'état des profils de pare-feu (Ch.18)
- Le tout en PSCustomObject, avec résumé coloré et export CSV, robuste aux erreurs (`try/catch`)

C'est le pendant « réseau » de ta boîte à outils. Combiné au Capstone de la Partie II, tu obtiens un véritable outil de diagnostic de poste.

### ✅ Tu sais maintenant...

- Les profils de pare-feu (Domain/Private/Public) et pourquoi ils comptent
- Lister, créer, modifier, supprimer des règles (`*-NetFirewallRule`)
- Direction (Inbound/Outbound) et action (Allow/Block)
- Restreindre par profil et adresse pour ne pas trop ouvrir
- Auditer ce qui est ouvert en entrée

### 💬 Questions d'entretien typiques

- **À quoi servent les profils de pare-feu ?** → Appliquer des règles différentes selon le type de réseau (Domain/Private/Public), Public étant le plus restrictif.
- **Comment ouvrir un port sans trop exposer la machine ?** → `New-NetFirewallRule` en restreignant `-Profile` et `-RemoteAddress` au strict nécessaire.
- **Comment savoir quel port est ouvert en entrée ?** → Croiser `Get-NetFirewallRule` (Inbound/Allow/Enabled) avec `Get-NetFirewallPortFilter`.

---
