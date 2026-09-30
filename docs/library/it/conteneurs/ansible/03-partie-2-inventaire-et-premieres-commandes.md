---
title: PARTIE 2 — INVENTAIRE ET PREMIÈRES COMMANDES
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
chapter: 3
chapters: 13
---

> **Objectif de la partie :** décrire tes machines dans un **inventaire**, puis **agir** dessus en une seule ligne avec les **commandes ad hoc**. On apprend aussi à **lire les sorties** d'Ansible — un réflexe essentiel pour la suite.

---


## Chapitre 2.1 — L'inventaire INI

### Le minimum à savoir

Avant d'agir sur des machines, Ansible doit **savoir lesquelles existent**. C'est le rôle de l'**inventaire** : un fichier qui **liste** tes machines et les **organise en groupes**.

Le format le plus simple pour débuter est le format **INI** :

```ini
# inventory.ini

[web]
cible1 ansible_host=192.168.56.11
cible2 ansible_host=192.168.56.12

[db]
cible3 ansible_host=192.168.56.13
```

- `[web]` et `[db]` sont des **groupes**.
- `cible1`, `cible2`, `cible3` sont des **hôtes** (les machines).
- `ansible_host=...` indique l'**adresse IP** réelle de connexion.

> **L'inventaire est la base de tout.** Toutes tes commandes et tous tes playbooks viseront un **hôte** ou un **groupe** défini ici. Un inventaire clair, c'est la moitié du travail.

#### Le groupe `all`

Toutes les machines de l'inventaire appartiennent automatiquement à un groupe spécial : **`all`**. Cibler `all`, c'est cibler **toutes** les machines d'un coup.

> 💡 **Mention pour plus tard :** au début, on précise l'inventaire à chaque commande avec `-i inventory.ini`. C'est un peu répétitif. En **Partie 10**, on verra qu'un petit fichier `ansible.cfg` permet d'**éviter** de retaper `-i` à chaque fois. Pour l'instant, on garde le `-i` : c'est plus explicite pour comprendre.

### Très utile en pratique

```bash
# Visualiser l'inventaire tel qu'Ansible le comprend (vue en arbre)
ansible-inventory -i inventory.ini --graph
```

```text
@all:
  |--@web:
  |  |--cible1
  |  |--cible2
  |--@db:
  |  |--cible3
```

Cette vue `--graph` est ton **réflexe de vérification** : avant d'agir, tu regardes **qui est dans quel groupe**. C'est la meilleure protection contre l'erreur de cible.

### Exemple simple

Un inventaire minimal pour le lab du cours :

```ini
[web]
cible1 ansible_host=192.168.56.11
cible2 ansible_host=192.168.56.12
```

Deux machines, un groupe `web`. C'est suffisant pour commencer.

### ❌ Erreur classique

> **Se tromper d'IP ou mettre un hôte dans le mauvais groupe.**

Une IP erronée dans `ansible_host`, et Ansible n'arrive pas à joindre la machine (ou en joint une autre !). Un hôte dans le mauvais groupe, et ta commande touche la mauvaise cible. Le réflexe correct : **vérifier l'inventaire avec `ansible-inventory --graph`** avant d'agir, et confirmer les IP avec un `ssh` à la main en cas de doute.

### Exercices

#### Guidé
Crée un fichier `inventory.ini` décrivant tes deux cibles dans un groupe `web`, avec leurs vraies IP. Lance `ansible-inventory -i inventory.ini --graph` et vérifie que l'arbre correspond à ce que tu attendais.

#### Autonome
Ajoute un groupe `db` avec une troisième machine (réelle ou fictive). Relance `--graph` et observe la nouvelle structure. Un hôte peut-il être dans plusieurs groupes ? Teste en mettant `cible1` à la fois dans `web` et dans un nouveau groupe `pilote`.

#### Défi
Sans encore l'utiliser, ajoute une **variable de groupe** dans ton inventaire :
```ini
[web:vars]
http_port=80
```
Relance `ansible-inventory -i inventory.ini --graph --vars` (ou `--list`) et retrouve cette variable dans la sortie. On s'en servira au chapitre suivant.

### ✅ Tu sais maintenant…

- Que l'**inventaire** liste tes machines et les organise en **groupes**.
- Écrire un inventaire au format **INI** (hôtes, groupes, `ansible_host`).
- Que le groupe **`all`** désigne toutes les machines.
- Vérifier ton inventaire avec **`ansible-inventory --graph`**.
- Qu'on précise l'inventaire avec **`-i`** (et qu'`ansible.cfg` simplifiera ça plus tard).

---


## Chapitre 2.2 — Variables simples d'inventaire

### Le minimum à savoir

Parfois, une machine ou un groupe a besoin d'une **valeur particulière** : un port, un nom, un utilisateur de connexion. On peut le préciser **directement dans l'inventaire**, avec des **variables**.

#### Variables d'un hôte

```ini
[web]
cible1 ansible_host=192.168.56.11 ansible_user=admin
```

Ici, `ansible_user=admin` dit à Ansible de se connecter en tant qu'`admin` sur cette machine.

#### Variables d'un groupe

```ini
[web]
cible1 ansible_host=192.168.56.11
cible2 ansible_host=192.168.56.12

[web:vars]
ansible_user=admin
http_port=80
```

`[web:vars]` définit des variables pour **toutes** les machines du groupe `web`.

> **Quelques variables spéciales utiles** (Ansible les reconnaît automatiquement) : `ansible_host` (l'IP), `ansible_user` (l'utilisateur SSH), `ansible_port` (le port SSH si différent de 22).

### Très utile en pratique

```bash
# Voir toutes les variables effectives d'un hôte
ansible-inventory -i inventory.ini --host cible1
```

```text
{
    "ansible_host": "192.168.56.11",
    "ansible_user": "admin",
    "http_port": 80
}
```

Cette commande est précieuse : elle te montre **exactement** quelles valeurs s'appliquent à une machine.

### Exemple simple

```ini
[web]
cible1 ansible_host=192.168.56.11
cible2 ansible_host=192.168.56.12

[web:vars]
ansible_user=admin
```

Les deux machines du groupe `web` se connecteront avec l'utilisateur `admin`.

### 🔀 À ne pas confondre

> **Variable d'hôte vs variable de groupe.**
> Une variable mise sur une **ligne d'hôte** ne concerne **que** cette machine. Une variable dans `[groupe:vars]` concerne **toutes** les machines du groupe. Si les deux définissent la même variable, c'est la plus **spécifique** (l'hôte) qui l'emporte.

### ❌ Erreur classique

> **Mettre une variable au mauvais endroit et obtenir une valeur inattendue.**

Tu définis `ansible_user=admin` pour le groupe, mais une ligne d'hôte précise `ansible_user=root` : sur cette machine, ce sera `root`, et tu ne comprends pas pourquoi. Le réflexe correct : utiliser **`ansible-inventory --host <machine>`** pour voir la **valeur réellement appliquée**.

### Exercices

#### Guidé
Ajoute `ansible_user=<ton_utilisateur>` en variable de groupe `[web:vars]`. Lance `ansible-inventory -i inventory.ini --host cible1` et vérifie que `ansible_user` apparaît bien.

#### Autonome
Ajoute une variable `http_port=8080` à **une seule** machine (sur sa ligne d'hôte), tout en gardant `http_port=80` dans `[web:vars]`. Avec `--host`, vérifie quelle valeur gagne sur cette machine, et laquelle gagne sur l'autre.

#### Défi
Explique en quelques lignes l'intérêt de définir `ansible_user` dans l'inventaire plutôt que de le retaper à chaque commande. Quel lien fais-tu avec le futur fichier `ansible.cfg` (Partie 10) ?

### ✅ Tu sais maintenant…

- Définir des **variables** d'hôte (sur la ligne) et de groupe (`[groupe:vars]`).
- Les variables spéciales utiles : `ansible_host`, `ansible_user`, `ansible_port`.
- Voir les valeurs effectives avec **`ansible-inventory --host`**.
- Que la variable la plus **spécifique** (hôte) l'emporte sur celle du groupe.

---


## Chapitre 2.3 — Le ping et les commandes ad hoc

### Le minimum à savoir

Une **commande ad hoc** est une action Ansible lancée **directement en ligne de commande**, sans écrire de fichier. C'est parfait pour une action **ponctuelle** : vérifier que les machines répondent, lancer une commande rapide.

La structure d'une commande ad hoc :

```
ansible  <cible>  -m <module>  -a "<arguments>"
         ▲        ▲            ▲
         groupe   le module    les arguments
         ou hôte  à exécuter   du module
```

#### Le premier réflexe : `ping`

Le tout premier test, c'est de vérifier qu'Ansible **joint** ses cibles, avec le module `ping` :

```bash
ansible all -i inventory.ini -m ansible.builtin.ping
```

> 🔀 **À ne pas confondre :** le `ping` d'Ansible n'est **pas** le `ping` réseau habituel (ICMP). Il vérifie qu'Ansible peut **se connecter en SSH** à la machine **et** y exécuter du Python. Un `ping` Ansible réussi prouve que **toute la chaîne fonctionne**.

#### Une note sur les noms de modules (FQCN)

Tu remarques qu'on écrit `ansible.builtin.ping` et pas juste `ping`. C'est le **nom complet** du module (on parle de **FQCN**). On l'utilise pour **éviter les ambiguïtés** entre modules de même nom. Retiens simplement : **on écrit le nom complet `ansible.builtin.xxx`**. Pas besoin d'en savoir plus pour l'instant.

### Très utile en pratique

```bash
# Pinguer toutes les machines
ansible all -i inventory.ini -m ansible.builtin.ping

# Pinguer un seul groupe
ansible web -i inventory.ini -m ansible.builtin.ping

# Lancer une commande simple (lecture, sans danger)
ansible all -i inventory.ini -m ansible.builtin.command -a "uptime"

# Voir l'espace disque de chaque machine
ansible web -i inventory.ini -m ansible.builtin.command -a "df -h /"
```

```text
$ ansible all -i inventory.ini -m ansible.builtin.ping
cible1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
cible2 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

`SUCCESS` + `"ping": "pong"` = la machine est joignable et opérationnelle. C'est le feu vert.

### Exemple simple

```bash
# "Est-ce que mes deux cibles répondent ?"
ansible web -i inventory.ini -m ansible.builtin.ping
```

Si les deux répondent `SUCCESS`, ton lab est prêt à travailler.

### ❌ Erreur classique

> **Un `ping` qui échoue avec `UNREACHABLE`, et chercher le problème dans Ansible.**

Si `ping` renvoie `UNREACHABLE`, le souci est dans la **connexion SSH**, pas dans Ansible (mauvaise IP, mauvaise clé, mauvais utilisateur, machine éteinte). Le réflexe correct : tester **`ssh utilisateur@cible` à la main**. Si ça échoue aussi, règle SSH d'abord (rappel : Partie 1).

### Exercices

#### Guidé
Lance `ansible all -i inventory.ini -m ansible.builtin.ping`. Tes deux cibles doivent répondre `SUCCESS` / `pong`. Si l'une affiche `UNREACHABLE`, teste `ssh` à la main vers cette machine et corrige.

#### Autonome
Avec le module `command`, récupère l'`uptime` (depuis quand la machine tourne) et l'espace disque (`df -h /`) de chaque cible. Tu viens de faire un petit **état des lieux** de ton parc en deux commandes.

#### Défi
Cible **une seule** machine au lieu d'un groupe entier : `ansible cible1 -i inventory.ini -m ansible.builtin.ping`. Puis essaie de cibler le groupe `web` mais en te limitant à une machine. (Indice : il existe une option `--limit`. On la verra plus en détail en Partie 8.)

### ✅ Tu sais maintenant…

- Ce qu'est une **commande ad hoc** : agir en une ligne, sans playbook.
- La structure `ansible <cible> -m <module> -a "<args>"`.
- Le module **`ping`** comme premier test (SSH + Python), différent du ping réseau.
- Qu'on écrit les modules en **nom complet** (`ansible.builtin.xxx`).
- Lancer des commandes de lecture (`uptime`, `df`).

---


## Chapitre 2.4 — `command` et `shell`

### Le minimum à savoir

Ansible propose deux modules pour lancer une commande « brute » sur les cibles :

- **`ansible.builtin.command`** : exécute une commande **simple**, sans passer par un shell complet.
- **`ansible.builtin.shell`** : exécute une commande **via un shell**, ce qui permet les `|`, `>`, `&&`, etc.

```bash
# command : commande simple
ansible web -i inventory.ini -m ansible.builtin.command -a "hostname"

# shell : nécessaire pour les redirections, pipes, etc.
ansible web -i inventory.ini -m ansible.builtin.shell -a "cat /etc/os-release | grep PRETTY"
```

> **Règle simple :** utilise **`command`** par défaut. Passe à **`shell`** seulement si tu as besoin des fonctionnalités du shell (pipes `|`, redirections `>`, `&&`). `shell` est un peu plus puissant, mais aussi un peu moins sûr (il interprète tout).

### Très utile en pratique

```bash
# command suffit pour une commande simple
ansible all -i inventory.ini -m ansible.builtin.command -a "whoami"

# shell est nécessaire ici (à cause du pipe)
ansible all -i inventory.ini -m ansible.builtin.shell -a "ps aux | grep ssh"
```

### Exemple simple

```bash
# "Quelle est la version de l'OS sur chaque machine ?"
ansible all -i inventory.ini -m ansible.builtin.shell -a "cat /etc/os-release | grep PRETTY_NAME"
```

(On utilise `shell` ici à cause du `|`.)

### 🔀 À ne pas confondre

> **`command` (simple) vs `shell` (avec shell).**
> `command` ne comprend **pas** les `|`, `>`, `&&` — si tu en as besoin, il faut `shell`. Inversement, pour une commande simple, **préfère `command`** : c'est plus prévisible.

### ❌ Erreur classique

> **Tout faire en `command`/`shell`, même quand un module dédié existe.**

On pourrait être tenté de tout faire avec `shell` : `shell -a "apt install htop"`, `shell -a "systemctl start nginx"`. Mais c'est une **mauvaise habitude** : ces commandes ne sont **pas idempotentes** (relancer relance l'action) et contournent toute l'intelligence d'Ansible. Le réflexe correct : pour installer un paquet, gérer un service, copier un fichier… **utilise le module dédié** (qu'on verra en Partie 5). Garde `command`/`shell` pour ce qui n'a **pas** de module dédié. On comprendra **pourquoi** en détail dès la Partie 3.

### Exercices

#### Guidé
Lance une commande simple avec `command` (par exemple `hostname` ou `whoami`) sur tout le parc. Observe la sortie pour chaque machine.

#### Autonome
Essaie de lancer une commande avec un **pipe** (`|`) en utilisant `command`. Observe que ça échoue ou se comporte mal. Refais-la avec `shell`. Tu comprends ainsi quand `shell` est nécessaire.

#### Défi
Sans encore connaître les modules dédiés, réfléchis : pourquoi `shell -a "apt install htop"` est-il une **mauvaise idée** comparé à un futur module `apt` ? (Indice : que se passe-t-il si on le relance alors que htop est déjà installé ?)

### ✅ Tu sais maintenant…

- La différence entre **`command`** (commande simple) et **`shell`** (avec pipes/redirections).
- Préférer **`command`** par défaut, **`shell`** seulement si nécessaire.
- Que `command`/`shell` ne sont **pas idempotents** et qu'il faut leur préférer les **modules dédiés** quand ils existent.

---


## Chapitre 2.5 — Lire les sorties : `ok`, `changed`, `failed`, `skipped`, `unreachable`

### Le minimum à savoir

Savoir **lire ce qu'Ansible répond** est un réflexe indispensable. Chaque action, sur chaque machine, se termine dans l'un de ces **cinq états** :

| Statut | Signification |
|--------|---------------|
| **`ok`** | La machine était **déjà** dans l'état voulu : rien à faire |
| **`changed`** | Ansible a **modifié** quelque chose pour atteindre l'état voulu |
| **`failed`** | L'action a **échoué** sur cette machine |
| **`skipped`** | L'action a été **ignorée** (à cause d'une condition — on verra ça en Partie 6) |
| **`unreachable`** | Ansible **n'a pas pu joindre** la machine (problème SSH/réseau) |

> **Apprends ces cinq mots maintenant.** Ils sont ta boussole pour tout le reste du cours. La distinction la plus importante est **`ok` vs `changed`** : on l'approfondit dans la partie suivante (l'idempotence).

#### Commande ad hoc vs playbook

Une **commande ad hoc** agit une fois, en ligne de commande. Un **playbook** (Partie 4) est un fichier réutilisable qui décrit plusieurs actions. Mais dans les **deux** cas, tu liras ces **mêmes** statuts.

### Très utile en pratique

Avec une commande ad hoc, le statut apparaît au début de la réponse de chaque machine :

```text
cible1 | SUCCESS => { ... }          ← tout va bien (équivaut à ok)
cible2 | CHANGED => { ... }          ← Ansible a modifié quelque chose
cible3 | UNREACHABLE! => { ... }     ← machine injoignable (SSH/réseau)
cible4 | FAILED! => { ... }          ← l'action a échoué
```

### Exemple simple

```bash
ansible all -i inventory.ini -m ansible.builtin.ping
```
```text
cible1 | SUCCESS => {"ping": "pong"}      ← ok : la machine répond
cible2 | UNREACHABLE! => {...}            ← problème SSH : à diagnostiquer
```

Ici, tu vois immédiatement que `cible2` a un souci de connexion, et que `cible1` va bien.

### 🔍 Réflexe diagnostic

> Devant une exécution, **lis les statuts d'abord** :
> - `unreachable` → problème **SSH/réseau** (teste `ssh` à la main).
> - `failed` → l'action a échoué (lis le **message d'erreur** affiché).
> - `changed` partout alors que tu rejoues → quelque chose n'est pas idempotent (Partie 3).
> - `skipped` → une condition a ignoré l'action (Partie 6).

### ❌ Erreur classique

> **Ne pas lire les statuts et croire que « ça a marché » parce qu'il n'y a pas eu d'erreur évidente.**

Un débutant lance une commande, ne voit pas de message rouge, et passe à la suite — sans vérifier. Or `unreachable` sur une machine signifie qu'elle n'a **rien** reçu, et tu pourrais ne pas t'en rendre compte. Le réflexe correct : **toujours regarder le statut de chaque machine**. Une absence d'erreur évidente n'est pas une preuve que tout s'est bien passé partout.

### Exercices

#### Guidé
Lance un `ping` sur tout le parc et identifie le statut de **chaque** machine. Tout doit être `SUCCESS`. Note ce que tu vois.

#### Autonome
Provoque un `unreachable` : éteins une cible (ou coupe son réseau) et relance le `ping`. Observe `UNREACHABLE` sur cette machine et `SUCCESS` sur l'autre. Rallume la cible et confirme le retour à `SUCCESS`.

#### Défi
Provoque un `failed` : lance une commande qui échoue, par exemple `ansible all -i inventory.ini -m ansible.builtin.command -a "ls /dossier_qui_nexiste_pas"`. Lis le message d'erreur. En quoi `failed` (l'action a échoué) est-il **différent** de `unreachable` (la machine n'a pas été jointe) ?

### ✅ Tu sais maintenant…

- Lire les **cinq statuts** : `ok`, `changed`, `failed`, `skipped`, `unreachable`.
- Que la distinction reine est **`ok` vs `changed`** (approfondie en Partie 3).
- Que ces statuts sont les **mêmes** en ad hoc et en playbook.
- Le réflexe : **lire les statuts** pour diagnostiquer (`unreachable` = SSH, `failed` = erreur d'action).

---

### 🚩 Checkpoint — Fin de la Partie 2

Ansible **agit** maintenant sur ton parc. Avant de plonger dans l'idempotence, assure-toi de pouvoir :

- [ ] Écrire un **inventaire INI** avec des groupes et des variables simples.
- [ ] Vérifier ton inventaire avec **`ansible-inventory --graph`** et **`--host`**.
- [ ] Lancer un **`ping`** et des commandes ad hoc (`command`, `shell`).
- [ ] Savoir quand utiliser **`command`** vs **`shell`**.
- [ ] Lire les **cinq statuts** (`ok`, `changed`, `failed`, `skipped`, `unreachable`).
- [ ] Diagnostiquer un **`unreachable`** (côté SSH).

> **🧩 Mini-projet 2 — « Inventaire propre + état des lieux ».**
> 1. Écris un `inventory.ini` avec un groupe `web` (tes deux cibles) et une variable de groupe `ansible_user`.
> 2. Vérifie-le avec `ansible-inventory --graph` et `--host`.
> 3. Pingue tout le parc.
> 4. Avec des commandes ad hoc en lecture, collecte l'uptime et l'espace disque de chaque machine.
> Objectif : enchaîner **décrire → vérifier → agir → lire les sorties**, avec le réflexe « je regarde le statut de chaque machine ».
>
> **🧩 Mini-projet 3 — « Commandes ad hoc multi-machines ».**
> Sur le groupe `web`, lance trois commandes de lecture différentes (par exemple : `hostname`, `df -h /`, et la version de l'OS via `shell` + pipe). Compare les sorties entre les deux machines.

> **La suite :** en Partie 3, on s'attaque au concept qui rend Ansible **vraiment** différent d'un script : l'**idempotence**. Tu vas le **voir de tes yeux** en relançant une commande.

---
---
---
