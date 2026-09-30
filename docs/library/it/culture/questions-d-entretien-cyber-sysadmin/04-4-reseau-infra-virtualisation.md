---
title: 4) Réseau / Infra / Virtualisation
source: IT/Culture/Questions_Entretien_Cyber_SysAdmin.md
note: Questions d'entretien cyber & sysadmin
up:
- - Questions d'entretien cyber & sysadmin
  - index.md
---

---

- **Question : Qu'est-ce qu'un RAID ?**
  **Réponse type :** RAID (Redundant Array of Independent Disks) est une technologie qui combine plusieurs disques physiques pour améliorer la performance, la redondance, ou les deux. L'idée c'est soit d'aller plus vite en répartissant les données (striping), soit de résister à la panne d'un disque (mirroring/parité), soit un mix des deux.

- **Question : Quelle différence entre RAID 0, RAID 1, RAID 5, RAID 6 et RAID 10 ?**
  **Réponse type :** RAID 0 (striping) répartit les données sur tous les disques sans redondance — ça double les performances mais si un seul disque tombe, tout est perdu. RAID 1 (mirroring) duplique les données sur deux disques — redondance totale, perte de 50% de la capacité. RAID 5 répartit les données avec de la parité distribuée sur au moins 3 disques — tolère la perte d'un disque, bonne capacité utile (n-1 disques). RAID 6 c'est comme le RAID 5 mais avec double parité — tolère la perte de 2 disques simultanément. RAID 10 (1+0) combine mirroring et striping — performance et redondance, mais coûteux (50% de la capacité utile, minimum 4 disques). En production critique, RAID 6 ou RAID 10 sont recommandés.

- **Question : Qu'est-ce que le kernel space et le user space ?**
  **Réponse type :** Le kernel space (Ring 0) c'est la zone mémoire où s'exécutent le noyau du système d'exploitation et les drivers — accès total au matériel et à toute la mémoire. Un crash ici provoque un écran bleu (Windows) ou un kernel panic (Linux). Le user space (Ring 3, ou userland) c'est la zone où tournent les applications normales — accès limité et contrôlé. Un crash en user space ne fait planter que le processus concerné. Cette séparation est la base de la sécurité : un processus utilisateur ne peut pas accéder directement au matériel ou à la mémoire d'un autre processus — il doit passer par des syscalls contrôlés par le noyau.

- **Question : Quelle différence concrète entre une machine virtuelle et un conteneur ?**
  **Réponse type :** La VM embarque un OS complet avec son propre kernel, au-dessus d'un hyperviseur. Chaque VM est fortement isolée mais consomme des Go de RAM et met des minutes à démarrer. Le container partage le kernel de l'hôte et n'embarque que l'application et ses dépendances — il démarre en secondes et consomme très peu. L'isolation d'un container est moins forte (kernel partagé) mais suffisante pour la plupart des usages. En sécurité : un escape de container donne accès au kernel de l'hôte, un escape de VM est beaucoup plus difficile.

- **Question : Quelle différence entre un NAS et un SAN ?**
  **Réponse type :** Un NAS (Network Attached Storage) est un serveur de fichiers accessible via le réseau IP (protocoles SMB, NFS). Il partage des fichiers — c'est simple à déployer, utilisé pour le partage de fichiers classique et les sauvegardes. Un SAN (Storage Area Network) est un réseau de stockage dédié qui fournit des volumes de blocs bruts (protocoles Fibre Channel, iSCSI). Le serveur voit le stockage SAN comme un disque local. Le SAN est utilisé pour les bases de données, la virtualisation — là où les performances I/O sont critiques. En résumé : le NAS partage des fichiers, le SAN partage du stockage bloc.

- **Question : Quelle différence entre vCenter et vSphere ?**
  **Réponse type :** vSphere c'est la suite complète de virtualisation VMware — c'est le nom commercial de l'ensemble. ESXi est l'hyperviseur bare-metal qui s'installe sur chaque serveur physique. vCenter est la console d'administration centralisée qui permet de gérer plusieurs ESXi : migration de VMs (vMotion), HA, DRS, templates, snapshots. Sans vCenter, on administre chaque ESXi individuellement. En sécurité, vCenter est un composant Tier 0 — sa compromission donne le contrôle total sur toute l'infrastructure virtualisée.

- **Question : Comment fonctionne le swap ?**
  **Réponse type :** Le swap c'est une zone du disque utilisée comme extension de la RAM quand la mémoire physique est pleine. Quand le système manque de RAM, il déplace les pages mémoire les moins utilisées (pages inactives) vers le swap sur le disque pour libérer de la RAM pour les processus actifs. C'est beaucoup plus lent que la RAM. Sous Linux, c'est soit une partition swap soit un fichier swap (`swapon`, `swapoff`). En forensic, le swap (pagefile.sys sur Windows, swap sur Linux) peut contenir des fragments de données sensibles — credentials, code malveillant — car la mémoire y a été copiée.

---
