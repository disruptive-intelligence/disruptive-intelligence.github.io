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
df -h
```

```bash title="Exemple"
df -h /   # la partition racine
```

```bash title="Exemple 2"
df -i   # inodes : « disque plein » alors qu'il reste de la place
```

Pour comprendre : [Administration Linux, ch. 21](../../../library/it/linux/administration-linux/06-partie-6-entretenir-le-systeme/02-chapitre-21-stockage-et-espace-disque.md)
{ .kw-cs-meta }

### Trouver ce qui occupe la place

```bash title="Commande"
du -sh <dossier>/* | sort -h
```

```bash title="Exemple"
sudo du -sh /var/* 2>/dev/null | sort -h
```

### Lister disques et partitions

```bash title="Commande"
lsblk -f
```

```bash title="Exemple"
lsblk -f
```

```bash title="Exemple 2"
sudo fdisk -l   # tailles et tables de partitions
```

### Monter ou démonter un disque

```bash title="Commande"
sudo mount <périphérique> <point_de_montage>
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
tar -czf <archive>.tar.gz <dossier>
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
tar -xzf <archive>.tar.gz -C <dossier>
```

```bash title="Exemple"
tar -xzf etc-2026-10-01.tar.gz -C /tmp/restau
```

```bash title="Exemple 2"
tar -tzf etc-2026-10-01.tar.gz | head   # lister sans extraire
```

## Transferts

### Copier un fichier vers une autre machine

```bash title="Commande"
scp <fichier> <utilisateur>@<hôte>:<chemin>
```

```bash title="Exemple"
scp rapport.pdf alice@192.168.1.20:/tmp/
```

```bash title="Exemple 2"
rsync -avz --progress /srv/data/ alice@192.168.1.20:/sauvegarde/data/   # reprend là où il s'est arrêté
```

Pour comprendre : [Administration Linux, ch. 19](../../../library/it/linux/administration-linux/05-partie-5-linux-en-reseau/03-chapitre-19-transferer-des-fichiers.md)
{ .kw-cs-meta }

### Télécharger un fichier

```bash title="Commande"
curl -O <url>
wget <url>
```

```bash title="Exemple"
curl -LO https://example.com/outil.tar.gz   # -L suit les redirections
```

### Servir un dossier en HTTP pour un transfert rapide

```bash title="Commande"
python3 -m http.server <port> --directory <dossier>
```

```bash title="Exemple"
python3 -m http.server 8000 --directory /tmp/partage
```

!!! warning "Attention"
    Tout le dossier devient lisible par le réseau, sans authentification : à couper juste après.
