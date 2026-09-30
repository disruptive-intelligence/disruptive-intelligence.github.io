---
title: PARTIE VI — ADMINISTRATION DISTANTE, API ET AUTOMATISATION
source: IT/02_Windows/Powershell.md
note: PowerShell
chapter: 6
chapters: 8
---

Jusqu'ici, on administrait des machines une par une, souvent en local. Cette partie change d'échelle : exécuter des commandes sur **des dizaines de machines à distance** (Remoting), puis dialoguer avec des services web via des **API REST** — en comprenant d'abord comment fonctionne l'**authentification** moderne, avant d'aborder **Microsoft Graph**.

---


## Chapitre 29 — PowerShell Remoting

### 🟢 Le minimum à savoir

#### Le principe

**PowerShell Remoting** exécute des commandes sur des machines distantes — c'est l'équivalent Windows de SSH. Il repose sur **WinRM** (Windows Remote Management), le service qui écoute les connexions distantes.

Deux usages :
- **Session interactive** (`Enter-PSSession`) : tu « entres » sur la machine distante, comme SSH
- **Commande distante** (`Invoke-Command`) : tu envoies un bloc de code à exécuter, éventuellement sur plusieurs machines à la fois

#### Activer le remoting `[🔑 Admin]`

```powershell
# Sur la machine CIBLE (celle qu'on veut administrer), une seule fois
Enable-PSRemoting -Force
```

En environnement AD, le remoting est souvent déjà activé (par GPO) sur les serveurs.

#### Session interactive

```powershell
Enter-PSSession -ComputerName SRV01
# [SRV01]: PS C:\>   ← tu es maintenant SUR SRV01
Get-Service           # s'exécute sur SRV01
Exit-PSSession        # revenir sur ta machine
```

#### Commande distante (le cas le plus puissant)

```powershell
# Sur une machine
Invoke-Command -ComputerName SRV01 -ScriptBlock { Get-Service -Name wuauserv }

# Sur PLUSIEURS machines à la fois
Invoke-Command -ComputerName SRV01, SRV02, DC01 -ScriptBlock {
    Get-CimInstance Win32_OperatingSystem | Select-Object LastBootUpTime
}
```

> **La propriété `PSComputerName` :** quand `Invoke-Command` cible plusieurs machines, chaque objet renvoyé porte automatiquement une propriété `PSComputerName` indiquant sa provenance. Indispensable pour savoir quel résultat vient de quelle machine :
> ```powershell
> Invoke-Command -ComputerName SRV01,SRV02 -ScriptBlock { Get-Service Spooler } |
>     Select-Object PSComputerName, Name, Status
> ```

#### Le modèle d'exécution : local vs distant

> **Point important :** le `-ScriptBlock` s'exécute **sur la machine distante**, avec ses variables et son contexte. Tes variables locales n'y sont **pas** disponibles automatiquement — il faut les passer explicitement :
> ```powershell
> $nomService = "wuauserv"
> Invoke-Command -ComputerName SRV01 -ScriptBlock {
>     Get-Service -Name $using:nomService     # $using: injecte la variable locale
> }
> ```
> Le préfixe `$using:` transporte une variable locale dans le bloc distant. Sans lui, `$nomService` serait vide côté serveur.

### 🟡 WinRM, authentification et sécurité : les vraies nuances

> **⚠️ Correction d'une simplification répandue.** On lit souvent « WinRM est chiffré » ou « le remoting utilise HTTPS ». La réalité est plus nuancée, et un administrateur doit la connaître.

#### Le transport : HTTP (5985) vs HTTPS (5986)

Par défaut, WinRM écoute sur le port **5985 (HTTP)**. Cela ne veut **pas** dire que tout circule en clair : dans un domaine, l'**authentification et le chiffrement** du contenu sont assurés au niveau du protocole d'authentification (voir ci-dessous), même sur le port HTTP. Le port **5986 (HTTPS)** ajoute une couche TLS au niveau **transport** (avec un certificat), utile hors domaine ou pour une exigence de conformité.

#### Les mécanismes d'authentification

| Contexte | Mécanisme | Chiffrement du contenu |
|----------|-----------|----------------------|
| **Dans un domaine AD** | **Kerberos** (automatique) | Oui, assuré par Kerberos même sur HTTP/5985 |
| **Hors domaine** (workgroup) | **NTLM** ou HTTPS | NTLM chiffre le contenu ; sinon HTTPS requis |
| **Hors domaine, par IP** | Nécessite **TrustedHosts** ou HTTPS | Selon configuration |

**En résumé nuancé :**
- **En domaine :** Kerberos gère l'authentification **et** chiffre le contenu, de façon transparente, même sur le port HTTP 5985. C'est le cas le plus courant et il est sûr.
- **Hors domaine :** l'authentification par nom/IP hors domaine oblige à configurer **TrustedHosts** (liste des machines de confiance) côté client, ce qui **contourne certaines protections** — ou, mieux, à utiliser **HTTPS** avec un certificat.

```powershell
# Hors domaine : déclarer une machine de confiance (à manier avec prudence)  [🔑 Admin]
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "192.168.1.60" -Force

# Se connecter avec des identifiants explicites (hors domaine)
$cred = Get-Credential
Invoke-Command -ComputerName 192.168.1.60 -Credential $cred -ScriptBlock { hostname }
```

> **À retenir, sans simplifier abusivement :** ne dis pas « WinRM est toujours chiffré ». Dis plutôt : « en domaine, Kerberos authentifie et chiffre le contenu, même sur HTTP ; hors domaine, il faut NTLM correctement configuré, ou TrustedHosts (moins sûr), ou HTTPS (recommandé) ». Cette précision est ce qui distingue un administrateur qui comprend de celui qui récite.

#### Les sessions persistantes

Ouvrir une connexion à chaque `Invoke-Command` est coûteux. Une **session persistante** (`PSSession`) maintient la connexion pour plusieurs commandes :

```powershell
$session = New-PSSession -ComputerName SRV01
Invoke-Command -Session $session -ScriptBlock { $svc = Get-Service }   # la variable persiste
Invoke-Command -Session $session -ScriptBlock { $svc.Count }           # réutilisable
Remove-PSSession $session                                              # fermer proprement
```

### 🔴 Bonus

#### Exécution en parallèle sur un grand parc

Pour interroger beaucoup de machines, `Invoke-Command` parallélise déjà nativement (jusqu'à 32 par défaut, réglable via `-ThrottleLimit`) :

```powershell
$serveurs = Get-ADComputer -Filter "OperatingSystem -like '*Server*'" |
    Select-Object -ExpandProperty Name

Invoke-Command -ComputerName $serveurs -ThrottleLimit 20 -ScriptBlock {
    [PSCustomObject]@{
        Uptime = (Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
    }
} | Select-Object PSComputerName, Uptime
```

Voilà comment on obtient l'uptime de tout un parc en une commande. On croise ici le remoting (Ch.29) et l'inventaire AD (Ch.22).

### ❌ Erreur classique

```powershell
# Croire que ses variables locales sont dispo dans le ScriptBlock distant
$nom = "wuauserv"
Invoke-Command -ComputerName SRV01 -ScriptBlock { Get-Service $nom }   # ❌ $nom vide
Invoke-Command -ComputerName SRV01 -ScriptBlock { Get-Service $using:nom }  # ✅

# Affirmer "WinRM est toujours chiffré" sans nuance
# → vrai en domaine (Kerberos), à qualifier hors domaine (NTLM/TrustedHosts/HTTPS)

# Ajouter tout le monde dans TrustedHosts
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "*"   # ❌ dangereux
# → lister seulement les machines nécessaires, ou utiliser HTTPS

# Oublier de fermer les sessions persistantes
New-PSSession ...    # ⚠️ sessions qui s'accumulent
Remove-PSSession ...  # ✅
```

### 💡 Exercices

**Guidé :** Avec `Invoke-Command`, récupère l'heure de dernier démarrage de deux machines de ton lab et affiche le résultat avec `PSComputerName`.

**Autonome :** Écris un script qui prend une liste de `-ComputerName`, exécute à distance une collecte (OS, uptime, espace disque C:), et renvoie un PSCustomObject par machine (avec `PSComputerName`). Gère les machines injoignables avec `try/catch`.

### ✅ Tu sais maintenant...

- Le remoting via WinRM : session interactive (`Enter-PSSession`) et commande distante (`Invoke-Command`)
- Cibler plusieurs machines et exploiter `PSComputerName`
- Passer des variables locales avec `$using:`
- **Les vraies nuances WinRM** : HTTP/5985 vs HTTPS/5986, Kerberos (domaine) vs NTLM/TrustedHosts/HTTPS (hors domaine)
- Les sessions persistantes (`New`/`Remove-PSSession`)

### 💬 Questions d'entretien typiques

- **Le remoting WinRM est-il chiffré ?** → En domaine, oui : Kerberos authentifie et chiffre le contenu même sur le port HTTP 5985. Hors domaine, il faut NTLM correctement configuré, TrustedHosts (moins sûr) ou HTTPS.
- **Comment utiliser une variable locale dans un `Invoke-Command` distant ?** → Avec le préfixe `$using:`.
- **Comment savoir de quelle machine vient un résultat ?** → La propriété `PSComputerName`, ajoutée automatiquement par `Invoke-Command`.
- **Pourquoi `TrustedHosts = *` est-il déconseillé ?** → Il fait confiance à toutes les machines, contournant des protections ; on limite à la liste nécessaire ou on utilise HTTPS.

---


## Chapitre 30 — Authentification, autorisation et tokens

### 🟢 Le minimum à savoir

> **Pourquoi ce chapitre avant les API ?** Sans lui, on arrive à `-Headers @{ Authorization = "Bearer $token" }` sans comprendre d'où vient `$token` ni ce qu'il autorise. Ce chapitre donne le **modèle mental** nécessaire — pas un cours complet d'OAuth, juste ce qu'il faut pour utiliser une API et Microsoft Graph en connaissance de cause.

#### Authentification vs autorisation : deux choses différentes

C'est la distinction fondamentale, souvent confondue :

- **Authentification** (AuthN) : **qui es-tu ?** Prouver son identité (mot de passe, certificat, token…).
- **Autorisation** (AuthZ) : **qu'as-tu le droit de faire ?** Une fois identifié, quelles actions te sont permises.

On peut être authentifié (identifié) sans être autorisé (avoir le droit) pour une action donnée. Les deux étapes sont séparées.

#### Les grandes méthodes d'authentification aux API

| Méthode | Principe | Sécurité |
|---------|----------|----------|
| **API Key** | Une clé secrète envoyée à chaque requête (souvent dans un header) | Simple, mais la clé = accès total si elle fuite |
| **Basic Auth** | Nom + mot de passe encodés en base64 dans le header | Historique, à éviter (le mot de passe circule à chaque appel) |
| **Bearer Token** | Un jeton temporaire obtenu après authentification | Moderne, recommandé (jeton à durée limitée) |

> **⚠️ Base64 n'est PAS du chiffrement.** Le « base64 » de Basic Auth est un simple **encodage**, décodable instantanément. Il ne protège rien par lui-même — c'est **HTTPS** (le transport chiffré) qui protège les identifiants en circulation. Ne confonds jamais encodage (base64) et chiffrement.

#### Le Bearer Token : le modèle moderne

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

#### OAuth 2.0, à très haut niveau

**OAuth 2.0** est le standard qui orchestre cette délivrance de tokens. Sans entrer dans les détails, retiens les acteurs :

- **Resource Owner** : l'utilisateur (toi) ou l'organisation propriétaire des données
- **Client** : l'application qui veut accéder aux données (ton script)
- **Authorization Server** : celui qui authentifie et délivre les tokens (ex : Entra ID pour Microsoft)
- **Resource Server** : l'API qui héberge les données (ex : Microsoft Graph)

Le flux, très simplifié : *le client demande un token à l'Authorization Server, en prouvant son identité et en précisant les permissions voulues (scopes) ; s'il est autorisé, il reçoit un access token qu'il présente au Resource Server.*

#### Les scopes : des permissions précises

Un **scope** est une permission granulaire attachée au token : `User.Read`, `User.ReadWrite.All`, `Group.Read.All`… Le token ne donne accès qu'à ce que ses scopes permettent. C'est le principe de **moindre privilège** appliqué aux API : on ne demande que les scopes strictement nécessaires.

### 🟡 Très utile en pratique

#### Permissions déléguées vs permissions d'application

Distinction **cruciale** pour Microsoft Graph (Ch.32), et souvent mal comprise :

| Type | Qui agit ? | Exemple d'usage |
|------|-----------|-----------------|
| **Déléguée** | L'application agit **au nom d'un utilisateur connecté** | Un script interactif : « lis MES emails » — limité aux droits de l'utilisateur |
| **Application** | L'application agit **en son propre nom**, sans utilisateur | Un service automatisé/planifié : « lis les emails de toute l'organisation » — droits larges, sans humain |

> **Conséquence pratique :** un script d'administration **interactif** utilise généralement des permissions **déléguées** (tu te connectes, le script agit avec tes droits). Un script **automatisé** (tâche planifiée, sans humain) utilise des permissions **d'application** (l'app a ses propres droits, via un secret ou un certificat). Les permissions d'application sont plus puissantes et donc plus sensibles — elles doivent être minimales et surveillées.

#### Où stocker un token ou un secret ?

> **Jamais en clair dans le script.** Un token, une API key, un secret client ne doivent pas être écrits en dur. On les stocke dans un **SecureString**, un coffre (SecretManagement), une variable d'environnement protégée, ou on utilise un certificat. Le Ch.33 détaille ces mécanismes. Retiens dès maintenant : un secret dans un `.ps1` versionné dans Git est une fuite garantie.

### 🔴 Bonus

#### Anatomie d'un token JWT

Les access tokens sont souvent des **JWT** (JSON Web Tokens) : trois parties séparées par des points (`header.payload.signature`), encodées en base64url. Le *payload* contient des *claims* (qui, quels scopes, quelle expiration). On peut le décoder (sans la clé) pour l'inspecter — utile pour déboguer « pourquoi mon appel est refusé ? » (souvent un scope manquant ou un token expiré). Décoder ≠ falsifier : la **signature** garantit l'intégrité.

### ❌ Erreur classique

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

### 💡 Exercices

**Guidé (conceptuel) :** Pour chacun de ces cas, dis s'il faut des permissions **déléguées** ou **d'application** : (a) un script interactif où l'admin lit ses propres groupes ; (b) une tâche planifiée nocturne qui désactive les comptes inactifs de toute l'organisation.

**Autonome (conceptuel) :** Explique en 3-4 phrases, à un collègue débutant, pourquoi `Authorization: Bearer <token>` est plus sûr que d'envoyer un mot de passe à chaque requête. Mentionne l'expiration et les scopes.

### ✅ Tu sais maintenant...

- La différence **authentification** (qui es-tu) / **autorisation** (qu'as-tu le droit de faire)
- Les méthodes : API Key, Basic (à éviter), **Bearer Token** (moderne)
- Que **base64 ≠ chiffrement** (c'est HTTPS qui protège le transport)
- **OAuth 2.0** à haut niveau : client, authorization server, resource server, access token
- Les **scopes** (permissions granulaires, moindre privilège)
- **Déléguées vs application** — distinction clé pour Graph
- Qu'un secret ne s'écrit **jamais** en clair (Ch.33)

### 💬 Questions d'entretien typiques

- **Différence entre authentification et autorisation ?** → AuthN prouve l'identité (qui es-tu) ; AuthZ décide des droits (qu'as-tu le droit de faire).
- **Pourquoi un Bearer token est-il préférable à Basic Auth ?** → Il expire (limite les dégâts d'une fuite), porte des scopes précis, et évite d'envoyer le mot de passe à chaque requête.
- **Permissions déléguées ou d'application pour une tâche planifiée sans utilisateur ?** → D'application (l'app agit en son propre nom) — puissantes, donc à restreindre au minimum.
- **base64 protège-t-il un mot de passe ?** → Non, c'est un encodage réversible ; seule la couche HTTPS protège les identifiants en transit.

---


## Chapitre 31 — API REST avec PowerShell

### 🟢 Le minimum à savoir

#### Ce qu'est une API REST, en clair

Une **API REST** est une interface qui permet à des programmes de dialoguer via le web. Concrètement : tu envoies une requête HTTP à une **URL** (endpoint), et tu reçois une réponse, presque toujours en **JSON**. C'est ainsi qu'un script PowerShell peut interroger un service en ligne, un outil de ticketing, un système de supervision, ou Microsoft Graph (Ch.32).

#### Le vocabulaire HTTP minimal

| Terme | Ce que c'est |
|-------|-------------|
| **URI / endpoint** | L'adresse de la ressource (`https://api.exemple.com/v1/users`) |
| **Méthode** | L'action : `GET` (lire), `POST` (créer), `PUT`/`PATCH` (modifier), `DELETE` (supprimer) |
| **Headers** | Métadonnées de la requête (authentification, type de contenu…) |
| **Body** | Les données envoyées (pour POST/PUT/PATCH), en général du JSON |
| **Status code** | Le résultat : `200` OK, `201` créé, `401` non authentifié, `403` interdit, `404` introuvable, `429` trop de requêtes, `500` erreur serveur |

#### `Invoke-RestMethod` : la cmdlet clé

`Invoke-RestMethod` envoie une requête HTTP **et convertit automatiquement le JSON de réponse en objets PowerShell**. C'est ce qui rend PowerShell si agréable pour les API :

```powershell
# GET simple — la réponse JSON devient un objet directement exploitable
$reponse = Invoke-RestMethod -Uri "https://api.github.com/users/powershell"
$reponse.name           # "PowerShell"
$reponse.public_repos   # un nombre
```

> **📌 Réflexe `Get-Member` :** `Invoke-RestMethod -Uri "..." | Get-Member` te montre la structure de la réponse — les propriétés que l'API renvoie. C'est ainsi qu'on découvre ce qu'une API expose, sans deviner.

#### `Invoke-RestMethod` vs `Invoke-WebRequest`

- **`Invoke-RestMethod`** : parse automatiquement le JSON en objets. **À privilégier pour les API REST.**
- **`Invoke-WebRequest`** : renvoie la réponse HTTP brute (status, headers, contenu texte). Utile quand on a besoin des détails HTTP (code de statut exact, headers de réponse) ou pour du web non-API.

#### Envoyer des headers (dont l'authentification)

Rappel du Ch.30 : l'authentification passe souvent par un header `Authorization` :

```powershell
$headers = @{
    Authorization = "Bearer $token"
    Accept        = "application/json"
}
Invoke-RestMethod -Uri "https://api.exemple.com/v1/me" -Headers $headers
```

#### Envoyer des données : POST avec un body JSON

```powershell
# Construire le corps comme une hashtable, puis le convertir en JSON
$corps = @{
    name  = "Nouveau projet"
    owner = "equipe-infra"
} | ConvertTo-Json

Invoke-RestMethod -Uri "https://api.exemple.com/v1/projects" `
    -Method Post `
    -Headers $headers `
    -Body $corps `
    -ContentType "application/json"
```

> **Le duo `ConvertTo-Json` / `ConvertFrom-Json` :** on construit le body avec une hashtable qu'on convertit en JSON (`ConvertTo-Json`) ; et si on reçoit du JSON brut (via `Invoke-WebRequest`), on le reconvertit en objets avec `ConvertFrom-Json`. Avec `Invoke-RestMethod`, la conversion de la réponse est automatique.

### 🟡 Très utile en pratique

#### Gérer les erreurs HTTP

Une requête peut échouer (401, 404, 500…). On l'encadre d'un `try/catch` (rappel Ch.8) :

```powershell
try {
    $r = Invoke-RestMethod -Uri "https://api.exemple.com/v1/users/999" `
        -Headers $headers -ErrorAction Stop
}
catch {
    $code = $_.Exception.Response.StatusCode.value__
    switch ($code) {
        401 { Write-Warning "Non authentifié — token invalide ou expiré (Ch.30)" }
        403 { Write-Warning "Interdit — scope insuffisant (Ch.30)" }
        404 { Write-Warning "Ressource introuvable" }
        429 { Write-Warning "Trop de requêtes — ralentir (throttling)" }
        default { Write-Warning "Erreur HTTP $code : $($_.Exception.Message)" }
    }
}
```

> **Diagnostic croisé Ch.30 :** un `401` renvoie souvent à un token expiré, un `403` à un **scope manquant**. Comprendre l'auth (Ch.30) rend le débogage des API bien plus rapide.

#### La pagination

Les API limitent le nombre de résultats par réponse et fournissent un lien vers la « page suivante ». Il faut boucler tant qu'il y en a une :

```powershell
$url = "https://api.exemple.com/v1/users?limit=100"
$tous = [System.Collections.Generic.List[object]]::new()

while ($url) {
    $page = Invoke-RestMethod -Uri $url -Headers $headers
    $page.data | ForEach-Object { $tous.Add($_) }
    $url = $page.next_page_url    # null quand il n'y a plus de page → sort de la boucle
}

"Total récupéré : $($tous.Count)"
```

Le nom du champ de pagination varie selon l'API (`next`, `next_page_url`, `@odata.nextLink` pour Graph…) — c'est là que lire la doc de l'API est indispensable.

#### Query parameters

Les paramètres de requête affinent une requête GET (`?cle=valeur&autre=valeur`) :

```powershell
$params = @{ q = "powershell"; sort = "stars"; per_page = 5 }
Invoke-RestMethod -Uri "https://api.github.com/search/repositories" -Body $params
# En GET, -Body est encodé comme query string : ?q=powershell&sort=stars&per_page=5
```

### 🔴 Bonus

#### Un mini-connecteur réutilisable

En pratique, on encapsule les appels dans une fonction, avec l'auth et la gestion d'erreurs centralisées :

```powershell
function Invoke-MonApi {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)][string]$Endpoint,
        [string]$Method = "Get",
        [object]$Body
    )
    $headers = @{ Authorization = "Bearer $script:Token"; Accept = "application/json" }
    $params = @{
        Uri = "https://api.exemple.com/v1/$Endpoint"
        Method = $Method; Headers = $headers; ErrorAction = "Stop"
    }
    if ($Body) { $params.Body = ($Body | ConvertTo-Json); $params.ContentType = "application/json" }
    Invoke-RestMethod @params    # splatting (Ch.3)
}

Invoke-MonApi -Endpoint "users" | Select-Object id, name
```

Ce pattern (splatting + fonction + gestion d'erreurs) est directement réutilisable pour n'importe quelle API. Le `$script:Token` est ici une variable de portée script : en pratique, on la remplit depuis un coffre (`Get-Secret`, Ch.33), jamais avec un token écrit en dur.

### ❌ Erreur classique

```powershell
# Utiliser Invoke-WebRequest et parser le JSON à la main
$r = Invoke-WebRequest -Uri "..."; $data = $r.Content | ConvertFrom-Json   # ⚠️ verbeux
$data = Invoke-RestMethod -Uri "..."   # ✅ conversion automatique

# Oublier -ContentType sur un POST JSON
Invoke-RestMethod -Uri "..." -Method Post -Body $json   # ⚠️ l'API peut mal interpréter
Invoke-RestMethod -Uri "..." -Method Post -Body $json -ContentType "application/json"  # ✅

# Ne pas gérer la pagination → ne récupérer que la 1re page
# ✅ boucler tant qu'il y a une "page suivante"

# Ignorer le status code en cas d'échec
# ✅ try/catch + lire $_.Exception.Response.StatusCode
```

### 💡 Exercices

**Guidé :** Avec `Invoke-RestMethod`, interroge `https://api.github.com/users/microsoft` et affiche le nom, le nombre de dépôts publics et la date de création. Explore la réponse avec `Get-Member`.

**Autonome :** Écris une fonction `Get-GitHubRepos -User <nom>` qui récupère les dépôts publics d'un utilisateur GitHub (gère la pagination via le header `Link` ou le paramètre `page`), et exporte nom + langage + nombre d'étoiles en CSV.

### ✅ Tu sais maintenant...

- Ce qu'est une API REST (endpoint, méthode, headers, body, status code)
- `Invoke-RestMethod` (JSON → objets automatiquement) vs `Invoke-WebRequest`
- Envoyer des headers d'authentification (Bearer, rappel Ch.30) et un body JSON (`ConvertTo-Json`)
- Gérer les erreurs HTTP (401/403/404/429) et la **pagination**
- Encapsuler les appels dans une fonction réutilisable

### 💬 Questions d'entretien typiques

- **`Invoke-RestMethod` ou `Invoke-WebRequest` ?** → `Invoke-RestMethod` pour les API REST (conversion JSON→objets automatique) ; `Invoke-WebRequest` quand on a besoin des détails HTTP bruts.
- **Que signifie un 401 vs un 403 ?** → 401 = non authentifié (token absent/expiré) ; 403 = authentifié mais non autorisé (scope insuffisant).
- **Comment récupérer tous les résultats d'une API paginée ?** → Boucler en suivant le lien de page suivante jusqu'à ce qu'il soit nul.

---


## Chapitre 32 — Microsoft Graph et Entra ID

### 🟢 Le minimum à savoir

#### Ce qu'est Microsoft Graph

**Microsoft Graph** est l'API REST unifiée de Microsoft 365 et **Entra ID** (l'ancien Azure Active Directory — l'annuaire *cloud*, à distinguer de l'AD *on-premise* des Parties IV-V). Via Graph, on administre les utilisateurs, groupes, licences, appareils, e-mails, équipes Teams… du cloud Microsoft. C'est l'équivalent moderne, côté cloud, de ce qu'on faisait avec le module `ActiveDirectory` en local.

> **AD on-premise vs Entra ID :** l'Active Directory des Parties IV-V vit sur **tes serveurs** (contrôleurs de domaine). **Entra ID** est l'annuaire **dans le cloud** Microsoft. Beaucoup d'organisations utilisent les deux, synchronisés. Les cmdlets diffèrent : `Get-ADUser` (on-premise) vs `Get-MgUser` (cloud). Ne les confonds pas.

#### Deux façons d'appeler Graph

1. **Le module Microsoft Graph PowerShell** (`Microsoft.Graph`) : des cmdlets prêtes à l'emploi (`Get-MgUser`…) qui gèrent l'authentification et la pagination pour toi. **Recommandé pour débuter.**
2. **Les appels REST directs** (`Invoke-RestMethod` vers `https://graph.microsoft.com`) : plus de contrôle, mais tu gères toi-même le token et la pagination (Ch.31). Utile quand une fonctionnalité n'est pas couverte par le module.

#### Installer et se connecter (module)

```powershell
# Installer le module (une fois) — en CurrentUser, PAS besoin de console admin
Install-Module Microsoft.Graph -Scope CurrentUser

# Se connecter en demandant les SCOPES nécessaires (rappel Ch.30 : moindre privilège)
Connect-MgGraph -Scopes "User.Read.All", "Group.Read.All"
```

> **Note :** l'installation en `-Scope CurrentUser` ne nécessite **pas** de console administrateur (elle s'installe dans ton profil). Microsoft **recommande PowerShell 7** pour le SDK Graph ; il peut fonctionner sur d'autres versions selon les prérequis, mais 7 est la cible conseillée.

> **Le lien direct avec le Ch.30 :** `Connect-MgGraph -Scopes ...` matérialise tout ce qu'on a vu sur l'autorisation. Tu demandes des **scopes** précis ; une fenêtre de connexion t'authentifie (permissions **déléguées** : le script agira avec **tes** droits) ; un **token** est obtenu et géré par le module. Tu ne vois pas le token, mais c'est bien le mécanisme du Ch.30 qui opère.

#### Interroger Graph (module)

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

#### Se déconnecter

```powershell
Disconnect-MgGraph
```

### 🟡 Très utile en pratique

#### Les scopes et le consentement

La première connexion avec de nouveaux scopes déclenche un **consentement** : Microsoft demande d'approuver les permissions. C'est le principe d'autorisation du Ch.30 rendu visible.

- Un scope en **lecture** (`User.Read.All`) suffit pour un rapport — ne demande pas d'écriture « au cas où ».
- Un scope en **écriture** (`User.ReadWrite.All`) est nécessaire pour modifier — et bien plus sensible.

```powershell
# Pour un rapport : lecture seule (moindre privilège)
Connect-MgGraph -Scopes "User.Read.All"

# Pour modifier des comptes : écriture (plus sensible, à justifier)
Connect-MgGraph -Scopes "User.ReadWrite.All"
```

#### Un rapport d'utilisateurs Entra ID

```powershell
Connect-MgGraph -Scopes "User.Read.All"

Get-MgUser -All -Property DisplayName, UserPrincipalName, AccountEnabled, Department |
    Select-Object DisplayName, UserPrincipalName, AccountEnabled, Department |
    Export-Csv "C:\rapports\entra_users.csv" -NoTypeInformation -Encoding UTF8

Disconnect-MgGraph
```

On retrouve exactement le schéma des rapports AD (Ch.23), transposé au cloud : requête filtrée → projection → export.

#### Appel REST direct (quand le module ne couvre pas un endpoint)

Le SDK fournit `Invoke-MgGraphRequest`, qui appelle **n'importe quel endpoint Graph en réutilisant le contexte d'authentification** de `Connect-MgGraph` — sans que tu aies à manipuler le token toi-même :

```powershell
# Après Connect-MgGraph : appeler un endpoint brut avec le contexte déjà authentifié
Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/me"

# Un endpoint moins courant, non couvert par une cmdlet dédiée
Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/users?`$top=5"
```

> **Attention à une confusion courante :** `Get-MgContext` renvoie le **contexte** (compte, scopes accordés, tenant) — **pas** un access token prêt à coller dans un header `Authorization`. Pour un appel REST authentifié, utilise `Invoke-MgGraphRequest` (qui gère le token pour toi), plutôt que d'essayer d'extraire un bearer token du contexte.

> **Renvoi Ch.31 — attention à la pagination.** `Invoke-MgGraphRequest` gère l'**authentification** (il réutilise la session `Connect-MgGraph`, tu n'as pas à manipuler le token). Mais il **ne suit pas automatiquement la pagination** : si la réponse contient un `@odata.nextLink`, c'est à **toi** de rappeler cette URL pour récupérer les pages suivantes (comme au Ch.31). En résumé : les **cmdlets** Graph avec `-All` (ex. `Get-MgUser -All`) parcourent les pages pour toi ; `Invoke-MgGraphRequest` gère l'auth mais te laisse suivre `@odata.nextLink` toi-même. L'appel `Invoke-RestMethod` totalement manuel (avec ton propre token) reste possible quand tu gères l'authentification hors du SDK.

### 🔴 Bonus

#### Permissions d'application pour l'automatisation

Les exemples ci-dessus utilisent des permissions **déléguées** (tu te connectes interactivement). Pour une **tâche planifiée sans humain** (rappel Ch.30), on utilise des permissions **d'application** : on enregistre une *app* dans Entra ID, on lui attribue des permissions d'application, et on s'authentifie avec un **certificat** (préférable) ou un **secret client**. C'est plus puissant (agit sur toute l'organisation, sans utilisateur) donc plus sensible — à réserver aux automatisations, avec des permissions minimales.

```powershell
# Authentification applicative (schéma), pour un script non interactif
Connect-MgGraph -ClientId "<app-id>" -TenantId "<tenant-id>" -CertificateThumbprint "<empreinte>"
```

### ❌ Erreur classique

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

### 💡 Exercices

**Guidé (nécessite un tenant de test/dev) :** Connecte-toi à Graph en lecture (`User.Read.All`), affiche ton propre compte avec `Get-MgContext`, puis liste 5 utilisateurs avec leur UPN.

**Autonome :** Écris un script qui produit un rapport CSV des utilisateurs Entra ID désactivés (`AccountEnabled -eq $false`), avec leur nom, UPN et service. Utilise le bon scope minimal et déconnecte-toi à la fin.

### ✅ Tu sais maintenant...

- Ce qu'est Microsoft Graph (API unifiée M365/Entra ID) et la différence **AD on-premise / Entra ID cloud**
- Les deux approches : **module `Microsoft.Graph`** (recommandé) vs **REST direct** (Ch.31)
- `Connect-MgGraph -Scopes` comme application concrète de l'autorisation (Ch.30)
- Interroger utilisateurs/groupes (`Get-MgUser`, `Get-MgGroup`) et produire des rapports
- Déléguées (interactif) vs application (automatisation) pour Graph

### 💬 Questions d'entretien typiques

- **Différence entre AD on-premise et Entra ID ?** → L'AD on-premise vit sur tes contrôleurs de domaine ; Entra ID est l'annuaire cloud de Microsoft. Cmdlets différentes (`Get-ADUser` vs `Get-MgUser`).
- **Module Graph ou REST direct ?** → Le module pour la simplicité (auth et pagination gérées) ; le REST direct pour le contrôle fin ou ce que le module ne couvre pas.
- **Que fait `Connect-MgGraph -Scopes` ?** → Il demande des permissions précises, authentifie l'utilisateur et obtient un token — l'autorisation OAuth du Ch.30 en pratique.
- **Déléguées ou application pour un script planifié Graph ?** → Application (pas d'utilisateur interactif), avec certificat de préférence, permissions minimales.

---
