---
title: Chapitre 11.2 — La structure d'un role
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 11 — Roles simples
  - index.md
---

## Le minimum à savoir

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

## Très utile en pratique

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


## Exemple simple

```yaml
# roles/common/tasks/main.yml
- name: Déposer le message du jour
  ansible.builtin.template:
    src: motd.j2            # cherché automatiquement dans roles/common/templates/
    dest: /etc/motd
```


## 🔀 À ne pas confondre

> **Un role n'est pas magique.** C'est juste tes tâches, templates et variables **rangés** dans des dossiers que Ansible connaît. Tu sais déjà écrire tout ce qu'il y a dedans — le role, c'est de **l'organisation**, pas une nouvelle compétence.

## ❌ Erreur classique

> **Se tromper de dossier ou de nom de fichier (`main.yml`).**

Les tâches vont dans `tasks/main.yml`, les handlers dans `handlers/main.yml` — avec ce **nom précis**. Une erreur de dossier ou de nom, et Ansible ne trouve rien. Le réflexe correct : utiliser `ansible-galaxy role init` pour créer la structure correcte, et respecter les noms `main.yml`.

## Exercices

### Guidé
Crée la structure d'un role avec `ansible-galaxy role init roles/common`. Explore les dossiers créés. Mets une tâche simple (installer un paquet) dans `roles/common/tasks/main.yml`.

### Autonome
Ajoute un template dans `roles/common/templates/` et une tâche dans `tasks/main.yml` qui l'utilise (sans chemin complet, juste le nom du fichier). Vérifie qu'Ansible le trouve automatiquement.

### Défi
Ajoute un handler dans `roles/common/handlers/main.yml` et notifie-le depuis une tâche du role. Vérifie que le mécanisme `notify` fonctionne **dans** le role comme dans un playbook normal.

## ✅ Tu sais maintenant…

- La **structure standard** d'un role (`tasks/`, `handlers/`, `templates/`, `files/`, `defaults/`).
- Créer un role avec **`ansible-galaxy role init`**.
- Qu'Ansible cherche **automatiquement** templates et fichiers dans les bons dossiers.
- Qu'un role, c'est de l'**organisation**, pas une nouvelle compétence.

---
