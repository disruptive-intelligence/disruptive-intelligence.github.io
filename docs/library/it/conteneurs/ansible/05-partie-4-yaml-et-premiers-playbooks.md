---
title: PARTIE 4 — YAML ET PREMIERS PLAYBOOKS
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
chapter: 5
chapters: 13
---

> **Objectif de la partie :** écrire tes premiers playbooks. On apprend d'abord le **YAML** (le format des playbooks), puis on construit un playbook complet, et on découvre les options pour **vérifier avant d'agir**.

---


## Chapitre 4.1 — YAML sans peur

### Le minimum à savoir

Les playbooks Ansible s'écrivent en **YAML**, un format texte fait pour être **lisible par un humain**. Pas de programmation : juste des **clés**, des **valeurs** et des **listes**, organisées par l'**indentation**.

Les trois briques de base :

```yaml
# 1. Une paire clé : valeur
nom: serveur-web
actif: true

# 2. Une liste (chaque élément commence par un tiret)
paquets:
  - nginx
  - htop
  - git

# 3. Un dictionnaire imbriqué (l'indentation crée la hiérarchie)
serveur:
  nom: web1
  ip: 192.168.56.11
```

#### LA règle d'or : l'indentation

> **En YAML, l'indentation EST la structure.** Elle se fait avec des **espaces**, **jamais** avec des tabulations. La convention : **2 espaces** par niveau, et on reste **cohérent** dans tout le fichier.

```yaml
# ✅ CORRECT
serveur:
  nom: web1
  ip: 192.168.56.11

# ❌ FAUX (ip n'est plus dans serveur)
serveur:
  nom: web1
ip: 192.168.56.11
```

Un fichier YAML commence souvent par `---` (qui marque le début du document).

### Très utile en pratique

```bash
# Vérifier qu'un fichier YAML / playbook est syntaxiquement correct (sans rien exécuter)
ansible-playbook playbook.yml --syntax-check
```

> 🔍 **Réflexe diagnostic :** `--syntax-check` attrape les erreurs d'indentation **avant** toute exécution. C'est gratuit et instantané. Prends l'habitude de le lancer dès qu'un YAML te résiste.

### Exemple simple

```yaml
---
serveur:
  nom: web1
  paquets:
    - nginx
    - htop
```

Lisible, non ? C'est tout l'intérêt du YAML : on **comprend** le fichier en le lisant.

### ❌ Erreur classique

> **Mélanger tabulations et espaces, ou se tromper de niveau d'indentation.**

C'est **l'**erreur YAML par excellence. Un copier-coller depuis le web introduit une tabulation invisible, et Ansible refuse le fichier avec un message parfois obscur. Le réflexe correct : configure ton éditeur pour afficher les caractères invisibles et **convertir les tabs en espaces**, et lance `--syntax-check` au moindre doute. La plupart des « bugs Ansible » des débutants sont des **bugs d'indentation**.

### Exercices

#### Guidé
Écris un petit fichier YAML décrivant un serveur (un nom, une liste de 3 paquets, un sous-dictionnaire). Lance `ansible-playbook ton_fichier.yml --syntax-check`. Corrige jusqu'à ce qu'il n'y ait plus d'erreur de syntaxe.

#### Autonome
Prends ton fichier et **casse-le** volontairement : décale une ligne, ou ajoute une tabulation. Lance `--syntax-check` et observe le message d'erreur. Apprends à relier le message à la cause.

#### Défi
Réécris ton inventaire INI (Partie 2) au format **YAML** dans la tête (clés/listes). Ce n'est pas obligatoire pour le cours, mais ça t'entraîne à « penser en YAML » : hôtes, groupes, variables sous forme de clés et de listes.

### ✅ Tu sais maintenant…

- Que les playbooks s'écrivent en **YAML** : clés/valeurs, listes, dictionnaires.
- Que **l'indentation EST la structure** (espaces, jamais de tabs, 2 espaces par niveau).
- Vérifier la syntaxe avec **`--syntax-check`**.
- Que la plupart des « bugs Ansible » débutants sont des **bugs d'indentation**.

---


## Chapitre 4.2 — Anatomie d'un playbook

### Le minimum à savoir

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

### Très utile en pratique

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

### Exemple simple

Un playbook minimal à une seule tâche :

```yaml
---
- name: Vérifier la connexion
  hosts: all
  tasks:
    - name: Ping
      ansible.builtin.ping:
```

### ❌ Erreur classique

> **Oublier de nommer ses tâches, ou se tromper de niveau d'indentation entre `hosts`, `tasks` et les tâches.**

Sans `name:`, la sortie devient illisible (« tâche anonyme »). Et une mauvaise indentation entre `tasks:` et les tâches casse le playbook. Le réflexe correct : **nommer chaque tâche** et respecter l'indentation (les tâches sont **indentées sous** `tasks:`). Un `--syntax-check` confirme que la structure tient.

### Exercices

#### Guidé
Écris le playbook `site.yml` qui installe et démarre nginx sur le groupe `web` (modèle ci-dessus). Lance `--syntax-check`, puis exécute-le. Vérifie le `PLAY RECAP` et l'accès à nginx (avec `curl` ou un navigateur vers l'IP d'une cible).

#### Autonome
Relance **le même** playbook une seconde fois. Observe le `PLAY RECAP` : les tâches passent de `changed` à `ok` (idempotence à l'échelle du playbook). Puis arrête nginx à la main sur une cible et relance : observe qu'Ansible **corrige** la dérive.

#### Défi
Ajoute une troisième tâche qui affiche un message avec le module `ansible.builtin.debug` (par exemple `msg: "nginx est prêt"`). Vérifie que la nouvelle tâche apparaît bien, nommée, dans la sortie.

### ✅ Tu sais maintenant…

- L'anatomie d'un playbook : **play → tasks → modules**, avec `hosts` et `name:`.
- Lancer un playbook avec **`ansible-playbook`**.
- Lire le **`PLAY RECAP`** comme premier réflexe.
- Qu'il faut **nommer** chaque tâche et soigner l'indentation.

---


## Chapitre 4.3 — `become` : les droits root

### Le minimum à savoir

Beaucoup d'actions d'administration (installer un paquet, modifier un fichier système, gérer un service) nécessitent les droits **root**. En Ansible, on les obtient avec **`become`** :

```yaml
- name: Installer un paquet (nécessite root)
  hosts: web
  become: true          # ← devient root (via sudo) pour les tâches de ce play
  tasks:
    - name: Installer nginx
      ansible.builtin.apt:
        name: nginx
        state: present
```

> **Rappel (Partie 1) :** se **connecter** (avec ton utilisateur SSH, souvent non-root) et **devenir root** (`become`) sont deux étapes distinctes. La bonne pratique : se connecter en utilisateur normal, et n'élever les droits **que** quand c'est nécessaire.

`become` peut se mettre au niveau du **play** (toutes les tâches) ou d'une **tâche précise** (seulement celle-là).

### Très utile en pratique

```yaml
- name: Play mixte
  hosts: web
  tasks:
    - name: Voir qui je suis (pas besoin de root)
      ansible.builtin.command: whoami

    - name: Installer un paquet (besoin de root)
      ansible.builtin.apt:
        name: htop
        state: present
      become: true          # ← root UNIQUEMENT pour cette tâche
```

### Exemple simple

Sans `become`, une installation de paquet échoue (« permission refusée ») :

```text
FAILED! => "msg": "... Permission denied ..."
```

Avec `become: true`, elle réussit. C'est le signe qu'il fallait les droits root.

### 🛡️ Réflexe sécurité

> N'active `become` que **là où c'est nécessaire**. Donner les droits root « par confort » à des tâches qui n'en ont pas besoin est une mauvaise habitude. Élève les privilèges **au cas par cas**, pour les seules tâches qui le requièrent.

### ❌ Erreur classique

> **Oublier `become` sur une tâche qui nécessite root, et conclure qu'« Ansible ne marche pas ».**

Une installation de paquet sans `become` échoue avec « Permission denied », et le débutant croit à un bug. Le réflexe correct : si une tâche d'administration système échoue pour des raisons de **permission**, il manque probablement **`become: true`**. Lis le message d'erreur : « permission denied » est un indice clair.

### Exercices

#### Guidé
Écris un playbook qui installe `htop` **sans** `become`. Lance-le : il échoue probablement avec une erreur de permission. Ajoute `become: true` et relance : il réussit. Tu comprends à quoi sert `become`.

#### Autonome
Crée un playbook avec deux tâches : une qui ne nécessite pas root (`whoami`) et une qui le nécessite (installer un paquet). Mets `become` **uniquement** sur la seconde. Vérifie que tout fonctionne.

#### Défi
Lance une tâche `ansible.builtin.command: whoami` **avec** puis **sans** `become: true`, et compare la sortie (le `debug` ou le retour de la commande). Que t'apprend la différence sur ce que fait réellement `become` ?

### ✅ Tu sais maintenant…

- Que **`become: true`** donne les droits **root** sur la cible.
- Que se **connecter** et **devenir root** sont deux étapes distinctes.
- Mettre `become` au niveau du **play** ou d'une **tâche** précise.
- Qu'une erreur de **permission** signale souvent un `become` manquant.

---


## Chapitre 4.4 — Vérifier avant d'agir : `--syntax-check` et `--check`

### Le minimum à savoir

Avant de lancer un playbook « pour de vrai », on prend l'habitude de le **vérifier**. Deux outils essentiels :

- **`--syntax-check`** : vérifie que la **syntaxe YAML** est correcte. Instantané, ne se connecte à rien.
- **`--check`** : lance le playbook en **simulation**. Ansible te dit **ce qu'il ferait**, **sans rien modifier** sur les machines.

```bash
ansible-playbook -i inventory.ini site.yml --syntax-check   # 1. la syntaxe est-elle bonne ?
ansible-playbook -i inventory.ini site.yml --check          # 2. qu'est-ce qui CHANGERAIT ?
ansible-playbook -i inventory.ini site.yml                  # 3. exécution réelle
```

> **L'enchaînement de prudence :** `--syntax-check` → `--check` → exécution réelle. Chaque étape attrape un type de problème différent, **avant** qu'il ne touche tes machines.

### Très utile en pratique

En mode `--check`, les tâches qui **modifieraient** quelque chose apparaissent en `changed` (mais **rien n'est réellement modifié**), et les autres en `ok`. C'est une **simulation**.

```bash
ansible-playbook -i inventory.ini site.yml --check
```

> ⚠️ **Bon à savoir :** `--check` est une **simulation très utile**, mais **pas parfaite**. Certains modules gèrent mal le mode simulation, et certains résultats dépendent de l'état réel au moment de l'exécution. Vois `--check` comme un **réflexe de prudence**, pas comme une garantie absolue.

### Exemple simple

```text
$ ansible-playbook -i inventory.ini site.yml --check
TASK [Installer nginx] ***
changed: [cible1]          ← en réalité, RIEN n'est installé : c'est une simulation
```

### 🧪 Lab vs production

> En **lab**, tu peux te permettre de lancer directement. Mais prends **dès maintenant** l'habitude de `--check` avant les actions importantes : c'est le réflexe qui, en **production**, t'évitera des catastrophes. Apprendre le bon geste en lab, c'est l'avoir acquis pour plus tard.

### ❌ Erreur classique

> **Lancer un playbook directement, sans jamais vérifier la syntaxe ni simuler.**

On écrit un playbook, on le lance, et une erreur d'indentation (ou pire, une action non voulue) se déclenche. Le réflexe correct : **`--syntax-check` systématique**, et **`--check`** avant toute action qui modifie des machines. Quelques secondes de vérification évitent bien des ennuis.

### Exercices

#### Guidé
Sur ton playbook nginx, lance d'abord `--syntax-check` (corrige les erreurs éventuelles), puis `--check` (observe ce qui *changerait*), puis l'exécution réelle. Compare la sortie `--check` et la sortie réelle.

#### Autonome
Modifie ton playbook (par exemple, ajoute l'installation d'un paquet supplémentaire) et lance `--check` **avant** d'exécuter. Vérifie que la simulation annonce bien le changement attendu, puis exécute pour de vrai.

#### Défi
Lance `--check` sur un playbook **déjà appliqué** (donc tout est déjà conforme). Que montre la simulation (`ok` partout ou `changed` ?) ? Explique ce que ça t'apprend sur l'état actuel de tes machines.

### ✅ Tu sais maintenant…

- Vérifier la syntaxe avec **`--syntax-check`** (instantané).
- Simuler avec **`--check`** : voir ce qui changerait **sans rien modifier**.
- L'enchaînement **`--syntax-check` → `--check` → exécution**.
- Que `--check` est **utile mais pas parfait** (réflexe de prudence, pas garantie).

---

### 🚩 Checkpoint — Fin de la Partie 4

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
