---
title: Chapitre 20 — Active Directory forensics
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - ../index.md
- - Partie V — Investigation réseau ET identité
  - index.md
---

## 20.1 Pourquoi un chapitre dédié à l'AD

Dans 95 % des compromissions Windows, l'objectif stratégique de l'attaquant est le contrôle de l'Active Directory. L'AD gère l'authentification de tous les utilisateurs, les autorisations sur toutes les ressources, le déploiement de logiciel via GPO, et les secrets (hashes NTLM, clés Kerberos). Le forensic AD est donc une composante centrale de presque toute investigation Windows — et pourtant, il est rarement traité comme une discipline à part entière.

Ce chapitre couvre l'investigation AD sous l'angle forensic : quels artefacts analyser, quelles attaques détecter, et comment reconstituer la chronologie de la compromission AD. Il complète le Ch.14 (Event Logs) en se focalisant sur les artefacts spécifiques à l'AD, et le Ch.20 du cours IR (investigation identité) en allant plus en profondeur sur la technique.

## 20.2 Investigation des authentifications

Les Event Logs des DC sont la source primaire. Les patterns à rechercher : authentifications depuis des IP inhabituelles (le compte `svc-backup` se connecte habituellement depuis le serveur de sauvegarde — une connexion depuis un poste de travail est suspecte), authentifications à des heures inhabituelles (un admin qui se connecte à 3h du matin un dimanche), volume anormal d'échecs d'authentification depuis une même source (password spraying), et authentifications avec des comptes de service utilisés manuellement (les comptes de service ne devraient jamais être utilisés interactivement).

L'**ADTimeline** (outil de l'ANSSI) produit une timeline des modifications AD à partir des métadonnées de réplication — c'est l'outil de référence pour comprendre chronologiquement ce que l'attaquant a fait dans l'AD. Il parse les métadonnées de réplication (attributs `whenChanged`, `whenCreated`, `msDS-ReplAttributeMetaData`) pour reconstruire la séquence des modifications sans dépendre des Event Logs (qui peuvent avoir été effacés).

## 20.3 Investigation Kerberos

**Kerberoasting :** l'attaquant demande des TGS (Ticket Granting Service) pour des comptes de service ayant un SPN (Service Principal Name), puis cracke les tickets offline pour obtenir le mot de passe en clair. Détection forensic : Event ID 4769 avec encryption type 0x17 (RC4) en volume anormal depuis une seule machine. Interprétation : si un seul poste demande des TGS RC4 pour 10+ comptes de service en quelques minutes, c'est du Kerberoasting. L'attaquant a obtenu les tickets et les cracke offline — il n'y aura pas d'autre trace visible tant que le mot de passe n'est pas cracké et utilisé.

**DCSync :** l'attaquant simule un DC pour demander la réplication des hashes NTLM de tous les comptes. Détection forensic : Event ID 4662 avec les GUID de réplication (`1131f6ad-9c07-11d1-f79f-00c04fc2dcd2` pour DS-Replication-Get-Changes, `1131f6aa-...` pour DS-Replication-Get-Changes-All) provenant d'une machine qui n'est PAS un DC. C'est la preuve formelle que l'attaquant a récupéré tous les hashes — y compris le krbtgt.

**Golden Ticket :** l'attaquant forge un TGT avec le hash du krbtgt. Détection forensic : anomalies dans les tickets Kerberos — lifetime anormalement long (le Golden Ticket a souvent un lifetime de 10 ans alors que la politique du domaine est de 10 heures), SID qui ne correspond pas à un utilisateur existant, ou TGT sans événement de pré-authentification (4768) correspondant. La détection est difficile — c'est pourquoi la prévention (mots de passe krbtgt complexes, rotation régulière) est critique.

## 20.4 Investigation des modifications AD

Les modifications d'objets AD (comptes créés, groupes modifiés, GPO ajoutées, ACL modifiées) sont enregistrées dans les Event Logs (Event ID 5136 pour les modifications d'attribut via LDAP, Event IDs 4720/4728/4732 pour la gestion des comptes et groupes) et dans les métadonnées de réplication (parsables par ADTimeline).

L'analyse du fichier **ntds.dit** (la base de données AD, stockée sur les DC dans `C:\Windows\NTDS\`) avec **secretsdump.py** (Impacket) ou **DSInternals** (PowerShell) permet d'extraire les hashes NTLM de tous les comptes, de vérifier les mots de passe (comparaison avec des dictionnaires pour identifier les mots de passe faibles que l'attaquant a pu craquer), et d'auditer les comptes (date de création, date de dernière connexion, membership des groupes).

**BloodHound** (en mode défensif) peut être utilisé pour visualiser les chemins d'attaque que l'attaquant a pu emprunter : quels comptes avaient des droits sur quels systèmes, quels chemins menaient au Domain Admin, quelles ACL permettaient l'élévation de privilèges. C'est un outil offensif (utilisé par les pentesters et les attaquants pour la reconnaissance) qui est aussi un outil défensif puissant pour comprendre comment la compromission a été possible.

## 20.5 Fil rouge — MUSIC BOX : la compromission AD

> **🔬 MUSIC BOX — Épisode 17**
>
> L'investigation AD révèle la séquence complète :
>
> **ADTimeline :** 3 modifications critiques identifiées. (1) J-30 : création du compte `svc-monitor-temp` (ajouté au groupe Domain Admins). (2) J-14 : modification de l'attribut `msDS-AllowedToDelegateTo` sur le compte `svc-backup` — délégation Kerberos contrainte ajoutée, permettant l'impersonation d'administrateurs. (3) J-7 : création d'une GPO « Application Update Policy » dans une OU peu surveillée — contenu : script PowerShell de staging de données.
>
> **ntds.dit (secretsdump.py) :** extraction des hashes de tous les comptes. Comparaison avec la base Have I Been Pwned et un dictionnaire de mots de passe : 23 comptes ont des mots de passe faibles (< 12 caractères, mots du dictionnaire). Le compte `svc-backup` avait le mot de passe `NovaPharma2024!` — cracable en 2 heures avec un GPU moderne.

---
