---
title: Chapitre 14 — Les services avec systemd
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 4 — La machine vivante
  - index.md
---

## Le minimum à savoir

### Qu'est-ce qu'un service (ou démon) ?

Certains programmes ne sont pas faits pour être lancés à la main puis fermés : ils doivent tourner **en permanence**, en arrière-plan, prêts à répondre à tout moment. C'est le cas d'un serveur web, d'une base de données, ou du **serveur SSH** qui attend les connexions distantes. Ces programmes de fond s'appellent des **services**, ou **démons** (*daemons*). Leur nom se termine souvent par un `d` : `sshd` (SSH daemon), `cron`, etc.

### systemd : le chef d'orchestre

Au démarrage de la machine, quelque chose doit lancer tous ces services dans le bon ordre, les surveiller, les redémarrer s'ils tombent. Sur la quasi-totalité des distributions modernes, ce rôle est tenu par **systemd**. C'est lui le fameux **PID 1** du chapitre précédent : le tout premier processus, ancêtre de tous les autres. systemd gère des unités appelées **units**, dont les plus courantes sont les services (`.service`).

### Piloter un service : `systemctl`

L'outil unique pour gérer les services est `systemctl`. Sa logique est simple et régulière :

```bash
systemctl status ssh         # quel est l'état du service SSH ? (actif ? en erreur ?)
sudo systemctl start ssh     # démarre le service
sudo systemctl stop ssh      # arrête le service
sudo systemctl restart ssh   # redémarre (stop puis start)
sudo systemctl reload ssh    # recharge la config sans interrompre le service
```


La commande la plus utile au quotidien est `status` : elle te dit si le service tourne, depuis quand, et affiche ses dernières lignes de journal — précieux pour comprendre un problème.

> **Le minimum à savoir :** `systemctl status nom-du-service` pour diagnostiquer, `start`/`stop`/`restart` pour agir. Les actions qui modifient l'état (start, stop, restart) demandent `sudo` ; consulter le `status` est souvent possible sans.

### Démarrage automatique : `enable` et `disable`

Démarrer un service avec `start` ne le relance **pas** au prochain redémarrage de la machine. Pour qu'un service se lance **automatiquement au boot**, il faut l'**activer** :

```bash
sudo systemctl enable ssh    # SSH démarrera automatiquement à chaque démarrage
sudo systemctl disable ssh   # SSH ne démarrera plus automatiquement
sudo systemctl enable --now ssh   # active ET démarre tout de suite
```


> **Distinction essentielle :** `start` agit **maintenant** (jusqu'au prochain reboot), `enable` agit **au démarrage** (de façon permanente). On les confond souvent. Un service qu'on veut voir tourner durablement doit être à la fois **démarré** et **activé** — d'où le pratique `enable --now`.

## Très utile en pratique

### Lister et explorer les services

```bash
systemctl list-units --type=service          # tous les services actuellement chargés
systemctl list-units --type=service --state=running   # uniquement ceux qui tournent
systemctl list-unit-files --type=service     # tous les services installés et leur statut
```


> **Très utile en sécurité :** lister les services actifs revient à dresser l'inventaire de ce qui **tourne** — donc de ce qui pourrait être attaqué. Un service inattendu, ou activé sans raison, mérite qu'on s'y intéresse. C'est aussi la base du durcissement (chapitre 25) : **désactiver les services inutiles réduit la surface d'attaque**.

### Lire le journal d'un service

Quand un service refuse de démarrer, son journal explique pourquoi. `systemctl status` en donne un aperçu, mais on accède au journal complet avec `journalctl` (le chapitre 15 lui est consacré) :

```bash
systemctl status nginx       # aperçu de l'état + dernières lignes de log
journalctl -u nginx          # le journal complet du service nginx
```


Ce duo `status` + `journalctl -u` est la base du diagnostic d'un service défaillant : on regarde l'état, puis on lit ce que le service a écrit avant de tomber.

## ❌ Erreur classique

```bash
# Confondre start et enable
sudo systemctl start ssh     # démarre maintenant... mais pas après reboot
sudo systemctl enable ssh    # ✅ pour qu'il revienne au démarrage
sudo systemctl enable --now ssh  # ✅ les deux d'un coup

# Oublier sudo pour les actions
systemctl restart ssh        # ❌ "Permission denied" / demande d'authentification
sudo systemctl restart ssh   # ✅

# Se tromper de nom de service
systemctl status sshd        # selon la distro, le service s'appelle "ssh" ou "sshd"
systemctl status ssh         # ✅ sur Debian/Ubuntu c'est souvent "ssh"

# Modifier une config de service et oublier de recharger
sudoedit /etc/ssh/sshd_config   # modification faite...
# ❌ ...mais le service tourne encore avec l'ancienne config
sudo systemctl restart ssh      # ✅ recharge la nouvelle config
```


## Exercices

**Guidé :** Affiche l'état du service SSH avec `systemctl status ssh` (ou `sshd` selon ta distribution). Est-il `active (running)` ? Est-il `enabled` (démarrage auto) ? Lis attentivement les dernières lignes affichées : que t'apprennent-elles sur le service ?

**Autonome :** Liste tous les services en cours d'exécution avec `systemctl list-units --type=service --state=running`. Combien y en a-t-il ? Parcours la liste : reconnais-tu le rôle de quelques-uns (réseau, journalisation, planification…) ?

**Défi (en lab) :** Sur une machine de test, choisis un service non critique, note son état avec `systemctl status`, arrête-le avec `sudo systemctl stop`, vérifie qu'il est bien `inactive`, puis redémarre-le et confirme qu'il est de nouveau `active`. **Ne fais jamais cela sur le service SSH d'une machine à laquelle tu es connecté à distance** — tu couperais ta propre connexion (on en reparlera au chapitre 17).

## ✅ Tu sais maintenant…

- Ce qu'est un **service / démon** : un programme qui tourne en permanence en arrière-plan
- Que **systemd** orchestre les services et qu'il est le **PID 1**
- Piloter un service avec `systemctl` : `status`, `start`, `stop`, `restart`, `reload`
- La différence cruciale entre `start` (maintenant) et `enable` (au démarrage), et le raccourci `enable --now`
- Lister les services actifs (`list-units`) et pourquoi c'est un enjeu de surface d'attaque
- Diagnostiquer un service défaillant avec `status` puis `journalctl -u`

---
