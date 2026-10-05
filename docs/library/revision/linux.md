---
title: Révision — Linux
revision: it/linux
domaine: IT
sources:
- IT/01 Linux/Linux — prises de notes.md
---

*D'après le cours [Linux — prises de notes](../it/linux/linux-prises-de-notes/index.md)*

## Questions essentielles

- **Question :** Décrivez la hiérarchie du système de fichiers Linux — les répertoires les plus importants.
    - **Réponse type :** Tout part de `/`, la racine. Les plus importants : `/etc` contient les fichiers de configuration système, `/var` les données variables comme les logs (`/var/log`), `/home` les dossiers personnels des utilisateurs, `/tmp` les fichiers temporaires, `/bin` et `/sbin` les binaires essentiels et d'administration. Pour un analyste sécurité, `/var/log` et `/etc` sont les répertoires critiques — c'est là qu'on trouve les traces d'activité et les configurations à auditer.

- **Question :** Quelle est la différence entre `su` et `sudo` ?
    - **Réponse type :** `su` change d'utilisateur — il demande le mot de passe de l'utilisateur cible. `sudo` exécute une commande avec les droits d'un autre utilisateur (souvent root), mais demande votre propre mot de passe. `sudo` est préférable en sécurité car il offre un contrôle granulaire via `/etc/sudoers`, une journalisation des actions, et n'oblige pas à partager le mot de passe root.

- **Question :** Quels fichiers de logs sont essentiels pour une investigation Linux ?
    - **Réponse type :** Les trois principaux : `/var/log/auth.log` pour toutes les authentifications (connexions SSH, sudo, création d'utilisateurs), `/var/log/syslog` pour les messages système généraux (services, cron, erreurs), et les logs applicatifs dans `/var/log/`. Pour les connexions, il y a aussi `wtmp` (historique des connexions réussies) et `btmp` (tentatives échouées), consultables avec la commande `last`.

- **Question :** Comment vérifier les mécanismes de persistence sur une machine Linux ?
    - **Réponse type :** Je regarderais les cron jobs (`/etc/crontab`, `crontab -l`), les services activés au démarrage (`systemctl list-unit-files --type=service`), les scripts d'initialisation dans `/etc/init.d/`, et les fichiers `.bashrc` de chaque utilisateur qui s'exécutent à l'ouverture d'un shell. Ce sont les endroits classiques où un attaquant peut placer de la persistence.

- **Question :** Expliquez le processus de démarrage Linux.
    - **Réponse type :** En quatre étapes : d'abord le firmware BIOS/UEFI fait le POST et trouve le disque de boot. Ensuite le bootloader (GRUB) charge le noyau en mémoire. Le kernel se décompresse, monte un système de fichiers temporaire, puis le vrai disque. Enfin, le premier processus (PID 1) est lancé — c'est systemd — qui démarre tous les services.

## Questions complémentaires

- **Question :** Quelles commandes utiliseriez-vous pour diagnostiquer un problème réseau sur Linux ?
    **Réponse type :** `ip a` pour voir les interfaces et adresses, `ip route show` pour la table de routage, `netstat -natp` ou `ss -natp` pour les connexions actives et les ports en écoute, `ping` pour tester la connectivité, et `tcpdump` pour capturer du trafic. En complément, `cat /etc/resolv.conf` pour vérifier le DNS configuré.

## Questions les plus probables en entretien

1. Hiérarchie du système de fichiers Linux ?
2. Différence `su` vs `sudo` ?
3. Logs essentiels pour une investigation ?
4. Où chercher la persistence sur Linux ?
5. Processus de démarrage Linux ?

## Réponses flash

- **Fichiers clés** → `/etc` (config), `/var/log` (logs), `/home` (users), `/tmp` (temporaire), `/bin` (binaires).
- **su vs sudo** → su = change d'user (mot de passe cible). sudo = exécute en tant que (votre mot de passe, journalisé, granulaire).
- **Logs investigation** → `auth.log` (auth), `syslog` (système), `wtmp`/`btmp` (connexions), `.bash_history` (commandes).
- **Persistence** → crontab, services systemd, /etc/init.d, .bashrc.
- **Boot** → BIOS/UEFI → GRUB → Kernel → systemd (PID 1).

---
        
        - Décoder base64
            - echo VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg== | base64 --decode

[Cheat sheet](https://www.notion.so/Cheat-sheet-2b73297e159781df9e28f265489a8e2e?pvs=21)
