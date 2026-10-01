---
title: Commandes et outils
source: IT/02 Windows/Windows — fiche cyber.md
note: Windows — fiche cyber
up:
- - Windows — fiche cyber
  - index.md
---

## 16. CMD, PowerShell et commandes essentielles

### À retenir

- **CMD** : interpréteur classique pour commandes ponctuelles et scripts simples.
- **PowerShell** : plus puissant, basé sur .NET, utilise des **cmdlets** (`Verbe-Nom`, ex. `Get-Service`).
- **Execution Policy** : limite l'exécution de scripts (`Restricted`, `RemoteSigned`, `Bypass`...). Ce **n'est pas une vraie barrière de sécurité** : elle se contourne en une ligne.

### Commandes utiles

**Système** — énumération de base

```cmd
systeminfo / ver / set
```

**Réseau** — cartographier connexions et résolution

```cmd
ipconfig /all               # Infos réseau complètes
netstat -abon               # Connexions + ports + PID + programme
nslookup example.com        # Résolution DNS
```

**Fichiers** — navigation et lecture

```cmd
dir / cd / tree / type
```

**Processus** — lister et arrêter

```cmd
tasklist                    # Processus en cours
tasklist /FI "imagename eq sshd.exe"
taskkill /PID <pid>
```

**PowerShell** — services, objets, contournement de policy

```powershell
Get-Service / Get-Process
Get-ChildItem -Recurse
Set-ExecutionPolicy Bypass -Scope Process   # Pour la session courante
```


### Point clé à mémoriser
`netstat -abon` pour le réseau, `tasklist`/`taskkill` pour les processus. L'Execution Policy ne protège pas vraiment.

---

## 17. Outils utiles : Task Manager et Sysinternals

### À retenir
La suite **Sysinternals** (sans installation) complète le Task Manager pour l'analyse fine des processus, du réseau et de la persistance.

### Comment ça fonctionne

| Outil | Usage | Intérêt cyber |
| --- | --- | --- |
| **Task Manager** | Processus, services, perfs, programmes au démarrage | Repérage rapide d'un processus anormal |
| **Process Explorer** | Task Manager amélioré : hiérarchie parent/enfant, handles, DLL, signatures | Identifier un imposteur via son parent et sa signature |
| **Process Monitor (Procmon)** | Traces temps réel FS / Registre / Réseau | Suivre ce qu'un binaire touche réellement |
| **TCPView** | Connexions réseau actives par processus | Détecter une connexion sortante suspecte |
| **PsExec** | Exécution de commandes à distance via SMB (admin) | Mouvement latéral / administration distante |

### Pourquoi c'est important en cyber
Ces outils servent autant à l'**analyse SOC** (repérer un processus ou une connexion malveillante) qu'à la **reconnaissance en pentest** (trouver des chemins d'élévation, observer le comportement d'un binaire). Sans installation, ils s'utilisent même sur une machine compromise.

### Commandes utiles

```cmd
\\live.sysinternals.com\tools\procdump.exe -accepteula
```


### Point clé à mémoriser
Process Explorer pour parent/enfant, Procmon pour le temps réel, TCPView pour le réseau, PsExec pour le distant.

---
