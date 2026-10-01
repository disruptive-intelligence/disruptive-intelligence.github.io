---
title: Chapitre 2.1 — L'inventaire INI
source: IT/08 Conteneurs & automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 2 — Inventaire et premières commandes
  - index.md
---

## Le minimum à savoir

Avant d'agir sur des machines, Ansible doit **savoir lesquelles existent**. C'est le rôle de l'**inventaire** : un fichier qui **liste** tes machines et les **organise en groupes**.

Le format le plus simple pour débuter est le format **INI** :

```ini
# inventory.ini

[web]
cible1 ansible_host=192.168.56.11
cible2 ansible_host=192.168.56.12

[db]
cible3 ansible_host=192.168.56.13
```


- `[web]` et `[db]` sont des **groupes**.
- `cible1`, `cible2`, `cible3` sont des **hôtes** (les machines).
- `ansible_host=...` indique l'**adresse IP** réelle de connexion.

> **L'inventaire est la base de tout.** Toutes tes commandes et tous tes playbooks viseront un **hôte** ou un **groupe** défini ici. Un inventaire clair, c'est la moitié du travail.

### Le groupe `all`

Toutes les machines de l'inventaire appartiennent automatiquement à un groupe spécial : **`all`**. Cibler `all`, c'est cibler **toutes** les machines d'un coup.

> 💡 **Mention pour plus tard :** au début, on précise l'inventaire à chaque commande avec `-i inventory.ini`. C'est un peu répétitif. En **Partie 10**, on verra qu'un petit fichier `ansible.cfg` permet d'**éviter** de retaper `-i` à chaque fois. Pour l'instant, on garde le `-i` : c'est plus explicite pour comprendre.

## Très utile en pratique

```bash
# Visualiser l'inventaire tel qu'Ansible le comprend (vue en arbre)
ansible-inventory -i inventory.ini --graph
```


```text
@all:
  |--@web:
  |  |--cible1
  |  |--cible2
  |--@db:
  |  |--cible3
```


Cette vue `--graph` est ton **réflexe de vérification** : avant d'agir, tu regardes **qui est dans quel groupe**. C'est la meilleure protection contre l'erreur de cible.

## Exemple simple

Un inventaire minimal pour le lab du cours :

```ini
[web]
cible1 ansible_host=192.168.56.11
cible2 ansible_host=192.168.56.12
```


Deux machines, un groupe `web`. C'est suffisant pour commencer.

## ❌ Erreur classique

> **Se tromper d'IP ou mettre un hôte dans le mauvais groupe.**

Une IP erronée dans `ansible_host`, et Ansible n'arrive pas à joindre la machine (ou en joint une autre !). Un hôte dans le mauvais groupe, et ta commande touche la mauvaise cible. Le réflexe correct : **vérifier l'inventaire avec `ansible-inventory --graph`** avant d'agir, et confirmer les IP avec un `ssh` à la main en cas de doute.

## Exercices

### Guidé
Crée un fichier `inventory.ini` décrivant tes deux cibles dans un groupe `web`, avec leurs vraies IP. Lance `ansible-inventory -i inventory.ini --graph` et vérifie que l'arbre correspond à ce que tu attendais.

### Autonome
Ajoute un groupe `db` avec une troisième machine (réelle ou fictive). Relance `--graph` et observe la nouvelle structure. Un hôte peut-il être dans plusieurs groupes ? Teste en mettant `cible1` à la fois dans `web` et dans un nouveau groupe `pilote`.

### Défi
Sans encore l'utiliser, ajoute une **variable de groupe** dans ton inventaire :

```ini
[web:vars]
http_port=80
```

Relance `ansible-inventory -i inventory.ini --graph --vars` (ou `--list`) et retrouve cette variable dans la sortie. On s'en servira au chapitre suivant.

## ✅ Tu sais maintenant…

- Que l'**inventaire** liste tes machines et les organise en **groupes**.
- Écrire un inventaire au format **INI** (hôtes, groupes, `ansible_host`).
- Que le groupe **`all`** désigne toutes les machines.
- Vérifier ton inventaire avec **`ansible-inventory --graph`**.
- Qu'on précise l'inventaire avec **`-i`** (et qu'`ansible.cfg` simplifiera ça plus tard).

---
