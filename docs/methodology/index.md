# Méthodologie

Le **quand** : chaque phase est une checklist courte qui renvoie vers les fiches détaillées
(Services, Outils, Active Directory…), qui sont le **quoi**.

| # | Phase | Question |
|---|---|---|
| 0 | [Préparation](../start/checklist.md) | Suis-je prêt ? |
| 1 | [Reconnaissance passive](01-passive-recon.md) | Que sait-on sans toucher la cible ? |
| 2 | [Reconnaissance active](02-active-recon.md) | Quels hôtes, quels ports ? |
| 3 | [Énumération](03-enumeration.md) | Que révèle chaque service ? |
| 4 | [Accès initial](04-initial-access.md) | Comment entrer ? |
| 5 | [Élévation de privilèges](05-privesc.md) | Comment devenir admin ? |
| 6 | [Mouvement latéral](06-lateral-movement.md) | Où aller ensuite ? |
| 7 | [Post-exploitation](07-post-exploitation.md) | Que récupérer, que documenter ? |

!!! tip "Ce n'est pas linéaire"
    On revient souvent en arrière : un nouvel accès = nouvelle énumération.

## Port → fiche { #port-fiche }

| Port | Service | Fiche |
|---|---|---|
| 88 | Kerberos | [Kerberos](../services/kerberos.md) |
| 139, 445 | SMB | [SMB](../services/smb.md) |

!!! note "À compléter"
    Ajouter une ligne à chaque nouvelle fiche service.
