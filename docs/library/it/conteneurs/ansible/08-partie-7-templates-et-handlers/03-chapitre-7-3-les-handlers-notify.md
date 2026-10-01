---
title: Chapitre 7.3 — Les handlers (notify)
source: IT/08 Conteneurs & automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 7 — Templates et handlers
  - index.md
---

## Le minimum à savoir

Quand tu modifies la configuration d'un service, il faut souvent le **redémarrer** pour appliquer le changement. Mais le redémarrer **à chaque** exécution (même quand rien n'a changé) provoque des interruptions inutiles. La solution : les **handlers**.

Un **handler** est une tâche spéciale qui ne s'exécute **que si elle est notifiée** par un changement.

```yaml
tasks:
  - name: Déployer la config nginx
    ansible.builtin.template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify: Redémarrer nginx        # ← notifie le handler SI cette tâche change qqch
    become: true

handlers:
  - name: Redémarrer nginx          # ← le handler (déclenché seulement si notifié)
    ansible.builtin.service:
      name: nginx
      state: restarted
    become: true
```


> **Le mécanisme :** si la tâche de config **change** quelque chose (`changed`), elle **notifie** le handler, qui s'exécute **à la fin** du play. Si la config n'a **pas** changé (`ok`), le handler **ne s'exécute pas**. Résultat : **on ne redémarre que si nécessaire.**

## Très utile en pratique

```
   Config modifiée (changed)  →  handler notifié  →  service redémarré
   Config inchangée (ok)       →  handler NON notifié →  service PAS redémarré
```


C'est exactement ce qu'on veut : pas de redémarrage inutile, mais un redémarrage **garanti** quand la config change.

## Exemple simple

```yaml
tasks:
  - name: Modifier la config SSH
    ansible.builtin.lineinfile:
      path: /etc/ssh/sshd_config
      regexp: '^#?PermitRootLogin'
      line: 'PermitRootLogin no'
    notify: Redemarrer ssh
    become: true

handlers:
  - name: Redemarrer ssh
    ansible.builtin.service:
      name: ssh
      state: restarted
    become: true
```


## 🔀 À ne pas confondre

> **Tâche normale vs handler.**
> Une **tâche** s'exécute à chaque fois (selon son idempotence). Un **handler** ne s'exécute **que s'il est notifié** par un changement, et **une seule fois** à la fin, même s'il est notifié plusieurs fois. C'est fait pour les actions « à déclencher si quelque chose a changé ».

## ❌ Erreur classique

> **Mettre un `restart` directement dans les tâches au lieu d'utiliser un handler.**

Une tâche `service: state=restarted` placée dans les `tasks` redémarre le service **à chaque** exécution, même quand rien n'a changé — interruptions inutiles. Le réflexe correct : mettre le redémarrage dans un **handler**, notifié par la tâche de config. Le service ne redémarre **que** quand sa config change réellement.

## Exercices

### Guidé
Transforme ton playbook nginx : déploie la config par `template` (ou modifie une ligne par `lineinfile`), et **notifie** un handler « Redémarrer nginx ». Lance le playbook : le handler se déclenche (config posée). Relance-le : le handler **ne se déclenche pas** (rien n'a changé).

### Autonome
Crée un handler pour redémarrer SSH, notifié par une modification de `sshd_config`. Vérifie qu'il ne se déclenche que lorsque la config change réellement. (Attention : teste sur une cible avec snapshot, pour ne pas te couper l'accès.)

### Défi
Mets **deux** tâches qui notifient le **même** handler. Observe qu'il ne s'exécute **qu'une seule fois** à la fin, même notifié deux fois. Explique pourquoi ce comportement est utile.

## ✅ Tu sais maintenant…

- Ce qu'est un **handler** : une tâche déclenchée **uniquement si notifiée** par un changement.
- Utiliser **`notify`** pour relier une tâche à un handler.
- Que le handler s'exécute **à la fin** du play, **une seule fois**.
- Que les handlers évitent les **redémarrages inutiles**.

---

## 🚩 Checkpoint — Fin de la Partie 7

Tu sais maintenant générer de la config et redémarrer proprement. Avant les bonnes pratiques, assure-toi de pouvoir :

- [ ] Générer des fichiers dynamiques avec **`template`** + **Jinja2** (`{{ }}`, `{% if %}`, `{% for %}`).
- [ ] Choisir entre **`copy`**, **`template`** et **`lineinfile`**.
- [ ] Utiliser des **handlers** avec **`notify`** pour redémarrer un service seulement si nécessaire.

> **🧩 Mini-projet 8 — « Générer une configuration avec template ».**
> Déploie un fichier de configuration (par exemple un `motd` ou une page web) **personnalisé par machine** grâce à un template Jinja2. Vérifie que chaque cible a sa version.
>
> **🧩 Mini-projet 9 — « Handler conditionnel ».**
> Déploie une config de service par template, avec un **handler** de redémarrage notifié. Lance deux fois : observe que le service ne redémarre **qu'au premier passage** (quand la config change), pas au second.

> **La suite :** en Partie 8, on apprend les **bons réflexes** du débutant : nommer ses tâches, vérifier avant d'agir (`--check`, `--diff`), cibler avec prudence (`--limit`), et les bases de sécurité (clés SSH, pas de secret en clair).

---
---
