---
title: Questions essentielles
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - index.md
---

- **Question :** Quelles sont les grandes phases de la réponse à incident ?
  - **Réponse type :** Le NIST 800-61 définit 4 phases : Préparation (avant l'incident — playbooks, outillage, exercices), Détection et Analyse (du signal faible à l'incident confirmé, triage, scoping), Confinement-Éradication-Restauration (isoler, nettoyer, reconstruire), et Post-Incident (retex, amélioration). En réalité, ces phases ne sont pas linéaires — on investigue pendant qu'on contient, on découvre de nouvelles compromissions pendant l'éradication. C'est itératif et parallèle.

- **Question :** Quelle est la différence entre un événement, une alerte, un incident et une crise ?
  - **Réponse type :** Un événement c'est tout fait observable dans le SI — il y en a des milliards par jour. Une alerte c'est un événement signalé comme potentiellement anormal par un système de détection. Un incident c'est une alerte confirmée qui compromet effectivement la confidentialité, l'intégrité ou la disponibilité. Une crise c'est un incident dont l'impact dépasse la capacité de réponse normale et nécessite une gouvernance exécutive. Ces distinctions déterminent le niveau de mobilisation, les processus activés, et les obligations de notification.

- **Question :** Un ransomware est en cours de déploiement — que faites-vous en priorité ?
  - **Réponse type :** Confinement immédiat. Chaque minute qui passe c'est des machines supplémentaires chiffrées. On isole les segments réseau touchés — on coupe la connectivité mais on n'éteint PAS les machines pour préserver la mémoire (qui contient les clés de chiffrement et les artefacts forensic). On désactive les comptes compromis. On protège les sauvegardes — si elles sont accessibles par les mêmes credentials, c'est la priorité absolue. En parallèle, on commence le scoping : l'attaquant est-il ailleurs dans le réseau ?

- **Question :** Pourquoi la préparation est-elle si importante en IR ?
  - **Réponse type :** Parce que le jour de l'incident, il est trop tard pour construire les processus. La préparation détermine tout : est-ce qu'on a un IRP avec des playbooks par type d'incident ? Est-ce qu'on a la télémétrie nécessaire pour investiguer ? Est-ce qu'on sait qui appeler à 2h du matin ? Est-ce qu'on a un contrat avec un prestataire PRIS ? Est-ce qu'on a testé la restauration des sauvegardes ? Une organisation préparée contient un ransomware en quelques heures. Une organisation non préparée met des semaines et paie souvent la rançon.

- **Question :** Comment construisez-vous une timeline d'attaque ?
  - **Réponse type :** La timeline reconstitue chronologiquement toutes les actions de l'attaquant. On croise plusieurs sources : les logs EDR/Sysmon (processus, connexions), les Event Logs Windows (4624 logons, 4698 scheduled tasks), les logs d'authentification AD, les logs proxy/DNS, et les artefacts forensic (prefetch, amcache, MFT). On cherche le point d'entrée initial, les pivots, les escalades de privilèges, les persistances, et les actions sur objectif. La timeline est le livrable central de l'investigation.
