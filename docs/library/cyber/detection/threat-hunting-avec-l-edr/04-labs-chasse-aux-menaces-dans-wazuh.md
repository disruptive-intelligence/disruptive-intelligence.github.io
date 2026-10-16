---
title: Labs — chasse aux menaces dans Wazuh
source: Cyber/06 Détection & réponse/Threat hunting/Threat hunting avec l'EDR.md
note: Threat hunting avec l'EDR
up:
- - Threat hunting avec l'EDR
  - index.md
---

Trois chasses guidées par une hypothèse, menées dans le SIEM Wazuh (onglet Discover, index `wazuh-alerts-*`, requêtes en DQL). Le lab 1 reprend mes captures ; les labs 2 et 3 s'appuient sur le [writeup de Yusuf Arbaç](https://yusufarbc.dev/en/writeups/threat-hunting-with-edr-writeup-letsdefend/).

Environnement du Laboratoire de Chasse aux Menaces :

- SIEM (Wazuh)
- Événements EDR (Sysmon)
- Événements CTI ([Threat Intel - LetsDefend](https://app.letsdefend.io/threath-intelligence-feed))
- Journaux du Moniteur Système (Zabbix)

## Requêtes Wazuh : l'essentiel

- Toujours fixer la **période** de la question avant de chercher.
- Recherche libre : penser à mettre les étoiles autour du mot pour qu'il soit bien pris en compte : `*miner.exe*`, `*nltest*`.
- Filtrer d'abord par **groupe de règles**, puis par champ.

|Champ / filtre|Ce qu'il donne|
|---|---|
|`rule.groups: sysmon_event1`|Sysmon 1 : processus créés|
|`rule.groups: sysmon_event3`|Sysmon 3 : connexions réseau|
|`rule.groups: windows_application`|Journal Application (dont MsiInstaller 1033)|
|`rule.groups: zabbix`|Alertes de supervision Zabbix (CPU, mémoire…)|
|`rule.groups: firewall`|Journaux du pare-feu|
|`rule.mitre.id: T1087.001`|Alertes que Wazuh rattache à une technique ATT&CK|
|`data.win.system.eventID`|Event ID Windows ou Sysmon|
|`data.win.eventdata.image`|Exécutable du processus|
|`data.win.eventdata.parentImage`|Processus parent|
|`data.win.eventdata.commandLine`|Ligne de commande complète|
|`data.win.eventdata.originalFileName`|Nom interne du binaire (révèle un exécutable renommé)|
|`data.win.eventdata.hashes`|Hashes du fichier exécuté|
|`data.win.eventdata.queryName`|Sysmon 22 : nom de domaine résolu|
|`data.win.eventdata.destinationIp`|Sysmon 3 : IP contactée|
|`agent.name` / `agent.ip`|Machine qui a remonté l'événement|

## Lab 1 — Malware de minage

- `Hypothèse`  Un groupe d'acteurs de la menace distribue peut-être un logiciel malveillant (malware) pour effectuer du minage de cryptomonnaie sur nos systèmes. Ce logiciel malveillant pourrait utiliser secrètement les ressources de nos systèmes pour des opérations de minage de cryptomonnaie.

Point de départ : un mineur se trahit d'abord par la **charge CPU**. On part de la supervision, puis on remonte vers le processus.

### Étape 1 — La machine en surcharge CPU (Zabbix)

- Question 1 : According to System Monitor (Zabbix) logs, what is the hostname of the system that triggered a high CPU usage alert between Aug 1, 2024 00:00 - Aug 7, 2024 00:00?
- Query : `rule.groups: "zabbix" and cpu`
- Champs utiles : `data.host`, `data.cpu_usage`, `rule.description`.

![Alerte Zabbix de CPU au-dessus du seuil dans Wazuh](../../../assets/threat-hunting-avec-l-edr-letsdefend-th-edr-lab1-01.png)

### Étape 2 — Le logiciel installé : Event ID 1033

- Question 2 : What is the name of the application installed on the high-CPU system during Aug 1-7, 2024? Answer Format: Test Tester: Winrar & 7zip Extract Software
    - Query : `rule.groups: "windows" and data.win.system.eventID:1033`
    - Event ID intéressant à checker 1033

```text
Journaux Windows → Application → 1033 (MsiInstaller) → Windows Installer installed the product
```


- Le nom du produit est dans `data.win.eventdata.data` ; la machine dans `agent.name`.
- Voisins utiles : **1034** (produit désinstallé), **11707** (installation réussie), **11724** (désinstallation réussie).
- Seules les installations par **Windows Installer (MSI)** sont tracées : un `.exe` copié et lancé directement n'en laisse pas.

![Trois événements 1033 MsiInstaller dans Wazuh](../../../assets/threat-hunting-avec-l-edr-letsdefend-th-edr-lab1-02.png)

### Étape 3 — Le chemin de l'exécutable de minage : Sysmon 1

- Question 3 : What is the full path of the mining executable? Answer Format: C:\\\\Temp\\\\LetsDefend\\\\Uploads\\\ ester.exe
    - Query : Penser à mettre les étoiles entre le mot pour qu'il soit bien pris en compte * MOT **
    - Event ID sysmon : 1
- Requête : filtre `rule.groups: sysmon_event1`, recherche `*miner.exe*`, colonnes `agent.name`, `data.win.eventdata.image`, `data.win.eventdata.currentDirectory`.

![Processus de minage trouvés par Sysmon 1 sur deux serveurs](../../../assets/threat-hunting-avec-l-edr-letsdefend-th-edr-lab1-03.png)

### Étape 4 — Qui a lancé le mineur : le processus parent

- Même requête ; lire `data.win.eventdata.parentImage`.
- Le parent oriente l'enquête :
    - un binaire de téléchargement Windows (`bitsadmin.exe`, `certutil.exe`) : le fichier a été rapatrié avec un outil du système (LOLBin) ;
    - un processus de serveur web (`w3wp.exe`, IIS) : l'application web a probablement servi de porte d'entrée ;
    - `explorer.exe` : lancement par l'utilisateur (double-clic).

### Étape 5 — Le domaine contacté par le mineur

- Pivot sur l'exécutable : `data.win.eventdata.image: "C:\\Users\\…\\miner.exe"`.
- **Sysmon 22** (requête DNS) donne le domaine dans `queryName` ; **Sysmon 3** donne l'IP et le port de destination.

### Étape 6 — Attribution par la CTI

- Chercher le domaine dans le flux Threat Intel : il renvoie au **groupe** qui l'utilise et à ses autres **IOCs** (hashes).

### Étape 7 — Pivot sur le hash : l'étendue

- Recherche libre `*<hash>*` sur toute la période, toutes machines : le même binaire apparaît-il ailleurs, sous un autre nom ou un autre chemin ?
- Pour chaque nouvelle machine : chemin (`image`), parent (`parentImage`), heure.

```text
Alerte CPU (Zabbix) → machine
   → 1033 : logiciel installé
   → Sysmon 1 : chemin + parent du mineur
   → Sysmon 22 / 3 : domaine contacté
   → CTI : groupe + hash
   → recherche du hash : autres machines touchées
```


## Lab 2 — PowerShell encodé

- `Hypothèse` Des attaquants exécutent des commandes malveillantes par l'option `-EncodedCommand` de PowerShell.

### Étape 1 — Trouver la machine

- Filtre `rule.groups: sysmon_event1`, recherche `*powershell.exe*`, puis `data.win.eventdata.commandLine: *EncodedCommand*` (variantes : `-enc`, `-e`).
- La machine : `agent.name`, `agent.ip`.

### Étape 2 — Décoder la commande

- L'argument est du **Base64 de texte UTF-16LE** : un décodeur Base64 simple affiche des caractères séparés par des points.
- CyberChef : `From Base64` → `Decode text` (UTF-16LE).
- PowerShell :

```powershell
[Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('<chaîne>'))
```


- Dans le lab, la commande décodée télécharge un exécutable dans `C:\Windows\Temp` avec `Invoke-WebRequest` : l'IP du serveur de téléchargement devient le pivot suivant.

### Étape 3 — CTI sur l'IP, puis le hash

- L'IP dans le flux Threat Intel → groupe associé et ses IOCs, dont un hash.
- Filtre `rule.groups: sysmon_event1`, recherche `*<hash>*` → `parentImage` du processus.

### Étape 4 — Connexion réseau et réponse du pare-feu

- Filtre `rule.groups: sysmon_event3`, recherche `*malware.exe*` → `destinationIp`.
- Puis `rule.groups: firewall and data.dstip: "<IP>"` → action du pare-feu.
- Une connexion **bloquée** (`deny`) ne clôt pas l'affaire : le malware s'est exécuté sur le poste, seule sa communication a échoué.

```text
Sysmon 1 : powershell -EncodedCommand → décodage → URL de téléchargement
   → CTI : groupe + hash → Sysmon 1 : parent
   → Sysmon 3 : IP contactée → pare-feu : autorisé ou bloqué
```


## Lab 3 — Reconnaissance et effacement des journaux

- `Hypothèse` Un attaquant a reconnu le poste et le domaine, puis a effacé des journaux pour couvrir ses traces.

Ici, Wazuh rattache déjà ses alertes à des techniques ATT&CK : on chasse par `rule.mitre.id`.

### Étape 1 — Comptes locaux : T1087.001

- `rule.groups: windows and rule.mitre.id: T1087.001` → machine et commande (`net user` / `net users`).

### Étape 2 — Comptes et groupes du domaine : T1087.002

- `rule.mitre.id: T1087.002` → groupe énuméré, par ex. `net group "Domain Admins" /domain`.

### Étape 3 — Contrôleurs de domaine : T1018 et nltest

- `rule.mitre.id: T1018` → `nltest /dclist:<domaine>` : la liste des DC du domaine.
- Recherche directe : `data.win.eventdata.commandLine: *nltest*`
- Le champ `originalFileName` de `nltest.exe` vaut **`nltestrk.exe`** (nom interne du binaire). Chercher sur `originalFileName` retrouve aussi une copie **renommée** de l'outil, que la recherche sur `image` manquerait.

### Étape 4 — IP de sortie

- Un `curl ifconfig.me` (ou un service équivalent) révèle à l'attaquant l'IP publique de sortie.
- Wazuh range cette activité sous T1018 ; dans ATT&CK, la découverte de la connexion Internet est T1016.001 (Internet Connection Discovery).

### Étape 5 — Effacement : T1070.001

- `rule.mitre.id: T1070.001` → journal effacé et outil utilisé : `wevtutil cl Microsoft-Windows-Sysmon/Operational`.
- `originalFileName` confirme l'outil (`wevtutil.exe`).
- Côté Windows, l'effacement d'un journal autre que Security laisse un **104** dans System (1102 pour Security).
- Les événements déjà envoyés à Wazuh restent consultables : c'est tout l'intérêt de centraliser.

```text
T1087.001 net user → T1087.002 net group "Domain Admins" /domain
   → T1018 nltest /dclist → curl ifconfig.me
   → T1070.001 wevtutil cl (journal Sysmon) = Defense Evasion
```


## Ce que les labs apprennent

|Event ID|Source|Ce qu'il apporte en chasse|
|---|---|---|
|**1033** / 1034|Journaux Windows → Application (MsiInstaller)|Logiciel installé / désinstallé par Windows Installer|
|**1**|Sysmon → Operational|Processus : chemin, ligne de commande, parent, hash, `OriginalFileName`|
|**3**|Sysmon → Operational|Connexion réseau d'un processus : IP et port de destination|
|**22**|Sysmon → Operational|Requête DNS d'un processus : domaine contacté|
|**104** / 1102|Journaux Windows → System / Security|Journal effacé|

- Partir d'un **signal** (CPU, alerte, technique ATT&CK), remonter au **processus**, puis pivoter sur un **IOC** (hash, domaine, IP) pour mesurer l'étendue.
- Le **parent** d'un processus dit souvent comment l'attaquant est entré.
- `OriginalFileName` démasque un binaire renommé.

Les Event IDs Sysmon et les requêtes sont repris dans la cheat sheet [Sysmon et requêtes SIEM](/cheatsheets/windows/fondamentaux/logs/sysmon/).
