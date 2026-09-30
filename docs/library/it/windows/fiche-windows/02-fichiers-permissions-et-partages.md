---
title: Fichiers, permissions et partages
source: IT/02_Windows/Fiche_Windows.md
note: Fiche Windows
up:
- - Fiche Windows
  - index.md
---

## 4. Systèmes de fichiers : FAT32, exFAT, NTFS

### À retenir

- **FAT32** : universel mais limité (fichiers < 4 Go, aucune permission ni chiffrement natif).
- **exFAT** : version moderne de FAT pour gros fichiers et supports amovibles.
- **NTFS** : système par défaut de Windows depuis NT 3.1.

### Comment ça fonctionne
NTFS apporte ce que FAT n'a pas : **permissions granulaires** sur fichiers et dossiers, **journalisation** (chaque ajout/modif/suppression est tracé), support des grandes partitions, et **héritage** des permissions depuis le dossier parent. C'est cette structure qui rend le contrôle d'accès local possible.

### Pourquoi c'est important en cyber
Les permissions NTFS sont le cœur du contrôle d'accès local : qui peut lire, écrire, exécuter quoi. La journalisation NTFS est précieuse en **forensic** pour reconstituer une chronologie d'événements (fichiers créés, modifiés, supprimés).

### Exemple concret
Une clé USB en FAT32 ne conserve aucune permission : un fichier sensible copié dessus perd toute protection d'accès.

### Point clé à mémoriser
NTFS = permissions + journalisation + héritage. C'est ce qui sécurise (ou expose) les fichiers.

---

## 5. Permissions NTFS et icacls

### À retenir
Permissions principales : `Full Control`, `Modify`, `Read & Execute`, `Read`, `Write`, `List Folder Contents`. Par défaut, fichiers et dossiers **héritent** des permissions de leur parent.

### Comment ça fonctionne
Chaque objet NTFS possède une liste de permissions (ACL) attachée à des utilisateurs ou groupes. L'héritage évite à l'administrateur de tout définir manuellement : un dossier transmet ses permissions à son contenu, sauf si l'héritage est désactivé. Les dossiers et les fichiers peuvent recevoir des permissions différentes (ex. `List Folder Contents` ne concerne que les dossiers).

Lecture d'une sortie `icacls` :

```
BUILTIN\Users:(RX)              → les utilisateurs ont lecture + exécution
NT AUTHORITY\SYSTEM:(OI)(CI)(F) → SYSTEM a contrôle total, hérité aux objets/conteneurs
```

Codes d'accès : `F` full, `M` modify, `RX` read+execute, `R` read, `W` write.
Codes d'héritage : `(OI)` object inherit, `(CI)` container inherit, `(I)` hérité du parent.

### Pourquoi c'est important en cyber
Un dossier **inscriptible** contenant le binaire d'un service ou d'une application privilégiée est dangereux : on peut remplacer l'exécutable légitime par un binaire malveillant qui sera lancé avec les droits du service. C'est l'un des chemins d'élévation de privilèges les plus courants.

### Exemple concret
Si `BUILTIN\Users` a `(W)` sur le dossier d'un service tournant en SYSTEM, un utilisateur standard peut y déposer son propre exécutable et obtenir SYSTEM au prochain démarrage du service.

### Commandes utiles

```cmd
icacls C:\Windows                 # Lister les permissions d'un dossier
icacls C:\Temp\Test /grant joe:F  # Accorder Full control à "joe"
icacls C:\Temp\Test /remove joe   # Retirer les permissions de "joe"
```


### Point clé à mémoriser
Un dossier inscriptible sur le chemin d'un binaire privilégié = porte ouverte à l'élévation de privilèges.

---

## 6. SMB, partages réseau et permissions

### À retenir
**SMB** (Server Message Block, port **445**) partage fichiers et imprimantes sur le réseau. Deux jeux de permissions s'appliquent à un partage : **Share permissions** (accès réseau) et **NTFS permissions** (local + réseau).

### Comment ça fonctionne
Quand on accède à un partage via le réseau, Windows évalue **les deux** listes et applique **la plus restrictive**. En local (ou en RDP), seules les permissions NTFS comptent. Les partages NTFS étant plus granulaires, ils offrent un contrôle plus fin que les Share permissions.

L'authentification dépend du contexte :

- **Workgroup** : les connexions sont vérifiées contre la **SAM locale** de la machine cible.
- **Domaine** : les connexions sont vérifiées contre **Active Directory** (base centralisée).

### Pourquoi c'est important en cyber
Les partages mal configurés permettent la propagation de malwares et l'exfiltration de données. Surtout, les **partages administratifs** (`C$`, `ADMIN$`, `IPC$`) sont actifs par défaut : `C$` expose toute la partition système à qui possède les droits adéquats.

### Exemple concret
Depuis une machine Linux, `smbclient -L <IP> -U <user>` liste les partages ; si `Company Data` est accessible en lecture au groupe `Everyone`, son contenu est consultable à distance.

### Commandes utiles

```cmd
net share                              # Lister les partages locaux
```

```bash
smbclient -L <IP> -U <user>            # Lister les partages distants (Linux)
smbclient '\\<IP>\Company Data' -U <user>
sudo mount -t cifs -o username=<user> //<IP>/"share" /mnt/point
```


### Point clé à mémoriser
SMB = port 445 ; partages par défaut `C$`, `ADMIN$`, `IPC$` ; entre Share et NTFS, la plus restrictive gagne.

---
