---
title: Questions complémentaires
source: IT/04_Active-Directory/Active_Directory.md
note: Active Directory
up:
- - Active Directory
  - index.md
---

- **Question :** Comment fonctionne BloodHound et quel est son intérêt ?
  - **Réponse type :** BloodHound modélise l'AD comme un graphe : les objets sont des nœuds, les relations et droits sont des arêtes. Il collecte les données avec SharpHound et permet de visualiser les chemins d'attaque vers Domain Admin. C'est aussi un outil défensif : en le lançant sur son propre AD, on identifie les chemins avant l'attaquant et on peut couper les nœuds de convergence — un seul nœud corrigé peut fermer des dizaines de chemins.

- **Question :** Qu'est-ce qu'un DCSync et comment le détecter ?
  - **Réponse type :** Un DCSync simule un contrôleur de domaine pour demander la réplication des hashes via le protocole de réplication AD. L'attaquant a besoin des droits DS-Replication-Get-Changes et DS-Replication-Get-Changes-All. Côté détection, c'est l'Event ID 4662 avec des droits de réplication depuis une machine qui n'est PAS un DC — ça doit être une alerte critique.

- **Question :** En cas de compromission AD avec suspicion de Golden Ticket, que faites-vous ?
  - **Réponse type :** La priorité c'est la double rotation du krbtgt : une première rotation, on attend 10-12 heures, puis la deuxième. Ça invalide tous les Golden Tickets existants. Il ne faut pas faire les deux rotations en même temps, sinon on casse toutes les sessions Kerberos légitimes. En parallèle, on isole les systèmes compromis sans les éteindre pour préserver la mémoire, et on cherche les autres mécanismes de persistence.

- **Question :** Quels sont les avantages de la deception (honey objects) dans un environnement AD ?
  - **Réponse type :** L'intérêt principal c'est le zéro faux positif. On crée des comptes pièges avec des attributs attractifs — un adminCount=1, un SPN, un vieux mot de passe — et toute interaction avec ces objets est forcément suspecte. Par exemple, un honey SPN déclenche une alerte immédiate dès qu'un attaquant fait du Kerberoasting. C'est une couche de détection très efficace et simple à mettre en place.


## Questions les plus probables en entretien

1. C'est quoi AD et pourquoi c'est critique ?
2. Expliquez Kerberos en quelques étapes.
3. Kerberoasting : principe et défense ?
4. Tiering model : c'est quoi et pourquoi ?
5. Top 5 mesures de hardening AD ?
6. DCSync : c'est quoi, comment détecter ?
7. BloodHound : utilité offensive et défensive ?
