---
title: Chapitre 4.2 — Anatomie d'un playbook
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 4 — YAML et premiers playbooks
  - index.md
---

## Le minimum à savoir

Un **playbook** est un fichier YAML qui décrit une série d'actions **rejouables**. C'est le passage de « je tape une commande » à « j'écris une procédure que je peux relancer et partager ».

Voici un playbook complet et commenté :

```yaml
---
- name: Installer et démarrer un serveur web      # ← un PLAY (un bloc)
  hosts: web                                      # ← sur quelles machines
  become: true                                    # ← avec les droits root (Ch. 4.3)

  tasks:                                          # ← la liste des TÂCHES
    - name: Installer nginx                       # ← une TÂCHE (toujours nommée)
      ansible.builtin.apt:                        # ← le MODULE (nom complet)
        name: nginx                               # ← les arguments du module
        state: present

    - name: Démarrer et activer nginx
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: true
```


- Un **play** associe un **groupe de machines** (`hosts`) à une **liste de tâches**.
- Une **tâche** = un **module** + ses **arguments**, avec un **`name:`** lisible.

> **Toujours nommer ses tâches.** Le `name:` apparaît dans la sortie d'exécution : il rend le déroulé **lisible** et le diagnostic **facile**.

## Très utile en pratique

```bash
# Lancer un playbook
ansible-playbook -i inventory.ini site.yml
```


À la fin, Ansible affiche un **récapitulatif** (`PLAY RECAP`) par machine :

```text
PLAY RECAP *********************************************************
cible1  : ok=2    changed=2    unreachable=0    failed=0    skipped=0
cible2  : ok=2    changed=2    unreachable=0    failed=0    skipped=0
```


Ce récapitulatif te dit, machine par machine, combien de tâches ont réussi, modifié, échoué, été ignorées ou injoignables. **C'est le premier endroit où regarder.**

## Exemple simple

Un playbook minimal à une seule tâche :

```yaml
---
- name: Vérifier la connexion
  hosts: all
  tasks:
    - name: Ping
      ansible.builtin.ping:
```


## ❌ Erreur classique

> **Oublier de nommer ses tâches, ou se tromper de niveau d'indentation entre `hosts`, `tasks` et les tâches.**

Sans `name:`, la sortie devient illisible (« tâche anonyme »). Et une mauvaise indentation entre `tasks:` et les tâches casse le playbook. Le réflexe correct : **nommer chaque tâche** et respecter l'indentation (les tâches sont **indentées sous** `tasks:`). Un `--syntax-check` confirme que la structure tient.

## Exercices

### Guidé
Écris le playbook `site.yml` qui installe et démarre nginx sur le groupe `web` (modèle ci-dessus). Lance `--syntax-check`, puis exécute-le. Vérifie le `PLAY RECAP` et l'accès à nginx (avec `curl` ou un navigateur vers l'IP d'une cible).

### Autonome
Relance **le même** playbook une seconde fois. Observe le `PLAY RECAP` : les tâches passent de `changed` à `ok` (idempotence à l'échelle du playbook). Puis arrête nginx à la main sur une cible et relance : observe qu'Ansible **corrige** la dérive.

### Défi
Ajoute une troisième tâche qui affiche un message avec le module `ansible.builtin.debug` (par exemple `msg: "nginx est prêt"`). Vérifie que la nouvelle tâche apparaît bien, nommée, dans la sortie.

## ✅ Tu sais maintenant…

- L'anatomie d'un playbook : **play → tasks → modules**, avec `hosts` et `name:`.
- Lancer un playbook avec **`ansible-playbook`**.
- Lire le **`PLAY RECAP`** comme premier réflexe.
- Qu'il faut **nommer** chaque tâche et soigner l'indentation.

---
