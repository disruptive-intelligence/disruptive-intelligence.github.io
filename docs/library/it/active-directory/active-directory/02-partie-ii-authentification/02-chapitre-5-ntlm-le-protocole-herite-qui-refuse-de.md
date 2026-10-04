---
title: 'Chapitre 5 — NTLM : le protocole hérité qui refuse de disparaître'
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - ../index.md
- - Partie II — Authentification
  - index.md
---

## 5.1 Le principe du défi-réponse

NTLM prouve qu'un client connaît le secret d'un compte **sans envoyer le mot de passe**, par un échange de type défi-réponse :

```text
1. NEGOTIATE     Client → Serveur   « je veux m'authentifier »
2. CHALLENGE     Serveur → Client   un nombre aléatoire (le défi)
3. AUTHENTICATE  Client → Serveur   le défi transformé avec le hash NT du mot de passe
4. Vérification  Serveur → DC       le DC, qui connaît le hash, recalcule et compare
5. Résultat      Serveur → Client   accès accordé ou refusé
```


Pour un **compte local**, le serveur vérifie lui-même la réponse avec le hash stocké dans sa SAM, sans DC. Pour un **compte de domaine**, il transmet défi et réponse au DC (événement **4776** sur le DC).

## 5.2 Les versions

| Version | Statut |
|---|---|
| **LM** | Obsolète depuis longtemps, à interdire |
| **NTLMv1** | Cryptographiquement faible, à interdire |
| **NTLMv2** | Version actuelle, plus robuste, mais conserve les faiblesses de conception ci-dessous |

## 5.3 Les faiblesses de conception

| Faiblesse | Conséquence |
|---|---|
| Le **hash NT** suffit à répondre au défi | Le hash est équivalent au mot de passe : il doit être protégé comme lui |
| Pas d'**authentification mutuelle** | Le client ne prouve pas qu'il parle au bon serveur : un intermédiaire peut s'interposer |
| La réponse circule sur le réseau | Elle peut être interceptée et attaquée hors ligne si le mot de passe est faible |
| Pas de notion de service cible (sans protections additionnelles) | Une authentification peut être réutilisée vers un autre service |

Les protections qui compensent ces faiblesses — signature SMB, signature et *channel binding* LDAP, EPA sur les services web — sont détaillées au Ch.24.

## 5.4 Pourquoi NTLM persiste

Kerberos est le protocole par défaut, mais Windows **retombe sur NTLM** dès que Kerberos n'est pas possible :

- accès à une ressource **par adresse IP** plutôt que par nom ;
- **SPN** absent, erroné ou dupliqué ;
- machine **hors domaine** ou DC injoignable ;
- applications anciennes qui ne gèrent que NTLM.

> **Diagnostic classique.** « Un partage SMB utilise NTLM au lieu de Kerberos » : vérifier le nom utilisé (IP ? alias ?), le DNS, le SPN `cifs/` du serveur et ses doublons (`setspn -X`), l'horloge, puis les tickets présents (`klist`) et les événements 4769/4776.

## 5.5 Les protocoles de résolution de secours

Quand un nom ne se résout pas par DNS, Windows interroge le réseau local en diffusion : **LLMNR** (UDP 5355), **NBT-NS** (UDP 137), **mDNS** (UDP 5353). N'importe quelle machine du segment peut répondre, et la victime tente alors de s'authentifier auprès d'elle en NTLM. Ces protocoles sont rarement utiles en entreprise et se **désactivent par GPO** (Ch.23).

> **🔴 KERBEROS — Épisode 2**
>
> En 15 minutes sur le VLAN utilisateurs, Thomas recueille plusieurs réponses NTLM émises vers sa machine grâce aux protocoles de résolution de secours, actifs sur tout le parc. L'une d'elles appartient à m.laurent (responsable qualité), dont le mot de passe saisonnier est retrouvé en quelques secondes. Recommandation immédiate : désactiver LLMNR et NBT-NS, imposer une politique de mots de passe longs.

---
