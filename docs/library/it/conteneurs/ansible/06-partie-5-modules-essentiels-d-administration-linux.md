---
title: PARTIE 5 — MODULES ESSENTIELS D'ADMINISTRATION LINUX
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
chapter: 6
chapters: 13
---

> **Objectif de la partie :** apprendre les **modules** Ansible les plus utiles pour administrer une machine Linux : paquets, services, fichiers, permissions, utilisateurs et groupes. Ce sont tes outils du quotidien.

---


## Chapitre 5.1 — Gérer les paquets (`apt` / `dnf`)

### Le minimum à savoir

Pour installer ou retirer des logiciels, on utilise le module de paquets de la distribution : **`apt`** (Debian/Ubuntu) ou **`dnf`** (Fedora/RHEL).

```yaml
- name: Installer nginx
  ansible.builtin.apt:
    name: nginx
    state: present        # ← présent = doit être installé
  become: true
```

Les états possibles :
- `state: present` → le paquet **doit être installé**.
- `state: absent` → le paquet **ne doit pas être là** (Ansible le retire s'il est présent).
- `state: latest` → le paquet doit être à sa **dernière version**.

### Très utile en pratique

```yaml
# Installer plusieurs paquets d'un coup
- name: Installer des outils de base
  ansible.builtin.apt:
    name:
      - htop
      - git
      - curl
    state: present
    update_cache: true     # met à jour la liste des paquets avant d'installer
  become: true

# Retirer un paquet
- name: Retirer un paquet inutile
  ansible.builtin.apt:
    name: telnet
    state: absent
  become: true
```

> `update_cache: true` équivaut à un `apt update` avant l'installation : utile pour être sûr d'avoir la liste de paquets à jour.

### Exemple simple

```yaml
- name: nginx doit être installé
  ansible.builtin.apt:
    name: nginx
    state: present
  become: true
```

### 🔀 À ne pas confondre

> **`state: present` vs `state: latest`.**
> `present` = « installé » (peu importe la version, tant qu'il est là). `latest` = « à la dernière version » (Ansible mettra à jour si une version plus récente existe). Pour un débutant, `present` suffit dans la plupart des cas.

### ❌ Erreur classique

> **Utiliser `shell -a "apt install"` au lieu du module `apt`.**

Comme vu en Partie 3, `shell` n'est **pas idempotent**. Le réflexe correct : **toujours le module `apt`/`dnf`** pour les paquets. Il déclare un état, il est idempotent, et il gère les erreurs proprement.

### Exercices

#### Guidé
Écris un playbook qui installe `htop`, `git` et `curl` en une seule tâche (liste), avec `update_cache: true` et `become`. Lance-le, vérifie sur la cible (`which htop`), puis relance pour confirmer l'idempotence.

#### Autonome
Ajoute une tâche qui **retire** un paquet (`state: absent`). Lance avec `--check` d'abord pour voir ce qui se passerait, puis pour de vrai. Vérifie que le paquet a bien disparu.

#### Défi
Teste la différence entre `present` et `latest` : installe un paquet en `present`, note sa version (`apt list --installed | grep ...` via une commande ad hoc), puis change en `latest` et observe si Ansible le met à jour. Dans quel cas préférerais-tu `latest` ?

### ✅ Tu sais maintenant…

- Installer/retirer des paquets avec **`apt`** / **`dnf`**.
- Les états **`present`**, **`absent`**, **`latest`**.
- Installer **plusieurs paquets** en liste, avec `update_cache`.
- Toujours préférer le **module** à `shell` pour les paquets.

---


## Chapitre 5.2 — Gérer les services (`service`)

### Le minimum à savoir

Pour démarrer, arrêter ou activer un service, on utilise le module **`service`** :

```yaml
- name: nginx doit tourner et démarrer au boot
  ansible.builtin.service:
    name: nginx
    state: started        # tourne MAINTENANT
    enabled: true         # démarre AUTOMATIQUEMENT au boot
  become: true
```

Les options principales :
- `state: started` / `stopped` / `restarted` → l'état de marche **maintenant**.
- `enabled: true` / `false` → démarrage **automatique au boot** ou non.

### Très utile en pratique

```yaml
# Arrêter et désactiver un service inutile
- name: Désactiver un service superflu
  ansible.builtin.service:
    name: avahi-daemon
    state: stopped
    enabled: false
  become: true
```

### Exemple simple

```yaml
- name: Démarrer ssh
  ansible.builtin.service:
    name: ssh
    state: started
  become: true
```

### 🔀 À ne pas confondre

> **`state: started` (maintenant) ≠ `enabled: true` (au boot).**
> Un service peut **tourner maintenant** sans être **activé au boot** (il ne redémarrera pas après un redémarrage de la machine), et inversement. Les deux options sont **indépendantes**. Pour qu'un service soit là « tout le temps », il faut **les deux** : `started` + `enabled`.

### ❌ Erreur classique

> **Démarrer un service sans `enabled: true`, puis s'étonner qu'il ne redémarre pas après reboot.**

`state: started` lance le service **maintenant**, mais ne garantit pas qu'il redémarrera après un redémarrage de la machine. Le réflexe correct : si tu veux qu'un service soit **toujours** présent, mets **à la fois** `state: started` **et** `enabled: true`.

### Exercices

#### Guidé
Dans ton playbook nginx, ajoute (ou vérifie) une tâche `service` avec `state: started` et `enabled: true`. Lance, puis vérifie sur la cible avec une commande ad hoc (`systemctl is-active nginx`, `systemctl is-enabled nginx`).

#### Autonome
Crée une tâche qui **arrête et désactive** un service de ton choix (par exemple un service présent mais inutile sur tes cibles). Vérifie le résultat. Restaure avec un snapshot si besoin.

#### Défi
Démarre un service avec `state: started` **sans** `enabled`. Redémarre la VM (`sudo reboot` à la main ou via Ansible plus tard). Le service est-il toujours actif après le reboot ? Explique le rôle de `enabled`.

### ✅ Tu sais maintenant…

- Gérer les services avec **`service`** : `started`, `stopped`, `restarted`.
- La différence **`state` (maintenant)** vs **`enabled` (au boot)**.
- Qu'un service « toujours présent » nécessite **`started` + `enabled`**.

---


## Chapitre 5.3 — Fichiers et permissions (`copy`, `file`)

### Le minimum à savoir

Deux modules pour gérer fichiers et dossiers :

- **`copy`** : dépose un fichier (depuis la machine de contrôle) vers les cibles.
- **`file`** : gère l'**état** d'un fichier/dossier (existence, permissions, propriétaire).

```yaml
- name: Déposer un fichier de configuration
  ansible.builtin.copy:
    src: motd.txt              # fichier local (sur le contrôle)
    dest: /etc/motd            # destination sur la cible
    owner: root
    group: root
    mode: "0644"               # permissions (toujours entre guillemets)
  become: true

- name: Créer un dossier avec les bonnes permissions
  ansible.builtin.file:
    path: /opt/app
    state: directory
    owner: admin
    mode: "0750"
  become: true
```

### Très utile en pratique

Les **permissions** (`mode`) s'écrivent en notation octale, **entre guillemets** :
- `"0644"` → lecture/écriture pour le propriétaire, lecture pour les autres (fichiers courants).
- `"0600"` → lecture/écriture pour le propriétaire **seulement** (fichiers sensibles).
- `"0750"` → dossier accessible au propriétaire et au groupe, pas aux autres.

> 🛡️ **Réflexe sécurité :** mets les **bonnes permissions** sur les fichiers, surtout les sensibles. Un fichier de configuration en `"0777"` (accessible à tout le monde en écriture) est une mauvaise pratique. Ansible rend ces permissions **explicites et reproductibles** sur tout le parc.

### Exemple simple

```yaml
- name: Déposer une page d'accueil
  ansible.builtin.copy:
    src: index.html
    dest: /var/www/html/index.html
    mode: "0644"
  become: true
```

### ❌ Erreur classique

> **Oublier les guillemets autour du `mode`, ou se tromper de permissions.**

Écrire `mode: 0644` **sans** guillemets peut être mal interprété par YAML. Le réflexe correct : **toujours `mode: "0644"`** entre guillemets. Et réfléchis aux permissions : un fichier sensible (mot de passe, clé) doit être en `"0600"`, pas `"0644"`.

### Exercices

#### Guidé
Crée un petit fichier local (`motd.txt`) et déploie-le sur tes cibles dans `/etc/motd` avec `copy`, en `mode: "0644"`. Connecte-toi en SSH à une cible et vérifie le contenu et les permissions (`ls -l /etc/motd`).

#### Autonome
Crée un dossier `/opt/monapp` sur les cibles avec `file` (`state: directory`), propriétaire `root`, permissions `"0750"`. Vérifie avec `ls -ld /opt/monapp`.

#### Défi
Déploie un fichier « sensible » (par exemple un faux fichier de config avec un contenu quelconque) en `mode: "0600"`. Vérifie qu'un utilisateur non propriétaire ne peut **pas** le lire. Explique pourquoi les permissions comptent pour la sécurité.

### ✅ Tu sais maintenant…

- Déposer un fichier avec **`copy`** (avec `owner`, `group`, `mode`).
- Gérer fichiers/dossiers et permissions avec **`file`**.
- Écrire le **`mode`** entre guillemets (notation octale).
- Que les **bonnes permissions** sont une base de sécurité.

---


## Chapitre 5.4 — Modifier une ligne (`lineinfile`)

### Le minimum à savoir

Parfois, tu ne veux pas remplacer **tout** un fichier, juste **t'assurer qu'une ligne précise** y figure (ou la modifier). C'est le rôle de **`lineinfile`** :

```yaml
- name: S'assurer que la connexion root SSH est désactivée
  ansible.builtin.lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^#?PermitRootLogin'        # cherche cette ligne (existante ou commentée)
    line: 'PermitRootLogin no'          # et la remplace par celle-ci
  become: true
```

- `path` : le fichier à modifier.
- `regexp` : le motif de la ligne à chercher.
- `line` : la ligne voulue (ajoutée si absente, corrigée si différente).

### Très utile en pratique

`lineinfile` est **idempotent** : si la ligne voulue est déjà là, il ne fait rien (`ok`). S'il faut la modifier ou l'ajouter, il agit (`changed`). C'est parfait pour ajuster des fichiers de configuration existants.

### Exemple simple

```yaml
- name: Ajouter une ligne d'information dans un fichier
  ansible.builtin.lineinfile:
    path: /etc/motd
    line: "Machine administrée par Ansible"
  become: true
```

### 🔀 À ne pas confondre

> **`lineinfile` (une ligne) vs `template`/`copy` (tout le fichier).**
> `lineinfile` ajuste **une ligne** dans un fichier existant. Si tu dois **générer tout** un fichier de config, ce sera plutôt `template` (Partie 7) ou `copy`. Choisis selon que tu modifies **un détail** ou **tout** le fichier.

### ❌ Erreur classique

> **Utiliser `lineinfile` pour réécrire tout un fichier ligne par ligne.**

Si tu te retrouves avec dix tâches `lineinfile` pour le même fichier, c'est le signe qu'il faut plutôt un **template** (Partie 7). Le réflexe correct : `lineinfile` pour **un ou deux ajustements** ; template pour **générer** un fichier entier.

### Exercices

#### Guidé
Avec `lineinfile`, assure-toi que `/etc/ssh/sshd_config` contient `PermitRootLogin no`. Lance avec `--check --diff` d'abord pour **voir** le changement, puis applique. (On verra `--diff` en Partie 8 ; il montre la ligne modifiée.)

#### Autonome
Ajoute une ligne d'information dans `/etc/motd` avec `lineinfile`. Relance le playbook : la ligne ne doit **pas** être ajoutée une seconde fois (idempotence). Vérifie sur la cible.

#### Défi
Modifie une option de configuration existante (par exemple un paramètre dans un fichier de ton choix) avec `regexp` + `line`. Vérifie qu'au second passage, Ansible affiche `ok` (la ligne est déjà conforme). Explique le rôle du `regexp`.

### ✅ Tu sais maintenant…

- Ajuster **une ligne** d'un fichier avec **`lineinfile`** (`path`, `regexp`, `line`).
- Que `lineinfile` est **idempotent**.
- Quand préférer `lineinfile` (un détail) vs `template`/`copy` (tout le fichier).

---


## Chapitre 5.5 — Utilisateurs et groupes (`user`, `group`)

### Le minimum à savoir

Pour gérer les comptes, deux modules : **`group`** (les groupes) et **`user`** (les utilisateurs).

```yaml
- name: Créer un groupe
  ansible.builtin.group:
    name: developpeurs
    state: present
  become: true

- name: Créer un utilisateur
  ansible.builtin.user:
    name: alice
    groups: developpeurs      # groupe secondaire
    shell: /bin/bash
    state: present
  become: true
```

- `state: present` → le compte/groupe **doit exister**.
- `state: absent` → il **ne doit pas exister** (Ansible le supprime).

### Très utile en pratique

```yaml
# Créer un utilisateur avec un dossier personnel et un shell
- name: Créer un utilisateur admin
  ansible.builtin.user:
    name: bob
    groups: sudo              # l'ajoute au groupe sudo
    shell: /bin/bash
    create_home: true
    state: present
  become: true
```

> 🛡️ **Réflexe sécurité :** gérer les comptes **par Ansible** rend la gestion des accès **centralisée et reproductible**. Créer ou retirer un utilisateur sur tout le parc devient une opération propre, plutôt que des `useradd` éparpillés à la main.

### Exemple simple

```yaml
- name: L'utilisateur alice doit exister
  ansible.builtin.user:
    name: alice
    state: present
  become: true
```

### ❌ Erreur classique

> **Oublier que `state: present` maintient le compte à chaque exécution.**

Si tu déclares `state: present` pour un utilisateur et que quelqu'un le supprime à la main, le prochain run le **recrée** (correction de dérive). C'est voulu, mais il faut le savoir. Le réflexe correct : décider explicitement l'état (`present` ou `absent`) et comprendre qu'Ansible **maintient** cet état à chaque passage.

### Exercices

#### Guidé
Écris un playbook qui crée un groupe `developpeurs` et un utilisateur `alice` membre de ce groupe, avec le shell `/bin/bash`. Lance-le, vérifie sur la cible (`id alice`), puis relance pour confirmer l'idempotence.

#### Autonome
Ajoute un utilisateur `bob` dans le groupe `sudo` avec un dossier personnel. Vérifie qu'il peut (en théorie) utiliser sudo. Puis crée une tâche qui **supprime** un utilisateur (`state: absent`) et teste-la sur un compte de test.

#### Défi
Crée un utilisateur, supprime-le **à la main** sur une cible (`sudo userdel ...`), puis relance le playbook. Observe qu'Ansible le **recrée**. Explique en quoi ce comportement illustre la logique d'**état souhaité** et la correction de dérive.

### ✅ Tu sais maintenant…

- Gérer les **groupes** (`group`) et **utilisateurs** (`user`).
- Les options utiles : `groups`, `shell`, `create_home`, `state`.
- Que la gestion centralisée des comptes est **propre et reproductible**.
- Qu'Ansible **maintient** l'état des comptes à chaque passage.

---

### 🚩 Checkpoint — Fin de la Partie 5

Tu sais maintenant administrer une machine Linux avec Ansible. Avant de rendre tes playbooks adaptables, assure-toi de pouvoir :

- [ ] Gérer les **paquets** (`apt`/`dnf`) : présent, absent, latest, en liste.
- [ ] Gérer les **services** (`service`) : `started` vs `enabled`.
- [ ] Déposer des fichiers et gérer les **permissions** (`copy`, `file`, `mode`).
- [ ] Ajuster **une ligne** d'un fichier (`lineinfile`).
- [ ] Gérer **utilisateurs et groupes** (`user`, `group`).

> **🧩 Mini-projet 6 — « Copier un fichier sur plusieurs machines ».**
> Crée un fichier local et déploie-le sur le groupe `web` avec `copy`, en gérant propriétaire et permissions. Vérifie sur chaque cible.
>
> **🧩 Mini-projet 7 — « Créer un utilisateur sur plusieurs machines ».**
> Écris un playbook qui crée un groupe et un utilisateur (membre du groupe, avec un shell) sur tout le groupe `web`. Vérifie avec `id` sur chaque cible. Confirme l'idempotence.

> **La suite :** en Partie 6, on rend les playbooks **adaptables** : variables, facts (ce qu'Ansible sait des machines), conditions `when` et boucles `loop`. Un playbook qui s'ajuste à chaque machine.

---
---
