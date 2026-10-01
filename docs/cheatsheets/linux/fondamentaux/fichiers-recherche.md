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
less <fichier>
```

```bash title="Exemple"
less /var/log/syslog   # / pour chercher, n pour suivant, q pour quitter
```

Pour comprendre : [Administration Linux, ch. 3](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/03-chapitre-3-lire-le-contenu-des-fichiers.md)
{ .kw-cs-meta }

### Lire le début ou la fin d'un fichier

```bash title="Commande"
head -n <N> <fichier>
tail -n <N> <fichier>
```

```bash title="Exemple"
tail -n 50 /var/log/auth.log
```

### Suivre un fichier qui grossit

```bash title="Commande"
tail -f <fichier>
```

```bash title="Exemple"
tail -f /var/log/nginx/access.log
```

```bash title="Exemple 2"
tail -F /var/log/syslog | grep --line-buffered -i error   # suit aussi après une rotation, filtre les erreurs
```

## Trouver des fichiers

### Trouver un fichier par son nom

```bash title="Commande"
find <dossier> -name "<motif>" 2>/dev/null
```

```bash title="Exemple"
find / -name "*.conf" 2>/dev/null
```

```bash title="Exemple 2"
find /etc -iname "*ssh*" -type f   # -iname : sans tenir compte des majuscules
```

Pour comprendre : [Linux — prises de notes, fichiers et flux](../../../library/it/linux/linux-prises-de-notes/03-fichiers-recherche-et-flux.md)
{ .kw-cs-meta }

### Trouver les fichiers modifiés récemment

```bash title="Commande"
find <dossier> -type f -mmin -<minutes> -ls 2>/dev/null
```

```bash title="Exemple"
find /var/www -type f -mmin -60 -ls 2>/dev/null   # modifiés dans la dernière heure
```

```bash title="Exemple 2"
find / -xdev -type f -newermt "2026-10-01 08:00" ! -newermt "2026-10-01 12:00" 2>/dev/null
# tous les fichiers modifiés entre 8 h et 12 h, sans descendre dans les autres disques
```

### Trouver les gros fichiers

```bash title="Commande"
find <dossier> -type f -size +<taille>
```

```bash title="Exemple"
find /var -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

```bash title="Exemple 2"
du -ah /var 2>/dev/null | sort -rh | head -20   # les 20 plus gros fichiers et dossiers
```

Ensuite : [trouver ce qui occupe la place](../administration/disques.md#trouver-ce-qui-occupe-la-place)
{ .kw-cs-meta }

### Trouver les fichiers d'un utilisateur

```bash title="Commande"
find <dossier> -user <utilisateur>
```

```bash title="Exemple"
find /home /tmp -user www-data -type f 2>/dev/null
```

### Combiner plusieurs critères et agir sur le résultat

```bash title="Commande"
find <dossier> <critères> -exec <commande> {} \;
```

```bash title="Exemple"
find / -type f -name "*.conf" -user root -size +20k -newermt 2020-03-03 -exec ls -al {} \; 2>/dev/null
```

Pour comprendre : [Linux — prises de notes, fichiers et flux](../../../library/it/linux/linux-prises-de-notes/03-fichiers-recherche-et-flux.md)
{ .kw-cs-meta }

### Trouver vite avec l'index locate

```bash title="Commande"
locate <motif>
```

```bash title="Exemple"
sudo updatedb && locate sshd_config
```

## Chercher dans le contenu

### Chercher un mot dans un fichier

```bash title="Commande"
grep -i "<motif>" <fichier>
```

```bash title="Exemple"
grep -i "error" /var/log/syslog
```

Ensuite : [afficher le contexte autour d'une correspondance](#afficher-le-contexte-autour-dune-correspondance) — Pour comprendre : [Administration Linux, ch. 4](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
{ .kw-cs-meta }

### Chercher un mot dans tout un dossier

```bash title="Commande"
grep -rni "<motif>" <dossier>
```

```bash title="Exemple"
grep -rni "password" /etc 2>/dev/null
```

```bash title="Exemple 2"
grep -rIl --include="*.php" "eval(" /var/www   # noms des fichiers PHP qui contiennent eval(
```

### Afficher le contexte autour d'une correspondance

```bash title="Commande"
grep -C <N> "<motif>" <fichier>
```

```bash title="Exemple"
grep -C 3 "Failed password" /var/log/auth.log   # 3 lignes avant et après
```

## Copier, comparer, vérifier

### Copier, déplacer ou supprimer

```bash title="Commande"
cp -a <source> <destination>
mv <source> <destination>
rm -i <fichier>
```

```bash title="Exemple"
cp -a /etc/nginx /tmp/nginx.bak   # copie en gardant droits et dates
```

!!! warning "Attention"
    `rm -rf` ne demande rien et ne passe pas par une corbeille.

Pour comprendre : [Administration Linux, ch. 5](../../../library/it/linux/administration-linux/02-partie-2-manipuler-le-systeme-de-fichiers/01-chapitre-5-creer-copier-deplacer-supprimer.md)
{ .kw-cs-meta }

### Créer un lien symbolique et le suivre

```bash title="Commande"
ln -s <cible> <lien>
readlink -f <lien>
```

```bash title="Exemple"
ln -s /opt/outil/bin/outil ~/bin/outil
```

Pour comprendre : [Administration Linux, ch. 7](../../../library/it/linux/administration-linux/02-partie-2-manipuler-le-systeme-de-fichiers/03-chapitre-7-liens-redirections-et-tuyaux.md)
{ .kw-cs-meta }

### Comparer deux fichiers

```bash title="Commande"
diff -u <fichier_a> <fichier_b>
```

```bash title="Exemple"
diff -u sshd_config.bak /etc/ssh/sshd_config
```

### Calculer l'empreinte d'un fichier

```bash title="Commande"
sha256sum <fichier>
```

```bash title="Exemple"
sha256sum /usr/bin/ssh
```

```bash title="Exemple 2"
sha256sum -c empreintes.txt   # vérifier une liste d'empreintes enregistrée plus tôt
```
