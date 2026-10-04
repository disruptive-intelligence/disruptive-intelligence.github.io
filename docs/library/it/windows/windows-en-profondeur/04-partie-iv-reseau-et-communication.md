---
title: Partie IV — Réseau et communication
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - index.md
---

---


## Chapitre 14 — Pile réseau Windows et API

### 14.1 De l'application au câble

```text
Application (navigateur, malware, outil d'admin)
   ↓  API : Winsock, WinHTTP, WinINet
AFD.sys  (pilote d'interface des sockets)
   ↓
tcpip.sys  (TCP/IP)  ←── WFP : filtrage (pare-feu Windows, certains EDR)
   ↓
NDIS  →  pilote de carte réseau
```


Les API de haut niveau (WinHTTP, WinINet, `URLDownloadToFile`) sont celles qu'utilisent aussi bien les applications légitimes que les programmes malveillants pour communiquer : c'est pourquoi la corrélation **processus → connexion** (Sysmon 3, EDR) compte plus que la connexion seule.

### 14.2 Le pare-feu Windows

| Profil | Appliqué quand… |
|---|---|
| **Domaine** | La machine joint un DC de son domaine |
| **Privé** | Réseau marqué comme de confiance |
| **Public** | Tout autre réseau (le plus restrictif) |

Bonnes pratiques : pare-feu actif sur les trois profils, règles **entrantes** limitées au strict nécessaire (le poste n'a pas à accepter SMB ou RDP de tous les autres postes), règles **sortantes** au moins sur les serveurs, journalisation des paquets refusés, gestion centralisée par GPO ou Intune. Un pare-feu local bien réglé freine fortement les déplacements latéraux d'un poste à l'autre.

### 14.3 Voir qui communique

| Commande / outil | Usage |
|---|---|
| `netstat -anob` | Connexions avec PID et binaire (console administrateur) |
| `Get-NetTCPConnection -State Established` | Connexions établies, avec `OwningProcess` |
| `Get-NetUDPEndpoint` | Ports UDP ouverts |
| TCPView (Sysinternals) | Vue graphique en temps réel |
| `Get-NetFirewallRule` / `Get-NetFirewallProfile` | Règles et profils du pare-feu |

En triage, la première question réseau est toujours : **quel processus parle à quelle adresse, et est-ce normal pour lui ?**

---


## Chapitre 15 — SMB, partages et accès distant

### 15.1 SMB en bref

**SMB** (*Server Message Block*, TCP 445) sert au partage de fichiers et d'imprimantes, mais aussi de transport à de nombreuses opérations d'administration (RPC sur canaux nommés, SYSVOL, déploiement).

| Version | Statut |
|---|---|
| **SMBv1** | Obsolète et vulnérable (EternalBlue, WannaCry) : **à désactiver** |
| **SMBv2** | Minimum acceptable |
| **SMBv3** | Recommandé : chiffrement possible, signature plus robuste |

### 15.2 Permissions de partage et permissions NTFS

Un dossier partagé est protégé par **deux** couches :

| Couche | S'applique | Droits |
|---|---|---|
| **Permissions de partage** | Seulement à l'accès **réseau** (`\\serveur\partage`) | Read, Change, Full Control |
| **Permissions NTFS** | À tout accès, local ou réseau | Full Control, Modify, Read & Execute, Read, Write… (Ch.4) |

> **Accès effectif par le réseau = la plus restrictive des deux.** Partage en Full Control et NTFS en Read : l'utilisateur ne peut que lire. Bonne pratique : partage large pour les utilisateurs authentifiés, finesse portée par les droits NTFS.

### 15.3 Les partages administratifs

Windows crée automatiquement des partages cachés (le `$` final les masque de la liste, pas de l'accès) :

| Partage | Cible | Usage |
|---|---|---|
| `C$` (et autres lettres) | Racine de chaque volume | Administration à distance |
| `ADMIN$` | `C:\Windows` | Déploiement, outils d'administration |
| `IPC$` | Communication inter-processus | Canaux nommés, RPC |

Ils sont réservés aux administrateurs locaux. D'où l'importance de LAPS : avec un mot de passe administrateur local commun à tout le parc, un seul poste compromis ouvre `C$` sur tous les autres.

### 15.4 Compte local ou compte de domaine

Avant d'accéder à `\\hôte\partage`, se demander où vit le compte : `MACHINE\utilisateur` pour un compte local (vérifié par la SAM de la machine cible), `DOMAINE\utilisateur` pour un compte de domaine (vérifié via le DC).

### 15.5 Commandes

| Commande | Usage |
|---|---|
| `net share` / `Get-SmbShare` | Lister les partages |
| `Get-SmbShareAccess -Name <partage>` | Permissions de partage |
| `icacls <chemin>` | Permissions NTFS |
| `Get-SmbConnection` / `Get-SmbSession` | Connexions sortantes / sessions entrantes |
| `Get-SmbServerConfiguration` | Versions activées, signature exigée |
| `smbclient -L //<IP> -U <utilisateur>` | Depuis Linux : lister les partages |

### 15.6 Les traces de l'accès distant

Les techniques d'accès distant et leur profil de détection : **PsExec** (crée un service temporaire PSEXESVC — Event 7045 + 4624 type 3 + Sysmon 1 avec psexesvc.exe en child de services.exe), **WMI** (Event 4624 type 3 + 4688 avec parent wmiprvse.exe sur la cible), **WinRM** (PowerShell Remoting — Event 4624 type 3 + 4688 wsmprovhost.exe), **RDP** (Event 4624 type 10 — connexion interactive à distance), **DCOM** (appel COM à distance — mmc.exe, excel.exe comme parent de processus suspect), **schtasks** (tâche planifiée à distance — Event 4698 sur la cible). Chaque technique a un profil de détection différent — connaître ces profils est une compétence SOC fondamentale.

---


## Chapitre 16 — Résolution de noms et protocoles à risque

### 16.1 L'ordre de résolution

Quand Windows cherche l'adresse d'un nom, il essaie dans l'ordre :

```text
1. Fichier hosts (C:\Windows\System32\drivers\etc\hosts) et cache DNS local
2. Serveur DNS
3. En cas d'échec : protocoles de diffusion sur le réseau local (LLMNR, NBT-NS, mDNS)
```


Le cache DNS (`ipconfig /displaydns`) est un artefact volatil utile en triage ; Sysmon 22 journalise les requêtes DNS par processus.

### 16.2 Les protocoles de secours

| Protocole | Port | Principe | Risque |
|---|---|---|---|
| **LLMNR** | UDP 5355 | Question en multicast à tout le segment | N'importe quelle machine peut répondre, et la victime tente de s'authentifier auprès d'elle |
| **NBT-NS** | UDP 137 | Résolution NetBIOS en diffusion | Même risque |
| **mDNS** | UDP 5353 | Résolution multicast (appareils, imprimantes) | Même risque sur les postes |
| **WPAD** | via DHCP, DNS puis protocoles de secours | Découverte automatique du proxy | Un faux serveur peut se déclarer proxy |

Ces mécanismes n'apportent presque rien en entreprise, où le DNS fonctionne. Ils se **désactivent** : LLMNR par GPO (*Turn off multicast name resolution*), NetBIOS sur les interfaces (option DHCP ou réglage de la carte), WPAD par GPO ou en déclarant explicitement le proxy.

### 16.3 Fil rouge

LLMNR et NBT-NS sont actifs sur tout le réseau de Valtec. L'accès initial est ici venu d'un hameçonnage, mais Léa note la faiblesse dans ses recommandations P0.

---
