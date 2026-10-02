---
title: Chapitre 7.2 — copy vs template (bien choisir)
source: IT/08 Conteneurs & automatisation/Automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 7 — Templates et handlers
  - index.md
---

## Le minimum à savoir

Maintenant que tu connais les deux, voici comment **choisir** :

| Situation | Module à utiliser |
|-----------|-------------------|
| Le fichier est **identique** sur toutes les machines | **`copy`** |
| Le fichier doit **varier** selon la machine (nom, IP, port…) | **`template`** |
| Tu veux ajuster **une seule ligne** d'un fichier existant | **`lineinfile`** (Partie 5) |

> **En résumé :** `copy` = fichier figé, `template` = fichier généré, `lineinfile` = une ligne. Trois outils, trois usages.

## Très utile en pratique

Beaucoup de fichiers de configuration réels (nginx, ssh…) contiennent des valeurs spécifiques à la machine. Dans la vraie vie, on utilise donc surtout **`template`** pour les configs, et `copy` pour les fichiers statiques (un script, une image, un fichier de licence).

## Exemple simple

- Un logo identique partout → `copy`.
- Une config nginx avec le nom du serveur → `template`.

## ❌ Erreur classique

> **Hésiter entre les deux et choisir au hasard.**

Le réflexe correct est simple : **« est-ce que ce fichier doit être différent selon la machine ? »** Si oui → `template`. Si non → `copy`. Cette seule question tranche presque toujours.

## Exercices

### Guidé
Liste trois fichiers que tu pourrais déployer (par exemple : un logo, une config nginx, un script). Pour chacun, dis si tu utiliserais `copy` ou `template`, et **pourquoi**.

### Autonome
Prends un fichier que tu as déployé avec `copy` et qui gagnerait à être personnalisé. Transforme-le en `template` avec au moins une variable. Compare le résultat sur deux machines.

### Défi
Explique en quelques lignes pourquoi, dans un vrai projet, on utilise surtout `template` pour les fichiers de configuration. Qu'apporte la génération dynamique par rapport à des copies figées ?

## ✅ Tu sais maintenant…

- Choisir entre **`copy`** (identique), **`template`** (généré) et **`lineinfile`** (une ligne).
- La question qui tranche : « ce fichier doit-il varier selon la machine ? ».
- Que les configs réelles utilisent surtout **`template`**.

---
