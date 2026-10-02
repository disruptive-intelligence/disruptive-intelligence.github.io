---
title: 'Chapitre 4.4 — Vérifier avant d''agir : --syntax-check et --check'
source: IT/08 Conteneurs & automatisation/Automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 4 — YAML et premiers playbooks
  - index.md
---

## Le minimum à savoir

Avant de lancer un playbook « pour de vrai », on prend l'habitude de le **vérifier**. Deux outils essentiels :

- **`--syntax-check`** : vérifie que la **syntaxe YAML** est correcte. Instantané, ne se connecte à rien.
- **`--check`** : lance le playbook en **simulation**. Ansible te dit **ce qu'il ferait**, **sans rien modifier** sur les machines.

```bash
ansible-playbook -i inventory.ini site.yml --syntax-check   # 1. la syntaxe est-elle bonne ?
ansible-playbook -i inventory.ini site.yml --check          # 2. qu'est-ce qui CHANGERAIT ?
ansible-playbook -i inventory.ini site.yml                  # 3. exécution réelle
```


> **L'enchaînement de prudence :** `--syntax-check` → `--check` → exécution réelle. Chaque étape attrape un type de problème différent, **avant** qu'il ne touche tes machines.

## Très utile en pratique

En mode `--check`, les tâches qui **modifieraient** quelque chose apparaissent en `changed` (mais **rien n'est réellement modifié**), et les autres en `ok`. C'est une **simulation**.

```bash
ansible-playbook -i inventory.ini site.yml --check
```


> ⚠️ **Bon à savoir :** `--check` est une **simulation très utile**, mais **pas parfaite**. Certains modules gèrent mal le mode simulation, et certains résultats dépendent de l'état réel au moment de l'exécution. Vois `--check` comme un **réflexe de prudence**, pas comme une garantie absolue.

## Exemple simple

```text
$ ansible-playbook -i inventory.ini site.yml --check
TASK [Installer nginx] ***
changed: [cible1]          ← en réalité, RIEN n'est installé : c'est une simulation
```


## 🧪 Lab vs production

> En **lab**, tu peux te permettre de lancer directement. Mais prends **dès maintenant** l'habitude de `--check` avant les actions importantes : c'est le réflexe qui, en **production**, t'évitera des catastrophes. Apprendre le bon geste en lab, c'est l'avoir acquis pour plus tard.

## ❌ Erreur classique

> **Lancer un playbook directement, sans jamais vérifier la syntaxe ni simuler.**

On écrit un playbook, on le lance, et une erreur d'indentation (ou pire, une action non voulue) se déclenche. Le réflexe correct : **`--syntax-check` systématique**, et **`--check`** avant toute action qui modifie des machines. Quelques secondes de vérification évitent bien des ennuis.

## Exercices

### Guidé
Sur ton playbook nginx, lance d'abord `--syntax-check` (corrige les erreurs éventuelles), puis `--check` (observe ce qui *changerait*), puis l'exécution réelle. Compare la sortie `--check` et la sortie réelle.

### Autonome
Modifie ton playbook (par exemple, ajoute l'installation d'un paquet supplémentaire) et lance `--check` **avant** d'exécuter. Vérifie que la simulation annonce bien le changement attendu, puis exécute pour de vrai.

### Défi
Lance `--check` sur un playbook **déjà appliqué** (donc tout est déjà conforme). Que montre la simulation (`ok` partout ou `changed` ?) ? Explique ce que ça t'apprend sur l'état actuel de tes machines.

## ✅ Tu sais maintenant…

- Vérifier la syntaxe avec **`--syntax-check`** (instantané).
- Simuler avec **`--check`** : voir ce qui changerait **sans rien modifier**.
- L'enchaînement **`--syntax-check` → `--check` → exécution**.
- Que `--check` est **utile mais pas parfait** (réflexe de prudence, pas garantie).

---

## 🚩 Checkpoint — Fin de la Partie 4

Tu sais maintenant écrire de vrais playbooks. Avant d'apprendre les modules d'administration, assure-toi de pouvoir :

- [ ] Écrire un **YAML** correct (indentation espaces, listes, dictionnaires) et le valider.
- [ ] Structurer un playbook en **play → tasks → modules**, avec des `name:` clairs.
- [ ] Utiliser **`become`** pour les actions nécessitant root.
- [ ] Lire le **`PLAY RECAP`**.
- [ ] Vérifier avec **`--syntax-check`** et simuler avec **`--check`**.

> **🧩 Mini-projet 5 — « Déployer un service web simple ».**
> Écris un playbook qui : installe nginx (module `apt`, avec `become`), le démarre et l'active (module `service`). Vérifie-le (`--syntax-check`, `--check`), exécute-le, teste l'accès web, **relance-le** pour confirmer l'idempotence (`ok` partout), puis provoque une dérive (arrête nginx à la main) et montre qu'un nouveau run la **corrige**.

> **La suite :** en Partie 5, on apprend les **modules d'administration Linux** les plus utiles : paquets, services, fichiers, permissions, utilisateurs et groupes. De quoi administrer une vraie machine proprement.

---
---
---
