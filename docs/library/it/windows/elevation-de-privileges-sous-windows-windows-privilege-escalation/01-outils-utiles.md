---
title: Outils utiles
source: IT/02 Windows/Élévation de privilèges/Élévation de privilèges sous Windows (Windows Privilege Escalation).md
note: Élévation de privilèges sous Windows (Windows Privilege Escalation)
up:
- - Élévation de privilèges sous Windows (Windows Privilege Escalation)
  - index.md
---

| Outil                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Seatbelt](https://github.com/GhostPack/Seatbelt)                                                        | Projet C# permettant d'effectuer une grande variété de vérifications d'élévation de privilèges locaux.                                                                                                                                                                                                                                                                                                                |
| [winPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS) | WinPEAS est un script qui recherche les chemins possibles pour une élévation de privilèges sur les hôtes Windows. Toutes les vérifications sont expliquées [ici](https://book.hacktricks.wiki/en/windows-hardening/checklist-windows-privilege-escalation.html). Il est très complet, mais peut produire un volume considérable de résultats. Il faut donc savoir identifier les découvertes réellement exploitables. |
| [PowerUp](https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Privesc/PowerUp.ps1)      | Script PowerShell pour trouver les vecteurs courants d'élévation de privilèges Windows qui reposent sur des erreurs de configuration. Il peut également être utilisé pour exploiter certaines des failles trouvées.                                                                                                                                                                                                   |
| [SharpUp](https://github.com/GhostPack/SharpUp)                                                          | Version C# de PowerUp.                                                                                                                                                                                                                                                                                                                                                                                                |
| [JAWS](https://github.com/411Hall/JAWS)                                                                  | Script PowerShell pour énumérer les vecteurs d'élévation de privilèges, écrit en PowerShell 2.0.                                                                                                                                                                                                                                                                                                                      |
| [SessionGopher](https://github.com/Arvanaghi/SessionGopher)                                              | SessionGopher est un outil PowerShell qui trouve et déchiffre les informations de session enregistrées pour les outils d'accès à distance. Il extrait les informations de session enregistrées de PuTTY, WinSCP, SuperPuTTY, FileZilla et RDP.                                                                                                                                                                        |
| [Watson](https://github.com/rasta-mouse/Watson)                                                          | Watson est un outil .NET conçu pour énumérer les KB manquants et suggérer des exploits pour les vulnérabilités d'Élévation de Privilèges.                                                                                                                                                                                                                                                                             |
| [LaZagne](https://github.com/AlessandroZ/LaZagne)                                                        | Outil utilisé pour récupérer les mots de passe stockés sur une machine locale à partir des navigateurs web, des outils de chat, des bases de données, de Git, des e-mails, des vidages mémoire (memory dumps), de PHP, des outils d'administration système, des configurations de réseaux sans fil, des mécanismes internes de stockage de mots de passe de Windows, et plus encore.                                  |
| [Windows Exploit Suggester - Next Generation](https://github.com/bitsadmin/wesng)                        | WES-NG est un outil basé sur la sortie de l'utilitaire `systeminfo` de Windows qui fournit la liste des vulnérabilités auxquelles le système d'exploitation est exposé, y compris les exploits pour ces vulnérabilités. Tous les systèmes d'exploitation Windows, de Windows XP à Windows 10, y compris leurs équivalents Windows Server, sont pris en charge.                                                        |
| [Sysinternals Suite](https://docs.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite)         | Nous utiliserons plusieurs outils de la suite Sysinternals dans notre énumération, notamment [AccessChk](https://docs.microsoft.com/en-us/sysinternals/downloads/accesschk), [PipeList](https://docs.microsoft.com/en-us/sysinternals/downloads/pipelist) et [PsService](https://docs.microsoft.com/en-us/sysinternals/downloads/psservice).                                                                          |
## 1. Windows Privilege Escalation Tools

### Local Enumeration & Misconfiguration Detection

|Outil|Fonction principale|
|---|---|
|[Seatbelt](https://github.com/GhostPack/Seatbelt)|Outil C# réalisant de nombreuses vérifications de sécurité et d'énumération locale Windows|
|[winPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS)|Recherche automatisée de vecteurs potentiels d'élévation de privilèges|
|[PowerUp](https://github.com/PowerShellMafia/PowerSploit)|Script PowerShell recherchant des erreurs de configuration exploitables, avec certaines capacités d'exploitation|
|[SharpUp](https://github.com/GhostPack/SharpUp)|Implémentation C# de vérifications similaires à PowerUp|
|[JAWS](https://github.com/411Hall/JAWS)|Script d'énumération Windows développé en PowerShell 2.0|

- Seatbelt : Particulièrement utile pour collecter des informations sur l'environnement Windows et identifier des éléments méritant une investigation supplémentaire.

- winPEAS : Effectue un grand nombre de contrôles liés aux permissions, configurations et vecteurs potentiels de Privilege Escalation. Il est très complet, mais peut produire un volume considérable de résultats. Il faut donc savoir identifier les découvertes réellement exploitables.

- PowerUp / SharpUp : Ces outils s'intéressent notamment aux Security Misconfigurations pouvant permettre une élévation locale.
    - La différence principale est leur technologie :
        - `PowerUp` : PowerShell.

        - `SharpUp` : C# / .NET.
    
- JAWS : Permet d'automatiser des vérifications d'élévation de privilèges dans des environnements Windows utilisant PowerShell.

### Credential Hunting & Recovery

|Outil|Fonction principale|
|---|---|
|[SessionGopher](https://github.com/Arvanaghi/SessionGopher)|Recherche des informations de connexion enregistrées dans des outils d'accès à distance|
|[LaZagne](https://github.com/AlessandroZ/LaZagne)|Recherche des identifiants et mots de passe stockés localement par différents logiciels|

- SessionGopher : Recherche des informations de session enregistrées par des applications comme :
    - PuTTY ;
    - WinSCP ;
    - SuperPuTTY ;
    - FileZilla ;
    - clients RDP.
    - Selon l'application et les données disponibles, ces informations peuvent inclure des noms d'hôtes, comptes, paramètres de connexion ou secrets enregistrés.

- LaZagne : Recherche des identifiants stockés sur la machine dans diverses catégories :
    - navigateurs web ;
    - messageries et clients e-mail ;
    - bases de données ;
    - Git et outils de développement ;
    - clients Wi-Fi ;
    - outils d'administration ;
    - mécanismes de stockage de secrets Windows.
    - La possibilité de récupérer un mot de passe dépend de l'application, de la protection appliquée et du contexte de sécurité de l'utilisateur exécutant l'outil.

Notion importante — Credential Hunting : la découverte d'identifiants peut permettre d'accéder à un compte plus privilégié sans exploiter directement une vulnérabilité du système d'exploitation.

### Missing Patches & Vulnerability Identification

|Outil|Fonction principale|
|---|---|
|[Watson](https://github.com/rasta-mouse/Watson)|Recherche des correctifs Windows potentiellement manquants et des vulnérabilités locales associées|
|[Windows Exploit Suggester NG (WES-NG)](https://github.com/bitsadmin/wesng)|Analyse notamment les informations issues de `systeminfo` pour identifier des vulnérabilités potentielles|

- Watson : Outil .NET qui aide à identifier des vulnérabilités locales connues à partir des informations du système et de ses mises à jour.

- WES-NG : Utilise les informations relatives au système Windows pour établir une liste de vulnérabilités potentiellement applicables.

Le cours mentionne notamment sa compatibilité avec les anciennes versions de Windows et leurs équivalents Windows Server.

Point essentiel : un correctif apparemment manquant ne prouve pas qu'une vulnérabilité est exploitable. Il faut vérifier la version exacte de Windows, les mises à jour cumulatives et les conditions techniques de la vulnérabilité.

## 2. Microsoft Sysinternals Suite

La [Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite) regroupe des utilitaires Microsoft permettant d'examiner en détail le fonctionnement et la configuration de Windows.

Le cours mentionne particulièrement trois outils.

|Outil|Utilisation|
|---|---|
|AccessChk|Examiner les droits d'accès effectifs ou déclarés sur des objets Windows|
|PipeList|Lister les Named Pipes présentes sur le système|
|PsService|Examiner et administrer les services Windows selon les permissions disponibles|

### AccessChk — Permissions Analysis

[AccessChk](https://learn.microsoft.com/en-us/sysinternals/downloads/accesschk) permet d'examiner les permissions associées notamment aux fichiers, dossiers, services et autres objets sécurisés.

Il est particulièrement intéressant pour identifier des Weak Permissions.

### PipeList — Named Pipes

[PipeList](https://learn.microsoft.com/en-us/sysinternals/downloads/pipelist) permet de lister les Named Pipes, mécanismes de communication entre processus (Inter-Process Communication — IPC).

Ces objets peuvent être pertinents lors d'investigations portant sur certains services Windows ou mécanismes d'impersonation.

### PsService — Windows Services

[PsService](https://learn.microsoft.com/en-us/sysinternals/downloads/psservice) permet de consulter et, avec les autorisations adaptées, d'interagir avec les services Windows.

Les services sont particulièrement importants en Privilege Escalation, car certains s'exécutent dans des contextes privilégiés comme `LocalSystem`.

### Prérequis — ACLs & Access Rights

- **ACL (Access Control List)** : C'est une liste globale qui contient un ensemble de règles (les ACE) définissant les droits ou l'audit sur un objet (fichier, dossier, clé de registre, objet Active Directory). 
- **ACE (Access Control Entry)** : C'est une règle individuelle qui compose une ACL. Elle cible un utilisateur ou un groupe spécifique (via son SID) et indique un droit précis (autoriser, refuser ou auditer). 
- **DACL (Discretionary Access Control List)** : C'est le type d'ACL qui gère la sécurité fonctionnelle. Elle détermine **qui a le droit d'accéder** à un objet et avec quels privilèges (lecture, écriture, modification, etc.). 
- **SACL (System Access Control List)** : C'est le type d'ACL qui gère **l'audit et la journalisation**. Elle permet au système d'enregistrer dans le _Journal des événements de sécurité_ (Security Event Log) les tentatives d'accès (réussies ou échouées) à un objet. 

---

Résumé des différences

|Concept|Nom complet|Fonction principale|
|---|---|---|
|**ACE**|Access Control Entry|Une ligne / règle individuelle dans une liste|
|**ACL**|Access Control List|Le conteneur global regroupant plusieurs ACE|
|**DACL**|Discretionary Access Control List|Contrôle les **permissions d'accès** (autoriser / refuser)|
|**SACL**|System Access Control List|Contrôle **l'audit et la traçabilité** des accès|

## 3. Tool Preparation & Execution

### Precompiled Binaries

Le cours mentionne plusieurs sources de binaires :

- [GhostPack Compiled Binaries](https://github.com/r3motecontrol/Ghostpack-CompiledBinaries) : versions précompilées de Seatbelt et SharpUp.
    
- [LaZagne Releases](https://github.com/AlessandroZ/LaZagne/releases/) : exécutables disponibles dans les publications du projet.
    

Il recommande toutefois de compiler les outils depuis leur code source lors d'une mission client.

Cela permet notamment de mieux maîtriser leur provenance, leur version, leurs dépendances et leur comportement.

### Writable Directories

Pour exécuter un outil sur un endpoint, il peut être nécessaire de le transférer vers un répertoire accessible en écriture.

Le cours propose :

```
C:\Windows\Temp
```


Il indique que ce répertoire est généralement accessible aux membres de `BUILTIN\Users`.

Précision : les permissions effectives varient selon la configuration et le durcissement du système. L'accès en écriture doit être vérifié ; il ne faut pas le considérer comme garanti.

## 4. Automated vs Manual Enumeration

Les outils automatisés accélèrent les investigations, mais peuvent introduire plusieurs difficultés.

|Limitation|Explication|
|---|---|
|Information Overload|Trop de résultats, parfois peu pertinents|
|False Positives|Identification de faiblesses qui ne sont pas réellement exploitables|
|False Negatives|Certaines erreurs de configuration peuvent ne pas être détectées|
|Tool Compatibility|Incompatibilité avec une version de Windows ou certaines protections|
|Execution Restrictions|Impossibilité de transférer ou d'exécuter un outil|

### Manual Enumeration — Fondamentaux

Même sans script spécialisé, Windows propose des commandes natives permettant de commencer une investigation.

```
whoami /all
whoami /priv
systeminfo
```


Ces commandes permettent respectivement d'examiner le contexte de sécurité du compte, ses privilèges et les informations générales du système.

D'autres utilitaires natifs, comme `icacls`, `sc.exe` et PowerShell, permettent d'approfondir l'analyse des permissions et des services.

Ces commandes constituent des compléments de compréhension ; la section introduit principalement les outils spécialisés.

### Recommended Approach

```
Initial Windows Access
          ↓
Manual System Enumeration
          ↓
Automated Enumeration
          ↓
Review Interesting Findings
          ↓
Validate Permissions / Vulnerabilities
          ↓
Select Relevant Privilege Escalation Path
```


L'objectif n'est pas d'exécuter le plus d'outils possible, mais de comprendre les résultats et de confirmer les faiblesses identifiées.

## 5. Operational Risks & Security Detection

L'utilisation d'outils de Privilege Escalation peut également présenter des risques opérationnels.

### System Stability

Même une simple énumération peut provoquer des problèmes sur des systèmes fragiles, particulièrement lorsque les vérifications sont nombreuses ou intrusives.

Il est donc important de maîtriser les actions exécutées lors d'une évaluation.

### Antivirus & EDR Detection

Les outils de reconnaissance, d'extraction d'identifiants et d'exploitation sont souvent reconnus par les solutions de sécurité.

Le cours donne l'exemple de LaZagne v2.4.3, dont un échantillon était détecté par 47 moteurs sur 70 lors d'une analyse VirusTotal historique.

Ce résultat illustre la forte visibilité des outils connus auprès des solutions de sécurité ; il ne représente pas un taux de détection actuel ou universel.

### Assessment Scope

Le cours distingue implicitement deux objectifs :

- Vulnerability Assessment / Privilege Escalation Assessment : identifier autant de faiblesses que possible.
    
- Evasive Assessment / Red Team : évaluer également la capacité de détection de l'organisation.
    

Pour ce module, l'hypothèse est que le client a temporairement configuré Windows Defender pour ne pas bloquer les activités prévues pendant les exercices.

Le support évoque également des techniques de modification d'outils destinées à contourner certaines détections, mais indique que leur étude est réservée à un module ultérieur.


## 6. Uses Beyond Penetration Testing

Ces outils peuvent aussi aider les équipes d'administration et de sécurité à :

- détecter des faiblesses facilement corrigeables (Low-Hanging Fruit) ;
    
- réaliser des audits périodiques de sécurité ;
    
- vérifier l'impact d'une mise à niveau Windows ;
    
- analyser une Gold Image avant son déploiement ;
    
- contrôler la sécurité des services, permissions et configurations ;
    
- améliorer la posture de sécurité et la conformité de l'organisation.
    

Ils présentent donc un intérêt autant offensif que défensif.

## 7. Synthèse — Which Tool for Which Task?

|Besoin|Outils pertinents|
|---|---|
|General Windows Enumeration|Seatbelt, winPEAS, JAWS|
|Misconfiguration Discovery|PowerUp, SharpUp, AccessChk|
|Credential Hunting|SessionGopher, LaZagne|
|Missing Patch Analysis|Watson, WES-NG|
|Service Enumeration|PsService, AccessChk|
|Named Pipe Enumeration|PipeList|

Les éléments essentiels à retenir sont :

- Les outils automatisés accélèrent l'énumération, mais ne garantissent pas l'identification de toutes les vulnérabilités.
    
- Les résultats doivent être interprétés et validés manuellement pour distinguer les vulnérabilités réelles des False Positives.
    
- La compréhension des Windows Privileges, ACLs, Services et mécanismes d'authentification permet de poursuivre une investigation même sans outils spécialisés.
    
- Un bon Pentester doit pouvoir expliquer précisément les commandes qu'il exécute, les informations qu'il collecte et les conséquences possibles de ses actions.
    

Principe central : maîtriser les mécanismes d'élévation de privilèges Windows avant de dépendre des outils qui les automatisent.
