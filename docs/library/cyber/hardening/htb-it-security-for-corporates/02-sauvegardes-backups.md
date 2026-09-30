---
title: Sauvegardes — Backups
source: Cyber/99_Concepts/HTB_IT Security for Corporates.md
note: HTB — IT Security for Corporates
up:
- - HTB — IT Security for Corporates
  - index.md
---

- Les sauvegardes **n'empêchent pas** une attaque ransomware, mais constituent une **dernière ligne de défense / mécanisme de recovery**.
- Une sauvegarde inutilisable ou elle-même compromise peut mettre en danger la continuité de l'entreprise.

```
Ransomware → prévention/détection : EDR, hardening, segmentation...
Backup     → récupération après compromission
```

### Règle 3-2-1

- 3 copies > 2 supports différents > 1 une sauvegarde hors site
#### 3 copies

- Conserver **3 copies des données au total** :
    - données de production ;
    - Backup 1 ;
    - Backup 2.
#### 2 supports différents

- La règle classique demande de conserver les copies sur **au moins 2 types de supports / systèmes de stockage différents**.
- Exemples :

```
Disk + Tape
NAS + Object Storage
Local Storage + Cloud Backup
```

#### 1 copie hors site — Offsite

- Au moins une sauvegarde doit être située **hors du site principal**.
- Protège contre :
    - incendie ;
    - inondation ;
    - vol ;
    - destruction du datacenter.

```
Site principal détruit
→ Offsite Backup toujours disponible
```

### Règle 3-2-1-1-0
Extension de la règle 3-2-1 pour les ressources critiques.
#### +1 copie Offline

- Une copie doit être **isolée de l'infrastructure de production** afin qu'un attaquant ayant compromis le réseau ne puisse pas la supprimer/chiffrer.

```
Production Network
      X
Offline Backup
```

- Aujourd'hui, on utilise aussi des sauvegardes **air-gapped ou immutable**.

```
Offline / Air-Gapped / Immutable
→ difficile à modifier ou supprimer par l'attaquant
```

#### +0 erreur

- Les sauvegardes doivent être **vérifiées et restaurables sans erreur**.
- Il ne suffit pas qu'un job affiche `Backup successful`.

→ effectuer régulièrement des **restore tests** et vérifier l'intégrité des données restaurées.
### Durée de conservation — Retention

- Pouvoir restaurer des données datant d'au moins **30 jours**, afin d'éviter que toutes les sauvegardes disponibles contiennent déjà les traces d'une compromission ancienne.

```
Attaquant présent depuis plusieurs semaines
→ backups récents potentiellement déjà compromis
→ besoin de points de restauration plus anciens
```

> Les `30 jours` ne sont pas une règle universelle : la rétention doit être définie selon le risque, les contraintes légales, la criticité et les besoins métier.
### Tests de restauration

- Suivre/documenter les tests de restauration.
- Le cours recommande que **chaque serveur soit restauré au moins une fois par an**.
- Pour les systèmes critiques, des tests plus fréquents sont préférables.
- À vérifier :
	- données lisibles ;
	- fichiers non corrompus ;
	- applications fonctionnelles ;
	- procédure de restauration maîtrisée ;
	- temps nécessaire à la restauration.
### RPO (PDMA) / RTO (DMIA)

- Complément important pour la stratégie de backup :

| Concept                                                                             | Signification                                           |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **RPO — Recovery Point Objective** / PDMA - Perte de données maximale admissible    | Quantité maximale de données que l'on accepte de perdre |
| **RTO — Recovery Time Objective** / DMIA - durée maximale d'interruption admissible | Temps maximal acceptable pour restaurer le service      |

- Exemple :

```
RPO = 4h
→ backups suffisamment fréquents pour perdre ≤ 4h de données

RTO = 2h
→ service doit être restauré en ≤ 2h
```

### Protection des backups

- Pour éviter qu'un ransomware compromette aussi les sauvegardes :
	- comptes de backup dédiés ;
	- MFA sur les consoles d'administration ;
	- droits minimums ;
	- sauvegardes immutables/offline ;
	- séparation entre infrastructure de production et backup ;
	- alertes sur suppression/modification anormale des sauvegardes.

```
Attaquant Domain Admin
≠ doit automatiquement devenir Backup Admin
```


## Prévention contre l’hameçonnage — Phishing Prevention

- Le **phishing** reste un vecteur majeur d’**Initial Access**, au même titre que l’exploitation de vulnérabilités sur des services exposés à Internet.
- La prévention repose sur plusieurs couches : filtrage technique + procédure d’analyse + sensibilisation utilisateur.
### Antispam & Email Security

- Tous les emails entrants doivent passer par un **filtre antispam / Email Security Gateway**.
- Les pièces jointes doivent être analysées par l’**AV**.
- La configuration doit être :
    - maintenue à jour ;
    - adaptée aux nouvelles menaces ;
    - régulièrement revue.

```
Email entrant
→ Antispam
→ AV / analyse pièce jointe
→ Allow / Quarantine / Block
```


- **Complément utile :**
	- analyser également les **URLs** contenues dans les emails ;
	- utiliser SPF / DKIM / DMARC contre certaines formes de spoofing ;
	- sandboxer les pièces jointes suspectes si disponible.
### Procédure d’analyse

- Un employé ayant un doute sur un email doit savoir **à qui le signaler**.
- L’organisation doit prévoir un canal simple :
    - bouton `Report Phishing` ;
    - adresse dédiée ;
    - ticket SOC / IT.

```
Email suspect
→ utilisateur signale
→ SOC / IT analyse
→ verdict + actions
```

- L’objectif est d’éviter que l’utilisateur doive décider seul si l’email est sûr.
### Exercices de phishing

- Réaliser des **phishing simulations** permet de vérifier si les employés savent :
    - reconnaître un email suspect ;
    - ne pas cliquer ;
    - signaler correctement l’événement.
- Ces exercices doivent surtout servir à **mesurer et améliorer la préparation**, pas simplement à piéger les utilisateurs.
- Indicateurs possibles :

```
Click Rate
Credential Submission Rate
Report Rate
```

→ le **Report Rate** est particulièrement intéressant pour mesurer la capacité des utilisateurs à remonter rapidement une menace.
