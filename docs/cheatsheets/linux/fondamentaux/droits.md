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
ls -l <fichier>
stat -c '%A %U:%G %n' <fichier>
```

```bash title="Exemple"
ls -l /etc/shadow
```

Pour comprendre : [Administration Linux, ch. 9](../../../library/it/linux/administration-linux/03-partie-3-qui-a-le-droit-de-quoi/01-chapitre-9-comprendre-les-permissions.md)
{ .kw-cs-meta }

### Changer les droits d'un fichier

```bash title="Commande"
chmod <mode> <fichier>
```

```bash title="Exemple"
chmod +x deploie.sh   # rendre un script exécutable
```

```bash title="Exemple 2"
chmod 640 /etc/app/config.ini   # rw- r-- --- : propriétaire lit/écrit, groupe lit
```

### Changer le propriétaire d'un fichier

```bash title="Commande"
sudo chown <utilisateur>:<groupe> <fichier>
```

```bash title="Exemple"
sudo chown -R www-data:www-data /var/www/site   # -R : tout le dossier
```

Pour comprendre : [Administration Linux, ch. 10](../../../library/it/linux/administration-linux/03-partie-3-qui-a-le-droit-de-quoi/02-chapitre-10-propriete-utilisateurs-et-groupes.md)
{ .kw-cs-meta }

### Voir les droits fins (ACL)

```bash title="Commande"
getfacl <fichier>
```

```bash title="Exemple"
getfacl /srv/partage
```

```bash title="Exemple 2"
sudo setfacl -m u:alice:rx /srv/partage   # donner lecture à alice
```

Pour comprendre : [Administration Linux, ch. 12](../../../library/it/linux/administration-linux/03-partie-3-qui-a-le-droit-de-quoi/04-chapitre-12-permissions-avancees-panorama.md)
{ .kw-cs-meta }

## Identités

### Savoir qui je suis et ce que sudo m'autorise

```bash title="Commande"
id
sudo -l
```

```bash title="Exemple"
id   # UID, groupe principal, groupes
```

```bash title="Exemple 2"
sudo -l   # commandes autorisées avec sudo
```

Pour comprendre : [Administration Linux, ch. 11](../../../library/it/linux/administration-linux/03-partie-3-qui-a-le-droit-de-quoi/03-chapitre-11-sudo-et-l-elevation-de-privileges.md)
{ .kw-cs-meta }

### Lister les comptes du système

```bash title="Commande"
getent passwd
```

```bash title="Exemple"
getent passwd | awk -F: '$3 >= 1000 {print $1}'   # comptes « humains »
```

```bash title="Exemple 2"
awk -F: '$7 !~ /(nologin|false)$/ {print $1, $7}' /etc/passwd   # comptes qui ont un shell
```

### Lister les membres d'un groupe

```bash title="Commande"
getent group <groupe>
```

```bash title="Exemple"
getent group sudo
```

## Droits à surveiller

### Trouver les fichiers SUID ou SGID

```bash title="Commande"
find / -perm -4000 -type f 2>/dev/null
```

```bash title="Exemple"
find / -perm -4000 -type f -exec ls -l {} \; 2>/dev/null
```

```bash title="Exemple 2"
find / -perm -2000 -type f 2>/dev/null   # SGID
```

Pour comprendre : [Administration Linux, ch. 12](../../../library/it/linux/administration-linux/03-partie-3-qui-a-le-droit-de-quoi/04-chapitre-12-permissions-avancees-panorama.md)
{ .kw-cs-meta }

### Trouver les fichiers modifiables par tous

```bash title="Commande"
find <dossier> -xdev -type f -perm -o+w 2>/dev/null
```

```bash title="Exemple"
find /etc /usr -xdev -type f -perm -o+w 2>/dev/null
```

### Voir les capabilities des binaires

```bash title="Commande"
getcap -r / 2>/dev/null
```

```bash title="Exemple"
getcap -r /usr 2>/dev/null
```

## Repères : lire `rwx`

| Notation | Octal | Sens |
|---|---|---|
| `r--` | 4 | lecture |
| `-w-` | 2 | écriture |
| `--x` | 1 | exécution (ou traverser un dossier) |
| `rw-r-----` | 640 | propriétaire lit/écrit, groupe lit, les autres rien |
| `rwxr-xr-x` | 755 | propriétaire tout, les autres lisent et exécutent |
| `s` à la place de `x` | 4000 / 2000 | SUID / SGID : s'exécute avec les droits du propriétaire / du groupe |
