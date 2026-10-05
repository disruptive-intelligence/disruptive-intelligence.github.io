---
title: "Processus et services"
cours:
  - library/it/linux/administration-linux/index.md
  - library/it/linux/linux-prises-de-notes/index.md
---

# Processus et services

Repérer un processus, remonter à son parent, voir ses enfants, ses fichiers et ses connexions, l'arrêter ; observer les services.

Les incontournables : `ps aux` · `pgrep -a` · `pstree -p` · `lsof -p` · `kill` · `systemctl status`
{ .kw-cs-top }

## Observer

### Lister tous les processus

```bash title="Commande"
ps aux   # tous les processus, de tous les utilisateurs
```

```bash title="Exemple"
ps aux --sort=-%cpu | head -4
```

??? example "Sortie"
    ```text
    USER       PID %CPU %MEM    VSZ   RSS TTY  STAT START   TIME COMMAND
    www-data  1236 12.4  1.9 215032 39812 ?    S    09:01   2:31 nginx: worker process
    mysql      901  3.1 11.2 2412340 230112 ?  Ssl  Sep29  41:07 /usr/sbin/mysqld
    alice     5180  0.3  0.2  10124  5236 pts/0 Ss  09:12   0:00 -bash
    ```

```bash title="Exemple 2"
ps -eo pid,ppid,user,%cpu,%mem,etime,cmd --sort=-%mem | head   # colonnes choisies, triées par mémoire
```

Ensuite : [trouver un processus par son nom](#trouver-un-processus-par-son-nom) — Pour comprendre : [Administration Linux, ch. 13](../../../library/it/linux/administration-linux/04-partie-4-la-machine-vivante/01-chapitre-13-les-processus.md)
{ .kw-cs-meta }

### Trouver un processus par son nom

```bash title="Commande"
pgrep -a <nom>   # -a : affiche aussi la ligne de commande
```

```bash title="Exemple"
pgrep -a nginx
```

??? example "Sortie"
    ```text
    1234 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
    1235 nginx: worker process
    1236 nginx: worker process
    ```

```bash title="Exemple 2"
ps -C nginx -o pid,ppid,user,etime,cmd   # avec parent, utilisateur et ancienneté
```

Ensuite : [voir les processus enfants d'un PID](#voir-les-processus-enfants-dun-pid) · [tout savoir sur un PID](#tout-savoir-sur-un-pid)
{ .kw-cs-meta }

### Voir l'arbre des processus

```bash title="Commande"
pstree -p   # -p : PID, -u : changements d'utilisateur
ps auxf     # même idée, avec les colonnes de ps
```

```bash title="Exemple"
pstree -p | head -6
```

??? example "Sortie"
    ```text
    systemd(1)─┬─cron(642)
               ├─mysqld(901)─┬─{mysqld}(912)
               │             └─{mysqld}(913)
               ├─nginx(1234)─┬─nginx(1235)
               │             └─nginx(1236)
               └─sshd(812)───sshd(5123)───bash(5180)
    ```

### Voir les processus enfants d'un PID

```bash title="Commande"
pstree -p <PID>                      # tout l'arbre sous ce PID
ps --ppid <PID> -o pid,user,cmd      # enfants directs seulement
```

```bash title="Exemple"
pstree -p 1234
```

??? example "Sortie"
    ```text
    nginx(1234)─┬─nginx(1235)
                └─nginx(1236)
    ```

```bash title="Exemple 2"
ps --ppid 1234 -o pid,user,etime,cmd
```

Ensuite : [tout savoir sur un PID](#tout-savoir-sur-un-pid)
{ .kw-cs-meta }

### Trouver le parent d'un processus

```bash title="Commande"
ps -o ppid= -p <PID>   # PID du parent
```

```bash title="Exemple"
ps -o pid,ppid,user,cmd -p "$(ps -o ppid= -p 5180)"
```

??? example "Sortie"
    ```text
        PID    PPID USER     CMD
       5123     812 root     sshd: alice [priv]
    ```

### Tout savoir sur un PID

```bash title="Commande"
ls -l /proc/<PID>/exe                     # binaire exécuté (même supprimé du disque)
tr '\0' ' ' < /proc/<PID>/cmdline; echo   # ligne de commande complète
ls -l /proc/<PID>/cwd                     # dossier de travail
```

```bash title="Exemple"
ls -l /proc/1234/exe
```

??? example "Sortie"
    ```text
    lrwxrwxrwx 1 root root 0 Oct  2 09:20 /proc/1234/exe -> /usr/sbin/nginx
    ```

```bash title="Exemple 2"
sudo cat /proc/1234/environ | tr '\0' '\n'   # variables d'environnement du processus
```

Ensuite : [voir les fichiers et connexions d'un PID](#voir-les-fichiers-et-connexions-dun-pid) — Pour comprendre : [Linux — prises de notes, investigation](../../../library/it/linux/linux-prises-de-notes/02-investigation-forensics.md)
{ .kw-cs-meta }

### Voir les fichiers et connexions d'un PID

```bash title="Commande"
sudo lsof -p <PID>   # tout ce que le processus a ouvert
```

```bash title="Exemple"
sudo lsof -p 1236 | grep -E 'REG|IPv'
```

??? example "Sortie"
    ```text
    nginx  1236 www-data  txt  REG    8,1  1271584  393402 /usr/sbin/nginx
    nginx  1236 www-data    5w REG    8,1  5532176  524313 /var/log/nginx/access.log
    nginx  1236 www-data    8u IPv4  41230      0t0     TCP *:http (LISTEN)
    ```

```bash title="Exemple 2"
sudo ss -tunp | grep "pid=1236,"   # connexions réseau de ce seul processus
```

Ensuite : [arrêter un processus (poliment, puis de force)](#arreter-un-processus-poliment-puis-de-force)
{ .kw-cs-meta }

### Suivre les processus en temps réel

```bash title="Commande"
top   # P trier par CPU, M par mémoire, k tuer un processus, q quitter
```

```bash title="Exemple"
top -o %MEM
```

```bash title="Exemple 2"
htop -u www-data   # seulement les processus de www-data (si htop est installé)
```

## Agir

### Arrêter un processus (poliment, puis de force)

```bash title="Commande"
kill <PID>      # SIGTERM : laisse le processus se fermer proprement
kill -9 <PID>   # SIGKILL : arrêt immédiat
```

```bash title="Exemple"
kill 1236
```

```bash title="Exemple 2"
kill -9 1236   # seulement s'il résiste
```

!!! warning "Attention"
    En investigation, relever binaire et connexions avant de tuer : `kill -9` efface l'état en mémoire.

### Arrêter un processus par son nom

```bash title="Commande"
pkill -x <nom>   # -x : nom exact (sinon « python » arrête aussi « python3 »)
```

```bash title="Exemple"
pkill -TERM -x python3
```

### Passer une commande en arrière-plan et la reprendre

```bash title="Commande"
<commande> &   # lance en arrière-plan
jobs           # liste les tâches du terminal
fg %<n>        # ramène la tâche n au premier plan (Ctrl+Z la suspend)
```

```bash title="Exemple"
sleep 300 &
```

??? example "Sortie"
    ```text
    [1] 4567
    ```

### Lancer une commande qui survit à la déconnexion

```bash title="Commande"
nohup <commande> > <journal> 2>&1 &   # sortie et erreurs dans le journal
```

```bash title="Exemple"
nohup ./sauvegarde.sh > sauvegarde.log 2>&1 &
```

??? example "Sortie"
    ```text
    [1] 4612
    ```

## Services

### Voir l'état d'un service

```bash title="Commande"
systemctl status <service>   # état, PID, mémoire, dernières lignes du journal
```

```bash title="Exemple"
systemctl status ssh --no-pager
```

??? example "Sortie"
    ```text
    ● ssh.service - OpenBSD Secure Shell server
         Loaded: loaded (/usr/lib/systemd/system/ssh.service; enabled; preset: enabled)
         Active: active (running) since Mon 2026-09-29 05:02:41 UTC; 3 days ago
       Main PID: 812 (sshd)
         Memory: 6.1M
    ```

```bash title="Exemple 2"
systemctl is-active ssh; systemctl is-enabled ssh   # actif maintenant ? activé au démarrage ?
```

Ensuite : [lire le journal d'un service](logs.md#lire-le-journal-dun-service) — Pour comprendre : [Administration Linux, ch. 14](../../../library/it/linux/administration-linux/04-partie-4-la-machine-vivante/02-chapitre-14-les-services-avec-systemd.md)
{ .kw-cs-meta }

### Lister les services actifs ou en échec

```bash title="Commande"
systemctl list-units --type=service --state=running   # services qui tournent
systemctl --failed                                    # services en échec
```

```bash title="Exemple"
systemctl --failed --no-pager
```

??? example "Sortie"
    ```text
      UNIT              LOAD   ACTIVE SUB    DESCRIPTION
    ● backup-db.service loaded failed failed Sauvegarde de la base

    1 loaded units listed.
    ```

### Voir la définition d'un service

```bash title="Commande"
systemctl cat <service>   # le fichier d'unité et ses surcharges
```

```bash title="Exemple"
systemctl cat ssh.service
```

??? example "Sortie"
    ```text
    # /usr/lib/systemd/system/ssh.service
    [Unit]
    Description=OpenBSD Secure Shell server

    [Service]
    ExecStart=/usr/sbin/sshd -D $SSHD_OPTS
    Restart=on-failure
    ```

Ensuite : [démarrer, arrêter ou redémarrer un service](../administration/services.md#demarrer-arreter-ou-redemarrer-un-service)
{ .kw-cs-meta }

## Vue d'ensemble : les signaux

| Signal | Numéro | Effet |
|---|---|---|
| `SIGTERM` | 15 | Demande d'arrêt propre (par défaut avec `kill`) |
| `SIGKILL` | 9 | Arrêt immédiat, ne peut pas être ignoré |
| `SIGHUP` | 1 | Souvent : relire la configuration |
| `SIGINT` | 2 | Interruption (`Ctrl+C`) |
| `SIGSTOP` / `SIGCONT` | 19 / 18 | Suspendre / reprendre |
