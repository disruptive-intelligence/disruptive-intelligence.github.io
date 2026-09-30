---
title: PARTIE IV — INVESTIGATION ET ANALYSE
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
chapter: 5
chapters: 9
---

*Le confinement initial est en place ou en cours de décision. L'investigation approfondie commence pour reconstituer le chemin d'attaque complet, déterminer l'étendue exacte, et identifier les données compromises.*

---

### Chapitre 16 — Principes de l'investigation IR

#### 16.1 Agir vite sans détruire la preuve

La tension fondamentale de l'investigation IR : collecter des évidences (rigueur, temps) tout en fournissant des réponses rapides aux décideurs (vitesse, pragmatisme). La méthode de résolution est le triage : collecte rapide des artefacts critiques d'abord (30 minutes par machine avec KAPE ou Velociraptor), image complète ensuite (si le temps et les ressources le permettent). Le triage donne 80 % de l'information en 20 % du temps ; l'image complète donne les 20 % restants mais prend 5 fois plus longtemps.

#### 16.2 Investigation orientée décision

Chaque action d'investigation doit répondre à une question opérationnelle concrète. « Ce serveur est-il compromis ? » → pour décider de l'isoler. « L'attaquant a-t-il les privilèges domain admin ? » → pour décider de l'ampleur du confinement et du reset des comptes. « Des données personnelles ont-elles été exfiltrées ? » → pour décider de la notification CNIL. « Le krbtgt est-il compromis ? » → pour décider si un double reset est nécessaire. Si une action d'investigation ne répond à aucune question décisionnelle en cours, elle est dé-priorisée — ce n'est pas qu'elle est inutile, c'est qu'elle n'est pas urgente.

#### 16.3 Hypothèses et itérativité

L'investigateur formule des hypothèses (« le point d'entrée est probablement un phishing sur le sous-traitant RH, car le premier compte compromis est un compte VPN du sous-traitant ») et les teste contre les données. Chaque hypothèse confirmée ouvre de nouvelles pistes. L'investigation n'est pas linéaire — elle est itérative, avec des allers-retours constants entre collecte, analyse, et reformulation des hypothèses.

#### 16.4 Fil rouge — BLACKTIDE : les priorités d'investigation

> **🔍 BLACKTIDE — Épisode 16**
>
> Samedi 08h30. Nadia établit les 4 questions prioritaires pour les 12 prochaines heures, chacune assignée à un analyste :
>
> **Q1 (Thomas/PRIS) :** Quel est le patient zéro ? Remonter au point d'entrée initial. → Investigation forensic sur le poste du DRH GestPaie et les logs VPN.
>
> **Q2 (Léa/PRIS) :** Le compte krbtgt est-il compromis ? → Investigation AD, analyse des logs de réplication, vérification des tickets Kerberos.
>
> **Q3 (Karim/SOC) :** Quel est le volume exact de données exfiltrées ? Quelles données ? → Analyse des logs proxy, identification des fichiers accédés avant l'exfiltration.
>
> **Q4 (Fatima/SOC) :** L'attaquant est-il toujours actif dans le réseau ? → Surveillance temps réel des communications C2, monitoring des authentifications suspectes.

---

### Chapitre 17 — Construction de la timeline d'attaque

#### 17.1 Méthode de reconstruction

La timeline d'attaque est le livrable central de l'investigation IR. Elle reconstitue la séquence complète des actions de l'attaquant, de la compromission initiale au déploiement final, en passant par chaque étape intermédiaire. La méthode est rétrospective : partir de ce qu'on sait (l'alerte qui a déclenché l'IR) et remonter dans le temps, événement par événement, jusqu'au patient zéro.

Pour chaque événement identifié, rechercher l'événement précédent : « PsExec a été exécuté sur DC01 à 22h17 — d'où venait la session ? depuis quel poste ? avec quel compte ? ce compte était-il compromis avant ? comment ? » Remonter de machine en machine, de compte en compte, jusqu'au point d'entrée initial.

Puis reconstruire la séquence dans l'ordre chronologique, en identifiant les phases ATT&CK (voir 17.3).

#### 17.2 Corrélation multi-sources

Les logs d'une seule source ne racontent qu'une partie de l'histoire. L'Event Log Windows montre que PsExec a été exécuté, mais pas d'où venait la connexion. Le log VPN montre qu'un compte s'est connecté depuis l'extérieur, mais pas ce que l'utilisateur a fait ensuite. Le log proxy montre un flux vers AWS S3, mais pas quel processus l'a généré. La corrélation entre sources reconstitue la séquence complète.

Outils pour la construction de timeline : le SIEM (Splunk, ELK, Sentinel) pour la corrélation des logs centralisés, Plaso/log2timeline pour la construction d'une « Super Timeline » à partir des artefacts forensic d'un endpoint (fusion de la MFT, du Prefetch, des Event Logs, du registre en une seule timeline chronologique), et Timesketch pour la visualisation collaborative de la timeline résultante.

#### 17.3 Mapping ATT&CK

Chaque étape du chemin d'attaque est cartographiée sur la matrice MITRE ATT&CK. Ce mapping remplit trois fonctions : il structure le rapport final (les TTP sont décrites dans un vocabulaire normalisé que les autres équipes de sécurité comprennent), il oriente la remédiation (pour chaque technique utilisée par l'attaquant, quelle détection ou quelle mesure préventive aurait pu la contrer ?), et il facilite le partage avec la communauté (IoC + TTP ATT&CK = renseignement actionnable pour les pairs).

#### 17.4 Fil rouge — BLACKTIDE : la timeline complète

> **🔍 BLACKTIDE — Épisode 17**
>
> Après 36 heures d'investigation, la timeline est reconstituée :
>
> | Date | Action | Technique ATT&CK |
> |------|--------|-------------------|
> | J-35 (7 fév.) | Phishing ciblé sur le DRH de GestPaie — email avec pièce jointe Excel contenant macro VBA | T1566.001 — Spearphishing Attachment |
> | J-35 | Macro exécutée → téléchargement et exécution de Lumma infostealer | T1204.002 — User Execution: Malicious File |
> | J-35 | Lumma collecte credentials navigateur, cookies, credentials VPN Arvantis | T1555 — Credentials from Password Stores |
> | J-28 (12 fév.) | Première connexion VPN au réseau Arvantis avec le compte compromis (`admin_rh_ext`), 20h47 | T1078 — Valid Accounts |
> | J-25 (15 fév.) | Exécution de BloodHound pour reconnaissance AD (détecté rétrospectivement via DNS) | T1087 — Account Discovery |
> | J-21 (19 fév.) | Kerberoasting — demande de TGS pour 12 comptes de service avec SPN | T1558.003 — Kerberoasting |
> | J-21 | Crackage offline du hash du compte `svc_deploy` (mot de passe : `Deploy2024!`, 12 car.) — 4h | T1110.002 — Password Cracking |
> | J-14 (26 fév.) | DCSync sur DC01 — dump de tous les hashes NTLM, y compris krbtgt | T1003.006 — DCSync |
> | J-12 (28 fév.) | Création d'un Golden Ticket avec le hash krbtgt | T1558.001 — Golden Ticket |
> | J-12 | Création de 3 comptes admin cachés dans des OU peu surveillées | T1136.001 — Create Account: Local Account |
> | J-7 (7 mars) | Installation de rclone sur 3 serveurs internes, exfiltration vers AWS S3 | T1567.002 — Exfiltration to Cloud Storage |
> | J-7 à J-0 | Exfiltration progressive : 380 Go de données R&D et RH | T1041 — Exfiltration Over C2 Channel |
> | J-0 (14 mars) | Création d'une GPO malveillante « Windows Update Configuration » | T1484.001 — Group Policy Modification |
> | J-0, 22h10 | Déploiement de PhantomCrypt via GPO sur les serveurs de fichiers | T1486 — Data Encrypted for Impact |
> | J-0, 22h17 | Détection EDR — PsExec + désactivation Defender | T1562.001 — Disable or Modify Tools |

---

### Chapitre 18 — Cartographie des sources de données

*Ce chapitre est un référentiel : il recense et décrit les sources de données disponibles pour l'investigation IR, avec leurs forces, leurs limites, et leur localisation. Il ne traite pas de l'analyse concrète des artefacts (c'est l'objet des Ch.19-22) mais de la cartographie de ce qui existe et de ce qu'on peut en attendre.*

#### 18.1 Sources endpoint (Windows)

Les **Windows Event Logs** sont la source primaire pour l'investigation Windows. Les Event IDs critiques pour l'IR sont référencés en Annexe D avec leur interprétation détaillée. Les catégories les plus importantes : Security (authentification 4624/4625, privilèges 4672, création de processus 4688, création de compte 4720, modification de groupe 4728/4732), System (installation de service 7045), PowerShell (script block logging 4104, module logging 4103), Sysmon (si déployé — fournit une granularité très supérieure aux Event Logs natifs : création de processus avec hash et ligne de commande, connexions réseau par processus, chargement de DLL).

Les **artefacts forensic Windows** incluent le Prefetch (historique des exécutions de programmes), l'Amcache et le ShimCache (historique des programmes exécutés avec hash), la MFT et le USN Journal (journal du système de fichiers — création, modification, suppression), le registre (persistence, configuration, activité utilisateur), le SRUM (consommation réseau par processus), et les Jump Lists et Shellbags (activité de navigation dans l'explorateur). Ces artefacts sont détaillés au Ch.19.

Les **logs EDR** fournissent une telemetry riche et centralisée : exécution de processus avec arbre de parenté, connexions réseau par processus, modifications système, et détections comportementales. La rétention varie selon l'EDR (typiquement 7 à 90 jours selon la licence).

#### 18.2 Sources endpoint (Linux)

Les fichiers de log système (`/var/log/auth.log`, `/var/log/secure`, `/var/log/syslog`), les journaux d'authentification (`wtmp`, `btmp`, `lastlog`), les historiques de commandes (`bash_history`, `zsh_history`), les tâches planifiées (`crontab`, `systemd timers`), et les fichiers de configuration modifiés récemment.

#### 18.3 Sources réseau

Les logs pare-feu (flux autorisés et refusés, volumes, destinations), les logs proxy (URLs visitées, user-agents, volumes de données sortantes, codes de retour HTTP), les logs DNS (résolutions vers des domaines suspects, patterns DGA, tunneling DNS), les logs VPN (connexions, géolocalisation, durée), le NetFlow (profils de communication entre IP internes et externes, volumes), et les PCAP (captures complètes de paquets — si le NDR ou une capacité de capture existe).

#### 18.4 Sources Active Directory

Les Event Logs des contrôleurs de domaine (authentification, réplication, modifications d'objets), les logs d'Azure AD Connect (si synchronisation hybride), et les métadonnées AD (date de création et de modification des objets, membres des groupes, ACL, GPO).

#### 18.5 Sources cloud

Microsoft 365 : Unified Audit Log (rétention variable selon licence), Sign-in Logs (Entra ID), Azure Activity Log, Mailbox Audit Log. AWS : CloudTrail (API calls), VPC Flow Logs, S3 Access Logs. GCP : Cloud Audit Logs, VPC Flow Logs. Azure IaaS : Activity Log, NSG Flow Logs.

#### 18.6 Sources externes

Les feeds de threat intelligence (IoC partagés par la communauté), les bases de malware (VirusTotal, MalwareBazaar, ANY.RUN), les rapports d'éditeurs CTI (Mandiant, CrowdStrike, Recorded Future, Secureworks), et les notifications du CERT-FR.

#### 18.7 Fil rouge — BLACKTIDE : les sources mobilisées

> **🔍 BLACKTIDE — Épisode 18**
>
> Sources disponibles et exploitées : EDR CrowdStrike Falcon (telemetry 90 jours sur 92 % du parc), SIEM Splunk (9 mois de rétention — Event Logs Windows, proxy Squid, DNS Infoblox, pare-feu Palo Alto, VPN Fortinet), logs VPN Fortinet (180 jours), logs pare-feu Palo Alto (12 mois), Microsoft 365 UAL (180 jours — licence E3).
>
> Sources manquantes : pas de NDR (la visibilité réseau est limitée aux logs proxy et pare-feu — pas de capture de paquets, pas de détection de beaconing sur le trafic chiffré). Pas de Sysmon (les Event Logs natifs sont moins granulaires). PowerShell script block logging activé sur les serveurs mais pas sur les postes de travail (angle mort sur l'exécution de scripts sur les postes).

---

### Chapitre 19 — Investigation endpoint : collecte et analyse concrète

*Ce chapitre est le volet pratique de l'investigation sur les machines. Là où le Ch.18 cartographie les sources, ce chapitre montre concrètement comment collecter et interpréter les artefacts pour répondre aux questions de l'investigation.*

#### 19.1 Acquisition de preuves : triage vs image complète

Le **triage live** collecte les artefacts les plus informatifs d'une machine en 20 à 30 minutes, sans éteindre la machine. L'outil de référence est KAPE (Kroll Artifact Parser and Extractor) qui collecte automatiquement les Event Logs, le Prefetch, l'Amcache, le ShimCache, le registre, le SRUM, les Scheduled Tasks, les services, les fichiers récents, et d'autres artefacts configurables. Velociraptor offre une capacité similaire mais avec la possibilité de déployer la collecte à distance sur des centaines de machines simultanément — essentiel quand le périmètre de compromission est large. Le triage est la méthode par défaut en IR : il donne 80 % de l'information en 20 % du temps.

L'**image complète** (bit-à-bit) capture l'intégralité du disque. Outils : FTK Imager (interface graphique, Windows), dd/dcfldd (ligne de commande, Linux), ou acquisition via EDR pour les environnements cloud. L'image est nécessaire quand la chaîne de custody doit être préservée pour une procédure judiciaire, quand une analyse approfondie est requise (analyse de la MFT complète, carving de fichiers supprimés, analyse du slack space), ou quand le triage n'a pas donné de résultats concluants.

L'**acquisition mémoire** capture la RAM de la machine en cours d'exécution. Outils : DumpIt (Windows, simple et rapide), WinPmem (Windows, plus flexible), ou LiME (Linux). L'acquisition mémoire doit être faite AVANT tout redémarrage — la mémoire est la source la plus volatile. Elle est indispensable pour les malwares fileless (qui n'écrivent rien sur le disque), pour l'extraction de credentials en mémoire (hashes NTLM dans le processus lsass), et pour l'analyse des connexions réseau actives.

**Chaîne de custody :** chaque acquisition est documentée : qui (nom de l'analyste), quoi (machine, artefact), quand (horodatage précis), avec quel outil (nom, version), et hash de vérification (SHA256 calculé immédiatement). Le formulaire de chaîne de custody est en Annexe C.

#### 19.2 Analyse mémoire

L'analyse de la mémoire vive avec **Volatility 3** (l'outil de référence open source) permet d'extraire les processus en cours d'exécution (`windows.pslist`, `windows.pstree` — identifier les processus suspects par leur arbre de parenté, leur chemin d'exécution, ou leur nom), les DLL chargées (`windows.dlllist` — identifier les DLL injectées ou suspectes), les connexions réseau actives (`windows.netscan` — les connexions vers le C2 sont directement visibles), les credentials en mémoire (hashes NTLM extraits du processus lsass — si mimikatz ou un outil similaire a été exécuté, les credentials déchiffrées peuvent encore être en mémoire), les commandes exécutées (`windows.cmdline` — les arguments passés aux processus), et le code injecté (`windows.malfind` — détection de zones mémoire suspectes dans les processus, indicatrices d'injection de code).

L'analyse mémoire est indispensable quand le malware est fileless (il s'exécute uniquement en mémoire, sans écrire de fichier sur le disque), quand l'attaquant utilise le process hollowing ou le reflective DLL loading (techniques d'évasion qui injectent du code dans des processus légitimes), et pour capturer les credentials actives (les hashes NTLM dans lsass permettent de comprendre quels comptes l'attaquant a compromis).

#### 19.3 Artefacts système Windows — interprétation pour l'IR

Le **Prefetch** (situé dans `C:\Windows\Prefetch\`) enregistre les programmes exécutés, avec le nom du fichier, les 8 dernières dates/heures d'exécution, et le nombre total d'exécutions. En IR, le Prefetch révèle l'exécution d'outils de l'attaquant (PsExec, mimikatz, rclone, ransomware builder) même si les fichiers ont été supprimés depuis.

L'**Amcache** (`C:\Windows\AppCompat\Programs\Amcache.hve`) et le **ShimCache** enregistrent les programmes exécutés avec leur hash SHA1 et leur chemin — permettant de confirmer que le binaire malveillant a bien été exécuté et d'en identifier le hash pour enrichissement CTI.

La **MFT** (Master File Table) et le **USN Journal** sont le journal du système de fichiers NTFS. Ils enregistrent la création, la modification, le renommage, et la suppression de fichiers avec horodatage. En IR, ils révèlent les fichiers créés par l'attaquant (scripts, binaires, fichiers de staging), les fichiers supprimés (l'attaquant nettoie souvent ses traces), et les mouvements de données (fichiers copiés vers un répertoire de staging avant exfiltration).

Le **registre Windows** contient des informations critiques pour l'IR : les clés `Run`/`RunOnce` (persistence via exécution automatique au démarrage), les services (persistence via création de service), les clés `UserAssist` (historique des programmes exécutés via l'interface graphique), les clés `BAM`/`DAM` (programmes exécutés avec horodatage, disponibles sur Windows 10/11 et Server 2016+), et les informations réseau (profils WiFi, historique des connexions).

Le **SRUM** (System Resource Usage Monitor, `C:\Windows\System32\SRU\SRUDB.dat`) enregistre la consommation réseau par processus sur 30 à 60 jours. En IR, il révèle les processus ayant généré du trafic réseau significatif — excellent pour détecter l'exfiltration (un processus rclone ayant transféré 380 Go sera visible dans le SRUM même si le processus n'est plus en cours d'exécution).

#### 19.4 Analyse malware first-pass

L'IR n'est pas du reverse engineering approfondi, mais un first-pass rapide sur le malware est essentiel pour extraire les IoC et comprendre le comportement. L'analyse statique rapide (strings — extraire les chaînes de caractères pour identifier les URLs, les IP, les clés de registre, les noms de fichiers ; imports — identifier les API Windows utilisées ; sections PE — identifier les sections suspectes ou packé) et la soumission en sandbox (ANY.RUN, Joe Sandbox, CAPE — exécution contrôlée avec observation du comportement réseau, des modifications système, et des artefacts créés) suffisent généralement pour l'IR. Le reverse engineering approfondi (décompilation, analyse du code assembleur) est délégué aux analystes malware spécialisés ou au prestataire PRIS.

#### 19.5 Fil rouge — BLACKTIDE : le forensic sur le DC

> **🔍 BLACKTIDE — Épisode 19**
>
> Samedi 09h00-14h00. Thomas (PRIS) priorise DC01 — le contrôleur de domaine principal, le plus compromis.
>
> **Acquisition mémoire (DumpIt) :** 32 Go, 12 minutes. L'analyse Volatility révèle un processus `lsass.exe` avec des zones mémoire modifiées (malfind positif — injection de code), des credentials en clair de 12 comptes admin dans la mémoire de lsass, et un processus `svchost.exe` suspect avec une connexion active vers le C2 `update-srv-infra[.]xyz` sur le port 443.
>
> **Triage KAPE (DC01, DC02, DC03) :** 20 minutes par machine. Le Prefetch confirme l'exécution de `psexec.exe`, `rclone.exe`, `bc.exe` (le builder PhantomCrypt), et `mimikatz.exe`. L'Amcache fournit les hashes SHA1 de tous ces binaires. Le SRUM de DC01 montre que `rclone.exe` a transféré 147 Go de données réseau sur les 7 derniers jours (une partie des 380 Go totaux). Les Scheduled Tasks révèlent une tâche `WindowsUpdateCheck` créée à J-12, exécutant un script PowerShell obfusqué toutes les 4 heures — mécanisme de persistence.
>
> **Constat :** David, l'admin d'astreinte, a redémarré les serveurs de fichiers FS01-Lyon et FS01-Fos à 23h30 la veille (« pour stopper le chiffrement »). La mémoire de ces serveurs est perdue. Les artefacts Prefetch et Amcache sont préservés (ils sont sur disque), mais les connexions réseau actives et les credentials en mémoire sont irrémédiablement perdus. Nadia documente : « Perte de preuve — RAM de FS01-Lyon et FS01-Fos — cause : redémarrage sans collecte préalable. »

---

### Chapitre 20 — Investigation identité et Active Directory

#### 20.1 Pourquoi l'AD est la cible ultime

Dans la quasi-totalité des compromissions Windows, l'objectif stratégique de l'attaquant est le contrôle de l'Active Directory. L'AD gère l'authentification de tous les utilisateurs, les autorisations sur toutes les ressources, le déploiement de logiciels et de configurations via GPO, et les secrets (hashes NTLM, clés Kerberos, mots de passe en clair dans certains cas). Compromettre l'AD signifie contrôler l'ensemble du SI Windows — c'est pourquoi l'investigation AD est la composante la plus critique de l'IR dans un environnement Windows.

#### 20.2 Techniques d'attaque AD et leur détection

**Kerberoasting :** l'attaquant demande des TGS (Ticket Granting Service) pour des comptes de service ayant un SPN (Service Principal Name), puis cracke les tickets offline pour obtenir le mot de passe en clair. Détection : Event ID 4769 avec encryption type RC4 (0x17), en volume anormal. Implication IR : si un compte de service avec droits DA a un mot de passe faible, il a été compromis.

**DCSync :** l'attaquant simule un contrôleur de domaine pour demander la réplication des hashes NTLM de tous les comptes, y compris le krbtgt. Détection : Event ID 4662 avec les GUID de réplication (`1131f6ad-...` et `1131f6aa-...`), provenant d'une machine qui n'est pas un DC. Implication IR : si le DCSync a réussi, TOUS les hashes sont compromis — y compris le krbtgt (Golden Ticket possible).

**Golden Ticket :** l'attaquant forge un TGT (Ticket Granting Ticket) avec le hash du compte krbtgt, lui donnant un accès illimité au domaine, sans expiration normale. Détection : anomalies dans les tickets Kerberos (lifetime anormalement long, SID incohérent), Event ID 4769 avec des tickets dont les propriétés ne correspondent pas à la politique du domaine. Implication IR : si un Golden Ticket a été créé, l'attaquant peut s'authentifier comme n'importe quel utilisateur du domaine, même après un reset des mots de passe — seul un double reset du krbtgt invalide les Golden Tickets.

**Modifications d'ACL/DACL :** l'attaquant modifie les permissions sur des objets AD (OU, groupes, comptes) pour se donner des droits persistants (GenericAll, WriteDACL, AddMember). Ces modifications sont subtiles et difficiles à détecter sans un audit AD dédié. Outils de détection : BloodHound (visualisation des chemins d'attaque), PingCastle (score de sécurité AD et identification des faiblesses), Purple Knight (audit automatisé).

#### 20.3 Évaluation de la profondeur de compromission

Les questions critiques que l'investigateur doit trancher pour déterminer le plan d'éradication :

Le **krbtgt est-il compromis ?** Si oui → le double reset est obligatoire (Ch.27). Un seul reset ne suffit pas car Kerberos retient les 2 derniers mots de passe du krbtgt — il faut donc 2 resets espacés de 12h minimum pour invalider tous les tickets.

Des **comptes admin cachés** ont-ils été créés ? Vérification de tous les groupes privilégiés (Domain Admins, Enterprise Admins, Schema Admins, Administrators, mais aussi les groupes avec des délégations non standard) et de toutes les créations de comptes récentes.

Des **GPO malveillantes** existent-elles ? Revue de toutes les GPO créées ou modifiées récemment — une GPO malveillante peut déployer du malware, désactiver des défenses, ou modifier des configurations de sécurité sur tout le parc.

Les **ACL/DACL** ont-elles été modifiées ? Des permissions anormales sur des objets critiques (OU des DC, OU des serveurs, comptes de service) peuvent permettre une re-compromission même après éradication.

#### 20.4 Fil rouge — BLACKTIDE : la profondeur de la compromission AD

> **🔍 BLACKTIDE — Épisode 20**
>
> Samedi 14h00. Léa (PRIS, spécialiste AD) présente ses conclusions à la cellule technique.
>
> **DCSync confirmé** sur DC01 à J-14. L'attaquant a obtenu tous les hashes NTLM du domaine, y compris le hash du krbtgt. **→ Golden Ticket possible et probable.**
>
> **Golden Ticket utilisé.** L'analyse des logs Kerberos montre des TGT avec un lifetime de 10 ans (la politique du domaine est de 10 heures) — signature d'un Golden Ticket.
>
> **3 comptes admin cachés** créés à J-12 dans l'OU `OU=ServiceAccounts,OU=IT,DC=arvantis,DC=local` : `svc_monitor01`, `svc_backup_ext`, `svc_audit_temp`. Noms choisis pour se fondre dans les comptes de service légitimes. Tous membres du groupe Domain Admins.
>
> **1 GPO malveillante** : « Windows Update Configuration » créée à J-0, liée aux OU des serveurs de fichiers, exécutant le ransomware PhantomCrypt via un script de démarrage.
>
> **Modification des ACL** : GenericAll attribué au compte `svc_deploy` (le compte compromis) sur l'OU des serveurs critiques — permettant à ce compte de modifier n'importe quel objet dans cette OU.
>
> **DSRM password** : non modifié par l'attaquant (il n'en a pas eu besoin — le Golden Ticket lui suffisait).
>
> **Conclusion de Léa :** « L'AD est compromis en profondeur. Un simple reset de mots de passe ne suffit pas. Il faut un double reset du krbtgt, la suppression des 3 comptes cachés, le retrait de la GPO malveillante, et la correction des ACL. La reconstruction complète de l'AD n'est pas strictement nécessaire si ces actions sont menées proprement, mais le risque résiduel n'est pas nul. »

---

### Chapitre 21 — Investigation réseau et exfiltration

#### 21.1 Identification des communications C2

Les communications C2 (Command and Control) sont le lien entre le malware et l'attaquant. Leur identification est un objectif prioritaire de l'investigation réseau car elles révèlent les machines compromises et les destinations de l'attaquant.

Le **beaconing** est le pattern le plus courant : le malware contacte le C2 à intervalles réguliers (toutes les 30 secondes, toutes les 5 minutes) pour recevoir des instructions. Les attaquants sophistiqués ajoutent du jitter (variation aléatoire de l'intervalle) pour simuler du trafic humain, mais le pattern reste détectable par analyse statistique. Le **DNS tunneling** utilise les requêtes DNS pour encapsuler des données — un volume anormal de requêtes DNS vers un même domaine, ou des requêtes avec des sous-domaines longs et encodés, sont des indicateurs. Le **fingerprinting TLS** (JA3/JA4) permet d'identifier des clients TLS suspects même sur du trafic chiffré — le hash JA3 du client TLS d'un malware est souvent distinct de celui d'un navigateur légitime.

#### 21.2 Identification de l'exfiltration

L'exfiltration est souvent la composante la plus difficile à détecter et à quantifier. Les indicateurs incluent un volume anormal de trafic sortant par rapport à la baseline, des flux vers des services cloud non autorisés (Mega, file.io, transfer.sh, ou des instances AWS/Azure/GCP louées à la demande), des connexions longue durée vers des IP inconnues, et l'utilisation d'outils de transfert identifiables (rclone a un user-agent caractéristique dans les logs proxy, WinSCP et FTP ont des empreintes réseau spécifiques).

L'estimation du volume exfiltré est cruciale pour la CNIL (la notification doit indiquer le nombre de personnes et le type de données concernées), pour la communication de crise (« avons-nous perdu nos secrets industriels ? »), et pour la décision sur la rançon (si les données sont déjà exfiltrées, payer ne les « dé-exfiltrera » pas).

Le cas du **living off trusted services** : les attaquants utilisent de plus en plus des services légitimes pour l'exfiltration (AWS S3, Azure Blob, Google Drive, OneDrive). Ces flux passent les contrôles de sécurité (les domaines sont réputés légitimes) et sont invisibles aux filtres URL. La détection repose sur l'identification des outils (rclone, aws-cli) via les user-agents proxy, l'analyse volumétrique, et la corrélation avec les autres IoC.

#### 21.3 Fil rouge — BLACKTIDE : l'exfiltration

> **🔍 BLACKTIDE — Épisode 21**
>
> Karim analyse les logs proxy (Squid) pour reconstituer l'exfiltration. Il identifie des connexions HTTPS vers `s3.eu-west-1.amazonaws.com` depuis 3 machines internes (10.42.15.87, 10.42.15.92, 10.42.10.45), totalisant 380 Go sur 7 jours (J-7 à J-0). Le user-agent est `rclone/v1.65.0` — confirmant l'utilisation de rclone, un outil de synchronisation cloud légitime détourné par l'attaquant.
>
> Les données exfiltrées sont identifiées par corrélation avec les logs d'accès aux partages de fichiers (Event ID 5140/5145) : accès massif aux partages `\\FS01-Lyon\R&D`, `\\FS01-Fos\Projets`, et `\\FS01-Lyon\RH` dans les 7 jours précédant l'exfiltration. Le volume se répartit en environ 310 Go de données R&D (formules chimiques, procédés de fabrication, brevets en cours) et 70 Go de données RH (fiches de paie, contrats, données de sécurité sociale de 8 000 employés).
>
> Le serveur de staging est une instance EC2 AWS en région `eu-west-1` (Irlande). L'identification du locataire nécessitera une réquisition judiciaire auprès d'AWS.

---

### Chapitre 22 — Investigation des environnements hybrides, OT et dépendances tierces

*Ce chapitre est un panorama qui traite trois environnements d'investigation spécifiques, chacun avec ses propres contraintes. Il assume explicitement un traitement moins approfondi que les chapitres précédents sur chaque volet, en renvoyant vers les cours spécialisés de la bibliothèque.*

#### 22.1 Investigation cloud (Microsoft 365 / Entra ID)

Les compromissions cloud suivent des logiques différentes de l'on-premise. L'attaquant ne « compromet » pas un serveur — il vole un token, il abuse d'un consentement OAuth, il modifie une conditional access policy. L'investigation repose sur les **Sign-in Logs** d'Entra ID (connexions, y compris les échecs, avec géolocalisation et device info), les **Unified Audit Logs** (toutes les actions administratives et utilisateur dans M365 — création de règles de forwarding, accès aux mailboxes, modifications de configuration, ajout d'app registrations), et les **Azure Activity Logs** (si Azure IaaS/PaaS est utilisé).

Les pièges spécifiques au cloud : la rétention des logs dépend de la licence (180 jours en E3, jusqu'à 365 jours en E5 pour certains types de logs), les tokens volés permettent un accès persistant même après reset du mot de passe (il faut révoquer explicitement les refresh tokens), et les app registrations malveillantes peuvent fournir un accès API permanent sans interaction utilisateur.

#### 22.2 Investigation OT/ICS

L'investigation en environnement OT (Operational Technology) est contrainte par des réalités physiques que l'IT ne connaît pas. Les systèmes ne sont pas patchables (un automate en production ne peut pas être redémarré pour appliquer un correctif), les protocoles sont propriétaires (Modbus, S7, OPC-UA — les outils d'investigation réseau classiques ne les comprennent pas), les logs centralisés sont rares (les automates n'envoient pas de syslog au SIEM), les agents EDR ne peuvent pas être déployés sur les PLC (Programmable Logic Controllers), et les contraintes de disponibilité sont extrêmes (arrêter un automate dans une usine chimique peut causer un accident physique).

La plupart des incidents OT commencent par une compromission IT qui pivote vers le réseau OT via les passerelles de supervision (SCADA), les jump servers, ou les postes d'ingénierie à double connexion (un poste connecté à la fois au réseau IT et au réseau OT — c'est exactement le cas de BLACKTIDE). L'investigation OT est donc souvent une extension de l'investigation IT, menée conjointement avec les ingénieurs de production.

L'évaluation critique : l'attaquant a-t-il atteint les systèmes de contrôle ? A-t-il modifié des configurations d'automates ? A-t-il la capacité de causer un dommage physique ? Ces questions déterminent le niveau d'urgence et la mobilisation de compétences spécialisées (CERT-FR dispose d'équipes OT déployables sur les OIV).

#### 22.3 Investigation supply chain et dépendances tierces

Quand l'incident provient d'un tiers de confiance (mise à jour logicielle piégée, accès VPN prestataire compromis, dépendance SaaS compromise), l'investigation dépasse le périmètre de l'organisation. Le scoping doit considérer tous les systèmes ayant interagi avec le tiers compromis, la coordination avec le fournisseur est indispensable (mais souvent lente, juridiquement complexe, et politiquement sensible), et l'évaluation de l'impact doit considérer le cas où le tiers a été un vecteur vers d'autres clients.

Dans le cas de BLACKTIDE, le point d'entrée est la compromission du sous-traitant RH GestPaie — un cas classique de supply chain via prestataire. L'infostealer sur le poste du DRH de GestPaie a fourni les credentials VPN d'Arvantis. La question de la responsabilité contractuelle (GestPaie avait-elle une obligation de MFA sur ses postes ?) est un enjeu juridique post-incident.

#### 22.4 Fil rouge — BLACKTIDE : les volets spécifiques

> **🔍 BLACKTIDE — Épisode 22**
>
> **Cloud :** l'attaquant a utilisé un token volé d'un admin M365 (obtenu via le DCSync — le hash NTLM du compte a permis un pass-the-hash vers Entra ID via Azure AD Connect sync). Il a créé une règle de forwarding sur la boîte mail du CFO (toutes les PJ PDF redirigées vers une adresse ProtonMail externe). La règle est active depuis J-10. Les UAL E3 (180 jours) permettent de confirmer qu'aucune autre manipulation M365 n'a eu lieu.
>
> **OT :** le site OIV de Fos-sur-Mer utilise un SCADA Schneider Electric pour le contrôle des réacteurs. L'investigation révèle que l'attaquant a atteint le poste d'ingénierie OT (Windows 10, connecté au réseau IT via un second adaptateur réseau — la segmentation IT/OT reposait uniquement sur un VLAN, pas sur un pare-feu physique). Le ransomware a chiffré le poste d'ingénierie mais PAS les PLC Schneider (pas de système de fichiers Windows sur les automates). L'ANSSI déploie une équipe CERT-FR spécialisée OT le lundi pour vérifier l'intégrité des configurations SCADA.
>
> **Supply chain :** GestPaie est notifié de la compromission de son poste DRH le samedi matin. Réponse : « On va regarder. » Arvantis désactive immédiatement l'accès VPN de GestPaie et demande un audit de sécurité contractuel (la clause existe dans le contrat de prestation).

---
