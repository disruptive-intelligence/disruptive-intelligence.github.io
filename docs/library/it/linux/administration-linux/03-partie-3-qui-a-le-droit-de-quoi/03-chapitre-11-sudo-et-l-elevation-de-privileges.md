---
title: Chapitre 11 — sudo et l'élévation de privilèges
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 3 — Qui a le droit de quoi
  - index.md
---

## Le minimum à savoir

### Le principe de moindre privilège

Le concept le plus important de la sécurité tient en une phrase : **on n'utilise que les droits dont on a besoin, au moment où on en a besoin, et pas plus.** C'est le **principe de moindre privilège**. Rester connecté en root « pour être tranquille » est exactement le contraire : la moindre erreur, ou le moindre programme malveillant lancé par mégarde, dispose alors de tous les pouvoirs. La bonne pratique est de travailler en utilisateur normal et de **n'élever ses privilèges que ponctuellement**, commande par commande.

### `sudo` : emprunter les pouvoirs de root, une commande à la fois

`sudo` (*substitute user do*, « faire en tant qu'un autre ») exécute **une seule commande** avec les droits de root, puis te rend immédiatement ton identité normale :

```bash
sudo apt update                  # exécute CETTE commande en root
sudo cat /etc/shadow             # lit un fichier réservé à root, puis on redevient normal
```


La première fois, `sudo` te demande **ton propre** mot de passe (pas celui de root), puis le mémorise quelques minutes pour ne pas te le redemander à chaque commande. Seuls les utilisateurs autorisés (membres du groupe `sudo` sur Debian/Ubuntu — souviens-toi de `id` au chapitre 10) peuvent l'utiliser.

> **Le minimum à savoir :** quand une commande échoue avec « Permission denied » et qu'il s'agit d'une vraie tâche d'administration (installer un logiciel, modifier `/etc`, gérer un service), préfixe-la par `sudo`. Mais demande-toi toujours : ai-je **vraiment** besoin des droits root pour ça ?

### Distinguer les façons d'élever ses privilèges

Plusieurs commandes se ressemblent mais font des choses différentes. Cette distinction est essentielle :

| Commande | Ce qu'elle fait |
|----------|-----------------|
| `sudo commande` | Exécute **une seule** commande en root, puis revient à toi. **C'est la méthode recommandée.** |
| `sudo -i` | Ouvre un **shell root interactif** (tu *deviens* root jusqu'à ce que tu tapes `exit`). À éviter sauf nécessité. |
| `su -` | Bascule vers le compte root en demandant **le mot de passe de root** (pas le tien). Souvent désactivé sur Ubuntu. |
| `sudoedit fichier` | Édite un fichier système en sécurité (vu au chapitre 6). Préférable à `sudo nano`. |

> **La différence clé entre `sudo -i` et `su -` :** `sudo -i` utilise **ton** mot de passe et passe par `sudo` (donc c'est journalisé, voir plus bas) ; `su -` réclame le mot de passe **de root** directement. Sur Ubuntu, le compte root n'a pas de mot de passe défini par défaut, donc `su -` échoue et l'on passe par `sudo`. Pour une commande ponctuelle, `sudo commande` reste **toujours** préférable à ouvrir un shell root entier.

## Très utile en pratique

### sudo est journalisé : chaque usage laisse une trace

Contrairement à une connexion root directe, **chaque commande lancée avec `sudo` est enregistrée** : qui, quand, depuis où, quelle commande. C'est un atout majeur pour la sécurité et la traçabilité. On retrouve ces traces dans le journal d'authentification (souviens-toi du chapitre 4 : `/var/log/auth.log` sur Debian/Ubuntu, `/var/log/secure` ailleurs, ou `journalctl`) :

```bash
sudo grep sudo /var/log/auth.log     # retrouve les usages de sudo (Debian/Ubuntu)
```


> **Très utile en sécurité (SOC) :** lors d'une investigation, ces lignes permettent de répondre à « qui a fait quoi en tant qu'administrateur, et quand ? ». Une élévation de privilège inattendue dans ces logs est un signal d'alerte classique. On approfondira l'analyse des journaux au chapitre 15.

### Configurer sudo proprement : `visudo`

Les droits sudo sont définis dans un fichier spécial, `/etc/sudoers`. **On ne l'édite jamais directement** : on passe par `visudo`, qui **vérifie la syntaxe avant d'enregistrer**. Une erreur dans ce fichier pourrait sinon bloquer tout accès administrateur à la machine.

```bash
sudo visudo              # édite /etc/sudoers en toute sécurité (contrôle de syntaxe)
```


Pour débuter, tu n'as pas besoin de modifier ce fichier ; retiens surtout **pourquoi** `visudo` existe : c'est le garde-fou qui t'empêche de te verrouiller dehors. C'est le même esprit que le `.bak` du chapitre 6, appliqué au fichier le plus sensible du système.

### sudo, vecteur d'attaque classique

Du point de vue d'un attaquant, `sudo` est une cible de choix : s'il parvient à exécuter une commande via un `sudo` mal configuré, il obtient les pleins pouvoirs. C'est pourquoi, en sécurité, on vérifie systématiquement **ce qu'un utilisateur a le droit de faire avec sudo** :

```bash
sudo -l          # liste ce que TU es autorisé à exécuter via sudo
```


> **Orientation cyber / eJPT :** `sudo -l` est l'une des toutes premières commandes lancées lors d'une recherche d'élévation de privilèges. Une règle sudo trop permissive (par exemple, le droit de lancer un éditeur ou un interpréteur en root) est une voie d'escalade très répandue. Côté défense, on garde les règles sudo **minimales et précises**. On reverra ce réflexe au chapitre sécurité (25).

## ❌ Erreur classique

```bash
# Tout faire en root "pour être tranquille"
sudo -i                  # ❌ shell root permanent : une erreur = dégâts maximaux
sudo commande            # ✅ une commande à la fois, on reste normal le reste du temps

# Éditer /etc/sudoers directement
sudo nano /etc/sudoers   # ❌ une faute de syntaxe peut bloquer tout sudo
sudo visudo              # ✅ vérifie la syntaxe avant d'enregistrer

# Mettre sudo devant TOUT, par réflexe
sudo ls ~                # ❌ inutile : tu peux déjà lire ton propre dossier
ls ~                     # ✅ sudo seulement quand c'est nécessaire

# Confondre son mot de passe et celui de root
sudo commande            # demande TON mot de passe
su -                     # demande celui de ROOT (souvent absent sur Ubuntu)

# Oublier que sudo expire
sudo apt update          # mot de passe demandé...
# (quelques minutes plus tard)
sudo apt upgrade         # peut le redemander : c'est normal, c'est une sécurité
```


## Exercices

**Guidé :** Lance `sudo -l` pour voir ce que tu es autorisé à faire via sudo sur ta machine. Ensuite, tente `cat /etc/shadow` sans sudo (ça échoue : Permission denied), puis `sudo cat /etc/shadow` (ça fonctionne, mais ne te montre que des empreintes chiffrées). Observe la différence d'accès qu'apporte l'élévation.

**Autonome :** Utilise `sudo` pour une vraie tâche d'administration inoffensive, par exemple `sudo apt update`. Puis cherche la trace de ton action dans le journal d'authentification avec `sudo grep sudo /var/log/auth.log | tail` (adapte le chemin à ta distribution). Retrouves-tu la commande que tu viens de lancer, avec l'heure ?

**Défi :** Compare concrètement `sudo whoami` et `whoami`. Le premier doit afficher `root`, le second ton nom. Explique en une phrase pourquoi : `sudo` a exécuté `whoami` **en tant que root**, le temps de cette seule commande, avant de te rendre ton identité.

## ✅ Tu sais maintenant…

- Le **principe de moindre privilège** : n'élever ses droits que ponctuellement
- Utiliser `sudo commande` pour exécuter **une** action en root (avec **ton** mot de passe)
- Distinguer `sudo commande`, `sudo -i`, `su -` et `sudoedit`
- Que **chaque usage de sudo est journalisé** (traçabilité, valeur en sécurité)
- Configurer sudo en sécurité avec `visudo` (et pourquoi on n'édite jamais `/etc/sudoers` à la main)
- Vérifier tes droits avec `sudo -l` — réflexe clé en recherche d'escalade de privilèges

---
