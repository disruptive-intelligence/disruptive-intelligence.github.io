---
title: "Disques, archives et transferts"
cours:
  - library/it/linux/administration-linux/index.md
---

# Disques, archives et transferts

Espace disque, partitions et montages ; archives ; copier des fichiers vers une autre machine.

Les incontournables : `df -h` · `du -sh` · `lsblk -f` · `tar -czf` · `scp` · `rsync -avz`
{ .kw-cs-top }

## Espace et disques

### Voir l'espace disque

```bash title="Commande"
df -h   # -h : tailles lisibles ; df -i : inodes
```

```bash title="Exemple"
df -h /
```

??? example "Sortie"
    ```text
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/sda2        48G   41G  4.6G  90% /
    ```

```bash title="Exemple 2"
df -i   # « disque plein » alors qu'il reste de la place : plus d'inodes
```

Pour comprendre : [Administration Linux, ch. 21](../../../library/it/linux/administration-linux/06-partie-6-entretenir-le-systeme/02-chapitre-21-stockage-et-espace-disque.md)
{ .kw-cs-meta }

### Trouver ce qui occupe la place

```bash title="Commande"
du -sh <dossier>/* | sort -h   # -s total par élément, -h lisible ; sort -h trie les tailles
```

```bash title="Exemple"
sudo du -sh /var/* 2>/dev/null | sort -h | tail -3
```

??? example "Sortie"
    ```text
    1.9G	/var/cache
    2.4G	/var/log
    6.8G	/var/lib
    ```

### Lister disques et partitions

```bash title="Commande"
lsblk -f          # arborescence des disques, systèmes de fichiers
sudo fdisk -l     # tailles et tables de partitions
```

```bash title="Exemple"
lsblk -f
```

??? example "Sortie"
    ```text
    NAME   FSTYPE FSVER LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
    sda
    ├─sda1 vfat   FAT32       4C1E-2A7B                             1G     1% /boot/efi
    └─sda2 ext4   1.0         1b5c7a9e-3d2f-4e6a-8b1c-9d0e1f2a3b4c  4.6G    90% /
    sdb
    └─sdb1 exfat  1.0   USB   61C2-0A44
    ```

```bash title="Exemple 2"
sudo fdisk -l
```

### Monter ou démonter un disque

```bash title="Commande"
sudo mount <périphérique> <point_de_montage>   # -o ro : lecture seule
sudo umount <point_de_montage>
```

```bash title="Exemple"
sudo mkdir -p /mnt/usb && sudo mount /dev/sdb1 /mnt/usb
```

```bash title="Exemple 2"
sudo mount -o ro,noexec /dev/sdb1 /mnt/usb   # lecture seule, rien d'exécutable (support douteux)
```

## Archives

### Créer une archive compressée

```bash title="Commande"
tar -czf <archive>.tar.gz <dossier>   # c créer, z compresser (gzip), f fichier
```

```bash title="Exemple"
sudo tar -czf etc-$(date +%F).tar.gz /etc
```

```bash title="Exemple 2"
zip -r projet.zip projet/
```

Pour comprendre : [Administration Linux, ch. 22](../../../library/it/linux/administration-linux/06-partie-6-entretenir-le-systeme/03-chapitre-22-archives-et-compression.md)
{ .kw-cs-meta }

### Extraire ou lister une archive

```bash title="Commande"
tar -xzf <archive>.tar.gz -C <dossier>   # x extraire ; t au lieu de x : lister
```

```bash title="Exemple"
tar -xzf etc-2026-10-01.tar.gz -C /tmp/restau
```

```bash title="Exemple 2"
tar -tzf etc-2026-10-01.tar.gz | head -3
```

??? example "Sortie"
    ```text
    etc/
    etc/hostname
    etc/hosts
    ```

## Transferts

### Copier un fichier vers une autre machine

```bash title="Commande"
scp <fichier> <utilisateur>@<hôte>:<chemin>   # -r pour un dossier
rsync -avz <source> <utilisateur>@<hôte>:<dest>   # reprend là où il s'est arrêté
```

```bash title="Exemple"
scp rapport.pdf alice@192.168.1.20:/tmp/
```

??? example "Sortie"
    ```text
    rapport.pdf                                   100% 2048KB  11.2MB/s   00:00
    ```

```bash title="Exemple 2"
rsync -avz --progress /srv/data/ alice@192.168.1.20:/sauvegarde/data/
```

Pour comprendre : [Administration Linux, ch. 19](../../../library/it/linux/administration-linux/05-partie-5-linux-en-reseau/03-chapitre-19-transferer-des-fichiers.md)
{ .kw-cs-meta }

### Télécharger un fichier

```bash title="Commande"
curl -O <url>   # -L : suit les redirections
wget <url>
```

```bash title="Exemple"
curl -LO https://example.com/outil.tar.gz
```

??? example "Sortie"
    ```text
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
    100 4211k  100 4211k    0     0  9876k      0 --:--:-- --:--:-- --:--:-- 9884k
    ```

### Servir un dossier en HTTP pour un transfert rapide

```bash title="Commande"
python3 -m http.server <port> --directory <dossier>
```

```bash title="Exemple"
python3 -m http.server 8000 --directory /tmp/partage
```

??? example "Sortie"
    ```text
    Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
    192.168.1.23 - - [02/Oct/2026 10:02:11] "GET /rapport.pdf HTTP/1.1" 200 -
    ```

!!! warning "Attention"
    Tout le dossier devient lisible par le réseau, sans authentification : à couper juste après.
