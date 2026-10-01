---
title: Partie 8 — Bonnes pratiques débutant
source: IT/08 Conteneurs & automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - index.md
---

> **Objectif de la partie :** acquérir les bons réflexes sans alourdir. Quelques habitudes simples qui font la différence entre un playbook fragile et un playbook fiable.

---


## Chapitre 8.1 — Lisibilité et modules dédiés

### Le minimum à savoir

Deux habitudes qui rendent tes playbooks **lisibles et fiables** :

1. **Nommer chaque tâche** avec un `name:` clair. Le nom apparaît dans la sortie : un playbook bien nommé **se lit comme une procédure**.
2. **Préférer les modules dédiés** à `command`/`shell` (rappel Partie 3). Un module dédié est idempotent et explicite.

```yaml
# ✅ BON : nommé, module dédié
- name: Installer nginx
  ansible.builtin.apt:
    name: nginx
    state: present

# ❌ MOINS BON : pas de nom, shell non idempotent
- ansible.builtin.shell: apt install -y nginx
```


### Très utile en pratique

Un playbook lisible, c'est :

- des `name:` qui décrivent **ce que fait** chaque tâche ;
- des modules dédiés plutôt que du `shell` ;
- une structure claire (un play par objectif).

C'est ce qui te permet, dans six mois, de **relire** ton playbook et de le comprendre — et à un collègue de le reprendre.

### Exemple simple

```yaml
- name: Configurer le serveur web
  hosts: web
  become: true
  tasks:
    - name: Installer nginx
      ansible.builtin.apt:
        name: nginx
        state: present

    - name: Démarrer et activer nginx
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: true
```


On **lit** ce playbook comme une recette.

### ❌ Erreur classique

> **Des tâches sans nom et des `shell` partout.**

Un playbook fait de tâches anonymes et de `shell` est illisible et fragile. Le réflexe correct : **nomme** chaque tâche, et **cherche le module dédié** avant de sortir `shell`.

### Exercices

#### Guidé
Reprends un de tes playbooks et vérifie que **chaque** tâche a un `name:` clair. Renomme celles qui sont vagues (« tâche 1 » → « Installer nginx »).

#### Autonome
Cherche dans tes playbooks un `command`/`shell` que tu pourrais remplacer par un module dédié. Réécris-le. Vérifie que le comportement est identique mais désormais idempotent.

#### Défi
Donne ton playbook à relire à quelqu'un (ou relis-le toi-même à voix haute). Est-ce qu'on **comprend** ce qu'il fait juste en lisant les `name:` ? Si non, améliore-les.

### ✅ Tu sais maintenant…

- **Nommer** chaque tâche pour la lisibilité.
- Préférer les **modules dédiés** à `command`/`shell`.
- Qu'un playbook lisible **se lit comme une procédure**.

---


## Chapitre 8.2 — Vérifier avant d'agir (`--check`, `--diff`)

### Le minimum à savoir

Tu connais déjà `--check` (Partie 4). Ajoute **`--diff`** : il **montre les changements** qu'Ansible ferait (les lignes modifiées d'un fichier, par exemple).

```bash
ansible-playbook -i inventory.ini site.yml --check --diff
```


- **`--check`** : simule (ne modifie rien).
- **`--diff`** : montre **le détail** de ce qui changerait.

Combinés, ils te donnent un **aperçu précis** avant d'agir.

### Très utile en pratique

`--diff` est particulièrement utile avec les **templates** et **`lineinfile`** : il t'affiche **exactement** les lignes ajoutées ou modifiées dans le fichier, avant que tu n'appliques.

```text
--- avant
+++ après
-PermitRootLogin yes
+PermitRootLogin no
```


### Exemple simple

```bash
ansible-playbook -i inventory.ini hardening.yml --check --diff
```

Tu **vois** ce qui changerait, sans rien toucher.

### 🔍 Réflexe diagnostic

> Avant d'appliquer une modification de config importante, lance **`--check --diff`**. Tu vois précisément ce qui va changer. Si le diff ne correspond pas à ce que tu attendais, **n'applique pas** : corrige d'abord.

### ❌ Erreur classique

> **Appliquer une modification de config sans regarder le diff.**

On modifie un fichier système (SSH, par exemple) sans vérifier, et on découvre un effet de bord après coup. Le réflexe correct : **`--check --diff`** avant d'appliquer toute modification de configuration sensible.

### Exercices

#### Guidé
Sur un playbook qui modifie un fichier (template ou `lineinfile`), lance `--check --diff`. Observe les lignes affichées (avant/après). Puis applique pour de vrai et compare.

#### Autonome
Modifie volontairement ton template, puis lance `--check --diff` : tu dois voir **uniquement** les lignes que tu as changées. Tu valides ainsi que ton changement est bien ciblé.

#### Défi
Lance `--check --diff` sur un playbook **déjà appliqué** (tout est conforme). Le diff doit être **vide** et tout en `ok`. Explique ce que ça t'apprend sur l'état de tes machines.

### ✅ Tu sais maintenant…

- Simuler avec **`--check`** et voir le détail avec **`--diff`**.
- Que `--diff` montre les **lignes** qui changeraient (utile pour templates/`lineinfile`).
- Le réflexe : **`--check --diff`** avant toute modif de config importante.

---


## Chapitre 8.3 — Cibler avec prudence (`--limit`)

### Le minimum à savoir

Quand tu lances un playbook, il s'applique à **tout** ce que vise `hosts:`. L'option **`--limit`** permet de **restreindre** à une machine ou un sous-groupe précis — un garde-fou très utile.

```bash
# Le playbook vise "web", mais on le limite à une seule machine
ansible-playbook -i inventory.ini site.yml --limit cible1
```


> **`--limit` est ton garde-fou de périmètre.** Il te permet de **tester sur une seule machine** avant d'appliquer à tout le groupe. Indispensable pour les actions importantes.

### Très utile en pratique

La bonne démarche pour une action importante :

```
1. --check --diff           (simuler, voir ce qui changerait)
2. --limit cible1           (appliquer à UNE machine d'abord)
3. vérifier que tout va bien sur cible1
4. lancer sur tout le groupe (sans --limit)
```


Tu valides sur une machine **témoin** avant de généraliser.

### Exemple simple

```bash
ansible-playbook -i inventory.ini site.yml --limit cible1   # une seule machine
ansible-playbook -i inventory.ini site.yml                  # tout le groupe
```


### 🧪 Lab vs production

> En **lab**, l'enjeu est faible. Mais prends l'habitude de `--limit` **dès maintenant** : en **production**, appliquer une action à tout un parc d'un coup sans l'avoir testée sur une machine témoin est **risqué**. Le bon geste appris en lab te protégera plus tard.

### ❌ Erreur classique

> **Lancer un playbook sur tout le parc sans l'avoir testé sur une seule machine.**

Une erreur dans le playbook se propage alors à **toutes** les machines d'un coup. Le réflexe correct : **`--limit` sur une machine témoin d'abord**, vérifier, **puis** généraliser. C'est rapide et ça évite les incidents en chaîne.

### Exercices

#### Guidé
Lance un de tes playbooks avec `--limit cible1`. Vérifie qu'il ne s'applique qu'à cette machine (l'autre n'apparaît pas dans la sortie). Puis relance sans `--limit` et observe qu'il touche tout le groupe.

#### Autonome
Adopte la démarche complète sur un playbook qui modifie quelque chose : `--check --diff`, puis `--limit cible1`, vérification, puis tout le groupe. Note chaque étape.

#### Défi
Combine `--limit` avec un groupe : si tu as un groupe `web` de plusieurs machines, limite à une seule d'entre elles. Réfléchis : en quoi `--limit` est-il un filet de sécurité complémentaire de `--check` ?

### ✅ Tu sais maintenant…

- Restreindre l'exécution avec **`--limit`** (une machine ou un sous-groupe).
- La démarche : **simuler → tester sur une machine témoin → généraliser**.
- Que `--limit` est un **garde-fou de périmètre** essentiel.

---


## Chapitre 8.4 — Hygiène de sécurité de base

### Le minimum à savoir

Quelques réflexes simples, sans transformer ce cours en cours de sécurité :

- **Protéger les clés SSH** : la clé privée reste sur le contrôle, ne se partage pas, ne se commite pas.
- **Pas de mot de passe en clair** dans les playbooks ou l'inventaire (on chiffrera avec Vault en Partie 9).
- **Séparer lab et production** : des inventaires distincts, pour ne jamais viser la prod en croyant viser le lab.
- **`become` au juste besoin** : root seulement là où c'est nécessaire.

### Très utile en pratique

> 🛡️ **Réflexe sécurité :** avant de versionner un projet (Git, Partie 10), demande-toi toujours : « y a-t-il un secret en clair là-dedans ? une clé privée ? un mot de passe ? ». Si oui, **ne commite pas** : chiffre d'abord (Vault) ou exclus le fichier.

### Exemple simple

Mauvais (mot de passe en clair) :

```yaml
vars:
  db_password: SuperSecret123    # ❌ JAMAIS en clair
```


Bon (on chiffrera ça avec Vault, Partie 9) :

```yaml
vars_files:
  - secrets.yml                  # ✅ fichier chiffré par Vault
```


### 🧪 Lab vs production

> En **lab**, tu peux te permettre des raccourcis (comme un mot de passe simple pour tester). Mais ne prends **jamais** l'habitude de mettre des secrets en clair, car ce réflexe te suivrait en production, où c'est dangereux.

### ❌ Erreur classique

> **Mettre un mot de passe en clair « juste pour tester », puis l'oublier et le versionner.**

« Je le chiffrerai plus tard » est la phrase qui mène à la fuite. Le réflexe correct : dès qu'il y a un secret, utilise **Vault** (Partie 9) ou exclus le fichier du dépôt. Ne laisse **jamais** un secret en clair traîner dans un projet.

### Exercices

#### Guidé
Vérifie tes playbooks et ton inventaire : y a-t-il un mot de passe ou un secret en clair ? Si oui, note-le — on le chiffrera en Partie 9.

#### Autonome
Crée deux inventaires distincts : `inventory_lab.ini` et `inventory_prod.ini` (même fictif). Explique pourquoi cette séparation est une bonne habitude.

#### Défi
Liste les fichiers de ton projet qui ne devraient **jamais** être partagés ou versionnés en clair (clé privée, secrets…). Tu prépares ainsi le `.gitignore` de la Partie 10.

### ✅ Tu sais maintenant…

- Protéger les **clés SSH** (privée secrète, jamais partagée).
- Ne **jamais** mettre de secret en clair (→ Vault, Partie 9).
- **Séparer** les inventaires lab et production.
- Utiliser **`become`** au juste besoin.

---

### 🚩 Checkpoint — Fin de la Partie 8

Tu as les bons réflexes de base. Avant Vault, assure-toi de pouvoir :

- [ ] **Nommer** tes tâches et préférer les **modules dédiés**.
- [ ] Vérifier avec **`--check --diff`** avant d'agir.
- [ ] Cibler avec **`--limit`** (machine témoin d'abord).
- [ ] Protéger les **clés SSH** et éviter les **secrets en clair**.

> Pas de nouveau mini-projet ici : applique ces réflexes à **tous** tes playbooks existants. Reprends-les, nomme les tâches, ajoute `--check --diff` à tes habitudes, teste avec `--limit`.

> **La suite :** en Partie 9, on apprend à gérer les **secrets** proprement avec **Ansible Vault** — pour ne plus jamais écrire un mot de passe en clair.

---
---
