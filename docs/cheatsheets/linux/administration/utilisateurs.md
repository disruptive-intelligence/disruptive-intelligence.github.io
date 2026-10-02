---
title: "Utilisateurs et groupes"
cours:
  - library/it/linux/administration-linux/index.md
---

# Utilisateurs et groupes

Créer, modifier, verrouiller ou supprimer des comptes et des groupes ; donner des droits sudo précis.

Les incontournables : `adduser` · `usermod -aG` · `passwd` · `usermod -L` · `visudo`
{ .kw-cs-top }

## Comptes

### Créer un utilisateur

```bash title="Commande"
sudo adduser <utilisateur>   # interactif (Debian, Ubuntu)
sudo useradd -m <utilisateur>   # non interactif, toutes distributions
```

```bash title="Exemple"
sudo adduser alice
```

??? example "Sortie"
    ```text
    info: Adding user `alice' ...
    info: Adding new group `alice' (1001) ...
    info: Adding new user `alice' (1001) with group `alice (1001)' ...
    info: Creating home directory `/home/alice' ...
    New password:
    ```

```bash title="Exemple 2"
sudo useradd -m -s /bin/bash -G sudo alice   # dossier, shell bash, groupe sudo
```

Pour comprendre : [Administration Linux, ch. 10](../../../library/it/linux/administration-linux/03-partie-3-qui-a-le-droit-de-quoi/02-chapitre-10-propriete-utilisateurs-et-groupes.md)
{ .kw-cs-meta }

### Changer un mot de passe

```bash title="Commande"
sudo passwd <utilisateur>   # nouveau mot de passe
sudo chage -l <utilisateur>   # dates d'expiration
```

```bash title="Exemple"
sudo passwd alice
```

```bash title="Exemple 2"
sudo chage -l alice
```

??? example "Sortie"
    ```text
    Last password change					: Oct 01, 2026
    Password expires					: never
    Account expires						: never
    ```

### Verrouiller ou déverrouiller un compte

```bash title="Commande"
sudo usermod -L <utilisateur>   # verrouiller
sudo usermod -U <utilisateur>   # déverrouiller
```

```bash title="Exemple"
sudo usermod -L alice
```

```bash title="Exemple 2"
sudo usermod -s /usr/sbin/nologin alice   # interdit aussi la connexion par clé SSH
```

### Changer d'utilisateur

```bash title="Commande"
su - <utilisateur>        # demande le mot de passe de cet utilisateur
sudo -iu <utilisateur>    # demande le mien (droits sudo)
```

```bash title="Exemple"
sudo -iu www-data
```

### Supprimer un utilisateur

```bash title="Commande"
sudo deluser --remove-home <utilisateur>   # userdel -r sur RHEL
```

```bash title="Exemple"
sudo deluser --remove-home alice
```

!!! warning "Attention"
    Supprime aussi son dossier : sauvegarder avant si on en a besoin (`sudo tar -czf alice.tar.gz /home/alice`).

## Groupes et sudo

### Ajouter un utilisateur à un groupe

```bash title="Commande"
sudo usermod -aG <groupe> <utilisateur>   # -a : ajoute (sans -a : remplace)
```

```bash title="Exemple"
sudo usermod -aG docker alice
```

!!! warning "Attention"
    Sans `-a`, l'utilisateur est retiré de tous ses autres groupes. Le changement compte à la prochaine connexion.

### Créer un groupe

```bash title="Commande"
sudo groupadd <groupe>
```

```bash title="Exemple"
sudo groupadd projet-x
```

### Donner un droit sudo précis

```bash title="Commande"
sudo visudo -f /etc/sudoers.d/<fichier>   # éditeur qui vérifie la syntaxe
```

```bash title="Exemple"
sudo visudo -f /etc/sudoers.d/alice
# puis, dans le fichier :
alice ALL=(root) /usr/bin/systemctl restart nginx
```

!!! warning "Attention"
    Toujours `visudo` : il vérifie la syntaxe ; un sudoers cassé bloque sudo pour tout le monde.

Pour comprendre : [Administration Linux, ch. 11](../../../library/it/linux/administration-linux/03-partie-3-qui-a-le-droit-de-quoi/03-chapitre-11-sudo-et-l-elevation-de-privileges.md)
{ .kw-cs-meta }
