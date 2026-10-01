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
sudo adduser <utilisateur>
```

```bash title="Exemple"
sudo adduser alice   # interactif : mot de passe, nom complet…
```

```bash title="Exemple 2"
sudo useradd -m -s /bin/bash -G sudo alice   # non interactif : dossier, shell et groupe sudo
```

Pour comprendre : [Administration Linux, ch. 10](../../../library/it/linux/administration-linux/03-partie-3-qui-a-le-droit-de-quoi/02-chapitre-10-propriete-utilisateurs-et-groupes.md)
{ .kw-cs-meta }

### Changer un mot de passe

```bash title="Commande"
sudo passwd <utilisateur>
```

```bash title="Exemple"
sudo passwd alice
```

```bash title="Exemple 2"
sudo chage -l alice   # dates d'expiration du mot de passe
```

### Verrouiller ou déverrouiller un compte

```bash title="Commande"
sudo usermod -L <utilisateur>
sudo usermod -U <utilisateur>
```

```bash title="Exemple"
sudo usermod -L alice
```

```bash title="Exemple 2"
sudo usermod -s /usr/sbin/nologin alice   # interdit aussi la connexion par clé SSH
```

### Changer d'utilisateur

```bash title="Commande"
su - <utilisateur>
sudo -iu <utilisateur>
```

```bash title="Exemple"
sudo -iu www-data   # shell de connexion en tant que www-data
```

### Supprimer un utilisateur

```bash title="Commande"
sudo deluser --remove-home <utilisateur>
```

```bash title="Exemple"
sudo deluser --remove-home alice
```

!!! warning "Attention"
    Supprime aussi son dossier : sauvegarder avant si on en a besoin (`sudo tar -czf alice.tar.gz /home/alice`).

## Groupes et sudo

### Ajouter un utilisateur à un groupe

```bash title="Commande"
sudo usermod -aG <groupe> <utilisateur>
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
sudo visudo -f /etc/sudoers.d/<fichier>
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
