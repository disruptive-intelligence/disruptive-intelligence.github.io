---
title: Partie IV — Attaques AD
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - index.md
---

*Comprendre comment AD est attaqué pour mieux défendre — chaque technique avec mécanisme, outils, preuves et détection.*

---


## Chapitre 13 — Reconnaissance et énumération

Tout utilisateur du domaine peut énumérer l'intégralité de l'AD via LDAP. Les outils : **BloodHound/SharpHound** (collecte et analyse de chemins d'attaque — traité en détail au Ch.14), **ADRecon** (collecte structurée), **PowerView** (énumération PowerShell — Get-DomainUser, Get-DomainGroup, Get-DomainComputer, Find-LocalAdminAccess), **ldapsearch** (requêtes LDAP depuis Linux), **Enum4linux** (énumération SMB/RPC).

Ce que l'attaquant cherche en priorité : comptes avec SPN → Kerberoasting surface, comptes sans pré-auth → AS-REP Roasting, comptes avec unconstrained delegation → cible de coercion, groupes privilégiés et leurs membres (Domain Admins, Enterprise Admins — combien de DA ? des comptes de service DA ?), ACLs permissives sur les objets critiques (GenericAll, WriteDACL), GPOs modifiables, trusts entre domaines/forêts, machines avec des sessions admin actives (Find-DomainUserLocation), et le RODC (PRP — quels comptes sont cachés ?).

> **🔴 KERBEROS — Épisode 4**
>
> Thomas lance SharpHound en mode « All » — en 90 secondes, il a le graphe complet de Meridian : 47 chemins vers Domain Admin, 12 comptes avec SPN dont 8 avec des mots de passe > 3 ans, 1 serveur avec unconstrained delegation (SRV-PRINT01), et le RODC de Genève dont la PRP inclut 45 comptes — dont 3 comptes de service Tier 1.

---


## Chapitre 14 — BloodHound et analyse de chemins d'attaque

*L'outil qui a transformé la sécurité AD — il rend visible ce qui était invisible.*

Le concept : modéliser l'AD comme un graphe (les nœuds = objets AD, les arêtes = relations/droits) et trouver les chemins du compte compromis au Domain Admin. La collecte **SharpHound** (modes : Default — sessions + groupes + ACLs, All — tout, DCOnly — uniquement les données du DC ; les données collectées : sessions actives, appartenances aux groupes, ACLs, trusts, SPNs, délégation). L'analyse : **shortest paths** vers Domain Admin, shortest paths depuis les comptes « owned », **nœuds de convergence** (les objets par lesquels passent le plus de chemins — les couper ferme le plus de chemins), et les droits dangereux visualisés (GenericAll, WriteDACL, ForceChangePassword, AddMember, ReadLAPSPassword).

L'**utilisation défensive** : lancer BloodHound sur son propre AD pour identifier les chemins AVANT l'attaquant, supprimer les ACLs inutiles, couper les chemins critiques (remédier un seul nœud de convergence peut fermer 30 chemins), et valider après remédiation. **BloodHound CE** (Community Edition — version moderne, interface web, API, stockage Neo4j). Fil rouge : Thomas analyse le graphe de Meridian — un chemin passe par svc_monitoring (compte de service avec GenericWrite sur le groupe « IT-Admins » qui a WriteDACL sur le DC). La Blue Team n'avait jamais vu ce chemin.

---


## Chapitre 15 — Credential attacks

Kerberoasting, AS-REP, relay et coercion

**Kerberoasting** : tout utilisateur demande un TGS pour un SPN → le ticket est chiffré avec le hash du compte de service → crack offline (hashcat -m 13100, john). Cible : comptes de service avec SPN et mot de passe faible. Outils : Rubeus kerberoast, GetUserSPNs.py. Défense : gMSA (mot de passe 240 caractères roté automatiquement), AES au lieu de RC4, comptes de service avec mots de passe forts (25+ caractères).

**AS-REP Roasting** : comptes avec DONT_REQUIRE_PREAUTH → l'AS-REP contient des données chiffrées avec le hash du compte → crack offline. Outils : Rubeus asreproast, GetNPUsers.py. Défense : activer la pré-auth sur tous les comptes (aucune raison de la désactiver sauf cas exceptionnel documenté).

**Password Spraying** : tester 1-2 mots de passe communs contre tous les comptes — sous le seuil de verrouillage. Outils : Spray, DomainPasswordSpray. Détection : 4625 en volume, 4771 KDC_ERR_PREAUTH_FAILED.

**NTLM Relay** : intercepter une authentification NTLM et la relayer vers un autre service — l'attaquant agit au nom de la victime. Chaîne typique : coercion ou Responder → ntlmrelayx → cible (LDAP pour DCSync/RBCD abuse, AD CS web enrollment pour ESC8, SMB pour exécution de code). Les **coercions** (forcer une machine à s'authentifier vers l'attaquant) : **PetitPotam** (abus EFS RPC — le DC s'authentifie vers l'attaquant → relay vers LDAP → DCSync), **PrinterBug/SpoolSample** (abus du spooler d'impression), **DFSCoerce** (abus DFS). Les coercions de DC sont les plus dangereuses. Défenses : SMB signing obligatoire, LDAP signing + channel binding, EPA sur IIS et AD CS, désactiver le spooler sur les DC, patcher PetitPotam.

---


## Chapitre 16 — Mouvement latéral, escalade et ACL abuse

**Pass-the-Hash** (utiliser un hash NTLM volé pour s'authentifier — fonctionne car NTLM ne vérifie pas le mot de passe mais le hash ; outils : Mimikatz sekurlsa::pth, Impacket psexec/wmiexec/smbexec ; détection : 4624 logon type 3/9 avec processus inhabituel). **Pass-the-Ticket** (utiliser un ticket Kerberos volé ; outils : Mimikatz sekurlsa::tickets, Rubeus). **Overpass-the-Hash** (convertir un hash NTLM en ticket Kerberos — plus discret).

**ACL Abuse** : GenericAll sur un utilisateur → réinitialiser son mot de passe, GenericAll sur un groupe → s'ajouter comme membre, WriteDACL → modifier les ACL pour s'accorder des droits, WriteOwner → prendre la propriété, ForceChangePassword → changer le mot de passe, AddSelf/AddMember → s'ajouter à un groupe, GenericWrite sur un compte → modifier le SPN (targeted Kerberoasting) ou modifier msDS-KeyCredentialLink (Shadow Credentials — voir ci-dessous). Outils : PowerView (Add-DomainObjectAcl), BloodHound (visualisation), Impacket dacledit. Détection : Event 5136 sur objets sensibles, 4662.

**Shadow Credentials** : l'attaquant qui a GenericWrite ou WriteDACL sur un compte utilisateur ou machine peut modifier l'attribut **msDS-KeyCredentialLink** pour ajouter une clé publique qu'il contrôle. Ensuite, il utilise PKINIT pour s'authentifier en tant que ce compte sans connaître son mot de passe — en obtenant un TGT via le certificat associé à la clé. L'attaque est puissante car elle ne modifie pas le mot de passe du compte (moins de bruit), elle fonctionne avec PKINIT (Kerberos, pas NTLM), et elle est persistante tant que la clé n'est pas supprimée de l'attribut. Outils : **Whisker** (C# — ajout de la clé), **pywhisker** (Python), puis **Rubeus** (obtention du TGT via PKINIT). Pré-requis : AD CS déployé avec au moins un DC qui supporte PKINIT, et GenericWrite/WriteDACL sur le compte cible. Détection : Event 5136 sur l'attribut msDS-KeyCredentialLink, Event 4768 avec certificat (pré-auth type 16). Défense : auditer les modifications de msDS-KeyCredentialLink, restreindre les ACL (qui a GenericWrite sur les comptes critiques ?), monitorer les authentifications PKINIT depuis des sources inhabituelles.

Les techniques d'exécution à distance : PsExec (crée un service temporaire — Event 7045), WMI (Event 4688 + wmiprvse.exe), WinRM/PowerShell Remoting (Event 4624 logon type 3 + 4688 wsmprovhost.exe), DCOM, schtasks (tâche planifiée à distance). Chaque technique a un profil de détection différent.

---


## Chapitre 17 — Persistence

Golden Ticket, Shadow Credentials et au-delà

**Golden Ticket** (forger un TGT avec le hash krbtgt → accès illimité, durée arbitraire ; fonctionne même après reset de tous les mots de passe — tant que krbtgt n'est pas roté ; détection : TGT avec durée anormale, SID inexistant, absence d'AS-REQ correspondant). **Silver Ticket** (forger un Service Ticket avec le hash d'un compte de service → accès au service ciblé sans passer par le KDC ; plus discret — pas de TGS-REQ ; détection : PAC validation, ticket sans TGS-REQ). **DCSync** (simuler un DC pour demander la réplication des hashes — droits requis : DS-Replication-Get-Changes + DS-Replication-Get-Changes-All ; outils : Mimikatz lsadump::dcsync, Impacket secretsdump ; détection : Event 4662 avec droits de réplication depuis une machine non-DC = alerte critique).

**Shadow Credentials comme persistence** : l'attaquant qui a déjà compromis un compte DA peut ajouter une clé dans msDS-KeyCredentialLink d'un compte machine (DC par exemple) et maintenir un accès persistant via PKINIT, même après rotation du mot de passe du compte. Combiné avec un UnPAC-the-Hash (obtenir le hash NTLM du compte via le TGT PKINIT), cette persistence survit aux rotations de mots de passe classiques.

**Golden Certificate** (compromettre la clé privée de la CA → forger des certificats pour n'importe quel utilisateur → persistence tant que la CA n'est pas reconstruite ; c'est la persistence la plus durable — la clé privée de la CA a une durée de vie de 5-20 ans). **AdminSDHolder Persistence** (modifier les ACL d'AdminSDHolder → SDProp réapplique automatiquement les ACL sur tous les comptes adminCount=1 toutes les 60 min). **Skeleton Key** (injection dans lsass sur le DC — mot de passe « maître » pour tous les comptes ; survit au reboot uniquement si persistance via patch). **DCShadow** (enregistrer un faux DC pour pousser des modifications via la réplication — extrêmement discret ; détection : objets nTDSDSA inhabituels).

---


## Chapitre 18 — Kill chain AD typique : du phishing au Domain Admin

Scénario réaliste complet en 8 étapes : (1) Phishing → accès initial (C2), (2) Reconnaissance AD (SharpHound — 47 chemins vers DA), (3) Kerberoasting du compte svc_backup (mot de passe : Backup2019!), (4) Mouvement latéral (WMI vers SRV-APP01 avec les credentials svc_backup — admin local), (5) Credential dumping (Mimikatz sur SRV-APP01 → hash de bob.admin — Domain Admin qui avait une session active sur ce serveur Tier 1 — violation de tiering), (6) Pass-the-Hash vers le DC avec le hash de bob.admin, (7) DCSync (extraction de tous les hashes y compris krbtgt), (8) Golden Ticket + Golden Certificate pour la persistence.

Mapping MITRE ATT&CK complet. Temps réel observé : quelques heures dans un environnement peu durci — 30 minutes dans les cas les plus rapides. Où la défense aurait pu stopper la chaîne : gMSA pour svc_backup (Kerberoasting impossible), LAPS (admin local unique par machine), Credential Guard (Mimikatz bloqué), tiering (bob.admin ne devrait pas avoir de session Tier 1), détection DCSync (Event 4662), rotation krbtgt (invalide le Golden Ticket), audit AD CS (Golden Certificate détecté).

Fil rouge : Thomas réalise 2 kill chains sur Meridian — chemin 1 (classique : Kerberoasting → PtH → DCSync) et chemin 2 (AD CS : ESC1 → certificat DA → PKINIT → TGT DA). La Blue Team détecte le chemin 1 (alert sur le Kerberoasting — volume anormal de 4769 RC4) mais manque le chemin 2 (logs AD CS non centralisés).

---
