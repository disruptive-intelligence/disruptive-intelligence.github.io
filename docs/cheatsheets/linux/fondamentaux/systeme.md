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
cat /etc/os-release
```

```bash title="Exemple"
grep -E '^(NAME|VERSION)=' /etc/os-release
```

Pour comprendre : [Linux — prises de notes, fondamentaux](../../../library/it/linux/linux-prises-de-notes/01-fondamentaux-du-systeme.md)
{ .kw-cs-meta }

### Connaître le noyau et l'architecture

```bash title="Commande"
uname -<option>
```

```bash title="Exemple"
uname -a
```

```bash title="Exemple 2"
uname -r && uname -m   # version du noyau, puis architecture (x86_64, aarch64)
```

### Connaître le nom d'hôte, le fuseau et l'heure

```bash title="Commande"
hostnamectl
timedatectl
```

```bash title="Exemple"
hostnamectl status
```

```bash title="Exemple 2"
timedatectl | grep -E 'Local time|Time zone|synchronized'   # l'horloge est-elle synchronisée ?
```

### Voir depuis quand la machine tourne et sa charge

```bash title="Commande"
uptime
```

```bash title="Exemple"
uptime -p   # « up 3 days, 4 hours »
```

Pour comprendre : [Administration Linux, ch. 24](../../../library/it/linux/administration-linux/07-partie-7-diagnostiquer-securiser-automatiser/01-chapitre-24-diagnostic-systeme-methode.md)
{ .kw-cs-meta }

### Voir le matériel : processeur, mémoire, disques, périphériques

```bash title="Commande"
lscpu
free -h
lsblk
lsusb
lspci
```

```bash title="Exemple"
lscpu | grep -E 'Model name|^CPU\(s\)'
```

```bash title="Exemple 2"
free -h && lsblk -f   # mémoire, puis disques avec leurs systèmes de fichiers
```

## Se repérer

### Savoir où l'on est et lister un dossier

```bash title="Commande"
pwd
ls -lah <dossier>
```

```bash title="Exemple"
ls -lah /etc/ssh
```

Pour comprendre : [Administration Linux, ch. 2](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/02-chapitre-2-se-reperer-dans-l-arborescence.md)
{ .kw-cs-meta }

### Afficher l'arborescence d'un dossier

```bash title="Commande"
tree -L <profondeur> <dossier>
```

```bash title="Exemple"
tree -L 2 /var/log
```

```bash title="Exemple 2"
find /var/log -maxdepth 2 -type d   # si tree n'est pas installé
```

### Identifier le type d'un fichier

```bash title="Commande"
file <fichier>
```

```bash title="Exemple"
file /usr/bin/passwd   # binaire ELF, script, texte…
```

### Savoir où est un programme et ce qu'il est réellement

```bash title="Commande"
command -v <programme>
type -a <programme>
```

```bash title="Exemple"
type -a python3
```

```bash title="Exemple 2"
readlink -f "$(command -v python3)"   # le vrai binaire derrière les liens symboliques
```

Pour comprendre : [Administration Linux, ch. 1](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/01-chapitre-1-le-terminal-le-shell-et-l-aide.md)
{ .kw-cs-meta }

## Qui est là

### Voir qui est connecté maintenant

```bash title="Commande"
w
```

```bash title="Exemple"
w -h   # utilisateurs, terminal, origine, commande en cours
```

Ensuite : [voir les dernières connexions](#voir-les-dernieres-connexions)
{ .kw-cs-meta }

### Voir les dernières connexions

```bash title="Commande"
last -n <nombre>
```

```bash title="Exemple"
last -n 20 -a
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
