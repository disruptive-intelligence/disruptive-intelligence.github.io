---
title: PARTIE VI — ÉRADICATION, RECONSTRUCTION ET REPRISE
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
chapter: 7
chapters: 9
---

*L'attaquant est identifié, le périmètre est connu, les mécanismes de persistance sont cartographiés. Il faut éradiquer, reconstruire, valider, et reprendre — sans réintroduire la compromission.*

---

### Chapitre 27 — Plan d'éradication coordonné

#### 27.1 Éradication simultanée, pas séquentielle

Si l'éradication est menée machine par machine, l'attaquant réinfecte les machines nettoyées depuis les machines non encore traitées. Le plan d'éradication doit être coordonné : un « jour J » est planifié (typiquement quelques jours après la fin de l'investigation, le temps de préparer toutes les actions), et toutes les mesures d'éradication sont exécutées simultanément dans une fenêtre courte (4 à 8 heures).

Le plan d'éradication liste exhaustivement toutes les actions à mener, l'ordre d'exécution (certaines actions dépendent d'autres — le double reset du krbtgt doit être fait avant le reset massif des comptes), les responsables de chaque action, et les validations post-exécution (comment vérifie-t-on que chaque action a réussi ?).

#### 27.2 Suppression des mécanismes de persistance

Pour chaque mécanisme identifié au Ch.20 : suppression des tâches planifiées malveillantes (vérification sur tout le parc via Velociraptor ou GPO de nettoyage), désinstallation des services Windows parasites (identification par nom, chemin, et hash), nettoyage des clés de registre Run/RunOnce, suppression des comptes créés par l'attaquant (après documentation — les comptes sont une preuve), retrait de la GPO malveillante (suppression complète, pas simple désactivation), suppression des règles de forwarding email (vérification de toutes les boîtes mail du domaine, pas seulement celles identifiées), révocation de tous les tokens cloud (M365, Azure, AWS — forcer une réauthentification complète), retrait des clés SSH non autorisées (vérification de tous les serveurs Linux), et correction des ACL/DACL modifiées sur l'AD (retour aux permissions d'origine, documentées).

#### 27.3 Le cas du krbtgt compromis

Quand le hash du krbtgt est compromis (DCSync confirmé), l'attaquant peut forger des Golden Tickets — des TGT qui ne seront pas invalidés par un simple reset des mots de passe utilisateurs. Le seul remède est le **double reset du krbtgt** : deux resets du mot de passe du compte krbtgt espacés de 12 heures minimum.

Pourquoi deux resets ? Kerberos retient les 2 derniers mots de passe du krbtgt (pour permettre la transition sans interruption de service). Un seul reset invalide le mot de passe N-1 mais les tickets forgés avec le mot de passe N (celui que l'attaquant connaît) restent valides tant que N est l'un des 2 derniers mots de passe. Le second reset pousse N en position N-2 (plus retenu par Kerberos), invalidant tous les Golden Tickets.

Procédure : premier reset du krbtgt à T0, vérification du fonctionnement de l'authentification Kerberos (les perturbations sont normalement limitées mais possibles — surveiller les tickets de service), second reset à T0+12h minimum (certaines recommandations préconisent T0+24h pour plus de sécurité), re-vérification du fonctionnement.

Le double reset du krbtgt impacte le fonctionnement de Kerberos pendant la transition — tous les TGT en circulation deviennent invalides et doivent être renouvelés. L'impact est généralement transparent (les systèmes renouvellent automatiquement) mais peut causer des dysfonctionnements sur les systèmes legacy ou mal configurés. Le reset doit être planifié dans la fenêtre d'éradication avec une surveillance active des dysfonctionnements.

#### 27.4 Fil rouge — BLACKTIDE : le jour J

> **🔍 BLACKTIDE — Épisode 27**
>
> Le « jour J » est planifié pour le mercredi 19 mars, de 22h à 04h (fenêtre de maintenance). L'équipe est constituée de 4 analystes internes + 2 consultants PRIS + 3 admins système.
>
> Séquence d'éradication :
> 1. 22h00 : Premier reset du krbtgt sur DC01.
> 2. 22h15 : Suppression des 3 comptes admin cachés (svc_monitor01, svc_backup_ext, svc_audit_temp).
> 3. 22h30 : Suppression de la GPO « Windows Update Configuration ».
> 4. 22h45 : Nettoyage des scheduled tasks malveillantes sur les 40+ machines (via Velociraptor — exécution centralisée).
> 5. 23h00 : Correction des ACL sur l'OU des serveurs critiques (retrait du GenericAll de svc_deploy).
> 6. 23h15 : Révocation de tous les tokens M365 (forçage de réauthentification).
> 7. 23h30 : Désactivation du compte VPN `admin_rh_ext` (sous-traitant GestPaie).
> 8. 00h00 : Rotation de tous les mots de passe des comptes de service (25 comptes).
> 9. 10h00 (J+1) : Second reset du krbtgt (T0+12h).
> 10. 12h00 : Forçage du changement de mot de passe pour TOUS les comptes utilisateurs du domaine (12 000 comptes — communication préparée, helpdesk renforcé pour le lundi).

---

### Chapitre 28 — Reconstruction des systèmes

#### 28.1 Reconstruire plutôt que nettoyer

Le principe fondamental de la reconstruction post-incident : un système compromis ne peut jamais être « nettoyé » avec certitude absolue. Le nettoyage (suppression du malware visible, patchs, reset des configurations) laisse un doute résiduel — l'attaquant a pu installer un mécanisme de persistance non détecté par l'investigation (rootkit, firmware implant, backdoor dans un fichier système légitime). Le seul moyen fiable de garantir l'éradication est la reconstruction à partir de sources propres : images gold (images système de référence, maintenues à jour), sauvegardes vérifiées antérieures à la compromission, ou installation fraîche depuis les médias d'origine.

En pratique, la reconstruction complète de tout le parc est rarement réalisable (trop long, trop coûteux). L'approche courante est un mix : reconstruction des systèmes critiques (DC, serveurs d'infrastructure, serveurs sensibles), nettoyage vérifié des systèmes moins critiques (postes de travail — réinstallation du poste si compromission confirmée, scan EDR approfondi sinon), et surveillance renforcée post-éradication (Ch.29) pour détecter une persistance non identifiée.

#### 28.2 Reconstruction par cercles de confiance

L'infrastructure est reconstruite en 3 cercles concentriques. Le **cercle 1 (noyau de confiance)** comprend les DC, le DNS interne, la PKI, l'infrastructure de sécurité (EDR console, SIEM, serveur de logs). Ces systèmes sont reconstruits en premier, à partir d'images gold, sur un réseau isolé. Ils forment le « noyau dur » à partir duquel le reste est déployé. Le **cercle 2 (services critiques)** comprend les serveurs de fichiers, la messagerie, les applications métier essentielles, le VPN, les portails clients. Ils sont reconstruits ou restaurés une fois le cercle 1 validé. Le **cercle 3 (reste du parc)** comprend les postes de travail, les services secondaires, les applications non critiques. Chaque cercle n'est reconnecté au réseau de production qu'après vérification complète du cercle précédent.

#### 28.3 Restauration des données

La restauration des données (à distinguer de la reconstruction des systèmes) pose des questions spécifiques. Les sauvegardes sont-elles intactes ? (si elles sont chiffrées par le ransomware, elles sont inutilisables). Sont-elles antérieures à la compromission ? (attention au dwell time — si la compromission a commencé il y a 5 semaines et que les sauvegardes ont 4 semaines, elles contiennent potentiellement le malware ou des backdoors). Contiennent-elles des données exploitables ? (une sauvegarde de données utilisateur est différente d'une sauvegarde d'image système — restaurer les données sur un système reconstruit proprement est la bonne approche, restaurer une image système potentiellement compromise est la mauvaise).

Stratégie recommandée : restaurer les DONNÉES sur des SYSTÈMES reconstruits proprement (pas les images système depuis des sauvegardes qui pourraient être compromises). Vérifier l'intégrité des données restaurées (scan EDR, recherche d'artefacts malveillants).

#### 28.4 Fil rouge — BLACKTIDE : la reconstruction

> **🔍 BLACKTIDE — Épisode 28**
>
> La reconstruction suit le modèle par cercles de confiance.
>
> **Cercle 1 (J+5 à J+7) :** 3 DC reconstruits à partir d'images gold Windows Server 2022, durcis selon les recommandations CIS Benchmark. L'AD est nettoyé en profondeur (option a du Ch.28 — pas de reconstruction complète, car la compromission est bien délimitée après le double reset krbtgt et la suppression des comptes/GPO/ACL). SIEM Splunk vérifié. Console EDR CrowdStrike vérifiée.
>
> **Cercle 2 (J+7 à J+10) :** Serveurs de fichiers reconstruits (installation fraîche Windows Server 2022). Données restaurées depuis les sauvegardes hebdomadaires sur bandes offline — intactes, mais avec 6 jours de perte de données (les sauvegardes quotidiennes sur NAS réseau sont partiellement chiffrées — inutilisables). Messagerie Microsoft 365 : tokens révoqués, conditional access policies renforcées, règles de forwarding malveillantes supprimées.
>
> **Cercle 3 (J+10 à J+12) :** Postes de travail des 3 sites impactés : les postes confirmés compromis (12 machines) sont réinstallés. Les autres subissent un scan EDR approfondi et un reset de l'utilisateur local admin (LAPS activé à cette occasion).

---

### Chapitre 29 — Validation d'éradication et surveillance post-nettoyage

#### 29.1 Comment savoir qu'on a vraiment éradiqué

L'éradication n'est pas un acte ponctuel (« on a supprimé le malware, c'est fini ») mais un processus qui se valide dans la durée. La question « l'attaquant est-il vraiment parti ? » ne peut jamais recevoir une réponse avec certitude absolue — mais la confiance se construit par accumulation de vérifications positives et absence de réapparition.

#### 29.2 Checklist de validation technique

Après l'éradication, une checklist de contrôle est exécutée sur l'ensemble du parc. Aucun processus malveillant actif (scan EDR complet — tous les endpoints, pas un échantillon). Aucune tâche planifiée non légitime (script de vérification exécuté via Velociraptor sur tout le parc). Aucun service Windows non répertorié. Aucun compte non autorisé dans les groupes privilégiés (audit AD complet). Aucune GPO non légitime (revue de toutes les GPO). Aucune règle de forwarding email non légitime (audit de toutes les boîtes mail M365). Aucun flux réseau vers les destinations C2 identifiées (monitoring continu proxy + pare-feu). Intégrité vérifiée des fichiers système critiques.

#### 29.3 Hunts post-nettoyage

Pendant 2 à 4 semaines après l'éradication, un threat hunting ciblé est mené en continu. Les hypothèses de hunting sont dérivées directement de l'attaque observée. « L'attaquant utilisait des scheduled tasks pour la persistence → chercher toute nouvelle scheduled task créée depuis le jour J. » « L'attaquant utilisait rclone pour l'exfiltration → chercher tout processus rclone ou tout flux vers S3/Blob/Cloud storage. » « L'attaquant avait un Golden Ticket → monitorer les anomalies Kerberos (TGT avec lifetime anormal, authentifications sans pré-authentification). »

Si le hunting révèle des traces, l'éradication est incomplète et le cycle recommence (investigation complémentaire → éradication complémentaire → validation).

#### 29.4 Seuil de confiance

Après 3 à 4 semaines de surveillance renforcée sans détection de réapparition, l'éradication est déclarée réussie avec un niveau de confiance « élevé — risque résiduel faible ». Ce seuil est documenté : il ne signifie pas « certitude absolue » mais « confiance suffisante pour un retour à la normale, avec un monitoring standard ». Le risque résiduel (un mécanisme de persistance non détecté, une porte d'entrée secondaire non identifiée) est accepté explicitement et géré par la surveillance continue.

#### 29.5 Fil rouge — BLACKTIDE : la validation

> **🔍 BLACKTIDE — Épisode 29**
>
> 3 semaines de surveillance renforcée post-éradication. Hunting quotidien sur les IoC PhantomCrypt (hash, domaines C2, patterns de beaconing). Monitoring continu des flux réseau vers les IP/domaines identifiés. Audit AD hebdomadaire via PingCastle (score passé de D à B après le durcissement). Scan EDR approfondi de tout le parc (100 % — y compris les 8 % auparavant non couverts, sur lesquels l'EDR a été déployé en urgence pendant l'incident).
>
> Résultat : aucun indicateur de réapparition après 3 semaines. Marc (RSSI) déclare l'éradication réussie avec un niveau de confiance « élevé ».

---

### Chapitre 30 — Reprise d'activité

#### 30.1 Priorisation des services

La reprise ne se fait pas en « big bang » — elle est progressive et priorisée en fonction de l'impact business. Les services critiques (messagerie, VPN pour le télétravail, systèmes de production industrielle, systèmes de paiement) reprennent en premier. Les services secondaires (applications RH, intranet, outils collaboratifs non essentiels) reprennent ensuite. Chaque service redémarré est validé fonctionnellement (le service fonctionne-t-il ?) et sécuritairement (aucun indicateur de compromission ?) avant le suivant.

#### 30.2 Critères de retour nominal

Le SI est considéré comme revenu à un état normal quand tous les systèmes sont opérationnels et les performances normales, les sauvegardes fonctionnent sur la nouvelle architecture immuable, la surveillance est revenue au niveau standard (plus de monitoring renforcé), aucune action résiduelle d'éradication n'est en cours, et les processus métiers fonctionnent sans workaround.

#### 30.3 Fil rouge — BLACKTIDE : la reprise progressive

> **🔍 BLACKTIDE — Épisode 30**
>
> La production reprend progressivement sur 12 jours (pas « lundi » comme le CEO le voulait).
> - J+5 : Messagerie M365 et VPN (12 000 utilisateurs retrouvent l'email et l'accès distant).
> - J+7 : Serveurs de fichiers restaurés (avec 6 jours de perte de données sur les bandes).
> - J+8 : Applications métier non critiques (ERP en lecture seule pour vérification).
> - J+10 : Production reprise sur les 12 sites non impactés (qui fonctionnaient en mode dégradé par précaution — interdiction des flux inter-sites levée).
> - J+12 : Production reprise sur les 3 sites impactés (Fos, Lyon, Cologne). Le site OIV de Fos est le dernier — la reprise est conditionnée à la validation conjointe ANSSI/Arvantis de l'intégrité du réseau SCADA.

---

### Chapitre 31 — Durcissement post-incident

#### 31.1 Quick wins (premières semaines)

Les quick wins sont les mesures de durcissement à impact élevé et à déploiement rapide, directement inspirées des failles exploitées pendant l'incident. Segmentation IT/OT renforcée avec pare-feu dédié (pas juste un VLAN taggé — un pare-feu physique entre le réseau IT et le réseau OT, avec filtrage applicatif). MFA obligatoire sur tous les accès externes (VPN, Microsoft 365, portails web) y compris les accès prestataires (la faille GestPaie ne se reproduira pas). LAPS (Local Administrator Password Solution) activé sur tout le parc Windows (mots de passe admin locaux uniques et rotatifs). PowerShell script block logging activé sur TOUS les postes (pas seulement les serveurs). Sauvegardes migrées vers un système immuable (stockage cloud avec MFA delete protection et versioning). Comptes break glass créés et stockés en coffre-fort physique. PingCastle exécuté mensuellement avec suivi du score.

#### 31.2 Plan structurel (mois suivants)

Les mesures structurelles nécessitent un investissement plus significatif. Tiering model AD (Tier 0 pour les DC et l'infrastructure de sécurité, Tier 1 pour les serveurs, Tier 2 pour les postes de travail — avec des comptes admin dédiés par tier, jamais réutilisés entre tiers). PAW (Privileged Access Workstations) pour les administrateurs Tier 0 (des postes dédiés, durcis, non utilisés pour la navigation ou la messagerie). Déploiement NDR pour la visibilité réseau. Upgrade licence M365 vers E5 (rétention UAL étendue). Sysmon déployé sur l'ensemble du parc Windows. Programme d'exercices de crise annuel avec la direction. Revue contractuelle des prestataires (clause MFA obligatoire pour les accès au SI).

---

### Chapitre 32 — Extorsion, rançon et arbitrages stratégiques

#### 32.1 Le paysage de l'extorsion en 2025-2026

L'extorsion cyber a considérablement évolué. La **simple extorsion** (chiffrement seul) est devenue rare — la plupart des victimes qui ont de bonnes sauvegardes refusent de payer. La **double extorsion** (chiffrement + menace de publication des données exfiltrées) est le standard depuis 2020 — même si la victime peut restaurer ses systèmes, la menace de publication de données sensibles crée une pression supplémentaire. La **triple extorsion** (chiffrement + publication + pression directe sur les clients, employés, ou partenaires de la victime) se développe — certains groupes contactent directement les clients de la victime pour les informer de la fuite, ou menacent les employés individuellement. Certains groupes abandonnent le chiffrement et ne pratiquent que l'exfiltration avec menace de publication (**pure data extortion**) — ce modèle nécessite moins de compétences techniques et génère des revenus significatifs.

#### 32.2 Payer ou ne pas payer : les arguments

**Arguments pour ne pas payer :** position de principe (ne pas financer le crime), pas de garantie que le déchiffreur fonctionnera, pas de garantie que les données ne seront pas publiées (les attaquants mentent), signal envoyé que l'organisation est une « bonne payeuse » (risque de reciblage), risque de sanctions OFAC/UE (si l'opérateur est sanctionné), et positionnement éthique (l'ANSSI et les autorités françaises recommandent de ne pas payer).

**Arguments pour payer :** quand les sauvegardes sont détruites et que l'activité ne peut pas reprendre autrement (survie de l'entreprise en jeu), quand des vies sont en danger (hôpital sans accès aux dossiers patients), quand le coût de la non-reprise dépasse significativement le montant de la rançon. Payer n'est pas illégal en France (ce n'est pas une interdiction légale mais une recommandation de l'ANSSI), mais c'est une décision stratégique avec des implications juridiques, éthiques et réputationnelles.

#### 32.3 Si la décision est de payer

Engagement d'un négociateur spécialisé (certains PRIS ou courtiers spécialisés offrent ce service — la négociation est un métier, pas une improvisation). Vérification de la liste des sanctions OFAC et de l'UE (payer une entité sanctionnée expose à des sanctions pénales). Négociation du montant (les rançons sont systématiquement négociables — des réductions de 40 à 60 % sont courantes). Test du déchiffreur sur un échantillon avant paiement complet. Documentation exhaustive pour l'assureur (si la police couvre la rançon — ce qui est de moins en moins fréquent en France depuis la loi LOPMI de 2023 qui conditionne le remboursement au dépôt de plainte dans les 72h).

#### 32.4 Gestion de la publication des données

Si la décision est de ne pas payer (ou si l'attaquant publie malgré le paiement), la publication des données sur le leak site est quasi certaine. L'organisation doit anticiper : monitoring du leak site pour détecter la publication dès qu'elle survient, communication proactive vers les personnes concernées (RGPD — notification aux personnes dont les données sont publiées), communication publique préparée (communiqué de presse factuel, validé juridiquement), et analyse des données publiées (quelles données exactement ? le volume correspond-il à l'exfiltration estimée ? y a-t-il des données de tiers ?).

#### 32.5 Fil rouge — BLACKTIDE : la rançon

> **🔍 BLACKTIDE — Épisode 32**
>
> PhantomCrypt demande 4,2 M€ en Bitcoin, avec un compte à rebours de 10 jours sur le portail de négociation. Le portail est professionnel : chat en direct, FAQ, démo de déchiffrement sur 3 fichiers gratuits.
>
> L'analyse de la direction : les sauvegardes offline (bandes) sont intactes — la production peut reprendre avec 6 jours de perte. Les données R&D exfiltrées (310 Go) seront publiées que la rançon soit payée ou non (pas de garantie de suppression). Les données RH (70 Go) seront publiées aussi. Le coût de la non-reprise est limité (les sauvegardes fonctionnent). Le coût réputationnel de la publication est réel mais gérable.
>
> **Décision : ne pas payer.** Documentée, signée par le CEO. Motifs : sauvegardes exploitables, pas de garantie sur les données, refus éthique de financer le crime. La rançon n'est pas couverte par l'assurance (exclusion contractuelle).
>
> J+10 : PhantomCrypt publie les données sur son leak site. Le DPO notifie les 8 000 employés dont les données RH sont concernées. L'image de marque est impactée — 3 articles dans la presse spécialisée, 1 article dans un quotidien national. Le cours de bourse d'Arvantis baisse de 2,3 % avant de se stabiliser.

---
