---
title: Types / périmètres de surfaces d’attaque
source: Cyber/99_Concepts/HTB_Attack Surface Management.md
note: HTB — Attack Surface Management
up:
- - HTB — Attack Surface Management
  - index.md
---

- L’ASM peut couvrir plusieurs **périmètres d’exposition**, selon les types d’assets observés et leur position dans l’environnement.
- L’objectif reste le même :

```
Discover
→ Understand Exposure
→ Assess Risk
→ Reduce Attack Surface
```


| Type                                                                     | Définition                                                                                        | Assets / éléments concernés                                                                                                                                                                 |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ASM Externe -          **EASM — External Attack Surface Management**     | Gestion de la surface visible depuis Internet                                                     | Inclut les sites web, l’infrastructure cloud publique et les comptes de réseaux sociaux. Domaines, sous-domaines, IP publiques, websites, APIs, services exposés, cloud public, certificats |
| ASM Interne -            **IASM — Internal Attack Surface Management**   | Gestion de la surface d’attaque des ressources internes                                           | Inclut les équipements, les applications et les réseaux internes. Endpoints, serveurs, Active Directory, applications internes, VLAN, services et ports internes                            |
| ASM des assets cyber - **CAASM — Cyber Asset Attack Surface Management** | Consolidation et corrélation des informations sur les cyber-assets afin d’obtenir une vue unifiée | Inclut les logiciels, les données et la propriété intellectuelle. Endpoints, servers, cloud assets, identities, security tools, vulnerability data                                          |
| **OSASM : Open-Source / Software Supply Chain**                          | Gestion des risques provenant des composants logiciels tiers et open source                       | libraries, frameworks, packages, dependencies, containers                                                                                                                                   |
## EASM — External Attack Surface Management

- Se concentre sur **ce qu’un attaquant externe peut découvrir depuis Internet**.

```
Internet
→ Domains
→ IPs
→ Services
→ Applications
→ Cloud Resources
```


Exemples :

- domaine oublié ;
- sous-domaine exposé ;
- VPN gateway ;
- RDP/SSH accessible ;
- API publique ;
- bucket cloud mal configuré ;
- certificat révélant un hostname ;
- application Shadow IT.
### Objectif

```
What can an external attacker see?
```

→ identifier et réduire les expositions accessibles **sans accès préalable au réseau interne**.
## IASM — Internal Attack Surface Management

- Se concentre sur les actifs et chemins d’attaque présents **à l’intérieur de l’organisation**.

Exemples :

```
Endpoints
Servers
Active Directory
Internal Applications
Network Segments
Databases
Internal Services
```


L’IASM cherche notamment à identifier :

- systèmes vulnérables ;
- ports/services inutiles ;
- mauvaises configurations ;
- privilèges excessifs ;
- segmentation insuffisante ;
- chemins de lateral movement.

```
Initial Compromise
→ Internal Exposure
→ Lateral Movement
→ Critical Asset
```


> EASM regarde principalement **l’exposition avant compromission**, tandis que l’IASM aide aussi à comprendre ce qu’un attaquant pourrait atteindre **après avoir obtenu un premier accès**.
## CAASM — Cyber Asset Attack Surface Management

- **CAASM** vise surtout à obtenir une **vue centralisée et cohérente des cyber-assets** en agrégeant les informations provenant de plusieurs outils.

```
EDR
Vulnerability Scanner
CMDB
Cloud
IAM
Network Tools
      ↓
    CAASM
      ↓
Unified Asset View
```


Il permet notamment de répondre à :

```
What assets exist?
Who owns them?
Are they managed?
Are they vulnerable?
Which security controls cover them?
```

### Intérêt

- détecter les assets inconnus ;
- identifier les gaps de couverture ;
- corréler asset + vulnerability + identity + security controls ;
- améliorer la qualité de l’inventaire.

> ⚠️ **CAASM n’est pas vraiment une “surface d’attaque” distincte au même titre que EASM/IASM**. C’est plutôt une capacité/approche d’ASM centrée sur la **visibilité et la consolidation des assets**.
## Open Source & Software Supply Chain

- `OSASM` correspond davantage à la gestion de la surface d’attaque introduite par les **composants logiciels tiers et open source**.

Exemples :

```
Application
├─ Library A
├─ Framework B
├─ Package C
└─ Container Image
```


Risques :

- dépendance vulnérable ;
- package obsolète ;
- dependency confusion ;
- package malveillant ;
- composant abandonné ;
- vulnérabilité transitive.

Les mécanismes les plus utilisés sont plutôt :

```
SCA
→ Software Composition Analysis

SBOM
→ Software Bill of Materials
```

### SCA

- détecte les dépendances utilisées ;
- identifie les versions ;
- compare avec les CVE connues ;
- signale les composants vulnérables.
### SBOM

- fournit l’inventaire des composants constituant un logiciel.

```
Application
→ SBOM
→ Components / Versions / Dependencies
```

## Vue globale

```
Attack Surface Management
│
├─ EASM
│  → exposition externe / Internet
│
├─ IASM
│  → exposition interne
│
├─ CAASM
│  → visibilité et corrélation des cyber-assets
│
└─ Software Supply Chain
   → dependencies / open source / third-party code
```


La distinction utile à retenir est donc :

```
EASM
→ What can attackers see from outside?

IASM
→ What can attackers reach inside?

CAASM
→ What cyber-assets do we actually have and how are they covered?

SCA / SBOM
→ What third-party components are inside our software?
```
