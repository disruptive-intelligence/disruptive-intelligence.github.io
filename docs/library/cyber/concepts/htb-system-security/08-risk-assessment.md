---
title: Risk Assessment
source: Cyber/99_Concepts/HTB_System Security.md
note: HTB — System Security
up:
- - HTB — System Security
  - index.md
---

- La sécurité physique commence par une **évaluation des risques**.
- Il faut identifier :
    - les actifs ;
    - les activités critiques ;
    - les menaces ;
    - les vulnérabilités ;
    - les mesures prioritaires à mettre en place.

```
Assets
+ Threats
+ Vulnerabilities
→ Risk Assessment
→ Priorisation des protections
```

## Sécurité des installations

- Concerne notamment :
	- bâtiments ;
	- bureaux ;
	- entrepôts ;
	- usines.
- L’objectif est de protéger les **personnes, actifs et informations** présents sur le site.
### Sécurité environnementale

- Utiliser des barrières physiques pour limiter les accès non autorisés :
	- clôtures ;
	- barrières ;
	- checkpoints ;
	- points d’entrée/sortie contrôlés ;
	- éclairage ;
	- agents de sécurité ;
	- caméras.

```
Perimeter
→ Detect
→ Deter
→ Restrict Access
```

### Gestion des visiteurs

- Les visiteurs doivent être contrôlés via :
	- vérification d’identité ;
	- enregistrement ;
	- badges/cartes temporaires ;
	- accompagnement par un employé.

```
Visitor
→ Identify
→ Register
→ Temporary Access
→ Escort si nécessaire
```

### Éclairage & Security Lighting

- Un bon éclairage permet :
    - d’identifier plus facilement les menaces ;
    - d’améliorer les images des caméras ;
    - de faciliter la surveillance ;
    - de dissuader les intrusions.
### Personnel de sécurité

- Le personnel de sécurité doit :
    - surveiller les installations ;
    - appliquer les procédures ;
    - réagir rapidement aux incidents ;
    - recevoir une formation régulière.
### Visiteurs & médias portables

- Contrôler également les équipements amenés dans les locaux :
    - clés USB ;
    - disques externes ;
    - autres supports portables.
- Ils peuvent être vérifiés afin de détecter des menaces potentielles.
## Préparation aux urgences

- Prévoir :
	- plans d’évacuation ;
	- procédures de gestion de crise ;
	- systèmes de communication ;
	- procédures adaptées aux incendies, catastrophes ou attaques.
- Ces plans doivent être :

```
Create
→ Review regularly
→ Train personnel
→ Update
```

## Sécurité des Data Centers

- Les centres de données hébergent des ressources critiques :
	- données ;
	- serveurs ;
	- systèmes ;
	- infrastructure réseau.
### Contrôle d’accès

- L’accès doit être limité au personnel autorisé.
- Mécanismes possibles :
    - systèmes de contrôle d’accès ;
    - protections physiques ;
    - biométrie.
### Firewall & Network Security

- Le trafic du datacenter doit être surveillé et protégé par :
    - firewalls ;
    - équipements de sécurité réseau.
- Objectifs :

```
Unauthorized Access → Prevent
Malicious Traffic   → Detect / Block
```

### Physical Security

- Mesures possibles :
	- CCTV ;
	- détecteurs de mouvement ;
	- alarmes ;
	- systèmes de surveillance ;
	- personnel de sécurité.

→ permettent de détecter ou empêcher :

- accès non autorisé ;
- vol ;
- dommages matériels.
### Incendie & contrôle climatique

- Un datacenter doit disposer de :
	- détection de fumée ;
	- systèmes anti-incendie ;
	- extinction incendie ;
	- contrôle de la température ;
	- contrôle de l’humidité.

→ protège le matériel et les données contre les risques environnementaux.
### UPS / ASI & sauvegardes

- Les **UPS / ASI** maintiennent temporairement l’alimentation lors :
    - d’une panne ;
    - d’une perturbation électrique.
- Les systèmes de sauvegarde contribuent à assurer la continuité des données et services.

```
Power Failure
→ UPS
→ service maintenu temporairement
```

### Monitoring & Logging

- Surveiller :
    - systèmes ;
    - trafic réseau ;
    - événements de sécurité.
- Journaliser les événements permet :
    - détection rapide ;
    - investigation ;
    - traçabilité ;
    - troubleshooting.
### Redondance

- Utiliser :
    - datacenters redondants ;
    - systèmes de secours ;
    - infrastructures alternatives.
- Objectif :

```
Primary Data Center DOWN
→ Secondary / Backup Infrastructure
→ Services continue
```

### Audits & Compliance

- Réaliser régulièrement :
    - audits de sécurité ;
    - révision des policies ;
    - identification des vulnérabilités ;
    - vérification de conformité aux standards.
### Personnel & Least Privilege

- Former régulièrement le personnel.
- Adapter les autorisations pour que chacun possède uniquement les accès nécessaires.

```
Personnel
→ Awareness
→ Authorized Access Only
→ Least Privilege
```

## Sécurité des postes de travail et du matériel

- Les postes de travail et équipements doivent être protégés contre l’accès physique non autorisé.
- Les zones sensibles peuvent utiliser :
    - portes sécurisées ;
    - casiers ;
    - barrières ;
    - contrôles d’accès.
- Objectifs :
	- protéger les données sensibles ;
	- réduire les risques de fuite/perte ;
	- assurer la continuité d’activité ;
	- protéger les équipements volés/perdus ;
	- répondre aux exigences de conformité.
