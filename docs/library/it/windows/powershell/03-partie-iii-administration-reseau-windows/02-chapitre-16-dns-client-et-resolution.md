---
title: Chapitre 16 — DNS client et résolution
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie III — Administration réseau Windows
  - index.md
---

## 🟢 Le minimum à savoir

### Le DNS, en une phrase

Le **DNS** (Domain Name System) traduit les noms (`serveur.lab.local`, `google.com`) en adresses IP. Côté client, deux choses nous intéressent : **quels serveurs DNS** la machine utilise, et **comment résoudre** un nom.

### Voir et définir les serveurs DNS

```powershell
# Quels serveurs DNS utilise chaque interface ?
Get-DnsClientServerAddress -AddressFamily IPv4 |
    Select-Object InterfaceAlias, ServerAddresses

# Définir les serveurs DNS d'une interface                 [🔑 Admin]
# Machine jointe au domaine : UNIQUEMENT des DNS INTERNES (les DC/DNS du domaine)
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" `
    -ServerAddresses "192.168.1.10"                 # un seul DC/DNS
# Avec deux contrôleurs/serveurs DNS internes :
# Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses "192.168.1.10","192.168.1.11"

# Revenir au DNS automatique (via DHCP)
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ResetServerAddresses
```


> **⚠️ Ne mets JAMAIS un DNS public (8.8.8.8…) sur un poste joint au domaine.** Une machine du domaine doit interroger **exclusivement les DNS internes**, seuls capables de résoudre les enregistrements AD (localisation des contrôleurs de domaine, services…). Mettre `8.8.8.8` en secondaire casse la résolution AD de façon intermittente (le client peut interroger le mauvais serveur). La résolution des **noms Internet** se fait ensuite via des **forwarders configurés côté serveur DNS** (Ch.26) — pas en ajoutant un DNS public sur le client. C'est un pré-requis pour tout le lab AD des parties IV-V.

### Résoudre un nom : `Resolve-DnsName`

L'équivalent moderne et puissant de `nslookup` :

```powershell
Resolve-DnsName google.com                       # résolution simple (A/AAAA)
Resolve-DnsName lab.local -Type A                # enregistrements A (IPv4)
Resolve-DnsName lab.local -Type MX               # serveurs mail
Resolve-DnsName 192.168.1.10 -Type PTR           # résolution inverse (IP → nom)
Resolve-DnsName dc01.lab.local -Server 192.168.1.10   # interroger un serveur précis
```


> **📌 Réflexe `Get-Member` :** `Resolve-DnsName google.com | Get-Member` montre que le résultat est un objet avec `Name`, `Type`, `IPAddress`, `TTL`. On peut donc filtrer et exploiter la réponse, contrairement au texte brut de `nslookup`.

> **Comparaison :** `Resolve-DnsName` ≈ `dig`/`nslookup` sous Linux, mais renvoie des objets. `-Type` sélectionne le type d'enregistrement (A, AAAA, MX, CNAME, PTR, TXT, NS…).

### Le cache DNS du client

Windows garde en cache les résolutions récentes :

```powershell
Get-DnsClientCache               # voir le cache
Clear-DnsClientCache             # vider le cache (équivaut à ipconfig /flushdns)
```


> **Cas pratique :** après un changement DNS côté serveur, un client peut continuer à résoudre l'ancienne IP tant que son cache n'est pas expiré. `Clear-DnsClientCache` règle ce genre de « pourquoi ça pointe encore vers l'ancienne adresse ? ».

## 🟡 Très utile en pratique

### Diagnostiquer une résolution qui échoue

```powershell
# 1. La machine a-t-elle des serveurs DNS configurés ?
Get-DnsClientServerAddress -AddressFamily IPv4 | Select InterfaceAlias, ServerAddresses

# 2. Le serveur DNS répond-il pour ce nom ?
Resolve-DnsName dc01.lab.local -Server 192.168.1.10 -ErrorAction SilentlyContinue

# 3. Le cache contient-il une vieille entrée ?
Get-DnsClientCache -Name "*lab.local*"
```


Cette séquence est un mini-arbre de décision de dépannage DNS très courant.

## 🔴 Bonus

### Comparer résolution interne et externe

Interroger explicitement deux serveurs DNS différents permet de repérer une incohérence (split-horizon, cache empoisonné, mauvaise configuration) :

```powershell
Resolve-DnsName intranet.lab.local -Server 192.168.1.10    # DNS interne
Resolve-DnsName intranet.lab.local -Server 8.8.8.8 -ErrorAction SilentlyContinue   # DNS public
```


## ❌ Erreur classique

```powershell
# Oublier de vider le cache après un changement DNS
# → le client résout encore l'ancienne IP
Clear-DnsClientCache    # ✅

# Confondre "pas de réponse DNS" et "hôte injoignable"
# Resolve-DnsName teste la RÉSOLUTION (nom→IP), pas la connectivité
# Pour la connectivité → Test-Connection / Test-NetConnection (Ch.17)

# Interroger le DNS système alors qu'on veut tester un serveur précis
Resolve-DnsName x.lab.local -Server 192.168.1.10   # ✅ cible explicite
```


## 💡 Exercices

**Guidé :** Affiche les serveurs DNS configurés sur chaque interface, puis résous `google.com` et affiche uniquement les adresses IPv4 (`Type -eq "A"`).

**Autonome :** Écris un script `-Name` qui résout un nom, et si la résolution échoue, affiche les serveurs DNS configurés et suggère de vider le cache. Utilise `try/catch`.

## ✅ Tu sais maintenant...

- Le rôle du DNS et comment voir/définir les serveurs DNS d'une interface
- Résoudre des noms avec `Resolve-DnsName` (types A, MX, PTR…) — objets exploitables
- Gérer le cache DNS (`Get`/`Clear-DnsClientCache`)
- Une séquence de diagnostic de résolution

## 💬 Questions d'entretien typiques

- **Quelle cmdlet remplace `nslookup` ?** → `Resolve-DnsName`, qui renvoie des objets (avec `-Type`, `-Server`).
- **Pourquoi vider le cache DNS ?** → Pour forcer une nouvelle résolution après un changement côté serveur (l'ancienne entrée peut persister).
- **`Resolve-DnsName` teste-t-il la connectivité ?** → Non, seulement la résolution nom→IP. La connectivité se teste avec `Test-Connection`/`Test-NetConnection`.

---
