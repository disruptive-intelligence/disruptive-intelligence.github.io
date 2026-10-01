---
title: "Paquets et logiciels"
cours:
  - library/it/linux/administration-linux/index.md
---

# Paquets et logiciels

Mettre à jour, chercher, installer, retrouver d'où vient un fichier ; installer un outil Python ou depuis Git.

Les incontournables : `apt update && apt upgrade` · `apt search` · `apt install` · `dpkg -S` · `pipx install`
{ .kw-cs-top }

## Debian, Ubuntu, Kali (apt)

### Mettre à jour le système

```bash title="Commande"
sudo apt update && sudo apt upgrade
```

```bash title="Exemple"
sudo apt update && sudo apt full-upgrade -y
```

Pour comprendre : [Administration Linux, ch. 20](../../../library/it/linux/administration-linux/06-partie-6-entretenir-le-systeme/01-chapitre-20-gerer-les-paquets-et-logiciels.md)
{ .kw-cs-meta }

### Chercher un paquet

```bash title="Commande"
apt search <mot>
```

```bash title="Exemple"
apt search impacket
```

```bash title="Exemple 2"
apt show nmap   # description et version disponible
```

### Installer ou supprimer un paquet

```bash title="Commande"
sudo apt install <paquet>
sudo apt remove <paquet>
```

```bash title="Exemple"
sudo apt install -y nmap
```

```bash title="Exemple 2"
sudo apt purge apache2 && sudo apt autoremove   # supprime aussi la configuration et les dépendances inutiles
```

### Savoir si un paquet est installé et sa version

```bash title="Commande"
apt policy <paquet>
```

```bash title="Exemple"
apt policy openssh-server
```

```bash title="Exemple 2"
dpkg -l | grep -i ssh
```

### Savoir quel paquet a installé un fichier

```bash title="Commande"
dpkg -S <chemin>
```

```bash title="Exemple"
dpkg -S /usr/sbin/sshd
```

```bash title="Exemple 2"
dpkg -L openssh-server   # et l'inverse : les fichiers d'un paquet
```

### Installer un fichier .deb téléchargé

```bash title="Commande"
sudo apt install ./<fichier>.deb
```

```bash title="Exemple"
sudo apt install ./outil_1.2_amd64.deb   # apt résout les dépendances, pas dpkg -i
```

## Outils hors paquets

### Installer un outil Python

```bash title="Commande"
pipx install <outil>
```

```bash title="Exemple"
pipx install impacket
```

```bash title="Exemple 2"
python3 -m pip install --user requests   # une bibliothèque pour ses scripts
```

### Récupérer un outil depuis Git

```bash title="Commande"
git clone <url> <dossier>
```

```bash title="Exemple"
git clone https://github.com/<auteur>/<projet>.git /opt/projet
```

## Repères : équivalents d'une famille à l'autre

| Besoin | Debian, Ubuntu | RHEL, Fedora | Arch |
|---|---|---|---|
| Mettre à jour | `apt update && apt upgrade` | `dnf upgrade` | `pacman -Syu` |
| Installer | `apt install` | `dnf install` | `pacman -S` |
| Chercher | `apt search` | `dnf search` | `pacman -Ss` |
| Fichier → paquet | `dpkg -S` | `rpm -qf` | `pacman -Qo` |
