---
title: Chapitre 20 — Gérer les paquets et logiciels
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 6 — Entretenir le système
  - index.md
---

## Le minimum à savoir

### Qu'est-ce qu'un gestionnaire de paquets ?

Sous Linux, on n'installe presque jamais un logiciel en téléchargeant un fichier sur un site web. À la place, un **gestionnaire de paquets** récupère les logiciels depuis des **dépôts** (des serveurs officiels et vérifiés), gère automatiquement leurs **dépendances** (les autres logiciels nécessaires), et permet de tout mettre à jour d'un coup. C'est plus simple, plus sûr (les paquets sont signés et vérifiés), et plus facile à maintenir.

Chaque famille de distributions a son gestionnaire :

- **Debian / Ubuntu** : `apt` (c'est celui de ce cours)
- **RHEL / CentOS / Fedora** : `dnf` (ou son ancêtre `yum`)
- **Arch** : `pacman`

### Les commandes apt essentielles

Sur Debian/Ubuntu, tout passe par `apt`, avec une poignée de sous-commandes très régulières (toutes celles qui modifient le système demandent `sudo`) :

```bash
sudo apt update              # met à jour la LISTE des paquets disponibles
sudo apt upgrade             # installe les mises à jour des paquets déjà présents
sudo apt install nom         # installe un paquet
sudo apt remove nom          # désinstalle un paquet (garde sa configuration)
sudo apt purge nom           # désinstalle ET supprime sa configuration
apt search motclé            # cherche un paquet par mot-clé (sans sudo)
apt show nom                 # affiche les détails d'un paquet
```


> **La distinction `update` / `upgrade` est essentielle et souvent confondue :** `update` rafraîchit seulement le **catalogue** (la liste de ce qui existe et des versions), il n'installe rien. `upgrade` applique réellement les mises à jour. **On fait toujours `update` avant `upgrade`** (ou avant un `install`), pour travailler sur un catalogue à jour. C'est exactement le réflexe `sudo apt update` qu'on a introduit dès la Partie 0.

### Mettre à jour son système

L'enchaînement de maintenance le plus courant, à faire régulièrement :

```bash
sudo apt update && sudo apt upgrade      # rafraîchit le catalogue PUIS met à jour
```


Le `&&` enchaîne les deux commandes : la seconde ne s'exécute que si la première a réussi.

> **À connaître — `apt full-upgrade` :** il existe aussi `sudo apt full-upgrade`, qui peut **installer ou supprimer** des paquets pour résoudre des mises à jour plus complexes (changements de dépendances). Pour débuter, retiens surtout `apt upgrade`. Utilise `full-upgrade` avec prudence, en **lisant bien ce qu'APT propose de supprimer** avant de confirmer.

> **Très utile en sécurité :** maintenir un système à jour fait partie des mesures défensives les plus **rentables** : beaucoup d'attaques exploitent des vulnérabilités **déjà connues et corrigées**. Un système non mis à jour laisse ces portes ouvertes. C'est le premier point de toute checklist de durcissement (chapitre 25).

## Très utile en pratique

### Sous le capot : `dpkg`

`apt` s'appuie sur un outil de plus bas niveau, `dpkg`, qui gère les paquets individuellement. Utile surtout pour interroger ce qui est installé :

```bash
dpkg -l                      # liste TOUS les paquets installés
dpkg -l | grep nginx         # cherche si nginx est installé (pipe du chapitre 7)
dpkg -L nom                  # liste les fichiers installés par un paquet
```


### Installer les outils de ce cours

Le moment est venu d'installer, **maintenant que tu en comprends le sens**, les outils mentionnés au fil des chapitres et regroupés dès la Partie 0. On les sépare en deux lots, ce qui clarifie leur rôle :

```bash
sudo apt update
# Lot 1 — outils d'apprentissage et d'administration
sudo apt install tree htop curl wget dnsutils traceroute net-tools rsync
# Lot 2 — outils de durcissement (on les configurera au chapitre 25)
sudo apt install ufw fail2ban
```


> **Lab vs production :** sur une machine de **lab**, tu peux installer ce lot d'un coup pour suivre le cours confortablement. Sur un **serveur réel**, installe uniquement les paquets nécessaires au besoin immédiat — chaque logiciel ajouté agrandit la surface d'attaque et la charge de maintenance. Les outils de sécurité `ufw` et `fail2ban` (lot 2) ne servent vraiment qu'une fois **configurés** : on s'en occupera au chapitre 25.

Petit rappel de ce que chacun apporte, et où on l'a croisé :

| Paquet | Outil(s) | Vu au chapitre |
|--------|----------|----------------|
| `tree` | affichage en arbre | 2 |
| `htop` | moniteur de processus | 13 |
| `curl`, `wget` | requêtes et téléchargements web | 17 |
| `dnsutils` | `dig`, `nslookup` | 17 |
| `traceroute` | chemin réseau | 17 |
| `net-tools` | `netstat`, `ifconfig` (anciens) | 17 |
| `rsync` | synchronisation/transfert | 19, 23 |
| `ufw` | pare-feu simple | 25 |
| `fail2ban` | protection contre la force brute | 25 |

> **Principe à garder :** on n'installe pas tout « au cas où » sur un vrai serveur. Sur une machine d'apprentissage, ces deux lots sont pratiques ; sur un serveur de production, on installe **uniquement le nécessaire**.

### Faire le ménage

Avec le temps, des paquets deviennent inutiles. Pour récupérer de l'espace proprement :

```bash
sudo apt autoremove          # supprime les dépendances devenues inutiles
sudo apt clean               # vide le cache des paquets téléchargés
```


## ❌ Erreur classique

```bash
# Faire upgrade sans update d'abord
sudo apt upgrade             # ❌ travaille sur un catalogue peut-être périmé
sudo apt update && sudo apt upgrade   # ✅ catalogue à jour, puis mise à jour

# Oublier sudo
apt install htop             # ❌ "Permission denied" / "are you root?"
sudo apt install htop        # ✅

# Confondre remove et purge
sudo apt remove apache2      # garde les fichiers de config
sudo apt purge apache2       # ✅ si tu veux TOUT supprimer, config comprise

# Installer des logiciels hors des dépôts sans réfléchir
# ❌ télécharger un .deb au hasard sur Internet contourne les vérifications
# ✅ privilégier les dépôts officiels ; vérifier la source si exception

# Ignorer les mises à jour de sécurité pendant des mois
# ❌ c'est la cause n°1 d'intrusions évitables
```


## Exercices

**Guidé :** Rafraîchis le catalogue avec `sudo apt update` et lis le résumé (combien de paquets peuvent être mis à jour ?). Cherche ensuite un outil avec `apt search`, par exemple `apt search htop`, puis affiche ses détails avec `apt show htop`. Enfin, installe-le avec `sudo apt install htop` et lance-le.

**Autonome :** Liste les paquets installés avec `dpkg -l` et compte-les (`dpkg -l | wc -l`, en gardant en tête que les premières lignes sont un en-tête). Cherche si quelques outils précis sont présents : `dpkg -l | grep -E "ssh|curl|rsync"`. Lesquels sont installés ?

**Défi (orientation sécurité) :** Vérifie l'état des mises à jour de sécurité de ta machine. Lance `sudo apt update`, puis `apt list --upgradable` pour voir ce qui peut être mis à jour. Combien de paquets sont concernés ? Sur un vrai système, pourquoi appliquer ces mises à jour est-il considéré comme la mesure de sécurité prioritaire ? Applique-les avec `sudo apt upgrade`.

## ✅ Tu sais maintenant…

- Ce qu'est un **gestionnaire de paquets**, des **dépôts** et des **dépendances**
- Les familles : `apt` (Debian/Ubuntu), `dnf`/`yum` (RHEL/Fedora), `pacman` (Arch)
- Les commandes `apt` clés : `update`, `upgrade`, `install`, `remove`, `purge`, `search`, `show`
- La distinction **`update`** (catalogue) vs **`upgrade`** (vraies mises à jour), et l'enchaînement `update && upgrade`
- Que **maintenir à jour** est la mesure de sécurité la plus efficace
- Interroger les paquets installés avec `dpkg -l`
- Faire le ménage avec `autoremove` et `clean`

---
