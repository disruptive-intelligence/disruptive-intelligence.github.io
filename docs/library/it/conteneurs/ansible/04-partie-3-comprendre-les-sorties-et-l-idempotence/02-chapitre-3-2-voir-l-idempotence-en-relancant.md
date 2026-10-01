---
title: Chapitre 3.2 — Voir l'idempotence en relançant
source: IT/08 Conteneurs & automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 3 — Comprendre les sorties et l'idempotence
  - index.md
---

## Le minimum à savoir

L'**idempotence**, tu en as eu l'image en Partie 0. Maintenant, tu vas la **voir en vrai**. Le principe : tu lances **deux fois** la même action, et tu observes le changement de statut.

```
   1er lancement : action effectuée    →  CHANGED
   2e lancement :  rien à faire         →  OK
   3e lancement :  rien à faire         →  OK
   ... (toujours OK tant que l'état voulu est respecté)
```


> **C'est ça, l'idempotence en pratique :** la première fois, Ansible agit (`changed`). Ensuite, tant que l'état voulu est respecté, il ne fait plus rien (`ok`). Tu peux relancer cent fois, ce sera toujours `ok`.

## Très utile en pratique

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


## Exemple simple

Le cœur de la démonstration tient en deux lignes de sortie :

```text
changed   ← la première fois, Ansible a agi
ok        ← la seconde fois, rien à faire
```


Si tu vois ça, **félicitations** : tu viens d'observer l'idempotence.

## 🔍 Réflexe diagnostic

> Si une action affiche **`changed` à CHAQUE** relance (jamais `ok`), c'est le signe qu'elle **n'est pas idempotente**. C'est presque toujours le cas avec `command`/`shell` (qui réexécutent aveuglément). On voit pourquoi au chapitre suivant.

## ❌ Erreur classique

> **S'inquiéter de voir `changed` au premier passage.**

Un débutant voit `changed` et croit qu'il y a un problème. **Non** : `changed` au premier passage est **normal et attendu** — Ansible met la machine en conformité. Le réflexe correct : ce qui compte, c'est le **second** passage. S'il affiche `ok`, ton action est idempotente et tout va bien.

## Exercices

### Guidé
Lance la commande d'installation de `htop` ci-dessus **une fois**, observe `changed`. Relance-la **à l'identique**, observe `ok` (`changed: false`). Tu viens de voir l'idempotence en action.

### Autonome
Crée une **dérive** : installe `htop` avec Ansible (`changed`), puis désinstalle-le **à la main** sur une cible (`sudo apt remove htop`). Relance la commande Ansible : que se passe-t-il ? Explique pourquoi Ansible réaffiche `changed`.

### Défi
Explique en quelques lignes pourquoi cette propriété fait d'Ansible un outil capable de **corriger les dérives** : si une machine s'écarte de l'état voulu, que se passe-t-il quand on rejoue ?

## ✅ Tu sais maintenant…

- **Voir** l'idempotence : `changed` au 1er passage, `ok` aux suivants.
- Qu'un module **idempotent** (comme `apt`) ne réagit que s'il y a un écart.
- Qu'un **`changed` permanent** au rejeu signale une action **non idempotente**.
- Qu'Ansible **corrige les dérives** : rejouer ramène une machine à l'état voulu.

---
