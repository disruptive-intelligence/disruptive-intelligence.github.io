---
title: Chapitre 4.1 — YAML sans peur
source: IT/08 Conteneurs & automatisation/Automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 4 — YAML et premiers playbooks
  - index.md
---

## Le minimum à savoir

Les playbooks Ansible s'écrivent en **YAML**, un format texte fait pour être **lisible par un humain**. Pas de programmation : juste des **clés**, des **valeurs** et des **listes**, organisées par l'**indentation**.

Les trois briques de base :

```yaml
# 1. Une paire clé : valeur
nom: serveur-web
actif: true

# 2. Une liste (chaque élément commence par un tiret)
paquets:
  - nginx
  - htop
  - git

# 3. Un dictionnaire imbriqué (l'indentation crée la hiérarchie)
serveur:
  nom: web1
  ip: 192.168.56.11
```


### LA règle d'or : l'indentation

> **En YAML, l'indentation EST la structure.** Elle se fait avec des **espaces**, **jamais** avec des tabulations. La convention : **2 espaces** par niveau, et on reste **cohérent** dans tout le fichier.

```yaml
# ✅ CORRECT
serveur:
  nom: web1
  ip: 192.168.56.11

# ❌ FAUX (ip n'est plus dans serveur)
serveur:
  nom: web1
ip: 192.168.56.11
```


Un fichier YAML commence souvent par `---` (qui marque le début du document).

## Très utile en pratique

```bash
# Vérifier qu'un fichier YAML / playbook est syntaxiquement correct (sans rien exécuter)
ansible-playbook playbook.yml --syntax-check
```


> 🔍 **Réflexe diagnostic :** `--syntax-check` attrape les erreurs d'indentation **avant** toute exécution. C'est gratuit et instantané. Prends l'habitude de le lancer dès qu'un YAML te résiste.

## Exemple simple

```yaml
---
serveur:
  nom: web1
  paquets:
    - nginx
    - htop
```


Lisible, non ? C'est tout l'intérêt du YAML : on **comprend** le fichier en le lisant.

## ❌ Erreur classique

> **Mélanger tabulations et espaces, ou se tromper de niveau d'indentation.**

C'est **l'**erreur YAML par excellence. Un copier-coller depuis le web introduit une tabulation invisible, et Ansible refuse le fichier avec un message parfois obscur. Le réflexe correct : configure ton éditeur pour afficher les caractères invisibles et **convertir les tabs en espaces**, et lance `--syntax-check` au moindre doute. La plupart des « bugs Ansible » des débutants sont des **bugs d'indentation**.

## Exercices

### Guidé
Écris un petit fichier YAML décrivant un serveur (un nom, une liste de 3 paquets, un sous-dictionnaire). Lance `ansible-playbook ton_fichier.yml --syntax-check`. Corrige jusqu'à ce qu'il n'y ait plus d'erreur de syntaxe.

### Autonome
Prends ton fichier et **casse-le** volontairement : décale une ligne, ou ajoute une tabulation. Lance `--syntax-check` et observe le message d'erreur. Apprends à relier le message à la cause.

### Défi
Réécris ton inventaire INI (Partie 2) au format **YAML** dans la tête (clés/listes). Ce n'est pas obligatoire pour le cours, mais ça t'entraîne à « penser en YAML » : hôtes, groupes, variables sous forme de clés et de listes.

## ✅ Tu sais maintenant…

- Que les playbooks s'écrivent en **YAML** : clés/valeurs, listes, dictionnaires.
- Que **l'indentation EST la structure** (espaces, jamais de tabs, 2 espaces par niveau).
- Vérifier la syntaxe avec **`--syntax-check`**.
- Que la plupart des « bugs Ansible » débutants sont des **bugs d'indentation**.

---
