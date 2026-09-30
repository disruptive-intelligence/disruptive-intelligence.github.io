---
title: PARTIE VIII — POWERSHELL POUR LA CYBERSÉCURITÉ
source: IT/02_Windows/Powershell.md
note: PowerShell
chapter: 8
chapters: 8
---

> **Pourquoi la cybersécurité arrive en dernier.** On ne peut repérer une **anomalie** que si on connaît la **normale**. Grâce aux parties précédentes, tu sais désormais à quoi ressemble un système sain : quels services tournent, quels comptes existent, quelles tâches sont planifiées, quelles connexions sont attendues. Cette partie applique ces compétences au **diagnostic**, à la **détection** et au **durcissement** — dans une optique défensive (blue team), jamais offensive.
>
> On distingue clairement quatre postures : **administration** (gérer), **diagnostic** (comprendre un problème), **défense** (durcir, surveiller) et **investigation** (trier après un incident). PowerShell sert les quatre.

---


## Chapitre 34 — Diagnostic, logs et triage

### 🟢 Le minimum à savoir

#### Les journaux d'événements Windows

Les **Event Logs** sont la mémoire de Windows : chaque événement notable (connexion, erreur, démarrage de service, création de compte…) y est enregistré. C'est **la** source d'information pour le diagnostic et la sécurité. La cmdlet moderne est `Get-WinEvent`.

```powershell
# Lister les journaux disponibles et leur volume
Get-WinEvent -ListLog * | Where-Object RecordCount -gt 0 |
    Select-Object LogName, RecordCount | Sort-Object RecordCount -Descending

# Lire les derniers événements d'un journal
Get-WinEvent -LogName System -MaxEvents 20
Get-WinEvent -LogName Security -MaxEvents 20     # [🔑 Admin]
```

> **📌 Réflexe `Get-Member` :** `Get-WinEvent -LogName System -MaxEvents 1 | Get-Member` révèle `TimeCreated`, `Id`, `LevelDisplayName`, `Message`, `ProviderName`. Ces propriétés permettent de filtrer et corréler les événements.

#### Filtrer efficacement avec `-FilterHashtable`

> **⚠️ Point de performance majeur.** Sur un journal de millions d'événements, filtrer **côté serveur** avec `-FilterHashtable` est incomparablement plus rapide que tout ramener puis filtrer avec `Where-Object` (même logique qu'`-Filter` en AD, Ch.23).

```powershell
# ✅ RAPIDE : le filtre est appliqué à la source
Get-WinEvent -FilterHashtable @{
    LogName   = 'Security'
    Id        = 4625              # échecs de connexion
    StartTime = (Get-Date).AddHours(-24)
}

# ❌ LENT : ramène tout, puis filtre
Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4625 }
```

#### Les Event IDs à connaître

| Event ID | Journal | Signification |
|----------|---------|--------------|
| **4624** | Security | Connexion réussie |
| **4625** | Security | **Échec** de connexion (brute-force si répété) |
| **4634 / 4647** | Security | Déconnexion |
| **4720** | Security | **Création** d'un compte utilisateur |
| **4726** | Security | Suppression d'un compte |
| **4732 / 4728** | Security | Ajout à un groupe (local / global) — surveiller les groupes admin |
| **4688** | Security | Création d'un processus (traçabilité des exécutions) |
| **7045** | System | **Installation d'un nouveau service** (persistance possible) |
| **1102** | Security | **Effacement du journal de sécurité** (signal fort) |

> **⚠️ Les Event IDs dépendent de la stratégie d'audit — l'absence d'un événement ne prouve pas l'absence d'activité.** Windows ne génère la plupart de ces événements que si l'**audit correspondant est activé** (par GPO, Ch.25). Exemple concret : l'événement **4688** (création de processus) n'apparaît que si *Audit Process Creation* est activé ; et pour que la **ligne de commande** du processus soit renseignée dans l'événement, il faut **en plus** activer *Include command line in process creation events* — sinon le champ reste vide.
>
> C'est un piège conceptuel majeur en défense : conclure « aucun 4688 → aucun processus suspect créé » est un **faux négatif**. Le bon réflexe est celui du Ch.35 sur le 4104 : avant d'interpréter une absence, **vérifier que la journalisation est configurée**. Un journal muet peut signifier « rien ne s'est passé »… ou « on n'écoutait pas ».

#### Détecter une attaque par brute-force

Un cas d'école, qui réunit filtrage, regroupement et seuil :

```powershell
# Compter les échecs de connexion (4625) par compte sur 24h
Get-WinEvent -FilterHashtable @{ LogName='Security'; Id=4625; StartTime=(Get-Date).AddHours(-24) } |
    ForEach-Object {
        # On convertit l'événement en XML pour lire le champ PAR SON NOM (TargetUserName),
        # plutôt que par une position d'index fragile.
        $xml = [xml]$_.ToXml()
        ($xml.Event.EventData.Data | Where-Object Name -eq 'TargetUserName').'#text'
    } |
    Group-Object |
    Where-Object Count -gt 10 |
    Select-Object @{N="Compte";E={$_.Name}}, Count |
    Sort-Object Count -Descending
```

> **⚠️ Ne lis pas les champs d'un event par index (`$_.Properties[5]`).** L'ordre et le nombre des propriétés d'un événement **varient** selon la version de Windows et le type d'événement : un index en dur casse silencieusement (tu lis le mauvais champ). La méthode robuste : convertir l'événement en XML (`$_.ToXml()`) et lire le champ **par son nom** (`TargetUserName` pour le compte ciblé, `IpAddress` pour la source…). C'est un peu plus verbeux, mais fiable dans le temps.

Un compte avec des dizaines d'échecs en peu de temps = tentative de brute-force à investiguer. C'est exactement le genre de détection qu'un analyste blue team automatise.

### 🟡 Le triage : appliquer ses connaissances d'admin

Le **triage** consiste à examiner rapidement un système suspect. Tout ce qu'on a appris devient un point de contrôle. La logique : **comparer à la normale**.

#### Vérifier l'intégrité d'un fichier : `Get-FileHash`

```powershell
Get-FileHash "C:\Windows\System32\cmd.exe" -Algorithm SHA256
```

Comparer le hash d'un fichier à une référence connue détecte une altération. On vérifie aussi un téléchargement contre le hash publié par l'éditeur.

#### Vérifier la signature : `Get-AuthenticodeSignature`

```powershell
Get-AuthenticodeSignature "C:\Windows\System32\cmd.exe" |
    Select-Object Status, SignerCertificate
```

Un binaire système **non signé** ou à signature **invalide** dans un emplacement système est très suspect. `Status = Valid` et un signataire Microsoft sont attendus pour les fichiers système.

#### Détecter la persistance : les points de démarrage automatique

Un attaquant cherche à **survivre au redémarrage**. Les mécanismes de persistance sont exactement les objets qu'on sait déjà administrer :

```powershell
# 1. Clés Run/RunOnce du registre (rappel Ch.12)
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue

# 2. Tâches planifiées non-Microsoft (rappel Ch.13)
Get-ScheduledTask | Where-Object { $_.TaskPath -notlike "\Microsoft\*" } |
    Select-Object TaskName, @{N="Action";E={$_.Actions.Execute}}

# 3. Services dont le binaire est dans un emplacement inhabituel (rappel Ch.11)
Get-CimInstance Win32_Service |
    Where-Object { $_.PathName -notlike "*\Windows\*" -and $_.PathName -notlike "*Program Files*" } |
    Select-Object Name, PathName, StartName

# 4. Nouveaux services récemment installés (Event ID 7045)
Get-WinEvent -FilterHashtable @{ LogName='System'; Id=7045; StartTime=(Get-Date).AddDays(-7) } -ErrorAction SilentlyContinue
```

> **La bascule admin → sécurité :** remarque que ce sont **exactement** les mêmes cmdlets qu'en administration (Ch.11, 12, 13). La différence est l'**intention** : là où l'admin configure, l'analyste **compare à la normale** pour repérer l'anomalie. C'est pour ça qu'on a appris l'administration d'abord.

#### Détecter les comptes et connexions suspects

```powershell
# Membres du groupe Administrateurs locaux — ciblé par SID pour être portable FR/EN (rappel Ch.10)
$grpAdmins = Get-LocalGroup | Where-Object SID -eq "S-1-5-32-544"
Get-LocalGroupMember -Group $grpAdmins.Name

# Connexions établies HORS du réseau 192.168.x.x du lab (rappel Ch.17)
Get-NetTCPConnection -State Established |
    Where-Object { $_.RemoteAddress -notlike "192.168.*" -and $_.RemoteAddress -ne "127.0.0.1" } |
    ForEach-Object {
        [PSCustomObject]@{
            Distant = "$($_.RemoteAddress):$($_.RemotePort)"
            Process = (Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).Name
        }
    }
```

> **⚠️ Heuristique volontairement simplifiée.** Ce filtre ne dit pas « connexion externe » mais « connexion hors du réseau `192.168.x.x` du lab ». D'autres plages **privées** (`10.0.0.0/8`, `172.16.0.0/12`) et l'IPv6 seraient classées à tort comme extérieures. En entreprise, compare aux **plages internes réellement utilisées** chez toi. C'est le principe général du triage : un filtre grossier sert à **réduire le bruit**, pas à produire un verdict — le tri fin reste humain.

#### Les Alternate Data Streams (ADS)

NTFS permet de cacher des données dans des **flux alternatifs** attachés à un fichier — une technique de dissimulation classique :

```powershell
# Lister les flux alternatifs d'un fichier
Get-Item "C:\suspect.txt" -Stream * | Select-Object Stream, Length

# Lire un flux caché
Get-Content "C:\suspect.txt" -Stream "cache"
```

Un fichier anodin portant un flux `:` volumineux ou exécutable mérite attention.

### 🔴 Bonus

#### Un script de triage synthétique

En pratique, on regroupe ces contrôles dans un script de triage qui produit un rapport horodaté — réutilisant fonctions (Ch.7), objets (Ch.6) et gestion d'erreurs (Ch.8) :

```powershell
function Invoke-QuickTriage {
    [CmdletBinding()]
    param([string]$OutputPath = "C:\triage")

    # Test avant d'agir : le dossier de sortie doit exister
    if (-not (Test-Path $OutputPath)) { New-Item -ItemType Directory -Path $OutputPath -Force | Out-Null }

    # Groupe Administrateurs ciblé par SID → portable FR/EN (rappel Ch.10)
    $grpAdmins = Get-LocalGroup | Where-Object SID -eq "S-1-5-32-544"

    $rapport = [ordered]@{
        Date            = Get-Date
        AdminsLocaux    = (Get-LocalGroupMember -Group $grpAdmins.Name -ErrorAction SilentlyContinue).Name
        TachesNonMs     = (Get-ScheduledTask | Where-Object TaskPath -notlike "\Microsoft\*").TaskName
        RunKeys         = (Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue)
        # Nom honnête : c'est "hors 192.168.x.x", pas "externe" au sens strict
        ConnexionsHorsLAN = (Get-NetTCPConnection -State Established |
            Where-Object RemoteAddress -notlike "192.168.*").RemoteAddress
    }
    $rapport | ConvertTo-Json -Depth 4 |
        Set-Content "$OutputPath\triage_$(Get-Date -Format yyyyMMdd_HHmmss).json" -Encoding UTF8
}
```

C'est un point de départ de triage, pas un outil forensic complet — mais il montre comment tes compétences d'admin se convertissent directement en capacité défensive.

### ❌ Erreur classique

```powershell
# Filtrer les logs côté client (très lent)
Get-WinEvent -LogName Security | Where-Object Id -eq 4625   # ❌
Get-WinEvent -FilterHashtable @{LogName='Security';Id=4625}  # ✅

# Conclure trop vite ("un service hors Windows = malware")
# → un binaire hors chemin standard est un SIGNAL à investiguer, pas une preuve
# → toujours corréler (hash, signature, date, contexte) avant de conclure

# Lire le journal Security sans droits admin
Get-WinEvent -LogName Security    # ❌ sans admin → accès refusé
```

### 💡 Exercices

**Guidé :** Compte les échecs de connexion (Event ID 4625) des dernières 24 h et affiche les comptes ayant plus de 5 échecs.

**Autonome :** Écris `Get-PersistenceReport.ps1` qui collecte les clés Run (HKLM + HKCU), les tâches planifiées non-Microsoft et les services hors chemins standard, puis exporte le tout en JSON horodaté. Réutilise ce que tu sais des Ch.11-13.

### ✅ Tu sais maintenant...

- Lire et **filtrer efficacement** les Event Logs (`Get-WinEvent -FilterHashtable`)
- Les Event IDs clés (4624/4625/4720/7045/1102…)
- Détecter une attaque par brute-force
- Vérifier intégrité (`Get-FileHash`) et signature (`Get-AuthenticodeSignature`)
- Trier la persistance (Run, tâches, services) — les **mêmes cmdlets qu'en admin, avec l'intention de détecter**
- Repérer connexions suspectes et flux alternatifs (ADS)

### 💬 Questions d'entretien typiques

- **Comment détecter une attaque par brute-force en PowerShell ?** → Filtrer les Event ID 4625 sur une période, regrouper par compte, alerter au-dessus d'un seuil.
- **Pourquoi `-FilterHashtable` plutôt que `Where-Object` sur les logs ?** → Le filtrage est appliqué à la source : indispensable sur des journaux volumineux.
- **Où un malware cherche-t-il à persister ?** → Clés Run/RunOnce, tâches planifiées, services, dossiers de démarrage — tout ce qu'on sait déjà administrer.
- **Comment vérifier qu'un binaire système est légitime ?** → Sa signature (`Get-AuthenticodeSignature`, statut Valid + signataire attendu) et son hash (`Get-FileHash`) comparé à une référence.

---


## Chapitre 35 — Sécurité de l'exécution et durcissement

### 🟢 Le minimum à savoir

#### Journaliser ce que fait PowerShell lui-même

PowerShell est un outil puissant — donc utilisé aussi par les attaquants. La défense commence par **tracer son propre usage**. Trois mécanismes clés, à activer (idéalement par GPO, Ch.25) :

**Script Block Logging** — enregistre le **contenu des blocs de script traités** par PowerShell dans le journal `Microsoft-Windows-PowerShell/Operational` (Event ID **4104**). Comme il journalise le code tel qu'il est traité par le moteur, il offre souvent une **excellente visibilité sur du code décodé/désobfusqué au moment de l'exécution** — un atout majeur pour la détection. (Ne le présente pas comme une garantie absolue que *tout* script obfusqué sera toujours journalisé entièrement déminé : c'est très utile, sans être infaillible.)

```powershell
# Lire les blocs de script journalisés
Get-WinEvent -LogName "Microsoft-Windows-PowerShell/Operational" -FilterXPath "*[System[EventID=4104]]" -MaxEvents 20

# Vérifier si le Script Block Logging est CONFIGURÉ (via registre / GPO)
# EnableScriptBlockLogging = 1 → activé. L'ABSENCE d'événements 4104 ne prouve PAS qu'il est désactivé.
$k = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"
if (Test-Path $k) {
    (Get-ItemProperty $k).EnableScriptBlockLogging    # 1 = activé
} else {
    "Non configuré par GPO/registre"
}
```

**Module Logging** — journalise les commandes des modules ciblés.

**Transcription** — enregistre des **transcriptions complètes** des sessions (entrées/sorties) dans des fichiers texte :

```powershell
Start-Transcript -Path "C:\logs\session.txt"    # démarrer manuellement (ou via GPO)
# ... activité ...
Stop-Transcript
```

> **Activation par GPO :** en entreprise, ces trois mécanismes s'activent par stratégie de groupe (Ch.25) sous *Computer Configuration → Administrative Templates → Windows Components → Windows PowerShell*. C'est la boucle bouclée : on utilise les GPO (Partie V) pour durcir PowerShell.

#### AMSI : l'inspection à l'exécution

**AMSI** (Antimalware Scan Interface) permet à l'antivirus d'inspecter le code (scripts, commandes) **au moment où il s'exécute**, même s'il a été téléchargé et exécuté en mémoire sans toucher le disque. C'est une défense importante contre les scripts malveillants « fileless ». AMSI est actif par défaut sur les Windows modernes avec Defender ; les attaquants cherchent à le contourner, ce que la journalisation (4104) aide à repérer.

#### Le Constrained Language Mode

PowerShell peut fonctionner en **Constrained Language Mode (CLM)**, un mode restreint qui **réduit les capacités de PowerShell** (appels .NET arbitraires, COM, types complexes) tout en autorisant l'administration courante. Mais il faut bien distinguer les rôles :

- **Le mécanisme qui applique la politique**, c'est le **contrôle applicatif** : **App Control for Business** (le nom actuel de la technologie WDAC) ou, plus ancien, **AppLocker**. C'est lui qui décide quel code est approuvé.
- **CLM est la conséquence** : quand le contrôle applicatif est en place, PowerShell bascule **automatiquement** le code **non approuvé** en Constrained Language Mode, ce qui le prive des fonctions dangereuses.

> **Recommandation actuelle :** pour les nouveaux déploiements, Microsoft recommande **App Control for Business (WDAC)** plutôt qu'AppLocker (considéré comme la solution héritée). AppLocker reste répandu dans l'existant.

```powershell
# Voir le mode de langage courant
$ExecutionContext.SessionState.LanguageMode
# FullLanguage (normal) ou ConstrainedLanguage (restreint)
```

> **Rappel Ch.1 :** *ceci* — contrôle applicatif (App Control/WDAC, ou AppLocker) qui déclenche CLM sur le code non approuvé, plus la signature de code — constitue la **vraie** sécurité d'exécution, par opposition à l'Execution Policy qui n'est qu'un garde-fou anti-erreur. On boucle ici la nuance posée au tout début du cours.

### 🟡 Très utile en pratique

#### La signature de scripts

Signer ses scripts avec un certificat garantit leur **intégrité** (non modifiés) et leur **origine**. Combinée à une Execution Policy `AllSigned` imposée par GPO, la signature **impose la vérification de signature dans les usages PowerShell normaux et renforce la gouvernance** (on sait d'où viennent les scripts, on détecte les modifications). En revanche — cohérence avec le Ch.1 — l'Execution Policy `AllSigned` **n'est pas** un rempart opposable à un attaquant déterminé (contournable). Pour un **contrôle de sécurité réellement opposable**, on s'appuie sur le **contrôle applicatif (App Control/WDAC ou AppLocker)** vu juste avant. La signature reste néanmoins une excellente pratique d'intégrité et de traçabilité :

```powershell
# Signer un script (avec un certificat de signature de code)
$cert = Get-ChildItem Cert:\CurrentUser\My -CodeSigningCert
Set-AuthenticodeSignature -FilePath ".\MonScript.ps1" -Certificate $cert

# Vérifier la signature (rappel Ch.34)
Get-AuthenticodeSignature ".\MonScript.ps1" | Select-Object Status
```

#### Le principe de moindre privilège, appliqué

Toute la discipline du cours converge ici :

- Des **comptes de service** dédiés, avec le minimum de droits (Ch.10, 20)
- Des **scopes** d'API minimaux (Ch.30, 32)
- Des **secrets** dans un coffre, jamais en clair (Ch.33)
- Une appartenance **minimale** aux groupes privilégiés (Ch.21)
- Le remoting **restreint** (pas de `TrustedHosts = *`, Ch.29)

La sécurité n'est pas un chapitre isolé : c'est une **manière de faire** présente dans toutes les parties.

#### Détecter les usages suspects de PowerShell

```powershell
# Rechercher des lignes de commande PowerShell suspectes (base64, téléchargement)
Get-WinEvent -LogName "Microsoft-Windows-PowerShell/Operational" -FilterXPath "*[System[EventID=4104]]" -MaxEvents 100 -ErrorAction SilentlyContinue |
    Where-Object { $_.Message -match "-enc|FromBase64|DownloadString|IEX|Invoke-Expression" } |
    Select-Object TimeCreated, @{N="Extrait";E={$_.Message.Substring(0, [Math]::Min(120,$_.Message.Length))}}
```

Ces motifs (`-enc`, `FromBase64String`, `DownloadString`, `IEX`) sont des signaux classiques d'exécution malveillante — à corréler, jamais à interpréter isolément.

### 🔴 Bonus

#### JEA — Just Enough Administration

**JEA** permet d'accorder à un opérateur **juste les commandes nécessaires** (ex : redémarrer un service précis) via des *endpoints* de remoting contraints, **sans** lui donner de droits d'administrateur complets. C'est le moindre privilège appliqué au remoting — un sujet avancé, mais la direction à connaître pour déléguer sans sur-privilégier.

### ❌ Erreur classique

```powershell
# Se reposer sur l'Execution Policy comme sécurité
# ❌ rappel : ce n'est PAS une barrière → contrôle applicatif (App Control/WDAC) + CLM + signature

# Ne pas activer la journalisation PowerShell
# ❌ sans Script Block Logging (4104), les usages malveillants passent inaperçus
# ✅ activer par GPO : Script Block Logging + Module Logging + Transcription

# Interpréter un seul signal comme une preuve
# → base64 ou IEX peut être légitime ; corréler avant de conclure
```

### 💡 Exercices

**Guidé :** Affiche ton mode de langage courant (`$ExecutionContext.SessionState.LanguageMode`) et lis les 10 derniers événements 4104 du journal PowerShell Operational.

**Autonome :** Écris un script qui recherche dans les événements 4104 les motifs suspects (`-enc`, `DownloadString`, `IEX`) sur les dernières 24 h et produit un rapport horodaté. Rappelle en commentaire que ces motifs sont des signaux à corréler, pas des preuves.

### 🧩 Capstone Partie VIII — Script de posture défensive

Construis `Get-SecurityPosture.ps1` qui audite la posture de sécurité d'un poste :

- Script Block Logging **configuré** ? (lire la **configuration** — GPO/registre — et **non** conclure sur la simple absence d'événements 4104 récents : une absence peut juste signifier qu'aucun script n'a tourné. Optionnellement, provoquer un événement de test bénin puis vérifier son 4104)
- Mode de langage (FullLanguage vs ConstrainedLanguage)
- Pare-feu actif sur tous les profils (Ch.18)
- Admins locaux (Ch.10) et comparaison à une liste attendue
- Persistance suspecte (Ch.34 : Run, tâches, services)
- Rapport structuré (PSCustomObject → JSON/CSV), avec une note rappelant que les signaux doivent être corrélés

C'est la synthèse défensive de tout le cours : tes compétences d'administration, retournées en capacité d'audit de sécurité.

### ✅ Tu sais maintenant...

- Journaliser PowerShell : **Script Block Logging (4104)**, Module Logging, Transcription (via GPO)
- Le rôle d'**AMSI** (inspection à l'exécution, anti-fileless)
- Le contrôle applicatif (**App Control/WDAC** ou AppLocker) qui déclenche le **Constrained Language Mode** = la vraie sécurité d'exécution (vs Execution Policy)
- **Signer** ses scripts et appliquer le **moindre privilège** partout
- Détecter les usages suspects de PowerShell (motifs à corréler)

### 💬 Questions d'entretien typiques

- **Qu'est-ce qui sécurise vraiment l'exécution de scripts (pas l'Execution Policy) ?** → Le contrôle applicatif (App Control/WDAC, recommandé ; ou AppLocker) qui bascule le code non approuvé en Constrained Language Mode, plus la signature de code — imposés par GPO.
- **À quoi sert le Script Block Logging ?** → Journaliser le code PowerShell réellement exécuté (Event 4104), même obfusqué — clé pour détecter les usages malveillants.
- **Qu'est-ce qu'AMSI ?** → Une interface qui laisse l'antivirus inspecter le code à l'exécution, y compris en mémoire (contre les attaques fileless).
- **Comment déléguer une action précise sans donner les pleins droits ?** → JEA (Just Enough Administration), qui expose juste les commandes nécessaires via un endpoint contraint.

---


## ANNEXES

---

### Annexe A — Correspondance PowerShell / Bash / Python

Pour ceux qui viennent de Linux ou de Python. **Rappel fondamental :** Bash et la plupart des pipelines Unix manipulent du **texte** ; PowerShell manipule des **objets**. L'analogie aide à démarrer mais ne doit pas faire oublier cette différence.

| Tâche | PowerShell | Bash | Python |
|-------|-----------|------|--------|
| Lister un dossier | `Get-ChildItem` | `ls` | `os.listdir` / `pathlib` |
| Chemin existe ? | `Test-Path` | `[[ -e ]]` | `Path.exists()` |
| Lire un fichier | `Get-Content` | `cat` | `open().read()` |
| Filtrer | `Where-Object` | `grep` / `awk` | `filter` / compréhension |
| Transformer | `ForEach-Object` | boucle / `sed` | `map` / compréhension |
| Trier | `Sort-Object` | `sort` | `sorted()` |
| Compter | `Measure-Object` / `.Count` | `wc` | `len()` |
| Longueur d'une chaîne | `$s.Length` | `${#s}` | `len(s)` |
| Découper une chaîne | `-split` / `.Split()` | `cut` / IFS | `str.split()` |
| Recoller | `-join` | `paste` | `str.join()` |
| Remplacer | `-replace` / `.Replace()` | `sed` | `str.replace()` / `re.sub` |
| Variable | `$x = 1` | `x=1` | `x = 1` |
| Dictionnaire | `@{ k = v }` | `declare -A` | `{ "k": v }` |
| Condition | `if () {}` | `if [[ ]]; then` | `if:` |
| Boucle | `foreach () {}` | `for … do` | `for … in` |
| Fonction | `function f {}` | `f() {}` | `def f():` |
| Ping | `Test-Connection` | `ping` | `subprocess` |
| Requête HTTP | `Invoke-RestMethod` | `curl` | `requests` |
| Exécution distante | `Invoke-Command` | `ssh` | `paramiko` |
| JSON → objet | `ConvertFrom-Json` | `jq` | `json.loads` |

---

### Annexe B — Cmdlets essentielles par domaine

#### Découverte
`Get-Command`, `Get-Help`, `Get-Member`, `Get-Module`, `Get-Verb`

#### Système & infos
`Get-CimInstance`, `Get-ComputerInfo`, `Get-Date`, `$env:`, `$PSVersionTable`

#### Fichiers
`Get-ChildItem`, `Get/Set/Add-Content`, `Copy/Move/Remove-Item`, `New-Item`, `Test-Path`, `Join-Path`, `Get-Acl`, `Set-Acl`, `Select-String`

#### Comptes locaux
`Get/New/Set/Disable/Enable-LocalUser`, `Get-LocalGroup`, `Get-LocalGroupMember`, `Add/Remove-LocalGroupMember`

#### Processus & services
`Get/Start/Stop-Process`, `Get/Start/Stop/Restart/Set-Service`, `Get-CimInstance Win32_Service`

#### Registre
`Get-ChildItem`, `Get-ItemProperty`, `Get-ItemPropertyValue`, `New/Set/Remove-ItemProperty`, `Test-Path`

#### Tâches planifiées
`Get-ScheduledTask`, `Get-ScheduledTaskInfo`, `New-ScheduledTaskAction/Trigger/Principal`, `Register/Unregister-ScheduledTask`

#### Stockage
`Get-Disk`, `Get-Partition`, `Get-Volume`, `Get-PSDrive`, `Get-WindowsFeature` (Server)

#### Réseau
`Get-NetIPConfiguration`, `Get-NetAdapter`, `Get-NetIPAddress`, `New-NetIPAddress`, `Get/Set-DnsClientServerAddress`, `Resolve-DnsName`, `Get-NetRoute`, `Get-NetTCPConnection`, `Test-Connection`, `Test-NetConnection`, `Get/New/Set/Remove-NetFirewallRule`

#### Active Directory
`Get/New/Set/Remove-ADUser`, `Enable/Disable/Unlock-ADAccount`, `Set-ADAccountPassword`, `Get/New-ADGroup`, `Get/Add/Remove-ADGroupMember`, `Get-ADPrincipalGroupMembership`, `Get/New/Set/Remove-ADComputer`, `Get/New-ADOrganizationalUnit`, `Move-ADObject`, `Search-ADAccount`, `Get-ADDomain`

#### GPO & Server
`Get/New/Remove-GPO`, `New/Set-GPLink`, `Get-GPOReport`, `Backup/Restore-GPO`, `Get-GPResultantSetOfPolicy`, `Get-DnsServerZone`, `*-DnsServerResourceRecord*`, `Get-DhcpServerv4Scope/Lease`, `Add-DhcpServerv4Reservation`, `Get/New-SmbShare`, `Get-SmbSession`, `Get-SmbShareAccess`

#### Distant & API
`Enter-PSSession`, `Invoke-Command`, `New/Remove-PSSession`, `Enable-PSRemoting`, `Invoke-RestMethod`, `Invoke-WebRequest`, `ConvertTo/From-Json`, `Connect-MgGraph`, `Get-MgUser`, `Get-MgGroup`

#### Industrialisation
`Export-ModuleMember`, `Import-Module`, `Get/Set-Secret`, `Start/Stop-Transcript`, `Invoke-Pester`

#### Sécurité & triage
`Get-WinEvent`, `Get-FileHash`, `Get-AuthenticodeSignature`, `Set-AuthenticodeSignature`, `Get-Item -Stream`

---

### Annexe C — Event IDs de référence

| Event ID | Journal | Signification |
|----------|---------|--------------|
| 4624 | Security | Connexion réussie |
| 4625 | Security | Échec de connexion (brute-force si répété) |
| 4634 / 4647 | Security | Déconnexion |
| 4648 | Security | Connexion avec identifiants explicites |
| 4672 | Security | Privilèges spéciaux attribués (compte à privilèges) |
| 4688 | Security | Création d'un processus |
| 4720 | Security | Création d'un compte |
| 4722 / 4725 | Security | Compte activé / désactivé |
| 4726 | Security | Suppression d'un compte |
| 4728 / 4732 | Security | Ajout à un groupe (global / local) |
| 4740 | Security | Compte verrouillé |
| 1102 | Security | Journal de sécurité effacé (signal fort) |
| 7045 | System | Nouveau service installé |
| 7040 | System | Type de démarrage d'un service modifié |
| 4104 | PowerShell/Operational | Bloc de script exécuté (Script Block Logging) |

---

### Annexe D — Droits, versions et modules requis

| Opération | Droits | Version / Environnement | Module |
|-----------|--------|------------------------|--------|
| Lire services/processus | Standard | 5.1 / 7 | intégré |
| Modifier services, écrire `HKLM:` | **Admin** | 5.1 / 7 | intégré |
| Lire journal Security | **Admin** | 5.1 / 7 | intégré |
| `Get-WmiObject` | — | **5.1 seulement** (absent en 7) | intégré |
| `Get-CimInstance` | selon classe | 5.1 / 7 | intégré |
| Cmdlets `*-LocalUser` | Admin (modif) | Win 10/11 & Server | LocalAccounts |
| Cmdlets `*-AD*` | délégué/Admin | 5.1 / 7 + **RSAT** ou DC | ActiveDirectory |
| Cmdlets `*-GPO`, `*-GPLink` | Admin | **RSAT** ou DC | GroupPolicy |
| `Install-WindowsFeature` | Admin | **Windows Server uniquement** | ServerManager |
| Cmdlets `*-DnsServer*` | Admin | Serveur DNS ou RSAT | DnsServer |
| Cmdlets `*-DhcpServer*` | Admin | Serveur DHCP ou RSAT | DhcpServer |
| `Enable-PSRemoting` | **Admin** | 5.1 / 7 | intégré |
| `Connect-MgGraph`, `Get-Mg*` | selon scopes | 5.1 / 7 | Microsoft.Graph |
| `Invoke-Pester` | Standard | 5.1 / 7 | Pester |
| `ForEach-Object -Parallel` | Standard | **7 uniquement** | intégré |
| Opérateur ternaire `? :` | Standard | **7 uniquement** | intégré |

> **Note sur la compatibilité des modules Windows en PowerShell 7.** Les modules d'administration Windows n'ont pas tous le même statut en PS7. Certains sont **nativement compatibles** ; d'autres (historiquement liés à Windows PowerShell) sont chargés via la **couche de compatibilité Windows PowerShell** : PS7 les exécute en réalité dans une session Windows PowerShell 5.1 en arrière-plan et **sérialise** les objets échangés — ce qui fonctionne dans la grande majorité des cas, mais peut entraîner des **limitations** (objets « désérialisés » sans leurs méthodes, quelques différences de comportement). En pratique, pour ce cours : `ActiveDirectory`, `DnsServer`, `DhcpServer`, `GroupPolicy`, `ServerManager` fonctionnent en 7, parfois via cette couche de compatibilité. En cas de comportement inattendu sur un objet renvoyé par un de ces modules, vérifie s'il n'est pas désérialisé (un `Get-Member` montrera des types préfixés `Deserialized.`) et, au besoin, exécute la commande depuis une console Windows PowerShell 5.1. La liste exacte évolue : consulte la matrice de compatibilité Microsoft si un module précis pose problème.

---

### Annexe E — Pièges classiques et corrections

| Piège | ❌ Incorrect | ✅ Correct |
|-------|-------------|-----------|
| Comparaison | `if ($a == $b)` | `if ($a -eq $b)` |
| Interpolation de propriété | `"$obj.Prop"` | `"$($obj.Prop)"` |
| Concaténer deux caractères | `$s[0] + $s[1]` (→ addition **numérique** : 195) | `-join @($s[0], $s[1])` ou `"$($s[0])$($s[1])"` |
| Plage calculée pouvant valoir 0 | `1..($n - 4)` (si `$n=4` → `1..0` = **@(1,0)**, 2 éléments !) | tester `if ($n -gt 4) { 1..($n - 4) }` |
| Format avant traitement | `... \| Format-Table \| Export-Csv` | `... \| Export-Csv` (Format en dernier) |
| Filtrer côté client | `Get-ADUser -Filter * \| Where …` | `Get-ADUser -Filter "…"` |
| Encodage fichier | `Set-Content x` | `Set-Content x -Encoding UTF8` |
| `Get-WmiObject` en PS7 | `Get-WmiObject …` | `Get-CimInstance …` |
| Inventaire logiciels | `Win32_Product` | clés `Uninstall` du registre |
| Variable distante | `{ Get-Service $nom }` | `{ Get-Service $using:nom }` |
| try/catch sans Stop | `try { Get-… }` | `try { Get-… -ErrorAction Stop }` |
| `$?` après un .exe | `ping…; if (-not $?)` | `ping…; if ($LASTEXITCODE -ne 0)` |
| Créer sans vérifier | `New-ADUser …` | `if (-not (Get-ADUser …)) { New-ADUser … }` |
| Masse sans simuler | `New-ADUser …` (en boucle) | `… -WhatIf` d'abord |
| Secret en clair | `$token = "abc"` | SecretManagement / SecureString |
| Execution Policy = sécurité | s'y fier | contrôle applicatif (App Control/WDAC) → CLM + signature |
| WinRM « toujours chiffré » | affirmation brute | nuancer (Kerberos domaine / NTLM-HTTPS hors domaine) |
| `LastLogonDate` exact | s'y fier à la minute | approximatif (réplication différée) |
| Permissions fichiers | ne voir que SMB ou que NTFS | l'intersection des deux gagne |

---

### Annexe F — Les deux réflexes transversaux

Tout le cours repose sur deux habitudes. Si tu ne retiens que ça :

#### Réflexe 1 — Explorer avec `Get-Member`

Face à **tout** objet inconnu (service, utilisateur AD, tâche, réponse d'API, événement…) :

```powershell
<commande> | Get-Member
```

Tu découvres ses propriétés (informations) et méthodes (actions). Tu n'as pas à mémoriser PowerShell — tu l'explores. On l'a appliqué à chaque nouveau type d'objet du cours.

#### Réflexe 2 — `Get`/`Test` avant `Set`/`New`/`Remove`

On regarde **toujours** avant de modifier :

```powershell
Get-…    /  Test-…        # 1. observer l'état actuel
# … décision …
Set-… / New-… / Remove-…  # 2. agir en connaissance de cause
-WhatIf                    # 3. et pour les opérations sensibles/en masse, simuler d'abord
```

Cette discipline — vérifier, simuler, sauvegarder avant d'agir — traverse toute l'administration, de la création d'un dossier (Ch.9) à l'onboarding de masse (Ch.24) en passant par les GPO (Ch.25) et le registre (Ch.12).

---

### Annexe G — Parcours de certification et ressources

#### Certifications utiles (à jour 2025-2026)

| Certification | Éditeur | Portée |
|--------------|---------|--------|
| **AZ-104** (Azure Administrator) | Microsoft | Administration cloud, inclut PowerShell/Graph |
| **MD-102** (Endpoint Administrator) | Microsoft | Postes de travail, Intune |
| **AZ-802** (Windows Server Administrator Associate) | Microsoft | Windows Server, AD, hybride — successeur 2026, remplace AZ-800/AZ-801 (retirés le 30/09/2026) |
| **SC-300** (Identity and Access) | Microsoft | Entra ID, identité |
| **Sec+** (Security+) | CompTIA | Fondamentaux sécurité (utile Partie VIII) |

> Les certifications Microsoft évoluent régulièrement (noms, codes, contenus). Vérifie les intitulés actuels sur le site officiel Microsoft Learn avant de t'engager.

#### Ressources d'apprentissage

- **Microsoft Learn** — documentation officielle et parcours gratuits
- **`Get-Help` et `Get-Command`** — ta première documentation, toujours à portée
- **PowerShell Gallery** ([powershellgallery.com](https://www.powershellgallery.com/)) — modules communautaires
- **Le dépôt GitHub PowerShell** — source, discussions, nouveautés
- **Communautés** : r/PowerShell, PowerShell.org, les forums Microsoft Q&A

#### Pour approfondir séparément

Ce cours t'a donné les fondations PowerShell pour piloter Windows. Pour aller plus loin sur chaque technologie **en tant que telle**, oriente-toi vers des cours dédiés :

- **Active Directory** (conception, réplication, FSMO, approbations, sécurité AD)
- **Windows Server** (rôles avancés, clustering, stockage)
- **Réseau Windows** (routage, VLAN, VPN)
- **Entra ID / Microsoft 365 / Intune** (identité et gestion cloud)
- **Cybersécurité Windows / Digital Forensics** (investigation approfondie)
- **PowerShell avancé** (classes, DSC, modules binaires, CI/CD)

---

### Conclusion

Tu es parti de zéro et tu sais maintenant :

- **Comprendre PowerShell** : cmdlets `Verbe-Nom`, pipeline **objet**, variables, conditions, boucles, fonctions, gestion d'erreurs
- **Administrer un poste Windows** : fichiers et permissions NTFS, comptes locaux, processus, services, registre, tâches, disques, logiciels
- **Gérer le réseau** : IP, DNS, routage, connexions, pare-feu
- **Automatiser Active Directory** : utilisateurs, groupes, ordinateurs, OU, recherche filtrée, onboarding de masse
- **Piloter GPO et services serveur** : stratégies de groupe, DNS, DHCP, partages SMB
- **Administrer à distance et via API** : Remoting nuancé, authentification/tokens, REST, Microsoft Graph
- **Industrialiser** : modules, secrets, idempotence, `-WhatIf`, tests
- **Défendre** : diagnostic, triage, journalisation, durcissement

Et surtout, tu as acquis les **deux réflexes** qui te rendront autonome bien au-delà de ce cours : **explorer avec `Get-Member`** tout objet inconnu, et **observer avant d'agir** (`Get`/`Test` → `Set`/`New`/`Remove`, puis `-WhatIf`).

Le niveau atteint est celui d'un **administrateur Windows PowerShell junior solide** : capable d'administrer, d'automatiser, de diagnostiquer, et de s'appuyer sur ces bases pour se spécialiser. PowerShell n'est pas une fin en soi — c'est le **fil conducteur** qui relie toute l'administration Windows. Tu tiens maintenant ce fil. À toi de tirer.

**Bon scripting, et bonne administration !**
