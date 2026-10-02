---
title: Chapitre 1.2 — SSH et clés
source: IT/08 Conteneurs & automatisation/Automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 1 — Préparer le lab
  - index.md
---

## Le minimum à savoir

Ansible n'a pas de « canal magique ». Il utilise **SSH**, exactement le même que celui que tu utilises pour te connecter à un serveur à la main. **C'est la fondation de tout le cours.**

La règle d'or :

> **Si `ssh utilisateur@cible` marche à la main, alors Ansible marchera. Si SSH ne marche pas, Ansible ne marchera pas non plus.** SSH d'abord, Ansible ensuite.

### Mot de passe ou clé ?

On peut se connecter en SSH par **mot de passe**, mais pour Ansible (et pour le confort), on utilise des **clés SSH**. Une clé SSH, c'est une **paire** :

- une **clé privée**, qui reste **secrète** sur la machine de contrôle ;
- une **clé publique**, qu'on **dépose** sur chaque cible.

Une fois la clé publique déposée, tu te connectes **sans taper de mot de passe** : la cible reconnaît ta clé.

```
   MACHINE DE CONTRÔLE                 CIBLE
   ┌──────────────────┐                ┌──────────────────┐
   │  clé PRIVÉE      │ ── prouve ───▶ │  clé PUBLIQUE    │
   │  (reste secrète) │   l'identité   │  (déposée ici)   │
   └──────────────────┘                └──────────────────┘
```


## Très utile en pratique

Les trois commandes à connaître (sur la **machine de contrôle**) :

```bash
# 1. Générer une paire de clés (si tu n'en as pas déjà)
ssh-keygen -t ed25519

# 2. Déposer la clé publique sur une cible
ssh-copy-id utilisateur@192.168.56.11

# 3. Vérifier qu'on se connecte SANS mot de passe
ssh utilisateur@192.168.56.11
```


Si la troisième commande t'ouvre une session **sans demander de mot de passe**, tout est prêt pour Ansible.

```text
$ ssh admin@192.168.56.11
Welcome to Ubuntu ...
admin@cible1:~$        ← connecté sans mot de passe : parfait
```


## Exemple simple

Tu génères ta clé une fois, puis tu la déposes sur chaque cible :

```bash
ssh-keygen -t ed25519                       # une seule fois, sur le contrôle
ssh-copy-id admin@192.168.56.11             # cible1
ssh-copy-id admin@192.168.56.12             # cible2
ssh admin@192.168.56.11                     # test : doit marcher sans mot de passe
```


## 🛡️ Réflexe sécurité

> La **clé privée** reste sur la machine de contrôle et **ne se partage jamais**. C'est elle qui ouvre l'accès à tes cibles. Traite-la comme un trousseau de clés : on ne le laisse pas traîner, on ne l'envoie pas par mail. (On reparlera de protéger les secrets en Partie 9.)

## ❌ Erreur classique

> **Essayer de faire marcher Ansible alors que SSH ne marche pas encore à la main.**

C'est **l'**erreur n°1 du débutant. On lance Ansible, ça échoue, et on cherche le problème dans Ansible… alors qu'il est dans **SSH** (mauvaise clé, mauvais utilisateur, machine pas joignable). Le réflexe correct : **toujours tester `ssh utilisateur@cible` à la main d'abord**. Si la connexion manuelle échoue, Ansible échouera aussi — Ansible ne **répare** pas SSH, il s'**appuie** dessus.

## Exercices

### Guidé
Sur ta machine de contrôle, génère une paire de clés avec `ssh-keygen -t ed25519`. Dépose la clé publique sur **une** cible avec `ssh-copy-id`. Connecte-toi ensuite avec `ssh utilisateur@cible` et vérifie que **tu n'as pas à taper de mot de passe**.

### Autonome
Explique avec tes mots la différence entre la **clé privée** et la **clé publique** : laquelle reste secrète, laquelle se distribue, et pourquoi ce système permet de se connecter sans mot de passe.

### Défi
Fais le test sur la **deuxième** cible. Puis, depuis la machine de contrôle, connecte-toi successivement aux deux cibles. Si l'une demande un mot de passe et pas l'autre, trouve **pourquoi** (la clé publique a-t-elle bien été déposée sur les deux ?).

## ✅ Tu sais maintenant…

- Qu'Ansible utilise **SSH**, et que **SSH doit marcher avant Ansible**.
- Le principe d'une **paire de clés** : privée (secrète, sur le contrôle) / publique (déposée sur les cibles).
- Générer et déposer une clé : `ssh-keygen`, `ssh-copy-id`, test avec `ssh`.
- Que la **clé privée** ne se partage jamais.

---
