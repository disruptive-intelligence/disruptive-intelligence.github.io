---
title: Chapitre 32 — Microsoft Graph et Entra ID
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie VI — Administration distante, API et automatisation
  - index.md
---

## 🟢 Le minimum à savoir

### Ce qu'est Microsoft Graph

**Microsoft Graph** est l'API REST unifiée de Microsoft 365 et **Entra ID** (l'ancien Azure Active Directory — l'annuaire *cloud*, à distinguer de l'AD *on-premise* des Parties IV-V). Via Graph, on administre les utilisateurs, groupes, licences, appareils, e-mails, équipes Teams… du cloud Microsoft. C'est l'équivalent moderne, côté cloud, de ce qu'on faisait avec le module `ActiveDirectory` en local.

> **AD on-premise vs Entra ID :** l'Active Directory des Parties IV-V vit sur **tes serveurs** (contrôleurs de domaine). **Entra ID** est l'annuaire **dans le cloud** Microsoft. Beaucoup d'organisations utilisent les deux, synchronisés. Les cmdlets diffèrent : `Get-ADUser` (on-premise) vs `Get-MgUser` (cloud). Ne les confonds pas.

### Deux façons d'appeler Graph

1. **Le module Microsoft Graph PowerShell** (`Microsoft.Graph`) : des cmdlets prêtes à l'emploi (`Get-MgUser`…) qui gèrent l'authentification et la pagination pour toi. **Recommandé pour débuter.**
2. **Les appels REST directs** (`Invoke-RestMethod` vers `https://graph.microsoft.com`) : plus de contrôle, mais tu gères toi-même le token et la pagination (Ch.31). Utile quand une fonctionnalité n'est pas couverte par le module.

### Installer et se connecter (module)

```powershell
# Installer le module (une fois) — en CurrentUser, PAS besoin de console admin
Install-Module Microsoft.Graph -Scope CurrentUser

# Se connecter en demandant les SCOPES nécessaires (rappel Ch.30 : moindre privilège)
Connect-MgGraph -Scopes "User.Read.All", "Group.Read.All"
```


> **Note :** l'installation en `-Scope CurrentUser` ne nécessite **pas** de console administrateur (elle s'installe dans ton profil). Microsoft **recommande PowerShell 7** pour le SDK Graph ; il peut fonctionner sur d'autres versions selon les prérequis, mais 7 est la cible conseillée.

> **Le lien direct avec le Ch.30 :** `Connect-MgGraph -Scopes ...` matérialise tout ce qu'on a vu sur l'autorisation. Tu demandes des **scopes** précis ; une fenêtre de connexion t'authentifie (permissions **déléguées** : le script agira avec **tes** droits) ; un **token** est obtenu et géré par le module. Tu ne vois pas le token, mais c'est bien le mécanisme du Ch.30 qui opère.

### Interroger Graph (module)

```powershell
# L'utilisateur actuellement connecté
Get-MgContext                                   # contexte : compte, scopes accordés

# Rechercher un utilisateur
Get-MgUser -Filter "startsWith(displayName,'Jean')" |
    Select-Object DisplayName, UserPrincipalName, Id

# Lister des groupes
Get-MgGroup -Top 10 | Select-Object DisplayName, Id

# Les membres d'un groupe
Get-MgGroupMember -GroupId "<id-du-groupe>"
```


> **📌 Réflexe `Get-Member` :** `Get-MgUser -Top 1 | Get-Member` révèle les propriétés d'un utilisateur Entra ID (`DisplayName`, `UserPrincipalName`, `Mail`, `AccountEnabled`, `Id`…). Comme pour l'AD on-premise, certains attributs nécessitent d'être demandés explicitement (`-Property`).

### Se déconnecter

```powershell
Disconnect-MgGraph
```


## 🟡 Très utile en pratique

### Les scopes et le consentement

La première connexion avec de nouveaux scopes déclenche un **consentement** : Microsoft demande d'approuver les permissions. C'est le principe d'autorisation du Ch.30 rendu visible.

- Un scope en **lecture** (`User.Read.All`) suffit pour un rapport — ne demande pas d'écriture « au cas où ».
- Un scope en **écriture** (`User.ReadWrite.All`) est nécessaire pour modifier — et bien plus sensible.

```powershell
# Pour un rapport : lecture seule (moindre privilège)
Connect-MgGraph -Scopes "User.Read.All"

# Pour modifier des comptes : écriture (plus sensible, à justifier)
Connect-MgGraph -Scopes "User.ReadWrite.All"
```


### Un rapport d'utilisateurs Entra ID

```powershell
Connect-MgGraph -Scopes "User.Read.All"

Get-MgUser -All -Property DisplayName, UserPrincipalName, AccountEnabled, Department |
    Select-Object DisplayName, UserPrincipalName, AccountEnabled, Department |
    Export-Csv "C:\rapports\entra_users.csv" -NoTypeInformation -Encoding UTF8

Disconnect-MgGraph
```


On retrouve exactement le schéma des rapports AD (Ch.23), transposé au cloud : requête filtrée → projection → export.

### Appel REST direct (quand le module ne couvre pas un endpoint)

Le SDK fournit `Invoke-MgGraphRequest`, qui appelle **n'importe quel endpoint Graph en réutilisant le contexte d'authentification** de `Connect-MgGraph` — sans que tu aies à manipuler le token toi-même :

```powershell
# Après Connect-MgGraph : appeler un endpoint brut avec le contexte déjà authentifié
Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/me"

# Un endpoint moins courant, non couvert par une cmdlet dédiée
Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/users?`$top=5"
```


> **Attention à une confusion courante :** `Get-MgContext` renvoie le **contexte** (compte, scopes accordés, tenant) — **pas** un access token prêt à coller dans un header `Authorization`. Pour un appel REST authentifié, utilise `Invoke-MgGraphRequest` (qui gère le token pour toi), plutôt que d'essayer d'extraire un bearer token du contexte.

> **Renvoi Ch.31 — attention à la pagination.** `Invoke-MgGraphRequest` gère l'**authentification** (il réutilise la session `Connect-MgGraph`, tu n'as pas à manipuler le token). Mais il **ne suit pas automatiquement la pagination** : si la réponse contient un `@odata.nextLink`, c'est à **toi** de rappeler cette URL pour récupérer les pages suivantes (comme au Ch.31). En résumé : les **cmdlets** Graph avec `-All` (ex. `Get-MgUser -All`) parcourent les pages pour toi ; `Invoke-MgGraphRequest` gère l'auth mais te laisse suivre `@odata.nextLink` toi-même. L'appel `Invoke-RestMethod` totalement manuel (avec ton propre token) reste possible quand tu gères l'authentification hors du SDK.

## 🔴 Bonus

### Permissions d'application pour l'automatisation

Les exemples ci-dessus utilisent des permissions **déléguées** (tu te connectes interactivement). Pour une **tâche planifiée sans humain** (rappel Ch.30), on utilise des permissions **d'application** : on enregistre une *app* dans Entra ID, on lui attribue des permissions d'application, et on s'authentifie avec un **certificat** (préférable) ou un **secret client**. C'est plus puissant (agit sur toute l'organisation, sans utilisateur) donc plus sensible — à réserver aux automatisations, avec des permissions minimales.

```powershell
# Authentification applicative (schéma), pour un script non interactif
Connect-MgGraph -ClientId "<app-id>" -TenantId "<tenant-id>" -CertificateThumbprint "<empreinte>"
```


## ❌ Erreur classique

```powershell
# Confondre AD on-premise et Entra ID
Get-ADUser alice        # ❌ AD local — ne marche pas pour le cloud
Get-MgUser -Filter "..."   # ✅ pour Entra ID (cloud)

# Demander des scopes en écriture pour un simple rapport
Connect-MgGraph -Scopes "User.ReadWrite.All"   # ❌ trop pour lire
Connect-MgGraph -Scopes "User.Read.All"         # ✅ moindre privilège

# Oublier de se déconnecter / laisser des scopes larges accordés
Disconnect-MgGraph   # ✅ bonne hygiène

# Croire que Get-MgUser renvoie tous les attributs
Get-MgUser -Top 1                              # ⚠️ jeu réduit
Get-MgUser -Top 1 -Property Department, Mail   # ✅ demander explicitement
```


## 💡 Exercices

**Guidé (nécessite un tenant de test/dev) :** Connecte-toi à Graph en lecture (`User.Read.All`), affiche ton propre compte avec `Get-MgContext`, puis liste 5 utilisateurs avec leur UPN.

**Autonome :** Écris un script qui produit un rapport CSV des utilisateurs Entra ID désactivés (`AccountEnabled -eq $false`), avec leur nom, UPN et service. Utilise le bon scope minimal et déconnecte-toi à la fin.

## ✅ Tu sais maintenant...

- Ce qu'est Microsoft Graph (API unifiée M365/Entra ID) et la différence **AD on-premise / Entra ID cloud**
- Les deux approches : **module `Microsoft.Graph`** (recommandé) vs **REST direct** (Ch.31)
- `Connect-MgGraph -Scopes` comme application concrète de l'autorisation (Ch.30)
- Interroger utilisateurs/groupes (`Get-MgUser`, `Get-MgGroup`) et produire des rapports
- Déléguées (interactif) vs application (automatisation) pour Graph

## 💬 Questions d'entretien typiques

- **Différence entre AD on-premise et Entra ID ?** → L'AD on-premise vit sur tes contrôleurs de domaine ; Entra ID est l'annuaire cloud de Microsoft. Cmdlets différentes (`Get-ADUser` vs `Get-MgUser`).
- **Module Graph ou REST direct ?** → Le module pour la simplicité (auth et pagination gérées) ; le REST direct pour le contrôle fin ou ce que le module ne couvre pas.
- **Que fait `Connect-MgGraph -Scopes` ?** → Il demande des permissions précises, authentifie l'utilisateur et obtient un token — l'autorisation OAuth du Ch.30 en pratique.
- **Déléguées ou application pour un script planifié Graph ?** → Application (pas d'utilisateur interactif), avec certificat de préférence, permissions minimales.

---
