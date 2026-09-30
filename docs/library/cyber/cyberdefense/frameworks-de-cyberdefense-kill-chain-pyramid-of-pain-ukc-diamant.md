---
title: Frameworks de cyberdéfense (Kill chain, Pyramid of pain, UKC, Diamant)
source: Cyber/05_Cyberdefense/Frameworks Cyber Defense (Kill chain, Pyramid of pain, UKC, Diamant).md
---

### Pyramids of pain

Moyen qui va évaluer la difficulté pour un attaquant de modifier un IoC

<img src="../../assets/pyramid_of_pain.png" alt="Pyramid of Pain" width="600">
#### Hash values (empreintes de fichiers) — trivial
- Valeur numérique fixe qui identifie de façon condensée un fichier ou une donnée, produite par un algo de hachage, plus petit changement dans le fichier, le hash changera du tout au tout.
- Algorithmes :
	- MD5 : Très répandu historiquement mais plus sûr : collisions connues.
	- SHA-1 : Déprécié par le NIST
	- SHA-2 (ex : 256) : Recommandé comme alternative aujourd’hui.
- Utilité : Recherche et classification, sources publiques, usage opérationnel.
- Limite : Modifier un seul bit du fichier change hash, l’attaquant peut aisément créer une variante si on ne s’appuie que sur les hashs.
- Outils : Virustotal, MetaDefender…
- Commandes :
	- **Get-FileHash fichier.ext -Algorithm MD5**

![image 1 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-1-1.png)

#### IP addresses
- IP identifie un appareil sur un réseau
- Attaquant peut facilement la changer : Nouvelle IP publique, proxys, VPS, utilisation de machine compro…
- Bloquer/Filtrer IP sur firewall donne un gain immédiat mais peu durable.
- Technique qui complique : Fast Flux
	- Technique DNS employée par botnets pour masquer l’infrastructure C2. https://unit42.paloaltonetworks.com/fast-flux-101/
	- Principe : Un même nom de domaine pointe vers beaucoup d’adresses IP qui changent très souvent. Les IP sont souvent des machines compro faisant office de proxies.
	- But : Rendre C2 / site malveillant résilient et difficile à détecter.
	- Conséquence : Bloquer IP individuelles devient inefficace.

#### Domain names
- Associer nom humainement lisible à une adresse IP
- Plus compliqué qu’une IP, doit acheter/maintenir domaine, configurer DNS? potentiellement payer/renouveler, gérer certificats. Même si fournisseurs DNS proposent API et process automatisés.
- Techniques :
	- Punnycode / IDN homograph attack
		- Attaquants créent domaines qui ressemblent à des légit en utilisant caractères Unicode (ex : [adıdas.de](http://xn--addas-o4a.de/)) ; convertis en ASCII ces domaines deviennent du Punycode comme [adıdas.de](http://xn--addas-o4a.de/). A première vue URL semble legit visuellement, mais c’ets un leurre.
	- URL shorteners :
		- Attaquants cachent destination réelle derrière des services de raccourcissement. Astuce défensive simple : Certains raccourcisseurs ajoutent ajoute après l’URL dans le navigateur, la page de dest.
	- Analyse en sandbox (any.run) :
		- Exécutent échantillon et montrent les échanges DNS… Pour ne pas avoir à visiter directement.

#### Network/Host artifacts (ex : clés de registre, chemins, mutex, patterns réseau)
- Compliqué pour l’attaquant d’agir sur ces aspects
- Process d’exécution suspect de Word

![image 2 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-2-1.png)

- Event suspects qui suivent l’ouverture d’une application

![image 3 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-3-1.png)

- Fichier déposé / modifié par l’attaquant

![image 4 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-4-1.png)

- Requête HTTP qui peuvent être détectés avec Wireshark ou Tshark

![image 5 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-5-1.png)

- tshark --Y http.request -T fields -e http.host -e http.user_agent -r analysis_file.pcap

![image 6 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-6-1.png)

  

#### Tools (outils ou binaires employés par l’attaquant)
- A ce niveau ça devient coûteux car doit recréer outils, réapprendre, réinvestir.
- Leviers principaux : Signature AV, règles de détection. YARA, Marketplaces (MalwareBazaar, Malshare) pour obtenir échantillons et indicateurs, Fuzzy hashing (SSDEEP) peut faire de la similarité entre variantes, utile quand les hashes classiques changent.
- Sources / Plateformes :
	- MalwareBazaar, Malshare : sources pour récupérer échantillons connus. Toujours manipuler en environnement isolé (VM/sandbox hors réseau de prod).
	- SOC Prime Threat Detection Marketplace : règles de détection partagées (Sigma, YARA, signatures) — utile pour récupérer règles et les adapter.
	- *VirusTotal / Any.run : pour enrichissement et visualisation comportementale (HTTP requests, DNS, connexions) sans exécuter toi-même le sample.
	- **YARA** = Recherche de patterns dans les **fichiers** (statique).
	- **SIGMA** = Recherche de patterns dans les **logs/événements** (SIEM).

#### TTPs (Tactics, Techniques, Procedures)
- Décrit comportement global d’un attaquant, pas juste un indicateur technique.
	- Tactics : Le pourquoi : Objectif de l’adversaire (obtenir un accès initial, élever ses privilèges, exfiltrer des données…)
	- Techniques : Le comment général : Méthode employée (hameçonnage, exploitation de vulnérabilité, vol d’identifiants…)
	- Procedures : Le comment précis : L’exécution concrète (Pièce jointe Excel avec macro malveillante envoyée via email)
        
		```jsx
		Tactic : Credential Access
		Technique : Pass-the-Hash (MITRE T1550.002)
		Procedure : L’attaquant utilise mimikatz pour extraire un hash NTLM et se connecter à un autre poste via psexec.
		```
        

### Cyber Kill Chain (RALEICA)

![image 7 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-7-1.png)

#### 1. Reconnaissance : But de l’attaquant : collecter des infos publiques ou directement interagir pour construire un profil ciblé (employés, technos exposées, emails, sous-domaines…).
- Objectif concret : augmenter la connaissance de la cible pour identifier :
	- Phase de recherche et de planning pour l’attaque. Récup des info sur la cible pour se préparer aux étapes suivante. Peut inclure des info sur l’infra, les employées, les process business, techno exposées.
	- Attack Surface : ensemble des éléments potentiellement attaquables (hosts, services, users, applications...)
	- Attack Vector : chemin/méthode précise permettant d'exploiter cette surface (phishing, vuln web, service exposé...)
- OSINT : Collecter depuis : Moteur de recherche, magazine et média en ligne, réseaux sociaux, forum et blog, base de donnée publiques, WHOIS et donnée technique.
- Reco passive : Pas d’interaction directe : WHOIS lookups, social media scrapping, data breach. 
	- Web archives (Wayback Machine) : retrouver anciennes pages, endpoints, fichiers ou technos qui ne sont plus visibles sur le site actuel.
	- Identifier : 
		- Plages IP appartenant à l'orga ;
		- Fournisseurs / partenaires ;
		- Anciennes fuites de données ;
		- Techno et versions publiquement visibles ;
		- Adresses emails / structure des usernames.
- Reco active : Génère directement du trafic vers l'infrastructure cible -> Plus facilement détectable / loggables
	- Ex :
		- Social engineering ;
		- Port scanning ;
		- Banner grabbing ;
		- Service / version détection ;
		- Vulnerability scanning ;
		- Requêtes directes vers serveur Web
	- Identifier : IP -> Port -> Service -> Version -> Vuln potentielle
- Point de vue Blue Team / SOC : Reco est difficile à empêcher, surtout lorsqu'elle utilise des sources publiques. Objectif est donc de réduire l'information exposée et détecter la reconnaissance active.
	- Réaliser réguliérement :
		- External pentest / Attack Surface Assessment ;
		- Recherches OSINT de sa propre organisation ;
		- Surveillance des leaks via Threat Intell.
	- Réduire : 
		- Documents internes accessibles publiquement ;
		- Metadata inutiles ;
		- Versions de logiciels exposées ;
		- Services internet non nécessaires.
	- Détecter : 
		- Scans de ports ;
		- Nombreuses requêtes sur différents endpoints ;
		- Enumération répétée ;
		- Reconnaissance de services.
	- Maintenir les services exposés à jour pour éviter qu'une vulnérabilité découverte pendant la reco soit directement exploitable.
#### 2. Armement (Weaponization) : But : Préparation de l'arsenal, transformer l’info en charge actionable (maldoc, exploit pack, payload), mais pas encore d'interaction avec la cible.
- A partir des infos de Reconnaissance, il choisit/assemble : 
	- Exploit adapté à une vulnérabilité identifiée ;
	- Payload / malware ;
	- Document malveillant ;
	- Infrastructure nécessaire ;
	- Techniques d'évasion adaptées aux défenses supposées.
- Exploit vs Payload : 
	- Exploit : code/méthode permettant d'exploiter une vuln.
	- Payload : code exécuté après l'exploitation pour obtenir l'effet désiré.

| Outil / ressource      | Usage                                                                 |
| ---------------------- | --------------------------------------------------------------------- |
| **Metasploit**         | Framework contenant exploits, modules post-exploitation, payloads…    |
| **MSFVenom**           | Génération/formatage de payloads                                      |
| **Exploit-DB**         | Recherche d’exploits publics pour vulnérabilités connues              |
| **Fuzzer (ex: AFL++)** | Découverte de bugs/crashs pouvant mener à de nouvelles vulnérabilités |

- Evasion / Obfuscation : 
	- Une partie importnate de Weaponization peut consister à rendre le payload plus difficile à détecter / analyser
- Point de vue Defender / SOC : L'armement se déroule généralement hors de l'infra de la victime, donc impossible à observer directement dans la majorité des cas.
	- Le défenseur agit surtout en anticipation :
		- patch management ;
		- réduction de la surface d'attaque ;
		- analyse des nouvelles vulns ;
		- Threat Intell sur les outils/malwares utilisés par les adversaires ;
		- tester si EDR/AV détectent les techniques attendues ;

#### 3. Livraison (Delivery) : Acheminer le payload à la cible. phishing (spear), watering-hole, USB drops, OAuth consent frauds, liens raccourcis.
- Le payload est déjà préparé à l'étape précédente (Weaponization), ici on cherche seulement à le faire parvenir.
- Principaux vecteurs de Delivery :

| Vecteur      | Exemple                              |
| ------------ | ------------------------------------ |
| Email        | `.docx`, `.zip`, lien phishing       |
| Web          | Fake update/installer, watering hole |
| Social       | DM avec lien/fichier                 |
| Physique     | USB drop                             |
| Accès direct | Upload sur serveur déjà compromis    |
- Point de vue Defender / SOC :
	- Contrôle utiles :
		- Email Security Gateway ;
		- Sandbox des PJ ;
		- URL rewriting / URL scanning ;
		- AV / EDR ;
		- Filtrage Web / DNS ;
		- Firewall ;
		- Blocage des macros non fiables ;
		- Contrôles des périphériques USB ;
		- User awareness / phishing training.
	- A rechercher : 
		- DL depuis domaine récent/suspect ;
		- Fichier avec .ext trompeuse ;
		- Archive protégée par MDP ;
		- Document Office provenant d'internet ;
		- Exécutable lancé depuis / USB / Downloads / Temps ;
		- URL raccourcie ou redirection multiple.

#### 4. Exploitation : But : exécuter le code, tirer parti d’une vulnérabilité (CVE connue ou 0-day), exécuter macro, drive-by.
- C'est le moment où le contenu livré devient réellement actif.
- Peut nécessiter : 
	- Vuln logicielle / OS ;
	- Vuln matérielle ;
	- Mauvaise configuration ;
	- Action utilisateur (ouvrir un document, activer une macro, lancer un .exe)
- Exploit /=/ Exploitation : 
	- Exploit : code ou méthode permettant de tirer parti d'une vulnérabilité.
	- Exploitation : phase pendant laquelle cette faiblesse est effectivement utilisée.
- Point de vue Defender / SOC : 
	- A cette phase, les contrôles importants sont classiques : EDR/AV, Patch management, Vuln management, IDP/IPS, application control, sandboxing...
	- A surveiller : 
		- Process creation ;
		- Parent / Child process ;
		- Exploit alert ;
		- PowerShell / CMD lancés par Office ;
		- Connexion réseau juste après ouverture d'un fichier.

#### 5. Installation : But : installer composants nécessaires à la compromission sur le système cible. (backdoor, webshell, services, run keys, scheduled tasks).
- Installer ou modifier des composants sur la machine compromise pour maintenir / renforcer l'accès.
- Persistence : Si l'accès initial dépend d'une vulnérabilité (CVE) -> patch demain -> accès perdu, donc attaquant cherche un autre mécanisme : 
	- Scheduled Task ;
	- Installer web shell sur webservers : Script malicieux utilisé pour maintenir un accès sur le système compromis.
	- Installer backdoor : Attaquant peut utiliser Meterpreter pour installer backdoor sur la victime.
	- Créer ou modifier service.
	- Ajouter une entrée dans les “run keys” pour le payload dans l’éditeur de registre.
	- DLL / autorun.
- Dropper / Loader / Payload : 
	- Dropper : dépose un ou plusieurs fichiers malveillants sur la machine.
	- Loader : charge/exécute un payload, parfois directement en mémoire.
	- Payload : composant qui réalise l'action finale.
- Backdoor / Webshell :
	- Backdoor : mécanisme permettant de revenir sur le système sans repasser par le vecteur initial.
	- Webshell : script malveillant placé sur un serveur Web permettant d'exécuter des commandes à distance.
- Defense Evasion : Pendant l'installation, l'attaquant cherche généralement aussi à rester discret : 
	- Masquer fichiers/process ;
	- Utiliser noms ressemblant à des binaires Windows ;
	- Modifier exclusion AV ;
	- Désactiver protections ; 
	- Supprimer certaines traces ;
	- Utiliser LOLBins.
- Point de vue Defender / Threat Hunting : Si l'attaquant atteint cette étape, il à déjà exécuté quelque chose sur la machine, il faut donc chercher les changements post-compromission : 
	- Nouveaux services, scheduled tasks, clés Run modifiées, comptes crées, règles firewall ajoutées, fichiers dans Startup, nouveaux fichiers dans webroot ;
	- Exécutables déplosés dans : 
		- `%TEMP%`
		- `%APPDATA%`
		- `%ProgramData%`
		- `C:\Users\Public`
	- Signature / Application Control : Recommande d'autoriser uniquement les exécutables signés : AppLocker / Windows Defender Application Control (WDAC)

#### 6. Command & Control (C2) : But : Canal de communication entre l'attaquant et le système compromis (beaconing, exfiltration).
- Machine compromise pourra communiquer vers un serveur externe mis en place par un attaquant. Après cela établit, attaquant aura contrôle total sur la machine de la victime.
- Callback / Beaconing :
	- Très souvent ce n'est pas l'attaquant qui initie une connexion entrante vers la victime, le malware contacte lui-même le C2 : traverse plus facilement NAT/Firewall, trafic sortant souvent moins filtré, peut se mélanger au trafic légitime.
	- Beaconing : un implant peut contacter périodiquement son C2 pour demander "As-tu une commande pour moi ?", cette periodicité est appelée beaconing, Pour éviter d'être détectés, certains implants utilisent du jitter (rend périodicité moins évidente)/
- Canal C2 les plus communs :
	- HTTP sur le port 80 et HTTPS sur le port 443, permet à l’attaquant de se noyer dans la masse et passer Firewall.
	- DNS : Machine infectée va faire constamment des requêtes DNS au serveur DNS contrôlé par l’attaquant, connu sous DNS Tunneling

| Canal                  | Pourquoi utilisé                                                     |
| ---------------------- | -------------------------------------------------------------------- |
| **HTTP/HTTPS**         | Se mélange au trafic Web normal ; `80/443` souvent autorisés         |
| **DNS**                | DNS presque toujours disponible ; possibilité de tunneling           |
| **TCP/UDP custom**     | Protocole spécifique au malware                                      |
| **Cloud/API légitime** | Discord, Telegram, GitHub, stockage cloud… pour masquer le trafic    |
| **SMB**                | Peut servir à la communication entre machines compromises en interne |

- Reverse Shell vs C2 implant : 
	- Reverse shell : la victime ouvre une connexion vers l'attaquant et lui fournit directement un shell.
	- C2 implant / agent : programme plus complet qui communique périodiquement avec une infra C2. 
		- Frameworks courants : Metasploit (Meterpreter), Sliver, Mythic, Havoc.
- Infrastructure C2 : 
	- L'attaquant peut utiliser plusieurs couches : Victime -> Redirector / Proxy -> C2 réel. Redirector évite d'exposer directement le serveur principal de l'attaquant.
	- Infra possible : VPS, domaine dédié, domaine compromis, proxy/redirector, service cloud légit.
- Point de vue Defender / SOC : Phase où Network Security Monitoring devient particulièrement importante.
	- A rechercher : 
		- Connexion périodiques vers la même IP/domaine ;
		- Domaine récemment crée ou très rare ;
		- Machine qui contacte une IP connue comme C2 ;
		- Trafic externe inhabituel depuis un serveur ;
		- Processus inhabituel initiant une co réseau
- Egress filtreing : Complément important côté défense : 
	- Contrôler connexions sortantes, pas uniquement entrantes ;
	- Limiter les machines pouvant accéder directement à internet ;
	- Imposer proxy / DNS interne ;
	- Bloquer destinations malveillantes via Threat Intell.

#### 7. Actions sur l’objectif : But : Phase où l’adversaire utilise l'accès obtenu pour atteindre son objectif réel (vol de credentials, exfiltration, sabotage, chiffrement).

| Objectif                   | Exemple                                       |
| -------------------------- | --------------------------------------------- |
| **Espionnage**             | Vol de documents, emails, secrets industriels |
| **Financier**              | Ransomware, fraude, extorsion                 |
| **Sabotage**               | Suppression de données, arrêt de services     |
| **Exfiltration**           | Vol massif de fichiers / bases de données     |
| **Manipulation**           | Modification de données ou transactions       |
| **Expansion de l’attaque** | Compromettre d’autres machines / comptes      |
| **Destruction**            | Wiper, corruption de systèmes                 |

- Collection vs Exfiltration vs Impact : 
	- Collection : rassembler les données intéressantes.
	- Exfiltration : Faire sortir les données de l'environnement.
	- Impact : Perturber, chiffrer, supprimer ou modifier les systèmes/données.
- Compression / Staging : 
	- Data compression : sert surtout à préparer les données.
	- Staging : Regroupement temporaire des données avant exfiltration.
- Exfiltration : 
	- Méthodes courantes : HTTPS, cloud storage, FTP/SFTP, SMB vers un autre hôte compromis, C2, DNS tunneling, services légit détournés. 
- Point de vue Defender / SOC : A ce stade, l'objectif principal est de limiter les dégâts et empêcher l'attaquant d'atteindre complétement son objectif. 
	- Contrôles importants : 
		- Network Security Monitoring, EDR, DLP, segmentation réseau, contrôle des accès aux fichiers / DB, monitoring des comptes privilégiés, détection d'archives massives, contrôle du trafic sortant, sauvegardes protégées / offline, incident response rapide.
	- A surveiller : 
		- Gros volume sortant inhabituel ;
		- Upload vers domaine rare ;
		- Archives créées juste avant transfert ;
		- Trafic nocturne inhabituel ;
		- Workstation envoyant plusieurs Go vers Internet.
- DLP : Data Loss Prevention : Permet de détecter / empêcher la sortie de données sensibles. 
- Least Privilege / Segmentation : 
	- Limiter les droits réduit l'impact : segmentation, PAM, séparation des comptes admins, ACL correctes.
### Kill Chain Unifiée (UKC)

Intéressante car plus moderne (2017 update en 2022) et prend en compte les nouvelles tendances.

La UKC regroupe **18 phases**, organisées en **3 macro-phases** :

1. **In** → Gagner un accès initial (Initial Foothold)
2. **Through** → Se propager et consolider sa position (Network Propagation)
3. **Out** → Atteindre les objectifs (Actions on Objectives)

![image 8 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-8-1.png)

#### Phase 1 - In - Initial foothold : Obtenir premier point d’entrée dans la cible
##### 1. Reconnaissance (MITRE : TA0043)
- Collecte d’information sur la cible (OSINT, scans, services, emails…)
- Passive (WHOIS, Linkedin…) & Active (Port scanning)
- Sert à identifier des vulnérabilités exploitables, employés ou creds exposés

##### 2. Weaponization (TA0001)
- Préparation de l’attaque : Création ou acquisition d’outils malveillants.
- Exemple : Configurer C2, générer payload…

##### 3. Social Engineering (TA0001)
- Manipulation humaine pour obtenir un accès.
- Exemples : phishing, spear-phishing, faux sites de login, appels téléphoniques d’ingénierie sociale.

##### 4️⃣ Exploitation (TA0002)
- Exploitation technique d’une faille (logicielle ou humaine).
- Exemples : exécution de code via une vulnérabilité web, macros malveillantes, injections, exploits 0-day.

##### 5️⃣ Persistence (TA0003)
- Maintenir un accès même après un redémarrage ou un nettoyage.
- Exemples : création de services Windows, modification de clés de registre, installation d’un web shell.

##### 6️⃣ Defence Evasion (TA0005)
- Techniques pour **éviter la détection** par les antivirus, EDR, ou IDS.
- Exemples : obfuscation, chiffrement, timestomping, désactivation de logs.

##### 7️⃣ Command & Control (TA0011)
- Mise en place d’un **canal de communication** entre l’attaquant et la machine compromise.
- Exemples : C2 via HTTP/HTTPS, DNS tunneling, ou protocoles chiffrés personnalisés.

##### 8️⃣ Pivoting (TA0008)
- Utiliser une machine compromise comme **base d’opérations** pour atteindre d’autres systèmes internes.
- Exemples : SSH tunneling, proxychains, RDP vers d’autres hôtes internes.

  

#### Phase 2 - Through (Propagation réseau) : Étendre l’accès dans le réseau et accroître les privilèges.
##### 9️⃣ Pivoting (TA0008)
- Utiliser un point d’entrée pour attaquer d’autres segments du réseau (intranet, serveurs internes).

##### 🔟 Discovery (TA0007)
- Identifier les systèmes, utilisateurs, services et configurations internes.
- Exemples : `net view`, `ipconfig /all`, `whoami`, `Get-ADUser`.

##### 1️⃣1️⃣ Privilege Escalation (TA0004)
- Obtenir des droits supérieurs (Admin, Root).
- Exemples : exploitation de vulnérabilités locales, abus de services, jetons, ou permissions faibles.

##### 1️⃣2️⃣ Execution (TA0002)
- Exécuter du code malveillant sur le système.
- Exemples : scripts PowerShell, scheduled tasks, injection de processus.

##### 1️⃣3️⃣ Credential Access (TA0006)
- Vol de mots de passe, hash, tokens ou cookies.
- Exemples : keylogging, Mimikatz, LSASS dump, vol de sessions RDP.

##### 1️⃣4️⃣ Lateral Movement (TA0008)
- Déplacement d’un système à un autre pour étendre le contrôle.
- Exemples : Pass-the-Hash, RDP, SMB exploitation.

#### Phase 3 - Out - (Actions sur objectifs) : Réaliser les buts de l’attaque (vol, destruction, rançon, etc.).
##### 1️⃣5️⃣ Collection (TA0009)
- Rassembler les données sensibles.
- Exemples : documents, bases de données, historiques de navigation, emails.

##### 1️⃣6️⃣ Exfiltration (TA0010)
- Extraire les données du réseau vers l’extérieur.
- Exemples : transfert via C2, FTP, cloud, ou dissimulation dans un flux chiffré.

##### 1️⃣7️⃣ Impact (TA0040)
- Dégrader ou détruire les ressources du système.
- Exemples : ransomware, effacement de disques, DDoS, sabotage, défacement.

##### 1️⃣8️⃣ Objectives
- Réalisation finale de la mission de l’adversaire.
- Exemples : gain financier (ransomware), espionnage, sabotage, atteinte à la réputation

|**Macro-phase**|**Objectif**|**Phases principales**|
|---|---|---|
|**IN**|Gagner un accès initial|Recon, Weaponization, Social Eng., Exploit, Persistence, Defence Evasion, C2, Pivoting|
|**THROUGH**|Se propager dans le réseau|Discovery, Priv. Escalation, Execution, Credential Access, Lateral Movement|
|**OUT**|Atteindre les objectifs finaux|Collection, Exfiltration, Impact, Objectives|

### Modèle Diamant
Représente l’unité fondamentale d’une activité malveillante à travers quatre éléments principaux reliés en forme de diamant. Chaque attaque peut être décrite par ces quatre points interconnectés, qui expliquent qui fait quoi, comment et contre qui.

![image 9 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-9-1.png)

#### Adversary (Attaquant)

L’acteur malveillant à l’origine de l’attaque

- Adversary Operator : Personne réalisation concrètement l’attaque.
- Adversary Customer : Commanditaire ou bénéficiaire de l’attaque (Entreprise, État, groupe criminel…)
- Exemple : Groupe APT chinois (Customer) mandate des opérateurs pour compro une société FR d’aéronautique afin de voler de la PI.

#### Victime (Cible)

Entité visée par l’adversaire : Une organisation, individu, domaine, IP…

- Victim Persona : Personne ou organisations ciblées (RH, dirigeants…)
- Victim Assets : Systèmes, serveurs, mail, réseaux exploités…
- Ex : Employée du service financier reçoit mail piégé, elle devient la victim persona, son ordi et son adresse mail sont les victim assets

#### Capability (Outils et techniques)

Moyens techniques utilisés par l’adversaire pour exécuter l’attaque, reflètent TTP.

- Capability Capacity : Ensemble des vuln et expositions exploitables.
- Adversary Arsenal : Ensemble des capacités de l’adversaire.
- Ex : Exploits, malwares, rootkits, scripts, techniques d’hameçonnage, brute force, obfuscation

#### Infrastructure (Moyens de déploiement)

Ressources logiques ou physiques utilisées pour livrer, héberger ou contrôler les capacités.

- Type 1 : Infra directement contrôlée par l’adversaire (Son propre serveur C2)
- Type 2 : Infra intermédiaire (serveurs compro, domaines legits piratés)
- Ex : Serveur C2, domaines de phishing, emails mailveillants, USB infecté…

#### Meta-features (informations supplémentaires)

Éléments contextualisant un événement pour l’analyse et la corrélation :

|Meta-feature|Description|Exemple|
|---|---|---|
|**Timestamp**|Date et heure de l’événement|2025-10-09 02:10:12|
|**Phase**|Étape dans la kill chain|Exploitation, Exfiltration|
|**Result**|Succès, échec, inconnu|"Integrity compromised"|
|**Direction**|Sens de l’attaque|Infrastructure → Victim|
|**Methodology**|Type d’attaque|Phishing, DDoS, Breach|
|**Resources**|Moyens nécessaires à l’attaque|Serveurs, argent, accès réseau|

#### Axes complémentaires

- Composant Social-Politique : Décrit l’intention & motivation de l’adversaire
	- Gai financier, espionnage industriel ou étatique, hacktivisme…
- Composant technologique : Décrit la relation entre la capacité et l’infrastructure
	- Comment les outils (capabilities) interagissent avec les serveurs ou vecteurs techniques (infrastructures), met en évidence les méthodes d’attaque spécifiques.

### MITRE

Organisation à but non lucratif qui créée des projets liés à la cybersécurité :

- Terminology :

|Terme|Signification|
|---|---|
|**APT** (_Advanced Persistent Threat_)|Groupe organisé (souvent étatique) menant des attaques prolongées et ciblées.|
|**TTPs**|Décrit comportement global d’un attaquant, pas juste un indicateur technique.  <br>- _T_**actic** → objectif de l’adversaire  <br>- **Technique** → méthode pour atteindre l’objectif  <br>- **Procedure** → manière concrète d’exécuter la technique|

#### ATT&CK Framework & NAVIGATOR : Décrit les attaques

Base de connaissance sur les tactiques et techniques des cyberattaquants, décrit TTP.

- For Enterprise contient 14 catégories (de reconnaissance à impact), chaque catégories contient la technique pour parvenir à sa tactique

![image 10 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-10-1.png)

- Sous chaque tactique → Plusieurs techniques, parfois déclinées en sous-techniques.

![image 11 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-11-1.png)

![image 12 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-12-1.png)

- Chaque fiche technique détaille : Description, Procedure Examples, détection, mitigation, liens avec des groupes et logiciels

![image 13 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-13-1.png)

![image 14 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-14-1.png)

##### Navigator

Permet de visualiser et d’annoter les matrices, utiles pour individualiser en fonction de soihttps://mitre-attack.github.io/attack-navigator//#layerURL=https%3A%2F%2Fattack.mitre.org%2Fgroups%2FG0008%2FG0008-enterprise-layer.json

![image 15 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-15-1.png)

![image 16 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-16-1.png)

  

#### CAR (Cyber Analytics Repository) : Explique comment les détecter

Un référentiel d’**analyses de détection** basé sur le modèle ATT&CK. CAR complète ATT&CK qui décrit les attaques, CAR explique comment les détecter. https://car.mitre.org/

- Fournit des éléments divers :
	- Pseudocodes décrivant requêtes de détection (Splunk, EQL…)
	- Références vers TTPs
	- Implémentations selon OS et outils.

![image 17 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-17-1.png)

![image 18 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-18-1.png)

![image 19 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-19-1.png)

  

#### ENGAGE : Planifier et mener opérations d’engagement adversaire

- Cyber Denial : Empêcher l’adversaire d’agir
- Cyber Deception : Le tromper volontairement
- Catégories principales (Engage Matrix) :

|Catégorie|Description|
|---|---|
|**Prepare**|Actions préliminaires menant à l’objectif|
|**Expose**|Identifier l’adversaire via la tromperie|
|**Affect**|Actions qui perturbent ses opérations|
|**Elicit**|Recueillir des infos sur son mode opératoire|
|**Understand**|Analyser les résultats obtenus|

![image 20 1.png](../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-20-1.png)

- **Engage Matrix Explorer** → permet d’explorer ces interactions.

#### D3FEND : Base de connaissance des contre-mesures cyber

- Chaque artefact contient

|   |   |
|---|---|
|**Catégorie**|**Description**|
|Definition|Information sur ce qu’est la technique|
|How it works|Comment cette technique fonctionne|
|Consideration|Chose à penser lors de l’implémentation|
|Example|Comment utiliser la technique|

#### ATT&CK Emulation Plans : Simuler attaques réelles

#### ATT&CK & Threat Intelligence : Faire lien TTP et posture défensive

### TLP

- **TLP:RED** : Réservé aux participants directs (yeux/oreilles uniquement). Pas de partage.
- **TLP:AMBER** : Partage limité au sein de l'organisation et avec les clients.
- **TLP:AMBER+STRICT** : Partage limité à l'organisation uniquement.
- **TLP:GREEN** : Partage avec la communauté (partenaires, secteur).
- **TLP:CLEAR** : Public (pas de restriction).

### L'évaluation de la confiance (Admiralty Code / NATO System)

En CTI, une info n'est jamais fiable à 100%. Tu dois ajouter comment noter tes sources.

- **Fiabilité de la source (A à F)** : De "A - Complètement fiable" à "F - Impossible à évaluer".
- **Crédibilité de l'information (1 à 6)** : De "1 - Confirmée par d'autres sources" à "6 - Impossible à évaluer".
- _Exemple :_ Une info classée **A1** est un fait avéré venant d'une source sûre. Une info **E5** est une rumeur improbable.

### Biais cognitif

|   |   |   |   |
|---|---|---|---|
|**Biais**|**Définition**|**Exemple**|**Contre-mesure**|
|**Biais de confirmation**|Chercher uniquement les preuves qui valident notre hypothèse de départ.|"Je suis sûr que c'est APT28, donc je cherche seulement des IP russes."|**ACH (Analysis of Competing Hypotheses) :** Essayer activement de prouver que son hypothèse est fausse.|
|**Biais de récence**|Donner plus d'importance aux informations reçues récemment.|"On a vu 3 attaques de ransomware hier, donc cette alerte est forcément un ransomware."|Regarder les statistiques historiques sur 12 mois.|
|**Effet de groupe**|S'aligner sur l'opinion de la majorité ou du chef sans critique.|"Si le Senior Analyst dit que c'est bénin, je ne vérifie pas."|Encourager l'avocat du diable ("Red Teaming" des idées).|
