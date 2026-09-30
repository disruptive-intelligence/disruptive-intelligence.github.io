---
title: Chapitre 7.1 — Les templates Jinja2 (template)
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 7 — Templates et handlers
  - index.md
---

## Le minimum à savoir

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

## Très utile en pratique

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

## Exemple simple

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

## 🔀 À ne pas confondre

> **`copy` (fichier identique) vs `template` (fichier généré).**
> `copy` dépose un fichier **tel quel**, le même partout. `template` **génère** un fichier en remplaçant les `{{ }}` par les valeurs de chaque machine. Dès qu'un fichier doit **varier** selon la cible, c'est un **template**.

## ❌ Erreur classique

> **Utiliser `copy` puis se retrouver à maintenir dix versions d'un fichier de config.**

Si tu copies un fichier de config et que tu dois l'adapter machine par machine, tu finis avec dix fichiers presque identiques. Le réflexe correct : dès qu'un fichier varie selon la machine, **un seul template** avec des variables remplace les dix copies.

## Exercices

### Guidé
Crée un template `motd.j2` qui affiche le nom d'hôte et l'OS de chaque machine. Déploie-le avec `template` dans `/etc/motd`. Connecte-toi en SSH à chaque cible et vérifie que le contenu est **personnalisé**.

### Autonome
Crée un template de page web (`index.html.j2`) affichant le nom de la machine, et déploie-le dans `/var/www/html/`. Accède à chaque serveur (navigateur ou `curl`) et vérifie que chacun affiche son propre nom.

### Défi
Utilise une **boucle Jinja2** (`{% for %}`) dans un template pour générer une liste à partir d'une variable (par exemple une liste d'utilisateurs définie en `group_vars`). Vérifie le fichier généré sur la cible.

## ✅ Tu sais maintenant…

- Générer des fichiers **dynamiques** avec **`template`** et **Jinja2**.
- Insérer des valeurs (`{{ }}`), des conditions (`{% if %}`) et des boucles (`{% for %}`) dans un template.
- La convention d'extension **`.j2`**.
- La différence **`copy`** (identique) vs **`template`** (adapté à chaque machine).

---
