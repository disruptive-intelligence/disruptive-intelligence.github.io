---
title: "Triage à chaud"
cours:
  - library/cyber/forensic/investigation-numerique-forensic/index.md
  - library/cyber/detection/reponse-a-incident/index.md
besoin: "Faire le triage à chaud d'une machine Linux suspecte"
---
# Triage à chaud — Linux

Machine allumée et suspecte : relever ce qui est volatil (processus, connexions) avant ce qui l'est moins
(fichiers, journaux), sans rien détruire. Chaque commande enregistre aussi sa sortie dans le dossier de
collecte.

Les entrées marquées « Repris de » viennent des fiches Linux : elles ne sont écrites qu'à un seul endroit.

Les incontournables : `date -u` · `ps auxf` · `ls -l /proc/<PID>/exe` · `ss -tnp` · `last` · `find -newermt`
{ .kw-cs-top }

## Collecte de base, en un bloc

Tout le triage d'un coup, dans l'ordre de volatilité : à coller dans un shell root, depuis le dossier de
collecte ouvert sur un support externe. Chaque ligne écrit sa sortie dans un fichier numéroté. Le détail de
chaque commande est dans les pages de chaque étape.

!!! tip "Des binaires de confiance"
    Sur une machine compromise, `ps`, `ss` ou `ls` peuvent avoir été remplacés. Mieux vaut apporter les siens
    sur la clé de collecte et les utiliser en priorité :
    `export PATH=/mnt/usb/bin:/mnt/usb/sbin:$PATH` et `export LD_LIBRARY_PATH=/mnt/usb/lib:/mnt/usb/lib64`.

```bash title="Collecte de base"
sudo -s                                                           # tout le bloc en root
date -u                                         > 01-date.txt     # heure UTC (l'horloge peut dériver)
{ uname -a; cat /etc/os-release; uptime; }      > 02-systeme.txt  # noyau, distribution, durée de fonctionnement
{ w; last -Faiwx | head -50; }                  > 03-sessions.txt # qui est là, dernières connexions
ps auxf                                         > 04-processus.txt          # processus en arbre
ls -l /proc/*/exe 2>/dev/null | grep deleted    > 05-binaires-supprimes.txt # en mémoire, effacés du disque
ss -tunap                                       > 06-reseau.txt   # ports en écoute et connexions, avec processus
{ ip -br a; ip route; ip neigh; }               > 07-interfaces.txt
lsof -nP 2>/dev/null                            > 08-fichiers-ouverts.txt
lsmod                                           > 09-modules.txt  # modules noyau chargés
systemctl list-units --type=service --state=running --no-pager > 10-services.txt
systemctl list-timers --all --no-pager          > 11-timers.txt
grep -R . /etc/cron* /var/spool/cron 2>/dev/null > 12-cron.txt
{ getent passwd; awk -F: '$3 == 0' /etc/passwd; } > 13-comptes.txt  # comptes, et ceux d'UID 0
awk -F: '$2 !~ /^[!*]/ {print $1}' /etc/shadow  > 14-comptes-avec-mot-de-passe.txt
cat /root/.bash_history /home/*/.bash_history  > 15-historiques.txt 2>/dev/null
find / -xdev -type f -mmin -120 -ls 2>/dev/null > 16-fichiers-recents.txt   # modifiés dans les 2 h
{ df -h; mount; }                               > 17-montages.txt
sha256sum ./*                                   > empreintes-collecte.txt    # en dernier
```

!!! warning "Ce qui doit alerter en relisant la collecte"
    - **Processus** lancé depuis `/tmp`, `/var/tmp` ou `/dev/shm`, ou dont le binaire est marqué `(deleted)`.
    - **Processus root avec un très grand PID** : les services système démarrent tôt, avec de petits PID.
    - **Connexion sortante** vers une adresse inconnue ou un port inhabituel (`4444`, `1337`, `8443`…).
    - **Compte d'UID 0** autre que `root`, ou compte « de service » sans shell qui a pourtant un mot de passe.
    - **Tâche planifiée, service ou timer récent**, surtout s'il télécharge et exécute un script (`curl … | sh`).
    - **Module noyau** que la distribution n'explique pas (piste de rootkit).
    - **Historique vide ou effacé** (`history -c`, `.bash_history` lié à `/dev/null`).
    - **Fichiers récemment modifiés** dans `/etc`, `/usr/bin` ou `~/.ssh/authorized_keys`.

## Avant tout

### Ouvrir un dossier de collecte et noter l'heure

```bash title="Commande"
mkdir -p <dossier_collecte> && cd <dossier_collecte>   # dossier de collecte, sur un support externe
date -u | tee 00-debut.txt; hostname | tee -a 00-debut.txt; uptime | tee -a 00-debut.txt   # heure UTC, machine, durée de fonctionnement
```

```bash title="Exemple"
mkdir -p /mnt/usb/collecte-srv-web-01 && cd /mnt/usb/collecte-srv-web-01
date -u | tee 00-debut.txt; hostnamectl | tee -a 00-debut.txt; uptime | tee -a 00-debut.txt
```

??? example "Sortie"
    ```text
    Thu Oct  2 09:40:12 UTC 2026
     Static hostname: srv-web-01
    Operating System: Ubuntu 24.04.1 LTS
     09:40:12 up 3 days,  4:11,  2 users,  load average: 0.31, 0.27, 0.22
    ```

!!! warning "Attention"
    Écrire la collecte sur un support externe, pas sur le disque suspect : chaque fichier créé écrase des traces.

Pour comprendre : [Investigation numérique (forensic)](../../../../library/cyber/forensic/investigation-numerique-forensic/index.md)
{ .kw-cs-meta }

![[cheatsheets/linux/fondamentaux/systeme#Voir qui est connecté maintenant]]

## Le triage, étape par étape

Dans l'ordre de volatilité :

1. [Processus](processus.md) — ce qui tourne, arbre, binaires suspects à préserver.
2. [Réseau](reseau.md) — ports en écoute, connexions établies.
3. [Persistance](persistance.md) — cron, services, timers, scripts de connexion, clés SSH.
4. [Traces d'activité](traces.md) — connexions, échecs, sudo, historiques, fichiers modifiés.
5. [Clore la collecte](cloture.md) — empreintes et fin du journal d'intervention.
