---
title: Découvrir Windows
source: IT/02_Windows/Fiche_Windows.md
note: Windows — fiche cyber
up:
- - Windows — fiche cyber
  - index.md
---

## 1. Introduction à Windows

### À retenir
Deux familles : **Windows Desktop** (XP → 11), pour les postes utilisateurs, et **Windows Server** (2000 → 2022), pour l'infrastructure. C'est Server qui introduit les rôles d'entreprise : Active Directory, IIS, partage de fichiers centralisé, services réseau.

### Comment ça fonctionne
Windows Server étend le noyau Desktop avec des composants d'administration centralisée. En entreprise, un **Domaine** (géré par Active Directory) regroupe les machines sous une authentification et des politiques communes, au lieu de comptes isolés sur chaque poste.

### Pourquoi c'est important en cyber
La majorité des cibles en entreprise sont Windows. Beaucoup de systèmes **legacy** (anciens, non patchés) restent en production pour des raisons applicatives ou budgétaires : ils concentrent les vulnérabilités connues et sont des points d'entrée privilégiés.

### Exemple concret
Un serveur Windows Server 2012 toujours en SMBv1 reste exposé à **EternalBlue**, exploit qui a alimenté des campagnes de ransomware (WannaCry).

### Point clé à mémoriser
Desktop = poste utilisateur, Server = infrastructure ; les vieux systèmes non patchés sont les cibles les plus rentables.

---

## 2. Versions Windows et énumération système

### À retenir
Chaque version Windows porte un numéro. Repères utiles :

| OS | Version |
| --- | --- |
| Windows 7 / Server 2008 R2 | 6.1 |
| Windows 8 / Server 2012 | 6.2 |
| Windows 10 / Server 2016 / 2019 | 10.0 |

### Comment ça fonctionne
Le couple **version + build** identifie précisément l'OS. `systeminfo` agrège aussi les correctifs installés (hotfixes), le domaine, la RAM et la carte réseau. WMI (`Get-WmiObject`) interroge les classes système pour obtenir ces infos par script.

### Pourquoi c'est important en cyber
L'énumération système est la **première étape** d'un test : version, build, patchs et appartenance à un domaine orientent vers les exploits applicables et révèlent si la machine est à jour. C'est aussi utile en inventaire défensif.

### Exemple concret
Sur une cible, le build `19041` + l'absence de certains hotfixes peut indiquer une vulnérabilité d'élévation de privilèges connue.

### Commandes utiles

```cmd
systeminfo                  # Vue d'ensemble : OS, build, patchs, domaine
ver                         # Version courte
```

```powershell
Get-WmiObject -Class Win32_OperatingSystem | select Version,BuildNumber
```


### Point clé à mémoriser
`systeminfo` = réflexe n°1 pour cartographier une cible Windows.

---

## 3. Arborescence Windows

### À retenir
Racine = `C:\` (partition de démarrage, où l'OS est installé). Au-delà de la liste des dossiers, chacun a un intérêt cyber précis.

### Comment ça fonctionne

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

### Pourquoi c'est important en cyber
Connaître l'arborescence permet de savoir **où chercher** (identifiants, config, registre) et **où écrire** quand on dispose de droits limités. C'est central en énumération comme en forensic.

### Commandes utiles

```cmd
dir C:\ /a                  # Lister tout, y compris fichiers cachés
tree C:\ /f | more          # Arborescence complète paginée
```


### Point clé à mémoriser
System32 = 64 bits, SysWOW64 = 32 bits. AppData et System32\config sont les zones à fouiller.

---
