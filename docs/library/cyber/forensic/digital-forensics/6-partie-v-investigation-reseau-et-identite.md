---
title: PARTIE V — INVESTIGATION RÉSEAU ET IDENTITÉ
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
chapter: 6
chapters: 9
---

*Partie dédiée aux investigations qui dépassent le périmètre d'un seul endpoint : l'analyse du trafic réseau, l'investigation de l'Active Directory, et l'investigation des identités hybrides et du cloud.*

---

### Chapitre 19 — Network forensics

#### 19.1 Ce que le réseau raconte

Le réseau est le terrain de jeu de l'attaquant pour la communication C2 (commandes envoyées au malware), le mouvement latéral (progression entre machines), et l'exfiltration (envoi des données volées vers l'extérieur). L'analyse réseau répond à des questions que le forensic endpoint seul ne peut pas couvrir : avec qui la machine compromise communique-t-elle ? quel volume de données a été transféré ? quels autres systèmes ont été contactés ?

#### 19.2 Analyse PCAP avec Wireshark

Wireshark est l'outil de référence pour l'analyse de captures de paquets. Les filtres les plus utiles pour le forensic : `ip.addr == 103.xx.xx.xx` (isoler le trafic vers/depuis le C2), `http.request.method == POST` (identifier les données envoyées en HTTP — potentielle exfiltration), `dns.qry.name contains "suspect"` (résolutions DNS suspectes), `tcp.flags.syn == 1 && tcp.flags.ack == 0` (nouvelles connexions TCP — identifier les scans), et `tls.handshake.type == 1` (Client Hello — pour l'analyse JA3). La reconstruction de sessions TCP (`Follow TCP Stream`) permet de lire le contenu des communications non chiffrées. L'extraction de fichiers (`File > Export Objects > HTTP/SMB/...`) récupère les fichiers transférés via le réseau.

#### 19.3 Détection de C2 et beaconing

Le beaconing est le pattern de communication le plus courant des malwares C2 : le malware contacte le serveur de l'attaquant à intervalles réguliers pour recevoir des instructions. La détection repose sur l'analyse statistique des intervalles de connexion : un processus qui contacte la même IP toutes les 30 minutes (± un jitter de 10 %) pendant 60 jours n'est pas un comportement humain — c'est un automate. L'outil **RITA** (Real Intelligence Threat Analytics, open source) automatise la détection de beaconing dans les logs Zeek. Les **fingerprints JA3/JA4** (hash de la négociation TLS Client Hello) identifient des clients TLS spécifiques même sur du trafic chiffré — le JA3 d'un RAT custom est différent de celui d'un navigateur Chrome.

#### 19.4 Reconstruction de l'exfiltration

L'estimation du volume exfiltré est une question à laquelle le network forensics doit répondre. L'analyse des logs proxy (user-agent `rclone/v1.65.0`, volume cumulé vers des endpoints S3), des NetFlow (volume de données sortantes par destination), et des PCAP (si disponibles — extraction des fichiers transférés) permet de quantifier l'exfiltration. Le DNS tunneling est une technique d'exfiltration plus discrète — les données sont encodées dans les sous-domaines des requêtes DNS (`encoded-data.c2-domain.com`). La détection repose sur la longueur anormale des requêtes, l'entropie élevée des sous-domaines, et le volume de requêtes vers un même domaine.

#### 19.5 Outils complémentaires

**Zeek** (ex-Bro) produit des logs structurés à partir du trafic réseau — conn.log (connexions), dns.log (requêtes DNS), http.log (requêtes HTTP), ssl.log (certificats TLS), files.log (fichiers transférés). Ces logs sont beaucoup plus faciles à analyser à grande échelle que les PCAP bruts. **NetworkMiner** (open source) extrait automatiquement les fichiers, les images, et les metadata des captures réseau. **Arkime** (ex-Moloch) est une plateforme de capture et d'analyse réseau à grande échelle, avec indexation full-text et interface web.

---

### Chapitre 20 — Active Directory forensics

#### 20.1 Pourquoi un chapitre dédié à l'AD

Dans 95 % des compromissions Windows, l'objectif stratégique de l'attaquant est le contrôle de l'Active Directory. L'AD gère l'authentification de tous les utilisateurs, les autorisations sur toutes les ressources, le déploiement de logiciel via GPO, et les secrets (hashes NTLM, clés Kerberos). Le forensic AD est donc une composante centrale de presque toute investigation Windows — et pourtant, il est rarement traité comme une discipline à part entière.

Ce chapitre couvre l'investigation AD sous l'angle forensic : quels artefacts analyser, quelles attaques détecter, et comment reconstituer la chronologie de la compromission AD. Il complète le Ch.14 (Event Logs) en se focalisant sur les artefacts spécifiques à l'AD, et le Ch.20 du cours IR (investigation identité) en allant plus en profondeur sur la technique.

#### 20.2 Investigation des authentifications

Les Event Logs des DC sont la source primaire. Les patterns à rechercher : authentifications depuis des IP inhabituelles (le compte `svc-backup` se connecte habituellement depuis le serveur de sauvegarde — une connexion depuis un poste de travail est suspecte), authentifications à des heures inhabituelles (un admin qui se connecte à 3h du matin un dimanche), volume anormal d'échecs d'authentification depuis une même source (password spraying), et authentifications avec des comptes de service utilisés manuellement (les comptes de service ne devraient jamais être utilisés interactivement).

L'**ADTimeline** (outil de l'ANSSI) produit une timeline des modifications AD à partir des métadonnées de réplication — c'est l'outil de référence pour comprendre chronologiquement ce que l'attaquant a fait dans l'AD. Il parse les métadonnées de réplication (attributs `whenChanged`, `whenCreated`, `msDS-ReplAttributeMetaData`) pour reconstruire la séquence des modifications sans dépendre des Event Logs (qui peuvent avoir été effacés).

#### 20.3 Investigation Kerberos

**Kerberoasting :** l'attaquant demande des TGS (Ticket Granting Service) pour des comptes de service ayant un SPN (Service Principal Name), puis cracke les tickets offline pour obtenir le mot de passe en clair. Détection forensic : Event ID 4769 avec encryption type 0x17 (RC4) en volume anormal depuis une seule machine. Interprétation : si un seul poste demande des TGS RC4 pour 10+ comptes de service en quelques minutes, c'est du Kerberoasting. L'attaquant a obtenu les tickets et les cracke offline — il n'y aura pas d'autre trace visible tant que le mot de passe n'est pas cracké et utilisé.

**DCSync :** l'attaquant simule un DC pour demander la réplication des hashes NTLM de tous les comptes. Détection forensic : Event ID 4662 avec les GUID de réplication (`1131f6ad-9c07-11d1-f79f-00c04fc2dcd2` pour DS-Replication-Get-Changes, `1131f6aa-...` pour DS-Replication-Get-Changes-All) provenant d'une machine qui n'est PAS un DC. C'est la preuve formelle que l'attaquant a récupéré tous les hashes — y compris le krbtgt.

**Golden Ticket :** l'attaquant forge un TGT avec le hash du krbtgt. Détection forensic : anomalies dans les tickets Kerberos — lifetime anormalement long (le Golden Ticket a souvent un lifetime de 10 ans alors que la politique du domaine est de 10 heures), SID qui ne correspond pas à un utilisateur existant, ou TGT sans événement de pré-authentification (4768) correspondant. La détection est difficile — c'est pourquoi la prévention (mots de passe krbtgt complexes, rotation régulière) est critique.

#### 20.4 Investigation des modifications AD

Les modifications d'objets AD (comptes créés, groupes modifiés, GPO ajoutées, ACL modifiées) sont enregistrées dans les Event Logs (Event ID 5136 pour les modifications d'attribut via LDAP, Event IDs 4720/4728/4732 pour la gestion des comptes et groupes) et dans les métadonnées de réplication (parsables par ADTimeline).

L'analyse du fichier **ntds.dit** (la base de données AD, stockée sur les DC dans `C:\Windows\NTDS\`) avec **secretsdump.py** (Impacket) ou **DSInternals** (PowerShell) permet d'extraire les hashes NTLM de tous les comptes, de vérifier les mots de passe (comparaison avec des dictionnaires pour identifier les mots de passe faibles que l'attaquant a pu craquer), et d'auditer les comptes (date de création, date de dernière connexion, membership des groupes).

**BloodHound** (en mode défensif) peut être utilisé pour visualiser les chemins d'attaque que l'attaquant a pu emprunter : quels comptes avaient des droits sur quels systèmes, quels chemins menaient au Domain Admin, quelles ACL permettaient l'élévation de privilèges. C'est un outil offensif (utilisé par les pentesters et les attaquants pour la reconnaissance) qui est aussi un outil défensif puissant pour comprendre comment la compromission a été possible.

#### 20.5 Fil rouge — MUSIC BOX : la compromission AD

> **🔬 MUSIC BOX — Épisode 17**
>
> L'investigation AD révèle la séquence complète :
>
> **ADTimeline :** 3 modifications critiques identifiées. (1) J-30 : création du compte `svc-monitor-temp` (ajouté au groupe Domain Admins). (2) J-14 : modification de l'attribut `msDS-AllowedToDelegateTo` sur le compte `svc-backup` — délégation Kerberos contrainte ajoutée, permettant l'impersonation d'administrateurs. (3) J-7 : création d'une GPO « Application Update Policy » dans une OU peu surveillée — contenu : script PowerShell de staging de données.
>
> **ntds.dit (secretsdump.py) :** extraction des hashes de tous les comptes. Comparaison avec la base Have I Been Pwned et un dictionnaire de mots de passe : 23 comptes ont des mots de passe faibles (< 12 caractères, mots du dictionnaire). Le compte `svc-backup` avait le mot de passe `NovaPharma2024!` — cracable en 2 heures avec un GPU moderne.

---

### Chapitre 21 — Investigation des identités hybrides, du cloud et des accès distants

*Ce chapitre traite l'investigation au-delà du périmètre AD classique : les environnements hybrides (AD sync avec Entra ID), les services cloud (M365, AWS), et les accès distants (VPN). Il est conçu comme un chapitre de synthèse orienté identité — la question transversale étant : comment l'attaquant a-t-il pivoté entre l'on-premise et le cloud ?*

#### 21.1 Investigation des accès VPN

Les logs VPN sont une source critique pour identifier l'accès initial et le mouvement latéral inter-sites. Les indicateurs de compromission dans les logs VPN : connexions depuis des IP géographiquement incohérentes avec l'utilisateur (geo-impossible travel — le même utilisateur se connecte depuis Paris et depuis Hong Kong à 1 heure d'intervalle), connexions en dehors des horaires habituels, et utilisation de comptes rarement actifs (le compte `admin_rh_ext` du sous-traitant GestPaie dans le cours IR, le compte `svc-backup` dans MUSIC BOX).

#### 21.2 Investigation Microsoft 365 et Entra ID

Le **Unified Audit Log** (UAL) est la source centrale pour l'investigation M365. Les événements les plus pertinents : `UserLoggedIn` (connexions — corréler avec le Sign-in Log pour la géolocalisation et le device info), `New-InboxRule` et `Set-InboxRule` (règles de forwarding — technique BEC classique), `FileDownloaded` et `FileAccessed` (accès aux fichiers SharePoint/OneDrive), `Add application` et `Consent to application` (app registrations OAuth — technique de persistance cloud), et `Update StsRefreshTokenValidFrom` (révocation de token — une révocation non initiée par l'IT est suspecte).

Les **Sign-in Logs** d'Entra ID fournissent des détails sur chaque authentification : IP, géolocalisation, device info, résultat de la conditional access policy, et méthode MFA utilisée. L'absence de MFA (quand la politique devrait l'exiger) ou un MFA bypass (utilisation d'un token volé) sont des indicateurs critiques.

Quand l'AD on-premise est synchronisé avec Entra ID via **Azure AD Connect**, la compromission se propage : l'attaquant qui a le hash NTLM d'un compte on-premise peut l'utiliser pour accéder aux ressources cloud synchronisées. L'investigation doit couvrir les deux environnements.

#### 21.3 Investigation AWS

Les sources forensic AWS incluent **CloudTrail** (chaque appel API est enregistré : `GetObject` sur S3, `RunInstances` pour les EC2, `CreateUser` pour IAM — avec l'IP source, l'identité appelante, et le timestamp), les **VPC Flow Logs** (métadonnées réseau — source, destination, port, volume, accept/reject), les **S3 Access Logs** (accès aux buckets — qui a accédé à quel objet, quand), et les **EBS Snapshots** (pour la préservation de l'état d'un volume sans arrêter l'instance).

L'investigation AWS se concentre sur les questions d'identité : quel utilisateur IAM ou quel rôle a été utilisé ? depuis quelle IP ? les access keys sont-elles les mêmes que celles présentes sur un serveur compromis ? (corrélation on-premise → cloud). La rétention par défaut de CloudTrail est de 90 jours — au-delà, il faut un trail configuré vers S3 ou CloudWatch.

#### 21.4 Fil rouge — MUSIC BOX : le pivot vers le cloud

> **🔬 MUSIC BOX — Épisode 18**
>
> L'investigation cloud confirme l'exfiltration. CloudTrail montre 347 appels `GetObject` sur le bucket `projets-molecule-np427` en 5 jours, depuis le rôle IAM `svc-backup-role` mais avec des access keys (`AKIA...`) qui correspondent à celles trouvées dans le fichier `~/.aws/credentials` du serveur Linux SRV-RD-01. L'attaquant a exfiltré les données R&D via le serveur Linux compromis, en utilisant les credentials AWS stockées sur le serveur.
>
> M365 : le UAL montre une connexion au compte `j.mallet@novapharma.com` depuis l'IP C2 `103.xx.xx.xx` à J-20 (token volé via le credential dump de mimikatz). L'attaquant a accédé à 15 emails contenant des informations sur la stratégie de brevet de NovaPharma pour la molécule NP-427. Aucune règle de forwarding n'a été créée — l'accès était ponctuel et ciblé.

---
