---
title: Gestion des MAJ et des correctifs
source: IT/02_Windows/HTB_Windows System Sécurity.md
note: HTB — Windows System Security
up:
- - HTB — Windows System Security
  - index.md
---

- Le **Patch Management** consiste à identifier, tester, déployer et vérifier les correctifs destinés à :
    - vulnérabilités ;
    - bugs ;
    - problèmes de stabilité ;
    - composants obsolètes.
- Sous Windows, **Windows Update** permet de récupérer et installer les correctifs Microsoft.

```
Vulnerability / Bug
→ Patch available
→ Test
→ Deploy
→ Verify
```

- Activer les mises à jour automatiques est utile, mais ne suffit pas toujours en entreprise : un correctif peut avoir un impact sur une application ou un service métier.
## Gestion des MAJ dans les grandes organisations

- La gestion des mises à jour et des correctifs est généralement effectuée à l'aide d'une approche centralisée.
- Une gestion correcte des correctifs suit généralement :

```
Inventory
→ Identify missing patches
→ Prioritize
→ Test
→ Approve
→ Deploy
→ Monitor
→ Report
```

Objectifs :

- réduire la fenêtre d’exposition aux vulnérabilités ;
- maintenir la compatibilité ;
- éviter qu’un patch défectueux perturbe la production ;
- vérifier que les systèmes sont réellement à jour.
### Gestion centralisée

- Dans une grande organisation, les correctifs sont généralement gérés depuis une plateforme centrale plutôt que machine par machine.
- Ces solutions garantissent que tous les systèmes reçoivent les dernières mises à jour et les derniers correctifs.
- **WSUS — Windows Server Update Services** ;
- **MECM — Microsoft Endpoint Configuration Manager**.

```
Microsoft Updates
       ↓
Patch Management Platform
       ↓
Workstations / Servers
```

Cela permet notamment :

- sélectionner les updates ;
- approuver/refuser certains correctifs ;
- définir des groupes de machines ;
- planifier les déploiements ;
- suivre l’état de conformité.
### Test des correctifs

- Il est très important que chaque correctif soit correctement testé. Cela permet de vérifier la compatibilité d'un correctif avec les applications, d'identifier les bogues éventuels et d'évaluer les performances globales.

Avant un déploiement massif, vérifier :

- compatibilité applicative ;
- stabilité ;
- performances ;
- impact sur les services ;
- nécessité d’un reboot.

Une approche classique consiste à utiliser plusieurs **deployment rings** :

```
Test / Pilot Group
       ↓
Small Production Group
       ↓
General Deployment
```

→ limite l’impact si un patch provoque un problème.
### Distribution

- Une fois validés, les correctifs sont déployés selon une fenêtre définie.
- Ce processus implique généralement de choisir un moment qui aura un impact minimal sur le flux de travail de l'organisation.

```
Approved Patch
→ Maintenance Window
→ Automated Deployment
```

Il faut notamment prendre en compte :

- horaires d’activité ;
- redémarrages ;
- disponibilité des services ;
- criticité des systèmes.
### Monitoring & Reporting
Après le déploiement, vérifier :

- machines patchées ;
- machines en échec ;
- update installée ;
- reboot nécessaire ;
- systèmes hors ligne ;
- taux de conformité.

```
Deploy
→ Success / Failure
→ Remediation
→ Compliance Report
```

> `Patch deployed` ≠ `Patch successfully installed everywhere`.

### Correctifs d’urgence
Certaines vulnérabilités nécessitent un traitement beaucoup plus rapide :

- exploitation active ;
- vulnérabilité critique ;
- système exposé à Internet ;
- exploit public ;
- asset critique.

```
Critical + Exploited + Internet-facing
→ Emergency Patching
```

Le processus peut être accéléré :

```
Rapid Test
→ Approval
→ Emergency Deployment
→ Verification
```

-> Tout en conservant suffisamment de tests pour éviter une interruption majeure.
