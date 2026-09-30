---
title: 'Chapitre 0.2 — L''idée d''Ansible : l''état souhaité'
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 0 — Introduction
  - index.md
---

## Le minimum à savoir

Voici la différence la plus importante à comprendre, et elle est simple.

Un **script** (en Bash, par exemple) est une **liste d'ordres** : « fais ceci, puis cela ». Il exécute, point. Si tu le relances, il refait tout — même ce qui était déjà fait. Et parfois, ça casse (par exemple, créer un utilisateur qui existe déjà provoque une erreur).

Ansible fonctionne autrement. Tu décris un **état souhaité** : « cet utilisateur **doit exister** », « ce paquet **doit être installé** », « ce service **doit tourner** ». Ansible regarde la machine, **compare** avec ce que tu as demandé, et n'agit **que** s'il y a un écart.

```
   SCRIPT (impératif)              ANSIBLE (état souhaité)
   "crée l'utilisateur bob"        "l'utilisateur bob doit exister"
   → erreur si bob existe déjà     → bob existe ? rien à faire.
                                     bob absent ? je le crée.
```


> **L'idée clé :** tu ne dis pas **comment** faire étape par étape, tu dis **ce que tu veux obtenir**. Ansible se charge d'y arriver, et de **ne rien refaire inutilement**.

## Très utile en pratique

Cette façon de penser change tout :

- Tu peux **rejouer** une description autant de fois que tu veux, sans crainte.
- Tu peux l'appliquer à **une** machine ou à **cent**, c'est la même description.
- Si une machine a **dévié**, rejouer la description la **ramène** à l'état voulu.

C'est pour ça qu'on dit qu'Ansible **maintient** un état, alors qu'un script **exécute** des ordres.

## Exemple simple

Une instruction Ansible typique ressemble à ça (ne t'inquiète pas de la syntaxe, on l'apprendra) :

```yaml
- name: S'assurer que nginx est installé
  ansible.builtin.apt:
    name: nginx
    state: present       # ← "present" = l'état souhaité : nginx DOIT être là
```


Remarque le mot **`present`** : tu ne dis pas « installe nginx », tu dis « nginx **doit être présent** ». Si c'est déjà le cas, Ansible ne fait rien. C'est subtil, mais c'est **toute** la philosophie.

## ❌ Erreur classique

> **Penser en « ordres à exécuter » au lieu de « résultat à obtenir ».**

Un débutant venant des scripts a le réflexe d'écrire « lance cette commande ». Ansible préfère « assure-toi que cet état est atteint ». Le réflexe correct : pour chaque tâche, demande-toi **« quel résultat je veux ? »** plutôt que **« quelle commande je tape ? »**. C'est ce changement d'état d'esprit qui rend Ansible puissant.

## Exercices

### Guidé
Reformule ces trois ordres en **états souhaités** :

- « installe le paquet git » → « le paquet git doit… »
- « démarre le service ssh » → « le service ssh doit… »
- « crée le dossier /opt/app » → « le dossier /opt/app doit… »

### Autonome
Explique avec tes mots la différence entre « exécuter une commande » et « décrire un état souhaité ». Donne un exemple où **relancer** un script poserait problème, mais où **relancer** une description Ansible ne poserait aucun problème.

### Défi
Le mot `state: present` a un opposé : `state: absent`. Sans encore connaître la syntaxe, devine ce que voudrait dire une tâche avec `state: absent` pour un paquet. En quoi est-ce, là aussi, un **état souhaité** plutôt qu'un ordre ?

## ✅ Tu sais maintenant…

- La différence entre un **script** (liste d'ordres) et Ansible (**état souhaité**).
- Que tu décris **ce que tu veux obtenir**, pas **comment** le faire étape par étape.
- Que cette approche rend les actions **rejouables** sans risque.
- Le sens d'un mot comme **`present`** (l'état voulu, pas l'ordre « installe »).

---
