---
title: "grep"
commande: "grep"
---
# `grep`

Affiche les lignes qui contiennent un motif — dans un fichier, dans tout un dossier ou dans la sortie d'une autre commande.

```bash title="Syntaxe"
grep <options> "<motif>" <fichiers>   # ou : <commande> | grep "<motif>"
```

Pour comprendre : [Administration Linux, ch. 4](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
{ .kw-cs-meta }

## Les options utiles

| Option | Ce qu'elle fait |
|---|---|
| `-i` | Sans tenir compte des majuscules |
| `-r` · `-R` | Dans tout un dossier · en suivant aussi les liens symboliques |
| `-n` | Numéro de ligne |
| `-v` | Inverse : les lignes qui **ne** contiennent **pas** le motif |
| `-c` | Compte les lignes au lieu de les afficher |
| `-l` · `-L` | Seulement le nom des fichiers qui contiennent · qui ne contiennent pas |
| `-o` | Seulement la partie qui correspond, pas toute la ligne |
| `-E` · `-F` | Expression régulière étendue (`+`, `?`, `|`, `{n}`) · texte littéral, sans regex |
| `-w` | Mot entier (`root` ne trouve pas `chroot`) |
| `-A <N>` · `-B <N>` · `-C <N>` | N lignes après · avant · autour |
| `--include="*.php"` · `--exclude-dir=.git` | Seulement ces fichiers · sauf ce dossier (avec `-r`) |
| `-I` · `-h` · `-q` | Ignore les binaires · sans nom de fichier · silencieux (pour un test `if`) |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `grep -rni "password" /etc 2>/dev/null` | Dans tout `/etc`, sans casse, avec le numéro de ligne |
| `grep -vE '^\s*(#|$)' sshd_config` | Les lignes qui ne sont ni des commentaires ni vides : la configuration active |
| `grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' auth.log` | Seulement les adresses IPv4 trouvées dans le fichier |
| `grep -rIl --include="*.php" "eval(" /var/www` | Le nom des fichiers PHP qui contiennent `eval(`, binaires ignorés |
| `grep -C 2 -w "sshd" syslog` | Le mot `sshd`, avec 2 lignes de contexte avant et après |

## Pièges

- Les caractères `.` `*` `[` `$` ont un sens en regex : `-F` pour chercher du texte tel quel (`grep -F "1.2.3.4"`).
- Guillemets **simples** autour d'une regex : le shell n'interprète ni `$` ni `\`.
- `ps aux | grep nginx` affiche aussi la ligne du `grep` lui-même : `pgrep -a nginx`, ou `grep "[n]ginx"`.
- Derrière `tail -f`, ajouter `--line-buffered` pour que les lignes sortent tout de suite.
