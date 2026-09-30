---
title: Chapitre 31 — API REST avec PowerShell
source: IT/02_Windows/Powershell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie VI — Administration distante, API ET automatisation
  - index.md
---

## 🟢 Le minimum à savoir

### Ce qu'est une API REST, en clair

Une **API REST** est une interface qui permet à des programmes de dialoguer via le web. Concrètement : tu envoies une requête HTTP à une **URL** (endpoint), et tu reçois une réponse, presque toujours en **JSON**. C'est ainsi qu'un script PowerShell peut interroger un service en ligne, un outil de ticketing, un système de supervision, ou Microsoft Graph (Ch.32).

### Le vocabulaire HTTP minimal

| Terme | Ce que c'est |
|-------|-------------|
| **URI / endpoint** | L'adresse de la ressource (`https://api.exemple.com/v1/users`) |
| **Méthode** | L'action : `GET` (lire), `POST` (créer), `PUT`/`PATCH` (modifier), `DELETE` (supprimer) |
| **Headers** | Métadonnées de la requête (authentification, type de contenu…) |
| **Body** | Les données envoyées (pour POST/PUT/PATCH), en général du JSON |
| **Status code** | Le résultat : `200` OK, `201` créé, `401` non authentifié, `403` interdit, `404` introuvable, `429` trop de requêtes, `500` erreur serveur |

### `Invoke-RestMethod` : la cmdlet clé

`Invoke-RestMethod` envoie une requête HTTP **et convertit automatiquement le JSON de réponse en objets PowerShell**. C'est ce qui rend PowerShell si agréable pour les API :

```powershell
# GET simple — la réponse JSON devient un objet directement exploitable
$reponse = Invoke-RestMethod -Uri "https://api.github.com/users/powershell"
$reponse.name           # "PowerShell"
$reponse.public_repos   # un nombre
```


> **📌 Réflexe `Get-Member` :** `Invoke-RestMethod -Uri "..." | Get-Member` te montre la structure de la réponse — les propriétés que l'API renvoie. C'est ainsi qu'on découvre ce qu'une API expose, sans deviner.

### `Invoke-RestMethod` vs `Invoke-WebRequest`

- **`Invoke-RestMethod`** : parse automatiquement le JSON en objets. **À privilégier pour les API REST.**
- **`Invoke-WebRequest`** : renvoie la réponse HTTP brute (status, headers, contenu texte). Utile quand on a besoin des détails HTTP (code de statut exact, headers de réponse) ou pour du web non-API.

### Envoyer des headers (dont l'authentification)

Rappel du Ch.30 : l'authentification passe souvent par un header `Authorization` :

```powershell
$headers = @{
    Authorization = "Bearer $token"
    Accept        = "application/json"
}
Invoke-RestMethod -Uri "https://api.exemple.com/v1/me" -Headers $headers
```


### Envoyer des données : POST avec un body JSON

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

## 🟡 Très utile en pratique

### Gérer les erreurs HTTP

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

### La pagination

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

### Query parameters

Les paramètres de requête affinent une requête GET (`?cle=valeur&autre=valeur`) :

```powershell
$params = @{ q = "powershell"; sort = "stars"; per_page = 5 }
Invoke-RestMethod -Uri "https://api.github.com/search/repositories" -Body $params
# En GET, -Body est encodé comme query string : ?q=powershell&sort=stars&per_page=5
```


## 🔴 Bonus

### Un mini-connecteur réutilisable

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

## ❌ Erreur classique

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


## 💡 Exercices

**Guidé :** Avec `Invoke-RestMethod`, interroge `https://api.github.com/users/microsoft` et affiche le nom, le nombre de dépôts publics et la date de création. Explore la réponse avec `Get-Member`.

**Autonome :** Écris une fonction `Get-GitHubRepos -User <nom>` qui récupère les dépôts publics d'un utilisateur GitHub (gère la pagination via le header `Link` ou le paramètre `page`), et exporte nom + langage + nombre d'étoiles en CSV.

## ✅ Tu sais maintenant...

- Ce qu'est une API REST (endpoint, méthode, headers, body, status code)
- `Invoke-RestMethod` (JSON → objets automatiquement) vs `Invoke-WebRequest`
- Envoyer des headers d'authentification (Bearer, rappel Ch.30) et un body JSON (`ConvertTo-Json`)
- Gérer les erreurs HTTP (401/403/404/429) et la **pagination**
- Encapsuler les appels dans une fonction réutilisable

## 💬 Questions d'entretien typiques

- **`Invoke-RestMethod` ou `Invoke-WebRequest` ?** → `Invoke-RestMethod` pour les API REST (conversion JSON→objets automatique) ; `Invoke-WebRequest` quand on a besoin des détails HTTP bruts.
- **Que signifie un 401 vs un 403 ?** → 401 = non authentifié (token absent/expiré) ; 403 = authentifié mais non autorisé (scope insuffisant).
- **Comment récupérer tous les résultats d'une API paginée ?** → Boucler en suivant le lien de page suivante jusqu'à ce qu'il soit nul.

---
