---
title: Partie III — Administration réseau Windows
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
---

Le réseau est le système nerveux de toute infrastructure. Cette partie t'apprend à inspecter et configurer le réseau d'un poste Windows avec PowerShell : interfaces, adresses IP, DNS, routes, connexions et pare-feu. On y remplace avantageusement les vieux outils (`ipconfig`, `ping`, `netstat`, `nslookup`) par des cmdlets qui renvoient des **objets** exploitables.

> **Comparaison Linux :** là où Linux utilise `ip`, `ping`, `ss`, `dig`, PowerShell offre `Get-NetIPConfiguration`, `Test-Connection`, `Get-NetTCPConnection`, `Resolve-DnsName`. Même logique, mais avec des objets au lieu de texte à parser.

---

## Dans cette partie

- [Chapitre 15 — Interfaces et configuration IP](01-chapitre-15-interfaces-et-configuration-ip.md)
- [Chapitre 16 — DNS client et résolution](02-chapitre-16-dns-client-et-resolution.md)
- [Chapitre 17 — Routage et connexions](03-chapitre-17-routage-et-connexions.md)
- [Chapitre 18 — Pare-feu Windows](04-chapitre-18-pare-feu-windows.md)
