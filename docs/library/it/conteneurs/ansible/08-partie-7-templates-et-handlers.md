---
title: PARTIE 7 — TEMPLATES ET HANDLERS
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
chapter: 8
chapters: 13
---

> **Objectif de la partie :** générer des fichiers de configuration **dynamiques** avec les templates Jinja2 (un fichier adapté à chaque machine), et redémarrer un service **uniquement si nécessaire** grâce aux handlers.

---


## Chapitre 7.1 — Les templates Jinja2 (`template`)

### Le minimum à savoir

Avec `copy`, tu déposes un fichier **tel quel**, identique partout. Mais souvent, tu veux un fichier **adapté à chaque machine** : son nom d'hôte, son IP, un port spécifique. C'est le rôle du module **`template`** et du moteur **Jinja2**.

Un **template** est un fichier de configuration contenant des **variables** `{{ }}`. Ansible le **génère** pour chaque machine avec ses valeurs propres.

```jinja
{# fichier templates/motd.j2 #}
Bienvenue sur {{ ansible_hostname }}
OS : {{ ansible_distribution }} {{ ansible_distribution_version }}
Cette machine est administrée par Ansible.
```

```yaml
- name: Générer le message du jour personnalisé
  ansible.builtin.template:
    src: motd.j2               # le template (sur le contrôle)
    dest: /etc/motd            # le fichier généré (sur la cible)
  become: true
```

> **Le fichier généré sera différent sur chaque machine** : `cible1` aura son nom, `cible2` le sien. C'est toute la puissance des templates. Par convention, les templates ont l'extension **`.j2`** (pour Jinja2).

### Très utile en pratique

Jinja2 permet aussi des **conditions** et des **boucles** **dans** le fichier généré :

```jinja
{# Selon l'OS #}
{% if ansible_os_family == "Debian" %}
# Configuration Debian
{% endif %}

{# Une liste d'utilisateurs autorisés #}
{% for utilisateur in utilisateurs_autorises %}
AllowUsers {{ utilisateur }}
{% endfor %}
```

- `{{ }}` insère une **valeur**.
- `{% if %}` / `{% endif %}` : une **condition**.
- `{% for %}` / `{% endfor %}` : une **boucle**.

### Exemple simple

```jinja
{# templates/index.html.j2 #}
<h1>Bienvenue sur {{ ansible_hostname }}</h1>
```

```yaml
- name: Déployer une page d'accueil personnalisée
  ansible.builtin.template:
    src: index.html.j2
    dest: /var/www/html/index.html
  become: true
```

Chaque serveur affichera **son propre** nom dans la page.

### 🔀 À ne pas confondre

> **`copy` (fichier identique) vs `template` (fichier généré).**
> `copy` dépose un fichier **tel quel**, le même partout. `template` **génère** un fichier en remplaçant les `{{ }}` par les valeurs de chaque machine. Dès qu'un fichier doit **varier** selon la cible, c'est un **template**.

### ❌ Erreur classique

> **Utiliser `copy` puis se retrouver à maintenir dix versions d'un fichier de config.**

Si tu copies un fichier de config et que tu dois l'adapter machine par machine, tu finis avec dix fichiers presque identiques. Le réflexe correct : dès qu'un fichier varie selon la machine, **un seul template** avec des variables remplace les dix copies.

### Exercices

#### Guidé
Crée un template `motd.j2` qui affiche le nom d'hôte et l'OS de chaque machine. Déploie-le avec `template` dans `/etc/motd`. Connecte-toi en SSH à chaque cible et vérifie que le contenu est **personnalisé**.

#### Autonome
Crée un template de page web (`index.html.j2`) affichant le nom de la machine, et déploie-le dans `/var/www/html/`. Accède à chaque serveur (navigateur ou `curl`) et vérifie que chacun affiche son propre nom.

#### Défi
Utilise une **boucle Jinja2** (`{% for %}`) dans un template pour générer une liste à partir d'une variable (par exemple une liste d'utilisateurs définie en `group_vars`). Vérifie le fichier généré sur la cible.

### ✅ Tu sais maintenant…

- Générer des fichiers **dynamiques** avec **`template`** et **Jinja2**.
- Insérer des valeurs (`{{ }}`), des conditions (`{% if %}`) et des boucles (`{% for %}`) dans un template.
- La convention d'extension **`.j2`**.
- La différence **`copy`** (identique) vs **`template`** (adapté à chaque machine).

---


## Chapitre 7.2 — `copy` vs `template` (bien choisir)

### Le minimum à savoir

Maintenant que tu connais les deux, voici comment **choisir** :

| Situation | Module à utiliser |
|-----------|-------------------|
| Le fichier est **identique** sur toutes les machines | **`copy`** |
| Le fichier doit **varier** selon la machine (nom, IP, port…) | **`template`** |
| Tu veux ajuster **une seule ligne** d'un fichier existant | **`lineinfile`** (Partie 5) |

> **En résumé :** `copy` = fichier figé, `template` = fichier généré, `lineinfile` = une ligne. Trois outils, trois usages.

### Très utile en pratique

Beaucoup de fichiers de configuration réels (nginx, ssh…) contiennent des valeurs spécifiques à la machine. Dans la vraie vie, on utilise donc surtout **`template`** pour les configs, et `copy` pour les fichiers statiques (un script, une image, un fichier de licence).

### Exemple simple

- Un logo identique partout → `copy`.
- Une config nginx avec le nom du serveur → `template`.

### ❌ Erreur classique

> **Hésiter entre les deux et choisir au hasard.**

Le réflexe correct est simple : **« est-ce que ce fichier doit être différent selon la machine ? »** Si oui → `template`. Si non → `copy`. Cette seule question tranche presque toujours.

### Exercices

#### Guidé
Liste trois fichiers que tu pourrais déployer (par exemple : un logo, une config nginx, un script). Pour chacun, dis si tu utiliserais `copy` ou `template`, et **pourquoi**.

#### Autonome
Prends un fichier que tu as déployé avec `copy` et qui gagnerait à être personnalisé. Transforme-le en `template` avec au moins une variable. Compare le résultat sur deux machines.

#### Défi
Explique en quelques lignes pourquoi, dans un vrai projet, on utilise surtout `template` pour les fichiers de configuration. Qu'apporte la génération dynamique par rapport à des copies figées ?

### ✅ Tu sais maintenant…

- Choisir entre **`copy`** (identique), **`template`** (généré) et **`lineinfile`** (une ligne).
- La question qui tranche : « ce fichier doit-il varier selon la machine ? ».
- Que les configs réelles utilisent surtout **`template`**.

---


## Chapitre 7.3 — Les handlers (`notify`)

### Le minimum à savoir

Quand tu modifies la configuration d'un service, il faut souvent le **redémarrer** pour appliquer le changement. Mais le redémarrer **à chaque** exécution (même quand rien n'a changé) provoque des interruptions inutiles. La solution : les **handlers**.

Un **handler** est une tâche spéciale qui ne s'exécute **que si elle est notifiée** par un changement.

```yaml
tasks:
  - name: Déployer la config nginx
    ansible.builtin.template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify: Redémarrer nginx        # ← notifie le handler SI cette tâche change qqch
    become: true

handlers:
  - name: Redémarrer nginx          # ← le handler (déclenché seulement si notifié)
    ansible.builtin.service:
      name: nginx
      state: restarted
    become: true
```

> **Le mécanisme :** si la tâche de config **change** quelque chose (`changed`), elle **notifie** le handler, qui s'exécute **à la fin** du play. Si la config n'a **pas** changé (`ok`), le handler **ne s'exécute pas**. Résultat : **on ne redémarre que si nécessaire.**

### Très utile en pratique

```
   Config modifiée (changed)  →  handler notifié  →  service redémarré
   Config inchangée (ok)       →  handler NON notifié →  service PAS redémarré
```

C'est exactement ce qu'on veut : pas de redémarrage inutile, mais un redémarrage **garanti** quand la config change.

### Exemple simple

```yaml
tasks:
  - name: Modifier la config SSH
    ansible.builtin.lineinfile:
      path: /etc/ssh/sshd_config
      regexp: '^#?PermitRootLogin'
      line: 'PermitRootLogin no'
    notify: Redemarrer ssh
    become: true

handlers:
  - name: Redemarrer ssh
    ansible.builtin.service:
      name: ssh
      state: restarted
    become: true
```

### 🔀 À ne pas confondre

> **Tâche normale vs handler.**
> Une **tâche** s'exécute à chaque fois (selon son idempotence). Un **handler** ne s'exécute **que s'il est notifié** par un changement, et **une seule fois** à la fin, même s'il est notifié plusieurs fois. C'est fait pour les actions « à déclencher si quelque chose a changé ».

### ❌ Erreur classique

> **Mettre un `restart` directement dans les tâches au lieu d'utiliser un handler.**

Une tâche `service: state=restarted` placée dans les `tasks` redémarre le service **à chaque** exécution, même quand rien n'a changé — interruptions inutiles. Le réflexe correct : mettre le redémarrage dans un **handler**, notifié par la tâche de config. Le service ne redémarre **que** quand sa config change réellement.

### Exercices

#### Guidé
Transforme ton playbook nginx : déploie la config par `template` (ou modifie une ligne par `lineinfile`), et **notifie** un handler « Redémarrer nginx ». Lance le playbook : le handler se déclenche (config posée). Relance-le : le handler **ne se déclenche pas** (rien n'a changé).

#### Autonome
Crée un handler pour redémarrer SSH, notifié par une modification de `sshd_config`. Vérifie qu'il ne se déclenche que lorsque la config change réellement. (Attention : teste sur une cible avec snapshot, pour ne pas te couper l'accès.)

#### Défi
Mets **deux** tâches qui notifient le **même** handler. Observe qu'il ne s'exécute **qu'une seule fois** à la fin, même notifié deux fois. Explique pourquoi ce comportement est utile.

### ✅ Tu sais maintenant…

- Ce qu'est un **handler** : une tâche déclenchée **uniquement si notifiée** par un changement.
- Utiliser **`notify`** pour relier une tâche à un handler.
- Que le handler s'exécute **à la fin** du play, **une seule fois**.
- Que les handlers évitent les **redémarrages inutiles**.

---

### 🚩 Checkpoint — Fin de la Partie 7

Tu sais maintenant générer de la config et redémarrer proprement. Avant les bonnes pratiques, assure-toi de pouvoir :

- [ ] Générer des fichiers dynamiques avec **`template`** + **Jinja2** (`{{ }}`, `{% if %}`, `{% for %}`).
- [ ] Choisir entre **`copy`**, **`template`** et **`lineinfile`**.
- [ ] Utiliser des **handlers** avec **`notify`** pour redémarrer un service seulement si nécessaire.

> **🧩 Mini-projet 8 — « Générer une configuration avec template ».**
> Déploie un fichier de configuration (par exemple un `motd` ou une page web) **personnalisé par machine** grâce à un template Jinja2. Vérifie que chaque cible a sa version.
>
> **🧩 Mini-projet 9 — « Handler conditionnel ».**
> Déploie une config de service par template, avec un **handler** de redémarrage notifié. Lance deux fois : observe que le service ne redémarre **qu'au premier passage** (quand la config change), pas au second.

> **La suite :** en Partie 8, on apprend les **bons réflexes** du débutant : nommer ses tâches, vérifier avant d'agir (`--check`, `--diff`), cibler avec prudence (`--limit`), et les bases de sécurité (clés SSH, pas de secret en clair).

---
---
