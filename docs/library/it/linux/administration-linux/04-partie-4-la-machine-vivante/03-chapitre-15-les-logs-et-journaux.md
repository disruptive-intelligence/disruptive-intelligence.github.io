---
title: Chapitre 15 — Les logs et journaux
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 4 — La machine vivante
  - index.md
---

## Le minimum à savoir

### Pourquoi les logs sont la matière première de la sécurité

Un système Linux **raconte en permanence ce qu'il fait** : connexions, erreurs, démarrages de services, tentatives d'accès refusées… Ces enregistrements sont les **logs** (journaux). Pour un administrateur, ils répondent à « pourquoi ça ne marche pas ? ». Pour un analyste sécurité, ils répondent à « que s'est-il passé, qui, quand ? ». **Sans logs, pas d'investigation possible.** Savoir où ils sont et comment les lire est une compétence centrale, en admin comme en SOC.

### Deux mondes : fichiers texte et journal systemd

Il existe historiquement **deux façons** de stocker les logs, et tu rencontreras les deux :

1. **Les fichiers texte dans `/var/log`** : la méthode classique. Chaque service y écrit son journal, et on les lit avec les outils du chapitre 3-4 (`cat`, `less`, `tail`, `grep`).
2. **Le journal systemd** : centralisé, structuré, interrogeable avec une seule commande, `journalctl`. C'est la méthode moderne, présente sur tous les systèmes systemd.

### Explorer `/var/log`

```bash
ls -lt /var/log              # liste les journaux, les plus récents en premier
sudo less /var/log/syslog    # journal général du système (Debian/Ubuntu)
sudo tail -f /var/log/syslog # suivre le journal système en direct (chapitre 3)
```


Quelques fichiers courants : `syslog` (journal général), les logs d'authentification, et des dossiers propres à certains services.

### Où sont les logs d'authentification ? (rappel essentiel)

Comme annoncé au chapitre 4, l'emplacement du journal d'authentification **dépend de la distribution** :

- **Debian / Ubuntu** : `/var/log/auth.log`
- **RHEL / CentOS / Fedora** : `/var/log/secure`
- **Tout système systemd** : `journalctl` est la méthode **la plus fiable et universelle** (voir ci-dessous)

> Ne sois pas surpris si `/var/log/auth.log` n'existe pas chez toi : c'est que ta distribution range ses logs ailleurs, ou s'appuie entièrement sur le journal systemd. Dans le doute, `journalctl` fonctionne partout où systemd est présent.

## Très utile en pratique

### `journalctl` : le journal unifié

`journalctl` interroge le journal systemd. C'est l'outil le plus puissant de ce chapitre :

```bash
journalctl                       # tout le journal (long ; navigue comme less, quitte avec q)
journalctl -e                    # saute directement à la fin (événements récents)
journalctl -u ssh                # uniquement les messages du service ssh
journalctl -f                    # suit le journal EN DIRECT (comme tail -f)
journalctl --since "today"       # depuis aujourd'hui
journalctl --since "1 hour ago"  # depuis une heure
journalctl -p err                # uniquement les messages de niveau "erreur" et plus grave
```


Les options à retenir en priorité : **`-u`** (filtrer par service), **`-f`** (suivre en direct), **`--since`** (filtrer par date). Combinées, elles répondent à des questions précises :

```bash
journalctl -u ssh --since "today"     # toutes les activités SSH d'aujourd'hui
```


> **Très utile en sécurité (SOC) :** `journalctl -u ssh -f` permet de **suivre en direct les tentatives de connexion SSH**. Couplé au `grep` du chapitre 4, c'est la base de la détection d'une attaque par force brute : on isole les échecs d'authentification, on compte les IP sources, on identifie celles qui frappent le plus.

### `dmesg` : les messages du noyau

À côté des logs de services, il existe un journal particulier : celui du **noyau** (le kernel), accessible avec `dmesg`. Il enregistre tout ce qui touche au **matériel et au bas niveau** :

```bash
sudo dmesg               # messages du noyau
sudo dmesg | tail        # les plus récents
sudo dmesg -T            # avec des dates lisibles (-T = timestamps humains)
```


`dmesg` est l'outil de référence pour les problèmes **matériels** :

- erreurs de **disque** (secteurs défectueux, déconnexions)
- branchement/débranchement de **périphériques USB**
- problèmes de **pilotes (drivers)**
- messages d'erreur du **noyau** lui-même

> **Réflexe :** quand un disque se comporte mal, qu'une clé USB n'est pas reconnue, ou qu'un matériel pose problème, `dmesg -T | tail` est souvent le moyen le plus rapide de voir ce que le noyau a constaté. On le réutilisera dans la démarche de diagnostic du chapitre 24.

### La rotation des logs : `logrotate` (notion)

Les logs grandissent sans cesse. Pour qu'ils ne remplissent pas le disque, un mécanisme appelé **rotation** archive et compresse régulièrement les anciens journaux, et supprime les plus vieux. C'est géré automatiquement par **`logrotate`**. Pour débuter, retiens simplement que ça **existe** : c'est pourquoi tu verras des fichiers comme `auth.log.1`, `auth.log.2.gz` — ce sont d'anciens journaux archivés. Tu n'as rien à configurer maintenant.

## ❌ Erreur classique

```bash
# Lire un gros log avec cat
cat /var/log/syslog          # ❌ des milliers de lignes défilent
sudo less /var/log/syslog    # ✅ page par page
journalctl -u ssh -e         # ✅ ou cibler directement le service

# Oublier sudo pour les logs sensibles
cat /var/log/auth.log        # ❌ souvent "Permission denied"
sudo cat /var/log/auth.log   # ✅ les logs d'auth sont protégés

# Chercher auth.log là où il n'existe pas
cat /var/log/auth.log        # ❌ absent sur RHEL/Fedora
sudo cat /var/log/secure     # ✅ sur RHEL/CentOS/Fedora
journalctl -u sshd           # ✅ méthode universelle (systemd)

# Croire que dmesg ne sert qu'au démarrage
dmesg                        # ❌ besoin de sudo sur beaucoup de systèmes
sudo dmesg -T | tail         # ✅ utile à tout moment pour le matériel
```


## Exercices

**Guidé :** Affiche les événements système d'aujourd'hui avec `journalctl --since "today"` (navigue, puis quitte avec `q`). Ensuite, cible un service précis avec `journalctl -u ssh` (ou un autre service actif chez toi vu au chapitre 14). Que t'apprend son journal ?

**Autonome :** Utilise `sudo dmesg -T | tail -20` pour voir les 20 derniers messages du noyau. Repères-tu des mentions de matériel (disque, USB, réseau) ? Si tu peux brancher/débrancher une clé USB, relance la commande juste après : vois-tu apparaître l'événement ?

**Défi (orientation SOC) :** Reprends la logique de détection de force brute du chapitre 4, mais avec le journal moderne. Avec `journalctl`, isole les tentatives d'authentification SSH échouées (cherche « Failed » dans le journal de SSH), puis, à l'aide des pipes et de `awk`/`grep`/`sort`/`uniq -c` (chapitre 4), identifie les adresses IP qui reviennent le plus souvent. Tu obtiens la même analyse qu'avec `auth.log`, mais d'une façon qui fonctionne sur **n'importe quel** système systemd.

## ✅ Tu sais maintenant…

- Pourquoi les logs sont **la matière première** de l'administration et de la sécurité
- Les deux mondes : **fichiers texte dans `/var/log`** et **journal systemd**
- Explorer `/var/log` avec `ls -lt`, `less`, `tail -f`
- Que les logs d'auth sont dans `auth.log` (Debian/Ubuntu), `secure` (RHEL/Fedora) ou via `journalctl` (universel)
- Interroger le journal avec `journalctl` et ses options clés `-u`, `-f`, `--since`, `-p`
- Lire les messages **matériels et noyau** avec `dmesg` (et `dmesg -T`)
- Que la **rotation** (`logrotate`) archive automatiquement les vieux journaux

---
