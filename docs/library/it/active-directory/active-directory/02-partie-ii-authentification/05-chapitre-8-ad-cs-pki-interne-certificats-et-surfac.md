---
title: 'Chapitre 8 — AD CS : PKI interne, certificats et surface d''attaque'
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - ../index.md
- - Partie II — Authentification
  - index.md
---

*AD CS est devenu l'un des vecteurs d'attaque les plus exploités — les vulnérabilités ESC transforment une PKI interne en machine à fabriquer des Domain Admin.*

## 8.1 Architecture et usages

| Élément | Rôle |
|---|---|
| **CA racine** | Sommet de la chaîne de confiance ; idéalement **hors ligne** |
| **CA subordonnée (émettrice)** | En ligne, elle émet les certificats |
| **Modèles de certificats** (*templates*) | Définissent l'usage du certificat (EKU), qui peut le demander, comment le sujet est construit |
| **Inscription** (*enrollment*) | Demande manuelle ou automatique (*auto-enrollment* par GPO) |
| **NTAuth** | Magasin AD des CA autorisées à émettre des certificats d'**authentification** au domaine |

Usages légitimes : 802.1X, VPN, TLS interne, signature, chiffrement EFS, **ouverture de session par certificat** (carte à puce, PKINIT). Ce dernier usage fait de la PKI un fournisseur d'identités : un certificat d'authentification vaut un mot de passe pour le compte qu'il désigne.

En résumé, l'architecture AD CS : CA racine (idéalement hors ligne), CA subordonnée (en ligne, émet les certificats), templates de certificats (définissent ce que le certificat autorise et qui peut le demander), enrollment (demande automatique ou manuelle), et auto-enrollment (les machines reçoivent automatiquement leurs certificats). Usages légitimes : certificats machines pour 802.1X, certificats VPN, certificats SSL internes, authentification par certificat (PKINIT/smart card).

## 8.2 Les mauvaises configurations (ESC)

Les **vulnérabilités ESC** (Escalation via Certificate Services — documentées par SpecterOps) : **ESC1** (le template permet au demandeur de spécifier un SAN arbitraire → demander un certificat au nom d'un Domain Admin ; conditions : Client Authentication + CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT + permissions d'enrollment pour les utilisateurs), **ESC2** (le template permet « Any Purpose » ou « SubCA » → certificat utilisable pour tout), **ESC3** (un agent d'enrollment peut demander des certificats au nom d'autres utilisateurs), **ESC4** (les ACL du template sont trop permissives → un utilisateur peut modifier le template pour le rendre ESC1), **ESC6** (le flag EDITF_ATTRIBUTESUBJECTALTNAME2 est activé sur la CA → tout template devient ESC1), **ESC7** (un utilisateur a le droit ManageCA → peut activer le flag ESC6), **ESC8** (le web enrollment est en HTTP sans EPA → NTLM relay vers le web enrollment → certificat au nom de n'importe qui).

## 8.3 Audit et durcissement

Outils : **Certify** (C# — énumération et exploitation), **Certipy** (Python — énumération, exploitation, et extraction de certificats). Hardening AD CS : auditer les templates (Invoke-PKIAudit, Certipy find), supprimer les SAN libres (CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT), restreindre les permissions d'enrollment, désactiver « Any Purpose », activer HTTPS + EPA sur le web enrollment, et surveiller les enrollments (Event 4887). Détails au Ch.25.

> **🔴 KERBEROS — Épisode 3**
>
> Thomas lance Certipy contre Meridian : `certipy find -u t.granier@meridian.local -p '...' -dc-ip 10.0.1.10`. Résultat : ESC1 sur le template « VPN-User » — Client Authentication activé, CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT activé, et l'enrollment est autorisé pour « Authenticated Users ». Thomas demande un certificat avec le SAN de l'admin DA admin.ssi@meridian.local. Le certificat est émis en 3 secondes. Il utilise PKINIT pour obtenir un TGT de Domain Admin. L'ensemble de l'attaque a pris 90 secondes depuis la découverte du template vulnérable. La Blue Team n'a rien vu — les logs AD CS n'étaient pas centralisés vers le SIEM.

---
