---
title: Partie 9 — Ansible vault et secrets
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
up:
- - Ansible
  - index.md
---

> **Objectif de la partie :** gérer les secrets (mots de passe, clés) **sans** les écrire en clair, grâce à Ansible Vault.

---


## Chapitre 9.1 — Pourquoi ne pas mettre de secret en clair

### Le minimum à savoir

Tes playbooks ont parfois besoin de **secrets** : un mot de passe, une clé d'API. Les écrire **en clair** est une **mauvaise pratique** :

- N'importe qui ayant accès au fichier les **lit**.
- Si tu versionnes ton projet (Git), ils se retrouvent dans l'**historique** — et un secret poussé dans Git est **compromis**, même si tu le retires ensuite.

> **La règle :** **aucun secret en clair, jamais.** Et surtout pas dans un dépôt Git. C'est exactement pour ça qu'Ansible Vault existe.

### Très utile en pratique

Un secret peut traîner dans :

- une variable de playbook (`db_password: ...`) ;
- un fichier de variables (`group_vars/...`) ;
- l'inventaire.

Partout où il y a un secret, il faut le **chiffrer** avec Vault.

### Exemple simple

À éviter absolument :

```yaml
vars:
  db_password: SuperSecret123    # ❌ lisible par tous, versionné dans Git
```


### ❌ Erreur classique

> **« Je mettrai le mot de passe en clair maintenant, je sécuriserai plus tard. »**

Le « plus tard » n'arrive jamais, et le secret finit dans Git. Le réflexe correct : **chiffrer dès le premier secret**. Ne laisse jamais un secret en clair, même temporairement, dans un projet versionné.

### Exercices

#### Guidé
Cherche dans tes playbooks et ton inventaire s'il y a un secret en clair (même fictif). Note-le : on va le chiffrer au chapitre suivant.

#### Autonome
Explique en 3-4 phrases pourquoi un secret poussé dans Git est considéré comme **compromis**, même après l'avoir retiré du fichier.

#### Défi
Imagine les conséquences concrètes d'un mot de passe de base de données versionné en clair dans un dépôt partagé. Qui pourrait y accéder ? Pourquoi est-ce difficile à rattraper ?

### ✅ Tu sais maintenant…

- Pourquoi un secret en clair est une **faute** (lisible, versionné, compromis à vie).
- Qu'il ne faut **jamais** mettre de secret en clair, surtout dans Git.
- Que la solution est de **chiffrer** avec Ansible Vault.

---


## Chapitre 9.2 — Chiffrer avec Ansible Vault

### Le minimum à savoir

**Ansible Vault** chiffre tes secrets. Le fichier devient illisible sans le mot de passe Vault, mais reste **utilisable** par Ansible à l'exécution.

```bash
# Créer un fichier chiffré
ansible-vault create secrets.yml

# Éditer un fichier chiffré (demande le mot de passe Vault)
ansible-vault edit secrets.yml

# Afficher le contenu (sans le déchiffrer sur le disque)
ansible-vault view secrets.yml

# Chiffrer un fichier existant
ansible-vault encrypt group_vars/web/secrets.yml
```


Un fichier chiffré ressemble à ça — **illisible**, donc **versionnable sans danger** :

```text
$ANSIBLE_VAULT;1.1;AES256
66386439653...   (contenu chiffré)
```


### Très utile en pratique

Quand tu crées un fichier Vault, Ansible te demande un **mot de passe Vault**. Ce mot de passe te sera redemandé pour lire ou utiliser le fichier. Choisis-en un solide, et **ne le mets jamais dans le projet**.

### Exemple simple

```bash
ansible-vault create secrets.yml
# Ansible demande un mot de passe, puis ouvre un éditeur.
# Tu écris :  db_password: SuperSecret123
# Tu sauvegardes : le fichier est chiffré.
```


```bash
cat secrets.yml      # → contenu chiffré, illisible
```


### ❌ Erreur classique

> **Oublier son mot de passe Vault.**

Sans le mot de passe, **personne** ne peut déchiffrer le fichier — c'est le but du chiffrement. Le réflexe correct : conserver le mot de passe Vault dans un **gestionnaire de mots de passe**, jamais dans le projet. Le perdre, c'est perdre l'accès aux secrets.

### Exercices

#### Guidé
Crée un fichier chiffré avec `ansible-vault create secrets.yml` contenant une variable `db_password`. Vérifie avec `cat secrets.yml` que le contenu est **illisible**. Ouvre-le avec `ansible-vault view` pour confirmer que tu peux le lire avec le mot de passe.

#### Autonome
Édite le fichier avec `ansible-vault edit secrets.yml` et ajoute une seconde variable. Sauvegarde et vérifie qu'il reste chiffré. Tu maîtrises le cycle créer/éditer/voir.

#### Défi
Crée un fichier de variables **en clair**, puis chiffre-le avec `ansible-vault encrypt`. Vérifie qu'il est devenu illisible. Dans quel cas cette commande (`encrypt`) est-elle utile par rapport à `create` ?

### ✅ Tu sais maintenant…

- Chiffrer des secrets avec **`ansible-vault`** (`create`, `edit`, `view`, `encrypt`).
- Qu'un fichier Vault est **illisible** sans le mot de passe (donc versionnable).
- Qu'il faut **conserver précieusement** le mot de passe Vault (hors du projet).

---


## Chapitre 9.3 — Utiliser un secret chiffré

### Le minimum à savoir

Une fois ton secret chiffré, tu l'utilises dans un playbook **comme une variable normale**. Ansible le déchiffre à la volée au moment de l'exécution.

```yaml
# secrets.yml (chiffré) contient :  db_password: SuperSecret123

- name: Configurer la base de données
  hosts: db
  vars_files:
    - secrets.yml            # ← charge le fichier chiffré
  tasks:
    - name: Afficher (pour l'exemple) que le secret est disponible
      ansible.builtin.debug:
        msg: "Le mot de passe est chargé (longueur : {{ db_password | length }})"
```


Pour lancer un playbook qui utilise des secrets Vault, il faut **fournir le mot de passe** :

```bash
ansible-playbook -i inventory.ini site.yml --ask-vault-pass
```


`--ask-vault-pass` demande le mot de passe Vault au lancement.

### Très utile en pratique

L'organisation propre : séparer les variables **normales** des variables **secrètes**.

```
group_vars/
└── web/
    ├── vars.yml        # variables NORMALES (en clair, versionnées)
    └── vault.yml       # variables SECRÈTES (chiffrées par Vault)
```


Ansible charge **automatiquement** les deux pour le groupe `web`. Les secrets sont chiffrés, le reste reste lisible.

### Exemple simple

```bash
ansible-playbook -i inventory.ini site.yml --ask-vault-pass
# → Ansible demande le mot de passe Vault, puis déchiffre les secrets à la volée
```


### 🔍 Réflexe diagnostic

> Une erreur **« Attempting to decrypt but no vault secrets found »** signifie que tu as **oublié `--ask-vault-pass`** (ou le fichier de mot de passe). Ansible a trouvé du contenu chiffré mais n'a pas la clé pour le lire. Ajoute `--ask-vault-pass`.

### ❌ Erreur classique

> **Lancer un playbook avec des secrets Vault sans fournir le mot de passe.**

Sans `--ask-vault-pass`, Ansible ne peut pas déchiffrer et s'arrête en erreur. Le réflexe correct : dès qu'un playbook utilise un fichier Vault, **ajoute `--ask-vault-pass`** au lancement.

### Exercices

#### Guidé
Utilise la variable `db_password` (chiffrée au chapitre précédent) dans un playbook, via `vars_files: - secrets.yml`. Lance avec `--ask-vault-pass` et vérifie que ça fonctionne. Puis lance **sans** `--ask-vault-pass` et observe l'erreur.

#### Autonome
Organise tes variables en `vars.yml` (clair) et `vault.yml` (chiffré) dans un `group_vars`. Place une variable normale dans l'un, un secret dans l'autre. Lance un playbook qui utilise les deux.

#### Défi
Explique en quelques lignes pourquoi la **séparation** vars.yml / vault.yml est meilleure que de tout chiffrer (on perd en lisibilité) ou de tout laisser en clair (on perd les secrets). Quel équilibre apporte-t-elle ?

### ✅ Tu sais maintenant…

- Utiliser un secret chiffré comme une **variable normale** (`vars_files`).
- Fournir le mot de passe Vault avec **`--ask-vault-pass`**.
- Séparer **`vars.yml`** (clair) et **`vault.yml`** (chiffré).
- Reconnaître l'erreur « no vault secrets found ».

---

### 🚩 Checkpoint — Fin de la Partie 9

Tu sais gérer les secrets proprement. Avant d'organiser un vrai projet, assure-toi de pouvoir :

- [ ] Expliquer pourquoi un secret en clair (surtout dans Git) est une **faute**.
- [ ] Chiffrer un secret avec **`ansible-vault`** (`create`, `edit`, `view`).
- [ ] Utiliser un secret chiffré dans un playbook (`vars_files`, `--ask-vault-pass`).
- [ ] Séparer variables normales (`vars.yml`) et secrètes (`vault.yml`).

> **🧩 Mini-projet 10 — « Chiffrer une variable avec Vault ».**
> Crée un fichier `vault.yml` chiffré contenant un mot de passe. Utilise-le dans un playbook (par exemple pour configurer un fichier via template). Lance avec `--ask-vault-pass`. Vérifie qu'aucun secret n'apparaît en clair dans tes fichiers non chiffrés.

> **La suite :** en Partie 10, on passe de playbooks isolés à un **projet Ansible organisé** : arborescence, `ansible.cfg`, Git et documentation.

---
---
