---
title: Fondamentaux du système
source: IT/01 Linux/Linux — prises de notes.md
note: Linux — prises de notes
up:
- - Linux — prises de notes
  - index.md
---

## Usages courants

### Linux Structure

### Composants

| **Composants** | **Description** |
| --- | --- |
| Bootloarder | Morceau de code qui guide process de démarrage pour lancer OS. Ex : GRUB, charge noyau et ses paramètres avant de passer la main au système; |
| Noyau (OS Kernel) | Composant principal de l’OS. Gère ressources des périphériques au niveau hardware.  |
| Daemons | Service en arrière-plan. Assure bon fonctionnement de fonctions clés (plannification, impression, multimédias…). Se chargent après le démarrage, gérés par ***systemd***. |
| OS Shell | Interface entre l’OS et l’user. Permet d’intérragir  |
| Serveur graphique | Fournit sous système graphique appelé “X” ou “X-server”. Permettant exécution de programmes graphiques localement ou à distance sur système de fenêtrage. Ex : Wayland ou X11. |
| Gestionnaire de fenêtres (Window manager) | Appelé interface graphique (GUI). Environnement de bureau inclut souvent appli (fichiers, navigateur web…). Ex : GNOME, KDE… |
| Utilitaire | Programmes qui remplissent fonctions particulières pour l’user. Ex : ls, cp, find, curl… |

### Architecture Linux

| **Couche** | **Description** |
| --- | --- |
| Hardware | Périphériques matériels comme la RAM, CPU, disque…  |
| Kernel | Coeur de l’OS. Fonction de virtualiser et contrôler les ressources matérielles,  CPU, mémoire allouée, données… Donne à chaque processus ressources virtuelles. Fait interface entre programmes et le matériel via appels système. |
| Shell | CLI dans laquelle user saisit commandes pour effectuer fonctions du kernel. Lance des processus et permet de chainer outils. |
| Utilitaires système | Mettent à disposition de l’user l’ensemble des fonctionnalités de l’OS.  |

### Hiérarchie du système de fichier

| **Chemin** | **Description** |
| --- | --- |
| / | Répertoire racine, contient fichiers nécessaires pour boot l’OS avant que les autres filesystems soient montés. |
| /bin | Contient les binaires de commandes essentiels Ex : ls, cp, mv… |
| /boot | Contient bootloader, exécutable du noyau et les fichiers requis pour démarrer. Ex : Config GRUB… |
| /dev | Contient fichiers de périphériques pour accéder aux périphériques matériel connectés. |
| /etc | Fichiers de configuration systèmes locaux et des apps. |
| /home | Chaque user possède sous-dossier. Ex : /home/cam |
| /lib | Bibliothèques partagées nécessaires au démarrage du système. |
| /media | Point de montage des médias amovibles. |
| /mnt | Point de montage temporaire pour systèmes de fichiers. |
| /opt | Fichiers optionnels, comme outils tiers. |
| /root | Dossier perso de l’user root. |
| /sbin | Exécutable utilisés pour l’admin système. Ex : ip, mount, fsck… |
| /tmp | Dossier pour fichiers temporaires du système & des programmes. |
| /usr | Contient exécutables, bibliothèques, pages de manuels… |
| /var | Données variables : logs, mail, fichiers d’apps web, cron… Ex : /var/log |

### Boot Process

Lorsque l’on appuie sur le bouton “Power” :

1. BIOS / UEFI (Firmware) : La carte mère se réveille, vérifie que le matériel (RAM, CPU, Disque) fonctionne (c'est le POST - *Power-On Self-Test*) et cherche un périphérique sur lequel démarrer.
2. Bootloader (GRUB) : Le système charge un petit programme (souvent GRUB) situé au tout début du disque. Son rôle est de laisser l'utilisateur choisir l'OS et de charger le noyau en mémoire.
    - Rôle : Menu bleu au démarrage, demande si on veut lancer Linux, Mode récup…
3. Kernel : Le noyau Linux se décompresse, prend le contrôle du processeur, monte un système de fichiers temporaire (initramfs) pour charger les pilotes nécessaires, puis monte le vrai disque dur.
4. Init (Systemd) : Le Kernel initialise le matériel puis lance le tout premier programme. Son identifiant (PID) est 1.

### BIOS / MBR & UEFI / GPT

- **L'Ancienne École (Legacy) : BIOS + MBR**
    - **BIOS (Basic Input/Output System) :** C'est le vieux logiciel de la carte mère (souvent un écran bleu/gris avec du texte pixelisé). Il est simple mais limité.
    - **MBR (Master Boot Record) :** C'est la façon dont le BIOS note les adresses sur le disque dur. C'est comme un vieux carnet d'adresses papier : il n'a pas beaucoup de pages.
- **La Nouvelle Technologie : UEFI + GPT**
    - **UEFI (Unified Extensible Firmware Interface) :** C'est le remplaçant moderne. Il supporte la souris, les graphismes, et il est beaucoup plus intelligent.
    - **GPT (GUID Partition Table) :** C'est le système de classement moderne. C'est comme une base de données numérique immense et sécurisée.

### Informations système
