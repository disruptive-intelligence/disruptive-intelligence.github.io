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
ps aux
```

```bash title="Exemple"
ps aux --sort=-%cpu | head -15   # les plus gourmands en processeur
```

```bash title="Exemple 2"
ps -eo pid,ppid,user,%cpu,%mem,etime,cmd --sort=-%mem | head   # colonnes choisies, triées par mémoire
```

Ensuite : [trouver un processus par son nom](#trouver-un-processus-par-son-nom) — Pour comprendre : [Administration Linux, ch. 13](../../../library/it/linux/administration-linux/04-partie-4-la-machine-vivante/01-chapitre-13-les-processus.md)
{ .kw-cs-meta }

### Trouver un processus par son nom

```bash title="Commande"
pgrep -a <nom>
```

```bash title="Exemple"
pgrep -a sshd   # PID et ligne de commande
```

```bash title="Exemple 2"
ps -C nginx -o pid,ppid,user,etime,cmd   # avec parent, utilisateur et ancienneté
```

Ensuite : [voir les processus enfants d'un PID](#voir-les-processus-enfants-dun-pid) · [tout savoir sur un PID](#tout-savoir-sur-un-pid)
{ .kw-cs-meta }

### Voir l'arbre des processus

```bash title="Commande"
pstree -p
ps auxf
```

```bash title="Exemple"
pstree -p -u | less   # PID et changements d'utilisateur
```

### Voir les processus enfants d'un PID

```bash title="Commande"
pstree -p <PID>
ps --ppid <PID> -o pid,user,cmd
```

```bash title="Exemple"
pstree -p 1234   # tout l'arbre sous le PID 1234
```

```bash title="Exemple 2"
ps --ppid 1234 -o pid,user,etime,cmd   # enfants directs seulement
```

Ensuite : [tout savoir sur un PID](#tout-savoir-sur-un-pid)
{ .kw-cs-meta }

### Trouver le parent d'un processus

```bash title="Commande"
ps -o ppid= -p <PID>
```

```bash title="Exemple"
ps -o pid,ppid,user,cmd -p "$(ps -o ppid= -p 1234)"   # affiche directement le parent
```

### Tout savoir sur un PID

```bash title="Commande"
ls -l /proc/<PID>/exe
tr '\0' ' ' < /proc/<PID>/cmdline; echo
ls -l /proc/<PID>/cwd
```

```bash title="Exemple"
ls -l /proc/1234/exe   # binaire réellement exécuté (même s'il a été supprimé)
```

```bash title="Exemple 2"
sudo cat /proc/1234/environ | tr '\0' '\n'   # variables d'environnement du processus
```

Ensuite : [voir les fichiers et connexions d'un PID](#voir-les-fichiers-et-connexions-dun-pid) — Pour comprendre : [Linux — prises de notes, investigation](../../../library/it/linux/linux-prises-de-notes/02-investigation-forensics.md)
{ .kw-cs-meta }

### Voir les fichiers et connexions d'un PID

```bash title="Commande"
sudo lsof -p <PID>
```

```bash title="Exemple"
sudo lsof -p 1234 | grep -E 'REG|IPv'   # fichiers et sockets
```

```bash title="Exemple 2"
sudo ss -tunp | grep "pid=1234,"   # connexions réseau de ce seul processus
```

Ensuite : [arrêter un processus (poliment, puis de force)](#arreter-un-processus-poliment-puis-de-force)
{ .kw-cs-meta }

### Suivre les processus en temps réel

```bash title="Commande"
top
```

```bash title="Exemple"
top -o %MEM   # trié par mémoire ; q pour quitter
```

```bash title="Exemple 2"
htop -u www-data   # seulement les processus de www-data (si htop est installé)
```

## Agir

### Arrêter un processus (poliment, puis de force)

```bash title="Commande"
kill <PID>
kill -9 <PID>
```

```bash title="Exemple"
kill 1234   # SIGTERM : le processus se ferme proprement
```

```bash title="Exemple 2"
kill -9 1234   # SIGKILL : seulement s'il résiste
```

!!! warning "Attention"
    En investigation, relever binaire et connexions avant de tuer : `kill -9` efface l'état en mémoire.

### Arrêter un processus par son nom

```bash title="Commande"
pkill -x <nom>
```

```bash title="Exemple"
pkill -TERM -x python3
```

### Passer une commande en arrière-plan et la reprendre

```bash title="Commande"
<commande> &
jobs
fg %<n>
bg %<n>
```

```bash title="Exemple"
sleep 300 &   # puis jobs, puis fg %1 ; Ctrl+Z suspend la commande au premier plan
```

### Lancer une commande qui survit à la déconnexion

```bash title="Commande"
nohup <commande> > <journal> 2>&1 &
```

```bash title="Exemple"
nohup ./sauvegarde.sh > sauvegarde.log 2>&1 &
```

## Services

### Voir l'état d'un service

```bash title="Commande"
systemctl status <service>
```

```bash title="Exemple"
systemctl status ssh
```

```bash title="Exemple 2"
systemctl is-active ssh; systemctl is-enabled ssh   # actif maintenant ? activé au démarrage ?
```

Ensuite : [lire le journal d'un service](logs.md#lire-le-journal-dun-service) — Pour comprendre : [Administration Linux, ch. 14](../../../library/it/linux/administration-linux/04-partie-4-la-machine-vivante/02-chapitre-14-les-services-avec-systemd.md)
{ .kw-cs-meta }

### Lister les services actifs ou en échec

```bash title="Commande"
systemctl list-units --type=service --state=running
```

```bash title="Exemple"
systemctl list-units --type=service --state=running --no-pager
```

```bash title="Exemple 2"
systemctl --failed
```

### Voir la définition d'un service

```bash title="Commande"
systemctl cat <service>
```

```bash title="Exemple"
systemctl cat ssh.service   # quel binaire, quel utilisateur, quelles options
```

Ensuite : [démarrer, arrêter ou redémarrer un service](../administration/services.md#demarrer-arreter-ou-redemarrer-un-service)
{ .kw-cs-meta }

## Repères : les signaux

| Signal | Numéro | Effet |
|---|---|---|
| `SIGTERM` | 15 | Demande d'arrêt propre (par défaut avec `kill`) |
| `SIGKILL` | 9 | Arrêt immédiat, ne peut pas être ignoré |
| `SIGHUP` | 1 | Souvent : relire la configuration |
| `SIGINT` | 2 | Interruption (`Ctrl+C`) |
| `SIGSTOP` / `SIGCONT` | 19 / 18 | Suspendre / reprendre |
