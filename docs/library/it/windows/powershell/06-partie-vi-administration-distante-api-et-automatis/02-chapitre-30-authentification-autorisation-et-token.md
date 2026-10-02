---
title: Chapitre 30 — Authentification, autorisation et tokens
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie VI — Administration distante, API et automatisation
  - index.md
---

## 🟢 Le minimum à savoir

> **Pourquoi ce chapitre avant les API ?** Sans lui, on arrive à `-Headers @{ Authorization = "Bearer $token" }` sans comprendre d'où vient `$token` ni ce qu'il autorise. Ce chapitre donne le **modèle mental** nécessaire — pas un cours complet d'OAuth, juste ce qu'il faut pour utiliser une API et Microsoft Graph en connaissance de cause.

### Authentification vs autorisation : deux choses différentes

C'est la distinction fondamentale, souvent confondue :

- **Authentification** (AuthN) : **qui es-tu ?** Prouver son identité (mot de passe, certificat, token…).
- **Autorisation** (AuthZ) : **qu'as-tu le droit de faire ?** Une fois identifié, quelles actions te sont permises.

On peut être authentifié (identifié) sans être autorisé (avoir le droit) pour une action donnée. Les deux étapes sont séparées.

### Les grandes méthodes d'authentification aux API

| Méthode | Principe | Sécurité |
|---------|----------|----------|
| **API Key** | Une clé secrète envoyée à chaque requête (souvent dans un header) | Simple, mais la clé = accès total si elle fuite |
| **Basic Auth** | Nom + mot de passe encodés en base64 dans le header | Historique, à éviter (le mot de passe circule à chaque appel) |
| **Bearer Token** | Un jeton temporaire obtenu après authentification | Moderne, recommandé (jeton à durée limitée) |

> **⚠️ Base64 n'est PAS du chiffrement.** Le « base64 » de Basic Auth est un simple **encodage**, décodable instantanément. Il ne protège rien par lui-même — c'est **HTTPS** (le transport chiffré) qui protège les identifiants en circulation. Ne confonds jamais encodage (base64) et chiffrement.

### Le Bearer Token : le modèle moderne

Le schéma dominant aujourd'hui :

1. Tu t'authentifies auprès d'un **serveur d'autorisation** (avec des identifiants, un certificat, etc.)
2. Il te délivre un **access token** (un jeton) à durée de vie limitée (souvent ~1h)
3. Tu joins ce token à chaque requête API dans un header : `Authorization: Bearer <token>`
4. L'API vérifie le token et t'autorise (ou non) selon ce qu'il contient

```powershell
# Le token une fois obtenu (on verra comment au Ch.31-32)
$headers = @{ Authorization = "Bearer $token" }
Invoke-RestMethod -Uri "https://api.exemple.com/v1/users" -Headers $headers
```


L'intérêt du token : il **expire** (limite les dégâts en cas de fuite), et il peut porter des **permissions précises** (les scopes).

### OAuth 2.0, à très haut niveau

**OAuth 2.0** est le standard qui orchestre cette délivrance de tokens. Sans entrer dans les détails, retiens les acteurs :

- **Resource Owner** : l'utilisateur (toi) ou l'organisation propriétaire des données
- **Client** : l'application qui veut accéder aux données (ton script)
- **Authorization Server** : celui qui authentifie et délivre les tokens (ex : Entra ID pour Microsoft)
- **Resource Server** : l'API qui héberge les données (ex : Microsoft Graph)

Le flux, très simplifié : *le client demande un token à l'Authorization Server, en prouvant son identité et en précisant les permissions voulues (scopes) ; s'il est autorisé, il reçoit un access token qu'il présente au Resource Server.*

### Les scopes : des permissions précises

Un **scope** est une permission granulaire attachée au token : `User.Read`, `User.ReadWrite.All`, `Group.Read.All`… Le token ne donne accès qu'à ce que ses scopes permettent. C'est le principe de **moindre privilège** appliqué aux API : on ne demande que les scopes strictement nécessaires.

## 🟡 Très utile en pratique

### Permissions déléguées vs permissions d'application

Distinction **cruciale** pour Microsoft Graph (Ch.32), et souvent mal comprise :

| Type | Qui agit ? | Exemple d'usage |
|------|-----------|-----------------|
| **Déléguée** | L'application agit **au nom d'un utilisateur connecté** | Un script interactif : « lis MES emails » — limité aux droits de l'utilisateur |
| **Application** | L'application agit **en son propre nom**, sans utilisateur | Un service automatisé/planifié : « lis les emails de toute l'organisation » — droits larges, sans humain |

> **Conséquence pratique :** un script d'administration **interactif** utilise généralement des permissions **déléguées** (tu te connectes, le script agit avec tes droits). Un script **automatisé** (tâche planifiée, sans humain) utilise des permissions **d'application** (l'app a ses propres droits, via un secret ou un certificat). Les permissions d'application sont plus puissantes et donc plus sensibles — elles doivent être minimales et surveillées.

### Où stocker un token ou un secret ?

> **Jamais en clair dans le script.** Un token, une API key, un secret client ne doivent pas être écrits en dur. On les stocke dans un **SecureString**, un coffre (SecretManagement), une variable d'environnement protégée, ou on utilise un certificat. Le Ch.33 détaille ces mécanismes. Retiens dès maintenant : un secret dans un `.ps1` versionné dans Git est une fuite garantie.

## 🔴 Bonus

### Anatomie d'un token JWT

Les access tokens sont souvent des **JWT** (JSON Web Tokens) : trois parties séparées par des points (`header.payload.signature`), encodées en base64url. Le *payload* contient des *claims* (qui, quels scopes, quelle expiration). On peut le décoder (sans la clé) pour l'inspecter — utile pour déboguer « pourquoi mon appel est refusé ? » (souvent un scope manquant ou un token expiré). Décoder ≠ falsifier : la **signature** garantit l'intégrité.

## ❌ Erreur classique

```powershell
# Confondre authentification et autorisation
# → être connecté ne signifie pas avoir le droit pour CETTE action

# Croire que base64 protège quelque chose
# ❌ base64 = encodage réversible, PAS du chiffrement → HTTPS est ce qui protège

# Demander des scopes trop larges "pour être tranquille"
# ❌ viole le moindre privilège → ne demander que le nécessaire

# Écrire un token/secret en dur dans le script
$token = "eyJ0eXAi..."   # ❌ fuite si versionné → coffre/SecureString (Ch.33)
```


## 💡 Exercices

**Guidé (conceptuel) :** Pour chacun de ces cas, dis s'il faut des permissions **déléguées** ou **d'application** : (a) un script interactif où l'admin lit ses propres groupes ; (b) une tâche planifiée nocturne qui désactive les comptes inactifs de toute l'organisation.

**Autonome (conceptuel) :** Explique en 3-4 phrases, à un collègue débutant, pourquoi `Authorization: Bearer <token>` est plus sûr que d'envoyer un mot de passe à chaque requête. Mentionne l'expiration et les scopes.

## ✅ Tu sais maintenant...

- La différence **authentification** (qui es-tu) / **autorisation** (qu'as-tu le droit de faire)
- Les méthodes : API Key, Basic (à éviter), **Bearer Token** (moderne)
- Que **base64 ≠ chiffrement** (c'est HTTPS qui protège le transport)
- **OAuth 2.0** à haut niveau : client, authorization server, resource server, access token
- Les **scopes** (permissions granulaires, moindre privilège)
- **Déléguées vs application** — distinction clé pour Graph
- Qu'un secret ne s'écrit **jamais** en clair (Ch.33)

## 💬 Questions d'entretien typiques

- **Différence entre authentification et autorisation ?** → AuthN prouve l'identité (qui es-tu) ; AuthZ décide des droits (qu'as-tu le droit de faire).
- **Pourquoi un Bearer token est-il préférable à Basic Auth ?** → Il expire (limite les dégâts d'une fuite), porte des scopes précis, et évite d'envoyer le mot de passe à chaque requête.
- **Permissions déléguées ou d'application pour une tâche planifiée sans utilisateur ?** → D'application (l'app agit en son propre nom) — puissantes, donc à restreindre au minimum.
- **base64 protège-t-il un mot de passe ?** → Non, c'est un encodage réversible ; seule la couche HTTPS protège les identifiants en transit.

---
