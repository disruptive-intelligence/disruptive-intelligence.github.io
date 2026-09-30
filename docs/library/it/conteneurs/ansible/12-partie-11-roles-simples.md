---
title: PARTIE 11 — ROLES SIMPLES
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
chapter: 12
chapters: 13
---

> **Objectif de la partie :** comprendre pourquoi et comment créer un **role** basique, pour organiser et réutiliser ton code. On reste simple : juste l'essentiel.

---


## Chapitre 11.1 — Pourquoi les roles existent

### Le minimum à savoir

À force d'ajouter des tâches, un playbook devient **long et difficile à relire**. Et tu te retrouves à **copier-coller** les mêmes tâches d'un projet à l'autre. Les **roles** résolvent ça : ils **regroupent et réutilisent** le code.

> **Un role**, c'est un ensemble cohérent de tâches, templates, variables et handlers, **rangés** dans une structure standard, qu'on peut **réutiliser** dans n'importe quel playbook. Par exemple, un role `common` qui installe les paquets de base et applique la config commune à toutes tes machines.

### Très utile en pratique

L'intérêt des roles :
- **Organiser** : un gros playbook devient un role bien rangé.
- **Réutiliser** : le même role s'applique dans plusieurs projets.
- **Partager** : un role est facile à donner à un collègue.

### Exemple simple

Sans role, ton playbook contient 20 tâches en vrac. Avec un role `common`, ton playbook devient :

```yaml
- name: Configuration de base
  hosts: all
  become: true
  roles:
    - common          # tout le contenu du role en une ligne
```

Limpide, non ?

### ❌ Erreur classique

> **Vouloir créer des roles trop tôt, pour tout.**

Un débutant qui découvre les roles veut tout transformer en role immédiatement. C'est prématuré. Le réflexe correct : crée un role **quand un playbook devient gros** ou **quand tu veux réutiliser** du code. Pas avant. Un petit playbook simple n'a pas besoin d'être un role.

### Exercices

#### Guidé
Regarde tes playbooks actuels. Lequel est devenu **assez gros** pour justifier un role ? Lequel est encore **trop simple** pour ça ? Justifie.

#### Autonome
Liste trois choses que tu refais **souvent** d'un playbook à l'autre (installer des paquets de base, créer un utilisateur admin, durcir SSH…). Ce sont de bons candidats pour un role réutilisable.

#### Défi
Explique en quelques lignes la différence entre **réutiliser** un role et **copier-coller** des tâches. Pourquoi le role est-il une meilleure approche à long terme ?

### ✅ Tu sais maintenant…

- Pourquoi les **roles** existent : organiser et réutiliser le code.
- Qu'un role regroupe tâches, templates, variables et handlers.
- Qu'on appelle un role en **une ligne** dans un playbook.
- Qu'il ne faut créer des roles **ni trop tôt, ni pour tout**.

---


## Chapitre 11.2 — La structure d'un role

### Le minimum à savoir

Un role suit une **structure standard** de dossiers. Ansible sait où chercher chaque chose :

```
roles/
└── common/
    ├── tasks/main.yml          # les tâches du role (le cœur)
    ├── handlers/main.yml       # les handlers
    ├── templates/              # les templates Jinja2
    ├── files/                  # les fichiers à copier
    └── defaults/main.yml       # les variables par défaut
```

> **Les dossiers clés :**
> - **`tasks/main.yml`** : les tâches (obligatoire en pratique).
> - **`handlers/main.yml`** : les handlers.
> - **`templates/`** : les `.j2`.
> - **`files/`** : les fichiers pour `copy`.
> - **`defaults/main.yml`** : les variables par défaut (faciles à surcharger).

On crée cette structure automatiquement :

```bash
ansible-galaxy role init roles/common
```

*(`ansible-galaxy` sert ici juste à créer la structure — on n'utilise pas le côté « téléchargement de roles » dans ce cours.)*

### Très utile en pratique

Dans un role, tu n'écris plus les chemins complets : Ansible cherche **automatiquement** les templates dans `templates/`, les fichiers dans `files/`, etc. C'est l'avantage de la structure standard.

```yaml
# roles/common/tasks/main.yml
- name: Installer les paquets de base
  ansible.builtin.apt:
    name:
      - htop
      - git
      - curl
    state: present
```

### Exemple simple

```yaml
# roles/common/tasks/main.yml
- name: Déposer le message du jour
  ansible.builtin.template:
    src: motd.j2            # cherché automatiquement dans roles/common/templates/
    dest: /etc/motd
```

### 🔀 À ne pas confondre

> **Un role n'est pas magique.** C'est juste tes tâches, templates et variables **rangés** dans des dossiers que Ansible connaît. Tu sais déjà écrire tout ce qu'il y a dedans — le role, c'est de **l'organisation**, pas une nouvelle compétence.

### ❌ Erreur classique

> **Se tromper de dossier ou de nom de fichier (`main.yml`).**

Les tâches vont dans `tasks/main.yml`, les handlers dans `handlers/main.yml` — avec ce **nom précis**. Une erreur de dossier ou de nom, et Ansible ne trouve rien. Le réflexe correct : utiliser `ansible-galaxy role init` pour créer la structure correcte, et respecter les noms `main.yml`.

### Exercices

#### Guidé
Crée la structure d'un role avec `ansible-galaxy role init roles/common`. Explore les dossiers créés. Mets une tâche simple (installer un paquet) dans `roles/common/tasks/main.yml`.

#### Autonome
Ajoute un template dans `roles/common/templates/` et une tâche dans `tasks/main.yml` qui l'utilise (sans chemin complet, juste le nom du fichier). Vérifie qu'Ansible le trouve automatiquement.

#### Défi
Ajoute un handler dans `roles/common/handlers/main.yml` et notifie-le depuis une tâche du role. Vérifie que le mécanisme `notify` fonctionne **dans** le role comme dans un playbook normal.

### ✅ Tu sais maintenant…

- La **structure standard** d'un role (`tasks/`, `handlers/`, `templates/`, `files/`, `defaults/`).
- Créer un role avec **`ansible-galaxy role init`**.
- Qu'Ansible cherche **automatiquement** templates et fichiers dans les bons dossiers.
- Qu'un role, c'est de l'**organisation**, pas une nouvelle compétence.

---


## Chapitre 11.3 — Créer et utiliser un role simple

### Le minimum à savoir

Voici le cycle complet : transformer un playbook en role, puis l'utiliser.

**1. Le contenu du role** (`roles/common/tasks/main.yml`) :
```yaml
- name: Installer les paquets de base
  ansible.builtin.apt:
    name:
      - htop
      - git
      - curl
    state: present

- name: Déposer le message du jour
  ansible.builtin.template:
    src: motd.j2
    dest: /etc/motd
```

**2. Le playbook qui appelle le role** (`playbooks/site.yml`) :
```yaml
- name: Configuration de base de toutes les machines
  hosts: all
  become: true
  roles:
    - common
```

**3. Lancer :**
```bash
ansible-playbook -i inventory.ini playbooks/site.yml
```

> Le playbook devient **court et clair** : il dit juste « applique le role `common` à toutes les machines ». Tout le détail est **rangé** dans le role.

### Très utile en pratique

Les **variables par défaut** du role vont dans `defaults/main.yml`. On peut les **surcharger** depuis le playbook ou les `group_vars`, ce qui rend le role **paramétrable** :

```yaml
# roles/common/defaults/main.yml
paquets_base:
  - htop
  - git
```

```yaml
# roles/common/tasks/main.yml
- name: Installer les paquets de base
  ansible.builtin.apt:
    name: "{{ paquets_base }}"
    state: present
```

### Exemple simple

```yaml
# playbooks/site.yml
- hosts: all
  become: true
  roles:
    - common
```

Trois lignes, et tout le role s'applique.

### ❌ Erreur classique

> **Mettre des valeurs en dur dans le role au lieu d'utiliser `defaults`.**

Un role avec des valeurs codées en dur n'est **pas réutilisable** : il fait toujours exactement la même chose. Le réflexe correct : mettre les valeurs configurables dans **`defaults/main.yml`** et les utiliser via `{{ }}`. Ainsi, le même role s'adapte à différents besoins.

### Exercices

#### Guidé
Transforme ton playbook de configuration de base en role `common` : déplace les tâches dans `tasks/main.yml`, les templates dans `templates/`. Crée un playbook court qui appelle le role. Vérifie que tout fonctionne comme avant.

#### Autonome
Mets la liste des paquets dans `defaults/main.yml` (variable `paquets_base`) et utilise-la dans le role via `{{ paquets_base }}`. Surcharge cette liste depuis un `group_vars` pour un groupe précis. Observe le résultat.

#### Défi
Crée un second playbook (pour un autre groupe) qui réutilise le **même** role `common`. Tu prouves ainsi la **réutilisabilité** : un seul role, plusieurs usages. Explique l'économie de code réalisée.

### ✅ Tu sais maintenant…

- Transformer un playbook en **role** et l'appeler avec `roles:`.
- Que le playbook devient **court** (le détail est dans le role).
- Rendre un role **paramétrable** avec **`defaults/main.yml`**.
- **Réutiliser** un role dans plusieurs playbooks.

---

### 🚩 Checkpoint — Fin de la Partie 11

Tu sais créer et utiliser un role simple. Avant les mini-projets finaux, assure-toi de pouvoir :

- [ ] Expliquer **pourquoi** les roles existent (organiser, réutiliser).
- [ ] Connaître la **structure** d'un role (`tasks/`, `handlers/`, `templates/`, `files/`, `defaults/`).
- [ ] Créer un role avec **`ansible-galaxy role init`**.
- [ ] Appeler un role depuis un playbook (`roles:`) et le rendre paramétrable (`defaults`).

> **🧩 Mini-projet 12 — « Créer un role simple `common` ».**
> Crée un role `common` qui installe les paquets de base, dépose un `motd` par template, et applique une petite config commune. Rends-le paramétrable via `defaults`. Appelle-le depuis un playbook court qui vise toutes les machines. Vérifie l'idempotence.

> **La suite :** la Partie 12 regroupe **tous** les mini-projets en un parcours complet, pour consolider l'ensemble du cours.

---
---
