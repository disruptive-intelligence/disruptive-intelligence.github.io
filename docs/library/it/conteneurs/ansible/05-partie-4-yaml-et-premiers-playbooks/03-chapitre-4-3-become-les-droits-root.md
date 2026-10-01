---
title: 'Chapitre 4.3 — become : les droits root'
source: IT/08 Conteneurs & automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 4 — YAML et premiers playbooks
  - index.md
---

## Le minimum à savoir

Beaucoup d'actions d'administration (installer un paquet, modifier un fichier système, gérer un service) nécessitent les droits **root**. En Ansible, on les obtient avec **`become`** :

```yaml
- name: Installer un paquet (nécessite root)
  hosts: web
  become: true          # ← devient root (via sudo) pour les tâches de ce play
  tasks:
    - name: Installer nginx
      ansible.builtin.apt:
        name: nginx
        state: present
```


> **Rappel (Partie 1) :** se **connecter** (avec ton utilisateur SSH, souvent non-root) et **devenir root** (`become`) sont deux étapes distinctes. La bonne pratique : se connecter en utilisateur normal, et n'élever les droits **que** quand c'est nécessaire.

`become` peut se mettre au niveau du **play** (toutes les tâches) ou d'une **tâche précise** (seulement celle-là).

## Très utile en pratique

```yaml
- name: Play mixte
  hosts: web
  tasks:
    - name: Voir qui je suis (pas besoin de root)
      ansible.builtin.command: whoami

    - name: Installer un paquet (besoin de root)
      ansible.builtin.apt:
        name: htop
        state: present
      become: true          # ← root UNIQUEMENT pour cette tâche
```


## Exemple simple

Sans `become`, une installation de paquet échoue (« permission refusée ») :

```text
FAILED! => "msg": "... Permission denied ..."
```


Avec `become: true`, elle réussit. C'est le signe qu'il fallait les droits root.

## 🛡️ Réflexe sécurité

> N'active `become` que **là où c'est nécessaire**. Donner les droits root « par confort » à des tâches qui n'en ont pas besoin est une mauvaise habitude. Élève les privilèges **au cas par cas**, pour les seules tâches qui le requièrent.

## ❌ Erreur classique

> **Oublier `become` sur une tâche qui nécessite root, et conclure qu'« Ansible ne marche pas ».**

Une installation de paquet sans `become` échoue avec « Permission denied », et le débutant croit à un bug. Le réflexe correct : si une tâche d'administration système échoue pour des raisons de **permission**, il manque probablement **`become: true`**. Lis le message d'erreur : « permission denied » est un indice clair.

## Exercices

### Guidé
Écris un playbook qui installe `htop` **sans** `become`. Lance-le : il échoue probablement avec une erreur de permission. Ajoute `become: true` et relance : il réussit. Tu comprends à quoi sert `become`.

### Autonome
Crée un playbook avec deux tâches : une qui ne nécessite pas root (`whoami`) et une qui le nécessite (installer un paquet). Mets `become` **uniquement** sur la seconde. Vérifie que tout fonctionne.

### Défi
Lance une tâche `ansible.builtin.command: whoami` **avec** puis **sans** `become: true`, et compare la sortie (le `debug` ou le retour de la commande). Que t'apprend la différence sur ce que fait réellement `become` ?

## ✅ Tu sais maintenant…

- Que **`become: true`** donne les droits **root** sur la cible.
- Que se **connecter** et **devenir root** sont deux étapes distinctes.
- Mettre `become` au niveau du **play** ou d'une **tâche** précise.
- Qu'une erreur de **permission** signale souvent un `become` manquant.

---
