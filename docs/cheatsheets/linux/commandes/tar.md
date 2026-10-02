---
title: "tar"
commande: "tar"
---
# `tar`

Regroupe des fichiers dans une archive (souvent compressée), en liste le contenu ou l'extrait.

```bash title="Syntaxe"
tar -<action><compression>f <archive> <fichiers>   # f en dernier : il est suivi du nom de l'archive
```

Pour comprendre : [Administration Linux, ch. 22](../../../library/it/linux/administration-linux/06-partie-6-entretenir-le-systeme/03-chapitre-22-archives-et-compression.md)
{ .kw-cs-meta }

## Les options utiles

| Lettre | Ce qu'elle fait |
|---|---|
| `c` · `x` · `t` | **C**rée · e**x**trait · liste le contenu (**t**able) |
| `z` · `j` · `J` | Compression gzip (`.tar.gz`) · bzip2 (`.tar.bz2`) · xz (`.tar.xz`) |
| `a` | Choisit la compression d'après l'extension de l'archive |
| `f <archive>` | Nom de l'archive (toujours en dernier dans le groupe de lettres) |
| `v` | Affiche chaque fichier traité |
| `-C <dossier>` | Extrait dans ce dossier (au lieu du dossier courant) |
| `--exclude='<motif>'` | Laisse de côté ces fichiers |
| `p` | Conserve les droits à l'extraction (par défaut pour root) |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `tar -czf etc.tar.gz /etc` | **C**rée, compresse en g**z**ip, dans le **f**ichier `etc.tar.gz`, le dossier `/etc` |
| `tar -xzf etc.tar.gz -C /tmp/restau` | E**x**trait l'archive gzip dans `/tmp/restau` |
| `tar -tzf etc.tar.gz` | Liste le contenu sans rien extraire |
| `tar -czf site.tar.gz --exclude='*.log' /var/www/site` | Archive le site, sans ses journaux |
| `tar -xzf etc.tar.gz etc/hosts` | N'extrait que `etc/hosts` |

## Pièges

- `f` est suivi du nom de l'archive : `-czf archive.tar.gz`, jamais `-cfz archive.tar.gz`.
- tar retire le `/` initial des chemins : à l'extraction, `etc/hosts` arrive dans le dossier courant (ou `-C`), pas dans `/etc`.
- Archive d'origine inconnue : la **lister** (`-t`) avant de l'extraire, elle peut écraser des fichiers existants.
