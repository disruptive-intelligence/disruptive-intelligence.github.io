---
title: Fiche Windows
source: IT/02_Windows/Fiche_Windows.md
---

> Fiche intermédiaire orientée compréhension (eJPT / Hack The Box).
> Objectif : comprendre les mécanismes de sécurité Windows, pas seulement les mémoriser.

---

### 1. Introduction à Windows

#### À retenir
Deux familles : **Windows Desktop** (XP → 11), pour les postes utilisateurs, et **Windows Server** (2000 → 2022), pour l'infrastructure. C'est Server qui introduit les rôles d'entreprise : Active Directory, IIS, partage de fichiers centralisé, services réseau.

#### Comment ça fonctionne
Windows Server étend le noyau Desktop avec des composants d'administration centralisée. En entreprise, un **Domaine** (géré par Active Directory) regroupe les machines sous une authentification et des politiques communes, au lieu de comptes isolés sur chaque poste.

#### Pourquoi c'est important en cyber
La majorité des cibles en entreprise sont Windows. Beaucoup de systèmes **legacy** (anciens, non patchés) restent en production pour des raisons applicatives ou budgétaires : ils concentrent les vulnérabilités connues et sont des points d'entrée privilégiés.

#### Exemple concret
Un serveur Windows Server 2012 toujours en SMBv1 reste exposé à **EternalBlue**, exploit qui a alimenté des campagnes de ransomware (WannaCry).

#### Point clé à mémoriser
Desktop = poste utilisateur, Server = infrastructure ; les vieux systèmes non patchés sont les cibles les plus rentables.

---

### 2. Versions Windows et énumération système

#### À retenir
Chaque version Windows porte un numéro. Repères utiles :

| OS | Version |
| --- | --- |
| Windows 7 / Server 2008 R2 | 6.1 |
| Windows 8 / Server 2012 | 6.2 |
| Windows 10 / Server 2016 / 2019 | 10.0 |

#### Comment ça fonctionne
Le couple **version + build** identifie précisément l'OS. `systeminfo` agrège aussi les correctifs installés (hotfixes), le domaine, la RAM et la carte réseau. WMI (`Get-WmiObject`) interroge les classes système pour obtenir ces infos par script.

#### Pourquoi c'est important en cyber
L'énumération système est la **première étape** d'un test : version, build, patchs et appartenance à un domaine orientent vers les exploits applicables et révèlent si la machine est à jour. C'est aussi utile en inventaire défensif.

#### Exemple concret
Sur une cible, le build `19041` + l'absence de certains hotfixes peut indiquer une vulnérabilité d'élévation de privilèges connue.

#### Commandes utiles

```cmd
systeminfo                  # Vue d'ensemble : OS, build, patchs, domaine
ver                         # Version courte
```

```powershell
Get-WmiObject -Class Win32_OperatingSystem | select Version,BuildNumber
```


#### Point clé à mémoriser
`systeminfo` = réflexe n°1 pour cartographier une cible Windows.

---

### 3. Arborescence Windows

#### À retenir
Racine = `C:\` (partition de démarrage, où l'OS est installé). Au-delà de la liste des dossiers, chacun a un intérêt cyber précis.

#### Comment ça fonctionne

| Dossier                          | Rôle et intérêt cyber                                                                                                                                                                                     |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Windows\System32`               | Binaires et DLL système. **64 bits** sur un OS 64 bits. Cible privilégiée pour repérer ou détourner des binaires légitimes.                                                                               |
| `Windows\SysWOW64`               | Hôte des binaires **32 bits** sur OS 64 bits (redirection WoW64). Nom contre-intuitif.                                                                                                                    |
| `ProgramData` *(caché)*          | Données partagées entre applis, indépendantes de l'utilisateur connecté (licences, caches, settings globaux).                                                                                             |
| `Users\<user>\AppData` *(caché)* | Données par utilisateur : `Roaming` (suit le profil sur le réseau), `Local` (lié à la machine), `LocalLow` (intégrité faible, ex. navigateur en mode protégé). Souvent riche en identifiants applicatifs. |
| `Windows\System32\config`        | Fichiers du **registre** machine (SAM, SYSTEM, SECURITY...). Cible directe pour extraire les secrets locaux.                                                                                              |

**Dossiers inscriptibles intéressants** (dépôt de fichiers en tant qu'utilisateur peu privilégié) :

| Variable            | Chemin                               | Intérêt                                  |
| ------------------- | ------------------------------------ | ---------------------------------------- |
| `%TEMP%`            | `C:\Users\<user>\AppData\Local\Temp` | Écriture par l'utilisateur courant       |
| `%PUBLIC%`          | `C:\Users\Public`                    | Accessible à tous, souvent peu surveillé |
| `%SYSTEMROOT%\Temp` | `C:\Windows\Temp`                    | Lecture/écriture pour tous               |

#### Pourquoi c'est important en cyber
Connaître l'arborescence permet de savoir **où chercher** (identifiants, config, registre) et **où écrire** quand on dispose de droits limités. C'est central en énumération comme en forensic.

#### Commandes utiles

```cmd
dir C:\ /a                  # Lister tout, y compris fichiers cachés
tree C:\ /f | more          # Arborescence complète paginée
```


#### Point clé à mémoriser
System32 = 64 bits, SysWOW64 = 32 bits. AppData et System32\config sont les zones à fouiller.

---

### 4. Systèmes de fichiers : FAT32, exFAT, NTFS

#### À retenir

- **FAT32** : universel mais limité (fichiers < 4 Go, aucune permission ni chiffrement natif).
- **exFAT** : version moderne de FAT pour gros fichiers et supports amovibles.
- **NTFS** : système par défaut de Windows depuis NT 3.1.

#### Comment ça fonctionne
NTFS apporte ce que FAT n'a pas : **permissions granulaires** sur fichiers et dossiers, **journalisation** (chaque ajout/modif/suppression est tracé), support des grandes partitions, et **héritage** des permissions depuis le dossier parent. C'est cette structure qui rend le contrôle d'accès local possible.

#### Pourquoi c'est important en cyber
Les permissions NTFS sont le cœur du contrôle d'accès local : qui peut lire, écrire, exécuter quoi. La journalisation NTFS est précieuse en **forensic** pour reconstituer une chronologie d'événements (fichiers créés, modifiés, supprimés).

#### Exemple concret
Une clé USB en FAT32 ne conserve aucune permission : un fichier sensible copié dessus perd toute protection d'accès.

#### Point clé à mémoriser
NTFS = permissions + journalisation + héritage. C'est ce qui sécurise (ou expose) les fichiers.

---

### 5. Permissions NTFS et icacls

#### À retenir
Permissions principales : `Full Control`, `Modify`, `Read & Execute`, `Read`, `Write`, `List Folder Contents`. Par défaut, fichiers et dossiers **héritent** des permissions de leur parent.

#### Comment ça fonctionne
Chaque objet NTFS possède une liste de permissions (ACL) attachée à des utilisateurs ou groupes. L'héritage évite à l'administrateur de tout définir manuellement : un dossier transmet ses permissions à son contenu, sauf si l'héritage est désactivé. Les dossiers et les fichiers peuvent recevoir des permissions différentes (ex. `List Folder Contents` ne concerne que les dossiers).

Lecture d'une sortie `icacls` :

```
BUILTIN\Users:(RX)              → les utilisateurs ont lecture + exécution
NT AUTHORITY\SYSTEM:(OI)(CI)(F) → SYSTEM a contrôle total, hérité aux objets/conteneurs
```

Codes d'accès : `F` full, `M` modify, `RX` read+execute, `R` read, `W` write.
Codes d'héritage : `(OI)` object inherit, `(CI)` container inherit, `(I)` hérité du parent.

#### Pourquoi c'est important en cyber
Un dossier **inscriptible** contenant le binaire d'un service ou d'une application privilégiée est dangereux : on peut remplacer l'exécutable légitime par un binaire malveillant qui sera lancé avec les droits du service. C'est l'un des chemins d'élévation de privilèges les plus courants.

#### Exemple concret
Si `BUILTIN\Users` a `(W)` sur le dossier d'un service tournant en SYSTEM, un utilisateur standard peut y déposer son propre exécutable et obtenir SYSTEM au prochain démarrage du service.

#### Commandes utiles

```cmd
icacls C:\Windows                 # Lister les permissions d'un dossier
icacls C:\Temp\Test /grant joe:F  # Accorder Full control à "joe"
icacls C:\Temp\Test /remove joe   # Retirer les permissions de "joe"
```


#### Point clé à mémoriser
Un dossier inscriptible sur le chemin d'un binaire privilégié = porte ouverte à l'élévation de privilèges.

---

### 6. SMB, partages réseau et permissions

#### À retenir
**SMB** (Server Message Block, port **445**) partage fichiers et imprimantes sur le réseau. Deux jeux de permissions s'appliquent à un partage : **Share permissions** (accès réseau) et **NTFS permissions** (local + réseau).

#### Comment ça fonctionne
Quand on accède à un partage via le réseau, Windows évalue **les deux** listes et applique **la plus restrictive**. En local (ou en RDP), seules les permissions NTFS comptent. Les partages NTFS étant plus granulaires, ils offrent un contrôle plus fin que les Share permissions.

L'authentification dépend du contexte :

- **Workgroup** : les connexions sont vérifiées contre la **SAM locale** de la machine cible.
- **Domaine** : les connexions sont vérifiées contre **Active Directory** (base centralisée).

#### Pourquoi c'est important en cyber
Les partages mal configurés permettent la propagation de malwares et l'exfiltration de données. Surtout, les **partages administratifs** (`C$`, `ADMIN$`, `IPC$`) sont actifs par défaut : `C$` expose toute la partition système à qui possède les droits adéquats.

#### Exemple concret
Depuis une machine Linux, `smbclient -L <IP> -U <user>` liste les partages ; si `Company Data` est accessible en lecture au groupe `Everyone`, son contenu est consultable à distance.

#### Commandes utiles

```cmd
net share                              # Lister les partages locaux
```

```bash
smbclient -L <IP> -U <user>            # Lister les partages distants (Linux)
smbclient '\\<IP>\Company Data' -U <user>
sudo mount -t cifs -o username=<user> //<IP>/"share" /mnt/point
```


#### Point clé à mémoriser
SMB = port 445 ; partages par défaut `C$`, `ADMIN$`, `IPC$` ; entre Share et NTFS, la plus restrictive gagne.

---

### 7. Services Windows

#### À retenir
Un **service** est un processus long, qui démarre au boot sans session ouverte et tourne en arrière-plan (réseau, diagnostics, mises à jour...). Il est piloté par le **SCM** (Service Control Manager).

#### Comment ça fonctionne
Chaque service a :

- un **état** : `Running`, `Stopped`, `Paused` ;
- un **type de démarrage** : `Automatic`, `Automatic (Delayed)`, `Manual`, `Disabled` ;
- un **compte d'exécution** (souvent LocalSystem) ;
- un **`BINARY_PATH_NAME`** : le chemin de l'exécutable lancé.

Seuls les administrateurs peuvent normalement créer ou modifier un service. Mais une mauvaise configuration (permissions trop larges, chemin inscriptible) ouvre des failles.

#### Pourquoi c'est important en cyber
Les permissions de service sont un **vecteur classique d'élévation de privilèges et de persistance**. Si un utilisateur peut modifier le `BINARY_PATH_NAME` ou remplacer le binaire pointé, il fait exécuter son code avec les privilèges du service (souvent SYSTEM). C'est aussi un point d'analyse SOC : un service au chemin suspect doit alerter.

#### Exemple concret

```cmd
sc qc wuauserv
# BINARY_PATH_NAME : C:\WINDOWS\system32\svchost.exe -k netsvcs
# SERVICE_START_NAME : LocalSystem
```

Si ce chemin pointait vers un binaire inhabituel dans un dossier inscriptible, ce serait un signe de compromission ou une opportunité d'élévation.

#### Commandes utiles

```cmd
sc qc <service>             # Config : binaire, compte, démarrage
sc query <service>          # État
sc stop <service>           # Stopper (nécessite admin)
```

```powershell
Get-Service | ? {$_.Status -eq "Running"}
```


#### Point clé à mémoriser
Toujours vérifier `BINARY_PATH_NAME` et le compte d'exécution d'un service.

---

### 8. Processus Windows importants

#### À retenir
Certains processus sont critiques : les connaître permet de **repérer les imposteurs** (malwares qui usurpent un nom légitime).
Gère services système qui s’exécutent à partir de .dll, tels que 
#### Comment ça fonctionne

| Processus      | Rôle                                                                        | À vérifier en analyse                                                   |
| -------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `lsass.exe`    | Authentifie les connexions, crée les jetons d'accès, gère les mots de passe | Un seul instance, chemin `System32`, pas de faute de frappe             |
| `svchost.exe`  | Héberge les services tournant à partir de DLL                               | Chemin, signature, processus parent (`services.exe`), services hébergés |
| `services.exe` | Démarre/arrête les services (le SCM)                                        | Parent = `wininit.exe`                                                  |
| `winlogon.exe` | Charge le profil à la connexion, gère le verrouillage                       | Chemin légitime                                                         |
| `smss.exe`     | Gestion des sessions (Session Manager)                                      | Premier processus utilisateur lancé                                     |
| `csrss.exe`    | Sous-système Windows en mode utilisateur                                    | Présence multiple normale                                               |
| `System`       | Exécute le noyau Windows                                                    | PID 4, pas un fichier sur disque                                        |

#### Pourquoi c'est important en cyber
Les malwares se déguisent souvent en processus système (`svchost.exe`, ou `scvhost.exe` avec une faute volontaire) pour passer inaperçus. Vérifier le **chemin**, la **signature** et le **processus parent** permet de distinguer le légitime de l'imposteur. Essentiel en SOC et forensic.

#### Exemple concret
Un `svchost.exe` lancé depuis `C:\Users\bob\AppData\` (au lieu de `System32`) et sans parent `services.exe` est presque certainement malveillant.

#### Point clé à mémoriser
`svchost.exe` est souvent imité ou abusé : vérifier chemin, signature, parent et services hébergés.

---

### 9. Comptes de service

#### À retenir
Trois comptes intégrés non-interactifs servent à exécuter les services :

| Compte                                  | Privilèges                                                           |
| --------------------------------------- | -------------------------------------------------------------------- |
| **LocalSystem** (`NT AUTHORITY\SYSTEM`) | Compte le plus puissant de la machine, au-dessus des admins locaux   |
| **NetworkService**                      | Droits locaux limités, présente l'**identité machine** sur le réseau |
| **LocalService**                        | Droits locaux limités, identité **anonyme** sur le réseau            |

#### Comment ça fonctionne
La différence se joue sur deux plans : les **droits locaux** (élevés pour LocalSystem, limités pour les deux autres) et l'**identité réseau** (machine pour NetworkService, anonyme pour LocalService). SYSTEM dépasse l'administrateur local car il agit au niveau du système d'exploitation lui-même, sans les restrictions appliquées aux comptes utilisateurs.

#### Pourquoi c'est important en cyber
Le **principe du moindre privilège** veut qu'un service ne tourne pas en LocalSystem s'il n'en a pas besoin. Un service privilégié mal sécurisé devient un tremplin vers SYSTEM. Côté offensif, obtenir SYSTEM = contrôle total de la machine.

#### Exemple concret
Une application de monitoring installée par défaut en LocalSystem alors qu'un compte limité suffirait : si son binaire est modifiable, l'attaquant hérite directement de SYSTEM.

#### Point clé à mémoriser
SYSTEM > Administrateur local. Obtenir SYSTEM, c'est obtenir toute la machine.

---

### 10. Sessions Windows

#### À retenir

- **Session interactive** : un utilisateur saisit ses identifiants (connexion locale, RDP, ou `runas`).
- **Session non-interactive** : comptes système sans mot de passe classique, utilisés pour lancer services et tâches planifiées.

#### Comment ça fonctionne
Une session interactive démarre par une authentification explicite et ouvre un environnement de travail (`explorer.exe` et son token). Une session non-interactive est créée automatiquement par l'OS au démarrage pour exécuter les services en arrière-plan, sans intervention humaine. **RDP** (port 3389) ouvre une session interactive distante avec interface graphique ; **`runas`** lance un programme sous une autre identité.

#### Pourquoi c'est important en cyber
Distinguer les deux aide à comprendre comment les services s'exécutent et quels comptes sont exploitables sans identifiants. RDP est un vecteur d'accès distant fréquent (recherche de fichiers `.rdp` sauvegardés en pentest).

#### Point clé à mémoriser
Interactive = un humain s'authentifie ; non-interactive = l'OS lance des services sans mot de passe classique.

---

### 11. SID, Access Token, ACL, ACE, DACL, SACL

#### À retenir
Le cœur du modèle de sécurité Windows : **qui** agit (SID), avec **quels droits** (token), sur **quel objet** (protégé par une ACL).

#### Comment ça fonctionne

**SID (Security Identifier)** : identifiant unique d'un principal de sécurité (utilisateur, groupe, machine). Généré automatiquement, il rend deux comptes au même nom distinguables.

```
S-1-5-21-674899381-4069889467-2080702030-1002
│ │ │  └──── SID domaine/machine ────┘  └─ RID
│ │ └── Identifier-authority (5 = NT Authority)
│ └──── Revision (toujours 1)
└────── "S" = SID
```

**RID (Relative ID)** : la dernière partie du SID, qui distingue un compte des autres. **RID 500 = le vrai Administrateur**, **RID 1000+ = utilisateurs normaux**.

**Access Token** : à la connexion, après vérification par LSASS, Windows crée un jeton attaché à la session. Il contient le **SID de l'utilisateur**, les **SIDs de ses groupes**, ses **privilèges** et son **niveau d'intégrité**. Ce token est hérité par les processus lancés : `explorer.exe` en transmet une copie à chaque programme ouvert.

**ACL / ACE / DACL / SACL** : chaque objet sécurisable (fichier, clé de registre, service...) possède un **Security Descriptor** contenant :

- une **DACL** (Discretionary ACL) : la liste des **ACE** (Access Control Entries), chacune disant « tel SID → Allow/Deny telles opérations ». C'est elle qui décide de l'accès.
- une **SACL** (System ACL) : définit ce qui est **audité/journalisé** (succès/échecs d'accès).

**Décision d'accès** : à chaque tentative, Windows compare le **token** du processus à la **DACL** de l'objet, et applique les ACE pour décider **Allow ou Deny**.

#### Pourquoi c'est important en cyber
Comprendre cette chaîne, c'est comprendre comment Windows autorise ou refuse une action — donc où chercher des **failles de permissions** et quels comptes privilégiés repérer (via leurs SID/RID). C'est le socle de l'élévation de privilèges et de l'analyse d'accès.

#### Exemple concret
Bob (token avec SID `...-1002`, groupe Users) tente d'écrire dans un fichier dont la DACL n'autorise l'écriture qu'aux Administrators. Windows compare, ne trouve pas de SID correspondant côté Allow → **accès refusé**.

#### Commandes utiles

```cmd
whoami /user                # SID du compte courant
whoami /groups              # SIDs des groupes
whoami /priv                # Privilèges actifs
```


#### Point clé à mémoriser
Token (qui je suis + ce que je peux) comparé à DACL (qui a droit à quoi) = décision Allow/Deny. RID 500 = vrai Administrateur.

---

### 12. SAM, LSA et LSASS

#### À retenir

- **SAM** : base locale des comptes et de leurs secrets (hashes).
- **LSA** : l'autorité de sécurité qui valide identités et jetons.
- **LSASS** : le processus qui applique tout ça en mémoire.

#### Comment ça fonctionne
La **SAM** (`C:\Windows\System32\config\SAM`, clé dans registre `HKLM\SAM`) stocke les comptes **locaux** et leurs hashes. Elle est **chiffrée par une clé rangée dans le fichier SYSTEM** : la SAM seule est inutilisable, il faut **SAM + SYSTEM** pour en extraire les secrets. En environnement **domaine**, les comptes sont dans Active Directory (`NTDS.dit`) ; la SAM locale ne gère alors que les comptes locaux.

La **LSA** fournit à l'authentification les identités (SID) et secrets, et valide les access tokens. **LSASS** (`lsass.exe`) est le processus qui exécute cette politique : il vérifie chaque connexion, crée les tokens et gère les changements de mot de passe.

Pour permettre le **SSO** (ne pas retaper son mot de passe), Windows garde des identifiants en mémoire dans LSASS : hashes **NTLM**, tickets **Kerberos**, et parfois mots de passe en clair sur d'anciens systèmes (**WDigest**).

#### Pourquoi c'est important en cyber
LSASS est une **cible de haute valeur** : sa mémoire contient des identifiants réutilisables pour se déplacer latéralement sur le réseau. En forensic, l'accès à la SAM ou à la mémoire LSASS est un indicateur fort de compromission ; en durcissement, désactiver WDigest et protéger LSASS (Credential Guard) sont des mesures clés.

#### Exemple concret
Sauvegarder les ruches pour analyse hors ligne nécessite les deux fichiers liés :

```cmd
reg save HKLM\sam sam.save
reg save HKLM\system system.save
```

Sans `system.save`, la SAM reste illisible.

#### Point clé à mémoriser
Pour exploiter la SAM, il faut SAM **et** SYSTEM. LSASS garde des identifiants sensibles en mémoire.

> La SAM ne peut pas être copiée tant que Windows tourne → on passe par les **Volume Shadow Copies**.

---

### 13. Registre Windows

#### À retenir
Base de données hiérarchique de configuration de l'OS et des applications. Structure : **clés** (dossiers) → **sous-clés** → **valeurs** (données).

#### Comment ça fonctionne
Le registre est organisé en **ruches (hives)**, dont les principales :

| Ruche                          | Contenu                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------- |
| **HKLM** (HKEY_LOCAL_MACHINE)  | Config machine globale : services, pilotes, SAM, SYSTEM, SOFTWARE               |
| **HKCU** (HKEY_CURRENT_USER)   | Config de l'utilisateur courant : préférences, programmes au démarrage          |
| **HKU** (HKEY_USERS)           | Tous les profils chargés (un SID par utilisateur) ; HKCU pointe vers l'un d'eux |
| **HKCR** (HKEY_CLASSES_ROOT)   | Associations de fichiers et COM                                                 |
| **HKCC** (HKEY_CURRENT_CONFIG) | Config matérielle courante                                                      |

Physiquement, les ruches machine sont dans `C:\Windows\System32\config\` (SAM, SYSTEM, SOFTWARE...) et la ruche utilisateur dans `C:\Users\<user>\NTUSER.DAT`. Types de valeurs courants : `REG_SZ` (chaîne), `REG_DWORD` (entier 32 bits), `REG_BINARY` (données brutes), `REG_EXPAND_SZ` (chaîne avec variables).

#### Pourquoi c'est important en cyber
Le registre stocke des paramètres de sécurité, des points de persistance et parfois des identifiants. C'est un terrain d'analyse forensic central et un levier de durcissement.

#### Commandes utiles

```cmd
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
regedit                     # Éditeur graphique
```


#### Point clé à mémoriser
HKLM = machine (global), HKCU = utilisateur courant. Les fichiers sont sous `System32\config` et `NTUSER.DAT`.

---

### 14. Run / RunOnce

#### À retenir
Clés de registre qui lancent des programmes **automatiquement** au démarrage ou à l'ouverture de session.

```
HKLM\Software\Microsoft\Windows\CurrentVersion\Run
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
HKLM\...\CurrentVersion\RunOnce
HKCU\...\CurrentVersion\RunOnce
```


#### Comment ça fonctionne

- Les clés sous **HKLM** s'exécutent pour **tous les utilisateurs** au démarrage de la machine.
- Les clés sous **HKCU** s'exécutent **à l'ouverture de session** de l'utilisateur concerné.
- **Run** relance le programme à chaque fois ; **RunOnce** le supprime après une exécution.

#### Pourquoi c'est important en cyber
C'est un mécanisme de **persistance** classique : ajouter une valeur pointant vers un binaire le fait relancer automatiquement. En réponse à incident, vérifier les clés Run/RunOnce fait partie des premiers réflexes pour repérer un programme indésirable qui se relance seul.

#### Exemple concret
Une valeur `Updater → C:\Users\Public\update.exe` dans `HKCU\...\Run` qui ne correspond à aucun logiciel installé est un signe de persistance à investiguer.

#### Commandes utiles

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```


#### Point clé à mémoriser
Run/RunOnce = persistance classique à vérifier en priorité.

---

### 15. UAC (User Account Control)

#### À retenir
Fonctionnalité empêchant un programme d'effectuer des actions privilégiées **sans confirmation explicite**, même lancé par un administrateur.

#### Comment ça fonctionne
Avec l'**Admin Approval Mode**, un administrateur travaille par défaut avec un token **standard** (privilèges réduits). Quand une action nécessite des droits élevés (installation, modif système), une **invite de consentement** apparaît : l'utilisateur doit confirmer, ce qui « élève » le programme vers un token administrateur complet. Un utilisateur standard, lui, doit fournir un mot de passe admin.

C'est ici la distinction clé : **être administrateur** ne signifie pas **s'exécuter en contexte élevé**. Tant que l'élévation n'a pas eu lieu, le programme tourne avec des droits limités.

#### Pourquoi c'est important en cyber
L'UAC interrompt l'exécution silencieuse de scripts ou binaires malveillants jusqu'à confirmation. Mais ce **n'est pas une frontière de sécurité absolue** : il existe des techniques de contournement (UAC bypass). Côté durcissement, il faut le configurer correctement sans s'y fier comme unique protection.

#### Exemple concret
Un script lancé par un admin qui tente de modifier le système déclenche l'invite UAC : sans clic de confirmation, l'action est bloquée.

#### Point clé à mémoriser
Administrateur ≠ contexte élevé. L'UAC ralentit l'abus mais se contourne ; ce n'est pas une barrière infranchissable.

---

### 16. CMD, PowerShell et commandes essentielles

#### À retenir

- **CMD** : interpréteur classique pour commandes ponctuelles et scripts simples.
- **PowerShell** : plus puissant, basé sur .NET, utilise des **cmdlets** (`Verbe-Nom`, ex. `Get-Service`).
- **Execution Policy** : limite l'exécution de scripts (`Restricted`, `RemoteSigned`, `Bypass`...). Ce **n'est pas une vraie barrière de sécurité** : elle se contourne en une ligne.

#### Commandes utiles

**Système** — énumération de base

```cmd
systeminfo / ver / set
```

**Réseau** — cartographier connexions et résolution

```cmd
ipconfig /all               # Infos réseau complètes
netstat -abon               # Connexions + ports + PID + programme
nslookup example.com        # Résolution DNS
```

**Fichiers** — navigation et lecture

```cmd
dir / cd / tree / type
```

**Processus** — lister et arrêter

```cmd
tasklist                    # Processus en cours
tasklist /FI "imagename eq sshd.exe"
taskkill /PID <pid>
```

**PowerShell** — services, objets, contournement de policy

```powershell
Get-Service / Get-Process
Get-ChildItem -Recurse
Set-ExecutionPolicy Bypass -Scope Process   # Pour la session courante
```


#### Point clé à mémoriser
`netstat -abon` pour le réseau, `tasklist`/`taskkill` pour les processus. L'Execution Policy ne protège pas vraiment.

---

### 17. Outils utiles : Task Manager et Sysinternals

#### À retenir
La suite **Sysinternals** (sans installation) complète le Task Manager pour l'analyse fine des processus, du réseau et de la persistance.

#### Comment ça fonctionne

| Outil | Usage | Intérêt cyber |
| --- | --- | --- |
| **Task Manager** | Processus, services, perfs, programmes au démarrage | Repérage rapide d'un processus anormal |
| **Process Explorer** | Task Manager amélioré : hiérarchie parent/enfant, handles, DLL, signatures | Identifier un imposteur via son parent et sa signature |
| **Process Monitor (Procmon)** | Traces temps réel FS / Registre / Réseau | Suivre ce qu'un binaire touche réellement |
| **TCPView** | Connexions réseau actives par processus | Détecter une connexion sortante suspecte |
| **PsExec** | Exécution de commandes à distance via SMB (admin) | Mouvement latéral / administration distante |

#### Pourquoi c'est important en cyber
Ces outils servent autant à l'**analyse SOC** (repérer un processus ou une connexion malveillante) qu'à la **reconnaissance en pentest** (trouver des chemins d'élévation, observer le comportement d'un binaire). Sans installation, ils s'utilisent même sur une machine compromise.

#### Commandes utiles

```cmd
\\live.sysinternals.com\tools\procdump.exe -accepteula
```


#### Point clé à mémoriser
Process Explorer pour parent/enfant, Procmon pour le temps réel, TCPView pour le réseau, PsExec pour le distant.

---

## Synthèse mentale

Tout le modèle de sécurité Windows tient dans une chaîne :

> **Utilisateur** → s'authentifie → **LSASS** vérifie l'identité (contre la **SAM** en local, ou Active Directory en domaine) → Windows crée un **access token** → ce token contient le **SID**, les **groupes** et les **privilèges** → l'utilisateur tente d'accéder à un **objet** (fichier, service, clé de registre) → Windows compare le token à la **DACL** de l'objet → **autorisation ou refus**.

Tout le reste s'y rattache : les **services** s'exécutent avec un compte (souvent SYSTEM) et donc un token privilégié ; les **permissions NTFS** définissent les DACL des fichiers ; le **registre** stocke la config et des points de **persistance** (Run/RunOnce) ; **LSASS** garde en mémoire les secrets qui rendent ce SSO possible — et en fait une cible. Comprendre cette chaîne, c'est comprendre où chercher une faille et comment Windows décide.

---

## Commandes à connaître par cœur

```cmd
systeminfo                            # Cartographie de la cible
whoami /user                          # SID du compte courant
whoami /groups                        # SIDs des groupes
whoami /priv                          # Privilèges actifs
ipconfig /all                         # Réseau
netstat -abon                         # Connexions + ports + PID
tasklist                              # Lister les processus
taskkill /PID <pid>                   # Tuer un processus
net share                             # Partages locaux
icacls <dossier>                      # Permissions NTFS
sc qc <service>                       # Config d'un service
reg query HKCU\...\CurrentVersion\Run # Persistance
```

```powershell
Get-Service | ? {$_.Status -eq "Running"}
Get-WmiObject -Class Win32_OperatingSystem | select Version,BuildNumber
```


---

## Erreurs fréquentes à éviter

- Croire que **System32 = 32 bits** → c'est **64 bits** (SysWOW64 = 32 bits).
- Confondre **NTFS permissions** et **Share permissions** → les deux s'appliquent, la plus restrictive gagne.
- Penser que l'**Execution Policy** PowerShell ou l'**UAC** sont des protections infranchissables → ils se contournent.
- Vouloir exploiter la **SAM seule** → il faut **SAM + SYSTEM**.
- Oublier que **SYSTEM est plus puissant qu'Administrateur**.
- Confondre **être administrateur** et **s'exécuter en contexte élevé** (UAC).
- Ignorer les **partages par défaut** (`C$`, `ADMIN$`) en énumération.
- Négliger les clés **Run/RunOnce** en analyse de persistance.

---

## Résumé ultra-court pour entretien

> Windows fonde sa sécurité sur les **SID** (identifiants uniques), les **access tokens** (qui portent SID, groupes et privilèges d'une session) et les **ACL/DACL** (qui décident, par comparaison avec le token, l'accès à chaque objet). L'authentification passe par **LSASS**, qui vérifie l'identité contre la **SAM** locale (ou Active Directory en domaine) et garde des identifiants en mémoire — ce qui en fait une cible de vol. Les **services** tournent souvent en **LocalSystem** : leurs mauvaises permissions sont un vecteur d'élévation vers SYSTEM. La **persistance** se cache dans le **registre** (clés Run/RunOnce) ou dans des services. **SMB** (port 445) gère les partages, avec des partages administratifs (`C$`, `ADMIN$`) actifs par défaut. L'**UAC** ralentit l'abus de privilèges mais n'est pas une barrière absolue.

---

## Mini quiz

1. Quelle commande donne une vue d'ensemble du système (OS, build, patchs) ?
2. System32 contient-il les binaires 32 ou 64 bits ?
3. Quel port utilise SMB ?
4. Quels sont les trois partages administratifs activés par défaut ?
5. Que contient un access token ?
6. Quel RID correspond toujours au vrai compte Administrateur ?
7. Quels deux fichiers faut-il pour exploiter la SAM ?
8. Quel processus est responsable de l'authentification et garde les identifiants en mémoire ?
9. Quelles clés de registre sont à vérifier en priorité pour détecter une persistance ?
10. Entre NTFS et Share permissions, laquelle l'emporte quand les deux s'appliquent ?
11. Pourquoi SYSTEM est-il plus puissant qu'un administrateur local ?
12. Comment Windows décide-t-il d'autoriser ou refuser un accès à un objet ?
13. Quelle est la différence entre une session interactive et non-interactive ?
14. L'UAC est-il une barrière de sécurité infranchissable ? Pourquoi ?
15. Où sont stockés physiquement les fichiers du registre machine ?

## Windows — Processus, Services et Sécurité

> Objectif : comprendre les mécanismes Windows utiles en cybersécurité : processus, services, LSASS, tokens, SID, ACL, registre, permissions de services, persistance et protections natives.

---

### 0. Vue d’ensemble

Windows exécute des programmes sous forme de **processus**. Chaque processus tourne dans un contexte précis : utilisateur, privilèges, espace mémoire, fichiers ouverts, DLL chargées, connexions réseau, etc.

Les **services Windows** sont des processus particuliers : ils sont conçus pour tourner longtemps, souvent en arrière-plan, parfois dès le démarrage de la machine et sans session utilisateur ouverte.

Côté sécurité, Windows s’appuie sur plusieurs notions centrales :

- **SID** : identifiant unique d’un utilisateur, groupe, machine ou service.
    
- **Access token** : “badge” attaché aux processus pour représenter les droits de l’utilisateur.
    
- **ACL / ACE / DACL / SACL** : règles d’accès appliquées aux objets sécurisables.
    
- **LSASS** : processus critique chargé de l’authentification et de la politique de sécurité locale.
    
- **Registre** : base de configuration de Windows, souvent utilisée pour les services, la sécurité et la persistance.
    

> Idée clé : pour comprendre Windows en cyber, il faut comprendre la chaîne suivante :
> 
> **Utilisateur → authentification → token → processus → accès aux objets → DACL → autorisation ou refus**.

---

## 1. Programmes, processus et threads

### 1.1 Programme vs processus

Un **programme** est un fichier présent sur le disque, par exemple :

```text
C:\Windows\System32\notepad.exe
C:\Windows\System32\cmd.exe
C:\Program Files\Google\Chrome\Application\chrome.exe
```


Un programme ne fait rien tant qu’il n’est pas exécuté.

Quand Windows lance ce programme, il crée un **processus**.

Un **processus** est donc une instance d’un programme en cours d’exécution.

Exemple :

- `notepad.exe` sur disque = programme.
    
- `notepad.exe` lancé en mémoire = processus.
    

Un même programme peut avoir plusieurs processus en même temps. Exemple : plusieurs fenêtres Chrome peuvent correspondre à plusieurs processus `chrome.exe`.

---

### 1.2 Ce que contient un processus

|Élément|Rôle|
|---|---|
|**PID**|Identifiant unique du processus.|
|**PPID**|PID du processus parent.|
|**Nom**|Nom du processus, ex : `lsass.exe`, `svchost.exe`.|
|**Chemin**|Emplacement du binaire lancé.|
|**Command line**|Commande complète utilisée pour lancer le processus.|
|**Utilisateur**|Compte sous lequel le processus tourne.|
|**Access token**|Droits et privilèges du processus.|
|**Threads**|Unités d’exécution à l’intérieur du processus.|
|**Handles**|Références vers fichiers, clés registre, sockets, mutex, etc.|
|**DLL chargées**|Bibliothèques utilisées par le processus.|

---

### 1.3 Thread

Un **thread** est une unité d’exécution à l’intérieur d’un processus.

Un processus peut contenir un ou plusieurs threads.

Résumé simple :

- **Programme** = fichier sur disque.
    
- **Processus** = programme en cours d’exécution.
    
- **Thread** = fil d’exécution à l’intérieur du processus.
    

Exemple mental :

```text
Programme = recette de cuisine
Processus = cuisinier qui exécute la recette
Thread = tâche précise effectuée par le cuisinier
```


---

### 1.4 Processus parent / enfant

Quand un processus lance un autre processus, il devient son **parent**.

Exemple :

```text
explorer.exe → cmd.exe → powershell.exe
```


Ici :

- `explorer.exe` lance `cmd.exe` ;
    
- `cmd.exe` lance `powershell.exe`.
    

Cette relation parent/enfant est très importante en analyse SOC et forensic.

Exemples suspects :

```text
winword.exe → powershell.exe
excel.exe → cmd.exe
outlook.exe → wscript.exe
browser.exe → rundll32.exe
```


Ce type de chaîne peut indiquer une macro malveillante, un phishing ou une exécution indirecte de payload.

---

### 1.5 Commandes utiles pour les processus

```powershell
Get-Process
Get-Process -Id <PID> | Format-List *
```


```cmd
tasklist
tasklist /svc
```


```powershell
Get-CimInstance Win32_Process | Select-Object ProcessId, ParentProcessId, Name, ExecutablePath, CommandLine
```


```cmd
wmic process get processid,parentprocessid,executablepath,commandline
```


---

### 1.6 Intérêt cyber des processus

Comprendre les processus permet de :

- repérer un processus suspect ;
    
- analyser une chaîne parent/enfant ;
    
- identifier un faux processus système ;
    
- voir quel utilisateur a lancé quoi ;
    
- comprendre les privilèges associés à un processus ;
    
- repérer des processus qui communiquent sur le réseau ;
    
- détecter une exécution anormale, par exemple `powershell.exe` lancé par Word ;
    
- comprendre les attaques sur LSASS ou les abus de services.
    

---

## 2. Processus système critiques

|Processus|Rôle|
|---|---|
|`System`|Processus système lié au noyau Windows.|
|`smss.exe`|Session Manager Subsystem. Gère l’initialisation des sessions.|
|`csrss.exe`|Client/Server Runtime Subsystem. Partie user-mode du sous-système Windows.|
|`wininit.exe`|Lance des composants critiques au démarrage du système.|
|`services.exe`|Processus du Service Control Manager. Gère le démarrage et l’arrêt des services.|
|`winlogon.exe`|Gère la connexion utilisateur, le verrouillage et le chargement du profil.|
|`lsass.exe`|Local Security Authority Subsystem Service. Authentification, politique de sécurité, tokens.|
|`svchost.exe`|Hôte de services Windows basés sur des DLL.|
|`explorer.exe`|Shell utilisateur : bureau, barre des tâches, explorateur.|

---

### 2.1 svchost.exe

`svchost.exe` signifie **Service Host**.

Son rôle : héberger des services Windows qui sont fournis sous forme de DLL.

Problème : une DLL ne peut pas se lancer toute seule comme un `.exe`.

Solution : Windows utilise `svchost.exe` comme processus hôte pour charger et exécuter ces services.

Exemples de services pouvant être hébergés via `svchost.exe` :

- Windows Update ;
    
- pare-feu Windows ;
    
- Plug and Play ;
    
- services réseau ;
    
- RPC ;
    
- DCOM.
    

Voir les services associés à chaque `svchost.exe` :

```cmd
tasklist /svc
```


Avec PowerShell :

```powershell
Get-CimInstance Win32_Service | Select-Object Name, ProcessId, State, StartName, PathName
```


#### Focus cyber

`svchost.exe` est souvent imité par des malwares.

Exemples de faux noms :

```text
scvhost.exe
svhost.exe
svch0st.exe
svchosts.exe
```


Points à vérifier :

- chemin du binaire ;
    
- signature numérique ;
    
- processus parent ;
    
- compte utilisateur ;
    
- connexions réseau ;
    
- services hébergés.
    

Un vrai `svchost.exe` se trouve normalement ici :

```text
C:\Windows\System32\svchost.exe
```


---

## 3. Focus LSASS

### 3.1 Définition

`lsass.exe` signifie **Local Security Authority Subsystem Service**.

C’est un processus critique de Windows chargé d’appliquer la politique de sécurité locale.

Il intervient notamment dans :

- l’authentification des utilisateurs ;
    
- la vérification des identifiants ;
    
- la création ou la gestion des access tokens ;
    
- les changements de mots de passe ;
    
- la journalisation des événements de connexion/déconnexion ;
    
- la gestion de certains secrets d’authentification.
    

---

### 3.2 LSASS et authentification

Quand un utilisateur se connecte :

1. l’utilisateur saisit ses identifiants ;
    
2. Windows transmet la demande au sous-système de sécurité ;
    
3. LSASS vérifie l’identité ;
    
4. si l’authentification réussit, Windows crée un access token ;
    
5. ce token est attaché aux processus de l’utilisateur.
    

Schéma simplifié :

```text
Login user
   ↓
LSASS vérifie l’identité
   ↓
Création d’un access token
   ↓
Lancement de la session utilisateur
   ↓
Les processus héritent du token
```


---

### 3.3 Pourquoi LSASS est une cible critique ?

LSASS peut contenir en mémoire des informations sensibles liées à l’authentification.

Selon la version de Windows, la configuration et les protections activées, on peut y trouver :

- hashes NTLM ;
    
- tickets Kerberos ;
    
- secrets liés au SSO ;
    
- informations de session ;
    
- parfois mots de passe en clair sur anciens systèmes ou configurations faibles.
    

C’est pourquoi LSASS est une cible majeure pour le vol d’identifiants.

---

### 3.4 Logs associés

Les événements liés aux connexions sont journalisés dans le journal **Security** de Windows.

|Event ID|Signification|
|---|---|
|4624|Connexion réussie.|
|4625|Échec de connexion.|
|4634|Déconnexion.|
|4648|Connexion avec identifiants explicites.|
|4672|Privilèges spéciaux attribués à une nouvelle connexion.|
|4688|Création de processus, si l’audit est activé.|

---

### 3.5 Protections autour de LSASS

Protections utiles :

- **Credential Guard** : isole certains secrets d’authentification via Virtualization-Based Security.
    
- **LSA Protection / RunAsPPL** : limite l’accès non autorisé à LSASS.
    
- **Defender / EDR** : surveille les tentatives de dump ou d’accès suspect à LSASS.
    
- **Réduction des privilèges admin** : moins d’utilisateurs capables d’interagir avec LSASS.
    
- **Désactivation de WDigest** sur anciens systèmes.
    

Commandes utiles :

```powershell
Get-Process lsass
Get-Process lsass | Format-List *
```


---

## 4. Services Windows

### 4.1 Définition

Un **service Windows** est un composant conçu pour exécuter une tâche en arrière-plan, souvent pendant longtemps.

Un service peut :

- démarrer automatiquement au boot ;
    
- tourner sans utilisateur connecté ;
    
- continuer à fonctionner après la déconnexion d’un utilisateur ;
    
- exécuter des fonctions système critiques ;
    
- être lancé sous un compte spécifique.
    

Exemples de fonctions gérées par des services :

- réseau ;
    
- mises à jour Windows ;
    
- diagnostic système ;
    
- journalisation ;
    
- authentification ;
    
- impression ;
    
- antivirus ;
    
- supervision.
    

---

### 4.2 Service Control Manager — SCM

Les services sont gérés par le **Service Control Manager** ou **SCM**.

Le SCM permet de :

- lister les services ;
    
- démarrer un service ;
    
- arrêter un service ;
    
- modifier la configuration d’un service ;
    
- gérer les dépendances ;
    
- définir le compte d’exécution ;
    
- définir le mode de démarrage.
    

Le processus associé au SCM est :

```text
services.exe
```


---

### 4.3 Où gérer les services ?

#### Interface graphique

```text
services.msc
```


Permet de voir :

- nom du service ;
    
- description ;
    
- état ;
    
- type de démarrage ;
    
- chemin de l’exécutable ;
    
- compte d’exécution ;
    
- dépendances ;
    
- options de récupération.
    

#### Ligne de commande CMD

```cmd
sc query
sc qc <ServiceName>
sc start <ServiceName>
sc stop <ServiceName>
```


#### PowerShell

```powershell
Get-Service
Start-Service <ServiceName>
Stop-Service <ServiceName>
Restart-Service <ServiceName>
```


Pour plus de détails que `Get-Service` :

```powershell
Get-CimInstance Win32_Service | Select-Object Name, State, StartMode, StartName, PathName
```


---

### 4.4 États d’un service

|État|Signification|
|---|---|
|`Running`|Service en cours d’exécution.|
|`Stopped`|Service arrêté.|
|`Paused`|Service suspendu.|
|`Start Pending`|Service en cours de démarrage.|
|`Stop Pending`|Service en cours d’arrêt.|

---

### 4.5 Modes de démarrage

|Mode|Signification|
|---|---|
|`Automatic`|Démarre automatiquement au boot.|
|`Automatic (Delayed Start)`|Démarre automatiquement avec un délai.|
|`Manual`|Démarre seulement si demandé.|
|`Disabled`|Ne peut pas démarrer tant qu’il reste désactivé.|

---

### 4.6 Comptes d’exécution des services

Un service tourne sous un compte. Ce compte détermine ses droits locaux et réseau.

|Compte|Description|
|---|---|
|`LocalSystem`|Privilèges très élevés sur la machine locale. À éviter si non nécessaire.|
|`NetworkService`|Droits locaux limités, identité de la machine sur le réseau.|
|`LocalService`|Droits locaux limités, identité anonyme sur le réseau.|
|Compte de service dédié|Compte spécifique créé pour faire tourner un service. Recommandé pour les services applicatifs.|
|gMSA|Group Managed Service Account. Utilisé en domaine AD pour mieux gérer les mots de passe de services.|

Bon réflexe : appliquer le **principe du moindre privilège**.

Un service n’a pas toujours besoin de tourner en `LocalSystem`.

---

## 5. Permissions de services

### 5.1 Pourquoi c’est important ?

Les services sont sensibles car :

- ils tournent souvent avec des privilèges élevés ;
    
- ils peuvent démarrer automatiquement ;
    
- ils peuvent être modifiés par des administrateurs ;
    
- ils peuvent utiliser des comptes de service ;
    
- leur mauvaise configuration peut causer une panne ou une élévation de privilèges.
    

Bonnes pratiques :

- utiliser des comptes de service dédiés ;
    
- éviter `LocalSystem` si inutile ;
    
- contrôler les permissions sur le service ;
    
- contrôler les permissions sur le dossier du binaire ;
    
- vérifier les actions de récupération ;
    
- documenter les comptes de service.
    

---

### 5.2 Points à vérifier sur un service

|Élément|Pourquoi c’est important ?|
|---|---|
|Nom du service|Nécessaire pour les commandes `sc`, PowerShell, logs.|
|Display Name|Nom lisible dans l’interface graphique.|
|État|Savoir si le service tourne ou non.|
|Mode de démarrage|Persistance potentielle si démarrage automatique.|
|Compte d’exécution|Détermine les privilèges du service.|
|Chemin du binaire|Permet de voir ce qui est exécuté.|
|Permissions du service|Qui peut démarrer, arrêter, modifier le service.|
|Permissions du dossier|Qui peut remplacer le binaire exécuté.|
|Recovery actions|Peut exécuter un programme en cas d’échec.|

---

### 5.3 Interroger la configuration d’un service

```cmd
sc qc wuauserv
```


Champs importants :

```text
BINARY_PATH_NAME     → binaire lancé
SERVICE_START_NAME   → compte d’exécution
START_TYPE           → mode de démarrage
DEPENDENCIES         → dépendances
```


---

### 5.4 Examiner les permissions d’un service avec SDDL

```cmd
sc sdshow wuauserv
```


Exemple :

```text
D:(A;;CCLCSWRPLORC;;;AU)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;SY)
```


Ce format est appelé **SDDL** : Security Descriptor Definition Language.

Exemple simplifié :

```text
(A;;CCLCSWRPLORC;;;AU)
 ^  ^-------------^   ^
 |       droits       principal cible
 |
 A = Allow
```


|Élément|Signification|
|---|---|
|`D:`|Indique la DACL.|
|`( ... )`|Une ACE.|
|`A`|Allow.|
|`D`|Deny.|
|`AU`|Authenticated Users.|
|`BA`|Built-in Administrators.|
|`SY`|SYSTEM.|
|`BU`|Built-in Users.|

---

## 6. Abus cyber liés aux services

### 6.1 Mauvaises permissions de service

Une mauvaise permission peut permettre à un utilisateur non privilégié de :

- démarrer un service ;
    
- arrêter un service ;
    
- modifier le chemin du binaire ;
    
- modifier le compte d’exécution ;
    
- remplacer le programme lancé ;
    
- obtenir une élévation de privilèges si le service tourne en `LocalSystem`.
    

Droit particulièrement sensible :

```text
SERVICE_CHANGE_CONFIG
```


---

### 6.2 Binaire de service modifiable

Cas typique :

```text
Service tourne en LocalSystem
        ↓
Le binaire est dans un dossier modifiable par un user standard
        ↓
L’attaquant remplace le binaire
        ↓
Au redémarrage du service, le binaire modifié tourne en LocalSystem
```


Vérifier :

```cmd
icacls "C:\Program Files\Application\"
```


---

### 6.3 Unquoted Service Path

Un **Unquoted Service Path** apparaît quand le chemin du binaire contient des espaces mais n’est pas entouré par des guillemets.

Exemple vulnérable :

```text
C:\Program Files\My App\service.exe
```


Au lieu de :

```text
"C:\Program Files\My App\service.exe"
```


Windows peut tenter d’interpréter le chemin par étapes :

```text
C:\Program.exe
C:\Program Files\My.exe
C:\Program Files\My App\service.exe
```


Recherche avec PowerShell :

```powershell
Get-CimInstance Win32_Service |
Where-Object {$_.PathName -match ' ' -and $_.PathName -notmatch '"'} |
Select-Object Name, StartName, PathName
```


---

## 7. Modèle de sécurité Windows

### 7.1 Security principal

Un **security principal** est une entité à laquelle Windows peut attribuer des droits.

Exemples :

- utilisateur ;
    
- groupe ;
    
- ordinateur ;
    
- service ;
    
- domaine.
    

Chaque security principal possède un identifiant unique : le **SID**.

---

### 7.2 SID — Security Identifier

Un **SID** identifie de façon unique un utilisateur, groupe, ordinateur, domaine ou service.

Windows ne se base pas sur le nom affiché mais sur le SID.

Voir son SID :

```cmd
whoami /user
```


Voir ses groupes :

```cmd
whoami /groups
```


Lister les comptes locaux et leurs SID :

```cmd
wmic useraccount get name,sid
```


---

### 7.3 Structure d’un SID

Exemple :

```text
S-1-5-21-674899381-4069889467-2080702030-1002
```


Décomposition :

```text
S-1-5-21-674899381-4069889467-2080702030-1002
^ ^ ^ ^-----------------------------------^ ^^^^
| | |             SID machine/domaine       RID
| | +-- Authority : 5 = NT Authority
| +---- Revision : toujours 1
+------ S = SID
```


|Partie|Signification|
|---|---|
|`S`|Indique qu’il s’agit d’un SID.|
|`1`|Niveau de révision. Toujours 1.|
|`5`|Identifier Authority. `5` = NT Authority.|
|`21-...`|SID de la machine ou du domaine.|
|`1002`|RID : identifiant relatif du compte.|

RID connus :

|RID|Signification|
|---|---|
|`500`|Administrateur local intégré.|
|`501`|Invité.|
|`512`|Domain Admins, en domaine AD.|
|`513`|Domain Users, en domaine AD.|
|`1000+`|Utilisateurs créés ensuite.|

---

### 7.4 Access token

Lorsqu’un utilisateur s’authentifie, Windows crée un **access token**.

Ce token contient notamment :

- SID de l’utilisateur ;
    
- SID des groupes ;
    
- privilèges ;
    
- niveau d’intégrité ;
    
- type de logon ;
    
- éventuels restricted SIDs.
    

Ensuite, les processus lancés par l’utilisateur héritent généralement de ce token.

Exemple :

```text
Utilisateur se connecte
   ↓
LSASS valide l’identité
   ↓
Windows crée un token
   ↓
explorer.exe reçoit le token
   ↓
Les programmes lancés depuis explorer.exe héritent du token
```


Quand un processus veut accéder à un fichier, une clé registre ou un service, Windows compare :

```text
Token du processus ↔ DACL de l’objet demandé
```


Puis Windows décide :

```text
Accès autorisé ou refusé
```


---

### 7.5 Privilèges Windows

Voir ses privilèges :

```cmd
whoami /priv
```


Exemples :

|Privilège|Intérêt|
|---|---|
|`SeDebugPrivilege`|Permet de déboguer ou ouvrir d’autres processus. Sensible pour LSASS.|
|`SeImpersonatePrivilege`|Permet l’impersonation. Souvent important en privesc Windows.|
|`SeBackupPrivilege`|Permet de lire certains fichiers malgré les ACL.|
|`SeRestorePrivilege`|Permet d’écrire/restaurer certains fichiers.|
|`SeShutdownPrivilege`|Permet d’arrêter le système.|
|`SeTakeOwnershipPrivilege`|Permet de prendre possession d’un objet.|

---

### 7.6 Integrity Levels

Windows utilise des niveaux d’intégrité pour limiter ce qu’un processus peut faire.

|Niveau|Exemple|
|---|---|
|`Low`|Navigateur en mode sandbox, processus très limité.|
|`Medium`|Processus utilisateur standard.|
|`High`|Processus administrateur élevé.|
|`System`|Processus système.|

Voir son niveau d’intégrité :

```cmd
whoami /groups
```


Chercher la ligne :

```text
Mandatory Label\Medium Mandatory Level
Mandatory Label\High Mandatory Level
```


---

## 8. ACL, ACE, DACL, SACL

### 8.1 Objet sécurisable

Dans Windows, beaucoup d’objets peuvent avoir des permissions :

- fichier ;
    
- dossier ;
    
- clé de registre ;
    
- service ;
    
- tâche planifiée ;
    
- processus ;
    
- thread ;
    
- imprimante ;
    
- partage réseau.
    

Ces objets possèdent un **Security Descriptor**.

---

### 8.2 Security Descriptor

Un **Security Descriptor** décrit la sécurité d’un objet.

Il contient notamment :

- **Owner** : propriétaire ;
    
- **Primary Group** : groupe principal ;
    
- **DACL** : qui a le droit de faire quoi ;
    
- **SACL** : quoi auditer/journaliser.
    

---

### 8.3 ACL / ACE / DACL / SACL

|Terme|Définition|Rôle|
|---|---|---|
|**ACE**|Access Control Entry|Une règle : tel SID a tel droit en Allow ou Deny.|
|**ACL**|Access Control List|Liste d’ACE.|
|**DACL**|Discretionary ACL|Liste des autorisations/refus d’accès.|
|**SACL**|System ACL|Liste des accès à auditer/journaliser.|

Exemple mental :

```text
Security Descriptor
├── Owner
├── Group
├── DACL
│   ├── ACE : Alice peut lire
│   ├── ACE : Bob peut écrire
│   └── ACE : Users ne peuvent pas modifier
└── SACL
    └── Auditer les échecs d’écriture
```


---

### 8.4 Access check

Quand un processus veut accéder à un objet :

```text
1. Le processus présente son token.
2. Windows lit la DACL de l’objet.
3. Windows compare les SID du token avec les ACE de la DACL.
4. Windows autorise ou refuse l’accès.
```


Schéma :

```text
Processus
  ↓ token : SID user + groupes + privilèges
Objet demandé
  ↓ DACL : ACE Allow/Deny
Décision
  ↓
Access granted / Access denied
```


---

## 9. SAM, LSA et secrets locaux

### 9.1 SAM — Security Accounts Manager

La **SAM** est la base locale des comptes Windows.

Elle contient notamment :

- comptes utilisateurs locaux ;
    
- groupes locaux ;
    
- SID ;
    
- informations nécessaires à l’authentification locale ;
    
- secrets comme les hashes de mots de passe.
    

Sur disque, la ruche SAM est ici :

```text
C:\Windows\System32\config\SAM
```


Dans le registre :

```text
HKLM\SAM
```


---

### 9.2 SAM et SYSTEM

Les secrets de la SAM sont protégés.

Pour exploiter ou analyser hors ligne la SAM dans un lab autorisé, on a souvent besoin de :

```text
SAM + SYSTEM
```


Pourquoi ?

- `SAM` contient les comptes et hashes.
    
- `SYSTEM` contient notamment des éléments nécessaires au déchiffrement local.
    

Ruches intéressantes :

|Ruche|Contenu|
|---|---|
|`SAM`|Comptes locaux et hashes.|
|`SYSTEM`|Configuration système, clés nécessaires à certains secrets.|
|`SECURITY`|Secrets LSA, informations sensibles locales.|

---

### 9.3 Extraire les ruches en lab

Commande possible en contexte administrateur/lab :

```cmd
reg save HKLM\SAM sam.save
reg save HKLM\SYSTEM system.save
reg save HKLM\SECURITY security.save
```


Note : il n’est généralement pas possible de copier directement `C:\Windows\System32\config\SAM` pendant que Windows tourne, car le fichier est verrouillé.

---

### 9.4 SAM en domaine Active Directory

Sur une machine jointe à un domaine :

- les comptes locaux restent dans la SAM locale ;
    
- les comptes de domaine sont stockés côté Active Directory ;
    
- la base AD principale est `NTDS.dit` sur les contrôleurs de domaine.
    

À retenir :

```text
Compte local → SAM locale
Compte domaine → Active Directory / NTDS.dit
```


---

## 10. Registre Windows

### 10.1 Définition

Le **registre Windows** est une base de données hiérarchique qui stocke la configuration de Windows et de nombreuses applications.

Il contient :

- paramètres système ;
    
- configuration logicielle ;
    
- services ;
    
- pilotes ;
    
- profils utilisateurs ;
    
- paramètres de sécurité ;
    
- mécanismes de démarrage automatique.
    

Ouvrir l’éditeur de registre :

```cmd
regedit
```


Interroger le registre en ligne de commande :

```cmd
reg query <clé>
```


---

### 10.2 Vocabulaire

|Terme|Définition simple|
|---|---|
|Ruche / Hive|Grande racine logique du registre.|
|Key / clé|Équivalent d’un dossier.|
|Subkey / sous-clé|Sous-dossier dans une clé.|
|Value / valeur|Entrée contenant une donnée.|
|Data / donnée|Contenu de la valeur.|

Image mentale :

```text
Ruche = disque
Clé = dossier
Valeur = fichier
Donnée = contenu du fichier
```


---

### 10.3 Ruches principales

|Ruche|Abréviation|Contenu principal|
|---|---|---|
|`HKEY_LOCAL_MACHINE`|`HKLM`|Configuration globale machine : services, pilotes, logiciels, sécurité.|
|`HKEY_CURRENT_USER`|`HKCU`|Configuration du profil utilisateur courant.|
|`HKEY_CLASSES_ROOT`|`HKCR`|Associations de fichiers, COM, classes.|
|`HKEY_USERS`|`HKU`|Profils utilisateurs chargés, identifiés par SID.|
|`HKEY_CURRENT_CONFIG`|`HKCC`|Configuration matérielle courante.|

À retenir :

```text
HKLM = machine
HKCU = utilisateur courant
HKU  = tous les profils utilisateurs chargés
```


---

### 10.4 Fichiers physiques du registre

Les ruches système sont stockées dans :

```text
C:\Windows\System32\config\
```


|Fichier|Rôle|
|---|---|
|`SAM`|Comptes locaux.|
|`SYSTEM`|Configuration système.|
|`SECURITY`|Secrets et politiques de sécurité.|
|`SOFTWARE`|Configuration logicielle.|
|`DEFAULT`|Profil par défaut.|

La ruche utilisateur courante est stockée dans :

```text
C:\Users\<USERNAME>\NTUSER.DAT
```


---

### 10.5 Services dans le registre

Les services sont configurés dans :

```text
HKLM\SYSTEM\CurrentControlSet\Services\<ServiceName>
```


Exemple :

```powershell
Get-Acl -Path HKLM:\System\CurrentControlSet\Services\wuauserv | Format-List
```


Interroger avec `reg` :

```cmd
reg query HKLM\SYSTEM\CurrentControlSet\Services\wuauserv
```


---

## 11. Persistance Windows

### 11.1 Définition

La **persistance** désigne les mécanismes permettant à un programme ou à un attaquant de survivre à :

- un redémarrage ;
    
- une déconnexion ;
    
- une reconnexion utilisateur ;
    
- un arrêt temporaire du processus.
    

---

### 11.2 Run et RunOnce Registry Keys

Les clés `Run` et `RunOnce` permettent de lancer automatiquement des programmes.

Clés principales :

```text
HKLM\Software\Microsoft\Windows\CurrentVersion\Run
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce
HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce
```


Différence :

|Clé|Effet|
|---|---|
|`Run`|Lance le programme à chaque ouverture de session.|
|`RunOnce`|Lance le programme une seule fois puis supprime l’entrée.|
|`HKLM`|S’applique à la machine / tous les utilisateurs.|
|`HKCU`|S’applique à l’utilisateur courant.|

Exemple d’interrogation :

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
```


Focus forensic : ces clés sont parmi les premiers endroits à vérifier en cas de suspicion de persistance.

---

### 11.3 Services comme persistance

Un attaquant peut chercher à créer ou modifier un service pour exécuter un programme au démarrage.

À vérifier :

```powershell
Get-CimInstance Win32_Service | Select-Object Name, State, StartMode, StartName, PathName
```


Points suspects :

- service récemment créé ;
    
- nom imitant un service Windows ;
    
- chemin dans `Temp`, `AppData`, `Public` ;
    
- service en `Automatic` ;
    
- binaire non signé ;
    
- compte d’exécution très privilégié.
    

---

### 11.4 Tâches planifiées

Les tâches planifiées sont un mécanisme très fréquent de persistance.

Lister les tâches :

```cmd
schtasks /query /fo LIST /v
```


Avec PowerShell :

```powershell
Get-ScheduledTask
```


Points à regarder :

- déclencheur ;
    
- action exécutée ;
    
- compte utilisé ;
    
- chemin du binaire ;
    
- date de création/modification ;
    
- tâche cachée ou nom trompeur.
    

---

### 11.5 Startup folder

Dossier de démarrage utilisateur :

```text
C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```


Dossier de démarrage commun :

```text
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
```


---

### 11.6 Autoruns

`Autoruns` est un outil Sysinternals très utile pour analyser la persistance Windows.

Il permet de voir :

- Run Keys ;
    
- services ;
    
- drivers ;
    
- tâches planifiées ;
    
- DLL chargées automatiquement ;
    
- extensions shell ;
    
- AppInit ;
    
- Winlogon ;
    
- WMI ;
    
- codecs ;
    
- composants navigateur.
    

Outil recommandé :

```text
autoruns.exe
```


---

## 12. Outils Windows et Sysinternals

### 12.1 Task Manager

Le **Task Manager** permet d’observer rapidement :

- processus ;
    
- performance CPU/RAM/disque/réseau ;
    
- utilisateurs connectés ;
    
- applications au démarrage ;
    
- services ;
    
- PID ;
    
- consommation des ressources.
    

Raccourcis :

```text
Ctrl + Shift + Esc
Ctrl + Alt + Del → Task Manager
taskmgr
```


---

### 12.2 Resource Monitor

Resource Monitor donne plus de détails sur :

- CPU ;
    
- mémoire ;
    
- disque ;
    
- réseau.
    

Lancement :

```cmd
resmon
```


---

### 12.3 Sysinternals

Sysinternals est une suite d’outils Microsoft pour l’administration, le diagnostic et l’analyse Windows.

Accès possible via :

```text
\\live.sysinternals.com\tools
```


Exemple :

```cmd
\\live.sysinternals.com\tools\procdump.exe -accepteula
```


---

### 12.4 Process Explorer

`Process Explorer` est une version avancée du Task Manager.

Utile pour voir :

- hiérarchie parent/enfant ;
    
- chemin du binaire ;
    
- utilisateur ;
    
- niveau d’intégrité ;
    
- DLL chargées ;
    
- handles ;
    
- signature ;
    
- services hébergés par `svchost.exe`.
    

Outil :

```text
procexp.exe
```


---

### 12.5 Process Monitor — Procmon

`Procmon` permet de surveiller en temps réel :

- accès fichiers ;
    
- accès registre ;
    
- activité réseau ;
    
- création de processus/threads.
    

Outil :

```text
procmon.exe
```


Filtres utiles :

```text
Process Name is <process.exe>
Operation is RegSetValue
Operation is CreateFile
Result is ACCESS DENIED
Result is NAME NOT FOUND
Path ends with .dll
```


---

### 12.6 TCPView

`TCPView` affiche les connexions réseau actives par processus.

Outil :

```text
tcpview.exe
```


Commandes natives alternatives :

```cmd
netstat -ano
```


```powershell
Get-NetTCPConnection
```


---

### 12.7 AccessChk

`AccessChk` permet d’auditer les permissions.

Outil :

```text
accesschk.exe
```


Exemple :

```cmd
accesschk.exe -uwcqv "Authenticated Users" *
```


---

### 12.8 Sigcheck

`Sigcheck` permet de vérifier les signatures de fichiers.

Outil :

```text
sigcheck.exe
```


Exemple :

```cmd
sigcheck.exe -m C:\Windows\System32\svchost.exe
```


---

## 13. UAC — User Account Control

### 13.1 Définition

L’**UAC** est un mécanisme de sécurité Windows qui contrôle l’élévation de privilèges.

Il vise à empêcher qu’un programme réalise des actions administrateur sans validation.

Exemples d’actions déclenchant potentiellement l’UAC :

- installation d’un logiciel ;
    
- modification système ;
    
- écriture dans certains dossiers protégés ;
    
- modification de clés registre sensibles ;
    
- lancement d’un outil en administrateur.
    

---

### 13.2 Admin Approval Mode

Un utilisateur membre du groupe Administrators ne travaille pas forcément en permanence avec un token administrateur complet.

En pratique, il peut avoir :

- un token filtré, utilisé par défaut ;
    
- un token élevé, utilisé après validation UAC.
    

Schéma :

```text
Admin connecté
   ↓
Token standard filtré
   ↓
Demande d’élévation
   ↓
Prompt UAC
   ↓
Token administrateur élevé
```


À retenir :

```text
Être admin ≠ être élevé
```


---

## 14. Protections Windows

### 14.1 Windows Defender

Windows Defender Antivirus est l’antivirus intégré de Windows.

Fonctionnalités importantes :

- protection temps réel ;
    
- protection cloud ;
    
- soumission automatique d’échantillons ;
    
- Tamper Protection ;
    
- exclusions ;
    
- Controlled Folder Access ;
    
- protection contre certains comportements malveillants.
    

Commandes utiles :

```powershell
Get-MpComputerStatus
Get-MpPreference
```


---

### 14.2 Credential Guard

**Credential Guard** protège certains secrets d’authentification en les isolant via Virtualization-Based Security.

Objectif : réduire l’impact d’un accès au système en empêchant certains vols de credentials depuis LSASS.

---

### 14.3 LSA Protection / RunAsPPL

**LSA Protection** permet de lancer LSASS comme processus protégé.

Objectif : empêcher des processus non autorisés d’ouvrir ou de manipuler LSASS.

---

### 14.4 AppLocker

**AppLocker** permet de contrôler quels programmes peuvent être exécutés.

Il peut créer des règles sur :

- exécutables ;
    
- scripts ;
    
- fichiers MSI ;
    
- DLL ;
    
- applications packagées.
    

Types de règles :

|Type|Exemple|
|---|---|
|Publisher|Autoriser les binaires signés par Microsoft.|
|Path|Autoriser uniquement certains chemins.|
|Hash|Autoriser un fichier précis par son hash.|

Bon réflexe : commencer en **audit mode** avant de bloquer réellement.

---

### 14.5 WDAC

**Windows Defender Application Control** est une solution plus robuste de contrôle d’exécution applicative.

Différence simplifiée :

|Outil|Usage|
|---|---|
|AppLocker|Contrôle applicatif plus simple à déployer.|
|WDAC|Contrôle plus fort, plus adapté aux environnements très sécurisés.|

---

## 15. Mini checklists cyber

### 15.1 Analyse rapide d’un processus suspect

À vérifier :

- nom du processus ;
    
- PID / PPID ;
    
- processus parent ;
    
- chemin du binaire ;
    
- ligne de commande ;
    
- utilisateur ;
    
- niveau d’intégrité ;
    
- signature ;
    
- DLL chargées ;
    
- connexions réseau ;
    
- date de création/modification du fichier.
    

Commandes/outils :

```powershell
Get-Process
Get-CimInstance Win32_Process | Select ProcessId,ParentProcessId,Name,ExecutablePath,CommandLine
```


```cmd
tasklist /svc
netstat -ano
```


Outils :

```text
Process Explorer
Process Monitor
TCPView
Sigcheck
```


---

### 15.2 Analyse rapide d’un service suspect

À vérifier :

- nom du service ;
    
- display name ;
    
- état ;
    
- mode de démarrage ;
    
- compte d’exécution ;
    
- chemin du binaire ;
    
- permissions du service ;
    
- permissions du dossier ;
    
- signature du binaire ;
    
- date de création/modification ;
    
- recovery actions.
    

Commandes :

```cmd
sc qc <service>
sc sdshow <service>
```


```powershell
Get-CimInstance Win32_Service | Select Name,State,StartMode,StartName,PathName
Get-Acl "C:\chemin\du\dossier"
```


---

### 15.3 Analyse rapide d’une persistance

À vérifier :

- Run Keys ;
    
- RunOnce ;
    
- services ;
    
- tâches planifiées ;
    
- Startup folders ;
    
- WMI persistence ;
    
- drivers ;
    
- extensions shell ;
    
- Winlogon ;
    
- AppInit DLLs.
    

Commandes :

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
schtasks /query /fo LIST /v
```


```powershell
Get-ScheduledTask
Get-CimInstance Win32_Service | Select Name,StartMode,StartName,PathName
```


Outil recommandé :

```text
Autoruns
```


---

## 16. Résumé mental

### Chaîne d’exécution

```text
Programme sur disque
   ↓
Processus en mémoire
   ↓
Threads exécutent le code
   ↓
Le processus possède un token
   ↓
Le token contient SID, groupes, privilèges, intégrité
   ↓
Windows compare le token aux ACL des objets
   ↓
Accès autorisé ou refusé
```


### Chaîne services

```text
Service configuré dans le registre
   ↓
Géré par le SCM
   ↓
Lancé via services.exe
   ↓
Tourne sous un compte défini
   ↓
Exécute un binaire ou une DLL via svchost.exe
   ↓
Peut devenir un vecteur de persistance ou privesc si mal configuré
```


### Chaîne authentification

```text
Utilisateur saisit ses identifiants
   ↓
LSASS vérifie l’identité
   ↓
Windows crée un access token
   ↓
Les processus héritent du token
   ↓
Les accès sont décidés via les DACL
```


---

## 17. Commandes à retenir

### Processus

```powershell
Get-Process
Get-Process -Id <PID> | Format-List *
Get-CimInstance Win32_Process | Select ProcessId,ParentProcessId,Name,ExecutablePath,CommandLine
```


```cmd
tasklist
tasklist /svc
wmic process get processid,parentprocessid,executablepath,commandline
```


### Identité / token

```cmd
whoami
whoami /user
whoami /groups
whoami /priv
```


### Services

```powershell
Get-Service
Get-Service | Where-Object {$_.Status -eq "Running"}
Get-CimInstance Win32_Service | Select Name,State,StartMode,StartName,PathName
```


```cmd
sc query
sc qc <service>
sc start <service>
sc stop <service>
sc sdshow <service>
```


### Permissions

```cmd
icacls "C:\chemin"
```


```powershell
Get-Acl "C:\chemin" | Format-List
Get-Acl HKLM:\System\CurrentControlSet\Services\wuauserv | Format-List
```


### Registre

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKLM\SYSTEM\CurrentControlSet\Services\wuauserv
```


### Ruches en lab

```cmd
reg save HKLM\SAM sam.save
reg save HKLM\SYSTEM system.save
reg save HKLM\SECURITY security.save
```


### Tâches planifiées

```cmd
schtasks /query /fo LIST /v
```


```powershell
Get-ScheduledTask
```


### Defender

```powershell
Get-MpComputerStatus
Get-MpPreference
```


---

## 18. Erreurs fréquentes à éviter

- Confondre **programme** et **processus**.
    
- Confondre **processus** et **service**.
    
- Dire que tous les `svchost.exe` sont suspects : il y en a beaucoup de légitimes.
    
- Oublier de vérifier le **chemin réel** du binaire.
    
- Se fier uniquement au nom du processus.
    
- Oublier le **compte d’exécution** d’un service.
    
- Regarder seulement les permissions du service, mais pas celles du dossier contenant le binaire.
    
- Croire qu’être administrateur signifie toujours avoir un token élevé.
    
- Confondre **DACL** et **SACL**.
    
- Oublier que les Run Keys peuvent exister en `HKCU` et `HKLM`.
    
- Ne pas vérifier les tâches planifiées dans une analyse de persistance.
    
- Négliger les signatures numériques des binaires.
    

---

## 19. Mini quiz

### Questions

1. Quelle est la différence entre un programme et un processus ?
    
2. Pourquoi faut-il regarder le PPID d’un processus suspect ?
    
3. À quoi sert `svchost.exe` ?
    
4. Pourquoi LSASS est-il une cible importante pour un attaquant ?
    
5. Quelle commande permet de voir le SID de l’utilisateur courant ?
    
6. Que contient un access token ?
    
7. Quelle est la différence entre DACL et SACL ?
    
8. Où sont stockés les services dans le registre ?
    
9. Pourquoi un service en `LocalSystem` avec un dossier modifiable est dangereux ?
    
10. Quelles clés registre vérifier pour une persistance simple ?
    
11. Quelle commande permet de lister les services avec leur chemin de binaire ?
    
12. Pourquoi UAC peut bloquer une action même si l’utilisateur est administrateur ?
    

### Réponses attendues

1. Un programme est un fichier sur disque ; un processus est une instance en cours d’exécution.
    
2. Le PPID permet de comprendre quel processus l’a lancé et de détecter des chaînes suspectes.
    
3. `svchost.exe` héberge des services Windows fournis sous forme de DLL.
    
4. LSASS peut contenir des secrets d’authentification comme hashes NTLM ou tickets Kerberos.
    
5. `whoami /user`.
    
6. SID utilisateur, SID des groupes, privilèges, niveau d’intégrité, informations de session.
    
7. DACL = autorisations/refus ; SACL = audit/journalisation.
    
8. `HKLM\SYSTEM\CurrentControlSet\Services\<ServiceName>`.
    
9. Un attaquant pourrait remplacer le binaire et le faire exécuter avec des privilèges élevés.
    
10. `HKCU/HKLM\Software\Microsoft\Windows\CurrentVersion\Run` et `RunOnce`.
    
11. `Get-CimInstance Win32_Service | Select Name,State,StartMode,StartName,PathName`.
    
12. Parce qu’un admin utilise souvent un token filtré tant qu’il n’a pas validé l’élévation UAC.
    

---

## 20. Réponse type entretien

> Sous Windows, un programme devient un processus lorsqu’il est exécuté. Ce processus possède un PID, un contexte utilisateur et un access token contenant les SID, groupes, privilèges et niveau d’intégrité. Lorsqu’il tente d’accéder à un objet comme un fichier, une clé de registre ou un service, Windows compare ce token à la DACL de l’objet pour autoriser ou refuser l’accès. Les services sont des processus particuliers, gérés par le Service Control Manager, qui peuvent démarrer automatiquement et tourner sous des comptes privilégiés comme LocalSystem. C’est pourquoi les permissions de services, le chemin du binaire, le compte d’exécution et les mécanismes de persistance comme les Run Keys ou les tâches planifiées sont des points essentiels à analyser en cybersécurité.
