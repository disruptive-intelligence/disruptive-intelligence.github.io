---
title: Réseau — Network Security
source: Cyber/04_Hardening/HTB_Sécurité IT en entreprise.md
note: Sécurité IT en entreprise
up:
- - Sécurité IT en entreprise
  - index.md
---

- Surveiller le trafic **entrant et sortant** de l’organisation.
- Objectifs principaux :
    - détecter des comportements anormaux ;
    - limiter les mouvements d’un attaquant ;
    - conserver de la visibilité pour l’investigation.
## PCAP — Packet Capture

- Utiliser des ports **SPAN / Mirror** sur les équipements réseau pour copier le trafic vers une sonde d’analyse.
- Si possible, mettre en place **TAP**.
- Les captures réseau permettent :
    - d’observer les protocoles utilisés ;
    - d’identifier des destinations inhabituelles ;
    - de détecter certains comportements anormaux ;
    - d’effectuer une analyse post-mortem après compromission.

```
Switch
├─ trafic normal
└─ SPAN / Mirror → IDS / Sensor / Packet Capture
```

- Exemples d’éléments suspects :
	- hausse inhabituelle du trafic DNS ;
	- connexions vers une IP rare ;
	- protocole inhabituel ;
	- volume anormal de données sortantes ;
	- beaconing périodique vers une destination externe.

> ⚠️ Un port SPAN peut perdre des paquets en cas de forte charge. Pour une capture plus fiable, un **network TAP** peut être préférable.
## Segmentation réseau

- La segmentation découpe le réseau en **zones plus petites et contrôlées**.
- Elle permet :
    - de réduire la surface d’attaque ;
    - de limiter le **Lateral Movement** ;
    - de contrôler les flux entre catégories de systèmes ;
    - d’isoler les ressources critiques.

```
Users VLAN
Servers VLAN
Management VLAN
Backup VLAN
DMZ
```

### VLAN / PVLAN

- **VLAN** → sépare logiquement plusieurs réseaux de niveau 2.
- **PVLAN — Private VLAN** → permet d’isoler davantage des hôtes au sein d’un même VLAN.

> Un VLAN seul n’est pas une barrière de sécurité suffisante : les communications inter-VLAN doivent être contrôlées via **firewall / ACL / routing policy**.
## Réseau d’administration

- Les interfaces d’administration ne devraient pas être accessibles depuis n’importe quel poste utilisateur.

```
User Workstation
    X
Management Interface

Admin Network
    ↓
Management Interface
```

- À isoler idéalement :
	- interfaces de switches/routers/firewalls ;
	- hyperviseurs ;
	- iDRAC / iLO ;
	- consoles d’administration ;
	- RDP / SSH d’administration.
- Le **RDP administratif** peut par exemple être limité à un réseau dédié ou à un jump server.
## Examen des flux bloqués

- Après segmentation et mise en place de règles restrictives, il faut analyser les flux bloqués.
- Un blocage peut révéler :
	- endpoint compromis ;
	- malware tentant une communication ;
	- application non inventoriée ;
	- mauvaise configuration ;
	- dépendance oubliée ;
	- tentative de mouvement latéral.

```
Firewall DENY
→ Source ?
→ Destination ?
→ Port ?
→ Application ?
→ Legitimate ou Suspicious ?
```

→ un `DENY` n’est pas seulement un événement technique : il peut constituer un **signal de détection**.
## Alerte en cas d’utilisation anormale

- Une fois la visibilité réseau suffisante, définir des alertes sur les comportements inhabituels.
- Exemples :
	- hausse soudaine du trafic ;
	- transfert important vers Internet ;
	- protocole jamais utilisé auparavant ;
	- communication vers une destination rare ;
	- scans réseau ;
	- trafic hors des horaires habituels ;
	- saturation d’un lien.

```
Baseline normale
      ↓
Déviation importante
      ↓
Alert
```

## Baseline réseau

- Il faut connaître le **comportement réseau normal** pour repérer une anomalie.
- Cela peut inclure :
    - volumes habituels ;
    - protocoles utilisés ;
    - destinations fréquentes ;
    - horaires d’activité.
- Exemple :

```
Backup habituel : 01h00–03h00
Trafic élevé à 14h00
→ anomalie à vérifier
```

- Une anomalie n’est pas forcément malveillante : elle peut aussi révéler un problème opérationnel, comme un backup qui sature le réseau.
