---
title: Révision — Active Directory
revision: it/active-directory
domaine: IT
sources:
- IT/03 Active Directory/Active Directory.md
---

*D'après le cours [Active Directory](../it/active-directory/active-directory/index.md)*

## Questions essentielles

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

## Questions complémentaires

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

## Réponses flash

- **AD** → Annuaire centralisé Microsoft, SSO, 90 % des entreprises, cible n°1 (accès total si compromis).
- **Kerberos** → Client → TGT (via krbtgt) → TGS (via SPN) → accès service. Secret = hash krbtgt.
- **Kerberoasting** → Demande TGS pour SPN → crack offline. Défense = gMSA, mots de passe 25+ chars, AES.
- **Tiering** → Tier 0 (DC/DA), Tier 1 (serveurs), Tier 2 (postes). Jamais de connexion cross-tier.
- **Hardening quick wins** → Audit Policy, LAPS, séparation comptes, SMB signing, désactiver LLMNR.
- **DCSync** → Fausse réplication pour extraire hashes. Détection = 4662 depuis non-DC.
- **Golden Ticket** → TGT forgé avec hash krbtgt. Remédiation = double rotation krbtgt espacée de 10-12h.
- **BloodHound** → Graphe AD, chemins vers DA, nœuds de convergence. Offensif ET défensif.

---

> **Note de clôture**
>
> Ce cours a été conçu comme LA référence Active Directory de la bibliothèque — la ressource complète pour comprendre, attaquer, défendre et répondre à incident sur AD.
>
> L'opération KERBEROS illustre une réalité que tout professionnel cyber constate sur le terrain : la majorité des compromissions AD exploitent des fondamentaux négligés. Un compte de service avec un SPN et un mot de passe de 5 ans. Un template AD CS avec le SAN libre. Un Domain Admin qui a une session active sur un serveur Tier 1. Un krbtgt jamais roté depuis la création du domaine. Un RODC avec une PRP trop large. Un LLMNR actif. Ce ne sont pas des vulnérabilités exotiques — ce sont des configurations par défaut que personne n'a durcies.
>
> Le cours assume deux convictions. Première : comprendre l'attaque est le prérequis pour défendre efficacement — chaque technique offensive est présentée avec son mécanisme, ses outils, ses preuves, ET sa détection et sa remédiation. Deuxième : aucune mesure seule ne suffit — c'est la défense en profondeur (hardening + détection + deception + IR) qui protège AD. Un Golden Ticket est forgeable, mais si le krbtgt est roté régulièrement, les sessions sont monitorées, et les honey accounts sont en place, l'attaquant est détecté avant d'atteindre son objectif.
>
> *Comprendre le mécanisme • Exploiter la faiblesse • Détecter le signal • Durcir la configuration • Répondre à l'incident — avec méthode et profondeur.*
