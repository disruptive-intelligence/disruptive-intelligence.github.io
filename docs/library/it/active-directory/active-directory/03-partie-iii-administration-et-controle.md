---
title: Partie III — Administration ET contrôle
source: IT/04_Active-Directory/Active_Directory.md
note: Active Directory
up:
- - Active Directory
  - index.md
---

---


## Chapitre 9 — Group Policy (GPO) : configuration et sécurité

Les GPO sont des ensembles de paramètres appliqués aux utilisateurs et machines d'une OU. L'ordre d'application : **LSDOU** (Local → Site → Domain → OU — le dernier appliqué gagne, sauf « Enforced »). Le filtrage de sécurité (appliquer une GPO uniquement à certains groupes). Les GPO de sécurité essentielles : politique de mots de passe (longueur, complexité, historique, verrouillage), audit policy (Advanced Audit Policy — activer les bons Event IDs), restriction d'exécution (AppLocker/WDAC), Windows Firewall, PowerShell logging (Script Block + Module Logging).

Les GPO comme vecteur d'attaque : un attaquant qui a WriteDACL sur une GPO peut ajouter un scheduled task ou un script de login → exécution de code sur toutes les machines de l'OU liée. SYSVOL contient les GPO (\\domain\SYSVOL\domain\Policies\{GUID}) et NETLOGON contient les scripts de login — les deux sont accessibles en lecture par tous les utilisateurs du domaine.

---


## Chapitre 10 — Outils d'administration et requêtage

Les outils natifs (ADUC, GPMC, DNS Manager, AD Sites and Services). **PowerShell AD module** (Get-ADUser, Get-ADGroup, Get-ADComputer, Get-ADObject, Set-ADUser — les cmdlets essentielles). Les requêtes LDAP pour l'audit sécurité : comptes inactifs > 90j, mots de passe qui n'expirent jamais, comptes avec SPN (surface Kerberoasting), comptes sans pré-auth (AS-REP Roasting), unconstrained delegation, comptes avec adminCount=1. Les outils d'audit : **PingCastle** (score de maturité AD — 0 à 100, avec recommandations priorisées), **BloodHound** (analyse de chemins d'attaque — traité en profondeur au Ch.14), **Purple Knight** (audit Semperis), **ADRecon** (collecte structurée d'informations AD).

---


## Chapitre 11 — Tiering model et séparation des privilèges

Le principe : séparer les environnements en tiers de criticité pour empêcher le mouvement latéral vertical. **Tier 0** (DC, comptes Domain Admin, Enterprise Admin, AD CS, Azure AD Connect — zone la plus protégée : isolation réseau, PAW obligatoire, aucun accès internet, monitoring maximal). **Tier 1** (serveurs membres, comptes admin serveur — les admins Tier 1 ne se connectent JAMAIS à un DC ni à un poste Tier 2). **Tier 2** (postes de travail, comptes utilisateurs).

La **PAW** (Privileged Access Workstation — poste durci dédié à l'administration, sans internet, sans email, sans navigation). **LAPS** (Local Administrator Password Solution — mot de passe admin local unique et roté sur chaque machine, stocké dans AD). La réalité du terrain : le tiering complet est difficile — commencer par protéger le Tier 0 (séparer les comptes DA, interdire les connexions DA sur les postes, déployer LAPS).

---


## Chapitre 12 — Journalisation et audit AD

L'**Advanced Audit Policy** à activer sur tous les DC (Account Logon, Logon/Logoff, Object Access, DS Access, Policy Change, Account Management). Les **Event IDs critiques** : 4624 (logon succès), 4625 (logon échec), 4648 (explicit credentials), 4672 (special privileges), 4720 (account created), 4728/4732/4756 (member added to group), 4769 (TGS request), 4768 (TGT request), 5136 (directory object modified), 4662 (directory service access), 4887 (certificate enrollment). **Sysmon** sur les DC (Event 1 process creation, 3 network connection, 10 process access → lsass.exe, 13 registry). **PowerShell logging** (Script Block — Event 4104, Module Logging). La **centralisation** (WEF ou agent SIEM — les logs locaux sont effacés par l'attaquant). Le volume (des milliers d'événements/heure par DC — filtrage et priorisation essentiels).

---
