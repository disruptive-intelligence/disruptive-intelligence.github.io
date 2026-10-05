---
title: "Droits et identités"
cours:
  - library/it/linux/administration-linux/index.md
---

# Droits et identités

Lire et changer les droits, savoir qui je suis et ce que je peux faire, repérer les droits dangereux.

Les incontournables : `ls -l` · `chmod` · `chown` · `id` · `sudo -l` · `find / -perm -4000`
{ .kw-cs-top }

## Lire et changer

### Lire les droits d'un fichier

```bash title="Commande"
ls -l <fichier>                    # droits, propriétaire, groupe
stat -c '%A %U:%G %n' <fichier>    # même chose, en une ligne choisie
```

```bash title="Exemple"
ls -l /etc/shadow
```

??? example "Sortie"
    ```text
    -rw-r----- 1 root shadow 1442 Sep 12 10:02 /etc/shadow
    ```

Pour comprendre : [Administration Linux, ch. 9](../../../library/it/linux/administration-linux/03-partie-3-qui-a-le-droit-de-quoi/01-chapitre-9-comprendre-les-permissions.md)
{ .kw-cs-meta }

### Changer les droits d'un fichier

```bash title="Commande"
chmod <mode> <fichier>   # u/g/o + r/w/x (u+x), ou en octal (640, 755)
```

```bash title="Exemple"
chmod +x deploie.sh
```

```bash title="Exemple 2"
chmod 640 /etc/app/config.ini   # rw- r-- --- : propriétaire lit/écrit, groupe lit
```

### Changer le propriétaire d'un fichier

```bash title="Commande"
sudo chown <utilisateur>:<groupe> <fichier>   # -R : tout le dossier
```

```bash title="Exemple"
sudo chown -R www-data:www-data /var/www/site
```

Pour comprendre : [Administration Linux, ch. 10](../../../library/it/linux/administration-linux/03-partie-3-qui-a-le-droit-de-quoi/02-chapitre-10-propriete-utilisateurs-et-groupes.md)
{ .kw-cs-meta }

### Voir les droits fins (ACL)

```bash title="Commande"
getfacl <fichier>                         # lire les ACL
setfacl -m u:<utilisateur>:<droits> <f>   # en ajouter
```

```bash title="Exemple"
getfacl /srv/partage
```

??? example "Sortie"
    ```text
    # file: srv/partage
    # owner: root
    # group: projet-x
    user::rwx
    user:alice:r-x
    group::rwx
    other::---
    ```

```bash title="Exemple 2"
sudo setfacl -m u:alice:rx /srv/partage   # donner lecture à alice
```

Pour comprendre : [Administration Linux, ch. 12](../../../library/it/linux/administration-linux/03-partie-3-qui-a-le-droit-de-quoi/04-chapitre-12-permissions-avancees-panorama.md)
{ .kw-cs-meta }

## Identités

### Savoir qui je suis et ce que sudo m'autorise

```bash title="Commande"
id        # UID, groupe principal, groupes
sudo -l   # commandes autorisées avec sudo
```

```bash title="Exemple"
id
```

??? example "Sortie"
    ```text
    uid=1000(alice) gid=1000(alice) groups=1000(alice),27(sudo),998(docker)
    ```

```bash title="Exemple 2"
sudo -l
```

Pour comprendre : [Administration Linux, ch. 11](../../../library/it/linux/administration-linux/03-partie-3-qui-a-le-droit-de-quoi/03-chapitre-11-sudo-et-l-elevation-de-privileges.md)
{ .kw-cs-meta }

### Lister les comptes du système

```bash title="Commande"
getent passwd   # tous les comptes, un par ligne
```

```bash title="Exemple"
getent passwd | awk -F: '$3 >= 1000 {print $1}'
```

??? example "Sortie"
    ```text
    nobody
    alice
    bob
    ```

```bash title="Exemple 2"
awk -F: '$7 !~ /(nologin|false)$/ {print $1, $7}' /etc/passwd   # comptes qui ont un shell
```

### Lister les membres d'un groupe

```bash title="Commande"
getent group <groupe>   # nom:x:GID:membres
```

```bash title="Exemple"
getent group sudo
```

??? example "Sortie"
    ```text
    sudo:x:27:alice,bob
    ```

## Droits à surveiller

### Trouver les fichiers SUID ou SGID

```bash title="Commande"
find / -perm -4000 -type f 2>/dev/null   # SUID ; -2000 pour SGID
```

```bash title="Exemple"
find / -perm -4000 -type f -exec ls -l {} \; 2>/dev/null | head -3
```

??? example "Sortie"
    ```text
    -rwsr-xr-x 1 root root  59976 Feb  6  2026 /usr/bin/passwd
    -rwsr-xr-x 1 root root 277936 Jun 25  2026 /usr/bin/sudo
    -rwsr-xr-x 1 root root  72072 Feb  6  2026 /usr/bin/gpasswd
    ```

```bash title="Exemple 2"
find / -perm -2000 -type f 2>/dev/null
```

Pour comprendre : [Administration Linux, ch. 12](../../../library/it/linux/administration-linux/03-partie-3-qui-a-le-droit-de-quoi/04-chapitre-12-permissions-avancees-panorama.md)
{ .kw-cs-meta }

### Trouver les fichiers modifiables par tous

```bash title="Commande"
find <dossier> -xdev -type f -perm -o+w 2>/dev/null   # -xdev : reste sur ce disque
```

```bash title="Exemple"
find /etc /usr -xdev -type f -perm -o+w 2>/dev/null
```

??? example "Sortie"
    ```text
    /etc/app/scripts/maintenance.sh
    ```

### Voir les capabilities des binaires

```bash title="Commande"
getcap -r <dossier> 2>/dev/null   # -r : récursif
```

```bash title="Exemple"
getcap -r /usr 2>/dev/null
```

??? example "Sortie"
    ```text
    /usr/bin/ping cap_net_raw=ep
    /usr/bin/python3.12 cap_setuid=ep
    ```

## Vue d'ensemble : lire `rwx`

| Notation | Octal | Sens |
|---|---|---|
| `r--` | 4 | lecture |
| `-w-` | 2 | écriture |
| `--x` | 1 | exécution (ou traverser un dossier) |
| `rw-r-----` | 640 | propriétaire lit/écrit, groupe lit, les autres rien |
| `rwxr-xr-x` | 755 | propriétaire tout, les autres lisent et exécutent |
| `s` à la place de `x` | 4000 / 2000 | SUID / SGID : s'exécute avec les droits du propriétaire / du groupe |
