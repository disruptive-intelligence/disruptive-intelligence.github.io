---
title: Partie 6 — Variables, facts, conditions et boucles
source: IT/08 Conteneurs & automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - index.md
---

> **Objectif de la partie :** rendre tes playbooks **adaptables**. Avec les variables, les facts, les conditions et les boucles, un même playbook s'ajuste à chaque machine au lieu de tout coder en dur.

---


## Chapitre 6.1 — Variables et `{{ }}`

### Le minimum à savoir

Une **variable** permet de ne pas coder une valeur « en dur ». Au lieu d'écrire `nginx` partout, tu définis une variable et tu la réutilises.

```yaml
- name: Installer le serveur web
  hosts: web
  become: true
  vars:
    paquet_web: nginx          # ← on DÉFINIT la variable
  tasks:
    - name: Installer
      ansible.builtin.apt:
        name: "{{ paquet_web }}"   # ← on UTILISE la variable avec {{ }}
        state: present
```


> **La syntaxe `{{ nom_variable }}`** sert à **utiliser** une variable. Les doubles accolades disent à Ansible : « remplace ceci par la valeur de la variable ».

### Très utile en pratique

Les variables servent à :

- Éviter de répéter une valeur (et de devoir la changer à dix endroits).
- Adapter un playbook selon le contexte (un port différent par groupe, par exemple).
- Rendre un playbook **réutilisable**.

### Exemple simple

```yaml
vars:
  port: 8080
tasks:
  - name: Afficher le port
    ansible.builtin.debug:
      msg: "Le port configuré est {{ port }}"
```


### ❌ Erreur classique

> **Oublier les guillemets autour d'une valeur qui commence par `{{ }}`.**

En YAML, une valeur qui **commence** par `{{` doit être entre guillemets : `name: "{{ paquet_web }}"`. Sans guillemets, YAML peut mal l'interpréter. Le réflexe correct : **mets des guillemets** dès qu'une valeur commence par `{{`.

### Exercices

#### Guidé
Reprends ton playbook nginx et remplace le nom du paquet en dur par une variable `paquet_web` définie dans `vars:`. Vérifie que le playbook fonctionne exactement comme avant — mais maintenant, c'est paramétré.

#### Autonome
Définis une variable `port` et utilise-la dans un message `debug`. Lance le playbook et observe la valeur affichée. Change la valeur de la variable et relance : le message s'adapte.

#### Défi
Crée un playbook avec **deux** variables (un paquet et un port) et utilise-les dans deux tâches différentes. En quoi le fait d'avoir les valeurs **en haut** du playbook (dans `vars:`) rend-il la maintenance plus facile ?

### ✅ Tu sais maintenant…

- Définir une variable dans **`vars:`** et l'utiliser avec **`{{ }}`**.
- Que les variables évitent les répétitions et rendent les playbooks réutilisables.
- Qu'une valeur commençant par `{{` doit être **entre guillemets**.

---


## Chapitre 6.2 — `group_vars` et `host_vars`

### Le minimum à savoir

Mettre toutes les variables dans le playbook devient vite lourd. La bonne pratique : les **ranger** dans des dossiers dédiés, chargés **automatiquement** par Ansible.

```
projet/
├── inventory.ini
├── group_vars/
│   ├── all.yml          # variables pour TOUTES les machines
│   └── web.yml          # variables pour le groupe "web"
└── host_vars/
    └── cible1.yml       # variables pour l'hôte "cible1" uniquement
```


```yaml
# group_vars/web.yml
paquet_web: nginx
port_web: 80
```


> **Le principe :** Ansible charge **tout seul** les variables du bon fichier selon le groupe ou l'hôte ciblé. Une machine du groupe `web` reçoit les variables de `group_vars/web.yml`. C'est propre et organisé.

### Très utile en pratique

```bash
# Voir toutes les variables effectives d'un hôte
ansible-inventory -i inventory.ini --host cible1
```


La règle de priorité, version simple :

> **Du plus général au plus spécifique :** `group_vars/all` < `group_vars/<groupe>` < `host_vars/<hôte>`. Plus c'est **spécifique**, plus ça **l'emporte**.

### Exemple simple

```yaml
# group_vars/all.yml
fuseau_horaire: Europe/Paris

# group_vars/web.yml
paquet_web: nginx
```


Toutes les machines reçoivent `fuseau_horaire` ; celles du groupe `web` reçoivent **en plus** `paquet_web`.

### 🔍 Réflexe diagnostic

> Si une variable « ne prend pas la bonne valeur », c'est presque toujours une question de **priorité** : la même variable est définie à un endroit plus spécifique. **`ansible-inventory --host <machine>`** te montre la valeur réellement appliquée.

### ❌ Erreur classique

> **Définir une variable à plusieurs endroits et obtenir une valeur surprenante.**

Tu mets `port_web: 80` dans `group_vars/web.yml`, mais un vieux `port_web: 8080` traîne dans `host_vars/cible1.yml` : sur cible1, ce sera 8080. Le réflexe correct : connaître la règle (**spécifique > général**) et utiliser `--host` pour voir la valeur effective.

### Exercices

#### Guidé
Crée un dossier `group_vars/` avec un fichier `web.yml` contenant `paquet_web: nginx`. Modifie ton playbook pour utiliser `{{ paquet_web }}` sans définir la variable dans le playbook (elle vient du `group_vars`). Vérifie que ça marche.

#### Autonome
Ajoute `host_vars/cible1.yml` avec une variable spécifique à cette machine. Lance `ansible-inventory --host cible1` et `--host cible2` et compare les variables de chacune.

#### Défi
Définis la **même** variable dans `group_vars/web.yml` et dans `host_vars/cible1.yml` avec des valeurs différentes. Vérifie avec `--host` laquelle gagne sur cible1. Explique la règle de priorité que tu observes.

### ✅ Tu sais maintenant…

- Ranger les variables dans **`group_vars/`** et **`host_vars/`** (chargement automatique).
- La règle de priorité simple : **spécifique > général**.
- Voir les variables effectives avec **`ansible-inventory --host`**.

---


## Chapitre 6.3 — Les facts et le module `setup`

### Le minimum à savoir

Avant d'exécuter ses tâches, Ansible **récolte automatiquement** des informations sur chaque machine : système d'exploitation, version, IP, mémoire, etc. Ce sont les **facts**.

```bash
# Voir tous les facts d'une machine
ansible cible1 -i inventory.ini -m ansible.builtin.setup

# Filtrer un fact précis
ansible cible1 -i inventory.ini -m ansible.builtin.setup -a "filter=ansible_distribution"
```


```yaml
# Utiliser un fact dans un playbook
- name: Afficher la distribution
  ansible.builtin.debug:
    msg: "{{ ansible_distribution }} {{ ansible_distribution_version }}"
```


> **Les facts sont une mine d'or :** sans rien configurer, Ansible connaît l'OS, la version, l'IP de chaque machine. Quelques facts utiles : `ansible_distribution` (Ubuntu, Debian…), `ansible_distribution_version`, `ansible_os_family` (Debian, RedHat…), `ansible_hostname`.

### Très utile en pratique

Les facts servent surtout à **adapter** un playbook : faire quelque chose **selon l'OS**, par exemple. On combine ça avec les conditions (chapitre suivant).

### Exemple simple

```yaml
- name: Afficher des infos sur la machine
  ansible.builtin.debug:
    msg: "{{ ansible_hostname }} tourne sous {{ ansible_distribution }}"
```


### 🔀 À ne pas confondre

> **Variable que tu définis vs fact qu'Ansible récolte.**
> Une **variable** (`vars`, `group_vars`), c'est **toi** qui la fixes. Un **fact** (`ansible_distribution`…), c'est Ansible qui le **découvre** sur la machine. Les deux s'utilisent avec `{{ }}`, mais l'origine diffère.

### ❌ Erreur classique

> **Inventer un nom de fact au lieu de vérifier le vrai nom.**

On écrit `{{ ansible_os }}` alors que le bon nom est `{{ ansible_os_family }}` ou `{{ ansible_distribution }}`. Le réflexe correct : lancer `ansible <machine> -m ansible.builtin.setup` (ou avec `filter=`) pour **voir les vrais noms** des facts disponibles.

### Exercices

#### Guidé
Lance `ansible cible1 -i inventory.ini -m ansible.builtin.setup` et parcours la sortie. Repère `ansible_distribution`, `ansible_distribution_version` et `ansible_hostname`. Puis affiche-les dans un playbook avec `debug`.

#### Autonome
Avec `filter=ansible_*`, explore quelques facts (mémoire, processeur, interfaces réseau). Affiche-en deux ou trois dans un message `debug`.

#### Défi
Écris un playbook qui affiche, pour **chaque** machine, une phrase du type « cible1 : Ubuntu 24.04, famille Debian ». Tu combines plusieurs facts dans un seul message.

### ✅ Tu sais maintenant…

- Que les **facts** sont des infos qu'Ansible **récolte automatiquement** sur les machines.
- Les voir avec le module **`setup`** (et `filter=`).
- Quelques facts utiles : `ansible_distribution`, `ansible_os_family`, `ansible_hostname`.
- La différence entre une **variable** (que tu fixes) et un **fact** (qu'Ansible découvre).

---


## Chapitre 6.4 — Les conditions (`when`)

### Le minimum à savoir

**`when`** exécute une tâche **seulement si** une condition est vraie. C'est souvent combiné avec les facts pour s'adapter à chaque machine.

```yaml
- name: Installer avec apt (familles Debian/Ubuntu)
  ansible.builtin.apt:
    name: htop
    state: present
  when: ansible_os_family == "Debian"
  become: true

- name: Installer avec dnf (familles RedHat/Fedora)
  ansible.builtin.dnf:
    name: htop
    state: present
  when: ansible_os_family == "RedHat"
  become: true
```


Une tâche dont la condition est **fausse** apparaît en **`skipped`** (rappel : Partie 2).

### Très utile en pratique

`when` permet d'écrire **un seul** playbook qui fonctionne sur des machines **différentes** : Ubuntu et Fedora, par exemple. Chaque tâche s'exécute là où elle a du sens, et est ignorée ailleurs.

### Exemple simple

```yaml
- name: Message seulement pour Ubuntu
  ansible.builtin.debug:
    msg: "Cette machine est sous Ubuntu"
  when: ansible_distribution == "Ubuntu"
```


### 🔀 À ne pas confondre

> **`skipped` n'est pas une erreur.**
> Une tâche `skipped` n'a **pas** échoué : elle a été **volontairement ignorée** parce que sa condition n'était pas remplie. C'est normal et attendu. Ne confonds pas `skipped` (ignoré) avec `failed` (échoué).

### ❌ Erreur classique

> **Comparer avec `=` au lieu de `==`, ou se tromper de nom de fact.**

En condition, l'égalité s'écrit `==` (double), pas `=`. Et il faut le **bon** nom de fact (`ansible_os_family`, pas `ansible_os`). Le réflexe correct : `==` pour comparer, et vérifier les noms de facts avec `setup`.

### Exercices

#### Guidé
Écris deux tâches d'installation : une avec `when: ansible_os_family == "Debian"`, une avec `when: ansible_os_family == "RedHat"`. Lance sur tes cibles (probablement Debian/Ubuntu) et observe : une tâche s'exécute, l'autre est `skipped`.

#### Autonome
Crée une tâche qui n'affiche un message que si la machine s'appelle `cible1` (`when: ansible_hostname == "cible1"`). Lance sur tout le parc et observe quelles machines exécutent la tâche et lesquelles la sautent.

#### Défi
Combine **deux** conditions avec `and` (par exemple : famille Debian **et** un certain nom d'hôte). Teste et observe le résultat. Comment l'ajout de conditions affine-t-il le ciblage ?

### ✅ Tu sais maintenant…

- Utiliser **`when`** pour exécuter une tâche **sous condition**.
- Combiner `when` avec les **facts** pour s'adapter à l'OS.
- Qu'une tâche non remplie passe en **`skipped`** (ignorée, pas échouée).
- Comparer avec **`==`** (et utiliser les bons noms de facts).

---


## Chapitre 6.5 — Les boucles (`loop`)

### Le minimum à savoir

**`loop`** répète une tâche sur une **liste**, au lieu de la copier-coller plusieurs fois.

```yaml
- name: Installer plusieurs paquets
  ansible.builtin.apt:
    name: "{{ item }}"          # ← "item" = l'élément courant de la boucle
    state: present
  loop:
    - htop
    - git
    - curl
  become: true
```


> **Le mot-clé `item`** représente l'élément en cours de la boucle. À chaque tour, `{{ item }}` prend la valeur suivante de la liste.

### Très utile en pratique

`loop` évite la répétition. Sans lui, tu écrirais trois tâches pour trois paquets. Avec lui, **une** tâche suffit. On peut boucler sur des paquets, des utilisateurs, des fichiers…

### Exemple simple

```yaml
- name: Créer plusieurs utilisateurs
  ansible.builtin.user:
    name: "{{ item }}"
    state: present
  loop:
    - alice
    - bob
    - charlie
  become: true
```


### 🔀 À ne pas confondre

> **Le module `apt` accepte déjà une liste de paquets** (`name: [htop, git]`) sans boucle. `loop` est plus général : il sert quand le module ne gère pas les listes lui-même (créer plusieurs utilisateurs, par exemple). Pour les paquets, les deux marchent ; pour les utilisateurs, `loop` est nécessaire.

### ❌ Erreur classique

> **Oublier `{{ item }}` dans la tâche, ou mal indenter `loop`.**

Si tu écris `loop:` mais que tu mets une valeur en dur au lieu de `{{ item }}`, la boucle ne sert à rien. Et `loop:` doit être au **même niveau** que le module, pas dedans. Le réflexe correct : utiliser **`{{ item }}`** dans les arguments, et bien aligner `loop:`.

### Exercices

#### Guidé
Réécris l'installation de `htop`, `git` et `curl` avec une **boucle** `loop` (au lieu d'une liste dans `name`). Lance et vérifie que les trois paquets sont installés.

#### Autonome
Crée trois utilisateurs avec une boucle `loop` sur le module `user`. Vérifie avec `id` sur la cible que les trois existent.

#### Défi
Combine **boucle** et **condition** : installe une liste de paquets, mais seulement sur les machines de famille Debian (`when` + `loop`). Observe le comportement sur tes cibles.

### ✅ Tu sais maintenant…

- Répéter une tâche sur une liste avec **`loop`** et **`{{ item }}`**.
- Que `loop` évite la répétition de tâches.
- Quand `loop` est nécessaire (créer plusieurs utilisateurs) vs quand le module gère déjà les listes (paquets).

---


## Chapitre 6.6 — Afficher et diagnostiquer (`debug`)

### Le minimum à savoir

Le module **`debug`** affiche un message ou la valeur d'une variable. C'est ton outil pour **comprendre** ce qui se passe et **diagnostiquer**.

```yaml
- name: Afficher un message
  ansible.builtin.debug:
    msg: "Bonjour depuis {{ ansible_hostname }}"

- name: Afficher la valeur d'une variable
  ansible.builtin.debug:
    var: paquet_web        # affiche le contenu de la variable paquet_web
```


> Deux usages : **`msg`** pour un message libre (avec des `{{ }}` dedans), et **`var`** pour afficher directement le contenu d'une variable.

### Très utile en pratique

`debug` est précieux quand un playbook ne se comporte pas comme prévu : tu affiches la valeur d'une variable ou d'un fact pour **voir** ce qu'Ansible utilise réellement.

### Exemple simple

```yaml
- name: Vérifier une variable
  ansible.builtin.debug:
    var: ansible_distribution
```


### 🔍 Réflexe diagnostic

> Quand une condition `when` ou une variable ne se comporte pas comme tu l'attends, ajoute un **`debug`** pour **afficher** la valeur réelle. Tu verras souvent immédiatement le problème (un fait mal nommé, une variable vide, une valeur inattendue).

### ❌ Erreur classique

> **Confondre `msg` et `var`.**

`msg:` attend un **texte** (où tu peux insérer des `{{ }}`). `var:` attend un **nom de variable** (sans accolades). Écrire `var: "{{ paquet_web }}"` est redondant. Le réflexe correct : `msg` pour une phrase, `var` pour afficher une variable directement.

### Exercices

#### Guidé
Ajoute une tâche `debug` qui affiche un message personnalisé avec le nom d'hôte (`msg: "Machine : {{ ansible_hostname }}"`). Lance et observe la sortie pour chaque machine.

#### Autonome
Utilise `debug` avec `var:` pour afficher le contenu d'une variable que tu as définie (par exemple `paquet_web`). Vérifie que la valeur affichée correspond.

#### Défi
Tu as une condition `when` qui ne se déclenche pas comme prévu. Ajoute un `debug` qui affiche le fait utilisé dans la condition (par exemple `ansible_os_family`). Utilise cet affichage pour comprendre pourquoi la condition est vraie ou fausse.

### ✅ Tu sais maintenant…

- Afficher messages et variables avec **`debug`** (`msg` et `var`).
- Utiliser `debug` pour **diagnostiquer** variables, facts et conditions.
- La différence entre **`msg`** (texte) et **`var`** (nom de variable).

---

### 🚩 Checkpoint — Fin de la Partie 6

Tes playbooks sont maintenant adaptables. Avant les templates, assure-toi de pouvoir :

- [ ] Définir et utiliser des **variables** (`vars`, `group_vars`, `host_vars`) avec la bonne priorité.
- [ ] Récolter et utiliser des **facts** (`setup`, `ansible_distribution`…).
- [ ] Écrire des conditions **`when`** (et comprendre `skipped`).
- [ ] Répéter avec des boucles **`loop`** et **`{{ item }}`**.
- [ ] Afficher et diagnostiquer avec **`debug`**.

> **🧩 Mini-projet (consolidation) — « Playbook adaptable ».**
> Écris un playbook qui : installe une liste de paquets en **boucle**, mais seulement sur les machines de la bonne famille d'OS (`when` + facts), en utilisant une **variable** pour la liste (rangée dans `group_vars`). Ajoute un `debug` qui affiche, pour chaque machine, son OS et sa version. Vérifie l'idempotence sur deux passages.

> **La suite :** en Partie 7, on génère des fichiers de configuration **dynamiques** avec les **templates Jinja2**, et on apprend à redémarrer un service **uniquement si nécessaire** grâce aux **handlers**.

---
---
---
