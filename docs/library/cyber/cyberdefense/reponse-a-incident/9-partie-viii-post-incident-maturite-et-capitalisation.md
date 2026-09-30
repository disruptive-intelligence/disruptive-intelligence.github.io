---
title: PARTIE VIII — POST-INCIDENT, MATURITÉ ET CAPITALISATION
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
chapter: 9
chapters: 9
---

*L'incident est clos techniquement. Le travail le plus important commence : capitaliser pour ne pas revivre la même chose. Cette partie conclut le cours avec le retex, les métriques de maturité, et un chapitre d'application synthétique.*

---

#### Chapitre 38 — Clôture de l'incident et retour d'expérience (RETEX)

##### 38.1 Quand considérer l'incident clos

Critères techniques : éradication validée (Ch.29), surveillance post-nettoyage terminée sans alerte, tous les systèmes en production. Critères métiers : activité revenue à la normale, backlog rattrapé. Critères administratifs : notifications effectuées (ANSSI, CNIL), plainte déposée, assureur informé, rapport final livré, actions résiduelles attribuées et suivies.

La clôture formelle est documentée : date, décideur, synthèse des résultats, et liste des actions résiduelles avec responsables et échéances.

##### 38.2 Le RETEX structuré

Le RETEX est mené 2 à 4 semaines après la clôture (assez proche pour que les mémoires soient fraîches, assez éloigné pour avoir le recul). Il implique toutes les parties prenantes (cellule technique, cellule exécutive, IT, métiers, communication, juridique). Il suit une structure en 5 parties.

**Chronologie factuelle** : reconstitution des événements sans interprétation ni jugement. « Le serveur FS01-Lyon a été redémarré à 23h30 par l'admin d'astreinte sans collecte forensic préalable. » Pas : « L'admin d'astreinte a commis une erreur en redémarrant le serveur. »

**Ce qui a fonctionné** : détection EDR efficace (l'alerte a déclenché la réponse), escalade rapide du SOC N2, mobilisation du PRIS dans les délais contractuels, décision de ne pas payer (justifiée par les sauvegardes intactes), communication maîtrisée.

**Ce qui n'a pas fonctionné** : signaux faibles manqués (3 alertes classées faux positifs en 5 semaines), IRP jamais testé, sauvegardes quotidiennes non segmentées, absence de MFA sur le VPN prestataire, logs M365 limités (E3), comptes de service avec droits DA, redémarrage de serveurs sans collecte, absence de NDR.

**Causes racines** (Root Cause Analysis) : pourquoi le phishing a-t-il réussi ? (pas de MFA sur le VPN du sous-traitant + pas de sandbox email sur les pièces jointes). Pourquoi l'attaquant a-t-il pu progresser ? (compte de service `svc_deploy` avec droits Domain Admin et mot de passe faible). Pourquoi l'exfiltration n'a-t-elle pas été détectée ? (pas de NDR, exfiltration via services cloud légitimes, pas de DLP sur les partages).

**Recommandations priorisées** : chaque recommandation est classée par impact, faisabilité, urgence, et budget.

##### 38.3 Culture du RETEX sans blâme

Le RETEX ne fonctionne que dans un environnement de sécurité psychologique. Les participants doivent pouvoir décrire leurs erreurs sans crainte de sanction. L'admin qui a redémarré les serveurs doit pouvoir dire « j'ai redémarré les serveurs parce que je pensais que c'était la bonne chose à faire et personne ne m'avait dit de ne pas le faire » — sans être blâmé. La culture du blâme tue le RETEX : les gens cachent leurs erreurs au lieu de les documenter, et les mêmes erreurs se reproduisent.

Le RETEX vise à améliorer le système, pas à punir les individus. La question n'est pas « qui a fait une erreur ? » mais « quel processus a permis que cette erreur soit possible, et comment le corriger ? »

##### 38.4 Fil rouge — BLACKTIDE : le RETEX final

> **🔍 BLACKTIDE — Épisode 38 (conclusion du fil rouge)**
>
> Réunion RETEX le 11 avril 2026, 3 semaines après la clôture. Présents : Nadia (IR lead), Marc (RSSI), Thomas et Léa (PRIS CyberForce), Karim et Fatima (SOC), David (admin), le DPO, et un représentant de la direction générale.
>
> **15 recommandations validées :**
>
> | # | Recommandation | Priorité | Budget | Échéance |
> |---|---------------|----------|--------|----------|
> | 1 | Segmentation IT/OT physique (pare-feu dédié) | Critique | 150 K€ | J+30 |
> | 2 | Sauvegardes immuables (cloud WORM) | Critique | 80 K€/an | J+21 |
> | 3 | MFA sur tous les accès externes y compris prestataires | Critique | 30 K€ | J+14 |
> | 4 | Déploiement EDR 100 % du parc | Critique | 60 K€ | J+30 |
> | 5 | Exercice de crise annuel avec la direction | Haute | 25 K€/an | J+90 |
> | 6 | Upgrade M365 E5 (rétention logs étendue) | Haute | 200 K€/an | J+60 |
> | 7 | NDR déployé sur les segments critiques | Haute | 180 K€ | J+120 |
> | 8 | Tiering model AD (Tier 0/1/2 + PAW) | Haute | 250 K€ | J+180 |
> | 9 | Formation IR pour les admins d'astreinte | Haute | 15 K€ | J+45 |
> | 10 | Révision des comptes de service (suppression droits DA inutiles) | Haute | Interne | J+30 |
> | 11 | Sysmon déployé sur tout le parc | Moyenne | 40 K€ | J+90 |
> | 12 | Clause MFA obligatoire dans les contrats prestataires | Moyenne | Interne | J+60 |
> | 13 | DLP sur les partages de fichiers sensibles | Moyenne | 120 K€ | J+180 |
> | 14 | Playbooks IR mis à jour (AD compromis, OT, notification OIV) | Haute | Interne | J+30 |
> | 15 | Comptes break glass créés et sécurisés | Haute | 5 K€ | J+7 |
>
> Le conseil d'administration approuve un budget exceptionnel de 1,2 M€ pour le plan de durcissement, étalé sur 18 mois.

---

#### Chapitre 39 — Métriques, maturité et programme IR durable

##### 39.1 Métriques de performance IR

Les métriques clés pour évaluer et améliorer la capacité IR. Le **MTTD** (Mean Time To Detect) : délai entre la compromission initiale et la détection. Pour BLACKTIDE : 35 jours (l'infostealer est resté non détecté pendant 5 semaines) — un chiffre élevé qui révèle les failles de détection. Le **MTTC** (Mean Time To Contain) : délai entre la détection et le confinement effectif. Pour BLACKTIDE : environ 3 heures (de l'alerte EDR à la décision de confinement des 3 sites) — un chiffre honorable. Le **MTTR** (Mean Time To Recover) : délai entre le confinement et la reprise complète. Pour BLACKTIDE : 12 jours — un chiffre dans la norme pour un incident de cette ampleur.

Les métriques complémentaires incluent le taux de couverture EDR (92 % → objectif 100 %), la couverture des logs critiques (PowerShell logging activé sur les serveurs seulement → objectif : tout le parc), le pourcentage du parc sans Sysmon (100 % → objectif : 0 %), et la fréquence des exercices (1 tabletop en 18 mois → objectif : 1 tabletop trimestriel, 1 technique semestriel, 1 crise annuel).

##### 39.2 Modèle de maturité IR

5 niveaux de maturité pour auto-évaluation :

**Niveau 1 — Réactif ad hoc :** Pas de processus formalisé. L'équipe IT improvise quand un incident survient. Pas d'IRP, pas de playbooks, pas de PRIS sous contrat.

**Niveau 2 — Processus défini :** Un IRP existe, les rôles sont attribués, un PRIS est sous contrat. Mais l'IRP n'est pas testé, les playbooks sont incomplets, les logs sont partiels. C'est le niveau d'Arvantis avant BLACKTIDE.

**Niveau 3 — Outillage intégré :** EDR à 100 %, SIEM avec logs complets, playbooks testés, exercices réguliers, PRIS avec SLA validé. La capacité IR fonctionne en cas d'incident mais n'est pas proactive.

**Niveau 4 — Capacité proactive :** Threat hunting régulier, purple team, exercices de crise avec la direction, métriques suivies, amélioration continue post-incidents et post-exercices. C'est l'objectif d'Arvantis à 18 mois.

**Niveau 5 — Résilience systémique :** L'IR est intégré dans la culture de l'organisation. La direction participe activement aux exercices. Les boucles de rétroaction SOC → IR → CTI → Prévention fonctionnent. Le programme IR est budgété, staffé, et évalué annuellement.

##### 39.3 Construire un programme IR durable

Un programme IR durable repose sur une équipe dimensionnée et formée (formation continue SANS/GIAC, participation aux communautés FIRST/InterCERT), un budget pérenne (investissement initial + fonctionnement annuel — le budget IR ne doit pas être une ligne « exceptionnelle » supprimée l'année suivante), un outillage maintenu (EDR, SIEM, NDR, SOAR, outils forensic — mis à jour, calibrés, testés), des contrats à jour (PRIS, assurance, exercices), une astreinte organisée (rotation, compensation, formation des astreinteurs), un entraînement régulier (exercices progressifs, participation à des CTF, sessions de retex avec d'autres organisations), et une amélioration continue (chaque incident, chaque exercice, chaque retex alimente un plan de progrès suivi trimestriellement).

L'intégration des boucles de rétroaction entre disciplines est l'indicateur de maturité le plus avancé : le SOC alimente l'IR (détection → escalade), l'IR alimente le forensic (questions → investigation), le forensic alimente la CTI (artefacts → attribution → renseignement), la CTI alimente le SOC (IoC → règles de détection), et l'IR alimente la gestion de crise (situation technique → décisions stratégiques). Le programme IR durable organise ces boucles explicitement.

---

#### Chapitre 40 — Scénarios d'incident : atelier de synthèse

*Ce chapitre est conçu comme un atelier de synthèse — une mise en pratique transversale de toute la méthodologie IR enseignée dans le cours. Chaque scénario applique le processus complet : détection → qualification → investigation → confinement → éradication → reprise → RETEX. L'objectif n'est pas d'ajouter de la matière théorique nouvelle, mais de démontrer la polyvalence de la méthode sur des types d'incidents aux dynamiques distinctes.*

---

##### 40.1 Scénario 1 — Ransomware avec double extorsion (synthèse BLACKTIDE)

Synthèse intégrée du fil rouge, structurée comme un cas d'étude autonome avec les décisions clés à chaque étape. Focus sur les arbitrages spécifiques au ransomware : timing du confinement (course contre le chiffrement), gestion de la double extorsion (l'exfiltration est irréversible — payer ne la « dé-fait » pas), décision sur la rançon (tableau d'aide à la décision avec critères : sauvegardes disponibles ?, survie de l'entreprise en jeu ?, données irremplaçables ?, opérateur sanctionné ?), et reconstruction sans paiement (cercles de confiance, restauration depuis bandes).

##### 40.2 Scénario 2 — Compromission de messagerie (BEC)

Un directeur financier d'une ETI française reçoit un email de son CEO demandant un virement urgent de 2,3 M€ vers un compte à Hong Kong. L'email provient du vrai compte M365 du CEO — compromis par un phishing 3 jours plus tôt. L'investigation via les Unified Audit Logs révèle : connexion depuis une IP nigériane, création d'une règle de forwarding (tous les emails du CFO redirigés vers une boîte externe), et envoi de 12 emails frauduleux à des partenaires bancaires. Confinement : désactivation du compte CEO, révocation de tous les tokens, suppression de la règle de forwarding, alerte aux banques. L'investigation montre que le phishing initial a exploité une absence de MFA (le CEO avait refusé le MFA pour « raisons de praticité »). Le virement a été bloqué par la banque (procédure de confirmation téléphonique pour les virements internationaux > 500 K€). RETEX : MFA obligatoire pour tous, sans exception, y compris la direction.

##### 40.3 Scénario 3 — Exfiltration de données / espionnage

Une entreprise de biotechnologie française est alertée par un partenaire : des données de R&D confidentielles circulent sur un forum underground. L'investigation révèle un dwell time de 8 mois — un implant RAT installé via une clé USB trouvée dans le parking (social engineering physique). L'attaquant a exfiltré lentement (quelques centaines de Mo par semaine) via DNS tunneling, en dessous de tous les seuils d'alerte. L'AD n'est pas compromis (l'attaquant est resté avec des privilèges utilisateur standard sur un poste R&D). Confinement : isolation du poste, blocage du domaine de tunneling DNS. Le scénario illustre l'importance du NDR (le DNS tunneling aurait été détectable) et des règles DLP (l'accès massif aux fichiers R&D depuis un seul poste sur 8 mois aurait pu être alerté).

##### 40.4 Scénario 4 — Compromission supply chain

Un éditeur de logiciel de supervision industrielle publie une mise à jour contenant un implant malveillant (à la SolarWinds). L'implant est découvert 3 semaines après la mise à jour, quand un CERT sectoriel publie un advisory. 200 clients sont potentiellement touchés. L'investigation dans chaque organisation cliente doit déterminer : la mise à jour a-t-elle été installée ?, l'implant a-t-il été activé (communication C2 observée) ou est-il dormant ?, si activé, quelles actions l'attaquant a-t-il menées ? Le scénario illustre la complexité de l'IR supply chain : le périmètre est vaste (centaines de clients), la coordination avec l'éditeur est critique, et chaque client doit mener sa propre investigation.

##### 40.5 Scénario 5 — Insider threat

Un ingénieur R&D annonce sa démission pour rejoindre un concurrent. Après son départ, un audit DLP révèle : 50 Go de documentation technique copiée sur une clé USB dans les 2 semaines précédant le départ, et un upload de 15 Go vers un compte Google Drive personnel depuis le réseau d'entreprise. L'investigation forensic (analyse du poste, des logs DLP, des logs proxy) confirme les transferts. Le scénario illustre les spécificités de l'insider threat : les accès sont légitimes (pas de mouvement latéral classique), l'investigation est autant RH/juridique que technique, la gestion de la preuve doit être compatible avec une procédure disciplinaire ou pénale (vol de secrets de fabrication — article L.1227-1 du Code du travail et articles L.621-1 et suivants du Code de la propriété intellectuelle), et la communication interne est extrêmement sensible (pas de witch hunt, pas de rumeurs).

---


### ANNEXES

---

#### Annexe A — Glossaire

| Terme | Définition |
|-------|-----------|
| **ACL/DACL** | Access Control List / Discretionary ACL — permissions d'accès sur les objets Active Directory ou le système de fichiers |
| **Amcache** | Artefact Windows enregistrant l'historique des programmes exécutés avec leur hash SHA1 |
| **ASN** | Autonomous System Number — identifiant d'un réseau autonome, utile pour identifier l'hébergeur |
| **ATT&CK** | Framework MITRE décrivant les tactiques, techniques et procédures des attaquants |
| **Beaconing** | Pattern de communication périodique entre un malware et son serveur C2 |
| **BEC** | Business Email Compromise — fraude par compromission de messagerie professionnelle |
| **Blast radius** | Périmètre d'impact potentiel d'un incident — nombre de systèmes, utilisateurs, données touchés |
| **BloodHound** | Outil de cartographie des chemins d'attaque dans Active Directory |
| **Break glass account** | Compte d'administration d'urgence, non lié à l'AD principal, utilisable quand le SI est compromis |
| **C2** | Command and Control — infrastructure de commande utilisée par l'attaquant pour piloter le malware |
| **Cellule de crise** | Instance de gouvernance exécutive activée lors d'un incident majeur ou d'une crise |
| **CERT-FR** | Computer Emergency Response Team de l'ANSSI — centre de réponse aux incidents pour l'État français |
| **Chain of custody** | Chaîne de traçabilité des preuves, documentant chaque manipulation d'une preuve numérique |
| **Confinement** | Ensemble des mesures visant à stopper la progression de l'attaquant et limiter l'impact |
| **CSIRT** | Computer Security Incident Response Team — équipe de réponse aux incidents de sécurité |
| **DCSync** | Technique d'attaque AD permettant de simuler un DC pour récupérer les hashes NTLM de tous les comptes |
| **DGA** | Domain Generation Algorithm — algorithme générant des noms de domaine pseudo-aléatoires pour le C2 |
| **Dwell time** | Temps de séjour — durée entre la compromission initiale et la détection de l'incident |
| **EDR** | Endpoint Detection and Response — solution de détection et réponse sur les postes et serveurs |
| **Éradication** | Phase de l'IR consistant à supprimer tous les mécanismes de compromission et de persistence |
| **Event ID** | Identifiant numérique des événements dans les Windows Event Logs |
| **Fileless malware** | Malware s'exécutant uniquement en mémoire, sans écrire de fichier sur le disque |
| **FTK Imager** | Outil d'acquisition forensic pour la création d'images disque bit-à-bit |
| **Golden Ticket** | TGT Kerberos forgé avec le hash du compte krbtgt, donnant un accès illimité au domaine AD |
| **GPO** | Group Policy Object — objet de stratégie de groupe dans Active Directory |
| **IAB** | Initial Access Broker — acteur spécialisé dans la vente d'accès initiaux compromis |
| **IRP** | Incident Response Plan — plan de réponse à incident, document cadre de la capacité IR |
| **IoC** | Indicator of Compromise — indicateur technique de compromission (hash, domaine, IP) |
| **IoA** | Indicator of Attack — indicateur comportemental d'attaque (pattern de mouvement latéral, etc.) |
| **JA3/JA4** | Fingerprinting TLS — empreinte du client TLS permettant d'identifier des connexions suspectes |
| **KAPE** | Kroll Artifact Parser and Extractor — outil de collecte automatisée d'artefacts forensic Windows |
| **Kerberoasting** | Technique d'attaque AD consistant à demander des TGS pour craquer les mots de passe des comptes de service |
| **Kill Chain** | Modèle Lockheed Martin décrivant les 7 phases d'une cyber-attaque |
| **krbtgt** | Compte Active Directory utilisé pour le chiffrement des tickets Kerberos — sa compromission permet les Golden Tickets |
| **LAPS** | Local Administrator Password Solution — solution Microsoft de gestion des mots de passe admin locaux |
| **Lateral movement** | Mouvement latéral — progression de l'attaquant d'un système à un autre au sein du réseau |
| **Loader** | Malware de première étape qui télécharge et exécute le payload principal |
| **MFT** | Master File Table — table maîtresse du système de fichiers NTFS, enregistrant tous les fichiers et métadonnées |
| **MTTC** | Mean Time To Contain — délai moyen entre la détection et le confinement effectif |
| **MTTD** | Mean Time To Detect — délai moyen entre la compromission et la détection |
| **MTTR** | Mean Time To Recover — délai moyen entre le confinement et la reprise complète |
| **NDR** | Network Detection and Response — solution de détection et réponse sur le réseau |
| **NIS 2** | Directive européenne sur la sécurité des réseaux et des systèmes d'information, version 2 |
| **OIV** | Opérateur d'Importance Vitale — organisation identifiée par l'État français comme essentielle |
| **OPSEC** | Operational Security — pratiques de sécurité opérationnelle |
| **PAW** | Privileged Access Workstation — poste dédié et durci pour l'administration privilégiée |
| **Patient zéro** | Premier système compromis dans un incident — le point d'entrée initial de l'attaquant |
| **Playbook** | Document opérationnel décrivant les actions à mener pour un type d'incident spécifique |
| **Plaso** | Outil de création de Super Timeline à partir d'artefacts forensic multiples |
| **Prefetch** | Artefact Windows enregistrant l'historique des programmes exécutés |
| **PRIS** | Prestataires de Réponse aux Incidents de Sécurité — qualification ANSSI pour les prestataires IR |
| **PsExec** | Outil Sysinternals d'exécution de processus à distance — fréquemment utilisé pour le mouvement latéral |
| **RACI** | Responsible, Accountable, Consulted, Informed — matrice de responsabilité |
| **RaaS** | Ransomware-as-a-Service — modèle franchisé de distribution de ransomware |
| **RETEX** | Retour d'expérience — analyse post-incident structurée |
| **Scoping** | Délimitation du périmètre de compromission d'un incident |
| **ShimCache** | Artefact Windows (AppCompatCache) enregistrant les programmes exécutés |
| **SIEM** | Security Information and Event Management — plateforme de collecte et corrélation des logs |
| **SitRep** | Situation Report — rapport de situation périodique pendant un incident |
| **SPN** | Service Principal Name — identifiant de service dans Active Directory, cible du Kerberoasting |
| **SRUM** | System Resource Usage Monitor — artefact Windows enregistrant la consommation réseau par processus |
| **Tiering** | Modèle de séparation des niveaux d'administration AD (Tier 0/1/2) |
| **Timeline** | Chronologie reconstituée des événements d'un incident |
| **Triage** | Évaluation rapide initiale d'un incident pour déterminer sa nature et sa gravité |
| **TTP** | Tactics, Techniques, and Procedures — méthodes opérationnelles d'un attaquant |
| **UAL** | Unified Audit Log — journal d'audit unifié de Microsoft 365 |
| **USN Journal** | Update Sequence Number Journal — journal des modifications du système de fichiers NTFS |
| **Velociraptor** | Outil de collecte forensic et de threat hunting à grande échelle |
| **Volatility** | Framework open source d'analyse de mémoire vive (RAM) |
| **WORM** | Write Once Read Many — stockage immuable, résistant au ransomware |

---

#### Annexe B — Checklists opérationnelles

##### Checklist des 30 premières minutes

- [ ] Confirmer le vrai positif (exclure faux positif, maintenance planifiée)
- [ ] Identifier les systèmes visiblement impactés
- [ ] Évaluer la sévérité initiale (P1-P4)
- [ ] Augmenter le logging sur les systèmes suspects
- [ ] Sauvegarder les logs actuels (avant rotation)
- [ ] Activer la capture réseau si possible
- [ ] NE PAS redémarrer, NE PAS nettoyer, NE PAS modifier
- [ ] Escalader vers l'IR lead selon la chaîne d'escalade
- [ ] Ouvrir le canal de communication sécurisé (hors SI)
- [ ] Documenter les actions dans le journal d'incident

##### Checklist de confinement

- [ ] Décision de confinement validée par le RSSI ou l'IR lead
- [ ] Collecte forensic (RAM + triage) effectuée AVANT l'isolation
- [ ] Isolation réseau exécutée (EDR containment / VLAN / ACL pare-feu)
- [ ] Comptes compromis désactivés
- [ ] Tokens et sessions révoqués (M365, VPN, SSO)
- [ ] Sauvegardes protégées (déconnexion si sur le même réseau)
- [ ] Accès tiers compromis désactivés
- [ ] Communication au SOC : surveillance renforcée sur les IoC identifiés
- [ ] SitRep mis à jour avec le périmètre de confinement

##### Checklist de collecte forensic

- [ ] Acquisition mémoire (DumpIt/WinPmem) — AVANT tout redémarrage
- [ ] Hash SHA256 calculé immédiatement après acquisition
- [ ] Triage KAPE ou Velociraptor (artefacts Windows/Linux)
- [ ] Image disque si nécessaire (FTK Imager / dd)
- [ ] Chaîne de custody documentée (formulaire complété)
- [ ] Stockage sécurisé de la preuve (hors SI compromis)
- [ ] Sample malware isolé pour analyse (sandbox)

##### Checklist de validation post-éradication

- [ ] Scan EDR complet sur 100 % du parc
- [ ] Aucune tâche planifiée malveillante résiduelle
- [ ] Aucun service non répertorié
- [ ] Aucun compte non autorisé dans les groupes privilégiés
- [ ] Aucune GPO non légitime
- [ ] Aucune règle de forwarding email non légitime
- [ ] Aucun flux réseau vers les C2 identifiés
- [ ] Audit AD (PingCastle / Purple Knight) passé
- [ ] Threat hunting ciblé en cours (4 semaines minimum)

##### Checklist de clôture

- [ ] Éradication validée (surveillance post sans alerte)
- [ ] Tous les systèmes en production
- [ ] Notifications effectuées (ANSSI, CNIL, assureur)
- [ ] Plainte déposée
- [ ] Rapport d'incident final livré
- [ ] Actions résiduelles attribuées avec responsables et échéances
- [ ] RETEX planifié (J+14 à J+28 après clôture)
- [ ] Journal d'incident archivé

---

#### Annexe C — Templates de documents IR

##### Template SitRep

```
SITREP #[N] — [NOM OPÉRATION] — [DATE HEURE]
Classification : [INTERNE / CONFIDENTIEL]

1. CE QU'ON SAIT (faits confirmés)
   - ...

2. CE QU'ON NE SAIT PAS (inconnues explicites)
   - ...

3. CE QU'ON FAIT (actions en cours)
   - ...

4. CE QU'ON ENVISAGE (prochaines étapes, options)
   - ...

5. CE DONT ON A BESOIN (ressources, décisions, autorisations)
   - ...

6. PROCHAINE ÉCHÉANCE : [date/heure]

Rédigé par : [nom]    Validé par : [nom]
```

##### Template journal d'incident

```
JOURNAL D'INCIDENT — [NOM OPÉRATION]
Ouvert le : [date heure]    IR Lead : [nom]

| Date/Heure | Auteur | Action / Observation / Décision | Source | Impact |
|-----------|--------|-------------------------------|--------|--------|
| JJ/MM HH:MM | [nom] | [description] | [source] | [impact] |
```

##### Template notification CNIL (72h)

```
NOTIFICATION DE VIOLATION DE DONNÉES PERSONNELLES
(Article 33 du RGPD)

1. NATURE DE LA VIOLATION
   Type : [confidentialité / intégrité / disponibilité]
   Description : [description factuelle]
   Date de prise de connaissance : [date]

2. CATÉGORIES DE DONNÉES CONCERNÉES
   [données d'identification, données financières, données de santé, etc.]

3. CATÉGORIES ET NOMBRE DE PERSONNES CONCERNÉES
   [nombre estimé]    [catégories : employés, clients, partenaires]

4. CONSÉQUENCES PROBABLES
   [risque d'usurpation d'identité, risque financier, etc.]

5. MESURES PRISES OU PROPOSÉES
   [mesures de confinement, d'éradication, de notification aux personnes]

6. COORDONNÉES DU DPO
   [nom, email, téléphone]
```

---

#### Annexe D — Cheat sheets techniques

##### Event IDs Windows critiques pour l'IR

| Event ID | Source | Signification IR |
|----------|--------|-----------------|
| 4624 | Security | Authentification réussie — types de logon : 2 (interactif), 3 (réseau), 10 (RDP) |
| 4625 | Security | Authentification échouée — volume élevé = brute force ou password spraying |
| 4648 | Security | Logon avec credentials explicites — indicateur de mouvement latéral |
| 4672 | Security | Attribution de privilèges spéciaux — accès administrateur |
| 4688 | Security | Création de processus — nécessite l'activation de la ligne de commande |
| 4698 | Security | Création de tâche planifiée — mécanisme de persistence fréquent |
| 4720 | Security | Création de compte — activité de backdoor account |
| 4728/4732 | Security | Ajout de membre à un groupe de sécurité global/local |
| 4769 | Security | Demande de TGS Kerberos — encryption type 0x17 (RC4) = Kerberoasting |
| 4662 | Security | Opération sur objet AD — avec GUID de réplication = DCSync |
| 5136 | Security | Modification d'objet DS — modification de GPO ou d'attribut AD |
| 5140/5145 | Security | Accès à un partage réseau / vérification d'accès à un fichier partagé |
| 7045 | System | Installation de service — mécanisme de persistence |
| 4103 | PowerShell | Module logging — modules PowerShell chargés |
| 4104 | PowerShell | Script block logging — contenu des scripts PowerShell exécutés |

##### Commandes Volatility 3 essentielles

```bash
# Lister les processus
python3 vol.py -f dump.raw windows.pslist
python3 vol.py -f dump.raw windows.pstree

# Connexions réseau actives
python3 vol.py -f dump.raw windows.netscan

# DLL chargées par un processus
python3 vol.py -f dump.raw windows.dlllist --pid [PID]

# Détection d'injection de code
python3 vol.py -f dump.raw windows.malfind

# Ligne de commande des processus
python3 vol.py -f dump.raw windows.cmdline

# Extraction des hashes
python3 vol.py -f dump.raw windows.hashdump

# Handles de fichiers/registre
python3 vol.py -f dump.raw windows.handles --pid [PID]
```

##### Commandes KAPE essentielles

```bash
# Triage complet Windows (tous les artefacts principaux)
kape.exe --tsource C: --tdest E:\KAPE_Output --tflush
  --target KapeTriage

# Collecte ciblée Event Logs + Prefetch + Amcache
kape.exe --tsource C: --tdest E:\KAPE_Output
  --target EventLogs,Prefetch,Amcache

# Collecte + parsing automatique
kape.exe --tsource C: --tdest E:\KAPE_Output
  --target KapeTriage --mdest E:\KAPE_Parsed
  --module !EZParser
```

---

#### Annexe E — Playbooks types détaillés

Les playbooks complets sont structurés selon le format du Ch.7 : trigger, actions immédiates (0-15 min), actions d'investigation (15 min-4h), actions de confinement, critères d'escalade, communication, et clôture. Pour des raisons de volume, seuls les éléments clés de chaque playbook sont listés ici. Les versions complètes, avec les commandes exactes par outil (Splunk, CrowdStrike, Sentinel, Velociraptor), doivent être adaptées à l'environnement spécifique de chaque organisation.

##### Playbook Ransomware — Éléments clés

**Trigger :** Détection EDR (chiffrement de fichiers, exécution de binaire suspect), ou découverte de fichiers chiffrés / note de rançon.

**Actions immédiates (0-15 min) :** Ne PAS éteindre les machines. Isoler via EDR (network containment). Protéger les sauvegardes (déconnexion physique immédiate du NAS réseau). Alerter l'IR lead.

**Actions critiques :** Identifier le variant (note de rançon, extension des fichiers, hash du binaire). Évaluer l'étendue du chiffrement (combien de machines, quel pourcentage du parc). Vérifier l'intégrité des sauvegardes (sont-elles chiffrées ? antérieures à la compromission ?). Vérifier la compromission de l'AD (DCSync ? krbtgt ?). Estimer l'exfiltration (double extorsion ?).

**Escalade :** P1 automatique si plus de 10 machines chiffrées OU si un DC est compromis OU si les sauvegardes sont touchées.

##### Playbook Compromission de compte — Éléments clés

**Trigger :** Alerte SIEM (geo-impossible travel, connexion depuis IP suspecte, activité anormale), ou signalement utilisateur.

**Actions immédiates :** Désactiver le compte. Révoquer toutes les sessions actives et refresh tokens. Reset du mot de passe.

**Investigation :** Revue de l'activité du compte sur les 30 derniers jours (Sign-in Logs, UAL). Recherche de règles de forwarding email. Recherche de consentements OAuth suspects. Vérification : le phishing initial a-t-il touché d'autres utilisateurs ?

##### Playbook Exfiltration — Éléments clés

**Trigger :** Alerte DLP, volume anormal de trafic sortant, notification externe (données trouvées sur un forum).

**Actions immédiates :** Identifier le canal d'exfiltration (destination, protocole, outil). Bloquer le canal si identifié.

**Investigation :** Identifier les données exfiltrées (quels partages accédés, quels fichiers, quel volume). Identifier la source (quelle machine, quel compte). Remonter au point d'entrée.

**Notification :** CNIL sous 72h si données personnelles.

---

#### Annexe F — Tableau d'outils de référence IR

| Catégorie | Outil | Gratuit/Payant | Usage | Limites |
|-----------|-------|---------------|-------|---------|
| **EDR** | CrowdStrike Falcon | Payant | Détection, containment, telemetry | Coût élevé, nécessite agent |
| **EDR** | Microsoft Defender for Endpoint | Payant (inclus E5) | Détection, containment, intégration M365 | Nécessite licence E5 pour full feature |
| **EDR** | SentinelOne | Payant | Détection, containment, rollback ransomware | Coût élevé |
| **SIEM** | Splunk Enterprise | Payant | Corrélation logs, investigation, dashboards | Coût de licence basé sur le volume |
| **SIEM** | Microsoft Sentinel | Payant (cloud) | Corrélation, intégration Azure/M365 | Coût variable selon ingestion |
| **SIEM** | Elastic Security (ELK) | Gratuit (OSS) / Payant (cloud) | Corrélation, flexible, extensible | Expertise nécessaire pour déploiement |
| **NDR** | Vectra AI | Payant | Détection réseau, beaconing, mouvement latéral | Coût élevé |
| **NDR** | Zeek (ex-Bro) | Gratuit (OSS) | Analyse de trafic réseau, génération de logs | Nécessite expertise, pas de GUI |
| **Forensic** | KAPE | Gratuit | Collecte automatisée d'artefacts Windows | Windows uniquement |
| **Forensic** | Velociraptor | Gratuit (OSS) | Collecte à grande échelle, hunting | Courbe d'apprentissage |
| **Forensic** | FTK Imager | Gratuit | Image disque bit-à-bit | Interface vieillissante |
| **Forensic** | Autopsy | Gratuit (OSS) | Analyse forensic complète | Performances variables |
| **Mémoire** | Volatility 3 | Gratuit (OSS) | Analyse de dumps mémoire | Nécessite expertise, plugins limités |
| **Mémoire** | DumpIt (Comae) | Gratuit | Acquisition mémoire Windows rapide | Windows uniquement |
| **Timeline** | Plaso (log2timeline) | Gratuit (OSS) | Super Timeline à partir d'artefacts multiples | Lent sur gros volumes |
| **Timeline** | Timesketch | Gratuit (OSS) | Visualisation collaborative de timelines | Nécessite infrastructure |
| **Malware** | ANY.RUN | Freemium | Sandbox interactive en ligne | Échantillons publics en version gratuite |
| **Malware** | Joe Sandbox | Payant | Sandbox automatisée, analyse approfondie | Coût |
| **Malware** | VirusTotal | Freemium | Multi-scanner, intelligence, relations | Échantillons partagés avec la communauté |
| **AD Audit** | PingCastle | Gratuit (usage interne) | Score de sécurité AD, recommandations | Ne couvre pas tout ATT&CK |
| **AD Audit** | Purple Knight (Semperis) | Gratuit | Audit AD automatisé, détection faiblesses | Rapport parfois verbeux |
| **AD Audit** | BloodHound | Gratuit (OSS) | Cartographie des chemins d'attaque AD | Nécessite collecte SharpHound |
| **SOAR** | Cortex XSOAR (Palo Alto) | Payant | Orchestration, playbooks automatisés | Coût, complexité |
| **SOAR** | Shuffle | Gratuit (OSS) | Orchestration, playbooks | Moins mature que XSOAR |
| **Cloud** | Hawk (PowerShell) | Gratuit (OSS) | Investigation M365 / Entra ID | Limité à l'écosystème Microsoft |

---

#### Annexe G — Grilles d'évaluation et RACI

##### Grille de gravité des incidents

| Niveau | Critères techniques | Critères métier | Exemples |
|--------|-------------------|----------------|----------|
| **P4 — Mineur** | 1-2 postes impactés, malware isolé, pas de mouvement latéral | Pas d'impact production, pas de données sensibles | Phishing bloqué, PUA détecté, malware contenu par AV |
| **P3 — Significatif** | Compromission confirmée sur quelques systèmes, mouvement latéral limité | Impact limité sur un service non critique | Compromission d'un compte utilisateur, malware avec C2 actif sur 2-3 postes |
| **P2 — Majeur** | Compromission de serveurs critiques, mouvement latéral étendu, exfiltration possible | Impact sur un service critique, données sensibles potentiellement exposées | Compromission de serveur de fichiers, accès admin non autorisé, exfiltration détectée |
| **P1 — Critique** | Compromission AD (DC, krbtgt), ransomware déployé, exfiltration massive | Production arrêtée, données sensibles confirmées exfiltrées, site OIV impacté | Ransomware à grande échelle, Golden Ticket, exfiltration R&D/RH |

##### Grille de décision de confinement

| Situation | Confinement immédiat ? | Observation contrôlée possible ? | Critère de décision |
|-----------|----------------------|-------------------------------|-------------------|
| Ransomware en cours de déploiement | **OUI — immédiat** | NON | Chaque minute = machines chiffrées |
| Espionnage discret (attaquant non alerté) | Différé possible | **OUI — si l'attaquant ne sait pas** | Comprendre l'étendue avant de couper |
| Compromission de compte sans activité destructrice | **OUI — désactivation du compte** | NON | L'impact est limité et réversible |
| Exfiltration en cours | **OUI — blocage du canal** | Éventuellement, si plusieurs canaux suspectés | Arrêter la fuite est prioritaire |
| Compromission OT avec risque physique | **OUI — isolation IT/OT** | NON | La sécurité physique prime |

##### Matrice RACI type — Réponse à incident

| Action | SOC | IR Lead | Forensic | RSSI | DSI | DG | Juridique | Communication | DPO |
|--------|-----|---------|----------|------|-----|-----|-----------|--------------|-----|
| Détection et escalade | **R** | I | | I | | | | | |
| Classification et triage | C | **R/A** | C | I | | | | | |
| Décision de confinement | | **R** | C | **A** | I | I | | | |
| Collecte forensic | | C | **R** | I | | | | | |
| Investigation technique | | **A** | **R** | I | C | | | | |
| Notification ANSSI | | C | | **R/A** | | I | C | | |
| Notification CNIL | | C | | C | | I | C | | **R/A** |
| Communication interne | | I | | C | C | **A** | C | **R** | |
| Communication externe | | I | | C | | **A** | C | **R** | |
| Décision rançon | | C | | C | C | **A** | **R** | C | |
| Dépôt de plainte | | C | C | C | | I | **R/A** | | |
| RETEX | C | **R** | C | **A** | C | I | I | I | I |

R = Responsible (exécute), A = Accountable (valide), C = Consulted, I = Informed.

---

---


## Annexe — Questions types d'entretien et réponses types


### Questions essentielles

- **Question :** Quelles sont les grandes phases de la réponse à incident ?
  - **Réponse type :** Le NIST 800-61 définit 4 phases : Préparation (avant l'incident — playbooks, outillage, exercices), Détection et Analyse (du signal faible à l'incident confirmé, triage, scoping), Confinement-Éradication-Restauration (isoler, nettoyer, reconstruire), et Post-Incident (retex, amélioration). En réalité, ces phases ne sont pas linéaires — on investigue pendant qu'on contient, on découvre de nouvelles compromissions pendant l'éradication. C'est itératif et parallèle.

- **Question :** Quelle est la différence entre un événement, une alerte, un incident et une crise ?
  - **Réponse type :** Un événement c'est tout fait observable dans le SI — il y en a des milliards par jour. Une alerte c'est un événement signalé comme potentiellement anormal par un système de détection. Un incident c'est une alerte confirmée qui compromet effectivement la confidentialité, l'intégrité ou la disponibilité. Une crise c'est un incident dont l'impact dépasse la capacité de réponse normale et nécessite une gouvernance exécutive. Ces distinctions déterminent le niveau de mobilisation, les processus activés, et les obligations de notification.

- **Question :** Un ransomware est en cours de déploiement — que faites-vous en priorité ?
  - **Réponse type :** Confinement immédiat. Chaque minute qui passe c'est des machines supplémentaires chiffrées. On isole les segments réseau touchés — on coupe la connectivité mais on n'éteint PAS les machines pour préserver la mémoire (qui contient les clés de chiffrement et les artefacts forensic). On désactive les comptes compromis. On protège les sauvegardes — si elles sont accessibles par les mêmes credentials, c'est la priorité absolue. En parallèle, on commence le scoping : l'attaquant est-il ailleurs dans le réseau ?

- **Question :** Pourquoi la préparation est-elle si importante en IR ?
  - **Réponse type :** Parce que le jour de l'incident, il est trop tard pour construire les processus. La préparation détermine tout : est-ce qu'on a un IRP avec des playbooks par type d'incident ? Est-ce qu'on a la télémétrie nécessaire pour investiguer ? Est-ce qu'on sait qui appeler à 2h du matin ? Est-ce qu'on a un contrat avec un prestataire PRIS ? Est-ce qu'on a testé la restauration des sauvegardes ? Une organisation préparée contient un ransomware en quelques heures. Une organisation non préparée met des semaines et paie souvent la rançon.

- **Question :** Comment construisez-vous une timeline d'attaque ?
  - **Réponse type :** La timeline reconstitue chronologiquement toutes les actions de l'attaquant. On croise plusieurs sources : les logs EDR/Sysmon (processus, connexions), les Event Logs Windows (4624 logons, 4698 scheduled tasks), les logs d'authentification AD, les logs proxy/DNS, et les artefacts forensic (prefetch, amcache, MFT). On cherche le point d'entrée initial, les pivots, les escalades de privilèges, les persistances, et les actions sur objectif. La timeline est le livrable central de l'investigation.


### Questions complémentaires

- **Question :** Quand décidez-vous de confiner immédiatement vs observer ?
  - **Réponse type :** Confinement immédiat si l'impact est destructif (ransomware en cours, exfiltration active, risque OT). Observation contrôlée si l'attaquant est discret et ne sait pas qu'il est détecté — ça permet de comprendre l'étendue avant de couper, et d'identifier tous les mécanismes de persistence. Mais cette décision est un arbitrage : observer c'est prendre le risque que l'attaquant accélère. En cas de doute, le confinement prime — surtout s'il y a un risque physique (OT) ou des données sensibles en jeu.

- **Question :** Quels sont les cadres méthodologiques IR que vous connaissez ?
  - **Réponse type :** Les deux principaux sont le NIST SP 800-61 (4 phases : Préparation, Détection-Analyse, Confinement-Éradication-Restauration, Post-Incident) et le SANS PICERL (6 phases : Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned). En France, on a aussi le cadre ANSSI/CERT-FR et le référentiel PRIS pour la qualification des prestataires d'IR. En parallèle, MITRE ATT&CK est utilisé comme grille de lecture pour mapper les TTP observées.

- **Question :** Qu'est-ce qu'un RETEX et pourquoi c'est essentiel ?
  - **Réponse type :** Le RETEX (retour d'expérience) est l'analyse post-incident : timeline complète, vecteur initial, chemins d'escalade, persistence, ce qui a fonctionné et ce qui a échoué, et les recommandations d'amélioration. C'est essentiel parce que sans RETEX, on ne corrige pas les causes racines et on revit le même incident. Un bon RETEX produit des actions concrètes priorisées — pas juste un rapport technique, mais un plan d'amélioration avec des responsables et des délais.


### Questions les plus probables en entretien

1. Phases de la réponse à incident ?
2. Événement vs alerte vs incident vs crise ?
3. Ransomware en cours : premières actions ?
4. Pourquoi la préparation est critique ?
5. Comment construire une timeline d'attaque ?
6. Confiner immédiatement ou observer ?


### Réponses flash

- **Phases NIST** → Préparation → Détection/Analyse → Confinement/Éradication/Restauration → Post-Incident. Itératif, pas linéaire.
- **Échelle** → Événement (fait brut) → Alerte (signalé anormal) → Incident (confirmé) → Crise (dépasse la capacité normale).
- **Ransomware** → Confiner immédiatement, ne PAS éteindre (préserver mémoire), protéger les sauvegardes, désactiver comptes compromis, scoper.
- **Préparation** → IRP, playbooks, télémétrie, contrat PRIS, exercices, test de restauration. Le jour J c'est trop tard.
- **Timeline** → Croiser EDR + Event Logs + proxy/DNS + artefacts forensic. Point d'entrée → pivots → persistence → actions sur objectif.
- **Confinement vs observation** → Destructif/exfiltration = confinement immédiat. Espionnage discret = observation possible si l'attaquant ne sait pas. Doute = confiner.
- **RETEX** → Timeline + causes racines + ce qui a marché/échoué + plan d'amélioration priorisé.

---

> **Note de clôture**
>
> Ce cours a été conçu pour former à l'orchestration de la réponse à incident — la capacité de piloter une investigation, coordonner des acteurs hétérogènes, prendre des décisions sous pression, et ramener une organisation à un état de fonctionnement sûr.
>
> L'incident BLACKTIDE qui traverse les 38 premiers chapitres n'est pas un cas exceptionnel. C'est un incident représentatif de ce que vivent des centaines d'organisations chaque année : un phishing sur un sous-traitant, un infostealer qui vole des credentials VPN, un mouvement latéral progressif, un ransomware déployé un vendredi soir. Les montants, les noms et les circonstances sont fictifs, mais chaque décision, chaque tension, chaque erreur décrite dans le fil rouge est tirée de la réalité opérationnelle d'incidents réels.
>
> La réponse à incident n'est pas un exercice théorique. C'est une discipline qui se prépare (Partie II), se pratique en exercice (Ch.10), et s'améliore par le retour d'expérience (Ch.38). Le jour où l'incident arrive — et il arrivera —, ce qui fait la différence n'est pas la chance, c'est la préparation.
>
> *Préparer • Détecter • Qualifier • Investiguer • Contenir • Éradiquer • Restaurer • Capitaliser — avec méthode, rigueur et sang-froid.*
