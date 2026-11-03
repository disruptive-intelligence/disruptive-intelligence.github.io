---
title: Chapitre 7 — De la mise à jour au redémarrage
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - ../index.md
- - Partie III — Ce qui se passe dans la machine
  - index.md
---

> 🧱 **Les bases**
>
> - Un **service** Windows est un programme qui tourne en arrière-plan, sans fenêtre, souvent avec le compte **SYSTEM** (les droits les plus élevés sur la machine). On les voit dans `services.msc` ou avec `Get-Service`.
> - Une **DLL** est une bibliothèque de code partagée par plusieurs programmes. Quand un programme l'utilise, elle est **chargée en mémoire** et le fichier est verrouillé.
> - Une **signature numérique** prouve qu'un fichier provient bien de son éditeur et n'a pas été modifié.

## 7.1 Les formats de paquets

| Format | Ce que c'est | Outil |
|---|---|---|
| **.msu** (*Microsoft Update Standalone Package*) | Paquet autonome téléchargé du catalogue. Contient un ou plusieurs .cab, un fichier de métadonnées et des fichiers XML | double-clic, `wusa.exe`, ou `DISM /Add-Package` |
| **.cab** | Archive du paquet CBS lui-même (dans le .msu, ou fourni seul) | `DISM /Online /Add-Package /PackagePath:…` |
| **.psf** + **.cab** / **.wim** | Formats des cumulatives récentes : le .psf contient les **fichiers différentiels** (avant/après) | via le .msu |
| **.exe** / **.msi** | Office MSI, Edge, MSRT, Defender | l'installeur du produit |
| **.esd** / **.wim** / ISO | Images complètes de Windows (mises à niveau, installations) | `setup.exe`, outils de déploiement |
| **Express** | Variante différentielle d'une cumulative : le client ne télécharge que ce qui lui manque. **Très lourde côté serveur WSUS** (plusieurs fois la taille de la cumulative en stockage), option à éviter en général | — |
| **UUP** (*Unified Update Platform*) | Mode de livraison de Windows Update et des services cloud : un seul format pour toutes les sources, téléchargement différentiel optimisé | Windows Update, Intune, Autopatch |

```powershell
wusa C:\Temp\windows11.0-kb50xxxxx-x64.msu /quiet /norestart
DISM /Online /Add-Package /PackagePath:C:\Temp\windows11.0-kb50xxxxx-x64.msu
DISM /Online /Get-Packages /Format:Table
DISM /Online /Remove-Package /PackageName:Package_for_RollupFix~31bf3856ad364e35~amd64~~26100.xxxx.1.x
```


**Ce que contient vraiment une cumulative moderne.** Pas une copie de chaque fichier corrigé, mais, pour chaque fichier, un **différentiel « vers l'avant »** (de la version de base à la nouvelle) et un **différentiel « vers l'arrière »** (pour revenir à la version de base). C'est ce qui permet des cumulatives raisonnables en taille malgré « tout depuis la sortie », et la désinstallation.

**Signature et intégrité.** Chaque paquet et chaque fichier système est signé par Microsoft. Les **catalogues de signatures** (fichiers .cat) sont stockés dans `C:\Windows\System32\catroot` et leur base dans `catroot2`. Le client WSUS vérifie aussi que les fichiers téléchargés correspondent aux **empreintes** (hash) annoncées dans les métadonnées. Une mise à jour non signée par Microsoft (ou par un certificat explicitement approuvé pour la publication locale) est **refusée**.

## 7.2 Les services impliqués

| Service | Nom | Rôle |
|---|---|---|
| Windows Update | `wuauserv` | l'**agent** (WUA) : recherche, téléchargement, dialogue avec WSUS ou Windows Update |
| Update Orchestrator | `UsoSvc` | **orchestre** : planification, échéances, redémarrages, notifications |
| BITS | `BITS` | téléchargement en arrière-plan, avec reprise après coupure et bande passante adaptative |
| Delivery Optimization | `DoSvc` | téléchargement en pair à pair entre machines du réseau (Windows Update, Intune, ConfigMgr) |
| Windows Modules Installer | `TrustedInstaller` | **installe** les paquets CBS dans le magasin de composants |
| Windows Update Medic | `WaaSMedicSvc` | **répare** les composants Windows Update s'ils ont été désactivés ou abîmés |
| Services de chiffrement | `CryptSvc` | vérifie les signatures, gère `catroot2` |

> ⚠️ **Piège** — Désactiver `wuauserv` pour « bloquer les mises à jour » ne marche pas durablement : `WaaSMedicSvc` le réactive. On contrôle les mises à jour **par les stratégies** (GPO, Intune), pas en cassant les services.

## 7.3 Les étapes d'une mise à jour

1. **Recherche** (*scan*) : l'agent demande à sa source (WSUS ou Windows Update) les **métadonnées**, puis évalue lui-même les **règles d'applicabilité** de chaque mise à jour (version, build, fichiers présents, prérequis, mises à jour déjà installées). Résultat : applicable, non applicable, ou déjà installée. **C'est le client qui décide de ce dont il a besoin**, pas le serveur.
2. **Téléchargement** : via BITS (ou Delivery Optimization avec les sources cloud), dans `C:\Windows\SoftwareDistribution\Download`. Vérification des empreintes.
3. **Installation** (*staging*) : TrustedInstaller prépare les nouvelles versions des composants dans le **magasin de composants** (`C:\Windows\WinSxS`). Les fichiers qui ne sont pas utilisés sont remplacés tout de suite ; les fichiers **verrouillés** (DLL chargées, pilotes, noyau) sont inscrits dans une liste d'opérations à faire au redémarrage (`C:\Windows\WinSxS\pending.xml`).
4. **Redémarrage** : à l'arrêt puis au démarrage, Windows applique les opérations en attente (« Mise à jour en cours, ne pas éteindre l'ordinateur »). **Avant ce redémarrage, la machine n'est pas protégée** : les anciennes versions vulnérables sont toujours en mémoire.
5. **Rapport** : l'agent envoie à la source l'état de chaque mise à jour (installée, échec avec code, redémarrage en attente).

```
 Scan ──► Téléchargement ──► Staging (WinSxS) ──► Redémarrage ──► Rapport
  │            │                    │                  │            │
 WUA        BITS / DO         TrustedInstaller     CBS au boot     WUA
```


## 7.4 Le magasin de composants (WinSxS) et la CBS

**CBS** (*Component-Based Servicing*) : Windows n'est pas un ensemble de fichiers posés en vrac, mais un ensemble de **composants** décrits par des **manifestes** (quels fichiers, quelles clés de registre, quelles dépendances). La CBS sait quelle version de chaque composant est installée, et laquelle doit l'être.

**WinSxS** (*Windows Side-by-Side*) : le dossier où Windows garde les composants, **y compris plusieurs versions** du même composant (c'est ce qui permet la désinstallation d'une mise à jour). Les fichiers de `System32` sont pour la plupart des **liens physiques** vers WinSxS : l'Explorateur compte deux fois le même fichier, d'où une taille **apparente** énorme (souvent 10 à 15 Go) très supérieure à la taille réelle.

```powershell
DISM /Online /Cleanup-Image /AnalyzeComponentStore     # taille réelle du magasin, nettoyage recommandé ?
DISM /Online /Cleanup-Image /StartComponentCleanup     # supprime les anciennes versions (fait aussi par une tâche planifiée)
```


> ⚠️ **Piège** — `DISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase` supprime **définitivement** les versions remplacées : on ne peut **plus désinstaller** aucune des mises à jour déjà installées. À réserver aux images de référence (masters), jamais sur un poste en production en plein cycle de déploiement.

## 7.5 Le redémarrage en attente

Une machine « installée, redémarrage en attente » **n'est pas corrigée**. Comment le savoir :

| Indicateur | Emplacement |
|---|---|
| Opérations CBS en attente | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending` (la clé existe) |
| Windows Update attend un redémarrage | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired` |
| Renommages de fichiers en attente | valeur `PendingFileRenameOperations` sous `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager` |
| WSUS | état *Installed/Pending Reboot* |

```powershell
Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending'
Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired'
```


L'orchestrateur (`UsoSvc`) gère le moment du redémarrage selon les stratégies : **heures d'activité** (période pendant laquelle Windows ne redémarre pas seul), **échéances** (au-delà, le redémarrage est forcé), notifications à l'utilisateur. Les réglages sont vus au Ch.9 (GPO) et au Ch.12 (fenêtres de maintenance).

> 🧵 **Fil rouge — Jeudi 22 janvier 2026**
>
> Le rapport WSUS montre 210 postes « installé, redémarrage en attente » depuis plus de 7 jours. Ce sont surtout des portables d'agents commerciaux, mis en veille le soir et jamais redémarrés. Inès explique à Claire, la RSSI, que ces 210 postes **ne sont pas protégés** malgré la mention « installé ». La décision : une échéance de redémarrage à 3 jours avec notifications, et un indicateur dédié dans le rapport mensuel.

> 📌 **À retenir**
>
> - Une mise à jour suit cinq étapes : scan (par le client), téléchargement, staging dans WinSxS, **redémarrage**, rapport.
> - Tant que la machine n'a pas redémarré, l'ancienne version vulnérable reste active.
> - On ne bloque pas Windows Update en désactivant des services ; on le pilote par stratégie.
> - `/ResetBase` rend les mises à jour **non désinstallables**.

---
