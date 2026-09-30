---
title: Partie 4 — Taxonomie des surfaces d'attaque
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie cyber
up:
- - Taxonomie cyber
  - index.md
---

> Une **surface d'attaque** est l'ensemble des points exploitables d'un actif. Cette partie cartographie les grandes surfaces du SI moderne. Pour chacune : *ce qu'elle contient*, *pourquoi elle est exposée*, *les attaques typiques*, *les erreurs fréquentes*, *les défenses*. C'est la carte géographique du champ de bataille.


## Chapitre 40 — Poste utilisateur

**Ce qu'elle contient.** Postes de travail (Windows, macOS, Linux), leur système, leurs applications (navigateur, bureautique, lecteurs PDF), les sessions et identifiants de l'utilisateur, ses fichiers locaux.

**Pourquoi exposée.** C'est le point de contact direct entre l'humain et le SI : l'utilisateur ouvre des mails, navigue, branche des clés USB, installe des logiciels. C'est le *point d'entrée n°1* des attaques (phishing, pièce jointe piégée, drive-by).

**Attaques typiques.** Phishing et pièces jointes malveillantes, macro malware, drive-by download, infostealer, vol de jetons de session, exécution de LOLBins, escalade de privilèges locale.

⚠️ **Erreur fréquente** — Donner les droits administrateur local aux utilisateurs : une compromission devient immédiatement totale sur le poste, et facilite le vol d'identifiants.

🛡️ **Défense** — EDR, moindre privilège (pas d'admin local), durcissement, désactivation des macros, filtrage mail/web, application allowlisting, chiffrement disque, mises à jour.

🧭 **Taxonomie** — Souvent le **Tier 2** (chapitre 19) et la première étape d'un chemin d'attaque vers l'identité puis les serveurs.

🎯 **À retenir** — Le poste utilisateur est la porte d'entrée privilégiée : on le suppose tôt ou tard compromis (assume breach) et on limite ce qu'il permet d'atteindre.


## Chapitre 41 — Serveur

**Ce qu'elle contient.** Serveurs applicatifs, bases de données, serveurs de fichiers, contrôleurs de domaine, hyperviseurs — hébergeant services et données de valeur.

**Pourquoi exposée.** Concentration de valeur (données, services critiques) et souvent grande longévité (systèmes legacy, patchs retardés pour ne pas interrompre la production).

**Attaques typiques.** Exploitation de service exposé/non patché, exécution de code à distance (RCE), abus de comptes de service, mouvement latéral, déploiement de ransomware, exfiltration.

⚠️ **Erreur fréquente** — Exposer directement des services d'administration (RDP, SSH, bases) sur Internet ; retarder indéfiniment les patchs critiques.

🛡️ **Défense** — Durcissement, segmentation, gestion stricte des vulnérabilités, accès d'administration via bastion, journalisation, EDR serveur, sauvegardes immuables.

🧭 **Taxonomie** — Typiquement **Tier 1** (applications/données) ou **Tier 0** (contrôleurs de domaine, IAM, PKI — joyaux).

🎯 **À retenir** — Le serveur concentre la valeur : sa compromission a un impact direct sur les actifs essentiels.


## Chapitre 42 — Réseau

**Ce qu'elle contient.** Commutateurs, routeurs, pare-feu, VLAN, protocoles (ARP, DNS, DHCP, BGP), liaisons filaires et sans fil, flux de données en transit.

**Pourquoi exposée.** Le réseau relie *tout* : il transporte identifiants, données et commandes. Un réseau « plat » (non segmenté) permet à un attaquant d'atteindre tout depuis n'importe où.

**Attaques typiques.** Sniffing, spoofing (ARP/DNS/DHCP), MITM, scan/énumération, mouvement latéral, pivoting, DoS/DDoS, attaques sur les protocoles de routage (BGP).

🛡️ **Défense** — Segmentation et microsegmentation, chiffrement en transit (TLS), inspection (NDR/IDS), durcissement des équipements, contrôle d'accès réseau (NAC), supervision des flux.

🧭 **Taxonomie** — Surface centrale traitée en détail en Partie 7. Le réseau est aussi le *terrain* du chemin d'attaque.

🎯 **À retenir** — Un réseau non segmenté transforme toute intrusion locale en compromission globale.


## Chapitre 43 — Active Directory et IAM

**Ce qu'elle contient.** L'annuaire central (Active Directory, Entra ID, LDAP), la gestion des identités et des accès (IAM) : comptes, groupes, droits, authentification (Kerberos, NTLM), politiques (GPO).

**Pourquoi exposée.** C'est le *cerveau des accès* : qui contrôle l'AD/IAM contrôle tout le SI. Surface complexe, riche en relations de confiance et en chemins d'élévation souvent invisibles.

**Attaques typiques.** Kerberoasting, AS-REP roasting, pass-the-hash/ticket, DCSync, abus de délégation, abus d'ACL/GPO, AD CS abuse, password spraying, credential dumping.

🛡️ **Défense** — Tiering (Tier 0), PAM/bastion, durcissement AD, surveillance des objets et ACL, LAPS, désactivation des protocoles faibles, détection comportementale.

🧭 **Taxonomie** — **Tier 0** par excellence ; objet de toute la Partie 8. « L'identité est le nouveau périmètre. »

🎯 **À retenir** — Compromettre l'AD/IAM, c'est souvent compromettre l'entreprise entière. C'est la cible finale de la majorité des intrusions.


## Chapitre 44 — Application web

**Ce qu'elle contient.** Sites et applications accessibles par navigateur : code serveur, code client (JS), sessions, formulaires, logique métier, bases de données associées.

**Pourquoi exposée.** Souvent accessible depuis Internet, par nature ouverte au public, traitant des entrées non fiables. Surface immense et en évolution permanente.

**Attaques typiques.** Toute la Partie 6 : injection (XSS, SQLi), contrôle d'accès cassé (IDOR/BOLA), SSRF, désérialisation, CSRF, abus de logique métier, etc.

🛡️ **Défense** — Secure by design, validation/encodage des entrées-sorties, contrôle d'accès systématique côté serveur, WAF, tests (SAST/DAST/IAST), gestion des dépendances, en-têtes de sécurité (CSP).

🧭 **Taxonomie** — Surface la plus riche en sous-types d'attaques (OWASP Top 10). Détaillée en Partie 6.

🎯 **À retenir** — L'application web traite par définition des entrées hostiles : *ne jamais faire confiance à l'entrée utilisateur* est la règle d'or.


## Chapitre 45 — API

**Ce qu'elle contient.** Interfaces programmatiques (REST, GraphQL, gRPC, SOAP) exposant fonctions et données aux applications, partenaires et clients mobiles.

**Pourquoi exposée.** Les API exposent directement la logique et les données, souvent sans interface humaine pour « masquer » les failles. Multiplication rapide (microservices), documentation parfois publique, contrôle d'accès souvent insuffisant.

**Attaques typiques.** OWASP API Top 10 : BOLA (autorisation au niveau objet cassée), BFLA (au niveau fonction), exposition excessive de données, consommation de ressources non limitée, mauvaise gestion d'inventaire (shadow/zombie APIs).

⚠️ **Erreur fréquente** — Supposer qu'une API « non documentée publiquement » est invisible (sécurité par obscurité). Les endpoints sont découvrables.

🛡️ **Défense** — Authentification/autorisation robustes par objet *et* par fonction, validation de schéma, limitation de débit (rate limiting), inventaire d'API, passerelle API, journalisation.

🧭 **Taxonomie** — Surface en forte croissance ; traitée en Partie 10. L'autorisation par objet (BOLA) est l'équivalent API de l'IDOR web.

🎯 **À retenir** — Les API sont les nouvelles portes du SI ; leur faille la plus fréquente est l'**autorisation** (BOLA/BFLA), pas l'authentification.


## Chapitre 46 — Cloud

**Ce qu'elle contient.** Ressources IaaS/PaaS/SaaS : machines virtuelles, stockage objet (buckets), bases managées, IAM cloud, réseaux virtuels, fonctions serverless, services de secrets.

**Pourquoi exposée.** Surface gérée par configuration (et non plus par périmètre physique) : une simple erreur de configuration expose des données au monde entier. Modèle de **responsabilité partagée** souvent mal compris.

**Attaques typiques.** Buckets publics, secrets/clés exposés, abus du service de métadonnées, élévation de privilèges via IAM mal configuré, mouvement latéral cloud, prise de contrôle de comptes.

⚠️ **Erreur fréquente** — Croire que « le cloud est sécurisé par le fournisseur ». Le fournisseur sécurise *l'infrastructure* ; *vos* configurations et données restent *votre* responsabilité.

🛡️ **Défense** — Moindre privilège IAM, chiffrement, CSPM (détection de mauvaises configurations), gestion des secrets, journalisation cloud, durcissement par défaut, revue des accès.

🧭 **Taxonomie** — Surface détaillée en Partie 10. La mauvaise *configuration* y remplace souvent la *vulnérabilité* logicielle classique.

🎯 **À retenir** — Dans le cloud, l'erreur n°1 est la **mauvaise configuration**, pas la faille logicielle. La responsabilité partagée doit être comprise.


## Chapitre 47 — Conteneurs et Kubernetes

**Ce qu'elle contient.** Images de conteneurs, registres, moteurs d'exécution (Docker/containerd), orchestrateurs (Kubernetes : pods, RBAC, secrets, API server, etcd).

**Pourquoi exposée.** Densité (beaucoup de charges sur un même hôte), images héritées de dépendances vulnérables, complexité de configuration de Kubernetes (RBAC, réseau), API server parfois exposée.

**Attaques typiques.** Image vulnérable/malveillante, registre exposé, abus de RBAC Kubernetes, évasion de conteneur (container escape) vers l'hôte, secrets mal protégés, mouvement latéral entre pods.

🛡️ **Défense** — Images minimales et scannées, registres privés, RBAC au moindre privilège, isolation (politiques réseau, security contexts), gestion des secrets, durcissement de l'orchestrateur, admission control.

🧭 **Taxonomie** — Sous-surface du cloud moderne (Partie 10). L'évasion de conteneur est l'équivalent « escalade vers l'hôte ».

🎯 **À retenir** — Un conteneur n'est pas une frontière de sécurité parfaite : une mauvaise config peut permettre l'évasion vers l'hôte.


## Chapitre 48 — CI/CD

**Ce qu'elle contient.** La chaîne d'intégration et de déploiement continus : dépôts de code, pipelines de build, runners, artefacts, secrets de déploiement, accès aux environnements de production.

**Pourquoi exposée.** La CI/CD a, par conception, des *droits puissants* (déployer en production) et manipule du code et des secrets. La compromettre permet d'injecter du code malveillant *dans tout ce qui est déployé*.

**Attaques typiques.** Pipeline poisoning (injection dans le build), vol de secrets de pipeline, dependency confusion, compromission du système de build, altération d'artefacts, abus de tokens CI.

⚠️ **Erreur fréquente** — Stocker des secrets en clair dans les fichiers de pipeline ou les variables non protégées ; donner aux pipelines des droits de production illimités.

🛡️ **Défense** — Moindre privilège des pipelines, gestion des secrets dédiée, signature des artefacts, isolation des runners, revue de code obligatoire, provenance (SLSA), SBOM.

🧭 **Taxonomie** — Maillon critique de la **supply chain logicielle** (Partie 10). Cible à fort effet de levier.

🎯 **À retenir** — Compromettre la CI/CD, c'est empoisonner la source : le code malveillant est ensuite distribué « légitimement » partout.


## Chapitre 49 — Messagerie

**Ce qu'elle contient.** Serveurs et services de mail, boîtes des utilisateurs, passerelles, protocoles (SMTP, IMAP), mécanismes d'authentification d'expéditeur (SPF/DKIM/DMARC).

**Pourquoi exposée.** Canal d'entrée privilégié des attaques (phishing, malware, BEC), ouvert au monde par nature, reposant sur la confiance de l'utilisateur.

**Attaques typiques.** Phishing/spear phishing, BEC (fraude au président), malspam, usurpation d'expéditeur (spoofing), consent phishing, pièces jointes et liens piégés.

🛡️ **Défense** — Filtrage anti-spam/anti-malware, SPF/DKIM/DMARC, bac à sable des pièces jointes, réécriture/analyse des liens, sensibilisation, MFA pour contrer le vol de comptes.

🧭 **Taxonomie** — Vecteur d'entrée majeur ; relié à toute la Partie 9 (phishing, social engineering).

🎯 **À retenir** — La messagerie est le vecteur d'attaque le plus utilisé ; SPF/DKIM/DMARC + filtrage + sensibilisation forment la base.


## Chapitre 50 — Navigateur

**Ce qu'elle contient.** Le navigateur web et son écosystème : moteur de rendu, JavaScript, extensions, cookies/sessions, stockage local.

**Pourquoi exposée.** C'est l'application la plus exposée à du contenu hostile (chaque site visité est du code non fiable). Très ciblé par les exploits et le vol de session.

**Attaques typiques.** Drive-by download, exploitation de vulnérabilités du moteur, extensions malveillantes, vol de cookies/jetons de session, XSS côté client, malvertising.

🛡️ **Défense** — Mises à jour automatiques, contrôle des extensions, isolation/sandboxing, filtrage web/DNS, politiques (CSP côté sites), navigateur durci, isolation de la navigation à risque.

🧭 **Taxonomie** — Surface client-side ; pont entre le poste utilisateur (chapitre 40) et les attaques web (Partie 6).

🎯 **À retenir** — Le navigateur exécute en permanence du code étranger ; sa mise à jour et son isolation sont critiques.


## Chapitre 51 — Mobile

**Ce qu'elle contient.** Smartphones/tablettes (iOS, Android), applications mobiles, données locales, accès aux ressources d'entreprise (mail, MFA, VPN), capteurs.

**Pourquoi exposée.** Appareils nomades, souvent personnels (BYOD), hors du périmètre, cibles de smishing, d'applications malveillantes et de vol physique. Souvent dépositaires du second facteur MFA.

**Attaques typiques.** Smishing, applications malveillantes, MFA fatigue/SIM swapping, vol/perte d'appareil, exploitation d'OS non mis à jour, interception sur Wi-Fi public.

🛡️ **Défense** — MDM/MAM (gestion de flotte), chiffrement, conteneurisation pro/perso, magasins d'applications contrôlés, mises à jour, MFA résistant au phishing, effacement à distance.

🧭 **Taxonomie** — Extension nomade du poste utilisateur ; relié à l'identité (porteur du MFA) et au social engineering (smishing).

🎯 **À retenir** — Le mobile est souvent le coffre du second facteur : sa compromission peut faire tomber le MFA.


## Chapitre 52 — IoT

**Ce qu'elle contient.** Objets connectés (caméras, capteurs, imprimantes, domotique, dispositifs médicaux), souvent à faible puissance et faible sécurité.

**Pourquoi exposée.** Sécurité native faible (mots de passe par défaut, firmware rarement mis à jour, protocoles non chiffrés), nombre massif, durée de vie longue, souvent non inventoriés (shadow IoT).

**Attaques typiques.** Identifiants par défaut, enrôlement dans des botnets (DDoS), pivot vers le réseau interne, espionnage (caméras/micros), exploitation de firmware non patché.

🛡️ **Défense** — Segmentation dédiée (VLAN IoT isolé), changement des mots de passe par défaut, inventaire, mises à jour firmware, désactivation des services inutiles, supervision.

🧭 **Taxonomie** — Surface en explosion ; souvent un *point de pivot* faible vers des surfaces plus sensibles. Recoupe l'OT (chapitre 53).

🎯 **À retenir** — L'IoT élargit massivement la surface d'attaque avec des objets peu sécurisables : la segmentation est la parade clé.


## Chapitre 53 — OT / ICS

**Ce qu'elle contient.** Technologies opérationnelles : systèmes industriels (ICS), automates (PLC), SCADA, capteurs/actionneurs pilotant des processus physiques (usines, énergie, eau, transport).

**Pourquoi exposée.** Priorité historique à la *disponibilité et la sûreté physique* plutôt qu'à la cybersécurité ; systèmes très anciens, protocoles non chiffrés/non authentifiés, convergence IT/OT qui les expose désormais.

**Attaques typiques.** Sabotage de processus physique, ransomware débordant de l'IT vers l'OT, manipulation d'automates, déni de service industriel. Impact potentiel : *physique* (sécurité des personnes, environnement).

⚠️ **Erreur fréquente** — Appliquer tels quels les outils IT (patchs intempestifs, scans agressifs) sur de l'OT fragile, au risque d'interrompre un processus critique.

🛡️ **Défense** — Séparation stricte IT/OT (modèle de zones type Purdue), diodes/relais unidirectionnels, surveillance passive, durcissement prudent, plans de continuité spécifiques.

🧭 **Taxonomie** — Surface à part : ici l'impact peut être *physique et vital*, ce qui change la hiérarchie CIA (la disponibilité/sûreté prime).

🎯 **À retenir** — En OT, une cyberattaque peut avoir des conséquences physiques. L'isolation IT/OT est la priorité absolue.


## Chapitre 54 — Wi-Fi

**Ce qu'elle contient.** Réseaux sans fil, points d'accès, protocoles de chiffrement (WPA2/WPA3), portails captifs, clients connectés.

**Pourquoi exposée.** Le signal déborde des murs physiques : un attaquant à proximité peut écouter, usurper ou brouiller sans accès filaire.

**Attaques typiques.** Evil twin (faux point d'accès), rogue AP, deauthentication, capture de poignées de main, exploitation de protocoles faibles, interception sur Wi-Fi public.

🛡️ **Défense** — WPA3/WPA2-Enterprise (802.1X), réseaux invités isolés, détection de points d'accès indésirables, VPN sur réseaux non fiables, désactivation des protocoles faibles.

🧭 **Taxonomie** — Sous-surface réseau (Partie 7) ; point d'entrée physique de proximité.

🎯 **À retenir** — Le Wi-Fi étend le réseau au-delà des murs : il faut un chiffrement fort et la détection des faux points d'accès.


## Chapitre 55 — VPN

**Ce qu'elle contient.** Passerelles d'accès distant chiffré au réseau interne, clients VPN, concentrateurs.

**Pourquoi exposée.** Exposé sur Internet *par conception* (point d'entrée distant) et donnant accès au cœur du réseau. Cible récurrente d'exploits critiques et de vol d'identifiants.

**Attaques typiques.** Exploitation de vulnérabilités de la passerelle (RCE), credential stuffing/brute force, contournement de MFA, accès trop large une fois connecté.

⚠️ **Erreur fréquente** — VPN sans MFA, ou donnant un accès *plat* à tout le réseau interne une fois connecté (contraire au Zero Trust).

🛡️ **Défense** — Patch prioritaire des passerelles, MFA résistant au phishing, moindre privilège d'accès, journalisation, et migration progressive vers le **ZTNA** (accès par application plutôt que par réseau).

🧭 **Taxonomie** — Point d'entrée distant majeur ; le ZTNA (chapitre 280) en est le successeur Zero Trust.

🎯 **À retenir** — Le VPN est une porte exposée vers le cœur du réseau : patch + MFA + moindre privilège sont impératifs.


## Chapitre 56 — SaaS

**Ce qu'elle contient.** Applications en ligne tierces (messagerie cloud, CRM, stockage, collaboration), où *vos données* résident chez le fournisseur, gérées par configuration et identités.

**Pourquoi exposée.** Accessible de partout, dépendante de la configuration (partages, permissions) et de la sécurité des identités. Multiplication non maîtrisée (shadow SaaS) et intégrations OAuth à risque.

**Attaques typiques.** Prise de contrôle de comptes (sans MFA), partages publics involontaires, consent phishing (octroi d'autorisations OAuth à une app malveillante), mauvaises configurations, intégrations tierces compromises.

🛡️ **Défense** — SSO + MFA, revue des permissions et partages, contrôle des intégrations OAuth, CASB/SSPM, journalisation des accès, gouvernance des applications autorisées.

🧭 **Taxonomie** — Surface « données hors les murs » ; recoupe l'identité (chapitre 57) et le cloud (Partie 10).

🎯 **À retenir** — En SaaS, la sécurité repose surtout sur l'**identité** et la **configuration** : SSO/MFA et revue des partages sont essentiels.


## Chapitre 57 — Identité

**Ce qu'elle contient.** L'ensemble des comptes, identifiants, jetons, droits et mécanismes d'authentification — humains et machines — à travers tout le SI (on-prem et cloud).

**Pourquoi exposée.** « L'identité est le nouveau périmètre » : dans un monde cloud/SaaS/télétravail, l'identité est ce qui donne accès, indépendamment du réseau. Voler une identité = obtenir ses accès partout.

**Attaques typiques.** Phishing d'identifiants, credential stuffing, password spraying, vol de jetons de session, MFA fatigue, abus d'OAuth, attaques AD (Partie 8).

🛡️ **Défense** — MFA résistant au phishing, SSO, moindre privilège et revue d'accès, gestion des identités (gouvernance IGA), détection des connexions anormales, PAM pour les privilèges.

🧭 **Taxonomie** — Surface transverse et centrale, pont entre AD (chapitre 43), cloud, SaaS et Zero Trust.

🎯 **À retenir** — Protéger l'identité est devenu *la* priorité : c'est elle, plus que le réseau, qui garde les accès.


## Chapitre 58 — Données

**Ce qu'elle contient.** L'information elle-même, dans ses trois états : *au repos* (stockée), *en transit* (sur le réseau), *en cours d'utilisation* (en mémoire/traitement).

**Pourquoi exposée.** Les données sont l'objectif final de la plupart des attaques (vol, chiffrement, falsification). Elles se dispersent (copies, exports, cloud, SaaS, postes), rendant leur protection diffuse.

**Attaques typiques.** Exfiltration, chiffrement (ransomware), falsification (intégrité), fuite par mauvaise configuration, vol de sauvegardes, interception en transit.

🛡️ **Défense** — Classification (chapitre 34), chiffrement au repos et en transit, DLP, contrôle d'accès et besoin d'en connaître, minimisation et rétention maîtrisée, sauvegardes protégées.

🧭 **Taxonomie** — *L'actif* ultime du fil rouge ; toutes les autres surfaces ne sont que des chemins vers la donnée.

🎯 **À retenir** — Les données sont la cible finale ; les protéger dans leurs trois états (repos, transit, usage) est l'objectif de tout le reste.


## Chapitre 59 — Humain

**Ce qu'elle contient.** Les personnes : utilisateurs, administrateurs, dirigeants, prestataires — leurs décisions, leur vigilance, leurs droits.

**Pourquoi exposée.** L'humain prend des décisions sous influence (urgence, autorité, peur, appât du gain) et détient des accès. Il est la cible de l'ingénierie sociale, qui contourne *toutes* les défenses techniques.

**Attaques typiques.** Phishing, vishing, BEC, manipulation/ingénierie sociale, MFA fatigue, menace interne (négligence ou malveillance), corruption.

🛡️ **Défense** — Sensibilisation continue, culture du signalement sans punition, procédures de vérification (double validation des paiements), moindre privilège, séparation des tâches, surveillance des comportements à risque.

🧭 **Taxonomie** — Surface transverse ; cœur de la Partie 9 (social engineering). « On ne patche pas l'humain, on l'accompagne. »

🎯 **À retenir** — L'humain est à la fois la cible la plus exploitée et le meilleur capteur : la sensibilisation est un contrôle de sécurité à part entière.


## Chapitre 60 — Physique

**Ce qu'elle contient.** Les locaux, datacenters, postes, équipements réseau, supports (disques, sauvegardes, clés USB), badges, et l'accès physique en général.

**Pourquoi exposée.** Un accès physique contourne la plupart des protections logiques : « qui contrôle le matériel contrôle souvent les données ». Vol, branchement de périphériques, accès aux consoles.

**Attaques typiques.** Vol d'équipements/supports, intrusion dans les locaux (tailgating), branchement de périphériques malveillants, accès aux consoles/ports, photographie d'écrans, fouille (dumpster diving).

🛡️ **Défense** — Contrôle d'accès physique (badges, sas), vidéosurveillance, chiffrement disque (protège la donnée en cas de vol), verrouillage des sessions, gestion des supports, destruction sécurisée, sensibilisation au tailgating.

🧭 **Taxonomie** — Surface fondamentale souvent négligée ; le chiffrement disque est le pont entre sécurité physique et protection de la donnée.

🎯 **À retenir** — La sécurité logique s'effondre sans sécurité physique : un accès matériel est un quasi-game over, sauf chiffrement.


## Chapitre 61 — Firmware et matériel

**Ce qu'elle contient.** Le code de bas niveau (BIOS/UEFI, firmware des cartes, microcontrôleurs), les composants matériels, les chaînes d'approvisionnement matérielles.

**Pourquoi exposée.** Couche *sous* le système d'exploitation : une compromission y est très furtive, persistante (survit à la réinstallation) et difficile à détecter. Rarement mise à jour, peu surveillée.

**Attaques typiques.** Bootkits/implants firmware, altération de la chaîne d'approvisionnement matérielle, exploitation de vulnérabilités UEFI, attaques par canaux auxiliaires (side-channel), périphériques malveillants.

🛡️ **Défense** — Secure Boot, mesure d'intégrité (TPM, attestation), mises à jour de firmware signées, approvisionnement de confiance, surveillance de l'intégrité, désactivation des interfaces de debug.

🧭 **Taxonomie** — La surface la plus *basse* de la pile ; recoupe la supply chain (chapitre 38) côté matériel. Persistance maximale pour l'attaquant.

🎯 **À retenir** — Une compromission firmware/matériel est furtive et persistante : Secure Boot et intégrité matérielle (TPM) sont les garde-fous.

---
