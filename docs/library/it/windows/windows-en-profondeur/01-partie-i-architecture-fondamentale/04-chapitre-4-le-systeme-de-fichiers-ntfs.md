---
title: Chapitre 4 — Le système de fichiers NTFS
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - ../index.md
- - Partie I — Architecture fondamentale
  - index.md
---

## 4.1 NTFS face aux autres systèmes de fichiers

| Système | À savoir | Avantages | Limites |
|---|---|---|---|
| **FAT32** | Clés USB, cartes SD | Compatible partout | Fichiers ≤ 4 Go, ni permissions ni journal |
| **exFAT** | Supports amovibles modernes | Gros fichiers, multi-OS | Pas de permissions |
| **NTFS** | Système par défaut de Windows | Permissions fines (ACL), journalisation, chiffrement EFS, compression, flux alternatifs | Peu lu nativement par certains appareils |

## 4.2 La MFT et les horodatages

La **MFT** (*Master File Table*) contient un enregistrement par fichier ou dossier, y compris récemment supprimé : c'est un artefact forensic majeur (outil : MFTECmd).

Chaque fichier porte ses horodatages **MACB** (*Modified, Accessed, Changed, Birth*) en **deux exemplaires** :

| Attribut | Modifiable par | Usage forensic |
|---|---|---|
| `$STANDARD_INFORMATION` | Les API utilisateur | Ce qu'affiche l'Explorateur |
| `$FILE_NAME` | Le noyau seulement | Référence plus fiable |

Une incohérence entre les deux révèle souvent une falsification des dates (*timestomping*).

## 4.3 Les flux de données alternatifs (ADS)

Sous NTFS, un fichier peut porter plusieurs **flux** : le flux principal (le contenu visible) et des flux nommés (`document.txt:nom`). L'Explorateur n'affiche que la taille du flux principal.

```powershell
Get-Item .\document.txt -Stream *          # lister les flux
Get-Content .\document.txt -Stream Zone.Identifier
```


Le flux le plus important est **`Zone.Identifier`** : c'est la **Mark of the Web (MotW)**. Windows l'ajoute à tout fichier téléchargé ou reçu par messagerie (`ZoneId=3` = Internet), et elle déclenche toute la chaîne de protection — SmartScreen, mode protégé d'Office, blocage des macros, règles ASR (Ch.26).

## 4.4 Le journal des modifications

Le **`$UsnJrnl`** enregistre créations, suppressions et renommages de fichiers : il permet de dater ce qui s'est passé sur le volume, même pour des fichiers disparus (Ch.24).

## 4.5 Permissions NTFS

Chaque fichier et dossier porte une ACL (le modèle complet est au Ch.17).

| Permission de base | Autorise |
|---|---|
| **Full Control** | Tout, y compris modifier les permissions et prendre la propriété |
| **Modify** | Lire, écrire, supprimer |
| **Read & Execute** | Lire et exécuter |
| **List Folder Contents** | Lister et exécuter (dossiers uniquement) |
| **Read** | Lire contenu et attributs |
| **Write** | Créer des fichiers, écrire |

Ces permissions de base regroupent des **permissions spéciales** (traverser un dossier, lire les données, créer des fichiers, ajouter des données, supprimer, lire les permissions, **modifier les permissions**, **prendre possession**).

```powershell
icacls C:\Données                              # lire l'ACL
icacls D:\Projets /grant Equipe:(OI)(CI)M      # Modify, hérité par fichiers et sous-dossiers
icacls D:\Partage /remove joe                  # retirer un compte
```


Droits abrégés d'`icacls` : `F` (Full), `M` (Modify), `RX` (Read & Execute), `R`, `W`, `D` (Delete), `N` (aucun accès).

> **À repérer en audit :** `Everyone`, `BUILTIN\Users` ou `Authenticated Users` en `(F)` ou `(M)` sur un dossier de programme, un binaire de service ou un script exécuté par un compte privilégié.

## 4.6 NTFS et partages SMB

Un dossier partagé sur le réseau porte **deux** couches de permissions :

| Couche | S'applique | Niveaux |
|---|---|---|
| **Permissions de partage** | Accès par le réseau (`\\serveur\partage`) | Read, Change, Full Control |
| **Permissions NTFS** | Tout accès, local ou réseau | Voir §4.5 |

Pour un accès réseau, l'accès effectif est **le plus restrictif des deux** : partage en Full Control et NTFS en Read donne… Read. La pratique courante : partage large (*Authenticated Users : Change*) et contrôle fin en NTFS.

---
