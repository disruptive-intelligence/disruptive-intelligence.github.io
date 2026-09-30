---
title: Partie 12 — Mini-projets pratiques (récapitulatif)
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
up:
- - Ansible
  - index.md
---

> **Objectif de la partie :** consolider tous tes acquis. Les 12 mini-projets ci-dessous ont été **distribués** au fil des parties ; les voici **regroupés** comme un parcours complet, du lab nu au projet organisé avec roles. Reprends-les dans l'ordre pour un entraînement complet.

---

## Le parcours complet

| # | Mini-projet | Compétences | Partie |
|---|-------------|-------------|--------|
| 1 | **Mettre en place le lab Ansible** | VMs, SSH par clé, snapshots | 1 |
| 2 | **Créer un inventaire propre** | inventaire INI, groupes, variables | 2 |
| 3 | **Commandes ad hoc multi-machines** | `ping`, `command`, lecture des sorties | 2 |
| 4 | **Installer des paquets** (idempotence) | module `apt`, `changed` vs `ok` | 3 |
| 5 | **Déployer un service web simple** | playbook, `become`, `service` | 4 |
| 6 | **Copier un fichier sur plusieurs machines** | `copy`, permissions | 5 |
| 7 | **Créer un utilisateur sur plusieurs machines** | `user`, `group` | 5 |
| 8 | **Générer une configuration avec template** | `template`, Jinja2 | 7 |
| 9 | **Handler : redémarrer si nécessaire** | `notify`, handlers | 7 |
| 10 | **Chiffrer une variable avec Vault** | `ansible-vault`, `--ask-vault-pass` | 9 |
| 11 | **Organiser un mini-projet propre** | arborescence, `ansible.cfg`, Git | 10 |
| 12 | **Créer un role simple `common`** | roles, `defaults`, réutilisation | 11 |

---

## 🎯 Projet final intégrateur

Pour vraiment tout consolider, voici un **projet final** qui combine l'essentiel du cours :

**Objectif :** construire, à partir de ton lab, un projet Ansible **propre et complet** qui administre tes machines de bout en bout.

**Étapes :**

1. **Lab** : control + 2 cibles, SSH par clé, snapshots (mini-projet 1).
2. **Inventaire** : groupes `web`, variables de groupe, `ansible.cfg` (mini-projets 2 et 11).
3. **Role `common`** : paquets de base + `motd` par template + config commune (mini-projet 12).
4. **Playbook web** : installe nginx, déploie une page par template, gère le service avec un handler (mini-projets 5, 8, 9).
5. **Secret** : un mot de passe chiffré par Vault, utilisé dans un template (mini-projet 10).
6. **Organisation** : arborescence propre, README, Git avec `.gitignore` (mini-projet 11).
7. **Vérification** : tout en `--check --diff` d'abord, `--limit` sur une machine témoin, puis le groupe ; idempotence confirmée (deux passages → `ok`).

**Livrable :** un dépôt Git propre, documenté, idempotent, que tu pourrais montrer ou réutiliser.

> Ce projet final est ta **preuve de maîtrise** : il mobilise l'inventaire, les playbooks, les modules, les variables, les templates, les handlers, Vault, l'organisation et les roles. Si tu le réalises de bout en bout, tu sais administrer un parc Linux avec Ansible.

---
---
