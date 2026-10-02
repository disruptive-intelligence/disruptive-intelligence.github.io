---
title: "ps"
commande: "ps"
---
# `ps`

Photographie les processus à un instant donné : qui tourne, sous quel utilisateur, lancé par qui, avec quelles ressources.

```bash title="Syntaxe"
ps aux   # syntaxe BSD, sans tiret
ps -ef   # syntaxe Unix, avec le PPID
```

Pour comprendre : [Administration Linux, ch. 13](../../../library/it/linux/administration-linux/04-partie-4-la-machine-vivante/01-chapitre-13-les-processus.md)
{ .kw-cs-meta }

## Les options utiles

| Option | Ce qu'elle fait |
|---|---|
| `a` · `u` · `x` | Tous les utilisateurs · format détaillé (utilisateur, %CPU, %MEM) · y compris sans terminal |
| `f` (`ps auxf`) | Dessine l'arbre parent → enfants |
| `-e` · `-f` | Tous les processus · format complet (avec le PPID) |
| `-o pid,ppid,user,etime,cmd` | Colonnes choisies (`etime` : depuis combien de temps il tourne) |
| `--sort=-%cpu` · `--sort=-%mem` | Trié par processeur · par mémoire, décroissant |
| `-p <PID>` · `--ppid <PID>` | Ce processus · ses enfants directs |
| `-C <nom>` · `-u <utilisateur>` | Par nom de programme · par utilisateur |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `ps aux --sort=-%cpu | head` | Tous les processus, les plus gourmands en processeur d'abord |
| `ps -eo pid,ppid,user,etime,cmd --sort=-%mem` | PID, parent, utilisateur, ancienneté et commande, triés par mémoire |
| `ps -o ppid= -p 5180` | Seulement le PID du parent de 5180 (`=` vide l'en-tête) |
| `ps -fu www-data` | Les processus de `www-data`, en format complet |

## Pièges

- Colonne **STAT** : `R` en cours, `S` endormi, `D` bloqué sur le disque, `Z` zombie, `T` stoppé ; `s` chef de session, `+` premier plan, `l` multi-thread.
- **VSZ** / **RSS** : mémoire réservée / réellement occupée, en Ko. Un nom `[entre crochets]` est un thread du noyau.
- `ps aux | grep x` se trouve lui-même : `pgrep -a x`. Et `ps` est une photo : `top` pour suivre.
