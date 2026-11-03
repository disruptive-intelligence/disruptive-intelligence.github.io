---
title: Chapitre 10 — Le cycle mensuel dans WSUS et son entretien
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - ../index.md
- - Partie IV — WSUS
  - index.md
---

> 🧱 **Les bases**
>
> - Un **groupe d'ordinateurs** WSUS rassemble des machines qui reçoivent les mêmes approbations. Il existe toujours *Tous les ordinateurs* et *Ordinateurs non attribués* (les nouvelles machines sans groupe).
> - Une **échéance** (*deadline*) est une date après laquelle l'installation est forcée, même si l'utilisateur repousse.

## 10.1 Les approbations

| Action | Effet |
|---|---|
| **Approuvée pour installation** | les machines du groupe qui en ont besoin l'installent (selon leur stratégie AUOptions) |
| avec **échéance** | installation **forcée** à la date, puis redémarrage forcé selon la stratégie |
| **Approuvée pour suppression** | désinstallation, si la mise à jour le permet (rarement pour les cumulatives combinées) |
| **Non approuvée** | aucune action pour ce groupe |
| **Refusée** (*declined*) | masquée partout, **plus évaluée** par les clients ; **ne désinstalle rien** |

Les approbations s'**héritent** des groupes parents vers les groupes enfants. Approuver sur *Tous les ordinateurs* revient à approuver pour **tout le parc** : c'est l'erreur la plus coûteuse qu'on puisse faire dans la console.

```powershell
# Les mises à jour de sécurité non approuvées, nécessaires à au moins une machine
Get-WsusUpdate -Classification Security -Approval Unapproved -Status FailedOrNeeded

# Approuver une mise à jour pour le groupe pilote
Get-WsusUpdate -UpdateId '<GUID>' | Approve-WsusUpdate -Action Install -TargetGroupName 'Postes-Pilote'

# Refuser une mise à jour
Get-WsusUpdate -UpdateId '<GUID>' | Deny-WsusUpdate
```


**Règles d'approbation automatique.** Une règle associe des classifications et des produits à des groupes, avec une échéance optionnelle. Elles sont **adaptées aux définitions Defender** (plusieurs fois par jour, risque faible, sécurité immédiate). Pour les cumulatives, elles suppriment l'étape de décision : à n'utiliser que pour le **groupe pilote**, et en sachant qu'une règle s'applique aussi aux **OOB** et aux **préversions** si leur classification correspond.

> ⚠️ **Piège** — L'option *Approuver automatiquement les nouvelles révisions des mises à jour déjà approuvées* est généralement souhaitable (correction de métadonnées). L'option qui approuve **automatiquement toute une classification pour Tous les ordinateurs**, elle, ne l'est presque jamais.

## 10.2 Les états d'une machine pour une mise à jour

| État | Sens |
|---|---|
| Inconnu (*Unknown*) | la machine n'a pas encore rapporté pour cette mise à jour |
| Non applicable | ne la concerne pas (autre version, déjà plus récent…) |
| Nécessaire (*Not installed*) | applicable, pas encore installée |
| Téléchargée | fichiers sur la machine, pas installée |
| Installée, redémarrage en attente | installée mais **pas encore active** |
| Installée | OK |
| Échec | l'installation a échoué (code dans l'événement 20 du poste) |

> ⚠️ **Piège** — « Non applicable » n'est pas « protégé » : une machine en version hors support ne trouve **aucune** cumulative applicable (Ch.3). Et un état « Inconnu » qui dure signifie souvent que la machine **ne contacte plus WSUS**.

## 10.3 Remplacement, expiration, révision

- **Remplacée** (*superseded*) : à **refuser** quand plus aucune machine n'en a besoin. Garder des centaines de cumulatives remplacées non refusées **ralentit fortement** les recherches des clients (chaque client évalue toutes les mises à jour non refusées).
- **Expirée** : retirée par Microsoft. À refuser.
- **Révision** : nouvelle version des métadonnées d'une même mise à jour ; les anciennes révisions sont supprimées par le nettoyage.

L'assistant de nettoyage refuse les remplacées **avec prudence** : seulement celles qui sont remplacées par une mise à jour approuvée, non approuvées depuis au moins 30 jours, et qu'aucun client ne déclare nécessaires.

## 10.4 Le rapport de conformité

```powershell
# Vue d'ensemble : machines avec des mises à jour en échec ou nécessaires
Get-WsusComputer -All | Select-Object FullDomainName, OSDescription, LastReportedStatusTime |
    Sort-Object LastReportedStatusTime

# Machines qui n'ont pas rapporté depuis 14 jours (fantômes ou postes hors réseau)
Get-WsusComputer -All | Where-Object { $_.LastReportedStatusTime -lt (Get-Date).AddDays(-14) } |
    Select-Object FullDomainName, LastReportedStatusTime
```


Les rapports intégrés de la console nécessitent l'installation de *Microsoft Report Viewer* (composant ancien) ; beaucoup d'équipes préfèrent PowerShell ou des requêtes SQL sur les vues de SUSDB. Dans tous les cas, un rapport WSUS mesure **ce que les clients ont déclaré**, à la date de leur dernier rapport (Ch.12).

## 10.5 La maintenance

Un WSUS non entretenu se dégrade : recherches clients de plus en plus longues, console qui plante, pool IIS qui s'arrête → erreur HTTP 503 côté client (**0x80244022**). Chaque mois (après le déploiement en production, à J+22 dans le cycle d'ORIAN) :

1. **Refuser** les mises à jour remplacées et expirées.
2. Lancer l'**assistant de nettoyage** (console : *Options > Assistant de nettoyage du serveur*) ou son équivalent PowerShell.
3. **Réindexer SUSDB** avec le script fourni par Microsoft (*Reindex the WSUS database*).
4. **Surveiller** l'espace disque de WsusContent et la santé du pool IIS.

```powershell
# Nettoyage complet (peut être long la première fois : des heures sur un WSUS jamais nettoyé)
Invoke-WsusServerCleanup -DeclineSupersededUpdates -DeclineExpiredUpdates `
    -CleanupObsoleteUpdates -CleanupUnneededContentFiles -CompressUpdates -CleanupObsoleteComputers
```


```cmd
:: Réindexation de SUSDB sur WID (Windows Server 2012 et ultérieurs)
sqlcmd -S np:\\.\pipe\MICROSOFT##WID\tsql\query -i C:\Scripts\WsusDBMaintenance.sql
```


**Réglages IIS du pool WsusPool** couramment recommandés par la documentation Microsoft de maintenance (à adapter) :

| Paramètre | Valeur par défaut | Valeur courante |
|---|---|---|
| *Queue Length* | 1000 | 2000 |
| *Idle Time-out* | 20 min | 0 |
| *Ping Enabled* | True | False |
| *Private Memory Limit* | ~1,8 Go | 0 (illimité) ou nettement augmenté (4 à 8 Go) |
| *Regular Time Interval* (recyclage) | 1740 min | 0 |

## 10.6 Les pannes classiques

| Symptôme | Cause fréquente | Action |
|---|---|---|
| Clients en **0x80244022** (503) | pool **WsusPool arrêté** (mémoire dépassée) | redémarrer le pool, puis corriger la cause (réglages IIS, nettoyage) |
| Console qui expire ou plante | SUSDB jamais réindexée, trop de mises à jour non refusées | nettoyage + réindexation ; *Réinitialiser le nœud du serveur* dans la console |
| Synchronisation en échec | proxy, certificat, accès à Microsoft Update, base saturée | journaux de synchronisation (console) et `C:\Program Files\Update Services\LogFiles\SoftwareDistribution.log` sur le serveur |
| Une machine « clignote » entre deux noms | **SusClientId dupliqué** (clone) | §9.4 |
| Machines qui ne rapportent plus | GPO non appliquée, DNS, pare-feu, agent cassé | `gpresult`, `Test-NetConnection -Port 8530`, journaux client |
| Fichiers manquants après restauration | WsusContent incomplet | `wsusutil reset` (revérifie et retélécharge) |
| Disque plein | fichiers express, produits/langues en trop, absence de nettoyage | revoir la configuration, nettoyer |

> 🧵 **Fil rouge — Lundi 16 mars 2026**
>
> Le lendemain d'une grosse synchronisation, les postes de Nantes remontent 0x80244022. Inès trouve le pool WsusPool arrêté sur le réplica : limite de mémoire atteinte. Karim reconnaît que le nettoyage mensuel sautait « quand on n'avait pas le temps » depuis un an : 2 300 cumulatives remplacées non refusées. Inès lance le nettoyage (six heures la première fois), réindexe SUSDB, applique les réglages IIS recommandés et inscrit la maintenance **dans le cycle mensuel**, à date fixe (J+22), avec une case dans la checklist. La recherche des clients passe de 9 minutes à 40 secondes.

> 📌 **À retenir**
>
> - Approuver **par groupe**, jamais sur *Tous les ordinateurs* par réflexe ; refuser ne désinstalle rien.
> - États à surveiller : *Échec*, *Redémarrage en attente*, *Inconnu* qui dure.
> - Chaque mois : refuser remplacées/expirées, nettoyage, réindexation SUSDB, surveillance du pool IIS et du disque.

---
