---
title: Chapitre 35 — Sécurité de l'exécution et durcissement
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie VIII — PowerShell pour la cybersécurité
  - index.md
---

## 🟢 Le minimum à savoir

### Journaliser ce que fait PowerShell lui-même

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

### AMSI : l'inspection à l'exécution

**AMSI** (Antimalware Scan Interface) permet à l'antivirus d'inspecter le code (scripts, commandes) **au moment où il s'exécute**, même s'il a été téléchargé et exécuté en mémoire sans toucher le disque. C'est une défense importante contre les scripts malveillants « fileless ». AMSI est actif par défaut sur les Windows modernes avec Defender ; les attaquants cherchent à le contourner, ce que la journalisation (4104) aide à repérer.

### Le Constrained Language Mode

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

## 🟡 Très utile en pratique

### La signature de scripts

Signer ses scripts avec un certificat garantit leur **intégrité** (non modifiés) et leur **origine**. Combinée à une Execution Policy `AllSigned` imposée par GPO, la signature **impose la vérification de signature dans les usages PowerShell normaux et renforce la gouvernance** (on sait d'où viennent les scripts, on détecte les modifications). En revanche — cohérence avec le Ch.1 — l'Execution Policy `AllSigned` **n'est pas** un rempart opposable à un attaquant déterminé (contournable). Pour un **contrôle de sécurité réellement opposable**, on s'appuie sur le **contrôle applicatif (App Control/WDAC ou AppLocker)** vu juste avant. La signature reste néanmoins une excellente pratique d'intégrité et de traçabilité :

```powershell
# Signer un script (avec un certificat de signature de code)
$cert = Get-ChildItem Cert:\CurrentUser\My -CodeSigningCert
Set-AuthenticodeSignature -FilePath ".\MonScript.ps1" -Certificate $cert

# Vérifier la signature (rappel Ch.34)
Get-AuthenticodeSignature ".\MonScript.ps1" | Select-Object Status
```


### Le principe de moindre privilège, appliqué

Toute la discipline du cours converge ici :

- Des **comptes de service** dédiés, avec le minimum de droits (Ch.10, 20)
- Des **scopes** d'API minimaux (Ch.30, 32)
- Des **secrets** dans un coffre, jamais en clair (Ch.33)
- Une appartenance **minimale** aux groupes privilégiés (Ch.21)
- Le remoting **restreint** (pas de `TrustedHosts = *`, Ch.29)

La sécurité n'est pas un chapitre isolé : c'est une **manière de faire** présente dans toutes les parties.

### Détecter les usages suspects de PowerShell

```powershell
# Rechercher des lignes de commande PowerShell suspectes (base64, téléchargement)
Get-WinEvent -LogName "Microsoft-Windows-PowerShell/Operational" -FilterXPath "*[System[EventID=4104]]" -MaxEvents 100 -ErrorAction SilentlyContinue |
    Where-Object { $_.Message -match "-enc|FromBase64|DownloadString|IEX|Invoke-Expression" } |
    Select-Object TimeCreated, @{N="Extrait";E={$_.Message.Substring(0, [Math]::Min(120,$_.Message.Length))}}
```


Ces motifs (`-enc`, `FromBase64String`, `DownloadString`, `IEX`) sont des signaux classiques d'exécution malveillante — à corréler, jamais à interpréter isolément.

## 🔴 Bonus

### JEA — Just Enough Administration

**JEA** permet d'accorder à un opérateur **juste les commandes nécessaires** (ex : redémarrer un service précis) via des *endpoints* de remoting contraints, **sans** lui donner de droits d'administrateur complets. C'est le moindre privilège appliqué au remoting — un sujet avancé, mais la direction à connaître pour déléguer sans sur-privilégier.

## ❌ Erreur classique

```powershell
# Se reposer sur l'Execution Policy comme sécurité
# ❌ rappel : ce n'est PAS une barrière → contrôle applicatif (App Control/WDAC) + CLM + signature

# Ne pas activer la journalisation PowerShell
# ❌ sans Script Block Logging (4104), les usages malveillants passent inaperçus
# ✅ activer par GPO : Script Block Logging + Module Logging + Transcription

# Interpréter un seul signal comme une preuve
# → base64 ou IEX peut être légitime ; corréler avant de conclure
```


## 💡 Exercices

**Guidé :** Affiche ton mode de langage courant (`$ExecutionContext.SessionState.LanguageMode`) et lis les 10 derniers événements 4104 du journal PowerShell Operational.

**Autonome :** Écris un script qui recherche dans les événements 4104 les motifs suspects (`-enc`, `DownloadString`, `IEX`) sur les dernières 24 h et produit un rapport horodaté. Rappelle en commentaire que ces motifs sont des signaux à corréler, pas des preuves.

## 🧩 Capstone Partie VIII — Script de posture défensive

Construis `Get-SecurityPosture.ps1` qui audite la posture de sécurité d'un poste :

- Script Block Logging **configuré** ? (lire la **configuration** — GPO/registre — et **non** conclure sur la simple absence d'événements 4104 récents : une absence peut juste signifier qu'aucun script n'a tourné. Optionnellement, provoquer un événement de test bénin puis vérifier son 4104)
- Mode de langage (FullLanguage vs ConstrainedLanguage)
- Pare-feu actif sur tous les profils (Ch.18)
- Admins locaux (Ch.10) et comparaison à une liste attendue
- Persistance suspecte (Ch.34 : Run, tâches, services)
- Rapport structuré (PSCustomObject → JSON/CSV), avec une note rappelant que les signaux doivent être corrélés

C'est la synthèse défensive de tout le cours : tes compétences d'administration, retournées en capacité d'audit de sécurité.

## ✅ Tu sais maintenant...

- Journaliser PowerShell : **Script Block Logging (4104)**, Module Logging, Transcription (via GPO)
- Le rôle d'**AMSI** (inspection à l'exécution, anti-fileless)
- Le contrôle applicatif (**App Control/WDAC** ou AppLocker) qui déclenche le **Constrained Language Mode** = la vraie sécurité d'exécution (vs Execution Policy)
- **Signer** ses scripts et appliquer le **moindre privilège** partout
- Détecter les usages suspects de PowerShell (motifs à corréler)

## 💬 Questions d'entretien typiques

- **Qu'est-ce qui sécurise vraiment l'exécution de scripts (pas l'Execution Policy) ?** → Le contrôle applicatif (App Control/WDAC, recommandé ; ou AppLocker) qui bascule le code non approuvé en Constrained Language Mode, plus la signature de code — imposés par GPO.
- **À quoi sert le Script Block Logging ?** → Journaliser le code PowerShell réellement exécuté (Event 4104), même obfusqué — clé pour détecter les usages malveillants.
- **Qu'est-ce qu'AMSI ?** → Une interface qui laisse l'antivirus inspecter le code à l'exécution, y compris en mémoire (contre les attaques fileless).
- **Comment déléguer une action précise sans donner les pleins droits ?** → JEA (Just Enough Administration), qui expose juste les commandes nécessaires via un endpoint contraint.

---
