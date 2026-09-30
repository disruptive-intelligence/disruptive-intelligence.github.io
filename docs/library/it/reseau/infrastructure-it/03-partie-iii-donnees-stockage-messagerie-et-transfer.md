---
title: Partie III — Données, stockage, messagerie ET transferts
source: IT/03_Networking/Infrastructure_IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - index.md
---

*Comment les données sont stockées, sécurisées, échangées et sauvegardées — le patrimoine informationnel et son infrastructure.*

---


## Chapitre 12 — Bases de données relationnelles (SQL)

Le modèle relationnel (tables, colonnes, clés primaires/étrangères, relations). SQL en pratique (SELECT, JOIN, INSERT, UPDATE, DELETE — les requêtes qu'un analyste doit comprendre pour investiguer). Les SGBD majeurs : **MySQL/MariaDB** (port 3306, le plus répandu en web — fichiers my.cnf, general_log, slow_query_log), **PostgreSQL** (port 5432, le plus riche fonctionnellement — postgresql.conf, pg_log, pgaudit), **SQL Server** (port 1433, écosystème Microsoft — .mdf/.ldf, SQL Audit), **Oracle** (port 1521, grandes entreprises/legacy — Unified Auditing).

L'**injection SQL** est l'une des vulnérabilités les plus dévastatrices. Le principe : l'attaquant insère du code SQL dans un champ utilisateur que l'application concatène dans une requête sans la nettoyer. Impact : lecture de toute la base, modification ou suppression de données, exécution de commandes OS (xp_cmdshell sur SQL Server, INTO OUTFILE sur MySQL, COPY TO sur PostgreSQL), contournement d'authentification. Défense : requêtes paramétrées (prepared statements), ORM, validation des entrées, moindre privilège sur le compte DB de l'application.

Les **credentials dans les fichiers de configuration** : les mots de passe de connexion à la base sont souvent en clair dans les fichiers de conf — .my.cnf, .pgpass, web.config, .env, wp-config.php, connection strings. Un attaquant qui accède au serveur applicatif trouve souvent les credentials DB.

📋 **Logs & traces à surveiller** — Sources : slow_query_log (MySQL), pg_log (PostgreSQL), SQL Audit (SQL Server). Normal : SELECT sur les tables applicatives, connexions depuis le serveur applicatif. Suspect : UNION SELECT, SLEEP(), tentatives d'export/écriture fichier, accès aux tables système (information_schema, pg_shadow).

---


## Chapitre 13 — Bases de données NoSQL

Pourquoi NoSQL : scalabilité horizontale, schéma flexible, performances sur de gros volumes, cas d'usage spécifiques. Les types : **document** (MongoDB — port 27017), **clé-valeur** (Redis — port 6379), **colonnes** (Cassandra — port 9042), **graphe** (Neo4j — port 7474), **search** (Elasticsearch/OpenSearch — port 9200).

**MongoDB** : documents JSON/BSON dans des collections. Le risque historique : MongoDB sans authentification exposé sur Internet — des dizaines de milliers de bases ransonnées. Toujours activer l'authentification et restreindre l'écoute (bindIp: 127.0.0.1). **Redis** : base clé-valeur en mémoire, ultra-rapide (cache, sessions). Le risque : Redis sans authentification (pas de requirepass) permet l'injection de cron jobs à distance → RCE (CONFIG SET dir /var/spool/cron/ → SAVE). **Elasticsearch** : moteur de recherche full-text, backend de la stack ELK. Le risque : API port 9200 sans authentification (pas de X-Pack Security) → lecture/suppression de tous les index, exposition de logs contenant des données sensibles. **NoSQL injection** : concept similaire à l'injection SQL adapté au langage de requête NoSQL (MongoDB : { username: {$ne: null} } → bypass d'authentification).

---


## Chapitre 14 — Stockage, sauvegardes et résilience technique

*Le stockage est à la fois une surface d'attaque et le dernier rempart en cas de compromission — les ransomwares ciblent les sauvegardes en priorité.*

### 14.1 Technologies de stockage

**DAS** (Direct Attached Storage — disques locaux, le plus simple). **NAS** (Network Attached Storage — partage de fichiers en réseau via SMB/NFS, accessible depuis le LAN → attaquable depuis le LAN). **SAN** (Storage Area Network — stockage bloc haute performance via Fibre Channel ou iSCSI, normalement isolé du réseau utilisateur — sauf erreur de configuration). **Stockage objet** (S3, Azure Blob, GCS — accès via API REST, scalabilité illimitée, risque de buckets publics).

**RAID** : RAID 1 (mirroring — 2 disques identiques, survit à 1 panne), RAID 5 (parité distribuée — survit à 1 panne, capacité N-1), RAID 10 (mirroring + striping — survit à 1 panne par paire, performance + résilience). Point fondamental : **RAID ≠ sauvegarde**. RAID protège contre la panne matérielle d'un disque. Il ne protège PAS contre le ransomware (qui chiffre les données sur tous les disques du RAID simultanément), la suppression accidentelle, la corruption logique, ou l'exfiltration.

### 14.2 Sauvegardes

**Snapshots vs vraies sauvegardes** : un snapshot est une copie à un instant T dans le même système de stockage — si le stockage est chiffré par un ransomware, les snapshots le sont aussi. Une vraie sauvegarde est une copie sur un système séparé, idéalement hors ligne ou immuable.

La règle **3-2-1** : 3 copies des données, sur 2 supports différents, dont 1 hors site (cloud, bande, datacenter distant). Les **sauvegardes immuables** (WORM — Write Once Read Many) sont le contrôle anti-ransomware le plus critique : même avec un accès admin, l'attaquant ne peut pas modifier ou supprimer les sauvegardes immuables pendant la période de rétention configurée. Le **chiffrement des sauvegardes** est impératif : les sauvegardes contiennent TOUTES les données de l'organisation — si elles ne sont pas chiffrées et qu'un attaquant y accède, c'est une fuite complète.

### 14.3 Erreurs classiques

La sauvegarde sur un **NAS joint au domaine AD** est l'erreur la plus courante et la plus dévastatrice : le ransomware qui compromet le domaine chiffre aussi les sauvegardes. Le **même compte admin partout** (l'admin du domaine est admin du NAS de sauvegarde → pas d'isolation de la chaîne de sauvegarde). **Pas de test de restauration** (le jour J, on découvre que les sauvegardes sont corrompues, incomplètes, ou que la procédure de restauration prend 5 jours au lieu de 48h). Une **rétention incohérente** (30 jours de rétention mais le ransomware était dormant depuis 45 jours → les sauvegardes « propres » n'existent plus). Et **pas de segmentation du stockage** (le réseau de sauvegarde est accessible depuis le réseau utilisateur).

> **🔧 BACKBONE — Épisode 5**
>
> Lucas inspecte les sauvegardes de CargoPlex : NAS Synology joint au domaine AD, accessible en SMB depuis le réseau utilisateur, non chiffré, pas de snapshot immuable, et des tests de restauration jamais réalisés. Le NAS utilise le même compte admin que le domaine. Lucas réalise un test de restauration de l'ERP → échec partiel : les logs de transaction des 3 derniers jours sont absents. En cas de ransomware, les sauvegardes seraient chiffrées en même temps que le reste du SI, et même sans ransomware, la restauration est incomplète.

---


## Chapitre 15 — Messagerie : SMTP, sécurité email et anti-phishing

L'architecture email : **MTA** (Mail Transfer Agent — le serveur qui envoie et relaye les mails : Postfix, Exchange, Sendmail), **MDA** (Mail Delivery Agent — stocke le mail dans la boîte), **MUA** (Mail User Agent — le client : Outlook, Thunderbird, webmail). Le flux : envoi SMTP 25/587/465, réception IMAP 143/993 ou POP3 110/995.

SMTP en détail : le protocole est conversationnel (HELO/EHLO, MAIL FROM, RCPT TO, DATA). Les commandes de reconnaissance (VRFY — vérifier si un utilisateur existe, EXPN — lister les membres d'une liste — à désactiver). L'**open relay** (un serveur SMTP qui relaye les mails de n'importe qui vers n'importe qui → vecteur de spam massif — à ne jamais configurer).

La sécurité email : **SPF** (Sender Policy Framework — enregistrement TXT DNS qui liste les serveurs autorisés à envoyer des mails pour le domaine — un mail provenant d'un serveur non listé échoue la vérification SPF), **DKIM** (DomainKeys Identified Mail — signature cryptographique du mail par le serveur d'envoi — le destinataire vérifie la signature avec la clé publique dans le DNS), **DMARC** (Domain-based Message Authentication, Reporting and Conformance — politique qui dit quoi faire si SPF ou DKIM échoue : none/quarantine/reject). Les trois sont complémentaires et indispensables : SPF seul ne suffit pas (contournable), DKIM seul ne suffit pas (pas de politique de rejet), DMARC orchestre les deux et fournit du reporting.

L'anti-phishing du point de vue infrastructure : **email gateway** (filtrage entrant — analyse des URLs, sandboxing des pièces jointes, réécriture des liens), les **headers email** comme artefacts d'investigation (Received — trace le chemin du mail serveur par serveur, X-Originating-IP, Authentication-Results — résultat SPF/DKIM/DMARC, Return-Path vs From — la différence trahit le spoofing).

---


## Chapitre 16 — Partage de fichiers et transfert de données

Les protocoles de transfert : **FTP** (port 21, en clair → obsolète, ne jamais utiliser), **FTPS** (FTP + TLS — acceptable), **SFTP** (port 22, via SSH — recommandé, ce n'est PAS du FTP, c'est un sous-système SSH), **SCP** (copie simple via SSH), **rsync** (synchronisation incrémentale via SSH).

**SMB/CIFS** (Server Message Block — port 445, protocole de partage Windows) : SMBv1 est responsable de la propagation de WannaCry et NotPetya via EternalBlue (MS17-010) → **désactiver immédiatement** (Get-SmbServerConfiguration | Select EnableSMB1Protocol). SMBv2 est le minimum acceptable. SMBv3 ajoute le chiffrement et la signature — recommandé.

**NFS** (Network File System — port 2049, partage Unix) : les risques sont les exports trop larges (exporter vers * au lieu d'une IP/sous-réseau spécifique) et no_root_squash (un utilisateur root sur le client est root sur le partage → écriture de fichiers arbitraires, escalade de privilèges).

Le stockage cloud (S3, Azure Blob, GCS — accès via API REST, risque de buckets publics — des milliers de fuites documentées). Le transfert moderne (WebDAV — extension HTTP pour l'édition collaborative, MFT — Managed File Transfer — transfert sécurisé avec traçabilité).

---
