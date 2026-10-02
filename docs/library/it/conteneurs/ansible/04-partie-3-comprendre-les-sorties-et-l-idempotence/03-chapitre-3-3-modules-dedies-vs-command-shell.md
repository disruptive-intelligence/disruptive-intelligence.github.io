---
title: Chapitre 3.3 — Modules dédiés vs command/shell
source: IT/08 Conteneurs & automatisation/Automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 3 — Comprendre les sorties et l'idempotence
  - index.md
---

## Le minimum à savoir

Voici **pourquoi** on t'a dit, en Partie 2, de préférer les modules dédiés. C'est une question d'**idempotence**.

Compare deux façons d'installer nginx :

```bash
# ❌ Avec shell : PAS idempotent
ansible web -i inventory.ini -m ansible.builtin.shell -a "apt install -y nginx" --become
# → relancé, il relance l'installation. TOUJOURS "changed". Il ne SAIT pas si c'est déjà fait.

# ✅ Avec le module dédié apt : IDEMPOTENT
ansible web -i inventory.ini -m ansible.builtin.apt -a "name=nginx state=present" --become
# → relancé, il constate que nginx est là → "ok". Il déclare un ÉTAT VOULU.
```


> **La différence est fondamentale :**
> - Un **module dédié** (`apt`, `service`, `copy`…) **déclare un état** (`state: present`) et sait **vérifier** si cet état est déjà atteint. D'où l'idempotence.
> - **`command`/`shell`** **exécutent aveuglément** : ils ne savent pas si l'action est déjà faite, donc ils la refont, et signalent toujours `changed`.

## Très utile en pratique

La règle pratique pour tout le cours :

- **Pour installer un paquet** → module `apt`/`dnf` (pas `shell -a "apt install"`).
- **Pour gérer un service** → module `service` (pas `shell -a "systemctl"`).
- **Pour copier un fichier** → module `copy` (pas `shell -a "cp"`).
- **Pour créer un utilisateur** → module `user` (pas `shell -a "useradd"`).

`command`/`shell` ne servent que pour ce qui **n'a pas** de module dédié.

## Exemple simple

```text
shell -a "apt install -y htop"  (relancé)  →  changed, changed, changed...  (jamais idempotent)
apt   name=htop state=present   (relancé)  →  changed, puis ok, ok, ok...   (idempotent !)
```


## 🔀 À ne pas confondre

> **« Lancer une commande » vs « déclarer un état ».**
> `shell -a "apt install nginx"` = « lance cette commande » (impératif). `apt name=nginx state=present` = « nginx doit être présent » (état souhaité). Le second est idempotent, le premier non.

## ❌ Erreur classique

> **Reproduire ses réflexes Bash dans Ansible en utilisant `shell` partout.**

L'admin habitué à la ligne de commande écrit `shell -a "systemctl start nginx"`, `shell -a "useradd bob"`. Ça **fonctionne**, mais ça **détruit** l'idempotence et la lisibilité. Le réflexe correct : **chercher d'abord le module dédié** (on les apprend en Partie 5). Ils existent pour presque tout. Garde `command`/`shell` pour les rares cas sans module.

## Exercices

### Guidé
Installe `htop` de **deux** façons sur une cible de test (snapshot pris) : d'abord avec `shell -a "apt install -y htop"`, relancé deux fois (observe `changed` à chaque fois). Puis avec `apt name=htop state=present`, relancé deux fois (observe `changed` puis `ok`). Compare.

### Autonome
Liste **quatre** tâches d'administration courantes et, pour chacune, indique le **module dédié** que tu utiliserais plutôt que `shell` (indice : paquet, service, fichier, utilisateur).

### Défi
Explique en quelques lignes pourquoi un playbook rempli de `shell` est difficile à **rejouer en confiance**, alors qu'un playbook fait de modules dédiés peut être relancé sans crainte. Relie ta réponse à l'idempotence.

## ✅ Tu sais maintenant…

- Pourquoi les **modules dédiés** sont **idempotents** (ils déclarent et vérifient un état).
- Pourquoi **`command`/`shell`** ne le sont pas (ils exécutent aveuglément).
- La règle : **module dédié** pour paquets/services/fichiers/utilisateurs ; `shell` seulement en dernier recours.
- Que l'idempotence rend un playbook **rejouable en confiance**.

---

## 🚩 Checkpoint — Fin de la Partie 3

Tu tiens maintenant le concept central d'Ansible. Avant d'écrire des playbooks, assure-toi de pouvoir :

- [ ] Expliquer **`ok` vs `changed`** avec tes mots.
- [ ] **Démontrer** l'idempotence en relançant une commande (`changed` → `ok`).
- [ ] Expliquer pourquoi les **modules dédiés** sont idempotents et pas `command`/`shell`.
- [ ] Comprendre qu'Ansible **corrige les dérives** quand on rejoue.

> **🧩 Mini-projet 4 — « L'idempotence en pratique ».**
> 1. Installe un paquet (`htop`) sur le groupe `web` avec le module `apt` et `--become`.
> 2. Relance la commande et **observe** le passage de `changed` à `ok`.
> 3. Désinstalle le paquet à la main sur une cible, relance Ansible, observe qu'il **corrige la dérive**.
> 4. Refais l'installation avec `shell -a "apt install -y htop"` et constate qu'il affiche **toujours** `changed`.
> Objectif : **vivre** la différence entre une action idempotente (module dédié) et une action non idempotente (`shell`).

> **La suite :** en Partie 4, on passe de l'éphémère (commandes ad hoc) au **rejouable et documenté** : on apprend le **YAML** et on écrit nos premiers **playbooks**.

---
---
