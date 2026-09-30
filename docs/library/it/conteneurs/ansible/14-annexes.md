---
title: Annexes
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
up:
- - Ansible
  - index.md
---

> Annexes courtes, pour référence rapide.

---

## Annexe A — Cheat-sheet des commandes

```bash
# --- Inventaire ---
ansible-inventory -i inventory.ini --graph        # voir l'inventaire en arbre
ansible-inventory -i inventory.ini --host cible1  # variables d'un hôte

# --- Commandes ad hoc ---
ansible all -i inventory.ini -m ansible.builtin.ping
ansible web -i inventory.ini -m ansible.builtin.command -a "uptime"
ansible web -i inventory.ini -m ansible.builtin.apt -a "name=htop state=present" --become

# --- Playbooks ---
ansible-playbook -i inventory.ini site.yml --syntax-check   # vérifier la syntaxe
ansible-playbook -i inventory.ini site.yml --check --diff   # simuler + voir les changements
ansible-playbook -i inventory.ini site.yml --limit cible1   # une seule machine
ansible-playbook -i inventory.ini site.yml                  # exécuter

# --- Vault ---
ansible-vault create secrets.yml                  # créer un fichier chiffré
ansible-vault edit secrets.yml                    # éditer
ansible-vault view secrets.yml                    # afficher
ansible-playbook -i inventory.ini site.yml --ask-vault-pass

# --- Roles ---
ansible-galaxy role init roles/common             # créer la structure d'un role
```


---

## Annexe B — Erreurs fréquentes

| Symptôme | Cause probable | Solution |
|----------|----------------|----------|
| `UNREACHABLE` | Problème SSH (clé, user, réseau) | Tester `ssh user@cible` à la main |
| `FAILED` + « Permission denied » | `become` manquant | Ajouter `become: true` |
| Toujours `changed` au 2e passage | Abus de `command`/`shell` | Utiliser un module dédié |
| Variable inattendue | Question de priorité | `ansible-inventory --host` |
| YAML refusé | Indentation (tabs/espaces) | `--syntax-check`, vérifier les espaces |
| « no vault secrets found » | Mot de passe Vault non fourni | Ajouter `--ask-vault-pass` |
| Tâche `skipped` | Condition `when` non remplie | Normal (pas une erreur) |

---

## Annexe C — Rappel YAML

```yaml
# Clé : valeur
nom: serveur1
actif: true

# Liste (tirets)
paquets:
  - nginx
  - git

# Dictionnaire imbriqué (indentation = hiérarchie)
serveur:
  nom: web1
  ip: 192.168.56.11
```


**Règles d'or :** indentation par **espaces** (jamais de tabs), **2 espaces** par niveau, cohérence dans tout le fichier. Une valeur commençant par `{{` se met **entre guillemets**.

---

## Annexe D — Rappel SSH

```bash
ssh-keygen -t ed25519               # générer une paire de clés (sur le contrôle)
ssh-copy-id utilisateur@cible       # déposer la clé publique sur une cible
ssh utilisateur@cible               # tester la connexion (doit être sans mot de passe)
ssh -v utilisateur@cible            # mode verbeux pour diagnostiquer
```


**Règle d'or :** SSH doit fonctionner **à la main** avant qu'Ansible ne fonctionne. Au moindre souci Ansible au début, teste `ssh` d'abord.

---

## Annexe E — Ansible vs Terraform / Docker / Kubernetes

| Outil | Rôle |
|-------|------|
| **Ansible** | **Configurer** des machines existantes |
| **Terraform** | **Provisionner / créer** l'infrastructure |
| **Docker** | **Packager** une application en conteneur |
| **Kubernetes** | **Orchestrer** des conteneurs |

Outils **complémentaires** : Terraform crée → Ansible configure → Docker/Kubernetes font tourner les apps. Ce cours reste centré sur **Ansible**.

---

## Annexe F — Roadmap après le cours

Une fois ce cours maîtrisé, tu peux explorer (dans l'ordre qui te convient) :

- **AWX / Ansible Automation Platform** : interface web, planification, logs centralisés.
- **Terraform** : créer l'infrastructure (complément d'Ansible).
- **CI/CD** : tester et déployer automatiquement tes playbooks.
- **Kubernetes** : orchestration de conteneurs.
- **Durcissement avancé** (hardening) : baselines de sécurité complètes.

Ces sujets dépassent le cadre de ce cours débutant, mais Ansible est une excellente base pour les aborder.

---

## 🎓 Mot de la fin

Tu es parti de zéro, et tu sais maintenant **automatiser l'administration de machines Linux** avec Ansible.

Tu as appris, pas à pas :

- à **comprendre** Ansible (l'état souhaité, l'idempotence) avant de l'utiliser ;
- à monter un **lab** et te connecter en **SSH par clé** ;
- à décrire ton parc avec un **inventaire** et à agir en **commandes ad hoc** ;
- à **lire les sorties** (`ok`, `changed`, `failed`, `skipped`, `unreachable`) ;
- à écrire des **playbooks** lisibles et rejouables ;
- à utiliser les **modules** essentiels (paquets, services, fichiers, utilisateurs) ;
- à rendre tes playbooks **adaptables** (variables, facts, conditions, boucles) ;
- à générer de la config avec **templates** et à redémarrer proprement avec **handlers** ;
- à protéger tes secrets avec **Vault** ;
- à **organiser** un projet et créer un **role** simple.

Garde en tête les réflexes qui font la différence : **comprendre l'état souhaité**, **lire les sorties**, **préférer les modules dédiés**, **vérifier avant d'agir** (`--check`, `--limit`), et **ne jamais laisser un secret en clair**.

La suite t'appartient : approfondis avec AWX, Terraform ou le durcissement, ou continue simplement à automatiser ton propre parc. Tu as maintenant le **socle**.

**Bon courage, et bonne automatisation. 🚀**

---
