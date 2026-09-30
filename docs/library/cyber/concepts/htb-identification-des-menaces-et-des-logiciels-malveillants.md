---
title: HTB — Identification des menaces et des logiciels malveillants
source: Cyber/99_Concepts/HTB_Identification des menaces et des logiciels malveillants.md
---

## System Vulnerabilities & Security Measures
### Zero-Day 
- Zero-Day vulnérabilité : Vuln inconnue de l'éditeur, donc aucun patch officiel dispo au moment de sa découverte/exploitation
- Risque élevé car les défenses classiques basées sur signatures/patchs peuvent être inefficaces.
#### Défense en profondeur :
- Patching régulier des autres composants ;
- application layer Firewall / WAF ;
- IPS pour détecter/bloquer des comportements suspects ;
- EDR / monitoring comportemental en complément.
- Le patching ne corrige pas directement un vrai zero-day tant que le vendor n'a pas publié de fix mais réduit l'exposition globale et les autres chemins d'attaque.

### Origines des vulnérabilités 
#### Weak configuration / Misconfiguration 
- Une mauvaise configuration peut rendre un système vulnérable même si aucun bug logiciel n'existe.

| Problème                         | Risque / exemple                                                             |
| -------------------------------- | ---------------------------------------------------------------------------- |
| **Open Permissions**             | Droits trop larges, comptes guest/anonymous capables de modifier des données |
| **Unsecure Admin/Root Accounts** | Comptes privilégiés mal protégés ou trop nombreux                            |
| **Configuration Errors**         | Ex : DNS Zone Transfer accessible sans restriction                           |
| **Weak Encryption**              | Chiffrement faible ou absent pour données au repos/en transit                |
| **Unsecure Protocols**           | HTTP/Telnet/FTP au lieu de HTTPS/SSH/protocoles sécurisés                    |
| **Default Settings**             | Services inutiles installés/activés par défaut                               |
| **Open Ports & Services**        | Services inutiles exposés → surface d’attaque plus grande                    |
#### Third-Party Risks
- Un fournisseur ou partenaire peut introduire des vulnérabilités dans l'environnement.

| Problème                    | Risque / exemple                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Vendor Management           | Vérifier comment le produit s'intégre au réseau, protocoles utilisés, comptes nécessaires, support/patch encore dispo.                      |
| Supply Chain                | Fournisseur compromis peut livrer un produit/composant déjà malveillant.                                                                    |
| Outsourced code development | Code développé sans secure coding -> vuln applicatives.                                                                                     |
| Data storage                | Données stockées chez un tiers doivent rester : chiffrées, correctement contrôlées, idéalement déchiffrables uniquement par l'organisation. |
#### Patch management
- L'absence de stratégie de patching laisse les vuln connues exploitables.
- A maintenir à jour : 
	- Firmware : serveurs, routeurs, switches, appliances...
	- Operating System : patchs Windows/Linux/Mac...
	- Applications : Une app vuln peut compromettre l'host.

#### Vendor support / Legacy systems
- Legacy system : ancien système encore utilisé souvent : 
	- Plus supporté, plus patché, utilisant des protocoles obsolètes.
- Risque élevé car les vulns restent ouvertes.
- Si remplacement impossible :
	- isoler sur un segment réseau dédié, limiter flux autorisés, monitorer fortement, restreindre les accès.

### Impacts possibles d'une vulnérabilité non traitées

|Impact|Description|
|---|---|
|**Data Loss**|Suppression/chiffrement de données, ex : ransomware|
|**Data Breach**|Accès non autorisé à des données confidentielles|
|**Data Exfiltration**|Transfert non autorisé de données hors de l’organisation|
|**Identity Theft**|Données personnelles utilisées pour fraude/usurpation|
|**Financial Loss**|Arrêt de production, récupération, pertes commerciales|
|**Reputation Damage**|Perte de confiance clients/partenaires|
|**Availability Loss**|Service/système indisponible|
#### Data breach vs data exfiltration
- Breach : accès non autorisé aux données
- Exfiltration : données effectivement transférées hors de l'environnement.
- Exemple de protection contre exfiltration : 
	- désactivation/restriction USB, DLP, contrôle des uploads/emails, monitoring réseau.

### Configuration faible ou mauvaise configuration 
#### Unencrypted credentials / Cleartext
- Certains protocoles historiques transmettent les credentials sans chiffrement.
#### Logs & Event Anomalies
- Activer les logs ;
- Connaître leur emplacement ;
- Rechercher : 
	- Anomalies ;
	- event inhabituels ;
	- connexions suspectes ;
	- changement de configuration.
#### Permission issues
- Mauvaises permissions = cause fréquente de compromission interne.
- Appliquer : moindre privilege, revoir régulièrement ACL et permissions.
#### Access Violations 
- Accès à une ressource par un user non autorisé.
- Prévention :
	- Authentification obligatoire ;
	- trafic de login chiffré ;
	- permissions correctes ;
	- contrôles d'accès.
#### Certificate issues
- Les certificats sécurisent : web, email, communications serveur <-> serveur
- A vérifier : certificat non expiré, non révoqué, chaîne de confiance valdie, CA de confiance, nom du certificat correspondant au service.

## Principales menaces et stratégies d'atténuation
### Exfiltration de données
- Transfert de données hors d'un système/réseau sans autorisation.
- Exemple : 
	- copie sur USB, envoi par email, upload vers stockage cloud personnel.
- Prévention :
	- désactiver/restreindre les ports USB ;
	- utiliser solution DLP pour détecter/bloquer les transferts de données sensibles.
### Appareils mal configurés
- Les misconfigurations constituent un point d'entrée fréquent pour les attaquants. 

| Élément               | Risque / mesure                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------ |
| **Firewall**          | Vérifier les règles, segmenter le réseau et empêcher les accès non autorisés entre segments      |
| **Content Filtering** | Bloquer les sites dangereux ou susceptibles d’exécuter du contenu malveillant                    |
| **Access Points**     | WPA2/WPA3, clés robustes, changer les credentials admin par défaut, éventuellement MAC filtering |
| **Security Settings** | Vérifier ACL, passwords, clés, algorithmes de chiffrement et règles de filtrage                  |

### Problèmes liés aux employés 

| Élément                | Risque / mesure                                                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Policy violations**  | Former les employés aux politiques internes et à leur raison d'être.                                                                  |
| **Insider threat**     | Utiliser authentification, permissions et ACL, limiter les accès aux ressources nécessaires, anti malware sur les endpoints.          |
| **Social engineering** | Sensibiliser au phishing, baiting et autres techniques de manipulation.                                                               |
| **Social media**       | Définir ce qui peut être partagé, éviter photos/info internes pouvant révéler des données sensibles en arrière-plan.                  |
| **Personal email**     | Risque d'envoi de données pro vers extérieur, DLP pour bloquer les transferts, limiter l'accès au cloud/storage perso via firewall... |

### Application security
#### Logiciel non autorisé 
- Limiter les logiciels pouvant être installés/exécutés.
- Application allowlisting : seuls les logiciels explicitement autorisés peuvent s'exécuter. Type AppLocker.
####  Réferentiel de sécurité / Ecart par rapport au référentiel
- Security Baseline : configuration de sécurité de référence que les systèmes doivent conserver.
- Baseline Deviation : changement qui fait sortir un système de cet état attendu.
	- PowerShell Desired State Configuration (DSC) pour empêcher les changements qui s'écartent du référentiel.
#### Violation de la conformité des licences 
- Le dépassement ou non-respect des licences logicielles peut entraîner : 
	- problèmes de conformité ;
	- coûts/amendes.
- Utiliser inventaire centralisé pour suivre installations et licences.
#### Asset management
- Maintenir un inventaire et une gestion centralisée des systèmes :
	- Config, patches, drivers, applications....
	- Ex : GPO, MECM
#### Authentification Issues 
- Sécuriser les mécanismes d’authentification des applications.
- Éviter que les credentials puissent être interceptés.
- Utiliser des **comptes dédiés** pour les applications/services.

## Analyse des résultats des outils de sécurité 

- Diverses technologies de sécurité fournissent des résultats qui peuvent vous aider à identifier et à répondre aux incidents de sécurité potentiels.
### HIDS / HIPS
- **Output** : alertes sur des activités suspectes détectées sur l’hôte.
- Examiner :
    - date/heure ;
    - source ;
    - compte impliqué ;
    - événement déclencheur.

```
HIDS → détecte
HIPS → détecte + peut bloquer
```
### Antivirus
- Fournit logs/notifications sur :
    - malware détecté ;
    - fichier concerné ;
    - résultat du scan ;
    - action effectuée : quarantaine, suppression
→ Surveiller les détections et vérifier que la menace a bien été traitée.
### Advanced Malware Removal Tools
- Donnent davantage de détails sur :
    - malware identifié ;
    - suppression/quarantaine ;
    - état du nettoyage.

→ Vérifier que le malware est réellement **contenu et supprimé**.
### Patch Management Tools
- Rapports sur :
    - patches nécessaires ;
    - état du déploiement ;
    - systèmes à jour/non à jour ;
    - échecs d’installation.
→ Prioriser les patches critiques et enquêter sur les systèmes où le déploiement échoue
### UTM — Unified Threat Management
Regroupe plusieurs fonctions de sécurité dans une même solution.
Output possible :
- trafic suspect ;
- virus/spam bloqués ;
- violations de content filtering.
→ Examiner les alertes et rapports réseau.
### DLP
- Génère une alerte lorsqu’un transfert sensible est détecté/bloqué.
Exemples :
```
Copie fichier confidentiel → USB
Email contenant données sensibles → externe
```
→ appliquer les politiques DLP et surveiller les violations.
### DEP — Data Execution Prevention
- Empêche l’exécution de code dans certaines zones mémoire normalement destinées aux **données**.
### WAF — Web Application Firewall
- Filtre le trafic destiné aux **applications Web**.
- Les logs indiquent notamment :
    - requêtes autorisées ;
    - trafic malveillant bloqué ;
    - tentatives d’attaque Web.
```
Client → WAF → Web Application
```
→ analyser les logs pour identifier et répondre aux attaques applicatives.

## Cloud vs On Prem
- Lors de la transition vers des environnements cloud, il est essentiel de traiter les vulnérabilités qui peuvent découler d'erreurs de configuration.
- Voici les principales considérations pour les vulnérabilités basées sur le cloud par rapport aux installations sur site (on-premises) :

### Ports ouverts
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

### Authentication Methods
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
### Conditional Access
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
### Privilege Management
**On-Prem :**
- permissions locales/AD ;
- contrôle via rôles et groupes.

**Cloud :**
- éviter les privilèges excessifs ;
- appliquer **RBAC + Least Privilege** ;
- limiter fortement les rôles à très hauts privilèges (`Global Administrator`, etc.).

## Menaces sur la sécurité physique
### Espionnage - Snooping
- **Snooping** : accès non autorisé à des informations confidentielles par observation ou fouille.
- Exemples :
    - **Dumpster Diving** : récupérer des documents jetés ;
    - fouiller bureaux, tiroirs ou armoires d’autres employés.
- Prévention
	- **Clean Desk Policy** : ne pas laisser de documents sensibles sans surveillance.
	- Stocker les documents dans des **armoires verrouillées** et zones sécurisées.
	- **Détruire/shredder** les documents avant de les jeter.
```
Document sensible
→ stockage sécurisé
→ destruction avant élimination
```
### Asset Lost / Stolen
Les laptops, smartphones et tablettes perdus ou volés peuvent exposer des données sensibles.
- Ne pas laisser les appareils visibles dans une voiture → risque de **smash-and-grab**.
- Les placer dans un endroit non visible/sécurisé, par exemple le coffre.
- Au bureau, utiliser des **lockdown/security cables** pour attacher :
    - laptops ;
    - écrans ;
    - projecteurs ;
    - desktops.

> Les câbles antivol sont surtout un **moyen de dissuasion** : ils ne résistent pas forcément à un attaquant déterminé.
### Remote Device Reset / Wipe
- Un appareil perdu ou volé doit être **signalé immédiatement**.
- **Remote Wipe** : le serveur envoie une commande demandant au device d’effacer :
    - données ;
    - configurations.

```
Device perdu
→ signalement
→ Remote Wipe
→ données supprimées
```

→ réduit le risque d’exposition des données présentes sur l’appareil.
### Device Security Measures

#### Smartphones / Mobile Devices
Mesures principales :
- password/PIN ;
- **auto-lock** après une période d’inactivité ;
- fonctions de **device tracking** ;
- remote wipe.
L’objectif est qu’un appareil volé ne puisse pas être utilisé directement par l’attaquant.
#### Laptops
Mesures possibles au niveau BIOS/UEFI :
- **Power-on password** ;
- password administrateur BIOS/UEFI ;
- limiter/modifier le **boot order** pour empêcher facilement le démarrage sur USB/CD externe.
```
Boot externe bloqué
→ plus difficile de démarrer un OS contrôlé par l'attaquant
```
#### Full-Disk Encryption
Si un attaquant possède physiquement le disque, le chiffrement complet protège les données au repos.
Exemple Windows :
- **BitLocker**.
```
Disque volé
+
BitLocker
→ données chiffrées
```
**Complément :** BitLocker n’est pas simplement un « boot password ». Il chiffre le disque ; avec une configuration **TPM + PIN**, il peut également imposer une authentification avant le démarrage de Windows.
### Employee Mistakes
Les erreurs humaines peuvent provoquer des dégâts physiques.
#### ESD — Electrostatic Discharge
- Une personne peut accumuler de l’électricité statique.
- En touchant un composant, cette charge peut être transférée et :
    - endommager ;
    - voire détruire le composant.
Exemple :
```
Technicien
→ électricité statique
→ touche motherboard/RAM
→ ESD
→ composant endommagé
```
Prévention :
- former les équipes support ;
- utiliser un **anti-static wrist strap** relié à la terre avant de manipuler les composants.
### Malicious Interference / Sabotage
- **Sabotage** : action volontaire visant à endommager ou perturber les systèmes.
- Peut notamment provenir d’un **disgruntled employee**, mais pas uniquement.
Exemple :
```
Employé malveillant
→ modification/suppression d'une base de données
→ interruption du service
```
Prévention / Résilience
- identifier les systèmes particulièrement exposés au sabotage ;
- limiter les privilèges ;
- disposer d’un **Recovery Plan** détaillé ;
- prévoir :
    - procédures de restauration ;
    - backups ;
    - pièces de rechange nécessaires.
Le but n’est pas seulement d’empêcher le sabotage, mais aussi de pouvoir **restaurer rapidement le service** après un incident.

## Comprendre les logiciels malveillants
- Un malware est un programme conçu pour endommager, perturber ou détourner un système : suppression de fichiers, espionnage, vol de données, ralentissement, prise de contrôle, etc.
### Elévation de privilège 
- Le Privilege Escalation consiste à obtenir des droits supérieurs à ceux initialement accordés, souvent en exploitant une vulnérabilité ou une mauvaise configuration.
- Avec des privilèges élevés, un attaquant peut notamment modifier le système ou installer une backdoor pour conserver l'accès. 

| Type                                | Principe                                                                                                                                                                                                         |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Vertical Privilege Escalation**   | Passer d’un niveau faible à un niveau supérieur, ex. `user → admin`.                                                                                                                                             |
| **Horizontal Privilege Escalation** | Accéder aux ressources d’un autre utilisateur ayant un niveau de privilège similaire.                                                                                                                            |
| **Privilege De-escalation**         | Diminuer volontairement ses privilèges pour agir avec un niveau d’accès inférieur. ⚠️ La **de-escalation** n’est pas réellement une forme d’escalade de privilèges ; c’est plutôt le fait d’abaisser ses droits. |
### Virus & Malware
#### Virus exécutable 
- Ne s'active que lorsque le fichier infecté est exécuté.
- S'attache à des fichiers exécutables comme : .exe, .com
- Peut se propager via : USB, partage réseau, anciens supports amovibles.
#### Boot Sector Virus - Virus de secteur d'amorçage
- Infecter le secteur d'amorçage d'un disque.
- Peut remplacer/modifier le code chargé au démarrage.
- Une infection grave peut empêcher le système de démarrer correctement.
#### Macro Virus
- De nombreuses applications prennent aujourd'hui en charge les macros, qui automatisent des tâches au sein du logiciel.
- Malware écrit dans un langage de macro, souvent **VBA** dans Microsoft Office.
	- Langage de programmation puissant qui peut manipuler à la fois l'application et le système d'exploitation.
- Intégré dans un document et exécuté lorsque la macro est déclenchée.
- Peut :
    - supprimer/modifier des fichiers ;
    - exécuter des commandes ;
    - envoyer des messages ;
    - télécharger d’autres payloads.

```
Document Office
→ Macro VBA
→ code malveillant
```

> Les macros ne s’exécutent pas nécessairement automatiquement aujourd’hui : les versions modernes d’Office appliquent davantage de restrictions et avertissements.
#### Logic bomb
- Code malveillant qui reste dormant jusqu'à un événement précis.
- Type de virus qui se cache dans un logiciel installé. Le logiciel fonctionne normalement jusqu'à ce qu'un certain événement se produise.
- Déclencheurs possibles :
	- date/heure ;
	- suppression d’un compte ;
	- changement particulier dans le système ;
	- autre condition définie par l’attaquant.

```
Malware dormant
      ↓
Condition atteinte
      ↓
Payload déclenché
```

Exemple :

```
Date = 01/09
→ suppression des données
```

Peut notamment être utilisée pour du **sabotage interne**.

> Une logic bomb n’est pas nécessairement un virus ; c’est surtout un mécanisme de déclenchement conditionnel.
#### Ver - Worm
- Malware capable de se répliquer automatiquement.
- Peut se propager rapidement entre systèmes, notamment via :
	- vulnérabilités réseau ;
	- protocoles/services réseau ;
	- email ;
	- supports USB.
- Différence importante :
```
Virus → généralement dépend d'un fichier/hôte et d'une exécution
Worm  → capacité d'auto-propagation
```
#### Trojan - Cheval de Troie
- Malware qui se **fait passer pour un logiciel légitime ou utile** afin de pousser l’utilisateur à l’installer.
- Une fois installé, il peut :
	- installer une **backdoor** ;
	- permettre un contrôle distant ;
	- voler des informations ;
	- installer d’autres malwares.
#### Backdoor
- Historiquement, certains Trojans ouvraient un **port TCP/IP en écoute** :
```
Trojan
→ ouvre port
→ attaquant se connecte
→ contrôle du système
```
- Aujourd’hui, les malwares utilisent aussi souvent des connexions **sortantes vers un serveur C2**, plus faciles à faire passer à travers certains firewalls.
- Payloads possibles
	- **Adware**
		- affiche des publicités indésirables.
	- **Keylogger**
		- enregistre les frappes clavier ;
		- peut voler :
		    - passwords ;
		    - messages ;
		    - informations sensibles.
```
Victime tape password
→ Keylogger
→ credentials capturés
```

## Différents types de logiciels malveillants
### Spyware 
- Logiciel espion, installé discrètement pour surveiller l'activité d'un utilisateur et transmettre les informations à un système distant.
- Peut notamment :
	- suivre la navigation ;
	- collecter des informations ;
	- modifier certains paramètres système ;
	- rediriger le navigateur ;
	- dégrader les performances réseau.
### Adware
- **Adware** : logiciel qui affiche automatiquement des publicités, souvent sous forme de pop-ups.
- Peut chercher à pousser l’utilisateur vers des produits ou services.
### Spam
- Le spam désigne les courriels commerciaux non sollicités qui inondent les boîtes de réception.
- Envoi massif d’**emails non sollicités**, généralement pour promouvoir produits/services.
- Les spammeurs peuvent récupérer des adresses via :
    - sites Web ;
    - forums/groupes de discussion ;
    - listes d’adresses achetées.
- Des **spambots** automatisent la collecte d’adresses visibles publiquement.
- Prévention :
	- filtres antispam ;
	- éviter d’exposer inutilement des adresses email publiques.
### Rootkit
- **Rootkit** : malware conçu pour maintenir un **accès privilégié et furtif** au système.
- Son objectif principal est souvent de **cacher sa présence ou celle d’autres composants malveillants**.

| Type                                                  | Principe                                                                                                                                                                                                                                |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rootkits au niveau applicatif - **Application-level** | Fichiers exécutables qui fonctionnent en mode utilisateur, tels que les virus de type cheval de Troie, permettant aux pirates d'accéder au système discrètement.                                                                        |
| rootkits au niveau bibliothèque - **Library-level**   | Remplacement/modification de DLL pour dissimuler l’activité                                                                                                                                                                             |
| rootkits au niveau du noyau - **Kernel-level**        | Chargés par le noyau du système d'exploitation, souvent en remplaçant des fichiers drivers. Ils fonctionnent en mode noyau, accordant un accès étendu au système et le potentiel de causer des dommages importants.                     |
| rootkits virtualisés - **Virtualized**                | Se charge sous/avant l’OS et l’exécute dans un environnement virtualisé. Leur furtivité réside dans le fait que le système d'exploitation reste inconscient de cette virtualisation.                                                    |
| rootkits de firmware - **Firmware**                   | Implanté directement dans le firmware d’un périphérique/système. indépendamment du système d'exploitation. Leur détection est particulièrement difficile en raison de leur intégration profonde dans les opérations au niveau matériel. |
- Plus le rootkit est bas dans la stack → plus sa détection peut être difficile
### Botnet
- **Botnet** : ensemble de systèmes compromis contrôlés par un attaquant.
- Chaque système compromis est appelé :
    - **bot** ;
    - **zombie**.
- Le botnet peut être utilisé pour :
    - spam ;
    - DoS/DDoS ;
    - autres attaques coordonnées.
- L’accès au botnet peut également être loué à d’autres attaquants.
### RAT — Remote Access Trojan
- Malware donnant à un attaquant un **accès distant au système compromis**.
- Peut arriver via :
    - logiciel apparemment légitime ;
    - pièce jointe ;
    - téléchargement malveillant.
- Une fois installé :
    - crée une backdoor ;
    - permet l’exécution de commandes à distance ;
    - peut servir à compromettre d’autres systèmes.
```
Trojan installé
→ backdoor
→ Remote Access
→ exécution de commandes
```
- RAT vs Trojan
```
Trojan → méthode de camouflage / installation
RAT    → fonctionnalité de contrôle distant
```
	- Un RAT peut donc être distribué sous forme de Trojan.
### Keylogger
- Outil logiciel ou matériel conçu pour capturer toutes les frappes de touches effectuées sur un système.
- Hardware Keylogger
	- Petit dispositif placé physiquement entre → l’attaquant le récupère ensuite pour consulter les données.
- Software Keylogger
	- fonctionne en arrière-plan ;
	- enregistre les touches :
	    - dans un fichier local ;
	    - ou les transmet à distance.
### Backdoor
- Méthode d’accès alternative permettant à l’attaquant de revenir sur le système sans utiliser le point d’entrée initial.
- Peut être créée via :
    - Trojan ;
    - service/port malveillant ;
    - compte utilisateur ajouté ;
    - autre mécanisme de persistence.

```
Compromission initiale
       ↓
Backdoor
       ↓
Accès futur
```
### Ransomware
- Malware qui chiffre ou bloque les données/systèmes afin d’exiger une rançon.
- L’attaquant conserve la possibilité de déchiffrement et demande un paiement.
### PUP — Potentially Unwanted Program
- Logiciel installé en même temps qu’un programme souhaité mais **non désiré par l’utilisateur**.
- Peut :
    - afficher de la publicité ;
    - installer des toolbars ;
    - ralentir le système ;
    - collecter certaines informations.
- Prévention :
	- lire les écrans d’installation ;
	- décocher les logiciels supplémentaires ;
	- anti-malware.
```
PUP ≠ forcément malware pur
mais
PUP → logiciel indésirable / potentiellement intrusif
```
### Virus sans fichier -  Fileless Malware
- Malware fonctionnant **principalement en mémoire** plutôt qu’en déposant un exécutable classique sur disque.
- Peut s’appuyer sur des processus ou outils déjà présents sur le système.
> **Fileless** ne veut pas nécessairement dire « absolument aucun fichier n’existe jamais », mais que l’exécution malveillante repose principalement sur la mémoire et/ou des composants légitimes.
### Command & Control — C2 / C&C
- Après compromission, les malwares peuvent communiquer avec un serveur **Command & Control**.
- Le C2 permet à l’attaquant :
    - d’envoyer des commandes ;
    - de contrôler les machines ;
    - d’exfiltrer des données ;
    - de perturber le système ;
    - de télécharger d’autres payloads.
```
Attacker
   ↓
C2 Server
   ↓
Compromised Host
```
- Le **C2 n’est pas un type de malware**, mais une infrastructure/méthode de communication utilisée par les malwares.
### Cryptomalware
- Malware qui **chiffre les fichiers sans autorisation**.
- Souvent utilisé comme composant d’un ransomware :
    - fichiers chiffrés ;
    - accès impossible ;
    - demande de paiement.
```
Cryptomalware → action = chiffrement
Ransomware    → objectif = extorsion
```
- Les deux concepts se recouvrent souvent, mais ne sont pas strictement synonymes.
### Polymorphic Malware
- Malware qui **modifie son apparence/code** afin d’éviter les détections basées sur des signatures statiques.
- Le comportement général peut rester identique malgré les modifications.
```
Version A → Signature A
Version B → Signature B
Version C → Signature C

même comportement général
```
→ rend les signatures antivirus traditionnelles moins efficaces.
### Virus blindé - Armored Virus
- Malware conçu pour rendre son **analyse / reverse engineering difficile**.
- Peut employer des techniques empêchant ou compliquant :
    - décompilation ;
    - debugging ;
    - analyse statique/dynamique.
```
Polymorphic → évite surtout la détection
Armored     → complique surtout l'analyse
```

## Considération sur le matériel et les appareils
### BIOS /UEFI
- Le BIOS contient le code nécessaire à l’initialisation du matériel et permet de configurer différents paramètres via le setup BIOS/CMOS.
- Côté sécurité :
	- contrôler le **boot order** ;
	- éviter le boot depuis :
	    - USB ;
	    - CD/DVD ;
	    - réseau/PXE ;
	- privilégier le disque local.

```
Boot externe autorisé
→ attaquant démarre sur un Live OS
→ peut tenter d'accéder aux données locales
```

→ Protéger également l’accès au BIOS/UEFI avec un mot de passe administrateur.
### Sécurité USB
- Les clés USB facilitent le transport de données hors de l’entreprise.
- Mesures :
	- définir quelles données peuvent être stockées sur USB ;
	- interdire les supports personnels si nécessaire ;
	- mettre en place station blanche ;
	- dans les environnements sensibles, **désactiver complètement les ports USB**.

```
USB → risque d'exfiltration + introduction de malware
```
### Smartphones & Tablettes
- Les appareils mobiles contiennent souvent :
	- contacts professionnels ;
	- documents ;
	- emails ;
	- accès Internet et applications internes.
- Mesures principales :
	- gestion du cycle de vie, via mdm ;
	- verrouillage de l’appareil ;
	- chiffrement des données ;
	- analyser les vulnérabilités des appareils utilisés dans l’organisation.
- Vulnérables à plusieurs types d'attaques : 
	- Bluesnarfing : Connexion Bluetooth non autorisée permettant de **récupérer des données** depuis l’appareil.
	- Bluejacking : Envoi de **messages non sollicités** entre appareils Bluetooth.
	- Bluebugging : Exploit Bluetooth qui permet à un pirate d'accéder aux fonctionnalités du téléphone. Peut permettre, par exemple, de passer des appels via des commandes AT.
```
Bluesnarfing → récupérer des données
Bluejacking  → envoyer des messages
Bluebugging  → contrôler certaines fonctions
```
### Stockage amovible
- Les supports amovibles peuvent :
	- introduire des malwares ;
	- permettre l’exfiltration de données ;
	- être perdus ou volés.
- Exemple :
```
USB personnel infecté
→ connecté au poste professionnel
→ malware introduit sur le réseau
```
- Mesures :
	- interdire les supports amovibles si possible ;
	- interdire les supports personnels ;
	- interdire la sortie des supports ;
	- mettre en place station blanche ;
	- formaliser cette règle dans la politique de sécurité ;
	- lorsqu’ils sont nécessaires :
	    - les retirer lorsque l’utilisateur quitte son poste ;
	    - les stocker dans une armoire sécurisée.
	- La même logique peut s’appliquer aux laptops laissés sans surveillance.
### Stockage en réseau (NAS)
- Un **NAS** fournit un stockage central accessible via le réseau.
- La sauvegarde des données sur un NAS est essentielle, car il peut stocker toutes les données de l'entreprise en un seul endroit.
- Caractéristiques :
	- ses paramètres peuvent être gérés via une interface web ;
	- plusieurs disques ;
	- souvent RAID / tolérance aux pannes ;
	- partage de fichiers centralisé ;
	- compatible avec différents OS/protocoles.
- Exemples :
```
Windows → SMB
Linux   → NFS
```
#### Risques / protections
- **Access Control**
    - un NAS compromis peut exposer une grande quantité de données ;
    - éviter son exposition directe à Internet.
- **Malware**
    - un malware peut toucher de nombreux fichiers centralisés ;
    - scanner régulièrement les données.
- **Authentication / Authorization**
    - contrôler précisément qui peut accéder aux fichiers.
- **Encryption**
    - protéger les données stockées et, si possible, les communications.
- **Backups**
    - RAID ≠ backup ;
    - conserver des sauvegardes séparées du NAS.
### PBX  - Téléphonie
- Un **PBX (Private Branch Exchange)** est un système téléphonique utilisé au sein d'une entreprise pour gérer tous les appels téléphoniques internes, permettant de gérer plusieurs extensions à partir de l’infrastructure téléphonique de l’entreprise.
-  Il permet à une entreprise d'avoir une seule ligne téléphonique externe tout en prenant en charge plusieurs systèmes et numéros de téléphone internes. Chaque téléphone de l'entreprise se voit attribuer un numéro de poste unique.
- Mesures de sécurité :
	-  Contrôle physique :
		- placer le PBX dans une salle verrouillée ;
		- accès limité ;
		- dispositifs anti-sabotage ;
		- inspection régulière du matériel.
	- Paramètres par défaut :
		- changer les comptes/passwords par défaut ;
		- sécuriser l’administration distante.
### Risques de sécurité avec les systèmes embarqués et spécialisés
#### Raspberry Pi
- petit système contenant CPU, RAM et interfaces ;
- utilisé pour créer des systèmes personnalisés.
Sécurité :
- désactiver les fonctionnalités inutiles, ex. Bluetooth.
#### FPGA - **Field-Programmable Gate Array**
- circuit intégré pouvant être programmé pour exécuter des fonctions matérielles personnalisées.
#### Arduino
- carte basée sur microcontrôleurs ;
- utilisée pour créer des systèmes électroniques ;
- généralement programmée en C/C++.
##### Autres systèmes embarqués

| Technologie                                                | À savoir                                                                                                                                          |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **HVAC / CVC**                                             | Systèmes informatisés contrôlant chauffage, ventilation, climatisation                                                                            |
| Système sur une puce **SoC**                               | Puce intégrant diverses fonctionnalités comme des processeurs (CPU) et des processeurs graphiques (GPU). Exemple : Raspberry Pi.                  |
| Système d'exploitation en temps réel **RTOS**              | OS conçus pour traiter les données en temps réel.                                                                                                 |
| Imprimantes/Appareils multifonctions **MFD / Imprimantes** | Peuvent stocker des documents dans leur mémoire/disque et exposer une interface Web                                                               |
| **Surveillance Systems**                                   | Comprennent des caméras avec des systèmes embarqués qui peuvent se connecter à un serveur central ou à Internet, posant des risques d'exposition. |
| **Drones**                                                 | Véhicules aériens pilotés à distance                                                                                                              |
| **VoIP**                                                   | Technologie pour la communication vocale sur des réseaux TCP/IP comme Internet.                                                                   |
### SCADA / ICS
#### SCADA - Supervisory Control and Data Acquisition
- utilisé pour superviser et contrôler des processus industriels.
- Exemples :
    - HVAC ;
    - éclairage ;
    - réfrigération ;
    - systèmes industriels.
- La sécurité physique est importante car une manipulation peut perturber :
	- supervision ;
	- alarmes ;
	- fonctionnement industriel.
#### ICS - Industrial Control Systems
- Terme plus large (qui inclut les systèmes SCADA) regroupant les systèmes utilisés pour surveiller/contrôler des équipements industriels.
```
ICS
 ├─ SCADA
 └─ autres systèmes de contrôle industriel
```
- Présents notamment dans :
	- usines ;
	- manufacturing ;
	- production d’énergie.
### IoT - Internet of Things 
- Les appareils **IoT** communiquent avec d’autres systèmes via Internet ou des réseaux locaux.
- Leur sécurité peut être faible lorsque les fabricants privilégient la **connectivité et la simplicité** aux contrôles de sécurité.
-  Catégories
	- **Sensors**
	    - thermostats ;
	    - caméras ;
	    - capteurs environnementaux.
	- **Smart Devices** : appareils connectés au réseau qui communiquent avec d'autres en utilisant des technologies telles que :
	    - Wi-Fi ;
	    - Bluetooth ;
	    - réseau cellulaire.
	- **Wearables**
	    - smartwatch ;
	    - objets portés sur le corps ;
	    - souvent reliés au smartphone.
	- **Facility Automation** : Systèmes conçus pour contrôler les éléments de :
	    - HVAC/CVC ( (chauffage, ventilation et climatisation)) ;
	    - automatisation du bâtiment.
- Weak Default Settings
	- Problème fréquent :
```
Default username/password
Default services
Default network settings
```
→ les attaquants connaissent souvent ces configurations.
- Mesures :
	- changer les credentials par défaut ;
	- désactiver les services inutiles ;
	- patcher/mettre à jour si possible ;
	- segmenter les appareils IoT du reste du réseau.
