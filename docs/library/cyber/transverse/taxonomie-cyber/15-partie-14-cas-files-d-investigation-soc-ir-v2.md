---
title: Partie 14 — Cas filés d'investigation SOC/IR (V2)
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie cyber
chapter: 15
chapters: 15
---

> Cette partie répond à la principale limite du référentiel : le passage du *vocabulaire* au *raisonnement opérationnel*. Six cas filés déroulent le cycle complet **événement → alerte → hypothèse → qualification → investigation → confinement → éradication → rétablissement → REX**, en nommant à chaque étape les **sources de logs**, les **signaux faibles** et les **décisions défensives**.
>
> **Posture inchangée** : défensive et pédagogique. Les cas sont conceptuels — aucune procédure offensive, aucune commande d'exploitation. Les noms de journaux et d'identifiants d'événements sont donnés à titre indicatif (les versions exactes évoluent ; se reporter aux sources de l'Annexe I).

### Schéma de référence du cycle d'incident

```text
ÉVÉNEMENT ──► ALERTE ──► TRIAGE ──► QUALIFICATION ──► [INCIDENT ?]
                                                          │ oui
                                                          ▼
   INVESTIGATION ──► CONFINEMENT ──► ÉRADICATION ──► RÉTABLISSEMENT ──► REX
   (portée totale)   (stopper)       (tout retirer)  (restaurer sain)   (apprendre)
        ▲                                                                   │
        └───────────────── boucle d'amélioration continue ◄────────────────┘
```

🧭 **Comment lire un cas.** Chaque cas suit la même trame : *contexte → signal initial → classement taxonomique (renvois aux chapitres) → hypothèse → sources de logs → investigation/pivots → confinement → éradication → rétablissement → REX → erreurs à éviter*.

---

### Chapitre 314 — Cas 1 : Phishing avec vol d'identifiants

**Contexte.** Une PME en environnement cloud + SaaS. Un employé reçoit un e-mail « sécurité » imitant le fournisseur d'identité.

**Signal initial (événement → alerte).** Le SIEM corrèle : une connexion réussie à la messagerie cloud depuis un pays inhabituel, quelques minutes après que l'utilisateur a soumis ses identifiants sur un domaine récemment enregistré (vu dans les logs proxy/DNS).

**Classement taxonomique.** Surface : identité + messagerie (ch. 49, 57). Vulnérabilité-racine : confiance humaine + absence de MFA résistant au phishing (ch. 62). Attaque : phishing → vol d'identifiants (ch. 203), suivi possible d'un consent phishing (ch. 217). Tactique ATT&CK : *Initial Access / Credential Access*.

**Hypothèse.** « Un compte a été hameçonné ; l'attaquant teste l'accès et va chercher à persister (règles de boîte, octroi OAuth) puis à pivoter. »

**Sources de logs utiles.**
- Journaux de connexion du fournisseur d'identité (sign-in logs) : localisation, appareil, ASN, statut MFA.
- Journaux de la messagerie cloud : création de **règles de transfert/suppression** (signal faible majeur de compromission), accès inhabituels.
- Logs proxy/DNS : domaine de phishing visité.
- Journaux d'**octrois OAuth** : application tierce nouvellement autorisée.

**Investigation / pivots.**
1. Confirmer la connexion suspecte (lieu, appareil, heure) et son écart avec la ligne de base de l'utilisateur.
2. Chercher les **mécanismes de persistance** propres au cloud : règles de boîte cachées, octroi OAuth, inscription d'un nouveau facteur MFA par l'attaquant.
3. Vérifier les accès aux fichiers/SharePoint et les envois sortants (exfiltration, fraude type BEC — ch. 209).
4. Identifier les autres destinataires de la campagne (même expéditeur/domaine) pour mesurer l'ampleur.

**Confinement.** Invalider les sessions actives (révoquer les jetons), réinitialiser le mot de passe, désactiver temporairement le compte si besoin, bloquer le domaine de phishing (proxy/DNS/mail), retirer les règles de boîte malveillantes.

**Éradication.** Supprimer les octrois OAuth illégitimes, retirer tout facteur MFA ajouté par l'attaquant, confirmer l'absence de backdoor cloud. Élargir aux autres comptes ciblés par la campagne.

**Rétablissement.** Réactiver le compte avec **MFA résistant au phishing** (FIDO2/passkeys — ch. 282), surveiller étroitement les connexions, informer l'utilisateur.

**REX.** Renforcer le filtrage mail et SPF/DKIM/DMARC (ch. 294), passer au MFA anti-phishing, ajouter une détection « création de règle de transfert externe » et « octroi OAuth à risque », simuler un phishing de sensibilisation.

⚠️ **Erreurs à éviter.** Réinitialiser le mot de passe *sans* révoquer les sessions (le jeton volé reste valide — ch. 191) ; oublier les persistances cloud (règles, OAuth, MFA ajouté) ; ne pas chercher les autres victimes de la campagne.

🎯 **À retenir.** Un phishing cloud ne s'arrête pas au mot de passe : il faut révoquer les sessions *et* traquer la persistance (règles de boîte, OAuth, MFA ajouté). Le MFA anti-phishing est la correction de fond.

---

### Chapitre 315 — Cas 2 : Suspicion de Kerberoasting

**Contexte.** Domaine Active Directory on-premise. Un poste utilisateur a déjà été compromis (accès initial obtenu).

**Signal initial.** Le SIEM remonte un **volume anormal de demandes de tickets de service** (TGS-REQ) émanant d'un seul poste, ciblant plusieurs comptes de service dotés d'un SPN, avec demande d'un chiffrement faible.

**Classement taxonomique.** Surface : Active Directory / identité (ch. 43). Vulnérabilité-racine : comptes de service à mot de passe faible + SPN exposés (ch. 160). Attaque : Kerberoasting (ch. 163). Tactique ATT&CK : *Credential Access (T1558.003)*.

**Hypothèse.** « Un attaquant déjà présent récolte des tickets de comptes de service pour casser leurs mots de passe hors ligne et élever ses privilèges. »

**Sources de logs utiles.**
- Journaux Kerberos des contrôleurs de domaine : **demandes de tickets de service** (Event ID 4769), en filtrant sur les chiffrements faibles et le volume par compte source.
- EDR du poste source : processus à l'origine des demandes, comportement de collecte.
- Inventaire AD : comptes de service avec SPN, leurs privilèges et l'ancienneté de leurs mots de passe.

**Investigation / pivots.**
1. Identifier le poste/compte à l'origine des demandes (le « qui »).
2. Lister les comptes de service ciblés et **évaluer leur danger** : sont-ils privilégiés ? mots de passe faibles/anciens ?
3. Vérifier si un cassage a déjà abouti : connexions réussies récentes de ces comptes de service depuis des emplacements anormaux (signal d'élévation réussie).
4. Rechercher la suite logique : mouvement latéral (ch. 182), tentative vers le Tier 0 (ch. 162).

**Confinement.** Isoler le poste source (EDR), désactiver/forcer le changement des comptes de service à risque, surveiller le Tier 0.

**Éradication.** Réinitialiser les mots de passe des comptes de service compromis (idéalement migrer vers **gMSA** à rotation automatique — ch. 163), retirer les SPN inutiles, vérifier l'absence de persistance (tickets forgés — ch. 171/172, shadow credentials — ch. 179).

**Rétablissement.** Remettre le poste en service après reconstruction, durcir les comptes de service, renforcer la surveillance Kerberos.

**REX.** Imposer gMSA / mots de passe longs aléatoires aux comptes de service, appliquer le tiering (ch. 162), créer/affiner la détection « TGS-REQ en volume + chiffrement faible », auditer régulièrement les SPN et privilèges.

⚠️ **Erreurs à éviter.** Traiter l'alerte comme un simple « bruit Kerberos » sans vérifier le cassage réussi ; réinitialiser les comptes de service sans corriger leur faiblesse de fond (gMSA) ; ignorer la progression possible vers le Tier 0.

🎯 **À retenir.** Le Kerberoasting est silencieux et hors-ligne : la détection se fait sur le *comportement de demande* (volume TGS-REQ, chiffrement faible), et la correction de fond est gMSA + tiering.

---

### Chapitre 316 — Cas 3 : Malware sur un poste de travail

**Contexte.** Poste utilisateur Windows. Une pièce jointe a été ouverte et a activé une macro.

**Signal initial.** L'EDR alerte sur un document bureautique lançant un processus enfant qui établit une connexion sortante vers un domaine de mauvaise réputation (comportement de loader/downloader — ch. 194/196).

**Classement taxonomique.** Surface : poste utilisateur (ch. 40). Vulnérabilité-racine : macro autorisée + confiance utilisateur (ch. 200). Attaque : macro malware → loader → charge (RAT/infostealer — ch. 192/191). Tactique ATT&CK : *Execution / Command and Control*.

**Hypothèse.** « Un loader a été exécuté via macro et tente de récupérer une charge ; il faut empêcher la suite (charge, persistance, C2) et vérifier le vol de secrets. »

**Sources de logs utiles.**
- EDR : arbre de processus (document → interpréteur → enfant), injections mémoire (fileless — ch. 199), persistance (tâches planifiées, clés de démarrage).
- Journaux DNS/proxy : domaine C2 contacté, autres résolutions suspectes.
- Journaux d'authentification : usage des identifiants depuis le poste (signe de vol/infostealer).

**Investigation / pivots.**
1. Reconstituer l'arbre de processus et déterminer si une charge a été récupérée/exécutée.
2. Chercher la **persistance** (tâches, démarrage, services).
3. Évaluer le **vol de secrets** (infostealer — ch. 191) : si des identifiants/jetons ont pu être volés, traiter aussi le volet identité (révoquer sessions, réinitialiser).
4. Vérifier un éventuel **mouvement latéral** initié depuis le poste.

**Confinement.** **Isoler le poste du réseau via l'EDR** (sans l'éteindre, pour préserver la mémoire/preuves — ch. 263), bloquer le domaine C2.

**Éradication.** Supprimer la charge et toute persistance ; en cas de doute sur la profondeur (fileless, rootkit — ch. 197), **reconstruire le poste** plutôt que nettoyer. Si vol de secrets confirmé : réinitialiser les identifiants concernés et révoquer les sessions.

**Rétablissement.** Réimager le poste, restaurer les données depuis une sauvegarde saine, surveiller le poste et le compte.

**REX.** Bloquer les macros (surtout depuis Internet — ch. 200), renforcer le filtrage mail, vérifier la couverture EDR, ajouter une détection « document → processus enfant → connexion sortante », sensibiliser.

⚠️ **Erreurs à éviter.** Éteindre le poste (perte des preuves mémoire) ; « nettoyer » un poste potentiellement infecté en profondeur au lieu de le reconstruire ; oublier le volet identité si un infostealer a opéré.

🎯 **À retenir.** Sur un malware de poste : isoler (sans éteindre), reconstruire en cas de doute, et toujours évaluer le vol d'identifiants — l'incident « poste » devient souvent un incident « identité ».

---

### Chapitre 317 — Cas 4 : Exfiltration depuis le cloud

**Contexte.** Environnement cloud IaaS. Une clé d'accès a fuité (dépôt public — ch. 222).

**Signal initial.** Les journaux d'audit cloud montrent un usage d'une clé d'accès depuis une adresse inhabituelle, avec une rafale d'opérations de **listing et de lecture sur des buckets** de stockage.

**Classement taxonomique.** Surface : cloud (ch. 46). Vulnérabilité-racine : secret exposé + permissions excessives (ch. 221/219). Attaque : usage de clé volée → accès aux données → exfiltration ; risque d'élévation (ch. 224) et de lateral movement cloud (ch. 225). Tactique ATT&CK : *Collection / Exfiltration*.

**Hypothèse.** « Une clé exposée est utilisée pour lire et exfiltrer des données ; l'attaquant peut tenter d'élever ses privilèges et de persister (nouvelle clé/utilisateur). »

**Sources de logs utiles.**
- Journaux d'audit cloud (type CloudTrail / journaux d'activité) : appels d'API, source, identité utilisée, opérations sur le stockage.
- Journaux d'accès au stockage : volumes lus/téléchargés (mesurer l'exfiltration).
- Journaux IAM : création de clés/utilisateurs/rôles, modifications de politiques (persistance/élévation).

**Investigation / pivots.**
1. Identifier la clé compromise et **toutes** ses actions (lecture, mais aussi création d'accès, modification de politiques).
2. Mesurer le périmètre de données exfiltrées (quels buckets, quel volume) — impact réglementaire potentiel.
3. Chercher la **persistance** : nouvelles clés/utilisateurs/rôles créés, politiques modifiées (auto-élévation — ch. 224).
4. Vérifier le rebond vers d'autres comptes/services (relations de confiance — ch. 225).

**Confinement.** **Révoquer/désactiver immédiatement la clé** compromise, restreindre les accès au stockage concerné, bloquer la source si possible.

**Éradication.** Supprimer toute persistance créée (clés/utilisateurs/rôles illégitimes), corriger les politiques modifiées, faire tourner les secrets potentiellement exposés.

**Rétablissement.** Émettre de nouveaux secrets à portée minimale, durcir les permissions (moindre privilège IAM — ch. 219), activer le blocage public par défaut (ch. 220), renforcer la surveillance.

**REX.** Déployer le **secrets scanning** (ch. 300) et un coffre-fort (ch. 244), appliquer le moindre privilège IAM et l'analyse des chemins d'élévation, activer/affiner les alertes « usage de clé depuis source inhabituelle » et « création d'accès IAM », gérer l'obligation de notification si fuite de données personnelles (ch. 268).

⚠️ **Erreurs à éviter.** Désactiver la clé sans chercher la persistance IAM créée entre-temps ; sous-estimer le périmètre de données (impact réglementaire) ; réémettre des secrets surprivilégiés.

🎯 **À retenir.** Une clé cloud volée mène vite à l'exfiltration *et* à la persistance IAM : révoquer la clé ne suffit pas, il faut traquer les accès créés et corriger le moindre privilège. La prévention de fond est le coffre-fort + le scanning.

---

### Chapitre 318 — Cas 5 : Ransomware

**Contexte.** Réseau d'entreprise mixte. Accès initial obtenu (ex. RDP exposé — ch. 140, ou phishing), suivi d'un mouvement latéral.

**Signal initial.** Vague d'alertes EDR/SIEM : **chiffrement massif de fichiers** sur plusieurs serveurs, **suppression des clichés/sauvegardes** accessibles, comptes d'administration utilisés à des heures inhabituelles. Souvent précédée (rétrospectivement) de signaux faibles : reconnaissance interne, désactivation de défenses.

**Classement taxonomique.** Surface : multiple (serveurs, identité, réseau). Vulnérabilité-racine : multiple (accès exposé, réutilisation d'identifiants, absence de segmentation/tiering). Attaque : ransomware (ch. 188), souvent avec double extorsion (exfiltration préalable). Tactique ATT&CK : *Impact (T1486)*, précédé de *Lateral Movement / Exfiltration*.

**Hypothèse.** « Un opérateur de ransomware est présent depuis un certain temps ; il a probablement exfiltré avant de chiffrer (double extorsion) et cherché à neutraliser les sauvegardes. »

**Sources de logs utiles.**
- EDR/SIEM : début du chiffrement, processus responsable, propagation, suppression de clichés/sauvegardes.
- Journaux d'authentification/AD : usage de comptes d'administration, mouvement latéral (ch. 182), accès au Tier 0.
- Journaux réseau/exfiltration : volumes sortants anormaux *avant* le chiffrement (double extorsion).
- Journaux des sauvegardes : tentatives de suppression/altération.

**Investigation / pivots.**
1. Déterminer l'**étendue** (machines chiffrées, données exfiltrées) et le **point d'entrée initial** (RDP, phishing, VPN — ch. 141).
2. Reconstituer le **mouvement latéral** et l'accès aux comptes privilégiés (krbtgt compromis ? ch. 171).
3. Évaluer l'**exfiltration** (impact réglementaire et négociation).
4. Identifier les sauvegardes **saines et hors-ligne/immuables** disponibles (ch. 287).

**Confinement.** **Segmenter/isoler** massivement (couper les liaisons entre zones) pour stopper la propagation, désactiver les comptes compromis, **déclencher la cellule de crise** (ch. 39/266) et activer le **PRA/PCA** (ch. 267). Communication de crise et obligations de notification (ch. 268).

**Éradication.** Identifier et supprimer *toute* la présence de l'attaquant (backdoors, comptes, persistance, krbtgt à roter deux fois si AD compromis — ch. 171) avant toute reconnexion. Une éradication partielle = rechiffrement.

**Rétablissement.** Restaurer depuis des **sauvegardes immuables et vérifiées** (ch. 287), reconstruire les systèmes critiques, corriger le vecteur initial, surveiller étroitement la réapparition de l'attaquant pendant la reprise.

**REX.** Supprimer les expositions (RDP/VPN — ch. 140/141), imposer MFA et tiering, déployer des sauvegardes immuables testées, segmenter, améliorer la détection précoce (reconnaissance interne, désactivation de défenses, suppression de clichés), réaliser des exercices de crise (tabletop — ch. 304).

⚠️ **Erreurs à éviter.** Restaurer avant d'avoir éradiqué (rechiffrement) ; restaurer depuis une sauvegarde elle-même compromise/en ligne ; négliger l'exfiltration (la double extorsion change la gestion de crise) ; payer en croyant que cela garantit la récupération (un wiper déguisé — ch. 189 — ne déchiffre rien).

🎯 **À retenir.** Le ransomware est l'aboutissement d'une intrusion complète : confiner (segmenter) + cellule de crise + éradication exhaustive *avant* restauration depuis l'immuable. La prévention de fond combine sauvegardes immuables testées, segmentation, tiering, MFA et détection précoce.

---

### Chapitre 319 — Cas 6 : SSRF vers les métadonnées cloud

**Contexte.** Application web hébergée sur une instance cloud, exposant une fonctionnalité qui récupère une ressource à partir d'une URL fournie.

**Signal initial.** Le NDR/journaux applicatifs montrent que le **serveur applicatif initie des requêtes vers l'adresse interne du service de métadonnées** de l'instance, puis un usage anormal des identifiants de rôle de l'instance apparaît dans les journaux cloud.

**Classement taxonomique.** Surface : web + cloud (ch. 44/46). Vulnérabilité-racine : validation/allowlist d'URL insuffisante + confiance (ch. 80). Attaque : SSRF → métadonnées cloud (ch. 105/107). Tactique ATT&CK : *Credential Access / Discovery*.

**Hypothèse.** « Une SSRF est exploitée pour atteindre le service de métadonnées et récupérer les identifiants temporaires du rôle de l'instance, ensuite utilisés pour accéder aux ressources cloud. »

**Sources de logs utiles.**
- Journaux applicatifs / reverse proxy : URL fournies en paramètre, requêtes sortantes du serveur.
- NDR / journaux réseau : **accès au point de métadonnées** depuis l'application (signal fort).
- Journaux d'audit cloud : usage des identifiants de rôle d'instance depuis des contextes anormaux, opérations sur les ressources.

**Investigation / pivots.**
1. Confirmer la SSRF (paramètre d'URL menant à l'adresse de métadonnées) et son exploitation.
2. Déterminer si des **identifiants de rôle** ont été récupérés et utilisés (journaux cloud).
3. Mesurer les actions effectuées avec ce rôle (lecture/exfiltration, élévation, persistance — comme le Cas 4).
4. Identifier le périmètre des ressources accessibles via ce rôle (impact lié au moindre privilège).

**Confinement.** Corriger/bloquer la fonctionnalité vulnérable (allowlist stricte, blocage de l'adresse de métadonnées), **révoquer/roter les identifiants de rôle** potentiellement exposés, restreindre les actions du rôle.

**Éradication.** Supprimer toute persistance créée avec le rôle (cf. Cas 4), corriger le code de l'application (allowlist de destinations, normalisation d'URL — ch. 105).

**Rétablissement.** Déployer la version corrigée, activer la **version renforcée du service de métadonnées** (étape supplémentaire requise pour y accéder), appliquer le **moindre privilège** au rôle d'instance, renforcer la surveillance.

**REX.** Généraliser la version renforcée des métadonnées et le filtrage sortant (egress filtering), revoir les rôles d'instance (moindre privilège), ajouter une détection « accès applicatif au point de métadonnées », intégrer un test SSRF aux campagnes DAST (ch. 297).

⚠️ **Erreurs à éviter.** Corriger la SSRF sans roter les identifiants déjà exposés ; laisser le service de métadonnées en version permissive ; conserver un rôle d'instance surprivilégié.

🎯 **À retenir.** Une SSRF côté web devient un vol d'identifiants côté cloud : la réponse couvre les *deux* surfaces (corriger le code + roter le rôle + durcir les métadonnées). Prévention de fond : allowlist SSRF, métadonnées renforcées, moindre privilège des rôles.

---

> **Synthèse de la Partie 14.** Ces six cas illustrent un invariant : un incident traverse presque toujours *plusieurs surfaces* (un phishing devient un incident identité ; une SSRF devient un incident cloud ; un malware de poste devient un vol d'identifiants). Le réflexe opérationnel est donc : **comprendre la portée complète avant d'agir**, **confiner sans détruire les preuves**, **éradiquer exhaustivement** (toute la persistance) *avant* de **rétablir depuis du sain**, puis **apprendre** (REX). C'est l'application vivante du fil rouge et de la posture *assume breach*.

---


## Annexes

### Annexe A — Glossaire cyber essentiel

- **Actif** : ce qui a de la valeur et qu'on protège (donnée, service, système, identité).
- **Menace** : danger potentiel (acteur/événement) pouvant nuire.
- **Vulnérabilité** : faiblesse exploitable.
- **Risque** : combinaison vraisemblance × impact d'une menace exploitant une vulnérabilité.
- **Impact** : gravité des conséquences.
- **CIA/DIC** : Confidentialité, Intégrité, Disponibilité.
- **Authentification** : prouver son identité. **Autorisation** : déterminer ses droits.
- **Surface d'attaque** : ensemble des points exploitables.
- **Défense en profondeur** : empilement de couches indépendantes.
- **Moindre privilège** : droits strictement nécessaires.
- **Zero Trust** : ne jamais faire confiance par défaut, toujours vérifier.
- **Assume breach** : supposer la compromission pour mieux limiter/détecter/répondre.
- **Tiering** : cloisonnement des niveaux d'administration (Tier 0/1/2).
- **MFA** : authentification multi-facteur ; *résistant au phishing* = FIDO2/passkeys, number matching.
- **EDR/NDR/SIEM/SOAR** : détection/réponse hôte / réseau / corrélation centrale / automatisation.
- **IOC/IOA/TTP** : indicateur de compromission / d'attaque / tactiques-techniques-procédures.
- **CVE/CVSS/EPSS/KEV** : identifiant de vulnérabilité / score de gravité / probabilité d'exploitation / catalogue d'exploitation active.
- **SBOM** : inventaire des composants logiciels.
- **PRA/PCA** : reprise / continuité d'activité ; **RTO/RPO** : délai de reprise / perte de données acceptables.
- **Lateral movement** : déplacement interne de l'attaquant.
- **RCE** : exécution de code à distance.
- **Pentest / bug bounty / purple teaming** : test offensif ponctuel / continu communautaire / collaboration red-blue.

### Annexe B — Tableau de correspondance central (fiche réflexe)

> **Tableau-pivot du référentiel** (enrichi en V2). Pour chaque attaque majeure : famille, vulnérabilité-racine, surface, propriété CIA visée, **logs utiles** (où chercher), **défenses principales**. C'est l'outil pratique à garder sous la main pour relier *attaque ↔ vulnérabilité ↔ surface ↔ impact ↔ détection ↔ défense* en une ligne.

| Attaque | Famille | Vulnérabilité-racine | Surface | Impact CIA | Logs utiles | Défenses principales |
|---|---|---|---|---|---|---|
| Stored XSS | Injection | Encodage de sortie absent | Web | Confidentialité / Intégrité | Logs applicatifs, rapports CSP, WAF | Encodage contextuel, CSP, cookies HttpOnly |
| Reflected/DOM XSS | Injection | Sortie/sink non sécurisés | Web / navigateur | Confidentialité | Logs app, CSP, analyse JS client | Encodage, CSP, Trusted Types |
| SQLi | Injection | Requête concaténée | Web / base | Confidentialité / Intégrité | Erreurs SQL, logs base/app, WAF | Requêtes paramétrées, moindre privilège base |
| Command injection | Injection | Concaténation vers shell | Web / serveur | C/I/Disponibilité | EDR serveur (processus enfants), logs app | API sans shell, allowlist, moindre privilège |
| SSTI | Injection | Entrée dans la structure du template | Web / serveur | C/I/D (RCE) | Logs app, EDR, comportement d'évaluation | Données en variables (jamais en template), sandbox |
| XXE | Parsing | Entités externes XML activées | Web / API | Confidentialité (+SSRF) | Logs app, accès fichiers/réseau du parser | Désactiver entités externes & DOCTYPE |
| IDOR / BOLA | Contrôle d'accès | Défaut d'autorisation par objet | Web / API | Confidentialité / Intégrité | Logs API (accès hors périmètre), énumération d'IDs | Contrôle d'accès par objet côté serveur, deny by default |
| BFLA | Contrôle d'accès | Défaut d'autorisation par fonction | API | Intégrité / privilège | Logs API (appels privilégiés) | Contrôle d'autorisation par fonction, séparation des rôles |
| SSRF → métadonnées | Falsification requête | Validation/allowlist d'URL insuffisante | Web / cloud | Confidentialité (secrets) | Proxy/app, NDR, accès au point de métadonnées, audit cloud | Allowlist, egress filtering, métadonnées renforcées, moindre privilège du rôle |
| CSRF | Falsification requête | Pas de jeton anti-CSRF / SameSite | Web | Intégrité | Logs app (requêtes sans jeton/origine incohérente) | Jetons anti-CSRF, SameSite, vérification d'origine |
| Path traversal / LFI / Zip Slip | Accès fichiers | Chemin dérivé d'une entrée | Web / serveur | Confidentialité (+RCE) | Logs app (séquences de traversée), accès fichiers | Allowlist mappée, normaliser puis vérifier l'appartenance |
| Unrestricted upload | Accès fichiers | Type/emplacement non contrôlés | Web | C/I/D (RCE) | Logs upload, EDR, accès aux fichiers servis | Valider le contenu réel, stockage hors webroot, domaine isolé |
| Insecure deserialization | Intégrité logicielle | Désérialisation d'entrée non fiable | Web / serveur | C/I/D (RCE) | EDR (instanciation/processus), logs app | Ne pas désérialiser le non fiable, signer/typer strictement |
| Request smuggling | Parsing protocole | Désaccord de framing entre serveurs | Web / infra | Intégrité / Confidentialité | Logs frontal/back incohérents, outils dédiés | Normaliser au frontal, rejeter l'ambiguïté, HTTP cohérent |
| Cache poisoning / deception | Infra web | Clé de cache incomplète / cache de privé | Web / CDN | Intégrité / Confidentialité | Logs cache/CDN, réponses incohérentes | Clé de cache complète, ne jamais cacher le privé |
| Bucket public | Mauvaise configuration | Accès public par défaut | Cloud | Confidentialité | CSPM, audit cloud, accès anonymes | Blocage public par défaut, CSPM, chiffrement |
| Clé/secret exposé | Exposition de secrets | Secret hors coffre | Cloud / CI-CD | Confidentialité | Secrets scanning, audit cloud (usage de clé) | Coffre-fort, portée minimale, rotation, scanning |
| Privilege escalation cloud | Autorisation cloud | Permissions IAM dangereuses | Cloud | C/I/privilège | Audit IAM (modif. politiques/rôles) | Moindre privilège, suppression des chemins d'auto-élévation |
| Kubernetes RBAC abuse | Autorisation conteneurs | RBAC trop large | Conteneurs | C/I/privilège | Audit Kubernetes, API server | Moindre privilège RBAC, comptes de service minimaux |
| Container escape | Élévation conteneurs | Conteneur privilégié / montages | Conteneurs | C/I/D | Runtime security, EDR, audit | Conteneurs non privilégiés, capacités/montages minimaux |
| Dependency confusion / typosquat | Supply chain | Résolution de paquets | CI-CD / dépendances | C/I/D (RCE) | Logs build, résolution de sources | Dépôts internes prioritaires, lockfiles, SBOM/SCA |
| CI/CD / pipeline poisoning | Supply chain | Build/pipeline non protégé | CI-CD | C/I/D | Logs CI, intégrité des artefacts | Moindre privilège, isolation, provenance/signature (SLSA) |
| Password spraying | Authentification | Mots de passe faibles, pas de MFA | Identité | C/privilège | Auth logs (échecs multi-comptes), sign-in logs | MFA, bannissement de mots de passe courants, détection de spraying |
| Credential stuffing | Authentification | Réutilisation de mots de passe | Identité / SaaS | Confidentialité | Sign-in logs (taux d'échec élevé, sources distribuées) | MFA, détection d'identifiants fuités, rate limiting |
| Kerberoasting | Identité (AD) | Compte de service/SPN + mot de passe faible | Active Directory | Confidentialité / privilège | Kerberos 4769 (TGS-REQ + chiffrement faible), EDR | gMSA, mots de passe longs, tiering, détection comportementale |
| Pass-the-hash / ticket | Identité (AD) | Réutilisation de secrets + privilèges excessifs | Active Directory | Privilège / latéral | Auth NTLM/Kerberos anormales, EDR | Tiering, LAPS, Credential Guard, restriction NTLM |
| DCSync | Identité (AD) | Droits de réplication excessifs | Active Directory | Confidentialité (secrets domaine) | Réplication depuis hôte non-DC, audit droits | Restreindre/surveiller les droits de réplication (Tier 0) |
| Golden ticket | Identité (AD) | Secret krbtgt compromis | Active Directory | Privilège / persistance | Tickets aux propriétés anormales (durée/chiffrement) | Protéger krbtgt, double rotation post-incident, surveillance DC |
| AD CS abuse | Identité (AD) | Modèles de certificats permissifs | Active Directory | Privilège / persistance | Inscriptions de certificats anormales, audit CA | Durcir modèles & droits, CA en Tier 0 |
| Lateral movement | Mouvement latéral | Réutilisation d'identifiants + réseau plat | Réseau / AD | Latéral / privilège | Connexions inter-machines, EDR/NDR, SIEM | Segmentation, tiering, LAPS, MFA admin |
| Ransomware | Impact (multi) | Accès + propagation + privilèges | Multi | Disponibilité (+Confidentialité) | EDR (chiffrement, suppression clichés), auth, exfiltration | Sauvegardes immuables/testées, segmentation, MFA, tiering, détection précoce |
| Wiper | Impact (destruction) | Accès + sabotage | Multi | Disponibilité / Intégrité | EDR (destruction), comportements | Sauvegardes hors-ligne, segmentation, continuité |
| Infostealer | Malware (vol) | Malware sur poste + secrets accessibles | Poste / identité | Confidentialité | EDR (accès aux stockages de secrets), connexions par jeton | EDR, expiration de session, MFA anti-phishing |
| Phishing | Ingénierie sociale | Confiance humaine, pas de MFA fort | Messagerie / humain | Confidentialité | Sign-in logs, logs mail/proxy, création de règles de boîte | Sensibilisation, filtrage mail, SPF/DKIM/DMARC, MFA anti-phishing |
| BEC | Ingénierie sociale | Confiance + pas de double validation | Messagerie / humain | Intégrité (fraude) | Logs mail (expéditeur/domaine), règles de boîte | Double validation hors canal, séparation des tâches, DMARC |
| Consent phishing | Ingénierie sociale / OAuth | Octroi OAuth non gouverné | SaaS / identité | Confidentialité / persistance | Journaux d'octrois OAuth | Gouvernance des consentements OAuth, allowlist d'applications |
| MFA fatigue | Contournement MFA | Push simple (approuver/refuser) | Identité | Privilège / accès | Volume anormal de demandes MFA, approbation après rafale | MFA résistant au phishing (FIDO2, number matching) |
| ARP/DNS/DHCP spoofing → MITM | Usurpation réseau | Protocoles non authentifiés | Réseau | Confidentialité / Intégrité | NDR, anomalies d'association, alertes WIPS | DAI, DHCP snooping, chiffrement authentifié, DNSSEC |
| DNS tunneling | Exfiltration / C2 | DNS sortant non inspecté | Réseau | Confidentialité | Logs DNS (volume/entropie/fréquence), NDR | Inspection/filtrage DNS, détection d'anomalies |
| DDoS | Disponibilité | Capacité finie / spoofing | Réseau | Disponibilité | NetFlow, signatures DDoS, alertes amont | Anti-DDoS amont (scrubbing/CDN), anti-spoofing (BCP38) |
| BGP hijacking | Routage | Confiance BGP non validée | Infra Internet | Intégrité / Disponibilité | Monitoring BGP, anomalies de chemins | RPKI, filtrage de préfixes, MANRS |

🧭 **Mode d'emploi.** Lire une ligne de gauche à droite, c'est dérouler le fil rouge sur une attaque : *où elle frappe* (surface), *pourquoi elle marche* (vulnérabilité-racine), *ce qu'elle vise* (CIA), *où la voir* (logs), *comment l'arrêter* (défenses). Pour une attaque inconnue, appliquer d'abord la méthode du chapitre 306, puis l'inscrire dans ce format.

### Annexe C — Tableau surface → attaques typiques → logs utiles

| Surface | Attaques typiques | Sources de logs utiles |
|---|---|---|
| Poste utilisateur | Phishing, malware, infostealer | EDR, logs système, proxy/DNS |
| Active Directory | Kerberoasting, DCSync, pass-the-hash | Journaux AD/Kerberos, EDR, SIEM |
| Application web | XSS, SQLi, IDOR, SSRF | Logs applicatifs, WAF, accès HTTP |
| API | BOLA, BFLA, exposition de données | Logs API/passerelle |
| Cloud | Buckets publics, IAM, métadonnées | Journaux cloud (audit), CSPM |
| Réseau | Scan, MITM, lateral movement | NDR/IDS, flux (NetFlow), DNS |
| Messagerie | Phishing, BEC, malspam | Logs mail, DMARC reports |
| Conteneurs/K8s | RBAC abuse, container escape | Audit Kubernetes, runtime security |

### Annexe D — Tableau de correspondance des cadres

| Besoin | Cadre de référence |
|---|---|
| Fonctions de sécurité de haut niveau | NIST CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover) |
| Tactiques/techniques adverses | MITRE ATT&CK |
| Contre-mesures défensives | MITRE D3FEND |
| Patterns d'attaque | MITRE CAPEC |
| Faiblesses logicielles | CWE |
| Risques applicatifs web | OWASP Top 10 |
| Risques API | OWASP API Security Top 10 (2023) |
| Vérification applicative | OWASP ASVS |
| Intégrité de la supply chain | SLSA, SBOM |
| Analyse de risque | EBIOS RM, ISO 27005, FAIR |
| Gestion de la sécurité | ISO/IEC 27001 |

**Logique de lecture :** ATT&CK décrit *ce que fait l'attaquant* ; CWE/CAPEC, *par quelle faiblesse/pattern* ; D3FEND, *comment se défendre* ; NIST CSF, *comment organiser le tout* ; OWASP, *les risques applicatifs concrets*.

### Annexe E — Fiches réflexes

**XSS** — Encoder la sortie selon le contexte ; CSP ; cookies HttpOnly ; assainir le HTML riche. *Racine : injection côté navigateur.*

**SQLi** — Requêtes paramétrées partout (y compris données stockées) ; moindre privilège base ; erreurs génériques. *Racine : injection SQL.*

**SSRF** — Allowlist de destinations ; bloquer plages internes et service de métadonnées ; filtrage sortant ; durcir les rôles d'instance. *Racine : confiance dans une URL fournie.*

**Phishing** — Sensibilisation + culture du signalement ; filtrage mail ; SPF/DKIM/DMARC ; MFA résistant au phishing. *Racine : manipulation humaine.*

**Ransomware** — Sauvegardes immuables/testées ; segmentation ; MFA ; EDR ; patch ; tiering ; plan de crise/PRA. *Racine : multiple (accès + propagation).*

**Compromission AD** — Tiering (protéger le Tier 0/krbtgt) ; PAM/bastion ; LAPS ; Credential Guard ; audit ACL/délégations/GPO ; surveillance. *Racine : exposition/réutilisation de secrets privilégiés.*

### Annexe F — Mini-cas d'analyse défensive

**Cas 1 — Alerte « connexion réussie après 200 échecs sur 200 comptes ».**
Classer : authentification, password spraying (chapitre 165). Réponse : confiner le compte réussi, vérifier MFA, chercher le mouvement latéral. Fond : MFA + détection de spraying.

**Cas 2 — Un serveur web initie des requêtes vers l'adresse interne de métadonnées.**
Classer : SSRF vers métadonnées cloud (chapitre 107). Réponse : couper, vérifier l'usage des identifiants de rôle, roter. Fond : allowlist SSRF + métadonnées renforcées + moindre privilège.

**Cas 3 — Chiffrement massif de fichiers + suppression de clichés sur plusieurs serveurs.**
Classer : ransomware (chapitre 188), avec lateral movement. Réponse : confiner/segmenter, déclencher la cellule de crise et le PRA, restaurer depuis l'immuable. Fond : sauvegardes immuables + segmentation + MFA + tiering.

### Annexe G — Cartographie des métiers cyber

- **SOC analyst (N1/N2/N3)** : détection, triage, qualification, réponse de premier niveau.
- **Incident responder / DFIR** : investigation, forensic, éradication, rétablissement.
- **Threat intelligence (CTI)** : connaissance des menaces, acteurs, TTP, alimentation de la détection.
- **Pentester / Red team** : test offensif autorisé, simulation d'adversaire.
- **Blue team / Detection engineer** : construction et réglage des détections.
- **Purple team** : pont red/blue pour améliorer la détection.
- **GRC / Risk manager** : gouvernance, analyse de risque, conformité, homologation.
- **Security architect** : conception sécurisée (secure by design, Zero Trust).
- **AppSec / Product security** : sécurité du développement (SAST/DAST, threat modeling).
- **Cloud security engineer** : sécurité des environnements cloud (IAM, configuration, CSPM).
- **IAM/PAM engineer** : identités, accès, comptes privilégiés.
- **RSSI / CISO** : pilotage stratégique de la sécurité.

🧭 Ces métiers se répartissent sur le fil rouge : *prévenir* (architecture, AppSec, GRC), *détecter/répondre* (SOC, DFIR, CTI), *évaluer* (pentest, purple), *gouverner* (RSSI, GRC).

### Annexe H — Apprendre les attaques sans apprendre à attaquer illégalement

Principes pour progresser de façon **légale et éthique** :

1. **Comprendre les mécanismes, pas les payloads** : ce cours privilégie le *pourquoi ça marche* et *comment s'en défendre*.
2. **S'entraîner uniquement dans des environnements autorisés** : laboratoires personnels isolés, plateformes d'entraînement légales et dédiées, machines virtuelles vous appartenant, environnements de CTF/lab conçus pour cela.
3. **N'attaquer que ce qu'on est explicitement autorisé à tester** : un test sur un système sans autorisation écrite est illégal, même « pour apprendre ».
4. **Privilégier la posture défensive (blue/purple)** : détecter, comprendre les TTP (ATT&CK), construire des détections — une voie d'apprentissage riche et sans risque légal.
5. **Pratiquer la divulgation responsable** : si l'on découvre une faille, la signaler par les canaux prévus (bug bounty, contact sécurité), jamais l'exploiter.
6. **Se former via les cadres** : ATT&CK, OWASP, CWE/CAPEC, D3FEND offrent une montée en compétence structurée et légale.

⚠️ La frontière est simple : la *connaissance* est libre ; l'*action* sur un système exige une *autorisation*. Ce cours vise la première et la défense.

### Annexe I — Bibliographie indicative et standards à surveiller

- **NIST Cybersecurity Framework 2.0** — organisation des fonctions de sécurité.
- **MITRE ATT&CK** — base de connaissances des TTP adverses (à suivre, mise à jour régulière).
- **MITRE D3FEND** — contre-mesures défensives.
- **MITRE CAPEC** — patterns d'attaque.
- **CWE** — faiblesses logicielles (Top 25 mis à jour périodiquement).
- **OWASP Top 10** (web) et **OWASP API Security Top 10** (API) — révisés régulièrement.
- **OWASP ASVS** — exigences de vérification applicative.
- **ISO/IEC 27001 / 27005** — management et risque.
- **EBIOS Risk Manager (ANSSI)** — méthode d'analyse de risque.
- **CIS Benchmarks / CIS Controls** — durcissement et contrôles prioritaires.
- **SLSA** et travaux SBOM (formats type CycloneDX/SPDX) — intégrité de la supply chain.
- **Catalogue KEV (CISA)** — vulnérabilités activement exploitées, pour prioriser.

> **Note de mise à jour.** La cybersécurité évolue vite : versions de référentiels, nouvelles techniques, nouveaux outils. La *taxonomie* de ce référentiel (les familles et les principes) reste stable ; les *détails* (versions, CVE, produits) doivent être réactualisés via les sources ci-dessus.

### Annexe J — Schémas mentaux (ASCII)

> Quelques cartes mentales minimalistes à mémoriser. En cybersécurité, un bon schéma vaut souvent un paragraphe.

**Le fil rouge du référentiel**
```text
ACTIF → MENACE → VULNÉRABILITÉ → RISQUE → ATTAQUE → IMPACT → DÉTECTION → RÉPONSE → REMÉDIATION
```

**Chaîne d'un chemin d'attaque typique (du clic au domaine)**
```text
Phishing/Exploit → Poste compromis → Vol d'identifiants → Mouvement latéral → Tier 0 → Domaine compromis
   (Initial Access)   (Execution)      (Credential Access)   (Lateral Mvt)     (PrivEsc)   (Impact)
```

**SSRF → cloud (deux surfaces)**
```text
Attaquant → Application vulnérable (URL fournie) → Service de métadonnées → Identifiants de rôle → Ressources cloud
            [allowlist + egress filtering]          [métadonnées renforcées]  [moindre privilège du rôle]
```

**Injection (principe unique, plusieurs interpréteurs)**
```text
Entrée non fiable ─┬─► Navigateur  → XSS
                   ├─► SQL         → SQLi
                   ├─► Shell       → Command injection
                   ├─► LDAP/XPath  → LDAP/XPath injection
                   └─► Template    → SSTI
   Parade commune : SÉPARER données et code (paramétrage + encodage de sortie)
```

**Cycle de réponse à incident**
```text
Événement → Alerte → Triage → Qualification → [Incident] → Investigation →
Confinement → Éradication → Rétablissement → REX ──(boucle d'amélioration)──► Préparation
```

**Tiering Active Directory (étanchéité)**
```text
Tier 0  [Contrôleurs de domaine, krbtgt, IAM, AD CS]   ◄── ne jamais exposer ses identifiants plus bas
   ▲ (jamais de contrôle depuis le bas)
Tier 1  [Serveurs & applications]
   ▲
Tier 2  [Postes de travail]
```

**Défense en profondeur (un mail malveillant face aux couches)**
```text
Mail → [Filtrage mail] → [Sensibilisation] → [EDR] → [Moindre privilège] → [Segmentation] → [Détection SOC]
        chaque couche peut faillir ; l'attaquant doit TOUTES les franchir
```

**Pyramide de la douleur (valeur de la détection)**
```text
        TTP        ◄── le plus douloureux pour l'attaquant (change ses méthodes)
      Outils
   Artefacts réseau/hôte
      Noms de domaine
        IOC (hash, IP)  ◄── le moins douloureux (changé en un instant)
```

🎯 **À retenir** — Ces schémas condensent les invariants du référentiel : un même principe (injection, défense en profondeur, tiering, cycle d'incident) se décline partout. Les mémoriser, c'est tenir la carte mentale en tête.

---

> **Fin du référentiel.**
>
> Vous disposez désormais d'une cartographie complète et structurée de la cybersécurité : **14 parties, 319 chapitres** (dont 6 cas filés d'investigation), des fondations au raisonnement SOC/IR, reliées par un fil rouge unique et outillées de tableaux de correspondance et de schémas mentaux. L'objectif n'était pas de tout mémoriser, mais d'acquérir la **carte mentale** qui permet de *classer, relier, défendre et répondre* — y compris face à des menaces jamais rencontrées.
>
> Ce document est un **référentiel-pivot** : la colonne vertébrale d'une bibliothèque cyber. Les cours spécialisés (CTI, forensic, AD, cloud, web, malware…) approfondissent ensuite chaque territoire que cette carte permet de situer.
>
> *« Comprendre les familles, c'est comprendre les attaques qu'on n'a jamais vues. »*
