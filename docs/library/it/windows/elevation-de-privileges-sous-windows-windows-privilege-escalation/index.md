---
title: Élévation de privilèges sous Windows (Windows Privilege Escalation)
source: IT/02 Windows/Élévation de privilèges/Élévation de privilèges sous Windows (Windows Privilege Escalation).md
format: cours
provenance: HTB Academy
revue: '2026-10-24'
---

Ces commandes servent aussi à l'inventaire et à l'audit de durcissement. Sur le site : [Énumération et audit local](https://disruptive-intelligence.github.io/cheatsheets/windows/fondamentaux/enumeration/). Les sorties réseau ci-dessous utilisent des adresses de remplacement ; les captures originales restent dans les archives locales.

Le Windows Privilege Escalation désigne l'ensemble des techniques permettant d'obtenir des privilèges plus élevés sur un système Windows après avoir obtenu un premier accès (Initial Foothold).

Dans un contexte de Pentest / Active Directory Assessment, l'objectif consiste généralement à passer d'un utilisateur disposant de droits limités à un contexte plus privilégié :

- Local Administrators : membres du groupe des administrateurs locaux.
    
- NT AUTHORITY\SYSTEM : compte système Windows disposant de privilèges locaux très élevés.
    
- Another User Context : contexte d'un autre utilisateur donnant accès à des ressources supplémentaires.
    

L'élévation de privilèges est une étape importante de la phase de Post-Exploitation. Elle peut permettre d'obtenir des identifiants, d'accéder à des données protégées, d'établir une persistance ou de poursuivre une attaque vers d'autres systèmes du réseau.

### 1. Comprendre la Privilege Escalation

#### Initial Foothold vs Privilege Escalation

Un Initial Foothold correspond à un premier accès obtenu sur un système, souvent avec des privilèges limités.

La Privilege Escalation cherche ensuite à étendre les capacités associées à cet accès.

```
Initial Foothold
Standard User Access
        ↓
Local Enumeration
        ↓
Identify Misconfiguration / Vulnerability
        ↓
Privilege Escalation
        ↓
Local Administrator / SYSTEM
        ↓
Further Access & Post-Exploitation
```


#### Objectifs principaux

Le cours présente quatre situations dans lesquelles l'élévation de privilèges peut être nécessaire.

|Objectif|Description|
|---|---|
|Gold Image Assessment|Évaluer la sécurité d'une configuration Windows standardisée utilisée pour déployer plusieurs machines|
|Local Resource Access|Obtenir les privilèges nécessaires pour accéder à une ressource locale, comme une base de données|
|Active Directory Foothold|Obtenir un contexte privilégié sur une machine jointe au domaine pour poursuivre l'investigation dans l'environnement AD|
|Credential Access & Lateral Movement|Récupérer des identifiants ou secrets d'authentification permettant d'accéder à d'autres systèmes|

L'élévation de privilèges peut constituer l'objectif final d'une mission, mais elle sert souvent d'étape intermédiaire vers d'autres ressources.

#### Notions préalables — Windows Security Context

Il est important de distinguer plusieurs concepts avant d'étudier les techniques d'exploitation.

|Concept|Explication|
|---|---|
|Standard User|Compte disposant de permissions limitées|
|Local Administrator|Compte membre du groupe Administrators sur une machine|
|NT AUTHORITY\SYSTEM|Identité système utilisée notamment par les services Windows|
|Access Token|Structure de sécurité associée à un processus ou thread, contenant notamment l'identité, les groupes et les privilèges|
|User Rights / Privileges|Droits particuliers comme `SeDebugPrivilege` ou `SeImpersonatePrivilege`|
|UAC (User Account Control)|Mécanisme contrôlant l'utilisation de certains privilèges administratifs|

Distinction essentielle : être membre du groupe local Administrators et exécuter un processus en tant que `NT AUTHORITY\SYSTEM` ne sont pas exactement la même chose.

De même, SYSTEM sur une machine jointe au domaine ne signifie pas Domain Admin. Lorsqu'un processus SYSTEM accède à certaines ressources réseau, il peut utiliser l'identité du compte ordinateur, mais cela ne lui accorde pas automatiquement des privilèges administratifs sur le domaine.

### 2. Main Windows Privilege Escalation Techniques

Windows présente une surface d'attaque importante, comprenant les comptes utilisateurs, services, fichiers, permissions et composants du système.

Le cours introduit plusieurs grandes catégories :

|Technique|Principe|
|---|---|
|Windows Group Privilege Abuse|Exploiter les droits associés à certains groupes Windows|
|Windows User Privilege Abuse|Exploiter des privilèges particuliers attribués à un compte ou à un token|
|UAC Bypass|Contourner certains mécanismes de contrôle de l'élévation administrative|
|Weak Service / File Permissions|Exploiter des permissions trop permissives sur des services ou fichiers|
|Kernel Exploitation|Exploiter une vulnérabilité non corrigée du noyau Windows|
|Credential Theft|Récupérer des secrets d'authentification pour obtenir davantage d'accès|
|Traffic Capture|Observer certaines communications réseau pouvant exposer des informations sensibles|

#### Manual Enumeration vs Automated Tools

De nombreux outils facilitent la recherche de vulnérabilités et de mauvaises configurations.

Cependant, le cours insiste sur la nécessité de maîtriser également l'énumération manuelle, à l'aide de PowerShell et des commandes Windows.

Cette compétence devient indispensable dans certains environnements :

- accès Internet interdit ;
    
- ports USB bloqués ;
    
- filtrage réseau strict ;
    
- poste de travail administré et fortement restreint ;
    
- impossibilité d'importer des scripts ou des exécutables.
    

Principe : comprendre les mécanismes Windows est plus important que dépendre exclusivement d'un outil d'énumération automatique.

### 3. Scenario 1 — Contourner les restrictions réseau

#### Contexte

Lors d'une mission de Pentest, l'analyste travaille sur un système client soumis à plusieurs restrictions :

- aucun accès Internet ;
    
- ports USB désactivés ;
    
- impossibilité de connecter directement sa machine d'attaque au réseau utilisateur ;
    
- présence de contrôles d'accès réseau.
    

Cependant, une erreur de configuration permet au Printer VLAN de communiquer vers l'extérieur sur certains ports :

`80`, `443` et `445`.

#### Chaîne d'attaque présentée

L'analyste réalise une énumération manuelle et identifie une faiblesse de permissions permettant une élévation locale.

L'accès privilégié obtenu lui permet ensuite de réaliser un dump mémoire du processus Windows `LSASS`.

Le fichier est transféré au moyen d'un partage SMB accessible via le VLAN des imprimantes.

L'analyse hors ligne avec Mimikatz révèle le hash NTLM d'un compte Domain Admin. Le hash est ensuite cassé hors ligne, permettant d'obtenir les identifiants nécessaires pour accéder au contrôleur de domaine.

```
Restricted Windows Workstation
           ↓
Manual Enumeration
           ↓
Weak Permissions Discovered
           ↓
Local Privilege Escalation
           ↓
LSASS Memory Dump
           ↓
SMB Transfer via Printer VLAN
           ↓
Offline Mimikatz Analysis
           ↓
Domain Admin NTLM Hash
           ↓
Offline Password Cracking
           ↓
Domain Controller Access
```


#### Notions importantes

- LSASS — Local Security Authority Subsystem Service : Processus Windows chargé de nombreuses fonctions liées à la sécurité et à l'authentification. Sa mémoire peut contenir des informations d'authentification sensibles selon les sessions et les protections configurées.

- NTLM Hash : Représentation cryptographique dérivée d'un mot de passe Windows, utilisée dans certains mécanismes d'authentification. Un hash NTLM n'est pas le mot de passe en clair. Certaines attaques peuvent toutefois exploiter directement le hash ou tenter de retrouver le mot de passe d'origine.

SMB — Server Message Block : Protocole principalement utilisé pour accéder aux fichiers et ressources partagés sur un réseau Windows, généralement sur TCP `445`.

#### Enseignement du scénario

Même lorsqu'un poste est fortement verrouillé, une faiblesse locale combinée à une erreur de segmentation réseau peut permettre de progresser vers des ressources beaucoup plus sensibles.

### 4. Scenario 2 — Piller les partages ouverts

#### Contexte

L'environnement est correctement surveillé, avec peu de vulnérabilités apparentes.

L'analyste découvre cependant un partage réseau insuffisamment protégé, accessible en lecture à l'ensemble des utilisateurs.

Ce partage contient des sauvegardes de machines virtuelles.

#### Virtual Disk Files

Le cours mentionne deux formats :

- `.VMDK` : disque virtuel couramment utilisé dans les environnements VMware.
    
- `.VHDX` : format de disque virtuel Microsoft, notamment utilisé avec Hyper-V.
    

Ces fichiers peuvent contenir l'intégralité du système de fichiers d'une machine virtuelle, y compris des artefacts sensibles.

#### Chaîne d'attaque

L'analyste accède à une sauvegarde `.VHDX`, la monte sur une machine Windows et récupère trois ruches de registre :

- `SYSTEM`
    
- `SAM`
    
- `SECURITY`
    

Il utilise ensuite `secretsdump.py`, un outil de la suite Impacket, pour extraire le hash du compte administrateur local.

L'organisation ayant déployé ses systèmes à partir d'une Gold Image partageant les mêmes identifiants administratifs locaux, le hash permet d'obtenir un accès administrateur sur de nombreuses machines via une attaque Pass-the-Hash.

```
Overly Permissive Network Share
             ↓
VM Backups Exposed
             ↓
VHDX File Retrieved & Mounted
             ↓
SYSTEM / SAM / SECURITY Hives
             ↓
Offline Secrets Extraction
             ↓
Local Administrator NTLM Hash
             ↓
Pass-the-Hash
             ↓
Administrative Access on Multiple Hosts
```


#### Windows Registry Hives — Prérequis

Une Registry Hive est un ensemble de données constituant une partie du registre Windows.

|Hive|Rôle dans ce scénario|
|---|---|
|SAM|Contient des informations relatives aux comptes locaux et à leurs hashes de mots de passe|
|SYSTEM|Contient notamment des informations nécessaires au déchiffrement de certains secrets stockés localement|
|SECURITY|Contient des informations et secrets associés à la configuration de sécurité locale|

Ces ruches sont particulièrement sensibles lors d'une investigation ou d'un Pentest.

#### Pass-the-Hash — Concept

Le Pass-the-Hash (PtH) est une technique permettant, dans certains contextes d'authentification NTLM, d'utiliser un hash de mot de passe sans connaître le mot de passe en clair.

Dans cet exemple, l'attaque devient possible à grande échelle parce que plusieurs postes partagent le même secret d'administrateur local.

Enseignement du scénario : un partage contenant des sauvegardes accessibles à tous peut exposer indirectement les secrets d'authentification d'un grand nombre de systèmes.

### 5. Scenario 3 — Chasse aux identifiants et abus des privilèges de compte

#### Contexte

L'objectif de la mission consiste à accéder à des serveurs de bases de données critiques.

L'analyste dispose initialement :

- d'un ordinateur portable fourni par le client ;
    
- d'un compte utilisateur standard du domaine ;
    
- de la possibilité d'exécuter des outils.
    

#### Snaffler — Credential Hunting

L'outil Snaffler est utilisé pour rechercher des informations sensibles dans les partages réseau accessibles.

L'analyste découvre des fichiers `.sql` contenant des identifiants de base de données à faibles privilèges.

Ces identifiants permettent d'établir une connexion au serveur Microsoft SQL Server (MSSQL).

#### MSSQL & xp_cmdshell

La procédure stockée `xp_cmdshell` permet à SQL Server d'exécuter des commandes au niveau du système d'exploitation.

Dans le scénario, l'analyste parvient à activer et utiliser cette fonctionnalité.

Cela lui permet d'obtenir une exécution de commandes dans le contexte d'un compte associé au service SQL Server.

Précision : l'utilisation de `xp_cmdshell` dépend des permissions SQL disponibles. Elle n'est pas automatiquement accessible à n'importe quel compte de base de données.

#### SeImpersonatePrivilege

L'analyste découvre que le compte dispose du privilège :

`SeImpersonatePrivilege`

Ce droit permet à un processus d'usurper, sous certaines conditions, le contexte de sécurité d'un autre utilisateur à travers des mécanismes d'impersonation Windows.

Il est particulièrement intéressant en recherche d'élévation locale, car certaines techniques exploitent les mécanismes d'impersonation pour obtenir un contexte plus privilégié.

#### Juicy Potato

Le cours utilise Juicy Potato pour exploiter la situation et obtenir davantage de privilèges.

L'analyste réussit à créer un utilisateur administrateur local.

Cette méthode n'était pas son premier choix : il avait auparavant tenté d'obtenir un Beacon / Reverse Shell, sans succès.

Il peut finalement se connecter à distance au serveur de base de données et obtenir le contrôle de la base de données cible.

#### Chaîne d'attaque

```
Standard Domain User
          ↓
Snaffler — Network Share Enumeration
          ↓
SQL Files with Credentials
          ↓
MSSQL Access
          ↓
xp_cmdshell
          ↓
OS Command Execution
          ↓
SeImpersonatePrivilege
          ↓
Juicy Potato
          ↓
Local Administrator Access
          ↓
RDP to Database Server
          ↓
Control of Target Database
```


Précision technique : Juicy Potato ne fonctionne pas universellement sur toutes les versions de Windows. Son efficacité dépend notamment du système, des privilèges du processus et des mécanismes d'impersonation disponibles.

#### Enseignement du scénario

Une compromission peut résulter de l'enchaînement de plusieurs faiblesses distinctes :

Identifiants exposés → Accès SQL → Exécution de commandes → Abus de privilèges Windows → Accès administrateur.

L'exploitation n'exige donc pas nécessairement une seule vulnérabilité critique : plusieurs mauvaises configurations peuvent suffire.

### 6. Why Does Privilege Escalation Happen?

Les possibilités d'élévation de privilèges résultent souvent de faiblesses organisationnelles et techniques.

Le cours identifie notamment :

- Insufficient Staffing : manque de personnel dédié à la sécurité.
    
- Budget Constraints : ressources financières insuffisantes.
    
- Incomplete Patch Management : systèmes et applications non corrigés.
    
- Weak Vulnerability Management : gestion insuffisante des vulnérabilités.
    
- Lack of Internal Assessments : absence d'audits et de tests réguliers.
    
- Insufficient Monitoring : surveillance incomplète.
    
- Outdated Infrastructure : postes et serveurs anciens ou insuffisamment maintenus.
    
- Insecure File Shares : permissions trop permissives.
    
- Exposed Credentials : identifiants présents dans des scripts ou fichiers de configuration.
    

Ces faiblesses peuvent rester longtemps inaperçues, notamment lorsqu'une organisation ne dispose pas des moyens nécessaires pour auditer régulièrement son environnement.

### 7. Key Takeaways

|Scénario|Faiblesse principale|Résultat|
|---|---|---|
|Network Restrictions|Permissions locales faibles + segmentation réseau insuffisante|LSASS Dump, récupération d'identifiants et accès au domaine|
|Open Shares|Sauvegardes de VM accessibles + réutilisation de secrets locaux|Extraction de hashes et Pass-the-Hash|
|Credential Hunting|Identifiants SQL exposés + abus de privilèges système|Élévation locale et accès au serveur de base de données|

Les trois études de cas illustrent un principe central du Windows Privilege Escalation : une élévation de privilèges résulte souvent d'une chaîne de mauvaises configurations et d'accès excessifs, plutôt que d'une vulnérabilité isolée.

Pour les prochaines sections, les fondamentaux à maîtriser seront donc particulièrement importants : Windows Access Tokens, User Privileges, Group Memberships, ACLs, Services, Credentials et mécanismes d'authentification Windows.

La maîtrise de ces concepts permet d'identifier les chemins d'élévation de privilèges, y compris dans les environnements fortement restreints où les outils automatisés ne sont pas disponibles.

## Sommaire

- [Outils utiles](01-outils-utiles.md)
- [Situational Awareness](02-situational-awareness.md)
- [Énumération Initiale](03-enumeration-initiale.md)
