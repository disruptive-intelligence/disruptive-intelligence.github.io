---
title: Inventaire
source: Cyber/99_Concepts/HTB_IT Security for Corporates.md
note: HTB — IT Security for Corporates
up:
- - HTB — IT Security for Corporates
  - index.md
---

- Pour protéger une infrastructure, il faut savoir :
    - quels équipements sont connectés ;
    - quels logiciels sont utilisés ;
    - qui y a accès ;
    - quelles mesures de sécurité sont appliquées.
## Contenu minimal de l’inventaire

- matériel de chaque PdT/server ;
- logiciels installés avec leur **version exacte** ;
- date du dernier inventaire/report.
- Complément utile pour un inventaire exploitable :
	- hostname / IP / OS ;
	- propriétaire / utilisateur ;
	- localisation ;
	- criticité de l’asset ;
	- statut de support ;
	- dernier contact / dernière mise à jour.

```
Inventory → savoir ce qu'on possède
→ pouvoir patcher, surveiller et retirer ce qui est vulnérable
```

## Équipements en fin de vie - End-of-Life — EOL

- Grâce à votre inventaire, vous avez pu isoler tous les équipements (matériels et logiciels) en fin de support.
- Un matériel/logiciel **End-of-Life / End-of-Support** ne reçoit plus de correctifs de sécurité.
- Il faut donc :
    - l’identifier via l’inventaire ;
    - le remplacer ou le retirer du réseau.
- Si son maintien est indispensable :
	- effectuer une **risk acceptance** formelle par le CISO ;
	- documenter cette exception dans l’inventaire ;
	- réévaluer régulièrement le risque, notamment lors de nouvelles vulnérabilités.
- Complément pertinent :

```
EOL impossible à remplacer
→ segmentation
→ accès fortement restreints
→ monitoring renforcé
→ compensating controls
```

## Secure Boot

- Activer **Secure Boot** sur tous les équipements compatibles.
- Vérifie au démarrage que les composants chargés sont **signés et approuvés par une chaîne de confiance UEFI**.

```
Bootloader non approuvé / signature invalide
→ boot bloqué
```

→ réduit le risque de bootkits/rootkits chargés avant l’OS.

> Ce n’est pas simplement « logiciel approuvé par le fabricant » : Secure Boot repose sur des **signatures cryptographiques et clés de confiance configurées dans l’UEFI**.
## Software Policy

- Pour réduire l’**Attack Surface**, définir clairement :

```
Allowed Software
vs
Forbidden Software
```

### Allowed Software

- Fournir aux utilisateurs un catalogue de logiciels approuvés via :
    - **GPO**
    - **Microsoft Intune**
- Permet d’installer des applications sans donner de droits administrateur ni télécharger soi-même des installateurs sur Internet.

```
Catalogue approuvé
→ installation contrôlée
→ moins de téléchargements suspects
```

### Forbidden Software

- Bloquer les logiciels :
    - non approuvés par l’entreprise ;
    - vulnérables / présentant une CVE jugée critique ;
    - incompatibles avec la politique de sécurité.
- Outils possibles :
	- **AppLocker**
	- Intune
	- politiques centralisées.
- Toute tentative d’exécution d’un logiciel interdit doit idéalement :

```
Block
+
Log
+
Alert IT/SOC
```

## Security Hardening

- Définir des **hardening baselines** afin que les postes/serveurs aient une configuration sécurisée et homogène.
- Peut couvrir :
	- procédure de remise d’un poste avec checklist ;
	- audit de la configuration sécurisée ;
	- détection/alerte lorsqu’une configuration est modifiée.

```
Security Baseline
→ configuration attendue

Configuration modifiée
→ Drift / Deviation
→ détecter + corriger
```

- Outils cités :
	- **Ansible**
	- **GPO**
	- **Intune**
## Antivirus / EDR

- Déployer un **AV**, idéalement un **EDR**, sur l’ensemble du parc.
- Prioriser au minimum les systèmes critiques si le déploiement doit être progressif.

```
AV  → détecter / bloquer principalement les malwares
EDR → monitorer / détecter / investiguer / répondre
```

- Le déploiement seul ne suffit pas :
	- vérifier que les agents fonctionnent ;
	- surveiller les alertes ;
	- investiguer les détections ;
	- suivre les endpoints non protégés ou déconnectés.
