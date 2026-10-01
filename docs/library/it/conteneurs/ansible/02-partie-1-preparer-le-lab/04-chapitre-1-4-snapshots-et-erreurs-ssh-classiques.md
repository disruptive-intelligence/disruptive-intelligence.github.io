---
title: Chapitre 1.4 — Snapshots et erreurs SSH classiques
source: IT/08 Conteneurs & automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 1 — Préparer le lab
  - index.md
---

## Le minimum à savoir

Avant de commencer à « casser » des choses en apprenant, mets en place ton **filet de sécurité** : les **snapshots**.

Un **snapshot** (instantané) est une **photo** de l'état d'une VM à un moment donné. Si un essai casse une cible, tu **restaures** le snapshot et tu repars de l'état sain en quelques secondes. VirtualBox et VMware proposent tous les deux cette fonction.

> 🧪 **Lab vs production :** en lab, les snapshots te donnent une **liberté totale** d'expérimenter. Tu tentes, tu observes, et si ça tourne mal, tu restaures. C'est exactement ce qui rend l'apprentissage **serein**. (En production, on n'a pas ce confort — d'où l'importance d'apprendre **maintenant**, en lab.)

### Les erreurs SSH les plus fréquentes

Comme Ansible passe par SSH, les premiers blocages viennent presque toujours de là :

| Message / symptôme | Cause probable | Quoi vérifier |
|--------------------|----------------|---------------|
| `Permission denied` | Mauvaise clé ou mauvais utilisateur | La clé publique est-elle déposée ? Bon utilisateur ? |
| `Connection refused` / timeout | Cible éteinte, mauvaise IP, réseau | La VM tourne ? La bonne IP ? Même réseau ? |
| Demande de mot de passe | Clé publique pas déposée | Refaire `ssh-copy-id` |
| `Host key verification failed` | Clé d'hôte changée (VM recréée) | Nettoyer l'ancienne entrée `known_hosts` |

## Très utile en pratique

```bash
# Tester la connexion à la main (TOUJOURS le premier réflexe)
ssh admin@192.168.56.11

# Voir plus de détails si ça échoue (verbeux)
ssh -v admin@192.168.56.11
```


> 🔍 **Réflexe diagnostic :** au moindre souci avec Ansible **au début du cours**, reviens à `ssh utilisateur@cible` à la main. Si ça échoue, le problème est dans **SSH/le réseau**, pas dans Ansible. Règle SSH d'abord.

## Exemple simple

Le bon ordre des opérations pour un lab sain :

```text
1. Les 3 VMs démarrent et se voient sur le réseau
2. SSH par clé fonctionne du contrôle vers chaque cible (testé à la main)
3. SNAPSHOT de chaque VM, nommé "lab-pret"   ← ton point de restauration
```


## ❌ Erreur classique

> **Monter un lab « presque bon » : pas de snapshot, réseau bancal, et chercher des bugs Ansible qui sont en réalité des bugs réseau.**

Sans snapshot, le moindre essai raté t'oblige à tout refaire. Et un réseau mal configuré transforme chaque exercice en chasse au bug qui n'a **rien à voir** avec Ansible. Le réflexe correct : **valider SSH à la main** sur chaque cible, **puis** prendre un snapshot « lab-pret » avant de continuer. Trente secondes de préparation t'épargnent des heures de frustration.

## Exercices

### Guidé
Une fois que SSH par clé fonctionne vers tes deux cibles, prends un **snapshot** de chaque VM (contrôle + cibles), nommé « lab-pret ». Tu viens de créer ton point de restauration.

### Autonome
Casse volontairement quelque chose sur une cible (par exemple, supprime la clé publique déposée, ou éteins la VM) et observe l'échec de `ssh`. Puis **restaure le snapshot** « lab-pret » et vérifie que la connexion refonctionne. Tu viens de tester ton filet de sécurité.

### Défi
Provoque une erreur `Host key verification failed` : recrée (ou réinitialise) une cible après t'y être déjà connecté, puis retente `ssh`. Lis le message. Sans forcément le résoudre, explique **pourquoi** SSH se méfie quand la clé d'hôte change (indice : c'est une protection de sécurité).

## ✅ Tu sais maintenant…

- Ce qu'est un **snapshot** et pourquoi il rend l'apprentissage **serein**.
- À prendre un snapshot **« lab-pret »** une fois SSH validé.
- Les **erreurs SSH** les plus fréquentes et quoi vérifier pour chacune.
- Le réflexe : au moindre souci, **tester `ssh` à la main d'abord**.

---

## 🚩 Checkpoint — Fin de la Partie 1

Ton lab est prêt. Avant de décrire ton parc et d'agir avec Ansible, assure-toi de pouvoir :

- [ ] Expliquer la différence **machine de contrôle** / **cibles**, et le principe **agentless**.
- [ ] Avoir **Ansible installé** sur la machine de contrôle (`ansible --version` répond).
- [ ] Te connecter en **SSH par clé** (sans mot de passe) à **chaque** cible.
- [ ] Comprendre que **SSH doit marcher avant Ansible**.
- [ ] Avoir pris un **snapshot « lab-pret »** de chaque VM.
- [ ] Reconnaître les **erreurs SSH** courantes et savoir tester `ssh` à la main.

> **🧩 Mini-projet 1 — « Le lab opérationnel ».**
> 1. Crée tes VMs : une machine de contrôle (avec Ansible) et deux cibles Linux, sur un réseau commun.
> 2. Génère une paire de clés sur le contrôle et dépose la clé publique sur **chaque** cible.
> 3. Vérifie `ssh utilisateur@cible` **sans mot de passe** vers les deux cibles.
> 4. Prends un **snapshot « lab-pret »** de chaque VM.
> Objectif : disposer d'un lab **fiable**, prêt pour la suite, avec le réflexe « je valide SSH à la main avant Ansible ».

> **La suite :** en Partie 2, on décrit nos machines dans un **inventaire**, et on lance nos **premières commandes ad hoc** avec Ansible — enfin de l'action ! On apprendra aussi à lire les premières **sorties** (`ok`, `changed`, `failed`, `skipped`, `unreachable`).

---
---
---
