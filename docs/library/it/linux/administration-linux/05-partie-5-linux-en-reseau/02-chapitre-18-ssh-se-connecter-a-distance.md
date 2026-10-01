---
title: 'Chapitre 18 — SSH : se connecter à distance'
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 5 — Linux en réseau
  - index.md
---

## Le minimum à savoir

### Le principe : un terminal sur une machine distante

**SSH** (*Secure Shell*) est le protocole qui permet d'ouvrir un terminal sur une machine **distante**, à travers le réseau, de façon **chiffrée** (personne ne peut espionner la session). C'est l'outil fondamental de l'administration : la quasi-totalité des serveurs dans le monde se gèrent en SSH. Tout ce que tu as appris depuis le chapitre 1 s'applique à l'identique sur la machine distante — c'est juste le terminal qui est « ailleurs ».

Il y a deux côtés :

- Le **client SSH** (`ssh`) : sur ta machine, tu t'en sers pour te connecter.
- Le **serveur SSH** (`sshd`, le démon du chapitre 14) : sur la machine distante, il attend et accepte les connexions, sur le **port 22** par défaut.

### Se connecter : `ssh`

```bash
ssh alice@192.168.1.50       # se connecte en tant qu'alice sur la machine 192.168.1.50
ssh alice@serveur.exemple.com  # avec un nom de domaine
ssh -p 2222 alice@serveur    # -p pour préciser un port différent du 22
```


À la **première** connexion, SSH affiche l'**empreinte** (*fingerprint*) de la machine distante et te demande de confirmer. C'est une sécurité : tu vérifies que tu te connectes à la bonne machine, et non à un imposteur. Une fois acceptée, l'empreinte est mémorisée ; un changement futur déclenchera un avertissement.

Pour terminer une session distante, on tape simplement `exit` (ou `Ctrl + D`).

## Très utile en pratique

### L'authentification par clé : plus sûre que le mot de passe

Se connecter par mot de passe fonctionne, mais reste vulnérable (on peut le deviner, le forcer). La méthode professionnelle est l'**authentification par clé**, fondée sur une paire :

- une **clé privée**, qui reste **secrète** sur ta machine (à ne **jamais** partager) ;
- une **clé publique**, qu'on dépose sur les serveurs où l'on veut se connecter.

Le serveur vérifie que tu possèdes la clé privée correspondant à la clé publique qu'il connaît, sans qu'aucun secret ne circule. On génère sa paire de clés une fois :

```bash
ssh-keygen -t ed25519        # crée une paire de clés (algorithme moderne et sûr)
```


Cela crée deux fichiers dans `~/.ssh/` : `id_ed25519` (privée, à protéger) et `id_ed25519.pub` (publique, à diffuser). On copie ensuite la clé **publique** sur le serveur :

```bash
ssh-copy-id alice@serveur    # installe ta clé publique sur le serveur distant
```


Désormais, `ssh alice@serveur` te connecte **sans mot de passe**, de façon plus sûre.

> **Règle d'or des clés :** la clé **privée** ne quitte **jamais** ta machine et ne se partage **jamais**. Si quelqu'un l'obtient, il peut se faire passer pour toi. La clé **publique**, elle, peut être diffusée sans risque. Protège ta clé privée comme le mot de passe le plus important.

### Simplifier avec `~/.ssh/config`

Si tu te connectes souvent aux mêmes machines, tu peux leur donner des surnoms dans un fichier de configuration personnel :

```bash
# Dans ~/.ssh/config
Host monserveur
    HostName 192.168.1.50
    User alice
    Port 22
```


Tu n'as plus qu'à taper `ssh monserveur`. C'est plus court, moins source d'erreurs, et ça centralise tes accès.

### Durcir le serveur SSH (côté défense)

Le serveur SSH étant la porte d'entrée d'une machine, c'est une **cible privilégiée** des attaques (notamment les attaques par force brute du chapitre 4). Quelques réglages, dans `/etc/ssh/sshd_config`, réduisent fortement le risque. On les modifie **avec le réflexe du chapitre 6** (`.bak`, `sudoedit`, `diff`) :

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak    # 1. sauvegarde
sudoedit /etc/ssh/sshd_config                            # 2. édition sécurisée
```


Les durcissements les plus courants :

- **`PermitRootLogin no`** : interdire la connexion directe en root (on se connecte en utilisateur normal, puis `sudo`). C'est l'un des réglages les plus importants.
- **`PasswordAuthentication no`** : n'autoriser que les clés, une fois celles-ci en place (supprime tout risque de force brute sur mot de passe).
- Éventuellement, changer le port par défaut pour réduire le bruit automatisé.

Après modification, on **recharge** le service (chapitre 14) pour appliquer :

```bash
diff /etc/ssh/sshd_config.bak /etc/ssh/sshd_config       # 3. vérifier le changement
sudo systemctl restart ssh                               # 4. appliquer
```


> **⚠️ Prudence vitale en SSH distant :** ne désactive **jamais** ta seule méthode d'accès sans en avoir une autre qui fonctionne. Avant de couper l'authentification par mot de passe, **vérifie que ta clé fonctionne**. Avant de redémarrer `sshd` à distance, garde une session ouverte de secours. Une mauvaise manipulation peut te verrouiller dehors de ta propre machine.

> **Orientation cyber / SOC :** le durcissement SSH (pas de root, clés uniquement) est l'un des gestes défensifs les plus rentables. Et côté surveillance, suivre les tentatives de connexion (`journalctl -u ssh -f`, chapitre 15) permet de détecter une attaque en cours.

## ❌ Erreur classique

```bash
# Partager ou copier la mauvaise clé
cat ~/.ssh/id_ed25519        # ❌ JAMAIS : c'est la clé PRIVÉE, elle reste secrète
cat ~/.ssh/id_ed25519.pub    # ✅ la clé PUBLIQUE, celle qu'on diffuse

# Mauvaises permissions sur ~/.ssh (SSH refuse de fonctionner)
chmod 777 ~/.ssh             # ❌ SSH refusera d'utiliser des clés trop ouvertes
chmod 700 ~/.ssh             # ✅ dossier privé
chmod 600 ~/.ssh/id_ed25519  # ✅ clé privée lisible par toi seul

# Désactiver le mot de passe AVANT de tester la clé
# ❌ risque de se verrouiller dehors
# ✅ teste d'abord ssh par clé, PUIS désactive le mot de passe

# Redémarrer sshd à distance sans filet
sudo systemctl restart ssh   # ⚠️ garde une 2e session ouverte au cas où

# Ignorer un changement d'empreinte
# Un avertissement de changement de fingerprint peut signaler un vrai problème : ne pas l'ignorer aveuglément
```


## Exercices

**Guidé :** Génère ta paire de clés SSH avec `ssh-keygen -t ed25519` (accepte l'emplacement par défaut, choisis ou non une passphrase). Vérifie que deux fichiers ont été créés dans `~/.ssh/` avec `ls -l ~/.ssh/`. Identifie lequel est la clé privée et lequel est la publique. Quelles sont leurs permissions ?

**Autonome (si tu disposes d'une seconde machine ou d'une VM) :** Connecte-toi en SSH d'une machine à l'autre par mot de passe. Observe la demande de confirmation d'empreinte à la première connexion. Une fois connecté, lance `hostname` et `whoami` pour confirmer que tu es bien sur la machine distante. Termine avec `exit`.

**Défi (orientation sécurité, en lab) :** Sur une machine de test où tu as déjà un accès de secours, mets en place l'authentification par clé (`ssh-copy-id`), vérifie qu'elle fonctionne, puis prépare (sans forcément appliquer) les durcissements de `sshd_config` : `PermitRootLogin no` et `PasswordAuthentication no`. Avant tout `restart`, relis la règle d'or : as-tu un accès garanti si quelque chose tourne mal ? Décris la procédure prudente que tu suivrais.

## ✅ Tu sais maintenant…

- Que **SSH** ouvre un terminal **chiffré** sur une machine distante (port 22, démon `sshd`)
- Te connecter avec `ssh user@machine` (et `-p` pour un autre port), et l'importance de l'**empreinte**
- Mettre en place l'**authentification par clé** (`ssh-keygen`, `ssh-copy-id`), plus sûre que le mot de passe
- Que la clé **privée** ne se partage **jamais**, contrairement à la publique
- Simplifier tes accès avec `~/.ssh/config`
- **Durcir** le serveur SSH (`PermitRootLogin no`, `PasswordAuthentication no`) avec le réflexe `.bak`/`sudoedit`/`diff`
- La prudence vitale pour ne pas se verrouiller dehors lors d'un changement à distance

---
