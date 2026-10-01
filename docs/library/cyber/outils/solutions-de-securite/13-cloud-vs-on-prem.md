---
title: Cloud vs On Prem
source: Cyber/10 Outils & solutions/Solutions de sécurité/Solutions de sécurité.md
note: Solutions de sécurité
up:
- - Solutions de sécurité
  - index.md
---

- Lors de la transition vers des environnements cloud, il est essentiel de traiter les vulnérabilités qui peuvent découler d'erreurs de configuration.
- Voici les principales considérations pour les vulnérabilités basées sur le cloud par rapport aux installations sur site (on-premises) :

## Ports ouverts
**On-Prem :**

- ne pas exposer de ports/services inutiles sur le LAN ou Internet.

**Cloud :**

- éviter les ports inutiles sur VM/services ;
- ne pas exposer directement RDP/SSH si une solution intermédiaire existe.

Exemple Azure :

```
Internet
   ↓
Azure Bastion
   ↓
VM

plutôt que

Internet → RDP 3389 → VM
```


## Authentication Methods
**On-Prem :**

- authentification souvent gérée localement ou via **Active Directory / Domain Controllers**.

**Cloud :**

- ressources potentiellement accessibles mondialement ;
- utiliser **MFA** pour réduire l’impact d’un password compromis.

```
Password
+
Second facteur
→ MFA
```


> Un facteur résistant au phishing est préférable quand disponible ; le SMS reste une forme de MFA mais est moins robuste.
## Conditional Access
**On-Prem :**

- contrôles souvent basés sur réseau, AD et GPO.

**Cloud :**

- **Conditional Access Policies** selon :
    - identité utilisateur ;
    - emplacement ;
    - état/conformité du device ;
    - niveau de risque.

Exemple :

```
Login admin
+
device non conforme
+
pays inhabituel
→ MFA renforcée / accès bloqué
```

## Privilege Management
**On-Prem :**

- permissions locales/AD ;
- contrôle via rôles et groupes.

**Cloud :**

- éviter les privilèges excessifs ;
- appliquer **RBAC + Least Privilege** ;
- limiter fortement les rôles à très hauts privilèges (`Global Administrator`, etc.).
