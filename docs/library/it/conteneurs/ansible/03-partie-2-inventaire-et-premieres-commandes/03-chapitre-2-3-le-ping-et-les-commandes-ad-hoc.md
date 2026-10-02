---
title: Chapitre 2.3 — Le ping et les commandes ad hoc
source: IT/08 Conteneurs & automatisation/Automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 2 — Inventaire et premières commandes
  - index.md
---

## Le minimum à savoir

Une **commande ad hoc** est une action Ansible lancée **directement en ligne de commande**, sans écrire de fichier. C'est parfait pour une action **ponctuelle** : vérifier que les machines répondent, lancer une commande rapide.

La structure d'une commande ad hoc :

```
ansible  <cible>  -m <module>  -a "<arguments>"
         ▲        ▲            ▲
         groupe   le module    les arguments
         ou hôte  à exécuter   du module
```


### Le premier réflexe : `ping`

Le tout premier test, c'est de vérifier qu'Ansible **joint** ses cibles, avec le module `ping` :

```bash
ansible all -i inventory.ini -m ansible.builtin.ping
```


> 🔀 **À ne pas confondre :** le `ping` d'Ansible n'est **pas** le `ping` réseau habituel (ICMP). Il vérifie qu'Ansible peut **se connecter en SSH** à la machine **et** y exécuter du Python. Un `ping` Ansible réussi prouve que **toute la chaîne fonctionne**.

### Une note sur les noms de modules (FQCN)

Tu remarques qu'on écrit `ansible.builtin.ping` et pas juste `ping`. C'est le **nom complet** du module (on parle de **FQCN**). On l'utilise pour **éviter les ambiguïtés** entre modules de même nom. Retiens simplement : **on écrit le nom complet `ansible.builtin.xxx`**. Pas besoin d'en savoir plus pour l'instant.

## Très utile en pratique

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

## Exemple simple

```bash
# "Est-ce que mes deux cibles répondent ?"
ansible web -i inventory.ini -m ansible.builtin.ping
```


Si les deux répondent `SUCCESS`, ton lab est prêt à travailler.

## ❌ Erreur classique

> **Un `ping` qui échoue avec `UNREACHABLE`, et chercher le problème dans Ansible.**

Si `ping` renvoie `UNREACHABLE`, le souci est dans la **connexion SSH**, pas dans Ansible (mauvaise IP, mauvaise clé, mauvais utilisateur, machine éteinte). Le réflexe correct : tester **`ssh utilisateur@cible` à la main**. Si ça échoue aussi, règle SSH d'abord (rappel : Partie 1).

## Exercices

### Guidé
Lance `ansible all -i inventory.ini -m ansible.builtin.ping`. Tes deux cibles doivent répondre `SUCCESS` / `pong`. Si l'une affiche `UNREACHABLE`, teste `ssh` à la main vers cette machine et corrige.

### Autonome
Avec le module `command`, récupère l'`uptime` (depuis quand la machine tourne) et l'espace disque (`df -h /`) de chaque cible. Tu viens de faire un petit **état des lieux** de ton parc en deux commandes.

### Défi
Cible **une seule** machine au lieu d'un groupe entier : `ansible cible1 -i inventory.ini -m ansible.builtin.ping`. Puis essaie de cibler le groupe `web` mais en te limitant à une machine. (Indice : il existe une option `--limit`. On la verra plus en détail en Partie 8.)

## ✅ Tu sais maintenant…

- Ce qu'est une **commande ad hoc** : agir en une ligne, sans playbook.
- La structure `ansible <cible> -m <module> -a "<args>"`.
- Le module **`ping`** comme premier test (SSH + Python), différent du ping réseau.
- Qu'on écrit les modules en **nom complet** (`ansible.builtin.xxx`).
- Lancer des commandes de lecture (`uptime`, `df`).

---
