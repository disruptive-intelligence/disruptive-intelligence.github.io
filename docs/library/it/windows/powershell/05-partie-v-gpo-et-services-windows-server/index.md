---
title: Partie V — GPO et services Windows server
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
---

> **🏗️ On reste dans l'administration d'infrastructure.** Cette partie couvre les stratégies de groupe (GPO) et trois rôles serveur essentiels : DNS, DHCP et le partage de fichiers (SMB). Environnement requis : le lab Windows Server de la Partie IV.
>
> **PowerShell reste le fil rouge.** On n'apprend pas ici à concevoir une architecture DNS ou un plan d'adressage — on apprend à *piloter* ces rôles avec PowerShell. Pour la conception, réfère-toi aux cours dédiés à chaque technologie.
>
> **⚠️ Lab uniquement.** Comme en Partie IV, ces chapitres modifient des éléments d'infrastructure (GPO liées à des OU, enregistrements DNS, étendues DHCP, partages). Une GPO mal réglée ou un enregistrement DNS erroné affecte **tout un domaine**. Pratique exclusivement sur ton lab, et sauvegarde avant de modifier (`Backup-GPO`, export de zone…).

---

## Dans cette partie

- [Chapitre 25 — Group Policy (GPO)](01-chapitre-25-group-policy-gpo.md)
- [Chapitre 26 — DNS Server](02-chapitre-26-dns-server.md)
- [Chapitre 27 — DHCP Server](03-chapitre-27-dhcp-server.md)
- [Chapitre 28 — File Server et partages SMB](04-chapitre-28-file-server-et-partages-smb.md)
