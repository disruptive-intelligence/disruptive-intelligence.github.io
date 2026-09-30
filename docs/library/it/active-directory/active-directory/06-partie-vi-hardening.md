---
title: Partie VI — Hardening
source: IT/04_Active-Directory/Active_Directory.md
note: Active Directory
up:
- - Active Directory
  - index.md
---

---


## Chapitre 23 — Top 10 actions de hardening et quick wins

Par où commencer quand le temps et le budget sont limités. Les 10 actions par impact décroissant : (1) Activer Advanced Audit Policy sur tous les DC (visibilité), (2) Déployer LAPS sur tout le parc (supprime le PtH via admin local), (3) Séparer les comptes admin/user (pas de DA sur les postes), (4) Activer SMB signing obligatoire (bloque le relay), (5) Désactiver LLMNR et NBT-NS (bloque le poisoning Responder), (6) Rotater le krbtgt (double rotation — invalide tout Golden Ticket), (7) Auditer les ACLs avec BloodHound (identifier et couper les chemins), (8) Supprimer les comptes inactifs et SPNs inutiles (réduire la surface), (9) Activer Protected Users pour les comptes Tier 0 (protection renforcée), (10) Durcir les templates AD CS (bloquer ESC1-ESC8).

---


## Chapitre 24 — Hardening NTLM, Kerberos et authentification

Désactivation progressive de NTLM (audit d'abord : Network security: Restrict NTLM: Audit pour identifier les applications qui utilisent NTLM → corriger ou documenter les exceptions → puis restreindre par GPO). SMB signing obligatoire (GPO : Microsoft network server/client: Digitally sign communications always). LDAP signing et channel binding (bloque le relay LDAP — LDAP server signing requirements = Require signing). EPA (Extended Protection for Authentication — IIS, AD CS web enrollment). **Protected Users** (les membres ne peuvent pas : utiliser NTLM, être délégués, cacher les credentials, utiliser DES/RC4 pour Kerberos, avoir des TGT > 4h). **Credential Guard** (isolation de lsass dans un environnement virtuel via Hyper-V — empêche Mimikatz). PPL/RunAsPPL (protège lsass contre les injections — moins contraignant que Credential Guard mais contournable). FGPP (Fine-Grained Password Policy — politique différenciée : mots de passe longs pour les comptes de service, MFA pour les admins).

---


## Chapitre 25 — Hardening AD CS, GPO et Tier 0

**AD CS hardening** : auditer les templates (Certipy find, Invoke-PKIAudit — supprimer les SAN libres, restreindre enrollment, désactiver « Any Purpose »), activer HTTPS + EPA sur le web enrollment, CA racine hors ligne, surveiller les enrollments (Event 4887 centralisé), et auditer msDS-KeyCredentialLink (Shadow Credentials). **GPO hardening** : restreindre qui peut créer/modifier les GPO, auditer les modifications (5136), verrouiller les GPO critiques. **Tier 0 hardening** : DC sans accès internet, sans agent superflu, sans logiciel tiers, pas de compte de service non-gMSA, VLAN dédié, PAW obligatoire, monitoring maximal. **RODC hardening** : PRP minimale (seuls les comptes strictement nécessaires), pas de comptes privilégiés dans la PRP, auditer régulièrement les comptes cachés, surveiller les tentatives de réplication depuis le RODC.

> **🔴 KERBEROS — Épisode 6**
>
> Thomas teste le RODC de Genève. La PRP inclut 45 comptes dont 3 comptes de service Tier 1 — c'est trop large. Il compromet le RODC (accès physique simulé — le RODC est dans un local technique sans contrôle d'accès) et extrait les hashes des 45 comptes cachés. Parmi eux, svc_monitoring a GenericWrite sur un groupe IT — un chemin vers l'escalade. Le RODC, censé limiter l'exposition, a été configuré trop permissivement et devient un vecteur d'attaque. Recommandation : PRP réduite aux comptes strictement nécessaires pour le site (utilisateurs de Genève uniquement, pas de comptes de service Tier 1), et sécurisation physique du local.

---


## Chapitre 26 — Backup, restore et résilience AD

Pourquoi les backups AD sont critiques (un AD compromis sans backup sain = reconstruction from scratch = semaines d'arrêt). Les méthodes : **System State backup** (NTDS.dit, registre, SYSVOL, boot files — via Windows Server Backup, Veeam, ou outil spécialisé). La récupération : **authoritative restore** (restaurer un objet supprimé en le marquant comme autoritaire → la réplication le propage), **non-authoritative restore** (restaurer un DC et le laisser se re-synchroniser avec les autres DC), **bare metal restore** (reconstruire un DC from scratch à partir du backup). La **Corbeille AD** (Active Directory Recycle Bin — récupération d'objets supprimés pendant la durée de rétention — à activer impérativement). Les tests de restauration (tester régulièrement — la première fois ne doit PAS être le jour de l'incident). La réplication comme résilience (2 DC minimum, sur des sites différents).

---
