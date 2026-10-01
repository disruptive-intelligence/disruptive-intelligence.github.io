---
title: 'Partie IV — Use cases : scénarios de menace'
source: Cyber/06 Détection & réponse/Analyste SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - index.md
---

*Chaque use case est un chapitre complet qui enseigne un grand schéma de menace avec sa logique de détection et sa réponse. La Partie III enseignait les méthodes d'investigation par domaine (endpoint, identité, réseau, cloud). La Partie IV enseigne comment ces méthodes s'appliquent face à chaque type de menace.*

---


## Chapitre 19 — Phishing et compromission de credentials

Le scénario complet, de l'email malveillant à la post-exploitation. L'email de phishing arrive (détection email gateway — liens suspects, pièces jointes malveillantes, SPF/DKIM/DMARC fail, domaine de typosquatting). L'utilisateur clique sur le lien (détection proxy — accès à une URL catégorisée « phishing » ou vers un domaine récemment enregistré). L'utilisateur soumet ses credentials sur le faux portail (détection proxy — POST vers un domaine suspect après un clic depuis un email). L'attaquant se connecte avec les credentials volées (détection Azure AD — connexion depuis une nouvelle IP/géolocalisation, sans le device habituel, potentiellement sans MFA si token replay). Post-exploitation : création de règle de forwarding Outlook (détection UAL — `New-InboxRule` avec `ForwardTo`), accès aux données SharePoint/OneDrive (détection UAL — `FileDownloaded` en volume), envoi de phishing interne depuis le compte compromis (détection email gateway — le même compte envoie des emails inhabituels à de nombreux destinataires).

Règle Sigma pour la détection de forwarding rule suspecte. Playbook complet : scope (d'autres ont-ils reçu le même email ?), vérification des clics (proxy), vérification des soumissions de credentials (POST dans le proxy), reset credentials + révocation de sessions + révocation de refresh tokens si compromission confirmée, vérification des inbox rules, blocage du domaine/URL au proxy et à l'email gateway, notification et sensibilisation de l'utilisateur.

Variante AitM : le kit de phishing (EvilGinx2, Modlishka) intercepte le token de session MFA en temps réel — la détection par anomalie post-authentification (nouvelle IP, absence de device enrollment, changement de comportement) remplace la détection par absence de MFA.

---


## Chapitre 20 — Mouvement latéral et escalade de privilèges

Les techniques de mouvement latéral avec leurs artefacts de détection. **PsExec** : Event ID 7045 (service PSEXESVC installé sur la machine destination), 4624 type 3 (logon réseau depuis la machine source), et le Prefetch de psexec.exe sur la machine source. **WMI** : Event ID 4688 avec `wmiprvse.exe` comme parent sur la machine destination, et les logs WMI-Activity/Operational. **RDP** : Event IDs 21/22/25 dans le canal TerminalServices-RemoteConnectionManager, 4624 type 10, et le bitmap cache RDP. **SMB lateral movement** : Event ID 5140 (accès à un partage — notamment ADMIN$, C$, IPC$), 5145 (audit granulaire d'accès aux fichiers partagés).

Les techniques d'escalade de privilèges. **Kerberoasting** (4769 avec encryption RC4 en rafale), **AS-REP Roasting** (4768 sans pré-authentification), **DCSync** (4662 avec les GUID de réplication depuis une machine qui n'est PAS un DC). Chaque technique avec sa règle Sigma commentée.

La difficulté opérationnelle : distinguer l'admin IT légitime de l'attaquant. PsExec est utilisé quotidiennement par l'IT — la détection repose sur le contexte (PsExec depuis un poste non-IT, vers un serveur critique, à 3h du matin, avec un compte compromis = suspect) et sur la corrélation avec d'autres indicateurs (PsExec + accès LSASS + Kerberoasting = chaîne d'attaque, pas administration légitime).

---


## Chapitre 21 — Exécution et persistence malveillante

Détection de l'exécution suspecte : PowerShell obfusqué (`-EncodedCommand`, `Invoke-Expression` avec download, `-WindowStyle Hidden`), LOLBins (certutil `-urlcache`, mshta avec URL, bitsadmin `/transfer`, regsvr32 `/s /u /n /i:` — chaque binaire légitime détourné avec sa signature de détection et ses faux positifs), et process trees anormaux (svchost.exe avec un parent qui n'est pas services.exe, rundll32.exe sans argument — indicateurs de process injection ou de process hollowing).

Détection de la persistence : clés registre Run/RunOnce (Event ID 13 Sysmon — modification de registre), services Windows (Event ID 7045 — installation de service, avec attention aux services avec des chemins d'exécutable dans des répertoires temporaires ou des noms aléatoires), tâches planifiées (Event ID 4698 — création, avec analyse du contenu XML de la tâche), WMI event subscriptions (les plus discrètes — détectables via `Get-WMIObject -Namespace root\Subscription`), et DLL sideloading (Event ID 7 Sysmon — DLL non signée chargée dans le répertoire d'une application légitime).

---


## Chapitre 22 — Exfiltration et communication C2

Détection de l'exfiltration : volume anormal de données sortantes (agrégation par utilisateur et destination dans les logs proxy/firewall — un utilisateur qui uploade 12 Go vers mega.nz en 4 heures n'est pas un comportement normal), upload vers des services de partage (détection par catégorisation proxy ou par domaine — mega.nz, transfer.sh, anonfiles, gofile), DNS tunneling (entropie élevée des sous-domaines, volume de requêtes vers un domaine unique, taille inhabituelle des réponses DNS), et rclone/cloud sync (détection de l'exécutable par hash ou nom de processus, ou de ses patterns de connexion vers des endpoints S3/Azure Blob/GDrive).

Détection du C2 : beaconing (analyse statistique des intervalles de connexion — un processus qui contacte une IP avec un intervalle régulier de 45 secondes ± 5 % est un automate ; requête SPL/KQL avec calcul de moyenne et d'écart-type des intervalles), JA3/JA4 fingerprints (le JA3 d'un RAT custom est différent de celui d'un navigateur Chrome — détectable même sur du trafic chiffré), domaines DGA (entropie élevée et longueur anormale du domaine — les algorithmes de génération produisent des domaines comme `xj7kzp2m9q.xyz`), et connexions vers des IP sans domaine associé (les serveurs C2 sont souvent des VPS sans nom de domaine légitime — une connexion HTTPS vers une IP nue est suspecte).

---


## Chapitre 23 — Ransomware : détection pré-déploiement et réponse

Le ransomware est la dernière étape d'une chaîne d'attaque — les précurseurs sont détectables si le SOC sait quoi chercher. Les **précurseurs** (détectables heures à jours avant le chiffrement) : reconnaissance interne (scans réseau avec Advanced IP Scanner, énumération AD avec BloodHound/ADFind/nltest/`net group "Domain Admins" /domain`), mouvement latéral (PsExec, RDP, SMB — voir Ch.18), désactivation des défenses (arrêt de l'antivirus via PowerShell ou GPO, modification des GPO de sécurité, suppression des shadow copies — `vssadmin delete shadows /all` est un signal critique quasi-pathognomonique du pré-ransomware), et staging de données (copie vers un serveur de staging avant exfiltration — double extorsion).

La **golden hour** : les 1 à 4 heures entre le mouvement latéral confirmé et le déploiement du ransomware. C'est la fenêtre de détection critique. Si le SOC détecte et confine pendant cette fenêtre, le ransomware est évité. Si la fenêtre est ratée, le chiffrement commence et les options se réduisent.

Playbook ransomware : isolation immédiate des machines détectées (EDR containment), isolation réseau du segment (firewall — couper les communications entre segments pour empêcher la propagation), vérification de l'étendue (quelles machines contactent le C2 ? quelles machines ont eu des shadow copies supprimées ?), préservation des preuves (ne pas redémarrer, ne pas nettoyer), et escalade IR immédiate.

---
