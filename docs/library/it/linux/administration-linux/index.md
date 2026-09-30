---
title: Administration Linux
source: IT/01_Linux/Admin_Linux.md
chapters: 7
---

### De zéro à l'autonomie — Guide pour débutant absolu

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
1. [Le terminal, le shell et l'aide](1-partie-1-survivre-dans-le-terminal.md#chapitre-1-le-terminal-le-shell-et-laide)
2. [Se repérer dans l'arborescence](1-partie-1-survivre-dans-le-terminal.md#chapitre-2-se-reperer-dans-larborescence)
3. [Lire le contenu des fichiers](1-partie-1-survivre-dans-le-terminal.md#chapitre-3-lire-le-contenu-des-fichiers)
4. [Chercher, filtrer et transformer du texte](1-partie-1-survivre-dans-le-terminal.md#chapitre-4-chercher-filtrer-et-transformer-du-texte)

#### Partie 2 — Manipuler le système de fichiers
5. [Créer, copier, déplacer, supprimer](2-partie-2-manipuler-le-systeme-de-fichiers.md#chapitre-5-creer-copier-deplacer-supprimer)
6. [Éditer des fichiers dans le terminal](2-partie-2-manipuler-le-systeme-de-fichiers.md#chapitre-6-editer-des-fichiers-dans-le-terminal)
7. [Liens, redirections et tuyaux](2-partie-2-manipuler-le-systeme-de-fichiers.md#chapitre-7-liens-redirections-et-tuyaux)
8. [Variables d'environnement et configuration du shell](2-partie-2-manipuler-le-systeme-de-fichiers.md#chapitre-8-variables-denvironnement-et-configuration-du-shell)

#### Partie 3 — Qui a le droit de quoi
9. [Comprendre les permissions](3-partie-3-qui-a-le-droit-de-quoi.md#chapitre-9-comprendre-les-permissions)
10. [Propriété, utilisateurs et groupes](3-partie-3-qui-a-le-droit-de-quoi.md#chapitre-10-propriete-utilisateurs-et-groupes)
11. [sudo et l'élévation de privilèges](3-partie-3-qui-a-le-droit-de-quoi.md#chapitre-11-sudo-et-lelevation-de-privileges)
12. [Permissions avancées (panorama)](3-partie-3-qui-a-le-droit-de-quoi.md#chapitre-12-permissions-avancees-panorama)

#### Partie 4 — La machine vivante
13. [Les processus](4-partie-4-la-machine-vivante.md#chapitre-13-les-processus)
14. [Les services avec systemd](4-partie-4-la-machine-vivante.md#chapitre-14-les-services-avec-systemd)
15. [Les logs et journaux](4-partie-4-la-machine-vivante.md#chapitre-15-les-logs-et-journaux)
16. [Tâches planifiées](4-partie-4-la-machine-vivante.md#chapitre-16-taches-planifiees)

#### Partie 5 — Linux en réseau
17. [Les bases du réseau Linux](5-partie-5-linux-en-reseau.md#chapitre-17-les-bases-du-reseau-linux)
18. [SSH : se connecter à distance](5-partie-5-linux-en-reseau.md#chapitre-18-ssh-se-connecter-a-distance)
19. [Transférer des fichiers](5-partie-5-linux-en-reseau.md#chapitre-19-transferer-des-fichiers)

#### Partie 6 — Entretenir le système
20. [Gérer les paquets et logiciels](6-partie-6-entretenir-le-systeme.md#chapitre-20-gerer-les-paquets-et-logiciels)
21. [Stockage et espace disque](6-partie-6-entretenir-le-systeme.md#chapitre-21-stockage-et-espace-disque)
22. [Archives et compression](6-partie-6-entretenir-le-systeme.md#chapitre-22-archives-et-compression)
23. [Sauvegardes](6-partie-6-entretenir-le-systeme.md#chapitre-23-sauvegardes)

#### Partie 7 — Diagnostiquer, sécuriser, automatiser
24. [Diagnostic système (méthode)](7-partie-7-diagnostiquer-securiser-automatiser.md#chapitre-24-diagnostic-systeme-methode)
25. [Sécurité de base (durcissement)](7-partie-7-diagnostiquer-securiser-automatiser.md#chapitre-25-securite-de-base-durcissement)
26. [Automatiser avec Bash (admin)](7-partie-7-diagnostiquer-securiser-automatiser.md#chapitre-26-automatiser-avec-bash-admin)
27. [Mini-projets pratiques](7-partie-7-diagnostiquer-securiser-automatiser.md#chapitre-27-mini-projets-pratiques)

#### Synthèse finale
- Cheat-sheets, erreurs classiques, arbre de décision, pour continuer

#### Annexes
- Regex, sed/awk avancés, stockage avancé, pare-feu avancé, conteneurs, familles de distributions

---
---

## Sommaire

1. [PARTIE 1 — Survivre dans le terminal](1-partie-1-survivre-dans-le-terminal.md)
2. [PARTIE 2 — Manipuler le système de fichiers](2-partie-2-manipuler-le-systeme-de-fichiers.md)
3. [PARTIE 3 — Qui a le droit de quoi](3-partie-3-qui-a-le-droit-de-quoi.md)
4. [PARTIE 4 — La machine vivante](4-partie-4-la-machine-vivante.md)
5. [PARTIE 5 — Linux en réseau](5-partie-5-linux-en-reseau.md)
6. [PARTIE 6 — Entretenir le système](6-partie-6-entretenir-le-systeme.md)
7. [PARTIE 7 — Diagnostiquer, sécuriser, automatiser](7-partie-7-diagnostiquer-securiser-automatiser.md)
