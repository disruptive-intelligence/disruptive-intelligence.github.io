---
title: Chapitre 3.1 — ok vs changed
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 3 — Comprendre les sorties et L'idempotence
  - index.md
---

## Le minimum à savoir

Au chapitre précédent, tu as vu les cinq statuts. Concentrons-nous sur les **deux plus importants**, car ils expliquent tout le fonctionnement d'Ansible :

- **`changed`** : Ansible a **agi**. Il y avait un écart entre l'état voulu et l'état réel, et Ansible l'a corrigé.
- **`ok`** : Ansible **n'a rien fait**. L'état voulu était **déjà** atteint, donc il n'y avait rien à corriger.

```
   ÉTAT VOULU : "htop installé"

   Machine où htop est ABSENT   →  Ansible installe  →  CHANGED
   Machine où htop est PRÉSENT  →  Ansible vérifie   →  OK (rien à faire)
```


> **C'est la distinction reine d'Ansible.** `changed` = « j'ai modifié quelque chose ». `ok` = « c'était déjà bon, je n'ai pas touché ». Comprendre ça, c'est comprendre l'idempotence.

## Très utile en pratique

Cette distinction te permet de **lire** ce qu'Ansible a réellement fait :

- Beaucoup de `changed` au **premier** passage : normal, Ansible met les machines en conformité.
- Que des `ok` quand tu **rejoues** : parfait, tout est déjà en place, rien n'a bougé.
- Un `changed` **inattendu** quand tu rejoues : quelque chose avait changé sur la machine, et Ansible l'a corrigé (ou alors ton action n'est pas idempotente — on verra ça).

## Exemple simple

```text
1er passage :  cible1 | CHANGED   (htop a été installé)
2e passage :   cible1 | SUCCESS   (htop était déjà là, rien à faire → ok)
```


## ❌ Erreur classique

> **Croire qu'un `changed` est forcément une bonne nouvelle, ou qu'un `ok` veut dire « rien ne marche ».**

`ok` ne veut **pas** dire « échec » ou « inaction inutile » — ça veut dire « **déjà conforme** », ce qui est excellent. Et `changed` n'est pas toujours souhaitable : si tu **rejoues** un playbook et qu'une tâche repasse en `changed` sans raison, c'est suspect. Le réflexe correct : **`ok` au second passage = bon signe** ; `changed` inattendu = à investiguer.

## Exercices

### Guidé
Sans encore installer quoi que ce soit, relis dans ta tête : que signifie `ok` ? que signifie `changed` ? Écris une phrase pour chacun, avec tes propres mots.

### Autonome
Imagine une tâche « le fichier /etc/motd doit contenir le texte X ». Au premier passage, quel statut attends-tu ? Et si tu relances **sans** avoir modifié le fichier ? Et si quelqu'un a modifié le fichier à la main entre-temps ?

### Défi
Explique pourquoi voir **`ok` partout** quand on rejoue un playbook est, en réalité, **rassurant** pour un administrateur. Qu'est-ce que ça prouve sur l'état du parc ?

## ✅ Tu sais maintenant…

- Que **`changed`** = Ansible a agi (il y avait un écart) et **`ok`** = rien à faire (déjà conforme).
- Que c'est la **distinction reine** qui explique le fonctionnement d'Ansible.
- Que des **`ok` au rejeu** sont un bon signe, et qu'un **`changed` inattendu** mérite attention.

---
