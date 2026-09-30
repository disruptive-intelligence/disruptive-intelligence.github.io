---
title: PARTIE 3 — COMPRENDRE LES SORTIES ET L'IDEMPOTENCE
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
chapter: 4
chapters: 13
---

> **Objectif de la partie :** comprendre ce qui rend Ansible différent d'un simple script. Tu vas **voir de tes yeux** l'idempotence en relançant une commande, et comprendre pourquoi les **modules dédiés** sont supérieurs à `command`/`shell`.

---


## Chapitre 3.1 — `ok` vs `changed`

### Le minimum à savoir

Au chapitre précédent, tu as vu les cinq statuts. Concentrons-nous sur les **deux plus importants**, car ils expliquent tout le fonctionnement d'Ansible :

- **`changed`** : Ansible a **agi**. Il y avait un écart entre l'état voulu et l'état réel, et Ansible l'a corrigé.
- **`ok`** : Ansible **n'a rien fait**. L'état voulu était **déjà** atteint, donc il n'y avait rien à corriger.

```
   ÉTAT VOULU : "htop installé"

   Machine où htop est ABSENT   →  Ansible installe  →  CHANGED
   Machine où htop est PRÉSENT  →  Ansible vérifie   →  OK (rien à faire)
```

> **C'est la distinction reine d'Ansible.** `changed` = « j'ai modifié quelque chose ». `ok` = « c'était déjà bon, je n'ai pas touché ». Comprendre ça, c'est comprendre l'idempotence.

### Très utile en pratique

Cette distinction te permet de **lire** ce qu'Ansible a réellement fait :

- Beaucoup de `changed` au **premier** passage : normal, Ansible met les machines en conformité.
- Que des `ok` quand tu **rejoues** : parfait, tout est déjà en place, rien n'a bougé.
- Un `changed` **inattendu** quand tu rejoues : quelque chose avait changé sur la machine, et Ansible l'a corrigé (ou alors ton action n'est pas idempotente — on verra ça).

### Exemple simple

```text
1er passage :  cible1 | CHANGED   (htop a été installé)
2e passage :   cible1 | SUCCESS   (htop était déjà là, rien à faire → ok)
```

### ❌ Erreur classique

> **Croire qu'un `changed` est forcément une bonne nouvelle, ou qu'un `ok` veut dire « rien ne marche ».**

`ok` ne veut **pas** dire « échec » ou « inaction inutile » — ça veut dire « **déjà conforme** », ce qui est excellent. Et `changed` n'est pas toujours souhaitable : si tu **rejoues** un playbook et qu'une tâche repasse en `changed` sans raison, c'est suspect. Le réflexe correct : **`ok` au second passage = bon signe** ; `changed` inattendu = à investiguer.

### Exercices

#### Guidé
Sans encore installer quoi que ce soit, relis dans ta tête : que signifie `ok` ? que signifie `changed` ? Écris une phrase pour chacun, avec tes propres mots.

#### Autonome
Imagine une tâche « le fichier /etc/motd doit contenir le texte X ». Au premier passage, quel statut attends-tu ? Et si tu relances **sans** avoir modifié le fichier ? Et si quelqu'un a modifié le fichier à la main entre-temps ?

#### Défi
Explique pourquoi voir **`ok` partout** quand on rejoue un playbook est, en réalité, **rassurant** pour un administrateur. Qu'est-ce que ça prouve sur l'état du parc ?

### ✅ Tu sais maintenant…

- Que **`changed`** = Ansible a agi (il y avait un écart) et **`ok`** = rien à faire (déjà conforme).
- Que c'est la **distinction reine** qui explique le fonctionnement d'Ansible.
- Que des **`ok` au rejeu** sont un bon signe, et qu'un **`changed` inattendu** mérite attention.

---


## Chapitre 3.2 — Voir l'idempotence en relançant

### Le minimum à savoir

L'**idempotence**, tu en as eu l'image en Partie 0. Maintenant, tu vas la **voir en vrai**. Le principe : tu lances **deux fois** la même action, et tu observes le changement de statut.

```
   1er lancement : action effectuée    →  CHANGED
   2e lancement :  rien à faire         →  OK
   3e lancement :  rien à faire         →  OK
   ... (toujours OK tant que l'état voulu est respecté)
```

> **C'est ça, l'idempotence en pratique :** la première fois, Ansible agit (`changed`). Ensuite, tant que l'état voulu est respecté, il ne fait plus rien (`ok`). Tu peux relancer cent fois, ce sera toujours `ok`.

### Très utile en pratique

On le démontre avec un module **idempotent** (le module `apt`, qu'on détaillera en Partie 5). L'idée : installer un paquet, puis relancer.

```bash
# 1er lancement : le paquet n'est pas là → Ansible l'installe
ansible web -i inventory.ini -m ansible.builtin.apt -a "name=htop state=present" --become

# 2e lancement : EXACTEMENT la même commande
ansible web -i inventory.ini -m ansible.builtin.apt -a "name=htop state=present" --become
```

*(Le `--become` sert à obtenir les droits root pour installer — on l'explique en Partie 4. Pour l'instant, accepte-le.)*

```text
1er lancement :  cible1 | CHANGED   (htop installé)
2e lancement :   cible1 | SUCCESS   (htop déjà là → ok, changed: false)
```

### Exemple simple

Le cœur de la démonstration tient en deux lignes de sortie :

```text
changed   ← la première fois, Ansible a agi
ok        ← la seconde fois, rien à faire
```

Si tu vois ça, **félicitations** : tu viens d'observer l'idempotence.

### 🔍 Réflexe diagnostic

> Si une action affiche **`changed` à CHAQUE** relance (jamais `ok`), c'est le signe qu'elle **n'est pas idempotente**. C'est presque toujours le cas avec `command`/`shell` (qui réexécutent aveuglément). On voit pourquoi au chapitre suivant.

### ❌ Erreur classique

> **S'inquiéter de voir `changed` au premier passage.**

Un débutant voit `changed` et croit qu'il y a un problème. **Non** : `changed` au premier passage est **normal et attendu** — Ansible met la machine en conformité. Le réflexe correct : ce qui compte, c'est le **second** passage. S'il affiche `ok`, ton action est idempotente et tout va bien.

### Exercices

#### Guidé
Lance la commande d'installation de `htop` ci-dessus **une fois**, observe `changed`. Relance-la **à l'identique**, observe `ok` (`changed: false`). Tu viens de voir l'idempotence en action.

#### Autonome
Crée une **dérive** : installe `htop` avec Ansible (`changed`), puis désinstalle-le **à la main** sur une cible (`sudo apt remove htop`). Relance la commande Ansible : que se passe-t-il ? Explique pourquoi Ansible réaffiche `changed`.

#### Défi
Explique en quelques lignes pourquoi cette propriété fait d'Ansible un outil capable de **corriger les dérives** : si une machine s'écarte de l'état voulu, que se passe-t-il quand on rejoue ?

### ✅ Tu sais maintenant…

- **Voir** l'idempotence : `changed` au 1er passage, `ok` aux suivants.
- Qu'un module **idempotent** (comme `apt`) ne réagit que s'il y a un écart.
- Qu'un **`changed` permanent** au rejeu signale une action **non idempotente**.
- Qu'Ansible **corrige les dérives** : rejouer ramène une machine à l'état voulu.

---


## Chapitre 3.3 — Modules dédiés vs `command`/`shell`

### Le minimum à savoir

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

### Très utile en pratique

La règle pratique pour tout le cours :

- **Pour installer un paquet** → module `apt`/`dnf` (pas `shell -a "apt install"`).
- **Pour gérer un service** → module `service` (pas `shell -a "systemctl"`).
- **Pour copier un fichier** → module `copy` (pas `shell -a "cp"`).
- **Pour créer un utilisateur** → module `user` (pas `shell -a "useradd"`).

`command`/`shell` ne servent que pour ce qui **n'a pas** de module dédié.

### Exemple simple

```text
shell -a "apt install -y htop"  (relancé)  →  changed, changed, changed...  (jamais idempotent)
apt   name=htop state=present   (relancé)  →  changed, puis ok, ok, ok...   (idempotent !)
```

### 🔀 À ne pas confondre

> **« Lancer une commande » vs « déclarer un état ».**
> `shell -a "apt install nginx"` = « lance cette commande » (impératif). `apt name=nginx state=present` = « nginx doit être présent » (état souhaité). Le second est idempotent, le premier non.

### ❌ Erreur classique

> **Reproduire ses réflexes Bash dans Ansible en utilisant `shell` partout.**

L'admin habitué à la ligne de commande écrit `shell -a "systemctl start nginx"`, `shell -a "useradd bob"`. Ça **fonctionne**, mais ça **détruit** l'idempotence et la lisibilité. Le réflexe correct : **chercher d'abord le module dédié** (on les apprend en Partie 5). Ils existent pour presque tout. Garde `command`/`shell` pour les rares cas sans module.

### Exercices

#### Guidé
Installe `htop` de **deux** façons sur une cible de test (snapshot pris) : d'abord avec `shell -a "apt install -y htop"`, relancé deux fois (observe `changed` à chaque fois). Puis avec `apt name=htop state=present`, relancé deux fois (observe `changed` puis `ok`). Compare.

#### Autonome
Liste **quatre** tâches d'administration courantes et, pour chacune, indique le **module dédié** que tu utiliserais plutôt que `shell` (indice : paquet, service, fichier, utilisateur).

#### Défi
Explique en quelques lignes pourquoi un playbook rempli de `shell` est difficile à **rejouer en confiance**, alors qu'un playbook fait de modules dédiés peut être relancé sans crainte. Relie ta réponse à l'idempotence.

### ✅ Tu sais maintenant…

- Pourquoi les **modules dédiés** sont **idempotents** (ils déclarent et vérifient un état).
- Pourquoi **`command`/`shell`** ne le sont pas (ils exécutent aveuglément).
- La règle : **module dédié** pour paquets/services/fichiers/utilisateurs ; `shell` seulement en dernier recours.
- Que l'idempotence rend un playbook **rejouable en confiance**.

---

### 🚩 Checkpoint — Fin de la Partie 3

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
