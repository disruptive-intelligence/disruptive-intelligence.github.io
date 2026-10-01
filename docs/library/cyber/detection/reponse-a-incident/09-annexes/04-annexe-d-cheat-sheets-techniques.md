---
title: Annexe D — Cheat sheets techniques
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Annexes
  - index.md
---

## Event IDs Windows critiques pour l'IR

| Event ID | Source | Signification IR |
|----------|--------|-----------------|
| 4624 | Security | Authentification réussie — types de logon : 2 (interactif), 3 (réseau), 10 (RDP) |
| 4625 | Security | Authentification échouée — volume élevé = brute force ou password spraying |
| 4648 | Security | Logon avec credentials explicites — indicateur de mouvement latéral |
| 4672 | Security | Attribution de privilèges spéciaux — accès administrateur |
| 4688 | Security | Création de processus — nécessite l'activation de la ligne de commande |
| 4698 | Security | Création de tâche planifiée — mécanisme de persistence fréquent |
| 4720 | Security | Création de compte — activité de backdoor account |
| 4728/4732 | Security | Ajout de membre à un groupe de sécurité global/local |
| 4769 | Security | Demande de TGS Kerberos — encryption type 0x17 (RC4) = Kerberoasting |
| 4662 | Security | Opération sur objet AD — avec GUID de réplication = DCSync |
| 5136 | Security | Modification d'objet DS — modification de GPO ou d'attribut AD |
| 5140/5145 | Security | Accès à un partage réseau / vérification d'accès à un fichier partagé |
| 7045 | System | Installation de service — mécanisme de persistence |
| 4103 | PowerShell | Module logging — modules PowerShell chargés |
| 4104 | PowerShell | Script block logging — contenu des scripts PowerShell exécutés |

## Commandes Volatility 3 essentielles

```bash
# Lister les processus
python3 vol.py -f dump.raw windows.pslist
python3 vol.py -f dump.raw windows.pstree

# Connexions réseau actives
python3 vol.py -f dump.raw windows.netscan

# DLL chargées par un processus
python3 vol.py -f dump.raw windows.dlllist --pid [PID]

# Détection d'injection de code
python3 vol.py -f dump.raw windows.malfind

# Ligne de commande des processus
python3 vol.py -f dump.raw windows.cmdline

# Extraction des hashes
python3 vol.py -f dump.raw windows.hashdump

# Handles de fichiers/registre
python3 vol.py -f dump.raw windows.handles --pid [PID]
```


## Commandes KAPE essentielles

```bash
# Triage complet Windows (tous les artefacts principaux)
kape.exe --tsource C: --tdest E:\KAPE_Output --tflush
  --target KapeTriage

# Collecte ciblée Event Logs + Prefetch + Amcache
kape.exe --tsource C: --tdest E:\KAPE_Output
  --target EventLogs,Prefetch,Amcache

# Collecte + parsing automatique
kape.exe --tsource C: --tdest E:\KAPE_Output
  --target KapeTriage --mdest E:\KAPE_Parsed
  --module !EZParser
```


---
