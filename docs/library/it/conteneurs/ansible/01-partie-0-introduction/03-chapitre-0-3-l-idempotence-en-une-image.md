---
title: Chapitre 0.3 — L'idempotence en une image
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 0 — Introduction
  - index.md
---

## Le minimum à savoir

Le mot fait peur, l'idée est simple. **Idempotent** veut dire : *qu'on l'applique une fois ou dix fois, le résultat est le même, et rejouer ne casse rien.*

Reprends l'idée de l'état souhaité. Si tu demandes « nginx doit être installé » :

- **1ʳᵉ fois** : nginx n'est pas là → Ansible l'installe. Il signale qu'il a **changé** quelque chose.
- **2ᵉ fois** : nginx est déjà là → Ansible **ne fait rien**. Il signale que tout était déjà **ok**.
- **3ᵉ, 4ᵉ, 100ᵉ fois** : toujours `ok`. Rien ne bouge.

```
   1er run :  [ nginx absent ]  →  Ansible installe  →  CHANGED  (j'ai agi)
   2e run :   [ nginx présent ] →  Ansible vérifie   →  OK       (rien à faire)
   3e run :   [ nginx présent ] →  Ansible vérifie   →  OK       (rien à faire)
```


> **C'est ça, l'idempotence :** tu peux rejouer une description Ansible autant de fois que tu veux. Elle n'agit **que** s'il y a un écart à corriger. Un script Bash avec `apt install`, lui, relancerait l'installation à chaque fois.

## Très utile en pratique

L'idempotence te donne une **tranquillité** énorme :

- Tu peux relancer un playbook **sans crainte** de tout casser ou dupliquer.
- Tu peux l'utiliser pour **vérifier** : si tout est `ok`, le parc est conforme ; si quelque chose passe en `changed`, c'est qu'une machine avait **dévié** et qu'Ansible l'a corrigée.

On reviendra **vraiment** dessus en Partie 3, avec une démonstration que tu feras toi-même. Pour l'instant, garde juste l'image.

## Exemple simple

Tu lances deux fois de suite la même description « htop doit être installé » :

```text
1er lancement →  changed   (Ansible a installé htop)
2e lancement →  ok         (htop était déjà là, rien à faire)
```


Si tu voyais `changed` **à chaque** relance, ce serait le signe que quelque chose n'est **pas** idempotent — un point qu'on apprendra à repérer.

## ❌ Erreur classique

> **Confondre « idempotent » avec « qui ne fait jamais rien ».**

Idempotent ne veut **pas** dire « passif ». Ansible **agit** quand il le faut (1ʳᵉ fois, ou quand une machine a dévié), et **se retient** quand tout est déjà bon. Le réflexe correct : voir l'idempotence comme « **agir juste ce qu'il faut, ni plus ni moins** ».

## Exercices

### Guidé
Pour chacune de ces actions, dis si elle est naturellement **idempotente** (rejouer ne change rien si c'est déjà fait) ou non :

- « s'assurer qu'un fichier contient une ligne précise »
- « ajouter une ligne à la fin d'un fichier à chaque exécution »
- « s'assurer qu'un utilisateur existe »

### Autonome
Explique en 3-4 phrases pourquoi l'idempotence rend Ansible **rassurant** à utiliser, comparé à un script qu'on hésite à relancer.

### Défi
Imagine un script qui crée un utilisateur avec la commande `useradd bob`. Que se passe-t-il si on le lance **deux fois** ? Et comment une approche en **état souhaité** (« bob doit exister ») évite-t-elle ce problème ?

## ✅ Tu sais maintenant…

- Ce que veut dire **idempotent** : rejouer donne le même résultat, sans rien casser.
- Qu'Ansible agit **seulement s'il y a un écart** (`changed`), sinon il ne fait rien (`ok`).
- Que l'idempotence rend les playbooks **rejouables sans crainte**.
- Qu'« idempotent » ne veut **pas** dire « passif » : Ansible agit **juste ce qu'il faut**.

---
