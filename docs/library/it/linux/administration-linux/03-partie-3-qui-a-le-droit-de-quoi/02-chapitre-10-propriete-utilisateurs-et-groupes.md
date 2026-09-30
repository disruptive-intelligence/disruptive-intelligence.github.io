---
title: Chapitre 10 — Propriété, utilisateurs et groupes
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 3 — Qui a le droit de quoi
  - index.md
---

## Le minimum à savoir

### L'identité sur un système Linux

Les permissions du chapitre 9 reposent sur une question : **qui es-tu ?** Sous Linux, chaque utilisateur a une identité numérique (un **UID**, *user ID*) et appartient à un ou plusieurs **groupes** (chacun avec un **GID**, *group ID*). Le système ne raisonne pas vraiment avec les noms (`alice`), mais avec ces numéros ; les noms sont là pour nous, humains.

```bash
id               # affiche TON identité : uid, gid, et tous tes groupes
whoami           # affiche juste ton nom d'utilisateur
groups           # affiche les groupes auxquels tu appartiens
```


Un exemple de sortie de `id` :

```
uid=1000(alice) gid=1000(alice) groups=1000(alice),27(sudo),100(users)
```


On y lit : alice a l'UID 1000, son groupe principal est `alice`, et elle appartient aussi aux groupes `sudo` (important : il donne le droit d'administrer !) et `users`.

### root : le super-utilisateur

Un compte est à part : **root**, l'administrateur. Son UID est **0**, et il **ignore les permissions** : root peut tout lire, tout modifier, tout supprimer. C'est à la fois indispensable (pour administrer) et dangereux (une erreur en root peut détruire le système). On verra au chapitre 11 comment utiliser ce pouvoir proprement, sans rester connecté en root en permanence.

### Où sont stockés les comptes ? Trois fichiers clés

Toute l'information sur les utilisateurs vit dans trois fichiers texte. **Savoir les lire est un réflexe d'audit fondamental.**

```bash
cat /etc/passwd          # la liste des comptes (lisible par tous)
cat /etc/group           # la liste des groupes
sudo cat /etc/shadow     # les mots de passe (chiffrés) — accès root uniquement
```


- **`/etc/passwd`** : une ligne par compte. Malgré son nom, il ne contient **pas** les mots de passe (historiquement oui, plus aujourd'hui). Chaque ligne, séparée par des `:`, donne le nom, l'UID, le GID, le dossier personnel, le shell…

  ```
  alice:x:1000:1000:Alice Martin:/home/alice:/bin/bash
  ```


- **`/etc/group`** : les groupes et leurs membres.
- **`/etc/shadow`** : les **empreintes chiffrées** des mots de passe. Lisible uniquement par root — c'est une protection essentielle.

> **Très utile en sécurité :** lire `/etc/passwd` est l'un des premiers gestes d'un audit. On y repère les comptes existants, ceux qui ont un vrai shell de connexion (`/bin/bash`) versus ceux qui n'en ont pas (`/usr/sbin/nologin`, typiques des comptes de service), et tout compte suspect ajouté par un intrus. La première colonne (`cut -d: -f1 /etc/passwd`, vu au chapitre 4) liste tous les comptes.

## Très utile en pratique

### Changer le propriétaire : `chown` et `chgrp`

Quand un fichier doit appartenir à quelqu'un d'autre (ou à un autre groupe), on utilise `chown` (*change owner*) :

```bash
sudo chown alice fichier.txt          # alice devient propriétaire
sudo chown alice:equipe fichier.txt   # propriétaire alice, groupe equipe
sudo chgrp equipe fichier.txt         # change seulement le groupe
```


Ces commandes nécessitent en général `sudo` : changer la propriété d'un fichier est une opération privilégiée.

> **Souviens-toi de la Partie 0 :** `chown -R` et `chmod -R` (récursifs) figurent dans les commandes dangereuses. Appliqués au mauvais dossier, ils peuvent rendre tout un pan du système inaccessible. Vérifie **toujours** le chemin avant un `-R`.

### Créer un utilisateur

Sur Debian/Ubuntu, le plus simple est `adduser`, un assistant interactif qui crée le compte, son dossier personnel et demande le mot de passe :

```bash
sudo adduser bob         # assistant guidé (recommandé sur Debian/Ubuntu)
```


Il existe aussi `useradd`, plus bas niveau et plus universel, mais moins convivial (il ne crée pas le dossier personnel sans options) :

```bash
sudo useradd -m -s /bin/bash bob     # -m crée le /home, -s définit le shell
sudo passwd bob                      # définit ensuite son mot de passe
```


### Gérer les mots de passe et les groupes

```bash
passwd                   # change TON propre mot de passe
sudo passwd bob          # change le mot de passe de bob (en admin)
sudo usermod -aG sudo bob   # ajoute bob au groupe "sudo" (-aG = append to Group)
```


> **L'option `-aG` est cruciale et piégeuse :** le `-a` (*append*, ajouter) est **obligatoire**. Sans lui, `usermod -G` **remplace** tous les groupes de l'utilisateur par celui indiqué, le retirant de tous les autres. Oublier le `-a` est une erreur classique qui peut, par exemple, retirer quelqu'un du groupe `sudo` sans le vouloir.

### Changer d'identité : `su`

`su` (*substitute user*) permet de devenir un autre utilisateur le temps d'une session :

```bash
su - bob         # devient bob (le tiret recharge SON environnement complet)
```


Le tiret `-` est important : il charge l'environnement de la cible (son `PATH`, son `HOME`, son `.bashrc` — tout ce qu'on a vu au chapitre 8) comme une vraie connexion. Sans le tiret, tu gardes en partie ton ancien environnement, ce qui prête à confusion. On reparlera de `su -` face à `sudo` au chapitre suivant.

## ❌ Erreur classique

```bash
# Oublier le -a dans usermod et écraser les groupes
sudo usermod -G sudo bob     # ❌ retire bob de TOUS ses autres groupes
sudo usermod -aG sudo bob    # ✅ AJOUTE bob au groupe sudo

# Croire que /etc/passwd contient les mots de passe
cat /etc/passwd              # le "x" en 2e champ renvoie à /etc/shadow
sudo cat /etc/shadow         # les empreintes chiffrées sont ICI

# Utiliser useradd en pensant que tout est prêt
sudo useradd bob             # ❌ pas de /home, pas de shell utilisable par défaut
sudo adduser bob             # ✅ assistant complet sur Debian/Ubuntu

# Faire su sans le tiret et s'étonner de l'environnement
su bob                       # garde une partie de TON environnement
su - bob                     # ✅ charge proprement l'environnement de bob

# chown récursif sur le mauvais dossier
sudo chown -R bob /           # ❌❌ catastrophe système
sudo chown -R bob /home/bob   # ✅ cible précise
```


## Exercices

**Guidé :** Lance `id` et `groups` sur ton propre compte. Repère ton UID, ton groupe principal, et la liste de tes groupes. Es-tu membre du groupe `sudo` ? Ensuite, affiche les cinq premières lignes de `/etc/passwd` avec `head -5 /etc/passwd` et identifie, pour ton compte, son dossier personnel et son shell.

**Autonome (en lab) :** Crée un nouvel utilisateur `testuser` avec `sudo adduser testuser`. Vérifie qu'il apparaît bien dans `/etc/passwd` (avec `grep testuser /etc/passwd`). Ajoute-le à un groupe existant avec `sudo usermod -aG users testuser`, puis confirme avec `groups testuser`. Quand tu as terminé, tu peux le supprimer avec `sudo deluser testuser`.

**Défi (orientation sécurité) :** Réalise un mini-audit des comptes. Avec `cut -d: -f1,7 /etc/passwd`, liste chaque compte avec son shell. Distingue les comptes qui ont un shell de connexion réel (`/bin/bash`, `/bin/sh`) de ceux qui ont `nologin` ou `false` (comptes de service, non destinés à se connecter). Combien de comptes peuvent réellement ouvrir une session ? C'est exactement la question que se pose un analyste face à une machine inconnue.

## ✅ Tu sais maintenant…

- Que l'identité repose sur des **UID** et des **GID**, derrière les noms lisibles
- Inspecter ton identité avec `id`, `whoami`, `groups`
- Le rôle de **root** (UID 0), qui ignore les permissions
- Lire les trois fichiers de comptes : `/etc/passwd`, `/etc/group`, `/etc/shadow`
- Changer la propriété avec `chown` / `chgrp` (et la prudence du `-R`)
- Créer un utilisateur (`adduser` sur Debian/Ubuntu, `useradd` ailleurs) et gérer son mot de passe
- Ajouter un utilisateur à un groupe avec `usermod -aG` (le `-a` **obligatoire**)
- Changer d'identité avec `su -` (le tiret recharge l'environnement)
- **Auditer les comptes** d'une machine en lisant `/etc/passwd`

---
