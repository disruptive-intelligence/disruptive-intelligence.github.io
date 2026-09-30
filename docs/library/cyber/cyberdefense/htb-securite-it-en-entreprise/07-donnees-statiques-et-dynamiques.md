---
title: Données Statiques et Dynamiques
source: Cyber/04_Hardening/HTB_Sécurité IT en entreprise.md
note: HTB — Sécurité IT en entreprise
up:
- - HTB — Sécurité IT en entreprise
  - index.md
---

- Pour sécuriser les données, il est utile de distinguer :
    - les **données statiques / Data at Rest** ;
    - les **données dynamiques / Data in Transit**.
- Ces deux états nécessitent des mesures de protection différentes.

```
Data at Rest
→ données stockées

Data in Transit
→ données en déplacement
```

## Données statiques — Data at Rest

- Données stockées quelque part et en attente d’utilisation.
- Exemples :
    - fichiers sur disque ;
    - données stockées sur serveur ;
    - données en base de données ;
    - sauvegardes.

```
File on Disk
→ Data at Rest
```

Une donnée reste **statique** tant qu’elle est stockée et n’est pas en cours de transmission.
## Données dynamiques — Data in Transit

- Données qui se déplacent d’un système ou emplacement à un autre.
- Exemples :
    - téléchargement d’un fichier depuis Internet ;
    - transfert depuis un file server ;
    - échange entre deux sites.

```
Server A
→ Network / Internet
→ Client B

= Data in Transit
```


- Une même donnée peut donc changer d’état :

```
File stored on Server
→ Data at Rest

Download starts
→ Data in Transit

File stored on Client
→ Data at Rest
```

### Exemple : transfert entre deux sites
![DATA](../../../assets/htb-securite-it-en-entreprise-data.png){ width="500" }
Supposons :

```
Location A
→ File Server
→ invoices.pdf

Location B
→ User Endpoint
```

Même si l’environnement dispose déjà de :

- firewall rules ;
- RBAC ;
- strong password policy ;
- 2FA ;

- le fichier doit encore être protégé **pendant son transit** entre les deux emplacements.

Le problème :

```
A
→ systèmes intermédiaires
→ Internet
→ B
```

- L’organisation ne contrôle pas nécessairement tous les systèmes traversés.

→ il faut donc transformer les données avant leur départ pour qu’elles soient illisibles par un tiers, puis les restaurer à destination.

```
Plaintext
→ Encryption
→ Transmission
→ Decryption
→ Plaintext
```

## Protection des Données Dynamiques

- Objectif : protéger les données pendant leur **transfert et leur partage**.
- Principaux besoins :
    - confidentialité ;
    - intégrité ;
    - disponibilité/accessibilité.
### Chiffrement des données — Data Encryption

- Le chiffrement est l’une des principales protections pour les données dynamiques.
- Les données sont rendues illisibles avant ou pendant leur transmission.

```
Readable Data
→ Encryption
→ Unreadable Data
→ Transmission
```

→ empêche un tiers non autorisé de comprendre les données interceptées.
### Communication sécurisée des données

- Utiliser des **canaux de communication sécurisés**.
- Ces canaux permettent :
    - transfert chiffré ;
    - authentification ;
    - vérification de l’échange.

Le cours cite notamment :

```
SSL / TLS
```


Principe : 

```
Client
→ Secure Channel
→ Server
```

### Intégration des données

- Pendant le processus d'intégration des données, nous devons nous assurer que les données sont transférées et vérifiées de manière sécurisée.

Les données peuvent transiter entre différents :

- systèmes ;
- applications ;
- services.

Les points d’intégration doivent être protégés avec :

- authentification ;
- autorisation ;
- vérification du transfert ;
- contrôle contre les accès non autorisés.

```
Application A
→ Secure Integration
→ Application B
```

### Limitation du stockage

- Ne pas conserver inutilement des données qui n’ont plus de raison d’être stockées.
- Appliquer une politique de **retention** adaptée.
- Purger régulièrement les données devenues inutiles.
- Pendant leur conservation :
    - stockage sécurisé ;
    - accès restreint.

```
Collect
→ Use
→ Retain only if needed
→ Purge
```

### Contrôle et surveillance des données

- Surveiller :
    - flux de données ;
    - partage de données ;
    - accès non autorisés ;
    - potentielles violations.

```
Data Flow
→ Monitoring
→ Suspicious Activity?
→ Detection / Response
```

La surveillance permet de détecter plus rapidement un incident et d’y répondre.
## Protection des Données Statiques
Les données stockées doivent également être protégées par plusieurs mécanismes complémentaires.
### Chiffrement des données

- Les données statiques doivent être chiffrées pour limiter l’accès en cas de compromission du support.
- Le chiffrement peut être appliqué au niveau :
    - disque ;
    - système de stockage ;
    - base de données.

```
Stored Data
→ Encryption
→ Protected Data at Rest
```

### Contrôles d’accès

- Restreindre l’accès aux données aux seuls utilisateurs autorisés.
- Appliquer :
    - rôles ;
    - permissions ;
    - restrictions ;
    - authorization controls.

```
User
→ Access Control
→ Data

Need Access?
├─ Yes → Allow
└─ No  → Deny
```

→ application du **Least Privilege**.
### Sauvegarde et récupération

- Effectuer des sauvegardes régulières des données statiques.
- Prévoir un processus de récupération.
- Les sauvegardes doivent elles-mêmes être protégées.

```
Production Data
→ Backup
→ Secure Storage
→ Recovery if needed
```

## Sécurité du stockage
Les zones de stockage doivent être protégées à la fois :

### Physiquement

- datacenters sécurisés ;
- server rooms ;
- contrôle d’accès ;
- caméras ;
- alarmes.
### Logiquement / électroniquement

- chiffrement ;
- firewall ;
- security tools ;
- intrusion detection systems.
## Monitoring & Incident Response

- Surveiller l’état de sécurité des données.
- Détecter les comportements anormaux ou inhabituels.
- Utiliser notamment :
    - logs ;
    - SIEM ;
    - mécanismes de monitoring.

```
Logs
→ SIEM
→ Detection
→ Alert
→ Incident Response
```

## Suppression et destruction

- Les données statiques doivent également être supprimées ou détruites de manière sécurisée lorsqu’elles ne sont plus nécessaires.

```
Data no longer needed
→ Secure Deletion / Destruction
```

## Data at Rest vs Data in Transit

|                       | Data at Rest                          | Data in Transit                           |
| --------------------- | ------------------------------------- | ----------------------------------------- |
| État                  | Stockée                               | En déplacement                            |
| Exemple               | fichier sur disque                    | fichier téléchargé                        |
| Risque principal      | accès au stockage                     | interception pendant le transfert         |
| Protection principale | chiffrement + access control          | chiffrement + secure communication        |
| Autres contrôles      | backup, monitoring, physical security | monitoring, authentication, authorization |

```
At Rest
→ Protect Storage

In Transit
→ Protect Communication
```


Le point central est qu’une même donnée peut passer de **statique à dynamique puis redevenir statique** ; les protections doivent donc suivre son état tout au long de son cycle de vie.
