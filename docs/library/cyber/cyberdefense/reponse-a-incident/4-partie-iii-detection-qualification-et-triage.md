---
title: PARTIE III — DÉTECTION, QUALIFICATION ET TRIAGE
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
chapter: 4
chapters: 9
---

*L'incident est suspecté ou confirmé. Il faut comprendre de quoi il s'agit, depuis quand, et quelle est l'étendue probable — le tout en prenant les premières mesures conservatoires sans détruire les preuves.*

---

### Chapitre 11 — Du signal faible à l'incident confirmé

#### 11.1 Sources de détection et leurs biais

Chaque source de détection a un périmètre de visibilité et des angles morts. L'**EDR/XDR** détecte les comportements suspects sur les endpoints (exécution de binaires, modifications système, connexions réseau des processus) mais ne voit pas le trafic réseau entre les machines ni les activités cloud. Le **SIEM** voit les logs qui y sont envoyés — ce qui signifie que tout ce qui n'est pas journalisé est invisible (si le PowerShell script block logging n'est pas activé, le SIEM ne verra jamais les commandes PowerShell de l'attaquant). Le **NDR** voit le trafic réseau en temps réel mais ne voit pas le contenu du trafic chiffré (et en 2025-2026, la quasi-totalité du trafic C2 est chiffrée en HTTPS). Les **alertes antivirus** sont souvent noyées dans le bruit des faux positifs et des détections de PUA (Potentially Unwanted Applications). Le **signalement utilisateur** est parfois le premier signal (« j'ai cliqué sur un lien bizarre ») mais il est souvent tardif (l'utilisateur n'ose pas signaler, ou ne se rend pas compte). La **notification externe** (CERT-FR, partenaire, threat intel feed, notification par l'attaquant via une note de rançon) indique que la compromission est déjà connue en dehors de l'organisation — et souvent que le temps de séjour est déjà long.

La conséquence pour l'investigateur est qu'aucune source seule ne donne la vision complète. La corrélation multi-sources (endpoint + réseau + AD + cloud) est la seule méthode fiable pour établir l'étendue réelle de la compromission.

#### 11.2 Le temps de séjour (dwell time)

Le dwell time — la durée entre la compromission initiale et la détection — est la métrique qui détermine la profondeur de l'investigation. Selon le M-Trends 2025 de Mandiant, la médiane mondiale est d'environ 10 à 13 jours, avec une amélioration progressive grâce à la généralisation des EDR. Mais cette médiane masque une distribution très dispersée : les ransomwares sont souvent détectés en quelques jours (l'attaquant accélère pour chiffrer), tandis que les opérations d'espionnage peuvent durer des mois, voire des années.

Le dwell time détermine la fenêtre temporelle de l'investigation : si l'attaquant est dans le réseau depuis 5 semaines, il faut investiguer 5 semaines de logs, d'artefacts, et de flux réseau. Si les logs ne couvrent que 30 jours, les premières actions de l'attaquant sont perdues.

#### 11.3 Les signaux faibles pré-incident

Avant l'alerte majeure qui déclenche l'IR, des signaux faibles ont souvent été générés — et ignorés ou sous-priorisés. Les connexions à des heures inhabituelles (un compte de service qui s'authentifie à 3h du matin un dimanche), les alertes Kerberos en masse (erreurs de pré-authentification répétées sur de nombreux comptes = possible password spraying ou Kerberoasting), les modifications de GPO non documentées, les exécutions de binaires depuis des répertoires temporaires, les requêtes DNS vers des domaines générés algorithmiquement (DGA), et les petits pics d'exfiltration (quelques Go par jour, en dessous du seuil d'alerte mais visibles en tendance).

La difficulté est que ces signaux sont noyés dans le bruit de fonctionnement normal d'un SI de 12 000 utilisateurs. L'amélioration de la détection des signaux faibles passe par le tuning des règles de détection (réduction des faux positifs pour rendre les vrais positifs visibles), la détection comportementale (baseline de normalité par utilisateur et par machine, alertes sur les écarts), et la corrélation multi-sources (un signal faible sur l'endpoint + un signal faible sur le réseau + un signal faible sur l'AD = un signal fort).

#### 11.4 Fil rouge — BLACKTIDE : les signaux manqués

> **🔍 BLACKTIDE — Épisode 11**
>
> L'investigation post-incident révélera que 3 alertes avaient été générées et classées faux positifs ou basse priorité. À J-30 : alerte antivirus sur un script PowerShell encodé détecté sur le poste du DRH du sous-traitant GestPaie, qui se connectait via VPN au réseau Arvantis. L'alerte a été classée « PUA — faux positif probable » par le SOC N1. En réalité, c'était l'infostealer Lumma en phase d'installation. À J-22 : pic anormal de requêtes Kerberos TGS (Event ID 4769) avec encryption type RC4 (0x17) sur DC01 — signature classique de Kerberoasting. L'alerte SIEM a été classée « activité suspecte — priorité basse » parce que le volume ne dépassait pas le seuil d'alerte automatique. À J-15 : seconde alerte antivirus, cette fois sur DC01, pour un script PowerShell obfusqué dans `C:\Windows\Temp\`. Classée faux positif parce que « les admins utilisent parfois PowerShell sur les DC ».
>
> Trois occasions manquées de détecter l'intrusion 2 à 4 semaines plus tôt — quand le confinement aurait été beaucoup plus simple.

---

### Chapitre 12 — Triage initial et premières mesures conservatoires

#### 12.1 Les 30 premières minutes

Le triage initial est l'évaluation rapide qui transforme une alerte en décision d'action. Les objectifs des 30 premières minutes sont de confirmer le vrai positif (exclure le faux positif, l'erreur de configuration, l'opération de maintenance planifiée), d'identifier les systèmes visiblement impactés (la machine source de l'alerte, les machines contactées, les comptes utilisés), d'évaluer la sévérité initiale (P4 à P1, avec possibilité de réévaluation), et de prendre les premières mesures conservatoires.

#### 12.2 Ce que l'on sait et ce que l'on ne sait pas

L'exercice fondamental du triage consiste à lister explicitement les faits confirmés et les inconnues. Cette discipline évite les conclusions prématurées et oriente l'investigation. Format recommandé :

**Ce qu'on sait :** « L'EDR a détecté l'exécution de PsExec sur DC01 à 22h17, depuis le profil du compte svc_deploy. Une modification de GPO visant à désactiver Defender a été tentée. Le compte svc_deploy n'est pas utilisé par les administrateurs ce soir. »

**Ce qu'on ne sait pas :** « Depuis quand l'attaquant est-il dans le réseau. Combien de systèmes sont compromis. Si des données ont été exfiltrées. Si d'autres DC sont touchés. Si l'attaquant est toujours actif en ce moment. »

Cette distinction structure le raisonnement et guide les questions d'investigation suivantes.

#### 12.3 Premières mesures conservatoires

À ce stade, l'objectif n'est pas de contenir (c'est trop tôt — on ne connaît pas l'étendue) mais de préserver la capacité d'investigation et de limiter les risques immédiats sans alerter l'attaquant. Les mesures conservatoires incluent l'augmentation du niveau de logging sur les systèmes suspects (activer la journalisation de la ligne de commande des processus si elle ne l'est pas, augmenter la verbosité du logging AD), la capture réseau sur les segments critiques (si un NDR ou une capacité de capture existe), la sauvegarde immédiate des logs disponibles (avant qu'ils ne soient écrasés par la rotation), et la mise en surveillance renforcée des systèmes identifiés (le SOC concentre son attention sur les machines suspectes).

L'isolation réseau n'est pas systématiquement la bonne décision à ce stade. Si l'attaquant ne sait pas qu'il est détecté, l'isoler maintenant l'alertera et il pourra activer des mécanismes de destruction (wiper, chiffrement accéléré) ou détruire des preuves. Le dilemme du confinement est traité en détail au Ch.23.

#### 12.4 Fil rouge — BLACKTIDE : le triage

> **🔍 BLACKTIDE — Épisode 12**
>
> 22h30-23h00. Karim confirme : PsExec sur DC01, DC02 et DC03. Modification GPO tentée sur les 3 DC. Exécution d'un binaire inconnu sur DC01 (hash non présent dans VirusTotal — soumission en cours). Le compte svc_deploy est un compte de service pour le déploiement de logiciel via SCCM — il a des droits élevés mais est rarement utilisé manuellement. L'authentification avec ce compte provient de l'IP 10.42.15.87 (un serveur de fichiers du site de Lyon).
>
> Mesures conservatoires immédiates : augmentation du logging sur les 3 DC (activation de la journalisation de la ligne de commande, Event ID 4688), capture réseau activée sur le segment DMZ et le segment serveurs via le port mirroring du switch core, sauvegarde des Event Logs actuels des 3 DC sur un partage hors domaine (clé USB branchée par l'admin d'astreinte, sous les instructions de Nadia).
>
> Pas d'isolation réseau à ce stade. Nadia veut d'abord comprendre l'étendue avant de décider du périmètre de confinement.

---

### Chapitre 13 — Qualification, catégorisation et évaluation de gravité

#### 13.1 Catégorisation de l'incident

La catégorisation identifie le type d'incident pour orienter vers le playbook approprié et conditionner les obligations réglementaires. La question n'est pas « qu'est-ce qui s'est passé techniquement ? » (ça, c'est l'investigation) mais « quel type de problème avons-nous ? » (ransomware, espionnage, compromission de compte, etc.).

Dans le cas de BLACKTIDE, la catégorisation initiale est « compromission de serveur critique avec mouvement latéral ». Elle évoluera vers « ransomware avec double extorsion et exfiltration massive » au fur et à mesure de l'investigation.

#### 13.2 Évaluation de la gravité

La gravité s'évalue sur une grille multicritères. La **gravité technique** mesure le nombre de systèmes touchés, le niveau de privilèges compromis, et la propagation (en cours vs achevée). La **gravité métier** mesure l'impact sur la production, la facturation, la logistique, et les clients. La **sensibilité des données** qualifie les données potentiellement exposées (données personnelles, propriété intellectuelle, secret industriel, secret défense). La **criticité des systèmes** identifie les systèmes touchés (Active Directory, systèmes de paiement, systèmes OT, serveurs de production). Le **potentiel de propagation** évalue si l'attaquant est toujours actif et si la compromission peut s'étendre. L'**impact réglementaire** identifie les notifications obligatoires et les sanctions potentielles.

La grille de gravité complète avec les critères détaillés pour chaque niveau (P1 à P4) est en Annexe G.

#### 13.3 Évaluation dynamique

La gravité n'est pas figée — elle doit être réévaluée à chaque nouvelle découverte. Un incident initialement classé P3 peut basculer P1 quand l'investigation révèle que le malware « isolé » était en fait un infostealer actif depuis des semaines, alimentant la compromission de l'AD. La réévaluation régulière est une discipline essentielle : à chaque SitRep (toutes les 4-6 heures en phase aiguë), la gravité est recalculée et les décisions ajustées.

#### 13.4 Fil rouge — BLACKTIDE : réévaluation en cascade

> **🔍 BLACKTIDE — Épisode 13**
>
> La gravité est réévaluée 4 fois en 8 heures.
> - 22h30 : **P2** — alerte EDR sur un DC, compromission de serveur probable.
> - 01h00 : **P1** — 3 DC touchés, ransomware en cours de déploiement, compromission majeure confirmée.
> - 06h00 : **P1 / Crise** — exfiltration de 380 Go confirmée, 3 sites impactés dont un OIV, données RH de 8 000 personnes exposées.
> - 10h00 : **Crise confirmée** — publication sur le canal Telegram de PhantomCrypt avec compte à rebours de 10 jours, presse spécialisée informée par la revendication.

---

### Chapitre 14 — Scoping initial : délimiter l'étendue de la compromission

#### 14.1 La question la plus critique et la plus difficile

L'attaquant a-t-il compromis un seul poste, un segment réseau, ou le domaine entier ? La réponse conditionne toutes les décisions suivantes : le périmètre du confinement (isoler 3 machines ou 3 sites ?), le dimensionnement de l'équipe IR (3 analystes ou 15 ?), les notifications réglementaires (incident technique interne ou violation de données à déclarer ?), et la durée prévisible de la réponse (2 jours ou 3 semaines ?).

Le scoping est un exercice d'approximation rapide — il sera affiné au fil de l'investigation, mais la première estimation doit être produite dans les premières heures pour guider les décisions de confinement. Sous-estimer le périmètre conduit à un confinement insuffisant. Surestimer conduit à un impact business disproportionné.

#### 14.2 Méthode de scoping rapide

Croiser les sources disponibles dans les premières heures pour délimiter le périmètre. Les IoC identifiés (hash du malware, domaine C2, IP C2) sont recherchés sur l'ensemble du parc via l'EDR — quelles machines ont communiqué avec le C2, exécuté le hash, ou présenté les mêmes artefacts ? Les logs d'authentification Active Directory sont analysés — quels comptes ont été utilisés, depuis quelles machines, à quelles heures ? Y a-t-il des authentifications anormales (geo-impossible, horaires inhabituels, comptes de service utilisés manuellement) ? Les logs réseau sont examinés — quels systèmes communiquent avec des destinations suspectes ?

L'intersection de ces sources donne le périmètre initial : les machines confirmées compromises, les machines probablement compromises, et les machines non touchées (à ce stade).

#### 14.3 Première timeline

La timeline provisoire est la reconstitution chronologique des événements identifiés à ce stade. Elle sera enrichie et corrigée tout au long de l'investigation (Ch.17), mais la première version oriente le scoping : si le premier signe de compromission remonte à 5 semaines, tout ce qui s'est passé pendant ces 5 semaines doit être investigué.

#### 14.4 Fil rouge — BLACKTIDE : le scoping

> **🔍 BLACKTIDE — Épisode 14**
>
> En 3 heures (22h30-01h30), l'équipe établit un périmètre provisoire.
>
> **Confirmé compromis :** DC01, DC02, DC03 (traces de PsExec, GPO malveillante, exécution du ransomware builder). Serveur de fichiers FS01-Lyon, FS01-Fos, FS01-Cologne (chiffrement en cours). Le poste du DRH de GestPaie (sous-traitant — point d'entrée de l'infostealer, confirmé par analyse de l'alerte antivirus de J-30).
>
> **Probablement compromis :** 40+ machines listées dans les logs PsExec. Le serveur SCCM (utilisé comme pivot via le compte svc_deploy). Au moins un serveur du réseau OT de Fos (le poste d'ingénierie a des traces de connexion depuis DC01).
>
> **Volume estimé de l'exfiltration :** 380 Go (identifié par corrélation des logs proxy — flux HTTPS vers des endpoints AWS S3 depuis 3 machines internes, sur 7 jours).
>
> **Timeline provisoire :** Patient zéro estimé à J-35 (phishing sur GestPaie). Compromission de l'AD estimée à J-14 (DCSync). Début d'exfiltration estimé à J-7. Déploiement du ransomware : J-0.

---

### Chapitre 15 — Déclenchement formel et premières notifications

#### 15.1 Ouverture formelle de l'incident

L'ouverture formelle marque le passage du mode « investigation exploratoire » au mode « réponse structurée ». Elle comprend la désignation du pilote (IR lead), la constitution de la cellule technique, l'ouverture du journal d'incident (chronologique, chaque action horodatée et signée — le document le plus important de l'incident, car il reconstitue la séquence des décisions et protège les décideurs), l'activation du canal de communication sécurisé (hors SI — Signal, WhatsApp groupe, téléphone — le SI interne est potentiellement compromis et ne peut plus être utilisé pour des communications sensibles), et l'attribution d'un nom de code (pour la communication interne et la traçabilité des documents).

#### 15.2 Première SitRep

Le premier SitRep est produit dans les 2 à 4 premières heures, à destination du RSSI et de la direction. Il suit une structure standardisée : ce qu'on sait (faits confirmés, cotés), ce qu'on ne sait pas (inconnues explicites), ce qu'on fait (actions en cours), ce qu'on envisage (prochaines étapes, options de confinement), et ce dont on a besoin (ressources, décisions, autorisations). Format : une page maximum, factuel, sans jargon technique excessif.

#### 15.3 Notifications urgentes

Les notifications qui ne peuvent pas attendre : ANSSI/CERT-FR si OIV ou OSE (dans les délais réglementaires), prestataire PRIS (si non encore mobilisé), assureur cyber (dans les conditions du contrat — souvent 24 à 48h), et direction générale (information de la bascule en crise si applicable). Les notifications complètes (CNIL 72h, dépôt de plainte) viendront dans les jours suivants mais doivent être préparées dès maintenant.

#### 15.4 Fil rouge — BLACKTIDE : le déclenchement

> **🔍 BLACKTIDE — Épisode 15**
>
> 01h00 — Opération BLACKTIDE est officiellement ouverte. Nadia est IR lead. Canal Signal « IR-BLACKTIDE » activé avec 8 participants (Nadia, Karim, Marc/RSSI, David/admin astreinte, Fatima/SOC N2 relève, et 3 autres analystes mobilisables). Journal d'incident ouvert sur un tableur Excel hébergé sur le laptop personnel de Nadia (non joint au domaine Arvantis — bonne pratique improvisée).
>
> ANSSI notifiée à 08h00 le samedi (obligation OIV — site de Fos-sur-Mer impacté). Le CERT-FR accuse réception et propose un appui spécialisé OT pour le lundi. Prestataire PRIS CyberForce arrivé à 08h15 (Thomas Hartmann, consultant senior forensic, et Léa Chen, spécialiste AD). Assureur cyber AXA XL notifié à 10h00 le samedi (dans le délai contractuel de 48h).

---
