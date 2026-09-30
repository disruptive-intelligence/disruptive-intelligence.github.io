---
title: HTB — Windows System Security
source: IT/02_Windows/HTB_Windows System Sécurity.md
---

### Comptes utilisateur et gestion
- Un **compte utilisateur** représente une identité dans Windows pour une personne ou un service.
- Il est généralement associé à :
    - un username ;
    - un password ;
    - des permissions ;
    - des appartenances à des groupes.
```
Identity
→ User Account
→ Groups
→ Permissions / Privileges
```
#### Comptes Administrateur
- Les comptes administrateur disposent de privilèges élevés sur le système.
- Ils peuvent notamment :
    - modifier des paramètres système ;
    - installer/configurer des logiciels ;
    - gérer d’autres comptes ;
    - accéder à davantage de ressources.
> Un compte administrateur ne devrait pas être utilisé pour les tâches quotidiennes lorsqu’un compte standard suffit.
#### Comptes utilisateur standard
- Permettent notamment :
    - d’exécuter des applications ;
    - de gérer les fichiers personnels ;
    - de modifier certains paramètres utilisateur.
- Les modifications globales du système sont limitées.
```
Standard User
→ usage quotidien

Administrator
→ opérations privilégiées
```
##### Gestion des utilisateurs locaux
- Sous Windows Server :
	- L'écran Démarrer -> Gestion de l'ordinateur -> Utilisateurs et groupes locaux -> Utilisateurs s'ouvre :
<img src="../../assets/w_gestion_user.png" alt="W User" width="600">
- Les principaux users par défaut fournis avec Windows Server sont : 
<img src="../../assets/w_user_account.png" alt="W Account" width="600">
- Pour créer un nouvel user local puis de le supprimer.
<img src="../../assets/w_user_create.png" alt="W Create" width="500">
<img src="../../assets/w_user_delete.png" alt="W Delete" width="500">
> Les **Local Users and Groups** concernent les comptes stockés localement sur une machine, pas les comptes Active Directory du domaine.
#### Permissions et autorisations des utilisateurs
##### Principe du moindre privilège - Principle of Least Privilege
- Accorder uniquement les permissions réellement nécessaires en appliquant le niveau de privilèges le plus bas possible.
- Éviter :
    - droits administrateur inutiles ;
    - permissions excessives ;
    - accès permanent à des ressources sensibles.
##### Limiter les comptes administrateur
- Réduire le nombre de comptes à privilèges.
- Réserver leur usage aux tâches qui nécessitent réellement une élévation.
- Bonnes pratiques :
	- compte standard pour le quotidien ;
	- compte admin dédié ;
	- MFA pour les comptes privilégiés ;
	- monitoring renforcé.
#### Politiques de sécurité
##### Politiques de mot de passe
###### Strong Passwords
Le cours recommande :
- au moins 12 caractères ;
- lettres ;
- chiffres ;
- caractères spéciaux.
Complément utile :
> La **longueur** et l’absence de mot de passe compromis sont généralement plus importantes qu’une complexité artificielle excessive.
###### Changement périodique
Le cours recommande un changement périodique des mots de passe.
> ⚠️ Les recommandations modernes déconseillent souvent la rotation forcée fréquente **sans signe de compromission**, car elle pousse les utilisateurs à choisir des mots de passe prévisibles. 

Un changement doit surtout être imposé en cas de :
- fuite ;
- compromission ;
- suspicion ;
- exigence réglementaire spécifique.
##### 2FA / MFA 
- Ajouter un second facteur réduit fortement le risque lié au vol de mot de passe.
- Exemples :
	- authenticator app ;
	- security key ;
	- OTP ;
	- biométrie.
##### UAC — User Account Control - Contrôle de compte user
- **UAC** limite l’élévation de privilèges automatique.
- Lorsqu’une application demande des droits administrateur, Windows affiche une demande de consentement ou de credentials.
```
Application
→ demande élévation
→ UAC prompt
→ Approve / Deny
```
> UAC n’est pas une barrière de sécurité absolue, mais une couche importante pour limiter les élévations involontaires.
##### Session Timeout / Screen Lock
- Configurer :
    - verrouillage automatique ;
    - expiration de session ;
    - demande d’authentification au retour.
##### Audit et surveillance des comptes
- Activer la journalisation des événements liés aux comptes et authentifications.
- Surveiller notamment :
    - connexions réussies/échouées ;
    - création/suppression de comptes ;
    - changements de mot de passe ;
    - modifications de groupes ;
    - élévations de privilèges.
#### Groupes et gestion
- Un **groupe** contient un ou plusieurs utilisateurs.
- Il permet d’attribuer des droits collectivement plutôt qu’utilisateur par utilisateur.
```
Users
  ↓
Group
  ↓
Permissions
```
- Avantage principal :
```
Add user to group
→ inherits group permissions

Remove user
→ permissions removed
```
##### Groupes locaux
- Définis sur **une seule machine**.
- Utilisés pour contrôler l’accès aux ressources locales.
Exemple :
```
Local Administrators
Remote Desktop Users
Backup Operators
```
###### Créer groupe local 
<img src="../../assets/w_user_local.png" alt="W Local" width="600">
###### Groupes locaux par défaut fournis avec Windows Server
<img src="../../assets/w_group_locaux.png" alt="W Group Local" width="400">
##### Groupes de domaine Active Directory
- Gérés dans **Active Directory**.
- Utilisés pour contrôler l’accès aux ressources de plusieurs systèmes du domaine.
- Les membres d'un groupe peuvent disposer de certains privilèges par le biais de stratégies de groupe.
- L'ajout ou la suppression d'un utilisateur d'un groupe est un moyen simple de modifier rapidement les privilèges d'un utilisateur.
```
AD User
→ Domain Group
→ Access to shared resources
```
###### Groupes fournis avec le rôle AD de Windows Server
<img src="../../assets/w_group_ad1.png" alt="W Group AD1" width="400">
<img src="../../assets/w_group_ad2.png" alt="W Group AD2" width="400">
###### Types de groupes Active Directory
- Domain Local
	- Utilisé principalement pour attribuer des permissions sur des ressources du domaine concerné.
- Global
	- Regroupe surtout des utilisateurs/comptes ayant un rôle commun dans le même domaine.
- Universal
	- Peut contenir des membres provenant de plusieurs domaines d’une forêt.
```
Global Group
→ regroupe les utilisateurs

Domain Local Group
→ reçoit les permissions

Universal Group
→ utile entre plusieurs domaines
```
Complément utile : modèle classique **AGDLP** :
```
Accounts
→ Global Groups
→ Domain Local Groups
→ Permissions
```
##### Relation utilisateur-groupe
###### Ajout / suppression
- L’appartenance aux groupes doit suivre un processus contrôlé :
    - demande ;
    - validation ;
    - ajout ;
    - suppression lorsque le besoin disparaît.
###### Revue des appartenances
- Vérifier régulièrement :
    - qui appartient à quel groupe ;
    - pourquoi ;
    - si cet accès est encore nécessaire.
- Particulièrement important pour les groupes sensibles :
	- Administrators
	- Domain Admins
	- Enterprise Admins
	- Remote Desktop Users
	- Backup Operators

## Sécurité Active Directory 
- Active Directory est un service d'annuaire Microsoft utilisé pour centraliser la gestion des identités, groupes, ordinateurs et ressources dans un environnement Windows.
#### Gestion centralisée des identités
- Gestion centralisée des comptes utilisateurs et credentials.
- Une même identité peut être utilisée pour accéder à plusieurs ressources du domaine.
- Permet d’appliquer plus facilement :
    - password policies ;
    - autorisations ;
    - contrôles de sécurité.
#### Gestion centralisée des ressources
- facilite la configuration et la mise à jour régulières des ressources ainsi que le contrôle des droits d'accès.
- AD permet de gérer notamment :
	- utilisateurs ;
	- groupes ;
	- ordinateurs ;
	- serveurs ;
	- shared folders ;
	- imprimantes ;
	- autres ressources réseau.
#### Stratégie de groupe
- Les stratégies de groupe sont utilisées pour gérer de manière centralisée les paramètres de configuration des utilisateurs et des ordinateurs.
- Ces stratégies incluent des paramètres de sécurité, des paramètres de bureau, des paramètres d'application, et plus encore.
#### Group Policy — GPO
- Les **Group Policies** permettent de configurer centralement les utilisateurs et ordinateurs du domaine.
- Elles peuvent gérer :
    - paramètres de sécurité ;
    - configuration système ;
    - desktop settings ;
    - paramètres applicatifs.
```
Active Directory
      ↓
     GPO
      ↓
Users / Computers
→ configuration homogène
```
#### Concepts de base AD

| Concept    | Rôle                                                                        |
| ---------- | --------------------------------------------------------------------------- |
| **Domain** | Unité logique contenant utilisateurs, ordinateurs, groupes et autres objets |
| **OU**     | Regrouper et gérer les objets au sein du domaine de manière plus organisée. |
| **Group**  | Regroupement logique permettant notamment d’attribuer des permissions       |
| **Object** | Élément stocké dans AD : user, computer, group, printer, OU…                |

##### Objet 
- Éléments de base dans Active Directory. Les utilisateurs, les ordinateurs, les imprimantes, les groupes, les OU et d'autres objets constituent les blocs de construction de la base de données dans Active Directory.
##### Domain
- Le domaine est utilisé comme l'unité de gestion de base d'un réseau.
- Les comptes d'utilisateurs, les groupes, les comptes d'ordinateurs et d'autres objets se trouvent dans le domaine, qui fournit une authentification et un contrôle d'accès communs.
- Fournit notamment un cadre commun pour :
    - authentification ;
    - gestion ;
    - contrôle d’accès.
##### Organizational Unit — OU
- L'unité d'organisation (Organizational Unit ou OU) est utilisée pour regrouper et gérer les objets au sein du domaine de manière plus organisée.
- Utile pour :
    - délégation d’administration ;
    - organisation logique ;
    - application de GPO.
> **OU ≠ Security Group** : une OU sert surtout à organiser/déléguer/appliquer des GPO, tandis qu’un groupe sert notamment à attribuer des permissions.
##### Groupes 
- Les groupes sont utilisés pour regrouper logiquement des utilisateurs ou des ordinateurs.
- Le regroupement d'utilisateurs par caractéristiques ou fonctions similaires facilite la gestion des droits d'accès et des autorisations.
#### Comptes par défaut — Default Accounts
- Certains comptes sont créés automatiquement, par exemple :
    - `Administrator` ;
    - `Guest`.
- Leur existence et leur nom étant prévisibles, ils représentent des cibles évidentes pour les attaquants.
Bonnes pratiques :
- désactiver les comptes inutiles ;
- contrôler régulièrement leurs privilèges ;
- ne pas les utiliser pour les tâches quotidiennes ;
- surveiller leurs activités ;
- utiliser des comptes nominatifs lorsque possible.
```
Default Account
→ Known identity
→ High-value target
→ Restrict + Monitor
```
> Un nom de compte connu n’est pas en lui-même une vulnérabilité : le problème vient surtout de **privilèges élevés, credentials faibles, mauvaise surveillance ou utilisation permanente**.
#### Groupes privilégiés
Les groupes comme :
```
Domain Admins
Enterprise Admins
```
disposent de privilèges extrêmement élevés sur l’environnement AD.
- Les comptes ordinaires ne doivent pas y appartenir.
- Leur nombre de membres doit être **minimal**.
- L’accès privilégié doit idéalement être accordé seulement lorsque nécessaire.
```
Standard User
      X
Domain Admins

Privileged Admin
→ accès uniquement si nécessaire
```
> ⚠️ Le compte `Administrator` intégré ne doit pas être considéré comme une exception à utiliser quotidiennement. Il doit lui aussi être fortement protégé et réservé aux usages réellement nécessaires.
##### Just-In-Time Privilege
- Le cours recommande d’ajouter temporairement un compte à `Domain Admins`, puis de le retirer une fois l’opération terminée.
- Conceptuellement :
```
Need Admin Privilege
→ Grant temporarily
→ Perform task
→ Remove privilege
```
→ approche proche du **Just-In-Time (JIT)**.
#### Séparer compte utilisateur et compte administrateur
- Pourquoi utiliser plusieurs comptes ? 
	- Séparation des privilèges ;
	- Limitation des attaques ;
	- Sécurité des données et du système.
- Un administrateur devrait posséder au minimum :
```
Account 1 → tâches quotidiennes
Account 2 → tâches administratives
```
##### Compte utilisateur standard
Utilisé pour :
- email ;
- Web ;
- bureautique ;
- tâches quotidiennes.
##### Compte administratif
Utilisé seulement pour :
- administration système ;
- installation/configuration ;
- opérations nécessitant des privilèges élevés.
Pourquoi ?
```
Daily Account compromised
→ privilèges limités

Admin Account compromised
→ impact potentiellement très élevé
```
→ la séparation réduit l’exposition des credentials privilégiés.
#### Stratégie d’audit — Audit Policy
- Les **Audit Policies** déterminent quels événements Windows sont enregistrés.
- Dans un domaine, elles peuvent être déployées via GPO sur les endpoints et serveurs.
- Chemin cité : « Configuration de l'ordinateur -> Stratégies -> Paramètres Windows -> Paramètres de sécurité -> Configuration avancée de la stratégie d'audit »
<img src="../../assets/w_audit.png" alt="W Audit" width="550">

| Catégorie              | Sous-catégorie                  | Audit             |
| ---------------------- | ------------------------------- | ----------------- |
| **Account Logon**      | Credential Validation           | Success + Failure |
| **Account Management** | Application Group Management    | Success + Failure |
|                        | Computer Account Management     | Success + Failure |
|                        | Other Account Management Events | Success + Failure |
|                        | Security Group Management       | Success + Failure |
|                        | User Account Management         | Success + Failure |
| **Detailed Tracking**  | PnP Activity                    | Success           |
|                        | Process Creation                | Success           |
| **Logon/Logoff**       | Account Lockout                 | Success + Failure |
|                        | Group Membership                | Success           |
|                        | Logoff                          | Success           |
|                        | Logon                           | Success + Failure |
|                        | Other Logon/Logoff Events       | Success + Failure |
|                        | Special Logon                   | Success           |
| **Object Access**      | Removable Storage               | Success + Failure |
| **Policy Change**      | Audit Policy Change             | Success + Failure |
|                        | Authentication Policy Change    | Success           |
|                        | Authorization Policy Change     | Success           |
| **Privilege Use**      | Sensitive Privilege Use         | Success + Failure |
| **System**             | IPsec Driver                    | Success + Failure |
|                        | Other System Events             | Success + Failure |
|                        | Security State Change           | Success           |
|                        | Security System Extension       | Success + Failure |
|                        | System Integrity                | Success + Failure |
##### Process Creation
- L’audit de création de processus est particulièrement intéressant pour le SOC :
```
User
→ launches powershell.exe
→ Process Creation Event
→ Security Log
→ SIEM / Detection
```
- Complément utile : sur Windows, l’Event ID fréquemment exploité est :
```
4688 → A new process has been created
```
- Avec une configuration adaptée, la **command line** peut également être enregistrée.
#### Windows LAPS
- **Windows LAPS — Local Administrator Password Solution** automatise la gestion des mots de passe des comptes administrateur locaux.
- Permet :
	- Simplifier gestion des MDP ;
	- Améliorer la sécurité des MDP ;
	- Prévenir les attaques.
- Problème classique sans LAPS :
```
PC01 → local Administrator / SamePassword
PC02 → local Administrator / SamePassword
PC03 → local Administrator / SamePassword
```
- Si le password est compromis :
```
→ lateral movement facilité
```

- Avec LAPS :
```
PC01 → RandomPassword-A
PC02 → RandomPassword-B
PC03 → RandomPassword-C
```
→ chaque machine possède idéalement un secret distinct.
##### Avantages et bonnes pratiques
- gestion centralisée ;
- génération de passwords forts ;
- rotation automatique ;
- limitation de la réutilisation ;
- réduction du risque lié aux mots de passe locaux statiques.
```
Unique Password
+
Automatic Rotation
+
Restricted Retrieval
→ Local Admin Risk ↓
```
###### Point important
Le password LAPS doit être :
- accessible uniquement aux comptes autorisés ;
- protégé par les ACL appropriées ;
- audité lors de sa consultation.
> Les logs doivent tracer les **rotations et accès au secret**, pas exposer le mot de passe en clair.
#### Password Policy dans Active Directory
Une politique de mot de passe peut définir :
- longueur minimale ;
- complexité ;
- historique ;
- durée de vie ;
- account lockout après échecs répétés.
```
Password Policy
├─ Minimum Length
├─ Complexity
├─ Password History
├─ Maximum Age
└─ Account Lockout
```
###### Complexité
Le cours recommande de combiner :
- uppercase ;
- lowercase ;
- numbers ;
- symbols.
> En pratique, une **longueur suffisante** et le blocage des mots de passe faibles/compromis sont souvent plus importants qu’une complexité artificielle excessive.
##### Password History
- Empêche l’utilisateur de réutiliser immédiatement ses anciens passwords.
```
Password1
→ Password2
→ Password3

X Password1
```
##### Stratégie de verrouillage de compte - Account Lockout
- Une **Account Lockout Policy** verrouille temporairement un compte après un certain nombre de tentatives d’authentification échouées.
- Objectif principal : limiter les attaques de type **brute force** et rendre les tentatives répétées plus coûteuses pour l’attaquant.
```
Failed Login × N
→ Account Lockout
→ accès temporairement bloqué
```
Avantages :
- ralentit les attaques par mot de passe ;
- empêche les tentatives illimitées ;
- les verrouillages répétés peuvent servir d’**indicateur d’attaque**.
> ⚠️ **Nuance hors cours :** une lockout policy protège surtout contre les attaques nécessitant des essais de password. Elle n’empêche pas directement un **Pass-the-Hash**, puisque celui-ci réutilise un hash NTLM déjà compromis plutôt que de deviner le mot de passe.

→ peut réduire l’efficacité du brute force online, mais les seuils doivent être configurés pour éviter de faciliter un **DoS par verrouillage de comptes**.
<img src="../../assets/w_lockout.png" alt="W Lockout" width="550">
###### Étapes de création d'une stratégie de mot de passe dans Active Directory
- Ouvrez les Outils d'administration Active Directory et sélectionnez Gestion des stratégies de groupe.
- Pour gérer les mots de passe, accédez aux Stratégies de mot de passe.
- Créez une nouvelle stratégie de mot de passe et nommez-la.
- Spécifiez le niveau de complexité que vous exigez dans la stratégie de mot de passe. Par exemple, l'utilisation de lettres majuscules, de lettres minuscules, de chiffres et de symboles.
- Spécifiez la période de validité du mot de passe. Le mot de passe sera alors désactivé et l'utilisateur aura besoin de l'aide d'un administrateur pour le réactiver. Cela garantit que le mot de passe est changé régulièrement.
- Spécifiez le nombre minimum de fois que les utilisateurs doivent se souvenir de leurs mots de passe précédents. Cela empêche la réutilisation d'anciens mots de passe.
- Définissez des limites de temps ou le verrouillage des comptes à la suite de tentatives de saisie de mots de passe incorrects.
<img src="../../assets/w_length.png" alt="W Length" width="550">

#### SAW — Secure Admin Workstation
- Une **Secure Admin Workstation** est une machine dédiée exclusivement aux opérations administratives utilisant des comptes privilégiés.
```
Daily Workstation
→ Web / Email / Office

SAW
→ Administration uniquement
→ Privileged Accounts
```
- Objectif : empêcher que des credentials administratifs soient exposés sur une workstation utilisée pour des activités plus risquées comme le Web ou les emails.
##### Caractéristiques d’une SAW
###### Environnement isolé
- Séparé des usages utilisateur classiques.
- Réseau et configuration adaptés aux opérations administratives.
###### Pas d’accès Internet
- Ne pas utiliser la SAW pour :
    - consulter ses emails ;
    - naviguer sur Internet ;
    - effectuer des tâches quotidiennes.
###### Authentification forte
- Comptes privilégiés fortement protégés.
- Utilisation de :
    - passwords robustes ;
    - MFA lorsque possible.
###### Applications minimales
- Installer uniquement les outils nécessaires à l’administration.
- Supprimer les logiciels inutiles afin de réduire l’**Attack Surface**.
###### Patching
- OS et applications maintenus à jour.
- Correctifs de sécurité appliqués régulièrement.
```
SAW
→ Isolated
→ No Web / Email
→ MFA
→ Minimal Software
→ Fully Patched
```
##### Avantages d’une SAW
- réduit l’exposition des comptes privilégiés ;
- diminue le risque de malware/ransomware ;
- facilite le contrôle des opérations administratives ;
- améliore la surveillance des activités privilégiées.
#### Support du système d’exploitation
- Utiliser des versions Windows encore **supportées** est essentiel.
- Un OS **End-of-Life / End-of-Support** ne recevant plus de security patches augmente fortement le risque.
#### Gestion des comptes de service
- Les **Service Accounts** sont utilisés par des applications, services ou systèmes pour fonctionner automatiquement.
- Ils représentent une cible importante car ils peuvent :
    - disposer de privilèges élevés ;
    - avoir des passwords rarement modifiés ;
    - accéder à plusieurs ressources.
##### Bonnes pratiques
###### Un compte par service
```
Service A → Account A
Service B → Account B
```
→ éviter les comptes partagés entre plusieurs services, garantit l'isolement.
Cela facilite :
- isolation ;
- auditing ;
- révocation ;
- limitation de l’impact d’une compromission.
###### Least Privilege
- Un compte de service ne doit posséder que les droits indispensables.
```
Service Account
→ Required Resources Only
→ Required Permissions Only
```
###### Gestion des credentials
- Utiliser des secrets forts.
- Automatiser leur rotation lorsque possible.
- Préférer des mécanismes de **managed service accounts** lorsqu’ils sont disponibles.
###### Restreindre le réseau
- Limiter les systèmes auxquels le compte peut accéder.
- Bloquer les communications inutiles.
###### Monitoring
Surveiller :
- authentifications inhabituelles ;
- nouvelles machines sources ;
- horaires anormaux ;
- accès inhabituels ;
- modifications de privilèges.
###### Patch Management
- Maintenir à jour les systèmes et applications exécutant ces comptes.
#### Surveillance des modifications utilisateurs / groupes 
- Les modifications AD importantes doivent être auditées :
```
User Created
User Deleted
Password Changed / Reset
Group Membership Changed
Privilege Changed
```
- Les Domain Controllers enregistrent ces opérations dans leurs **Event Logs**.
- Cependant, dans les réseaux à grande échelle, la surveillance manuelle de ces journaux d'événements peut être difficile et prendre beaucoup de temps, il est important d'avoir un SIEM :
```
Domain Controller Logs
        ↓
       SIEM
        ↓
Correlation / Alerting
```
Le SIEM facilite :
- centralisation ;
- analyse ;
- détection d’anomalies ;
- génération d’alertes.
##### Événements sensibles
- Exemples particulièrement importants à surveiller :
```
New User Created
→ vérifier légitimité

User added to privileged group
→ High Priority

Account Disabled / Deleted
→ vérifier origine

Password Reset
→ vérifier initiateur
```
- Le changement d’appartenance à des groupes comme :
```
Domain Admins
Enterprise Admins
Administrators
```
-> doit recevoir une attention particulière.
###### Tableau user
<img src="../../assets/w_act-user.png" alt="W Act User" width="400">
###### Tableau group
<img src="../../assets/w_act-group.png" alt="W Act Group" width="400">
##### Contrôle de l'appartenance au groupe d'admin. locaux
- Un membre du groupe local **Administrators** possède des privilèges élevés sur la machine.
- Il peut notamment :
    - installer des logiciels ;
    - modifier la configuration ;
    - gérer les comptes ;
    - désactiver certaines protections ;
    - accéder à des données locales sensibles.
```
Standard User
      X
Local Administrators
```
Les utilisateurs standards ne devraient pas disposer de droits admin locaux sans nécessité métier.
<img src="../../assets/w_local_admin.png" alt="W Local Admin" width="550">
###### Risque des Local Admin Rights
- Une compromission d’un compte administrateur local peut permettre à l’attaquant de :
```
Execute as Admin
→ Disable Security Controls
→ Dump Credentials
→ Establish Persistence
→ Attempt Lateral Movement
```
→ supprimer les droits locaux inutiles réduit donc fortement l’impact potentiel d’une compromission.
###### Gestion centralisée
- Le cours recommande de contrôler les appartenances au groupe `Administrators` via des mécanismes centralisés, notamment **Group Policy**.
```
GPO
→ Local Administrators Membership
→ Centralized Enforcement
```
Sinon, une modification locale peut réintroduire des privilèges qui avaient été supprimés manuellement.
### Sécurité DNS sous Windows
- Le **DNS — Domain Name System** traduit les noms de domaine en adresses IP.
- Sous Windows Server, le rôle DNS est souvent étroitement intégré à **Active Directory**.
- Sa compromission peut permettre :
    - redirection vers des sites malveillants ;
    - empoisonnement / usurpation DNS ;
    - interruption de service ;
    - modification des enregistrements ;
    - collecte d’informations sur l’infrastructure.
```
Client
→ Query DNS
→ DNS Server
→ IP Address
→ Target Service
```
#### Restriction des transferts de zones
- Une **zone DNS** contient les enregistrements associés à un espace de noms.
- Exemples :
```
A
AAAA
CNAME
MX
NS
TXT
PTR
```
-> Les transferts de zone permettent de synchroniser les données entre serveurs DNS.
##### AXFR — Full Zone Transfer
- Copie **l’ensemble de la zone DNS**.
```
Primary DNS
→ AXFR
→ Secondary DNS
```
Utilisé notamment lors :
- de l’initialisation d’un serveur secondaire ;
- d’une synchronisation complète ;
- lorsque le serveur de sauvegarde est complétement redémarré.
##### IXFR — Incremental Zone Transfer
- Transmet seulement les **modifications** depuis la dernière version connue.
```
Zone v10
→ modifications
→ IXFR
→ Zone v11
```
Avantages :
- moins de trafic ;
- synchronisation plus efficace.
###### Risque de sécurité
- Si un transfert de zone est autorisé à n’importe qui :
```
Attacker
→ AXFR
→ récupération de nombreux DNS records
```
L’attaquant peut découvrir :
- tous les enregistrements du serveur DNS ;
- hostnames ;
- serveurs internes ;
- mail servers ;
- noms de services ;
- informations utiles pour la reconnaissance.
→ limiter les transferts aux **serveurs DNS secondaires autorisés**.
Sous Windows Server :
```
DNS Manager
→ Zone Properties
→ Zone Transfers
→ Allow zone transfers
→ Only to the following servers
```

**Complément :** un zone transfer sert surtout à la **réplication entre serveurs DNS autoritatifs** ; ce n’est pas en lui-même un mécanisme de load balancing.
#### DNSSEC
**DNSSEC — Domain Name System Security Extensions** permet de vérifier :
- l’**authenticité** des données DNS ;
- leur **intégrité**.
Il repose sur des **signatures cryptographiques**.
```
DNS Record
+
Digital Signature
→ Validation
```
Objectif :
```
Réponse DNS reçue
→ provient-elle bien de la chaîne de confiance attendue ?
→ a-t-elle été modifiée ?
```
DNSSEC aide notamment à limiter certains scénarios de :
- DNS spoofing ;
- DNS cache poisoning.
<img src="../../assets/w_dnsec.png" alt="W DNSEC" width="400">
<img src="../../assets/w_dnsec_2.png" alt="W DNSEC" width="400">
<img src="../../assets/w_dnsec_3.png" alt="W DNSEC" width="400">
##### Limites de DNSSEC
- DNSSEC peut être complexe à mettre en œuvre et à gérer, et utiliser plus de ressources système. Par conséquent, une mise en œuvre de DNSSEC doit être soigneusement planifiée et gérée.
- configuration plus complexe ;
- gestion des clés/signatures ;
- consommation supplémentaire de ressources ;
- maintenance nécessaire.
> **Complément : DNSSEC ne chiffre pas les requêtes DNS.** Il apporte principalement **authenticité + intégrité**, pas la confidentialité du trafic.
```
DNSSEC
→ Authenticity
→ Integrity

DNSSEC ≠ Encryption
```
#### Surveillance du serveur DNS
- Windows Server fournit des événements DNS dans :
```
Event Viewer
→ Applications and Services Logs
→ Microsoft
→ Windows
→ DNS-Server
→ Audit
```
La surveillance permet de détecter :
- modifications de zones ;
- changements d’enregistrements ;
- activités administratives anormales ;
- comportements pouvant indiquer un détournement DNS.
<img src="../../assets/w_dns_sur.png" alt="W DNS Sur" width="400">
##### DNS Hijacking
- Le **DNS Hijacking** consiste à détourner le mécanisme de résolution DNS afin de rediriger les utilisateurs vers une destination contrôlée par l’attaquant.
- Exemple :
```
DNS Record légitime
example.com → 10.0.0.10

Attaquant modifie le record
example.com → 10.0.0.99
```
→ les clients suivent ensuite la résolution falsifiée.
- Cela peut provenir notamment d’une modification :
	- des DNS records ;
	- de la configuration DNS ;
	- du serveur utilisé pour la résolution.
### Sécurité du DHCP Windows
- **DHCP — Dynamic Host Configuration Protocol** attribue automatiquement aux clients leur configuration réseau :
    - adresse IP ;
    - masque/prefix ;
    - default gateway ;
    - DNS ;
    - autres options DHCP.
- Un serveur DHCP compromis ou malveillant peut fournir une configuration falsifiée et rediriger une partie du trafic réseau.
```
Client
→ DHCP Server
→ IP + Gateway + DNS
→ Network Access
```
#### Risques liés au DHCP
Principales menaces :
- **Rogue DHCP** → serveur DHCP non autorisé ;
- **DHCP Spoofing** → réponses DHCP falsifiées ;
- **DHCP Starvation** → épuisement du pool d’adresses ;
- accès réseau par un équipement non autorisé ;
- modification frauduleuse de la gateway ou du DNS.
Exemple :
```
Rogue DHCP
→ Gateway = Attacker
→ DNS = Attacker
→ trafic potentiellement redirigé/intercepté
```

## Stratégie de sécurité locale, Group Policy et UAC
- Windows fournit plusieurs mécanismes natifs de sécurité, notamment **UAC**, Windows Defender, Windows Firewall, les contrôles d’accès du système de fichiers et BitLocker.
```
Local Security Policy
→ sécurité d'une machine

Group Policy / GPO
→ configuration centralisée

UAC
→ contrôle de l'élévation de privilèges
```
### Local Security Policy (secpol.msc)
- **Local Security Policy** permet de gérer les paramètres de sécurité d’un ordinateur Windows individuel.
- Accessible via PowerShell, MMC notamment avec :
```
secpol.msc
```
Elle permet de configurer entre autres :
- password policies ;
- account policies ;
- attributions de droits d'utilisateur ;
- audit policies ;
- security options ;
- certains paramètres UAC.
Exemple :
```
Account Policies
→ Password Policy
→ Minimum password length
→ Password history
```
- Une mauvaise configuration peut réduire la sécurité ou provoquer des dysfonctionnements, donc les changements doivent être contrôlés.
<img src="../../assets/w_secpol.png" alt="W Secpol" width="500">
### Stratégie de groupe (gpedit.msc)
- Une **Group Policy** permet d’appliquer des configurations aux :
	- ordinateurs ;
	- utilisateurs.
- Cet outil est souvent utilisé pour contrôler de manière centralisée les paramètres sur plusieurs ordinateurs d'un réseau.
- Elle peut gérer :
	- paramètres de sécurité ;
	- Windows Update ;
	- firewall ;
	- network settings ;
	- applications autorisées/interdites ;
	- scripts startup/shutdown ;
	- Windows Defender ;
	- paramètres utilisateur.
#### `gpedit.msc` vs Group Policy Management
```
gpedit.msc
→ Local Group Policy Editor
→ politique de la machine locale

Group Policy Management (GPMC)
→ création/gestion de GPO Active Directory
→ plusieurs machines/utilisateurs du domaine
```
> ⚠️ Le cours mélange légèrement les deux : `gpedit.msc` sert principalement à éditer la **Local Group Policy**, tandis que les GPO de domaine sont normalement gérées via **Group Policy Management Console — GPMC**.
#### Création d’une GPO de domaine
Dans Group Policy Management :
```
Domain / OU
→ Create a GPO and Link it here
→ Name
→ Edit
```
Une GPO contient deux grandes sections.
##### Computer Configuration
- Paramètres appliqués aux **machines**.
- Peut définir :
    - services ;
    - security settings ;
    - réseau ;
    - firewall ;
    - paramètres système.
```
Computer
→ démarre / actualise les policies
→ Computer Configuration appliquée
```
##### User Configuration
- Paramètres associés à l’**utilisateur**.
- Peut gérer :
    - desktop ;
    - applications ;
    - paramètres réseau ;
    - expérience utilisateur.
```
User
→ logon / policy refresh
→ User Configuration appliquée
```
#### Local Policy vs Domain GPO
- Dans un environnement Active Directory, plusieurs politiques peuvent s’appliquer au même système.
Ordre conceptuel classique :
```
L → Local
S → Site
D → Domain
OU → Organizational Unit
```
→ **LSDOU**.
Les politiques de domaine/OU peuvent donc imposer une configuration différente de celle définie localement.
### UAC — User Account Control
- **UAC** contrôle les opérations nécessitant des privilèges administrateur.
- Lorsqu’une application demande une élévation, Windows affiche un prompt permettant d’autoriser ou refuser l’opération.
```
Application
→ privileged operation
→ UAC
→ Approve / Deny
```
#### Administrateur
- Un utilisateur déjà membre des administrateurs reçoit généralement un **consent prompt** :
```
Do you want to allow this app...?
→ Yes / No
```
#### Utilisateur standard
- Un utilisateur standard doit généralement fournir les **credentials d’un administrateur**.
```
Standard User
→ elevation requested
→ Admin credentials required
```
#### Pourquoi UAC ?
- UAC limite l’utilisation automatique des privilèges administrateur.
Exemple :
```
Malicious Application
→ veut modifier une zone système
→ elevation nécessaire
→ UAC prompt
```
Cela réduit notamment le risque qu’une application réalise silencieusement certaines modifications privilégiées.
> **UAC ≠ sandbox / antivirus** : il s’agit principalement d’un mécanisme de **séparation et d’élévation de privilèges**.

<img src="../../assets/w_uac.png" alt="W UAC" width="600">
#### Niveaux UAC
Windows propose quatre niveaux principaux.
##### Always Notify
- Niveau le plus strict.
- Notification lorsqu’une application **ou l’utilisateur** tente d’effectuer certaines modifications nécessitant une élévation.
- Utilise le **Secure Desktop**.
```
Always Notify
→ maximum prompts
→ highest UAC visibility
```
##### Notify me only when apps try to make changes — Default
- Niveau par défaut.
- Prompt lorsqu’une application tente une modification nécessitant une élévation.
- Les actions initiées directement par l’utilisateur peuvent être traitées différemment selon le paramètre.
- Utilise normalement le **Secure Desktop**.
> ⚠️ Le cours indique que le niveau par défaut ne diminue pas le bureau. C’est inversé : le niveau **par défaut utilise normalement le Secure Desktop**, qui assombrit le reste de l’écran.
##### Notify me only when apps try to make changes — Do not dim desktop
- Même logique générale, mais le prompt apparaît **sans Secure Desktop**.
```
UAC Prompt
→ desktop reste interactif/non assombri
```
→ légèrement moins sécurisé car d’autres processus peuvent davantage interagir avec le desktop normal.
##### Never Notify
- Aucun prompt UAC.
- Niveau le moins protecteur.
```
Never Notify
→ UAC prompts disabled
→ security ↓
```
Il est déconseillé de désactiver UAC sans raison spécifique.
#### Secure Desktop
Lorsqu’UAC utilise le **Secure Desktop** :
```
Normal Desktop
→ dimmed / inaccessible

UAC Prompt
→ displayed on secure desktop
```
Objectif :
- réduire les possibilités pour une application non privilégiée :
    - d’interagir avec le prompt ;
    - de simuler certains clics ;
    - de manipuler son interface.
### À retenir
```
secpol.msc
→ Local Security Policy
→ paramètres de sécurité locaux
```

```
gpedit.msc
→ Local Group Policy

GPMC
→ GPO Active Directory
→ administration centralisée
```

```
GPO
├─ Computer Configuration
└─ User Configuration
```

```
UAC
→ contrôle l'élévation de privilèges
→ Consent Prompt / Credential Prompt
→ Secure Desktop
```

Le point clé est de distinguer les trois rôles : **Local Security Policy configure la sécurité locale, les GPO permettent d’imposer des configurations à grande échelle, et UAC contrôle l’utilisation des privilèges administrateur.**
## Authentification et Autorisation sous Windows

```
Authentication → Qui es-tu ?
Authorization  → Qu'as-tu le droit de faire ?
```

- **Authentication** vérifie l’identité d’un utilisateur, d’un ordinateur ou d’un service.
- **Authorization** détermine ensuite les ressources et actions auxquelles cette identité a droit.
### Authentification
- L'authentification est le processus de vérification de l'identité d'un utilisateur.
- Windows peut utiliser plusieurs méthodes :
	- username/password ;
	- smart card ;
	- biométrie ;
	- certificats ;
	- MFA.
- Dans un environnement Active Directory, les protocoles les plus importants sont surtout **Kerberos** et **NTLM**.
#### Kerberos
- Protocole d’authentification principal dans un **domaine Active Directory**.
- Repose sur un **KDC — Key Distribution Center**, généralement fourni par les Domain Controllers.
- Lorsqu'un utilisateur se connecte au système pour la première fois, il reçoit un « ticket » du KDC. Ce ticket est utilisé pour vérifier l'identité de l'utilisateur pendant une certaine période. Le protocole Kerberos offre une authentification rapide et sécurisée et prend en charge l'authentification entre les services sur le réseau.
- Utilise des **tickets** plutôt que de retransmettre constamment le password.
```
User
 ↓
KDC
 ↓
Ticket
 ↓
Service
```
Principe simplifié :
```
Login
→ obtention d'un TGT
→ demande d'un Service Ticket
→ accès au service
```
##### Clock Synchronization
- Kerberos dépend fortement du temps.
```
Client Time ≈ Domain Controller Time
```
Une différence d’horloge trop importante peut provoquer des erreurs d’authentification.
→ utiliser une synchronisation temporelle fiable.
##### SPN — Service Principal Name
- Identifie une instance de service dans Active Directory.
- Doit être :
    - correctement configuré ;
    - associé au bon compte ;
    - unique.
Exemple :
```
HTTP/webserver.domain.local
MSSQLSvc/sql01.domain.local
```
-> Une mauvaise configuration des SPN peut empêcher Kerberos et provoquer un fallback vers NTLM.
##### Chiffrement
- Privilégier les algorithmes modernes comme **AES**.
- Éviter les mécanismes historiques comme DES lorsqu’ils sont encore présents dans un environnement legacy.
#### NTLM — NT LAN Manager
- Protocole plus ancien que Kerberos.
- NTLM hache les informations d'identification de l'utilisateur et utilise ces hachages (hashes) pour l'authentification.
- Souvent utilisé lorsque Kerberos ne peut pas fonctionner :
    - système hors domaine ;
    - accès par IP dans certains contextes ;
    - legacy systems ;
    - mauvaise configuration Kerberos.
```
Kerberos indisponible
→ NTLM fallback possible
```
NTLM utilise un mécanisme **challenge-response** dérivé du secret utilisateur.
> Il ne transmet normalement pas directement le password sur le réseau.
##### NTLMv1 vs NTLMv2
```
NTLMv1 → ancien / faible
NTLMv2 → plus robuste
```
Bonnes pratiques :
- désactiver NTLMv1 ;
- utiliser NTLMv2 si NTLM reste nécessaire ;
- réduire progressivement l’utilisation de NTLM ;
- préférer Kerberos dans AD.
#### Digest Authentication
- Mécanisme historique utilisé notamment avec certains services HTTP.
- Fonctionne via un mécanisme challenge-response basé sur un digest plutôt qu’en envoyant directement le password.
> Historiquement, Digest est fortement associé à **MD5**, aujourd’hui considéré comme faible. C’est donc surtout un mécanisme legacy.
#### Basic Authentication
- Envoie les credentials sous une forme **Base64**, qui n’est pas un chiffrement.
```
username:password
→ Base64
→ facilement décodable
```
Donc :
```
Basic sans TLS
→ credentials exposés

Basic + HTTPS/TLS
→ transport chiffré
```
> Dire que Basic envoie « en clair » est conceptuellement correct du point de vue sécurité : Base64 n’offre aucune confidentialité.
#### Carte à puce - Smart Card Authentication
- Utilise une **carte à puce** contenant des éléments cryptographiques, associée généralement à un PIN.
```
Something you have → Smart Card
+
Something you know → PIN
```
Bonnes pratiques :
- protéger le PIN ;
- protéger physiquement la carte ;
- contrôler les lecteurs ;
- révoquer rapidement une carte perdue.
#### Authentification basée sur les certificats
- Cette méthode utilise des certificats numériques (digital certificates) et est souvent utilisée en conjonction avec une Infrastructure à Clé Publique.
- L'identité d'un utilisateur est vérifiée via un certificat numérique signé par une autorité de certification (certificate authority) et détenu par l'utilisateur.
#### Comparaison rapide

|Méthode|Usage|
|---|---|
|**Kerberos**|Authentification principale en Active Directory|
|**NTLM**|Legacy / fallback|
|**Digest**|Mécanisme ancien, notamment HTTP|
|**Basic**|Simple, doit être protégé par TLS|
|**Smart Card**|Authentification forte avec carte + PIN|
|**Certificate**|Authentification basée PKI|
### Autorisation — Authorization
- Une fois l’utilisateur authentifié, Windows doit déterminer ce qu’il peut faire.
- Lors de la connexion, Windows construit un **Access Token / Security Token** contenant notamment :
	- SID de l’utilisateur ;
	- SIDs des groupes ;
	- privilèges ;
	- informations de sécurité.
```
Authenticated User
→ Access Token
→ Groups + Privileges
→ Authorization Decisions
```
- Une partie importante de l'autorisation Windows est l'utilisation des Listes de Contrôle d'Accès (Access Control Lists - ACL) et des Entrées de Contrôle d'Accès (Access Control Entries - ACE).
	- ACL déterminent le type d'accès qu'un utilisateur ou un groupe a sur un objet (par exemple, un fichier, un dossier ou une clé de registre) ;
	- ACE sont des entrées individuelles dans les ACL et déterminent comment un utilisateur ou un groupe particulier peut accéder à un objet.
#### SID — Security Identifier
- Windows identifie les utilisateurs et groupes principalement avec leur **SID**, pas simplement leur nom.
- Exemple conceptuel :
```
S-1-5-21-...
```

```
Username → lisible par l'humain
SID      → identité réellement utilisée par Windows
```
#### ACL — Access Control List
- Une **ACL** définit les règles de contrôle d’accès associées à un objet.
- Une ACL répertorie les utilisateurs et les groupes qui ont la permission d'accéder à l'objet.
- Chaque entrée est appelée une ACE et détermine comment un utilisateur ou un groupe particulier peut accéder à l'objet.
- Objets possibles :
	- fichier ;
	- dossier ;
	- registry key ;
	- printer ;
	- service ;
	- autr
```
Object
→ ACL
→ ACE
→ Allow / Deny / Audit
```
#### ACE — Access Control Entry
- Chaque entrée d’une ACL est une **ACE**.
- Une ACE associe généralement :
```
User / Group
+
Permission
+
Allow / Deny
```
Exemple :
```
Finance Group
→ Read + Write
→ ALLOW
```
#### DACL et SACL
- Complément important :
- Une Security Descriptor Windows peut notamment contenir :
##### DACL — Discretionary ACL
- Définit **qui peut faire quoi** sur l’objet.
```
Alice → Read  → Allow
Bob   → Write → Deny
```
##### SACL — System ACL
- Définit **quels accès doivent être audités**.
```
Failed Write
→ generate Security Event
```

```
DACL → authorization
SACL → auditing
```
#### Permissions NTFS
Permissions classiques :

|Permission|Fonction|
|---|---|
|**Full Control**|Tous les droits + modification des permissions|
|**Modify**|Lire, écrire, modifier, supprimer|
|**Read & Execute**|Lire et exécuter|
|**List Folder Contents**|Voir le contenu d’un dossier|
|**Read**|Lire|
|**Write**|Créer/modifier certaines données|
#### Stratégie de groupe (GPO) 
Les **GPO** peuvent compléter le contrôle d’accès en imposant des règles aux utilisateurs et ordinateurs :
- User Rights Assignment ;
- restrictions système ;
- sécurité ;
- application control ;
- firewall ;
- restrictions de connexion.

```
GPO
→ configure les règles

ACL
→ contrôle l'accès à un objet précis
```

> Une GPO et une ACL ne remplissent donc pas exactement le même rôle.

## Gestion des MAJ et des correctifs
- Le **Patch Management** consiste à identifier, tester, déployer et vérifier les correctifs destinés à :
    - vulnérabilités ;
    - bugs ;
    - problèmes de stabilité ;
    - composants obsolètes.
- Sous Windows, **Windows Update** permet de récupérer et installer les correctifs Microsoft.
```
Vulnerability / Bug
→ Patch available
→ Test
→ Deploy
→ Verify
```
- Activer les mises à jour automatiques est utile, mais ne suffit pas toujours en entreprise : un correctif peut avoir un impact sur une application ou un service métier.
### Gestion des MAJ dans les grandes organisations
- La gestion des mises à jour et des correctifs est généralement effectuée à l'aide d'une approche centralisée.
- Une gestion correcte des correctifs suit généralement :
```
Inventory
→ Identify missing patches
→ Prioritize
→ Test
→ Approve
→ Deploy
→ Monitor
→ Report
```
Objectifs :
- réduire la fenêtre d’exposition aux vulnérabilités ;
- maintenir la compatibilité ;
- éviter qu’un patch défectueux perturbe la production ;
- vérifier que les systèmes sont réellement à jour.
#### Gestion centralisée
- Dans une grande organisation, les correctifs sont généralement gérés depuis une plateforme centrale plutôt que machine par machine.
- Ces solutions garantissent que tous les systèmes reçoivent les dernières mises à jour et les derniers correctifs.
- **WSUS — Windows Server Update Services** ;
- **MECM — Microsoft Endpoint Configuration Manager**.

```
Microsoft Updates
       ↓
Patch Management Platform
       ↓
Workstations / Servers
```
Cela permet notamment :
- sélectionner les updates ;
- approuver/refuser certains correctifs ;
- définir des groupes de machines ;
- planifier les déploiements ;
- suivre l’état de conformité.
#### Test des correctifs
- Il est très important que chaque correctif soit correctement testé. Cela permet de vérifier la compatibilité d'un correctif avec les applications, d'identifier les bogues éventuels et d'évaluer les performances globales.
Avant un déploiement massif, vérifier :
- compatibilité applicative ;
- stabilité ;
- performances ;
- impact sur les services ;
- nécessité d’un reboot.
Une approche classique consiste à utiliser plusieurs **deployment rings** :
```
Test / Pilot Group
       ↓
Small Production Group
       ↓
General Deployment
```
→ limite l’impact si un patch provoque un problème.
#### Distribution
- Une fois validés, les correctifs sont déployés selon une fenêtre définie.
- Ce processus implique généralement de choisir un moment qui aura un impact minimal sur le flux de travail de l'organisation.
```
Approved Patch
→ Maintenance Window
→ Automated Deployment
```
Il faut notamment prendre en compte :
- horaires d’activité ;
- redémarrages ;
- disponibilité des services ;
- criticité des systèmes.
#### Monitoring & Reporting
Après le déploiement, vérifier :
- machines patchées ;
- machines en échec ;
- update installée ;
- reboot nécessaire ;
- systèmes hors ligne ;
- taux de conformité.
```
Deploy
→ Success / Failure
→ Remediation
→ Compliance Report
```
> `Patch deployed` ≠ `Patch successfully installed everywhere`.

#### Correctifs d’urgence
Certaines vulnérabilités nécessitent un traitement beaucoup plus rapide :
- exploitation active ;
- vulnérabilité critique ;
- système exposé à Internet ;
- exploit public ;
- asset critique.
```
Critical + Exploited + Internet-facing
→ Emergency Patching
```
Le processus peut être accéléré :
```
Rapid Test
→ Approval
→ Emergency Deployment
→ Verification
```
-> Tout en conservant suffisamment de tests pour éviter une interruption majeure.
## Protection antivirus, anti-malware et contre les menaces
- Windows intègre plusieurs mécanismes complémentaires pour protéger les endpoints :
```
Microsoft Defender Antivirus
→ prévention / détection de malware

Windows Defender Firewall
→ contrôle du trafic réseau

Microsoft Defender for Endpoint
→ EDR / gestion et investigation avancées
```
- Ces protections doivent rester **à jour**, car de nouvelles signatures, modèles de détection et vulnérabilités apparaissent régulièrement.
> Un antivirus ne remplace pas le firewall, l’EDR, le patch management ou le least privilege : ces contrôles se complètent.
### Microsoft Defender Antivirus
- **Microsoft Defender Antivirus** est l’antivirus intégré à Windows.
- Il peut notamment :
	- analyser les fichiers ;
	- détecter malware, spyware et autres menaces ;
	- mettre en quarantaine des fichiers ;
	- supprimer certaines menaces ;
	- surveiller les activités en temps réel ;
	- utiliser des renseignements de sécurité locaux et cloud.
Dans Windows Security :
```
Windows Security
→ Virus & threat protection
```
On peut notamment consulter :
- dernier scan ;
- menaces détectées ;
- historique de protection ;
- état des protections ;
- mises à jour de sécurité.
<img src="../../assets/w_av.png" alt="W AV" width="500">
#### Real-Time Protection
- La **Real-Time Protection** surveille continuellement :
	- fichiers ouverts/créés ;
	- programmes exécutés ;
	- activités système pertinentes.
```
File / Process
→ Defender inspection
→ Malicious?
   ├─ No  → Allow
   └─ Yes → Block / Quarantine
```
- Elle constitue une protection importante contre l’exécution de malware.
#### Cloud-Delivered Protection
- La **Cloud-Delivered Protection** permet au client Defender de consulter les services cloud Microsoft afin d’obtenir rapidement des informations sur des fichiers ou comportements inconnus.
```
Unknown File
→ Local Defender
→ Microsoft Cloud
→ Reputation / Analysis
→ Verdict
```
Avantages :
- détection plus rapide des nouvelles menaces ;
- réputation cloud ;
- analyse complémentaire ;
- meilleure réaction aux menaces encore peu connues.
#### Automatic Sample Submission
- Defender peut envoyer automatiquement des **échantillons suspects** à Microsoft pour analyse.
- Cette fonctionnalité fonctionne en complément de la protection cloud.
```
Suspicious Sample
→ Microsoft analysis
→ New detection intelligence
```
Certaines organisations peuvent limiter cette fonctionnalité pour des raisons de :
- confidentialité ;
- réglementation ;
- sensibilité des fichiers.
> Cela doit être géré par politique plutôt que désactivé arbitrairement.
### Windows Defender Firewall
- Le firewall Windows contrôle le trafic réseau selon des règles.
- Il peut filtrer :
	- inbound ;
	- outbound ;
	- protocoles ;
	- ports ;
	- applications ;
	- profils réseau.
```
Network Traffic
→ Windows Firewall
→ Rule Evaluation
→ Allow / Block
```
> Le firewall ne protège pas seulement contre « Internet » : il peut également filtrer le trafic provenant du **LAN, d’autres segments réseau ou de machines compromises internes**.
### Protection contre les ransomwares
- Windows Security fournit notamment **Controlled Folder Access** pour réduire les modifications non autorisées de fichiers importants.
```
Application
→ attempts to modify protected folder
→ Trusted?
   ├─ Yes → Allow
   └─ No  → Block
```
- Selon la configuration/version, cette protection peut devoir être activée explicitement.
#### Controlled Folder Access
- Cette fonctionnalité protège certains dossiers contre les modifications effectuées par des applications non approuvées.
- Dossiers typiques :
	- Documents ;
	- Pictures ;
	- Videos ;
	- autres dossiers ajoutés manuellement.
Objectif principal :
```
Ransomware
→ tries to encrypt Documents
→ Controlled Folder Access
→ modification blocked
```
Une application légitime bloquée peut être ajoutée à la liste des applications autorisées.
> ⚠️ Il faut éviter de créer trop d’exceptions : une allowlist trop permissive réduit fortement l’efficacité de la protection.

<img src="../../assets/w_rams_1.png" alt="W Rams" width="500">
<img src="../../assets/w_rams_2.png" alt="W Rams" width="500">
## Infrastructure de journalisation Windows
- La journalisation Windows permet d’enregistrer les activités du système, des applications et des utilisateurs afin de faciliter :
	- troubleshooting ;
	- monitoring ;
	- détection d’incidents ;
	- investigation ;
	- audit / conformité.
```
Windows Events
→ Collect
→ Store
→ Analyze
→ Detect / Investigate
```
### Principaux journaux Windows
#### Application
- Ces journaux surveillent et enregistrent les activités des applications s'exécutant sur un système. C'est particulièrement utile pour détecter les erreurs et les plantages d'applications.
- événements générés par les applications ;
- erreurs ;
- crashs ;
- problèmes applicatifs.
#### Security
- C'est essentiel pour surveiller les activités non autorisées sur un système et détecter les failles de sécurité (security breaches) potentielles.
- authentifications réussies/échouées ;
- accès aux ressources ;
- événements d’audit ;
- activités liées à la sécurité.
#### System
- C'est important pour surveiller la santé globale et les performances du système d'exploitation.
- événements liés à Windows et ses composants ;
- erreurs système ;
- warnings ;
- problèmes de services ou drivers.
```
Application → apps
Security    → sécurité / audit
System      → OS / services / drivers
```
### Composants du moteur de journalisation Windows
#### Windows Event Log Service

- collecte et stocke les événements générés par Windows et les applications ;
- gère les journaux d’événements.
#### Event Viewer
L’**Observateur d’événements** permet de :
- visualiser les logs ;
- filtrer les événements ;
- analyser leurs détails ;
- rechercher des Event IDs spécifiques.
```
eventvwr.msc
```
#### Windows Logs
- Les Journaux Windows stockent des informations sur un certain nombre de catégories telles que :
```
Application
Security
Setup
System
Forwarded Events
```
-> Ils sont utilisés pour détecter les erreurs, surveiller les menaces de sécurité et analyser les performances du système.
#### Applications and Services Logs
- logs plus spécifiques à des composants, applications et services Windows ;
- Ces informations sont utilisées pour détecter les erreurs liées à une application ou à un service particulier ;
- souvent très utiles pour l’investigation détaillée.
Exemples :

```
Microsoft
└─ Windows
   ├─ PowerShell
   ├─ Defender
   ├─ TerminalServices
   └─ DNS-Server
```
#### Subscriptions
- Les **Event Subscriptions** permettent de collecter des événements provenant de plusieurs machines distantes.
- Cela peut être utilisé avec **Windows Event Forwarding — WEF** :
```
Endpoints
   ↓
Windows Event Forwarding
   ↓
Collector
   ↓
SIEM
```
### Politique de journalisation
#### Choisir les événements à enregistrer
Une journalisation trop faible peut faire perdre des informations importantes, tandis qu’une journalisation excessive génère énormément de bruit et de stockage.
Pour la sécurité, il est notamment pertinent de journaliser :
- login success/failure ;
- changements de privilèges ;
- changements de comptes/groupes ;
- process creation ;
- accès à des ressources sensibles.
> Sous Windows, la journalisation de sécurité repose surtout sur les **Audit Policies / Advanced Audit Policies**, pas uniquement sur des niveaux génériques comme `Error` ou `Information`.
#### Stockage des logs
Les logs peuvent grossir rapidement sur les systèmes actifs.
Il faut prévoir :
- capacité disque suffisante ;
- taille maximale adaptée ;
- politique de rétention ;
- alertes sur l’espace disponible.
```
High Event Volume
→ Log Growth
→ Disk Full
→ Events potentially lost
```
#### Archivage
Les anciens logs peuvent être nécessaires pour :
- incident response ;
- forensic ;
- audit ;
- conformité.
Ils doivent donc être archivés selon une politique de rétention définie.
```
Current Logs
→ Archive
→ Retention
→ Investigation later
```
#### Protection des journaux
Les logs peuvent contenir :
- usernames ;
- IP ;
- command lines ;
- chemins de fichiers ;
- activités administratives ;
- parfois des données sensibles.
Il faut donc appliquer :
- ACL ;
- RBAC ;
- least privilege ;
- stockage protégé ;
- accès limité aux personnes autorisées.
> Un attaquant privilégié peut chercher à **effacer ou modifier les logs** pour masquer son activité. Leur centralisation hors de l’endpoint réduit ce risque.
#### Centralisation via SIEM
Un **SIEM** permet de centraliser et corréler les événements de plusieurs sources.
```
Windows
Firewall
EDR
DNS
AD
PowerShell
   ↓
  SIEM
   ↓
Correlation
Detection
Alerting
Investigation
```
#### Alertes automatiques
Certains événements doivent déclencher rapidement une alerte :
```
Suspicious Admin Login
→ Alert

Privilege Change
→ Alert

Security Control Disabled
→ Alert
```
Les SIEM permettent de créer des **use cases / detection rules** basés sur les Event IDs et leur contexte.
> Un Event ID seul n’indique pas forcément une attaque : il faut souvent corréler **user + host + time + process + source IP + contexte**.
#### Revue régulière
Même avec des alertes automatiques, une revue périodique des logs reste utile pour :
- repérer des anomalies lentes ;
- détecter des patterns ;
- valider les règles SIEM ;
- identifier des événements non couverts.
### Journaux essentiels pour les violations de sécurité
#### Journaux de sécurité - Security Logs
- Les **Security Logs** sont essentiels pour détecter les signes d’une compromission.
- Ils peuvent aider à identifier :
	- activités anormales ;
	- multiples password failures ;
	- accès inhabituels ;
	- changements de comptes ;
	- élévations de privilèges ;
	- corréler les menaces ;
	- modifications de sécurité.
```
Multiple Failed Logons
→ possible brute force

Successful Logon after failures
→ possible compromise
```
<img src="../../assets/w_event.png" alt="W Event" width="600">
##### Event IDs utiles
Quelques événements Windows souvent surveillés :
```
4624 → Successful logon
4625 → Failed logon
4688 → Process created
4720 → User account created
4728 → Member added to global security group
4732 → Member added to local security group
1102 → Security audit log cleared
```

> Ce sont des exemples courants ; leur disponibilité dépend des **Audit Policies** activées.
#### Journaux PowerShell
- PowerShell est largement utilisé pour :
	- administration ;
	- automatisation ;
	- configuration ;
	- mais aussi par des attaquants.
- Ses logs sont donc très importants en investigation.
- Ils peuvent fournir des informations sur :
	- journaux d'exécution de commandes ;
	- commandes exécutées ;
	- scripts ;
	- utilisateur ;
	- modules chargés ;
	- exécution distante ;
	- paramètres ;
	- certaines sorties.
<img src="../../assets/w_event_P.png" alt="W Event P" width="600">
##### Logs PowerShell importants
Complément utile :
```
Microsoft-Windows-PowerShell/Operational
```
Fonctionnalités intéressantes :
- **Script Block Logging**
- **Module Logging**
- **Transcription**
Event ID très connu :
```
4104 → Script Block Logging
```
→ peut contenir le contenu de commandes/scripts PowerShell exécutés.
> Ces fonctionnalités doivent être activées/configurées pour fournir une visibilité maximale.

#### Remote Desktop / RDP Logs
Les journaux **TerminalServices / Remote Desktop Services** permettent de suivre l’usage de RDP.
Ils peuvent fournir :
- tentatives d'accès non autorisé ;
- utilisateur ;
- source IP ;
- connexion réussie/échouée ;
- ouverture/fermeture de session ;
- erreurs ;
- informations de session ;
- changements de configuration.
```
Remote IP
→ RDP Attempt
→ User
→ Success / Failure
```
Utilité SOC :
```
RDP Login
+ Unknown External IP
+ Privileged User
→ suspicious
```
<img src="../../assets/w_event_RDP.png" alt="W Event RDP" width="600">
##### Sources utiles pour RDP
- On peut notamment retrouver des événements sous :
```
Microsoft-Windows-TerminalServices-
  LocalSessionManager
  RemoteConnectionManager
```
- Les Security Logs peuvent également fournir du contexte supplémentaire sur les authentifications.
### Protection contre la suppression des traces
Un attaquant ayant obtenu des privilèges élevés peut tenter :
```
Compromise
→ Perform actions
→ Clear logs
→ Hide evidence
```
D’où l’intérêt de :
- centraliser rapidement les événements ;
- limiter les droits sur les logs ;
- alerter sur leur suppression ;
- conserver des copies hors de l’endpoint.
Exemple particulièrement sensible :
```
Event ID 1102
→ Security audit log was cleared
```
