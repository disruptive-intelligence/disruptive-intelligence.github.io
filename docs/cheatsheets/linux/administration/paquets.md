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
sudo apt update    # rafraîchit la liste des paquets
sudo apt upgrade   # installe les mises à jour
```

```bash title="Exemple"
sudo apt update && sudo apt full-upgrade -y
```

??? example "Sortie"
    ```text
    Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease
    Reading package lists... Done
    12 packages can be upgraded. Run 'apt list --upgradable' to see them.
    ```

Pour comprendre : [Administration Linux, ch. 20](../../../library/it/linux/administration-linux/06-partie-6-entretenir-le-systeme/01-chapitre-20-gerer-les-paquets-et-logiciels.md)
{ .kw-cs-meta }

### Chercher un paquet

```bash title="Commande"
apt search <mot>   # apt show <paquet> : description et version
```

```bash title="Exemple"
apt search impacket
```

??? example "Sortie"
    ```text
    python3-impacket/noble 0.11.0-2 all
      Python3 module to easily build and dissect network protocols
    ```

```bash title="Exemple 2"
apt show nmap
```

### Installer ou supprimer un paquet

```bash title="Commande"
sudo apt install <paquet>   # -y : sans confirmation
sudo apt remove <paquet>    # purge : supprime aussi la configuration
```

```bash title="Exemple"
sudo apt install -y nmap
```

??? example "Sortie"
    ```text
    Setting up nmap (7.94+git20230807.3be01efb1+dfsg-3build2) ...
    ```

```bash title="Exemple 2"
sudo apt purge apache2 && sudo apt autoremove
```

### Savoir si un paquet est installé et sa version

```bash title="Commande"
apt policy <paquet>   # Installed : installée, Candidate : disponible
```

```bash title="Exemple"
apt policy openssh-server
```

??? example "Sortie"
    ```text
    openssh-server:
      Installed: 1:9.6p1-3ubuntu13.5
      Candidate: 1:9.6p1-3ubuntu13.5
    ```

```bash title="Exemple 2"
dpkg -l | grep -i ssh
```

### Savoir quel paquet a installé un fichier

```bash title="Commande"
dpkg -S <chemin>   # fichier -> paquet
dpkg -L <paquet>   # paquet -> fichiers
```

```bash title="Exemple"
dpkg -S /usr/sbin/sshd
```

??? example "Sortie"
    ```text
    openssh-server: /usr/sbin/sshd
    ```

```bash title="Exemple 2"
dpkg -L openssh-server
```

### Installer un fichier .deb téléchargé

```bash title="Commande"
sudo apt install ./<fichier>.deb   # le ./ indique un fichier local
```

```bash title="Exemple"
sudo apt install ./outil_1.2_amd64.deb
```

## Outils hors paquets

### Installer un outil Python

```bash title="Commande"
pipx install <outil>   # outil en ligne de commande
python3 -m pip install --user <paquet>   # bibliothèque pour ses scripts
```

```bash title="Exemple"
pipx install impacket
```

??? example "Sortie"
    ```text
      installed package impacket 0.12.0, installed using Python 3.12.3
      These apps are now globally available
        - secretsdump.py
        - smbclient.py
    ```

### Récupérer un outil depuis Git

```bash title="Commande"
git clone <url> <dossier>
```

```bash title="Exemple"
git clone https://github.com/<auteur>/<projet>.git /opt/projet
```

??? example "Sortie"
    ```text
    Cloning into '/opt/projet'...
    Receiving objects: 100% (1532/1532), 2.41 MiB | 8.10 MiB/s, done.
    ```

## Repères : équivalents d'une famille à l'autre

| Besoin | Debian, Ubuntu | RHEL, Fedora | Arch |
|---|---|---|---|
| Mettre à jour | `apt update && apt upgrade` | `dnf upgrade` | `pacman -Syu` |
| Installer | `apt install` | `dnf install` | `pacman -S` |
| Chercher | `apt search` | `dnf search` | `pacman -Ss` |
| Fichier → paquet | `dpkg -S` | `rpm -qf` | `pacman -Qo` |
