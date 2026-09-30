---
title: PARTIE V — GPO ET SERVICES WINDOWS SERVER
source: IT/02_Windows/Powershell.md
note: PowerShell
chapter: 5
chapters: 8
---

> **🏗️ On reste dans l'administration d'infrastructure.** Cette partie couvre les stratégies de groupe (GPO) et trois rôles serveur essentiels : DNS, DHCP et le partage de fichiers (SMB). Environnement requis : le lab Windows Server de la Partie IV.
>
> **PowerShell reste le fil rouge.** On n'apprend pas ici à concevoir une architecture DNS ou un plan d'adressage — on apprend à *piloter* ces rôles avec PowerShell. Pour la conception, réfère-toi aux cours dédiés à chaque technologie.
>
> **⚠️ Lab uniquement.** Comme en Partie IV, ces chapitres modifient des éléments d'infrastructure (GPO liées à des OU, enregistrements DNS, étendues DHCP, partages). Une GPO mal réglée ou un enregistrement DNS erroné affecte **tout un domaine**. Pratique exclusivement sur ton lab, et sauvegarde avant de modifier (`Backup-GPO`, export de zone…).

---


## Chapitre 25 — Group Policy (GPO)

### 🟢 Le minimum à savoir

#### Comprendre le modèle AVANT les cmdlets

> **⚠️ Point pédagogique clé.** Administrer les GPO, ce n'est **pas** mémoriser `New-GPO`. C'est comprendre un **modèle** : comment une stratégie s'applique, à qui, dans quel ordre. Sans ce modèle, les cmdlets ne servent à rien. On pose donc d'abord les concepts.

Une **GPO** (Group Policy Object) est un ensemble de réglages appliqués automatiquement à des utilisateurs et/ou des ordinateurs : politique de mot de passe, fonds d'écran, restrictions, scripts de démarrage, déploiement de logiciels, réglages de sécurité (dont le Script Block Logging du Ch.35)…

#### Les deux moitiés d'une GPO

Une GPO a deux sections :

- **Computer Configuration** : s'applique aux **ordinateurs** (au démarrage et périodiquement)
- **User Configuration** : s'applique aux **utilisateurs** (à la connexion et périodiquement)

Selon ce que tu veux régler, tu utilises l'une ou l'autre.

#### Le mécanisme d'application : lien + héritage

Une GPO ne fait rien tant qu'elle n'est pas **liée** à un conteneur. On lie une GPO à :

- un **site**, un **domaine**, ou (le plus courant) une **OU**

Et elle s'applique à **tous les objets de ce conteneur et des OU en dessous** (héritage). D'où l'importance de la structure d'OU vue au Ch.22 : **c'est elle qui détermine qui reçoit quelles GPO**.

L'ordre d'application (le dernier gagne en cas de conflit) suit l'acronyme **LSDOU** : **L**ocal → **S**ite → **D**omaine → **OU** (de la plus haute à la plus basse). Une GPO liée à une OU proche de l'objet l'emporte donc sur une GPO de domaine.

#### Les modificateurs d'héritage

Trois mécanismes altèrent cet ordre — à connaître pour comprendre ce qui s'applique vraiment :

| Mécanisme | Effet |
|-----------|-------|
| **Enforced** (Appliqué) | Force la GPO à gagner, même sur les OU enfants qui bloquent l'héritage |
| **Block Inheritance** (Bloquer l'héritage) | Une OU refuse les GPO héritées des niveaux supérieurs (sauf Enforced) |
| **Security Filtering** | Restreint l'application de la GPO à certains utilisateurs/groupes seulement |
| **WMI Filtering** | Applique la GPO seulement si une condition WMI est vraie (ex : « seulement les portables ») |

#### Les cmdlets GPO `[🖥️ Server]` `[🔑 Admin]`

Elles viennent du module **GroupPolicy** (présent sur un DC ou via RSAT) :

```powershell
Import-Module GroupPolicy

Get-GPO -All                          # lister toutes les GPO
Get-GPO -Name "Politique Mot de Passe"

New-GPO -Name "Restrictions USB" -Comment "Bloque les clés USB"    # créer (vide)

# Lier une GPO à une OU (c'est le lien qui la rend active)
New-GPLink -Name "Restrictions USB" -Target "OU=Postes,DC=lab,DC=local"

# Modifier un lien (ordre, activation, enforced)
Set-GPLink -Name "Restrictions USB" -Target "OU=Postes,DC=lab,DC=local" -Enforced Yes

Remove-GPO -Name "Restrictions USB"   # supprimer
```

> **📌 Le piège du débutant :** `New-GPO` crée une GPO **vide et non liée** — elle ne fait rien. Il faut ensuite (1) **configurer** ses réglages (souvent via la console graphique GPMC, car PowerShell ne couvre pas tous les réglages nativement) et (2) la **lier** à une OU avec `New-GPLink`. Créer ≠ appliquer.

### 🟡 Très utile en pratique

#### Documenter et sauvegarder les GPO

```powershell
# Générer un rapport HTML lisible d'une GPO (ce qu'elle contient)
Get-GPOReport -Name "Politique Mot de Passe" -ReportType Html -Path "C:\rapports\GPO_MDP.html"

# Rapport de TOUTES les GPO
Get-GPOReport -All -ReportType Html -Path "C:\rapports\Toutes_GPO.html"

# Sauvegarder / restaurer (indispensable avant toute modification)
Backup-GPO -All -Path "C:\backup\gpo"
Restore-GPO -Name "Politique Mot de Passe" -Path "C:\backup\gpo"
```

> **📌 Discipline `Get`/backup avant modification :** avant de toucher à une GPO, on la **sauvegarde** (`Backup-GPO`) et on **documente** l'existant (`Get-GPOReport`). Une GPO mal réglée peut affecter des milliers de postes d'un coup.

#### Diagnostiquer ce qui s'applique réellement : RSOP

La question fréquente « pourquoi ce réglage ne s'applique-t-il pas ? » se résout avec le **Resultant Set of Policy** — l'ensemble des stratégies effectivement appliquées à un utilisateur/ordinateur :

```powershell
# Rapport RSOP pour un utilisateur sur une machine
Get-GPResultantSetOfPolicy -User lab\jdupont -Computer CLIENT01 -ReportType Html -Path "C:\rapports\rsop.html"

# En ligne de commande rapide (sur la machine cible)
gpresult /r                    # résumé des GPO appliquées
gpresult /h rsop.html          # rapport HTML complet

# Forcer la réapplication immédiate des GPO
gpupdate /force
```

### 🔴 Bonus

#### Les limites de PowerShell pour les GPO

PowerShell gère très bien le **cycle de vie** des GPO (créer, lier, sauvegarder, rapporter, déléguer). Mais **modifier le contenu** d'une GPO (les milliers de réglages individuels) est partiellement couvert : `Set-GPRegistryValue` permet de piloter les réglages basés sur le registre, mais beaucoup de réglages passent encore par la console graphique (GPMC) ou des modèles ADMX. C'est une limite à connaître : PowerShell orchestre, la GPMC affine.

```powershell
# Exemple de réglage basé sur le registre via PowerShell
Set-GPRegistryValue -Name "Restrictions USB" `
    -Key "HKLM\SYSTEM\CurrentControlSet\Services\USBSTOR" `
    -ValueName "Start" -Type DWord -Value 4
```

### ❌ Erreur classique

```powershell
# Croire que New-GPO applique quelque chose
New-GPO -Name "X"           # ❌ crée une GPO VIDE et NON LIÉE (sans effet)
# → il faut la configurer PUIS New-GPLink vers une OU

# Modifier une GPO sans sauvegarde
Set-GPRegistryValue ...     # ❌ sans filet
Backup-GPO -Name "X" -Path C:\backup ; Set-GPRegistryValue ...   # ✅

# Ne pas comprendre pourquoi une GPO ne s'applique pas
# → vérifier : lien actif ? Block Inheritance ? Security Filtering ? → RSOP / gpresult
```

### 💡 Exercices

**Guidé :** Liste toutes les GPO du domaine, puis génère un rapport HTML de l'une d'elles avec `Get-GPOReport`.

**Autonome :** Crée une GPO de test, lie-la à une OU, sauvegarde-la avec `Backup-GPO`, génère son rapport, puis nettoie (supprime le lien et la GPO).

### ✅ Tu sais maintenant...

- Le **modèle** GPO (Computer/User Config, lien, héritage LSDOU, Enforced, Block Inheritance, filtres)
- Piloter le cycle de vie des GPO (`Get`/`New`/`Remove-GPO`, `New`/`Set-GPLink`)
- Documenter (`Get-GPOReport`) et sauvegarder (`Backup`/`Restore-GPO`)
- Diagnostiquer l'application réelle (RSOP, `gpresult`, `gpupdate`)
- Que `New-GPO` ne suffit pas (créer ≠ configurer ≠ lier) et les limites de PowerShell

### 💬 Questions d'entretien typiques

- **Que fait `New-GPO` exactement ?** → Crée une GPO vide et non liée ; il faut la configurer puis la lier à une OU pour qu'elle s'applique.
- **Dans quel ordre les GPO s'appliquent-elles ?** → LSDOU : Local, Site, Domaine, OU — la dernière (OU la plus proche) l'emporte, sauf Enforced.
- **Comment savoir quelles GPO s'appliquent à un poste ?** → RSOP (`Get-GPResultantSetOfPolicy`) ou `gpresult /r` sur la machine.
- **Que faire avant de modifier une GPO ?** → La sauvegarder (`Backup-GPO`) et documenter l'existant (`Get-GPOReport`).

---


## Chapitre 26 — DNS Server

### 🟢 Le minimum à savoir

#### Client vs serveur DNS

Au Ch.16, on configurait le DNS **côté client** (quels serveurs interroger, résoudre un nom). Ici, on administre le **serveur DNS** lui-même — celui qui héberge les enregistrements. Dans un domaine AD, le DNS est presque toujours installé sur les contrôleurs de domaine (AD en dépend fortement).

Le module : **DnsServer** (`[🖥️ Server]`, sur un serveur DNS ou via RSAT).

#### Les zones

Une **zone** est une portion de l'espace de noms DNS que le serveur gère (ex : la zone `lab.local`). Deux grandes familles :

- **Zone de recherche directe** : nom → IP (le cas normal)
- **Zone de recherche inversée** : IP → nom (pour les requêtes PTR)

```powershell
Get-DnsServerZone                          # lister les zones
Get-DnsServerZone -Name "lab.local"        # une zone précise
```

#### Les enregistrements

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

#### Créer et supprimer des enregistrements `[🔑 Admin]`

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

### 🟡 Très utile en pratique

#### Vérifier la cohérence client/serveur

Le Ch.16 (client) et ce chapitre (serveur) se combinent pour diagnostiquer :

```powershell
# Côté serveur : l'enregistrement existe-t-il ?
Get-DnsServerResourceRecord -ZoneName "lab.local" -Name "srv-app"

# Côté client : la résolution fonctionne-t-elle ? (rappel Ch.16)
Resolve-DnsName "srv-app.lab.local" -Server 192.168.1.10
```

Si l'enregistrement existe côté serveur mais que le client ne résout pas : problème de cache client (`Clear-DnsClientCache`) ou de serveur DNS interrogé.

#### Auditer les enregistrements d'une zone

```powershell
Get-DnsServerResourceRecord -ZoneName "lab.local" -RRType A |
    Select-Object HostName, @{N="IP";E={$_.RecordData.IPv4Address}} |
    Sort-Object HostName |
    Export-Csv "C:\rapports\dns_A_records.csv" -NoTypeInformation -Encoding UTF8
```

### 🔴 Bonus

#### Zones intégrées à AD

Dans un domaine, les zones DNS sont souvent **intégrées à Active Directory** : elles sont répliquées automatiquement entre tous les DC (via la réplication AD) et sécurisées. C'est la configuration recommandée, mais sa mise en place relève d'un cours DNS/AD dédié.

### ❌ Erreur classique

```powershell
# Créer un doublon d'enregistrement A
Add-DnsServerResourceRecordA ...    # ❌ sans vérifier l'existant → résolution aléatoire
Get-DnsServerResourceRecord -ZoneName lab.local -Name srv-app   # ✅ vérifier d'abord

# Oublier de vider le cache client après un changement serveur (Ch.16)
Clear-DnsClientCache

# Confondre zone directe et inversée
# Un enregistrement PTR va dans la zone INVERSÉE, pas la directe
```

### 💡 Exercices

**Guidé :** Liste les zones du serveur DNS, puis affiche tous les enregistrements A de `lab.local` avec leur IP.

**Autonome :** Ajoute un enregistrement A `test-srv` pointant vers une IP, vérifie sa création côté serveur (`Get-DnsServerResourceRecord`) et côté client (`Resolve-DnsName`), puis supprime-le.

### ✅ Tu sais maintenant...

- La différence DNS client (Ch.16) / serveur (ici)
- Les zones (directe/inversée) et les types d'enregistrements (A, AAAA, CNAME, PTR, MX, NS)
- Lister, créer, supprimer des enregistrements (`*-DnsServerResourceRecord*`)
- Diagnostiquer en croisant serveur et client

### 💬 Questions d'entretien typiques

- **Différence entre un enregistrement A et un CNAME ?** → A pointe un nom vers une IP ; CNAME pointe un nom vers un autre nom (alias).
- **Où va un enregistrement PTR ?** → Dans une zone de recherche **inversée** (résolution IP → nom).
- **Pourquoi le DNS est-il critique en AD ?** → Active Directory repose sur le DNS pour localiser les contrôleurs de domaine et les services ; un DNS cassé casse l'authentification.

---


## Chapitre 27 — DHCP Server

### 🟢 Le minimum à savoir

#### À quoi sert le DHCP

Le **DHCP** (Dynamic Host Configuration Protocol) attribue automatiquement une configuration IP (adresse, masque, passerelle, DNS) aux machines qui se connectent au réseau. Sans lui, il faudrait configurer chaque poste à la main. Au Ch.15, on voyait le côté client (« l'interface est en DHCP ») ; ici, on administre le **serveur** qui distribue les adresses.

Le module : **DhcpServer** (`[🖥️ Server]`).

#### Les concepts clés

| Terme | Ce que c'est |
|-------|-------------|
| **Scope (étendue)** | Une plage d'adresses distribuables (ex : `192.168.1.100` → `192.168.1.200`) |
| **Lease (bail)** | Une adresse attribuée à une machine pour une durée limitée |
| **Reservation** | Une adresse toujours attribuée à la même machine (via son adresse MAC) |
| **Option** | Un paramètre distribué avec l'adresse (passerelle = option 3, DNS = option 6…) |

#### Lister les scopes et les baux

```powershell
Get-DhcpServerv4Scope                          # les étendues configurées

# Les baux actifs d'une étendue (qui a quelle IP ?)
Get-DhcpServerv4Lease -ScopeId 192.168.1.0
```

> **📌 Réflexe `Get-Member` :** `Get-DhcpServerv4Lease -ScopeId 192.168.1.0 | Get-Member` révèle `IPAddress`, `ClientId` (la MAC), `HostName`, `AddressState`, `LeaseExpiryTime`. C'est ainsi qu'on répond à « quelle machine a l'adresse .150 ? ».

#### Les réservations `[🔑 Admin]`

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

### 🟡 Très utile en pratique

#### Diagnostiquer l'épuisement d'un scope

Un problème classique : « plus personne ne reçoit d'adresse ». Souvent, le scope est **épuisé** (toutes les adresses distribuées) :

```powershell
# Statistiques d'une étendue (taux d'utilisation)
Get-DhcpServerv4ScopeStatistics -ScopeId 192.168.1.0 |
    Select-Object ScopeId, Free, InUse, PercentageInUse
```

Un `PercentageInUse` proche de 100 % explique pourquoi les nouvelles machines n'obtiennent pas d'adresse.

#### Auditer les baux actifs

```powershell
Get-DhcpServerv4Lease -ScopeId 192.168.1.0 |
    Where-Object AddressState -eq "Active" |
    Select-Object IPAddress, HostName, ClientId, LeaseExpiryTime |
    Sort-Object IPAddress
```

Utile pour repérer une machine inconnue sur le réseau (un `HostName` ou une MAC non identifiés = point d'attention sécurité).

### 🔴 Bonus

#### Convertir un bail en réservation

Quand une machine a déjà un bail et qu'on veut fixer son adresse, on peut créer la réservation depuis son bail existant — pratique pour « figer » l'IP d'un serveur récemment déployé :

```powershell
$bail = Get-DhcpServerv4Lease -ScopeId 192.168.1.0 |
    Where-Object HostName -like "SRV-APP*"
Add-DhcpServerv4Reservation -ScopeId 192.168.1.0 `
    -IPAddress $bail.IPAddress -ClientId $bail.ClientId -Description "SRV-APP fixé"
```

### ❌ Erreur classique

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

### 💡 Exercices

**Guidé :** Affiche les statistiques d'utilisation de ton étendue DHCP et ses baux actifs (IP, nom d'hôte, expiration).

**Autonome :** Crée une réservation pour une machine fictive, vérifie-la, puis supprime-la (`Remove-DhcpServerv4Reservation`). Exporte la liste des baux actifs en CSV.

### ✅ Tu sais maintenant...

- Le rôle du DHCP (attribution IP automatique) — côté serveur
- Les concepts : scope, lease, reservation, option
- Lister scopes et baux, créer des réservations (`*-DhcpServerv4*`)
- Diagnostiquer un scope épuisé (`Get-DhcpServerv4ScopeStatistics`)

### 💬 Questions d'entretien typiques

- **Différence entre un bail et une réservation ?** → Un bail est temporaire et dynamique ; une réservation attribue toujours la même IP à une machine (via sa MAC).
- **Pourquoi une machine n'obtient-elle plus d'adresse ?** → Souvent un scope épuisé (`PercentageInUse` ~100 %), à vérifier via les statistiques.
- **Comment garantir une IP fixe à une imprimante sans la configurer en statique ?** → Une réservation DHCP basée sur sa MAC.

---


## Chapitre 28 — File Server et partages SMB

### 🟢 Le minimum à savoir

#### Le partage de fichiers en réseau

**SMB** (Server Message Block) est le protocole de partage de fichiers de Windows. Un **partage** (share) expose un dossier du serveur sur le réseau, accessible via `\\serveur\partage`. On gère tout ça avec le module **SmbShare**.

```powershell
Get-SmbShare                          # les partages du serveur
Get-SmbShare -Name "Compta"           # un partage précis
```

> **📌 Réflexe `Get-Member` :** `Get-SmbShare | Get-Member` révèle `Name`, `Path`, `Description`, `EncryptData`. Un partage relie un **nom réseau** à un **chemin local**.

#### Créer un partage `[🔑 Admin]`

```powershell
New-SmbShare -Name "Compta" -Path "C:\Partages\Compta" `
    -Description "Dossier du service Comptabilité" `
    -FullAccess "lab\Administrateurs" `
    -ChangeAccess "lab\GG_Compta" `
    -ReadAccess "lab\GG_Consultants"
```

#### LE point crucial : permissions de partage vs permissions NTFS

> **⚠️ La confusion n°1 en administration de fichiers.** Il existe **deux couches de permissions** distinctes qui se cumulent, et c'est **la plus restrictive des deux qui gagne** :
>
> 1. **Permissions de partage (SMB)** : s'appliquent quand on accède via le réseau (`\\serveur\partage`). Gérées par `Grant-SmbShareAccess`. Grossières (FullAccess / ChangeAccess / ReadAccess).
> 2. **Permissions NTFS** (Ch.9, `Get-Acl`/`Set-Acl`) : s'appliquent **toujours** (réseau ET local). Fines (par fichier/dossier, nombreux droits).
>
> **L'accès effectif = l'intersection des deux.** Si le partage autorise `Change` mais que NTFS n'autorise que `Read`, l'utilisateur n'aura que `Read`. Et inversement.

```powershell
# Permissions de PARTAGE (couche SMB)
Get-SmbShareAccess -Name "Compta"
Grant-SmbShareAccess -Name "Compta" -AccountName "lab\GG_Compta" -AccessRight Change -Force

# Permissions NTFS (couche fichiers — rappel Ch.9)
Get-Acl "C:\Partages\Compta" | Select-Object -ExpandProperty Access
```

> **Une approche courante (à comprendre, pas à appliquer aveuglément) :** beaucoup d'administrateurs mettent les permissions de partage **assez larges** et gèrent la **finesse au niveau NTFS** uniquement, pour éviter de raisonner sur deux couches en parallèle. Attention toutefois : « large » ne veut pas dire `Full Control` pour tout le monde. Donner `Full Control` en partage inclut le droit de **modifier les permissions**, ce qui est excessif ; on se limite en général à `Change` pour les groupes qui écrivent, et l'on s'appuie sur NTFS pour le détail. Le point à retenir : il faut **comprendre les deux couches** pour diagnostiquer un « je ne peux pas écrire alors que j'ai les droits » — le choix de simplifier côté partage est un compromis d'exploitation, pas une règle absolue.

#### Voir qui est connecté

```powershell
Get-SmbSession                        # sessions SMB ouvertes (qui est connecté ?)
Get-SmbOpenFile                       # fichiers actuellement ouverts via le réseau
```

Utile avant une maintenance (« qui utilise ce partage là maintenant ? ») ou pour diagnostiquer un fichier verrouillé.

### 🟡 Très utile en pratique

#### Diagnostiquer « je n'ai pas accès »

La séquence de dépannage type, qui combine les deux couches :

```powershell
# 1. Le partage existe et quelles permissions SMB ?
Get-SmbShare -Name "Compta"
Get-SmbShareAccess -Name "Compta"

# 2. Quelles permissions NTFS sur le dossier ? (Ch.9)
(Get-Acl "C:\Partages\Compta").Access |
    Select-Object IdentityReference, FileSystemRights, AccessControlType

# 3. L'utilisateur est-il dans le bon groupe ? (Ch.21)
Get-ADGroupMember "GG_Compta" | Where-Object SamAccountName -eq "jdupont"
```

Ce diagnostic croise SMB (ce chapitre), NTFS (Ch.9) et les groupes AD (Ch.21) — une vraie synthèse d'administration.

#### Fermer une session ou un fichier bloqué

```powershell
# Fermer un fichier ouvert (avant maintenance) — force la fermeture côté serveur
Close-SmbOpenFile -FileId <id> -Force

# Fermer une session
Close-SmbSession -SessionId <id> -Force
```

### 🔴 Bonus

#### Partages administratifs cachés

Windows crée des partages cachés (suffixés `$` : `C$`, `ADMIN$`) réservés aux administrateurs. Ils n'apparaissent pas en navigation réseau mais sont accessibles via `\\serveur\C$` :

```powershell
Get-SmbShare | Where-Object Name -like "*$"    # les partages administratifs
```

> **Sécurité :** ces partages administratifs sont utiles pour l'administration distante, mais aussi exploités par les attaquants pour se déplacer latéralement. Leur usage est surveillé en sécurité (Ch.34).

### ❌ Erreur classique

```powershell
# Ne raisonner que sur une seule couche de permissions
# ❌ "j'ai mis Full en partage mais l'utilisateur ne peut pas écrire"
# → vérifier AUSSI les permissions NTFS (l'intersection gagne)

# Créer un partage sans restreindre l'accès
New-SmbShare -Name "X" -Path "C:\X" -FullAccess "Tout le monde"   # ❌ trop ouvert
New-SmbShare -Name "X" -Path "C:\X" -ChangeAccess "lab\GG_X"       # ✅ par groupe

# Supprimer un partage occupé sans prévenir
Remove-SmbShare -Name "Compta"    # ⚠️ vérifier Get-SmbSession avant
```

### 💡 Exercices

**Guidé :** Liste les partages du serveur (hors partages administratifs `$`), avec leur chemin et leur description. Affiche les permissions SMB de l'un d'eux.

**Autonome :** Écris un script qui, pour un partage donné, affiche côte à côte ses permissions SMB (`Get-SmbShareAccess`) et NTFS (`Get-Acl`), pour visualiser les deux couches d'un coup.

### 🧩 Capstone Partie V — Rapport d'infrastructure

Construis `Get-InfraReport.ps1` (à exécuter sur le serveur) qui produit un état des lieux :

- Les GPO du domaine et leurs liens (Ch.25)
- Les zones DNS et le nombre d'enregistrements A (Ch.26)
- Les scopes DHCP et leur taux d'utilisation (Ch.27)
- Les partages SMB et leurs permissions (Ch.28)
- Le tout en sections claires, exporté en CSV (un fichier par domaine) ou en rapport HTML

C'est le type de livrable qu'un administrateur produit pour documenter une infrastructure.

### ✅ Tu sais maintenant...

- Créer et gérer des partages SMB (`*-SmbShare`)
- **La distinction cruciale permissions de partage (SMB) vs NTFS**, et que la plus restrictive gagne
- Voir les sessions et fichiers ouverts (`Get-SmbSession`, `Get-SmbOpenFile`)
- Diagnostiquer un problème d'accès en croisant SMB, NTFS et groupes AD
- Les partages administratifs cachés (`C$`, `ADMIN$`)

### 💬 Questions d'entretien typiques

- **Quelle est la différence entre permissions de partage et NTFS ?** → Le partage (SMB) ne s'applique qu'en accès réseau et reste grossier ; NTFS s'applique toujours et est fin. L'accès effectif est l'intersection (la plus restrictive gagne).
- **Un utilisateur a Full en partage mais ne peut pas écrire, pourquoi ?** → Les permissions NTFS sont probablement plus restrictives ; c'est l'intersection qui compte.
- **Comment savoir qui utilise un partage avant une maintenance ?** → `Get-SmbSession` et `Get-SmbOpenFile`.

---
