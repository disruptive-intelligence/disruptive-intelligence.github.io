---
title: Partie VII — Incident response, hybrid identity et synthèse
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - index.md
---

*Répondre à une compromission d'AD, décider entre nettoyage et reconstruction, puis étendre la réflexion à l'identité hybride.*

---


## Chapitre 27 — Incident Response AD : méthodologie

### 27.1 Le scénario type

« L'EDR signale un outil de vol d'identifiants sur un serveur ; un compte d'administration du domaine semble utilisé hors des heures habituelles ; des modifications de permissions inattendues apparaissent sur des objets sensibles. » Dès qu'AD est en jeu, l'incident change d'échelle : il ne s'agit plus d'une machine, mais de la **confiance** dans tout le système d'information.

### 27.2 Les questions du triage

| Question | Où chercher |
|---|---|
| **Quels comptes** sont compromis ? | 4624, 4648, 4672 ; connexions inhabituelles de comptes privilégiés |
| **Quels systèmes** sont touchés ? | Postes, serveurs, DC ; traces de mouvement latéral (sessions réseau, créations de services, tâches planifiées) |
| Le **Tier 0** est-il atteint ? | DC, comptes Domain/Enterprise Admins, `krbtgt`, AD CS, Entra Connect, sauvegardes |
| **Depuis quand** ? | Première activité suspecte : elle fixe la date de dernière sauvegarde « saine » |
| Y a-t-il de la **persistance** ? | Comptes créés, ajouts aux groupes, ACL modifiées (AdminSDHolder, racine du domaine), GPO modifiées, certificats émis, clés ajoutées sur des comptes, tâches et services |

> **Règle d'or.** Si le Tier 0 est touché, on suppose le pire — tous les secrets du domaine exposés — et on cherche à le réfuter, pas l'inverse.

### 27.3 Les principes de conduite

- **Communiquer hors bande** : si le domaine est compromis, la messagerie et les comptes de l'entreprise le sont peut-être aussi ;
- **Préserver les preuves** avant d'agir : mémoire des machines clés, journaux des DC, exports de l'annuaire ;
- **Ne pas alerter l'attaquant trop tôt** : une remédiation partielle et visible le pousse à se réimplanter ailleurs ; on prépare une éviction coordonnée ;
- **Se faire accompagner** (prestataire qualifié de réponse à incident, CERT) quand le Tier 0 est atteint.

---


## Chapitre 28 — Confinement, nettoyage et rotation de krbtgt

### 28.1 Confinement

| Action | Précision |
|---|---|
| Isoler les systèmes compromis | Couper le réseau, **ne pas éteindre** (la mémoire contient des preuves) |
| Désactiver les comptes compromis | Désactiver plutôt que supprimer : on garde l'objet pour l'enquête |
| Réinitialiser les mots de passe | Comptes compromis, comptes privilégiés, comptes de service exposés — **deux fois** pour les comptes sensibles |
| Révoquer les sessions | Purge des tickets, rotation de `krbtgt` si des tickets forgés sont suspectés |
| Bloquer les indicateurs | IP, domaines, hashes de fichiers sur les équipements de sécurité |
| Protéger les sauvegardes | Les isoler immédiatement de l'environnement compromis |

### 28.2 La rotation de krbtgt

Le compte `krbtgt` garde en mémoire son **mot de passe actuel et le précédent** (pour ne pas invalider brutalement les tickets en cours). D'où la **double rotation** :

```text
Rotation 1 → attendre la réplication complète et au moins la durée de vie maximale d'un ticket (10 h par défaut)
Rotation 2 → l'ancien secret disparaît définitivement : les tickets fabriqués avec lui deviennent invalides
```


Faire les deux rotations d'affilée casse les sessions Kerberos légitimes de tout le domaine. Microsoft fournit un script de réinitialisation qui vérifie la réplication entre les étapes. Les RODC ont chacun leur propre `krbtgt_XXXXX`, à traiter aussi.

### 28.3 Nettoyer la persistance

| Où | Quoi vérifier |
|---|---|
| Comptes | Comptes créés pendant la période (4720), comptes réactivés |
| Groupes privilégiés | Ajouts (4728/4732/4756), imbrications nouvelles |
| ACL | Comparaison avec une référence : racine du domaine, AdminSDHolder, OU Tier 0, GPO |
| GPO | Modifications (5136, numéros de version), scripts ajoutés dans SYSVOL |
| Attributs sensibles | SPN ajoutés, délégations ajoutées, clés ajoutées sur `msDS-KeyCredentialLink`, `SIDHistory` |
| AD CS | Certificats émis pendant la période (à révoquer), modèles modifiés |
| Configuration | Objets de DC inattendus dans la partition de configuration |
| Machines | Services, tâches planifiées, clés Run sur chaque DC et serveur touché |

---


## Chapitre 29 — Rebuild vs Clean et retour à la normale

### 29.1 Nettoyer ou reconstruire

| Critère | Plutôt nettoyer | Plutôt reconstruire |
|---|---|---|
| Périmètre | Limité, Tier 0 épargné | Tier 0 compromis |
| Durée de présence | Courte, bien datée | Longue ou inconnue |
| Visibilité | Journaux complets sur la période | Trous dans la journalisation |
| Sauvegardes | Saines et antérieures à l'intrusion | Absentes ou douteuses |
| Persistance | Toute identifiée | Doute raisonnable sur des mécanismes non trouvés |

La reconstruction (nouvelle forêt, migration des comptes et des ressources) est longue et coûteuse, mais c'est parfois la seule façon de **retrouver une confiance démontrable**.

### 29.2 Valider avant de rouvrir

- nouveau rapport PingCastle et nouvelle analyse BloodHound : les chemins sont-ils fermés ?
- rotation de `krbtgt` confirmée (double) et mots de passe des comptes privilégiés et de service renouvelés ;
- ACL des objets Tier 0 conformes à la référence ;
- modèles AD CS audités, certificats suspects révoqués ;
- surveillance renforcée pendant plusieurs semaines (l'attaquant tente souvent de revenir).

### 29.3 Le retour d'expérience

Chronologie complète, vecteur initial, chemin d'escalade, mécanismes de persistance, ce qui a fonctionné et ce qui a manqué (détection, sauvegardes, procédures), puis un plan d'amélioration priorisé et suivi.

---


## Chapitre 30 — Entra ID et hybride : architecture et synchronisation

### 30.1 Entra ID en bref

| | AD DS | Entra ID |
|---|---|---|
| Structure | Forêts, domaines, OU | Tenant plat, unités administratives |
| Protocoles | Kerberos, NTLM, LDAP | OAuth 2.0, OpenID Connect, SAML |
| Configuration des postes | GPO | Intune |
| Contrôle d'accès | ACL, groupes | Rôles, Conditional Access |
| Équivalent du TGT | TGT Kerberos | **PRT** (*Primary Refresh Token*) sur les appareils joints |

### 30.2 Les trois modes de synchronisation

La synchronisation passe par **Entra Connect** (ex-Azure AD Connect) ou **Cloud Sync**. Trois façons d'authentifier les utilisateurs dans le cloud :

| Mode | Principe | Point d'attention |
|---|---|---|
| **PHS** (*Password Hash Sync*) | Un dérivé du hash des mots de passe est synchronisé vers Entra ID | Le plus simple et le plus résilient ; le serveur de synchronisation devient Tier 0 |
| **PTA** (*Pass-Through Authentication*) | Les authentifications cloud sont validées en temps réel par des agents on-premises | Les agents PTA sont Tier 0 |
| **Fédération** (ADFS) | Un serveur ADFS émet les jetons pour le cloud | ADFS et son certificat de signature de jetons sont Tier 0 |

### 30.3 Le serveur de synchronisation est Tier 0

Le compte utilisé par Entra Connect dispose de droits de réplication sur l'annuaire (en PHS) et le serveur détient de quoi agir sur les deux mondes. Il doit être traité comme un DC : isolé, sans accès Internet superflu, administré depuis une PAW, surveillé par l'EDR.

Erreurs fréquentes : serveur hors Tier 0, comptes Domain Admins synchronisés vers le cloud, aucun filtrage (tous les comptes de service synchronisés), comptes d'administration cloud adossés à des comptes on-premises.

> **Bonne pratique.** Les administrateurs du cloud utilisent des comptes **cloud-only**, distincts des comptes AD : une compromission on-premises ne doit pas donner le contrôle du tenant, et inversement.

---


## Chapitre 31 — Menaces et défense de l'identité cloud

### 31.1 Les familles de menaces

| Menace | Principe |
|---|---|
| **Vol de jetons** | Un jeton d'accès ou de rafraîchissement volé donne accès aux applications sans repasser par le MFA |
| **Vol du PRT** | Le « TGT du cloud » : il ouvre le SSO vers toutes les applications Entra ID |
| **Consentement abusif** (*consent phishing*) | L'utilisateur autorise une application malveillante à lire sa messagerie ou ses fichiers |
| **Jetons SAML forgés** | Avec le certificat de signature ADFS, on fabrique des jetons pour toutes les applications fédérées (technique observée lors de l'affaire SolarWinds) |
| **Persistance dans le tenant** | Secrets ajoutés à des applications ou principaux de service, rôles attribués durablement |

### 31.2 Les défenses

| Mesure | Rôle |
|---|---|
| **Conditional Access** | MFA résistant au phishing pour les administrateurs, appareil conforme exigé, blocage des protocoles anciens (authentification de base), restrictions géographiques |
| **PIM** (*Privileged Identity Management*) | Rôles d'administration activés à la demande, pour une durée limitée, avec justification et approbation |
| **Contrôle des consentements** | Consentement utilisateur restreint aux éditeurs vérifiés, workflow d'approbation administrateur |
| **Protection des jetons** | *Token protection*, évaluation continue de l'accès (CAE), durée de session adaptée |
| **Comptes d'urgence** (*break-glass*) | Deux comptes cloud-only exclus des politiques bloquantes, surveillés de près |

### 31.3 Journaux et détection

Journaux de connexion (*Sign-in logs*), journaux d'audit, détections de risque (*Entra ID Protection*), journaux de provisionnement, exportés vers le SIEM (Microsoft Sentinel ou autre). À surveiller en priorité : ajouts de rôles privilégiés, nouveaux secrets sur les applications, consentements accordés, connexions risquées de comptes administrateurs.

---


## Chapitre 32 — Cas de synthèse : rapport de pentest AD complet

Synthèse du fil rouge KERBEROS. Le rapport de pentest de Thomas sur Meridian Pharma.

**Résumé exécutif** (pour la direction — score PingCastle : 73/100, Domain Admin atteint en 4 heures par 2 chemins indépendants, recommandations critiques : 5 actions P0 pour réduire le risque de 80 %).

**Findings classés par criticité :**

**Critique :** ESC1 sur template VPN-User (Domain Admin en 90 secondes via AD CS), krbtgt jamais roté depuis 7 ans, 3 comptes DA avec sessions actives sur des serveurs Tier 1 (violation de tiering), Azure AD Connect non isolé avec accès internet, RODC Genève avec PRP trop large (45 comptes dont 3 comptes de service Tier 1).

**Élevé :** 12 comptes de service avec SPN et mot de passe > 3 ans (Kerberoasting surface), LLMNR/NBT-NS actifs (4 hashes capturés en 15 min), pas de Credential Guard (Mimikatz fonctionnel), pas de SMB signing (relay possible), svc_monitoring avec GenericWrite sur le groupe IT-Admins → chemin vers DA via ACL abuse.

**Moyen :** 47 comptes inactifs > 180 jours, 3 GPO modifiables par des utilisateurs non privilégiés, NTLM non restreint, pas de honey objects, logs AD CS non centralisés (la kill chain AD CS est passée inaperçue), msDS-KeyCredentialLink non monitoré.

**Kill chains documentées :** Chemin 1 (Responder → hash capture → Kerberoasting svc_backup → mouvement latéral SRV-APP01 → credential dumping → PtH vers DC → DCSync). Chemin 2 (Certipy ESC1 → certificat DA → PKINIT → TGT DA → DCSync). Chemin 3 (RODC Genève → PRP trop large → hash svc_monitoring → GenericWrite → ACL abuse → DA).

**Recommandations priorisées :** P0 immédiat (corriger ESC1, rotater krbtgt double rotation, séparer les comptes DA des serveurs Tier 1, isoler Azure AD Connect, réduire la PRP du RODC), P1 3 mois (déployer LAPS, gMSA pour les comptes de service, désactiver LLMNR/NBT-NS, SMB signing, centraliser les logs AD CS, monitorer msDS-KeyCredentialLink), P2 6 mois (Credential Guard sur les serveurs Tier 0/1, tiering complet, déployer honey objects, restreindre NTLM, audit ACL complet et remédiation BloodHound). Risques résiduels acceptés : 2 applications legacy nécessitant NTLM (compensatoire : monitoring renforcé + segmentation).

---
