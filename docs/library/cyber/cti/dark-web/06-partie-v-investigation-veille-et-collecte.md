---
title: PARTIE V — INVESTIGATION, VEILLE ET COLLECTE
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
chapter: 6
chapters: 10
---

> **Ce que cette partie apprend.** Conduire une investigation dark web de manière professionnelle — cadre juridique et éthique, OPSEC de l'analyste, méthodes de collecte, workflow d'investigation d'un data leak, pivoting OSINT, veille continue, préservation des preuves.
>
> **Ce qu'elle ne couvre pas.** Les méthodes avancées d'analyse et d'attribution (Partie VI), les cas d'usage spécifiques par secteur (Partie VII), les études de cas complètes (Partie VIII).
>
> **Ce que vous saurez faire après cette partie.** Conduire une enquête OSINT sur le dark web en respectant le cadre légal français/européen, bâtir et maintenir une persona, investiguer un leak de données de manière structurée, préserver les preuves de manière admissible, et construire un programme de veille dark web durable.

---

## Chapitre 22 — Cadre juridique, éthique et sécurité de l'analyste

Avant tout outil technique, l'analyste dark web doit maîtriser le cadre légal qui encadre son activité. Consulter un forum cybercriminel n'est pas illégal en soi — mais certains actes d'investigation le sont, et d'autres sont dans une **zone grise** qu'il faut savoir naviguer.

### 22.1 Le cadre français

**Code pénal articles 323-1 à 323-8**. Atteinte aux STAD (systèmes de traitement automatisé de données). Incrimine :
- **323-1** : l'accès ou le maintien frauduleux dans un STAD (maximum 3 ans d'emprisonnement et 100 000 € d'amende ; circonstances aggravantes si suppression/modification de données : 5 ans, 150 000 €).
- **323-2** : l'entrave du fonctionnement d'un STAD (7 ans, 300 000 €).
- **323-3** : la modification frauduleuse de données (7 ans, 300 000 €).
- **323-3-1** : la détention et la diffusion d'outils conçus pour commettre ces infractions — **article clé pour l'analyste**, qui encadre la manipulation d'outils offensifs.

**Loi du 24 juillet 2015 sur le renseignement** et articles associés dans le Code de la sécurité intérieure : cadre des activités de renseignement encadrées par l'État. L'analyste privé n'opère pas sous ce régime, mais les agences partenaires (DGSI, DGSE) peuvent.

**Loi Informatique et Libertés + RGPD**. La collecte et le traitement de données personnelles exposées (même exposées par un attaquant) restent soumis aux régimes de protection. Un analyste qui capture un dump contenant des données personnelles doit gérer ce stock selon les règles applicables — base légale de traitement, minimisation, sécurisation, suppression post-exploitation.

**Code de procédure pénale article 40**. Tout fonctionnaire qui, dans l'exercice de ses fonctions, acquiert la connaissance d'un crime ou d'un délit, est tenu d'en aviser le procureur. Un analyste fonctionnaire (service public, OIV) peut être concerné — même en secteur privé, la logique de signalement est structurante.

**Cadre ANSSI / OIV**. Les OIV ont obligation de notification d'incidents significatifs à l'ANSSI. Les prestataires PASSI/PDIS/PRIS opèrent sous qualification.

### 22.2 Le cadre européen

**Directive NIS 2 (UE 2022/2555)**. Transposée en France et dans tous les États membres. Obligations de cybersécurité et notification pour les entités essentielles et importantes dans 18 secteurs. Les analystes opérant pour ces entités ont un rôle dans la posture de notification.

**RGPD**. Régit les données personnelles. Les dumps contenant données personnelles doivent être traités avec base légale (intérêt légitime de l'investigation, mission de service public, etc.), minimisation, sécurité.

**Convention de Budapest sur la cybercriminalité (2001) et ses protocoles additionnels**. Cadre de coopération internationale en matière cybercriminalité. Protocole additionnel de mai 2022 facilite l'accès transfrontière à la preuve électronique.

**EU Cyber Solidarity Act (2024)**. Crée un réseau européen de SOC et un mécanisme de réponse d'urgence pour incidents cyber transfrontaliers.

**EU Cyber Sanctions Regime**. Sanctions ciblées contre cyberacteurs malveillants.

### 22.3 Les zones grises

Plusieurs activités sont **dans la zone grise** — techniquement légales mais nécessitent prudence.

**Consulter des forums criminels**. Légal en tant que tel. La simple consultation d'un contenu publiquement accessible (même sur .onion) n'est pas une infraction.

**Créer un compte sur un forum criminel**. Nécessaire pour accéder aux zones fermées. Légal, avec précautions — le pseudonyme ne doit pas être utilisé pour commettre des infractions (solliciter des services criminels, acheter des données, participer à des discussions opérationnelles).

**Télécharger des échantillons**. Zone sensible. Télécharger un fichier contenant des données personnelles (même publiquement exposées par l'attaquant) peut contrevenir au RGPD. Télécharger du malware pour analyse est **généralement accepté** dans un cadre de recherche, mais la détention de malware est encadrée par l'article 323-3-1. Pratique recommandée : n'en télécharger que ce qui est strictement nécessaire à la mission, documenter la justification, sécuriser le stock, supprimer après exploitation.

**Télécharger des données volées**. Encore plus sensible. Principe : **nécessité et proportionnalité**. Télécharger un échantillon pour authentification est différent de télécharger l'intégralité d'un dump.

**Télécharger du CSAM**. **Interdit absolument**. Même dans un cadre d'investigation, la détention est criminelle. Les investigations CSAM relèvent des autorités judiciaires avec cadre spécifique (pornographie enfantine, articles 227-23 et suivants du Code pénal).

**Payer pour obtenir de l'information**. Dépend du contexte. Payer un droit d'entrée forum pour investigation : généralement accepté avec autorisation hiérarchique et traçabilité. Acheter des données volées : **risqué** — peut constituer recel. La DGSI accompagne ces cas.

**Contacter un vendeur en se faisant passer pour acheteur**. Zone grise classique. Généralement accepté pour investigation avec encadrement, mais peut constituer provocation dans certains cadres — la jurisprudence française est restrictive sur la **provocation à la commission d'infraction**. L'analyste doit se présenter comme acheteur potentiel pour obtenir des échantillons, mais ne pas pousser le vendeur à augmenter son activité criminelle.

**Infiltrer un groupe comme membre actif**. Réservé aux forces de l'ordre avec mandat judiciaire. Un analyste privé qui « infiltrerait » un groupe criminel dépasse largement le cadre légal.

### 22.4 L'éthique professionnelle

Au-delà de la légalité stricte, plusieurs principes éthiques s'appliquent.

**Minimisation**. Collecter le minimum nécessaire à la mission. Ne pas stocker plus que ce qu'on exploite. Supprimer après exploitation.

**Non-prolifération**. Ne pas rediffuser les données collectées au-delà du cercle justifié. Un dump contenant des données personnelles ne se partage pas lightly, même entre analystes.

**Non-exploitation abusive**. Les données volées peuvent contenir des informations sensibles (vie privée, communications intimes, données médicales). L'analyste ne les exploite qu'au strict nécessaire à la mission, pas par curiosité.

**Transparence hiérarchique**. Les choix d'investigation sensibles (contact vendeur, paiement, téléchargement) sont documentés et autorisés par la hiérarchie.

**Respect des victimes**. Les victimes de breach sont des personnes. Contact avec elles doit respecter leur dignité — ni sensationnaliser, ni exploiter leur détresse.

**Coopération avec autorités**. Si l'investigation révèle des infractions graves (trafic humain, CSAM, terrorisme), signalement obligatoire aux autorités compétentes. Le secret professionnel n'est pas absolu.

### 22.5 La sécurité personnelle de l'analyste

L'investigation dark web expose à plusieurs risques **personnels**.

**Risque technique**. Compromission du poste d'investigation via malware piégé. Les fichiers téléchargés, les liens cliqués, les sites visités peuvent contenir des exploits ciblant les analystes. Mesures : machine dédiée, VM jetables (Whonix + VM d'exécution), pas de comptes personnels sur la machine.

**Risque d'identification par les cibles**. Les acteurs malveillants font de la contre-surveillance. Un analyste qui utilise ses accès personnels, qui lit systématiquement les posts d'un vendeur spécifique, qui pose des questions révélatrices — peut être identifié comme investigateur. Conséquences : ciblage du compte d'investigation, tentative d'identification réelle (dox), voire menaces physiques dans les cas extrêmes.

**Risque juridique transfrontalier**. Un analyste français qui interagit avec un vendeur russe via un forum hébergé aux Pays-Bas peut techniquement tomber sous multiple juridictions. En pratique, si l'activité est légale en France et dans le cadre d'une mission professionnelle, le risque est faible, mais pas nul.

**Risque de manipulation psychologique**. L'immersion dans l'écosystème dark web expose à des contenus difficiles (violences, CSAM accidentellement croisé, narratifs extrêmes). L'analyste doit être soutenu par son organisation — debriefing psychologique, rotation des missions, limitation de l'exposition aux contenus traumatisants.

**Risque de compromission éthique**. Dérive possible — un analyste exposé longtemps à l'écosystème peut développer de l'empathie pour les cibles, se laisser tenter par des relations personnelles avec des sources, perdre la distance professionnelle. Supervision hiérarchique et rotation atténuent.

### 22.6 Fil rouge — DARKSTREAM : encadrement légal

> **🌐 DARKSTREAM — Épisode 12 : cadrage DGSI**
>
> Lucas prépare son premier contact avec aero_source. Avant action, validation DGSI obligatoire.
>
> Réunion avec l'officier DGSI référent. Points validés :
> - **Contact OK** sous persona « mapletech » — acheteur technologique intéressé par specs aéronautiques. Légende crédible.
> - **Pas d'engagement ferme d'achat** — Lucas peut exprimer intérêt, demander échantillons, négocier indirectement, mais jamais confirmer la transaction. La DGSI précise : « ne provoquez pas la vente, cherchez à comprendre ».
> - **Pas de téléchargement de l'intégralité** — échantillons acceptés pour authentification, le dump complet non.
> - **Remontée bi-hebdomadaire** : Lucas briefe la DGSI tous les 3-4 jours sur l'évolution.
> - **Arrêt immédiat** si Lucas perçoit un risque d'exposition (persona identifiée comme analyste, menaces, contre-enquête).
> - **Pas d'achat** des données. Si aero_source impose paiement pour les échantillons (rare), arrêt de l'investigation de ce côté.
>
> Tous les échanges XMPP sont archivés (logs chiffrés chez Athéna, accessibles DGSI). Capture d'écran au fur et à mesure. Hash des fichiers téléchargés. Documentation exhaustive du cheminement d'investigation.
>
> Cette rigueur procédurale est **la condition de l'utilisabilité** de ce que Lucas produira. Un rapport sans chain of custody documentée n'a aucune valeur judiciaire. Un rapport trop fondé sur des actions juridiquement douteuses peut être écarté.

---

## Chapitre 23 — OPSEC opérationnelle de l'investigation

L'**OPSEC** (Operations Security) de l'analyste dark web est le pilier de la réussite d'une investigation. Une OPSEC défaillante expose l'analyste, compromet la mission, et peut mettre en danger les sources coopératives ou les collègues.

### 23.1 La séparation des univers

Principe fondamental : **séparation totale** entre l'univers personnel de l'analyste, son univers professionnel hors investigation, et son univers d'investigation.

**Machines séparées**. Ordinateur dédié à l'investigation dark web. Jamais utilisé pour activités personnelles (réseaux sociaux, emails, banque), jamais pour activités professionnelles générales (mails corporate, documents, visioconférences). Configuration minimale : OS dédié (Whonix, Tails), navigateur Tor Browser uniquement, outils strictement nécessaires.

**Comptes séparés**. Emails jetables (protonmail, ctemplar, services .onion) pour les comptes d'investigation. Jamais de lien avec emails corporate ou personnels.

**Identités séparées**. Les personas d'investigation (pseudonymes, handles Telegram, JID XMPP) sont **strictement cloisonnées** de l'identité réelle de l'analyste. Aucune réutilisation d'un pseudo entre personas. Aucun lien traçable entre les personas et l'identité réelle.

**Financier séparé**. Wallets crypto dédiés à l'investigation, financés par un circuit professionnel (exchange corporate avec KYC de l'entreprise, pas de l'analyste personnellement). Transactions tracées par l'entreprise pour audit.

**Temporel séparé**. L'investigation se fait dans des créneaux dédiés. Le mélange entre activités dark web et tâches personnelles dans le même créneau temporel crée des risques de contamination (oubli de fermer Tor Browser avant d'ouvrir son email personnel, etc.).

### 23.2 La persona

Une **persona** est un personnage fictif construit pour l'investigation. Elle doit être **crédible** et **cohérente**.

**Éléments de la persona** :
- **Pseudonyme** : unique, ne ressemble pas à d'autres pseudonymes utilisés par l'analyste (pas de pattern identifiable).
- **Histoire** : d'où vient-elle ? quel métier ? quelles compétences ? quels intérêts ?
- **Langue** : style d'écriture cohérent avec l'origine prétendue. Un analyste français qui joue un persona russophone doit maîtriser les codes linguistiques russophones — sinon se cantonne à l'anglais.
- **Niveau technique** : si persona « script kiddie » prétend avoir peu de skills, elle ne doit pas poser des questions trop sophistiquées. Si persona « pro » doit comprendre les concepts avancés.
- **Activité historique** : la persona a-t-elle des posts dans des forums parallèles ? Une présence sur Telegram ? Un historique crédible ?
- **Infrastructure cohérente** : serveur XMPP utilisé, méthodes de paiement préférées, heures d'activité.

**Construction préalable**. Une persona utilisable pour une investigation sérieuse prend **3-6 mois** à construire — inscription sur un forum, posts graduels, participation communautaire, construction d'une histoire minimale. Les personas « jetables » (créées le jour, utilisées le lendemain) sont facilement identifiables comme non-authentiques.

**Maintenance**. Une persona doit être **active** même quand pas utilisée sur une investigation active. Posts occasionnels, participation à des discussions générales. Une persona inactive pendant 6 mois puis réactivée pour une enquête ciblée déclenche la méfiance.

**Burnability**. Accepter qu'une persona peut être brûlée. En ce cas, ne pas chercher à la « sauver » — l'abandonner, en construire une nouvelle. Toute tentative de réactiver une persona suspecte aggrave l'exposition.

### 23.3 La sécurité technique

**Tor Browser en mode Safest**. JavaScript désactivé. Beaucoup de fonctionnalités cassées, mais pas d'exécution de code exploitable. Certains sites nécessitent JS — évaluer le risque au cas par cas, activer temporairement si site considéré sûr.

**VM isolée**. Toute interaction au-delà de la simple navigation (téléchargements, fichiers exécutables) dans une VM jetable. Snapshot avant action, restauration après. Ne jamais exposer l'OS hôte à du contenu dark web non-simple-HTML.

**Pas de JavaScript actif sur sites suspects**. Les NIT (Network Investigative Techniques) et les exploits navigateur exploitent JS (Ch.30). Mode Safest le bloque ; si on l'active, on doit comprendre les risques.

**Pas de WebRTC**. Tor Browser désactive WebRTC ; ne pas l'activer manuellement. WebRTC peut leaker l'IP réelle.

**Pas de plugins**. Flash, Java, PDF readers intégrés — désactivés ou absents. Tor Browser configure ça par défaut.

**Vérification des .onion**. Les adresses .onion sont longues (56 caractères v3). Les scammers créent des adresses similaires via vanity generation. **Toujours vérifier l'adresse complète**, via source fiable (site officiel du service, post établi sur forum réputé, backup en dur pré-validé).

**Hashing des fichiers**. Tout fichier téléchargé est hashé (SHA-256 minimum) avant ouverture. Le hash sert de référence pour la chain of custody et pour vérifier que le fichier n'a pas été altéré entre collecte et analyse.

**Pas de métadonnées**. Les screenshots sont pris puis **strippés de métadonnées** (exiftool). Les documents créés pendant l'investigation (notes, rapports) ne doivent pas contenir de métadonnées personnelles (nom d'auteur dans Word, etc.).

### 23.4 Les erreurs classiques

**Réutilisation de pseudonymes**. Un analyste qui utilise le même pseudo sur plusieurs enquêtes risque la corrélation. Les forums observent les patterns — un pseudo qui demande des échantillons de données industrielles aerospace sur un forum et des échantillons bancaires sur un autre est soit un acheteur éclectique, soit un investigateur.

**Corrélation temporelle**. Pseudo actif aux heures ouvrables françaises systématiquement. Indique fuseau horaire Europe occidentale, incompatible avec un persona prétendument russophone.

**Fuites linguistiques**. Expressions françaises dans un persona anglophone, conventions de dates françaises (DD/MM) dans un persona américain (MM/DD), traduction littérale d'idiomes français.

**Over-sharing**. Par nervosité ou tentative de crédibilité, l'analyste donne trop d'infos sur sa « persona » — détails sur son entreprise fictive, anecdotes personnelles vérifiables. Chaque détail est une surface d'attaque pour la contre-investigation.

**Accès depuis infrastructure corporate**. L'analyste qui accède à Tor depuis l'IP corporate de son bureau (même via VPN Tor) expose son organisation. Poste dédié dans un réseau isolé recommandé.

**Comptes personnels sur la machine d'investigation**. Un analyste qui check ses emails personnels sur la machine dark web compromet tout le cloisonnement.

**Documentation défaillante**. Une investigation sans logs précis de chaque action (heure, URL visitée, fichier téléchargé, hash, pseudonyme utilisé) ne produit pas de preuves utilisables.

**Abandon de prudence sur la durée**. Au début de l'enquête, OPSEC rigoureuse. Après 3 mois, fatigue, relâchement. L'erreur survient plus tard, pas au début.

### 23.5 Le programme OPSEC d'équipe

Pour une équipe CTI, l'OPSEC doit être **institutionnelle**, pas individuelle.

**Procédures documentées**. Playbook formalisé : comment créer une persona, comment ouvrir un compte, comment gérer les paiements, comment capturer les preuves, comment documenter.

**Peer review**. Chaque action sensible (création de persona, premier contact vendeur, téléchargement d'échantillon) est validée par un pair ou la hiérarchie.

**Supervision**. Un responsable CTI a visibilité sur les investigations en cours, alloue les personas, valide les escalades.

**Formation continue**. L'OPSEC évolue (nouvelles techniques de dé-anonymisation, nouveaux pièges). Formation périodique, veille sur les techniques offensives utilisées contre les analystes.

**Incident response OPSEC**. Plan d'action en cas de compromission de persona — quoi abandonner, quoi sauvegarder, qui prévenir, comment communiquer.

**Débriefing psychologique**. Les missions longues dans l'écosystème dark web sont éprouvantes. Sessions régulières avec psychologue ou pair expérimenté.

---

## Chapitre 24 — Naviguer et collecter : méthodes, outils, limites

Aspect pratique : comment on navigue effectivement sur le dark web, quels outils on utilise, et quelles sont les limites techniques et méthodologiques.

### 24.1 L'outillage de base

**Tor Browser** : navigateur de référence. Basé sur Firefox ESR, hardened, en mode Safest pour l'investigation. À télécharger **uniquement** depuis torproject.org (ou ses miroirs officiels).

**Tails** : distribution Linux live. Démarre sur clé USB, ne laisse aucune trace sur la machine. Recommandée pour les investigations les plus sensibles.

**Whonix** : architecture en deux VM (Gateway + Workstation). Isolation forte. Recommandée pour setup permanent d'investigation.

**Qubes OS** : système d'exploitation avec isolation par VM (AppVMs). Très sécurisé mais courbe d'apprentissage plus raide.

**VM dédiée dans VMware/VirtualBox** : alternative accessible si Whonix est trop lourd. Clone de l'OS avant chaque session, restauration post-session.

**Outils complémentaires** :
- **curl / wget via Tor** (torify) : récupération en ligne de commande.
- **OnionScan** : audit automatique de services .onion pour failles OPSEC.
- **tsocks / proxychains** : chaînage de proxies.
- **Aquatone, Eyewitness** : capture automatisée de screenshots en masse.
- **Hunchly** : outil commercial de capture structurée d'investigation (horodatage, archivage, notes).
- **Maltego** : graphing des relations entre entités (avec transformations spécifiques dark web).

### 24.2 Les sources et points d'entrée

**Comment trouve-t-on des .onion** ?

**Listes communautaires**. The Hidden Wiki (multiple instances, pas toutes fiables), Dark.fail, Tor.taxi. Ces listes sont **partielles et partiellement scam-compromised** — ne jamais cliquer aveuglément.

**Moteurs de recherche .onion**. Ahmia, Torch, Haystak, Excavator. Indexation **très partielle** du contenu .onion. Utile pour des recherches spécifiques, mais rarement exhaustif.

**Cross-references depuis forums**. Les forums mentionnent d'autres forums, marchés, canaux. Documentation par ce biais — plus fiable que les listes car vouchées par la communauté.

**Canaux Telegram**. Beaucoup d'acteurs postent leurs adresses .onion sur Telegram, ce qui les rend plus facilement découvrables. Surveiller les canaux pertinents.

**Services de monitoring commerciaux**. Recorded Future, SOCRadar, Flashpoint, Flare, Intel471, DarkOwl, Cybersixgill — tous maintiennent des bases d'entités dark web crawlées. Accès via abonnement entreprise.

**OSINT public**. Articles de presse, papers académiques, rapports vendors — regorgent de mentions d'adresses .onion qui ont fait l'actualité.

### 24.3 La collecte structurée

**Capture vs simple navigation**. La collecte doit être **structurée**, pas simple navigation. Capturer systématiquement :
- **URL complète** visitée.
- **Horodatage précis** (timestamp avec seconde, fuseau horaire).
- **Capture d'écran** du contenu.
- **HTML source** sauvegardé.
- **Hash** du contenu sauvegardé.
- **Pseudonyme utilisé** pour la session.

**Archivage**. Plusieurs options :
- **Hunchly** : outil commercial qui automatise capture + organisation + horodatage.
- **Archivage manuel** : dossiers structurés, nommage convention (YYYYMMDD-HHMMSS-source-description), fichiers immutables.
- **Container cryptographiquement signé** : après collecte, générer un hash global du dossier, horodater, signer (GPG), stocker en immutable.

**Organisation**. Par cas d'investigation, par source, par date. Éviter le « one big folder » — impossible à remonter après 6 mois.

### 24.4 Les challenges techniques

**Lenteur du réseau Tor**. Navigation 5-10× plus lente que clearnet. Planifier des sessions d'investigation longues, éviter la multitâche excessive.

**Disponibilité intermittente des .onion**. Un site .onion peut être down pour heures ou jours. Tenter plusieurs fois, utiliser des mirrors (si connus), noter les patterns de disponibilité.

**DDoS permanents**. Les grands forums sont régulièrement DDoSés. Les pages chargent lentement, partiellement, ou pas du tout. Les meilleures heures d'investigation sont souvent les créneaux nocturnes (fuseau horaire attaquant).

**CAPTCHA pervasifs**. Pour limiter le scraping, beaucoup de sites .onion implémentent CAPTCHAs difficiles, parfois impossibles pour des outils automatisés.

**Protections anti-scraping**. Limites de requêtes, défis JS, tokens de session, fingerprinting — rendent la collecte automatisée complexe.

**Sites éphémères**. Un forum peut déménager d'adresse .onion sans préavis. Une capture d'il y a 6 mois peut pointer vers un site disparu. Les archives ont donc une valeur disproportionnée sur le dark web.

### 24.5 Les limites méthodologiques

**Biais de survivance**. Ce qu'on observe est ce qui existe actuellement. Les acteurs qui disparaissent ne sont plus observables. Les forums saisis ne sont plus accessibles (sauf archives). L'image du dark web à un instant T est partielle et biaisée vers les survivants.

**Biais de visibilité**. Les acteurs les plus sophistiqués sont souvent les moins visibles. Un APT étatique n'a pas besoin d'un leak site flashy — il opère discrètement. Les acteurs observables sur forums publics sont majoritairement de profil intermédiaire.

**Biais de représentation**. L'analyste observe à travers les forums qu'il connaît. L'écosystème russophone, chinois, arabophone, persan ont chacun leurs dynamiques propres, partiellement accessibles selon les compétences linguistiques de l'équipe.

**Biais de fraîcheur**. Les données anciennes disparaissent. Un forum actif il y a 2 ans peut être invisible aujourd'hui. L'histoire du dark web est partiellement perdue.

**Biais d'accès**. Les zones premium des forums (souvent les plus intéressantes analytiquement) nécessitent paiement, vouching, tenure. Un analyste privé n'a pas toujours les moyens d'accéder à toutes les zones utiles.

### 24.6 Automatisation et échelle

**Scraping automatisé** : possible mais difficile. Les protections anti-bot sont fortes. Nécessite infrastructure (plusieurs instances Tor, rotation d'identités), résilience (retry logic, gestion erreurs), légalité (certains ToS interdisent scraping même sur sites criminels).

**Plateformes commerciales** : outils SaaS qui font le crawling à grande échelle et exposent les résultats via API. Recorded Future, DarkOwl, Flare, Intel471, Cybersixgill. Coût : 50 k - 500 k USD/an selon scale.

**Open source** : quelques projets open source (OnionScan, TorBot, Dark-Scrape) mais moins robustes que solutions commerciales.

**Approche hybride** : scraping ciblé sur sources prioritaires + plateforme commerciale pour couverture large + veille humaine pour les signaux faibles.

### 24.7 Fil rouge — DARKSTREAM : l'accès à IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 13 : setup et navigation**
>
> Lucas utilise son environnement Whonix avec Tor Browser Safest. Accès initial à IndustrialLeaks via l'adresse .onion communiquée par le partenaire vouching. Vérification de l'adresse : 56 caractères, cross-check sur 2 sources indépendantes (mention dans un post Recorded Future + mention sur un forum russophone peer).
>
> Navigation lente — 2-3 secondes par clic. Le forum affiche un CAPTCHA proof-of-work (JS requis à minima pour le CAPTCHA). Lucas active JS **uniquement pour la page de login**, puis le désactive après. Session de navigation active, avec Hunchly en background pour capture systématique.
>
> Exploration structurée :
> 1. Captures de toutes les catégories publiques (arborescence du forum).
> 2. Lecture et capture du post aero_source + tous les posts du même user.
> 3. Navigation aux autres vendeurs du mois, pour profiling comparatif.
> 4. Règles du forum (capture).
> 5. Statistiques visibles (nombre de membres, posts, transactions).
>
> Cycle de 3 heures. 147 pages capturées, structurées par dossier. Hash du corpus calculé. Persona « mapletech » affiche activité cohérente (quelques réponses en threads, aucun message offensif, aucune tentative de solliciter info sensible au-delà de ce qui est publiquement affiché).
>
> Post-session, Lucas produit un **mémo d'observations** : architecture du forum, profils de vendeurs actifs, posts d'intérêt, observations sur aero_source. Ce mémo alimente le dossier DARKSTREAM et permet aux autres membres de l'équipe Athéna d'orienter leurs propres recherches sans re-naviguer manuellement.

---

## Chapitre 25 — Investigation dans un data leak : workflow

Ce chapitre présente un workflow structuré pour investiguer une annonce de fuite de données. C'est l'une des situations les plus fréquentes pour un analyste CTI défensif — alerte de monitoring, il faut déterminer si la fuite est réelle, pertinente, et actionnable.

### 25.1 Le cadre de l'investigation

**Déclencheur typique** :
- Alerte automatique de plateforme de monitoring (Recorded Future, Flare, Hudson Rock) : « mention de votre marque détectée sur forum X ».
- Signalement journalistique : « un journaliste cite une rumeur de breach sur votre entreprise ».
- Signalement partenaire : « un CERT sectoriel partage une alerte ».
- Auto-découverte : analyste qui observe un post suspect lors de sa veille courante.

**Objectifs de l'investigation** (dans l'ordre de priorité) :
1. **Confirmer ou infirmer l'existence** du breach.
2. **Authentifier les données** offertes.
3. **Évaluer le volume et la sensibilité** de ce qui circule.
4. **Cartographier l'écosystème** (vendeur, acheteurs, éventuels courtiers intermédiaires).
5. **Dater** la compromission.
6. **Identifier le vecteur** si possible.
7. **Produire un rapport actionnable** pour la cellule de crise.

**Contraintes** :
- **Temps** : la cellule de crise attend des réponses rapides. 24-72h pour premier verdict.
- **Légal** : cadre défini Ch.22. Pas de téléchargement massif, pas de provocation.
- **OPSEC** : ne pas alerter le vendeur que la victime est notifiée (sinon disparition des traces).
- **Coordination** : si OIV, DGSI/ANSSI impliqués ; si multi-victimes, partage sectoriel.

### 25.2 Étape 1 — Triage initial

**Objectif** : en 2-4 heures, déterminer si l'alerte mérite investigation approfondie ou peut être classée.

**Questions clés** :
- Le **post** est-il récent ou recyclé (reposé d'un breach antérieur) ?
- Le **vendeur** a-t-il un profil crédible (ancienneté, transactions, vouching) ou est-ce un nouveau compte ?
- Le **forum** est-il sérieux (XSS, Exploit, BreachForums) ou low-end ?
- Les **détails du post** sont-ils spécifiques (volumétrie, types de données, contexte) ou génériques ?
- Les **échantillons** sont-ils fournis ou non ?

**Décision** :
- **Scam probable** : fermer le dossier avec note. Monitoring light pour détecter escalade.
- **Recyclage** : identifier le breach original, mettre à jour le dossier historique, pas d'investigation approfondie.
- **Cas authentique probable** : escalader en investigation structurée (suite du workflow).
- **Ambigu** : investigation légère pour clarifier avant décision.

### 25.3 Étape 2 — Profiling du vendeur

**Objectif** : comprendre qui pose l'annonce.

**Collecte** :
- Historique **sur le forum principal** : tous les posts du pseudo, dates, catégories, réponses reçues.
- **Cross-platform** : présence du pseudo sur d'autres forums, canaux Telegram, Jabber, etc. Ch.26 pour pivoting détaillé.
- **Style linguistique** : langue maternelle apparente, niveau technique, style de négociation.
- **Activité financière connue** : adresses crypto affichées, patterns de transactions visibles on-chain.
- **Relations** : qui vouche le vendeur ? qui achète ? avec qui interagit-il dans les threads ?

**Output** : fiche de profil du vendeur, 2-4 pages, avec observations et hypothèses initiales sur son positionnement dans l'écosystème.

### 25.4 Étape 3 — Acquisition d'échantillons

**Objectif** : obtenir des données permettant l'authentification.

**Modalités** :
- **Échantillons publics** : si le vendeur en a posté en thread public, capture simple.
- **Échantillons sur demande** : contact via canal indiqué (XMPP, Telegram), avec persona d'investigation.
- **Pas d'engagement ferme** : demande d'échantillons supplémentaires positionnée comme due diligence pré-achat, pas comme achat effectif.
- **Refus d'achat complet** : le cadre n'autorise pas l'achat du dump complet. Les échantillons servent à confirmer, pas à exfiltrer.

**Précautions** :
- Fichiers manipulés **uniquement en VM isolée**.
- Scan antivirus/sandbox avant ouverture.
- Extraction de métadonnées avant exécution.
- **Ne jamais ouvrir dans l'OS hôte**.

### 25.5 Étape 4 — Authentification

**Objectif** : déterminer si les données sont authentiques et proviennent de la victime annoncée.

**Techniques** :

**Métadonnées de fichiers**. PDF, DOCX, XLSX — extraction des métadonnées avec exiftool. Cherche : auteur, entreprise, chemin de création, horodatages, révisions. Un document avec métadonnées « Created: Vectris Aerospace, Author: M. Dubois, 2025-11 » cohérentes avec l'entreprise cible est fort.

**Cohérence de contenu**. Les noms d'employés dans le fichier correspondent-ils à des employés réels (vérifiables sur LinkedIn, site corporate) ? Les références projets correspondent-elles à des projets connus ? Les références fournisseurs sont-elles plausibles ? Les numéros de révision, codes internes, formats de référence correspondent-ils aux conventions documentées de l'entreprise ?

**Markers internes**. Certaines entreprises matures incluent des **markers intentionnels** dans leurs documents sensibles — fausses entrées dans les bases fournisseurs, employés fictifs dans les annuaires internes, entreprises fictives dans les listes de partenaires. La présence de ces markers dans un dump confirme qu'il provient bien de l'entreprise. **Vectris avait un tel marker** (fictif) dans sa liste fournisseurs — retrouvé dans l'échantillon DARKSTREAM.

**Corrélation avec données publiques**. Si le dump contient des éléments disponibles publiquement (communiqués, rapports annuels, documents marketing), les comparer. Un dump qui contient un document public identique à la version publique n'ajoute rien ; un dump qui contient un brouillon du communiqué postérieur à une version précédente — et ce brouillon est antérieur à la publication officielle — atteste d'un accès interne.

**Demande d'échantillon ciblé**. Demander au vendeur un fichier spécifique contenant un nom connu. S'il peut le fournir, l'authenticité est très probable. S'il refuse ou fournit quelque chose d'incohérent, suspicion.

**Cross-check forensics interne**. Transmettre les échantillons à l'équipe IR de la victime. Ils peuvent confirmer l'authenticité par comparaison avec leurs bases internes.

**Output** : niveau de confiance dans l'authenticité (scale : non-authentique / probable / très probable / confirmé), argumentaire détaillé.

### 25.6 Étape 5 — Cartographie de l'écosystème

Une fois l'authenticité évaluée, cartographier le contexte.

**Qui est l'auteur initial du vol** ? Le vendeur sur le forum est-il l'attaquant, un courtier, un acheteur final revendeur ?

**Y a-t-il d'autres traces** ? Le même dump est-il proposé sur d'autres forums ? Circulation privée ? Tentatives de chantage direct de la victime ?

**Qui sont les acheteurs potentiels** ? Concurrents ? Acteurs étatiques ? Groupes cybercriminels cherchant un levier de ransomware ? IndustrialLeaks ciblant une clientèle spécifique ?

**Quel est le vecteur d'entrée** ? Corrélation avec logs internes, stealer logs sur la victime, exploits publics de la période, TTP d'un groupe APT connu.

**Quelle est la chronologie** ? Dates de compromission, d'exfiltration, de mise en vente — compatibles avec les traces forensiques internes ?

### 25.7 Étape 6 — Analyse des flux financiers

Si le vendeur affiche une adresse crypto (pour recevoir paiement), cette adresse est une mine de renseignement.

**Capture de l'adresse**. Copier exactement depuis la source.

**Traçage on-chain**. Analyse via Chainalysis Reactor, TRM Labs Forensics, Elliptic Investigator, ou équivalent open source (Breadcrumbs, OXT).

**Questions analytiques** :
- L'adresse a-t-elle reçu des paiements ? De qui (quels autres wallets) ?
- L'adresse est-elle connue comme liée à d'autres opérations (blacklistée par Chainalysis) ?
- Les fonds ont-ils été déplacés ? Vers où (mixer, exchange, autre wallet) ?
- Cluster d'adresses connecté : des dizaines d'autres adresses peuvent être contrôlées par le même acteur.

Voir Ch.31 pour détails du traçage crypto.

### 25.8 Étape 7 — Production du rapport

**Structure standard** :
1. **Executive summary** (1 page) : qu'est-ce qui a fuité, degré de confiance, recommandations urgentes.
2. **Contexte** : comment l'alerte a été détectée, sources initiales.
3. **Observations factuelles** : ce qui a été observé sur le dark web, avec captures et horodatages.
4. **Analyse d'authenticité** : arguments pour/contre, conclusion.
5. **Cartographie** : acteurs impliqués, chaîne potentielle, chronologie.
6. **Impact évalué** : quelles données exposées, conséquences potentielles business/légale/réputationnelle.
7. **Recommandations** : actions immédiates (isolation postes, reset credentials, notifications), actions moyen terme (monitoring, communication, enquêtes).
8. **Annexes** : captures d'écran, hashes, extraits de communications, adresses crypto observées.

**Ton** :
- **Factuel**, pas sensationnaliste.
- **Calibré** : utiliser le vocabulaire des Words of Estimative Probability — « très probable », « probable », « possible », « incertain ».
- **Actionnable** : les recommandations sont concrètes, chiffrées quand possible, hiérarchisées.
- **Révisable** : le rapport est une photo d'un instant T, à compléter avec nouvelles observations.

**Diffusion** :
- Cellule de crise interne : diffusion restreinte, TLP RED ou AMBER selon sensibilité.
- Autorités (DGSI, ANSSI, CNIL si données personnelles) : remontée obligatoire pour OIV.
- Partenaires sectoriels (ISAC) : éventuellement TLP AMBER anonymisé.
- Public (rare, cas exceptionnels) : communiqué officiel coordonné.

### 25.9 Fil rouge — DARKSTREAM : rapport intermédiaire

> **🌐 DARKSTREAM — Épisode 14 : rapport à mi-parcours**
>
> Après 3 semaines d'investigation, Lucas produit un rapport intermédiaire pour la cellule de crise Vectris et la DGSI.
>
> **Executive summary** :
> - Authenticité des données Vectris sur IndustrialLeaks : **confirmée** (marker interne + cohérence forensics Mandiant).
> - Volume exfiltré : **420 Go confirmés**, incluant specs propulsion, documents de conception, bases clients/fournisseurs, emails internes, budgets.
> - Vendeur aero_source : acteur russophone intermédiaire, probablement **revendeur** (pas auteur direct de l'exfiltration).
> - Chaîne reconstituée : infostealer Lumma → vente log Russian Market → achat par IAB magnit_ru → revente accès → exfiltration par aero_source ou commanditaire.
> - Aucun acheteur final identifié pour les données Vectris (ni traces de paiement sur l'adresse BTC affichée par aero_source).
> - Niveau de menace : **élevé** mais pas **critique** en termes de diffusion élargie.
>
> **Recommandations immédiates** :
> - Poursuite isolation/reset des postes compromis identifiés (VECTRIS-RD-112, VECTRIS-SALES-047, VECTRIS-IT-008).
> - Notification aux partenaires défense concernés par les spécifications exposées.
> - Poursuite monitoring IndustrialLeaks + forums liés pour détection publication totale ou vente confirmée.
> - Préparation communication client/partenaires en cas d'escalade.
>
> **Recommandations moyen terme** :
> - Durcissement politique de téléchargement de logiciels sur postes R&D.
> - Déploiement EDR renforcé sur segment R&D.
> - Campagne sensibilisation antivol de credentials (stealer) pour collaborateurs.
> - Revue des règles firewall pour détecter exfiltrations volumineuses sortantes.
>
> Le rapport est transmis TLP:RED à la cellule de crise, TLP:AMBER à la DGSI. La cellule active les recommandations ; la DGSI oriente Lucas vers la suite de l'investigation — identification d'aero_source.

---

## Chapitre 26 — Pivoting, enrichissement et corrélation OSINT

Le **pivoting** est l'art de passer d'un indicateur à un autre pour enrichir l'investigation. Sur le dark web, c'est la différence entre une observation isolée et un renseignement exploitable.

### 26.1 Les types de pivots

**Pseudonyme → autres forums**. Un pseudonyme observé sur un forum peut exister sur d'autres. Recherche directe du pseudo sur XSS, Exploit, BreachForums, forums concurrents.

**Pseudonyme → Telegram / Jabber / TOX**. Les posts mentionnent souvent des handles de contact. Suivre ces handles sur les plateformes correspondantes.

**PGP key → autres utilisations**. Une clé PGP est un identifiant quasi-unique. Rechercher la clé (fingerprint) sur d'autres forums, dans des archives, sur des keyservers publics — peut révéler d'autres pseudos ou usages antérieurs.

**Adresse crypto → transactions, clustering**. Une adresse BTC observée permet de découvrir : historique on-chain, adresses liées (cluster), exchanges interagis, autres wallets probablement contrôlés par le même acteur (via heuristiques de change, co-dépense, etc.).

**Infrastructure (domaines, IPs) → autres services**. Un domaine enregistré pour un service criminel peut partager des infos avec d'autres (registrant email, serveurs de noms, mêmes IPs d'hébergement). Outils : DomainTools, SecurityTrails, ViewDNS, passivedns commerciaux.

**Email / fingerprint → OSINT classique**. Un email leaked sur un forum, un pseudonyme utilisé ailleurs (Discord, GitHub, Reddit, StackOverflow, jabber distinct) — permettent de construire un graphe d'identité.

**Style linguistique → attribution**. Tournures, fautes, patterns — peuvent corréler plusieurs pseudos.

**Timing → fuseau horaire**. Patterns d'activité horaire révèlent fuseau. Crosscheck avec autres pseudonymes actifs aux mêmes heures.

### 26.2 Méthodologie de pivoting

**Graph d'investigation**. Maintenir un graphe (Maltego, graphes maison) où chaque nœud est une entité (pseudo, email, wallet, IP, domaine) et chaque arête est une relation (« utilise », « contrôle », « a interagi avec », « mentionne »). Chaque nouveau pivot ajoute des nœuds et arêtes.

**Hypothèses explicites**. À chaque pivot, formuler une hypothèse (« Je pense que pseudo A et pseudo B sont la même personne parce que… »). Tester l'hypothèse avec nouveaux pivots. Renforcer ou rejeter.

**Niveaux de confiance**. Comme pour l'attribution APT (voir cours APT), utiliser vocabulaire calibré : certain / très probable / probable / possible / spéculatif.

**Limites documentées**. Certaines corrélations sont faibles (mêmes initiales pseudo, timing vague) ; d'autres fortes (même PGP key, même wallet). Le rapport final doit distinguer les deux.

### 26.3 Les ressources OSINT utiles

**Bases de données de breach**. Have I Been Pwned, DeHashed, LeakCheck, Snusbase — vérifier si un email ou identifiant a été exposé dans des breaches publics, reconnaître un pseudo qui apparaît dans d'autres contextes.

**Archives forums**. Certains forums disparus ont des archives partielles disponibles — BreachForums archives, Tor's Everything mirror, Internet Archive pour le clearnet.

**GitHub / GitLab**. Parfois, un acteur utilise le même pseudo professionnellement (développement, open source) et dans les forums cybercriminels. Historique public GitHub peut révéler nom réel, email, localisation, compétences.

**LinkedIn / Xing**. Pour les pivots partiels vers identité civile. Un email pro leaked peut correspondre à un profil LinkedIn.

**Keyservers PGP**. Ubuntu keyserver, SKS pools (legacy), Keys.openpgp.org. Recherche par fingerprint peut révéler identités alternatives.

**Blockchain explorers**. Blockstream.info, Mempool.space (Bitcoin), Etherscan (Ethereum), Tronscan (TRON), BlockChair (multi-chain). Traçage des transactions à partir d'adresses observées.

**WHOIS et passive DNS**. Pour le pivoting d'infrastructure.

**Reverse image search**. Google Images, TinEye, Yandex. Un profile picture d'un forum peut correspondre à un profil ailleurs.

**Services spécialisés dark web**. IntelX (archives .onion et leaks), Flare, Recorded Future, DarkOwl, Cybersixgill — agrègent et indexent.

### 26.4 Les erreurs courantes

**Sur-corrélation**. Conclure qu'un pattern faible (initiales communes, style superficiel) prouve que deux pseudos sont la même personne. Le dark web compte des millions d'utilisateurs, beaucoup de coïncidences.

**Biais de confirmation**. Une fois qu'on a un chouchou (« c'est forcément X »), on trouve partout des « preuves ». Discipline : chercher activement ce qui **infirmerait** l'hypothèse.

**Timing trompeur**. Les fuseaux horaires se simulent facilement — un acteur peut activer son compte à des heures calibrées.

**Pseudos communs**. « admin », « king », « boss », « ghost » sont utilisés par des milliers d'acteurs indépendants. Pas un pivot fiable seul.

**Infrastructure partagée**. Plusieurs acteurs utilisent le même hébergeur, registrar, service de certificat. Pas un pivot fiable à lui seul.

**PGP reprise**. Rare, mais une clé PGP peut être volée ou rachetée. Changement soudain du style après une longue présence d'un pseudo avec la même clé = alerte sur une possible rachat.

### 26.5 Fil rouge — DARKSTREAM : pivoting sur aero_source

> **🌐 DARKSTREAM — Épisode 15 : élargissement**
>
> Lucas pivote sur aero_source au-delà d'IndustrialLeaks.
>
> **Pivot 1 — XSS Forum** : recherche du pseudo « aero_source » sur XSS (accès Athéna via partenariat vouching). **Pas de compte direct**, mais un compte « aerosrc » créé il y a 13 mois, style similaire, utilise le même serveur XMPP. Probable sock puppet ou compte antérieur. Activité modeste (4 posts).
>
> **Pivot 2 — Exploit.in** : recherche. Pseudo « aero_src » existe, compte créé il y a 7 mois, style compatible. 3 posts, un sur une vente de specs turbines (non-Vectris, différente cible). **Cohérent avec pattern** d'un même acteur opérant sur 3 forums russophones.
>
> **Pivot 3 — PGP** : la clé PGP affichée par aero_source sur IndustrialLeaks est **identique** à celle sur aerosrc (XSS) et aero_src (Exploit.in). **Très forte corrélation** — probabilité qu'il s'agisse du même acteur : 95%+.
>
> **Pivot 4 — Wallet BTC** : l'adresse BTC mentionnée dans le post aero_source sur IndustrialLeaks. Chainalysis révèle un cluster de ~40 adresses liées. Transactions totales : ~180 000 USDT sur 14 mois. Quelques flux vers exchange non-KYC (Garantex historique, avant sanctions 2022). Interactions avec adresses labellisées « BlackSprut » (marché russophone) — indique acheteur de drogues ou fournisseur dans cet écosystème.
>
> **Pivot 5 — Analyse linguistique** : les posts des 3 comptes (aero_source, aerosrc, aero_src) présentent les mêmes tics — « dear colleagues » comme ouverture, « best regards » comme signature, fautes consistantes (confusion article « the », prépositions). Russophone, niveau anglais intermédiaire. **Corrélation linguistique cohérente avec PGP**.
>
> **Pivot 6 — Telegram** : le handle mentionné par aero_source (non utilisé ici pour OPSEC) pointe vers un compte Telegram. Observation light, pas de contact. Ancienneté compte : 2 ans. Membre de plusieurs canaux cybercriminels russophones.
>
> **Synthèse** : aero_source est (très probablement) un acteur russophone individuel, présent sur l'écosystème depuis 2+ ans, profil IAB/courtier de données intermédiaire, pas un acteur majeur. Son réel intérêt pour les données Vectris n'est pas idéologique ni étatique — motivation financière classique.
>
> Ce profiling oriente l'attribution et le conseil : la menace est réelle mais contenue dans un profil cybercriminel, pas le signe d'une opération étatique majeure. Conséquences pour Vectris : le dump ne servira probablement pas un concurrent direct ou un service de renseignement étranger à court terme — il sera vendu au plus offrant, potentiellement n'importe qui.

---

## Chapitre 27 — Veille dark web : surveillance, alerting, réduction du bruit

La **veille dark web** n'est pas une investigation ponctuelle — c'est un programme durable. Ce chapitre couvre la structuration d'une veille efficace, les outils, et la gestion du bruit.

### 27.1 Les objectifs de la veille

Pour une organisation, plusieurs objectifs distincts peuvent justifier une veille dark web.

**Détection de compromission**. Mentions de la marque sur forums/marchés/leak sites → possible breach à investiguer. Détection de credentials de l'organisation sur marchés de logs → possible vecteur de compromission. Détection d'IAB proposant des accès compatibles → menace imminente.

**Monitoring de dirigeants et VIP**. Mentions de personnalités (CEO, CFO, membres du conseil) — risques de fraude, chantage, usurpation.

**Veille concurrentielle / réputationnelle**. Activité malveillante autour de la marque — deepfakes, impersonations, phishing ciblant clients.

**Renseignement sectoriel**. Tendances dans le secteur : quelles campagnes ransomware ciblent l'aerospace ? quels vecteurs utilisés pour compromettre manufacturers ? Alimentation de la threat intel.

**Renseignement géographique**. Tendances par pays : quelles entités françaises sont ciblées ? quels groupes actifs en Europe ?

**Renseignement sur adversaires spécifiques**. Suivi d'APT ou groupes ransomware identifiés comme menaces prioritaires pour l'organisation.

### 27.2 Les sources à surveiller

**Leak sites ransomware**. Monitoring via Ransomwatch, Ransomfeed, plateformes commerciales. Alerting sur mentions de la marque ou du secteur.

**Forums majeurs**. XSS, Exploit, BreachForums — via crawling (si capacités) ou via plateformes qui le font.

**Marchés de logs**. Russian Market principalement. Monitoring par domaine.

**Marchés de fraude**. BriansClub, successeurs. Moins critique pour la plupart des organisations non-financières.

**Canaux Telegram**. Canaux identifiés comme pertinents — cybercrime russophone, leaks, hacktivisme pro/anti-pays X.

**Pastebins et assimilés**. Pastebin (partiellement désactivé pour usage criminel), Ghostbin, Rentry, Doxbin, etc.

**Feeds CTI**. VirusTotal, URLhaus, ThreatFox, etc. — indicateurs partagés communautairement.

**GitHub**. Fuites de credentials dans repos publics (GitHub dorking). Secrets committed par erreur, puis effacés mais toujours dans l'historique.

**Réseaux sociaux**. Twitter/X, Mastodon pour signaux de mentions, revendications hacktivistes, réactions de la communauté.

**Deep web non-tor**. Forums clearnet à accès restreint (payment, invite), souvent plus faciles d'accès que les .onion et riches en contenu.

### 27.3 Les outils de monitoring

**Plateformes commerciales CTI** (budget 50 k - 500 k USD/an) :
- **Recorded Future** : leader du marché, intelligence mondiale, intégration étendue.
- **Flashpoint** : forte expertise russophone et Telegram.
- **Intel471** : focus acteurs et écosystème cybercriminel.
- **SOCRadar** : plus abordable, bon rapport qualité/prix pour PME.
- **Flare** : niche dark web et data leaks, prix compétitif.
- **DarkOwl** : crawling .onion étendu.
- **Cybersixgill** (Zenity) : profilage et attribution.
- **Hudson Rock** : spécialisé stealer logs.
- **KELA** : forte couverture russophone.
- **Group-IB** : vision Europe/Asie.

**Outils open source** :
- **Ahmia** : moteur de recherche .onion, partiellement open source.
- **TorBot, Dark-Scrape** : crawlers open source (maintenance variable).
- **OnionScan** : audit de services .onion.
- **GitHub dorking** : outils pour détecter secrets dans repos.
- **Ransomwatch** : agrégateur public de leak sites ransomware.

**Services sectoriels**. Certains ISAC (par secteur) partagent de la threat intel par abonnement ou gratuitement pour leurs membres.

**Services gouvernementaux**. En France, partage d'information via l'ANSSI (CERT-FR, signalement d'incidents). Bulletins d'alerte publics.

### 27.4 Le défi du bruit

La veille dark web produit **énormément de faux positifs**. Un programme mal configuré génère des centaines d'alertes par semaine, dont la majorité ne nécessitent aucune action. Gérer le bruit est la compétence centrale du programme de veille.

**Sources de bruit** :
- **Homonymies** : « Vectris » est une marque, mais aussi possiblement un prénom, un nom commun dans d'autres langues, une entité sans lien.
- **Mentions éditoriales** : articles de presse, rapports CTI mentionnent l'entreprise sans être des signaux de compromission.
- **Credentials anciens** : comptes employés exposés dans breaches antérieurs (Adobe 2013, LinkedIn 2012, Collection #1 en 2019), re-mis en vente ou re-publiés.
- **Scams et fakes** : annonces de breach inexistants.
- **Typos et variantes** : « Vectriss », « Vectris_corp », « Victreis » — à filtrer ou à surveiller.

**Stratégies de réduction du bruit** :

**Keywords précis**. Utiliser des termes spécifiques (noms de produits internes, codes clients, adresses email pro, identifiants propriétaires) plutôt que seulement la marque générique.

**Whitelist éditoriale**. Filtrer les sources éditoriales (presse, rapports publics) qui mentionnent légitimement la marque sans menace.

**Filtrage temporel**. Dépriorer les mentions anciennes, prioritiser les nouvelles.

**Priorisation par criticité**. Mention sur forum XSS russophone > mention sur pastebin anonyme > mention éditoriale. Logs VPN corporate > logs consumer perso d'un employé.

**Machine learning**. Les plateformes commerciales appliquent du ML pour scorer la pertinence. Efficacité variable — complément de l'humain, pas remplaçant.

**Triage humain**. En fin de chaîne, un analyste trie les alertes résiduelles. 80-90% classées en quelques secondes chacune, 10-20% méritent investigation plus poussée.

### 27.5 Workflow de veille type

**Quotidien** (1-2h/jour pour un analyste dédié) :
- Revue des alertes automatiques (plateforme commerciale).
- Triage initial — classement en « ignorer », « surveiller », « investiguer ».
- Investigations légères sur les alertes ambigües.
- Mise à jour des indicateurs suivis.

**Hebdomadaire** (demi-journée) :
- Revue des leak sites ransomware ciblage sectoriel.
- Veille sur forums prioritaires (top 5-10 identifiés).
- Synthèse hebdomadaire pour le CISO et la direction.
- Mise à jour de la liste de surveillance.

**Mensuel** :
- Rapport mensuel structuré : tendances, incidents majeurs, évolutions observées.
- Revue du scope de monitoring — ajouts, retraits.
- Évaluation de la qualité des sources et outils.

**Trimestriel** :
- Audit du programme de veille.
- Évolution du budget et des ressources.
- Formation continue des analystes.
- Partage avec pairs sectoriels (ISAC, RSSIs par secteur).

### 27.6 Le programme de veille comme outil défensif

Au-delà de la détection d'incidents, un programme de veille bien structuré sert plusieurs fonctions défensives.

**Threat intelligence pour le SOC**. Les observations alimentent les règles de détection (IoC à surveiller, TTP à anticiper, vulnérabilités exploitées activement par acteurs connus).

**Aide à la priorisation défensive**. Si les stealers ciblent massivement un secteur, durcir les politiques correspondantes. Si un vecteur spécifique (phishing kit, vulnérabilité edge device) est en croissance, mitiger en priorité.

**Sensibilisation**. Les exemples observés nourrissent les campagnes de sensibilisation employés. « Regardez, voici un log d'infostealer vendu pour 15 USD qui contenait les credentials d'un collègue » fait plus d'impact qu'une théorie abstraite.

**Préparation stratégique**. Les tendances observées (convergence crime-étatique, montée de tel groupe, décl in de tel autre) alimentent la planification pluriannuelle de sécurité.

**Posture de négociation**. En cas de crise (ransomware subi, données exposées), une bonne veille préalable permet de connaître l'adversaire et de négocier en position informée.

---

## Chapitre 28 — Preuve, capture et documentation

La différence entre une observation intéressante et une preuve utilisable tient à la **documentation**. Ce chapitre couvre la préservation des preuves de manière admissible — pour rapport interne, pour coordination avec autorités, et le cas échéant pour usage judiciaire.

### 28.1 Les niveaux de documentation

**Niveau 1 — Documentation interne** : pour rapport à la cellule de crise, à la direction. Exigence : lisible, structuré, horodaté. Pas de formalisme judiciaire strict.

**Niveau 2 — Documentation pour autorités** : pour transmission à DGSI, ANSSI, CNIL. Exigence : chain of custody, horodatages fiables, hashes, traçabilité. Format standard (IOCs, STIX/TAXII si pertinent).

**Niveau 3 — Documentation admissible judiciairement** : pour usage dans procédure pénale. Exigence : chain of custody rigoureuse, capture forensically sound, témoin pour certaines captures, signature notariale ou équivalent pour éléments critiques. Un analyste privé produit rarement directement ce niveau ; il prépare les éléments pour que les forces de l'ordre puissent les reconstituer avec leur propre cadre.

**Niveau 4 — Documentation coopérative** : pour partage sectoriel (ISAC, pairs RSSI). TLP AMBER typiquement. Format structuré pour réutilisation par les pairs (indicators actionnables, sans données sensibles exposées).

### 28.2 La chain of custody

Principe : pour chaque élément de preuve, tracer **qui l'a collecté, quand, comment, et par qui il a été manipulé depuis**. Toute rupture dans la chaîne invalide potentiellement la preuve.

**Éléments à tracer pour chaque capture** :
- **Date et heure précise** (UTC recommandé, avec fuseau indiqué).
- **Analyste** qui a effectué la capture.
- **Source** : URL .onion, forum, thread ID, post ID.
- **Méthode** : capture d'écran, HTML source save, wget, screenshot d'une VM.
- **Hash cryptographique** du fichier capturé (SHA-256 minimum).
- **Emplacement de stockage** : chemin dans l'archive Athéna, sauvegarde sur stockage immutable.
- **Modifications** : aucune idéalement, ou documentées si nécessaires.

**Outils d'aide** :
- **Hunchly** : outil commercial qui automatise une grande partie de la chain of custody.
- **OSINT Cloner** : alternative open source, moins complète.
- **Custom scripts** : beaucoup d'équipes développent leurs propres scripts de capture structurée.

### 28.3 Types de preuves et méthodes de capture

**Pages web (HTML)**. Capture en deux formats :
- **Screenshot** : rendu visuel, incluant CSS et images. Utile pour le lecteur humain.
- **HTML source** : code source brut. Utile pour l'analyse technique et la reconstitution.

Outils : wget/curl (via torify), outils navigateur (save page as, print to PDF), Hunchly, Aquatone pour volumes.

**Threads de forums**. Capturer tous les posts d'un thread, même si longs et paginés. Hunchly ou scripts qui parcourent la pagination.

**Messages privés**. Dans une messagerie (XMPP, Telegram), exporter le log chiffré complet. Conserver les métadonnées (horodatages, clés de session, participants).

**Fichiers téléchargés**. Hash immédiat post-téléchargement. Pas de modification avant analyse en VM. Stockage du fichier original intact + copie de travail pour analyse.

**Adresses crypto et transactions**. Capture de l'adresse exacte (copier-coller, pas retranscrire). Capture de transactions via blockchain explorer avec screenshots. Exports via Chainalysis, TRM, etc. horodatés.

**Captures temporelles**. Un site peut changer entre 2 visites. Capture datée à chaque fois. Archive via service tiers (Internet Archive pour clearnet, mais difficile pour .onion — archives manuelles alors).

### 28.4 Le stockage des preuves

**Immutabilité**. Une fois capturées, les preuves ne doivent pas pouvoir être modifiées. Options :
- **Stockage WORM** (Write Once Read Many) : solutions enterprise (AWS S3 Object Lock, Azure immutable blobs, NAS avec WORM).
- **Blockchain timestamping** : horodatage sur blockchain publique (OpenTimestamps, Bitcoin via OP_RETURN) — prouve qu'un document existait à une date donnée.
- **Signature cryptographique** : GPG signature par l'analyste, horodatée.
- **Archive sur CD/DVD non réinscriptibles** (pratique moins moderne mais acceptée judiciairement).

**Confidentialité**. Les preuves stockées restent sensibles. Chiffrement au repos, contrôle d'accès granulaire, logs d'accès. Idéalement : accès nécessitant plusieurs personnes pour ouvrir (modèle multi-party).

**Rétention**. Politique documentée : combien de temps conserver ? La plupart des organisations retiennent 3-7 ans selon cadre réglementaire et risques. Destruction formalisée après fin de rétention.

**Localisation**. Stockage dans pays cohérent avec le cadre juridique (France pour les preuves servant enquêtes françaises, idéalement), éviter stockage dans juridictions où les preuves pourraient être saisies ou exposées.

### 28.5 La notarisation et l'horodatage qualifié

Pour les preuves à haute valeur, le **simple hash** ne suffit pas toujours. Techniques additionnelles :

**Horodatage qualifié**. En France et en UE, services d'horodatage qualifiés eIDAS. Un horodatage qualifié prouve juridiquement qu'un document existait à une date donnée. Plusieurs fournisseurs (Universign, Docapost, prestataires qualifiés).

**Constat d'huissier**. Un huissier de justice peut constater le contenu d'un site web à un instant T. Coûteux (plusieurs centaines à milliers d'euros par constat) mais haute valeur probante en procédure judiciaire française.

**APCTA** (Authentification de Preuve Constatée par un Tiers Attentif) — services privés qui fournissent une forme d'attestation horodatée, moins formelle qu'un huissier mais plus accessible.

Pour une investigation CTI courante, horodatage + hash + chain of custody documentée suffit. Les procédures judiciaires plus lourdes (constat d'huissier) sont réservées aux cas où la preuve sera utilisée en contentieux.

### 28.6 Les indicators of compromise (IoC)

Au-delà de la documentation narrative, l'investigation produit des **indicators of compromise** — artefacts techniques réutilisables.

**Types d'IoC** :
- **Hashes de fichiers** (MD5, SHA-1, SHA-256 — le dernier préféré).
- **URLs / domaines** malveillants.
- **Adresses IP** C2, infrastructure.
- **Adresses crypto** utilisées par acteurs criminels.
- **Emails** utilisés dans phishing / scams.
- **Pseudonymes** de forum.
- **PGP fingerprints**.
- **YARA rules** : règles de pattern-matching pour détecter malwares.
- **Sigma rules** : règles de détection pour SIEM.
- **STIX objects** : format structuré pour interchange de TI.

**Format de partage** :
- **STIX/TAXII** : standard OASIS pour cyber threat intelligence, format structuré pour interchange machine-to-machine.
- **MISP** : plateforme communautaire de partage, format riche, TLP natif.
- **Feeds CSV / JSON** : formats simples pour intégration SIEM.
- **Emails structurés** pour partage ad hoc entre équipes.

**Coordination**. Les IoC sont partagés selon TLP :
- **TLP RED** : strictement entre équipes désignées.
- **TLP AMBER** : partage avec partenaires de confiance (ISAC, RSSI sectoriel).
- **TLP GREEN** : partage avec communauté élargie (CERT communautaire).
- **TLP CLEAR** : public.

### 28.7 La communication des résultats

Au-delà de la production des preuves, **communiquer les résultats** est une compétence à part entière.

**À la cellule de crise interne** :
- **Sommaire exécutif** : 1 page max, conclusions et recommandations.
- **Dossier technique** : détails pour l'équipe IR.
- **Capture préservée** : preuves accessibles en cas de besoin ultérieur.

**Aux autorités** :
- **Format standard** requis par l'autorité (DGSI a ses canaux, ANSSI a ses templates).
- **Anonymisation éventuelle** : parfois, certaines informations ne peuvent être transmises (sources, méthodes d'obtention).
- **Chain of custody maintenue**.

**Aux pairs sectoriels (ISAC)** :
- **Indicators anonymisés** : victim stripped, IoC techniques conservés.
- **Tactics observées** : utile pour détection chez les pairs.
- **TLP AMBER** typiquement.

**Publiquement (rare)** :
- **Rapports éditoriaux** : pour sensibilisation. Un cabinet CTI peut publier son investigation après anonymisation de la victime (si elle consent) ou généralisation.
- **Advisories** publiques : pour alerter la communauté sur des menaces spécifiques.

**Erreurs de communication à éviter** :
- **Sur-confidence** : présenter une hypothèse comme certitude. Calibrer.
- **Jargon excessif** : audience non-technique se perd. Ajuster le niveau.
- **Conclusions trop techniques** : ne pas traduire en action business.
- **Rigidité** : le rapport est un instantané, pas une vérité éternelle. Indiquer révisabilité.

### 28.8 Fil rouge — DARKSTREAM : la documentation finale

> **🌐 DARKSTREAM — Épisode 16 : la pochette de preuves**
>
> Après 6 semaines d'investigation, Lucas finalise la **pochette de preuves** de DARKSTREAM pour remise à Vectris et DGSI.
>
> **Contenu de la pochette** :
>
> 1. **Rapport principal** (42 pages, signature PGP de Lucas) — narration complète, analyse, recommandations.
> 2. **Annexe A : captures IndustrialLeaks** — 147 screenshots + HTML sources de tous les posts pertinents, chaque fichier horodaté et haché SHA-256. Index XLSX avec correspondance screenshots/horodatages.
> 3. **Annexe B : conversations XMPP avec aero_source** — export complet chiffré, hashé, horodaté. 18 échanges sur 4 semaines.
> 4. **Annexe C : échantillons reçus** — les 8 fichiers reçus, en archives chiffrées, avec hashes et analyses.
> 5. **Annexe D : analyse blockchain** — exports Chainalysis du cluster aero_source, graphes de relations, IoC (adresses crypto).
> 6. **Annexe E : logs Russian Market** — les 12 stealer logs Vectris identifiés, métadonnées et extraits pertinents.
> 7. **Annexe F : IoC structurés** — format MISP, prêt pour partage sectoriel après anonymisation.
> 8. **Annexe G : chain of custody** — liste chronologique de toutes les actions d'investigation, signées par Lucas avec horodatage qualifié.
> 9. **Annexe H : note méthodologique** — sources, outils, limites, biais.
>
> La pochette totale représente ~1,2 Go de données. Stockée sur share chiffré Athéna, accès contrôlé. Versions papier signées du rapport principal.
>
> Transmission : TLP:RED à Vectris (cellule de crise + RSSI), TLP:AMBER à la DGSI. La DGSI a indiqué qu'elle transmettra les éléments pertinents à ses partenaires internationaux (notamment si identifications complémentaires d'aero_source émergent via d'autres services).
>
> La solidité de cette pochette conditionne la solidité des actions défensives et coercitives qui en découleront. Si un jour aero_source est identifié physiquement et interpellé, les preuves collectées par Lucas pourront être remontées dans le dossier d'accusation. Si les données Vectris apparaissent ailleurs ultérieurement, la pochette fournira le baseline pour distinguer leak originel et recirculation.

---
