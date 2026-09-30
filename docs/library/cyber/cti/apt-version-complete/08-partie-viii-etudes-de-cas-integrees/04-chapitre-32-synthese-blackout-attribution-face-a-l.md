---
title: 'Chapitre 32 — Synthèse BLACKOUT : attribution face à l’incertitude'
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
up:
- - APT — version complète
  - ../index.md
- - Partie VIII — Études DE cas intégrées
  - index.md
---

Synthèse complète du fil rouge du cours — de la détection à la réponse, en passant par l’attribution, en un cas autonome intégré.

## 32.1 Rappel du contexte et des questions d’investigation

**L’opérateur** : distributeur d’énergie européen, 4 pays (France, Belgique, Allemagne, Pays-Bas), 6 200 collaborateurs, classé OIV en France, entité essentielle NIS 2. Infrastructure SCADA reliée à plusieurs dizaines de postes de transformation haute tension.

**L’incident** : détection le J+42 par le SOC d’un comportement anormal sur un poste d’ingénierie OT — rundll32 exécutant une DLL non signée + beaconing HTTPS régulier. Triage CERT rapide : profil APT, pas cybercrime.

**Les questions** :

- **QI-1** : Qui est l’attaquant ?
- **QI-2** : Depuis combien de temps est-il présent, et qu’a-t-il fait ?
- **QI-3** : Quelle est son intention (espionnage, sabotage à venir, pré-positionnement) ?
- **QI-4** : Comment l’éradiquer sans qu’il revienne ?
- **QI-5** : Comment communiquer et coordonner avec les autorités ?

## 32.2 Reconstitution de la timeline

L’investigation approfondie reconstitue la timeline complète.

**J0 (~42 jours avant détection)** : accès initial via exploitation de **CVE-2024-21887** sur un VPN Ivanti Connect Secure non patché. Le VPN est utilisé par des prestataires externes pour la maintenance des systèmes de supervision — sa compromission donne accès à des zones sensibles sans franchir beaucoup de contrôles internes.

**J+3** : persistence établie. DLL sideloading sur une application de supervision légitime (`SupervisionCenter.exe` charge `plugin_common.dll` — la DLL malveillante remplace la DLL légitime dans un répertoire où l’application regarde avant le répertoire système). Deux mécanismes de persistence additionnels créés : tâche planifiée déguisée en mise à jour système, service Windows modifié.

**J+5** : credential access. Mimikatz déployé en mémoire (sans dépôt sur disque), extraction des credentials LSASS. **Kerberoasting** contre plusieurs comptes de service avec SPN et mots de passe faibles — l’un des comptes crackés est un compte de service privilégié avec droits sur les serveurs de supervision.

**J+8** : mouvement latéral. PsExec utilisé pour pivoter depuis la DMZ vers les serveurs internes de supervision. Compromission d’un serveur historian.

**J+15** : pivot vers l’OT. Identification du poste d’ingénierie OT double-connecté (interface IT + interface SCADA). Compromission du poste via credentials admin locaux obtenus dans la phase précédente. DLL sideloading sur ce poste pour la persistence.

**J+15 à J+30** : reconnaissance OT. Consultation des documentations techniques, des schémas, des procédures. Identification des équipements contrôlés (automates Siemens S7-1500, protocole IEC 104 pour la télécommande des disjoncteurs dans les postes de transformation).

**J+30 à J+42** : dormance. L’attaquant ne fait presque rien pendant 12 jours. Simple maintenance de l’accès via beaconing régulier (27 min ± 3 min) vers un domaine hébergé derrière Cloudflare. Aucune action observable sur les automates.

**J+42 — détection** : l’EDR alerte sur le comportement `rundll32.exe` + DLL non signée + beaconing. Début de l’investigation.

## 32.3 Collecte des artefacts et mapping ATT&CK

Le CERT collecte méthodiquement les artefacts.

**Collecte** :

- **Logs Sysmon** sur les endpoints compromis (récupération complète depuis la rétention SIEM).
- **Event Logs AD** : authentifications, création de tickets Kerberos, accès aux ressources.
- **Captures réseau** pendant plusieurs jours post-détection (pour observer le beaconing).
- **Dump mémoire** du poste d’ingénierie OT (capture volatile avant redémarrage).
- **Artefacts disque** : persistence, DLL malveillantes, outputs de commandes exécutées.
- **Logs des appliances** : VPN Ivanti, firewalls, proxies.

**Mapping ATT&CK** :

- T1190 — Exploit Public-Facing Application (CVE-2024-21887 Ivanti).
- T1574.002 — DLL Side-Loading (persistence).
- T1003.001 — OS Credential Dumping: LSASS Memory (Mimikatz en mémoire).
- T1558.003 — Kerberoasting.
- T1021.002 — Remote Services: SMB/Windows Admin Shares (PsExec).
- T1071.001 — Application Layer Protocol: Web Protocols (C2 HTTPS).
- T1053.005 — Scheduled Task/Job: Scheduled Task (persistence additionnelle).
- T1543.003 — Create or Modify System Process: Windows Service (persistence).
- T1083 — File and Directory Discovery (reconnaissance OT).

Documentation structurée pour transmission aux autorités et à l’ISAC énergie européen.

## 32.4 Matrice ACH et attribution

Référence détaillée à l’Épisode 6 (Ch.24). Synthèse.

**H1 Sandworm** : confiance modérée. TTP cohérentes, ciblage énergie, contexte géopolitique. Point faible : absence de malware custom Sandworm identifié.

**H2 cluster chinois (Volt Typhoon ou similaire)** : confiance faible à modérée. TTP LotL s’alignent fortement, mais contexte géopolitique moins aligné, beaconing régulier atypique.

**H3 nouveau cluster étatique non attribué** : confiance faible. Ne peut être écartée.

**H4 acteur non-étatique** : **éliminée** (4 incohérences fortes).

**Conclusion** : pré-positionnement OT par acteur étatique — très probable (>80%). Attribution la plus probable Sandworm/GRU confiance modérée, Chine confiance faible-modérée, cluster non identifié possibility. Documentation des indicateurs de révision.

## 32.5 La réponse : scope avant contenir

Le CERT applique la règle **scope avant contenir**.

**Scope approfondi** (J+42 à J+48) :

- Threat hunting sur tous les endpoints : recherche d’autres systèmes compromis via les TTP identifiées.
- Identification de **2 autres endpoints compromis** non détectés initialement (un autre poste d’ingénierie, un serveur de supervision).
- Identification de **1 compte admin de domaine compromis** (Kerberoasting réussi — credentials cachés sur les systèmes compromis).
- Identification des mécanismes de persistence sur chaque système.
- Cartographie complète : 3 endpoints, 1 compte admin, 3 mécanismes de persistence par endpoint, plusieurs backdoors secondaires.

**Planification du containment coordonné** (J+48) :

- Équipe dédiée constituée (CERT + IT + OT + direction sécurité).
- Plan de containment simultané documenté : éradication de tous les accès dans une fenêtre de 6 heures.
- Playbook de communication (interne, autorités, potentiellement public).

**Containment exécuté (J+49, nuit de vendredi à samedi)** :

- 22h : réinitialisation de **tous** les comptes compromis (changement de mots de passe, révocation des tickets Kerberos via changement du KRBTGT deux fois).
- 23h : isolation réseau des endpoints compromis.
- 23h30 : neutralisation des mécanismes de persistence (suppression des DLL, des tâches planifiées, des services modifiés).
- 01h : patching du VPN Ivanti (vecteur initial) — patches appliqués depuis plusieurs semaines mais vérification et re-validation.
- 02h-06h : reconstruction des systèmes compromis à partir d’images propres.
- 06h : validation des systèmes reconstruits.
- Ensuite : monitoring renforcé, règles de détection spécifiques déployées pour détecter une tentative de réentrée.

## 32.6 Sécurisation OT post-incident

Post-éradication, l’opérateur renforce sa posture OT.

**Segmentation physique IT/OT renforcée** : revue complète des points de convergence. Plusieurs accès sont reconfigurés, certains supprimés (simplification de l’architecture).

**Déploiement Sysmon/EDR sur les postes d’ingénierie OT** : quand techniquement possible (OS récents). Les postes sur OS hérités font l’objet de compensating controls (restriction réseau, monitoring renforcé en amont).

**Passive monitoring OT** : déploiement d’une solution OT dédiée (Claroty ou équivalent) sur les segments de supervision. Baseline construite sur 30 jours puis règles de détection activées.

**Durcissement AD** : tiering strict, PAM pour les comptes admin, monitoring des changements critiques.

**Patching edge** : processus accéléré (patch en < 48h sur les vulnérabilités CISA KEV).

**Exercice tabletop programmé** : scénario « pré-positionnement OT à nouveau détecté » pour éprouver la coordination après le vécu de l’incident réel.

## 32.7 Signalement et coordination

**Signalement ANSSI** : l’opérateur étant OIV, la notification à l’ANSSI est obligatoire dès la qualification de l’incident. Notification initiale sous 24h, détaillée sous 72h, rapport complet ultérieurement.

**Accompagnement ANSSI** : équipe technique mobilisée, revue des éléments techniques, partage d’IoC avec d’autres opérateurs français potentiellement concernés.

**Partage ISAC énergie européen (EE-ISAC)** : diffusion TLP:AMBER des IoC et TTP. Dans les 2 semaines suivantes, **2 autres opérateurs européens confirment avoir observé des TTP identiques** — signe que BLACKOUT n’est pas isolé, mais partie d’une campagne plus large ciblant l’énergie européenne.

**Coordination internationale** : les TTP et le contexte sont partagés avec CISA (via l’ANSSI), NCSC UK, BSI. Coordination croisée pour identifier d’autres victimes.

**Attribution publique** : l’opérateur et l’ANSSI décident de **ne pas communiquer publiquement** à court terme. Raisons : éviter d’exposer les méthodes de détection, préserver la capacité de surveillance d’autres opérations potentielles, contexte diplomatique à gérer par les autorités. Une attribution publique pourrait survenir ultérieurement dans le cadre d’un advisory multilatéral coordonné.

## 32.8 Monitoring post-éradication et veille

Post-éradication, l’opérateur met en place un **monitoring renforcé** pour détecter une éventuelle tentative de réentrée.

**Règles de détection spécifiques** :

- Alertes sur toute exploitation détectée de CVE Ivanti récentes.
- Monitoring des DLL loading dans les applications de supervision (détection de sideloading).
- Baseline comportementale stricte sur les postes d’ingénierie OT.
- Alertes sur tout Kerberoasting détecté.

**Veille sur les indicateurs** : surveillance des IoC publics liés à Sandworm, Volt Typhoon, et clusters associés. Intégration aux flux CTI.

**Threat hunting trimestriel** : chasse active sur les TTP observées, extension progressive à d’autres TTP Sandworm documentées.

**Exercices réguliers** : tabletop trimestriel sur des scénarios APT dérivés de BLACKOUT.

**Résultat à 6 mois** : **pas de détection d’une nouvelle intrusion** dans l’environnement. L’attaquant n’est pas revenu (ou n’a pas été détecté) via les vecteurs surveillés. L’éradication semble efficace.

## 32.9 La leçon centrale

comprendre les acteurs pour calibrer la réponse

**La leçon centrale de BLACKOUT — et du cours entier** — peut être formulée ainsi : **face à une intrusion sophistiquée, comprendre les acteurs est indispensable pour répondre correctement**.

Sans la connaissance des acteurs, l’analyste face à BLACKOUT :

- Ne sait pas interpréter le **pré-positionnement OT** — s’agit-il d’un sabotage imminent (réaction immédiate brutale nécessaire) ? d’une capacité de dissuasion (réaction mesurée, surveillance longue possible) ? d’une reconnaissance (exfiltration à craindre) ? Les réponses diffèrent radicalement.
- Ne sait pas **calibrer l’urgence** — un acteur qui prépare un sabotage (profil Sandworm en contexte ukrainien escaladant) nécessite une éradication immédiate. Un acteur en pré-positionnement stratégique (profil Volt Typhoon) peut justifier une phase de surveillance contrôlée.
- Ne sait pas **qui alerter et comment** — le signalement ANSSI déclenche des processus différents selon que l’acteur est russe (contexte ukrainien, information-sensibilité diplomatique), chinois (enjeu Taïwan), ou inconnu (prudence supplémentaire).
- Ne sait pas **anticiper les prochains mouvements** — un Sandworm éradiqué tentera probablement de revenir via des vecteurs différents (adaptation rapide des TTP). Un Volt Typhoon éradiqué pourrait se rétablir via des accès redondants non identifiés. Le monitoring post-incident se calibre sur ces profils.

**Un SOC sans connaissance des APT** détecte un beaconing et isole un poste. Un **SOC informé par le cours APT** comprend que ce beaconing dans un OIV énergétique européen en contexte géopolitique tendu est compatible avec un pré-positionnement étatique, calibre l’urgence de la réponse en conséquence, et déclenche les bons processus (signalement ANSSI, partage ISAC, monitoring OT renforcé, potentiellement coordination diplomatique).

C’est la raison d’être de ce cours.

## 32.10 Ce qui aurait pu rater, ce qu’on aurait pu mieux faire

Post-mortem blameless sur BLACKOUT, dans l’esprit de l’apprentissage continu.

**Ce qui a marché** :

- La **détection EDR** a fonctionné — le comportement anormal (rundll32 + DLL non signée + beaconing) a produit une alerte traitée.
- La discipline **scope avant contenir** a été respectée, évitant une éradication partielle qui aurait alerté l’attaquant.
- La **coordination ANSSI/ISAC** a produit de la valeur — identification d’autres victimes, enrichissement analytique.

**Ce qui aurait pu rater** :

- **Si l’EDR avait été moins bien configuré**, le rundll32 avec DLL non signée serait passé inaperçu. Beaucoup d’organisations n’ont pas ce niveau de configuration.
- **Si l’opérateur n’avait pas eu de visibilité sur les postes d’ingénierie OT** (beaucoup d’organisations OT n’en ont pas), l’attaquant serait resté indétecté probablement des années.
- **Si l’équipe CERT avait été moins mûre**, l’investigation aurait confondu cybercrime et APT, et la réponse aurait été inadaptée.
- **Si le patching Ivanti avait été plus rapide** (CVE-2024-21887 était disponible plusieurs semaines avant la compromission J0), l’intrusion initiale n’aurait pas eu lieu.

**Ce qu’on aurait pu mieux faire** :

- **Détection plus précoce** : 42 jours de dwell time est long. Des baselines comportementales plus matures, des règles de détection sur les TTP Sandworm/Volt Typhoon déjà publiées, auraient pu détecter plus tôt.
- **Visibilité OT dès le début** : le passive monitoring OT déployé post-incident aurait pu détecter le pivot IT→OT beaucoup plus tôt s’il avait été en place. Investissement qui aurait été priorisé en amont.
- **Durcissement des postes double-connectés** : les engineering workstations double-connectés sont le point de rupture structurel. Un durcissement spécifique (EDR dédié, monitoring renforcé, restrictions strictes, MFA systématique) aurait réduit la surface.
- **Exercices APT plus fréquents** : l’organisation avait fait des tabletops généraux, pas spécifiquement sur des scénarios APT OT. L’expérience aurait été plus fluide avec une préparation spécifique.
- **Contacts ISAC établis plus tôt** : la coordination EE-ISAC s’est construite pendant la crise. Des relations établies en amont auraient accéléré le partage.

**La leçon transversale** : la défense APT-ready est un **investissement continu** qui doit être fait **avant** l’incident. Pendant la crise, il est trop tard pour construire les capacités — on ne peut que mobiliser ce qui existe. L’opérateur BLACKOUT avait assez de capacités pour détecter, scoper, et éradiquer avec succès. Mais la perfection relative de la réponse n’efface pas la question : combien d’autres opérateurs européens ont des pré-positionnements similaires non détectés, faute de capacités ?

La réponse à cette question est le sujet des années à venir. Ce cours a tenté d’y contribuer.

-----
