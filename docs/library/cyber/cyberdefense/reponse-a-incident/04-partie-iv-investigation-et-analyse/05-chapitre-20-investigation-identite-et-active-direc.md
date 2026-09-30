---
title: Chapitre 20 — Investigation identité et Active Directory
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie IV — Investigation ET analyse
  - index.md
---

## 20.1 Pourquoi l'AD est la cible ultime

Dans la quasi-totalité des compromissions Windows, l'objectif stratégique de l'attaquant est le contrôle de l'Active Directory. L'AD gère l'authentification de tous les utilisateurs, les autorisations sur toutes les ressources, le déploiement de logiciels et de configurations via GPO, et les secrets (hashes NTLM, clés Kerberos, mots de passe en clair dans certains cas). Compromettre l'AD signifie contrôler l'ensemble du SI Windows — c'est pourquoi l'investigation AD est la composante la plus critique de l'IR dans un environnement Windows.

## 20.2 Techniques d'attaque AD et leur détection

**Kerberoasting :** l'attaquant demande des TGS (Ticket Granting Service) pour des comptes de service ayant un SPN (Service Principal Name), puis cracke les tickets offline pour obtenir le mot de passe en clair. Détection : Event ID 4769 avec encryption type RC4 (0x17), en volume anormal. Implication IR : si un compte de service avec droits DA a un mot de passe faible, il a été compromis.

**DCSync :** l'attaquant simule un contrôleur de domaine pour demander la réplication des hashes NTLM de tous les comptes, y compris le krbtgt. Détection : Event ID 4662 avec les GUID de réplication (`1131f6ad-...` et `1131f6aa-...`), provenant d'une machine qui n'est pas un DC. Implication IR : si le DCSync a réussi, TOUS les hashes sont compromis — y compris le krbtgt (Golden Ticket possible).

**Golden Ticket :** l'attaquant forge un TGT (Ticket Granting Ticket) avec le hash du compte krbtgt, lui donnant un accès illimité au domaine, sans expiration normale. Détection : anomalies dans les tickets Kerberos (lifetime anormalement long, SID incohérent), Event ID 4769 avec des tickets dont les propriétés ne correspondent pas à la politique du domaine. Implication IR : si un Golden Ticket a été créé, l'attaquant peut s'authentifier comme n'importe quel utilisateur du domaine, même après un reset des mots de passe — seul un double reset du krbtgt invalide les Golden Tickets.

**Modifications d'ACL/DACL :** l'attaquant modifie les permissions sur des objets AD (OU, groupes, comptes) pour se donner des droits persistants (GenericAll, WriteDACL, AddMember). Ces modifications sont subtiles et difficiles à détecter sans un audit AD dédié. Outils de détection : BloodHound (visualisation des chemins d'attaque), PingCastle (score de sécurité AD et identification des faiblesses), Purple Knight (audit automatisé).

## 20.3 Évaluation de la profondeur de compromission

Les questions critiques que l'investigateur doit trancher pour déterminer le plan d'éradication :

Le **krbtgt est-il compromis ?** Si oui → le double reset est obligatoire (Ch.27). Un seul reset ne suffit pas car Kerberos retient les 2 derniers mots de passe du krbtgt — il faut donc 2 resets espacés de 12h minimum pour invalider tous les tickets.

Des **comptes admin cachés** ont-ils été créés ? Vérification de tous les groupes privilégiés (Domain Admins, Enterprise Admins, Schema Admins, Administrators, mais aussi les groupes avec des délégations non standard) et de toutes les créations de comptes récentes.

Des **GPO malveillantes** existent-elles ? Revue de toutes les GPO créées ou modifiées récemment — une GPO malveillante peut déployer du malware, désactiver des défenses, ou modifier des configurations de sécurité sur tout le parc.

Les **ACL/DACL** ont-elles été modifiées ? Des permissions anormales sur des objets critiques (OU des DC, OU des serveurs, comptes de service) peuvent permettre une re-compromission même après éradication.

## 20.4 Fil rouge — BLACKTIDE : la profondeur de la compromission AD

> **🔍 BLACKTIDE — Épisode 20**
>
> Samedi 14h00. Léa (PRIS, spécialiste AD) présente ses conclusions à la cellule technique.
>
> **DCSync confirmé** sur DC01 à J-14. L'attaquant a obtenu tous les hashes NTLM du domaine, y compris le hash du krbtgt. **→ Golden Ticket possible et probable.**
>
> **Golden Ticket utilisé.** L'analyse des logs Kerberos montre des TGT avec un lifetime de 10 ans (la politique du domaine est de 10 heures) — signature d'un Golden Ticket.
>
> **3 comptes admin cachés** créés à J-12 dans l'OU `OU=ServiceAccounts,OU=IT,DC=arvantis,DC=local` : `svc_monitor01`, `svc_backup_ext`, `svc_audit_temp`. Noms choisis pour se fondre dans les comptes de service légitimes. Tous membres du groupe Domain Admins.
>
> **1 GPO malveillante** : « Windows Update Configuration » créée à J-0, liée aux OU des serveurs de fichiers, exécutant le ransomware PhantomCrypt via un script de démarrage.
>
> **Modification des ACL** : GenericAll attribué au compte `svc_deploy` (le compte compromis) sur l'OU des serveurs critiques — permettant à ce compte de modifier n'importe quel objet dans cette OU.
>
> **DSRM password** : non modifié par l'attaquant (il n'en a pas eu besoin — le Golden Ticket lui suffisait).
>
> **Conclusion de Léa :** « L'AD est compromis en profondeur. Un simple reset de mots de passe ne suffit pas. Il faut un double reset du krbtgt, la suppression des 3 comptes cachés, le retrait de la GPO malveillante, et la correction des ACL. La reconstruction complète de l'AD n'est pas strictement nécessaire si ces actions sont menées proprement, mais le risque résiduel n'est pas nul. »

---
