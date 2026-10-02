---
title: "Système et arborescence"
cours:
  - library/it/linux/administration-linux/index.md
  - library/it/linux/linux-prises-de-notes/index.md
---

# Système et arborescence

Identifier la machine, se repérer dans l'arborescence, savoir qui est connecté.

Les incontournables : `cat /etc/os-release` · `uname -a` · `hostnamectl` · `ls -lah` · `w` · `last`
{ .kw-cs-top }

## Identifier la machine

### Connaître la distribution et sa version

```bash title="Commande"
cat /etc/os-release   # nom, version et famille de la distribution
```

```bash title="Exemple"
grep -E '^(NAME|VERSION)=' /etc/os-release
```

??? example "Sortie"
    ```text
    NAME="Ubuntu"
    VERSION="24.04.1 LTS (Noble Numbat)"
    ```

Pour comprendre : [Linux — prises de notes, fondamentaux](../../../library/it/linux/linux-prises-de-notes/01-fondamentaux-du-systeme.md)
{ .kw-cs-meta }

### Connaître le noyau et l'architecture

```bash title="Commande"
uname -<option>   # -a tout, -r version du noyau, -m architecture
```

```bash title="Exemple"
uname -a
```

??? example "Sortie"
    ```text
    Linux srv-web-01 6.8.0-45-generic #45-Ubuntu SMP PREEMPT_DYNAMIC Fri Aug 30 12:02:04 UTC 2024 x86_64 GNU/Linux
    ```

```bash title="Exemple 2"
uname -r && uname -m   # version du noyau, puis architecture
```

### Connaître le nom d'hôte, le fuseau et l'heure

```bash title="Commande"
hostnamectl   # nom d'hôte, OS, noyau, type de machine
timedatectl   # heure locale et UTC, fuseau, synchronisation NTP
```

```bash title="Exemple"
hostnamectl
```

??? example "Sortie"
    ```text
     Static hostname: srv-web-01
    Operating System: Ubuntu 24.04.1 LTS
              Kernel: Linux 6.8.0-45-generic
        Architecture: x86-64
    ```

```bash title="Exemple 2"
timedatectl | grep -E 'Local time|Time zone|synchronized'
```

### Voir depuis quand la machine tourne et sa charge

```bash title="Commande"
uptime   # heure, durée de fonctionnement, utilisateurs, charge
```

```bash title="Exemple"
uptime
```

??? example "Sortie"
    ```text
     09:41:22 up 3 days,  4:12,  2 users,  load average: 0.31, 0.27, 0.22
    ```

```bash title="Exemple 2"
uptime -p   # seulement la durée, en clair
```

Pour comprendre : [Administration Linux, ch. 24](../../../library/it/linux/administration-linux/07-partie-7-diagnostiquer-securiser-automatiser/01-chapitre-24-diagnostic-systeme-methode.md)
{ .kw-cs-meta }

### Voir le matériel : processeur, mémoire, disques, périphériques

```bash title="Commande"
lscpu   # processeur
free -h   # mémoire
lsblk    # disques et partitions
lsusb    # périphériques USB
lspci    # cartes (réseau, graphique…)
```

```bash title="Exemple"
lscpu | grep -E 'Model name|^CPU\(s\)'
```

??? example "Sortie"
    ```text
    CPU(s):                 4
    Model name:             Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz
    ```

```bash title="Exemple 2"
free -h && lsblk -f
```

## Se repérer

### Savoir où l'on est et lister un dossier

```bash title="Commande"
pwd                # dossier courant
ls -lah <dossier>  # détail, fichiers cachés, tailles lisibles
```

```bash title="Exemple"
ls -lah /etc/ssh
```

??? example "Sortie"
    ```text
    total 548K
    drwxr-xr-x   4 root root 4.0K Sep 12 10:02 .
    drwxr-xr-x 112 root root 4.0K Oct  1 08:15 ..
    -rw-r--r--   1 root root 3.2K Sep 12 10:02 sshd_config
    -rw-------   1 root root  505 Mar 14  2026 ssh_host_ecdsa_key
    ```

Pour comprendre : [Administration Linux, ch. 2](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/02-chapitre-2-se-reperer-dans-l-arborescence.md)
{ .kw-cs-meta }

### Afficher l'arborescence d'un dossier

```bash title="Commande"
tree -L <profondeur> <dossier>   # -L : nombre de niveaux affichés
```

```bash title="Exemple"
tree -L 2 /var/log
```

??? example "Sortie"
    ```text
    /var/log
    ├── apt
    │   ├── history.log
    │   └── term.log
    ├── auth.log
    ├── nginx
    │   ├── access.log
    │   └── error.log
    └── syslog
    ```

```bash title="Exemple 2"
find /var/log -maxdepth 2 -type d   # si tree n'est pas installé
```

### Identifier le type d'un fichier

```bash title="Commande"
file <fichier>   # binaire, script, texte, image, archive…
```

```bash title="Exemple"
file /usr/bin/passwd
```

??? example "Sortie"
    ```text
    /usr/bin/passwd: setuid ELF 64-bit LSB pie executable, x86-64, dynamically linked, stripped
    ```

### Savoir où est un programme et ce qu'il est réellement

```bash title="Commande"
command -v <programme>   # chemin du programme utilisé
type -a <programme>      # toutes les correspondances (alias, binaires)
```

```bash title="Exemple"
type -a python3
```

??? example "Sortie"
    ```text
    python3 is /usr/bin/python3
    python3 is /bin/python3
    ```

```bash title="Exemple 2"
readlink -f "$(command -v python3)"   # le vrai binaire derrière les liens
```

Pour comprendre : [Administration Linux, ch. 1](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/01-chapitre-1-le-terminal-le-shell-et-l-aide.md)
{ .kw-cs-meta }

## Qui est là

### Voir qui est connecté maintenant

```bash title="Commande"
w   # qui, depuis où, depuis quand, quelle commande
```

```bash title="Exemple"
w -h
```

??? example "Sortie"
    ```text
    alice  pts/0  192.168.1.23  09:12   0.00s  0.04s  0.00s w -h
    bob    pts/1  192.168.1.40  08:47  12:30   0.10s  0.10s -bash
    ```

Ensuite : [voir les dernières connexions](#voir-les-dernieres-connexions)
{ .kw-cs-meta }

### Voir les dernières connexions

```bash title="Commande"
last -n <nombre>   # les N dernières connexions, -a : origine en fin de ligne
```

```bash title="Exemple"
last -n 20 -a
```

??? example "Sortie"
    ```text
    alice   pts/0        Wed Oct  1 09:12   still logged in    192.168.1.23
    bob     pts/1        Wed Oct  1 08:47 - 09:30  (00:43)     192.168.1.40
    reboot  system boot  Mon Sep 29 05:02   still running      6.8.0-45-generic
    ```

```bash title="Exemple 2"
sudo lastb -n 20   # tentatives échouées (lit /var/log/btmp)
```

Pour comprendre : [Linux — prises de notes, investigation](../../../library/it/linux/linux-prises-de-notes/02-investigation-forensics.md)
{ .kw-cs-meta }

## Repères : où sont les choses

| Dossier | Contenu |
|---|---|
| `/etc` | Configuration du système et des applications |
| `/var/log` | Journaux |
| `/home`, `/root` | Dossiers personnels (`/root` pour root) |
| `/tmp`, `/var/tmp` | Fichiers temporaires (souvent modifiables par tous) |
| `/opt` | Logiciels tiers |
| `/usr/bin`, `/usr/sbin` | Commandes (`sbin` : administration) |
| `/proc` | Processus en cours et paramètres du noyau (virtuel) |
| `/dev` | Périphériques |
| `/boot` | Noyau et chargeur de démarrage |
