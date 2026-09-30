---
title: 'Chapitre 3 — Tradecraft et TTP : le comment opérationnel'
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
up:
- - APT — version complète
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 3.1 La Pyramide de la Douleur

La **Pyramide de la Douleur** (David Bianco, 2013) hiérarchise les indicateurs défensifs par leur coût pour l’attaquant quand ils sont brûlés.

|Niveau                  |Type d’indicateur   |Coût pour l’attaquant                                 |Durée de vie    |
|------------------------|--------------------|------------------------------------------------------|----------------|
|Base (peu douloureux)   |Hash de fichier     |Trivial (recompiler)                                  |Minutes à heures|
|                        |IP                  |Faible (changer de VPS)                               |Heures à jours  |
|                        |Nom de domaine      |Faible (acheter un nouveau)                           |Jours à semaines|
|                        |Artefact réseau/hôte|Modéré (adapter l’implant)                            |Semaines à mois |
|                        |Outils              |Fort (développer de nouveau)                          |Mois à années   |
|Sommet (très douloureux)|TTP / tradecraft    |Maximum (changer les pratiques, former les opérateurs)|Années          |

La leçon défensive fondamentale : **détecter des hashes et des IP, c’est imposer une gêne d’une journée à l’attaquant. Détecter des TTP, c’est imposer un coût qui peut lui prendre des mois à absorber.** La CTI moderne oriente l’effort vers le haut de la pyramide — c’est pour cela qu’ATT&CK est devenu le langage partagé.

Pour l’analyste APT, cela signifie : un IoC (hash, IP) est utile pour une détection immédiate, mais le renseignement qui produit une valeur durable est la description des TTP. Un rapport CTI qui liste 50 hashes a peu de valeur dans trois mois ; un rapport qui décrit précisément comment APT29 abuse des tokens SAML reste utile cinq ans.

## 3.2 Living off the Land (LotL)

Le **Living off the Land** est la pratique qui consiste à atteindre ses objectifs en utilisant exclusivement les outils légitimes présents sur le système, sans déposer de malware custom. L’avantage est la discrétion — aucun binaire suspect à détecter par signature. L’inconvénient est la traçabilité : les commandes restent loguées, et la détection se fait par anomalie comportementale.

Les **LOLBins** sont les binaires Windows qui peuvent être détournés : rundll32, regsvr32, mshta, msiexec, installutil, wmic, PowerShell, cmd, certutil, bitsadmin, schtasks, sc.exe. Le projet **LOLBAS** (lolbas-project.github.io) maintient un catalogue exhaustif avec les techniques de détournement.

Le **LotL total** (zéro malware custom) est le standard des APT les plus sophistiquées. **Volt Typhoon** est l’exemple canonique : aucun binaire malveillant identifié sur les cibles, tout passe par LOLBins + credentials légitimes. **APT29** pratique un LotL partiel — malware custom en phase 2, mais LotL en mouvement latéral et en phase d’exploration. **Sandworm** utilise davantage de malware custom (wipers, outils OT dédiés) car ses objectifs destructifs imposent des capacités spécifiques.

Pour la défense, le LotL déplace l’effort vers la **détection comportementale** : surveiller les utilisations anormales des LOLBins (PowerShell exécuté depuis un processus inhabituel, rundll32 avec des paramètres suspects, certutil utilisé pour télécharger un fichier — un usage rare pour cet outil administratif).

## 3.3 Credential access : l’arsenal moderne

Le credential access mérite un traitement détaillé car c’est la phase la plus sensible et la plus défendable.

**Mimikatz** (Benjamin Delpy, 2011) est l’outil emblématique — extraction de credentials depuis LSASS, génération de Golden Tickets et Silver Tickets, Pass-the-Hash, Pass-the-Ticket, DCSync. Détecté par les EDR modernes, il est souvent remplacé par des **réimplémentations furtives** : NanoDump (dump de LSASS en évitant les méthodes surveillées), SafetyKatz (Mimikatz refondu en C#), Rubeus (Kerberos-focused), Impacket (Python toolkit complet utilisé par quasi tous les opérateurs offensifs).

**DCSync** (T1003.006) : technique qui simule un contrôleur de domaine demandant une réplication, pour récupérer les hashs NTLM de tous les comptes du domaine. Nécessite les droits de réplication (Replicating Directory Changes / Replicating Directory Changes All). Une fois le DCSync réussi, l’attaquant a les hashs de tous les comptes, y compris le compte KRBTGT — qui permet les Golden Tickets.

**Golden Ticket** (T1558.001) : forgeage d’un ticket Kerberos TGT valide en utilisant le hash du compte KRBTGT. Résultat : l’attaquant peut s’authentifier comme n’importe quel utilisateur, avec une validité de 10 ans par défaut, sans jamais avoir à interagir avec le contrôleur de domaine pour s’authentifier. Contrer un Golden Ticket nécessite de changer le mot de passe KRBTGT deux fois — opération lourde, souvent retardée.

**Silver Ticket** (T1558.002) : forgeage d’un ticket Kerberos de service pour un service spécifique, en utilisant le hash du compte de service. Moins puissant qu’un Golden Ticket mais moins détectable (ne sollicite pas le DC).

**Kerberoasting** (T1558.003) : demander des tickets Kerberos (TGS) pour des comptes de service ayant un SPN, puis cracker les hashs hors ligne. Fonctionne si les comptes de service ont des mots de passe faibles — ce qui est fréquent historiquement. Défense : mots de passe forts pour les comptes de service (ou managed service accounts).

**AS-REP Roasting** (T1558.004) : cibler les comptes qui n’exigent pas de pré-authentification Kerberos (setting « Do not require Kerberos preauthentication »). Pour ces comptes, un attaquant peut demander directement un AS-REP chiffré avec le hash du compte, et le cracker hors ligne. Défense : éliminer le setting sauf usage documenté.

**Pass-the-Hash** (T1550.002) : s’authentifier avec un hash NTLM sans jamais avoir le mot de passe en clair. Fonctionne pour des services qui acceptent NTLM.

**Pass-the-Ticket** (T1550.003) : réutiliser un ticket Kerberos volé sur une autre machine.

**Overpass-the-Hash** : utiliser un hash NTLM pour demander un ticket Kerberos — permet de passer de NTLM à Kerberos quand seule la deuxième authentification est acceptée.

**Dans le cloud**, l’arsenal évolue : vol de **Primary Refresh Tokens** (Azure AD), **Golden SAML** (forgeage de tokens SAML via compromission d’ADFS — pivot de SolarWinds), vol de cookies de session (**pass-the-cookie** — contourne la MFA en réutilisant des sessions authentifiées), abus d’**applications OAuth** sur-permissives (technique APT29 récurrente).

## 3.4 Persistence moderne

La persistence moderne va bien au-delà des clés Run/RunOnce classiques.

**DLL Sideloading** (T1574.002) : placer une DLL malveillante dans le même répertoire qu’une application légitime qui la charge par défaut au lancement. L’application légitime exécute la DLL, qui est donc exécutée dans le contexte du processus légitime. Les APT chinoises en font un usage massif — il est difficile à détecter car la DLL n’est pas exécutée directement, elle est chargée par un processus signé et de confiance.

**COM Hijacking** (T1546.015) : détourner une clé de registre COM pour pointer vers un CLSID malveillant, qui sera chargé quand un composant COM légitime est invoqué par une application Windows normale.

**WMI Event Subscription** (T1546.003) : créer un consommateur WMI qui se déclenche sur un événement système (démarrage, connexion utilisateur, à une heure précise). Exécute le code malveillant sans fichier persistant facilement identifiable.

**Scheduled Tasks** (T1053) : tâches planifiées Windows, avec des mécanismes récents de création sans écrire dans le registre visible (Task Scheduler 2.0 COM interfaces).

**Service Creation / Modification** (T1543.003) : créer un service Windows qui exécute le malware à chaque démarrage, ou modifier un service existant. Techniques avancées : modifier le ServiceDll d’un service svchost.exe existant.

**Scheduled Tasks avec déclencheurs inhabituels** : tâches déclenchées à la connexion d’un périphérique USB, à une heure précise, à un événement du journal système.

**Bootkits / Rootkits UEFI** (T1542) : persistence au niveau du firmware. Survit à la réinstallation complète de l’OS. Techniquement complexe mais démontré par Turla (MoonBounce), CosmicStrand (groupe chinois suspecté), LoJax (APT28). Extrêmement difficile à détecter et éliminer — la machine doit être physiquement reflashée.

**Cloud persistence** : création de comptes de service Azure AD avec permissions étendues, enregistrement d’applications OAuth avec consentement administrateur, ajout de comptes aux rôles privilégiés d’Entra ID. Une compromission cloud bien installée peut survivre à la réinstallation complète de tous les endpoints.

## 3.5 Defense evasion

La defense evasion évolue en symbiose avec les EDR et les mécanismes de détection.

**Obfuscation** (T1027) à plusieurs niveaux : scripts PowerShell en base64 (détecté par beaucoup d’EDR aujourd’hui, donc combiné avec d’autres techniques), obfuscation XOR, chiffrement AES des payloads, strings chiffrées dans les binaires, noms de variables et fonctions randomisés, control-flow flattening.

**Signed Binary Proxy Execution** (T1218) : détourner des binaires Windows signés pour exécuter du code malveillant. Outil de référence : InstallUtil.exe, MSBuild.exe, RegAsm.exe, rundll32.exe, mshta.exe. L’exécution apparaît comme provenant d’un binaire légitime signé par Microsoft, ce qui contourne beaucoup de contrôles.

**Process Injection** (T1055) : injecter du code dans un processus légitime déjà en cours (explorer.exe, svchost.exe, un processus Office). Variantes techniques : classic DLL injection, reflective DLL injection, process hollowing, AtomBombing, Early Bird APC injection, Module Stomping. Chaque nouvelle technique cherche à échapper aux contrôles EDR de la génération précédente.

**EDR Bypass** : désactivation de l’EDR via des privilèges élevés, exploitation de vulnérabilités dans les drivers EDR eux-mêmes (technique « Bring Your Own Vulnerable Driver » — BYOVD, où l’attaquant déploie un driver signé mais vulnérable pour obtenir un contexte kernel et désactiver l’EDR). Cas célèbre : **RTCore64.sys** exploité par plusieurs acteurs, **PROCEXP.SYS** (un driver Sysinternals abusé), **Ryuk** et d’autres groupes ransomware ont utilisé BYOVD systématiquement.

**Timestomping** (T1070.006) : modifier les timestamps des fichiers malveillants pour qu’ils ressemblent à des fichiers système anciens, échappant aux analyses temporelles des investigateurs.

**Log Clearing** (T1070.001) : nettoyage des logs Windows (Security, System, Application, Sysmon). Détectable si les logs sont exfiltrés en temps réel vers un SIEM — d’où l’importance du log forwarding.

**Masquerading** (T1036) : nommer les fichiers malveillants avec des noms de binaires légitimes (svchost.exe placé dans un répertoire non standard, fichier malveillant nommé « Microsoft Update »), ou modifier les métadonnées (champ Description, CompanyName).

**Anti-forensics** : détection de sandbox / VM (l’implant refuse de s’exécuter si l’environnement ressemble à une sandbox analyste), effacement auto après un délai si pas de C2 reçu, mécanismes de kill switch.

## 3.6 Command and Control moderne

Le C2 moderne a évolué pour rendre la détection réseau beaucoup plus difficile.

**HTTPS comme standard** : la quasi-totalité des C2 APT passent par HTTPS, avec des certificats Let’s Encrypt (gratuits, faciles à obtenir). Le contenu est chiffré, seul le domaine/SNI et les patterns de trafic sont visibles au défenseur sans déchiffrement.

**Catégorisation des domaines** : les attaquants enregistrent des domaines plausibles (lookalike des marques connues, domaines techniques type `cdn-updates-microsoft.net`, domaines dans des TLD peu surveillés). Les domaines récents sont suspects, d’où la mise en **aging** — l’acteur enregistre un domaine, le laisse « vieillir » plusieurs mois sans activité, puis l’active.

**Domain Fronting** (T1090.004) : faire transiter le C2 via un CDN légitime (Fastly, Akamai, Azure CDN, AWS CloudFront), en exploitant le fait que les CDN routent le trafic basé sur le header Host HTTPS après le déchiffrement SNI. L’attaquant voit le trafic partir vers `cdn-legitimate.com`, mais le backend reçoit et répond via le C2 réel. Technique massivement utilisée entre 2015 et 2018 ; largement restreinte depuis par les CDN majeurs qui bloquent le domain fronting.

**Abus de services légitimes** (T1102) : utiliser Slack, Discord, Telegram, GitHub, Pastebin, Google Drive, OneDrive, Dropbox comme canaux C2. Le trafic semble légitime, les domaines sont blanc-listés par défaut. APT29 excelle dans cette technique — leur malware FoggyWeb communiquait via des cookies Exchange bien calibrés. Des implants récents utilisent des canaux Discord pour recevoir leurs commandes.

**DNS Tunneling** (T1071.004) : encoder les données dans les requêtes DNS (particulièrement les requêtes TXT et CNAME). Lent (limité par la taille des enregistrements et le throughput DNS), mais très difficile à bloquer car le DNS doit rester fonctionnel pour le réseau. Souvent utilisé comme canal secondaire en cas de blocage du canal primaire.

**Routeurs SOHO compromis comme relais** : **Volt Typhoon** a construit un botnet de routeurs résidentiels compromis (Cisco RV, Fortinet, NetGear, ASUS). Le trafic C2 des implants transite via ces routeurs — apparaissant depuis des IP résidentielles aux États-Unis ou en Asie, fondant le trafic malveillant dans le trafic domestique. Détection très difficile. Démantèlement partiel par le FBI en janvier 2024, mais le modèle se reproduit. **APT28** a utilisé la même approche avec son botnet **MooBot** démantelé en février 2024.

**Beaconing** : le pattern temporel est caractéristique. Interval de 30 minutes à 24 heures pour les opérations patientes ; quelques secondes pour l’interactif. **Jitter** (variation aléatoire) ajouté pour éviter la détection par analyse de périodicité. La détection statistique du beaconing (RITA, machine learning sur les timeseries de connexions) est une parade efficace — d’où les attaquants expérimentent des patterns moins réguliers (beacon irrégulier, synchronisation avec les horaires de travail pour se fondre).

## 3.7 OPSEC des attaquants sophistiqués

L’OPSEC distingue l’APT mature de l’amateur.

**Infrastructure compartimentée** : chaque opération a sa propre infrastructure C2, ses propres domaines, ses propres identités fictives. Une compromission découverte sur une cible ne propage pas le risque aux autres opérations. APT29 et Turla sont documentés pour cette pratique.

**Infrastructure renouvelable** : les domaines, IP, certificats sont prévus pour être jetables. Quand une infrastructure est brûlée publiquement, l’opérateur migre vers une infrastructure de remplacement déjà préparée.

**Opérateurs formés** : les APT matures ont des opérateurs entraînés, qui connaissent les techniques récentes, testent leurs actions avant de les déployer, et évitent les erreurs de débutant. Les services étatiques investissent dans la formation continue.

**Séparation des rôles** : développeurs de malware, opérateurs d’intrusion, analystes du renseignement collecté sont des rôles distincts. Le développeur ne sait pas quelle cible utilisera son implant ; l’opérateur ne voit pas le renseignement final. Cette compartimentation limite l’impact d’une trahison ou d’une infiltration.

**Heures de travail** : les opérateurs étatiques travaillent à des heures de bureau du pays sponsor. Les analyses timing ont permis d’identifier des fuseaux horaires : APT29 travaille aux heures de Moscou, les APT chinoises aux heures de Pékin (avec des variations selon les bureaux régionaux MSS), Lazarus aux heures de Pyongyang. Ce signal, seul, n’est pas probant — il peut être manipulé — mais il contribue au faisceau d’attribution.

**Langage et artefacts culturels** : les commentaires dans le code, les noms de variables, les chaînes de debug trahissent parfois la langue maternelle de l’opérateur. Les APT sophistiquées nettoient systématiquement ces artefacts, mais les erreurs arrivent.

## 3.8 L’ATT&CK framework en pratique

ATT&CK est à la fois un langage commun et une base de connaissance exploitable opérationnellement.

**Lire une matrice ATT&CK** : les colonnes sont les 14 tactiques (objectifs adversaires), les lignes sous chaque colonne sont les techniques et sous-techniques. Une intrusion est « cartographiée » en sélectionnant les techniques effectivement observées.

**Utiliser ATT&CK pour la défense** : mapper les détections existantes (quelles techniques votre SIEM/EDR/NDR détecte déjà, avec quelle fiabilité), identifier les **gaps** (quelles techniques importantes ne sont pas détectées), construire un **détection roadmap** priorisé par fréquence d’usage et impact. Des outils comme **ATT&CK Navigator** permettent la visualisation interactive.

**Prioriser par acteur** : les techniques utilisées par les acteurs pertinents pour votre secteur/géographie sont à prioriser. Si vous êtes un opérateur énergie européen, les TTP de Sandworm, Volt Typhoon, et certains clusters chinois sont plus importantes que les TTP d’APT32 (Vietnam) ou d’un groupe régional ciblant l’Amérique latine. **ATT&CK Groups** liste pour chaque groupe les techniques documentées — point de départ pour une priorisation.

**Ingérer les rapports CTI via ATT&CK** : un bon rapport CTI d’incident référence les TTP observées par leur identifiant ATT&CK. Cela permet de confronter rapidement les TTP au profil connu de groupes, et de construire des détections transférables d’un incident à l’autre.

**Les matrices spécialisées** : ATT&CK ICS (pour l’OT, voir Ch.20-21), ATT&CK Mobile (pour iOS/Android), ATT&CK Cloud (intégré à Enterprise mais avec des techniques spécifiques par plateforme). À chaque environnement sa grammaire.

La maturité CTI d’une organisation se mesure notamment à sa capacité à parler ATT&CK : non seulement connaître les techniques, mais les utiliser pour prioriser défenses, détections, exercices, et communications avec les partenaires.

-----
