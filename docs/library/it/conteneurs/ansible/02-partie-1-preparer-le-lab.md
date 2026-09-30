---
title: PARTIE 1 — PRÉPARER LE LAB
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
chapter: 2
chapters: 13
---

> **Objectif de la partie :** mettre en place l'environnement d'apprentissage et **valider la connexion** avant de faire quoi que ce soit avec Ansible. Un lab solide t'évitera des heures de confusion plus tard.

---


## Chapitre 1.1 — Control node et machines cibles

### Le minimum à savoir

Ansible repose sur une distinction très simple :

```
   ┌─────────────────┐       SSH       ┌─────────────────┐
   │  MACHINE DE     │ ──────────────▶ │     CIBLE 1     │
   │  CONTRÔLE       │ ──────────────▶ │     CIBLE 2     │
   │  (Ansible ICI)  │ ──────────────▶ │   (Cible 3)     │
   └─────────────────┘                 └─────────────────┘
   Tu pilotes d'ici         Les machines administrées
```

- La **machine de contrôle** (*control node*) : c'est là, et **seulement** là, qu'on **installe Ansible**. C'est ton poste de pilotage.
- Les **machines cibles** (*managed nodes*) : ce sont les machines qu'Ansible **administre**. On **n'installe pas** Ansible dessus.

#### Le point qui surprend : « agentless »

Ansible n'installe **aucun programme permanent** sur les cibles. On dit qu'il est **agentless** (sans agent). Il se connecte en **SSH** (comme tu le ferais à la main), fait son travail en s'appuyant sur **Python** (déjà présent sur la plupart des Linux), puis se déconnecte. Rien ne reste installé sur les cibles.

> **Conséquence pratique :** si une machine est accessible en **SSH** et qu'elle a **Python**, Ansible peut l'administrer **immédiatement**. Pas de déploiement d'agent, pas de configuration lourde sur les cibles.

### Très utile en pratique

Sur la **machine de contrôle**, une seule commande confirmera (plus tard) qu'Ansible est là :

```bash
ansible --version
```

Sur les **cibles**, tu ne vérifies **pas** « si Ansible est installé » (il ne l'est pas, et c'est normal). Tu vérifieras seulement qu'elles répondent en **SSH** — c'est l'objet des chapitres suivants.

### Exemple simple

Le lab de ce cours, c'est :

```text
control   → 1 VM Linux, on y installe Ansible
cible1    → 1 VM Linux, rien à installer
cible2    → 1 VM Linux, rien à installer
(cible3)  → optionnelle, pour s'entraîner aux groupes plus tard
```

Trois petites VMs Linux sur ton ordinateur, reliées par un réseau local. C'est tout.

### 🔀 À ne pas confondre

> **« Agentless » ne veut pas dire « rien sur les cibles ».**
> Les cibles ont besoin de **SSH** (pour la connexion) et de **Python** (pour exécuter le travail). Simplement, il n'y a **pas d'agent Ansible** à installer et à maintenir.

### ❌ Erreur classique

> **Vouloir « installer Ansible sur les machines cibles ».**

Si tu viens d'outils qui posent un agent partout, tu pourrais croire qu'il faut installer Ansible sur chaque cible. **C'est inutile.** Le réflexe correct : **Ansible s'installe uniquement sur la machine de contrôle**. Les cibles n'ont besoin que de SSH et Python. Si tu te surprends à vouloir installer Ansible sur « cible1 », arrête-toi : ce n'est pas comme ça que ça marche.

### Exercices

#### Guidé
Sur une feuille, dessine ton futur lab : une machine de contrôle, deux cibles, et des flèches **SSH** qui partent du contrôle vers les cibles. Écris « Ansible installé ici » sur la machine de contrôle, et « SSH + Python » sur les cibles.

#### Autonome
Explique avec tes mots ce que veut dire **agentless**, et donne **un avantage** concret pour quelqu'un qui doit administrer beaucoup de machines.

#### Défi
Pourquoi est-ce pratique qu'Ansible utilise **SSH** plutôt qu'un protocole spécial à lui ? (Indice : pense à ce que tu sais déjà faire avec SSH, et à ce qui est déjà en place sur tes serveurs Linux.)

### ✅ Tu sais maintenant…

- La distinction **machine de contrôle** (Ansible installé) vs **cibles** (rien d'installé).
- Ce que veut dire **agentless** : pas d'agent permanent, juste **SSH + Python** sur les cibles.
- Qu'Ansible s'installe **uniquement** sur la machine de contrôle.
- À quoi ressemble le lab du cours (1 contrôle + 2-3 cibles Linux).

---


## Chapitre 1.2 — SSH et clés

### Le minimum à savoir

Ansible n'a pas de « canal magique ». Il utilise **SSH**, exactement le même que celui que tu utilises pour te connecter à un serveur à la main. **C'est la fondation de tout le cours.**

La règle d'or :

> **Si `ssh utilisateur@cible` marche à la main, alors Ansible marchera. Si SSH ne marche pas, Ansible ne marchera pas non plus.** SSH d'abord, Ansible ensuite.

#### Mot de passe ou clé ?

On peut se connecter en SSH par **mot de passe**, mais pour Ansible (et pour le confort), on utilise des **clés SSH**. Une clé SSH, c'est une **paire** :

- une **clé privée**, qui reste **secrète** sur la machine de contrôle ;
- une **clé publique**, qu'on **dépose** sur chaque cible.

Une fois la clé publique déposée, tu te connectes **sans taper de mot de passe** : la cible reconnaît ta clé.

```
   MACHINE DE CONTRÔLE                 CIBLE
   ┌──────────────────┐                ┌──────────────────┐
   │  clé PRIVÉE      │ ── prouve ───▶ │  clé PUBLIQUE    │
   │  (reste secrète) │   l'identité   │  (déposée ici)   │
   └──────────────────┘                └──────────────────┘
```

### Très utile en pratique

Les trois commandes à connaître (sur la **machine de contrôle**) :

```bash
# 1. Générer une paire de clés (si tu n'en as pas déjà)
ssh-keygen -t ed25519

# 2. Déposer la clé publique sur une cible
ssh-copy-id utilisateur@192.168.56.11

# 3. Vérifier qu'on se connecte SANS mot de passe
ssh utilisateur@192.168.56.11
```

Si la troisième commande t'ouvre une session **sans demander de mot de passe**, tout est prêt pour Ansible.

```text
$ ssh admin@192.168.56.11
Welcome to Ubuntu ...
admin@cible1:~$        ← connecté sans mot de passe : parfait
```

### Exemple simple

Tu génères ta clé une fois, puis tu la déposes sur chaque cible :

```bash
ssh-keygen -t ed25519                       # une seule fois, sur le contrôle
ssh-copy-id admin@192.168.56.11             # cible1
ssh-copy-id admin@192.168.56.12             # cible2
ssh admin@192.168.56.11                     # test : doit marcher sans mot de passe
```

### 🛡️ Réflexe sécurité

> La **clé privée** reste sur la machine de contrôle et **ne se partage jamais**. C'est elle qui ouvre l'accès à tes cibles. Traite-la comme un trousseau de clés : on ne le laisse pas traîner, on ne l'envoie pas par mail. (On reparlera de protéger les secrets en Partie 9.)

### ❌ Erreur classique

> **Essayer de faire marcher Ansible alors que SSH ne marche pas encore à la main.**

C'est **l'**erreur n°1 du débutant. On lance Ansible, ça échoue, et on cherche le problème dans Ansible… alors qu'il est dans **SSH** (mauvaise clé, mauvais utilisateur, machine pas joignable). Le réflexe correct : **toujours tester `ssh utilisateur@cible` à la main d'abord**. Si la connexion manuelle échoue, Ansible échouera aussi — Ansible ne **répare** pas SSH, il s'**appuie** dessus.

### Exercices

#### Guidé
Sur ta machine de contrôle, génère une paire de clés avec `ssh-keygen -t ed25519`. Dépose la clé publique sur **une** cible avec `ssh-copy-id`. Connecte-toi ensuite avec `ssh utilisateur@cible` et vérifie que **tu n'as pas à taper de mot de passe**.

#### Autonome
Explique avec tes mots la différence entre la **clé privée** et la **clé publique** : laquelle reste secrète, laquelle se distribue, et pourquoi ce système permet de se connecter sans mot de passe.

#### Défi
Fais le test sur la **deuxième** cible. Puis, depuis la machine de contrôle, connecte-toi successivement aux deux cibles. Si l'une demande un mot de passe et pas l'autre, trouve **pourquoi** (la clé publique a-t-elle bien été déposée sur les deux ?).

### ✅ Tu sais maintenant…

- Qu'Ansible utilise **SSH**, et que **SSH doit marcher avant Ansible**.
- Le principe d'une **paire de clés** : privée (secrète, sur le contrôle) / publique (déposée sur les cibles).
- Générer et déposer une clé : `ssh-keygen`, `ssh-copy-id`, test avec `ssh`.
- Que la **clé privée** ne se partage jamais.

---


## Chapitre 1.3 — Installer Ansible

### Le minimum à savoir

On installe Ansible **uniquement sur la machine de contrôle**. Les cibles, elles, n'ont besoin de rien (juste SSH + Python, déjà vus).

Il y a deux façons courantes d'installer Ansible sur un Linux :

1. **Via le gestionnaire de paquets** de ta distribution — simple, parfait pour un lab.
2. **Via `pipx`** — installe Ansible dans un environnement isolé, plus propre et à jour.

> Les commandes d'installation **évoluent** avec le temps et dépendent de ta distribution. En cas de doute, la **documentation officielle d'Ansible fait foi**. Voici les deux approches générales :

### Très utile en pratique

```bash
# Option 1 — simple, pour un lab (familles Debian/Ubuntu)
sudo apt update && sudo apt install -y ansible

# Option 2 — propre et isolée (recommandée si tu connais un peu Python)
pipx install --include-deps ansible

# Vérifier que c'est installé (sur la machine de contrôle)
ansible --version
```

`ansible --version` doit afficher un numéro de version. Si la commande est introuvable, c'est qu'Ansible n'est pas (encore) installé, ou pas dans le `PATH`.

### Exemple simple

```text
$ ansible --version
ansible [core 2.x.x]
  config file = ...
  python version = 3.x.x ...
```

Cet affichage = Ansible est prêt sur ta machine de contrôle.

### 🔀 À ne pas confondre

> **Installer Ansible (sur le contrôle) ≠ préparer les cibles.**
> Tu installes Ansible **une seule fois**, sur la machine de contrôle. Tu n'installes **rien** sur les cibles. Si tu te retrouves à lancer `apt install ansible` sur « cible1 », c'est une erreur.

### ❌ Erreur classique

> **Installer Ansible sur les cibles, ou s'attendre à un décalage de version.**

Deux pièges fréquents. D'abord, installer Ansible partout (inutile : seul le contrôle en a besoin). Ensuite, s'étonner que la version du paquet de la distribution soit un peu ancienne — c'est normal. Pour un lab, ce n'est pas grave. Si tu veux la version la plus récente, l'option `pipx` est préférable. Le réflexe correct : **Ansible sur le contrôle uniquement**, et la **doc officielle** comme référence en cas de doute.

### Exercices

#### Guidé
Installe Ansible sur ta machine de contrôle (choisis l'option `apt` ou `pipx`). Lance `ansible --version` et vérifie qu'un numéro de version s'affiche. Note la commande qui a fonctionné pour ta distribution.

#### Autonome
Connecte-toi à une de tes **cibles** et lance `ansible --version`. Que se passe-t-il ? Explique pourquoi c'est **normal** que la commande ne soit pas trouvée sur la cible.

#### Défi
Compare les deux méthodes d'installation (`apt` vs `pipx`) en une ou deux phrases chacune : avantage principal de chacune pour un débutant. Laquelle choisirais-tu et pourquoi ?

### ✅ Tu sais maintenant…

- Qu'on installe Ansible **uniquement sur la machine de contrôle**.
- Les deux méthodes courantes : **paquet de la distribution** (`apt`) ou **`pipx`** (isolé).
- Vérifier l'installation avec **`ansible --version`**.
- Que la version du paquet peut être un peu ancienne (normal pour un lab).

---


## Chapitre 1.4 — Snapshots et erreurs SSH classiques

### Le minimum à savoir

Avant de commencer à « casser » des choses en apprenant, mets en place ton **filet de sécurité** : les **snapshots**.

Un **snapshot** (instantané) est une **photo** de l'état d'une VM à un moment donné. Si un essai casse une cible, tu **restaures** le snapshot et tu repars de l'état sain en quelques secondes. VirtualBox et VMware proposent tous les deux cette fonction.

> 🧪 **Lab vs production :** en lab, les snapshots te donnent une **liberté totale** d'expérimenter. Tu tentes, tu observes, et si ça tourne mal, tu restaures. C'est exactement ce qui rend l'apprentissage **serein**. (En production, on n'a pas ce confort — d'où l'importance d'apprendre **maintenant**, en lab.)

#### Les erreurs SSH les plus fréquentes

Comme Ansible passe par SSH, les premiers blocages viennent presque toujours de là :

| Message / symptôme | Cause probable | Quoi vérifier |
|--------------------|----------------|---------------|
| `Permission denied` | Mauvaise clé ou mauvais utilisateur | La clé publique est-elle déposée ? Bon utilisateur ? |
| `Connection refused` / timeout | Cible éteinte, mauvaise IP, réseau | La VM tourne ? La bonne IP ? Même réseau ? |
| Demande de mot de passe | Clé publique pas déposée | Refaire `ssh-copy-id` |
| `Host key verification failed` | Clé d'hôte changée (VM recréée) | Nettoyer l'ancienne entrée `known_hosts` |

### Très utile en pratique

```bash
# Tester la connexion à la main (TOUJOURS le premier réflexe)
ssh admin@192.168.56.11

# Voir plus de détails si ça échoue (verbeux)
ssh -v admin@192.168.56.11
```

> 🔍 **Réflexe diagnostic :** au moindre souci avec Ansible **au début du cours**, reviens à `ssh utilisateur@cible` à la main. Si ça échoue, le problème est dans **SSH/le réseau**, pas dans Ansible. Règle SSH d'abord.

### Exemple simple

Le bon ordre des opérations pour un lab sain :

```text
1. Les 3 VMs démarrent et se voient sur le réseau
2. SSH par clé fonctionne du contrôle vers chaque cible (testé à la main)
3. SNAPSHOT de chaque VM, nommé "lab-pret"   ← ton point de restauration
```

### ❌ Erreur classique

> **Monter un lab « presque bon » : pas de snapshot, réseau bancal, et chercher des bugs Ansible qui sont en réalité des bugs réseau.**

Sans snapshot, le moindre essai raté t'oblige à tout refaire. Et un réseau mal configuré transforme chaque exercice en chasse au bug qui n'a **rien à voir** avec Ansible. Le réflexe correct : **valider SSH à la main** sur chaque cible, **puis** prendre un snapshot « lab-pret » avant de continuer. Trente secondes de préparation t'épargnent des heures de frustration.

### Exercices

#### Guidé
Une fois que SSH par clé fonctionne vers tes deux cibles, prends un **snapshot** de chaque VM (contrôle + cibles), nommé « lab-pret ». Tu viens de créer ton point de restauration.

#### Autonome
Casse volontairement quelque chose sur une cible (par exemple, supprime la clé publique déposée, ou éteins la VM) et observe l'échec de `ssh`. Puis **restaure le snapshot** « lab-pret » et vérifie que la connexion refonctionne. Tu viens de tester ton filet de sécurité.

#### Défi
Provoque une erreur `Host key verification failed` : recrée (ou réinitialise) une cible après t'y être déjà connecté, puis retente `ssh`. Lis le message. Sans forcément le résoudre, explique **pourquoi** SSH se méfie quand la clé d'hôte change (indice : c'est une protection de sécurité).

### ✅ Tu sais maintenant…

- Ce qu'est un **snapshot** et pourquoi il rend l'apprentissage **serein**.
- À prendre un snapshot **« lab-pret »** une fois SSH validé.
- Les **erreurs SSH** les plus fréquentes et quoi vérifier pour chacune.
- Le réflexe : au moindre souci, **tester `ssh` à la main d'abord**.

---

### 🚩 Checkpoint — Fin de la Partie 1

Ton lab est prêt. Avant de décrire ton parc et d'agir avec Ansible, assure-toi de pouvoir :

- [ ] Expliquer la différence **machine de contrôle** / **cibles**, et le principe **agentless**.
- [ ] Avoir **Ansible installé** sur la machine de contrôle (`ansible --version` répond).
- [ ] Te connecter en **SSH par clé** (sans mot de passe) à **chaque** cible.
- [ ] Comprendre que **SSH doit marcher avant Ansible**.
- [ ] Avoir pris un **snapshot « lab-pret »** de chaque VM.
- [ ] Reconnaître les **erreurs SSH** courantes et savoir tester `ssh` à la main.

> **🧩 Mini-projet 1 — « Le lab opérationnel ».**
> 1. Crée tes VMs : une machine de contrôle (avec Ansible) et deux cibles Linux, sur un réseau commun.
> 2. Génère une paire de clés sur le contrôle et dépose la clé publique sur **chaque** cible.
> 3. Vérifie `ssh utilisateur@cible` **sans mot de passe** vers les deux cibles.
> 4. Prends un **snapshot « lab-pret »** de chaque VM.
> Objectif : disposer d'un lab **fiable**, prêt pour la suite, avec le réflexe « je valide SSH à la main avant Ansible ».

> **La suite :** en Partie 2, on décrit nos machines dans un **inventaire**, et on lance nos **premières commandes ad hoc** avec Ansible — enfin de l'action ! On apprendra aussi à lire les premières **sorties** (`ok`, `changed`, `failed`, `skipped`, `unreachable`).

---
---
---
