---
title: Chapitre 4 — Autorisations, ACL et modèle de sécurité
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - ../index.md
- - Partie I — Fondations
  - index.md
---

Tout objet dans AD possède un **Security Descriptor** composé de : l'**Owner** (propriétaire — peut modifier les ACL), la **DACL** (liste d'ACE qui définissent qui a le droit de faire quoi sur l'objet), et la **SACL** (liste d'ACE qui définissent ce qui est audité — génère les Event Logs).

Les **ACE** (Access Control Entries) sont de type Allow ou Deny, avec des droits standard (Read, Write, Delete) et des droits étendus spécifiques à AD. Les **droits dangereux** : **GenericAll** (contrôle total — modifier l'objet, réinitialiser le mot de passe, s'ajouter aux groupes), **GenericWrite** (modifier les attributs — notamment ServicePrincipalName pour un targeted Kerberoasting, ou msDS-KeyCredentialLink pour Shadow Credentials), **WriteDACL** (modifier les permissions de l'objet — s'accorder GenericAll), **WriteOwner** (prendre la propriété → puis modifier les ACL), **ForceChangePassword** (réinitialiser le mot de passe sans connaître l'ancien), **Self** (s'ajouter soi-même à un groupe), **Extended Rights DS-Replication-Get-Changes + DS-Replication-Get-Changes-All** (DCSync).

L'**héritage** des ACL : les ACL se propagent dans l'arborescence — une ACL permissive sur une OU s'applique à tous les objets en dessous. **AdminSDHolder** : le processus SDProp réapplique les ACL d'AdminSDHolder sur tous les objets avec adminCount=1 toutes les 60 minutes — un attaquant qui modifie les ACL d'AdminSDHolder obtient un accès persistant à tous les comptes privilégiés (persistence — Ch.17).

---
