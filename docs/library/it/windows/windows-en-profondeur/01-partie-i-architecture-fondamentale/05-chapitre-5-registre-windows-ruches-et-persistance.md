---
title: Chapitre 5 — Registre Windows, ruches et persistance
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - ../index.md
- - Partie I — Architecture fondamentale
  - index.md
---

## 5.1 Structure

Le registre est la base de données hiérarchique de configuration du système et des applications.

| Terme | Définition | Image mentale | Exemple |
|---|---|---|---|
| **Clé racine** | Point d'entrée visible dans `regedit` | Racine | `HKLM`, `HKCU` |
| **Ruche** (*hive*) | Bloc du registre stocké dans un fichier et chargé en mémoire | Le fichier sur disque | `config\SAM` monté sous `HKLM\SAM` |
| **Clé / sous-clé** | Conteneur | Dossier | `HKLM\SYSTEM\CurrentControlSet\Services` |
| **Valeur** | Entrée nommée | Fichier | `ImagePath`, `Start` |
| **Donnée** | Contenu de la valeur | Contenu du fichier | `C:\Windows\System32\svchost.exe -k netsvcs` |

| Clé racine | Contenu |
|---|---|
| **HKLM** | Configuration de la machine : services, pilotes, logiciels, SAM, SECURITY |
| **HKCU** | Configuration de l'utilisateur connecté |
| **HKU** | Tous les profils chargés (un par SID) ; HKCU pointe vers l'un d'eux |
| **HKCR** | Associations de fichiers et objets COM |
| **HKCC** | Profil matériel courant |

| Type de valeur | Contenu |
|---|---|
| `REG_SZ` | Chaîne |
| `REG_EXPAND_SZ` | Chaîne avec variables (`%SystemRoot%`) |
| `REG_DWORD` / `REG_QWORD` | Entier 32 / 64 bits |
| `REG_MULTI_SZ` | Liste de chaînes |
| `REG_BINARY` | Données brutes |

> **Le registre n'est pas un fichier unique**, et `HKLM` n'est pas un fichier : c'est une vue logique assemblée à partir de plusieurs ruches.

## 5.2 Les ruches et leurs fichiers

| Ruche | Fichier | Contenu |
|---|---|---|
| `SAM` | `C:\Windows\System32\config\SAM` | Comptes locaux et leurs secrets |
| `SECURITY` | `config\SECURITY` | Politique locale, secrets LSA |
| `SYSTEM` | `config\SYSTEM` | Services, pilotes, configuration ; contient la clé qui protège la SAM |
| `SOFTWARE` | `config\SOFTWARE` | Windows et logiciels installés |
| `DEFAULT` | `config\DEFAULT` | Profil système par défaut |
| `NTUSER.DAT` | `C:\Users\<user>\NTUSER.DAT` | Paramètres de l'utilisateur |
| `UsrClass.dat` | `…\AppData\Local\Microsoft\Windows\UsrClass.dat` | Explorer (dont shellbags), associations |
| `Amcache.hve` | `C:\Windows\AppCompat\Programs\Amcache.hve` | Programmes présents et exécutés |

`CurrentControlSet` est un lien vers le jeu de contrôle actif (`ControlSet001` le plus souvent).

## 5.3 Les emplacements de persistance

Les clés où un programme s'inscrit pour se relancer au démarrage ou à l'ouverture de session :

| Emplacement | Déclenchement |
|---|---|
| `HKLM\…\CurrentVersion\Run` et `RunOnce` | Ouverture de session de tout utilisateur |
| `HKCU\…\CurrentVersion\Run` et `RunOnce` | Ouverture de session de cet utilisateur (sans droits admin) |
| `HKLM\SYSTEM\CurrentControlSet\Services` | Démarrage d'un service ou pilote |
| `HKLM\…\Winlogon` (`Shell`, `Userinit`) | Ouverture de session |
| Image File Execution Options (IFEO) | Lancement d'un exécutable donné |
| CLSID dans `HKCU\Software\Classes` | Chargement d'un objet COM |
| `AppInit_DLLs` | Chargement de `user32.dll` (désactivé par Secure Boot) |
| `Session Manager\BootExecute` | Démarrage, très tôt |

```powershell
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run'
```


En pratique, **Autoruns** couvre tous ces emplacements d'un coup.

## 5.4 Le registre en investigation et en défense

- **Investigation** : chaque clé garde l'heure de sa dernière écriture ; le registre révèle persistance, logiciels installés, périphériques USB (`USBSTOR`), documents et programmes récents, réseaux connus. Outils : Registry Explorer, RECmd.
- **Défense** : les clés ont des ACL — une permission faible sur la clé d'un service privilégié est une faille ; on surveille les clés de persistance (Sysmon 12/13/14), on peut poser une **SACL** sur les clés sensibles et on désactive le service *Remote Registry* s'il est inutile.

---
