---
title: Annexes
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - index.md
---

---


## Annexe A — Cheat Sheet AD

### Commandes PowerShell AD essentielles

```powershell
# --- UTILISATEURS ---
Get-ADUser -Identity alice -Properties *                    # Tout sur un user
Get-ADUser -Filter {Enabled -eq $true} -Properties lastLogonTimestamp  # Users actifs
Get-ADUser -Filter {adminCount -eq 1}                       # Comptes avec adminCount=1
Search-ADAccount -LockedOut                                  # Comptes verrouillés
Search-ADAccount -PasswordNeverExpires                       # MdP n'expire jamais
Search-ADAccount -AccountInactive -TimeSpan 90.00:00:00     # Inactifs 90j
Get-ADUser krbtgt -Properties PasswordLastSet                # Dernière rotation krbtgt

# --- GROUPES ---
Get-ADGroupMember -Identity 'Domain Admins' -Recursive       # Membres DA (récursif)
Get-ADPrincipalGroupMembership -Identity alice               # Groupes d'un user
Get-ADGroup -Filter {adminCount -eq 1}                       # Groupes privilégiés

# --- SPN (Kerberoasting surface) ---
Get-ADUser -Filter {ServicePrincipalName -ne '$null'} -Properties ServicePrincipalName

# --- DELEGATION ---
Get-ADComputer -Filter {TrustedForDelegation -eq $true}      # Unconstrained
Get-ADComputer -Filter {msDS-AllowedToDelegateTo -ne '$null'} # Constrained

# --- TRUSTS ---
Get-ADTrust -Filter *                                        # Tous les trusts

# --- PRE-AUTH (AS-REP Roasting surface) ---
Get-ADUser -Filter {DoesNotRequirePreAuth -eq $true}

# --- SHADOW CREDENTIALS ---
Get-ADUser -Filter {msDS-KeyCredentialLink -ne '$null'} -Properties msDS-KeyCredentialLink

# --- GPO ---
Get-GPO -All | Select DisplayName, ModificationTime
Get-GPResultantSetOfPolicy -ReportType Html -Path gpo.html

# --- RODC PRP ---
Get-ADDomainControllerPasswordReplicationPolicy -Identity RODC-GVA
```


### Requêtes LDAP courantes

```
# Tous les utilisateurs avec adminCount=1
(&(objectClass=user)(adminCount=1))

# Comptes avec SPN (Kerberoasting)
(&(objectClass=user)(servicePrincipalName=*)(!(objectClass=computer)))

# Comptes sans pré-auth (AS-REP Roasting)
(&(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=4194304))

# Unconstrained delegation
(&(objectClass=computer)(userAccountControl:1.2.840.113556.1.4.803:=524288))

# Comptes avec msDS-KeyCredentialLink (Shadow Credentials)
(&(objectClass=user)(msDS-KeyCredentialLink=*))
```


---


## Annexe B — Matrice Attaque / Détection / Remédiation

| Technique | Event IDs | Outils offensifs | Signal de détection | Faux positifs | Remédiation |
|-----------|-----------|-----------------|---------------------|---------------|-------------|
| Kerberoasting | 4769 | Rubeus, GetUserSPNs.py | Volume 4769 RC4 depuis un même compte | Monitoring légitime | gMSA, AES, MdP forts |
| AS-REP Roasting | 4768 | Rubeus, GetNPUsers.py | 4768 sans pré-auth | Comptes legacy | Activer pré-auth |
| Password Spraying | 4625, 4771 | Spray, DomainPasswordSpray | Volume 4625 même MdP | Oublis utilisateurs | Verrouillage, MFA |
| NTLM Relay | 4624 | ntlmrelayx, Responder | 4624 depuis source inhabituelle | Services légitimes | SMB/LDAP signing |
| PetitPotam | 4624 | PetitPotam.py | Auth DC vers machine non-DC | — | Patch, disable EFS RPC |
| Pass-the-Hash | 4624 (type 3/9) | Mimikatz, Impacket | Logon avec processus inhabituel | Admin légitime | Credential Guard, LAPS |
| DCSync | 4662 | Mimikatz, secretsdump | 4662 replication depuis non-DC | Backup légitime | Auditer droits replic. |
| Golden Ticket | — | Mimikatz | TGT durée anormale, SID inexistant | — | Rotation krbtgt |
| Silver Ticket | — | Mimikatz | Ticket sans TGS-REQ | — | PAC validation |
| Shadow Credentials | 5136 | Whisker, pywhisker | 5136 sur msDS-KeyCredentialLink | Windows Hello | Auditer ACLs, monitoring |
| ESC1 (AD CS) | 4887 | Certipy, Certify | Enrollment avec SAN ≠ demandeur | — | Supprimer SAN libre |
| ACL Abuse | 5136, 4662 | PowerView, BloodHound | Modification ACL sur objets sensibles | Admin changements | Audit BloodHound |
| AdminSDHolder | 5136 | PowerView | Modification AdminSDHolder | — | Monitoring dédié |
| DCShadow | 5137 | Mimikatz | Objet nTDSDSA inhabituel | — | Monitoring CN=Config |

---


## Annexe C — Event IDs critiques AD

| Event ID | Source | Description | Pertinence sécurité |
|----------|--------|-------------|-------------------|
| 4624 | Security | Logon succès | Type 3/9/10 = réseau/credentials, source inhabituelle = PtH |
| 4625 | Security | Logon échec | Volume = brute force/spraying |
| 4648 | Security | Explicit credentials | Utilisation de credentials différentes = mouvement latéral |
| 4662 | Security | Directory service access | Droits de réplication depuis non-DC = DCSync |
| 4672 | Security | Special privileges assigned | Nouveaux privilèges = escalade potentielle |
| 4720 | Security | Account created | Compte créé par l'attaquant ? |
| 4728/4732/4756 | Security | Member added to group | Ajout à un groupe privilégié = alerte |
| 4768 | Security | TGT request | Sans pré-auth = AS-REP Roasting |
| 4769 | Security | TGS request | RC4 en volume = Kerberoasting |
| 4771 | Security | Kerberos pre-auth failed | Volume = spraying |
| 4776 | Security | Validation NTLM | Repli hors de Kerberos, source inhabituelle |
| 4670 | Security | Permissions d'un objet modifiées | Objets Tier 0 |
| 4887 | Security | Certificate enrollment | SAN inhabituel = ESC1 abuse |
| 5136 | Security | Directory object modified | AdminSDHolder, GPO, ACL, msDS-KeyCredentialLink |
| 5137 | Security | Directory object created | Objet nTDSDSA = DCShadow |
| 7045 | System | Service installed | PsExec crée un service temporaire |
| 1 | Sysmon | Process creation | Mimikatz, Rubeus, SharpHound, PsExec |
| 3 | Sysmon | Network connection | C2 beaconing, mouvement latéral |
| 10 | Sysmon | Process access | lsass.exe access = credential dumping |
| 4104 | PowerShell | Script Block | PowerShell offensif = PowerView, etc. |

---


## Annexe D — Lab AD : monter son environnement de test

**Infrastructure minimale** : 1 VM Windows Server 2022 (DC01 — DC + DNS + AD CS), 1 VM Windows Server 2022 (SRV01 — serveur membre), 1 VM Windows 10/11 (PC01 — poste joint au domaine), 1 VM Kali Linux (attaquant). Total : ~16 Go RAM, 100 Go disque. Hyperviseur : VirtualBox, VMware Workstation, ou Proxmox.

**Configuration AD** : Promouvoir DC01 en DC (Install-WindowsFeature AD-Domain-Services + Install-ADDSForest), créer des OUs (IT, Finance, HR), créer des utilisateurs (dont au moins 1 DA, 1 compte de service avec SPN, 1 compte sans pré-auth), créer des groupes, joindre SRV01 et PC01 au domaine, déployer AD CS (Install-WindowsFeature ADCS-Cert-Authority + Install-AdcsCertificationAuthority), créer un template vulnérable ESC1, et configurer un trust (optionnel — 2ème forêt).

**Outils à installer** : Mimikatz, Rubeus, SharpHound/BloodHound CE, Certipy, Responder, Impacket, PowerView, PingCastle, Sysmon (avec config SwiftOnSecurity).

---


## Annexe E — MITRE ATT&CK mapping AD

| Tactique | Techniques AD clés | Sub-techniques |
|----------|-------------------|---------------|
| Reconnaissance | T1087 Account Discovery | .002 Domain Account |
| | T1069 Permission Groups Discovery | .002 Domain Groups |
| Credential Access | T1558 Steal or Forge Kerberos Tickets | .003 Kerberoasting, .001 Golden Ticket |
| | T1003 OS Credential Dumping | .001 LSASS Memory, .003 NTDS, .006 DCSync |
| | T1557 Adversary-in-the-Middle | .001 LLMNR/NBT-NS Poisoning |
| Lateral Movement | T1550 Use Alternate Authentication | .002 Pass the Hash, .003 Pass the Ticket |
| | T1021 Remote Services | .002 SMB, .006 WinRM |
| Persistence | T1098 Account Manipulation | .xxx Shadow Credentials |
| | T1484 Domain Policy Modification | .001 Group Policy Modification |
| Privilege Escalation | T1078 Valid Accounts | .002 Domain Accounts |
| | T1134 Access Token Manipulation | |
| Defense Evasion | T1207 Rogue Domain Controller | DCShadow |

---


## Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Cours complémentaires |
|-----------|----------------|----------------------|
| Active Directory (ce cours) | **Ce cours (AD)** | — |
| Infrastructure IT | **Cours Infra** | AD (Ch.21 Infra — AD comme socle, vue d'ensemble) |
| Détection SOC | **Cours SOC** | AD (Ch.19-22 — détection AD spécifique, Event IDs) |
| Incident Response | **Cours IR** | AD (Ch.27-29 — IR spécifique AD, rotation krbtgt, rebuild) |
| APT | **Cours APT** | AD (Ch.18 kill chain — APT29 Golden SAML, Ch.31 cloud attacks) |
| Windows en profondeur | **Cours Windows** | AD (Ch.5-7 — NTLM/Kerberos/lsass, complémentaire) |
| GRC | **Cours GRC** | AD (Ch.11 tiering — le tiering est une mesure de gouvernance) |
| CTI | **Cours CTI** | AD (Ch.14 BloodHound — même logique d'analyse de graphe) |

---


## Annexe G — Glossaire et ressources

### Glossaire (sélection)

| Terme | Définition |
|-------|-----------|
| **ACE** | Access Control Entry — entrée de contrôle d'accès |
| **ACL** | Access Control List — liste de contrôle d'accès (DACL/SACL) |
| **AdminSDHolder** | Objet dont les ACL sont propagées aux comptes privilégiés |
| **AGDLP** | Imbrication recommandée : comptes → groupes globaux → groupes domaine local → permissions |
| **Entra Connect** | Outil de synchronisation AD ↔ Entra ID (PHS, PTA, fédération) — Tier 0 |
| **LSASS** | Processus qui exécute la LSA : authentification, jetons, cache des tickets |
| **PIM** | Privileged Identity Management — rôles cloud activés à la demande |
| **Protected Users** | Groupe qui retire NTLM, RC4, la délégation et le cache aux comptes privilégiés |
| **SDDL** | Format texte d'un security descriptor (`O:…G:…D:(A;;…;;;AU)`) |
| **Security descriptor** | Owner, Primary Group, DACL et SACL d'un objet |
| **Tiering** | Séparation Tier 0 (identité) / Tier 1 (serveurs) / Tier 2 (postes) |
| **AS-REP** | Authentication Service Reply — réponse du KDC avec le TGT |
| **BloodHound** | Outil d'analyse de chemins d'attaque AD par graphe |
| **Credential Guard** | Isolation de lsass via Hyper-V contre Mimikatz |
| **DCSync** | Simulation de réplication DC pour extraire les hashes |
| **DFSR** | Distributed File System Replication — réplication SYSVOL |
| **ESC1-ESC8** | Escalation via Certificate Services — vulnérabilités AD CS |
| **FGPP** | Fine-Grained Password Policy — politique MdP différenciée |
| **FSMO** | Flexible Single Master Operations — rôles spéciaux DC |
| **GC** | Global Catalog — DC avec copie partielle de toute la forêt |
| **gMSA** | Group Managed Service Account — compte de service sécurisé |
| **Golden Ticket** | TGT forgé avec le hash krbtgt → accès illimité |
| **GPO** | Group Policy Object — politique de configuration/sécurité |
| **KDC** | Key Distribution Center — service Kerberos sur le DC |
| **Kerberoasting** | Crack offline de tickets de service (TGS) |
| **krbtgt** | Compte qui chiffre tous les TGT — cible n°1 |
| **LAPS** | Local Administrator Password Solution |
| **NTDS.dit** | Base de données AD (hashes de tous les comptes) |
| **NTLM** | NT LAN Manager — protocole d'authentification legacy |
| **OU** | Organizational Unit — conteneur d'objets AD |
| **PAC** | Privilege Attribute Certificate — SID + groupes dans le ticket |
| **PAW** | Privileged Access Workstation — poste admin durci |
| **PKINIT** | Authentification Kerberos par certificat |
| **PRP** | Password Replication Policy — politique du RODC |
| **PRT** | Primary Refresh Token — « TGT du cloud » |
| **RBCD** | Resource-Based Constrained Delegation |
| **RODC** | Read-Only Domain Controller |
| **SDProp** | Processus qui propage les ACL d'AdminSDHolder |
| **Shadow Credentials** | Abus de msDS-KeyCredentialLink via PKINIT |
| **SID** | Security Identifier — identifiant unique d'un objet |
| **Silver Ticket** | Service Ticket forgé avec le hash du compte de service |
| **SPN** | Service Principal Name — identifie un service Kerberos |
| **SYSVOL** | Partage répliqué entre DC (GPO, scripts) |
| **TGT / TGS** | Ticket Granting Ticket / Ticket Granting Service |
| **Trust** | Relation de confiance entre domaines/forêts |

### Ressources

| Ressource | Type | Focus |
|-----------|------|-------|
| harmj0y (blog) | Blog | Recherche offensive AD — BloodHound, Kerberos, AD CS |
| adsecurity.org (Sean Metcalf) | Blog | Défense AD — détection, hardening |
| thehacker.recipes | Wiki | Techniques d'attaque AD pas-à-pas |
| ired.team | Blog | Red team techniques avec exemples |
| SpecterOps (blog) | Blog | AD CS (ESC), BloodHound, recherche |
| The DFIR Report | Blog | Intrusions réelles analysées |
| PingCastle | Outil | Audit de maturité AD |
| BloodHound CE | Outil | Analyse de chemins d'attaque |

### Formations

| Formation | Organisme | Focus |
|-----------|----------|-------|
| CRTP (Certified Red Team Professional) | Altered Security | Attaque AD |
| CRTE (Certified Red Team Expert) | Altered Security | Attaque AD avancé + forêts |
| SANS SEC560 | SANS | Pentest réseau + AD |
| SANS SEC566 | SANS | Hardening AD |
| HTB CPTS | HackTheBox | Pentest avancé (incluant AD) |
| HTB Dante/Offshore/Zephyr | HackTheBox | Pro Labs AD |

---

---
