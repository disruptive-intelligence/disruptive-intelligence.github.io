---
title: Solutions de gestion des actifs — Asset Management
source: Cyber/10 Outils & solutions/Solutions de sécurité/Solutions de sécurité.md
note: Solutions de sécurité
up:
- - Solutions de sécurité
  - index.md
---

## Asset Management

- Une solution de gestion des actifs permet de **suivre, maintenir et gérer le cycle de vie des actifs IT** présents dans l’organisation.
- Elle aide notamment à connaître :
    - quels équipements existent ;
    - où ils se trouvent ;
    - leur état ;
    - leur version ;
    - s’ils doivent être maintenus, remplacés ou retirés.

```
Asset
→ Inventory
→ Monitor
→ Maintain
→ Retire
```

## Types d’actifs gérés

- Les principaux types d’actifs IT sont :
    1. **Software**
    2. **Hardware**
    3. **Mobile Devices**
    4. **Cloud Assets**

```
ITAM
├─ Software
├─ Hardware
├─ Mobile
└─ Cloud
```

## Importance pour la sécurité

- Plus le nombre d’équipements augmente, plus il devient difficile de savoir :
    - quels systèmes sont présents ;
    - quelles versions ils utilisent ;
    - lesquels sont obsolètes ;
    - lesquels nécessitent une mise à jour ;
    - lesquels ne devraient plus être connectés au réseau.
- Un outil d’Asset Management permet donc d’identifier rapidement :

```
Asset inconnu
Asset obsolète
Software vulnérable
Firmware ancien
Équipement non maintenu
```

→ améliore la visibilité et réduit les oublis.
## Asset Management & Vulnerability / Patch Management

- Exemple :

```
Firewall vulnérable
→ Asset Management identifie le modèle/version
→ mise à jour de sécurité disponible
→ équipe sécurité peut agir rapidement
```

- L’outil d’Asset Management ne réalise pas forcément lui-même le patching ; il fournit surtout **l’inventaire, la visibilité et l’état des actifs**, puis peut s’intégrer avec des outils de patch/vulnerability management.

```
Asset Management → "Qu'est-ce que j'ai ?"
Vulnerability Management → "Qu'est-ce qui est vulnérable ?"
Patch Management → "Qu'est-ce que je dois mettre à jour ?"
```

## Cycle de vie d’un actif

- Complément important pour bien comprendre l’ITAM :

```
Acquire
→ Deploy
→ Maintain
→ Monitor
→ Retire / Dispose
```

- Le retrait d’un actif doit aussi être contrôlé pour éviter de laisser :
    - données sensibles ;
    - credentials ;
    - configurations ;
    - équipements encore accessibles.
