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
mkdir -p <dossier_collecte> && cd <dossier_collecte>
date -u | tee 00-debut.txt; hostname | tee -a 00-debut.txt; uptime | tee -a 00-debut.txt
```

```bash title="Exemple"
mkdir -p /mnt/usb/collecte-srv-web-01 && cd /mnt/usb/collecte-srv-web-01
date -u | tee 00-debut.txt; hostnamectl | tee -a 00-debut.txt; uptime | tee -a 00-debut.txt
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
sudo cp /proc/<PID>/exe ./preuve_<PID>.bin
sha256sum ./preuve_<PID>.bin | tee -a empreintes.txt
```

```bash title="Exemple"
sudo cp /proc/1234/exe ./preuve_1234.bin && sha256sum ./preuve_1234.bin | tee -a empreintes.txt
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
sudo ls -la /etc/cron.* /var/spool/cron/crontabs 2>/dev/null
systemctl list-unit-files --state=enabled
ls -la /etc/profile.d ~/.bashrc ~/.profile ~/.ssh/authorized_keys
```

```bash title="Exemple"
sudo grep -R . /etc/cron* /var/spool/cron 2>/dev/null | tee persistance-cron.txt
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
sudo cat /home/<utilisateur>/.bash_history
```

```bash title="Exemple"
sudo tail -n 50 /root/.bash_history
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
sha256sum <dossier_collecte>/* > <dossier_collecte>/empreintes-collecte.txt
```

```bash title="Exemple"
date -u | tee -a 00-debut.txt && sha256sum ./* > empreintes-collecte.txt
```

Pour comprendre : [Réponse à incident](../../../library/cyber/detection/reponse-a-incident/index.md)
{ .kw-cs-meta }
