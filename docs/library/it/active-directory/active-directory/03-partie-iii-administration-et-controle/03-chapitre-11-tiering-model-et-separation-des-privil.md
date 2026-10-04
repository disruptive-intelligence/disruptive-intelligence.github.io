---
title: Chapitre 11 — Tiering model et séparation des privilèges
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - ../index.md
- - Partie III — Administration et contrôle
  - index.md
---

## 11.1 Le problème que résout le tiering

Quand un administrateur ouvre une session sur une machine, des éléments de son authentification restent en mémoire sur cette machine (Ch.7). Si un **Domain Admin** se connecte sur un poste utilisateur compromis, l'attaquant qui contrôle ce poste peut récupérer de quoi agir au nom de ce Domain Admin. Le tiering casse cette chaîne en interdisant aux identités privilégiées de s'exposer sur des machines moins fiables.

## 11.2 Les trois niveaux

| Tier | Ressources | Identités |
|---|---|---|
| **Tier 0** | DC, AD CS, Entra Connect, ADFS, sauvegardes de l'AD, hyperviseurs des DC, outils capables de contrôler l'AD (déploiement, EDR, supervision avec droits admin) | Domain / Enterprise Admins, comptes d'administration Tier 0 |
| **Tier 1** | Serveurs et applications métier | Administrateurs serveurs |
| **Tier 2** | Postes de travail, terminaux | Support poste, utilisateurs |

> **Règle fondamentale.** Un secret d'un tier supérieur ne doit **jamais** être exposé sur un tier inférieur. Un compte Tier 0 ne se connecte qu'à des ressources Tier 0, depuis un poste Tier 0.

Le Tier 0 ne se limite pas aux DC : tout ce qui peut **contrôler** un DC en fait partie (les sauvegardes qui contiennent NTDS.dit, la console de virtualisation qui héberge les DC, l'outil qui pousse des scripts sur tous les serveurs…).

## 11.3 Des comptes séparés par usage

```text
camille           → bureautique, messagerie, navigation (aucun droit admin)
camille.adm.t2    → administration des postes
camille.adm.t1    → administration des serveurs
camille.adm.t0    → administration de l'AD, depuis une PAW uniquement
```


## 11.4 Les outils du tiering

| Mesure | Rôle |
|---|---|
| **PAW** (*Privileged Access Workstation*) | Poste durci dédié à l'administration : pas de messagerie, pas de navigation, contrôle applicatif, Credential Guard |
| **Restrictions d'ouverture de session** (GPO *Deny log on locally / through RDP / as a batch job / as a service*) | Empêcher techniquement un compte Tier 0 de se connecter en Tier 1 ou 2 |
| **Authentication Policies et Silos** | Restreindre depuis quelles machines un compte peut obtenir un ticket |
| **Protected Users** | Groupe qui retire aux comptes privilégiés les mécanismes d'authentification les plus exposés (Ch.24) |
| **LAPS** | Mot de passe administrateur local unique par machine (§11.5) |
| **Administration à distance sans exposition** | *Restricted Admin* / *Remote Credential Guard* pour RDP |

## 11.5 LAPS

Sans LAPS, le compte administrateur local a souvent le **même mot de passe sur tout le parc** : un poste compromis donne accès à tous les autres. **Windows LAPS** génère un mot de passe unique par machine, le stocke dans un attribut protégé d'AD (ou dans Entra ID) et le renouvelle périodiquement.

```text
PC01 → secret A      PC02 → secret B      PC03 → secret C
```


Points de contrôle : droits de lecture du mot de passe réservés à un groupe restreint, consultation journalisée, rotation après usage, suivi des machines qui ne renouvellent plus leur secret. LAPS ne protège pas les comptes du domaine : c'est une brique, pas le tiering entier.

## 11.6 La réalité du terrain

Le tiering complet est un projet long. L'ordre réaliste :

1. inventorier le Tier 0 (y compris les systèmes qui contrôlent indirectement l'AD) ;
2. séparer les comptes d'administration de l'AD des comptes bureautiques ;
3. interdire par GPO les connexions Tier 0 sur postes et serveurs ;
4. déployer LAPS ;
5. fournir des PAW aux administrateurs Tier 0 ;
6. étendre ensuite au Tier 1.

---
