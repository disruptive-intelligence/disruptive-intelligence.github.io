---
title: Chapitre 21 — Le serveur de fichiers
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE III — Les serveurs et l'exécution
  - index.md
---

## 21.1 À quoi ça sert

Stocker des documents accessibles par les postes, avec des droits par dossier.

**Pourquoi ça existe encore.** Malgré les outils collaboratifs, le partage de fichiers reste le socle documentaire de la majorité des organisations — parce qu'il est simple, universel, et qu'il ne demande aucun apprentissage.

## 21.2 Ce qu'il fait à la donnée

Il la conserve **sans la structurer**. C'est ce qui le rend à la fois indispensable et incontrôlable : **personne ne sait exactement ce qu'il contient**. C'est le sujet du chapitre 8 du volume Asset Management.

## 21.3 Le problème des droits

```
   Année 1    Une arborescence propre, des droits par service
   Année 2    « Marie a besoin d'accéder à ce dossier »  → droit individuel
   Année 3    Un projet transverse  → un groupe créé pour l'occasion
   Année 4    Le projet est fini. Le groupe existe toujours
   Année 5    Marie change de service. Son droit individuel reste
   Année 8    Plus personne ne sait qui a accès à quoi
```


⚠️ **Les droits sur un partage de fichiers ne se réduisent jamais spontanément.** Chaque exception ajoutée y reste, et l'arborescence devient inauditable en quelques années. C'est le même mécanisme que les règles de pare-feu — §10.3 — et la même conclusion : **ce qui s'accumule sans processus de retrait devient ingérable**.

## 21.4 S'il disparaît

Les utilisateurs perdent leurs documents partagés.

⚠️ **Une distinction importante pour la vue service** : **le service métier ne s'arrête pas toujours, mais le travail s'arrête.** Un service de commande en ligne continue de fonctionner sans le partage de fichiers ; l'équipe qui le pilote, non. C'est le §35.4 — dégradation contre arrêt.

🔥 **SCÉNARIO — le partage est chiffré par un rançongiciel**

| Question | Réponse |
|---|---|
| Symptôme | Les fichiers sont illisibles. Le serveur fonctionne |
| Hypothèse naïve | « Le serveur a été compromis » |
| Dépendance réelle | **Un poste utilisateur**, avec les droits de son utilisateur — mini-lab 3 |
| Ce que le schéma aurait dû montrer | **Les postes**, absents de la quasi-totalité des schémas — §6.1 |
| Ce qui décide de la suite | **La sauvegarde est-elle atteignable depuis le même compte ?** Si oui, elle est chiffrée aussi |

⚠️ **La dernière ligne est celle qui décide de la gravité.** Un rançongiciel qui atteint les sauvegardes transforme un incident en catastrophe. **La question de conception : la sauvegarde est-elle accessible depuis le réseau bureautique, et avec quel compte ?**

## 21.5 Sur un schéma

Une boîte isolée en zone interne, souvent sans trait — comme l'annuaire. Tous les postes s'y connectent, personne ne le dessine.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est sur le P: » | Un lecteur réseau monté | **Vers quel serveur ? Quels droits ?** |
| « Tout le monde y a accès » | Les droits sont larges | « Tout le monde » inclut-il les comptes de service et les prestataires ? |
| « On a des snapshots » | Des copies existent | **Sont-elles atteignables par un compte compromis ?** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Partager des documents avec des droits | **Une arborescence de droits qui devient inauditable** |
| Centraliser pour sauvegarder | Un volume qui croît sans limite naturelle |
| Offrir un accès simple | **Une cible de choix pour un rançongiciel** |

---
