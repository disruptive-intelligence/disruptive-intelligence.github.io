---
title: Administration Linux
source: IT/01_Linux/Admin_Linux.md
format: cours
revue: '2026-06-08'
---

*De zéro à l'autonomie — Guide pour débutant absolu*

---

> **Prérequis :** Aucun. Ce cours est conçu pour quelqu'un qui n'a jamais ouvert un terminal de sa vie.
> Tout ce dont tu as besoin, c'est un ordinateur et la possibilité d'installer une machine Linux (on t'explique comment juste après).
>
> **Orientation :** ce cours t'apprend à **utiliser, comprendre et administrer** un système Linux depuis le terminal. La progression est utile pour l'administration système classique, mais aussi pour monter en compétence en **cybersécurité défensive (SOC), pentest débutant et eJPT**. Les concepts d'admin et de sécurité sont enseignés ensemble, au moment où ils ont du sens. On apprend à **comprendre et défendre** un système, jamais à attaquer celui des autres.

---

### Glossaire — Les mots à connaître

Avant de commencer, voici les termes que tu vas croiser tout au long du cours. Reviens ici dès qu'un mot te semble flou.

| Terme | Définition simple |
|-------|------------------|
| **Terminal** | La fenêtre où tu tapes des commandes texte pour parler à ton ordinateur |
| **Shell** | Le programme qui lit et exécute tes commandes (Bash est le shell le plus courant) |
| **Commande** | Une instruction que le shell sait exécuter (`ls`, `cd`, `cat`…) |
| **Prompt** | L'invite de commande : le petit texte affiché avant ton curseur, qui attend que tu tapes |
| **Kernel (noyau)** | Le cœur du système : il fait le lien entre le matériel et les programmes |
| **Distribution (distro)** | Une version « prête à l'emploi » de Linux (Ubuntu, Debian, Kali…) |
| **Root** | Le super-administrateur : il a tous les droits sur la machine |
| **Utilisateur (user)** | Un compte qui utilise la machine, avec des droits limités |
| **Fichier** | Une unité de stockage : du texte, une image, un programme… |
| **Répertoire (dossier)** | Un conteneur qui range des fichiers et d'autres dossiers |
| **Chemin (path)** | L'adresse d'un fichier ou d'un dossier dans le système |
| **Arborescence** | L'organisation des dossiers en arbre, à partir d'une racine unique |
| **Paquet** | Un logiciel prêt à installer, avec tout ce dont il a besoin |
| **Démon (daemon)** | Un programme qui tourne en permanence en arrière-plan (ex. le serveur SSH) |
| **Processus** | Un programme en train de s'exécuter |
| **Permission (droit)** | Ce qu'un utilisateur a le droit de faire sur un fichier (lire, écrire, exécuter) |
| **Log (journal)** | Un fichier qui enregistre les événements du système (connexions, erreurs…) |
| **SSH** | Le protocole pour se connecter à distance à une machine, en sécurité |
| **Option (flag)** | Un réglage ajouté à une commande, souvent précédé d'un `-` (ex. `ls -l`) |
| **Argument** | L'information sur laquelle une commande agit (ex. le fichier dans `cat fichier.txt`) |
| **SOC** | *Security Operations Center* : l'équipe qui surveille et défend un système d'information |

---

### Comment penser Linux

Avant de taper la moindre commande, il faut comprendre **l'état d'esprit** de Linux. Si tu intègres ces trois idées, tout le reste deviendra logique.

#### 1. Tout est fichier

En Linux, presque tout est représenté comme un fichier : un document texte évidemment, mais aussi un disque dur, une imprimante, une connexion réseau, ou même un processus. Cette idée paraît étrange au début, mais elle est **libératrice** : si tout est fichier, alors les mêmes outils (lire, copier, chercher) marchent partout. Tu apprends à manipuler des fichiers une fois, et tu sais manipuler presque tout le système.

#### 2. De petits outils qu'on combine

La philosophie Linux, c'est : **un outil = une tâche, faite bien.** Plutôt qu'un énorme programme qui fait tout, Linux te donne plein de petites commandes simples. La puissance vient de leur **combinaison**. Par exemple : une commande lit un fichier de logs, une autre filtre les lignes intéressantes, une troisième les compte. Mises bout à bout, elles répondent à une vraie question. On verra ce mécanisme (les « tuyaux ») dès la Partie 1.

#### 3. Le système te fait confiance

Linux part du principe que **tu sais ce que tu fais**. Si tu lui demandes de supprimer tous tes fichiers, il le fait, sans demander « êtes-vous sûr ? » et **sans corbeille**. C'est un outil professionnel, pas une interface grand public. Cette confiance est une force (tu contrôles tout) mais elle impose une **discipline** (voir l'encadré ci-dessous). C'est tout l'enjeu de ce cours : te donner le contrôle **et** les bons réflexes.

---

### ⚠️ Les commandes à manipuler avec prudence

> **Lis ce passage avant tout le reste, et reviens-y souvent.** Certaines commandes peuvent endommager le système ou détruire des données **sans confirmation et sans retour possible**. Tu ne les utiliseras pas tout de suite, mais tu dois savoir dès maintenant qu'elles existent et qu'elles demandent de l'attention.

Les commandes à connaître comme « sensibles » (on les verra en détail au fil du cours) :

| Commande | Pourquoi elle est dangereuse |
|----------|------------------------------|
| `rm -rf` | Supprime fichiers et dossiers en masse, définitivement, sans confirmation |
| `chmod -R` | Change les permissions en cascade : peut casser tout un dossier système |
| `chown -R` | Change le propriétaire en cascade : mêmes risques |
| `dd` | Écrit directement sur un disque : une erreur peut effacer un disque entier |
| `mkfs` | Formate (= efface) un système de fichiers |
| `mount` / `umount` | Peut perturber l'accès à un disque ou un partage |
| `>` sur un fichier important | Écrase tout le contenu du fichier sans prévenir |
| `sudo` sur un chemin système | Multiplie la portée d'une erreur par les droits administrateur |

#### Les 3 règles d'or

1. **Toujours vérifier `pwd` et `ls` avant une commande destructive.** Sais-tu vraiment où tu es et sur quoi tu agis ? Vérifie avant d'appuyer sur Entrée.
2. **Toujours tester dans un dossier de lab.** Avant d'utiliser une commande puissante « pour de vrai », essaie-la dans un dossier de test sans importance.
3. **Toujours faire une copie `.bak` avant de modifier une configuration.** Une seule ligne (`cp config config.bak`) peut te sauver des heures. On en fera un réflexe au chapitre 6.

> Ces règles reviendront au bon moment dans le cours (surtout au chapitre 5, sur la suppression). Pour l'instant, garde-les simplement en tête : **la prudence n'est pas de la peur, c'est du professionnalisme.**

---

### Mettre en place ton environnement

Pour suivre ce cours, il te faut un Linux où **tu ne risques rien** : un endroit où tu peux tout casser et tout recommencer. Voici tes options, de la plus simple à la plus complète.

**Option 1 — Une machine virtuelle (recommandé).** Une machine virtuelle (VM) est un « ordinateur dans ton ordinateur ». Tu installes un logiciel comme **VirtualBox** (gratuit), puis tu y installes **Ubuntu** ou **Debian**. Avantage : c'est isolé, tu peux faire une sauvegarde de l'état (snapshot) et revenir en arrière si tu casses tout. C'est le bac à sable idéal.

**Option 2 — WSL (si tu es sur Windows).** Le *Windows Subsystem for Linux* te donne un vrai terminal Linux directement dans Windows, sans VM. Rapide à installer (`wsl --install` dans un terminal Windows administrateur). Parfait pour débuter sur les commandes, avec quelques limites sur la partie matériel/réseau qu'on verra plus tard.

**Option 3 — Un serveur cloud.** Beaucoup d'hébergeurs proposent de petites machines Linux pour quelques euros par mois. Utile plus tard pour t'entraîner au SSH et à l'administration distante (Partie 5). Pas indispensable pour commencer.

#### Quelle distribution choisir ?

> **Ubuntu ou Debian sont la base de ce cours.** Ce sont les distributions les plus répandues, les mieux documentées, et celles que tu rencontreras le plus souvent en entreprise. **Tous les exemples du cours sont écrits pour elles.**
>
> Tu entendras peut-être parler de **Kali Linux**, très populaire en cybersécurité. Kali est excellente comme boîte à outils offensive, mais **ce n'est pas une distribution d'administration quotidienne** : on la mentionnera ponctuellement pour le contexte cyber, sans en faire la base du cours. Apprends d'abord à administrer un système classique ; les outils spécialisés viendront ensuite.

#### Installer un outil quand tu en as besoin

Linux n'installe pas tous les programmes par défaut. Quand le cours te demandera un outil qui n'est pas présent (par exemple `tree` ou `htop`), tu utiliseras **deux commandes** :

```bash
sudo apt update              # met à jour la liste des logiciels disponibles
sudo apt install tree        # installe le paquet "tree"
```


> **Pour l'instant, retiens juste ce réflexe :** `sudo apt update` puis `sudo apt install <nom-du-paquet>`. Tu n'as **rien à installer maintenant** : on le fera au cas par cas, au moment où chaque outil devient utile. La gestion complète des paquets (mises à jour, suppression, recherche…) est expliquée en détail au **chapitre 20**.

---

### Table des matières

#### Partie 0 — Avant de commencer
*(glossaire, état d'esprit, prudence, installation — ci-dessus)*

#### Partie 1 — Survivre dans le terminal

1. [Le terminal, le shell et l'aide](01-partie-1-survivre-dans-le-terminal/01-chapitre-1-le-terminal-le-shell-et-l-aide.md)
2. [Se repérer dans l'arborescence](01-partie-1-survivre-dans-le-terminal/02-chapitre-2-se-reperer-dans-l-arborescence.md)
3. [Lire le contenu des fichiers](01-partie-1-survivre-dans-le-terminal/03-chapitre-3-lire-le-contenu-des-fichiers.md)
4. [Chercher, filtrer et transformer du texte](01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)

#### Partie 2 — Manipuler le système de fichiers

5. [Créer, copier, déplacer, supprimer](02-partie-2-manipuler-le-systeme-de-fichiers/01-chapitre-5-creer-copier-deplacer-supprimer.md)
6. [Éditer des fichiers dans le terminal](02-partie-2-manipuler-le-systeme-de-fichiers/02-chapitre-6-editer-des-fichiers-dans-le-terminal.md)
7. [Liens, redirections et tuyaux](02-partie-2-manipuler-le-systeme-de-fichiers/03-chapitre-7-liens-redirections-et-tuyaux.md)
8. [Variables d'environnement et configuration du shell](02-partie-2-manipuler-le-systeme-de-fichiers/04-chapitre-8-variables-d-environnement-et-configurat.md)

#### Partie 3 — Qui a le droit de quoi

9. [Comprendre les permissions](03-partie-3-qui-a-le-droit-de-quoi/01-chapitre-9-comprendre-les-permissions.md)
10. [Propriété, utilisateurs et groupes](03-partie-3-qui-a-le-droit-de-quoi/02-chapitre-10-propriete-utilisateurs-et-groupes.md)
11. [sudo et l'élévation de privilèges](03-partie-3-qui-a-le-droit-de-quoi/03-chapitre-11-sudo-et-l-elevation-de-privileges.md)
12. [Permissions avancées (panorama)](03-partie-3-qui-a-le-droit-de-quoi/04-chapitre-12-permissions-avancees-panorama.md)

#### Partie 4 — La machine vivante

13. [Les processus](04-partie-4-la-machine-vivante/01-chapitre-13-les-processus.md)
14. [Les services avec systemd](04-partie-4-la-machine-vivante/02-chapitre-14-les-services-avec-systemd.md)
15. [Les logs et journaux](04-partie-4-la-machine-vivante/03-chapitre-15-les-logs-et-journaux.md)
16. [Tâches planifiées](04-partie-4-la-machine-vivante/04-chapitre-16-taches-planifiees.md)

#### Partie 5 — Linux en réseau

17. [Les bases du réseau Linux](05-partie-5-linux-en-reseau/01-chapitre-17-les-bases-du-reseau-linux.md)
18. [SSH : se connecter à distance](05-partie-5-linux-en-reseau/02-chapitre-18-ssh-se-connecter-a-distance.md)
19. [Transférer des fichiers](05-partie-5-linux-en-reseau/03-chapitre-19-transferer-des-fichiers.md)

#### Partie 6 — Entretenir le système

20. [Gérer les paquets et logiciels](06-partie-6-entretenir-le-systeme/01-chapitre-20-gerer-les-paquets-et-logiciels.md)
21. [Stockage et espace disque](06-partie-6-entretenir-le-systeme/02-chapitre-21-stockage-et-espace-disque.md)
22. [Archives et compression](06-partie-6-entretenir-le-systeme/03-chapitre-22-archives-et-compression.md)
23. [Sauvegardes](06-partie-6-entretenir-le-systeme/04-chapitre-23-sauvegardes.md)

#### Partie 7 — Diagnostiquer, sécuriser, automatiser

24. [Diagnostic système (méthode)](07-partie-7-diagnostiquer-securiser-automatiser/01-chapitre-24-diagnostic-systeme-methode.md)
25. [Sécurité de base (durcissement)](07-partie-7-diagnostiquer-securiser-automatiser/02-chapitre-25-securite-de-base-durcissement.md)
26. [Automatiser avec Bash (admin)](07-partie-7-diagnostiquer-securiser-automatiser/03-chapitre-26-automatiser-avec-bash-admin.md)
27. [Mini-projets pratiques](07-partie-7-diagnostiquer-securiser-automatiser/04-chapitre-27-mini-projets-pratiques.md)

#### Synthèse finale

- Cheat-sheets, erreurs classiques, arbre de décision, pour continuer

#### Annexes

- Regex, sed/awk avancés, stockage avancé, pare-feu avancé, conteneurs, familles de distributions

---
---

## Sommaire

- [PARTIE 1 — Survivre dans le terminal](01-partie-1-survivre-dans-le-terminal/index.md)
    - [Chapitre 1 — Le terminal, le shell et l'aide](01-partie-1-survivre-dans-le-terminal/01-chapitre-1-le-terminal-le-shell-et-l-aide.md)
    - [Chapitre 2 — Se repérer dans l'arborescence](01-partie-1-survivre-dans-le-terminal/02-chapitre-2-se-reperer-dans-l-arborescence.md)
    - [Chapitre 3 — Lire le contenu des fichiers](01-partie-1-survivre-dans-le-terminal/03-chapitre-3-lire-le-contenu-des-fichiers.md)
    - [Chapitre 4 — Chercher, filtrer et transformer du texte](01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
- [PARTIE 2 — Manipuler le système de fichiers](02-partie-2-manipuler-le-systeme-de-fichiers/index.md)
    - [Chapitre 5 — Créer, copier, déplacer, supprimer](02-partie-2-manipuler-le-systeme-de-fichiers/01-chapitre-5-creer-copier-deplacer-supprimer.md)
    - [Chapitre 6 — Éditer des fichiers dans le terminal](02-partie-2-manipuler-le-systeme-de-fichiers/02-chapitre-6-editer-des-fichiers-dans-le-terminal.md)
    - [Chapitre 7 — Liens, redirections et tuyaux](02-partie-2-manipuler-le-systeme-de-fichiers/03-chapitre-7-liens-redirections-et-tuyaux.md)
    - [Chapitre 8 — Variables d'environnement et configuration du shell](02-partie-2-manipuler-le-systeme-de-fichiers/04-chapitre-8-variables-d-environnement-et-configurat.md)
- [PARTIE 3 — Qui a le droit de quoi](03-partie-3-qui-a-le-droit-de-quoi/index.md)
    - [Chapitre 9 — Comprendre les permissions](03-partie-3-qui-a-le-droit-de-quoi/01-chapitre-9-comprendre-les-permissions.md)
    - [Chapitre 10 — Propriété, utilisateurs et groupes](03-partie-3-qui-a-le-droit-de-quoi/02-chapitre-10-propriete-utilisateurs-et-groupes.md)
    - [Chapitre 11 — sudo et l'élévation de privilèges](03-partie-3-qui-a-le-droit-de-quoi/03-chapitre-11-sudo-et-l-elevation-de-privileges.md)
    - [Chapitre 12 — Permissions avancées (panorama)](03-partie-3-qui-a-le-droit-de-quoi/04-chapitre-12-permissions-avancees-panorama.md)
- [PARTIE 4 — La machine vivante](04-partie-4-la-machine-vivante/index.md)
    - [Chapitre 13 — Les processus](04-partie-4-la-machine-vivante/01-chapitre-13-les-processus.md)
    - [Chapitre 14 — Les services avec systemd](04-partie-4-la-machine-vivante/02-chapitre-14-les-services-avec-systemd.md)
    - [Chapitre 15 — Les logs et journaux](04-partie-4-la-machine-vivante/03-chapitre-15-les-logs-et-journaux.md)
    - [Chapitre 16 — Tâches planifiées](04-partie-4-la-machine-vivante/04-chapitre-16-taches-planifiees.md)
- [PARTIE 5 — Linux en réseau](05-partie-5-linux-en-reseau/index.md)
    - [Chapitre 17 — Les bases du réseau Linux](05-partie-5-linux-en-reseau/01-chapitre-17-les-bases-du-reseau-linux.md)
    - [Chapitre 18 — SSH : se connecter à distance](05-partie-5-linux-en-reseau/02-chapitre-18-ssh-se-connecter-a-distance.md)
    - [Chapitre 19 — Transférer des fichiers](05-partie-5-linux-en-reseau/03-chapitre-19-transferer-des-fichiers.md)
- [PARTIE 6 — Entretenir le système](06-partie-6-entretenir-le-systeme/index.md)
    - [Chapitre 20 — Gérer les paquets et logiciels](06-partie-6-entretenir-le-systeme/01-chapitre-20-gerer-les-paquets-et-logiciels.md)
    - [Chapitre 21 — Stockage et espace disque](06-partie-6-entretenir-le-systeme/02-chapitre-21-stockage-et-espace-disque.md)
    - [Chapitre 22 — Archives et compression](06-partie-6-entretenir-le-systeme/03-chapitre-22-archives-et-compression.md)
    - [Chapitre 23 — Sauvegardes](06-partie-6-entretenir-le-systeme/04-chapitre-23-sauvegardes.md)
- [PARTIE 7 — Diagnostiquer, sécuriser, automatiser](07-partie-7-diagnostiquer-securiser-automatiser/index.md)
    - [Chapitre 24 — Diagnostic système (méthode)](07-partie-7-diagnostiquer-securiser-automatiser/01-chapitre-24-diagnostic-systeme-methode.md)
    - [Chapitre 25 — Sécurité de base (durcissement)](07-partie-7-diagnostiquer-securiser-automatiser/02-chapitre-25-securite-de-base-durcissement.md)
    - [Chapitre 26 — Automatiser avec Bash (admin)](07-partie-7-diagnostiquer-securiser-automatiser/03-chapitre-26-automatiser-avec-bash-admin.md)
    - [Chapitre 27 — Mini-projets pratiques](07-partie-7-diagnostiquer-securiser-automatiser/04-chapitre-27-mini-projets-pratiques.md)
- [Synthèse finale](08-synthese-finale.md)
- [Annexes](09-annexes.md)
