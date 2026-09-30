---
title: Chapitre 21 — Investigation des identités hybrides, du cloud et des accès distants
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - ../index.md
- - Partie V — Investigation réseau ET identité
  - index.md
---

*Ce chapitre traite l'investigation au-delà du périmètre AD classique : les environnements hybrides (AD sync avec Entra ID), les services cloud (M365, AWS), et les accès distants (VPN). Il est conçu comme un chapitre de synthèse orienté identité — la question transversale étant : comment l'attaquant a-t-il pivoté entre l'on-premise et le cloud ?*

## 21.1 Investigation des accès VPN

Les logs VPN sont une source critique pour identifier l'accès initial et le mouvement latéral inter-sites. Les indicateurs de compromission dans les logs VPN : connexions depuis des IP géographiquement incohérentes avec l'utilisateur (geo-impossible travel — le même utilisateur se connecte depuis Paris et depuis Hong Kong à 1 heure d'intervalle), connexions en dehors des horaires habituels, et utilisation de comptes rarement actifs (le compte `admin_rh_ext` du sous-traitant GestPaie dans le cours IR, le compte `svc-backup` dans MUSIC BOX).

## 21.2 Investigation Microsoft 365 et Entra ID

Le **Unified Audit Log** (UAL) est la source centrale pour l'investigation M365. Les événements les plus pertinents : `UserLoggedIn` (connexions — corréler avec le Sign-in Log pour la géolocalisation et le device info), `New-InboxRule` et `Set-InboxRule` (règles de forwarding — technique BEC classique), `FileDownloaded` et `FileAccessed` (accès aux fichiers SharePoint/OneDrive), `Add application` et `Consent to application` (app registrations OAuth — technique de persistance cloud), et `Update StsRefreshTokenValidFrom` (révocation de token — une révocation non initiée par l'IT est suspecte).

Les **Sign-in Logs** d'Entra ID fournissent des détails sur chaque authentification : IP, géolocalisation, device info, résultat de la conditional access policy, et méthode MFA utilisée. L'absence de MFA (quand la politique devrait l'exiger) ou un MFA bypass (utilisation d'un token volé) sont des indicateurs critiques.

Quand l'AD on-premise est synchronisé avec Entra ID via **Azure AD Connect**, la compromission se propage : l'attaquant qui a le hash NTLM d'un compte on-premise peut l'utiliser pour accéder aux ressources cloud synchronisées. L'investigation doit couvrir les deux environnements.

## 21.3 Investigation AWS

Les sources forensic AWS incluent **CloudTrail** (chaque appel API est enregistré : `GetObject` sur S3, `RunInstances` pour les EC2, `CreateUser` pour IAM — avec l'IP source, l'identité appelante, et le timestamp), les **VPC Flow Logs** (métadonnées réseau — source, destination, port, volume, accept/reject), les **S3 Access Logs** (accès aux buckets — qui a accédé à quel objet, quand), et les **EBS Snapshots** (pour la préservation de l'état d'un volume sans arrêter l'instance).

L'investigation AWS se concentre sur les questions d'identité : quel utilisateur IAM ou quel rôle a été utilisé ? depuis quelle IP ? les access keys sont-elles les mêmes que celles présentes sur un serveur compromis ? (corrélation on-premise → cloud). La rétention par défaut de CloudTrail est de 90 jours — au-delà, il faut un trail configuré vers S3 ou CloudWatch.

## 21.4 Fil rouge — MUSIC BOX : le pivot vers le cloud

> **🔬 MUSIC BOX — Épisode 18**
>
> L'investigation cloud confirme l'exfiltration. CloudTrail montre 347 appels `GetObject` sur le bucket `projets-molecule-np427` en 5 jours, depuis le rôle IAM `svc-backup-role` mais avec des access keys (`AKIA...`) qui correspondent à celles trouvées dans le fichier `~/.aws/credentials` du serveur Linux SRV-RD-01. L'attaquant a exfiltré les données R&D via le serveur Linux compromis, en utilisant les credentials AWS stockées sur le serveur.
>
> M365 : le UAL montre une connexion au compte `j.mallet@novapharma.com` depuis l'IP C2 `103.xx.xx.xx` à J-20 (token volé via le credential dump de mimikatz). L'attaquant a accédé à 15 emails contenant des informations sur la stratégie de brevet de NovaPharma pour la molécule NP-427. Aucune règle de forwarding n'a été créée — l'accès était ponctuel et ciblé.

---
