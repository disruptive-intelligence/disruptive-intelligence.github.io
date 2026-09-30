---
title: 'Chapitre 2.5 — Lire les sorties : ok, changed, failed, skipped, unreachable'
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 2 — Inventaire et premières commandes
  - index.md
---

## Le minimum à savoir

Savoir **lire ce qu'Ansible répond** est un réflexe indispensable. Chaque action, sur chaque machine, se termine dans l'un de ces **cinq états** :

| Statut | Signification |
|--------|---------------|
| **`ok`** | La machine était **déjà** dans l'état voulu : rien à faire |
| **`changed`** | Ansible a **modifié** quelque chose pour atteindre l'état voulu |
| **`failed`** | L'action a **échoué** sur cette machine |
| **`skipped`** | L'action a été **ignorée** (à cause d'une condition — on verra ça en Partie 6) |
| **`unreachable`** | Ansible **n'a pas pu joindre** la machine (problème SSH/réseau) |

> **Apprends ces cinq mots maintenant.** Ils sont ta boussole pour tout le reste du cours. La distinction la plus importante est **`ok` vs `changed`** : on l'approfondit dans la partie suivante (l'idempotence).

### Commande ad hoc vs playbook

Une **commande ad hoc** agit une fois, en ligne de commande. Un **playbook** (Partie 4) est un fichier réutilisable qui décrit plusieurs actions. Mais dans les **deux** cas, tu liras ces **mêmes** statuts.

## Très utile en pratique

Avec une commande ad hoc, le statut apparaît au début de la réponse de chaque machine :

```text
cible1 | SUCCESS => { ... }          ← tout va bien (équivaut à ok)
cible2 | CHANGED => { ... }          ← Ansible a modifié quelque chose
cible3 | UNREACHABLE! => { ... }     ← machine injoignable (SSH/réseau)
cible4 | FAILED! => { ... }          ← l'action a échoué
```


## Exemple simple

```bash
ansible all -i inventory.ini -m ansible.builtin.ping
```

```text
cible1 | SUCCESS => {"ping": "pong"}      ← ok : la machine répond
cible2 | UNREACHABLE! => {...}            ← problème SSH : à diagnostiquer
```


Ici, tu vois immédiatement que `cible2` a un souci de connexion, et que `cible1` va bien.

## 🔍 Réflexe diagnostic

> Devant une exécution, **lis les statuts d'abord** :
> - `unreachable` → problème **SSH/réseau** (teste `ssh` à la main).
> - `failed` → l'action a échoué (lis le **message d'erreur** affiché).
> - `changed` partout alors que tu rejoues → quelque chose n'est pas idempotent (Partie 3).
> - `skipped` → une condition a ignoré l'action (Partie 6).

## ❌ Erreur classique

> **Ne pas lire les statuts et croire que « ça a marché » parce qu'il n'y a pas eu d'erreur évidente.**

Un débutant lance une commande, ne voit pas de message rouge, et passe à la suite — sans vérifier. Or `unreachable` sur une machine signifie qu'elle n'a **rien** reçu, et tu pourrais ne pas t'en rendre compte. Le réflexe correct : **toujours regarder le statut de chaque machine**. Une absence d'erreur évidente n'est pas une preuve que tout s'est bien passé partout.

## Exercices

### Guidé
Lance un `ping` sur tout le parc et identifie le statut de **chaque** machine. Tout doit être `SUCCESS`. Note ce que tu vois.

### Autonome
Provoque un `unreachable` : éteins une cible (ou coupe son réseau) et relance le `ping`. Observe `UNREACHABLE` sur cette machine et `SUCCESS` sur l'autre. Rallume la cible et confirme le retour à `SUCCESS`.

### Défi
Provoque un `failed` : lance une commande qui échoue, par exemple `ansible all -i inventory.ini -m ansible.builtin.command -a "ls /dossier_qui_nexiste_pas"`. Lis le message d'erreur. En quoi `failed` (l'action a échoué) est-il **différent** de `unreachable` (la machine n'a pas été jointe) ?

## ✅ Tu sais maintenant…

- Lire les **cinq statuts** : `ok`, `changed`, `failed`, `skipped`, `unreachable`.
- Que la distinction reine est **`ok` vs `changed`** (approfondie en Partie 3).
- Que ces statuts sont les **mêmes** en ad hoc et en playbook.
- Le réflexe : **lire les statuts** pour diagnostiquer (`unreachable` = SSH, `failed` = erreur d'action).

---

## 🚩 Checkpoint — Fin de la Partie 2

Ansible **agit** maintenant sur ton parc. Avant de plonger dans l'idempotence, assure-toi de pouvoir :

- [ ] Écrire un **inventaire INI** avec des groupes et des variables simples.
- [ ] Vérifier ton inventaire avec **`ansible-inventory --graph`** et **`--host`**.
- [ ] Lancer un **`ping`** et des commandes ad hoc (`command`, `shell`).
- [ ] Savoir quand utiliser **`command`** vs **`shell`**.
- [ ] Lire les **cinq statuts** (`ok`, `changed`, `failed`, `skipped`, `unreachable`).
- [ ] Diagnostiquer un **`unreachable`** (côté SSH).

> **🧩 Mini-projet 2 — « Inventaire propre + état des lieux ».**
> 1. Écris un `inventory.ini` avec un groupe `web` (tes deux cibles) et une variable de groupe `ansible_user`.
> 2. Vérifie-le avec `ansible-inventory --graph` et `--host`.
> 3. Pingue tout le parc.
> 4. Avec des commandes ad hoc en lecture, collecte l'uptime et l'espace disque de chaque machine.
> Objectif : enchaîner **décrire → vérifier → agir → lire les sorties**, avec le réflexe « je regarde le statut de chaque machine ».
>
> **🧩 Mini-projet 3 — « Commandes ad hoc multi-machines ».**
> Sur le groupe `web`, lance trois commandes de lecture différentes (par exemple : `hostname`, `df -h /`, et la version de l'OS via `shell` + pipe). Compare les sorties entre les deux machines.

> **La suite :** en Partie 3, on s'attaque au concept qui rend Ansible **vraiment** différent d'un script : l'**idempotence**. Tu vas le **voir de tes yeux** en relançant une commande.

---
---
---
