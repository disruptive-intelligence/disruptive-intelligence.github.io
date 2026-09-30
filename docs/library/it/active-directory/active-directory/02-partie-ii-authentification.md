---
title: Partie II — Authentification
source: IT/04_Active-Directory/Active_Directory.md
note: Active Directory
up:
- - Active Directory
  - index.md
---

*Le cœur d'AD — les protocoles qui authentifient les utilisateurs et les services.*

---


## Chapitre 5 — NTLM : le protocole legacy qui refuse de mourir

Le challenge/response NTLM en 4 étapes : négociation (le client demande une connexion), challenge (le serveur envoie un nombre aléatoire), response (le client chiffre le challenge avec le hash de son mot de passe), et vérification (le serveur transmet au DC qui vérifie). **NTLMv1** est cryptographiquement cassable en minutes. **NTLMv2** est plus résistant mais reste vulnérable au relay. Les faiblesses structurelles : pas d'authentification mutuelle (le client ne vérifie pas le serveur → relay possible), hash = clé (Pass-the-Hash), et le hash transite sur le réseau (capture via Responder).

Pourquoi NTLM persiste : accès par IP au lieu du nom DNS, applications legacy, machines non jointes au domaine, certains proxy. Le **Net-NTLMv2 hash** est le hash capturé sur le réseau — crackable offline si le mot de passe est faible, relayable vers d'autres services. Le poisoning **LLMNR/NBT-NS/mDNS** : quand un client ne résout pas un nom via DNS, il tombe en fallback sur des protocoles broadcast (LLMNR port 5355, NBT-NS port 137) — un attaquant avec Responder répond à ces requêtes et capture les hashes NTLM des clients.

> **🔴 KERBEROS — Épisode 2**
>
> Thomas lance Responder sur le VLAN utilisateurs de Meridian. En 15 minutes, il capture 4 hashes Net-NTLMv2 — dont celui de m.laurent (responsable qualité) dont le mot de passe (Pharma2024!) cède en 8 secondes avec hashcat. LLMNR et NBT-NS sont actifs sur tout le parc.

---


## Chapitre 6 — Kerberos : le flux complet et les subtilités

Le principe fondamental : les mots de passe ne transitent jamais sur le réseau — système de tickets chiffrés. Les **5 étapes** : AS-REQ (le client envoie son identité + timestamp chiffré par son hash = pré-authentification), AS-REP (le KDC vérifie et renvoie un TGT chiffré par la clé krbtgt — le client ne peut pas lire le TGT mais peut le présenter), TGS-REQ (le client présente le TGT et demande un ticket de service pour un SPN), TGS-REP (le KDC renvoie un TGS chiffré par la clé du compte de service cible), AP-REQ (le client présente le TGS au serveur cible qui le déchiffre avec sa propre clé).

Les composants : **KDC** (Key Distribution Center — hébergé sur chaque DC), **TGT** (valide 10h, renouvelable 7j, chiffré par krbtgt), **TGS** (spécifique à un service/SPN, chiffré par le hash du compte de service), **PAC** (Privilege Attribute Certificate — contient le SID de l'utilisateur et ses groupes, inclus dans le ticket), **pré-authentification** (empêche de demander des TGT sans connaître le mot de passe — si désactivée : AS-REP Roasting).

Les **SPN** (Service Principal Name) : identifient un service de manière unique (format service/hostname:port — MSSQLSvc/sql01.meridian.local:1433). Tout utilisateur du domaine peut demander un ticket pour n'importe quel SPN. Si le ticket est chiffré avec le hash d'un compte de service dont le mot de passe est faible → crack offline = **Kerberoasting**.

La **délégation Kerberos** : **Unconstrained** (le service reçoit le TGT complet de l'utilisateur → très dangereux, l'attaquant qui compromet le service récupère tous les TGT des utilisateurs qui s'y connectent), **Constrained** (S4U2Proxy — le service ne peut déléguer que vers des services listés dans msDS-AllowedToDelegateTo), **RBCD** (Resource-Based Constrained Delegation — c'est la ressource cible qui définit qui peut déléguer vers elle via msDS-AllowedToActOnBehalfOfOtherIdentity → abus si l'attaquant contrôle un compte machine).

Le **compte krbtgt** chiffre tous les TGT. Compromettre son hash = forger n'importe quel TGT = **Golden Ticket**. Si le krbtgt n'a jamais été roté (vérifier : Get-ADUser krbtgt -Properties PasswordLastSet), c'est un red flag majeur.

---


## Chapitre 7 — Où sont stockés les secrets et comment ils sont volés

Le **NTDS.dit** (base AD sur les DC — hashes NTLM de TOUS les comptes, historique de MdP ; extraction = compromission totale ; méthodes : ntdsutil, Volume Shadow Copy, DCSync). La **SAM** (Security Account Manager — hashes des comptes locaux sur chaque machine ; extraction : reg save, secretsdump ; risque : même mot de passe admin local partout → LAPS est la solution). Les **LSA Secrets** (registre — mots de passe de comptes de service, clés de chiffrement, mot de passe machine ; accessibles avec SYSTEM). La **mémoire lsass.exe** (tickets Kerberos, hashes NTLM, parfois mots de passe en clair — Mimikatz, Pypykatz, comsvcs.dll MiniDump ; protection : Credential Guard, PPL/RunAsPPL). Les **Group Policy Preferences** (cpassword — mots de passe chiffrés en AES-256 avec une clé publiée par Microsoft → déchiffrement trivial ; corrigé par MS14-025 mais les GPP historiques restent souvent en place).

---


## Chapitre 8 — AD CS : PKI interne, certificats et surface d'attaque

*AD CS est devenu l'un des vecteurs d'attaque les plus exploités — les vulnérabilités ESC transforment une PKI interne en machine à fabriquer des Domain Admin.*

L'architecture AD CS : CA racine (idéalement hors ligne), CA subordonnée (en ligne, émet les certificats), templates de certificats (définissent ce que le certificat autorise et qui peut le demander), enrollment (demande automatique ou manuelle), et auto-enrollment (les machines reçoivent automatiquement leurs certificats). Usages légitimes : certificats machines pour 802.1X, certificats VPN, certificats SSL internes, authentification par certificat (PKINIT/smart card).

Les **vulnérabilités ESC** (Escalation via Certificate Services — documentées par SpecterOps) : **ESC1** (le template permet au demandeur de spécifier un SAN arbitraire → demander un certificat au nom d'un Domain Admin ; conditions : Client Authentication + CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT + permissions d'enrollment pour les utilisateurs), **ESC2** (le template permet « Any Purpose » ou « SubCA » → certificat utilisable pour tout), **ESC3** (un agent d'enrollment peut demander des certificats au nom d'autres utilisateurs), **ESC4** (les ACL du template sont trop permissives → un utilisateur peut modifier le template pour le rendre ESC1), **ESC6** (le flag EDITF_ATTRIBUTESUBJECTALTNAME2 est activé sur la CA → tout template devient ESC1), **ESC7** (un utilisateur a le droit ManageCA → peut activer le flag ESC6), **ESC8** (le web enrollment est en HTTP sans EPA → NTLM relay vers le web enrollment → certificat au nom de n'importe qui).

Outils : **Certify** (C# — énumération et exploitation), **Certipy** (Python — énumération, exploitation, et extraction de certificats). Hardening AD CS : auditer les templates (Invoke-PKIAudit, Certipy find), supprimer les SAN libres (CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT), restreindre les permissions d'enrollment, désactiver « Any Purpose », activer HTTPS + EPA sur le web enrollment, et surveiller les enrollments (Event 4887).

> **🔴 KERBEROS — Épisode 3**
>
> Thomas lance Certipy contre Meridian : `certipy find -u t.granier@meridian.local -p '...' -dc-ip 10.0.1.10`. Résultat : ESC1 sur le template « VPN-User » — Client Authentication activé, CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT activé, et l'enrollment est autorisé pour « Authenticated Users ». Thomas demande un certificat avec le SAN de l'admin DA admin.ssi@meridian.local. Le certificat est émis en 3 secondes. Il utilise PKINIT pour obtenir un TGT de Domain Admin. L'ensemble de l'attaque a pris 90 secondes depuis la découverte du template vulnérable. La Blue Team n'a rien vu — les logs AD CS n'étaient pas centralisés vers le SIEM.

---
