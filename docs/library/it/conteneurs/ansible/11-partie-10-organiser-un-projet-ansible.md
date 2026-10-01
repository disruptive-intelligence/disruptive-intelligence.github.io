---
title: Partie 10 — Organiser un projet Ansible
source: IT/08 Conteneurs & automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - index.md
---

> **Objectif de la partie :** passer de petits playbooks éparpillés à un **projet propre**, structuré, versionné et documenté.

---


## Chapitre 10.1 — Une arborescence propre

### Le minimum à savoir

À mesure que ton projet grandit, il faut l'**organiser**. Voici une structure simple et standard :

```
mon-projet/
├── ansible.cfg            # configuration du projet
├── inventory.ini          # l'inventaire
├── group_vars/            # variables par groupe
│   ├── all.yml
│   └── web.yml
├── host_vars/             # variables par hôte
├── playbooks/             # les playbooks
│   └── site.yml
├── roles/                 # les roles (Partie 11)
├── templates/             # les templates Jinja2 (ou dans les roles)
├── README.md              # documentation
└── .gitignore             # fichiers à ne pas versionner
```


> **L'idée :** chaque chose à sa place. Inventaire, variables, playbooks, roles, templates sont rangés dans des dossiers prévisibles. N'importe qui (toi dans six mois, ou un collègue) **s'y retrouve**.

### Très utile en pratique

Tu n'as pas besoin de **tous** ces dossiers dès le début. Commence simple (inventaire + un playbook + `ansible.cfg`), et ajoute les dossiers (`group_vars`, `roles`…) **quand tu en as besoin**.

### Exemple simple

Un projet minimal mais propre :

```
mon-projet/
├── ansible.cfg
├── inventory.ini
└── playbooks/
    └── site.yml
```


### ❌ Erreur classique

> **Tout mettre dans un seul gros fichier, ou éparpiller les fichiers sans logique.**

Un projet désorganisé devient vite ingérable. Le réflexe correct : adopter une **structure standard** dès que le projet dépasse deux ou trois fichiers. Ça paraît superflu au début, mais ça paie très vite.

### Exercices

#### Guidé
Réorganise tes fichiers existants selon l'arborescence proposée : inventaire à la racine, playbooks dans `playbooks/`, variables dans `group_vars/`. Vérifie que tout fonctionne encore.

#### Autonome
Crée un dossier `templates/` et déplaces-y tes fichiers `.j2`. Ajuste les chemins `src:` si besoin. Lance un playbook pour vérifier que les templates sont toujours trouvés.

#### Défi
Dessine (ou écris) l'arborescence **idéale** pour ton projet actuel. Justifie l'emplacement de chaque type de fichier. En quoi cette organisation facilite-t-elle la reprise du projet par quelqu'un d'autre ?

### ✅ Tu sais maintenant…

- Organiser un projet selon une **arborescence standard**.
- Que chaque type de fichier a son **dossier** (inventaire, variables, playbooks, roles, templates).
- Commencer **simple** et ajouter les dossiers au besoin.

---


## Chapitre 10.2 — Le fichier `ansible.cfg`

### Le minimum à savoir

Depuis le début, tu tapes `-i inventory.ini` à chaque commande. Le fichier **`ansible.cfg`**, placé à la racine de ton projet, rassemble ces réglages **une fois pour toutes**.

```ini
# ansible.cfg
[defaults]
inventory = ./inventory.ini          # plus besoin de -i !
remote_user = admin                  # utilisateur SSH par défaut
private_key_file = ~/.ssh/id_ed25519 # clé privée à utiliser
host_key_checking = False            # pratique en lab (voir avertissement)
```


> **Avec `ansible.cfg`, les commandes raccourcissent :**
> ```bash
> # Avant :
> ansible web -i inventory.ini -u admin -m ansible.builtin.ping
> # Après :
> ansible web -m ansible.builtin.ping
> ```

### Très utile en pratique

```bash
# Vérifier quel ansible.cfg est utilisé
ansible --version       # affiche le chemin du fichier de config lu
```


Quand tu lances une commande depuis un dossier contenant un `ansible.cfg`, Ansible le lit **automatiquement**.

### Exemple simple

```ini
[defaults]
inventory = ./inventory.ini
remote_user = admin
```


Avec ça, `ansible all -m ansible.builtin.ping` fonctionne **sans** `-i` ni `-u`.

### 🧪 Lab vs production

> `host_key_checking = False` désactive une vérification de sécurité SSH. **En lab**, c'est commode (les VMs changent souvent). **En production**, garde cette vérification **active** : elle protège contre certaines attaques. Ne désactive ce réglage que pour un lab.

### ❌ Erreur classique

> **Croire qu'un réglage « ne marche pas », alors qu'un autre `ansible.cfg` est lu.**

Ansible peut trouver plusieurs fichiers de config. Si tu édites le mauvais, tes changements semblent ignorés. Le réflexe correct : lancer **`ansible --version`** pour voir **quel fichier est réellement utilisé**, et travailler avec un `ansible.cfg` **à la racine de ton projet**.

### Exercices

#### Guidé
Crée un `ansible.cfg` à la racine de ton projet avec `inventory`, `remote_user` et `private_key_file`. Lance une commande **sans** `-i` ni `-u` : elle doit fonctionner grâce au `ansible.cfg`. Vérifie avec `ansible --version` que c'est bien ton fichier qui est lu.

#### Autonome
Compare une commande **avant** (`-i ... -u ...`) et **après** (`ansible.cfg` en place). Mesure le confort gagné. Toutes tes commandes du cours peuvent-elles maintenant se passer de `-i` ?

#### Défi
Ajoute `host_key_checking = False` à ton `ansible.cfg` de lab. Explique en quelques lignes pourquoi ce réglage est pratique en lab mais **déconseillé** en production.

### ✅ Tu sais maintenant…

- Que **`ansible.cfg`** centralise la configuration (inventaire, utilisateur, clé).
- Qu'il évite de répéter **`-i`** et **`-u`** à chaque commande.
- Vérifier quel fichier est lu avec **`ansible --version`**.
- Que `host_key_checking = False` est un réglage **de lab**.

---


## Chapitre 10.3 — Git, `.gitignore` et documentation

### Le minimum à savoir

Un projet Ansible devrait être dans **Git** : historique des changements, retour arrière, travail à plusieurs. Mais attention aux **secrets**.

```gitignore
# .gitignore
*.retry
.vault_pass          # le mot de passe Vault, JAMAIS dans Git
```


> 🛡️ **Réflexe sécurité :** le `.gitignore` empêche de versionner les fichiers sensibles. Exclus tout fichier de **mot de passe Vault** et toute **clé privée**. Les fichiers **chiffrés par Vault**, eux, peuvent être versionnés (ils sont illisibles sans la clé).

#### Documenter avec un README

Un fichier **`README.md`** explique le projet : à quoi il sert, comment l'utiliser, comment lancer les playbooks. Un projet sans documentation est difficile à reprendre.

### Très utile en pratique

```bash
git init
git add .
git status              # VÉRIFIER qu'aucun secret en clair n'est suivi !
git commit -m "Projet Ansible : inventaire, playbooks, role common"
```


> 🔍 **Réflexe diagnostic / sécurité :** avant **chaque** commit, lance `git status` et **vérifie** qu'aucun fichier sensible (secret en clair, clé privée) n'est sur le point d'être versionné.

### Exemple simple

Un `README.md` minimal :

```markdown
# Mon projet Ansible

Administration des serveurs web.

## Utilisation
ansible-playbook playbooks/site.yml --ask-vault-pass
```


### ❌ Erreur classique

> **Commiter une clé privée ou un secret en clair par mégarde.**

Un `git add .` un peu rapide, et un secret part dans l'historique. Le réflexe correct : un **`.gitignore`** solide **dès le début**, et un **`git status`** systématique avant chaque commit. Un secret déjà poussé doit être considéré comme **compromis** (le changer, pas juste le retirer).

### Exercices

#### Guidé
Initialise Git dans ton projet. Crée un `.gitignore` excluant `.vault_pass` et les clés privées. Fais un premier commit après avoir vérifié `git status`. Confirme qu'aucun secret n'est suivi.

#### Autonome
Rédige un `README.md` pour ton projet : à quoi il sert, comment lancer le playbook principal, quels prérequis. Place-le à la racine et commite-le.

#### Défi
Structure ton projet complet (arborescence + `ansible.cfg` + `.gitignore` + README) et fais un commit propre. Vérifie que tes fichiers Vault chiffrés sont bien versionnés (c'est voulu) mais qu'aucun secret en clair ne l'est.

### ✅ Tu sais maintenant…

- Versionner un projet avec **Git**.
- Protéger les secrets avec un **`.gitignore`** (mot de passe Vault, clés privées).
- Que les fichiers **chiffrés par Vault** peuvent être versionnés.
- Documenter avec un **`README.md`**.
- Vérifier **`git status`** avant chaque commit.

---

### 🚩 Checkpoint — Fin de la Partie 10

Ton projet est maintenant organisé. Avant les roles, assure-toi de pouvoir :

- [ ] Organiser un projet selon une **arborescence standard**.
- [ ] Utiliser un **`ansible.cfg`** (fini les `-i` répétés).
- [ ] Versionner avec **Git** et protéger les secrets avec **`.gitignore`**.
- [ ] Documenter avec un **README**.

> **🧩 Mini-projet 11 — « Organiser un mini-projet Ansible propre ».**
> Structure ton projet : `ansible.cfg`, inventaire, `group_vars`, dossier `playbooks/`, README, `.gitignore`. Initialise Git et fais un commit propre (après `git status`). Tu as maintenant un projet réutilisable et partageable.

> **La suite :** en Partie 11, on découvre les **roles** : comment regrouper et réutiliser ton code proprement, sans aller trop loin.

---
---
