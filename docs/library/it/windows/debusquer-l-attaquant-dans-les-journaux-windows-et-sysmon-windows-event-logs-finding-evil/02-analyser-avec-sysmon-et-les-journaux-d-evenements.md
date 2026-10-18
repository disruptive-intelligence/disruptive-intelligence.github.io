---
title: Analyser avec Sysmon et les journaux d'événements
source: IT/02 Windows/Journaux & investigation/Débusquer l'attaquant dans les journaux Windows et Sysmon (Windows Event Logs & Finding Evil).md
note: Débusquer l'attaquant dans les journaux Windows et Sysmon (Windows Event Logs & Finding Evil)
up:
- - Débusquer l'attaquant dans les journaux Windows et Sysmon (Windows Event Logs & Finding Evil)
  - index.md
---

Cette section présente l'utilisation de Sysmon et des Windows Event Logs pour détecter et investiguer trois techniques d'attaque :

- DLL Hijacking : détournement du chargement de bibliothèques DLL.
- Unmanaged PowerShell / C# Injection : exécution de code .NET au sein de processus inhabituels.
- Credential Dumping : tentative d'extraction d'identifiants Windows, notamment depuis LSASS.

L'objectif est de transformer des événements système en indicateurs exploitables pour le Threat Hunting et le DFIR.

## 1. Les bases de Sysmon

Sysmon (System Monitor) est un outil Microsoft Sysinternals qui surveille les activités Windows et les enregistre dans les journaux d'événements.

Il complète les Windows Event Logs natifs en fournissant une télémétrie plus détaillée.

### Architecture de Sysmon

Sysmon repose sur trois composants :

- Windows Service : assure la surveillance des activités système.
- Device Driver : participe à la collecte des événements.
- Event Log : stocke les événements capturés pour leur analyse.

Le service et son driver restent actifs après un redémarrage lorsque Sysmon est installé et configuré pour fonctionner automatiquement.

### Journaux Windows natifs ou Sysmon

| Événement | Source           | Utilisation                             |
| --------- | ---------------- | --------------------------------------- |
| 4624      | Windows Security | Successful Logon                        |
| 4688      | Windows Security | Process Creation                        |
| 1         | Sysmon           | Process Creation avec contexte détaillé |
| 3         | Sysmon           | Network Connection                      |
| 7         | Sysmon           | Image / DLL Loaded                      |
| 10        | Sysmon           | ProcessAccess                           |

Dans cette section, les détections reposent principalement sur Sysmon Event ID 7 et Sysmon Event ID 10.

### Installation de Sysmon
https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

Depuis un terminal administrateur :

```
sysmon.exe -i -accepteula -h md5,sha256,imphash -l -n
```


![Installation et demarrage de Sysmon v13.33](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-15.png)

Pour appliquer ensuite un fichier XML de configuration :

```
sysmon.exe -c filename.xml
```


### Configuration XML de Sysmon

Sysmon utilise un fichier XML pour définir quels événements enregistrer ou exclure selon leurs attributs : processus, chemin, adresse IP, type d'événement, etc.

Deux configurations communautaires sont citées :

- [SwiftOnSecurity — Sysmon Config](https://github.com/SwiftOnSecurity/sysmon-config?utm_source=chatgpt.com) : utilisée dans le lab.
- [Sysmon Modular](https://github.com/olafhartong/sysmon-modular?utm_source=chatgpt.com) : approche modulaire.

Précision : Sysmon est un outil de collecte et de surveillance, pas une solution EDR complète avec toutes les fonctionnalités de réponse.

## 2. Détection n° 1 — DLL hijacking

Le DLL Hijacking consiste à exploiter le mécanisme de recherche et de chargement des DLL de Windows pour faire charger une bibliothèque contrôlée par l'attaquant à la place de celle attendue.

### Sysmon Event ID 7 — chargement d'image (Image Loaded)

L'Event ID `7` enregistre les chargements de modules, notamment de DLL.

Les champs utiles comprennent :

| Champ       | Description                                 |
| ----------- | ------------------------------------------- |
| Image       | Chemin du processus qui charge la DLL       |
| ImageLoaded | Chemin de la DLL chargée                    |
| ProcessId   | PID du processus                            |
| Signed      | Indication de signature numérique de la DLL |
| Signature   | Informations sur le signataire              |
| User        | Compte associé au processus                 |

Exemple légitime :

```
Image        : C:\Windows\System32\mmc.exe
ImageLoaded  : C:\Windows\System32\psapi.dll
Signed       : true
```


![Sysmon Event 7 : mmc.exe charge psapi.dll, signee](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-20.png)

L'événement indique que `mmc.exe` a chargé `psapi.dll`, signée par Microsoft.

### Configuration de la collecte

Dans la configuration SwiftOnSecurity, on modifie le comportement de `ImageLoad` pour enregistrer tous les chargements :

![Configuration d'origine : ImageLoad en include, sans regle](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-16.png)

```
<ImageLoad onmatch="exclude">
</ImageLoad>
```


![Configuration modifiee : ImageLoad en exclude](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-17.png)

Avec aucune condition d'exclusion, ce réglage permet de journaliser tous les événements de cette catégorie.

À l'inverse, `onmatch="include"` sans condition d'inclusion ne sélectionne aucun événement.

Appliquer la configuration :

```
sysmon.exe -c sysmonconfig-export.xml
```


![Chargement de sysmonconfig-export.xml, configuration validee](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-18.png)

Puis consulter :

`Event Viewer → Applications and Services Logs → Microsoft → Windows → Sysmon → Operational`

![Journal Sysmon avec des evenements 7 Image loaded](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-19.png)

Attention : l'Event ID 7 peut générer un volume de logs important. En production, une sélection adaptée des événements est généralement préférable.

### Scénario du lab — calc.exe / WININET.dll
https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon
https://hijacklibs.net/#calc.exe
Exemple de détournement impliquant :

- `calc.exe`, un exécutable Windows légitime ;
- `WININET.dll`, une bibliothèque normalement fournie par Windows ;
- une DLL de démonstration renommée `WININET.dll`.

https://github.com/stephenfewer/ReflectiveDLLInjection/tree/master/bin
En suivant les étapes requises, qui impliquent de renommer `reflective_dll.x64.dll` en `WININET.dll`, de déplacer `calc.exe` de `C:\Windows\System32` avec `WININET.dll` vers un répertoire accessible en écriture (comme le dossier `Desktop`), et d'exécuter `calc.exe`, nous réussissons. Au lieu de l'application Calculatrice, une [MessageBox](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxa) s'affiche.

![DLL detournables par calc.exe (dont WININET.dll)](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-21.png)

Dans le lab, `calc.exe` est copié depuis `System32` vers le bureau, avec la DLL de démonstration.

Lors de l'exécution, la DLL contrôlée par le test est chargée et affiche une MessageBox à la place du comportement attendu de la Calculatrice.

![calc.exe lance depuis le bureau : MessageBox Hello from DllMain!](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-22.png)

La DLL utilisée provient d'un exemple de Reflective DLL, bien que le DLL Hijacking ne nécessite pas de DLL réfléchissante.

### Détection et investigation

L'analyse consiste à filtrer les événements Sysmon sur `Event ID 7`, puis à rechercher `calc.exe`.

![Filter Current Log : Sysmon/Operational, Event ID 7](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-23.png)

| Critère    | Chargement légitime                            | Chargement suspect du lab                   |
| ---------- | ---------------------------------------------- | ------------------------------------------- |
| Executable | `calc.exe` dans un emplacement Windows attendu | `calc.exe` copié dans un dossier modifiable |
| DLL        | `wininet.dll` depuis `System32`                | `WININET.dll` depuis le bureau              |
| Signature  | DLL Microsoft signée                           | DLL non signée                              |

- En faisant un Find, on retrouve notre calc.exe détourné

![Chargement suspect : calc.exe charge WININET.dll non signee](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-24.png)

- En comparaison avec notre calc.exe original, on peut voir des path et des IoC pertinentes à dégager de tout ça.

![Chargement legitime : calc.exe charge wininet.dll signee](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-25.png)

Trois indicateurs ressortent :

1. Unexpected Executable Path : exécution de `calc.exe` depuis un emplacement utilisateur modifiable. Initialement situé dans System32, ne devrait pas se trouver dans un répertoire accessible en écriture.
2. Unexpected DLL Location : chargement de `WININET.dll` depuis un emplacement inhabituel. initialement situé dans System32, ne devrait pas être chargé en dehors de System32 par calc.exe. Si des instances de chargement de « WININET.dll » se produisent en dehors de System32 avec « calc.exe » comme processus parent, cela indique un détournement de DLL au sein de calc.exe.
3. Unsigned DLL : La « WININET.dll » originale est signée par Microsoft, tandis que notre DLL injectée reste non signée..

```
calc.exe — Unexpected Location
          ↓
Loads WININET.dll — User-Writable Directory
          ↓
Unsigned DLL
          ↓
Potential DLL Hijacking
```


Ces critères peuvent alimenter une règle de détection.

Précisions : `Image` désigne le processus qui charge la DLL, pas nécessairement son processus parent. Une DLL non signée ou située hors de `System32` n'est pas automatiquement malveillante ; les trois indicateurs doivent être interprétés ensemble.

## 3. Détection n° 2 — PowerShell non managé / injection C#

### Code managé et CLR

Le langage C# utilise généralement l'environnement d'exécution .NET, notamment le Common Language Runtime (CLR).

Le code compilé est exécuté à travers cet environnement, avec notamment des mécanismes de compilation Just-In-Time (JIT).

Deux DLL sont particulièrement importantes :

- `clr.dll` : composant du Common Language Runtime.
- `clrjit.dll` : composant associé à la compilation JIT.

Leur présence est normale dans certains processus qui utilisent .NET.

### Process Hacker — repérer un processus managé

Process Hacker permet d'examiner les processus actifs.

Un processus comme `powershell.exe` peut apparaître comme Managed (.NET).

![Liste des processus dans Process Hacker](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-26.png)

![Infobulle de powershell.exe : processus manage (.NET)](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-27.png)

Depuis :

`Process Hacker → Process Properties → Modules`

L'analyste peut rechercher les modules :

```
clr.dll
clrjit.dll
```


![Modules clr.dll et clrjit.dll (Microsoft .NET Runtime)](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-28.png)

Cette inspection permet d'identifier la présence du runtime .NET dans un processus.

- La présence de « Microsoft .NET Runtime... », `clr.dll` et `clrjit.dll` devrait attirer notre attention. Ces 2 DLL sont utilisées lorsque du code C# est exécuté dans le cadre du runtime pour exécuter le bytecode.
- Si nous observons ces DLL chargées dans des processus qui ne les requièrent généralement pas, cela suggère une potentielle attaque [execute-assembly](https://www.cobaltstrike.com/blog/cobalt-strike-3-11-the-snake-that-eats-its-tail/) ou [d'injection PowerShell non managée](https://www.youtube.com/watch?v=7tvfb9poTKg&ab_channel=RaphaelMudge).

### Scénario du lab — injection dans spoolsv.exe

Exemple : une injection de code PowerShell dans `spoolsv.exe`, le processus Windows associé au Print Spooler.

L'injection est réalisée avec le projet PSInject, via `Invoke-PSInject`, en ciblant le PID de `spoolsv.exe`.

```
powershell -ep bypass 
Set-Location "C:\Tools\PSInject"
Import-Module .\Invoke-PSInject.ps1
Invoke-PSInject -ProcId (Get-Process spoolsv).Id -PoshCode "V3JpdGUtSG9zdCAiSGVsbG8sIEd1cnU5OSEi"
```


Avant l'injection, le processus ne présente pas les caractéristiques d'un processus .NET managé.

![spoolsv.exe avant l'injection : processus non manage](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-29.png)

Après l'injection :

- Process Hacker identifie `spoolsv.exe` comme utilisant .NET.
- Les modules associés au CLR deviennent observables.
- Sysmon Event ID `7` enregistre le chargement de `clr.dll`.

![spoolsv.exe apres l'injection : processus manage par .NET](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-30.png)

![Modules de spoolsv.exe dans Process Hacker](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-31.png)

![Sysmon Event 7 : spoolsv.exe charge clr.dll](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-32.png)

### Logique de détection

```
spoolsv.exe
    ↓
Unexpected CLR Initialization
    ↓
clr.dll / clrjit.dll Loaded
    ↓
Sysmon Event ID 7
    ↓
Potential Code Injection
```


L'indicateur principal est le chargement inattendu du runtime .NET dans un processus qui ne l'utilise normalement pas.

Cette technique de hunting peut contribuer à détecter :

- des injections de code C# ;
- certains usages d'Unmanaged PowerShell ;
- certaines techniques d'exécution d'assemblages .NET dans un processus tiers.

Limite : un processus natif peut légitimement héberger le CLR. La présence de `clr.dll` doit être corrélée au contexte du processus, aux modules chargés et aux autres événements disponibles.

## 4. Détection n° 3 — vol d'identifiants (credential dumping)

Le Credential Dumping consiste à extraire des secrets d'authentification depuis un système compromis.

Sous Windows, LSASS (Local Security Authority Subsystem Service) est une cible fréquente puisqu'il intervient dans la gestion des authentifications et des sessions de sécurité.

### Mimikatz & LSASS

Mimikatz est un outil capable d'examiner certaines informations d'authentification Windows.

Deux commandes sont présentées :

| Commande Mimikatz          | Fonction                                                           |
| -------------------------- | ------------------------------------------------------------------ |
| `privilege::debug`         | Tenter d'activer `SeDebugPrivilege`                                |
| `sekurlsa::logonpasswords` | Examiner certains secrets liés aux sessions de connexion via LSASS |

Selon la configuration et les protections Windows, les résultats peuvent comprendre des hashes ou d'autres informations d'authentification.

Sa sortie montre notamment un compte `Administrator` et des valeurs de hash, tandis que certains champs de mots de passe apparaissent comme `(null)`.

![image-22](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-image-22.png)

L'accès à LSASS et la réussite de l'extraction dépendent des privilèges et des mécanismes de protection en place.

### Sysmon Event ID 10 — accès à un processus (ProcessAccess)

Pour détecter les tentatives d'accès suspectes à LSASS, on utilise Sysmon Event ID 10.

Cet événement permet d'observer les accès entre processus.

![Documentation Sysmon de l'Event ID 10 ProcessAccess](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-33.png)

Champs pertinents :

| Champ         | Description                                                        |
| ------------- | ------------------------------------------------------------------ |
| SourceImage   | Processus à l'origine de l'accès                                   |
| TargetImage   | Processus ciblé                                                    |
| SourceUser    | Compte associé au processus source                                 |
| TargetUser    | Compte associé au processus cible                                  |
| GrantedAccess | Droits d'accès accordés au processus cible                         |
| CallTrace     | Informations sur la chaîne d'appels, lorsqu'elles sont disponibles |

### Exemple — AgentEXE.exe → lsass.exe

Exemple : un événement dans lequel un exécutable inhabituel, `AgentEXE.exe`, situé dans un répertoire `Downloads`, tente d'accéder à `lsass.exe`.

```
SourceImage : ...\Downloads\AgentEXE.exe
TargetImage : ...\lsass.exe
SourceUser  : ...\waldo
TargetUser  : NT AUTHORITY\SYSTEM
```


![Sysmon Event 10 : AgentEXE.exe accede a lsass.exe](../../../assets/debusquer-l-attaquant-dans-les-journaux-windows-et-sysmon-windows-event-logs-finding-evil-htb-windows-event-logs-34.png)

Cette activité est suspecte, car un exécutable peu connu provenant d'un dossier utilisateur accède à un processus sensible.

### Indicateurs de détection

- Unexpected Source Process : programme inhabituel accédant à LSASS.
- Suspicious File Location : exécutable provenant d'un dossier comme `Downloads`.
- Sensitive Target Process : accès à `lsass.exe`.
- Privileged Process Access : demande ou obtention de droits sensibles.
- Debug Privilege Usage : éventuelle utilisation de `SeDebugPrivilege`.

```
Unknown Executable
       ↓
Access to lsass.exe
       ↓
Sysmon Event ID 10
       ↓
Investigate Credential Dumping
```


### Points de vigilance

Des processus légitimes peuvent accéder à LSASS, notamment des composants d'authentification et des solutions Antivirus / EDR.

Par ailleurs :

- `SourceUser` différent de `TargetUser` ne prouve pas une compromission.
- La présence de `SeDebugPrivilege` n'est pas une preuve de Credential Dumping et son utilisation n'est pas systématiquement indispensable à toutes les techniques.
- ProcessAccess ≠ Successful Credential Extraction : l'Event ID 10 signale un accès entre processus, pas nécessairement une extraction réussie.

L'analyse doit intégrer l'identité du processus, son chemin, ses droits d'accès et les événements associés.

## 5. Comparaison des trois détections

| Technique                           | Event ID principal | Indicateur clé                                                     |
| ----------------------------------- | ------------------ | ------------------------------------------------------------------ |
| DLL Hijacking                       | Sysmon 7           | DLL chargée depuis un chemin inhabituel par un exécutable légitime |
| Unmanaged PowerShell / C# Injection | Sysmon 7           | Chargement inattendu de `clr.dll` / `clrjit.dll`                   |
| Credential Dumping                  | Sysmon 10          | Processus suspect accédant à `lsass.exe`                           |

### Démarche d'investigation

```
Sysmon Telemetry
       ↓
Identify Relevant Event ID
       ↓
Inspect Process & Target
       ↓
Examine Paths / Signatures / Access Rights
       ↓
Correlate Related Events
       ↓
Validate Suspicious Behavior
       ↓
Threat Hunting / DFIR Investigation
```


Pour renforcer les investigations, ces événements peuvent être corrélés avec :

- Sysmon Event ID 1 : création de processus ;
- Windows Security Event ID 4688 : création de processus, selon la politique d'audit ;
- Windows Security Event ID 4624 : sessions de connexion ;
- d'autres événements Sysmon, EDR et réseau.

## 6. Points essentiels

La valeur de Sysmon en Threat Hunting réside dans la capacité à observer des comportements techniques précis qui ne seraient pas toujours visibles dans les journaux Windows traditionnels.

Les trois exemples illustrent des méthodes de détection différentes :

- DLL Hijacking : examiner l'origine et les caractéristiques des DLL chargées.
- Code Injection : identifier les composants .NET chargés dans des processus inhabituels.
- Credential Dumping : surveiller les accès suspects à LSASS.

Dans chaque cas, un événement Sysmon constitue une observation à analyser, et non une preuve automatique d'activité malveillante. La détection devient plus fiable lorsque plusieurs éléments sont corrélés : processus, fichiers, chemins, signatures, utilisateurs et chronologie des événements.

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
