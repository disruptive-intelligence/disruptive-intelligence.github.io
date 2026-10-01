---
title: Chapitre 5 — Pourquoi la préparation détermine tout
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - 'Partie II — Préparation : avant que l''incident n''arrive'
  - index.md
---

## 5.1 Le constat récurrent des retex

Dans la quasi-totalité des post-mortems d'incidents majeurs, les problèmes les plus graves ne sont pas techniques mais organisationnels. L'IRP existait mais n'avait jamais été testé — le jour J, personne ne savait où le trouver ni comment l'appliquer. Les contacts d'escalade étaient obsolètes — le RSSI avait changé de numéro 6 mois plus tôt. Les logs critiques n'étaient pas collectés — le PowerShell script block logging n'était pas activé, rendant l'investigation sur le mouvement latéral quasi impossible. Les sauvegardes étaient sur le même réseau que les serveurs de production — le ransomware les a chiffrées en même temps. Le canal de communication de crise n'était pas prévu — quand le serveur de messagerie a été chiffré, l'équipe s'est retrouvée sans moyen de communiquer.

Ces défaillances ne sont pas des « malchances » — ce sont des défauts de préparation identifiables et corrigeables avant l'incident. Chaque euro investi dans la préparation en économise dix ou cent en réponse.

## 5.2 Les trois dimensions de la préparation

La préparation technique couvre les outils, les logs, les sauvegardes, la capacité d'isolation réseau, et les accès d'urgence. La préparation organisationnelle couvre les processus (IRP, playbooks, escalade), les rôles (qui fait quoi), les contrats (prestataire PRIS, assurance, exercices), et les relations (ANSSI, forces de l'ordre, CERT sectoriel). La préparation humaine couvre la formation (les analystes savent-ils utiliser Volatility ?), les réflexes (le SOC sait-il qu'il ne faut pas redémarrer un serveur compromis ?), et la capacité à fonctionner sous stress (l'IR lead a-t-elle déjà géré un incident majeur, même en exercice ?).

Négliger une seule dimension rend les deux autres insuffisantes. Un SIEM parfaitement configuré ne sert à rien si personne ne sait lire les alertes. Un IRP impeccable ne sert à rien si les logs ne sont pas collectés. Une équipe brillante ne sert à rien si elle n'a pas les outils pour investiguer.

## 5.3 Le plan de réponse à incident (IRP)

L'IRP est le document fondateur de la capacité IR d'une organisation. Il doit contenir le périmètre d'application (quels systèmes, quels sites, quels processus sont couverts), la taxonomie des incidents adoptée (cohérente avec la classification du Ch.1), les critères de classification et de gravité (P1 à P4, avec des critères objectifs et des exemples), les critères de bascule en crise (repris du Ch.3), les rôles et contacts (à jour — c'est le point le plus souvent défaillant), les playbooks par type d'incident (ou pointeurs vers les playbooks séparés — Ch.7), les procédures d'escalade (qui appelle qui, dans quel ordre, avec quels critères), les modèles de communication pré-rédigés (premier message aux employés, premier SitRep à la direction, notification ANSSI, notification CNIL), les listes de diffusion (qui doit être informé à chaque niveau de gravité), et les arbres de décision (couper le réseau ? notifier l'ANSSI ? activer l'assurance ?).

Un IRP opérationnel fait 10 à 20 pages, pas 85. Il est stocké hors du SI principal (version papier, clé USB, cloud personnel du RSSI) car le SI peut être indisponible pendant l'incident. Il est mis à jour au minimum semestriellement et après chaque incident. Et il est testé en exercice au moins une fois par an (Ch.10).

> **Piège fréquent :** L'IRP « vitrine » — un document de 100 pages, magnifiquement rédigé, validé par la direction, rangé dans un tiroir, et jamais lu par les opérationnels. Le jour de l'incident, personne ne l'ouvre. Un IRP efficace est court, concret, et connu de tous les acteurs.

## 5.4 Fil rouge — BLACKTIDE : l'état de préparation d'Arvantis

> **🔍 BLACKTIDE — Épisode 5**
>
> L'IRP d'Arvantis existe — un document de 85 pages rédigé 2 ans plus tôt par un consultant externe, validé par la direction, stocké sur SharePoint. Il n'a jamais été testé en conditions réelles. Le numéro du prestataire PRIS est à jour. Celui de l'ANSSI aussi. Le numéro personnel du DPO a changé il y a 3 mois — l'IRP n'a pas été mis à jour. Nadia l'a dans son téléphone — elle le retrouve. Par chance.
>
> L'IRP couvre les grandes lignes (escalade, classification, notification) mais ne contient pas de playbook ransomware détaillé. Il ne mentionne pas la procédure de double reset du krbtgt. Il ne traite pas l'articulation IT/OT. Et surtout : il est stocké sur SharePoint, qui est hébergé sur l'infrastructure Microsoft 365 d'Arvantis — si l'attaquant avait compromis le tenant M365, l'IRP aurait été inaccessible.

---
