---
title: Synthèse finale
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
up:
- - Administration Linux
  - index.md
---

Cette section te sert de **référence rapide** une fois le cours terminé. Garde-la sous la main : ce sont les commandes et réflexes que tu utiliseras au quotidien.

## Cheat-sheets thématiques

### Navigation et repérage

| Besoin | Commande |
|--------|----------|
| Où suis-je ? | `pwd` |
| Lister (détaillé, cachés, lisible) | `ls -lah` |
| Se déplacer / revenir | `cd chemin` / `cd -` / `cd ~` |
| Voir l'arbre | `tree -L 2` |
| Remonter d'un niveau | `cd ..` |

### Fichiers et lecture

| Besoin | Commande |
|--------|----------|
| Type d'un fichier | `file fichier` |
| Lire (petit / gros) | `cat fichier` / `less fichier` |
| Début / fin | `head fichier` / `tail fichier` |
| Suivre en direct | `tail -f fichier` (sortie : `Ctrl+C`) |
| Compter les lignes | `wc -l fichier` |
| Créer / copier / déplacer | `touch` / `cp -r` / `mv` |
| Supprimer (prudence !) | `rm -i` / `rm -r` |
| Créer une arborescence | `mkdir -p a/b/c` |

### Recherche et texte

| Besoin | Commande |
|--------|----------|
| Chercher du texte | `grep -i "motif" fichier` |
| Compter / inverser / numéroter | `grep -c` / `grep -v` / `grep -n` |
| Trouver un fichier | `find /chemin -name "*.ext"` |
| Extraire une colonne | `cut -d: -f1` / `awk '{print $1}'` |
| Remplacer du texte | `sed 's/ancien/nouveau/g'` |
| Trier / dédoublonner + compter | `sort` / `sort \| uniq -c` |
| Casse | `tr 'A-Z' 'a-z'` |

### Flux et environnement

| Besoin | Commande |
|--------|----------|
| Enregistrer / ajouter | `cmd > fichier` / `cmd >> fichier` |
| Jeter les erreurs | `cmd 2>/dev/null` |
| Enchaîner | `cmd1 \| cmd2` |
| Voir ET enregistrer | `cmd \| tee fichier` |
| Voir une variable | `echo $PATH` |
| Toutes les variables | `env` |
| Localiser un programme | `which cmd` / `command -v cmd` |
| Variable / alias permanents | éditer `~/.bashrc` puis `source ~/.bashrc` |

### Permissions et identité

| Besoin | Commande |
|--------|----------|
| Voir les droits | `ls -l` |
| Modifier (symbolique / octal) | `chmod u+x` / `chmod 755` |
| Rendre un script exécutable | `chmod +x script.sh` |
| Changer propriétaire / groupe | `chown user:grp` / `chgrp grp` |
| Mon identité | `id` / `whoami` / `groups` |
| Créer un user / l'ajouter à un groupe | `adduser bob` / `usermod -aG sudo bob` |
| Admin ponctuel | `sudo cmd` |
| Mes droits sudo | `sudo -l` |
| Lister les SUID / capabilities | `find / -type f -perm -4000 2>/dev/null` / `getcap -r / 2>/dev/null` |

### Processus et services

| Besoin | Commande |
|--------|----------|
| Lister les processus | `ps aux` / `ps aux \| grep nom` |
| Temps réel | `top` / `htop` (sortie : `q`) |
| Arrêter (poli / forcé) | `kill PID` / `kill -9 PID` |
| Par nom | `killall nom` |
| État d'un service | `systemctl status nom` |
| Démarrer / arrêter / redémarrer | `sudo systemctl start\|stop\|restart nom` |
| Auto au démarrage | `sudo systemctl enable --now nom` |
| Lister les services | `systemctl list-units --type=service` |

### Logs et diagnostic

| Besoin | Commande |
|--------|----------|
| Journal d'un service | `journalctl -u nom` |
| Suivre en direct | `journalctl -f` |
| Depuis quand / filtré | `journalctl --since "today"` |
| Messages noyau/matériel | `sudo dmesg -T \| tail` |
| Charge / uptime | `uptime` |
| Mémoire | `free -h` |
| Logs d'auth (selon distro) | `/var/log/auth.log` · `/var/log/secure` · `journalctl` |

### Réseau et SSH

| Besoin | Commande |
|--------|----------|
| Mes adresses / routes | `ip a` / `ip r` |
| Tester la connectivité | `ping -c 4 cible` |
| Ports en écoute | `sudo ss -tulpn` |
| Résolution DNS | `dig nom` / `nslookup nom` |
| Tester un site | `curl -I url` |
| Connexion distante | `ssh user@machine` |
| Générer / copier une clé | `ssh-keygen -t ed25519` / `ssh-copy-id user@machine` |
| Copier / synchroniser | `scp` / `rsync -av --dry-run` |

### Paquets, disque, archives

| Besoin | Commande |
|--------|----------|
| Mettre à jour | `sudo apt update && sudo apt upgrade` |
| Installer / supprimer | `sudo apt install nom` / `sudo apt purge nom` |
| Chercher un paquet | `apt search motclé` |
| Espace disque global | `df -h` |
| Taille d'un dossier | `du -sh dossier` |
| Plus gros dossiers | `du -h --max-depth=1 / \| sort -rh \| head` |
| Disques / montages (observer) | `lsblk` / `findmnt` |
| Archiver / extraire | `tar -czvf a.tar.gz dossier/` / `tar -xzvf a.tar.gz` |
| Lire un log compressé | `zcat fichier.gz` / `zgrep "motif" fichier.gz` |

## Récapitulatif des erreurs classiques

| Domaine | Le piège | Le bon réflexe |
|---------|----------|----------------|
| Suppression | `rm` est définitif, pas de corbeille | `pwd` → `ls` → `rm -i` ; relire `rm -rf` |
| Espace parasite | `rm -rf / chemin` détruit la racine | relire la ligne avant Entrée |
| Permissions | `chmod 777` = faille ouverte | donner le minimum (`644`, `755`, `600`) |
| Dossiers | `r` ne suffit pas pour entrer | il faut le `x` pour traverser |
| Groupes | `usermod -G` écrase les groupes | toujours `usermod -aG` |
| sudo | shell root permanent (`sudo -i`) | `sudo cmd` ponctuel |
| Services | `start` ≠ persistant | `enable --now` pour le démarrage auto |
| Redirection | `>` écrase sans prévenir | `>>` pour ajouter ; vérifier la cible |
| Recherche | confondre `find` (fichiers) et `grep` (texte) | `find` = noms, `grep` = contenu |
| Réseau | `netstat`/`ifconfig` absents | `ss` / `ip` (modernes) |
| Paquets | `upgrade` sans `update` | `update && upgrade` |
| Disque | confondre `df` (disque) et `du` (dossier) | `df` constate, `du` trouve le coupable |
| Montage | `mount`/`umount`/`fstab` sensibles | observer d'abord (`lsblk`, `findmnt`) |
| Archives | `f` mal placé dans `tar` | `f` toujours juste avant le nom |
| SSH | se verrouiller dehors | garder une session de secours, tester la clé d'abord |
| Pare-feu | `ufw enable` coupe SSH | `ufw allow 22/tcp` avant d'activer |
| cron | chemins relatifs, `%` non échappé | chemins absolus, `\%` |
| Variables | `echo PATH` au lieu de `$PATH` | `$` pour lire ; écraser le `PATH` casse tout |

## Arbre de décision — « Quelle commande pour quel besoin ? »

```
Je veux...
├─ me repérer / naviguer ........... pwd, ls, cd, tree
├─ lire un fichier
│   ├─ petit ....................... cat
│   ├─ gros ........................ less
│   └─ suivre en direct ........... tail -f / journalctl -f
├─ chercher
│   ├─ du texte DANS des fichiers .. grep
│   └─ des fichiers (par nom) ...... find
├─ modifier des fichiers .......... touch, cp, mv, rm, nano/sudoedit
├─ comprendre les droits .......... ls -l, chmod, chown, id
├─ faire une action admin ......... sudo
├─ voir ce qui tourne ............. ps aux, top/htop, systemctl
├─ comprendre un problème ......... journalctl, systemctl status, dmesg
├─ regarder le réseau ............. ip a, ss -tulpn, ping
├─ me connecter à distance ........ ssh
├─ transférer des fichiers ........ scp, rsync
├─ installer un logiciel .......... sudo apt install
├─ gérer l'espace disque .......... df -h, du -sh, lsblk, findmnt
├─ archiver / sauvegarder ......... tar, gzip, rsync
└─ automatiser .................... script Bash + cron
```


## Pour continuer

Tu as les fondations solides de l'administration Linux. Voici les prolongements naturels :

- **Scripting Bash approfondi** : conditions, boucles, fonctions, gestion d'arguments et de cas d'erreur. C'est le complément direct du chapitre 26, pour transformer tes commandes en véritables outils. *(Un cours de scripting Bash dédié prolonge idéalement cette formation.)*
- **Python pour l'automatisation défensive** : quand Bash atteint ses limites (parsing complexe, API, structures de données), Python prend le relais — particulièrement en analyse de logs, OSINT et traitement d'IOC.
- **Cybersécurité défensive / SOC** : approfondis l'analyse de logs, la détection d'intrusion, les SIEM. Les chapitres 4, 11, 12, 15 et le projet 3 en sont la porte d'entrée.
- **Pentest débutant / eJPT** : l'énumération système (chapitres 10-12), le réseau (chapitre 17) et SSH (chapitre 18) constituent exactement les bases attendues. Tu connais déjà le versant défensif de ce que cette certification aborde côté offensif.
- **La pratique, surtout** : monte un petit lab (quelques VM), casse-le, répare-le, automatise-le. C'est en administrant de vraies machines qu'on devient administrateur.

Bon parcours sous Linux.

---
---
