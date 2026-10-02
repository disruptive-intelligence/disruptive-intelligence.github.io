---
title: "Fichiers et recherche"
cours:
  - library/it/linux/administration-linux/index.md
---

# Fichiers et recherche

Lire, trouver et comparer des fichiers ; chercher un mot dans un fichier ou tout un dossier.

Les incontournables : `less` · `tail -f` · `find / -name` · `grep -rni` · `sha256sum`
{ .kw-cs-top }

## Lire

### Lire un fichier long

```bash title="Commande"
less <fichier>   # / chercher, n suivant, G fin du fichier, q quitter
```

```bash title="Exemple"
less /var/log/syslog
```

Pour comprendre : [Administration Linux, ch. 3](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/03-chapitre-3-lire-le-contenu-des-fichiers.md)
{ .kw-cs-meta }

### Lire le début ou la fin d'un fichier

```bash title="Commande"
head -n <N> <fichier>   # les N premières lignes
tail -n <N> <fichier>   # les N dernières lignes
```

```bash title="Exemple"
tail -n 3 /var/log/auth.log
```

??? example "Sortie"
    ```text
    Oct  2 09:12:01 srv-web-01 sshd[5123]: Accepted publickey for alice from 192.168.1.23 port 51544 ssh2
    Oct  2 09:12:01 srv-web-01 sshd[5123]: pam_unix(sshd:session): session opened for user alice(uid=1000)
    Oct  2 09:14:37 srv-web-01 sudo:    alice : TTY=pts/0 ; PWD=/home/alice ; USER=root ; COMMAND=/usr/bin/systemctl restart nginx
    ```

### Suivre un fichier qui grossit

```bash title="Commande"
tail -f <fichier>   # -F : continue aussi après une rotation du fichier
```

```bash title="Exemple"
tail -f /var/log/nginx/access.log
```

??? example "Sortie"
    ```text
    192.168.1.23 - - [02/Oct/2026:09:20:11 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/8.5.0"
    203.0.113.7 - - [02/Oct/2026:09:20:14 +0000] "GET /wp-login.php HTTP/1.1" 404 162 "-" "Mozilla/5.0"
    ```

```bash title="Exemple 2"
tail -F /var/log/syslog | grep --line-buffered -i error   # seulement les erreurs, en direct
```

## Trouver des fichiers

### Trouver un fichier par son nom

```bash title="Commande"
find <dossier> -name "<motif>" 2>/dev/null   # 2>/dev/null masque les « Permission denied »
```

```bash title="Exemple"
find /etc -name "*.conf" 2>/dev/null | head -4
```

??? example "Sortie"
    ```text
    /etc/adduser.conf
    /etc/ca-certificates.conf
    /etc/debconf.conf
    /etc/deluser.conf
    ```

```bash title="Exemple 2"
find /etc -iname "*ssh*" -type f   # -iname : sans tenir compte des majuscules
```

Pour comprendre : [Linux — prises de notes, fichiers et flux](../../../library/it/linux/linux-prises-de-notes/03-fichiers-recherche-et-flux.md)
{ .kw-cs-meta }

### Trouver les fichiers modifiés récemment

```bash title="Commande"
find <dossier> -type f -mmin -<minutes> -ls 2>/dev/null   # -mtime -<jours> pour des jours
```

```bash title="Exemple"
find /var/www -type f -mmin -60 -ls 2>/dev/null
```

??? example "Sortie"
    ```text
       524301      4 -rw-r--r--   1 www-data www-data     2741 Oct  2 09:02 /var/www/site/index.php
       524377      8 -rw-r--r--   1 www-data www-data     5120 Oct  2 09:05 /var/www/site/uploads/img.php
    ```

```bash title="Exemple 2"
find / -xdev -type f -newermt "2026-10-01 08:00" ! -newermt "2026-10-01 12:00" 2>/dev/null
# tous les fichiers modifiés entre 8 h et 12 h, sans descendre dans les autres disques
```

### Trouver les gros fichiers

```bash title="Commande"
find <dossier> -type f -size +<taille>   # +100M : plus de 100 Mo
```

```bash title="Exemple"
find /var -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

??? example "Sortie"
    ```text
    -rw-r----- 1 syslog adm 412M Oct  2 09:30 /var/log/syslog
    -rw-r--r-- 1 root   root 1.1G Sep 30 23:59 /var/backups/base.sql
    ```

```bash title="Exemple 2"
du -ah /var 2>/dev/null | sort -rh | head -20   # les 20 plus gros fichiers et dossiers
```

Ensuite : [trouver ce qui occupe la place](../administration/disques.md#trouver-ce-qui-occupe-la-place)
{ .kw-cs-meta }

### Trouver les fichiers d'un utilisateur

```bash title="Commande"
find <dossier> -user <utilisateur>   # -group <groupe> pour un groupe
```

```bash title="Exemple"
find /home /tmp -user www-data -type f 2>/dev/null
```

??? example "Sortie"
    ```text
    /tmp/.sess_9f3a
    /tmp/upload_4471.tmp
    ```

### Combiner plusieurs critères et agir sur le résultat

```bash title="Commande"
find <dossier> <critères> -exec <commande> {} \;   # {} : le fichier trouvé
```

```bash title="Exemple"
find / -type f -name "*.conf" -user root -size +20k -newermt 2020-03-03 -exec ls -al {} \; 2>/dev/null
```

??? example "Sortie"
    ```text
    -rw-r--r-- 1 root root 26612 Jun  4 11:20 /etc/ssh/sshd_config.d/hardening.conf
    ```

Pour comprendre : [Linux — prises de notes, fichiers et flux](../../../library/it/linux/linux-prises-de-notes/03-fichiers-recherche-et-flux.md)
{ .kw-cs-meta }

### Trouver vite avec l'index locate

```bash title="Commande"
locate <motif>   # sudo updatedb : remettre l'index à jour
```

```bash title="Exemple"
locate sshd_config
```

??? example "Sortie"
    ```text
    /etc/ssh/sshd_config
    /usr/share/openssh/sshd_config
    ```

## Chercher dans le contenu

### Chercher un mot dans un fichier

```bash title="Commande"
grep -i "<motif>" <fichier>   # -i : sans tenir compte des majuscules
```

```bash title="Exemple"
grep -i "error" /var/log/nginx/error.log
```

??? example "Sortie"
    ```text
    2026/10/02 09:05:33 [error] 1235#1235: *42 open() "/var/www/site/wp-login.php" failed (2: No such file or directory)
    ```

Ensuite : [afficher le contexte autour d'une correspondance](#afficher-le-contexte-autour-dune-correspondance) — Pour comprendre : [Administration Linux, ch. 4](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
{ .kw-cs-meta }

### Chercher un mot dans tout un dossier

```bash title="Commande"
grep -rni "<motif>" <dossier>   # r récursif, n numéro de ligne, i sans casse
```

```bash title="Exemple"
grep -rni "PermitRootLogin" /etc/ssh
```

??? example "Sortie"
    ```text
    /etc/ssh/sshd_config:33:#PermitRootLogin prohibit-password
    /etc/ssh/sshd_config.d/hardening.conf:2:PermitRootLogin no
    ```

```bash title="Exemple 2"
grep -rIl --include="*.php" "eval(" /var/www   # seulement les noms des fichiers PHP qui contiennent eval(
```

### Afficher le contexte autour d'une correspondance

```bash title="Commande"
grep -C <N> "<motif>" <fichier>   # -B avant seulement, -A après seulement
```

```bash title="Exemple"
grep -C 1 "Failed password" /var/log/auth.log
```

??? example "Sortie"
    ```text
    Oct  2 03:11:04 srv-web-01 sshd[7781]: Invalid user admin from 203.0.113.7 port 40122
    Oct  2 03:11:06 srv-web-01 sshd[7781]: Failed password for invalid user admin from 203.0.113.7 port 40122 ssh2
    Oct  2 03:11:08 srv-web-01 sshd[7781]: Connection closed by invalid user admin 203.0.113.7 port 40122
    ```

## Copier, comparer, vérifier

### Copier, déplacer ou supprimer

```bash title="Commande"
cp -a <source> <destination>   # copie, dossiers compris, droits et dates gardés
mv <source> <destination>      # déplace ou renomme
rm -i <fichier>                # supprime en demandant confirmation
```

```bash title="Exemple"
cp -a /etc/nginx /tmp/nginx.bak
```

!!! warning "Attention"
    `rm -rf` ne demande rien et ne passe pas par une corbeille.

Pour comprendre : [Administration Linux, ch. 5](../../../library/it/linux/administration-linux/02-partie-2-manipuler-le-systeme-de-fichiers/01-chapitre-5-creer-copier-deplacer-supprimer.md)
{ .kw-cs-meta }

### Créer un lien symbolique et le suivre

```bash title="Commande"
ln -s <cible> <lien>   # crée le raccourci
readlink -f <lien>     # cible réelle, liens suivis jusqu'au bout
```

```bash title="Exemple"
ln -s /opt/outil/bin/outil ~/bin/outil && readlink -f ~/bin/outil
```

??? example "Sortie"
    ```text
    /opt/outil/bin/outil
    ```

Pour comprendre : [Administration Linux, ch. 7](../../../library/it/linux/administration-linux/02-partie-2-manipuler-le-systeme-de-fichiers/03-chapitre-7-liens-redirections-et-tuyaux.md)
{ .kw-cs-meta }

### Comparer deux fichiers

```bash title="Commande"
diff -u <fichier_a> <fichier_b>   # -u : format unifié, lisible
```

```bash title="Exemple"
diff -u sshd_config.bak /etc/ssh/sshd_config
```

??? example "Sortie"
    ```text
    --- sshd_config.bak
    +++ /etc/ssh/sshd_config
    @@ -33 +33 @@
    -#PermitRootLogin prohibit-password
    +PermitRootLogin no
    ```

### Calculer l'empreinte d'un fichier

```bash title="Commande"
sha256sum <fichier>   # md5sum, sha1sum : empreintes plus faibles
```

```bash title="Exemple"
sha256sum /usr/bin/ssh
```

??? example "Sortie"
    ```text
    8c1f2a7e0d5b9c3e4f6a1b2c3d4e5f60718293a4b5c6d7e8f9a0b1c2d3e4f5a6  /usr/bin/ssh
    ```

```bash title="Exemple 2"
sha256sum -c empreintes.txt   # vérifier une liste d'empreintes enregistrée plus tôt
```
