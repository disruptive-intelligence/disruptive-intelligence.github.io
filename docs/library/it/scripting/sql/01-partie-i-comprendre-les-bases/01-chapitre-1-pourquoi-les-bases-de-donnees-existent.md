---
title: Chapitre 1 — Pourquoi les bases de données existent
source: IT/07 Scripting & programmation/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie I — Comprendre les bases
  - index.md
---

## Le minimum à savoir

### Le problème : pourquoi pas Excel ?

Imagine que tu gères une médiathèque avec un fichier Excel. Une feuille pour les livres, une pour les lecteurs, une pour les emprunts. Au début, tout va bien. Puis, peu à peu :

- Le fichier dépasse 50 000 lignes — il devient lent à ouvrir
- Deux personnes veulent le modifier en même temps — l’une perd son travail
- Tu cherches “tous les emprunts d’Alice Martin” — il faut faire un filtre, copier-coller, recouper avec une autre feuille
- Tu écris “Allice Martin” dans une ligne et “Alice Martin” dans une autre — Excel ne sait pas que c’est la même personne
- Tu envoies le fichier par mail à un collègue, il en fait une copie, modifie sa version — laquelle est la vraie ?

C’est exactement le problème que les **bases de données** résolvent.

### Qu’est-ce qu’une base de données ?

Une base de données est un système conçu pour :

- **Stocker** beaucoup de données de manière structurée
- **Chercher** rapidement, même dans des millions de lignes
- **Gérer** plusieurs utilisateurs en même temps sans conflits
- **Garantir** la cohérence des données (pas de doublons, pas d’incohérences)
- **Sécuriser** l’accès (qui peut lire, qui peut modifier)
- **Sauvegarder** et restaurer en cas de problème

Tu interagis avec elle via un **langage** : SQL.

### Où trouve-t-on des bases de données ?

**Partout.** Chaque fois que tu utilises une application qui mémorise quelque chose, il y a probablement une base de données derrière :

|Application                  |Ce que la base stocke                      |
|-----------------------------|-------------------------------------------|
|Site e-commerce              |Produits, clients, commandes, paiements    |
|Réseau social                |Utilisateurs, posts, messages, likes       |
|Application bancaire         |Comptes, transactions, virements           |
|Outil RH                     |Salariés, contrats, congés, paies          |
|Système de tickets (helpdesk)|Tickets, utilisateurs, échanges            |
|SIEM (cybersécurité)         |Logs, alertes, indicateurs de compromission|
|Bibliothèque/médiathèque     |Livres, lecteurs, emprunts, retards        |

Comprendre SQL te donne accès à **toutes ces données** — c’est l’une des compétences les plus universelles en informatique.

### Excel vs base de données : la comparaison

|Aspect            |Excel / fichier texte      |Base de données            |
|------------------|---------------------------|---------------------------|
|Volume            |Quelques milliers de lignes|Millions, milliards        |
|Recherche         |Lente, manuelle            |Rapide, structurée         |
|Multi-utilisateurs|Conflits fréquents         |Géré nativement            |
|Cohérence         |Aucune garantie            |Contraintes strictes       |
|Relations         |Difficile                  |Natif (jointures)          |
|Sécurité          |Fichier protégé ou pas     |Permissions par utilisateur|
|Sauvegarde        |Manuelle                   |Automatisable              |
|Langage           |Formules Excel             |SQL (universel)            |


> **À retenir :** Excel n’est pas mauvais — il est parfait pour de petits volumes et de l’analyse ponctuelle. Mais dès qu’il faut **stocker durablement**, **partager** et **chercher efficacement**, la base de données est l’outil adapté.

> **📋 FIL ROUGE — Épisode 1**
> 
> Premier jour de Nora à la médiathèque. La directrice lui montre l’organisation actuelle : un fichier Excel “Liste_lecteurs_2024_v17_final_def.xlsx” et une autre feuille pour les emprunts. Trois personnes ont chacune leur propre version sur leur poste. Pour savoir si Alice Martin a rendu son livre, il faut ouvrir deux fichiers et croiser à la main. Heureusement, l’ancien stagiaire informatique a laissé une **base SQLite** `bibliotheque.db` mais personne ne sait l’utiliser. C’est ce que Nora va apprendre.

## ✅ Tu sais maintenant…

- Pourquoi les fichiers Excel atteignent vite leurs limites
- Ce qu’apporte une base de données (volume, recherche, cohérence, multi-utilisateurs)
- Que SQL est le langage universel pour parler aux bases de données
- Que les bases de données sont partout — apprendre SQL ouvre l’accès à toutes les applications qui en utilisent

-----
