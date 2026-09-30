---
title: Chapitre 16 — Tâches planifiées
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 4 — La machine vivante
  - index.md
---

## Le minimum à savoir

### Pourquoi automatiser dans le temps

Beaucoup de tâches d'administration doivent se répéter : sauvegarder chaque nuit, nettoyer des fichiers temporaires chaque semaine, vérifier l'espace disque tous les matins. Plutôt que de les lancer à la main, on les **planifie** : le système les exécute tout seul, à l'heure dite, que tu sois là ou non. C'est l'un des grands intérêts d'un serveur, qui tourne en continu.

### cron : le planificateur classique

L'outil historique et universel est **cron**. Chaque utilisateur dispose de sa propre table de tâches planifiées, la **crontab**, qu'on édite ainsi :

```bash
crontab -e               # éditer SA table de tâches planifiées
crontab -l               # afficher SA table actuelle
```


La première fois, `crontab -e` te demande quel éditeur utiliser (choisis `nano` si tu hésites).

### Lire la syntaxe cron : cinq champs

Chaque ligne de la crontab décrit **quand** lancer **quoi**, avec cinq champs de temps suivis de la commande :

```
┌───────── minute (0-59)
│ ┌─────── heure (0-23)
│ │ ┌───── jour du mois (1-31)
│ │ │ ┌─── mois (1-12)
│ │ │ │ ┌─ jour de la semaine (0-7, dimanche = 0 ou 7)
│ │ │ │ │
* * * * *  commande-à-exécuter
```


Une `*` signifie « toutes les valeurs ». Quelques exemples parlants :

```bash
0 8 * * *    /chemin/script.sh      # tous les jours à 8h00
30 2 * * 0   /chemin/backup.sh      # chaque dimanche à 2h30
*/15 * * * * /chemin/check.sh       # toutes les 15 minutes
0 0 1 * *    /chemin/mensuel.sh     # le 1er de chaque mois à minuit
```


> **Le minimum à savoir :** les deux premiers champs (minute, heure) suffisent pour l'immense majorité des besoins : « tous les jours à telle heure ». Pour le reste, on met des `*`. En cas de doute sur une expression, des aides en ligne existent pour traduire une ligne cron en langage clair.

## Très utile en pratique

### Les dossiers cron du système

À côté de la crontab personnelle, le système propose des dossiers où **déposer un script** pour qu'il s'exécute à une fréquence donnée, sans même écrire de ligne cron :

```bash
ls /etc/cron.daily/      # scripts exécutés chaque jour
ls /etc/cron.weekly/     # chaque semaine
ls /etc/cron.hourly/     # chaque heure
```


Déposer un script exécutable (chapitre 9 : `chmod +x`) dans `/etc/cron.daily/` suffit à le faire tourner quotidiennement. Pratique et lisible.

### Une exécution unique : `at`

Là où cron **répète**, `at` exécute une commande **une seule fois**, à un moment futur :

```bash
echo "commande" | at 22:00       # lance la commande à 22h, une seule fois
at now + 1 hour                  # planifie pour dans une heure (mode interactif)
```


`at` n'est pas toujours installé ; au besoin, `sudo apt install at`.

### Les timers systemd (notion)

systemd propose une alternative moderne à cron : les **timers** (`.timer`). Ils sont plus puissants (meilleure journalisation via `journalctl`, gestion des tâches manquées…) mais plus verbeux à écrire. Pour débuter, retiens qu'ils **existent** et qu'on les rencontre de plus en plus ; cron reste parfaitement valable et plus simple pour commencer.

> **Orientation cyber / sécurité :** les tâches planifiées sont à double tranchant. Côté défense, elles automatisent la surveillance et les sauvegardes. Côté attaque, elles sont un **mécanisme de persistance** classique : un intrus ajoute une tâche cron pour relancer son code régulièrement. Lors d'un audit, **inspecter les crontabs** (`crontab -l`, les fichiers dans `/etc/cron.*` et `/var/spool/cron/`) fait partie des réflexes pour repérer une persistance suspecte.

## ❌ Erreur classique

```bash
# Éditer la crontab à la main au mauvais endroit
nano /var/spool/cron/...      # ❌ ne pas éditer directement les fichiers internes
crontab -e                    # ✅ toujours passer par crontab -e

# Utiliser un chemin relatif dans une tâche cron
0 8 * * * script.sh           # ❌ cron ne sait pas où il est ; PATH minimal
0 8 * * * /home/alice/script.sh   # ✅ TOUJOURS un chemin absolu

# Oublier de rendre le script exécutable
0 8 * * * /home/alice/backup.sh   # ❌ échoue si pas de droit x
chmod +x /home/alice/backup.sh    # ✅ (chapitre 9)

# Croire que la tâche tourne alors que la machine est éteinte
# cron a besoin que la machine soit ALLUMÉE à l'heure prévue
```


> **Le piège du chemin et de l'environnement :** une tâche cron s'exécute dans un environnement **minimal** (un `PATH` réduit, pas tes alias du chapitre 8). Une commande qui marche dans ton terminal peut échouer en cron si elle dépend de ton environnement. La parade : **utiliser des chemins absolus** partout dans tes scripts planifiés.

## Exercices

**Guidé :** Ouvre ta crontab avec `crontab -e` (choisis `nano` si on te le demande). Ajoute une ligne qui écrit la date dans un fichier toutes les minutes, à des fins de test : `* * * * * date >> /home/alice/cron-test.log` (**remplace `alice` par ton vrai nom d'utilisateur** — on met un chemin absolu, conformément à la règle ci-dessus). Enregistre, attends deux-trois minutes, puis lis `cron-test.log` : vois-tu plusieurs horodatages s'accumuler ? Retire ensuite la ligne avec `crontab -e` pour ne pas polluer.

**Autonome :** Écris en langage clair ce que feraient ces lignes cron, puis vérifie ton interprétation : `0 6 * * 1`, `*/10 * * * *`, `0 0 * * 0`. À quelle fréquence chacune s'exécute-t-elle ?

**Défi (orientation sécurité) :** Fais l'inventaire des tâches planifiées de ta machine. Affiche ta crontab (`crontab -l`), liste le contenu des dossiers `/etc/cron.daily/`, `/etc/cron.hourly/`, et regarde s'il existe des crontabs système (`cat /etc/crontab`). Sur une vraie investigation, pourquoi serait-il important de connaître **toutes** les tâches planifiées d'une machine ? Que chercherait un analyste là-dedans ?

## ✅ Tu sais maintenant…

- Pourquoi on **planifie** des tâches répétitives (sauvegardes, nettoyages, vérifications)
- Éditer et lire ta planification avec `crontab -e` et `crontab -l`
- Lire la **syntaxe cron** à cinq champs (minute, heure, jour, mois, jour de semaine)
- Déposer un script dans `/etc/cron.daily/` (et `.weekly`, `.hourly`)
- Planifier une exécution **unique** avec `at`, et que les **timers systemd** existent
- Le piège des **chemins relatifs** en cron (toujours des chemins absolus)
- Que les tâches planifiées sont un **mécanisme de persistance** à auditer en sécurité

---

> **🏁 CHECKPOINT 4 — Fin de la Partie 4**
>
> Tu sais désormais **piloter une machine en fonctionnement** : observer et contrôler les processus, gérer les services qui tournent en permanence, lire ce que le système raconte dans ses journaux, et automatiser des tâches dans le temps.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - retrouver le PID d'un programme et l'arrêter proprement (puis de force si besoin) ?
> - vérifier si un service tourne, le redémarrer, et le faire démarrer automatiquement au boot ?
> - expliquer la différence entre `systemctl start` et `systemctl enable` ?
> - suivre en direct les tentatives de connexion SSH avec `journalctl` ?
> - utiliser `dmesg` pour diagnostiquer un souci matériel ?
> - planifier un script pour qu'il tourne tous les jours à heure fixe ?
>
> Si oui, tu administres une machine vivante. Il est temps de l'**ouvrir sur le monde** : place à la **Partie 5 — Linux en réseau**.

---

---
---
