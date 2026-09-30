---
title: Questions essentielles
source: IT/04_Active-Directory/Active_Directory.md
note: Active Directory
up:
- - Active Directory
  - index.md
---

- **Question :** Qu'est-ce qu'Active Directory et pourquoi c'est la cible principale des attaquants ?
  - **Réponse type :** Active Directory est l'annuaire centralisé de Microsoft qui gère les identités, les authentifications et les politiques de sécurité dans plus de 90 % des entreprises. C'est la cible n°1 parce que compromettre AD donne accès à tout : tous les comptes, toutes les machines, toutes les données. Les composants AD — les contrôleurs de domaine, le krbtgt, les comptes Domain Admin — sont classés Tier 0, le niveau de criticité le plus élevé.

- **Question :** Expliquez le fonctionnement de Kerberos en quelques étapes.
  - **Réponse type :** L'utilisateur s'authentifie auprès du KDC (le DC) et obtient un TGT — c'est le ticket qui prouve son identité. Ensuite, quand il veut accéder à un service, il présente son TGT au KDC qui lui délivre un TGS (ticket de service) pour ce service précis. Le service valide le ticket et autorise l'accès. Tout repose sur le secret du compte krbtgt, qui chiffre les TGT. Si un attaquant obtient ce hash, il peut forger des Golden Tickets — des TGT illimités.

- **Question :** Qu'est-ce que le Kerberoasting et comment s'en protéger ?
  - **Réponse type :** Le Kerberoasting exploite le fait que tout utilisateur du domaine peut demander un ticket de service (TGS) pour n'importe quel SPN. Ce ticket est chiffré avec le hash du compte de service — si le mot de passe est faible, on le cracke en offline. La défense principale c'est d'utiliser des gMSA (Group Managed Service Accounts), qui ont des mots de passe de 240 caractères rotés automatiquement. Sinon, il faut des mots de passe de 25+ caractères sur les comptes de service et forcer l'AES au lieu de RC4.

- **Question :** Qu'est-ce que le tiering model et pourquoi c'est important ?
  - **Réponse type :** Le tiering sépare l'environnement en trois niveaux : Tier 0 pour les DC et comptes Domain Admin, Tier 1 pour les serveurs, Tier 2 pour les postes utilisateurs. L'idée c'est d'empêcher le mouvement latéral vertical — un admin ne doit jamais utiliser un compte Tier 0 pour se connecter à une machine Tier 1 ou 2. Si un attaquant compromet un poste et qu'un DA a une session active dessus, il récupère le hash et c'est terminé. Le tiering casse cette chaîne.

- **Question :** Quelles sont les premières mesures de hardening AD que vous recommanderiez ?
  - **Réponse type :** Je commencerais par : activer l'Advanced Audit Policy sur tous les DC pour avoir de la visibilité, déployer LAPS pour avoir un mot de passe admin local unique par machine, séparer les comptes admin et utilisateur, activer le SMB signing obligatoire pour bloquer le relay NTLM, et désactiver LLMNR et NBT-NS pour empêcher le poisoning. Ce sont des quick wins à fort impact.
