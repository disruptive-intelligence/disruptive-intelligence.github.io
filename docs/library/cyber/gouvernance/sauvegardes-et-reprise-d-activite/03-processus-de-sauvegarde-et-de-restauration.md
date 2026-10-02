---
title: Processus de Sauvegarde et de Restauration
source: Cyber/08 Gouvernance & résilience/Résilience/Sauvegardes et reprise d'activité.md
note: Sauvegardes et reprise d'activité
up:
- - Sauvegardes et reprise d'activité
  - index.md
---

- Les processus de **Backup** et **Restore** servent à limiter l’impact d’une perte de données et à assurer la continuité d’activité.

```
Backup  → créer une copie exploitable
Restore → récupérer les données à partir de cette copie
```

## Processus de sauvegarde — Backup Process
### 1. Spécifier les données

- Identifier les données à protéger.
- Prioriser notamment :
    - données métier critiques ;
    - bases de données ;
    - configurations ;
    - fichiers utilisateurs importants ;
    - systèmes nécessaires au fonctionnement de l’entreprise.

```
Inventory / Criticality
→ What must be backed up?
```

### 2. Choisir le type de sauvegarde

- Selon les besoins :
	- **Full** ;
	- **Incremental** ;
	- **Differential** ;
	- **Mirror**.
- Le choix dépend notamment de :
	- volume de données ;
	- fréquence des changements ;
	- capacité de stockage ;
	- temps disponible pour le backup ;
	- temps attendu pour la restauration.

```
Backup Type
→ impacte Storage + Backup Time + Restore Time
```

### 3. Planifier les sauvegardes

- Les sauvegardes sont généralement automatisées selon un **schedule**.
- Elles peuvent être exécutées pendant des périodes de faible activité afin de limiter leur impact sur :
    - CPU ;
    - stockage ;
    - bande passante ;
    - applications métier.

> Pour les systèmes critiques, la fréquence doit surtout être définie selon le **RPO**, pas uniquement selon les périodes de faible activité.

```
RPO faible
→ sauvegardes plus fréquentes
```

### 4. Effectuer la sauvegarde

- Le processus est généralement réalisé automatiquement par :
    - logiciel de backup ;
    - appliance ;
    - service cloud ;
    - plateforme centralisée.
- À contrôler après exécution :
	- statut du job ;
	- erreurs ;
	- quantité de données sauvegardées ;
	- durée ;
	- destination ;
	- intégrité du backup.

```
Backup Job
→ Success / Failed
→ Logs + Monitoring
```


> Un job marqué `Successful` ne garantit pas que les données pourront réellement être restaurées.
## Processus de restauration — Restore Process

- Lorsqu’une donnée est supprimée, corrompue ou indisponible, une sauvegarde peut être utilisée pour la récupérer.

```
Data Loss
→ Select Backup
→ Restore
→ Validate
```

### 1. Choisir le point de restauration

- Déterminer **quel backup utiliser**.
- Le plus récent n’est pas automatiquement le meilleur.
- Exemple :

```
Ransomware détecté vendredi
Compromission commencée mercredi

Backup jeudi → potentiellement compromis
Backup mardi → peut être préférable
```

- Il faut donc choisir un **known-good restore point** : un point connu comme sain.
### 2. Choisir l’emplacement de restauration

- Deux possibilités principales :
	- Original Location :Utilisé lorsque l’environnement original est toujours considéré comme fiable.
	- Alternate Location : backup → nouvelle machine / environnement isolé. Utile notamment :
		- après compromission ;
		- pour tester une restauration ;
		- pour analyser des données ;
		- lorsque le système original est détruit.
### 3. Effectuer la restauration

- La solution de backup récupère les données depuis le support choisi puis les replace à l’emplacement défini.
- Selon le type de backup :

```
Full Restore
→ Full

Incremental Restore
→ Full + tous les Incrementals nécessaires

Differential Restore
→ Full + dernier Differential
```

### Validation après restauration

- Une restauration ne doit pas s’arrêter au message `Restore completed`.
- Il faut vérifier :
	- intégrité des fichiers ;
	- fonctionnement des applications ;
	- cohérence des bases de données ;
	- permissions ;
	- services ;
	- données attendues ;
	- absence de corruption.

```
Restore
→ Validate
→ Functional Test
→ Return to Production
```

### Tests de restauration

- Les processus doivent être **régulièrement testés**.
- Objectifs :
	- vérifier que les backups sont utilisables ;
	- entraîner les équipes ;
	- mesurer la durée réelle de restauration ;
	- identifier les dépendances oubliées ;
	- vérifier que le RTO peut être respecté.

```
Backup Test
→ Can we restore?

Recovery Test
→ Can we restore correctly and fast enough?
```

### RPO / RTO

- Deux métriques directement liées au processus :

|Concept|Question|
|---|---|
|**RPO — Recovery Point Objective**|Jusqu’à combien de données peut-on perdre ?|
|**RTO — Recovery Time Objective**|Combien de temps peut-on rester indisponible ?|

- Exemple :

```
RPO = 1h
→ au maximum 1h de données perdues

RTO = 4h
→ service restauré en moins de 4h
```
