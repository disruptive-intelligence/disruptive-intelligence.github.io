---
title: Chapitre 2.4 — command et shell
source: IT/08 Conteneurs & automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 2 — Inventaire et premières commandes
  - index.md
---

## Le minimum à savoir

Ansible propose deux modules pour lancer une commande « brute » sur les cibles :

- **`ansible.builtin.command`** : exécute une commande **simple**, sans passer par un shell complet.
- **`ansible.builtin.shell`** : exécute une commande **via un shell**, ce qui permet les `|`, `>`, `&&`, etc.

```bash
# command : commande simple
ansible web -i inventory.ini -m ansible.builtin.command -a "hostname"

# shell : nécessaire pour les redirections, pipes, etc.
ansible web -i inventory.ini -m ansible.builtin.shell -a "cat /etc/os-release | grep PRETTY"
```


> **Règle simple :** utilise **`command`** par défaut. Passe à **`shell`** seulement si tu as besoin des fonctionnalités du shell (pipes `|`, redirections `>`, `&&`). `shell` est un peu plus puissant, mais aussi un peu moins sûr (il interprète tout).

## Très utile en pratique

```bash
# command suffit pour une commande simple
ansible all -i inventory.ini -m ansible.builtin.command -a "whoami"

# shell est nécessaire ici (à cause du pipe)
ansible all -i inventory.ini -m ansible.builtin.shell -a "ps aux | grep ssh"
```


## Exemple simple

```bash
# "Quelle est la version de l'OS sur chaque machine ?"
ansible all -i inventory.ini -m ansible.builtin.shell -a "cat /etc/os-release | grep PRETTY_NAME"
```


(On utilise `shell` ici à cause du `|`.)

## 🔀 À ne pas confondre

> **`command` (simple) vs `shell` (avec shell).**
> `command` ne comprend **pas** les `|`, `>`, `&&` — si tu en as besoin, il faut `shell`. Inversement, pour une commande simple, **préfère `command`** : c'est plus prévisible.

## ❌ Erreur classique

> **Tout faire en `command`/`shell`, même quand un module dédié existe.**

On pourrait être tenté de tout faire avec `shell` : `shell -a "apt install htop"`, `shell -a "systemctl start nginx"`. Mais c'est une **mauvaise habitude** : ces commandes ne sont **pas idempotentes** (relancer relance l'action) et contournent toute l'intelligence d'Ansible. Le réflexe correct : pour installer un paquet, gérer un service, copier un fichier… **utilise le module dédié** (qu'on verra en Partie 5). Garde `command`/`shell` pour ce qui n'a **pas** de module dédié. On comprendra **pourquoi** en détail dès la Partie 3.

## Exercices

### Guidé
Lance une commande simple avec `command` (par exemple `hostname` ou `whoami`) sur tout le parc. Observe la sortie pour chaque machine.

### Autonome
Essaie de lancer une commande avec un **pipe** (`|`) en utilisant `command`. Observe que ça échoue ou se comporte mal. Refais-la avec `shell`. Tu comprends ainsi quand `shell` est nécessaire.

### Défi
Sans encore connaître les modules dédiés, réfléchis : pourquoi `shell -a "apt install htop"` est-il une **mauvaise idée** comparé à un futur module `apt` ? (Indice : que se passe-t-il si on le relance alors que htop est déjà installé ?)

## ✅ Tu sais maintenant…

- La différence entre **`command`** (commande simple) et **`shell`** (avec pipes/redirections).
- Préférer **`command`** par défaut, **`shell`** seulement si nécessaire.
- Que `command`/`shell` ne sont **pas idempotents** et qu'il faut leur préférer les **modules dédiés** quand ils existent.

---
