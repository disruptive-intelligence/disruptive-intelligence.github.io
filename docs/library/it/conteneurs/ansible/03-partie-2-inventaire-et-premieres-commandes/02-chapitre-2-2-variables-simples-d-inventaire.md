---
title: Chapitre 2.2 — Variables simples d'inventaire
source: IT/08 Conteneurs & automatisation/Automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 2 — Inventaire et premières commandes
  - index.md
---

## Le minimum à savoir

Parfois, une machine ou un groupe a besoin d'une **valeur particulière** : un port, un nom, un utilisateur de connexion. On peut le préciser **directement dans l'inventaire**, avec des **variables**.

### Variables d'un hôte

```ini
[web]
cible1 ansible_host=192.168.56.11 ansible_user=admin
```


Ici, `ansible_user=admin` dit à Ansible de se connecter en tant qu'`admin` sur cette machine.

### Variables d'un groupe

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

## Très utile en pratique

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

## Exemple simple

```ini
[web]
cible1 ansible_host=192.168.56.11
cible2 ansible_host=192.168.56.12

[web:vars]
ansible_user=admin
```


Les deux machines du groupe `web` se connecteront avec l'utilisateur `admin`.

## 🔀 À ne pas confondre

> **Variable d'hôte vs variable de groupe.**
> Une variable mise sur une **ligne d'hôte** ne concerne **que** cette machine. Une variable dans `[groupe:vars]` concerne **toutes** les machines du groupe. Si les deux définissent la même variable, c'est la plus **spécifique** (l'hôte) qui l'emporte.

## ❌ Erreur classique

> **Mettre une variable au mauvais endroit et obtenir une valeur inattendue.**

Tu définis `ansible_user=admin` pour le groupe, mais une ligne d'hôte précise `ansible_user=root` : sur cette machine, ce sera `root`, et tu ne comprends pas pourquoi. Le réflexe correct : utiliser **`ansible-inventory --host <machine>`** pour voir la **valeur réellement appliquée**.

## Exercices

### Guidé
Ajoute `ansible_user=<ton_utilisateur>` en variable de groupe `[web:vars]`. Lance `ansible-inventory -i inventory.ini --host cible1` et vérifie que `ansible_user` apparaît bien.

### Autonome
Ajoute une variable `http_port=8080` à **une seule** machine (sur sa ligne d'hôte), tout en gardant `http_port=80` dans `[web:vars]`. Avec `--host`, vérifie quelle valeur gagne sur cette machine, et laquelle gagne sur l'autre.

### Défi
Explique en quelques lignes l'intérêt de définir `ansible_user` dans l'inventaire plutôt que de le retaper à chaque commande. Quel lien fais-tu avec le futur fichier `ansible.cfg` (Partie 10) ?

## ✅ Tu sais maintenant…

- Définir des **variables** d'hôte (sur la ligne) et de groupe (`[groupe:vars]`).
- Les variables spéciales utiles : `ansible_host`, `ansible_user`, `ansible_port`.
- Voir les valeurs effectives avec **`ansible-inventory --host`**.
- Que la variable la plus **spécifique** (hôte) l'emporte sur celle du groupe.

---
