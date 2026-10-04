---
title: Chapitre 12 — Journalisation et audit AD
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - ../index.md
- - Partie III — Administration et contrôle
  - index.md
---

## 12.1 Activer la bonne politique d'audit

La politique d'audit par défaut est insuffisante. On active l'**Advanced Audit Policy** par GPO sur les DC (et une politique adaptée sur les serveurs et postes) :

| Catégorie | Sous-catégories clés | Pour voir |
|---|---|---|
| Account Logon | Kerberos Authentication Service, Kerberos Service Ticket Operations, Credential Validation | Demandes de tickets, validations NTLM |
| Logon/Logoff | Logon, Special Logon | Ouvertures de session, sessions privilégiées |
| Account Management | User / Security Group / Computer Account Management | Créations, ajouts aux groupes |
| DS Access | Directory Service Changes, Directory Service Access | Modifications d'objets, opérations sensibles |
| Policy Change | Audit Policy Change, Authentication Policy Change | Désactivation d'audit, changements de politique |
| Detailed Tracking | Process Creation (avec ligne de commande) | Exécution de programmes |

Les modifications d'objets (5136) nécessitent en plus une **SACL** sur les objets à surveiller (§4.9).

## 12.2 Les événements de référence

| Event ID | Signification |
|---|---|
| 4624 / 4625 | Ouverture de session réussie / échouée (le *Logon Type* précise interactif, réseau, RDP…) |
| 4634 / 4647 | Fermeture de session |
| 4648 | Ouverture de session avec identifiants explicites |
| 4672 | Privilèges spéciaux attribués à une session (session administrateur) |
| 4720 / 4722 / 4725 / 4726 | Compte créé / activé / désactivé / supprimé |
| 4723 / 4724 | Changement / réinitialisation de mot de passe |
| 4728 / 4732 / 4756 | Membre ajouté à un groupe global / local / universel |
| 4740 | Compte verrouillé |
| 4768 / 4769 / 4771 | Ticket TGT demandé / ticket de service demandé / échec de pré-authentification Kerberos |
| 4776 | Validation d'identifiants NTLM |
| 4662 / 5136 / 5137 | Opération sur un objet / objet modifié / objet créé |
| 4887 | Certificat délivré par AD CS |
| 1102 | Journal de sécurité effacé |

## 12.3 Compléter la télémétrie

- **PowerShell** : *Script Block Logging* (4104) et *Module Logging* (4103) ;
- **Sysmon** sur les DC et serveurs sensibles : création de processus, connexions réseau, accès aux processus sensibles comme `lsass.exe` ;
- **AD CS** : journalisation de la CA (demandes, émissions, modifications de modèles) ;
- **DNS** : journal des requêtes sur les DC.

## 12.4 Centraliser et dimensionner

Un journal local peut être effacé ou écrasé : les événements doivent partir vers un **SIEM** (agent ou *Windows Event Forwarding*). Un DC produit des milliers d'événements par heure : on dimensionne la taille des journaux, on filtre à la source ce qui n'a aucune valeur, et on construit des **baselines** (qui s'authentifie où, à quelle heure, avec quels comptes de service) pour que les écarts ressortent. La Partie V détaille la détection.

---
