---
title: Chapitre 29 — PowerShell Remoting
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie VI — Administration distante, API et automatisation
  - index.md
---

## 🟢 Le minimum à savoir

### Le principe

**PowerShell Remoting** exécute des commandes sur des machines distantes — c'est l'équivalent Windows de SSH. Il repose sur **WinRM** (Windows Remote Management), le service qui écoute les connexions distantes.

Deux usages :

- **Session interactive** (`Enter-PSSession`) : tu « entres » sur la machine distante, comme SSH
- **Commande distante** (`Invoke-Command`) : tu envoies un bloc de code à exécuter, éventuellement sur plusieurs machines à la fois

### Activer le remoting `[🔑 Admin]`

```powershell
# Sur la machine CIBLE (celle qu'on veut administrer), une seule fois
Enable-PSRemoting -Force
```


En environnement AD, le remoting est souvent déjà activé (par GPO) sur les serveurs.

### Session interactive

```powershell
Enter-PSSession -ComputerName SRV01
# [SRV01]: PS C:\>   ← tu es maintenant SUR SRV01
Get-Service           # s'exécute sur SRV01
Exit-PSSession        # revenir sur ta machine
```


### Commande distante (le cas le plus puissant)

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

### Le modèle d'exécution : local vs distant

> **Point important :** le `-ScriptBlock` s'exécute **sur la machine distante**, avec ses variables et son contexte. Tes variables locales n'y sont **pas** disponibles automatiquement — il faut les passer explicitement :
> ```powershell
> $nomService = "wuauserv"
> Invoke-Command -ComputerName SRV01 -ScriptBlock {
>     Get-Service -Name $using:nomService     # $using: injecte la variable locale
> }
> ```
> Le préfixe `$using:` transporte une variable locale dans le bloc distant. Sans lui, `$nomService` serait vide côté serveur.

## 🟡 WinRM, authentification et sécurité : les vraies nuances

> **⚠️ Correction d'une simplification répandue.** On lit souvent « WinRM est chiffré » ou « le remoting utilise HTTPS ». La réalité est plus nuancée, et un administrateur doit la connaître.

### Le transport : HTTP (5985) vs HTTPS (5986)

Par défaut, WinRM écoute sur le port **5985 (HTTP)**. Cela ne veut **pas** dire que tout circule en clair : dans un domaine, l'**authentification et le chiffrement** du contenu sont assurés au niveau du protocole d'authentification (voir ci-dessous), même sur le port HTTP. Le port **5986 (HTTPS)** ajoute une couche TLS au niveau **transport** (avec un certificat), utile hors domaine ou pour une exigence de conformité.

### Les mécanismes d'authentification

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

### Les sessions persistantes

Ouvrir une connexion à chaque `Invoke-Command` est coûteux. Une **session persistante** (`PSSession`) maintient la connexion pour plusieurs commandes :

```powershell
$session = New-PSSession -ComputerName SRV01
Invoke-Command -Session $session -ScriptBlock { $svc = Get-Service }   # la variable persiste
Invoke-Command -Session $session -ScriptBlock { $svc.Count }           # réutilisable
Remove-PSSession $session                                              # fermer proprement
```


## 🔴 Bonus

### Exécution en parallèle sur un grand parc

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

## ❌ Erreur classique

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


## 💡 Exercices

**Guidé :** Avec `Invoke-Command`, récupère l'heure de dernier démarrage de deux machines de ton lab et affiche le résultat avec `PSComputerName`.

**Autonome :** Écris un script qui prend une liste de `-ComputerName`, exécute à distance une collecte (OS, uptime, espace disque C:), et renvoie un PSCustomObject par machine (avec `PSComputerName`). Gère les machines injoignables avec `try/catch`.

## ✅ Tu sais maintenant...

- Le remoting via WinRM : session interactive (`Enter-PSSession`) et commande distante (`Invoke-Command`)
- Cibler plusieurs machines et exploiter `PSComputerName`
- Passer des variables locales avec `$using:`
- **Les vraies nuances WinRM** : HTTP/5985 vs HTTPS/5986, Kerberos (domaine) vs NTLM/TrustedHosts/HTTPS (hors domaine)
- Les sessions persistantes (`New`/`Remove-PSSession`)

## 💬 Questions d'entretien typiques

- **Le remoting WinRM est-il chiffré ?** → En domaine, oui : Kerberos authentifie et chiffre le contenu même sur le port HTTP 5985. Hors domaine, il faut NTLM correctement configuré, TrustedHosts (moins sûr) ou HTTPS.
- **Comment utiliser une variable locale dans un `Invoke-Command` distant ?** → Avec le préfixe `$using:`.
- **Comment savoir de quelle machine vient un résultat ?** → La propriété `PSComputerName`, ajoutée automatiquement par `Invoke-Command`.
- **Pourquoi `TrustedHosts = *` est-il déconseillé ?** → Il fait confiance à toutes les machines, contournant des protections ; on limite à la liste nécessaire ou on utilise HTTPS.

---
