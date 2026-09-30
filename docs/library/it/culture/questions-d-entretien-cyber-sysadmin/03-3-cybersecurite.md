---
title: 3) Cybersécurité
source: IT/Culture/Questions_Entretien_Cyber_SysAdmin.md
note: Questions d'entretien cyber & sysadmin
up:
- - Questions d'entretien cyber & sysadmin
  - index.md
---

---

- **Question : Qu'est-ce qu'une vulnérabilité ?**
  **Réponse type :** C'est une faiblesse dans un système, un logiciel, une configuration ou un processus, qui peut être exploitée pour compromettre la sécurité. Ça peut être un bug logiciel (buffer overflow), une configuration par défaut non durcie (mot de passe admin/admin), un composant non patché (CVE connue), ou une erreur de design (IDOR dans une API). Une vulnérabilité en soi ne cause pas de dommage — c'est son exploitation qui le fait.

- **Question : Qu'est-ce qu'une menace ?**
  **Réponse type :** C'est tout événement ou acteur susceptible d'exploiter une vulnérabilité et de causer un dommage. Ça peut être un acteur humain (un attaquant, un insider malveillant), un groupe organisé (APT, ransomware gang), ou un événement naturel (incendie, inondation). La menace est définie par sa capacité, son intention et son opportunité.

- **Question : Qu'est-ce qu'un risque ?**
  **Réponse type :** C'est la combinaison d'une menace exploitant une vulnérabilité, multipliée par l'impact potentiel. En gestion des risques, on l'évalue souvent comme : risque = probabilité × impact. Un risque élevé c'est quand une vulnérabilité est facilement exploitable, qu'une menace crédible existe, et que l'impact serait important. Le risque se gère de 4 façons : le réduire (patch, hardening), l'accepter (si le coût de protection dépasse l'impact), le transférer (assurance cyber), ou l'éviter (supprimer le service).

- **Question : Qu'est-ce qu'un SIEM et à quoi sert-il ?**
  **Réponse type :** Un SIEM (Security Information and Event Management) centralise et corrèle les logs de toute l'infrastructure — postes, serveurs, firewalls, proxy, AD, cloud. Il permet de détecter les incidents en temps réel via des règles de corrélation (par exemple : 50 échecs de connexion depuis la même IP en 5 minutes = probable brute force). Il fournit une vue unifiée pour l'investigation, le stockage longue durée pour la conformité, et des dashboards pour le reporting. Exemples : Splunk, Microsoft Sentinel, Elastic Security.

- **Question : Qu'est-ce qu'un IOC ?**
  **Réponse type :** Un IOC (Indicator of Compromise) est un artefact observable qui indique qu'une compromission a eu lieu ou est en cours. Ça peut être un hash de fichier malveillant, une adresse IP ou un domaine C2, une clé de registre suspecte, un user-agent inhabituel. Les IOC sont utiles pour la détection immédiate mais ils sont fragiles — l'attaquant les change facilement entre chaque campagne. C'est pour ça que la détection basée sur les TTP (comportements) est plus durable.

- **Question : Qu'est-ce que le threat hunting ?**
  **Réponse type :** C'est la recherche proactive de menaces dans le SI, guidée par une hypothèse — pas par une alerte. Le hunter cherche ce que les règles du SIEM et de l'EDR ne voient pas : les attaquants qui ont délibérément évité de déclencher les alertes. L'objectif c'est de réduire le dwell time. On part d'une hypothèse liée à une technique ATT&CK, on construit une requête, on cherche dans la télémétrie, et on documente la conclusion. Un hunt négatif n'est pas un échec — ça confirme l'absence de la menace avec le scope donné.

- **Question : Quelles sont les grandes étapes d'une réponse à incident ?**
  **Réponse type :** Le NIST 800-61 définit 4 phases : Préparation (playbooks, outillage, exercices — c'est avant l'incident), Détection et Analyse (du signal faible à l'incident confirmé, triage, scoping, timeline), Confinement-Éradication-Restauration (isoler la menace, nettoyer les persistances, reconstruire, vérifier), et Post-Incident (retex, root cause analysis, amélioration). En réalité c'est itératif — on investigue pendant qu'on contient, on découvre de nouvelles compromissions pendant l'éradication.

- **Question : Que fais-tu en premier face à un poste suspecté compromis ?**
  **Réponse type :** D'abord : ne PAS éteindre la machine — la mémoire RAM contient des preuves critiques (processus malveillants, clés de chiffrement, connexions C2). Je vérifie via l'EDR ou en consultant les logs si l'activité est confirmée suspecte. Si oui, je fais un dump mémoire (DumpIt) avant toute autre action. Ensuite j'isole le poste du réseau (sans l'éteindre), je lance un triage KAPE pour collecter les artefacts, et je vérifie si l'attaquant est présent ailleurs dans le SI. La préservation des preuves dès le début est essentielle.

- **Question : Comment vérifier rapidement si un fichier est suspect ?**
  **Réponse type :** Plusieurs vérifications rapides. D'abord le hash : calculer le SHA-256 du fichier et le chercher sur VirusTotal. Vérifier la signature numérique (sur Windows : clic droit → Propriétés → Signatures numériques, ou `Get-AuthenticodeSignature` en PowerShell) — un fichier non signé ou avec une signature invalide dans System32 est suspect. Regarder les métadonnées (date de création, taille, nom) et comparer avec ce qui est attendu. Sur un système live, vérifier avec Process Explorer si le processus associé charge des DLLs inhabituelles. Et utiliser l'outil `strings` pour extraire les chaînes lisibles — les URLs, les IPs, les clés de registre peuvent révéler la nature du fichier.

- **Question : Pourquoi la centralisation des logs est-elle importante en sécurité ?**
  **Réponse type :** Parce que la première chose qu'un attaquant fait après avoir compromis un système, c'est effacer les logs locaux. Si les logs sont centralisés dans un SIEM, il ne peut pas les supprimer. La centralisation permet aussi la corrélation : un événement isolé sur un poste ne semble pas suspect, mais corrélé avec d'autres événements sur d'autres systèmes, ça révèle un mouvement latéral ou une chaîne d'attaque. Enfin, c'est indispensable pour le forensic et la conformité — reconstituer une timeline d'attaque sur 60 jours est impossible si les logs n'ont pas été conservés.

- **Question : Quels sont les moyens de persistance d'un malware sur Linux et sur Windows ?**
  **Réponse type :** Sur Windows : clés de registre Run/RunOnce (exécution au logon), services (gérés par SCM), tâches planifiées (schtasks), DLL hijacking, COM hijacking, WMI event subscriptions, Winlogon Shell/Userinit, et des mécanismes plus avancés comme les bootkit UEFI. Autoruns de Sysinternals les recense tous. Sur Linux : cron jobs (`/etc/crontab`, `crontab -l`), services systemd (systemctl enable), scripts dans `/etc/init.d/`, fichiers `.bashrc` ou `.profile` (exécutés à l'ouverture de shell), clés SSH dans `authorized_keys`, et des modules kernel malveillants (rootkits).

- **Question : Comment est effectué un mouvement latéral ?**
  **Réponse type :** L'attaquant utilise des credentials volés pour se déplacer d'un système à un autre dans le réseau. Les techniques principales : Pass-the-Hash (utiliser un hash NTLM sans connaître le mot de passe — Mimikatz), PsExec (exécution à distance via SMB — crée un service temporaire), WMI (exécution à distance via WMI), WinRM/PowerShell Remoting, RDP, et les tâches planifiées à distance. Chaque technique laisse des traces différentes dans les logs (4624 logon type 3, 7045 création de service, etc.). C'est pourquoi la segmentation réseau, le tiering AD, et LAPS sont essentiels — ils limitent les possibilités de mouvement latéral.

- **Question : Comment faire de la reconnaissance sur une cible ?**
  **Réponse type :** En OSINT passif d'abord : Whois pour le propriétaire du domaine et les contacts, les enregistrements DNS (A, MX, TXT — SPF/DKIM/DMARC révèlent l'infrastructure mail), crt.sh pour les certificats SSL (révèle les sous-domaines), Shodan/Censys pour les services exposés, Google dorks pour les fichiers et pages indexées. LinkedIn pour les employés et la stack technique. Ensuite en actif (avec autorisation) : scan Nmap pour les ports et services, énumération DNS (transferts de zone, brute force de sous-domaines), scan de répertoires web (gobuster, dirsearch). En environnement AD interne : BloodHound/SharpHound pour les chemins d'attaque, LDAP pour l'énumération des objets AD.

- **Question : Qu'est-ce que le Kerberoasting et comment s'en protéger ?**
  **Réponse type :** Le Kerberoasting exploite le fait que tout utilisateur du domaine peut demander un ticket de service (TGS) pour n'importe quel SPN. Ce ticket est chiffré avec le hash du compte de service — si le mot de passe est faible, on le cracke en offline avec hashcat ou john. La défense principale c'est d'utiliser des gMSA (Group Managed Service Accounts) avec des mots de passe de 240 caractères rotés automatiquement. Sinon : mots de passe 25+ caractères sur les comptes de service et forcer l'AES au lieu de RC4.

- **Question : C'est quoi un DCSync et comment le détecter ?**
  **Réponse type :** Un DCSync simule un contrôleur de domaine pour demander la réplication des hashes via le protocole de réplication AD. L'attaquant a besoin des droits DS-Replication-Get-Changes et DS-Replication-Get-Changes-All. Côté détection, c'est l'Event ID 4662 avec des droits de réplication depuis une machine qui n'est PAS un DC — ça doit être une alerte critique.

---
