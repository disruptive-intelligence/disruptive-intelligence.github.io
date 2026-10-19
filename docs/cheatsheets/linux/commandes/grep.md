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

## Exemples

??? example kw-cs-more "Dans un fichier"
    ```bash
    grep "root" /etc/passwd                     # lignes qui contiennent root
    grep -i "error" /var/log/syslog             # sans casse
    grep -w "admin" users.txt                   # le mot admin, pas administrator
    grep -n "Listen" /etc/apache2/ports.conf    # avec le numéro de ligne
    grep -c "Failed password" /var/log/auth.log # combien de lignes
    grep -v "^#" /etc/fstab                     # sans les commentaires
    grep -m 5 "error" /var/log/syslog           # s'arrêter aux 5 premières
    ```

??? example kw-cs-more "Dans tout un dossier"
    ```bash
    grep -rn "password" /var/www 2>/dev/null           # partout, avec fichier et ligne
    grep -rl "PermitRootLogin" /etc                    # seulement les noms de fichiers
    grep -rL "license" src/                            # les fichiers qui ne contiennent pas « license »
    grep -r --include="*.conf" "Listen" /etc           # seulement dans les .conf
    grep -r --exclude-dir={.git,node_modules} "TODO" . # sans .git ni node_modules
    grep -rIl "BEGIN RSA PRIVATE KEY" / 2>/dev/null    # clés privées oubliées, binaires ignorés
    ```

??? example kw-cs-more "Expressions régulières"
    ```bash
    grep -E "(root|admin)" /etc/passwd                  # root OU admin
    grep -E "root.*bash" /etc/passwd                    # root puis, plus loin, bash
    grep "^alice" /etc/passwd                           # lignes qui commencent par alice
    grep "bash$" /etc/passwd                            # lignes qui finissent par bash
    grep -E "^[^:]+:[^:]*:0:" /etc/passwd               # comptes d'UID 0 (root et ses copies)
    grep -oE "([0-9]{1,3}\.){3}[0-9]{1,3}" access.log | sort -u          # adresses IP distinctes
    grep -oE "[[:alnum:]._%+-]+@[[:alnum:].-]+\.[a-z]{2,}" fichier.txt   # adresses e-mail
    ```

??? example kw-cs-more "Avec d'autres commandes"
    ```bash
    ps aux | grep "[n]ginx"                         # processus nginx, sans la ligne du grep
    history | grep ssh                              # mes commandes ssh passées
    sudo ss -tulpn | grep ":443 "                   # qui écoute sur 443
    tail -f /var/log/syslog | grep --line-buffered -i "error"   # erreurs en direct
    zgrep "Failed password" /var/log/auth.log.*.gz  # dans les journaux compressés
    grep "Failed password" /var/log/auth.log | grep -oE "from [0-9.]+" | sort | uniq -c | sort -rn   # IP qui échouent le plus
    ```

??? example kw-cs-more "Avec du contexte"
    ```bash
    grep -A 3 "Exception" app.log                    # 3 lignes après
    grep -B 2 "segfault" /var/log/kern.log           # 2 lignes avant
    grep -C 5 "Accepted password" /var/log/auth.log  # 5 lignes autour
    ```

## Cas concrets

??? example kw-cs-cas "Pare-feu : filtrer des lignes, puis extraire un champ"
    Export `…|src=…|dstport=…|action=…|` : vérifier d'abord avec `head -n 3 firewall.log`.
    ```bash
    grep -F '|src=198.51.100.23|' firewall.log |      # lignes de cette source (adresse d'exemple)
      grep -F '|action=allow|' |                      # … autorisées
      grep -oE 'dstport=[0-9]+' | cut -d= -f2 | sort -n -u   # -o : seulement le champ dstport
    grep -F '|action=allow|' firewall.log |
      grep -oE 'dstport=[0-9]+' | cut -d= -f2 | sort -n -u | wc -l   # combien de ports différents
    ```
    `-F` : texte tel quel, `|` n'y est pas une alternative regex. Toutes les tentatives : retirer le filtre `action=allow`.

??? example kw-cs-cas "VPN : ne garder que les événements réussis ou échoués"
    ```bash
    grep -E '(^|[|])status=success([|]|$)' vpn.log
    grep -E '(^|[|])status=failure([|]|$)' vpn.log
    ```
    `(^|[|])` et `([|]|$)` : le champ exact, pas `status=successful`. Événements collés sur une ligne : [les séparer d'abord](sed.md#cas-concrets).

??? example kw-cs-cas "Gros journaux : contexte, rotations compressées, suivi en direct"
    ```bash
    grep -n -C 2 'Failed password' /var/log/auth.log | less -S          # n° de ligne et 2 lignes autour
    zgrep -h 'Failed password' /var/log/auth.log.*.gz | head             # dans les rotations .gz
    tail -F /var/log/auth.log | grep --line-buffered 'Failed password'  # nouvelles lignes, sans attendre le tampon
    ```

??? example kw-cs-cas "Zeek `http.log` : repérer un outil dans le User-Agent"
    ```bash
    grep -m1 '^#fields' http.log                                         # ordre des champs
    grep -v '^#' http.log | grep -iE 'nmap|nikto|sqlmap|gobuster|dirbuster'   # recherche rapide, toute la ligne
    zeek-cut id.orig_h method uri user_agent status_code < http.log |
      awk -F '\t' 'tolower($4) ~ /(nmap|nikto|sqlmap|gobuster|dirbuster)/ {print}'   # seulement dans user_agent
    ```
    La recherche rapide trouve aussi le mot dans l'URI. Un User-Agent peut être falsifié. Le cas complet : [Forensic › Zeek HTTP](../../forensic/reseau/journaux/web.md#zeek-bro-analyser-httplog)

Voir aussi : [Forensic › Pare-feu](../../forensic/reseau/journaux/pare-feu-vpn.md#lister-et-compter-les-ports-vises-dans-un-journal) · [Compter les valeurs distinctes d'un champ](../fondamentaux/texte-filtres.md#compter-les-valeurs-distinctes-dun-champ)
