---
title: HTB — IT Security for Corporates
source: Cyber/99_Concepts/HTB_IT Security for Corporates.md
---

## Inventaire

- Pour protéger une infrastructure, il faut savoir :
    - quels équipements sont connectés ;
    - quels logiciels sont utilisés ;
    - qui y a accès ;
    - quelles mesures de sécurité sont appliquées.
### Contenu minimal de l’inventaire

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

### Équipements en fin de vie - End-of-Life — EOL

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

### Secure Boot

- Activer **Secure Boot** sur tous les équipements compatibles.
- Vérifie au démarrage que les composants chargés sont **signés et approuvés par une chaîne de confiance UEFI**.

```
Bootloader non approuvé / signature invalide
→ boot bloqué
```

→ réduit le risque de bootkits/rootkits chargés avant l’OS.

> Ce n’est pas simplement « logiciel approuvé par le fabricant » : Secure Boot repose sur des **signatures cryptographiques et clés de confiance configurées dans l’UEFI**.
### Software Policy

- Pour réduire l’**Attack Surface**, définir clairement :

```
Allowed Software
vs
Forbidden Software
```

#### Allowed Software

- Fournir aux utilisateurs un catalogue de logiciels approuvés via :
    - **GPO**
    - **Microsoft Intune**
- Permet d’installer des applications sans donner de droits administrateur ni télécharger soi-même des installateurs sur Internet.

```
Catalogue approuvé
→ installation contrôlée
→ moins de téléchargements suspects
```

#### Forbidden Software

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

### Security Hardening

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
### Antivirus / EDR

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
## Sauvegardes — Backups

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
## Protection de la navigation Internet

- Objectif : empêcher l’accès à des :
    - sites non autorisés ;
    - domaines suspects ;
    - domaines connus comme malveillants.

```
User → DNS / Web Filtering → Allow / Block
```

### DNS Filtering

- Le **DNS Filtering** bloque la résolution de domaines classés comme :
    - malware ;
    - phishing ;
    - C2 ;
    - contenus interdits par la politique interne.
- Peut aussi bloquer certaines catégories non professionnelles.

```
User demande malicious-site.com
→ DNS Filter
→ domaine interdit
→ résolution bloquée
```


> Le filtrage DNS n’est pas forcément réalisé directement par le firewall : il peut être assuré par un **resolver DNS sécurisé**, une passerelle Web ou une solution dédiée.
### URL Shorteners

- Les **raccourcisseurs d’URL** masquent la destination finale d’un lien.
- Ils sont fréquemment utilisés dans :
    - phishing ;
    - redirections malveillantes ;
    - contournement de certains filtres.
- Exemple :

```
https://bit.ly/xxxx
→ destination réelle non visible immédiatement
```

- Selon la politique de l’entreprise :
	- bloquer certains services de shortening ;
	- ou les analyser/résoudre avant autorisation.
### Monitoring des blocages

- Après mise en place du filtrage, il faut examiner les tentatives d’accès bloquées.
- Informations utiles :
	- utilisateur ;
	- device ;
	- domaine demandé ;
	- catégorie ;
	- timestamp ;
	- fréquence des tentatives.

```
DNS Block Logs
→ domaine malveillant
→ quel utilisateur ?
→ quelle machine ?
→ incident isolé ou compromission ?
```

- Une tentative vers un domaine C2 ou phishing peut être un **signal d’investigation**, pas seulement un événement à bloquer.
### Gestion centralisée des navigateurs

- Appliquer une configuration homogène et sécurisée sur les navigateurs de l’entreprise.
- Objectif : réduire les possibilités d’exécution ou d’installation de contenu dangereux.
- Mesures possibles :
	- mises à jour automatiques ;
	- limiter/interdire les extensions non approuvées ;
	- désactiver certains contenus ou fonctions à risque ;
	- imposer les paramètres de sécurité ;
	- contrôler les téléchargements ;
	- appliquer des politiques de navigation.
- Outils possibles selon l’environnement :

```
GPO
Intune
Browser Enterprise Policies
```

### Extensions / Plug-ins

- Une extension navigateur peut disposer de permissions importantes :
    - lire les pages visitées ;
    - modifier leur contenu ;
    - accéder à certaines données utilisateur.

→ utiliser une **allowlist d’extensions approuvées** plutôt que laisser les utilisateurs installer librement n’importe quel plug-in.
## Application de correctifs — Patch Management

- Déployer les correctifs de **logiciels, OS et firmware** aussi rapidement que possible, en prenant évidemment en compte les contraintes liés à l'infrastructure, s'assurer qu'une montée de version ne bloque rien.
- Activer les **mises à jour automatiques** lorsqu’elles sont compatibles avec les contraintes de l’environnement.

```
Vulnérabilité connue
→ Correctif disponible
→ Déploiement
→ Réduction de la fenêtre d'exposition
```

### SLA de patching

- Un **SLA — Service-Level Agreement** définit notamment un **délai maximal attendu** pour effectuer une action ou fournir un service.
- Dans le cadre du patch management :

```
Criticité de la vulnérabilité
→ délai maximum de correction
```

- Exemple :

```
Critical → patch ≤ 48h
High     → patch ≤ 7 jours
Medium   → patch ≤ 30 jours
```


> Les délais exacts dépendent de la politique et du niveau de risque de l’organisation.
### Priorisation des correctifs

- Le délai ne doit pas dépendre uniquement du score CVSS.
- Critères importants :

|Critère|Impact sur la priorité|
|---|---|
|**CVSS**|Mesure la sévérité technique de la vulnérabilité|
|**Internet Exposure**|Un serveur exposé publiquement est généralement prioritaire|
|**Known Exploitation**|Vulnérabilité activement exploitée → priorité très élevée|
|**Asset Criticality**|Un système critique doit être traité plus rapidement|
|**Exploit Availability**|Exploit public disponible → risque accru|

```
CVSS élevé
+
Internet-facing
+
Exploit public / exploitation active
→ Patch prioritaire
```

### CVE vs CVSS

```
CVE  → identifiant d'une vulnérabilité
CVSS → score de sévérité de cette vulnérabilité
```

- Exemple :

```
CVE-2026-XXXX
CVSS: 9.8 Critical
```

### Zero-Day

- **Zero-day** : vulnérabilité pour laquelle aucun correctif n’est encore disponible au moment où elle est découverte/exploitée.
- Dès qu’un patch existe, il faut le déployer selon une priorité élevée si le risque le justifie.

> À distinguer de **Known Exploited Vulnerability** : une vulnérabilité peut être activement exploitée sans être un zero-day.
### Bon processus de patching

- connaître les assets/version via l’inventaire ;
- identifier les vulnérabilités ;
- prioriser selon le risque ;
- tester si nécessaire avant production ;
- déployer ;
- vérifier que le patch a réellement été appliqué.
## Analyse de risque — Risk Assessment

- Les **Risk Assessments** servent à identifier et prioriser les risques afin d’allouer les ressources et investissements de sécurité là où ils sont les plus importants.
- Une analyse de risque prend généralement en compte :

```
Risk ≈ Likelihood × Impact
```

→ probabilité qu’un événement se produise + conséquences pour l’organisation.
### Retour en service — Recovery Priority

- L’entreprise doit déterminer **quels systèmes/services doivent être restaurés en priorité** après un incident.
- Cette analyse permet également d’évaluer :
    - l’impact d’une interruption ;
    - la durée maximale d’indisponibilité acceptable ;
    - les dépendances entre systèmes.
- Exemple :

```
Incident majeur
   ↓
1. Identity / AD
2. Network / DNS
3. ERP / applications critiques
4. Services secondaires
```

### Business Impact Analysis — BIA

- Cette démarche correspond notamment à une **BIA — Business Impact Analysis** :
	- identifier les processus critiques ;
	- mesurer l’impact de leur indisponibilité ;
	- déterminer leurs priorités de restauration.
- Elle permet notamment de définir :

|Concept|Signification|
|---|---|
|**RTO**|Temps maximal acceptable avant restauration du service|
|**RPO**|Quantité maximale de données que l’on accepte de perdre|

### Risques liés aux réseaux connectés

- Toute connexion à l’infrastructure crée une **relation de confiance** et donc une surface de risque supplémentaire.
- Cela concerne :
    - autres entités du groupe ;
    - partenaires ;
    - prestataires ;
    - fournisseurs ;
    - services cloud.

```
Company A ← VPN / API / Network Link → Partner B
                              ↓
                     risque transférable
```

- Une compromission du partenaire peut devenir un point d’entrée vers votre propre infrastructure.
### Third-Party Risk

- Il faut évaluer le niveau de sécurité des partenaires avant et pendant la relation.
- Points à vérifier :
	- rapidité d’application des correctifs ;
	- politique de gestion des vulnérabilités ;
	- configuration sécurisée des VPN ;
	- gestion des certificats ;
	- MFA et contrôle des accès ;
	- sécurité des services exposés ;
	- configuration des solutions cloud ;
	- journalisation et capacité de réponse aux incidents.

```
Votre sécurité
≠ seulement votre infrastructure

Votre sécurité
→ dépend aussi des tiers qui y ont accès
```

### VPN & certificats

- Les équipements VPN doivent être correctement configurés.
- Éviter les certificats/configurations par défaut pouvant :
    - affaiblir l’authentification ;
    - révéler une mauvaise configuration ;
    - faciliter certaines attaques selon le produit.

→ les certificats doivent être **propres à l’organisation**, valides et correctement gérés.
### Accès partenaires

- Le principe de **Least Privilege** s’applique également aux tiers.

```
Partner
→ uniquement les systèmes nécessaires
→ uniquement les ports/services nécessaires
→ uniquement pendant la durée nécessaire
```

- Mesures utiles :
	- segmentation réseau ;
	- comptes dédiés ;
	- MFA ;
	- accès temporaires si possible ;
	- monitoring renforcé ;
	- révocation immédiate lorsque l’accès n’est plus nécessaire.
### Réévaluation du risque

- Une analyse de risque n’est pas définitive.
- Elle doit être réévaluée notamment lors de :
	- nouvelle vulnérabilité critique ;
	- changement d’architecture ;
	- ajout d’un partenaire ;
	- nouvelle connexion réseau ;
	- migration cloud ;
	- incident de sécurité chez un fournisseur.
## Réseau — Network Security

- Surveiller le trafic **entrant et sortant** de l’organisation.
- Objectifs principaux :
    - détecter des comportements anormaux ;
    - limiter les mouvements d’un attaquant ;
    - conserver de la visibilité pour l’investigation.
### PCAP — Packet Capture

- Utiliser des ports **SPAN / Mirror** sur les équipements réseau pour copier le trafic vers une sonde d’analyse.
- Si possible, mettre en place **TAP**.
- Les captures réseau permettent :
    - d’observer les protocoles utilisés ;
    - d’identifier des destinations inhabituelles ;
    - de détecter certains comportements anormaux ;
    - d’effectuer une analyse post-mortem après compromission.

```
Switch
├─ trafic normal
└─ SPAN / Mirror → IDS / Sensor / Packet Capture
```

- Exemples d’éléments suspects :
	- hausse inhabituelle du trafic DNS ;
	- connexions vers une IP rare ;
	- protocole inhabituel ;
	- volume anormal de données sortantes ;
	- beaconing périodique vers une destination externe.

> ⚠️ Un port SPAN peut perdre des paquets en cas de forte charge. Pour une capture plus fiable, un **network TAP** peut être préférable.
### Segmentation réseau

- La segmentation découpe le réseau en **zones plus petites et contrôlées**.
- Elle permet :
    - de réduire la surface d’attaque ;
    - de limiter le **Lateral Movement** ;
    - de contrôler les flux entre catégories de systèmes ;
    - d’isoler les ressources critiques.

```
Users VLAN
Servers VLAN
Management VLAN
Backup VLAN
DMZ
```

#### VLAN / PVLAN

- **VLAN** → sépare logiquement plusieurs réseaux de niveau 2.
- **PVLAN — Private VLAN** → permet d’isoler davantage des hôtes au sein d’un même VLAN.

> Un VLAN seul n’est pas une barrière de sécurité suffisante : les communications inter-VLAN doivent être contrôlées via **firewall / ACL / routing policy**.
### Réseau d’administration

- Les interfaces d’administration ne devraient pas être accessibles depuis n’importe quel poste utilisateur.

```
User Workstation
    X
Management Interface

Admin Network
    ↓
Management Interface
```

- À isoler idéalement :
	- interfaces de switches/routers/firewalls ;
	- hyperviseurs ;
	- iDRAC / iLO ;
	- consoles d’administration ;
	- RDP / SSH d’administration.
- Le **RDP administratif** peut par exemple être limité à un réseau dédié ou à un jump server.
### Examen des flux bloqués

- Après segmentation et mise en place de règles restrictives, il faut analyser les flux bloqués.
- Un blocage peut révéler :
	- endpoint compromis ;
	- malware tentant une communication ;
	- application non inventoriée ;
	- mauvaise configuration ;
	- dépendance oubliée ;
	- tentative de mouvement latéral.

```
Firewall DENY
→ Source ?
→ Destination ?
→ Port ?
→ Application ?
→ Legitimate ou Suspicious ?
```

→ un `DENY` n’est pas seulement un événement technique : il peut constituer un **signal de détection**.
### Alerte en cas d’utilisation anormale

- Une fois la visibilité réseau suffisante, définir des alertes sur les comportements inhabituels.
- Exemples :
	- hausse soudaine du trafic ;
	- transfert important vers Internet ;
	- protocole jamais utilisé auparavant ;
	- communication vers une destination rare ;
	- scans réseau ;
	- trafic hors des horaires habituels ;
	- saturation d’un lien.

```
Baseline normale
      ↓
Déviation importante
      ↓
Alert
```

### Baseline réseau

- Il faut connaître le **comportement réseau normal** pour repérer une anomalie.
- Cela peut inclure :
    - volumes habituels ;
    - protocoles utilisés ;
    - destinations fréquentes ;
    - horaires d’activité.
- Exemple :

```
Backup habituel : 01h00–03h00
Trafic élevé à 14h00
→ anomalie à vérifier
```

- Une anomalie n’est pas forcément malveillante : elle peut aussi révéler un problème opérationnel, comme un backup qui sature le réseau.
