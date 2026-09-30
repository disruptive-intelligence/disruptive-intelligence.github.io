---
title: Chapitre 0.1 — Pourquoi Ansible existe
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 0 — Introduction
  - index.md
---

## Le minimum à savoir

Imagine que tu administres **un** serveur Linux. Tu te connectes en SSH, tu installes un paquet, tu modifies un fichier de configuration, tu redémarres un service. Cinq minutes, c'est réglé.

Maintenant, imagine que tu as **vingt** serveurs. La même tâche, vingt fois. À la main. Tu te connectes, tu tapes, tu recommences. C'est **long**, c'est **fastidieux**, et surtout : à la machine n°13, tu oublies une étape. Personne ne le remarque. Trois mois plus tard, cette machine se comporte différemment des autres, et personne ne sait pourquoi.

Ce problème porte un nom : la **dérive de configuration**. Des machines censées être identiques qui **divergent** lentement, parce qu'elles ont été modifiées à la main, à des moments différents, par des personnes différentes.

**Ansible existe pour résoudre exactement ça.** Au lieu de répéter les mêmes gestes machine par machine, tu **décris une fois** ce que tu veux, et Ansible l'applique à **toutes** les machines, de façon **identique** et **rejouable**.

> **En une phrase :** Ansible automatise l'administration de plusieurs machines, pour que tu ne répètes pas les mêmes commandes une par une, et pour que tes machines restent **cohérentes** dans le temps.

## Très utile en pratique

Voici les corvées d'admin que tu fais (ou ferais) à la main, et ce qu'Ansible change :

| À la main | Avec Ansible |
|-----------|--------------|
| Se connecter à chaque serveur pour installer un paquet | Une description, appliquée à toutes les machines |
| Refaire la même config sur 20 serveurs | Le même playbook, rejoué partout |
| Oublier une étape sur une machine | L'état décrit est appliqué **partout** pareil |
| Ne plus savoir quelles machines sont à jour | Rejouer pour **vérifier** et **corriger** d'un coup |

Tu n'as **rien à taper** dans ce chapitre. C'est de la mise en place mentale.

## Exemple simple

Sans Ansible, pour installer `htop` sur trois serveurs, tu ferais :

```bash
ssh serveur1     # puis : sudo apt install htop, puis exit
ssh serveur2     # puis : sudo apt install htop, puis exit
ssh serveur3     # puis : sudo apt install htop, puis exit
```


Avec Ansible, tu écriras **une seule** instruction qui s'applique aux trois d'un coup. Et si `htop` est déjà installé sur le serveur 2, Ansible le **constatera** et ne fera rien sur celui-là. C'est ça, l'idée de départ.

## ❌ Erreur classique

> **Croire qu'Ansible sert juste à « lancer une commande à distance plus vite ».**

C'est un raccourci trompeur. Lancer une commande sur plusieurs machines, une boucle SSH le fait aussi. Ce qu'Ansible apporte en plus, c'est l'**état souhaité** et l'**idempotence** : tu décris un **résultat** que tu peux **rejouer sans risque**, pas une commande à exécuter une fois. On verra la différence concrète très vite.

## Exercices

### Guidé
Sur une feuille (ou un fichier texte), écris **3 tâches** que tu fais ou ferais à la main pour administrer un serveur Linux (par exemple : « installer un paquet », « créer un utilisateur », « démarrer un service »). Pour chacune, imagine que tu doives la faire sur **10 machines** : note ce qui devient pénible ou risqué.

### Autonome
Décris en quelques lignes une situation (vécue ou imaginée) où **deux machines censées être identiques** se sont mises à se comporter différemment. Qu'est-ce qui a divergé ? Comment l'aurais-tu remarqué ?

### Défi
Explique à un proche **non technique**, en 4-5 phrases, ce que fait Ansible — **sans** utiliser les mots « playbook » ni « serveur ». Utilise une image (une recette qu'on rejoue à l'identique, un chef qui donne les mêmes instructions à toute une brigade…).

## ✅ Tu sais maintenant…

- **Pourquoi** Ansible existe : éviter de répéter les tâches d'admin machine par machine.
- Ce qu'est la **dérive de configuration** (des machines identiques qui divergent).
- Qu'Ansible applique un **état souhaité**, de façon **identique** et **rejouable**.
- Qu'Ansible n'est **pas** seulement « lancer des commandes à distance ».

---
