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

## Sommaire

- [1. Programmes, processus et threads](01-1-programmes-processus-et-threads.md)
- [3. Focus LSASS](02-3-focus-lsass.md)
- [4. Services Windows](03-4-services-windows.md)
- [5. Permissions de services](04-5-permissions-de-services.md)
- [7. Modèle de sécurité Windows](05-7-modele-de-securite-windows.md)
- [10. Registre Windows](06-10-registre-windows.md)
- [11. Persistance Windows](07-11-persistance-windows.md)
- [12. Outils Windows et Sysinternals](08-12-outils-windows-et-sysinternals.md)
