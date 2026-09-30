---
title: Chapitre 11.3 — Créer et utiliser un role simple
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 11 — Roles simples
  - index.md
---

## Le minimum à savoir

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

## Très utile en pratique

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


## Exemple simple

```yaml
# playbooks/site.yml
- hosts: all
  become: true
  roles:
    - common
```


Trois lignes, et tout le role s'applique.

## ❌ Erreur classique

> **Mettre des valeurs en dur dans le role au lieu d'utiliser `defaults`.**

Un role avec des valeurs codées en dur n'est **pas réutilisable** : il fait toujours exactement la même chose. Le réflexe correct : mettre les valeurs configurables dans **`defaults/main.yml`** et les utiliser via `{{ }}`. Ainsi, le même role s'adapte à différents besoins.

## Exercices

### Guidé
Transforme ton playbook de configuration de base en role `common` : déplace les tâches dans `tasks/main.yml`, les templates dans `templates/`. Crée un playbook court qui appelle le role. Vérifie que tout fonctionne comme avant.

### Autonome
Mets la liste des paquets dans `defaults/main.yml` (variable `paquets_base`) et utilise-la dans le role via `{{ paquets_base }}`. Surcharge cette liste depuis un `group_vars` pour un groupe précis. Observe le résultat.

### Défi
Crée un second playbook (pour un autre groupe) qui réutilise le **même** role `common`. Tu prouves ainsi la **réutilisabilité** : un seul role, plusieurs usages. Explique l'économie de code réalisée.

## ✅ Tu sais maintenant…

- Transformer un playbook en **role** et l'appeler avec `roles:`.
- Que le playbook devient **court** (le détail est dans le role).
- Rendre un role **paramétrable** avec **`defaults/main.yml`**.
- **Réutiliser** un role dans plusieurs playbooks.

---

## 🚩 Checkpoint — Fin de la Partie 11

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
