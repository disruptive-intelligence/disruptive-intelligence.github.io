---
title: Chapitre 15 — SSH, transferts sécurisés et OpenPGP
source: IT/04 Réseau/Comprendre le réseau/Réseau.md
note: Réseau
up:
- - Réseau
  - ../index.md
- - Partie IV — Sécuriser les échanges
  - index.md
---

## 15.1 SSH

**SSH** (port 22) remplace Telnet et rlogin pour l'administration à distance :

| Apport | Détail |
|---|---|
| **Authentification forte** | Mot de passe, mais surtout **clés publiques** ; MFA possible |
| **Confidentialité** | Tout est chiffré de bout en bout |
| **Intégrité et authenticité du serveur** | Le client mémorise l'empreinte de la clé du serveur (`known_hosts`) et alerte si elle change — signe d'une réinstallation ou d'une interception |
| **Tunnels** | Redirection de ports, proxy SOCKS : un « mini-VPN » applicatif |

```bash
ssh alice@srv-web-01.example.com      # connexion
ssh -i ~/.ssh/id_ed25519 alice@srv     # avec une clé précise
ssh -L 8080:intranet:80 alice@bastion  # redirige localhost:8080 vers intranet:80 via le bastion
```


## 15.2 SFTP et FTPS

Deux façons de sécuriser le transfert de fichiers, à ne pas confondre :

| | **SFTP** | **FTPS** |
|---|---|---|
| Base | Sous-système de **SSH** | **FTP + TLS** (comme HTTPS pour HTTP) |
| Port | 22 | 990 (implicite) ou 21 + STARTTLS |
| Authentification | Comme SSH (clés, mots de passe) | Certificat serveur, identifiants FTP |
| Pare-feu | Un seul port | Canal de données séparé, plus délicat |

## 15.3 Les versions TLS de la messagerie

| Protocole | Version chiffrée | Port |
|---|---|---|
| SMTP (soumission) | STARTTLS / SMTPS | 587 / 465 |
| POP3 | POP3S | 995 |
| IMAP | IMAPS | 993 |

Même principe que HTTPS : TLS enveloppe le protocole d'origine. **STARTTLS** démarre en clair puis bascule en TLS sur le même port ; le **TLS implicite** chiffre dès la connexion.

## 15.4 OpenPGP

**OpenPGP** (implémentation libre : **GnuPG**) est un standard de signature et de chiffrement de fichiers et de courriels, de bout en bout — indépendant du transport. Chacun possède une paire de clés :

| Opération | Clé utilisée |
|---|---|
| **Signer** | Clé **privée** de l'expéditeur |
| **Vérifier la signature** | Clé **publique** de l'expéditeur |
| **Chiffrer** | Clé **publique** du destinataire |
| **Déchiffrer** | Clé **privée** du destinataire |

> **Moyen mnémotechnique.** On signe avec ce qu'on est seul à avoir (sa clé privée) ; on chiffre pour quelqu'un avec ce que tout le monde a (sa clé publique).

---
