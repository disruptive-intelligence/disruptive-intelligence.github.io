---
title: 'Avant les protocoles : LSASS et l''ouverture de session'
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - ../index.md
- - Partie II — Authentification
  - index.md
---

Quel que soit le protocole, c'est **LSASS** qui orchestre l'authentification sur la machine et crée le **jeton d'accès** de l'utilisateur (SID, groupes, privilèges). Le chemin dépend du type de compte.

## Compte de domaine

```text
Identifiants
→ Credential Provider / Winlogon
→ LSASS
→ module Kerberos
→ KDC du contrôleur de domaine
→ TGT
→ jeton d'accès
→ session Windows
```


1. L'utilisateur saisit ses identifiants.
2. Le Credential Provider les transmet à Winlogon, puis à LSASS.
3. LSASS reconnaît un compte de domaine et sollicite son module Kerberos.
4. Le poste dérive une clé du mot de passe et envoie une demande `AS-REQ` au KDC.
5. Le KDC vérifie la pré-authentification à partir des données du compte dans AD.
6. S'il accepte, il renvoie un `AS-REP` contenant notamment un **TGT**.
7. LSASS crée le jeton d'accès et ouvre la session.

> Le mot de passe n'est pas envoyé au KDC : il sert à produire une preuve cryptographique que le DC sait vérifier.

## Compte local

```text
Identifiants → LSASS → vérification dans la SAM locale → jeton d'accès → session
```


Aucun KDC n'intervient : LSASS valide le compte avec la base SAM de la machine.

## Compte de domaine hors connexion

Si aucun DC n'est joignable, LSASS vérifie les **identifiants de domaine mis en cache** localement :

```text
Identifiants → LSASS → cache local → session hors ligne
```


Aucun nouveau TGT n'est obtenu : la session locale s'ouvre, mais l'accès aux ressources du domaine reste limité jusqu'au retour de la connectivité.

## LSASS côté poste et côté DC

| Poste membre | Contrôleur de domaine |
|---|---|
| LSASS exécute le **client** Kerberos | Le service **KDC** fonctionne dans le contexte de LSASS |
| Il contacte le KDC distant | Il vérifie les comptes AD et délivre les tickets |

## Après l'ouverture de session

Le TGT permet ensuite de demander un ticket par service, sans ressaisir le mot de passe : c'est le **SSO**.

```text
TGT → ticket CIFS      → partage SMB
    → ticket HTTP      → application web
    → ticket MSSQLSvc  → SQL Server
```


LSASS garde ces tickets dans le cache de la session (`klist` pour les afficher). C'est ce cache, nécessaire au SSO, qui fait de LSASS une cible : il contient de quoi agir au nom des utilisateurs connectés (Ch.7).

> **À retenir.** LSASS orchestre l'authentification et crée la session. Pour un compte de domaine, le KDC vérifie l'identité et délivre les tickets ; pour un compte local, LSASS vérifie directement la SAM.

---
