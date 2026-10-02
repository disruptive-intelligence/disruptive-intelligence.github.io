---
title: Sécurité des sauvegardes & Disaster Recovery
source: Cyber/08 Gouvernance & résilience/Résilience/Sauvegardes et reprise d'activité.md
note: Sauvegardes et reprise d'activité
up:
- - Sauvegardes et reprise d'activité
  - index.md
---

## Sécurité des sauvegardes — Backup Security

- Les sauvegardes doivent être protégées au même titre que les données de production.
- Un attaquant qui compromet les backups peut :
    - voler les données ;
    - supprimer les copies ;
    - les chiffrer ;
    - empêcher toute restauration.

```
Production compromise
→ Backup compromise
→ Recovery impossible
```

### Access Control

- Limiter l’accès aux sauvegardes aux seuls utilisateurs/services autorisés.
- Utiliser :
    - comptes dédiés ;
    - Least Privilege ;
    - MFA / 2FA ;
    - séparation des rôles.

```
User/Admin standard
        X
Backup Administration

Backup Admin
→ accès dédié + MFA
```

→ idéalement, la compromission d’un compte administrateur de production ne doit pas automatiquement donner accès aux backups.
### Encryption

- Les sauvegardes doivent être chiffrées :

```
In Transit
→ lors du transfert

At Rest
→ lorsqu'elles sont stockées
```

- Objectif :
	- protéger la confidentialité des données ;
	- empêcher leur lecture en cas de vol du support ou d’accès non autorisé.

> Il faut également protéger les **clés de chiffrement** : perdre la clé peut rendre une sauvegarde parfaitement intacte mais inutilisable.
### Integrity Checks

- Vérifier régulièrement que les backups :
    - ne sont pas corrompus ;
    - n’ont pas été modifiés ;
    - peuvent être restaurés correctement.

```
Backup
→ Integrity Check
→ Restore Test
```

- Un hash/checksum peut aider à détecter certaines altérations, mais le **test de restauration** reste essentiel.
### Physical Security

- Les supports physiques doivent être protégés contre :
	- vol ;
	- incendie ;
	- dégâts matériels ;
	- accès non autorisé.
- Exemples :

```
External HDD
Tape / LTO
Offline Media
```

→ stockage dans des zones contrôlées, coffres ou sites sécurisés selon la criticité.
### Copies multiples — règle 3-2-1

- Principe classique :

```
3 → copies des données au total
2 → types de supports différents
1 → copie offsite
```


> ⚠️ Le cours mélange ici **offsite** et **offline**. La règle 3-2-1 classique demande une copie **hors site** ; une copie offline/immutable correspond à une protection supplémentaire, souvent exprimée avec la règle **3-2-1-1-0**.

Pour renforcer la résistance au ransomware :

```
Offline / Air-Gapped / Immutable Backup
→ difficile à modifier ou supprimer
```

### Secure Erase

- Lorsqu’un support arrive en fin de vie :
	- supprimer les données de manière irréversible ;
	- éviter qu’elles puissent être récupérées par un tiers.
- Selon le support :
	- secure erase ;
	- cryptographic erase ;
	- destruction physique.

```
Backup Media EOL
→ Secure Erase / Destroy
→ Dispose
```

## Disaster Recovery — Reprise après sinistre

- Le **Disaster Recovery (DR)** désigne l’ensemble des moyens permettant de **restaurer les systèmes et reprendre les services** après un incident majeur.
- Scénarios :
	- cyberattaque ;
	- ransomware ;
	- panne matérielle majeure ;
	- destruction d’un datacenter ;
	- catastrophe naturelle ;
	- corruption massive.

```
Disaster
→ Recover Data
→ Restore Systems
→ Restore Services
→ Resume Business
```


> Le **Data Recovery** concerne principalement la récupération des données, tandis que le **Disaster Recovery** est plus large : données + systèmes + infrastructure + procédures + ordre de reprise.
### 1. Planification d'urgence - Emergency Planning

- Préparer à l’avance un **Disaster Recovery Plan / DRP**.
- Définir :
    - responsabilités ;
    - procédures ;
    - ordre de restauration ;
    - contacts ;
    - ressources nécessaires.

```
Incident majeur
→ Who does what?
→ What gets restored first?
→ How?
```

- L’objectif est d’éviter d’improviser pendant la crise.
### 2. Data Backup

- Effectuer des sauvegardes régulières.
- Les stocker de manière sécurisée et indépendante.
- Vérifier régulièrement leur fonctionnement.

```
Backup
→ Protect
→ Monitor
→ Test
```

- La fréquence des backups doit être cohérente avec le **RPO** attendu.
### 3. Data Restoration

- En cas de perte :
	1. identifier le bon restore point ;
	2. vérifier que le backup est sain ;
	3. restaurer les données ;
	4. valider leur intégrité.

```
Known-Good Backup
→ Restore
→ Validate
```

- Après une cyberattaque, restaurer simplement le backup le plus récent peut être dangereux s’il contient déjà des éléments compromis.
### 4. System Reinstallation / Recovery

- Un sinistre peut nécessiter plus qu’une restauration de fichiers :
	- réinstaller OS et applications ;
	- reconstruire des serveurs ;
	- reconfigurer le réseau ;
	- restaurer les services ;
	- appliquer patches/hardening ;
	- effectuer des tests avant remise en production.

```
Clean System
→ Restore Configuration
→ Restore Data
→ Test
→ Production
```

- Dans certains incidents, reconstruire un système sain est préférable à réutiliser directement un système compromis.
### 5. Test et amélioration

- Le DR Plan doit être régulièrement testé.
- Objectifs :
	- vérifier que les procédures fonctionnent ;
	- mesurer les temps de récupération ;
	- identifier les dépendances oubliées ;
	- former les équipes ;
	- corriger les faiblesses.
