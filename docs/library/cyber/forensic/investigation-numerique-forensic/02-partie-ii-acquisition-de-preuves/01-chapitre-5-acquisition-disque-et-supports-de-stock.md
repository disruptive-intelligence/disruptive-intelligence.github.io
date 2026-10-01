---
title: Chapitre 5 — Acquisition disque et supports de stockage
source: Cyber/04 Forensic/Investigation numérique (forensic).md
note: Investigation numérique (forensic)
up:
- - Investigation numérique (forensic)
  - ../index.md
- - Partie II — Acquisition de preuves
  - index.md
---

## 5.1 Principes fondamentaux

L'acquisition disque produit une copie bit-à-bit du support de stockage : chaque secteur est copié, y compris les espaces non alloués (où se trouvent les fichiers supprimés), le slack space (espace résiduel en fin de cluster), et les zones cachées (HPA, DCO). Ce n'est pas une simple copie de fichiers — c'est un clone exact du support au niveau des secteurs.

Le **write blocker** est le garant de l'intégrité. Un write blocker matériel (Tableau T35es, CRU WiebeTech) est un dispositif physique interposé entre le support source et la station d'acquisition qui empêche électriquement toute écriture sur le support. Un write blocker logiciel (sous Linux : montage avec `mount -o ro`, ou utilisation de udev rules) empêche les écritures au niveau du système d'exploitation. Le write blocker matériel est préféré en contexte judiciaire car il est physiquement vérifiable et indépendant du logiciel. Sans write blocker, le simple fait de connecter un disque à Windows modifie des métadonnées (timestamps d'accès, journaux du système de fichiers) — ce qui peut compromettre l'intégrité de la preuve.

La **vérification d'intégrité par double hash** (MD5 + SHA-256) est obligatoire. Le hash est calculé sur le support source avant l'acquisition, sur l'image produite immédiatement après l'acquisition, et éventuellement sur le support source après l'acquisition (pour vérifier que l'acquisition n'a rien modifié — ce qui serait le cas si le write blocker avait défailli). Si les hash correspondent, l'intégrité est prouvée mathématiquement.

## 5.2 Acquisition physique vs logique

L'**acquisition physique** copie l'intégralité du support au niveau des secteurs — c'est la méthode privilégiée car elle capture tout, y compris les données supprimées et les zones cachées. Commande type sous Linux avec dc3dd :

```
dc3dd if=/dev/sdX hof=/path/image.dd hash=md5 hash=sha256 log=/path/acquisition.log
```


L'**acquisition logique** copie uniquement les fichiers visibles par le système de fichiers. Plus rapide et moins volumineuse, mais elle ne capture ni les fichiers supprimés, ni le slack space, ni les zones non allouées. L'acquisition logique est utilisée quand l'acquisition physique est impossible (VM en production accessible uniquement par réseau, volume chiffré qu'on ne peut pas déchiffrer hors ligne) ou quand le triage rapide suffit (combinée avec KAPE pour une collecte ciblée des artefacts).

## 5.3 HDD : le support le plus favorable

Les disques durs magnétiques (HDD) sont les plus favorables au forensic. Les données supprimées restent physiquement présentes sur le plateau magnétique tant que les secteurs n'ont pas été réécrits par de nouvelles données — ce qui peut prendre des mois ou des années dans les zones peu utilisées du disque. La récupération de fichiers supprimés sur HDD est souvent possible et productive.

Les zones cachées du disque — **HPA** (Host Protected Area) et **DCO** (Device Configuration Overlay) — sont des zones que le BIOS et le système d'exploitation ne voient pas normalement, mais qui peuvent contenir des données dissimulées. L'outil `hdparm` (Linux) détecte leur présence (`hdparm -N /dev/sdX` affiche la taille réelle vs la taille visible) et permet de les rendre accessibles pour l'acquisition. Les outils forensic commerciaux (EnCase, X-Ways) gèrent cette détection automatiquement.

## 5.4 SSD : les défis du forensic moderne

Les SSD ont fondamentalement changé le forensic. Trois mécanismes posent problème.

Le **TRIM** est une commande que le système d'exploitation envoie au SSD pour indiquer que des secteurs ne sont plus utilisés — le contrôleur du SSD peut alors effacer physiquement ces secteurs pour optimiser les performances d'écriture futures. Conséquence : les fichiers supprimés sur un SSD avec TRIM actif (c'est le cas par défaut sur tous les OS modernes depuis Windows 7, macOS 10.6, et Linux avec les filesystems récents) sont souvent irrécupérables, contrairement aux HDD. Le TRIM peut s'exécuter en quelques secondes après la suppression d'un fichier.

Le **garbage collection** est un processus interne au contrôleur SSD qui réorganise et nettoie les blocs de données de manière autonome — même sans commande du système d'exploitation. Le SSD peut effacer des données « supprimées » de sa propre initiative, à n'importe quel moment, y compris quand le disque est connecté via un write blocker (le write blocker empêche les écritures venant du système, mais pas les opérations internes du contrôleur).

Le **wear leveling** distribue les écritures sur toutes les cellules NAND pour équilibrer l'usure, ce qui signifie que les données ne sont pas nécessairement stockées à l'emplacement attendu au niveau des secteurs logiques.

Implication pratique : sur un SSD, l'acquisition doit être faite le plus rapidement possible après la détection de l'incident. Chaque minute qui passe est une minute pendant laquelle le garbage collection peut effacer des preuves. Et il ne faut jamais promettre de récupérer des fichiers supprimés sur un SSD — c'est souvent impossible.

## 5.5 Stockage chiffré

Le chiffrement est un défi majeur. BitLocker (Windows), FileVault (macOS), LUKS (Linux) et VeraCrypt chiffrent le contenu du disque — sans la clé, l'image acquise est un bloc de données inexploitable. Stratégies de récupération :

Si la machine est **allumée et le volume déverrouillé**, la clé de chiffrement est en mémoire — d'où l'importance absolue du dump RAM avant toute extinction (Ch.6). Le dump mémoire, analysé avec Volatility, peut révéler la clé BitLocker, la passphrase FileVault, ou les clés LUKS.

La **recovery key** BitLocker est souvent stockée dans Active Directory (vérifiable par les administrateurs), dans le compte Microsoft de l'utilisateur, ou sur un support physique (papier, clé USB). La recovery key FileVault est stockable dans le compte Apple (iCloud) ou par un administrateur MDM. Les clés LUKS n'ont pas de recovery centralisé — si la passphrase est perdue et que la RAM n'a pas été dumpée, les données sont inaccessibles.

Le **TPM** (Trusted Platform Module) protège la clé BitLocker sur les machines modernes, mais il la libère automatiquement au boot normal — une acquisition à chaud (machine allumée avec le volume déverrouillé) contourne cette protection.

## 5.6 RAID, NAS et serveurs virtualisés

Les serveurs utilisent généralement des configurations RAID. Deux approches : acquisition disque par disque (acquérir individuellement chaque disque du RAID, puis reconstruire le volume logique avec X-Ways, Autopsy, ou `mdadm` — méthode la plus sûre car elle préserve les données brutes de chaque disque) ou acquisition du volume logique via le contrôleur (capture directe du volume RAID reconstruit — plus rapide, mais perte des données résiduelles au niveau physique).

Les **NAS** et serveurs de fichiers en production posent la question de l'acquisition à chaud. Un NAS ne peut pas toujours être éteint et retiré du rack (impact sur la production). L'acquisition à chaud — via le réseau (FTK Imager en mode réseau, ou `dd` via SSH) ou via un snapshot — est souvent le seul choix, mais elle est moins « propre » qu'une acquisition physique avec write blocker car le système de fichiers peut évoluer pendant la copie.

Les **machines virtuelles** sont un cas favorable : l'image VMDK (VMware), VHDX (Hyper-V), ou QCOW2 (KVM/QEMU) EST le disque. Il suffit de copier le fichier d'image de la VM ou de prendre un snapshot (qui gèle l'état du disque à un instant T). Le snapshot de VM est l'équivalent fonctionnel d'une acquisition à chaud avec write blocker — et il capture simultanément la mémoire si la VM est en cours d'exécution.

## 5.7 Fil rouge — MUSIC BOX : l'acquisition disque

> **🔬 MUSIC BOX — Épisode 5**
>
> Samedi 9h00. Maître Fournier (experte judiciaire) est sur site. L'acquisition formelle commence.
>
> **WKS-RD-047** (SSD NVMe 512 Go, Windows 11, BitLocker activé) : la machine est encore allumée (le dump RAM a été fait la veille — la clé BitLocker est en mémoire). Acquisition physique via FTK Imager avec write blocker Tableau T35es. Format E01, segmenté en fichiers de 4 Go. Durée : 45 minutes. Hash MD5 + SHA-256 calculés automatiquement : correspondance vérifiée. Documenté dans le formulaire de chaîne de custody, signé par Maître Fournier.
>
> **SRV-RD-01** (serveur Linux Ubuntu 22.04, RAID 5 × 4 disques de 2 To) : le serveur est en production, les expériences en cours ne peuvent pas être interrompues. Décision : acquisition logique via `dc3dd` sur le réseau (accès SSH), ciblée sur les répertoires `/home/`, `/var/log/`, `/tmp/`, et `/opt/research/`. Image physique reportée à l'arrêt de maintenance (J+5). Hash calculé sur chaque acquisition partielle.

---
