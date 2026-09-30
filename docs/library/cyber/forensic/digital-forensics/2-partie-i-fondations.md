---
title: PARTIE I — FONDATIONS
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
chapter: 2
chapters: 9
---

*Cette première partie pose les bases indispensables avant toute investigation. Elle répond aux questions que tout analyste forensic doit maîtriser avant de toucher un clavier : qu'est-ce que le forensic numérique, dans quel cadre juridique il s'inscrit, quelle méthodologie il suit, avec quels outils il opère, et avec quelle posture intellectuelle il raisonne.*

---

### Chapitre 1 — Qu'est-ce que le digital forensics

#### 1.1 Définition : science de la preuve numérique

Le digital forensics — ou investigation numérique — est la discipline scientifique qui consiste à identifier, préserver, collecter, analyser et présenter des preuves numériques de manière à ce qu'elles soient recevables devant un tribunal ou exploitables pour une décision stratégique. Le mot clé est « scientifique » : le forensic n'est pas du bricolage technique, c'est un processus rigoureux, reproductible et documenté.

Le forensic numérique répond à des questions fondamentales : que s'est-il passé, quand, comment, par qui, et quelles données ont été impactées. Ces questions sont les mêmes qu'en criminalistique physique (qui a commis l'acte, avec quel outil, où, quand), transposées au monde numérique. Et comme en criminalistique physique, la qualité de la collecte de preuves détermine la qualité des conclusions. Un disque mal acquis, un log non préservé, un dump mémoire raté : autant de scènes de crime contaminées dont les conclusions seront contestables.

La particularité du numérique est la volatilité : contrairement à une empreinte digitale sur une poignée de porte, une connexion réseau disparaît quand le processus se termine, un fichier supprimé peut être écrasé par le système d'exploitation en quelques minutes sur un SSD, et un redémarrage de machine efface la mémoire vive avec tout ce qu'elle contenait — credentials en clair, processus malveillants, connexions C2 actives. L'urgence de la préservation est la contrainte fondamentale du forensic numérique.

#### 1.2 Forensic ≠ incident response ≠ pentest ≠ threat intel

Le forensic s'inscrit dans un écosystème plus large de cybersécurité, et les confusions de posture entre disciplines sont fréquentes et dommageables.

Le **digital forensics** cherche à comprendre ce qui s'est passé et à produire des preuves exploitables. Son tempo est long (jours à semaines), sa contrainte clé est l'intégrité des preuves et la rigueur méthodologique. L'**incident response** cherche à contenir l'attaque, éradiquer la menace, et restaurer le service. Son tempo est court (heures à jours), sa contrainte clé est la rapidité et la continuité d'activité. Le **pentest / red team** cherche à trouver les vulnérabilités avant les attaquants. Son tempo est planifié (semaines), sa contrainte est le périmètre autorisé. La **threat intelligence** cherche à comprendre les menaces, les acteurs, et les tendances. Son tempo est continu, sa contrainte est la qualité des sources et la prudence de l'attribution.

En pratique, ces disciplines interagissent constamment. Le SOC détecte une alerte, l'IR qualifie et contient, le forensic investigue en profondeur, et la CTI contextualise (quel groupe, quelles TTP, quel objectif). Le forensic peut aussi intervenir hors incident : investigation sur un employé suspect (insider threat), due diligence lors d'une acquisition d'entreprise, analyse d'un litige commercial (preuve de suppression de fichiers), ou expertise judiciaire ordonnée par un magistrat.

Le cours IR de la bibliothèque traite de l'orchestration de la réponse ; le cours CTI/Écosystèmes traite de la contextualisation de la menace. Ce cours traite de l'investigation technique et de la production de preuves.

#### 1.3 Les branches du forensic

Le forensic numérique se décline en plusieurs spécialités, chacune avec ses artefacts, ses outils et ses contraintes. Ces spécialités ne sont pas cloisonnées — une investigation complète les combine presque toujours.

Le **disk forensics** (analyse de supports de stockage) est la branche historique : acquisition bit-à-bit d'un disque, analyse du système de fichiers, récupération de fichiers supprimés, analyse des métadonnées et des artefacts système. C'est le socle du cours (Parties II-IV). Le **memory forensics** (analyse de mémoire vive) capture l'état instantané du système — processus, connexions, credentials, malware fileless. C'est devenu incontournable avec la montée des attaques sans fichier (Ch.17). Le **network forensics** (analyse réseau) examine les captures de trafic et les logs réseau pour reconstituer les communications de l'attaquant et caractériser l'exfiltration (Ch.19). Le **mobile forensics** analyse les smartphones et tablettes — terminaux qui contiennent souvent plus de données exploitables qu'un PC, mais avec des protections renforcées (Ch.23). Le **cloud forensics** investigue dans les environnements cloud (AWS, Azure, GCP, M365) avec des défis spécifiques : pas d'accès physique, données éphémères, multi-juridiction (Ch.21). Le **malware forensics** analyse le comportement d'un malware pour comprendre ses fonctionnalités et extraire les IoC, sans aller jusqu'au reverse engineering complet (Ch.18).

#### 1.4 La tension fondamentale : forensic judiciaire vs triage DFIR

C'est la distinction la plus structurante du cours, et elle conditionne chaque décision que l'analyste prendra sur le terrain.

Le **forensic judiciaire** vise à produire des preuves recevables devant un tribunal. L'exhaustivité prime sur la rapidité : chaque élément de preuve est acquis dans le respect de la chaîne de custody, hashé, documenté, et traçable. L'intégrité est absolue. Le tempo est long (jours à semaines). Le destinataire est un juge, un expert contradictoire, ou un procureur.

Le **triage DFIR** vise à comprendre rapidement ce qui se passe pour contenir la menace et éradiquer l'attaquant. La rapidité prime sur l'exhaustivité : on collecte les artefacts les plus parlants sur les machines les plus critiques, on analyse en parallèle, on produit des IoC pour le SOC. Le tempo est court (heures à jours). Le destinataire est l'IR lead, le SOC, et le RSSI.

En pratique, ces deux régimes ne s'excluent pas — ils s'articulent. La plupart des investigations commencent en mode triage (comprendre l'urgence) et basculent en mode judiciaire si les constatations le justifient (vol de données avéré, fraude, attaque étatique). Savoir quand et comment basculer est une compétence critique : le triage initial ne doit pas compromettre les preuves nécessaires à la judiciarisation. C'est pourquoi, même en triage, les bonnes pratiques de chaîne de custody et de hashing doivent être respectées dès le début — on ne sait jamais si l'affaire finira devant un juge.

Trois axes de tension traversent toute investigation : rapidité vs exhaustivité (collecter 80 % en 2 heures ou 100 % en 2 jours), continuité d'activité vs gel des preuves (laisser la machine en production ou la saisir), et investigation interne vs perspective judiciaire (souplesse méthodologique vs procédure stricte, scellés, expert judiciaire).

#### 1.5 Qui fait du forensic

Les acteurs du forensic sont variés. Les **CERT/CSIRT** (Computer Emergency Response Teams) combinent IR et forensic — en France, le CERT-FR (ANSSI) pour l'État et les OIV, les CSIRT sectoriels (santé, finance), et les CSIRT d'entreprise. Les **SOC** font du triage de premier niveau — qualification d'alertes, collecte initiale d'artefacts. Les **forces de l'ordre spécialisées** mènent les investigations judiciaires : le C3N (Centre de lutte contre les criminalités numériques, Gendarmerie), l'OCLCTIC (Office central de lutte contre la criminalité liée aux TIC), les ICC (Investigateurs en cybercriminalité) répartis dans les brigades territoriales, et la BL2C (Brigade de Lutte contre la Cybercriminalité, Préfecture de Police de Paris). Les **cabinets privés** et prestataires qualifiés PRIS interviennent pour des investigations internes, des due diligences, ou en appui des entreprises victimes. Les **experts judiciaires**, inscrits sur les listes des cours d'appel, sont mandatés par les magistrats pour les expertises contradictoires.

#### 1.6 Le forensic dans la chaîne cybersécurité

Le forensic s'insère dans une chaîne plus large : détection (le SOC identifie une alerte via le SIEM ou l'EDR) → qualification (l'analyste SOC confirme le vrai positif et évalue la gravité) → triage/investigation (l'équipe DFIR collecte les artefacts et analyse) → remédiation (éradication de la menace, restauration, durcissement) → judiciarisation éventuelle (dépôt de plainte, expertise judiciaire). Le forensic intervient principalement dans la phase triage/investigation, mais il prépare aussi la judiciarisation et alimente la remédiation. Le cours IR de la bibliothèque détaille l'ensemble de cette chaîne ; ce cours se concentre sur la phase forensic.

#### 1.7 Fil rouge — MUSIC BOX : l'alerte

> **🔬 MUSIC BOX — Épisode 1**
>
> Vendredi 7 mars 2026, 17h12. L'EDR déclenche sur le poste WKS-RD-047 (Windows 11, département R&D, utilisateur : Dr. Julien Mallet, chercheur principal sur la molécule NP-427). Alerte : « Process svchost.exe (PID 7284, parent: explorer.exe) attempting to access LSASS memory ».
>
> Romain (SOC) vérifie : svchost.exe avec explorer.exe comme parent est anormal — les svchost légitimes ont services.exe comme parent. L'accès à LSASS est un indicateur de credential dumping (T1003). C'est un vrai positif.
>
> Première décision : triage rapide ou investigation complète ? Claire (IR lead) tranche : triage immédiat pour évaluer la gravité (dump RAM du poste suspect, collecte des artefacts KAPE, vérification des connexions sortantes via le proxy). La machine n'est PAS éteinte, PAS isolée du réseau immédiatement — on veut d'abord comprendre avec qui elle communique. En parallèle, préservation de la chaîne de custody dès le début : l'experte judiciaire Maître Fournier est contactée et sera sur site samedi matin.
>
> La bascule vers une investigation complète sera décidée lundi, selon les premiers résultats. Mais la préservation des preuves commence maintenant — on ne sait pas encore si cette affaire finira devant un juge.

---

### Chapitre 2 — Cadre juridique et recevabilité de la preuve

#### 2.1 La preuve numérique en droit français

La preuve numérique est admissible en droit français, tant en matière pénale (Code de procédure pénale) qu'en matière civile et commerciale (Code civil, Code de commerce). Mais son admissibilité est conditionnée par trois principes fondamentaux qui guident toute la méthodologie forensic.

La **loyauté** signifie que la preuve doit avoir été obtenue par des moyens légaux et éthiques. Une preuve obtenue par piratage, par intrusion non autorisée dans un système tiers, ou en violation du droit du travail est irrecevable, quel que soit son contenu. En matière pénale, la jurisprudence est stricte : les preuves obtenues de manière déloyale par les forces de l'ordre sont annulées (principe posé par la chambre criminelle de la Cour de cassation). En matière civile, la jurisprudence a évolué : l'assemblée plénière de la Cour de cassation a admis en 2023 que des preuves obtenues de manière déloyale pouvaient être recevables si leur production était indispensable à l'exercice du droit à la preuve et proportionnée aux intérêts en jeu. Mais cette ouverture ne dispense pas de la rigueur.

L'**intégrité** garantit que la preuve n'a pas été altérée entre le moment de la collecte et le moment de la présentation. C'est le fondement de la chaîne de custody et du hashing : prouver qu'un fichier analysé est identique au fichier collecté, bit pour bit. Sans preuve d'intégrité, la partie adverse peut contester que la preuve a été modifiée — intentionnellement ou accidentellement.

Le **contradictoire** impose que la partie adverse puisse examiner, contester et faire contre-expertiser la preuve. C'est pourquoi la documentation méthodologique est aussi importante que l'analyse elle-même : il faut pouvoir expliquer exactement comment on a procédé, avec quels outils (nom, version, paramètres), et pourquoi, pour qu'un expert adverse puisse reproduire ou contester les résultats. Un rapport forensic techniquement brillant mais méthodologiquement opaque sera attaqué au contradictoire.

#### 2.2 Code de procédure pénale : perquisitions numériques

Les perquisitions numériques obéissent aux règles générales de la perquisition (autorisation judiciaire, présence de témoins, procès-verbal) adaptées au numérique. Les enquêteurs peuvent saisir les équipements informatiques ou, plus couramment dans la pratique actuelle, réaliser des copies forensic sur place (moins perturbant pour l'activité de l'entreprise). Les réquisitions (articles 60-1 et 77-1-1 du CPP) permettent d'obtenir des données auprès des fournisseurs de services (opérateurs télécom, hébergeurs, éditeurs SaaS, fournisseurs cloud) sans saisie physique. Les scellés numériques garantissent l'intégrité des supports saisis : le hash calculé au moment de la saisie est l'équivalent numérique du scellé physique apposé sur un sac de preuves.

L'accès aux données chiffrées est un enjeu croissant. L'article 434-15-2 du Code pénal punit le refus de remettre une convention de chiffrement (clé ou mot de passe) demandée par l'autorité judiciaire, mais en pratique, si le suspect ne coopère pas et que la clé n'est pas récupérable par ailleurs, les données restent inaccessibles. D'où l'importance du dump mémoire à chaud (la clé de chiffrement BitLocker ou FileVault est en mémoire tant que le volume est déverrouillé).

#### 2.3 L'expert judiciaire

L'expert judiciaire en informatique est un technicien inscrit sur la liste d'une cour d'appel, mandaté par un magistrat (juge d'instruction, juge civil, ou tribunal de commerce) pour réaliser une expertise technique. Son statut est régi par la loi du 29 juin 1971 et le décret du 23 décembre 2004.

L'expert reçoit une mission précise définie par le magistrat (par exemple : « déterminer si des données ont été exfiltrées du SI de la société X entre le 1er janvier et le 31 mars 2026, identifier les moyens utilisés, et chiffrer le préjudice »). Il est tenu par cette mission et ne peut pas la dépasser sans autorisation. Il doit respecter le contradictoire : les parties sont informées des opérations d'expertise, peuvent y assister (ou se faire représenter par un conseil technique, souvent appelé « sapiteur »), et peuvent soumettre des « dires » (observations écrites auxquelles l'expert doit répondre dans son rapport). Le rapport d'expertise est soumis au juge, qui reste libre de le suivre ou non (l'expertise est un avis technique, pas un jugement).

L'inscription sur la liste des experts exige une compétence technique reconnue et une formation à la procédure judiciaire. L'expert prête serment. Sa responsabilité professionnelle est engagée en cas de faute. Dans le contexte forensic, l'expert doit maîtriser à la fois la technique (acquisition, analyse, outils) et la procédure (chaîne de custody, documentation, rédaction pour le contradictoire).

#### 2.4 Chaîne de custody

La chaîne de custody (chain of custody) retrace le parcours complet d'une pièce à conviction numérique, de sa collecte à sa présentation. Elle répond à une question simple : qui a eu accès à cette preuve, quand, et qu'en a-t-il fait ?

Chaque manipulation est documentée : qui a acquis le support (nom, qualité, organisme), à quelle date et heure (horodatage précis, fuseau horaire explicite), avec quel outil (nom, version, paramètres), quel est le hash d'intégrité (MD5 + SHA-256 calculés immédiatement après l'acquisition), où le support est-il stocké (lieu physique, conditions de sécurité), qui l'a transporté (nom, date, moyen de transport), et qui l'a analysé (nom, dates, outils utilisés).

Une rupture dans la chaîne de custody — un moment où la preuve n'était pas sous contrôle documenté — permet à la partie adverse de contester son intégrité. C'est la différence entre une preuve et un simple fichier. Le formulaire de chaîne de custody est en Annexe E.

> **Bonne pratique :** Même en investigation interne (sans perspective judiciaire immédiate), respecter les principes de la chaîne de custody dès le départ. La raison est pragmatique : de nombreuses investigations internes basculent en judiciaire quand l'ampleur des faits est révélée. Si les preuves ont été collectées sans rigueur au début, elles sont inexploitables devant un tribunal — et l'entreprise a perdu sa chance de judiciariser.

#### 2.5 Recevabilité de la preuve numérique

Pour qu'une preuve numérique soit acceptée par un tribunal, plusieurs conditions cumulatives doivent être remplies : **authenticité** (la preuve est bien ce qu'elle prétend être — hash d'intégrité vérifié), **fiabilité** (la méthode de collecte et d'analyse est reconnue et reproductible — outils documentés, méthodologie explicite), **pertinence** (la preuve est en rapport avec les faits litigieux — hors sujet = irrecevable), **proportionnalité** (la collecte n'a pas été disproportionnée par rapport à l'enjeu — imager le disque du DG pour un conflit sur l'utilisation de la photocopieuse serait disproportionné), et **loyauté** (obtenue par des moyens légaux — ce critère a été assoupli en matière civile par la jurisprudence de 2023, mais reste strict en matière pénale).

Un rapport forensic parfaitement rédigé mais fondé sur une acquisition non documentée sera contesté. Un rapport fondé sur une acquisition impeccable mais dont les conclusions dépassent les constatations sera également contesté. La rigueur doit être de bout en bout.

#### 2.6 Forensic judiciaire vs investigation interne : deux régimes

L'investigation interne (menée par l'entreprise elle-même ou un prestataire mandaté) et l'investigation judiciaire (menée sous mandat d'un magistrat) obéissent à des règles différentes. L'investigation interne n'a pas de pouvoir de réquisition (elle ne peut pas forcer un hébergeur AWS à communiquer les logs CloudTrail), elle est contrainte par le RGPD et le droit du travail (voir 2.7 et 2.8), mais elle bénéficie d'une flexibilité méthodologique plus grande (pas de scellés formels, pas de contradictoire obligatoire). L'investigation judiciaire dispose de pouvoirs étendus (perquisition, réquisition, scellés, mandat international) mais est soumise à un cadre procédural strict dont la violation entraîne la nullité des actes.

Le moment de la bascule est critique : quand les premiers résultats de l'investigation interne révèlent une infraction pénale (accès frauduleux — art. 323-1 CP, vol de données, abus de confiance, extorsion), l'entreprise doit décider si elle judiciarise (dépôt de plainte). À ce moment, les preuves collectées en interne doivent être exploitables judiciairement — d'où l'importance de la rigueur dès le début.

#### 2.7 RGPD et forensic

Le RGPD s'applique dès que l'investigation traite des données à caractère personnel — ce qui est presque toujours le cas (un dump de disque contient les fichiers personnels de l'utilisateur, un log contient des identifiants, un dump mémoire peut contenir des mots de passe en clair). La base légale la plus courante pour l'investigation forensic est l'intérêt légitime de l'entreprise à assurer la sécurité de son SI (article 6.1.f du RGPD). La proportionnalité est essentielle : ne collecter que ce qui est nécessaire à l'investigation, ne conserver les données que le temps de l'investigation et de l'éventuelle procédure, et documenter la justification. Le DPO doit être impliqué dès le début de l'investigation.

#### 2.8 Droit du travail et forensic interne

L'investigation forensic sur le poste d'un salarié est encadrée par le droit du travail et la jurisprudence de la chambre sociale de la Cour de cassation. Les grands principes : l'employeur peut accéder aux fichiers professionnels du salarié (présomption de caractère professionnel des fichiers sur le poste de travail de l'entreprise), mais les fichiers explicitement marqués « personnel » ou « privé » ne peuvent être ouverts qu'en présence du salarié ou après information (sauf si un événement particulier le justifie — menace sur la sécurité du SI). La charte informatique de l'entreprise (si elle existe, a été communiquée, et est à jour) encadre l'utilisation des outils et les modalités de contrôle. En pratique, impliquer le juridique et le DPO avant toute investigation sur un poste de salarié est indispensable — une preuve obtenue en violation du droit du travail est irrecevable dans une procédure disciplinaire.

#### 2.9 Normes internationales

Trois normes ISO encadrent les pratiques forensic. **ISO 27037** (2012) couvre l'identification, la collecte, l'acquisition et la préservation des preuves numériques — c'est la norme de référence pour la phase d'acquisition (comment manipuler un support, quand utiliser un write blocker, comment documenter). **ISO 27042** (2015) couvre l'analyse et l'interprétation des preuves — elle formalise les principes d'analyse objective et de documentation des résultats. **ISO 27043** (2015) définit le processus global d'investigation — de l'identification au rapport. Ces normes ne sont pas obligatoires mais constituent un cadre de bonnes pratiques reconnu internationalement. S'y conformer renforce la crédibilité de l'investigation et la recevabilité des preuves, tant en France qu'à l'international.

#### 2.10 Fil rouge — MUSIC BOX : le cadrage juridique

> **🔬 MUSIC BOX — Épisode 2**
>
> Vendredi soir, 18h30. Claire appelle le directeur juridique de NovaPharma, Maître Antoine Renard, et le DPO, Sandrine Leclerc.
>
> Questions immédiates : peut-on investiguer le poste de Julien Mallet ? Réponse : oui, c'est une investigation de sécurité sur un poste professionnel, pas une surveillance du salarié. La charte informatique autorise les contrôles de sécurité. Le DPO valide la base légale (intérêt légitime). Faut-il déposer plainte maintenant ? Pas encore — il faut d'abord comprendre l'étendue. Mais on préserve les preuves comme si on allait judiciariser.
>
> Le directeur juridique recommande de mandater une experte judiciaire inscrite pour sécuriser la chaîne de custody dès le début. Maître Élise Fournier (experte judiciaire en informatique, cour d'appel de Paris) est contactée — elle sera sur site samedi 9h. Son rôle : superviser les acquisitions, garantir la chaîne de custody, et être en mesure de témoigner de la rigueur méthodologique si l'affaire est judiciarisée.

---

### Chapitre 3 — Méthodologie forensic et posture d'enquêteur

#### 3.1 Le modèle en 5 phases

Toute investigation forensic suit un processus structuré en cinq phases séquentielles. Ce n'est pas un formalisme bureaucratique — c'est un cadre qui évite les erreurs fatales et qui structure la documentation.

**Phase 1 — Identification :** définir le périmètre de l'investigation, les systèmes concernés, les données volatiles (à acquérir en priorité), et les questions investigatives auxquelles l'investigation doit répondre. Output : liste des cibles, ordre d'acquisition, questions investigatives formulées. Piège principal : périmètre trop large (on se noie dans les données) ou trop étroit (on rate l'essentiel).

**Phase 2 — Préservation :** protéger les preuves contre toute altération. Ne pas éteindre une machine allumée (on perdrait la RAM). Ne pas allumer une machine éteinte (le boot modifie le disque). Isoler la machine du réseau (pour éviter que l'attaquant efface ses traces ou que des processus légitimes écrasent des preuves). Documenter l'état initial (photos de l'écran, des connexions, des équipements). Piège principal : modifier involontairement la preuve par une action bien intentionnée mais mal exécutée.

**Phase 3 — Acquisition :** copier les données de manière forensiquement valide. Image bit-à-bit du disque avec write blocker, dump de la mémoire vive, export des logs, capture réseau. Hash d'intégrité (MD5 + SHA-256) calculé sur le support source et sur l'image acquise — si les hash correspondent, l'intégrité est prouvée. Piège principal : oublier le write blocker, rater le dump RAM, ne pas hasher immédiatement. Détaillé en Partie II.

**Phase 4 — Analyse :** extraire les artefacts pertinents, construire une timeline chronologique, formuler des hypothèses, et les tester contre les évidences. C'est le cœur intellectuel du forensic. Piège principal : biais de confirmation, tunnel vision. Détaillé en Parties III et IV.

**Phase 5 — Présentation :** produire le rapport forensic et, le cas échéant, témoigner devant un tribunal ou une direction générale. Le rapport doit être compréhensible par un non-technicien tout en étant techniquement inattaquable. La distinction fait/déduction/hypothèse doit être explicite à chaque étape. Piège principal : rapport trop technique ou conclusions dépassant les constatations. Détaillé au Ch.26.

#### 3.2 Scoping strategy : définir le périmètre d'enquête

Le scoping est l'une des compétences les plus sous-estimées en forensic. La difficulté n'est pas seulement d'analyser, c'est de délimiter : quelles machines investiguer, quelle période couvrir, quels utilisateurs examiner, quels logs collecter, quel niveau de profondeur, et quand s'arrêter.

Les **questions investigatives** structurent le périmètre. Avant de toucher un clavier, l'investigateur formule les questions auxquelles l'investigation doit répondre : comment l'attaquant a-t-il pénétré (vecteur d'accès initial) ? Quand l'intrusion a-t-elle commencé ? Quels systèmes ont été compromis (mouvement latéral) ? Quelles données ont été impactées (exfiltration, modification, destruction) ? L'attaquant est-il encore présent ? Qui est l'attaquant (attribution, si possible) ? Ces questions orientent chaque action d'investigation.

**Délimiter le périmètre** implique des choix concrets. Quelles machines : on commence par les machines directement concernées par l'alerte, puis on élargit en fonction des découvertes (mouvement latéral, même IoC trouvé sur d'autres machines). Quelle période : la fenêtre temporelle initiale est définie par l'alerte, mais l'investigation révèle souvent que l'intrusion remonte beaucoup plus loin (dans MUSIC BOX, l'alerte est à J, mais l'intrusion initiale est à J-60). Quels logs : dépend de la rétention réelle (pas la rétention théorique configurée, mais ce qui est effectivement disponible et exploitable).

Le **piège du scope creep** : chaque découverte ouvre de nouvelles pistes. Un bon investigateur distingue les pistes prioritaires (qui répondent aux questions investigatives) des pistes secondaires (intéressantes mais non essentielles). Il documente les pistes non suivies pour éventuelle investigation ultérieure (avec la mention « piste identifiée, non suivie dans le cadre du scoping actuel — recommandation : investiguer ultérieurement si nécessaire »).

**Quand s'arrêter :** l'investigation est terminée quand toutes les questions investigatives ont reçu une réponse (même si la réponse est « indéterminable avec les données disponibles »), que la couverture temporelle est suffisante, et que la timeline est cohérente. La tentation du perfectionnisme (« et si on regardait aussi ce serveur ? ») doit être résistée si elle ne répond à aucune question investigative ouverte.

**Triage vs investigation complète — arbre de décision :** le choix entre triage rapide (KAPE, Velociraptor — artefacts ciblés, résultats en heures) et investigation complète (image disque + dump RAM + capture réseau + timeline exhaustive — résultats en jours à semaines) dépend de la gravité confirmée, de la perspective judiciaire, de la sensibilité des données, et des moyens disponibles. La bascule du triage vers l'investigation complète se fait quand la gravité est confirmée (vol de données, compromission étendue, insider), quand des données réglementées sont concernées (RGPD, santé, défense), ou quand la direction souhaite judiciariser.

#### 3.3 Posture intellectuelle de l'enquêteur

Le forensic exige une posture intellectuelle rigoureuse qui va au-delà de la maîtrise technique des outils.

Le **doute méthodique** : l'analyste ne prend rien pour acquis. Un timestamp peut être falsifié (timestomping). Un log peut être incomplet (rotation, effacement). Un artefact peut être un planted evidence (fausse preuve déposée par l'attaquant pour incriminer un tiers ou brouiller les pistes). Chaque constatation est vérifiée contre au moins une source indépendante quand c'est possible.

Les **hypothèses alternatives** : l'analyste formule plusieurs hypothèses et les teste toutes, pas seulement celle qui semble la plus probable. Si l'hypothèse initiale est « le salarié Julien Mallet a exfiltré les données », l'analyste doit aussi tester « le compte de Julien Mallet a été compromis par un attaquant externe ». Le biais de confirmation — la tendance à chercher les données qui confirment l'hypothèse préférée et à ignorer celles qui la contredisent — est le piège le plus dangereux du forensic (développé au Ch.11).

La **distinction fait / déduction / hypothèse** : l'analyste distingue rigoureusement ce qu'il constate (« le fichier X a été supprimé le 3 mars à 14h32 » — fait, observable dans la MFT), ce qu'il en déduit (« la suppression a été effectuée par le compte svc-backup, car c'est le seul compte actif sur la machine à cette heure selon les Event Logs » — déduction logique), et ce qu'il suppose (« cette suppression est intentionnelle et liée à la compromission » — hypothèse, qui nécessite des évidences supplémentaires pour être confirmée). Le rapport forensic doit rendre cette distinction explicite à chaque étape.

#### 3.4 Documentation continue

La documentation est un livrable continu, pas un exercice de fin d'investigation. Le **journal d'investigation** (case log) enregistre chronologiquement chaque action de l'investigateur : heure, action, outil utilisé, résultat, décision. Le **formulaire de chaîne de custody** suit chaque pièce à conviction. Les **photos** documentent l'état physique des équipements (avant de débrancher un câble, on photographie). Les **captures d'écran horodatées** documentent les étapes de l'analyse. Sans documentation, l'investigation la plus brillante est irrecevable (en judiciaire) et irrépétable (en interne).

#### 3.5 Les 10 erreurs fatales

Ces erreurs invalident une preuve ou égarent une investigation : (1) éteindre une machine allumée avant le dump RAM, (2) allumer une machine éteinte sans write blocker, (3) oublier de hasher avant ET après l'acquisition, (4) travailler sur l'original au lieu de la copie, (5) ne pas documenter ses actions en temps réel, (6) ignorer les fuseaux horaires lors de la corrélation de timestamps, (7) se fixer sur la première hypothèse sans en tester d'autres, (8) ignorer les sources de preuves volatiles (connexions réseau, processus en mémoire), (9) sous-estimer l'anti-forensics (l'attaquant a pu falsifier des timestamps, supprimer des logs, ou déposer de fausses preuves), et (10) produire un rapport dont les conclusions dépassent les constatations.

#### 3.6 Fil rouge — MUSIC BOX : le scoping

> **🔬 MUSIC BOX — Épisode 3**
>
> Scoping initial chez NovaPharma. Claire formule 4 questions investigatives :
> 1. Comment l'attaquant a-t-il pénétré le SI ? (vecteur d'accès initial)
> 2. Quels systèmes sont compromis au-delà du poste WKS-RD-047 ? (mouvement latéral)
> 3. Des données ont-elles été exfiltrées, et si oui, lesquelles et quel volume ? (impact sur la propriété intellectuelle)
> 4. L'attaquant est-il encore présent dans le réseau ? (urgence de confinement)
>
> Machines prioritaires : WKS-RD-047 (poste compromis), SRV-RD-01 (serveur R&D Linux, données de recherche NP-427), DC01 (contrôleur de domaine — vérifier si l'AD est compromis).
>
> Fenêtre temporelle : J-90 à J (on prend large pour ne pas rater le début de l'intrusion — les logs du SIEM couvrent 12 mois, les logs proxy 6 mois).
>
> Décision : triage immédiat (dump RAM de WKS-RD-047 + collecte KAPE sur les 3 machines + export des logs AD) ce soir. Image disque complète de WKS-RD-047 et du serveur R&D samedi matin avec l'experte judiciaire. Perspective : probable judiciarisation si vol de données R&D confirmé.

---

### Chapitre 4 — Environnement technique et outils fondamentaux

#### 4.1 Le lab forensic

Un laboratoire forensic est un environnement contrôlé dédié à l'analyse des preuves numériques. Son objectif est double : protéger l'intégrité des preuves et fournir les outils nécessaires à l'analyse.

Le **matériel** comprend des write blockers matériels (Tableau/Guidance T356789iu, CRU WiebeTech — qui empêchent physiquement toute écriture sur le support source, indépendamment du logiciel), des duplicateurs forensic (Logicube Falcon Neo, Atola TaskForce — pour les acquisitions rapides avec hashing intégré), et des stations d'analyse puissantes (minimum 64 Go de RAM pour l'analyse mémoire avec Volatility, stockage rapide NVMe pour les images disque qui font souvent plusieurs centaines de Go, processeurs multi-cœurs pour le traitement de Super Timelines qui peuvent contenir des millions d'événements).

Le **réseau du lab** est isolé du réseau de production (on ne connecte jamais un support potentiellement compromis au réseau d'entreprise). Le stockage des preuves est sécurisé : coffre physique fermé à clé (ou salle avec contrôle d'accès et vidéosurveillance pour les investigations judiciaires), registre d'accès documentant chaque entrée/sortie de support.

#### 4.2 Distributions forensic

Plusieurs distributions Linux pré-configurées facilitent le travail forensic. **SIFT Workstation** (SANS Investigative Forensic Toolkit), maintenue par le SANS Institute, est la référence pédagogique et professionnelle — basée sur Ubuntu, elle contient Autopsy, Volatility, Plaso, RegRipper, les outils Eric Zimmerman (via Wine ou natifs), et des centaines d'outils spécialisés. **Tsurugi Linux** est une distribution très complète d'origine japonaise/italienne. **CSI Linux** est orientée investigation et OSINT. **Kali Linux**, connue pour le pentest, inclut un méta-paquet forensic (`kali-tools-forensics`). **REMnux** est spécialisée dans l'analyse de malware.

Le choix de la distribution est moins important que la maîtrise des outils qu'elle contient. Un analyste expert avec un Ubuntu nu et les bons outils installés sera plus efficace qu'un débutant avec la distribution la plus complète.

#### 4.3 Outils open source vs commerciaux

Les outils forensic se répartissent en deux catégories. Les **outils open source** (Autopsy/The Sleuth Kit pour le disk forensics, Volatility 3 pour le memory forensics, Wireshark/Zeek pour le network forensics, Plaso pour la Super Timeline, RegRipper pour le registre Windows) sont gratuits, auditables (leur code source est vérifiable — argument important pour le contradictoire), et largement utilisés tant par les forces de l'ordre que par les cabinets privés. Les **outils commerciaux** (EnCase d'OpenText, FTK d'Exterro, X-Ways Forensics, Magnet AXIOM, Cellebrite UFED pour le mobile) offrent des interfaces intégrées, un support commercial, et sont parfois requis ou préférés par certaines juridictions ou certains clients institutionnels.

En 2025-2026, la tendance est clairement à la convergence : Autopsy est devenu une plateforme mature capable de rivaliser avec les outils commerciaux pour le disk forensics, Volatility 3 est la référence incontestée pour le memory forensics (même les éditeurs commerciaux l'utilisent comme moteur), et les outils Eric Zimmerman ont transformé le Windows forensics en fournissant des parsers spécialisés de qualité professionnelle, gratuitement.

#### 4.4 La suite Eric Zimmerman — l'outillage Windows forensics de référence

Eric Zimmerman est un ancien agent du FBI devenu formateur SANS, qui a développé une suite d'outils de parsing forensic pour Windows, devenus la référence de facto en 2025-2026. Ces outils parsent les artefacts Windows bruts et produisent des résultats structurés (CSV) exploitables dans Timeline Explorer ou un tableur.

**MFTECmd** parse la $MFT (Master File Table) NTFS et produit une timeline de tous les fichiers avec leurs timestamps $SI et $FN — indispensable pour détecter le timestomping. **PECmd** parse le Prefetch — historique d'exécution des programmes avec dates, nombre d'exécutions, et fichiers chargés. **LECmd** parse les fichiers LNK (raccourcis) — révèlent les fichiers récemment ouverts, les chemins réseau accédés, les volumes USB connectés. **SBECmd** (ShellBags Explorer) parse les ShellBags du registre — historique complet de la navigation dans l'explorateur de fichiers. **JLECmd** parse les Jump Lists — fichiers récemment ouverts par application. **EvtxECmd** parse les Event Logs Windows (format evtx) en CSV structuré — beaucoup plus rapide et flexible que l'Event Viewer natif. **RECmd** parse le registre Windows en ligne de commande avec des batch files prédéfinies. **AmcacheParser** parse l'Amcache — historique des programmes exécutés avec hash SHA1. **AppCompatCacheParser** parse le ShimCache — historique des programmes avec timestamps. **SrumECmd** parse la base SRUM — consommation réseau et CPU par processus. **Timeline Explorer** est l'interface de visualisation qui permet de filtrer, trier, et analyser les CSV produits par tous les outils ci-dessus.

Ces outils sont distribués gratuitement via le site d'Eric Zimmerman (ericzimmerman.github.io) et sont pré-installés dans SIFT Workstation. Ils sont utilisés tout au long de la Partie IV.

#### 4.5 Hashing et vérification d'intégrité

Le hashing est le mécanisme fondamental de vérification d'intégrité en forensic. Un hash est une empreinte numérique de taille fixe calculée à partir de l'intégralité des données : si un seul bit change, le hash change complètement. **MD5** (128 bits) est rapide mais théoriquement vulnérable aux collisions (deux fichiers différents produisant le même hash — démontré en 2004). **SHA-256** (256 bits) est plus robuste et considéré comme sûr. La pratique recommandée est le **double hashing** (MD5 + SHA-256) : les deux doivent correspondre. La probabilité que deux fichiers différents produisent le même MD5 ET le même SHA-256 est négligeable.

Les outils standards sont `md5sum` et `sha256sum` (Linux), `Get-FileHash` (PowerShell), et `hashdeep` (multi-hash, récursif — utile pour hasher des répertoires entiers). Chaque acquisition doit être accompagnée de ses hash, notés dans le journal d'investigation et le formulaire de chaîne de custody.

#### 4.6 Outils d'acquisition et formats d'images

L'acquisition bit-à-bit d'un disque se fait avec des outils spécifiques. La commande **dd** (Linux) est l'outil historique : `dd if=/dev/sdX of=/path/image.raw bs=4M status=progress` — simple, universel, mais sans hashing intégré ni barre de progression utile. **dc3dd** (développé par le DoD américain) ajoute le hashing intégré, le logging, et la gestion des erreurs. **FTK Imager** (gratuit, Windows et Linux) est l'outil le plus utilisé en entreprise : interface graphique, hashing automatique, support des formats E01 et AFF4, preview du contenu avant acquisition. **Guymager** (Linux, open source) offre une acquisition multi-threadée rapide avec interface graphique.

Les formats d'images : le format **raw** (dd) est une copie exacte, secteur par secteur — simple mais volumineux (taille = taille du disque source) et sans métadonnées intégrées. Le format **E01** (EnCase/Expert Witness Format) compresse les données (réduction de 30-50 % typiquement), intègre les métadonnées (hash, notes, informations de case), et permet la segmentation en fichiers multiples — c'est le format le plus utilisé en forensic. Le format **AFF4** (Advanced Forensic Format 4) est un format ouvert moderne, conteneurisé, qui supporte le stockage de multiples types d'évidences dans un seul conteneur.

#### 4.7 Outils de triage rapide

Les outils de triage collectent rapidement les artefacts les plus pertinents sans image complète du disque. **KAPE** (Kroll Artifact Parser and Extractor) utilise des targets (définitions de quels fichiers/artefacts collecter) et des modules (parsers pour analyser les artefacts collectés). La commande `kape.exe --tsource C: --tdest E:\Output --target KapeTriage` collecte en quelques minutes les Event Logs, le registre, le Prefetch, l'Amcache, le ShimCache, la $MFT, le SRUM, les historiques navigateur, et d'autres artefacts clés. **Velociraptor** (open source, développé initialement par Google) est un agent déployable sur tout un parc : il permet de lancer des collectes et des hunts à distance sur des centaines de machines simultanément via des requêtes VQL (Velociraptor Query Language). **DFIR-ORC** (développé par l'ANSSI) est un outil de collecte français optimisé pour les grands déploiements dans les OIV.

#### 4.8 Environnement d'analyse

L'analyse se fait toujours sur une machine dédiée, jamais sur la machine source. L'environnement standard est une VM isolée du réseau, avec des snapshots pour pouvoir revenir en arrière si une manipulation corrompt l'état de l'analyse. Les images forensic sont montées en lecture seule dans la VM (sous Linux : `mount -o ro,loop,noexec image.raw /mnt/evidence`). Arsenal Image Mounter (Windows) permet de monter des images E01 comme des disques virtuels accessibles en lecture seule. La configuration de l'environnement (version des outils, options utilisées, paramètres de montage) est documentée pour la reproductibilité.

#### 4.9 Fil rouge — MUSIC BOX : le lab et l'acquisition initiale

> **🔬 MUSIC BOX — Épisode 4**
>
> Vendredi soir, 19h00. L'équipe met en place le dispositif d'investigation. Claire utilise sa station forensic portable (laptop avec 64 Go de RAM, 4 To NVMe, SIFT Workstation en VM, write blocker Tableau T35es).
>
> **Acquisition mémoire (priorité absolue) :** DumpIt est exécuté sur WKS-RD-047 (machine allumée, session utilisateur active). Dump RAM : 32 Go, 14 minutes. Hash SHA-256 calculé immédiatement : `a7f3e2...`. Documenté dans le journal d'investigation et le formulaire de chaîne de custody.
>
> **Triage KAPE :** lancé sur WKS-RD-047 en parallèle du dump. Target : KapeTriage. Résultat : tous les artefacts Windows critiques collectés en 8 minutes. Hash calculé sur l'archive.
>
> **Acquisition disque prévue samedi matin** avec l'experte judiciaire — image E01 via FTK Imager avec write blocker matériel.
>
> **Serveur R&D Linux (SRV-RD-01) :** la machine est en production et ne peut pas être éteinte (les expériences en cours seraient perdues). Décision : acquisition logique à chaud — copie des logs (`/var/log/`), de l'historique bash, du crontab, des authorized_keys SSH, et des fichiers récemment modifiés. Image disque reportée à un arrêt de maintenance planifié (dans 5 jours).
>
> Choix du format : E01 pour l'image disque (compression, métadonnées intégrées, compatibilité Autopsy). Raw pour le dump mémoire (compatibilité Volatility 3).

---
