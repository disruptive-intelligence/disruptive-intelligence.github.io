---
title: "Texte et filtres"
cours:
  - library/it/linux/administration-linux/index.md
---

# Texte et filtres

Découper, trier, compter et transformer la sortie d'une commande ou le contenu d'un fichier.

Les incontournables : `cut` · `sort | uniq -c` · `sed` · `grep -v` · `awk` · `| tee`
{ .kw-cs-top }

## Extraire

### Extraire une colonne

```bash title="Commande"
cut -d'<séparateur>' -f<N> <fichier>
```

```bash title="Exemple"
cut -d: -f1 /etc/passwd   # noms des comptes
```

```bash title="Exemple 2"
awk -F: '$3 >= 1000 {print $1, $6}' /etc/passwd   # comptes « humains » et leur dossier
```

Pour comprendre : [Administration Linux, ch. 4](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
{ .kw-cs-meta }

### Extraire avec une expression régulière

```bash title="Commande"
grep -oE '<regex>' <fichier>
```

```bash title="Exemple"
grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' /var/log/auth.log | sort -u   # toutes les IP citées
```

### Exclure des lignes (commentaires, lignes vides)

```bash title="Commande"
grep -v '<motif>' <fichier>
```

```bash title="Exemple"
grep -vE '^\s*(#|$)' /etc/ssh/sshd_config   # la configuration réellement active
```

## Compter et trier

### Trier et compter les occurrences

```bash title="Commande"
<commande> | sort | uniq -c | sort -rn
```

```bash title="Exemple"
cut -d' ' -f1 /var/log/nginx/access.log | sort | uniq -c | sort -rn | head   # IP les plus actives
```

### Compter des lignes

```bash title="Commande"
wc -l <fichier>
```

```bash title="Exemple"
grep -c "Failed password" /var/log/auth.log   # nombre de lignes qui correspondent
```

## Transformer

### Remplacer du texte

```bash title="Commande"
sed 's/<ancien>/<nouveau>/g' <fichier>
```

```bash title="Exemple"
sed 's/http:/https:/g' liens.txt   # affiche le résultat, ne modifie rien
```

```bash title="Exemple 2"
sudo sed -i.bak 's/^PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
# modifie le fichier sur place et garde une copie .bak
```

!!! warning "Attention"
    `sed -i` modifie le fichier : toujours `-i.bak` pour garder l'original.

### Changer un séparateur ou la casse

```bash title="Commande"
tr '<de>' '<vers>'
```

```bash title="Exemple"
tr ':' '\t' < /etc/passwd
```

```bash title="Exemple 2"
tr 'A-Z' 'a-z' < liste.txt
```

### Afficher en tableau aligné

```bash title="Commande"
column -t -s'<séparateur>'
```

```bash title="Exemple"
column -t -s: /etc/passwd | less -S
```

## Enchaîner et enregistrer

### Envoyer la sortie dans un fichier

```bash title="Commande"
<commande> > <fichier>    # écrase
<commande> >> <fichier>   # ajoute à la fin
```

```bash title="Exemple"
find / -perm -4000 2>/dev/null > suid.txt   # résultats dans le fichier, erreurs jetées
```

Pour comprendre : [Administration Linux, ch. 7](../../../library/it/linux/administration-linux/02-partie-2-manipuler-le-systeme-de-fichiers/03-chapitre-7-liens-redirections-et-tuyaux.md)
{ .kw-cs-meta }

### Voir la sortie et l'enregistrer en même temps

```bash title="Commande"
<commande> | tee <fichier>
```

```bash title="Exemple"
sudo ss -tunap | tee connexions.txt
```

```bash title="Exemple 2"
sudo ss -tunap | tee -a journal-intervention.txt   # -a : ajoute au fichier
```
