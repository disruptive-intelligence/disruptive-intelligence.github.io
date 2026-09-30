---
title: 'Chapitre 25 — Investigation dans un data leak : workflow'
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie V — Investigation, veille et collecte
  - index.md
---

Ce chapitre présente un workflow structuré pour investiguer une annonce de fuite de données. C'est l'une des situations les plus fréquentes pour un analyste CTI défensif — alerte de monitoring, il faut déterminer si la fuite est réelle, pertinente, et actionnable.

## 25.1 Le cadre de l'investigation

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

## 25.2 Étape 1 — Triage initial

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

## 25.3 Étape 2 — Profiling du vendeur

**Objectif** : comprendre qui pose l'annonce.

**Collecte** :

- Historique **sur le forum principal** : tous les posts du pseudo, dates, catégories, réponses reçues.
- **Cross-platform** : présence du pseudo sur d'autres forums, canaux Telegram, Jabber, etc. Ch.26 pour pivoting détaillé.
- **Style linguistique** : langue maternelle apparente, niveau technique, style de négociation.
- **Activité financière connue** : adresses crypto affichées, patterns de transactions visibles on-chain.
- **Relations** : qui vouche le vendeur ? qui achète ? avec qui interagit-il dans les threads ?

**Output** : fiche de profil du vendeur, 2-4 pages, avec observations et hypothèses initiales sur son positionnement dans l'écosystème.

## 25.4 Étape 3 — Acquisition d'échantillons

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

## 25.5 Étape 4 — Authentification

**Objectif** : déterminer si les données sont authentiques et proviennent de la victime annoncée.

**Techniques** :

**Métadonnées de fichiers**. PDF, DOCX, XLSX — extraction des métadonnées avec exiftool. Cherche : auteur, entreprise, chemin de création, horodatages, révisions. Un document avec métadonnées « Created: Vectris Aerospace, Author: M. Dubois, 2025-11 » cohérentes avec l'entreprise cible est fort.

**Cohérence de contenu**. Les noms d'employés dans le fichier correspondent-ils à des employés réels (vérifiables sur LinkedIn, site corporate) ? Les références projets correspondent-elles à des projets connus ? Les références fournisseurs sont-elles plausibles ? Les numéros de révision, codes internes, formats de référence correspondent-ils aux conventions documentées de l'entreprise ?

**Markers internes**. Certaines entreprises matures incluent des **markers intentionnels** dans leurs documents sensibles — fausses entrées dans les bases fournisseurs, employés fictifs dans les annuaires internes, entreprises fictives dans les listes de partenaires. La présence de ces markers dans un dump confirme qu'il provient bien de l'entreprise. **Vectris avait un tel marker** (fictif) dans sa liste fournisseurs — retrouvé dans l'échantillon DARKSTREAM.

**Corrélation avec données publiques**. Si le dump contient des éléments disponibles publiquement (communiqués, rapports annuels, documents marketing), les comparer. Un dump qui contient un document public identique à la version publique n'ajoute rien ; un dump qui contient un brouillon du communiqué postérieur à une version précédente — et ce brouillon est antérieur à la publication officielle — atteste d'un accès interne.

**Demande d'échantillon ciblé**. Demander au vendeur un fichier spécifique contenant un nom connu. S'il peut le fournir, l'authenticité est très probable. S'il refuse ou fournit quelque chose d'incohérent, suspicion.

**Cross-check forensics interne**. Transmettre les échantillons à l'équipe IR de la victime. Ils peuvent confirmer l'authenticité par comparaison avec leurs bases internes.

**Output** : niveau de confiance dans l'authenticité (scale : non-authentique / probable / très probable / confirmé), argumentaire détaillé.

## 25.6 Étape 5 — Cartographie de l'écosystème

Une fois l'authenticité évaluée, cartographier le contexte.

**Qui est l'auteur initial du vol** ? Le vendeur sur le forum est-il l'attaquant, un courtier, un acheteur final revendeur ?

**Y a-t-il d'autres traces** ? Le même dump est-il proposé sur d'autres forums ? Circulation privée ? Tentatives de chantage direct de la victime ?

**Qui sont les acheteurs potentiels** ? Concurrents ? Acteurs étatiques ? Groupes cybercriminels cherchant un levier de ransomware ? IndustrialLeaks ciblant une clientèle spécifique ?

**Quel est le vecteur d'entrée** ? Corrélation avec logs internes, stealer logs sur la victime, exploits publics de la période, TTP d'un groupe APT connu.

**Quelle est la chronologie** ? Dates de compromission, d'exfiltration, de mise en vente — compatibles avec les traces forensiques internes ?

## 25.7 Étape 6 — Analyse des flux financiers

Si le vendeur affiche une adresse crypto (pour recevoir paiement), cette adresse est une mine de renseignement.

**Capture de l'adresse**. Copier exactement depuis la source.

**Traçage on-chain**. Analyse via Chainalysis Reactor, TRM Labs Forensics, Elliptic Investigator, ou équivalent open source (Breadcrumbs, OXT).

**Questions analytiques** :

- L'adresse a-t-elle reçu des paiements ? De qui (quels autres wallets) ?
- L'adresse est-elle connue comme liée à d'autres opérations (blacklistée par Chainalysis) ?
- Les fonds ont-ils été déplacés ? Vers où (mixer, exchange, autre wallet) ?
- Cluster d'adresses connecté : des dizaines d'autres adresses peuvent être contrôlées par le même acteur.

Voir Ch.31 pour détails du traçage crypto.

## 25.8 Étape 7 — Production du rapport

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

## 25.9 Fil rouge — DARKSTREAM : rapport intermédiaire

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
