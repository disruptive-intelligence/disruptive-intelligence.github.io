---
title: PARTIE 3 — Qui a le droit de quoi
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
chapter: 3
chapters: 7
---

Voici le cœur de l'administration Linux et de la sécurité. Jusqu'ici, tu manipulais des fichiers ; maintenant, tu vas comprendre **qui** a le droit de faire **quoi**, et **pourquoi**. C'est le modèle qui protège un système : il décide qui peut lire un mot de passe, modifier une configuration, ou lancer un programme privilégié. Maîtriser cette partie, c'est comprendre à la fois comment administrer proprement **et** comment un système se fait attaquer. C'est la partie la plus importante du cours pour l'orientation cybersécurité.

---


## Chapitre 9 — Comprendre les permissions

### Le minimum à savoir

#### L'idée : trois questions, trois réponses

Sous Linux, chaque fichier répond à trois questions :

1. **Qui possède ce fichier ?** → son **propriétaire** (*user*)
2. **Quel groupe y a accès ?** → son **groupe** (*group*)
3. **Et tous les autres ?** → les **autres** (*others*)

Pour chacune de ces trois catégories, le système définit ce qui est permis : **lire**, **écrire**, **exécuter**. C'est tout. Ce modèle simple (trois catégories × trois droits) gouverne l'accès à l'ensemble du système.

#### Lire un `ls -l` : décrypter la première colonne

Tu as déjà vu `ls -l` au chapitre 2. Reprends-le maintenant avec un œil neuf :

```bash
ls -l rapport.txt
# -rw-r--r-- 1 alice equipe 1240 Jan 10 14:30 rapport.txt
```

Concentrons-nous sur le premier bloc, `-rw-r--r--`. Il se découpe ainsi :

```
  -        rw-       r--       r--
  │         │         │         │
type    propriétaire groupe   autres
```

- **1er caractère** : le **type**. `-` = fichier ordinaire, `d` = dossier (*directory*), `l` = lien symbolique.
- **Caractères 2 à 4** (`rw-`) : les droits du **propriétaire**.
- **Caractères 5 à 7** (`r--`) : les droits du **groupe**.
- **Caractères 8 à 10** (`r--`) : les droits des **autres**.

#### Les trois droits : r, w, x

Chaque triplet se lit toujours dans le même ordre : `r`, `w`, `x`. Un tiret `-` signifie « ce droit est absent ».

| Lettre | Sur un fichier | Sur un dossier |
|--------|----------------|----------------|
| `r` (read) | lire le contenu | lister les fichiers qu'il contient |
| `w` (write) | modifier le contenu | créer/supprimer des fichiers dedans |
| `x` (execute) | exécuter le fichier (programme/script) | **entrer** dans le dossier (`cd`) |

> **Le piège des dossiers :** sur un **dossier**, `x` ne veut pas dire « exécuter » mais « traverser » (pouvoir faire `cd` dedans et accéder à son contenu). Un dossier sans `x` est inaccessible même si tu as `r`. Retiens : pour entrer dans un dossier, il faut le `x`.

Reprenons `-rw-r--r--` : c'est un fichier ordinaire, le propriétaire peut lire et écrire (`rw-`), le groupe peut seulement lire (`r--`), les autres aussi (`r--`). Personne ne peut l'exécuter. C'est typique d'un fichier de données.

### Très utile en pratique

#### Modifier les permissions : `chmod` en notation symbolique

`chmod` (*change mode*) modifie les droits. La façon la plus lisible utilise des lettres :

- **Qui** : `u` (user/propriétaire), `g` (group), `o` (others), `a` (all/tous)
- **Action** : `+` (ajouter), `-` (retirer), `=` (fixer exactement)
- **Droit** : `r`, `w`, `x`

```bash
chmod u+x script.sh      # ajoute le droit d'exécution AU PROPRIÉTAIRE
chmod go-w fichier       # retire l'écriture au groupe ET aux autres
chmod a+r fichier        # donne la lecture à tout le monde
```

Le cas le plus fréquent de tout le cours : **rendre un script exécutable**.

```bash
chmod u+x mon-script.sh      # maintenant on peut le lancer avec ./mon-script.sh
```

> Ça boucle avec le chapitre 8 : un script fraîchement écrit n'est qu'un fichier texte. Pour que le système accepte de l'**exécuter**, il lui faut le droit `x`. Sans lui : « Permission denied ».

#### La notation octale : les chiffres

Tu verras très souvent les permissions exprimées en **chiffres**, comme `chmod 755`. C'est la même chose, écrite autrement. Chaque droit vaut un nombre :

- `r` = **4**
- `w` = **2**
- `x` = **1**

On **additionne** pour chaque catégorie, ce qui donne un chiffre de 0 à 7 :

| Chiffre | Droits | Calcul |
|---------|--------|--------|
| 7 | `rwx` | 4+2+1 |
| 6 | `rw-` | 4+2 |
| 5 | `r-x` | 4+1 |
| 4 | `r--` | 4 |
| 0 | `---` | rien |

On écrit alors **trois** chiffres : propriétaire, groupe, autres.

```bash
chmod 755 script.sh      # rwx pour le proprio, r-x pour groupe et autres
chmod 644 fichier.txt    # rw- pour le proprio, r-- pour groupe et autres
chmod 600 secret.txt     # rw- pour le proprio, RIEN pour les autres
```

> **Les deux valeurs à mémoriser :** `644` pour un fichier de données normal (le propriétaire écrit, les autres lisent), `755` pour un programme ou un dossier (tout le monde peut exécuter/traverser, seul le propriétaire modifie). `600` pour un fichier privé (clé, secret) que toi seul peux lire. Ces trois valeurs couvrent l'immense majorité des cas.

#### `umask` : les permissions par défaut

Quand tu crées un fichier, il reçoit des permissions par défaut. Celles-ci sont déterminées par le `umask`, un « filtre » qui **retire** des droits par défaut (typiquement, il enlève l'écriture aux autres) :

```bash
umask            # affiche le masque actuel (souvent 022)
```

Pour débuter, retiens simplement que `umask` **existe** et explique pourquoi tes nouveaux fichiers ne sont pas en écriture pour tout le monde. Tu n'as pas besoin de le modifier maintenant.

### ❌ Erreur classique

```bash
# Oublier de rendre un script exécutable
./mon-script.sh          # ❌ "Permission denied"
chmod u+x mon-script.sh  # ✅ puis ./mon-script.sh fonctionne

# Donner trop de droits "pour que ça marche"
chmod 777 fichier        # ❌ rwx pour TOUT LE MONDE : faille de sécurité béante
chmod 755 fichier        # ✅ juste ce qu'il faut

# Confondre l'ordre des chiffres
chmod 457 fichier        # rarement ce qu'on veut : réfléchis proprio/groupe/autres
chmod 644 fichier        # ✅ l'ordre est TOUJOURS proprio, groupe, autres

# Croire que r suffit pour entrer dans un dossier
chmod 600 dossier/       # ❌ sans x, impossible d'y faire cd
chmod 700 dossier/       # ✅ le x permet de traverser le dossier
```

> **Le réflexe `777` est un grand classique du débutant** : « ça ne marche pas, je mets tous les droits à tout le monde ». C'est exactement ce qu'un attaquant rêve de trouver. Donne **le minimum nécessaire**, jamais `777`.

### Exercices

**Guidé :** Crée un fichier `script.sh` contenant `echo "Bonjour"` (avec `echo "echo \"Bonjour\"" > script.sh`). Regarde ses permissions avec `ls -l`. Essaie de le lancer avec `./script.sh` — ça échoue. Rends-le exécutable avec `chmod u+x script.sh`, vérifie le changement avec `ls -l`, puis relance-le.

**Autonome :** Crée trois fichiers et donne-leur respectivement les permissions `644`, `600` et `755` en notation octale. Vérifie chacune avec `ls -l` et **traduis à voix haute** ce que chaque triplet signifie (qui peut faire quoi).

**Défi :** Pour un fichier donné, atteins exactement les permissions `rw-r-----` (le proprio lit/écrit, le groupe lit, les autres rien). Fais-le d'abord en notation symbolique (`chmod`), puis recommence sur un autre fichier en notation octale. Quel est le chiffre octal correspondant ? Vérifie avec `ls -l` que les deux méthodes donnent le même résultat.

### ✅ Tu sais maintenant…

- Le modèle **propriétaire / groupe / autres** (u/g/o) et les trois droits **r/w/x**
- **Lire** la ligne de permissions d'un `ls -l`, caractère par caractère
- Que `x` signifie « exécuter » sur un fichier mais « traverser » sur un dossier
- Modifier les droits avec `chmod` en **symbolique** (`u+x`, `go-w`…)
- La notation **octale** (r=4, w=2, x=1) et les valeurs clés `644`, `755`, `600`
- Pourquoi `chmod 777` est une mauvaise idée de sécurité
- Que `umask` détermine les permissions par défaut

---


## Chapitre 10 — Propriété, utilisateurs et groupes

### Le minimum à savoir

#### L'identité sur un système Linux

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

#### root : le super-utilisateur

Un compte est à part : **root**, l'administrateur. Son UID est **0**, et il **ignore les permissions** : root peut tout lire, tout modifier, tout supprimer. C'est à la fois indispensable (pour administrer) et dangereux (une erreur en root peut détruire le système). On verra au chapitre 11 comment utiliser ce pouvoir proprement, sans rester connecté en root en permanence.

#### Où sont stockés les comptes ? Trois fichiers clés

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

### Très utile en pratique

#### Changer le propriétaire : `chown` et `chgrp`

Quand un fichier doit appartenir à quelqu'un d'autre (ou à un autre groupe), on utilise `chown` (*change owner*) :

```bash
sudo chown alice fichier.txt          # alice devient propriétaire
sudo chown alice:equipe fichier.txt   # propriétaire alice, groupe equipe
sudo chgrp equipe fichier.txt         # change seulement le groupe
```

Ces commandes nécessitent en général `sudo` : changer la propriété d'un fichier est une opération privilégiée.

> **Souviens-toi de la Partie 0 :** `chown -R` et `chmod -R` (récursifs) figurent dans les commandes dangereuses. Appliqués au mauvais dossier, ils peuvent rendre tout un pan du système inaccessible. Vérifie **toujours** le chemin avant un `-R`.

#### Créer un utilisateur

Sur Debian/Ubuntu, le plus simple est `adduser`, un assistant interactif qui crée le compte, son dossier personnel et demande le mot de passe :

```bash
sudo adduser bob         # assistant guidé (recommandé sur Debian/Ubuntu)
```

Il existe aussi `useradd`, plus bas niveau et plus universel, mais moins convivial (il ne crée pas le dossier personnel sans options) :

```bash
sudo useradd -m -s /bin/bash bob     # -m crée le /home, -s définit le shell
sudo passwd bob                      # définit ensuite son mot de passe
```

#### Gérer les mots de passe et les groupes

```bash
passwd                   # change TON propre mot de passe
sudo passwd bob          # change le mot de passe de bob (en admin)
sudo usermod -aG sudo bob   # ajoute bob au groupe "sudo" (-aG = append to Group)
```

> **L'option `-aG` est cruciale et piégeuse :** le `-a` (*append*, ajouter) est **obligatoire**. Sans lui, `usermod -G` **remplace** tous les groupes de l'utilisateur par celui indiqué, le retirant de tous les autres. Oublier le `-a` est une erreur classique qui peut, par exemple, retirer quelqu'un du groupe `sudo` sans le vouloir.

#### Changer d'identité : `su`

`su` (*substitute user*) permet de devenir un autre utilisateur le temps d'une session :

```bash
su - bob         # devient bob (le tiret recharge SON environnement complet)
```

Le tiret `-` est important : il charge l'environnement de la cible (son `PATH`, son `HOME`, son `.bashrc` — tout ce qu'on a vu au chapitre 8) comme une vraie connexion. Sans le tiret, tu gardes en partie ton ancien environnement, ce qui prête à confusion. On reparlera de `su -` face à `sudo` au chapitre suivant.

### ❌ Erreur classique

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

### Exercices

**Guidé :** Lance `id` et `groups` sur ton propre compte. Repère ton UID, ton groupe principal, et la liste de tes groupes. Es-tu membre du groupe `sudo` ? Ensuite, affiche les cinq premières lignes de `/etc/passwd` avec `head -5 /etc/passwd` et identifie, pour ton compte, son dossier personnel et son shell.

**Autonome (en lab) :** Crée un nouvel utilisateur `testuser` avec `sudo adduser testuser`. Vérifie qu'il apparaît bien dans `/etc/passwd` (avec `grep testuser /etc/passwd`). Ajoute-le à un groupe existant avec `sudo usermod -aG users testuser`, puis confirme avec `groups testuser`. Quand tu as terminé, tu peux le supprimer avec `sudo deluser testuser`.

**Défi (orientation sécurité) :** Réalise un mini-audit des comptes. Avec `cut -d: -f1,7 /etc/passwd`, liste chaque compte avec son shell. Distingue les comptes qui ont un shell de connexion réel (`/bin/bash`, `/bin/sh`) de ceux qui ont `nologin` ou `false` (comptes de service, non destinés à se connecter). Combien de comptes peuvent réellement ouvrir une session ? C'est exactement la question que se pose un analyste face à une machine inconnue.

### ✅ Tu sais maintenant…

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


## Chapitre 11 — sudo et l'élévation de privilèges

### Le minimum à savoir

#### Le principe de moindre privilège

Le concept le plus important de la sécurité tient en une phrase : **on n'utilise que les droits dont on a besoin, au moment où on en a besoin, et pas plus.** C'est le **principe de moindre privilège**. Rester connecté en root « pour être tranquille » est exactement le contraire : la moindre erreur, ou le moindre programme malveillant lancé par mégarde, dispose alors de tous les pouvoirs. La bonne pratique est de travailler en utilisateur normal et de **n'élever ses privilèges que ponctuellement**, commande par commande.

#### `sudo` : emprunter les pouvoirs de root, une commande à la fois

`sudo` (*substitute user do*, « faire en tant qu'un autre ») exécute **une seule commande** avec les droits de root, puis te rend immédiatement ton identité normale :

```bash
sudo apt update                  # exécute CETTE commande en root
sudo cat /etc/shadow             # lit un fichier réservé à root, puis on redevient normal
```

La première fois, `sudo` te demande **ton propre** mot de passe (pas celui de root), puis le mémorise quelques minutes pour ne pas te le redemander à chaque commande. Seuls les utilisateurs autorisés (membres du groupe `sudo` sur Debian/Ubuntu — souviens-toi de `id` au chapitre 10) peuvent l'utiliser.

> **Le minimum à savoir :** quand une commande échoue avec « Permission denied » et qu'il s'agit d'une vraie tâche d'administration (installer un logiciel, modifier `/etc`, gérer un service), préfixe-la par `sudo`. Mais demande-toi toujours : ai-je **vraiment** besoin des droits root pour ça ?

#### Distinguer les façons d'élever ses privilèges

Plusieurs commandes se ressemblent mais font des choses différentes. Cette distinction est essentielle :

| Commande | Ce qu'elle fait |
|----------|-----------------|
| `sudo commande` | Exécute **une seule** commande en root, puis revient à toi. **C'est la méthode recommandée.** |
| `sudo -i` | Ouvre un **shell root interactif** (tu *deviens* root jusqu'à ce que tu tapes `exit`). À éviter sauf nécessité. |
| `su -` | Bascule vers le compte root en demandant **le mot de passe de root** (pas le tien). Souvent désactivé sur Ubuntu. |
| `sudoedit fichier` | Édite un fichier système en sécurité (vu au chapitre 6). Préférable à `sudo nano`. |

> **La différence clé entre `sudo -i` et `su -` :** `sudo -i` utilise **ton** mot de passe et passe par `sudo` (donc c'est journalisé, voir plus bas) ; `su -` réclame le mot de passe **de root** directement. Sur Ubuntu, le compte root n'a pas de mot de passe défini par défaut, donc `su -` échoue et l'on passe par `sudo`. Pour une commande ponctuelle, `sudo commande` reste **toujours** préférable à ouvrir un shell root entier.

### Très utile en pratique

#### sudo est journalisé : chaque usage laisse une trace

Contrairement à une connexion root directe, **chaque commande lancée avec `sudo` est enregistrée** : qui, quand, depuis où, quelle commande. C'est un atout majeur pour la sécurité et la traçabilité. On retrouve ces traces dans le journal d'authentification (souviens-toi du chapitre 4 : `/var/log/auth.log` sur Debian/Ubuntu, `/var/log/secure` ailleurs, ou `journalctl`) :

```bash
sudo grep sudo /var/log/auth.log     # retrouve les usages de sudo (Debian/Ubuntu)
```

> **Très utile en sécurité (SOC) :** lors d'une investigation, ces lignes permettent de répondre à « qui a fait quoi en tant qu'administrateur, et quand ? ». Une élévation de privilège inattendue dans ces logs est un signal d'alerte classique. On approfondira l'analyse des journaux au chapitre 15.

#### Configurer sudo proprement : `visudo`

Les droits sudo sont définis dans un fichier spécial, `/etc/sudoers`. **On ne l'édite jamais directement** : on passe par `visudo`, qui **vérifie la syntaxe avant d'enregistrer**. Une erreur dans ce fichier pourrait sinon bloquer tout accès administrateur à la machine.

```bash
sudo visudo              # édite /etc/sudoers en toute sécurité (contrôle de syntaxe)
```

Pour débuter, tu n'as pas besoin de modifier ce fichier ; retiens surtout **pourquoi** `visudo` existe : c'est le garde-fou qui t'empêche de te verrouiller dehors. C'est le même esprit que le `.bak` du chapitre 6, appliqué au fichier le plus sensible du système.

#### sudo, vecteur d'attaque classique

Du point de vue d'un attaquant, `sudo` est une cible de choix : s'il parvient à exécuter une commande via un `sudo` mal configuré, il obtient les pleins pouvoirs. C'est pourquoi, en sécurité, on vérifie systématiquement **ce qu'un utilisateur a le droit de faire avec sudo** :

```bash
sudo -l          # liste ce que TU es autorisé à exécuter via sudo
```

> **Orientation cyber / eJPT :** `sudo -l` est l'une des toutes premières commandes lancées lors d'une recherche d'élévation de privilèges. Une règle sudo trop permissive (par exemple, le droit de lancer un éditeur ou un interpréteur en root) est une voie d'escalade très répandue. Côté défense, on garde les règles sudo **minimales et précises**. On reverra ce réflexe au chapitre sécurité (25).

### ❌ Erreur classique

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

### Exercices

**Guidé :** Lance `sudo -l` pour voir ce que tu es autorisé à faire via sudo sur ta machine. Ensuite, tente `cat /etc/shadow` sans sudo (ça échoue : Permission denied), puis `sudo cat /etc/shadow` (ça fonctionne, mais ne te montre que des empreintes chiffrées). Observe la différence d'accès qu'apporte l'élévation.

**Autonome :** Utilise `sudo` pour une vraie tâche d'administration inoffensive, par exemple `sudo apt update`. Puis cherche la trace de ton action dans le journal d'authentification avec `sudo grep sudo /var/log/auth.log | tail` (adapte le chemin à ta distribution). Retrouves-tu la commande que tu viens de lancer, avec l'heure ?

**Défi :** Compare concrètement `sudo whoami` et `whoami`. Le premier doit afficher `root`, le second ton nom. Explique en une phrase pourquoi : `sudo` a exécuté `whoami` **en tant que root**, le temps de cette seule commande, avant de te rendre ton identité.

### ✅ Tu sais maintenant…

- Le **principe de moindre privilège** : n'élever ses droits que ponctuellement
- Utiliser `sudo commande` pour exécuter **une** action en root (avec **ton** mot de passe)
- Distinguer `sudo commande`, `sudo -i`, `su -` et `sudoedit`
- Que **chaque usage de sudo est journalisé** (traçabilité, valeur en sécurité)
- Configurer sudo en sécurité avec `visudo` (et pourquoi on n'édite jamais `/etc/sudoers` à la main)
- Vérifier tes droits avec `sudo -l` — réflexe clé en recherche d'escalade de privilèges

---


## Chapitre 12 — Permissions avancées (panorama)

### Le minimum à savoir

#### Au-delà des r/w/x : un panorama

Le modèle r/w/x du chapitre 9 couvre 95 % des situations. Mais il existe des permissions **spéciales** qui résolvent des problèmes particuliers — et qui sont, justement pour cette raison, des **cibles privilégiées en sécurité**. L'objectif de ce chapitre n'est pas de te rendre expert, mais de te faire **reconnaître** ces mécanismes : tu dois savoir qu'ils existent, ce qu'ils font, et comment les repérer. C'est exactement ce qu'on regarde lors d'un audit ou d'une recherche d'élévation de privilèges.

#### Le bit SUID : exécuter avec les droits du propriétaire

Normalement, quand tu lances un programme, il s'exécute avec **tes** droits. Le bit **SUID** (*Set User ID*) change cela : un programme avec SUID s'exécute avec les droits de **son propriétaire**, pas les tiens. Si le propriétaire est root, le programme tourne donc avec les pouvoirs de root, même lancé par un utilisateur normal.

Un exemple légitime et universel : `passwd`. Pour changer ton mot de passe, le système doit écrire dans `/etc/shadow` (réservé à root). `passwd` est donc SUID root : il te laisse modifier **ta** ligne, en toute sécurité, sans te donner root pour autant.

On repère le SUID dans un `ls -l` par un **`s`** à la place du `x` du propriétaire :

```bash
ls -l /usr/bin/passwd
# -rwsr-xr-x 1 root root ... /usr/bin/passwd
#    ↑ ce "s" = bit SUID
```

#### Pourquoi le SUID est central en sécurité

Le SUID est puissant, donc dangereux. **Un programme SUID root mal conçu ou inattendu est une porte vers les privilèges root.** Si un attaquant trouve sur le système un binaire SUID qui lui permet, d'une manière ou d'une autre, d'exécuter ses propres commandes, il devient root. C'est l'une des voies d'escalade les plus connues.

D'où un réflexe fondamental, aussi bien pour l'auditeur défensif que pour le testeur d'intrusion : **lister tous les fichiers SUID du système**.

```bash
find / -type f -perm -4000 2>/dev/null
```

Décortiquons cette commande, qui réunit tout ce que tu as appris :

- `find /` → cherche à partir de la racine (chapitre 4)
- `-type f` → uniquement des **fichiers** (pas des dossiers ni autres objets)
- `-perm -4000` → qui ont le bit SUID activé (le `4000` octal)
- `2>/dev/null` → on jette les innombrables « Permission denied » (chapitre 7) pour ne garder que les résultats utiles

> **Orientation cyber / eJPT :** cette commande figure dans toute checklist d'énumération d'un système Linux. Côté défense, on compare la liste obtenue aux binaires SUID **attendus** (ceux livrés par la distribution) ; tout SUID inhabituel mérite une enquête immédiate.

### Très utile en pratique

#### SGID et sticky bit, en bref

Deux autres bits spéciaux, à connaître de nom :

- **SGID** (*Set Group ID*) : comme le SUID mais pour le **groupe**. Sur un dossier, il fait hériter tous les nouveaux fichiers du groupe du dossier — pratique pour le travail collaboratif. Repérable par un `s` dans le triplet du groupe.
- **Sticky bit** : posé sur un dossier partagé (comme `/tmp`), il empêche chacun de supprimer les fichiers des autres — tu ne peux effacer que **tes** fichiers. Repérable par un `t` à la fin :

  ```bash
  ls -ld /tmp
  # drwxrwxrwt ... /tmp     ← le "t" final = sticky bit
  ```

#### Les capabilities : des privilèges root « en pièces détachées »

Sur les systèmes modernes, une alternative plus fine au tout-puissant SUID existe : les **capabilities**. Plutôt que de donner *tous* les pouvoirs de root à un programme, on lui accorde **un privilège précis et limité**. Par exemple, la capability `cap_net_raw` autorise un programme (comme `ping`) à manipuler le réseau à bas niveau, sans pour autant lui donner le reste des pouvoirs root.

On **observe** les capabilities présentes sur le système avec `getcap` :

```bash
getcap -r / 2>/dev/null      # liste récursivement tous les binaires porteurs de capabilities
```

> **Si `getcap` n'est pas disponible** (installations minimales), installe le paquet qui le fournit : `sudo apt install libcap2-bin`.

C'est le pendant moderne de la recherche de SUID : un binaire doté d'une capability trop puissante (ou inattendue) peut, lui aussi, ouvrir une voie d'escalade.

> **Important — observation, pas manipulation :** à ton niveau, `getcap` s'utilise en **observation** (lister, auditer). La commande inverse, `setcap`, qui *attribue* une capability à un binaire, ne doit être expérimentée qu'en **lab contrôlé**, sur une **copie** de binaire ou un exemple jetable — **jamais** sur un binaire système réel sans comprendre précisément ce que l'on fait. Modifier les capabilities d'un binaire système peut affaiblir gravement la sécurité de la machine.

#### Les ACL, en un mot

Le modèle u/g/o ne permet qu'**un** propriétaire et **un** groupe. Quand on a besoin de droits plus granulaires (« alice peut écrire, bob peut seulement lire, et ce groupe précis a un autre accès »), on utilise les **ACL** (*Access Control Lists*). On les consulte avec `getfacl` et on les modifie avec `setfacl`. Pour débuter, retiens simplement qu'elles **existent** et permettent des permissions plus fines que le modèle de base — tu n'as pas à les manipuler maintenant.

### ❌ Erreur classique

```bash
# Oublier 2>/dev/null et se noyer sous les erreurs
find / -type f -perm -4000           # ❌ noyé sous les "Permission denied"
find / -type f -perm -4000 2>/dev/null  # ✅ seulement les résultats utiles

# Oublier -type f et lister autre chose que des fichiers
find / -perm -4000 2>/dev/null       # mélange fichiers et autres objets
find / -type f -perm -4000 2>/dev/null  # ✅ uniquement des fichiers

# Confondre le "s" du SUID et le "s" du SGID
# -rwsr-xr-x → SUID (s dans le triplet PROPRIÉTAIRE)
# -rwxr-sr-x → SGID (s dans le triplet GROUPE)

# Utiliser setcap sur un binaire système "pour tester"
sudo setcap cap_setuid+ep /usr/bin/python3   # ❌❌ faille de sécurité majeure
# ✅ getcap pour OBSERVER ; setcap seulement en lab sur une copie jetable

# Ajouter du SUID par curiosité
sudo chmod u+s /un/binaire           # ❌ ne jamais "essayer" ça sur un système réel
```

### Exercices

**Guidé :** Liste les fichiers SUID de ton système avec `find / -type f -perm -4000 2>/dev/null`. Tu devrais y voir des classiques comme `/usr/bin/passwd` ou `/usr/bin/sudo`. Choisis-en un et confirme son bit SUID avec `ls -l` : repères-tu bien le `s` à la place du `x` du propriétaire ?

**Autonome :** Observe le sticky bit de `/tmp` avec `ls -ld /tmp` et identifie le `t` final. Explique en une phrase pourquoi ce bit est important sur un dossier où **tout le monde** peut écrire. Ensuite, liste les capabilities présentes sur ta machine avec `getcap -r / 2>/dev/null` : combien de binaires en portent ?

**Défi (orientation sécurité) :** Tu fais l'inventaire de sécurité d'une machine. Produis deux listes : (1) tous les fichiers SUID, (2) tous les binaires avec capabilities. Enregistre chacune dans un fichier (avec `>` ou `tee`, chapitre 7) pour garder une trace. Ces deux listes constituent une **base de référence** : sur un vrai système, on les comparerait régulièrement pour détecter tout ajout suspect. Quel intérêt défensif vois-tu à conserver une telle référence dans le temps ?

### ✅ Tu sais maintenant…

- Que des permissions **spéciales** existent au-delà des r/w/x
- Ce qu'est le **SUID** (exécuter avec les droits du propriétaire) et comment le repérer (`s`)
- Pourquoi le SUID est une **voie d'escalade** majeure, et comment lister les SUID : `find / -type f -perm -4000 2>/dev/null`
- Reconnaître le **SGID** (`s` du groupe) et le **sticky bit** (`t`, sur `/tmp`)
- Que les **capabilities** découpent les pouvoirs de root, et les observer avec `getcap -r /` (jamais `setcap` hors lab)
- Que les **ACL** existent pour des droits plus fins (`getfacl`/`setfacl`)
- À constituer une **base de référence** SUID/capabilities, réflexe défensif

---

> **🏁 CHECKPOINT 3 — Fin de la Partie 3 (le plus important pour la sécurité)**
>
> Tu comprends maintenant **le modèle de sécurité de Linux** : qui possède quoi, qui peut faire quoi, comment on élève ses privilèges proprement, et où se cachent les voies d'escalade. C'est le socle de toute administration sérieuse et de toute analyse défensive.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - lire une ligne de `ls -l` et dire exactement qui peut lire, écrire, exécuter ?
> - traduire `chmod 640` en `rw-r-----` et inversement ?
> - expliquer le principe de moindre privilège et pourquoi `sudo commande` vaut mieux que `sudo -i` ?
> - retrouver dans les logs qui a utilisé `sudo` et quand ?
> - lister les binaires SUID d'un système et expliquer pourquoi c'est un enjeu de sécurité ?
>
> Si oui, tu as franchi l'étape conceptuelle la plus exigeante du cours. La suite va te faire passer de « gérer des fichiers et des droits » à « piloter une machine vivante » : place à la **Partie 4 — Processus, services et logs**.

---

---
---
