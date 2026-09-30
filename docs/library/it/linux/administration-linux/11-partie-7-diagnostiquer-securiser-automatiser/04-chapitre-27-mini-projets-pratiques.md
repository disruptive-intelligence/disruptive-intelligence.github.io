---
title: Chapitre 27 — Mini-projets pratiques
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 7 — Diagnostiquer, sécuriser, automatiser
  - index.md
---

Voici trois projets fil rouge qui mobilisent **l'ensemble du cours**. Ils sont conçus pour être réalisés sur ta machine d'apprentissage ou une VM dédiée. Prends ton temps : la valeur est dans la réalisation, pas dans la lecture.

---

## Projet 1 — Mettre en service un serveur (orientation admin)

**Objectif :** partir d'une machine fraîchement installée et la rendre opérationnelle, propre et sécurisée. C'est la synthèse de l'administration classique.

> **⚠️ À faire en lab :** réalise ce projet dans une **VM locale ou un serveur de lab**. N'expose **pas** un service sur Internet tant que tu n'as pas solidement compris le pare-feu, les mises à jour, les logs et les sauvegardes. Un serveur mal préparé exposé au Web est attaqué en quelques minutes.

**Étapes proposées :**

1. **Première prise en main** (parties 1-2) : connecte-toi, repère-toi (`pwd`, `ls`, arborescence), mets à jour le système (`sudo apt update && sudo apt upgrade`).
2. **Comptes** (partie 3) : crée un utilisateur d'administration dédié (`adduser`), ajoute-le au groupe `sudo` (`usermod -aG sudo`), vérifie ses droits (`id`, `sudo -l`).
3. **Accès distant sécurisé** (partie 5) : mets en place l'authentification SSH par clé (`ssh-keygen`, `ssh-copy-id`), puis durcis `sshd_config` (`PermitRootLogin no`, clés uniquement) avec le réflexe `.bak`/`sudoedit`/`diff`. **Garde une session de secours.**
4. **Pare-feu** (partie 7) : configure `ufw` (deny par défaut, autorise SSH **avant** d'activer).
5. **Un service** (partie 4) : installe un service simple (par exemple un serveur web), vérifie son `systemctl status`, active-le au démarrage (`enable --now`), confirme qu'il écoute (`ss -tulpn`).
6. **Sauvegardes** (partie 6) : écris un petit script de sauvegarde (`rsync` ou `tar` horodaté), teste-le, puis planifie-le en cron.
7. **Vérification finale** : déroule la checklist de durcissement du chapitre 25.

**Livrable :** une machine opérationnelle + un court document décrivant ce que tu as configuré et pourquoi.

---

## Projet 2 — Script de surveillance défensive (orientation SOC)

**Objectif :** créer un tableau de bord texte qui donne, en un coup d'œil, l'état de santé et de sécurité de la machine. C'est l'outil quotidien d'un analyste.

**Ce que le script doit produire** (un rapport horodaté) :

1. **Santé système** (parties 4, 6) : charge (`uptime`), mémoire (`free -h`), espace disque (`df -h`).
2. **Services clés** (partie 4) : état des services importants (SSH, pare-feu…) via `systemctl is-active`.
3. **Réseau** (partie 5) : ports actuellement en écoute (`ss -tulpn`).
4. **Sécurité — connexions** (parties 1, 3, 4) : dernières connexions réussies, et surtout les **tentatives d'authentification échouées** récentes, en isolant les IP sources les plus fréquentes (le pipeline `grep`/`awk`/`sort`/`uniq -c` du chapitre 4, appliqué à `auth.log`/`secure` ou via `journalctl`).
5. **Mise en forme** : un rapport clair, horodaté (`$(date)`), enregistré dans un fichier daté et/ou affiché avec `tee`.

**Étapes :**

- Construis le script section par section (chapitre 26), en testant chaque bloc à la main d'abord.
- Rends-le exécutable, range-le dans `~/bin`.
- Planifie-le (cron) pour un rapport quotidien automatique.

**Livrable :** un script `surveillance.sh` fonctionnel + un exemple de rapport généré. C'est une véritable première brique de supervision défensive.

---

## Projet 3 — Investigation d'incident (orientation cyber / eJPT)

**Objectif :** à partir d'un jeu de logs (réels de ta machine, ou un jeu de logs d'entraînement que tu te constitues), **reconstituer le déroulé d'une activité suspecte**. C'est l'exercice central de l'analyse défensive.

**Trame d'investigation :**

1. **Collecte** (parties 1, 6) : rassemble les logs pertinents sans les altérer (`rsync`/`tar` qui préservent les dates, chapitre 19/22). Travaille sur des **copies**.
2. **Connexions** (parties 1, 4) : dans le journal d'authentification, distingue les connexions réussies des échecs. Y a-t-il une rafale d'échecs (signe de force brute) ? Suivie d'une réussite (compromission possible) ? Depuis quelles IP ? (pipeline du chapitre 4 / `journalctl` du chapitre 15.)
3. **Privilèges** (partie 3) : recherche les usages de `sudo` dans les logs. Une élévation de privilèges inattendue ? Par quel compte ?
4. **Persistance** (partie 4) : inspecte les tâches planifiées (`crontab -l`, `/etc/cron.*`) et les services (`systemctl list-units`). Quelque chose d'anormal aurait-il été ajouté ?
5. **Traces sur le système** (parties 2, 3) : cherche des fichiers récents ou suspects (`find` par date), des binaires SUID ou capabilities inattendus (`find -perm -4000`, `getcap -r /`, chapitre 12), des fichiers dans des emplacements inhabituels (`/tmp`).
6. **Synthèse** : rédige une **chronologie** de ce que tu as reconstitué — quoi, quand, depuis où, par quel compte — comme un mini-rapport d'incident.

**Livrable :** un rapport d'investigation : la chronologie reconstituée, les indices retenus, et les recommandations (que faudrait-il durcir pour empêcher la récidive ? → chapitre 25).

> **Note éthique :** cet exercice est **défensif**. On apprend à **comprendre et reconstituer** une activité pour mieux protéger, jamais à attaquer un système qui ne nous appartient pas. Entraîne-toi uniquement sur tes propres machines ou des environnements prévus pour l'apprentissage.

---

> **🏁 CHECKPOINT FINAL — Fin du cours**
>
> Tu es allé du tout début — ouvrir un terminal sans savoir quoi en faire — jusqu'à savoir **administrer, diagnostiquer, sécuriser et automatiser** un système Linux, avec les réflexes défensifs d'un analyste. C'est un parcours considérable.
>
> **Tu sais maintenant :**
> - survivre et te repérer dans le terminal (parties 1-2) ;
> - comprendre le modèle de sécurité de Linux : permissions, utilisateurs, privilèges (partie 3) ;
> - piloter une machine vivante : processus, services, logs, planification (partie 4) ;
> - administrer une machine à distance et en réseau (partie 5) ;
> - entretenir un système : paquets, disque, archives, sauvegardes (partie 6) ;
> - diagnostiquer, durcir et automatiser (partie 7).
>
> La suite t'appartient : pratique sur tes propres machines, approfondis le **scripting Bash**, et explore les pistes **SOC / pentest / eJPT** qui prolongent naturellement ces fondations.

---

---
---
